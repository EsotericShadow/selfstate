# SSRM-3D Long-Horizon Adaptation Sandbox

## Purpose

This note records the first pass toward an overnight-scale live sandbox.

The goal is to stop the open-emergence viewer from behaving like a short dramatic loop. At `1x`, the world now has a 12-hour development phase before autonomous major shocks are allowed. Agents can still face small pressures immediately, but large world events are delayed so infrastructure, skills, symbols, influence, and knowledge transmission have time to develop.

## What changed

The sandbox now separates pressure into two layers:

- slow continuous pressure;
- delayed major shocks.

Slow pressure starts immediately:

- hunger and thirst drift slowly;
- weather changes over hour-scale intervals;
- soil fertility, contamination, visibility, temperature, wind, rainfall, and route hazard change gradually;
- shelters, paths, tools, storage, waterworks, and architecture wear down slowly;
- agents adapt through repeated actions, repairs, teaching, symbols, and infrastructure improvement.

Major shocks are gated:

- the first autonomous shock is locked until at least 12 simulated hours;
- after the gate opens, drought, blight, epidemic, structural failure, or frontier threat can occur;
- later shocks are spaced by additional multi-hour intervals.

The time slider can accelerate inspection, but at `1x` the system is meant to be watchable over an overnight run.

## New world variables

The long-horizon pass adds:

- architecture;
- tool design;
- food storage;
- path network;
- waterworks;
- teaching tradition;
- risk memory;
- soil fertility;
- contamination;
- temperature;
- visibility;
- wind;
- rainfall;
- route hazard;
- ecology volatility;
- resource migration;
- food, water, and material reliability;
- disease strain;
- social inequality;
- knowledge drift;
- adaptive pressure;
- adaptation evidence and quality;
- major shock countdown.

These variables are visible in the HUD and included in the agent policy input.

## Scientific pressure ledger

The follow-up pass adds a simple pressure ledger so the sandbox is not just harder in a vague way.

The ledger separates pressure into:

- survival pressure: hunger, thirst, reserve loss, sickness, contamination;
- ecology pressure: weather, temperature, visibility, route danger, resource movement;
- infrastructure pressure: shelter, architecture, tools, paths, waterworks;
- social pressure: trust, conflict, violence, dependents, unequal influence;
- uncertainty pressure: stale maps, resource migration, weak risk memory, weak symbol field.

The HUD reports adaptive pressure, accumulated pressure exposure, adaptation evidence, and adaptation quality. A result only counts as stronger evidence if agents survive shifting pressure through inspection, repair, construction, tool modification, treatment, sharing, care, and other long-horizon actions rather than by memorizing one route or repeating one loop.

This gives the later headless benchmark a falsifiable shape:

```text
same world seed + same pressure schedule
with self/body/memory/social channels vs ablated channels
measure survival, recovery, adaptation evidence, and post-shock function
```

## Wisdom as a scientific variable

This pass treats wisdom operationally.

Wisdom is not a claim about subjective experience. It is a control variable that increases when an agent succeeds at long-horizon actions such as:

- inspecting uncertainty;
- repairing;
- constructing;
- modifying tools;
- treating illness;
- sharing patterns;
- reducing future risk.

Wisdom affects influence and reserve cost. It is also partly transmissible through offspring and teaching tradition.

The intended measurable question is:

```text
Do agents with memory, symbols, social transmission, and self/body state become better at surviving delayed nonstationary pressure than agents without those channels?
```

## Knowledge transmission

Children no longer inherit direct human labels. They inherit:

- a small amount of parent skill;
- parent category/token/glyph exposure;
- culture-weighted wisdom and adaptation;
- risk memory through the world.

Adults can also transmit skill through `share_pattern`, which strengthens teaching tradition and improves later learning.

## What still remains designed

This is still a browser sandbox, not canonical evidence.

Still designed:

- the action primitives;
- the numeric pressure equations;
- the shock types;
- the visible HUD variables;
- the online learner architecture;
- the reward shaping.

The scientific version still needs:

- headless training;
- held-out worlds;
- no label leakage;
- ablations for wisdom state, teaching tradition, risk memory, architecture, tool design, symbol memory, knowledge drift, resource reliability, disease strain, and social inequality;
- multi-seed overnight/accelerated stress tests.

## Current status

This pass makes the live sandbox closer to the requested shape:

```text
early hours: development, exploration, learning, infrastructure
after 12h: major shocks and adaptation pressure
across generations: partial skill/symbol/wisdom transmission
```

It does not prove selfhood or consciousness.

## Browser audit hook

The visualization now exposes a machine-readable audit helper:

```js
window.ssrmOpenEmergence.longHorizonAudit()
```

The HUD also includes an `Audit 12h` intervention button. It runs the same helper, pauses the simulation at the final checkpoint, writes the JSON result to `document.body.dataset.ssrmAudit`, and shows a short pass/fail summary.

The helper pauses animation, optionally resets the population, advances the same simulation stepper to fixed checkpoints, refreshes the viewer, and returns:

- checkpoint snapshots at `1h`, `6h`, `12h`, `12.5h`, and `14.5h`;
- a verdict that no major shock occurred before `12h`;
- a verdict that no major shock occurred exactly at the `12h` gate;
- a verdict that a post-gate major shock occurred by the final checkpoint;
- a verdict that adaptation evidence accumulated;
- a verdict that at least one agent survived.

This is a browser-side audit of the live sandbox. It is stronger than watching the animation by eye, but it is still not the final scientific test. The next stronger version should move the same long-horizon pressure schedule into a headless multi-seed benchmark with ablations.

## Current browser-audit evidence

The tuned browser audit passed on the live page after the survival-arbitration fix.

| checkpoint | alive | major shocks | food | water | architecture | tool design | adaptation evidence |
|---|---:|---:|---:|---:|---:|---:|---:|
| `1h` | 10 | 0 | 0.763 | 0.832 | 0.261 | 0.208 | 0.098 |
| `6h` | 10 | 0 | 0.439 | 0.707 | 0.183 | 0.302 | 0.141 |
| `12h` | 10 | 0 | 0.308 | 0.400 | 0.275 | 0.731 | 0.438 |
| `12.5h` | 10 | 0 | 0.301 | 0.392 | 0.280 | 0.748 | 0.458 |
| `14.5h` | 10 | 1 | 0.355 | 0.261 | 0.443 | 0.839 | 0.632 |

Verdict:

- no major shock occurred before the 12h gate;
- no major shock occurred at the 12h gate;
- one post-gate major shock occurred by 14.5h;
- all 10 agents survived to 14.5h;
- adaptation evidence, architecture, and tool design increased across the run.

This verifies the current browser sandbox shape. It does not replace the needed headless multi-seed benchmark.
