"""Data models for the programmable repair bridge benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Sequence, Tuple


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


@dataclass(frozen=True)
class EvalRow:
    policy: str
    task_id: str
    selected_repair: str
    expected_best_repair: str
    visible_pass: bool
    hidden_pass: bool
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


@dataclass(frozen=True)
class SummaryRow:
    policy: str
    task_count: int
    visible_pass_rate: float
    hidden_pass_rate: float
    wrong_fix_rate: float
    root_cause_repair_rate: float
    regression_avoidance_rate: float
    weakest_channel_score: float
    oracle_match_rate: float
    mean_repair_quality: float


@dataclass(frozen=True)
class VerdictRow:
    visible_hidden_pass_rate: float
    min_channel_hidden_pass_rate: float
    visible_wrong_fix_rate: float
    min_channel_wrong_fix_rate: float
    visible_root_cause_repair_rate: float
    min_channel_root_cause_repair_rate: float
    visible_weakest_channel_score: float
    min_channel_weakest_channel_score: float
    hidden_pass_gain: float
    wrong_fix_reduction: float
    root_cause_gain: float
    weakest_channel_gain: float
    supports_programmable_repair_bridge: bool
    verdict: str


TaskList = Sequence[RepairTask]
