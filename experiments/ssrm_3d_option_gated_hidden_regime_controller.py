#!/usr/bin/env python3
"""Option-gated hidden-regime controller for SSRM-3D.

Report 95 showed a useful but partial learned result: a GRU controller acted
closed-loop and beat reactive survival, but its ablations did not prove clean
symptom-memory dependence. This experiment tries a more structured learned
controller: a neural policy predicts both an action and a response option from
the same observation stream, then the option prediction biases action selection
inside the closed-loop hidden-regime world.

The option heads are designed affordance groups, not discovered civilization.
The model still receives no hidden regime label as input.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import random
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
REPORT95_PATH = ROOT / "experiments" / "ssrm_3d_learned_hidden_regime_controller.py"


def load_report95_module():
    spec = importlib.util.spec_from_file_location("ssrm_learned_hidden", REPORT95_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {REPORT95_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p95 = load_report95_module()
h = p95.h

ACTIONS = p95.ACTIONS
ACTION_TO_INDEX = p95.ACTION_TO_INDEX
INDEX_TO_ACTION = p95.INDEX_TO_ACTION
FEATURE_COUNT = p95.FEATURE_COUNT
CHECKPOINTS = p95.CHECKPOINTS

OPTION_NAMES = (
    "survival",
    "water",
    "weather",
    "food",
    "tool",
    "social",
    "infrastructure",
    "teaching",
)
OPTION_TO_INDEX = {name: index for index, name in enumerate(OPTION_NAMES)}
SYMPTOM_OPTIONS = ("water", "weather", "food", "tool", "social")
ACTION_OPTIONS = {
    "rest": "survival",
    "harvest_water": "water",
    "harvest_food": "food",
    "inspect": "teaching",
    "construct": "infrastructure",
    "reinforce_shelter": "weather",
    "redesign_tools": "tool",
    "filter_water": "water",
    "quarantine": "water",
    "diversify_food": "food",
    "teach": "teaching",
    "mediate": "social",
}
OPTION_ACTIONS = {
    "survival": ("rest", "harvest_water", "harvest_food"),
    "water": ("filter_water", "quarantine", "harvest_water", "inspect"),
    "weather": ("reinforce_shelter", "construct", "rest", "inspect"),
    "food": ("diversify_food", "harvest_food", "inspect", "teach"),
    "tool": ("redesign_tools", "inspect", "construct", "teach"),
    "social": ("mediate", "teach", "inspect"),
    "infrastructure": ("construct", "reinforce_shelter", "redesign_tools"),
    "teaching": ("teach", "inspect", "mediate"),
}
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {
    **p95.FEATURE_GROUPS,
    "regime_signal": tuple(range(36, 46)),
}


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 16.0
    step_hours: float = 0.08
    population: int = 10
    epochs: int = 100
    hidden_size: int = 56
    learning_rate: float = 0.004
    option_loss_weight: float = 0.62
    option_bias: float = 1.35
    device: str = "auto"
    trace_seed: int = 20260803


@dataclass(frozen=True)
class TrainingRow:
    architecture: str
    train_loss: float
    action_accuracy: float
    option_accuracy: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class AblationRow:
    architecture: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_response_score: float
    response_loss: float
    mean_inference_score: float
    inference_loss: float


@dataclass(frozen=True)
class VerdictRow:
    option_gru_score: float
    option_frame_score: float
    reactive_score: float
    option_gru_gain_over_frame: float
    option_gru_gain_over_reactive: float
    regime_signal_ablation_loss: float
    infrastructure_ablation_loss: float
    social_culture_ablation_loss: float
    body_ablation_loss: float
    option_gru_inference_score: float
    option_gru_response_score: float
    option_gru_targeted_response_rate: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_option_gated_learning_precursor: bool
    supports_ablation_specificity: bool
    verdict: str


class OptionPolicyNet(nn.Module):
    def __init__(self, architecture: str, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        if architecture == "option_frame":
            self.frame = nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, hidden_size),
                nn.Tanh(),
            )
        elif architecture == "option_gru":
            self.recurrent = nn.GRU(input_size, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown architecture {architecture!r}")
        self.action_head = nn.Linear(hidden_size, len(ACTIONS))
        self.option_head = nn.Linear(hidden_size, len(OPTION_NAMES))

    def forward(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor | None]:
        if self.architecture == "option_frame":
            hidden = self.frame(x)
            return self.action_head(hidden), self.option_head(hidden), None
        hidden, next_state = self.recurrent(x, state)
        return self.action_head(hidden), self.option_head(hidden), next_state

    def step(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor | None]:
        if self.architecture == "option_frame":
            action_logits, option_logits, _ = self.forward(x)
            return action_logits, option_logits, None
        action_logits, option_logits, next_state = self.forward(x.unsqueeze(1), state)
        return action_logits[:, -1, :], option_logits[:, -1, :], next_state


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def resolve_device(requested: str) -> torch.device:
    return p95.resolve_device(requested)


def parse_seed_list(raw: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def option_for_sample(features: Sequence[float], action_index: int) -> int:
    symptoms = list(features[36:41])
    dominant_value = max(symptoms)
    if dominant_value >= 0.24:
        return OPTION_TO_INDEX[SYMPTOM_OPTIONS[symptoms.index(dominant_value)]]
    action = INDEX_TO_ACTION[int(action_index)]
    return OPTION_TO_INDEX[ACTION_OPTIONS[action]]


def sample_weight(features: Sequence[float], action_index: int, option_index: int) -> float:
    action = INDEX_TO_ACTION[int(action_index)]
    symptom_strength = max(float(value) for value in features[36:41])
    option_name = OPTION_NAMES[int(option_index)]
    weight = 1.0 + symptom_strength * 1.6
    if action in {"filter_water", "quarantine", "reinforce_shelter", "diversify_food", "redesign_tools", "mediate"}:
        weight += 1.15
    if option_name in {"water", "weather", "food", "tool", "social"}:
        weight += 0.55
    return weight


def derive_option_targets(train_x_raw: torch.Tensor, train_y: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
    option_targets = torch.zeros_like(train_y)
    weights = torch.zeros(train_y.shape, dtype=torch.float32)
    for seq in range(train_y.shape[0]):
        for step in range(train_y.shape[1]):
            features = train_x_raw[seq, step].tolist()
            action_index = int(train_y[seq, step].item())
            option_index = option_for_sample(features, action_index)
            option_targets[seq, step] = option_index
            weights[seq, step] = sample_weight(features, action_index, option_index)
    return option_targets, weights


def standardize(train_x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    return p95.standardize(train_x)


def train_option_controller(
    architecture: str,
    train_x: torch.Tensor,
    train_y: torch.Tensor,
    option_y: torch.Tensor,
    weights: torch.Tensor,
    cfg: Config,
    device: torch.device,
) -> Tuple[OptionPolicyNet, TrainingRow]:
    torch.manual_seed(20260803 + len(architecture) * 41)
    model = OptionPolicyNet(architecture, FEATURE_COUNT, cfg.hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    x = train_x.to(device)
    actions = train_y.to(device)
    options = option_y.to(device)
    sample_weights = weights.to(device)
    action_loss_fn = nn.CrossEntropyLoss(reduction="none")
    option_loss_fn = nn.CrossEntropyLoss(reduction="none")
    last_loss = 0.0
    for _ in range(cfg.epochs):
        optimizer.zero_grad(set_to_none=True)
        action_logits, option_logits, _ = model(x)
        action_loss = action_loss_fn(action_logits.reshape(-1, action_logits.shape[-1]), actions.reshape(-1)).reshape_as(actions)
        option_loss = option_loss_fn(option_logits.reshape(-1, option_logits.shape[-1]), options.reshape(-1)).reshape_as(options)
        loss = ((action_loss + cfg.option_loss_weight * option_loss) * sample_weights).mean()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
        last_loss = float(loss.detach().cpu().item())
    model.eval()
    with torch.no_grad():
        action_logits, option_logits, _ = model(x)
        action_accuracy = float((action_logits.argmax(dim=-1) == actions).float().mean().detach().cpu().item())
        option_accuracy = float((option_logits.argmax(dim=-1) == options).float().mean().detach().cpu().item())
    return model, TrainingRow(
        architecture=architecture,
        train_loss=last_loss,
        action_accuracy=action_accuracy,
        option_accuracy=option_accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def apply_feature_ablation(features: List[float], ablation: str) -> List[float]:
    if ablation == "none":
        return features
    out = list(features)
    group = FEATURE_GROUPS.get(ablation)
    if group is None:
        raise ValueError(f"unknown ablation {ablation!r}")
    for index in group:
        out[index] = 0.0
    return out


def option_action_bias(option_logits: torch.Tensor, cfg: Config) -> torch.Tensor:
    probabilities = torch.softmax(option_logits, dim=-1)
    bias = torch.zeros((option_logits.shape[0], len(ACTIONS)), dtype=option_logits.dtype, device=option_logits.device)
    for option_name, actions in OPTION_ACTIONS.items():
        option_index = OPTION_TO_INDEX[option_name]
        for action in actions:
            bias[:, ACTION_TO_INDEX[action]] += probabilities[:, option_index] * cfg.option_bias
    return bias


def choose_action(
    model: OptionPolicyNet,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    agent,
    world,
    signals: Dict[str, float],
    previous_action: int,
    state: torch.Tensor | None,
    cfg: Config,
    ablation: str,
) -> Tuple[str, int, str, torch.Tensor | None]:
    raw = apply_feature_ablation(p95.observation(agent, world, signals, previous_action), ablation)
    x = torch.tensor(raw, dtype=torch.float32).unsqueeze(0)
    x = (x - feature_mean) / feature_std
    x = x.to(device)
    with torch.no_grad():
        action_logits, option_logits, next_state = model.step(x, state)
    scores = action_logits + option_action_bias(option_logits, cfg)
    action_index = int(scores.argmax(dim=-1).item())
    option_index = int(option_logits.argmax(dim=-1).item())
    return INDEX_TO_ACTION[action_index], action_index, OPTION_NAMES[option_index], next_state


def run_option_episode(
    seed: int,
    architecture: str,
    model: OptionPolicyNet,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    cfg: Config,
    *,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[p95.EvalRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 223 + 29 + sum(ord(ch) for ch in architecture + ablation))
    agents = h.make_agents(rng, cfg.population)
    world = h.make_world(seed, rng)
    condition = p95.teacher_condition()
    h.current_agents = agents
    baseline = {
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "teaching": world.teaching,
        "sanitation": world.sanitation,
    }
    previous_actions = [ACTION_TO_INDEX["rest"] for _ in range(max(32, cfg.population + 8))]
    states: Dict[int, torch.Tensor | None] = {index: None for index in range(len(agents))}
    checkpoints = list(CHECKPOINTS)
    snapshots: List[Dict[str, object]] = []
    alive_at_12h: int | None = None
    no_major_before_12 = True
    last_option = "survival"

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        h.apply_baseline_environment(world, agents, condition, dt, rng)
        h.apply_hidden_regime(world, condition, dt)
        signals = p95.sensor_features(world, condition, rng)
        h.update_beliefs(world, condition, signals, dt)
        pressure = h.pressure_score(world, agents)
        world.pressure_integral = p95.clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
        h.update_agent_influence(agents, condition.reputation_influence)
        for index, agent in enumerate(list(agents)):
            if index >= len(previous_actions):
                previous_actions.append(ACTION_TO_INDEX["rest"])
                states[index] = None
            if not agent.alive or agent.child:
                continue
            action, action_index, option_name, next_state = choose_action(
                model,
                device,
                feature_mean,
                feature_std,
                agent,
                world,
                signals,
                previous_actions[index],
                states.get(index),
                cfg,
                ablation,
            )
            last_option = option_name
            states[index] = next_state
            h.apply_action(agent, world, condition, action, dt, rng)
            previous_actions[index] = action_index
        p95.apply_body_dynamics(world, agents, dt)
        before_count = len(agents)
        h.maybe_reproduce(world, agents, condition, rng, dt)
        if len(agents) > before_count:
            for index in range(before_count, len(agents)):
                previous_actions.append(ACTION_TO_INDEX["rest"])
                states[index] = None
        if world.time < 12.0 and h.regime_active(world):
            no_major_before_12 = False
        if alive_at_12h is None and world.time >= 12.0:
            alive_at_12h = len(h.living(agents))
        while checkpoints and world.time >= checkpoints[0] - 1e-9:
            if trace:
                snap = p95.trace_snapshot(world, agents, f"{checkpoints[0]:.1f}h")
                snap["last_option"] = last_option
                snapshots.append(snap)
            checkpoints.pop(0)

    row = p95.score_episode(seed, architecture, ablation, world, agents, baseline, alive_at_12h)
    row = p95.EvalRow(**{**asdict(row), "no_major_regime_before_12h": no_major_before_12})
    return row, snapshots


def make_ablations(summary: Sequence[p95.SummaryRow]) -> List[AblationRow]:
    full = p95.row_lookup(summary, "option_gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("regime_signal", "infrastructure", "social_culture", "body"):
        row = p95.row_lookup(summary, "option_gru", ablation)
        rows.append(
            AblationRow(
                architecture="option_gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_response_score=row.mean_response_score,
                response_loss=full.mean_response_score - row.mean_response_score,
                mean_inference_score=row.mean_inference_score,
                inference_loss=full.mean_inference_score - row.mean_inference_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[p95.SummaryRow], ablations: Sequence[AblationRow]) -> VerdictRow:
    recurrent = p95.row_lookup(summary, "option_gru", "none")
    frame = p95.row_lookup(summary, "option_frame", "none")
    reactive = p95.row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    supports_learning = (
        recurrent.no_major_regime_before_12h_rate == 1.0
        and recurrent.hidden_regime_after_12h_rate == 1.0
        and recurrent.mean_alive_at_12h >= 8.0
        and recurrent.mean_final_alive >= 7.0
        and recurrent.mean_long_horizon_score >= 0.58
        and recurrent.mean_response_score >= 0.50
        and recurrent.mean_development_score >= 0.20
        and recurrent.mean_long_horizon_score - reactive.mean_long_horizon_score >= 0.12
    )
    supports_ablation = (
        by_ablation["regime_signal"].response_loss >= 0.025
        and by_ablation["infrastructure"].score_loss >= 0.050
        and by_ablation["social_culture"].score_loss >= 0.010
    )
    if supports_learning and supports_ablation:
        verdict = "pass"
    elif supports_learning:
        verdict = "partial"
    else:
        verdict = "failed"
    return VerdictRow(
        option_gru_score=recurrent.mean_long_horizon_score,
        option_frame_score=frame.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        option_gru_gain_over_frame=recurrent.mean_long_horizon_score - frame.mean_long_horizon_score,
        option_gru_gain_over_reactive=recurrent.mean_long_horizon_score - reactive.mean_long_horizon_score,
        regime_signal_ablation_loss=by_ablation["regime_signal"].score_loss,
        infrastructure_ablation_loss=by_ablation["infrastructure"].score_loss,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        body_ablation_loss=by_ablation["body"].score_loss,
        option_gru_inference_score=recurrent.mean_inference_score,
        option_gru_response_score=recurrent.mean_response_score,
        option_gru_targeted_response_rate=recurrent.mean_targeted_response_rate,
        shock_gate_pass_rate=recurrent.no_major_regime_before_12h_rate,
        hidden_regime_rate=recurrent.hidden_regime_after_12h_rate,
        supports_option_gated_learning_precursor=supports_learning,
        supports_ablation_specificity=supports_ablation,
        verdict=verdict,
    )


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    p95.rows_to_csv(path, rows)


def write_json(path: Path, payload: object) -> None:
    p95.write_json(path, payload)


def write_js(path: Path, variable: str, payload: object) -> None:
    p95.write_js(path, variable, payload)


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device = resolve_device(cfg.device)
    p95_cfg = p95.Config(
        train_seeds=cfg.train_seeds,
        eval_seeds=cfg.eval_seeds,
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )
    train_x_raw, train_y = p95.generate_teacher_sequences(p95_cfg)
    option_y, sample_weights = derive_option_targets(train_x_raw, train_y)
    train_x, feature_mean, feature_std = standardize(train_x_raw)
    training_rows: List[TrainingRow] = []
    models: Dict[str, OptionPolicyNet] = {}
    for architecture in ("option_frame", "option_gru"):
        model, training_row = train_option_controller(architecture, train_x, train_y, option_y, sample_weights, cfg, device)
        models[architecture] = model
        training_rows.append(training_row)

    eval_rows: List[p95.EvalRow] = []
    trace: List[Dict[str, object]] = []
    for seed in cfg.eval_seeds:
        eval_rows.append(p95.run_scripted_episode(seed, p95_cfg, p95.reactive_condition(), "scripted", "reactive_survival_only"))
        for architecture, model in models.items():
            row, maybe_trace = run_option_episode(
                seed,
                architecture,
                model,
                device,
                feature_mean,
                feature_std,
                cfg,
                ablation="none",
                trace=(seed == cfg.trace_seed and architecture == "option_gru"),
            )
            eval_rows.append(row)
            if maybe_trace:
                trace = maybe_trace
        for ablation in ("regime_signal", "infrastructure", "social_culture", "body"):
            row, _ = run_option_episode(seed, "option_gru", models["option_gru"], device, feature_mean, feature_std, cfg, ablation=ablation)
            eval_rows.append(row)

    summary = p95.summarize(eval_rows)
    ablations = make_ablations(summary)
    verdict = verdict_from_summary(summary, ablations)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "learning_rate": cfg.learning_rate,
            "option_loss_weight": cfg.option_loss_weight,
            "option_bias": cfg.option_bias,
            "device": str(device),
            "trace_seed": cfg.trace_seed,
        },
        "actions": list(ACTIONS),
        "options": list(OPTION_NAMES),
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "training": [asdict(row) for row in training_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "option-gated closed-loop learned hidden-regime controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or return-trained deep RL",
            "label_discipline": "model observations contain symptoms and state, not hidden regime labels",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_option_gated_hidden_regime_controller"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), trace)
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_OPTION_GATED_HIDDEN_REGIME_CONTROLLER_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_OPTION_GATED_HIDDEN_REGIME_CONTROLLER_TRACE", trace)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725")
    parser.add_argument("--eval-seeds", default="20260803,20260804,20260805,20260806,20260807")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--hidden-size", type=int, default=56)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--option-loss-weight", type=float, default=0.62)
    parser.add_argument("--option-bias", type=float, default=1.35)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260803)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_seed_list(args.train_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        option_loss_weight=args.option_loss_weight,
        option_bias=args.option_bias,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"training": payload["training"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] in {"pass", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
