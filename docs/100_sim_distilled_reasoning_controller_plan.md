# Sim-Distilled Reasoning Controller Plan

## Purpose

This document records the long-term direction downstream of the SSRM-3D simulation work.

The goal is not to make the highest-scoring simulation agent into an LLM. The goal is to train autonomous agents in accelerated embodied/social worlds, then distill their learned causal judgment into controller modules that can guide an LLM reasoning loop.

In short:

```text
LLM = language, abstraction, explanation, code, and general knowledge
sim-distilled controller = consequence judgment, self-state feasibility, social repair, cascade risk, and action prioritization
reasoning algorithm = search loop that lets the LLM propose candidates while the controller scores, rejects, repairs, and prioritizes them
```

## Research Claim

The mature claim to test is:

```text
Autonomous agents trained in accelerated embodied/social simulations may learn reusable self/world/social credit-assignment structures. Those structures may be distillable into reasoning controllers that improve LLM planning, repair, and long-horizon decision-making.
```

This does not claim subjective consciousness. It does not claim that the current SSRM-3D agents are mature enough for this use. It identifies the practical downstream reason to keep building the simulation.

## Why This Follows From The Current Project

The repo's central claim is that self-like state becomes useful when future control depends on the agent's own hidden, changing body, memory, capabilities, commitments, relationships, and action effects.

The LLM extension asks the next question:

```text
If self/world/social state improves simulated agents, can distilled versions of those learned structures improve LLM reasoning?
```

The simulation is therefore not only an artificial-life environment. It is a possible pretraining environment for agency priors:

```text
action -> delayed consequence -> memory update -> social response -> repair attempt -> cascade outcome
```

Text models learn from descriptions of consequences. Simulation-trained agents can learn from consequence loops themselves.

## Adjacent Research

This direction is adjacent to existing LLM reasoning and agent work, but the proposed contribution is different.

| Work | Nearby idea | Difference from this plan |
|---|---|---|
| [ReAct](https://arxiv.org/abs/2210.03629) | Interleaves language reasoning with actions and environment feedback. | Here, the non-language controller is trained from embodied/social simulation outcomes and scores the LLM's options. |
| [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | Searches over multiple candidate reasoning paths. | Here, branch evaluation is not only LLM self-evaluation; it can be a sim-distilled consequence critic. |
| [Language Agent Tree Search](https://arxiv.org/abs/2310.04406) | Combines language agents, planning, action, and value-style search. | Here, value/process critics come from accelerated civilization/agency traces. |
| [Voyager](https://arxiv.org/abs/2305.16291) | Uses an LLM-powered Minecraft agent with curriculum, feedback, and a growing skill library. | Here, the simulation-trained component is distilled as an evaluator/controller around the LLM rather than only as an LLM-driven agent. |
| [Process supervision](https://arxiv.org/abs/2305.20050) | Scores intermediate reasoning steps, not just final answers. | Here, process rewards target embodied/social repair, self-state feasibility, and cascade avoidance rather than only math reasoning. |
| [Mesa-optimization risk](https://arxiv.org/abs/1906.01820) | Warns that trained systems can become internal optimizers with misaligned objectives. | This argues for using sim-trained agents first as bounded critics and evaluators, not autonomous real-world executors. |

## Architecture

The clean architecture is:

```text
user problem
  -> LLM proposes candidate interpretations, plans, and actions
  -> sim-distilled critics score the candidates
  -> search keeps promising branches and expands them
  -> safety/verifier layer checks facts, constraints, and manipulative-risk boundaries
  -> LLM verbalizes the selected answer or plan
```

The simulation-trained component does not need to speak naturally. It can operate as a latent evaluator.

The LLM effectively asks:

```text
Here are several plausible next moves. Which one preserves future options, repairs the true cause, and avoids cascade failure?
```

The controller answers in scores, risk flags, and suggested repairs.

## Distilled Modules

The project should not distill one opaque "best agent" into one giant model. It should distill separate modules with clear responsibilities.

| Module | What it should learn |
|---|---|
| Policy prior | Which next actions are worth considering first in a given embodied/social state. |
| Value model | Which plan preserves future option-space, survival, trust, capability, and adaptability. |
| Process reward model | Whether each reasoning step improves diagnosis, feasibility, repair, and cascade control. |
| Social credit-assignment critic | Who was harmed, what caused the harm, what repair fits, and what worsens while repair is attempted. |
| Self-state feasibility critic | Whether the acting system has the time, tools, memory, authority, trust, capability, and continuity needed to execute the plan. |
| World-cascade critic | Which non-social failures worsen while the system attends to a chosen repair path. |
| Commitment/continuity model | Which promises, identities, roles, prior actions, and obligations must remain coherent across time. |

## Report 99 Bridge

Report 99 is directly relevant because it exposes the failure that a future LLM-facing critic would need to solve.

A normal system may notice that "something social is wrong" and choose a plausible repair. The harder question is:

```text
Is this the right repair for the actual hidden cause, under time pressure, while other failures are worsening?
```

Report 99 creates that pressure and records a failed result. The learned GRU responds broadly to hidden social shock, but it spends too much of the recovery window on wrong repair classes. That is exactly the failure mode a social credit-assignment critic must learn to detect.

Reports 112 and 113 add a second bridge for the same roadmap. A diagnostic label can be correct offline and still fail online if using it collapses another required repair channel. The first bounded positive coupled-crisis result comes from joint arbitration that keeps environmental and social repair active together. A future LLM-facing controller should therefore score coordination among consequence channels, not only one plausible root cause.

Example transfer target:

```text
LLM candidate A: apologize immediately
LLM candidate B: punish the blamed agent
LLM candidate C: replace the missing tool
LLM candidate D: inspect cause, delegate urgent infrastructure repair, then make a credible social repair
```

A good sim-distilled critic should score:

- apology as socially plausible but possibly causally incomplete;
- punishment as high misblame risk;
- replacement as useful only if tool loss is the true cause;
- inspection plus delegation plus later repair as strongest when hidden cause and cascading world failure both matter.

## Training Pipeline

The research pipeline should be:

1. Build persistent embodied/social simulations with delayed shocks, partial observability, tools, shelters, social memory, illness, weather, infrastructure, teaching, and resource pressure.
2. Train many autonomous agents under accelerated time.
3. Select candidates that are robust across seeds, maps, pressures, and ablations rather than only high-scoring in one world.
4. Log observations, beliefs, self-state, social state, world state, obligations, candidate actions, chosen actions, outcomes, and counterfactual outcomes.
5. Generate counterfactual traces for wrong repair, delayed repair, overrepair, underrepair, misblame, and cascade amplification.
6. Train separate critics/value models from those traces.
7. Attach those critics to an LLM reasoning/search loop.
8. Evaluate on held-out simulation scenarios and real-world-style text/tool tasks.
9. Ablate each critic to prove which learned structure matters.

## Evaluation

The key test is transfer.

Compare:

- LLM alone;
- LLM plus ordinary chain/search prompting;
- LLM plus a generic reward model;
- LLM plus sim-distilled controller;
- LLM plus sim-distilled controller with targeted critic ablations.

Evaluation tasks should include:

- social repair after false blame;
- project recovery after deadline failure;
- emergency triage with trust damage;
- robotics delivery failure;
- multi-agent AI workflow failure;
- tool ownership and misplaced-resource disputes;
- infrastructure repair under time pressure;
- illness, overload, or capability-related failure attribution;
- commitment renegotiation under changing constraints.

The strongest result would be:

```text
The sim-distilled controller improves repair decisions on held-out real-world-style scenarios it never saw, and ablations show that the gain comes from self-state, social credit assignment, cascade-risk, or commitment-continuity critics.
```

## Selection Discipline

Do not select agents only because they win the simulation.

The selected agents or traces should satisfy:

- high performance;
- cross-seed robustness;
- held-out map and pressure transfer;
- low exploit behavior;
- no privileged state dependence;
- interpretable failure modes;
- good ablation profile;
- good social repair and cascade control;
- bounded use as critic/evaluator before any real-world action authority.

The best brain is not the one that dominates one simulated world. The best brain is the one whose learned judgment transfers.

## Safety Boundary

Open-ended selection can produce unwanted optimizers, manipulation, concealment, or reward exploitation. The safe initial use is:

- offline critic;
- bounded evaluator;
- synthetic data generator;
- plan-ranking model;
- failure detector;
- simulation-only policy.

Do not directly give a winning simulated agent broad real-world tool access.

The safe architecture is:

```text
LLM proposes plans
  -> sim-trained critic scores risk, repair fit, cascade risk, and option preservation
  -> rule/safety layer blocks unsafe or manipulative actions
  -> verifier checks facts and constraints
  -> LLM explains the selected plan
```

The system should learn to avoid misblame, repair actual harm, preserve cooperation, and prevent cascades. It should not be rewarded for manipulating trust efficiently.

## Near-Term Connection To Current Goals

The immediate SSRM-3D goal remains the 12h delayed-shock simulation:

- agents develop before major shocks;
- environments create richer risk and adaptation pressure;
- agents improve tools, buildings, teaching, memory, and social repair;
- learned controllers act under held-out worlds and targeted ablations.

The long-term reasoning-controller direction depends on solving the current bottlenecks first:

1. close the loop in the physics world;
2. fix social repair credit assignment;
3. add counterfactual trace generation;
4. train critics from consequences, not only imitation;
5. prove transfer across seeds, maps, and tasks;
6. only then attach distilled critics to an LLM search loop.

## Direct Commercial Specialization

The clearest commercial specialization is software engineering.

Software has executable feedback, hidden tests, code review, CI cost, regression risk, and repo-specific conventions. That makes it a clean domain for testing whether field-experience critics improve frontier LLM agents.

The dedicated plan is [Software Field-Experience Controller Plan](102_software_field_experience_controller_plan.md).

## One-Sentence Direction

Build autonomous simulated agents that learn long-horizon embodied/social survival, then distill their learned causal judgment into reasoning controllers that help LLMs make better decisions under uncertainty, time pressure, social ambiguity, self-state limits, and cascading failure.
