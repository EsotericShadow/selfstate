# Repository Weakness Audit

## Purpose

This audit records the strongest current objections to the research stack. It is not a failure note. It is a control surface for preventing the repo from turning bridge results into stronger claims than the evidence supports.

## Findings

### Report 69 Is A Designed Packet Bridge

[Report 69](69_ssrm_3d_learned_integration_controller_report.md) should not be treated as strong learned integration.

The experiment trains a recurrent controller on short compressed packet traces, but scenario identity and separated feature groups are still supplied by the task design. The result is better described as:

> A learned controller can use designed packet channels when the task is structured to make those channels useful.

That still matters because it moves part of tool, social, and continuity pressure into learned policy state. It does not show autonomous discovery of the cross-gate abstraction.

An initial full-manifest run exposed instability because model initialization was not seeded. After seeding model weights, the canonical rows pass repeatably. That repair does not upgrade the claim: the result remains a designed packet bridge because scenario identity and feature-group boundaries are supplied.

### The Attractor Claim Is Not Stable

The architecture boundary stress test remains negative evidence against an architecture-independent attractor. Only one of three tested recurrent architectures converges in all shared regimes.

This means the repo cannot yet claim:

- architecture-independent convergence;
- seed-stable convergence;
- general learned selfhood;
- a law of adaptive systems.

The current best phrasing is narrower:

> Under some pressure regimes and some learners, recurrent policy state can recover agent-bounded variables that pass causal boundary tests.

### Actor-Critic Evidence Is Strong But Single-Run

[Report 59](59_architecture_torch_actor_critic_report.md) is the strongest current learned-controller result because `RNN`, `GRU`, and `LSTM` actor-critics recover the boundary signatures in the canonical MPS run.

But it remains one tuned canonical run on a compact toy benchmark. It needs seed sweeps, budget sweeps, and richer surfaces before it can support an attractor claim.

### SSRM-3D Gates Are Partial

[The done-enough gates](63_ssrm_3d_done_enough_gates.md) are still partial:

- learned control exists, but direct self-edit action effects remain weak;
- tool-making is return-selected from candidate affordance policies;
- social pressure is return-selected from candidate social policies and role agents;
- continuity uses explicit records;
- attention, LLM stream, continuity memory, and tool-building access are not yet independently ablated inside the full embodied learned-controller setting.

The right status is:

> SSRM-3D has useful precursors. It has not passed the four gates.

### Learned Discovery Is The Frontier

The live weakness is the gap between:

- selected policies from designed candidates;
- learned behavior from designed packets;
- autonomous discovery of the abstraction under pressure.

The repo should stop treating return-selected candidate behavior as close to invention. Candidate-policy wins are good pressure tests. They are not discovery.

## Near-Term Attack On Report 69

The next experiment should keep the same broad learned-integration idea but remove the obvious shortcuts:

- remove scenario identity leakage from packet rows;
- randomize pressure combinations instead of using one scenario per pressure;
- run multiple seeds;
- require margins that are not sitting near the threshold;
- report bridge support separately from strong integration support;
- allow the strong result to fail without making the experiment process fail.

Success would strengthen the integration claim.

Failure would correctly downgrade Report 69 to a designed packet precursor.

Both outcomes are useful.
