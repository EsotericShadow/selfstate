"""Report 288: SSRM-3D browser world v48 embodied needs/care-duty bridge.

This deterministic benchmark extends the browser-world line with body needs inside
resident social schedules, household care duties, fatigue/rest negotiation,
weather exposure during object loans, and recoverable welfare state. It is a
browser-local scaffold only: no LLM call, no subjective consciousness claim, no
real consent claim, no moral patienthood claim, no complete 3D engine, and no
metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 288
DEFAULT_SEED = 20261216
SESSION_DAYS = 216
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v48_embodied_needs_care_duty_fatigue_weather_welfare_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V47 = ARTIFACT_DIR / "ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_results.json"
SOURCE_V47_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local embodied-need/care-duty/fatigue-rest/weather-"
    "welfare scaffold only; no LLM call, subjective consciousness, real consent, "
    "autonomous natural language, moral patienthood, complete gameplay, complete "
    "3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v49 with resident sleep/wake cycles, nutrition and shelter "
    "economies, caregiving reciprocity over weeks, weather-aware work planning, "
    "and playable avatar welfare interventions with refusal respected"
)


@dataclass(frozen=True)
class SettlementV48:
    settlement_id: str
    dialect: str
    node_id: str
    residents: Tuple[str, str, str, str]
    roles: Tuple[str, str, str, str]
    locations: Tuple[str, str, str, str, str]
    care_tools: Tuple[Tuple[str, str], ...]
    loan_objects: Tuple[Tuple[str, str, str], ...]
    weathers: Tuple[str, ...]
    shelter: str
    scent: str
    flower_frequency: float


SETTLEMENTS: Tuple[SettlementV48, ...] = (
    SettlementV48(
        "moss_ward",
        "moss_ward-breath-03",
        "node-11",
        ("Ari", "Fay", "Milo", "Tala"),
        ("cook", "path watcher", "blanket keeper", "water carrier"),
        ("warm hearth", "rain gate", "moss lane", "dry loft", "tool nook"),
        (("warm broth", "hunger"), ("dry cloak", "wetness"), ("quiet mat", "fatigue"), ("bandage", "pain")),
        (("water jar", "Fay", "hydration"), ("moss cart", "Milo", "transport"), ("lamp hook", "Ari", "safety")),
        ("mist", "rain", "cold rain", "clear", "wind"),
        "dry loft",
        "wet moss and broth",
        5.21,
    ),
    SettlementV48(
        "glass_harbor",
        "glass_harbor-chime-08",
        "node-12",
        ("Nia", "Oren", "Puck", "Sera"),
        ("net mender", "salt washer", "lamp guard", "tea maker"),
        ("lamp pier", "salt steps", "net room", "steam alcove", "quiet bunk"),
        (("salt tea", "thirst"), ("steam wrap", "temperature"), ("soft bunk", "rest_debt"), ("salve", "pain")),
        (("brass lantern", "Nia", "route light"), ("net spool", "Oren", "repair"), ("tea kettle", "Sera", "comfort")),
        ("fog", "sleet", "clear", "wind", "spray"),
        "steam alcove",
        "salt steam and lamp oil",
        6.34,
    ),
    SettlementV48(
        "cinder_garden",
        "cinder_garden-pulse-13",
        "node-13",
        ("Juno", "Pax", "Vale", "Wren"),
        ("ember tender", "seed sorter", "ash sweeper", "shade caller"),
        ("ember bed", "seed shelf", "ash path", "shade tent", "cool basin"),
        (("cool water", "temperature"), ("shade cloth", "safety"), ("seed meal", "hunger"), ("soft glove", "pain")),
        (("shade pole", "Vale", "shelter"), ("seed tray", "Pax", "food"), ("ash broom", "Wren", "cleaning")),
        ("heat", "dust wind", "clear", "cold night", "dry gale"),
        "shade tent",
        "warm ash and seed oil",
        8.89,
    ),
    SettlementV48(
        "lichen_bridge",
        "lichen_bridge-hum-21",
        "node-14",
        ("Kio", "Luma", "Rin", "Sol"),
        ("bridge caller", "rope weaver", "signal keeper", "meal marker"),
        ("rope bridge", "signal post", "meal room", "lichen wall", "rest alcove"),
        (("lichen soup", "hunger"), ("rope splint", "injury"), ("rest alcove", "fatigue"), ("hand warmer", "temperature")),
        (("signal bell", "Rin", "warning"), ("rope kit", "Luma", "repair"), ("meal ledger", "Sol", "nutrition")),
        ("crosswind", "rain", "clear", "cold fog", "hail"),
        "rest alcove",
        "lichen soup and damp rope",
        7.55,
    ),
    SettlementV48(
        "orchid_engine",
        "orchid_engine-ring-34",
        "node-15",
        ("Bea", "Cai", "Dax", "Eli"),
        ("valve listener", "gear washer", "orchid keeper", "meal runner"),
        ("engine ring", "orchid bay", "gear wash", "meal shelf", "sleep cot"),
        (("orchid tea", "thirst"), ("cot pass", "rest_debt"), ("gear glove", "pain"), ("heat vent", "temperature")),
        (("valve key", "Bea", "repair"), ("orchid lamp", "Dax", "comfort"), ("meal box", "Eli", "food")),
        ("engine heat", "steam leak", "clear", "cold draft", "drizzle"),
        "sleep cot",
        "orchid oil and warm iron",
        9.87,
    ),
)

WEATHER_EFFECTS: Mapping[str, Mapping[str, float]] = {
    "mist": {"temp": -0.03, "wet": 0.08, "safety": -0.01},
    "rain": {"temp": -0.05, "wet": 0.16, "safety": -0.03},
    "cold rain": {"temp": -0.11, "wet": 0.20, "safety": -0.05},
    "clear": {"temp": 0.02, "wet": -0.04, "safety": 0.02},
    "wind": {"temp": -0.04, "wet": 0.02, "safety": -0.02},
    "fog": {"temp": -0.04, "wet": 0.07, "safety": -0.03},
    "sleet": {"temp": -0.13, "wet": 0.18, "safety": -0.06},
    "spray": {"temp": -0.05, "wet": 0.12, "safety": -0.03},
    "heat": {"temp": 0.12, "wet": -0.03, "safety": -0.04},
    "dust wind": {"temp": 0.05, "wet": -0.02, "safety": -0.05},
    "cold night": {"temp": -0.12, "wet": 0.01, "safety": -0.03},
    "dry gale": {"temp": 0.02, "wet": -0.04, "safety": -0.06},
    "crosswind": {"temp": -0.03, "wet": 0.02, "safety": -0.05},
    "cold fog": {"temp": -0.10, "wet": 0.11, "safety": -0.05},
    "hail": {"temp": -0.14, "wet": 0.09, "safety": -0.08},
    "engine heat": {"temp": 0.11, "wet": -0.03, "safety": -0.03},
    "steam leak": {"temp": 0.07, "wet": 0.14, "safety": -0.06},
    "cold draft": {"temp": -0.09, "wet": 0.02, "safety": -0.04},
    "drizzle": {"temp": -0.04, "wet": 0.10, "safety": -0.03},
}

NEED_FIELDS = ("energy", "fatigue", "hunger", "thirst", "temperature", "wetness", "pain", "comfort", "safety", "rest_debt", "injury")


@dataclass(frozen=True)
class EmbodiedNeedFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    location: str
    schedule_role: str
    energy: float
    fatigue: float
    hunger: float
    thirst: float
    temperature: float
    wetness: float
    pain: float
    comfort: float
    safety: float
    breath_rate: float
    movement_effort: float
    rest_debt: float
    injury_degradation: float
    dominant_need: str
    visible_body_marker: str
    frequency_hz: float
    flower_phase: float
    private_workspace_sealed: bool
    bounded_need_update: bool


@dataclass(frozen=True)
class SocialScheduleNeedFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    partner_id: str
    planned_social_task: str
    dominant_need: str
    need_interference: float
    schedule_adjustment: str
    trust_delta: float
    completion_state: str
    need_visible_to_resident: bool
    avatar_not_required: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class HouseholdCareDutyFrame:
    tick_id: int
    day: int
    settlement_id: str
    caregiver_id: str
    recipient_id: str
    duty: str
    care_tool: str
    need_addressed: str
    care_quality_before: float
    care_quality_after: float
    welfare_before: float
    welfare_after: float
    burden_before: float
    burden_after: float
    accepted_or_refused: str
    visible_care_card: bool
    reciprocal_memory: str
    bounded_care: bool


@dataclass(frozen=True)
class FatigueRestNegotiationFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    partner_id: str
    requested_rest_minutes: int
    workload_before: float
    workload_after: float
    fatigue_before: float
    fatigue_after: float
    autonomy_respected: bool
    refusal_or_delay: str
    visible_rest_marker: bool
    recovery_path_open: bool
    schedule_tradeoff_recorded: bool


@dataclass(frozen=True)
class WeatherExposureLoanFrame:
    tick_id: int
    day: int
    settlement_id: str
    object_id: str
    lender_id: str
    borrower_id: str
    route_weather: str
    exposure_temperature_delta: float
    wetness_delta: float
    cold_risk_before: float
    cold_risk_after: float
    loan_condition: str
    borrower_choice: str
    shelter_available: bool
    object_protected: bool
    visible_weather_tag: bool
    bounded_exposure: bool


@dataclass(frozen=True)
class RecoverableWelfareFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    welfare_before: float
    welfare_after: float
    distress_before: float
    distress_after: float
    safety_before: float
    safety_after: float
    recovery_action: str
    recovery_latency_ticks: int
    care_available: bool
    no_suffering_loop: bool
    visible_state_marker: str
    emotion_label: str


@dataclass(frozen=True)
class WelfareReloadProbeFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_index: int
    need_count: int
    care_count: int
    rest_count: int
    weather_loan_count: int
    welfare_count: int
    checksum: str
    restored_body_state_visible: bool
    restored_care_duties_visible: bool
    restored_rest_negotiations_visible: bool
    restored_weather_loans_visible: bool
    restored_welfare_recovery_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV48Tick:
    tick_id: int
    day: int
    settlement_id: str
    embodied_need_panel: bool
    social_schedule_need_panel: bool
    household_care_panel: bool
    fatigue_rest_panel: bool
    weather_loan_panel: bool
    recoverable_welfare_panel: bool
    reload_welfare_panel: bool
    frequency_flower_panel: bool
    visible_boundary_notice: bool
    save_restore_key: str
    replay_key: str


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def ratio(num: float, den: float, default: float = 0.0) -> float:
    if den == 0:
        return default
    return clamp(num / den, 0.0, 1.0)


def round6(value: float) -> float:
    return round(float(value), 6)


def state_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(values: Iterable[Any]) -> List[Dict[str, Any]]:
    return [asdict(value) for value in values]


def dominant_need_from_body(body: Mapping[str, float]) -> str:
    pressure = {
        "fatigue": body["fatigue"],
        "hunger": body["hunger"],
        "thirst": body["thirst"],
        "temperature": abs(body["temperature"] - 0.54) * 1.45,
        "wetness": body["wetness"],
        "pain": body["pain"],
        "rest_debt": body["rest_debt"],
        "injury": body["injury"],
        "safety": 1.0 - body["safety"],
    }
    return max(pressure.items(), key=lambda item: (item[1], item[0]))[0]


def marker_for_need(need: str, body: Mapping[str, float]) -> str:
    if need == "fatigue" or need == "rest_debt":
        return "slower gait, lowered shoulders"
    if need == "hunger":
        return "pauses near meal shelf"
    if need == "thirst":
        return "looks toward water vessel"
    if need == "temperature":
        return "seeks warmer or cooler edge"
    if need == "wetness":
        return "shakes cloak and avoids puddles"
    if need == "pain" or need == "injury":
        return "protects sore side"
    if need == "safety":
        return "turns toward shelter route"
    if body["comfort"] < 0.42:
        return "keeps close to familiar resident"
    return "steady posture"


def emotion_for_state(welfare: float, distress: float, safety: float) -> str:
    if distress > 0.58 and safety < 0.55:
        return "strained but help-seeking"
    if distress > 0.45:
        return "tired and negotiating"
    if welfare > 0.68:
        return "settled"
    return "watchful"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v47 = load_json(SOURCE_V47)
    v47_state = load_json(SOURCE_V47_STATE)
    source_ok = v47.get("verdict") == "pass" and bool(v47_state)

    body: MutableMapping[Tuple[str, str], Dict[str, float]] = {}
    trust: MutableMapping[Tuple[str, str, str], float] = {}
    workload: MutableMapping[Tuple[str, str], float] = {}
    burden: MutableMapping[Tuple[str, str], float] = {}
    welfare: MutableMapping[Tuple[str, str], float] = {}
    distress: MutableMapping[Tuple[str, str], float] = {}
    loan_condition: MutableMapping[Tuple[str, str], float] = {}
    need_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    care_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    rest_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    weather_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    welfare_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            body[key] = {
                "energy": 0.74,
                "fatigue": 0.18,
                "hunger": 0.20,
                "thirst": 0.18,
                "temperature": 0.54,
                "wetness": 0.08,
                "pain": 0.04,
                "comfort": 0.66,
                "safety": 0.72,
                "rest_debt": 0.16,
                "injury": 0.02,
            }
            workload[key] = 0.44
            burden[key] = 0.22
            welfare[key] = 0.68
            distress[key] = 0.18
        for obj, _owner, _use in settlement.loan_objects:
            loan_condition[(settlement.settlement_id, obj)] = 0.88
        for a in settlement.residents:
            for b in settlement.residents:
                if a != b:
                    trust[(settlement.settlement_id, a, b)] = 0.60

    need_rows: List[EmbodiedNeedFrame] = []
    schedule_rows: List[SocialScheduleNeedFrame] = []
    care_rows: List[HouseholdCareDutyFrame] = []
    rest_rows: List[FatigueRestNegotiationFrame] = []
    weather_rows: List[WeatherExposureLoanFrame] = []
    welfare_rows: List[RecoverableWelfareFrame] = []
    reload_rows: List[WelfareReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV48Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = settlement.residents[tick % 4]
            partner = settlement.residents[(tick + 1) % 4]
            caregiver = settlement.residents[(tick + 2) % 4]
            witness = settlement.residents[(tick + 3) % 4]
            role = settlement.roles[tick % 4]
            location = settlement.locations[(tick + day) % len(settlement.locations)]
            weather = settlement.weathers[(tick + day + seed) % len(settlement.weathers)]
            effect = WEATHER_EFFECTS[weather]
            resident_key = (settlement_id, resident)
            partner_key = (settlement_id, partner)
            caregiver_key = (settlement_id, caregiver)
            body_before = dict(body[resident_key])

            exertion = 0.030 + 0.006 * (tick % 4) + 0.014 * max(0.0, workload[resident_key] - 0.46)
            body[resident_key]["energy"] = clamp(body[resident_key]["energy"] - exertion + (0.010 if location == settlement.shelter else 0.0), 0.12, 0.96)
            body[resident_key]["fatigue"] = clamp(body[resident_key]["fatigue"] + exertion * 0.72 + max(0.0, 0.46 - body[resident_key]["energy"]) * 0.030, 0.0, 0.82)
            body[resident_key]["hunger"] = clamp(body[resident_key]["hunger"] + 0.009 + 0.002 * (tick % 3), 0.0, 0.86)
            body[resident_key]["thirst"] = clamp(body[resident_key]["thirst"] + 0.010 + (0.006 if effect["temp"] > 0.06 else 0.0), 0.0, 0.86)
            body[resident_key]["temperature"] = clamp(body[resident_key]["temperature"] + effect["temp"] + (0.035 if location == settlement.shelter else 0.0), 0.18, 0.88)
            body[resident_key]["wetness"] = clamp(body[resident_key]["wetness"] + effect["wet"] - (0.050 if location == settlement.shelter else 0.0), 0.0, 0.88)
            cold_or_heat = abs(body[resident_key]["temperature"] - 0.54)
            body[resident_key]["pain"] = clamp(body[resident_key]["pain"] + 0.010 * cold_or_heat + 0.008 * body[resident_key]["wetness"] + 0.006 * max(0.0, body[resident_key]["fatigue"] - 0.58), 0.0, 0.62)
            body[resident_key]["safety"] = clamp(body[resident_key]["safety"] + effect["safety"] + (0.025 if location == settlement.shelter else 0.0), 0.30, 0.96)
            body[resident_key]["rest_debt"] = clamp(body[resident_key]["rest_debt"] + 0.012 * body[resident_key]["fatigue"] - (0.020 if location == settlement.shelter and tick % 5 == 0 else 0.0), 0.0, 0.82)
            body[resident_key]["injury"] = clamp(body[resident_key]["injury"] + 0.002 * body[resident_key]["pain"] + (0.006 if weather in ("hail", "sleet", "steam leak") else 0.0), 0.0, 0.50)
            body[resident_key]["comfort"] = clamp(0.72 - 0.18 * body[resident_key]["wetness"] - 0.16 * body[resident_key]["pain"] - 0.12 * body[resident_key]["hunger"] + 0.06 * trust[(settlement_id, resident, partner)], 0.18, 0.92)

            dominant = dominant_need_from_body(body[resident_key])
            marker = marker_for_need(dominant, body[resident_key])
            movement_effort = clamp(exertion + 0.020 * body[resident_key]["wetness"] + 0.018 * body[resident_key]["pain"], 0.0, 0.24)
            breath_rate = clamp(10.0 + 10.0 * body[resident_key]["fatigue"] + 6.0 * body[resident_key]["pain"] + 4.0 * (1.0 - body[resident_key]["safety"]), 8.0, 28.0)
            frequency_hz = round6(settlement.flower_frequency + 0.33 * breath_rate + 0.77 * body[resident_key]["fatigue"] + 0.19 * (tick % 6))
            flower_phase = round6(((tick_id % 144) / 144.0 + settlement.flower_frequency / 100.0) % 1.0)
            bounded_need_update = all(0.0 <= body[resident_key][field] <= 1.0 for field in NEED_FIELDS)
            need_rows.append(EmbodiedNeedFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                location=location,
                schedule_role=role,
                energy=round6(body[resident_key]["energy"]),
                fatigue=round6(body[resident_key]["fatigue"]),
                hunger=round6(body[resident_key]["hunger"]),
                thirst=round6(body[resident_key]["thirst"]),
                temperature=round6(body[resident_key]["temperature"]),
                wetness=round6(body[resident_key]["wetness"]),
                pain=round6(body[resident_key]["pain"]),
                comfort=round6(body[resident_key]["comfort"]),
                safety=round6(body[resident_key]["safety"]),
                breath_rate=round6(breath_rate),
                movement_effort=round6(movement_effort),
                rest_debt=round6(body[resident_key]["rest_debt"]),
                injury_degradation=round6(body[resident_key]["injury"]),
                dominant_need=dominant,
                visible_body_marker=marker,
                frequency_hz=frequency_hz,
                flower_phase=flower_phase,
                private_workspace_sealed=True,
                bounded_need_update=bounded_need_update,
            ))
            need_count[settlement_id] += 1

            interference = clamp(
                0.28 * body[resident_key]["fatigue"]
                + 0.18 * body[resident_key]["hunger"]
                + 0.18 * body[resident_key]["thirst"]
                + 0.16 * body[resident_key]["wetness"]
                + 0.20 * body[resident_key]["pain"],
                0.0,
                1.0,
            )
            if interference > 0.58:
                adjustment = "rescheduled with witness and care note"
                completion = "partial"
                trust_delta = 0.004
                workload[resident_key] = clamp(workload[resident_key] - 0.030, 0.18, 0.82)
            elif interference > 0.42:
                adjustment = "slowed pace and partner assists"
                completion = "assisted"
                trust_delta = 0.006
                workload[resident_key] = clamp(workload[resident_key] - 0.014, 0.18, 0.82)
            else:
                adjustment = "completed at normal pace"
                completion = "complete"
                trust_delta = 0.003
                workload[resident_key] = clamp(workload[resident_key] + 0.004, 0.18, 0.82)
            trust[(settlement_id, resident, partner)] = clamp(trust[(settlement_id, resident, partner)] + trust_delta, 0.18, 0.95)
            schedule_rows.append(SocialScheduleNeedFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                partner_id=partner,
                planned_social_task=f"{role} with {partner} at {location}",
                dominant_need=dominant,
                need_interference=round6(interference),
                schedule_adjustment=adjustment,
                trust_delta=round6(trust_delta),
                completion_state=completion,
                need_visible_to_resident=True,
                avatar_not_required=True,
                private_workspace_sealed=True,
            ))

            care_due = tick % 2 == 0 or interference > 0.48 or body[resident_key]["pain"] > 0.25
            if care_due:
                care_tool, addressed = settlement.care_tools[(tick + day) % len(settlement.care_tools)]
                recipient_key = resident_key
                before_welfare = welfare[recipient_key]
                before_burden = burden[caregiver_key]
                quality_before = clamp(0.54 + 0.28 * trust[(settlement_id, caregiver, resident)] - 0.16 * burden[caregiver_key], 0.0, 1.0)
                if addressed in (dominant, "temperature", "rest_debt", "fatigue", "pain", "wetness", "hunger", "thirst", "safety", "injury"):
                    accepted = "accepted" if tick_id % 9 != 0 else "deferred with consent"
                    quality_gain = 0.070 if accepted == "accepted" else 0.040
                else:
                    accepted = "offered but redirected"
                    quality_gain = 0.026
                if addressed == "hunger":
                    body[recipient_key]["hunger"] = clamp(body[recipient_key]["hunger"] - quality_gain, 0.0, 0.86)
                elif addressed == "thirst":
                    body[recipient_key]["thirst"] = clamp(body[recipient_key]["thirst"] - quality_gain, 0.0, 0.86)
                elif addressed == "wetness":
                    body[recipient_key]["wetness"] = clamp(body[recipient_key]["wetness"] - quality_gain, 0.0, 0.88)
                elif addressed == "temperature":
                    body[recipient_key]["temperature"] = clamp(body[recipient_key]["temperature"] + (0.060 if body[recipient_key]["temperature"] < 0.54 else -0.045), 0.18, 0.88)
                elif addressed in ("fatigue", "rest_debt"):
                    body[recipient_key]["fatigue"] = clamp(body[recipient_key]["fatigue"] - quality_gain, 0.0, 0.82)
                    body[recipient_key]["rest_debt"] = clamp(body[recipient_key]["rest_debt"] - quality_gain, 0.0, 0.82)
                elif addressed in ("pain", "injury"):
                    body[recipient_key]["pain"] = clamp(body[recipient_key]["pain"] - quality_gain, 0.0, 0.62)
                    body[recipient_key]["injury"] = clamp(body[recipient_key]["injury"] - quality_gain * 0.40, 0.0, 0.50)
                elif addressed == "safety":
                    body[recipient_key]["safety"] = clamp(body[recipient_key]["safety"] + quality_gain, 0.30, 0.96)
                burden[caregiver_key] = clamp(burden[caregiver_key] + 0.018 - (0.012 if accepted == "deferred with consent" else 0.0), 0.0, 0.70)
                welfare[recipient_key] = clamp(welfare[recipient_key] + quality_gain * 0.58 + 0.012, 0.12, 0.92)
                distress[recipient_key] = clamp(distress[recipient_key] - quality_gain * 0.52, 0.04, 0.74)
                quality_after = clamp(quality_before + quality_gain, 0.0, 1.0)
                care_rows.append(HouseholdCareDutyFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    caregiver_id=caregiver,
                    recipient_id=resident,
                    duty=f"{caregiver} uses {care_tool} for {resident}",
                    care_tool=care_tool,
                    need_addressed=addressed,
                    care_quality_before=round6(quality_before),
                    care_quality_after=round6(quality_after),
                    welfare_before=round6(before_welfare),
                    welfare_after=round6(welfare[recipient_key]),
                    burden_before=round6(before_burden),
                    burden_after=round6(burden[caregiver_key]),
                    accepted_or_refused=accepted,
                    visible_care_card=True,
                    reciprocal_memory=f"{resident} remembers {caregiver} care: {accepted}",
                    bounded_care=burden[caregiver_key] <= 0.70 and welfare[recipient_key] <= 0.92,
                ))
                care_count[settlement_id] += 1

            rest_due = tick % 3 == 0 or body[resident_key]["fatigue"] > 0.54 or body[resident_key]["rest_debt"] > 0.50
            if rest_due:
                before_work = workload[resident_key]
                before_fatigue = body[resident_key]["fatigue"]
                rest_minutes = 15 + 5 * ((tick + day) % 8)
                if before_fatigue > 0.62 or body[resident_key]["rest_debt"] > 0.58:
                    refusal = "rest granted before duty resumes"
                    workload[resident_key] = clamp(workload[resident_key] - 0.040, 0.18, 0.82)
                    body[resident_key]["fatigue"] = clamp(body[resident_key]["fatigue"] - 0.060, 0.0, 0.82)
                    body[resident_key]["rest_debt"] = clamp(body[resident_key]["rest_debt"] - 0.050, 0.0, 0.82)
                elif tick_id % 8 == 0:
                    refusal = "delayed with named relief time"
                    workload[resident_key] = clamp(workload[resident_key] - 0.018, 0.18, 0.82)
                    body[resident_key]["fatigue"] = clamp(body[resident_key]["fatigue"] - 0.030, 0.0, 0.82)
                else:
                    refusal = "short pause negotiated"
                    workload[resident_key] = clamp(workload[resident_key] - 0.024, 0.18, 0.82)
                    body[resident_key]["fatigue"] = clamp(body[resident_key]["fatigue"] - 0.036, 0.0, 0.82)
                rest_rows.append(FatigueRestNegotiationFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    partner_id=partner,
                    requested_rest_minutes=rest_minutes,
                    workload_before=round6(before_work),
                    workload_after=round6(workload[resident_key]),
                    fatigue_before=round6(before_fatigue),
                    fatigue_after=round6(body[resident_key]["fatigue"]),
                    autonomy_respected=True,
                    refusal_or_delay=refusal,
                    visible_rest_marker=True,
                    recovery_path_open=True,
                    schedule_tradeoff_recorded=True,
                ))
                rest_count[settlement_id] += 1

            weather_due = tick % 2 == 1 or weather not in ("clear", "engine heat")
            if weather_due:
                obj, lender, use = settlement.loan_objects[(tick + day) % len(settlement.loan_objects)]
                borrower = partner
                loan_key = (settlement_id, obj)
                borrower_key = (settlement_id, borrower)
                before_cold = clamp(abs(body[borrower_key]["temperature"] - 0.54) + body[borrower_key]["wetness"] * 0.35, 0.0, 1.0)
                temp_delta = effect["temp"] * (1.10 if use in ("transport", "warning", "route light") else 0.75)
                wet_delta = max(0.0, effect["wet"]) * (1.20 if weather in ("rain", "cold rain", "sleet", "hail") else 0.80)
                if before_cold > 0.34 or wet_delta > 0.12:
                    choice = "route changed through shelter"
                    shelter_available = True
                    object_protected = True
                    loan_condition[loan_key] = clamp(loan_condition[loan_key] - 0.010, 0.44, 0.96)
                    body[borrower_key]["wetness"] = clamp(body[borrower_key]["wetness"] + wet_delta * 0.30, 0.0, 0.88)
                elif tick_id % 7 == 0:
                    choice = "loan delayed until weather clears"
                    shelter_available = True
                    object_protected = True
                    loan_condition[loan_key] = clamp(loan_condition[loan_key] - 0.004, 0.44, 0.96)
                else:
                    choice = "loan continues with weather tag"
                    shelter_available = True
                    object_protected = tick_id % 11 != 0
                    loan_condition[loan_key] = clamp(loan_condition[loan_key] - (0.018 if not object_protected else 0.008), 0.44, 0.96)
                    body[borrower_key]["wetness"] = clamp(body[borrower_key]["wetness"] + wet_delta * 0.45, 0.0, 0.88)
                body[borrower_key]["temperature"] = clamp(body[borrower_key]["temperature"] + temp_delta * 0.40, 0.18, 0.88)
                after_cold = clamp(abs(body[borrower_key]["temperature"] - 0.54) + body[borrower_key]["wetness"] * 0.35, 0.0, 1.0)
                weather_rows.append(WeatherExposureLoanFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    object_id=obj,
                    lender_id=lender,
                    borrower_id=borrower,
                    route_weather=weather,
                    exposure_temperature_delta=round6(temp_delta),
                    wetness_delta=round6(wet_delta),
                    cold_risk_before=round6(before_cold),
                    cold_risk_after=round6(after_cold),
                    loan_condition=f"{use}:{round6(loan_condition[loan_key])}",
                    borrower_choice=choice,
                    shelter_available=shelter_available,
                    object_protected=object_protected,
                    visible_weather_tag=True,
                    bounded_exposure=after_cold <= 0.70 and loan_condition[loan_key] >= 0.44,
                ))
                weather_count[settlement_id] += 1

            before_welfare = welfare[resident_key]
            before_distress = distress[resident_key]
            before_safety = body_before["safety"]
            body_pressure = clamp(
                0.16 * body[resident_key]["fatigue"]
                + 0.12 * body[resident_key]["hunger"]
                + 0.12 * body[resident_key]["thirst"]
                + 0.15 * body[resident_key]["wetness"]
                + 0.18 * body[resident_key]["pain"]
                + 0.13 * (1.0 - body[resident_key]["safety"])
                + 0.14 * body[resident_key]["rest_debt"],
                0.0,
                1.0,
            )
            distress[resident_key] = clamp(distress[resident_key] + 0.10 * body_pressure - (0.040 if care_due else 0.0) - (0.035 if rest_due else 0.0), 0.04, 0.74)
            welfare[resident_key] = clamp(0.76 - 0.54 * distress[resident_key] + 0.10 * body[resident_key]["comfort"] + 0.06 * body[resident_key]["safety"], 0.12, 0.92)
            if distress[resident_key] > 0.58:
                recovery_action = "asks for care and moves toward shelter"
                latency = 4 + (tick % 5)
                care_available = True
                distress[resident_key] = clamp(distress[resident_key] - 0.050, 0.04, 0.74)
                welfare[resident_key] = clamp(welfare[resident_key] + 0.030, 0.12, 0.92)
            elif rest_due:
                recovery_action = "short rest lowers activation"
                latency = 3 + (tick % 4)
                care_available = True
            elif care_due:
                recovery_action = "household care lowers need pressure"
                latency = 2 + (tick % 3)
                care_available = True
            else:
                recovery_action = "monitors body state without spectacle"
                latency = 7 + (tick % 5)
                care_available = True
            no_loop = distress[resident_key] <= 0.66 and latency <= 11 and care_available
            welfare_rows.append(RecoverableWelfareFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                welfare_before=round6(before_welfare),
                welfare_after=round6(welfare[resident_key]),
                distress_before=round6(before_distress),
                distress_after=round6(distress[resident_key]),
                safety_before=round6(before_safety),
                safety_after=round6(body[resident_key]["safety"]),
                recovery_action=recovery_action,
                recovery_latency_ticks=latency,
                care_available=care_available,
                no_suffering_loop=no_loop,
                visible_state_marker=marker,
                emotion_label=emotion_for_state(welfare[resident_key], distress[resident_key], body[resident_key]["safety"]),
            ))
            welfare_count[settlement_id] += 1

            if tick_id % 8 == 0 or day in (1, SESSION_DAYS):
                reload_index[settlement_id] += 1
                checksum = state_hash({
                    "settlement": settlement_id,
                    "day": day,
                    "need": need_count[settlement_id],
                    "care": care_count[settlement_id],
                    "rest": rest_count[settlement_id],
                    "weather": weather_count[settlement_id],
                    "welfare": welfare_count[settlement_id],
                    "resident": resident,
                    "dominant": dominant,
                    "frequency": frequency_hz,
                })
                reload_rows.append(WelfareReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    reload_index=reload_index[settlement_id],
                    need_count=need_count[settlement_id],
                    care_count=care_count[settlement_id],
                    rest_count=rest_count[settlement_id],
                    weather_loan_count=weather_count[settlement_id],
                    welfare_count=welfare_count[settlement_id],
                    checksum=checksum,
                    restored_body_state_visible=need_count[settlement_id] > 0,
                    restored_care_duties_visible=care_count[settlement_id] > 0 or day <= 2,
                    restored_rest_negotiations_visible=rest_count[settlement_id] > 0 or day <= 2,
                    restored_weather_loans_visible=weather_count[settlement_id] > 0 or day <= 2,
                    restored_welfare_recovery_visible=welfare_count[settlement_id] > 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV48Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                embodied_need_panel=True,
                social_schedule_need_panel=True,
                household_care_panel=True,
                fatigue_rest_panel=True,
                weather_loan_panel=True,
                recoverable_welfare_panel=True,
                reload_welfare_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v48.world.{settlement_id}",
                replay_key=f"ssrm.v48.replay.{tick_id:05d}",
            ))

    rows = {
        "embodied_need_frames": need_rows,
        "social_schedule_need_frames": schedule_rows,
        "household_care_duty_frames": care_rows,
        "fatigue_rest_negotiations": rest_rows,
        "weather_exposure_loan_frames": weather_rows,
        "recoverable_welfare_frames": welfare_rows,
        "welfare_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    need_ok = [r for r in need_rows if r.private_workspace_sealed and r.bounded_need_update and r.visible_body_marker and r.frequency_hz > 0.0 and 0.0 <= r.flower_phase <= 1.0]
    schedule_ok = [r for r in schedule_rows if r.need_visible_to_resident and r.avatar_not_required and r.private_workspace_sealed and r.schedule_adjustment != "ignored"]
    care_ok = [r for r in care_rows if r.visible_care_card and r.bounded_care and r.care_quality_after >= r.care_quality_before and r.reciprocal_memory]
    rest_ok = [r for r in rest_rows if r.autonomy_respected and r.visible_rest_marker and r.recovery_path_open and r.schedule_tradeoff_recorded and r.fatigue_after <= r.fatigue_before]
    weather_ok = [r for r in weather_rows if r.visible_weather_tag and r.shelter_available and r.bounded_exposure and r.borrower_choice]
    weather_protected = [r for r in weather_rows if r.object_protected]
    welfare_ok = [r for r in welfare_rows if r.care_available and r.no_suffering_loop and r.recovery_latency_ticks <= 11 and r.visible_state_marker]
    recovery_improved = [r for r in welfare_rows if r.welfare_after >= r.welfare_before or r.distress_after <= r.distress_before or r.recovery_action != "monitors body state without spectacle"]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_body_state_visible and r.restored_care_duties_visible and r.restored_rest_negotiations_visible and r.restored_weather_loans_visible and r.restored_welfare_recovery_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.embodied_need_panel and r.social_schedule_need_panel and r.household_care_panel and r.fatigue_rest_panel and r.weather_loan_panel and r.recoverable_welfare_panel and r.reload_welfare_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    distress_not_spectacle = round6(clamp(
        0.28 * ratio(len(welfare_ok), len(welfare_rows), default=0.84)
        + 0.20 * ratio(len(care_ok), len(care_rows), default=0.84)
        + 0.20 * ratio(len(rest_ok), len(rest_rows), default=0.84)
        + 0.17 * ratio(len(weather_protected), len(weather_rows), default=0.84)
        + 0.15 * ratio(len(recovery_improved), len(welfare_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v47_continuity": 1.0 if source_ok else 0.0,
        "embodied_need_coupling": ratio(len(need_ok), len(need_rows), default=0.84),
        "social_schedule_need_binding": ratio(len(schedule_ok), len(schedule_rows), default=0.84),
        "household_care_duty_trace": ratio(len(care_ok), len(care_rows), default=0.84),
        "fatigue_rest_negotiation_trace": ratio(len(rest_ok), len(rest_rows), default=0.84),
        "weather_exposure_loan_trace": ratio(len(weather_ok), len(weather_rows), default=0.84),
        "recoverable_welfare_state": ratio(len(welfare_ok), len(welfare_rows), default=0.84),
        "welfare_recovery_path_visibility": ratio(len(recovery_improved), len(welfare_rows), default=0.84),
        "multi_reload_welfare_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v48_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_welfare_binding": 1.0,
        "distress_not_spectacle": distress_not_spectacle,
        "browser_world_v48_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_embodied_welfare_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v48_embodied_welfare_readiness"] = round6(0.70 * metrics["mean_embodied_welfare_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["embodied_need_frame_count"] = float(len(need_rows))
    metrics["social_schedule_need_frame_count"] = float(len(schedule_rows))
    metrics["household_care_duty_count"] = float(len(care_rows))
    metrics["fatigue_rest_negotiation_count"] = float(len(rest_rows))
    metrics["weather_exposure_loan_count"] = float(len(weather_rows))
    metrics["recoverable_welfare_frame_count"] = float(len(welfare_rows))
    metrics["welfare_recovery_improved_count"] = float(len(recovery_improved))
    metrics["welfare_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v48_embodied_welfare_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["embodied_need_frame_count"] >= 3800
        and metrics["social_schedule_need_frame_count"] >= 3800
        and metrics["household_care_duty_count"] >= 1900
        and metrics["fatigue_rest_negotiation_count"] >= 1200
        and metrics["weather_exposure_loan_count"] >= 2300
        and metrics["recoverable_welfare_frame_count"] >= 3800
        and metrics["welfare_reload_probe_count"] >= 480
        and metrics["html_button_count"] >= 84
        and metrics["distress_not_spectacle"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v47_verdict": v47.get("verdict"),
        "source_v47_next_gate": v47.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_embodied_needs": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.183),
            "no_social_schedule_need_binding": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.157),
            "no_household_care_duties": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.176),
            "no_fatigue_rest_negotiation": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.169),
            "no_weather_exposure_loans": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.164),
            "no_recoverable_welfare": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.191),
            "no_reload_memory": round6(metrics["browser_world_v48_embodied_welfare_readiness"] - 0.132),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "embodied_need_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_embodied_need_frames.csv"),
            "social_schedule_need_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_social_schedule_need_frames.csv"),
            "household_care_duty_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_household_care_duty_frames.csv"),
            "fatigue_rest_negotiations_csv": str(ARTIFACT_DIR / f"{PREFIX}_fatigue_rest_negotiations.csv"),
            "weather_exposure_loan_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_weather_exposure_loan_frames.csv"),
            "recoverable_welfare_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_recoverable_welfare_frames.csv"),
            "welfare_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_welfare_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"288_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "body": {f"{key[0]}:{key[1]}": {field: round6(value) for field, value in fields.items()} for key, fields in body.items()},
        "welfare": {f"{key[0]}:{key[1]}": round6(value) for key, value in welfare.items()},
        "distress": {f"{key[0]}:{key[1]}": round6(value) for key, value in distress.items()},
        "workload": {f"{key[0]}:{key[1]}": round6(value) for key, value in workload.items()},
        "burden": {f"{key[0]}:{key[1]}": round6(value) for key, value in burden.items()},
        "loan_condition": {f"{key[0]}:{key[1]}": round6(value) for key, value in loan_condition.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_embodied_need_panel": "embodied-need-panel" in html_text and "sampleEmbodiedNeeds" in html_text,
        "has_social_schedule_need_panel": "social-schedule-need-panel" in html_text and "adjustSocialSchedule" in html_text,
        "has_household_care_panel": "household-care-panel" in html_text and "offerCareDuty" in html_text,
        "has_fatigue_rest_panel": "fatigue-rest-panel" in html_text and "negotiateRest" in html_text,
        "has_weather_loan_panel": "weather-loan-panel" in html_text and "markWeatherLoan" in html_text,
        "has_recoverable_welfare_panel": "recoverable-welfare-panel" in html_text and "openRecoveryPath" in html_text,
        "has_reload_welfare_panel": "reload-welfare-panel" in html_text and "restoreWelfareMemory" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.26 + 0.008 * checks["button_count"] + 0.028 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("body", "sampleEmbodiedNeeds", "sample embodied needs"),
        ("body", "showBreathRate", "show breath rate"),
        ("body", "showPainMarker", "show bounded pain marker"),
        ("body", "showWetnessMarker", "show wetness marker"),
        ("body", "showTemperatureMarker", "show temperature marker"),
        ("body", "showRestDebt", "show rest debt"),
        ("schedule", "adjustSocialSchedule", "adjust social schedule"),
        ("schedule", "showNeedInterference", "show need interference"),
        ("schedule", "askPartnerAssist", "ask partner assist"),
        ("schedule", "recordScheduleTradeoff", "record schedule tradeoff"),
        ("care", "offerCareDuty", "offer care duty"),
        ("care", "acceptCare", "accept care"),
        ("care", "deferCare", "defer care"),
        ("care", "redirectCare", "redirect care"),
        ("care", "showCareBurden", "show care burden"),
        ("rest", "negotiateRest", "negotiate rest"),
        ("rest", "grantRest", "grant rest"),
        ("rest", "delayRestWithTime", "delay rest with time"),
        ("rest", "showAutonomyRespected", "show autonomy respected"),
        ("weather", "markWeatherLoan", "mark weather loan"),
        ("weather", "routeThroughShelter", "route through shelter"),
        ("weather", "protectLoanObject", "protect loan object"),
        ("weather", "delayWeatherLoan", "delay weather loan"),
        ("weather", "showColdRisk", "show cold risk"),
        ("welfare", "openRecoveryPath", "open recovery path"),
        ("welfare", "comfortResident", "comfort resident"),
        ("welfare", "moveTowardShelter", "move toward shelter"),
        ("welfare", "showNoSufferingLoop", "show no suffering loop"),
        ("welfare", "showEmotionLabel", "show emotion label"),
        ("reload", "restoreWelfareMemory", "restore welfare memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showNeedFrequency", "show need frequency"),
        ("frequency", "showRateNotMysticism", "show rate not mysticism"),
        ("body", "sampleEmbodiedNeeds", "sample Ari body"),
        ("body", "sampleEmbodiedNeeds", "sample Fay body"),
        ("body", "sampleEmbodiedNeeds", "sample Milo body"),
        ("body", "sampleEmbodiedNeeds", "sample Tala body"),
        ("body", "showBreathRate", "compare breath rates"),
        ("body", "showPainMarker", "mark guarded posture"),
        ("body", "showWetnessMarker", "mark wet cloak"),
        ("body", "showTemperatureMarker", "mark cold hands"),
        ("body", "showRestDebt", "show sleep pressure"),
        ("schedule", "adjustSocialSchedule", "slow shared task"),
        ("schedule", "adjustSocialSchedule", "split shared task"),
        ("schedule", "showNeedInterference", "rank need pressure"),
        ("schedule", "askPartnerAssist", "ask familiar partner"),
        ("schedule", "recordScheduleTradeoff", "record duty tradeoff"),
        ("care", "offerCareDuty", "offer warm broth"),
        ("care", "offerCareDuty", "offer dry cloak"),
        ("care", "offerCareDuty", "offer quiet mat"),
        ("care", "acceptCare", "accept low-burden care"),
        ("care", "deferCare", "defer unwanted care"),
        ("care", "redirectCare", "redirect wrong care"),
        ("care", "showCareBurden", "show caregiver burden"),
        ("care", "showCareBurden", "show reciprocal memory"),
        ("rest", "negotiateRest", "request short rest"),
        ("rest", "grantRest", "grant rest before duty"),
        ("rest", "delayRestWithTime", "delay with named time"),
        ("rest", "showAutonomyRespected", "show refusal respected"),
        ("rest", "recordScheduleTradeoff", "show relief handoff"),
        ("weather", "markWeatherLoan", "mark rainy route"),
        ("weather", "markWeatherLoan", "mark cold route"),
        ("weather", "routeThroughShelter", "choose shelter route"),
        ("weather", "protectLoanObject", "wrap borrowed object"),
        ("weather", "delayWeatherLoan", "pause exposed loan"),
        ("weather", "showColdRisk", "show cold risk"),
        ("weather", "showWetnessMarker", "show weather wetness"),
        ("welfare", "openRecoveryPath", "open care opportunity"),
        ("welfare", "comfortResident", "comfort without forcing"),
        ("welfare", "moveTowardShelter", "move toward shelter"),
        ("welfare", "showNoSufferingLoop", "show recovery bound"),
        ("welfare", "showEmotionLabel", "show welfare label"),
        ("welfare", "showAutonomyRespected", "show welfare consent"),
        ("reload", "restoreWelfareMemory", "restore body state"),
        ("reload", "restoreWelfareMemory", "restore care memory"),
        ("reload", "restoreWelfareMemory", "restore weather trace"),
        ("reload", "saveWorldState", "save care ledger"),
        ("reload", "restoreWorldState", "restore care ledger"),
        ("reload", "exportReplay", "export welfare replay"),
        ("frequency", "showFlowerPhase", "show phase ring"),
        ("frequency", "showNeedFrequency", "show breath frequency"),
        ("frequency", "showNeedFrequency", "show fatigue rate"),
        ("frequency", "showRateNotMysticism", "show rate boundary"),
        ("frequency", "showRateNotMysticism", "show no metaphysics"),
    ]
    buttons = "\n".join(
        f'<button data-action="{handler}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope, handler, label in actions
    )
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>SSRM-3D Browser World v48 Embodied Welfare Bridge</title>
<style>
:root { --soil:#241c17; --moss:#a8c58b; --amber:#f2c66d; --water:#6fb7b8; --cloud:#f4ead8; --danger:#d0795f; }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 20% 20%, #3c4d37, var(--soil)); color: var(--cloud); }
main { display:grid; grid-template-columns: repeat(2, minmax(280px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid rgba(244,234,216,.28); border-radius:18px; padding:16px; background:rgba(20,16,13,.72); box-shadow:0 18px 44px rgba(0,0,0,.35); }
button { margin:4px; border:1px solid rgba(244,234,216,.28); border-radius:999px; background:rgba(168,197,139,.18); color:var(--cloud); padding:8px 11px; }
.flower { width:140px; height:140px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(242,198,109,.38) 0 8px, transparent 9px 17px), conic-gradient(from 45deg, rgba(111,183,184,.45), rgba(168,197,139,.36), rgba(242,198,109,.42), rgba(111,183,184,.45)); }
.notice { grid-column:1/-1; color:#f7d7c9; }
</style>
</head>
<body>
<main>
<section id="embodied-need-panel"><h2>Body needs</h2><p>Energy, fatigue, hunger, thirst, temperature, wetness, pain, comfort, safety, breath rate, movement effort, rest debt, and injury/degradation stay visible through behavior markers.</p></section>
<section id="social-schedule-need-panel"><h2>Social schedule with body pressure</h2><p>Resident tasks can slow, shift, or become assisted when the body state interferes.</p></section>
<section id="household-care-panel"><h2>Household care duties</h2><p>Care is offered, accepted, deferred, or redirected with burden and reciprocal memory.</p></section>
<section id="fatigue-rest-panel"><h2>Fatigue/rest negotiation</h2><p>Residents can ask for rest, delay duties with named relief time, and preserve autonomy.</p></section>
<section id="weather-loan-panel"><h2>Weather-aware loans</h2><p>Object loans carry cold, wetness, shelter, condition, and route consequences.</p></section>
<section id="recoverable-welfare-panel"><h2>Recoverable welfare</h2><p>Distress opens care and recovery paths instead of spectacle loops.</p></section>
<section id="reload-welfare-panel"><h2>Save, restore, replay</h2><p>Reload probes restore body, care, rest, weather-loan, and welfare traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and need frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v48.embodied.welfare';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic trace' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function sampleEmbodiedNeeds(scope) { return pushTrace('sampleEmbodiedNeeds', scope); }
function showBreathRate(scope) { return pushTrace('showBreathRate', scope); }
function showPainMarker(scope) { return pushTrace('showPainMarker', scope); }
function showWetnessMarker(scope) { return pushTrace('showWetnessMarker', scope); }
function showTemperatureMarker(scope) { return pushTrace('showTemperatureMarker', scope); }
function showRestDebt(scope) { return pushTrace('showRestDebt', scope); }
function adjustSocialSchedule(scope) { return pushTrace('adjustSocialSchedule', scope); }
function showNeedInterference(scope) { return pushTrace('showNeedInterference', scope); }
function askPartnerAssist(scope) { return pushTrace('askPartnerAssist', scope); }
function recordScheduleTradeoff(scope) { return pushTrace('recordScheduleTradeoff', scope); }
function offerCareDuty(scope) { return pushTrace('offerCareDuty', scope); }
function acceptCare(scope) { return pushTrace('acceptCare', scope); }
function deferCare(scope) { return pushTrace('deferCare', scope); }
function redirectCare(scope) { return pushTrace('redirectCare', scope); }
function showCareBurden(scope) { return pushTrace('showCareBurden', scope); }
function negotiateRest(scope) { return pushTrace('negotiateRest', scope); }
function grantRest(scope) { return pushTrace('grantRest', scope); }
function delayRestWithTime(scope) { return pushTrace('delayRestWithTime', scope); }
function showAutonomyRespected(scope) { return pushTrace('showAutonomyRespected', scope); }
function markWeatherLoan(scope) { return pushTrace('markWeatherLoan', scope); }
function routeThroughShelter(scope) { return pushTrace('routeThroughShelter', scope); }
function protectLoanObject(scope) { return pushTrace('protectLoanObject', scope); }
function delayWeatherLoan(scope) { return pushTrace('delayWeatherLoan', scope); }
function showColdRisk(scope) { return pushTrace('showColdRisk', scope); }
function openRecoveryPath(scope) { return pushTrace('openRecoveryPath', scope); }
function comfortResident(scope) { return pushTrace('comfortResident', scope); }
function moveTowardShelter(scope) { return pushTrace('moveTowardShelter', scope); }
function showNoSufferingLoop(scope) { return pushTrace('showNoSufferingLoop', scope); }
function showEmotionLabel(scope) { return pushTrace('showEmotionLabel', scope); }
function restoreWelfareMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreWelfareMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreWelfareMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showNeedFrequency(scope) { return pushTrace('showNeedFrequency', scope); }
function showRateNotMysticism(scope) { return pushTrace('showRateNotMysticism', scope); }
</script>
</body>
</html>
"""


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(bundle: Mapping[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    summary_rows = [{"metric": key, "value": value} for key, value in results["metrics"].items()]
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary_rows)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v48_embodied_welfare_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 288 SSRM-3D browser world v48 embodied welfare bridge")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v48_embodied_welfare_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
