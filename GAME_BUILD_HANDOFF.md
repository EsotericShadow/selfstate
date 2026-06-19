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

## Prototype v0 deep-time update

`game-prototype-v0` now includes a compressed deep-time civilization surface in the maintained shell. The controls `Deep-time epoch` and `Million-year sim` advance practice lineages through stochastic pressures such as drought, wet storage decay, route drift, material exhaustion, memory compression, floods, tool wear, and abundance intervals.

This is a game prototype mechanic, not a new research report. It lets effects emerge without a scripted tech tree by mutating local practice lineages from pressure, entropy, material drift, memory strength, usefulness, maintenance burden, forgetting, and adaptation. The active village remains small; deep time is represented as lineage history rather than a full population or region simulator.

## Prototype v0 deep-time village feedback update

Deep-time epochs now feed back into ordinary village play. Each emergent effect can change a resident schedule and memory, create a Village Board concern/proposal, and write a Reality Constraint Ledger row. The player-facing `Apply effect` control is guarded against duplicating the same effect if an epoch already applied it.

## Prototype v0 survivability update

Deep time now tracks civilization survivability, not just effects. The prototype records a survival ledger with continuity score, active lineages, trace lineages, resource total, average memory, burden, recovery potential, and whether the culture remains million-year capable. The `Ten-million-year sim` control runs compressed long-horizon evolution until ten million years or collapse into trace memory.

## Prototype v0 autonomous resident update

Residents now have an autonomous stochastic tick loop. `Resident tick` advances one resident action from runtime entropy; `Resident season` runs repeated autonomous actions and periodically advances deep time. Residents can rest, refuse, repair safety, forage, work on proposals, maintain practices, teach, experiment, or observe based on needs, resources, proposals, practices, and stochastic pressure. These actions update schedules, memories, resources, proposal support, care ledgers, and Reality Constraint Ledger rows without direct player command.

## Prototype v0 QA smoke update

The maintained shell now includes a player-facing `Prototype QA` control. It executes the current playable loop, autonomous resident season, million-year deep-time run, survival audit, causal audit, and save/restore preservation check, then writes a visible `gamePrototypeQA` receipt. This is not production certification; it is an in-shell hardening gate for the playable prototype branch.

## Prototype v0 auto-simulation update

The prototype now includes a browser-local auto-simulation clock. `Start auto sim` advances resident ticks on a timer; `Pause auto sim` stops it; `Auto burst` runs twenty inspected steps. The cadence advances resident autonomy every step, supports proposals periodically, runs deep-time epochs, audits survival, and saves on schedule. This makes the prototype watchable without manually pressing every subsystem button.

## Prototype v0 basic visual-state update

The canvas now shows a basic playable state view instead of only a backdrop: village zones, avatar position, resident need/state markers, recent proposals, recent practices, deep-time emergent effects, resources, auto-sim state, and survival continuity. This keeps visuals intentionally simple while making the stochastic civilization legible during play.

## Prototype v0 save-slot update

The game prototype shell now includes browser-local prototype save slots. The player can save a slot, advance the autonomous simulation, return to the saved slot, and export a save receipt. This is intentionally scoped as prototype persistence evidence: it preserves meaningful village state, practice/proposal summaries, deep-time year, autonomous day, return log, and replay row counts without claiming production persistence.


## Prototype v0 ordinary-play discovery update

Normal player actions now feed the practical discovery loop. Talking, asking schedules, offering help, borrowing tools, and returning tools record ordinary pressure. Once public village pressure exists, repeated ordinary actions can trigger resident-generated tests and emergent practice candidates. This keeps practice formation inside lived play instead of requiring a separate report-style panel loop.


## Prototype v0 readable behavior update

Residents now expose public body-language cues derived from existing needs and actions. Autonomous ticks write a visible expression ledger with posture, movement, gaze, marker, and reason. The canvas draws those cues as simple readable markers, and the prototype surface includes a `Readable behavior` card. This is public behavior expression only, not private workspace exposure or subjective feeling.


## Prototype v0 acceptance receipt update

The shell now exports a browser-local `Game Prototype v0` acceptance receipt. Exporting acceptance runs or consumes Prototype QA, ensures a prototype save/return path exists, evaluates the current playable foundation against concrete requirements, stores the receipt in localStorage, and prepares a JSON download. This is a hardening artifact for game-build evidence, not production certification or a new research report.

