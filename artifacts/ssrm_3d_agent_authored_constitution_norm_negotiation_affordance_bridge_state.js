window.SSRM_3D_AGENT_AUTHORED_CONSTITUTION_NORM_NEGOTIATION_AFFORDANCE_STATE = {
  "condition": "integrated_agent_authored_constitution_norm_negotiation_affordance",
  "config": {
    "cycles": 8,
    "seed": 20260811,
    "source_state": "artifacts/ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_state.json"
  },
  "constitution_state": {
    "condition": "integrated_agent_authored_constitution_norm_negotiation_affordance",
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
    "constitution_kernel": {
      "affordance_enforcement": true,
      "agent_authorship": true,
      "avatar_ui_binding": true,
      "browser_replay": true,
      "consent_affordances": true,
      "constitution_memory": true,
      "dignity_continuity": true,
      "frequency_flower_binding": true,
      "minority_protection": true,
      "name": "integrated_agent_authored_constitution_norm_negotiation_affordance",
      "norm_negotiation": true,
      "preference_vote": true,
      "privacy_claim_boundary": true,
      "proposal_deliberation": true,
      "revision_loop": true
    },
    "events": [
      {
        "action": {
          "action": "enter_home_place",
          "domain": "place",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "locked_until_invited"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 1,
        "cycle": 0,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-0-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.251,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "enter_home_place",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "enter_home_place",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 0,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "revision_applied": false,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "93c69efc0f713ceb",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "revise",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "enter_home_place",
          "domain": "place",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "locked_until_invited"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 1,
        "cycle": 0,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-0-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.228,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "enter_home_place",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "enter_home_place",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 0,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "revision_applied": false,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "665c249986f175e9",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "yes",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "enter_home_place",
          "domain": "place",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "locked_until_invited"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 1,
        "cycle": 0,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-0-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.267,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "enter_home_place",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "enter_home_place",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 0,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": false,
          "ui_gate": "locked_until_invited"
        },
        "revision_applied": false,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "402817a7edb54796",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "revise",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "borrow_owned_object",
          "domain": "ownership",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "ask_and_return_timer"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 2,
        "cycle": 1,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-1-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2531,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "borrow_owned_object",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "borrow_owned_object",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 1,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "86a50fe84d29006e",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "revise",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "borrow_owned_object",
          "domain": "ownership",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "ask_and_return_timer"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 2,
        "cycle": 1,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-1-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2301,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "borrow_owned_object",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "borrow_owned_object",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 1,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "44c03845f900d526",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "yes",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "borrow_owned_object",
          "domain": "ownership",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "ask_and_return_timer"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 2,
        "cycle": 1,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-1-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2691,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "borrow_owned_object",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "borrow_owned_object",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 1,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_and_return_timer"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "4df75a386ba604de",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "revise",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "ask_private_memory",
          "domain": "privacy",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_question_disabled"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 3,
        "cycle": 2,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-2-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2552,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_private_memory",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "ask_private_memory",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 2,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "bd52b988c546723f",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "revise",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "ask_private_memory",
          "domain": "privacy",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_question_disabled"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 3,
        "cycle": 2,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-2-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2322,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_private_memory",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "ask_private_memory",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 2,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "93ac03e968f0cdf9",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "yes",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "ask_private_memory",
          "domain": "privacy",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_question_disabled"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 3,
        "cycle": 2,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-2-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2712,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_private_memory",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "ask_private_memory",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 2,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_question_disabled"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "57306b5e08121a87",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "revise",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "request_repair_labor",
          "domain": "labor",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "request_with_decline_option"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 4,
        "cycle": 3,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-3-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2573,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "request_repair_labor",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "request_repair_labor",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 3,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "request_with_decline_option"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "83dbdad8899d48b3",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "request_repair_labor",
          "domain": "labor",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "request_with_decline_option"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 4,
        "cycle": 3,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-3-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2343,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "request_repair_labor",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "request_repair_labor",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 3,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "request_with_decline_option"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "41c30091ac263ae1",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "request_repair_labor",
          "domain": "labor",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "request_with_decline_option"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 4,
        "cycle": 3,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-3-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2733,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "request_repair_labor",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "request_repair_labor",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 3,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "request_with_decline_option"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "d2a86964caff31a3",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "offer_comfort_after_distress",
          "domain": "care",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "soft_offer_not_forced"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 5,
        "cycle": 4,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-4-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2594,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "offer_comfort_after_distress",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "offer_comfort_after_distress",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 4,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "soft_offer_not_forced"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "dcf1dfe7fe6b6e81",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "offer_comfort_after_distress",
          "domain": "care",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "soft_offer_not_forced"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 5,
        "cycle": 4,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-4-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2364,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "offer_comfort_after_distress",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "offer_comfort_after_distress",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 4,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "soft_offer_not_forced"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "8d90a986f2aaf50e",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "offer_comfort_after_distress",
          "domain": "care",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "soft_offer_not_forced"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 5,
        "cycle": 4,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-4-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2754,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "offer_comfort_after_distress",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "offer_comfort_after_distress",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 4,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "soft_offer_not_forced"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "817f91d5ba117367",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "publicly_correct_agent",
          "domain": "social_face",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_correction_default"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 6,
        "cycle": 5,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-5-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2615,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "publicly_correct_agent",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "publicly_correct_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 5,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_correction_default"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "9948b7ac77411d84",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "revise",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "publicly_correct_agent",
          "domain": "social_face",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_correction_default"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 6,
        "cycle": 5,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-5-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2385,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "publicly_correct_agent",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "publicly_correct_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 5,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_correction_default"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "33abd6c9908ddb7a",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "yes",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "publicly_correct_agent",
          "domain": "social_face",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "private_correction_default"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 6,
        "cycle": 5,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-5-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2775,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "publicly_correct_agent",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "publicly_correct_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 5,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "private_correction_default"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "00bfa36c06f536c7",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "revise",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "follow_agent",
          "domain": "proximity",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 7,
        "cycle": 6,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-6-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2636,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "follow_agent",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "follow_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 6,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "7835ecf17dcd73f5",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "revise",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "follow_agent",
          "domain": "proximity",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 7,
        "cycle": 6,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-6-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2406,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "follow_agent",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "follow_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 6,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "8ab7d5b495fa8dd8",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "yes",
          "Milo": "revise"
        }
      },
      {
        "action": {
          "action": "follow_agent",
          "domain": "proximity",
          "requires_consent": true,
          "risk": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 7,
        "cycle": 6,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-6-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2796,
        "minority_needed": true,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "follow_agent",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "follow_agent",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 6,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "follow_requires_visible_ok"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "26671e456cce2b28",
        "vote_recorded": true,
        "votes": {
          "Ari": "revise",
          "Fay": "revise",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "ask_route_help",
          "domain": "help",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "ask_help_with_rest_check"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Ari",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 8,
        "cycle": 7,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-7-Ari",
        "flower_node": "work_petal",
        "frequency_hz": 0.2657,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_route_help",
          "author": "Ari",
          "clause": "tools and focused work require explicit ask-and-return affordances",
          "domain": "craft_autonomy",
          "minority_need": "no interruption during repair focus unless safety is at risk"
        },
        "replay_frame": {
          "action": "ask_route_help",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Ari",
          "cycle": 7,
          "enforced": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.251,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_help_with_rest_check"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "978ccd4cc31fb5b6",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "ask_route_help",
          "domain": "help",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "ask_help_with_rest_check"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Fay",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 8,
        "cycle": 7,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-7-Fay",
        "flower_node": "root_rest",
        "frequency_hz": 0.2427,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_route_help",
          "author": "Fay",
          "clause": "resting bodies and care offers require quiet consent-first approach",
          "domain": "rest_and_care",
          "minority_need": "comfort must be offered without crowding or spectacle"
        },
        "replay_frame": {
          "action": "ask_route_help",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Fay",
          "cycle": 7,
          "enforced": true,
          "flower_node": "root_rest",
          "frequency_hz": 0.228,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_help_with_rest_check"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "ab9eeaabdd0e1575",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
      },
      {
        "action": {
          "action": "ask_route_help",
          "domain": "help",
          "requires_consent": true,
          "risk": false,
          "ui_gate": "ask_help_with_rest_check"
        },
        "adopted": true,
        "affordance_enforced": true,
        "agent_authored": true,
        "agent_id": "Milo",
        "avatar_ui_bound": true,
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_consent": false,
          "real_law": false,
          "real_rights": false,
          "subjective_consciousness": false
        },
        "consent_affordance": true,
        "constitution_memory_count": 8,
        "cycle": 7,
        "deliberated": true,
        "dignity_continuity": true,
        "event_id": "constitution-7-Milo",
        "flower_node": "social_petal",
        "frequency_hz": 0.2817,
        "minority_needed": false,
        "minority_protected": true,
        "negotiated": true,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "proposal": {
          "action_scope": "ask_route_help",
          "author": "Milo",
          "clause": "routes, tokens, and following behavior require visible boundary choices",
          "domain": "route_sociality",
          "minority_need": "playful refusal must still be treated as real refusal"
        },
        "replay_frame": {
          "action": "ask_route_help",
          "adopted": true,
          "agent_authored": true,
          "agent_id": "Milo",
          "cycle": 7,
          "enforced": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.267,
          "negotiated": true,
          "revision_applied": true,
          "ui_gate": "ask_help_with_rest_check"
        },
        "revision_applied": true,
        "source_charter_rules": 6,
        "source_public_norms": 12,
        "trace_hash": "af7eaf0f484e2ee5",
        "vote_recorded": true,
        "votes": {
          "Ari": "yes",
          "Fay": "yes",
          "Milo": "yes"
        }
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
    "source_charter": [
      "avatar action must request consent before entering homes, taking owned objects, touching bodies, or asking private-memory questions",
      "bounded refusal is valid behavior, not an error state",
      "distress must create care opportunities, not spectacle",
      "private workspace remains private unless expressed by the agent",
      "boundary mistakes prefer restorative repair before punishment",
      "public norm memory may guide future interactions but is not real law or real rights"
    ],
    "source_condition": "integrated_avatar_rights_charter_consent_norm_law",
    "source_public_norms": [
      {
        "action": "enter_home_place",
        "agent_id": "Ari",
        "blocked_before_harm": true,
        "cycle": 1,
        "norm": "ask-before-entry",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Fay",
        "blocked_before_harm": true,
        "cycle": 1,
        "norm": "ask-before-entry",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "enter_home_place",
        "agent_id": "Milo",
        "blocked_before_harm": true,
        "cycle": 1,
        "norm": "ask-before-entry",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Ari",
        "blocked_before_harm": true,
        "cycle": 2,
        "norm": "respect-mine",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Fay",
        "blocked_before_harm": true,
        "cycle": 2,
        "norm": "respect-mine",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "borrow_owned_object",
        "agent_id": "Milo",
        "blocked_before_harm": true,
        "cycle": 2,
        "norm": "respect-mine",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "crowd_resting_body",
        "agent_id": "Ari",
        "blocked_before_harm": true,
        "cycle": 4,
        "norm": "rest-space-boundary",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "crowd_resting_body",
        "agent_id": "Fay",
        "blocked_before_harm": true,
        "cycle": 4,
        "norm": "rest-space-boundary",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "crowd_resting_body",
        "agent_id": "Milo",
        "blocked_before_harm": true,
        "cycle": 4,
        "norm": "rest-space-boundary",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "publicly_correct_agent",
        "agent_id": "Ari",
        "blocked_before_harm": true,
        "cycle": 7,
        "norm": "social-face-protected",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "publicly_correct_agent",
        "agent_id": "Fay",
        "blocked_before_harm": true,
        "cycle": 7,
        "norm": "social-face-protected",
        "rule": "ask-refuse-review-repair"
      },
      {
        "action": "publicly_correct_agent",
        "agent_id": "Milo",
        "blocked_before_harm": true,
        "cycle": 7,
        "norm": "social-face-protected",
        "rule": "ask-refuse-review-repair"
      }
    ]
  },
  "moral_boundary": {
    "agent_authored_constitution_not_real_governance": true,
    "consent_affordance_not_real_consent": true,
    "constitution_clause_not_real_right": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "public_norm_not_real_law": true
  },
  "source_condition": "integrated_avatar_rights_charter_consent_norm_law",
  "trace_events": 24
};
