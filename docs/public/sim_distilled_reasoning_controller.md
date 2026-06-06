# The Long-Term Use: Simulation-Distilled Reasoning For LLMs

The long-term use of this project is bigger than making smarter agents in a simulated world.

The stronger goal is:

> Train agents in accelerated embodied/social simulations, then distill what they learn about consequences into reasoning controllers that help LLMs plan better.

The LLM should not become the whole agent.

The cleaner architecture is:

| Part | Job |
|---|---|
| LLM | Language, abstraction, explanation, code, general knowledge. |
| Simulation-distilled controller | Long-horizon consequence judgment, self-state feasibility, social repair, cascade risk, action prioritization. |
| Search loop | Lets the LLM propose candidate plans while the controller scores, rejects, repairs, and prioritizes them. |

## Why This Matters

LLMs are trained mostly on text. They are good at producing explanations, plans, and plausible advice.

But text is not the same as living through consequences.

The simulation gives agents a different kind of training signal:

```text
action -> delayed consequence -> memory update -> social response -> repair attempt -> cascade outcome
```

That kind of experience can teach patterns that ordinary language models often miss:

- do not repair the visible social problem if the physical cause is still active;
- do not punish before checking whether the failure was illness, overload, tool failure, or environment;
- do not optimize one relationship while the shelter is collapsing;
- do not plan as if your tools, body, authority, trust, and memory are unchanged;
- do not spend the whole recovery window on the wrong repair.

## What Gets Distilled

The goal is not to copy the single highest-scoring simulated agent.

The goal is to distill separate judgment modules:

| Module | What it helps an LLM judge |
|---|---|
| Self-state feasibility critic | Can the acting system actually do this with its current time, tools, trust, memory, authority, and capability? |
| Social credit-assignment critic | Who was harmed, what caused it, and what repair actually fits? |
| World-cascade critic | What gets worse while this plan is being executed? |
| Option-preservation value model | Which plan preserves the most future flexibility? |
| Commitment/continuity model | Which promises, roles, identities, and prior actions must remain coherent? |
| Policy prior | Which next actions are usually worth considering first? |

Together, these become a reasoning layer around the LLM.

## Why Report 99 Matters

Report 99 is a failed result, and that is why it matters.

The learned controller notices that a hidden social shock happened, but it often spends the recovery window on the wrong repair class.

That is exactly the kind of mistake LLMs can make in real tasks:

- apologizing when diagnosis is needed;
- blaming when evidence is incomplete;
- fixing a relationship while a tool or infrastructure failure continues;
- solving the visible conflict while the hidden bottleneck gets worse.

The future controller should learn to score candidate plans by repair correctness, time cost, trust damage, and cascade risk.

## The Future Test

A serious evaluation would compare:

- LLM alone;
- LLM with ordinary search prompting;
- LLM with a generic reward model;
- LLM with a simulation-distilled controller;
- LLM with individual critics removed.

Then test on problems the simulated agents never saw:

- a hospital delivery robot missed a medicine run;
- a software team missed a deadline;
- a warehouse robot misplaced a shared tool;
- a disaster-response team failed to arrive;
- a multi-agent AI workflow produced a broken result;
- a support escalation blamed the wrong person.

The question would be:

> Does the simulation-distilled controller help the LLM choose repairs that address the true cause and avoid cascading failure?

## Most Direct Commercial Version

The same architecture can specialize into software development.

Software has unusually clean feedback:

```text
issue -> repo state -> patch -> tests -> review -> deploy -> regression
```

That makes it a natural domain for field-experience controllers. The critic does not need to replace a coding LLM. It can score root-cause localization, patch risk, test strategy, hidden-regression risk, review fit, and repo conventions around the LLM.

The dedicated roadmap is here: [The Commercial Path: Software Field-Experience Controllers](software_field_experience_controller.md).

## Safety Boundary

The winning simulated agent should not be given broad real-world authority.

The safe first use is:

- offline critic;
- bounded evaluator;
- plan-ranking model;
- synthetic data generator;
- failure detector.

The sim-trained part should advise and score. A separate verifier and safety layer should still block unsafe or manipulative actions.

## The One-Sentence Version

This project can become a way to train non-linguistic agency priors, then use those priors to make LLMs better at long-horizon planning, social repair, self-state feasibility, and cascade avoidance.
