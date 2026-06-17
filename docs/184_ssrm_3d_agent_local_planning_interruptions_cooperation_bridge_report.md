# Report 184: SSRM-3D Agent-Local Planning, Interruptions, Project Dependencies, and Cooperation Bridge

## Purpose

Report 184 adds a planning layer above Report 183 autonomous routines. Report 183 showed that agents can choose actions from homes, routine phases, needs, work projects, object affordances, routes, frequency/flower coupling, rest recovery, and relationship carryover. This report asks whether agents can hold multi-step local plans, pause after interruptions, resume, resolve project dependencies, hand objects across boundaries, coordinate routes, and cooperate without exposing a private planning workspace.

This is local planning substrate. It does not claim complete gameplay, subjective consciousness, moral patienthood, natural language emergence, or free will.

## Architecture

The bridge consumes the Report 183 autonomous routine state:

```text
autonomous routine state
        |
        v
private local plan stacks
        |
        v
public plan summaries
        |
        v
project dependencies
        |
        v
interruptions and priority replans
        |
        v
pause / resume recovery
        |
        v
object handoffs and cooperation
        |
        v
route coordination
        |
        v
frequency + flower plan binding
        |
        v
browser-local planning replay
```

The default deterministic run uses:

- `4` simulated local days
- `6` planning ticks per day
- `3` agents
- `72` planning events
- private multi-step plan stacks with public summaries
- deterministic interruptions at selected global ticks
- dependency handoffs between agents
- route coordination and replay frames

## Projects

The integrated run gives each agent a project:

- `Ari`: `repair_clay_latch_with_dry_patch`
- `Fay`: `dry_cloak_and_moss_bedding_support`
- `Milo`: `ridge_warning_route_clearance`

Project dependencies include:

- `dry_cloak_handoff`
- `ridge_route_signal`
- `reed_cup_ready`
- `glass_lens_check`

The point is not that these are complex projects yet. The point is that progress now depends on dependency state, object handoff, cooperation, and replanning rather than a single-step routine action.

## Interruptions

The integrated run injects deterministic interruptions:

- `wet_squall`
- `missing_dependency`
- `route_hazard_warning`

These interruptions pause plans, create priority replans, and require recovery/resume behavior. Negative state remains bounded and recoverable.

## Browser surface

The browser artifact is:

- `visualizations/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge.html`

It loads generated JS artifacts and lets the user:

- step through planning events
- inspect public plan summaries
- confirm private plan stacks remain hidden
- watch agents move on the settlement graph
- inspect interruptions and recovery packets
- inspect dependency status
- inspect object handoffs and cooperation packets
- save, restore, and reset local browser planning state

## Conditions

The integrated condition is:

- `integrated_agent_local_planning_interruptions_cooperation`

Ablations remove one mechanism at a time:

- `no_plan_generation`
- `no_multi_step_plan`
- `no_interruptions`
- `no_resume_after_interrupt`
- `no_project_dependencies`
- `no_cooperation`
- `no_dependency_handoff`
- `no_route_coordination`
- `no_priority_replan`
- `no_frequency_flower_plan_binding`
- `no_bounded_stress_recovery`
- `no_replay_timeline`
- `no_privacy_filter`

The critical ablations are plan generation, project dependencies, cooperation, handoff integrity, priority replanning, and interruption recovery. A convincing agent cannot only perform routine ticks; it needs to plan, pause, coordinate, and resume.

## Metrics

The benchmark reports:

- `plan_generation_rate`
- `multi_step_plan_integrity_rate`
- `interruption_detection_rate`
- `interruption_recovery_rate`
- `project_dependency_resolution_rate`
- `cooperation_event_rate`
- `handoff_integrity_rate`
- `route_coordination_rate`
- `priority_replan_rate`
- `frequency_flower_plan_binding_rate`
- `bounded_stress_recovery_rate`
- `browser_plan_replay_rate`
- `privacy_preservation_rate`
- `trace_integrity`
- `local_planning_readiness`

Metric weights are normalized to sum to `1.0`.

## Results

The deterministic run produced:

| Metric | Value |
| --- | ---: |
| `module_verdict` | `pass` |
| `local_planning_readiness` | `1.000000` |
| `planning_events` | `72` |
| `no_project_dependencies_loss` | `0.170000` |
| `no_cooperation_loss` | `0.090000` |
| `no_priority_replan_loss` | `0.080000` |

Interpretation:

- Multi-step local planning is present.
- Interruptions are detected and recovered from.
- Project dependencies are load-bearing.
- Cooperation is load-bearing.
- Priority replanning is load-bearing.
- Private plan stacks remain hidden; public plan summaries are exposed for traceability.

## Moral and claim boundary

This report keeps the boundary explicit:

- no subjective-consciousness claim
- no moral-patienthood claim
- no complete-3D-world claim
- no complete-playable-world claim
- no natural-language-emergence claim
- private plan stacks are not subjective workspace
- cooperation policy is not moral patienthood
- interruption recovery is not subjective suffering
- private workspace is not exposed as a debug shortcut

## Artifacts

- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_eval.csv`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_verdict.csv`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_results.json`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_results.js`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_trace.json`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_trace.js`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_state.json`
- `artifacts/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_state.js`
- `visualizations/ssrm_3d_agent_local_planning_interruptions_cooperation_bridge.html`

## Command

```bash
python3 -m experiments.ssrm_3d_agent_local_planning_interruptions_cooperation_bridge
```

## Verdict

Report 184 supports a deterministic agent-local planning, interruption recovery, project dependency, and cooperation seed over the Report 183 autonomous routine layer. Agents now generate public plan summaries from private hidden plan stacks, pause and resume plans, replan around interruptions, resolve dependencies, coordinate routes, and cooperate through object handoffs.

The next gate is a multi-agent project economy with resource scarcity, negotiation, and tool chains: plans should start competing for scarce materials, require sequential tools, negotiate access, and leave persistent economic consequences.
