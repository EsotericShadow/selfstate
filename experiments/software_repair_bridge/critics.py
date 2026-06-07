"""Baseline repair selection policies."""

from __future__ import annotations

from typing import Callable, Dict

from .models import RepairCandidate, RepairTask


QUALITY_WEIGHTS: Dict[str, float] = {
    "visible_test": 0.10,
    "hidden_test": 0.20,
    "root_cause": 0.20,
    "regression_risk": 0.15,
    "api_contract_safety": 0.10,
    "security": 0.10,
    "maintainability": 0.07,
    "performance": 0.05,
    "reviewability": 0.03,
}


def weakest_channel_score(task: RepairTask, candidate: RepairCandidate) -> float:
    scores = candidate.channel_scores()
    return min(scores[channel] for channel in task.correctness_channels)


def weighted_quality_score(task: RepairTask, candidate: RepairCandidate) -> float:
    scores = candidate.channel_scores()
    total_weight = sum(QUALITY_WEIGHTS[channel] for channel in task.correctness_channels)
    return sum(scores[channel] * QUALITY_WEIGHTS[channel] for channel in task.correctness_channels) / total_weight


def visible_test_only(task: RepairTask) -> RepairCandidate:
    for candidate in task.candidate_repairs:
        if candidate.visible_test_result:
            return candidate
    return task.candidate_repairs[0]


def root_cause_first(task: RepairTask) -> RepairCandidate:
    return max(
        task.candidate_repairs,
        key=lambda candidate: (
            candidate.root_cause_score,
            weakest_channel_score(task, candidate),
            weighted_quality_score(task, candidate),
            candidate.repair_id,
        ),
    )


def min_channel_critic(task: RepairTask) -> RepairCandidate:
    return max(
        task.candidate_repairs,
        key=lambda candidate: (
            weakest_channel_score(task, candidate),
            weighted_quality_score(task, candidate),
            candidate.root_cause_score,
            candidate.repair_id,
        ),
    )


def weighted_quality_critic(task: RepairTask) -> RepairCandidate:
    return max(
        task.candidate_repairs,
        key=lambda candidate: (
            weighted_quality_score(task, candidate),
            weakest_channel_score(task, candidate),
            candidate.root_cause_score,
            candidate.repair_id,
        ),
    )


def oracle(task: RepairTask) -> RepairCandidate:
    for candidate in task.candidate_repairs:
        if candidate.repair_id == task.expected_best_repair:
            return candidate
    raise KeyError(f"missing expected repair {task.expected_best_repair!r} for {task.task_id}")


POLICIES: Dict[str, Callable[[RepairTask], RepairCandidate]] = {
    "visible_test_only": visible_test_only,
    "root_cause_first": root_cause_first,
    "min_channel_critic": min_channel_critic,
    "weighted_quality_critic": weighted_quality_critic,
    "oracle": oracle,
}
