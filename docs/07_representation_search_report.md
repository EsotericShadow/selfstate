# Representation Search Report

## Purpose

The first experiment supplied the self/world factorization directly. This second experiment asks a narrower question:

> If a learner only sees actions and effects, does an agent-state-like variable get selected because it is the shortest accurate predictive model?

This tests "self as compression" without asking the system to report a self and without labeling any variable as self during fitting.

## Command

```bash
python3 experiments/representation_search.py --episodes 500 --seed 20260530 --max-action 15 --calibration-samples 8
```

Outputs:

- `artifacts/representation_search_model_summary.csv`
- `artifacts/representation_search_category_summary.csv`
- `artifacts/representation_search_results.json`

## Data

For each scenario, the simulator samples the post-perturb hidden state and gives each candidate model the same action/effect calibration samples.

The learner sees:

```text
action -> observed delta
```

It does not receive the true `gain`, true `wind`, scenario type, or labels such as "self" or "world".

The held-out test set evaluates predictions across the full action range.

## Candidate Representations

| Model | Form | Parameters | Category |
|---|---:|---:|---|
| identity fixed body | `delta = action` | 0 | no self |
| world bias | `delta = action + wind` | 1 | world only |
| self gain | `delta = gain * action` | 1 | self-equivalent |
| factorized gain/wind | `delta = gain * action + wind` | 2 | self-equivalent |
| action memory | one effect per observed action | variable | implicit action memory |

Selection uses Bayesian information criterion on calibration data, with held-out mean absolute error reported separately.

## Category Results

| Scenario | Selected category | Selection rate |
|---|---|---:|
| static goal switch | no self | 1.000 |
| world drift | world only | 1.000 |
| self drift | self-equivalent | 1.000 |
| mixed hidden | self-equivalent | 0.788 |
| mixed hidden | world only | 0.152 |
| mixed hidden | no self | 0.060 |

The mixed-hidden result splits because the sampled post-perturb state does not always require both hidden variables. When actuator gain matters, a self-equivalent model is selected; when only external drift or no hidden change matters, simpler models can win.

## Model Results

| Scenario | Model | Selection rate | Mean test MAE |
|---|---|---:|---:|
| static goal switch | identity fixed body | 1.000 | 0.000 |
| static goal switch | self gain | 0.000 | 0.000 |
| static goal switch | factorized gain/wind | 0.000 | 0.000 |
| world drift | world bias | 1.000 | 0.000 |
| world drift | factorized gain/wind | 0.000 | 0.000 |
| self drift | self gain | 1.000 | 0.000 |
| self drift | factorized gain/wind | 0.000 | 0.000 |
| mixed hidden | factorized gain/wind | 0.522 | 0.000 |
| mixed hidden | self gain | 0.266 | 1.011 |
| mixed hidden | world bias | 0.152 | 6.125 |
| mixed hidden | identity fixed body | 0.060 | 6.311 |
| mixed hidden | action memory | 0.000 | 1.416 |

Exact-fit models with fewer parameters win. That is why identity wins in the static case, world-bias wins in the external-drift case, self-gain wins in the pure self-drift case, and factorized gain/wind wins when both hidden causes matter.

## Interpretation

This supports the compression hypothesis in a limited but useful way.

The learner does not need a variable named "self". It needs a compact adjustable parameter that captures how its own actions now affect the world. In this toy environment, that parameter is `gain`.

The result is conditional:

- no hidden agent-state relevance -> no-self model selected;
- external hidden cause only -> world-only model selected;
- hidden agent action-effect state -> self-equivalent model selected;
- mixed hidden causes -> self/world factorization selected when both terms matter.

That is the pattern the research program predicts.

## What This Does Not Prove

This is still not spontaneous selfhood in a strong sense. The candidate model family includes action-conditioned linear forms, and the environment is deliberately linear.

It also does not prove that explicit self-representation is necessary. A richer generic predictive-state learner could encode the same information implicitly. That remains a live alternative and a required future test.

It does not touch phenomenal consciousness, subjective continuity, or human identity.

## Stronger Next Step

The next experiment should remove hand-chosen candidate forms and train a compact recurrent predictor or predictive-state model on sequences:

```text
observation_t, action_t -> observation_{t+1}
```

Then probe whether hidden actuator state is:

- decodable from the learned state;
- causally necessary for prediction and control;
- more decodable as horizon, drift, and action-space size increase;
- stable across new tasks and perturbation regimes.
