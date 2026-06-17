# The Commercial Path: Software Field-Experience Controllers

The most direct money path is software development.

Not because the system can write code snippets. Frontier coding agents can already do that.

The valuable thing would be:

> A field-experienced software engineering controller that makes an LLM better at real repo work than the LLM alone.

That means better at:

- finding the real cause;
- editing the right files;
- choosing the right tests;
- avoiding regressions;
- surviving code review;
- not wasting time on the wrong repair.

## Why Software Fits This Project

Software has a clean consequence loop:

```text
issue -> repo state -> patch -> build -> tests -> review -> deploy -> regressions
```

That makes it perfect for the same idea behind Report 99.

In Report 99, the agent had to choose the right social repair. A wrong repair consumed time and made other failures worse.

In software, the same pattern is:

```text
Several plausible fixes exist. Only one addresses the true cause.
Wrong fixes pass shallow tests, waste CI, create regressions, or fail review.
```

This is the most direct commercial version of the broader [simulation-distilled reasoning controller](sim_distilled_reasoning_controller.md) direction.

## The Product Shape

The LLM should remain the code generator and repo tool user.

The field-experience controller should sit around it:

```text
issue / failing test / PR diff
  -> LLM proposes candidate plans and patches
  -> software controller scores root cause, risk, tests, and review fit
  -> LLM edits and runs tools
  -> controller reviews before PR
```

Think of the controller as a senior engineer/reviewer layer trained from consequence-rich coding episodes.

## What It Would Score

| Critic | What it catches |
|---|---|
| Root-cause critic | The likely real cause, not only the visible symptom. |
| Patch-risk critic | Hidden regressions, API breaks, security risks, over-refactors. |
| Test-strategy planner | Which tests to run first and which missing tests to add. |
| Code-review critic | Whether the patch would survive maintainer review. |
| Regression-cascade model | What other behavior may break after this fix. |
| Repo-convention model | Local style, invariants, risky files, and patterns. |

## The First Product

Start with a patch critic / PR reviewer.

It reads:

- issue text;
- repo state;
- branch diff;
- test output;
- CI logs;
- review comments.

It returns:

- likely root cause;
- likely hidden regression;
- missing tests;
- risky files;
- overfit-to-test warning;
- API/security/style risks;
- recommended next test or edit.

That is easier to prove and safer than a fully autonomous coding agent.

## The Money Claim

The product is not valuable because it can type code. Coding agents already do that.

The product is valuable if it makes the same coding agent behave more like a careful senior engineer:

- find the actual cause before patching;
- avoid fixes that only satisfy the visible test;
- choose the next test instead of wasting a full CI run;
- spot hidden regressions before review;
- keep the patch small enough to merge;
- avoid changes that create security, migration, or API risk.

So the test is simple:

```text
coding agent alone
vs.
coding agent plus field-experience controller
```

If the wrapped agent ships more accepted patches with fewer regressions, lower review time, and lower cost, the controller is commercially useful.

## What Is Not Proven Yet

The current simulator does not yet prove that field-experience critics work. Reports 111 and 112 are the caution. A critic can be trained from cloned rollouts, or a diagnostic head can reach `0.991` offline label accuracy, and validation can still reject it because it does not improve held-out consequences.

Report 113 adds one useful positive lesson: a controller can improve when it keeps multiple consequence channels active at the same time. In the simulation, separate environmental and social action heads need joint arbitration. In software, a root-cause critic would need the same kind of balance across tests, regression risk, API compatibility, review fit, and time cost.

Report 116 adds the caution for product work: a value selector can win on the tune set and still transfer worse than a simple seed/fixed allocator. For software, that means a reviewer that looks good on a small validation set is not enough. It has to improve hidden tests, regressions, review outcomes, and cost on held-out repositories.

For software, the controller has to prove itself on real outcomes: better patches, fewer regressions, stronger hidden-test performance, less review time, and lower debugging cost.

Report 139 adds the first structured bridge toward this product path. It is a toy WrongFix Arena with `15` software-repair tasks represented as structured data, not executable repositories. The result is positive but bounded: `visible_test_only` passes visible tests while getting hidden pass rate `0.067` and wrong-fix rate `1.000`; `min_channel_critic` gets hidden pass rate `1.000`, wrong-fix rate `0.000`, root-cause repair rate `1.000`, and weakest-channel score `0.864`.

Report 141 adds a seeded dynamic extension to `120` generated tasks plus 5 deterministic false-positive calibration tasks with held-out families, noisy and irrelevant signals, difficulty tiers, and explicit ambiguity across correctness channels. It shows why visible tests alone fail under realistic uncertainty while multi-channel critics can do better, but this remains a benchmark bridge: no executable repositories, no external repos, and no claim of frontier coding-agent improvement.

That supports the benchmark shape:

```text
do not trust a green visible test if another required correctness channel is weaker
```

It does not yet prove that a field-experience controller improves an LLM on real repo work.

## What Would Prove Value

The proof is a head-to-head:

```text
frontier coding agent alone
vs.
same frontier coding agent + field-experience controller
```

Measure:

- hidden-test pass rate;
- regression rate;
- PR acceptance rate;
- reviewer minutes saved;
- time to valid patch;
- CI minutes consumed;
- token cost;
- patch size;
- security findings introduced;
- rollback or follow-up bug rate.

The product is valuable if it produces:

> more accepted patches, fewer regressions, less review time, less CI waste, and lower token cost.

## Why This Is Different From A Better Prompt

A prompt can remind an LLM to be careful.

A field-experience controller would be trained across many executable coding episodes where wrong choices had consequences:

- wrong file edited;
- shallow tests passed but hidden tests failed;
- patch fixed symptom but not invariant;
- refactor caused review rejection;
- dependency change broke another path;
- migration patch risked data loss.

The controller learns from the repair history, not just from text about software.

## One-Sentence Version

Build a software engineering controller trained from consequence-rich repo episodes, then use it to make frontier LLM coding agents better at root-cause repair, test strategy, regression avoidance, and code review.

## Report 216 Public-Health Governance Bridge Note

Report 216 adds playable public-health governance with outbreak signals, quarantine or spacing consent, appeals, privacy/stigma guardrails, care access under restriction, trust recovery, frequency/flower rhythm, and browser replay: across `8` outbreak signals, `3` policies, `8` consent records, `4` appeals, `5` trust-recovery records, and `28` events, agents handle false positives, irrelevant failing signals, conditional consent, refusal without punishment, deferred privacy appeals, anonymized evidence, rollback rules, and partial social repair with readiness `0.888849`. Signal detection is only `0.600000`, appeal resolution is `0.750000`, containment traceability is `0.678571`, and trust recovery is `0.734200`, so the bridge is deliberately messy. This is deterministic public-health-governance substrate, not real medicine, epidemiology, public-health authority, consent, suffering, or consciousness. The next gate is playable community-scale crisis governance with resource triage, rumor dynamics, restorative appeals, and long-term trust memory.

## Report 217 Community Crisis Governance Bridge Note

Report 217 adds playable community crisis governance with scarce resource ledgers, triage decisions, rumor dynamics, restorative appeals, long-term trust memory, frequency/flower rhythm, and browser replay: across `5` resources, `3` crisis policies, `8` triage decisions, `5` rumors, `5` restorative appeals, `5` trust memories, and `31` events, agents allocate blankets, cups, tools, water, and medicine while rumor, stigma, and social debt remain visible. Readiness is `0.856399`; resource triage fairness is `0.682851`, care continuity is `0.750000`, appealable debt traceability is `0.500000`, rumor correction is `0.800000`, restorative appeal resolution is `0.800000`, and trust repair is `0.725968`, so crisis governance is explicitly unfinished. This is deterministic community-crisis-governance substrate, not real crisis management, medicine, public-health authority, consent, suffering, or consciousness. The next gate is playable multi-generational culture memory with language drift, inherited rituals, institutions, and avatar-entry after deep simulated history.

## Report 218 Multi-Generational Culture Avatar-Entry Bridge Note

Report 218 adds playable multi-generational culture memory with language drift, inherited rituals, institutions, technology lineages, living-agent inheritance, an avatar-entry gate, frequency/flower rhythm, and browser replay: across `4980` simulated pre-avatar years, `10` epoch strata, `10` language layers, `6` rituals, `6` institutions, `6` technology lineages, `5` living-agent inheritance records, and `44` events, the avatar can enter only after a public deep-history briefing while private workspaces remain sealed. Readiness is `0.933020`; language drift continuity is `0.891500`, mutual intelligibility floor is `0.560000`, ritual inheritance is `0.878333`, institution persistence is `0.884167`, and agent identity continuity is `0.856000`, so the world now has traceable depth but not autonomous civilization. This is deterministic deep-history and avatar-gating substrate, not real anthropology, language emergence, consent, suffering, or consciousness. The next gate is a playable pre-avatar civilization simulator with autonomous generations, child-to-adult learning, cultural mutation, institution competition, and late avatar entry.

## Report 219 Pre-Avatar Civilization Simulator Bridge Note

Report 219 adds playable pre-avatar civilization dynamics with autonomous generation cohorts, child-to-adult learning, cultural mutation, institution competition, demographic events, late avatar entry, frequency/flower rhythm, and browser replay: across `3698` simulated pre-avatar years, `24` cohorts, `12` learning episodes, `12` cultural mutations, `8` institution contests, `9` demographic events, and `66` events, generations learn, choose, mutate, contest, and remember before the avatar enters. Readiness is `0.911072`; child learning is `0.833333`, skill transfer is `0.750000`, mutation survival is `0.888889`, institution resolution is `0.875000`, institution legitimacy after competition is `0.730225`, demographic traceability is `0.888889`, and living-world continuity is `0.782387`, so the bridge is active but still deterministic cohort simulation. This is not open-ended civilization, real anthropology, language emergence, consent, suffering, or consciousness. The next gate is playable embodied pre-avatar ecology with births, aging, illness, apprenticeship, habitat construction, agriculture, weather, and material economies before avatar entry.

## Report 220 Embodied Pre-Avatar Ecology Bridge Note

Report 220 adds embodied pre-avatar ecology with life-stage body records, functional body costs, illness and care, apprenticeships, habitat construction, agriculture, weather sensory fields, material exchanges, late avatar entry, frequency/flower rhythm, and browser replay: across `2758` simulated pre-avatar years, `18` life-stage records, `8` illness/care records, `6` apprenticeships, `6` habitat projects, `8` agriculture cycles, `9` weather cycles, `8` material exchanges, and `64` events, bodies carry energy, fatigue, hunger, cold, wetness, pain, private workspace digests, storm sounds, crop smells, material debts, and shelter maintenance pressure before avatar entry. Readiness is `0.855896`; habitat-weather adaptation is only `0.347500`, food storage security is `0.617125`, illness recovery is `0.750000`, agriculture stability is `0.750000`, and material fairness after debt is `0.734812`, so the ecology is materially fragile. This is deterministic embodied-ecology substrate, not real biology, ecology, agriculture, consent, suffering, or consciousness. The next gate is a playable local 3D ecology scene with spatialized bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, and avatar conversation entry.

## Report 221 Playable Local 3D Ecology Scene Bridge Note

Report 221 adds a standalone playable local ecology scene with keyboard avatar movement, spatialized bodies, sensory fields, weather volumes, crop plots, habitat interiors, material objects, proximity conversation, respect/intrude choices, frequency/flower rhythm, and browser replay: across `6` spatial bodies, `6` sensory fields, `4` weather volumes, `4` crop plots, `4` habitat interiors, `7` material objects, `6` conversation nodes, and `7` replay frames, the avatar can approach agents and trigger boundary-aware dialogue while private workspaces stay sealed. Readiness is `0.961905`; material object pickup rate is only `0.428571` because owned, child-work, medicine, repair, and sealed threshold objects cannot be freely taken, and spatialized dialogue context is `0.857143`. This is deterministic local playable scene substrate, not a full 3D engine, LLM dialogue, consent, suffering, or consciousness. The next gate is a playable local 3D agent conversation loop with memory updates, object interaction consequences, bounded refusal, and save/restore state.
