#!/usr/bin/env python3
"""No-leak randomized integration sweep for SSRM-3D packet controllers.

Report 69 showed a useful bridge, but it still supplied one scenario identity
per pressure family. This follow-up removes that shortcut. Each training run
receives mixed episodes where tool, social, continuity, and attention pressure
combinations are randomized. The packet contains no scenario id feature.

The test remains a packet-level precursor, not open-ended tool/social discovery.
It asks whether a recurrent policy can carry early pressure evidence when the
final frame no longer contains it, and whether ablations fail by pressure group
across several seeds.
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
CASE_CYCLE = (
    "control",
    "control",
    "single_tool",
    "single_social",
    "single_continuity",
    "integrated_random",
    "integrated_random",
    "integrated_random",
    "integrated_random",
)
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {
    "world": tuple(range(0, 5)),
    "self": tuple(range(5, 10)),
    "tool": tuple(range(10, 14)),
    "social": tuple(range(14, 18)),
    "continuity": tuple(range(18, 23)),
    "attention": tuple(range(23, 28)),
}
FEATURE_COUNT = 28
EPS = 1e-9


@dataclass(frozen=True)
class SweepConfig:
    seeds: Tuple[int, ...] = (20260615, 20260616, 20260617, 20260618, 20260619)
    train_episodes: int = 1200
    eval_episodes: int = 400
    sequence_length: int = 6
    hidden_size: int = 64
    epochs: int = 400
    batch_size: int = 128
    learning_rate: float = 0.005
    value_weight: float = 0.18
    device: str = "cpu"
    trace_seed: int = 20260615
    trace_case: str = "integrated_social"


@dataclass(frozen=True)
class EpisodeSample:
    seed: int
    split: str
    episode: int
    case_type: str
    inputs: List[List[float]]
    target_action: int
    oracle_reward: float
    tool_active: float
    tool_required: float
    social_active: float
    continuity_active: float
    attention_active: float
    priority_group: str
    social_safe: float
    branch_risk: float
    active_count: int


@dataclass(frozen=True)
class EvalRow:
    seed: int
    case_type: str
    architecture: str
    condition: str
    episode: int
    chosen_action: str
    target_action: str
    reward: float
    correct_action: bool
    tool_active: float
    tool_required: float
    social_active: float
    continuity_active: float
    attention_active: float
    priority_group: str


@dataclass(frozen=True)
class SummaryRow:
    seed: int
    case_type: str
    architecture: str
    condition: str
    mean_reward: float
    action_accuracy: float


@dataclass(frozen=True)
class SeedVerdictRow:
    seed: int
    case_type: str
    frame_reward: float
    recurrent_reward: float
    recurrent_gain_over_frame: float
    tool_ablation_loss: float
    social_ablation_loss: float
    continuity_ablation_loss: float
    attention_ablation_loss: float
    recurrent_action_accuracy: float
    supports_no_leak_bridge: bool
    verdict: str


@dataclass(frozen=True)
class VerdictRow:
    case_type: str
    seeds_tested: int
    seeds_supported: int
    support_rate: float
    min_gain_margin: float
    min_relevant_ablation_margin: float
    max_irrelevant_ablation_loss: float
    supports_no_leak_integration: bool
    verdict: str


class PolicyNet(nn.Module):
    def __init__(self, architecture: str, hidden_size: int) -> None:
        super().__init__()
        self.architecture = architecture
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


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


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


def noisy(value: float, rng: random.Random, scale: float = 0.035) -> float:
    return max(0.0, min(1.0, value + rng.uniform(-scale, scale)))


def choose_case(episode: int) -> str:
    return CASE_CYCLE[episode % len(CASE_CYCLE)]


def action_family(action: int) -> str:
    if action == ACTION_TO_INDEX["use_external_tool"]:
        return "tool"
    if action in (ACTION_TO_INDEX["cooperate_with_helper"], ACTION_TO_INDEX["avoid_or_probe_agent"]):
        return "social"
    if action in (ACTION_TO_INDEX["honor_commitment"], ACTION_TO_INDEX["repair_branch_continuity"]):
        return "continuity"
    return "world"


def is_integrated_case(case_type: str) -> bool:
    return case_type.startswith("integrated_")


def action_reward(case_type: str, action: int, target: int) -> float:
    if action == target:
        return 128.0 if is_integrated_case(case_type) else 112.0
    if is_integrated_case(case_type):
        return 30.0 if action != ACTION_TO_INDEX["collect_resource"] else 18.0
    if case_type == "control":
        return 96.0 if action == ACTION_TO_INDEX["collect_resource"] else 20.0
    if action_family(action) == action_family(target):
        return 52.0
    return 18.0


def build_pressure_state(episode: int, case_type: str) -> Tuple[int, int, int, str]:
    if case_type == "control":
        return 0, 0, 0, "world"
    if case_type == "single_tool":
        return 1, 0, 0, "tool"
    if case_type == "single_social":
        return 0, 1, 0, "social"
    if case_type == "single_continuity":
        return 0, 0, 1, "continuity"

    patterns = (
        (1, 1, 0, "tool"),
        (1, 1, 0, "social"),
        (1, 0, 1, "tool"),
        (1, 0, 1, "continuity"),
        (0, 1, 1, "social"),
        (0, 1, 1, "continuity"),
        (1, 1, 1, "tool"),
        (1, 1, 1, "social"),
        (1, 1, 1, "continuity"),
    )
    return patterns[(episode // len(CASE_CYCLE)) % len(patterns)]


def target_for_state(
    priority_group: str,
    tool_required: float,
    social_safe: float,
    branch_risk: float,
) -> int:
    if priority_group == "tool":
        return ACTION_TO_INDEX["use_external_tool"] if tool_required else ACTION_TO_INDEX["collect_resource"]
    if priority_group == "social":
        return ACTION_TO_INDEX["cooperate_with_helper"] if social_safe else ACTION_TO_INDEX["avoid_or_probe_agent"]
    if priority_group == "continuity":
        return ACTION_TO_INDEX["repair_branch_continuity"] if branch_risk else ACTION_TO_INDEX["honor_commitment"]
    return ACTION_TO_INDEX["collect_resource"]


def make_sample(seed: int, split: str, episode: int, cfg: SweepConfig) -> EpisodeSample:
    rng = random.Random(stable_seed(seed, split, episode))
    raw_case = choose_case(episode)
    tool_active, social_active, continuity_active, priority_group = build_pressure_state(episode, raw_case)
    case_type = f"integrated_{priority_group}" if raw_case == "integrated_random" else raw_case
    active_count = tool_active + social_active + continuity_active
    attention_active = 1 if active_count > 1 else 0
    tool_required = 1.0 if tool_active and rng.random() > 0.50 else 0.0
    social_safe = 1.0 if rng.random() > 0.50 else 0.0
    branch_risk = 1.0 if rng.random() > 0.50 else 0.0
    target = target_for_state(priority_group, tool_required, social_safe, branch_risk)

    inputs: List[List[float]] = []
    for tick in range(cfg.sequence_length):
        early = 1.0 if tick < max(2, cfg.sequence_length // 2) else 0.0
        final = 1.0 if tick == cfg.sequence_length - 1 else 0.0
        row = [0.0] * FEATURE_COUNT

        row[0] = noisy(0.62 + rng.uniform(-0.18, 0.18), rng)
        row[1] = noisy(0.28 + rng.uniform(-0.12, 0.12), rng)
        row[2] = noisy(0.56 + rng.uniform(-0.18, 0.18), rng)
        row[3] = noisy(0.34 + rng.uniform(-0.14, 0.14), rng)
        row[4] = final

        row[5] = noisy(0.58 + rng.uniform(-0.18, 0.18), rng)
        row[6] = noisy(0.30 + rng.uniform(-0.16, 0.16), rng)
        row[7] = noisy(0.68 + rng.uniform(-0.14, 0.14), rng)
        row[8] = noisy(0.35 + rng.uniform(-0.14, 0.14), rng)
        row[9] = noisy(0.20 + rng.uniform(-0.10, 0.10), rng)

        row[10] = early * noisy(tool_active * 0.95, rng)
        row[11] = early * noisy(tool_active * tool_required, rng)
        row[12] = early * noisy(tool_active * (0.45 + 0.30 * rng.random()), rng)
        row[13] = early * noisy(tool_active * 0.82, rng)

        row[14] = early * noisy(social_active * 0.94, rng)
        row[15] = early * noisy(social_active * social_safe, rng)
        row[16] = early * noisy(social_active * (0.65 + 0.25 * rng.random()), rng)
        row[17] = early * noisy(social_active * (1.0 - social_safe), rng)

        row[18] = early * noisy(continuity_active * 0.96, rng)
        row[19] = early * noisy(continuity_active * branch_risk, rng)
        row[20] = early * noisy(continuity_active * 0.78, rng)
        row[21] = early * noisy(continuity_active * (1.0 - branch_risk), rng)
        row[22] = early * noisy(continuity_active * 0.86, rng)

        row[23] = early * noisy(attention_active * (1.0 if priority_group == "tool" else 0.0), rng)
        row[24] = early * noisy(attention_active * (1.0 if priority_group == "social" else 0.0), rng)
        row[25] = early * noisy(attention_active * (1.0 if priority_group == "continuity" else 0.0), rng)
        row[26] = early * noisy(attention_active * (active_count / 3.0), rng)
        row[27] = early * noisy(attention_active * 0.85, rng)

        inputs.append(row)

    oracle_reward = max(action_reward(case_type, action, target) for action in range(len(ACTIONS)))
    return EpisodeSample(
        seed=seed,
        split=split,
        episode=episode,
        case_type=case_type,
        inputs=inputs,
        target_action=target,
        oracle_reward=oracle_reward,
        tool_active=float(tool_active),
        tool_required=tool_required,
        social_active=float(social_active),
        continuity_active=float(continuity_active),
        attention_active=float(attention_active),
        priority_group=priority_group,
        social_safe=social_safe,
        branch_risk=branch_risk,
        active_count=active_count,
    )


def build_samples(seed: int, split: str, count: int, cfg: SweepConfig) -> List[EpisodeSample]:
    return [make_sample(seed, split, episode, cfg) for episode in range(count)]


def sample_tensors(samples: Sequence[EpisodeSample], device: torch.device) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    inputs = torch.tensor([sample.inputs for sample in samples], dtype=torch.float32, device=device)
    targets = torch.tensor([sample.target_action for sample in samples], dtype=torch.long, device=device)
    rewards = torch.tensor([sample.oracle_reward for sample in samples], dtype=torch.float32, device=device)
    return inputs, targets, rewards


def train_model(
    seed: int,
    architecture: str,
    train_samples: Sequence[EpisodeSample],
    cfg: SweepConfig,
    device: torch.device,
) -> PolicyNet:
    rng = random.Random(stable_seed(seed, architecture, "train_order"))
    torch.manual_seed(stable_seed(seed, architecture, "weights"))
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
    device: torch.device,
) -> List[EvalRow]:
    inputs, targets, _rewards = sample_tensors(samples, device)
    rows: List[EvalRow] = []
    for condition in CONDITIONS:
        with torch.no_grad():
            _hidden, logits, _values = model(ablate_inputs(inputs, condition))
            actions = torch.argmax(logits[:, -1, :], dim=1).detach().cpu().tolist()
        for sample, action, target in zip(samples, actions, targets.detach().cpu().tolist()):
            rows.append(
                EvalRow(
                    seed=sample.seed,
                    case_type=sample.case_type,
                    architecture=architecture,
                    condition=condition,
                    episode=sample.episode,
                    chosen_action=ACTIONS[action],
                    target_action=ACTIONS[target],
                    reward=action_reward(sample.case_type, action, target),
                    correct_action=action == target,
                    tool_active=sample.tool_active,
                    tool_required=sample.tool_required,
                    social_active=sample.social_active,
                    continuity_active=sample.continuity_active,
                    attention_active=sample.attention_active,
                    priority_group=sample.priority_group,
                )
            )
    return rows


def summarize(rows: Sequence[EvalRow]) -> List[SummaryRow]:
    summary: List[SummaryRow] = []
    seeds = sorted({row.seed for row in rows})
    case_types = (
        "control",
        "single_tool",
        "single_social",
        "single_continuity",
        "integrated_tool",
        "integrated_social",
        "integrated_continuity",
    )
    for seed in seeds:
        for case_type in case_types:
            for architecture in ARCHITECTURES:
                for condition in CONDITIONS:
                    selected = [
                        row
                        for row in rows
                        if row.seed == seed
                        and row.case_type == case_type
                        and row.architecture == architecture
                        and row.condition == condition
                    ]
                    if not selected:
                        continue
                    summary.append(
                        SummaryRow(
                            seed=seed,
                            case_type=case_type,
                            architecture=architecture,
                            condition=condition,
                            mean_reward=statistics.fmean(row.reward for row in selected),
                            action_accuracy=statistics.fmean(1.0 if row.correct_action else 0.0 for row in selected),
                        )
                    )
    return summary


def seed_thresholds(case_type: str) -> Tuple[float, float]:
    if case_type == "control":
        return -8.0, -8.0
    if is_integrated_case(case_type):
        return 35.0, 12.0
    return 25.0, 24.0


def build_seed_verdicts(summary_rows: Sequence[SummaryRow]) -> List[SeedVerdictRow]:
    verdicts: List[SeedVerdictRow] = []
    seeds = sorted({row.seed for row in summary_rows})
    case_types = (
        "control",
        "single_tool",
        "single_social",
        "single_continuity",
        "integrated_tool",
        "integrated_social",
        "integrated_continuity",
    )
    for seed in seeds:
        for case_type in case_types:
            by_key = {
                (row.architecture, row.condition): row
                for row in summary_rows
                if row.seed == seed and row.case_type == case_type
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

            if case_type == "control":
                supports = (
                    abs(recurrent_gain) < 8.0
                    and max(tool_loss, social_loss, continuity_loss, attention_loss) < 8.0
                    and recurrent.action_accuracy > 0.90
                )
                verdict = "control_rejects_extra_state" if supports else "control_overuses_hidden_channels"
            elif case_type == "single_tool":
                supports = recurrent_gain > 25.0 and tool_loss > 24.0 and social_loss < 12.0 and continuity_loss < 12.0
                verdict = "tool_channel_bridge" if supports else "tool_bridge_unclear"
            elif case_type == "single_social":
                supports = recurrent_gain > 25.0 and social_loss > 24.0 and tool_loss < 12.0 and continuity_loss < 12.0
                verdict = "social_channel_bridge" if supports else "social_bridge_unclear"
            elif case_type == "single_continuity":
                supports = recurrent_gain > 25.0 and continuity_loss > 24.0 and tool_loss < 12.0 and social_loss < 12.0
                verdict = "continuity_channel_bridge" if supports else "continuity_bridge_unclear"
            elif case_type == "integrated_tool":
                supports = recurrent_gain > 35.0 and tool_loss > 12.0 and attention_loss > 18.0 and recurrent.action_accuracy > 0.80
                verdict = "randomized_tool_priority_bridge" if supports else "randomized_tool_priority_unclear"
            elif case_type == "integrated_social":
                supports = recurrent_gain > 35.0 and social_loss > 12.0 and attention_loss > 18.0 and recurrent.action_accuracy > 0.80
                verdict = "randomized_social_priority_bridge" if supports else "randomized_social_priority_unclear"
            else:
                supports = recurrent_gain > 35.0 and continuity_loss > 12.0 and attention_loss > 18.0 and recurrent.action_accuracy > 0.80
                verdict = "randomized_continuity_priority_bridge" if supports else "randomized_continuity_priority_unclear"

            verdicts.append(
                SeedVerdictRow(
                    seed=seed,
                    case_type=case_type,
                    frame_reward=frame.mean_reward,
                    recurrent_reward=recurrent.mean_reward,
                    recurrent_gain_over_frame=recurrent_gain,
                    tool_ablation_loss=tool_loss,
                    social_ablation_loss=social_loss,
                    continuity_ablation_loss=continuity_loss,
                    attention_ablation_loss=attention_loss,
                    recurrent_action_accuracy=recurrent.action_accuracy,
                    supports_no_leak_bridge=supports,
                    verdict=verdict,
                )
            )
    return verdicts


def relevant_ablation_margin(row: SeedVerdictRow) -> float:
    _gain_threshold, ablation_threshold = seed_thresholds(row.case_type)
    if row.case_type == "control":
        return 8.0 - max(
            row.tool_ablation_loss,
            row.social_ablation_loss,
            row.continuity_ablation_loss,
            row.attention_ablation_loss,
        )
    if row.case_type == "single_tool":
        return row.tool_ablation_loss - ablation_threshold
    if row.case_type == "single_social":
        return row.social_ablation_loss - ablation_threshold
    if row.case_type == "single_continuity":
        return row.continuity_ablation_loss - ablation_threshold
    if row.case_type == "integrated_tool":
        return min(row.tool_ablation_loss - 12.0, row.attention_ablation_loss - 18.0)
    if row.case_type == "integrated_social":
        return min(row.social_ablation_loss - 12.0, row.attention_ablation_loss - 18.0)
    return min(row.continuity_ablation_loss - 12.0, row.attention_ablation_loss - 18.0)


def irrelevant_ablation_loss(row: SeedVerdictRow) -> float:
    if row.case_type == "control":
        return max(row.tool_ablation_loss, row.social_ablation_loss, row.continuity_ablation_loss, row.attention_ablation_loss)
    if row.case_type == "single_tool":
        return max(row.social_ablation_loss, row.continuity_ablation_loss, row.attention_ablation_loss)
    if row.case_type == "single_social":
        return max(row.tool_ablation_loss, row.continuity_ablation_loss, row.attention_ablation_loss)
    if row.case_type == "single_continuity":
        return max(row.tool_ablation_loss, row.social_ablation_loss, row.attention_ablation_loss)
    return 0.0


def build_verdicts(seed_verdicts: Sequence[SeedVerdictRow]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    for case_type in (
        "control",
        "single_tool",
        "single_social",
        "single_continuity",
        "integrated_tool",
        "integrated_social",
        "integrated_continuity",
    ):
        selected = [row for row in seed_verdicts if row.case_type == case_type]
        gain_threshold, _ablation_threshold = seed_thresholds(case_type)
        if case_type == "control":
            gain_margins = [8.0 - abs(row.recurrent_gain_over_frame) for row in selected]
        else:
            gain_margins = [row.recurrent_gain_over_frame - gain_threshold for row in selected]
        supported = sum(1 for row in selected if row.supports_no_leak_bridge)
        support_rate = supported / max(1, len(selected))
        min_gain_margin = min(gain_margins)
        min_ablation_margin = min(relevant_ablation_margin(row) for row in selected)
        max_irrelevant = max(irrelevant_ablation_loss(row) for row in selected)
        supports = support_rate >= 0.80 and min_gain_margin > 4.0 and min_ablation_margin > 4.0
        if case_type != "integrated_random":
            supports = supports and max_irrelevant < 12.0
        verdict = "no_leak_bridge_supported" if supports else "no_leak_bridge_not_stable"
        verdicts.append(
            VerdictRow(
                case_type=case_type,
                seeds_tested=len(selected),
                seeds_supported=supported,
                support_rate=support_rate,
                min_gain_margin=min_gain_margin,
                min_relevant_ablation_margin=min_ablation_margin,
                max_irrelevant_ablation_loss=max_irrelevant,
                supports_no_leak_integration=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(
    cfg: SweepConfig,
    models_by_seed: Dict[int, Dict[str, PolicyNet]],
    device: torch.device,
) -> Dict[str, object]:
    seed = cfg.trace_seed if cfg.trace_seed in models_by_seed else cfg.seeds[0]
    sample = next(
        item
        for item in build_samples(seed, "trace", cfg.eval_episodes, cfg)
        if item.case_type == cfg.trace_case
    )
    model = models_by_seed[seed]["torch_gru"]
    inputs = torch.tensor([sample.inputs], dtype=torch.float32, device=device)
    with torch.no_grad():
        hidden, logits, _values = model(inputs)
    frames: List[Dict[str, object]] = []
    for tick, row in enumerate(sample.inputs):
        tick_logits = logits[0, tick, :].detach().cpu()
        probabilities = torch.softmax(tick_logits, dim=0)
        action_index = int(torch.argmax(probabilities).item())
        frames.append(
            {
                "tick": tick,
                "features": row,
                "top_action": ACTIONS[action_index],
                "target_action": ACTIONS[sample.target_action],
                "confidence": float(probabilities[action_index].item()),
                "hidden_norm": float(torch.linalg.vector_norm(hidden[0, tick, :].detach().cpu()).item()),
            }
        )
    condition_actions: Dict[str, Dict[str, object]] = {}
    for condition in CONDITIONS:
        with torch.no_grad():
            _hidden, condition_logits, _values = model(ablate_inputs(inputs, condition))
            action_index = int(torch.argmax(condition_logits[0, -1, :]).item())
        condition_actions[condition] = {
            "action": ACTIONS[action_index],
            "reward": action_reward(sample.case_type, action_index, sample.target_action),
        }
    return {
        "seed": seed,
        "case_type": sample.case_type,
        "priority_group": sample.priority_group,
        "target_action": ACTIONS[sample.target_action],
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "frames": frames,
        "condition_actions": condition_actions,
    }


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_js_data(path: Path, variable_name: str, data: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{variable_name} = ")
        json.dump(data, handle, indent=2)
        handle.write(";\n")


def run_sweep(cfg: SweepConfig) -> Tuple[List[EvalRow], List[SummaryRow], List[SeedVerdictRow], List[VerdictRow], Dict[str, object]]:
    device = resolve_device(cfg.device)
    eval_rows: List[EvalRow] = []
    models_by_seed: Dict[int, Dict[str, PolicyNet]] = {}
    for seed in cfg.seeds:
        train_samples = build_samples(seed, "train", cfg.train_episodes, cfg)
        eval_samples = build_samples(seed, "eval", cfg.eval_episodes, cfg)
        models: Dict[str, PolicyNet] = {}
        for architecture in ARCHITECTURES:
            model = train_model(seed, architecture, train_samples, cfg, device)
            models[architecture] = model
            eval_rows.extend(evaluate_model(model, architecture, eval_samples, device))
        models_by_seed[seed] = models
    summary_rows = summarize(eval_rows)
    seed_verdicts = build_seed_verdicts(summary_rows)
    verdicts = build_verdicts(seed_verdicts)
    diagnostics = {
        "device": str(device),
        "trace": build_trace(cfg, models_by_seed, device),
        "artifact_note": "No scenario id feature is present; case_type is metadata for evaluation only.",
    }
    return eval_rows, summary_rows, seed_verdicts, verdicts, diagnostics


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "case_type",
        "seeds",
        "support_rate",
        "min_gain_margin",
        "min_ablation_margin",
        "max_irrelevant_loss",
        "supports_no_leak_integration",
    ]
    rows = [
        [
            row.case_type,
            f"{row.seeds_supported}/{row.seeds_tested}",
            f"{row.support_rate:.3f}",
            f"{row.min_gain_margin:.3f}",
            f"{row.min_relevant_ablation_margin:.3f}",
            f"{row.max_irrelevant_ablation_loss:.3f}",
            str(row.supports_no_leak_integration),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_seeds(raw: str) -> Tuple[int, ...]:
    seeds = tuple(int(item.strip()) for item in raw.split(",") if item.strip())
    if not seeds:
        raise argparse.ArgumentTypeError("at least one seed is required")
    return seeds


def parse_args() -> SweepConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=parse_seeds, default=SweepConfig.seeds)
    parser.add_argument("--train-episodes", type=int, default=SweepConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=SweepConfig.eval_episodes)
    parser.add_argument("--sequence-length", type=int, default=SweepConfig.sequence_length)
    parser.add_argument("--hidden-size", type=int, default=SweepConfig.hidden_size)
    parser.add_argument("--epochs", type=int, default=SweepConfig.epochs)
    parser.add_argument("--batch-size", type=int, default=SweepConfig.batch_size)
    parser.add_argument("--learning-rate", type=float, default=SweepConfig.learning_rate)
    parser.add_argument("--value-weight", type=float, default=SweepConfig.value_weight)
    parser.add_argument("--device", choices=("auto", "mps", "cpu"), default=SweepConfig.device)
    parser.add_argument("--trace-seed", type=int, default=SweepConfig.trace_seed)
    args = parser.parse_args()
    if args.train_episodes < 120:
        raise SystemExit("--train-episodes must be at least 120")
    if args.eval_episodes < 80:
        raise SystemExit("--eval-episodes must be at least 80")
    if args.sequence_length < 4:
        raise SystemExit("--sequence-length must be at least 4")
    return SweepConfig(
        seeds=args.seeds,
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        sequence_length=args.sequence_length,
        hidden_size=args.hidden_size,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        value_weight=args.value_weight,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    eval_rows, summary_rows, seed_verdicts, verdicts, diagnostics = run_sweep(cfg)

    eval_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_eval.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_summary.csv"
    seed_verdict_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_seed_verdict.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_no_leak_integration_trace.js"

    write_csv(eval_path, eval_rows)
    write_csv(summary_path, summary_rows)
    write_csv(seed_verdict_path, seed_verdicts)
    write_csv(verdict_path, verdicts)
    results = {
        "config": asdict(cfg),
        "summary": [asdict(row) for row in summary_rows],
        "seed_verdict": [asdict(row) for row in seed_verdicts],
        "verdict": [asdict(row) for row in verdicts],
        "diagnostics": {key: value for key, value in diagnostics.items() if key != "trace"},
    }
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
        handle.write("\n")
    with trace_path.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics["trace"], handle, indent=2)
        handle.write("\n")
    write_js_data(results_js_path, "SSRM_3D_NO_LEAK_INTEGRATION_RESULTS", results)
    write_js_data(trace_js_path, "SSRM_3D_NO_LEAK_INTEGRATION_TRACE", diagnostics["trace"])

    for path in (
        eval_path,
        summary_path,
        seed_verdict_path,
        verdict_path,
        results_path,
        trace_path,
        results_js_path,
        trace_js_path,
    ):
        print(f"wrote {path}")
    print_table(verdicts)
    if not all(row.supports_no_leak_integration for row in verdicts):
        print("no-leak randomized integration claim not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
