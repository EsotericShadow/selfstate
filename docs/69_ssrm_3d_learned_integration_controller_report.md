# SSRM-3D Learned Integration Controller Report

## Question

Can tool use, social memory, continuity memory, and attention mixing move into learned controller state rather than remaining separate return-selected policy families?

This report targets the next SSRM-3D gap after reports 65-68. Tool-making, social pressure, social ecology, and continuity now have useful precursors, but they are still mostly candidate-policy or explicit-record tests. This experiment asks whether a learned recurrent controller uses those information streams because they improve action.

The tested claim is deliberately vulnerable:

> A learned recurrent policy state should outperform a frame-only policy when early tool, social, continuity, or attention evidence must be carried forward, and ablations should fail only in the regimes that need the removed evidence.

The result should be read as a designed packet bridge, not as open learned integration. Scenario identity and feature-group structure are still supplied by the experiment.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_learned_integration_controller.py --train-episodes 320 --eval-episodes 140 --epochs 160 --seed 20260614 --device auto
```

The learner receives short compressed state-packet traces. It is trained from reward-derived action choices, not from labels named self, tool, social, continuity, or attention.

Architectures:

| Architecture | Role |
|---|---|
| `frame_mlp` | Reads the final packet only. |
| `torch_gru` | Integrates the packet sequence into recurrent policy state. |

Feature groups:

| Group | Meaning |
|---|---|
| `world` | visible resource, hazard, shelter, night, decision tick |
| `self` | energy, damage, mobility, uncertainty, commitment urgency |
| `tool` | route cue, marker memory, alarm/tool confidence |
| `social` | identity cue, trust cue, reputation, vulnerability |
| `continuity` | commitment ownership, branch risk, event log, body/model match |
| `attention` | priority over action modes |

Post-training ablations zero the tool, social, continuity, or attention group at evaluation.

## Multi-Rate Scope

This experiment uses short packet sequences, so `tick` is only a trace index. It should not be read as one global cognitive loop.

The intended SSRM framing is rate based:

```text
base_tick_hz = 60
reflex_hz = 60
motor_control_hz = 30
perception_hz = 10
attention_hz = 10
self_state_hz = 5
goal_hz = 2
reasoning_hz = 0.5
memory_hz = 0.1
```

The simulator can derive implementation intervals from those rates, but the claim being tested is multi-rate integration: fast loops protect viability and movement, medium loops estimate world and attention state, slower loops maintain self-state and goals, and the LLM/memory layers should update only when their timescale earns the cost.

## Scenarios

| Scenario | Pressure |
|---|---|
| `visible_resource_control` | no tool, social, continuity, or attention pressure |
| `learned_tool_route` | route evidence appears early and must be carried into tool action |
| `learned_social_repair` | helper/deceiver identity appears early and controls repair action |
| `learned_continuity_restore` | commitment and branch evidence appears early and controls restore action |
| `integrated_gate_pressure` | tool, social, and continuity cues compete; attention selects priority |

## Results

| Scenario | Frame reward | Recurrent reward | Gain | Key ablation loss | Verdict |
|---|---:|---:|---:|---:|---|
| `visible_resource_control` | 112.000 | 112.000 | 0.000 | max loss 0.000 | extra state rejected |
| `learned_tool_route` | 79.214 | 112.000 | 32.786 | tool loss 38.571 | tool memory used |
| `learned_social_repair` | 82.286 | 112.000 | 29.714 | social loss 90.000 | social identity memory used |
| `learned_continuity_restore` | 86.314 | 112.000 | 25.686 | continuity loss 90.000 | continuity memory used |
| `integrated_gate_pressure` | 71.971 | 128.000 | 56.029 | attention loss 50.214; continuity loss 37.529 | designed integration bridge |

All rows pass `supports_learned_integration_precursor=True` in the seeded canonical run. This is still a bridge result because the packet schema, scenario identity, and feature-group ablations are supplied.

## Interpretation

This is stronger than the previous tool/social/continuity precursors in one specific way: useful designed packet channels can affect a learned policy state.

It does not show open-ended tool invention, open-ended society, learned identity repair, or stable cross-pressure integration across seeds and randomized pressures. The traces and reward surfaces are still designed. It removes one weakness only partially: successful behavior is no longer only a hand-selected candidate policy or an explicit continuity record, but the integration surface remains hand structured.

The result supports the next bounded claim only at bridge level:

- tool evidence matters only when route memory must be externalized;
- social evidence matters only when identity or trust affects repair and risk;
- continuity evidence matters only when branch or commitment ownership affects future action;
- attention matters when several valid pressures compete and one must be selected;
- the strong claim that one recurrent state independently discovers tool, social, continuity, and attention pressures is not yet supported.

If the frame-only controller matched recurrent performance, or if every ablation caused the same generic collapse, the bridge claim would fail. If no-scenario-leakage, randomized-pressure, or multi-seed versions collapse, the strong learned-integration claim remains false.

## Limits

- The controller is trained from reward-derived action choices, not online RL.
- The packet structure is hand designed.
- Scenario identity is still embedded in the packet rows.
- The feature groups are known for ablation.
- The recurrent architecture is a small GRU, not a rich embodied model-based agent.
- Probe scores are diagnostic only; the boundary evidence is the pressure-specific action loss.
- Early unseeded runs exposed verdict instability; model initialization is now seeded, but multi-seed robustness is still untested.

The next stronger version should remove scenario identity leakage, randomize pressure combinations, run multiple seeds, require wider margins, and then move the result into the full SSRM-3D world with learned tool construction, repeated social interaction, continuity restore/fork events, and multi-rate control.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_learned_integration.html
```

The visualization replays the integrated gate-pressure trace, showing feature-group activation over time, recurrent action confidence, ablation outcomes, and scenario verdicts.

The page loads generated JS fallback artifacts so it can recover when JSON fetch is not available.

## Artifacts

- [experiment script](../experiments/ssrm_3d_learned_integration_controller.py)
- [visualization](../visualizations/ssrm_3d_learned_integration.html)
- [evaluation CSV](../artifacts/ssrm_3d_learned_integration_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_learned_integration_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_learned_integration_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_learned_integration_trace.json)
- [JSON results](../artifacts/ssrm_3d_learned_integration_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_learned_integration_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_learned_integration_results.js)
