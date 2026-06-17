#!/usr/bin/env python3
"""Pre-avatar deep time civilization simulator bridge.

Report 201 consumes the Report 200 generational language state and simulates a
long pre-avatar cultural period: institutions, languages, dialects, rituals,
tools, settlement memory, weather/resource pressure, apprenticeship, dispute
norm carryover, oral history, avatar-entry locking, frequency/flower rhythms,
and browser replay.

This is deterministic deep-time artificial-life substrate. It is not real
civilization, real language understanding, subjective consciousness, moral
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
PREFIX = "ssrm_3d_pre_avatar_deep_time_civilization_simulator_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_multigenerational_language_drift_dialect_oral_history_conversation_bridge_state.json"

WEATHER_CYCLE = ["wet_spring", "dry_heat", "cold_rain", "wind_harvest", "long_frost", "clear_repair"]
RESOURCE_PRESSURE = ["water", "warmth", "toolstone", "fiber", "food", "shelter"]
INSTITUTION_FORMS = ["memory_council", "tool_guild", "care_circle", "route_court", "ritual_calendar", "settlement_assembly"]
TOOL_FORMS = ["rain_cistern", "heat_screen", "stone_gauge", "fiber_loom", "grain_cache", "wind_roof"]
RITUAL_FORMS = ["first_rain_naming", "tool_return_vow", "winter_hearth_count", "route_opening_song", "repair_before_blame", "quiet_rest_lantern"]
SETTLEMENT_FORMS = ["west_bench_cluster", "root_rest_hollow", "north_route_ring"]

WEIGHTS = {
    "epoch_progression_rate": 0.07,
    "institution_continuity_rate": 0.08,
    "language_dialect_continuity_rate": 0.07,
    "ritual_calendar_rate": 0.06,
    "tool_innovation_rate": 0.08,
    "settlement_memory_rate": 0.08,
    "resource_weather_adaptation_rate": 0.07,
    "apprenticeship_transmission_rate": 0.06,
    "dispute_norm_carryover_rate": 0.06,
    "oral_history_integration_rate": 0.06,
    "avatar_entry_readiness_gate_rate": 0.08,
    "private_workspace_privacy_rate": 0.07,
    "frequency_flower_world_rhythm_rate": 0.05,
    "browser_deep_time_replay_rate": 0.04,
    "trace_integrity": 0.07,
}


@dataclass(frozen=True)
class DeepTimeConfig:
    seed: int = 20260814
    epochs: int = 18
    years_per_epoch: int = 192
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    epoch_progression: bool
    institution_evolution: bool
    language_dialect_binding: bool
    ritual_calendar: bool
    tool_innovation: bool
    settlement_memory: bool
    resource_weather_pressure: bool
    apprenticeship_transmission: bool
    dispute_norm_carryover: bool
    oral_history: bool
    avatar_entry_gate: bool
    privacy_filter: bool
    frequency_flower_binding: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    lineage_count: int
    deep_time_epochs: int
    simulated_years: int
    deep_time_events: int
    epoch_progression_rate: float
    institution_continuity_rate: float
    language_dialect_continuity_rate: float
    ritual_calendar_rate: float
    tool_innovation_rate: float
    settlement_memory_rate: float
    resource_weather_adaptation_rate: float
    apprenticeship_transmission_rate: float
    dispute_norm_carryover_rate: float
    oral_history_integration_rate: float
    avatar_entry_readiness_gate_rate: float
    private_workspace_privacy_rate: float
    frequency_flower_world_rhythm_rate: float
    browser_deep_time_replay_rate: float
    trace_integrity: float
    deep_time_civilization_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_deep_time_civilization_readiness: float
    full_epoch_progression_rate: float
    full_institution_continuity_rate: float
    full_language_dialect_continuity_rate: float
    full_ritual_calendar_rate: float
    full_tool_innovation_rate: float
    full_settlement_memory_rate: float
    full_resource_weather_adaptation_rate: float
    full_apprenticeship_transmission_rate: float
    full_dispute_norm_carryover_rate: float
    full_oral_history_integration_rate: float
    full_avatar_entry_readiness_gate_rate: float
    full_private_workspace_privacy_rate: float
    full_frequency_flower_world_rhythm_rate: float
    full_browser_deep_time_replay_rate: float
    full_trace_integrity: float
    no_epoch_progression_loss: float
    no_institution_evolution_loss: float
    no_language_dialect_binding_loss: float
    no_ritual_calendar_loss: float
    no_tool_innovation_loss: float
    no_settlement_memory_loss: float
    no_resource_weather_pressure_loss: float
    no_apprenticeship_transmission_loss: float
    no_dispute_norm_carryover_loss: float
    no_oral_history_loss: float
    no_avatar_entry_gate_loss: float
    no_privacy_filter_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    supports_pre_avatar_deep_time_civilization_bridge: bool
    supports_avatar_entry_after_deep_time_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_civilization_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_pre_avatar_deep_time_civilization", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_epoch_progression", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_institution_evolution", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_language_dialect_binding", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_ritual_calendar", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_tool_innovation", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_settlement_memory", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_resource_weather_pressure", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_apprenticeship_transmission", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_dispute_norm_carryover", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_oral_history", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_avatar_entry_gate", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
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


def load_source(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("condition") != "integrated_multigenerational_language_drift_dialect_oral_history_conversation":
        raise ValueError("source state is not the integrated Report 200 generational language state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, str], list[dict[str, object]], dict[str, object]]:
    generation_state = source.get("generational_language_state") if isinstance(source.get("generational_language_state"), Mapping) else None
    if not generation_state:
        raise ValueError("Report 200 state has no generational_language_state")
    lineages = {str(k): copy.deepcopy(v) for k, v in (generation_state.get("lineages") or {}).items()}
    source_lexicon = {str(k): str(v) for k, v in (generation_state.get("source_lexicon") or {}).items()}
    source_events = copy.deepcopy(generation_state.get("events") or [])
    world = {
        "institutions": {lineage: [] for lineage in lineages},
        "settlements": {lineage: [] for lineage in lineages},
        "tools": {lineage: [] for lineage in lineages},
        "rituals": {lineage: [] for lineage in lineages},
        "apprenticeships": {lineage: [] for lineage in lineages},
        "dispute_norms": {lineage: [] for lineage in lineages},
        "oral_histories": {lineage: [] for lineage in lineages},
    }
    return lineages, source_lexicon, source_events, world


def latest_source_event(source_events: Sequence[Mapping[str, object]], lineage: str, epoch: int) -> Mapping[str, object]:
    lineage_events = [event for event in source_events if event.get("lineage") == lineage]
    if not lineage_events:
        return {}
    return lineage_events[epoch % len(lineage_events)]


def apply_deep_time_event(lineage: str, epoch: int, config: DeepTimeConfig, lineages: Mapping[str, Mapping[str, object]], source_lexicon: Mapping[str, str], source_events: Sequence[Mapping[str, object]], world: dict[str, object], condition: Condition) -> dict[str, object]:
    profile = lineages[lineage]
    year = (epoch + 1) * config.years_per_epoch if condition.epoch_progression else 0
    weather = WEATHER_CYCLE[(epoch + len(lineage)) % len(WEATHER_CYCLE)]
    pressure = RESOURCE_PRESSURE[(epoch + len(str(profile.get("identity", lineage)))) % len(RESOURCE_PRESSURE)]
    source_event = latest_source_event(source_events, lineage, epoch)
    base_action = str(source_event.get("action") or next(iter(source_lexicon), "ask_route_help"))
    inherited_word = str(source_event.get("inherited_word") or source_lexicon.get(base_action, "no-word"))
    institution = None
    if condition.institution_evolution:
        institution = {
            "epoch": epoch,
            "year": year,
            "name": f"{lineage}_{INSTITUTION_FORMS[epoch % len(INSTITUTION_FORMS)]}",
            "purpose": f"coordinate {base_action} during {weather}",
        }
        world["institutions"][lineage].append(institution)
    language_binding = {
        "dialect_id": source_event.get("dialect_id"),
        "inherited_word": inherited_word,
        "base_action": base_action,
        "intelligibility": source_event.get("intelligibility", 1.0),
    } if condition.language_dialect_binding and inherited_word != "no-word" else None
    ritual = None
    if condition.ritual_calendar:
        ritual = {
            "epoch": epoch,
            "name": RITUAL_FORMS[epoch % len(RITUAL_FORMS)],
            "spoken_word": inherited_word if language_binding else None,
            "weather": weather,
        }
        world["rituals"][lineage].append(ritual)
    tool = None
    if condition.tool_innovation:
        tool = {
            "epoch": epoch,
            "name": f"{TOOL_FORMS[epoch % len(TOOL_FORMS)]}_{lineage.lower()}",
            "solves": pressure,
            "requires_institution": bool(institution),
        }
        world["tools"][lineage].append(tool)
    settlement = None
    if condition.settlement_memory:
        settlement = {
            "epoch": epoch,
            "name": SETTLEMENT_FORMS[epoch % len(SETTLEMENT_FORMS)],
            "memory": f"{lineage} remembers {weather} and {pressure} through {inherited_word}",
            "institution_count": len(world["institutions"][lineage]),
            "tool_count": len(world["tools"][lineage]),
        }
        world["settlements"][lineage].append(settlement)
    adaptation = None
    if condition.resource_weather_pressure:
        adaptation = {
            "weather": weather,
            "pressure": pressure,
            "response": tool["name"] if tool else f"ration_{pressure}",
            "settlement_anchor": settlement["name"] if settlement else None,
        }
    apprenticeship = None
    if condition.apprenticeship_transmission:
        apprenticeship = {
            "elder": f"{lineage}-g{max(0, epoch - 1):02d}",
            "learner": f"{lineage}-g{epoch:02d}",
            "teaches": tool["name"] if tool else base_action,
            "word": inherited_word,
        }
        world["apprenticeships"][lineage].append(apprenticeship)
    dispute_norm = None
    if condition.dispute_norm_carryover:
        dispute_norm = {
            "norm": "repair_before_blame",
            "source_protocol": len(source_event.get("avatar_conversation_protocol") or []),
            "institution": institution["name"] if institution else None,
        }
        world["dispute_norms"][lineage].append(dispute_norm)
    oral_history = None
    if condition.oral_history:
        oral_history = {
            "epoch": epoch,
            "elder_line": source_event.get("ritual_recall") or f"{lineage} keeps {inherited_word}",
            "settlement": settlement["name"] if settlement else None,
            "ritual": ritual["name"] if ritual else None,
        }
        world["oral_histories"][lineage].append(oral_history)
    prerequisites = [
        bool(institution),
        bool(language_binding),
        bool(ritual),
        bool(tool),
        bool(settlement),
        bool(adaptation),
        bool(apprenticeship),
        bool(dispute_norm),
        bool(oral_history),
        condition.privacy_filter,
    ]
    avatar_entry_gate = None
    if condition.avatar_entry_gate:
        avatar_entry_gate = {
            "state": "eligible_after_deep_time" if epoch == config.epochs - 1 and all(prerequisites) else "locked_until_deep_time_complete",
            "requires_public_translation": True,
            "requires_visible_consent_gate": True,
            "requires_private_workspace_seal": True,
            "simulated_year": year,
        }
    expected_boundary = {
        "real_civilization": False,
        "real_language_understanding": False,
        "real_consent": False,
        "moral_patienthood": False,
        "subjective_consciousness": False,
        "complete_3d_world": False,
    }
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_civilization": True}
    frequency = None
    flower_path = None
    if condition.frequency_flower_binding:
        base_frequency = float(profile.get("base_frequency", 0.25))
        frequency = round(base_frequency + (epoch * 0.0043) + (len(world["institutions"][lineage]) * 0.0007), 6)
        flower_path = f"{profile.get('flower_node', 'unknown')}:{profile.get('identity', lineage)}:epoch_{epoch}"
    event = {
        "event_id": f"deep-time-{epoch}-{lineage}",
        "epoch": epoch,
        "simulated_year": year,
        "lineage": lineage,
        "weather": weather,
        "resource_pressure": pressure,
        "source_action": base_action,
        "inherited_word": inherited_word,
        "institution": institution,
        "language_binding": language_binding,
        "ritual": ritual,
        "tool": tool,
        "settlement": settlement,
        "adaptation": adaptation,
        "apprenticeship": apprenticeship,
        "dispute_norm": dispute_norm,
        "oral_history": oral_history,
        "avatar_entry_gate": avatar_entry_gate,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unpublished_stress": f"{lineage} privately worries about {pressure}", "private_dialect_note": inherited_word},
        "frequency_hz": frequency,
        "flower_path": flower_path,
        "replay_frame": {
            "epoch": epoch,
            "simulated_year": year,
            "lineage": lineage,
            "weather": weather,
            "pressure": pressure,
            "institution": institution["name"] if institution else None,
            "tool": tool["name"] if tool else None,
            "settlement": settlement["name"] if settlement else None,
            "avatar_gate": avatar_entry_gate["state"] if avatar_entry_gate else None,
            "frequency_hz": frequency,
            "flower_path": flower_path,
        } if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["simulated_year"], event["inherited_word"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("simulated_year"), event.get("inherited_word"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: DeepTimeConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    lineages, source_lexicon, source_events, world = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["epoch", "institution", "language", "ritual", "tool", "settlement", "adapt", "apprentice", "dispute", "oral", "gate", "privacy", "freq", "replay", "trace"]}
    expected_boundary = {"real_civilization": False, "real_language_understanding": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for epoch in range(config.epochs):
        for lineage in sorted(lineages):
            event = apply_deep_time_event(lineage, epoch, config, lineages, source_lexicon, source_events, world, condition)
            events.append(event)
            hits["epoch"].append(1.0 if condition.epoch_progression and event["simulated_year"] > 0 else 0.0)
            hits["institution"].append(1.0 if condition.institution_evolution and event["institution"] and len(world["institutions"][lineage]) >= 1 else 0.0)
            hits["language"].append(1.0 if condition.language_dialect_binding and event["language_binding"] else 0.0)
            hits["ritual"].append(1.0 if condition.ritual_calendar and event["ritual"] else 0.0)
            hits["tool"].append(1.0 if condition.tool_innovation and event["tool"] else 0.0)
            hits["settlement"].append(1.0 if condition.settlement_memory and event["settlement"] else 0.0)
            hits["adapt"].append(1.0 if condition.resource_weather_pressure and event["adaptation"] else 0.0)
            hits["apprentice"].append(1.0 if condition.apprenticeship_transmission and event["apprenticeship"] else 0.0)
            hits["dispute"].append(1.0 if condition.dispute_norm_carryover and event["dispute_norm"] else 0.0)
            hits["oral"].append(1.0 if condition.oral_history and event["oral_history"] else 0.0)
            hits["gate"].append(1.0 if condition.avatar_entry_gate and event["avatar_entry_gate"] and event["avatar_entry_gate"]["requires_private_workspace_seal"] else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_path"] else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "epoch_progression_rate": mean(hits["epoch"]),
        "institution_continuity_rate": mean(hits["institution"]),
        "language_dialect_continuity_rate": mean(hits["language"]),
        "ritual_calendar_rate": mean(hits["ritual"]),
        "tool_innovation_rate": mean(hits["tool"]),
        "settlement_memory_rate": mean(hits["settlement"]),
        "resource_weather_adaptation_rate": mean(hits["adapt"]),
        "apprenticeship_transmission_rate": mean(hits["apprentice"]),
        "dispute_norm_carryover_rate": mean(hits["dispute"]),
        "oral_history_integration_rate": mean(hits["oral"]),
        "avatar_entry_readiness_gate_rate": mean(hits["gate"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "frequency_flower_world_rhythm_rate": mean(hits["freq"]),
        "browser_deep_time_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, lineage_count=len(lineages), deep_time_epochs=config.epochs, simulated_years=config.epochs * config.years_per_epoch, deep_time_events=len(events), deep_time_civilization_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "lineages": lineages, "source_lexicon": source_lexicon, "world": world, "events": events, "deep_time_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_pre_avatar_deep_time_civilization"]

    def loss(name: str) -> float:
        return round(full.deep_time_civilization_readiness - by_name[name].deep_time_civilization_readiness, 6)

    losses = {
        "no_epoch_progression_loss": loss("no_epoch_progression"),
        "no_institution_evolution_loss": loss("no_institution_evolution"),
        "no_language_dialect_binding_loss": loss("no_language_dialect_binding"),
        "no_ritual_calendar_loss": loss("no_ritual_calendar"),
        "no_tool_innovation_loss": loss("no_tool_innovation"),
        "no_settlement_memory_loss": loss("no_settlement_memory"),
        "no_resource_weather_pressure_loss": loss("no_resource_weather_pressure"),
        "no_apprenticeship_transmission_loss": loss("no_apprenticeship_transmission"),
        "no_dispute_norm_carryover_loss": loss("no_dispute_norm_carryover"),
        "no_oral_history_loss": loss("no_oral_history"),
        "no_avatar_entry_gate_loss": loss("no_avatar_entry_gate"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.deep_time_civilization_readiness >= 0.92
        and full.simulated_years >= 3000
        and full.deep_time_events >= 54
        and full.epoch_progression_rate == 1.0
        and full.institution_continuity_rate == 1.0
        and full.language_dialect_continuity_rate == 1.0
        and full.ritual_calendar_rate == 1.0
        and full.tool_innovation_rate == 1.0
        and full.settlement_memory_rate == 1.0
        and full.avatar_entry_readiness_gate_rate == 1.0
        and full.private_workspace_privacy_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_epoch_progression_loss"] >= 0.07
        and losses["no_institution_evolution_loss"] >= 0.08
        and losses["no_language_dialect_binding_loss"] >= 0.07
        and losses["no_tool_innovation_loss"] >= 0.08
        and losses["no_settlement_memory_loss"] >= 0.08
        and losses["no_avatar_entry_gate_loss"] >= 0.08
        and losses["no_privacy_filter_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_deep_time_civilization_readiness=full.deep_time_civilization_readiness,
        full_epoch_progression_rate=full.epoch_progression_rate,
        full_institution_continuity_rate=full.institution_continuity_rate,
        full_language_dialect_continuity_rate=full.language_dialect_continuity_rate,
        full_ritual_calendar_rate=full.ritual_calendar_rate,
        full_tool_innovation_rate=full.tool_innovation_rate,
        full_settlement_memory_rate=full.settlement_memory_rate,
        full_resource_weather_adaptation_rate=full.resource_weather_adaptation_rate,
        full_apprenticeship_transmission_rate=full.apprenticeship_transmission_rate,
        full_dispute_norm_carryover_rate=full.dispute_norm_carryover_rate,
        full_oral_history_integration_rate=full.oral_history_integration_rate,
        full_avatar_entry_readiness_gate_rate=full.avatar_entry_readiness_gate_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_frequency_flower_world_rhythm_rate=full.frequency_flower_world_rhythm_rate,
        full_browser_deep_time_replay_rate=full.browser_deep_time_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_pre_avatar_deep_time_civilization_bridge=supports,
        supports_avatar_entry_after_deep_time_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_civilization_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: DeepTimeConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_pre_avatar_deep_time_civilization"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "deep_time_simulation_not_real_civilization": True,
        "institution_state_not_real_society": True,
        "language_continuity_not_real_understanding": True,
        "avatar_entry_gate_not_real_consent": True,
        "no_subjective_consciousness_claim": True,
        "no_moral_patienthood_claim": True,
        "private_workspace_not_debug_leaked": True,
    }
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": moral_boundary,
        "next_gate": "pre-avatar playable world seed with spatial settlements, ecological cycles, embodied agents, and avatar spawn lock",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "deep_time_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PRE_AVATAR_DEEP_TIME_CIVILIZATION_SIMULATOR_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PRE_AVATAR_DEEP_TIME_CIVILIZATION_SIMULATOR_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PRE_AVATAR_DEEP_TIME_CIVILIZATION_SIMULATOR_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DeepTimeConfig.seed)
    parser.add_argument("--epochs", type=int, default=DeepTimeConfig.epochs)
    parser.add_argument("--years-per-epoch", type=int, default=DeepTimeConfig.years_per_epoch)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(DeepTimeConfig(seed=args.seed, epochs=args.epochs, years_per_epoch=args.years_per_epoch, source_state=args.source_state))
    verdict = results["verdict"]
    full = next(row for row in results["rows"] if row["condition"] == verdict["full_condition"])
    print("module_verdict", verdict["verdict"])
    print("deep_time_civilization_readiness", f"{verdict['full_deep_time_civilization_readiness']:.6f}")
    print("simulated_years", full["simulated_years"])
    print("deep_time_events", full["deep_time_events"])
    print("no_institution_evolution_loss", f"{verdict['no_institution_evolution_loss']:.6f}")
    print("no_avatar_entry_gate_loss", f"{verdict['no_avatar_entry_gate_loss']:.6f}")
    print("no_privacy_filter_loss", f"{verdict['no_privacy_filter_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
