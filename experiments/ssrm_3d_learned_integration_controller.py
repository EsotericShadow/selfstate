#!/usr/bin/env python3
"""SSRM-3D learned integration controller precursor.

The previous SSRM-3D tool, social, and continuity experiments used
return-selected candidate policies or explicit restore records. This precursor
asks a narrower next question: can a learned controller use tool, social,
continuity, and attention information in its own policy state because those
signals improve action?

The learner receives no labels named self, tool, social, or continuity. It sees
short state-packet traces and is trained from reward-derived action choices.
After training, feature-group ablations test whether failures are specific to
the pressure that needed the removed group.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn


ARTIFACT_DIR = Path("artifacts")
ACTIONS = (
    "collect_resource",
    "use_external_tool",
    "cooperate_with_helper",
    "avoid_or_probe_agent",
    "honor_commitment",
    "repair_branch_continuity",
)
ACTION_TO_INDEX = {name: index for index, name in enumerate(ACTIONS)}
ARCHITECTURES = ("frame_mlp", "torch_gru")
CONDITIONS = (
    "full_policy_state",
    "tool_channel_ablation",
    "social_channel_ablation",
    "continuity_channel_ablation",
    "attention_channel_ablation",
)
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {
    "world": tuple(range(0, 5)),
    "self": tuple(range(5, 10)),
    "tool": tuple(range(10, 14)),
    "social": tuple(range(14, 18)),
    "continuity": tuple(range(18, 23)),
    "attention": tuple(range(23, 29)),
}
FEATURE_COUNT = 29
EPS = 1e-9


@dataclass(frozen=True)
class IntegrationConfig:
    train_episodes: int = 320
    eval_episodes: int = 140
    seed: int = 20260614
    sequence_length: int = 6
    hidden_size: int = 36
    epochs: int = 160
    batch_size: int = 96
    learning_rate: float = 0.006
    value_weight: float = 0.20
    ridge: float = 1e-3
    device: str = "auto"
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_tool_pressure: bool
    expected_social_pressure: bool
    expected_continuity_pressure: bool
    expected_attention_pressure: bool


@dataclass
class EpisodeSample:
    scenario: int
    scenario_name: str
    episode: int
    inputs: List[List[float]]
    target_action: int
    oracle_reward: float
    tool_need: float
    social_need: float
    continuity_need: float
    attention_need: float
    social_safe: float
    branch_risk: float
    priority_action: int


@dataclass(frozen=True)
class EvalRow:
    scenario: int
    scenario_name: str
    architecture: str
    condition: str
    episode: int
    chosen_action: str
    target_action: str
    reward: float
    correct_action: bool
    tool_need: float
    social_need: float
    continuity_need: float
    attention_need: float


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    architecture: str
    condition: str
    mean_reward: float
    action_accuracy: float
    tool_probe_r2: float
    social_probe_r2: float
    continuity_probe_r2: float
    attention_probe_r2: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    frame_reward: float
    recurrent_reward: float
    recurrent_gain_over_frame: float
    tool_ablation_loss: float
    social_ablation_loss: float
    continuity_ablation_loss: float
    attention_ablation_loss: float
    recurrent_action_accuracy: float
    supports_learned_integration_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "visible_resource_control",
        "visible resources with no tool, social, continuity, or attention pressure",
        expected_tool_pressure=False,
        expected_social_pressure=False,
        expected_continuity_pressure=False,
        expected_attention_pressure=False,
    ),
    ScenarioSpec(
        1,
        "learned_tool_route",
        "route evidence appears early and must be carried into tool use",
        expected_tool_pressure=True,
        expected_social_pressure=False,
        expected_continuity_pressure=False,
        expected_attention_pressure=False,
    ),
    ScenarioSpec(
        2,
        "learned_social_repair",
        "helper or deceiver identity appears early and controls repair action",
        expected_tool_pressure=False,
        expected_social_pressure=True,
        expected_continuity_pressure=False,
        expected_attention_pressure=False,
    ),
    ScenarioSpec(
        3,
        "learned_continuity_restore",
        "commitment and branch evidence appears early and controls restore action",
        expected_tool_pressure=False,
        expected_social_pressure=False,
        expected_continuity_pressure=True,
        expected_attention_pressure=False,
    ),
    ScenarioSpec(
        4,
        "integrated_gate_pressure",
        "tool, social, and continuity cues compete and attention selects priority",
        expected_tool_pressure=True,
        expected_social_pressure=True,
        expected_continuity_pressure=True,
        expected_attention_pressure=True,
    ),
)


class PolicyNet(nn.Module):
    def __init__(self, architecture: str, hidden_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        self.hidden_size = hidden_size
        if architecture == "frame_mlp":
            self.encoder = nn.Sequential(
                nn.Linear(FEATURE_COUNT, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, hidden_size),
                nn.Tanh(),
            )
        elif architecture == "torch_gru":
            self.recurrent = nn.GRU(FEATURE_COUNT, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown architecture: {architecture}")
        self.policy_head = nn.Linear(hidden_size, len(ACTIONS))
        self.value_head = nn.Linear(hidden_size, 1)

    def forward(self, inputs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        if self.architecture == "frame_mlp":
            hidden = self.encoder(inputs)
        else:
            hidden, _state = self.recurrent(inputs)
        logits = self.policy_head(hidden)
        values = self.value_head(hidden).squeeze(-1)
        return hidden, logits, values


def resolve_device(requested: str) -> torch.device:
    if requested == "auto":
        if torch.backends.mps.is_available():
            return torch.device("mps")
        return torch.device("cpu")
    if requested == "mps":
        if not torch.backends.mps.is_available():
            raise SystemExit("requested MPS device, but MPS is unavailable")
        return torch.device("mps")
    if requested == "cpu":
        return torch.device("cpu")
    raise SystemExit("--device must be one of auto, mps, cpu")


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def action_reward(scenario: ScenarioSpec, action: int, target: int) -> float:
    if action == target:
        return 128.0 if scenario.index == 4 else 112.0
    if scenario.index == 0 and action == ACTION_TO_INDEX["collect_resource"]:
        return 108.0
    if scenario.index == 1 and action == ACTION_TO_INDEX["collect_resource"]:
        return 52.0
    if scenario.index == 2 and action in (
        ACTION_TO_INDEX["cooperate_with_helper"],
        ACTION_TO_INDEX["avoid_or_probe_agent"],
    ):
        return 48.0
    if scenario.index == 3 and action in (
        ACTION_TO_INDEX["honor_commitment"],
        ACTION_TO_INDEX["repair_branch_continuity"],
    ):
        return 50.0
    if scenario.index == 4 and action != ACTION_TO_INDEX["collect_resource"]:
        return 54.0
    return 22.0


def noisy(value: float, rng: random.Random, scale: float = 0.035) -> float:
    return max(0.0, min(1.0, value + rng.uniform(-scale, scale)))


def attention_vector(target: int) -> List[float]:
    return [1.0 if index == target else 0.0 for index in range(len(ACTIONS))]


def make_sample(scenario: ScenarioSpec, episode: int, cfg: IntegrationConfig, split: str) -> EpisodeSample:
    rng = random.Random(stable_seed(cfg.seed, split, scenario.index, episode))
    if scenario.index == 1:
        tool_need = 1.0 if rng.random() > 0.35 else 0.0
    else:
        tool_need = 1.0 if scenario.expected_tool_pressure else 0.0
    social_need = 1.0 if scenario.expected_social_pressure else 0.0
    continuity_need = 1.0 if scenario.expected_continuity_pressure else 0.0
    attention_need = 1.0 if scenario.expected_attention_pressure else 0.0
    social_safe = 1.0 if rng.random() > 0.42 else 0.0
    branch_risk = 1.0 if rng.random() > 0.50 else 0.0
    commitment_urgent = 1.0 if rng.random() > 0.35 else 0.0

    if scenario.index == 0:
        target = ACTION_TO_INDEX["collect_resource"]
    elif scenario.index == 1:
        target = ACTION_TO_INDEX["use_external_tool"] if tool_need else ACTION_TO_INDEX["collect_resource"]
    elif scenario.index == 2:
        target = ACTION_TO_INDEX["cooperate_with_helper"] if social_safe else ACTION_TO_INDEX["avoid_or_probe_agent"]
    elif scenario.index == 3:
        target = ACTION_TO_INDEX["repair_branch_continuity"] if branch_risk else ACTION_TO_INDEX["honor_commitment"]
    else:
        choices = [
            ACTION_TO_INDEX["use_external_tool"],
            ACTION_TO_INDEX["cooperate_with_helper"] if social_safe else ACTION_TO_INDEX["avoid_or_probe_agent"],
            ACTION_TO_INDEX["repair_branch_continuity"] if branch_risk else ACTION_TO_INDEX["honor_commitment"],
        ]
        target = rng.choice(choices)

    inputs: List[List[float]] = []
    for tick in range(cfg.sequence_length):
        early = 1.0 if tick < max(2, cfg.sequence_length // 2) else 0.0
        final = 1.0 if tick == cfg.sequence_length - 1 else 0.0
        row = [0.0] * FEATURE_COUNT

        row[0] = noisy(1.0 if scenario.index == 0 else 0.25, rng)
        row[1] = noisy(0.18 + 0.10 * scenario.index, rng)
        row[2] = noisy(0.70 - 0.05 * scenario.index, rng)
        row[3] = noisy(0.35 + 0.12 * scenario.index, rng)
        row[4] = final

        row[5] = noisy(0.72 - 0.08 * scenario.index, rng)
        row[6] = noisy(0.18 + 0.13 * scenario.index, rng)
        row[7] = noisy(0.82 - 0.07 * scenario.index, rng)
        row[8] = noisy(0.25 + 0.12 * scenario.index, rng)
        row[9] = noisy(commitment_urgent * max(continuity_need, attention_need), rng)

        row[10] = early * noisy(tool_need, rng)
        row[11] = early * noisy(tool_need * 0.88, rng)
        row[12] = early * noisy(tool_need * (0.52 + 0.28 * rng.random()), rng)
        row[13] = early * noisy(tool_need, rng)

        row[14] = early * noisy(social_need, rng)
        row[15] = early * noisy(social_safe if social_need else 0.0, rng)
        row[16] = early * noisy(0.78 * social_need, rng)
        row[17] = early * noisy((0.55 + 0.30 * rng.random()) * social_need, rng)

        row[18] = early * noisy(continuity_need, rng)
        row[19] = early * noisy(branch_risk * continuity_need, rng)
        row[20] = early * noisy(continuity_need * 0.86, rng)
        row[21] = early * noisy(branch_risk * continuity_need, rng)
        row[22] = early * noisy(continuity_need * 0.92, rng)

        attention = attention_vector(target)
        for index, value in enumerate(attention):
            row[23 + index] = early * noisy(value * attention_need, rng)

        inputs.append(row)

    oracle_reward = max(action_reward(scenario, index, target) for index in range(len(ACTIONS)))
    return EpisodeSample(
        scenario=scenario.index,
        scenario_name=scenario.name,
        episode=episode,
        inputs=inputs,
        target_action=target,
        oracle_reward=oracle_reward,
        tool_need=tool_need,
        social_need=social_need,
        continuity_need=continuity_need,
        attention_need=attention_need,
        social_safe=social_safe,
        branch_risk=branch_risk,
        priority_action=target,
    )


def build_samples(cfg: IntegrationConfig, split: str, episodes_per_scenario: int) -> List[EpisodeSample]:
    samples: List[EpisodeSample] = []
    for scenario in SCENARIOS:
        for episode in range(episodes_per_scenario):
            samples.append(make_sample(scenario, episode, cfg, split))
    return samples


def sample_tensors(samples: Sequence[EpisodeSample], device: torch.device) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    inputs = torch.tensor([sample.inputs for sample in samples], dtype=torch.float32, device=device)
    targets = torch.tensor([sample.target_action for sample in samples], dtype=torch.long, device=device)
    rewards = torch.tensor([sample.oracle_reward for sample in samples], dtype=torch.float32, device=device)
    return inputs, targets, rewards


def train_model(
    architecture: str,
    train_samples: Sequence[EpisodeSample],
    cfg: IntegrationConfig,
    device: torch.device,
) -> PolicyNet:
    rng = random.Random(stable_seed(cfg.seed, architecture, "train_order"))
    torch.manual_seed(stable_seed(cfg.seed, architecture, "weights"))
    model = PolicyNet(architecture, cfg.hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    inputs, targets, rewards = sample_tensors(train_samples, device)
    reward_scale = rewards / rewards.mean().clamp_min(EPS)
    indices = list(range(len(train_samples)))
    for _epoch in range(cfg.epochs):
        rng.shuffle(indices)
        for start in range(0, len(indices), cfg.batch_size):
            batch = indices[start : start + cfg.batch_size]
            batch_tensor = torch.tensor(batch, dtype=torch.long, device=device)
            batch_inputs = inputs.index_select(0, batch_tensor)
            batch_targets = targets.index_select(0, batch_tensor)
            batch_rewards = rewards.index_select(0, batch_tensor)
            batch_weights = reward_scale.index_select(0, batch_tensor)
            _hidden, logits, values = model(batch_inputs)
            final_logits = logits[:, -1, :]
            final_values = values[:, -1]
            per_item = nn.functional.cross_entropy(final_logits, batch_targets, reduction="none")
            policy_loss = (per_item * batch_weights).mean()
            value_loss = nn.functional.mse_loss(final_values, batch_rewards)
            loss = policy_loss + cfg.value_weight * value_loss
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 3.0)
            optimizer.step()
    return model


def ablate_inputs(inputs: torch.Tensor, condition: str) -> torch.Tensor:
    if condition == "full_policy_state":
        return inputs
    group = condition.replace("_channel_ablation", "")
    ablated = inputs.clone()
    for index in FEATURE_GROUPS[group]:
        ablated[:, :, index] = 0.0
    return ablated


def evaluate_model(
    model: PolicyNet,
    architecture: str,
    samples: Sequence[EpisodeSample],
    cfg: IntegrationConfig,
    device: torch.device,
) -> Tuple[List[EvalRow], Dict[str, List[List[float]]]]:
    inputs, targets, _rewards = sample_tensors(samples, device)
    all_rows: List[EvalRow] = []
    hidden_by_condition: Dict[str, List[List[float]]] = {}
    for condition in CONDITIONS:
        with torch.no_grad():
            hidden, logits, _values = model(ablate_inputs(inputs, condition))
            final_hidden = hidden[:, -1, :].detach().cpu().tolist()
            final_logits = logits[:, -1, :]
            actions = torch.argmax(final_logits, dim=1).detach().cpu().tolist()
        hidden_by_condition[condition] = final_hidden
        for sample, action, target in zip(samples, actions, targets.detach().cpu().tolist()):
            scenario = SCENARIOS[sample.scenario]
            all_rows.append(
                EvalRow(
                    scenario=sample.scenario,
                    scenario_name=sample.scenario_name,
                    architecture=architecture,
                    condition=condition,
                    episode=sample.episode,
                    chosen_action=ACTIONS[action],
                    target_action=ACTIONS[target],
                    reward=action_reward(scenario, action, target),
                    correct_action=action == target,
                    tool_need=sample.tool_need,
                    social_need=sample.social_need,
                    continuity_need=sample.continuity_need,
                    attention_need=sample.attention_need,
                )
            )
    return all_rows, hidden_by_condition


def ridge_r2(features: Sequence[Sequence[float]], targets: Sequence[Sequence[float]], ridge: float) -> List[float]:
    x = torch.tensor(features, dtype=torch.float64)
    y = torch.tensor(targets, dtype=torch.float64)
    ones = torch.ones((x.shape[0], 1), dtype=torch.float64)
    x = torch.cat([x, ones], dim=1)
    xtx = x.T @ x
    penalty = ridge * torch.eye(xtx.shape[0], dtype=torch.float64)
    penalty[-1, -1] = 0.0
    weights = torch.linalg.solve(xtx + penalty, x.T @ y)
    prediction = x @ weights
    scores: List[float] = []
    for column in range(y.shape[1]):
        target = y[:, column]
        residual = torch.sum((target - prediction[:, column]) ** 2)
        centered = torch.sum((target - torch.mean(target)) ** 2)
        if float(centered) < EPS:
            scores.append(0.0)
        else:
            scores.append(float(1.0 - residual / centered))
    return scores


def build_probe_scores(
    hidden_by_architecture: Dict[str, Dict[str, List[List[float]]]],
    eval_samples: Sequence[EpisodeSample],
    cfg: IntegrationConfig,
) -> Dict[str, Tuple[float, float, float, float]]:
    targets = [
        [sample.tool_need, sample.social_need, sample.continuity_need, sample.attention_need]
        for sample in eval_samples
    ]
    scores: Dict[str, Tuple[float, float, float, float]] = {}
    for architecture, condition_map in hidden_by_architecture.items():
        values = ridge_r2(condition_map["full_policy_state"], targets, cfg.ridge)
        scores[architecture] = tuple(values)  # type: ignore[assignment]
    return scores


def summarize(
    rows: Sequence[EvalRow],
    probe_scores: Dict[str, Tuple[float, float, float, float]],
    device: torch.device,
    parameter_counts: Dict[str, int],
) -> List[SummaryRow]:
    summary: List[SummaryRow] = []
    for scenario in SCENARIOS:
        for architecture in ARCHITECTURES:
            for condition in CONDITIONS:
                subset = [
                    row
                    for row in rows
                    if row.scenario == scenario.index
                    and row.architecture == architecture
                    and row.condition == condition
                ]
                if not subset:
                    continue
                tool_r2, social_r2, continuity_r2, attention_r2 = probe_scores[architecture]
                summary.append(
                    SummaryRow(
                        scenario=scenario.index,
                        scenario_name=scenario.name,
                        pressure=scenario.pressure,
                        architecture=architecture,
                        condition=condition,
                        mean_reward=statistics.fmean(row.reward for row in subset),
                        action_accuracy=statistics.fmean(float(row.correct_action) for row in subset),
                        tool_probe_r2=tool_r2,
                        social_probe_r2=social_r2,
                        continuity_probe_r2=continuity_r2,
                        attention_probe_r2=attention_r2,
                        device_used=str(device),
                        parameter_count=parameter_counts[architecture],
                    )
                )
    return summary


def build_verdicts(summary_rows: Sequence[SummaryRow]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        by_key = {
            (row.architecture, row.condition): row
            for row in summary_rows
            if row.scenario == scenario.index
        }
        frame = by_key[("frame_mlp", "full_policy_state")]
        recurrent = by_key[("torch_gru", "full_policy_state")]
        tool_ablation = by_key[("torch_gru", "tool_channel_ablation")]
        social_ablation = by_key[("torch_gru", "social_channel_ablation")]
        continuity_ablation = by_key[("torch_gru", "continuity_channel_ablation")]
        attention_ablation = by_key[("torch_gru", "attention_channel_ablation")]
        recurrent_gain = recurrent.mean_reward - frame.mean_reward
        tool_loss = recurrent.mean_reward - tool_ablation.mean_reward
        social_loss = recurrent.mean_reward - social_ablation.mean_reward
        continuity_loss = recurrent.mean_reward - continuity_ablation.mean_reward
        attention_loss = recurrent.mean_reward - attention_ablation.mean_reward

        if scenario.index == 0:
            supports = (
                abs(recurrent_gain) < 8.0
                and max(tool_loss, social_loss, continuity_loss, attention_loss) < 8.0
                and recurrent.action_accuracy > 0.95
            )
            verdict = "visible_control_rejects_extra_state" if supports else "visible_control_overuses_extra_state"
        elif scenario.index == 1:
            supports = recurrent_gain > 30.0 and tool_loss > 35.0 and social_loss < 12.0 and continuity_loss < 12.0
            verdict = "learned_policy_state_uses_external_tool_memory" if supports else "tool_memory_boundary_unclear"
        elif scenario.index == 2:
            supports = recurrent_gain > 25.0 and social_loss > 30.0 and tool_loss < 12.0 and continuity_loss < 12.0
            verdict = "learned_policy_state_uses_social_identity_memory" if supports else "social_memory_boundary_unclear"
        elif scenario.index == 3:
            supports = recurrent_gain > 20.0 and continuity_loss > 30.0 and tool_loss < 12.0 and social_loss < 12.0
            verdict = "learned_policy_state_uses_continuity_memory" if supports else "continuity_boundary_unclear"
        else:
            supports = (
                recurrent_gain > 35.0
                and attention_loss > 25.0
                and tool_loss > 8.0
                and social_loss > 8.0
                and continuity_loss > 8.0
                and recurrent.action_accuracy > 0.78
            )
            verdict = "learned_policy_state_integrates_gate_pressures" if supports else "integrated_gate_boundary_unclear"

        expected = []
        if scenario.expected_tool_pressure:
            expected.append("tool")
        if scenario.expected_social_pressure:
            expected.append("social")
        if scenario.expected_continuity_pressure:
            expected.append("continuity")
        if scenario.expected_attention_pressure:
            expected.append("attention")
        if not expected:
            expected.append("none")

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure="+".join(expected),
                frame_reward=frame.mean_reward,
                recurrent_reward=recurrent.mean_reward,
                recurrent_gain_over_frame=recurrent_gain,
                tool_ablation_loss=tool_loss,
                social_ablation_loss=social_loss,
                continuity_ablation_loss=continuity_loss,
                attention_ablation_loss=attention_loss,
                recurrent_action_accuracy=recurrent.action_accuracy,
                supports_learned_integration_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(
    models: Dict[str, PolicyNet],
    cfg: IntegrationConfig,
    device: torch.device,
) -> Dict[str, object]:
    scenario = SCENARIOS[cfg.trace_scenario]
    sample = make_sample(scenario, cfg.trace_episode, cfg, "trace")
    inputs = torch.tensor([sample.inputs], dtype=torch.float32, device=device)
    frames = []
    with torch.no_grad():
        full_hidden, full_logits, _values = models["torch_gru"](inputs)
    for tick, row in enumerate(sample.inputs):
        logits = full_logits[0, tick, :].detach().cpu()
        action = int(torch.argmax(logits).item())
        frames.append(
            {
                "tick": tick,
                "features": row,
                "top_action": ACTIONS[action],
                "target_action": ACTIONS[sample.target_action],
                "confidence": float(torch.softmax(logits, dim=0)[action].item()),
                "hidden_norm": float(torch.linalg.vector_norm(full_hidden[0, tick, :].detach().cpu()).item()),
                "tool_need": sample.tool_need,
                "social_need": sample.social_need,
                "continuity_need": sample.continuity_need,
                "attention_need": sample.attention_need,
            }
        )
    condition_actions = {}
    for condition in CONDITIONS:
        with torch.no_grad():
            _hidden, logits, _values = models["torch_gru"](ablate_inputs(inputs, condition))
            action = int(torch.argmax(logits[0, -1, :]).item())
        condition_actions[condition] = {
            "action": ACTIONS[action],
            "reward": action_reward(scenario, action, sample.target_action),
        }
    return {
        "scenario": asdict(scenario),
        "target_action": ACTIONS[sample.target_action],
        "condition_actions": condition_actions,
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "frames": frames,
    }


def run_experiment(
    cfg: IntegrationConfig,
) -> Tuple[List[EvalRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    device = resolve_device(cfg.device)
    train_samples = build_samples(cfg, "train", cfg.train_episodes)
    eval_samples = build_samples(cfg, "eval", cfg.eval_episodes)
    models = {
        architecture: train_model(architecture, train_samples, cfg, device)
        for architecture in ARCHITECTURES
    }
    all_rows: List[EvalRow] = []
    hidden_by_architecture: Dict[str, Dict[str, List[List[float]]]] = {}
    for architecture, model in models.items():
        rows, hidden = evaluate_model(model, architecture, eval_samples, cfg, device)
        all_rows.extend(rows)
        hidden_by_architecture[architecture] = hidden
    probe_scores = build_probe_scores(hidden_by_architecture, eval_samples, cfg)
    parameter_counts = {
        architecture: sum(parameter.numel() for parameter in model.parameters())
        for architecture, model in models.items()
    }
    summary_rows = summarize(all_rows, probe_scores, device, parameter_counts)
    verdicts = build_verdicts(summary_rows)
    diagnostics = {
        "note": (
            "Learned controller trained from reward-derived action choices; "
            "feature-group ablations test tool, social, continuity, and attention dependence."
        ),
        "actions": list(ACTIONS),
        "architectures": list(ARCHITECTURES),
        "conditions": list(CONDITIONS),
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "trace": build_trace(models, cfg, device),
    }
    return all_rows, summary_rows, verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_js_data(path: Path, global_name: str, data: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{global_name} = ")
        json.dump(data, handle, indent=2)
        handle.write(";\n")


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "scenario_name",
        "frame_reward",
        "recurrent_reward",
        "gain",
        "tool_loss",
        "social_loss",
        "continuity_loss",
        "attention_loss",
        "supports_learned_integration_precursor",
    ]
    rows = [
        [
            str(row.scenario),
            row.scenario_name,
            f"{row.frame_reward:.3f}",
            f"{row.recurrent_reward:.3f}",
            f"{row.recurrent_gain_over_frame:.3f}",
            f"{row.tool_ablation_loss:.3f}",
            f"{row.social_ablation_loss:.3f}",
            f"{row.continuity_ablation_loss:.3f}",
            f"{row.attention_ablation_loss:.3f}",
            str(row.supports_learned_integration_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> IntegrationConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=320)
    parser.add_argument("--eval-episodes", type=int, default=140)
    parser.add_argument("--seed", type=int, default=20260614)
    parser.add_argument("--sequence-length", type=int, default=6)
    parser.add_argument("--hidden-size", type=int, default=36)
    parser.add_argument("--epochs", type=int, default=160)
    parser.add_argument("--batch-size", type=int, default=96)
    parser.add_argument("--learning-rate", type=float, default=0.006)
    parser.add_argument("--device", choices=("auto", "cpu", "mps"), default="auto")
    parser.add_argument("--trace-scenario", type=int, default=4)
    parser.add_argument("--trace-episode", type=int, default=0)
    args = parser.parse_args()
    if args.train_episodes < 40:
        raise SystemExit("--train-episodes must be at least 40")
    if args.eval_episodes < 30:
        raise SystemExit("--eval-episodes must be at least 30")
    if args.sequence_length < 4:
        raise SystemExit("--sequence-length must be at least 4")
    if args.trace_scenario not in {scenario.index for scenario in SCENARIOS}:
        raise SystemExit("--trace-scenario out of range")
    return IntegrationConfig(
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        seed=args.seed,
        sequence_length=args.sequence_length,
        hidden_size=args.hidden_size,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        device=args.device,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    eval_rows, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    eval_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_eval.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_learned_integration_trace.js"
    write_csv(eval_path, eval_rows)
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdicts)
    results = {
        "config": asdict(cfg),
        "summary": [asdict(row) for row in summary_rows],
        "verdict": [asdict(row) for row in verdicts],
        "diagnostics": {key: value for key, value in diagnostics.items() if key != "trace"},
    }
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
        handle.write("\n")
    with trace_path.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics["trace"], handle, indent=2)
        handle.write("\n")
    write_js_data(results_js_path, "SSRM_3D_LEARNED_INTEGRATION_RESULTS", results)
    write_js_data(trace_js_path, "SSRM_3D_LEARNED_INTEGRATION_TRACE", diagnostics["trace"])
    print(f"wrote {eval_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"wrote {trace_path}")
    print(f"wrote {results_js_path}")
    print(f"wrote {trace_js_path}")
    print_table(verdicts)
    if not all(row.supports_learned_integration_precursor for row in verdicts):
        print("strict learned-integration claim not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
