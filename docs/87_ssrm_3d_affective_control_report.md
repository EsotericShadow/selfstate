# SSRM-3D Affective Control Report

## Question

Do emotion-like variables create useful persistent control pressure, without claiming subjective feeling?

Report 74 puts affective control after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, resource ecology, injury/disability adaptation, development/skill learning, dependent care, and irreversible loss. This experiment asks whether fear, stress, trust, frustration, affiliation, curiosity, guilt analogue, attention mixing, memory salience, risk modulation, communication bias, and continuity become useful only when they change control.

The test is narrow:

> Affective machinery should be rejected in a calm clear control, but selected when compact internal summaries improve attention, risk tolerance, approach/avoidance, communication, memory salience, information seeking, commitment repair, or restore continuity.

This is not subjective emotion, valence, or consciousness. It tests `affective_control_state` as an abstract control summary.

## Command

```bash
python3 experiments/ssrm_3d_affective_control.py --train-episodes 72 --eval-episodes 96 --seed 20260702 --candidate-count 8
```

## Mechanisms

| Mechanism | Control role |
|---|---|
| fear control | shifts attention and risk tolerance under hazard, injury, darkness, or threat pressure |
| stress control | arbitrates competing needs, low energy, commitments, and overload |
| trust control | biases approach, help-seeking, cooperation, and repair access from history |
| frustration control | detects repeated failure and switches strategy or asks for help |
| affiliation control | maintains low-cost cooperation and future social access |
| curiosity control | turns tolerable uncertainty into inspection or information seeking |
| guilt analogue | repairs failed commitments before social access collapses |
| attention mixing | routes the active control summary into arbitration |
| memory salience | preserves high-control-value events for later action |
| risk modulation | adjusts risk tolerance when future options are exposed |
| communication bias | changes signaling, repair, warning, or social-maintenance actions |
| affective continuity | preserves affective-control state after restore/interruption |

## Conditions

| Condition | Meaning |
|---|---|
| `full_control` | intact affective-control state |
| `no_fear_control` | removes hazard-linked fear control |
| `no_stress_control` | removes competing-need stress arbitration |
| `no_trust_control` | removes trust-based social access control |
| `no_frustration_control` | removes repeated-failure switching pressure |
| `no_affiliation_control` | removes low-cost cooperation maintenance |
| `no_curiosity_control` | removes uncertainty-driven inspection |
| `no_guilt_control` | removes commitment-repair control |
| `no_attention_mixing` | removes routing of affective summaries into arbitration |
| `no_memory_salience` | removes event salience/memory weighting |
| `no_risk_modulation` | removes risk-threshold adjustment |
| `no_communication_bias` | removes affect-driven communication changes |
| `no_affective_continuity` | removes restore-time affective-control continuity |
| `reactive_no_affect` | acts without affective summaries |
| `omniscient_affect_control` | upper-bound affective-control policy |

## Results

Loss values are mean reward loss from the selected `full_control` policy.

| Scenario | Selected policy | fear | stress | trust | frustration | affiliation | curiosity | guilt | attention | memory | risk | communication | continuity | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `calm_clear_control` | `reactive_no_affect` | 0.014 | 0.018 | 0.008 | -0.015 | 0.032 | 0.014 | 0.000 | 0.026 | 0.012 | -0.008 | 0.008 | -0.006 | affect rejected |
| `fear_hazard_attention` | `integrated_affect_planner` | 847.626 | -2.518 | -2.687 | -2.582 | -2.509 | -2.593 | -2.814 | 207.364 | 170.564 | 215.222 | -2.530 | 0.014 | fear/risk pressure |
| `stress_need_arbitration` | `stress_arbitrator` | -0.036 | 883.874 | 0.006 | -0.041 | -0.013 | -0.044 | -0.039 | 214.736 | 184.493 | 99.029 | -0.002 | -0.001 | stress pressure |
| `trust_affiliation_social` | `trust_affiliation_planner` | -0.014 | -0.008 | 932.404 | -0.011 | 159.422 | -0.030 | 0.014 | 122.789 | 131.466 | 0.011 | 183.036 | -0.010 | trust/affiliation pressure |
| `frustration_curiosity_switching` | `frustration_curiosity_planner` | 0.010 | -0.001 | -0.001 | 535.667 | 0.008 | 230.398 | -0.010 | 127.938 | 144.210 | 123.946 | 0.016 | 0.010 | switching/inspection pressure |
| `guilt_commitment_repair` | `guilt_repair_planner` | -0.024 | 518.126 | 869.422 | -0.028 | 0.018 | 0.019 | 586.740 | 127.461 | 149.266 | -0.056 | 189.052 | -0.011 | commitment repair pressure |
| `restore_affective_continuity` | `continuity_affect_planner` | 362.016 | 242.474 | 656.888 | 342.960 | 131.237 | 232.573 | 211.664 | 224.185 | 229.148 | 222.121 | 287.649 | 235.729 | restore pressure |

All seven verdict rows pass `supports_affective_control_precursor=True`.

## Interpretation

This result supports the thirteenth pressure-layer step at precursor level:

- affective machinery is rejected in the calm clear control;
- fear-like control matters only when hazards, injury risk, and low visibility make risk and attention costly;
- stress-like control matters only when competing needs and commitments require arbitration;
- trust and affiliation matter only when repeated social history changes future help or access;
- frustration and curiosity matter only when repeated failure and uncertainty make switching or inspection useful;
- a guilt analogue matters only when failed commitments change future social access unless repaired;
- attention mixing, memory salience, risk modulation, communication, and continuity matter only under matching pressure.

The anti-overclaim boundary is:

> Affective control state is not subjective emotion. It becomes relevant to selfhood only when compact internal summaries change the tested agent's own future control, memory, social access, risk tolerance, or continuity.

## Limits

- Candidate policies are supplied and return-selected.
- Affective dynamics are abstract control variables, not psychology or feeling.
- The selected planner is not an online RL agent discovering emotion-like control from scratch.
- Some scenarios select an integrated policy because extra summaries are low-cost enough to keep, so this is not a sparse-discovery result.
- This does not yet test learned affective state inside the full SSRM-3D recurrent controller.

## Next Test

The next pressure-layer step should move from individual pressure variables toward places with function and territory/social infrastructure, or start extracting the live demo/framework surface. For affect specifically, the stronger follow-up is:

- remove labels from affective channels;
- train recurrent controllers under the same pressures;
- test whether compact affective subspaces emerge without named fear, stress, trust, frustration, affiliation, curiosity, or guilt inputs;
- ablate learned subspaces to see whether failures remain pressure-specific.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_affective_control.html
```

The page replays the `frustration_curiosity_switching` trace with affective-control summaries, attention, memory salience, uncertainty, social access, commitment standing, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_affective_control.py)
- [visualization](../visualizations/ssrm_3d_affective_control.html)
- [evaluation CSV](../artifacts/ssrm_3d_affective_control_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_affective_control_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_affective_control_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_affective_control_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_affective_control_trace.json)
- [JSON results](../artifacts/ssrm_3d_affective_control_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_affective_control_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_affective_control_results.js)
