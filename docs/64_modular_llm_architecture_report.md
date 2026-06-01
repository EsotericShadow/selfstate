# Modular LLM Architecture Report

## Question

What does the research program gain by treating an LLM as one module inside an adaptive system rather than as the whole agent?

The answer is a control-boundary test.

If the LLM is treated as the organism, then selfhood, language, planning, memory, action, and consciousness collapse into one opaque object. That would make the theory harder to falsify. If the LLM is one slow reasoning module inside a layered control system, then the self-model can be tested separately as persistent control state.

## Architecture Claim

The LLM is not the self.

The self-model is the persistent control state that links viability, capability, uncertainty, commitments, memory, attention, prediction error, and action consequences across time.

The LLM is a language and abstraction module. It reads a compressed state packet, produces recommendations or hypotheses, and may propose memory edits or plans. It does not own reflexes, realtime motor control, collision avoidance, energy maintenance, or survival arbitration.

## Layer Contract

| Layer | Control role | LLM access |
|---|---|---|
| Reflex | Fast survival overrides for hazards and viability. | No direct access. |
| Perception | Converts world and body streams into state estimates. | Receives only summarized outputs. |
| Self-state | Tracks energy, damage, capability, uncertainty, commitments, and continuity. | Reads and proposes high-level edits through the arbiter. |
| Attention | Scores threat, energy, damage, goals, commitments, novelty, prediction error, social signals, tools, memory, navigation, and uncertainty. | Reads top priorities. |
| Arbiter | Chooses between survival, goals, curiosity, commitments, social pressure, and LLM proposals. | Can accept or reject recommendations. |
| LLM | Slow abstract reasoning, decomposition, reflection, explanation, social reasoning, tool-use proposals, and memory summaries. | Receives compressed packets only. |
| Action | Executes motor or tool actions. | No direct motor control. |

## Rate Contract

Ticks are the simulator's implementation clock. Rates are the architecture.

The system should be documented as a multi-rate controller, even when the code counts integer ticks internally:

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
reflection_hz = event_triggered
```

The implementation can convert those rates into intervals:

```text
interval_ticks = base_tick_hz / subsystem_hz
```

The falsifiable claim is not that every layer updates every world tick. The claim is that survival pressure, motor correction, perception, attention, self-state maintenance, goal arbitration, language reasoning, and memory consolidation operate on different timescales. A single-loop architecture that asks the LLM to process every tick would erase the boundary this report is trying to test.

## Compressed Packet Boundary

The LLM should receive a packet like this:

```json
{
  "self": {
    "energy": 0.41,
    "damage": "left actuator degraded",
    "confidence": 0.72,
    "current_goal": "reach shelter"
  },
  "world": {
    "threat_nearby": true,
    "resource_visible": true,
    "shelter_direction": "northwest"
  },
  "attention": {
    "top_priority": "avoid hazard",
    "prediction_error": "movement slower than expected"
  },
  "memory": {
    "commitment": "return to charging station before night"
  }
}
```

The LLM can answer:

```text
Recommendation: prioritize shelter over resource collection.
Reason: energy is low, actuator damage reduces travel margin, and night is approaching.
```

The arbiter still decides.

## Falsifiable Predictions

If this architecture is correct:

- removing the LLM should hurt slow abstract planning, social explanation, hypothesis generation, tool-use proposals, and memory summarization more than reflex survival;
- direct LLM motor control should increase invalid actions, latency, hazard exposure, and recovery failures;
- full world dumps should not outperform compressed packets when the arbiter and self-state layers already maintain the relevant state;
- corrupting self-state should hurt both LLM recommendations and non-LLM arbitration under embodied pressure;
- corrupting language output alone should not destroy low-level reflexes or basic collision avoidance;
- the LLM should become more useful only when tasks require slow abstraction, counterfactual planning, social reasoning, externalized cognition, or long commitment repair.

If removing the LLM improves all performance, the language module is harmful in this environment.

If direct LLM control matches layered control at realtime survival, the architecture boundary is too conservative.

If LLM access to the full world state beats compressed packets in every stage, then the compressed-state claim is too narrow or the packet omits important state.

## Relation To SSRM-3D

SSRM-3D already implements the first version of this boundary:

- reflexes can override immediately under hazard pressure;
- perception runs at 10 Hz;
- self-state and goal arbitration run slower than reflexes and perception;
- the self-state workspace tracks viability, mobility, sensor capability, confidence, commitments, and prediction error;
- attention weighs threat, energy, damage, uncertainty, novelty, prediction error, goals, commitments, and social pressure;
- the arbiter chooses action mode;
- the language-like module only recommends from a compressed packet;
- the motor layer executes movement.

The current implementation is deterministic and toy-scale. It does not call an external LLM. That is intentional for the current research phase: the experiment needs a clean control boundary before adding a stochastic language model.

## Stronger Next Test

The next version should add a specific LLM-stream ablation to the SSRM-3D done-enough gates:

| Variant | Expected result |
|---|---|
| No LLM | Reflex survival remains intact; slow planning, explanation, tool-use proposals, and social hypotheses decline. |
| Advisory LLM | Abstract planning improves only when the packet contains enough self/world/attention/memory state. |
| Direct motor LLM | Hazard handling and low-level movement degrade under realtime pressure. |
| Full-world LLM | May improve explanation, but should not replace self-state and arbiter layers without latency or control costs. |
| Corrupted self packet | LLM recommendations become specifically wrong in ways predicted by the corrupted self-state. |

This test belongs after tool-making and richer social pressure are integrated into learned-controller runs, because those are the regimes where slow language reasoning should actually matter.

## Visualization

Open the architecture visualization through a local server:

```bash
python3 -m http.server 8765
```

Then open:

```text
http://127.0.0.1:8765/visualizations/modular_llm_architecture.html
```

The visualization shows the control layers, the compressed packet boundary, the arbiter gate, and three ablation modes: normal advisory LLM, LLM removed, and invalid direct motor control.

## Current Interpretation

This architecture keeps the project from smuggling selfhood into language.

The self-equivalent object under test remains the persistent control state. The LLM is a reasoning organ that can read and influence parts of that state only through an arbiter. That separation makes the claim falsifiable: language can help, hurt, or be irrelevant depending on whether the environment actually requires slow abstraction.

## Artifacts

- [SSRM-3D embodied-world script](../experiments/ssrm_3d_embodied_world.py)
- [SSRM-3D embodied-world report](60_ssrm_3d_embodied_world_report.md)
- [SSRM-3D done-enough gates](63_ssrm_3d_done_enough_gates.md)
- [modular LLM architecture visualization](../visualizations/modular_llm_architecture.html)
