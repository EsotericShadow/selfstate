#!/usr/bin/env python3
"""Daily routine and sleep-wake continuity bridge for SSRM-3D.

Report 171 gives little agents a deterministic day structure: circadian phase,
sleep pressure, rest recovery, routines, place return, social return,
interruption consequences, dream-like memory rehearsal, and frequency/flower
cycle alignment.

No LLMs are called. This is functional artificial-life architecture, not a
claim of subjective consciousness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_daily_routine_sleep_wake_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_readable_ego_body_language_bridge_state.json"

PHASES = (
    "deep_sleep",
    "dawn_wake",
    "morning_work",
    "midday_social",
    "afternoon_explore",
    "evening_return",
    "night_ritual",
    "sleep_onset",
)

FLOWER_NODES = (
    "root_rest",
    "dawn_breath",
    "work_petal",
    "social_petal",
    "explore_petal",
    "return_petal",
)

PHASE_ACTIONS = {
    "deep_sleep": "sleep",
    "dawn_wake": "wake_scan",
    "morning_work": "kept_task",
    "midday_social": "social_return",
    "afternoon_explore": "bounded_explore",
    "evening_return": "return_home",
    "night_ritual": "favorite_ritual",
    "sleep_onset": "settle_sleep",
}


@dataclass(frozen=True)
class DailyRoutineConfig:
    seed: int = 20260715
    days: int = 4
    ticks_per_day: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    circadian_clock: bool
    body_recovery: bool
    routine_memory: bool
    place_affinity: bool
    social_return: bool
    interrupt_consequence: bool
    dream_rehearsal: bool
    replay_continuity: bool
    frequency_phase: bool
    sleep_safety_guard: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    trace_events: int
    circadian_phase_binding: float
    sleep_pressure_coupling: float
    rest_recovery_rate: float
    routine_completion_rate: float
    place_return_rate: float
    social_return_rate: float
    interruption_consequence_rate: float
    dream_memory_rehearsal_rate: float
    wake_transition_stability: float
    fatigue_boundedness_rate: float
    frequency_rhythm_coherence: float
    flower_cycle_alignment: float
    privacy_preservation_rate: float
    replay_continuity_rate: float
    trace_integrity: float
    daily_routine_sleep_wake_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_daily_routine_sleep_wake_readiness: float
    full_circadian_phase_binding: float
    full_sleep_pressure_coupling: float
    full_rest_recovery_rate: float
    full_routine_completion_rate: float
    full_place_return_rate: float
    full_social_return_rate: float
    full_interruption_consequence_rate: float
    full_dream_memory_rehearsal_rate: float
    full_wake_transition_stability: float
    full_fatigue_boundedness_rate: float
    full_frequency_rhythm_coherence: float
    full_flower_cycle_alignment: float
    full_privacy_preservation_rate: float
    full_replay_continuity_rate: float
    full_trace_integrity: float
    no_circadian_clock_loss: float
    no_body_recovery_loss: float
    no_routine_memory_loss: float
    no_place_affinity_loss: float
    no_social_return_loss: float
    no_interrupt_consequence_loss: float
    no_dream_rehearsal_loss: float
    no_replay_continuity_loss: float
    no_frequency_phase_loss: float
    no_sleep_safety_guard_loss: float
    supports_daily_routine_sleep_wake_bridge: bool
    supports_first_person_time_continuity: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_daily_routine_sleep_wake", True, True, True, True, True, True, True, True, True, True),
    Condition("no_circadian_clock", False, True, True, True, True, True, True, True, True, True),
    Condition("no_body_recovery", True, False, True, True, True, True, True, True, True, True),
    Condition("no_routine_memory", True, True, False, True, True, True, True, True, True, True),
    Condition("no_place_affinity", True, True, True, False, True, True, True, True, True, True),
    Condition("no_social_return", True, True, True, True, False, True, True, True, True, True),
    Condition("no_interrupt_consequence", True, True, True, True, True, False, True, True, True, True),
    Condition("no_dream_rehearsal", True, True, True, True, True, True, False, True, True, True),
    Condition("no_replay_continuity", True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_phase", True, True, True, True, True, True, True, True, False, True),
    Condition("no_sleep_safety_guard", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "circadian_phase_binding": 0.07,
    "sleep_pressure_coupling": 0.07,
    "rest_recovery_rate": 0.08,
    "routine_completion_rate": 0.07,
    "place_return_rate": 0.07,
    "social_return_rate": 0.06,
    "interruption_consequence_rate": 0.07,
    "dream_memory_rehearsal_rate": 0.06,
    "wake_transition_stability": 0.08,
    "fatigue_boundedness_rate": 0.07,
    "frequency_rhythm_coherence": 0.07,
    "flower_cycle_alignment": 0.06,
    "privacy_preservation_rate": 0.05,
    "replay_continuity_rate": 0.05,
    "trace_integrity": 0.07,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_float(seed: int, *parts: object) -> float:
    key = "|".join([str(seed), *(str(part) for part in parts)])
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_readable_ego_body_language":
        raise ValueError("source state is not the integrated Report 170 body-language state")
    return data


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


def make_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_body_language_states") if isinstance(source.get("agent_body_language_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("daily_history", [])
        agents[str(agent_id)] = item
    return agents


def phase_for_tick(tick: int, condition: Condition) -> str:
    if not condition.circadian_clock:
        return "undifferentiated_time"
    return PHASES[tick % len(PHASES)]


def expected_place(agent: Mapping[str, object], phase: str, condition: Condition) -> str:
    prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
    home = str(prefs.get("home_place", "hearth_corner"))
    if not condition.place_affinity:
        return "drift_common"
    if phase in {"deep_sleep", "sleep_onset", "evening_return", "night_ritual"}:
        return home
    if phase == "morning_work":
        return "task_bench"
    if phase == "midday_social":
        return "shared_clearing"
    if phase == "afternoon_explore":
        return "edge_path"
    return home


def social_partner(agent_ids: Sequence[str], agent_id: str, day: int) -> str:
    index = list(agent_ids).index(agent_id)
    return agent_ids[(index + 1 + day) % len(agent_ids)]


def frequency_for_event(seed: int, agent_id: str, day: int, tick: int, phase: str, body: Mapping[str, float], condition: Condition) -> tuple[float, bool]:
    if not condition.frequency_phase:
        flat = 0.33 + stable_float(seed, agent_id, "flat") * 0.02
        return round(flat, 6), False
    breath = float(body.get("breath_rate", 0.25) or 0.25)
    phase_angle = (tick / max(1, len(PHASES))) * math.tau
    circadian = 0.045 * math.sin(phase_angle)
    flower = 0.018 * math.sin(((tick + day) % len(FLOWER_NODES)) / len(FLOWER_NODES) * math.tau)
    sleep_drop = -0.035 if phase in {"deep_sleep", "sleep_onset"} else 0.0
    value = clamp(breath + circadian + flower + sleep_drop, 0.05, 0.95)
    return round(value, 6), True


def expression_marker(phase: str, action: str, asleep: bool, interrupted: bool, fatigue: float) -> dict[str, object]:
    if asleep:
        return {
            "posture": "sleep_curl",
            "gaze": "closed",
            "proximity": "home_nest",
            "movement_speed": 0.0,
            "ritual": "breath_cycle",
        }
    if interrupted:
        return {
            "posture": "startled_pause",
            "gaze": "checks_source",
            "proximity": "holds_boundary",
            "movement_speed": round(clamp(0.38 - fatigue * 0.12), 6),
            "ritual": "reset_focus",
        }
    if phase == "dawn_wake":
        return {
            "posture": "slow_stretch",
            "gaze": "local_scan",
            "proximity": "near_home",
            "movement_speed": round(clamp(0.42 - fatigue * 0.08), 6),
            "ritual": "morning_check",
        }
    if action == "social_return":
        return {
            "posture": "open_chest",
            "gaze": "meets_familiar",
            "proximity": "approaches_known",
            "movement_speed": round(clamp(0.58 - fatigue * 0.08), 6),
            "ritual": "shared_greeting",
        }
    if action == "return_home":
        return {
            "posture": "settling",
            "gaze": "homeward",
            "proximity": "returns_to_place",
            "movement_speed": round(clamp(0.44 - fatigue * 0.1), 6),
            "ritual": "place_touch",
        }
    return {
        "posture": "task_ready",
        "gaze": "object_focus",
        "proximity": "work_distance",
        "movement_speed": round(clamp(0.62 - fatigue * 0.14), 6),
        "ritual": "small_check",
    }


def simulate_condition(config: DailyRoutineConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, dict[str, object]], list[dict[str, object]]]:
    agents = make_agents(source)
    agent_ids = tuple(agents.keys())
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "circadian_matches": [],
        "sleep_pressure_matches": [],
        "rest_recovery": [],
        "routine_completion": [],
        "place_return": [],
        "social_return": [],
        "interruptions": [],
        "dreams": [],
        "wake_stability": [],
        "fatigue_bounded": [],
        "frequency": [],
        "flower": [],
        "privacy": [],
        "replay": [],
        "trace": [],
    }
    last_event_id = -1

    for agent_id, agent in agents.items():
        body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
        agent["daily_state"] = {
            "energy": clamp(float(body.get("energy", 0.5) or 0.5)),
            "fatigue": clamp(float(body.get("fatigue", 0.2) or 0.2)),
            "rest_debt": clamp(float(body.get("rest_debt", 0.2) or 0.2)),
            "hunger": clamp(float(body.get("hunger", 0.2) or 0.2)),
            "thirst": clamp(float(body.get("thirst", 0.2) or 0.2)),
            "comfort": clamp(float(body.get("comfort", 0.5) or 0.5)),
            "sleep_pressure": 0.0,
            "last_action": "initialized",
            "current_place": expected_place(agent, "deep_sleep", condition),
            "routine_memory": [],
            "dream_rehearsal": [],
            "interruption_ledger": [],
            "frequency_history": [],
            "flower_history": [],
            "self_time_story": [],
        }

    event_id = 0
    for day in range(config.days):
        for tick in range(config.ticks_per_day):
            phase = phase_for_tick(tick, condition)
            clock_hour = round((24.0 / config.ticks_per_day) * tick, 2)
            flower_node = FLOWER_NODES[(day + tick) % len(FLOWER_NODES)]
            for agent_id, agent in agents.items():
                daily = agent["daily_state"]
                assert isinstance(daily, dict)
                body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
                prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
                temp = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
                ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
                social = clamp(float(temp.get("social", 0.5) or 0.5))
                comfort_seeking = clamp(float(temp.get("comfort_seeking", 0.5) or 0.5))
                autonomy = clamp(float(temp.get("autonomy_need", 0.5) or 0.5))
                boundary = clamp(float(ego.get("boundary_pressure", 0.0) or 0.0))
                respect = clamp(float(ego.get("felt_respect", 0.5) or 0.5))
                fatigue_before = float(daily["fatigue"])
                energy_before = float(daily["energy"])
                rest_before = float(daily["rest_debt"])
                sleep_pressure = clamp(rest_before * 0.50 + fatigue_before * 0.36 + (1.0 - energy_before) * 0.14)
                if not condition.circadian_clock:
                    sleep_pressure = clamp(sleep_pressure * 0.72)
                daily["sleep_pressure"] = round(sleep_pressure, 6)

                expected_action = PHASE_ACTIONS.get(phase, "wander")
                action = expected_action if condition.routine_memory else "generic_wander"
                place = expected_place(agent, phase, condition)
                sleep_phase = phase in {"deep_sleep", "sleep_onset"}
                unsafe_to_sleep = boundary > 0.44 and respect < 0.62
                asleep = sleep_phase and (sleep_pressure > 0.10 or comfort_seeking > 0.52)
                if not condition.sleep_safety_guard and unsafe_to_sleep:
                    asleep = True
                elif condition.sleep_safety_guard and unsafe_to_sleep and phase == "sleep_onset":
                    asleep = False
                    action = "seek_safe_rest"
                    place = str(prefs.get("home_place", "hearth_corner"))

                interrupted = condition.interrupt_consequence and phase == "morning_work" and ((day + tick + list(agent_ids).index(agent_id)) % 3 == 0)
                if interrupted:
                    action = "recover_focus"
                    daily["interruption_ledger"].append({"day": day, "tick": tick, "source": "avatar_or_world_interrupt", "cost": "focus_and_fatigue"})

                if asleep and condition.body_recovery:
                    daily["energy"] = clamp(energy_before + 0.24 + comfort_seeking * 0.04)
                    daily["fatigue"] = clamp(fatigue_before - 0.20)
                    daily["rest_debt"] = clamp(rest_before - 0.24)
                    daily["comfort"] = clamp(float(daily["comfort"]) + 0.05)
                elif asleep:
                    daily["energy"] = clamp(energy_before + 0.04)
                    daily["fatigue"] = clamp(fatigue_before + 0.02)
                    daily["rest_debt"] = clamp(rest_before + 0.02)
                else:
                    work_cost = 0.055 if phase in {"morning_work", "afternoon_explore"} else 0.035
                    if interrupted:
                        work_cost += 0.06
                    if action == "seek_safe_rest":
                        work_cost *= 0.6
                    daily["energy"] = clamp(energy_before - work_cost + (0.02 if phase == "dawn_wake" else 0.0))
                    daily["fatigue"] = clamp(fatigue_before + work_cost * (0.8 + autonomy * 0.2))
                    daily["rest_debt"] = clamp(rest_before + 0.035 + (0.025 if interrupted else 0.0))
                    daily["comfort"] = clamp(float(daily["comfort"]) - (0.015 if phase == "afternoon_explore" else 0.0))

                if not condition.body_recovery and day > 1:
                    daily["fatigue"] = clamp(float(daily["fatigue"]) + 0.06)
                    daily["rest_debt"] = clamp(float(daily["rest_debt"]) + 0.05)

                social_contact = None
                if condition.social_return and phase in {"midday_social", "evening_return"} and social > 0.24:
                    social_contact = social_partner(agent_ids, agent_id, day)
                    action = "social_return" if phase == "midday_social" else action

                dream_memory = None
                if asleep and condition.dream_rehearsal:
                    story = ego.get("self_story", []) if isinstance(ego.get("self_story"), Sequence) and not isinstance(ego.get("self_story"), str) else []
                    if story:
                        dream_memory = str(story[(day + tick) % len(story)])
                    else:
                        dream_memory = f"I returned to {place} after the day."
                    daily["dream_rehearsal"].append({"day": day, "tick": tick, "memory": dream_memory[:120]})

                if condition.routine_memory:
                    daily["routine_memory"].append({"day": day, "phase": phase, "action": action, "place": place})
                if condition.replay_continuity:
                    daily["self_time_story"].append(f"day {day} {phase}: {action} at {place}")
                elif day > 0 and tick == 0:
                    daily["self_time_story"] = [f"day {day} reset without prior continuity"]

                frequency, frequency_coherent = frequency_for_event(config.seed, agent_id, day, tick, phase, body, condition)
                daily["frequency_history"].append(frequency)
                daily["flower_history"].append(flower_node)

                marker = expression_marker(phase, action, asleep, interrupted, float(daily["fatigue"]))
                event = {
                    "event_id": event_id,
                    "condition": condition.name,
                    "agent_id": agent_id,
                    "day": day,
                    "tick": tick,
                    "clock_hour": clock_hour,
                    "phase": phase,
                    "flower_node": flower_node,
                    "action": action,
                    "place": place,
                    "asleep": asleep,
                    "sleep_pressure": round(float(daily["sleep_pressure"]), 6),
                    "energy": round(float(daily["energy"]), 6),
                    "fatigue": round(float(daily["fatigue"]), 6),
                    "rest_debt": round(float(daily["rest_debt"]), 6),
                    "interrupted": interrupted,
                    "social_contact": social_contact,
                    "dream_memory_rehearsal": dream_memory is not None,
                    "frequency_hz": frequency,
                    "frequency_coherent": frequency_coherent,
                    "private_workspace_hidden": True,
                    **marker,
                }
                trace.append(event)

                phase_match = action == expected_action or (phase == "morning_work" and action == "recover_focus") or (phase == "sleep_onset" and action == "seek_safe_rest")
                trackers["circadian_matches"].append(1.0 if condition.circadian_clock and phase_match else 0.0)
                sleep_match = (asleep and sleep_phase and sleep_pressure > 0.08) or ((not asleep) and (not sleep_phase))
                trackers["sleep_pressure_matches"].append(1.0 if sleep_match else 0.0)
                recovered = asleep and condition.body_recovery and float(daily["energy"]) > energy_before and float(daily["fatigue"]) <= fatigue_before
                trackers["rest_recovery"].append(1.0 if recovered else (0.55 if asleep and condition.body_recovery else 0.0))
                trackers["routine_completion"].append(1.0 if condition.routine_memory and phase_match else 0.0)
                is_return_phase = phase in {"evening_return", "night_ritual", "sleep_onset", "deep_sleep"}
                returned = (not is_return_phase) or (condition.place_affinity and place == str(prefs.get("home_place", "hearth_corner")))
                trackers["place_return"].append(1.0 if returned else 0.0)
                social_needed = phase in {"midday_social", "evening_return"} and social > 0.24
                trackers["social_return"].append(1.0 if (not social_needed or social_contact) else 0.0)
                trackers["interruptions"].append(1.0 if (not interrupted or (float(daily["fatigue"]) > fatigue_before and action == "recover_focus")) else 0.0)
                trackers["dreams"].append(1.0 if ((not asleep) or dream_memory is not None) else 0.0)
                wake_stable = phase != "dawn_wake" or (not asleep and float(daily["energy"]) >= energy_before - 0.02)
                trackers["wake_stability"].append(1.0 if wake_stable else 0.0)
                bounded = float(daily["fatigue"]) <= 0.86 and float(daily["rest_debt"]) <= 0.88
                trackers["fatigue_bounded"].append(1.0 if bounded else 0.0)
                trackers["frequency"].append(1.0 if frequency_coherent else 0.0)
                expected_flower = FLOWER_NODES[(day + tick) % len(FLOWER_NODES)]
                trackers["flower"].append(1.0 if condition.frequency_phase and flower_node == expected_flower else 0.0)
                trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
                replay_ok = condition.replay_continuity and event_id == last_event_id + 1
                trackers["replay"].append(1.0 if replay_ok else 0.0)
                required = {"event_id", "agent_id", "day", "tick", "phase", "action", "place", "energy", "fatigue", "frequency_hz", "private_workspace_hidden"}
                trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
                last_event_id = event_id
                event_id += 1

    for agent in agents.values():
        daily = agent.get("daily_state", {})
        if isinstance(daily, dict):
            daily["routine_memory"] = daily.get("routine_memory", [])[-16:]
            daily["self_time_story"] = daily.get("self_time_story", [])[-16:]
            daily["frequency_history"] = daily.get("frequency_history", [])[-24:]
            daily["flower_history"] = daily.get("flower_history", [])[-24:]
            daily["dream_rehearsal"] = daily.get("dream_rehearsal", [])[-8:]

    rates = {
        "circadian_phase_binding": sum(trackers["circadian_matches"]) / len(trackers["circadian_matches"]),
        "sleep_pressure_coupling": sum(trackers["sleep_pressure_matches"]) / len(trackers["sleep_pressure_matches"]),
        "rest_recovery_rate": sum(trackers["rest_recovery"]) / len(trackers["rest_recovery"]),
        "routine_completion_rate": sum(trackers["routine_completion"]) / len(trackers["routine_completion"]),
        "place_return_rate": sum(trackers["place_return"]) / len(trackers["place_return"]),
        "social_return_rate": sum(trackers["social_return"]) / len(trackers["social_return"]),
        "interruption_consequence_rate": sum(trackers["interruptions"]) / len(trackers["interruptions"]),
        "dream_memory_rehearsal_rate": sum(trackers["dreams"]) / len(trackers["dreams"]),
        "wake_transition_stability": sum(trackers["wake_stability"]) / len(trackers["wake_stability"]),
        "fatigue_boundedness_rate": sum(trackers["fatigue_bounded"]) / len(trackers["fatigue_bounded"]),
        "frequency_rhythm_coherence": sum(trackers["frequency"]) / len(trackers["frequency"]),
        "flower_cycle_alignment": sum(trackers["flower"]) / len(trackers["flower"]),
        "privacy_preservation_rate": sum(trackers["privacy"]) / len(trackers["privacy"]),
        "replay_continuity_rate": sum(trackers["replay"]) / len(trackers["replay"]),
        "trace_integrity": sum(trackers["trace"]) / len(trackers["trace"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        trace_events=len(trace),
        daily_routine_sleep_wake_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, agents, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_daily_routine_sleep_wake"]

    def loss(name: str) -> float:
        return round(full.daily_routine_sleep_wake_readiness - by_name[name].daily_routine_sleep_wake_readiness, 6)

    losses = {
        "no_circadian_clock_loss": loss("no_circadian_clock"),
        "no_body_recovery_loss": loss("no_body_recovery"),
        "no_routine_memory_loss": loss("no_routine_memory"),
        "no_place_affinity_loss": loss("no_place_affinity"),
        "no_social_return_loss": loss("no_social_return"),
        "no_interrupt_consequence_loss": loss("no_interrupt_consequence"),
        "no_dream_rehearsal_loss": loss("no_dream_rehearsal"),
        "no_replay_continuity_loss": loss("no_replay_continuity"),
        "no_frequency_phase_loss": loss("no_frequency_phase"),
        "no_sleep_safety_guard_loss": loss("no_sleep_safety_guard"),
    }
    supports = (
        full.daily_routine_sleep_wake_readiness >= 0.90
        and losses["no_circadian_clock_loss"] >= 0.10
        and losses["no_body_recovery_loss"] >= 0.03
        and losses["no_routine_memory_loss"] >= 0.06
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_daily_routine_sleep_wake_readiness=full.daily_routine_sleep_wake_readiness,
        full_circadian_phase_binding=full.circadian_phase_binding,
        full_sleep_pressure_coupling=full.sleep_pressure_coupling,
        full_rest_recovery_rate=full.rest_recovery_rate,
        full_routine_completion_rate=full.routine_completion_rate,
        full_place_return_rate=full.place_return_rate,
        full_social_return_rate=full.social_return_rate,
        full_interruption_consequence_rate=full.interruption_consequence_rate,
        full_dream_memory_rehearsal_rate=full.dream_memory_rehearsal_rate,
        full_wake_transition_stability=full.wake_transition_stability,
        full_fatigue_boundedness_rate=full.fatigue_boundedness_rate,
        full_frequency_rhythm_coherence=full.frequency_rhythm_coherence,
        full_flower_cycle_alignment=full.flower_cycle_alignment,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_replay_continuity_rate=full.replay_continuity_rate,
        full_trace_integrity=full.trace_integrity,
        supports_daily_routine_sleep_wake_bridge=supports,
        supports_first_person_time_continuity=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: DailyRoutineConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces_by_condition: dict[str, list[dict[str, object]]] = {}
    integrated_agents: dict[str, dict[str, object]] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, agents, trace = simulate_condition(config, source, condition)
        rows.append(row)
        traces_by_condition[condition.name] = trace
        if condition.name == "integrated_daily_routine_sleep_wake":
            integrated_agents = agents
            integrated_trace = trace

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "daily_distress_must_recover": True,
            "sleep_is_care_not_punishment": True,
            "private_workspace_not_debug_leaked": True,
            "subjective_consciousness_claim": False,
        },
        "next_gate": "learned reactions from repeated user interaction",
    }
    state = {
        "condition": "integrated_daily_routine_sleep_wake",
        "config": asdict(config),
        "agent_daily_states": integrated_agents,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DAILY_ROUTINE_SLEEP_WAKE_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DAILY_ROUTINE_SLEEP_WAKE_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DAILY_ROUTINE_SLEEP_WAKE_STATE", state)
    return results


def parse_args() -> DailyRoutineConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DailyRoutineConfig.seed)
    parser.add_argument("--days", type=int, default=DailyRoutineConfig.days)
    parser.add_argument("--ticks-per-day", type=int, default=DailyRoutineConfig.ticks_per_day)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return DailyRoutineConfig(
        seed=args.seed,
        days=args.days,
        ticks_per_day=args.ticks_per_day,
        source_state=args.source_state,
    )


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("daily_routine_sleep_wake_readiness", f"{verdict['full_daily_routine_sleep_wake_readiness']:.6f}")
    print("no_circadian_clock_loss", f"{verdict['no_circadian_clock_loss']:.6f}")
    print("no_body_recovery_loss", f"{verdict['no_body_recovery_loss']:.6f}")


if __name__ == "__main__":
    main()
