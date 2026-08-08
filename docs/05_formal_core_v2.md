# Formal Core v2: Decision Sufficiency and Self-Equivalent State

## Status

This document is the normative formal statement for the research program as of 2026-08-07. It corrects the overly broad posterior-necessity wording in [`05_formal_core.md`](05_formal_core.md) while preserving the repository's central empirical question.

The theory concerns representation and control. It does not define or detect consciousness.

## 1. Controlled process

Let the latent state of a partially observable controlled process be

\[
X_t = (E_t, A_t),
\]

where:

- \(E_t\) is external world state;
- \(A_t\) is state of the continuing controlled system, potentially including morphology, actuator and sensor properties, energy, damage, competence, memory-relevant commitments, policy parameters, and restore or branch state;
- \(U_t\) is the selected action;
- \(O_t\) is the observation;
- \(R_t\) is reward, cost, viability, or another declared control objective.

A general controlled transition model is

\[
(E_{t+1},A_{t+1}) \sim P(\cdot\mid E_t,A_t,U_t),
\]

\[
O_t \sim P(\cdot\mid E_t,A_t),
\qquad
R_t \sim P(\cdot\mid E_t,A_t,U_t).
\]

The interaction history before choosing \(U_t\) is

\[
H_t=(O_{1:t},U_{1:t-1},R_{1:t-1}).
\]

The complete Bayesian belief state is

\[
b_t(x)=P(X_t=x\mid H_t),
\]

with agent-state marginal

\[
b^A_t(a)=P(A_t=a\mid H_t).
\]

For a known POMDP, the complete belief state is a sufficient Markov state for optimal control. That fact does **not** establish that the full belief is the smallest necessary representation, and it does not make every latent state a self.

## 2. Representations of history

A controller may replace the full history with a representation

\[
Z_t=\phi(H_t).
\]

Several different sufficiency standards must be kept separate.

### 2.1 Predictive sufficiency

A representation is predictive-sufficient for a declared family of future action sequences if histories mapped to the same \(z\) induce the same relevant distribution of future observations and rewards under those sequences.

Informally:

\[
\phi(h)=\phi(h')
\Rightarrow
P(Y_{t:\,t+k}\mid h,u_{t:\,t+k})
=
P(Y_{t:\,t+k}\mid h',u_{t:\,t+k}),
\]

for the future variables \(Y\), horizons, and action sequences included in the claim.

This is related to predictive-state representations. It does not require recovery of named latent variables.

### 2.2 Value sufficiency

Let

\[
Q^*(h,u)
\]

be the optimal action value after history \(h\). A representation is value-sufficient if

\[
\phi(h)=\phi(h')
\Rightarrow
Q^*(h,u)=Q^*(h',u)
\quad \text{for every }u.
\]

This is stronger than is required merely to select an optimal action.

### 2.3 Policy sufficiency

Define the optimal-action set

\[
\mathcal U^*(h)=\operatorname*{arg\,max}_{u}Q^*(h,u).
\]

A representation is policy-sufficient if each representation cell admits at least one action that is optimal for every history in that cell:

\[
\bigcap_{h:\phi(h)=z}\mathcal U^*(h)\neq\varnothing
\quad \text{for every reachable }z.
\]

Equivalently, there exists a policy \(\pi(u\mid z)\) that is optimal for all histories represented by \(z\).

Policy sufficiency is the weakest of these three standards. Two beliefs may differ substantially while remaining policy-equivalent.

## 3. Why the full posterior is not generally necessary

Consider a one-step decision problem with hidden agent state

\[
A\in\{0,1\},
\qquad
p=P(A=1\mid H).
\]

The action set is \(\{0,1\}\), and reward is one exactly when the selected action equals \(A\). Then

\[
Q(p,0)=1-p,
\qquad
Q(p,1)=p.
\]

Every belief with \(p<1/2\) has optimal action 0, and every belief with \(p>1/2\) has optimal action 1. The beliefs \(p=0.10\), \(0.25\), and \(0.40\) are different posteriors but belong to the same optimal-decision class.

Therefore, a binary statistic

\[
Z=\mathbb 1[p>1/2]
\]

is policy-sufficient even though it does not reconstruct the full posterior.

This counterexample establishes:

> Full posterior recovery can be sufficient without being necessary.

The correct research target is a minimal or compressed **decision-sufficient quotient** of history, not necessarily a complete posterior or an interpretable self variable.

A Wolfram Language reproduction is provided in [`experiments/decision_sufficiency_wolfram.wl`](../experiments/decision_sufficiency_wolfram.wl).

## 4. Weak necessity of agent-state distinctions

The useful necessity claim is conditional and representation-relative.

### Proposition 1 — merged conflicting histories incur regret

Let \(\psi(H_t)\) be any proposed representation. Suppose two reachable histories \(h_1,h_2\) satisfy

\[
\psi(h_1)=\psi(h_2)
\]

but have disjoint optimal-action sets:

\[
\mathcal U^*(h_1)\cap\mathcal U^*(h_2)=\varnothing.
\]

Then no policy measurable only with respect to \(\psi(H_t)\) can be optimal at both histories.

#### Proof

A \(\psi\)-measurable policy must use the same action distribution after \(h_1\) and \(h_2\), because both histories produce the same representation. An action distribution supported only on optimal actions for \(h_1\) cannot also be supported only on optimal actions for \(h_2\) when the optimal-action sets are disjoint. Therefore the policy is suboptimal at one or both histories. ∎

### Regret form

For histories \(h_i\) merged into one representation cell \(z\), with conditional weights \(w_i=P(H_t=h_i\mid Z_t=z)\), the minimum deterministic regret attributable to the merge is

\[
\mathcal R(z)
=
\min_u
\sum_i w_i
\left[V^*(h_i)-Q^*(h_i,u)\right].
\]

If the histories have disjoint optimal-action sets and strictly positive action gaps, then \(\mathcal R(z)>0\).

This quantity provides a direct benchmark target. A representation is not merely declared insufficient; its merged histories produce measurable control regret.

### Proposition 2 — conditional agent-state necessity

Let \(\psi_E(H_t)\) preserve all world information admitted by the comparator class while deliberately discarding distinctions in hidden agent state. Suppose there exist histories \(h_1,h_2\) such that:

1. \(\psi_E(h_1)=\psi_E(h_2)\);
2. the histories are matched on the external variables relevant to the declared decision;
3. their beliefs about \(A_t\) differ;
4. those differences induce disjoint optimal-action sets.

Then every policy based only on \(\psi_E\) is suboptimal on at least one of the histories. Any optimal representation must preserve some information that distinguishes the decision-relevant agent-state cases.

This proposition supports only the following conclusion:

> Some information statistically equivalent to the relevant agent-state distinction is necessary for optimal control in that benchmark.

It does not imply that the information is explicit, localized, semantic, complete, reportable, or conscious.

## 5. Information diagnostic

Let \(D_t\) denote the optimal-decision class required at time \(t\), and let \(Z^E_t\) denote the world-information component admitted by the comparison. If the controller's representation \(Z_t\) determines \(D_t\), then conditional data processing gives

\[
I(B^A_t;Z_t\mid Z^E_t)
\ge
I(B^A_t;D_t\mid Z^E_t),
\]

where \(B^A_t\) is the random variable corresponding to the agent-state belief.

Interpretation:

- when the correct decision remains statistically dependent on agent-state belief after conditioning on world information, a sufficient representation cannot be conditionally independent of all agent-state information;
- the bound concerns decision information, not complete reconstruction;
- mutual information alone does not establish an agent boundary or selfhood;
- spurious correlations, label leakage, and common causes can produce decodability without causal use.

The required follow-up is intervention or targeted ablation.

## 6. From decision-sufficient state to self-equivalent state

A decision-sufficient representation is not automatically self-equivalent. The term is applied only to a factor or subspace \(Z^A_t\subseteq Z_t\) that passes all declared boundary tests.

### 6.1 Agent boundary

The candidate must track a state of the continuing controlled system rather than merely an external variable.

Evidence should compare matched interventions on:

- persistent body or actuator state;
- external world state;
- passive internal diagnostics;
- detachable tools;
- controllable external objects;
- other agents' state.

A variable is not agent-bounded merely because it is physically internal, correlated with action, or controllable.

### 6.2 Persistence

The variable must affect more than one observation-action cycle or support transfer across contexts. A transient motor command, one-frame sensor artifact, or task-local label is insufficient.

### 6.3 Action mediation

The candidate should alter at least one of:

\[
P(X_{t+1}\mid X_t,U_t),
\qquad
P(R_t\mid X_t,U_t),
\qquad
\mathcal U_{\mathrm{available}}(X_t),
\]

in a way tied to the continuing system's action interface, cost, or capability.

### 6.4 Control or value relevance

Conditioning on the candidate should improve a declared endpoint such as return, survival, recovery, transfer, calibration, option preservation, or commitment coherence. Randomizing or removing it should create a selective loss in tasks that require agent state but not in matched world-only controls.

### 6.5 Counterfactual activity

Editing the candidate in the direction corresponding to changed energy, damage, capability, ownership, or commitment state should predictably change action values, future-viability estimates, or policy choice.

Decodability without intervention sensitivity is evidence that information is present, not that it is used.

### 6.6 Cross-context reuse

The same candidate should support more than one decision context, horizon, task, or environment. A separate local probe for each task does not establish a reusable self-equivalent abstraction.

### 6.7 Continuity extension

Identity-like continuity additionally requires an ownership relation over time. A continuity representation should determine which memories, commitments, social records, tools, event-log positions, restore records, and branch states belong to the same continuing controlled process.

This is stronger than minimal sensorimotor self-equivalence and weaker than narrative or phenomenal selfhood.

## 7. Compression hypothesis

The repository's compression claim should be expressed as an optimization hypothesis rather than a universal assertion.

Let a learner jointly choose a representation \(\phi\) and policy \(\pi\). One generic rate-distortion-style objective is

\[
\min_{\phi,\pi}
\quad
\mathbb E[\operatorname{Regret}(\pi\circ\phi)]
+
\beta\,\mathcal C(Z_t),
\]

where \(\mathcal C\) may be description length, state dimension, parameter cost, or an information bottleneck such as \(I(H_t;Z_t)\).

The **self-state attractor hypothesis** is:

> Across a declared family of partially observable tasks, increasing reuse, horizon, agent drift, and action/value dependence should increase the frequency with which low-regret compressed representations retain a shared quotient of agent-state belief that passes the operational boundary tests.

This predicts a gradient, not an all-or-nothing transition.

### 7.1 Reuse-pressure sanity check

Suppose a reusable latent requires \(m\) bits. Encoding it independently in each of \(k\) contexts costs approximately

\[
L_{\mathrm{local}}=km.
\]

A shared encoding with \(c\) bits of interface per context costs

\[
L_{\mathrm{shared}}=m+kc.
\]

Sharing is cheaper when

\[
m+kc<km,
\]

or

\[
k(m-c)>m.
\]

When \(c<m\), the threshold is

\[
k>\frac{m}{m-c}.
\]

This is only a minimum-description-length sanity check. It predicts why reuse can reward a shared latent, but it does not predict that the latent will be agent-bounded. A persistent external world variable has the same compression advantage. The causal boundary test remains indispensable.

### 7.2 Horizon pressure

If one persistent agent-state estimate informs many future decisions, its acquisition cost may be amortized over the horizon. If each future decision depends on an independent latent, a shared estimate should lose to local inference. If the persistent latent is external, the selected representation should be classified as world state.

### 7.3 Partial-observability pressure

When noisy observations reveal one persistent agent variable, filtering should become more useful as cue reliability and future reuse increase. The claim fails if generic recurrence or world-state filtering provides the same value with equal complexity and no causally separable agent factor.

## 8. Attractor evidence standard

The word **attractor** should be used only when convergence is measured across independent learning systems.

A strong attractor result requires:

1. multiple architecture families;
2. multiple random seeds;
3. multiple optimizers or credit-assignment methods;
4. matched parameter, memory, data, and compute budgets;
5. no self labels, scenario labels, supplied source directions, or boundary-aware restart selection;
6. held-out embodiments and environments;
7. world, passive-internal, detachable-tool, local-hidden, and irrelevant-hidden controls;
8. post-training boundary interventions;
9. increasing convergence probability as the predicted pressures increase;
10. raw failure distributions rather than only selected canonical runs.

A successful trained controller is not sufficient. High return, recurrence, decodability, and one positive ablation are each weaker than stable causal boundary convergence.

## 9. Comparator classes

Claims of necessity are always relative to a declared comparator class. At minimum, experiments should compare:

- reactive observation-only policies;
- frame-only feed-forward policies;
- unrestricted recurrent or external-memory policies;
- predictive-state or belief-state learners;
- structured self-state bottlenecks;
- task-local probes;
- shared world-state representations;
- matched-capacity representations with shuffled or irrelevant auxiliary targets;
- model-based planners where relevant.

The claim “self-state is necessary” is invalid unless the excluded policy class, observation access, memory budget, compute budget, and approximation tolerance are stated.

## 10. Approximate sufficiency and practical endpoints

Real learned controllers will rarely be exactly optimal. Let \(\epsilon\ge0\). A representation is \(\epsilon\)-policy-sufficient over a distribution of histories if the best policy using that representation has expected regret at most \(\epsilon\).

For a representation family \(\Phi\), define

\[
\epsilon^*(\Phi)
=
\inf_{\phi\in\Phi,\pi}
\mathbb E\left[V^*(H_t)-Q^*(H_t,\pi(\phi(H_t)))\right].
\]

A benchmark-level necessity result can then be stated as a lower bound:

\[
\epsilon^*(\Phi_{\mathrm{self\mbox{-}blind}})
-
\epsilon^*(\Phi_{\mathrm{agent\mbox{-}aware}})
\ge \delta>0,
\]

under matched resource constraints.

This is more defensible than claiming metaphysical or architecture-independent necessity. It says that a declared self-blind comparator class pays at least \(\delta\) additional regret in the benchmark.

## 11. Experimental implications

The formal core produces concrete tests.

### Test A — matched self/world latent

Construct two regimes with identical latent cardinality, persistence, observation noise, and reward impact. In one, the latent changes the agent's action effects; in the other, it changes external world dynamics. A discovered representation should support control in both, but only the first should pass the agent-boundary intervention.

### Test B — conflicting-history pairs

Generate pairs of histories matched on world information but differing in hidden agent-state belief. Estimate whether their optimal-action sets are disjoint and measure the regret created when a representation merges them.

### Test C — generic-memory attack

Give an unrestricted recurrent baseline the same parameter count, training data, action access, and compute. The self-attractor claim weakens if it matches transfer and recovery while no stable agent-bounded factor can be found or causally edited.

### Test D — reuse gradient

Increase the number of tasks that share one hidden agent variable while keeping total training data controlled. Compare shared self-state, shared world-state, and task-local inference. The selected factor should follow the causal location of the reusable variable.

### Test E — held-out embodiment

Train across a family of bodies or actuator mappings and evaluate on unseen bodies. A reusable agent-state representation should transfer better than memorized body identity or scenario labels.

### Test F — causal edit

Identify a candidate agent-state direction without using the test labels, intervene on it, and measure changes in action value and policy. Include equal-norm random directions, world-state directions, and detachable-tool directions.

### Test G — continuity necessity

Construct restore or fork cases where weights, generic memory, body state, commitments, social history, and branch identity are independently corrupted. Measure which record components are required to preserve declared continuation behavior.

## 12. Strong falsifiers

The central hypothesis is weakened if:

- a self-blind representation is equally compact and equally effective across the declared task family;
- generic recurrent state preserves optimal decisions with no stable, causally active agent-state quotient;
- external hidden variables reproduce the same claimed boundary evidence;
- intervention on the proposed self factor does not alter action-centered counterfactuals;
- causal effects disappear under new seeds, architectures, optimizers, bodies, or worlds;
- learned factors depend on self labels, scenario identifiers, oracle source directions, or evaluation-set selection;
- the reusable latent follows task-local correlations rather than the continuing agent boundary;
- explicit self-state helps only by increasing parameter count, observation access, or training signal;
- low-pressure controls recruit the same machinery without a control job;
- the claimed continuity result is reproduced by a smaller non-identity record.

## 13. Claim boundaries

The strongest warranted form of the current thesis is:

> In bounded partially observable control problems, when hidden properties of the continuing controlled system change the consequences or value of actions across time and contexts, successful compressed controllers may need to preserve decision-relevant information about those properties. A representation counts as self-equivalent only when causal tests locate that information at the persistent agent/action boundary and show reuse across control problems.

The following statements are not established:

- every intelligent system needs a self;
- every recurrent state is a self;
- the full posterior over agent state is necessary;
- compression alone identifies selfhood;
- high return proves self-model emergence;
- self-equivalent control state implies consciousness;
- the current simulator establishes a general law of biological or artificial identity.

## 14. Literature anchors

The formal positioning is grounded in:

- Kaelbling, Littman, and Cassandra on POMDP planning and belief state;
- Littman, Sutton, and Singh on predictive representations of state;
- Ni et al. on self-predictive state and history abstractions;
- Wang et al. on learned compact belief representations for partially observable deep RL;
- Zhang et al. on bisimulation-based task-relevant representations;
- Schölkopf et al. and Ahuja et al. on causal representation learning and interventional identification;
- Bongard, Zykov, and Lipson; Kwiatkowski and Lipson; and Chen et al. on robotic self-modeling and damage recovery;
- Wolpert, Ghahramani, and Jordan; Crapse and Sommer; and Straka et al. on forward models and predictive motor signaling;
- Keramati and Gutkin, Petzschner et al., and Sennesh et al. on homeostatic, interoceptive, and allostatic control.

Machine-readable references are in [`references.bib`](../references.bib).
