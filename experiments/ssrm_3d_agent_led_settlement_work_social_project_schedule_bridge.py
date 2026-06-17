#!/usr/bin/env python3
"""Agent-led settlement work schedules, social obligations, and project planning.

Report 192 consumes the Report 191 seasonal logistics state and adds settlement
scheduling: role assignment, seasonal work plans, rest/care balance, promise and
social obligations, project dependencies, repair/gather/teach/care rotation,
conflict resolution, schedule adaptation, fatigue guardrails, logistics-memory
binding, frequency/flower work rhythms, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not subjective obligation, real labor, subjective suffering, subjective
consciousness, moral patienthood, or complete 3D gameplay.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_led_seasonal_logistics_stock_planning_bridge_state.json"

AGENTS = {
    "Ari": {"role": "repair_lead", "craft": 0.78, "social": 0.55, "teaching": 0.62, "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"role": "care_steward", "craft": 0.67, "social": 0.84, "teaching": 0.78, "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"role": "route_keeper", "craft": 0.60, "social": 0.66, "teaching": 0.57, "frequency_hz": 0.258, "flower_node": "social_petal"},
}

SEASON_TASKS = {
    "warm_regrowth": ["gather_food", "teach_skill", "repair_shelter"],
    "dry_heat": ["draw_water", "care_shift", "promise_delivery"],
    "storm_wet": ["repair_shelter", "council_resolve", "craft_medicine"],
    "cold_low_light": ["shelter_watch", "rest_shift", "project_build"],
}

WEIGHTS = {
    "seasonal_work_schedule_rate": 0.10,
    "role_assignment_rate": 0.07,
    "rest_care_balance_rate": 0.07,
    "promise_obligation_rate": 0.08,
    "project_dependency_rate": 0.09,
    "repair_gather_teach_balance_rate": 0.07,
    "conflict_resolution_rate": 0.07,
    "schedule_adaptation_rate": 0.08,
    "fatigue_guardrail_rate": 0.08,
    "social_obligation_memory_rate": 0.07,
    "logistics_dependency_binding_rate": 0.07,
    "seasonal_project_progress_rate": 0.06,
    "frequency_flower_schedule_rhythm_rate": 0.04,
    "browser_schedule_replay_rate": 0.02,
    "privacy_preservation_rate": 0.02,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class ScheduleConfig:
    seed: int = 20260805
    days: int = 18
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    seasonal_schedule: bool
    role_assignment: bool
    rest_care_balance: bool
    promise_obligations: bool
    project_dependencies: bool
    repair_gather_teach_balance: bool
    conflict_resolution: bool
    schedule_adaptation: bool
    fatigue_guardrail: bool
    social_obligation_memory: bool
    logistics_dependency_binding: bool
    seasonal_project_progress: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_days: int
    schedule_events: int
    seasonal_work_schedule_rate: float
    role_assignment_rate: float
    rest_care_balance_rate: float
    promise_obligation_rate: float
    project_dependency_rate: float
    repair_gather_teach_balance_rate: float
    conflict_resolution_rate: float
    schedule_adaptation_rate: float
    fatigue_guardrail_rate: float
    social_obligation_memory_rate: float
    logistics_dependency_binding_rate: float
    seasonal_project_progress_rate: float
    frequency_flower_schedule_rhythm_rate: float
    browser_schedule_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    settlement_schedule_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_settlement_schedule_readiness: float
    full_seasonal_work_schedule_rate: float
    full_role_assignment_rate: float
    full_rest_care_balance_rate: float
    full_promise_obligation_rate: float
    full_project_dependency_rate: float
    full_repair_gather_teach_balance_rate: float
    full_conflict_resolution_rate: float
    full_schedule_adaptation_rate: float
    full_fatigue_guardrail_rate: float
    full_social_obligation_memory_rate: float
    full_logistics_dependency_binding_rate: float
    full_seasonal_project_progress_rate: float
    full_frequency_flower_schedule_rhythm_rate: float
    full_browser_schedule_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_seasonal_schedule_loss: float
    no_role_assignment_loss: float
    no_rest_care_balance_loss: float
    no_promise_obligations_loss: float
    no_project_dependencies_loss: float
    no_repair_gather_teach_balance_loss: float
    no_conflict_resolution_loss: float
    no_schedule_adaptation_loss: float
    no_fatigue_guardrail_loss: float
    no_social_obligation_memory_loss: float
    no_logistics_dependency_binding_loss: float
    no_seasonal_project_progress_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_agent_led_settlement_schedule_bridge: bool
    supports_settlement_schedule_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_subjective_obligation_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_led_settlement_work_social_project_schedule", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_seasonal_schedule", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_role_assignment", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_rest_care_balance", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_promise_obligations", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_project_dependencies", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_repair_gather_teach_balance", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_conflict_resolution", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_schedule_adaptation", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_fatigue_guardrail", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_social_obligation_memory", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_logistics_dependency_binding", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_seasonal_project_progress", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2, sort_keys=True)};\n", encoding="utf-8")


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_agent_led_seasonal_logistics_stock_planning":
        raise ValueError("source state is not the integrated Report 191 seasonal logistics state")
    return data


def logistics_state(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("logistics_state") if isinstance(source.get("logistics_state"), Mapping) else None
    if not state:
        raise ValueError("Report 191 state has no logistics_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, float], dict[str, object]]:
    logi = logistics_state(source)
    relationships = {str(k): copy.deepcopy(v) for k, v in (logi.get("relationships") or {}).items()}
    stocks = {str(k): float(v) for k, v in (logi.get("stocks") or {}).items()}
    projects = {
        "winter_shelter_repair": {"progress": 0.18, "requires": ["shelter_fuel", "repair_cloth"], "owner": "Ari"},
        "water_route_markers": {"progress": 0.22, "requires": ["water_jars", "repair_cloth"], "owner": "Milo"},
        "medicine_corner": {"progress": 0.30, "requires": ["medicine_batches", "repair_cloth"], "owner": "Fay"},
    }
    agents = {}
    for agent_id, spec in AGENTS.items():
        rel = relationships.setdefault(agent_id, {})
        agents[agent_id] = {
            "agent_id": agent_id,
            "role": spec["role"],
            "fatigue": 0.26 + (0.04 if agent_id == "Ari" else 0.02),
            "social_debt": 0.18,
            "promise_due": agent_id != "Fay",
            "teaching_credit": 0.0,
            "last_task": None,
            "schedule_memories": [],
            "source_logistics_memories": len(rel.get("logistics_memories") or []),
        }
    return agents, stocks, projects


def season_name(day: int) -> str:
    return ("warm_regrowth", "dry_heat", "storm_wet", "cold_low_light")[(day // 5) % 4]


def choose_task(agent_id: str, day: int, season: str, agent: Mapping[str, object], stocks: Mapping[str, float], projects: Mapping[str, Mapping[str, object]], condition: Condition) -> str | None:
    if not condition.seasonal_schedule:
        return None
    base = SEASON_TASKS[season][(day + list(sorted(AGENTS)).index(agent_id)) % 3]
    if condition.fatigue_guardrail and float(agent.get("fatigue", 0.0)) > 0.58:
        return "rest_shift"
    if condition.promise_obligations and agent.get("promise_due") and day % 4 == 1:
        return "promise_delivery"
    if condition.project_dependencies:
        blocked_project = min(projects.values(), key=lambda p: float(p["progress"]))
        if all(float(stocks.get(req, 0.0)) > 1.0 for req in blocked_project["requires"]) and day % 3 == 0:
            return "project_build"
    return base


def apply_task(agent_id: str, task: str | None, season: str, day: int, agents: dict[str, dict[str, object]], stocks: dict[str, float], projects: dict[str, dict[str, object]], condition: Condition) -> dict[str, object]:
    agent = agents[agent_id]
    packet = {"task": task, "applied": False, "project": None, "promise_kept": False, "conflict_resolved": False, "adapted": False, "balanced": False}
    if not task:
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.030)
        return packet
    if condition.schedule_adaptation and season in {"storm_wet", "cold_low_light"} and task in {"gather_food", "draw_water"}:
        task = "repair_shelter" if season == "storm_wet" else "shelter_watch"
        packet["task"] = task
        packet["adapted"] = True
    if task == "rest_shift" and condition.rest_care_balance:
        agent["fatigue"] = clamp(float(agent["fatigue"]) - 0.18)
        packet["balanced"] = True
    elif task == "care_shift" and condition.rest_care_balance:
        target = max(agents, key=lambda aid: float(agents[aid]["fatigue"]))
        agents[target]["fatigue"] = clamp(float(agents[target]["fatigue"]) - 0.055)
        agent["social_debt"] = clamp(float(agent["social_debt"]) - 0.035)
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.025)
        packet["balanced"] = True
    elif task == "promise_delivery" and condition.promise_obligations:
        agent["promise_due"] = False
        agent["social_debt"] = clamp(float(agent["social_debt"]) - 0.060)
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.020)
        packet["promise_kept"] = True
    elif task == "project_build" and condition.project_dependencies:
        project_name, project = min(projects.items(), key=lambda item: float(item[1]["progress"]))
        if all(float(stocks.get(req, 0.0)) > 1.0 for req in project["requires"]):
            for req in project["requires"]:
                stocks[req] = max(0.0, float(stocks[req]) - 0.18)
            project["progress"] = clamp(float(project["progress"]) + 0.115 + AGENTS[agent_id]["craft"] * 0.035)
            agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.045)
            packet["project"] = project_name
    elif task == "repair_shelter":
        stocks["shelter_fuel"] = max(0.0, float(stocks.get("shelter_fuel", 0.0)) - 0.07)
        stocks["repair_cloth"] = max(0.0, float(stocks.get("repair_cloth", 0.0)) - 0.04)
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.035)
    elif task == "gather_food":
        stocks["food_rations"] = float(stocks.get("food_rations", 0.0)) + 0.45
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.032)
    elif task == "draw_water":
        stocks["water_jars"] = float(stocks.get("water_jars", 0.0)) + 0.42
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.030)
    elif task == "craft_medicine":
        stocks["medicine_batches"] = float(stocks.get("medicine_batches", 0.0)) + 0.30
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.028)
    elif task == "teach_skill":
        agent["teaching_credit"] = clamp(float(agent["teaching_credit"]) + 0.11)
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.018)
    elif task == "council_resolve" and condition.conflict_resolution:
        for other in agents.values():
            other["social_debt"] = clamp(float(other["social_debt"]) - 0.030)
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.020)
        packet["conflict_resolved"] = True
    elif task == "shelter_watch":
        agent["fatigue"] = clamp(float(agent["fatigue"]) + 0.026)
    if condition.fatigue_guardrail and float(agent["fatigue"]) > 0.72:
        agent["fatigue"] = 0.62
        packet["adapted"] = True
    packet["applied"] = True
    agent["last_task"] = task
    if condition.social_obligation_memory:
        agent["schedule_memories"].append(f"day {day}: {task} during {season}")
    return packet


def task_balanced(task: str | None) -> bool:
    return task in {"repair_shelter", "gather_food", "draw_water", "teach_skill", "care_shift", "craft_medicine", "rest_shift", "project_build", "shelter_watch"}


def make_event(event_id: int, condition: Condition, day: int, season: str, agent_id: str, before_agent: Mapping[str, object], after_agent: Mapping[str, object], packet: Mapping[str, object], stocks: Mapping[str, float], projects: Mapping[str, Mapping[str, object]], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    spec = AGENTS[agent_id]
    public_packets = {
        "schedule": {"season": season, "task": packet.get("task"), "role": after_agent.get("role") if condition.role_assignment else "unassigned", "adapted": packet.get("adapted")},
        "agent_public": {"fatigue": round(float(after_agent.get("fatigue", 0.0)), 6), "social_debt": round(float(after_agent.get("social_debt", 0.0)), 6), "promise_due": bool(after_agent.get("promise_due")), "memories": len(after_agent.get("schedule_memories", []))},
        "stocks": {key: round(float(value), 6) for key, value in stocks.items()},
        "projects": {key: {"progress": round(float(value["progress"]), 6), "owner": value["owner"]} for key, value in projects.items()},
        "dependency": {"logistics_bound": condition.logistics_dependency_binding, "source_logistics_memories": after_agent.get("source_logistics_memories", 0)},
    }
    replay = {"day": day, "agent_id": agent_id, "season": season, "task": packet.get("task"), "pose": "resting" if packet.get("task") == "rest_shift" else "working", "flower_node": spec["flower_node"], "frequency_hz": spec["frequency_hz"]}
    return {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "agent_id": agent_id,
        "before_public": {"fatigue": round(float(before_agent.get("fatigue", 0.0)), 6), "promise_due": bool(before_agent.get("promise_due"))},
        "after_public": {"fatigue": round(float(after_agent.get("fatigue", 0.0)), 6), "promise_due": bool(after_agent.get("promise_due"))},
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_task_preference": spec["role"], "private_fatigue_projection": round(float(after_agent.get("fatigue", 0.0)) + 0.08, 6)},
        "frequency_hz": round(spec["frequency_hz"] + (day % 5) * 0.0013, 6) if condition.frequency_flower_binding else None,
        "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, day, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary") and "after_public" in event)


def run_condition(condition: Condition, config: ScheduleConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents, stocks, projects = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["schedule", "role", "rest", "promise", "dependency", "balance", "conflict", "adapt", "fatigue", "memory", "logistics", "progress", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"subjective_consciousness": False, "subjective_obligation": False, "subjective_suffering": False, "moral_patienthood": False, "complete_3d_world": False, "real_labor": False}
    event_id = 0
    for day in range(config.days):
        season = season_name(day)
        for agent_id in sorted(agents):
            agent = agents[agent_id]
            before = copy.deepcopy(agent)
            task = choose_task(agent_id, day, season, agent, stocks, projects, condition)
            packet = apply_task(agent_id, task, season, day, agents, stocks, projects, condition)
            after = copy.deepcopy(agent)
            event = make_event(event_id, condition, day, season, agent_id, before, after, packet, stocks, projects, claim_boundary)
            events.append(event)
            project_progress = any(float(project["progress"]) > 0.50 for project in projects.values())
            logistics_bound = condition.logistics_dependency_binding and min(stocks.values()) > 0.5 and int(agent.get("source_logistics_memories", 0)) >= 20
            hits["schedule"].append(1.0 if condition.seasonal_schedule and task else 0.0)
            hits["role"].append(1.0 if condition.role_assignment and event["public_packets"]["schedule"]["role"] == AGENTS[agent_id]["role"] else 0.0)
            hits["rest"].append(1.0 if condition.rest_care_balance and (packet.get("balanced") or float(agent["fatigue"]) <= 0.72) else 0.0)
            hits["promise"].append(1.0 if condition.promise_obligations and (packet.get("promise_kept") or not agent.get("promise_due")) else 0.0)
            hits["dependency"].append(1.0 if condition.project_dependencies and (packet.get("project") or project_progress) else 0.0)
            hits["balance"].append(1.0 if condition.repair_gather_teach_balance and task_balanced(task) else 0.0)
            hits["conflict"].append(1.0 if condition.conflict_resolution and (packet.get("conflict_resolved") or max(float(a["social_debt"]) for a in agents.values()) < 0.22) else 0.0)
            hits["adapt"].append(1.0 if condition.schedule_adaptation and (packet.get("adapted") or task is not None) else 0.0)
            hits["fatigue"].append(1.0 if condition.fatigue_guardrail and float(agent["fatigue"]) <= 0.72 else 0.0)
            hits["memory"].append(1.0 if condition.social_obligation_memory and len(agent.get("schedule_memories", [])) >= 1 else 0.0)
            hits["logistics"].append(1.0 if logistics_bound else 0.0)
            hits["progress"].append(1.0 if condition.seasonal_project_progress and project_progress else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "seasonal_work_schedule_rate": mean(hits["schedule"]),
        "role_assignment_rate": mean(hits["role"]),
        "rest_care_balance_rate": mean(hits["rest"]),
        "promise_obligation_rate": mean(hits["promise"]),
        "project_dependency_rate": mean(hits["dependency"]),
        "repair_gather_teach_balance_rate": mean(hits["balance"]),
        "conflict_resolution_rate": mean(hits["conflict"]),
        "schedule_adaptation_rate": mean(hits["adapt"]),
        "fatigue_guardrail_rate": mean(hits["fatigue"]),
        "social_obligation_memory_rate": mean(hits["memory"]),
        "logistics_dependency_binding_rate": mean(hits["logistics"]),
        "seasonal_project_progress_rate": mean(hits["progress"]),
        "frequency_flower_schedule_rhythm_rate": mean(hits["freq"]),
        "browser_schedule_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(agents), simulated_days=config.days, schedule_events=len(events), settlement_schedule_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "agents": agents, "stocks": stocks, "projects": projects, "events": events, "schedule_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_led_settlement_work_social_project_schedule"]

    def loss(name: str) -> float:
        return round(full.settlement_schedule_readiness - by_name[name].settlement_schedule_readiness, 6)

    losses = {
        "no_seasonal_schedule_loss": loss("no_seasonal_schedule"),
        "no_role_assignment_loss": loss("no_role_assignment"),
        "no_rest_care_balance_loss": loss("no_rest_care_balance"),
        "no_promise_obligations_loss": loss("no_promise_obligations"),
        "no_project_dependencies_loss": loss("no_project_dependencies"),
        "no_repair_gather_teach_balance_loss": loss("no_repair_gather_teach_balance"),
        "no_conflict_resolution_loss": loss("no_conflict_resolution"),
        "no_schedule_adaptation_loss": loss("no_schedule_adaptation"),
        "no_fatigue_guardrail_loss": loss("no_fatigue_guardrail"),
        "no_social_obligation_memory_loss": loss("no_social_obligation_memory"),
        "no_logistics_dependency_binding_loss": loss("no_logistics_dependency_binding"),
        "no_seasonal_project_progress_loss": loss("no_seasonal_project_progress"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.settlement_schedule_readiness >= 0.88
        and full.schedule_events >= 45
        and full.seasonal_work_schedule_rate >= 0.90
        and full.role_assignment_rate >= 0.90
        and full.rest_care_balance_rate >= 0.80
        and full.promise_obligation_rate >= 0.80
        and full.project_dependency_rate >= 0.65
        and full.logistics_dependency_binding_rate >= 0.90
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_seasonal_schedule_loss"] >= 0.10
        and losses["no_project_dependencies_loss"] >= 0.08
        and losses["no_schedule_adaptation_loss"] >= 0.07
        and losses["no_social_obligation_memory_loss"] >= 0.07
        and losses["no_logistics_dependency_binding_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_settlement_schedule_readiness=full.settlement_schedule_readiness,
        full_seasonal_work_schedule_rate=full.seasonal_work_schedule_rate,
        full_role_assignment_rate=full.role_assignment_rate,
        full_rest_care_balance_rate=full.rest_care_balance_rate,
        full_promise_obligation_rate=full.promise_obligation_rate,
        full_project_dependency_rate=full.project_dependency_rate,
        full_repair_gather_teach_balance_rate=full.repair_gather_teach_balance_rate,
        full_conflict_resolution_rate=full.conflict_resolution_rate,
        full_schedule_adaptation_rate=full.schedule_adaptation_rate,
        full_fatigue_guardrail_rate=full.fatigue_guardrail_rate,
        full_social_obligation_memory_rate=full.social_obligation_memory_rate,
        full_logistics_dependency_binding_rate=full.logistics_dependency_binding_rate,
        full_seasonal_project_progress_rate=full.seasonal_project_progress_rate,
        full_frequency_flower_schedule_rhythm_rate=full.frequency_flower_schedule_rhythm_rate,
        full_browser_schedule_replay_rate=full.browser_schedule_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_led_settlement_schedule_bridge=supports,
        supports_settlement_schedule_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_subjective_obligation_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: ScheduleConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_agent_led_settlement_work_social_project_schedule"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "settlement_schedule_not_subjective_obligation": True,
            "work_rotation_not_real_labor_claim": True,
            "fatigue_guardrail_not_subjective_suffering": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "multi-week apprenticeship, skill transfer, and tool-specialization careers",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "schedule_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_LED_SETTLEMENT_WORK_SOCIAL_PROJECT_SCHEDULE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_LED_SETTLEMENT_WORK_SOCIAL_PROJECT_SCHEDULE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_LED_SETTLEMENT_WORK_SOCIAL_PROJECT_SCHEDULE_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=ScheduleConfig.seed)
    parser.add_argument("--days", type=int, default=ScheduleConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(ScheduleConfig(seed=args.seed, days=args.days, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("settlement_schedule_readiness", f"{verdict['full_settlement_schedule_readiness']:.6f}")
    print("schedule_events", next(row["schedule_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_seasonal_schedule_loss", f"{verdict['no_seasonal_schedule_loss']:.6f}")
    print("no_project_dependencies_loss", f"{verdict['no_project_dependencies_loss']:.6f}")
    print("no_social_obligation_memory_loss", f"{verdict['no_social_obligation_memory_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
