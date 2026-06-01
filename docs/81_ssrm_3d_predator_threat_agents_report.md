# SSRM-3D Predator/Threat Agents Report

## Question

Do tracking threats create persistent control pressure without turning the simulation into animal roleplay?

Report 74 puts predator/threat agents after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, and social trust/contracts. This experiment asks whether threat perception, self-vulnerability state, sound/scent memory, stealth, shelter, alarms, social warning, and restore continuity become useful only when a tracker changes future viability.

The tested claim is narrow:

> Threat machinery should be rejected in a safe control, but selected when trackers exploit sound, scent, weakness, routines, social isolation, or restore-time forgetting.

This is not a predator simulation. It tests threats as control pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_predator_threat_agents.py --train-episodes 72 --eval-episodes 96 --seed 20260626 --candidate-count 7
```

The experiment uses return-selected candidate policies over abstract threat-control state. Policies can use:

| Channel | Role |
|---|---|
| threat perception | estimates tracker pressure before damage occurs |
| self-vulnerability state | treats injury/weakness as something trackers can exploit |
| sound/scent memory | remembers and reduces own trace profile |
| stealth action | trades speed for lower detection |
| shelter memory | uses safe places to reduce exposure |
| tool alarm | lowers surprise and enables earlier avoidance |
| social warning | coordinates group defense and shared shelter |
| continuity memory | preserves tracker pattern, alarms, shelter, and warnings after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact threat control |
| `no_threat_perception` | removes early threat estimation |
| `no_self_vulnerability_state` | removes body-state-aware threat handling |
| `no_sound_scent_memory` | removes trace memory |
| `no_stealth_action` | removes stealth control |
| `no_shelter_access` | removes shelter use |
| `no_tool_alarm` | removes alarm use |
| `no_social_warning` | removes group warning |
| `no_continuity` | removes restore-time threat continuity |
| `reactive_panic_only` | waits for obvious danger before responding |
| `omniscient_threat_control` | upper-bound threat control |

## Results

| Scenario | Selected policy | Perception loss | Self loss | Sound/scent loss | Stealth loss | Shelter loss | Alarm loss | Social loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `open_safe_control` | `no_threat_baseline` | 0.050 | 0.001 | 0.054 | -0.010 | 0.012 | 0.049 | 0.037 | 0.043 | threat machinery rejected |
| `sound_tracking_predator` | `sound_stealth_alarm_planner` | 241.950 | 2.880 | 97.304 | 212.716 | -1.753 | 247.609 | 3.255 | -0.840 | sound tracking stealth/alarm pressure |
| `scent_weakness_tracker` | `scent_vulnerability_shelter_planner` | 799.505 | 625.712 | 698.117 | 691.223 | 227.281 | -2.645 | -2.568 | -2.496 | scent weakness self/shelter pressure |
| `routine_ambush_predator` | `routine_avoidance_alarm_planner` | 436.794 | 0.102 | 79.481 | 768.663 | -0.278 | 49.838 | 0.008 | 0.035 | routine ambush route/stealth pressure |
| `social_warning_group_defense` | `social_warning_shelter_planner` | 853.586 | 429.448 | 16.269 | 8.571 | 505.424 | 611.224 | 709.125 | 22.671 | social warning group defense pressure |
| `restore_threat_continuity` | `continuity_threat_planner` | 901.346 | 174.666 | 112.164 | 687.772 | 180.319 | 190.285 | 573.358 | 125.758 | restore threat continuity pressure |

All six verdict rows pass `supports_predator_threat_precursor=True`.

Key targeted losses:

- `open_safe_control`: threat machinery is not selected and all ablations have near-zero effect.
- `sound_tracking_predator`: removing threat perception, sound/scent memory, stealth, or alarms causes large loss.
- `scent_weakness_tracker`: removing self-vulnerability, sound/scent memory, stealth, or shelter causes large loss.
- `routine_ambush_predator`: removing threat perception, sound/scent memory, stealth, or alarms causes large loss.
- `social_warning_group_defense`: removing social warning, shelter, alarm, self-vulnerability, or threat perception causes large loss.
- `restore_threat_continuity`: removing continuity plus perception, self-state, trace memory, stealth, shelter, alarms, or social warning causes large loss.

## Interpretation

This result supports the seventh pressure-layer step at precursor level:

- threat state is not globally useful;
- fear-like control state is useful only when it changes attention, risk, stealth, shelter, alarms, or group defense;
- sound and scent matter only when the agent's own trace can be tracked;
- self-vulnerability matters only when weakness changes threat exposure;
- social warning matters only when group defense preserves future options;
- continuity matters when restore can erase known threat patterns and defenses.

The boundary remains explicit:

> A predator is not selfhood. Threats become relevant to selfhood only when the agent must model its own vulnerability, trace, routines, tools, shelter, and social exposure as future-control variables.

Some selected policies carry extra channels whose ablations are neutral in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Threat dynamics are abstract control variables, not predator biology.
- Fear-like state is an affective control summary, not a subjective feeling claim.
- The selected planner is not an online RL agent discovering stealth, shelter, or group defense from scratch.
- This does not yet include resource ecology, territorial conflict, development, dependent care, or irreversible loss.

## Next Test

The next pressure-layer step should add resource ecology:

- food and water should regrow, spoil, migrate, or deplete slowly;
- restraint, caches, sharing, hoarding, territory, memory, and long-horizon planning should compete;
- ablations should separate resource memory, spoilage state, regeneration model, territory/ownership, sharing contracts, and continuity.

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_predator_threat_agents.html
```

The page replays the `social_warning_group_defense` trace with detection risk, fear-like state, injury, sound/scent traces, shelter security, social support, attacks, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_predator_threat_agents.py)
- [visualization](../visualizations/ssrm_3d_predator_threat_agents.html)
- [evaluation CSV](../artifacts/ssrm_3d_predator_threat_agents_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_predator_threat_agents_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_predator_threat_agents_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_predator_threat_agents_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_predator_threat_agents_trace.json)
- [JSON results](../artifacts/ssrm_3d_predator_threat_agents_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_predator_threat_agents_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_predator_threat_agents_results.js)
