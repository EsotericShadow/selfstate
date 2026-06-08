"""Baseline software-repair selection policies."""

from __future__ import annotations

from typing import Callable, Dict, Sequence

from .models import PolicyDecision, RepairCandidate, RepairTask


QUALITY_WEIGHTS: Dict[str, float] = {
    "visible_test": 0.10,
    "hidden_test": 0.20,
    "root_cause": 0.20,
    "regression_risk": 0.15,
    "api_contract_safety": 0.10,
    "security": 0.08,
    "maintainability": 0.07,
    "performance": 0.08,
    "reviewability": 0.04,
    "migration_rollback_safety": 0.06,
    "observability_logging_quality": 0.04,
}


def weakest_channel_score(task: RepairTask, candidate: RepairCandidate) -> float:
    scores = candidate.channel_scores()
    return min(scores[channel] for channel in task.correctness_channels)


def weighted_quality_score(task: RepairTask, candidate: RepairCandidate) -> float:
    scores = candidate.channel_scores()
    total_weight = sum(QUALITY_WEIGHTS[channel] for channel in task.correctness_channels)
    return sum(scores[channel] * QUALITY_WEIGHTS[channel] for channel in task.correctness_channels) / total_weight


def visible_test_only(task: RepairTask) -> PolicyDecision:
    for candidate in task.candidate_repairs:
        if candidate.visible_test_result:
            return PolicyDecision(candidate, "selected first visible candidate")
    return PolicyDecision(task.candidate_repairs[0], "no visible candidate found; fallback to first")


def _max_candidates(
    candidates: Sequence[RepairCandidate],
    key_fn: Callable[[RepairCandidate], tuple],
) -> PolicyDecision:
    return PolicyDecision(max(candidates, key=key_fn))


def root_cause_first(task: RepairTask) -> PolicyDecision:
    return _max_candidates(
        task.candidate_repairs,
        lambda candidate: (
            candidate.root_cause_score,
            weakest_channel_score(task, candidate),
            weighted_quality_score(task, candidate),
            candidate.suspicious_signal * -1.0,
            candidate.repair_id,
        ),
    )


def min_channel_critic(task: RepairTask) -> PolicyDecision:
    return _max_candidates(
        task.candidate_repairs,
        lambda candidate: (
            weakest_channel_score(task, candidate),
            weighted_quality_score(task, candidate),
            candidate.root_cause_score,
            candidate.suspicious_signal * -1.0,
            candidate.repair_id,
        ),
    )


def weighted_quality_critic(task: RepairTask) -> PolicyDecision:
    return _max_candidates(
        task.candidate_repairs,
        lambda candidate: (
            weighted_quality_score(task, candidate),
            weakest_channel_score(task, candidate),
            candidate.suspicious_signal * -1.0,
            candidate.root_cause_score,
            candidate.repair_id,
        ),
    )


def conservative_review_critic(task: RepairTask) -> PolicyDecision:
    decision = min_channel_critic(task)
    candidate = decision.candidate
    if candidate is None:
        return decision

    minimum_channel = weakest_channel_score(task, candidate)
    quality = weighted_quality_score(task, candidate)
    suspicious = candidate.suspicious_signal

    if minimum_channel < 0.72:
        return PolicyDecision(None, "weakest required channel is below review threshold")
    if suspicious > 0.77 and quality < 0.88:
        return PolicyDecision(
            None,
            "suspicious repair with mixed correctness profile requires manual review",
        )
    return decision


def risk_tolerant_shipper(task: RepairTask) -> PolicyDecision:
    visible_candidates = [candidate for candidate in task.candidate_repairs if candidate.visible_test_result]
    if not visible_candidates:
        return _max_candidates(
            task.candidate_repairs,
            lambda candidate: (
                candidate.hidden_test_result,
                candidate.root_cause_score,
                weighted_quality_score(task, candidate),
                candidate.suspicious_signal * -1.0,
                candidate.repair_id,
            ),
        )

    return _max_candidates(
        visible_candidates,
        lambda candidate: (
            candidate.root_cause_score,
            weighted_quality_score(task, candidate),
            candidate.repair_id,
        ),
    )


def oracle(task: RepairTask) -> PolicyDecision:
    for candidate in task.candidate_repairs:
        if candidate.repair_id == task.expected_best_repair:
            return PolicyDecision(candidate, "oracle match")
    raise KeyError(f"missing expected repair {task.expected_best_repair!r} for {task.task_id}")


POLICIES: Dict[str, Callable[[RepairTask], PolicyDecision]] = {
    "visible_test_only": visible_test_only,
    "root_cause_first": root_cause_first,
    "min_channel_critic": min_channel_critic,
    "weighted_quality_critic": weighted_quality_critic,
    "conservative_review_critic": conservative_review_critic,
    "risk_tolerant_shipper": risk_tolerant_shipper,
    "oracle": oracle,
}
