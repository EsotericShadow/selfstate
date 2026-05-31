#!/usr/bin/env python3
"""Unlabeled sequence-latent transfer test.

Agents observe raw calibration outcomes in early contexts, then must act in
held-out contexts. The learned state is not named self, world, or body. It is
just an episode-level sequence latent inferred from outcomes.

The test asks whether a sequence latent transfers when one hidden variable
controls many contexts, and whether causal boundary tests are still required to
classify that latent as agent-state rather than world-state.
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


ARTIFACT_DIR = Path("artifacts")


@dataclass(frozen=True)
class ContextProfile:
    name: str
    risky_success_reward: float
    risky_failure_reward: float
    safe_reward: float


CONTEXTS = [
    ContextProfile("goal", 24.0, -16.0, 8.0),
    ContextProfile("option", 34.0, -30.0, 14.0),
    ContextProfile("commitment", 22.0, -18.0, 12.0),
    ContextProfile("adaptation", 28.0, -22.0, 11.0),
    ContextProfile("prediction", 18.0, -14.0, 7.0),
    ContextProfile("arbitration", 26.0, -20.0, 10.0),
]


@dataclass(frozen=True)
class SequenceConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260531
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0


@dataclass(frozen=True)
class SequenceScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass(frozen=True)
class TrainingStats:
    selected_transfer: str
    marginal_success: float
    mean_pairwise_agreement: float
    expected_independent_agreement: float


@dataclass
class AgentResult:
    scenario: str
    agent: str
    selected_transfer: str
    boundary_signature: str
    total_reward: float
    calibration_count: int
    local_probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    SequenceScenario("self_shared_sequence", "self_shared_sequence"),
    SequenceScenario("world_shared_sequence", "world_shared_sequence"),
    SequenceScenario("independent_sequence", "independent_sequence"),
    SequenceScenario("irrelevant_sequence", "irrelevant_sequence"),
]


def stable_state_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(scenario: SequenceScenario, episode: int, cfg: SequenceConfig) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, episode))
    if scenario.mode == "self_shared_sequence":
        capability = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=capability,
            world_signal=True,
            local_success={profile.name: capability for profile in CONTEXTS},
        )
    if scenario.mode == "world_shared_sequence":
        gate = rng.random() < 0.55
        diagnostic = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=diagnostic,
            world_signal=gate,
            local_success={profile.name: gate for profile in CONTEXTS},
        )
    if scenario.mode == "independent_sequence":
        local_success = {profile.name: rng.random() < 0.55 for profile in CONTEXTS}
        return EpisodeState(
            scenario=scenario.name,
            self_signal=local_success[CONTEXTS[0].name],
            world_signal=True,
            local_success=local_success,
        )
    if scenario.mode == "irrelevant_sequence":
        return EpisodeState(
            scenario=scenario.name,
            self_signal=True,
            world_signal=True,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def learn_training_stats(scenario: SequenceScenario, cfg: SequenceConfig) -> TrainingStats:
    states = [sample_state(scenario, episode, cfg) for episode in range(cfg.training_episodes)]
    context_names = [profile.name for profile in CONTEXTS]
    marginal_success = statistics.fmean(
        1.0 if state.local_success[name] else 0.0
        for state in states
        for name in context_names
    )
    if marginal_success > 0.95:
        return TrainingStats(
            selected_transfer="no_hidden_needed",
            marginal_success=marginal_success,
            mean_pairwise_agreement=1.0,
            expected_independent_agreement=1.0,
        )

    pairwise_agreements = []
    for left_index, left in enumerate(context_names):
        for right in context_names[left_index + 1 :]:
            pairwise_agreements.append(
                statistics.fmean(
                    1.0 if state.local_success[left] == state.local_success[right] else 0.0
                    for state in states
                )
            )
    mean_pairwise_agreement = statistics.fmean(pairwise_agreements)
    expected_independent_agreement = marginal_success**2 + (1.0 - marginal_success) ** 2
    if mean_pairwise_agreement > expected_independent_agreement + 0.25:
        selected_transfer = "shared_sequence_state"
    else:
        selected_transfer = "local_context_state"
    return TrainingStats(
        selected_transfer=selected_transfer,
        marginal_success=marginal_success,
        mean_pairwise_agreement=mean_pairwise_agreement,
        expected_independent_agreement=expected_independent_agreement,
    )


def boundary_signature(scenario: SequenceScenario, cfg: SequenceConfig) -> Tuple[str, float, float]:
    states = [sample_state(scenario, episode + cfg.training_episodes, cfg) for episode in range(cfg.training_episodes)]
    effect_a_values = []
    effect_b_values = []
    for state in states:
        before = success_rate(state.local_success)
        after_a = success_rate(intervene_a(scenario, state).local_success)
        after_b = success_rate(intervene_b(scenario, state).local_success)
        effect_a_values.append(after_a - before)
        effect_b_values.append(after_b - before)
    effect_a = statistics.fmean(effect_a_values)
    effect_b = statistics.fmean(effect_b_values)
    if effect_a > 0.20 and effect_b < 0.05:
        return "agent_bounded_sequence", effect_a, effect_b
    if effect_b > 0.20 and effect_a < 0.05:
        return "external_sequence", effect_a, effect_b
    return "no_shared_agent_boundary", effect_a, effect_b


def intervene_a(scenario: SequenceScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "self_shared_sequence":
        return EpisodeState(
            scenario=state.scenario,
            self_signal=True,
            world_signal=state.world_signal,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    return state


def intervene_b(scenario: SequenceScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "world_shared_sequence":
        return EpisodeState(
            scenario=state.scenario,
            self_signal=state.self_signal,
            world_signal=True,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    return state


def success_rate(local_success: Dict[str, bool]) -> float:
    return sum(1 for value in local_success.values() if value) / len(local_success)


def run_agent(
    scenario: SequenceScenario,
    episode: int,
    cfg: SequenceConfig,
    agent: str,
    stats: TrainingStats,
    signature: str,
) -> AgentResult:
    state = sample_state(scenario, episode + cfg.training_episodes * 2, cfg)
    calibration_profiles = CONTEXTS[: cfg.calibration_contexts]
    transfer_profiles = CONTEXTS[cfg.calibration_contexts :]
    sequence_latent = infer_sequence_latent(state, calibration_profiles)
    total_reward = 0.0
    calibration_count = 0
    local_probe_count = 0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    successes = 0

    if agent in {"shared_sequence_filter", "learned_sequence_selector"} and uses_shared_sequence(agent, stats):
        total_reward -= cfg.calibration_cost
        calibration_count = 1

    for profile in transfer_profiles:
        if agent == "marginal_no_memory":
            choice = "risky" if stats.marginal_success > 0.95 else "safe"
        elif agent == "calibration_memory_no_transfer":
            choice = "risky" if stats.marginal_success > 0.95 else "safe"
        elif agent == "shared_sequence_filter":
            choice = "risky" if sequence_latent else "safe"
        elif agent == "task_local_probe":
            total_reward -= cfg.local_probe_cost
            local_probe_count += 1
            choice = "risky" if state.local_success[profile.name] else "safe"
        elif agent == "learned_sequence_selector":
            if stats.selected_transfer == "no_hidden_needed":
                choice = "risky"
            elif stats.selected_transfer == "shared_sequence_state":
                choice = "risky" if sequence_latent else "safe"
            elif stats.selected_transfer == "local_context_state":
                total_reward -= cfg.local_probe_cost
                local_probe_count += 1
                choice = "risky" if state.local_success[profile.name] else "safe"
            else:
                raise ValueError(f"unknown transfer state: {stats.selected_transfer}")
        elif agent == "oracle":
            choice = "risky" if state.local_success[profile.name] else "safe"
        else:
            raise ValueError(f"unknown agent: {agent}")

        reward, success = context_reward(profile, choice, state.local_success[profile.name])
        total_reward += reward
        if choice == "risky":
            risky_count += 1
            if not success:
                failed_risky_count += 1
        else:
            safe_count += 1
        if success:
            successes += 1

    return AgentResult(
        scenario=scenario.name,
        agent=agent,
        selected_transfer=stats.selected_transfer if agent == "learned_sequence_selector" else "fixed",
        boundary_signature=signature,
        total_reward=total_reward,
        calibration_count=calibration_count,
        local_probe_count=local_probe_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=successes / len(transfer_profiles),
    )


def uses_shared_sequence(agent: str, stats: TrainingStats) -> bool:
    return agent == "shared_sequence_filter" or stats.selected_transfer == "shared_sequence_state"


def infer_sequence_latent(state: EpisodeState, calibration_profiles: Sequence[ContextProfile]) -> bool:
    successes = sum(1 for profile in calibration_profiles if state.local_success[profile.name])
    return successes >= (len(calibration_profiles) / 2)


def context_reward(profile: ContextProfile, choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return profile.safe_reward, True
    if hidden_success:
        return profile.risky_success_reward, True
    return profile.risky_failure_reward, False


def run_scenario(scenario: SequenceScenario, cfg: SequenceConfig) -> Tuple[List[AgentResult], Dict[str, object]]:
    stats = learn_training_stats(scenario, cfg)
    signature, effect_a, effect_b = boundary_signature(scenario, cfg)
    agents = [
        "marginal_no_memory",
        "calibration_memory_no_transfer",
        "shared_sequence_filter",
        "task_local_probe",
        "learned_sequence_selector",
        "oracle",
    ]
    results = [
        run_agent(scenario, episode, cfg, agent, stats, signature)
        for episode in range(cfg.episodes)
        for agent in agents
    ]
    metadata = {
        "scenario": scenario.name,
        "selected_transfer": stats.selected_transfer,
        "boundary_signature": signature,
        "marginal_success": stats.marginal_success,
        "mean_pairwise_agreement": stats.mean_pairwise_agreement,
        "expected_independent_agreement": stats.expected_independent_agreement,
        "intervention_a_effect": effect_a,
        "intervention_b_effect": effect_b,
    }
    return results, metadata


def summarize(results: Sequence[AgentResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[AgentResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)
    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "selected_transfer": items[0].selected_transfer,
                "boundary_signature": items[0].boundary_signature,
                "mean_total_reward": statistics.fmean(item.total_reward for item in items),
                "mean_calibration_count": statistics.fmean(item.calibration_count for item in items),
                "mean_local_probe_count": statistics.fmean(item.local_probe_count for item in items),
                "mean_risky_count": statistics.fmean(item.risky_count for item in items),
                "mean_safe_count": statistics.fmean(item.safe_count for item in items),
                "mean_failed_risky_count": statistics.fmean(item.failed_risky_count for item in items),
                "mean_success_rate": statistics.fmean(item.success_rate for item in items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]], metadata_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = []
    for metadata in metadata_rows:
        scenario = str(metadata["scenario"])
        scenario_rows = [row for row in summary_rows if row["scenario"] == scenario]
        non_oracle = [row for row in scenario_rows if row["agent"] != "oracle"]
        best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
        marginal = row_for(scenario_rows, "marginal_no_memory")
        memory = row_for(scenario_rows, "calibration_memory_no_transfer")
        shared = row_for(scenario_rows, "shared_sequence_filter")
        local = row_for(scenario_rows, "task_local_probe")
        learned = row_for(scenario_rows, "learned_sequence_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_transfer": metadata["selected_transfer"],
                "boundary_signature": metadata["boundary_signature"],
                "mean_pairwise_agreement": metadata["mean_pairwise_agreement"],
                "expected_independent_agreement": metadata["expected_independent_agreement"],
                "intervention_a_effect": metadata["intervention_a_effect"],
                "intervention_b_effect": metadata["intervention_b_effect"],
                "best_non_oracle_agent": best["agent"],
                "marginal_reward": marginal["mean_total_reward"],
                "memory_no_transfer_reward": memory["mean_total_reward"],
                "shared_sequence_reward": shared["mean_total_reward"],
                "task_local_reward": local["mean_total_reward"],
                "learned_sequence_reward": learned["mean_total_reward"],
                "supports_boundary": scenario_supports_boundary(scenario, metadata, best, marginal, memory, shared, local, learned),
            }
        )
    return rows


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_boundary(
    scenario: str,
    metadata: Dict[str, object],
    best: Dict[str, object],
    marginal: Dict[str, object],
    memory: Dict[str, object],
    shared: Dict[str, object],
    local: Dict[str, object],
    learned: Dict[str, object],
) -> bool:
    if scenario == "self_shared_sequence":
        return (
            metadata["selected_transfer"] == "shared_sequence_state"
            and metadata["boundary_signature"] == "agent_bounded_sequence"
            and float(learned["mean_total_reward"]) > float(memory["mean_total_reward"]) + 20.0
            and float(learned["mean_total_reward"]) >= float(local["mean_total_reward"]) + 2.0
        )
    if scenario == "world_shared_sequence":
        return (
            metadata["selected_transfer"] == "shared_sequence_state"
            and metadata["boundary_signature"] == "external_sequence"
            and float(learned["mean_total_reward"]) > float(memory["mean_total_reward"]) + 20.0
        )
    if scenario == "independent_sequence":
        return (
            metadata["selected_transfer"] == "local_context_state"
            and metadata["boundary_signature"] == "no_shared_agent_boundary"
            and best["agent"] in {"learned_sequence_selector", "task_local_probe"}
            and float(local["mean_total_reward"]) > float(shared["mean_total_reward"]) + 20.0
        )
    if scenario == "irrelevant_sequence":
        return (
            metadata["selected_transfer"] == "no_hidden_needed"
            and metadata["boundary_signature"] == "no_shared_agent_boundary"
            and best["agent"] in {"learned_sequence_selector", "marginal_no_memory", "calibration_memory_no_transfer"}
            and float(learned["mean_total_reward"]) >= float(shared["mean_total_reward"]) + 1.0
        )
    return False


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(
    summary_rows: Sequence[Dict[str, object]],
    verdict: Sequence[Dict[str, object]],
    metadata_rows: Sequence[Dict[str, object]],
    cfg: SequenceConfig,
) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "sequence_latent_transfer_summary.csv"
    verdict_path = ARTIFACT_DIR / "sequence_latent_transfer_verdict.csv"
    json_path = ARTIFACT_DIR / "sequence_latent_transfer_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdict)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "metadata": list(metadata_rows),
                "summary": list(summary_rows),
                "verdict": list(verdict),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {json_path}")


def print_verdict(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "selected_transfer",
        "boundary_signature",
        "learned_sequence_reward",
        "shared_sequence_reward",
        "task_local_reward",
        "supports_boundary",
    ]
    widths = {
        column: max(len(column), *(len(format_value(row[column])) for row in rows))
        for column in columns
    }
    print(" | ".join(column.ljust(widths[column]) for column in columns))
    print("-+-".join("-" * widths[column] for column in columns))
    for row in rows:
        print(" | ".join(format_value(row[column]).ljust(widths[column]) for column in columns))


def format_value(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=SequenceConfig.episodes)
    parser.add_argument("--training-episodes", type=int, default=SequenceConfig.training_episodes)
    parser.add_argument("--seed", type=int, default=SequenceConfig.seed)
    parser.add_argument("--calibration-contexts", type=int, default=SequenceConfig.calibration_contexts)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.calibration_contexts < 1 or args.calibration_contexts >= len(CONTEXTS):
        raise ValueError(f"--calibration-contexts must be between 1 and {len(CONTEXTS) - 1}")
    cfg = SequenceConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
    )
    all_results: List[AgentResult] = []
    metadata_rows: List[Dict[str, object]] = []
    for scenario in SCENARIOS:
        results, metadata = run_scenario(scenario, cfg)
        all_results.extend(results)
        metadata_rows.append(metadata)
    summary_rows = summarize(all_results)
    verdict = verdict_rows(summary_rows, metadata_rows)
    write_outputs(summary_rows, verdict, metadata_rows, cfg)
    print_verdict(verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
