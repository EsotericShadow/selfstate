#!/usr/bin/env python3
"""Multi-week apprenticeship, skill transfer, and tool-specialization careers.

Report 193 consumes the Report 192 settlement schedule state and adds persistent
career formation: mentor assignment, multi-week apprenticeship, deliberate
practice, skill transfer, tool specialization, career identity, teaching
lineage, craft-quality improvement, project-role fit, apprentice autonomy,
fatigue-balanced learning, schedule-memory binding, frequency/flower career
rhythms, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not subjective vocation, real labor, subjective consciousness, moral
patienthood, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_led_settlement_work_social_project_schedule_bridge_state.json"

AGENT_SPECS = {
    "Ari": {"role": "repair_lead", "primary_skill": "repair", "tool": "resonant_mallet", "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"role": "care_steward", "primary_skill": "care", "tool": "root_satchel", "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"role": "route_keeper", "primary_skill": "routing", "tool": "path_chisel", "frequency_hz": 0.258, "flower_node": "social_petal"},
}

MENTOR_RING = {
    "Ari": "Fay",
    "Fay": "Milo",
    "Milo": "Ari",
}

SKILL_ROTATION = ("repair", "care", "routing", "teaching", "medicine", "construction")

WEIGHTS = {
    "multi_week_apprenticeship_rate": 0.08,
    "mentor_assignment_rate": 0.08,
    "skill_practice_rate": 0.08,
    "skill_transfer_rate": 0.09,
    "tool_specialization_rate": 0.08,
    "career_identity_stability_rate": 0.09,
    "teaching_lineage_rate": 0.07,
    "craft_quality_improvement_rate": 0.08,
    "project_role_fit_rate": 0.07,
    "apprentice_autonomy_growth_rate": 0.06,
    "fatigue_learning_balance_rate": 0.06,
    "schedule_memory_binding_rate": 0.06,
    "frequency_flower_career_rhythm_rate": 0.04,
    "browser_career_replay_rate": 0.03,
    "privacy_preservation_rate": 0.02,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class CareerConfig:
    seed: int = 20260806
    weeks: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    apprenticeship: bool
    mentor_assignment: bool
    skill_practice: bool
    skill_transfer: bool
    tool_specialization: bool
    career_identity: bool
    teaching_lineage: bool
    craft_quality: bool
    project_role_fit: bool
    autonomy_growth: bool
    fatigue_learning_balance: bool
    schedule_memory_binding: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_weeks: int
    career_events: int
    multi_week_apprenticeship_rate: float
    mentor_assignment_rate: float
    skill_practice_rate: float
    skill_transfer_rate: float
    tool_specialization_rate: float
    career_identity_stability_rate: float
    teaching_lineage_rate: float
    craft_quality_improvement_rate: float
    project_role_fit_rate: float
    apprentice_autonomy_growth_rate: float
    fatigue_learning_balance_rate: float
    schedule_memory_binding_rate: float
    frequency_flower_career_rhythm_rate: float
    browser_career_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    apprenticeship_career_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_apprenticeship_career_readiness: float
    full_multi_week_apprenticeship_rate: float
    full_mentor_assignment_rate: float
    full_skill_practice_rate: float
    full_skill_transfer_rate: float
    full_tool_specialization_rate: float
    full_career_identity_stability_rate: float
    full_teaching_lineage_rate: float
    full_craft_quality_improvement_rate: float
    full_project_role_fit_rate: float
    full_apprentice_autonomy_growth_rate: float
    full_fatigue_learning_balance_rate: float
    full_schedule_memory_binding_rate: float
    full_frequency_flower_career_rhythm_rate: float
    full_browser_career_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_apprenticeship_loss: float
    no_mentor_assignment_loss: float
    no_skill_practice_loss: float
    no_skill_transfer_loss: float
    no_tool_specialization_loss: float
    no_career_identity_loss: float
    no_teaching_lineage_loss: float
    no_craft_quality_loss: float
    no_project_role_fit_loss: float
    no_autonomy_growth_loss: float
    no_fatigue_learning_balance_loss: float
    no_schedule_memory_binding_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_multi_week_apprenticeship_career_bridge: bool
    supports_tool_specialization_career_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_subjective_vocation_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_multi_week_apprenticeship_skill_transfer_tool_career", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_apprenticeship", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_mentor_assignment", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_skill_practice", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_skill_transfer", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_tool_specialization", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_career_identity", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_teaching_lineage", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_craft_quality", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_project_role_fit", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_autonomy_growth", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_fatigue_learning_balance", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_schedule_memory_binding", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
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
    if data.get("condition") != "integrated_agent_led_settlement_work_social_project_schedule":
        raise ValueError("source state is not the integrated Report 192 settlement schedule state")
    return data


def schedule_state(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("schedule_state") if isinstance(source.get("schedule_state"), Mapping) else None
    if not state:
        raise ValueError("Report 192 state has no schedule_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, object]]:
    schedule = schedule_state(source)
    source_agents = schedule.get("agents") or {}
    source_projects = schedule.get("projects") or {}
    careers: dict[str, dict[str, object]] = {}
    for agent_id, spec in AGENT_SPECS.items():
        src = copy.deepcopy(source_agents.get(agent_id, {}))
        base_primary = spec["primary_skill"]
        skills = {skill: 0.28 for skill in SKILL_ROTATION}
        skills[base_primary] = 0.58
        if base_primary == "repair":
            skills["construction"] = 0.46
        if base_primary == "care":
            skills["medicine"] = 0.48
            skills["teaching"] = 0.44
        if base_primary == "routing":
            skills["teaching"] = 0.38
        careers[agent_id] = {
            "agent_id": agent_id,
            "role": src.get("role", spec["role"]),
            "primary_skill": base_primary,
            "skills": skills,
            "tool": spec["tool"],
            "tool_affinity": 0.34,
            "career_identity": [f"I am learning the {spec['role']} path."],
            "teaching_lineage": [],
            "career_memories": [],
            "autonomy": 0.25,
            "fatigue": float(src.get("fatigue", 0.35)),
            "source_schedule_memories": len(src.get("schedule_memories") or []),
            "last_mentor": None,
            "last_skill": None,
        }
    projects = {str(k): copy.deepcopy(v) for k, v in source_projects.items()}
    tools = {spec["tool"]: {"quality": 0.42, "owner": aid, "lineage_marks": []} for aid, spec in AGENT_SPECS.items()}
    return careers, tools, projects


def target_skill(agent_id: str, week: int) -> str:
    spec = AGENT_SPECS[agent_id]
    if week % 3 == 0:
        return spec["primary_skill"]
    if week % 3 == 1:
        return {"Ari": "construction", "Fay": "medicine", "Milo": "teaching"}[agent_id]
    return {"Ari": "teaching", "Fay": "care", "Milo": "routing"}[agent_id]


def role_fits(agent_id: str, skill: str) -> bool:
    primary = AGENT_SPECS[agent_id]["primary_skill"]
    return skill == primary or skill in {
        "repair": {"construction", "teaching"},
        "care": {"medicine", "teaching"},
        "routing": {"teaching", "construction"},
    }[primary]


def apply_week(agent_id: str, week: int, careers: dict[str, dict[str, object]], tools: dict[str, dict[str, object]], projects: Mapping[str, object], condition: Condition) -> dict[str, object]:
    career = careers[agent_id]
    mentor_id = MENTOR_RING[agent_id] if condition.mentor_assignment else None
    mentor = careers.get(mentor_id) if mentor_id else None
    skill = target_skill(agent_id, week)
    before_skill = float(career["skills"].get(skill, 0.0))
    before_quality = float(tools[career["tool"]]["quality"])
    packet = {"mentor": mentor_id, "skill": skill, "practice_gain": 0.0, "transfer_gain": 0.0, "tool_gain": 0.0, "quality_gain": 0.0, "autonomy_gain": 0.0, "role_fit": role_fits(agent_id, skill)}
    if not condition.apprenticeship:
        career["fatigue"] = clamp(float(career["fatigue"]) + 0.025)
        return packet
    if condition.skill_practice:
        gain = 0.035 + (0.012 if packet["role_fit"] and condition.project_role_fit else 0.0)
        career["skills"][skill] = clamp(before_skill + gain)
        career["fatigue"] = clamp(float(career["fatigue"]) + 0.026)
        packet["practice_gain"] = round(gain, 6)
    if condition.skill_transfer and mentor:
        mentor_skill = float(mentor["skills"].get(skill, 0.0))
        transfer = max(0.018, (mentor_skill - before_skill) * 0.18) if condition.mentor_assignment else 0.0
        career["skills"][skill] = clamp(float(career["skills"].get(skill, 0.0)) + transfer)
        packet["transfer_gain"] = round(transfer, 6)
    if condition.tool_specialization:
        tool_gain = 0.030 + float(career["skills"].get(skill, 0.0)) * 0.010
        career["tool_affinity"] = clamp(float(career["tool_affinity"]) + tool_gain)
        tools[career["tool"]]["lineage_marks"].append(f"week {week}: {agent_id} practiced {skill}")
        packet["tool_gain"] = round(tool_gain, 6)
    if condition.craft_quality:
        quality_gain = (0.020 + float(career["tool_affinity"]) * 0.018) if condition.tool_specialization else 0.012
        tools[career["tool"]]["quality"] = clamp(before_quality + quality_gain)
        packet["quality_gain"] = round(quality_gain, 6)
    if condition.autonomy_growth and float(career["skills"].get(skill, 0.0)) >= 0.46:
        autonomy_gain = 0.030 + (0.015 if condition.career_identity else 0.0)
        career["autonomy"] = clamp(float(career["autonomy"]) + autonomy_gain)
        packet["autonomy_gain"] = round(autonomy_gain, 6)
    if condition.fatigue_learning_balance and float(career["fatigue"]) > 0.62:
        career["fatigue"] = 0.52
    if condition.career_identity:
        identity = f"I am becoming {career['role']} through {skill}."
        if identity not in career["career_identity"]:
            career["career_identity"].append(identity)
    if condition.teaching_lineage and mentor_id:
        lineage = f"{mentor_id}->{agent_id}:{skill}:week{week}"
        career["teaching_lineage"].append(lineage)
    if condition.schedule_memory_binding and int(career.get("source_schedule_memories", 0)) >= 18:
        career["career_memories"].append(f"week {week}: schedule memory guided {skill}")
    career["last_mentor"] = mentor_id
    career["last_skill"] = skill
    return packet


def make_event(event_id: int, condition: Condition, week: int, agent_id: str, before: Mapping[str, object], after: Mapping[str, object], packet: Mapping[str, object], tool: Mapping[str, object], projects: Mapping[str, object], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    spec = AGENT_SPECS[agent_id]
    public_packets = {
        "apprenticeship": {"week": week, "mentor": packet.get("mentor"), "skill": packet.get("skill"), "role_fit": packet.get("role_fit")},
        "skill": {"before": round(float(before["skills"].get(packet.get("skill"), 0.0)), 6), "after": round(float(after["skills"].get(packet.get("skill"), 0.0)), 6), "practice_gain": packet.get("practice_gain"), "transfer_gain": packet.get("transfer_gain")},
        "tool": {"name": after.get("tool"), "affinity": round(float(after.get("tool_affinity", 0.0)), 6), "quality": round(float(tool.get("quality", 0.0)), 6), "lineage_marks": len(tool.get("lineage_marks", []))},
        "career": {"role": after.get("role"), "identity_count": len(after.get("career_identity", [])), "autonomy": round(float(after.get("autonomy", 0.0)), 6), "fatigue": round(float(after.get("fatigue", 0.0)), 6)},
        "lineage": {"entries": len(after.get("teaching_lineage", [])), "career_memories": len(after.get("career_memories", [])), "source_schedule_memories": after.get("source_schedule_memories", 0)},
        "projects": {key: {"progress": value.get("progress"), "owner": value.get("owner")} for key, value in projects.items()},
    }
    replay = {"week": week, "agent_id": agent_id, "mentor": packet.get("mentor"), "skill": packet.get("skill"), "tool": after.get("tool"), "pose": "practicing with mentor" if packet.get("mentor") else "solo practice", "flower_node": spec["flower_node"], "frequency_hz": spec["frequency_hz"]}
    return {
        "event_id": event_id,
        "condition": condition.name,
        "week": week,
        "agent_id": agent_id,
        "before_public": {"fatigue": round(float(before.get("fatigue", 0.0)), 6), "autonomy": round(float(before.get("autonomy", 0.0)), 6)},
        "after_public": {"fatigue": round(float(after.get("fatigue", 0.0)), 6), "autonomy": round(float(after.get("autonomy", 0.0)), 6)},
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_mastery_worry": round(1.0 - max(after["skills"].values()), 6), "private_tool_attachment": after.get("tool")},
        "frequency_hz": round(spec["frequency_hz"] + week * 0.0012, 6) if condition.frequency_flower_binding else None,
        "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, week, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary") and "after_public" in event)


def run_condition(condition: Condition, config: CareerConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    careers, tools, projects = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["apprentice", "mentor", "practice", "transfer", "tool", "career", "lineage", "quality", "role_fit", "autonomy", "fatigue", "schedule", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"subjective_consciousness": False, "subjective_vocation": False, "subjective_obligation": False, "moral_patienthood": False, "complete_3d_world": False, "real_labor": False}
    event_id = 0
    for week in range(config.weeks):
        for agent_id in sorted(careers):
            before = copy.deepcopy(careers[agent_id])
            packet = apply_week(agent_id, week, careers, tools, projects, condition)
            after = copy.deepcopy(careers[agent_id])
            tool = copy.deepcopy(tools[after["tool"]])
            event = make_event(event_id, condition, week, agent_id, before, after, packet, tool, projects, claim_boundary)
            events.append(event)
            skill = packet.get("skill")
            skill_delta = float(after["skills"].get(skill, 0.0)) - float(before["skills"].get(skill, 0.0)) if skill else 0.0
            hits["apprentice"].append(1.0 if condition.apprenticeship and week >= 0 and skill else 0.0)
            hits["mentor"].append(1.0 if condition.mentor_assignment and packet.get("mentor") in careers else 0.0)
            hits["practice"].append(1.0 if condition.skill_practice and float(packet.get("practice_gain", 0.0)) > 0.0 else 0.0)
            hits["transfer"].append(1.0 if condition.skill_transfer and float(packet.get("transfer_gain", 0.0)) > 0.0 and skill_delta > 0.0 else 0.0)
            hits["tool"].append(1.0 if condition.tool_specialization and float(after.get("tool_affinity", 0.0)) > float(before.get("tool_affinity", 0.0)) else 0.0)
            hits["career"].append(1.0 if condition.career_identity and len(after.get("career_identity", [])) >= 2 else 0.0)
            hits["lineage"].append(1.0 if condition.teaching_lineage and len(after.get("teaching_lineage", [])) >= 1 else 0.0)
            hits["quality"].append(1.0 if condition.craft_quality and float(tool.get("quality", 0.0)) > 0.42 else 0.0)
            hits["role_fit"].append(1.0 if condition.project_role_fit and packet.get("role_fit") else 0.0)
            hits["autonomy"].append(1.0 if condition.autonomy_growth and float(after.get("autonomy", 0.0)) > float(before.get("autonomy", 0.0)) else 0.0)
            hits["fatigue"].append(1.0 if condition.fatigue_learning_balance and float(after.get("fatigue", 0.0)) <= 0.62 else 0.0)
            hits["schedule"].append(1.0 if condition.schedule_memory_binding and len(after.get("career_memories", [])) >= 1 and int(after.get("source_schedule_memories", 0)) >= 18 else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "multi_week_apprenticeship_rate": mean(hits["apprentice"]),
        "mentor_assignment_rate": mean(hits["mentor"]),
        "skill_practice_rate": mean(hits["practice"]),
        "skill_transfer_rate": mean(hits["transfer"]),
        "tool_specialization_rate": mean(hits["tool"]),
        "career_identity_stability_rate": mean(hits["career"]),
        "teaching_lineage_rate": mean(hits["lineage"]),
        "craft_quality_improvement_rate": mean(hits["quality"]),
        "project_role_fit_rate": mean(hits["role_fit"]),
        "apprentice_autonomy_growth_rate": mean(hits["autonomy"]),
        "fatigue_learning_balance_rate": mean(hits["fatigue"]),
        "schedule_memory_binding_rate": mean(hits["schedule"]),
        "frequency_flower_career_rhythm_rate": mean(hits["freq"]),
        "browser_career_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(careers), simulated_weeks=config.weeks, career_events=len(events), apprenticeship_career_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "careers": careers, "tools": tools, "projects": projects, "events": events, "career_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_multi_week_apprenticeship_skill_transfer_tool_career"]

    def loss(name: str) -> float:
        return round(full.apprenticeship_career_readiness - by_name[name].apprenticeship_career_readiness, 6)

    losses = {
        "no_apprenticeship_loss": loss("no_apprenticeship"),
        "no_mentor_assignment_loss": loss("no_mentor_assignment"),
        "no_skill_practice_loss": loss("no_skill_practice"),
        "no_skill_transfer_loss": loss("no_skill_transfer"),
        "no_tool_specialization_loss": loss("no_tool_specialization"),
        "no_career_identity_loss": loss("no_career_identity"),
        "no_teaching_lineage_loss": loss("no_teaching_lineage"),
        "no_craft_quality_loss": loss("no_craft_quality"),
        "no_project_role_fit_loss": loss("no_project_role_fit"),
        "no_autonomy_growth_loss": loss("no_autonomy_growth"),
        "no_fatigue_learning_balance_loss": loss("no_fatigue_learning_balance"),
        "no_schedule_memory_binding_loss": loss("no_schedule_memory_binding"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.apprenticeship_career_readiness >= 0.88
        and full.career_events >= 24
        and full.multi_week_apprenticeship_rate >= 0.90
        and full.mentor_assignment_rate >= 0.90
        and full.skill_practice_rate >= 0.90
        and full.skill_transfer_rate >= 0.80
        and full.tool_specialization_rate >= 0.90
        and full.career_identity_stability_rate >= 0.80
        and full.teaching_lineage_rate >= 0.80
        and full.schedule_memory_binding_rate >= 0.80
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_apprenticeship_loss"] >= 0.15
        and losses["no_skill_transfer_loss"] >= 0.08
        and losses["no_tool_specialization_loss"] >= 0.08
        and losses["no_career_identity_loss"] >= 0.08
        and losses["no_teaching_lineage_loss"] >= 0.06
        and losses["no_schedule_memory_binding_loss"] >= 0.05
    )
    return VerdictRow(
        full_condition=full.condition,
        full_apprenticeship_career_readiness=full.apprenticeship_career_readiness,
        full_multi_week_apprenticeship_rate=full.multi_week_apprenticeship_rate,
        full_mentor_assignment_rate=full.mentor_assignment_rate,
        full_skill_practice_rate=full.skill_practice_rate,
        full_skill_transfer_rate=full.skill_transfer_rate,
        full_tool_specialization_rate=full.tool_specialization_rate,
        full_career_identity_stability_rate=full.career_identity_stability_rate,
        full_teaching_lineage_rate=full.teaching_lineage_rate,
        full_craft_quality_improvement_rate=full.craft_quality_improvement_rate,
        full_project_role_fit_rate=full.project_role_fit_rate,
        full_apprentice_autonomy_growth_rate=full.apprentice_autonomy_growth_rate,
        full_fatigue_learning_balance_rate=full.fatigue_learning_balance_rate,
        full_schedule_memory_binding_rate=full.schedule_memory_binding_rate,
        full_frequency_flower_career_rhythm_rate=full.frequency_flower_career_rhythm_rate,
        full_browser_career_replay_rate=full.browser_career_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_multi_week_apprenticeship_career_bridge=supports,
        supports_tool_specialization_career_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_subjective_vocation_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: CareerConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_multi_week_apprenticeship_skill_transfer_tool_career"
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
            "career_identity_not_subjective_vocation": True,
            "apprenticeship_not_real_labor_claim": True,
            "tool_specialization_not_moral_status": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "guild memory, craft standards, certification, and intergenerational tool inheritance",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "career_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_MULTI_WEEK_APPRENTICESHIP_SKILL_TRANSFER_TOOL_CAREER_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_MULTI_WEEK_APPRENTICESHIP_SKILL_TRANSFER_TOOL_CAREER_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_MULTI_WEEK_APPRENTICESHIP_SKILL_TRANSFER_TOOL_CAREER_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=CareerConfig.seed)
    parser.add_argument("--weeks", type=int, default=CareerConfig.weeks)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(CareerConfig(seed=args.seed, weeks=args.weeks, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("apprenticeship_career_readiness", f"{verdict['full_apprenticeship_career_readiness']:.6f}")
    print("career_events", next(row["career_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_apprenticeship_loss", f"{verdict['no_apprenticeship_loss']:.6f}")
    print("no_skill_transfer_loss", f"{verdict['no_skill_transfer_loss']:.6f}")
    print("no_tool_specialization_loss", f"{verdict['no_tool_specialization_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
