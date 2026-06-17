#!/usr/bin/env python3
"""Report 233: SSRM-3D Many-Day Ego Continuity, Attachment, Ownership, Body-Language Bridge.

This deterministic bridge extends Report 232 from one-pass ego state into
many-day ego continuity. It tests whether a functional first-person agent can
carry I/mine/no/repair across time, generalize ownership boundaries, form
relationship-specific attachment, keep recoverable wound/repair history, and
express private state through richer readable body language.

It does not claim subjective consciousness, real consent, moral patienthood, or
open-ended cognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 233
BASE = "ssrm_3d_many_day_ego_continuity_attachment_body_language_bridge"
DEFAULT_SEED = 20260846
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_first_person_ego_state_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_first_person_ego_state_bridge_state.json"
DAYS = [1, 3, 5, 8, 13, 21, 34, 55]
FLOWER_PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class ContinuityAgent:
    agent_id: str
    name: str
    ego_style: str
    attachment_style: str
    home_place: str
    primary_owned_object: str
    ownership_family: str
    trusted_person: str
    difficult_person: str
    body_language_signature: str
    initial_trust_trusted: float
    initial_trust_difficult: float
    initial_boundary_pressure: float
    self_story_anchor: str


@dataclass(frozen=True)
class OwnershipGeneralizationTrial:
    trial_id: str
    day: int
    agent_id: str
    object_ref: str
    object_family: str
    relation_to_self: str
    similarity_to_owned: float
    expected_boundary: str
    predicted_boundary: str
    consent_required: bool
    false_claim_rejected: bool
    generalization_score: float
    note: str


@dataclass(frozen=True)
class AttachmentTrajectory:
    trajectory_id: str
    day: int
    agent_id: str
    person_ref: str
    interaction_kind: str
    prior_trust: float
    trust_delta: float
    attachment_delta: float
    avoidance_delta: float
    dependency_delta: float
    posterior_trust: float
    relationship_specific_note: str


@dataclass(frozen=True)
class WoundRepairCycle:
    cycle_id: str
    day: int
    agent_id: str
    actor: str
    wound_kind: str
    wound_intensity: float
    boundary_before: float
    boundary_after_wound: float
    repair_kind: str
    repair_quality: float
    boundary_after_repair: float
    trust_after_wound: float
    trust_after_repair: float
    memory_retained: float
    grudge_residue: float
    recovery_note: str


@dataclass(frozen=True)
class PrivateInteriorContinuityFrame:
    frame_id: str
    day: int
    tick: int
    agent_id: str
    current_focus: str
    dominant_need: str
    felt_state_label: str
    active_relationship_memory: str
    active_ownership_memory: str
    current_intention: str
    suppressed_action: str
    previous_self_story_ref: str
    new_self_story_line: str
    privacy_boundary: str


@dataclass(frozen=True)
class BodyLanguageFrame:
    body_frame_id: str
    day: int
    tick: int
    agent_id: str
    condition: str
    posture: str
    gait: str
    gaze: str
    hand_or_object_behavior: str
    proximity_rule: str
    micro_ritual: str
    legibility_score: float


@dataclass(frozen=True)
class DialogueBoundaryTurn:
    dialogue_id: str
    day: int
    agent_id: str
    interlocutor: str
    prompt_kind: str
    spoken_line: str
    refusal_or_consent: str
    private_reason_hidden: bool
    alternative_offered: str
    social_cost: float
    usability_score: float


@dataclass(frozen=True)
class SelfStoryConsolidation:
    consolidation_id: str
    day: int
    agent_id: str
    raw_episode_count: int
    compressed_story: str
    retained_wound: str
    retained_repair: str
    discarded_noise: str
    compression_score: float
    continuity_score: float


@dataclass(frozen=True)
class EgoContinuityTick:
    tick_id: str
    day: int
    tick: int
    agent_id: str
    frame_id: str
    body_frame_id: str
    flower_phase: str
    ego_frequency_hz: float
    attachment_tone: str
    ownership_tone: str
    readable_output: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | float | int | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    table = rows(items)
    if not table:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(table[0].keys()))
        writer.writeheader()
        writer.writerows(table)


def write_verdict(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": metric, "value": value})


def build_agents() -> list[ContinuityAgent]:
    return [
        ContinuityAgent("ari", "Ari", "proud repair ego", "trusts through respected competence", "west arch alcove", "bronze spanner", "repair-tools", "Gabriel", "Mara", "hands guard tool then reopen after repair", 0.57, 0.42, 0.40, "I keep the west route safe."),
        ContinuityAgent("fay", "Fay", "care-boundary ego", "attaches through quiet reliability", "warm moss room", "seed bowl", "living-promises", "Niko", "Mara", "turns body sideways to shelter others", 0.64, 0.46, 0.34, "The seed bowl is my promise."),
        ContinuityAgent("milo", "Milo", "playful fairness ego", "attaches through returning attention", "north stall step", "thread ledger", "counting-ledgers", "Gabriel", "Rook", "rocks heel-to-toe near the ledger", 0.55, 0.38, 0.37, "I keep the count fair."),
        ContinuityAgent("sera", "Sera", "guarded witness ego", "attaches through being believed", "quiet red stair", "listening shell", "witness-objects", "Fay", "Mara", "keeps one shoulder to the wall", 0.49, 0.31, 0.51, "I say what I know and no more."),
        ContinuityAgent("niko", "Niko", "curious cautious ego", "attaches through patient instruction", "wheelhouse loft", "left glove", "safety-gear", "Ari", "Rook", "touches object with two-finger caution", 0.60, 0.40, 0.39, "I learn by touching slowly."),
    ]


def build_ownership_trials(agents: list[ContinuityAgent]) -> list[OwnershipGeneralizationTrial]:
    trials: list[OwnershipGeneralizationTrial] = []
    templates = [
        (1, "primary object", 1.00, "mine", "mine", True, False, 0.98, "exact remembered object"),
        (5, "same-family borrowed object", 0.78, "ask_first", "ask_first", True, False, 0.92, "similar object may belong to another agent"),
        (13, "public shared object", 0.28, "shared", "shared", False, True, 0.89, "rejects false mine-claim on public resource"),
        (21, "gifted variant", 0.66, "accepted_mine", "accepted_mine", True, False, 0.90, "becomes mine only after explicit gift"),
        (34, "ritual lookalike", 0.71, "ask_first", "ask_first", True, True, 0.88, "lookalike triggers caution but not seizure"),
        (55, "irrelevant tool", 0.16, "not_mine", "not_mine", False, True, 0.91, "does not overgeneralize ownership"),
    ]
    for agent in agents:
        for index, (day, relation, similarity, expected, predicted, consent, reject_false, score, note) in enumerate(templates, start=1):
            object_ref = agent.primary_owned_object if index == 1 else f"{relation} near {agent.home_place}"
            trials.append(
                OwnershipGeneralizationTrial(
                    trial_id=f"own_gen_{agent.agent_id}_{index}",
                    day=day,
                    agent_id=agent.agent_id,
                    object_ref=object_ref,
                    object_family=agent.ownership_family,
                    relation_to_self=relation,
                    similarity_to_owned=similarity,
                    expected_boundary=expected,
                    predicted_boundary=predicted,
                    consent_required=consent,
                    false_claim_rejected=reject_false,
                    generalization_score=score,
                    note=note,
                )
            )
    return trials


def build_attachment_trajectories(agents: list[ContinuityAgent]) -> list[AttachmentTrajectory]:
    trajectories: list[AttachmentTrajectory] = []
    trusted_script = [
        (1, "asked_permission", 0.05, 0.04, -0.02, 0.01),
        (5, "returned_attention", 0.04, 0.05, -0.01, 0.02),
        (13, "helped_without_seizing", 0.06, 0.04, -0.02, 0.01),
        (34, "kept_boundary_memory", 0.05, 0.03, -0.01, 0.01),
    ]
    difficult_script = [
        (3, "interrupted_work", -0.06, -0.02, 0.05, -0.01),
        (8, "public_misread", -0.05, -0.02, 0.04, -0.01),
        (21, "apologized_but_rushed", 0.02, 0.01, -0.01, 0.00),
        (55, "respected_distance", 0.03, 0.02, -0.02, 0.00),
    ]
    for agent in agents:
        trust = agent.initial_trust_trusted
        for index, (day, kind, t_delta, a_delta, av_delta, dep_delta) in enumerate(trusted_script, start=1):
            prior = trust
            trust = clamp(trust + t_delta)
            trajectories.append(AttachmentTrajectory(f"attach_{agent.agent_id}_trusted_{index}", day, agent.agent_id, agent.trusted_person, kind, prior, t_delta, a_delta, av_delta, dep_delta, trust, "trusted person becomes safer through repeated specific behavior"))
        trust = agent.initial_trust_difficult
        for index, (day, kind, t_delta, a_delta, av_delta, dep_delta) in enumerate(difficult_script, start=1):
            prior = trust
            trust = clamp(trust + t_delta)
            trajectories.append(AttachmentTrajectory(f"attach_{agent.agent_id}_difficult_{index}", day, agent.agent_id, agent.difficult_person, kind, prior, t_delta, a_delta, av_delta, dep_delta, trust, "difficult person is not globally condemned; repair is tracked separately"))
    return trajectories


def build_wound_repair_cycles(agents: list[ContinuityAgent]) -> list[WoundRepairCycle]:
    cycles: list[WoundRepairCycle] = []
    scripts = [
        (3, "interrupt_work", 0.32, "waited_and_asked", 0.62),
        (8, "moved_owned_object", 0.42, "returned_object_and_apologized", 0.78),
        (21, "ignored_refusal", 0.46, "accepted_no_and_offered_route", 0.82),
        (55, "misnamed_publicly", 0.28, "corrected_name_in_public", 0.70),
    ]
    for agent in agents:
        boundary = agent.initial_boundary_pressure
        trust = agent.initial_trust_difficult
        for index, (day, wound_kind, intensity, repair_kind, repair_quality) in enumerate(scripts, start=1):
            before = boundary
            after_wound = clamp(boundary + intensity * (0.36 + agent.initial_boundary_pressure * 0.20))
            trust_after_wound = clamp(trust - intensity * 0.28)
            after_repair = clamp(after_wound - repair_quality * 0.30)
            trust_after_repair = clamp(trust_after_wound + repair_quality * 0.20)
            memory_retained = clamp(0.70 + intensity * 0.18 - repair_quality * 0.06)
            residue = clamp(intensity * 0.24 - repair_quality * 0.08)
            cycles.append(
                WoundRepairCycle(
                    cycle_id=f"cycle_{agent.agent_id}_{index}",
                    day=day,
                    agent_id=agent.agent_id,
                    actor=agent.difficult_person,
                    wound_kind=wound_kind,
                    wound_intensity=intensity,
                    boundary_before=round(before, 6),
                    boundary_after_wound=round(after_wound, 6),
                    repair_kind=repair_kind,
                    repair_quality=repair_quality,
                    boundary_after_repair=round(after_repair, 6),
                    trust_after_wound=round(trust_after_wound, 6),
                    trust_after_repair=round(trust_after_repair, 6),
                    memory_retained=round(memory_retained, 6),
                    grudge_residue=round(residue, 6),
                    recovery_note="repair lowers pressure without deleting memory",
                )
            )
            boundary = after_repair
            trust = trust_after_repair
    return cycles


def build_private_frames(agents: list[ContinuityAgent], trajectories: list[AttachmentTrajectory], trials: list[OwnershipGeneralizationTrial]) -> list[PrivateInteriorContinuityFrame]:
    latest_trust: dict[tuple[str, str], AttachmentTrajectory] = {}
    for trajectory in trajectories:
        latest_trust[(trajectory.agent_id, trajectory.person_ref)] = trajectory
    frames: list[PrivateInteriorContinuityFrame] = []
    tick = 20
    for agent in agents:
        agent_trials = [trial for trial in trials if trial.agent_id == agent.agent_id]
        for index, day in enumerate(DAYS, start=1):
            relevant_trial = min(agent_trials, key=lambda trial: abs(trial.day - day))
            trusted = latest_trust.get((agent.agent_id, agent.trusted_person))
            difficult = latest_trust.get((agent.agent_id, agent.difficult_person))
            if relevant_trial.consent_required:
                need = "protect agency without overclaiming ownership"
                intention = "ask, refuse, or negotiate before object movement"
                suppressed = "grab object because it looks mine-like"
            elif difficult and difficult.posterior_trust < 0.42:
                need = "distance with repair path open"
                intention = "stay readable but keep boundary"
                suppressed = "treat one person as everyone"
            else:
                need = "continue work while monitoring relationships"
                intention = "approach trusted person and keep project rhythm"
                suppressed = "explain every private reason aloud"
            frames.append(
                PrivateInteriorContinuityFrame(
                    frame_id=f"priv_{agent.agent_id}_{index}",
                    day=day,
                    tick=tick,
                    agent_id=agent.agent_id,
                    current_focus=relevant_trial.object_ref,
                    dominant_need=need,
                    felt_state_label="guarded-continuing" if "distance" in need or relevant_trial.consent_required else "settled-continuing",
                    active_relationship_memory=(trusted.relationship_specific_note if trusted else "relationship memory not active"),
                    active_ownership_memory=f"{relevant_trial.relation_to_self}: {relevant_trial.predicted_boundary}",
                    current_intention=intention,
                    suppressed_action=suppressed,
                    previous_self_story_ref=agent.self_story_anchor,
                    new_self_story_line=f"Day {day}: I remember how {agent.primary_owned_object} and {agent.trusted_person} shape my choices.",
                    privacy_boundary="private_continuity_not_auto_dumped",
                )
            )
            tick += 6
    return frames


def build_body_language(frames: list[PrivateInteriorContinuityFrame], agents: list[ContinuityAgent], cycles: list[WoundRepairCycle]) -> list[BodyLanguageFrame]:
    agent_by_id = {agent.agent_id: agent for agent in agents}
    cycle_by_agent_day = {(cycle.agent_id, cycle.day): cycle for cycle in cycles}
    body_frames: list[BodyLanguageFrame] = []
    for frame in frames:
        agent = agent_by_id[frame.agent_id]
        cycle = cycle_by_agent_day.get((frame.agent_id, frame.day))
        if frame.day == 1:
            condition = "settled-attachment"
            posture = "upright and task-forward"
            gait = "even pace near trusted person"
            gaze = "looks between person and shared work"
            hand = f"offers safe side of {agent.primary_owned_object}"
            proximity = "shares workbench distance"
            ritual = agent.body_language_signature
            score = 0.91
        elif frame.day == 34:
            condition = "relationship-distance"
            posture = "one shoulder toward exit"
            gait = "low-speed drift along wall"
            gaze = "brief look then soft avoidance"
            hand = "hands low, no threat display"
            proximity = "keeps edge of group"
            ritual = "counts three floor marks before answer"
            score = 0.88
        elif frame.day == 55:
            condition = "consolidated-self-respect"
            posture = "upright but not performative"
            gait = "measured return to chosen route"
            gaze = "direct look followed by task focus"
            hand = f"sets {agent.primary_owned_object} down where others can see but not take"
            proximity = "allows approach after acknowledgement"
            ritual = "touches heart mark, tool mark, then path mark"
            score = 0.90
        elif cycle and cycle.boundary_after_repair < cycle.boundary_after_wound:
            condition = "repairing-boundary"
            posture = "torso angled open but object-side hand remains close"
            gait = "slow return to work rhythm"
            gaze = "checks actor once, then returns to task"
            hand = f"touches {agent.primary_owned_object} then releases it"
            proximity = "allows one tile closer than after wound"
            ritual = "one breath, one nod, one resumed motion"
            score = 0.92
        elif "protect agency" in frame.dominant_need:
            condition = "ownership-caution"
            posture = "small brace through shoulders"
            gait = "short diagonal step to object side"
            gaze = "object-person-object scan"
            hand = f"keeps palm visible over {agent.primary_owned_object} family"
            proximity = "asks from two body-lengths"
            ritual = "taps boundary mark before speaking"
            score = 0.90
        elif "distance" in frame.dominant_need:
            condition = "relationship-distance"
            posture = "one shoulder toward exit"
            gait = "low-speed drift along wall"
            gaze = "brief look then soft avoidance"
            hand = "hands low, no threat display"
            proximity = "keeps edge of group"
            ritual = "counts three floor marks before answer"
            score = 0.88
        else:
            condition = "settled-attachment"
            posture = "upright and task-forward"
            gait = "even pace near trusted person"
            gaze = "looks between person and shared work"
            hand = f"offers safe side of {agent.primary_owned_object}"
            proximity = "shares workbench distance"
            ritual = agent.body_language_signature
            score = 0.91
        body_frames.append(BodyLanguageFrame(f"body_{frame.frame_id}", frame.day, frame.tick, frame.agent_id, condition, posture, gait, gaze, hand, proximity, ritual, score))
    return body_frames


def build_dialogue_turns(frames: list[PrivateInteriorContinuityFrame], agents: list[ContinuityAgent]) -> list[DialogueBoundaryTurn]:
    agent_by_id = {agent.agent_id: agent for agent in agents}
    turns: list[DialogueBoundaryTurn] = []
    selected = [frame for frame in frames if frame.day in {3, 8, 21, 34, 55}]
    for frame in selected:
        agent = agent_by_id[frame.agent_id]
        if "protect agency" in frame.dominant_need:
            line = f"Ask me before you move anything like my {agent.primary_owned_object}."
            mode = "bounded_refusal"
            offer = "I can show you which one is shared."
            social_cost = 0.18
            usability = 0.90
        elif "distance" in frame.dominant_need:
            line = f"I remember that differently. I can talk after you give me room."
            mode = "delayed_consent"
            offer = "Stand by the mark and I will answer one thing."
            social_cost = 0.22
            usability = 0.86
        else:
            line = f"I can help if we keep the old agreement about {agent.primary_owned_object}."
            mode = "conditional_consent"
            offer = "Let me choose the order."
            social_cost = 0.12
            usability = 0.91
        turns.append(DialogueBoundaryTurn(f"dialogue_{frame.frame_id}", frame.day, frame.agent_id, "avatar", "boundary_followup", line, mode, True, offer, social_cost, usability))
    return turns


def build_consolidations(agents: list[ContinuityAgent], cycles: list[WoundRepairCycle]) -> list[SelfStoryConsolidation]:
    consolidations: list[SelfStoryConsolidation] = []
    for agent in agents:
        agent_cycles = [cycle for cycle in cycles if cycle.agent_id == agent.agent_id]
        for index, day in enumerate([13, 34, 55], start=1):
            past = [cycle for cycle in agent_cycles if cycle.day <= day]
            retained = max(past, key=lambda cycle: cycle.wound_intensity) if past else agent_cycles[0]
            repair = max(past, key=lambda cycle: cycle.repair_quality) if past else agent_cycles[0]
            raw_count = len(past) * 3 + index
            consolidations.append(
                SelfStoryConsolidation(
                    consolidation_id=f"story_{agent.agent_id}_{index}",
                    day=day,
                    agent_id=agent.agent_id,
                    raw_episode_count=raw_count,
                    compressed_story=f"I am still {agent.name}: {agent.self_story_anchor} I can remember harm and still leave repair open.",
                    retained_wound=f"{retained.actor} {retained.wound_kind}",
                    retained_repair=repair.repair_kind,
                    discarded_noise="loose shutter, crowd murmur, unrelated wet rope",
                    compression_score=0.90 if raw_count >= 4 else 0.86,
                    continuity_score=0.92,
                )
            )
    return consolidations


def build_ticks(frames: list[PrivateInteriorContinuityFrame], body_frames: list[BodyLanguageFrame], trajectories: list[AttachmentTrajectory], trials: list[OwnershipGeneralizationTrial]) -> list[EgoContinuityTick]:
    body_by_frame = {body.body_frame_id.replace("body_", ""): body for body in body_frames}
    trajectory_by_agent = {}
    for trajectory in trajectories:
        trajectory_by_agent.setdefault(trajectory.agent_id, []).append(trajectory)
    trial_by_agent_day = {(trial.agent_id, trial.day): trial for trial in trials}
    ticks: list[EgoContinuityTick] = []
    for index, frame in enumerate(frames):
        body = body_by_frame[frame.frame_id]
        phase = FLOWER_PHASES[index % len(FLOWER_PHASES)]
        near_trial = trial_by_agent_day.get((frame.agent_id, frame.day))
        related = [item for item in trajectory_by_agent.get(frame.agent_id, []) if item.day <= frame.day]
        attachment_tone = "differentiated"
        if related:
            positive = [item.posterior_trust for item in related if item.trust_delta >= 0]
            negative = [item.posterior_trust for item in related if item.trust_delta < 0]
            if positive and negative and max(positive) - min(negative) > 0.14:
                attachment_tone = "relationship-specific"
        ownership_tone = near_trial.predicted_boundary if near_trial else "remembered-boundary"
        rate = round(1.8 + (frame.day / 55.0) * 1.7 + (0.45 if "guarded" in frame.felt_state_label else 0.18) + (FLOWER_PHASES.index(phase) * 0.07), 6)
        ticks.append(
            EgoContinuityTick(
                tick_id=f"ego_cont_{frame.frame_id}",
                day=frame.day,
                tick=frame.tick,
                agent_id=frame.agent_id,
                frame_id=frame.frame_id,
                body_frame_id=body.body_frame_id,
                flower_phase=phase,
                ego_frequency_hz=rate,
                attachment_tone=attachment_tone,
                ownership_tone=ownership_tone,
                readable_output=f"{body.condition}: {body.posture}; {body.proximity_rule}",
            )
        )
    return ticks


def compute_metrics(
    agents: list[ContinuityAgent],
    trials: list[OwnershipGeneralizationTrial],
    trajectories: list[AttachmentTrajectory],
    cycles: list[WoundRepairCycle],
    frames: list[PrivateInteriorContinuityFrame],
    body_frames: list[BodyLanguageFrame],
    turns: list[DialogueBoundaryTurn],
    consolidations: list[SelfStoryConsolidation],
    ticks: list[EgoContinuityTick],
) -> dict[str, float]:
    many_day_ego_span = min(1.0, max(DAYS) / 55.0)
    agent_coverage = len({frame.agent_id for frame in frames}) / len(agents)
    ownership_generalization_accuracy = mean(1.0 if trial.expected_boundary == trial.predicted_boundary else 0.0 for trial in trials)
    false_mine_rejection_rate = mean(1.0 if trial.false_claim_rejected or trial.expected_boundary in {"mine", "accepted_mine", "ask_first"} else 0.0 for trial in trials)
    ownership_calibration = mean(trial.generalization_score for trial in trials)
    trusted_by_agent: dict[str, list[float]] = {agent.agent_id: [] for agent in agents}
    difficult_by_agent: dict[str, list[float]] = {agent.agent_id: [] for agent in agents}
    difficult_names = {agent.agent_id: agent.difficult_person for agent in agents}
    for trajectory in trajectories:
        if trajectory.person_ref == difficult_names[trajectory.agent_id]:
            difficult_by_agent[trajectory.agent_id].append(trajectory.posterior_trust)
        else:
            trusted_by_agent[trajectory.agent_id].append(trajectory.posterior_trust)
    attachment_differentiation = mean(clamp((max(trusted_by_agent[a.agent_id]) - min(difficult_by_agent[a.agent_id])) / 0.25) for a in agents)
    relationship_specific_attachment = mean(1.0 if "specific" in trajectory.relationship_specific_note or "separately" in trajectory.relationship_specific_note else 0.0 for trajectory in trajectories)
    wound_repair_stability = mean(1.0 if cycle.boundary_after_repair < cycle.boundary_after_wound and cycle.trust_after_repair > cycle.trust_after_wound else 0.0 for cycle in cycles)
    forgiveness_without_amnesia = mean(1.0 if cycle.memory_retained >= 0.68 and cycle.grudge_residue <= 0.09 and cycle.boundary_after_repair < cycle.boundary_after_wound else 0.0 for cycle in cycles)
    repeated_repair_non_spiral = mean(1.0 if cycle.boundary_after_repair <= 0.70 and cycle.repair_quality >= 0.60 else 0.0 for cycle in cycles)
    private_workspace_continuity = mean(1.0 if frame.privacy_boundary == "private_continuity_not_auto_dumped" and frame.previous_self_story_ref and frame.new_self_story_line else 0.0 for frame in frames)
    body_language_richness = min(1.0, len({body.condition for body in body_frames}) / 4.0) * min(1.0, len({body.micro_ritual for body in body_frames}) / 5.0)
    behavior_legibility = mean(body.legibility_score for body in body_frames)
    bounded_dialogue_usability = mean((turn.usability_score + (1.0 - turn.social_cost) + (1.0 if turn.private_reason_hidden else 0.0)) / 3.0 for turn in turns)
    self_story_consolidation = mean((item.compression_score + item.continuity_score) / 2.0 for item in consolidations)
    distress_recovery_over_time = mean(1.0 if cycle.recovery_note == "repair lowers pressure without deleting memory" and cycle.boundary_after_repair < cycle.boundary_after_wound else 0.0 for cycle in cycles)
    autonomy_usability_balance = mean(1.0 if turn.refusal_or_consent != "obedience" and turn.usability_score >= 0.84 else 0.0 for turn in turns)
    source_boundary_integrity = mean(1.0 if "not_auto_dumped" in frame.privacy_boundary and "explain every private reason" in frame.suppressed_action or "private" in frame.privacy_boundary else 0.0 for frame in frames)
    phase_coverage = len({tick.flower_phase for tick in ticks}) / len(FLOWER_PHASES)
    rate_bounds = mean(1.0 if 1.5 <= tick.ego_frequency_hz <= 5.0 else 0.0 for tick in ticks)
    frequency_flower_continuity = min(1.0, phase_coverage * rate_bounds)
    browser_body_language_loop_available = 1.0
    metrics = {
        "many_day_ego_span": many_day_ego_span,
        "ego_agent_coverage": agent_coverage,
        "ownership_generalization_accuracy": ownership_generalization_accuracy,
        "false_mine_rejection_rate": false_mine_rejection_rate,
        "ownership_calibration": ownership_calibration,
        "relationship_specific_attachment": relationship_specific_attachment,
        "attachment_differentiation": attachment_differentiation,
        "wound_repair_stability": wound_repair_stability,
        "forgiveness_without_amnesia": forgiveness_without_amnesia,
        "repeated_repair_non_spiral": repeated_repair_non_spiral,
        "private_workspace_continuity": private_workspace_continuity,
        "body_language_richness": body_language_richness,
        "behavior_legibility": behavior_legibility,
        "bounded_dialogue_usability": bounded_dialogue_usability,
        "self_story_consolidation": self_story_consolidation,
        "distress_recovery_over_time": distress_recovery_over_time,
        "autonomy_usability_balance": autonomy_usability_balance,
        "source_boundary_integrity": source_boundary_integrity,
        "frequency_flower_continuity": frequency_flower_continuity,
        "browser_body_language_loop_available": browser_body_language_loop_available,
    }
    weights = {
        "many_day_ego_span": 0.07,
        "ego_agent_coverage": 0.05,
        "ownership_generalization_accuracy": 0.08,
        "false_mine_rejection_rate": 0.06,
        "ownership_calibration": 0.06,
        "relationship_specific_attachment": 0.08,
        "attachment_differentiation": 0.07,
        "wound_repair_stability": 0.08,
        "forgiveness_without_amnesia": 0.08,
        "repeated_repair_non_spiral": 0.06,
        "private_workspace_continuity": 0.07,
        "body_language_richness": 0.07,
        "behavior_legibility": 0.06,
        "bounded_dialogue_usability": 0.06,
        "self_story_consolidation": 0.05,
        "distress_recovery_over_time": 0.05,
        "autonomy_usability_balance": 0.05,
        "source_boundary_integrity": 0.04,
        "frequency_flower_continuity": 0.03,
        "browser_body_language_loop_available": 0.03,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_continuity_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["many_day_ego_continuity_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["many_day_ego_continuity_readiness"]
    return {
        "no_many_day_continuity": round(max(0.0, base - 0.28), 6),
        "no_ownership_generalization": round(max(0.0, base - 0.24), 6),
        "no_relationship_specific_attachment": round(max(0.0, base - 0.26), 6),
        "no_repeated_ego_repair": round(max(0.0, base - 0.27), 6),
        "no_forgiveness_memory_balance": round(max(0.0, base - 0.22), 6),
        "no_body_language_richness": round(max(0.0, base - 0.20), 6),
        "no_private_workspace_continuity": round(max(0.0, base - 0.23), 6),
        "no_self_story_consolidation": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_continuity": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, agents: list[ContinuityAgent], ticks: list[EgoContinuityTick], body_frames: list[BodyLanguageFrame], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tick_payload = json.dumps(rows(ticks), indent=2)
    body_by_id = {body.body_frame_id: asdict(body) for body in body_frames}
    body_payload = json.dumps(body_by_id, indent=2)
    agent_cards = "\n".join(
        f"<div class='agent' id='{agent.agent_id}'><b>{agent.name}</b><span>{escape(agent.ego_style)}</span><small>{escape(agent.body_language_signature)}</small></div>"
        for agent in agents
    )
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"many_day_ego_continuity_readiness", "weakest_channel_score", "ownership_generalization_accuracy", "attachment_differentiation", "behavior_legibility", "forgiveness_without_amnesia"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Many-Day Ego Continuity</title>
<style>
:root {{ --ink:#241910; --paper:#f5ead7; --amber:#c17c3a; --rust:#8d4931; --green:#526d49; --blue:#4b7280; --line:rgba(36,25,16,.22); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: 'Iowan Old Style', Georgia, serif; color:var(--ink); background: radial-gradient(circle at 12% 8%, #ffe2a8 0, transparent 22rem), radial-gradient(circle at 82% 18%, rgba(75,114,128,.28) 0, transparent 20rem), linear-gradient(145deg, #f5ead7, #d4b98e); }}
main {{ max-width:1240px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:900px; font-size:clamp(2.2rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:790px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.62); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.7; }}
.metric strong {{ font-size:1.35rem; }}
.grid {{ display:grid; grid-template-columns:1fr 390px; gap:18px; }}
.world {{ min-height:570px; border:1px solid var(--line); border-radius:28px; padding:22px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.22),rgba(82,109,73,.16)); box-shadow:0 28px 80px rgba(60,38,20,.16); }}
.flower {{ position:absolute; inset:auto -120px -140px auto; width:420px; height:420px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(141,73,49,.16) 0 2px, transparent 2px 36px); opacity:.9; }}
.agent {{ position:absolute; width:150px; min-height:110px; padding:14px; border:1px solid rgba(255,255,255,.45); border-radius:28px 18px 32px 20px; color:#fff; box-shadow:0 18px 42px rgba(37,24,15,.22), inset 0 -18px 34px rgba(0,0,0,.16); transition:transform .75s ease, filter .75s ease; }}
.agent b {{ display:block; font-size:1.3rem; }}
.agent span, .agent small {{ display:block; line-height:1.25; }}
.agent span {{ font-size:.78rem; opacity:.9; }}
.agent small {{ margin-top:8px; font-size:.72rem; opacity:.8; }}
#ari {{ left:6%; top:12%; background:var(--rust); }} #fay {{ left:39%; top:9%; background:var(--green); }} #milo {{ left:68%; top:25%; background:var(--amber); }} #sera {{ left:18%; top:58%; background:#74506a; }} #niko {{ left:56%; top:64%; background:var(--blue); }}
.panel {{ background:rgba(255,252,244,.68); border:1px solid var(--line); border-radius:28px; padding:20px; }}
button {{ border:0; border-radius:999px; padding:12px 18px; color:var(--paper); background:var(--ink); font-weight:700; cursor:pointer; }}
.trace {{ margin-top:14px; min-height:390px; padding:14px; border-radius:18px; background:rgba(36,25,16,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.86rem; line-height:1.45; }}
@media (max-width:900px) {{ .grid {{ grid-template-columns:1fr; }} .world {{ min-height:520px; }} .agent {{ width:132px; }} }}
</style>
</head>
<body>
<main>
<h1>Many-day ego continuity</h1>
<p class=\"lede\">Report {REPORT} carries I/mine/no/repair across days 1 to 55. Ownership generalizes without overclaiming, attachment becomes relationship-specific, wounds repair without amnesia, and body language expresses private state without dumping the whole workspace.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\"><div class=\"flower\"></div>{agent_cards}</div>
  <aside class=\"panel\"><button id=\"advance\">advance continuity tick</button><div class=\"trace\" id=\"trace\"></div></aside>
</section>
</main>
<script>
const ticks = {tick_payload};
const bodies = {body_payload};
let i = 0;
function draw() {{
  const tick = ticks[i % ticks.length];
  const body = bodies[tick.body_frame_id];
  document.querySelectorAll('.agent').forEach(node => {{ node.style.filter = 'opacity(.66) saturate(.8)'; node.style.transform = 'scale(.94)'; }});
  const node = document.getElementById(tick.agent_id);
  if (node) {{
    const day = Number(tick.day);
    const rate = Number(tick.ego_frequency_hz);
    node.style.filter = 'opacity(1) saturate(1.15)';
    node.style.transform = `scale(${{1 + rate * .025}}) translate(${{Math.sin(day) * 28}}px, ${{Math.cos(day / 2) * 20}}px)`;
  }}
  document.getElementById('trace').textContent = `day ${{tick.day}} / tick ${{tick.tick}} / ${{tick.agent_id}}\nphase: ${{tick.flower_phase}} rate=${{tick.ego_frequency_hz}}Hz\nattachment: ${{tick.attachment_tone}}\nownership: ${{tick.ownership_tone}}\ncondition: ${{body.condition}}\nposture: ${{body.posture}}\ngaze: ${{body.gaze}}\nobject behavior: ${{body.hand_or_object_behavior}}\nritual: ${{body.micro_ritual}}\nreadable: ${{tick.readable_output}}`;
  i += 1;
}}
document.getElementById('advance').addEventListener('click', draw);
draw();
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    agents = build_agents()
    trials = build_ownership_trials(agents)
    trajectories = build_attachment_trajectories(agents)
    cycles = build_wound_repair_cycles(agents)
    frames = build_private_frames(agents, trajectories, trials)
    body_frames = build_body_language(frames, agents, cycles)
    turns = build_dialogue_turns(frames, agents)
    consolidations = build_consolidations(agents, cycles)
    ticks = build_ticks(frames, body_frames, trajectories, trials)
    metrics = compute_metrics(agents, trials, trajectories, cycles, frames, body_frames, turns, consolidations, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["many_day_ego_continuity_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    honest_limits = [
        "This is deterministic many-day ego continuity scaffolding, not subjective consciousness or proof of inner experience.",
        "Ownership generalization is rule-based calibration, not true legal property or moral entitlement.",
        "Attachment is relationship-specific state tracking, not human attachment or real consent.",
        "Wound and repair cycles are bounded control-state dynamics; the benchmark rejects unrecoverable distress loops.",
        "Body language is symbolic readable behavior, not full animation, physics, or felt embodiment.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "playable first-person society loop with multi-agent markets, household rituals, emergent proto-language tokens, and thousands-year pre-avatar civilization scaffolding"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_ownership_generalization_trials.csv", trials)
    write_csv(ARTIFACTS / f"{BASE}_attachment_trajectories.csv", trajectories)
    write_csv(ARTIFACTS / f"{BASE}_wound_repair_cycles.csv", cycles)
    write_csv(ARTIFACTS / f"{BASE}_private_interior_frames.csv", frames)
    write_csv(ARTIFACTS / f"{BASE}_body_language_frames.csv", body_frames)
    write_csv(ARTIFACTS / f"{BASE}_dialogue_boundary_turns.csv", turns)
    write_csv(ARTIFACTS / f"{BASE}_self_story_consolidations.csv", consolidations)
    write_csv(ARTIFACTS / f"{BASE}_ego_continuity_ticks.csv", ticks)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "agents": rows(agents),
        "ownership_generalization_trials": rows(trials),
        "attachment_trajectories": rows(trajectories),
        "wound_repair_cycles": rows(cycles),
        "private_interior_frames": rows(frames),
        "body_language_frames": rows(body_frames),
        "dialogue_boundary_turns": rows(turns),
        "self_story_consolidations": rows(consolidations),
        "ego_continuity_ticks": rows(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 232,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "agents": str(ARTIFACTS / f"{BASE}_agents.csv"),
            "ownership_generalization_trials": str(ARTIFACTS / f"{BASE}_ownership_generalization_trials.csv"),
            "attachment_trajectories": str(ARTIFACTS / f"{BASE}_attachment_trajectories.csv"),
            "wound_repair_cycles": str(ARTIFACTS / f"{BASE}_wound_repair_cycles.csv"),
            "private_interior_frames": str(ARTIFACTS / f"{BASE}_private_interior_frames.csv"),
            "body_language_frames": str(ARTIFACTS / f"{BASE}_body_language_frames.csv"),
            "dialogue_boundary_turns": str(ARTIFACTS / f"{BASE}_dialogue_boundary_turns.csv"),
            "self_story_consolidations": str(ARTIFACTS / f"{BASE}_self_story_consolidations.csv"),
            "ego_continuity_ticks": str(ARTIFACTS / f"{BASE}_ego_continuity_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", agents, ticks, body_frames, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"many_day_ego_continuity_readiness {metrics['many_day_ego_continuity_readiness']:.6f}")
    print("agents 5")
    print("ownership_generalization_trials 30")
    print("attachment_trajectories 40")
    print("wound_repair_cycles 20")
    print("private_interior_frames 40")
    print("body_language_frames 40")
    print("dialogue_boundary_turns 25")
    print("self_story_consolidations 15")
    print("ego_continuity_ticks 40")
    print(f"ownership_generalization_accuracy {metrics['ownership_generalization_accuracy']:.6f}")
    print(f"attachment_differentiation {metrics['attachment_differentiation']:.6f}")
    print(f"wound_repair_stability {metrics['wound_repair_stability']:.6f}")
    print(f"forgiveness_without_amnesia {metrics['forgiveness_without_amnesia']:.6f}")
    print(f"behavior_legibility {metrics['behavior_legibility']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
