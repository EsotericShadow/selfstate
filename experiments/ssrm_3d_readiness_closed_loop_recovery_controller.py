#!/usr/bin/env python3
"""Closed-loop recovery training for the SSRM-3D readiness world.

Report 136 showed that plain imitation does not transfer the designed
environment-readiness behavior into robust 72h learned control. This benchmark
keeps that failed boundary intact and tests a narrower follow-up: let the
learner act, collect the off-trajectory states it creates, relabel those states
with the designed readiness controller, and retrain a recurrent policy.

This is DAgger-style closed-loop recovery supervision. It is not deep
reinforcement learning, subjective consciousness, or open-ended civilization.
A failed strong verdict remains a completed result and exits cleanly.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
import torch.nn.functional as F

import ssrm_3d_environment_readiness_maturation as env
import ssrm_3d_learned_environment_readiness_controller as learned


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = "ssrm_3d_readiness_closed_loop_recovery"
ABLATIONS = ("body", "infrastructure", "tools", "social_culture", "environment", "readiness", "previous_action")


@dataclass(frozen=True)
class Config:
    behavior_train_seeds: Sequence[int]
    recovery_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 52
    recovery_epochs: int = 42
    hidden_size: int = 72
    learning_rate: float = 0.0035
    recovery_learning_rate: float = 0.0022
    device: str = "cpu"
    trace_seed: int = 20261251


@dataclass(frozen=True)
class TrainingRow:
    pass_name: str
    architecture: str
    source: str
    train_loss: float
    train_accuracy: float
    weighted_accuracy: float
    device_used: str
    parameter_count: int
    train_sequences: int
    train_steps: int
    recovery_examples: int


@dataclass(frozen=True)
class CollectionRow:
    pass_name: str
    seed: int
    visited_sequences: int
    visited_steps: int
    teacher_student_disagreement: float
    mean_recovery_weight: float
    mean_state_readiness: float
    mean_survival_urgency: float
    final_student_alive: int
    final_student_readiness: float
    final_student_score: float


@dataclass(frozen=True)
class VerdictRow:
    recovery_score: float
    behavior_score: float
    frame_score: float
    designed_score: float
    reactive_score: float
    recovery_gain_over_behavior: float
    recovery_gain_over_reactive: float
    recovery_gap_to_designed: float
    recovery_gain_over_frame: float
    body_ablation_loss: float
    infrastructure_ablation_loss: float
    tools_ablation_loss: float
    social_culture_ablation_loss: float
    environment_ablation_loss: float
    readiness_ablation_loss: float
    previous_action_ablation_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    final_alive: float
    readiness_at_12h: float
    final_readiness: float
    knowledge_transfer: float
    final_pest_pressure: float
    final_structural_strain: float
    supports_closed_loop_recovery: bool
    supports_recurrent_recovery_gain: bool
    supports_ablation_specificity: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_seed_list(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def config_for_learned(cfg: Config) -> learned.Config:
    return learned.Config(
        train_seeds=tuple(cfg.behavior_train_seeds),
        eval_seeds=tuple(cfg.eval_seeds),
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def build_weighted_tensors(
    sequences: Sequence[Sequence[Sequence[float]]],
    labels: Sequence[Sequence[int]],
    weights: Sequence[Sequence[float]],
    device: torch.device,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    max_len = max(len(sequence) for sequence in sequences)
    x = torch.zeros((len(sequences), max_len, learned.FEATURE_COUNT), dtype=torch.float32)
    y = torch.full((len(sequences), max_len), -100, dtype=torch.long)
    mask = torch.zeros((len(sequences), max_len), dtype=torch.bool)
    weight_tensor = torch.zeros((len(sequences), max_len), dtype=torch.float32)
    for row, sequence in enumerate(sequences):
        if len(sequence) != len(labels[row]) or len(sequence) != len(weights[row]):
            raise RuntimeError("sequence, label, and weight lengths must match")
        seq_len = len(sequence)
        x[row, :seq_len, :] = torch.tensor(sequence, dtype=torch.float32)
        y[row, :seq_len] = torch.tensor(labels[row], dtype=torch.long)
        mask[row, :seq_len] = True
        weight_tensor[row, :seq_len] = torch.tensor(weights[row], dtype=torch.float32)
    return x.to(device), y.to(device), mask.to(device), weight_tensor.to(device)


def train_weighted_model(
    architecture: str,
    x: torch.Tensor,
    y: torch.Tensor,
    mask: torch.Tensor,
    weights: torch.Tensor,
    cfg: Config,
    device: torch.device,
    pass_name: str,
    source: str,
    epochs: int,
    learning_rate: float,
    seed_offset: int,
    recovery_examples: int,
) -> Tuple[learned.ControllerNet, TrainingRow]:
    torch.manual_seed(20261370 + seed_offset)
    model = learned.ControllerNet(architecture, learned.FEATURE_COUNT, cfg.hidden_size, len(learned.ACTIONS)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    active = y.reshape(-1) != -100
    flat_weights = weights.reshape(-1)
    for _ in range(epochs):
        model.train()
        optimizer.zero_grad()
        logits, _ = model(x)
        loss_values = F.cross_entropy(logits.reshape(-1, len(learned.ACTIONS)), y.reshape(-1), ignore_index=-100, reduction="none")
        loss = (loss_values[active] * flat_weights[active]).sum() / flat_weights[active].sum().clamp_min(1.0)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    model.eval()
    with torch.no_grad():
        logits, _ = model(x)
        loss_values = F.cross_entropy(logits.reshape(-1, len(learned.ACTIONS)), y.reshape(-1), ignore_index=-100, reduction="none")
        loss = (loss_values[active] * flat_weights[active]).sum() / flat_weights[active].sum().clamp_min(1.0)
        predictions = logits.argmax(dim=-1)
        correct = (predictions == y) & mask
        train_accuracy = correct.sum().item() / max(1, mask.sum().item())
        weighted_accuracy = (correct.float() * weights).sum().item() / max(1e-9, (mask.float() * weights).sum().item())
    return model, TrainingRow(
        pass_name=pass_name,
        architecture=architecture,
        source=source,
        train_loss=float(loss.item()),
        train_accuracy=float(train_accuracy),
        weighted_accuracy=float(weighted_accuracy),
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_sequences=int(x.shape[0]),
        train_steps=int(mask.sum().item()),
        recovery_examples=recovery_examples,
    )


def recovery_weight(agent: env.Agent, world: env.World) -> Tuple[float, float]:
    survival_urgency = max(
        agent.hunger,
        agent.thirst,
        1.0 - agent.health,
        agent.illness,
        agent.injury,
        max(0.0, 0.44 - world.food) * 1.4,
        max(0.0, 0.44 - world.water) * 1.4,
    )
    readiness_deficit = mean(
        max(0.0, 0.62 - value)
        for value in (
            world.fuel_reserve,
            world.seed_bank,
            world.building_blueprints,
            world.tool_blueprints,
            world.forecast_memory,
            world.apprenticeship,
        )
    )
    infrastructure_risk = max(world.pest_pressure, world.structural_strain, world.disease, world.contamination)
    post_gate = 1.0 if world.time >= 12.0 else 0.25
    weight = 1.0 + survival_urgency * 1.7 + readiness_deficit * 2.4 + infrastructure_risk * 1.4 + post_gate * 0.45
    return min(8.0, max(1.0, weight)), survival_urgency


def student_action(
    model: learned.ControllerNet,
    device: torch.device,
    features: List[float],
    recurrent_states: Dict[str, torch.Tensor],
    ident: str,
) -> str:
    model_features = torch.tensor([features], dtype=torch.float32, device=device)
    with torch.no_grad():
        if model.architecture == "gru":
            state = recurrent_states.get(ident)
            logits, next_state = model.step(model_features, state)
            if next_state is not None:
                recurrent_states[ident] = next_state.detach()
        else:
            logits, _ = model.step(model_features, None)
    return learned.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]


def collect_recovery_sequences(
    cfg: Config,
    model: learned.ControllerNet,
    device: torch.device,
    seeds: Sequence[int],
    pass_name: str,
) -> Tuple[List[List[List[float]]], List[List[int]], List[List[float]], List[CollectionRow]]:
    condition = env.CONDITIONS[0]
    sequences: Dict[str, List[List[float]]] = {}
    labels: Dict[str, List[int]] = {}
    weights: Dict[str, List[float]] = {}
    rows: List[CollectionRow] = []

    for seed in seeds:
        rng = random.Random(seed * 149 + sum(ord(ch) for ch in pass_name))
        agents = env.make_agents(rng, cfg.population)
        world = env.make_world(rng)
        baseline = learned.initial_baseline(world, cfg.population)
        previous_actions: Dict[str, int] = {}
        recurrent_states: Dict[str, torch.Tensor] = {}
        events: List[str] = []
        no_pre_gate_shock = True
        alive_at_12h = cfg.population
        at_12: Dict[str, float] = {}
        disagreements: List[float] = []
        local_weights: List[float] = []
        readiness_values: List[float] = []
        urgencies: List[float] = []

        def selector(
            agent: env.Agent,
            current_world: env.World,
            current_condition: env.Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            teacher = env.choose_action(agent, current_world, current_condition, current_rng)
            teacher_index = learned.ACTION_TO_INDEX.get(teacher, learned.DEFAULT_ACTION)
            action = student_action(model, device, features, recurrent_states, agent.ident)
            action_index = learned.ACTION_TO_INDEX.get(action, learned.DEFAULT_ACTION)
            weight, urgency = recovery_weight(agent, current_world)
            key = f"{pass_name}:{seed}:{agent.ident}"
            sequences.setdefault(key, []).append(features)
            labels.setdefault(key, []).append(teacher_index)
            weights.setdefault(key, []).append(weight)
            disagreements.append(1.0 if action_index != teacher_index else 0.0)
            local_weights.append(weight)
            readiness_values.append(env.environment_readiness(current_world))
            urgencies.append(urgency)
            return action

        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            learned.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            if world.time < 12.0 and world.major_shocks > 0:
                no_pre_gate_shock = False
            if world.time >= 12.0 and not at_12:
                alive_at_12h = len(env.living(agents))
                at_12 = {"readiness": env.environment_readiness(world)}

        episode = env.score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
        seed_keys = [key for key in sequences if key.startswith(f"{pass_name}:{seed}:")]
        rows.append(
            CollectionRow(
                pass_name=pass_name,
                seed=seed,
                visited_sequences=len(seed_keys),
                visited_steps=sum(len(sequences[key]) for key in seed_keys),
                teacher_student_disagreement=mean(disagreements),
                mean_recovery_weight=mean(local_weights),
                mean_state_readiness=mean(readiness_values),
                mean_survival_urgency=mean(urgencies),
                final_student_alive=episode.final_alive,
                final_student_readiness=episode.final_readiness,
                final_student_score=episode.maturation_score,
            )
        )

    keys = sorted(sequences)
    return [sequences[key] for key in keys], [labels[key] for key in keys], [weights[key] for key in keys], rows


def ablations_from_summary(summary: Sequence[learned.SummaryRow], controller: str) -> List[learned.AblationRow]:
    by_key = {(row.controller, row.ablation): row for row in summary}
    base_row = by_key[(controller, "none")]
    rows: List[learned.AblationRow] = []
    for ablation in ABLATIONS:
        row = by_key[(controller, ablation)]
        rows.append(
            learned.AblationRow(
                controller=controller,
                ablation=ablation,
                mean_score=row.mean_maturation_score,
                score_loss=base_row.mean_maturation_score - row.mean_maturation_score,
                mean_readiness_score=row.mean_readiness_score,
                readiness_loss=base_row.mean_readiness_score - row.mean_readiness_score,
                mean_development_score=row.mean_development_score,
                development_loss=base_row.mean_development_score - row.mean_development_score,
                mean_knowledge_score=row.mean_knowledge_score,
                knowledge_loss=base_row.mean_knowledge_score - row.mean_knowledge_score,
                mean_resilience_score=row.mean_resilience_score,
                resilience_loss=base_row.mean_resilience_score - row.mean_resilience_score,
                pest_pressure_delta=row.mean_final_pest_pressure - base_row.mean_final_pest_pressure,
                structural_strain_delta=row.mean_final_structural_strain - base_row.mean_final_structural_strain,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[learned.SummaryRow], ablations: Sequence[learned.AblationRow]) -> VerdictRow:
    by_key = {(row.controller, row.ablation): row for row in summary}
    recovery = by_key[("recovery_gru", "none")]
    behavior = by_key[("behavior_gru", "none")]
    frame = by_key[("frame_mlp", "none")]
    designed = by_key[("designed", "none")]
    reactive = by_key[("reactive", "none")]
    losses = {row.ablation: row.score_loss for row in ablations}
    closed_loop_recovery = (
        recovery.shock_gate_pass_rate == 1.0
        and recovery.post_gate_shock_rate == 1.0
        and recovery.mean_alive_at_12h >= 12.0
        and recovery.mean_maturation_score - behavior.mean_maturation_score >= 0.04
        and recovery.mean_maturation_score - reactive.mean_maturation_score >= 0.14
        and recovery.mean_final_readiness - behavior.mean_final_readiness >= 0.035
        and recovery.mean_final_alive > behavior.mean_final_alive
        and designed.mean_maturation_score - recovery.mean_maturation_score <= 0.62
    )
    recurrent_gain = recovery.mean_maturation_score > frame.mean_maturation_score and recovery.mean_maturation_score > behavior.mean_maturation_score
    ablation_specific = (
        losses["body"] >= 0.010
        and losses["infrastructure"] >= 0.010
        and losses["tools"] >= 0.010
        and losses["environment"] >= 0.010
        and losses["readiness"] >= 0.010
    )
    return VerdictRow(
        recovery_score=recovery.mean_maturation_score,
        behavior_score=behavior.mean_maturation_score,
        frame_score=frame.mean_maturation_score,
        designed_score=designed.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        recovery_gain_over_behavior=recovery.mean_maturation_score - behavior.mean_maturation_score,
        recovery_gain_over_reactive=recovery.mean_maturation_score - reactive.mean_maturation_score,
        recovery_gap_to_designed=designed.mean_maturation_score - recovery.mean_maturation_score,
        recovery_gain_over_frame=recovery.mean_maturation_score - frame.mean_maturation_score,
        body_ablation_loss=losses["body"],
        infrastructure_ablation_loss=losses["infrastructure"],
        tools_ablation_loss=losses["tools"],
        social_culture_ablation_loss=losses["social_culture"],
        environment_ablation_loss=losses["environment"],
        readiness_ablation_loss=losses["readiness"],
        previous_action_ablation_loss=losses["previous_action"],
        shock_gate_pass_rate=recovery.shock_gate_pass_rate,
        post_gate_shock_rate=recovery.post_gate_shock_rate,
        survival_at_12h=recovery.mean_alive_at_12h,
        final_alive=recovery.mean_final_alive,
        readiness_at_12h=recovery.mean_readiness_at_12h,
        final_readiness=recovery.mean_final_readiness,
        knowledge_transfer=recovery.mean_knowledge_transfer,
        final_pest_pressure=recovery.mean_final_pest_pressure,
        final_structural_strain=recovery.mean_final_structural_strain,
        supports_closed_loop_recovery=closed_loop_recovery,
        supports_recurrent_recovery_gain=recurrent_gain,
        supports_ablation_specificity=ablation_specific,
        verdict="pass" if closed_loop_recovery and recurrent_gain and ablation_specific else "partial_or_failed",
    )


def evaluate_models(
    cfg: Config,
    device: torch.device,
    frame_model: learned.ControllerNet,
    behavior_model: learned.ControllerNet,
    recovery_model: learned.ControllerNet,
) -> Tuple[List[learned.EvalRow], List[learned.SummaryRow], List[learned.AblationRow], VerdictRow, env.Trace]:
    learned_cfg = config_for_learned(cfg)
    eval_rows: List[learned.EvalRow] = []
    trace = env.Trace(seed=cfg.trace_seed, condition="recovery_gru:none")
    controllers = (
        ("designed", None, "none"),
        ("reactive", None, "none"),
        ("frame_mlp", frame_model, "none"),
        ("behavior_gru", behavior_model, "none"),
        ("recovery_gru", recovery_model, "none"),
    )
    for seed in cfg.eval_seeds:
        for controller, model, ablation in controllers:
            row, maybe_trace = learned.run_controller_episode(
                seed,
                learned_cfg,
                controller,
                model,
                device,
                ablation=ablation,
                trace=(seed == cfg.trace_seed and controller == "recovery_gru" and ablation == "none"),
            )
            eval_rows.append(row)
            if maybe_trace.frames:
                trace = maybe_trace
        for ablation in ABLATIONS:
            row, _ = learned.run_controller_episode(seed, learned_cfg, "recovery_gru", recovery_model, device, ablation=ablation)
            eval_rows.append(row)
    summary = learned.summarize(eval_rows)
    ablations = ablations_from_summary(summary, "recovery_gru")
    verdict = verdict_from_summary(summary, ablations)
    return eval_rows, summary, ablations, verdict, trace


def write_artifacts(
    cfg: Config,
    training: Sequence[TrainingRow],
    collection: Sequence[CollectionRow],
    eval_rows: Sequence[learned.EvalRow],
    summary: Sequence[learned.SummaryRow],
    ablations: Sequence[learned.AblationRow],
    verdict: VerdictRow,
    trace: env.Trace,
) -> Dict[str, object]:
    payload = {
        "config": asdict(cfg),
        "feature_names": learned.FEATURE_NAMES,
        "feature_groups": {key: list(value) for key, value in learned.FEATURE_GROUPS.items()},
        "actions": list(learned.ACTIONS),
        "training": [asdict(row) for row in training],
        "collection": [asdict(row) for row in collection],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "closed-loop recovery supervision for the learned environment-readiness controller",
            "method": "teacher traces plus two student-visited recovery passes with consequence-weighted labels",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
        },
    }
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_training.csv", training)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_collection.csv", collection)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", eval_rows)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_ablations.csv", ablations)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    learned.write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    learned.write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", asdict(trace))
    learned.write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_READINESS_CLOSED_LOOP_RECOVERY_RESULTS", payload)
    learned.write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_READINESS_CLOSED_LOOP_RECOVERY_TRACE", asdict(trace))
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device = learned.resolve_device(cfg.device)
    learned_cfg = config_for_learned(cfg)
    teacher_sequences, teacher_labels = learned.collect_sequences(learned_cfg)
    teacher_weights = [[1.0 for _ in labels] for labels in teacher_labels]

    x, y, mask, weights = build_weighted_tensors(teacher_sequences, teacher_labels, teacher_weights, device)
    training_rows: List[TrainingRow] = []
    frame_model, row = train_weighted_model(
        "frame_mlp",
        x,
        y,
        mask,
        weights,
        cfg,
        device,
        "behavior",
        "designed_teacher_traces",
        cfg.epochs,
        cfg.learning_rate,
        0,
        0,
    )
    training_rows.append(row)
    behavior_model, row = train_weighted_model(
        "gru",
        x,
        y,
        mask,
        weights,
        cfg,
        device,
        "behavior",
        "designed_teacher_traces",
        cfg.epochs,
        cfg.learning_rate,
        17,
        0,
    )
    training_rows.append(row)

    pass1_sequences, pass1_labels, pass1_weights, pass1_rows = collect_recovery_sequences(
        cfg, behavior_model, device, cfg.recovery_seeds, "student_recovery_1"
    )
    aggregate_sequences = list(teacher_sequences) + pass1_sequences
    aggregate_labels = list(teacher_labels) + pass1_labels
    aggregate_weights = list(teacher_weights) + pass1_weights
    x1, y1, mask1, weights1 = build_weighted_tensors(aggregate_sequences, aggregate_labels, aggregate_weights, device)
    recovery_stage1, row = train_weighted_model(
        "gru",
        x1,
        y1,
        mask1,
        weights1,
        cfg,
        device,
        "recovery_stage_1",
        "teacher_traces_plus_student_visited_states",
        cfg.recovery_epochs,
        cfg.recovery_learning_rate,
        137,
        sum(len(labels) for labels in pass1_labels),
    )
    training_rows.append(row)

    shifted_seeds = tuple(seed + 1000 for seed in cfg.recovery_seeds)
    pass2_sequences, pass2_labels, pass2_weights, pass2_rows = collect_recovery_sequences(
        cfg, recovery_stage1, device, shifted_seeds, "student_recovery_2"
    )
    aggregate_sequences = aggregate_sequences + pass2_sequences
    aggregate_labels = aggregate_labels + pass2_labels
    aggregate_weights = aggregate_weights + pass2_weights
    x2, y2, mask2, weights2 = build_weighted_tensors(aggregate_sequences, aggregate_labels, aggregate_weights, device)
    recovery_model, row = train_weighted_model(
        "gru",
        x2,
        y2,
        mask2,
        weights2,
        cfg,
        device,
        "recovery_final",
        "teacher_traces_plus_two_student_recovery_passes",
        cfg.recovery_epochs,
        cfg.recovery_learning_rate,
        197,
        sum(len(labels) for labels in pass1_labels) + sum(len(labels) for labels in pass2_labels),
    )
    training_rows.append(row)

    eval_rows, summary, ablations, verdict, trace = evaluate_models(cfg, device, frame_model, behavior_model, recovery_model)
    return write_artifacts(cfg, training_rows, pass1_rows + pass2_rows, eval_rows, summary, ablations, verdict, trace)


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--behavior-train-seeds", default="20261211,20261212,20261213,20261214,20261215,20261216")
    parser.add_argument("--recovery-seeds", default="20261231,20261232,20261233")
    parser.add_argument("--eval-seeds", default="20261251,20261252,20261253,20261254,20261255")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=52)
    parser.add_argument("--recovery-epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=72)
    parser.add_argument("--learning-rate", type=float, default=0.0035)
    parser.add_argument("--recovery-learning-rate", type=float, default=0.0022)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--trace-seed", type=int, default=20261251)
    args = parser.parse_args()
    return Config(
        behavior_train_seeds=parse_seed_list(args.behavior_train_seeds),
        recovery_seeds=parse_seed_list(args.recovery_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        recovery_epochs=args.recovery_epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        recovery_learning_rate=args.recovery_learning_rate,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(
        json.dumps(
            {
                "verdict": payload["verdict"],
                "training": payload["training"],
                "collection": payload["collection"],
                "summary": payload["summary"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
