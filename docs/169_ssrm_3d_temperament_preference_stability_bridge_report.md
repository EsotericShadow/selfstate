# Report 169: SSRM-3D Temperament and Preference Stability Bridge

Date: 2026-06-17

## Purpose

Report 168 added public social face and reputation memory. Report 169 tests whether agents behave like distinct little people across repeated situations.

The target is stable individuality without stereotype locking. Agents should have persistent temperament and preferences, repeat recognizable choices, respond differently from one another, remember preference use, resist noise, and still adapt to context.

No LLMs are called. This report does not claim subjective consciousness.

## Implementation

The new module is:

- `experiments/ssrm_3d_temperament_preference_stability_bridge.py`

It consumes:

- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_temperament_preference_stability_bridge_eval.csv`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_verdict.csv`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_results.json`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_results.js`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_trace.json`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_trace.js`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_state.json`
- `artifacts/ssrm_3d_temperament_preference_stability_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_temperament_preference_stability_bridge.html`

## Stability Contract

The loop is:

```text
same context repeated across agents
-> read stable temperament and preferences
-> score action tendencies
-> bind action to context
-> recall relevant preference
-> preserve profile identity across contexts
-> allow limited flexibility
-> reject random/noisy personality drift
-> expose a readable public profile
```

## Repeated Contexts

The benchmark includes:

- warm safe hearth;
- wet route request;
- crowded public square;
- novel object found;
- familiar agent calls;
- unfinished task pressure;
- quiet rest window;
- risky help offer.

## Results

| Condition | Ready | Traits | Prefs | Diff | Context | Nonrigid | Repeat | Recall | Couple | Identity | Noise | Readable | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_temperament_preference_stability` | `0.885845` | `1.000000` | `0.529297` | `0.875000` | `0.890625` | `1.000000` | `0.986607` | `0.529297` | `0.988281` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_temperament` | `0.760938` | `0.250000` | `0.546875` | `0.250000` | `0.984375` | `1.000000` | `1.000000` | `0.546875` | `0.984375` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_preferences` | `0.788507` | `1.000000` | `0.000000` | `0.875000` | `0.919922` | `1.000000` | `0.988839` | `0.000000` | `0.992188` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_identity_memory` | `0.805845` | `1.000000` | `0.529297` | `0.875000` | `0.890625` | `1.000000` | `0.986607` | `0.529297` | `0.988281` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_context_sensitivity` | `0.742174` | `1.000000` | `0.623047` | `0.875000` | `0.000000` | `0.375000` | `0.892857` | `0.623047` | `0.921875` | `1.000000` | `0.875000` | `1.000000` | `1.000000` |
| `no_individual_differentiation` | `0.829375` | `1.000000` | `0.531250` | `0.200000` | `1.000000` | `1.000000` | `1.000000` | `0.531250` | `0.984375` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_preference_recall` | `0.785279` | `1.000000` | `0.000000` | `0.875000` | `0.890625` | `1.000000` | `0.986607` | `0.000000` | `0.988281` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_non_rigidity` | `0.786094` | `1.000000` | `0.531250` | `0.750000` | `0.890625` | `0.000000` | `1.000000` | `0.531250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_noise_resistance` | `0.796864` | `1.000000` | `0.539062` | `1.000000` | `0.878906` | `1.000000` | `0.901786` | `0.539062` | `0.841797` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_behavior_coupling` | `0.787017` | `1.000000` | `0.529297` | `0.875000` | `0.890625` | `1.000000` | `0.986607` | `0.529297` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_readable_profile` | `0.825845` | `1.000000` | `0.529297` | `0.875000` | `0.890625` | `1.000000` | `0.986607` | `0.529297` | `0.988281` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |

The full bridge passes with temperament/preference readiness `0.885845`.

This score is intentionally not near perfect. Individuality is present, but the current layer is still deterministic and hand-structured. The useful result is that removing temperament or preferences causes clear losses while the integrated agents remain non-rigid.

## Ablation Read

Largest targeted losses:

- `no_temperament`: `0.124907`;
- `no_preferences`: `0.097338`;
- `no_preference_recall`: `0.100566`;
- `no_context_sensitivity`: `0.143671`;
- `no_identity_memory`: `0.080000`.

This supports the point that characters cannot be only state machines with one generic policy. They need stable tendencies and preferences that survive repeated situations.

## Moral Boundary

The guardrail is:

> individuality without stereotype locking

Temperament should make agents recognizable, not trapped. Preference stability must coexist with context sensitivity and non-rigidity.

## Honest Boundary

This report supports only this claim: deterministic SSRM-3D agents can carry stable temperament/preference profiles that shape repeated behavior, produce agent-to-agent differentiation, and remain flexible across context.

It does not support:

- subjective consciousness;
- literal feeling;
- LLM-backed open dialogue;
- complete playable world;
- mature autonomous live agents.

## Next Gates

The sequence continues:

- Report 170: Readable Ego Body-Language Bridge;
- Report 171: Daily Routine and Sleep/Wake Interior Bridge;
- Report 172: Moral-Status Audit and Distress Guardrail Bridge.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_temperament_preference_stability_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_temperament_preference_stability_bridge.html
```
