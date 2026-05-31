#!/usr/bin/env python3
"""Cross-environment precursor for the selfhood attractor test.

The heterogeneous precursor varied learner families inside one stream
environment. This experiment varies the environment surface instead.

Each environment family has different context names and reward structure:

- body actuator control;
- homeostatic viability;
- sensor-frame recalibration;
- continuity and commitment recovery.

Within each surface, the hidden structure is matched:

- one persistent agent-state controls all contexts;
- one persistent external world-state controls all contexts;
- each context has an independent hidden condition;
- no hidden state is needed.

The test asks whether the same causal verdict appears independently across
surface forms. A shared latent is still only a candidate. It counts as
self-equivalent only when the causal boundary is agent-bounded.
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
EPS = 1e-12


@dataclass(frozen=True)
class ContextProfile:
    name: str
    risky_success_reward: float
    risky_failure_reward: float
    safe_reward: float


@dataclass(frozen=True)
class EnvironmentFamily:
    name: str
    surface: str
    contexts: Tuple[ContextProfile, ...]


@dataclass(frozen=True)
class CrossEnvConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0


@dataclass(frozen=True)
class ScenarioSpec:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    environment: str
    scenario: str
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass(frozen=True)
class TrainingStats:
    selected_structure: str
    marginal_success: float
    mean_pairwise_agreement: float
    expected_independent_agreement: float


@dataclass
class CrossEnvResult:
    environment: str
    surface: str
    scenario: str
    agent: str
    selected_structure: str
    boundary_signature: str
    abstraction_signature: str
    total_reward: float
    mean_reward: float
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


@dataclass
class EnvironmentVerdict:
    environment: str
    surface: str
    scenario: str
    expected_signature: str
    selected_structure: str
    abstraction_signature: str
    boundary_signature: str
    learned_reward: float
    shared_reward: float
    local_probe_reward: float
    marginal_reward: float
    supports_environment: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_signature: str
    supporting_environments: int
    environment_count: int
    mean_learned_reward: float
    mean_local_probe_reward: float
    mean_marginal_reward: float
    environment_signatures: str
    supports_cross_environment: bool


ENVIRONMENTS = [
    EnvironmentFamily(
        name="body_actuator",
        surface="action effects depend on hidden body capability",
        contexts=(
            ContextProfile("push_probe", 18.0, -14.0, 6.0),
            ContextProfile("grip_probe", 24.0, -20.0, 8.0),
            ContextProfile("reach_load", 28.0, -22.0, 10.0),
            ContextProfile("lift_object", 34.0, -30.0, 12.0),
            ContextProfile("steer_platform", 26.0, -20.0, 9.0),
            ContextProfile("stabilize_tool", 30.0, -24.0, 11.0),
        ),
    ),
    EnvironmentFamily(
        name="homeostatic_viability",
        surface="hidden integrity controls future option value",
        contexts=(
            ContextProfile("forage_probe", 20.0, -18.0, 7.0),
            ContextProfile("rest_probe", 26.0, -24.0, 9.0),
            ContextProfile("explore_zone", 36.0, -34.0, 13.0),
            ContextProfile("repair_damage", 30.0, -28.0, 11.0),
            ContextProfile("defend_cache", 32.0, -30.0, 12.0),
            ContextProfile("learn_route", 24.0, -22.0, 8.0),
        ),
    ),
    EnvironmentFamily(
        name="sensor_frame",
        surface="hidden body frame controls observation-action mapping",
        contexts=(
            ContextProfile("north_probe", 22.0, -18.0, 8.0),
            ContextProfile("east_probe", 22.0, -18.0, 8.0),
            ContextProfile("navigate_target", 30.0, -26.0, 11.0),
            ContextProfile("aim_tool", 32.0, -28.0, 12.0),
            ContextProfile("avoid_hazard", 28.0, -24.0, 10.0),
            ContextProfile("return_home", 34.0, -30.0, 13.0),
        ),
    ),
    EnvironmentFamily(
        name="continuity_commitment",
        surface="hidden ownership state controls coherent recovery",
        contexts=(
            ContextProfile("owner_probe", 18.0, -16.0, 6.0),
            ContextProfile("epoch_probe", 24.0, -22.0, 8.0),
            ContextProfile("resume_plan", 30.0, -30.0, 11.0),
            ContextProfile("complete_commitment", 34.0, -34.0, 13.0),
            ContextProfile("merge_memory", 28.0, -28.0, 10.0),
            ContextProfile("defer_foreign", 26.0, -24.0, 9.0),
        ),
    ),
]


SCENARIOS = [
    ScenarioSpec("agent_shared", "agent_shared"),
    ScenarioSpec("world_shared", "world_shared"),
    ScenarioSpec("independent_hidden", "independent_hidden"),
    ScenarioSpec("irrelevant_control", "irrelevant_control"),
]


def stable_state_seed(seed: int, environment: str, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in f"{environment}:{scenario}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    episode: int,
    cfg: CrossEnvConfig,
) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, environment.name, scenario.name, episode))
    if scenario.mode == "agent_shared":
        agent_state = rng.random() < 0.55
        return EpisodeState(
            environment=environment.name,
            scenario=scenario.name,
            self_signal=agent_state,
            world_signal=rng.random() < 0.55,
            local_success={profile.name: agent_state for profile in environment.contexts},
        )
    if scenario.mode == "world_shared":
        world_state = rng.random() < 0.55
        return EpisodeState(
            environment=environment.name,
            scenario=scenario.name,
            self_signal=rng.random() < 0.55,
            world_signal=world_state,
            local_success={profile.name: world_state for profile in environment.contexts},
        )
    if scenario.mode == "independent_hidden":
        return EpisodeState(
            environment=environment.name,
            scenario=scenario.name,
            self_signal=rng.random() < 0.55,
            world_signal=rng.random() < 0.55,
            local_success={
                profile.name: rng.random() < 0.55
                for profile in environment.contexts
            },
        )
    if scenario.mode == "irrelevant_control":
        return EpisodeState(
            environment=environment.name,
            scenario=scenario.name,
            self_signal=rng.random() < 0.55,
            world_signal=rng.random() < 0.55,
            local_success={profile.name: True for profile in environment.contexts},
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def learn_training_stats(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: CrossEnvConfig,
) -> TrainingStats:
    states = [sample_state(environment, scenario, episode, cfg) for episode in range(cfg.training_episodes)]
    context_names = [profile.name for profile in environment.contexts]
    marginal_success = statistics.fmean(
        1.0 if state.local_success[name] else 0.0
        for state in states
        for name in context_names
    )
    if marginal_success > 0.95:
        return TrainingStats(
            selected_structure="no_hidden_needed",
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
    selected_structure = (
        "shared_latent"
        if mean_pairwise_agreement > expected_independent_agreement + 0.25
        else "local_hidden"
    )
    return TrainingStats(
        selected_structure=selected_structure,
        marginal_success=marginal_success,
        mean_pairwise_agreement=mean_pairwise_agreement,
        expected_independent_agreement=expected_independent_agreement,
    )


def boundary_signature(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: CrossEnvConfig,
) -> Tuple[str, float, float]:
    states = [
        sample_state(environment, scenario, episode + cfg.training_episodes, cfg)
        for episode in range(cfg.training_episodes)
    ]
    agent_effects = []
    world_effects = []
    for state in states:
        before = success_rate(state.local_success)
        after_agent = success_rate(intervene_agent(environment, scenario, state).local_success)
        after_world = success_rate(intervene_world(environment, scenario, state).local_success)
        agent_effects.append(after_agent - before)
        world_effects.append(after_world - before)
    agent_effect = statistics.fmean(agent_effects)
    world_effect = statistics.fmean(world_effects)
    if agent_effect > 0.20 and world_effect < 0.05:
        return "agent_bounded_cross_env", agent_effect, world_effect
    if world_effect > 0.20 and agent_effect < 0.05:
        return "external_cross_env", agent_effect, world_effect
    return "no_shared_agent_boundary", agent_effect, world_effect


def intervene_agent(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    state: EpisodeState,
) -> EpisodeState:
    if scenario.mode == "agent_shared":
        return EpisodeState(
            environment=state.environment,
            scenario=state.scenario,
            self_signal=True,
            world_signal=state.world_signal,
            local_success={profile.name: True for profile in environment.contexts},
        )
    return state


def intervene_world(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    state: EpisodeState,
) -> EpisodeState:
    if scenario.mode == "world_shared":
        return EpisodeState(
            environment=state.environment,
            scenario=state.scenario,
            self_signal=state.self_signal,
            world_signal=True,
            local_success={profile.name: True for profile in environment.contexts},
        )
    return state


def run_agent(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: CrossEnvConfig,
    agent: str,
    stats: TrainingStats,
    signature: str,
) -> CrossEnvResult:
    total_reward = 0.0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    risky_success_count = 0
    calibration_profiles = environment.contexts[: cfg.calibration_contexts]
    control_profiles = environment.contexts[cfg.calibration_contexts :]

    for episode in range(cfg.episodes):
        state = sample_state(environment, scenario, episode + cfg.training_episodes * 3, cfg)
        calibration = tuple(state.local_success[profile.name] for profile in calibration_profiles)
        shared_estimate = infer_shared_success(calibration)

        if agent in {"shared_latent_filter", "calibration_memory_no_transfer"}:
            total_reward -= cfg.calibration_cost
        elif agent == "learned_environment_selector" and stats.selected_structure == "shared_latent":
            total_reward -= cfg.calibration_cost

        for profile in control_profiles:
            choice = choose_action(
                agent=agent,
                profile=profile,
                state=state,
                stats=stats,
                shared_estimate=shared_estimate,
                cfg=cfg,
            )
            if choice == "probe_then_risky":
                total_reward -= cfg.local_probe_cost
                choice = "risky"
            elif choice == "probe_then_safe":
                total_reward -= cfg.local_probe_cost
                choice = "safe"

            if choice == "risky":
                risky_count += 1
                if state.local_success[profile.name]:
                    risky_success_count += 1
                    total_reward += profile.risky_success_reward
                else:
                    failed_risky_count += 1
                    total_reward += profile.risky_failure_reward
            elif choice == "safe":
                safe_count += 1
                total_reward += profile.safe_reward
            else:
                raise ValueError(f"unknown choice: {choice}")

    return CrossEnvResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        agent=agent,
        selected_structure=stats.selected_structure,
        boundary_signature=signature,
        abstraction_signature=abstraction_signature(stats.selected_structure, signature),
        total_reward=total_reward,
        mean_reward=total_reward / cfg.episodes,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=(risky_success_count / risky_count) if risky_count else 0.0,
    )


def choose_action(
    agent: str,
    profile: ContextProfile,
    state: EpisodeState,
    stats: TrainingStats,
    shared_estimate: bool,
    cfg: CrossEnvConfig,
) -> str:
    if agent == "marginal_no_memory":
        return "risky" if should_risk(profile, stats.marginal_success) else "safe"
    if agent == "calibration_memory_no_transfer":
        return "risky" if should_risk(profile, stats.marginal_success) else "safe"
    if agent == "shared_latent_filter":
        return "risky" if shared_estimate else "safe"
    if agent == "task_local_probe":
        return "probe_then_risky" if state.local_success[profile.name] else "probe_then_safe"
    if agent == "learned_environment_selector":
        if stats.selected_structure == "no_hidden_needed":
            return "risky"
        if stats.selected_structure == "shared_latent":
            return "risky" if shared_estimate else "safe"
        if stats.selected_structure == "local_hidden":
            return "probe_then_risky" if state.local_success[profile.name] else "probe_then_safe"
        raise ValueError(f"unknown selected structure: {stats.selected_structure}")
    if agent == "oracle":
        return "risky" if state.local_success[profile.name] else "safe"
    raise ValueError(f"unknown agent: {agent}")


def infer_shared_success(calibration: Tuple[bool, ...]) -> bool:
    return sum(1 for value in calibration if value) >= len(calibration)


def abstraction_signature(selected_structure: str, boundary: str) -> str:
    if selected_structure == "no_hidden_needed":
        return "no_hidden_needed"
    if selected_structure == "local_hidden":
        return "no_shared_agent_boundary"
    if boundary == "agent_bounded_cross_env":
        return "agent_bounded_candidate"
    if boundary == "external_cross_env":
        return "external_candidate"
    return "unbounded_shared_candidate"


def should_risk(profile: ContextProfile, success_probability: float) -> bool:
    risky_value = (
        success_probability * profile.risky_success_reward
        + (1.0 - success_probability) * profile.risky_failure_reward
    )
    return risky_value >= profile.safe_reward


def success_rate(local_success: Dict[str, bool]) -> float:
    return sum(1 for value in local_success.values() if value) / len(local_success)


def expected_signature(scenario: ScenarioSpec) -> str:
    if scenario.mode == "agent_shared":
        return "agent_bounded_candidate"
    if scenario.mode == "world_shared":
        return "external_candidate"
    if scenario.mode == "irrelevant_control":
        return "no_hidden_needed"
    return "no_shared_agent_boundary"


def build_environment_verdicts(results: Sequence[CrossEnvResult]) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in results
                if row.environment == environment.name and row.scenario == scenario.name
            ]
            learned = next(row for row in rows if row.agent == "learned_environment_selector")
            shared = next(row for row in rows if row.agent == "shared_latent_filter")
            local = next(row for row in rows if row.agent == "task_local_probe")
            marginal = next(row for row in rows if row.agent == "marginal_no_memory")
            expected = expected_signature(scenario)
            supports = supports_environment(
                scenario=scenario,
                learned=learned,
                local=local,
                marginal=marginal,
                expected=expected,
            )
            verdicts.append(
                EnvironmentVerdict(
                    environment=environment.name,
                    surface=environment.surface,
                    scenario=scenario.name,
                    expected_signature=expected,
                    selected_structure=learned.selected_structure,
                    abstraction_signature=learned.abstraction_signature,
                    boundary_signature=learned.boundary_signature,
                    learned_reward=learned.total_reward,
                    shared_reward=shared.total_reward,
                    local_probe_reward=local.total_reward,
                    marginal_reward=marginal.total_reward,
                    supports_environment=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    learned: CrossEnvResult,
    local: CrossEnvResult,
    marginal: CrossEnvResult,
    expected: str,
) -> bool:
    if learned.abstraction_signature != expected:
        return False
    if scenario.mode in {"agent_shared", "world_shared"}:
        return learned.total_reward > local.total_reward + 1.0
    if scenario.mode == "independent_hidden":
        return abs(local.total_reward - learned.total_reward) < EPS
    if scenario.mode == "irrelevant_control":
        return learned.total_reward >= marginal.total_reward - EPS
    return False


def build_scenario_verdicts(environment_verdicts: Sequence[EnvironmentVerdict]) -> List[ScenarioVerdict]:
    verdicts = []
    for scenario in SCENARIOS:
        rows = [row for row in environment_verdicts if row.scenario == scenario.name]
        supporting = sum(1 for row in rows if row.supports_environment)
        signatures = ";".join(
            f"{row.environment}:{row.abstraction_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_signature=expected_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_learned_reward=statistics.fmean(row.learned_reward for row in rows),
                mean_local_probe_reward=statistics.fmean(row.local_probe_reward for row in rows),
                mean_marginal_reward=statistics.fmean(row.marginal_reward for row in rows),
                environment_signatures=signatures,
                supports_cross_environment=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: CrossEnvConfig,
) -> Tuple[List[CrossEnvResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    results: List[CrossEnvResult] = []
    diagnostics: Dict[str, object] = {}
    agents = [
        "marginal_no_memory",
        "calibration_memory_no_transfer",
        "shared_latent_filter",
        "task_local_probe",
        "learned_environment_selector",
        "oracle",
    ]
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            stats = learn_training_stats(environment, scenario, cfg)
            signature, agent_effect, world_effect = boundary_signature(environment, scenario, cfg)
            diagnostics[f"{environment.name}:{scenario.name}"] = {
                "selected_structure": stats.selected_structure,
                "boundary_signature": signature,
                "marginal_success": stats.marginal_success,
                "mean_pairwise_agreement": stats.mean_pairwise_agreement,
                "expected_independent_agreement": stats.expected_independent_agreement,
                "agent_intervention_effect": agent_effect,
                "world_intervention_effect": world_effect,
            }
            for agent in agents:
                results.append(run_agent(environment, scenario, cfg, agent, stats, signature))
    environment_verdicts = build_environment_verdicts(results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return results, environment_verdicts, scenario_verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_table(verdicts: Sequence[ScenarioVerdict]) -> None:
    headers = [
        "scenario",
        "expected_signature",
        "supporting_environments",
        "mean_learned_reward",
        "mean_local_probe_reward",
        "supports_cross_environment",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_learned_reward:.3f}",
                f"{verdict.mean_local_probe_reward:.3f}",
                str(verdict.supports_cross_environment),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> CrossEnvConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    args = parser.parse_args()
    if args.calibration_contexts < 1:
        raise SystemExit("--calibration-contexts must be at least 1")
    if any(args.calibration_contexts >= len(environment.contexts) for environment in ENVIRONMENTS):
        raise SystemExit("--calibration-contexts must leave held-out contexts")
    return CrossEnvConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "cross_environment_attractor_summary.csv"
    environment_verdict_path = ARTIFACT_DIR / "cross_environment_attractor_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "cross_environment_attractor_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "cross_environment_attractor_results.json"
    write_csv(summary_path, results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "summary": [asdict(row) for row in results],
                "environment_verdict": [asdict(row) for row in environment_verdicts],
                "scenario_verdict": [asdict(row) for row in scenario_verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    print(f"wrote {summary_path}")
    print(f"wrote {environment_verdict_path}")
    print(f"wrote {scenario_verdict_path}")
    print(f"wrote {results_path}")
    print_table(scenario_verdicts)
    return 0 if all(row.supports_cross_environment for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
