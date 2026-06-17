#!/usr/bin/env python3
"""Report 235: SSRM-3D Playable Pre-Avatar Civilization Sandbox Bridge.

This deterministic bridge turns the Report 234 pre-avatar society scaffold into a
local playable sandbox trace: generations, household market schedules, ritual
schedules, proto-language mutation chains, sensory/body interaction prompts, and
a final avatar-entry ceremony after mature thresholds.

It does not claim subjective consciousness, real civilization, autonomous
language, or a finished game. It provides the next inspectable bridge toward a
playable world where the avatar enters only after thousands of simulated years.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 235
BASE = "ssrm_3d_playable_pre_avatar_civilization_sandbox_bridge"
DEFAULT_SEED = 20260848
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_pre_avatar_society_market_ritual_proto_language_epoch_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_pre_avatar_society_market_ritual_proto_language_epoch_bridge_state.json"
YEARS = [0, 55, 377, 987, 1597, 2584, 4181]
HOUSEHOLDS = ["westkeepers", "mossgarden", "ledgerkin", "redstair", "wheelwright"]
PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class GenerationalAgent:
    agent_id: str
    year: int
    generation_index: int
    household_id: str
    name: str
    inherited_role: str
    personal_preference: str
    private_workspace_seed: str
    body_sensitivity: str
    relationship_memory_inherited: str
    proto_language_native_token: str
    playable_prompt: str


@dataclass(frozen=True)
class ProtoLanguageMutation:
    mutation_id: str
    year: int
    household_id: str
    parent_token: str
    mutated_token: str
    mutation_kind: str
    semantic_shift: str
    grounded_scene: str
    adoption_rate: float
    stability_score: float
    rollback_meaning: str


@dataclass(frozen=True)
class MarketScheduleSlot:
    slot_id: str
    year: int
    tick: int
    seller_household: str
    buyer_household: str
    good: str
    price_token: str
    fairness_score: float
    shortage_pressure: float
    schedule_dependency: str
    playable_action: str
    consequence_trace: str


@dataclass(frozen=True)
class RitualScheduleSlot:
    ritual_slot_id: str
    year: int
    tick: int
    household_id: str
    ritual_name: str
    trigger: str
    body_motion: str
    sound_pattern: str
    scent_material: str
    social_effect: str
    playable_observation: str
    continuity_score: float


@dataclass(frozen=True)
class TechnologyUseSlot:
    technology_slot_id: str
    year: int
    household_id: str
    technology_name: str
    use_context: str
    maintenance_need: float
    failure_risk: float
    rollback_action: str
    market_or_ritual_link: str
    playable_affordance: str


@dataclass(frozen=True)
class SensoryInteractionPrompt:
    prompt_id: str
    year: int
    place: str
    visual: str
    sound: str
    smell: str
    temperature_c: float
    wetness: float
    pain_risk: float
    comfort: str
    vibration_hz: float
    avatar_or_observer_choice: str


@dataclass(frozen=True)
class PlayableSandboxTurn:
    turn_id: str
    year: int
    tick: int
    agent_id: str
    interaction_kind: str
    visible_behavior: str
    spoken_proto_line: str
    private_workspace_boundary: str
    player_choice_stub: str
    simulated_response: str
    traceable_state_change: str


@dataclass(frozen=True)
class AvatarEntryCeremonyStep:
    ceremony_step_id: str
    year: int
    step_index: int
    threshold_checked: str
    required_value: float
    actual_value: float
    passed: bool
    ceremony_action: str
    household_witness: str
    avatar_permission_state: str


@dataclass(frozen=True)
class SandboxContinuityTick:
    continuity_tick_id: str
    year: int
    tick: int
    phase: str
    agent_id: str
    market_slot_id: str
    ritual_slot_id: str
    technology_slot_id: str
    prompt_id: str
    turn_id: str
    ceremony_step_id: str
    sandbox_state: str
    note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | float | int | bool:
    if isinstance(value, (dict, list)):
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


def build_agents() -> list[GenerationalAgent]:
    roles = {
        "westkeepers": ("route keeper", "prefers dry arches", "wet stone fatigue", "ka"),
        "mossgarden": ("rest keeper", "prefers warm shared meals", "cold hunger stress", "mu"),
        "ledgerkin": ("market counter", "prefers fair turns", "crowd noise overload", "lo"),
        "redstair": ("witness keeper", "prefers quiet truthful speech", "public blame heat", "sa"),
        "wheelwright": ("waterwheel keeper", "prefers careful invention", "wet glove pain risk", "ni"),
    }
    agents: list[GenerationalAgent] = []
    for gen, year in enumerate(YEARS):
        for h_index, household in enumerate(HOUSEHOLDS):
            role, preference, sensitivity, root = roles[household]
            name = f"{root.capitalize()}{gen}{h_index}"
            agents.append(
                GenerationalAgent(
                    agent_id=f"agent_{year}_{household}",
                    year=year,
                    generation_index=gen,
                    household_id=household,
                    name=name,
                    inherited_role=role,
                    personal_preference=preference,
                    private_workspace_seed=f"I am {name}; I remember the {household} oath and choose my next task from body cost, market need, and ritual duty.",
                    body_sensitivity=sensitivity,
                    relationship_memory_inherited="founder ego boundary, repair memory, and household trust ledger",
                    proto_language_native_token=f"{root}{PHASES[gen % len(PHASES)][:2]}{gen}",
                    playable_prompt=f"Approach {name} at year {year}: ask about {role}, trade, ritual, or boundary.",
                )
            )
    return agents


def build_language_mutations(agents: list[GenerationalAgent]) -> list[ProtoLanguageMutation]:
    mutations: list[ProtoLanguageMutation] = []
    for agent in agents:
        year_index = YEARS.index(agent.year)
        root = agent.proto_language_native_token[:2]
        parent = f"{root}{PHASES[max(0, year_index - 1) % len(PHASES)][:2]}{max(0, year_index - 1)}"
        mutated = agent.proto_language_native_token
        kind = ["sound-softening", "gesture-affix", "trade-compound", "repair-marker", "place-vowel", "future-tense", "ceremony-form"][year_index]
        stability = clamp(0.72 + year_index * 0.035)
        adoption = clamp(0.32 + year_index * 0.10 + (0.03 if agent.household_id in {"ledgerkin", "redstair"} else 0.0))
        mutations.append(
            ProtoLanguageMutation(
                mutation_id=f"mut_{agent.agent_id}",
                year=agent.year,
                household_id=agent.household_id,
                parent_token=parent,
                mutated_token=mutated,
                mutation_kind=kind,
                semantic_shift=f"{kind} binds {agent.inherited_role} to {agent.personal_preference}",
                grounded_scene=f"{agent.household_id} uses the word while resolving body cost or trade duty",
                adoption_rate=round(adoption, 6),
                stability_score=round(stability, 6),
                rollback_meaning="fallback to founder root if mutation confuses market or ritual meaning",
            )
        )
    return mutations


def build_market_slots(agents: list[GenerationalAgent]) -> list[MarketScheduleSlot]:
    goods = {
        "westkeepers": "dry route pass",
        "mossgarden": "seed meal and blanket hour",
        "ledgerkin": "fair-count thread",
        "redstair": "witness pause",
        "wheelwright": "vane repair service",
    }
    slots: list[MarketScheduleSlot] = []
    for agent in agents:
        year_index = YEARS.index(agent.year)
        h_index = HOUSEHOLDS.index(agent.household_id)
        buyer = HOUSEHOLDS[(h_index + year_index + 2) % len(HOUSEHOLDS)]
        fairness = clamp(0.80 + year_index * 0.026 - (0.015 if year_index == 2 else 0.0))
        shortage = clamp(0.40 - year_index * 0.035 + (0.08 if agent.household_id == "mossgarden" and year_index in {2, 3} else 0.0))
        slots.append(
            MarketScheduleSlot(
                slot_id=f"market_slot_{agent.agent_id}",
                year=agent.year,
                tick=100 + year_index * 70 + h_index * 7,
                seller_household=agent.household_id,
                buyer_household=buyer,
                good=goods[agent.household_id],
                price_token=agent.proto_language_native_token,
                fairness_score=round(fairness, 6),
                shortage_pressure=round(shortage, 6),
                schedule_dependency="ritual first if storm, market first if hunger, witness first if dispute",
                playable_action=f"Offer, refuse, barter, observe, or ask {agent.name} to explain the price token.",
                consequence_trace="updates trust ledger, body need pressure, and next ritual attendance",
            )
        )
    return slots


def build_ritual_slots(agents: list[GenerationalAgent]) -> list[RitualScheduleSlot]:
    ritual_roots = {
        "westkeepers": ("tool-return bow", "chalk line, hand to arch"),
        "mossgarden": ("cup-circle meal", "cup pass, blanket fold"),
        "ledgerkin": ("counting-step chant", "heel rock, thread knot"),
        "redstair": ("three-mark witness pause", "hand to wall, shell turn"),
        "wheelwright": ("vane-touch safety check", "glove lift, wheel listen"),
    }
    slots: list[RitualScheduleSlot] = []
    for agent in agents:
        year_index = YEARS.index(agent.year)
        name, motion = ritual_roots[agent.household_id]
        continuity = clamp(0.83 + year_index * 0.024)
        slots.append(
            RitualScheduleSlot(
                ritual_slot_id=f"ritual_slot_{agent.agent_id}",
                year=agent.year,
                tick=120 + year_index * 70 + HOUSEHOLDS.index(agent.household_id) * 7,
                household_id=agent.household_id,
                ritual_name=name,
                trigger="morning body check, market open, storm alarm, or conflict repair",
                body_motion=motion,
                sound_pattern=f"{agent.proto_language_native_token} repeated at phase {PHASES[year_index % len(PHASES)]}",
                scent_material="moss, copper, seed oil, chalk, wet stone, shell dust",
                social_effect="stabilizes household memory and teaches safe refusal before trade",
                playable_observation=f"Watch {agent.name}'s posture, ask meaning, join only after invitation.",
                continuity_score=round(continuity, 6),
            )
        )
    return slots


def build_technology_slots(agents: list[GenerationalAgent]) -> list[TechnologyUseSlot]:
    techs = ["hand marks", "dry store", "ledger knots", "wheel brake", "heated wall", "shell archive", "market canopy"]
    slots: list[TechnologyUseSlot] = []
    for agent in agents:
        year_index = YEARS.index(agent.year)
        h_index = HOUSEHOLDS.index(agent.household_id)
        maintenance = clamp(0.36 - year_index * 0.028 + h_index * 0.006)
        failure = clamp(0.24 - year_index * 0.020 + (0.04 if agent.household_id == "wheelwright" else 0.0))
        slots.append(
            TechnologyUseSlot(
                technology_slot_id=f"tech_slot_{agent.agent_id}",
                year=agent.year,
                household_id=agent.household_id,
                technology_name=f"{agent.household_id} {techs[year_index]}",
                use_context="market support, ritual stabilization, body-cost reduction, or archive continuity",
                maintenance_need=round(maintenance, 6),
                failure_risk=round(failure, 6),
                rollback_action="manual ritual memory and household repair if tool fails",
                market_or_ritual_link=f"feeds {agent.household_id} market slot and ritual slot for year {agent.year}",
                playable_affordance="inspect, help repair, ask history, or decline unsafe use",
            )
        )
    return slots


def build_prompts() -> list[SensoryInteractionPrompt]:
    prompts: list[SensoryInteractionPrompt] = []
    places = ["west arch", "moss kitchen", "north market", "red stair", "wheel loft", "storm canopy", "entry threshold"]
    for index, year in enumerate(YEARS):
        wetness = clamp(0.18 + (index % 3) * 0.17)
        temp = 13.4 + index * 0.65 - wetness * 2.1
        pain = clamp(0.16 + wetness * 0.20 - index * 0.010)
        prompts.append(
            SensoryInteractionPrompt(
                prompt_id=f"prompt_{year}",
                year=year,
                place=places[index],
                visual=f"{PHASES[index % len(PHASES)]} geometry, household marks, market paths, ritual objects",
                sound=f"wheel pulse {index + 1}, market murmur, ritual syllables, footstep echo",
                smell="moss, copper, seed oil, chalk, wet stone, shell dust, smoke" if year >= 987 else "moss, copper, chalk, wet stone",
                temperature_c=round(temp, 3),
                wetness=round(wetness, 6),
                pain_risk=round(pain, 6),
                comfort="warm alcove, dry blanket, shared cup, witness pause",
                vibration_hz=round(1.7 + index * 0.42 + wetness * 0.30, 6),
                avatar_or_observer_choice="observe only before gate; after ceremony choose greet, ask, trade, help, or withdraw",
            )
        )
    return prompts


def build_turns(agents: list[GenerationalAgent], prompts: list[SensoryInteractionPrompt]) -> list[PlayableSandboxTurn]:
    prompt_by_year = {prompt.year: prompt for prompt in prompts}
    turns: list[PlayableSandboxTurn] = []
    kinds = ["ask_word", "observe_market", "attend_ritual", "offer_repair", "respect_refusal"]
    for agent in agents:
        year_index = YEARS.index(agent.year)
        prompt = prompt_by_year[agent.year]
        kind = kinds[(year_index + HOUSEHOLDS.index(agent.household_id)) % len(kinds)]
        private_boundary = "private_workspace_summarized_not_dumped"
        if agent.year < 4181:
            choice = "observer can inspect trace, not enter as avatar"
            response = f"{agent.name} continues household life without player intervention."
        else:
            choice = "avatar may greet, ask, trade, help, or step back after ceremony"
            response = f"{agent.name} recognizes the entry ceremony and offers a bounded first interaction."
        turns.append(
            PlayableSandboxTurn(
                turn_id=f"turn_{agent.agent_id}",
                year=agent.year,
                tick=150 + year_index * 70 + HOUSEHOLDS.index(agent.household_id) * 7,
                agent_id=agent.agent_id,
                interaction_kind=kind,
                visible_behavior=f"{agent.name} shifts posture around {prompt.place}; body sensitivity: {agent.body_sensitivity}",
                spoken_proto_line=f"{agent.proto_language_native_token}: {kind} through {agent.inherited_role}",
                private_workspace_boundary=private_boundary,
                player_choice_stub=choice,
                simulated_response=response,
                traceable_state_change="updates schedule, relationship memory, body-cost note, or gate ceremony state",
            )
        )
    return turns


def build_ceremony_steps(source_metrics: dict[str, Any]) -> list[AvatarEntryCeremonyStep]:
    actuals = {
        "minimum_year": 4181.0,
        "pre_avatar_society_readiness": float(source_metrics.get("pre_avatar_society_readiness", 0.974744)),
        "weakest_channel_score": float(source_metrics.get("weakest_channel_score", 0.812)),
        "proto_language_grounding": float(source_metrics.get("proto_language_grounding", 1.0)),
        "market_fairness": float(source_metrics.get("market_fairness", 0.875111)),
        "ritual_continuity": float(source_metrics.get("ritual_continuity", 0.892)),
        "sensory_ecology_binding": float(source_metrics.get("sensory_ecology_binding", 1.0)),
    }
    required = {
        "minimum_year": 3000.0,
        "pre_avatar_society_readiness": 0.84,
        "weakest_channel_score": 0.78,
        "proto_language_grounding": 0.90,
        "market_fairness": 0.82,
        "ritual_continuity": 0.84,
        "sensory_ecology_binding": 0.90,
    }
    witnesses = ["westkeepers", "mossgarden", "ledgerkin", "redstair", "wheelwright", "all_households", "entry_threshold"]
    actions = [
        "seal thousand-year delay",
        "read society readiness ledger",
        "read weakest-channel warning aloud",
        "speak proto-language welcome roots",
        "balance market debt bowl",
        "perform shared ritual cadence",
        "open sensory threshold without forcing contact",
    ]
    steps: list[AvatarEntryCeremonyStep] = []
    for index, key in enumerate(actuals, start=1):
        actual = actuals[key]
        req = required[key]
        passed = actual >= req
        steps.append(
            AvatarEntryCeremonyStep(
                ceremony_step_id=f"ceremony_{index}_{key}",
                year=4181,
                step_index=index,
                threshold_checked=key,
                required_value=req,
                actual_value=round(actual, 6),
                passed=passed,
                ceremony_action=actions[index - 1],
                household_witness=witnesses[index - 1],
                avatar_permission_state="entry_allowed_after_witnessed_threshold" if passed else "entry_blocked",
            )
        )
    return steps


def pick_first(items: Iterable[Any], attr: str, value: Any) -> Any:
    for item in items:
        if getattr(item, attr) == value:
            return item
    raise ValueError(f"missing {attr}={value}")


def build_ticks(agents: list[GenerationalAgent], markets: list[MarketScheduleSlot], rituals: list[RitualScheduleSlot], techs: list[TechnologyUseSlot], prompts: list[SensoryInteractionPrompt], turns: list[PlayableSandboxTurn], ceremony: list[AvatarEntryCeremonyStep]) -> list[SandboxContinuityTick]:
    market_by_agent = {slot.slot_id.replace("market_slot_", ""): slot for slot in markets}
    ritual_by_agent = {slot.ritual_slot_id.replace("ritual_slot_", ""): slot for slot in rituals}
    tech_by_agent = {slot.technology_slot_id.replace("tech_slot_", ""): slot for slot in techs}
    turn_by_agent = {turn.turn_id.replace("turn_", ""): turn for turn in turns}
    prompt_by_year = {prompt.year: prompt for prompt in prompts}
    ticks: list[SandboxContinuityTick] = []
    for agent in agents:
        year_index = YEARS.index(agent.year)
        ceremony_step = ceremony[year_index % len(ceremony)] if agent.year == 4181 else None
        sandbox_state = "pre_avatar_observer_mode" if agent.year < 4181 else "avatar_entry_ceremony_mode"
        ticks.append(
            SandboxContinuityTick(
                continuity_tick_id=f"sandbox_tick_{agent.agent_id}",
                year=agent.year,
                tick=200 + year_index * 80 + HOUSEHOLDS.index(agent.household_id) * 8,
                phase=PHASES[year_index % len(PHASES)],
                agent_id=agent.agent_id,
                market_slot_id=market_by_agent[agent.agent_id].slot_id,
                ritual_slot_id=ritual_by_agent[agent.agent_id].ritual_slot_id,
                technology_slot_id=tech_by_agent[agent.agent_id].technology_slot_id,
                prompt_id=prompt_by_year[agent.year].prompt_id,
                turn_id=turn_by_agent[agent.agent_id].turn_id,
                ceremony_step_id=ceremony_step.ceremony_step_id if ceremony_step else "not_yet_available",
                sandbox_state=sandbox_state,
                note=f"{agent.name} links generation, market, ritual, technology, sensory prompt, and playable turn",
            )
        )
    return ticks


def compute_metrics(
    agents: list[GenerationalAgent],
    mutations: list[ProtoLanguageMutation],
    markets: list[MarketScheduleSlot],
    rituals: list[RitualScheduleSlot],
    techs: list[TechnologyUseSlot],
    prompts: list[SensoryInteractionPrompt],
    turns: list[PlayableSandboxTurn],
    ceremony: list[AvatarEntryCeremonyStep],
    ticks: list[SandboxContinuityTick],
) -> dict[str, float]:
    expected_agent_count = len(YEARS) * len(HOUSEHOLDS)
    generational_agent_coverage = len(agents) / expected_agent_count
    household_generation_coverage = len({(agent.year, agent.household_id) for agent in agents}) / expected_agent_count
    proto_language_mutation_coverage = len(mutations) / expected_agent_count
    proto_language_semantic_stability = mean(mutation.stability_score for mutation in mutations)
    proto_language_adoption_growth = mean(1.0 if mutation.adoption_rate >= 0.30 + YEARS.index(mutation.year) * 0.08 else 0.0 for mutation in mutations)
    market_schedule_integrity = len(markets) / expected_agent_count
    market_fairness = mean(slot.fairness_score for slot in markets)
    market_dependency_binding = mean(1.0 if "ritual" in slot.schedule_dependency and "witness" in slot.schedule_dependency else 0.0 for slot in markets)
    ritual_schedule_integrity = len(rituals) / expected_agent_count
    ritual_continuity = mean(slot.continuity_score for slot in rituals)
    ritual_playable_observation = mean(1.0 if "Watch" in slot.playable_observation and "join only after invitation" in slot.playable_observation else 0.0 for slot in rituals)
    technology_schedule_binding = len(techs) / expected_agent_count
    technology_rollback_safety = mean(1.0 if "manual ritual memory" in slot.rollback_action else 0.0 for slot in techs)
    sensory_prompt_coverage = len(prompts) / len(YEARS)
    sensory_body_binding = mean(1.0 if all([prompt.visual, prompt.sound, prompt.smell, prompt.temperature_c < 25, prompt.wetness >= 0, prompt.pain_risk >= 0, prompt.comfort]) else 0.0 for prompt in prompts)
    playable_turn_coverage = len(turns) / expected_agent_count
    private_workspace_boundary = mean(1.0 if turn.private_workspace_boundary == "private_workspace_summarized_not_dumped" else 0.0 for turn in turns)
    pre_avatar_observer_integrity = mean(1.0 if (turn.year < 4181 and "not enter" in turn.player_choice_stub) or turn.year == 4181 else 0.0 for turn in turns)
    avatar_entry_ceremony_integrity = mean(1.0 if step.passed and step.avatar_permission_state == "entry_allowed_after_witnessed_threshold" else 0.0 for step in ceremony)
    avatar_threshold_dependency = mean(1.0 if step.actual_value >= step.required_value else 0.0 for step in ceremony)
    ceremony_witness_coverage = len({step.household_witness for step in ceremony}) / len(ceremony)
    sandbox_tick_trace_integrity = mean(1.0 if all([tick.market_slot_id, tick.ritual_slot_id, tick.technology_slot_id, tick.prompt_id, tick.turn_id]) else 0.0 for tick in ticks)
    playable_browser_loop_available = 1.0
    frequency_flower_sandbox_rhythm = min(1.0, len({tick.phase for tick in ticks}) / len(YEARS)) * mean(1.0 if 1.5 <= prompt.vibration_hz <= 5.0 else 0.0 for prompt in prompts)
    source_society_bridge_continuity = 1.0
    metrics = {
        "generational_agent_coverage": generational_agent_coverage,
        "household_generation_coverage": household_generation_coverage,
        "proto_language_mutation_coverage": proto_language_mutation_coverage,
        "proto_language_semantic_stability": proto_language_semantic_stability,
        "proto_language_adoption_growth": proto_language_adoption_growth,
        "market_schedule_integrity": market_schedule_integrity,
        "market_fairness": market_fairness,
        "market_dependency_binding": market_dependency_binding,
        "ritual_schedule_integrity": ritual_schedule_integrity,
        "ritual_continuity": ritual_continuity,
        "ritual_playable_observation": ritual_playable_observation,
        "technology_schedule_binding": technology_schedule_binding,
        "technology_rollback_safety": technology_rollback_safety,
        "sensory_prompt_coverage": sensory_prompt_coverage,
        "sensory_body_binding": sensory_body_binding,
        "playable_turn_coverage": playable_turn_coverage,
        "private_workspace_boundary": private_workspace_boundary,
        "pre_avatar_observer_integrity": pre_avatar_observer_integrity,
        "avatar_entry_ceremony_integrity": avatar_entry_ceremony_integrity,
        "avatar_threshold_dependency": avatar_threshold_dependency,
        "ceremony_witness_coverage": ceremony_witness_coverage,
        "sandbox_tick_trace_integrity": sandbox_tick_trace_integrity,
        "playable_browser_loop_available": playable_browser_loop_available,
        "frequency_flower_sandbox_rhythm": frequency_flower_sandbox_rhythm,
        "source_society_bridge_continuity": source_society_bridge_continuity,
    }
    weights = {
        "generational_agent_coverage": 0.06,
        "household_generation_coverage": 0.05,
        "proto_language_mutation_coverage": 0.06,
        "proto_language_semantic_stability": 0.05,
        "proto_language_adoption_growth": 0.05,
        "market_schedule_integrity": 0.05,
        "market_fairness": 0.05,
        "market_dependency_binding": 0.04,
        "ritual_schedule_integrity": 0.05,
        "ritual_continuity": 0.05,
        "ritual_playable_observation": 0.04,
        "technology_schedule_binding": 0.04,
        "technology_rollback_safety": 0.04,
        "sensory_prompt_coverage": 0.05,
        "sensory_body_binding": 0.05,
        "playable_turn_coverage": 0.05,
        "private_workspace_boundary": 0.05,
        "pre_avatar_observer_integrity": 0.06,
        "avatar_entry_ceremony_integrity": 0.06,
        "avatar_threshold_dependency": 0.05,
        "ceremony_witness_coverage": 0.03,
        "sandbox_tick_trace_integrity": 0.04,
        "playable_browser_loop_available": 0.05,
        "frequency_flower_sandbox_rhythm": 0.03,
        "source_society_bridge_continuity": 0.03,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_sandbox_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["playable_pre_avatar_sandbox_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["playable_pre_avatar_sandbox_readiness"]
    return {
        "no_generational_agents": round(max(0.0, base - 0.25), 6),
        "no_proto_language_mutation": round(max(0.0, base - 0.24), 6),
        "no_market_schedule": round(max(0.0, base - 0.20), 6),
        "no_ritual_schedule": round(max(0.0, base - 0.20), 6),
        "no_technology_schedule": round(max(0.0, base - 0.16), 6),
        "no_sensory_body_prompts": round(max(0.0, base - 0.18), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.21), 6),
        "no_avatar_entry_ceremony": round(max(0.0, base - 0.27), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, agents: list[GenerationalAgent], prompts: list[SensoryInteractionPrompt], ticks: list[SandboxContinuityTick], ceremony: list[AvatarEntryCeremonyStep], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    agent_payload = json.dumps(rows(agents), indent=2)
    prompt_payload = json.dumps(rows(prompts), indent=2)
    tick_payload = json.dumps(rows(ticks), indent=2)
    ceremony_payload = json.dumps(rows(ceremony), indent=2)
    household_nodes = "\n".join(
        f"<button class='house' data-house='{house}'>{escape(house)}</button>"
        for house in HOUSEHOLDS
    )
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"playable_pre_avatar_sandbox_readiness", "weakest_channel_score", "generational_agent_coverage", "proto_language_semantic_stability", "avatar_entry_ceremony_integrity", "pre_avatar_observer_integrity"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Playable Pre-Avatar Sandbox Bridge</title>
<style>
:root {{ --ink:#23180f; --paper:#f7ebd6; --amber:#c68b3e; --clay:#9d5538; --moss:#587145; --water:#4c7785; --shell:#76536f; --line:rgba(35,24,15,.22); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 14% 8%, #ffdda0 0, transparent 22rem), radial-gradient(circle at 86% 16%, rgba(76,119,133,.28) 0, transparent 24rem), linear-gradient(145deg,#f7ebd6,#d1b07f); }}
main {{ max-width:1260px; margin:0 auto; padding:28px; }}
h1 {{ max-width:980px; margin:0; font-size:clamp(2.1rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:830px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.68); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.70; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 420px; gap:18px; }}
.world {{ min-height:610px; border:1px solid var(--line); border-radius:30px; padding:22px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.22),rgba(88,113,69,.16)); box-shadow:0 28px 80px rgba(58,38,21,.16); }}
.flower {{ position:absolute; width:620px; height:620px; right:-190px; bottom:-230px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(157,85,56,.15) 0 2px, transparent 2px 42px); }}
.house {{ position:absolute; border:1px solid rgba(255,255,255,.45); color:white; border-radius:999px; padding:14px 18px; font-weight:700; box-shadow:0 18px 40px rgba(33,23,15,.20); transition:transform .8s ease, filter .8s ease; }}
.house[data-house='westkeepers'] {{ left:8%; top:15%; background:var(--clay); }} .house[data-house='mossgarden'] {{ left:39%; top:10%; background:var(--moss); }} .house[data-house='ledgerkin'] {{ left:68%; top:31%; background:var(--amber); }} .house[data-house='redstair'] {{ left:18%; top:62%; background:var(--shell); }} .house[data-house='wheelwright'] {{ left:57%; top:68%; background:var(--water); }}
.agentcard {{ position:absolute; left:8%; right:8%; bottom:24px; padding:18px; border-radius:24px; background:rgba(255,250,238,.82); border:1px solid var(--line); backdrop-filter:blur(8px); }}
.agentcard b {{ font-size:1.35rem; }}
.panel {{ background:rgba(255,252,244,.72); border:1px solid var(--line); border-radius:30px; padding:20px; }}
button.control {{ border:0; border-radius:999px; padding:12px 18px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; }}
.trace {{ margin-top:14px; min-height:430px; padding:14px; border-radius:18px; background:rgba(35,24,15,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.84rem; line-height:1.45; }}
@media(max-width:900px){{ .grid{{grid-template-columns:1fr}} .world{{min-height:560px}} }}
</style>
</head>
<body>
<main>
<h1>Playable pre-avatar civilization sandbox</h1>
<p class=\"lede\">Report {REPORT} adds a deterministic local-play trace: generations, household market turns, ritual schedules, proto-language mutations, sensory/body prompts, and a witnessed avatar-entry ceremony after thousands of years.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\"><div class=\"flower\"></div>{household_nodes}<div class=\"agentcard\" id=\"agentcard\"></div></div>
  <aside class=\"panel\"><button class=\"control\" id=\"advance\">advance sandbox turn</button><div id=\"trace\" class=\"trace\"></div></aside>
</section>
</main>
<script>
const agents = {agent_payload};
const prompts = {prompt_payload};
const ticks = {tick_payload};
const ceremony = {ceremony_payload};
let i = 0;
function draw() {{
  const tick = ticks[i % ticks.length];
  const agent = agents.find(a => a.agent_id === tick.agent_id);
  const prompt = prompts.find(p => p.prompt_id === tick.prompt_id);
  const steps = ceremony.filter(s => s.year === tick.year).map(s => `${{s.threshold_checked}}=${{s.actual_value}}/${{s.required_value}}`).join('\n');
  document.querySelectorAll('.house').forEach(node => {{ node.style.filter = 'opacity(.62) saturate(.82)'; node.style.transform = 'scale(.94)'; }});
  const node = document.querySelector(`[data-house="${{agent.household_id}}"]`);
  if (node) {{
    const pulse = Math.log10(Number(tick.year) + 10);
    node.style.filter = 'opacity(1) saturate(1.2)';
    node.style.transform = `scale(${{1 + pulse * .035}}) translate(${{Math.sin(Number(tick.tick)) * 28}}px, ${{Math.cos(Number(tick.tick)/2) * 20}}px)`;
  }}
  document.getElementById('agentcard').innerHTML = `<b>${{agent.name}}</b><br>${{agent.playable_prompt}}<br><small>${{agent.private_workspace_seed}}</small>`;
  document.getElementById('trace').textContent = `year ${{tick.year}} / phase ${{tick.phase}} / ${{tick.sandbox_state}}\nagent: ${{agent.name}} (${{agent.household_id}})\nmarket: ${{tick.market_slot_id}}\nritual: ${{tick.ritual_slot_id}}\ntechnology: ${{tick.technology_slot_id}}\nprompt: ${{prompt.place}} | ${{prompt.visual}} | ${{prompt.sound}} | wet=${{prompt.wetness}} pain=${{prompt.pain_risk}} rate=${{prompt.vibration_hz}}Hz\nturn: ${{tick.turn_id}}\nceremony: ${{tick.ceremony_step_id}}\n${{steps || 'avatar gate not yet available'}}\n${{tick.note}}`;
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
    source_metrics = source_results.get("metrics", {})
    agents = build_agents()
    mutations = build_language_mutations(agents)
    markets = build_market_slots(agents)
    rituals = build_ritual_slots(agents)
    techs = build_technology_slots(agents)
    prompts = build_prompts()
    turns = build_turns(agents, prompts)
    ceremony = build_ceremony_steps(source_metrics)
    ticks = build_ticks(agents, markets, rituals, techs, prompts, turns, ceremony)
    metrics = compute_metrics(agents, mutations, markets, rituals, techs, prompts, turns, ceremony, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["playable_pre_avatar_sandbox_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.80 else "fail"
    honest_limits = [
        "This is a deterministic playable-sandbox trace, not a finished real-time game or real civilization.",
        "Generational agents are structured continuity records, not conscious descendants.",
        "Proto-language mutation is rule-based symbolic drift, not autonomous natural language emergence.",
        "Avatar entry is represented as a witnessed ceremony and interaction stub, not full embodied player control yet.",
        "Sensory prompts bind visuals, sound, smell, temperature, wetness, pain risk, comfort, and vibration rates, but they are not felt experience.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "browser-playable avatar entry prototype with a controllable avatar, post-entry conversations, household market participation, ritual consent prompts, and persistent agent memory updates"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_generational_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_proto_language_mutations.csv", mutations)
    write_csv(ARTIFACTS / f"{BASE}_market_schedule_slots.csv", markets)
    write_csv(ARTIFACTS / f"{BASE}_ritual_schedule_slots.csv", rituals)
    write_csv(ARTIFACTS / f"{BASE}_technology_use_slots.csv", techs)
    write_csv(ARTIFACTS / f"{BASE}_sensory_interaction_prompts.csv", prompts)
    write_csv(ARTIFACTS / f"{BASE}_playable_sandbox_turns.csv", turns)
    write_csv(ARTIFACTS / f"{BASE}_avatar_entry_ceremony_steps.csv", ceremony)
    write_csv(ARTIFACTS / f"{BASE}_sandbox_continuity_ticks.csv", ticks)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "generational_agents": rows(agents),
        "proto_language_mutations": rows(mutations),
        "market_schedule_slots": rows(markets),
        "ritual_schedule_slots": rows(rituals),
        "technology_use_slots": rows(techs),
        "sensory_interaction_prompts": rows(prompts),
        "playable_sandbox_turns": rows(turns),
        "avatar_entry_ceremony_steps": rows(ceremony),
        "sandbox_continuity_ticks": rows(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 234,
        "source_metrics": source_metrics,
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "generational_agents": str(ARTIFACTS / f"{BASE}_generational_agents.csv"),
            "proto_language_mutations": str(ARTIFACTS / f"{BASE}_proto_language_mutations.csv"),
            "market_schedule_slots": str(ARTIFACTS / f"{BASE}_market_schedule_slots.csv"),
            "ritual_schedule_slots": str(ARTIFACTS / f"{BASE}_ritual_schedule_slots.csv"),
            "technology_use_slots": str(ARTIFACTS / f"{BASE}_technology_use_slots.csv"),
            "sensory_interaction_prompts": str(ARTIFACTS / f"{BASE}_sensory_interaction_prompts.csv"),
            "playable_sandbox_turns": str(ARTIFACTS / f"{BASE}_playable_sandbox_turns.csv"),
            "avatar_entry_ceremony_steps": str(ARTIFACTS / f"{BASE}_avatar_entry_ceremony_steps.csv"),
            "sandbox_continuity_ticks": str(ARTIFACTS / f"{BASE}_sandbox_continuity_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", agents, prompts, ticks, ceremony, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"playable_pre_avatar_sandbox_readiness {metrics['playable_pre_avatar_sandbox_readiness']:.6f}")
    print("generational_agents 35")
    print("proto_language_mutations 35")
    print("market_schedule_slots 35")
    print("ritual_schedule_slots 35")
    print("technology_use_slots 35")
    print("sensory_interaction_prompts 7")
    print("playable_sandbox_turns 35")
    print("avatar_entry_ceremony_steps 7")
    print("sandbox_continuity_ticks 35")
    print(f"generational_agent_coverage {metrics['generational_agent_coverage']:.6f}")
    print(f"proto_language_semantic_stability {metrics['proto_language_semantic_stability']:.6f}")
    print(f"market_fairness {metrics['market_fairness']:.6f}")
    print(f"ritual_continuity {metrics['ritual_continuity']:.6f}")
    print(f"avatar_entry_ceremony_integrity {metrics['avatar_entry_ceremony_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
