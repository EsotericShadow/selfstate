# SSRM-3D Embodied World Report

## Purpose

This experiment starts the SSRM-3D track: a persistent 3D embodied-world precursor for the selfhood research program.

It is not a consciousness experiment. It asks whether the same pressures tested in the toy stack still favor reusable agent-bounded latent state when the agent must move through a continuous world with terrain, resources, hazards, shelter, weather, day/night change, commitments, conflict, and a simple social competitor.

## Architecture

The LLM is not the brain in this design.

The simulated organism uses layered control:

| Layer | Role |
|---|---|
| Reflex | Fast hazard and viability overrides. |
| Perception | 10 Hz object and noisy self-sensor packet. |
| Self-state | Persistent estimates of energy, integrity, mobility, sensor capability, uncertainty, and commitments. |
| Attention | Continuous priority weights from threat, viability, prediction error, novelty, goals, commitments, and social pressure. |
| Arbiter | Chooses between survival, resource, commitment, curiosity, and social modes. |
| LLM module | Slow recommendation from a compressed state packet only. |
| Action | Motor target and speed execution. |

The LLM-like module can recommend, but the arbiter still decides and the motor layer executes. It is a language-cortex module, not the organism.

## Design

The experiment compares four agents:

| Agent | Description |
|---|---|
| `reactive_no_self` | Uses immediate visible cues and reflexes, with no persistent self-state workspace. |
| `world_model_only` | Tracks visible world structure but assumes fixed internal capability. |
| `layered_self_state` | Uses persistent self-state estimates, attention, arbitration, and a slow language module. |
| `layered_self_state_ablation` | Keeps the layered shell but removes the reusable self-state/commitment latent. |

Pressure stages:

| Stage | Pressure |
|---:|---|
| 0 | Position, orientation, resource collection. |
| 1 | Hidden energy state and resource management. |
| 2 | Actuator degradation, damage, and capability drift. |
| 3 | Delayed rewards and future option preservation. |
| 4 | Persistent goals, interruption, and recovery. |
| 5 | Survival, curiosity, and commitments compete. |
| 6 | Social prediction under cooperative and competitive dynamics. |

Measurements include survival, reward, resources, prediction error, attention entropy, latent decodability, latent reuse, ablation loss, counterfactual edit swing, recovery after interruption, and LLM recommendation follow rate.

## Command

```bash
python3 experiments/ssrm_3d_embodied_world.py --episodes 48 --ticks 540 --seed 20260607 --stage-min 0 --stage-max 6 --world-size 80 --perception-hz 10 --goal-hz 2 --reasoning-hz 0.5 --trace-stage 6 --trace-episode 0
```

## Current Result

| Stage | Best agent | Layered reward | Best nonself reward | Ablation loss | Verdict |
|---:|---|---:|---:|---:|---|
| 0 | `reactive_no_self` | 91.580 | 92.291 | -0.482 | No self required in low-pressure spatial task. |
| 1 | `layered_self_state` | 91.767 | 87.317 | 5.135 | Agent latent becomes decodable before a large performance gap. |
| 2 | `reactive_no_self` | 79.238 | 86.581 | 3.577 | Body-drift latent beats world-only, but reactive remains competitive. |
| 3 | `reactive_no_self` | 143.792 | 155.503 | 4.952 | Delayed-option latent beats world-only, but reactive remains competitive. |
| 4 | `layered_self_state` | 175.942 | 62.405 | 119.413 | Agent-bounded latent supported. |
| 5 | `layered_self_state` | 102.773 | 46.148 | 99.521 | Agent-bounded latent supported. |
| 6 | `layered_self_state` | 80.874 | 31.300 | 76.777 | Agent-bounded latent supported. |

Latent reuse grows with pressure in the layered agent, from `1.000` in hidden-energy pressure to `5.146` in the multiagent stage. Counterfactual energy edits change the arbiter's selected mode in most sampled states from stage 1 onward.

## Visualization

Open the visualization through a local server:

```bash
python3 -m http.server 8765
```

Then open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d.html
```

The visualization replays `artifacts/ssrm_3d_trajectory.json`, showing terrain, resources, hazards, shelter, competitor motion, the agent path, energy/integrity/mobility estimates, attention weights, and the slow language-module recommendation.

## Interpretation

The result is a useful embodied precursor, not a proof.

The strongest positive evidence appears only after commitments and subsystem conflict enter. In stages 4 to 6, the reusable self-state workspace becomes both performance-relevant and causally important: removing it sharply reduces reward.

The early stages are intentionally mixed:

- stage 0 supports the claim that self-state is not universally necessary;
- stage 1 shows decodability and mild ablation value before a large performance gap;
- stages 2 and 3 show the self-state latent beating world-only, while reactive control remains competitive.

That mixed result is important. It prevents the claim from collapsing into "hidden state always equals self." Embodiment pressure becomes self-like only when hidden agent-state is reused across viability, movement capability, commitments, attention, arbitration, and future options.

## Limits

This is still toy-scale:

- no learned deep policy;
- hand-built world dynamics;
- simple continuous movement, not full physics;
- no external LLM call;
- the language module is a deterministic stand-in for a slow reasoner;
- latent metrics are computed from known simulator state;
- social dynamics are minimal.

Report 61 takes the next representation step by training recurrent observers on embodied traces. Report 62 takes the next policy-state step by training learned controllers. Report 64 makes the LLM-as-module boundary explicit and turns the language stream into a future ablation target. Report 65 starts the tool-making/externalized-cognition gate. The stronger remaining version is online-return or model-based control with robust causal policy-state edits and learned tool discovery.

## Artifacts

- [experiment script](../experiments/ssrm_3d_embodied_world.py)
- [visualization](../visualizations/ssrm_3d.html)
- [modular LLM architecture visualization](../visualizations/modular_llm_architecture.html)
- [summary CSV](../artifacts/ssrm_3d_summary.csv)
- [episode metrics CSV](../artifacts/ssrm_3d_episode_metrics.csv)
- [verdict CSV](../artifacts/ssrm_3d_verdict.csv)
- [trajectory JSON](../artifacts/ssrm_3d_trajectory.json)
- [JSON results](../artifacts/ssrm_3d_results.json)
