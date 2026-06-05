# SSRM-3D Settlement/Civilization Pressure Report

## Question

The first physics benchmark produced a visible limitation: one agent could look like it was looping between water and shelter. This experiment asks whether the SSRM-3D track can represent a richer inhabited world where the relevant pressure is not just body survival, but shared settlement survival.

The narrow question is:

> When does a persistent self-like control layer become useful because an agent is embedded in a group that builds, remembers, repairs, teaches, regulates conflict, and prepares for future shocks?

## What changed

This is a separate settlement layer, not a rewrite of the C++ physics kernel. It adds:

- eight named agents with persistent roles;
- shared projects: shelter, water purifier, clinic, farm, workshop, watchtower, school, and commons;
- shared resources: food, water, materials, medicine, and tools;
- social state: trust network, norms, conflict, morale, migration pressure;
- emotion-like control state: fear, stress, anger, guilt, attachment, curiosity;
- civilization state: knowledge, map coverage, completed infrastructure, and future-capital readiness;
- late-horizon frontier shocks that punish failure to prepare.

## What this does not claim

This is not open-ended civilization emergence. It is not subjective emotion. It is not subjective consciousness. It is not closed-loop deep reinforcement learning.

It is a designed precursor showing that a richer settlement state can create specific ablation pressure beyond a single-agent water/shelter loop.

## Canonical command

```bash
python3 experiments/ssrm_3d_civilization_pressure.py --eval-episodes 48 --ticks 96 --seed 20260706 --trace-episode 3
```

## Conditions

- `integrated_settlement_self`
- `reactive_individuals`
- `no_social_memory`
- `no_building_memory`
- `no_role_memory`
- `no_affective_control`
- `no_norms`
- `no_future_planning`

## Canonical result

The integrated settlement policy reaches a mean civilization score of `0.812`.

Targeted ablations reduce that score:

- reactive individuals: `0.502`, loss `0.309`;
- no norms: `0.557`, loss `0.254`;
- no role memory: `0.670`, loss `0.142`;
- no future planning: `0.675`, loss `0.136`;
- no building memory: `0.741`, loss `0.071`;
- no social memory: `0.738`, loss `0.074`;
- no affective control: `0.746`, loss `0.065`.

The verdict is a designed precursor pass:

```text
supports_civilization_pressure_precursor = true
supports_closed_loop_rl = false
```

## Interpretation

The result is stronger than a single-agent survival loop because the score depends on population-level state:

- social norms reduce conflict and protect shared resources;
- role memory prevents everyone from chasing the same short-term need;
- building memory turns materials and tools into infrastructure;
- social memory preserves trust and cooperation;
- affective-control state changes care, guard, rest, and council behavior;
- future planning matters after late frontier shocks.

This does not prove that civilization emerges naturally. The environment and policies are still designed. The useful result is the expanded falsification surface: we can now remove social memory, roles, norms, building memory, affect, or future planning and watch the settlement fail in different ways.

## Artifacts

- [script](../experiments/ssrm_3d_civilization_pressure.py)
- [module package](../experiments/ssrm_civilization)
- [evaluation CSV](../artifacts/ssrm_3d_civilization_pressure_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_civilization_pressure_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_civilization_pressure_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_civilization_pressure_trace.json)
- [results JSON](../artifacts/ssrm_3d_civilization_pressure_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_civilization_pressure_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_civilization_pressure_results.js)
- [visualization](../visualizations/ssrm_3d_civilization_pressure.html)

## Next gate

The next serious step is to move this settlement layer into closed-loop learned control:

- agents act from observations instead of designed policy rules;
- interventions alter live state, not only the replay log;
- the trained recurrent policy is evaluated across held-out settlement layouts;
- ablations are applied during acting, not only during designed rollout.
