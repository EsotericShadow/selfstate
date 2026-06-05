# Why Does a Self Exist?

A plain-language guide to the current research program.

![Pressures in toy worlds leading to repeated self-like structure](assets/self_like_structure_pressure_map.png)

## The Question

When does an artificial agent need to represent "me" instead of only representing "the world"?

The current answer is narrow:

> A self-like model becomes useful when an agent must act through time while its own body, memory, needs, tools, relationships, commitments, or abilities are changing in ways it cannot fully observe.

This project does not claim that the agents are conscious. It does not claim that a self is a separate inner entity. It treats a self as a control structure: a persistent model of the system that is acting.

## The Simple Version

A thermostat does not need a self. It can read temperature and turn heat on or off.

An embodied agent in a changing world may need more than that. It may need to know:

- how much energy it has;
- whether it is damaged, tired, sick, or overloaded;
- what it can currently do;
- what it promised or started earlier;
- who it can trust;
- which tools and shelters still work;
- whether a problem came from the world changing or from itself changing.

![A simple reactive system compared with an embodied agent that must model itself](assets/reactive_vs_embodied_agent.png)

In this project, "self" means that kind of persistent agent-state model.

## What We Built

The repository contains a sequence of toy experiments and SSRM-3D simulations. They ask whether self-like state becomes useful under different pressures.

The current canonical manifest reports:

- `72` experiment runs;
- `0` manifest failures;
- a public evidence stack from minimal hidden-state tests through SSRM-3D pressure layers.

That is not a final proof. It is a working research record.

## What Counts As Self-Like Here

A hidden variable does not count as selfhood just because it is hidden or internal.

It counts as self-like only when it is:

- agent-bounded: about the system that is acting;
- persistent: relevant across time;
- action-mediated: it changes what the agent's actions do;
- value-relevant: it changes survival, reward, options, or commitments;
- counterfactually active: changing it changes what the agent should do;
- reused: the same state helps across multiple decisions.

That boundary matters. Weather, terrain, or another agent's mood may be hidden and important, but those are world models, not self models.

## What The Experiments Suggest

The evidence points to one main pattern:

> Self-like state is optional in simple tasks, but becomes useful when future control depends on the agent's own changing state.

Examples:

| Pressure | Why it creates self-state pressure |
|---|---|
| Hidden actuator drift | The agent must know whether the world changed or its own control changed. |
| Energy and damage | Future options depend on internal viability. |
| Continuity after interruption | The agent must know which memories and commitments still belong to this run. |
| Goals and arbitration | Feasible goals depend on current capability, risk, and competing needs. |
| Tools and shelter | External aids matter only if the agent remembers their condition and ownership. |
| Social trust | Promises, deception, help, and reputation require identity and continuity memory. |
| Illness and fatigue | Hidden internal state changes what is safe, possible, and urgent. |
| Skill learning | Current ability affects which goals are realistic. |
| Affective control state | Fear, stress, trust, curiosity, and guilt analogues act as control summaries, not subjective feelings. |

![SSRM-3D persistent world concept](assets/ssrm_3d_persistent_world_concept.png)

## What The SSRM-3D Pressure Layers Add

The later simulations make the toy world richer, but still controlled. The point is not to recreate biology. The point is to add pressure variables that force tradeoffs across time.

![SSRM-3D pressure layer overview](assets/ssrm_3d_pressure_layer.png)

Current SSRM-3D pressure layers include:

- structured vision and spatial audio;
- day/night cycles, sleep, and rest;
- hunger, thirst, illness, sanitation, and contamination;
- weather and exposure;
- tool, marker, alarm, and shelter degradation;
- social contracts, trust, and promises;
- predator and threat agents;
- resource ecology;
- injury and disability adaptation;
- development and skill learning;
- dependent care;
- irreversible loss;
- affective control state.

These are not claims about consciousness. They are tests of when persistent self-state becomes useful for control.

## Where Language Fits

Language is treated as a slow reasoning layer, not as the self and not as the whole organism.

The language module can receive compressed state packets, reason about them, and suggest plans. The fast control system still owns perception, self-state, attention, arbitration, and action.

![Language enters the simulated world as local input](assets/language_enters_simulation.png)

That lets the project test whether language helps planning without confusing language ability with selfhood.

## The Current Honest Finding

In plain English:

> A persistent self-like model looks useful when an agent has to survive, adapt, remember, repair, cooperate, and continue through changing conditions. But the current evidence is still toy-scale. It supports a mechanism, not a consciousness claim.

The most important negative result is also clear:

> The project has not yet proven that selfhood naturally emerges in open learned agents. Some results still depend on designed scenarios, supplied candidate policies, or structured state packets.

That is why the next serious step is not "add more labels." It is to move more of the pressure into shared learned controllers and see whether the same self-like variables are discovered without shortcuts.

## How To Read The Repo

Start here:

- [Public findings article](research_article.md)
- [Current synthesis](../11_current_synthesis.md)
- [Evidence matrix](../12_evidence_matrix.md)
- [Repository weakness audit](../70_repo_weakness_audit.md)
- [Persistent pressure layer spec](../74_ssrm_3d_persistent_pressure_layer_spec.md)

For the technical stack, use the root [README](../../README.md).
