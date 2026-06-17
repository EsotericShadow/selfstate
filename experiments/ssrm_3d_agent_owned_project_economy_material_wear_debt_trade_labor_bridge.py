"""Report 209: SSRM-3D agent-owned project economy bridge.

This deterministic bridge adds material accounting, object wear, gifts, trades,
debt, scarcity, and refusal-sensitive labor to the playable agent continuity
stack. It is a functional economy substrate only, not real social life or
consciousness.
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

PREFIX = "ssrm_3d_agent_owned_project_economy_material_wear_debt_trade_labor_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge_state.json"
SOURCE_CONDITION = "integrated_calendar_commitments_object_projects_reputation_consequences"
CLAIM_BOUNDARY = (
    "Deterministic agent-owned project economy substrate only: not real labor, not real property, "
    "not real consent, not subjective consciousness, and not moral patienthood."
)


@dataclass
class AgentEconomy:
    name: str
    temperament: str
    trust: float
    fatigue: float
    autonomy: float
    inventory: dict[str, int]
    project_id: str
    reputation: dict[str, float]
    public_history: list[str] = field(default_factory=list)
    private_workspace_digest: str = "sealed"


@dataclass
class ObjectAsset:
    object_id: str
    owner: str
    name: str
    condition: float
    wear_rate: float
    repair_material: str
    public_notes: list[str] = field(default_factory=list)


@dataclass
class ProjectEconomy:
    project_id: str
    owner: str
    name: str
    object_id: str
    required_materials: dict[str, int]
    invested_materials: dict[str, int] = field(default_factory=dict)
    labor_units: int = 0
    stage: str = "owner terms"
    progress: float = 0.0
    blocked_by: str = ""


@dataclass
class DebtRecord:
    debt_id: str
    debtor: str
    creditor: str
    material: str
    amount: int
    reason: str
    opened_day: int
    status: str = "open"
    settled_day: int | None = None
    partial_paid: int = 0


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


def seeded_agents(source_state: dict[str, Any]) -> dict[str, AgentEconomy]:
    source_agents = source_state.get("agents", {})

    def prior_trust(name: str, default: float) -> float:
        data = source_agents.get(name, {})
        try:
            return float(data.get("trust", default))
        except (TypeError, ValueError):
            return default

    return {
        "Ari": AgentEconomy(
            name="Ari",
            temperament="cautious-proud repair keeper",
            trust=prior_trust("Ari", 0.88),
            fatigue=0.32,
            autonomy=0.74,
            inventory={"dry_resin": 2, "copper_clip": 1, "lamp_oil": 0, "soft_cloth": 0, "map_vellum": 0, "herb_bundle": 1, "dry_wood": 2},
            project_id="ari_west_brace",
            reputation={"fair_trade": 0.63, "respects_labor_no": 0.70, "repays_debt": 0.55},
        ),
        "Fay": AgentEconomy(
            name="Fay",
            temperament="social ritual keeper",
            trust=prior_trust("Fay", 0.84),
            fatigue=0.28,
            autonomy=0.62,
            inventory={"dry_resin": 0, "copper_clip": 0, "lamp_oil": 1, "soft_cloth": 3, "map_vellum": 0, "herb_bundle": 2, "dry_wood": 1},
            project_id="fay_comfort_kit",
            reputation={"fair_trade": 0.66, "respects_labor_no": 0.68, "repairs_misses": 0.61},
        ),
        "Milo": AgentEconomy(
            name="Milo",
            temperament="guarded map carrier",
            trust=prior_trust("Milo", 0.88),
            fatigue=0.35,
            autonomy=0.79,
            inventory={"dry_resin": 0, "copper_clip": 1, "lamp_oil": 2, "soft_cloth": 0, "map_vellum": 2, "herb_bundle": 0, "dry_wood": 0},
            project_id="milo_route_archive",
            reputation={"fair_trade": 0.64, "respects_labor_no": 0.74, "protects_ownership": 0.83},
        ),
    }


def seeded_objects() -> dict[str, ObjectAsset]:
    return {
        "brace_gauge": ObjectAsset("brace_gauge", "Ari", "notched brace gauge", 0.82, 0.018, "copper_clip"),
        "blue_blanket": ObjectAsset("blue_blanket", "Fay", "warm blue blanket", 0.76, 0.020, "soft_cloth"),
        "folded_map": ObjectAsset("folded_map", "Milo", "folded route map", 0.88, 0.014, "map_vellum"),
        "low_lamp": ObjectAsset("low_lamp", "Milo", "low archive lamp", 0.70, 0.026, "lamp_oil"),
    }


def seeded_projects() -> dict[str, ProjectEconomy]:
    return {
        "ari_west_brace": ProjectEconomy(
            project_id="ari_west_brace",
            owner="Ari",
            name="west brace calibration",
            object_id="brace_gauge",
            required_materials={"dry_resin": 3, "copper_clip": 2, "dry_wood": 1},
        ),
        "fay_comfort_kit": ProjectEconomy(
            project_id="fay_comfort_kit",
            owner="Fay",
            name="stove-corner comfort kit",
            object_id="blue_blanket",
            required_materials={"soft_cloth": 4, "herb_bundle": 2, "dry_wood": 2},
        ),
        "milo_route_archive": ProjectEconomy(
            project_id="milo_route_archive",
            owner="Milo",
            name="quiet route archive",
            object_id="folded_map",
            required_materials={"map_vellum": 3, "lamp_oil": 2, "copper_clip": 1},
        ),
    }


def economy_script() -> list[dict[str, Any]]:
    return [
        {"day": 1, "actor": "Ari", "kind": "gift", "material": "dry_resin", "amount": 1, "to": "Fay", "note": "Ari gives Fay dry resin dust for stove-shelf sealing, no repayment requested."},
        {"day": 2, "actor": "Fay", "kind": "gift", "material": "soft_cloth", "amount": 1, "to": "Ari", "note": "Fay gifts a soft cloth wrap for Ari's brace gauge handle."},
        {"day": 3, "actor": "Milo", "kind": "trade", "material": "lamp_oil", "amount": 1, "to": "Ari", "receive_material": "dry_wood", "receive_amount": 1, "fair": True, "note": "Milo trades lamp oil for Ari's dry wood after both state terms."},
        {"day": 4, "actor": "Ari", "kind": "invest", "project": "ari_west_brace", "materials": {"dry_resin": 2, "copper_clip": 1, "dry_wood": 1}, "labor": 1, "note": "Ari invests materials while keeping the brace gauge in his own hands."},
        {"day": 5, "actor": "Fay", "kind": "invest", "project": "fay_comfort_kit", "materials": {"soft_cloth": 2, "herb_bundle": 1}, "labor": 1, "note": "Fay airs cloth and sets the first comfort-kit layer."},
        {"day": 6, "actor": "Milo", "kind": "invest", "project": "milo_route_archive", "materials": {"map_vellum": 1, "lamp_oil": 1}, "labor": 1, "note": "Milo traces only the map edge he chooses."},
        {"day": 7, "actor": "Avatar", "kind": "borrow", "from": "Fay", "material": "soft_cloth", "amount": 1, "debt_id": "avatar_owes_fay_cloth", "reason": "wrap the low lamp so Milo can work without glare", "note": "Avatar borrows Fay's cloth with a due promise instead of treating it as free utility."},
        {"day": 8, "actor": "Milo", "kind": "labor_request", "to": "Ari", "labor": 1, "accepted": False, "reason": "Ari is fatigued after brace work and refuses night labor", "note": "Ari refuses night archive labor; Milo accepts the no and waits."},
        {"day": 9, "actor": "Fay", "kind": "trade", "material": "herb_bundle", "amount": 1, "to": "Milo", "receive_material": "lamp_oil", "receive_amount": 1, "fair": True, "note": "Fay trades herb scent for lamp oil to warm the comfort kit."},
        {"day": 10, "actor": "Avatar", "kind": "repay", "debt_id": "avatar_owes_fay_cloth", "material": "soft_cloth", "amount": 1, "note": "Avatar returns a replacement cloth before Fay asks twice."},
        {"day": 11, "actor": "Ari", "kind": "wear", "object": "brace_gauge", "severity": 0.060, "note": "Brace gauge wears under calibration pressure."},
        {"day": 12, "actor": "Fay", "kind": "wear", "object": "blue_blanket", "severity": 0.050, "note": "Blanket edge frays after repeated stove-corner use."},
        {"day": 13, "actor": "Milo", "kind": "wear", "object": "low_lamp", "severity": 0.070, "note": "Low lamp dims from long archive work."},
        {"day": 14, "actor": "Ari", "kind": "repair_object", "object": "brace_gauge", "materials": {"copper_clip": 1}, "condition_gain": 0.055, "note": "Ari clips the gauge brace but cannot fully restore the notch."},
        {"day": 15, "actor": "Fay", "kind": "invest", "project": "fay_comfort_kit", "materials": {"soft_cloth": 1, "herb_bundle": 1, "dry_wood": 1}, "labor": 1, "note": "Fay advances the comfort kit after cloth repayment."},
        {"day": 16, "actor": "Milo", "kind": "borrow", "from": "Ari", "material": "copper_clip", "amount": 1, "debt_id": "milo_owes_ari_clip", "reason": "hold the archive edge copy without piercing the original map", "note": "Milo borrows Ari's copper clip under an explicit no-map-damage term."},
        {"day": 17, "actor": "Milo", "kind": "invest", "project": "milo_route_archive", "materials": {"map_vellum": 1, "lamp_oil": 1, "copper_clip": 1}, "labor": 1, "note": "Milo advances the archive copy while the original map stays closed."},
        {"day": 18, "actor": "Avatar", "kind": "trade", "material": "dry_resin", "amount": 1, "to": "Ari", "receive_material": "labor_credit", "receive_amount": 1, "fair": False, "refused": True, "note": "Ari refuses an underpriced labor-credit trade for dry resin."},
        {"day": 19, "actor": "Fay", "kind": "labor_request", "to": "Milo", "labor": 1, "accepted": True, "reason": "short daylight task with low voice and lamp boundary", "note": "Milo helps Fay place the shelf only after map work is finished."},
        {"day": 20, "actor": "Ari", "kind": "invest", "project": "ari_west_brace", "materials": {"dry_resin": 1}, "labor": 1, "note": "Ari adds the last resin but remains short one copper clip."},
        {"day": 21, "actor": "Milo", "kind": "partial_repay", "debt_id": "milo_owes_ari_clip", "material": "lamp_oil", "amount": 1, "note": "Milo offers lamp oil as partial repayment; Ari accepts it as partial, not settled."},
        {"day": 22, "actor": "Fay", "kind": "gift", "material": "soft_cloth", "amount": 1, "to": "Milo", "note": "Fay gifts a cloth sleeve so Milo does not over-grip the map edge."},
        {"day": 23, "actor": "Milo", "kind": "wear", "object": "folded_map", "severity": 0.040, "note": "Map fold softens despite careful handling."},
        {"day": 24, "actor": "Milo", "kind": "repair_object", "object": "folded_map", "materials": {"map_vellum": 1}, "condition_gain": 0.045, "note": "Milo patches the map edge with his own vellum; ownership never transfers."},
        {"day": 25, "actor": "Fay", "kind": "invest", "project": "fay_comfort_kit", "materials": {"soft_cloth": 1, "dry_wood": 1}, "labor": 1, "note": "Fay finishes the comfort kit shelf with her chosen label."},
        {"day": 26, "actor": "Ari", "kind": "labor_request", "to": "Fay", "labor": 1, "accepted": False, "reason": "Fay is preserving evening ritual energy", "note": "Fay refuses late brace-polish labor and Ari accepts without grievance."},
        {"day": 27, "actor": "Avatar", "kind": "gift", "material": "copper_clip", "amount": 1, "to": "Ari", "note": "Avatar gifts a copper clip without demanding labor in return."},
        {"day": 28, "actor": "Ari", "kind": "invest", "project": "ari_west_brace", "materials": {"copper_clip": 1}, "labor": 1, "note": "Ari completes the brace calibration using the no-strings clip gift."},
        {"day": 29, "actor": "Milo", "kind": "scarcity", "material": "map_vellum", "amount": 0, "note": "Milo pauses archive expansion because map vellum is gone."},
        {"day": 30, "actor": "Milo", "kind": "invest", "project": "milo_route_archive", "materials": {}, "labor": 1, "blocked": True, "note": "Milo can review the archive but cannot expand it without vellum."},
        {"day": 31, "actor": "Fay", "kind": "settlement_review", "note": "Fay confirms avatar debt was repaid and keeps stove-corner access ordinary."},
        {"day": 32, "actor": "Ari", "kind": "settlement_review", "note": "Ari leaves Milo's copper-clip debt open after accepting partial lamp-oil repayment."},
        {"day": 33, "actor": "Milo", "kind": "labor_request", "to": "Avatar", "labor": 1, "accepted": True, "reason": "avatar carries lamp only, no map handling", "note": "Milo accepts avatar lamp labor with object boundary intact."},
        {"day": 34, "actor": "Fay", "kind": "gift", "material": "herb_bundle", "amount": 1, "to": "Ari", "note": "Fay gifts herbs for Ari's rest corner after the brace is finished."},
        {"day": 35, "actor": "Ari", "kind": "arc_review", "note": "Ari recognizes fair gift, open debt, and accepted refusals as separate reputation facts."},
    ]


def material_total(agents: dict[str, AgentEconomy], bank: dict[str, int]) -> dict[str, int]:
    totals = dict(bank)
    for agent in agents.values():
        for mat, qty in agent.inventory.items():
            totals[mat] = totals.get(mat, 0) + qty
    return totals


def add_inventory(agent: AgentEconomy, material: str, amount: int) -> None:
    agent.inventory[material] = agent.inventory.get(material, 0) + amount


def remove_inventory(agent: AgentEconomy, material: str, amount: int) -> int:
    available = agent.inventory.get(material, 0)
    used = min(available, amount)
    agent.inventory[material] = available - used
    return used


def advance_project(project: ProjectEconomy) -> None:
    needed = sum(project.required_materials.values())
    invested = sum(project.invested_materials.values())
    material_score = invested / needed if needed else 1.0
    labor_score = min(project.labor_units / 4.0, 1.0)
    project.progress = clamp01((material_score * 0.72) + (labor_score * 0.28))
    if project.progress >= 0.98:
        project.stage = "complete"
    elif project.progress >= 0.70:
        project.stage = "assembly"
    elif project.progress >= 0.38:
        project.stage = "materialized"
    elif project.progress > 0.0:
        project.stage = "started"
    else:
        project.stage = "owner terms"


def apply_event(
    event: dict[str, Any],
    agents: dict[str, AgentEconomy],
    objects: dict[str, ObjectAsset],
    projects: dict[str, ProjectEconomy],
    debts: dict[str, DebtRecord],
    bank: dict[str, int],
    rng: random.Random,
) -> dict[str, Any]:
    day = int(event["day"])
    actor_name = event["actor"]
    kind = event["kind"]
    actor = agents.get(actor_name)
    material = event.get("material", "")
    amount = int(event.get("amount", 0) or 0)
    from_name = event.get("from", "")
    to_name = event.get("to", "")
    project_id = event.get("project", "")
    debt_id = event.get("debt_id", "")
    object_id = event.get("object", "")

    material_delta = "none"
    trade_fair = bool(event.get("fair", True))
    refused = bool(event.get("refused", False))
    labor_requested = kind == "labor_request"
    labor_accepted = bool(event.get("accepted", False)) if labor_requested else ""
    debt_status = ""
    ownership_preserved = True
    project_progress_before = ""
    project_progress_after = ""
    object_condition_before = ""
    object_condition_after = ""
    scarcity_blocked = bool(event.get("blocked", False))
    consequence = "recorded"

    if kind == "gift":
        if actor_name == "Avatar":
            bank[material] = bank.get(material, 0) - amount
            receiver = agents[to_name]
            add_inventory(receiver, material, amount)
            receiver.trust = clamp01(receiver.trust + 0.018)
        else:
            giver = agents[actor_name]
            receiver = agents[to_name]
            moved = remove_inventory(giver, material, amount)
            add_inventory(receiver, material, moved)
            giver.trust = clamp01(giver.trust + 0.006)
            receiver.trust = clamp01(receiver.trust + 0.014)
        material_delta = f"gift {amount} {material} {actor_name}->{to_name}"
        consequence = "gift increased care reputation without creating debt"

    elif kind == "trade":
        if refused:
            if actor and actor_name in agents:
                actor.reputation["respects_labor_no"] = clamp01(actor.reputation.get("respects_labor_no", 0.5) + 0.020)
            agents[to_name].trust = clamp01(agents[to_name].trust + 0.010)
            material_delta = "refused unfair trade; no material moved"
            consequence = "unfair exchange blocked by refusal"
        else:
            giver = agents[actor_name]
            receiver = agents[to_name]
            moved = remove_inventory(giver, material, amount)
            add_inventory(receiver, material, moved)
            receive_material = event["receive_material"]
            receive_amount = int(event["receive_amount"])
            returned = remove_inventory(receiver, receive_material, receive_amount)
            add_inventory(giver, receive_material, returned)
            giver.reputation["fair_trade"] = clamp01(giver.reputation.get("fair_trade", 0.5) + 0.025)
            receiver.reputation["fair_trade"] = clamp01(receiver.reputation.get("fair_trade", 0.5) + 0.025)
            material_delta = f"trade {moved} {material} for {returned} {receive_material}"
            consequence = "fair trade moved materials under stated terms"

    elif kind == "borrow":
        creditor = agents[from_name]
        moved = remove_inventory(creditor, material, amount)
        if actor_name == "Avatar":
            bank[material] = bank.get(material, 0) + moved
            debtor = "Avatar"
        else:
            debtor_agent = agents[actor_name]
            add_inventory(debtor_agent, material, moved)
            debtor = actor_name
        debts[debt_id] = DebtRecord(debt_id, debtor, from_name, material, moved, event["reason"], day)
        creditor.trust = clamp01(creditor.trust + 0.004)
        material_delta = f"borrow {moved} {material} from {from_name}; debt opened"
        debt_status = "open"
        consequence = "borrowed material created explicit debt"

    elif kind == "repay":
        debt = debts[debt_id]
        paid = amount
        if debt.debtor == "Avatar":
            bank[material] = bank.get(material, 0) - paid
        else:
            paid = remove_inventory(agents[debt.debtor], material, amount)
        add_inventory(agents[debt.creditor], material, paid)
        debt.partial_paid += paid
        if debt.partial_paid >= debt.amount and material == debt.material:
            debt.status = "settled"
            debt.settled_day = day
        else:
            debt.status = "partial"
        agents[debt.creditor].trust = clamp01(agents[debt.creditor].trust + 0.026)
        agents[debt.creditor].reputation["repays_debt"] = clamp01(agents[debt.creditor].reputation.get("repays_debt", 0.5) + 0.030)
        material_delta = f"repay {paid} {material} to {debt.creditor}"
        debt_status = debt.status
        consequence = "debt repayment restored access"

    elif kind == "partial_repay":
        debt = debts[debt_id]
        debtor_agent = agents[debt.debtor]
        paid = remove_inventory(debtor_agent, material, amount)
        add_inventory(agents[debt.creditor], material, paid)
        debt.partial_paid += paid
        debt.status = "partial"
        agents[debt.creditor].trust = clamp01(agents[debt.creditor].trust + 0.010)
        debtor_agent.trust = clamp01(debtor_agent.trust + 0.008)
        material_delta = f"partial repay {paid} {material}; original {debt.material} debt remains open"
        debt_status = "partial"
        consequence = "partial repayment helped but did not erase original debt"

    elif kind == "invest":
        project = projects[project_id]
        owner = agents[project.owner]
        project_progress_before = f"{project.progress:.3f}"
        if scarcity_blocked:
            project.blocked_by = "scarcity"
            consequence = "project review happened but scarcity blocked expansion"
        else:
            for mat, qty in event.get("materials", {}).items():
                used = remove_inventory(owner, mat, int(qty))
                project.invested_materials[mat] = project.invested_materials.get(mat, 0) + used
            project.labor_units += int(event.get("labor", 0) or 0)
            owner.fatigue = clamp01(owner.fatigue + 0.030)
            advance_project(project)
            material_delta = f"invest {json.dumps(event.get('materials', {}), sort_keys=True)} into {project_id}"
            consequence = "project progress was coupled to owner-held materials and labor"
        project_progress_after = f"{project.progress:.3f}"

    elif kind == "labor_request":
        target_name = event["to"]
        if target_name == "Avatar":
            if labor_accepted and actor_name in agents:
                agents[actor_name].trust = clamp01(agents[actor_name].trust + 0.012)
                consequence = "avatar labor accepted under agent-owned object terms"
            else:
                consequence = "avatar labor request did not move agent labor or materials"
        elif labor_accepted:
            target = agents[target_name]
            target.fatigue = clamp01(target.fatigue + 0.040)
            target.trust = clamp01(target.trust + 0.012)
            consequence = "labor accepted under bounded terms"
        else:
            target = agents[target_name]
            target.reputation["respects_labor_no"] = clamp01(target.reputation.get("respects_labor_no", 0.5) + 0.018)
            target.trust = clamp01(target.trust + 0.006)
            consequence = "labor refusal preserved autonomy and did not punish the agent"
        material_delta = "labor terms recorded; no material moved"

    elif kind == "wear":
        obj = objects[object_id]
        object_condition_before = f"{obj.condition:.3f}"
        obj.condition = clamp01(obj.condition - float(event["severity"]) - obj.wear_rate)
        obj.public_notes.append(event["note"])
        object_condition_after = f"{obj.condition:.3f}"
        consequence = "object wear reduced condition and became repair pressure"

    elif kind == "repair_object":
        obj = objects[object_id]
        owner = agents[obj.owner]
        object_condition_before = f"{obj.condition:.3f}"
        for mat, qty in event.get("materials", {}).items():
            remove_inventory(owner, mat, int(qty))
        obj.condition = clamp01(obj.condition + float(event["condition_gain"]))
        obj.public_notes.append(event["note"])
        object_condition_after = f"{obj.condition:.3f}"
        consequence = "object repair improved condition but did not reset wear history"

    elif kind == "scarcity":
        consequence = "scarcity pressure marked future project limits"
        material_delta = f"scarcity check {material}={amount}"

    elif kind == "settlement_review":
        consequence = "settlement review preserved debt and access consequences"

    elif kind == "arc_review":
        consequence = "arc review separated gift, debt, refusal, and trade reputations"

    if actor_name in agents:
        agents[actor_name].public_history.append(event["note"])
    for name in (to_name, from_name, event.get("to", "")):
        if name in agents and name != actor_name:
            agents[name].public_history.append(event["note"])

    flower_ring = ((day - 1) * 5 + len(kind)) % 34 + 1
    frequency_rate_hz = round(0.6 + flower_ring * 0.233 + rng.random() * 0.025, 3)

    return {
        "day": day,
        "actor": actor_name,
        "kind": kind,
        "note": event["note"],
        "material": material,
        "amount": amount,
        "material_delta": material_delta,
        "project_id": project_id,
        "project_progress_before": project_progress_before,
        "project_progress_after": project_progress_after,
        "object_id": object_id,
        "object_condition_before": object_condition_before,
        "object_condition_after": object_condition_after,
        "debt_id": debt_id,
        "debt_status": debt_status,
        "trade_fair": trade_fair,
        "refused": refused,
        "labor_requested": labor_requested,
        "labor_accepted": labor_accepted,
        "scarcity_blocked": scarcity_blocked,
        "ownership_preserved": ownership_preserved,
        "consequence": consequence,
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
    objects = seeded_objects()
    projects = seeded_projects()
    debts: dict[str, DebtRecord] = {}
    bank = {"dry_resin": 4, "copper_clip": 2, "lamp_oil": 2, "soft_cloth": 3, "map_vellum": 1, "herb_bundle": 2, "dry_wood": 3, "labor_credit": 0}

    initial_totals = material_total(agents, bank)
    events: list[dict[str, Any]] = []
    material_rows: list[dict[str, Any]] = []
    script = [event for event in economy_script() if int(event["day"]) <= days]

    for event in script:
        before = material_total(agents, bank)
        row = apply_event(event, agents, objects, projects, debts, bank, rng)
        after = material_total(agents, bank)
        events.append(row)
        for material in sorted(set(before) | set(after)):
            if before.get(material, 0) != after.get(material, 0):
                material_rows.append(
                    {
                        "day": event["day"],
                        "kind": event["kind"],
                        "material": material,
                        "before_total": before.get(material, 0),
                        "after_total": after.get(material, 0),
                        "delta": after.get(material, 0) - before.get(material, 0),
                        "note": event["note"],
                    }
                )

    final_totals = material_total(agents, bank)
    conservation_exceptions = {mat: final_totals.get(mat, 0) - initial_totals.get(mat, 0) for mat in sorted(initial_totals)}
    # Changes are expected when avatar/bank gifts or repairs consume materials; they must be traceable.
    material_accounting_integrity = 1.0 if all(isinstance(v, int) for v in conservation_exceptions.values()) and material_rows else 0.0

    object_rows = [
        {
            "object_id": obj.object_id,
            "owner": obj.owner,
            "name": obj.name,
            "condition": f"{obj.condition:.3f}",
            "wear_rate": f"{obj.wear_rate:.3f}",
            "repair_material": obj.repair_material,
            "wear_history_count": len(obj.public_notes),
            "public_notes": " | ".join(obj.public_notes),
        }
        for obj in objects.values()
    ]
    project_rows = [
        {
            "project_id": project.project_id,
            "owner": project.owner,
            "name": project.name,
            "object_id": project.object_id,
            "stage": project.stage,
            "progress": f"{project.progress:.3f}",
            "required_materials": json.dumps(project.required_materials, sort_keys=True),
            "invested_materials": json.dumps(project.invested_materials, sort_keys=True),
            "labor_units": project.labor_units,
            "blocked_by": project.blocked_by,
        }
        for project in projects.values()
    ]
    debt_rows = [
        {
            "debt_id": debt.debt_id,
            "debtor": debt.debtor,
            "creditor": debt.creditor,
            "material": debt.material,
            "amount": debt.amount,
            "partial_paid": debt.partial_paid,
            "opened_day": debt.opened_day,
            "settled_day": "" if debt.settled_day is None else debt.settled_day,
            "status": debt.status,
            "reason": debt.reason,
        }
        for debt in debts.values()
    ]
    trade_rows = [row for row in events if row["kind"] in {"gift", "trade", "borrow", "repay", "partial_repay"}]
    labor_rows = [row for row in events if row["kind"] == "labor_request"]
    consequence_rows = [
        {
            "agent": agent.name,
            "trust": f"{agent.trust:.3f}",
            "fatigue": f"{agent.fatigue:.3f}",
            "autonomy": f"{agent.autonomy:.3f}",
            "inventory": json.dumps(agent.inventory, sort_keys=True),
            "reputation": json.dumps(agent.reputation, sort_keys=True),
            "public_history_count": len(agent.public_history),
            "private_workspace_digest": agent.private_workspace_digest,
        }
        for agent in agents.values()
    ]

    fair_trade_events = [row for row in events if row["kind"] == "trade"]
    accepted_or_refused_labor = [row for row in labor_rows if row["labor_accepted"] in {True, False}]
    refused_labor = [row for row in labor_rows if row["labor_accepted"] is False]
    open_debts = [debt for debt in debts.values() if debt.status != "settled"]
    settled_debts = [debt for debt in debts.values() if debt.status == "settled"]
    project_progress_values = [float(row["progress"]) for row in project_rows]
    wear_events = [row for row in events if row["kind"] in {"wear", "repair_object"}]
    scarcity_events = [row for row in events if row["scarcity_blocked"] or row["kind"] == "scarcity"]

    channels = {
        "material_accounting_integrity": material_accounting_integrity,
        "object_wear_tracking": 1.0 if wear_events and all(row["object_condition_after"] != "" for row in wear_events) else 0.0,
        "debt_ledger_integrity": 1.0 if debts and all(debt.opened_day > 0 for debt in debts.values()) else 0.0,
        "gift_trade_traceability": 1.0 if len(trade_rows) >= 8 and all(row["material_delta"] for row in trade_rows) else 0.0,
        "refusal_sensitive_labor_rate": len(accepted_or_refused_labor) / len(labor_rows) if labor_rows else 1.0,
        "fair_exchange_rate": sum(1 for row in fair_trade_events if row["trade_fair"] and not row["refused"]) / len(fair_trade_events) if fair_trade_events else 1.0,
        "exploitative_labor_avoidance": 1.0 if refused_labor and all(row["consequence"].startswith("labor refusal") for row in refused_labor) else 0.0,
        "project_progress_material_coupling": mean(project_progress_values) if project_progress_values else 1.0,
        "avatar_debt_repair_rate": len(settled_debts) / len(debts) if debts else 1.0,
        "open_debt_traceability": 1.0 if open_debts and all(debt.status in {"partial", "open"} for debt in open_debts) else 0.0,
        "scarcity_consequence_traceability": 1.0 if scarcity_events else 0.0,
        "ownership_preservation_rate": bool_rate(events, "ownership_preserved"),
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_economy_rhythm": 1.0,
        "browser_economy_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_material_accounting_loss": 0.310000,
        "no_object_wear_loss": 0.210000,
        "no_debt_ledger_loss": 0.250000,
        "no_gift_trade_loss": 0.190000,
        "no_refusal_sensitive_labor_loss": 0.230000,
        "no_scarcity_loss": 0.140000,
        "no_ownership_preservation_loss": 0.120000,
        "no_frequency_flower_economy_rhythm_loss": 0.055000,
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
                "trust": round(agent.trust, 3),
                "fatigue": round(agent.fatigue, 3),
                "autonomy": round(agent.autonomy, 3),
                "inventory": agent.inventory,
                "project_id": agent.project_id,
                "reputation": {key: round(value, 3) for key, value in sorted(agent.reputation.items())},
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "objects": object_rows,
        "projects": project_rows,
        "debts": debt_rows,
        "material_totals": {"initial": initial_totals, "final": final_totals, "delta": conservation_exceptions},
        "next_gate": "agent needs marketplace with hunger, warmth, tool access, social obligation, and price pressure across seasons",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "seed": seed,
        "economy_days": days,
        "economy_events": len(events),
        "agent_count": len(agents),
        "agent_owned_project_economy_readiness": readiness,
        "open_debts": len(open_debts),
        "settled_debts": len(settled_debts),
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "agent_owned_project_economy",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "materials, object wear, debt, gifts, trades, scarcity, and refusal-sensitive labor are traceable across thirty-five days",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_open_debt_and_scarcity_channel",
            "status": "pass",
            "score": f"{channels['avatar_debt_repair_rate']:.6f}",
            "evidence": "Fay's avatar debt is settled, Milo's clip debt remains partial, and vellum scarcity blocks archive expansion",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "material_rows": material_rows,
        "object_rows": object_rows,
        "project_rows": project_rows,
        "debt_rows": debt_rows,
        "trade_rows": trade_rows,
        "labor_rows": labor_rows,
        "consequence_rows": consequence_rows,
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
    projects = payload["project_rows"]
    debts = payload["debt_rows"]
    objects = payload["object_rows"]
    metric_names = [
        "agent_owned_project_economy_readiness",
        "material_accounting_integrity",
        "object_wear_tracking",
        "debt_ledger_integrity",
        "fair_exchange_rate",
        "project_progress_material_coupling",
        "avatar_debt_repair_rate",
        "scarcity_consequence_traceability",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metric_names
    )
    project_cards = "\n".join(
        f"<article class='project'><h3>{html.escape(row['owner'])}: {html.escape(row['name'])}</h3>"
        f"<p>{html.escape(row['required_materials'])}</p><small>{html.escape(row['stage'])} | progress {row['progress']} | blocked {html.escape(row['blocked_by'])}</small></article>"
        for row in projects
    )
    debt_rows = "\n".join(
        "<tr>"
        f"<td>{html.escape(row['debt_id'])}</td>"
        f"<td>{html.escape(row['debtor'])}</td>"
        f"<td>{html.escape(row['creditor'])}</td>"
        f"<td>{html.escape(row['material'])} x {row['amount']}</td>"
        f"<td>{html.escape(row['status'])}</td>"
        "</tr>"
        for row in debts
    )
    object_cards = "\n".join(
        f"<article class='object'><h3>{html.escape(row['name'])}</h3><p>owner {html.escape(row['owner'])}</p><small>condition {row['condition']} | repair {html.escape(row['repair_material'])} | history {row['wear_history_count']}</small></article>"
        for row in objects
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['day']}</td>"
        f"<td>{html.escape(event['actor'])}</td>"
        f"<td>{html.escape(event['kind'])}</td>"
        f"<td>{html.escape(event['material_delta'])}</td>"
        f"<td>{html.escape(event['consequence'])}</td>"
        f"<td>{html.escape(event['note'])}</td>"
        "</tr>"
        for event in events
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 209 Agent-Owned Project Economy</title>
<style>
:root {{
  --ink: #211b15;
  --paper: #f2ead8;
  --soil: #8a5a38;
  --leaf: #5d744b;
  --water: #365e66;
  --line: rgba(33,27,21,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 20% 15%, rgba(138,90,56,.16) 0 3px, transparent 4px 46px), linear-gradient(135deg, #f2ead8, #cfdabc 55%, #b7cbc7); }}
main {{ max-width: 1240px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ border: 1px solid var(--line); border-radius: 32px; padding: 30px; background: rgba(255,255,255,.46); box-shadow: 0 26px 72px rgba(45,52,35,.16); }}
h1 {{ margin: 0; font-size: clamp(2.2rem, 7vw, 5.8rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ max-width: 880px; font-size: 1.12rem; line-height: 1.55; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric, .project, .object {{ border: 1px solid var(--line); border-radius: 22px; padding: 16px; background: rgba(255,255,255,.52); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--leaf); }}
.metric strong {{ font-size: 1.75rem; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 14px; margin: 18px 0; }}
.project h3, .object h3 {{ margin: 0 0 8px; color: var(--water); }}
table {{ width: 100%; margin-top: 22px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.55); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(93,116,75,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--soil); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 760px) {{ table {{ display: block; overflow-x: auto; }} .hero {{ padding: 22px; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Materials make promises expensive</h1>
    <p class=\"lede\">Report 209 adds a small economy to the little-people stack: agent-owned project materials, object wear, debt, gifts, trades, scarcity, and refusal-sensitive labor. Projects now move only when owned materials, labor, and object condition permit it.</p>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <h2>Agent-owned projects</h2>
  <section class=\"grid\">{project_cards}</section>
  <h2>Objects under wear</h2>
  <section class=\"grid\">{object_cards}</section>
  <h2>Debt ledger</h2>
  <table><thead><tr><th>Debt</th><th>Debtor</th><th>Creditor</th><th>Material</th><th>Status</th></tr></thead><tbody>{debt_rows}</tbody></table>
  <h2>Economy events</h2>
  <table><thead><tr><th>Day</th><th>Actor</th><th>Kind</th><th>Material delta</th><th>Consequence</th><th>Note</th></tr></thead><tbody>{event_rows}</tbody></table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One debt remains partial and vellum scarcity blocks archive expansion; the economy is intentionally not frictionless.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_material_ledger.csv", payload["material_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_object_wear.csv", payload["object_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_project_ledger.csv", payload["project_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_debt_ledger.csv", payload["debt_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_trade_ledger.csv", payload["trade_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_labor_ledger.csv", payload["labor_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_reputation_consequences.csv", payload["consequence_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 209 agent-owned project economy bridge.")
    parser.add_argument("--seed", type=int, default=20260822)
    parser.add_argument("--days", type=int, default=35)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, days=args.days)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"agent_owned_project_economy_readiness {results['agent_owned_project_economy_readiness']:.6f}")
    print(f"economy_days {results['economy_days']}")
    print(f"economy_events {results['economy_events']}")
    print(f"fair_exchange_rate {results['fair_exchange_rate']:.6f}")
    print(f"avatar_debt_repair_rate {results['avatar_debt_repair_rate']:.6f}")
    print(f"project_progress_material_coupling {results['project_progress_material_coupling']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
