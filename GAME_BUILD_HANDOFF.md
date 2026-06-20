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

## Prototype v0 browser QA readiness update

The maintained shell now includes a player-facing `QA readiness` control. It inspects the current browser state for normal player surface, primary canvas cues, first-playable session evidence, lived-action physics visibility, save/return continuity, and causal-ledger boundaries.

This preflight deliberately does not run Prototype QA or export acceptance. It exists to make the next browser-validation pass explicit and inspectable before validation is authorized.

## Prototype v0 auto-simulation update

The prototype now includes a browser-local auto-simulation clock. `Start auto sim` advances resident ticks on a timer; `Pause auto sim` stops it; `Auto burst` runs twenty inspected steps. The cadence advances resident autonomy every step, supports proposals periodically, runs deep-time epochs, audits survival, and saves on schedule. This makes the prototype watchable without manually pressing every subsystem button.

## Prototype v0 basic visual-state update

The canvas now shows a basic playable state view instead of only a backdrop: village zones, avatar position, resident need/state markers, recent proposals, recent practices, deep-time emergent effects, resources, auto-sim state, and survival continuity. This keeps visuals intentionally simple while making the stochastic civilization legible during play.

## Prototype v0 normal material-handling update

The maintained shell now exposes resident material handling as a normal player-facing verb. `Handling` routes to resident-chosen physical manipulation under carry capacity, tool, resource, moisture, support, and hidden-law constraints, while the avatar only influences conditions.

The first-playable session receipt records material-handling deltas and latest manipulation IDs. The Player Mode surface keeps the resident material-handling card visible so physical work is readable during ordinary play rather than isolated in debug controls.

## Prototype v0 embodied handling update

Resident material handling now emits resident body-physics links. The same handling event records the component manipulation and a resident body step with load, fatigue, contact/slip, target, and embodied distance.

The canvas now draws resident-to-object handling links and carried-object markers. This is still placeholder rendering, but it makes physical work legible as body-mediated action rather than an abstract receipt.

## Prototype v0 visible project-construction update

Resident project work now has a visual construction ledger. Each project advance records progress before/after, affected components, construction IDs, resident terms, canvas cue text, and no-fixed-asset/no-resource-spawning boundaries.

The canvas draws project progress bars and highlights repaired or newly added components. The visual result remains component-based: proposals change simulated posts, beams, lashings, vessels, and repair patches rather than spawning a building asset.

## Prototype v0 construction return-continuity update

Visible construction cues now participate in persistence evidence. Prototype save slots store project visual row counts, latest project visual IDs, and cue text. Save-slot restores report the restored visual construction state, and forward return-later receipts record visual construction rows added while the avatar was away.

The return journal surfaces these fields beside lived-action physics so later-session continuity includes physical project changes, not just abstract project completion counts.

## Prototype v0 avatar-presence return-continuity update

Avatar worksite presence now participates in return-session continuity. Presence rows, comfort/boundary rows, return-memory rows, remembered tone, comfort, boundary pressure, and refusal risk are summarized in prototype save slots and restore logs.

Return greetings can now reflect whether Gabriel was a helpful/familiar presence, a crowding pressure, a nearby witness, or absent from the worksite. This remains a condition-memory loop only: it does not command residents, transform material, expose hidden law, or erase the resident's ability to refuse.

## Prototype v0 integrated first-playable causality update

The first-playable session now writes an integrated causality row that links ordinary player pressure, resident-generated tests, resident proposals, physical handling, lived-action physics, emergent practice, save slot, and restore row into one inspectable chain.

This is the current prototype direction: the player should be able to follow one small village loop from problem to action to material consequence to practice to return-session continuity without reading separate report-style panels. The chain remains bounded by no-direct-command, no hidden law in normal view, and no tech-tree unlock.

## Prototype v0 integrated chain player-surface update

The primary play surface and world canvas now carry the latest integrated `FPI-...` chain. The normal player view can show the active chain, proposal, practice, lived physics row, save slot, and restore slot as public continuity cues while keeping hidden simulator law audit-only.

The `primary_play_surface` acceptance gate now requires at least one integrated-chain canvas cue. This makes the first playable loop visible in the actual player surface instead of only in a session receipt.

## Prototype v0 actionable integrated-chain update

The normal action rail now includes `Follow`. This player-facing verb reads the current integrated `FPI-...` chain and advances the next missing public link through existing resident-mediated systems: proposal cards, material handling, lived-practice physics, save, restore, return journal, or surface refresh.

`Follow` is not a command to a resident and does not unlock a technology. It is a player navigation affordance for continuing the visible chain while preserving no-direct-command, no hidden-law normal view, and no tech-tree boundaries.

## Prototype v0 Follow resident-response update

When the player uses `Follow`, the selected resident now records a small memory/social-state response and emits a public body-language cue. The normal rail stores the response expression ID and marker beside the `NPF-...` row.

This makes chain-following readable as a resident-noticed interaction rather than a silent UI automation step. The response remains bounded: it adjusts memory, comfort, trust, and public posture only; it does not command work, expose hidden state, or install knowledge.

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

## Prototype v0 physical routine-context update

Autonomous resident routines now read the physical village before choosing work. The resident tick derives a routine context from visible project construction, component damage/stability, carried or project-built components, and active practice nodes. That context can bias a resident toward repair, project work, or practice maintenance, but needs, hunger, safety, autonomy, and resource pressure can still override it.

Each tick writes a `routineContextLedger` row and links the action row back to the physical context. The normal village state and autonomous resident card show the latest worksite/component/practice link, while acceptance now checks that resident routines use physical context without direct player command or hidden-law exposure.

## Prototype v0 visual routine-context update

Routine context is now visible on the primary player canvas. The stage header shows the latest routine-context ID, resident, suggested action, and source. The canvas draws dashed resident-to-worksite links from resident body positions to physical components, project visuals, or practice anchors, and resident markers show the routine target in normal view.

This is intentionally simple placeholder rendering, but it moves the prototype closer to the game target: residents appear to orbit, repair, maintain, or watch actual physical places rather than only carrying abstract schedule text.

## Prototype v0 routine-directed body movement update

Routine context now affects resident body physics. When a resident tick or body-physics step has a physical routine target, the body target resolves to the linked component, project visual, or practice anchor. Body rows record the routine-context ID, target source, target component, distance before/after, and whether the resident moved toward the target.

This keeps the visible dashed worksite cues honest: resident bodies are not only connected to worksites graphically; the stochastic body simulation now steps toward those physical places with fatigue, footing, contact, and recovery costs.

## Prototype v0 worksite proximity update

Resident work now depends on physical proximity. Autonomous repair, proposal work, practice maintenance, and safety repair actions compute distance to the routine target before applying component effects. Close work can reduce damage, improve stability, or dry/maintain a component; distant work becomes partial or blocked evidence instead of magically changing the world.

Resident project construction also records proposer distance to the target component. That distance changes project progress and construction repair scale, so project labor is coupled to the body-position simulation rather than a detached progress bar.

## Prototype v0 avatar worksite-presence update

Avatar presence now affects cooperation as a condition, not a command. When the avatar is near a physical worksite, support/project/autonomous work rows can record a bounded presence influence: cooperation modifier, trust delta, willingness delta, distance, crowding, and whether the resident can still refuse.

This lets the player help by being present near the work, but the simulation still records `avatar_direct_command: false`. Presence alone never transforms material; it only changes social/attention conditions around resident-chosen work.

## Prototype v0 presence comfort/boundary update

Repeated avatar presence now has social memory pressure. Respectful repeated presence near a worksite can improve comfort and familiarity. Crowded or repeatedly intrusive presence raises boundary pressure and refusal risk. Residents expose this through public cues such as guarded stance, boundary posture, and refusal rows.

This keeps proximity meaningful without making residents obedient. Being nearby can help, crowd, or annoy depending on distance and history.

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

## Prototype v0 water/fluid physics update

The prototype now models bounded water/fluid physics. Stored jar water, low wet patches, and small hand-cut runoff lines track volume, capacity, containment, leakage, evaporation, slope, flow resistance, contamination, route pressure, vessel damage, and recoverable safety proposals.

Game-build consequence: water is no longer only a resource number or terrain moisture color. It can leak from damaged vessels, evaporate, pool on low routes, flow through a channel, affect walkability, sync back into stored water, and create resident proposals without direct player command.

Boundary: this is not full fluid dynamics. It is a causal gameplay layer that preserves volume, containment, slope, resistance, route pressure, and auditability.

## Prototype v0 ecology/food physics update

The prototype now has bounded ecology and food physics. Nearby food patches track biomass, carrying capacity, moisture fit, heat fit, rot pressure, route stress, regrowth, harvest difficulty, stored food, spoilage, hunger relief, and recoverable food-pressure proposals.

Game-build consequence: hunger is no longer relieved by a magic forage action. Food must grow, be gathered, survive storage, and be consumed. Weather, terrain moisture, water route pressure, heat, spoilage, and resident hunger now affect ordinary survival and scheduling.

Boundary: this is not a farming tech tree or population-growth system. It is a small causal ecology loop for the first village prototype.

## Prototype v0 structural-stress physics update

The game prototype shell now treats resident-built structures as stress-bearing component assemblies. The browser-local physics kernel tracks load paths, support margin, bending stress, anchor slip, deformation/sag, partial collapse rows, and repair pressure for the existing raised storage structure and future resident-built components.

This remains a bounded prototype solver, not certified engineering physics. It strengthens the game direction: structures are not fixed assets, materials are not free labels, and stress consequences become resident-facing repair pressure through the village board and reality ledger.

## Prototype v0 contact/joint constraint physics update

The prototype shell now models touching and bound components with a bounded stochastic contact-constraint layer. Structures can accumulate contact rows, joint rows, friction rows, impulse transfer rows, failed-joint rows, and constraint repair pressure.

This keeps the simulation direction physical without claiming production-grade rigid-body accuracy: components are conserved, resident-visible effects stay local and imperfect, and hidden friction/joint calculations remain audit-only.

## Prototype v0 material-state physics update

The prototype shell now gives each physical component a bounded material-state model. Components can accumulate saturation, dryness, rot, char, seal, cracking, softening, hardening, and effective property drift from heat, moisture, time, decay pressure, and stochastic material variation.

This keeps the direction physics-first: resident-built objects do not merely have labels or static material IDs. Their material condition changes over time and can create repair pressure without spawning or deleting matter.

## Prototype v0 playable physics-to-practice slice

The current game build now has a named playable milestone: `physics_to_practice_playable_slice`.

The slice is not a new research report. It is a browser-shell game loop that connects existing systems:

- 3D material/structural/contact/resource physics produce grounded evidence.
- Residents interpret the evidence as a local storage/repair concern, not as a modern technical concept.
- A resident proposal appears on the village board without direct avatar command.
- A resident material action/test links the proposal to repeated practice evidence.
- The emergent practice graph records a local term, `taku-ren`, with roots, drift, failed ancestors, materials, risks, and maintenance cost.
- A prototype save slot records the slice state so return sessions can preserve the linked physics/proposal/practice evidence.
- QA and acceptance receipts now include `physics_to_practice_playable_slice` as a named gate.

Player-facing target: enter the village, run `Playable slice`, inspect the new card, and confirm that physics evidence can become a resident-mediated practice without a tech-tree unlock.

## Prototype v0 milestone: Playable Village Day 0-3

The game shell now has a finite `Playable Village Day 0-3` loop. This is the next prototype milestone after the physics-to-practice slice.

The loop demonstrates one cohesive path:

- Day 0: enter the village, inspect ordinary place pressure, and advance stochastic 3D physics.
- Day 1: let physics evidence become a resident-mediated proposal/test path.
- Day 2: support commons, advance resident work, run autonomous residents, and include body/recovery cost.
- Day 3: leave, return, inspect continuity, and save the resulting state.

The acceptance gate is `playable_village_day_0_3`. It is deliberately finite: it proves a playable loop exists before expanding the world or adding new research branches.

## Prototype v0 milestone: Primary Play Surface

The browser shell now has a `Primary play surface` milestone. The canvas is treated as the main game readout, while panels remain inspection and audit support.

The surface summarizes, in one place:

- current village problem
- selected resident and schedule
- next player action
- active proposal
- active practice
- active physical component
- latest physics row
- latest lived-action physics row
- resource pressure

The canvas now draws recent lived-action physics on actual component positions. Rings, small state bars, and latest physics IDs show whether ordinary play affected moisture, damage, stability, or field stress. This keeps practice formation visible as material change rather than only as ledger text.

The acceptance gate is `primary_play_surface`. This does not make the visual layer final art; it makes the existing primitive 3D/canvas shell function as a playable interface instead of only a debug dashboard.

## Prototype v0 milestone: First Playable Walkthrough

The shell now includes a `First playable` walkthrough action and exportable walkthrough receipt.

The walkthrough sequences the current game foundation into one player-facing path:

- enter the village
- inspect the primary world stage
- observe a physical bottleneck
- let residents produce or test a proposal/practice path
- support conditions without direct command
- wait through resident work or recovery
- leave and return with continuity
- save the state
- build an acceptance snapshot

The acceptance gate is `first_playable_walkthrough`. This is the first durable receipt that the shell can be played as a coherent path instead of only as individual subsystem buttons.

## Prototype v0 milestone: Normal Play Action Rail

The shell now includes a normal player-facing action rail with nine verbs:

- Look
- Move
- Ask
- Talk
- Objects
- Support
- Wait
- Return
- Save

These actions map onto existing systems while preserving resident mediation. The acceptance gate is `normal_play_action_rail`.

This moves the prototype closer to a playable interface: the player no longer needs to understand subsystem names to drive the first playable path.

## Game prototype v0 update: Player Mode Interface

The browser shell now includes a `Player mode` toggle and `Player mode loop` milestone. Player mode foregrounds the actual play surface: canvas, normal action rail, selected resident cue, current problem, player guide, primary play surface, walkthrough state, normal action receipt, and public outcomes.

While player mode is active, debug-heavy controls, subsystem action grids, QA manifest, deep traces, and hidden-law audit panels are hidden by default. They remain available by leaving player mode or using explicit audit/reviewer controls. The mode records `player_mode_interface` acceptance evidence without spawning resources, commanding residents, exposing hidden simulator law, or adding a tech-tree shortcut.

This is game-build interface work, not a research report. The goal is to make the existing village prototype playable before adding more systems.

## Game prototype v0 update: Resident Proposal Deck

The browser shell now includes a `Proposals` rail action, `Proposal deck` prototype action, and `Resident proposal deck` player-mode card. The deck reads existing Village Board proposals and exposes them as player-facing cards with proposer, problem, materials, willingness/support, status, risk, objections, related practice nodes, and possible failure modes.

Player deck actions are limited to Ask, Support, and Wait. They route through the existing Village Board functions, preserve resident autonomy, record causal ledger rows, and can still produce delay, refusal, resource cost, or stalled work. The acceptance gate is `resident_proposal_deck`.

This moves the prototype closer to a real village-management loop while preserving the rule that the avatar influences conditions rather than commanding people.

## Game prototype v0 update: Lived Practice Loop

The browser shell now includes a `Practice` normal rail action, `Practice loop` prototype action, and `Lived practice loop` player-mode card. The loop now uses ordinary Move, Objects, Support, and Wait actions, routes them through practical discovery, records source ordinary-pressure feed rows, applies bounded physical deltas to real 3D components, and surfaces the resulting emergent practice as a normal gameplay object.

The card shows local practice name, status, materials, supporting observations, failed ancestors, adoption count, maintenance cost, ordinary feed count, and physics rows. Save slots, return logs, return journal rows, and first-playable session rows now preserve the lived-action physics count and latest physics ID. Acceptance evidence is recorded as `lived_practice_loop`. The loop preserves the no-command, no-hidden-law-normal-view, no-correct-concept-installed, no-resource-spawning, conservation, and no-predeclared-tech-tree boundaries.

This is a key game-foundation step: practice formation is now visible from normal play instead of existing only as a debug panel or research receipt.

## Game prototype v0 update: Resident Worksite

The browser shell now includes a `Worksite` normal rail action, `Worksite loop` prototype action, and `Resident worksite` player-mode card. The worksite wraps the existing resident project system and displays consequences as gameplay: active proposal, resident, status, progress, construction id, resident term, linked practice, components added/repaired, stalls, and maintenance burden.

The loop preserves project autonomy. Work can stall on resident readiness or resource scarcity, consume materials, wear tools, repair simulated components, add component-built structure pieces, complete, or create future maintenance obligations. Acceptance evidence is recorded as `resident_worksite`.

This moves the prototype toward a playable village-management loop without turning it into job assignment or a fixed building-placement game.

## Game prototype v0 update: Return Journal

The browser shell now includes a `Journal` normal rail action, `Return journal` prototype action, and `Return journal` player-mode card. The journal wraps existing forward return sessions and prototype save-slot restoration into one readable player surface.

Each run records a before-save snapshot, an after-away snapshot, and an after-save-slot-return snapshot. The card shows days away, remembered residents, resource totals before/after/restore, active save slot, restored year/day, forward return id, lived-action physics rows before/after/restore, and source-history boundary flags. Acceptance evidence is recorded as `return_journal`.

This closes a major player-facing continuity gap: the prototype can now show what happened while the avatar was gone and what a saved return restored without conflating away-time persistence with rollback.

## Game prototype v0 update: First Playable Session Receipt

The browser shell now includes a `Session` normal rail action, `Play session` prototype action, and `Play session receipt` player-mode card. The session receipt sequences the already-built player surfaces as one coherent playable pass: Player mode, Look, Move, Talk, Objects, resident proposals, lived practice, resident worksite, return journal, Save, and Return. It also records lived-action physics continuity for the session steps.

## Game prototype v0 update: Player Movement Route

The shell now includes a `Move` normal rail action, `Movement route` prototype action, and `Movement route` player-mode card. The movement route keeps the prototype spatial: the avatar changes village zones through bounded movement, the interface records nearby residents/materials/practices after each move, and the reality ledger records that movement as a causal spatial action rather than an instant command or abstract menu choice.

The acceptance gate is `first_playable_session`. It records step rows and snapshots while preserving no direct command, no hidden-law exposure in normal view, and no tech-tree unlock. This is the first receipt for the player-facing session itself rather than another subsystem panel.

This should be treated as the handoff point for the next game-build increment: improve the actual feel of playing this sequence before adding new conceptual systems.

## Game prototype v0 update: Physical Object Interaction

The browser shell now includes an `Objects` normal rail action, `Object interaction` prototype action, and `Physical object interaction` player-mode card. The player can inspect the active physical component, see the resident-local term and imperfect gloss, and let residents choose a handling response through the existing material manipulation system.

The acceptance gate is `player_object_interaction`. It records component state before/after, resident action, manipulation id, physics step, practice link, and boundary flags. The player does not pick up, place, repair, or command the object directly; the avatar creates attention and residents decide what handling is possible under mass, moisture, stability, tool, labor, and resource constraints.

This makes the 3D physics substrate playable through ordinary UI instead of leaving it as a debug panel.

## Game prototype v0 update: Bounded Resident Encounter

The browser shell now includes a `Talk` normal rail action, `Resident encounter` prototype action, and `Resident encounter` player-mode card. It turns the selected resident into a readable game interaction without adding open-ended language.

The acceptance gate is `player_resident_encounter`. It records resident cue, posture, schedule, memory, active proposal, active practice, active object, trust before/after, and a deterministic bounded response. The response is assembled from existing state and phrasebook hooks; no LLM is called and no autonomous natural-language system is introduced.

This makes resident continuity visible in normal play. The player talks and listens; the resident response remains source-traced, bounded, and tied to actual simulation state.
