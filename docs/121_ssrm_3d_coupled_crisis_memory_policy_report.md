# SSRM-3D Coupled Crisis Memory Policy Report

## Question

Report 120 showed that adding a critic/value baseline to the sampled active
crisis policy did not solve coupled repair. The critic trained, but held-out
crisis behavior collapsed.

This report tests the next narrower claim:

```text
Does a recurrent hidden state carried across the active crisis window make
sampled crisis-policy learning solve held-out coupled repair?
```

The benchmark keeps the same hard setting:

- `96h` worlds;
- no major crisis before `12h`;
- randomized post-gate crisis timing, order, repetition, and initial pressure;
- learned base GRU;
- fixed-joint learned action-head baseline;
- no crisis profile name in memory-policy inputs;
- held-out eval seeds with targeted ablations.

## What Changed

The controller still samples from the same supplied candidate actions:

```text
none, sanitize, treat, scout, construct, social_repair, teach, learn
```

The new part is a recurrent crisis-memory policy. During an active crisis, the
policy carries a GRU hidden state through the sequence of agent decisions. When
the crisis ends, the full sampled crisis sequence is replayed through the GRU
and updated from the completed crisis return.

This directly tests the Report 120 hypothesis that the policy needed durable
crisis-window state rather than only per-step features. It is still not
open-ended civilization, not unsupplied action discovery, and not evidence of
subjective consciousness.

## Canonical Command

```bash
python3 experiments/ssrm_3d_coupled_crisis_memory_policy_controller.py --train-seeds 20260911,20260912,20260913 --tune-seeds 20261111,20261112 --eval-seeds 20261121,20261122,20261123 --hours 96 --step-hours 0.10 --population 14 --epochs 24 --hidden-size 64 --action-epochs 32 --action-hidden-size 64 --policy-epochs 4 --policy-hidden-size 64 --memory-epochs 5 --memory-hidden-size 64 --memory-learning-rate 0.003 --entropy-coef 0.008 --policy-temperature 1.0 --policy-bias-candidates 0.0,0.20,0.40,0.70,1.00 --device auto --trace-seed 20261121
```

## Training Result

The recurrent memory policy trained across completed crisis sequences:

```text
episodes = 15
training_crises = 90
memory_epochs = 5
parameters = 29640
mean_return = 1.473
return_std = 1.222
moving_baseline = 0.907
mean_sequence_length = 1221.6
mean_entropy = 1.614
final_loss = -3.235
device = mps
```

This confirms that recurrent crisis-window sequence learning executed. It does
not prove that the learned sequence transfers.

## Selection Result

Validation selected `policy_bias = 1.00`.

| Policy bias | Tune total | Tune crisis | Tune resolved | Tune coupled | Tune damage | Selected |
|---:|---:|---:|---:|---:|---:|---|
| `0.00` | `0.502` | `0.000` | `0.000` | `0.000` | `2.457` | no |
| `0.20` | `0.520` | `0.000` | `0.000` | `0.000` | `2.569` | no |
| `0.40` | `0.508` | `0.000` | `0.000` | `0.000` | `2.533` | no |
| `0.70` | `0.510` | `0.000` | `0.000` | `0.000` | `2.476` | no |
| `1.00` | `0.515` | `0.000` | `0.000` | `0.000` | `2.414` | yes |

All tune rows still have `0.000` crisis score, `0.000` resolved rate, and
`0.000` coupled response. Selection mostly chooses lower damage, not actual
coupled repair.

## Held-Out Result

The recurrent memory policy underperforms the simpler active-policy baseline.

| Controller | Total score | Crisis score | Resolved rate | Coupled response |
|---|---:|---:|---:|---:|
| fixed joint GRU | `0.773` | `0.528` | `0.800` | `0.795` |
| designed | `0.770` | `0.522` | `1.000` | `0.000` |
| active policy GRU | `0.520` | `0.000` | `0.178` | `0.147` |
| return-selected GRU | `0.520` | `0.000` | `0.111` | `0.028` |
| memory policy GRU | `0.517` | `0.000` | `0.000` | `0.000` |
| base GRU | `0.323` | `0.000` | `0.000` | `0.009` |
| frame MLP | `0.315` | `0.000` | `0.000` | `0.000` |
| reactive | `0.104` | `0.000` | `0.000` | `0.000` |

The verdict is:

```text
supports_active_policy_improvement = false
supports_return_baseline_improvement = false
supports_fixed_joint_improvement = false
supports_memory_policy_learning = false
supports_social_environment_dependency = false
verdict = partial_or_failed
```

## Interpretation

This is another useful negative boundary.

The recurrent state did not solve delayed coupled repair. It learned an
environment-leaning response pattern:

- memory-policy environmental response is `0.178`;
- memory-policy social response is `0.000`;
- memory-policy coupled response is `0.000`;
- active-policy coupled response was `0.147`;
- fixed-joint coupled response is `0.795`.

So the failure is now more specific. The learned policy can carry memory, and
it can act inside the active crisis window, but the return update still does
not preserve the two-channel coordination needed to resolve the crisis.

The current objective does not make the recurrent policy pay enough for
dropping the social channel while nudging environmental response. This is the
same underlying problem from the user-facing long-run simulation goal:
survival pressure is not enough unless the world and learning objective make
coordinated adaptation causally necessary and hard to route around.

## Ablation Boundary

Because the full memory policy has `0.000` crisis score and `0.000` coupled
response, targeted crisis dependency cannot pass.

| Ablation | Total loss | Crisis loss | Resolved loss | Coupled response loss |
|---|---:|---:|---:|---:|
| `body` | `0.037` | `0.000` | `0.000` | `0.000` |
| `infrastructure` | `0.162` | `0.000` | `0.000` | `0.000` |
| `tools` | `0.013` | `0.000` | `0.000` | `0.000` |
| `social_culture` | `0.258` | `0.000` | `0.000` | `0.000` |
| `environment` | `-0.003` | `0.000` | `0.000` | `0.000` |
| `previous_action` | `0.002` | `0.000` | `0.000` | `0.000` |

The total-score losses still show maturation dependencies. They do not show
successful crisis repair dependencies.

## Next Step

Do not claim recurrent crisis memory solved the coupled-crisis problem.

The next credible step should change the training pressure, not only the model
shape:

- train from counterfactual sequence rollouts where dropping either repair
  channel is explicitly penalized;
- add a two-channel process loss for maintaining both environmental and social
  repair activity during crises;
- use model-based search over repair sequences and distill the successful
  sequences into the recurrent policy;
- expose the policy to stronger held-out crises where one-channel response
  cannot lower damage enough to win selection;
- keep fixed-joint coordination as the comparison baseline until the learned
  policy has nonzero crisis score.

## Artifacts

- [script](../experiments/ssrm_3d_coupled_crisis_memory_policy_controller.py)
- [schedule CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_schedule.csv)
- [base training CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_base_training.csv)
- [action training CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_action_training.csv)
- [router selection CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_router_selection.csv)
- [active-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_active_policy_training.csv)
- [active-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_active_policy_selection.csv)
- [memory-policy training CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_memory_policy_training.csv)
- [memory-policy selection CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_memory_policy_selection.csv)
- [evaluation CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_coupled_crisis_memory_policy_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_coupled_crisis_memory_policy_trace.json)
- [results JSON](../artifacts/ssrm_3d_coupled_crisis_memory_policy_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_coupled_crisis_memory_policy_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_coupled_crisis_memory_policy_results.js)
