# SSRM-3D Social Ecology Report

## Question

When does communication become cheaper than acting alone?

This report follows the SSRM-3D social-pressure precursor with a narrower test. It does not reward talking, bonding, friendship, or language. Communication has explicit energy/time/opportunity costs, and return-selected policies are evaluated only by survival, resources, repair, deception resistance, trust maintenance, and future options.

The tested boundary is:

> Costly communication should be rejected when it has no job, and selected only when a signal, name, gossip report, or trust-maintenance check-in buys more control than it costs.

## Experiment

Canonical command:

```bash
python3 experiments/ssrm_3d_social_ecology.py --train-episodes 80 --eval-episodes 120 --candidate-count 180 --seed 20260612
```

The experiment uses five social ecology scenarios:

| Scenario | Pressure | Expected useful communication |
|---|---|---|
| `visible_solo_control` | visible resources, no social information advantage | none |
| `costly_warning_signal` | a scout knows a safer resource route | signal |
| `persistent_identity_names` | helpers and opportunists recur | name/identity label |
| `absent_agent_gossip` | absent deceivers and cache histories matter | name plus gossip |
| `trust_maintenance_infrastructure` | future repair, shared tools, and scarce resources depend on trust | signal, name, gossip, check-in |

Candidate policies can use signals, names, gossip, check-ins, babble, or deception-like short-term communication. They are selected by training return, then re-evaluated under:

- no-communication baseline;
- full selected policy;
- signal ablation;
- name ablation;
- gossip ablation;
- check-in ablation;
- babble control.

## Results

| Scenario | Selected policy | Selected reward | No-comm reward | Gain | Key loss | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `visible_solo_control` | `no_comm_baseline` | 145.540 | 145.540 | 0.000 | babble loses 53.472 | costly communication rejected |
| `costly_warning_signal` | `costly_signal_only` | 108.168 | 7.385 | 100.783 | signal loss 102.066 | warning signal earns cost |
| `persistent_identity_names` | `identity_label_memory` | 106.980 | 14.840 | 92.140 | name loss 92.140 | name compresses social history |
| `absent_agent_gossip` | `gossip_with_names` | 100.880 | -11.560 | 112.440 | gossip loss 84.658 | gossip preserves options |
| `trust_maintenance_infrastructure` | `trust_maintenance_full` | 161.450 | -64.900 | 226.350 | check-in loss 130.616 | low-cost contact maintains infrastructure |

All five verdict rows pass `supports_social_ecology_precursor=True`.

## Interpretation

This is a partial Gate 3 extension, not a full language-emergence result.

The useful pattern is specific:

- communication is rejected in the visible solo control;
- babble is punished by cost when it has no control job;
- a warning signal is useful only when route information beats rediscovery;
- a name becomes useful when identity history compresses who helped or exploited;
- gossip becomes useful when absent-agent information improves future decisions;
- check-ins become useful when low-cost contact preserves trust, repair, and shared-tool access.

This tightens the social-self boundary. Modeling other agents is not selfhood by itself. The result matters only because the tested agent's future depends on how persistent others remember, help, exploit, deceive, or trust it. In that regime, selfhood begins to include social control state: not just "what can I do?" but "what do they remember me as, and what future options does that open or close?"

## Failure Modes Kept Alive

The result remains toy-scale and return-selected.

It does not show:

- open-ended language;
- learned communication protocols from raw interaction;
- learned deception arms races;
- friendship, status, tribes, or emotion;
- learned-controller discovery of social communication;
- a general law that societies must emerge.

The strongest falsifier is still a learned-controller social ecology where no persistent identity, reputation, or self-as-modeled-by-others variable is needed, yet performance matches under scarce resources, repair dependence, deception, shared tools, and future cooperation.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_social_ecology.html
```

The visualization replays `artifacts/ssrm_3d_social_ecology_trace.json`, showing the tested agent, persistent social roles, signal/name/gossip/check-in events, communication cost, trust state, and future-option preservation.

The page also loads generated JS fallback artifacts so it can recover when opened outside the repo-root server path.

## Artifacts

- [experiment script](../experiments/ssrm_3d_social_ecology.py)
- [visualization](../visualizations/ssrm_3d_social_ecology.html)
- [evaluation CSV](../artifacts/ssrm_3d_social_ecology_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_social_ecology_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_social_ecology_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_social_ecology_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_social_ecology_trace.json)
- [JSON results](../artifacts/ssrm_3d_social_ecology_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_social_ecology_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_social_ecology_results.js)
