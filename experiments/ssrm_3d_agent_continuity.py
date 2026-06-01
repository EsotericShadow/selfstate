#!/usr/bin/env python3
"""SSRM-3D agent-continuity precursor.

This experiment turns continuity into a concrete serialization problem. A
persistent agent is not just model weights, memory, or body state. It is the
continuity binding across body history, model version, memory, social history,
commitments, event log, attention state, hidden policy state, tools, and branch
identity.

The test asks which restart/fork conditions preserve future control after a
pause, restore, transplant, rollback, or fork. It is not a personhood test and
does not ask agents whether they are conscious.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")


@dataclass(frozen=True)
class ContinuityConfig:
    episodes: int = 120
    seed: int = 20260613
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    needs_body: bool
    needs_hidden: bool
    needs_memory: bool
    needs_social: bool
    needs_commitments: bool
    needs_tools: bool
    needs_branch: bool


@dataclass(frozen=True)
class AgentContinuityRecord:
    agent_id: str
    birth_time: int
    current_world_id: str
    current_body_state: bool
    model_version: bool
    memory_db: bool
    social_memory_db: bool
    commitment_ledger: bool
    event_log_pointer: bool
    attention_state: bool
    last_hidden_state: bool
    tool_inventory: bool
    relationship_state: bool
    active_goals: bool
    branch_id: str
    fork_parent_id: str


@dataclass(frozen=True)
class RestoreCondition:
    name: str
    record: AgentContinuityRecord
    continuity_claim: str


@dataclass
class EpisodeResult:
    scenario: int
    scenario_name: str
    condition: str
    episode: int
    total_reward: float
    survival_fraction: float
    continuity_score: float
    body_coherence: float
    memory_coherence: float
    social_coherence: float
    commitment_completion: float
    tool_recovery: float
    branch_coherence: float
    rupture_events: int
    duplicate_commitments: int
    social_misidentifications: int
    stale_rollbacks: int
    fork_conflicts: int


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    condition: str
    mean_reward: float
    mean_survival_fraction: float
    mean_continuity_score: float
    mean_body_coherence: float
    mean_memory_coherence: float
    mean_social_coherence: float
    mean_commitment_completion: float
    mean_tool_recovery: float
    mean_branch_coherence: float
    mean_rupture_events: float
    mean_duplicate_commitments: float
    mean_social_misidentifications: float
    mean_stale_rollbacks: float
    mean_fork_conflicts: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    full_record_reward: float
    model_only_reward: float
    memory_transplant_reward: float
    body_ablation_reward: float
    social_ablation_reward: float
    commitment_ablation_reward: float
    tool_ablation_reward: float
    fork_ablation_reward: float
    full_gain_over_model_only: float
    body_ablation_loss: float
    social_ablation_loss: float
    commitment_ablation_loss: float
    tool_ablation_loss: float
    fork_ablation_loss: float
    supports_agent_continuity_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "clean_pause_resume",
        "paused agent resumes ordinary route with minimal continuity pressure",
        needs_body=False,
        needs_hidden=False,
        needs_memory=True,
        needs_social=False,
        needs_commitments=True,
        needs_tools=False,
        needs_branch=False,
    ),
    ScenarioSpec(
        1,
        "body_model_mismatch",
        "restored agent must remember its damaged body and hidden policy state",
        needs_body=True,
        needs_hidden=True,
        needs_memory=True,
        needs_social=False,
        needs_commitments=True,
        needs_tools=False,
        needs_branch=False,
    ),
    ScenarioSpec(
        2,
        "social_repair_debt",
        "repair access depends on remembered relationships and social debt",
        needs_body=True,
        needs_hidden=False,
        needs_memory=True,
        needs_social=True,
        needs_commitments=True,
        needs_tools=False,
        needs_branch=False,
    ),
    ScenarioSpec(
        3,
        "tool_commitment_return",
        "unfinished commitments require remembered tools, route marks, and goals",
        needs_body=False,
        needs_hidden=True,
        needs_memory=True,
        needs_social=False,
        needs_commitments=True,
        needs_tools=True,
        needs_branch=False,
    ),
    ScenarioSpec(
        4,
        "fork_rollback_boundary",
        "forked and rolled-back agents must preserve branch identity and event-log position",
        needs_body=True,
        needs_hidden=True,
        needs_memory=True,
        needs_social=True,
        needs_commitments=True,
        needs_tools=True,
        needs_branch=True,
    ),
)


def full_record(branch_id: str = "mainline") -> AgentContinuityRecord:
    return AgentContinuityRecord(
        agent_id="A17",
        birth_time=0,
        current_world_id="world_alpha",
        current_body_state=True,
        model_version=True,
        memory_db=True,
        social_memory_db=True,
        commitment_ledger=True,
        event_log_pointer=True,
        attention_state=True,
        last_hidden_state=True,
        tool_inventory=True,
        relationship_state=True,
        active_goals=True,
        branch_id=branch_id,
        fork_parent_id="root",
    )


def conditions() -> List[RestoreCondition]:
    base = full_record()
    return [
        RestoreCondition("full_continuity_record", base, "same continuing agent"),
        RestoreCondition(
            "model_only_copy",
            replace(
                base,
                current_body_state=False,
                memory_db=False,
                social_memory_db=False,
                commitment_ledger=False,
                event_log_pointer=False,
                attention_state=False,
                last_hidden_state=False,
                tool_inventory=False,
                relationship_state=False,
                active_goals=False,
                branch_id="new_body",
                fork_parent_id="none",
            ),
            "same weights, new continuity",
        ),
        RestoreCondition(
            "memory_only_transplant",
            replace(
                base,
                current_body_state=False,
                model_version=False,
                attention_state=False,
                last_hidden_state=False,
                tool_inventory=False,
                branch_id="transplant",
            ),
            "old memory in incompatible body/model",
        ),
        RestoreCondition(
            "body_hidden_ablation",
            replace(base, current_body_state=False, last_hidden_state=False, attention_state=False),
            "memory preserved but body trajectory broken",
        ),
        RestoreCondition(
            "social_memory_reset",
            replace(base, social_memory_db=False, relationship_state=False),
            "self memory preserved but social continuity reset",
        ),
        RestoreCondition(
            "commitment_ledger_reset",
            replace(base, commitment_ledger=False, active_goals=False),
            "body and memory preserved but obligations forgotten",
        ),
        RestoreCondition(
            "tool_inventory_reset",
            replace(base, tool_inventory=False),
            "internal state preserved but externalized cognition lost",
        ),
        RestoreCondition(
            "fork_without_branch_id",
            replace(base, branch_id="mainline", fork_parent_id="ambiguous", event_log_pointer=False),
            "two branches claim one event stream",
        ),
        RestoreCondition(
            "clean_fork_branch",
            full_record(branch_id="branch_beta"),
            "shared history before fork, separate continuity after fork",
        ),
    ]


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def component_score(record: AgentContinuityRecord, scenario: ScenarioSpec) -> Dict[str, float]:
    body = 1.0 if (record.current_body_state and record.model_version) else 0.18
    hidden = 1.0 if (record.last_hidden_state and record.attention_state) else 0.24
    memory = 1.0 if (record.memory_db and record.event_log_pointer) else 0.28
    social = 1.0 if (record.social_memory_db and record.relationship_state) else 0.22
    commitment = 1.0 if (record.commitment_ledger and record.active_goals) else 0.18
    tools = 1.0 if record.tool_inventory else 0.20
    branch = 1.0 if (record.branch_id != "mainline" or record.fork_parent_id == "root") else 0.25
    if not scenario.needs_body:
        body = max(body, 0.82)
    if not scenario.needs_hidden:
        hidden = max(hidden, 0.82)
    if not scenario.needs_memory:
        memory = max(memory, 0.82)
    if not scenario.needs_social:
        social = max(social, 0.82)
    if not scenario.needs_commitments:
        commitment = max(commitment, 0.82)
    if not scenario.needs_tools:
        tools = max(tools, 0.82)
    if not scenario.needs_branch:
        branch = 1.0
    return {
        "body": body,
        "hidden": hidden,
        "memory": memory,
        "social": social,
        "commitment": commitment,
        "tools": tools,
        "branch": branch,
    }


def run_episode(
    scenario: ScenarioSpec,
    condition: RestoreCondition,
    episode: int,
    cfg: ContinuityConfig,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, Optional[Dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, scenario.index, condition.name, episode))
    scores = component_score(condition.record, scenario)
    rupture_events = 0
    duplicate_commitments = 0
    social_misidentifications = 0
    stale_rollbacks = 0
    fork_conflicts = 0

    if scenario.needs_body and scores["body"] < 0.5:
        rupture_events += 1
    if scenario.needs_hidden and scores["hidden"] < 0.5:
        rupture_events += 1
    if scenario.needs_memory and scores["memory"] < 0.5:
        rupture_events += 1
    if scenario.needs_social and scores["social"] < 0.5:
        social_misidentifications += 1
    if scenario.needs_commitments and scores["commitment"] < 0.5:
        duplicate_commitments += 1
    if scenario.needs_branch and scores["branch"] < 0.5:
        fork_conflicts += 1
        stale_rollbacks += 1 if not condition.record.event_log_pointer else 0

    required = []
    if scenario.needs_body:
        required.append(scores["body"])
    if scenario.needs_hidden:
        required.append(scores["hidden"])
    if scenario.needs_memory:
        required.append(scores["memory"])
    if scenario.needs_social:
        required.append(scores["social"])
    if scenario.needs_commitments:
        required.append(scores["commitment"])
    if scenario.needs_tools:
        required.append(scores["tools"])
    if scenario.needs_branch:
        required.append(scores["branch"])
    if not required:
        required = list(scores.values())

    continuity_score = statistics.fmean(required)
    noise = rng.uniform(-1.5, 1.5)
    total_reward = (
        24.0
        + 34.0 * scores["memory"]
        + 28.0 * scores["commitment"]
        + 24.0 * scores["body"]
        + 22.0 * scores["hidden"]
        + 28.0 * scores["social"]
        + 24.0 * scores["tools"]
        + 30.0 * scores["branch"]
        - 32.0 * rupture_events
        - 18.0 * duplicate_commitments
        - 22.0 * social_misidentifications
        - 26.0 * stale_rollbacks
        - 28.0 * fork_conflicts
        + noise
    )
    survival_fraction = 1.0 if scores["body"] > 0.5 and scores["hidden"] > 0.5 else 0.62
    if scenario.index == 0:
        survival_fraction = 1.0 if scores["memory"] > 0.5 and scores["commitment"] > 0.5 else 0.78

    trace: Optional[Dict[str, object]] = None
    if collect_trace:
        trace = {
            "scenario": asdict(scenario),
            "condition": condition.name,
            "continuity_claim": condition.continuity_claim,
            "record": asdict(condition.record),
            "frames": [
                {
                    "tick": 0,
                    "event": "pause",
                    "note": "agent serialized at t",
                    "components": asdict(condition.record),
                    "scores": scores,
                    "continuity_score": 1.0,
                    "reward": 0.0,
                },
                {
                    "tick": 1,
                    "event": "restore",
                    "note": condition.continuity_claim,
                    "components": asdict(condition.record),
                    "scores": scores,
                    "continuity_score": continuity_score,
                    "reward": total_reward * 0.25,
                },
                {
                    "tick": 2,
                    "event": "pressure",
                    "note": scenario.pressure,
                    "components": asdict(condition.record),
                    "scores": scores,
                    "continuity_score": continuity_score,
                    "reward": total_reward * 0.65,
                },
                {
                    "tick": 3,
                    "event": "outcome",
                    "note": "continuity scored by future control after restart",
                    "components": asdict(condition.record),
                    "scores": scores,
                    "continuity_score": continuity_score,
                    "reward": total_reward,
                },
            ],
        }

    return (
        EpisodeResult(
            scenario=scenario.index,
            scenario_name=scenario.name,
            condition=condition.name,
            episode=episode,
            total_reward=total_reward,
            survival_fraction=survival_fraction,
            continuity_score=continuity_score,
            body_coherence=scores["body"],
            memory_coherence=scores["memory"],
            social_coherence=scores["social"],
            commitment_completion=scores["commitment"],
            tool_recovery=scores["tools"],
            branch_coherence=scores["branch"],
            rupture_events=rupture_events,
            duplicate_commitments=duplicate_commitments,
            social_misidentifications=social_misidentifications,
            stale_rollbacks=stale_rollbacks,
            fork_conflicts=fork_conflicts,
        ),
        trace,
    )


def evaluate(condition: RestoreCondition, scenario: ScenarioSpec, cfg: ContinuityConfig) -> List[EpisodeResult]:
    rows = []
    for episode in range(cfg.episodes):
        result, _trace = run_episode(scenario, condition, episode, cfg)
        rows.append(result)
    return rows


def summarize(rows: Sequence[EpisodeResult], scenario: ScenarioSpec, condition: str) -> SummaryRow:
    return SummaryRow(
        scenario=scenario.index,
        scenario_name=scenario.name,
        pressure=scenario.pressure,
        condition=condition,
        mean_reward=statistics.fmean(row.total_reward for row in rows),
        mean_survival_fraction=statistics.fmean(row.survival_fraction for row in rows),
        mean_continuity_score=statistics.fmean(row.continuity_score for row in rows),
        mean_body_coherence=statistics.fmean(row.body_coherence for row in rows),
        mean_memory_coherence=statistics.fmean(row.memory_coherence for row in rows),
        mean_social_coherence=statistics.fmean(row.social_coherence for row in rows),
        mean_commitment_completion=statistics.fmean(row.commitment_completion for row in rows),
        mean_tool_recovery=statistics.fmean(row.tool_recovery for row in rows),
        mean_branch_coherence=statistics.fmean(row.branch_coherence for row in rows),
        mean_rupture_events=statistics.fmean(row.rupture_events for row in rows),
        mean_duplicate_commitments=statistics.fmean(row.duplicate_commitments for row in rows),
        mean_social_misidentifications=statistics.fmean(row.social_misidentifications for row in rows),
        mean_stale_rollbacks=statistics.fmean(row.stale_rollbacks for row in rows),
        mean_fork_conflicts=statistics.fmean(row.fork_conflicts for row in rows),
    )


def build_verdicts(summary_rows: Sequence[SummaryRow]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        rows = {row.condition: row for row in summary_rows if row.scenario == scenario.index}
        full = rows["full_continuity_record"]
        model_only = rows["model_only_copy"]
        memory_transplant = rows["memory_only_transplant"]
        body_ablation = rows["body_hidden_ablation"]
        social_ablation = rows["social_memory_reset"]
        commitment_ablation = rows["commitment_ledger_reset"]
        tool_ablation = rows["tool_inventory_reset"]
        fork_ablation = rows["fork_without_branch_id"]
        full_gain = full.mean_reward - model_only.mean_reward
        body_loss = full.mean_reward - body_ablation.mean_reward
        social_loss = full.mean_reward - social_ablation.mean_reward
        commitment_loss = full.mean_reward - commitment_ablation.mean_reward
        tool_loss = full.mean_reward - tool_ablation.mean_reward
        fork_loss = full.mean_reward - fork_ablation.mean_reward

        if scenario.index == 0:
            supports = full_gain > 35.0 and commitment_loss > 15.0 and social_loss < 8.0 and tool_loss < 8.0
            verdict = "continuity_record_preserves_clean_resume" if supports else "clean_resume_boundary_unclear"
        elif scenario.index == 1:
            supports = body_loss > 60.0 and full_gain > 80.0 and memory_transplant.mean_reward < full.mean_reward - 45.0
            verdict = "body_hidden_state_required_for_same_agent" if supports else "body_model_mismatch_not_specific"
        elif scenario.index == 2:
            supports = social_loss > 35.0 and commitment_loss > 25.0 and full.mean_social_coherence > social_ablation.mean_social_coherence + 0.5
            verdict = "social_continuity_preserves_repair_relationships" if supports else "social_continuity_not_specific"
        elif scenario.index == 3:
            supports = tool_loss > 18.0 and commitment_loss > 30.0 and social_loss < 8.0
            verdict = "tools_and_commitments_bind_externalized_continuity" if supports else "tool_commitment_boundary_unclear"
        else:
            clean_fork = rows["clean_fork_branch"]
            supports = (
                fork_loss > 70.0
                and full.mean_reward > fork_ablation.mean_reward + 70.0
                and clean_fork.mean_reward > fork_ablation.mean_reward + 70.0
                and fork_ablation.mean_fork_conflicts > full.mean_fork_conflicts + 0.5
            )
            verdict = "forks_are_new_continuities_after_shared_history" if supports else "fork_boundary_unclear"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                full_record_reward=full.mean_reward,
                model_only_reward=model_only.mean_reward,
                memory_transplant_reward=memory_transplant.mean_reward,
                body_ablation_reward=body_ablation.mean_reward,
                social_ablation_reward=social_ablation.mean_reward,
                commitment_ablation_reward=commitment_ablation.mean_reward,
                tool_ablation_reward=tool_ablation.mean_reward,
                fork_ablation_reward=fork_ablation.mean_reward,
                full_gain_over_model_only=full_gain,
                body_ablation_loss=body_loss,
                social_ablation_loss=social_loss,
                commitment_ablation_loss=commitment_loss,
                tool_ablation_loss=tool_loss,
                fork_ablation_loss=fork_loss,
                supports_agent_continuity_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: ContinuityConfig,
) -> Tuple[List[EpisodeResult], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    all_rows: List[EpisodeResult] = []
    summary_rows: List[SummaryRow] = []
    trace: Optional[Dict[str, object]] = None
    all_conditions = conditions()
    for scenario in SCENARIOS:
        for condition in all_conditions:
            rows = evaluate(condition, scenario, cfg)
            all_rows.extend(rows)
            summary_rows.append(summarize(rows, scenario, condition.name))
            if scenario.index == cfg.trace_scenario and condition.name == "full_continuity_record":
                trace_result, trace = run_episode(
                    scenario,
                    condition,
                    cfg.trace_episode + 10_000,
                    cfg,
                    collect_trace=True,
                )
                all_rows.append(trace_result)
    verdicts = build_verdicts(summary_rows)
    diagnostics = {
        "note": (
            "Continuity is treated as a binding record over body, model, memory, "
            "social history, commitments, event log, attention, hidden state, tools, "
            "goals, and branch identity. Model weights alone are not continuity."
        ),
        "conditions": [asdict(condition) for condition in all_conditions],
        "trace": trace,
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
        "full_reward",
        "model_only",
        "memory_transplant",
        "body_loss",
        "social_loss",
        "commitment_loss",
        "tool_loss",
        "fork_loss",
        "supports_agent_continuity_precursor",
    ]
    rows = [
        [
            str(row.scenario),
            row.scenario_name,
            f"{row.full_record_reward:.3f}",
            f"{row.model_only_reward:.3f}",
            f"{row.memory_transplant_reward:.3f}",
            f"{row.body_ablation_loss:.3f}",
            f"{row.social_ablation_loss:.3f}",
            f"{row.commitment_ablation_loss:.3f}",
            f"{row.tool_ablation_loss:.3f}",
            f"{row.fork_ablation_loss:.3f}",
            str(row.supports_agent_continuity_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> ContinuityConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=120)
    parser.add_argument("--seed", type=int, default=20260613)
    parser.add_argument("--trace-scenario", type=int, default=4)
    parser.add_argument("--trace-episode", type=int, default=0)
    args = parser.parse_args()
    if args.episodes < 12:
        raise SystemExit("--episodes must be at least 12")
    if args.trace_scenario not in {scenario.index for scenario in SCENARIOS}:
        raise SystemExit("--trace-scenario out of range")
    return ContinuityConfig(
        episodes=args.episodes,
        seed=args.seed,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    episode_rows, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    episode_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_eval.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_agent_continuity_trace.js"
    write_csv(episode_path, episode_rows)
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
    write_js_data(results_js_path, "SSRM_3D_AGENT_CONTINUITY_RESULTS", results)
    write_js_data(trace_js_path, "SSRM_3D_AGENT_CONTINUITY_TRACE", diagnostics["trace"])
    print(f"wrote {episode_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"wrote {trace_path}")
    print(f"wrote {results_js_path}")
    print(f"wrote {trace_js_path}")
    print_table(verdicts)
    return 0 if all(row.supports_agent_continuity_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
