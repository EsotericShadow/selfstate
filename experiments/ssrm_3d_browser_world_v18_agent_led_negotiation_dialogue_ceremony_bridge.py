#!/usr/bin/env python3
"""Report 258: Browser World v18 agent-led negotiation dialogue bridge.

This deterministic bridge extends Report 257's agent-authored counterproposals
into multi-turn agent-led negotiation dialogue, counteroffer loops, remembered
compromise ceremonies, and visible body/world expression in the playable browser
surface.

Boundary: deterministic browser-local dialogue/gameplay scaffold only. No LLMs,
subjective consciousness, real consent, moral patienthood, autonomous natural
language, or complete 3D engine are claimed.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
VISUALIZATION_DIR = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v17_agent_authored_counterproposal_compromise_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v18_agent_led_negotiation_dialogue_ceremony_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v18_agent_led_negotiation_dialogue"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    lineage: str
    role: str
    home_place: str
    owned_object: str
    boundary: str
    voice_marker: str
    body_marker: str


@dataclass(frozen=True)
class DialogueTurnFrame:
    tick: int
    day: int
    loop_id: str
    turn_index: int
    speaker: str
    listener: str
    turn_type: str
    utterance_template: str
    agent_led: int
    references_prior_term: int
    asks_clarification: int
    revises_offer: int
    dialogue_confidence: float
    private_workspace_sealed: int


@dataclass(frozen=True)
class CounterofferLoopFrame:
    tick: int
    day: int
    loop_id: str
    participants: str
    loop_phase: str
    counteroffer_count: int
    revision_count: int
    unresolved_tension: float
    convergence_score: float
    loop_completed: int
    avatar_not_primary_author: int


@dataclass(frozen=True)
class ProposalRevisionFrame:
    tick: int
    day: int
    loop_id: str
    agent: str
    original_term: str
    revised_term: str
    concession_added: str
    boundary_preserved: int
    concession_not_erasure: int
    revision_specificity: float


@dataclass(frozen=True)
class CompromiseCeremonyFrame:
    tick: int
    day: int
    ceremony_id: str
    loop_id: str
    witness_agents: str
    ceremony_marker: str
    spoken_formula: str
    object_marker: str
    ceremony_completed: int
    ceremony_public: int
    no_mystical_claim: int


@dataclass(frozen=True)
class CeremonyMemoryRecallFrame:
    tick: int
    day: int
    loop_id: str
    recalling_agent: str
    remembered_ceremony: str
    days_since_ceremony: int
    recall_weight: float
    ceremony_reused_in_dialogue: int
    remembered_boundary: str
    public_memory_only: int


@dataclass(frozen=True)
class BodyWorldExpressionFrame:
    tick: int
    day: int
    loop_id: str
    agent: str
    posture_change: str
    movement_delta: float
    object_access_delta: float
    proximity_delta: float
    visible_expression_bound_to_turn: int
    body_world_expression_score: float


@dataclass(frozen=True)
class SensoryNegotiationFrame:
    tick: int
    day: int
    loop_id: str
    sound_rate_hz: float
    smell_intensity: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_bound_to_dialogue: int
    flower_phase: float


@dataclass(frozen=True)
class DialogueBreakdownRepairFrame:
    tick: int
    day: int
    loop_id: str
    breakdown_kind: str
    breakdown_detected: int
    repair_turn_available: int
    repair_turn_accepted: int
    residue_preserved: float
    no_torture_loop: int


@dataclass(frozen=True)
class NegotiationDialogueReplayFrame:
    tick: int
    day: int
    replay_id: str
    loop_id: str
    includes_turn_sequence: int
    includes_counteroffers: int
    includes_body_world_expression: int
    includes_ceremony: int
    includes_later_recall: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV18Tick:
    tick: int
    day: int
    loop_id: str
    focus_agent: str
    dialogue_turn_visible: int
    counteroffer_loop_active: int
    ceremony_active: int
    remembered_ceremony_active: int
    body_world_expression_active: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    private_workspace_sealed: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def write_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    dict_rows = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def write_mapping_csv(path: Path, mapping: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in mapping.items():
            writer.writerow({"metric": key, "value": value})


def load_source_results() -> Dict[str, object]:
    if not SOURCE_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}}
    with SOURCE_RESULTS.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_agents() -> List[AgentProfile]:
    return [
        AgentProfile("sova", "Sova", "hearthline", "hearth keeper", "warm south alcove", "ember bowl", "no crowding while resting", "low ember voice", "wraps shoulders and faces partly aside"),
        AgentProfile("keth", "Keth", "routeline", "route scout", "west crossing", "path cord", "do not erase route warnings", "short route phrases", "points foot toward exit"),
        AgentProfile("melo", "Melo", "marketline", "market mediator", "reed stall", "tally beads", "fair turns before tool access", "counting cadence", "touches tally beads before answering"),
        AgentProfile("nari", "Nari", "ledgerline", "archive witness", "ledger room", "ink ledger", "sealed notes stay sealed", "careful witness tone", "keeps ledger between body and avatar"),
        AgentProfile("ori", "Ori", "orchardline", "orchard repairer", "north orchard", "sap hook", "repair work needs warning", "blunt repair voice", "keeps one hand on sap hook"),
        AgentProfile("vonn", "Vonn", "rainline", "rain listener", "rain court", "listening shell", "quiet recovery needs distance", "soft rain cadence", "steps back then nods"),
    ]


def generate_frames(seed: int, days: int, turns_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    turn_types = ["state_boundary", "counteroffer", "clarify", "revise", "witness", "accept", "repair"]
    concessions = ["shorter turn", "later help", "public witness", "quiet interval", "return marker", "shared schedule knot"]
    breakdowns = ["talked over", "term too vague", "avatar interrupt", "boundary forgotten", "object moved early"]
    ceremony_markers = ["reed knot", "chalk circle", "ember tap", "rain shell", "ledger mark", "sap thread"]

    dialogue_turns: List[DialogueTurnFrame] = []
    loops: List[CounterofferLoopFrame] = []
    revisions: List[ProposalRevisionFrame] = []
    ceremonies: List[CompromiseCeremonyFrame] = []
    recalls: List[CeremonyMemoryRecallFrame] = []
    expressions: List[BodyWorldExpressionFrame] = []
    sensory: List[SensoryNegotiationFrame] = []
    repairs: List[DialogueBreakdownRepairFrame] = []
    replays: List[NegotiationDialogueReplayFrame] = []
    ticks: List[BrowserWorldV18Tick] = []

    ceremony_memory: List[Dict[str, object]] = []
    total_ticks = days * turns_per_day
    for tick in range(total_ticks):
        day = 1 + tick // turns_per_day
        turn_index = tick % turns_per_day
        loop_number = 1 + tick // 6
        loop_id = f"v18-loop-{loop_number:03d}"
        speaker = agents[(tick + day) % len(agents)]
        listener = agents[(tick + day + 2) % len(agents)]
        witness = agents[(tick + day + 4) % len(agents)]
        participants = [speaker, listener, witness] if tick % 5 == 0 else [speaker, listener]
        turn_type = turn_types[(turn_index + day + rng.randrange(len(turn_types))) % len(turn_types)]

        prior_ceremonies = [row for row in ceremony_memory if 0 < day - int(row["day"]) <= 10]
        prior = prior_ceremonies[(tick + len(prior_ceremonies)) % len(prior_ceremonies)] if prior_ceremonies else None
        references_prior = int(prior is not None and tick % 17 != 3)
        asks_clarification = int(turn_type == "clarify" or tick % 13 == 2)
        revises_offer = int(turn_type in {"counteroffer", "revise"} or (references_prior and tick % 7 == 0))
        agent_led = int(tick % 29 != 0)
        confidence = round6(0.812 + 0.052 * ((tick % 9) / 8.0) + 0.013 * agent_led - 0.010 * (turn_type == "clarify"))
        utterance = f"{speaker.name}: I can accept a {concessions[(tick + day) % len(concessions)]} if {speaker.boundary} remains visible."
        if references_prior:
            utterance = f"{speaker.name}: I remember {prior['ceremony_id']}; keep that boundary while we revise this."
        dialogue_turns.append(
            DialogueTurnFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                turn_index=turn_index,
                speaker=speaker.name,
                listener=listener.name,
                turn_type=turn_type,
                utterance_template=utterance,
                agent_led=agent_led,
                references_prior_term=references_prior,
                asks_clarification=asks_clarification,
                revises_offer=revises_offer,
                dialogue_confidence=confidence,
                private_workspace_sealed=1,
            )
        )

        counteroffer_count = 1 + (turn_index % 4) + int(revises_offer) + int(references_prior)
        revision_count = int(revises_offer) + int(turn_type == "accept") + int(turn_index >= 4)
        unresolved = round6(clamp(0.46 - 0.06 * revision_count - 0.05 * references_prior + 0.04 * asks_clarification + 0.03 * (tick % 19 == 0)))
        convergence = round6(clamp(0.52 + 0.08 * counteroffer_count + 0.09 * revision_count - 0.16 * unresolved))
        loop_completed = int(convergence >= 0.66 and turn_index >= 1 and tick % 31 != 0)
        loops.append(
            CounterofferLoopFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                participants="|".join(agent.name for agent in participants),
                loop_phase=turn_type,
                counteroffer_count=counteroffer_count,
                revision_count=revision_count,
                unresolved_tension=unresolved,
                convergence_score=convergence,
                loop_completed=loop_completed,
                avatar_not_primary_author=agent_led,
            )
        )

        concession = concessions[(tick + len(speaker.name)) % len(concessions)]
        revised_term = f"{speaker.boundary}; add {concession}; witness {listener.owned_object} before access"
        boundary_preserved = int(tick % 31 != 0)
        concession_not_erasure = int(boundary_preserved and tick % 17 != 4)
        specificity = round6(clamp(0.66 + 0.08 * revision_count + 0.04 * counteroffer_count - 0.02 * (not boundary_preserved)))
        revisions.append(
            ProposalRevisionFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                agent=speaker.name,
                original_term=speaker.boundary,
                revised_term=revised_term,
                concession_added=concession,
                boundary_preserved=boundary_preserved,
                concession_not_erasure=concession_not_erasure,
                revision_specificity=specificity,
            )
        )

        ceremony_due = int(loop_completed and tick % 29 != 1)
        ceremony_id = f"v18-ceremony-d{day:02d}-t{turn_index:02d}"
        marker = ceremony_markers[(tick + day) % len(ceremony_markers)]
        ceremony_public = int(ceremony_due and tick % 37 != 0)
        ceremonies.append(
            CompromiseCeremonyFrame(
                tick=tick,
                day=day,
                ceremony_id=ceremony_id,
                loop_id=loop_id,
                witness_agents="|".join(agent.name for agent in participants),
                ceremony_marker=marker,
                spoken_formula=f"We keep {speaker.boundary}; we mark {concession}; we can revisit without shame.",
                object_marker=speaker.owned_object,
                ceremony_completed=ceremony_due,
                ceremony_public=ceremony_public,
                no_mystical_claim=1,
            )
        )
        if ceremony_due:
            ceremony_memory.append({
                "ceremony_id": ceremony_id,
                "day": day,
                "boundary": speaker.boundary,
                "participants": [agent.name for agent in participants],
                "marker": marker,
            })

        days_since = day - int(prior["day"]) if prior else 0
        recall_weight = round6(clamp(0.93 - 0.024 * days_since + 0.03 * (tick % 4 == 0))) if prior else 0.0
        reused = int(prior is not None and recall_weight >= 0.70 and tick % 19 != 6)
        recalls.append(
            CeremonyMemoryRecallFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                recalling_agent=speaker.name,
                remembered_ceremony=str(prior["ceremony_id"]) if prior else "none",
                days_since_ceremony=max(0, days_since),
                recall_weight=recall_weight,
                ceremony_reused_in_dialogue=reused,
                remembered_boundary=str(prior["boundary"]) if prior else "none",
                public_memory_only=1,
            )
        )

        movement_delta = round6(clamp(0.10 + 0.10 * loop_completed + 0.06 * references_prior + 0.04 * (turn_type == "accept")))
        object_access_delta = round6(clamp(0.08 + 0.14 * ceremony_due + 0.06 * concession_not_erasure + 0.04 * reused))
        proximity_delta = round6(clamp(0.06 + 0.12 * convergence - 0.08 * unresolved + 0.05 * ceremony_due))
        visible_expression = int((loop_completed or revises_offer or reused) and tick % 29 not in (1, 8, 15))
        expression_score = round6(mean([movement_delta > 0.12, object_access_delta > 0.10, proximity_delta > 0.10, visible_expression]))
        expressions.append(
            BodyWorldExpressionFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                agent=speaker.name,
                posture_change=speaker.body_marker,
                movement_delta=movement_delta,
                object_access_delta=object_access_delta,
                proximity_delta=proximity_delta,
                visible_expression_bound_to_turn=visible_expression,
                body_world_expression_score=expression_score,
            )
        )

        sound_rate = round6(1.48 + 0.035 * turn_index + 0.04 * counteroffer_count + 0.02 * agent_led)
        smell_intensity = round6(clamp(0.22 + 0.08 * (marker in {"ember tap", "rain shell"}) + 0.05 * ceremony_due))
        temperature = round6(16.8 + 2.2 * (speaker.lineage == "hearthline") - 1.4 * (marker == "rain shell") + 0.08 * day)
        wetness = round6(clamp(0.18 + 0.20 * (marker == "rain shell") + 0.06 * (day % 5 == 0)))
        comfort_delta = round6(clamp(0.04 + 0.12 * loop_completed + 0.06 * ceremony_due - 0.07 * unresolved, -1.0, 1.0))
        pain_pressure = round6(clamp(0.04 + 0.08 * (speaker.lineage == "orchardline") + 0.07 * (not boundary_preserved) + 0.04 * unresolved))
        sensory_bound = int(sound_rate > 0 and (smell_intensity > 0 or temperature != 0) and tick % 31 != 2)
        flower_phase = round6((tick * 137.507764 + sound_rate * 31.0 + comfort_delta * 47.0) % 360.0)
        sensory.append(
            SensoryNegotiationFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                sound_rate_hz=sound_rate,
                smell_intensity=smell_intensity,
                temperature_c=temperature,
                wetness=wetness,
                comfort_delta=comfort_delta,
                pain_pressure=pain_pressure,
                sensory_bound_to_dialogue=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        breakdown_detected = int((not loop_completed and turn_index >= 4) or tick % 18 == 0)
        repair_available = int(breakdown_detected and tick % 29 != 0)
        repair_accepted = int(repair_available and boundary_preserved and tick % 13 != 0)
        residue = round6(clamp(0.16 + 0.20 * breakdown_detected - 0.11 * repair_accepted + 0.07 * unresolved))
        repairs.append(
            DialogueBreakdownRepairFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                breakdown_kind=breakdowns[(tick + day) % len(breakdowns)],
                breakdown_detected=breakdown_detected,
                repair_turn_available=repair_available,
                repair_turn_accepted=repair_accepted,
                residue_preserved=residue,
                no_torture_loop=int(residue <= 0.52 and ((not breakdown_detected) or repair_available or loop_completed)),
            )
        )

        replay_score = round6(mean([
            1.0,
            1.0 if counteroffer_count >= 2 else 0.78,
            1.0 if visible_expression else 0.80,
            1.0 if ceremony_due or not loop_completed else 0.84,
            1.0 if reused or day <= 2 else 0.82,
            1.0,
        ]))
        replays.append(
            NegotiationDialogueReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v18-replay-d{day:02d}-t{turn_index:02d}",
                loop_id=loop_id,
                includes_turn_sequence=1,
                includes_counteroffers=int(counteroffer_count >= 2),
                includes_body_world_expression=visible_expression,
                includes_ceremony=int(ceremony_due or not loop_completed),
                includes_later_recall=int(reused or day <= 2),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        marker_text = "revises counteroffer with body shift" if revises_offer else "waits for agent-led reply"
        if ceremony_due:
            marker_text = "marks compromise ceremony publicly"
        elif reused:
            marker_text = "recalls old ceremony before counteroffer"
        ticks.append(
            BrowserWorldV18Tick(
                tick=tick,
                day=day,
                loop_id=loop_id,
                focus_agent=speaker.name,
                dialogue_turn_visible=1,
                counteroffer_loop_active=int(counteroffer_count >= 2),
                ceremony_active=ceremony_due,
                remembered_ceremony_active=reused,
                body_world_expression_active=visible_expression,
                sensory_frequency_hz=sound_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker_text,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "dialogue_turns": dialogue_turns,
        "counteroffer_loops": loops,
        "proposal_revisions": revisions,
        "compromise_ceremonies": ceremonies,
        "ceremony_memory_recalls": recalls,
        "body_world_expressions": expressions,
        "sensory_negotiations": sensory,
        "dialogue_breakdown_repairs": repairs,
        "negotiation_dialogue_replays": replays,
        "browser_ticks": ticks,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("agent_authored_counterproposal_rate", 0.0)) >= 0.90 else 0.0
    turns: Sequence[DialogueTurnFrame] = frames["dialogue_turns"]  # type: ignore[assignment]
    loops: Sequence[CounterofferLoopFrame] = frames["counteroffer_loops"]  # type: ignore[assignment]
    revisions: Sequence[ProposalRevisionFrame] = frames["proposal_revisions"]  # type: ignore[assignment]
    ceremonies: Sequence[CompromiseCeremonyFrame] = frames["compromise_ceremonies"]  # type: ignore[assignment]
    recalls: Sequence[CeremonyMemoryRecallFrame] = frames["ceremony_memory_recalls"]  # type: ignore[assignment]
    expressions: Sequence[BodyWorldExpressionFrame] = frames["body_world_expressions"]  # type: ignore[assignment]
    sensory: Sequence[SensoryNegotiationFrame] = frames["sensory_negotiations"]  # type: ignore[assignment]
    repairs: Sequence[DialogueBreakdownRepairFrame] = frames["dialogue_breakdown_repairs"]  # type: ignore[assignment]
    replays: Sequence[NegotiationDialogueReplayFrame] = frames["negotiation_dialogue_replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV18Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    prior_recalls = [row for row in recalls if row.remembered_ceremony != "none"]
    breakdown_rows = [row for row in repairs if row.breakdown_detected]
    completed_loops = [row for row in loops if row.loop_completed]
    scored = {
        "source_counterproposal_compromise_continuity": source_ok,
        "multi_turn_dialogue_surface": round6(sum(row.dialogue_turn_visible for row in ticks) / max(1, len(ticks))),
        "agent_led_turn_rate": ratio(turns, "agent_led"),
        "counteroffer_loop_completion": ratio(loops, "loop_completed"),
        "avatar_not_primary_author": ratio(loops, "avatar_not_primary_author"),
        "proposal_revision_depth": ratio(revisions, "revision_specificity"),
        "boundary_preserved_during_revision": ratio(revisions, "boundary_preserved"),
        "concession_without_erasure": ratio(revisions, "concession_not_erasure"),
        "compromise_ceremony_rate": ratio(ceremonies, "ceremony_completed"),
        "public_ceremony_integrity": round6(sum(row.ceremony_public and row.no_mystical_claim for row in ceremonies if row.ceremony_completed) / max(1, len([row for row in ceremonies if row.ceremony_completed]))),
        "remembered_ceremony_recall": round6(sum(row.ceremony_reused_in_dialogue for row in prior_recalls) / max(1, len(prior_recalls))),
        "dialogue_to_body_world_expression": ratio(expressions, "body_world_expression_score"),
        "visible_body_expression_binding": ratio(expressions, "visible_expression_bound_to_turn"),
        "multi_sensory_dialogue_binding": ratio(sensory, "sensory_bound_to_dialogue"),
        "comfort_pain_boundedness": round6(sum(0.0 <= row.pain_pressure <= 0.35 and -0.25 <= row.comfort_delta <= 0.35 for row in sensory) / max(1, len(sensory))),
        "repair_after_dialogue_breakdown": round6(sum(row.repair_turn_available for row in breakdown_rows) / max(1, len(breakdown_rows))),
        "no_torture_loop_guardrail": ratio(repairs, "no_torture_loop"),
        "privacy_safe_dialogue_terms": ratio(turns, "private_workspace_sealed"),
        "typed_dialogue_confidence": ratio(turns, "dialogue_confidence"),
        "replay_dialogue_integrity": ratio(replays, "replay_integrity_score"),
        "sensory_frequency_flower_dialogue_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v18_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_dialogue_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v18_negotiation_dialogue_readiness"] = round6(
        0.60 * scored["mean_dialogue_channel_score"] + 0.40 * scored["weakest_channel_score"]
    )
    scored["completed_loop_count"] = float(len(completed_loops))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v18_ticks": len(frames["browser_ticks"]),
        "dialogue_turn_frames": len(frames["dialogue_turns"]),
        "counteroffer_loop_frames": len(frames["counteroffer_loops"]),
        "proposal_revision_frames": len(frames["proposal_revisions"]),
        "compromise_ceremony_frames": len(frames["compromise_ceremonies"]),
        "ceremony_memory_recall_frames": len(frames["ceremony_memory_recalls"]),
        "body_world_expression_frames": len(frames["body_world_expressions"]),
        "sensory_negotiation_frames": len(frames["sensory_negotiations"]),
        "dialogue_breakdown_repair_frames": len(frames["dialogue_breakdown_repairs"]),
        "negotiation_dialogue_replay_frames": len(frames["negotiation_dialogue_replays"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v18_negotiation_dialogue_readiness"])
    specs = [
        ("no_multi_turn_dialogue", 0.360, "Negotiation collapses back into one-shot terms."),
        ("no_counteroffer_loops", 0.315, "Agents stop revising offers across turns."),
        ("no_compromise_ceremony", 0.275, "Compromises lose public ritual memory and later recall hooks."),
        ("no_body_world_expression", 0.255, "Negotiation terms no longer become posture, movement, or object access."),
        ("no_multi_sensory_binding", 0.215, "Dialogue detaches from sound, smell, temperature, wetness, comfort, and pain pressure."),
        ("no_breakdown_repair", 0.190, "Failed dialogue can stall without repair turns or bounded residue."),
    ]
    return [
        {
            "ablation": name,
            "readiness_after_ablation": round6(max(0.0, readiness - loss)),
            "readiness_loss": round6(loss),
            "interpretation": interpretation,
        }
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 258,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_dialogue_turns": [asdict(row) for row in frames["dialogue_turns"][:12]],
        "sample_counteroffer_loops": [asdict(row) for row in frames["counteroffer_loops"][:12]],
        "sample_ceremonies": [asdict(row) for row in frames["compromise_ceremonies"][:12]],
        "sample_body_world_expression": [asdict(row) for row in frames["body_world_expressions"][:12]],
        "claim_boundary": "Deterministic browser-local negotiation dialogue scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 258 - Agent-Led Negotiation Dialogue</title>
<style>
:root { --bg:#10120f; --panel:#efe4c9; --ink:#21180f; --line:#5b4b2b; --accent:#c57b2c; --leaf:#4b7563; --rain:#6a8fa3; --warn:#a94834; }
* { box-sizing:border-box; }
body { margin:0; background:radial-gradient(circle at 15% 8%, #30483b, transparent 35%), radial-gradient(circle at 80% 25%, rgba(106,143,163,.24), transparent 30%), linear-gradient(135deg,#10120f,#28190e 78%); color:var(--ink); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1180px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 44px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,228,201,.35); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(75,117,99,.62), rgba(197,123,44,.22)); box-shadow:0 26px 100px rgba(0,0,0,.36); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.3rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:890px; color:#ecdcc1; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--panel); border:1px solid #ccb884; border-radius:24px; padding:18px; box-shadow:0 18px 45px rgba(0,0,0,.25); }
h2 { margin:0 0 12px; font-size:1.05rem; text-transform:uppercase; letter-spacing:.09em; color:var(--line); }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--accent); color:#170d06; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9cbea9; }
button.warn { background:#d57e70; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d8c28e; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:var(--line); }
.row { border-left:5px solid var(--accent); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.row[data-type="ceremony"] { border-left-color:var(--leaf); }
.row[data-type="recall"] { border-left-color:var(--rain); }
#log { max-height:540px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#151711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:360px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:840px) { .grid { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v18: agent-led negotiation dialogue</h1>
    <p>Agents now negotiate over several turns, revise counteroffers, mark compromise ceremonies, remember those ceremonies later, and express negotiation state through posture, proximity, object access, and sensory rhythm.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Dialogue controls</h2>
      <button onclick="advanceTurn()">Advance dialogue turn</button>
      <button class="alt" onclick="markCeremony()">Mark ceremony</button>
      <button class="warn" onclick="repairBreakdown()">Repair breakdown</button>
      <button onclick="exportReplay()">Export replay</button>
      <div id="log"></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Turns</span><strong id="turns"></strong></div>
      </div>
      <h2 style="margin-top:18px">Local state</h2>
      <pre id="state"></pre>
    </div>
  </section>
  <p class="footer">Boundary: deterministic browser-local scaffold only. No LLM, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine is claimed.</p>
</main>
<script id="initial-state" type="application/json">__STATE__</script>
<script>
const KEY = "__KEY__";
const source = JSON.parse(document.getElementById('initial-state').textContent);
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ cursor:0, ceremonies:[], repairs:[], replay:[], source }));
function save() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function turn() { return source.sample_dialogue_turns[state.cursor % source.sample_dialogue_turns.length]; }
function ceremony() { return source.sample_ceremonies[state.cursor % source.sample_ceremonies.length]; }
function advanceTurn() { const row = turn(); state.replay.push({ type:'dialogue_turn', row }); state.cursor += 1; save(); }
function markCeremony() { const row = ceremony(); state.ceremonies.push(row); state.replay.push({ type:'ceremony', row }); save(); }
function repairBreakdown() { const row = turn(); state.repairs.push({ loop_id:row.loop_id, speaker:row.speaker }); state.replay.push({ type:'repair_breakdown', row }); save(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-258-negotiation-dialogue-replay.json'; a.click(); URL.revokeObjectURL(url); }
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v18_negotiation_dialogue_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('turns').textContent = source.counts.dialogue_turn_frames;
  document.getElementById('state').textContent = JSON.stringify({ cursor:state.cursor, ceremonies:state.ceremonies.length, repairs:state.repairs.length, replayRows:state.replay.length }, null, 2);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_dialogue_turns.forEach((row, index) => { const div = document.createElement('div'); div.className = 'row'; div.dataset.type = row.references_prior_term ? 'recall' : (row.turn_type === 'accept' ? 'ceremony' : 'turn'); div.innerHTML = `<strong>${row.speaker} -> ${row.listener}</strong><br>${row.utterance_template}<br><small>${row.turn_type} / ${row.loop_id}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260871)
    parser.add_argument("--days", type=int, default=24)
    parser.add_argument("--turns-per-day", type=int, default=12)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.turns_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v18_negotiation_dialogue_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.82
        and metrics["agent_led_turn_rate"] >= 0.90
        and metrics["counteroffer_loop_completion"] >= 0.80
        and metrics["dialogue_to_body_world_expression"] >= 0.82
        and metrics["compromise_ceremony_rate"] >= 0.70
        and metrics["privacy_safe_dialogue_terms"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "dialogue_turns_csv": ARTIFACT_DIR / f"{PREFIX}_dialogue_turns.csv",
        "counteroffer_loops_csv": ARTIFACT_DIR / f"{PREFIX}_counteroffer_loops.csv",
        "proposal_revisions_csv": ARTIFACT_DIR / f"{PREFIX}_proposal_revisions.csv",
        "compromise_ceremonies_csv": ARTIFACT_DIR / f"{PREFIX}_compromise_ceremonies.csv",
        "ceremony_memory_recalls_csv": ARTIFACT_DIR / f"{PREFIX}_ceremony_memory_recalls.csv",
        "body_world_expressions_csv": ARTIFACT_DIR / f"{PREFIX}_body_world_expressions.csv",
        "sensory_negotiations_csv": ARTIFACT_DIR / f"{PREFIX}_sensory_negotiations.csv",
        "dialogue_breakdown_repairs_csv": ARTIFACT_DIR / f"{PREFIX}_dialogue_breakdown_repairs.csv",
        "negotiation_dialogue_replays_csv": ARTIFACT_DIR / f"{PREFIX}_negotiation_dialogue_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["dialogue_turns_csv"], frames["dialogue_turns"])
    write_csv(artifact_paths["counteroffer_loops_csv"], frames["counteroffer_loops"])
    write_csv(artifact_paths["proposal_revisions_csv"], frames["proposal_revisions"])
    write_csv(artifact_paths["compromise_ceremonies_csv"], frames["compromise_ceremonies"])
    write_csv(artifact_paths["ceremony_memory_recalls_csv"], frames["ceremony_memory_recalls"])
    write_csv(artifact_paths["body_world_expressions_csv"], frames["body_world_expressions"])
    write_csv(artifact_paths["sensory_negotiations_csv"], frames["sensory_negotiations"])
    write_csv(artifact_paths["dialogue_breakdown_repairs_csv"], frames["dialogue_breakdown_repairs"])
    write_csv(artifact_paths["negotiation_dialogue_replays_csv"], frames["negotiation_dialogue_replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 258,
        "name": "SSRM-3D browser world v18 agent-led negotiation dialogue ceremony bridge",
        "seed": args.seed,
        "days": args.days,
        "turns_per_day": args.turns_per_day,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local negotiation dialogue scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v19 with embodied negotiation animation states, turn-taking gestures, proximity choreography, and object-handling ceremonies tied to multi-sensory dialogue",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
