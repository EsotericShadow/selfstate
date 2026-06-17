window.SSRM_3D_AGENT_ROUTINE_HOME_WORK_UNSCRIPTED_OBJECT_USE_TRACE = [
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "e8d1fce9764c673e"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.535,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.5188,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.304,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.27036,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.6442,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.6442,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 0,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.24999999999999997,
      "curiosity_deficit": 0.22,
      "fatigue": 0.28,
      "rest_debt": 0.34,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.32,
      "unfinished_task": 0.69
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "hearth_vale",
      "routine_uses": 0
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 1
    },
    "phase": "dawn_home",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.16,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "clay_patch_kit",
      "phase": "dawn_home",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.16,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 0,
      "tick": 0
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b4996504c329d912"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.535,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.5668,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3625,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.24978,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.6136,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.6136,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 1,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.175,
      "curiosity_deficit": 0.35,
      "fatigue": 0.52,
      "rest_debt": 0.34,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.44999999999999996,
      "unfinished_task": 0.28
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "moss_hollow",
      "routine_uses": 0
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 1
    },
    "phase": "dawn_home",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.16,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "dry_cloak",
      "phase": "dawn_home",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.16,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 1,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "d691bf680ca29ec4"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.535,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.5368,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3445,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.28256,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.5848,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.5848,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 2,
    "flower_node": "social_petal",
    "frequency_hz": 0.256,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.27999999999999997,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.37,
      "rest_debt": 0.34,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.41,
      "unfinished_task": 0.34
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 0
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 1
    },
    "phase": "dawn_home",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.16,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "signal_shell",
      "phase": "dawn_home",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.16,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 2,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "2ffcf3de0478ea88"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.3914,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3094,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.27036,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.9063,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.9063,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 3,
    "flower_node": "work_petal",
    "frequency_hz": 0.241,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.24999999999999997,
      "curiosity_deficit": 0.22,
      "fatigue": 0.32200000000000006,
      "rest_debt": 0.35000000000000003,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.332,
      "unfinished_task": 0.6349999999999999
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 1
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 2
    },
    "phase": "morning_work",
    "place_after": "clay_basin",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "clay_patch_kit",
      "phase": "morning_work",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 3,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "a2f5f3521ad540ba"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.255,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.4394,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3679,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.24978,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.89316,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.89316,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 4,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.175,
      "curiosity_deficit": 0.35,
      "fatigue": 0.562,
      "rest_debt": 0.35000000000000003,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.46199999999999997,
      "unfinished_task": 0.22500000000000003
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 1
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 2
    },
    "phase": "morning_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "dry_cloak",
      "phase": "morning_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 4,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "5deb1c06d30896e0"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4094,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3499,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.28256,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.8568,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.8568,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 5,
    "flower_node": "social_petal",
    "frequency_hz": 0.256,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.27999999999999997,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.41200000000000003,
      "rest_debt": 0.35000000000000003,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.422,
      "unfinished_task": 0.28500000000000003
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 1
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 2
    },
    "phase": "morning_work",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "signal_shell",
      "phase": "morning_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 5,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b46f77b8ae1d90b6"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.404,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.6148,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.27036,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.5284,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.6148,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 6,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.24999999999999997,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3640000000000001,
      "rest_debt": 0.36000000000000004,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.34400000000000003,
      "unfinished_task": 0.5799999999999998
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "place": "moss_hollow",
      "routine_uses": 0
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 1
    },
    "phase": "midday_care",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 6,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "54121b7076bdd25c"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.255,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.452,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.6733,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.24978,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.53272,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.6733,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 7,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.175,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6040000000000001,
      "rest_debt": 0.36000000000000004,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.474,
      "unfinished_task": 0.17000000000000004
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 1
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 2
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 7,
      "tick": 2
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "e6f483b394392316"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.422,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.6553,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.28256,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.4888,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.6553,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 8,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.27999999999999997,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.45400000000000007,
      "rest_debt": 0.36000000000000004,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.434,
      "unfinished_task": 0.23000000000000004
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 2
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 3
    },
    "phase": "midday_care",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.32,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.32,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 8,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "6d388071d74516fb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4106,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2392,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.26086,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.8084,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.8084,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 9,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.22499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3760000000000001,
      "rest_debt": 0.37000000000000005,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.17600000000000005,
      "unfinished_task": 0.5799999999999998
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 2
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 3
    },
    "phase": "afternoon_work",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "clay_patch_kit",
      "phase": "afternoon_work",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 9,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "3d6c844644742eef"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.255,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.4586,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2977,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.24028,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.81488,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.81488,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 10,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.15,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6160000000000001,
      "rest_debt": 0.37000000000000005,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.306,
      "unfinished_task": 0.17000000000000004
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 2
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 3
    },
    "phase": "afternoon_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "dry_cloak",
      "phase": "afternoon_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 10,
      "tick": 3
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "50f8eed5444e47cc"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4286,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2797,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.27306,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.7688,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.7688,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 11,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.25499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.4660000000000001,
      "rest_debt": 0.37000000000000005,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.266,
      "unfinished_task": 0.23000000000000004
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 2
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 3
    },
    "phase": "afternoon_work",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "signal_shell",
      "phase": "afternoon_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 11,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "1a1686926b8a298a"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4232,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2446,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.56086,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.4705,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.56086,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 12,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.22499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.41800000000000015,
      "rest_debt": 0.38000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.18800000000000006,
      "unfinished_task": 0.5249999999999998
    },
    "need_delta": {
      "connection_deficit": -0.12,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 3
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 4
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 12,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "bc6f44ff6d10e73a"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.255,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.4712,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3031,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.54028,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.49444,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.54028,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 13,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.15,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6580000000000001,
      "rest_debt": 0.38000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.318,
      "unfinished_task": 0.11500000000000005
    },
    "need_delta": {
      "connection_deficit": -0.12,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 4
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 5
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 13,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "7303ea403bc259e2"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4412,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2851,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.57306,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.4408,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.57306,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 14,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.25499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.5080000000000001,
      "rest_debt": 0.38000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.278,
      "unfinished_task": 0.17500000000000004
    },
    "need_delta": {
      "connection_deficit": -0.12,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 3
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 4
    },
    "phase": "dusk_social",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "signal_shell",
      "phase": "dusk_social",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 14,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "866dd9d071496686"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.7898,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.25,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.21622,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.4705,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.7898,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 15,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.10499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.43000000000000016,
      "rest_debt": 0.39000000000000007,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.20000000000000007,
      "unfinished_task": 0.5249999999999998
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 0
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 1
    },
    "phase": "night_rest",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 0,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 15,
      "tick": 5
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "c7d23d9f812cad54"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.255,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.8378,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3085,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.19564,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.4966,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.8378,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 16,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.03,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6700000000000002,
      "rest_debt": 0.39000000000000007,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.33,
      "unfinished_task": 0.11500000000000005
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 3
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 4
    },
    "phase": "night_rest",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 0,
      "object_id": "dry_cloak",
      "phase": "night_rest",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 16,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "26085802faef0b23"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.255,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.8078,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2905,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.22842,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.4408,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.8078,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 0,
    "event_id": 17,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.13499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.5200000000000001,
      "rest_debt": 0.39000000000000007,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.29000000000000004,
      "unfinished_task": 0.17500000000000004
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 1
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 2
    },
    "phase": "night_rest",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 0,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 17,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "6e3fea2f2f03b60f"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.535,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4538,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2554,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.21622,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.4705,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.535,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 18,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.10499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.27000000000000013,
      "rest_debt": 0.19000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.31,
      "thirst": 0.21200000000000008,
      "unfinished_task": 0.5249999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 2
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 3
    },
    "phase": "dawn_home",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 18,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "77b3c7faacd41d84"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.535,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.5018,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3139,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.19564,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.4678,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.535,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 19,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.03,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5100000000000001,
      "rest_debt": 0.19000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.27,
      "thirst": 0.342,
      "unfinished_task": 0.11500000000000005
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 4
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 5
    },
    "phase": "dawn_home",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "dry_cloak",
      "phase": "dawn_home",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 19,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "912d285acf3a1cd9"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.535,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.4718,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2959,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.22842,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.4408,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.535,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 20,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.13499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.3600000000000001,
      "rest_debt": 0.19000000000000006,
      "routine_boredom": 0.22,
      "safety_concern": 0.36,
      "thirst": 0.30200000000000005,
      "unfinished_task": 0.17500000000000004
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 3
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 4
    },
    "phase": "dawn_home",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.48,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.48,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 20,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "e9c6936219a4b8de"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.32796,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2608,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.21622,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.7905,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.7905,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 21,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.10499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.28200000000000014,
      "rest_debt": 0.21800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.2240000000000001,
      "unfinished_task": 0.5249999999999998
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 3
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 4
    },
    "phase": "morning_work",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "clay_patch_kit",
      "phase": "morning_work",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 21,
      "tick": 1
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "9a75994c253515b1"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2375,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.37596,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3193,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.19564,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.78996,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.78996,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 22,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.03,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5220000000000001,
      "rest_debt": 0.21800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.35400000000000004,
      "unfinished_task": 0.11500000000000005
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 5
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 6
    },
    "phase": "morning_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "dry_cloak",
      "phase": "morning_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 22,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "29c60ae2f01898e4"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.34596,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.3013,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.22842,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.7608,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.7608,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 23,
    "flower_node": "social_petal",
    "frequency_hz": 0.256,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.13499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.3720000000000001,
      "rest_debt": 0.21800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.31400000000000006,
      "unfinished_task": 0.17500000000000004
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 4
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 5
    },
    "phase": "morning_work",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "signal_shell",
      "phase": "morning_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 23,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "88084131180657f9"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.34056,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5662,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.21622,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.4126,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5662,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 24,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.10499999999999998,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3240000000000002,
      "rest_debt": 0.22800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.2360000000000001,
      "unfinished_task": 0.4699999999999998
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 5
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 6
    },
    "phase": "midday_care",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 24,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "ac8d437dbe11c7fb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2375,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.38856,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.6247,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.19564,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.42952,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.6247,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 25,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.03,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5640000000000002,
      "rest_debt": 0.22800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.36600000000000005,
      "unfinished_task": 0.060000000000000046
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 6
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 7
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 25,
      "tick": 2
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "1be3b7911a9875fc"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.35856,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.6067,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.22842,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3928,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.6067,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 26,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.13499999999999995,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.41400000000000015,
      "rest_debt": 0.22800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.32600000000000007,
      "unfinished_task": 0.12000000000000005
    },
    "need_delta": {
      "connection_deficit": -0.025,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 7
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 8
    },
    "phase": "midday_care",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.64,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.64,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 26,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "69e65ea640ea6384"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.34716,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1906,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.20672,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.6926,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.6926,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 27,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.07999999999999999,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3360000000000002,
      "rest_debt": 0.23800000000000007,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.0680000000000001,
      "unfinished_task": 0.4699999999999998
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 4
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 5
    },
    "phase": "afternoon_work",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "clay_patch_kit",
      "phase": "afternoon_work",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 27,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "38f13ab7eb10c5eb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2375,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.39516,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2491,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18614,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.71168,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.71168,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 28,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0049999999999999975,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5760000000000002,
      "rest_debt": 0.23800000000000007,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.19800000000000006,
      "unfinished_task": 0.060000000000000046
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 6
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 7
    },
    "phase": "afternoon_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "dry_cloak",
      "phase": "afternoon_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 28,
      "tick": 3
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b853a910170ceced"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.36516,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2311,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.21892,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.6728,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.6728,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 29,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.10999999999999996,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.42600000000000016,
      "rest_debt": 0.23800000000000007,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.15800000000000008,
      "unfinished_task": 0.12000000000000005
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 5
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 6
    },
    "phase": "afternoon_work",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "signal_shell",
      "phase": "afternoon_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 29,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "4a469a10a343aa6e"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.35976,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.196,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.50672,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.3547,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.50672,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 30,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.07999999999999999,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3780000000000002,
      "rest_debt": 0.24800000000000008,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.0800000000000001,
      "unfinished_task": 0.4149999999999998
    },
    "need_delta": {
      "connection_deficit": -0.08,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 8
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 9
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 30,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "a65ee6413cbd4a4a"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2375,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.40776,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2545,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.48614,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.39124,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.48614,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 31,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0049999999999999975,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6180000000000002,
      "rest_debt": 0.24800000000000008,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.21000000000000008,
      "unfinished_task": 0.005000000000000046
    },
    "need_delta": {
      "connection_deficit": -0.005,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 9
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 10
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 31,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "145927189c9f2c6f"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.37776,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2365,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.51892,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3448,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.51892,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 32,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.10999999999999996,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.4680000000000002,
      "rest_debt": 0.24800000000000008,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.1700000000000001,
      "unfinished_task": 0.06500000000000006
    },
    "need_delta": {
      "connection_deficit": -0.11,
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 6
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 7
    },
    "phase": "dusk_social",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "signal_shell",
      "phase": "dusk_social",
      "place_after": "clay_basin",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 32,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "7c63e150b658af2e"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.72636,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2014,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.3547,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.72636,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 33,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.39000000000000024,
      "rest_debt": 0.25800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.0920000000000001,
      "unfinished_task": 0.4149999999999998
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 4
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 5
    },
    "phase": "night_rest",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 1,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 33,
      "tick": 5
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "eb624ba9e5d27fc4"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2375,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.77436,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2599,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.3934,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.77436,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 34,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.6300000000000002,
      "rest_debt": 0.25800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.2220000000000001,
      "unfinished_task": 0.005000000000000046
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 7
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 8
    },
    "phase": "night_rest",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 1,
      "object_id": "dry_cloak",
      "phase": "night_rest",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 34,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "888be98155de0809"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2375,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.74436,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2419,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3448,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.74436,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 1,
    "event_id": 35,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.4800000000000002,
      "rest_debt": 0.25800000000000006,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.1820000000000001,
      "unfinished_task": 0.06500000000000006
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.2,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 5
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 6
    },
    "phase": "night_rest",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 1,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 35,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b9ed46278610de88"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.5175,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.39036,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2068,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.3547,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.5175,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 36,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.23000000000000023,
      "rest_debt": 0.05800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.31,
      "thirst": 0.10400000000000009,
      "unfinished_task": 0.4149999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 6
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 7
    },
    "phase": "dawn_home",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "hearth_vale",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 36,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "fc3ec00f73b6874b"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.5175,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.43836,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2653,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.3646,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.5175,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 37,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.4700000000000002,
      "rest_debt": 0.05800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.27,
      "thirst": 0.2340000000000001,
      "unfinished_task": 0.005000000000000046
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 8
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 9
    },
    "phase": "dawn_home",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "dry_cloak",
      "phase": "dawn_home",
      "place_after": "moss_hollow",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 37,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "fdb5013c8a6583a3"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.5175,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.40836,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2473,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3448,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.5175,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 38,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.3200000000000002,
      "rest_debt": 0.05800000000000005,
      "routine_boredom": 0.15,
      "safety_concern": 0.36,
      "thirst": 0.19400000000000012,
      "unfinished_task": 0.06500000000000006
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 7
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 8
    },
    "phase": "dawn_home",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": false,
      "progress": 0.8,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "stone_ridge",
      "project": {
        "complete": false,
        "progress": 0.8,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 38,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "f48fc4e1078ba9ac"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.26452,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2122,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "unfinished_task",
        "object_id": "clay_patch_kit",
        "score": 0.6747,
        "target_place": "clay_basin"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "unfinished_task",
      "score": 0.6747,
      "selection_policy": "need_scored",
      "target_place": "clay_basin"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 39,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.24200000000000024,
      "rest_debt": 0.08600000000000005,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.31,
      "thirst": 0.11600000000000009,
      "unfinished_task": 0.4149999999999998
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 5
    },
    "object_used": {
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
      "last_used_by": "Ari",
      "need_targets": [
        "unfinished_task",
        "autonomy_pressure"
      ],
      "object_id": "clay_patch_kit",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 6
    },
    "phase": "morning_work",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "clay_patch_kit",
      "phase": "morning_work",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 39,
      "tick": 1
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "f8349917dc3226bd"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.22,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.31252,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2707,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      },
      {
        "action": "work_project",
        "need_key": "fatigue",
        "object_id": "dry_cloak",
        "score": 0.68676,
        "target_place": "moss_hollow"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "fatigue",
      "score": 0.68676,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 40,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.4820000000000002,
      "rest_debt": 0.08600000000000005,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.2460000000000001,
      "unfinished_task": 0.005000000000000046
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.005
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 9
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 10
    },
    "phase": "morning_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "dry_cloak",
      "phase": "morning_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 40,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "e6ea6693a2f20eae"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.28252,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2527,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      },
      {
        "action": "work_project",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.6648,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "work_project",
      "need_key": "safety_concern",
      "score": 0.6648,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 41,
    "flower_node": "social_petal",
    "frequency_hz": 0.256,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.3320000000000002,
      "rest_debt": 0.08600000000000005,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.36,
      "thirst": 0.20600000000000013,
      "unfinished_task": 0.06500000000000006
    },
    "need_delta": {
      "fatigue": 0.042,
      "rest_debt": 0.01,
      "thirst": 0.012,
      "unfinished_task": -0.055
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
      "place": "stone_ridge",
      "routine_uses": 7
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 8
    },
    "phase": "morning_work",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "work_project",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "signal_shell",
      "phase": "morning_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 41,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "547c2ec344586d34"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.27712,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5176,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2378,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5176,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 42,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.28400000000000025,
      "rest_debt": 0.09600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.31,
      "thirst": 0.12800000000000009,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.116
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 10
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 11
    },
    "phase": "midday_care",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 42,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "96c03d27be238ac7"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.22,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.32512,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5761,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5761,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 43,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5240000000000002,
      "rest_debt": 0.09600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.2580000000000001,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 11
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 12
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 43,
      "tick": 2
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "f10946d3c234c685"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.29512,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5581,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2568,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5581,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 44,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.3740000000000002,
      "rest_debt": 0.09600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.36,
      "thirst": 0.21800000000000014,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.168
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 12
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 13
    },
    "phase": "midday_care",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 44,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "51de1e01e9c8ac25"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.28372,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3378,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.3378,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 45,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.29600000000000026,
      "rest_debt": 0.10600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.31,
      "thirst": 0.012,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "routine_boredom": -0.045,
      "safety_concern": -0.1,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "glass_mire",
      "routine_uses": 0
    },
    "object_used": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 1
    },
    "phase": "afternoon_work",
    "place_after": "clay_basin",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "glass_lens",
      "phase": "afternoon_work",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 45,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "fa82b87c33d38194"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.22,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.33172,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2005,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.33172,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 46,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.5360000000000003,
      "rest_debt": 0.10600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.09000000000000012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.106,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 10
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 11
    },
    "phase": "afternoon_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "dry_cloak",
      "phase": "afternoon_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 46,
      "tick": 3
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "3702564d8fc76d4d"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.22,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.30172,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1825,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3568,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.3568,
      "selection_policy": "need_scored",
      "target_place": "glass_mire"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 47,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.38600000000000023,
      "rest_debt": 0.10600000000000004,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.36,
      "thirst": 0.05000000000000014,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "routine_boredom": -0.045,
      "safety_concern": -0.1,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 8
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 9
    },
    "phase": "afternoon_work",
    "place_after": "reed_wetland",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "signal_shell",
      "phase": "afternoon_work",
      "place_after": "reed_wetland",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 47,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "8f48b3572714c588"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.20875,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.29032,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.47728,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.47728,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 48,
    "flower_node": "root_rest",
    "frequency_hz": 0.238286,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3080000000000003,
      "rest_debt": 0.11600000000000003,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.21,
      "thirst": 0.024,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 13
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 14
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 48,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "root_rest",
      "frequency_hz": 0.238286,
      "from": "clay_basin",
      "hazard": 0.198327,
      "kind": "work_path",
      "route_cost": 0.624197,
      "route_hash": "b96570a5f8f2c276",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b3baddfa27312a5d"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.22,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.2552,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2059,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.4852,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.4852,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 49,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.3760000000000002,
      "rest_debt": 0.0,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.10200000000000012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 14
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 15
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 49,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "530ed52de6384a03"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.20875,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.30832,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1879,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.47808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.47808,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 50,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.39800000000000024,
      "rest_debt": 0.11600000000000003,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.26,
      "thirst": 0.06200000000000014,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 9
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 10
    },
    "phase": "dusk_social",
    "place_after": "clay_basin",
    "place_before": "reed_wetland",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "signal_shell",
      "phase": "dusk_social",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 50,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.286356,
      "flower_node": "social_petal",
      "frequency_hz": 0.2618,
      "from": "reed_wetland",
      "hazard": 0.275466,
      "kind": "water_clay_path",
      "route_cost": 0.677626,
      "route_hash": "afafa45735bc7c2f",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "1603b8330c9cfea1"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.20875,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.65692,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.65692,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 51,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.3200000000000003,
      "rest_debt": 0.12600000000000003,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.21,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.126,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 8
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 9
    },
    "phase": "night_rest",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 2,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 51,
      "tick": 5
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b12fdd2156762f58"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.22,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.6218,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2113,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.6218,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 52,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.38800000000000023,
      "rest_debt": 0.01,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.11400000000000012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.01,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 11
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 12
    },
    "phase": "night_rest",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 2,
      "object_id": "dry_cloak",
      "phase": "night_rest",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 52,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "bd9b67fa8a453cda"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.20875,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.67492,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1933,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.67492,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 2,
    "event_id": 53,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.41000000000000025,
      "rest_debt": 0.12600000000000003,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.26,
      "thirst": 0.07400000000000014,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.126,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 9
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 10
    },
    "phase": "night_rest",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 2,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 53,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "04f13bea30bab913"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.48875,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.352,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1816,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.48875,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 54,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.16000000000000028,
      "rest_debt": 0.0,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.21,
      "thirst": 0.048,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.035,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 10
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 11
    },
    "phase": "dawn_home",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 54,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "66240ccc3ca4ea73"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.5,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.3656,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2167,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.5,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 55,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.22800000000000023,
      "rest_debt": 0.0,
      "routine_boredom": 0.07999999999999999,
      "safety_concern": 0.27,
      "thirst": 0.1260000000000001,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.07,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 12
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 13
    },
    "phase": "dawn_home",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "dry_cloak",
      "phase": "dawn_home",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 55,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "bc9b670a81f14ba3"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.48875,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.37,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1987,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.48875,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 56,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.2500000000000002,
      "rest_debt": 0.0,
      "routine_boredom": 0.03499999999999999,
      "safety_concern": 0.26,
      "thirst": 0.08600000000000013,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "routine_boredom": -0.035,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 11
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 12
    },
    "phase": "dawn_home",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 56,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "5ef4dfc205305eb2"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.22616,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.187,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.22616,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 57,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.1720000000000003,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.0,
      "safety_concern": 0.21,
      "thirst": 0.06,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.028,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 12
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 13
    },
    "phase": "morning_work",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "morning_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 57,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "1f79440a1bfbeeb1"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2025,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.23976,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2221,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.23976,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 58,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.24000000000000024,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.009999999999999981,
      "safety_concern": 0.27,
      "thirst": 0.13800000000000012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.028,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 13
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 14
    },
    "phase": "morning_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "dry_cloak",
      "phase": "morning_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 58,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b3048eea87fdbba0"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.24416,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.2041,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.24416,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 59,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.26200000000000023,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.0,
      "safety_concern": 0.26,
      "thirst": 0.09800000000000013,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": -0.16,
      "rest_debt": -0.028,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 13
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 14
    },
    "phase": "morning_work",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "morning_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 59,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "e407e0689f31eaeb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.1824,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.4924,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.4924,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 60,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.012000000000000288,
      "rest_debt": 0.0,
      "routine_boredom": 0.0,
      "safety_concern": 0.21,
      "thirst": 0.072,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.06
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 15
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 16
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 60,
      "tick": 2
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "0f6977a83e160af4"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2025,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.196,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5275,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5275,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 61,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.08000000000000024,
      "rest_debt": 0.0,
      "routine_boredom": 0.009999999999999981,
      "safety_concern": 0.27,
      "thirst": 0.15000000000000013,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.138
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 16
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 17
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 61,
      "tick": 2
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "bd570ec654b34aea"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.2004,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.5095,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.5095,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 62,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.10200000000000023,
      "rest_debt": 0.0,
      "routine_boredom": 0.0,
      "safety_concern": 0.26,
      "thirst": 0.11000000000000013,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.098
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 17
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 18
    },
    "phase": "midday_care",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 62,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "f56964d4514998b0"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.189,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.17824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2998,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.2998,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 63,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.02400000000000029,
      "rest_debt": 0.01,
      "routine_boredom": 0.0,
      "safety_concern": 0.21,
      "thirst": 0.012,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 1
    },
    "object_used": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 2
    },
    "phase": "afternoon_work",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "glass_lens",
      "phase": "afternoon_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 63,
      "tick": 3
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "22b21d6332080277"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2025,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.2026,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.3226,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.3226,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 64,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.09200000000000023,
      "rest_debt": 0.01,
      "routine_boredom": 0.009999999999999981,
      "safety_concern": 0.27,
      "thirst": 0.012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "routine_boredom": -0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 2
    },
    "object_used": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Fay",
      "label": "glass lens",
      "last_used_by": "Fay",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 3
    },
    "phase": "afternoon_work",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "glass_lens",
      "phase": "afternoon_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 64,
      "tick": 3
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "ff432e666a3c9599"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.207,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.17904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.3188,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.3188,
      "selection_policy": "need_scored",
      "target_place": "glass_mire"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 65,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.11400000000000023,
      "rest_debt": 0.01,
      "routine_boredom": 0.0,
      "safety_concern": 0.26,
      "thirst": 0.012,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 10
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 11
    },
    "phase": "afternoon_work",
    "place_after": "reed_wetland",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "signal_shell",
      "phase": "afternoon_work",
      "place_after": "reed_wetland",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 65,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "615549721338e108"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.1956,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.47824,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.47824,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 66,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.03600000000000029,
      "rest_debt": 0.02,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.024,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 18
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 19
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 66,
      "tick": 4
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "c73fd23ab48d9a31"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.2092,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.48616,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.48616,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 67,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.10400000000000023,
      "rest_debt": 0.02,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.024,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 19
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 20
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 67,
      "tick": 4
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "5a0d766e14eb9f2c"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.2136,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.47904,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.47904,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 68,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.12600000000000022,
      "rest_debt": 0.02,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.024,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 11
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 12
    },
    "phase": "dusk_social",
    "place_after": "clay_basin",
    "place_before": "reed_wetland",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "signal_shell",
      "phase": "dusk_social",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 68,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.286356,
      "flower_node": "social_petal",
      "frequency_hz": 0.2618,
      "from": "reed_wetland",
      "hazard": 0.275466,
      "kind": "water_clay_path",
      "route_cost": 0.677626,
      "route_hash": "afafa45735bc7c2f",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "2a837077c12c6bec"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.5622,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.5622,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 69,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.04800000000000029,
      "rest_debt": 0.03,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": -0.048,
      "rest_debt": -0.03,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 14
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 15
    },
    "phase": "night_rest",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 69,
      "tick": 5
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "75af85b1ec05fdd2"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.5758,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.5758,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 70,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.11600000000000023,
      "rest_debt": 0.03,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": -0.116,
      "rest_debt": -0.03,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 14
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 15
    },
    "phase": "night_rest",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 3,
      "object_id": "dry_cloak",
      "phase": "night_rest",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 70,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "efcc844f8e820ce0"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.5802,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.5802,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 3,
    "event_id": 71,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.13800000000000023,
      "rest_debt": 0.03,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": -0.138,
      "rest_debt": -0.03,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 15
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 16
    },
    "phase": "night_rest",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 3,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 71,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "c7087ff29a4b2226"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.48,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.32,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1816,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.48,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 72,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.0,
      "rest_debt": 0.0,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.048,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 16
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 17
    },
    "phase": "dawn_home",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 72,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "b8af650036402688"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.48,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.32,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1816,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.48,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 73,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.0,
      "rest_debt": 0.0,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.048,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 15
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 16
    },
    "phase": "dawn_home",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "dry_cloak",
      "phase": "dawn_home",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 73,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "6b62e01592da30b6"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.48,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.32,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1816,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.48,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 74,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.0,
      "rest_debt": 0.0,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.048,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 17
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 18
    },
    "phase": "dawn_home",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "dawn_home",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 74,
      "tick": 0
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 0
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "0d4c8b653ef2b67c"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.19416,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.187,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.2,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 75,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.012,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.06,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 18
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 19
    },
    "phase": "morning_work",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "morning_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 75,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "53202f697da06f3d"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.19416,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.187,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.2,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 76,
    "flower_node": "return_petal",
    "frequency_hz": 0.219,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.012,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.06,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 16
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 17
    },
    "phase": "morning_work",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "dry_cloak",
      "phase": "morning_work",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 76,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "7ddea08c72e07eac"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.19416,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.187,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "home_tend",
      "need_key": "routine_boredom",
      "score": 0.2,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 77,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "stone_ridge",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.012,
      "rest_debt": 0.027999999999999997,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.06,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.028,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 19
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 20
    },
    "phase": "morning_work",
    "place_after": "stone_ridge",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "home_tend",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "morning_work",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 77,
      "tick": 1
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 1
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "5e6862d82635870e"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.20832,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.4924,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.4924,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 78,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.024,
      "rest_debt": 0.056,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.072,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.06
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 20
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 21
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 78,
      "tick": 2
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "fbeceb515de2f66d"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.20832,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.4924,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.4924,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 79,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.024,
      "rest_debt": 0.056,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.072,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.06
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 21
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 22
    },
    "phase": "midday_care",
    "place_after": "moss_hollow",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 79,
      "tick": 2
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "ccb2d94391a745bb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.20832,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.4924,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "care_drink",
      "need_key": "thirst",
      "score": 0.4924,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 80,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.024,
      "rest_debt": 0.056,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.072,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": -0.06
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
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 22
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 23
    },
    "phase": "midday_care",
    "place_after": "clay_basin",
    "place_before": "stone_ridge",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "care_drink",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "reed_cup",
      "phase": "midday_care",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 80,
      "tick": 2
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.360555,
      "flower_node": "explore_petal",
      "frequency_hz": 0.264425,
      "from": "stone_ridge",
      "hazard": 0.238239,
      "kind": "ridge_work_path",
      "route_cost": 0.693658,
      "route_hash": "13ad5c02ec2a90f6",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 2
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "219f42eed5ba5db8"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.21492,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.1792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2618,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.2618,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 81,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "hearth_vale",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.036000000000000004,
      "rest_debt": 0.066,
      "routine_boredom": 0.0,
      "safety_concern": 0.10999999999999999,
      "thirst": 0.012,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Fay",
      "label": "glass lens",
      "last_used_by": "Fay",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 3
    },
    "object_used": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 4
    },
    "phase": "afternoon_work",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "glass_lens",
      "phase": "afternoon_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 81,
      "tick": 3
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "98062404a7bc9c28"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.21492,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.2846,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.2846,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 82,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.036000000000000004,
      "rest_debt": 0.066,
      "routine_boredom": 0.0,
      "safety_concern": 0.17,
      "thirst": 0.012,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Ari",
      "label": "glass lens",
      "last_used_by": "Ari",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 4
    },
    "object_used": {
      "affordances": [
        "inspect",
        "curiosity",
        "hazard_read"
      ],
      "available": true,
      "flower_node": "explore_petal",
      "frequency_hz": 0.267,
      "held_by": "Fay",
      "label": "glass lens",
      "last_used_by": "Fay",
      "need_targets": [
        "curiosity_deficit",
        "safety_concern"
      ],
      "object_id": "glass_lens",
      "owner": "commons",
      "place": "glass_mire",
      "routine_uses": 5
    },
    "phase": "afternoon_work",
    "place_after": "hearth_vale",
    "place_before": "moss_hollow",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "glass_lens",
      "phase": "afternoon_work",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 82,
      "tick": 3
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.32311,
      "flower_node": "return_petal",
      "frequency_hz": 0.256115,
      "from": "moss_hollow",
      "hazard": 0.201261,
      "kind": "shelter_path",
      "route_cost": 0.600138,
      "route_hash": "8461c58b00f85c14",
      "to": "hearth_vale"
    },
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "6b52d8aee28bd3df"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.21492,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1654,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.2808,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "explore_safety",
      "need_key": "safety_concern",
      "score": 0.2808,
      "selection_policy": "need_scored",
      "target_place": "glass_mire"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 83,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.036000000000000004,
      "rest_debt": 0.066,
      "routine_boredom": 0.0,
      "safety_concern": 0.16,
      "thirst": 0.012,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "safety_concern": -0.1,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 12
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 13
    },
    "phase": "afternoon_work",
    "place_after": "reed_wetland",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "explore_safety",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "signal_shell",
      "phase": "afternoon_work",
      "place_after": "reed_wetland",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 83,
      "tick": 3
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 3
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "a11b345bab7b1dd2"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.22152,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.4792,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1238,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.4792,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 84,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.048,
      "rest_debt": 0.076,
      "routine_boredom": 0.0,
      "safety_concern": 0.009999999999999981,
      "thirst": 0.024,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Milo",
      "label": "reed cup",
      "last_used_by": "Milo",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 23
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 24
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 84,
      "tick": 4
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "3777f32147479567"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.22152,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.48712,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1466,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.48712,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 85,
    "flower_node": "dawn_breath",
    "frequency_hz": 0.228,
    "home_place": "moss_hollow",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.048,
      "rest_debt": 0.076,
      "routine_boredom": 0.0,
      "safety_concern": 0.07,
      "thirst": 0.024,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "held_by": "Ari",
      "label": "reed cup",
      "last_used_by": "Ari",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 24
    },
    "object_used": {
      "affordances": [
        "drink",
        "share",
        "thirst_relief"
      ],
      "available": true,
      "flower_node": "dawn_breath",
      "frequency_hz": 0.228,
      "held_by": "Fay",
      "label": "reed cup",
      "last_used_by": "Fay",
      "need_targets": [
        "thirst",
        "connection_deficit"
      ],
      "object_id": "reed_cup",
      "owner": "commons",
      "place": "moss_hollow",
      "routine_uses": 25
    },
    "phase": "dusk_social",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "reed_cup",
      "phase": "dusk_social",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 85,
      "tick": 4
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "78430ddf8ebf57bb"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.22152,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1708,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.48,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1428,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "social_check",
      "need_key": "connection_deficit",
      "score": 0.48,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 86,
    "flower_node": "social_petal",
    "frequency_hz": 0.2618,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.048,
      "rest_debt": 0.076,
      "routine_boredom": 0.0,
      "safety_concern": 0.06,
      "thirst": 0.024,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": 0.012,
      "rest_debt": 0.01,
      "thirst": 0.012
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
      "place": "stone_ridge",
      "routine_uses": 13
    },
    "object_used": {
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
      "place": "stone_ridge",
      "routine_uses": 14
    },
    "phase": "dusk_social",
    "place_after": "clay_basin",
    "place_before": "reed_wetland",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "social_check",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "signal_shell",
      "phase": "dusk_social",
      "place_after": "clay_basin",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 86,
      "tick": 4
    },
    "route_step": {
      "avatar_traversable": true,
      "distance": 0.286356,
      "flower_node": "social_petal",
      "frequency_hz": 0.2618,
      "from": "reed_wetland",
      "hazard": 0.275466,
      "kind": "water_clay_path",
      "route_cost": 0.677626,
      "route_hash": "afafa45735bc7c2f",
      "to": "clay_basin"
    },
    "social_continuity_bias_applied": true,
    "tick": 4
  },
  {
    "agent_id": "Ari",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "246ead13187b9dd5"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "hearth_vale"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.58812,
        "target_place": "hearth_vale"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18016,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1238,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.58812,
      "selection_policy": "need_scored",
      "target_place": "hearth_vale"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 87,
    "flower_node": "root_rest",
    "frequency_hz": 0.213,
    "home_place": "hearth_vale",
    "moved": false,
    "need_before": {
      "autonomy_pressure": 0.17500000000000004,
      "cold": 0.41999999999999993,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.22,
      "fatigue": 0.06,
      "rest_debt": 0.086,
      "routine_boredom": 0.0,
      "safety_concern": 0.009999999999999981,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.3599999999999998
    },
    "need_delta": {
      "fatigue": -0.06,
      "rest_debt": -0.086,
      "thirst": 0.012
    },
    "object_before": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 20
    },
    "object_used": {
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
      "place": "hearth_vale",
      "routine_uses": 21
    },
    "phase": "night_rest",
    "place_after": "hearth_vale",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "repair_clay_latch",
      "required_object": "clay_patch_kit",
      "work_place": "clay_basin"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Ari",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "hearth_vale",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "repair_clay_latch",
        "required_object": "clay_patch_kit",
        "work_place": "clay_basin"
      },
      "replay_index": 87,
      "tick": 5
    },
    "route_step": null,
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Fay",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "0f4a0453f9d28686"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "dry_cloak",
        "score": 0.2,
        "target_place": "moss_hollow"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "dry_cloak",
        "score": 0.58812,
        "target_place": "moss_hollow"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "reed_cup",
        "score": 0.18808,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "glass_lens",
        "score": 0.1466,
        "target_place": "stone_ridge"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.58812,
      "selection_policy": "need_scored",
      "target_place": "moss_hollow"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 88,
    "flower_node": "return_petal",
    "frequency_hz": 0.256115,
    "home_place": "moss_hollow",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.255,
      "cold": 0.34,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.35,
      "fatigue": 0.06,
      "rest_debt": 0.086,
      "routine_boredom": 0.0,
      "safety_concern": 0.07,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.0
    },
    "need_delta": {
      "fatigue": -0.06,
      "rest_debt": -0.086,
      "thirst": 0.012
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 17
    },
    "object_used": {
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
      "last_used_by": "Fay",
      "need_targets": [
        "wetness",
        "cold"
      ],
      "object_id": "dry_cloak",
      "owner": "Fay",
      "place": "moss_hollow",
      "routine_uses": 18
    },
    "phase": "night_rest",
    "place_after": "moss_hollow",
    "place_before": "hearth_vale",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "dry_moss_bedding",
      "required_object": "dry_cloak",
      "work_place": "moss_hollow"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Fay",
      "day": 4,
      "object_id": "dry_cloak",
      "phase": "night_rest",
      "place_after": "moss_hollow",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "dry_moss_bedding",
        "required_object": "dry_cloak",
        "work_place": "moss_hollow"
      },
      "replay_index": 88,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  },
  {
    "agent_id": "Milo",
    "autonomy_tick": {
      "manual_script_event": false,
      "policy": "routine_need_object_route_score",
      "tick_hash": "09bb68070feb0f44"
    },
    "candidate_scores": [
      {
        "action": "home_tend",
        "need_key": "routine_boredom",
        "object_id": "ember_blanket",
        "score": 0.2,
        "target_place": "stone_ridge"
      },
      {
        "action": "rest",
        "need_key": "rest_debt",
        "object_id": "ember_blanket",
        "score": 0.58812,
        "target_place": "stone_ridge"
      },
      {
        "action": "care_drink",
        "need_key": "thirst",
        "object_id": "reed_cup",
        "score": 0.1762,
        "target_place": "moss_hollow"
      },
      {
        "action": "social_check",
        "need_key": "connection_deficit",
        "object_id": "signal_shell",
        "score": 0.18096,
        "target_place": "hearth_vale"
      },
      {
        "action": "explore_safety",
        "need_key": "safety_concern",
        "object_id": "signal_shell",
        "score": 0.1428,
        "target_place": "glass_mire"
      }
    ],
    "chosen_action": {
      "action": "rest",
      "need_key": "rest_debt",
      "score": 0.58812,
      "selection_policy": "need_scored",
      "target_place": "stone_ridge"
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "natural_language_emergence": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_agent_routine_home_work_unscripted_object_use",
    "day": 4,
    "event_id": 89,
    "flower_node": "explore_petal",
    "frequency_hz": 0.264425,
    "home_place": "stone_ridge",
    "moved": true,
    "need_before": {
      "autonomy_pressure": 0.25,
      "cold": 0.29,
      "connection_deficit": 0.0,
      "curiosity_deficit": 0.33999999999999997,
      "fatigue": 0.06,
      "rest_debt": 0.086,
      "routine_boredom": 0.0,
      "safety_concern": 0.06,
      "thirst": 0.036000000000000004,
      "unfinished_task": 0.010000000000000057
    },
    "need_delta": {
      "fatigue": -0.06,
      "rest_debt": -0.086,
      "thirst": 0.012
    },
    "object_before": {
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
      "place": "hearth_vale",
      "routine_uses": 21
    },
    "object_used": {
      "affordances": [
        "warmth",
        "rest",
        "comfort"
      ],
      "available": true,
      "flower_node": "root_rest",
      "frequency_hz": 0.213,
      "held_by": "Milo",
      "label": "ember blanket",
      "last_used_by": "Milo",
      "need_targets": [
        "cold",
        "fatigue"
      ],
      "object_id": "ember_blanket",
      "owner": "Ari",
      "place": "hearth_vale",
      "routine_uses": 22
    },
    "phase": "night_rest",
    "place_after": "stone_ridge",
    "place_before": "clay_basin",
    "private_workspace_hidden": true,
    "project_packet": {
      "complete": true,
      "progress": 0.9600000000000001,
      "project_id": "ridge_warning_watch",
      "required_object": "signal_shell",
      "work_place": "stone_ridge"
    },
    "replay_frame": {
      "action": "rest",
      "agent_id": "Milo",
      "day": 4,
      "object_id": "ember_blanket",
      "phase": "night_rest",
      "place_after": "stone_ridge",
      "project": {
        "complete": true,
        "progress": 0.9600000000000001,
        "project_id": "ridge_warning_watch",
        "required_object": "signal_shell",
        "work_place": "stone_ridge"
      },
      "replay_index": 89,
      "tick": 5
    },
    "route_step": {
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
    "social_continuity_bias_applied": true,
    "tick": 5
  }
];
