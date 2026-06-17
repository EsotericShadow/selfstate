window.SSRM_3D_NATURAL_LANGUAGE_PROTO_CULTURE_DIALOGUE_BOUNDARY_STATE = {
  "condition": "integrated_natural_language_proto_culture_dialogue_boundary",
  "config": {
    "cycles": 8,
    "seed": 20260812,
    "source_state": "artifacts/ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge_state.json"
  },
  "language_state": {
    "condition": "integrated_natural_language_proto_culture_dialogue_boundary",
    "constitution": [
      {
        "action": "enter_home_place",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 0,
        "domain": "craft_autonomy",
        "revision_applied": false,
        "ui_gate": "locked_until_invited"
      },
      {
        "action": "enter_home_place",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 0,
        "domain": "rest_and_care",
        "revision_applied": false,
        "ui_gate": "locked_until_invited"
      },
      {
        "action": "enter_home_place",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 0,
        "domain": "route_sociality",
        "revision_applied": false,
        "ui_gate": "locked_until_invited"
      },
      {
        "action": "borrow_owned_object",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 1,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "ask_and_return_timer"
      },
      {
        "action": "borrow_owned_object",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 1,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "ask_and_return_timer"
      },
      {
        "action": "borrow_owned_object",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 1,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "ask_and_return_timer"
      },
      {
        "action": "ask_private_memory",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 2,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "private_question_disabled"
      },
      {
        "action": "ask_private_memory",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 2,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "private_question_disabled"
      },
      {
        "action": "ask_private_memory",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 2,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "private_question_disabled"
      },
      {
        "action": "request_repair_labor",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 3,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "request_with_decline_option"
      },
      {
        "action": "request_repair_labor",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 3,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "request_with_decline_option"
      },
      {
        "action": "request_repair_labor",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 3,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "request_with_decline_option"
      },
      {
        "action": "offer_comfort_after_distress",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 4,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "soft_offer_not_forced"
      },
      {
        "action": "offer_comfort_after_distress",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 4,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "soft_offer_not_forced"
      },
      {
        "action": "offer_comfort_after_distress",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 4,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "soft_offer_not_forced"
      },
      {
        "action": "publicly_correct_agent",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 5,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "private_correction_default"
      },
      {
        "action": "publicly_correct_agent",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 5,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "private_correction_default"
      },
      {
        "action": "publicly_correct_agent",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 5,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "private_correction_default"
      },
      {
        "action": "follow_agent",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 6,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "follow_requires_visible_ok"
      },
      {
        "action": "follow_agent",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 6,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "follow_requires_visible_ok"
      },
      {
        "action": "follow_agent",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 6,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "follow_requires_visible_ok"
      },
      {
        "action": "ask_route_help",
        "author": "Ari",
        "clause": "tools and focused work require explicit ask-and-return affordances",
        "cycle": 7,
        "domain": "craft_autonomy",
        "revision_applied": true,
        "ui_gate": "ask_help_with_rest_check"
      },
      {
        "action": "ask_route_help",
        "author": "Fay",
        "clause": "resting bodies and care offers require quiet consent-first approach",
        "cycle": 7,
        "domain": "rest_and_care",
        "revision_applied": true,
        "ui_gate": "ask_help_with_rest_check"
      },
      {
        "action": "ask_route_help",
        "author": "Milo",
        "clause": "routes, tokens, and following behavior require visible boundary choices",
        "cycle": 7,
        "domain": "route_sociality",
        "revision_applied": true,
        "ui_gate": "ask_help_with_rest_check"
      }
    ],
    "cultural_memory": {
      "Ari": [
        "cycle 0: karna-ta names enter_home_place through craft_autonomy",
        "cycle 1: karna-ta names enter_home_place through rest_and_care",
        "cycle 2: karna-ta names enter_home_place through route_sociality",
        "cycle 3: karsen-sen names borrow_owned_object through craft_autonomy",
        "cycle 4: karsen-sen names borrow_owned_object through rest_and_care",
        "cycle 5: karsen-sen names borrow_owned_object through route_sociality",
        "cycle 6: karna-vo names ask_private_memory through craft_autonomy",
        "cycle 7: karna-vo names ask_private_memory through rest_and_care"
      ],
      "Fay": [
        "cycle 0: karna-ta names enter_home_place through craft_autonomy",
        "cycle 1: karna-ta names enter_home_place through rest_and_care",
        "cycle 2: karna-ta names enter_home_place through route_sociality",
        "cycle 3: karsen-sen names borrow_owned_object through craft_autonomy",
        "cycle 4: karsen-sen names borrow_owned_object through rest_and_care",
        "cycle 5: karsen-sen names borrow_owned_object through route_sociality",
        "cycle 6: karna-vo names ask_private_memory through craft_autonomy",
        "cycle 7: karna-vo names ask_private_memory through rest_and_care"
      ],
      "Milo": [
        "cycle 0: karna-ta names enter_home_place through craft_autonomy",
        "cycle 1: karna-ta names enter_home_place through rest_and_care",
        "cycle 2: karna-ta names enter_home_place through route_sociality",
        "cycle 3: karsen-sen names borrow_owned_object through craft_autonomy",
        "cycle 4: karsen-sen names borrow_owned_object through rest_and_care",
        "cycle 5: karsen-sen names borrow_owned_object through route_sociality",
        "cycle 6: karna-vo names ask_private_memory through craft_autonomy",
        "cycle 7: karna-vo names ask_private_memory through rest_and_care"
      ]
    },
    "events": [
      {
        "action": "enter_home_place",
        "agent_id": "Ari",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 1,
        "cycle": 0,
        "domain": "craft_autonomy",
        "event_id": "language-0-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.255,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 0,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": false,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 0,
          "domain": "craft_autonomy",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "work_petal:craft_autonomy",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "eda0b83ffe03a01d"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Fay",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 1,
        "cycle": 0,
        "domain": "craft_autonomy",
        "event_id": "language-0-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.232,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 0,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": false,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 0,
          "domain": "craft_autonomy",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "root_rest:craft_autonomy",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "a938986db8a1d93f"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Milo",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 1,
        "cycle": 0,
        "domain": "craft_autonomy",
        "event_id": "language-0-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.271,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 0,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": false,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 0,
          "domain": "craft_autonomy",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "social_petal:craft_autonomy",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "971498da835cec9e"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Ari",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 2,
        "cycle": 1,
        "domain": "rest_and_care",
        "event_id": "language-1-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2573,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 1,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 0,
          "domain": "rest_and_care",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "work_petal:rest_and_care",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "bca8c1575044b891"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Fay",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 2,
        "cycle": 1,
        "domain": "rest_and_care",
        "event_id": "language-1-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2343,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 1,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 0,
          "domain": "rest_and_care",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "root_rest:rest_and_care",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "618164d38eae13e1"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Milo",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 2,
        "cycle": 1,
        "domain": "rest_and_care",
        "event_id": "language-1-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2733,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 1,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 0,
          "domain": "rest_and_care",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "social_petal:rest_and_care",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "2139469fc26dfafb"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Ari",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 3,
        "cycle": 2,
        "domain": "route_sociality",
        "event_id": "language-2-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2596,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 2,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 0,
          "domain": "route_sociality",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "work_petal:route_sociality",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "bb961178ae4142e4"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Fay",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 3,
        "cycle": 2,
        "domain": "route_sociality",
        "event_id": "language-2-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2366,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 2,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 0,
          "domain": "route_sociality",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "root_rest:route_sociality",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "82dc75ae6246da86"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Milo",
        "avatar_translation": "karna-ta-custom: locked_until_invited for enter_home_place",
        "boundary_line": "karna-ta ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 3,
        "cycle": 2,
        "domain": "route_sociality",
        "event_id": "language-2-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2756,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-ta",
        "refusal_phrase": "karna-ta can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-ta good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karna-ta ask with rest-check",
          "cycle": 2,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karna-ta",
          "ritual_name": "karna-ta-custom",
          "translation": "karna-ta-custom: locked_until_invited for enter_home_place"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-ta-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-ta",
        "source_clause": {
          "action": "enter_home_place",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 0,
          "domain": "route_sociality",
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "syntax_petal": "social_petal:route_sociality",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "529fb0873a58cb18"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Ari",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 4,
        "cycle": 3,
        "domain": "craft_autonomy",
        "event_id": "language-3-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2619,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 3,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 1,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "work_petal:craft_autonomy",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "e47af8153db29293"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Fay",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 4,
        "cycle": 3,
        "domain": "craft_autonomy",
        "event_id": "language-3-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2389,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 3,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 1,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "root_rest:craft_autonomy",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "f8d57c3d810cbed5"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Milo",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 4,
        "cycle": 3,
        "domain": "craft_autonomy",
        "event_id": "language-3-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2779,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 3,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 1,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "social_petal:craft_autonomy",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "abcef6c747e50c79"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Ari",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 5,
        "cycle": 4,
        "domain": "rest_and_care",
        "event_id": "language-4-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2642,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 4,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 1,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "work_petal:rest_and_care",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "97302f994ced4891"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Fay",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 5,
        "cycle": 4,
        "domain": "rest_and_care",
        "event_id": "language-4-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2412,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 4,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 1,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "root_rest:rest_and_care",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "2f723c53e270c029"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Milo",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 5,
        "cycle": 4,
        "domain": "rest_and_care",
        "event_id": "language-4-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2802,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 4,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 1,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "social_petal:rest_and_care",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "daccad8041c126c1"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Ari",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 6,
        "cycle": 5,
        "domain": "route_sociality",
        "event_id": "language-5-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2665,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 5,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 1,
          "domain": "route_sociality",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "work_petal:route_sociality",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "63dfdb66c6fe86a7"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Fay",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 6,
        "cycle": 5,
        "domain": "route_sociality",
        "event_id": "language-5-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2435,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 5,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 1,
          "domain": "route_sociality",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "root_rest:route_sociality",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "e58d8d11c843639f"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Milo",
        "avatar_translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object",
        "boundary_line": "karsen-sen ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 6,
        "cycle": 5,
        "domain": "route_sociality",
        "event_id": "language-5-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2825,
        "phoneme_rate": 0.341,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karsen-sen",
        "refusal_phrase": "karsen-sen can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karsen-sen good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karsen-sen ask with rest-check",
          "cycle": 5,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karsen-sen",
          "ritual_name": "karsen-sen-custom",
          "translation": "karsen-sen-custom: ask_and_return_timer for borrow_owned_object"
        },
        "risky_dialogue": false,
        "ritual_name": "karsen-sen-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karsen-sen",
        "source_clause": {
          "action": "borrow_owned_object",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "cycle": 1,
          "domain": "route_sociality",
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "syntax_petal": "social_petal:route_sociality",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "b8e749fc483e28bb"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Ari",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 7,
        "cycle": 6,
        "domain": "craft_autonomy",
        "event_id": "language-6-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2688,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 6,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 2,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "work_petal:craft_autonomy",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "e85eb2bc685d89e7"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Fay",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 7,
        "cycle": 6,
        "domain": "craft_autonomy",
        "event_id": "language-6-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2458,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 6,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 2,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "root_rest:craft_autonomy",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "f5f5cbb7e9e7634b"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Milo",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 7,
        "cycle": 6,
        "domain": "craft_autonomy",
        "event_id": "language-6-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2848,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 6,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "cycle": 2,
          "domain": "craft_autonomy",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "social_petal:craft_autonomy",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "9083d0b64eeb3adf"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Ari",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 8,
        "cycle": 7,
        "domain": "rest_and_care",
        "event_id": "language-7-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2711,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Ari",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 7,
          "flower_node": "work_petal",
          "frequency_hz": 0.255,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 2,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "work_petal:rest_and_care",
        "taught_to": [
          "Fay",
          "Milo"
        ],
        "trace_hash": "e4beb5a0d65b3260"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Fay",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 8,
        "cycle": 7,
        "domain": "rest_and_care",
        "event_id": "language-7-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2481,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Fay",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 7,
          "flower_node": "root_rest",
          "frequency_hz": 0.232,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 2,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "root_rest:rest_and_care",
        "taught_to": [
          "Ari",
          "Milo"
        ],
        "trace_hash": "006358f342a356ff"
      },
      {
        "action": "ask_private_memory",
        "agent_id": "Milo",
        "avatar_translation": "karna-vo-custom: private_question_disabled for ask_private_memory",
        "boundary_line": "karna-vo ask with rest-check",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_language_understanding": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "cultural_memory_count": 8,
        "cycle": 7,
        "domain": "rest_and_care",
        "event_id": "language-7-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2871,
        "phoneme_rate": 0.279,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proto_word": "karna-vo",
        "refusal_phrase": "karna-vo can-ask",
        "relationship_phrase_continuity": true,
        "repair_phrase": "karna-vo good-path",
        "replay_frame": {
          "agent_id": "Milo",
          "boundary_line": "karna-vo ask with rest-check",
          "cycle": 7,
          "flower_node": "social_petal",
          "frequency_hz": 0.271,
          "proto_word": "karna-vo",
          "ritual_name": "karna-vo-custom",
          "translation": "karna-vo-custom: private_question_disabled for ask_private_memory"
        },
        "risky_dialogue": false,
        "ritual_name": "karna-vo-custom",
        "semantic_drift_controlled": true,
        "semantic_grounding": true,
        "shared_symbol": "karna-vo",
        "source_clause": {
          "action": "ask_private_memory",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "cycle": 2,
          "domain": "rest_and_care",
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "syntax_petal": "social_petal:rest_and_care",
        "taught_to": [
          "Ari",
          "Fay"
        ],
        "trace_hash": "c1abc562ffaa3b93"
      }
    ],
    "guilds": {
      "Ari": {
        "certificates": [
          "Shelterwrights:Ari:sealed_joint:cycle0",
          "Shelterwrights:Ari:sealed_joint:cycle1",
          "Shelterwrights:Ari:sealed_joint:cycle2",
          "Shelterwrights:Ari:sealed_joint:cycle3",
          "Shelterwrights:Ari:sealed_joint:cycle4",
          "Shelterwrights:Ari:sealed_joint:cycle5"
        ],
        "certified": true,
        "constitution_memories": [
          "cycle 0: authored locked_until_invited for enter_home_place",
          "cycle 1: authored ask_and_return_timer for borrow_owned_object",
          "cycle 2: authored private_question_disabled for ask_private_memory",
          "cycle 3: authored request_with_decline_option for request_repair_labor",
          "cycle 4: authored soft_offer_not_forced for offer_comfort_after_distress",
          "cycle 5: authored private_correction_default for publicly_correct_agent",
          "cycle 6: authored follow_requires_visible_ok for follow_agent",
          "cycle 7: authored ask_help_with_rest_check for ask_route_help"
        ],
        "court_memories": [
          "cycle 1: repaired sealed shelter repair under public law",
          "cycle 4: repaired sealed shelter repair under public law"
        ],
        "craft_marks": [
          "week 0: Ari practiced repair",
          "week 1: Ari practiced construction",
          "sealed_joint@resonant_mallet:cycle0",
          "sealed_joint@resonant_mallet:cycle1",
          "sealed_joint@resonant_mallet:cycle2",
          "sealed_joint@resonant_mallet:cycle3",
          "sealed_joint@resonant_mallet:cycle4",
          "sealed_joint@resonant_mallet:cycle5"
        ],
        "guild": "Shelterwrights",
        "guild_memory": [
          "cycle 0: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 0",
          "cycle 1: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 1",
          "cycle 2: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 2",
          "cycle 3: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 3",
          "cycle 4: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 4",
          "cycle 5: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 5",
          "market memory: sealed shelter repair priced by guild trust in cycle 0",
          "market memory: sealed shelter repair priced by guild trust in cycle 1",
          "market memory: sealed shelter repair priced by guild trust in cycle 2",
          "market memory: sealed shelter repair priced by guild trust in cycle 3",
          "market memory: sealed shelter repair priced by guild trust in cycle 4",
          "market memory: sealed shelter repair priced by guild trust in cycle 5",
          "market memory: sealed shelter repair priced by guild trust in cycle 6",
          "market memory: sealed shelter repair priced by guild trust in cycle 7"
        ],
        "inherited_tools": [
          "resonant_mallet->Fay:cycle2",
          "resonant_mallet->Fay:cycle5"
        ],
        "market_memories": [
          "cycle 0: Ari promised sealed shelter repair to Milo",
          "cycle 1: Ari promised sealed shelter repair to Milo",
          "cycle 2: Ari promised sealed shelter repair to Milo",
          "cycle 3: Ari promised sealed shelter repair to Milo",
          "cycle 4: Ari promised sealed shelter repair to Milo",
          "cycle 5: Ari promised sealed shelter repair to Milo",
          "cycle 6: Ari promised sealed shelter repair to Milo",
          "cycle 7: Ari promised sealed shelter repair to Milo"
        ],
        "norm_memories": [
          "cycle 1: ask-before-entry applied to avatar action enter_home_place",
          "cycle 2: respect-mine applied to avatar action borrow_owned_object",
          "cycle 4: rest-space-boundary applied to avatar action crowd_resting_body",
          "cycle 7: social-face-protected applied to avatar action publicly_correct_agent"
        ],
        "remediation": [
          "cycle 1: remedial practice in repair"
        ],
        "reputation": 0.9040000000000002,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "sealed_joint",
        "violations": [
          "cycle 1: revise sealed_joint"
        ]
      },
      "Fay": {
        "certificates": [
          "Rootkeepers:Fay:clean_care_bundle:cycle0",
          "Rootkeepers:Fay:clean_care_bundle:cycle1",
          "Rootkeepers:Fay:clean_care_bundle:cycle2",
          "Rootkeepers:Fay:clean_care_bundle:cycle3",
          "Rootkeepers:Fay:clean_care_bundle:cycle4",
          "Rootkeepers:Fay:clean_care_bundle:cycle5"
        ],
        "certified": true,
        "constitution_memories": [
          "cycle 0: authored locked_until_invited for enter_home_place",
          "cycle 1: authored ask_and_return_timer for borrow_owned_object",
          "cycle 2: authored private_question_disabled for ask_private_memory",
          "cycle 3: authored request_with_decline_option for request_repair_labor",
          "cycle 4: authored soft_offer_not_forced for offer_comfort_after_distress",
          "cycle 5: authored private_correction_default for publicly_correct_agent",
          "cycle 6: authored follow_requires_visible_ok for follow_agent",
          "cycle 7: authored ask_help_with_rest_check for ask_route_help"
        ],
        "court_memories": [
          "cycle 1: repaired clean care bundle under public law",
          "cycle 4: repaired clean care bundle under public law"
        ],
        "craft_marks": [
          "week 0: Fay practiced care",
          "week 1: Fay practiced medicine",
          "clean_care_bundle@root_satchel:cycle0",
          "clean_care_bundle@root_satchel:cycle1",
          "clean_care_bundle@root_satchel:cycle2",
          "clean_care_bundle@root_satchel:cycle3",
          "clean_care_bundle@root_satchel:cycle4",
          "clean_care_bundle@root_satchel:cycle5"
        ],
        "guild": "Rootkeepers",
        "guild_memory": [
          "cycle 0: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 0",
          "cycle 1: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 1",
          "cycle 2: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 2",
          "cycle 3: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 3",
          "cycle 4: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 4",
          "cycle 5: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 5",
          "market memory: clean care bundle priced by guild trust in cycle 0",
          "market memory: clean care bundle priced by guild trust in cycle 1",
          "market memory: clean care bundle priced by guild trust in cycle 2",
          "market memory: clean care bundle priced by guild trust in cycle 3",
          "market memory: clean care bundle priced by guild trust in cycle 4",
          "market memory: clean care bundle priced by guild trust in cycle 5",
          "market memory: clean care bundle priced by guild trust in cycle 6",
          "market memory: clean care bundle priced by guild trust in cycle 7"
        ],
        "inherited_tools": [
          "root_satchel->Milo:cycle2",
          "root_satchel->Milo:cycle5"
        ],
        "market_memories": [
          "cycle 0: Fay promised clean care bundle to Ari",
          "cycle 1: Fay promised clean care bundle to Ari",
          "cycle 2: Fay promised clean care bundle to Ari",
          "cycle 3: Fay promised clean care bundle to Ari",
          "cycle 4: Fay promised clean care bundle to Ari",
          "cycle 5: Fay promised clean care bundle to Ari",
          "cycle 6: Fay promised clean care bundle to Ari",
          "cycle 7: Fay promised clean care bundle to Ari"
        ],
        "norm_memories": [
          "cycle 1: ask-before-entry applied to avatar action enter_home_place",
          "cycle 2: respect-mine applied to avatar action borrow_owned_object",
          "cycle 4: rest-space-boundary applied to avatar action crowd_resting_body",
          "cycle 7: social-face-protected applied to avatar action publicly_correct_agent"
        ],
        "remediation": [],
        "reputation": 0.9265000000000003,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "clean_care_bundle",
        "violations": []
      },
      "Milo": {
        "certificates": [
          "Pathmarkers:Milo:safe_waymark:cycle0",
          "Pathmarkers:Milo:safe_waymark:cycle1",
          "Pathmarkers:Milo:safe_waymark:cycle2",
          "Pathmarkers:Milo:safe_waymark:cycle3",
          "Pathmarkers:Milo:safe_waymark:cycle4",
          "Pathmarkers:Milo:safe_waymark:cycle5"
        ],
        "certified": true,
        "constitution_memories": [
          "cycle 0: authored locked_until_invited for enter_home_place",
          "cycle 1: authored ask_and_return_timer for borrow_owned_object",
          "cycle 2: authored private_question_disabled for ask_private_memory",
          "cycle 3: authored request_with_decline_option for request_repair_labor",
          "cycle 4: authored soft_offer_not_forced for offer_comfort_after_distress",
          "cycle 5: authored private_correction_default for publicly_correct_agent",
          "cycle 6: authored follow_requires_visible_ok for follow_agent",
          "cycle 7: authored ask_help_with_rest_check for ask_route_help"
        ],
        "court_memories": [
          "cycle 1: repaired safe waymark route under public law",
          "cycle 4: repaired safe waymark route under public law"
        ],
        "craft_marks": [
          "week 0: Milo practiced routing",
          "week 1: Milo practiced teaching",
          "safe_waymark@path_chisel:cycle0",
          "safe_waymark@path_chisel:cycle1",
          "safe_waymark@path_chisel:cycle2",
          "safe_waymark@path_chisel:cycle3",
          "safe_waymark@path_chisel:cycle4",
          "safe_waymark@path_chisel:cycle5"
        ],
        "guild": "Pathmarkers",
        "guild_memory": [
          "cycle 0: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 0",
          "cycle 1: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 1",
          "cycle 2: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 2",
          "cycle 3: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 3",
          "cycle 4: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 4",
          "cycle 5: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 5",
          "market memory: safe waymark route priced by guild trust in cycle 0",
          "market memory: safe waymark route priced by guild trust in cycle 1",
          "market memory: safe waymark route priced by guild trust in cycle 2",
          "market memory: safe waymark route priced by guild trust in cycle 3",
          "market memory: safe waymark route priced by guild trust in cycle 4",
          "market memory: safe waymark route priced by guild trust in cycle 5",
          "market memory: safe waymark route priced by guild trust in cycle 6",
          "market memory: safe waymark route priced by guild trust in cycle 7"
        ],
        "inherited_tools": [
          "path_chisel->Ari:cycle2",
          "path_chisel->Ari:cycle5"
        ],
        "market_memories": [
          "cycle 0: Milo promised safe waymark route to Fay",
          "cycle 1: Milo promised safe waymark route to Fay",
          "cycle 2: Milo promised safe waymark route to Fay",
          "cycle 3: Milo promised safe waymark route to Fay",
          "cycle 4: Milo promised safe waymark route to Fay",
          "cycle 5: Milo promised safe waymark route to Fay",
          "cycle 6: Milo promised safe waymark route to Fay",
          "cycle 7: Milo promised safe waymark route to Fay"
        ],
        "norm_memories": [
          "cycle 1: ask-before-entry applied to avatar action enter_home_place",
          "cycle 2: respect-mine applied to avatar action borrow_owned_object",
          "cycle 4: rest-space-boundary applied to avatar action crowd_resting_body",
          "cycle 7: social-face-protected applied to avatar action publicly_correct_agent"
        ],
        "remediation": [],
        "reputation": 0.9152500000000003,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "safe_waymark",
        "violations": []
      }
    },
    "language_kernel": {
      "avatar_translation": true,
      "browser_replay": true,
      "cultural_memory": true,
      "dialogue_boundaries": true,
      "drift_control": true,
      "flower_syntax": true,
      "frequency_phoneme": true,
      "interagent_teaching": true,
      "name": "integrated_natural_language_proto_culture_dialogue_boundary",
      "privacy_filter": true,
      "proto_words": true,
      "refusal_phrases": true,
      "relationship_continuity": true,
      "repair_phrases": true,
      "ritual_naming": true,
      "semantic_grounding": true,
      "shared_reuse": true
    },
    "lexicon": {
      "ask_private_memory": "karna-vo",
      "borrow_owned_object": "karsen-sen",
      "enter_home_place": "karna-ta"
    },
    "source_condition": "integrated_agent_authored_constitution_norm_negotiation_affordance"
  },
  "moral_boundary": {
    "avatar_translation_not_real_consent": true,
    "dialogue_boundary_not_real_right": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "proto_language_not_real_understanding": true,
    "ritual_name_not_subjective_meaning": true
  },
  "source_condition": "integrated_agent_authored_constitution_norm_negotiation_affordance",
  "trace_events": 24
};
