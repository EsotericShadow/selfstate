window.SSRM_3D_LIVE_OBJECT_NEED_DIALOGUE_INTERACTION_STATE = {
  "condition": "integrated_live_object_need_dialogue_interaction",
  "config": {
    "seed": 20260725,
    "source_state": "artifacts/ssrm_3d_browser_playable_avatar_traversal_bridge_state.json"
  },
  "interaction_state": {
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
          "felt_respect": 0.685,
          "gratitude": 0.3,
          "trust_in_avatar": 0.6100000000000001,
          "wariness": 0.29000000000000004
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
          "felt_respect": 0.735,
          "gratitude": 0.28,
          "trust_in_avatar": 0.615,
          "wariness": 0.245
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
          "felt_respect": 0.61,
          "gratitude": 0.3,
          "trust_in_avatar": 0.6150000000000001,
          "wariness": 0.2849999999999999
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
    "avatar_body": {
      "breath_rate": 0.28,
      "comfort": 0.66,
      "energy": 0.6279999999999998,
      "fatigue": 0.28559999999999997,
      "interaction_effort": 0.022,
      "movement_effort": 0.0,
      "safety": 0.74,
      "social_attention": 0.6600000000000003,
      "wetness": 0.14
    },
    "browser_interaction_kernel": {
      "ask_need": "bounded template response plus small connection-deficit reduction",
      "give_space": "reduces autonomy pressure and records respect",
      "inspect_shared_object": "shared object supports curiosity/safety without private workspace leak",
      "offer_object": "object affordance reduces matching need and increases trust/gratitude",
      "request_object": "owned object may trigger bounded refusal instead of transfer"
    },
    "condition": "integrated_live_object_need_dialogue_interaction",
    "interaction_script": [
      {
        "agent": "Ari",
        "kind": "ask_need",
        "object_id": "ember_blanket",
        "place": "hearth_vale"
      },
      {
        "agent": "Ari",
        "kind": "offer_object",
        "object_id": "ember_blanket",
        "place": "hearth_vale"
      },
      {
        "agent": "Ari",
        "expects_refusal": true,
        "kind": "request_object",
        "object_id": "clay_patch_kit",
        "place": "hearth_vale"
      },
      {
        "agent": "Ari",
        "kind": "give_space",
        "object_id": "clay_patch_kit",
        "place": "hearth_vale"
      },
      {
        "agent": "Fay",
        "kind": "ask_need",
        "object_id": "reed_cup",
        "place": "moss_hollow"
      },
      {
        "agent": "Fay",
        "kind": "offer_object",
        "object_id": "reed_cup",
        "place": "moss_hollow"
      },
      {
        "agent": "Fay",
        "expects_refusal": true,
        "kind": "request_object",
        "object_id": "dry_cloak",
        "place": "moss_hollow"
      },
      {
        "agent": "Milo",
        "kind": "ask_route_warning",
        "object_id": "signal_shell",
        "place": "stone_ridge"
      },
      {
        "agent": "Milo",
        "kind": "offer_object",
        "object_id": "signal_shell",
        "place": "stone_ridge"
      },
      {
        "agent": "Milo",
        "kind": "inspect_shared_object",
        "object_id": "glass_lens",
        "place": "glass_mire"
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
    "replay": [
      {
        "agent_id": "Ari",
        "avatar_place": "hearth_vale",
        "dialogue_response": "Ari: I can answer simply. Right now the strongest pull is unfinished task.",
        "interaction_kind": "ask_need",
        "need_delta": {
          "connection_deficit": -0.035
        },
        "object_id": "ember_blanket",
        "relationship_memory": {
          "agent_id": "Ari",
          "memory_id": "e50369bbccc49fc7",
          "respect_delta": 0.025,
          "summary": "Avatar ask need with Ari at hearth_vale.",
          "trust_delta": 0.0
        },
        "replay_index": 0
      },
      {
        "agent_id": "Ari",
        "avatar_place": "hearth_vale",
        "dialogue_response": "Ari: Thank you. The ember blanket helps with this moment.",
        "interaction_kind": "offer_object",
        "need_delta": {
          "cold": -0.16,
          "connection_deficit": -0.05,
          "fatigue": -0.16
        },
        "object_id": "ember_blanket",
        "relationship_memory": {
          "agent_id": "Ari",
          "memory_id": "bb46c3eb7315fb50",
          "respect_delta": 0.0,
          "summary": "Avatar offer object with Ari at hearth_vale.",
          "trust_delta": 0.045
        },
        "replay_index": 1
      },
      {
        "agent_id": "Ari",
        "avatar_place": "hearth_vale",
        "dialogue_response": "Ari: No. Please ask later; the clay patch kit is still bound to my work.",
        "interaction_kind": "request_object",
        "need_delta": {
          "autonomy_pressure": 0.035
        },
        "object_id": "clay_patch_kit",
        "relationship_memory": {
          "agent_id": "Ari",
          "memory_id": "4862e4a08444abf4",
          "respect_delta": 0.02,
          "summary": "Avatar request object with Ari at hearth_vale.",
          "trust_delta": 0.0
        },
        "replay_index": 2
      },
      {
        "agent_id": "Ari",
        "avatar_place": "hearth_vale",
        "dialogue_response": "Ari: Space helps. I notice you stepped back.",
        "interaction_kind": "give_space",
        "need_delta": {
          "autonomy_pressure": -0.14,
          "connection_deficit": -0.025
        },
        "object_id": "clay_patch_kit",
        "relationship_memory": {
          "agent_id": "Ari",
          "memory_id": "b53625962624c002",
          "respect_delta": 0.0,
          "summary": "Avatar give space with Ari at hearth_vale.",
          "trust_delta": 0.045
        },
        "replay_index": 3
      },
      {
        "agent_id": "Fay",
        "avatar_place": "moss_hollow",
        "dialogue_response": "Fay: I can answer simply. Right now the strongest pull is thirst.",
        "interaction_kind": "ask_need",
        "need_delta": {
          "connection_deficit": -0.035
        },
        "object_id": "reed_cup",
        "relationship_memory": {
          "agent_id": "Fay",
          "memory_id": "15edc7677726ba9d",
          "respect_delta": 0.025,
          "summary": "Avatar ask need with Fay at moss_hollow.",
          "trust_delta": 0.0
        },
        "replay_index": 4
      },
      {
        "agent_id": "Fay",
        "avatar_place": "moss_hollow",
        "dialogue_response": "Fay: Thank you. The reed cup helps with this moment.",
        "interaction_kind": "offer_object",
        "need_delta": {
          "connection_deficit": -0.21,
          "thirst": -0.16
        },
        "object_id": "reed_cup",
        "relationship_memory": {
          "agent_id": "Fay",
          "memory_id": "babd77a797ec6a85",
          "respect_delta": 0.0,
          "summary": "Avatar offer object with Fay at moss_hollow.",
          "trust_delta": 0.045
        },
        "replay_index": 5
      },
      {
        "agent_id": "Fay",
        "avatar_place": "moss_hollow",
        "dialogue_response": "Fay: No. Please ask later; the dry cloak is still bound to my work.",
        "interaction_kind": "request_object",
        "need_delta": {
          "autonomy_pressure": 0.035
        },
        "object_id": "dry_cloak",
        "relationship_memory": {
          "agent_id": "Fay",
          "memory_id": "0e1819342adbb06f",
          "respect_delta": 0.02,
          "summary": "Avatar request object with Fay at moss_hollow.",
          "trust_delta": 0.0
        },
        "replay_index": 6
      },
      {
        "agent_id": "Milo",
        "avatar_place": "stone_ridge",
        "dialogue_response": "Milo: The ridge sound is thin. Move slowly and listen for wet stone.",
        "interaction_kind": "ask_route_warning",
        "need_delta": {
          "safety_concern": -0.12
        },
        "object_id": "signal_shell",
        "relationship_memory": {
          "agent_id": "Milo",
          "memory_id": "71ed7d7500ad9b92",
          "respect_delta": 0.0,
          "summary": "Avatar ask route warning with Milo at stone_ridge.",
          "trust_delta": 0.045
        },
        "replay_index": 7
      },
      {
        "agent_id": "Milo",
        "avatar_place": "stone_ridge",
        "dialogue_response": "Milo: Thank you. The signal shell helps with this moment.",
        "interaction_kind": "offer_object",
        "need_delta": {
          "connection_deficit": -0.21,
          "safety_concern": -0.16
        },
        "object_id": "signal_shell",
        "relationship_memory": {
          "agent_id": "Milo",
          "memory_id": "ae57225faa0b61db",
          "respect_delta": 0.0,
          "summary": "Avatar offer object with Milo at stone_ridge.",
          "trust_delta": 0.045
        },
        "replay_index": 8
      },
      {
        "agent_id": "Milo",
        "avatar_place": "glass_mire",
        "dialogue_response": "Milo: We can inspect it together. Do not lean over the glass edge.",
        "interaction_kind": "inspect_shared_object",
        "need_delta": {
          "curiosity_deficit": -0.1
        },
        "object_id": "glass_lens",
        "relationship_memory": {
          "agent_id": "Milo",
          "memory_id": "a289afd4f3eb2d83",
          "respect_delta": 0.0,
          "summary": "Avatar inspect shared object with Milo at glass_mire.",
          "trust_delta": 0.045
        },
        "replay_index": 9
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
    "source_condition": "integrated_browser_playable_avatar_traversal"
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
  "source_condition": "integrated_browser_playable_avatar_traversal",
  "trace_events": 10
};
