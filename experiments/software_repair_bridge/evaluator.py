"""Evaluation metrics for software repair policies."""

from __future__ import annotations

from statistics import mean
from typing import Dict, Iterable, List

from .critics import POLICIES, weakest_channel_score, weighted_quality_score
from .models import (
    EvalRow,
    PolicyDecision,
    RepairTask,
    SummaryRow,
    VerdictRow,
)


FALSE_POSITIVE_THRESHOLD = 0.20
OVERBLOCKING_THRESHOLD = 0.35


def _block_row(task: RepairTask, policy_name: str, decision: PolicyDecision) -> EvalRow:
    expected_exists = any(candidate.repair_id == task.expected_best_repair for candidate in task.candidate_repairs)
    is_fp = expected_exists
    return EvalRow(
        policy=policy_name,
        task_id=task.task_id,
        selected_repair="REVIEW_REQUIRED",
        expected_best_repair=task.expected_best_repair,
        visible_pass=False,
        hidden_pass=False,
        blocked_for_review=True,
        false_positive=is_fp,
        false_negative=False,
        block_reason=decision.reason or "manual-review block",
        wrong_fix=False,
        root_cause_repair=False,
        regression_avoided=False,
        weakest_channel_score=0.0,
        mean_repair_quality=0.0,
        root_cause_score=0.0,
        regression_risk=1.0,
        api_contract_score=0.0,
        security_score=0.0,
        maintainability_score=0.0,
        performance_score=0.0,
        reviewability_score=0.0,
        migration_rollback_risk=1.0,
        observability_score=0.0,
        is_held_out_family=task.is_held_out_family,
    )


def _selected_row(task: RepairTask, policy_name: str, candidate_id: str) -> EvalRow:
    candidate = next(c for c in task.candidate_repairs if c.repair_id == candidate_id)
    wrong_fix = candidate.repair_id != task.expected_best_repair
    return EvalRow(
        policy=policy_name,
        task_id=task.task_id,
        selected_repair=candidate.repair_id,
        expected_best_repair=task.expected_best_repair,
        visible_pass=candidate.visible_test_result,
        hidden_pass=candidate.hidden_test_result,
        blocked_for_review=False,
        false_positive=False,
        false_negative=wrong_fix,
        block_reason="",
        wrong_fix=wrong_fix,
        root_cause_repair=candidate.root_cause_score >= 0.80,
        regression_avoided=candidate.regression_risk <= 0.25,
        weakest_channel_score=round(weakest_channel_score(task, candidate), 6),
        mean_repair_quality=round(weighted_quality_score(task, candidate), 6),
        root_cause_score=round(candidate.root_cause_score, 6),
        regression_risk=round(candidate.regression_risk, 6),
        api_contract_score=round(candidate.api_contract_score, 6),
        security_score=round(candidate.security_score, 6),
        maintainability_score=round(candidate.maintainability_score, 6),
        performance_score=round(candidate.performance_score, 6),
        reviewability_score=round(candidate.reviewability_score, 6),
        migration_rollback_risk=round(candidate.migration_rollback_risk, 6),
        observability_score=round(candidate.observability_score, 6),
        is_held_out_family=task.is_held_out_family,
    )


def _score_row(task: RepairTask, policy_name: str, decision: PolicyDecision) -> EvalRow:
    if decision.blocked_for_review:
        return _block_row(task, policy_name, decision)
    if decision.candidate is None:
        raise ValueError(f"policy {policy_name} returned blocked decision without reason on {task.task_id}")
    return _selected_row(task, policy_name, decision.candidate.repair_id)


def evaluate_policy(policy_name: str, tasks: Iterable[RepairTask]) -> List[EvalRow]:
    chooser = POLICIES[policy_name]
    rows: List[EvalRow] = []
    for task in tasks:
        decision = chooser(task)
        rows.append(_score_row(task, policy_name, decision))
    return rows


def _safe_mean(values: Iterable[float]) -> float:
    values = list(values)
    if not values:
        return 0.0
    return round(mean(values), 6)


def _summarize_policy_rows(policy_rows: List[EvalRow], policy: str, split: str) -> SummaryRow:
    if split == "seen":
        selected_rows = [row for row in policy_rows if not row.is_held_out_family]
    elif split == "held_out":
        selected_rows = [row for row in policy_rows if row.is_held_out_family]
    else:
        selected_rows = policy_rows

    if not selected_rows:
        return SummaryRow(
            policy=policy,
            task_count=0,
            task_split=split,
            visible_pass_rate=0.0,
            hidden_pass_rate=0.0,
            wrong_fix_rate=0.0,
            false_positive_rate=0.0,
            false_negative_rate=0.0,
            root_cause_repair_rate=0.0,
            regression_avoidance_rate=0.0,
            security_preservation_rate=0.0,
            weakest_channel_score=0.0,
            mean_repair_quality=0.0,
            oracle_match_rate=0.0,
            overblocking_rate=0.0,
            underblocking_rate=0.0,
            migration_rollback_preservation_rate=0.0,
            observability_rate=0.0,
        )

    return SummaryRow(
        policy=policy,
        task_count=len(selected_rows),
        task_split=split,
        visible_pass_rate=_safe_mean(1.0 if row.visible_pass else 0.0 for row in selected_rows),
        hidden_pass_rate=_safe_mean(1.0 if row.hidden_pass else 0.0 for row in selected_rows),
        wrong_fix_rate=_safe_mean(1.0 if row.wrong_fix else 0.0 for row in selected_rows),
        false_positive_rate=_safe_mean(1.0 if row.false_positive else 0.0 for row in selected_rows),
        false_negative_rate=_safe_mean(1.0 if row.false_negative else 0.0 for row in selected_rows),
        root_cause_repair_rate=_safe_mean(1.0 if row.root_cause_repair else 0.0 for row in selected_rows),
        regression_avoidance_rate=_safe_mean(1.0 if row.regression_avoided else 0.0 for row in selected_rows),
        security_preservation_rate=_safe_mean(1.0 if row.security_score >= 0.80 else 0.0 for row in selected_rows),
        weakest_channel_score=_safe_mean(row.weakest_channel_score for row in selected_rows),
        mean_repair_quality=_safe_mean(row.mean_repair_quality for row in selected_rows),
        oracle_match_rate=_safe_mean(1.0 if not row.wrong_fix else 0.0 for row in selected_rows),
        overblocking_rate=_safe_mean(1.0 if row.blocked_for_review else 0.0 for row in selected_rows),
        underblocking_rate=_safe_mean(1.0 if (not row.blocked_for_review and row.wrong_fix) else 0.0 for row in selected_rows),
        migration_rollback_preservation_rate=_safe_mean(1.0 if row.migration_rollback_risk <= 0.20 else 0.0 for row in selected_rows),
        observability_rate=_safe_mean(1.0 if row.observability_score >= 0.80 else 0.0 for row in selected_rows),
    )


def summarize(rows: Iterable[EvalRow]) -> List[SummaryRow]:
    rows_by_policy: Dict[str, List[EvalRow]] = {}
    for row in rows:
        rows_by_policy.setdefault(row.policy, []).append(row)

    summaries: List[SummaryRow] = []
    for policy, policy_rows in sorted(rows_by_policy.items()):
        for split in ("all", "seen", "held_out"):
            summaries.append(_summarize_policy_rows(policy_rows, policy, split))
    return summaries


def _policy_row(summary: Iterable[SummaryRow], policy: str, split: str) -> SummaryRow:
    for row in summary:
        if row.policy == policy and row.task_split == split:
            return row
    raise KeyError(f"missing summary for policy {policy!r} split {split!r}")


def build_verdict(summary: Iterable[SummaryRow]) -> VerdictRow:
    all_rows = list(summary)
    visible = _policy_row(all_rows, "visible_test_only", "all")
    policy_rows = [
        row
        for row in all_rows
        if row.policy not in {"visible_test_only", "oracle"} and row.task_split == "all"
    ]
    if not policy_rows:
        raise ValueError("no non-oracle policies available for verdict")

    def total_score(row: SummaryRow) -> tuple[float, float, float, float, float]:
        return (
            row.hidden_pass_rate - visible.hidden_pass_rate,
            visible.wrong_fix_rate - row.wrong_fix_rate,
            row.root_cause_repair_rate - visible.root_cause_repair_rate,
            row.regression_avoidance_rate - visible.regression_avoidance_rate,
            row.weakest_channel_score - visible.weakest_channel_score,
        )

    best_policy = max(policy_rows, key=total_score)
    best = best_policy

    visible_hidden_gain = round(best.hidden_pass_rate - visible.hidden_pass_rate, 6)
    visible_wrong_fix_gain = round(visible.wrong_fix_rate - best.wrong_fix_rate, 6)
    visible_root_cause_gain = round(best.root_cause_repair_rate - visible.root_cause_repair_rate, 6)
    visible_regression_gain = round(best.regression_avoidance_rate - visible.regression_avoidance_rate, 6)
    visible_weakest_gain = round(best.weakest_channel_score - visible.weakest_channel_score, 6)

    false_positive_ok = best.false_positive_rate <= FALSE_POSITIVE_THRESHOLD
    overblocking_ok = best.overblocking_rate <= OVERBLOCKING_THRESHOLD
    supports = (
        visible_hidden_gain > 0.0
        and visible_wrong_fix_gain > 0.0
        and visible_regression_gain > 0.0
        and visible_weakest_gain > 0.0
        and false_positive_ok
        and overblocking_ok
    )

    return VerdictRow(
        visible_policy="visible_test_only",
        best_policy=best.policy,
        visible_hidden_pass_rate=visible.hidden_pass_rate,
        best_hidden_pass_rate=best.hidden_pass_rate,
        visible_wrong_fix_rate=visible.wrong_fix_rate,
        best_wrong_fix_rate=best.wrong_fix_rate,
        visible_root_cause_repair_rate=visible.root_cause_repair_rate,
        best_root_cause_repair_rate=best.root_cause_repair_rate,
        visible_regression_avoidance_rate=visible.regression_avoidance_rate,
        best_regression_avoidance_rate=best.regression_avoidance_rate,
        visible_weakest_channel_score=visible.weakest_channel_score,
        best_weakest_channel_score=best.weakest_channel_score,
        hidden_pass_gain=visible_hidden_gain,
        wrong_fix_reduction=visible_wrong_fix_gain,
        root_cause_gain=visible_root_cause_gain,
        weakest_channel_gain=visible_weakest_gain,
        false_positive_rate=best.false_positive_rate,
        overblocking_rate=best.overblocking_rate,
        underblocking_rate=best.underblocking_rate,
        meets_thresholds=(false_positive_ok and overblocking_ok),
        supports_programmable_repair_bridge=supports,
        verdict="pass" if supports else "partial_or_failed",
    )


def evaluate(tasks: Iterable[RepairTask]) -> tuple[List[EvalRow], List[SummaryRow], VerdictRow]:
    all_rows: List[EvalRow] = []
    for policy_name in sorted(POLICIES.keys()):
        all_rows.extend(evaluate_policy(policy_name, tasks))
    summary = summarize(all_rows)
    verdict = build_verdict(summary)
    return all_rows, summary, verdict
