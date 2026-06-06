# Software Field-Experience Controller Plan

## Purpose

This document records the most direct commercial path for the simulation-distilled controller idea:

```text
train consequence-aware software engineering controllers that make frontier LLM coding agents better at real repo work
```

The claim is not that the system should merely write code. Frontier LLM coding agents already write code, inspect repos, run tools, and iterate on tests. The valuable claim would be:

```text
A field-experienced software engineering controller improves a frontier LLM's root-cause localization, patch choice, test strategy, review quality, and regression avoidance.
```

## Why Software Is The Direct Money Path

Software has a clean feedback loop:

```text
issue -> repo state -> hypothesis -> patch -> build -> tests -> review -> deploy -> regressions
```

That makes it a strong domain for the project's core idea: wrong repairs are costly.

The software version of Report 99 is:

```text
Several plausible code fixes exist. Only one addresses the true cause. Wrong fixes consume time, pass shallow tests, introduce regressions, or make later failures harder to diagnose.
```

## Architecture

The controller should sit around the LLM, not replace it.

```text
issue / failing test / PR diff
  -> frontier LLM proposes candidate plans and patches
  -> software field-experience controller scores the candidates
  -> LLM edits, tests, debugs, and revises
  -> controller reviews before PR
```

The LLM remains the generator and repo tool user. The controller acts like a senior engineer, reviewer, release manager, and regression-risk critic.

## What The Controller Scores

| Critic | Question |
|---|---|
| Root-cause/localization critic | Which file, function, invariant, dependency, or caller contract probably caused the issue? |
| Patch-risk critic | Is this patch likely to regress behavior, break API compatibility, create security risk, or overfit visible tests? |
| Test-strategy planner | Which tests should run first, which tests should be added, and when is the full suite worth the cost? |
| Code-review critic | Does the patch actually satisfy the issue intent and repo conventions? |
| Regression-cascade model | What other failures might this fix trigger? |
| Repo-memory/convention model | Which local patterns, invariants, abstractions, and maintainer preferences matter? |
| Time/CI/token cost model | Is this debugging path worth its runtime cost? |

## Field Experience

For software, field experience means training across executable episodes:

```text
bug report
  -> inspect repo
  -> form hypothesis
  -> edit code
  -> run targeted tests
  -> hit failure
  -> debug
  -> revise
  -> pass visible tests
  -> hit hidden tests or review feedback
  -> fix style/API/security/regression issue
  -> merge or fail
```

The useful signal is not only the final successful patch. The useful signal is the memory of wrong repairs:

- patching a symptom instead of the invariant;
- adding a special case before checking the caller contract;
- running the full suite before localizing the bug;
- refactoring while fixing a production issue without reducing risk;
- trusting green tests that do not cover changed behavior;
- changing a public API without searching downstream call sites;
- silencing an error without understanding who depends on it;
- satisfying the issue text while violating repo style.

## Code Version Of Report 99

A first benchmark should be:

```text
Costly Code Repair Under Cascading Regression Pressure
```

Each task has:

- a real or synthetic repo issue;
- multiple plausible repairs;
- shallow tests that some wrong repairs can pass;
- hidden tests or review checks that expose causal mismatch;
- regression or technical-debt cost for wrong fixes;
- explicit time/CI/token cost.

Examples:

| Scenario | Wrong repair | Cascade |
|---|---|---|
| API bug | Add local special case | Breaks downstream callers. |
| Flaky test | Increase timeout | Hides race condition. |
| Memory leak | Clear cache aggressively | Performance collapses. |
| Auth bug | Loosen validation | Security regression. |
| Migration failure | Patch one schema path | Breaks rollback or old data. |
| Frontend state bug | Change visible component only | State model remains broken. |
| Build failure | Pin old dependency | Future security update blocked. |
| Type error | Suppress type check | Later runtime bug. |
| Test failure | Update test to match bug | False green CI. |
| Performance issue | Add caching | Stale data bug. |

## Product Sequence

Start with a reviewer, not a fully autonomous coder.

### Product 1: Patch Critic / PR Reviewer

Inputs:

- issue text;
- repo state;
- branch diff;
- CI logs;
- test output;
- review comments.

Outputs:

- likely root cause;
- likely hidden regression;
- missing tests;
- risky files;
- overfit-to-test warning;
- API/security/style risks;
- recommended next test or edit.

This is safer, easier to measure, and easier to sell than a fully autonomous coding agent.

### Product 2: Field-Experienced Coding Agent

After the reviewer works:

1. triage issue;
2. localize cause;
3. plan patch;
4. ask the LLM to implement;
5. run targeted tests;
6. debug;
7. add regression tests;
8. run broader suite;
9. review patch;
10. open PR;
11. respond to review;
12. learn from the outcome.

## Evaluation

The proof has to be head-to-head:

```text
frontier LLM coding agent alone
vs.
same frontier LLM + field-experience controller
```

Measure:

| Metric | Why it matters |
|---|---|
| Hidden-test pass rate | Did it really fix the issue? |
| Regression rate | Did it break something else? |
| PR acceptance rate | Would maintainers accept it? |
| Reviewer minutes saved | Direct enterprise value. |
| Time to valid patch | Developer productivity. |
| CI minutes consumed | Infrastructure cost. |
| Token cost | Operating margin. |
| Patch size | Maintainability. |
| Security findings introduced | Enterprise risk. |
| Rollback or follow-up bug rate | Real deployment quality. |

The killer metric is:

```text
higher valid-patch rate with fewer regressions, less review time, less CI waste, and lower token cost
```

## Benchmark Requirements

Static public benchmarks are not enough.

The benchmark should be:

- live or regularly refreshed;
- private where needed;
- executable;
- multi-language;
- hidden-test backed;
- review-aware;
- regression-aware;
- contamination-resistant;
- cost-aware;
- able to distinguish shallow pass from true causal repair.

Public benchmarks can be useful calibration, but the commercial proof is private/live repo work.

## Data Pipeline

Training data should include:

- issue text;
- repo snapshots;
- diffs;
- commands run;
- test output;
- CI output;
- review feedback;
- accepted/rejected PR status;
- hidden-test outcomes;
- rollback or follow-up bug signals;
- counterfactual failed patches where possible.

The key training target is not "write code." It is:

```text
choose the right repair path under uncertainty and prove it without wasting time
```

## Safety And Scope

Start bounded:

- reviewer mode;
- patch-risk scoring;
- test-strategy advice;
- no automatic production deploy;
- no automatic destructive migration;
- no security-sensitive change without human review.

The field-experience controller should advise and rank. The LLM can propose patches. Human or policy gates still control high-risk actions.

## Commercial Pitch

Current coding agents are language-trained and tool-using. This plan adds synthetic field experience:

```text
agents trained across executable repositories where wrong fixes consume time, pass shallow tests, trigger regressions, and fail review
```

The result is a software engineering controller that improves LLM coding by learning root-cause repair, regression avoidance, test strategy, and repo-specific judgment from consequences rather than text alone.

## One-Sentence Direction

Build a field-experienced software engineering controller that makes frontier LLM coding agents better at finding the real cause, editing the right files, choosing the right tests, avoiding regressions, and shipping patches that survive review.
