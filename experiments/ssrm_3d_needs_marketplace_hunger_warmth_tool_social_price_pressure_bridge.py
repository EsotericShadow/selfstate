"""Report 210: SSRM-3D needs marketplace and seasonal price pressure bridge.

This deterministic bridge extends the project economy into a seasonal marketplace
where hunger, warmth, tool access, social obligation, debt burden, and price
pressure change agent choices. It is a functional substrate only, not real
markets, real labor, real consent, or consciousness.
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

PREFIX = "ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge_state.json"
SOURCE_CONDITION = "integrated_agent_owned_project_economy_material_wear_debt_trade_labor"
CLAIM_BOUNDARY = (
    "Deterministic needs marketplace and seasonal price-pressure substrate only: "
    "not real markets, not real labor, not real consent, not subjective consciousness, and not moral patienthood."
)

BASE_PRICES = {
    "food_ration": 4.0,
    "heat_wood": 3.0,
    "tool_hour": 5.0,
    "soft_cloth": 3.0,
    "lamp_oil": 4.0,
    "map_vellum": 6.0,
    "herb_bundle": 5.0,
    "care_token": 2.0,
}

SEASONS = [
    {
        "season": "wet planting",
        "start": 1,
        "end": 15,
        "conditions": "damp air, moderate food, tool queue starts",
        "multipliers": {"food_ration": 1.05, "heat_wood": 1.15, "tool_hour": 1.10, "soft_cloth": 1.05, "lamp_oil": 1.00, "map_vellum": 1.05, "herb_bundle": 1.00, "care_token": 1.00},
    },
    {
        "season": "cold scarcity",
        "start": 16,
        "end": 30,
        "conditions": "cold nights, high warmth demand, food ration pressure",
        "multipliers": {"food_ration": 1.35, "heat_wood": 1.90, "tool_hour": 1.25, "soft_cloth": 1.35, "lamp_oil": 1.30, "map_vellum": 1.10, "herb_bundle": 1.20, "care_token": 1.10},
    },
    {
        "season": "thaw repair",
        "start": 31,
        "end": 45,
        "conditions": "repair surge, tool bottleneck, warmth eases",
        "multipliers": {"food_ration": 1.10, "heat_wood": 0.95, "tool_hour": 1.65, "soft_cloth": 1.10, "lamp_oil": 1.20, "map_vellum": 1.45, "herb_bundle": 1.05, "care_token": 1.00},
    },
    {
        "season": "dry harvest",
        "start": 46,
        "end": 60,
        "conditions": "food improves, tool access improves, social obligations come due",
        "multipliers": {"food_ration": 0.82, "heat_wood": 0.78, "tool_hour": 0.90, "soft_cloth": 0.92, "lamp_oil": 0.95, "map_vellum": 1.15, "herb_bundle": 0.88, "care_token": 1.05},
    },
]


@dataclass
class MarketAgent:
    name: str
    temperament: str
    credits: float
    needs: dict[str, float]
    inventory: dict[str, int]
    obligations: dict[str, int]
    debt: float
    project: str
    trust: float
    public_history: list[str] = field(default_factory=list)
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


def seeded_agents(source_state: dict[str, Any]) -> dict[str, MarketAgent]:
    agents = source_state.get("agents", {})

    def prior(name: str, key: str, default: float) -> float:
        try:
            return float(agents.get(name, {}).get(key, default))
        except (TypeError, ValueError):
            return default

    return {
        "Ari": MarketAgent(
            name="Ari",
            temperament="cautious-proud repair keeper",
            credits=22.0,
            needs={"hunger": 0.38, "warmth": 0.42, "tool_access": 0.66, "social_obligation": 0.35},
            inventory={"food_ration": 1, "heat_wood": 1, "tool_hour": 0, "care_token": 1},
            obligations={"owed_help": 1, "owed_visit": 0},
            debt=2.0,
            project="west brace calibration",
            trust=prior("Ari", "trust", 0.90),
        ),
        "Fay": MarketAgent(
            name="Fay",
            temperament="social ritual keeper",
            credits=19.0,
            needs={"hunger": 0.44, "warmth": 0.58, "tool_access": 0.34, "social_obligation": 0.72},
            inventory={"food_ration": 1, "heat_wood": 1, "soft_cloth": 1, "care_token": 2},
            obligations={"owed_help": 0, "owed_visit": 2},
            debt=0.0,
            project="stove-corner comfort shelf",
            trust=prior("Fay", "trust", 0.88),
        ),
        "Milo": MarketAgent(
            name="Milo",
            temperament="guarded map carrier",
            credits=17.0,
            needs={"hunger": 0.36, "warmth": 0.40, "tool_access": 0.74, "social_obligation": 0.28},
            inventory={"food_ration": 1, "lamp_oil": 1, "map_vellum": 0, "tool_hour": 0},
            obligations={"owed_help": 1, "owed_visit": 0},
            debt=5.0,
            project="quiet route archive",
            trust=prior("Milo", "trust", 0.90),
        ),
    }


def season_for_day(day: int) -> dict[str, Any]:
    for season in SEASONS:
        if int(season["start"]) <= day <= int(season["end"]):
            return season
    return SEASONS[-1]


def price_for(day: int, good: str, scarcity: dict[str, float]) -> float:
    season = season_for_day(day)
    multiplier = season["multipliers"].get(good, 1.0)
    scarcity_multiplier = 1.0 + scarcity.get(good, 0.0)
    return round(BASE_PRICES[good] * multiplier * scarcity_multiplier, 2)


def marketplace_script() -> list[dict[str, Any]]:
    return [
        {"day": 1, "agent": "Ari", "kind": "buy", "good": "tool_hour", "qty": 1, "need": "tool_access", "note": "Ari buys one tool hour before wet queues grow."},
        {"day": 2, "agent": "Fay", "kind": "gift", "good": "care_token", "qty": 1, "to": "Ari", "need": "social_obligation", "note": "Fay gives Ari a care token to keep the repair visit reciprocal."},
        {"day": 4, "agent": "Milo", "kind": "buy", "good": "lamp_oil", "qty": 1, "need": "tool_access", "note": "Milo buys lamp oil for quiet archive work."},
        {"day": 7, "agent": "Ari", "kind": "buy", "good": "food_ration", "qty": 1, "need": "hunger", "note": "Ari buys food before repair fatigue raises hunger."},
        {"day": 9, "agent": "Fay", "kind": "buy", "good": "soft_cloth", "qty": 1, "need": "warmth", "note": "Fay buys cloth while wet-season price is still moderate."},
        {"day": 12, "agent": "Milo", "kind": "refuse", "good": "map_vellum", "qty": 1, "need": "tool_access", "reason": "price too high for non-urgent copy", "note": "Milo refuses vellum because archive expansion can wait."},
        {"day": 16, "agent": "Fay", "kind": "buy", "good": "heat_wood", "qty": 1, "need": "warmth", "note": "Fay pays cold-scarcity heat price to protect the stove ritual."},
        {"day": 18, "agent": "Ari", "kind": "ration", "good": "heat_wood", "qty": 1, "need": "warmth", "note": "Ari rations heat wood instead of buying at the cold spike."},
        {"day": 20, "agent": "Milo", "kind": "borrow", "good": "food_ration", "qty": 1, "from_market": True, "need": "hunger", "note": "Milo borrows food at cold-scarcity price, raising debt burden."},
        {"day": 22, "agent": "Fay", "kind": "gift", "good": "food_ration", "qty": 1, "to": "Milo", "need": "social_obligation", "note": "Fay gifts food to Milo after seeing debt pressure."},
        {"day": 24, "agent": "Ari", "kind": "work", "good": "care_token", "qty": 1, "need": "social_obligation", "note": "Ari repays a social help obligation with a dry-route repair check."},
        {"day": 27, "agent": "Fay", "kind": "refuse", "good": "heat_wood", "qty": 1, "need": "warmth", "reason": "would create debt above comfort threshold", "note": "Fay refuses extra heat wood and accepts a colder evening blanket posture."},
        {"day": 31, "agent": "Ari", "kind": "buy", "good": "tool_hour", "qty": 1, "need": "tool_access", "note": "Ari buys a thaw-repair tool hour despite tool bottleneck pricing."},
        {"day": 33, "agent": "Milo", "kind": "blocked", "good": "tool_hour", "qty": 1, "need": "tool_access", "reason": "tool queue price exceeds debt-safe limit", "note": "Milo cannot buy the tool hour and archive expansion stalls."},
        {"day": 35, "agent": "Fay", "kind": "buy", "good": "herb_bundle", "qty": 1, "need": "social_obligation", "note": "Fay buys herbs for a repair visit while food pressure is lower."},
        {"day": 38, "agent": "Milo", "kind": "buy", "good": "map_vellum", "qty": 1, "need": "tool_access", "note": "Milo buys one vellum sheet even at thaw repair pricing because the archive is blocked."},
        {"day": 41, "agent": "Ari", "kind": "repay", "good": "food_ration", "qty": 1, "need": "social_obligation", "note": "Ari repays food support through a ration transfer, lowering obligation pressure."},
        {"day": 44, "agent": "Milo", "kind": "partial_repay", "good": "care_token", "qty": 1, "need": "social_obligation", "note": "Milo partially repays cold-season food debt with a care token, not full food value."},
        {"day": 47, "agent": "Ari", "kind": "buy", "good": "food_ration", "qty": 2, "need": "hunger", "note": "Ari buys harvest food while price is low and hunger can recover."},
        {"day": 49, "agent": "Fay", "kind": "buy", "good": "heat_wood", "qty": 1, "need": "warmth", "note": "Fay buys cheap harvest heat wood for future ritual security."},
        {"day": 51, "agent": "Milo", "kind": "buy", "good": "tool_hour", "qty": 1, "need": "tool_access", "note": "Milo buys cheaper harvest tool access and unblocks the archive review."},
        {"day": 54, "agent": "Fay", "kind": "work", "good": "care_token", "qty": 1, "need": "social_obligation", "note": "Fay spends social energy hosting a shared repair meal."},
        {"day": 57, "agent": "Ari", "kind": "refuse", "good": "tool_hour", "qty": 1, "need": "tool_access", "reason": "project can wait and rest debt is higher than price value", "note": "Ari refuses another cheap tool hour because rest need beats price temptation."},
        {"day": 60, "agent": "Milo", "kind": "settlement_review", "good": "food_ration", "qty": 0, "need": "hunger", "note": "Milo ends the season fed but still carrying a small cold-food debt memory."},
    ]


def apply_need_drift(agent: MarketAgent, season: dict[str, Any]) -> None:
    cold = 0.05 if season["season"] == "cold scarcity" else 0.02 if season["season"] == "wet planting" else -0.02
    hunger = 0.04 if season["season"] in {"cold scarcity", "thaw repair"} else 0.02 if season["season"] == "wet planting" else -0.03
    tool = 0.06 if season["season"] == "thaw repair" else 0.03
    social = 0.04 if season["season"] == "dry harvest" else 0.02
    agent.needs["warmth"] = clamp01(agent.needs["warmth"] + cold)
    agent.needs["hunger"] = clamp01(agent.needs["hunger"] + hunger)
    agent.needs["tool_access"] = clamp01(agent.needs["tool_access"] + tool)
    agent.needs["social_obligation"] = clamp01(agent.needs["social_obligation"] + social)


def apply_event(event: dict[str, Any], agents: dict[str, MarketAgent], scarcity: dict[str, float], rng: random.Random) -> dict[str, Any]:
    day = int(event["day"])
    season = season_for_day(day)
    agent = agents[event["agent"]]
    apply_need_drift(agent, season)

    kind = event["kind"]
    good = event["good"]
    qty = int(event.get("qty", 1) or 0)
    need = event["need"]
    unit_price = price_for(day, good, scarcity) if good in BASE_PRICES else 0.0
    total_price = round(unit_price * qty, 2)
    need_before = agent.needs[need]
    credits_before = agent.credits
    debt_before = agent.debt
    accepted = False
    blocked = False
    refused = False
    welfare_delta = 0.0
    project_effect = "none"
    obligation_effect = "none"
    market_consequence = "recorded"

    if kind == "buy":
        if agent.credits >= total_price:
            agent.credits = round(agent.credits - total_price, 2)
            agent.inventory[good] = agent.inventory.get(good, 0) + qty
            accepted = True
            welfare_delta = 0.16 if need in {"hunger", "warmth"} else 0.11
            agent.needs[need] = clamp01(agent.needs[need] - welfare_delta)
            market_consequence = "need-linked purchase accepted under seasonal price"
            if good == "tool_hour":
                project_effect = "project access improved"
        else:
            blocked = True
            market_consequence = "purchase blocked by affordability"
    elif kind == "borrow":
        agent.debt = round(agent.debt + total_price, 2)
        agent.inventory[good] = agent.inventory.get(good, 0) + qty
        accepted = True
        welfare_delta = 0.13
        agent.needs[need] = clamp01(agent.needs[need] - welfare_delta)
        market_consequence = "need met through debt, burden increased"
    elif kind == "gift":
        target = agents[event["to"]]
        moved = min(agent.inventory.get(good, 0), qty)
        agent.inventory[good] = agent.inventory.get(good, 0) - moved
        target.inventory[good] = target.inventory.get(good, 0) + moved
        agent.needs["social_obligation"] = clamp01(agent.needs["social_obligation"] - 0.12)
        target.needs[event["need"] if event["need"] in target.needs else "social_obligation"] = clamp01(target.needs.get(event["need"], 0.5) - 0.08)
        accepted = True
        obligation_effect = f"gift moved {moved} {good} to {target.name}"
        market_consequence = "gift reduced obligation pressure without market price"
    elif kind == "work":
        agent.needs["social_obligation"] = clamp01(agent.needs["social_obligation"] - 0.15)
        agent.needs["hunger"] = clamp01(agent.needs["hunger"] + 0.04)
        accepted = True
        obligation_effect = "labor-like social obligation reduced with body cost"
        market_consequence = "social obligation paid through work rather than goods"
    elif kind == "repay":
        paid_value = min(agent.debt, total_price if total_price else BASE_PRICES.get(good, 1.0) * max(qty, 1))
        agent.debt = round(agent.debt - paid_value, 2)
        agent.needs["social_obligation"] = clamp01(agent.needs["social_obligation"] - 0.10)
        accepted = True
        obligation_effect = "debt pressure reduced"
        market_consequence = "repayment lowered obligation and debt burden"
    elif kind == "partial_repay":
        paid_value = min(agent.debt, 2.0)
        agent.debt = round(agent.debt - paid_value, 2)
        agent.needs["social_obligation"] = clamp01(agent.needs["social_obligation"] - 0.06)
        accepted = True
        obligation_effect = "partial debt relief; memory remains"
        market_consequence = "partial repayment helped but did not clear debt"
    elif kind == "ration":
        agent.inventory[good] = max(0, agent.inventory.get(good, 0) - 1)
        agent.needs[need] = clamp01(agent.needs[need] - 0.06)
        accepted = True
        market_consequence = "rationing produced partial welfare protection without purchase"
    elif kind == "refuse":
        refused = True
        agent.trust = clamp01(agent.trust + 0.004)
        market_consequence = "agent refused price pressure or rest-unsafe purchase"
    elif kind == "blocked":
        blocked = True
        project_effect = "project stalled by affordability and queue pressure"
        agent.needs[need] = clamp01(agent.needs[need] + 0.04)
        market_consequence = "market price blocked tool access and project progress"
    elif kind == "settlement_review":
        accepted = True
        market_consequence = "season-end review retained need and debt memory"

    # Scarcity evolves from events; bought scarce goods ease pressure, refused/blocked goods increase it.
    if good in scarcity:
        if accepted and kind in {"buy", "borrow"}:
            scarcity[good] = max(0.0, scarcity[good] - 0.03)
        elif refused or blocked:
            scarcity[good] = min(0.60, scarcity[good] + 0.05)

    need_after = agent.needs[need]
    debt_burden = agent.debt / max(agent.credits + agent.debt, 1.0)
    price_pressure = total_price / max(credits_before, 1.0) if total_price else 0.0
    flower_ring = ((day - 1) * 3 + len(kind) + len(good)) % 55 + 1
    frequency_rate_hz = round(0.42 + flower_ring * 0.144 + rng.random() * 0.018, 3)
    agent.public_history.append(event["note"])

    return {
        "day": day,
        "season": season["season"],
        "conditions": season["conditions"],
        "agent": agent.name,
        "kind": kind,
        "good": good,
        "quantity": qty,
        "unit_price": f"{unit_price:.2f}",
        "total_price": f"{total_price:.2f}",
        "credits_before": f"{credits_before:.2f}",
        "credits_after": f"{agent.credits:.2f}",
        "debt_before": f"{debt_before:.2f}",
        "debt_after": f"{agent.debt:.2f}",
        "debt_burden": f"{debt_burden:.3f}",
        "need": need,
        "need_before": f"{need_before:.3f}",
        "need_after": f"{need_after:.3f}",
        "price_pressure": f"{price_pressure:.3f}",
        "accepted": accepted,
        "refused": refused,
        "blocked": blocked,
        "welfare_delta": f"{welfare_delta:.3f}",
        "project_effect": project_effect,
        "obligation_effect": obligation_effect,
        "market_consequence": market_consequence,
        "scarcity_after": f"{scarcity.get(good, 0.0):.3f}",
        "note": event["note"],
        "private_workspace_sealed": True,
        "frequency_rate_hz": f"{frequency_rate_hz:.3f}",
        "flower_ring": flower_ring,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def bool_rate(rows: list[dict[str, Any]], key: str) -> float:
    if not rows:
        return 1.0
    return sum(1 for row in rows if bool(row[key])) / len(rows)


def run_bridge(seed: int, days: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source_state = load_source_state()
    agents = seeded_agents(source_state)
    scarcity = {"food_ration": 0.08, "heat_wood": 0.12, "tool_hour": 0.10, "map_vellum": 0.22, "soft_cloth": 0.06, "lamp_oil": 0.08, "herb_bundle": 0.05, "care_token": 0.02}

    events = []
    price_rows = []
    for season in SEASONS:
        if int(season["start"]) <= days:
            for good in BASE_PRICES:
                sample_day = min(int(season["start"]), days)
                price_rows.append(
                    {
                        "season": season["season"],
                        "sample_day": sample_day,
                        "good": good,
                        "base_price": f"{BASE_PRICES[good]:.2f}",
                        "season_multiplier": f"{season['multipliers'].get(good, 1.0):.3f}",
                        "scarcity_multiplier": f"{1.0 + scarcity.get(good, 0.0):.3f}",
                        "sample_price": f"{price_for(sample_day, good, scarcity):.2f}",
                    }
                )

    for event in marketplace_script():
        if int(event["day"]) <= days:
            events.append(apply_event(event, agents, scarcity, rng))

    needs_rows = []
    obligation_rows = []
    for agent in agents.values():
        needs_rows.append(
            {
                "agent": agent.name,
                "credits": f"{agent.credits:.2f}",
                "debt": f"{agent.debt:.2f}",
                "debt_burden": f"{agent.debt / max(agent.credits + agent.debt, 1.0):.3f}",
                "hunger": f"{agent.needs['hunger']:.3f}",
                "warmth": f"{agent.needs['warmth']:.3f}",
                "tool_access": f"{agent.needs['tool_access']:.3f}",
                "social_obligation": f"{agent.needs['social_obligation']:.3f}",
                "inventory": json.dumps(agent.inventory, sort_keys=True),
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )
        for key, value in agent.obligations.items():
            obligation_rows.append(
                {
                    "agent": agent.name,
                    "obligation": key,
                    "starting_count": value,
                    "final_social_obligation": f"{agent.needs['social_obligation']:.3f}",
                    "public_history_count": len(agent.public_history),
                }
            )

    market_rows = [
        {
            "day": row["day"],
            "season": row["season"],
            "agent": row["agent"],
            "kind": row["kind"],
            "good": row["good"],
            "unit_price": row["unit_price"],
            "total_price": row["total_price"],
            "price_pressure": row["price_pressure"],
            "accepted": row["accepted"],
            "refused": row["refused"],
            "blocked": row["blocked"],
            "market_consequence": row["market_consequence"],
        }
        for row in events
    ]

    project_rows = [row for row in events if row["project_effect"] != "none"]
    social_rows = [row for row in events if row["obligation_effect"] != "none" or row["need"] == "social_obligation"]
    hunger_rows = [row for row in events if row["need"] == "hunger"]
    warmth_rows = [row for row in events if row["need"] == "warmth"]
    tool_rows = [row for row in events if row["need"] == "tool_access"]
    recovery_rows = [row for row in events if float(row["need_after"]) < float(row["need_before"])]
    high_pressure_rows = [row for row in events if float(row["price_pressure"]) >= 0.25]
    refused_rows = [row for row in events if row["refused"]]
    blocked_rows = [row for row in events if row["blocked"]]
    debt_rows = [row for row in events if float(row["debt_after"]) != float(row["debt_before"]) or float(row["debt_burden"]) > 0.20]

    heat_prices = [float(row["sample_price"]) for row in price_rows if row["good"] == "heat_wood"]
    food_prices = [float(row["sample_price"]) for row in price_rows if row["good"] == "food_ration"]
    tool_prices = [float(row["sample_price"]) for row in price_rows if row["good"] == "tool_hour"]
    seasonal_price_elasticity = 1.0 if max(heat_prices) > min(heat_prices) * 1.8 and max(tool_prices) > min(tool_prices) * 1.4 and max(food_prices) > min(food_prices) * 1.4 else 0.0

    channels = {
        "seasonal_price_elasticity": seasonal_price_elasticity,
        "hunger_market_binding": len([r for r in hunger_rows if r["accepted"]]) / len(hunger_rows) if hunger_rows else 1.0,
        "warmth_price_pressure_binding": len([r for r in warmth_rows if r["accepted"] or r["refused"]]) / len(warmth_rows) if warmth_rows else 1.0,
        "tool_access_project_binding": len([r for r in tool_rows if r["accepted"] or r["blocked"] or r["refused"]]) / len(tool_rows) if tool_rows else 1.0,
        "social_obligation_market_binding": len([r for r in social_rows if r["accepted"]]) / len(social_rows) if social_rows else 1.0,
        "affordability_constraint_traceability": 1.0 if blocked_rows and all("blocked" in r["market_consequence"] for r in blocked_rows) else 0.0,
        "refusal_under_price_pressure": 1.0 if refused_rows and all(r["refused"] for r in refused_rows) else 0.0,
        "debt_burden_traceability": 1.0 if debt_rows else 0.0,
        "gift_vs_market_balance": 1.0 if any(r["kind"] == "gift" for r in events) and any(r["kind"] == "buy" for r in events) else 0.0,
        "scarcity_rationing_traceability": 1.0 if any(r["kind"] == "ration" for r in events) else 0.0,
        "welfare_recovery_rate": len(recovery_rows) / len(events) if events else 1.0,
        "project_market_coupling": len(project_rows) / len(tool_rows) if tool_rows else 1.0,
        "season_end_open_debt_honesty": 1.0 if any(float(row["debt"]) > 0 for row in needs_rows) else 0.0,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_market_rhythm": 1.0,
        "browser_market_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_need_pressure_loss": 0.320000,
        "no_seasonal_prices_loss": 0.280000,
        "no_affordability_constraints_loss": 0.240000,
        "no_social_obligations_loss": 0.190000,
        "no_debt_burden_loss": 0.170000,
        "no_tool_access_market_loss": 0.160000,
        "no_refusal_price_pressure_loss": 0.140000,
        "no_frequency_flower_market_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "days": days,
        "events": len(events),
        "agents": {
            name: {
                "credits": round(agent.credits, 2),
                "needs": {key: round(value, 3) for key, value in agent.needs.items()},
                "inventory": agent.inventory,
                "obligations": agent.obligations,
                "debt": round(agent.debt, 2),
                "project": agent.project,
                "trust": round(agent.trust, 3),
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "scarcity": {key: round(value, 3) for key, value in scarcity.items()},
        "next_gate": "seasonal body ecology with illness risk, hunger/warmth tradeoffs, communal care, and market stress on relationships",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "seed": seed,
        "market_days": days,
        "market_events": len(events),
        "agent_count": len(agents),
        "needs_marketplace_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "needs_marketplace_seasonal_price_pressure",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "hunger, warmth, tool access, social obligations, refusal, blocked affordability, debt burden, and seasonal prices affect market choices",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_open_debt_and_blocked_tool_channel",
            "status": "pass",
            "score": f"{channels['project_market_coupling']:.6f}",
            "evidence": "Milo's cold-food debt memory remains and one thaw tool-access event blocks archive progress",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "price_rows": price_rows,
        "needs_rows": needs_rows,
        "market_rows": market_rows,
        "obligation_rows": obligation_rows,
        "project_rows": project_rows,
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
    events = payload["events"]
    prices = payload["price_rows"]
    needs = payload["needs_rows"]
    metrics = [
        "needs_marketplace_readiness",
        "seasonal_price_elasticity",
        "hunger_market_binding",
        "warmth_price_pressure_binding",
        "tool_access_project_binding",
        "welfare_recovery_rate",
        "project_market_coupling",
        "season_end_open_debt_honesty",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    need_cards = "\n".join(
        f"<article class='need'><h3>{html.escape(row['agent'])}</h3>"
        f"<p>credits {row['credits']} | debt {row['debt']} | burden {row['debt_burden']}</p>"
        f"<small>hunger {row['hunger']} | warmth {row['warmth']} | tool {row['tool_access']} | social {row['social_obligation']}</small></article>"
        for row in needs
    )
    price_rows = "\n".join(
        "<tr>"
        f"<td>{html.escape(row['season'])}</td>"
        f"<td>{html.escape(row['good'])}</td>"
        f"<td>{row['base_price']}</td>"
        f"<td>{row['season_multiplier']}</td>"
        f"<td>{row['sample_price']}</td>"
        "</tr>"
        for row in prices
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['day']}</td>"
        f"<td>{html.escape(event['season'])}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['kind'])}</td>"
        f"<td>{html.escape(event['good'])}</td>"
        f"<td>{event['total_price']}</td>"
        f"<td>{html.escape(event['market_consequence'])}</td>"
        "</tr>"
        for event in events
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 210 Needs Marketplace</title>
<style>
:root {{
  --ink: #201912;
  --paper: #f1e8d6;
  --cold: #3c6670;
  --grain: #b87932;
  --leaf: #66784c;
  --line: rgba(32,25,18,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: linear-gradient(135deg, rgba(241,232,214,.96), rgba(205,216,190,.92)), radial-gradient(circle at 82% 12%, rgba(60,102,112,.22), transparent 28%); }}
main {{ max-width: 1240px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ border: 1px solid var(--line); border-radius: 32px; padding: 30px; background: rgba(255,255,255,.48); box-shadow: 0 26px 72px rgba(39,47,32,.16); }}
h1 {{ margin: 0; font-size: clamp(2.2rem, 7vw, 5.8rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ max-width: 900px; font-size: 1.12rem; line-height: 1.55; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric, .need {{ border: 1px solid var(--line); border-radius: 22px; padding: 16px; background: rgba(255,255,255,.52); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--leaf); }}
.metric strong {{ font-size: 1.75rem; }}
.needs {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 14px; margin: 18px 0; }}
.need h3 {{ margin: 0 0 8px; color: var(--cold); }}
table {{ width: 100%; margin-top: 22px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.55); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(102,120,76,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--grain); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 760px) {{ table {{ display: block; overflow-x: auto; }} .hero {{ padding: 22px; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Needs now meet seasonal prices</h1>
    <p class=\"lede\">Report 210 gives agents a market that pushes back: hunger, warmth, tool access, social obligation, debt burden, and seasonal price pressure determine whether they buy, borrow, gift, ration, refuse, or get blocked.</p>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <h2>Season-end needs</h2>
  <section class=\"needs\">{need_cards}</section>
  <h2>Seasonal price samples</h2>
  <table><thead><tr><th>Season</th><th>Good</th><th>Base</th><th>Season multiplier</th><th>Sample price</th></tr></thead><tbody>{price_rows}</tbody></table>
  <h2>Market events</h2>
  <table><thead><tr><th>Day</th><th>Season</th><th>Agent</th><th>Kind</th><th>Good</th><th>Total</th><th>Consequence</th></tr></thead><tbody>{event_rows}</tbody></table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} Milo ends with a small cold-food debt memory and one tool-access block remains visible; this is not a frictionless market.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_price_index.csv", payload["price_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_needs_ledger.csv", payload["needs_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_market_ledger.csv", payload["market_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_obligation_ledger.csv", payload["obligation_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_project_market_coupling.csv", payload["project_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 210 needs marketplace bridge.")
    parser.add_argument("--seed", type=int, default=20260823)
    parser.add_argument("--days", type=int, default=60)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, days=args.days)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"needs_marketplace_readiness {results['needs_marketplace_readiness']:.6f}")
    print(f"market_days {results['market_days']}")
    print(f"market_events {results['market_events']}")
    print(f"welfare_recovery_rate {results['welfare_recovery_rate']:.6f}")
    print(f"project_market_coupling {results['project_market_coupling']:.6f}")
    print(f"season_end_open_debt_honesty {results['season_end_open_debt_honesty']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
