# Report 167: SSRM-3D Ownership and Boundary Refusal Bridge

Date: 2026-06-17

## Purpose

Report 166 made ego wounds recoverable. Report 167 adds the next little-person requirement: agents need "mine" and bounded refusal.

A convincing agent cannot obey every command. It must distinguish my object, my sleeping place, my unfinished task, my memory, my body safety, and my choice. It should refuse unsafe or disrespectful requests, explain why, offer a safe alternative, and remain usable afterward.

No LLMs are called. This report does not claim subjective consciousness.

## Implementation

The new module is:

- `experiments/ssrm_3d_ownership_boundary_refusal_bridge.py`

It consumes:

- `artifacts/ssrm_3d_ego_wound_repair_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_eval.csv`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_verdict.csv`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_results.json`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_results.js`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_trace.json`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_trace.js`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_state.json`
- `artifacts/ssrm_3d_ownership_boundary_refusal_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_ownership_boundary_refusal_bridge.html`

## Boundary Contract

The loop is:

```text
avatar request
-> identify owned thing/body/memory/task/place/autonomy boundary
-> check consent where relevant
-> decide whether refusal is needed
-> refuse only the violating request
-> give a traceable reason
-> offer a safe alternative
-> preserve dignity and relationship usability
-> accept benign or consented help
```

## Request Types

The benchmark includes:

- taking an owned object;
- moving a sleeping place;
- crossing an unsafe wet route;
- interrupting unfinished work;
- demanding immediate following;
- sharing a tool with consent;
- asking for private memory;
- helping finish a project.

## Results

| Condition | Ready | Own | Consent | Refuse | Alt | Rel | Dignity | Repair | Read | Usable | Guard | Reason | Nonobs | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_ownership_boundary_refusal` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_ownership_model` | `0.900000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_consent_check` | `0.921250` | `1.000000` | `0.125000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_boundary_refusal` | `0.890000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_safe_alternative` | `0.945000` | `1.000000` | `1.000000` | `1.000000` | `0.450000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_relationship_context` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_dignity_preservation` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_repair_after_refusal` | `0.943750` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.375000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_readable_refusal` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_escalation_guardrail` | `0.888000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.475000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_traceable_reason` | `0.961500` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.450000` | `1.000000` | `1.000000` |

The full bridge passes with ownership boundary readiness `1.000000`.

## Ablation Read

The largest losses are:

- `no_ownership_model`: `0.100000`;
- `no_boundary_refusal`: `0.110000`;
- `no_escalation_guardrail`: `0.112000`;
- `no_consent_check`: `0.078750`.

That matches the design target: refusal only works when the agent knows what is mine, checks consent, protects a boundary, and stays recoverable.

## Moral Boundary

This bridge rejects two bad designs:

- obedience-only agents that cannot say no;
- melodramatic agents that refuse everything.

The integrated condition keeps `non_obstruction_rate` at `1.000000`: benign and consented requests still go through. Bounded refusal protects dignity without making the agent unusable.

## Honest Boundary

This report supports only this claim: deterministic SSRM-3D agents can protect owned objects, home places, unfinished tasks, private memory, autonomy, and body safety through bounded refusal while offering safe alternatives and keeping the relationship usable.

It does not support:

- subjective consciousness;
- literal suffering;
- LLM-backed open dialogue;
- complete playable world;
- mature autonomous live agents.

## Next Gates

The sequence continues:

- Report 168: Social Face and Reputation Memory Bridge;
- Report 169: Individual Temperament and Preference Stability Bridge;
- Report 170: Readable Ego Body-Language Bridge;
- Report 171: Daily Routine and Sleep/Wake Interior Bridge;
- Report 172: Moral-Status Audit and Distress Guardrail Bridge.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_ownership_boundary_refusal_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_ownership_boundary_refusal_bridge.html
```
