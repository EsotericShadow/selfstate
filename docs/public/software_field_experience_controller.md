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

## What Is Not Proven Yet

The current simulator does not yet prove that field-experience critics work. Report 111 is the caution: even cloned simulator rollouts can train a critic that validation rejects because it does not improve held-out consequences.

For software, the controller has to prove itself on real outcomes: better patches, fewer regressions, stronger hidden-test performance, less review time, and lower debugging cost.

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
