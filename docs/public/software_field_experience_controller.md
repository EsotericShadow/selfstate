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

## Report 222 Local Agent Conversation Memory Loop Bridge Note

Report 222 adds a playable local state loop with conversation memory updates, object interaction consequences, bounded refusal, save/restore, export/import, frequency/flower rhythm, and a browser artifact: across `4` agents, `5` objects, `4` conversation actions, `5` object consequences, `13` memory updates, `4` save/restore snapshots, and `19` transitions, respectful or intrusive choices change trust, boundary pressure, memories, object locations, and material debt. Readiness is `0.980000`; allowed object consequence quality is `0.666667` because even respectful blanket use can create follow-up material debt, so interaction is not cost-free. This is deterministic local stateful interaction substrate, not LLM dialogue, autonomous agents, consent, suffering, or consciousness. The next gate is a playable local 3D social memory loop with autonomous agent ticks, need-driven approach/avoidance, object planning, and cross-session relationship continuity.

## Report 223 Local Social Memory Autonomous Tick Bridge Note

Report 223 adds a playable local social memory loop with autonomous ticks, need-driven approach/avoidance, object planning, cross-session relationship continuity, frequency/flower rhythm, and browser play: across `4` agents, `24` need appraisals, `24` approach/avoidance decisions, `4` object plans, `4` relationship continuity records, `4` cross-session snapshots, and `24` autonomous ticks, agents move and write memories between player actions. Readiness is `0.919167`; object plan completion is only `0.500000`, object plan progress is `0.750000`, cross-session relationship continuity is `0.750000`, and approach/avoidance coherence is `0.958333`, so the loop has autonomous behavior but not solved planning. This is deterministic local autonomous-tick substrate, not real consciousness, consent, suffering, or general-purpose reasoning. The next gate is playable local 3D autonomous social ecology with multi-agent interaction, shared object negotiation, social contagion, and durable relationship histories.

## Report 224 Local Autonomous Social Ecology Bridge Note

Report 224 adds a playable local autonomous social ecology with multi-agent interaction, shared object negotiation, bounded social contagion, durable relationship histories, frequency/flower rhythm, and browser play: across `5` agents, `8` interactions, `4` negotiations, `5` contagion events, `5` relationship histories, and `17` multi-agent ticks, agents negotiate scarce objects, respect partial refusals, write relationship memory, and express later visible behavior from durable social history. Readiness is `0.843630`; multi-agent interaction coverage is only `0.700000`, shared object resolution is `0.750000`, social contagion containment is `0.800000`, durable relationship history integrity is `0.800000`, and weakest channel is `0.529412`, so the ecology is social and replayable but not a full society simulator. This is deterministic local social-ecology substrate, not real consciousness, consent, suffering, moral patienthood, or open-ended social cognition. The next gate is a playable local 3D autonomous society slice with agent-agent dialogue, cooperative tasks, conflict repair, group routines, and richer body-language animation.

## Report 225 Local Autonomous Society Slice Bridge Note

Report 225 adds a playable local autonomous society slice with agent-agent dialogue, cooperative tasks, conflict repair, group routines, readable body-language markers, frequency/flower rhythm, and browser replay: across `5` agents, `12` dialogue turns, `5` cooperative tasks, `4` conflict repairs, `4` group routines, `15` body-language frames, and `25` society ticks, agents ask before touching learner objects, accept correction, protect private ledger wording, slow work during weather hurry, and carry unresolved shade-frame debt forward. Readiness is `0.857238`; dialogue coverage is only `0.600000`, conflict repair completion is `0.750000`, body-language readability is `0.725333`, and weakest channel is `0.600000`, so this is a playable society slice rather than a solved society simulator. This is deterministic local society-slice substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, or open-ended social cognition. The next gate is a playable local 3D society with avatar-entered cooperative participation, object manipulation, dialogue choice, routine disruption, and consequences across saved days.

## Report 226 Local Avatar Participation Consequence Bridge Note

Report 226 adds playable avatar participation inside the local society slice with cooperative task joining, object manipulation, bounded dialogue choices, routine disruption, repair offers, sensory feedback, saved-day consequences, frequency/flower rhythm, and browser save/restore: across `5` agents, `12` avatar actions, `6` object manipulations, `5` dialogue choices, `3` routine disruptions, `6` saved-day consequences, and `18` avatar play ticks, avatar choices change trust, object state, access, debt, and later public memory. Readiness is `0.932300`; object permission enforcement is only `0.666667`, routine disruption recovery is `0.793333`, cooperative participation completion is `0.833333`, cross-day relationship persistence is `0.816667`, and weakest channel is `0.666667`, so avatar action consequences exist but object permissions and routine recovery are not solved. This is deterministic avatar-participation substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, or open-ended social cognition. The next gate is playable local 3D multi-day avatar life with free-move task participation, richer object affordances, agent-initiated requests, and persistent reputation UI.

## Report 227 Local Multi-Day Free-Move Avatar Life Bridge Note

Report 227 adds playable local multi-day free-move avatar life with deterministic movement frames, collision/boundary states, richer object affordances, cooperative task participation, agent-initiated requests, public reputation UI, saved snapshots, sensory/body feedback, frequency/flower rhythm, and browser save/restore: across `5` agents, `12` movement frames, `8` object records, `6` task participations, `8` agent requests, `6` reputation events, `4` saved snapshots, and `36` life ticks, the avatar moves through the local world while agents request help and reputation changes access. Readiness is `0.929458`; object affordance depth is only `0.604167`, cross-day reputation persistence is `0.631667`, task participation completion is `0.813333`, and weakest channel is `0.604167`, so the world is more playable but still lacks a deep compositional affordance lattice. This is deterministic multi-day avatar-life substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, open-ended cognition, full physics, or complete gameplay. The next gate is a playable local 3D continuous life loop with real-time free movement, agent-initiated interruptions, a deeper affordance lattice, and multi-day autonomous background ticks.

## Report 228 Local Continuous Life Loop Bridge Note

Report 228 adds a playable local continuous life loop with realtime-ish movement frames, collision/social-boundary checks, agent-initiated interruptions, a deeper object affordance lattice, autonomous background ticks, merged continuous life ticks, sensory/body feedback, frequency/flower rhythm, and browser save/restore: across `5` agents, `48` movement frames, `59` affordance rules, `10` interruptions, `24` background ticks, and `90` merged ticks, the avatar moves while agents interrupt and the world continues ticking around them. Readiness is `0.998395`; interrupt delivery is `0.900000`, affordance lattice depth is `0.842857`, background consequence binding is `0.916667`, idle tick independence is `0.958333`, and weakest channel is `0.842857`, so integration is strong but still deterministic and hand-authored. This is continuous-life-loop substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, open-ended cognition, full physics, or complete gameplay. The next gate is playable local 3D continuous life with compositional object transformations, autonomous agent schedules, richer body-state dynamics, and typed dialogue inside the realtime loop.

## Report 229 Local Realtime Body Dialogue Transform Bridge Note

Report 229 adds playable local realtime body/dialogue integration with compositional object transformations, autonomous schedules, richer body-state dynamics, typed dialogue routing, waste/byproduct accounting, privacy gates, frequency/flower rhythm, and browser save/restore: across `5` agents, `10` transformations, `100` schedules, `20` body ticks, `8` typed turns, and `63` integration ticks, objects transform, schedules advance, body state changes visible behavior, and typed inputs route to bounded replies. Readiness is `0.987400`; transformation reversibility balance is only `0.700000`, schedule autonomy is `0.990000`, and weakest channel is `0.700000`, so integration is strong but object undo/repair semantics remain incomplete. This is deterministic realtime body/dialogue/material substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, open-ended cognition, full physics, arbitrary crafting, or complete gameplay. The next gate is typed multi-turn dialogue, compositional crafting chains, schedule conflicts, richer body recovery, and persistent personal projects.

## Report 230 Local Project Loop Bridge Note

Report 230 adds playable local project-loop continuity with typed multi-turn dialogue threads, compositional crafting chains, schedule conflicts, richer body recovery, persistent personal projects, frequency/flower rhythm, browser save/restore, and merged project-loop ticks: across `5` agents, `12` dialogue turns, `12` crafting steps, `5` schedule conflicts, `6` recoveries, `5` projects, and `40` loop ticks, agents carry projects forward through conversation, material dependencies, conflict, recovery, blockers, and next actions. Readiness is `0.944900`; schedule conflict recovery is `0.800000`, crafting quality is `0.805000`, fairness is `0.812000`, and weakest channel is `0.800000`, so project continuity exists but conflicts still leave real delay and debt. This is deterministic project-loop substrate, not real consciousness, consent, suffering, moral patienthood, LLM dialogue, open-ended cognition, full physics, arbitrary crafting, or complete gameplay. The next gate is longer personal project arcs, learned preference updates, richer multi-turn typed dialogue, and craft/economy consequences across many days.

## Report 231 Local Long Arc Preference/Economy Bridge Note

Report 231 extends the playable local SSRM-3D agent bridge from short project loops to many-day personal arcs with bounded learned preferences, richer multi-turn dialogue continuity, craft/economy consequences, persistent economy ledgers, body-recovery carryover, and phase/rhythm scaffolding. The result passes with readiness 0.930870 and weakest-channel score 0.818667, while keeping the boundary explicit: deterministic scaffold only, not subjective consciousness or open-ended language. The next controller target is first-person ego/interior state with self-boundary, ownership, bounded refusal, self-story, and recoverable ego repair.

## Report 232 First-Person Ego State Bridge Note

Report 232 adds the first explicit functional ego layer to the playable SSRM-3D stack: self-boundary, ownership, self/other attribution, private workspace frames, bounded refusal, self-story updates, visible expression, and recoverable ego wound/repair. The deterministic run passes with readiness 0.983242 and weakest-channel score 0.911667. The controller boundary remains strict: this is inspectable ego scaffolding, not subjective consciousness, legal consent, moral patienthood, or open-ended language. The next target is a many-day first-person interior loop with ownership generalization, relationship-specific attachment, and richer readable body language.

## Report 233 Many-Day Ego Continuity Bridge Note

Report 233 extends the first-person ego bridge across days 1, 3, 5, 8, 13, 21, 34, and 55. It adds ownership generalization, false mine-claim rejection, relationship-specific attachment, repeated wound/repair cycles, forgiveness without amnesia, private interior continuity, self-story consolidation, richer body-language expression, and boundary dialogue. The deterministic run passes with readiness 0.982171 and weakest-channel score 0.901333. The first full run failed on body-language richness, correctly forcing more varied visible ego states before publication. The next controller target is a playable first-person society loop with multi-agent markets, household rituals, proto-language tokens, and thousands-year pre-avatar civilization scaffolding.

## Report 234 Pre-Avatar Society Epoch Bridge Note

Report 234 starts the thousands-year pre-avatar civilization scaffold. It compresses years 0, 1, 8, 55, 377, 987, 1597, 2584, and 4181 into deterministic society epochs with five households, markets, rituals, proto-language tokens, technology lineages, cultural norms, sensory ecology, and avatar-entry gates. The run passes with readiness 0.974744 and weakest-channel score 0.812000. The first run failed on technology lineage depth, which exposed a bad maturity metric; the final version measures lineage continuity and primitive-to-mature improvement. The next controller target is a local playable pre-avatar civilization sandbox with generational agents, proto-language mutation, household markets, ritual schedules, and final avatar-entry ceremony after mature thresholds.

