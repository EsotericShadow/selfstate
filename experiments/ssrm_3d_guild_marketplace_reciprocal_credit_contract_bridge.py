#!/usr/bin/env python3
"""Guild marketplaces, reciprocal credit, and craft-service contracts.

Report 195 consumes the Report 194 guild state and adds a deterministic
marketplace layer: certified service listings, reciprocal credit ledgers,
contract formation, fulfillment, fair price calibration, cross-guild exchange,
reputation-credit binding, debt settlement, breach detection, dispute repair,
obligation memory, guild-memory dependency, frequency/flower market rhythms,
and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not real money, real markets, real contracts, subjective obligation,
subjective consciousness, moral patienthood, or complete 3D gameplay.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_guild_marketplace_reciprocal_credit_contract_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_guild_memory_craft_standards_tool_inheritance_bridge_state.json"

SERVICE_RING = {
    "Ari": {"service": "sealed shelter repair", "buyer": "Milo", "need": "water_route_markers", "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"service": "clean care bundle", "buyer": "Ari", "need": "winter_shelter_repair", "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"service": "safe waymark route", "buyer": "Fay", "need": "medicine_corner", "frequency_hz": 0.258, "flower_node": "social_petal"},
}

WEIGHTS = {
    "marketplace_listing_rate": 0.08,
    "certified_service_offer_rate": 0.08,
    "reciprocal_credit_ledger_rate": 0.08,
    "contract_formation_rate": 0.08,
    "contract_fulfillment_rate": 0.08,
    "fair_price_calibration_rate": 0.08,
    "cross_guild_exchange_rate": 0.07,
    "reputation_credit_binding_rate": 0.07,
    "debt_settlement_rate": 0.06,
    "breach_detection_rate": 0.05,
    "dispute_repair_rate": 0.05,
    "obligation_memory_rate": 0.07,
    "guild_memory_dependency_rate": 0.06,
    "frequency_flower_market_rhythm_rate": 0.04,
    "browser_market_replay_rate": 0.03,
    "privacy_preservation_rate": 0.01,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class MarketConfig:
    seed: int = 20260808
    cycles: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    marketplace_listing: bool
    certified_service_offer: bool
    reciprocal_credit: bool
    contract_formation: bool
    contract_fulfillment: bool
    fair_price: bool
    cross_guild_exchange: bool
    reputation_binding: bool
    debt_settlement: bool
    breach_detection: bool
    dispute_repair: bool
    obligation_memory: bool
    guild_memory_dependency: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    market_cycles: int
    market_events: int
    marketplace_listing_rate: float
    certified_service_offer_rate: float
    reciprocal_credit_ledger_rate: float
    contract_formation_rate: float
    contract_fulfillment_rate: float
    fair_price_calibration_rate: float
    cross_guild_exchange_rate: float
    reputation_credit_binding_rate: float
    debt_settlement_rate: float
    breach_detection_rate: float
    dispute_repair_rate: float
    obligation_memory_rate: float
    guild_memory_dependency_rate: float
    frequency_flower_market_rhythm_rate: float
    browser_market_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    guild_market_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_guild_market_readiness: float
    full_marketplace_listing_rate: float
    full_certified_service_offer_rate: float
    full_reciprocal_credit_ledger_rate: float
    full_contract_formation_rate: float
    full_contract_fulfillment_rate: float
    full_fair_price_calibration_rate: float
    full_cross_guild_exchange_rate: float
    full_reputation_credit_binding_rate: float
    full_debt_settlement_rate: float
    full_breach_detection_rate: float
    full_dispute_repair_rate: float
    full_obligation_memory_rate: float
    full_guild_memory_dependency_rate: float
    full_frequency_flower_market_rhythm_rate: float
    full_browser_market_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_marketplace_listing_loss: float
    no_certified_service_offer_loss: float
    no_reciprocal_credit_loss: float
    no_contract_formation_loss: float
    no_contract_fulfillment_loss: float
    no_fair_price_loss: float
    no_cross_guild_exchange_loss: float
    no_reputation_binding_loss: float
    no_debt_settlement_loss: float
    no_breach_detection_loss: float
    no_dispute_repair_loss: float
    no_obligation_memory_loss: float
    no_guild_memory_dependency_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_guild_marketplace_credit_contract_bridge: bool
    supports_reciprocal_credit_contract_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_market_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_guild_marketplace_reciprocal_credit_contract", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_marketplace_listing", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_certified_service_offer", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_reciprocal_credit", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_contract_formation", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_contract_fulfillment", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_fair_price", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_cross_guild_exchange", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_reputation_binding", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_debt_settlement", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_breach_detection", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_dispute_repair", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_obligation_memory", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_guild_memory_dependency", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_guild_memory_craft_standards_tool_inheritance":
        raise ValueError("source state is not the integrated Report 194 guild state")
    return data


def guild_state(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("guild_state") if isinstance(source.get("guild_state"), Mapping) else None
    if not state:
        raise ValueError("Report 194 state has no guild_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, float], list[dict[str, object]]]:
    gs = guild_state(source)
    guilds = {str(k): copy.deepcopy(v) for k, v in (gs.get("guilds") or {}).items()}
    tools = {str(k): copy.deepcopy(v) for k, v in (gs.get("tools") or {}).items()}
    credit = {agent_id: 0.0 for agent_id in guilds}
    contracts: list[dict[str, object]] = []
    return guilds, tools, credit, contracts


def service_price(agent_id: str, guild: Mapping[str, object], tool: Mapping[str, object], condition: Condition) -> float:
    base = 1.0 + float(tool.get("quality", 0.0)) * 0.55
    if condition.fair_price:
        return round(base + float(guild.get("reputation", 0.0)) * 0.32, 6)
    return round(base * 1.85, 6)


def apply_market_cycle(agent_id: str, cycle: int, guilds: dict[str, dict[str, object]], tools: dict[str, dict[str, object]], credit: dict[str, float], contracts: list[dict[str, object]], condition: Condition) -> dict[str, object]:
    guild = guilds[agent_id]
    service = SERVICE_RING[agent_id]
    buyer = service["buyer"]
    tool_name = next((name for name, tool in tools.items() if tool.get("owner") == agent_id), "unclaimed_tool")
    tool = tools.get(tool_name, {"quality": 0.0, "lineage_marks": []})
    listing = bool(condition.marketplace_listing)
    certified_offer = bool(listing and condition.certified_service_offer and guild.get("certified"))
    price = service_price(agent_id, guild, tool, condition) if certified_offer else 0.0
    contract_formed = bool(certified_offer and condition.contract_formation and condition.cross_guild_exchange and buyer != agent_id)
    late = cycle in {2, 6}
    fulfilled = bool(contract_formed and condition.contract_fulfillment and not (late and not condition.dispute_repair))
    breach = bool(contract_formed and late and condition.breach_detection)
    repaired = bool(breach and condition.dispute_repair and fulfilled)
    if condition.reciprocal_credit and contract_formed:
        credit[buyer] -= price
        credit[agent_id] += price
    if condition.debt_settlement and fulfilled:
        settle = price * 0.52
        credit[buyer] += settle
        credit[agent_id] -= settle
    if condition.reputation_binding and fulfilled:
        guild["reputation"] = clamp(float(guild.get("reputation", 0.0)) + 0.018)
    elif condition.reputation_binding and breach and not repaired:
        guild["reputation"] = clamp(float(guild.get("reputation", 0.0)) - 0.035)
    if condition.obligation_memory and contract_formed:
        guild.setdefault("market_memories", []).append(f"cycle {cycle}: {agent_id} promised {service['service']} to {buyer}")
    if condition.guild_memory_dependency and len(guild.get("guild_memory", [])) >= 2 and contract_formed:
        guild.setdefault("guild_memory", []).append(f"market memory: {service['service']} priced by guild trust in cycle {cycle}")
    contract = {
        "cycle": cycle,
        "seller": agent_id,
        "buyer": buyer,
        "service": service["service"],
        "need": service["need"],
        "tool": tool_name,
        "price": price,
        "formed": contract_formed,
        "fulfilled": fulfilled,
        "breach": breach,
        "repaired": repaired,
    }
    if contract_formed:
        contracts.append(contract)
    return contract


def make_event(event_id: int, condition: Condition, cycle: int, agent_id: str, contract: Mapping[str, object], guilds: Mapping[str, Mapping[str, object]], credit: Mapping[str, float], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    service = SERVICE_RING[agent_id]
    guild = guilds[agent_id]
    public_packets = {
        "listing": {"listed": condition.marketplace_listing, "service": service["service"], "seller_guild": guild.get("guild")},
        "offer": {"certified": bool(condition.certified_service_offer and guild.get("certified")), "standard": guild.get("standard"), "reputation": round(float(guild.get("reputation", 0.0)), 6)},
        "contract": dict(contract),
        "credit": {agent: round(balance, 6) for agent, balance in credit.items()},
        "memory": {"seller_market_memories": len(guild.get("market_memories", [])), "guild_memory_count": len(guild.get("guild_memory", [])), "certificates": len(guild.get("certificates", []))},
    }
    replay = {"cycle": cycle, "agent_id": agent_id, "service": service["service"], "buyer": service["buyer"], "price": contract.get("price"), "fulfilled": contract.get("fulfilled"), "flower_node": service["flower_node"], "frequency_hz": service["frequency_hz"]}
    return {
        "event_id": event_id,
        "condition": condition.name,
        "cycle": cycle,
        "agent_id": agent_id,
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_credit_worry": round(abs(float(credit.get(agent_id, 0.0))), 6), "private_fairness_estimate": contract.get("price")},
        "frequency_hz": round(service["frequency_hz"] + cycle * 0.0014, 6) if condition.frequency_flower_binding else None,
        "flower_node": service["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, cycle, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary"))


def run_condition(condition: Condition, config: MarketConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    guilds, tools, credit, contracts = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["listing", "offer", "credit", "formation", "fulfillment", "price", "cross", "reputation", "debt", "breach", "repair", "memory", "guilddep", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"subjective_consciousness": False, "subjective_obligation": False, "real_market": False, "real_contract": False, "moral_patienthood": False, "complete_3d_world": False}
    event_id = 0
    for cycle in range(config.cycles):
        for agent_id in sorted(guilds):
            contract = apply_market_cycle(agent_id, cycle, guilds, tools, credit, contracts, condition)
            event = make_event(event_id, condition, cycle, agent_id, contract, guilds, credit, claim_boundary)
            events.append(event)
            hits["listing"].append(1.0 if condition.marketplace_listing and event["public_packets"]["listing"]["listed"] else 0.0)
            hits["offer"].append(1.0 if condition.marketplace_listing and condition.certified_service_offer and event["public_packets"]["offer"]["certified"] else 0.0)
            hits["credit"].append(1.0 if condition.reciprocal_credit and contract.get("formed") and any(abs(v) > 0.0 for v in credit.values()) else 0.0)
            hits["formation"].append(1.0 if contract.get("formed") else 0.0)
            hits["fulfillment"].append(1.0 if condition.contract_fulfillment and contract.get("fulfilled") else 0.0)
            hits["price"].append(1.0 if condition.fair_price and 1.0 <= float(contract.get("price", 0.0)) <= 2.1 and contract.get("formed") else 0.0)
            hits["cross"].append(1.0 if condition.cross_guild_exchange and contract.get("formed") and contract.get("seller") != contract.get("buyer") else 0.0)
            hits["reputation"].append(1.0 if condition.reputation_binding and float(guilds[agent_id].get("reputation", 0.0)) >= 0.70 else 0.0)
            hits["debt"].append(1.0 if condition.reciprocal_credit and condition.debt_settlement and contract.get("fulfilled") and max(abs(v) for v in credit.values()) <= 8.0 else 0.0)
            hits["breach"].append(1.0 if condition.breach_detection and (contract.get("breach") or cycle not in {2, 6}) else 0.0)
            hits["repair"].append(1.0 if condition.dispute_repair and (contract.get("repaired") or not contract.get("breach")) else 0.0)
            hits["memory"].append(1.0 if condition.obligation_memory and len(guilds[agent_id].get("market_memories", [])) >= 1 else 0.0)
            hits["guilddep"].append(1.0 if condition.guild_memory_dependency and len(guilds[agent_id].get("guild_memory", [])) >= 3 and contract.get("formed") else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "marketplace_listing_rate": mean(hits["listing"]),
        "certified_service_offer_rate": mean(hits["offer"]),
        "reciprocal_credit_ledger_rate": mean(hits["credit"]),
        "contract_formation_rate": mean(hits["formation"]),
        "contract_fulfillment_rate": mean(hits["fulfillment"]),
        "fair_price_calibration_rate": mean(hits["price"]),
        "cross_guild_exchange_rate": mean(hits["cross"]),
        "reputation_credit_binding_rate": mean(hits["reputation"]),
        "debt_settlement_rate": mean(hits["debt"]),
        "breach_detection_rate": mean(hits["breach"]),
        "dispute_repair_rate": mean(hits["repair"]),
        "obligation_memory_rate": mean(hits["memory"]),
        "guild_memory_dependency_rate": mean(hits["guilddep"]),
        "frequency_flower_market_rhythm_rate": mean(hits["freq"]),
        "browser_market_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(guilds), market_cycles=config.cycles, market_events=len(events), guild_market_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "guilds": guilds, "tools": tools, "credit": credit, "contracts": contracts, "events": events, "market_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_guild_marketplace_reciprocal_credit_contract"]

    def loss(name: str) -> float:
        return round(full.guild_market_readiness - by_name[name].guild_market_readiness, 6)

    losses = {
        "no_marketplace_listing_loss": loss("no_marketplace_listing"),
        "no_certified_service_offer_loss": loss("no_certified_service_offer"),
        "no_reciprocal_credit_loss": loss("no_reciprocal_credit"),
        "no_contract_formation_loss": loss("no_contract_formation"),
        "no_contract_fulfillment_loss": loss("no_contract_fulfillment"),
        "no_fair_price_loss": loss("no_fair_price"),
        "no_cross_guild_exchange_loss": loss("no_cross_guild_exchange"),
        "no_reputation_binding_loss": loss("no_reputation_binding"),
        "no_debt_settlement_loss": loss("no_debt_settlement"),
        "no_breach_detection_loss": loss("no_breach_detection"),
        "no_dispute_repair_loss": loss("no_dispute_repair"),
        "no_obligation_memory_loss": loss("no_obligation_memory"),
        "no_guild_memory_dependency_loss": loss("no_guild_memory_dependency"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.guild_market_readiness >= 0.88
        and full.market_events >= 21
        and full.marketplace_listing_rate >= 0.90
        and full.certified_service_offer_rate >= 0.90
        and full.reciprocal_credit_ledger_rate >= 0.80
        and full.contract_formation_rate >= 0.90
        and full.contract_fulfillment_rate >= 0.80
        and full.obligation_memory_rate >= 0.80
        and full.guild_memory_dependency_rate >= 0.80
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_marketplace_listing_loss"] >= 0.10
        and losses["no_reciprocal_credit_loss"] >= 0.08
        and losses["no_contract_fulfillment_loss"] >= 0.08
        and losses["no_reputation_binding_loss"] >= 0.07
        and losses["no_obligation_memory_loss"] >= 0.07
        and losses["no_guild_memory_dependency_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_guild_market_readiness=full.guild_market_readiness,
        full_marketplace_listing_rate=full.marketplace_listing_rate,
        full_certified_service_offer_rate=full.certified_service_offer_rate,
        full_reciprocal_credit_ledger_rate=full.reciprocal_credit_ledger_rate,
        full_contract_formation_rate=full.contract_formation_rate,
        full_contract_fulfillment_rate=full.contract_fulfillment_rate,
        full_fair_price_calibration_rate=full.fair_price_calibration_rate,
        full_cross_guild_exchange_rate=full.cross_guild_exchange_rate,
        full_reputation_credit_binding_rate=full.reputation_credit_binding_rate,
        full_debt_settlement_rate=full.debt_settlement_rate,
        full_breach_detection_rate=full.breach_detection_rate,
        full_dispute_repair_rate=full.dispute_repair_rate,
        full_obligation_memory_rate=full.obligation_memory_rate,
        full_guild_memory_dependency_rate=full.guild_memory_dependency_rate,
        full_frequency_flower_market_rhythm_rate=full.frequency_flower_market_rhythm_rate,
        full_browser_market_replay_rate=full.browser_market_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_guild_marketplace_credit_contract_bridge=supports,
        supports_reciprocal_credit_contract_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_market_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: MarketConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_guild_marketplace_reciprocal_credit_contract"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "market_credit_not_real_money": True,
            "contracts_not_real_legal_obligations": True,
            "reputation_not_subjective_status": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "market dispute courts, public law memory, and restorative contract repair",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "market_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_GUILD_MARKETPLACE_RECIPROCAL_CREDIT_CONTRACT_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_GUILD_MARKETPLACE_RECIPROCAL_CREDIT_CONTRACT_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_GUILD_MARKETPLACE_RECIPROCAL_CREDIT_CONTRACT_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=MarketConfig.seed)
    parser.add_argument("--cycles", type=int, default=MarketConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(MarketConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("guild_market_readiness", f"{verdict['full_guild_market_readiness']:.6f}")
    print("market_events", next(row["market_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_marketplace_listing_loss", f"{verdict['no_marketplace_listing_loss']:.6f}")
    print("no_reciprocal_credit_loss", f"{verdict['no_reciprocal_credit_loss']:.6f}")
    print("no_contract_fulfillment_loss", f"{verdict['no_contract_fulfillment_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
