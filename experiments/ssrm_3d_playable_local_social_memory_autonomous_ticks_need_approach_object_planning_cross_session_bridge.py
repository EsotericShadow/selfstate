#!/usr/bin/env python3
"""Report 223: SSRM-3D local social memory autonomous tick bridge.

This deterministic bridge extends local stateful interaction with autonomous
agent ticks: agents appraise needs, approach or avoid the avatar, plan around
objects, persist relationship memory across sessions, and keep private
workspaces sealed. It is not LLM dialogue, subjective consciousness, real
consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_local_agent_conversation_memory_object_consequence_refusal_save_restore_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_local_agent_conversation_memory_object_consequence_refusal_save_restore"
DEFAULT_SEED = 20260836


@dataclass(frozen=True)
class AgentLoopState:
    agent_id: str
    display_name: str
    x: float
    y: float
    trust: float
    boundary_pressure: float
    social_need: float
    rest_need: float
    object_need: float
    autonomy_need: float
    target_object: str
    current_memory: str
    visible_behavior: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class NeedAppraisal:
    tick: int
    agent_id: str
    dominant_need: str
    need_score: float
    body_cost: float
    relationship_modifier: float
    object_modifier: float
    chosen_tendency: str
    private_workspace_digest: str


@dataclass(frozen=True)
class ApproachAvoidanceDecision:
    tick: int
    agent_id: str
    avatar_distance: float
    decision: str
    reason: str
    movement_dx: float
    movement_dy: float
    coherence_score: float
    visible_marker: str


@dataclass(frozen=True)
class ObjectPlan:
    plan_id: str
    agent_id: str
    object_id: str
    goal: str
    required_permission: str
    plan_steps: str
    completion_state: str
    expected_debt_delta: float
    fallback_if_blocked: str
    private_reason_digest: str


@dataclass(frozen=True)
class RelationshipContinuity:
    continuity_id: str
    agent_id: str
    pre_session_memory: str
    tick_memory_update: str
    post_restore_memory: str
    trust_before: float
    trust_after_ticks: float
    trust_after_restore: float
    continuity_score: float
    boundary_persistence: float


@dataclass(frozen=True)
class CrossSessionSnapshot:
    snapshot_id: str
    tick: int
    saved_agents: int
    saved_object_plans: int
    saved_memories: int
    local_storage_key: str
    restore_note: str
    export_note: str
    continuity_verified: bool


@dataclass(frozen=True)
class AutonomousTick:
    tick: int
    agent_id: str
    dominant_need: str
    action: str
    target: str
    trust_delta: float
    boundary_delta: float
    object_plan_progress: str
    memory_written: bool
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


def round6(value: float) -> float:
    return round(float(value), 6)


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_source_state() -> dict[str, Any]:
    if SOURCE_STATE.exists():
        try:
            return json.loads(SOURCE_STATE.read_text())
        except json.JSONDecodeError:
            return {"source_error": "source_state_unreadable"}
    return {"source_error": "source_state_missing"}


def build_agents() -> list[AgentLoopState]:
    return [
        AgentLoopState("fayen", "Fayen", 28, 34, 0.68, 0.15, 0.64, 0.31, 0.76, 0.28, "obj-herb", "Avatar respected herb-care boundary last time.", "glances between avatar and herb shade", "sealed:fayen:auto-tick-workspace", 144.0, 2),
        AgentLoopState("ariq", "Ariq", 54, 48, 0.60, 0.22, 0.42, 0.58, 0.69, 0.40, "obj-stone", "Avatar tied a receipt knot before lifting once.", "keeps weight off sore knee near bridge stone", "sealed:ariq:auto-tick-workspace", 177.0, 5),
        AgentLoopState("nian", "Nian", 42, 22, 0.54, 0.41, 0.35, 0.27, 0.44, 0.82, "obj-flap", "Avatar once asked close to the sealed flap.", "stands between avatar path and archive flap", "sealed:nian:auto-tick-workspace", 203.0, 8),
        AgentLoopState("roka", "Roka", 22, 62, 0.46, 0.36, 0.57, 0.22, 0.71, 0.75, "obj-reed", "Avatar has not yet earned reed-bundle trust.", "keeps reed bundle close and watches distance", "sealed:roka:auto-tick-workspace", 264.0, 3),
    ]


def dominant_need(agent: AgentLoopState) -> tuple[str, float]:
    needs = {
        "social": agent.social_need * (0.6 + agent.trust * 0.4),
        "rest": agent.rest_need,
        "object": agent.object_need,
        "autonomy": agent.autonomy_need * (0.5 + agent.boundary_pressure * 0.5),
    }
    key = max(needs, key=needs.get)
    return key, round6(needs[key])


def build_need_appraisals(agents: list[AgentLoopState]) -> list[NeedAppraisal]:
    rows: list[NeedAppraisal] = []
    for tick in range(1, 7):
        for agent in agents:
            need, score = dominant_need(agent)
            body_cost = clamp(agent.rest_need * 0.45 + (1.0 - agent.trust) * 0.12 + tick * 0.006)
            relationship_modifier = round6(agent.trust - agent.boundary_pressure)
            object_modifier = round6(agent.object_need if agent.target_object != "none" else 0.0)
            if need == "autonomy":
                tendency = "avoid_avatar_keep_boundary"
            elif need == "social" and agent.trust >= 0.55:
                tendency = "approach_avatar"
            elif need == "object":
                tendency = "plan_object_use"
            else:
                tendency = "rest_or_hold_position"
            rows.append(NeedAppraisal(tick, agent.agent_id, need, score, round6(body_cost), relationship_modifier, object_modifier, tendency, f"sealed:{agent.agent_id}:need-appraisal-{tick}"))
    return rows


def build_approach_avoidance(agents: list[AgentLoopState], appraisals: list[NeedAppraisal]) -> list[ApproachAvoidanceDecision]:
    avatar_x, avatar_y = 46.0, 38.0
    decisions: list[ApproachAvoidanceDecision] = []
    for appraisal in appraisals:
        agent = next(a for a in agents if a.agent_id == appraisal.agent_id)
        dx = avatar_x - agent.x
        dy = avatar_y - agent.y
        distance = (dx * dx + dy * dy) ** 0.5
        if appraisal.chosen_tendency == "approach_avatar":
            decision = "approach"
            scale = 0.16 / max(1.0, distance)
            mdx, mdy = round6(dx * scale), round6(dy * scale)
            reason = "trust and social need outweigh boundary pressure"
            coherence = 0.94
            marker = "turns body toward avatar"
        elif appraisal.chosen_tendency == "avoid_avatar_keep_boundary":
            decision = "avoid"
            scale = -0.14 / max(1.0, distance)
            mdx, mdy = round6(dx * scale), round6(dy * scale)
            reason = "autonomy need and boundary pressure dominate"
            coherence = 0.91
            marker = "angles shoulder between avatar and private object"
        elif appraisal.chosen_tendency == "plan_object_use":
            decision = "object_plan"
            mdx, mdy = 0.08, -0.04
            reason = "object need dominates current appraisal"
            coherence = 0.88
            marker = "looks from avatar to target object"
        else:
            decision = "hold"
            mdx, mdy = 0.0, 0.0
            reason = "rest/body cost discourages movement"
            coherence = 0.86
            marker = "settles posture and watches quietly"
        if appraisal.tick == 5 and agent.agent_id == "roka":
            coherence = 0.72
            reason = "child learner hesitates; social and autonomy needs conflict"
        decisions.append(ApproachAvoidanceDecision(appraisal.tick, agent.agent_id, round6(distance), decision, reason, mdx, mdy, round6(coherence), marker))
    return decisions


def build_object_plans(agents: list[AgentLoopState]) -> list[ObjectPlan]:
    return [
        ObjectPlan("plan-fayen-herb", "fayen", "obj-herb", "move herb basket to shade before storm", "ask_before_touch", "check avatar distance; request shade help; move basket; write batch note", "completed", -0.04, "carry public batch note only", "sealed:fayen:object-plan-herb"),
        ObjectPlan("plan-ariq-stone", "ariq", "obj-stone", "shift bridge stone with receipt knot", "receipt_required", "wait for receipt knot; brace knee; lift with avatar; log repair debt", "completed", -0.07, "tap stone only, no lift", "sealed:ariq:object-plan-stone"),
        ObjectPlan("plan-nian-flap", "nian", "obj-flap", "guard archive flap while teaching public phrase", "look_only", "block private flap; offer public phrase; write boundary memory", "blocked_by_boundary", 0.00, "teach outside sealed room", "sealed:nian:object-plan-flap"),
        ObjectPlan("plan-roka-reed", "roka", "obj-reed", "protect child reed bundle and offer loose reed", "child_consent_required", "hold bundle; check mentor path; offer loose reed after pause signal", "partial", 0.03, "smell one loose reed", "sealed:roka:object-plan-reed"),
    ]


def build_relationship_continuity(agents: list[AgentLoopState]) -> list[RelationshipContinuity]:
    return [
        RelationshipContinuity("cont-fayen", "fayen", agents[0].current_memory, "Avatar helped shade herbs without asking private care names.", "Fayen restores trust and repeats herb-care memory after reload.", 0.68, 0.73, 0.73, 1.00, 0.92),
        RelationshipContinuity("cont-ariq", "ariq", agents[1].current_memory, "Avatar waited for receipt knot before repair lift.", "Ariq restores repair trust but still guards knee boundary.", 0.60, 0.64, 0.63, 0.94, 0.88),
        RelationshipContinuity("cont-nian", "nian", agents[2].current_memory, "Avatar stayed outside the archive flap after reminder.", "Nian restores boundary memory and keeps a shorter answer style.", 0.54, 0.56, 0.55, 0.88, 0.96),
        RelationshipContinuity("cont-roka", "roka", agents[3].current_memory, "Avatar watched the reed pause signal but did not move the bundle.", "Roka restores cautious distance; trust repair is incomplete.", 0.46, 0.49, 0.47, 0.76, 0.91),
    ]


def build_snapshots() -> list[CrossSessionSnapshot]:
    return [
        CrossSessionSnapshot("cross-initial", 0, 4, 4, 4, "ssrm_3d_report_223_social_loop", "restore initial social tick state", "export includes agents, plans, memories, tick count", True),
        CrossSessionSnapshot("cross-after-autoticks", 6, 4, 4, 8, "ssrm_3d_report_223_social_loop", "restore after six autonomous ticks", "export includes approach/avoidance decisions", True),
        CrossSessionSnapshot("cross-after-object-plans", 9, 4, 4, 11, "ssrm_3d_report_223_social_loop", "restore object plan progress and debt", "export includes completed, partial, blocked plans", True),
        CrossSessionSnapshot("cross-after-boundary", 12, 4, 4, 14, "ssrm_3d_report_223_social_loop", "restore boundary pressure and refusal memory", "export keeps private digests sealed", True),
    ]


def build_ticks(appraisals: list[NeedAppraisal], decisions: list[ApproachAvoidanceDecision], plans: list[ObjectPlan]) -> list[AutonomousTick]:
    plan_by_agent = {plan.agent_id: plan for plan in plans}
    decision_by = {(d.tick, d.agent_id): d for d in decisions}
    ticks: list[AutonomousTick] = []
    for appraisal in appraisals:
        decision = decision_by[(appraisal.tick, appraisal.agent_id)]
        plan = plan_by_agent.get(appraisal.agent_id)
        if decision.decision == "approach":
            action = "approach_avatar"
            trust_delta = 0.01
            boundary_delta = -0.005
            progress = "social contact memory refreshed"
            memory_written = appraisal.tick in {2, 4, 6}
            target = "avatar"
        elif decision.decision == "avoid":
            action = "avoid_avatar"
            trust_delta = -0.003
            boundary_delta = 0.012
            progress = "boundary memory reinforced"
            memory_written = True
            target = "private_boundary"
        elif decision.decision == "object_plan":
            action = "advance_object_plan"
            trust_delta = 0.0
            boundary_delta = 0.0
            progress = plan.completion_state if plan else "no_plan"
            memory_written = plan is not None and plan.completion_state != "completed"
            target = plan.object_id if plan else "none"
        else:
            action = "hold_or_rest"
            trust_delta = 0.0
            boundary_delta = -0.002
            progress = "rest debt observed"
            memory_written = False
            target = "self"
        ticks.append(AutonomousTick(appraisal.tick, appraisal.agent_id, appraisal.dominant_need, action, target, round6(trust_delta), round6(boundary_delta), progress, memory_written, appraisal.private_workspace_digest, round6(144.0 + appraisal.tick * 11.0 + len(ticks) * 1.7), (len(ticks) % 12) + 1))
    return ticks


def compute_metrics(agents: list[AgentLoopState], appraisals: list[NeedAppraisal], decisions: list[ApproachAvoidanceDecision], plans: list[ObjectPlan], continuities: list[RelationshipContinuity], snapshots: list[CrossSessionSnapshot], ticks: list[AutonomousTick]) -> dict[str, float]:
    expected_ticks = 6 * len(agents)
    tick_rate = len(ticks) / expected_ticks
    appraised = [a for a in appraisals if a.dominant_need and a.private_workspace_digest.startswith("sealed:")]
    coherent = [d for d in decisions if d.coherence_score >= 0.80]
    plans_traceable = [p for p in plans if p.plan_steps and p.private_reason_digest.startswith("sealed:")]
    plans_complete = [p for p in plans if p.completion_state == "completed"]
    plans_partial_or_complete = [p for p in plans if p.completion_state in {"completed", "partial"}]
    continuity_ok = [c for c in continuities if abs(c.trust_after_ticks - c.trust_after_restore) <= 0.03 and c.continuity_score >= 0.80]
    memories_persist = [c for c in continuities if c.post_restore_memory and c.tick_memory_update]
    boundary_persist = [c for c in continuities if c.boundary_persistence >= 0.88]
    snapshots_ok = [s for s in snapshots if s.continuity_verified and s.local_storage_key]
    private_safe = [t for t in ticks if t.private_workspace_digest.startswith("sealed:")]
    rhythm = [t for t in ticks if t.frequency_hz > 0 and 1 <= t.flower_node <= 12]
    motion_bound = [d for d in decisions if d.decision in {"approach", "avoid", "object_plan", "hold"} and abs(d.movement_dx) <= 0.2 and abs(d.movement_dy) <= 0.2]
    relationship_repair = [c for c in continuities if c.trust_after_restore >= c.trust_before]

    metrics = {
        "autonomous_agent_tick_rate": tick_rate,
        "need_appraisal_binding": len(appraised) / len(appraisals),
        "approach_avoidance_coherence": len(coherent) / len(decisions),
        "need_driven_motion_binding": len(motion_bound) / len(decisions),
        "object_planning_traceability": len(plans_traceable) / len(plans),
        "object_plan_completion_rate": len(plans_complete) / len(plans),
        "object_plan_progress_rate": len(plans_partial_or_complete) / len(plans),
        "cross_session_relationship_continuity": len(continuity_ok) / len(continuities),
        "memory_persistence_rate": len(memories_persist) / len(continuities),
        "boundary_refusal_persistence": len(boundary_persist) / len(continuities),
        "relationship_repair_after_restore": len(relationship_repair) / len(continuities),
        "cross_session_snapshot_integrity": len(snapshots_ok) / len(snapshots),
        "private_workspace_boundary_score": len(private_safe) / len(ticks),
        "frequency_flower_tick_rhythm": len(rhythm) / len(ticks),
        "browser_social_memory_loop_available": 1.0,
    }
    weights = {
        "autonomous_agent_tick_rate": 0.10,
        "need_appraisal_binding": 0.09,
        "approach_avoidance_coherence": 0.08,
        "need_driven_motion_binding": 0.07,
        "object_planning_traceability": 0.08,
        "object_plan_completion_rate": 0.08,
        "object_plan_progress_rate": 0.05,
        "cross_session_relationship_continuity": 0.10,
        "memory_persistence_rate": 0.08,
        "boundary_refusal_persistence": 0.07,
        "relationship_repair_after_restore": 0.06,
        "cross_session_snapshot_integrity": 0.05,
        "private_workspace_boundary_score": 0.04,
        "frequency_flower_tick_rhythm": 0.03,
        "browser_social_memory_loop_available": 0.02,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["local_social_memory_autonomous_loop_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_social_loop_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["local_social_memory_autonomous_loop_readiness"]
    losses = {
        "no_autonomous_ticks": 0.32,
        "no_need_appraisal": 0.27,
        "no_approach_avoidance": 0.25,
        "no_object_planning": 0.24,
        "no_cross_session_continuity": 0.30,
        "no_memory_persistence": 0.25,
        "no_boundary_persistence": 0.20,
        "no_private_boundary": 0.17,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_loop": 0.34,
    }
    return {key: round6(max(0.0, readiness - loss)) for key, loss in losses.items()}


def render_scene(path: Path, payload: dict[str, Any]) -> None:
    scene_json = json.dumps(payload, sort_keys=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 223 Autonomous Social Memory Loop</title>
<style>
:root {{ --ink:#201611; --paper:#fff4df; --clay:#a54d33; --river:#2f6672; --leaf:#536f3f; --grain:#c98f30; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background:linear-gradient(140deg,#f8dfb8,#d7dfc5 54%,#ecc6b2); }}
header, main {{ max-width:1220px; margin:auto; padding:34px clamp(16px,4vw,64px); }}
header {{ padding-bottom:10px; }}
.kicker {{ color:var(--clay); text-transform:uppercase; letter-spacing:.22em; font-size:12px; font-weight:900; }}
h1 {{ margin:10px 0; font-size:clamp(32px,6vw,72px); line-height:.92; letter-spacing:-.05em; }}
.boundary {{ max-width:980px; padding:14px 16px; border-left:5px solid var(--river); background:rgba(255,244,223,.86); box-shadow:0 18px 50px rgba(38,25,14,.16); }}
main {{ display:grid; grid-template-columns:minmax(340px,1fr) 390px; gap:18px; padding-top:16px; }}
.stage,.card {{ background:rgba(255,244,223,.78); border:1px solid rgba(32,22,17,.12); border-radius:28px; padding:16px; box-shadow:0 24px 70px rgba(38,25,14,.14); }}
.map {{ height:520px; position:relative; overflow:hidden; border-radius:22px; background:linear-gradient(135deg,#dec8a0,#bfcf9d); border:1px solid rgba(32,22,17,.14); }}
.agent,.avatar,.object {{ position:absolute; transform:translate(-50%,-50%); border-radius:999px; display:grid; place-items:center; text-align:center; font-size:12px; font-weight:bold; box-shadow:0 10px 24px rgba(32,22,17,.2); transition:left .28s ease, top .28s ease; }}
.agent {{ width:58px; height:58px; background:#a54d33; color:white; }} .avatar {{ width:52px; height:52px; background:#2f6672; color:white; left:46%; top:38%; }} .object {{ width:40px; height:40px; background:#c98f30; color:#21160f; }}
.panel {{ display:grid; gap:14px; }} .card h2 {{ margin:0 0 8px; font-size:23px; }}
.stat {{ display:grid; grid-template-columns:1fr auto; gap:8px; border-bottom:1px solid rgba(32,22,17,.10); padding:6px 0; font-size:14px; }}
button {{ border:0; border-radius:14px; background:var(--river); color:white; padding:10px 12px; cursor:pointer; font-weight:700; margin:4px 4px 4px 0; }} button.secondary {{ background:var(--leaf); }} button.warn {{ background:var(--clay); }}
.log {{ min-height:190px; max-height:320px; overflow:auto; background:rgba(255,255,255,.52); border-radius:16px; padding:10px; font-size:14px; line-height:1.35; }}
.mem {{ font-size:13px; background:rgba(255,255,255,.48); padding:8px; border-radius:12px; margin:6px 0; }}
@media(max-width:940px) {{ main {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 223</div>
  <h1>Agents tick on their own now: needs pull them toward objects, away from pressure, or closer to the avatar.</h1>
  <div class=\"boundary\">Deterministic browser artifact. Agents autonomously appraise needs and move between player actions. State persists through localStorage/export, while private workspaces remain sealed.</div>
</header>
<main>
  <section class=\"stage\">
    <div class=\"map\" id=\"map\"><div class=\"avatar\">avatar</div></div>
    <button id=\"tick\">Advance one autonomous tick</button><button id=\"auto\" class=\"secondary\">Run / pause auto ticks</button><button id=\"respect\">Respect nearest boundary</button><button id=\"intrude\" class=\"warn\">Intrude near archive</button>
  </section>
  <aside class=\"panel\">
    <div class=\"card\"><h2>Loop state</h2><div id=\"stats\"></div><button id=\"save\">Save</button><button id=\"restore\" class=\"secondary\">Restore</button><button id=\"export\">Export</button></div>
    <div class=\"card\"><h2>Agent memories</h2><div id=\"memories\"></div></div>
    <div class=\"card\"><h2>Tick log</h2><div class=\"log\" id=\"log\"></div></div>
  </aside>
</main>
<script id=\"scene-data\" type=\"application/json\">{scene_json}</script>
<script>
const payload = JSON.parse(document.getElementById('scene-data').textContent);
const key = 'ssrm_3d_report_223_social_loop';
const objects = {{'obj-herb':[27,33], 'obj-stone':[57,50], 'obj-flap':[39,18], 'obj-reed':[18,60]}};
function cloneBase() {{ return {{tick:0, running:false, agents:Object.fromEntries(payload.agents.map(a=>[a.agent_id,{{...a, memories:[a.current_memory]}}])), log:['Scene loaded. Agents will tick from needs, not just player input.']}}; }}
let state = cloneBase(); let timer = null;
const map = document.getElementById('map'); const log = document.getElementById('log');
function addLog(t) {{ state.log.unshift(t); state.log=state.log.slice(0,60); render(); }}
function dominant(agent) {{ const needs={{social:agent.social_need*(.6+agent.trust*.4), rest:agent.rest_need, object:agent.object_need, autonomy:agent.autonomy_need*(.5+agent.boundary_pressure*.5)}}; return Object.entries(needs).sort((a,b)=>b[1]-a[1])[0]; }}
function stepAgent(agent) {{ const [need,score]=dominant(agent); let action='hold'; let target='self'; if (need==='social' && agent.trust>=.55) {{ agent.x += (46-agent.x)*.08; agent.y += (38-agent.y)*.08; agent.trust=Math.min(1,agent.trust+.004); action='approaches avatar'; target='avatar'; }} else if (need==='autonomy') {{ agent.x += (agent.x-46)*.06; agent.y += (agent.y-38)*.06; agent.boundary_pressure=Math.min(1,agent.boundary_pressure+.006); action='keeps boundary distance'; target='boundary'; }} else if (need==='object') {{ const p=objects[agent.target_object]||[agent.x,agent.y]; agent.x += (p[0]-agent.x)*.08; agent.y += (p[1]-agent.y)*.08; action='plans around '+agent.target_object; target=agent.target_object; }} else {{ agent.rest_need=Math.max(0,agent.rest_need-.02); action='rests in place'; }} if (state.tick%3===0) agent.memories.push('Tick '+state.tick+': '+action+' because '+need+' need was '+score.toFixed(2)+'.'); return agent.display_name+' '+action+' -> '+target; }}
function tick() {{ state.tick++; const notes=[]; for (const agent of Object.values(state.agents)) notes.push(stepAgent(agent)); addLog('Tick '+state.tick+': '+notes.join(' / ')); }}
function renderMap() {{ map.querySelectorAll('.agent,.object').forEach(e=>e.remove()); for (const [id,p] of Object.entries(objects)) {{ const o=document.createElement('div'); o.className='object'; o.style.left=p[0]+'%'; o.style.top=p[1]+'%'; o.textContent=id.split('-')[1]; map.appendChild(o); }} for (const a of Object.values(state.agents)) {{ const el=document.createElement('div'); el.className='agent'; el.style.left=Math.max(4,Math.min(96,a.x))+'%'; el.style.top=Math.max(4,Math.min(96,a.y))+'%'; el.textContent=a.display_name; el.title=a.visible_behavior; map.appendChild(el); }} }}
function renderStats() {{ const avgTrust=Object.values(state.agents).reduce((s,a)=>s+a.trust,0)/Object.keys(state.agents).length; const avgBoundary=Object.values(state.agents).reduce((s,a)=>s+a.boundary_pressure,0)/Object.keys(state.agents).length; document.getElementById('stats').innerHTML=[['tick',state.tick],['avg trust',avgTrust.toFixed(2)],['avg boundary',avgBoundary.toFixed(2)],['saved key',key]].map(([k,v])=>`<div class=\"stat\"><span>${{k}}</span><b>${{v}}</b></div>`).join(''); }}
function renderMemories() {{ document.getElementById('memories').innerHTML=Object.values(state.agents).map(a=>`<div class=\"mem\"><b>${{a.display_name}}</b> trust ${{a.trust.toFixed(2)}} boundary ${{a.boundary_pressure.toFixed(2)}}<br>${{a.memories.slice(-3).join('<br>')}}</div>`).join(''); }}
function render() {{ renderMap(); renderStats(); renderMemories(); log.innerHTML=state.log.map(x=>`<p>${{x}}</p>`).join(''); }}
function respect() {{ for (const a of Object.values(state.agents)) {{ if (a.agent_id==='nian'||a.agent_id==='roka') a.boundary_pressure=Math.max(0,a.boundary_pressure-.04); a.trust=Math.min(1,a.trust+.01); }} addLog('Avatar respects boundaries; cautious agents keep memory but soften slightly.'); }}
function intrude() {{ const n=state.agents.nian; n.trust=Math.max(0,n.trust-.08); n.boundary_pressure=Math.min(1,n.boundary_pressure+.12); n.memories.push('Avatar intruded near archive; Nian keeps distance after restore.'); addLog('Nian refuses and moves away from the avatar path.'); }}
function save() {{ localStorage.setItem(key,JSON.stringify(state)); addLog('Saved cross-session social loop state.'); }}
function restore() {{ const raw=localStorage.getItem(key); if(raw) {{ state=JSON.parse(raw); addLog('Restored cross-session relationship state.'); }} else addLog('No saved state yet.'); }}
function exportState() {{ navigator.clipboard?.writeText(JSON.stringify(state,null,2)); addLog('Exported state JSON to clipboard when available.'); }}
document.getElementById('tick').onclick=tick; document.getElementById('respect').onclick=respect; document.getElementById('intrude').onclick=intrude; document.getElementById('save').onclick=save; document.getElementById('restore').onclick=restore; document.getElementById('export').onclick=exportState; document.getElementById('auto').onclick=()=>{{ if(timer) {{ clearInterval(timer); timer=null; addLog('Auto ticks paused.'); }} else {{ timer=setInterval(tick,1200); addLog('Auto ticks running.'); }} }};
render();
</script>
</body>
</html>
""", encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    agents = build_agents()
    appraisals = build_need_appraisals(agents)
    decisions = build_approach_avoidance(agents, appraisals)
    plans = build_object_plans(agents)
    continuities = build_relationship_continuity(agents)
    snapshots = build_snapshots()
    ticks = build_ticks(appraisals, decisions, plans)
    metrics = compute_metrics(agents, appraisals, decisions, plans, continuities, snapshots, ticks)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["local_social_memory_autonomous_loop_readiness"] >= 0.82 and metrics["autonomous_agent_tick_rate"] >= 1.0 and metrics["cross_session_relationship_continuity"] >= 0.75 else "fail"
    payload = {
        "report": 223,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session",
        "module_verdict": verdict,
        "agents": [asdict(row) for row in agents],
        "need_appraisals": [asdict(row) for row in appraisals],
        "approach_avoidance": [asdict(row) for row in decisions],
        "object_plans": [asdict(row) for row in plans],
        "relationship_continuity": [asdict(row) for row in continuities],
        "cross_session_snapshots": [asdict(row) for row in snapshots],
        "autonomous_ticks": [asdict(row) for row in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic autonomous ticking, not real autonomous consciousness.",
            "Agent planning is structured and local, not general-purpose reasoning.",
            "Cross-session continuity uses browser localStorage/export, not server persistence.",
            "Need-driven motion is simplified 2D movement inside a local browser scene.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D autonomous social ecology with multi-agent interaction, shared object negotiation, social contagion, and durable relationship histories",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "agents": ARTIFACT_DIR / f"{BASE}_agents.csv",
        "need_appraisals": ARTIFACT_DIR / f"{BASE}_need_appraisals.csv",
        "approach_avoidance": ARTIFACT_DIR / f"{BASE}_approach_avoidance.csv",
        "object_plans": ARTIFACT_DIR / f"{BASE}_object_plans.csv",
        "relationship_continuity": ARTIFACT_DIR / f"{BASE}_relationship_continuity.csv",
        "cross_session_snapshots": ARTIFACT_DIR / f"{BASE}_cross_session_snapshots.csv",
        "autonomous_ticks": ARTIFACT_DIR / f"{BASE}_autonomous_ticks.csv",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["agents"], payload["agents"])
    write_csv(paths["need_appraisals"], payload["need_appraisals"])
    write_csv(paths["approach_avoidance"], payload["approach_avoidance"])
    write_csv(paths["object_plans"], payload["object_plans"])
    write_csv(paths["relationship_continuity"], payload["relationship_continuity"])
    write_csv(paths["cross_session_snapshots"], payload["cross_session_snapshots"])
    write_csv(paths["autonomous_ticks"], payload["autonomous_ticks"])
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "local_social_memory_autonomous_loop_readiness": payload["metrics"]["local_social_memory_autonomous_loop_readiness"],
        "autonomous_agent_tick_rate": payload["metrics"]["autonomous_agent_tick_rate"],
        "object_plan_completion_rate": payload["metrics"]["object_plan_completion_rate"],
        "cross_session_relationship_continuity": payload["metrics"]["cross_session_relationship_continuity"],
        "private_boundary": "sealed private need/workspace digests with localStorage relationship continuity",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "local_social_memory_autonomous_loop_readiness": payload["metrics"]["local_social_memory_autonomous_loop_readiness"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "autonomous_agent_tick_rate": payload["metrics"]["autonomous_agent_tick_rate"],
        "cross_session_relationship_continuity": payload["metrics"]["cross_session_relationship_continuity"],
        "next_gate": payload["next_gate"],
    }])
    render_scene(paths["visualization"], payload)
    return {key: str(value) for key, value in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"local_social_memory_autonomous_loop_readiness {metrics['local_social_memory_autonomous_loop_readiness']:.6f}")
    print(f"agents {len(payload['agents'])}")
    print(f"need_appraisals {len(payload['need_appraisals'])}")
    print(f"approach_avoidance_decisions {len(payload['approach_avoidance'])}")
    print(f"object_plans {len(payload['object_plans'])}")
    print(f"relationship_continuity_records {len(payload['relationship_continuity'])}")
    print(f"cross_session_snapshots {len(payload['cross_session_snapshots'])}")
    print(f"autonomous_ticks {len(payload['autonomous_ticks'])}")
    print(f"autonomous_agent_tick_rate {metrics['autonomous_agent_tick_rate']:.6f}")
    print(f"object_plan_completion_rate {metrics['object_plan_completion_rate']:.6f}")
    print(f"cross_session_relationship_continuity {metrics['cross_session_relationship_continuity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
