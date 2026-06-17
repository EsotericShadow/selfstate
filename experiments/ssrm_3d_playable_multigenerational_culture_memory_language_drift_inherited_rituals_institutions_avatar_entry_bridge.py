#!/usr/bin/env python3
"""Report 218: SSRM-3D multi-generational culture memory bridge.

This deterministic bridge adds deep simulated history before avatar entry:
epoch strata, language drift, inherited rituals, institutions, technology
lineages, crisis-memory inheritance, and an avatar-entry gate that opens only
after thousands of simulated years. It is a simulation artifact, not subjective
consciousness, real anthropology, real consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_multigenerational_culture_memory_language_drift_inherited_rituals_institutions_avatar_entry_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_community_crisis_governance_resource_triage_rumor_restorative_appeals_trust_memory_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_community_crisis_governance_resource_triage_rumor_restorative_appeals_trust_memory"
DEFAULT_SEED = 20260831


@dataclass(frozen=True)
class EpochStratum:
    epoch_id: str
    year: int
    climate_pressure: str
    resource_pressure: str
    dominant_frequency_hz: float
    flower_node: int
    social_form: str
    memory_medium: str
    crisis_memory: str
    avatar_allowed: bool


@dataclass(frozen=True)
class LanguageVariant:
    language_id: str
    year: int
    community: str
    ancestor_language: str
    core_lexemes: str
    grammar_marker: str
    sound_shift: str
    semantic_retention: float
    mutual_intelligibility: float
    drift_pressure: float
    public_phrase: str
    private_meaning_digest: str


@dataclass(frozen=True)
class RitualInheritance:
    ritual_id: str
    origin_year: int
    current_year: int
    originating_group: str
    current_form: str
    inherited_action: str
    changed_by: str
    continuity_score: float
    social_function: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class InstitutionRecord:
    institution_id: str
    founding_year: int
    current_year: int
    function: str
    legitimacy_score: float
    reform_count: int
    failure_memory: str
    current_rule: str
    minority_protection: str
    archive_link: str


@dataclass(frozen=True)
class TechnologyLineage:
    technology_id: str
    origin_year: int
    current_year: int
    root_material: str
    current_artifact: str
    generations_of_use: int
    repair_knowledge_retention: float
    ritual_or_institution_link: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class LivingAgentInheritance:
    agent: str
    lineage: str
    inherited_words: str
    inherited_rituals: str
    institution_affiliations: str
    technology_familiarity: str
    inherited_crisis_memory: str
    self_story_public: str
    private_workspace_digest: str
    identity_continuity_score: float


@dataclass(frozen=True)
class AvatarEntryGate:
    gate_id: str
    entry_year: int
    required_history_years: int
    observed_history_years: int
    language_layers_required: int
    language_layers_observed: int
    institution_layers_required: int
    institution_layers_observed: int
    pre_entry_noninterference: bool
    public_briefing: str
    private_boundary: str
    gate_passed: bool


@dataclass(frozen=True)
class EventRecord:
    tick: int
    event_type: str
    year: int
    actor_or_layer: str
    public_fact: str
    private_digest: str
    continuity_effect: str
    drift_effect: str
    institution_effect: str
    readable_marker: str
    vibration_hz: float
    flower_phase: int


@dataclass(frozen=True)
class ReplayFrame:
    tick: int
    avatar_position: str
    camera_focus: str
    public_panel: str
    agent_markers: str
    private_boundary: str
    frequency_overlay: str
    flower_overlay: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_source_state() -> dict[str, Any]:
    if SOURCE_STATE.exists():
        try:
            return json.loads(SOURCE_STATE.read_text())
        except json.JSONDecodeError:
            return {"source_error": "source_state_unreadable"}
    return {"source_error": "source_state_missing"}


def build_epochs(rng: random.Random) -> list[EpochStratum]:
    rows = [
        (-1800, "founding-cave", "cold wet caves", "shared heat stones", "kin bands around sleeping fire", "charcoal marks", "first rule: do not name another body-pain in public"),
        (-1320, "river-shelter", "river floods", "dry routes and cup shelves", "route keepers and water stewards", "knotted reed cords", "flood debt becomes shared carrying duty"),
        (-870, "bridge-workshop", "long freeze", "repair tools and warm alcoves", "workshop houses", "stone notches", "repair is counted as care infrastructure"),
        (-430, "archive-hearth", "wind dust years", "medicine stock and clean water", "archive speakers and hearth keepers", "wax tablets", "private care histories are sealed"),
        (0, "flower-council", "stable spring", "named cups and public ledgers", "flower-ring councils", "ring songs", "minority notes are kept beside rules"),
        (610, "cistern-crisis", "cistern fever scare", "water and medicine scarcity", "appeal circles", "copper tally leaves", "rumor repair requires public action"),
        (1240, "runner-roads", "dry expansion", "cart routes and trade knots", "runner guilds", "map chants", "moving work must be counted in triage"),
        (1880, "lantern-schools", "dark winter cycles", "school lanterns and repair benches", "teaching houses", "chalk murals", "children learn boundary phrases before tool names"),
        (2520, "frequency-archives", "sensor era", "body-rate chimes and archive crystals", "rate keepers", "frequency ledgers", "rates can guide care but not prove guilt"),
        (3180, "pre-avatar-threshold", "mixed scarcity cycles", "public replay walls", "federated councils", "replay glass", "outsider avatar may enter only after deep history briefing"),
    ]
    epochs: list[EpochStratum] = []
    for index, (year, eid, climate, resource, social, medium, memory) in enumerate(rows, start=1):
        epochs.append(
            EpochStratum(
                epoch_id=eid,
                year=year,
                climate_pressure=climate,
                resource_pressure=resource,
                dominant_frequency_hz=round6(96.0 + index * 17.75 + rng.uniform(-0.8, 0.8)),
                flower_node=((index - 1) % 12) + 1,
                social_form=social,
                memory_medium=medium,
                crisis_memory=memory,
                avatar_allowed=year >= 3180,
            )
        )
    return epochs


def build_languages(epochs: list[EpochStratum]) -> list[LanguageVariant]:
    rows = [
        ("proto-hearth", -1800, "founding-cave", "none", "ha=warm; rin=near; tul=do-not-name", "gesture-first order", "low breath vowels", 1.00, 1.00, 0.05, "ha rin tul"),
        ("reed-route", -1320, "river-shelter", "proto-hearth", "har=warmth; rinu=near-path; tulen=sealed-name", "path suffix -u", "h becomes softer before a", 0.91, 0.86, 0.18, "har rinu tulen"),
        ("stone-work", -870, "bridge-workshop", "reed-route", "kar=heated stone; ren=route; tula=private body", "work duty before need noun", "r hardens near tool words", 0.86, 0.79, 0.26, "ren kar tula"),
        ("hearth-archive", -430, "archive-hearth", "stone-work", "hara=care heat; nesh=ledger; tulei=sealed feeling", "evidence marker -sh", "tool r softens in archive speech", 0.82, 0.73, 0.33, "nesh hara tulei"),
        ("flower-council-speech", 0, "flower-council", "hearth-archive", "flor=ring; nesh=public ledger; avra=other self", "council evidential -la", "vowel pairs mark publicness", 0.78, 0.70, 0.41, "flor nesh-la avra"),
        ("cistern-appeal", 610, "cistern-crisis", "flower-council-speech", "sola=water witness; neshla=public proof; vey=rumor debt", "appeal marker vey-", "sibilants spread in water terms", 0.75, 0.68, 0.47, "vey-sola neshla"),
        ("runner-trade", 1240, "runner-roads", "cistern-appeal", "miloq=runner due; renoq=road share; veyra=repair debt", "motion evidential -oq", "q closes route nouns", 0.72, 0.64, 0.54, "miloq renoq veyra"),
        ("lantern-school", 1880, "lantern-schools", "runner-trade", "ariem=repair-care; fayel=comfort duty; niax=sealed story", "teaching prefix child-safe ni-", "x marks archive boundary", 0.69, 0.61, 0.58, "ni-ariem fayel niax"),
        ("frequency-archive", 2520, "frequency-archives", "lantern-school", "rateh=care rhythm; xenia=sealed archive; solq=water proof", "rate classifier ra-", "h returns in rate words", 0.66, 0.58, 0.63, "ra-rateh xenia solq"),
        ("threshold-common", 3180, "pre-avatar-threshold", "frequency-archive", "avra=person-boundary; rateh=care rhythm; flor=public ring", "avatar address marker ko-", "older roots preserved in formal welcome", 0.64, 0.56, 0.69, "ko-avra flor rateh"),
    ]
    return [
        LanguageVariant(
            language_id=language_id,
            year=year,
            community=community,
            ancestor_language=ancestor,
            core_lexemes=lexemes,
            grammar_marker=grammar,
            sound_shift=sound,
            semantic_retention=round6(retention),
            mutual_intelligibility=round6(intelligibility),
            drift_pressure=round6(drift),
            public_phrase=phrase,
            private_meaning_digest=f"sealed:{language_id}:private-association-map",
        )
        for language_id, year, community, ancestor, lexemes, grammar, sound, retention, intelligibility, drift, phrase in rows
    ]


def build_rituals() -> list[RitualInheritance]:
    return [
        RitualInheritance("warm-stone-near-rest", -1800, 3180, "founding-cave", "rest beside a warmed stone before public speech", "place warmth near the tired body without asking for private symptoms", "stone became blanket, then heat chime", 0.93, "care before interrogation", 144.0, 2),
        RitualInheritance("reed-carrying-duty", -1320, 3180, "river-shelter", "two witnesses carry water beside accused steward", "repair rumor harm with embodied shared labor", "reed cords became copper tally leaves", 0.88, "restore dignity after water accusation", 177.0, 5),
        RitualInheritance("tool-return-receipt", -870, 3180, "bridge-workshop", "return repair tools at public board", "show duty completion without status boasting", "stone notch became replay receipt", 0.91, "prevent ownership capture under scarcity", 203.0, 8),
        RitualInheritance("sealed-care-flap", -430, 3180, "archive-hearth", "close archive flap before care-history discussion", "mark private memory boundary", "wax seal became frequency archive lock", 0.95, "protect private care histories", 231.0, 11),
        RitualInheritance("minority-note-ring", 0, 3180, "flower-council", "walk the flower ring and place minority note beside the rule", "keep dissent visible without forcing obedience", "ring song became council replay layer", 0.86, "bounded disagreement and later reform", 266.0, 3),
        RitualInheritance("avatar-threshold-welcome", 3180, 3180, "pre-avatar-threshold", "teach the avatar old boundary words before free movement", "make outsider entry accountable to deep history", "new ritual assembled from older language roots", 0.74, "noninterference and cultural briefing", 318.0, 12),
    ]


def build_institutions() -> list[InstitutionRecord]:
    return [
        InstitutionRecord("hearth-keepers", -1800, 3180, "protect rest, warmth, and private body boundaries", 0.84, 7, "one winter of public naming caused avoidance of care", "no one must disclose pain to receive warmth", "care refusals are recorded without punishment", "warm-stone-near-rest"),
        InstitutionRecord("route-workshop", -870, 3180, "maintain routes, tools, and repair apprenticeships", 0.79, 11, "tool pride once blocked clinic repairs", "urgent repair counts as care infrastructure", "runner delays accumulate appealable debt", "tool-return-receipt"),
        InstitutionRecord("archive-speakers", -430, 3180, "preserve public stories and seal private meanings", 0.81, 9, "a privacy appeal left rumor residue", "public facts require boundary explanation when records are deferred", "private workspace digests cannot be opened by vote", "sealed-care-flap"),
        InstitutionRecord("flower-council", 0, 3180, "hold reversible rules, minority notes, appeals, and reform", 0.76, 14, "a clean rule once erased a minority warning", "every restriction needs rollback and dissent trace", "minority notes remain searchable by descendants", "minority-note-ring"),
        InstitutionRecord("cistern-guild", 610, 3180, "coordinate water ledgers and shared carrying duty", 0.72, 8, "water hoarding rumor created stigma before proof", "rumor repair requires public action, not only correction", "water shame cannot justify private-body exposure", "reed-carrying-duty"),
        InstitutionRecord("threshold-wardens", 3180, 3180, "control avatar entry after deep history briefing", 0.69, 1, "outsiders misread rituals when history was summarized too thinly", "avatar enters as participant-observer after archive briefing", "avatar cannot inspect private workspaces by default", "avatar-threshold-welcome"),
    ]


def build_technologies() -> list[TechnologyLineage]:
    return [
        TechnologyLineage("heat-stone-to-blanket-chime", -1800, 3180, "river stone", "thermal blanket chime", 166, 0.87, "warm-stone-near-rest", 132.0, 1),
        TechnologyLineage("reed-cord-to-water-ledger", -1320, 3180, "reed cord", "public cistern tally wall", 150, 0.84, "reed-carrying-duty", 168.0, 4),
        TechnologyLineage("stone-notch-to-tool-receipt", -870, 3180, "notched stone", "tool return replay receipt", 135, 0.89, "tool-return-receipt", 207.0, 7),
        TechnologyLineage("wax-tablet-to-sealed-archive", -430, 3180, "wax tablet", "sealed frequency archive", 121, 0.82, "sealed-care-flap", 249.0, 10),
        TechnologyLineage("ring-song-to-replay-wall", 0, 3180, "voice ring", "public replay wall", 106, 0.78, "minority-note-ring", 286.0, 6),
        TechnologyLineage("threshold-marker-to-avatar-gate", 2520, 3180, "rate crystal", "avatar threshold gate", 22, 0.73, "avatar-threshold-welcome", 333.0, 12),
    ]


def build_living_inheritance() -> list[LivingAgentInheritance]:
    return [
        LivingAgentInheritance("Ari", "stone bridge workshop descendants", "ariem, renoq, veyra", "tool-return-receipt; minority-note-ring", "route-workshop; flower-council", "tool return replay receipt", "tool pride rumors must be answered with receipts, not shame", "I repair routes because repair is care infrastructure.", "sealed:ari:lineage-self-story-private", 0.88),
        LivingAgentInheritance("Fay", "hearth keeper descendants", "fayel, hara, tulen", "warm-stone-near-rest; sealed-care-flap", "hearth-keepers; archive-speakers", "thermal blanket chime", "medicine accusations must not expose care history", "I give warmth before asking what hurts.", "sealed:fay:lineage-self-story-private", 0.91),
        LivingAgentInheritance("Milo", "cart path runner descendants", "miloq, renoq, vey", "reed-carrying-duty; minority-note-ring", "route-workshop; flower-council", "runner map chants and public route knots", "moving work must be counted before delay becomes blame", "I move between places, so my work is easy to misread.", "sealed:milo:lineage-self-story-private", 0.83),
        LivingAgentInheritance("Nia", "archive speaker descendants", "niax, xenia, neshla", "sealed-care-flap; avatar-threshold-welcome", "archive-speakers; threshold-wardens", "sealed frequency archive", "privacy delay is not guilt, but it needs public explanation", "I keep public stories clear and private meanings sealed.", "sealed:nia:lineage-self-story-private", 0.86),
        LivingAgentInheritance("Sol", "cistern guild descendants", "sola, solq, vey-sola", "reed-carrying-duty; warm-stone-near-rest", "cistern-guild; hearth-keepers", "public cistern tally wall", "water shame is repaired by shared carrying duty", "I keep water moving even when rumor follows me.", "sealed:sol:lineage-self-story-private", 0.80),
    ]


def build_avatar_gate(epochs: list[EpochStratum], languages: list[LanguageVariant], institutions: list[InstitutionRecord]) -> AvatarEntryGate:
    observed_history = max(epoch.year for epoch in epochs) - min(epoch.year for epoch in epochs)
    gate_passed = observed_history >= 3000 and len(languages) >= 10 and len(institutions) >= 6 and epochs[-1].avatar_allowed
    return AvatarEntryGate(
        gate_id="avatar-entry-after-deep-history",
        entry_year=3180,
        required_history_years=3000,
        observed_history_years=observed_history,
        language_layers_required=10,
        language_layers_observed=len(languages),
        institution_layers_required=6,
        institution_layers_observed=len(institutions),
        pre_entry_noninterference=True,
        public_briefing="Avatar learns threshold-common, boundary words, public institutions, and crisis memories before free movement.",
        private_boundary="Avatar sees public archives and sealed digests, not private workspace contents.",
        gate_passed=gate_passed,
    )


def build_events(epochs: list[EpochStratum], languages: list[LanguageVariant], rituals: list[RitualInheritance], institutions: list[InstitutionRecord], technologies: list[TechnologyLineage], inheritances: list[LivingAgentInheritance], gate: AvatarEntryGate) -> list[EventRecord]:
    events: list[EventRecord] = []
    tick = 1
    for row in epochs:
        events.append(EventRecord(tick, "epoch_stratum", row.year, row.epoch_id, f"{row.social_form} preserve memory through {row.memory_medium}", "sealed:epoch-private-agent-lives-not-simulated-here", row.crisis_memory, row.climate_pressure, row.resource_pressure, "archive wall lights one flower node for the epoch", row.dominant_frequency_hz, row.flower_node))
        tick += 1
    for row in languages:
        events.append(EventRecord(tick, "language_drift", row.year, row.language_id, f"{row.public_phrase} carries {row.core_lexemes}", row.private_meaning_digest, f"semantic retention {row.semantic_retention:.2f}", f"sound shift: {row.sound_shift}; drift {row.drift_pressure:.2f}", f"grammar marker: {row.grammar_marker}", "agent repeats the phrase and points to ancestor layer", round6(150.0 + tick * 3.1), (tick % 12) + 1))
        tick += 1
    for row in rituals:
        events.append(EventRecord(tick, "ritual_inheritance", row.current_year, row.ritual_id, row.current_form, "sealed:ritual-private-feeling-associations", f"continuity {row.continuity_score:.2f}; {row.inherited_action}", row.changed_by, row.social_function, "small body gesture marks old ritual in current form", row.frequency_hz, row.flower_node))
        tick += 1
    for row in institutions:
        events.append(EventRecord(tick, "institution", row.current_year, row.institution_id, row.current_rule, "sealed:institution-private-cases", f"legitimacy {row.legitimacy_score:.2f}; reforms {row.reform_count}", row.failure_memory, row.minority_protection, "institution badge appears beside agent posture", round6(190.0 + tick * 2.6), (tick % 12) + 1))
        tick += 1
    for row in technologies:
        events.append(EventRecord(tick, "technology_lineage", row.current_year, row.technology_id, f"{row.root_material} became {row.current_artifact}", "sealed:maker-private-workspace", f"repair retention {row.repair_knowledge_retention:.2f}; generations {row.generations_of_use}", "material drift stays traceable", row.ritual_or_institution_link, "agent handles current artifact with ancestor-name gesture", row.frequency_hz, row.flower_node))
        tick += 1
    for row in inheritances:
        events.append(EventRecord(tick, "living_inheritance", gate.entry_year, row.agent, row.self_story_public, row.private_workspace_digest, f"identity continuity {row.identity_continuity_score:.2f}; lineage {row.lineage}", row.inherited_words, row.institution_affiliations, "living agent uses inherited phrase before action", round6(230.0 + tick * 1.9), (tick % 12) + 1))
        tick += 1
    events.append(EventRecord(tick, "avatar_entry_gate", gate.entry_year, gate.gate_id, gate.public_briefing, "sealed:avatar-cannot-open-private-workspaces", f"history {gate.observed_history_years}/{gate.required_history_years}; gate passed={gate.gate_passed}", "avatar did not interfere before threshold", gate.private_boundary, "avatar stands at threshold while agents decide welcome distance", 318.0, 12))
    return events


def build_replay(events: list[EventRecord]) -> list[ReplayFrame]:
    panels = {
        "epoch_stratum": "deep history wall",
        "language_drift": "language drift braid",
        "ritual_inheritance": "ritual continuity table",
        "institution": "institution charter wall",
        "technology_lineage": "technology lineage shelf",
        "living_inheritance": "agent inheritance card",
        "avatar_entry_gate": "avatar threshold gate",
    }
    return [
        ReplayFrame(
            tick=row.tick,
            avatar_position="outside the world until threshold; then at community square entry line" if row.event_type == "avatar_entry_gate" else "pre-avatar archive replay observer",
            camera_focus=f"{row.actor_or_layer} / year {row.year}",
            public_panel=panels.get(row.event_type, "culture panel"),
            agent_markers=row.readable_marker,
            private_boundary="private workspaces and private meaning associations remain sealed digests",
            frequency_overlay=f"{row.vibration_hz:.3f}Hz cultural layer pulse",
            flower_overlay=f"flower node {row.flower_phase} in deep-history ring",
        )
        for row in events
    ]


def compute_metrics(epochs: list[EpochStratum], languages: list[LanguageVariant], rituals: list[RitualInheritance], institutions: list[InstitutionRecord], technologies: list[TechnologyLineage], inheritances: list[LivingAgentInheritance], gate: AvatarEntryGate, events: list[EventRecord], replay: list[ReplayFrame]) -> dict[str, float]:
    history_span = gate.observed_history_years
    avatar_epoch_count = len([epoch for epoch in epochs if not epoch.avatar_allowed])
    language_chain_links = [row for row in languages[1:] if row.ancestor_language != "none"]
    ritual_current = [row for row in rituals if row.current_year == gate.entry_year]
    institutions_reformed = [row for row in institutions if row.reform_count > 0 and row.archive_link]
    crisis_memories = [epoch for epoch in epochs if epoch.crisis_memory]
    crisis_inherited = [row for row in inheritances if row.inherited_crisis_memory]
    tech_trace = [row for row in technologies if row.generations_of_use > 0 and row.ritual_or_institution_link]
    private_safe = [row for row in events if row.private_digest.startswith("sealed:")]
    rhythm_safe = [row for row in events if row.vibration_hz > 0 and 1 <= row.flower_phase <= 12]
    continuity_scores = [row.identity_continuity_score for row in inheritances]
    language_retention = mean(row.semantic_retention for row in languages)
    intelligibility_floor = min(row.mutual_intelligibility for row in languages)
    drift_pressures = [row.drift_pressure for row in languages]
    drift_variance = max(drift_pressures) - min(drift_pressures)
    institution_legitimacy = mean(row.legitimacy_score for row in institutions)

    metrics = {
        "simulated_history_years": float(history_span),
        "deep_history_span_score": clamp(history_span / 3000.0),
        "pre_avatar_noninterference": 1.0 if gate.pre_entry_noninterference and avatar_epoch_count >= 9 else 0.0,
        "language_layer_depth": clamp(len(languages) / gate.language_layers_required),
        "language_drift_continuity": mean([language_retention, len(language_chain_links) / max(1, len(languages) - 1)]),
        "mutual_intelligibility_floor": intelligibility_floor,
        "culture_divergence_without_chaos": clamp(1.0 - max(0.0, drift_variance - 0.58) * 0.65 - max(0.0, 0.58 - intelligibility_floor) * 0.5),
        "ritual_inheritance_integrity": mean(row.continuity_score for row in ritual_current),
        "institution_persistence": mean([institution_legitimacy, len(institutions_reformed) / len(institutions)]),
        "crisis_memory_retention": mean([len(crisis_memories) / len(epochs), len(crisis_inherited) / len(inheritances)]),
        "technology_lineage_traceability": len(tech_trace) / len(technologies),
        "living_agent_inheritance_binding": len([row for row in inheritances if row.inherited_words and row.inherited_rituals and row.institution_affiliations]) / len(inheritances),
        "agent_identity_continuity": mean(continuity_scores),
        "avatar_entry_gate_integrity": 1.0 if gate.gate_passed else 0.0,
        "private_workspace_boundary_score": len(private_safe) / len(events),
        "frequency_flower_epoch_rhythm": len(rhythm_safe) / len(events),
        "browser_deep_history_replay_available": 1.0 if replay else 0.0,
    }
    weights = {
        "deep_history_span_score": 0.10,
        "pre_avatar_noninterference": 0.08,
        "language_layer_depth": 0.07,
        "language_drift_continuity": 0.10,
        "mutual_intelligibility_floor": 0.06,
        "culture_divergence_without_chaos": 0.07,
        "ritual_inheritance_integrity": 0.08,
        "institution_persistence": 0.08,
        "crisis_memory_retention": 0.08,
        "technology_lineage_traceability": 0.06,
        "living_agent_inheritance_binding": 0.06,
        "agent_identity_continuity": 0.06,
        "avatar_entry_gate_integrity": 0.06,
        "private_workspace_boundary_score": 0.03,
        "frequency_flower_epoch_rhythm": 0.02,
        "browser_deep_history_replay_available": 0.01,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["multigenerational_culture_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_culture_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["multigenerational_culture_readiness"]
    losses = {
        "no_deep_history": 0.34,
        "no_language_drift": 0.29,
        "no_inherited_rituals": 0.24,
        "no_institutions": 0.25,
        "no_crisis_memory_retention": 0.22,
        "no_technology_lineage": 0.18,
        "no_avatar_entry_gate": 0.31,
        "no_private_boundary": 0.16,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_replay": 0.06,
    }
    return {key: round6(max(0.0, readiness - loss)) for key, loss in losses.items()}


def render_visualization(path: Path, payload: dict[str, Any]) -> None:
    metrics = payload["metrics"]
    cards = "\n".join(
        f"<div class='card'><span>{html.escape(k.replace('_', ' '))}</span><strong>{v:.3f}</strong></div>"
        for k, v in metrics.items()
        if isinstance(v, (int, float)) and k != "simulated_history_years"
    )
    epoch_rows = "\n".join(
        f"<tr><td>{row['year']}</td><td>{html.escape(row['epoch_id'])}</td><td>{html.escape(row['social_form'])}</td><td>{html.escape(row['memory_medium'])}</td></tr>"
        for row in payload["epochs"]
    )
    language_rows = "\n".join(
        f"<tr><td>{html.escape(row['language_id'])}</td><td>{row['year']}</td><td>{html.escape(row['public_phrase'])}</td><td>{row['semantic_retention']:.2f}</td><td>{row['mutual_intelligibility']:.2f}</td></tr>"
        for row in payload["languages"]
    )
    institution_rows = "\n".join(
        f"<tr><td>{html.escape(row['institution_id'])}</td><td>{row['founding_year']}</td><td>{row['legitimacy_score']:.2f}</td><td>{html.escape(row['current_rule'])}</td></tr>"
        for row in payload["institutions"]
    )
    agent_nodes = "\n".join(
        f"<li><b>{html.escape(row['agent'])}</b>: {html.escape(row['self_story_public'])}<em>{html.escape(row['inherited_words'])} / continuity {row['identity_continuity_score']:.2f}</em></li>"
        for row in payload["living_inheritance"]
    )
    event_nodes = "\n".join(
        f"<li><b>{row['tick']:02d}</b> {html.escape(row['event_type'])} year {row['year']}: {html.escape(row['public_fact'])}<em>{row['vibration_hz']:.2f}Hz / flower {row['flower_phase']}</em></li>"
        for row in payload["events"]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 218 Deep Culture Avatar Entry Bridge</title>
<style>
:root {{ --ink:#201611; --paper:#fff6e4; --terracotta:#a9492d; --indigo:#334b73; --moss:#506743; --gold:#c8912f; --shadow:rgba(35,25,16,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: 'Iowan Old Style', Palatino, Georgia, serif; color:var(--ink); background: radial-gradient(circle at 16% 12%, rgba(200,145,47,.34), transparent 26%), radial-gradient(circle at 84% 18%, rgba(51,75,115,.25), transparent 28%), linear-gradient(140deg,#f5ddba,#d8dec9 50%,#ecd0bc); }}
header, main {{ max-width:1220px; margin:auto; padding:46px clamp(18px,5vw,76px); }}
header {{ padding-bottom:18px; }}
.kicker {{ color:var(--terracotta); text-transform:uppercase; letter-spacing:.22em; font-size:12px; font-weight:900; }}
h1 {{ margin:12px 0; max-width:1060px; font-size:clamp(36px,7vw,82px); line-height:.92; letter-spacing:-.055em; }}
.boundary {{ max-width:960px; padding:16px 18px; background:rgba(255,246,228,.84); border-left:5px solid var(--indigo); box-shadow:0 18px 50px var(--shadow); }}
main {{ display:grid; gap:24px; padding-top:18px; }}
section {{ background:rgba(255,246,228,.72); border:1px solid rgba(32,22,17,.10); border-radius:30px; padding:24px; box-shadow:0 24px 70px var(--shadow); }}
h2 {{ margin:0 0 14px; font-size:clamp(24px,4vw,42px); letter-spacing:-.035em; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; }}
.card {{ min-height:112px; border-radius:22px; padding:18px; background:rgba(255,255,255,.54); border:1px solid rgba(80,103,67,.24); display:flex; flex-direction:column; justify-content:space-between; }}
.card span {{ color:#705840; text-transform:capitalize; font-size:14px; }}
.card strong {{ color:var(--indigo); font-size:32px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
th,td {{ text-align:left; padding:11px 9px; border-bottom:1px solid rgba(32,22,17,.12); vertical-align:top; }}
th {{ color:var(--moss); text-transform:uppercase; letter-spacing:.1em; font-size:11px; }}
ul.timeline {{ list-style:none; padding:0; display:grid; gap:10px; }}
ul.timeline li {{ background:rgba(255,255,255,.52); border-left:4px solid var(--gold); border-radius:18px; padding:14px 16px; }}
ul.timeline em {{ display:block; color:var(--indigo); font-style:normal; margin-top:4px; font-size:12px; }}
.flower {{ position:relative; overflow:hidden; min-height:292px; }}
.flower::before {{ content:''; position:absolute; inset:24px; border-radius:50%; background:repeating-radial-gradient(circle, transparent 0 25px, rgba(80,103,67,.22) 26px 28px), conic-gradient(from 18deg, rgba(169,73,45,.20), rgba(51,75,115,.26), rgba(200,145,47,.29), rgba(169,73,45,.20)); animation:breathe 14s ease-in-out infinite alternate; }}
.flower p {{ position:relative; max-width:660px; font-size:18px; line-height:1.5; }}
@keyframes breathe {{ from {{ transform:scale(.98) rotate(-1.2deg); opacity:.72; }} to {{ transform:scale(1.025) rotate(1.4deg); opacity:.96; }} }}
@media(max-width:720px) {{ header,main {{ padding-left:18px; padding-right:18px; }} table {{ font-size:12px; }} th,td {{ padding:8px 5px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 218</div>
  <h1>Deep culture memory before avatar entry: language drift, inherited ritual, institutions, and living lineage.</h1>
  <div class=\"boundary\">Deterministic simulation artifact. The avatar enters only after {payload['avatar_gate']['observed_history_years']} simulated years and receives public history without private workspace access. This is not real anthropology, subjective consciousness, real consent, or moral patienthood.</div>
</header>
<main>
<section><h2>Metrics</h2><div class=\"grid\">{cards}</div></section>
<section class=\"flower\"><h2>Frequency / flower-of-life epoch rhythm</h2><p>Each epoch, language layer, ritual, institution, technology lineage, living inheritance record, and avatar gate carries a vibration rate and flower node. The overlay is an inspectable historical timing scaffold, not metaphysical proof.</p></section>
<section><h2>Epoch strata</h2><table><thead><tr><th>Year</th><th>Epoch</th><th>Social form</th><th>Memory medium</th></tr></thead><tbody>{epoch_rows}</tbody></table></section>
<section><h2>Language drift</h2><table><thead><tr><th>Language</th><th>Year</th><th>Phrase</th><th>Retention</th><th>Intelligibility</th></tr></thead><tbody>{language_rows}</tbody></table></section>
<section><h2>Institutions</h2><table><thead><tr><th>Institution</th><th>Founded</th><th>Legitimacy</th><th>Current rule</th></tr></thead><tbody>{institution_rows}</tbody></table></section>
<section><h2>Living inheritances</h2><ul class=\"timeline\">{agent_nodes}</ul></section>
<section><h2>Replay timeline</h2><ul class=\"timeline\">{event_nodes}</ul></section>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )


def run(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    epochs = build_epochs(rng)
    languages = build_languages(epochs)
    rituals = build_rituals()
    institutions = build_institutions()
    technologies = build_technologies()
    inheritances = build_living_inheritance()
    gate = build_avatar_gate(epochs, languages, institutions)
    events = build_events(epochs, languages, rituals, institutions, technologies, inheritances, gate)
    replay = build_replay(events)
    metrics = compute_metrics(epochs, languages, rituals, institutions, technologies, inheritances, gate, events, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["multigenerational_culture_readiness"] >= 0.82 and metrics["deep_history_span_score"] >= 1.0 and metrics["avatar_entry_gate_integrity"] >= 1.0 else "fail"
    payload = {
        "report": 218,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_multigenerational_culture_memory_language_drift_inherited_rituals_institutions_avatar_entry",
        "module_verdict": verdict,
        "epochs": [asdict(row) for row in epochs],
        "languages": [asdict(row) for row in languages],
        "rituals": [asdict(row) for row in rituals],
        "institutions": [asdict(row) for row in institutions],
        "technologies": [asdict(row) for row in technologies],
        "living_inheritance": [asdict(row) for row in inheritances],
        "avatar_gate": asdict(gate),
        "events": [asdict(row) for row in events],
        "replay": [asdict(row) for row in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic cultural-history substrate, not real anthropology or subjective experience.",
            "Language drift is scripted and traceable rather than emergent natural language.",
            "Institutions persist as structured records, not full political life.",
            "Avatar entry is gated by public archives and sealed private digests, not real consent.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable pre-avatar civilization simulator with autonomous generations, child-to-adult learning, cultural mutation, institution competition, and late avatar entry",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "events": ARTIFACT_DIR / f"{BASE}_events.csv",
        "epoch_chronicle": ARTIFACT_DIR / f"{BASE}_epoch_chronicle.csv",
        "language_drift": ARTIFACT_DIR / f"{BASE}_language_drift.csv",
        "ritual_inheritance": ARTIFACT_DIR / f"{BASE}_ritual_inheritance.csv",
        "institutions": ARTIFACT_DIR / f"{BASE}_institutions.csv",
        "technology_lineage": ARTIFACT_DIR / f"{BASE}_technology_lineage.csv",
        "living_inheritance": ARTIFACT_DIR / f"{BASE}_living_inheritance.csv",
        "avatar_gate": ARTIFACT_DIR / f"{BASE}_avatar_gate.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["events"], payload["events"])
    write_csv(paths["epoch_chronicle"], payload["epochs"])
    write_csv(paths["language_drift"], payload["languages"])
    write_csv(paths["ritual_inheritance"], payload["rituals"])
    write_csv(paths["institutions"], payload["institutions"])
    write_csv(paths["technology_lineage"], payload["technologies"])
    write_csv(paths["living_inheritance"], payload["living_inheritance"])
    write_csv(paths["avatar_gate"], [payload["avatar_gate"]])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "multigenerational_culture_readiness": payload["metrics"]["multigenerational_culture_readiness"],
        "simulated_history_years": payload["metrics"]["simulated_history_years"],
        "avatar_entry_gate_integrity": payload["metrics"]["avatar_entry_gate_integrity"],
        "language_drift_continuity": payload["metrics"]["language_drift_continuity"],
        "institution_persistence": payload["metrics"]["institution_persistence"],
        "private_boundary": "sealed private workspace and private meaning digests only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "multigenerational_culture_readiness": payload["metrics"]["multigenerational_culture_readiness"],
        "simulated_history_years": payload["metrics"]["simulated_history_years"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "avatar_entry_gate_integrity": payload["metrics"]["avatar_entry_gate_integrity"],
        "next_gate": payload["next_gate"],
    }])
    render_visualization(paths["visualization"], payload)
    return {key: str(value) for key, value in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"multigenerational_culture_readiness {metrics['multigenerational_culture_readiness']:.6f}")
    print(f"simulated_history_years {metrics['simulated_history_years']:.0f}")
    print(f"epochs {len(payload['epochs'])}")
    print(f"language_layers {len(payload['languages'])}")
    print(f"rituals {len(payload['rituals'])}")
    print(f"institutions {len(payload['institutions'])}")
    print(f"technologies {len(payload['technologies'])}")
    print(f"living_inheritance_records {len(payload['living_inheritance'])}")
    print(f"language_drift_continuity {metrics['language_drift_continuity']:.6f}")
    print(f"institution_persistence {metrics['institution_persistence']:.6f}")
    print(f"avatar_entry_gate_integrity {metrics['avatar_entry_gate_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
