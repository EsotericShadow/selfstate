# SSRM-3D Injury/Disability Adaptation Report

## Question

Do changed capabilities create persistent control pressure without turning the simulation into biology or roleplay?

Report 74 puts injury/disability adaptation after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, and resource ecology. This experiment asks whether capability self-state, motor adaptation, sensor compensation, infection management, repair access, help-seeking, compensation tools, route adaptation, and restore continuity become useful only when injury or disability changes future action feasibility.

The tested claim is narrow:

> Disability machinery should be rejected in a fixed-body control, but selected when changed mobility, degraded senses, wound infection, social help, compensation tools, route choice, or restore-time forgetting changes future control.

This is not a claim about subjective suffering. It tests injury/disability as delayed capability pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_injury_disability_adaptation.py --train-episodes 72 --eval-episodes 96 --seed 20260628 --candidate-count 7
```

The experiment uses return-selected candidate policies over abstract capability-control state. Policies can use:

| Channel | Role |
|---|---|
| capability self-state | tracks own mobility, sensor quality, infection, exposure, and support state |
| motor adaptation | paces and protects damaged movement capacity |
| sensor compensation | slows scans and adapts to degraded vision/hearing |
| infection management | tracks delayed wound risk and symptom load |
| repair access | seeks treatment or repair before infection and integrity loss compound |
| help-seeking | uses social support when own capability is insufficient |
| compensation tools | uses aids, markers, or devices that restore action feasibility |
| route adaptation | changes path choice to match current body and sensors |
| continuity memory | preserves damage, repair, support, tools, and route history after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact injury/disability control |
| `no_capability_state` | removes own capability estimate |
| `no_motor_adaptation` | removes pacing and mobility-protection control |
| `no_sensor_compensation` | removes degraded vision/hearing compensation |
| `no_infection_management` | removes wound-risk management |
| `no_repair_access` | removes treatment/repair access |
| `no_help_seeking` | removes social compensation |
| `no_compensation_tools` | removes support tools |
| `no_route_adaptation` | removes body-aware route changes |
| `no_continuity` | removes restore-time disability continuity |
| `ignore_disability_baseline` | acts as if body/sensors are fixed |
| `omniscient_disability_control` | upper-bound disability control |

## Results

| Scenario | Selected policy | Capability loss | Motor loss | Sensor loss | Infection loss | Repair loss | Help loss | Tool loss | Route loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `fixed_body_control` | `ignore_disability_baseline` | -0.019 | -0.075 | -0.044 | -0.098 | 0.082 | 0.027 | 0.008 | 0.016 | 0.011 | disability machinery rejected |
| `limp_route_adaptation` | `limp_route_tool_planner` | 76.843 | 184.822 | -0.157 | -0.298 | -0.255 | -0.257 | 113.561 | 115.636 | -0.095 | limp/route/tool pressure |
| `vision_hearing_damage` | `sensor_compensation_planner` | 93.679 | -0.954 | 206.126 | -0.695 | -0.281 | -0.423 | 131.054 | 130.512 | -0.045 | vision/hearing compensation pressure |
| `wound_infection_repair` | `infection_repair_planner` | 74.193 | 121.441 | 0.141 | 90.020 | 393.278 | 0.039 | 0.126 | 0.011 | -0.077 | wound infection repair pressure |
| `social_help_compensation` | `help_tool_route_planner` | 69.179 | 139.830 | 122.556 | 0.086 | 0.173 | 78.104 | 102.879 | 101.539 | 0.046 | social help compensation pressure |
| `restore_disability_continuity` | `continuity_disability_planner` | 64.629 | 127.753 | 121.122 | 75.136 | 238.188 | 47.429 | 82.206 | 80.644 | 59.908 | restore disability continuity pressure |

All six verdict rows pass `supports_injury_disability_precursor=True`.

Key targeted losses:

- `fixed_body_control`: disability machinery is not selected and targeted ablations have near-zero effect.
- `limp_route_adaptation`: removing capability state, motor adaptation, support tools, or route adaptation causes large loss.
- `vision_hearing_damage`: removing capability state, sensor compensation, support tools, or route adaptation causes large loss.
- `wound_infection_repair`: removing capability state, motor adaptation, infection management, or repair access causes large loss.
- `social_help_compensation`: removing capability state, motor adaptation, sensor compensation, help-seeking, support tools, or route adaptation causes large loss.
- `restore_disability_continuity`: removing continuity plus capability, motor, sensor, infection, repair, help, tool, or route channels causes targeted loss.

## Interpretation

This result supports the ninth pressure-layer step at precursor level:

- injury/disability machinery is not globally useful;
- capability state matters when current body or sensors differ from the fixed-body assumption;
- motor adaptation matters when limping changes route cost and fall risk;
- sensor compensation matters when degraded vision/hearing changes exposure and collision risk;
- infection and repair matter when wound state has delayed consequences;
- help and support tools matter when external assistance preserves future action;
- route adaptation matters when the feasible path depends on current capability;
- continuity matters when restore can erase damage, repair, help, tool, or route history.

The boundary remains explicit:

> Injury/disability is not selfhood. It becomes relevant to selfhood only when the agent must model its own capability, sensory limits, mobility limits, infection risk, tool support, help access, route feasibility, and restore-time adaptation history as future-control variables.

Some selected policies carry extra channels whose ablations are neutral in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Injury/disability dynamics are abstract control variables, not biology.
- Repair, help, tool, and route policies are designed channels.
- The selected planner is not an online RL agent discovering disability adaptation from scratch.
- This report itself does not include learned skill development, dependent care, or irreversible loss.

## Next Test

The implemented follow-up adds development and skill learning:

- repeated actions should improve competence;
- injury, fatigue, illness, and stress should degrade competence;
- agents should estimate what they can safely do now versus after rest, repair, help, or practice;
- ablations should separate skill memory, capability self-state, practice history, transfer, and continuity.

Implemented by [report 84](84_ssrm_3d_development_skill_learning_report.md).

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_injury_disability_adaptation.html
```

The page replays the `social_help_compensation` trace with mobility, vision, hearing, infection, integrity, exposure, support tools, help, route fit, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_injury_disability_adaptation.py)
- [visualization](../visualizations/ssrm_3d_injury_disability_adaptation.html)
- [evaluation CSV](../artifacts/ssrm_3d_injury_disability_adaptation_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_injury_disability_adaptation_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_injury_disability_adaptation_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_injury_disability_adaptation_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_injury_disability_adaptation_trace.json)
- [JSON results](../artifacts/ssrm_3d_injury_disability_adaptation_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_injury_disability_adaptation_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_injury_disability_adaptation_results.js)
