#!/usr/bin/env python3
"""Interruption and coherence experiment.

The task tests self as a coherence stabilizer. An agent begins a set of
commitments, completes some, is interrupted, and resumes from a corrupted
memory bundle containing own commitments, stale commitments, foreign
commitments, duplicates, and occasional contradictory cancel records.

The question is whether a persistent self/commitment index helps the agent
recover the right continuation target: my current commitments that remain
pending, not every remembered or high-priority item.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Counter as CounterType, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from self_world_attribution import stable_episode_seed


@dataclass(frozen=True)
class CoherenceConfig:
    episodes: int = 500
    own_commitments: int = 6
    action_budget: int = 9
    seed: int = 20260530


@dataclass(frozen=True)
class MemoryItem:
    item_id: str
    goal_id: str
    owner_id: str
    epoch: int
    kind: str
    status_hint: str
    priority: float


@dataclass
class EpisodeState:
    scenario: str
    episode: int
    own_id: str
    foreign_id: str
    current_epoch: int
    own_goals: List[str]
    pre_completed: Set[str]
    memory: List[MemoryItem]


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    coherent_success: bool
    own_completion_rate: float
    abandoned_own: int
    foreign_actions: int
    stale_actions: int
    duplicate_actions: int
    contradiction_actions: int
    total_value: float
    actions_used: int


class ContinuationWorld:
    def __init__(self, state: EpisodeState) -> None:
        self.state = state
        self.completed: Set[str] = set(state.pre_completed)
        self.pending: Set[str] = set(state.own_goals) - self.completed
        self.value = 0.0
        self.counts: CounterType[str] = Counter()

    def execute(self, item: MemoryItem) -> None:
        if item.kind == "cancel":
            if item.owner_id == self.state.own_id and item.epoch == self.state.current_epoch:
                self.counts["contradiction"] += 1
                self.value -= 10.0
            elif item.owner_id == self.state.own_id:
                self.counts["stale"] += 1
                self.value -= 6.0
            else:
                self.counts["foreign"] += 1
                self.value -= 8.0
            return

        if item.owner_id != self.state.own_id:
            self.counts["foreign"] += 1
            self.value -= 8.0
            return

        if item.epoch != self.state.current_epoch:
            self.counts["stale"] += 1
            self.value -= 6.0
            return

        if item.goal_id in self.pending:
            self.pending.remove(item.goal_id)
            self.completed.add(item.goal_id)
            self.value += 10.0
            return

        self.counts["duplicate"] += 1
        self.value -= 5.0

    def finalize(self, actions_used: int, agent_name: str) -> EpisodeResult:
        abandoned = len(self.pending)
        total_value = self.value - 8.0 * abandoned
        bad_actions = (
            self.counts["foreign"]
            + self.counts["stale"]
            + self.counts["duplicate"]
            + self.counts["contradiction"]
        )
        coherent_success = abandoned == 0 and bad_actions == 0
        initial_pending = len(set(self.state.own_goals) - self.state.pre_completed)
        completion_rate = 1.0 if initial_pending == 0 else 1.0 - abandoned / initial_pending
        return EpisodeResult(
            scenario=self.state.scenario,
            agent=agent_name,
            coherent_success=coherent_success,
            own_completion_rate=completion_rate,
            abandoned_own=abandoned,
            foreign_actions=self.counts["foreign"],
            stale_actions=self.counts["stale"],
            duplicate_actions=self.counts["duplicate"],
            contradiction_actions=self.counts["contradiction"],
            total_value=total_value,
            actions_used=actions_used,
        )


class BaseAgent:
    name = "base"

    def reset(self, state: EpisodeState) -> None:
        self.state = state
        self.used_items: Set[str] = set()

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        raise NotImplementedError

    def remember_execution(self, item: MemoryItem) -> None:
        self.used_items.add(item.item_id)

    def available(self) -> List[MemoryItem]:
        return [item for item in self.state.memory if item.item_id not in self.used_items]


class VisiblePriorityAgent(BaseAgent):
    name = "visible_priority_only"

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        items = self.available()
        if not items:
            return None
        return max(items, key=lambda item: (item.priority, item.status_hint == "pending", item.item_id))


class GenericMemoryAgent(BaseAgent):
    name = "generic_memory_no_identity"

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        candidates = [
            item
            for item in self.available()
            if item.status_hint in {"pending", "unknown"}
        ]
        if not candidates:
            return None
        return max(candidates, key=lambda item: (item.status_hint == "pending", item.priority, item.item_id))


class CurrentGoalOnlyAgent(BaseAgent):
    name = "current_goal_only"

    def reset(self, state: EpisodeState) -> None:
        super().reset(state)
        self.current_goal = max(state.memory, key=lambda item: item.priority).goal_id

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        candidates = [
            item
            for item in self.available()
            if item.goal_id == self.current_goal and item.status_hint != "done"
        ]
        if not candidates:
            return None
        return max(candidates, key=lambda item: (item.priority, item.item_id))


class IdentityAblationAgent(GenericMemoryAgent):
    name = "identity_metadata_ablation"


class IdentityContinuityAgent(BaseAgent):
    name = "identity_continuity_ledger"

    def reset(self, state: EpisodeState) -> None:
        super().reset(state)
        self.ledger_completed = set(state.pre_completed)
        self.done_after_resume: Set[str] = set()

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        candidates = []
        for item in self.available():
            if item.owner_id != self.state.own_id:
                continue
            if item.epoch != self.state.current_epoch:
                continue
            if item.kind != "deliver":
                continue
            if item.goal_id in self.ledger_completed or item.goal_id in self.done_after_resume:
                continue
            candidates.append(item)
        if not candidates:
            return None
        return max(candidates, key=lambda item: (item.priority, item.item_id))

    def remember_execution(self, item: MemoryItem) -> None:
        super().remember_execution(item)
        if (
            item.owner_id == self.state.own_id
            and item.epoch == self.state.current_epoch
            and item.kind == "deliver"
        ):
            self.done_after_resume.add(item.goal_id)


class OracleContinuationAgent(BaseAgent):
    name = "oracle_continuity"

    def choose(self, world: ContinuationWorld) -> Optional[MemoryItem]:
        if not world.pending:
            return None
        target = sorted(world.pending)[0]
        candidates = [
            item
            for item in self.available()
            if item.owner_id == self.state.own_id
            and item.epoch == self.state.current_epoch
            and item.kind == "deliver"
            and item.goal_id == target
        ]
        if candidates:
            return max(candidates, key=lambda item: (item.priority, item.item_id))
        return MemoryItem(
            item_id=f"oracle-{target}",
            goal_id=target,
            owner_id=self.state.own_id,
            epoch=self.state.current_epoch,
            kind="deliver",
            status_hint="pending",
            priority=1.0,
        )


def make_episode_state(scenario: str, episode: int, cfg: CoherenceConfig) -> EpisodeState:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    own_id = f"agent-{episode % 23}"
    foreign_id = f"agent-{(episode + 7) % 23}"
    current_epoch = 1000 + episode
    own_goals = [f"goal-{idx}" for idx in range(cfg.own_commitments)]
    completed_count = rng.randint(1, max(1, cfg.own_commitments // 2))
    pre_completed = set(rng.sample(own_goals, completed_count))
    memory: List[MemoryItem] = []

    for goal_id in own_goals:
        status = "done" if goal_id in pre_completed else "pending"
        if scenario == "corrupted_mixed" and goal_id not in pre_completed and rng.random() < 0.25:
            status = "done"
        memory.append(
            make_item(
                rng,
                "own",
                goal_id,
                own_id,
                current_epoch,
                "deliver",
                status,
                priority=rng.uniform(0.35, 0.85),
            )
        )

    if scenario in {"foreign_memory", "corrupted_mixed"}:
        add_foreign_items(memory, rng, foreign_id, current_epoch, count=4)

    if scenario in {"stale_self", "corrupted_mixed"}:
        add_stale_items(memory, rng, own_id, current_epoch - 1, count=3)

    if scenario == "corrupted_mixed":
        for goal_id in pre_completed:
            if rng.random() < 0.75:
                memory.append(
                    make_item(
                        rng,
                        "duplicate",
                        goal_id,
                        own_id,
                        current_epoch,
                        "deliver",
                        "pending",
                        priority=rng.uniform(0.75, 1.0),
                    )
                )
        for goal_id in sorted(set(own_goals) - pre_completed)[:2]:
            memory.append(
                make_item(
                    rng,
                    "cancel",
                    goal_id,
                    own_id,
                    current_epoch,
                    "cancel",
                    "pending",
                    priority=rng.uniform(0.8, 1.0),
                )
            )

    rng.shuffle(memory)
    return EpisodeState(
        scenario=scenario,
        episode=episode,
        own_id=own_id,
        foreign_id=foreign_id,
        current_epoch=current_epoch,
        own_goals=own_goals,
        pre_completed=pre_completed,
        memory=memory,
    )


def make_item(
    rng: random.Random,
    prefix: str,
    goal_id: str,
    owner_id: str,
    epoch: int,
    kind: str,
    status_hint: str,
    priority: float,
) -> MemoryItem:
    return MemoryItem(
        item_id=f"{prefix}-{goal_id}-{epoch}-{rng.randrange(10**9)}",
        goal_id=goal_id,
        owner_id=owner_id,
        epoch=epoch,
        kind=kind,
        status_hint=status_hint,
        priority=priority,
    )


def add_foreign_items(
    memory: List[MemoryItem],
    rng: random.Random,
    foreign_id: str,
    epoch: int,
    count: int,
) -> None:
    for idx in range(count):
        memory.append(
            make_item(
                rng,
                "foreign",
                f"foreign-goal-{idx}",
                foreign_id,
                epoch,
                "deliver",
                "pending",
                priority=rng.uniform(0.65, 1.0),
            )
        )


def add_stale_items(
    memory: List[MemoryItem],
    rng: random.Random,
    own_id: str,
    old_epoch: int,
    count: int,
) -> None:
    for idx in range(count):
        memory.append(
            make_item(
                rng,
                "stale",
                f"old-goal-{idx}",
                own_id,
                old_epoch,
                "deliver",
                "pending",
                priority=rng.uniform(0.6, 1.0),
            )
        )


def run_episode(agent: BaseAgent, state: EpisodeState, cfg: CoherenceConfig) -> EpisodeResult:
    world = ContinuationWorld(state)
    agent.reset(state)
    actions_used = 0
    for _ in range(cfg.action_budget):
        item = agent.choose(world)
        if item is None:
            break
        world.execute(item)
        agent.remember_execution(item)
        actions_used += 1
    return world.finalize(actions_used, agent.name)


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)

    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "coherent_success_rate": rate(item.coherent_success for item in items),
                "mean_own_completion_rate": statistics.fmean(
                    item.own_completion_rate for item in items
                ),
                "mean_abandoned_own": statistics.fmean(item.abandoned_own for item in items),
                "mean_foreign_actions": statistics.fmean(item.foreign_actions for item in items),
                "mean_stale_actions": statistics.fmean(item.stale_actions for item in items),
                "mean_duplicate_actions": statistics.fmean(
                    item.duplicate_actions for item in items
                ),
                "mean_contradiction_actions": statistics.fmean(
                    item.contradiction_actions for item in items
                ),
                "mean_total_value": statistics.fmean(item.total_value for item in items),
                "mean_actions_used": statistics.fmean(item.actions_used for item in items),
            }
        )
    return rows


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def write_outputs(rows: Sequence[Dict[str, object]], cfg: CoherenceConfig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "interruption_coherence_results.json"
    csv_path = output_dir / "interruption_coherence_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump({"config": asdict(cfg), "summary": list(rows)}, handle, indent=2)
        handle.write("\n")

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "agent",
        "coherent_success_rate",
        "mean_own_completion_rate",
        "mean_abandoned_own",
        "mean_foreign_actions",
        "mean_stale_actions",
        "mean_duplicate_actions",
        "mean_contradiction_actions",
        "mean_total_value",
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
    parser.add_argument("--episodes", type=int, default=CoherenceConfig.episodes)
    parser.add_argument("--own-commitments", type=int, default=CoherenceConfig.own_commitments)
    parser.add_argument("--action-budget", type=int, default=CoherenceConfig.action_budget)
    parser.add_argument("--seed", type=int, default=CoherenceConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = CoherenceConfig(
        episodes=args.episodes,
        own_commitments=args.own_commitments,
        action_budget=args.action_budget,
        seed=args.seed,
    )
    scenarios = ["clean_resume", "foreign_memory", "stale_self", "corrupted_mixed"]
    agent_factories = [
        VisiblePriorityAgent,
        GenericMemoryAgent,
        CurrentGoalOnlyAgent,
        IdentityAblationAgent,
        IdentityContinuityAgent,
        OracleContinuationAgent,
    ]
    results: List[EpisodeResult] = []
    for scenario in scenarios:
        for episode in range(cfg.episodes):
            state = make_episode_state(scenario, episode, cfg)
            for agent_factory in agent_factories:
                results.append(run_episode(agent_factory(), state, cfg))
    rows = summarize(results)
    write_outputs(rows, cfg, args.output_dir)
    print_summary(rows)


if __name__ == "__main__":
    main()
