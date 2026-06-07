"""Evaluation metrics for software repair policies."""

from __future__ import annotations

from statistics import mean
from typing import Dict, Iterable, List

from .critics import POLICIES, weakest_channel_score, weighted_quality_score
from .models import EvalRow, RepairTask, SummaryRow, VerdictRow


def evaluate_policy(policy_name: str, tasks: Iterable[RepairTask]) -> List[EvalRow]:
    chooser = POLICIES[policy_name]
    rows: List[EvalRow] = []
    for task in tasks:
        selected = chooser(task)
        rows.append(
            EvalRow(
                policy=policy_name,
                task_id=task.task_id,
                selected_repair=selected.repair_id,
                expected_best_repair=task.expected_best_repair,
                visible_pass=selected.visible_test_result,
                hidden_pass=selected.hidden_test_result,
                wrong_fix=selected.repair_id != task.expected_best_repair,
                root_cause_repair=selected.root_cause_score >= 0.80,
                regression_avoided=selected.regression_risk <= 0.25,
                weakest_channel_score=round(weakest_channel_score(task, selected), 6),
                mean_repair_quality=round(weighted_quality_score(task, selected), 6),
                root_cause_score=selected.root_cause_score,
                regression_risk=selected.regression_risk,
                api_contract_score=selected.api_contract_score,
                security_score=selected.security_score,
                maintainability_score=selected.maintainability_score,
                performance_score=selected.performance_score,
                reviewability_score=selected.reviewability_score,
            )
        )
    return rows


def summarize(rows: Iterable[EvalRow]) -> List[SummaryRow]:
    rows_by_policy: Dict[str, List[EvalRow]] = {}
    for row in rows:
        rows_by_policy.setdefault(row.policy, []).append(row)

    summaries: List[SummaryRow] = []
    for policy, policy_rows in sorted(rows_by_policy.items()):
        summaries.append(
            SummaryRow(
                policy=policy,
                task_count=len(policy_rows),
                visible_pass_rate=round(mean(1.0 if row.visible_pass else 0.0 for row in policy_rows), 6),
                hidden_pass_rate=round(mean(1.0 if row.hidden_pass else 0.0 for row in policy_rows), 6),
                wrong_fix_rate=round(mean(1.0 if row.wrong_fix else 0.0 for row in policy_rows), 6),
                root_cause_repair_rate=round(mean(1.0 if row.root_cause_repair else 0.0 for row in policy_rows), 6),
                regression_avoidance_rate=round(mean(1.0 if row.regression_avoided else 0.0 for row in policy_rows), 6),
                weakest_channel_score=round(mean(row.weakest_channel_score for row in policy_rows), 6),
                oracle_match_rate=round(mean(0.0 if row.wrong_fix else 1.0 for row in policy_rows), 6),
                mean_repair_quality=round(mean(row.mean_repair_quality for row in policy_rows), 6),
            )
        )
    return summaries


def build_verdict(summary: Iterable[SummaryRow]) -> VerdictRow:
    by_policy = {row.policy: row for row in summary}
    visible = by_policy["visible_test_only"]
    min_channel = by_policy["min_channel_critic"]

    hidden_pass_gain = round(min_channel.hidden_pass_rate - visible.hidden_pass_rate, 6)
    wrong_fix_reduction = round(visible.wrong_fix_rate - min_channel.wrong_fix_rate, 6)
    root_cause_gain = round(min_channel.root_cause_repair_rate - visible.root_cause_repair_rate, 6)
    weakest_channel_gain = round(min_channel.weakest_channel_score - visible.weakest_channel_score, 6)
    supports = (
        hidden_pass_gain > 0.0
        and wrong_fix_reduction > 0.0
        and root_cause_gain > 0.0
        and weakest_channel_gain > 0.0
    )
    return VerdictRow(
        visible_hidden_pass_rate=visible.hidden_pass_rate,
        min_channel_hidden_pass_rate=min_channel.hidden_pass_rate,
        visible_wrong_fix_rate=visible.wrong_fix_rate,
        min_channel_wrong_fix_rate=min_channel.wrong_fix_rate,
        visible_root_cause_repair_rate=visible.root_cause_repair_rate,
        min_channel_root_cause_repair_rate=min_channel.root_cause_repair_rate,
        visible_weakest_channel_score=visible.weakest_channel_score,
        min_channel_weakest_channel_score=min_channel.weakest_channel_score,
        hidden_pass_gain=hidden_pass_gain,
        wrong_fix_reduction=wrong_fix_reduction,
        root_cause_gain=root_cause_gain,
        weakest_channel_gain=weakest_channel_gain,
        supports_programmable_repair_bridge=supports,
        verdict="pass" if supports else "partial_or_failed",
    )


def evaluate(tasks: Iterable[RepairTask]) -> tuple[List[EvalRow], List[SummaryRow], VerdictRow]:
    all_rows: List[EvalRow] = []
    for policy_name in POLICIES:
        all_rows.extend(evaluate_policy(policy_name, tasks))
    summary = summarize(all_rows)
    verdict = build_verdict(summary)
    return all_rows, summary, verdict
