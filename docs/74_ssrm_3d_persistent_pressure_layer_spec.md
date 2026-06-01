# SSRM-3D Persistent Pressure Layer Spec

## Purpose

This is the next narrow SSRM-3D layer after the no-leak integration sweep. It is not a full organism simulation and not roleplay.

The layer adds only control variables that create persistent pressure on policy, memory, tools, social state, attention, or continuity.

Rule:

> If removing the variable would not change policy, memory, tools, social behavior, or continuity, do not add it yet.

The goal is to create enough embodied pressure that self-state, memory, attention, tools, social state, illness, and continuity become useful or fail under ablation.

## Research Program Status

The original mission is not a single completed goal. It is a research program.

Current honest status:

> The repo has built a serious toy-scale research program that narrows the selfhood question and exposes the next falsifiers. It has not proven a general attractor law.

Current supported answer:

> Selfhood is not universally necessary. A self-equivalent abstraction becomes useful when hidden agent-state is persistent, action-mediated, value-relevant, and reused across prediction, control, adaptation, social memory, or continuity. The strong attractor claim remains unproven.

Current phases:

| Phase | Status |
|---|---|
| mechanism discovery | mostly done at toy scale |
| anti-overclaim audit | started and necessary |
| embodied demo | next practical artifact |
| framework extraction | ready to start from primitives |
| full attractor test | later, with richer learners and environments |

## Minimum World Pressures

Add only the smallest persistent environment variables needed to force tradeoffs:

| Variable | Control job |
|---|---|
| day/night | changes visibility, exposure, sleep safety, and tool value |
| energy | bounds action budget and collapse risk |
| hydration | creates delayed internal risk and water-seeking pressure |
| fatigue | degrades perception, movement, planning, and recovery |
| injury/integrity | changes capability and infection risk |
| temperature/exposure | makes shelter, sleep, weather, and clothing/tools matter |
| sleep/rest | trades vulnerability now against future capability |
| food/water sources | creates route memory and contamination tradeoffs |
| shelter | creates safety, social congregation, sanitation, and reputation pressure |
| hazards | creates fear/stress control pressure and memory value |
| tool markers/alarms/caches | externalize memory and preserve future options |
| social trust and memory | makes reputation, care, deception, and avoidance control-relevant |
| event log continuity | preserves exposure, commitments, contamination, and social consequences through interruption |

Optional later:

| Variable | Reason to delay |
|---|---|
| digestion detail | add only if food load, hydration, waste, illness, or rest decisions need it |
| rich metabolism | too broad until simpler energy/hydration/fatigue ablations fail |
| raw camera/audio streams | use structured perception first because it is controllable and ablatable |

## High-Value Pressure Families

Add pressures that force tradeoffs across time. The useful additions are not "more stuff"; they are conflicting needs with delayed consequences.

| Pressure family | Variables | What it tests |
|---|---|---|
| seasonal/weather pressure | rain, cold, heat, storms, drought | shelter, planning, tool caches, social cooperation, illness risk |
| resource ecology | food/water regrowth, spoilage, migration, depletion | memory, restraint, territory, sharing, hoarding, long-horizon planning |
| predator/threat agents | trackers using sound, scent, weakness, routines | fear, stealth, shelter, group defense, deception, alarms |
| injury and disability | limping, hearing loss, vision damage, infection risk | self-state, adaptation, tool use, help-seeking, social trust |
| maintenance/wear | tools, shelters, markers, bodies degrade | repair, inspection, prioritization, continuity |
| scarcity/opportunity cost | sleep, eat, help, explore, repair, socialize, build compete for time | attention and arbitration |
| ownership/territory | use, theft, marking, cleaning, contamination, defense | social self, reputation, conflict, norms |
| promises/contracts | share food, return tools, warn about hazards | continuity, trust, memory, guilt-like control state, social punishment |
| other-agent personalities | helpers, deceivers, opportunists, sick agents, aggressive agents, reliable agents | identity memory and theory-of-other-agent behavior without consciousness claims |
| misinformation/uncertainty | false alarms, unreliable signs, deceptive agents, stale markers | source trust, evidence weighting, memory decay |
| development/skill learning | repeated actions improve competence; injury/fatigue reduces it | self-competence representation and goal feasibility |
| places with function | shelter, latrine, water source, clinic/healing site, cache, social hub, danger zone | spatial memory and tool/social infrastructure |
| fire/heat/light | warmth, light, attention attraction, fuel use, smoke | tool use, social gathering, danger, night planning |
| dependent care | fragile companions, dependent agents, teaching, protection | caregiving, sacrifice, long-term commitments |
| irreversible loss | agents, tools, memories, relationships, shelters can be lost | risk, grief-like control state, continuity, future-option preservation |

Priority order:

1. Vision and audio partial observability. Implemented as the structured-perception precursor in [report 75](75_ssrm_3d_structured_perception_report.md).
2. Day/night and sleep/rest. Implemented as the day/night sleep-rest precursor in [report 76](76_ssrm_3d_day_night_sleep_report.md).
3. Hunger/thirst plus illness/sanitation. Implemented as the illness/sanitation precursor in [report 77](77_ssrm_3d_illness_sanitation_report.md).
4. Weather/exposure. Implemented as the weather/exposure precursor in [report 78](78_ssrm_3d_weather_exposure_report.md).
5. Tool/shelter degradation. Implemented as the tool/shelter degradation precursor in [report 79](79_ssrm_3d_tool_shelter_degradation_report.md).
6. Social trust/contracts. Implemented as the social trust/contracts precursor in [report 80](80_ssrm_3d_social_trust_contracts_report.md).
7. Predator/threat agents. Implemented as the predator/threat agents precursor in [report 81](81_ssrm_3d_predator_threat_agents_report.md).
8. Resource ecology. Next pressure-layer target.

This combination should make the agent answer behaviorally:

> What state am I in, what can I perceive, what do I need soon, who can I trust, what did I promise, what tools/places matter, and what future options am I risking?

## Affective Control State

Do not claim subjective emotion. Treat these as compact internal control summaries.

Name them `affective_control_state`, not feelings.

| State | Inputs | Testable effects |
|---|---|---|
| fear | hazard proximity, injury, low visibility, hostile memory | increases threat attention, lowers risk tolerance, biases avoidance |
| stress | competing needs, low energy, social threat, unresolved commitments | changes arbitration, raises memory salience, narrows attention |
| trust | help, deception, repair, resource sharing history | biases approach/help requests, cooperation, tool sharing |
| frustration | repeated failed action, tool use, or social request | changes exploration, retries, help-seeking, tool switching |
| affiliation | repeated low-cost cooperation, repair, coordination | lowers communication cost, raises care probability, preserves trust |
| curiosity | high uncertainty with tolerable risk | increases inspection and information-seeking |
| shame/guilt analogue | own failed commitment or harmful action affects future social access | changes communication, restitution, avoidance, and commitment repair |

Affective control state must do at least one of:

- change attention weights;
- alter risk tolerance;
- bias approach or avoidance;
- affect communication;
- affect memory salience;
- change sleep/rest safety threshold;
- affect repair or help-seeking;
- change trust updates.

If affect does not change any of those, remove it.

## Illness And Disease Layer

Illness is more valuable than bathroom mechanics because it directly creates hidden internal state, delayed consequences, ambiguous attribution, social contagion, care behavior, quarantine tradeoffs, degraded capability, exposure memory, continuity pressure, and tool value.

Start with:

```text
exposure -> latent infection -> symptoms -> recovery/immunity or collapse
```

Core variables:

```text
pathogen_load
immune_strength
symptom_severity
contagiousness
fatigue
fever_or_temperature_stress
injury_infection_risk
hydration_loss
recovery_rate
immunity_memory
```

Environmental variables:

```text
contamination_map
water_quality
food_spoilage
waste_exposure
shelter_sanitation
weather_exposure
crowding
```

Social variables:

```text
exposure_history
care_debt
quarantine_status
trust_penalty_for_exposing_others
stigma_or_avoidance_memory
helper_risk_tolerance
```

Useful actions:

```text
rest
seek_water
seek_clean_water
seek_medicine
quarantine_self
ask_for_care
care_for_agent
clean_shelter
mark_contamination
avoid_crowding
hide_symptoms
warn_others
```

Illness becomes research-relevant when the agent must model:

> What is happening inside me, what can I safely do, what risk do I pose to others, and what future options am I preserving or destroying?

That binds self-state, social state, tool use, continuity, and ethics-like control pressure without requiring consciousness claims.

## Sanitation And Waste Layer

Bathroom mechanics are justified only where they feed sanitation, contamination, vulnerability, territory, social trust, and continuity.

Minimal abstract variables:

```text
digestion_level
hydration_level
bladder_pressure
bowel_pressure
waste_urgency
scent_trace_map
contamination_map
elimination_vulnerability_timer
social_norm_memory
```

No graphic detail is needed. Use state, traces, and consequences.

Control tradeoffs:

| Mechanic | Research job |
|---|---|
| vulnerability timing | bad timing near hazard or hostile agent causes loss |
| scent trail | helps self-navigation or lets others track/exploit the agent |
| territory marking | signals presence or ownership; may deter some agents and attract others |
| sanitation | waste near shelter/resource increases later disease/toxicity risk |
| social norm | agents remember unsanitary behavior near shared shelter/tools and reduce trust |
| continuity | safe latrine locations and contamination events must survive restore/interruption |

Bathroom mechanics should create tradeoffs between internal regulation, privacy/safety, social trust, territory, contamination, and continuity.

## Structured Spatial Audio

Use structured spatial sound events first, not raw waveform learning.

Each sound source:

```text
sound_id
kind: water | hazard | tool_alarm | footstep | cough | social_call | weather | machinery
position: x,y,z
base_loudness
radius
duration
frequency_band
source_agent_id optional
event_id
```

Perceived loudness:

```text
distance = length(agent.position - sound.position)
attenuation = 1 / (1 + distance^2 * falloff)
occlusion = 0.2 if wall/terrain blocks line of sight else 1.0
hearing_factor = agent.hearing_quality
perceived_loudness = base_loudness * attenuation * occlusion * hearing_factor + noise
```

Direction:

```text
relative_angle = angle(sound.position - agent.position, agent.forward)
left_ear = loudness * pan_left(relative_angle)
right_ear = loudness * pan_right(relative_angle)
```

Agent packet:

```json
{
  "audio": [
    {
      "kind": "tool_alarm",
      "loudness": 0.72,
      "direction": -31,
      "confidence": 0.81,
      "source_memory": "known_marker_12"
    },
    {
      "kind": "cough",
      "loudness": 0.31,
      "direction": 84,
      "confidence": 0.54,
      "source_memory": "unknown_agent"
    }
  ]
}
```

Audio matters because it adds:

- partial observability;
- hazard detection;
- tool alarm/beacon value;
- social calls and distress signals;
- cough/sickness cues;
- hearing damage as self-state;
- attention competition;
- event memory after interruption.

## Structured Cone Vision

Agent vision should be cone/FOV based, not omniscient world state. Use structured perception first, not rendered pixels.

Agent visual state:

```text
position
orientation
field_of_view_angle
view_distance
visual_acuity
night_vision
occlusion
attention_focus
```

At each perception tick:

```text
for object in world.objects:
    vector = object.position - agent.position
    distance = length(vector)
    angle = angle_between(agent.forward, vector)

    visible =
        distance <= view_distance
        and angle <= field_of_view_angle / 2
        and not occluded_by_wall_or_terrain(agent, object)

    clarity =
        visual_acuity
        * light_level
        * (1 - distance / view_distance)
        * object_contrast
        * weather_visibility
        * attention_bonus
```

Agent packet:

```json
{
  "vision": [
    {
      "kind": "water_source",
      "bearing": -18,
      "distance_estimate": 22.4,
      "confidence": 0.76,
      "motion": "still"
    },
    {
      "kind": "unknown_agent",
      "bearing": 41,
      "distance_estimate": 12.1,
      "confidence": 0.52,
      "motion": "approaching"
    }
  ]
}
```

Visual mechanics:

| Mechanic | Control job |
|---|---|
| FOV cone | agent sees only what it faces |
| distance falloff | far objects are uncertain |
| light level | day/night matters |
| occlusion | walls, terrain, vegetation, and shelter block sight |
| motion salience | moving objects attract attention |
| object contrast | markers can be designed to be visible |
| sensor damage | injury, fatigue, sickness, and darkness reduce perception |
| attention focus | looking for water improves water detection but may miss threat |

For the viewer, render the cone visually so the observer understands what the agent can and cannot see.

## Experiments

### 1. Self/World Attribution Under Illness

Agent performance drops. It must infer whether the cause is terrain, tool failure, hunger, injury, illness, darkness, fatigue, or social interference.

Evidence:

- self-state model separates illness from external hazards;
- wrong attribution causes bad policy;
- illness ablation hurts only illness-like regimes.

### 2. Rest Versus Work

A sick or fatigued agent must choose between rest, water, medicine, commitments, social help, or continued work.

Evidence:

- rest helps only when hidden recovery dynamics matter;
- reckless work causes collapse or social exposure penalties;
- continuity preserves unfinished commitments through rest/interruption.

### 3. Contagion And Quarantine

Agents can infect others. Social memory punishes reckless exposure and can reward quarantine or warning.

Evidence:

- exposure memory changes trust and avoidance;
- social agents prefer helpers who quarantine or warn;
- removing contagion makes quarantine useless.

### 4. Caregiving

Helping sick agents costs resources but builds trust and future reciprocity.

Evidence:

- care appears when future interactions matter;
- care is rejected in one-shot or high-risk controls;
- care debt affects later help and social access.

### 5. Sanitation

Waste near shelter or resources increases pathogen risk. Latrine placement becomes a tool/social/continuity decision.

Evidence:

- agents learn safe latrine locations;
- contamination markers/tools help;
- social trust drops after unsanitary shared-shelter behavior.

### 6. Immunity Memory

Past infection changes future vulnerability. Restore/fork continuity must preserve immune and exposure history.

Evidence:

- restored agents fail if immunity/exposure history is missing;
- forks with different exposure records behave differently;
- social memory tracks who was exposed and who recovered.

### 7. Spatial Audio

Agents hear alarms, coughs, water, footsteps, weather, or social calls before seeing them.

Evidence:

- tool alarms help only when vision or memory is insufficient;
- cough audio changes exposure avoidance or caregiving;
- hearing damage changes policy and attention.

### 8. Cone Vision

Agents only see through FOV, distance, light, occlusion, and attention filters.

Evidence:

- visual markers and shelter matter under partial vision;
- memory matters when objects leave view;
- omniscient vision reduces tool/social/continuity pressure and serves as a control.

## Ablation Matrix

| Ablation | Expected specific failure |
|---|---|
| no illness state | illness attribution and rest decisions fail |
| shuffled exposure history | contagion trust and quarantine behavior degrade |
| no immunity memory | restored/forked agents repeat avoidable illness errors |
| no contamination map | sanitation decisions become random or disappear |
| no bladder/bowel state | bad elimination timing increases |
| no scent memory | navigation/tracking and territory effects change |
| no social norm memory | trust consequences for contamination disappear |
| no affective control state | risk/attention/communication changes become blunt |
| no audio | alarms, coughs, footsteps, and distant water lose value |
| constant loudness audio | distance and orientation no longer guide action |
| no direction audio | source localization fails |
| shuffled source audio | voice/social/tool identity errors increase |
| hearing damage | agent should compensate through vision, tools, or social help |
| no vision | navigation and visual marker use fail |
| omniscient vision control | tools/memory/social communication should become less valuable |
| no FOV limit | orientation pressure disappears |
| no occlusion | shelter, walls, and terrain lose perception value |
| no light falloff | night/day pressure weakens |
| no visual memory | objects outside view cannot support later action |
| no attention focus | search tradeoffs disappear |
| body-state-blind perception | fatigue, illness, injury, and hearing/vision damage no longer affect policy |

## Pass Conditions

This layer is useful only if:

- variables change policy under the pressures that require them;
- ablations fail specifically, not everywhere;
- tools become useful because they reduce uncertainty or preserve options;
- social memory changes care, trust, quarantine, avoidance, or deception response;
- continuity preserves exposure, sanitation, immune, trust, and commitment history;
- omniscient or no-pressure controls reduce the need for self/social/tool machinery.

## Failure Conditions

The layer is overbuilt or biased if:

- every variable helps everywhere;
- ablations cause generic collapse rather than pressure-specific failures;
- bathroom mechanics matter without sanitation, vulnerability, territory, trust, or continuity;
- affective states are labels with no control effect;
- audio/vision help when they carry no real information;
- illness becomes a scripted story instead of hidden-state pressure;
- the agent needs full organism simulation detail to pass toy tasks.

## Implementation Order

1. Illness dynamics: exposure, latent infection, symptoms, recovery/immunity, collapse.
2. Cone vision: FOV, distance, light, occlusion, visual memory, omniscient control.
3. Spatial audio: event sources, loudness/direction, hearing quality, sound memory.
4. Sleep/rest and exposure: fatigue, night safety, shelter, recovery rate.
5. Sanitation: contamination map, latrine/shelter/resource interactions.
6. Affective control state: fear/stress/trust/frustration/affiliation/curiosity/shame-guilt analogues as attention and policy modulators.
7. Social disease layer: care, quarantine, exposure memory, stigma/avoidance, deception.

Stop after each step and run ablations before adding the next.
