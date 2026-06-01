# SSRM-3D Done-Enough Gates

## Purpose

SSRM-3D is not done because it has a 3D visualization or because a controller claims selfhood.

This track is done enough only when the embodied world passes four gates:

1. learned control;
2. tool-making or externalized cognition;
3. real social pressure;
4. targeted ablation.

The gates are designed to keep the project from mistaking named hidden variables, observer probes, scripted behavior, or pretty embodiment for evidence that selfhood is a useful control abstraction.

## Clock And Rates

The simulator can count ticks, but the architecture should be specified as subsystem update rates.

Example framing:

```text
base_tick_hz = 60
physics_hz = 60
reflex_hz = 60
motor_control_hz = 30
perception_hz = 10
attention_hz = 10
self_state_hz = 5
goal_hz = 2
reasoning_hz = 0.5
memory_hz = 0.1
reflection = event_triggered
```

The implementation can convert rates to tick intervals, but the cognitive claim is multi-rate control: threats and movement need fast loops, perception and attention can be medium rate, self-state and goal arbitration can be slower, and language reasoning or memory consolidation should be much slower. A single global reasoning tick would blur the control boundaries the gates are supposed to test.

## Gate 1: Learned Control

Question:

Can a controller trained in SSRM-3D use its own learned policy state to improve action under embodied pressure?

Pass condition:

- recurrent or model-based controllers are trained without self labels;
- policy state carries decodable self-state only where pressure requires it;
- learned recurrence is not useful in the low-pressure spatial stage;
- learned recurrence improves reward, survival, commitment completion, or recovery under hidden energy, body drift, delayed options, commitments, arbitration, and social pressure;
- self-state is probed in policy state, not only in an external observer.

Current status:

Partially passed by [report 62](62_ssrm_3d_learned_controller_report.md), extended by [report 69](69_ssrm_3d_learned_integration_controller_report.md), and constrained by the no-leak sweep in [report 73](73_ssrm_3d_no_leak_integration_sweep_report.md).

The SSRM-3D learned-controller precursor trains recurrent controllers without self labels. In stages 1-6, recurrent controllers beat frame-only controllers by 50.120 to 123.950 reward points and carry decodable self-state. Stage 0 remains a clean low-pressure control.

The learned-integration precursor trains a recurrent controller from reward-derived packet traces. It rejects extra state in visible control and carries early local and integrated pressure evidence in the seeded canonical run, but scenario identity and feature-group structure are supplied. The no-leak sweep removes scenario identity and randomizes pressure combinations; it preserves some bridges but rejects stable integration because the tool margin is fragile and integrated social pressure is not ablation-stable.

[Report 75](75_ssrm_3d_structured_perception_report.md) adds the first persistent-pressure perception layer. It does not satisfy learned control by itself, but it makes future learned-control gates less omniscient: route memory, tool alarms, multimodal night navigation, and sensor-damage adaptation now have targeted vision/audio ablations.

[Report 76](76_ssrm_3d_day_night_sleep_report.md) adds the second persistent-pressure layer. It does not satisfy learned control by itself, but it makes future learned-control gates more temporal: fatigue, night timing, shelter state, alarms, social watch, and continuity now have targeted sleep/rest ablations.

[Report 77](77_ssrm_3d_illness_sanitation_report.md) adds the third persistent-pressure layer. It does not satisfy learned control by itself, but it makes future learned-control gates more internally hidden: hunger/thirst, illness attribution, contamination, quarantine/care, immunity, and continuity now have targeted health-state ablations.

Remaining weakness:

Direct counterfactual self-state edits have weak action effects. This means the current evidence supports learned policy-state self tracking for control, but not robust causal policy editing.

## Gate 2: Tool-Making Or Externalized Cognition

Question:

Does the agent discover that external structures can reduce confusion, preserve options, or improve commitments?

Pass condition:

- the world gives the agent access to build or place simple external structures;
- useful structures include markers, maps, alarms, routes, sensors, caches, beacons, or simple device logic;
- the agent is not instructed to "make software" or "build tools";
- tools become useful because they reduce uncertainty, improve navigation, protect future options, support social coordination, or preserve commitments;
- removing tool-building access produces specific failures only in stages where externalization should matter.

Current status:

Partially passed by [report 65](65_ssrm_3d_tool_making_report.md), given a learned-controller bridge by [report 69](69_ssrm_3d_learned_integration_controller_report.md), and constrained by [report 73](73_ssrm_3d_no_leak_integration_sweep_report.md).

The SSRM-3D tool-making precursor gives the world marker, beacon, alarm, and cache affordances. Return selection rejects tools in the visible-resource control, selects tools under hidden-route, degraded-sensor, and interruption-recovery pressure, and loses most of the gain when tool access is ablated.

The learned-integration precursor adds that early tool-route evidence can be carried by recurrent policy state; frame-only control falls behind and tool-channel ablation removes the learned advantage. The no-leak sweep keeps raw tool support across seeds but the weakest margins are too close to the widened threshold, so the learned tool bridge remains provisional.

The structured-perception precursor adds a more concrete tool reason: visual markers and audio alarms matter when FOV, darkness, occlusion, and sound direction create partial observability. This is still candidate-policy evidence, not learned tool invention.

The sleep-rest precursor adds a second tool reason: alarms matter when the agent is vulnerable while resting near danger. This remains a supplied affordance, but the ablation is specific to the guarded-sleep regime.

The illness/sanitation precursor adds a third tool reason: clean-water tools matter when hydration and pathogen exposure conflict. This remains a supplied affordance, but the ablation is specific to contaminated-resource regimes.

The weather/exposure precursor adds a fourth tool reason: fire/light tools matter when shelter alone does not preserve capability under cold, rain, wind, and storm darkness. This remains a supplied affordance, but the ablation is specific to weather-pressure regimes.

The tool/shelter degradation precursor adds a fifth tool reason: markers, alarms, caches, shelters, spare parts, inspection, and repair matter when persistent infrastructure decays. This remains a supplied affordance, but the ablation is specific to maintenance-pressure regimes.

The resource-ecology precursor adds a sixth tool reason: caches matter when regrowth, depletion, spoilage, and delayed scarcity make storage and rotation useful. This remains a supplied affordance, but the ablation is specific to resource-pressure regimes.

Remaining weakness:

The successful policies are return-selected from candidate affordance policies, not learned end-to-end by the SSRM-3D controller. The cache-only affordance remains a limit control rather than a success. This means Gate 2 has a useful externalized-cognition precursor, but not a full pass.

Failure interpretation:

- If tools help everywhere, the environment is biased.
- If tools help nowhere, tool pressure is weak or tools are not connected to real uncertainty.
- If agents build tools only because the policy was scripted to do so, this gate has not passed.

## Gate 3: Real Social Pressure

Question:

Does selfhood become socially relevant when other agents can remember, help, block, exploit, trust, deceive, or coordinate with the agent?

Pass condition:

- other agents are not just moving obstacles;
- other agents have persistent memory, resource needs, and policies;
- the environment includes cooperation, competition, reputation, shared tools, communication, deception, or resource conflict;
- the tested agent must model itself as something that can be trusted, remembered, helped, blocked, or exploited;
- self-state or identity continuity improves social control only when social pressure is present.

Current status:

Partially passed by [report 66](66_ssrm_3d_social_pressure_report.md), extended by [report 67](67_ssrm_3d_social_ecology_report.md), extended again by [report 80](80_ssrm_3d_social_trust_contracts_report.md), and given a learned-controller bridge by [report 69](69_ssrm_3d_learned_integration_controller_report.md).

The SSRM-3D social-pressure precursor gives other agents persistent identities, resource needs, trust toward the tested agent, and helper, trader, opportunist, and deceiver policies. Return selection rejects social machinery in the visible-resource control, selects social identity policies under cooperative repair, opportunist vulnerability, deceptive-route, and shared-tool pressure, and loses the advantage when identity memory, social self-state, or shared-tool access is ablated.

The SSRM-3D social-ecology precursor makes communication costly. Return selection rejects communication in the visible solo control, selects warning signals when route information beats rediscovery, selects names when persistent social history matters, selects gossip when absent-agent information improves future choices, and selects check-ins when low-cost contact maintains repair, trust, shared-tool access, and future options.

The SSRM-3D social trust/contracts precursor makes promises costly. Return selection rejects contract machinery in the visible no-contract control, selects borrowed-tool return, hazard warning, resource sharing, and shelter repair duty only when they preserve future access, and loses the advantage under matching commitment, identity, communication, trust, ownership, repair-debt, or continuity ablations.

The SSRM-3D predator/threat precursor adds hostile tracking pressure. It is not a social-gate pass by itself, but it gives social warning and group defense a job: return selection keeps those channels only when trackers exploit isolation, weakness, alarms, shelter, or restore-time forgetting.

The SSRM-3D resource-ecology precursor adds shared-territory pressure. It is not a social-gate pass by itself, but it gives sharing contracts and territory memory a job: return selection keeps those channels only when other agents can change future resource access.

The learned-integration precursor adds that early helper/deceiver identity evidence can be carried by recurrent policy state; social-channel ablation removes the learned social-repair advantage.

Remaining weakness:

The successful policies are return-selected from candidate social-control, communication, contract, and group-defense policies, not learned end-to-end by the SSRM-3D controller. The social agents use simple role policies rather than open-ended communication, learned deception, or long multi-episode reputation. This means Gate 3 has useful social-pressure, costly-communication, contract, and threat-linked group-defense precursors, but not a full pass.

Failure interpretation:

- If social self-state helps without social memory or interaction, the test is biased.
- If world-only tracking solves all social stages, selfhood may not be socially necessary in this regime.
- If social behavior is scripted rather than learned or pressure-selected, the gate has not passed.

## Gate 4: Targeted Ablation

Question:

Do removals produce specific failures that match the theory?

Required ablations:

- remove self-state;
- damage the learned self-subspace;
- remove attention mixing;
- remove continuity memory;
- remove the LLM reasoning stream;
- remove tool-building access once tools exist.

Pass condition:

- removing self-state hurts only under embodied pressure, not in simple low-pressure tasks;
- damaging learned self-subspace hurts policy-state prediction or control where self-state is needed;
- removing attention mixing hurts multi-pressure arbitration, not simple resource collection;
- removing continuity memory hurts commitments, interruption recovery, identity tracking, reputation, or long-term obligations;
- removing the LLM reasoning stream hurts slow abstract planning but not reflex survival;
- removing tool-building access hurts uncertainty reduction, route memory, alarms, or option preservation only where external tools matter.

Current status:

Partially passed but incomplete.

Existing evidence includes self-state ablation in SSRM-3D, learned observer self-subspace ablation, and weak learned-controller self-edit probes. The ablation suite is not complete because attention mixing, continuity memory, LLM stream, and tool-building access are not yet independently removed in the embodied learned-control setting. The modular LLM architecture report defines the expected no-LLM, direct-motor LLM, full-world LLM, and corrupted-packet ablation patterns.

[Report 68](68_ssrm_3d_agent_continuity_report.md) adds a continuity-record precursor: model-only copies, incompatible memory transplants, social-memory resets, commitment resets, tool resets, and ambiguous forks fail in specific restore/fork regimes. That strengthens the continuity-memory side of Gate 4, but it is still not the learned-controller ablation suite required for a full pass.

[Report 69](69_ssrm_3d_learned_integration_controller_report.md) adds a learned packet-level ablation bridge: continuity-channel ablation damages the local restore row, attention-channel ablation damages integrated gate pressure, and tool/social ablations remain pressure-specific. It also records a failure: continuity-channel ablation does not damage the integrated gate-pressure row. [Report 73](73_ssrm_3d_no_leak_integration_sweep_report.md) then removes scenario identity and randomizes pressure combinations; the local social, local continuity, integrated tool, and integrated continuity bridges survive, but `single_tool` and `integrated_social` fail the stronger verdict. These reports still do not replace the full embodied learned-controller ablation suite.

[Report 81](81_ssrm_3d_predator_threat_agents_report.md) adds a pressure-layer ablation check for threat perception, self-vulnerability, sound/scent memory, stealth, shelter, alarms, social warning, and continuity. It strengthens the targeted-ablation pattern for designed policies, but it does not replace learned-controller self-state, attention, LLM-stream, or tool-building ablations.

[Report 82](82_ssrm_3d_resource_ecology_report.md) adds a pressure-layer ablation check for resource memory, regeneration, spoilage, migration, restraint, cache management, sharing contracts, territory ownership, and continuity. It strengthens the targeted-ablation pattern for designed policies, but it does not replace learned-controller discovery of sustainable resource use.

[Report 83](83_ssrm_3d_injury_disability_adaptation_report.md) adds a pressure-layer ablation check for capability self-state, motor adaptation, sensor compensation, infection management, repair access, help-seeking, compensation tools, route adaptation, and continuity. It strengthens the targeted-ablation pattern for designed policies, but it does not replace learned-controller discovery of disability adaptation or full embodied self-state ablations.

[Report 84](84_ssrm_3d_development_skill_learning_report.md) adds a pressure-layer ablation check for skill memory, practice planning, capability self-state, fatigue management, injury adaptation, transfer modeling, teaching help, training tools, goal feasibility, and continuity. It strengthens the targeted-ablation pattern for designed policies, but it does not replace learned-controller discovery of curriculum, transfer, or competence self-modeling.

[Report 85](85_ssrm_3d_dependent_care_report.md) adds a pressure-layer ablation check for dependent state, identity memory, protection planning, resource sharing, repair care, teaching support, shelter coordination, promise commitment, social trust, priority arbitration, and continuity. It strengthens the targeted-ablation pattern for designed policies, but it does not replace learned-controller discovery of caregiving, sacrifice, or persistent social obligations.

[Report 86](86_ssrm_3d_irreversible_loss_report.md) adds a pressure-layer ablation check for loss memory, value-at-risk estimation, replacement modeling, caution control, tool/shelter/relationship preservation, memory backup, loss response, and continuity. It strengthens the targeted-ablation pattern for designed policies under permanent option-space loss, but it does not replace learned-controller discovery of loss-sensitive planning or affective control state.

Failure interpretation:

- If removing self-state hurts everywhere, the environment is biased toward self variables.
- If removing self-state hurts nowhere, the selfhood theory is weak.
- If every ablation causes generic collapse, the architecture is not modular enough for causal interpretation.
- If no ablation causes specific failure, the apparent self-state may be epiphenomenal.

## Optional Follow-On: Attention Buffer Capacity Sweep

The dimensionality idea is worth preserving, but it should be framed narrowly.

It is not a 12-dimensional external world claim. It is a hypothesis about limited internal attention bandwidth.

Candidate experiment:

Run SSRM-3D pressure stages with active attention buffers of different capacities, such as 2, 4, 8, 12, 16, and 24 slots.

The slots are live priority channels, not literal spatial dimensions. Candidate channels include:

- threat;
- energy;
- damage;
- current goal;
- commitment urgency;
- novelty;
- prediction error;
- social signal;
- tool state;
- memory recall;
- spatial navigation;
- uncertainty.

Expected pressure-dependent result:

- small buffers fail under multi-pressure conflict;
- mid-sized buffers preserve survival, commitments, recovery, and self-state tracking;
- very large buffers may help, plateau, or add noise;
- low-pressure stages should not need large buffers.

This belongs after the basic four gates are in place, or as a supporting gate-4 ablation study for attention mixing. It should not be treated as consciousness evidence, and 12 slots should not be treated as special unless the sweep actually shows a repeatable optimum.

## Current Summary

Gate 1 has useful learned-control precursors.

Gate 2 has a partial externalized-cognition precursor and a learned tool-memory bridge.

Gate 3 has partial social-pressure, costly-communication, and social-contract precursors and a learned social-memory bridge.

Gate 4 has continuity-record and learned continuity/attention precursors, but the ablation suite is incomplete.

The strongest next experiment is moving learned tool, social, and continuity integration into the full SSRM-3D controller with actual construction, repeated interaction, restore/fork events, and richer societies.

The next stronger social ecology should move costly communication into learned controllers. Signals, names, promises, gossip, play, humour, and bonding should not be directly rewarded; they should survive only when they preserve future options, reduce uncertainty, protect commitments, or improve cooperation under social memory.
