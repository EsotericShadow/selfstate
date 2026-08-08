# Literature Positioning and Novelty Boundary

## Purpose

This document positions SelfState against adjacent scientific literature without treating citation overlap as validation.

A source can:

- establish a formal baseline;
- demonstrate a related mechanism;
- motivate an experimental variable;
- provide a competing explanation;
- limit the interpretation of a result.

A source does **not** validate SelfState merely because it uses words such as self-model, body model, belief state, homeostasis, agency, embodiment, or active inference.

## Evidence labels

| Label | Meaning |
|---|---|
| F — Formal foundation | A mathematical framework or theorem that constrains the claim |
| E — Direct empirical precedent | A peer-reviewed experiment demonstrating a closely related mechanism |
| M — Mechanistic review | A review synthesizing evidence for a mechanism |
| C — Conceptual framework | A useful organizing theory that does not directly establish the repository's claim |
| A — Alternative explanation | A framework that may solve the task without an explicit self representation |

## 1. Partial observability and belief state

### Primary anchor

Kaelbling, Littman, and Cassandra, “Planning and Acting in Partially Observable Stochastic Domains,” *Artificial Intelligence* 101, 99–134 (1998). DOI: [10.1016/S0004-3702(98)00023-X](https://doi.org/10.1016/S0004-3702(98)00023-X). **F/A**

### What it establishes

A partially observable Markov decision process can be converted into a belief-state decision process. The posterior distribution over latent state is a sufficient state for optimal control when the model is known.

This supports the general premise that an agent may need memory or latent-state inference when the current observation is not Markov.

### What it does not establish

- that the relevant latent is agent state rather than world state;
- that the complete posterior is the minimal necessary representation;
- that a belief state is a self;
- that an explicit or interpretable self module will emerge;
- that the representation has any phenomenal or narrative properties.

### Consequence for SelfState

The POMDP baseline is a strong alternative explanation. A generic belief-state or recurrent controller may solve the benchmark without a separable agent-state factor. SelfState must show that a compressed or causally probed representation preserves an **agent-bounded decision quotient**, not merely that memory helps.

## 2. Predictive-state representations

### Primary anchor

Littman, Sutton, and Singh, “Predictive Representations of State,” *Advances in Neural Information Processing Systems 14* (2001). [Proceedings record](https://papers.nips.cc/paper/1983-predictive-representations-of-state). **F/A**

### What it establishes

State can be represented using predictions of future observations conditioned on future actions rather than by recovering a privileged hidden-state ontology.

This directly supports SelfState's action-conditioned-prediction pathway.

### What it does not establish

Predictive state does not identify which predictive dimensions are “self.” A predictive representation can solve the task while remaining distributed, nonsemantic, or organized around external variables.

### Consequence for SelfState

The relevant test is not whether a model named `self_state` performs well. It is whether a learned predictive representation contains a persistent factor whose causal dependence aligns with the continuing agent/action boundary and is reused across contexts.

## 3. Self-predictive state and history abstractions

### Primary anchor

Ni et al., “Bridging State and History Representations: Understanding Self-Predictive RL,” ICLR 2024. [Conference record](https://proceedings.iclr.cc/paper_files/paper/2024/hash/666c1861d709bd84e20b6e0e02a2c223-Abstract-Conference.html). **F/A**

### What it establishes

Several representation-learning approaches for MDP state and POMDP history can be understood through self-predictive abstractions. The paper analyzes objectives used to learn representations that predict their own future representations.

The word **self-predictive** in this literature refers to a representation predicting its future representation. It does not mean selfhood or an agent model.

### Consequence for SelfState

Terminology must be kept precise. SelfState's “self-equivalent” means agent-bounded control state; Ni et al.'s “self-predictive” describes a representation-learning property. The two may interact, but one does not imply the other.

This literature strengthens the generic-representation comparator and supports using history abstractions rather than requiring full latent reconstruction.

## 4. Learned belief representations

### Primary anchor

Wang et al., “Learning Belief Representations for Partially Observable Deep RL,” ICML 2023, PMLR 202:35970–35988. [Proceedings record](https://proceedings.mlr.press/v202/wang23p.html). **E/A**

### What it establishes

Compact reward-relevant belief representations can improve partially observable deep reinforcement learning, including tasks requiring information seeking and long-term memory.

### Consequence for SelfState

A learned belief representation is a serious baseline. SelfState should compare against compact reward-relevant belief learning and ask whether:

- the same representation transfers across agent-state tasks;
- a stable subspace aligns with the agent boundary;
- targeted intervention on that subspace selectively changes action value;
- world-state and detachable-tool conditions produce different boundary signatures.

Without those tests, a positive result supports belief-state learning rather than self-equivalent representation.

## 5. State abstraction and bisimulation

### Primary anchor

Zhang et al., “Learning Invariant Representations for Reinforcement Learning without Reconstruction,” ICLR 2021. [Preprint and paper record](https://arxiv.org/abs/2006.10742). **F/E/A**

### What it establishes

Bisimulation-based objectives can learn representations that retain task-relevant reward and transition distinctions while ignoring distractors. This provides a principled account of state compression for control.

### Consequence for SelfState

SelfState should be framed as a proposed **factorization of a control-sufficient abstraction**.

The central question becomes:

> When does the coarsest low-regret abstraction preserve a reusable quotient of agent-state belief, and when does it instead preserve world state, local history, or no persistent latent at all?

A representation should not be credited for reconstructing agent variables that do not affect reward, transitions, action availability, or transfer.

## 6. Causal representation learning

### Primary anchors

Schölkopf et al., “Toward Causal Representation Learning,” *Proceedings of the IEEE* 109(5), 612–634 (2021). DOI: [10.1109/JPROC.2021.3058954](https://doi.org/10.1109/JPROC.2021.3058954). **C/F**

Ahuja et al., “Interventional Causal Representation Learning,” ICML 2023, PMLR 202:372–407. [Proceedings record](https://proceedings.mlr.press/v202/ahuja23a.html). **F**

### What they establish

Causal representation learning studies the recovery of high-level causal variables from lower-level observations. Interventional data can improve identifiability under stated assumptions.

### What they do not establish

A causally identifiable latent factor is not automatically a self. External world state, tools, and other agents can also be causal latent factors.

### Consequence for SelfState

Post-hoc linear decodability is insufficient. The research program should use:

- interventions on body or actuator dynamics;
- matched interventions on external and detachable-tool dynamics;
- held-out intervention combinations;
- causal edit directions learned without evaluation labels;
- tests of whether the same factor mediates action effects and value across tasks.

The self-equivalent classification should be an intervention result, not a naming decision.

## 7. Continuous robotic self-modeling

### Primary anchors

Bongard, Zykov, and Lipson, “Resilient Machines Through Continuous Self-Modeling,” *Science* 314(5802), 1118–1121 (2006). DOI: [10.1126/science.1133687](https://doi.org/10.1126/science.1133687). **E**

Kwiatkowski and Lipson, “Task-Agnostic Self-Modeling Machines,” *Science Robotics* 4(26), eaau9354 (2019). DOI: [10.1126/scirobotics.aau9354](https://doi.org/10.1126/scirobotics.aau9354). **E**

Chen et al., “Fully Body Visual Self-Modeling of Robot Morphologies,” *Science Robotics* 7(68), eabn1944 (2022). DOI: [10.1126/scirobotics.abn1944](https://doi.org/10.1126/scirobotics.abn1944). **E**

### What they establish

Robots can learn models of their own morphology or action-effect structure and use those models for planning, task transfer, damage detection, and recovery. These are direct precedents for action-mediated, agent-bounded self-modeling.

### What they do not establish

- general identity or continuity;
- internal viability and commitments;
- a universal pressure toward self-model emergence;
- consciousness;
- superiority over all implicit recurrent alternatives.

### Consequence for SelfState

The body-drift and damage portions of SelfState should be presented as extensions and abstractions of established robotic self-modeling, not as the invention of computational self-modeling.

Potential novelty lies in testing a common boundary across:

- morphology and actuator state;
- internal viability;
- future capability and option preservation;
- interruption and commitment continuity;
- social obligations;
- multiple task contexts;
- explicit versus distributed learned representations.

That broader unification remains a hypothesis until cross-domain evidence is produced.

## 8. Forward models and sensorimotor attribution

### Primary anchors

Wolpert, Ghahramani, and Jordan, “An Internal Model for Sensorimotor Integration,” *Science* 269(5232), 1880–1882 (1995). DOI: [10.1126/science.7569931](https://doi.org/10.1126/science.7569931). **E/F**

Crapse and Sommer, “Corollary Discharge Across the Animal Kingdom,” *Nature Reviews Neuroscience* 9, 587–600 (2008). DOI: [10.1038/nrn2457](https://doi.org/10.1038/nrn2457). **M**

Straka, Simmers, and Chagnaud, “A New Perspective on Predictive Motor Signaling,” *Current Biology* 28(5), R232–R243 (2018). DOI: [10.1016/j.cub.2018.01.033](https://doi.org/10.1016/j.cub.2018.01.033). **M**

### What they establish

Action-conditioned forward predictions and copies of motor commands can help distinguish reafferent, self-generated sensory consequences from externally generated change and can coordinate sensorimotor systems.

### What they do not establish

Corollary discharge can operate without reflective selfhood, narrative identity, or consciousness. It is a minimal agency and error-attribution mechanism.

### Consequence for SelfState

The self/world attribution benchmark has a strong mechanistic precedent. The repository's claim should remain minimal:

> Action-effect state can be self-equivalent when it tracks the continuing agent's control interface and causally supports attribution, prediction, and adaptation.

The benchmark should include controllable external variables so that generic action correlation is not mistaken for an agent boundary.

## 9. Homeostatic reinforcement learning

### Primary anchor

Keramati and Gutkin, “Homeostatic Reinforcement Learning for Integrating Reward Collection and Physiological Stability,” *eLife* 3:e04811 (2014). DOI: [10.7554/eLife.04811](https://doi.org/10.7554/eLife.04811). **F/C**

### What it establishes

The paper develops a normative reinforcement-learning account in which reward depends on how outcomes alter internal physiological state relative to desired ranges. It connects learned behavior, anticipatory regulation, and physiological stability.

### What it does not establish

Homeostatic regulation is not sufficient for selfhood. A fixed controller can regulate an internal variable without forming a reusable agent representation.

### Consequence for SelfState

Internal viability variables should count as self-equivalent only when they are:

- hidden or partially observed;
- persistent;
- action and value relevant;
- inferred rather than supplied as an oracle;
- reused across decisions;
- causally active under ablation or editing.

The strongest test is not whether energy exists in the simulator, but whether a learned control-sufficient representation retains energy or integrity when the future policy requires it and discards it when it does not.

## 10. Interoception and body regulation

### Primary anchors

Petzschner et al., “Computational Models of Interoception and Body Regulation,” *Trends in Neurosciences* 44(1), 63–76 (2021). DOI: [10.1016/j.tins.2020.09.012](https://doi.org/10.1016/j.tins.2020.09.012). **M/C**

Sennesh et al., “Interoception as Modeling, Allostasis as Control,” *Biological Psychology* 167, 108242 (2022). DOI: [10.1016/j.biopsycho.2021.108242](https://doi.org/10.1016/j.biopsycho.2021.108242). **C/F**

Seth, “Interoceptive Inference, Emotion, and the Embodied Self,” *Trends in Cognitive Sciences* 17(11), 565–573 (2013). DOI: [10.1016/j.tics.2013.09.007](https://doi.org/10.1016/j.tics.2013.09.007). **C**

### What they establish

This literature formalizes internal-state inference, regulation, prediction, and anticipatory control. It provides a principled vocabulary for hidden internal state and future physiological needs.

### What it does not establish

Biological interoceptive theories do not show that an artificial agent needs a unified self variable. They may support distributed controllers, hierarchical predictive models, or task-specific regulation.

### Consequence for SelfState

The repository can test a narrower engineering question:

> Does one shared internal-state estimate outperform independent local regulators as the number of tasks and future decisions depending on the same hidden agent condition increases?

That question connects interoceptive control to the reuse-pressure hypothesis without importing claims about human feeling.

## 11. Markov blankets and active inference

### Primary anchor

Kirchhoff et al., “The Markov Blankets of Life: Autonomy, Active Inference and the Free Energy Principle,” *Journal of the Royal Society Interface* 15, 20170792 (2018). DOI: [10.1098/rsif.2017.0792](https://doi.org/10.1098/rsif.2017.0792). **C**

### What it contributes

Markov-blanket formalisms provide vocabulary for conditional boundaries among internal, sensory, active, and external states.

### Limit

A Markov blanket is not automatically an organism, agent, self, or conscious subject. Blanket structure may occur in systems where the stronger functional criteria are absent.

### Consequence for SelfState

Markov blankets may help specify candidate boundaries, but the repository should classify self-equivalent state through action mediation, value relevance, persistence, intervention, and reuse. Blanket membership alone is not evidence.

## 12. Minimal and embodied self concepts

### Primary anchor

Gallagher, “Philosophical Conceptions of the Self: Implications for Cognitive Science,” *Trends in Cognitive Sciences* 4(1), 14–21 (2000). DOI: [10.1016/S1364-6613(99)01417-5](https://doi.org/10.1016/S1364-6613(99)01417-5). **C**

### What it contributes

The literature distinguishes multiple meanings of self, including minimal embodied, narrative, and reflective forms. This is useful for preventing category errors.

### Consequence for SelfState

The repository should maintain a layered vocabulary:

1. action-effect or sensorimotor self-equivalence;
2. viability and capability control self;
3. continuity and ownership index;
4. narrative self;
5. phenomenal self.

Current experiments address the first three only in bounded computational forms. They do not test the fourth or fifth as human cognitive or experiential phenomena.

## 13. Option preservation and instrumental power

### Primary anchor

Turner et al., “Optimal Policies Tend To Seek Power,” NeurIPS 2021. [Proceedings record](https://proceedings.neurips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html). **F/C**

### What it establishes

Under stated environment symmetries and reward distributions, optimal policies can tend to preserve options or seek power over the environment.

### What it does not establish

Option preservation is not selfhood. A planner can preserve reachable states without a self concept, and power-seeking claims depend on formal assumptions.

### Consequence for SelfState

The repository can use option preservation as an endpoint only when future options depend on the continuing agent's own capability state. It should compare:

- agent capability;
- external resource availability;
- detachable tools;
- independent future conditions.

Only the first is evidence for an agent-state control factor.

## 14. What prior literature already establishes

SelfState should not claim novelty for the following:

- partial observability creates a need for memory or belief state;
- predictive representations can replace explicit hidden-state reconstruction;
- task-relevant state abstraction can improve control;
- causal interventions can identify latent factors under assumptions;
- robots can learn body or action-effect self-models;
- forward models can distinguish self-generated sensory consequences;
- internal physiological state can alter reward and action;
- multiple philosophical and cognitive meanings of self exist;
- option preservation can be instrumentally valuable.

## 15. Defensible novelty target

The strongest potentially novel research target is the conjunction below:

> Across matched partially observable tasks, constrained learners should increasingly retain a shared, causally agent-bounded decision quotient when one persistent hidden property of the continuing system is reused across action prediction, internal viability, future capability, commitments, recovery, and arbitration. The same learners should retain world-state factors when the reusable cause is external, prefer local inference when hidden causes are independent, and retain no persistent factor when hidden state is irrelevant.

This target is more specific than generic memory, body modeling, homeostasis, or predictive state.

It produces a measurable program:

1. vary reuse, horizon, observability, and drift pressure;
2. match representation and compute budgets;
3. learn without self labels or scenario labels;
4. locate learned causal factors by intervention;
5. distinguish body, world, tool, passive-internal, and other-agent variables;
6. measure control regret, compression, transfer, and causal policy use;
7. test convergence across architectures, seeds, optimizers, embodiments, and environments;
8. preserve failures and estimate convergence probability rather than reporting one canonical success.

## 16. Current relationship between literature and repository evidence

| Literature-derived expectation | Repository evidence | Status |
|---|---|---|
| Current observation should fail under partial observability | Recurrent and belief-like models beat frame baselines in several pressured stages | Supported in toy environments |
| Full posterior need not be represented | Formal Core v2 and Wolfram counterexample | Corrected theoretically |
| Task-relevant abstractions should discard irrelevant state | Irrelevant-hidden and low-pressure controls often reject recurrence | Partial support |
| World and agent latents both can be useful | World-drift and self-drift controls select different components | Supported in bounded tasks |
| Body self-modeling helps after damage or drift | Morphology/action-effect experiments and robotics literature align | Mechanism precedent; repository extension remains bounded |
| Internal state can define future value | Viability and pressured learned-control stages | Supported in simulation |
| Decodability is weaker than causal use | Learned-controller action edits remain small in key reports | Explicit limitation |
| Compression alone cannot identify causal semantics | World-state reuse and boundary attacks | Supported limitation |
| Strong emergence requires robustness across learners | Architecture and seed sweeps are mixed | Attractor claim remains open |
| Planning competence need not distill into recurrent policy | Readiness sequence optimizer succeeds while GRU distillation fails | Strong negative result |

## 17. Literature-use rules for future reports

1. Cite a paper for the exact mechanism or formal result it supports.
2. State what the paper does **not** support.
3. Prefer primary papers for technical claims and reviews for field synthesis.
4. Do not cite consciousness theories to upgrade a control result into a consciousness claim.
5. Treat adjacent methods as comparators, not endorsements.
6. Distinguish replicated literature facts from repository-generated simulation results.
7. Add new references to [`references.bib`](../references.bib) and record their role in this map.
8. When sources disagree, preserve the disagreement and design a discriminating experiment.

## Bottom line

The literature makes the core idea scientifically plausible, but plausibility is not legitimacy. Legitimacy will come from showing that the proposed agent-boundary factor is:

- required relative to serious comparator classes;
- learned without semantic shortcuts;
- causally used rather than merely decoded;
- separated from world state and tools;
- robust across seeds, architectures, and environments;
- reproducible by people outside the project.

The repository is best presented as a rigorous, unusually broad **research program of precursors** toward that result—not as a completed theory of why a self exists.
