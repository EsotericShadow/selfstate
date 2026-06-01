# Hidden-State Boundary Attack

## The Attack

The current theory risks collapsing into:

```text
Systems with useful hidden variables benefit from tracking useful hidden variables.
```

That is too weak. It makes selfhood nearly tautological and fails to separate:

- hidden world-state tracking;
- hidden internal-state tracking;
- generic recurrent memory;
- agent-state modeling;
- selfhood.

The corrected theory must treat hidden-state tracking as a broader class. Selfhood is only one narrower solution inside that class.

## Replacement Claim

Hidden-state tracking becomes self-equivalent only when the tracked variable is:

1. agent-bounded: it belongs to the controlled system rather than only the external world;
2. persistent: it carries causal information across more than one observation/action cycle;
3. action-mediated: it changes what the same action does, or what actions remain available;
4. control/value relevant: policy quality, future options, or viability depend on it;
5. counterfactually agentic: intervening on the variable changes what this system can do or what its actions mean;
6. integrated: the same variable is reused across prediction, control, adaptation, or memory rather than isolated in one local predictor.

Continuity and ownership add a stronger identity-like layer:

7. continuity-indexed: it links past, present, and projected future states as states of the same continuing controlled process.
8. restore/fork specific: it preserves the components needed to resume or branch that process, rather than treating model weights, memory, body state, or social history alone as sufficient.

The minimal self-equivalent threshold is criteria 1-6. Criteria 7 and 8 are not required for simple sensorimotor selfhood, but they are required for identity-like continuity claims.

## Boundary Ladder

| Tier | Representation | Example | Counts as selfhood? |
|---|---|---|---|
| 0 | Hidden external state | Weather, terrain, market regime | No. This is world modeling. |
| 1 | Generic hidden internal variable | Local cache, unused diagnostic bit | No. Internal location is not enough. |
| 2 | Passive internal-state tracker | Fatigue sensor used only for report prediction | No, unless it affects control/value. |
| 3 | Agent-state controller | Actuator gain, damage, energy, sensor reliability | Minimal self-equivalent. |
| 4 | First-person control frame | Counterfactuals over what this system can do next | Stronger self-equivalent. |
| 5 | Continuity/identity self | Owner/epoch/commitment index across interruption; AgentContinuityRecord across restore or fork | Identity-like self. |
| 6 | Narrative or phenomenal self | Reportable autobiography or experience | Not tested here. |

The theory should not infer selfhood from tiers 0-2. Those are hidden-state mechanisms. They become evidence for selfhood only when the same latent participates in tier 3 or above.

## Why This Avoids Tautology

The claim is no longer:

```text
Hidden variables are useful, therefore self exists.
```

The claim becomes:

```text
When the hidden variable is a persistent state of the controlled system,
and future action, value, or coherence depends on it,
optimization should favor a reusable agent-state abstraction.
```

That abstraction is self-equivalent only because it answers action-centered questions:

- What can this system do now?
- What will happen if this system acts?
- What will this system be able to do later?
- Which prior commitments belong to this continuing system?
- Which prediction errors came from the world, and which came from changed agent-state?

## Positive And Negative Controls

### Negative Control A: Hidden World Variable

If a hidden external variable improves prediction or control, that supports hidden world modeling, not selfhood.

Example: wind affects movement. A wind posterior may be useful, but it is not a self-model unless it is bound to the agent's action interface, such as a worn sail or damaged actuator.

### Negative Control B: Internal But Control-Irrelevant Variable

If an internal variable is persistent and hidden but does not affect action, future options, reward, viability, or continuity, tracking it is not selfhood.

Example: a diagnostic counter improves self-report accuracy but never changes policy or future control.

### Negative Control C: Generic Memory

If raw history or recurrent state performs equally well with no decodable, stable, causally active agent-state factor, the self-attractor claim weakens.

### Positive Control A: Action-Effect State

If a hidden variable changes what actions do, and intervention on that variable changes predicted control, it passes the minimal self-equivalent threshold.

Example: actuator gain, body damage, sensor calibration, or current competence.

### Positive Control B: Future Viability State

If actions must regulate future internal state to preserve future options, self-state becomes a long-horizon control variable.

Example: energy, fatigue, damage, toxicity, or thermal state.

### Positive Control C: Continuity Index

If an agent must decide which past commitments, memories, or goals still belong to the same continuing process, the representation becomes identity-like.

Example: owner/current-epoch/pending-status metadata after interruption.

## Falsifiable Boundary Tests

A variable should not be counted as self-equivalent unless these probes succeed:

1. Boundary probe: does the variable describe the controlled system rather than only the external environment?
2. Action probe: does changing it alter action effects, available actions, or action costs?
3. Value probe: does using it improve reward, survival, transfer, or recovery?
4. Counterfactual probe: can the system answer what would happen if its own state were different?
5. Integration probe: is the same variable reused across more than one prediction/control problem?
6. Ablation probe: does removing or randomizing it selectively harm tasks that require agent-state but not tasks that only require world-state?
7. Continuity probe: for identity-like selfhood, does it distinguish current own commitments from stale, foreign, duplicated, or contradictory records?
8. Restore/fork probe: does a resumed or forked agent fail in predictable ways when the continuity record is reduced to weights, generic memory, body state, social history, commitments, tools, or branch id alone?

## New Falsifiers Introduced By The Attack

The selfhood claim weakens if:

- hidden external variables produce the same claimed advantages and were misclassified as self-state;
- hidden internal variables improve passive prediction but not control, value, adaptation, or continuity;
- generic recurrent memory solves scaled drift, viability, and interruption tasks with no decodable agent-bound latent;
- isolated internal trackers solve local tasks but do not integrate across prediction, action, viability, or memory;
- self-labeled variables improve performance only by adding capacity, not by carrying agent-bounded causal information;
- interventions on the proposed self-variable do not change action-centered counterfactuals.

## Revised Minimal Mechanism

The smallest non-conscious self-equivalent is not:

```text
persistent hidden state
```

It is:

```text
agent-bounded persistent state
+ action-conditioned prediction
+ control/value dependence
+ counterfactual intervention sensitivity
+ cross-task reuse
```

For identity-like selfhood, add:

```text
continuity index over owned past, present, and future states
```

## Consequence For The Research Program

The evidence standard must separate three questions:

1. Does hidden-state tracking help?
2. Is the hidden state internal to the controlled system?
3. Does it function as a reusable agent-state abstraction for action, value, adaptation, or continuity?

Only the third question is evidence for selfhood. The first is ordinary latent-state modeling. The second is agent-state tracking. The third is where "hidden internal variable tracking" becomes computational selfhood.

## Current Stress Evidence

The architecture hard-return and online-return audits make this boundary operational. They show that objective-only return training can select useful recurrent or local hidden-state strategies while still failing strict self/tool boundary convergence. That is exactly the distinction this attack requires:

- high return is not enough;
- recurrence is not enough;
- hidden-state usefulness is not enough;
- the learned state must pass the persistent agent-boundary intervention test.

In the current online return-learner audit, independent-hidden and irrelevant controls remain clean, but self, detachable, and passive shared regimes are only 1/3 convergent across recurrent architectures. The policy-gradient learner then recovers 3/3 convergence in those shared regimes while keeping the same controls clean. The policy-gradient seed sweep adds that this recovery is not automatically seed-stable: controls remain clean, but shared-regime strict convergence appears in only some seeds. The policy-gradient budget sweep repairs seed stability for self-persistent and passive-world recurrence, but detachable-tool recurrence remains partial. The Torch actor-critic learner then recovers strict self, detachable, and passive signatures across `RNN`, `GRU`, and `LSTM` actor-critics while independent-hidden and irrelevant controls still reject shared recurrence or hidden state. Together, the results keep the hidden-state loophole explicit: sampled return can shape self-equivalent boundary structure, but only when the learner actually passes the causal boundary test, and detachable external action effects remain a distinct boundary problem until the actor-critic result survives seed and environment sweeps.

The SSRM-3D precursor adds a second boundary: the LLM is not the self. The persistent self-equivalent state is the realtime control workspace that estimates viability, integrity, mobility, uncertainty, commitments, and attention priorities. The language module receives a compressed packet and recommends; reflex, arbiter, and motor layers still control the organism. This prevents the experiment from replacing the hidden-state loophole with a language-controller loophole.

The SSRM-3D recurrent-observer precursor adds a third boundary: the measured self-state does not have to be the hand-built workspace. Recurrent observers trained on embodied traces recover hidden energy, integrity, mobility, and sensor capability. Stage 0 remains only body-state decodability with little recurrent advantage; stages 1-6 show stronger recurrent self-state recovery and future-viability sensitivity to self-state edits. This still does not prove selfhood, but it blocks the simple objection that the SSRM-3D result is only a named internal variable table.

The SSRM-3D learned-controller precursor adds a fourth boundary: learned policy state, not just observer state, carries self-state under pressure. Recurrent controllers trained without self labels strongly beat frame-only controllers in stages 1-6 and contain decodable energy, integrity, mobility, and sensor capability. The action-edit swing remains weak, so the result blocks the "observer only" objection but keeps the causal-editability loophole open.

The modular LLM architecture adds a fifth boundary: language is not allowed to silently absorb the selfhood claim. The LLM reads a compressed packet and proposes; the persistent control workspace, attention layer, arbiter, and action layer remain separate. This creates a future ablation test: no-LLM should mainly damage slow abstraction, direct-motor LLM should mainly damage realtime control, and corrupted self packets should produce specific recommendation errors.

The SSRM-3D tool-making precursor adds a sixth boundary: externalized cognition is not automatically selfhood. Markers, beacons, alarms, and caches remain world structures. They matter because return selection uses them only when internal memory or perception is insufficient, and tool-access ablation removes the gain. This supports a tool-pressure bridge, not a claim that every useful external variable is self.

The SSRM-3D social-pressure precursor adds a seventh boundary: other-agent modeling is not automatically selfhood. Trust and reputation become relevant because other agents remember and act on the tested agent as a continuing social object. Identity-memory, social-self-state, and tool-access ablations must produce specific losses before the result counts as social self-pressure rather than generic multi-agent state tracking.

The SSRM-3D social-ecology precursor adds an eighth boundary: communication is not automatically language, selfhood, or social structure. Signals, names, gossip, and check-ins count only when they are costly, rejected in no-job controls, selected by return under social memory, and damaged by targeted ablation. Babble must lose when it has no control job.

The SSRM-3D agent-continuity precursor adds a ninth boundary: continuity is not model weights, memory, body state, or social history alone. A restored or forked agent counts as the same continuing control process only when the full record binds body, model, memory, social history, commitments, event-log position, attention, hidden state, tools, goals, and branch identity. Component ablations must fail specifically in the pressures that require those components.

The SSRM-3D learned-integration precursor adds a tenth boundary: a successful candidate policy is not enough. Tool, social, continuity, and attention evidence must be carried by learned policy state, and ablations must produce specific losses rather than generic collapse. The result is still only a designed packet bridge because scenario identity and feature groups are supplied.

The SSRM-3D no-leak integration sweep adds an eleventh boundary: a learned packet bridge must survive shortcut removal. Removing scenario identity, randomizing pressure combinations, running five seeds, and requiring wider margins produces a partial negative. Some bridges survive, but `single_tool` is margin-fragile and `integrated_social` is not ablation-stable. This keeps "learned hidden-state tracking" separate from stable self-equivalent integration.

The SSRM-3D structured-perception precursor adds a twelfth boundary: perception is not selfhood. Cone vision and spatial audio are world-access channels. They become relevant to selfhood only when partial perception creates pressure for memory, tools, attention, continuity, or self-state-aware sensor adaptation. The control must reject perception machinery when omniscient or open daylight access is enough.

The SSRM-3D day/night sleep-rest precursor adds a thirteenth boundary: sleep is not selfhood. Rest is an action that changes future capability and current vulnerability. It becomes relevant to selfhood only when the agent must track hidden fatigue, darkness timing, safe-rest context, alarms, social watch, or continuity after interruption. The daylight control must reject sleep when it has no control job.

The SSRM-3D illness/sanitation precursor adds a fourteenth boundary: illness is not selfhood. Hunger, thirst, infection, contamination, care, quarantine, and immunity are internal or environmental variables. They become relevant to selfhood only when delayed internal risk, self/world error attribution, social exposure, or restore-time continuity changes policy. Clean controls must reject health machinery when it has no control job.

The SSRM-3D weather/exposure precursor adds a fifteenth boundary: weather is not selfhood. Cold, heat, rain, wind, drought, shelter, fire/light, and water planning are external or tool variables. They become relevant to selfhood only when the agent must model how external conditions change its own future capability, accumulated exposure, hydration, safe shelter use, or restore-time continuity. Mild controls must reject weather machinery when it has no control job.

The SSRM-3D tool/shelter degradation precursor adds a sixteenth boundary: maintenance is not selfhood. Marker wear, shelter damage, alarm/cache decay, spare parts, and repair are persistent external variables. They become relevant to selfhood only when external infrastructure changes the agent's own future capability, route reliability, shelter safety, resource access, or restore-time continuity. Stable controls must reject maintenance machinery when it has no control job.

The SSRM-3D social trust/contracts precursor adds a seventeenth boundary: promises are not selfhood. Commitment memory, identity memory, ownership, repair debt, and trust updates are social control variables. They become relevant to selfhood only when the tested agent must model itself as a continuing social object whose kept or broken obligations change future access, help, tool use, shelter safety, or restore-time continuity. Visible controls must reject contract machinery when it has no control job.

The SSRM-3D predator/threat agents precursor adds an eighteenth boundary: threats are not selfhood. Trackers, sound, scent, stealth, shelter, alarms, social warning, and fear-like control state are threat-control variables. They become relevant to selfhood only when the tested agent must model its own vulnerability, trace, routines, defenses, social exposure, or restore-time memory as future-control variables. Safe controls must reject threat machinery when no tracker exploits those variables.

The SSRM-3D resource ecology precursor adds a nineteenth boundary: resource ecology is not selfhood. Regrowth, depletion, spoilage, migration, caches, sharing, and territory are resource-control variables. They become relevant to selfhood only when the tested agent must model its own future needs, restraint, access history, obligations, place relations, or restore-time resource memory as future-control variables. Abundant controls must reject ecology machinery when delayed resource consequences do not matter.

The SSRM-3D injury/disability adaptation precursor adds a twentieth boundary: injury/disability is not selfhood. Mobility loss, degraded senses, wound infection, repair, help, tools, and route changes are capability-control variables. They become relevant to selfhood only when the tested agent must model its own capability limits, infection risk, support access, tool compensation, route feasibility, or restore-time disability history as future-control variables. Fixed-body controls must reject disability machinery when changed capability does not matter.

The SSRM-3D development/skill learning precursor adds a twenty-first boundary: skill is not selfhood. Practice history, fatigue-limited competence, injury retraining, transfer, teaching, tools, and goal feasibility are competence-control variables. They become relevant to selfhood only when the tested agent must model its own changing competence, usable capability, and restore-time skill history as future-control variables. Easy fixed-skill controls must reject skill machinery when changing competence does not matter.
