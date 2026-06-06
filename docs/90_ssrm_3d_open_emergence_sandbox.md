# SSRM-3D Open Emergence Sandbox

## Purpose

This page is a live interactive sandbox for the next SSRM-3D direction: agents acting in an open settlement world without assigned roles or replayed traces.

It is not a canonical experiment report. It is not part of the manifest evidence stack yet. It is a prototype viewer for testing what the next serious benchmark needs to support.

## What changed

The sandbox removes the fixed-role replay structure from the settlement/civilization visualization. Agents now start with:

- inherited traits;
- an inherited biological reserve;
- aging rate and accumulated stress;
- health, energy, hunger, thirst, trust, attachment, fear, and stress;
- online neural action policies;
- learned skill values;
- generic action primitives rather than assigned jobs;
- body-made sound patterns and invented sound tokens;
- private belief maps, short memory traces, attention state, and deliberation summaries;
- persistent ASCII glyph marks placed in the world for resources, paths, danger, shelter, repair, and tools;
- abstract receptive/pair-bond state;
- gestation, offspring, dependent-care, and death pressure.

The world is larger than the prior live prototype and has multiple functional shelters:

- home shelter;
- ridge shelter;
- grove shelter;
- water source;
- clinic;
- garden;
- workshop;
- commons;
- frontier;
- mineral field;
- forest;
- creek;
- ruins;
- badlands.

Resources are farther apart and visually distinct. The viewer now uses a larger top-down map with terrain patches, forest props, mineral rocks, ruins, frontier formations, shelter differences, life reserve, cell-repair debt, carrying state, dependents, births, sound field, and per-agent inferred specializations.

The current action layer is deliberately primitive:

- `inspect`;
- `harvest`;
- `carry`;
- `construct`;
- `repair`;
- `modify`;
- `strike`;
- `treat`;
- `signal`;
- `share_pattern`;
- `rest`;
- `pair_bond`;
- `nurture_child`.

Those primitives are not social roles. For example, `construct` can improve a shelter, garden, purifier, workshop, or tool cache depending on material availability and world need. `strike` can damage a nearby agent or a structure, and can become lethal under repeated conflict, but it also lowers trust and raises conflict.

## Cognition, language, and marks

The sandbox now adds a lightweight cognition layer. Each live agent carries:

- imperfect private beliefs about places, value, danger, and recency;
- current emotion, motive, attention target, uncertainty, and plan text;
- a short thought trace and durable memory trace;
- an invented sound lexicon that maps concepts such as water, food, danger, child, shelter, illness, and repair to local tokens;
- learned token meanings from hearing other agents;
- learned glyph meanings from reading marks in the world.

Sounds and glyphs are grounded in consequences. A signal can teach nearby agents a token meaning, raise fear, increase attachment, unlock a relevant action, or spread attention. A glyph persists in the terrain and can teach future agents where food, water, danger, shelter, tools, or repairs matter. Optional browser audio turns emitted sound tokens into short synthesized tone sequences after the user enables audio.

## Current balance pass

The enlarged map needs slower life-clock constants than the smaller prototype. The current sandbox therefore uses:

- longer inherited biological-reserve time constants;
- lower passive hunger, thirst, sickness, shelter-wear, and tool-wear rates;
- emergency harvesting that routes agents to the nearest relevant water, food, or material source;
- rest and treatment paths that repair health, stress, and cell-repair debt;
- stricter pair-bond/reproduction conditions so dependents appear after a viable settlement exists;
- strike suppression under low-conflict conditions, while still allowing violence when scarcity, fear, or conflict actually rise.

This keeps death possible without causing immediate whole-population collapse before agents can learn or specialize.

## What this tests informally

The sandbox is useful for design pressure, not final evidence. It tests whether the public-facing world can expose control-relevant life functions:

- reproduction is costly rather than a free population increase;
- carrying reduces reserve and energy;
- offspring create dependent-care pressure;
- aging and stress drain biological reserve;
- poor shelter, illness, scarcity, and conflict shorten viable lifespan;
- sound can spread attention and discovered action knowledge;
- invented language and glyphs can alter attention, trust, fear, learned meanings, and action availability;
- agents can construct, repair, modify, damage, injure, or kill through generic physical/social interfaces;
- specializations emerge from action history rather than assigned roles.

## What this does not claim

This is not subjective consciousness.

This is not proof that selfhood emerged.

This is not closed-loop deep reinforcement learning.

The browser sandbox uses lightweight online neural learners and hand-built world dynamics. It should be treated as a design scaffold for the next physics/training benchmark, not as standalone research proof.

## How to run

From the repo root:

```bash
python3 -m http.server 8876
```

Then open:

```text
http://127.0.0.1:8876/visualizations/ssrm_3d_open_emergence.html
```

## Next serious step

The next evidence-bearing version should move this from viewer-side JavaScript into the modular simulation/training stack:

- physics-derived observations;
- closed-loop learned control;
- held-out world layouts;
- no scenario labels;
- ablations of self-state, body state, social memory, sound, shelter memory, life reserve, and dependent-care state;
- replayable intervention logs.

Only then should this become a canonical report instead of a sandbox.
