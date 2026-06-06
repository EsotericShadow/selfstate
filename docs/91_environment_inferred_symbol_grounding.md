# Environment-Inferred Symbol Grounding

## Purpose

This note records the first pass away from hand-labeled symbolic behavior in the live SSRM-3D open-emergence sandbox.

The goal is not to claim that the agents now discover a full reality from raw physics. The goal is narrower: move sounds and glyphs away from direct labels such as `water`, `food`, or `danger`, and toward agent-local categories inferred from environmental signatures and outcomes.

## What changed

The sandbox now gives each place a numeric environmental signature over sensor channels:

- liquid;
- nutrient;
- structure;
- material;
- hazard;
- care;
- social;
- path;
- thermal.

Agents form private latent categories from those signatures. A category has:

- an agent-local id such as `C4.1`;
- a prototype vector;
- a count of matching observations;
- learned value and danger estimates;
- example places;
- a human-facing debug hint such as `fluid-like`, `material-like`, or `hazard-like`.

Sounds and glyphs now point to those category ids rather than directly to human concept labels. For example, a mark may show:

```text
()<> points to C4.1 (material-like)
```

The `C4.1` category is the agent-facing symbol target. The `material-like` text is a viewer/debug hint.

## What still remains designed

This is only the first de-ontology pass.

Still designed:

- the sensor channels;
- the environmental signatures assigned to places;
- the action set;
- the survival variables;
- the high-level pressure summaries used by the browser policy bridge;
- the viewer debug hints;
- the reward and outcome shaping.

Less directly hard-coded:

- sounds no longer point directly to `water` or `food`;
- glyphs no longer store direct concept meanings;
- listeners learn token/glyph meanings through category ids, confidence, proximity, and consequence;
- marks and utterances can unlock behavior through learned category hints rather than fixed literal labels.

## Influence and convention pressure

The next problem was that every agent could invent a different name for the same category and no name would catch on. That is realistic as a failure mode, but the world also needs social reality vectors that make conventions possible.

The sandbox now gives agents a small set of influence-relevant state variables:

- mental aptitude;
- physical aptitude;
- social presence;
- cleanliness;
- reputation;
- status capital;
- skill evidence;
- health and trust.

These are not assigned roles. They are attributes and outcomes that change under world pressure. A cleaner, healthier, more competent, more trusted, more successful agent tends to be more influential. Repeated sounds and glyphs also accumulate public weight in a symbol field. Later agents can adopt a convention when they have heard or seen it, or when the public field has become strong enough.

This is still designed social physics. The intended move is not "agent X is the leader." The intended move is:

```text
aptitude + outcomes + trust + repeated public use -> influence -> naming convergence pressure
```

That gives language a route to convergence without programming a single correct word into the agent.

## Why this matters

The earlier cognition layer was grounded in consequences but still too label-heavy. If a glyph literally stored `water`, the agent was not really building a symbol from experience.

This pass changes the representation boundary:

```text
old: glyph -> water
new: glyph -> C7.2 -> prototype/liquid-high/value-high -> viewer says fluid-like
```

That is still not raw-sensor symbolic culture, but it is closer to the desired shape: symbols become handles for learned environmental regularities.

## Next steps

The next implementation should remove more designed ontology:

- replace named actions with primitive operations;
- let marks be built from strokes rather than selected glyph strings;
- let sounds be built from pitch, rhythm, duration, and volume rather than syllables;
- replace the browser public symbol field with spatially local exposure, memory, and social contact graphs;
- move category learning into the headless training stack;
- evaluate held-out worlds where the same useful category appears with different visual/physical forms;
- add ablations for category memory, sound learning, glyph learning, and outcome-grounded symbol confidence.

The browser sandbox remains a live prototype. The evidence-bearing version needs trained controllers, held-out worlds, no label leakage in model inputs, and targeted ablation metrics.
