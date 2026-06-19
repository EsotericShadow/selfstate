# SSRM-3D Game Build Handoff

## What the project is now

This repository now contains a browser-local artificial-life game foundation. The current research arc produced a maintained shell where residents can experience pressure, observe anomalies, form partial beliefs, propose tests, preserve failed experiments, stabilize emergent practices, post village concerns, negotiate project support, and carry consequences across return sessions.

This is not a finished game. It is the foundation for building one.

## Systems that exist

- Maintained browser shell at `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/`.
- Resident memory, schedules, obligations, debts, offscreen events, save/restore, replay, and audit surfaces.
- Hidden material-law anomaly layer with public-only resident observations.
- Resident-generated experiments, preserved failures, mutated social transmission, and cultural memory.
- Stochastic consequence and bounded recovery loops.
- Long-horizon belief lineage and civilization pressure integration.
- Emergent Practice Graph generated from repeated resident action, materials, failures, social transmission, and usefulness.
- Village Board with resident concerns and project proposals that the avatar can support but not command.
- Reality Constraint Ledger for material sources, time/work cost, tool wear, maintenance, conservation, and hidden-law/belief separation.
- Avatar hint divergence where households reinterpret questions, warnings, demonstrations, or materials differently.
- Hint branch return persistence with upkeep burden, reputation effects, recoverable forgetting, revival, and visible expression markers.

## First game build should include

- One village.
- Up to six named residents.
- A small walkable browser world using the maintained shell as the starting point.
- A normal player interface for entering, moving, asking, helping, waiting, supporting proposals, and inspecting public outcomes.
- One anomaly family with hidden laws and resident-visible observations.
- One or two emergent practice chains.
- One Village Board with resident-generated concerns and proposal cards.
- One recovery loop for stochastic or social disruption.
- One save/return loop that preserves branch history and source IDs.
- One audit/replay mode for inspecting hidden laws, source links, causal ledgers, and generated practice graphs.

## Deliberately out of scope

- No consciousness claim.
- No moral patienthood claim.
- No LLM dependency for resident behavior.
- No full physics engine.
- No region-scale civilization simulation.
- No combat, war, economy, or population-growth systems.
- No deterministic or pre-authored technology tree.
- No new research-report chain unless explicitly requested.
- No major new conceptual organs before a playable game build exists.

## How to start building the game

1. Treat the maintained shell as the prototype runtime, not as another report artifact.
2. Convert the current panels into a normal player-facing interface with one optional audit mode.
3. Keep the audit/replay layers intact so every consequence remains source-traced.
4. Pick one anomaly family and one practice chain for the first playable slice.
5. Use Village Board proposals as the player's main management surface.
6. Make save/restore and return-session persistence part of the first playable loop.
7. Only add mechanics that improve the first village prototype.

## Prototype branch

The first game-build branch is `game-prototype-v0`. It starts from the `research-arc-closed-v373` tag and adds a `Game Prototype v0` surface to the maintained shell. That surface is the intended starting point for the first playable loop: opening, practice/proposal, save-return proof, and public outcome summaries.

## Research arc closure rule

The current research/report arc is complete after the terminal closure report. Future work should be game/app implementation work unless the user explicitly requests another research report.
