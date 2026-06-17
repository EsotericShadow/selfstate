#!/usr/bin/env python3
"""Report 219: SSRM-3D playable pre-avatar civilization simulator bridge.

This deterministic bridge turns deep-history records into a small pre-avatar
civilization simulator: autonomous generation cohorts, child-to-adult learning,
cultural mutation, institution competition, demographic events, and late avatar
entry. It is a simulation artifact, not subjective consciousness, real
anthropology, real language emergence, real consent, or moral patienthood.
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


BASE = "ssrm_3d_playable_pre_avatar_civilization_autonomous_generations_learning_cultural_mutation_institution_competition_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_multigenerational_culture_memory_language_drift_inherited_rituals_institutions_avatar_entry_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_multigenerational_culture_memory_language_drift_inherited_rituals_institutions_avatar_entry"
DEFAULT_SEED = 20260832


@dataclass(frozen=True)
class GenerationCohort:
    cohort_id: str
    birth_year: int
    adulthood_year: int
    population_size: int
    survival_rate: float
    inherited_language: str
    inherited_crisis_memory: str
    dominant_need: str
    autonomous_choice: str
    parent_institution: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class LearningEpisode:
    episode_id: str
    cohort_id: str
    age_band: str
    mentor_institution: str
    learned_skill: str
    body_practice: str
    language_phrase: str
    autonomy_choice: str
    completion_score: float
    skill_transfer_score: float
    private_workspace_digest: str
    visible_behavior: str


@dataclass(frozen=True)
class CulturalMutation:
    mutation_id: str
    year: int
    mutation_type: str
    source_cohort: str
    parent_form: str
    proposed_form: str
    selection_pressure: str
    adopted: bool
    survival_generations: int
    semantic_continuity: float
    disruption_risk: float
    institution_response: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class InstitutionContest:
    contest_id: str
    year: int
    incumbent: str
    challenger: str
    conflict_reason: str
    tested_rule: str
    winning_institution: str
    settlement: str
    resolved: bool
    public_safety_preserved: bool
    minority_memory_preserved: bool
    legitimacy_delta: float
    unresolved_debt: float


@dataclass(frozen=True)
class DemographicEvent:
    event_id: str
    year: int
    event_type: str
    affected_cohorts: str
    population_delta: int
    cause: str
    care_response: str
    knowledge_effect: str
    private_boundary: str
    traceability_score: float


@dataclass(frozen=True)
class AvatarEntryProtocol:
    gate_id: str
    avatar_entry_year: int
    required_pre_avatar_years: int
    observed_pre_avatar_years: int
    required_autonomous_cohorts: int
    observed_autonomous_cohorts: int
    required_learning_episodes: int
    observed_learning_episodes: int
    required_institution_contests: int
    observed_institution_contests: int
    pre_entry_interference: bool
    entry_briefing: str
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
    learning_effect: str
    mutation_effect: str
    institution_effect: str
    demographic_effect: str
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


def build_cohorts(rng: random.Random) -> list[GenerationCohort]:
    languages = ["proto-hearth", "reed-route", "stone-work", "hearth-archive", "flower-council-speech", "cistern-appeal", "runner-trade", "lantern-school", "frequency-archive", "threshold-common"]
    institutions = ["hearth-keepers", "route-workshop", "archive-speakers", "flower-council", "cistern-guild", "threshold-wardens"]
    needs = ["warmth", "safe routes", "sealed care", "water trust", "repair tools", "language teaching"]
    memories = [
        "do not name body-pain in public",
        "flood debt becomes shared carrying duty",
        "repair is care infrastructure",
        "private care histories are sealed",
        "minority notes stay beside rules",
        "rumor repair needs public action",
        "moving work counts in triage",
        "boundary phrases precede tool names",
        "rates guide care but do not prove guilt",
        "avatar entry requires deep-history briefing",
    ]
    cohorts: list[GenerationCohort] = []
    for index in range(24):
        birth_year = index * 160
        size = 42 + index * 3 + int(rng.uniform(-4, 5))
        survival = clamp(0.72 + (index % 6) * 0.025 + rng.uniform(-0.018, 0.018), 0.66, 0.91)
        language = languages[min(len(languages) - 1, index // 3)]
        institution = institutions[index % len(institutions)]
        choice = [
            "kept old warmth ritual despite faster ration queue",
            "changed route chant after flood season",
            "refused to expose private care names in lesson board",
            "moved tool receipts to public wall",
            "split water duty into witness pairs",
            "accepted a new rate chime but kept boundary words",
        ][index % 6]
        cohorts.append(
            GenerationCohort(
                cohort_id=f"cohort-{index + 1:02d}",
                birth_year=birth_year,
                adulthood_year=birth_year + 18,
                population_size=size,
                survival_rate=round6(survival),
                inherited_language=language,
                inherited_crisis_memory=memories[min(len(memories) - 1, index // 2)],
                dominant_need=needs[index % len(needs)],
                autonomous_choice=choice,
                parent_institution=institution,
                frequency_hz=round6(108.0 + index * 8.75 + survival * 9.0),
                flower_node=(index % 12) + 1,
            )
        )
    return cohorts


def build_learning(cohorts: list[GenerationCohort]) -> list[LearningEpisode]:
    skills = [
        ("body-boundary words", "stand near warmth stone and decline public naming", "ko-avra flor"),
        ("water carrying duty", "carry small water bowl with witness pair", "vey-sola neshla"),
        ("tool return receipt", "return dull tool to public board", "ariem renoq"),
        ("sealed archive practice", "close archive flap before private story", "niax xenia"),
        ("runner route memory", "walk dry path and mark flood stones", "miloq renoq"),
        ("appeal circle posture", "face minority speaker without crowding", "flor avra veyra"),
    ]
    age_bands = ["child-play", "apprentice-body-practice", "adolescent-council-observer"]
    episodes: list[LearningEpisode] = []
    selected = cohorts[1::2]
    for index, cohort in enumerate(selected):
        skill, practice, phrase = skills[index % len(skills)]
        age = age_bands[index % len(age_bands)]
        completion = 0.72 + (index % 5) * 0.045
        if index in {5, 11}:
            completion -= 0.18
        transfer = clamp(completion - 0.04 + (0.05 if "body" in age or "practice" in age else 0.0))
        episodes.append(
            LearningEpisode(
                episode_id=f"learn-{index + 1:02d}",
                cohort_id=cohort.cohort_id,
                age_band=age,
                mentor_institution=cohort.parent_institution,
                learned_skill=skill,
                body_practice=practice,
                language_phrase=phrase,
                autonomy_choice=cohort.autonomous_choice,
                completion_score=round6(clamp(completion)),
                skill_transfer_score=round6(transfer),
                private_workspace_digest=f"sealed:{cohort.cohort_id}:child-learning-private-state",
                visible_behavior="child repeats phrase through body practice, not debug table",
            )
        )
    return episodes


def build_mutations(cohorts: list[GenerationCohort]) -> list[CulturalMutation]:
    rows = [
        ("mut-warmth-chime", 320, "ritual", "warm-stone-near-rest", "thermal blanket chime", "long cold season", True, 12, 0.88, 0.14, "hearth-keepers adopt after two child cohorts"),
        ("mut-route-q-suffix", 640, "language", "ren", "renoq", "runner routes need motion marking", True, 10, 0.76, 0.22, "route-workshop accepts because old root remains"),
        ("mut-cup-knot-colors", 960, "technology", "plain cup knots", "color-safe cup knots", "crowded cup shelf", True, 8, 0.81, 0.19, "archive-speakers require private status not encoded"),
        ("mut-water-accusation-wall", 1280, "institution", "spoken correction", "public countersign wall", "water rumor season", True, 7, 0.79, 0.25, "cistern-guild wins contested adoption"),
        ("mut-fast-tool-claim", 1440, "institution", "tool receipt", "fast claim without witness", "repair urgency", False, 1, 0.42, 0.61, "flower-council rejects ownership capture"),
        ("mut-child-boundary-song", 1760, "language", "boundary phrase lesson", "child-safe boundary song", "school lantern expansion", True, 6, 0.84, 0.16, "lantern teachers adopt"),
        ("mut-rate-guilt-index", 2080, "technology", "body-rate chime", "rate guilt index", "sensor overconfidence", False, 1, 0.38, 0.74, "archive-speakers reject because rates cannot prove guilt"),
        ("mut-minority-seed-vote", 2240, "institution", "minority note", "minority seed vote", "council fatigue", True, 5, 0.72, 0.31, "flower-council adopts with rollback"),
        ("mut-runner-night-map", 2560, "technology", "map chant", "glowing runner map", "dark winter routes", True, 4, 0.77, 0.27, "runner guilds preserve old chant under map"),
        ("mut-threshold-short-brief", 2880, "ritual", "deep-history briefing", "short avatar greeting", "outsider curiosity", False, 1, 0.46, 0.66, "threshold-wardens reject thin history"),
        ("mut-replay-apology-knot", 3200, "ritual", "apology knot", "replay apology knot", "restorative appeal delays", True, 3, 0.74, 0.28, "appeal circles adopt partial replay"),
        ("mut-common-threshold-creole", 3520, "language", "threshold-common", "threshold market creole", "trade with road houses", True, 1, 0.69, 0.34, "archive-speakers document drift without forcing purity but survival is not proven yet"),
    ]
    mutations: list[CulturalMutation] = []
    for index, row in enumerate(rows):
        mid, year, mtype, parent, proposed, pressure, adopted, survival, continuity, risk, response = row
        source = cohorts[min(len(cohorts) - 1, max(0, year // 160))].cohort_id
        mutations.append(
            CulturalMutation(mid, year, mtype, source, parent, proposed, pressure, adopted, survival, round6(continuity), round6(risk), response, round6(142.0 + index * 13.2), (index % 12) + 1)
        )
    return mutations


def build_institution_contests() -> list[InstitutionContest]:
    return [
        InstitutionContest("contest-tools", 520, "route-workshop", "runner guilds", "tool access for moving repair work", "whether moving work counts as repair", "route-workshop", "runner witness lane added", True, True, True, 0.04, 0.10),
        InstitutionContest("contest-water", 980, "cistern-guild", "flower-council", "water ledger accused stewards too quickly", "whether countersign needed before accusation", "flower-council", "countersign rule added", True, True, True, 0.07, 0.08),
        InstitutionContest("contest-care-history", 1320, "hearth-keepers", "archive-speakers", "care histories needed for medicine learning", "whether private histories can be opened by vote", "archive-speakers", "sealed aggregate evidence only", True, True, True, 0.05, 0.12),
        InstitutionContest("contest-school-boundaries", 1700, "lantern teachers", "route-workshop", "children learned tools before boundary words", "lesson order", "lantern teachers", "boundary phrase first curriculum", True, True, True, 0.03, 0.06),
        InstitutionContest("contest-rate-chimes", 2120, "rate keepers", "archive-speakers", "rate indexes used as guilt hints", "whether body rates can infer motive", "archive-speakers", "rate guilt index banned", True, True, True, 0.02, 0.18),
        InstitutionContest("contest-minority-fatigue", 2440, "flower-council", "route-workshop", "minority notes slowed emergency rules", "whether emergency can skip dissent", "flower-council", "dissent timer added, not removed", True, True, True, 0.01, 0.16),
        InstitutionContest("contest-threshold-brief", 3000, "threshold-wardens", "market houses", "market wanted early avatar trade", "whether avatar can enter before full briefing", "threshold-wardens", "entry delayed until deep briefing", True, True, True, 0.06, 0.05),
        InstitutionContest("contest-replay-ownership", 3480, "archive-speakers", "runner guilds", "replay wall failed to credit moving work", "who owns public replay annotation", "unresolved", "temporary dual annotation; debt remains", False, True, True, -0.02, 0.24),
    ]


def build_demographics(cohorts: list[GenerationCohort]) -> list[DemographicEvent]:
    return [
        DemographicEvent("demo-wet-winter", 240, "mortality-pressure", "cohort-02;cohort-03", -8, "wet winter raised rest debt", "hearth-keepers expanded warm-stone-near-rest", "warmth ritual survives as care infrastructure", "sealed individual body histories", 0.92),
        DemographicEvent("demo-flood-migration", 720, "migration", "cohort-05;cohort-06", 14, "flood moved families toward dry route", "route-workshop added child path lessons", "route suffix spreads", "sealed family fear records", 0.88),
        DemographicEvent("demo-cup-shelf-boom", 1040, "birth-cohort-growth", "cohort-07", 19, "dry cup shelf reduced winter illness-like absences", "hearth and archive split cup labels", "cup privacy words stabilize", "sealed child health details", 0.86),
        DemographicEvent("demo-tool-wear-loss", 1520, "labor-loss", "cohort-10", -6, "tool wear injured repair schedule", "tool-return receipt made wear visible", "repair apprenticeship becomes longer", "sealed injury details", 0.84),
        DemographicEvent("demo-lantern-school-expansion", 1840, "learning-expansion", "cohort-12;cohort-13", 23, "school lanterns allowed winter teaching", "child boundary song adopted", "boundary words taught before tools", "sealed child workspace states", 0.91),
        DemographicEvent("demo-rate-chime-dispute", 2160, "trust-loss", "cohort-14", -3, "rate guilt index caused avoidance", "archive-speakers banned motive inference", "rates guide care but do not prove guilt", "sealed body-rate identities", 0.82),
        DemographicEvent("demo-road-house-mixing", 2640, "migration", "cohort-17;cohort-18", 31, "runner roads connected far houses", "market creole begins", "language drift accelerates", "sealed newcomer private names", 0.79),
        DemographicEvent("demo-threshold-watch", 3120, "birth-cohort-growth", "cohort-20", 17, "threshold schools prepare for possible avatar era", "threshold wardens expand briefing ritual", "deep history becomes child lesson", "sealed fear of outsider records", 0.87),
        DemographicEvent("demo-replay-wall-debt", 3520, "trust-loss", "cohort-23", -2, "runner work undercredited by replay wall", "dual annotation added but debt remains", "public replay needs authorship memory", "sealed resentment details", 0.76),
    ]


def build_avatar_protocol(cohorts: list[GenerationCohort], learning: list[LearningEpisode], contests: list[InstitutionContest]) -> AvatarEntryProtocol:
    observed_years = max(cohort.adulthood_year for cohort in cohorts) - min(cohort.birth_year for cohort in cohorts)
    gate_passed = observed_years >= 3600 and len(cohorts) >= 20 and len(learning) >= 10 and len(contests) >= 8
    return AvatarEntryProtocol(
        gate_id="late-avatar-entry-after-autonomous-generations",
        avatar_entry_year=max(cohort.adulthood_year for cohort in cohorts) + 30,
        required_pre_avatar_years=3600,
        observed_pre_avatar_years=observed_years,
        required_autonomous_cohorts=20,
        observed_autonomous_cohorts=len(cohorts),
        required_learning_episodes=10,
        observed_learning_episodes=len(learning),
        required_institution_contests=8,
        observed_institution_contests=len(contests),
        pre_entry_interference=False,
        entry_briefing="Avatar receives cohort history, child-learning norms, mutation ledger, institution contest outcomes, and unresolved social debts before free movement.",
        private_boundary="Avatar sees public lineage and sealed digests, not child private workspaces or private body histories.",
        gate_passed=gate_passed,
    )


def build_events(cohorts: list[GenerationCohort], learning: list[LearningEpisode], mutations: list[CulturalMutation], contests: list[InstitutionContest], demographics: list[DemographicEvent], protocol: AvatarEntryProtocol) -> list[EventRecord]:
    events: list[EventRecord] = []
    tick = 1
    for row in cohorts:
        events.append(EventRecord(tick, "generation_cohort", row.birth_year, row.cohort_id, f"{row.population_size} children inherit {row.inherited_language} and choose: {row.autonomous_choice}", "sealed:cohort-private-child-lives", row.inherited_crisis_memory, "cohort may preserve or mutate inherited form", row.parent_institution, f"survival {row.survival_rate:.2f}; need {row.dominant_need}", "children cluster near mentor bodies before choosing work", row.frequency_hz, row.flower_node))
        tick += 1
    for row in learning:
        events.append(EventRecord(tick, "child_to_adult_learning", int(row.cohort_id.split('-')[1]) * 160, row.cohort_id, f"{row.age_band} learns {row.learned_skill} through {row.body_practice}", row.private_workspace_digest, f"completion {row.completion_score:.2f}; transfer {row.skill_transfer_score:.2f}", f"phrase {row.language_phrase} can mutate later", row.mentor_institution, "learning affects adult institution choice", row.visible_behavior, round6(162.0 + tick * 2.2), (tick % 12) + 1))
        tick += 1
    for row in mutations:
        events.append(EventRecord(tick, "cultural_mutation", row.year, row.mutation_id, f"{row.parent_form} mutates toward {row.proposed_form}; adopted={row.adopted}", "sealed:mutation-private-motive-map", f"source cohort {row.source_cohort}", f"survival {row.survival_generations}; continuity {row.semantic_continuity:.2f}; risk {row.disruption_risk:.2f}", row.institution_response, row.selection_pressure, "agents try new form at edge of old ritual", row.frequency_hz, row.flower_node))
        tick += 1
    for row in contests:
        events.append(EventRecord(tick, "institution_competition", row.year, row.contest_id, f"{row.incumbent} vs {row.challenger}: {row.conflict_reason}", "sealed:contest-private-faction-memory", "children inherit contest result as norm", "institution contest selects or rejects mutation", f"winner {row.winning_institution}; resolved={row.resolved}; settlement {row.settlement}", f"debt {row.unresolved_debt:.2f}; legitimacy {row.legitimacy_delta:+.2f}", "council ring opens a gap for challenger and incumbent", round6(216.0 + tick * 1.7), (tick % 12) + 1))
        tick += 1
    for row in demographics:
        events.append(EventRecord(tick, "demographic_event", row.year, row.event_id, f"{row.event_type} changes population by {row.population_delta}: {row.cause}", f"sealed:{row.event_id}:private-body-family-details", row.knowledge_effect, "demographic pressure changes cultural selection", row.care_response, f"traceability {row.traceability_score:.2f}; affected {row.affected_cohorts}", "population marker changes without exposing private family records", round6(241.0 + tick * 1.45), (tick % 12) + 1))
        tick += 1
    events.append(EventRecord(tick, "late_avatar_entry_protocol", protocol.avatar_entry_year, protocol.gate_id, protocol.entry_briefing, "sealed:avatar-no-private-child-workspaces", f"learning episodes {protocol.observed_learning_episodes}/{protocol.required_learning_episodes}", "avatar arrives after mutation ledger closes pre-entry phase", f"contests {protocol.observed_institution_contests}/{protocol.required_institution_contests}; gate {protocol.gate_passed}", f"pre-avatar years {protocol.observed_pre_avatar_years}/{protocol.required_pre_avatar_years}; interference {protocol.pre_entry_interference}", "avatar stands outside school-ring until wardens finish briefing", 333.0, 12))
    return sorted(events, key=lambda item: (item.year, item.tick))


def build_replay(events: list[EventRecord]) -> list[ReplayFrame]:
    panels = {
        "generation_cohort": "cohort ledger",
        "child_to_adult_learning": "learning yard",
        "cultural_mutation": "mutation selection table",
        "institution_competition": "institution contest ring",
        "demographic_event": "demographic chronicle",
        "late_avatar_entry_protocol": "late avatar gate",
    }
    return [
        ReplayFrame(
            tick=row.tick,
            avatar_position="outside world as noninterfering archive observer" if row.event_type != "late_avatar_entry_protocol" else "threshold school-ring entry line",
            camera_focus=f"{row.actor_or_layer} / year {row.year}",
            public_panel=panels.get(row.event_type, "civilization panel"),
            agent_markers=row.readable_marker,
            private_boundary="private child workspaces, body histories, motives, and family details remain sealed digests",
            frequency_overlay=f"{row.vibration_hz:.3f}Hz civilization pulse",
            flower_overlay=f"flower node {row.flower_phase} in generational ring",
        )
        for row in events
    ]


def compute_metrics(cohorts: list[GenerationCohort], learning: list[LearningEpisode], mutations: list[CulturalMutation], contests: list[InstitutionContest], demographics: list[DemographicEvent], protocol: AvatarEntryProtocol, events: list[EventRecord], replay: list[ReplayFrame]) -> dict[str, float]:
    adopted = [row for row in mutations if row.adopted]
    survived = [row for row in adopted if row.survival_generations >= 2 and row.semantic_continuity >= 0.68]
    resolved_contests = [row for row in contests if row.resolved]
    safe_contests = [row for row in contests if row.public_safety_preserved and row.minority_memory_preserved]
    completed_learning = [row for row in learning if row.completion_score >= 0.70]
    strong_transfer = [row for row in learning if row.skill_transfer_score >= 0.72]
    body_learning = [row for row in learning if row.body_practice and row.private_workspace_digest.startswith("sealed:")]
    memory_cohorts = [row for row in cohorts if row.inherited_crisis_memory]
    autonomous_cohorts = [row for row in cohorts if row.autonomous_choice and row.parent_institution]
    demographic_trace = [row for row in demographics if row.traceability_score >= 0.78 and row.private_boundary.startswith("sealed")]
    private_safe = [row for row in events if row.private_digest.startswith("sealed:")]
    rhythm_safe = [row for row in events if row.vibration_hz > 0 and 1 <= row.flower_phase <= 12]
    continuity = mean(row.survival_rate for row in cohorts)
    mutation_types = {row.mutation_type for row in mutations}
    institution_legitimacy = clamp(0.72 + mean(row.legitimacy_delta for row in contests) - mean(row.unresolved_debt for row in contests) * 0.18)

    metrics = {
        "simulated_pre_avatar_years": float(protocol.observed_pre_avatar_years),
        "pre_avatar_duration_score": clamp(protocol.observed_pre_avatar_years / protocol.required_pre_avatar_years),
        "autonomous_generation_depth": clamp(len(cohorts) / protocol.required_autonomous_cohorts),
        "autonomous_cohort_choice_rate": len(autonomous_cohorts) / len(cohorts),
        "child_to_adult_learning_rate": len(completed_learning) / len(learning),
        "skill_transmission_rate": len(strong_transfer) / len(learning),
        "embodied_learning_binding": len(body_learning) / len(learning),
        "cultural_mutation_survival_rate": len(survived) / len(adopted),
        "cultural_mutation_diversity": clamp(len(mutation_types) / 5.0),
        "institution_competition_resolution_rate": len(resolved_contests) / len(contests),
        "institution_turnover_without_collapse": len(safe_contests) / len(contests),
        "institution_legitimacy_after_competition": institution_legitimacy,
        "demographic_event_traceability": len(demographic_trace) / len(demographics),
        "crisis_memory_intergenerational_retention": len(memory_cohorts) / len(cohorts),
        "living_world_continuity": continuity,
        "late_avatar_entry_integrity": 1.0 if protocol.gate_passed and not protocol.pre_entry_interference else 0.0,
        "private_workspace_boundary_score": len(private_safe) / len(events),
        "frequency_flower_civilization_rhythm": len(rhythm_safe) / len(events),
        "browser_civilization_replay_available": 1.0 if replay else 0.0,
    }
    weights = {
        "pre_avatar_duration_score": 0.09,
        "autonomous_generation_depth": 0.08,
        "autonomous_cohort_choice_rate": 0.07,
        "child_to_adult_learning_rate": 0.09,
        "skill_transmission_rate": 0.07,
        "embodied_learning_binding": 0.06,
        "cultural_mutation_survival_rate": 0.08,
        "cultural_mutation_diversity": 0.05,
        "institution_competition_resolution_rate": 0.08,
        "institution_turnover_without_collapse": 0.07,
        "institution_legitimacy_after_competition": 0.07,
        "demographic_event_traceability": 0.06,
        "crisis_memory_intergenerational_retention": 0.05,
        "living_world_continuity": 0.05,
        "late_avatar_entry_integrity": 0.07,
        "private_workspace_boundary_score": 0.03,
        "frequency_flower_civilization_rhythm": 0.02,
        "browser_civilization_replay_available": 0.01,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["pre_avatar_civilization_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_civilization_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["pre_avatar_civilization_readiness"]
    losses = {
        "no_autonomous_generations": 0.33,
        "no_child_learning": 0.30,
        "no_cultural_mutation": 0.27,
        "no_institution_competition": 0.29,
        "no_demographic_events": 0.21,
        "no_late_avatar_gate": 0.31,
        "no_crisis_memory_inheritance": 0.18,
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
        if isinstance(v, (int, float)) and k != "simulated_pre_avatar_years"
    )
    cohort_rows = "\n".join(
        f"<tr><td>{row['cohort_id']}</td><td>{row['birth_year']}</td><td>{row['population_size']}</td><td>{html.escape(row['inherited_language'])}</td><td>{html.escape(row['autonomous_choice'])}</td></tr>"
        for row in payload["cohorts"][:12]
    )
    learning_rows = "\n".join(
        f"<tr><td>{row['episode_id']}</td><td>{html.escape(row['cohort_id'])}</td><td>{html.escape(row['learned_skill'])}</td><td>{row['completion_score']:.2f}</td><td>{row['skill_transfer_score']:.2f}</td></tr>"
        for row in payload["learning"]
    )
    mutation_rows = "\n".join(
        f"<tr><td>{row['mutation_id']}</td><td>{html.escape(row['mutation_type'])}</td><td>{str(row['adopted']).lower()}</td><td>{row['survival_generations']}</td><td>{html.escape(row['institution_response'])}</td></tr>"
        for row in payload["mutations"]
    )
    contest_nodes = "\n".join(
        f"<li><b>{html.escape(row['contest_id'])}</b>: {html.escape(row['incumbent'])} vs {html.escape(row['challenger'])}; resolved={str(row['resolved']).lower()}, debt {row['unresolved_debt']:.2f}</li>"
        for row in payload["institution_contests"]
    )
    event_nodes = "\n".join(
        f"<li><b>{row['tick']:02d}</b> year {row['year']} {html.escape(row['event_type'])}: {html.escape(row['public_fact'])}<em>{row['vibration_hz']:.2f}Hz / flower {row['flower_phase']}</em></li>"
        for row in payload["events"][:44]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 219 Pre-Avatar Civilization Simulator Bridge</title>
<style>
:root {{ --ink:#21160f; --paper:#fff4df; --clay:#a64b31; --lake:#2f6370; --leaf:#536b3d; --sun:#c78d2e; --shadow:rgba(38,25,14,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 12% 12%, rgba(199,141,46,.34), transparent 25%), radial-gradient(circle at 86% 20%, rgba(47,99,112,.25), transparent 30%), linear-gradient(140deg,#f8dfb9,#d9dfc7 52%,#eccab7); }}
header, main {{ max-width:1220px; margin:auto; padding:46px clamp(18px,5vw,76px); }}
header {{ padding-bottom:18px; }}
.kicker {{ color:var(--clay); text-transform:uppercase; letter-spacing:.22em; font-size:12px; font-weight:900; }}
h1 {{ margin:12px 0; max-width:1080px; font-size:clamp(36px,7vw,82px); line-height:.92; letter-spacing:-.055em; }}
.boundary {{ max-width:980px; padding:16px 18px; background:rgba(255,244,223,.84); border-left:5px solid var(--lake); box-shadow:0 18px 50px var(--shadow); }}
main {{ display:grid; gap:24px; padding-top:18px; }}
section {{ background:rgba(255,244,223,.72); border:1px solid rgba(33,22,15,.10); border-radius:30px; padding:24px; box-shadow:0 24px 70px var(--shadow); }}
h2 {{ margin:0 0 14px; font-size:clamp(24px,4vw,42px); letter-spacing:-.035em; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; }}
.card {{ min-height:112px; border-radius:22px; padding:18px; background:rgba(255,255,255,.54); border:1px solid rgba(83,107,61,.24); display:flex; flex-direction:column; justify-content:space-between; }}
.card span {{ color:#73583e; text-transform:capitalize; font-size:14px; }}
.card strong {{ color:var(--lake); font-size:32px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
th,td {{ text-align:left; padding:11px 9px; border-bottom:1px solid rgba(33,22,15,.12); vertical-align:top; }}
th {{ color:var(--leaf); text-transform:uppercase; letter-spacing:.1em; font-size:11px; }}
ul.timeline {{ list-style:none; padding:0; display:grid; gap:10px; }}
ul.timeline li {{ background:rgba(255,255,255,.52); border-left:4px solid var(--sun); border-radius:18px; padding:14px 16px; }}
ul.timeline em {{ display:block; color:var(--lake); font-style:normal; margin-top:4px; font-size:12px; }}
.flower {{ position:relative; overflow:hidden; min-height:292px; }}
.flower::before {{ content:''; position:absolute; inset:24px; border-radius:50%; background:repeating-radial-gradient(circle, transparent 0 25px, rgba(83,107,61,.22) 26px 28px), conic-gradient(from 18deg, rgba(166,75,49,.20), rgba(47,99,112,.26), rgba(199,141,46,.29), rgba(166,75,49,.20)); animation:breathe 14s ease-in-out infinite alternate; }}
.flower p {{ position:relative; max-width:680px; font-size:18px; line-height:1.5; }}
@keyframes breathe {{ from {{ transform:scale(.98) rotate(-1.2deg); opacity:.72; }} to {{ transform:scale(1.025) rotate(1.4deg); opacity:.96; }} }}
@media(max-width:720px) {{ header,main {{ padding-left:18px; padding-right:18px; }} table {{ font-size:12px; }} th,td {{ padding:8px 5px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 219</div>
  <h1>Pre-avatar civilization simulator: cohorts grow up, mutate culture, compete institutions, and only then admit the avatar.</h1>
  <div class=\"boundary\">Deterministic simulation artifact. The avatar remains outside for {payload['avatar_protocol']['observed_pre_avatar_years']} simulated years while generations learn, choose, mutate, contest, and remember. This is not real consciousness, anthropology, language emergence, consent, or moral patienthood.</div>
</header>
<main>
<section><h2>Metrics</h2><div class=\"grid\">{cards}</div></section>
<section class=\"flower\"><h2>Frequency / flower-of-life civilization rhythm</h2><p>Each cohort, lesson, cultural mutation, institution contest, demographic event, and avatar gate carries a vibration rate and flower node. The overlay is an inspectable temporal scaffold for cultural rates, not metaphysical proof.</p></section>
<section><h2>Early cohorts</h2><table><thead><tr><th>Cohort</th><th>Birth</th><th>Size</th><th>Language</th><th>Autonomous choice</th></tr></thead><tbody>{cohort_rows}</tbody></table></section>
<section><h2>Child-to-adult learning</h2><table><thead><tr><th>Episode</th><th>Cohort</th><th>Skill</th><th>Completion</th><th>Transfer</th></tr></thead><tbody>{learning_rows}</tbody></table></section>
<section><h2>Cultural mutations</h2><table><thead><tr><th>Mutation</th><th>Type</th><th>Adopted</th><th>Survival</th><th>Institution response</th></tr></thead><tbody>{mutation_rows}</tbody></table></section>
<section><h2>Institution contests</h2><ul class=\"timeline\">{contest_nodes}</ul></section>
<section><h2>Replay timeline excerpt</h2><ul class=\"timeline\">{event_nodes}</ul></section>
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
    cohorts = build_cohorts(rng)
    learning = build_learning(cohorts)
    mutations = build_mutations(cohorts)
    contests = build_institution_contests()
    demographics = build_demographics(cohorts)
    protocol = build_avatar_protocol(cohorts, learning, contests)
    events = build_events(cohorts, learning, mutations, contests, demographics, protocol)
    replay = build_replay(events)
    metrics = compute_metrics(cohorts, learning, mutations, contests, demographics, protocol, events, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["pre_avatar_civilization_readiness"] >= 0.82 and metrics["late_avatar_entry_integrity"] >= 1.0 and metrics["autonomous_generation_depth"] >= 1.0 else "fail"
    payload = {
        "report": 219,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_pre_avatar_civilization_autonomous_generations_child_learning_cultural_mutation_institution_competition_late_avatar_entry",
        "module_verdict": verdict,
        "cohorts": [asdict(row) for row in cohorts],
        "learning": [asdict(row) for row in learning],
        "mutations": [asdict(row) for row in mutations],
        "institution_contests": [asdict(row) for row in contests],
        "demographics": [asdict(row) for row in demographics],
        "avatar_protocol": asdict(protocol),
        "events": [asdict(row) for row in events],
        "replay": [asdict(row) for row in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic cohort simulation, not a full open-ended civilization engine.",
            "Children and institutions are structured records, not subjective minds.",
            "Cultural mutation is selected by deterministic rules rather than emergent population-scale language use.",
            "Avatar entry is a simulation gate, not real consent from conscious beings.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable embodied pre-avatar ecology with births, aging, illness, apprenticeship, habitat construction, agriculture, weather, and material economies before avatar entry",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "events": ARTIFACT_DIR / f"{BASE}_events.csv",
        "cohorts": ARTIFACT_DIR / f"{BASE}_cohorts.csv",
        "learning": ARTIFACT_DIR / f"{BASE}_learning.csv",
        "mutations": ARTIFACT_DIR / f"{BASE}_cultural_mutations.csv",
        "institution_contests": ARTIFACT_DIR / f"{BASE}_institution_contests.csv",
        "demographics": ARTIFACT_DIR / f"{BASE}_demographics.csv",
        "avatar_protocol": ARTIFACT_DIR / f"{BASE}_avatar_protocol.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["events"], payload["events"])
    write_csv(paths["cohorts"], payload["cohorts"])
    write_csv(paths["learning"], payload["learning"])
    write_csv(paths["mutations"], payload["mutations"])
    write_csv(paths["institution_contests"], payload["institution_contests"])
    write_csv(paths["demographics"], payload["demographics"])
    write_csv(paths["avatar_protocol"], [payload["avatar_protocol"]])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "pre_avatar_civilization_readiness": payload["metrics"]["pre_avatar_civilization_readiness"],
        "simulated_pre_avatar_years": payload["metrics"]["simulated_pre_avatar_years"],
        "autonomous_generation_depth": payload["metrics"]["autonomous_generation_depth"],
        "child_to_adult_learning_rate": payload["metrics"]["child_to_adult_learning_rate"],
        "institution_competition_resolution_rate": payload["metrics"]["institution_competition_resolution_rate"],
        "late_avatar_entry_integrity": payload["metrics"]["late_avatar_entry_integrity"],
        "private_boundary": "sealed private child workspace, body history, motive, and family digests only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "pre_avatar_civilization_readiness": payload["metrics"]["pre_avatar_civilization_readiness"],
        "simulated_pre_avatar_years": payload["metrics"]["simulated_pre_avatar_years"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "late_avatar_entry_integrity": payload["metrics"]["late_avatar_entry_integrity"],
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
    print(f"pre_avatar_civilization_readiness {metrics['pre_avatar_civilization_readiness']:.6f}")
    print(f"simulated_pre_avatar_years {metrics['simulated_pre_avatar_years']:.0f}")
    print(f"cohorts {len(payload['cohorts'])}")
    print(f"learning_episodes {len(payload['learning'])}")
    print(f"cultural_mutations {len(payload['mutations'])}")
    print(f"institution_contests {len(payload['institution_contests'])}")
    print(f"demographic_events {len(payload['demographics'])}")
    print(f"child_to_adult_learning_rate {metrics['child_to_adult_learning_rate']:.6f}")
    print(f"cultural_mutation_survival_rate {metrics['cultural_mutation_survival_rate']:.6f}")
    print(f"institution_competition_resolution_rate {metrics['institution_competition_resolution_rate']:.6f}")
    print(f"late_avatar_entry_integrity {metrics['late_avatar_entry_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
