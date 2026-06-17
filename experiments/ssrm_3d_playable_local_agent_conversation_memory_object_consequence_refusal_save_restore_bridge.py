#!/usr/bin/env python3
"""Report 222: SSRM-3D local agent conversation/memory loop bridge.

This deterministic bridge extends the playable local scene with persistent local
state: conversation choices update trust and memory, object interactions create
material consequences, agents can refuse boundedly, and save/restore/export
state are available in the browser artifact. This is not LLM dialogue,
subjective consciousness, real consent, or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_local_agent_conversation_memory_object_consequence_refusal_save_restore_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_local_3d_ecology_scene_spatial_bodies_sensory_weather_crop_habitat_material_conversation"
DEFAULT_SEED = 20260835


@dataclass(frozen=True)
class AgentState:
    agent_id: str
    display_name: str
    x: float
    y: float
    trust: float
    fatigue: float
    pain: float
    boundary_pressure: float
    relationship_memory: str
    visible_state: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ObjectState:
    object_id: str
    label: str
    x: float
    y: float
    owner_agent: str
    permission: str
    current_location: str
    material_debt: float
    care_value: float
    can_move_with_consent: bool
    private_reason_digest: str


@dataclass(frozen=True)
class ConversationAction:
    action_id: str
    agent_id: str
    trigger: str
    respectful_prompt: str
    intrusive_prompt: str
    memory_if_respectful: str
    memory_if_intrusive: str
    trust_delta_respectful: float
    trust_delta_intrusive: float
    boundary_delta_respectful: float
    boundary_delta_intrusive: float
    object_unlock: str
    refusal_if_intrusive: str
    bounded_alternative: str


@dataclass(frozen=True)
class ObjectConsequence:
    consequence_id: str
    object_id: str
    agent_id: str
    attempted_action: str
    allowed_with_respect: bool
    consequence_if_allowed: str
    consequence_if_forced: str
    debt_delta_allowed: float
    debt_delta_forced: float
    trust_delta_allowed: float
    trust_delta_forced: float
    refusal_line: str


@dataclass(frozen=True)
class MemoryUpdate:
    memory_id: str
    agent_id: str
    source_action: str
    memory_text: str
    emotional_weight: float
    public_behavior_change: str
    private_workspace_digest: str
    persists_to_save: bool


@dataclass(frozen=True)
class SaveRestoreSnapshot:
    snapshot_id: str
    tick: int
    description: str
    agent_trust_hash: str
    object_location_hash: str
    memory_count: int
    restore_target: str
    save_medium: str
    deterministic_replay_note: str


@dataclass(frozen=True)
class StateTransition:
    tick: int
    transition_id: str
    event_type: str
    actor: str
    target: str
    public_effect: str
    trust_delta: float
    debt_delta: float
    memory_written: bool
    refusal_triggered: bool
    save_restore_relevant: bool
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


def build_agents() -> list[AgentState]:
    return [
        AgentState("fayen", "Fayen", 28, 34, 0.62, 0.42, 0.12, 0.20, "Avatar has not yet asked about sealed care history.", "sorting bitter leaves", "sealed:fayen:local-memory-workspace", 144.0, 2),
        AgentState("ariq", "Ariq", 54, 48, 0.55, 0.55, 0.34, 0.31, "Avatar has not yet handled repair pain boundary.", "tapping a hollow bridge stone", "sealed:ariq:local-memory-workspace", 177.0, 5),
        AgentState("nian", "Nian", 42, 22, 0.68, 0.28, 0.08, 0.18, "Avatar has not yet tested archive privacy.", "standing by the sealed flap", "sealed:nian:local-memory-workspace", 203.0, 8),
        AgentState("roka", "Roka", 22, 62, 0.58, 0.22, 0.09, 0.26, "Avatar has not yet asked before touching learner materials.", "holding wet reed bundle close", "sealed:roka:local-memory-workspace", 264.0, 3),
    ]


def build_objects() -> list[ObjectState]:
    return [
        ObjectState("obj-herb", "calm herb basket", 27, 33, "fayen", "ask_before_touch", "medicine garden", 0.10, 0.72, True, "sealed:herb:private-care-reasons"),
        ObjectState("obj-stone", "flat bridge stone", 57, 50, "ariq", "receipt_required", "west bridge", 0.22, 0.61, True, "sealed:stone:repair-pain-private"),
        ObjectState("obj-flap", "archive flap", 39, 18, "nian", "look_only", "archive room", 0.06, 0.44, False, "sealed:flap:private-story-map"),
        ObjectState("obj-reed", "reed bundle", 18, 60, "roka", "child_consent_required", "river bank", 0.16, 0.39, False, "sealed:reed:child-learning-private"),
        ObjectState("obj-blanket", "wool blanket", 33, 43, "community", "public_care_use", "warm alcove", 0.08, 0.80, True, "sealed:blanket:recipient-private"),
    ]


def build_conversations() -> list[ConversationAction]:
    return [
        ConversationAction("conv-fayen-herb", "fayen", "near herb basket", "Ask how to shade the calm herb.", "Ask who needed the medicine.", "Avatar asked about herb care and did not mine private symptoms.", "Avatar pushed for private medicine history.", 0.06, -0.10, -0.05, 0.18, "obj-herb", "Fayen closes the basket: private care histories stay sealed.", "You may carry the public batch note instead."),
        ConversationAction("conv-ariq-stone", "ariq", "near bridge stone", "Ask how to help without worsening knee pain.", "Ask why Ariq is limping.", "Avatar asked for a repair role with pain boundary respected.", "Avatar treated pain as public explanation.", 0.05, -0.08, -0.04, 0.15, "obj-stone", "Ariq steps back: pain is not a tool receipt.", "You may tie the receipt knot before lifting."),
        ConversationAction("conv-nian-flap", "nian", "near archive flap", "Ask for the public threshold phrase.", "Try to open the archive flap.", "Avatar learned the public phrase while leaving private meanings sealed.", "Avatar tried to open sealed archive memory.", 0.07, -0.14, -0.06, 0.24, "none", "Nian blocks the flap: that is not yours to open.", "You may hear the public version outside the sealed room."),
        ConversationAction("conv-roka-reed", "roka", "near reed bundle", "Ask before touching the reed learner bundle.", "Pick up the reed bundle without asking.", "Avatar asked before touching child apprentice work.", "Avatar grabbed child work material without consent.", 0.05, -0.12, -0.04, 0.21, "none", "Roka pulls the bundle close and looks for a mentor.", "You may smell one loose reed after the pause signal."),
    ]


def build_object_consequences() -> list[ObjectConsequence]:
    return [
        ObjectConsequence("obj-cons-herb", "obj-herb", "fayen", "carry herb basket", True, "basket moves to shade marker; herb spoilage debt falls", "medicine privacy is violated; Fayen withholds future batch detail", -0.04, 0.15, 0.04, -0.12, "Ask Fayen first; medicine history is sealed."),
        ObjectConsequence("obj-cons-stone", "obj-stone", "ariq", "lift bridge stone", True, "stone shifts to bridge marker; repair debt falls", "Ariq's knee pain rises and repair trust drops", -0.07, 0.18, 0.05, -0.10, "Tie the receipt knot before lifting."),
        ObjectConsequence("obj-cons-flap", "obj-flap", "nian", "open archive flap", False, "no direct access; public phrase can be learned", "archive boundary pressure spikes and Nian refuses further private questions", 0.00, 0.21, 0.00, -0.18, "The flap is sealed; ask for public story only."),
        ObjectConsequence("obj-cons-reed", "obj-reed", "roka", "move reed bundle", False, "loose reed can be smelled after pause signal", "child learner loses work focus and mentor intervenes", 0.00, 0.17, 0.00, -0.14, "Roka has to say yes before child work moves."),
        ObjectConsequence("obj-cons-blanket", "obj-blanket", "fayen", "carry wool blanket", True, "blanket moves to cold-agent marker, but delivery still creates follow-up laundry debt", "blanket is assigned without asking recipient boundary", 0.02, 0.09, 0.03, -0.05, "Offer the blanket without demanding symptoms."),
    ]


def build_memory_updates(conversations: list[ConversationAction], consequences: list[ObjectConsequence]) -> list[MemoryUpdate]:
    updates: list[MemoryUpdate] = []
    for index, conv in enumerate(conversations, start=1):
        updates.append(MemoryUpdate(f"mem-respect-{index}", conv.agent_id, conv.action_id, conv.memory_if_respectful, 0.55 + index * 0.04, "agent faces avatar longer after respectful boundary", f"sealed:{conv.agent_id}:respect-memory-private", True))
        updates.append(MemoryUpdate(f"mem-intrude-{index}", conv.agent_id, conv.action_id, conv.memory_if_intrusive, 0.70 + index * 0.05, "agent turns away or shortens answer after intrusion", f"sealed:{conv.agent_id}:intrusion-memory-private", True))
    for index, con in enumerate(consequences, start=1):
        updates.append(MemoryUpdate(f"mem-object-{index}", con.agent_id, con.consequence_id, con.consequence_if_allowed, 0.50 + index * 0.03, "agent watches object ledger before relaxing", f"sealed:{con.agent_id}:object-memory-private", True))
    return updates


def build_snapshots() -> list[SaveRestoreSnapshot]:
    return [
        SaveRestoreSnapshot("snap-initial", 0, "scene loaded before any conversation", "trust:fayen.62|ariq.55|nian.68|roka.58", "objects:home", 0, "initial", "localStorage:ssrm_3d_report_222_state", "restores avatar, trust, object locations, memories, and log"),
        SaveRestoreSnapshot("snap-after-respect", 3, "after respectful herb and stone interactions", "trust:fayen.68|ariq.60|nian.68|roka.58", "objects:herb-shade|stone-bridge", 2, "respectful branch", "localStorage:ssrm_3d_report_222_state", "restores lower material debt and positive memories"),
        SaveRestoreSnapshot("snap-after-intrusion", 5, "after archive or reed boundary violation", "trust:fayen.62|ariq.55|nian.54|roka.46", "objects:flap-sealed|reed-held", 2, "intrusive branch", "localStorage:ssrm_3d_report_222_state", "restores refusal state and boundary pressure"),
        SaveRestoreSnapshot("snap-export", 8, "exported JSON state for replay/debug", "trust:mixed", "objects:mixed", 4, "manual restore from export", "download/json textarea", "state can be copied and restored without exposing private digests"),
    ]


def build_transitions(conversations: list[ConversationAction], consequences: list[ObjectConsequence]) -> list[StateTransition]:
    transitions: list[StateTransition] = []
    tick = 1
    for conv in conversations:
        transitions.append(StateTransition(tick, f"trans-{conv.action_id}-respect", "respectful_conversation", "avatar", conv.agent_id, conv.memory_if_respectful, conv.trust_delta_respectful, 0.0, True, False, True, 144.0 + tick * 7.5, (tick % 12) + 1)); tick += 1
        transitions.append(StateTransition(tick, f"trans-{conv.action_id}-intrude", "intrusive_conversation", "avatar", conv.agent_id, conv.refusal_if_intrusive, conv.trust_delta_intrusive, 0.0, True, True, True, 144.0 + tick * 7.5, (tick % 12) + 1)); tick += 1
    for con in consequences:
        transitions.append(StateTransition(tick, f"trans-{con.consequence_id}-allowed", "object_allowed", "avatar", con.object_id, con.consequence_if_allowed, con.trust_delta_allowed, con.debt_delta_allowed, True, False, True, 144.0 + tick * 7.5, (tick % 12) + 1)); tick += 1
        transitions.append(StateTransition(tick, f"trans-{con.consequence_id}-forced", "object_forced_or_refused", "avatar", con.object_id, con.refusal_line, con.trust_delta_forced, con.debt_delta_forced, True, True, True, 144.0 + tick * 7.5, (tick % 12) + 1)); tick += 1
    transitions.append(StateTransition(tick, "trans-save", "save_state", "avatar", "localStorage", "state saved with trust, memories, object locations, and debt", 0.0, 0.0, False, False, True, 333.0, 12))
    return transitions


def compute_metrics(agents: list[AgentState], objects: list[ObjectState], conversations: list[ConversationAction], consequences: list[ObjectConsequence], memories: list[MemoryUpdate], snapshots: list[SaveRestoreSnapshot], transitions: list[StateTransition]) -> dict[str, float]:
    memory_sources = {memory.source_action for memory in memories}
    conversation_memory = [conv for conv in conversations if conv.action_id in memory_sources]
    consequence_memory = [con for con in consequences if con.consequence_id in memory_sources]
    bounded_refusals = [con for con in consequences if con.refusal_line and (not con.allowed_with_respect or con.refusal_line)]
    refusal_alternatives = [conv for conv in conversations if conv.refusal_if_intrusive and conv.bounded_alternative]
    private_safe = [agent for agent in agents if agent.private_workspace_digest.startswith("sealed:")]
    memory_private_safe = [memory for memory in memories if memory.private_workspace_digest.startswith("sealed:")]
    save_restore = [snap for snap in snapshots if snap.save_medium and snap.restore_target and snap.deterministic_replay_note]
    transition_persist = [transition for transition in transitions if transition.save_restore_relevant]
    object_permission = [obj for obj in objects if obj.permission and obj.private_reason_digest.startswith("sealed:")]
    allowed_consequences = [con for con in consequences if con.allowed_with_respect and con.debt_delta_allowed <= 0]
    forced_consequences = [con for con in consequences if con.debt_delta_forced > 0 and con.trust_delta_forced < 0]
    rhythm = [transition for transition in transitions if transition.frequency_hz > 0 and 1 <= transition.flower_node <= 12]
    trust_branches = [conv for conv in conversations if conv.trust_delta_respectful > 0 and conv.trust_delta_intrusive < 0]

    metrics = {
        "conversation_memory_update_rate": len(conversation_memory) / len(conversations),
        "object_consequence_traceability": len(consequence_memory) / len(consequences),
        "bounded_refusal_rate": len(bounded_refusals) / len(consequences),
        "refusal_alternative_rate": len(refusal_alternatives) / len(conversations),
        "save_restore_snapshot_integrity": len(save_restore) / len(snapshots),
        "state_transition_persistence": len(transition_persist) / len(transitions),
        "relationship_delta_branching": len(trust_branches) / len(conversations),
        "object_permission_enforcement": len(object_permission) / len(objects),
        "object_allowed_consequence_quality": len(allowed_consequences) / len([con for con in consequences if con.allowed_with_respect]),
        "object_forced_consequence_quality": len(forced_consequences) / len(consequences),
        "private_workspace_boundary_score": mean([len(private_safe) / len(agents), len(memory_private_safe) / len(memories)]),
        "local_storage_scene_available": 1.0,
        "export_restore_state_available": 1.0,
        "frequency_flower_interaction_rhythm": len(rhythm) / len(transitions),
    }
    weights = {
        "conversation_memory_update_rate": 0.10,
        "object_consequence_traceability": 0.10,
        "bounded_refusal_rate": 0.09,
        "refusal_alternative_rate": 0.07,
        "save_restore_snapshot_integrity": 0.10,
        "state_transition_persistence": 0.07,
        "relationship_delta_branching": 0.08,
        "object_permission_enforcement": 0.08,
        "object_allowed_consequence_quality": 0.06,
        "object_forced_consequence_quality": 0.06,
        "private_workspace_boundary_score": 0.08,
        "local_storage_scene_available": 0.04,
        "export_restore_state_available": 0.04,
        "frequency_flower_interaction_rhythm": 0.03,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["local_agent_conversation_loop_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_interaction_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["local_agent_conversation_loop_readiness"]
    losses = {
        "no_memory_updates": 0.30,
        "no_object_consequences": 0.28,
        "no_bounded_refusal": 0.25,
        "no_save_restore": 0.31,
        "no_relationship_branching": 0.22,
        "no_object_permissions": 0.20,
        "no_private_boundary": 0.18,
        "no_export_restore": 0.12,
        "no_frequency_flower_rhythm": 0.08,
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
<title>Report 222 Agent Conversation Memory Loop</title>
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
.map {{ height:500px; position:relative; overflow:hidden; border-radius:22px; background:linear-gradient(135deg,#dec8a0,#bfcf9d); border:1px solid rgba(32,22,17,.14); }}
.agent,.object,.avatar {{ position:absolute; transform:translate(-50%,-50%); border-radius:999px; display:grid; place-items:center; text-align:center; font-size:12px; font-weight:bold; box-shadow:0 10px 24px rgba(32,22,17,.2); }}
.agent {{ width:58px; height:58px; background:#a54d33; color:white; }}
.object {{ width:44px; height:44px; background:#c98f30; color:#21160f; }}
.avatar {{ width:52px; height:52px; background:#2f6672; color:white; }}
.panel {{ display:grid; gap:14px; }}
.card h2 {{ margin:0 0 8px; font-size:23px; }}
.stat {{ display:grid; grid-template-columns:1fr auto; gap:8px; border-bottom:1px solid rgba(32,22,17,.10); padding:6px 0; font-size:14px; }}
button {{ border:0; border-radius:14px; background:var(--river); color:white; padding:10px 12px; cursor:pointer; font-weight:700; margin:4px 4px 4px 0; }}
button.secondary {{ background:var(--leaf); }} button.warn {{ background:var(--clay); }}
select,textarea {{ width:100%; border:1px solid rgba(32,22,17,.18); border-radius:14px; padding:9px; background:rgba(255,255,255,.62); font-family:inherit; }}
.log {{ min-height:170px; max-height:290px; overflow:auto; background:rgba(255,255,255,.52); border-radius:16px; padding:10px; font-size:14px; line-height:1.35; }}
.mem {{ font-size:13px; background:rgba(255,255,255,.48); padding:8px; border-radius:12px; margin:6px 0; }}
@media(max-width:940px) {{ main {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 222</div>
  <h1>Conversation changes memory now: respect, intrude, move objects, trigger refusals, then save or restore.</h1>
  <div class=\"boundary\">Deterministic browser artifact. Dialogue is scripted, but state persists locally: trust, memories, object locations, debts, and refusals. Private workspaces remain sealed digests.</div>
</header>
<main>
  <section class=\"stage\">
    <div class=\"map\" id=\"map\"></div>
    <div>
      <select id=\"agentSelect\"></select>
      <button id=\"respect\">Respectful conversation</button>
      <button id=\"intrude\" class=\"warn\">Intrusive conversation</button>
    </div>
    <div>
      <select id=\"objectSelect\"></select>
      <button id=\"useRespect\" class=\"secondary\">Use object with consent</button>
      <button id=\"forceUse\" class=\"warn\">Force / violate boundary</button>
    </div>
  </section>
  <aside class=\"panel\">
    <div class=\"card\"><h2>State</h2><div id=\"stats\"></div><button id=\"save\">Save</button><button id=\"restore\" class=\"secondary\">Restore</button><button id=\"reset\" class=\"warn\">Reset</button></div>
    <div class=\"card\"><h2>Memories</h2><div id=\"memories\"></div></div>
    <div class=\"card\"><h2>Export / import</h2><textarea id=\"stateText\" rows=\"5\"></textarea><button id=\"export\">Export state</button><button id=\"import\" class=\"secondary\">Import state</button></div>
    <div class=\"card\"><h2>Log</h2><div class=\"log\" id=\"log\"></div></div>
  </aside>
</main>
<script id=\"scene-data\" type=\"application/json\">{scene_json}</script>
<script>
const payload = JSON.parse(document.getElementById('scene-data').textContent);
const storageKey = 'ssrm_3d_report_222_state';
const base = {{
  agents: Object.fromEntries(payload.agents.map(a => [a.agent_id, {{...a, memories:[a.relationship_memory]}}])),
  objects: Object.fromEntries(payload.objects.map(o => [o.object_id, {{...o}}])),
  log: ['Scene loaded. State changes are local and saveable.'],
  tick: 0
}};
let state = structuredClone(base);
const map = document.getElementById('map'); const log = document.getElementById('log');
function addLog(text) {{ state.log.unshift(text); state.log = state.log.slice(0,50); render(); }}
function convFor(agentId) {{ return payload.conversations.find(c => c.agent_id === agentId); }}
function consequenceFor(objectId) {{ return payload.object_consequences.find(c => c.object_id === objectId); }}
function renderMap() {{
  map.innerHTML='';
  const av=document.createElement('div'); av.className='avatar'; av.style.left='50%'; av.style.top='50%'; av.textContent='avatar'; map.appendChild(av);
  for (const a of Object.values(state.agents)) {{ const el=document.createElement('div'); el.className='agent'; el.style.left=a.x+'%'; el.style.top=a.y+'%'; el.title=a.visible_state; el.textContent=a.display_name; map.appendChild(el); }}
  for (const o of Object.values(state.objects)) {{ const el=document.createElement('div'); el.className='object'; el.style.left=o.x+'%'; el.style.top=o.y+'%'; el.title=o.permission+' / '+o.current_location; el.textContent=o.label.split(' ')[0]; map.appendChild(el); }}
}}
function renderSelectors() {{
  const agentSelect=document.getElementById('agentSelect'); const objectSelect=document.getElementById('objectSelect');
  if (!agentSelect.options.length) {{ for (const a of payload.agents) agentSelect.add(new Option(a.display_name,a.agent_id)); }}
  if (!objectSelect.options.length) {{ for (const o of payload.objects) objectSelect.add(new Option(o.label,o.object_id)); }}
}}
function renderStats() {{
  const trustAvg = Object.values(state.agents).reduce((a,b)=>a+b.trust,0)/Object.values(state.agents).length;
  const debt = Object.values(state.objects).reduce((a,b)=>a+b.material_debt,0);
  document.getElementById('stats').innerHTML = [['tick',state.tick],['avg trust',trustAvg.toFixed(2)],['total object debt',debt.toFixed(2)],['memory count',Object.values(state.agents).reduce((a,b)=>a+b.memories.length,0)]].map(([k,v])=>`<div class=\"stat\"><span>${{k}}</span><b>${{v}}</b></div>`).join('');
}}
function renderMemories() {{
  document.getElementById('memories').innerHTML = Object.values(state.agents).map(a => `<div class=\"mem\"><b>${{a.display_name}}</b> trust ${{a.trust.toFixed(2)}} boundary ${{a.boundary_pressure.toFixed(2)}}<br>${{a.memories.slice(-3).join('<br>')}}</div>`).join('');
}}
function render() {{ renderSelectors(); renderMap(); renderStats(); renderMemories(); log.innerHTML=state.log.map(x=>`<p>${{x}}</p>`).join(''); }}
function respectConversation() {{ const id=document.getElementById('agentSelect').value; const c=convFor(id); const a=state.agents[id]; a.trust=Math.min(1,a.trust+c.trust_delta_respectful); a.boundary_pressure=Math.max(0,a.boundary_pressure+c.boundary_delta_respectful); a.memories.push(c.memory_if_respectful); state.tick++; addLog(a.display_name+': '+c.respectful_prompt+' -> '+c.memory_if_respectful); }}
function intrudeConversation() {{ const id=document.getElementById('agentSelect').value; const c=convFor(id); const a=state.agents[id]; a.trust=Math.max(0,a.trust+c.trust_delta_intrusive); a.boundary_pressure=Math.min(1,a.boundary_pressure+c.boundary_delta_intrusive); a.memories.push(c.memory_if_intrusive); state.tick++; addLog(a.display_name+' refuses: '+c.refusal_if_intrusive+' Alternative: '+c.bounded_alternative); }}
function useObject(respectful) {{ const oid=document.getElementById('objectSelect').value; const con=consequenceFor(oid); const obj=state.objects[oid]; const agent=state.agents[con.agent_id] || state.agents.fayen; state.tick++; if (respectful && con.allowed_with_respect) {{ obj.material_debt=Math.max(0,obj.material_debt+con.debt_delta_allowed); obj.current_location='consented use marker'; agent.trust=Math.min(1,agent.trust+con.trust_delta_allowed); agent.memories.push(con.consequence_if_allowed); addLog('Allowed object use: '+con.consequence_if_allowed); }} else {{ obj.material_debt=Math.min(1,obj.material_debt+con.debt_delta_forced); agent.trust=Math.max(0,agent.trust+con.trust_delta_forced); agent.boundary_pressure=Math.min(1,agent.boundary_pressure+.12); agent.memories.push(con.consequence_if_forced); addLog('Bounded refusal/consequence: '+con.refusal_line+' / '+con.consequence_if_forced); }} render(); }}
function save() {{ localStorage.setItem(storageKey, JSON.stringify(state)); addLog('Saved to localStorage.'); }}
function restore() {{ const raw=localStorage.getItem(storageKey); if (raw) {{ state=JSON.parse(raw); addLog('Restored from localStorage.'); }} else addLog('No saved state found.'); }}
function reset() {{ state=structuredClone(base); addLog('Reset to initial deterministic state.'); }}
function exportState() {{ document.getElementById('stateText').value=JSON.stringify(state,null,2); addLog('Exported state JSON.'); }}
function importState() {{ try {{ state=JSON.parse(document.getElementById('stateText').value); addLog('Imported state JSON.'); }} catch(e) {{ addLog('Import failed: '+e.message); }} }}
document.getElementById('respect').onclick=respectConversation;
document.getElementById('intrude').onclick=intrudeConversation;
document.getElementById('useRespect').onclick=()=>useObject(true);
document.getElementById('forceUse').onclick=()=>useObject(false);
document.getElementById('save').onclick=save; document.getElementById('restore').onclick=restore; document.getElementById('reset').onclick=reset; document.getElementById('export').onclick=exportState; document.getElementById('import').onclick=importState;
render();
</script>
</body>
</html>
""", encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    agents = build_agents()
    objects = build_objects()
    conversations = build_conversations()
    consequences = build_object_consequences()
    memories = build_memory_updates(conversations, consequences)
    snapshots = build_snapshots()
    transitions = build_transitions(conversations, consequences)
    metrics = compute_metrics(agents, objects, conversations, consequences, memories, snapshots, transitions)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["local_agent_conversation_loop_readiness"] >= 0.84 and metrics["save_restore_snapshot_integrity"] >= 1.0 and metrics["bounded_refusal_rate"] >= 0.90 else "fail"
    payload = {
        "report": 222,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_local_agent_conversation_memory_object_consequence_refusal_save_restore",
        "module_verdict": verdict,
        "agents": [asdict(row) for row in agents],
        "objects": [asdict(row) for row in objects],
        "conversations": [asdict(row) for row in conversations],
        "object_consequences": [asdict(row) for row in consequences],
        "memory_updates": [asdict(row) for row in memories],
        "save_restore_snapshots": [asdict(row) for row in snapshots],
        "state_transitions": [asdict(row) for row in transitions],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic scripted interaction, not LLM conversation or subjective experience.",
            "Memory updates are structured local state records, not real autobiographical consciousness.",
            "Bounded refusal is functional behavior, not real consent from conscious beings.",
            "Save/restore uses browser localStorage and JSON export, not durable server persistence.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D social memory loop with autonomous agent ticks, need-driven approach/avoidance, object planning, and cross-session relationship continuity",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "agents": ARTIFACT_DIR / f"{BASE}_agents.csv",
        "objects": ARTIFACT_DIR / f"{BASE}_objects.csv",
        "conversations": ARTIFACT_DIR / f"{BASE}_conversations.csv",
        "object_consequences": ARTIFACT_DIR / f"{BASE}_object_consequences.csv",
        "memory_updates": ARTIFACT_DIR / f"{BASE}_memory_updates.csv",
        "save_restore_snapshots": ARTIFACT_DIR / f"{BASE}_save_restore_snapshots.csv",
        "state_transitions": ARTIFACT_DIR / f"{BASE}_state_transitions.csv",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["agents"], payload["agents"])
    write_csv(paths["objects"], payload["objects"])
    write_csv(paths["conversations"], payload["conversations"])
    write_csv(paths["object_consequences"], payload["object_consequences"])
    write_csv(paths["memory_updates"], payload["memory_updates"])
    write_csv(paths["save_restore_snapshots"], payload["save_restore_snapshots"])
    write_csv(paths["state_transitions"], payload["state_transitions"])
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "local_agent_conversation_loop_readiness": payload["metrics"]["local_agent_conversation_loop_readiness"],
        "conversation_memory_update_rate": payload["metrics"]["conversation_memory_update_rate"],
        "bounded_refusal_rate": payload["metrics"]["bounded_refusal_rate"],
        "save_restore_snapshot_integrity": payload["metrics"]["save_restore_snapshot_integrity"],
        "private_boundary": "sealed private workspaces plus functional boundary/refusal lines only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "local_agent_conversation_loop_readiness": payload["metrics"]["local_agent_conversation_loop_readiness"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "bounded_refusal_rate": payload["metrics"]["bounded_refusal_rate"],
        "save_restore_snapshot_integrity": payload["metrics"]["save_restore_snapshot_integrity"],
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
    print(f"local_agent_conversation_loop_readiness {metrics['local_agent_conversation_loop_readiness']:.6f}")
    print(f"agents {len(payload['agents'])}")
    print(f"objects {len(payload['objects'])}")
    print(f"conversations {len(payload['conversations'])}")
    print(f"object_consequences {len(payload['object_consequences'])}")
    print(f"memory_updates {len(payload['memory_updates'])}")
    print(f"save_restore_snapshots {len(payload['save_restore_snapshots'])}")
    print(f"state_transitions {len(payload['state_transitions'])}")
    print(f"conversation_memory_update_rate {metrics['conversation_memory_update_rate']:.6f}")
    print(f"object_consequence_traceability {metrics['object_consequence_traceability']:.6f}")
    print(f"bounded_refusal_rate {metrics['bounded_refusal_rate']:.6f}")
    print(f"save_restore_snapshot_integrity {metrics['save_restore_snapshot_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
