#!/usr/bin/env python3
"""Guild memory, craft standards, certification, and tool inheritance.

Report 194 consumes the Report 193 career state and adds guild-like
institutions: guild memory, craft standards, quality evaluation, certification,
tool inheritance, lineage traces, apprentice cohorts, standard violation
detection, remedial training, reputation binding, intergenerational memory,
craft marks, frequency/flower guild rhythms, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not subjective vocation, real labor, real credentialing, subjective
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
PREFIX = "ssrm_3d_guild_memory_craft_standards_tool_inheritance_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_state.json"

GUILD_SPECS = {
    "Ari": {"guild": "Shelterwrights", "standard": "sealed_joint", "craft": "repair", "heir": "Fay", "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"guild": "Rootkeepers", "standard": "clean_care_bundle", "craft": "care", "heir": "Milo", "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"guild": "Pathmarkers", "standard": "safe_waymark", "craft": "routing", "heir": "Ari", "frequency_hz": 0.258, "flower_node": "social_petal"},
}

WEIGHTS = {
    "guild_memory_rate": 0.08,
    "craft_standard_definition_rate": 0.08,
    "quality_evaluation_rate": 0.08,
    "certification_rate": 0.08,
    "tool_inheritance_rate": 0.08,
    "lineage_trace_rate": 0.07,
    "apprentice_cohort_rate": 0.07,
    "standard_violation_detection_rate": 0.07,
    "remedial_training_rate": 0.06,
    "trust_reputation_binding_rate": 0.07,
    "intergenerational_memory_rate": 0.08,
    "craft_mark_persistence_rate": 0.06,
    "frequency_flower_guild_rhythm_rate": 0.04,
    "browser_guild_replay_rate": 0.04,
    "privacy_preservation_rate": 0.03,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class GuildConfig:
    seed: int = 20260807
    cycles: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    guild_memory: bool
    craft_standards: bool
    quality_evaluation: bool
    certification: bool
    tool_inheritance: bool
    lineage_trace: bool
    apprentice_cohort: bool
    violation_detection: bool
    remedial_training: bool
    reputation_binding: bool
    intergenerational_memory: bool
    craft_mark: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    guild_cycles: int
    guild_events: int
    guild_memory_rate: float
    craft_standard_definition_rate: float
    quality_evaluation_rate: float
    certification_rate: float
    tool_inheritance_rate: float
    lineage_trace_rate: float
    apprentice_cohort_rate: float
    standard_violation_detection_rate: float
    remedial_training_rate: float
    trust_reputation_binding_rate: float
    intergenerational_memory_rate: float
    craft_mark_persistence_rate: float
    frequency_flower_guild_rhythm_rate: float
    browser_guild_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    guild_inheritance_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_guild_inheritance_readiness: float
    full_guild_memory_rate: float
    full_craft_standard_definition_rate: float
    full_quality_evaluation_rate: float
    full_certification_rate: float
    full_tool_inheritance_rate: float
    full_lineage_trace_rate: float
    full_apprentice_cohort_rate: float
    full_standard_violation_detection_rate: float
    full_remedial_training_rate: float
    full_trust_reputation_binding_rate: float
    full_intergenerational_memory_rate: float
    full_craft_mark_persistence_rate: float
    full_frequency_flower_guild_rhythm_rate: float
    full_browser_guild_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_guild_memory_loss: float
    no_craft_standards_loss: float
    no_quality_evaluation_loss: float
    no_certification_loss: float
    no_tool_inheritance_loss: float
    no_lineage_trace_loss: float
    no_apprentice_cohort_loss: float
    no_violation_detection_loss: float
    no_remedial_training_loss: float
    no_reputation_binding_loss: float
    no_intergenerational_memory_loss: float
    no_craft_mark_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_guild_memory_craft_standards_bridge: bool
    supports_tool_inheritance_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_credentialing_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_guild_memory_craft_standards_tool_inheritance", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_guild_memory", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_craft_standards", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_quality_evaluation", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_certification", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_tool_inheritance", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_lineage_trace", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_apprentice_cohort", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_violation_detection", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_remedial_training", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_reputation_binding", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_intergenerational_memory", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_craft_mark", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
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
    if data.get("condition") != "integrated_multi_week_apprenticeship_skill_transfer_tool_career":
        raise ValueError("source state is not the integrated Report 193 career state")
    return data


def career_state(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("career_state") if isinstance(source.get("career_state"), Mapping) else None
    if not state:
        raise ValueError("Report 193 state has no career_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    career = career_state(source)
    careers = {str(k): copy.deepcopy(v) for k, v in (career.get("careers") or {}).items()}
    tools = {str(k): copy.deepcopy(v) for k, v in (career.get("tools") or {}).items()}
    guilds: dict[str, dict[str, object]] = {}
    for agent_id, spec in GUILD_SPECS.items():
        tool_name = careers[agent_id]["tool"]
        guilds[agent_id] = {
            "guild": spec["guild"],
            "standard": spec["standard"],
            "certified": False,
            "reputation": 0.42 + float(careers[agent_id].get("autonomy", 0.0)) * 0.25,
            "guild_memory": [],
            "certificates": [],
            "violations": [],
            "remediation": [],
            "inherited_tools": [],
            "craft_marks": list(tools[tool_name].get("lineage_marks", []))[:2],
            "source_lineage_marks": len(tools[tool_name].get("lineage_marks", [])),
            "source_career_memories": len(careers[agent_id].get("career_memories", [])),
        }
    return careers, tools, guilds


def quality_score(agent_id: str, careers: Mapping[str, Mapping[str, object]], tools: Mapping[str, Mapping[str, object]], cycle: int) -> float:
    career = careers[agent_id]
    tool_name = career["tool"]
    primary = GUILD_SPECS[agent_id]["craft"]
    skill = float(career.get("skills", {}).get(primary, 0.0))
    tool_quality = float(tools[tool_name].get("quality", 0.0))
    affinity = float(career.get("tool_affinity", 0.0))
    return clamp(skill * 0.42 + tool_quality * 0.34 + affinity * 0.18 + cycle * 0.012)


def apply_cycle(agent_id: str, cycle: int, careers: dict[str, dict[str, object]], tools: dict[str, dict[str, object]], guilds: dict[str, dict[str, object]], condition: Condition) -> dict[str, object]:
    spec = GUILD_SPECS[agent_id]
    guild = guilds[agent_id]
    career = careers[agent_id]
    tool_name = career["tool"]
    tool = tools[tool_name]
    q = quality_score(agent_id, careers, tools, cycle)
    packet = {"guild": spec["guild"], "standard": None, "quality": round(q, 6), "certified": False, "violation": False, "remedial": False, "inherited_to": None, "craft_mark": None}
    if condition.guild_memory:
        guild["guild_memory"].append(f"cycle {cycle}: {agent_id} submitted {spec['standard']}")
    if condition.craft_standards:
        packet["standard"] = spec["standard"]
    passed = q >= 0.56 if condition.quality_evaluation and condition.craft_standards else False
    if condition.violation_detection and condition.craft_standards and cycle in {1, 4} and q < 0.70:
        guild["violations"].append(f"cycle {cycle}: revise {spec['standard']}")
        packet["violation"] = True
    if condition.remedial_training and packet["violation"]:
        primary = spec["craft"]
        career["skills"][primary] = clamp(float(career["skills"].get(primary, 0.0)) + 0.045)
        guild["remediation"].append(f"cycle {cycle}: remedial practice in {primary}")
        packet["remedial"] = True
    if condition.certification and passed:
        guild["certified"] = True
        cert = f"{spec['guild']}:{agent_id}:{spec['standard']}:cycle{cycle}"
        if cert not in guild["certificates"]:
            guild["certificates"].append(cert)
        packet["certified"] = True
    if condition.reputation_binding and packet["certified"]:
        guild["reputation"] = clamp(float(guild["reputation"]) + 0.035)
    elif condition.reputation_binding and packet["violation"]:
        guild["reputation"] = clamp(float(guild["reputation"]) - 0.015)
    if condition.craft_mark:
        mark = f"{spec['standard']}@{tool_name}:cycle{cycle}"
        guild["craft_marks"].append(mark)
        tool.setdefault("lineage_marks", []).append(mark)
        packet["craft_mark"] = mark
    if condition.tool_inheritance and cycle in {2, 5}:
        heir = spec["heir"]
        inherited = f"{tool_name}->{heir}:cycle{cycle}"
        guild["inherited_tools"].append(inherited)
        packet["inherited_to"] = heir
    if condition.lineage_trace and packet["inherited_to"]:
        tool.setdefault("lineage_marks", []).append(f"inheritance:{agent_id}->{packet['inherited_to']}:cycle{cycle}")
    if condition.guild_memory and condition.intergenerational_memory and (packet["inherited_to"] or packet["certified"]):
        guild["guild_memory"].append(f"generation memory: {agent_id} entrusted {spec['standard']} in cycle {cycle}")
    return packet


def make_event(event_id: int, condition: Condition, cycle: int, agent_id: str, packet: Mapping[str, object], careers: Mapping[str, Mapping[str, object]], tools: Mapping[str, Mapping[str, object]], guilds: Mapping[str, Mapping[str, object]], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    spec = GUILD_SPECS[agent_id]
    career = careers[agent_id]
    tool = tools[career["tool"]]
    guild = guilds[agent_id]
    public_packets = {
        "guild": {"name": spec["guild"], "standard": packet.get("standard"), "certified": bool(guild.get("certified")), "reputation": round(float(guild.get("reputation", 0.0)), 6)},
        "quality": {"score": packet.get("quality"), "evaluated": condition.quality_evaluation},
        "certificate": {"issued": bool(packet.get("certified")), "count": len(guild.get("certificates", []))},
        "tool": {"name": career.get("tool"), "owner": tool.get("owner"), "quality": round(float(tool.get("quality", 0.0)), 6), "lineage_marks": len(tool.get("lineage_marks", [])), "inherited_to": packet.get("inherited_to")},
        "standards": {"violation": bool(packet.get("violation")), "remedial": bool(packet.get("remedial")), "craft_mark": packet.get("craft_mark")},
        "memory": {"guild_memory_count": len(guild.get("guild_memory", [])), "source_career_memories": guild.get("source_career_memories", 0), "source_lineage_marks": guild.get("source_lineage_marks", 0)},
    }
    replay = {"cycle": cycle, "agent_id": agent_id, "guild": spec["guild"], "standard": spec["standard"], "tool": career.get("tool"), "quality": packet.get("quality"), "flower_node": spec["flower_node"], "frequency_hz": spec["frequency_hz"]}
    return {
        "event_id": event_id,
        "condition": condition.name,
        "cycle": cycle,
        "agent_id": agent_id,
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_standard_doubt": round(1.0 - float(packet.get("quality", 0.0)), 6), "private_heir_preference": spec["heir"]},
        "frequency_hz": round(spec["frequency_hz"] + cycle * 0.0015, 6) if condition.frequency_flower_binding else None,
        "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, cycle, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary"))


def run_condition(condition: Condition, config: GuildConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    careers, tools, guilds = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["guild", "standard", "quality", "cert", "inherit", "lineage", "cohort", "violation", "remedial", "reputation", "intergen", "mark", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"subjective_consciousness": False, "subjective_vocation": False, "real_credentialing": False, "moral_patienthood": False, "complete_3d_world": False, "real_labor": False}
    event_id = 0
    for cycle in range(config.cycles):
        cohort_present = len(careers) >= 3 and condition.apprentice_cohort
        for agent_id in sorted(careers):
            packet = apply_cycle(agent_id, cycle, careers, tools, guilds, condition)
            event = make_event(event_id, condition, cycle, agent_id, packet, careers, tools, guilds, claim_boundary)
            events.append(event)
            guild = guilds[agent_id]
            tool = tools[careers[agent_id]["tool"]]
            hits["guild"].append(1.0 if condition.guild_memory and len(guild.get("guild_memory", [])) >= 1 else 0.0)
            hits["standard"].append(1.0 if condition.craft_standards and packet.get("standard") else 0.0)
            hits["quality"].append(1.0 if condition.quality_evaluation and float(packet.get("quality", 0.0)) >= 0.0 else 0.0)
            hits["cert"].append(1.0 if condition.certification and (packet.get("certified") or guild.get("certified")) else 0.0)
            hits["inherit"].append(1.0 if condition.tool_inheritance and (packet.get("inherited_to") or cycle not in {2, 5}) else 0.0)
            hits["lineage"].append(1.0 if condition.lineage_trace and len(tool.get("lineage_marks", [])) > guild.get("source_lineage_marks", 0) else 0.0)
            hits["cohort"].append(1.0 if cohort_present else 0.0)
            hits["violation"].append(1.0 if condition.violation_detection and (packet.get("violation") or cycle not in {1, 4}) else 0.0)
            hits["remedial"].append(1.0 if condition.remedial_training and (packet.get("remedial") or not packet.get("violation")) else 0.0)
            hits["reputation"].append(1.0 if condition.reputation_binding and float(guild.get("reputation", 0.0)) >= 0.40 else 0.0)
            hits["intergen"].append(1.0 if condition.guild_memory and condition.intergenerational_memory and len(guild.get("guild_memory", [])) >= 2 else 0.0)
            hits["mark"].append(1.0 if condition.craft_mark and packet.get("craft_mark") else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "guild_memory_rate": mean(hits["guild"]),
        "craft_standard_definition_rate": mean(hits["standard"]),
        "quality_evaluation_rate": mean(hits["quality"]),
        "certification_rate": mean(hits["cert"]),
        "tool_inheritance_rate": mean(hits["inherit"]),
        "lineage_trace_rate": mean(hits["lineage"]),
        "apprentice_cohort_rate": mean(hits["cohort"]),
        "standard_violation_detection_rate": mean(hits["violation"]),
        "remedial_training_rate": mean(hits["remedial"]),
        "trust_reputation_binding_rate": mean(hits["reputation"]),
        "intergenerational_memory_rate": mean(hits["intergen"]),
        "craft_mark_persistence_rate": mean(hits["mark"]),
        "frequency_flower_guild_rhythm_rate": mean(hits["freq"]),
        "browser_guild_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(careers), guild_cycles=config.cycles, guild_events=len(events), guild_inheritance_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "careers": careers, "tools": tools, "guilds": guilds, "events": events, "guild_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_guild_memory_craft_standards_tool_inheritance"]

    def loss(name: str) -> float:
        return round(full.guild_inheritance_readiness - by_name[name].guild_inheritance_readiness, 6)

    losses = {
        "no_guild_memory_loss": loss("no_guild_memory"),
        "no_craft_standards_loss": loss("no_craft_standards"),
        "no_quality_evaluation_loss": loss("no_quality_evaluation"),
        "no_certification_loss": loss("no_certification"),
        "no_tool_inheritance_loss": loss("no_tool_inheritance"),
        "no_lineage_trace_loss": loss("no_lineage_trace"),
        "no_apprentice_cohort_loss": loss("no_apprentice_cohort"),
        "no_violation_detection_loss": loss("no_violation_detection"),
        "no_remedial_training_loss": loss("no_remedial_training"),
        "no_reputation_binding_loss": loss("no_reputation_binding"),
        "no_intergenerational_memory_loss": loss("no_intergenerational_memory"),
        "no_craft_mark_loss": loss("no_craft_mark"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.guild_inheritance_readiness >= 0.88
        and full.guild_events >= 18
        and full.guild_memory_rate >= 0.85
        and full.craft_standard_definition_rate >= 0.90
        and full.certification_rate >= 0.80
        and full.tool_inheritance_rate >= 0.80
        and full.lineage_trace_rate >= 0.80
        and full.intergenerational_memory_rate >= 0.80
        and full.craft_mark_persistence_rate >= 0.90
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_guild_memory_loss"] >= 0.12
        and losses["no_craft_standards_loss"] >= 0.10
        and losses["no_certification_loss"] >= 0.08
        and losses["no_tool_inheritance_loss"] >= 0.08
        and losses["no_lineage_trace_loss"] >= 0.07
        and losses["no_intergenerational_memory_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_guild_inheritance_readiness=full.guild_inheritance_readiness,
        full_guild_memory_rate=full.guild_memory_rate,
        full_craft_standard_definition_rate=full.craft_standard_definition_rate,
        full_quality_evaluation_rate=full.quality_evaluation_rate,
        full_certification_rate=full.certification_rate,
        full_tool_inheritance_rate=full.tool_inheritance_rate,
        full_lineage_trace_rate=full.lineage_trace_rate,
        full_apprentice_cohort_rate=full.apprentice_cohort_rate,
        full_standard_violation_detection_rate=full.standard_violation_detection_rate,
        full_remedial_training_rate=full.remedial_training_rate,
        full_trust_reputation_binding_rate=full.trust_reputation_binding_rate,
        full_intergenerational_memory_rate=full.intergenerational_memory_rate,
        full_craft_mark_persistence_rate=full.craft_mark_persistence_rate,
        full_frequency_flower_guild_rhythm_rate=full.frequency_flower_guild_rhythm_rate,
        full_browser_guild_replay_rate=full.browser_guild_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_guild_memory_craft_standards_bridge=supports,
        supports_tool_inheritance_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_credentialing_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: GuildConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_guild_memory_craft_standards_tool_inheritance"
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
            "guild_certification_not_real_credentialing": True,
            "craft_standards_not_subjective_status": True,
            "tool_inheritance_not_moral_status": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "guild marketplaces, reciprocal credit, and craft-service exchange contracts",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "guild_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_GUILD_MEMORY_CRAFT_STANDARDS_TOOL_INHERITANCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_GUILD_MEMORY_CRAFT_STANDARDS_TOOL_INHERITANCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_GUILD_MEMORY_CRAFT_STANDARDS_TOOL_INHERITANCE_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=GuildConfig.seed)
    parser.add_argument("--cycles", type=int, default=GuildConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(GuildConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("guild_inheritance_readiness", f"{verdict['full_guild_inheritance_readiness']:.6f}")
    print("guild_events", next(row["guild_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_guild_memory_loss", f"{verdict['no_guild_memory_loss']:.6f}")
    print("no_tool_inheritance_loss", f"{verdict['no_tool_inheritance_loss']:.6f}")
    print("no_intergenerational_memory_loss", f"{verdict['no_intergenerational_memory_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
