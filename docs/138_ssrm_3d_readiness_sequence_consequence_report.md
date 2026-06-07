# SSRM-3D Readiness Sequence-Consequence Report

## Question

Report 137 showed that closed-loop recovery relabeling can repair survival in
the 72h readiness world, but it still does not produce knowledge transfer,
strong readiness, or stable ablation dependence.

This report asks the next narrower question:

```text
Does short multi-action consequence search reveal a readiness/control sequence
that solves the 72h world, and can a recurrent GRU absorb that sequence without
planner access?
```

## What Changed

This report adds:

- `experiments/ssrm_3d_readiness_sequence_consequence_optimizer.py`

The experiment keeps the Report 135 world mechanics and the Report 137 recovery
stack, then adds two layers:

- a bounded sequence-consequence optimizer that chooses short readiness plans
  by cloning the simulator and scoring candidate futures;
- a planner-free `sequence_gru` trained from teacher traces, recovery traces,
  and `896` student-created sequence labels.

The plan library contains generic multi-action pressure responses:

- `survival`
- `readiness`
- `build_tools`
- `culture`
- `ecology`
- `repair`

The sequence optimizer is allowed cloned simulator lookahead. The distilled GRU
is not.

## What This Does Not Claim

This is not deep reinforcement learning. It is not open-ended civilization. It
is not subjective consciousness. The sequence optimizer is a bounded planning
bridge, not a learned autonomous civilization.

The report separates two claims:

1. whether multi-step consequence search can identify the missing readiness
   behavior;
2. whether that behavior transfers into a planner-free recurrent controller.

Only the first claim passes.

## Canonical Command

```bash
python3 experiments/ssrm_3d_readiness_sequence_consequence_optimizer.py --behavior-train-seeds 20261211,20261212,20261213,20261214,20261215,20261216 --recovery-seeds 20261231,20261232,20261233 --sequence-seeds 20261301,20261302,20261303 --eval-seeds 20261321,20261322,20261323,20261324,20261325 --hours 72 --step-hours 0.10 --population 14 --epochs 52 --recovery-epochs 42 --sequence-epochs 38 --hidden-size 72 --plan-horizon-hours 2.4 --plan-commit-hours 0.8 --sample-interval-hours 1.2 --max-sequence-examples 900 --device cpu --trace-seed 20261321
```

## Training Result

The sequence labels add a small but high-pressure training set on top of the
Report 137 recovery stack:

| Pass | Architecture | Train accuracy | Weighted accuracy | Sequences | Steps | Extra examples |
|---|---|---:|---:|---:|---:|---:|
| `behavior` | `frame_mlp` | `0.251` | `0.251` | `108` | `71936` | `0` |
| `behavior` | `gru` | `0.249` | `0.249` | `108` | `71936` | `0` |
| `recovery_stage_1` | `gru` | `0.343` | `0.517` | `150` | `96165` | `24229` |
| `recovery_final` | `gru` | `0.423` | `0.639` | `192` | `124711` | `52775` |
| `sequence_distillation` | `gru` | `0.412` | `0.582` | `229` | `125607` | `896` |

The sequence optimizer's training rollouts all solve the world, but the
labeling set is still small and skewed toward the first sequence seed:

| Seed | Examples | Final alive | Final readiness | Knowledge transfer | Score |
|---|---:|---:|---:|---:|---:|
| `20261301` | `882` | `26` | `1.000` | `1.000` | `1.000` |
| `20261302` | `14` | `23` | `1.000` | `1.000` | `1.000` |
| `20261303` | `0` | `24` | `1.000` | `1.000` | `1.000` |

## Held-Out Result

The planner bridge works. The planner-free distillation fails.

| Controller | Maturation | Final alive | Final readiness | Knowledge transfer | Structural strain |
|---|---:|---:|---:|---:|---:|
| `designed` | `1.000` | `17.8` | `1.000` | `1.000` | `0.000` |
| `sequence_optimizer` | `1.000` | `23.0` | `1.000` | `1.000` | `0.002` |
| `recovery_gru` | `0.470` | `14.0` | `0.347` | `0.000` | `0.327` |
| `sequence_gru` | `0.287` | `0.0` | `0.465` | `0.000` | `0.036` |
| `behavior_gru` | `0.216` | `0.0` | `0.412` | `0.000` | `0.806` |
| `reactive` | `0.068` | `0.0` | `0.004` | `0.000` | `1.000` |

The sequence optimizer selects a mix of readiness, survival, culture,
build/tool, ecology, and repair plans. Across held-out seeds it reaches:

- maturation score `1.000`;
- mean final alive `23.0`;
- final readiness `1.000`;
- knowledge transfer `1.000`;
- final pest pressure `0.000`;
- final structural strain `0.002`.

The distilled GRU does not inherit that behavior. It increases some readiness
and building state, but the agents still die by the end and knowledge transfer
remains `0.000`.

The verdict is:

```text
supports_sequence_consequence_bridge = true
supports_planner_free_distillation = false
supports_ablation_specificity = false
verdict = partial_or_failed
```

## Ablation Boundary

The `sequence_gru` ablations are unstable:

| Ablation | Score loss |
|---|---:|
| `body` | `-0.182` |
| `infrastructure` | `-0.035` |
| `tools` | `-0.339` |
| `social_culture` | `-0.103` |
| `environment` | `0.067` |
| `readiness` | `-0.254` |
| `previous_action` | `-0.085` |

Only the environment ablation creates a positive score loss. Most ablations
improve the score, which means the planner-free GRU is not using those channels
as stable causal inputs.

## Interpretation

This is the clearest readiness result since Report 135:

- the richer 72h world is solvable;
- the missing control shape is multi-step consequence planning;
- planning must coordinate survival, readiness, culture, building/tools,
  ecology, and repair;
- one-step imitation and student-state relabeling do not transfer that behavior
  into a planner-free GRU.

That matters for the active simulation goal. The project now has a bounded
controller that can keep the 12h gate, let the world develop, pass knowledge
down, improve architecture/tools, and survive post-gate risk. But the controller
is still using explicit cloned lookahead, so it is not yet the mature learned
agent we want.

The next learning step should train directly from multi-step sequence outcomes,
not just first-action labels from the selected plan. The likely next boundary is
a value/process model over whole readiness windows: given a state and candidate
sequence, predict survival, readiness, knowledge transfer, development, and
strain/pest outcomes, then distill that scorer or train the policy against it.

## Artifacts

- [script](../experiments/ssrm_3d_readiness_sequence_consequence_optimizer.py)
- [training CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_training.csv)
- [recovery collection CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_recovery_collection.csv)
- [sequence collection CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_sequence_collection.csv)
- [plan evaluation CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_plan_eval.csv)
- [evaluation CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_summary.csv)
- [ablation CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_ablations.csv)
- [verdict CSV](../artifacts/ssrm_3d_readiness_sequence_consequence_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_readiness_sequence_consequence_trace.json)
- [results JSON](../artifacts/ssrm_3d_readiness_sequence_consequence_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_readiness_sequence_consequence_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_readiness_sequence_consequence_results.js)
