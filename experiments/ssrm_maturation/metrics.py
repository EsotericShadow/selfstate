"""Scoring and verdict logic for multi-day maturation runs."""

from __future__ import annotations

import statistics
from dataclasses import asdict
from typing import Dict, Iterable, Sequence

from .models import EpisodeRow, SummaryRow, VerdictRow


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def summarize(rows: Sequence[EpisodeRow]) -> list[SummaryRow]:
    grouped: Dict[str, list[EpisodeRow]] = {}
    for row in rows:
        grouped.setdefault(row.condition, []).append(row)
    summary: list[SummaryRow] = []
    for condition, items in sorted(grouped.items()):
        summary.append(
            SummaryRow(
                condition=condition,
                mean_maturation_score=mean(row.maturation_score for row in items),
                mean_survival_score=mean(row.survival_score for row in items),
                mean_development_score=mean(row.development_score for row in items),
                mean_knowledge_score=mean(row.knowledge_score for row in items),
                mean_recovery_score=mean(row.recovery_score for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_births=mean(row.births for row in items),
                mean_deaths=mean(row.deaths for row in items),
                mean_architecture_tier=mean(row.architecture_tier for row in items),
                mean_tool_tier=mean(row.tool_tier for row in items),
                mean_architecture_delta=mean(row.architecture_delta for row in items),
                mean_tool_delta=mean(row.tool_delta for row in items),
                mean_culture_delta=mean(row.culture_delta for row in items),
                mean_risk_memory_delta=mean(row.risk_memory_delta for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                mean_adaptation_evidence=mean(row.adaptation_evidence for row in items),
                shock_gate_pass_rate=mean(1.0 if row.no_major_shock_before_12h else 0.0 for row in items),
                post_gate_shock_rate=mean(1.0 if row.post_gate_shock else 0.0 for row in items),
            )
        )
    return summary


def verdict_from_summary(summary: Sequence[SummaryRow]) -> VerdictRow:
    by_name = {row.condition: row for row in summary}
    full = by_name["integrated_maturation"]
    reactive = by_name["reactive_survival_only"]
    no_teaching = by_name["no_teaching_lineage"]
    no_risk = by_name["no_risk_memory"]
    no_infra = by_name["no_infrastructure_memory"]
    no_tool = by_name["no_tool_improvement"]
    no_social = by_name["no_social_learning"]
    no_sensing = by_name["no_environmental_sensing"]
    reactive_loss = full.mean_maturation_score - reactive.mean_maturation_score
    teaching_loss = full.mean_knowledge_transfer - no_teaching.mean_knowledge_transfer
    risk_loss = full.mean_recovery_score - no_risk.mean_recovery_score
    infra_loss = full.mean_architecture_delta - no_infra.mean_architecture_delta
    tool_loss = full.mean_tool_delta - no_tool.mean_tool_delta
    social_loss = full.mean_culture_delta - no_social.mean_culture_delta
    sensing_loss = full.mean_maturation_score - no_sensing.mean_maturation_score
    supports_window = (
        full.shock_gate_pass_rate == 1.0
        and full.post_gate_shock_rate == 1.0
        and full.mean_alive_at_12h >= 12.0
        and full.mean_development_score >= 0.50
    )
    supports_maturation = (
        full.mean_maturation_score >= 0.72
        and full.mean_final_alive >= 10.0
        and full.mean_architecture_tier >= 2.0
        and full.mean_tool_tier >= 2.0
        and full.mean_knowledge_transfer >= 0.44
        and full.mean_adaptation_evidence >= 0.42
        and full.mean_births >= 1.0
    )
    supports_ablation = (
        reactive_loss >= 0.18
        and teaching_loss >= 0.12
        and risk_loss >= 0.040
        and infra_loss >= 0.24
        and tool_loss >= 0.40
        and social_loss >= 0.35
        and sensing_loss >= 0.020
    )
    return VerdictRow(
        integrated_score=full.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        no_teaching_score=no_teaching.mean_maturation_score,
        no_risk_memory_score=no_risk.mean_maturation_score,
        no_infrastructure_memory_score=no_infra.mean_maturation_score,
        no_tool_improvement_score=no_tool.mean_maturation_score,
        no_social_learning_score=no_social.mean_maturation_score,
        no_environmental_sensing_score=no_sensing.mean_maturation_score,
        reactive_loss=reactive_loss,
        teaching_loss=teaching_loss,
        risk_memory_loss=risk_loss,
        infrastructure_loss=infra_loss,
        tool_loss=tool_loss,
        social_learning_loss=social_loss,
        environmental_sensing_loss=sensing_loss,
        shock_gate_pass_rate=full.shock_gate_pass_rate,
        post_gate_shock_rate=full.post_gate_shock_rate,
        survival_at_12h=full.mean_alive_at_12h,
        supports_12h_development_window=supports_window,
        supports_multiday_maturation=supports_maturation,
        supports_ablation_specificity=supports_ablation,
        verdict="pass" if supports_window and supports_maturation and supports_ablation else "partial_or_failed",
    )


def asdict_rows(rows: Sequence[object]) -> list[dict[str, object]]:
    return [asdict(row) for row in rows]
