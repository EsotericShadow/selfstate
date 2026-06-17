# Report 263: SSRM-3D Browser World v23 Object-Specific Dialogue Inventory Request Reaction Consequence Bridge

## Purpose

Report 263 extends the v22 free-move browser scene by making object dialogue specific to owned objects, letting agents author inventory requests, and forcing reaction state to change later scene behavior. The key change is delayed consequence: a saved reaction can now alter later pathing, access gates, object requests, refusals, and agent-initiated behavior.

The boundary remains explicit: this is deterministic browser-local gameplay scaffolding. It is not an LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or a complete 3D engine.

## What changed

- Added `experiments/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge.py`.
- Generated `416` browser-world v23 ticks across `26` days.
- Added `416` object-specific dialogue frames that name an object, owner boundary, affordance, and prior reaction.
- Added `416` agent-owned inventory request frames for returns, distance-before-touch, help, and inspection.
- Added `416` reaction-consequence frames that map remembered reaction state into path bias, access gates, object request bias, and follow-up changes.
- Added `416` later scene behavior frames showing altered pathing, approach/avoidance, and request initiation.
- Added `416` access/refusal frames with bounded refusal and alternatives.
- Added `416` agent-initiated behavior frames, `416` storage snapshots, `416` sensory consequence frames, and `416` replay frames.
- Added browser artifact `visualizations/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge.html` with object requests, local reaction/access state, save/restore, and replay export controls.

## Deterministic run

Command:

```bash
python3 -m experiments.ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge
```

Result:

- Verdict: `pass`
- Seed: `20260876`
- Readiness: `0.886592`
- Weakest channel: `0.795673`
- Weakest pressure point: `agent_owned_request_resolution`
- Source dependency: `artifacts/ssrm_3d_browser_world_v22_free_move_proximity_dialogue_inventory_reaction_bridge_results.json`
- Source verdict: `pass`

## Metrics

- `access_refusal_calibration`: `0.974159`
- `agent_initiated_behavior_binding`: `0.989183`
- `agent_initiated_behavior_rate`: `0.961165`
- `agent_owned_inventory_request_rate`: `0.880000`
- `agent_owned_request_resolution`: `0.795673`
- `bounded_refusal_alternative_rate`: `0.947368`
- `browser_world_v23_reaction_consequence_readiness`: `0.886592`
- `browser_world_v23_surface_available`: `1.000000`
- `comfort_pain_consequence_bounds`: `1.000000`
- `delayed_followup_consequence`: `1.000000`
- `frequency_flower_consequence_rhythm`: `1.000000`
- `later_scene_behavior_score`: `0.917067`
- `mean_consequence_channel_score`: `0.952430`
- `object_affordance_reference_rate`: `0.940541`
- `object_owner_reference_rate`: `0.918919`
- `object_specific_dialogue_binding`: `0.943750`
- `privacy_safe_consequence_state`: `1.000000`
- `reaction_to_access_coupling`: `0.971154`
- `reaction_to_later_pathing_coupling`: `0.949519`
- `reaction_to_object_request_coupling`: `1.000000`
- `replay_consequence_integrity`: `0.943269`
- `request_boundary_integrity`: `0.875601`
- `sensory_consequence_binding`: `0.961538`
- `source_free_move_inventory_reaction_continuity`: `1.000000`
- `storage_consequence_schedule_integrity`: `0.939904`
- `visible_behavior_consequence_surface`: `0.949519`
- `weakest_channel_score`: `0.795673`

Additional counts:

- `visible_object_dialogue_count`: `370`
- `visible_agent_request_count`: `308`
- `visible_refusal_count`: `38`
- `reaction_request_bias_count`: `179`

## Ablations

- `no_object_specific_dialogue`: readiness `0.561592`; loss `0.325000` - Prompts stop naming owned objects and collapse back to generic proximity text.
- `no_agent_owned_inventory_requests`: readiness `0.581592`; loss `0.305000` - Agents stop asking for returns, help, inspection, or distance around owned objects.
- `no_reaction_to_later_pathing`: readiness `0.586592`; loss `0.300000` - Saved reaction labels no longer change later agent movement.
- `no_access_gate_consequence`: readiness `0.626592`; loss `0.260000` - Guarded or softened reactions no longer alter access/refusal behavior.
- `no_agent_initiated_followup`: readiness `0.651592`; loss `0.235000` - Agents stop initiating later behavior from remembered reaction state.
- `no_consequence_storage`: readiness `0.676592`; loss `0.210000` - Consequence schedules and request queues cannot survive reload.

## Interpretation

This report closes the specific weakness called out by Report 262: reaction labels no longer remain only stored panel state. Prior reactions now alter later agent pathing, access posture, refusal behavior, object request bias, and agent-initiated follow-up.

The pass is still bounded. The weakest channel is `agent_owned_request_resolution` at `0.795673`. That is the correct next pressure point: agents can ask for object-specific help or returns, but the browser scaffold does not yet sustain multi-day task obligations where unresolved requests compound across scene visits.

## Artifact ledger

- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_access_and_refusals.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_agent_initiated_behaviors.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_agent_owned_inventory_requests.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_browser_ticks.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_consequence_replays.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_later_scene_behaviors.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_multi_sensory_consequences.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_object_specific_dialogue.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_reaction_consequences.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_reaction_memory_snapshots.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_results.json`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_state.json`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_summary.csv`
- `artifacts/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_verdict.csv`
- `visualizations/ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge.html`

## Boundary

This report builds deterministic first-person artificial-life scaffolding only. It does not claim subjective consciousness, real feelings, real consent, moral patienthood, autonomous natural language, or complete 3D gameplay.

## Next gate

browser world v24 with agent-owned tasks that persist across many scene visits, object return obligations, and delayed trust/access changes that compound over multiple days
