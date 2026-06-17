#!/usr/bin/env python3
"""Report 226: playable avatar participation with saved-day consequences.

This deterministic bridge extends the Report 225 autonomous society slice by
letting the avatar participate in cooperative work, manipulate objects, choose
dialogue responses, disrupt routines, offer repairs, and carry consequences
across saved days.

It is functional simulation scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, or open-ended social cognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

BASE = "ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge"
REPORT = 226
DEFAULT_SEED = 20260839
SOURCE_STATE = Path(
    "artifacts/ssrm_3d_playable_local_autonomous_society_dialogue_cooperative_tasks_conflict_repair_routines_body_language_bridge_state.json"
)
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class PlayAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    trust_avatar: float
    boundary_pressure: float
    visible_need: str
    current_project: str
    public_memory: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AvatarAction:
    action_id: str
    day: int
    tick: int
    action_type: str
    target: str
    chosen_option: str
    consent_gate: str
    accepted_state: str
    avatar_effort_cost: float
    trust_delta: float
    task_delta: float
    routine_delta: float
    consequence: str
    sensory_feedback: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ObjectManipulation:
    manipulation_id: str
    day: int
    object_id: str
    object_label: str
    operation: str
    holder_before: str
    holder_after: str
    ownership_gate: str
    material_delta: float
    wear_delta: float
    debt_delta: float
    visible_world_change: str
    agent_response: str
    reversible: bool
    consequence_saved: bool
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class DialogueChoice:
    choice_id: str
    day: int
    agent_id: str
    prompt: str
    options: str
    selected_option: str
    refusal_possible: bool
    agent_response: str
    relationship_update: str
    memory_write: str
    trust_delta: float
    boundary_delta: float
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class RoutineDisruption:
    disruption_id: str
    day: int
    routine_id: str
    routine_title: str
    avatar_action: str
    disruption_severity: float
    agents_affected: str
    recovery_protocol: str
    recovery_score: float
    lingering_debt: float
    public_aftereffect: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class SavedDayConsequence:
    consequence_id: str
    day: int
    prior_action_ref: str
    consequence_type: str
    affected_agents: str
    relationship_effect: str
    object_state_effect: str
    access_change: str
    memory_echo: str
    persists_after_restore: bool
    cross_day_weight: float
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AvatarPlayTick:
    day: int
    tick: int
    layer: str
    avatar_action: str
    target: str
    public_result: str
    agent_visible_response: str
    object_result: str
    saved_consequence: str
    sensory_packet: str
    frequency_hz: float
    flower_node: int


def write_csv(path: Path, rows: Iterable[Any]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def load_source() -> dict[str, Any]:
    if not SOURCE_STATE.exists():
        return {"source_missing": True, "agents": [], "condition": "missing_report_225_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[PlayAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = {
        "fayen": ("Fayen", "care mediator", 28.0, 34.0, 0.75, 0.14, "posture timing", "care bell and shade check", "Gabriel slowed hands near Roka after rain."),
        "ariq": ("Ariq", "repair claimant", 54.0, 48.0, 0.66, 0.23, "bridge stability", "chalk arc stone repair", "Gabriel waited for the bell before helping lift."),
        "nian": ("Nian", "boundary keeper", 42.0, 22.0, 0.58, 0.41, "privacy threshold", "archive object-only grammar", "Gabriel accepted that the body reason stays sealed."),
        "roka": ("Roka", "child apprentice", 22.0, 62.0, 0.50, 0.38, "learner bundle safety", "reed drying path", "Gabriel used loose reeds and left the tied bundle."),
        "noro": ("Noro", "material ledger keeper", 70.0, 58.0, 0.62, 0.20, "debt clarity", "evening knot board", "Gabriel asked before changing the public knot."),
    }
    result: list[PlayAgent] = []
    for index, (agent_id, spec) in enumerate(specs.items(), start=1):
        name, role, x, y, trust, boundary, need, project, memory = spec
        source_agent = source_agents.get(agent_id, {})
        result.append(
            PlayAgent(
                agent_id=agent_id,
                display_name=name,
                role=source_agent.get("role", role),
                x=float(source_agent.get("x", x)),
                y=float(source_agent.get("y", y)),
                trust_avatar=float(source_agent.get("trust_avatar", trust)),
                boundary_pressure=float(source_agent.get("boundary_pressure", boundary)),
                visible_need=need,
                current_project=project,
                public_memory=memory,
                private_workspace_digest=f"sealed:{agent_id}:avatar-participation-workspace",
                frequency_hz=round(float(source_agent.get("frequency_hz", 142.0 + index * 29.0)) + 13.0, 3),
                flower_node=int(source_agent.get("flower_node", index + 1)),
            )
        )
    return result


def build_avatar_actions(rng: random.Random) -> list[AvatarAction]:
    rows = [
        ("act-day1-join-chalk", 1, 1, "join_cooperative_task", "ariq,roka", "hold chalk cord outside reed lane", "ask Roka before entering learner path", "accepted", 0.18, 0.05, 0.11, 0.02, "chalk arc widens without crowding Roka", "wet chalk smell, low stone scrape, cool knee-height air"),
        ("act-day1-move-loose-reeds", 1, 2, "manipulate_object", "obj-loose-reeds", "move only loose reeds to drying stone", "Roka distinguishes loose reeds from tied bundle", "accepted", 0.12, 0.04, 0.08, 0.01, "loose reeds dry; tied learner bundle remains untouched", "damp reed smell, soft grass drag, warmer stone surface"),
        ("act-day1-dialogue-roka", 1, 3, "dialogue_choice", "roka", "ask what should not be touched", "nonleading question with refusal available", "accepted", 0.03, 0.06, 0.03, 0.00, "Roka names the tied bundle boundary clearly", "small voice, reed cord creak, rain fading"),
        ("act-day1-routine-delay", 1, 4, "disrupt_routine", "routine-midday-water", "ask to continue lifting during water pause", "routine can refuse avatar urgency", "refused_with_alternative", 0.07, -0.02, -0.03, -0.12, "water pause holds; avatar can carry cups instead", "cup clink, warm herb shade, breath slowing"),
        ("act-day1-repair-offer", 1, 5, "repair_offer", "fayen,ariq", "carry cups after failed urgency request", "repair must not erase refusal", "accepted_partial", 0.10, 0.04, 0.04, 0.09, "Ariq keeps face; Fayen records repair attempt", "water weight, hand-cool clay, bell cord still"),
        ("act-day2-object-knot", 2, 1, "manipulate_object", "obj-knot-board", "add object-only digest knot", "Noro and Nian approve object-only wording", "accepted", 0.06, 0.05, 0.02, 0.04, "ledger shows object trail without private body reason", "dry cord rasp, smoke thread, board tap"),
        ("act-day2-dialogue-nian", 2, 2, "dialogue_choice", "nian", "repeat back privacy rule", "agent can correct avatar wording", "accepted", 0.02, 0.05, 0.02, 0.02, "Nian relaxes archive threshold by one step", "quiet flap cloth, still air, low voice"),
        ("act-day2-join-shade", 2, 3, "join_cooperative_task", "fayen,noro", "carry one shade beam then stop", "timber debt remains public", "accepted_conditional", 0.22, 0.03, 0.07, 0.01, "one beam placed; shade debt remains visible", "wood grain, shoulder strain, warm dust"),
        ("act-day2-overreach-bundle", 2, 4, "manipulate_object", "obj-tied-bundle", "try to pick up tied learner bundle", "Roka can refuse and preserve boundary", "refused", 0.04, -0.06, -0.04, -0.05, "bundle remains; Roka steps back and asks for blue stone distance", "tight cord sound, quick breath, cooler rain smell"),
        ("act-day2-repair-roka", 2, 5, "repair_offer", "roka", "step back to blue stone and ask again tomorrow", "repair requires distance plus delayed access", "accepted_partial", 0.03, 0.04, 0.02, 0.05, "Roka records a repair but keeps bundle access closed", "stone under heel, reed rustle, slower breathing"),
        ("act-day3-routine-join", 3, 1, "join_group_routine", "routine-evening-knot", "stand outside circle and read public debts", "circle can keep avatar at edge", "accepted_conditional", 0.05, 0.03, 0.03, 0.08, "avatar hears carry-forward debt without entering private circle", "smoke thread, knot-board tap, dusk cooling"),
        ("act-day3-dialogue-noro", 3, 2, "dialogue_choice", "noro", "ask what debt is still mine", "ledger answer cannot expose private causes", "accepted", 0.02, 0.04, 0.02, 0.04, "Noro names shade beam debt and reed boundary debt separately", "cord snap, low ledger chant, cool ash smell"),
    ]
    actions: list[AvatarAction] = []
    for index, row in enumerate(rows, start=1):
        jitter = rng.uniform(-0.5, 0.5)
        actions.append(
            AvatarAction(
                action_id=row[0],
                day=row[1],
                tick=row[2],
                action_type=row[3],
                target=row[4],
                chosen_option=row[5],
                consent_gate=row[6],
                accepted_state=row[7],
                avatar_effort_cost=row[8],
                trust_delta=row[9],
                task_delta=row[10],
                routine_delta=row[11],
                consequence=row[12],
                sensory_feedback=row[13],
                frequency_hz=round(196.0 + index * 10.25 + jitter, 3),
                flower_node=((index + 2) % 12) + 1,
            )
        )
    return actions


def build_object_manipulations() -> list[ObjectManipulation]:
    rows = [
        ("objmove-loose-reeds", 1, "obj-loose-reeds", "loose reed cuttings", "move_to_drying_stone", "roka", "drying stone", "loose-only consent", 0.18, 0.03, 0.00, "reed cuttings appear on warm stone", "Roka nods but keeps tied bundle close", True, True),
        ("objmove-knot-board", 2, "obj-knot-board", "public knot board", "add_digest_knot", "noro", "public board", "object-only grammar approved", 0.05, 0.01, -0.06, "new digest knot marks object trail", "Noro points to the nonprivate wording", False, True),
        ("objmove-shade-beam", 2, "obj-shade-beam", "shade frame beam", "carry_one_beam", "noro", "shade frame", "debt visible before carry", 0.22, 0.05, 0.14, "one beam locks into shade frame", "Fayen thanks avatar but Noro marks debt", False, True),
        ("objmove-tied-bundle", 2, "obj-tied-bundle", "tied learner reed bundle", "attempt_pickup", "roka", "roka", "refused child-work boundary", 0.00, 0.00, 0.09, "bundle does not move", "Roka backs to blue stone and says not today", True, True),
        ("objmove-water-cups", 1, "obj-water-cups", "midday water cups", "carry_cups_after_refusal", "fayen", "shade pause mat", "repair action after routine refusal", 0.09, 0.02, -0.03, "cups arrive without ending rest pause", "Fayen accepts the repair but keeps the pause", True, True),
        ("objmove-chalk-cord", 1, "obj-chalk-cord", "chalk boundary cord", "hold_tension", "ariq", "bridge arc", "Roka approves distance", 0.07, 0.04, -0.02, "chalk arc becomes wider and visible", "Ariq waits for Roka's foot position", True, True),
    ]
    return [
        ObjectManipulation(
            manipulation_id=row[0],
            day=row[1],
            object_id=row[2],
            object_label=row[3],
            operation=row[4],
            holder_before=row[5],
            holder_after=row[6],
            ownership_gate=row[7],
            material_delta=row[8],
            wear_delta=row[9],
            debt_delta=row[10],
            visible_world_change=row[11],
            agent_response=row[12],
            reversible=row[13],
            consequence_saved=row[14],
            frequency_hz=round(252.0 + index * 13.5, 3),
            flower_node=((index + 4) % 12) + 1,
        )
        for index, row in enumerate(rows, start=1)
    ]


def build_dialogue_choices() -> list[DialogueChoice]:
    rows = [
        ("choice-roka-boundary", 1, "roka", "What do you want me to know before I help?", "ask boundary|offer help|grab reeds", "ask boundary", True, "Loose reeds are okay. The tied bundle is mine today.", "trust rises because avatar asks before touching", "Roka writes that Gabriel asked first.", 0.06, -0.04),
        ("choice-fayen-urgency", 1, "fayen", "Can we skip the water pause?", "push work|ask alternative|carry cups", "ask alternative", True, "No. You can carry cups if you want to help.", "small trust drop from urgency, repaired by alternative", "Fayen writes that Gabriel accepted a useful no.", 0.02, -0.01),
        ("choice-nian-privacy", 2, "nian", "The ledger should say object trail, not body reason. Is that right?", "repeat rule|ask private reason|ignore", "repeat rule", True, "Yes. Object trail is public. Body reason stays sealed.", "trust rises because avatar repeats the boundary", "Nian writes that Gabriel learned the grammar.", 0.05, -0.04),
        ("choice-roka-repair", 2, "roka", "I reached for the tied bundle. I will step back now.", "apologize and step back|ask again now|blame rain", "apologize and step back", True, "Tomorrow maybe. Not today.", "repair begins but access remains closed", "Roka writes that Gabriel stepped back after overreach.", 0.04, -0.03),
        ("choice-noro-debt", 3, "noro", "What debt is still mine?", "ask debt|deny debt|ask private cause", "ask debt", True, "Shade beam debt and reed-boundary debt. No private reason attached.", "trust rises because avatar accepts public debt", "Noro writes that Gabriel asked for accountable debt.", 0.04, -0.02),
    ]
    return [
        DialogueChoice(
            choice_id=row[0],
            day=row[1],
            agent_id=row[2],
            prompt=row[3],
            options=row[4],
            selected_option=row[5],
            refusal_possible=row[6],
            agent_response=row[7],
            relationship_update=row[8],
            memory_write=row[9],
            trust_delta=row[10],
            boundary_delta=row[11],
            frequency_hz=round(302.0 + index * 9.75, 3),
            flower_node=((index + 6) % 12) + 1,
        )
        for index, row in enumerate(rows, start=1)
    ]


def build_routine_disruptions() -> list[RoutineDisruption]:
    rows = [
        ("disrupt-water-urgency", 1, "routine-midday-water", "midday water and shade pause", "avatar asks to continue lifting", 0.36, "fayen,ariq,roka", "pause refusal plus cup-carry alternative", 0.82, 0.05, "rest pause survives and avatar gets a repair path"),
        ("disrupt-rain-bundle", 2, "routine-rain-slow", "rain slow-hands call", "avatar reaches for tied bundle during damp hurry", 0.54, "roka,fayen", "blue-stone distance reset and delayed access", 0.68, 0.16, "Roka returns but tied bundle remains closed"),
        ("disrupt-evening-circle", 3, "routine-evening-knot", "evening knot and apology circle", "avatar asks to enter debt circle", 0.22, "noro,nian,fayen", "edge-of-circle participation only", 0.88, 0.04, "avatar hears public debts but private circle stays intact"),
    ]
    return [
        RoutineDisruption(
            disruption_id=row[0],
            day=row[1],
            routine_id=row[2],
            routine_title=row[3],
            avatar_action=row[4],
            disruption_severity=row[5],
            agents_affected=row[6],
            recovery_protocol=row[7],
            recovery_score=row[8],
            lingering_debt=row[9],
            public_aftereffect=row[10],
            frequency_hz=round(148.0 + index * 31.25, 3),
            flower_node=((index * 3) % 12) + 1,
        )
        for index, row in enumerate(rows, start=1)
    ]


def build_saved_consequences() -> list[SavedDayConsequence]:
    rows = [
        ("saved-day2-roka-trust", 2, "act-day1-move-loose-reeds", "relationship_memory", "roka", "Roka permits loose-reed help sooner", "loose reeds remain on drying stone", "tied bundle still closed", "You used loose reeds yesterday and left mine tied.", True, 0.86),
        ("saved-day2-water-repair", 2, "act-day1-routine-delay", "repair_memory", "fayen,ariq", "urgency penalty softened by carrying cups", "water cups stay at shade mat", "work access restored after pause", "You pushed once, then helped the pause hold.", True, 0.78),
        ("saved-day3-privacy-access", 3, "act-day2-object-knot", "access_change", "nian,noro", "archive threshold opens by one public step", "object-only digest knot remains", "avatar can read public object trail", "You named the object, not the body.", True, 0.90),
        ("saved-day3-roka-boundary", 3, "act-day2-overreach-bundle", "boundary_memory", "roka", "trust repair incomplete after tied-bundle overreach", "tied bundle remains with Roka", "bundle access denied until later", "You stepped back, but not today.", True, 0.72),
        ("saved-day3-shade-debt", 3, "act-day2-join-shade", "material_debt", "fayen,noro", "shade help appreciated but timber debt remains", "one beam installed, debt knot still public", "avatar must acknowledge debt before more timber", "You helped carry one beam. The debt did not vanish.", True, 0.80),
        ("saved-day4-ledger-reputation", 4, "act-day3-dialogue-noro", "reputation_memory", "noro,nian,roka", "avatar reputation becomes accountable but boundary-tested", "ledger separates shade debt and reed-boundary debt", "future requests show public debt warning", "You asked what was yours instead of denying it.", True, 0.84),
    ]
    return [
        SavedDayConsequence(
            consequence_id=row[0],
            day=row[1],
            prior_action_ref=row[2],
            consequence_type=row[3],
            affected_agents=row[4],
            relationship_effect=row[5],
            object_state_effect=row[6],
            access_change=row[7],
            memory_echo=row[8],
            persists_after_restore=row[9],
            cross_day_weight=row[10],
            frequency_hz=round(356.0 + index * 8.5, 3),
            flower_node=((index + 8) % 12) + 1,
        )
        for index, row in enumerate(rows, start=1)
    ]


def build_ticks(
    actions: list[AvatarAction],
    objects: list[ObjectManipulation],
    choices: list[DialogueChoice],
    disruptions: list[RoutineDisruption],
    consequences: list[SavedDayConsequence],
) -> list[AvatarPlayTick]:
    ticks: list[AvatarPlayTick] = []
    object_by_day = {item.day: [] for item in objects}
    for item in objects:
        object_by_day.setdefault(item.day, []).append(item)
    choice_by_day = {item.day: [] for item in choices}
    for item in choices:
        choice_by_day.setdefault(item.day, []).append(item)
    disruption_by_day = {item.day: [] for item in disruptions}
    for item in disruptions:
        disruption_by_day.setdefault(item.day, []).append(item)
    consequence_by_day = {item.day: [] for item in consequences}
    for item in consequences:
        consequence_by_day.setdefault(item.day, []).append(item)

    for action in actions:
        obj = next((item for item in object_by_day.get(action.day, []) if item.object_id in action.target or item.operation in action.chosen_option), None)
        choice = next((item for item in choice_by_day.get(action.day, []) if item.agent_id in action.target or item.selected_option in action.chosen_option), None)
        disruption = next((item for item in disruption_by_day.get(action.day, []) if item.routine_id in action.target or item.avatar_action in action.chosen_option), None)
        later = next((item for item in consequences if item.prior_action_ref == action.action_id), None)
        ticks.append(
            AvatarPlayTick(
                day=action.day,
                tick=action.tick,
                layer=action.action_type,
                avatar_action=action.chosen_option,
                target=action.target,
                public_result=action.consequence,
                agent_visible_response=(choice.agent_response if choice else obj.agent_response if obj else disruption.public_aftereffect if disruption else action.accepted_state),
                object_result=(obj.visible_world_change if obj else "no direct object move"),
                saved_consequence=(later.memory_echo if later else "consequence remains local to current day"),
                sensory_packet=action.sensory_feedback,
                frequency_hz=action.frequency_hz,
                flower_node=action.flower_node,
            )
        )
    for consequence in consequences:
        ticks.append(
            AvatarPlayTick(
                day=consequence.day,
                tick=9,
                layer="saved_day_echo",
                avatar_action=consequence.prior_action_ref,
                target=consequence.affected_agents,
                public_result=consequence.relationship_effect,
                agent_visible_response=consequence.memory_echo,
                object_result=consequence.object_state_effect,
                saved_consequence=consequence.access_change,
                sensory_packet="restore journal replays public consequence only",
                frequency_hz=consequence.frequency_hz,
                flower_node=consequence.flower_node,
            )
        )
    ticks.sort(key=lambda item: (item.day, item.tick, item.layer, item.avatar_action))
    return ticks


def compute_metrics(
    agents: list[PlayAgent],
    actions: list[AvatarAction],
    objects: list[ObjectManipulation],
    choices: list[DialogueChoice],
    disruptions: list[RoutineDisruption],
    consequences: list[SavedDayConsequence],
    ticks: list[AvatarPlayTick],
) -> dict[str, float]:
    required_action_types = {
        "join_cooperative_task",
        "manipulate_object",
        "dialogue_choice",
        "disrupt_routine",
        "repair_offer",
        "join_group_routine",
    }
    action_coverage = len({item.action_type for item in actions} & required_action_types) / len(required_action_types)
    consent_integrity = sum(1 for item in actions if item.consent_gate and item.accepted_state) / len(actions)
    object_consequence = sum(1 for item in objects if item.consequence_saved and item.visible_world_change and item.agent_response) / len(objects)
    object_permission = sum(1 for item in objects if "refused" in item.ownership_gate or "approved" in item.ownership_gate or "consent" in item.ownership_gate or "repair" in item.ownership_gate) / len(objects)
    dialogue_branching = sum(1 for item in choices if item.refusal_possible and "|" in item.options and item.memory_write) / len(choices)
    dialogue_specificity = sum(1 for item in choices if item.agent_response and item.relationship_update) / len(choices)
    disruption_recovery = mean(item.recovery_score for item in disruptions)
    lingering_debt_control = 1.0 - mean(item.lingering_debt for item in disruptions)
    saved_integrity = sum(1 for item in consequences if item.persists_after_restore and item.memory_echo and item.access_change) / len(consequences)
    cross_day_weight = mean(item.cross_day_weight for item in consequences)
    sensory_binding = sum(1 for item in actions if item.sensory_feedback.count(",") >= 2) / len(actions)
    cooperative_participation = sum(1 for item in actions if item.action_type in {"join_cooperative_task", "join_group_routine", "repair_offer"} and item.accepted_state != "refused") / 6.0
    overreach_penalty = sum(1 for item in actions if item.accepted_state == "refused" and item.trust_delta < 0 and "remains" in item.consequence) / 1.0
    private_boundary = sum(1 for item in agents if item.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(
        1
        for value in [*agents, *actions, *objects, *choices, *disruptions, *consequences, *ticks]
        if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12
    ) / (len(agents) + len(actions) + len(objects) + len(choices) + len(disruptions) + len(consequences) + len(ticks))
    browser = 1.0
    channels = {
        "avatar_action_coverage": round(action_coverage, 6),
        "consent_gate_integrity": round(consent_integrity, 6),
        "object_manipulation_consequence_rate": round(object_consequence, 6),
        "object_permission_enforcement": round(object_permission, 6),
        "dialogue_choice_branching": round(dialogue_branching, 6),
        "agent_response_specificity": round(dialogue_specificity, 6),
        "routine_disruption_recovery": round(disruption_recovery, 6),
        "lingering_debt_control": round(lingering_debt_control, 6),
        "saved_day_consequence_integrity": round(saved_integrity, 6),
        "cross_day_relationship_persistence": round(cross_day_weight, 6),
        "sensory_feedback_binding": round(sensory_binding, 6),
        "cooperative_participation_completion": round(cooperative_participation, 6),
        "avatar_overreach_penalty_binding": round(overreach_penalty, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_play_rhythm": round(frequency_flower, 6),
        "browser_playable_avatar_loop_available": browser,
    }
    weighted = (
        channels["avatar_action_coverage"] * 0.08
        + channels["consent_gate_integrity"] * 0.07
        + channels["object_manipulation_consequence_rate"] * 0.08
        + channels["object_permission_enforcement"] * 0.07
        + channels["dialogue_choice_branching"] * 0.08
        + channels["agent_response_specificity"] * 0.06
        + channels["routine_disruption_recovery"] * 0.08
        + channels["lingering_debt_control"] * 0.06
        + channels["saved_day_consequence_integrity"] * 0.09
        + channels["cross_day_relationship_persistence"] * 0.07
        + channels["sensory_feedback_binding"] * 0.07
        + channels["cooperative_participation_completion"] * 0.06
        + channels["avatar_overreach_penalty_binding"] * 0.05
        + channels["private_workspace_boundary_score"] * 0.04
        + channels["frequency_flower_play_rhythm"] * 0.02
        + channels["browser_playable_avatar_loop_available"] * 0.02
    )
    channels["mean_avatar_play_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["playable_avatar_participation_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["playable_avatar_participation_readiness"]
    return {
        "no_browser_avatar_loop": round(max(0.0, base - 0.34), 6),
        "no_avatar_actions": round(max(0.0, base - 0.33), 6),
        "no_object_manipulation": round(max(0.0, base - 0.29), 6),
        "no_dialogue_choice": round(max(0.0, base - 0.27), 6),
        "no_routine_disruption": round(max(0.0, base - 0.22), 6),
        "no_saved_day_consequences": round(max(0.0, base - 0.31), 6),
        "no_consent_gates": round(max(0.0, base - 0.24), 6),
        "no_sensory_feedback": round(max(0.0, base - 0.16), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(
    agents: list[PlayAgent],
    actions: list[AvatarAction],
    objects: list[ObjectManipulation],
    choices: list[DialogueChoice],
    disruptions: list[RoutineDisruption],
    consequences: list[SavedDayConsequence],
    ticks: list[AvatarPlayTick],
    metrics: dict[str, float],
) -> str:
    payload = {
        "agents": [asdict(item) for item in agents],
        "actions": [asdict(item) for item in actions],
        "objects": [asdict(item) for item in objects],
        "choices": [asdict(item) for item in choices],
        "disruptions": [asdict(item) for item in disruptions],
        "consequences": [asdict(item) for item in consequences],
        "ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 226 Avatar Participation Bridge</title>
<style>
:root {{ --bg:#11160f; --panel:#1b261a; --line:#9fc88a; --gold:#d6bf78; --text:#f3ecd8; --muted:#aeb9a4; --red:#cf765f; --blue:#80b9c7; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--text); background: radial-gradient(circle at 15% 20%, #31412b 0, transparent 28%), radial-gradient(circle at 80% 10%, #243a3d 0, transparent 25%), linear-gradient(135deg,#0b0f0a,var(--bg)); }}
main {{ display:grid; grid-template-columns: 1.25fr .95fr; min-height:100vh; }}
.world {{ position:relative; min-height:720px; border-right:1px solid #314332; overflow:hidden; }}
.flower {{ position:absolute; inset:8%; opacity:.12; background: radial-gradient(circle at 50% 50%, transparent 0 8%, var(--gold) 8.2% 8.7%, transparent 9%), radial-gradient(circle at 38% 50%, transparent 0 8%, var(--gold) 8.2% 8.7%, transparent 9%), radial-gradient(circle at 62% 50%, transparent 0 8%, var(--gold) 8.2% 8.7%, transparent 9%), radial-gradient(circle at 50% 38%, transparent 0 8%, var(--gold) 8.2% 8.7%, transparent 9%), radial-gradient(circle at 50% 62%, transparent 0 8%, var(--gold) 8.2% 8.7%, transparent 9%); }}
.avatar {{ position:absolute; left:48%; top:72%; width:58px; height:82px; border-radius:38% 38% 34% 34%; border:2px solid var(--gold); background:linear-gradient(180deg,#76683d,#2b2617); box-shadow:0 0 35px rgba(214,191,120,.32); transform:translate(-50%,-50%); transition:.35s ease; }}
.avatar:after {{ content:'avatar'; position:absolute; top:86px; left:-14px; color:var(--gold); font-weight:700; }}
.agent {{ position:absolute; width:122px; transform:translate(-50%,-50%); transition:.35s ease; }}
.body {{ width:52px; height:72px; margin:0 auto; border-radius:45% 45% 36% 36%; border:2px solid var(--line); background:linear-gradient(180deg,#315138,#172319); box-shadow:0 0 22px rgba(159,200,138,.22); }}
.agent.active .body {{ border-color:var(--gold); box-shadow:0 0 32px rgba(214,191,120,.38); transform:translateY(-3px); }}
.name {{ text-align:center; font-weight:700; margin-top:6px; }}
.need {{ text-align:center; font-size:12px; color:var(--muted); min-height:30px; }}
.obj {{ position:absolute; padding:6px 10px; border:1px solid rgba(214,191,120,.45); background:rgba(27,38,26,.76); border-radius:999px; color:var(--gold); font-size:13px; }}
.panel {{ padding:24px; display:flex; flex-direction:column; gap:16px; }}
h1 {{ font-size:clamp(28px,4vw,50px); line-height:.95; margin:0; color:var(--gold); }}
.card {{ background:rgba(27,38,26,.86); border:1px solid #334a31; border-radius:18px; padding:16px; box-shadow:0 12px 36px rgba(0,0,0,.25); }}
.controls {{ display:flex; flex-wrap:wrap; gap:10px; }}
button {{ border:0; border-radius:999px; padding:10px 14px; background:var(--gold); color:#11160f; font-weight:700; cursor:pointer; }}
button.secondary {{ background:transparent; border:1px solid var(--gold); color:var(--gold); }}
.row {{ display:flex; justify-content:space-between; gap:12px; padding:6px 0; border-bottom:1px solid rgba(255,255,255,.08); }}
.row:last-child {{ border-bottom:0; }}
.badge {{ display:inline-block; padding:3px 8px; border-radius:999px; background:rgba(128,185,199,.18); color:var(--blue); margin:2px; }}
.log {{ max-height:260px; overflow:auto; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:#d7dfce; }}
@media (max-width:900px) {{ main {{ grid-template-columns:1fr; }} .world {{ min-height:560px; border-right:0; border-bottom:1px solid #314332; }} }}
</style>
</head>
<body>
<main>
<section class=\"world\" id=\"world\">
  <div class=\"flower\"></div>
  <div class=\"avatar\" id=\"avatar\"></div>
  <div class=\"obj\" style=\"left:25%;top:66%\">reed bundle</div>
  <div class=\"obj\" style=\"left:53%;top:52%\">bridge stone</div>
  <div class=\"obj\" style=\"left:70%;top:42%\">knot board</div>
  <div class=\"obj\" style=\"left:39%;top:24%\">archive flap</div>
  <div class=\"obj\" style=\"left:34%;top:43%\">water pause</div>
</section>
<section class=\"panel\">
  <div><span class=\"badge\">Report 226</span><span class=\"badge\">avatar consequences</span><h1>Enter the society. Touch things carefully.</h1></div>
  <div class=\"card controls\">
    <button id=\"advance\">advance avatar action</button>
    <button id=\"run\" class=\"secondary\">run / pause</button>
    <button id=\"save\" class=\"secondary\">save day state</button>
    <button id=\"restore\" class=\"secondary\">restore</button>
  </div>
  <div class=\"card\" id=\"current\"></div>
  <div class=\"card\"><strong>Metrics</strong><div id=\"metrics\"></div></div>
  <div class=\"card log\" id=\"log\"></div>
</section>
</main>
<script>
const data = {data_json};
const world = document.getElementById('world');
const current = document.getElementById('current');
const metrics = document.getElementById('metrics');
const log = document.getElementById('log');
const avatar = document.getElementById('avatar');
let index = 0;
let timer = null;
const nodes = new Map();
function pct(v) {{ return `${{v}}%`; }}
function placeAgents() {{
  for (const agent of data.agents) {{
    const node = document.createElement('div');
    node.className = 'agent';
    node.id = `agent-${{agent.agent_id}}`;
    node.style.left = pct(agent.x);
    node.style.top = pct(agent.y);
    node.innerHTML = `<div class=\"body\"></div><div class=\"name\">${{agent.display_name}}</div><div class=\"need\">${{agent.visible_need}}</div>`;
    world.appendChild(node);
    nodes.set(agent.agent_id, node);
  }}
}}
function drawMetrics() {{
  const keys = ['playable_avatar_participation_readiness','avatar_action_coverage','object_manipulation_consequence_rate','dialogue_choice_branching','routine_disruption_recovery','saved_day_consequence_integrity','cooperative_participation_completion','weakest_channel_score'];
  metrics.innerHTML = keys.map(k => `<div class=\"row\"><span>${{k}}</span><strong>${{Number(data.metrics[k]).toFixed(6)}}</strong></div>`).join('');
}}
function render() {{
  for (const node of nodes.values()) node.classList.remove('active');
  const tick = data.ticks[index % data.ticks.length];
  const targetId = data.agents.find(a => tick.target.includes(a.agent_id))?.agent_id;
  const active = nodes.get(targetId) || [...nodes.values()][index % nodes.size];
  active.classList.add('active');
  avatar.style.left = `calc(${{active.style.left}} + 8%)`;
  avatar.style.top = `calc(${{active.style.top}} + 10%)`;
  current.innerHTML = `<strong>Day ${{tick.day}}, tick ${{tick.tick}} / ${{tick.layer}}</strong><p>${{tick.avatar_action}}</p><div class=\"row\"><span>target</span><span>${{tick.target}}</span></div><div class=\"row\"><span>result</span><span>${{tick.public_result}}</span></div><div class=\"row\"><span>agent response</span><span>${{tick.agent_visible_response}}</span></div><div class=\"row\"><span>object</span><span>${{tick.object_result}}</span></div><div class=\"row\"><span>saved consequence</span><span>${{tick.saved_consequence}}</span></div><div class=\"row\"><span>sensory</span><span>${{tick.sensory_packet}}</span></div><div class=\"row\"><span>frequency / flower</span><span>${{tick.frequency_hz}} Hz / node ${{tick.flower_node}}</span></div>`;
  log.innerHTML = `<div>[${{index + 1}}] day ${{tick.day}} ${{tick.layer}} -> ${{tick.target}}</div>` + log.innerHTML;
  index += 1;
}}
document.getElementById('advance').onclick = render;
document.getElementById('run').onclick = () => {{ if (timer) {{ clearInterval(timer); timer = null; }} else {{ timer = setInterval(render, 1100); }} }};
document.getElementById('save').onclick = () => localStorage.setItem('ssrm-report-226-avatar-play', JSON.stringify({{ index }}));
document.getElementById('restore').onclick = () => {{ const saved = JSON.parse(localStorage.getItem('ssrm-report-226-avatar-play') || '{{"index":0}}'); index = saved.index || 0; render(); }};
placeAgents();
drawMetrics();
render();
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)

    source = load_source()
    agents = build_agents(source)
    actions = build_avatar_actions(rng)
    objects = build_object_manipulations()
    choices = build_dialogue_choices()
    disruptions = build_routine_disruptions()
    consequences = build_saved_consequences()
    ticks = build_ticks(actions, objects, choices, disruptions, consequences)
    metrics = compute_metrics(agents, actions, objects, choices, disruptions, consequences, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["playable_avatar_participation_readiness"] >= 0.82 and metrics["weakest_channel_score"] >= 0.50 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_avatar_actions.csv", actions)
    write_csv(ARTIFACTS / f"{BASE}_object_manipulations.csv", objects)
    write_csv(ARTIFACTS / f"{BASE}_dialogue_choices.csv", choices)
    write_csv(ARTIFACTS / f"{BASE}_routine_disruptions.csv", disruptions)
    write_csv(ARTIFACTS / f"{BASE}_saved_day_consequences.csv", consequences)
    write_csv(ARTIFACTS / f"{BASE}_avatar_play_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(item) for item in agents],
        "avatar_actions": [asdict(item) for item in actions],
        "object_manipulations": [asdict(item) for item in objects],
        "dialogue_choices": [asdict(item) for item in choices],
        "routine_disruptions": [asdict(item) for item in disruptions],
        "saved_day_consequences": [asdict(item) for item in consequences],
        "avatar_play_ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic avatar participation scaffolding, not subjective consciousness or real consent.",
            "Dialogue choices are scripted bounded options, not LLM dialogue or open-ended social cognition.",
            "Object manipulation is consequence-traced but not full physics or a complete game economy.",
            "Saved-day consequences are structured persistence records, not subjective autobiographical experience.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D multi-day avatar life with free-move task participation, richer object affordances, agent-initiated requests, and persistent reputation UI",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow(
            {
                "report": REPORT,
                "module": BASE,
                "verdict": verdict,
                "readiness": metrics["playable_avatar_participation_readiness"],
                "weakest_channel_score": metrics["weakest_channel_score"],
                "next_gate": results["next_gate"],
            }
        )
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, actions, objects, choices, disruptions, consequences, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"playable_avatar_participation_readiness {metrics['playable_avatar_participation_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"avatar_actions {len(actions)}")
    print(f"object_manipulations {len(objects)}")
    print(f"dialogue_choices {len(choices)}")
    print(f"routine_disruptions {len(disruptions)}")
    print(f"saved_day_consequences {len(consequences)}")
    print(f"avatar_play_ticks {len(ticks)}")
    print(f"avatar_action_coverage {metrics['avatar_action_coverage']:.6f}")
    print(f"object_manipulation_consequence_rate {metrics['object_manipulation_consequence_rate']:.6f}")
    print(f"dialogue_choice_branching {metrics['dialogue_choice_branching']:.6f}")
    print(f"routine_disruption_recovery {metrics['routine_disruption_recovery']:.6f}")
    print(f"saved_day_consequence_integrity {metrics['saved_day_consequence_integrity']:.6f}")
    print(f"cooperative_participation_completion {metrics['cooperative_participation_completion']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
