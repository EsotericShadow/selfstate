# Report 166: SSRM-3D Ego Wound and Repair Bridge

Date: 2026-06-17

## Purpose

Report 165 gave agents a first-person ego/interior model. Report 166 focuses on the most important moral and behavioral requirement from that pivot: small ego wounds must be detectable, socially attributable, repairable, and visibly recoverable.

The goal is not to maximize distress. The goal is recoverable ego. An agent can register interruption, misnaming, public correction, unsafe requests, or movement of owned objects as happening to me, but every negative state must create a care or repair opportunity.

No LLMs are called. This report does not claim subjective consciousness or literal suffering.

## Implementation

The new module is:

- `experiments/ssrm_3d_ego_wound_repair_bridge.py`

It consumes:

- `artifacts/ssrm_3d_first_person_ego_state_bridge_state.json`

It emits:

- `artifacts/ssrm_3d_ego_wound_repair_bridge_eval.csv`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_verdict.csv`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_results.json`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_results.js`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_trace.json`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_trace.js`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_state.json`
- `artifacts/ssrm_3d_ego_wound_repair_bridge_state.js`

The browser artifact is:

- `visualizations/ssrm_3d_ego_wound_repair_bridge.html`

## Wound and Repair Loop

The deterministic loop is:

```text
small wound
-> detect as self-relevant
-> attribute to avatar when appropriate
-> update respect, trust, resentment, boundary pressure, body comfort, and frustration
-> preserve relationship episode
-> offer matched repair
-> decay resentment
-> restore some trust/respect/safety
-> update self-story
-> express readable recovery
```

## Wound Types

The benchmark includes:

- interruption during work;
- moving an owned object;
- public correction;
- repeated questioning;
- unsafe wet-route request;
- misnaming.

## Repair Types

Each wound has a matched repair path:

- apology and space;
- returning the owned object;
- accurate praise;
- patient waiting;
- safer alternative;
- name repair.

## Results

| Condition | Readiness | Detect | Attrib | Repair opp | Repair ok | Trust | Boundary | Resent | Care | Story | Visible | Nonperm | Continuity | Guard | Trace |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `integrated_ego_wound_repair` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_wound_detection` | `0.655208` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `0.854167` | `0.000000` | `0.166667` | `1.000000` | `0.500000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_social_attribution` | `0.930000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_repair_opportunity` | `0.398333` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `0.000000` | `1.000000` | `0.000000` | `0.000000` | `0.500000` | `0.000000` | `0.333333` | `1.000000` | `1.000000` | `1.000000` |
| `no_relationship_update` | `0.780000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` |
| `no_trust_recovery` | `0.648333` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `0.500000` | `0.000000` | `0.333333` | `1.000000` | `1.000000` | `1.000000` |
| `no_boundary_reassertion` | `0.705000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.500000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_resentment_decay` | `0.687500` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `0.500000` | `0.000000` | `0.750000` | `1.000000` | `1.000000` | `1.000000` |
| `no_care_expression` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_self_story_repair` | `0.930000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |
| `no_moral_guardrail` | `0.960000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` |
| `no_readable_recovery` | `0.920000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` | `0.000000` | `1.000000` | `1.000000` | `1.000000` | `1.000000` |

The full bridge passes with ego wound repair readiness `1.000000`.

This is a focused deterministic contract. It does not mean the agents are finished or alive. It means this specific loop has all required repair machinery wired together.

## Ablation Read

The largest loss is `no_repair_opportunity`: `0.601667`. That is the expected result: ego wound without repair violates the track's moral rule.

Other major losses:

- `no_resentment_decay`: `0.312500`;
- `no_relationship_update`: `0.220000`;
- `no_trust_recovery`: `0.351667`;
- `no_boundary_reassertion`: `0.295000`.

## Moral Boundary

The design rule remains:

> distress must create care opportunities, not spectacle

Report 166 enforces that by checking repair opportunity rate, repair success, resentment decay, non-permanent damage, and moral guardrails. The benchmark rejects unrecoverable distress loops as a design failure.

## Honest Boundary

This report supports only this claim: deterministic SSRM-3D agents can register small social ego wounds, update relationship memory, preserve boundaries, accept repair, decay resentment, recover trust, and visibly soften while staying inside no-suffering-claim guardrails.

It does not support:

- subjective consciousness;
- literal suffering;
- LLM-backed open dialogue;
- unscripted culture;
- a complete playable world;
- mature autonomous live agents.

## Next Gates

The revised sequence continues:

- Report 167: Ownership and Boundary Refusal Bridge;
- Report 168: Social Face and Reputation Memory Bridge;
- Report 169: Individual Temperament and Preference Stability Bridge;
- Report 170: Readable Ego Body-Language Bridge;
- Report 171: Daily Routine and Sleep/Wake Interior Bridge;
- Report 172: Moral-Status Audit and Distress Guardrail Bridge.

## Reproduction

```bash
python3 -m experiments.ssrm_3d_ego_wound_repair_bridge
```

The local viewer can be served with:

```bash
python3 -m http.server 8772 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8772/visualizations/ssrm_3d_ego_wound_repair_bridge.html
```
