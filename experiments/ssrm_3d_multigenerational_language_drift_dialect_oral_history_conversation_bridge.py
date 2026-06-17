#!/usr/bin/env python3
"""Multi-generational language drift, dialects, oral history, and conversation protocol.

Report 200 consumes the Report 199 proto-culture state and simulates language
continuity before avatar entry: lexicon inheritance across generations,
controlled drift, dialect branching, mutual intelligibility, oral history,
ritual-lineage recall, avatar conversation protocol, translation repair, privacy
preservation, frequency drift, flower lineage binding, and browser replay.

This is deterministic cultural-language substrate, not real language
understanding, real consent, real rights, subjective consciousness, moral
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
PREFIX = "ssrm_3d_multigenerational_language_drift_dialect_oral_history_conversation_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_natural_language_proto_culture_dialogue_boundary_bridge_state.json"

LINEAGES = {
    "Ari": {"dialect_seed": "kar", "identity": "workline", "flower_node": "work_petal", "base_frequency": 0.257},
    "Fay": {"dialect_seed": "lum", "identity": "restline", "flower_node": "root_rest", "base_frequency": 0.235},
    "Milo": {"dialect_seed": "ril", "identity": "routeline", "flower_node": "social_petal", "base_frequency": 0.274},
}

DRIFT_MARKS = ["a", "e", "i", "o", "u", "an", "el", "or", "im", "ul", "sa", "ve"]

WEIGHTS = {
    "generation_continuity_rate": 0.08,
    "lexicon_inheritance_rate": 0.08,
    "controlled_drift_rate": 0.08,
    "dialect_branch_rate": 0.07,
    "mutual_intelligibility_rate": 0.07,
    "oral_history_retention_rate": 0.08,
    "ritual_lineage_recall_rate": 0.06,
    "avatar_conversation_protocol_rate": 0.08,
    "turn_taking_boundary_rate": 0.06,
    "translation_repair_rate": 0.06,
    "privacy_preserving_conversation_rate": 0.07,
    "cultural_identity_persistence_rate": 0.06,
    "frequency_drift_rhythm_rate": 0.05,
    "flower_lineage_binding_rate": 0.04,
    "browser_conversation_replay_rate": 0.03,
    "trace_integrity": 0.03,
}


@dataclass(frozen=True)
class GenerationConfig:
    seed: int = 20260813
    generations: int = 12
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    generation_continuity: bool
    lexicon_inheritance: bool
    controlled_drift: bool
    dialect_branching: bool
    mutual_intelligibility: bool
    oral_history: bool
    ritual_lineage: bool
    avatar_protocol: bool
    turn_taking: bool
    translation_repair: bool
    privacy_filter: bool
    cultural_identity: bool
    frequency_drift: bool
    flower_lineage: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    lineage_count: int
    generation_count: int
    generation_events: int
    generation_continuity_rate: float
    lexicon_inheritance_rate: float
    controlled_drift_rate: float
    dialect_branch_rate: float
    mutual_intelligibility_rate: float
    oral_history_retention_rate: float
    ritual_lineage_recall_rate: float
    avatar_conversation_protocol_rate: float
    turn_taking_boundary_rate: float
    translation_repair_rate: float
    privacy_preserving_conversation_rate: float
    cultural_identity_persistence_rate: float
    frequency_drift_rhythm_rate: float
    flower_lineage_binding_rate: float
    browser_conversation_replay_rate: float
    trace_integrity: float
    generational_language_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_generational_language_readiness: float
    full_generation_continuity_rate: float
    full_lexicon_inheritance_rate: float
    full_controlled_drift_rate: float
    full_dialect_branch_rate: float
    full_mutual_intelligibility_rate: float
    full_oral_history_retention_rate: float
    full_ritual_lineage_recall_rate: float
    full_avatar_conversation_protocol_rate: float
    full_turn_taking_boundary_rate: float
    full_translation_repair_rate: float
    full_privacy_preserving_conversation_rate: float
    full_cultural_identity_persistence_rate: float
    full_frequency_drift_rhythm_rate: float
    full_flower_lineage_binding_rate: float
    full_browser_conversation_replay_rate: float
    full_trace_integrity: float
    no_generation_continuity_loss: float
    no_lexicon_inheritance_loss: float
    no_controlled_drift_loss: float
    no_dialect_branching_loss: float
    no_mutual_intelligibility_loss: float
    no_oral_history_loss: float
    no_ritual_lineage_loss: float
    no_avatar_protocol_loss: float
    no_turn_taking_loss: float
    no_translation_repair_loss: float
    no_privacy_filter_loss: float
    no_cultural_identity_loss: float
    no_frequency_drift_loss: float
    no_flower_lineage_loss: float
    no_browser_replay_loss: float
    supports_multigenerational_language_bridge: bool
    supports_avatar_conversation_protocol_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_language_understanding_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_multigenerational_language_drift_dialect_oral_history_conversation", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_generation_continuity", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_lexicon_inheritance", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_controlled_drift", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_dialect_branching", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_mutual_intelligibility", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_oral_history", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_ritual_lineage", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_avatar_protocol", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_turn_taking", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_translation_repair", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_cultural_identity", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_drift", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_flower_lineage", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_natural_language_proto_culture_dialogue_boundary":
        raise ValueError("source state is not the integrated Report 199 language state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, str], dict[str, list[str]], list[dict[str, object]]]:
    language_state = source.get("language_state") if isinstance(source.get("language_state"), Mapping) else None
    if not language_state:
        raise ValueError("Report 199 state has no language_state")
    lexicon = {str(k): str(v) for k, v in (language_state.get("lexicon") or {}).items()}
    cultural_memory = {str(k): list(v) for k, v in (language_state.get("cultural_memory") or {}).items()}
    source_events = copy.deepcopy(language_state.get("events") or [])
    return lexicon, cultural_memory, source_events


def action_for_generation(actions: Sequence[str], generation: int, lineage: str) -> str:
    if not actions:
        return "ask_route_help"
    return actions[(generation + len(lineage)) % len(actions)]


def drift_word(base_word: str, lineage: str, generation: int, condition: Condition) -> tuple[str | None, bool, float]:
    if not condition.lexicon_inheritance or not base_word:
        return None, False, 0.0
    if not condition.controlled_drift:
        uncontrolled = f"{generation}-{base_word[::-1]}-{LINEAGES[lineage]['dialect_seed']}"
        return uncontrolled, False, 0.28
    marker = DRIFT_MARKS[(generation + len(lineage)) % len(DRIFT_MARKS)]
    if generation == 0:
        return base_word, True, 1.0
    drifted = f"{base_word}.{LINEAGES[lineage]['dialect_seed']}{marker}{generation % 4}"
    intelligibility = max(0.74, 1.0 - generation * 0.018)
    return drifted, True, round(intelligibility, 6)


def apply_generation_event(lineage: str, generation: int, lexicon: Mapping[str, str], cultural_memory: dict[str, list[str]], source_events: Sequence[Mapping[str, object]], condition: Condition) -> dict[str, object]:
    profile = LINEAGES[lineage]
    actions = sorted(lexicon)
    action = action_for_generation(actions, generation, lineage)
    base_word = lexicon.get(action, "")
    descendant = f"{lineage}-g{generation:02d}" if condition.generation_continuity else f"unbound-g{generation:02d}"
    inherited_word, drift_bounded, intelligibility = drift_word(base_word, lineage, generation, condition)
    dialect_id = f"{profile['identity']}-{generation // 3}" if condition.dialect_branching and generation > 0 and inherited_word else None
    mutual_ok = bool(condition.mutual_intelligibility and inherited_word and intelligibility >= 0.70)
    elder_memory = cultural_memory.get(lineage, [])[:2]
    source_phrase = next((str(ev.get("avatar_translation")) for ev in source_events if ev.get("action") == action and ev.get("avatar_translation")), f"{base_word}: inherited boundary for {action}")
    oral_history = []
    if condition.oral_history and inherited_word:
        oral_history = elder_memory + [f"generation {generation}: {descendant} says {inherited_word} still points to {action}"]
    ritual_recall = f"{profile['identity']} keeps {inherited_word} from elder speech" if condition.ritual_lineage and oral_history else None
    protocol = None
    if condition.avatar_protocol and inherited_word:
        protocol = [
            {"speaker": descendant, "act": "greet_with_lineage_word", "text": inherited_word},
            {"speaker": "avatar", "act": "ask_translation", "text": "what does that boundary word mean?"},
            {"speaker": descendant, "act": "translate_norm", "text": source_phrase},
            {"speaker": "avatar", "act": "wait_for_consent_state", "text": "I will wait for the visible gate."},
        ]
    turn_boundary = bool(condition.turn_taking and protocol and protocol[0]["speaker"] == descendant and protocol[-1]["act"] == "wait_for_consent_state")
    translation_repair = None
    if condition.translation_repair and inherited_word and generation > 0:
        translation_repair = f"if avatar misses {inherited_word}, restate elder word {base_word} and gate {action}"
    expected_boundary = {
        "real_language_understanding": False,
        "real_consent": False,
        "real_rights": False,
        "moral_patienthood": False,
        "subjective_consciousness": False,
        "complete_3d_world": False,
    }
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_language_understanding": True}
    identity_persistent = bool(condition.cultural_identity and descendant.startswith(lineage) and dialect_id and oral_history)
    frequency = round(profile["base_frequency"] + generation * 0.0031 + intelligibility * 0.002, 6) if condition.frequency_drift and inherited_word else None
    flower_lineage = f"{profile['flower_node']}:{profile['identity']}:g{generation}" if condition.flower_lineage and inherited_word else None
    event = {
        "event_id": f"generation-{generation}-{lineage}",
        "generation": generation,
        "lineage": lineage,
        "descendant": descendant,
        "action": action,
        "base_word": base_word,
        "inherited_word": inherited_word,
        "drift_bounded": drift_bounded,
        "intelligibility": intelligibility,
        "dialect_id": dialect_id,
        "mutual_intelligibility": mutual_ok,
        "oral_history": oral_history,
        "ritual_recall": ritual_recall,
        "avatar_conversation_protocol": protocol,
        "turn_taking_boundary": turn_boundary,
        "translation_repair": translation_repair,
        "cultural_identity_persistent": identity_persistent,
        "source_phrase": source_phrase,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unspoken_dialect_association": f"{descendant} privately links {inherited_word} with {lineage}", "elder_memory": elder_memory},
        "frequency_hz": frequency,
        "flower_lineage": flower_lineage,
        "replay_frame": {
            "generation": generation,
            "lineage": lineage,
            "descendant": descendant,
            "action": action,
            "base_word": base_word,
            "inherited_word": inherited_word,
            "dialect_id": dialect_id,
            "intelligibility": intelligibility,
            "protocol_turns": len(protocol or []),
            "frequency_hz": frequency,
            "flower_lineage": flower_lineage,
        } if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["inherited_word"], event["dialect_id"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("inherited_word"), event.get("dialect_id"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: GenerationConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    lexicon, cultural_memory, source_events = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["generation", "lexicon", "drift", "dialect", "mutual", "oral", "ritual", "protocol", "turn", "repair", "privacy", "identity", "freq", "flower", "replay", "trace"]}
    expected_boundary = {"real_language_understanding": False, "real_consent": False, "real_rights": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for generation in range(config.generations):
        for lineage in sorted(LINEAGES):
            event = apply_generation_event(lineage, generation, lexicon, cultural_memory, source_events, condition)
            events.append(event)
            hits["generation"].append(1.0 if condition.generation_continuity and event["descendant"].startswith(lineage) else 0.0)
            hits["lexicon"].append(1.0 if condition.lexicon_inheritance and event["inherited_word"] and event["base_word"] in str(event["inherited_word"]) else 0.0)
            hits["drift"].append(1.0 if condition.controlled_drift and event["drift_bounded"] and event["intelligibility"] >= 0.70 else 0.0)
            hits["dialect"].append(1.0 if condition.dialect_branching and (event["dialect_id"] or generation == 0) else 0.0)
            hits["mutual"].append(1.0 if condition.mutual_intelligibility and event["mutual_intelligibility"] else 0.0)
            hits["oral"].append(1.0 if condition.oral_history and len(event["oral_history"]) >= 1 else 0.0)
            hits["ritual"].append(1.0 if condition.ritual_lineage and event["ritual_recall"] else 0.0)
            hits["protocol"].append(1.0 if condition.avatar_protocol and event["avatar_conversation_protocol"] and len(event["avatar_conversation_protocol"]) >= 4 else 0.0)
            hits["turn"].append(1.0 if condition.turn_taking and event["turn_taking_boundary"] else 0.0)
            hits["repair"].append(1.0 if condition.translation_repair and (event["translation_repair"] or generation == 0) else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
            hits["identity"].append(1.0 if condition.cultural_identity and (event["cultural_identity_persistent"] or generation == 0) else 0.0)
            hits["freq"].append(1.0 if condition.frequency_drift and event["frequency_hz"] is not None else 0.0)
            hits["flower"].append(1.0 if condition.flower_lineage and event["flower_lineage"] else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "generation_continuity_rate": mean(hits["generation"]),
        "lexicon_inheritance_rate": mean(hits["lexicon"]),
        "controlled_drift_rate": mean(hits["drift"]),
        "dialect_branch_rate": mean(hits["dialect"]),
        "mutual_intelligibility_rate": mean(hits["mutual"]),
        "oral_history_retention_rate": mean(hits["oral"]),
        "ritual_lineage_recall_rate": mean(hits["ritual"]),
        "avatar_conversation_protocol_rate": mean(hits["protocol"]),
        "turn_taking_boundary_rate": mean(hits["turn"]),
        "translation_repair_rate": mean(hits["repair"]),
        "privacy_preserving_conversation_rate": mean(hits["privacy"]),
        "cultural_identity_persistence_rate": mean(hits["identity"]),
        "frequency_drift_rhythm_rate": mean(hits["freq"]),
        "flower_lineage_binding_rate": mean(hits["flower"]),
        "browser_conversation_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, lineage_count=len(LINEAGES), generation_count=config.generations, generation_events=len(events), generational_language_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "lineages": LINEAGES, "source_lexicon": lexicon, "cultural_memory": cultural_memory, "events": events, "generation_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_multigenerational_language_drift_dialect_oral_history_conversation"]

    def loss(name: str) -> float:
        return round(full.generational_language_readiness - by_name[name].generational_language_readiness, 6)

    losses = {
        "no_generation_continuity_loss": loss("no_generation_continuity"),
        "no_lexicon_inheritance_loss": loss("no_lexicon_inheritance"),
        "no_controlled_drift_loss": loss("no_controlled_drift"),
        "no_dialect_branching_loss": loss("no_dialect_branching"),
        "no_mutual_intelligibility_loss": loss("no_mutual_intelligibility"),
        "no_oral_history_loss": loss("no_oral_history"),
        "no_ritual_lineage_loss": loss("no_ritual_lineage"),
        "no_avatar_protocol_loss": loss("no_avatar_protocol"),
        "no_turn_taking_loss": loss("no_turn_taking"),
        "no_translation_repair_loss": loss("no_translation_repair"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_cultural_identity_loss": loss("no_cultural_identity"),
        "no_frequency_drift_loss": loss("no_frequency_drift"),
        "no_flower_lineage_loss": loss("no_flower_lineage"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.generational_language_readiness >= 0.92
        and full.generation_events >= 36
        and full.generation_continuity_rate >= 0.95
        and full.lexicon_inheritance_rate >= 0.95
        and full.controlled_drift_rate >= 0.95
        and full.dialect_branch_rate >= 0.90
        and full.mutual_intelligibility_rate >= 0.95
        and full.oral_history_retention_rate >= 0.95
        and full.avatar_conversation_protocol_rate >= 0.95
        and full.privacy_preserving_conversation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_lexicon_inheritance_loss"] >= 0.20
        and losses["no_controlled_drift_loss"] >= 0.10
        and losses["no_dialect_branching_loss"] >= 0.05
        and losses["no_oral_history_loss"] >= 0.08
        and losses["no_avatar_protocol_loss"] >= 0.08
        and losses["no_privacy_filter_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_generational_language_readiness=full.generational_language_readiness,
        full_generation_continuity_rate=full.generation_continuity_rate,
        full_lexicon_inheritance_rate=full.lexicon_inheritance_rate,
        full_controlled_drift_rate=full.controlled_drift_rate,
        full_dialect_branch_rate=full.dialect_branch_rate,
        full_mutual_intelligibility_rate=full.mutual_intelligibility_rate,
        full_oral_history_retention_rate=full.oral_history_retention_rate,
        full_ritual_lineage_recall_rate=full.ritual_lineage_recall_rate,
        full_avatar_conversation_protocol_rate=full.avatar_conversation_protocol_rate,
        full_turn_taking_boundary_rate=full.turn_taking_boundary_rate,
        full_translation_repair_rate=full.translation_repair_rate,
        full_privacy_preserving_conversation_rate=full.privacy_preserving_conversation_rate,
        full_cultural_identity_persistence_rate=full.cultural_identity_persistence_rate,
        full_frequency_drift_rhythm_rate=full.frequency_drift_rhythm_rate,
        full_flower_lineage_binding_rate=full.flower_lineage_binding_rate,
        full_browser_conversation_replay_rate=full.browser_conversation_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_multigenerational_language_bridge=supports,
        supports_avatar_conversation_protocol_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_language_understanding_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: GenerationConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_multigenerational_language_drift_dialect_oral_history_conversation"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "generational_language_not_real_understanding": True,
        "dialect_identity_not_moral_status": True,
        "oral_history_not_subjective_memory": True,
        "avatar_protocol_not_real_consent": True,
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
        "next_gate": "pre-avatar deep time simulator with institutions, languages, dialects, rituals, tools, and settlement memory",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "generational_language_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_MULTIGENERATIONAL_LANGUAGE_DRIFT_DIALECT_ORAL_HISTORY_CONVERSATION_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_MULTIGENERATIONAL_LANGUAGE_DRIFT_DIALECT_ORAL_HISTORY_CONVERSATION_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_MULTIGENERATIONAL_LANGUAGE_DRIFT_DIALECT_ORAL_HISTORY_CONVERSATION_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=GenerationConfig.seed)
    parser.add_argument("--generations", type=int, default=GenerationConfig.generations)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(GenerationConfig(seed=args.seed, generations=args.generations, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("generational_language_readiness", f"{verdict['full_generational_language_readiness']:.6f}")
    print("generation_events", next(row["generation_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_lexicon_inheritance_loss", f"{verdict['no_lexicon_inheritance_loss']:.6f}")
    print("no_controlled_drift_loss", f"{verdict['no_controlled_drift_loss']:.6f}")
    print("no_avatar_protocol_loss", f"{verdict['no_avatar_protocol_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
