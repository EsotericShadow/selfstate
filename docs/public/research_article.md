# Why Would an Artificial Agent Need a Self?

## Findings So Far From A Controlled Simulation Research Program

![Pressures in toy worlds leading to repeated self-like structure](assets/self_like_structure_pressure_map.png)

### Short Version

The current evidence suggests that a self-like model is not needed for every intelligent system.

It becomes useful when an agent must keep acting over time while its own body, memory, needs, tools, social commitments, and abilities are changing.

That is the core result:

> A self can be understood as a persistent control model of the system that is acting.

This is not a proof of consciousness. It is not a claim that the agents have inner experience. It is a falsifiable architecture claim about prediction, control, adaptation, and continuity.

## The Research Question

The project starts with one question:

> When does representing "me" become more useful than representing "the world only"?

Many systems can work without anything like a self. A thermostat reacts to temperature. A simple game bot follows rules. A planner can choose actions from a map.

But a long-running embodied agent faces a harder problem. Its own state changes:

- its sensors can become unreliable;
- its actions can stop having the same effect;
- its energy can fall;
- its tools can wear out;
- its memory can become stale;
- its promises can carry forward;
- its relationships can change;
- its skills can improve or degrade.

In that kind of setting, the agent needs to model not only the world, but also the continuing system that is acting inside the world.

![A simple reactive system compared with an embodied agent that must model itself](assets/reactive_vs_embodied_agent.png)

## What "Self" Means In This Project

The word "self" is easy to overuse, so the project defines it narrowly.

Here, a self-like state is:

> a persistent internal model of the acting system as a distinct entity through time.

That does not require a human-like ego. It does not require language. It does not require consciousness.

It does require more than generic hidden-state tracking. A hidden variable counts as self-like only if it is:

| Requirement | Plain meaning |
|---|---|
| Agent-bounded | It is about the system that is acting. |
| Persistent | It matters beyond the current instant. |
| Action-mediated | It changes what the system's actions do. |
| Control-relevant | It affects survival, reward, options, or commitments. |
| Counterfactually active | If the state changed, the right action would change. |
| Reused | The same state helps across multiple decisions or contexts. |

This boundary is important. Hidden weather is not selfhood. Hidden terrain is not selfhood. Another agent's private state is not selfhood. Those may be important world models.

Self-like state is the model of "what condition am I, the acting system, in?"

## Method

The project uses toy experiments rather than philosophical argument.

The experiments compare agents that have different kinds of memory and state:

- no self-state;
- world-state only;
- local history;
- generic memory;
- explicit self-state;
- recurrent learned state;
- continuity records;
- attention and arbitration layers;
- structured SSRM-3D embodied agents.

The experiments then add pressure:

- partial observability;
- hidden actuator drift;
- energy and damage;
- interruption and memory corruption;
- long-horizon option preservation;
- tool use;
- social trust;
- illness and fatigue;
- skill learning;
- dependent care;
- irreversible loss;
- affective control summaries.
- physics-derived sensor streams.

The key question is not whether an agent says it has a self.

The key question is:

> Does removing the self-like state cause a specific control failure?

If a no-self or world-only agent performs just as well, the self claim fails for that setting.

## What The Evidence Shows

The canonical runner is now wired for `74` runs, including the physics-first benchmark and settlement/civilization pressure layer.

That does not mean all claims are proven. It means the repo evidence stack is designed to be regenerated under its canonical runner, and each new claim still needs its matching verification pass.

The main pattern is:

> Self-like state is unnecessary in simple or fully visible tasks, but becomes useful when future outcomes depend on hidden, changing agent-state.

### 1. Self-State Helps With Error Attribution

If an action suddenly produces a different result, two things may have happened:

- the world changed;
- the agent changed.

For example, a robot may turn poorly because the ground changed, or because its actuator drifted. A world-only model can confuse those. A self-like action-effect model helps separate them.

### 2. Self-State Helps With Survival Over Time

Energy, damage, fatigue, illness, and capability are not just facts. They change what the agent should do next.

An agent with low energy should not plan the same way as an agent with high energy. An injured agent should not treat every route as equally feasible. A sick agent may need water, rest, shelter, or quarantine.

That is self-state as a control variable.

### 3. Self-State Helps With Continuity

When an agent is interrupted, restored, copied, or corrupted, it needs to know which memories and commitments still belong to the same continuing process.

Generic memory is not enough when records can be stale, foreign, duplicated, or contradictory.

This is where identity-like behavior appears: not as a mystical essence, but as a continuity record that protects action coherence.

### 4. Self-State Helps With Goals

A goal is not just a desired world state. It must be feasible for the current agent.

The same task can be easy, impossible, risky, or irresponsible depending on the agent's current energy, damage, trust, skills, tools, and obligations.

That makes self-state part of goal formation.

### 5. Self-State Helps With Social Life

Social behavior requires memory of identity, promises, help, deception, shared tools, reputation, and trust.

Those are not just external facts. They bind to a continuing agent:

- What did I promise?
- Who helped me?
- Who deceived me?
- What do others expect from me?
- What should I repair or return?

The experiments do not claim human emotion or morality. They show that social control pressure creates a need for persistent identity and commitment state.

### 6. Affective State Can Be Treated As Control State

The project models fear, stress, trust, frustration, affiliation, curiosity, and guilt analogues as control summaries.

That means they affect attention, risk tolerance, memory priority, communication, or repair behavior.

It does not mean the agent feels them.

This distinction matters. A fear-like control state can be useful without being conscious fear.

![Attention mixer architecture concept](assets/attention_mixer_architecture.png)

## SSRM-3D: The Embodied Simulation Track

SSRM-3D is the project's persistent embodied simulation track.

It adds a body, position, orientation, hazards, resources, shelter, tools, social pressure, memory, and continuity state. The point is not realism for its own sake. The point is to add pressures that force tradeoffs over time.

![SSRM-3D persistent world concept](assets/ssrm_3d_persistent_world_concept.png)

The current SSRM-3D pressure layers include structured perception, sleep, illness, weather, tool degradation, social contracts, threats, resource ecology, injury, skill learning, dependent care, irreversible loss, and affective control.

![SSRM-3D pressure layer overview](assets/ssrm_3d_pressure_layer.png)

These layers are deliberately abstract. The project does not need a full digestive system, subjective pain, or biological detail unless that detail changes policy, memory, attention, tools, social behavior, or continuity.

The rule is:

> Add world detail only when removing it would change the agent's control problem.

The physics-first benchmark adds a modular foundation. A C++ simulation kernel now generates terrain, weather, shelter, resources, illness/care pressure, sound, vibration, tension, FOV perception, and user proposals. Python trains recurrent neural models on those physics-derived streams without scenario labels.

![SSRM-3D physics-first benchmark viewer](assets/ssrm_3d_physics_benchmark.png)

That is real neural sequence learning, but it is still offline decision learning from traces. It is not yet closed-loop deep reinforcement learning and it is not a claim that a self-aware agent has been created.

The newest step adds a settlement/civilization pressure layer. It moves the public replay beyond one-agent water/shelter survival into a small society with roles, construction, social memory, norms, affective-control state, conflict, sickness, and future shocks.

![SSRM-3D settlement/civilization pressure viewer](assets/ssrm_3d_civilization_pressure.png)

The integrated settlement policy reaches `0.812` mean civilization score. Reactive individuals fall to `0.502`, and targeted ablations for norms, role memory, future planning, building memory, social memory, and affective control all reduce score. This remains designed policy evidence, not open-ended civilization emergence.

## Visual Evidence Gallery

The following screenshots show current SSRM-3D pressure-layer visualizations. They are visual summaries of controlled experiments, not claims that these worlds are biologically realistic.

![Structured perception pressure layer](assets/ssrm_3d_structured_perception.png)

![Day and night sleep-rest pressure layer](assets/ssrm_3d_day_night_sleep.png)

![Illness and sanitation pressure layer](assets/ssrm_3d_illness_sanitation.png)

![Weather and exposure pressure layer](assets/ssrm_3d_weather_exposure.png)

![Tool and shelter degradation pressure layer](assets/ssrm_3d_tool_shelter_degradation.png)

![Social trust and contracts pressure layer](assets/ssrm_3d_social_trust_contracts.png)

![Predator and threat agents pressure layer](assets/ssrm_3d_predator_threat_agents.png)

![Resource ecology pressure layer](assets/ssrm_3d_resource_ecology.png)

![Injury and disability adaptation pressure layer](assets/ssrm_3d_injury_disability_adaptation.png)

![Development and skill learning pressure layer](assets/ssrm_3d_development_skill_learning.png)

![Dependent care pressure layer](assets/ssrm_3d_dependent_care.png)

![Irreversible loss pressure layer](assets/ssrm_3d_irreversible_loss.png)

![Affective control pressure layer](assets/ssrm_3d_affective_control.png)

## Where Language Fits

Language is not treated as the self.

In the proposed architecture, language is a slower reasoning module. It can receive compressed information from the agent's world model and self model, then suggest explanations, plans, or tool use.

But fast perception, self-state, attention, arbitration, and action remain outside the language module.

![Language enters the simulated world as local input](assets/language_enters_simulation.png)

This makes language testable:

- If removing language only hurts slow planning and explanation, language is not the core self.
- If corrupting self-state harms control while language remains intact, the self-state layer is doing real work.
- If a language-only agent with no persistent self-state performs equally well, the architecture claim is weakened.

## The Most Important Limitations

The project is still toy-scale.

The strongest limitations are:

1. Many experiments use designed scenarios.
2. Some policies are selected from supplied candidate behaviors.
3. Some learned-controller tests use structured packet features.
4. The architecture-independent attractor claim is not proven.
5. Learned integration is only partial.
6. The agents are not conscious and are not being tested for consciousness.

The no-leak integration sweep is especially important. It removed one shortcut from a learned-integration result and found a partial negative:

> Some local and integrated pressures survived, but the stronger no-leak integration claim did not fully hold.

That is good research hygiene. A negative result prevents the project from overstating the evidence.

## What Would Prove The Current Theory Wrong?

The project should fail if better evidence shows that:

- no-self agents match performance in rich long-horizon pressure worlds;
- generic memory solves the same tasks without agent-bounded state;
- self-like variables only appear when hand-coded;
- learned agents solve the tasks without stable, causally active agent-state;
- world-only models scale better than self-state models;
- self-like behavior appears only in narrow scenario templates;
- seed sweeps or architecture sweeps collapse the pattern.

Those are not side notes. They are the falsifiers.

## Current Best Claim

The strongest honest claim is:

> In toy environments, persistent self-like state becomes useful when hidden agent-state is action-mediated, value-relevant, persistent, and reused across prediction or control. The evidence supports selfhood as a control abstraction, not as a consciousness claim.

The stronger claim is not yet proven:

> Independent learned agents in rich open worlds naturally converge on selfhood as an attractor.

That remains the frontier.

## Why This Matters

The project reframes the self question in a testable way.

Instead of asking whether a system "really has a self," it asks:

> What breaks when the system cannot represent itself as the continuing actor?

That turns a philosophical question into an engineering and scientific one.

It also gives a practical architecture direction for future agents:

- keep self-state separate from world-state;
- track continuity across interruption and memory repair;
- treat affective state as control state, not proof of feeling;
- make language a reasoning module, not the whole agent;
- require ablation evidence before calling any variable self-like.

## Where To Go Next

The next serious research step is not simply to add more world detail.

The next step is to close the loop in the physics world:

- no scenario identity shortcuts;
- randomized pressure combinations;
- multiple seeds and architectures;
- online or model-based learning;
- causal ablations of learned policy state;
- learned policies acting inside richer SSRM-3D environments where tools, social pressure, continuity, perception, illness, weather, physics, and affect interact.

Only then can the project test the harder question:

> Does selfhood emerge as an attractor in adaptive systems, or is it just a useful structure we keep handing to the agent?
