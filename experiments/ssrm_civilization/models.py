"""Data types for the SSRM-3D settlement pressure benchmark."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


Position = Tuple[float, float]


@dataclass(frozen=True)
class AgentProfile:
    name: str
    role: str
    base_skill: float
    social_need: float
    risk_tolerance: float
    home: Position


@dataclass
class AgentState:
    profile: AgentProfile
    health: float
    energy: float
    hunger: float
    thirst: float
    illness: float
    fear: float
    stress: float
    anger: float
    guilt: float
    attachment: float
    curiosity: float
    trust: Dict[str, float] = field(default_factory=dict)
    skill_memory: Dict[str, float] = field(default_factory=dict)
    alive: bool = True
    action: str = "idle"
    animation: str = "idle"
    x: float = 0.0
    z: float = 0.0


@dataclass
class ProjectState:
    shelter: float = 0.46
    water_purifier: float = 0.16
    clinic: float = 0.20
    farm: float = 0.18
    workshop: float = 0.12
    watchtower: float = 0.10
    school: float = 0.08
    commons: float = 0.18

    def as_dict(self) -> Dict[str, float]:
        return {
            "shelter": self.shelter,
            "water_purifier": self.water_purifier,
            "clinic": self.clinic,
            "farm": self.farm,
            "workshop": self.workshop,
            "watchtower": self.watchtower,
            "school": self.school,
            "commons": self.commons,
        }


@dataclass
class SettlementState:
    food: float = 0.48
    water: float = 0.42
    materials: float = 0.36
    medicine: float = 0.28
    tools: float = 0.34
    morale: float = 0.54
    trust_network: float = 0.50
    norm_standing: float = 0.46
    knowledge: float = 0.24
    map_coverage: float = 0.18
    sickness: float = 0.24
    conflict: float = 0.18
    threat: float = 0.20
    weather: str = "clear"
    weather_severity: float = 0.0
    projects: ProjectState = field(default_factory=ProjectState)


@dataclass(frozen=True)
class ScenarioSpec:
    name: str
    description: str
    storm_pressure: float
    scarcity_pressure: float
    illness_pressure: float
    social_pressure: float
    frontier_pressure: float
    threat_pressure: float


@dataclass(frozen=True)
class PolicyConfig:
    name: str
    social_memory: bool
    building_memory: bool
    role_memory: bool
    affect_control: bool
    norms: bool
    future_planning: bool
    teaching: bool
    trade: bool


@dataclass(frozen=True)
class CivilizationConfig:
    seed: int = 20260706
    ticks: int = 96
    eval_episodes: int = 48
    trace_episode: int = 3


@dataclass(frozen=True)
class EpisodeMetrics:
    scenario: str
    condition: str
    episode: int
    reward: float
    survival_fraction: float
    infrastructure_score: float
    cohesion_score: float
    resource_score: float
    knowledge_score: float
    civilization_score: float
    building_actions: int
    social_actions: int
    care_actions: int
    teaching_actions: int
    conflict_events: int
    migration_events: int
    casualties: int
    completed_projects: int
    refusals: int


@dataclass(frozen=True)
class SummaryRow:
    condition: str
    mean_reward: float
    mean_survival_fraction: float
    mean_infrastructure_score: float
    mean_cohesion_score: float
    mean_resource_score: float
    mean_knowledge_score: float
    mean_civilization_score: float
    mean_building_actions: float
    mean_social_actions: float
    mean_care_actions: float
    mean_teaching_actions: float
    mean_conflict_events: float
    mean_migration_events: float
    mean_casualties: float
    mean_completed_projects: float
    mean_refusals: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_civilization_score: float
    reactive_civilization_score: float
    no_social_memory_score: float
    no_building_memory_score: float
    no_role_memory_score: float
    no_affective_control_score: float
    no_norms_score: float
    no_future_planning_score: float
    reactive_loss: float
    social_memory_loss: float
    building_memory_loss: float
    role_memory_loss: float
    affective_control_loss: float
    norms_loss: float
    future_planning_loss: float
    supports_civilization_pressure_precursor: bool
    supports_closed_loop_rl: bool
    verdict: str


Frame = Dict[str, object]


@dataclass
class Trace:
    scenario: str
    condition: str
    frames: List[Frame] = field(default_factory=list)
