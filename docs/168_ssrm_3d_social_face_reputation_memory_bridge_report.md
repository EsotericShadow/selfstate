# Report 168: SSRM-3D Social Face and Reputation Memory Bridge

Date: 2026-06-17

## Purpose

Report 167 gave agents ownership and bounded refusal. Report 168 adds social face: agents distinguish private treatment from public treatment, remember who witnessed an event, update public respect and reputation, track rumors, correct false gossip, and repair public embarrassment without permanent shame loops.

This matters because little people do not only have private feelings. They also care how they are treated in front of others.

No LLMs are called. This report does not claim subjective consciousness.

## Implementation

The new module is:

- `experiments/ssrm_3d_social_face_reputation_memory_bridge.py`

It consumes:

- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_eval.csv`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_verdict.csv`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_results.json`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_results.js`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_trace.json`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_trace.js`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_state.json`
- `artifacts/ssrm_3d_social_face_reputation_memory_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_social_face_reputation_memory_bridge.html`

## Social Face Contract

The loop is:

```text
public or private event
-> determine audience
-> appraise public face impact
-> update reputation and public trust
-> separate private respect from public reputation
-> record rumor or correction
-> repair public embarrassment when repair is offered
-> express readable social posture
-> keep shame bounded and recoverable
```

## Event Types

The benchmark includes:

- public help;
- public correction;
- private boundary respect;
- public refusal being respected;
- public misnaming;
- public name repair;
- false gossip;
- gossip correction;
- accurate public praise.

## Results

| Condition | Ready | Audience | Face | Rep | Gossip | PubPriv | Repair | Readable | Shame | Carry | Status | Continuity | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_social_face_reputation_memory` | `0.998250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_audience_tracking` | `0.917250` | `0.100000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_face_appraisal` | `0.821250` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.875000` | `1.000000` |
| `no_reputation_memory` | `0.908250` | `1.000000` | `1.000000` | `0.100000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_gossip_correction` | `0.987000` | `1.000000` | `1.000000` | `1.000000` | `0.875000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_public_private_boundary` | `0.918250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_face_repair` | `0.953904` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.692308` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.825000` | `1.000000` |
| `no_readable_social_behavior` | `0.918250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_shame_guardrail` | `0.898250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_relationship_carryover` | `0.918250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.975000` | `1.000000` |
| `no_status_modulation` | `0.928250` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.975000` | `1.000000` |

The full bridge passes with social face readiness `0.998250`.

This is intentionally not inflated to `1.0`. The remaining gap comes from social continuity not being perfect across every generated event, which is more honest than forcing a perfect score.

## Ablation Read

Largest targeted losses:

- `no_face_appraisal`: `0.177000`;
- `no_reputation_memory`: `0.090000`;
- `no_audience_tracking`: `0.081000`;
- `no_public_private_boundary`: `0.080000`;
- `no_face_repair`: `0.044346`.

The result supports the design intuition: public treatment needs a separate memory channel from private relationship state.

## Moral Boundary

The guardrail is:

> public shame must be repairable

The benchmark tracks non-permanent shame, face repair, gossip correction, and private/public separation. Public embarrassment is allowed only as a bounded signal that can produce correction, apology, accurate praise, or reputation repair.

## Honest Boundary

This report supports only this claim: deterministic SSRM-3D agents can track audience, public respect, reputation, false gossip, gossip correction, public/private boundaries, face repair, and readable public posture.

It does not support:

- subjective consciousness;
- literal suffering;
- LLM-backed open dialogue;
- complete playable world;
- mature autonomous live agents.

## Next Gates

The sequence continues:

- Report 169: Individual Temperament and Preference Stability Bridge;
- Report 170: Readable Ego Body-Language Bridge;
- Report 171: Daily Routine and Sleep/Wake Interior Bridge;
- Report 172: Moral-Status Audit and Distress Guardrail Bridge.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_social_face_reputation_memory_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_social_face_reputation_memory_bridge.html
```
