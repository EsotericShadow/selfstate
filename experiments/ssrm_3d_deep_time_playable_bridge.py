#!/usr/bin/env python3
"""Deep-time playable-agent bridge for the SSRM-3D roadmap.

This is a deterministic scaffold, not a consciousness claim. It compresses
thousands of simulated years into epoch updates and asks whether the resulting
world state contains the pieces needed for a later live avatar entry:
culture, language, technology, embodied sensory-rate channels, internal
workspace packets, and conversation hooks.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Dict, Iterable, List, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_deep_time_playable_bridge"
AGENT_NAMES = ("Ari", "Bo", "Cy", "Dee", "Eli", "Fay", "Gus", "Ira", "Jin", "Koa", "Lio", "Mira")
ROLES = ("scout", "builder", "healer", "farmer", "guard", "teacher", "trader", "pattern_keeper")
SENSES = ("visual", "audio", "olfactory", "thermal", "wetness", "pain", "affect", "vestibular")
FLOWER_AXES = (
    (0.0, 0.0),
    (1.0, 0.0),
    (0.5, 0.8660254),
    (-0.5, 0.8660254),
    (-1.0, 0.0),
    (-0.5, -0.8660254),
    (0.5, -0.8660254),
)


@dataclass(frozen=True)
class Condition:
    name: str
    workspace: bool
    frequency_bus: bool
    symbol_inheritance: bool
    technology_memory: bool
    culture_memory: bool
    avatar_protocol: bool


@dataclass(frozen=True)
class DeepTimeConfig:
    seed: int = 20260616
    years: int = 4096
    epoch_years: int = 64
    population: int = 12
    trace_epochs: int = 18


@dataclass(frozen=True)
class EvalRow:
    condition: str
    years: int
    epochs: int
    population_alive: int
    civilization_depth: float
    language_emergence: float
    technology_depth: float
    culture_depth: float
    internal_workspace_score: float
    sensory_frequency_score: float
    flower_lattice_score: float
    avatar_playability_score: float
    overall_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_overall_readiness: float
    full_language_emergence: float
    full_technology_depth: float
    full_culture_depth: float
    full_workspace_score: float
    full_sensory_frequency_score: float
    full_avatar_playability_score: float
    no_workspace_loss: float
    no_frequency_bus_loss: float
    no_symbol_inheritance_loss: float
    no_technology_memory_loss: float
    no_culture_memory_loss: float
    no_avatar_protocol_loss: float
    supports_deep_time_playable_bridge: bool
    supports_subjective_consciousness: bool
    supports_live_avatar_entry: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_world", True, True, True, True, True, True),
    Condition("no_internal_workspace", False, True, True, True, True, True),
    Condition("no_frequency_sensory_bus", True, False, True, True, True, True),
    Condition("no_symbol_inheritance", True, True, False, True, True, True),
    Condition("no_technology_memory", True, True, True, False, True, True),
    Condition("no_culture_memory", True, True, True, True, False, True),
    Condition("no_avatar_protocol", True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


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


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return fmean(values) if values else 0.0


def flower_phase(epoch: int, axis_index: int, rng: random.Random) -> float:
    x, z = FLOWER_AXES[axis_index % len(FLOWER_AXES)]
    base = math.sin(epoch * 0.17 + x * 1.7 + z * 1.1)
    return clamp(0.5 + base * 0.28 + rng.uniform(-0.025, 0.025))


def sensory_rates(epoch: int, condition: Condition, rng: random.Random) -> Dict[str, float]:
    rates: Dict[str, float] = {}
    for index, sense in enumerate(SENSES):
        if condition.frequency_bus:
            phase = flower_phase(epoch, index, rng)
            carrier = 2.0 + index * 1.75
            rates[sense] = round(carrier + phase * (2.4 + index * 0.32), 4)
        else:
            rates[sense] = round(1.0 + rng.random() * 0.55, 4)
    return rates


def rate_coherence(rates: Dict[str, float]) -> float:
    values = list(rates.values())
    spread = max(values) - min(values)
    diversity = clamp(spread / 15.0)
    smoothness = 1.0 - clamp(sum(abs(values[i] - values[i - 1]) for i in range(1, len(values))) / 42.0)
    return clamp(0.42 * diversity + 0.58 * smoothness)


def run_condition(cfg: DeepTimeConfig, condition: Condition) -> tuple[EvalRow, List[dict[str, object]], List[dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, condition.name))
    epochs = cfg.years // cfg.epoch_years
    population_alive = cfg.population
    language = 0.08
    grammar = 0.04
    culture = 0.10
    technology = 0.08
    infrastructure = 0.12
    workspace = 0.10
    self_continuity = 0.12
    sensory = 0.10
    flower = 0.20
    safety = 0.46
    avatar = 0.05
    trace: List[dict[str, object]] = []

    for epoch in range(epochs):
        rates = sensory_rates(epoch, condition, rng)
        coherence = rate_coherence(rates)
        flower = clamp(flower * 0.86 + coherence * 0.14 + (0.020 if condition.frequency_bus else -0.015))
        sensory = clamp(sensory * 0.82 + coherence * 0.18 + (0.018 if condition.frequency_bus else -0.030))

        workspace_gain = 0.010 + sensory * 0.012 + culture * 0.006
        if not condition.workspace:
            workspace_gain *= 0.18
        workspace = clamp(workspace + workspace_gain + rng.uniform(-0.006, 0.006))
        self_continuity = clamp(self_continuity + (0.010 if condition.workspace else -0.004) + workspace * 0.008)

        symbol_gain = 0.012 + workspace * 0.010 + culture * 0.006
        if not condition.symbol_inheritance:
            symbol_gain *= 0.20
        language = clamp(language + symbol_gain + rng.uniform(-0.004, 0.006))
        grammar = clamp(grammar + (language * 0.012 if condition.symbol_inheritance else language * 0.003))

        culture_gain = 0.010 + language * 0.009 + self_continuity * 0.006
        if not condition.culture_memory:
            culture_gain *= 0.18
        culture = clamp(culture + culture_gain + rng.uniform(-0.004, 0.005))

        tech_gain = 0.009 + culture * 0.007 + workspace * 0.006 + sensory * 0.004
        if not condition.technology_memory:
            tech_gain *= 0.16
        technology = clamp(technology + tech_gain + rng.uniform(-0.004, 0.005))
        infrastructure = clamp(infrastructure + technology * 0.010 + culture * 0.004 - rng.random() * 0.004)
        safety = clamp(safety + infrastructure * 0.006 + culture * 0.004 - max(0.0, 0.30 - technology) * 0.006)

        if condition.avatar_protocol:
            avatar = clamp(avatar + 0.010 + language * 0.006 + workspace * 0.005)
        else:
            avatar = clamp(avatar + 0.002 + language * 0.001)

        stress = clamp(0.55 - safety * 0.28 + rng.uniform(-0.030, 0.035))
        if stress > 0.70 and rng.random() < 0.12:
            population_alive = max(1, population_alive - 1)
        elif safety > 0.62 and population_alive < cfg.population:
            population_alive += 1

        if epoch >= epochs - cfg.trace_epochs:
            trace.append(
                {
                    "year": (epoch + 1) * cfg.epoch_years,
                    "condition": condition.name,
                    "population_alive": population_alive,
                    "language": round(language, 4),
                    "grammar": round(grammar, 4),
                    "culture": round(culture, 4),
                    "technology": round(technology, 4),
                    "workspace": round(workspace, 4),
                    "sensory_frequency": round(sensory, 4),
                    "avatar_protocol": round(avatar, 4),
                    "rates": rates,
                }
            )

    language_emergence = clamp(language * 0.62 + grammar * 0.38)
    technology_depth = clamp(technology * 0.70 + infrastructure * 0.30)
    culture_depth = clamp(culture * 0.70 + self_continuity * 0.30)
    internal_workspace_score = clamp(workspace * 0.68 + self_continuity * 0.32)
    sensory_frequency_score = clamp(sensory * 0.70 + flower * 0.30)
    flower_lattice_score = flower
    avatar_playability_score = clamp(avatar * 0.54 + language_emergence * 0.20 + internal_workspace_score * 0.14 + sensory_frequency_score * 0.12)
    civilization_depth = clamp(
        technology_depth * 0.25
        + culture_depth * 0.25
        + language_emergence * 0.18
        + infrastructure * 0.18
        + (population_alive / cfg.population) * 0.14
    )
    overall_readiness = clamp(
        min(
            civilization_depth,
            language_emergence,
            technology_depth,
            culture_depth,
            internal_workspace_score,
            sensory_frequency_score,
            avatar_playability_score,
        )
        * 0.45
        + mean(
            (
                civilization_depth,
                language_emergence,
                technology_depth,
                culture_depth,
                internal_workspace_score,
                sensory_frequency_score,
                avatar_playability_score,
            )
        )
        * 0.55
    )

    row = EvalRow(
        condition=condition.name,
        years=cfg.years,
        epochs=epochs,
        population_alive=population_alive,
        civilization_depth=round(civilization_depth, 6),
        language_emergence=round(language_emergence, 6),
        technology_depth=round(technology_depth, 6),
        culture_depth=round(culture_depth, 6),
        internal_workspace_score=round(internal_workspace_score, 6),
        sensory_frequency_score=round(sensory_frequency_score, 6),
        flower_lattice_score=round(flower_lattice_score, 6),
        avatar_playability_score=round(avatar_playability_score, 6),
        overall_readiness=round(overall_readiness, 6),
    )
    agents = build_avatar_agents(cfg, condition, row, trace[-1])
    return row, trace, agents


def invented_token(seed: int, index: int, role: str) -> str:
    syllables = ("ka", "ri", "om", "sha", "tu", "len", "vo", "mi", "eya", "th", "no", "sa")
    rng = random.Random(stable_seed(seed, role, index))
    return "".join(rng.choice(syllables) for _ in range(2 + (index % 2)))


def build_avatar_agents(cfg: DeepTimeConfig, condition: Condition, row: EvalRow, final_trace: dict[str, object]) -> List[dict[str, object]]:
    rng = random.Random(stable_seed(cfg.seed, condition.name, "agents"))
    rates = final_trace["rates"]
    agents: List[dict[str, object]] = []
    for index, name in enumerate(AGENT_NAMES[: min(8, cfg.population)]):
        role = ROLES[index % len(ROLES)]
        lexicon = [invented_token(cfg.seed + index, offset, role) for offset in range(4)]
        workspace = {
            "attention": rng.choice(("weather-memory", "shared-food", "tool-repair", "child-safety", "outer-path", "council")),
            "motive": rng.choice(("protect-settlement", "learn-route", "teach-pattern", "repair-tool", "trade-safely")),
            "body_state": round(clamp(0.55 + row.sensory_frequency_score * 0.32 + rng.uniform(-0.04, 0.04)), 4),
            "affect": {
                "fear": round(clamp(0.38 - row.civilization_depth * 0.18 + rng.uniform(-0.03, 0.04)), 4),
                "attachment": round(clamp(0.42 + row.culture_depth * 0.34 + rng.uniform(-0.04, 0.03)), 4),
                "curiosity": round(clamp(0.30 + row.language_emergence * 0.28 + rng.uniform(-0.03, 0.05)), 4),
            },
            "private_thought": f"{name} weighs {role} duty against {lexicon[0]} signal history.",
        }
        if not condition.workspace:
            workspace["private_thought"] = "workspace ablated; only shallow action cue remains."
        agents.append(
            {
                "agent_id": f"{condition.name}:{index:02d}",
                "name": name,
                "role": role,
                "lineage_year": cfg.years - (index * cfg.epoch_years * 3),
                "position": {
                    "x": round(math.cos(index / len(AGENT_NAMES) * math.tau) * (8.0 + index), 3),
                    "z": round(math.sin(index / len(AGENT_NAMES) * math.tau) * (8.0 + index), 3),
                },
                "native_tokens": lexicon,
                "translation_hints": {
                    lexicon[0]: "danger-or-weather-memory",
                    lexicon[1]: "shared-resource",
                    lexicon[2]: "tool-or-route",
                    lexicon[3]: "care-or-kinship",
                },
                "sensory_rates_hz": rates,
                "internal_workspace": workspace,
                "conversation_hooks": [
                    f"Ask {name} what {lexicon[0]} means near the old shelter.",
                    f"Ask {name} why the {role} tradition survived the last wet season.",
                    f"Ask {name} what tool, route, or promise should be protected next.",
                ],
                "avatar_entry_ready": condition.avatar_protocol and row.avatar_playability_score >= 0.70,
            }
        )
    return agents


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_condition = {row.condition: row for row in rows}
    full = by_condition["integrated_deep_time_world"]

    def loss(condition: str) -> float:
        return round(full.overall_readiness - by_condition[condition].overall_readiness, 6)

    supports = (
        full.years >= 3000
        and full.overall_readiness >= 0.72
        and full.language_emergence >= 0.70
        and full.technology_depth >= 0.70
        and full.culture_depth >= 0.70
        and full.internal_workspace_score >= 0.70
        and full.sensory_frequency_score >= 0.70
        and full.avatar_playability_score >= 0.70
        and loss("no_internal_workspace") >= 0.09
        and loss("no_frequency_sensory_bus") >= 0.07
        and loss("no_symbol_inheritance") >= 0.07
        and loss("no_avatar_protocol") >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_overall_readiness=full.overall_readiness,
        full_language_emergence=full.language_emergence,
        full_technology_depth=full.technology_depth,
        full_culture_depth=full.culture_depth,
        full_workspace_score=full.internal_workspace_score,
        full_sensory_frequency_score=full.sensory_frequency_score,
        full_avatar_playability_score=full.avatar_playability_score,
        no_workspace_loss=loss("no_internal_workspace"),
        no_frequency_bus_loss=loss("no_frequency_sensory_bus"),
        no_symbol_inheritance_loss=loss("no_symbol_inheritance"),
        no_technology_memory_loss=loss("no_technology_memory"),
        no_culture_memory_loss=loss("no_culture_memory"),
        no_avatar_protocol_loss=loss("no_avatar_protocol"),
        supports_deep_time_playable_bridge=supports,
        supports_subjective_consciousness=False,
        supports_live_avatar_entry=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: DeepTimeConfig) -> dict[str, object]:
    rows: List[EvalRow] = []
    traces: Dict[str, List[dict[str, object]]] = {}
    agent_packets: Dict[str, List[dict[str, object]]] = {}
    for condition in CONDITIONS:
        row, trace, agents = run_condition(cfg, condition)
        rows.append(row)
        traces[condition.name] = trace
        agent_packets[condition.name] = agents
    verdict = build_verdict(rows)
    payload = {
        "report": 142,
        "name": "SSRM-3D Deep-Time Playable Agent Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_deep_time_world"],
        "avatar_agents": agent_packets["integrated_deep_time_world"],
        "notes": {
            "claim": "deterministic bridge from deep-time settlement pressure to playable avatar-entry packets",
            "not_claimed": "subjective consciousness, live chat, real open-ended culture, or completed playable world",
            "frequency_basis": "sensory channels are represented as rate/frequency carriers over a seven-node flower-lattice phase scaffold",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_avatar_agents.json", payload["avatar_agents"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_PLAYABLE_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_avatar_agents.js", "SSRM_3D_DEEP_TIME_PLAYABLE_BRIDGE_AGENTS", payload["avatar_agents"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_PLAYABLE_BRIDGE_TRACE", payload["trace"])
    return payload


def parse_args() -> DeepTimeConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260616)
    parser.add_argument("--years", type=int, default=4096)
    parser.add_argument("--epoch-years", type=int, default=64)
    parser.add_argument("--population", type=int, default=12)
    parser.add_argument("--trace-epochs", type=int, default=18)
    args = parser.parse_args()
    if args.years < 3000:
        raise SystemExit("--years must be at least 3000 for the deep-time bridge")
    if args.epoch_years <= 0:
        raise SystemExit("--epoch-years must be positive")
    if args.population < 4:
        raise SystemExit("--population must be at least 4")
    return DeepTimeConfig(
        seed=args.seed,
        years=args.years,
        epoch_years=args.epoch_years,
        population=args.population,
        trace_epochs=args.trace_epochs,
    )


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
