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
- One stochastic consequence and recovery loop.
- One save/return loop.
- One audit/replay mode.
- One normal player-facing interface.
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
