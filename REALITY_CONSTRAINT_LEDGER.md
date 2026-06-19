# Reality Constraint Ledger

## Purpose

The Reality Constraint Ledger keeps the simulation causally grounded. It prevents dramatic text from replacing cause, cost, and traceability.

## Required ledger categories

- Material sources.
- Material transformations.
- Time cost.
- Labor or attention cost.
- Tool wear.
- Resident effort or fatigue.
- Weather, moisture, heat, or storage effects where relevant.
- Mass, gravity, support, contact/collision, friction, and failure pressure where physical objects change.
- Component position, stability, damage, and repair state where structures are involved.
- Hidden law involved.
- Public observation.
- Resident interpretation.
- Conservation check.
- Maintenance obligation created.
- Unintended consequence.

## Core invariants

- No effect without cause.
- No resource spawning.
- No work without time, labor, material, or attention.
- No recovery without cost, care, time, or stabilization.
- No construction without materials and maintenance.
- No structure without components, support, and physical affordances.
- No physical change without force, contact, material transformation, decay, work, or stochastic failure trace.
- No invention without observation, practice, material, failure, and transmission.
- No hidden law appearing as resident belief without evidence or teaching.

## Hidden law versus resident belief

The simulator can maintain stable hidden laws. Residents only receive observations and consequences. Resident beliefs may be wrong, partial, ritualized, disputed, useful, or forgotten.

Audit mode can reveal hidden laws. Normal player view should not.

## Physics ledger rows

When physics changes the world, the ledger should preserve:

- Object or component IDs.
- Material IDs and material source.
- Mass or weight when relevant.
- Support source and support capacity.
- Contact/collision pair and impulse where relevant.
- Friction or resistance where relevant.
- Moisture, decay, heat, or fatigue pressure where relevant.
- Stochastic field state: moisture, heat, wind, decay pressure, and structural stress where modeled.
- Energy/work proxy rows where gravity, stress, or decay changes the world.
- Stochastic entropy or failure probability when randomness influences outcome.
- Resulting damage, stability, position, or maintenance obligation.
- Project construction rows linking consumed resources to repaired or added components.

This keeps the game from faking life through dramatic text. Residents may misunderstand the event, but the simulation still needs a physical cause.

The ledger should treat physical field updates as first-class causal rows. A practice, proposal, refusal, repair, or deep-time survival change should not appear from narrative intent alone; it should point back to field pressure, material properties, resident effort, social transmission, or another inspectable causal source.

## Project construction ledger rows

When a resident project changes a structure, the ledger should preserve:

- Proposal ID and project work row.
- Resident proposer and who felt the work.
- Materials consumed from the commons.
- Components repaired.
- Components added.
- Structure ID affected.
- Resident term and player gloss.
- Maintenance obligation created.
- Confirmation that no fixed building asset or resource spawning occurred.

## Resident manipulation ledger rows

When a resident physically handles a component, the ledger should preserve:

- Manipulation row ID.
- Resident who handled the component.
- Action attempted: carry, drop, stack, tie, dry, wet-test, or test.
- Component ID, material ID, resident term, player gloss, and affordance.
- Mass and carry capacity when movement is attempted.
- Resource cost such as water or fiber.
- Before/after position, moisture, temperature, damage, stability, stress, and carried-by state.
- Whether the action succeeded or failed.
- Failed handling reason and recoverability.
- Public observation and resident interpretation.
- Linked physics step.
- Practice node link if repeated handling stabilized into evidence.

This prevents handling from becoming animation-only. A resident touching the world must leave material, social, and audit traces.

## Deep-time stochastic physics ledger rows

Compressed history must still obey material causality. A deep-time epoch should preserve:

- Physical substeps linked to support, contact, gravity, field stress, and stochastic fatigue.
- Material flux rows for mass loss, moisture shift, heat shift, damage, stability, settlement, and ruined traces.
- Resource pressure caused by drought, wetness, decay, wear, or ruined components.
- Lineage pressure created by the physical components a practice depends on.
- No-effect-without-cause and no-resource-spawning flags.
- Hidden-law audit separation from resident belief and player normal view.

Long-run civilization survival should read from these rows. A culture cannot remain viable merely because a lineage says it survived; its materials, structures, maintenance burden, and recovery capacity must also survive or leave trace evidence.

## Resident body physics ledger rows

Residents should not be weightless action labels. When a resident moves, works, rests, carries, tests, or avoids, the ledger should be able to preserve:

- Resident body step ID.
- Resident, action, and source.
- Body position, velocity, fatigue, balance, footing, load, carry capacity, and recovery debt before/after.
- Terrain moisture, field stress, friction, slope, and target location.
- Component contacts and resident contacts.
- Slip risk, slip event, overload, fatigue delta, and safety delta.
- Bounded recovery path when slips, overload, or fatigue accumulate.
- Confirmation that the player did not directly command the body.
- Hidden-law audit separation from resident normal view.

This keeps resident motion grounded in physics. Body language should be visible expression of position, effort, load, footing, and safety pressure, not a detached animation toggle.

## Terrain physics ledger rows

The ground should be simulated, not just painted. Terrain ledger rows should preserve:

- Terrain step ID and source.
- Cell moisture, slope, drainage, compaction, erosion, vegetation, walkability, support capacity, and height.
- Weather input, evaporation, neighbor moisture flow, body pressure, and component pressure.
- Which cells became weak, wet, hard to walk, or structurally poor.
- Resource pressure caused by weather or terrain, not resource spawning.
- Component stability or damage changes caused by weak/wet ground.
- Resident body footing and slip-risk changes caused by terrain.
- Hidden-law audit separation from resident normal view.

This lets routes, work yards, storage ground, and shelter ground become physical conditions that residents can adapt to, repair, avoid, ritualize, or misunderstand.

## Tool/work physics ledger rows

Tool work must satisfy:

- no work without a physical tool or embodied handling path
- no tool use without wear pressure
- no repair without material cost
- no blocked project without a recorded cause
- no hidden-law exposure in normal player view

Ledger rows now include `tool_work_physics`, with tool fit, wear delta, damage delta, failure probability, stochastic threshold, repair status, and conservation flags.

## Resource-stock physics ledger rows

Resource stock work must satisfy:

- no resource without a source or stored stock
- no resource loss without weather, storage, decay, leak, fatigue, or use pressure
- no care recovery without rest, trust, or reduced fatigue
- no stock change without a transform row
- no hidden-law exposure in normal player view

Ledger rows now include `resource_stock_physics`, with stock before/after quantities, weather, field values, causal terms, stochastic term, loss/gain rows, conservation flags, and resident-facing interpretation.
