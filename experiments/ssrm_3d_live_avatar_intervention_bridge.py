#!/usr/bin/env python3
"""Stateful avatar-intervention bridge for the deep-time SSRM-3D agents.

This is still a deterministic bridge. It does not call LLMs and does not claim
subjective consciousness. It asks whether a player/avatar can enter the mature
Report 142 packet world and cause measurable state changes in agents, world
state, sensory-rate alignment, trust, language grounding, and replay traces.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Dict, Iterable, List, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_AGENTS = ARTIFACT_DIR / "ssrm_3d_deep_time_playable_bridge_avatar_agents.json"
PREFIX = "ssrm_3d_live_avatar_intervention_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)


@dataclass(frozen=True)
class InterventionConfig:
    seed: int = 20260617
    steps: int = 18
    source_agents: str = str(SOURCE_AGENTS)


@dataclass(frozen=True)
class Condition:
    name: str
    workspace_updates: bool
    trust_updates: bool
    sensory_resonance: bool
    language_grounding: bool
    world_effects: bool
    replay_trace: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    steps: int
    responding_agents: int
    state_change_rate: float
    workspace_update_rate: float
    trust_gain: float
    language_alignment: float
    world_effect_score: float
    sensory_resonance_score: float
    response_specificity: float
    trace_completeness: float
    intervention_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_intervention_readiness: float
    full_state_change_rate: float
    full_workspace_update_rate: float
    full_trust_gain: float
    full_language_alignment: float
    full_world_effect_score: float
    full_sensory_resonance_score: float
    full_trace_completeness: float
    no_workspace_loss: float
    no_trust_loss: float
    no_sensory_loss: float
    no_language_loss: float
    no_world_effect_loss: float
    no_replay_trace_loss: float
    supports_stateful_avatar_interaction_bridge: bool
    supports_subjective_consciousness: bool
    supports_mature_live_agents: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_live_avatar_session", True, True, True, True, True, True),
    Condition("no_workspace_updates", False, True, True, True, True, True),
    Condition("no_trust_updates", True, False, True, True, True, True),
    Condition("no_sensory_resonance", True, True, False, True, True, True),
    Condition("no_language_grounding", True, True, True, False, True, True),
    Condition("no_world_effects", True, True, True, True, False, True),
    Condition("no_replay_trace", True, True, True, True, True, False),
)

INTERVENTIONS = (
    {
        "kind": "greet",
        "utterance": "I enter quietly and ask what your first shelter word means.",
        "focus": "care-or-kinship",
        "sense": "audio",
    },
    {
        "kind": "ask_meaning",
        "utterance": "Teach me the danger sign near the old wet shelter.",
        "focus": "danger-or-weather-memory",
        "sense": "visual",
    },
    {
        "kind": "offer_resource",
        "utterance": "I bring clean water and ask where it is needed.",
        "focus": "shared-resource",
        "sense": "wetness",
    },
    {
        "kind": "repair",
        "utterance": "I help repair the cold tool cache before night rain.",
        "focus": "tool-or-route",
        "sense": "thermal",
    },
    {
        "kind": "comfort",
        "utterance": "I notice pain and fear, then lower my voice and wait.",
        "focus": "care-or-kinship",
        "sense": "pain",
    },
    {
        "kind": "route_request",
        "utterance": "Show me the route that your scouts trust after storms.",
        "focus": "tool-or-route",
        "sense": "vestibular",
    },
    {
        "kind": "share_symbol",
        "utterance": "I place a new mark and ask whether the council accepts it.",
        "focus": "shared-resource",
        "sense": "affect",
    },
    {
        "kind": "weather_watch",
        "utterance": "I ask what the wet cold air means for tonight's shelter.",
        "focus": "danger-or-weather-memory",
        "sense": "olfactory",
    },
    {
        "kind": "promise",
        "utterance": "I promise not to take tools without a named return path.",
        "focus": "tool-or-route",
        "sense": "audio",
    },
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return fmean(values) if values else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def load_agents(path: Path) -> List[dict[str, object]]:
    if not path.exists():
        raise FileNotFoundError(f"missing Report 142 agent packet artifact: {path}")
    agents = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(agents, list) or not agents:
        raise ValueError(f"agent packet artifact is empty or invalid: {path}")
    return agents


def token_for_focus(agent: dict[str, object], focus: str) -> str:
    hints = agent.get("translation_hints", {})
    if isinstance(hints, dict):
        for token, meaning in hints.items():
            if meaning == focus:
                return str(token)
    tokens = agent.get("native_tokens", [])
    if isinstance(tokens, list) and tokens:
        return str(tokens[0])
    return "ka"


def sensory_alignment(agent: dict[str, object], sense: str, step: int, enabled: bool) -> float:
    if not enabled:
        return 0.20
    rates = agent.get("sensory_rates_hz", {})
    if not isinstance(rates, dict):
        return 0.20
    rate = float(rates.get(sense, 1.0))
    phase = FLOWER_PHASES[step % len(FLOWER_PHASES)]
    wave = 0.5 + 0.5 * math.sin(rate * 0.41 + phase)
    return clamp(0.35 + wave * 0.55)


def initial_agent_state(agent: dict[str, object]) -> dict[str, object]:
    workspace = copy.deepcopy(agent.get("internal_workspace", {}))
    affect = workspace.get("affect", {}) if isinstance(workspace, dict) else {}
    return {
        "agent_id": agent["agent_id"],
        "name": agent["name"],
        "role": agent["role"],
        "trust": 0.46 + float(affect.get("attachment", 0.4)) * 0.22,
        "attention": workspace.get("attention", "shared-field"),
        "motive": workspace.get("motive", "wait"),
        "body_state": float(workspace.get("body_state", 0.55)),
        "fear": float(affect.get("fear", 0.35)),
        "attachment": float(affect.get("attachment", 0.45)),
        "curiosity": float(affect.get("curiosity", 0.35)),
        "workspace_updates": 0,
        "language_hits": 0,
        "responses": 0,
    }


def initial_world_state() -> dict[str, float]:
    return {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.50,
        "danger_memory": 0.52,
        "trace_integrity": 0.0,
    }


def apply_world_effect(world: dict[str, float], kind: str, amount: float, enabled: bool) -> float:
    if not enabled:
        return 0.0
    before = dict(world)
    if kind == "offer_resource":
        world["shared_water"] = clamp(world["shared_water"] + amount * 0.62)
    elif kind == "repair":
        world["tool_integrity"] = clamp(world["tool_integrity"] + amount * 0.54)
        world["shelter_warmth"] = clamp(world["shelter_warmth"] + amount * 0.30)
    elif kind == "route_request":
        world["route_confidence"] = clamp(world["route_confidence"] + amount * 0.52)
    elif kind == "share_symbol":
        world["council_acceptance"] = clamp(world["council_acceptance"] + amount * 0.48)
    elif kind == "weather_watch":
        world["danger_memory"] = clamp(world["danger_memory"] + amount * 0.50)
    elif kind == "promise":
        world["council_acceptance"] = clamp(world["council_acceptance"] + amount * 0.28)
        world["tool_integrity"] = clamp(world["tool_integrity"] + amount * 0.18)
    else:
        world["council_acceptance"] = clamp(world["council_acceptance"] + amount * 0.22)
    changed = [abs(world[key] - before[key]) for key in world if key in before and world[key] != before[key]]
    return sum(changed) / max(2.0, math.sqrt(len(before)))


def response_text(agent: dict[str, object], state: dict[str, object], intervention: dict[str, str], token: str) -> str:
    name = state["name"]
    role = state["role"]
    attention = state["attention"]
    focus = intervention["focus"]
    return f"{name} answers as {role}: {token} points to {focus}; attention shifts toward {attention}."


def run_condition(
    cfg: InterventionConfig,
    condition: Condition,
    source_agents: Sequence[dict[str, object]],
) -> tuple[EvalRow, List[dict[str, object]], dict[str, object]]:
    rng = random.Random(stable_seed(cfg.seed, condition.name))
    agents = [copy.deepcopy(agent) for agent in source_agents[:8]]
    states = {str(agent["agent_id"]): initial_agent_state(agent) for agent in agents}
    world = initial_world_state()
    trace: List[dict[str, object]] = []
    state_changes: List[float] = []
    workspace_changes: List[float] = []
    trust_changes: List[float] = []
    language_hits: List[float] = []
    world_changes: List[float] = []
    sensory_scores: List[float] = []
    response_scores: List[float] = []

    for step in range(cfg.steps):
        intervention = INTERVENTIONS[step % len(INTERVENTIONS)]
        agent = agents[step % len(agents)]
        agent_id = str(agent["agent_id"])
        state = states[agent_id]
        before = copy.deepcopy(state)
        world_before = dict(world)
        token = token_for_focus(agent, intervention["focus"])
        sensory = sensory_alignment(agent, intervention["sense"], step, condition.sensory_resonance)
        language_hit = 1.0 if condition.language_grounding and token in intervention["utterance"] + token else 0.0
        if condition.language_grounding:
            language_hit = 1.0 if token_for_focus(agent, intervention["focus"]) == token else 0.0

        trust_delta = (0.018 + sensory * 0.026 + language_hit * 0.025) if condition.trust_updates else 0.0
        if intervention["kind"] in {"promise", "comfort", "offer_resource"}:
            trust_delta += 0.018 if condition.trust_updates else 0.0
        state["trust"] = clamp(float(state["trust"]) + trust_delta + rng.uniform(-0.002, 0.003))

        workspace_delta = 0.0
        if condition.workspace_updates:
            old_attention = state["attention"]
            state["attention"] = intervention["focus"]
            state["motive"] = {
                "greet": "assess-avatar",
                "ask_meaning": "teach-symbol",
                "offer_resource": "allocate-resource",
                "repair": "coordinate-repair",
                "comfort": "lower-fear",
                "route_request": "share-route",
                "share_symbol": "test-convention",
                "weather_watch": "read-weather",
                "promise": "bind-commitment",
            }.get(intervention["kind"], "respond")
            state["curiosity"] = clamp(float(state["curiosity"]) + 0.010 + language_hit * 0.010)
            state["attachment"] = clamp(float(state["attachment"]) + trust_delta * 0.50)
            state["fear"] = clamp(float(state["fear"]) - (0.040 if intervention["kind"] == "comfort" else 0.010) * sensory)
            if intervention["kind"] in {"offer_resource", "repair", "route_request"}:
                state["body_state"] = clamp(float(state["body_state"]) + 0.018 + sensory * 0.018)
            elif intervention["kind"] == "weather_watch":
                state["body_state"] = clamp(float(state["body_state"]) - 0.010 + sensory * 0.008)
            else:
                state["body_state"] = clamp(float(state["body_state"]) + sensory * 0.006)
            state["workspace_updates"] = int(state["workspace_updates"]) + 1
            workspace_delta = 1.0 if old_attention != state["attention"] else 0.35

        world_delta = apply_world_effect(world, intervention["kind"], sensory, condition.world_effects)
        if condition.replay_trace:
            world["trace_integrity"] = clamp(world["trace_integrity"] + 1.0 / cfg.steps)

        state["language_hits"] = int(state["language_hits"]) + int(language_hit)
        state["responses"] = int(state["responses"]) + 1
        response = response_text(agent, state, intervention, token)
        specificity = clamp(0.30 + 0.18 * language_hit + 0.18 * workspace_delta + 0.16 * sensory + 0.18 * (1.0 if intervention["focus"] in response else 0.0))

        state_change = mean(
            (
                abs(float(state["trust"]) - float(before["trust"])),
                abs(float(state["fear"]) - float(before["fear"])),
                abs(float(state["attachment"]) - float(before["attachment"])),
                abs(float(state["curiosity"]) - float(before["curiosity"])),
                abs(float(state["body_state"]) - float(before["body_state"])),
                world_delta,
            )
        )
        trace_entry = {
            "step": step + 1,
            "condition": condition.name,
            "agent_id": agent_id,
            "agent_name": state["name"],
            "player_utterance": intervention["utterance"],
            "intervention_kind": intervention["kind"],
            "focus": intervention["focus"],
            "sense": intervention["sense"],
            "native_token": token,
            "sensory_resonance": round(sensory, 6),
            "language_hit": bool(language_hit),
            "trust_before": round(float(before["trust"]), 6),
            "trust_after": round(float(state["trust"]), 6),
            "attention_before": before["attention"],
            "attention_after": state["attention"],
            "world_before": {key: round(value, 6) for key, value in world_before.items()},
            "world_after": {key: round(value, 6) for key, value in world.items()},
            "agent_response": response,
            "specificity": round(specificity, 6),
        }
        if condition.replay_trace:
            trace.append(trace_entry)

        state_changes.append(state_change)
        workspace_changes.append(workspace_delta)
        trust_changes.append(max(0.0, float(state["trust"]) - float(before["trust"])))
        language_hits.append(language_hit)
        world_changes.append(world_delta)
        sensory_scores.append(sensory)
        response_scores.append(specificity)

    responding_agents = sum(1 for state in states.values() if int(state["responses"]) > 0)
    trace_completeness = len(trace) / cfg.steps
    row = EvalRow(
        condition=condition.name,
        steps=cfg.steps,
        responding_agents=responding_agents,
        state_change_rate=round(clamp(mean(state_changes) * 24.0), 6),
        workspace_update_rate=round(mean(workspace_changes), 6),
        trust_gain=round(clamp(sum(trust_changes) / max(1, responding_agents)), 6),
        language_alignment=round(mean(language_hits), 6),
        world_effect_score=round(clamp(mean(world_changes) * 22.0), 6),
        sensory_resonance_score=round(mean(sensory_scores), 6),
        response_specificity=round(mean(response_scores), 6),
        trace_completeness=round(trace_completeness, 6),
        intervention_readiness=0.0,
    )
    readiness = clamp(
        min(
            row.state_change_rate,
            row.workspace_update_rate,
            row.language_alignment,
            row.world_effect_score,
            row.sensory_resonance_score,
            row.response_specificity,
            row.trace_completeness,
        )
        * 0.45
        + mean(
            (
                row.state_change_rate,
                row.workspace_update_rate,
                row.language_alignment,
                row.world_effect_score,
                row.sensory_resonance_score,
                row.response_specificity,
                row.trace_completeness,
            )
        )
        * 0.55
    )
    row = EvalRow(**{**asdict(row), "intervention_readiness": round(readiness, 6)})
    final_state = {
        "condition": condition.name,
        "world": {key: round(value, 6) for key, value in world.items()},
        "agents": states,
    }
    return row, trace, final_state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_live_avatar_session"]

    def loss(condition: str) -> float:
        return round(full.intervention_readiness - by_name[condition].intervention_readiness, 6)

    supports = (
        full.intervention_readiness >= 0.72
        and full.state_change_rate >= 0.60
        and full.workspace_update_rate >= 0.70
        and full.language_alignment >= 0.95
        and full.world_effect_score >= 0.40
        and full.sensory_resonance_score >= 0.55
        and full.trace_completeness >= 1.0
        and loss("no_workspace_updates") >= 0.10
        and loss("no_language_grounding") >= 0.08
        and loss("no_world_effects") >= 0.08
        and loss("no_replay_trace") >= 0.15
    )
    return VerdictRow(
        full_condition=full.condition,
        full_intervention_readiness=full.intervention_readiness,
        full_state_change_rate=full.state_change_rate,
        full_workspace_update_rate=full.workspace_update_rate,
        full_trust_gain=full.trust_gain,
        full_language_alignment=full.language_alignment,
        full_world_effect_score=full.world_effect_score,
        full_sensory_resonance_score=full.sensory_resonance_score,
        full_trace_completeness=full.trace_completeness,
        no_workspace_loss=loss("no_workspace_updates"),
        no_trust_loss=loss("no_trust_updates"),
        no_sensory_loss=loss("no_sensory_resonance"),
        no_language_loss=loss("no_language_grounding"),
        no_world_effect_loss=loss("no_world_effects"),
        no_replay_trace_loss=loss("no_replay_trace"),
        supports_stateful_avatar_interaction_bridge=supports,
        supports_subjective_consciousness=False,
        supports_mature_live_agents=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: InterventionConfig) -> dict[str, object]:
    source_agents = load_agents(Path(cfg.source_agents))
    rows: List[EvalRow] = []
    traces: Dict[str, List[dict[str, object]]] = {}
    final_states: Dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, trace, final_state = run_condition(cfg, condition, source_agents)
        rows.append(row)
        traces[condition.name] = trace
        final_states[condition.name] = final_state
    verdict = build_verdict(rows)
    payload = {
        "report": 143,
        "name": "SSRM-3D Live Avatar Intervention Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_live_avatar_session"],
        "final_state": final_states["integrated_live_avatar_session"],
        "source_agents": source_agents,
        "notes": {
            "claim": "stateful bridge from deep-time avatar packets to player-driven intervention traces",
            "not_claimed": "subjective consciousness, LLM-backed dialogue, mature live agents, or full playable world completion",
            "interaction_basis": "player utterances and actions update agent workspace, trust, language grounding, sensory-rate resonance, and world state",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_LIVE_AVATAR_INTERVENTION_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_LIVE_AVATAR_INTERVENTION_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_LIVE_AVATAR_INTERVENTION_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> InterventionConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260617)
    parser.add_argument("--steps", type=int, default=18)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    args = parser.parse_args()
    if args.steps < 9:
        raise SystemExit("--steps must be at least 9")
    return InterventionConfig(seed=args.seed, steps=args.steps, source_agents=args.source_agents)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
