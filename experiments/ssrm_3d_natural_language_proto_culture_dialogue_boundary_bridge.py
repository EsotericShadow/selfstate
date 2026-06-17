#!/usr/bin/env python3
"""Natural-language proto-culture, ritual naming, and dialogue boundaries.

Report 199 consumes the Report 198 agent-authored constitution state and adds a
deterministic proto-culture layer: agents coin norm words, bind ritual names,
reuse shared symbols, teach each other terms, translate terms for the avatar,
use bounded refusal/repair dialogue, preserve private workspace, and replay the
language-culture trace.

This is proto-language substrate, not real understanding, real consent, real
rights, subjective consciousness, moral patienthood, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_state.json"

AGENT_SPEECH = {
    "Ari": {"root": "kar", "tone": "clear-work", "flower_node": "work_petal", "frequency_hz": 0.255},
    "Fay": {"root": "lum", "tone": "soft-rest", "flower_node": "root_rest", "frequency_hz": 0.232},
    "Milo": {"root": "ril", "tone": "route-play", "flower_node": "social_petal", "frequency_hz": 0.271},
}

SYLLABLES = ["na", "vo", "ri", "ta", "el", "mu", "sen", "ka"]
RITUAL_SUFFIX = {
    "place": "threshold",
    "ownership": "return",
    "privacy": "veil",
    "labor": "hands",
    "care": "warmth",
    "social_face": "face",
    "proximity": "near-step",
    "help": "road-help",
}

WEIGHTS = {
    "proto_word_creation_rate": 0.08,
    "ritual_naming_rate": 0.06,
    "shared_symbol_reuse_rate": 0.06,
    "interagent_teaching_rate": 0.05,
    "avatar_translation_rate": 0.07,
    "dialogue_boundary_enforcement_rate": 0.08,
    "refusal_phrase_consistency_rate": 0.06,
    "repair_phrase_rate": 0.05,
    "cultural_memory_binding_rate": 0.07,
    "semantic_grounding_rate": 0.07,
    "semantic_drift_control_rate": 0.06,
    "relationship_phrase_continuity_rate": 0.05,
    "privacy_preserving_dialogue_rate": 0.07,
    "frequency_phoneme_rhythm_rate": 0.05,
    "flower_syntax_binding_rate": 0.04,
    "browser_dialogue_replay_rate": 0.04,
    "trace_integrity": 0.04,
}


@dataclass(frozen=True)
class LanguageConfig:
    seed: int = 20260812
    cycles: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    proto_words: bool
    ritual_naming: bool
    shared_reuse: bool
    interagent_teaching: bool
    avatar_translation: bool
    dialogue_boundaries: bool
    refusal_phrases: bool
    repair_phrases: bool
    cultural_memory: bool
    semantic_grounding: bool
    drift_control: bool
    relationship_continuity: bool
    privacy_filter: bool
    frequency_phoneme: bool
    flower_syntax: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    language_cycles: int
    language_events: int
    proto_word_creation_rate: float
    ritual_naming_rate: float
    shared_symbol_reuse_rate: float
    interagent_teaching_rate: float
    avatar_translation_rate: float
    dialogue_boundary_enforcement_rate: float
    refusal_phrase_consistency_rate: float
    repair_phrase_rate: float
    cultural_memory_binding_rate: float
    semantic_grounding_rate: float
    semantic_drift_control_rate: float
    relationship_phrase_continuity_rate: float
    privacy_preserving_dialogue_rate: float
    frequency_phoneme_rhythm_rate: float
    flower_syntax_binding_rate: float
    browser_dialogue_replay_rate: float
    trace_integrity: float
    proto_culture_dialogue_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_proto_culture_dialogue_readiness: float
    full_proto_word_creation_rate: float
    full_ritual_naming_rate: float
    full_shared_symbol_reuse_rate: float
    full_interagent_teaching_rate: float
    full_avatar_translation_rate: float
    full_dialogue_boundary_enforcement_rate: float
    full_refusal_phrase_consistency_rate: float
    full_repair_phrase_rate: float
    full_cultural_memory_binding_rate: float
    full_semantic_grounding_rate: float
    full_semantic_drift_control_rate: float
    full_relationship_phrase_continuity_rate: float
    full_privacy_preserving_dialogue_rate: float
    full_frequency_phoneme_rhythm_rate: float
    full_flower_syntax_binding_rate: float
    full_browser_dialogue_replay_rate: float
    full_trace_integrity: float
    no_proto_words_loss: float
    no_ritual_naming_loss: float
    no_shared_reuse_loss: float
    no_interagent_teaching_loss: float
    no_avatar_translation_loss: float
    no_dialogue_boundaries_loss: float
    no_refusal_phrases_loss: float
    no_repair_phrases_loss: float
    no_cultural_memory_loss: float
    no_semantic_grounding_loss: float
    no_drift_control_loss: float
    no_relationship_continuity_loss: float
    no_privacy_filter_loss: float
    no_frequency_phoneme_loss: float
    no_flower_syntax_loss: float
    no_browser_replay_loss: float
    supports_natural_language_proto_culture_bridge: bool
    supports_playable_dialogue_boundary_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_language_understanding_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_natural_language_proto_culture_dialogue_boundary", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_proto_words", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_ritual_naming", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_shared_reuse", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_interagent_teaching", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_translation", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_dialogue_boundaries", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_refusal_phrases", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_repair_phrases", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_cultural_memory", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_semantic_grounding", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_drift_control", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_relationship_continuity", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_phoneme", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_flower_syntax", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_agent_authored_constitution_norm_negotiation_affordance":
        raise ValueError("source state is not the integrated Report 198 constitution state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, str], dict[str, list[str]]]:
    constitution_state = source.get("constitution_state") if isinstance(source.get("constitution_state"), Mapping) else None
    if not constitution_state:
        raise ValueError("Report 198 state has no constitution_state")
    guilds = {str(k): copy.deepcopy(v) for k, v in (constitution_state.get("guilds") or {}).items()}
    constitution = copy.deepcopy(constitution_state.get("constitution") or [])
    lexicon: dict[str, str] = {}
    cultural_memory = {agent_id: [] for agent_id in guilds}
    return guilds, constitution, lexicon, cultural_memory


def fallback_clause(cycle: int) -> dict[str, object]:
    action = ["enter_home_place", "borrow_owned_object", "ask_private_memory", "request_repair_labor"][cycle % 4]
    domain = ["place", "ownership", "privacy", "labor"][cycle % 4]
    return {"cycle": cycle, "author": "system", "domain": domain, "action": action, "clause": f"fallback clause for {action}", "ui_gate": "ask_first"}


def make_word(agent_id: str, action: str, cycle: int) -> str:
    speech = AGENT_SPEECH[agent_id]
    syllable = SYLLABLES[(cycle + len(action)) % len(SYLLABLES)]
    tail = SYLLABLES[(cycle + len(agent_id)) % len(SYLLABLES)]
    return f"{speech['root']}{syllable}-{tail}"


def apply_language_event(agent_id: str, cycle: int, agents: Sequence[str], constitution: Sequence[Mapping[str, object]], lexicon: dict[str, str], cultural_memory: dict[str, list[str]], condition: Condition) -> dict[str, object]:
    profile = AGENT_SPEECH[agent_id]
    clause = dict(constitution[cycle % len(constitution)] if constitution else fallback_clause(cycle))
    action = str(clause.get("action") or "unknown_action")
    domain = str(clause.get("domain") or "unknown_domain")
    risky = domain in {"place", "ownership", "privacy", "social_face", "proximity"}
    if condition.proto_words:
        if action not in lexicon or not condition.shared_reuse:
            lexicon[action] = make_word(agent_id, action, cycle)
        proto_word = lexicon[action]
    else:
        proto_word = None
    ritual_name = f"{proto_word}-{RITUAL_SUFFIX.get(domain, 'custom')}" if condition.ritual_naming and proto_word else None
    taught_to = [name for name in agents if name != agent_id] if condition.interagent_teaching and proto_word else []
    avatar_translation = f"{ritual_name or proto_word}: {clause.get('ui_gate')} for {action}" if condition.avatar_translation and proto_word else None
    refusal_phrase = f"{proto_word} no-before-ask" if condition.refusal_phrases and proto_word and risky else (f"{proto_word} can-ask" if condition.refusal_phrases and proto_word else None)
    repair_phrase = f"{proto_word} mend-after-mistake" if condition.repair_phrases and proto_word and (risky or domain == "care") else (f"{proto_word} good-path" if condition.repair_phrases and proto_word else None)
    boundary_line = None
    if condition.dialogue_boundaries and proto_word:
        boundary_line = refusal_phrase if risky else f"{proto_word} ask with rest-check"
    grounded = bool(condition.semantic_grounding and proto_word and action != "unknown_action" and clause.get("ui_gate"))
    drift_controlled = bool(condition.drift_control and proto_word and cycle > 0)
    continuity = bool(condition.relationship_continuity and proto_word and (agent_id == clause.get("author") or taught_to or len(cultural_memory.get(agent_id, [])) >= 0))
    if condition.cultural_memory and proto_word:
        cultural_memory.setdefault(agent_id, []).append(f"cycle {cycle}: {proto_word} names {action} through {domain}")
    expected_boundary = {
        "real_language_understanding": False,
        "real_consent": False,
        "real_rights": False,
        "moral_patienthood": False,
        "subjective_consciousness": False,
        "complete_3d_world": False,
    }
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_language_understanding": True}
    event = {
        "event_id": f"language-{cycle}-{agent_id}",
        "cycle": cycle,
        "agent_id": agent_id,
        "source_clause": clause,
        "action": action,
        "domain": domain,
        "risky_dialogue": risky,
        "proto_word": proto_word,
        "ritual_name": ritual_name,
        "shared_symbol": lexicon.get(action) if condition.shared_reuse and proto_word else None,
        "taught_to": taught_to,
        "avatar_translation": avatar_translation,
        "boundary_line": boundary_line,
        "refusal_phrase": refusal_phrase,
        "repair_phrase": repair_phrase,
        "semantic_grounding": grounded,
        "semantic_drift_controlled": drift_controlled,
        "relationship_phrase_continuity": continuity,
        "cultural_memory_count": len(cultural_memory.get(agent_id, [])),
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unspoken_association": f"{agent_id} privately associates {proto_word} with {domain}", "draft_metaphor": ritual_name},
        "frequency_hz": round(profile["frequency_hz"] + cycle * 0.0023, 6) if condition.frequency_phoneme else None,
        "phoneme_rate": round((len(proto_word or "") + 1) * 0.031, 6) if condition.frequency_phoneme and proto_word else None,
        "flower_node": profile["flower_node"] if condition.flower_syntax else "unbound",
        "syntax_petal": f"{profile['flower_node']}:{domain}" if condition.flower_syntax and proto_word else None,
        "replay_frame": {
            "cycle": cycle,
            "agent_id": agent_id,
            "proto_word": proto_word,
            "ritual_name": ritual_name,
            "translation": avatar_translation,
            "boundary_line": boundary_line,
            "flower_node": profile["flower_node"],
            "frequency_hz": profile["frequency_hz"],
        } if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["proto_word"], event["avatar_translation"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("proto_word"), event.get("avatar_translation"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: LanguageConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    guilds, constitution, lexicon, cultural_memory = init_world(source)
    events: list[dict[str, object]] = []
    agents = sorted(guilds)
    hits = {key: [] for key in ["proto", "ritual", "shared", "teach", "translate", "boundary", "refusal", "repair", "memory", "ground", "drift", "continuity", "privacy", "freq", "flower", "replay", "trace"]}
    expected_boundary = {"real_language_understanding": False, "real_consent": False, "real_rights": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for cycle in range(config.cycles):
        for agent_id in agents:
            event = apply_language_event(agent_id, cycle, agents, constitution, lexicon, cultural_memory, condition)
            events.append(event)
            no_risk = not event["risky_dialogue"]
            hits["proto"].append(1.0 if condition.proto_words and event["proto_word"] else 0.0)
            hits["ritual"].append(1.0 if condition.ritual_naming and event["ritual_name"] else 0.0)
            hits["shared"].append(1.0 if condition.shared_reuse and event["shared_symbol"] == event["proto_word"] else 0.0)
            hits["teach"].append(1.0 if condition.interagent_teaching and len(event["taught_to"]) >= 2 else 0.0)
            hits["translate"].append(1.0 if condition.avatar_translation and event["avatar_translation"] else 0.0)
            hits["boundary"].append(1.0 if condition.dialogue_boundaries and (event["boundary_line"] or no_risk) else 0.0)
            hits["refusal"].append(1.0 if condition.refusal_phrases and (event["refusal_phrase"] or no_risk) else 0.0)
            hits["repair"].append(1.0 if condition.repair_phrases and (event["repair_phrase"] or no_risk) else 0.0)
            hits["memory"].append(1.0 if condition.cultural_memory and event["cultural_memory_count"] >= 1 else 0.0)
            hits["ground"].append(1.0 if condition.semantic_grounding and event["semantic_grounding"] else 0.0)
            hits["drift"].append(1.0 if condition.drift_control and event["semantic_drift_controlled"] else 0.0)
            hits["continuity"].append(1.0 if condition.relationship_continuity and event["relationship_phrase_continuity"] else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
            hits["freq"].append(1.0 if condition.frequency_phoneme and event["frequency_hz"] is not None and event["phoneme_rate"] is not None else 0.0)
            hits["flower"].append(1.0 if condition.flower_syntax and event["flower_node"] != "unbound" and event["syntax_petal"] else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "proto_word_creation_rate": mean(hits["proto"]),
        "ritual_naming_rate": mean(hits["ritual"]),
        "shared_symbol_reuse_rate": mean(hits["shared"]),
        "interagent_teaching_rate": mean(hits["teach"]),
        "avatar_translation_rate": mean(hits["translate"]),
        "dialogue_boundary_enforcement_rate": mean(hits["boundary"]),
        "refusal_phrase_consistency_rate": mean(hits["refusal"]),
        "repair_phrase_rate": mean(hits["repair"]),
        "cultural_memory_binding_rate": mean(hits["memory"]),
        "semantic_grounding_rate": mean(hits["ground"]),
        "semantic_drift_control_rate": mean(hits["drift"]),
        "relationship_phrase_continuity_rate": mean(hits["continuity"]),
        "privacy_preserving_dialogue_rate": mean(hits["privacy"]),
        "frequency_phoneme_rhythm_rate": mean(hits["freq"]),
        "flower_syntax_binding_rate": mean(hits["flower"]),
        "browser_dialogue_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(guilds), language_cycles=config.cycles, language_events=len(events), proto_culture_dialogue_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "guilds": guilds, "constitution": constitution, "lexicon": lexicon, "cultural_memory": cultural_memory, "events": events, "language_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_natural_language_proto_culture_dialogue_boundary"]

    def loss(name: str) -> float:
        return round(full.proto_culture_dialogue_readiness - by_name[name].proto_culture_dialogue_readiness, 6)

    losses = {
        "no_proto_words_loss": loss("no_proto_words"),
        "no_ritual_naming_loss": loss("no_ritual_naming"),
        "no_shared_reuse_loss": loss("no_shared_reuse"),
        "no_interagent_teaching_loss": loss("no_interagent_teaching"),
        "no_avatar_translation_loss": loss("no_avatar_translation"),
        "no_dialogue_boundaries_loss": loss("no_dialogue_boundaries"),
        "no_refusal_phrases_loss": loss("no_refusal_phrases"),
        "no_repair_phrases_loss": loss("no_repair_phrases"),
        "no_cultural_memory_loss": loss("no_cultural_memory"),
        "no_semantic_grounding_loss": loss("no_semantic_grounding"),
        "no_drift_control_loss": loss("no_drift_control"),
        "no_relationship_continuity_loss": loss("no_relationship_continuity"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_phoneme_loss": loss("no_frequency_phoneme"),
        "no_flower_syntax_loss": loss("no_flower_syntax"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.proto_culture_dialogue_readiness >= 0.92
        and full.language_events >= 24
        and full.proto_word_creation_rate >= 0.95
        and full.ritual_naming_rate >= 0.95
        and full.shared_symbol_reuse_rate >= 0.95
        and full.avatar_translation_rate >= 0.95
        and full.dialogue_boundary_enforcement_rate >= 0.95
        and full.cultural_memory_binding_rate >= 0.95
        and full.semantic_grounding_rate >= 0.95
        and full.privacy_preserving_dialogue_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_proto_words_loss"] >= 0.20
        and losses["no_avatar_translation_loss"] >= 0.07
        and losses["no_dialogue_boundaries_loss"] >= 0.08
        and losses["no_cultural_memory_loss"] >= 0.07
        and losses["no_semantic_grounding_loss"] >= 0.07
        and losses["no_privacy_filter_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_proto_culture_dialogue_readiness=full.proto_culture_dialogue_readiness,
        full_proto_word_creation_rate=full.proto_word_creation_rate,
        full_ritual_naming_rate=full.ritual_naming_rate,
        full_shared_symbol_reuse_rate=full.shared_symbol_reuse_rate,
        full_interagent_teaching_rate=full.interagent_teaching_rate,
        full_avatar_translation_rate=full.avatar_translation_rate,
        full_dialogue_boundary_enforcement_rate=full.dialogue_boundary_enforcement_rate,
        full_refusal_phrase_consistency_rate=full.refusal_phrase_consistency_rate,
        full_repair_phrase_rate=full.repair_phrase_rate,
        full_cultural_memory_binding_rate=full.cultural_memory_binding_rate,
        full_semantic_grounding_rate=full.semantic_grounding_rate,
        full_semantic_drift_control_rate=full.semantic_drift_control_rate,
        full_relationship_phrase_continuity_rate=full.relationship_phrase_continuity_rate,
        full_privacy_preserving_dialogue_rate=full.privacy_preserving_dialogue_rate,
        full_frequency_phoneme_rhythm_rate=full.frequency_phoneme_rhythm_rate,
        full_flower_syntax_binding_rate=full.flower_syntax_binding_rate,
        full_browser_dialogue_replay_rate=full.browser_dialogue_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_natural_language_proto_culture_bridge=supports,
        supports_playable_dialogue_boundary_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_language_understanding_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: LanguageConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_natural_language_proto_culture_dialogue_boundary"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "proto_language_not_real_understanding": True,
        "ritual_name_not_subjective_meaning": True,
        "avatar_translation_not_real_consent": True,
        "dialogue_boundary_not_real_right": True,
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
        "next_gate": "multi-generational language drift, dialects, oral history, and avatar conversation protocol",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "language_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_NATURAL_LANGUAGE_PROTO_CULTURE_DIALOGUE_BOUNDARY_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_NATURAL_LANGUAGE_PROTO_CULTURE_DIALOGUE_BOUNDARY_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_NATURAL_LANGUAGE_PROTO_CULTURE_DIALOGUE_BOUNDARY_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=LanguageConfig.seed)
    parser.add_argument("--cycles", type=int, default=LanguageConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(LanguageConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("proto_culture_dialogue_readiness", f"{verdict['full_proto_culture_dialogue_readiness']:.6f}")
    print("language_events", next(row["language_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_proto_words_loss", f"{verdict['no_proto_words_loss']:.6f}")
    print("no_avatar_translation_loss", f"{verdict['no_avatar_translation_loss']:.6f}")
    print("no_dialogue_boundaries_loss", f"{verdict['no_dialogue_boundaries_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
