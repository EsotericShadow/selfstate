# Learned Sensor-Subspace Filter Report

## Purpose

This experiment closes the main loophole left by the mixed-sensor recurrent filter.

The mixed-sensor test removed self-aligned input channels, but its ablation still removed known latent sources before mixing. This version learns the ablated direction directly in observed sensor space from training outcomes.

The question is:

```text
Can a useful recurrent dependency be recovered from mixed observations, then
damaged by a learned sensor-space intervention rather than known source
ablation?
```

## Environment

The environment is the same as the mixed-sensor recurrent filter.

Each episode has eight future control steps. Two noisy latent sources are rotated into two mixed sensors:

```text
sensor_1 = 0.8 * source_A + 0.6 * source_B
sensor_2 = -0.6 * source_A + 0.8 * source_B
```

The controller observes only `sensor_1` and `sensor_2`.

The learned intervention direction is computed from training data by contrasting episode outcome rates against mean mixed-sensor vectors. It uses:

- mixed sensor observations;
- observed outcome rates;
- no source labels;
- no source ablation.

Boundary interventions are still supplied only after the ablation test, to classify the damaged dependency as agent-bounded or external.

Scenarios:

| Scenario | Hidden structure | Expected result |
|---|---|---|
| `self_mixed_hidden` | Source A tracks persistent hidden agent-state. | Recurrent controller wins; learned sensor-direction ablation damages control; boundary test classifies it as agent-bounded. |
| `world_mixed_hidden` | Source B tracks persistent hidden external state. | Recurrent controller wins; learned sensor-direction ablation damages control; boundary test classifies it as external. |
| `independent_hidden` | Future steps have independent hidden states. | Local probing wins and learned subspace ablation does not establish a shared boundary. |
| `irrelevant_control` | Risky action always succeeds. | Greedy no-state wins and no learned subspace is needed. |

## Current Result

Canonical run:

```bash
python3 experiments/learned_sensor_subspace_filter.py --episodes 500 --training-episodes 800 --seed 20260603 --horizon 8 --evidence-samples 9 --cue-accuracy 0.85 --random-candidates 1800
```

Verdict:

| Scenario | Selected policy | Dependency signature | Recurrent reward | Local probe reward | Learned ablation loss | Supported? |
|---|---|---|---:|---:|---:|---|
| `self_mixed_hidden` | `recurrent_controller` | `agent_bounded_learned_subspace` | 133.528 | 127.168 | 83.200 | Yes |
| `world_mixed_hidden` | `recurrent_controller` | `external_learned_subspace` | 125.976 | 120.000 | 70.528 | Yes |
| `independent_hidden` | `task_local_probe` | `no_learned_subspace_boundary` | 62.408 | 125.024 | 0.000 | Yes |
| `irrelevant_control` | `greedy_no_state` | `no_learned_subspace_boundary` | 191.000 | 184.000 | 0.000 | Yes |

Learned sensor-space dependency:

| Scenario | Learned direction | Strength | Learned ablation loss | Boundary effect A | Boundary effect B | Interpretation |
|---|---:|---:|---:|---:|---:|---|
| `self_mixed_hidden` | `(0.822, -0.569)` | 0.701 | 83.200 | 0.460 | 0.000 | Learned sensor direction carries agent-bounded control evidence. |
| `world_mixed_hidden` | `(0.645, 0.764)` | 0.697 | 70.528 | 0.000 | 0.444 | Learned sensor direction carries external-state control evidence. |
| `independent_hidden` | `(-0.778, -0.628)` | 0.029 | 0.000 | 0.000 | 0.000 | Weak chance direction is not control-relevant. |
| `irrelevant_control` | `(0.000, 0.000)` | 0.000 | 0.000 | 0.000 | 0.000 | No hidden-state dependency needed. |

## Interpretation

The result supports a narrower precursor:

```text
The useful recurrent dependency does not need to be ablated by a known latent
source. A behaviorally relevant direction can be learned in mixed sensor space,
and removing that learned direction selectively damages control.
```

This still does not make recurrent hidden state selfhood by default. The world-hidden regime also produces a behaviorally relevant learned subspace. It is not self-equivalent because the boundary intervention classifies the dependency as external.

## What It Adds

Compared with the mixed-sensor recurrent filter, this test removes:

- known-source ablation as the destructive intervention;
- direct use of source coordinates when testing whether the policy depends on the recovered information.

It keeps:

- the same supplied mixing matrix;
- the same small recurrent architecture family;
- supervised outcome rates for learning the sensor-space direction;
- supplied boundary interventions for classifying self versus world.

## Limits

This is still a toy precursor.

The learned direction is outcome-supervised, not autonomously discovered by a general causal learner. The boundary interventions are supplied by the experimenter. The recurrent search is random-start, not scalable gradient RL. The observation stream remains a two-dimensional linear mixture.

The next stronger version should learn intervention directions from richer histories and test hidden-state interventions inside independently trained recurrent or model-based agents.

## Falsifiers

The learned sensor-subspace account weakens if:

- learned sensor-space ablation does not damage recurrent control in shared agent-state regimes;
- the same learned subspace damages self, world, independent, and irrelevant controls indiscriminately;
- local probing or greedy no-state control matches recurrent filtering when one persistent mixed latent controls future steps;
- boundary interventions cannot distinguish agent-bounded from external learned subspaces;
- richer agents require known source coordinates for causal ablation.

## Artifacts

- [experiment script](../experiments/learned_sensor_subspace_filter.py)
- [summary CSV](../artifacts/learned_sensor_subspace_filter_summary.csv)
- [training CSV](../artifacts/learned_sensor_subspace_filter_training.csv)
- [dependency CSV](../artifacts/learned_sensor_subspace_filter_dependency.csv)
- [verdict CSV](../artifacts/learned_sensor_subspace_filter_verdict.csv)
- [JSON results](../artifacts/learned_sensor_subspace_filter_results.json)
