# SSRM-3D Development/Skill Learning Report

## Question

Does changing competence create persistent control pressure without turning the simulation into growth roleplay?

Report 74 puts development/skill learning after structured perception, sleep/rest, illness/sanitation, weather/exposure, tool/shelter degradation, social trust/contracts, predator/threat agents, resource ecology, and injury/disability adaptation. This experiment asks whether skill memory, practice planning, capability self-state, fatigue management, injury adaptation, transfer modeling, teaching help, training tools, goal feasibility, and restore continuity become useful only when changing competence changes future action feasibility.

The tested claim is narrow:

> Skill machinery should be rejected in an easy fixed-skill control, but selected when practice, fatigue, injury, transfer, teaching, tools, feasibility, or restore-time forgetting changes what the agent can safely do.

This is not development simulation. It tests self-competence as delayed control pressure.

## Method

Canonical command:

```bash
python3 experiments/ssrm_3d_development_skill_learning.py --train-episodes 72 --eval-episodes 96 --seed 20260629 --candidate-count 7
```

The experiment uses return-selected candidate policies over abstract competence-control state. Policies can use:

| Channel | Role |
|---|---|
| skill memory | tracks learned competence and practice history |
| practice planning | trades immediate work for future competence |
| capability self-state | estimates current usable skill under fatigue or injury |
| fatigue management | rests or recalibrates when tired competence becomes unreliable |
| injury adaptation | retrains when injury changes the useful skill |
| transfer model | estimates whether old skill applies to the current task |
| teaching help | uses mentor/social instruction when it improves future competence |
| tool training | uses external aids that expand feasible action |
| goal feasibility | chooses goals that match current competence |
| continuity memory | preserves skill, practice, transfer, tool, teaching, and feasibility history after restore |

Evaluation conditions:

| Condition | Test |
|---|---|
| `full_control` | intact skill-learning control |
| `no_skill_memory` | removes learned competence memory |
| `no_practice_planning` | removes deliberate practice |
| `no_capability_state` | removes current self-competence estimate |
| `no_fatigue_management` | removes fatigue/rest calibration |
| `no_injury_adaptation` | removes retraining after injury |
| `no_transfer_model` | removes old-skill-to-new-task transfer estimate |
| `no_teaching_help` | removes social teaching |
| `no_tool_training` | removes training tools |
| `no_goal_feasibility` | removes competence-aware goal selection |
| `no_continuity` | removes restore-time skill continuity |
| `naive_fixed_skill_baseline` | acts as if skill is fixed |
| `omniscient_skill_control` | upper-bound skill control |

## Results

| Scenario | Selected policy | Skill loss | Practice loss | Capability loss | Fatigue loss | Injury loss | Transfer loss | Teaching loss | Tool loss | Feasibility loss | Continuity loss | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `easy_fixed_skill_control` | `naive_fixed_skill_baseline` | -0.157 | -0.081 | -0.191 | -0.133 | -0.210 | -0.223 | -0.232 | -0.057 | -0.261 | -0.076 | skill machinery rejected |
| `practice_curve_transfer` | `deliberate_transfer_planner` | 85.748 | 149.501 | 278.821 | -0.102 | -0.131 | 99.253 | 0.015 | 0.023 | 166.201 | -0.057 | practice/transfer pressure |
| `fatigue_skill_degradation` | `fatigue_calibration_planner` | 78.137 | 0.174 | 82.778 | 421.781 | 0.223 | 0.242 | 0.043 | 0.243 | 196.408 | 0.114 | fatigue calibration pressure |
| `injury_retraining_substitution` | `injury_retraining_planner` | 73.162 | 94.747 | 285.192 | -0.006 | 369.068 | -0.240 | -0.078 | 147.638 | 139.024 | -0.225 | injury retraining pressure |
| `teaching_tool_transfer` | `mentor_tool_transfer_planner` | 131.351 | 165.989 | 336.226 | -0.104 | 0.070 | 115.232 | 185.622 | 158.863 | 189.613 | 0.068 | teaching/tool transfer pressure |
| `restore_skill_continuity` | `continuity_skill_planner` | 56.484 | 56.345 | 242.629 | 277.208 | 71.307 | 44.549 | 56.761 | 75.517 | 109.369 | 83.001 | restore skill continuity pressure |

All six verdict rows pass `supports_development_skill_precursor=True`.

Key targeted losses:

- `easy_fixed_skill_control`: skill machinery is not selected and targeted ablations have near-zero effect.
- `practice_curve_transfer`: removing skill memory, practice planning, capability state, transfer modeling, goal feasibility, or the fixed-skill baseline causes large loss.
- `fatigue_skill_degradation`: removing skill memory, capability state, fatigue management, goal feasibility, or the fixed-skill baseline causes large loss.
- `injury_retraining_substitution`: removing skill memory, practice planning, capability state, injury adaptation, training tools, or goal feasibility causes large loss.
- `teaching_tool_transfer`: removing skill memory, practice planning, transfer modeling, teaching help, training tools, or goal feasibility causes large loss.
- `restore_skill_continuity`: removing continuity plus skill, practice, capability, fatigue, injury, transfer, teaching, tool, or feasibility state causes targeted loss.

## Interpretation

This result supports the tenth pressure-layer step at precursor level:

- skill machinery is not globally useful;
- practice matters when current effort changes future competence;
- capability self-state matters when nominal skill differs from usable skill;
- fatigue management matters when competence degrades through time;
- injury adaptation matters when prior skill no longer maps cleanly to action;
- transfer, teaching, and tools matter when competence can be carried, accelerated, or externalized;
- goal feasibility matters when overreach damages future options;
- continuity matters when restore can erase skill level, practice history, teaching, tools, transfer, or feasibility estimates.

The boundary remains explicit:

> Skill learning is not selfhood. It becomes relevant to selfhood only when the agent must model its own changing competence, practice history, fatigue-limited capability, injury-adapted skill, transfer, teaching, tools, goal feasibility, and restore-time skill history as future-control variables.

Some selected policies carry extra channels whose ablations are neutral in that row. Those are not positive evidence for those channels. The evidence comes only from targeted losses in matching regimes.

## Limits

- Candidate policies are supplied and return-selected.
- Skill dynamics are abstract control variables, not development simulation.
- Practice, teaching, transfer, and tool policies are designed channels.
- The selected planner is not an online RL agent discovering curriculum learning from scratch.
- This does not yet include irreversible loss.

## Next Test

The implemented follow-up adds dependent care without biological reproduction:

- fragile companions should create asymmetric capability and protection tradeoffs;
- teaching, repair, shelter, food/water, social trust, and promises should become useful only when another persistent agent depends on them;
- ablations should separate caregiving state, dependent identity memory, teaching, sacrifice/priority arbitration, social trust, and continuity.

Implemented by [report 85](85_ssrm_3d_dependent_care_report.md).

## Visualization

Serve the repo root and open:

```text
http://127.0.0.1:8765/visualizations/ssrm_3d_development_skill_learning.html
```

The page replays the `teaching_tool_transfer` trace with skill level, practice history, fatigue, injury, transfer confidence, teaching support, tool support, goal feasibility, actions, and ablation outcomes.

## Artifacts

- [experiment script](../experiments/ssrm_3d_development_skill_learning.py)
- [visualization](../visualizations/ssrm_3d_development_skill_learning.html)
- [evaluation CSV](../artifacts/ssrm_3d_development_skill_learning_eval.csv)
- [policy-selection CSV](../artifacts/ssrm_3d_development_skill_learning_policy_selection.csv)
- [summary CSV](../artifacts/ssrm_3d_development_skill_learning_summary.csv)
- [verdict CSV](../artifacts/ssrm_3d_development_skill_learning_verdict.csv)
- [trace JSON](../artifacts/ssrm_3d_development_skill_learning_trace.json)
- [JSON results](../artifacts/ssrm_3d_development_skill_learning_results.json)
- [trace JS fallback](../artifacts/ssrm_3d_development_skill_learning_trace.js)
- [results JS fallback](../artifacts/ssrm_3d_development_skill_learning_results.js)
