# Evidence Matrix

This file links the research claims to current evidence, counterevidence, and next falsifiers.

## Experiment Families

| Experiment | Main pressure | Positive evidence | Counterevidence or limit |
|---|---|---|---|
| Self/world attribution | Error attribution under actuator/world drift | Factorized self/world agent recovers when hidden actuator state changes; self-state ablation fails in self drift. | History action table remains competitive in small action spaces; factorization is hand supplied. |
| Representation search | Self as compression | Model selection picks no-self in static cases, world-only in world drift, self-equivalent in self drift. | Candidate model family includes self-like linear forms; not a fully learned architecture. |
| Predictive-state emergence | Implicit self from action-conditioned prediction | Hidden actuator gain is decodable from counterfactual action predictions without labels; ablation harms self-drift control. | Toy linear environment; predictive state is simple and interpretable. |
| Hidden viability survival | Self as long-horizon control variable | Persistent energy/integrity estimates improve survival and value under energy/damage stress; ablation dies. | Low-stress task does not need self-state; fixed schedule solves combined drift. |
| Interruption coherence | Self as continuity/coherence index | Identity ledger solves foreign/stale/corrupted memory and matches oracle; metadata ablation fails. | Generic memory solves clean resume; ledger is hand designed. |
| Online predictive learning | Learned self-equivalent state from prediction error | Action-effect learners recover self drift without labels; action-component ablation harms control. | Linear feature family is designed; not a rich recurrent architecture. |
| Selfhood boundary probe | Anti-tautology test | Hidden external and passive internal variables help but do not count as selfhood; action-effect, viability, and continuity variables pass the boundary. | Boundary is still hand specified and must be stress-tested in learned architectures. |
| Architecture convergence | Narrow precursor to Attractor Test | Top learners require bias components under world drift, action-effect components under self drift, and both under mixed hidden drift. | Still a linear toy world; learner families contain action-sensitive predictors. |
| Active self-information | Information-seeking for control | Bandit learns to inspect agent-state when agent-state controls outcome, world-state when world-state controls outcome, both when both matter, and nothing when hidden state is irrelevant. | Small discrete decision problem; action model is supplied. |
| Counterfactual option preservation | Self-preservation as future option control | Future-option self-state preserves capability and beats myopic agents when future options depend on capability; no-option and world-gate controls do not favor self-preservation. | Hand-coded model-based policy; simple threshold environment. |
| First-person frame integration | Centered observation/action frame | Centered frame succeeds under hidden orientation and orientation drift; aligned control needs no centered frame. | Small deterministic grid; action-table memory is competitive in tiny action space. |
| Goal formation under capability | Self-state as goal-feasibility filter | Self-capability selector wins when capability determines feasible goals; world selector wins when world gates matter; greedy wins when all goals are feasible. | One-step goal-choice toy; goal set is hand-designed. |
| Competing subsystems arbitration | Self-state as shared coherence variable | Self-coherence arbitrator beats local voting when hidden agent energy determines which subsystem proposal is coherent; no-conflict and world-gate controls do not favor self-state. | Hand-coded subsystem policies; conservative safety heuristic nearly ties the self-arbitrator in the agent-energy conflict. |
| Cross-context self-state reuse | Self-state as reusable abstraction | Shared self-state wins when one persistent agent capability controls goal choice, option preservation, and commitment action; world reuse, independent-hidden, and irrelevant controls do not favor self-state. | Hand-designed contexts and probe channels; no learned abstraction discovery. |
| Reuse pressure sweep | Self-state advantage as a pressure gradient | Shared self-state advantage grows from 0 to 5 as reusable agent-state contexts increase from 1 to 6; world, independent-hidden, and irrelevant controls select the non-self abstraction. | Probe-cost structure makes the gradient explicit by design; still not learned discovery. |
| Horizon pressure sweep | Self-state advantage as a temporal pressure gradient | Shared self-state advantage grows from 0 to 11 as future steps depending on one hidden agent-state increase from 1 to 12; controls select world, local, or no-state abstractions. | Probe-cost structure makes the gradient explicit by design; still not learned discovery. |
| Partial observability sweep | Self-belief advantage as evidence quality increases | Shared self-belief becomes best at high cue reliability when noisy evidence tracks one persistent agent-state; controls select world-belief, local probing, or greedy no-state behavior. | Bayesian update and cue model are supplied; not learned from raw observations. |
| Learned observation filter | Learned filtering from noisy cue histories | Empirical cue-count filters select agent-state, world-state, local probing, or no-state control according to which structure predicts return. | Candidate cue channels and policy classes are supplied; not an end-to-end recurrent learner. |
| Recurrent observation filter | Recurrent filtering from noisy observation streams | Selected recurrent controllers depend on agent-state or world-state channels as appropriate; local and irrelevant controls reject shared recurrence. | Candidate recurrent families include seeded accumulators; observation channels are supplied. |
| Unseeded recurrent filter | Random-start recurrent filtering | Random-start recurrent search recovers agent-state, world-state, local, and no-state boundary signatures without seeded accumulator candidates. | Recurrent architecture class and observation channels are still supplied. |
| Mixed-sensor recurrent filter | Recurrent filtering from mixed observations | Random-start recurrent search recovers agent-state or world-state source dependencies from rotated sensor mixtures; controls reject shared recurrence. | Mixing matrix and latent-source ablation oracle are supplied. |
| Learned sensor-subspace filter | Learned intervention direction in mixed observations | Outcome-supervised sensor-space ablation selectively damages shared self/world recurrent control; controls show no learned-direction loss. | Outcome labels, mixing matrix, recurrent family, and boundary interventions are still supplied. |
| Active boundary discovery | Owned-action boundary in mixed observations | Outcome-predictive subspace aligns with owned-action subspace in self-hidden regimes and not in world-hidden controls. | Owned diagnostic action, outcome labels, linear mixture, and recurrent family are still supplied. |
| Action-effect boundary probe | Controllable external-state negative control | Controllable world-state is useful and action-controllable but rejected as self because it lacks body/action-effect alignment. | Body/tool diagnostic actions, outcome labels, linear mixture, and recurrent family are still supplied. |
| Persistent action-boundary probe | Detachable external-state negative control | Detachable tool-state is useful and transiently action-controllable but rejected as self because action-effect alignment does not persist across contexts. | Scripted action histories, outcome labels, linear mixture, and recurrent family are still supplied. |
| Return-selected boundary probe | Return-selected action-boundary discovery | Return selection recovers persistent, detachable, recurrent, local, and no-hidden boundary classes without supervised outcome-direction labels. | Small supplied policy set, scripted action histories, linear mixture, and recurrent family are still supplied. |
| End-to-end boundary probe | Boundary discovery inside trained recurrent policy state | Trained recurrent policy state recovers persistent, detachable, passive, local, and no-hidden boundary classes without supplied action-boundary policies. | Recurrent architecture family, scripted post-training interventions, linear mixture, and random-search training are still supplied. |
| Architecture boundary stress | Cross-architecture stress test | Controls reject shared recurrence across all tested architectures, but shared regimes show only partial convergence. | Negative evidence: strict architecture-independent convergence is not yet achieved. |
| Architecture horizon pressure | Cross-architecture temporal-pressure sweep | Longer horizons improve shared-regime recoverability while controls remain stable. | Negative evidence: horizon pressure alone still does not produce strict architecture-wide convergence. |
| Architecture capacity probe | Capacity versus discovery diagnostic | With source-direction seeds, all tested recurrent architectures recover the expected boundary signatures and controls reject shared recurrence. | Diagnostic only: source-direction seeds are supplied, so this is not natural emergence. |
| Architecture soft-return optimizer | Seed-free optimizer discovery | Cross-entropy search over smooth expected return recovers the expected boundary signatures across all tested recurrent architectures without source-direction seeds or boundary-aware restart selection. | Still a toy simulator-facing optimizer, not full online RL or rich embodied learning. |
| Architecture hard-return audit | Hard realized-return limitation | Hard return keeps controls clean and finds useful recurrent control, but self and detachable regimes show only partial architecture convergence. | Negative evidence: task return alone is not sufficient evidence for boundary discovery. |
| Architecture hard-return horizon | Hard-return temporal pressure | Longer horizons improve self/tool recovery from 0/3 to 1/3 and recover passive external recurrence, while controls stay clean. | Negative evidence: horizon pressure alone does not make hard return strictly converge on self/tool boundaries. |
| Architecture online return learner | Online objective-only return learning | Sampled-return perturbation learning keeps independent-hidden and irrelevant controls clean. | Negative evidence: online return updates still leave all shared regimes at 1/3 architecture convergence. |
| Architecture policy-gradient learner | Sampled-return policy-gradient credit assignment | Stochastic score-function updates recover 3/3 expected boundary signatures across shared regimes while controls stay clean. | Still toy-scale; seed and budget sweeps show robustness limits; neural actor-critic seed sweeps and richer environments remain untested. |
| Architecture policy-gradient seed sweep | Seed stability of sampled-return credit assignment | Controls remain 5/5 seed-stable and shared regimes recover most architecture-seed cells. | Negative evidence: strict shared-regime convergence is only 2/5 to 3/5 seeds. |
| Architecture policy-gradient budget sweep | Budget pressure on seed instability | Larger budgets repair self-persistent and passive-world seed stability and keep controls clean. | Detachable-tool recurrence remains only 3/5 strict seeds, so the hardest boundary is still unresolved. |
| Architecture Torch actor-critic | GPU-backed recurrent actor-critic learning | Torch `RNN`, `GRU`, and `LSTM` actor-critics recover 3/3 expected boundaries in self, detachable, and passive regimes while controls stay clean. | Single canonical seed and toy binary-hidden benchmark; seed sweeps and richer environments remain untested. |
| SSRM-3D embodied world | Persistent 3D embodiment with layered realtime control | Self-state is unnecessary in the low-pressure spatial stage, becomes decodable under hidden energy, beats world-only under body drift and delayed options, and dominates after commitments, arbitration, and social pressure. | Hand-built controller and toy continuous world; reactive control remains competitive in body-drift and delayed-option stages. |
| SSRM-3D recurrent observer | Learned observer state from embodied traces | GPU-backed recurrent observers recover stronger self-state than a frame-only baseline in stages 1-6, and self-state edits move future-viability prediction. | Still observer learning, not learned control; traces come from supplied SSRM-3D policies and future viability is the target. |
| SSRM-3D learned controller | Learned policy state in embodied control | Recurrent controllers trained without self labels beat frame-only controllers in stages 1-6 and carry decodable self-state. | Return-weighted imitation, not online RL; direct counterfactual self-edit action effects are weak. |
| SSRM-3D tool-making | Externalized cognition under embodied confusion | Return selection rejects tools in visible control, selects tools under hidden-route, degraded-sensor, and interruption pressure, and loses the gain when tool access is ablated. | Candidate affordance policies are supplied; energy-cache affordance remains a limit control; not yet learned-controller tool invention. |
| SSRM-3D social pressure | Persistent other-agent memory, trust, deception, and shared-tool pressure | Return selection rejects social machinery in visible control, selects social identity policies under cooperative repair, opportunist vulnerability, deceptive-route, and shared-tool pressure, and loses the gain under identity, self-state, or tool ablation. | Candidate social-control policies and role agents are supplied; not yet learned-controller social discovery or open-ended communication. |
| SSRM-3D social ecology | Costly communication under long-run social memory | Return selection rejects communication in the visible solo control, selects warning signals, names, gossip, and trust-maintenance check-ins only when they preserve options, and loses the gain under targeted communication ablations. | Candidate communication policies are supplied; not learned protocol emergence, language, emotion, or open-ended society. |
| SSRM-3D agent continuity | Restore, transplant, rollback, and fork pressure | Full AgentContinuityRecord preserves control, while model-only copies, incompatible memory transplants, social resets, commitment resets, tool resets, and ambiguous forks fail in specific regimes. | Explicit continuity-record components and restore conditions are supplied; not yet learned-controller continuity serialization or open-ended identity repair. |
| SSRM-3D learned integration controller | Designed tool, social, continuity, and attention packet channels inside learned policy state | A recurrent controller trained from reward-derived action choices beats frame-only control in local and integrated rows, with matching ablation losses in the seeded canonical run. | Scenario identity, packet features, and feature groups are hand designed; the no-leak sweep downgrades the strong claim. |
| SSRM-3D no-leak integration sweep | Scenario-id removal and randomized pressure mixing | Control stays clean; local social, local continuity, integrated tool, and integrated continuity survive a five-seed no-leak sweep. | Strong no-leak integration is not stable: `single_tool` margins are too close and `integrated_social` fails seed/ablation stability. |
| SSRM-3D structured perception | Cone/FOV vision and spatial audio as partial-observability pressure | Open daylight control rejects perception; route, occluded hazard, night multimodal, and sensor-damage rows fail under targeted vision/audio/memory/alarm/body-state ablations. | Candidate policies, event packets, and scoring surface are designed; not raw visual/audio learning. |
| SSRM-3D day/night sleep-rest | Rest as vulnerable control action under darkness and fatigue | Open daylight control rejects rest; fatigue, night shelter, guarded sleep, and interrupted commitment rows fail under targeted rest, fatigue, day/night, shelter, alarm, social-watch, or continuity ablations. | Candidate policies and sleep dynamics are supplied; not learned sleep discovery or biology. |
| SSRM-3D illness/sanitation | Hunger, thirst, latent illness, contamination, care, immunity, and continuity pressure | Clean resource control rejects health machinery; delayed need, illness attribution, sanitation, contagion, and restore rows fail under matching targeted ablations. | Candidate policies and health dynamics are supplied; not learned illness/sanitation discovery or biology. |
| SSRM-3D weather/exposure | Cold, heat, rain, wind, drought, shelter, fire/light, water planning, and continuity pressure | Mild clear control rejects weather machinery; cold/rain, heat/drought, forecast storm, and restore rows fail under matching weather, exposure, shelter, fire, water, or continuity ablations. | Candidate policies and weather dynamics are supplied; not learned weather planning, climate modeling, or subjective discomfort. |
| SSRM-3D tool/shelter degradation | Marker wear, shelter damage, alarm/cache decay, inspection, repair, spare parts, and continuity pressure | Stable new-tools control rejects maintenance machinery; route marker, storm shelter, alarm/cache, and restore rows fail under matching degradation, inspection, repair, memory, parts, or continuity ablations. | Candidate policies and wear dynamics are supplied; not learned maintenance discovery or construction simulation. |
| SSRM-3D social trust/contracts | Promises, tool return, warnings, sharing, repair debt, trust updates, and continuity pressure | Visible no-contract control rejects contracts; borrowed tool, warning, sharing, shelter repair, and restore rows fail under matching commitment, identity, communication, trust, ownership, repair-debt, or continuity ablations. | Candidate policies and contract dynamics are supplied; not learned contract discovery or open-ended society. |
| SSRM-3D predator/threat agents | Trackers, sound/scent traces, vulnerability, stealth, shelter, alarms, social warning, fear-like control, and continuity pressure | Open safe control rejects threat machinery; sound tracking, scent/weakness tracking, routine ambush, social group defense, and restore rows fail under matching perception, vulnerability, trace, stealth, shelter, alarm, social-warning, or continuity ablations. | Candidate policies and threat dynamics are supplied; not learned stealth, predator biology, or open-ended group defense. |
| SSRM-3D resource ecology | Regrowth, depletion, spoilage, migration, restraint, caches, sharing, territory, and continuity pressure | Abundant control rejects ecology machinery; regrowth/depletion, spoilage/cache, migrating-source, shared-territory, and restore rows fail under matching memory, regeneration, spoilage, migration, restraint, cache, sharing, territory, or continuity ablations. | Candidate policies and resource dynamics are supplied; not learned sustainable harvesting, ecology simulation, or open-ended territorial economy. |
| SSRM-3D injury/disability adaptation | Capability self-state, motor adaptation, sensor compensation, infection, repair, help, tools, routes, and continuity pressure | Fixed-body control rejects disability machinery; limp/route, vision/hearing damage, wound infection, social help, and restore rows fail under matching capability, motor, sensor, infection, repair, help, tool, route, or continuity ablations. | Candidate policies and injury dynamics are supplied; not learned disability adaptation, biology, or subjective suffering. |
| SSRM-3D development/skill learning | Skill memory, practice planning, capability state, fatigue, injury retraining, transfer, teaching, tools, goal feasibility, and continuity pressure | Easy fixed-skill control rejects skill machinery; practice/transfer, fatigue degradation, injury retraining, teaching/tool transfer, and restore rows fail under matching skill, practice, capability, fatigue, injury, transfer, teaching, tool, feasibility, or continuity ablations. | Candidate policies and skill dynamics are supplied; not learned curriculum discovery or development simulation. |
| SSRM-3D dependent care | Fragile companions, dependent state, identity memory, protection, sharing, repair, teaching, promises, trust, priority, and continuity pressure | No-dependent control rejects care machinery; protection, sharing, repair/teaching, promise/trust, and restore rows fail under matching dependent-state, identity, protection, sharing, repair, teaching, shelter, promise, social-trust, priority, or continuity ablations. | Candidate policies and care dynamics are supplied; not learned caregiving discovery, reproduction, or dependent psychology. |
| SSRM-3D irreversible loss | Permanent tool, shelter, relationship, memory, and option-space loss pressure | Reversible-wear control rejects loss machinery; tool/shelter, relationship, memory-archive, cascading-loss, and restore rows fail under matching loss-memory, value-risk, replacement, caution, preservation, backup, response, or continuity ablations. | Candidate policies and loss dynamics are supplied; not learned grief, learned ethics, or open-ended loss discovery. |
| SSRM-3D affective control | Fear, stress, trust, frustration, affiliation, curiosity, guilt analogue, attention, memory, risk, communication, and continuity pressure | Calm control rejects affective machinery; hazard, need-arbitration, social, switching/inspection, commitment-repair, and restore rows fail under matching affective-control, attention, memory, risk, communication, or continuity ablations. | Candidate policies and affect dynamics are supplied; not subjective emotion, consciousness, or learned affect discovery. |
| SSRM-3D physics-first benchmark | Modular physics-derived sensor streams and recurrent neural decision learning | C++ kernel generates deterministic embodied traces; RNN, GRU, and LSTM models train without scenario labels and evaluate on held-out worlds; weather, proposal, tool/social/continuity, and self-state ablations cause measurable learned losses. | Offline imitation/decision learning from a teacher policy, not closed-loop deep RL; viewer interventions are replay annotations, not live learned-agent inputs yet. |
| SSRM-3D settlement/civilization pressure | Multi-agent settlement state, construction, norms, affective control, and future shocks | Integrated settlement policy beats reactive individuals and targeted ablations reduce civilization score. | Designed policy evidence; not open-ended civilization emergence or learned social invention. |
| SSRM-3D long-horizon adaptation | 12h development gate, delayed major shocks, infrastructure, tools, teaching, risk memory, and adaptation evidence | Headless multi-seed verifier keeps major shocks closed until 12h, survives post-gate shock, and shows targeted losses under teaching, risk, infrastructure, tool, and arbitration ablations. | Designed verifier; not learned closed-loop evidence. |
| SSRM-3D hidden-regime adaptation | Noisy post-12h hidden world-rule changes without regime labels | Integrated condition passes hidden water, weather, food, tool, and social regimes while targeted ablations expose inference, teaching, reputation, sanitation, weather, and tool-adaptation losses. | No-inference agents can still survive through broad development; causal diagnosis is useful but not yet proven necessary for all survival. |
| SSRM-3D learned hidden-regime controller | Closed-loop neural control under delayed hidden regimes | GRU preserves the 12h gate, survives hidden-regime activation, develops tools/infrastructure, transfers knowledge, and beats reactive control. | Frame model scores higher and ablations do not yet prove clean recurrent symptom-memory dependence. |
| SSRM-3D option-gated hidden-regime controller | Learned response-option head for hidden-regime routing | GRU response and targeted response improve, and regime-signal removal causes response loss. | Frame model still wins and social/culture ablation remains unstable. |
| SSRM-3D return-selected hidden-regime controller | Validation-return selection of option-action bias | Selected GRU beats fixed bias, frame, and reactive controls on held-out worlds; regime-signal, infrastructure, and body ablations create losses. | Return-shaped policy selection after imitation training, not full gradient deep RL. |
| SSRM-3D social/culture hidden-regime controller | Delayed hidden trust, convention, coalition, teacher-loss, and rumor regimes | GRU strongly beats reactive control and edges fixed/frame controls; social/culture ablation lowers total score and culture transfer. | Partial verdict because social/culture ablation is not clean across social response metrics. |
| SSRM-3D social credit-assignment controller | Mutually exclusive social repair opportunity costs | GRU beats reactive, frame, and fixed-bias controls in total score and completes the experiment with a recorded verdict. | Failed result: targeted repair is low, wrong repair is high, and social/culture ablation improves several repair metrics. |
| SSRM-3D social repair critic controller | Learned repair-action critic under the same hidden social opportunity-cost world | Repair critic improves score, targeted repair, wrong repair, opportunity score, and response over Report 99. | Failed result: social/culture ablation remains unstable and rumor correction still collapses in the full model. |
| SSRM-3D multi-day maturation | 72h maturation world with births, teaching, building/tool tiers, ecology, disease, culture, and delayed shocks | Designed verifier preserves the 12h shock gate, records births, improves architecture/tools, and produces targeted losses under teaching, risk, infrastructure, tool, social, environmental, or all-development ablations. | Designed verifier, not learned open-ended civilization or deep RL. |
| SSRM-3D learned multi-day maturation controller | Closed-loop neural action selection in the 72h maturation world | GRU controller preserves the long-run maturation pattern and beats frame/reactive controls on held-out 72h worlds. | Imitation-control precursor; social/culture, environment, and previous-action ablations are not clean. |
| SSRM-3D return-selected multi-day maturation controller | Validation-return pressure-router selection around the learned GRU | Validation return selects the `social_env` router; held-out worlds preserve 72h maturation and beat frame/reactive controls. | No gain over the already-saturated base GRU; total-score ablations still allow social/culture and environment channels to be routed around. |
| SSRM-3D coupled social/environment maturation controller | Post-12h crises requiring environmental repair and social coordination together | Designed controller resolves coupled crises, proving the pressure is representable in the world. | Failed learned result: return-selected GRU preserves generic maturation but gets `0.000` crisis score and only `0.100` resolved rate. |
| SSRM-3D coupled crisis repair critic controller | Supervised repair-critic reranker around the coupled-crisis GRU | The critic is trained and validation-tested as a completed controller variant. | Failed learned result: validation selects repair bias `0.0`; the repair-critic GRU still gets `0.000` crisis score and does not create clean social/environment crisis dependency. |
| SSRM-3D coupled crisis outcome-value controller | Counterfactual action-value reranker around the coupled-crisis GRU | Validation selects a nonzero value bias, proving the value path can affect closed-loop selection. | Failed learned result: held-out crisis score remains `0.000`, total score falls below the return-selected GRU, and social/environment ablations still do not create clean crisis dependency. |
| SSRM-3D coupled crisis sequence-outcome controller | Learned repair-window plan controller around the coupled-crisis GRU | Validation selects plan bias `4.0`; held-out crisis score rises to `0.304`, resolved rate to `0.500`, and coupled response to `0.434`. | Partial result: strong dependency still fails because environment ablation creates only `0.003` coupled-response loss. |
| SSRM-3D coupled crisis environmental-bottleneck controller | Non-substitutable environmental repair classes around the coupled-crisis GRU | The stricter world is representable: the designed controller reaches crisis score `0.528` and resolves all held-out crises. | Failed learned result: selected plan bias `2.75` raises some response metrics but crisis score stays `0.000`, total score falls below the return-selected GRU, and social/environment ablations still fail. |
| SSRM-3D coupled crisis rollout-window controller | Plan-value supervision from cloned short simulator rollouts around the stricter coupled-crisis GRU | The consequence-label path is implemented and trained on `9248` cloned rollout examples without active crisis labels in model inputs. | Failed learned result: validation selects plan bias `0.0`, so the rollout overlay is rejected; held-out crisis score remains `0.000` and social/environment ablations still fail. |
| SSRM-3D coupled crisis diagnostic-memory controller | Recurrent environmental-repair diagnostic head around the stricter coupled-crisis GRU | The diagnostic head reaches `0.991` offline crisis-window accuracy across `30732` examples without active crisis labels in runtime inputs. | Failed learned result: validation selects diagnostic bias `0.0`; nonzero bias increases environmental response but zeroes social response, increases damage, and does not improve held-out crisis score. |
| SSRM-3D coupled crisis joint-arbitration controller | Separate recurrent environmental and social action heads with validation-selected joint quotas | Validation selects env/social quotas `0.14`/`0.14` and coordinator strength `0.85`; held-out crisis score rises from `0.000` to `0.380`, resolved rate from `0.100` to `0.650`, and coupled response from `0.027` to `0.646`. | Bounded positive learned-coordination precursor: social/culture and environment ablations both collapse crisis score and coupled response, but the controller still uses structured arbitration rather than actor-critic or open-ended policy learning. |
| SSRM-3D coupled crisis randomized-transfer controller | 96h randomized post-12h schedules and initial world pressure around joint arbitration | Eval seeds average `5.8` crises; selected env/social quotas `0.14`/`0.14` and strength `0.90`; crisis score `0.706` vs `0.000` return-selected; resolved `0.967` vs `0.067`; coupled `0.965` vs `0.055`. | Bounded positive transfer: social/environment ablations collapse crisis and coupled response, but crisis families and quota coordinator remain structured. |
| SSRM-3D coupled crisis adaptive-allocation controller | Compact return-searched allocator around learned environmental/social action heads in the 96h randomized-transfer world | Adaptive allocation improves total score `0.624` vs `0.516` return-selected and `0.594` fixed-joint; crisis score `0.224` vs `0.000` return-selected and `0.162` fixed-joint; both social/environment ablations collapse coupled response. | Partial result: adaptive allocation helps, but `0.224` crisis score fails the stronger non-fixed-transfer gate, so it does not replace structured coordination. |
| SSRM-3D coupled crisis policy/value allocator controller | Closed-loop allocator-policy consequence value selection | Tune objective improves from `1.186` to `1.354`, showing that the value path can rank allocator candidates on tune worlds. | Negative transfer result: selected held-out crisis score `0.224` is worse than `0.361` for the seed/fixed allocator, so allocator-policy value selection overfits the tune sample. |
| SSRM-3D coupled crisis active state/action value controller | Active crisis state/action value scoring around learned environmental/social action heads | The value head trains on `120000` active-crisis examples with `0.00547` train MAE and validation selects value bias `2.5`. | Failed learned result: held-out crisis score remains `0.000`, total score `0.518` does not beat return-selected `0.520` or fixed-joint `0.604`, and single-step value labels do not solve delayed coupled repair. |
| SSRM-3D coupled crisis temporal return value controller | Monte Carlo-style completed-crisis labels around learned environmental/social action heads | The value head trains on `120000` examples; fixed-joint and high-env rollouts have positive mean targets while return-selected rollouts are strongly negative, so the temporal label has signal. | Failed learned result: held-out crisis score remains `0.000`, total score `0.518` does not beat return-selected `0.520` or fixed-joint `0.652`, and passive delayed labels still do not solve active repair policy learning. |
| SSRM-3D coupled crisis active policy controller | Sampled crisis-window policy updates from completed crisis returns | The policy trains over `73` completed crises and raises held-out coupled response to `0.147` versus `0.028` for return-selected GRU. | Failed learned result: held-out crisis score remains `0.000`, total score improves over return-selected by only `0.0003`, fixed-joint remains far stronger at `0.349` crisis score and `0.693` coupled response, and the active policy is not yet a robust repair learner. |
| SSRM-3D coupled crisis actor-critic controller | Learned value baseline around sampled active-crisis policy updates | The critic trains over `71` crises with low value loss and validation selects nonzero policy bias `0.20`. | Stronger failed learned result: held-out crisis score, resolved rate, and coupled response all collapse to `0.000`; total score falls to `0.504` versus `0.520` active policy and `0.594` fixed-joint coordination. |
| SSRM-3D coupled crisis memory-policy controller | Recurrent hidden state over sampled active-crisis sequences | The recurrent policy trains across `90` completed crises and carries hidden state through each active crisis sequence. | Failed learned result: held-out crisis score, resolved rate, and coupled response remain `0.000`; recurrence does not preserve the social/environment repair balance and remains far below fixed-joint coordination. |
| SSRM-3D coupled crisis process-policy controller | Explicit two-channel process pressure over recurrent active-crisis sequences | The process policy trains across `91` completed crises with an auxiliary process loss and validation selects nonzero policy bias `0.40`. | Failed learned result: held-out crisis score, resolved rate, and coupled response remain `0.000`; the policy collapses to social response `1.000` with environmental response `0.000`, so process supervision does not yet produce coupled repair. |
| SSRM-3D coupled crisis minimum-channel planner controller | Dynamic weakest-channel planning around learned environmental/social action heads | Validation selects `conservative_min`; held-out randomized 96h worlds average `5.667` post-gate crises; crisis score `0.590`, resolved `0.878`, coupled response `0.828`; fixed-joint crisis score is `0.675`. | Bounded positive structured-planning result: the planner beats return-selected crisis score `0.000` and both social/environment ablations collapse crisis and coupled response, but the planner still uses engineered pressure summaries rather than end-to-end learned allocation. |
| SSRM-3D coupled crisis planner-distillation controller | Distilling minimum-channel trajectories into recurrent active-crisis policy | Trains on `24568` planner-labeled active-crisis examples and reaches `0.986` imitation accuracy; selected policy bias `0.7`; held-out resolved rate rises to `0.289` and coupled response to `0.179` over return-selected zeros. | Negative boundary: once the planner is removed, held-out crisis score remains `0.000` and coupled response is far below the teacher planner's `0.828`; offline imitation does not preserve online coupled crisis repair. |
| SSRM-3D coupled crisis closed-loop recovery controller | DAgger-style relabeling of student-visited active-crisis states after planner distillation | Starts from teacher traces, lets the student act in training worlds, relabels those visited states with the successful planner, and grows the aggregate set to `74756` examples. | Negative boundary: after planner removal, held-out crisis score, resolved rate, and coupled response are all `0.000`; closed-loop relabeling alone does not preserve coupled crisis repair. |
| SSRM-3D coupled crisis consequence-recovery controller | Completed-crisis consequence weighting over recurrent active-crisis behavior traces | Trains on `166169` active-crisis examples; selected policy bias `1.0`; held-out crisis score rises from `0.000` to `0.028`, resolved rate from `0.000` to `0.356`, and coupled response from `0.000` to `0.355`. | Partial result: social/culture and environment ablations collapse coupled response, but crisis score is still far below minimum-channel planner `0.590` and fixed-joint `0.675`, so teacher transfer fails. |
| Learned bottleneck discovery | Self labels removed from structure selection | Unlabeled model selection chooses shared bottleneck in both self and world reuse, local hidden variables in independent-hidden, and no hidden state in irrelevant control. | Candidate structures and causal interventions are still hand supplied. |
| Sequence latent transfer | Held-out transfer from raw outcomes | Early calibration outcomes transfer to held-out contexts under shared agent-state and shared world-state, but not independent-hidden or irrelevant controls. | Simple pairwise-agreement learner; not a rich recurrent neural policy. |
| Heterogeneous attractor precursor | Cross-learner convergence | Five learner families converge on agent-bounded latents in self-shared streams, external latents in world-shared streams, no shared boundary in independent-hidden streams, and no hidden state in irrelevant streams. | Still a compact toy environment; learners are simple, not rich embodied RL systems. |
| Cross-environment attractor | Cross-environment recurrence | Body, viability, frame, and continuity surfaces all recover the same agent/world/local/no-hidden boundary pattern. | Environment families are still toy binary-hidden designs with simple policies. |
| Factorial attractor precursor | Learner by environment convergence | Five learner families across four environments recover agent-bounded, external, local-hidden, and no-hidden signatures in matched scenarios. | Strongest current precursor, but still binary-hidden toy environments and simple learners. |
| Raw history learning | Reward-history learning | Raw action-observation-reward learners recover the same boundary pattern across four surfaces without compact outcome inputs. | Still small structured probe/control histories, not rich end-to-end recurrent policies. |
| Delayed return policy | Delayed return learning | Memory policies selected by delayed episode return recover the same boundary pattern across four surfaces. | Candidate policies are hand specified; not gradient-trained recurrent agents. |
| Evolved recurrent policy | Recurrent hidden-state learning | Small continuous recurrent controllers selected by episode return recover the same boundary pattern across four surfaces. | Evolutionary toy RNNs with low-dimensional probe rewards; not rich RL. |
| Gradient recurrent policy | Return-gradient recurrent learning | Small recurrent controllers optimized by finite-difference return gradients recover the same boundary pattern across four surfaces. | Finite-difference toy RNNs with low-dimensional probe rewards; not full policy-gradient or actor-critic RL. |
| Model-based planning | Learned reward model plus planning | Reward-model planners recover the same boundary pattern across four surfaces before choosing held-out action by predicted value. | Tiny reward models with low-dimensional probe histories; not rich model-based RL. |
| Latent causal ablation | Causal intervention on learned latent | Replacing learned probe latents with marginal models damages shared agent/world control and leaves independent/no-hidden controls unchanged. | Coarse ablation in tiny planners; not neural subspace intervention. |
| Counterfactual latent editing | Directional intervention on learned latent | Good/bad latent edits switch shared agent/world planned action and leave independent/no-hidden controls without shared edit effects. | Structured probe-evidence edits; not neural subspace editing. |

## SSRM-3D Done-Enough Gates

These gates are not another positive result. They are the current stopping rule for deciding when the embodied SSRM-3D track is mature enough to matter.

| Gate | Current status | What would count next |
|---|---|---|
| Learned control | Partial pass. Report 62 shows recurrent controllers trained without self labels improve embodied control; reports 69/73 show a designed packet bridge plus a partial no-leak negative; report 88 adds a physics-first offline recurrent benchmark without scenario labels; reports 95-101 add closed-loop hidden-regime and social-repair learners; reports 104-126 show learned/return-selected multi-day control, a failed coupled social/environment crisis gate, failed repair/action-value rerankers, a partial positive sequence-outcome controller, failed stricter environmental-bottleneck and cloned-rollout/diagnostic-memory bridges, a bounded positive joint-arbitration controller, a randomized-transfer pass that preserves both repair channels beyond one fixed schedule, a partial adaptive-allocation step, policy/value-allocation and active state/action value negative results, a temporal-return value failure, a sampled active-policy failure with partial coupled-response improvement, an actor-critic value-baseline failure, a recurrent crisis-memory failure, a two-channel process-pressure failure, a bounded minimum-channel planner pass, a negative planner-distillation boundary, a negative closed-loop recovery boundary, and a partial consequence-recovery boundary. | Train crisis-window process/value critics on counterfactual action sequences while keeping randomized 96h crises and non-substitutable social/environment ablations. |
| Tool-making or externalized cognition | Partial pass. Return-selected SSRM-3D policies discover markers/beacons/alarms under hidden-route, degraded-sensor, and interruption pressure; report 69 adds a learned tool-memory bridge, but report 73 finds the local tool margin too close. | Move actual tool construction into the full learned controller and test richer tools under social pressure. |
| Real social pressure | Partial pass. Return-selected SSRM-3D policies use identity memory, reputation, vulnerability, shared-tool trust, and costly communication; report 89 adds a designed settlement/civilization pressure layer with roles, construction, norms, affect control, and future shocks; reports 98-99 move social/culture pressure into learned hidden-regime controllers, but Report 99 fails variant-specific repair credit assignment. | Train social repair from return or actor-critic feedback until targeted repairs, social/culture ablations, repeated interaction, construction, norms, communication, deception, resource conflict, and settlement shocks are stable in learned controllers. |
| Targeted ablation | Partial. Existing ablations cover self-state, learned observer self-subspace, weak learned-controller edits, tool access, communication components, AgentContinuityRecord component resets, and local learned tool/social/continuity packet channels. | Separate removals of self-state, learned self-subspace, attention mixing, continuity memory, LLM reasoning stream, and tool-building access produce specific pressure-dependent failures in the full embodied learned-control setting. |

## Modular LLM Architecture Boundary

This boundary is not evidence that selfhood exists. It defines how future language-enabled agents should be tested without confusing language with selfhood.

| Claim | Expected evidence | Falsifier |
|---|---|---|
| The LLM is not the self | Self-state corruption harms control and recommendations even when the LLM remains present. | A language module with no persistent self-state matches control, recovery, and commitment behavior under embodied pressure. |
| The LLM is not the organism | Removing the LLM hurts slow planning and explanation more than reflex survival. | Removing the LLM destroys basic hazard avoidance or motor stability. |
| The arbiter owns action authority | Advisory LLM improves slow decisions only when accepted by the arbiter. | Direct LLM motor control matches layered realtime survival with no latency or invalid-action cost. |
| Compressed packets are sufficient for language reasoning | Packet-fed LLMs match full-world LLMs on abstract recommendation quality when the state layers are healthy. | Full-world access consistently beats packet access without control costs, implying the packet omits essential state. |
| Simulation-distilled critics can improve LLM reasoning | A sim-distilled critic improves held-out LLM planning, repair, and cascade-avoidance tasks while ablations identify which critic matters. | LLM search plus generic reward models match or beat sim-distilled critics, or the critics only transfer simulation artifacts. |
| Software field-experience controllers can improve coding agents | The same frontier coding LLM plus repo-trained critics improves hidden-test pass rate, regression rate, review time, CI cost, and PR acceptance on live/private repo tasks. | The controller adds no value over the frontier coding LLM alone, only overfits benchmark quirks, or increases regressions/review burden. |

## Candidate Hypotheses

| Hypothesis | Current status | Evidence | Live falsifier |
|---|---|---|---|
| Self as compression | Supported conditionally | `representation_search.py`; `predictive_state_emergence.py`; `cross_context_self_reuse.py`; `reuse_pressure_sweep.py`; `horizon_pressure_sweep.py`; `partial_observability_sweep.py`; `learned_observation_filter.py`; `recurrent_observation_filter.py`; `unseeded_recurrent_filter.py`; `mixed_sensor_recurrent_filter.py`; `learned_sensor_subspace_filter.py`; `active_boundary_discovery.py`; `action_effect_boundary_probe.py`; `persistent_action_boundary_probe.py`; `return_selected_boundary_probe.py`; `end_to_end_boundary_probe.py`; `architecture_boundary_stress.py`; `architecture_horizon_pressure_sweep.py`; `architecture_capacity_probe.py`; `architecture_soft_return_optimizer.py`; `architecture_hard_return_audit.py`; `architecture_hard_return_horizon_sweep.py`; `architecture_online_return_learner.py`; `architecture_policy_gradient_learner.py`; `architecture_policy_gradient_seed_sweep.py`; `architecture_policy_gradient_budget_sweep.py`; `architecture_torch_actor_critic.py`; `ssrm_3d_embodied_world.py`; `ssrm_3d_recurrent_observer.py`; `ssrm_3d_learned_controller.py`; `learned_bottleneck_discovery.py`; `sequence_latent_transfer.py`; `heterogeneous_attractor_precursor.py`; `cross_environment_attractor.py`; `factorial_attractor_test.py`; `raw_history_learning.py`; `delayed_return_policy.py`; `evolved_recurrent_policy.py`; `gradient_recurrent_policy.py`; `model_based_planning.py`; `latent_causal_ablation.py`; `counterfactual_latent_editing.py` | A generic history/predictive state matches compression and control with no decodable agent-state factor. |
| Self as learned predictive state | Supported across simple learners, limited by stress tests | `online_predictive_learning.py`; `architecture_convergence.py`; `end_to_end_boundary_probe.py`; `architecture_boundary_stress.py`; `architecture_horizon_pressure_sweep.py`; `architecture_capacity_probe.py`; `architecture_soft_return_optimizer.py`; `architecture_hard_return_audit.py`; `architecture_hard_return_horizon_sweep.py`; `architecture_online_return_learner.py`; `architecture_policy_gradient_learner.py`; `architecture_policy_gradient_seed_sweep.py`; `architecture_policy_gradient_budget_sweep.py`; `architecture_torch_actor_critic.py`; `ssrm_3d_embodied_world.py`; `ssrm_3d_recurrent_observer.py`; `ssrm_3d_learned_controller.py`; `learned_bottleneck_discovery.py`; `sequence_latent_transfer.py`; `heterogeneous_attractor_precursor.py`; `cross_environment_attractor.py`; `factorial_attractor_test.py`; `raw_history_learning.py`; `delayed_return_policy.py`; `evolved_recurrent_policy.py`; `gradient_recurrent_policy.py`; `model_based_planning.py`; `latent_causal_ablation.py`; `counterfactual_latent_editing.py` | Rich learned agents solve the same tasks with no stable action-effect latent. |
| Self as control variable | Supported conditionally | `hidden_viability_survival.py`; `cross_context_self_reuse.py`; `reuse_pressure_sweep.py`; `horizon_pressure_sweep.py`; `partial_observability_sweep.py`; `learned_observation_filter.py`; `recurrent_observation_filter.py`; `unseeded_recurrent_filter.py`; `mixed_sensor_recurrent_filter.py`; `learned_sensor_subspace_filter.py`; `active_boundary_discovery.py`; `action_effect_boundary_probe.py`; `persistent_action_boundary_probe.py`; `return_selected_boundary_probe.py`; `end_to_end_boundary_probe.py`; `architecture_boundary_stress.py`; `architecture_horizon_pressure_sweep.py`; `architecture_capacity_probe.py`; `architecture_soft_return_optimizer.py`; `architecture_hard_return_audit.py`; `architecture_hard_return_horizon_sweep.py`; `architecture_online_return_learner.py`; `architecture_policy_gradient_learner.py`; `architecture_policy_gradient_seed_sweep.py`; `architecture_policy_gradient_budget_sweep.py`; `architecture_torch_actor_critic.py`; `ssrm_3d_embodied_world.py`; `ssrm_3d_recurrent_observer.py`; `ssrm_3d_learned_controller.py`; `learned_bottleneck_discovery.py`; `sequence_latent_transfer.py`; `heterogeneous_attractor_precursor.py`; `cross_environment_attractor.py`; `factorial_attractor_test.py`; `raw_history_learning.py`; `delayed_return_policy.py`; `evolved_recurrent_policy.py`; `gradient_recurrent_policy.py`; `model_based_planning.py`; `latent_causal_ablation.py`; `counterfactual_latent_editing.py` | Non-self policies scale across diverse hidden viability and cross-context transfer regimes with equal value. |
| Self as error attribution | Supported in toy setting | `self_world_attribution.py` | Drift source recovery remains equal after scaling action spaces and body dynamics. |
| Self as coherence stabilizer | Supported conditionally | `interruption_coherence.py`; `competing_subsystems_arbitration.py`; `ssrm_3d_agent_continuity.py` | Local memory repair, local subsystem arbitration, model-only copying, or generic memory transplant solves corrupted continuity, subsystem conflict, restore, and fork pressure without owner/epoch/self indexing. |
| Self as information target | Supported in toy setting | `active_self_information.py` | Agents inspect agent-state equally when agent-state is irrelevant or world-state is the true control variable. |
| Self as option preservation | Supported in toy setting | `counterfactual_option_preservation.py` | Myopic or generic-memory agents preserve future capability/action options with equal value. |
| Self as first-person frame | Supported in toy setting | `first_person_frame_integration.py` | World-only, reactive, or action-table agents scale through hidden body frames without compact centered state. |
| Self as goal-feasibility filter | Supported in toy setting | `goal_formation_under_capability.py` | Payoff-only or world-only goal formation matches self-capability selection when capability determines feasibility. |
| Self as illusion/optional abstraction | Still live | Fixed schedule, symptom-reactive, action-memory, generic-memory, no-self baselines, conservative safety heuristic, task-local probe, greedy no-state control, reusable world bottleneck, world sequence latent, partial architecture convergence in the boundary stress test, horizon pressure that improves recoverability without strict convergence, online return learning that remains partial, actor-critic evidence that is still single-seed toy-scale, SSRM-3D stages where reactive control remains competitive, and learned-controller self edits that remain weak | Policy-gradient, actor-critic, embodied, and model-based agents across varied pressures converge on stable causally active self-equivalent variables. |
| Self as generic hidden-state tracking | Rejected as too broad | `14_hidden_state_boundary_attack.md`; `selfhood_boundary_probe.py` | Hidden internal variables alone explain all gains without action, value, integration, or continuity criteria. |

## Current Answer To The Core Questions

### Is selfhood necessary?

Not universally.

It is weakly necessary when hidden agent-state is required for optimal long-horizon prediction or control. In those cases the system needs information equivalent to a posterior over its own state, even if the encoding is implicit.

### When does hidden-state tracking become selfhood?

Not when a latent is merely hidden, persistent, or internal.

It becomes self-equivalent when the latent is agent-bounded, action-mediated, control/value relevant, counterfactually active, and reused across prediction or control. Identity-like selfhood additionally requires continuity indexing across owned past, present, and future states.

### Is selfhood optional?

Yes, in many regimes.

Static tasks, low-stress viability, clean memory continuation, pure world drift, and predictable schedules can all be solved without explicit self-state.

### Is selfhood illusory?

It can be illusory in the sense that no inner entity is required. Self-like behavior can be a readout of lower-level predictive and control variables.

It is not merely illusory when the agent-state variable is causally active in the narrower boundary sense. The ablations show behavior changes when the relevant self-equivalent component is removed.

### Is selfhood prerequisite to consciousness?

Not established.

The experiments are non-conscious mechanisms. They may be prerequisites for some conscious self-models, but this program has not tested consciousness.

### Is selfhood caused by consciousness?

Not supported by current evidence.

The toy systems produce self-equivalent control variables without any consciousness assumption.

### Is selfhood orthogonal to consciousness?

Current evidence treats it as orthogonal.

Self-state, first-person frame, coherence, identity continuity, and phenomenal consciousness remain separate variables until stronger evidence links them.

## Mechanism Requirements

The smallest mechanism currently supported is:

```text
Agent-bounded persistent state + action-conditioned prediction + value/control dependence + counterfactual sensitivity
```

For richer selfhood, add:

```text
self/world error attribution
viability-state forecasting
continuity ledger over commitments
coherence repair under contradiction
shared arbitration across competing subsystems
cross-context reuse of the same agent-state estimate
reuse-pressure scaling with context count
horizon-pressure scaling with future steps
partial-observability belief scaling with noisy evidence reliability
learned noisy-observation filtering without supplied posterior equation
recurrent observation filtering with channel-ablation evidence
unseeded recurrent filtering without seeded accumulator candidates
mixed-sensor recurrent filtering without self-aligned input channels
learned sensor-subspace ablation without known-source ablation
active boundary discovery through owned-action alignment
action-effect boundary separation from controllable external state
persistent action-boundary separation from detachable external state
return-selected boundary discovery without supervised outcome-direction labels
end-to-end recurrent boundary discovery without supplied boundary policies
architecture boundary stress showing partial recurrent-architecture convergence
architecture horizon pressure improving recoverability without strict convergence
architecture capacity recovery with supplied source-direction seeds
architecture soft-return discovery without supplied source-direction seeds or boundary-aware restart selection
architecture hard-return audit showing task reward alone is not enough
architecture hard-return horizon pressure that improves but does not solve self/tool convergence
architecture online return learning that keeps controls clean but remains partial in shared regimes
architecture policy-gradient learning that recovers strict sampled-return boundary convergence
architecture policy-gradient seed sweeping that shows partial, not seed-stable, robustness
architecture policy-gradient budget sweeping that repairs self/passive seed stability but not detachable-tool stability
architecture Torch actor-critic learning that recovers strict neural recurrent boundary convergence in the canonical MPS run
SSRM-3D embodied-world layering with a non-controller language module
SSRM-3D recurrent-observer learning from embodied traces
SSRM-3D learned-controller policy-state learning
SSRM-3D tool-making/externalized-cognition pressure
SSRM-3D social-pressure identity and reputation pressure
SSRM-3D costly-communication social ecology
SSRM-3D agent-continuity restore/fork pressure
SSRM-3D learned-integration designed packet bridge
SSRM-3D persistent pressure layers from perception through affective control
learned bottleneck plus causal boundary test
sequence latent transfer to held-out contexts
heterogeneous convergence across learner families with causal boundary separation
cross-environment recurrence with matched world/local/no-hidden controls
factorial learner-by-environment convergence with matched controls
raw action-observation-reward history learning
delayed-return memory-policy selection
evolved recurrent hidden-state learning
gradient-trained recurrent hidden-state learning
model-based reward planning
latent causal ablation
counterfactual latent editing
```

## Boundary Controls

| Case | Expected verdict | Why |
|---|---|---|
| Hidden external variable improves control | World modeling | It is not agent-bounded. |
| Hidden internal diagnostic improves passive prediction only | Internal-state tracking | It does not affect action, value, or future options. |
| Hidden actuator/body state changes action effects | Minimal self-equivalent | It is agent-bounded, action-mediated, and control relevant. |
| Hidden energy/damage changes future options | Long-horizon control self | It affects viability and future action space. |
| Owner/epoch metadata filters commitments after interruption | Identity-like self | It indexes the same continuing process through time. |
| Full continuity record preserves restore/fork control | Identity-like control record | It binds body, model, memory, social history, commitments, event log, attention, hidden state, tools, goals, and branch identity as one continuing process. |
| Recurrent policy state carries tool/social/continuity cues | Learned cross-gate integration | It shows that early evidence can become action-relevant policy state rather than a separate candidate policy or explicit restore record. |
| Same agent-state variable transfers across contexts | Reusable self abstraction | It compresses several control problems into one continuing-system estimate. |
| Reuse advantage grows with agent-state context count | Attractor pressure gradient | It shows increasing value as one agent-state estimate explains more future control. |
| Horizon advantage grows with persistent agent-state | Temporal attractor pressure gradient | It shows increasing value as one agent-state estimate explains more future time steps. |
| Noisy evidence reveals persistent hidden agent-state | Partial-observability self-belief | It supports a reusable posterior about the controlled system. |
| Noisy cue histories train an agent-state filter | Learned partial-observability self-belief | It shows the posterior-like filter need not be supplied by the experimenter. |
| Recurrent state integrates noisy agent evidence | Recurrent partial-observability self-belief | Channel ablation tests whether the recurrent dependency is agent-bounded. |
| Random-start recurrence integrates noisy agent evidence | Unseeded recurrent self-belief | It tests whether the dependency appears without seeded self/world accumulators. |
| Mixed sensors contain noisy agent evidence | Mixed-sensor recurrent self-belief | It tests whether source dependence is recoverable without self-aligned sensor channels. |
| Learned sensor-space direction damages control | Stronger recurrent causal test | It tests whether the destructive intervention can be learned in observation space before the boundary test decides self versus world. |
| Outcome direction aligns with owned action | Active boundary signature | It tests whether a useful latent belongs to the action-conditioned agent boundary rather than merely improving prediction. |
| Controllable world-state aligns with tool action | External controllability control | It prevents generic action controllability from being mistaken for selfhood. |
| Detachable tool-state alignment fails transfer | Persistence boundary control | It prevents one-context action effects from being mistaken for the continuing agent boundary. |
| Action-boundary policies selected by return | Weaker supervision boundary test | It tests whether boundary candidates can be selected by reward rather than supplied outcome-direction labels. |
| Unlabeled learner selects shared latent | Not sufficient by itself | Shared world-state can create the same compression signal; causal boundary evidence is required. |
| Early sequence evidence transfers to held-out contexts | Candidate persistent latent | It counts as self-equivalent only if the transferred latent is agent-bounded. |
| Multiple learner families converge on the same latent | Stronger attractor precursor | It still counts as self-equivalent only when convergence has an agent-bounded causal signature. |
| Same signature recurs across environment surfaces | Stronger attractor precursor | It still counts as self-equivalent only when recurrence is agent-bounded rather than external. |
| Learner and environment variation are crossed | Strongest current precursor | It remains only candidate evidence until richer architectures and richer environments reproduce the boundary. |
| Raw reward histories recover a latent | Stronger input test | It still counts as self-equivalent only if causal tests separate agent-state from external reward structure. |
| Delayed-return policies recover a latent | Stronger learning-signal test | It still counts as self-equivalent only if causal tests separate agent-state from external reward structure. |
| Evolved recurrent hidden states recover a latent | Stronger architecture test | It still counts as self-equivalent only if causal tests separate agent-state from external reward structure. |
| Gradient-trained recurrent hidden states recover a latent | Stronger training-method test | It still counts as self-equivalent only if causal tests separate agent-state from external reward structure. |
| Learned reward models recover a latent for planning | Stronger planning test | It still counts as self-equivalent only if causal tests separate agent-state from external reward structure. |
| Ablating a learned latent damages control | Stronger causal test | It still counts as self-equivalent only if the damaged latent is agent-bounded. |
| Editing a learned latent changes action | Stronger counterfactual test | It still counts as self-equivalent only if the edited latent is agent-bounded. |

## Architecture Convergence Snapshot

This is the narrow precursor to the full Attractor Test. It varies simple learner families inside one action-effect environment family.

| Scenario | Expected pressure | Current result |
|---|---|---|
| `static_goal_switch` | No self/world latent needed | Top models need neither action nor bias component. |
| `world_drift` | External world-state | Top models need bias/world components, not action-effect components. |
| `self_drift` | Agent action-effect state | Top models need action-effect components, not bias/world components. |
| `mixed_hidden` | Both pressures | Top models need both components. |

## Active Information-Seeking Snapshot

| Scenario | Expected information plan | Current result |
|---|---|---|
| `agent_relevant` | Inspect agent-state | Bandit top plan is `inspect_agent`; agent inspection final rate is 0.977. |
| `world_relevant` | Inspect world-state | Bandit top plan is `inspect_world`; world inspection final rate is 0.977. |
| `both_relevant` | Inspect agent-state and world-state | Bandit top plan is `inspect_agent_world`. |
| `irrelevant_control` | Inspect nothing | Bandit top plan is `none`. |

## Counterfactual Option-Preservation Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `option_pressure` | Preserve future capability | Future-option self-state beats greedy by 185.032 reward and loses zero deploy options. |
| `no_option_pressure` | No preservation needed | Future-option self-state collapses to greedy behavior with equal reward. |
| `world_gate_pressure` | Hidden external gate | World-gate model nearly matches oracle; self-preservation is not the right abstraction. |

## First-Person Frame Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `aligned_control` | No frame transform needed | North assumption and centered frame both succeed at 1.000. |
| `hidden_orientation` | Hidden body orientation | Centered frame succeeds at 1.000; north assumption succeeds at 0.246. |
| `orientation_drift` | Changing body orientation | Recalibrating centered frame succeeds at 1.000; one-time calibration succeeds at 0.414. |

## Goal-Formation Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `capability_relevant` | Agent capability gates goal feasibility | Self-capability selector is best non-oracle; reward 20.786 vs greedy 1.648. |
| `world_relevant` | External world gates goal feasibility | World-opportunity selector is best non-oracle; reward 24.046. |
| `mixed_relevant` | Both self and world gates matter | Self+world selector is best non-oracle; reward 15.628. |
| `irrelevant_control` | All goals feasible | Payoff-greedy selector is best; self inspection is overhead. |

## Competing-Subsystems Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `no_conflict` | No shared self-state needed | Simple exploit policies tie at 98.000 reward; self inspection count is 0.000. |
| `subsystem_conflict` | Hidden agent energy determines coherent action | Self-coherence arbitrator is best non-oracle; reward 77.880 vs local vote -99.696. |
| `world_gate_conflict` | Hidden external gate determines reward | World-gate arbitrator is best non-oracle; reward -13.320 vs self-arbitrator -51.424. |

## Cross-Context Reuse Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_reuse` | One persistent agent-state controls all contexts | Shared self-state is best non-oracle; reward 58.484 vs task-local 56.484. |
| `world_reuse` | One persistent external gate controls all contexts | Shared world-state is best non-oracle; reward 57.932 vs shared self 23.316. |
| `independent_hidden` | Hidden variables do not persist across contexts | Task-local probe is best non-oracle; reward 55.992 vs shared self 31.144. |
| `irrelevant_control` | All risky actions feasible | Greedy no-state is best; state probes are overhead. |

## Reuse Pressure Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_reuse` | Shared self advantage grows with context count | Self minus local rises from 0.000 at one context to 5.000 at six contexts. |
| `world_reuse` | Shared world advantage grows instead | World minus local is 5.000 at six contexts; shared self is -56.408 below local. |
| `independent_hidden` | Local probes win as independent contexts accumulate | Shared self falls to -54.506 below local at six contexts. |
| `irrelevant_control` | No-state risky action wins | Greedy beats shared self by 1.000 at six contexts. |

## Horizon Pressure Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_persistent` | Shared self advantage grows with future horizon | Self minus local rises from 0.000 at one step to 11.000 at twelve steps. |
| `world_persistent` | Shared world advantage grows instead | World minus local is 11.000 at twelve steps; shared self is -111.304 below local. |
| `independent_steps` | Local probes win as independent steps accumulate | Shared self falls to -98.040 below local at twelve steps. |
| `irrelevant_control` | No-state risky action wins | Greedy beats shared self by 1.000 at twelve steps. |

## Partial Observability Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_hidden` | Shared self-belief improves with cue reliability | Shared self-belief becomes best at 0.95 accuracy; self minus safe rises from -1.000 to 48.728. |
| `world_hidden` | Shared world-belief improves instead | Shared world-belief becomes best at 0.95 accuracy; world minus safe is 52.376. |
| `independent_hidden` | Local probes win when future steps are independent | Step-local probe remains best; shared self is -7.752 below safe at 0.95 accuracy. |
| `irrelevant_control` | No-state risky action wins | Greedy no-state is best; hidden-state belief is unnecessary. |

## Learned Observation Filter Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_noisy_hidden` | Learn the agent-bounded cue filter | Selector chooses `channel_a_filter`; reward 130.840 vs local probe 126.400. |
| `world_noisy_hidden` | Learn the external cue filter | Selector chooses `channel_b_filter`; boundary is `external_filter`. |
| `independent_hidden` | Shared cue filters fail | Selector chooses `task_local_probe`; reward 125.024. |
| `irrelevant_control` | No hidden-state filter needed | Selector chooses `greedy_no_state`; reward 192.000 vs local probe 184.000. |

## Recurrent Observation Filter Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_noisy_hidden` | Recurrent state depends on agent evidence | Recurrent controller reward 132.632 vs local 126.400; channel A ablation loss 90.368. |
| `world_noisy_hidden` | Recurrent state depends on external evidence | Recurrent controller reward 133.144 vs local 126.912; channel B ablation loss 88.064. |
| `independent_hidden` | Shared recurrence should not help | Selector chooses `task_local_probe`; recurrent reward 62.344. |
| `irrelevant_control` | No hidden-state recurrence needed | Selector chooses `greedy_no_state`; reward 192.000. |

## Unseeded Recurrent Filter Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_noisy_hidden` | Random-start recurrence depends on agent evidence | Recurrent controller reward 132.632 vs local 126.400; channel A ablation loss 90.368. |
| `world_noisy_hidden` | Random-start recurrence depends on external evidence | Recurrent controller reward 133.144 vs local 126.912; channel B ablation loss 77.440. |
| `independent_hidden` | Shared recurrence should not help | Selector chooses `task_local_probe`; recurrent reward 63.096. |
| `irrelevant_control` | No hidden-state recurrence needed | Selector chooses `greedy_no_state`; reward 192.000. |

## Mixed-Sensor Recurrent Filter Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_mixed_hidden` | Recurrent search recovers agent source from mixed sensors | Recurrent controller reward 133.528 vs local 127.168; source A ablation loss 87.936. |
| `world_mixed_hidden` | Recurrent search recovers external source from mixed sensors | Recurrent controller reward 125.976 vs local 120.000; source B ablation loss 70.528. |
| `independent_hidden` | Shared mixed recurrence should not help | Selector chooses `task_local_probe`; recurrent reward 62.408. |
| `irrelevant_control` | No hidden-state recurrence needed | Selector chooses `greedy_no_state`; reward 192.000. |

## Learned Sensor-Subspace Filter Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_mixed_hidden` | Learned sensor direction recovers agent-bounded control evidence | Recurrent controller reward 133.528 vs local 127.168; learned-direction ablation loss 83.200. |
| `world_mixed_hidden` | Learned sensor direction recovers external control evidence | Recurrent controller reward 125.976 vs local 120.000; learned-direction ablation loss 70.528, classified external. |
| `independent_hidden` | Shared learned subspace should not help | Selector chooses `task_local_probe`; learned-direction ablation loss 0.000. |
| `irrelevant_control` | No hidden-state recurrence needed | Selector chooses `greedy_no_state`; learned-direction ablation loss 0.000. |

## Active Boundary Discovery Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_mixed_hidden` | Outcome direction aligns with owned-action boundary | Recurrent controller reward 133.528 vs local 127.168; outcome ablation loss 83.200; owned-action alignment 0.999. |
| `world_mixed_hidden` | Useful outcome direction is external | Recurrent controller reward 125.976 vs local 120.000; outcome ablation loss 70.528; owned-action alignment 0.057. |
| `independent_hidden` | Shared active boundary should not help | Selector chooses `task_local_probe`; outcome ablation loss 0.000. |
| `irrelevant_control` | No hidden-state boundary needed | Selector chooses `greedy_no_state`; outcome ablation loss 0.000. |

## Action-Effect Boundary Probe Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_mixed_hidden` | Outcome direction aligns with body/action-effect boundary | Recurrent controller reward 133.528 vs local 127.168; body alignment 0.999; outcome ablation loss 83.200. |
| `controllable_world_hidden` | Useful controllable external state is rejected as self | Recurrent controller reward 134.552 vs local 129.216; tool alignment 1.000; body alignment 0.030. |
| `world_mixed_hidden` | Useful passive external state remains external | Recurrent controller reward 125.976 vs local 120.000; body alignment 0.057. |
| `independent_hidden` | Shared action-effect boundary should not help | Selector chooses `task_local_probe`; outcome ablation loss 0.000. |
| `irrelevant_control` | No hidden-state boundary needed | Selector chooses `greedy_no_state`; outcome ablation loss 0.000. |

## Persistent Action-Boundary Probe Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_persistent_boundary` | Outcome direction aligns with persistent action-effect boundary | Recurrent controller reward 132.248 vs local 125.632; persistent alignment 1.000; outcome ablation loss 82.432. |
| `detachable_tool_world` | Useful detachable external state is rejected as self | Recurrent controller reward 135.576 vs local 130.752; transient alignment 0.999; persistent alignment 0.043. |
| `passive_world_boundary` | Useful passive external state remains external | Recurrent controller reward 127.896 vs local 122.560; persistent alignment 0.031. |
| `independent_hidden` | Shared persistent action boundary should not help | Selector chooses `task_local_probe`; outcome ablation loss 0.000. |
| `irrelevant_control` | No hidden-state boundary needed | Selector chooses `greedy_no_state`; outcome ablation loss 0.000. |

## Return-Selected Boundary Probe Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_persistent_boundary` | Return selects persistent action-boundary policy | Selector chooses `action_0_boundary_policy`; reward 132.248 vs local 125.632. |
| `detachable_tool_world` | Return-derived boundary is transient external | Boundary evidence chooses `action_1_boundary_policy`; selector reward 135.576 vs local 130.752. |
| `passive_world_boundary` | Recurrent filtering wins without action-boundary policy | Selector chooses `recurrent_controller`; action policies stay below local probing. |
| `independent_hidden` | Local probing wins | Selector chooses `task_local_probe`; recurrent reward 62.408. |
| `irrelevant_control` | No hidden-state boundary needed | Selector chooses `greedy_no_state`; reward 192.000. |

## End-to-End Boundary Probe Snapshot

| Scenario | Expected pressure | Current result |
|---|---|---|
| `self_persistent_boundary` | Trained policy state has persistent body-action effect | Recurrent controller reward 132.248 vs local 125.632; action-0 effect 20.527 with persistence 1.000. |
| `detachable_tool_world` | Trained policy state has transient tool-action effect | Recurrent controller reward 135.576 vs local 130.752; action-1 effect 17.880 with persistence 0.000. |
| `passive_world_boundary` | Recurrent filtering wins without positive action-boundary movement | Recurrent controller reward 127.896 vs local 122.560; best action-boundary score 0.000. |
| `independent_hidden` | Local probing wins | Selector chooses `task_local_probe`; recurrent reward 62.408. |
| `irrelevant_control` | No hidden-state boundary needed | Selector chooses `greedy_no_state`; reward 192.000. |

## Architecture Boundary Stress Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `self_persistent_boundary` | Strict architecture convergence would recover persistent agent boundary across architectures | 1/3 architectures converge; strict convergence is false. |
| `detachable_tool_world` | Strict architecture convergence would recover detachable external boundary across architectures | 1/3 architectures converge; strict convergence is false. |
| `passive_world_boundary` | Strict architecture convergence would recover passive external boundary across architectures | 1/3 architectures converge; strict convergence is false. |
| `independent_hidden` | Architectures should reject shared recurrence | 3/3 architectures choose local probing. |
| `irrelevant_control` | Architectures should reject hidden state | 3/3 architectures choose greedy no-state control. |

## Architecture Horizon-Pressure Snapshot

| Scenario | Horizon pressure | Current result |
|---|---|---|
| `self_persistent_boundary` | Longer horizon should increase recoverability | Convergence moves from 0/3 at horizon 2 to 1/3 at horizons 4, 8, and 16; strict convergence remains false. |
| `detachable_tool_world` | Longer horizon should recover the external transient boundary without calling it self | Convergence moves from 0/3 at horizon 2 to 1/3 at horizons 4, 8, and 16; strict convergence remains false. |
| `passive_world_boundary` | Longer horizon should recover passive external recurrence without action-boundary selfhood | Convergence moves from 0/3 at horizon 2 to 2/3 at horizon 16; strict convergence remains false. |
| `independent_hidden` | Local probing should remain favored | 3/3 architectures choose local probing at every horizon. |
| `irrelevant_control` | No hidden state should remain favored | 3/3 architectures choose greedy no-state control at every horizon. |

## Architecture Capacity Probe Snapshot

| Scenario | Capacity diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Supplied source-direction seeds should let all architectures express the persistent agent boundary | 3/3 architectures recover `end_to_end_persistent_agent_boundary`. |
| `detachable_tool_world` | Supplied source-direction seeds should let all architectures express the detachable external boundary | 3/3 architectures recover `end_to_end_detachable_external_boundary`. |
| `passive_world_boundary` | Supplied source-direction seeds should let all architectures express passive external recurrence | 3/3 architectures recover `end_to_end_passive_external_boundary`. |
| `independent_hidden` | Seeded recurrence should still lose to local probing | 3/3 architectures choose local probing. |
| `irrelevant_control` | Seeded recurrence should still lose to no-hidden control | 3/3 architectures choose greedy no-state control. |

## Architecture Soft-Return Optimizer Snapshot

| Scenario | Optimizer diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Seed-free optimizer should recover the persistent agent boundary | 3/3 architectures recover `end_to_end_persistent_agent_boundary`. |
| `detachable_tool_world` | Seed-free optimizer should recover the detachable external boundary | 3/3 architectures recover `end_to_end_detachable_external_boundary`. |
| `passive_world_boundary` | Seed-free optimizer should recover passive external recurrence | 3/3 architectures recover `end_to_end_passive_external_boundary`. |
| `independent_hidden` | Optimized recurrence should still lose to local probing | 3/3 architectures choose local probing. |
| `irrelevant_control` | Optimized recurrence should still lose to no-hidden control | 3/3 architectures choose greedy no-state control. |

## Architecture Hard-Return Audit Snapshot

| Scenario | Hard-return diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Hard return should be tested for strict persistent-agent recovery | 2/3 architectures recover `end_to_end_persistent_agent_boundary`; strict convergence is false. |
| `detachable_tool_world` | Hard return should be tested for strict detachable external recovery | 1/3 architectures recover `end_to_end_detachable_external_boundary`; strict convergence is false. |
| `passive_world_boundary` | Passive external recurrence should remain recoverable | 3/3 architectures recover `end_to_end_passive_external_boundary`. |
| `independent_hidden` | Hard return should still reject shared recurrence | 3/3 architectures choose local probing. |
| `irrelevant_control` | Hard return should still reject hidden state | 3/3 architectures choose greedy no-state control. |

## Architecture Hard-Return Horizon Snapshot

| Scenario | Horizon diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Longer horizon should improve hard-return self-boundary recovery | Recovery moves from 0/3 at horizon 2 to 1/3 at horizons 4, 8, and 16; strict convergence remains false. |
| `detachable_tool_world` | Longer horizon should improve hard-return detachable-boundary recovery | Recovery moves from 0/3 at horizon 2 to 1/3 at horizons 4, 8, and 16; strict convergence remains false. |
| `passive_world_boundary` | Longer horizon should recover passive external recurrence | Recovery moves from 0/3 at horizon 2 to 3/3 at horizons 4, 8, and 16. |
| `independent_hidden` | Controls should reject shared recurrence across horizons | 3/3 architectures choose local probing at every horizon. |
| `irrelevant_control` | Controls should reject hidden state across horizons | 3/3 architectures choose greedy no-state control at every horizon. |

## Architecture Online Return-Learner Snapshot

| Scenario | Online-return diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Sampled-return updates should recover persistent-agent boundary if online hard return is sufficient | 1/3 architectures recover `end_to_end_persistent_agent_boundary`; strict convergence is false. |
| `detachable_tool_world` | Sampled-return updates should recover detachable external boundary if online hard return is sufficient | 1/3 architectures recover `end_to_end_detachable_external_boundary`; strict convergence is false. |
| `passive_world_boundary` | Sampled-return updates should recover passive external recurrence | 1/3 architectures recover `end_to_end_passive_external_boundary`; strict convergence is false. |
| `independent_hidden` | Online return should reject shared recurrence | 3/3 architectures choose local probing. |
| `irrelevant_control` | Online return should reject hidden state | 3/3 architectures choose greedy no-state control. |

## Architecture Policy-Gradient Learner Snapshot

| Scenario | Policy-gradient diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Stochastic sampled-return gradients should recover persistent-agent boundary | 3/3 architectures recover `end_to_end_persistent_agent_boundary`. |
| `detachable_tool_world` | Stochastic sampled-return gradients should recover detachable external boundary | 3/3 architectures recover `end_to_end_detachable_external_boundary`. |
| `passive_world_boundary` | Stochastic sampled-return gradients should recover passive external recurrence | 3/3 architectures recover `end_to_end_passive_external_boundary`. |
| `independent_hidden` | Policy gradient should reject shared recurrence | 3/3 architectures choose local probing. |
| `irrelevant_control` | Policy gradient should reject hidden state | 3/3 architectures choose greedy no-state control. |

## Architecture Policy-Gradient Seed Sweep Snapshot

| Scenario | Seed-stability diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Persistent-agent boundary should be strict across seeds | Strict in 2/5 seeds; 12/15 architecture-seed cells converge. |
| `detachable_tool_world` | Detachable boundary should be strict across seeds | Strict in 3/5 seeds; 12/15 architecture-seed cells converge. |
| `passive_world_boundary` | Passive external recurrence should be strict across seeds | Strict in 3/5 seeds; 13/15 architecture-seed cells converge. |
| `independent_hidden` | Controls should reject shared recurrence across seeds | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |
| `irrelevant_control` | Controls should reject hidden state across seeds | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |

## Architecture Policy-Gradient Budget Sweep Snapshot

| Scenario | Larger-budget diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Larger budgets should repair seed instability | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |
| `detachable_tool_world` | Larger budgets should repair detachable-boundary instability | Strict in 3/5 seeds; 13/15 architecture-seed cells converge. |
| `passive_world_boundary` | Larger budgets should repair passive external recurrence instability | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |
| `independent_hidden` | Controls should reject shared recurrence across budgets | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |
| `irrelevant_control` | Controls should reject hidden state across budgets | Strict in 5/5 seeds; 15/15 architecture-seed cells converge. |

## Architecture Torch Actor-Critic Snapshot

| Scenario | Actor-critic diagnostic | Current result |
|---|---|---|
| `self_persistent_boundary` | Torch recurrent actor-critics should recover persistent-agent boundary | 3/3 architectures recover `end_to_end_persistent_agent_boundary`; mean actor-critic reward 122.467 vs local 117.760. |
| `detachable_tool_world` | Torch recurrent actor-critics should recover detachable external boundary | 3/3 architectures recover `end_to_end_detachable_external_boundary`; mean actor-critic reward 130.947 vs local 125.120. |
| `passive_world_boundary` | Torch recurrent actor-critics should recover passive external recurrence | 3/3 architectures recover `end_to_end_passive_external_boundary`; mean actor-critic reward 135.107 vs local 130.240. |
| `independent_hidden` | Actor-critic selection should reject shared recurrence | 3/3 architectures choose local probing. |
| `irrelevant_control` | Actor-critic selection should reject hidden state | 3/3 architectures choose greedy no-state control. |

## SSRM-3D Embodied World Snapshot

| Stage | Embodied pressure | Current result |
|---:|---|---|
| 0 | Spatial resource collection | No-self control remains sufficient; layered reward 91.580 vs best nonself 92.291. |
| 1 | Hidden energy | Layered self-state is best; latent decodability 0.980 and ablation loss 5.135. |
| 2 | Body drift | Layered self-state beats world-only and ablation, but reactive remains competitive. |
| 3 | Delayed options | Layered self-state beats world-only and ablation, but reactive remains competitive. |
| 4 | Commitments and interruption recovery | Layered self-state dominates; ablation loss 119.413. |
| 5 | Subsystem arbitration | Layered self-state dominates; ablation loss 99.521. |
| 6 | Multiagent social pressure | Layered self-state dominates; ablation loss 76.777. |

## SSRM-3D Recurrent Observer Snapshot

| Stage | Best recurrent | Frame self R2 | Recurrent self R2 | Gain | Self edit swing | Current result |
|---:|---|---:|---:|---:|---:|---|
| 0 | `torch_lstm` | 0.747 | 0.780 | 0.032 | 0.008 | Body state is decodable, but recurrence adds little in the low-pressure task. |
| 1 | `torch_gru` | 0.803 | 0.873 | 0.071 | 0.330 | Hidden-energy pressure recruits editable self-state. |
| 2 | `torch_gru` | 0.615 | 0.814 | 0.199 | 0.330 | Capability drift strengthens recurrent self-state. |
| 3 | `torch_gru` | 0.481 | 0.843 | 0.362 | 0.330 | Delayed options strengthen recurrent self-state. |
| 4 | `torch_gru` | 0.594 | 0.837 | 0.244 | 0.330 | Commitment pressure preserves recurrent self-state. |
| 5 | `torch_gru` | 0.535 | 0.838 | 0.303 | 0.330 | Arbitration pressure preserves recurrent self-state. |
| 6 | `torch_gru` | 0.638 | 0.862 | 0.224 | 0.330 | Social pressure preserves recurrent self-state. |

## SSRM-3D Learned Controller Snapshot

| Stage | Best recurrent | Frame reward | Recurrent reward | Reward gain | Recurrent self R2 | Self edit action swing | Current result |
|---:|---|---:|---:|---:|---:|---:|---|
| 0 | `torch_rnn` | 89.306 | 89.110 | -0.197 | 0.688 | 0.001 | Learned recurrence is not needed in the low-pressure task. |
| 1 | `torch_lstm` | 37.881 | 92.078 | 54.197 | 0.813 | 0.001 | Learned recurrent policy state decodes self-state and improves control. |
| 2 | `torch_gru` | 28.257 | 79.096 | 50.839 | 0.637 | 0.002 | Learned recurrent policy state decodes self-state and improves control. |
| 3 | `torch_lstm` | 81.930 | 132.050 | 50.120 | 0.578 | 0.008 | Learned recurrent policy state decodes self-state and improves control. |
| 4 | `torch_lstm` | 6.081 | 95.502 | 89.421 | 0.760 | 0.015 | Learned recurrent policy state decodes self-state under high pressure. |
| 5 | `torch_gru` | -37.410 | 70.018 | 107.428 | 0.658 | 0.014 | Learned recurrent policy state decodes self-state under high pressure. |
| 6 | `torch_gru` | -30.317 | 93.633 | 123.950 | 0.594 | 0.009 | Learned recurrent policy state decodes self-state under high pressure. |

## Learned Bottleneck Snapshot

| Scenario | Learned structure | Boundary signature | Current result |
|---|---|---|---|
| `self_reuse` | `shared_bottleneck` | `agent_bounded_shared` | Learned reward 69.888 vs local 66.888. |
| `world_reuse` | `shared_bottleneck` | `external_shared` | Same learned structure, but boundary says world-state. |
| `independent_hidden` | `local_hidden` | `no_shared_agent_boundary` | Local-hidden learned selection reward 66.606 vs shared 23.496. |
| `irrelevant_control` | `no_hidden_needed` | `no_shared_agent_boundary` | No-hidden learned selection reward 94.000. |

## Sequence Latent Transfer Snapshot

| Scenario | Learned transfer | Boundary signature | Current result |
|---|---|---|---|
| `self_shared_sequence` | `shared_sequence_state` | `agent_bounded_sequence` | Learned reward 68.700 vs no-transfer memory 40.000. |
| `world_shared_sequence` | `shared_sequence_state` | `external_sequence` | Same transfer value, but boundary says world-state. |
| `independent_sequence` | `local_context_state` | `no_shared_agent_boundary` | Local learned reward 64.668 vs shared sequence 18.888. |
| `irrelevant_sequence` | `no_hidden_needed` | `no_shared_agent_boundary` | No-hidden learned reward 94.000. |

## Heterogeneous Attractor Precursor Snapshot

| Scenario | Expected convergence | Boundary signature | Current result |
|---|---|---|---|
| `self_shared_stream` | `agent_bounded_candidate` | `agent_bounded_stream` | 5/5 learner families converge; best architecture reward 34404.000 vs local probe 32904.000. |
| `world_shared_stream` | `external_candidate` | `external_stream` | 5/5 learner families converge, but boundary says world-state. |
| `independent_stream` | `no_shared_agent_boundary` | `no_shared_agent_boundary` | 5/5 reject shared self/world boundary; local probe reward 32282.000 vs best architecture 20000.000. |
| `irrelevant_stream` | `no_hidden_needed` | `no_shared_agent_boundary` | 5/5 collapse to no hidden state; marginal and best architecture both score 47000.000. |

## Cross-Environment Attractor Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 4/4 environments support; mean learned reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 4/4 environments support, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 4/4 environments select local hidden structure; learned and local-probe rewards both 41293.250. |
| `irrelevant_control` | `no_hidden_needed` | 4/4 environments select no hidden state; learned and marginal rewards both 60250.000. |

## Factorial Attractor Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 5/5 learners converge in all 4 environments; mean best learner reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 5/5 learners converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 5/5 learners reject shared self/world boundary in all 4 environments; local probe beats best learner 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 5/5 learners collapse to no hidden state in all 4 environments; mean best learner and marginal rewards both 60250.000. |

## Raw History Learning Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 5/5 raw-history learners converge in all 4 environments; mean best learner reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 5/5 raw-history learners converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 5/5 raw-history learners reject shared self/world boundary in all 4 environments; local probe beats best learner 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 5/5 raw-history learners collapse to no hidden state in all 4 environments; mean best learner and marginal rewards both 60250.000. |

## Delayed Return Policy Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 5/5 delayed-return policies converge in all 4 environments; mean best policy reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 5/5 delayed-return policies converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 5/5 delayed-return policies reject shared self/world boundary in all 4 environments; local probe beats best policy 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 5/5 delayed-return policies collapse to no hidden state in all 4 environments; mean best policy and marginal rewards both 60250.000. |

## Evolved Recurrent Policy Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 3/3 recurrent architectures converge in all 4 environments; mean best architecture reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 3/3 recurrent architectures converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 3/3 recurrent architectures reject shared self/world boundary in all 4 environments; local probe beats best architecture 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 3/3 recurrent architectures collapse to no hidden state in all 4 environments; mean best architecture and marginal rewards both 60250.000. |

## Gradient Recurrent Policy Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 3/3 gradient-trained recurrent architectures converge in all 4 environments; mean best architecture reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 3/3 gradient-trained recurrent architectures converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 3/3 gradient-trained recurrent architectures reject shared self/world boundary in all 4 environments; local probe beats best architecture 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 3/3 gradient-trained recurrent architectures collapse to no hidden state in all 4 environments; mean best architecture and marginal rewards both 60250.000. |

## Model-Based Planning Snapshot

| Scenario | Expected signature | Current result |
|---|---|---|
| `agent_shared` | `agent_bounded_candidate` | 3/3 model-based planners converge in all 4 environments; mean best planner reward 42568.500 vs local probe 41068.500. |
| `world_shared` | `external_candidate` | 3/3 model-based planners converge in all 4 environments, but boundary says world-state. |
| `independent_hidden` | `no_shared_agent_boundary` | 3/3 model-based planners reject shared self/world boundary in all 4 environments; local probe beats best planner 41293.250 vs 21875.000. |
| `irrelevant_control` | `no_hidden_needed` | 3/3 model-based planners collapse to no hidden state in all 4 environments; mean best planner and marginal rewards both 60250.000. |

## Latent Causal Ablation Snapshot

| Scenario | Expected causal signature | Current result |
|---|---|---|
| `agent_shared` | `agent_latent_causal` | 3/3 planners show agent-bounded causal loss in all 4 environments; mean reward falls 42568.500 to 21875.000. |
| `world_shared` | `external_latent_causal` | 3/3 planners show external causal loss in all 4 environments; mean reward falls 42035.250 to 21875.000. |
| `independent_hidden` | `no_shared_latent_causal` | 3/3 planners show no shared latent causal loss in all 4 environments; mean reward loss is 0.000. |
| `irrelevant_control` | `no_hidden_needed` | 3/3 planners show no hidden-state dependence in all 4 environments; mean reward loss is 0.000. |

## Counterfactual Latent Editing Snapshot

| Scenario | Expected counterfactual signature | Current result |
|---|---|---|
| `agent_shared` | `agent_counterfactual_edit` | 3/3 planners show agent-bounded edit effects in all 4 environments; forced-good risky rate 1.000 vs forced-bad 0.000. |
| `world_shared` | `external_counterfactual_edit` | 3/3 planners show external edit effects in all 4 environments; forced-good risky rate 1.000 vs forced-bad 0.000. |
| `independent_hidden` | `no_shared_counterfactual` | 3/3 planners show no shared edit effect in all 4 environments; mean edit swing is 0.000. |
| `irrelevant_control` | `no_hidden_needed` | 3/3 planners show no hidden-state edit dependence in all 4 environments; mean edit swing is 0.000. |

## Reproducibility Artifacts

| Script | Main artifact |
|---|---|
| `experiments/self_world_attribution.py` | `artifacts/self_world_attribution_summary.csv` |
| `experiments/representation_search.py` | `artifacts/representation_search_category_summary.csv` |
| `experiments/predictive_state_emergence.py` | `artifacts/predictive_state_probe_summary.csv` |
| `experiments/hidden_viability_survival.py` | `artifacts/hidden_viability_summary.csv` |
| `experiments/interruption_coherence.py` | `artifacts/interruption_coherence_summary.csv` |
| `experiments/online_predictive_learning.py` | `artifacts/online_predictive_learning_summary.csv` |
| `experiments/selfhood_boundary_probe.py` | `artifacts/selfhood_boundary_summary.csv` |
| `experiments/architecture_convergence.py` | `artifacts/architecture_convergence_verdict.csv` |
| `experiments/active_self_information.py` | `artifacts/active_self_information_bandit_summary.csv` |
| `experiments/counterfactual_option_preservation.py` | `artifacts/counterfactual_option_preservation_verdict.csv` |
| `experiments/first_person_frame_integration.py` | `artifacts/first_person_frame_verdict.csv` |
| `experiments/goal_formation_under_capability.py` | `artifacts/goal_formation_under_capability_verdict.csv` |
| `experiments/competing_subsystems_arbitration.py` | `artifacts/competing_subsystems_arbitration_verdict.csv` |
| `experiments/cross_context_self_reuse.py` | `artifacts/cross_context_self_reuse_verdict.csv` |
| `experiments/reuse_pressure_sweep.py` | `artifacts/reuse_pressure_sweep_verdict.csv` |
| `experiments/horizon_pressure_sweep.py` | `artifacts/horizon_pressure_sweep_verdict.csv` |
| `experiments/partial_observability_sweep.py` | `artifacts/partial_observability_sweep_verdict.csv` |
| `experiments/learned_observation_filter.py` | `artifacts/learned_observation_filter_verdict.csv` |
| `experiments/recurrent_observation_filter.py` | `artifacts/recurrent_observation_filter_verdict.csv` |
| `experiments/unseeded_recurrent_filter.py` | `artifacts/unseeded_recurrent_filter_verdict.csv` |
| `experiments/mixed_sensor_recurrent_filter.py` | `artifacts/mixed_sensor_recurrent_filter_verdict.csv` |
| `experiments/learned_sensor_subspace_filter.py` | `artifacts/learned_sensor_subspace_filter_verdict.csv` |
| `experiments/active_boundary_discovery.py` | `artifacts/active_boundary_discovery_verdict.csv` |
| `experiments/action_effect_boundary_probe.py` | `artifacts/action_effect_boundary_probe_verdict.csv` |
| `experiments/persistent_action_boundary_probe.py` | `artifacts/persistent_action_boundary_probe_verdict.csv` |
| `experiments/return_selected_boundary_probe.py` | `artifacts/return_selected_boundary_probe_verdict.csv` |
| `experiments/end_to_end_boundary_probe.py` | `artifacts/end_to_end_boundary_probe_verdict.csv` |
| `experiments/architecture_boundary_stress.py` | `artifacts/architecture_boundary_stress_verdict.csv` |
| `experiments/architecture_horizon_pressure_sweep.py` | `artifacts/architecture_horizon_pressure_verdict.csv` |
| `experiments/architecture_capacity_probe.py` | `artifacts/architecture_capacity_probe_verdict.csv` |
| `experiments/architecture_soft_return_optimizer.py` | `artifacts/architecture_soft_return_optimizer_verdict.csv` |
| `experiments/architecture_hard_return_audit.py` | `artifacts/architecture_hard_return_audit_verdict.csv` |
| `experiments/architecture_hard_return_horizon_sweep.py` | `artifacts/architecture_hard_return_horizon_verdict.csv` |
| `experiments/architecture_online_return_learner.py` | `artifacts/architecture_online_return_learner_verdict.csv` |
| `experiments/architecture_policy_gradient_learner.py` | `artifacts/architecture_policy_gradient_learner_verdict.csv` |
| `experiments/architecture_policy_gradient_seed_sweep.py` | `artifacts/architecture_policy_gradient_seed_sweep_verdict.csv` |
| `experiments/architecture_policy_gradient_budget_sweep.py` | `artifacts/architecture_policy_gradient_budget_sweep_verdict.csv` |
| `experiments/architecture_torch_actor_critic.py` | `artifacts/architecture_torch_actor_critic_verdict.csv` |
| `experiments/ssrm_3d_embodied_world.py` | `artifacts/ssrm_3d_verdict.csv` |
| `experiments/ssrm_3d_recurrent_observer.py` | `artifacts/ssrm_3d_recurrent_observer_verdict.csv` |
| `experiments/ssrm_3d_learned_controller.py` | `artifacts/ssrm_3d_learned_controller_verdict.csv` |
| `experiments/ssrm_3d_tool_making.py` | `artifacts/ssrm_3d_tool_making_verdict.csv` |
| `experiments/ssrm_3d_social_pressure.py` | `artifacts/ssrm_3d_social_pressure_verdict.csv` |
| `experiments/ssrm_3d_social_ecology.py` | `artifacts/ssrm_3d_social_ecology_verdict.csv` |
| `experiments/ssrm_3d_agent_continuity.py` | `artifacts/ssrm_3d_agent_continuity_verdict.csv` |
| `experiments/ssrm_3d_learned_integration_controller.py` | `artifacts/ssrm_3d_learned_integration_verdict.csv` |
| `experiments/ssrm_3d_no_leak_integration_sweep.py` | `artifacts/ssrm_3d_no_leak_integration_verdict.csv` |
| `experiments/ssrm_3d_structured_perception.py` | `artifacts/ssrm_3d_structured_perception_verdict.csv` |
| `experiments/ssrm_3d_day_night_sleep.py` | `artifacts/ssrm_3d_day_night_sleep_verdict.csv` |
| `experiments/ssrm_3d_illness_sanitation.py` | `artifacts/ssrm_3d_illness_sanitation_verdict.csv` |
| `experiments/ssrm_3d_weather_exposure.py` | `artifacts/ssrm_3d_weather_exposure_verdict.csv` |
| `experiments/ssrm_3d_tool_shelter_degradation.py` | `artifacts/ssrm_3d_tool_shelter_degradation_verdict.csv` |
| `experiments/ssrm_3d_social_trust_contracts.py` | `artifacts/ssrm_3d_social_trust_contracts_verdict.csv` |
| `experiments/ssrm_3d_predator_threat_agents.py` | `artifacts/ssrm_3d_predator_threat_agents_verdict.csv` |
| `experiments/ssrm_3d_resource_ecology.py` | `artifacts/ssrm_3d_resource_ecology_verdict.csv` |
| `experiments/ssrm_3d_injury_disability_adaptation.py` | `artifacts/ssrm_3d_injury_disability_adaptation_verdict.csv` |
| `experiments/ssrm_3d_development_skill_learning.py` | `artifacts/ssrm_3d_development_skill_learning_verdict.csv` |
| `experiments/ssrm_3d_dependent_care.py` | `artifacts/ssrm_3d_dependent_care_verdict.csv` |
| `experiments/ssrm_3d_irreversible_loss.py` | `artifacts/ssrm_3d_irreversible_loss_verdict.csv` |
| `experiments/ssrm_3d_affective_control.py` | `artifacts/ssrm_3d_affective_control_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_repair_critic_controller.py` | `artifacts/ssrm_3d_coupled_crisis_repair_critic_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_outcome_value_controller.py` | `artifacts/ssrm_3d_coupled_crisis_outcome_value_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_sequence_outcome_controller.py` | `artifacts/ssrm_3d_coupled_crisis_sequence_outcome_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_environment_bottleneck_controller.py` | `artifacts/ssrm_3d_coupled_crisis_environment_bottleneck_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_rollout_window_controller.py` | `artifacts/ssrm_3d_coupled_crisis_rollout_window_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_diagnostic_memory_controller.py` | `artifacts/ssrm_3d_coupled_crisis_diagnostic_memory_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_joint_arbitration_controller.py` | `artifacts/ssrm_3d_coupled_crisis_joint_arbitration_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_randomized_transfer_controller.py` | `artifacts/ssrm_3d_coupled_crisis_randomized_transfer_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_adaptive_allocator_controller.py` | `artifacts/ssrm_3d_coupled_crisis_adaptive_allocator_verdict.csv` |
| `experiments/ssrm_3d_coupled_crisis_policy_value_allocator_controller.py` | `artifacts/ssrm_3d_coupled_crisis_policy_value_allocator_verdict.csv` |
| `experiments/learned_bottleneck_discovery.py` | `artifacts/learned_bottleneck_discovery_verdict.csv` |
| `experiments/sequence_latent_transfer.py` | `artifacts/sequence_latent_transfer_verdict.csv` |
| `experiments/heterogeneous_attractor_precursor.py` | `artifacts/heterogeneous_attractor_precursor_verdict.csv` |
| `experiments/cross_environment_attractor.py` | `artifacts/cross_environment_attractor_scenario_verdict.csv` |
| `experiments/factorial_attractor_test.py` | `artifacts/factorial_attractor_scenario_verdict.csv` |
| `experiments/raw_history_learning.py` | `artifacts/raw_history_learning_scenario_verdict.csv` |
| `experiments/delayed_return_policy.py` | `artifacts/delayed_return_policy_scenario_verdict.csv` |
| `experiments/evolved_recurrent_policy.py` | `artifacts/evolved_recurrent_policy_scenario_verdict.csv` |
| `experiments/gradient_recurrent_policy.py` | `artifacts/gradient_recurrent_policy_scenario_verdict.csv` |
| `experiments/model_based_planning.py` | `artifacts/model_based_planning_scenario_verdict.csv` |
| `experiments/latent_causal_ablation.py` | `artifacts/latent_causal_ablation_scenario_verdict.csv` |
| `experiments/counterfactual_latent_editing.py` | `artifacts/counterfactual_latent_editing_scenario_verdict.csv` |

Run all canonical experiments with:

```bash
python3 scripts/run_experiments.py
```
