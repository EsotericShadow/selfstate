# Scientific Status

**Audit date:** 2026-08-07  
**Repository status:** Independent computational research program; not yet externally peer reviewed or independently replicated.

## Research question

> Under what conditions does an adaptive controller benefit from representing the continuing system that is acting, rather than representing only external world state or undifferentiated history?

The repository studies a deliberately narrow, functional concept of self-representation. It does **not** test consciousness, subjective experience, personhood, or a metaphysically enduring self.

The working hypothesis is:

> In partially observable control problems, a reusable representation of hidden agent state becomes advantageous when the same persistent properties of the controlled system mediate action effects, value, future options, adaptation, or continuity across multiple decisions and contexts.

The term **self-equivalent state** is reserved for a learned or designed representation that passes operational boundary tests. Mere recurrence, memory, internal location, decodability, or hidden-state usefulness is not sufficient.

## Scientific positioning

This program sits at the intersection of several established research areas:

1. **POMDP belief and predictive-state representations.** Under partial observability, useful state can be represented by a belief over latent state or by action-conditional predictions of future observations. The full belief state is a sufficient representation for optimal POMDP control, but it is not generally the smallest necessary representation.
2. **State abstraction and bisimulation.** Reinforcement-learning representations can discard distinctions that do not change rewards, transitions, values, or optimal decisions. This is the correct formal baseline for asking whether an agent-specific factor is retained under compression.
3. **Robotic self-modeling and body schema.** Robots can learn models of their own morphology or action-effect dynamics and use them for planning, transfer, damage detection, and recovery.
4. **Forward models, efference copy, and corollary discharge.** Biological control systems use action-conditioned predictions to distinguish self-generated sensory change from external change.
5. **Interoception, homeostasis, and allostasis.** Internal physiological state can define control objectives, alter action value, and require anticipatory regulation over time.
6. **Causal representation learning.** Interventions and invariances can help distinguish causal latent factors from arbitrary predictive encodings.

The repository's proposed contribution is not the claim that hidden state, body models, belief states, or homeostatic control exist. Those are established. The narrower proposed contribution is this:

> When representation capacity is constrained, decision-sufficient state may preferentially factor along a persistent agent boundary if one hidden agent-state estimate is repeatedly reused across action prediction, viability, option preservation, commitments, recovery, and arbitration.

That is an empirical **attractor hypothesis**, not a theorem.

## Formal correction

The older formal core states too broadly that any Bayes-optimal long-horizon policy must encode information equivalent to the full posterior over hidden agent state.

That wording is not generally valid. Distinct posterior distributions can induce the same optimal action. Therefore:

- the full posterior is often **sufficient**;
- the full posterior is not generally **necessary**;
- an optimal controller need preserve only the distinctions required for prediction, value, or action selection in the task family under study.

The normative statement is now:

> If a representation merges histories that are matched on relevant world information but require disjoint optimal actions because of different hidden agent-state beliefs, then no policy using only that representation can be optimal on both histories.

This is a weak but defensible necessity claim: some **decision-relevant information** about agent state must be preserved in that setting. It does not require explicit variables, semantic labels, complete state reconstruction, reportability, or consciousness.

See [Formal Core v2: Decision Sufficiency and Self-Equivalent State](docs/05_formal_core_v2.md).

## Operational boundary

A candidate latent variable counts as self-equivalent in this program only when evidence supports all of the following:

| Criterion | Required evidence |
|---|---|
| Agent-bounded | Matched interventions distinguish a continuing body/control variable from an external world or detachable-tool variable. |
| Persistent | The variable remains useful across more than one observation-action cycle. |
| Action-mediated | Changing it changes action effects, available actions, action costs, or capability. |
| Control/value relevant | Conditioning on it improves reward, survival, recovery, transfer, option preservation, or commitment coherence. |
| Counterfactually active | Intervening on the learned representation changes an action-centered prediction or policy in the expected direction. |
| Reused | The same representation transfers across multiple decisions, horizons, or contexts. |

Identity-like continuity requires additional evidence that the representation binds owned memories, commitments, social history, restore state, or branch history across interruption. Narrative or phenomenal selfhood is outside the current scope.

## Current evidence status

The report count is not the evidence strength. Many numbered reports are implementation iterations, benchmark extensions, browser demonstrations, or review-workflow hardening. The canonical scientific evidence is curated separately in [Canonical Scientific Evidence](docs/00_canonical_scientific_evidence.md).

| Claim | Current status | Reason |
|---|---|---|
| Useful hidden state can improve partially observable control | Established background; reproduced in toy experiments | This follows from POMDP, belief-state, predictive-state, and recurrent-control literature. It is not a novel selfhood result. |
| Agent-state can be distinguished from hidden world state with matched controls | Supported in several toy benchmark families | The repository includes world-state, passive-diagnostic, detachable-tool, local-hidden, and irrelevant-hidden controls. |
| Learned recurrent state carries decodable agent variables under pressure | Supported in bounded simulations | Observer and controller reports recover energy, integrity, mobility, and sensor capability from recurrent state. |
| Recurrent control can outperform frame-only control when agent state matters over time | Supported in bounded simulations | Several stages show large gains under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure. |
| Learned self-state is robustly and causally editable | Partial | Some observer edits move future-viability predictions, but direct policy-action swings remain weak in important learned-controller results. |
| The same boundary emerges reliably across architectures and random seeds | Mixed | Some architecture and budget sweeps converge; other hard-return, seed, tool-boundary, social, and no-leak tests remain partial. |
| Compression reliably discovers an agent boundary | Not established | Compression can discover reusable world state as readily as reusable agent state. Boundary interventions remain necessary. |
| Self-equivalent state is a general optimization attractor | Open | The repository has precursors, not a domain-general or optimizer-independent law. |
| Full posterior recovery is necessary | Rejected as stated | Only policy-, value-, or prediction-sufficient distinctions are generally required. |
| Consciousness or subjective experience has been produced or detected | Not tested | No current experiment measures or establishes phenomenal consciousness. |
| External replication | Not documented | The current evidence is generated within this repository and simulator family. |

## Strong positive and negative results

A credible research program must preserve negative evidence rather than treating every iteration as progress.

### Positive evidence

- Recurrent observer state becomes more useful than a stateless frame representation when hidden energy, body drift, delayed options, commitments, arbitration, and social pressure accumulate.
- Learned recurrent controllers outperform frame-only controllers in several pressured SSRM-3D stages while retaining decodable agent-state information.
- A return-selected hidden-regime controller improves over its fixed-bias recurrent baseline and reactive control, with specific losses after regime-signal, infrastructure, and body-state ablations.
- World-state and irrelevant-hidden controls often reject an agent-state interpretation, supporting the anti-tautology boundary.

### Limiting and negative evidence

- Low-pressure spatial control does not require recurrent self-state.
- Decodability alone does not produce strong causal action changes.
- Some architectures and seeds fail to recover the proposed boundary even when task return is high.
- Detachable tools remain a difficult boundary case because useful external variables can be controllable and persistent.
- Social/culture ablations are unstable in several learned-controller experiments.
- In the 72-hour readiness benchmark, explicit short-horizon consequence search solves the world, while planner-free recurrent distillation fails, reaches zero final survivors, and exhibits unstable ablations.
- Many later reports improve auditability, browser continuity, or handoff workflow without adding scientific evidence for self-equivalent representation.

## Claim ladder

Every result should be labeled at one of these levels:

| Level | Meaning |
|---|---|
| C0 — Implementation | The code runs and the artifact matches the declared configuration. |
| C1 — Mechanism possibility | A specified mechanism can produce the predicted effect in a bounded benchmark. |
| C2 — Robust recovery | The effect survives matched controls, multiple seeds, and multiple architectures. |
| C3 — Comparative advantage | The representation improves control under matched parameter, data, and compute budgets. |
| C4 — Attractor evidence | Independent learners reliably converge on the same agent-boundary abstraction as pressure increases. |
| C5 — Benchmark necessity | Every policy in a declared comparator class incurs measurable regret without the relevant agent-state distinction. |
| C6 — General or biological claim | The result transfers across substantially different environments, embodiments, learning systems, and independent replications. |

The repository currently contains substantial C1 evidence, selected C2/C3 evidence, and incomplete precursors toward C4/C5. It contains no C6 evidence and makes no consciousness claim.

## Statistical and methodological standard going forward

An internal `pass` verdict means that a predeclared engineering acceptance threshold was crossed. It is not a p-value, confidence level, peer-review decision, or proof of a theory.

New canonical experiments should include:

- hypotheses, primary endpoints, comparator classes, and thresholds committed before the canonical result;
- distinct training, tuning, and held-out evaluation seeds;
- raw per-seed results, effect sizes, uncertainty intervals, and failure distributions;
- matched parameter, observation, data, memory, and compute budgets;
- world-state, passive-internal, detachable-tool, local-hidden, and irrelevant-hidden controls;
- post-training causal interventions rather than decodability alone;
- held-out bodies, sensor mappings, environments, and task families;
- negative and null results in the canonical index;
- exact commands, dependency versions, deterministic seeds where possible, and machine-readable artifacts.

See [Contributing](CONTRIBUTING.md) for the proposed external-review protocol.

## What would falsify the central hypothesis?

The attractor hypothesis should be weakened or rejected if, under matched budgets and across increasingly difficult agent-state pressures:

1. generic history or recurrent state matches structured or discovered agent-state representations without a stable agent-bounded factor;
2. hidden external variables produce the same effects and cannot be separated by intervention;
3. learned agent-state is decodable but its ablation or editing does not change control;
4. the advantage disappears on held-out bodies, environments, or task families;
5. convergence depends on one architecture, one optimizer, one seed family, label leakage, or hand-designed policy classes;
6. compression consistently favors task-local or world-state solutions instead of a reusable agent-state quotient;
7. an equally compact self-blind representation preserves optimal value and transfer across the declared task family.

## Canonical entry points

- [Formal Core v2](docs/05_formal_core_v2.md)
- [Canonical Scientific Evidence](docs/00_canonical_scientific_evidence.md)
- [Original Research Brief](docs/01_research_brief.md)
- [Experimental Program](docs/03_experimental_program.md)
- [Hidden-State Boundary Attack](docs/14_hidden_state_boundary_attack.md)
- [Curated Bibliography](references.bib)
- [Wolfram Decision-Sufficiency Checks](experiments/decision_sufficiency_wolfram.wl)

## Citation and reuse

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). No software or content license should be inferred from repository visibility; a license must be selected and added explicitly by the repository owner before third-party reuse terms are considered clear.
