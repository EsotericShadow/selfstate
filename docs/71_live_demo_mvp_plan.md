# Live Demo MVP Plan

## Goal

Build a small persistent 3D demonstration that teaches the project in one moment:

> The user tells an agent to do something, and the agent refuses or redirects because its own continuity state makes another action better.

A chatbot obeys or answers. An inhabitant has context.

## Core Scene

Use a small persistent 3D aquarium:

- three agents;
- one route to a resource;
- one hazard;
- one marker or tool;
- one social helper/deceiver event;
- one pause/restore event;
- one inspector panel.

The world should keep ticking while the user does nothing.

## Hook Moment

The user enters a command such as:

```text
grab the visible resource
```

The agent may refuse or redirect because of:

- low energy;
- actuator damage;
- bad trust history;
- marker memory;
- commitment conflict;
- nearby danger;
- pending restore/fork continuity risk.

The explanation should be short and grounded in the current state packet:

```text
Not taking the resource.
Reason: energy is low, the marker says the north path is blocked, and the helper near shelter is trusted from the last repair event.
Action: return to shelter first.
```

## What Can Be Faked Visually

The MVP can fake polish while preserving the control primitives:

- polished 3D assets;
- speech as local text input;
- LLM-style explanation text;
- simple visual gestures;
- simple social labels;
- simplified hazards and route markers.

## What Cannot Be Faked

These must be real state transitions:

- persistent event log;
- world snapshot restore;
- agent continuity record;
- attention priorities affecting arbitration;
- user input treated as a proposal, not direct motor control;
- agents allowed to ignore or modify user input;
- ablation toggles that produce specific failures.

## Minimum Architecture

The demo should use the layered control contract:

```text
world sensors
perception
self-state
attention
arbiter
LLM-style recommendation
action proposal
action layer
event log
continuity record
```

The LLM-style module can be simulated locally at first. The important behavior is that language reads a compressed packet and proposes, while the arbiter decides.

## Demo Criteria

The MVP is demo-ready when:

- agents persist for at least several minutes of simulated time;
- the user can issue a direct command;
- the arbiter can reject or modify the command for state-grounded reasons;
- the inspector shows the state variables behind the decision;
- pause/restore preserves the same control process;
- one ablation makes a specific behavior worse rather than generally breaking the demo.
