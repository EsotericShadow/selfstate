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
- Stochastic entropy or failure probability when randomness influences outcome.
- Resulting damage, stability, position, or maintenance obligation.

This keeps the game from faking life through dramatic text. Residents may misunderstand the event, but the simulation still needs a physical cause.
