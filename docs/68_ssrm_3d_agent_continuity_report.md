# SSRM-3D Agent Continuity Report

## Question

When is a saved or restored agent the same continuing control process rather than a new system using similar parts?

This report turns continuity into a concrete serialization problem. The ML model is not continuity by itself. The database is not continuity by itself. The body state is not continuity by itself. Continuity is the binding record that lets a paused agent wake up with the same body history, social history, unfinished commitments, learned relationships, world consequences, attention trajectory, hidden state, tools, goals, and branch identity.

The tested boundary is:

> A restored agent should preserve future control only when the continuity-relevant record is preserved. Model-only copies, incompatible memory transplants, social resets, commitment resets, tool resets, and ambiguous forks should fail in specific pressure regimes.

## AgentContinuityRecord

The experiment uses an explicit record:

```text
agent_id
birth_time
current_world_id
current_body_state
model_version
memory_db
social_memory_db
commitment_ledger
event_log_pointer
attention_state
last_hidden_state
tool_inventory
relationship_state
active_goals
branch_id
fork_parent_id
```

This is not a claim that such a record is sufficient for personhood or consciousness. It is a control record for testing whether the agent's past constrains its future.

## Experiment

Canonical command:

```bash
python3 experiments/ssrm_3d_agent_continuity.py --episodes 120 --seed 20260613
```

The experiment tests five restart/fork pressures:

| Scenario | Pressure | Expected required continuity |
|---|---|---|
| `clean_pause_resume` | ordinary pause/resume | memory and commitment ledger |
| `body_model_mismatch` | restored agent must remember damaged body and hidden policy state | body, model, attention, hidden state |
| `social_repair_debt` | repair access depends on remembered relationships and social debt | body, memory, social memory, commitments |
| `tool_commitment_return` | unfinished commitments require remembered tools and route marks | memory, hidden state, commitments, tools |
| `fork_rollback_boundary` | forked and rolled-back agents must preserve branch identity and event-log position | full continuity plus branch identity |

Each scenario is evaluated under:

- full continuity record;
- model-only copy;
- memory-only transplant;
- body/hidden-state ablation;
- social-memory reset;
- commitment-ledger reset;
- tool-inventory reset;
- fork without branch id;
- clean fork branch.

## Results

| Scenario | Full reward | Model-only reward | Key loss | Verdict |
|---|---:|---:|---:|---|
| `clean_pause_resume` | 213.914 | 99.022 | commitment loss 40.843 | continuity record preserves clean resume |
| `body_model_mismatch` | 214.060 | 6.767 | body/hidden loss 100.433 | body and hidden state required |
| `social_repair_debt` | 214.057 | 12.758 | social loss 43.785 | social continuity preserves repair relationships |
| `tool_commitment_return` | 214.052 | 39.235 | tool loss 19.252 | tools and commitments bind externalized continuity |
| `fork_rollback_boundary` | 213.998 | -46.827 | fork loss 132.946 | forks become separate continuities after shared history |

All five verdict rows pass `supports_agent_continuity_precursor=True`.

## Interpretation

This is a stronger continuity precursor than the earlier interruption-coherence ledger.

The older test showed that owner/epoch metadata filters corrupted memory. This test asks a broader persistence question: what must be serialized for the same agent to continue after pause, restore, body mismatch, social reset, tool loss, rollback, or fork?

The result supports a narrow claim:

- copying model weights into a new body is not enough;
- copying memory into an incompatible body/model is not enough;
- social history matters only when future repair or trust depends on it;
- tools become continuity-relevant when externalized cognition carries unfinished commitments;
- forks share history until the split, then require separate branch identity.

This makes identity continuity more falsifiable. If a model-only copy or a generic memory transplant matched the full continuity record across these pressures, the continuity-self hypothesis would weaken.

## Purpose Layer

This experiment does not test existential language or purpose claims.

The useful future translation is behavioral: purpose should first be treated as long-horizon value compression, not as a prompted self-report. A later test should ask whether an agent preserves goals that are not immediately rewarded, protects tools or places because they matter to its continuity, asks why a commitment exists, resists goals that conflict with its history, or creates a long-term project.

Only after continuity, social memory, communication, tools, loss, and long-term projects are stable should a human-contact layer offer a purpose as localized world input. The agent should be able to integrate, reinterpret, resist, or ignore that offer.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_agent_continuity.html
```

The visualization replays `artifacts/ssrm_3d_agent_continuity_trace.json`, showing pause, restore, pressure, and outcome frames for the full continuity record in the fork/rollback scenario. It also displays component coherence bars and verdict rows.

The page loads generated JS fallback artifacts so it can recover when opened outside the repo-root server path.

## Artifacts

- [experiment script](../experiments/ssrm_3d_agent_continuity.py)
- [visualization](../visualizations/ssrm_3d_agent_continuity.html)
- [evaluation CSV](../artifacts/ssrm_3d_agent_continuity_eval.csv)
- [summary CSV](../artifacts/ssrm_3d_agent_continuity_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_agent_continuity_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_agent_continuity_trace.json)
- [JSON results](../artifacts/ssrm_3d_agent_continuity_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_agent_continuity_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_agent_continuity_results.js)
