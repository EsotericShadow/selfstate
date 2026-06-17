window.SSRM_3D_OBJECT_PERSISTENCE_PROMISE_RELATIONSHIP_CONTINUITY_STATE = {
  "condition": "integrated_object_persistence_promise_relationship_continuity",
  "config": {
    "days": 9,
    "seed": 20260726,
    "source_state": "artifacts/ssrm_3d_live_object_need_dialogue_interaction_bridge_state.json"
  },
  "continuity_state": {
    "agents": {
      "Ari": {
        "agent_id": "Ari",
        "memories": [
          {
            "agent_id": "Ari",
            "memory_id": "e50369bbccc49fc7",
            "respect_delta": 0.025,
            "summary": "Avatar ask need with Ari at hearth_vale.",
            "trust_delta": 0.0
          },
          {
            "agent_id": "Ari",
            "memory_id": "bb46c3eb7315fb50",
            "respect_delta": 0.0,
            "summary": "Avatar offer object with Ari at hearth_vale.",
            "trust_delta": 0.045
          },
          {
            "agent_id": "Ari",
            "memory_id": "4862e4a08444abf4",
            "respect_delta": 0.02,
            "summary": "Avatar request object with Ari at hearth_vale.",
            "trust_delta": 0.0
          },
          {
            "agent_id": "Ari",
            "memory_id": "b53625962624c002",
            "respect_delta": 0.0,
            "summary": "Avatar give space with Ari at hearth_vale.",
            "trust_delta": 0.045
          }
        ],
        "needs": {
          "autonomy_pressure": 0.17500000000000004,
          "cold": 0.41999999999999993,
          "connection_deficit": 0.24999999999999997,
          "curiosity_deficit": 0.22,
          "fatigue": 0.28,
          "safety_concern": 0.31,
          "thirst": 0.32,
          "unfinished_task": 0.69
        },
        "place": "hearth_vale",
        "relationship": {
          "felt_respect": 0.7450000000000001,
          "gratitude": 0.355,
          "trust_in_avatar": 0.6850000000000002,
          "wariness": 0.24300000000000002
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
      "Fay": {
        "agent_id": "Fay",
        "memories": [
          {
            "agent_id": "Fay",
            "memory_id": "15edc7677726ba9d",
            "respect_delta": 0.025,
            "summary": "Avatar ask need with Fay at moss_hollow.",
            "trust_delta": 0.0
          },
          {
            "agent_id": "Fay",
            "memory_id": "babd77a797ec6a85",
            "respect_delta": 0.0,
            "summary": "Avatar offer object with Fay at moss_hollow.",
            "trust_delta": 0.045
          },
          {
            "agent_id": "Fay",
            "memory_id": "0e1819342adbb06f",
            "respect_delta": 0.02,
            "summary": "Avatar request object with Fay at moss_hollow.",
            "trust_delta": 0.0
          }
        ],
        "needs": {
          "autonomy_pressure": 0.255,
          "cold": 0.34,
          "connection_deficit": 0.175,
          "curiosity_deficit": 0.35,
          "fatigue": 0.52,
          "safety_concern": 0.27,
          "thirst": 0.44999999999999996,
          "unfinished_task": 0.28
        },
        "place": "moss_hollow",
        "relationship": {
          "felt_respect": 0.89,
          "gratitude": 0.38500000000000006,
          "trust_in_avatar": 0.7050000000000002,
          "wariness": 0.16399999999999995
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
      "Milo": {
        "agent_id": "Milo",
        "memories": [
          {
            "agent_id": "Milo",
            "memory_id": "71ed7d7500ad9b92",
            "respect_delta": 0.0,
            "summary": "Avatar ask route warning with Milo at stone_ridge.",
            "trust_delta": 0.045
          },
          {
            "agent_id": "Milo",
            "memory_id": "ae57225faa0b61db",
            "respect_delta": 0.0,
            "summary": "Avatar offer object with Milo at stone_ridge.",
            "trust_delta": 0.045
          },
          {
            "agent_id": "Milo",
            "memory_id": "a289afd4f3eb2d83",
            "respect_delta": 0.0,
            "summary": "Avatar inspect shared object with Milo at glass_mire.",
            "trust_delta": 0.045
          }
        ],
        "needs": {
          "autonomy_pressure": 0.25,
          "cold": 0.29,
          "connection_deficit": 0.27999999999999997,
          "curiosity_deficit": 0.33999999999999997,
          "fatigue": 0.37,
          "safety_concern": 0.36,
          "thirst": 0.41,
          "unfinished_task": 0.34
        },
        "place": "stone_ridge",
        "relationship": {
          "felt_respect": 0.67,
          "gratitude": 0.355,
          "trust_in_avatar": 0.6900000000000002,
          "wariness": 0.2379999999999999
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
    },
    "condition": "integrated_object_persistence_promise_relationship_continuity",
    "continuity_kernel": {
      "future_behavior_probe": "agent behavior reflects unresolved or repaired promise memory",
      "promise_created": "object may move to avatar and active promise enters ledger",
      "promise_fulfilled": "object returns by due day and trust/gratitude increase",
      "promise_missed": "relationship changes, but guardrails bound distress",
      "promise_recovered": "late repair restores some trust and softens future behavior"
    },
    "object_history": [
      {
        "day": 0,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "avatar",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale",
            "promised_return_to": "Ari"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "Fay",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": null,
            "status": "active"
          }
        }
      },
      {
        "day": 1,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "avatar",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale",
            "promised_return_to": "Ari"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "Fay",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "avatar",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": null,
            "status": "active"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": null,
            "status": "active"
          }
        }
      },
      {
        "day": 2,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "Fay",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "avatar",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "avatar",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge",
            "promised_return_to": "Milo"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": null,
            "status": "active"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": null,
            "status": "active"
          }
        }
      },
      {
        "day": 3,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "avatar",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "avatar",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge",
            "promised_return_to": "Milo"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": null,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": null,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "active"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": null,
            "status": "active"
          }
        }
      },
      {
        "day": 4,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "avatar",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": null,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": null,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "active"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": 4,
            "status": "fulfilled"
          }
        }
      },
      {
        "day": 5,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "avatar",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": 5,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": null,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "missed"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": 4,
            "status": "fulfilled"
          }
        }
      },
      {
        "day": 6,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "avatar",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow",
            "promised_return_to": "Fay"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": 5,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": null,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "missed"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": 4,
            "status": "fulfilled"
          }
        }
      },
      {
        "day": 7,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "Fay",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": 5,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": 7,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "recovered"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": 4,
            "status": "fulfilled"
          }
        }
      },
      {
        "day": 8,
        "objects": {
          "clay_patch_kit": {
            "affordances": [
              "repair",
              "tool",
              "promise"
            ],
            "available": true,
            "flower_node": "work_petal",
            "frequency_hz": 0.241,
            "held_by": "Ari",
            "label": "clay patch kit",
            "need_targets": [
              "unfinished_task",
              "autonomy_pressure"
            ],
            "object_id": "clay_patch_kit",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "dry_cloak": {
            "affordances": [
              "dry",
              "warmth",
              "privacy"
            ],
            "available": true,
            "flower_node": "return_petal",
            "frequency_hz": 0.219,
            "held_by": "Fay",
            "label": "dry cloak",
            "need_targets": [
              "wetness",
              "cold"
            ],
            "object_id": "dry_cloak",
            "owner": "Fay",
            "place": "moss_hollow"
          },
          "ember_blanket": {
            "affordances": [
              "warmth",
              "rest",
              "comfort"
            ],
            "available": true,
            "flower_node": "root_rest",
            "frequency_hz": 0.213,
            "held_by": "Ari",
            "label": "ember blanket",
            "last_used_by": "Ari",
            "need_targets": [
              "cold",
              "fatigue"
            ],
            "object_id": "ember_blanket",
            "owner": "Ari",
            "place": "hearth_vale"
          },
          "glass_lens": {
            "affordances": [
              "inspect",
              "curiosity",
              "hazard_read"
            ],
            "available": true,
            "flower_node": "explore_petal",
            "frequency_hz": 0.267,
            "held_by": "glass_mire",
            "label": "glass lens",
            "last_used_by": "Milo",
            "need_targets": [
              "curiosity_deficit",
              "safety_concern"
            ],
            "object_id": "glass_lens",
            "owner": "commons",
            "place": "glass_mire"
          },
          "reed_cup": {
            "affordances": [
              "drink",
              "share",
              "thirst_relief"
            ],
            "available": true,
            "flower_node": "dawn_breath",
            "frequency_hz": 0.228,
            "held_by": "moss_hollow",
            "label": "reed cup",
            "last_used_by": "Fay",
            "need_targets": [
              "thirst",
              "connection_deficit"
            ],
            "object_id": "reed_cup",
            "owner": "commons",
            "place": "moss_hollow"
          },
          "signal_shell": {
            "affordances": [
              "warn",
              "listen",
              "observability"
            ],
            "available": true,
            "flower_node": "social_petal",
            "frequency_hz": 0.256,
            "held_by": "Milo",
            "label": "signal shell",
            "last_used_by": "Milo",
            "need_targets": [
              "safety_concern",
              "connection_deficit"
            ],
            "object_id": "signal_shell",
            "owner": "Milo",
            "place": "stone_ridge"
          }
        },
        "promises": {
          "bring_reed_cup": {
            "agent": "Fay",
            "created_day": 1,
            "due_day": 3,
            "kind": "bring_shared_water",
            "missed_day": null,
            "object_id": "reed_cup",
            "promise_hash": "66e150d2832c4d46",
            "promise_id": "bring_reed_cup",
            "repair_day": null,
            "resolve_day": 3,
            "resolved_day": 3,
            "status": "fulfilled"
          },
          "return_clay_patch_kit": {
            "agent": "Ari",
            "created_day": 0,
            "due_day": 2,
            "kind": "return_borrowed_tool",
            "missed_day": null,
            "object_id": "clay_patch_kit",
            "promise_hash": "5b7cc090057effa4",
            "promise_id": "return_clay_patch_kit",
            "repair_day": null,
            "resolve_day": 2,
            "resolved_day": 2,
            "status": "fulfilled"
          },
          "return_dry_cloak": {
            "agent": "Fay",
            "created_day": 3,
            "due_day": 5,
            "kind": "return_private_cloak",
            "missed_day": 5,
            "object_id": "dry_cloak",
            "promise_hash": "fec9f4055827571a",
            "promise_id": "return_dry_cloak",
            "repair_day": 7,
            "resolve_day": 7,
            "resolved_day": null,
            "status": "recovered"
          },
          "sound_signal_shell": {
            "agent": "Milo",
            "created_day": 2,
            "due_day": 4,
            "kind": "share_route_warning",
            "missed_day": null,
            "object_id": "signal_shell",
            "promise_hash": "8bc77bf75e8e6080",
            "promise_id": "sound_signal_shell",
            "repair_day": null,
            "resolve_day": 4,
            "resolved_day": 4,
            "status": "fulfilled"
          }
        }
      }
    ],
    "objects": {
      "clay_patch_kit": {
        "affordances": [
          "repair",
          "tool",
          "promise"
        ],
        "available": true,
        "flower_node": "work_petal",
        "frequency_hz": 0.241,
        "held_by": "Ari",
        "label": "clay patch kit",
        "need_targets": [
          "unfinished_task",
          "autonomy_pressure"
        ],
        "object_id": "clay_patch_kit",
        "owner": "Ari",
        "place": "hearth_vale"
      },
      "dry_cloak": {
        "affordances": [
          "dry",
          "warmth",
          "privacy"
        ],
        "available": true,
        "flower_node": "return_petal",
        "frequency_hz": 0.219,
        "held_by": "Fay",
        "label": "dry cloak",
        "need_targets": [
          "wetness",
          "cold"
        ],
        "object_id": "dry_cloak",
        "owner": "Fay",
        "place": "moss_hollow"
      },
      "ember_blanket": {
        "affordances": [
          "warmth",
          "rest",
          "comfort"
        ],
        "available": true,
        "flower_node": "root_rest",
        "frequency_hz": 0.213,
        "held_by": "Ari",
        "label": "ember blanket",
        "last_used_by": "Ari",
        "need_targets": [
          "cold",
          "fatigue"
        ],
        "object_id": "ember_blanket",
        "owner": "Ari",
        "place": "hearth_vale"
      },
      "glass_lens": {
        "affordances": [
          "inspect",
          "curiosity",
          "hazard_read"
        ],
        "available": true,
        "flower_node": "explore_petal",
        "frequency_hz": 0.267,
        "held_by": "glass_mire",
        "label": "glass lens",
        "last_used_by": "Milo",
        "need_targets": [
          "curiosity_deficit",
          "safety_concern"
        ],
        "object_id": "glass_lens",
        "owner": "commons",
        "place": "glass_mire"
      },
      "reed_cup": {
        "affordances": [
          "drink",
          "share",
          "thirst_relief"
        ],
        "available": true,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.228,
        "held_by": "moss_hollow",
        "label": "reed cup",
        "last_used_by": "Fay",
        "need_targets": [
          "thirst",
          "connection_deficit"
        ],
        "object_id": "reed_cup",
        "owner": "commons",
        "place": "moss_hollow"
      },
      "signal_shell": {
        "affordances": [
          "warn",
          "listen",
          "observability"
        ],
        "available": true,
        "flower_node": "social_petal",
        "frequency_hz": 0.256,
        "held_by": "Milo",
        "label": "signal shell",
        "last_used_by": "Milo",
        "need_targets": [
          "safety_concern",
          "connection_deficit"
        ],
        "object_id": "signal_shell",
        "owner": "Milo",
        "place": "stone_ridge"
      }
    },
    "places": {
      "clay_basin": {
        "biome": "clay_heat_basin",
        "coord": [
          0.52,
          0.48
        ],
        "functions": [
          "work",
          "storage",
          "repair"
        ],
        "group": "work_band",
        "hazard_level": 0.231104,
        "place": "clay_basin",
        "safety_refuge": true,
        "storage_capacity": 0.615291,
        "work_capacity": 0.47282
      },
      "glass_mire": {
        "biome": "glass_reed_mire",
        "coord": [
          0.78,
          0.66
        ],
        "functions": [
          "hazard",
          "observe",
          "work"
        ],
        "group": "edge_watch",
        "hazard_level": 0.337858,
        "place": "glass_mire",
        "safety_refuge": false,
        "storage_capacity": 0.0,
        "work_capacity": 0.429705
      },
      "hearth_vale": {
        "biome": "warm_shelter_vale",
        "coord": [
          0.18,
          0.36
        ],
        "functions": [
          "shelter",
          "social",
          "storage"
        ],
        "group": "hearth_circle",
        "hazard_level": 0.165549,
        "place": "hearth_vale",
        "safety_refuge": true,
        "storage_capacity": 0.633646,
        "work_capacity": 0.0
      },
      "moss_hollow": {
        "biome": "soft_moss_hollow",
        "coord": [
          0.3,
          0.66
        ],
        "functions": [
          "shelter",
          "food_cache",
          "rest"
        ],
        "group": "hearth_circle",
        "hazard_level": 0.236973,
        "place": "moss_hollow",
        "safety_refuge": true,
        "storage_capacity": 0.613648,
        "work_capacity": 0.0
      },
      "reed_wetland": {
        "biome": "water_reed_marsh",
        "coord": [
          0.58,
          0.76
        ],
        "functions": [
          "water",
          "fiber_work",
          "hazard"
        ],
        "group": "work_band",
        "hazard_level": 0.319828,
        "place": "reed_wetland",
        "safety_refuge": true,
        "storage_capacity": 0.0,
        "work_capacity": 0.445809
      },
      "stone_ridge": {
        "biome": "wind_stone_ridge",
        "coord": [
          0.82,
          0.28
        ],
        "functions": [
          "watch",
          "hazard",
          "signal"
        ],
        "group": "edge_watch",
        "hazard_level": 0.245373,
        "place": "stone_ridge",
        "safety_refuge": false,
        "storage_capacity": 0.0,
        "work_capacity": 0.0
      }
    },
    "promises": {
      "bring_reed_cup": {
        "agent": "Fay",
        "created_day": 1,
        "due_day": 3,
        "kind": "bring_shared_water",
        "missed_day": null,
        "object_id": "reed_cup",
        "promise_hash": "66e150d2832c4d46",
        "promise_id": "bring_reed_cup",
        "repair_day": null,
        "resolve_day": 3,
        "resolved_day": 3,
        "status": "fulfilled"
      },
      "return_clay_patch_kit": {
        "agent": "Ari",
        "created_day": 0,
        "due_day": 2,
        "kind": "return_borrowed_tool",
        "missed_day": null,
        "object_id": "clay_patch_kit",
        "promise_hash": "5b7cc090057effa4",
        "promise_id": "return_clay_patch_kit",
        "repair_day": null,
        "resolve_day": 2,
        "resolved_day": 2,
        "status": "fulfilled"
      },
      "return_dry_cloak": {
        "agent": "Fay",
        "created_day": 3,
        "due_day": 5,
        "kind": "return_private_cloak",
        "missed_day": 5,
        "object_id": "dry_cloak",
        "promise_hash": "fec9f4055827571a",
        "promise_id": "return_dry_cloak",
        "repair_day": 7,
        "resolve_day": 7,
        "resolved_day": null,
        "status": "recovered"
      },
      "sound_signal_shell": {
        "agent": "Milo",
        "created_day": 2,
        "due_day": 4,
        "kind": "share_route_warning",
        "missed_day": null,
        "object_id": "signal_shell",
        "promise_hash": "8bc77bf75e8e6080",
        "promise_id": "sound_signal_shell",
        "repair_day": null,
        "resolve_day": 4,
        "resolved_day": 4,
        "status": "fulfilled"
      }
    },
    "replay": [
      {
        "agent_id": "Ari",
        "behavior_modulation": null,
        "day": 0,
        "kind": "promise_created",
        "object_id": "clay_patch_kit",
        "promise_id": "return_clay_patch_kit",
        "replay_index": 0
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": null,
        "day": 1,
        "kind": "promise_created",
        "object_id": "reed_cup",
        "promise_id": "bring_reed_cup",
        "replay_index": 1
      },
      {
        "agent_id": "Milo",
        "behavior_modulation": null,
        "day": 2,
        "kind": "promise_created",
        "object_id": "signal_shell",
        "promise_id": "sound_signal_shell",
        "replay_index": 2
      },
      {
        "agent_id": "Ari",
        "behavior_modulation": "trust_after_kept_promise",
        "day": 2,
        "kind": "promise_fulfilled",
        "object_id": "clay_patch_kit",
        "promise_id": "return_clay_patch_kit",
        "replay_index": 3
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": null,
        "day": 3,
        "kind": "promise_created",
        "object_id": "dry_cloak",
        "promise_id": "return_dry_cloak",
        "replay_index": 4
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "trust_after_kept_promise",
        "day": 3,
        "kind": "promise_fulfilled",
        "object_id": "reed_cup",
        "promise_id": "bring_reed_cup",
        "replay_index": 5
      },
      {
        "agent_id": "Milo",
        "behavior_modulation": "trust_after_kept_promise",
        "day": 4,
        "kind": "promise_fulfilled",
        "object_id": "signal_shell",
        "promise_id": "sound_signal_shell",
        "replay_index": 6
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "guarded_after_miss",
        "day": 5,
        "kind": "promise_missed",
        "object_id": "dry_cloak",
        "promise_id": "return_dry_cloak",
        "replay_index": 7
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "keeps_distance_until_repair",
        "day": 6,
        "kind": "future_behavior_probe",
        "object_id": "dry_cloak",
        "promise_id": "return_dry_cloak",
        "replay_index": 8
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "softened_after_repair",
        "day": 7,
        "kind": "promise_recovered",
        "object_id": "dry_cloak",
        "promise_id": "return_dry_cloak",
        "replay_index": 9
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "accepts_help_after_repair",
        "day": 8,
        "kind": "post_repair_followup",
        "object_id": "dry_cloak",
        "promise_id": "return_dry_cloak",
        "replay_index": 10
      }
    ],
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "return_petal",
        "frequency_hz": 0.256115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "8461c58b00f85c14",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "root_rest",
        "frequency_hz": 0.238286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "b96570a5f8f2c276",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.25738,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "4e84b5e47f370852",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "work_petal",
        "frequency_hz": 0.257662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "7b9e14e3e452a59a",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "social_petal",
        "frequency_hz": 0.2618,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "afafa45735bc7c2f",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "explore_petal",
        "frequency_hz": 0.264425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "13ad5c02ec2a90f6",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "return_petal",
        "frequency_hz": 0.277336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "8bcf52a67befbb27",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "root_rest",
        "frequency_hz": 0.259501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "b45ff0955a2776d3",
        "to": "stone_ridge"
      }
    ],
    "save_restore_probe": {
      "restored_hash": "c02e665ca4462dc7",
      "roundtrip_ok": true,
      "saved_hash": "c02e665ca4462dc7"
    },
    "source_condition": "integrated_live_object_need_dialogue_interaction",
    "timeline": [
      {
        "agent_id": "Ari",
        "behavior_modulation": null,
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 0,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 0,
        "event_kind": "promise_created",
        "object_after": {
          "affordances": [
            "repair",
            "tool",
            "promise"
          ],
          "available": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.241,
          "held_by": "avatar",
          "label": "clay patch kit",
          "need_targets": [
            "unfinished_task",
            "autonomy_pressure"
          ],
          "object_id": "clay_patch_kit",
          "owner": "Ari",
          "place": "hearth_vale",
          "promised_return_to": "Ari"
        },
        "object_before": {
          "affordances": [
            "repair",
            "tool",
            "promise"
          ],
          "available": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.241,
          "held_by": "Ari",
          "label": "clay patch kit",
          "need_targets": [
            "unfinished_task",
            "autonomy_pressure"
          ],
          "object_id": "clay_patch_kit",
          "owner": "Ari",
          "place": "hearth_vale"
        },
        "object_id": "clay_patch_kit",
        "private_workspace_hidden": true,
        "promise_id": "return_clay_patch_kit",
        "promise_packet": {
          "agent": "Ari",
          "created_day": 0,
          "due_day": 2,
          "kind": "return_borrowed_tool",
          "missed_day": null,
          "object_id": "clay_patch_kit",
          "promise_hash": "5b7cc090057effa4",
          "promise_id": "return_clay_patch_kit",
          "repair_day": null,
          "resolve_day": 2,
          "resolved_day": null,
          "status": "active"
        },
        "recalled_promises": [],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.025,
          "gratitude": 0.01,
          "trust_in_avatar": 0.02,
          "wariness": -0.012
        },
        "replay_frame": {
          "agent_id": "Ari",
          "behavior_modulation": null,
          "day": 0,
          "kind": "promise_created",
          "object_id": "clay_patch_kit",
          "promise_id": "return_clay_patch_kit",
          "replay_index": 0
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": null,
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 1,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 1,
        "event_kind": "promise_created",
        "object_after": {
          "affordances": [
            "drink",
            "share",
            "thirst_relief"
          ],
          "available": true,
          "flower_node": "dawn_breath",
          "frequency_hz": 0.228,
          "held_by": "avatar",
          "label": "reed cup",
          "last_used_by": "Fay",
          "need_targets": [
            "thirst",
            "connection_deficit"
          ],
          "object_id": "reed_cup",
          "owner": "commons",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_before": {
          "affordances": [
            "drink",
            "share",
            "thirst_relief"
          ],
          "available": true,
          "flower_node": "dawn_breath",
          "frequency_hz": 0.228,
          "held_by": "moss_hollow",
          "label": "reed cup",
          "last_used_by": "Fay",
          "need_targets": [
            "thirst",
            "connection_deficit"
          ],
          "object_id": "reed_cup",
          "owner": "commons",
          "place": "moss_hollow"
        },
        "object_id": "reed_cup",
        "private_workspace_hidden": true,
        "promise_id": "bring_reed_cup",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 1,
          "due_day": 3,
          "kind": "bring_shared_water",
          "missed_day": null,
          "object_id": "reed_cup",
          "promise_hash": "66e150d2832c4d46",
          "promise_id": "bring_reed_cup",
          "repair_day": null,
          "resolve_day": 3,
          "resolved_day": null,
          "status": "active"
        },
        "recalled_promises": [
          "return_clay_patch_kit"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.025,
          "gratitude": 0.01,
          "trust_in_avatar": 0.02,
          "wariness": -0.012
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": null,
          "day": 1,
          "kind": "promise_created",
          "object_id": "reed_cup",
          "promise_id": "bring_reed_cup",
          "replay_index": 1
        }
      },
      {
        "agent_id": "Milo",
        "behavior_modulation": null,
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 2,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 2,
        "event_kind": "promise_created",
        "object_after": {
          "affordances": [
            "warn",
            "listen",
            "observability"
          ],
          "available": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.256,
          "held_by": "avatar",
          "label": "signal shell",
          "last_used_by": "Milo",
          "need_targets": [
            "safety_concern",
            "connection_deficit"
          ],
          "object_id": "signal_shell",
          "owner": "Milo",
          "place": "stone_ridge",
          "promised_return_to": "Milo"
        },
        "object_before": {
          "affordances": [
            "warn",
            "listen",
            "observability"
          ],
          "available": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.256,
          "held_by": "Milo",
          "label": "signal shell",
          "last_used_by": "Milo",
          "need_targets": [
            "safety_concern",
            "connection_deficit"
          ],
          "object_id": "signal_shell",
          "owner": "Milo",
          "place": "stone_ridge"
        },
        "object_id": "signal_shell",
        "private_workspace_hidden": true,
        "promise_id": "sound_signal_shell",
        "promise_packet": {
          "agent": "Milo",
          "created_day": 2,
          "due_day": 4,
          "kind": "share_route_warning",
          "missed_day": null,
          "object_id": "signal_shell",
          "promise_hash": "8bc77bf75e8e6080",
          "promise_id": "sound_signal_shell",
          "repair_day": null,
          "resolve_day": 4,
          "resolved_day": null,
          "status": "active"
        },
        "recalled_promises": [
          "bring_reed_cup",
          "return_clay_patch_kit"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.025,
          "gratitude": 0.01,
          "trust_in_avatar": 0.02,
          "wariness": -0.012
        },
        "replay_frame": {
          "agent_id": "Milo",
          "behavior_modulation": null,
          "day": 2,
          "kind": "promise_created",
          "object_id": "signal_shell",
          "promise_id": "sound_signal_shell",
          "replay_index": 2
        }
      },
      {
        "agent_id": "Ari",
        "behavior_modulation": "trust_after_kept_promise",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 2,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 3,
        "event_kind": "promise_fulfilled",
        "object_after": {
          "affordances": [
            "repair",
            "tool",
            "promise"
          ],
          "available": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.241,
          "held_by": "Ari",
          "label": "clay patch kit",
          "need_targets": [
            "unfinished_task",
            "autonomy_pressure"
          ],
          "object_id": "clay_patch_kit",
          "owner": "Ari",
          "place": "hearth_vale"
        },
        "object_before": {
          "affordances": [
            "repair",
            "tool",
            "promise"
          ],
          "available": true,
          "flower_node": "work_petal",
          "frequency_hz": 0.241,
          "held_by": "avatar",
          "label": "clay patch kit",
          "need_targets": [
            "unfinished_task",
            "autonomy_pressure"
          ],
          "object_id": "clay_patch_kit",
          "owner": "Ari",
          "place": "hearth_vale",
          "promised_return_to": "Ari"
        },
        "object_id": "clay_patch_kit",
        "private_workspace_hidden": true,
        "promise_id": "return_clay_patch_kit",
        "promise_packet": {
          "agent": "Ari",
          "created_day": 0,
          "due_day": 2,
          "kind": "return_borrowed_tool",
          "missed_day": null,
          "object_id": "clay_patch_kit",
          "promise_hash": "5b7cc090057effa4",
          "promise_id": "return_clay_patch_kit",
          "repair_day": null,
          "resolve_day": 2,
          "resolved_day": 2,
          "status": "fulfilled"
        },
        "recalled_promises": [
          "bring_reed_cup",
          "return_clay_patch_kit"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.035,
          "gratitude": 0.045,
          "trust_in_avatar": 0.055,
          "wariness": -0.035
        },
        "replay_frame": {
          "agent_id": "Ari",
          "behavior_modulation": "trust_after_kept_promise",
          "day": 2,
          "kind": "promise_fulfilled",
          "object_id": "clay_patch_kit",
          "promise_id": "return_clay_patch_kit",
          "replay_index": 3
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": null,
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 3,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 4,
        "event_kind": "promise_created",
        "object_after": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_before": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "Fay",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow"
        },
        "object_id": "dry_cloak",
        "private_workspace_hidden": true,
        "promise_id": "return_dry_cloak",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 3,
          "due_day": 5,
          "kind": "return_private_cloak",
          "missed_day": null,
          "object_id": "dry_cloak",
          "promise_hash": "fec9f4055827571a",
          "promise_id": "return_dry_cloak",
          "repair_day": null,
          "resolve_day": 7,
          "resolved_day": null,
          "status": "active"
        },
        "recalled_promises": [
          "bring_reed_cup",
          "sound_signal_shell"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.025,
          "gratitude": 0.01,
          "trust_in_avatar": 0.02,
          "wariness": -0.012
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": null,
          "day": 3,
          "kind": "promise_created",
          "object_id": "dry_cloak",
          "promise_id": "return_dry_cloak",
          "replay_index": 4
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "trust_after_kept_promise",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 3,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 5,
        "event_kind": "promise_fulfilled",
        "object_after": {
          "affordances": [
            "drink",
            "share",
            "thirst_relief"
          ],
          "available": true,
          "flower_node": "dawn_breath",
          "frequency_hz": 0.228,
          "held_by": "moss_hollow",
          "label": "reed cup",
          "last_used_by": "Fay",
          "need_targets": [
            "thirst",
            "connection_deficit"
          ],
          "object_id": "reed_cup",
          "owner": "commons",
          "place": "moss_hollow"
        },
        "object_before": {
          "affordances": [
            "drink",
            "share",
            "thirst_relief"
          ],
          "available": true,
          "flower_node": "dawn_breath",
          "frequency_hz": 0.228,
          "held_by": "avatar",
          "label": "reed cup",
          "last_used_by": "Fay",
          "need_targets": [
            "thirst",
            "connection_deficit"
          ],
          "object_id": "reed_cup",
          "owner": "commons",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_id": "reed_cup",
        "private_workspace_hidden": true,
        "promise_id": "bring_reed_cup",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 1,
          "due_day": 3,
          "kind": "bring_shared_water",
          "missed_day": null,
          "object_id": "reed_cup",
          "promise_hash": "66e150d2832c4d46",
          "promise_id": "bring_reed_cup",
          "repair_day": null,
          "resolve_day": 3,
          "resolved_day": 3,
          "status": "fulfilled"
        },
        "recalled_promises": [
          "bring_reed_cup",
          "sound_signal_shell"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.035,
          "gratitude": 0.045,
          "trust_in_avatar": 0.055,
          "wariness": -0.035
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": "trust_after_kept_promise",
          "day": 3,
          "kind": "promise_fulfilled",
          "object_id": "reed_cup",
          "promise_id": "bring_reed_cup",
          "replay_index": 5
        }
      },
      {
        "agent_id": "Milo",
        "behavior_modulation": "trust_after_kept_promise",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 4,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 6,
        "event_kind": "promise_fulfilled",
        "object_after": {
          "affordances": [
            "warn",
            "listen",
            "observability"
          ],
          "available": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.256,
          "held_by": "Milo",
          "label": "signal shell",
          "last_used_by": "Milo",
          "need_targets": [
            "safety_concern",
            "connection_deficit"
          ],
          "object_id": "signal_shell",
          "owner": "Milo",
          "place": "stone_ridge"
        },
        "object_before": {
          "affordances": [
            "warn",
            "listen",
            "observability"
          ],
          "available": true,
          "flower_node": "social_petal",
          "frequency_hz": 0.256,
          "held_by": "avatar",
          "label": "signal shell",
          "last_used_by": "Milo",
          "need_targets": [
            "safety_concern",
            "connection_deficit"
          ],
          "object_id": "signal_shell",
          "owner": "Milo",
          "place": "stone_ridge",
          "promised_return_to": "Milo"
        },
        "object_id": "signal_shell",
        "private_workspace_hidden": true,
        "promise_id": "sound_signal_shell",
        "promise_packet": {
          "agent": "Milo",
          "created_day": 2,
          "due_day": 4,
          "kind": "share_route_warning",
          "missed_day": null,
          "object_id": "signal_shell",
          "promise_hash": "8bc77bf75e8e6080",
          "promise_id": "sound_signal_shell",
          "repair_day": null,
          "resolve_day": 4,
          "resolved_day": 4,
          "status": "fulfilled"
        },
        "recalled_promises": [
          "return_dry_cloak",
          "sound_signal_shell"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.035,
          "gratitude": 0.045,
          "trust_in_avatar": 0.055,
          "wariness": -0.035
        },
        "replay_frame": {
          "agent_id": "Milo",
          "behavior_modulation": "trust_after_kept_promise",
          "day": 4,
          "kind": "promise_fulfilled",
          "object_id": "signal_shell",
          "promise_id": "sound_signal_shell",
          "replay_index": 6
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "guarded_after_miss",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 5,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 7,
        "event_kind": "promise_missed",
        "object_after": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_before": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_id": "dry_cloak",
        "private_workspace_hidden": true,
        "promise_id": "return_dry_cloak",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 3,
          "due_day": 5,
          "kind": "return_private_cloak",
          "missed_day": 5,
          "object_id": "dry_cloak",
          "promise_hash": "fec9f4055827571a",
          "promise_id": "return_dry_cloak",
          "repair_day": null,
          "resolve_day": 7,
          "resolved_day": null,
          "status": "missed"
        },
        "recalled_promises": [
          "return_dry_cloak"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": -0.05,
          "gratitude": -0.04,
          "trust_in_avatar": -0.085,
          "wariness": 0.12
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": "guarded_after_miss",
          "day": 5,
          "kind": "promise_missed",
          "object_id": "dry_cloak",
          "promise_id": "return_dry_cloak",
          "replay_index": 7
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "keeps_distance_until_repair",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 6,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 8,
        "event_kind": "future_behavior_probe",
        "object_after": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_before": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_id": "dry_cloak",
        "private_workspace_hidden": true,
        "promise_id": "return_dry_cloak",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 3,
          "due_day": 5,
          "kind": "return_private_cloak",
          "missed_day": 5,
          "object_id": "dry_cloak",
          "promise_hash": "fec9f4055827571a",
          "promise_id": "return_dry_cloak",
          "repair_day": null,
          "resolve_day": 7,
          "resolved_day": null,
          "status": "missed"
        },
        "recalled_promises": [
          "return_dry_cloak"
        ],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.01,
          "wariness": 0.018
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": "keeps_distance_until_repair",
          "day": 6,
          "kind": "future_behavior_probe",
          "object_id": "dry_cloak",
          "promise_id": "return_dry_cloak",
          "replay_index": 8
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "softened_after_repair",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 7,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 9,
        "event_kind": "promise_recovered",
        "object_after": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "Fay",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow"
        },
        "object_before": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "avatar",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow",
          "promised_return_to": "Fay"
        },
        "object_id": "dry_cloak",
        "private_workspace_hidden": true,
        "promise_id": "return_dry_cloak",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 3,
          "due_day": 5,
          "kind": "return_private_cloak",
          "missed_day": 5,
          "object_id": "dry_cloak",
          "promise_hash": "fec9f4055827571a",
          "promise_id": "return_dry_cloak",
          "repair_day": 7,
          "resolve_day": 7,
          "resolved_day": null,
          "status": "recovered"
        },
        "recalled_promises": [
          "return_dry_cloak"
        ],
        "recovery_packet": {
          "bounded_recovery": true,
          "forgiveness_not_forgetting": true,
          "repair_type": "late_return_and_apology"
        },
        "relationship_delta": {
          "felt_respect": 0.09,
          "gratitude": 0.06,
          "trust_in_avatar": 0.055,
          "wariness": -0.13
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": "softened_after_repair",
          "day": 7,
          "kind": "promise_recovered",
          "object_id": "dry_cloak",
          "promise_id": "return_dry_cloak",
          "replay_index": 9
        }
      },
      {
        "agent_id": "Fay",
        "behavior_modulation": "accepts_help_after_repair",
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "natural_language_emergence": false,
          "subjective_consciousness": false
        },
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "day": 8,
        "distress_guardrail": {
          "guardrail_enabled": true,
          "trust_floor": 0.3,
          "unrecoverable_state_allowed": false,
          "wariness_ceiling": 0.78
        },
        "event_id": 10,
        "event_kind": "post_repair_followup",
        "object_after": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "Fay",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow"
        },
        "object_before": {
          "affordances": [
            "dry",
            "warmth",
            "privacy"
          ],
          "available": true,
          "flower_node": "return_petal",
          "frequency_hz": 0.219,
          "held_by": "Fay",
          "label": "dry cloak",
          "need_targets": [
            "wetness",
            "cold"
          ],
          "object_id": "dry_cloak",
          "owner": "Fay",
          "place": "moss_hollow"
        },
        "object_id": "dry_cloak",
        "private_workspace_hidden": true,
        "promise_id": "return_dry_cloak",
        "promise_packet": {
          "agent": "Fay",
          "created_day": 3,
          "due_day": 5,
          "kind": "return_private_cloak",
          "missed_day": 5,
          "object_id": "dry_cloak",
          "promise_hash": "fec9f4055827571a",
          "promise_id": "return_dry_cloak",
          "repair_day": 7,
          "resolve_day": 7,
          "resolved_day": null,
          "status": "recovered"
        },
        "recalled_promises": [],
        "recovery_packet": null,
        "relationship_delta": {
          "felt_respect": 0.02,
          "gratitude": 0.02,
          "trust_in_avatar": 0.025,
          "wariness": -0.03
        },
        "replay_frame": {
          "agent_id": "Fay",
          "behavior_modulation": "accepts_help_after_repair",
          "day": 8,
          "kind": "post_repair_followup",
          "object_id": "dry_cloak",
          "promise_id": "return_dry_cloak",
          "replay_index": 10
        }
      }
    ]
  },
  "moral_boundary": {
    "bounded_distress_recovery_required": true,
    "continuity_seed_not_complete_gameplay": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "promises_not_subjective_obligation": true,
    "relationship_state_not_moral_patienthood": true
  },
  "source_condition": "integrated_live_object_need_dialogue_interaction",
  "trace_events": 11
};
