window.SSRM_3D_LIVE_AVATAR_INTERVENTION_BRIDGE_RESULTS = {
  "report": 143,
  "name": "SSRM-3D Live Avatar Intervention Bridge",
  "config": {
    "seed": 20260617,
    "steps": 18,
    "source_agents": "artifacts/ssrm_3d_deep_time_playable_bridge_avatar_agents.json"
  },
  "eval": [
    {
      "condition": "integrated_live_avatar_session",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.786057,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.146257,
      "language_alignment": 1.0,
      "world_effect_score": 1.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.935698,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.76571
    },
    {
      "condition": "no_workspace_updates",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.497837,
      "workspace_update_rate": 0.0,
      "trust_gain": 0.147211,
      "language_alignment": 1.0,
      "world_effect_score": 1.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.755698,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.381201
    },
    {
      "condition": "no_trust_updates",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.401813,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.002057,
      "language_alignment": 1.0,
      "world_effect_score": 1.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.935698,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.647186
    },
    {
      "condition": "no_sensory_resonance",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.584018,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.122843,
      "language_alignment": 1.0,
      "world_effect_score": 0.7225,
      "sensory_resonance_score": 0.2,
      "response_specificity": 0.872,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.512598
    },
    {
      "condition": "no_language_grounding",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.594584,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.089178,
      "language_alignment": 0.0,
      "world_effect_score": 1.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.755698,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.388802
    },
    {
      "condition": "no_world_effects",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.548469,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.145436,
      "language_alignment": 1.0,
      "world_effect_score": 0.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.935698,
      "trace_completeness": 1.0,
      "intervention_readiness": 0.399322
    },
    {
      "condition": "no_replay_trace",
      "steps": 18,
      "responding_agents": 8,
      "state_change_rate": 0.786257,
      "workspace_update_rate": 1.0,
      "trust_gain": 0.14637,
      "language_alignment": 1.0,
      "world_effect_score": 1.0,
      "sensory_resonance_score": 0.59811,
      "response_specificity": 0.935698,
      "trace_completeness": 0.0,
      "intervention_readiness": 0.418005
    }
  ],
  "verdict": {
    "full_condition": "integrated_live_avatar_session",
    "full_intervention_readiness": 0.76571,
    "full_state_change_rate": 0.786057,
    "full_workspace_update_rate": 1.0,
    "full_trust_gain": 0.146257,
    "full_language_alignment": 1.0,
    "full_world_effect_score": 1.0,
    "full_sensory_resonance_score": 0.59811,
    "full_trace_completeness": 1.0,
    "no_workspace_loss": 0.384509,
    "no_trust_loss": 0.118524,
    "no_sensory_loss": 0.253112,
    "no_language_loss": 0.376908,
    "no_world_effect_loss": 0.366388,
    "no_replay_trace_loss": 0.347705,
    "supports_stateful_avatar_interaction_bridge": true,
    "supports_subjective_consciousness": false,
    "supports_mature_live_agents": false,
    "verdict": "pass"
  },
  "trace": [
    {
      "step": 1,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "player_utterance": "I enter quietly and ask what your first shelter word means.",
      "intervention_kind": "greet",
      "focus": "care-or-kinship",
      "sense": "audio",
      "native_token": "misavo",
      "sensory_resonance": 0.871021,
      "language_hit": true,
      "trust_before": 0.619258,
      "trust_after": 0.686398,
      "attention_before": "shared-food",
      "attention_after": "care-or-kinship",
      "world_before": {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.5,
        "danger_memory": 0.52,
        "trace_integrity": 0.0
      },
      "world_after": {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.691625,
        "danger_memory": 0.52,
        "trace_integrity": 0.055556
      },
      "agent_response": "Ari answers as scout: misavo points to care-or-kinship; attention shifts toward care-or-kinship.",
      "specificity": 0.979363
    },
    {
      "step": 2,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "player_utterance": "Teach me the danger sign near the old wet shelter.",
      "intervention_kind": "ask_meaning",
      "focus": "danger-or-weather-memory",
      "sense": "visual",
      "native_token": "eyaom",
      "sensory_resonance": 0.862588,
      "language_hit": true,
      "trust_before": 0.633206,
      "trust_after": 0.697463,
      "attention_before": "weather-memory",
      "attention_after": "danger-or-weather-memory",
      "world_before": {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.691625,
        "danger_memory": 0.52,
        "trace_integrity": 0.055556
      },
      "world_after": {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.111111
      },
      "agent_response": "Bo answers as builder: eyaom points to danger-or-weather-memory; attention shifts toward danger-or-weather-memory.",
      "specificity": 0.978014
    },
    {
      "step": 3,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "player_utterance": "I bring clean water and ask where it is needed.",
      "intervention_kind": "offer_resource",
      "focus": "shared-resource",
      "sense": "wetness",
      "native_token": "shathsha",
      "sensory_resonance": 0.733814,
      "language_hit": true,
      "trust_before": 0.622162,
      "trust_after": 0.702802,
      "attention_before": "child-safety",
      "attention_after": "shared-resource",
      "world_before": {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.111111
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.166667
      },
      "agent_response": "Cy answers as healer: shathsha points to shared-resource; attention shifts toward shared-resource.",
      "specificity": 0.95741
    },
    {
      "step": 4,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "player_utterance": "I help repair the cold tool cache before night rain.",
      "intervention_kind": "repair",
      "focus": "tool-or-route",
      "sense": "thermal",
      "native_token": "saka",
      "sensory_resonance": 0.661768,
      "language_hit": true,
      "trust_before": 0.630544,
      "trust_after": 0.69004,
      "attention_before": "council",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.166667
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.222222
      },
      "agent_response": "Dee answers as farmer: saka points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.945883
    },
    {
      "step": 5,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "player_utterance": "I notice pain and fear, then lower my voice and wait.",
      "intervention_kind": "comfort",
      "focus": "care-or-kinship",
      "sense": "pain",
      "native_token": "kathth",
      "sensory_resonance": 0.567276,
      "language_hit": true,
      "trust_before": 0.628564,
      "trust_after": 0.703532,
      "attention_before": "tool-repair",
      "attention_after": "care-or-kinship",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.48,
        "council_acceptance": 0.881394,
        "danger_memory": 0.52,
        "trace_integrity": 0.222222
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.48,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.277778
      },
      "agent_response": "Eli answers as guard: kathth points to care-or-kinship; attention shifts toward care-or-kinship.",
      "specificity": 0.930764
    },
    {
      "step": 6,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "player_utterance": "Show me the route that your scouts trust after storms.",
      "intervention_kind": "route_request",
      "focus": "tool-or-route",
      "sense": "vestibular",
      "native_token": "tulen",
      "sensory_resonance": 0.389546,
      "language_hit": true,
      "trust_before": 0.627464,
      "trust_after": 0.683489,
      "attention_before": "outer-path",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.48,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.277778
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.333333
      },
      "agent_response": "Fay answers as teacher: tulen points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.902327
    },
    {
      "step": 7,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "player_utterance": "I place a new mark and ask whether the council accepts it.",
      "intervention_kind": "share_symbol",
      "focus": "shared-resource",
      "sense": "affect",
      "native_token": "kamith",
      "sensory_resonance": 0.434724,
      "language_hit": true,
      "trust_before": 0.629224,
      "trust_after": 0.685474,
      "attention_before": "shared-food",
      "attention_after": "shared-resource",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.333333
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.388889
      },
      "agent_response": "Gus answers as trader: kamith points to shared-resource; attention shifts toward shared-resource.",
      "specificity": 0.909556
    },
    {
      "step": 8,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "player_utterance": "I ask what the wet cold air means for tonight's shelter.",
      "intervention_kind": "weather_watch",
      "focus": "danger-or-weather-memory",
      "sense": "olfactory",
      "native_token": "omom",
      "sensory_resonance": 0.699153,
      "language_hit": true,
      "trust_before": 0.626584,
      "trust_after": 0.685905,
      "attention_before": "tool-repair",
      "attention_after": "danger-or-weather-memory",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.52,
        "trace_integrity": 0.388889
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.444444
      },
      "agent_response": "Ira answers as pattern_keeper: omom points to danger-or-weather-memory; attention shifts toward danger-or-weather-memory.",
      "specificity": 0.951865
    },
    {
      "step": 9,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "player_utterance": "I promise not to take tools without a named return path.",
      "intervention_kind": "promise",
      "focus": "tool-or-route",
      "sense": "audio",
      "native_token": "nono",
      "sensory_resonance": 0.641596,
      "language_hit": true,
      "trust_before": 0.686398,
      "trust_after": 0.762653,
      "attention_before": "care-or-kinship",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 0.937355,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.444444
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.5
      },
      "agent_response": "Ari answers as scout: nono points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.942655
    },
    {
      "step": 10,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "player_utterance": "I enter quietly and ask what your first shelter word means.",
      "intervention_kind": "greet",
      "focus": "care-or-kinship",
      "sense": "audio",
      "native_token": "shatusha",
      "sensory_resonance": 0.395575,
      "language_hit": true,
      "trust_before": 0.697463,
      "trust_after": 0.753045,
      "attention_before": "danger-or-weather-memory",
      "attention_after": "care-or-kinship",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.5
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.555556
      },
      "agent_response": "Bo answers as builder: shatusha points to care-or-kinship; attention shifts toward care-or-kinship.",
      "specificity": 0.903292
    },
    {
      "step": 11,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "player_utterance": "Teach me the danger sign near the old wet shelter.",
      "intervention_kind": "ask_meaning",
      "focus": "danger-or-weather-memory",
      "sense": "visual",
      "native_token": "shath",
      "sensory_resonance": 0.386278,
      "language_hit": true,
      "trust_before": 0.702802,
      "trust_after": 0.757734,
      "attention_before": "shared-resource",
      "attention_after": "danger-or-weather-memory",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.555556
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.611111
      },
      "agent_response": "Cy answers as healer: shath points to danger-or-weather-memory; attention shifts toward danger-or-weather-memory.",
      "specificity": 0.901804
    },
    {
      "step": 12,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "player_utterance": "I bring clean water and ask where it is needed.",
      "intervention_kind": "offer_resource",
      "focus": "shared-resource",
      "sense": "wetness",
      "native_token": "vonono",
      "sensory_resonance": 0.789312,
      "language_hit": true,
      "trust_before": 0.69004,
      "trust_after": 0.771602,
      "attention_before": "tool-or-route",
      "attention_after": "shared-resource",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.611111
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.666667
      },
      "agent_response": "Dee answers as farmer: vonono points to shared-resource; attention shifts toward shared-resource.",
      "specificity": 0.96629
    },
    {
      "step": 13,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "player_utterance": "I help repair the cold tool cache before night rain.",
      "intervention_kind": "repair",
      "focus": "tool-or-route",
      "sense": "thermal",
      "native_token": "mivo",
      "sensory_resonance": 0.842635,
      "language_hit": true,
      "trust_before": 0.703532,
      "trust_after": 0.770286,
      "attention_before": "care-or-kinship",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.73853,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.666667
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.722222
      },
      "agent_response": "Eli answers as guard: mivo points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.974822
    },
    {
      "step": 14,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "player_utterance": "I notice pain and fear, then lower my voice and wait.",
      "intervention_kind": "comfort",
      "focus": "care-or-kinship",
      "sense": "pain",
      "native_token": "milenno",
      "sensory_resonance": 0.421011,
      "language_hit": true,
      "trust_before": 0.683489,
      "trust_after": 0.757547,
      "attention_before": "tool-or-route",
      "attention_after": "care-or-kinship",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.722222
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.777778
      },
      "agent_response": "Fay answers as teacher: milenno points to care-or-kinship; attention shifts toward care-or-kinship.",
      "specificity": 0.907362
    },
    {
      "step": 15,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "player_utterance": "Show me the route that your scouts trust after storms.",
      "intervention_kind": "route_request",
      "focus": "tool-or-route",
      "sense": "vestibular",
      "native_token": "omno",
      "sensory_resonance": 0.630317,
      "language_hit": true,
      "trust_before": 0.685474,
      "trust_after": 0.746253,
      "attention_before": "shared-resource",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 0.682564,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.777778
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.833333
      },
      "agent_response": "Gus answers as trader: omno points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.940851
    },
    {
      "step": 16,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "player_utterance": "I place a new mark and ask whether the council accepts it.",
      "intervention_kind": "share_symbol",
      "focus": "shared-resource",
      "sense": "affect",
      "native_token": "mieyaeya",
      "sensory_resonance": 0.701807,
      "language_hit": true,
      "trust_before": 0.685905,
      "trust_after": 0.747279,
      "attention_before": "danger-or-weather-memory",
      "attention_after": "shared-resource",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.833333
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.888889
      },
      "agent_response": "Ira answers as pattern_keeper: mieyaeya points to shared-resource; attention shifts toward shared-resource.",
      "specificity": 0.952289
    },
    {
      "step": 17,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "player_utterance": "I ask what the wet cold air means for tonight's shelter.",
      "intervention_kind": "weather_watch",
      "focus": "danger-or-weather-memory",
      "sense": "olfactory",
      "native_token": "vosha",
      "sensory_resonance": 0.358588,
      "language_hit": true,
      "trust_before": 0.762653,
      "trust_after": 0.813144,
      "attention_before": "tool-or-route",
      "attention_after": "danger-or-weather-memory",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 0.869577,
        "trace_integrity": 0.888889
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 1.0,
        "trace_integrity": 0.944444
      },
      "agent_response": "Ari answers as scout: vosha points to danger-or-weather-memory; attention shifts toward danger-or-weather-memory.",
      "specificity": 0.897374
    },
    {
      "step": 18,
      "condition": "integrated_live_avatar_session",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "player_utterance": "I promise not to take tools without a named return path.",
      "intervention_kind": "promise",
      "focus": "tool-or-route",
      "sense": "audio",
      "native_token": "vori",
      "sensory_resonance": 0.378979,
      "language_hit": true,
      "trust_before": 0.753045,
      "trust_after": 0.823216,
      "attention_before": "care-or-kinship",
      "attention_after": "tool-or-route",
      "world_before": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 1.0,
        "trace_integrity": 0.944444
      },
      "world_after": {
        "shared_water": 1.0,
        "tool_integrity": 1.0,
        "shelter_warmth": 0.991321,
        "route_confidence": 1.0,
        "council_acceptance": 1.0,
        "danger_memory": 1.0,
        "trace_integrity": 1.0
      },
      "agent_response": "Bo answers as builder: vori points to tool-or-route; attention shifts toward tool-or-route.",
      "specificity": 0.900637
    }
  ],
  "final_state": {
    "condition": "integrated_live_avatar_session",
    "world": {
      "shared_water": 1.0,
      "tool_integrity": 1.0,
      "shelter_warmth": 0.991321,
      "route_confidence": 1.0,
      "council_acceptance": 1.0,
      "danger_memory": 1.0,
      "trace_integrity": 1.0
    },
    "agents": {
      "integrated_deep_time_world:00": {
        "agent_id": "integrated_deep_time_world:00",
        "name": "Ari",
        "role": "scout",
        "trust": 0.8131444679163408,
        "attention": "danger-or-weather-memory",
        "motive": "read-weather",
        "body_state": 0.8672444036824737,
        "fear": 0.21718795381051276,
        "attachment": 0.8217256600463334,
        "curiosity": 0.5747000000000001,
        "workspace_updates": 3,
        "language_hits": 3,
        "responses": 3
      },
      "integrated_deep_time_world:01": {
        "agent_id": "integrated_deep_time_world:01",
        "name": "Bo",
        "role": "builder",
        "trust": 0.8232156127390092,
        "attention": "tool-or-route",
        "motive": "bind-commitment",
        "body_state": 0.8224228521236576,
        "fear": 0.2316285797939039,
        "attachment": 0.8820828462679249,
        "curiosity": 0.6361,
        "workspace_updates": 3,
        "language_hits": 3,
        "responses": 3
      },
      "integrated_deep_time_world:02": {
        "agent_id": "integrated_deep_time_world:02",
        "name": "Cy",
        "role": "healer",
        "trust": 0.7577338997844184,
        "attention": "danger-or-weather-memory",
        "motive": "teach-symbol",
        "body_state": 0.8385263273766016,
        "fear": 0.24789907637183917,
        "attachment": 0.8036612007166091,
        "curiosity": 0.5707,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      },
      "integrated_deep_time_world:03": {
        "agent_id": "integrated_deep_time_world:03",
        "name": "Dee",
        "role": "farmer",
        "trust": 0.7716015154778171,
        "attention": "shared-resource",
        "motive": "allocate-resource",
        "body_state": 0.899719443810116,
        "fear": 0.18508919788326889,
        "attachment": 0.8460640427517504,
        "curiosity": 0.5727,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      },
      "integrated_deep_time_world:04": {
        "agent_id": "integrated_deep_time_world:04",
        "name": "Eli",
        "role": "guard",
        "trust": 0.7702857493277879,
        "attention": "tool-or-route",
        "motive": "coordinate-repair",
        "body_state": 0.9060710857742332,
        "fear": 0.17498260011909547,
        "attachment": 0.8365288452020788,
        "curiosity": 0.5765,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      },
      "integrated_deep_time_world:05": {
        "agent_id": "integrated_deep_time_world:05",
        "name": "Fay",
        "role": "teacher",
        "trust": 0.757546931287271,
        "attention": "care-or-kinship",
        "motive": "lower-fear",
        "body_state": 0.8712378892561187,
        "fear": 0.24226411868475906,
        "attachment": 0.8237372337803998,
        "curiosity": 0.6082000000000001,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      },
      "integrated_deep_time_world:06": {
        "agent_id": "integrated_deep_time_world:06",
        "name": "Gus",
        "role": "trader",
        "trust": 0.746253135428775,
        "attention": "tool-or-route",
        "motive": "share-route",
        "body_state": 0.8689540455645995,
        "fear": 0.23374959157739975,
        "attachment": 0.8260455309493804,
        "curiosity": 0.547,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      },
      "integrated_deep_time_world:07": {
        "agent_id": "integrated_deep_time_world:07",
        "name": "Ira",
        "role": "pattern_keeper",
        "trust": 0.7472789727942305,
        "attention": "shared-resource",
        "motive": "test-convention",
        "body_state": 0.8238040681693213,
        "fear": 0.2229903972107449,
        "attachment": 0.8184124836260316,
        "curiosity": 0.5471,
        "workspace_updates": 2,
        "language_hits": 2,
        "responses": 2
      }
    }
  },
  "source_agents": [
    {
      "agent_id": "integrated_deep_time_world:00",
      "name": "Ari",
      "role": "scout",
      "lineage_year": 4096,
      "position": {
        "x": 8.0,
        "z": 0.0
      },
      "native_tokens": [
        "vosha",
        "shanoeya",
        "nono",
        "misavo"
      ],
      "translation_hints": {
        "vosha": "danger-or-weather-memory",
        "shanoeya": "shared-resource",
        "nono": "tool-or-route",
        "misavo": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "shared-food",
        "motive": "trade-safely",
        "body_state": 0.8653,
        "affect": {
          "fear": 0.2359,
          "attachment": 0.7239,
          "curiosity": 0.5147
        },
        "private_thought": "Ari weighs scout duty against vosha signal history."
      },
      "conversation_hooks": [
        "Ask Ari what vosha means near the old shelter.",
        "Ask Ari why the scout tradition survived the last wet season.",
        "Ask Ari what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:01",
      "name": "Bo",
      "role": "builder",
      "lineage_year": 3904,
      "position": {
        "x": 7.794,
        "z": 4.5
      },
      "native_tokens": [
        "eyaom",
        "nonoeya",
        "vori",
        "shatusha"
      ],
      "translation_hints": {
        "eyaom": "danger-or-weather-memory",
        "nonoeya": "shared-resource",
        "vori": "tool-or-route",
        "shatusha": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "weather-memory",
        "motive": "trade-safely",
        "body_state": 0.8126,
        "affect": {
          "fear": 0.248,
          "attachment": 0.7873,
          "curiosity": 0.5761
        },
        "private_thought": "Bo weighs builder duty against eyaom signal history."
      },
      "conversation_hooks": [
        "Ask Bo what eyaom means near the old shelter.",
        "Ask Bo why the builder tradition survived the last wet season.",
        "Ask Bo what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:02",
      "name": "Cy",
      "role": "healer",
      "lineage_year": 3712,
      "position": {
        "x": 5.0,
        "z": 8.66
      },
      "native_tokens": [
        "shath",
        "shathsha",
        "voeya",
        "eyasami"
      ],
      "translation_hints": {
        "shath": "danger-or-weather-memory",
        "shathsha": "shared-resource",
        "voeya": "tool-or-route",
        "eyasami": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "child-safety",
        "motive": "teach-pattern",
        "body_state": 0.805,
        "affect": {
          "fear": 0.2591,
          "attachment": 0.7371,
          "curiosity": 0.5307
        },
        "private_thought": "Cy weighs healer duty against shath signal history."
      },
      "conversation_hooks": [
        "Ask Cy what shath means near the old shelter.",
        "Ask Cy why the healer tradition survived the last wet season.",
        "Ask Cy what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:03",
      "name": "Dee",
      "role": "farmer",
      "lineage_year": 3520,
      "position": {
        "x": 0.0,
        "z": 11.0
      },
      "native_tokens": [
        "shavo",
        "vonono",
        "saka",
        "shatusha"
      ],
      "translation_hints": {
        "shavo": "danger-or-weather-memory",
        "vonono": "shared-resource",
        "saka": "tool-or-route",
        "shatusha": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "council",
        "motive": "repair-tool",
        "body_state": 0.8376,
        "affect": {
          "fear": 0.1996,
          "attachment": 0.7752,
          "curiosity": 0.5327
        },
        "private_thought": "Dee weighs farmer duty against shavo signal history."
      },
      "conversation_hooks": [
        "Ask Dee what shavo means near the old shelter.",
        "Ask Dee why the farmer tradition survived the last wet season.",
        "Ask Dee what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:04",
      "name": "Eli",
      "role": "guard",
      "lineage_year": 3328,
      "position": {
        "x": -6.0,
        "z": 10.392
      },
      "native_tokens": [
        "mitu",
        "vovomi",
        "mivo",
        "kathth"
      ],
      "translation_hints": {
        "mitu": "danger-or-weather-memory",
        "vovomi": "shared-resource",
        "mivo": "tool-or-route",
        "kathth": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "tool-repair",
        "motive": "learn-route",
        "body_state": 0.8695,
        "affect": {
          "fear": 0.2061,
          "attachment": 0.7662,
          "curiosity": 0.5365
        },
        "private_thought": "Eli weighs guard duty against mitu signal history."
      },
      "conversation_hooks": [
        "Ask Eli what mitu means near the old shelter.",
        "Ask Eli why the guard tradition survived the last wet season.",
        "Ask Eli what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:05",
      "name": "Fay",
      "role": "teacher",
      "lineage_year": 3136,
      "position": {
        "x": -11.258,
        "z": 6.5
      },
      "native_tokens": [
        "vomi",
        "shalenka",
        "tulen",
        "milenno"
      ],
      "translation_hints": {
        "vomi": "danger-or-weather-memory",
        "shalenka": "shared-resource",
        "tulen": "tool-or-route",
        "milenno": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "outer-path",
        "motive": "repair-tool",
        "body_state": 0.8437,
        "affect": {
          "fear": 0.263,
          "attachment": 0.7612,
          "curiosity": 0.5682
        },
        "private_thought": "Fay weighs teacher duty against vomi signal history."
      },
      "conversation_hooks": [
        "Ask Fay what vomi means near the old shelter.",
        "Ask Fay why the teacher tradition survived the last wet season.",
        "Ask Fay what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:06",
      "name": "Gus",
      "role": "trader",
      "lineage_year": 2944,
      "position": {
        "x": -14.0,
        "z": 0.0
      },
      "native_tokens": [
        "leneya",
        "kamith",
        "omno",
        "omriri"
      ],
      "translation_hints": {
        "leneya": "danger-or-weather-memory",
        "kamith": "shared-resource",
        "omno": "tool-or-route",
        "omriri": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "shared-food",
        "motive": "learn-route",
        "body_state": 0.837,
        "affect": {
          "fear": 0.2444,
          "attachment": 0.7692,
          "curiosity": 0.507
        },
        "private_thought": "Gus weighs trader duty against leneya signal history."
      },
      "conversation_hooks": [
        "Ask Gus what leneya means near the old shelter.",
        "Ask Gus why the trader tradition survived the last wet season.",
        "Ask Gus what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    },
    {
      "agent_id": "integrated_deep_time_world:07",
      "name": "Ira",
      "role": "pattern_keeper",
      "lineage_year": 2752,
      "position": {
        "x": -12.99,
        "z": -7.5
      },
      "native_tokens": [
        "omom",
        "mieyaeya",
        "voeya",
        "vothsha"
      ],
      "translation_hints": {
        "omom": "danger-or-weather-memory",
        "mieyaeya": "shared-resource",
        "voeya": "tool-or-route",
        "vothsha": "care-or-kinship"
      },
      "sensory_rates_hz": {
        "visual": 2.5642,
        "audio": 4.961,
        "olfactory": 6.9965,
        "thermal": 7.9895,
        "wetness": 11.2088,
        "pain": 13.2865,
        "affect": 13.4611,
        "vestibular": 15.372
      },
      "internal_workspace": {
        "attention": "tool-repair",
        "motive": "protect-settlement",
        "body_state": 0.824,
        "affect": {
          "fear": 0.237,
          "attachment": 0.7572,
          "curiosity": 0.5071
        },
        "private_thought": "Ira weighs pattern_keeper duty against omom signal history."
      },
      "conversation_hooks": [
        "Ask Ira what omom means near the old shelter.",
        "Ask Ira why the pattern_keeper tradition survived the last wet season.",
        "Ask Ira what tool, route, or promise should be protected next."
      ],
      "avatar_entry_ready": true
    }
  ],
  "notes": {
    "claim": "stateful bridge from deep-time avatar packets to player-driven intervention traces",
    "not_claimed": "subjective consciousness, LLM-backed dialogue, mature live agents, or full playable world completion",
    "interaction_basis": "player utterances and actions update agent workspace, trust, language grounding, sensory-rate resonance, and world state"
  }
};
