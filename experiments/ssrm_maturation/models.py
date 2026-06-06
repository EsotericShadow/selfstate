"""Shared data types for the SSRM-3D multi-day maturation benchmark."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence


@dataclass(frozen=True)
class Config:
    seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    trace_seed: int = 20260901


@dataclass(frozen=True)
class Condition:
    name: str
    description: str
    teaching: bool = True
    risk_memory: bool = True
    infrastructure_memory: bool = True
    tool_improvement: bool = True
    social_learning: bool = True
    future_planning: bool = True
    reproduction: bool = True
    environmental_sensing: bool = True


CONDITIONS = (
    Condition("integrated_maturation", "full slow-development world with memory, teaching, tools, social learning, and planning"),
    Condition("reactive_survival_only", "reactive food/water/rest/treat policy without persistent development channels", teaching=False, risk_memory=False, infrastructure_memory=False, tool_improvement=False, social_learning=False, future_planning=False, reproduction=False, environmental_sensing=False),
    Condition("no_teaching_lineage", "teaching and lineage knowledge transmission removed", teaching=False),
    Condition("no_risk_memory", "risk memory and post-shock warning tradition removed", risk_memory=False),
    Condition("no_infrastructure_memory", "buildings decay but persistent architectural improvement is removed", infrastructure_memory=False),
    Condition("no_tool_improvement", "tool tier and repair-design improvement removed", tool_improvement=False),
    Condition("no_social_learning", "trust, symbols, and social repair do not accumulate into culture", social_learning=False),
    Condition("no_environmental_sensing", "weather, route, contamination, and migration sensing are degraded", environmental_sensing=False),
)


@dataclass
class Agent:
    ident: str
    generation: int
    age_hours: float
    max_life_hours: float
    resilience: float
    dexterity: float
    sociability: float
    curiosity: float
    health: float
    energy: float
    hunger: float
    thirst: float
    stress: float
    fear: float
    injury: float
    illness: float
    attachment: float
    wisdom: float
    build_skill: float
    tool_skill: float
    harvest_skill: float
    care_skill: float
    teach_skill: float
    scout_skill: float
    alive: bool = True
    child: bool = False
    action: str = "idle"


@dataclass
class World:
    time: float = 0.0
    food: float = 0.80
    water: float = 0.80
    materials: float = 0.54
    medicine: float = 0.36
    tools: float = 0.32
    shelter: float = 0.46
    architecture: float = 0.12
    workshop: float = 0.10
    waterworks: float = 0.14
    granary: float = 0.12
    paths: float = 0.10
    garden: float = 0.22
    sanitation: float = 0.12
    fire_control: float = 0.10
    social_trust: float = 0.48
    conflict: float = 0.10
    culture: float = 0.06
    symbols: float = 0.05
    risk_memory: float = 0.07
    map_knowledge: float = 0.10
    terrain_knowledge: float = 0.08
    soil: float = 0.62
    contamination: float = 0.14
    temperature: float = 0.55
    rainfall: float = 0.18
    wind: float = 0.16
    visibility: float = 0.78
    route_hazard: float = 0.16
    disease: float = 0.10
    predators: float = 0.12
    resource_migration: float = 0.12
    resource_depletion: float = 0.08
    weather: str = "clear"
    adaptive_pressure: float = 0.10
    pressure_integral: float = 0.0
    adaptation_evidence: float = 0.0
    major_shocks: int = 0
    next_shock: float = 12.5
    first_shock_hour: Optional[float] = None
    births: int = 0
    deaths: int = 0
    knowledge_transfer: float = 0.0
    architecture_tier: int = 0
    tool_tier: int = 0


@dataclass(frozen=True)
class EpisodeRow:
    seed: int
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_shock_before_12h: bool
    post_gate_shock: bool
    major_shocks: int
    first_shock_hour: float
    births: int
    deaths: int
    architecture_tier: int
    tool_tier: int
    architecture_delta: float
    tool_delta: float
    culture_delta: float
    risk_memory_delta: float
    knowledge_transfer: float
    adaptation_evidence: float
    pressure_integral: float
    development_at_12h: float
    knowledge_at_12h: float
    survival_score: float
    development_score: float
    knowledge_score: float
    recovery_score: float
    maturation_score: float


@dataclass(frozen=True)
class SummaryRow:
    condition: str
    mean_maturation_score: float
    mean_survival_score: float
    mean_development_score: float
    mean_knowledge_score: float
    mean_recovery_score: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_births: float
    mean_deaths: float
    mean_architecture_tier: float
    mean_tool_tier: float
    mean_architecture_delta: float
    mean_tool_delta: float
    mean_culture_delta: float
    mean_risk_memory_delta: float
    mean_knowledge_transfer: float
    mean_adaptation_evidence: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float


@dataclass(frozen=True)
class VerdictRow:
    integrated_score: float
    reactive_score: float
    no_teaching_score: float
    no_risk_memory_score: float
    no_infrastructure_memory_score: float
    no_tool_improvement_score: float
    no_social_learning_score: float
    no_environmental_sensing_score: float
    reactive_loss: float
    teaching_loss: float
    risk_memory_loss: float
    infrastructure_loss: float
    tool_loss: float
    social_learning_loss: float
    environmental_sensing_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    supports_12h_development_window: bool
    supports_multiday_maturation: bool
    supports_ablation_specificity: bool
    verdict: str


TraceFrame = Dict[str, object]


@dataclass
class Trace:
    seed: int
    condition: str
    frames: List[TraceFrame] = field(default_factory=list)
