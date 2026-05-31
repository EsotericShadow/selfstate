# SSRM-3D Done-Enough Gates

## Purpose

SSRM-3D is not done because it has a 3D visualization or because a controller claims selfhood.

This track is done enough only when the embodied world passes four gates:

1. learned control;
2. tool-making or externalized cognition;
3. real social pressure;
4. targeted ablation.

The gates are designed to keep the project from mistaking named hidden variables, observer probes, scripted behavior, or pretty embodiment for evidence that selfhood is a useful control abstraction.

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

Partially passed by [report 62](62_ssrm_3d_learned_controller_report.md).

The SSRM-3D learned-controller precursor trains recurrent controllers without self labels. In stages 1-6, recurrent controllers beat frame-only controllers by 50.120 to 123.950 reward points and carry decodable self-state. Stage 0 remains a clean low-pressure control.

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

Open.

SSRM-3D currently has resources, hazards, shelter, commitments, and a simple competitor. It does not yet let agents construct external memory, route markers, alarms, sensors, or device-like policies.

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

Open, with only a weak precursor.

SSRM-3D stage 6 has a simple competitor. That is useful as a first social pressure, but it is not enough. There is no reputation, memory of prior interaction, communication, deception, shared tool use, or trust.

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

Gate 1 has a useful learned-control precursor.

Gates 2 and 3 remain open.

Gate 4 is partially supported, but the ablation suite is incomplete.

The strongest next experiment is tool-making or externalized cognition in SSRM-3D, because it creates the missing pressure needed for both social coordination and attention-buffer ablation to become meaningful.
