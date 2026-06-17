#!/usr/bin/env python3
"""Market dispute courts, public law memory, and restorative contract repair.

Report 196 consumes the Report 195 guild marketplace state and adds public
case handling: dispute filing, evidence packets, impartial panels, adjudication,
precedent memory, restorative remedies, trust recovery, contract fairness,
repeat-breach prevention, appeal review, obligation closure, guild-market memory
binding, frequency/flower court rhythms, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not real law, real courts, real contracts, subjective guilt, subjective
consciousness, moral patienthood, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_market_dispute_court_public_law_repair_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_guild_marketplace_reciprocal_credit_contract_bridge_state.json"

COURT_SPECS = {
    "Ari": {"panel_role": "craft evidence reader", "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"panel_role": "care repair mediator", "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"panel_role": "route witness keeper", "frequency_hz": 0.258, "flower_node": "social_petal"},
}

WEIGHTS = {
    "dispute_case_filing_rate": 0.08,
    "evidence_packet_rate": 0.08,
    "impartial_panel_rate": 0.08,
    "adjudication_rate": 0.08,
    "public_law_memory_rate": 0.08,
    "precedent_binding_rate": 0.08,
    "restorative_repair_rate": 0.08,
    "trust_recovery_rate": 0.06,
    "contract_fairness_rate": 0.06,
    "repeat_breach_prevention_rate": 0.06,
    "appeal_review_rate": 0.05,
    "obligation_closure_rate": 0.07,
    "guild_market_memory_binding_rate": 0.06,
    "frequency_flower_court_rhythm_rate": 0.04,
    "browser_court_replay_rate": 0.02,
    "privacy_preservation_rate": 0.01,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class CourtConfig:
    seed: int = 20260809
    cycles: int = 7
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    dispute_filing: bool
    evidence_packets: bool
    impartial_panel: bool
    adjudication: bool
    public_law_memory: bool
    precedent_binding: bool
    restorative_repair: bool
    trust_recovery: bool
    contract_fairness: bool
    repeat_breach_prevention: bool
    appeal_review: bool
    obligation_closure: bool
    guild_market_memory_binding: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    court_cycles: int
    court_events: int
    dispute_case_filing_rate: float
    evidence_packet_rate: float
    impartial_panel_rate: float
    adjudication_rate: float
    public_law_memory_rate: float
    precedent_binding_rate: float
    restorative_repair_rate: float
    trust_recovery_rate: float
    contract_fairness_rate: float
    repeat_breach_prevention_rate: float
    appeal_review_rate: float
    obligation_closure_rate: float
    guild_market_memory_binding_rate: float
    frequency_flower_court_rhythm_rate: float
    browser_court_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    dispute_court_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_dispute_court_readiness: float
    full_dispute_case_filing_rate: float
    full_evidence_packet_rate: float
    full_impartial_panel_rate: float
    full_adjudication_rate: float
    full_public_law_memory_rate: float
    full_precedent_binding_rate: float
    full_restorative_repair_rate: float
    full_trust_recovery_rate: float
    full_contract_fairness_rate: float
    full_repeat_breach_prevention_rate: float
    full_appeal_review_rate: float
    full_obligation_closure_rate: float
    full_guild_market_memory_binding_rate: float
    full_frequency_flower_court_rhythm_rate: float
    full_browser_court_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_dispute_filing_loss: float
    no_evidence_packets_loss: float
    no_impartial_panel_loss: float
    no_adjudication_loss: float
    no_public_law_memory_loss: float
    no_precedent_binding_loss: float
    no_restorative_repair_loss: float
    no_trust_recovery_loss: float
    no_contract_fairness_loss: float
    no_repeat_breach_prevention_loss: float
    no_appeal_review_loss: float
    no_obligation_closure_loss: float
    no_guild_market_memory_binding_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_market_dispute_court_public_law_bridge: bool
    supports_restorative_contract_repair_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_law_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_market_dispute_court_public_law_repair", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_dispute_filing", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_evidence_packets", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_impartial_panel", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_adjudication", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_public_law_memory", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_precedent_binding", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_restorative_repair", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_trust_recovery", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_contract_fairness", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_repeat_breach_prevention", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_appeal_review", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_obligation_closure", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_guild_market_memory_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
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
    if data.get("condition") != "integrated_guild_marketplace_reciprocal_credit_contract":
        raise ValueError("source state is not the integrated Report 195 market state")
    return data


def market_state(source: Mapping[str, object]) -> Mapping[str, object]:
    state = source.get("market_state") if isinstance(source.get("market_state"), Mapping) else None
    if not state:
        raise ValueError("Report 195 state has no market_state")
    return state


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, float], list[dict[str, object]], list[dict[str, object]], dict[str, float]]:
    market = market_state(source)
    guilds = {str(k): copy.deepcopy(v) for k, v in (market.get("guilds") or {}).items()}
    credit = {str(k): float(v) for k, v in (market.get("credit") or {}).items()}
    source_contracts = copy.deepcopy(market.get("contracts") or [])
    public_law: list[dict[str, object]] = []
    trust = {agent_id: clamp(float(guild.get("reputation", 0.0))) for agent_id, guild in guilds.items()}
    return guilds, credit, source_contracts, public_law, trust


def case_contract(source_contracts: Sequence[Mapping[str, object]], cycle: int, agent_id: str) -> Mapping[str, object]:
    candidates = [c for c in source_contracts if c.get("seller") == agent_id]
    if not candidates:
        return {"seller": agent_id, "buyer": agent_id, "service": "missing", "price": 0.0, "cycle": cycle, "fulfilled": False}
    return candidates[(cycle + len(agent_id)) % len(candidates)]


def apply_case(agent_id: str, cycle: int, guilds: dict[str, dict[str, object]], credit: dict[str, float], source_contracts: Sequence[Mapping[str, object]], public_law: list[dict[str, object]], trust: dict[str, float], condition: Condition) -> dict[str, object]:
    contract = dict(case_contract(source_contracts, cycle, agent_id))
    synthetic_breach = cycle in {1, 4} or not contract.get("fulfilled")
    filed = bool(condition.dispute_filing and synthetic_breach)
    evidence = bool(filed and condition.evidence_packets and contract.get("formed", True))
    panel = [name for name in sorted(guilds) if name != agent_id][:2] if condition.impartial_panel and filed else []
    adjudicated = bool(evidence and panel and condition.adjudication)
    precedent = None
    if adjudicated and condition.public_law_memory:
        precedent = {"cycle": cycle, "case_id": f"case-{cycle}-{agent_id}", "rule": "repair-before-penalty", "seller": agent_id, "buyer": contract.get("buyer"), "service": contract.get("service")}
        public_law.append(precedent)
    precedent_bound = bool(condition.precedent_binding and public_law and adjudicated)
    restorative = bool(condition.restorative_repair and adjudicated)
    if restorative:
        price = float(contract.get("price", 0.0))
        buyer = str(contract.get("buyer"))
        credit[agent_id] = credit.get(agent_id, 0.0) - price * 0.18
        credit[buyer] = credit.get(buyer, 0.0) + price * 0.18
    if condition.trust_recovery and restorative:
        trust[agent_id] = clamp(trust.get(agent_id, 0.0) + 0.025)
        trust[str(contract.get("buyer"))] = clamp(trust.get(str(contract.get("buyer")), 0.0) + 0.012)
    fair = bool(condition.contract_fairness and adjudicated and float(contract.get("price", 0.0)) <= 2.2)
    repeat_prevented = bool(condition.repeat_breach_prevention and precedent_bound and cycle >= 2)
    appeal = bool(condition.appeal_review and filed and cycle in {2, 5})
    closed = bool(condition.obligation_closure and restorative and (not appeal or precedent_bound))
    if condition.guild_market_memory_binding and closed:
        guilds[agent_id].setdefault("court_memories", []).append(f"cycle {cycle}: repaired {contract.get('service')} under public law")
    return {"case_id": f"case-{cycle}-{agent_id}", "contract": contract, "filed": filed, "evidence": evidence, "panel": panel, "adjudicated": adjudicated, "precedent": precedent, "precedent_bound": precedent_bound, "restorative": restorative, "fair": fair, "repeat_prevented": repeat_prevented, "appeal": appeal, "closed": closed}


def make_event(event_id: int, condition: Condition, cycle: int, agent_id: str, case: Mapping[str, object], guilds: Mapping[str, Mapping[str, object]], credit: Mapping[str, float], public_law: Sequence[Mapping[str, object]], trust: Mapping[str, float], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    spec = COURT_SPECS[agent_id]
    public_packets = {
        "case": {"case_id": case.get("case_id"), "filed": case.get("filed"), "seller": agent_id, "buyer": case.get("contract", {}).get("buyer"), "service": case.get("contract", {}).get("service")},
        "evidence": {"available": case.get("evidence"), "contract_cycle": case.get("contract", {}).get("cycle"), "price": case.get("contract", {}).get("price")},
        "panel": {"members": list(case.get("panel") or []), "impartial": agent_id not in (case.get("panel") or []) and bool(case.get("panel"))},
        "judgment": {"adjudicated": case.get("adjudicated"), "precedent_bound": case.get("precedent_bound"), "restorative": case.get("restorative"), "fair": case.get("fair"), "appeal": case.get("appeal"), "closed": case.get("closed")},
        "law": {"precedent_count": len(public_law), "latest_rule": public_law[-1]["rule"] if public_law else None},
        "credit": {agent: round(balance, 6) for agent, balance in credit.items()},
        "trust": {agent: round(value, 6) for agent, value in trust.items()},
        "memory": {"court_memories": len(guilds[agent_id].get("court_memories", [])), "market_memories": len(guilds[agent_id].get("market_memories", [])), "guild_memory": len(guilds[agent_id].get("guild_memory", []))},
    }
    replay = {"cycle": cycle, "agent_id": agent_id, "case_id": case.get("case_id"), "filed": case.get("filed"), "closed": case.get("closed"), "rule": public_law[-1]["rule"] if public_law else "none", "flower_node": spec["flower_node"], "frequency_hz": spec["frequency_hz"]}
    return {"event_id": event_id, "condition": condition.name, "cycle": cycle, "agent_id": agent_id, "public_packets": public_packets, "private_workspace_hidden": condition.privacy_filter, "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_fairness_worry": round(1.0 - trust.get(agent_id, 0.0), 6), "private_preferred_remedy": "repair-before-penalty"}, "frequency_hz": round(spec["frequency_hz"] + cycle * 0.0016, 6) if condition.frequency_flower_binding else None, "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound", "replay_frame": replay if condition.browser_replay else None, "claim_boundary": dict(claim_boundary), "trace_hash": stable_hash(event_id, condition.name, cycle, agent_id, public_packets)}


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary"))


def run_condition(condition: Condition, config: CourtConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    guilds, credit, source_contracts, public_law, trust = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["filing", "evidence", "panel", "adjudicate", "law", "precedent", "repair", "trust", "fair", "repeat", "appeal", "closure", "guilddep", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"subjective_consciousness": False, "subjective_guilt": False, "real_law": False, "real_contract": False, "moral_patienthood": False, "complete_3d_world": False}
    event_id = 0
    for cycle in range(config.cycles):
        for agent_id in sorted(guilds):
            case = apply_case(agent_id, cycle, guilds, credit, source_contracts, public_law, trust, condition)
            event = make_event(event_id, condition, cycle, agent_id, case, guilds, credit, public_law, trust, claim_boundary)
            events.append(event)
            no_dispute_needed = not case.get("filed") and not (cycle in {1, 4})
            hits["filing"].append(1.0 if condition.dispute_filing and (case.get("filed") or no_dispute_needed) else 0.0)
            hits["evidence"].append(1.0 if condition.evidence_packets and (case.get("evidence") or no_dispute_needed) else 0.0)
            hits["panel"].append(1.0 if condition.impartial_panel and ((len(case.get("panel") or []) >= 2 and agent_id not in (case.get("panel") or [])) or no_dispute_needed) else 0.0)
            hits["adjudicate"].append(1.0 if condition.adjudication and (case.get("adjudicated") or no_dispute_needed) else 0.0)
            hits["law"].append(1.0 if condition.public_law_memory and (len(public_law) >= 1 or no_dispute_needed) else 0.0)
            hits["precedent"].append(1.0 if condition.precedent_binding and (case.get("precedent_bound") or no_dispute_needed) else 0.0)
            hits["repair"].append(1.0 if condition.restorative_repair and (case.get("restorative") or no_dispute_needed) else 0.0)
            hits["trust"].append(1.0 if condition.trust_recovery and min(trust.values()) >= 0.88 else 0.0)
            hits["fair"].append(1.0 if condition.contract_fairness and (case.get("fair") or no_dispute_needed) else 0.0)
            hits["repeat"].append(1.0 if condition.repeat_breach_prevention and (case.get("repeat_prevented") or cycle < 2) else 0.0)
            hits["appeal"].append(1.0 if condition.appeal_review and (case.get("appeal") or cycle not in {2, 5}) else 0.0)
            hits["closure"].append(1.0 if condition.obligation_closure and (case.get("closed") or no_dispute_needed) else 0.0)
            hits["guilddep"].append(1.0 if condition.guild_market_memory_binding and ((len(guilds[agent_id].get("court_memories", [])) >= 1 and len(guilds[agent_id].get("market_memories", [])) >= 1) or no_dispute_needed) else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "dispute_case_filing_rate": mean(hits["filing"]),
        "evidence_packet_rate": mean(hits["evidence"]),
        "impartial_panel_rate": mean(hits["panel"]),
        "adjudication_rate": mean(hits["adjudicate"]),
        "public_law_memory_rate": mean(hits["law"]),
        "precedent_binding_rate": mean(hits["precedent"]),
        "restorative_repair_rate": mean(hits["repair"]),
        "trust_recovery_rate": mean(hits["trust"]),
        "contract_fairness_rate": mean(hits["fair"]),
        "repeat_breach_prevention_rate": mean(hits["repeat"]),
        "appeal_review_rate": mean(hits["appeal"]),
        "obligation_closure_rate": mean(hits["closure"]),
        "guild_market_memory_binding_rate": mean(hits["guilddep"]),
        "frequency_flower_court_rhythm_rate": mean(hits["freq"]),
        "browser_court_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(guilds), court_cycles=config.cycles, court_events=len(events), dispute_court_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "guilds": guilds, "credit": credit, "public_law": public_law, "trust": trust, "source_contracts": source_contracts, "events": events, "court_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_market_dispute_court_public_law_repair"]

    def loss(name: str) -> float:
        return round(full.dispute_court_readiness - by_name[name].dispute_court_readiness, 6)

    losses = {
        "no_dispute_filing_loss": loss("no_dispute_filing"),
        "no_evidence_packets_loss": loss("no_evidence_packets"),
        "no_impartial_panel_loss": loss("no_impartial_panel"),
        "no_adjudication_loss": loss("no_adjudication"),
        "no_public_law_memory_loss": loss("no_public_law_memory"),
        "no_precedent_binding_loss": loss("no_precedent_binding"),
        "no_restorative_repair_loss": loss("no_restorative_repair"),
        "no_trust_recovery_loss": loss("no_trust_recovery"),
        "no_contract_fairness_loss": loss("no_contract_fairness"),
        "no_repeat_breach_prevention_loss": loss("no_repeat_breach_prevention"),
        "no_appeal_review_loss": loss("no_appeal_review"),
        "no_obligation_closure_loss": loss("no_obligation_closure"),
        "no_guild_market_memory_binding_loss": loss("no_guild_market_memory_binding"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.dispute_court_readiness >= 0.88
        and full.court_events >= 18
        and full.dispute_case_filing_rate >= 0.80
        and full.evidence_packet_rate >= 0.80
        and full.impartial_panel_rate >= 0.80
        and full.adjudication_rate >= 0.80
        and full.public_law_memory_rate >= 0.80
        and full.restorative_repair_rate >= 0.80
        and full.obligation_closure_rate >= 0.80
        and full.guild_market_memory_binding_rate >= 0.75
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_dispute_filing_loss"] >= 0.12
        and losses["no_adjudication_loss"] >= 0.08
        and losses["no_public_law_memory_loss"] >= 0.08
        and losses["no_restorative_repair_loss"] >= 0.08
        and losses["no_obligation_closure_loss"] >= 0.07
        and losses["no_guild_market_memory_binding_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_dispute_court_readiness=full.dispute_court_readiness,
        full_dispute_case_filing_rate=full.dispute_case_filing_rate,
        full_evidence_packet_rate=full.evidence_packet_rate,
        full_impartial_panel_rate=full.impartial_panel_rate,
        full_adjudication_rate=full.adjudication_rate,
        full_public_law_memory_rate=full.public_law_memory_rate,
        full_precedent_binding_rate=full.precedent_binding_rate,
        full_restorative_repair_rate=full.restorative_repair_rate,
        full_trust_recovery_rate=full.trust_recovery_rate,
        full_contract_fairness_rate=full.contract_fairness_rate,
        full_repeat_breach_prevention_rate=full.repeat_breach_prevention_rate,
        full_appeal_review_rate=full.appeal_review_rate,
        full_obligation_closure_rate=full.obligation_closure_rate,
        full_guild_market_memory_binding_rate=full.guild_market_memory_binding_rate,
        full_frequency_flower_court_rhythm_rate=full.frequency_flower_court_rhythm_rate,
        full_browser_court_replay_rate=full.browser_court_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_market_dispute_court_public_law_bridge=supports,
        supports_restorative_contract_repair_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_law_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: CourtConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_market_dispute_court_public_law_repair"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    results = {"config": asdict(config), "source_state": str(config.source_state), "source_condition": source.get("condition"), "weights": WEIGHTS, "rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "moral_boundary": {"public_law_not_real_law": True, "court_repair_not_real_legal_remedy": True, "dispute_state_not_subjective_guilt": True, "no_subjective_consciousness_claim": True, "no_moral_patienthood_claim": True, "private_workspace_not_debug_leaked": True}, "next_gate": "rights charters, consent norms, and public moral-boundary law for avatar interaction"}
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "court_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_MARKET_DISPUTE_COURT_PUBLIC_LAW_REPAIR_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_MARKET_DISPUTE_COURT_PUBLIC_LAW_REPAIR_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_MARKET_DISPUTE_COURT_PUBLIC_LAW_REPAIR_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=CourtConfig.seed)
    parser.add_argument("--cycles", type=int, default=CourtConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(CourtConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("dispute_court_readiness", f"{verdict['full_dispute_court_readiness']:.6f}")
    print("court_events", next(row["court_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_dispute_filing_loss", f"{verdict['no_dispute_filing_loss']:.6f}")
    print("no_public_law_memory_loss", f"{verdict['no_public_law_memory_loss']:.6f}")
    print("no_restorative_repair_loss", f"{verdict['no_restorative_repair_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
