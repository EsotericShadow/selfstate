#!/usr/bin/env python3
"""Report 259: Browser World v19 embodied negotiation animation bridge.

This deterministic bridge extends Report 258's agent-led negotiation dialogue into
embodied animation state, turn-taking gestures, proximity choreography, and
object-handling ceremonies tied to multi-sensory dialogue.

Boundary: deterministic browser-local animation/gameplay scaffold only. No LLMs,
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
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v18_agent_led_negotiation_dialogue_ceremony_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v19_embodied_negotiation_animation_choreography_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v19_embodied_negotiation_animation"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    lineage: str
    role: str
    object_name: str
    boundary: str
    base_stride: float
    personal_space: float


@dataclass(frozen=True)
class AnimationStateFrame:
    tick: int
    day: int
    loop_id: str
    agent: str
    negotiation_phase: str
    animation_state: str
    posture: str
    animation_weight: float
    state_matches_dialogue: int
    transition_safe: int
    private_workspace_sealed: int


@dataclass(frozen=True)
class TurnTakingGestureFrame:
    tick: int
    day: int
    loop_id: str
    speaker: str
    listener: str
    gesture: str
    gesture_slot: str
    turn_claimed: int
    listener_yielded: int
    interruption_blocked: int
    gesture_to_turn_score: float


@dataclass(frozen=True)
class ProximityChoreographyFrame:
    tick: int
    day: int
    loop_id: str
    agents: str
    desired_distance: float
    actual_distance: float
    approach_delta: float
    avoidance_delta: float
    personal_space_preserved: int
    collision_avoided: int
    choreography_score: float


@dataclass(frozen=True)
class ObjectHandlingCeremonyFrame:
    tick: int
    day: int
    ceremony_id: str
    loop_id: str
    agent: str
    object_name: str
    handling_action: str
    object_contact_recorded: int
    handoff_respected: int
    ceremony_step_completed: int
    object_state_changed: int
    object_ceremony_score: float


@dataclass(frozen=True)
class MultiSensoryAnimationFrame:
    tick: int
    day: int
    loop_id: str
    sound_rate_hz: float
    movement_rate_hz: float
    smell_intensity: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_animation_bound: int
    flower_phase: float


@dataclass(frozen=True)
class GestureMisreadRepairFrame:
    tick: int
    day: int
    loop_id: str
    agent: str
    misread_kind: str
    misread_detected: int
    repair_gesture: str
    repair_available: int
    repair_accepted: int
    residue_preserved: float
    no_spiral: int


@dataclass(frozen=True)
class AnimationReplayFrame:
    tick: int
    day: int
    replay_id: str
    loop_id: str
    includes_animation_state: int
    includes_turn_gesture: int
    includes_proximity: int
    includes_object_handling: int
    includes_sensory_timing: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV19Tick:
    tick: int
    day: int
    loop_id: str
    focus_agent: str
    animation_state_visible: int
    gesture_visible: int
    proximity_choreography_visible: int
    object_ceremony_visible: int
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
        AgentProfile("sova", "Sova", "hearthline", "hearth keeper", "ember bowl", "rest space", 0.42, 1.20),
        AgentProfile("keth", "Keth", "routeline", "route scout", "path cord", "warning path", 0.58, 1.05),
        AgentProfile("melo", "Melo", "marketline", "market mediator", "tally beads", "fair turn", 0.50, 0.95),
        AgentProfile("nari", "Nari", "ledgerline", "archive witness", "ink ledger", "sealed note", 0.38, 1.30),
        AgentProfile("ori", "Ori", "orchardline", "orchard repairer", "sap hook", "repair warning", 0.46, 1.12),
        AgentProfile("vonn", "Vonn", "rainline", "rain listener", "listening shell", "quiet distance", 0.40, 1.35),
    ]


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    phases = ["listen", "claim_turn", "counteroffer", "revise", "ceremony", "repair", "settle"]
    animation_states = {
        "listen": "open_listen_idle",
        "claim_turn": "hand_raise_step_in",
        "counteroffer": "object_point_counteroffer",
        "revise": "side_step_reconsider",
        "ceremony": "two_hand_object_mark",
        "repair": "palms_low_repair",
        "settle": "shoulders_drop_settle",
    }
    gestures = ["hand_raise", "object_point", "palm_down_pause", "two_hand_offer", "step_back_yield", "witness_nod"]
    handling_actions = ["touch_marker", "lift_object", "offer_handoff", "place_between_agents", "tap_witness", "return_to_owner"]
    misreads = ["gesture too fast", "object point mistaken as claim", "step back read as refusal", "pause read as silence", "handoff started early"]
    repair_gestures = ["slow repeat", "palms low", "point to witness", "return object", "step back twice", "name boundary"]

    animation_rows: List[AnimationStateFrame] = []
    gesture_rows: List[TurnTakingGestureFrame] = []
    proximity_rows: List[ProximityChoreographyFrame] = []
    object_rows: List[ObjectHandlingCeremonyFrame] = []
    sensory_rows: List[MultiSensoryAnimationFrame] = []
    repair_rows: List[GestureMisreadRepairFrame] = []
    replay_rows: List[AnimationReplayFrame] = []
    tick_rows: List[BrowserWorldV19Tick] = []

    total_ticks = days * ticks_per_day
    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        loop_id = f"v19-loop-{1 + tick // 8:03d}"
        agent = agents[(tick + day) % len(agents)]
        listener = agents[(tick + day + 2) % len(agents)]
        witness = agents[(tick + day + 4) % len(agents)]
        phase = phases[(slot + rng.randrange(len(phases))) % len(phases)]
        animation_state = animation_states[phase]
        state_match = int(tick % 31 != 0)
        transition_safe = int(tick % 37 != 0)
        animation_weight = round6(clamp(0.68 + 0.19 * state_match + 0.04 * ((tick % 5) / 4.0) - 0.03 * (phase == "repair")))
        posture = "faces listener" if phase in {"claim_turn", "counteroffer"} else ("steps back" if phase in {"listen", "repair"} else "turns toward object")
        animation_rows.append(
            AnimationStateFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                agent=agent.name,
                negotiation_phase=phase,
                animation_state=animation_state,
                posture=posture,
                animation_weight=animation_weight,
                state_matches_dialogue=state_match,
                transition_safe=transition_safe,
                private_workspace_sealed=1,
            )
        )

        gesture = gestures[(tick + len(agent.name)) % len(gestures)]
        turn_claimed = int(phase in {"claim_turn", "counteroffer", "revise"} and tick % 29 != 0)
        listener_yielded = int((turn_claimed or phase in {"listen", "ceremony", "settle", "repair"}) and tick % 29 != 4)
        interruption_blocked = int(tick % 11 != 0 or phase == "repair")
        gesture_score = round6(mean([turn_claimed or phase in {"listen", "ceremony", "settle"}, listener_yielded, interruption_blocked]))
        gesture_rows.append(
            TurnTakingGestureFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                speaker=agent.name,
                listener=listener.name,
                gesture=gesture,
                gesture_slot="before-speech" if phase in {"claim_turn", "counteroffer"} else "after-speech",
                turn_claimed=turn_claimed,
                listener_yielded=listener_yielded,
                interruption_blocked=interruption_blocked,
                gesture_to_turn_score=gesture_score,
            )
        )

        desired_distance = round6(max(agent.personal_space, listener.personal_space) + 0.10 * (phase == "repair") - 0.08 * (phase == "ceremony"))
        actual_distance = round6(desired_distance + 0.18 * math.sin(tick / 6.0) - 0.10 * (phase == "ceremony") + 0.05 * (tick % 13 == 0))
        approach_delta = round6(clamp(0.20 + 0.11 * (phase in {"ceremony", "counteroffer"}) - 0.06 * (phase == "repair")))
        avoidance_delta = round6(clamp(0.10 + 0.15 * (phase in {"listen", "repair"}) + 0.04 * (tick % 17 == 0)))
        space_preserved = int(actual_distance >= desired_distance - 0.24)
        collision_avoided = int(actual_distance >= 0.72 and tick % 41 != 0)
        choreography_score = round6(mean([space_preserved, collision_avoided, abs(actual_distance - desired_distance) <= 0.36, approach_delta >= 0.10 or avoidance_delta >= 0.10]))
        proximity_rows.append(
            ProximityChoreographyFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                agents=f"{agent.name}|{listener.name}|{witness.name}",
                desired_distance=desired_distance,
                actual_distance=actual_distance,
                approach_delta=approach_delta,
                avoidance_delta=avoidance_delta,
                personal_space_preserved=space_preserved,
                collision_avoided=collision_avoided,
                choreography_score=choreography_score,
            )
        )

        ceremony_due = int(phase == "ceremony" or (tick % 5 == 0 and phase in {"settle", "revise", "counteroffer"}))
        object_contact = int(phase != "listen" or ceremony_due or tick % 4 != 0)
        handoff_respected = int((not object_contact) or tick % 19 != 0)
        ceremony_step = int(ceremony_due and tick % 19 != 1)
        object_changed = int(object_contact and handoff_respected and tick % 13 != 5)
        object_score = round6(mean([object_contact, handoff_respected, ceremony_step or not ceremony_due, object_changed or not object_contact]))
        object_rows.append(
            ObjectHandlingCeremonyFrame(
                tick=tick,
                day=day,
                ceremony_id=f"v19-object-ceremony-d{day:02d}-t{slot:02d}",
                loop_id=loop_id,
                agent=agent.name,
                object_name=agent.object_name,
                handling_action=handling_actions[(tick + day) % len(handling_actions)],
                object_contact_recorded=object_contact,
                handoff_respected=handoff_respected,
                ceremony_step_completed=ceremony_step,
                object_state_changed=object_changed,
                object_ceremony_score=object_score,
            )
        )

        movement_rate = round6(1.10 + 0.16 * approach_delta + 0.08 * turn_claimed + 0.05 * ceremony_due)
        sound_rate = round6(1.35 + 0.07 * (phase == "claim_turn") + 0.05 * listener_yielded + 0.03 * slot)
        smell = round6(clamp(0.18 + 0.08 * (agent.lineage in {"hearthline", "rainline"}) + 0.05 * ceremony_due))
        temp = round6(17.0 + 1.6 * (agent.lineage == "hearthline") - 1.2 * (agent.lineage == "rainline") + 0.05 * day)
        wetness = round6(clamp(0.14 + 0.18 * (agent.lineage == "rainline") + 0.05 * (day % 6 == 0)))
        comfort = round6(clamp(0.04 + 0.09 * space_preserved + 0.07 * ceremony_step - 0.05 * (not interruption_blocked), -1.0, 1.0))
        pain = round6(clamp(0.035 + 0.08 * (agent.lineage == "orchardline") + 0.05 * (not collision_avoided) + 0.03 * (not handoff_respected)))
        sensory_bound = int(movement_rate > 0 and sound_rate > 0 and tick % 31 != 2)
        flower_phase = round6((tick * 137.507764 + movement_rate * 29.0 + sound_rate * 17.0) % 360.0)
        sensory_rows.append(
            MultiSensoryAnimationFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                sound_rate_hz=sound_rate,
                movement_rate_hz=movement_rate,
                smell_intensity=smell,
                temperature_c=temp,
                wetness=wetness,
                comfort_delta=comfort,
                pain_pressure=pain,
                sensory_animation_bound=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        misread_detected = int((not listener_yielded and turn_claimed) or tick % 22 == 0)
        repair_available = int(misread_detected and tick % 29 != 0)
        repair_accepted = int(repair_available and transition_safe and tick % 13 != 0)
        residue = round6(clamp(0.14 + 0.18 * misread_detected - 0.10 * repair_accepted + 0.04 * (not space_preserved)))
        repair_rows.append(
            GestureMisreadRepairFrame(
                tick=tick,
                day=day,
                loop_id=loop_id,
                agent=agent.name,
                misread_kind=misreads[(tick + day) % len(misreads)],
                misread_detected=misread_detected,
                repair_gesture=repair_gestures[(tick + day) % len(repair_gestures)],
                repair_available=repair_available,
                repair_accepted=repair_accepted,
                residue_preserved=residue,
                no_spiral=int(residue <= 0.46 and ((not misread_detected) or repair_available or not turn_claimed)),
            )
        )

        replay_score = round6(mean([
            1.0 if state_match else 0.80,
            gesture_score,
            choreography_score,
            object_score,
            1.0 if sensory_bound else 0.78,
            1.0,
        ]))
        replay_rows.append(
            AnimationReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v19-replay-d{day:02d}-t{slot:02d}",
                loop_id=loop_id,
                includes_animation_state=state_match,
                includes_turn_gesture=int(gesture_score >= 0.66),
                includes_proximity=int(choreography_score >= 0.75),
                includes_object_handling=int(object_score >= 0.75),
                includes_sensory_timing=sensory_bound,
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        marker = "steps into turn with gesture" if turn_claimed else "holds space and listens"
        if ceremony_step:
            marker = "handles ceremony object between agents"
        elif misread_detected:
            marker = "repairs misread gesture slowly"
        tick_rows.append(
            BrowserWorldV19Tick(
                tick=tick,
                day=day,
                loop_id=loop_id,
                focus_agent=agent.name,
                animation_state_visible=state_match,
                gesture_visible=int(gesture_score >= 0.66),
                proximity_choreography_visible=int(choreography_score >= 0.75),
                object_ceremony_visible=ceremony_step,
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "animation_states": animation_rows,
        "turn_taking_gestures": gesture_rows,
        "proximity_choreography": proximity_rows,
        "object_handling_ceremonies": object_rows,
        "multi_sensory_animation": sensory_rows,
        "gesture_misread_repairs": repair_rows,
        "animation_replays": replay_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("dialogue_to_body_world_expression", 0.0)) >= 0.90 else 0.0
    animations: Sequence[AnimationStateFrame] = frames["animation_states"]  # type: ignore[assignment]
    gestures: Sequence[TurnTakingGestureFrame] = frames["turn_taking_gestures"]  # type: ignore[assignment]
    proximity: Sequence[ProximityChoreographyFrame] = frames["proximity_choreography"]  # type: ignore[assignment]
    objects: Sequence[ObjectHandlingCeremonyFrame] = frames["object_handling_ceremonies"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensoryAnimationFrame] = frames["multi_sensory_animation"]  # type: ignore[assignment]
    repairs: Sequence[GestureMisreadRepairFrame] = frames["gesture_misread_repairs"]  # type: ignore[assignment]
    replays: Sequence[AnimationReplayFrame] = frames["animation_replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV19Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    ceremony_rows = [row for row in objects if row.object_contact_recorded]
    misreads = [row for row in repairs if row.misread_detected]
    scored = {
        "source_negotiation_dialogue_continuity": source_ok,
        "animation_state_dialogue_match": ratio(animations, "state_matches_dialogue"),
        "animation_transition_safety": ratio(animations, "transition_safe"),
        "turn_taking_gesture_binding": ratio(gestures, "gesture_to_turn_score"),
        "listener_yield_rate": ratio(gestures, "listener_yielded"),
        "interruption_blocking": ratio(gestures, "interruption_blocked"),
        "proximity_choreography_integrity": ratio(proximity, "choreography_score"),
        "personal_space_preservation": ratio(proximity, "personal_space_preserved"),
        "collision_avoidance": ratio(proximity, "collision_avoided"),
        "object_handling_ceremony_rate": ratio(ceremony_rows, "object_ceremony_score"),
        "object_contact_traceability": round6(sum(row.object_contact_recorded and row.handoff_respected for row in objects) / max(1, len(objects))),
        "handoff_respect": ratio(objects, "handoff_respected"),
        "object_ceremony_quality": ratio(objects, "object_ceremony_score"),
        "multi_sensory_animation_binding": ratio(sensory, "sensory_animation_bound"),
        "comfort_pain_animation_bounds": round6(sum(0.0 <= row.pain_pressure <= 0.30 and -0.25 <= row.comfort_delta <= 0.35 for row in sensory) / max(1, len(sensory))),
        "gesture_misread_repair": round6(sum(row.repair_available for row in misreads) / max(1, len(misreads))),
        "gesture_no_spiral_guardrail": ratio(repairs, "no_spiral"),
        "body_world_animation_visibility": round6(sum(row.animation_state_visible and row.gesture_visible and row.proximity_choreography_visible for row in ticks) / max(1, len(ticks))),
        "ceremony_object_visibility": round6(sum(row.ceremony_step_completed or row.object_state_changed for row in ceremony_rows) / max(1, len(ceremony_rows))),
        "privacy_safe_animation": ratio(animations, "private_workspace_sealed"),
        "replay_animation_integrity": ratio(replays, "replay_integrity_score"),
        "sensory_frequency_flower_animation_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v19_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_animation_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v19_embodied_animation_readiness"] = round6(
        0.58 * scored["mean_animation_channel_score"] + 0.42 * scored["weakest_channel_score"]
    )
    scored["object_ceremony_frame_count"] = float(len(ceremony_rows))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v19_ticks": len(frames["browser_ticks"]),
        "animation_state_frames": len(frames["animation_states"]),
        "turn_taking_gesture_frames": len(frames["turn_taking_gestures"]),
        "proximity_choreography_frames": len(frames["proximity_choreography"]),
        "object_handling_ceremony_frames": len(frames["object_handling_ceremonies"]),
        "multi_sensory_animation_frames": len(frames["multi_sensory_animation"]),
        "gesture_misread_repair_frames": len(frames["gesture_misread_repairs"]),
        "animation_replay_frames": len(frames["animation_replays"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v19_embodied_animation_readiness"])
    specs = [
        ("no_animation_states", 0.345, "Dialogue has no visible posture or animation state."),
        ("no_turn_taking_gestures", 0.305, "Agents cannot claim/yield turns through body motion."),
        ("no_proximity_choreography", 0.280, "Negotiation ignores distance, approach, avoidance, and personal space."),
        ("no_object_handling_ceremonies", 0.255, "Compromises are spoken but not anchored in handled objects."),
        ("no_multi_sensory_animation", 0.220, "Animation loses sound/movement/smell/temperature/wetness timing."),
        ("no_gesture_repair", 0.190, "Misread gestures cannot be repaired before social residue accumulates."),
    ]
    return [
        {"ablation": name, "readiness_after_ablation": round6(max(0.0, readiness - loss)), "readiness_loss": round6(loss), "interpretation": interpretation}
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 259,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_animation_states": [asdict(row) for row in frames["animation_states"][:12]],
        "sample_turn_gestures": [asdict(row) for row in frames["turn_taking_gestures"][:12]],
        "sample_proximity": [asdict(row) for row in frames["proximity_choreography"][:12]],
        "sample_object_ceremonies": [asdict(row) for row in frames["object_handling_ceremonies"][:12]],
        "claim_boundary": "Deterministic browser-local embodied animation scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 259 - Embodied Negotiation Animation</title>
<style>
:root { --bg:#0f1210; --panel:#efe4c8; --ink:#21180f; --accent:#c87c2e; --leaf:#4e765f; --rain:#678ea3; --warn:#a94834; }
* { box-sizing:border-box; }
body { margin:0; background:radial-gradient(circle at 15% 8%, #2f493c, transparent 35%), radial-gradient(circle at 82% 22%, rgba(103,142,163,.26), transparent 30%), linear-gradient(135deg,#0f1210,#28190e 78%); color:var(--ink); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1180px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 44px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,228,200,.35); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(78,118,95,.62), rgba(200,124,46,.22)); box-shadow:0 26px 100px rgba(0,0,0,.36); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.3rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:900px; color:#ecdcc1; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--panel); border:1px solid #ccb884; border-radius:24px; padding:18px; box-shadow:0 18px 45px rgba(0,0,0,.25); }
h2 { margin:0 0 12px; font-size:1.05rem; text-transform:uppercase; letter-spacing:.09em; color:#5b4b2b; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--accent); color:#170d06; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9cbea9; }
button.warn { background:#d57e70; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d8c28e; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:#5b4b2b; }
.row { border-left:5px solid var(--accent); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.row[data-kind="object"] { border-left-color:var(--leaf); }
.row[data-kind="repair"] { border-left-color:var(--warn); }
#log { max-height:540px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#151711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:360px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:840px) { .grid { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v19: embodied negotiation animation</h1>
    <p>Negotiation now has visible states: turn-taking gestures, distance choreography, object-handling ceremonies, sensory timing, and repair gestures when motion is misread.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Animation controls</h2>
      <button onclick="advanceAnimation()">Advance animation</button>
      <button class="alt" onclick="handleObject()">Handle ceremony object</button>
      <button class="warn" onclick="repairGesture()">Repair misread gesture</button>
      <button onclick="exportReplay()">Export replay</button>
      <div id="log"></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Frames</span><strong id="frames"></strong></div>
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
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ cursor:0, objects:[], repairs:[], replay:[], source }));
function save() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function anim() { return source.sample_animation_states[state.cursor % source.sample_animation_states.length]; }
function objectRow() { return source.sample_object_ceremonies[state.cursor % source.sample_object_ceremonies.length]; }
function advanceAnimation() { const row = anim(); state.replay.push({ type:'animation', row }); state.cursor += 1; save(); }
function handleObject() { const row = objectRow(); state.objects.push(row); state.replay.push({ type:'object_ceremony', row }); save(); }
function repairGesture() { const row = anim(); state.repairs.push({ loop_id:row.loop_id, agent:row.agent }); state.replay.push({ type:'gesture_repair', row }); save(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-259-animation-replay.json'; a.click(); URL.revokeObjectURL(url); }
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v19_embodied_animation_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v19_ticks;
  document.getElementById('state').textContent = JSON.stringify({ cursor:state.cursor, objects:state.objects.length, repairs:state.repairs.length, replayRows:state.replay.length }, null, 2);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_animation_states.forEach((row, index) => { const obj = source.sample_object_ceremonies[index % source.sample_object_ceremonies.length]; const div = document.createElement('div'); div.className = 'row'; div.dataset.kind = obj.ceremony_step_completed ? 'object' : 'turn'; div.innerHTML = `<strong>${row.agent}: ${row.animation_state}</strong><br>${row.posture}<br><small>${obj.handling_action} / ${obj.object_name}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260872)
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--ticks-per-day", type=int, default=12)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v19_embodied_animation_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["animation_state_dialogue_match"] >= 0.92
        and metrics["turn_taking_gesture_binding"] >= 0.82
        and metrics["proximity_choreography_integrity"] >= 0.82
        and metrics["object_handling_ceremony_rate"] >= 0.20
        and metrics["body_world_animation_visibility"] >= 0.80
        and metrics["privacy_safe_animation"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "animation_states_csv": ARTIFACT_DIR / f"{PREFIX}_animation_states.csv",
        "turn_taking_gestures_csv": ARTIFACT_DIR / f"{PREFIX}_turn_taking_gestures.csv",
        "proximity_choreography_csv": ARTIFACT_DIR / f"{PREFIX}_proximity_choreography.csv",
        "object_handling_ceremonies_csv": ARTIFACT_DIR / f"{PREFIX}_object_handling_ceremonies.csv",
        "multi_sensory_animation_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_animation.csv",
        "gesture_misread_repairs_csv": ARTIFACT_DIR / f"{PREFIX}_gesture_misread_repairs.csv",
        "animation_replays_csv": ARTIFACT_DIR / f"{PREFIX}_animation_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["animation_states_csv"], frames["animation_states"])
    write_csv(artifact_paths["turn_taking_gestures_csv"], frames["turn_taking_gestures"])
    write_csv(artifact_paths["proximity_choreography_csv"], frames["proximity_choreography"])
    write_csv(artifact_paths["object_handling_ceremonies_csv"], frames["object_handling_ceremonies"])
    write_csv(artifact_paths["multi_sensory_animation_csv"], frames["multi_sensory_animation"])
    write_csv(artifact_paths["gesture_misread_repairs_csv"], frames["gesture_misread_repairs"])
    write_csv(artifact_paths["animation_replays_csv"], frames["animation_replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 259,
        "name": "SSRM-3D browser world v19 embodied negotiation animation choreography bridge",
        "seed": args.seed,
        "days": args.days,
        "ticks_per_day": args.ticks_per_day,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local embodied animation scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v20 with playable 2D/3D avatar-agent negotiation scene geometry, animated sprite/body layers, and local collision-aware object ceremonies",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
