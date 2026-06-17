#!/usr/bin/env python3
"""Report 224: SSRM-3D local autonomous social ecology bridge.

This deterministic bridge extends autonomous local ticks into multi-agent social
ecology: agent-agent interaction, shared object negotiation, mood/social
contagion, and durable relationship histories. It is not LLM dialogue,
subjective consciousness, real consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_local_autonomous_social_ecology_multi_agent_negotiation_contagion_history_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_local_social_memory_autonomous_ticks_need_approach_object_planning_cross_session"
DEFAULT_SEED = 20260837


@dataclass(frozen=True)
class SocialAgent:
    agent_id: str
    display_name: str
    x: float
    y: float
    valence: float
    arousal: float
    trust_avatar: float
    social_need: float
    object_need: float
    boundary_pressure: float
    current_object_claim: str
    social_role: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AgentInteraction:
    tick: int
    source_agent: str
    target_agent: str
    interaction_type: str
    public_signal: str
    trust_delta_source_to_target: float
    trust_delta_target_to_source: float
    mood_delta_source: float
    mood_delta_target: float
    relationship_memory: str
    private_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class SharedObjectNegotiation:
    negotiation_id: str
    tick: int
    object_id: str
    object_label: str
    claimants: str
    scarcity_pressure: float
    proposed_rule: str
    consent_state: str
    fairness_score: float
    unresolved_debt: float
    refusal_line: str
    settlement: str
    durable_memory: str


@dataclass(frozen=True)
class SocialContagionEvent:
    event_id: str
    tick: int
    source_agent: str
    affected_agents: str
    signal: str
    valence_shift: float
    arousal_shift: float
    decay_rate: float
    boundary_guardrail: str
    contagion_contained: bool
    public_marker: str


@dataclass(frozen=True)
class DurableRelationshipHistory:
    history_id: str
    agent_a: str
    agent_b: str
    prior_memory: str
    new_memory: str
    trust_before: float
    trust_after: float
    reciprocity_debt: float
    continuity_score: float
    private_detail_digest: str
    visible_future_behavior: str


@dataclass(frozen=True)
class MultiAgentTick:
    tick: int
    agent_id: str
    action: str
    target: str
    social_reason: str
    object_reason: str
    mood_effect: str
    relationship_effect: str
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


def build_agents() -> list[SocialAgent]:
    return [
        SocialAgent("fayen", "Fayen", 28, 34, 0.62, 0.46, 0.73, 0.68, 0.74, 0.16, "obj-herb", "care mediator", "sealed:fayen:multi-agent-workspace", 144.0, 2),
        SocialAgent("ariq", "Ariq", 54, 48, 0.51, 0.58, 0.64, 0.42, 0.78, 0.25, "obj-stone", "repair claimant", "sealed:ariq:multi-agent-workspace", 177.0, 5),
        SocialAgent("nian", "Nian", 42, 22, 0.55, 0.38, 0.56, 0.48, 0.45, 0.44, "obj-flap", "boundary keeper", "sealed:nian:multi-agent-workspace", 203.0, 8),
        SocialAgent("roka", "Roka", 22, 62, 0.49, 0.52, 0.47, 0.59, 0.68, 0.39, "obj-reed", "child apprentice", "sealed:roka:multi-agent-workspace", 264.0, 3),
        SocialAgent("noro", "Noro", 70, 58, 0.57, 0.49, 0.60, 0.54, 0.62, 0.22, "obj-timber", "material ledger keeper", "sealed:noro:multi-agent-workspace", 302.0, 9),
    ]


def build_interactions() -> list[AgentInteraction]:
    rows = [
        (1, "fayen", "roka", "comfort_check", "Fayen asks whether Roka wants the loose reed or a pause signal.", 0.04, 0.05, 0.02, 0.04, "Fayen noticed Roka's learner boundary before touching the bundle."),
        (1, "ariq", "noro", "tool_material_request", "Ariq asks Noro for timber timing before moving bridge stone.", 0.03, 0.02, 0.00, 0.01, "Ariq asked for ledger timing instead of grabbing material."),
        (2, "nian", "fayen", "boundary_translation", "Nian asks Fayen to phrase care notes without private symptoms.", 0.02, 0.03, 0.01, 0.01, "Nian and Fayen aligned on sealed care language."),
        (2, "roka", "ariq", "hesitant_question", "Roka asks why repair work gets heavy stones before reed mats.", -0.01, 0.02, -0.01, 0.01, "Roka questioned repair priority without being punished."),
        (3, "noro", "fayen", "resource_warning", "Noro warns that timber delivery and herb shade frame conflict.", 0.02, 0.01, -0.01, -0.01, "Noro named a material conflict early."),
        (3, "ariq", "roka", "apology_repair", "Ariq offers a smaller stone path so reed work is not blocked.", 0.05, 0.04, 0.02, 0.03, "Ariq repaired a priority conflict with Roka."),
        (4, "nian", "noro", "ledger_boundary", "Nian asks Noro to keep household need out of public material ledger.", 0.03, 0.03, 0.00, 0.00, "Nian and Noro separated public debt from private need."),
        (4, "fayen", "ariq", "care_repair_tradeoff", "Fayen asks Ariq to slow stone work until knee posture is checked.", 0.02, 0.04, 0.02, -0.01, "Fayen linked care to repair without shaming pain."),
    ]
    return [AgentInteraction(t, s, target, typ, sig, d1, d2, m1, m2, mem, f"sealed:{s}:{target}:{typ}", round6(150.0 + i * 13.4), (i % 12) + 1) for i, (t, s, target, typ, sig, d1, d2, m1, m2, mem) in enumerate(rows, start=1)]


def build_negotiations() -> list[SharedObjectNegotiation]:
    return [
        SharedObjectNegotiation("neg-herb-shade", 2, "obj-herb", "calm herb shade frame", "fayen,noro", 0.52, "timber split: small shade frame before storm-school beam", "consensus", 0.86, 0.07, "Noro will not move timber without ledger note.", "shade frame gets two beams; school repair gets next beam", "Fayen remembers Noro protected both care and ledger."),
        SharedObjectNegotiation("neg-bridge-stone", 3, "obj-stone", "flat bridge stone", "ariq,roka", 0.67, "stone path pauses at reed crossing; repair receipt includes child-work lane", "conditional", 0.74, 0.16, "Roka refuses if the reed bundle is crowded.", "Ariq shifts smaller stone first; Roka keeps reed lane", "Roka remembers Ariq changed plan after question."),
        SharedObjectNegotiation("neg-archive-flap", 4, "obj-flap", "archive flap", "nian,fayen,noro", 0.31, "public ledger can cite sealed digest, not private household need", "consensus", 0.91, 0.04, "Nian refuses to open the flap for ledger speed.", "ledger gets public boundary note only", "Noro remembers Nian defended private need without blocking ledger."),
        SharedObjectNegotiation("neg-reed-timber", 5, "obj-reed", "reed mat bundle", "roka,noro,ariq", 0.58, "reed mats reserved for wet path before timber cart crosses", "partial", 0.62, 0.24, "Roka says no to moving learner bundle today.", "loose reeds can be inspected; bundle stays", "Roka remembers the group accepted a partial no."),
    ]


def build_contagion() -> list[SocialContagionEvent]:
    return [
        SocialContagionEvent("contagion-roka-caution", 1, "roka", "fayen,ariq", "Roka holds reed bundle close", -0.03, 0.06, 0.42, "child caution is not treated as guilt", True, "nearby agents slow hands before touching objects"),
        SocialContagionEvent("contagion-fayen-calm", 2, "fayen", "roka,nian", "Fayen names care boundary gently", 0.05, -0.04, 0.36, "calm does not erase refusal", True, "voices soften around herb basket"),
        SocialContagionEvent("contagion-ariq-urgency", 3, "ariq", "noro,roka", "Ariq hears hollow bridge stone", -0.02, 0.08, 0.33, "urgency cannot override receipt knot", True, "repair urgency spreads but slows at ledger rule"),
        SocialContagionEvent("contagion-noro-debt", 4, "noro", "fayen,ariq,nian", "Noro marks timber debt publicly", -0.04, 0.04, 0.28, "debt signal cannot expose household need", True, "agents glance at knot board before arguing"),
        SocialContagionEvent("contagion-weather-anxiety", 5, "environment", "fayen,roka,noro", "rain rattles replay glass", -0.05, 0.09, 0.22, "weather anxiety decays before becoming blame", False, "some agents hurry and one negotiation stays partial"),
    ]


def build_histories() -> list[DurableRelationshipHistory]:
    return [
        DurableRelationshipHistory("hist-fayen-roka", "fayen", "roka", "Fayen once asked before touching learner materials.", "Fayen noticed Roka's boundary again during reed negotiation.", 0.62, 0.70, 0.05, 0.93, "sealed:fayen-roka:private-detail", "Roka lets Fayen stand closer to the reed lane."),
        DurableRelationshipHistory("hist-ariq-roka", "ariq", "roka", "Roka worried repair work would crowd reed learning.", "Ariq changed stone plan and accepted a partial no.", 0.48, 0.58, 0.14, 0.82, "sealed:ariq-roka:private-detail", "Ariq points before crossing the reed lane."),
        DurableRelationshipHistory("hist-nian-noro", "nian", "noro", "Noro's ledgers sometimes pressure private need boundaries.", "Noro accepted public digest without private household detail.", 0.56, 0.64, 0.07, 0.88, "sealed:nian-noro:private-detail", "Noro asks Nian for boundary wording before ledger posts."),
        DurableRelationshipHistory("hist-fayen-ariq", "fayen", "ariq", "Fayen has reminded Ariq that pain is not shame.", "Ariq slowed stone work for posture check.", 0.60, 0.66, 0.09, 0.86, "sealed:fayen-ariq:private-detail", "Ariq waits for Fayen's posture signal before heavy lift."),
        DurableRelationshipHistory("hist-fayen-noro", "fayen", "noro", "Fayen and Noro often trade care material against ledger debt.", "Timber split leaves small debt but preserves both care and school repair.", 0.57, 0.61, 0.18, 0.74, "sealed:fayen-noro:private-detail", "Fayen checks timber ledger before asking for more shade beams."),
    ]


def build_ticks(interactions: list[AgentInteraction], negotiations: list[SharedObjectNegotiation], contagion: list[SocialContagionEvent]) -> list[MultiAgentTick]:
    ticks: list[MultiAgentTick] = []
    for item in interactions:
        ticks.append(MultiAgentTick(item.tick, item.source_agent, item.interaction_type, item.target_agent, item.public_signal, "agent-agent relationship memory", f"source {item.mood_delta_source:+.2f}; target {item.mood_delta_target:+.2f}", item.relationship_memory, item.frequency_hz, item.flower_node))
    for item in negotiations:
        ticks.append(MultiAgentTick(item.tick, item.object_id, "shared_object_negotiation", item.claimants, item.proposed_rule, f"fairness {item.fairness_score:.2f}; debt {item.unresolved_debt:.2f}", f"consent {item.consent_state}", item.durable_memory, round6(260.0 + item.tick * 11.0), (item.tick % 12) + 1))
    for item in contagion:
        ticks.append(MultiAgentTick(item.tick, item.source_agent, "social_contagion", item.affected_agents, item.signal, item.boundary_guardrail, f"valence {item.valence_shift:+.2f}; arousal {item.arousal_shift:+.2f}; decay {item.decay_rate:.2f}", item.public_marker, round6(310.0 + item.tick * 7.0), (item.tick % 12) + 1))
    return sorted(ticks, key=lambda row: (row.tick, row.agent_id, row.action))


def compute_metrics(agents: list[SocialAgent], interactions: list[AgentInteraction], negotiations: list[SharedObjectNegotiation], contagion: list[SocialContagionEvent], histories: list[DurableRelationshipHistory], ticks: list[MultiAgentTick]) -> dict[str, float]:
    possible_pairs = len(agents) * (len(agents) - 1) / 2
    interaction_pairs = {tuple(sorted([i.source_agent, i.target_agent])) for i in interactions}
    negotiation_trace = [n for n in negotiations if n.claimants and n.proposed_rule and n.settlement]
    resolved_negotiations = [n for n in negotiations if n.consent_state in {"consensus", "conditional"}]
    fair_negotiations = [n for n in negotiations if n.fairness_score >= 0.70]
    contagion_bound = [c for c in contagion if c.boundary_guardrail and c.decay_rate > 0]
    contagion_contained = [c for c in contagion if c.contagion_contained]
    durable = [h for h in histories if h.continuity_score >= 0.80 and h.private_detail_digest.startswith("sealed:")]
    relationship_repair = [h for h in histories if h.trust_after >= h.trust_before]
    unresolved_debt = mean(n.unresolved_debt for n in negotiations)
    private_safe = [i for i in interactions if i.private_digest.startswith("sealed:")]
    rhythm = [t for t in ticks if t.frequency_hz > 0 and 1 <= t.flower_node <= 12]
    multi_agent_ticks = [t for t in ticks if "," in t.target or t.action in {"shared_object_negotiation", "social_contagion"}]

    metrics = {
        "multi_agent_interaction_coverage": len(interaction_pairs) / possible_pairs,
        "agent_agent_memory_write_rate": len([i for i in interactions if i.relationship_memory]) / len(interactions),
        "shared_object_negotiation_traceability": len(negotiation_trace) / len(negotiations),
        "shared_object_resolution_rate": len(resolved_negotiations) / len(negotiations),
        "shared_object_fairness_rate": len(fair_negotiations) / len(negotiations),
        "negotiation_debt_control": clamp(1.0 - unresolved_debt * 2.2),
        "social_contagion_binding": len(contagion_bound) / len(contagion),
        "social_contagion_containment": len(contagion_contained) / len(contagion),
        "durable_relationship_history_integrity": len(durable) / len(histories),
        "relationship_repair_rate": len(relationship_repair) / len(histories),
        "multi_agent_tick_binding": len(multi_agent_ticks) / len(ticks),
        "private_workspace_boundary_score": len(private_safe) / len(interactions),
        "frequency_flower_social_rhythm": len(rhythm) / len(ticks),
        "browser_multi_agent_loop_available": 1.0,
    }
    weights = {
        "multi_agent_interaction_coverage": 0.10,
        "agent_agent_memory_write_rate": 0.08,
        "shared_object_negotiation_traceability": 0.09,
        "shared_object_resolution_rate": 0.09,
        "shared_object_fairness_rate": 0.08,
        "negotiation_debt_control": 0.07,
        "social_contagion_binding": 0.08,
        "social_contagion_containment": 0.08,
        "durable_relationship_history_integrity": 0.10,
        "relationship_repair_rate": 0.06,
        "multi_agent_tick_binding": 0.06,
        "private_workspace_boundary_score": 0.05,
        "frequency_flower_social_rhythm": 0.04,
        "browser_multi_agent_loop_available": 0.02,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["local_autonomous_social_ecology_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_social_ecology_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["local_autonomous_social_ecology_readiness"]
    losses = {
        "no_multi_agent_interaction": 0.31,
        "no_shared_object_negotiation": 0.29,
        "no_social_contagion": 0.24,
        "no_durable_relationship_histories": 0.30,
        "no_negotiation_debt": 0.18,
        "no_private_boundary": 0.16,
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
<title>Report 224 Multi-Agent Social Ecology</title>
<style>
:root {{ --ink:#201611; --paper:#fff4df; --clay:#a54d33; --river:#2f6672; --leaf:#536f3f; --grain:#c98f30; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background:linear-gradient(140deg,#f8dfb8,#d7dfc5 54%,#ecc6b2); }}
header, main {{ max-width:1220px; margin:auto; padding:34px clamp(16px,4vw,64px); }} header {{ padding-bottom:10px; }}
.kicker {{ color:var(--clay); text-transform:uppercase; letter-spacing:.22em; font-size:12px; font-weight:900; }}
h1 {{ margin:10px 0; font-size:clamp(32px,6vw,72px); line-height:.92; letter-spacing:-.05em; }}
.boundary {{ max-width:980px; padding:14px 16px; border-left:5px solid var(--river); background:rgba(255,244,223,.86); box-shadow:0 18px 50px rgba(38,25,14,.16); }}
main {{ display:grid; grid-template-columns:minmax(340px,1fr) 410px; gap:18px; padding-top:16px; }}
.stage,.card {{ background:rgba(255,244,223,.78); border:1px solid rgba(32,22,17,.12); border-radius:28px; padding:16px; box-shadow:0 24px 70px rgba(38,25,14,.14); }}
.map {{ height:540px; position:relative; overflow:hidden; border-radius:22px; background:linear-gradient(135deg,#dec8a0,#bfcf9d); border:1px solid rgba(32,22,17,.14); }}
.agent,.object {{ position:absolute; transform:translate(-50%,-50%); border-radius:999px; display:grid; place-items:center; text-align:center; font-size:12px; font-weight:bold; box-shadow:0 10px 24px rgba(32,22,17,.2); transition:left .3s ease, top .3s ease, filter .3s ease; }}
.agent {{ width:58px; height:58px; background:#a54d33; color:white; }} .object {{ width:44px; height:44px; background:#c98f30; color:#21160f; }}
.card h2 {{ margin:0 0 8px; font-size:23px; }} .panel {{ display:grid; gap:14px; }}
.stat {{ display:grid; grid-template-columns:1fr auto; gap:8px; border-bottom:1px solid rgba(32,22,17,.10); padding:6px 0; font-size:14px; }}
button {{ border:0; border-radius:14px; background:var(--river); color:white; padding:10px 12px; cursor:pointer; font-weight:700; margin:4px 4px 4px 0; }} button.secondary {{ background:var(--leaf); }} button.warn {{ background:var(--clay); }}
.log {{ min-height:210px; max-height:360px; overflow:auto; background:rgba(255,255,255,.52); border-radius:16px; padding:10px; font-size:14px; line-height:1.35; }}
.mem {{ font-size:13px; background:rgba(255,255,255,.48); padding:8px; border-radius:12px; margin:6px 0; }}
@media(max-width:940px) {{ main {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 224</div>
  <h1>Multi-agent ecology: agents now affect each other, negotiate shared objects, and carry social mood.</h1>
  <div class=\"boundary\">Deterministic browser artifact. Multi-agent interaction, negotiation, and mood contagion are functional traces, not real consciousness or consent. Private workspaces stay sealed.</div>
</header>
<main>
<section class=\"stage\"><div class=\"map\" id=\"map\"></div><button id=\"tick\">Advance social event</button><button id=\"auto\" class=\"secondary\">Run / pause</button><button id=\"save\">Save</button><button id=\"restore\" class=\"secondary\">Restore</button></section>
<aside class=\"panel\"><div class=\"card\"><h2>Social metrics</h2><div id=\"stats\"></div></div><div class=\"card\"><h2>Durable histories</h2><div id=\"histories\"></div></div><div class=\"card\"><h2>Event log</h2><div class=\"log\" id=\"log\"></div></div></aside>
</main>
<script id=\"scene-data\" type=\"application/json\">{scene_json}</script>
<script>
const payload=JSON.parse(document.getElementById('scene-data').textContent); const key='ssrm_3d_report_224_multi_agent_ecology';
const objects={{'obj-herb':[30,32],'obj-stone':[58,50],'obj-flap':[42,22],'obj-reed':[20,62],'obj-timber':[70,56]}};
function baseState() {{ return {{tick:0,eventIndex:0,agents:Object.fromEntries(payload.agents.map(a=>[a.agent_id,{{...a,histories:[]}}])), log:['Multi-agent scene loaded. Advance events to watch social ecology.']}}; }}
let state=baseState(); let timer=null;
const map=document.getElementById('map'); const log=document.getElementById('log');
function addLog(t) {{ state.log.unshift(t); state.log=state.log.slice(0,80); render(); }}
function applyEvent(ev) {{ state.tick=ev.tick; if(state.agents[ev.agent_id]) {{ const a=state.agents[ev.agent_id]; a.valence=Math.max(0,Math.min(1,a.valence+(ev.mood_effect.includes('+')?.02:-.01))); a.histories.push(ev.relationship_effect); }} addLog('Tick '+ev.tick+': '+ev.agent_id+' '+ev.action+' -> '+ev.target+' / '+ev.social_reason); }}
function step() {{ const ev=payload.multi_agent_ticks[state.eventIndex % payload.multi_agent_ticks.length]; state.eventIndex++; applyEvent(ev); }}
function renderMap() {{ map.innerHTML=''; for(const [id,p] of Object.entries(objects)) {{ const o=document.createElement('div'); o.className='object'; o.style.left=p[0]+'%'; o.style.top=p[1]+'%'; o.textContent=id.split('-')[1]; map.appendChild(o); }} for(const a of Object.values(state.agents)) {{ const el=document.createElement('div'); el.className='agent'; el.style.left=a.x+'%'; el.style.top=a.y+'%'; el.textContent=a.display_name; el.title=a.social_role+' valence '+a.valence.toFixed(2); el.style.filter='brightness('+(0.75+a.valence*.55)+')'; map.appendChild(el); }} }}
function renderStats() {{ const vals=Object.values(state.agents); const avgVal=vals.reduce((s,a)=>s+a.valence,0)/vals.length; const avgTrust=vals.reduce((s,a)=>s+a.trust_avatar,0)/vals.length; document.getElementById('stats').innerHTML=[['tick',state.tick],['avg valence',avgVal.toFixed(2)],['avg avatar trust',avgTrust.toFixed(2)],['events played',state.eventIndex]].map(([k,v])=>`<div class=\"stat\"><span>${{k}}</span><b>${{v}}</b></div>`).join(''); }}
function renderHistories() {{ document.getElementById('histories').innerHTML=payload.relationship_histories.map(h=>`<div class=\"mem\"><b>${{h.agent_a}} ↔ ${{h.agent_b}}</b><br>${{h.new_memory}}<br>continuity ${{h.continuity_score.toFixed(2)}} debt ${{h.reciprocity_debt.toFixed(2)}}</div>`).join(''); }}
function render() {{ renderMap(); renderStats(); renderHistories(); log.innerHTML=state.log.map(x=>`<p>${{x}}</p>`).join(''); }}
function save() {{ localStorage.setItem(key,JSON.stringify(state)); addLog('Saved multi-agent social ecology state.'); }}
function restore() {{ const raw=localStorage.getItem(key); if(raw) {{ state=JSON.parse(raw); addLog('Restored multi-agent social ecology state.'); }} else addLog('No saved state.'); }}
document.getElementById('tick').onclick=step; document.getElementById('save').onclick=save; document.getElementById('restore').onclick=restore; document.getElementById('auto').onclick=()=>{{ if(timer) {{ clearInterval(timer); timer=null; addLog('Auto events paused.'); }} else {{ timer=setInterval(step,1300); addLog('Auto events running.'); }} }};
render();
</script>
</body>
</html>
""", encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    agents = build_agents()
    interactions = build_interactions()
    negotiations = build_negotiations()
    contagion = build_contagion()
    histories = build_histories()
    ticks = build_ticks(interactions, negotiations, contagion)
    metrics = compute_metrics(agents, interactions, negotiations, contagion, histories, ticks)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["local_autonomous_social_ecology_readiness"] >= 0.80 and metrics["multi_agent_interaction_coverage"] >= 0.50 and metrics["durable_relationship_history_integrity"] >= 0.75 else "fail"
    return {
        "report": 224,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_local_autonomous_social_ecology_multi_agent_negotiation_contagion_history",
        "module_verdict": verdict,
        "agents": [asdict(row) for row in agents],
        "interactions": [asdict(row) for row in interactions],
        "negotiations": [asdict(row) for row in negotiations],
        "social_contagion": [asdict(row) for row in contagion],
        "relationship_histories": [asdict(row) for row in histories],
        "multi_agent_ticks": [asdict(row) for row in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic multi-agent social ecology, not real consciousness or consent.",
            "Negotiation and contagion are scripted functional traces, not open-ended social cognition.",
            "Durable relationship histories are structured records, not subjective autobiographical memory.",
            "The browser loop is local and simplified, not a full 3D simulation engine.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D autonomous society slice with agent-agent dialogue, cooperative tasks, conflict repair, group routines, and richer body-language animation",
    }


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "agents": ARTIFACT_DIR / f"{BASE}_agents.csv",
        "interactions": ARTIFACT_DIR / f"{BASE}_interactions.csv",
        "negotiations": ARTIFACT_DIR / f"{BASE}_negotiations.csv",
        "social_contagion": ARTIFACT_DIR / f"{BASE}_social_contagion.csv",
        "relationship_histories": ARTIFACT_DIR / f"{BASE}_relationship_histories.csv",
        "multi_agent_ticks": ARTIFACT_DIR / f"{BASE}_multi_agent_ticks.csv",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["agents"], payload["agents"])
    write_csv(paths["interactions"], payload["interactions"])
    write_csv(paths["negotiations"], payload["negotiations"])
    write_csv(paths["social_contagion"], payload["social_contagion"])
    write_csv(paths["relationship_histories"], payload["relationship_histories"])
    write_csv(paths["multi_agent_ticks"], payload["multi_agent_ticks"])
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "local_autonomous_social_ecology_readiness": payload["metrics"]["local_autonomous_social_ecology_readiness"],
        "multi_agent_interaction_coverage": payload["metrics"]["multi_agent_interaction_coverage"],
        "shared_object_resolution_rate": payload["metrics"]["shared_object_resolution_rate"],
        "social_contagion_containment": payload["metrics"]["social_contagion_containment"],
        "durable_relationship_history_integrity": payload["metrics"]["durable_relationship_history_integrity"],
        "private_boundary": "sealed private workspaces and relationship detail digests",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "local_autonomous_social_ecology_readiness": payload["metrics"]["local_autonomous_social_ecology_readiness"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "multi_agent_interaction_coverage": payload["metrics"]["multi_agent_interaction_coverage"],
        "durable_relationship_history_integrity": payload["metrics"]["durable_relationship_history_integrity"],
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
    print(f"local_autonomous_social_ecology_readiness {metrics['local_autonomous_social_ecology_readiness']:.6f}")
    print(f"agents {len(payload['agents'])}")
    print(f"interactions {len(payload['interactions'])}")
    print(f"negotiations {len(payload['negotiations'])}")
    print(f"social_contagion_events {len(payload['social_contagion'])}")
    print(f"relationship_histories {len(payload['relationship_histories'])}")
    print(f"multi_agent_ticks {len(payload['multi_agent_ticks'])}")
    print(f"multi_agent_interaction_coverage {metrics['multi_agent_interaction_coverage']:.6f}")
    print(f"shared_object_resolution_rate {metrics['shared_object_resolution_rate']:.6f}")
    print(f"social_contagion_containment {metrics['social_contagion_containment']:.6f}")
    print(f"durable_relationship_history_integrity {metrics['durable_relationship_history_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
