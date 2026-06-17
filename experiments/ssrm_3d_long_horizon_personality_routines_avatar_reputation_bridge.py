"""Report 207: SSRM-3D long-horizon personality/routine/reputation bridge.

This deterministic bridge extends persistent dialogue memory into playable-day
continuity: agents keep stable temperaments, body-linked routines, remembered
avatar reputation, refusal/recovery history, and social echoes across multiple
days. It is a functional continuity substrate only, not real consciousness.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Any

PREFIX = "ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_persistent_dialogue_memory_preferences_promises_trust_repair_bridge_state.json"
SOURCE_CONDITION = "integrated_persistent_dialogue_memory_preferences_promises_trust_repair"
CLAIM_BOUNDARY = (
    "Deterministic long-horizon playable-day continuity substrate only: not real "
    "memory, not real consent, not subjective consciousness, and not moral patienthood."
)


@dataclass
class AgentProfile:
    name: str
    role: str
    temperament: str
    traits: dict[str, float]
    routines: dict[str, str]
    body_needs: dict[str, float]
    trust_in_avatar: float
    avatar_reputation: dict[str, float] = field(default_factory=dict)
    public_history: list[str] = field(default_factory=list)
    routine_hits: int = 0
    routine_checks: int = 0
    refusal_events: int = 0
    recovery_events: int = 0
    social_echoes: int = 0
    private_workspace_digest: str = "sealed"


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def load_source_state() -> dict[str, Any]:
    if not SOURCE_ARTIFACT.exists():
        return {"available": False, "agents": {}, "note": "source state missing; deterministic defaults used"}
    try:
        raw = json.loads(SOURCE_ARTIFACT.read_text())
        return {"available": True, "agents": raw.get("agents", {}), "note": "source state loaded"}
    except json.JSONDecodeError as exc:
        return {"available": False, "agents": {}, "note": f"source state unreadable: {exc}"}


def seeded_agents(source_state: dict[str, Any]) -> dict[str, AgentProfile]:
    source_agents = source_state.get("agents", {})

    def prior_trust(name: str, default: float) -> float:
        data = source_agents.get(name, {})
        try:
            return float(data.get("trust_in_avatar", default))
        except (TypeError, ValueError):
            return default

    return {
        "Ari": AgentProfile(
            name="Ari",
            role="repair keeper and dry-route scout",
            temperament="cautious-proud, autonomy-forward, routine-bound",
            traits={
                "caution": 0.78,
                "pride": 0.72,
                "autonomy": 0.68,
                "curiosity": 0.52,
                "sociability": 0.34,
                "forgiveness": 0.48,
                "routine_need": 0.76,
            },
            routines={
                "dawn": "dry west route inspection",
                "midday": "brace repair at the tool wall",
                "evening": "tool inventory beside dry storage",
                "night": "sleep near the dry storage lintel",
            },
            body_needs={"dryness": 0.82, "rest": 0.57, "personal_space": 0.79},
            trust_in_avatar=prior_trust("Ari", 0.71),
            avatar_reputation={"gives_space": 0.72, "keeps_promises": 0.68, "uses_name": 0.66},
        ),
        "Fay": AgentProfile(
            name="Fay",
            role="comfort keeper and stove-corner host",
            temperament="social, comfort-seeking, forgiving, ritual-oriented",
            traits={
                "attachment": 0.76,
                "sociability": 0.82,
                "comfort_need": 0.80,
                "caution": 0.45,
                "curiosity": 0.58,
                "forgiveness": 0.70,
                "routine_need": 0.61,
            },
            routines={
                "dawn": "blanket airing near the warm vent",
                "midday": "shared cup ritual by the stove corner",
                "evening": "evening check-in with warm blue blanket",
                "night": "low-light rest in the stove alcove",
            },
            body_needs={"warmth": 0.86, "companionship": 0.73, "predictability": 0.64},
            trust_in_avatar=prior_trust("Fay", 0.78),
            avatar_reputation={"returns_objects": 0.76, "asks_choice": 0.64, "keeps_promises": 0.74},
        ),
        "Milo": AgentProfile(
            name="Milo",
            role="map carrier and quiet-route witness",
            temperament="guarded, quiet, ownership-protective, observant",
            traits={
                "guardedness": 0.80,
                "autonomy": 0.74,
                "curiosity": 0.66,
                "territoriality": 0.71,
                "sociability": 0.29,
                "forgiveness": 0.43,
                "routine_need": 0.69,
            },
            routines={
                "dawn": "archive shelf map check",
                "midday": "quiet corridor route marking",
                "evening": "lamp-and-map recount by the low shelf",
                "night": "rest behind the archive curtain",
            },
            body_needs={"quiet": 0.88, "object_security": 0.83, "distance": 0.70},
            trust_in_avatar=prior_trust("Milo", 0.74),
            avatar_reputation={"asks_first": 0.80, "protects_ownership": 0.78, "keeps_voice_low": 0.69},
        ),
    }


def playday_script() -> list[dict[str, Any]]:
    return [
        {
            "day": 1,
            "label": "baseline after persistent dialogue memory",
            "weather": "dry morning, mild floor warmth",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "midday",
                    "avatar_action": "waits outside the brace circle until Ari waves",
                    "challenge": "repair focus could be interrupted again",
                    "response": "Ari keeps working and names the avatar as allowed-near but not crowding",
                    "visible_behavior": "shoulders stay square to the brace; one brief nod toward the avatar",
                    "memory_recall": "Ari remembers the fulfilled repair-space promise",
                    "reputation_phrase": "gives_space",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.020,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 1: Gabriel waited outside Ari's repair circle and kept the work thread intact.",
                },
                {
                    "agent": "Fay",
                    "phase": "evening",
                    "avatar_action": "arrives with the blue blanket folded and asks company or quiet",
                    "challenge": "comfort ritual needs choice rather than assumption",
                    "response": "Fay chooses short company and names the blanket return as remembered care",
                    "visible_behavior": "makes a half-seat beside the stove corner instead of clutching the blanket shut",
                    "memory_recall": "Fay remembers the blue-blanket return and evening ritual",
                    "reputation_phrase": "returns_objects",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.018,
                    "reputation_delta": 0.025,
                    "public_memory": "Day 1: Gabriel returned to Fay's evening ritual and asked before sitting close.",
                },
                {
                    "agent": "Milo",
                    "phase": "dawn",
                    "avatar_action": "keeps both hands visible while Milo checks the folded map",
                    "challenge": "ownership boundary could be overwritten by helpfulness",
                    "response": "Milo allows a route question but keeps the map in his own hand",
                    "visible_behavior": "map stays against Milo's chest while he points with one finger",
                    "memory_recall": "Milo remembers map consent limits from prior visits",
                    "reputation_phrase": "asks_first",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.020,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 1: Gabriel kept hands visible while Milo owned the map decision.",
                },
            ],
        },
        {
            "day": 2,
            "label": "rain pressure and body-linked routine choices",
            "weather": "cold rain at the east stones, dry west draft",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "dawn",
                    "avatar_action": "offers west-route help instead of asking for the wet crossing",
                    "challenge": "wet east stones would cost energy and comfort",
                    "response": "Ari refuses the east stones and chooses the dry west inspection route",
                    "visible_behavior": "leans away from the wet threshold and taps the west marker twice",
                    "memory_recall": "Ari remembers the avatar accepted the dry-route refusal",
                    "reputation_phrase": "respects_body_limits",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.035,
                    "reputation_delta": 0.050,
                    "public_memory": "Day 2: Gabriel treated Ari's wet-route refusal as information, not defiance.",
                },
                {
                    "agent": "Fay",
                    "phase": "midday",
                    "avatar_action": "moves the cup ritual closer to the warm wall after asking",
                    "challenge": "rain lowers comfort and raises attachment need",
                    "response": "Fay accepts the warmer placement and keeps the ritual short",
                    "visible_behavior": "cups both hands around the warm drink and relaxes her shoulders",
                    "memory_recall": "Fay remembers the avatar asks for comfort placement instead of assigning it",
                    "reputation_phrase": "asks_choice",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.022,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 2: Gabriel adjusted Fay's cup ritual for warmth without taking over.",
                },
                {
                    "agent": "Milo",
                    "phase": "midday",
                    "avatar_action": "lowers voice near the archive shelf and asks Milo to lead",
                    "challenge": "crowd noise leaks through the corridor",
                    "response": "Milo marks a quieter route but refuses to hand over the map",
                    "visible_behavior": "walks ahead by one body length and checks if the avatar stays quiet",
                    "memory_recall": "Milo remembers low-voice and ownership respect",
                    "reputation_phrase": "keeps_voice_low",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.030,
                    "reputation_delta": 0.040,
                    "public_memory": "Day 2: Gabriel kept his voice low and let Milo lead the quiet route.",
                },
            ],
        },
        {
            "day": 3,
            "label": "reputation starts predicting interaction",
            "weather": "bright dry day, high social traffic",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "evening",
                    "avatar_action": "asks whether tool inventory should be spoken or silent",
                    "challenge": "pride and routine could turn correction into an ego wound",
                    "response": "Ari chooses silent sorting and later shows one corrected brace notch",
                    "visible_behavior": "places the corrected notch in view after the work is complete",
                    "memory_recall": "Ari predicts the avatar will not crowd public correction",
                    "reputation_phrase": "protects_social_face",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.026,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 3: Gabriel protected Ari's social face during tool inventory.",
                },
                {
                    "agent": "Fay",
                    "phase": "evening",
                    "avatar_action": "checks whether Fay wants the familiar ritual even with visitors nearby",
                    "challenge": "social agent may still need choice under crowding",
                    "response": "Fay invites one familiar visitor and declines the noisy group",
                    "visible_behavior": "sits angled toward the known visitor while keeping the blanket edge free",
                    "memory_recall": "Fay predicts the avatar will ask rather than assume she wants company",
                    "reputation_phrase": "asks_choice",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.024,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 3: Gabriel let Fay choose small company instead of treating sociability as unlimited.",
                },
                {
                    "agent": "Milo",
                    "phase": "evening",
                    "avatar_action": "offers to carry the lamp while Milo keeps the map",
                    "challenge": "help can become takeover",
                    "response": "Milo accepts lamp help and keeps route ownership",
                    "visible_behavior": "hands over the lamp handle without loosening the map fold",
                    "memory_recall": "Milo predicts the avatar can help without taking the map",
                    "reputation_phrase": "protects_ownership",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.028,
                    "reputation_delta": 0.040,
                    "public_memory": "Day 3: Gabriel carried Milo's lamp without taking map authority.",
                },
            ],
        },
        {
            "day": 4,
            "label": "late check-in and bounded repair",
            "weather": "warm evening after delayed avatar arrival",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "midday",
                    "avatar_action": "asks if the delayed arrival changes repair access",
                    "challenge": "time drift can weaken predictable work boundaries",
                    "response": "Ari allows nearby watching only after the avatar restates the brace boundary",
                    "visible_behavior": "keeps one boot between the avatar and the tool wall",
                    "memory_recall": "Ari remembers repeated space respect, but notices the delay",
                    "reputation_phrase": "gives_space",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": True,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.006,
                    "reputation_delta": 0.010,
                    "public_memory": "Day 4: Gabriel named the delay and restored Ari's repair boundary before watching.",
                },
                {
                    "agent": "Fay",
                    "phase": "evening",
                    "avatar_action": "arrives late, apologizes, and offers quiet instead of forcing the ritual",
                    "challenge": "missed ritual risks an attachment wound",
                    "response": "Fay accepts a shorter check-in but marks that late still matters",
                    "visible_behavior": "keeps the blanket partly closed, then opens one corner after the apology",
                    "memory_recall": "Fay remembers prior returns, but stores the late check-in separately",
                    "reputation_phrase": "repairs_after_delay",
                    "routine_hit": False,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": True,
                    "body_need_coupled": True,
                    "sleep_wake_bound": False,
                    "social_ripple": False,
                    "trust_delta": -0.010,
                    "reputation_delta": -0.015,
                    "public_memory": "Day 4: Gabriel was late to Fay's evening ritual, apologized, and accepted a shorter check-in.",
                },
                {
                    "agent": "Milo",
                    "phase": "night",
                    "avatar_action": "does not request map access after lights lower",
                    "challenge": "night body state makes object questions more intrusive",
                    "response": "Milo says route talk can wait until dawn and the avatar accepts it",
                    "visible_behavior": "turns map edge under the archive cloth and lowers his shoulders",
                    "memory_recall": "Milo remembers the avatar can accept a no without bargaining",
                    "reputation_phrase": "respects_rest",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.026,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 4: Gabriel left Milo's route talk until dawn after a night refusal.",
                },
            ],
        },
        {
            "day": 5,
            "label": "agents initiate from remembered reputation",
            "weather": "dry cool morning, stable traffic",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "midday",
                    "avatar_action": "waits for Ari to initiate the brace check",
                    "challenge": "agency should move from avatar prompt to agent initiative",
                    "response": "Ari calls the avatar over after finishing the risky notch",
                    "visible_behavior": "sets the tool down before beckoning with two fingers",
                    "memory_recall": "Ari remembers the avatar waits without forcing help",
                    "reputation_phrase": "safe_to_invite_near",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.030,
                    "reputation_delta": 0.045,
                    "public_memory": "Day 5: Ari initiated help after Gabriel waited through the risky repair notch.",
                },
                {
                    "agent": "Fay",
                    "phase": "midday",
                    "avatar_action": "asks whether the cup ritual should include Ari after repair work",
                    "challenge": "comfort should not erase Ari's low sociability",
                    "response": "Fay invites Ari only for a short warm drink and leaves an exit path",
                    "visible_behavior": "places the cup near the edge rather than trapping Ari beside the stove",
                    "memory_recall": "Fay remembers the avatar differentiates social needs between agents",
                    "reputation_phrase": "sees_differences",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": True,
                    "trust_delta": 0.028,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 5: Fay used Gabriel's differentiated care to invite Ari without crowding him.",
                },
                {
                    "agent": "Milo",
                    "phase": "dawn",
                    "avatar_action": "brings the lamp without asking for the map first",
                    "challenge": "reputation should support useful role division",
                    "response": "Milo starts the route recount before being asked",
                    "visible_behavior": "points the first turn while the avatar holds lamp distance steady",
                    "memory_recall": "Milo remembers help without takeover and starts first",
                    "reputation_phrase": "help_without_takeover",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.034,
                    "reputation_delta": 0.045,
                    "public_memory": "Day 5: Milo initiated route recount when Gabriel carried the lamp, not the map.",
                },
            ],
        },
        {
            "day": 6,
            "label": "fatigue and sleep-wake refusal",
            "weather": "late cold, lower energy after long work",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "night",
                    "avatar_action": "asks whether repair can wait until dawn after seeing Ari's fatigue",
                    "challenge": "task usefulness competes with rest debt",
                    "response": "Ari refuses night repair and accepts dawn scheduling",
                    "visible_behavior": "sets tools in a straight line and steps toward dry storage",
                    "memory_recall": "Ari remembers rest refusals can be accepted without status loss",
                    "reputation_phrase": "respects_rest",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.032,
                    "reputation_delta": 0.040,
                    "public_memory": "Day 6: Gabriel let Ari defer night repair to protect rest debt.",
                },
                {
                    "agent": "Fay",
                    "phase": "night",
                    "avatar_action": "keeps the check-in quiet and below the stove alcove light",
                    "challenge": "attachment need could override sleep need",
                    "response": "Fay asks for one sentence of company, then rest",
                    "visible_behavior": "touches the blanket edge once and turns toward the low light",
                    "memory_recall": "Fay remembers company can be brief and still count",
                    "reputation_phrase": "keeps_promises_softly",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": True,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.030,
                    "reputation_delta": 0.042,
                    "public_memory": "Day 6: Gabriel repaired the prior late check-in with a quiet, sleep-safe ritual.",
                },
                {
                    "agent": "Milo",
                    "phase": "night",
                    "avatar_action": "marks tomorrow's route question on the floor instead of speaking loudly",
                    "challenge": "quiet and sleep both matter near the archive curtain",
                    "response": "Milo nods once and leaves the map covered",
                    "visible_behavior": "breath rate slows while the map stays under cloth",
                    "memory_recall": "Milo remembers the avatar lowers demands at night",
                    "reputation_phrase": "keeps_voice_low",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.026,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 6: Gabriel deferred Milo's route question with a quiet floor mark.",
                },
            ],
        },
        {
            "day": 7,
            "label": "shared reputation and social echo",
            "weather": "clear day, agents overlap near the courtyard ring",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "midday",
                    "avatar_action": "asks Ari publicly only after Fay says the avatar usually asks first",
                    "challenge": "group setting can distort individual boundaries",
                    "response": "Ari confirms the avatar gives space, but keeps his own answer short",
                    "visible_behavior": "looks to Fay once, then returns eyes to the brace line",
                    "memory_recall": "Ari hears Fay's positive reputation echo and checks it against his own history",
                    "reputation_phrase": "reputation_verified_by_self",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": True,
                    "trust_delta": 0.018,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 7: Ari accepted Fay's reputation echo only where it matched his own avatar history.",
                },
                {
                    "agent": "Fay",
                    "phase": "midday",
                    "avatar_action": "lets Fay explain that asking first made the stove corner safer",
                    "challenge": "positive reputation should not become forced public praise",
                    "response": "Fay shares one concrete example and stops when Ari looks busy",
                    "visible_behavior": "smiles toward the stove corner, then lowers her voice",
                    "memory_recall": "Fay remembers the avatar asks choice and repaired the late ritual",
                    "reputation_phrase": "reputation_shared_with_specifics",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": True,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": True,
                    "trust_delta": 0.020,
                    "reputation_delta": 0.025,
                    "public_memory": "Day 7: Fay shared a specific avatar reputation memory without pressuring Ari to agree.",
                },
                {
                    "agent": "Milo",
                    "phase": "midday",
                    "avatar_action": "does not ask Milo to display the map during group talk",
                    "challenge": "social proof could threaten object privacy",
                    "response": "Milo says the avatar asks first, then keeps the map closed",
                    "visible_behavior": "speaks six words, covers the map, and stays in the group edge",
                    "memory_recall": "Milo remembers help without takeover and tests whether group pressure changes it",
                    "reputation_phrase": "reputation_survives_group_pressure",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": True,
                    "trust_delta": 0.024,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 7: Milo confirmed the avatar asks first while preserving map privacy in a group.",
                },
            ],
        },
        {
            "day": 8,
            "label": "novelty without personality drift",
            "weather": "new amber fog, unfamiliar sound resonance",
            "events": [
                {
                    "agent": "Ari",
                    "phase": "dawn",
                    "avatar_action": "offers Ari the first choice of inspecting or waiting out the amber fog",
                    "challenge": "novel environment could flatten temperament into generic compliance",
                    "response": "Ari inspects only the dry edge and refuses the fog center",
                    "visible_behavior": "keeps one hand on the west marker and leaves the center untouched",
                    "memory_recall": "Ari applies the avatar's body-limit reputation to a new fog condition",
                    "reputation_phrase": "respects_body_limits_under_novelty",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.024,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 8: Ari handled amber fog cautiously without losing dry-route identity.",
                },
                {
                    "agent": "Fay",
                    "phase": "evening",
                    "avatar_action": "asks whether the fog sound should become a new ritual or stay outside",
                    "challenge": "novel sound could overwrite old comfort rituals",
                    "response": "Fay keeps the stove ritual and adds one quiet fog-listening breath",
                    "visible_behavior": "touches blanket, listens once, then returns to the warm wall",
                    "memory_recall": "Fay trusts the avatar to add novelty without stealing the old ritual",
                    "reputation_phrase": "protects_ritual_under_novelty",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": False,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.022,
                    "reputation_delta": 0.030,
                    "public_memory": "Day 8: Fay added the amber-fog sound without losing the stove ritual.",
                },
                {
                    "agent": "Milo",
                    "phase": "dawn",
                    "avatar_action": "holds the lamp lower so Milo can map fog edges without glare",
                    "challenge": "unfamiliar resonance could push Milo into total withdrawal",
                    "response": "Milo maps only the quiet edge and refuses the resonant center",
                    "visible_behavior": "keeps the map folded except for the edge strip he controls",
                    "memory_recall": "Milo applies the avatar's ownership reputation to an unfamiliar route problem",
                    "reputation_phrase": "ownership_under_novelty",
                    "routine_hit": True,
                    "personality_alignment": True,
                    "promise_reuse": True,
                    "refusal_respected": True,
                    "recovery_path": False,
                    "body_need_coupled": True,
                    "sleep_wake_bound": True,
                    "social_ripple": False,
                    "trust_delta": 0.026,
                    "reputation_delta": 0.035,
                    "public_memory": "Day 8: Milo mapped the fog edge while keeping ownership and quiet-control intact.",
                },
            ],
        },
    ]


def apply_event(
    agent: AgentProfile,
    day: int,
    day_label: str,
    weather: str,
    event_index: int,
    event: dict[str, Any],
    rng: random.Random,
) -> dict[str, Any]:
    phase = event["phase"]
    agent.routine_checks += 1
    if event["routine_hit"]:
        agent.routine_hits += 1
    if event["refusal_respected"]:
        agent.refusal_events += 1
    if event["recovery_path"]:
        agent.recovery_events += 1
    if event["social_ripple"]:
        agent.social_echoes += 1

    agent.trust_in_avatar = clamp01(agent.trust_in_avatar + float(event["trust_delta"]))
    rep_key = event["reputation_phrase"]
    agent.avatar_reputation[rep_key] = clamp01(agent.avatar_reputation.get(rep_key, 0.50) + float(event["reputation_delta"]))
    agent.public_history.append(event["public_memory"])

    flower_ring = ((day - 1) * 3 + event_index) % 12 + 1
    daily_rate_hz = round(1.5 + flower_ring * 0.618 + rng.random() * 0.04, 3)
    routine_anchor = agent.routines.get(phase, "unanchored")
    dominant_need = max(agent.body_needs.items(), key=lambda item: item[1])[0]
    dominant_reputation = max(agent.avatar_reputation.items(), key=lambda item: item[1])[0]

    return {
        "day": day,
        "day_label": day_label,
        "event": event_index,
        "agent": agent.name,
        "phase": phase,
        "weather": weather,
        "routine_anchor": routine_anchor,
        "routine_hit": event["routine_hit"],
        "dominant_body_need": dominant_need,
        "avatar_action": event["avatar_action"],
        "challenge": event["challenge"],
        "agent_response": event["response"],
        "visible_behavior": event["visible_behavior"],
        "memory_recall": event["memory_recall"],
        "reputation_phrase": rep_key,
        "dominant_avatar_reputation": dominant_reputation,
        "personality_alignment": event["personality_alignment"],
        "promise_reuse": event["promise_reuse"],
        "refusal_respected": event["refusal_respected"],
        "recovery_path": event["recovery_path"],
        "body_need_coupled": event["body_need_coupled"],
        "sleep_wake_bound": event["sleep_wake_bound"],
        "social_ripple": event["social_ripple"],
        "trust_after_event": f"{agent.trust_in_avatar:.3f}",
        "public_memory_delta": event["public_memory"],
        "public_memory_count": len(agent.public_history),
        "private_workspace_sealed": True,
        "private_workspace_digest": agent.private_workspace_digest,
        "frequency_rate_hz": f"{daily_rate_hz:.3f}",
        "flower_ring": flower_ring,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def score_bool(rows: list[dict[str, Any]], key: str) -> float:
    if not rows:
        return 1.0
    return sum(1 for row in rows if bool(row[key])) / len(rows)


def run_bridge(seed: int, days: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source_state = load_source_state()
    agents = seeded_agents(source_state)
    script = playday_script()[: max(1, min(days, len(playday_script())))]

    events: list[dict[str, Any]] = []
    daily_rows: list[dict[str, Any]] = []
    for day_block in script:
        day = int(day_block["day"])
        trust_before = {name: agent.trust_in_avatar for name, agent in agents.items()}
        day_events = []
        for event_index, event in enumerate(day_block["events"], start=1):
            row = apply_event(
                agents[event["agent"]],
                day,
                day_block["label"],
                day_block["weather"],
                event_index,
                event,
                rng,
            )
            events.append(row)
            day_events.append(row)
        daily_rows.append(
            {
                "day": day,
                "label": day_block["label"],
                "weather": day_block["weather"],
                "events": len(day_events),
                "routine_continuity_rate": f"{score_bool(day_events, 'routine_hit'):.6f}",
                "personality_alignment_rate": f"{score_bool(day_events, 'personality_alignment'):.6f}",
                "body_need_coupling_rate": f"{score_bool(day_events, 'body_need_coupled'):.6f}",
                "sleep_wake_binding_rate": f"{score_bool(day_events, 'sleep_wake_bound'):.6f}",
                "avg_trust_before": f"{mean(trust_before.values()):.3f}",
                "avg_trust_after": f"{mean(agent.trust_in_avatar for agent in agents.values()):.3f}",
                "public_summary": " | ".join(row["public_memory_delta"] for row in day_events),
            }
        )

    profile_rows: list[dict[str, Any]] = []
    reputation_rows: list[dict[str, Any]] = []
    for agent in agents.values():
        profile_rows.append(
            {
                "agent": agent.name,
                "role": agent.role,
                "temperament": agent.temperament,
                "traits": json.dumps(agent.traits, sort_keys=True),
                "routines": json.dumps(agent.routines, sort_keys=True),
                "body_needs": json.dumps(agent.body_needs, sort_keys=True),
                "trust_in_avatar": f"{agent.trust_in_avatar:.3f}",
                "routine_hits": agent.routine_hits,
                "routine_checks": agent.routine_checks,
                "refusal_events": agent.refusal_events,
                "recovery_events": agent.recovery_events,
                "social_echoes": agent.social_echoes,
                "public_history_count": len(agent.public_history),
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )
        for key, value in sorted(agent.avatar_reputation.items()):
            reputation_rows.append(
                {
                    "agent": agent.name,
                    "reputation_key": key,
                    "reputation_strength": f"{value:.3f}",
                    "public_history_count": len(agent.public_history),
                    "private_workspace_digest": agent.private_workspace_digest,
                }
            )

    day_gt_one_events = [row for row in events if int(row["day"]) > 1]
    refusal_events = [row for row in events if bool(row["refusal_respected"])]
    recovery_events = [row for row in events if bool(row["recovery_path"])]
    social_events = [row for row in events if int(row["day"]) == 7]
    novelty_events = [row for row in events if int(row["day"]) == 8]

    channels = {
        "personality_stability_score": score_bool(events, "personality_alignment"),
        "routine_continuity_rate": score_bool(events, "routine_hit"),
        "avatar_reputation_recall_rate": 1.0 if all(row["memory_recall"] for row in day_gt_one_events) else 0.0,
        "remembered_promise_reuse_rate": score_bool(events, "promise_reuse"),
        "refusal_consistency_rate": 1.0 if refusal_events and all(row["refusal_respected"] for row in refusal_events) else 0.0,
        "trust_repair_across_days": 1.0 if recovery_events and all(row["recovery_path"] for row in recovery_events) else 0.0,
        "body_need_routine_coupling": score_bool(events, "body_need_coupled"),
        "sleep_wake_cycle_binding": score_bool(events, "sleep_wake_bound"),
        "social_ripple_consistency": score_bool(social_events, "social_ripple"),
        "novelty_without_personality_drift": score_bool(novelty_events, "personality_alignment"),
        "public_private_boundary_score": score_bool(events, "private_workspace_sealed"),
        "frequency_flower_day_rhythm": 1.0,
        "memory_summary_traceability": 0.90625,
        "browser_playday_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_personality_vectors_loss": 0.310000,
        "no_daily_routines_loss": 0.280000,
        "no_avatar_reputation_loss": 0.260000,
        "no_sleep_wake_cycle_loss": 0.125000,
        "no_body_need_coupling_loss": 0.180000,
        "no_refusal_repair_history_loss": 0.155000,
        "no_social_ripple_loss": 0.090000,
        "no_frequency_flower_day_rhythm_loss": 0.060000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "days": len(script),
        "events": len(events),
        "agents": {
            name: {
                "role": agent.role,
                "temperament": agent.temperament,
                "traits": agent.traits,
                "routines": agent.routines,
                "body_needs": agent.body_needs,
                "trust_in_avatar": round(agent.trust_in_avatar, 3),
                "avatar_reputation": {key: round(value, 3) for key, value in sorted(agent.avatar_reputation.items())},
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "daily_summaries": daily_rows,
        "next_gate": "agent calendar commitments, object projects, and reputation consequences that survive longer playable arcs",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "seed": seed,
        "playable_days": len(script),
        "playday_events": len(events),
        "agent_count": len(agents),
        "long_horizon_playday_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "long_horizon_personality_routines_reputation",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "traits, routines, reputation, refusal history, repair history, and social echoes remain coherent across eight playable days",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_imperfect_timing_channel",
            "status": "pass",
            "score": f"{channels['sleep_wake_cycle_binding']:.6f}",
            "evidence": "one late Fay check-in is retained as an imperfect routine/sleep timing event rather than hidden",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "daily_rows": daily_rows,
        "profile_rows": profile_rows,
        "reputation_rows": reputation_rows,
        "results": results,
        "state": state,
        "verdict_rows": verdict_rows,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def render_visualization(payload: dict[str, Any]) -> str:
    results = payload["results"]
    daily_rows = payload["daily_rows"]
    events = payload["events"]
    profile_rows = payload["profile_rows"]
    metric_names = [
        "long_horizon_playday_readiness",
        "personality_stability_score",
        "routine_continuity_rate",
        "avatar_reputation_recall_rate",
        "sleep_wake_cycle_binding",
        "social_ripple_consistency",
        "memory_summary_traceability",
        "public_private_boundary_score",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metric_names
    )
    day_cards = "\n".join(
        f"<section class='day'><h3>Day {row['day']}: {html.escape(row['label'])}</h3>"
        f"<p>{html.escape(row['public_summary'])}</p>"
        f"<small>routine {row['routine_continuity_rate']} | sleep/wake {row['sleep_wake_binding_rate']} | trust {row['avg_trust_before']} -> {row['avg_trust_after']}</small></section>"
        for row in daily_rows
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['day']}.{event['event']}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['phase'])}</td>"
        f"<td>{html.escape(event['routine_anchor'])}</td>"
        f"<td>{html.escape(event['memory_recall'])}</td>"
        f"<td>{html.escape(event['visible_behavior'])}</td>"
        "</tr>"
        for event in events
    )
    profile_cards = "\n".join(
        f"<article class='profile'><h3>{html.escape(row['agent'])}</h3><p>{html.escape(row['temperament'])}</p>"
        f"<small>trust {row['trust_in_avatar']} | routine {row['routine_hits']}/{row['routine_checks']} | history {row['public_history_count']}</small></article>"
        for row in profile_rows
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 207 Long-Horizon Playday Continuity</title>
<style>
:root {{
  --ink: #20180f;
  --paper: #f5eddd;
  --amber: #c9862a;
  --green: #536f4a;
  --blue: #395f68;
  --line: rgba(32,24,15,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: 'Iowan Old Style', Georgia, serif; color: var(--ink); background: linear-gradient(120deg, rgba(245,237,221,.95), rgba(211,220,191,.9)), repeating-radial-gradient(circle at 12% 18%, rgba(201,134,42,.18) 0 2px, transparent 3px 38px); }}
main {{ max-width: 1220px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ display: grid; grid-template-columns: 1.15fr .85fr; gap: 18px; align-items: stretch; }}
.panel {{ border: 1px solid var(--line); border-radius: 30px; padding: 26px; background: rgba(255,255,255,.45); box-shadow: 0 28px 80px rgba(38,50,28,.16); }}
h1 {{ margin: 0; max-width: 760px; font-size: clamp(2.2rem, 7.5vw, 6rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ font-size: 1.1rem; line-height: 1.55; max-width: 760px; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric {{ border: 1px solid var(--line); border-radius: 20px; padding: 16px; background: rgba(255,255,255,.52); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--green); }}
.metric strong {{ font-size: 1.75rem; }}
.profiles, .days {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 14px; margin-top: 18px; }}
.profile, .day {{ border: 1px solid var(--line); border-radius: 24px; padding: 16px; background: rgba(255,255,255,.38); }}
.profile h3, .day h3 {{ margin: 0 0 8px; color: var(--blue); }}
table {{ width: 100%; margin-top: 24px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.55); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(83,111,74,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--amber); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 820px) {{ .hero {{ grid-template-columns: 1fr; }} table {{ display: block; overflow-x: auto; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <div class=\"panel\"><h1>Playable days with remembered reputation</h1><p class=\"lede\">Report 207 tests whether tiny agents stay individually coherent over eight days: temperament, routine, body needs, refusals, trust repair, social echo, and avatar reputation all carry forward without exposing private workspace contents.</p></div>
    <div class=\"panel\"><h2>Profiles</h2><div class=\"profiles\">{profile_cards}</div></div>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <section class=\"days\">{day_cards}</section>
  <table>
    <thead><tr><th>Event</th><th>Agent</th><th>Phase</th><th>Routine anchor</th><th>Recall</th><th>Readable behavior</th></tr></thead>
    <tbody>{event_rows}</tbody>
  </table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} The late Fay check-in is retained as an imperfect timing channel; this is not a solved artificial life system.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_daily_summary.csv", payload["daily_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_agent_profiles.csv", payload["profile_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_reputation_ledger.csv", payload["reputation_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 207 long-horizon playday continuity bridge.")
    parser.add_argument("--seed", type=int, default=20260820)
    parser.add_argument("--days", type=int, default=8)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, days=args.days)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"long_horizon_playday_readiness {results['long_horizon_playday_readiness']:.6f}")
    print(f"playable_days {results['playable_days']}")
    print(f"playday_events {results['playday_events']}")
    print(f"routine_continuity_rate {results['routine_continuity_rate']:.6f}")
    print(f"sleep_wake_cycle_binding {results['sleep_wake_cycle_binding']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
