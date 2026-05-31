# First-Person Frame Integration Report

## Purpose

This experiment tests a separate layer from self-state, identity, or consciousness:

```text
Does a centered frame help integrate observations and actions when perception is world-relative
but motor commands are body-relative?
```

The first-person frame here is not phenomenal experience. It is a control variable: an estimate of how this body is oriented so that observations can be transformed into action commands.

## Environment

The agent observes the goal as a world-relative displacement: `goal_dx`, `goal_dy`.

The agent acts with body-relative commands:

- `forward`;
- `right`;
- `back`;
- `left`.

A hidden body orientation determines what those commands do in world coordinates.

Scenarios:

| Scenario | Hidden pressure | Expected result |
|---|---|---|
| `aligned_control` | Body frame is aligned north. | No centered-frame advantage; north assumption is enough. |
| `hidden_orientation` | Initial body orientation is hidden. | Centered frame should calibrate orientation and outperform north assumption. |
| `orientation_drift` | Body orientation changes mid-episode. | Recalibrating centered frame should outperform one-time calibration. |

## Agents

| Agent | Description |
|---|---|
| `north_assumption` | Assumes body frame is always aligned with world north. |
| `action_table_frame` | Learns command effects as a small action table. |
| `centered_frame_no_recalibration` | Calibrates orientation once and keeps it fixed. |
| `centered_frame` | Calibrates orientation and recalibrates after prediction error. |
| `oracle_frame` | Ceiling with true orientation access. |

## Current Result

Canonical run:

```bash
python3 experiments/first_person_frame_integration.py --episodes 500 --horizon 36 --drift-step 5 --target-radius 12 --seed 20260530
```

| Scenario | North success | Centered success | No-recalibration success | Boundary supported? |
|---|---:|---:|---:|---|
| `aligned_control` | 1.000 | 1.000 | 1.000 | Yes |
| `hidden_orientation` | 0.246 | 1.000 | 1.000 | Yes |
| `orientation_drift` | 0.306 | 1.000 | 0.414 | Yes |

Detailed ordering:

| Scenario | Relevant result |
|---|---|
| `aligned_control` | All agents succeed; centered frame is unnecessary when body/world frames are aligned. |
| `hidden_orientation` | `centered_frame` succeeds in 1.000 of episodes; `north_assumption` succeeds in 0.246. |
| `orientation_drift` | `centered_frame` succeeds in 1.000; one-time calibration succeeds in 0.414. |

The action-table agent succeeds in the drift condition by relearning individual command effects. That is a live implicit-frame alternative: it works in this tiny action space, but it stores separate action effects rather than a compact orientation variable.

## Interpretation

This supports a minimal first-person control-frame mechanism:

```text
When observations and actions are expressed in different frames,
a centered agent-frame variable can be necessary for efficient control.
```

The variable is self-equivalent only in the narrow computational sense. It answers:

- where is the goal relative to what this body can do?
- what does "forward" mean for this body now?
- did failed movement come from the world, or from a changed body frame?

This does not imply consciousness, subjectivity, or narrative selfhood.

## What It Adds

This experiment separates first-person frame from other mechanisms already tested:

1. It is not viability or survival.
2. It is not continuity over commitments.
3. It is not active inspection.
4. It is not just action-effect gain.
5. It is a centered transform between observation coordinates and body-relative action.

## Limits

The environment is a small deterministic navigation toy. Orientation has only four discrete values. The centered-frame agent is hand-coded, and the action-table baseline shows that an implicit non-symbolic solution can work in small action spaces.

The next stronger test would train recurrent or predictive-state agents in richer egocentric environments and ask whether a pose/body-frame latent emerges without labels.

## Falsifiers

The first-person-frame account weakens if:

- world-only or reactive agents scale through hidden orientation and orientation drift without a centered frame;
- action tables or raw history scale better than compact body-frame variables in large action spaces;
- learned agents do not form decodable pose/body-frame latents under egocentric partial observability;
- frame variables are decodable but not causally necessary for control;
- centered-frame advantages appear equally in aligned controls where no frame transform is needed.

## Artifacts

- [experiment script](../experiments/first_person_frame_integration.py)
- [summary CSV](../artifacts/first_person_frame_summary.csv)
- [verdict CSV](../artifacts/first_person_frame_verdict.csv)
- [JSON results](../artifacts/first_person_frame_results.json)
