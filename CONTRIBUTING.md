# Contributing to SelfState

SelfState is an independent computational research program. Contributions are welcome when they improve falsifiability, reproducibility, mathematical precision, benchmark quality, or external review.

A contribution should not increase the apparent strength of a claim merely by adding reports, scenarios, interface layers, or metrics. The standard is whether it makes the central hypothesis easier to test, reject, reproduce, or compare against alternatives.

## Start with the scientific status

Before proposing a change, read:

- [`SCIENTIFIC_STATUS.md`](SCIENTIFIC_STATUS.md)
- [`docs/05_formal_core_v2.md`](docs/05_formal_core_v2.md)
- [`docs/00_canonical_scientific_evidence.md`](docs/00_canonical_scientific_evidence.md)
- [`docs/14_hidden_state_boundary_attack.md`](docs/14_hidden_state_boundary_attack.md)

The current program does not claim consciousness. Contributions that interpret recurrence, language, memory, affective-control variables, or rich simulated behavior as evidence of subjective experience will not be accepted without a separate and defensible theory and evidence standard.

## Contribution types

Label pull requests with one primary type.

| Type | Purpose |
|---|---|
| `theory` | Correct definitions, propositions, proofs, predictions, or falsifiers |
| `experiment` | Add a controlled experiment with matched comparators |
| `learner` | Add a learned representation, controller, optimizer, or planner |
| `replication` | Reproduce an existing canonical result independently |
| `negative-result` | Preserve a failed, null, or limiting result |
| `statistics` | Improve uncertainty estimates, power, effect-size reporting, or split discipline |
| `reproducibility` | Add environment locks, containers, hashes, deterministic runners, or artifact checks |
| `review` | Critique a claim, comparator, metric, intervention, or interpretation |
| `demo` | Improve presentation without changing the scientific claim |
| `engineering` | Improve code quality, performance, tests, or maintenance |

Demo and engineering work should not be described as new scientific evidence unless it also satisfies the experimental requirements below.

## Claim discipline

Every report must state:

1. the narrow question;
2. the claim level;
3. what changed;
4. what did not change;
5. what the experiment can support;
6. what it cannot support;
7. the strongest observed limitation;
8. the next result that would falsify or materially strengthen the claim.

Use the claim ladder:

- **C0 — Implementation:** code and artifacts match the declared configuration;
- **C1 — Mechanism possibility:** a mechanism can produce the expected effect in a bounded benchmark;
- **C2 — Robust recovery:** the effect survives controls, seeds, and architectures;
- **C3 — Comparative advantage:** it improves control under matched resource budgets;
- **C4 — Attractor evidence:** independent learners converge on the same boundary as pressure increases;
- **C5 — Benchmark necessity:** the declared self-blind comparator class incurs a positive regret lower bound;
- **C6 — General claim:** transfer across substantially different systems and independent replication.

Do not use `pass` as a synonym for proof, significance, peer review, or general validity. A `pass` field is an internal acceptance gate defined by code.

## Required experimental design

A canonical experiment should include all applicable items below.

### Hypothesis and endpoint

- one primary hypothesis;
- one primary endpoint;
- secondary endpoints labeled as secondary;
- success and failure thresholds committed before the canonical evaluation;
- a rationale for each threshold.

### Comparator class

Declare exactly what the claim is relative to:

- observation access;
- history access;
- memory type and size;
- parameter count;
- training data;
- optimization steps;
- simulator calls;
- planning horizon;
- privileged labels;
- inference-time compute.

A self-state model beating a reactive policy is not sufficient when an unrestricted recurrent or predictive-state baseline is missing.

### Data and split discipline

Use distinct:

- training seeds;
- hyperparameter-selection or tuning seeds;
- held-out evaluation seeds.

Do not select architectures, checkpoints, thresholds, intervention directions, or report wording using the held-out evaluation set.

Where possible, add held-out:

- bodies or actuator mappings;
- sensor mappings;
- environments;
- task families;
- latent-state distributions.

### Boundary controls

A self-equivalent claim requires matched controls for the relevant failure modes.

At minimum consider:

- hidden external world state;
- persistent but control-irrelevant internal state;
- passive internal diagnostics;
- independent local hidden variables;
- irrelevant hidden variables;
- controllable external objects;
- detachable tools;
- other-agent state;
- shuffled or random auxiliary targets.

The same latent-learning machinery may be useful in all of these conditions. Classification as self-equivalent depends on the persistent agent/action boundary, not usefulness alone.

### Causal evidence

Decodability is not enough. Include one or more of:

- targeted feature-group ablation;
- latent subspace ablation discovered without test-label leakage;
- counterfactual latent editing;
- intervention on body or actuator dynamics;
- matched intervention on external or tool dynamics;
- mediation analysis where assumptions are defensible;
- policy-value change after intervention.

Report equal-norm random-direction controls and non-agent latent directions when editing learned state.

### Statistical reporting

Canonical results should report:

- every evaluation seed;
- mean and median where useful;
- standard deviation or robust spread;
- confidence or bootstrap intervals when justified;
- paired effect sizes for matched seeds;
- the distribution of failures, not only the average;
- multiple-comparison handling when many endpoints are tested;
- missing or invalid runs;
- all evaluated hyperparameter candidates.

A fixed threshold can remain as an engineering release gate, but it should be shown separately from statistical uncertainty.

### Reproducibility

Include:

- exact command;
- random seeds;
- dependency versions;
- hardware and accelerator details where material;
- raw machine-readable outputs;
- summary outputs derived from raw data;
- artifact hashes or a manifest;
- deterministic rerun instructions where possible;
- explicit nondeterminism notes where exact reproduction is not expected.

The report must not be the only record of the result.

## Negative results

Negative and partial results are first-class contributions.

Do not remove or obscure a negative result because a later implementation passes a different gate. Preserve:

- architecture failures;
- unstable seeds;
- ablations that improve rather than damage performance;
- weak causal edits;
- tune/evaluation reversals;
- failed distillation;
- label leakage;
- shortcut learning;
- non-transfer;
- low-pressure cases where recurrence is unnecessary.

A later positive report should explain whether it repairs the earlier failure or changes the benchmark, learner, budget, or criterion.

## Report template

New experimental reports should use this structure:

```markdown
# Report title

## Claim level
C1 / C2 / C3 / C4 / C5

## Question
One narrow question.

## Preregistered hypothesis
Primary endpoint, comparator, expected direction, threshold, and failure rule.

## What changed
Only the material changes from the previous canonical baseline.

## What did not change
Environment, data, privileged information, model family, and evaluation assumptions.

## Comparator and resource table
Observation, parameters, memory, data, optimization, simulator calls, and inference compute.

## Canonical command
Exact executable command.

## Evaluation design
Training, tuning, held-out seeds, environments, bodies, and interventions.

## Results
Raw per-seed table first; aggregate summaries second.

## Boundary controls
World, passive-internal, detachable-tool, local-hidden, and irrelevant-hidden controls.

## Causal interventions
Ablations or edits and matched controls.

## Interpretation
The narrow supported statement.

## Strongest limitation
The most damaging unresolved alternative explanation.

## Verdict
Internal acceptance gate, reported separately from statistical evidence.

## Artifacts
Raw data, summaries, configuration, logs, and hashes.
```

## Code standards

- Prefer small composable experiment modules over duplicated report-specific programs.
- Keep environment dynamics separate from policy and evaluator code.
- Keep train, tune, and evaluation seed lists explicit.
- Do not embed expected verdict labels into learner inputs or selection logic.
- Do not select restarts using the post-hoc boundary class being tested.
- Use typed configuration objects where practical.
- Validate artifact schemas before writing reports.
- Add tests for metrics and verdict calculations.
- Fail loudly on missing rows, duplicate seeds, or tune/evaluation overlap.
- Keep generated artifacts reproducible from code rather than hand-edited.

## Reviewing a pull request

A scientific review should answer:

1. Is the claim narrower than the evidence?
2. Is the strongest comparator present?
3. Are resource budgets actually matched?
4. Could scenario labels, feature grouping, privileged targets, or hand-designed candidate policies explain the result?
5. Is the proposed self factor distinguishable from world state or detachable tools?
6. Is the factor causally used, or only decodable?
7. Were tuning and evaluation separated?
8. Are all seeds and failures visible?
9. Does the report preserve prior negative evidence?
10. Would an independent reviewer know how to reproduce the result?

A valuable review may conclude that the implementation is sound but the scientific claim is too strong.

## External replication

Independent replication is a priority. A replication contribution should:

- identify the exact commit reproduced;
- use a clean environment;
- report hardware and dependency differences;
- rerun raw experiments rather than relying on checked-in summaries;
- compare generated artifact hashes where deterministic;
- report discrepancies without forcing agreement;
- avoid author-supplied manual corrections after the run begins.

The first clean external reproduction of a small canonical subset would improve the project's credibility more than another large environment expansion.

## Citation and licensing

Citation metadata is available in [`CITATION.cff`](CITATION.cff), and the research bibliography is in [`references.bib`](references.bib).

Repository visibility does not grant a reuse license. Until the owner adds an explicit license, contributors and users should not assume permission to redistribute or incorporate the code into other projects.
