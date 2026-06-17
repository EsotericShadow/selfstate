window.SSRM_3D_LIVE_OBJECT_NEED_DIALOGUE_INTERACTION_RESULTS = {
  "agent_specs": [
    {
      "agent_id": "Ari",
      "needs": {
        "autonomy_pressure": 0.28,
        "cold": 0.58,
        "connection_deficit": 0.36,
        "curiosity_deficit": 0.22,
        "fatigue": 0.44,
        "safety_concern": 0.31,
        "thirst": 0.32,
        "unfinished_task": 0.69
      },
      "place": "hearth_vale",
      "relationship": {
        "felt_respect": 0.64,
        "gratitude": 0.18,
        "trust_in_avatar": 0.52,
        "wariness": 0.34
      },
      "self_story": [
        "I keep the clay latch repaired.",
        "My patch kit is not for grabbing."
      ],
      "temperament": {
        "autonomy_need": 0.72,
        "curious": 0.58,
        "forgiveness": 0.61,
        "guarded": 0.66
      }
    },
    {
      "agent_id": "Fay",
      "needs": {
        "autonomy_pressure": 0.22,
        "cold": 0.34,
        "connection_deficit": 0.42,
        "curiosity_deficit": 0.35,
        "fatigue": 0.52,
        "safety_concern": 0.27,
        "thirst": 0.61,
        "unfinished_task": 0.28
      },
      "place": "moss_hollow",
      "relationship": {
        "felt_respect": 0.69,
        "gratitude": 0.22,
        "trust_in_avatar": 0.57,
        "wariness": 0.26
      },
      "self_story": [
        "I keep moss bedding dry.",
        "I lend the cloak only when people ask."
      ],
      "temperament": {
        "autonomy_need": 0.54,
        "curious": 0.46,
        "forgiveness": 0.74,
        "guarded": 0.38
      }
    },
    {
      "agent_id": "Milo",
      "needs": {
        "autonomy_pressure": 0.25,
        "cold": 0.29,
        "connection_deficit": 0.49,
        "curiosity_deficit": 0.44,
        "fatigue": 0.37,
        "safety_concern": 0.64,
        "thirst": 0.41,
        "unfinished_task": 0.34
      },
      "place": "stone_ridge",
      "relationship": {
        "felt_respect": 0.61,
        "gratitude": 0.12,
        "trust_in_avatar": 0.48,
        "wariness": 0.39
      },
      "self_story": [
        "I listen for ridge changes.",
        "Warnings should be shared before sunset."
      ],
      "temperament": {
        "autonomy_need": 0.48,
        "curious": 0.71,
        "forgiveness": 0.57,
        "guarded": 0.49
      }
    }
  ],
  "config": {
    "seed": 20260725,
    "source_state": "artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_state.json"
  },
  "moral_boundary": {
    "bounded_dialogue_not_natural_language_emergence": true,
    "interaction_seed_not_complete_gameplay": true,
    "local_agent_state_not_moral_patienthood": true,
    "need_state_not_subjective_feeling": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true
  },
  "next_gate": "live object persistence, promise keeping, and longer relationship continuity",
  "object_specs": [
    {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "label": "ember blanket",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale"
    },
    {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "label": "reed cup",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow"
    },
    {
      "affordances": [
        "repair",
        "tool",
        "promise"
      ],
      "flower_node": "work_petal",
      "frequency_hz": 0.241,
      "label": "clay patch kit",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale"
    },
    {
      "affordances": [
        "dry",
        "warmth",
        "privacy"
      ],
      "flower_node": "return_petal",
      "frequency_hz": 0.219,
      "label": "dry cloak",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow"
    },
    {
      "affordances": [
        "warn",
        "listen",
        "observability"
      ],
      "flower_node": "social_petal",
      "frequency_hz": 0.256,
      "label": "signal shell",
      "need_targets": [
        "safety_concern",
        "connection_deficit"
      ],
      "object_id": "signal_shell",
      "owner": "Milo",
      "place": "stone_ridge"
    },
    {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "label": "glass lens",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire"
    }
  ],
  "rows": [
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "integrated_live_object_need_dialogue_interaction",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.993,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 0.5,
      "condition": "no_objects",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.673,
      "need_state_update_rate": 0.7,
      "object_affordance_binding_rate": 0.0,
      "object_count": 0,
      "object_ownership_respect_rate": 0.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 0.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 0.0,
      "condition": "no_need_state",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.813,
      "need_state_update_rate": 0.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_interaction_costs",
      "interaction_cost_application_rate": 0.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.923,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 0.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_bounded_dialogue",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.893,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_refusal_consent",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.889,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 0.8,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 0.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 0.0,
      "condition": "no_care_resolution",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.913,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_ownership",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.833,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 0.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 0.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_place_context",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.93,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.0,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_relationship_memory",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.903,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 0.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_replay_log",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.923,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 0.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 0.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_browser_mutation",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.913,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 1.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    },
    {
      "agent_count": 3,
      "bounded_dialogue_response_rate": 1.0,
      "browser_state_mutation_rate": 1.0,
      "care_opportunity_resolution_rate": 1.0,
      "condition": "no_privacy_filter",
      "interaction_cost_application_rate": 1.0,
      "interaction_events": 10,
      "live_interaction_readiness": 0.953,
      "need_state_update_rate": 1.0,
      "object_affordance_binding_rate": 1.0,
      "object_count": 6,
      "object_ownership_respect_rate": 1.0,
      "place_context_binding_rate": 0.9,
      "privacy_preservation_rate": 0.0,
      "refusal_consent_boundary_rate": 1.0,
      "relationship_memory_update_rate": 1.0,
      "replay_interaction_event_rate": 1.0,
      "trace_integrity": 1.0
    }
  ],
  "source_state": "artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_state.json",
  "verdict": {
    "full_bounded_dialogue_response_rate": 1.0,
    "full_browser_state_mutation_rate": 1.0,
    "full_care_opportunity_resolution_rate": 1.0,
    "full_condition": "integrated_live_object_need_dialogue_interaction",
    "full_interaction_cost_application_rate": 1.0,
    "full_live_interaction_readiness": 0.993,
    "full_need_state_update_rate": 1.0,
    "full_object_affordance_binding_rate": 1.0,
    "full_object_ownership_respect_rate": 1.0,
    "full_place_context_binding_rate": 0.9,
    "full_privacy_preservation_rate": 1.0,
    "full_refusal_consent_boundary_rate": 1.0,
    "full_relationship_memory_update_rate": 1.0,
    "full_replay_interaction_event_rate": 1.0,
    "full_trace_integrity": 1.0,
    "no_bounded_dialogue_loss": 0.1,
    "no_browser_mutation_loss": 0.08,
    "no_care_resolution_loss": 0.08,
    "no_interaction_costs_loss": 0.07,
    "no_need_state_loss": 0.18,
    "no_objects_loss": 0.32,
    "no_ownership_loss": 0.16,
    "no_place_context_loss": 0.063,
    "no_privacy_filter_loss": 0.04,
    "no_refusal_consent_loss": 0.104,
    "no_relationship_memory_loss": 0.09,
    "no_replay_log_loss": 0.07,
    "supports_complete_3d_world": false,
    "supports_complete_playable_world": false,
    "supports_live_object_need_dialogue_interaction_bridge": true,
    "supports_local_agent_interaction_seed": true,
    "supports_moral_patienthood_claim": false,
    "supports_natural_language_emergence": false,
    "supports_subjective_consciousness": false,
    "verdict": "pass"
  },
  "weights": {
    "bounded_dialogue_response_rate": 0.1,
    "browser_state_mutation_rate": 0.08,
    "care_opportunity_resolution_rate": 0.08,
    "interaction_cost_application_rate": 0.07,
    "need_state_update_rate": 0.1,
    "object_affordance_binding_rate": 0.09,
    "object_ownership_respect_rate": 0.07,
    "place_context_binding_rate": 0.07,
    "privacy_preservation_rate": 0.04,
    "refusal_consent_boundary_rate": 0.09,
    "relationship_memory_update_rate": 0.09,
    "replay_interaction_event_rate": 0.07,
    "trace_integrity": 0.05
  }
};
