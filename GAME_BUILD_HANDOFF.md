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
- Physics-first 3D material substrate in the prototype shell: component objects carry mass, support, collision/contact, friction, moisture, decay, damage, and stochastic failure state.
- Resident local-language layer for practices and materials: engine concepts remain internal, resident terms emerge from grounded sound roots, and the player sees imperfect glosses.

## First game build should include

- One village.
- Up to six named residents.
- A small walkable 3D-simulation browser world using the maintained shell as the starting point.
- Simple primitive rendering of actual simulated components, not decorative fixed building sprites.
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
- No production-certified physical accuracy or polished physics tooling yet.
- No polished 3D art pipeline.
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
8. Keep physics as the substrate: material, support, time, labor, collision/contact, decay, and stochastic failure should explain world change.

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


## Prototype v0 player guide update

The prototype surface now includes a derived `Player guide` card. It reads the current state and suggests the next concrete action in the first playable loop: arrival, world pressure, ordinary play, village board, autonomy, deep time, return proof, QA, acceptance, or watch/compare. The guide is advisory only; it does not command residents or create scripted outcomes.


## Prototype v0 seed-divergence update

The prototype now includes a `Compare seeds` action and `Seed divergence` card. It holds the hidden material-law seed fixed while running multiple deterministic social/history branches, then compares local practice names, statuses, material burdens, safety rules, and risk profiles. The goal is to show divergent practice histories from the same law without a hidden tech tree or direct installation of a correct concept.


## Prototype v0 commons causality update

The prototype now includes an `Audit commons` action and `Commons / causality` card. It summarizes resources, low-resource pressure, work/time cost, tool wear, maintenance obligations, practice burden, accepted proposals, conservation flags, and hidden-law exposure flags from existing world state and the Reality Constraint Ledger. This makes causal health visible during play without adding a god-game resource spreadsheet or exposing hidden simulator law in normal view.


## Prototype v0 guided-step update

The prototype now includes a `Guide step` action. It reads the current Player guide phase and executes the matching existing prototype action, recording a guide history row with source phase, action, next phase, selected resident, and no direct resident command. This turns the advisory guide into a playable one-button path while preserving resident autonomy and avoiding scripted technology unlocks.


## Prototype v0 resident project update

The prototype now includes a diegetic resident project progress loop. Accepted Village Board proposals can advance into material-consuming work, stall under scarcity or resident unreadiness, complete with a new maintenance burden, update resident memory, and write Reality Constraint Ledger rows. The avatar still supports conditions rather than assigning jobs: project rows explicitly record no direct command, consumed materials, time/work cost, stalls, completion, and who felt the consequence.


## Prototype v0 resource commons support update

The prototype now includes a `Support commons` loop for recovering low resources or stalled projects without a god-game resource grant. Commons support picks a shortage or low reserve, ties it to a named source such as well carry, reed bundles, fallen branch salvage, or shared care work, spends resident time/labor, updates memory, and writes a Reality Constraint Ledger row. If a source is capped or a resident is too tired, the action records a blocked support row instead of spawning resources.


## Prototype v0 location-sensitive play update

The prototype now includes a `Nearby action` control tied to the avatar's current place. Moving or clicking in the canvas changes the available local action: shelter routes to bounded help, storage routes to commons support, the work yard routes to practical discovery or project work, the Village Board routes to resident proposals, and ordinary village space routes to schedule inquiry. Each nearby action records zone, room, selected resident, result event, and no direct command, then writes causal trace evidence.


## Prototype v0 village day-cycle update

The prototype now includes an `End day` loop. One button advances weather/resource pressure, several autonomous resident actions, accepted project work when possible, commons recovery when needed, and a readable day recap. Weather changes are bounded and causal: drizzle can damp fiber while adding water, dry wind can reduce water while helping fiber, cold can consume care, fallen branches can add wood, and storage damp can decay stored material. Each day writes weather, resident, project, commons, and causal ledger evidence instead of skipping time for free.


## Prototype v0 return-later update

The prototype now includes a `Return later` loop separate from save-slot rollback. Leaving the village advances several offscreen days, lets weather/resources/resident actions continue, returns the avatar to the arrival court, and writes absence plus return receipts. This proves forward return-session persistence instead of restoring an old snapshot: residents remember the absence, resources may change, and the replay records that no direct reset occurred.


## Prototype v0 3D stochastic physics and language update

The prototype direction is now physics-first 3D simulation with basic visual presentation. The shell includes a component-built material world where a raised storage practice is assembled from rough branches, fiber bindings, reed cover, and clay vessels. These are simulated components with 3D positions, mass, material properties, support roles, moisture, damage, and stability. The canvas projects those components as simple primitives.

The physics step applies gravity, support checks, contact/collision checks, friction, stochastic fatigue/failure probability, material transformation, and causal ledger rows. This is the intended substrate for the game. It is not a claim of production-certified physical accuracy.

Residents do not receive English technology labels. The shell now tracks grounded sound roots and resident terms such as `ta`, `ku`, `ren`, and `taku-ren`, with origin events, adoption, drift, variants, and imperfect player glosses. Engine concepts remain audit/internal terms.


## Prototype v0 physics-to-village consequence update

Physics is now part of ordinary play flow instead of a standalone inspection panel. `End day` advances the material/physics substrate after weather pressure, records the physics step in the day recap, and can create resident-facing Village Board concerns when support, collision, moisture, damage, or stochastic failure creates maintenance pressure. Auto simulation also advances material physics every step.

Residents can now react to physical risk through a `physics_repair` autonomous action. That action consumes fiber when available, repairs actual component damage/stability, updates memory, and shows a public repairing cue. Physics-linked proposals are saved and shown in prototype save summaries, keeping physical consequences persistent across return sessions.


## Prototype v0 project-to-component construction update

Resident project work now changes the physical world. Every project work tick writes a construction row that can repair strained components, and completed projects can add new resident-built reinforcement components such as rough branch supports, rough branch spans, fiber lashings, or simple containers. These components are inserted into the existing 3D structure, carry material/physics state, increase future maintenance burden, and are rendered as primitives rather than fixed building assets.

Save slots, Prototype QA, acceptance receipts, project cards, material-world cards, and replay rows now include construction counts and project-built component evidence. This keeps village management tied to physical causality: support conditions lead to resident labor, consumed materials, component repair or construction, and later maintenance pressure.


## Prototype v0 construction-practice language update

Resident-built components now feed culture. Construction rows create or refine Emergent Practice Graph nodes when repeated repair/build work becomes useful evidence. The linked resident term gains adoption, meaning drift, variants, and stronger practical weight, while sound roots record repair/build associations. This keeps technology as a historical practice emerging from physical work, not as an asset unlock or English concept label.


## Prototype v0 stochastic physics substrate update

Physics is now the simulation substrate rather than a side panel. The maintained shell tracks stochastic physical fields for moisture, heat, wind, decay pressure, and structural stress. Each physics step writes field rows, energy/work proxy rows, force/support/contact/failure rows, and component transformations.

Resident state now reacts to physical pressure: heat, moisture, weak supports, and structural stress increase effort or safety pressure, while `physics_repair` consumes fiber and repairs actual component damage/stability. Deep-time survival also depends on physical continuity: construction-linked lineages, physical heritage rows, component effect rows, average stability, average damage, and physical burden feed the continuity score.

This is still a browser-local prototype and not production-certified physical accuracy. The design direction is nevertheless strict: world change should route through stochastic physics, materials, resident labor, component state, and causal ledgers before it becomes culture, language, practice, or long-run survival.


## Prototype v0 resident material manipulation update

Residents can now physically handle simulated components instead of only reacting to abstract physics pressure. The shell adds `Resident handling` and `Handling loop` controls. A resident chooses from constrained actions such as carry, drop, stack, tie, dry, wet-test, or test based on current material state, carry capacity, resources, and stochastic pressure.

Handling actions mutate actual components: position, carried-by state, moisture, temperature, damage, stability, and field stress. They consume water or fiber where relevant, preserve failed handling as warning evidence, write Reality Constraint Ledger rows, update resident memory and visible body cues, and can create or refine Emergent Practice Graph nodes after repeated useful handling or recoverable failure.

The avatar still does not assign object work directly. The game loop exposes resident physical manipulation as a living-world consequence: residents try, fail, remember, teach, rename, and stabilize handling practices from material contact.

## Prototype v0 deep-time stochastic physics update

Compressed civilization history now starts with stochastic physics, not only lineage mutation. Each deep-time epoch writes a physics epoch row and material flux rows before cultural consequences are interpreted. The epoch pass advances physical substeps, then applies long-horizon moisture, heat, decay, settlement, mass loss, stability drift, and ruined-trace state to actual components.

Lineages inherit pressure from the components they depend on. If the physical structure decays, a practice can become burdened, forgotten, or harder to maintain; if it remains stable, usefulness can improve. Save slots, QA, acceptance receipts, and the Deep-time civilization card now expose physics epoch counts, material flux rows, mass retention, physical continuity, and lineage pressure links.

The goal is still not production-certified physics. The important game rule is stricter: long-run culture must pass through material physics before it becomes practice survival, village memory, proposal burden, or historical continuity.

## Prototype v0 resident body physics update

Residents now have physical bodies in the prototype shell. Each resident carries a simple capsule state with 3D position, velocity, mass, radius, height, carried load, carry capacity, fatigue, balance, footing, slip risk, and bounded recovery debt.

Autonomous actions and the `Body physics` controls move residents through physical targets such as shelter rest, work yard project space, storage practice, route markers, commons paths, and teaching areas. Movement is affected by terrain moisture, field stress, friction, load, fatigue, body contact, component contact, and stochastic slip risk. Slips and overloads create bounded recovery rows instead of permanent punishment.

The canvas now draws residents from body positions when initialized, and QA, acceptance, save/return, replay, and the Reality Constraint Ledger preserve body physics rows. This moves residents closer to embodied simulation: action choices must be paid for by bodies moving through a physical world.

## Prototype v0 terrain physics update

The village ground is now part of the simulation substrate. The shell adds terrain cells with height, slope, moisture, compaction, erosion, vegetation, walkability, support capacity, and drainage. Terrain changes from weather, neighbor moisture flow, resident body pressure, and component mass.

Terrain affects both residents and structures. Resident bodies read cell walkability as footing and slip pressure; components lose stability or gain damage when the ground below them becomes weak or wet. `Terrain physics` and `Terrain loop` expose this directly, while `End day` and auto sim advance terrain as part of ordinary time passage.

The canvas now overlays terrain cells, and save/return, QA, acceptance, replay, and the Reality Constraint Ledger preserve terrain rows. This makes the world less like a background map and more like a physical place residents must cross, maintain, avoid, and remember.

## Prototype v0 tool/work physics update

The prototype now treats tools as physical objects inside the stochastic physics loop. Resident work routes through tool fit, wear, damage, moisture, edge integrity, binding strength, stochastic failure, and repair cost instead of abstract success flags.

Game-build consequence: projects and material handling can slow down or create maintenance obligations because the physical tool failed, not because a scripted outcome demanded it.

Boundary: this is still browser-local prototype physics. It is not production-grade rigid-body simulation, but it preserves the rule that work requires bodies, tools, material contact, time, wear, and recoverable maintenance.

## Prototype v0 resource-stock physics update

Village resources now have a browser-local stochastic stock model. Water, fiber, wood, and care/attention are tracked as stored stocks with capacity, storage context, moisture/temperature exposure, decay or contamination pressure, source history, and per-step loss/gain ledgers.

Game-build consequence: resources are no longer just counters. Weather, terrain field state, vessel damage, resident fatigue, trust/rest, storage limits, and stochastic pressure can change stocks and constrain projects.

Boundary: care is modeled as embodied attention/recovery capacity, not a physical commodity. It still obeys time, fatigue, rest, trust, and bounded recovery constraints.

## Prototype v0 thermal/fire physics update

The prototype now has bounded thermal/fire physics. Watched heat sources track fuel, heat, ash, smoke, containment, ventilation, heat transfer by distance, material flammability, moisture, stochastic ignition risk, resident comfort/safety effects, and recoverable safety proposals.

Game-build consequence: warmth, drying, smoke, and bounded hazard are causal simulation state. Fire does not appear without fuel, heat, and air-like exposure; smoke creates care and safety work rather than spectacle.

Boundary: this is not a disaster/combat branch. Hazards must remain bounded, recoverable, inspectable, and tied to fuel, material, resident, and safety ledgers.
