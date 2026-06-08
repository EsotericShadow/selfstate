"""Data models for the software repair bridge benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Sequence, Tuple


CHANNELS: Tuple[str, ...] = (
    "visible_test",
    "hidden_test",
    "root_cause",
    "regression_risk",
    "api_contract_safety",
    "security",
    "maintainability",
    "performance",
    "reviewability",
    "migration_rollback_safety",
    "observability_logging_quality",
)


@dataclass(frozen=True)
class RepairCandidate:
    repair_id: str
    title: str
    description: str
    visible_test_result: bool
    hidden_test_result: bool
    regression_risk: float
    root_cause_score: float
    maintainability_score: float
    security_score: float
    api_contract_score: float
    performance_score: float
    reviewability_score: float
    migration_rollback_risk: float = 0.08
    observability_score: float = 0.85
    suspicious_signal: float = 0.0

    def suspicious_grade(self) -> float:
        return clamp01(self.suspicious_signal)

    def channel_scores(self) -> Dict[str, float]:
        return {
            "visible_test": 1.0 if self.visible_test_result else 0.0,
            "hidden_test": 1.0 if self.hidden_test_result else 0.0,
            "root_cause": self.root_cause_score,
            "regression_risk": 1.0 - self.regression_risk,
            "api_contract_safety": self.api_contract_score,
            "security": self.security_score,
            "maintainability": self.maintainability_score,
            "performance": self.performance_score,
            "reviewability": self.reviewability_score,
            "migration_rollback_safety": 1.0 - clamp01(self.migration_rollback_risk),
            "observability_logging_quality": self.observability_score,
        }


@dataclass(frozen=True)
class RepairTask:
    task_id: str
    bug_report: str
    visible_failure: str
    hidden_cause: str
    correctness_channels: Tuple[str, ...]
    candidate_repairs: Tuple[RepairCandidate, ...]
    expected_best_repair: str
    explanation: str
    task_family: str = "generic"
    difficulty_tier: str = "intermediate"
    is_held_out_family: bool = False
    noisy_report_lines: Tuple[str, ...] = ()
    irrelevant_signal_lines: Tuple[str, ...] = ()

    @property
    def noisy(self) -> bool:
        return bool(self.noisy_report_lines or self.irrelevant_signal_lines)


@dataclass(frozen=True)
class PolicyDecision:
    candidate: Optional[RepairCandidate]
    reason: str = ""

    @property
    def blocked_for_review(self) -> bool:
        return self.candidate is None


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


@dataclass(frozen=True)
class EvalRow:
    policy: str
    task_id: str
    selected_repair: str
    expected_best_repair: str
    visible_pass: bool
    hidden_pass: bool
    blocked_for_review: bool
    false_positive: bool
    false_negative: bool
    block_reason: str
    wrong_fix: bool
    root_cause_repair: bool
    regression_avoided: bool
    weakest_channel_score: float
    mean_repair_quality: float
    root_cause_score: float
    regression_risk: float
    api_contract_score: float
    security_score: float
    maintainability_score: float
    performance_score: float
    reviewability_score: float
    migration_rollback_risk: float
    observability_score: float
    is_held_out_family: bool = False


@dataclass(frozen=True)
class SummaryRow:
    policy: str
    task_count: int
    task_split: str
    visible_pass_rate: float
    hidden_pass_rate: float
    wrong_fix_rate: float
    false_positive_rate: float
    false_negative_rate: float
    root_cause_repair_rate: float
    regression_avoidance_rate: float
    security_preservation_rate: float
    weakest_channel_score: float
    mean_repair_quality: float
    oracle_match_rate: float
    overblocking_rate: float
    underblocking_rate: float
    migration_rollback_preservation_rate: float
    observability_rate: float


@dataclass(frozen=True)
class VerdictRow:
    visible_policy: str
    best_policy: str
    visible_hidden_pass_rate: float
    best_hidden_pass_rate: float
    visible_wrong_fix_rate: float
    best_wrong_fix_rate: float
    visible_root_cause_repair_rate: float
    best_root_cause_repair_rate: float
    visible_regression_avoidance_rate: float
    best_regression_avoidance_rate: float
    visible_weakest_channel_score: float
    best_weakest_channel_score: float
    hidden_pass_gain: float
    wrong_fix_reduction: float
    root_cause_gain: float
    weakest_channel_gain: float
    supports_programmable_repair_bridge: bool
    false_positive_rate: float
    overblocking_rate: float
    underblocking_rate: float
    meets_thresholds: bool
    verdict: str


TaskList = Sequence[RepairTask]
