# First Playable Prototype Scope

## Included

- One village.
- Six residents maximum.
- Small map around shelter, storage, work area, route, and board.
- Physics-first 3D simulation state for physical components, materials, stochastic fields, support, collision/contact, heat/moisture, decay, energy/work proxies, and stochastic failure.
- Terrain physics cells for height, slope, moisture, compaction, erosion, vegetation, walkability, support, drainage, body footing, and component support.
- Deep-time stochastic physics epochs that mutate actual component mass, moisture, damage, stability, settlement, ruined traces, lineage pressure, and material flux evidence.
- Simple primitive rendering of simulated objects.
- Small resource set: water, fiber, wood, care, and one or two special materials.
- One anomaly family.
- One or two emergent practice chains.
- One Village Board.
- One resident proposal/project loop.
- One resident body physics layer for position, velocity, footing, load, fatigue, contact, slip risk, and bounded recovery.
- One resident physical material-handling loop for carry, drop, stack, tie, dry, wet-test, and test actions.
- One resident physical routine-context loop that links autonomous schedules to construction, components, project visuals, and practice sites.
- One worksite proximity loop that makes component repair/build effects depend on resident body position.
- One avatar worksite-presence loop that affects cooperation/trust/willingness without commanding residents.
- One presence comfort/boundary loop where repeated or crowded presence changes comfort, boundaries, and refusal risk.
- One stochastic consequence and recovery loop.
- One save/return loop.
- One audit/replay mode.
- One normal player-facing interface.
- One integrated first-playable causality chain linking ordinary action, resident bottleneck/test, proposal, physical handling, lived physics, emergent practice, save, and restore.
- One primary-surface/canvas cue for the integrated chain so the loop is playable without opening debug-only panels.
- One normal `Follow` verb that advances or refreshes the active integrated chain without directly commanding residents.
- One resident-visible `Follow` response that records memory and a public body-language cue.
- One calibrated `Follow` boundary path where residents can guard or refuse under pressure.
- One normal `Space` verb that recovers after guarded/refused `Follow` without advancing the chain.
- One 10-minute playable loop that proves object/material change, emergent practice evidence, and save/return persistence in one normal play path.
- One canvas-visible material-state overlay for the active physical component.
- One direct canvas component selection path that inspects simulated objects without direct manipulation.
- One bounded resident object-response path before material manipulation.
- One consequential object-response path where objections block and warnings reroute handling.
- One bounded resident language/gloss layer for local terms that emerge from grounded practice history.

## First prototype success condition

A new player can enter the village, learn that residents have their own concerns, support a proposal without commanding anyone, observe an anomaly, see residents interpret it differently, watch a practice emerge from repeated lived action, leave or save, return, and see the history still affect normal interaction.

## Out of scope for first prototype

- More villages.
- New regions.
- Combat or war.
- Full economy.
- Population growth simulation.
- Large tech trees.
- Open-ended LLM dialogue.
- New consciousness/metaphysics mechanics.
- Polished 3D engine/art pipeline.
- Production-certified physical accuracy.
- Production backend persistence.

## Deep-time prototype target

The first prototype may include a compressed million-year simulation as long as it remains tied to the one-village playable loop. Deep-time effects should become resident schedules, memories, public proposals, and audit rows rather than detached lore text.

Deep-time continuity should remain physically grounded: construction-linked lineages, component heritage, field pressure, stability, damage, maintenance burden, and resident repair practices should affect whether a lineage survives as living practice, costly habit, trace memory, or forgotten evidence.

Deep-time history should not be accepted as only a narrative/culture ledger. The prototype should preserve physics epoch rows and material flux rows showing what happened to components before residents reinterpret the result.

## Included prototype physics layer: tools and work

Prototype v0 includes a minimal physical tool/work subsystem:

- local resident tool terms and player glosses
- tool mass, hardness, leverage, edge integrity, binding, moisture, wear, and damage
- stochastic use/failure rows
- repair rows that consume real resources
- coupling into resident material handling and village project progress
- save/return and acceptance counters for tool use, wear, failure, and repair

This remains intentionally simple visually, but it is part of the serious simulation substrate.

## Included prototype physics layer: resource stocks

Prototype v0 includes a minimal resource-stock subsystem:

- stored water jars, fiber bundles, rough wood stack, and embodied care/attention reserve
- stock capacity, moisture, temperature, decay, contamination, and storage context
- stochastic stock, transform, loss, gain, and sync ledgers
- coupling to weather, terrain/material fields, vessel damage, resident fatigue, rest, and trust
- save/return and acceptance counters for stock steps, resource transformations, losses, and gains

This replaces pure resource-counter behavior with causal stock pressure while preserving simple player readability.

## Included prototype physics layer: thermal/fire

Prototype v0 includes a minimal thermal/fire subsystem:

- watched heat nodes and warm surfaces
- fuel consumption and ash/smoke state
- ventilation, moisture, heat transfer, drying, and material burn risk
- stochastic ignition rows that remain recoverable
- resident comfort/safety effects
- safety proposals for smoke or heat risk
- save/return and acceptance counters for heat, fuel, smoke, ignition, and safety rows

This is bounded utility physics, not disaster spectacle.

## Included prototype physics layer: water/fluid

Prototype v0 includes a minimal water/fluid subsystem:

- contained jar water, low wet patch, and small runoff channel
- volume, capacity, contamination, leakage, evaporation, slope, resistance, and route pressure
- terrain moisture/walkability/erosion coupling
- vessel damage and stored water resource sync
- resident footing/safety pressure and recoverable water proposals
- save/return and acceptance counters for flow, leak, vessel, quality, route, and safety rows

This is bounded causal fluid gameplay, not a full CFD simulation.

## Included prototype physics layer: ecology/food

Prototype v0 includes a minimal ecology/food subsystem:

- small edible patches with biomass, carrying capacity, regrowth, and rot sensitivity
- growth coupling to terrain moisture, thermal state, water route stress, and stochastic pressure
- harvest rows that add food only from patch biomass
- spoilage rows for stored food
- hunger rows that consume stored food to reduce resident hunger
- recoverable resident proposals for food pressure, spoilage, or overharvest risk
- save/return and acceptance counters for growth, harvest, spoilage, hunger, and safety rows

This is bounded survival ecology, not an agriculture tech tree.

## Included prototype physics layer: structural stress

Prototype v0 now includes bounded structural stress for component-built structures. The included scope is support margin, bending/load stress, anchor slip, deformation, partial collapse markers, and repair proposals.

Out of scope for v0: production-grade rigid-body simulation, finite-element accuracy, full fracture mechanics, polished construction art, and direct player building placement.

## Included prototype physics layer: contact constraints

Prototype v0 now includes bounded contact and joint constraints for component-built structures. The included scope is likely contact detection, joint/binding detection, friction limits, impulse transfer, slip probability, joint demand/strength, component wear, anchor slip, and repair pressure.

Out of scope for v0: full continuous collision detection, exact rigid-body stacks, detailed rope simulation, fracture meshes, and production-grade physics certification.

## Included prototype physics layer: material state

Prototype v0 now includes bounded material state and phase drift. Included states are saturation, dryness, rot, char, seal, crack, softening, hardening, effective hardness, brittleness, water resistance, and workability drift.

Out of scope for v0: real chemistry, molecular simulation, detailed combustion, full fermentation, exact drying models, and production-grade material science.

## Added scope gate: physics-to-practice playable slice

The first playable prototype includes one named acceptance gate for lived discovery:

`physics_to_practice_playable_slice`

Required evidence:

- linked physics rows from material state, structural/contact constraints, or resource stock
- one resident-generated proposal related to that pressure
- one resident-mediated material action/test
- one emergent practice mutation with local resident term and imperfect player gloss
- one save/return proof row linking the practice and proposal to a saved slot
- no direct player command
- no predeclared invention list
- no installed correct modern concept

This is the preferred next milestone for prototype work. Do not add new research reports to satisfy it; improve the playable shell.

## Added scope gate: Integrated first-playable causality chain

The first-playable session must include an inspectable chain from player action to return continuity.

Required evidence:

- ordinary player action or pressure row
- resident bottleneck or resident-generated test
- resident proposal or board pressure
- material handling row against a real component
- lived-action physics row
- emergent practice row with local name or imperfect gloss
- save slot row
- restore row
- primary play-surface or canvas cue carrying the chain ID
- normal action-rail follow row carrying the chain ID
- resident response expression linked to the follow row
- calibrated outcome showing constructive, guarded, helpful, or refused follow pressure
- no direct player command
- no hidden simulator law in normal view
- no tech-tree unlock or installed modern concept

This gate prevents the first playable from being a collection of isolated panels.

## Added scope gate: Resident routines use physical context

`resident_routines_use_physical_context` is part of the first playable prototype scope.

Required evidence:

- autonomous resident rows include linked routine-context IDs
- routine context rows reference physical state such as visible construction, construction rows, weak components, project-built components, carried components, or practice nodes
- routine context can suggest repair, proposal work, practice maintenance, or observation
- resident needs and autonomy can still override the suggestion
- resident body physics can resolve the routine context into a physical target
- body rows record distance before/after and whether the resident moved toward that target
- normal village state exposes only public worksite/component/practice context
- the primary canvas draws a resident-to-worksite routine cue
- hidden simulator law remains out of normal view
- no direct resident command is introduced

This gate prevents schedules from becoming abstract NPC text disconnected from the physical village.

## Added scope gate: Routine context visible on canvas

`routine_context_visible_on_canvas` is part of the first playable prototype scope.

Required evidence:

- primary play-surface cue rows include a routine-context ID
- the latest primary snapshot contains a non-empty routine-context source
- resident routine cues draw against physical components, project visuals, or practice anchors
- normal view shows resident, suggested action, and source without hidden-law exposure
- acceptance can prove the cue after save/return and autonomous resident activity

This gate keeps routine context visible in the player's world, not hidden in debug ledgers.

## Added scope gate: Routine context moves resident bodies

`routine_context_moves_resident_bodies` is part of the first playable prototype scope.

Required evidence:

- at least one resident body step uses `target_source=routine_context`
- the body row links to a non-empty routine-context ID
- the row records target component or practice/source context
- distance-to-target decreases during the step
- movement still pays fatigue, footing, contact, and recovery costs
- no direct player body command is introduced
- hidden simulator law remains out of normal view

This gate makes resident routine context embodied instead of only visual or textual.

## Added scope gate: Worksite proximity affects component work

`worksite_proximity_affects_component_work` is part of the first playable prototype scope.

Required evidence:

- autonomous resident work records a worksite proximity row
- at least one nearby work row changes component damage, stability, or moisture
- distant work can be recorded as partial or blocked instead of changing matter at a distance
- project progress rows record target component distance
- project construction uses proximity scale when repairing components
- no direct player command is introduced
- hidden simulator law remains out of normal view

This gate prevents resident schedules, movement, and project progress from becoming disconnected systems.

## Added scope gate: Avatar presence influences worksite cooperation

`avatar_presence_influences_worksite_cooperation` is part of the first playable prototype scope.

Required evidence:

- avatar presence rows record distance to a physical worksite component
- nearby avatar presence can change cooperation, trust, or willingness as a bounded condition
- resident can still refuse
- presence does not transform material by itself
- project/support/autonomous rows can link to a presence ID
- primary play-surface cues expose the presence link in normal view
- no direct player command is introduced
- hidden simulator law remains out of normal view

This gate makes player presence socially meaningful without turning the prototype into a god-game control surface.

## Added scope gate: Avatar presence affects comfort and refusal

`avatar_presence_affects_comfort_and_refusal` is part of the first playable prototype scope.

Required evidence:

- avatar presence rows track repeated nearby presence and crowding
- presence comfort rows record comfort before/after
- nearby presence can change comfort, boundary pressure, or refusal risk
- resident visible cues can show guarded or boundary state from presence pressure
- resident refusal remains possible and source-traced
- presence does not directly command work or transform material
- hidden simulator law remains out of normal view

This gate prevents player proximity from being a one-way positive buff.

## Added scope gate: Avatar presence persists through return

`avatar_presence_persists_through_return` is part of the first playable prototype scope.

Required evidence:

- avatar presence rows and comfort rows exist before save or return
- return-memory rows preserve the source presence and comfort history
- save slots summarize presence rows, comfort rows, remembered tone, comfort, boundary pressure, and refusal risk
- save-slot restore logs report restored presence state and create a return greeting row
- return-later receipts can carry the same remembered tone forward
- resident greetings can distinguish helpful/familiar presence from crowded/guarded presence
- no direct player command is introduced
- hidden simulator law remains out of normal view
- remembered presence does not transform material by itself

This gate keeps player proximity socially persistent without turning it into obedience, a buff, or a hidden reset.

## Added scope gate: Playable Village Day 0-3

`playable_village_day_0_3` is now part of the first playable prototype scope.

The gate requires:

- at least four Day 0-3 rows
- player loop evidence without direct command
- resident loop evidence with refusal/delay possibility preserved
- world loop evidence with causal trace
- linked physics evidence
- linked proposal evidence
- linked practice evidence
- save evidence
- return-session evidence
- no fixed tech-tree unlock

This is the current best next milestone for making the shell feel like a game rather than a collection of panels.

## Added scope gate: Primary Play Surface

`primary_play_surface` is now part of first playable prototype scope.

Required evidence:

- canvas-first milestone state
- at least three focus rows
- at least three canvas cue rows
- at least three action prompt rows
- active proposal appears in the surface history
- active practice appears in the surface history
- active physical component appears in the surface history
- no hidden simulator law exposed in normal view
- no direct resident command

This is the bridge from proof shell to playable shell.

## Added scope gate: First Playable Walkthrough

`first_playable_walkthrough` is now part of the first playable prototype scope.

Required evidence:

- all nine walkthrough steps present
- proposal evidence linked
- practice evidence linked
- physical component evidence linked
- physics evidence linked
- save evidence linked
- return-session evidence linked
- resident-mediated action preserved
- no hidden law in normal view
- no direct command
- no tech-tree unlock

This is the first single-receipt proof that the prototype has a coherent playable path.

## Added scope gate: Normal Play Action Rail

`normal_play_action_rail` is now part of first playable prototype scope.

Required evidence:

- all normal verbs are used at least once, including Move, Talk, and Objects
- options shown in player language
- action rows remain non-commanding
- hidden law is not exposed in normal view
- actions link to proposal/practice/component/physics/save/return evidence when available
- follow recovery rows show `chain_advanced=false` after guarded/refused pressure
- no tech-tree unlock

This is the main player-facing control layer for the first playable shell.

## Prototype v0 milestone: Player Mode Interface

`player_mode_interface` is now part of first playable prototype scope.

Required evidence:

- the shell can enter a normal player-facing mode
- the canvas, resident cue, player guide, primary play surface, normal action rail, and public outcomes remain visible
- debug-heavy panels and subsystem action grids are hidden by default while player mode is active
- audit access is preserved as an explicit mode, not mixed into normal play
- the mode records a session row without directly commanding residents
- hidden simulator law remains out of normal view
- player-visible labels remain glosses and player-language verbs, not resident omniscience or tech-tree terms

This is the first interface narrowing milestone after the normal action rail. It does not add new world law; it makes the existing prototype playable from the normal surface.

## Prototype v0 milestone: Resident Proposal Deck

`resident_proposal_deck` is now part of first playable prototype scope.

Required evidence:

- proposal cards are derived from resident-generated Village Board proposals
- each card shows proposer, problem, materials, willingness/support, status, risk, objections, and possible failure modes in player-facing language
- the player can Ask, Support, or Wait from the deck
- deck actions record no direct resident command
- hidden simulator law remains out of normal view
- support routes through the existing resident proposal system and may still be refused, delayed, stalled, or resource-constrained
- no proposal card installs a technology concept or unlocks a tech tree

This milestone turns resident proposals into a playable surface. It does not create a god-game task assignment panel.

## Prototype v0 milestone: Lived Practice Loop

`lived_practice_loop` is now part of first playable prototype scope.

Required evidence:

- repeated normal player actions can drive practical discovery, including Move, Objects, Support, and Wait
- the loop creates practical test rows and emergent practice snapshots
- lived-practice rows trace back to ordinary pressure feed, movement, or object-interaction evidence
- lived-practice actions apply bounded physical deltas to real 3D components
- physics rows record no resource spawning, material conservation, work/time/tool burden, and hidden-law separation
- save/return and first-playable session receipts preserve lived-action physics row counts and latest physics IDs
- the canvas shows lived-action physics cues on affected physical components
- the visible card shows local practice name, status, materials, observations, failed ancestors, adoption count, and maintenance burden
- actions remain player-language actions, not subsystem-only buttons
- the avatar does not directly command residents
- hidden simulator law remains out of normal view
- no predeclared technology or correct concept is installed

This milestone makes practice formation visible as gameplay: residents stabilize a practice from repeated lived actions and bottlenecks, not from a fixed tech tree or report-only artifact.

## Prototype v0 milestone: Resident Worksite

`resident_worksite` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes a Worksite action
- worksite rows come from resident proposal/project work, not player job assignment
- project work can consume materials, stall, repair components, add components, complete, or create maintenance burden
- the visible card shows proposal, resident, status, progress, construction id, resident term, related practice, components added/repaired, stalls, and maintenance cost
- every row records no direct command, no hidden-law exposure in normal view, and no resource spawning
- construction remains component-based, not fixed building assets

This milestone makes project consequences visible as gameplay. The player watches and supports conditions; residents still perform the work.

## Prototype v0 milestone: Return Journal

`return_journal` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes a Journal action
- the journal records a before-save snapshot, an after-away snapshot, and an after-save-slot-return snapshot
- forward return sessions remain distinct from save-slot restoration
- the visible card shows days away, remembered residents, resource totals before/after/restore, save slot, restored year/day, and source history
- the journal records no direct reset and no hidden-law exposure in normal view
- return evidence is player-facing instead of buried in debug panels

This milestone makes save/return and away-time continuity readable during play.

## Prototype v0 milestone: First Playable Session Receipt

`first_playable_session` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes a Session action
- the prototype action grid exposes Play session
- the session runs Player mode, Look, Move, Talk, Objects, Proposals, Practice, Worksite, Journal, Save, and Return as one sequence
- lived-action physics rows remain visible through Journal, Save, and Return steps

## Prototype v0 milestone: Player Movement Route

The first playable prototype now requires a movement receipt. The player must be able to move through bounded village space, update nearby affordances from the current zone, and leave a source-traced movement record that can participate in save/return continuity and later practice formation.
- each session step records a player-facing row and snapshot
- proposal, practice, worksite, return journal, save, and return evidence are linked from the same receipt
- every row records no direct resident command
- hidden simulator law remains out of normal view
- no step installs a tech-tree unlock or correct resident concept
- the receipt survives save-slot restoration boundaries without losing its existing step ledger

This milestone is the first coherent game-session receipt. It does not add a new simulation system; it proves the existing systems can be driven from the player-facing surface.

## Prototype v0 milestone: Browser QA Readiness

`first_playable_browser_qa_readiness` is now part of first playable prototype scope.

Required evidence:

- the prototype action grid exposes a QA readiness action
- the visible card reports readiness without running Prototype QA
- readiness checks cover normal player surface, primary canvas cues, first-playable session evidence, lived-action physics visibility, save/return continuity, and causal-ledger boundaries
- the receipt explicitly marks that QA was not executed
- the next action remains an explicitly authorized Prototype QA/browser pass

This milestone keeps the handoff honest: readiness is not completion, and validation is not claimed before it is run.

## Prototype v0 milestone: Normal Material Handling

`normal_material_handling` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes a Handling action
- Handling routes through resident-chosen manipulation, not direct avatar object control
- resident handling can carry, dry, tie, wet-test, stack, or test real simulated components
- handling respects carry capacity, tools, resource cost, moisture, support, stress, and hidden-law boundaries
- first-playable session steps record material-handling row deltas and latest manipulation IDs
- Player Mode keeps resident material handling visible as ordinary play evidence

This milestone makes physical work part of the player-facing game loop.

## Prototype v0 milestone: Embodied Handling Cues

`embodied_handling_cues` is now part of first playable prototype scope.

Required evidence:

- resident material-handling rows include body step IDs
- the body step records load, fatigue, contact/slip, target, and no direct player body command
- first-playable session receipts count body-linked handling rows
- the canvas draws resident-to-object handling cues
- carried components are visually attached to the resident marker when applicable
- hidden simulator law remains out of normal view

This milestone makes the placeholder renderer express the physical coupling between resident bodies and handled components.

## Prototype v0 milestone: Visible Project Construction

`visible_project_construction` is now part of first playable prototype scope.

Required evidence:

- resident project work records visual construction rows
- visual rows include proposal ID, construction ID, progress before/after, affected component IDs, resident term, and canvas cue
- repaired and newly added components are drawn as physical components on the canvas
- project progress appears as a visible bar instead of only text in a receipt
- project-built components preserve no-fixed-asset and no-resource-spawning boundaries
- acceptance evidence counts construction rows, visual rows, and project-built components

This milestone makes resident proposals visibly assemble or repair the world over time.

## Prototype v0 milestone: Construction Return Continuity

`construction_return_continuity` is now part of first playable prototype scope.

Required evidence:

- save slots record project visual row counts, latest visual IDs, and cue text
- save-slot return logs report restored project visual row counts and latest visual IDs
- forward return-later receipts report project visual rows added while away
- the return journal shows project visual rows before save, after away-time, and after restore
- the player can distinguish offscreen construction changes from restored saved construction state
- no hidden simulator law appears in normal return-journal view

This milestone keeps visible physical construction history persistent across return sessions.

## Prototype v0 milestone: Physical Object Interaction

`player_object_interaction` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes an Objects action
- Player Mode includes a Physical object interaction card
- the card shows an actual simulated component, resident term, imperfect player gloss, affordance, mass, moisture, stability, damage, stress, and carried state
- the player action routes through resident-chosen material manipulation, not direct avatar object control
- rows link component id, manipulation id, resident action, physics step, and practice id when available
- every row records no direct resident command
- hidden simulator law remains out of normal view
- no step installs a tech-tree unlock or correct resident concept
- component changes are caused by the existing material manipulation/physics system

This milestone makes the physics substrate playable from ordinary UI. It does not create free-form construction or direct object placement by the player.

## Prototype v0 milestone: Bounded Resident Encounter

`player_resident_encounter` is now part of first playable prototype scope.

Required evidence:

- the normal rail exposes a Talk action
- Player Mode includes a Resident encounter card
- the card shows selected resident cue, posture, schedule, memory, active proposal, active practice, and active object context
- the response is deterministic and phrasebook-bounded
- the row records no LLM and no open-ended language
- source history is preserved
- every row records no direct resident command
- hidden simulator law remains out of normal view

## Added scope gate: 10-minute playable loop

`ten_minute_playable_loop` is now part of first playable prototype scope.

Required evidence:

- the normal player surface can run a compact 10-minute path
- the path includes Look, Move, Talk, Objects, Handling, Support, Practice, Save, Wait, and Return
- object/material state changes visibly through resident-mediated handling
- the changed state persists after save/return
- one emergent practice id is linked to the lived evidence
- residents are not directly commanded
- hidden simulator law remains out of normal view
- no tech-tree unlock occurs

## Added scope gate: Canvas material state visible

`canvas_material_state_visible` is now part of first playable prototype scope.

Required evidence:

- the main canvas highlights the active physical component
- the canvas shows resident term and imperfect player gloss
- the canvas shows material id, mass, and carried state
- the canvas shows moisture, damage, stability, and stress as visible state bars
- exported acceptance includes material-state canvas cue rows
- hidden simulator law remains out of normal view
- no step installs a tech-tree unlock or correct resident concept

## Added scope gate: Canvas component selection

`canvas_component_selection` is now part of first playable prototype scope.

Required evidence:

- clicking near a projected physical component records a `COS-...` selection row
- the selected component becomes the active primary-surface component
- later object inspection uses the canvas-selected component
- selection rows are inspect-only
- residents are not commanded by selection
- hidden simulator law remains out of normal view
- no tech-tree unlock occurs

## Added scope gate: Resident object response

`resident_object_response` is now part of first playable prototype scope.

Required evidence:

- object inspection records an `OIR-...` resident response before handling
- response kind comes from visible component state
- resident response is phrasebook-only and deterministic
- visible body language records observation or objection
- response can warn, object, or allow handling without forcing obedience
- hidden simulator law remains out of normal view
- no LLM or open-ended language is used
- no tech-tree unlock occurs

## Added scope gate: Resident object response affects handling

`resident_object_response_affects_handling` is now part of first playable prototype scope.

Required evidence:

- object-interaction rows link an `OIR-...` response to a handling effect
- ownership objections or safety warnings can block handling before manipulation
- wet-material or labor cautions can reroute handling through caution action sources
- ordinary observations can allow resident-chosen handling to continue
- blocked handling rows do not require a manipulation id
- no direct command, hidden-law exposure, LLM, open-ended language, or tech-tree unlock occurs

This milestone makes resident continuity readable during ordinary play. It does not add an open-ended language system.

## Added scope gate: Blocked object response creates proposal

`blocked_object_response_creates_proposal` is now part of first playable prototype scope.

Required evidence:

- a blocked ownership objection or safety warning creates a follow-up `VBP-...` proposal
- the object-interaction row records `follow_up_proposal_id`
- the Village Board proposal records `related_object_response_id`
- the proposal describes resident access, safety, or stabilization work rather than direct object manipulation
- the avatar can ask, support, or wait on the proposal but cannot force acceptance
- the proposal preserves no direct command, hidden-law separation, and no tech-tree unlock
- blocked object handling becomes a diegetic management problem instead of an invisible failure

## Added scope gate: Object-objection proposal actionable

`object_objection_proposal_actionable` is now part of first playable prototype scope.

Required evidence:

- the proposal deck prioritizes an open proposal linked to an `OIR-...` response
- proposal-deck action rows record `source_object_response_id`
- support consumes only the proposal's own material requirements
- missing materials produce preserved shortage state, not spawned resources
- project, construction, completion, or worksite rows carry `related_object_response_id`
- resident work can repair or stabilize components only through accepted proposal work
- no direct command, hidden-law exposure, resource spawning, or tech-tree unlock occurs

## Added scope gate: Object-objection resolution recheck

`object_objection_resolution_recheck` is now part of first playable prototype scope.

Required evidence:

- resident project work linked to an object objection creates an `OIRR-...` resolution row
- the original `OIR-...` response records resolution status and follow-up project/construction ids
- the blocked object-interaction row records `proposal_resolution_id`
- resolution status requires resident recheck instead of directly allowing handling
- `handling_auto_allowed=false` is preserved
- physical work must be visible as repaired or added components, or as a preserved pending watch state
- no direct command, hidden-law exposure, resource spawning, or tech-tree unlock occurs

## Added scope gate: Object-objection recheck response

`object_objection_recheck_response` is now part of first playable prototype scope.

Required evidence:

- a later object inspection reads an existing `OIRR-...` resident recheck requirement
- the resident produces `post_resolution_recheck` or `recheck_still_blocks`
- `post_resolution_recheck` can reroute handling through careful resident action
- `recheck_still_blocks` preserves the block if the object remains unsafe or socially unavailable
- interaction rows record `resident_recheck_result`
- `handling_auto_allowed=false` remains preserved
- no LLM, open-ended language, direct command, hidden-law exposure, resource spawning, or tech-tree unlock occurs

## Added scope gate: Object-objection save/return persistence

`object_objection_save_return_persistence` is now part of first playable prototype scope.

Required evidence:

- save slots record object interaction rows, object response rows, object resolution rows, and object recheck-response rows
- save slots record latest `OIRR-...` resolution id and latest recheck response id
- restore logs report restored object resolution rows and recheck-response rows
- return journal snapshots show object-chain state before save, after away time, and after restore
- first-playable session snapshots preserve object-chain counts across Journal, Save, and Return steps
- the saved/restored object chain remains resident-mediated and does not expose hidden law or create direct object permission

## Added scope gate: Object-objection guided next step

`object_objection_guided_next_step` is now part of first playable prototype scope.

Required evidence:

- the Player guide can derive an object-chain phase from active `OIR/VBP/OIRR` state
- normal action options carry object-chain phase, next action, resolution id, and recheck result
- Follow can advance the next object-chain step through existing resident-mediated actions
- Follow rows record object response id, proposal id, resolution id, and recheck result
- guided object steps do not assign jobs, grant direct object permission, expose hidden law, or unlock technology

## Added scope gate: Object-objection canvas cue

The first playable scope now requires object-objection chain state to be visible in the normal primary surface/canvas cue model.

Evidence required:
- at least one `object_objection_canvas_cue` acceptance row
- canvas cue text containing active object-chain phase and next action
- linked `OIR`, `VBP`, or `OIRR` identifiers where present
- normal view keeps hidden law out of the player-facing cue
- the avatar still influences conditions through resident-mediated actions instead of direct command

## Added scope gate: Handling selected-component binding

The first playable scope now requires normal `Handling` to bind to the object the player selected or the primary surface is focused on when feasible.

Evidence required:
- at least one `handling_selected_component_binding` acceptance row
- resident material handling row with `selected_component_bound=true`
- `target_source` is `canvas_selection` or `primary_surface`
- handling remains resident-mediated and can fail under material/body/tool constraints
- normal view does not expose hidden law or grant direct object control

## Added scope gate: Material state save/return continuity

The first playable scope now requires handled physical components to survive save/return with explicit continuity evidence.

Evidence required:
- at least one saved handled-component fingerprint
- at least one return row where restored material state matches the saved fingerprint
- saved and restored rows identify component ID, handling action, target source, and body step where available
- continuity is derived from restored world state, not a separate fake counter
- normal view does not expose hidden material law

## Added scope gate: Normal handling practice emergence

The first playable scope now requires ordinary player `Handling` to be able to create or refine an emergent practice node through resident material manipulation.

Evidence required:
- at least one `normal_handling_practice_emergence` acceptance row
- a normal action rail row with `verb=handling`, a material handling ID, and a linked practice ID
- practice evidence comes from resident-mediated manipulation, not a predeclared tech tree
- primary surface carries the latest handling-derived practice cue
- normal view preserves no direct command and no hidden-law exposure

## Added scope gate: Normal-action resident-generated test

The first playable scope now requires ordinary player actions to be able to generate resident-authored tests from lived bottlenecks.

Evidence required:
- at least one `normal_action_resident_generated_test` acceptance row
- a normal action rail row with ordinary bottleneck feed, proposal, and test IDs
- a matching auto-generated test row linked to the normal action
- no predeclared invention and no correct concept installed
- normal view preserves resident interpretation and hidden-law separation

## Added scope gate: Normal test reaches village board

The first playable scope now requires resident-generated tests from ordinary play to enter diegetic village management.

Evidence required:
- at least one `normal_test_reaches_village_board` acceptance row
- a `VBP-NAT-...` proposal linked to a normal action and resident test
- proposal card fields include source normal action, resident test, and auto-test IDs
- avatar can ask/support/wait but cannot force the resident project
- no hidden-law exposure and no tech-tree unlock

## Added scope gate: Normal-test proposal actionable

The first playable scope now requires normal-action resident tests to become actionable resident work, not just board cards.

Evidence required:
- at least one `normal_test_proposal_actionable` acceptance row
- normal-test support event with `forced=false`
- project row linked to a resident test ID
- worksite row linked to the same normal-test path
- visual construction cue linked to the normal-test path
- no hidden-law exposure, no resource spawning, and no direct command

## Added scope gate: Normal-test save/return continuity

The first playable scope now requires normal-action resident-test project chains to persist across save/return.

Evidence required:
- at least one `normal_test_save_return_continuity` acceptance row
- saved normal-test chain includes resident test, board proposal, project, worksite, and visual evidence
- restored normal-test chain fingerprint matches the saved fingerprint
- evidence is recomputed from restored world state, not a detached counter
- no hidden-law exposure or direct command is introduced

## Added scope gate: Normal-test guided next step

The first playable scope now requires normal-action resident-test chains to have a guided next-step path through the normal action rail.

Evidence required:
- at least one `normal_test_guided_next_step` acceptance row
- normal action rail option or Follow row with normal-test phase and next action
- linked normal action ID, resident test ID, and board proposal ID
- Follow remains resident-mediated and cannot force work
- no hidden-law exposure and no tech-tree unlock

## Added scope gate: Normal-test canvas cue

The first playable scope now requires normal-action resident-test chains to be visible in the main primary surface/canvas cue model.

Evidence required:
- at least one `normal_test_canvas_cue` acceptance row
- primary surface snapshot includes normal-test phase, next action, test ID, and board proposal ID
- canvas cue ledger includes normal-test chain text
- normal view keeps hidden simulator law out of the player-facing cue

## Added scope gate: Normal-test visible resident expression

`normal_test_visible_resident_expression` is now part of first playable prototype scope.

The first playable path should show that resident-generated tests are embodied social events, not only ledger rows. A normal action that becomes a resident test must be able to produce:

- proposal-stage expression evidence
- support-stage expression evidence
- project/work-stage expression evidence
- canvas/player-surface expression cue
- no hidden-law exposure in normal view
- no direct avatar command
