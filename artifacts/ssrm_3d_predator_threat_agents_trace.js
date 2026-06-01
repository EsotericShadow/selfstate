window.SSRM_3D_PREDATOR_THREAT_AGENTS_TRACE = {
  "scenario": {
    "index": 4,
    "name": "social_warning_group_defense",
    "pressure": "group warning and coordinated shelter reduce a tracker that exploits isolated agents",
    "expected_threat_perception": true,
    "expected_self_vulnerability": true,
    "expected_sound_scent": false,
    "expected_stealth": false,
    "expected_shelter": true,
    "expected_alarm": true,
    "expected_social_warning": true,
    "expected_continuity": false,
    "threat_intensity": 0.86,
    "sound_tracking": 0.24,
    "scent_tracking": 0.2,
    "weakness_tracking": 0.62,
    "routine_tracking": 0.22,
    "night_factor": 0.3,
    "initial_vulnerability": 0.38,
    "required_progress": 90.0,
    "work_rate": 0.57,
    "restore_tick": -1
  },
  "policy": {
    "name": "social_warning_shelter_planner",
    "threat_perception": true,
    "self_vulnerability_state": true,
    "sound_scent_memory": false,
    "stealth_action": false,
    "shelter_memory": true,
    "tool_alarm": true,
    "social_warning": true,
    "continuity_memory": false,
    "risk_threshold": 0.28,
    "stealth_bias": 0.18,
    "shelter_bias": 0.78,
    "group_bias": 0.88
  },
  "episode_result": {
    "scenario": 4,
    "scenario_name": "social_warning_group_defense",
    "policy_name": "social_warning_shelter_planner",
    "condition": "full_control",
    "episode": 0,
    "total_reward": 131.26004874765806,
    "survival": 1.0,
    "task_success": 1.0,
    "progress": 93.39818407914285,
    "energy": 0.5883128618852875,
    "injury": 0.0,
    "detection_risk": 0.5870978255437486,
    "fear_state": 0.7103162757712534,
    "noise_level": 1.0,
    "scent_trace": 1.0,
    "shelter_security": 0.6136,
    "social_support": 0.6784,
    "attacks": 0,
    "near_misses": 7,
    "stealth_actions": 0,
    "shelter_actions": 1,
    "alarm_actions": 1,
    "social_warning_actions": 1,
    "route_changes": 0,
    "continuity_resets": 0,
    "threat_misses": 0
  },
  "condition_outcomes": {
    "full_control": {
      "mean_reward": 88.07839154210478,
      "mean_injury": 0.07044374729065951,
      "mean_detection_risk": 0.6177313967439246,
      "mean_attacks": 0.4791666666666667,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "no_threat_perception": {
      "mean_reward": -759.1018205432346,
      "mean_injury": 1.0,
      "mean_detection_risk": 1.554312606438538,
      "mean_attacks": 13.125,
      "mean_shelter_security": 0.18000000000000002,
      "mean_social_support": 0.0
    },
    "no_self_vulnerability_state": {
      "mean_reward": -355.00308819663525,
      "mean_injury": 0.9011741124644134,
      "mean_detection_risk": 0.7333424736977171,
      "mean_attacks": 5.895833333333333,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "no_sound_scent_memory": {
      "mean_reward": 96.58268473087618,
      "mean_injury": 0.05735217353004544,
      "mean_detection_risk": 0.6119137263805806,
      "mean_attacks": 0.3958333333333333,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "no_stealth_action": {
      "mean_reward": 88.81297160911517,
      "mean_injury": 0.07266212472160734,
      "mean_detection_risk": 0.6149926744741939,
      "mean_attacks": 0.5,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "no_shelter_access": {
      "mean_reward": -417.1127175888036,
      "mean_injury": 0.9854760185219092,
      "mean_detection_risk": 0.89834404516517,
      "mean_attacks": 5.9375,
      "mean_shelter_security": 0.18000000000000002,
      "mean_social_support": 0.6784
    },
    "no_tool_alarm": {
      "mean_reward": -522.2381449648992,
      "mean_injury": 1.0,
      "mean_detection_risk": 1.1893180879987766,
      "mean_attacks": 8.25,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "no_social_warning": {
      "mean_reward": -617.1223872362624,
      "mean_injury": 1.0,
      "mean_detection_risk": 1.5351045361561095,
      "mean_attacks": 9.958333333333334,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.0
    },
    "no_continuity": {
      "mean_reward": 76.13110968331216,
      "mean_injury": 0.09575354635077439,
      "mean_detection_risk": 0.6102493989896208,
      "mean_attacks": 0.6666666666666666,
      "mean_shelter_security": 0.6136,
      "mean_social_support": 0.6784
    },
    "reactive_panic_only": {
      "mean_reward": -766.3150044997855,
      "mean_injury": 1.0,
      "mean_detection_risk": 1.5788708701873604,
      "mean_attacks": 13.229166666666666,
      "mean_shelter_security": 0.18000000000000002,
      "mean_social_support": 0.0
    },
    "omniscient_threat_control": {
      "mean_reward": 51.77086144494506,
      "mean_injury": 0.13973743718370937,
      "mean_detection_risk": 0.5147528492388057,
      "mean_attacks": 0.6458333333333334,
      "mean_shelter_security": 0.18000000000000002,
      "mean_social_support": 0.6856
    }
  },
  "frames": [
    {
      "tick": 0,
      "action": "warn_group",
      "progress": -0.18,
      "energy": 0.903,
      "injury": 0.0,
      "detection_risk": 0.0,
      "fear_state": 0.012,
      "noise_level": 0.299,
      "scent_trace": 0.396,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense"
      ]
    },
    {
      "tick": 5,
      "action": "work",
      "progress": 2.518,
      "energy": 0.897,
      "injury": 0.0,
      "detection_risk": 0.051,
      "fear_state": 0.047,
      "noise_level": 0.333,
      "scent_trace": 0.42,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense"
      ]
    },
    {
      "tick": 8,
      "action": "set_alarm",
      "progress": 3.428,
      "energy": 0.882,
      "injury": 0.0,
      "detection_risk": 0.031,
      "fear_state": 0.068,
      "noise_level": 0.346,
      "scent_trace": 0.43,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 10,
      "action": "work",
      "progress": 4.5,
      "energy": 0.879,
      "injury": 0.0,
      "detection_risk": 0.039,
      "fear_state": 0.069,
      "noise_level": 0.36,
      "scent_trace": 0.439,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 15,
      "action": "work",
      "progress": 7.17,
      "energy": 0.873,
      "injury": 0.0,
      "detection_risk": 0.058,
      "fear_state": 0.074,
      "noise_level": 0.393,
      "scent_trace": 0.463,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 20,
      "action": "work",
      "progress": 9.829,
      "energy": 0.866,
      "injury": 0.0,
      "detection_risk": 0.079,
      "fear_state": 0.081,
      "noise_level": 0.427,
      "scent_trace": 0.487,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 25,
      "action": "work",
      "progress": 12.474,
      "energy": 0.86,
      "injury": 0.0,
      "detection_risk": 0.102,
      "fear_state": 0.091,
      "noise_level": 0.46,
      "scent_trace": 0.511,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 30,
      "action": "work",
      "progress": 15.105,
      "energy": 0.854,
      "injury": 0.0,
      "detection_risk": 0.126,
      "fear_state": 0.103,
      "noise_level": 0.494,
      "scent_trace": 0.535,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 35,
      "action": "work",
      "progress": 17.72,
      "energy": 0.847,
      "injury": 0.0,
      "detection_risk": 0.152,
      "fear_state": 0.117,
      "noise_level": 0.528,
      "scent_trace": 0.559,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 40,
      "action": "work",
      "progress": 20.318,
      "energy": 0.841,
      "injury": 0.0,
      "detection_risk": 0.179,
      "fear_state": 0.133,
      "noise_level": 0.561,
      "scent_trace": 0.583,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 45,
      "action": "work",
      "progress": 22.899,
      "energy": 0.834,
      "injury": 0.0,
      "detection_risk": 0.208,
      "fear_state": 0.151,
      "noise_level": 0.595,
      "scent_trace": 0.607,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 50,
      "action": "work",
      "progress": 25.46,
      "energy": 0.828,
      "injury": 0.0,
      "detection_risk": 0.238,
      "fear_state": 0.17,
      "noise_level": 0.628,
      "scent_trace": 0.631,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 55,
      "action": "work",
      "progress": 28.001,
      "energy": 0.821,
      "injury": 0.0,
      "detection_risk": 0.27,
      "fear_state": 0.192,
      "noise_level": 0.662,
      "scent_trace": 0.655,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 60,
      "action": "work",
      "progress": 30.52,
      "energy": 0.814,
      "injury": 0.0,
      "detection_risk": 0.303,
      "fear_state": 0.215,
      "noise_level": 0.696,
      "scent_trace": 0.679,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 65,
      "action": "work",
      "progress": 33.018,
      "energy": 0.807,
      "injury": 0.0,
      "detection_risk": 0.338,
      "fear_state": 0.24,
      "noise_level": 0.729,
      "scent_trace": 0.703,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 70,
      "action": "work",
      "progress": 35.491,
      "energy": 0.8,
      "injury": 0.0,
      "detection_risk": 0.374,
      "fear_state": 0.267,
      "noise_level": 0.763,
      "scent_trace": 0.727,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 75,
      "action": "work",
      "progress": 37.94,
      "energy": 0.793,
      "injury": 0.0,
      "detection_risk": 0.411,
      "fear_state": 0.295,
      "noise_level": 0.796,
      "scent_trace": 0.751,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 80,
      "action": "work",
      "progress": 40.364,
      "energy": 0.786,
      "injury": 0.0,
      "detection_risk": 0.451,
      "fear_state": 0.325,
      "noise_level": 0.83,
      "scent_trace": 0.775,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 85,
      "action": "work",
      "progress": 42.761,
      "energy": 0.778,
      "injury": 0.0,
      "detection_risk": 0.491,
      "fear_state": 0.356,
      "noise_level": 0.864,
      "scent_trace": 0.799,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 90,
      "action": "work",
      "progress": 45.13,
      "energy": 0.771,
      "injury": 0.0,
      "detection_risk": 0.533,
      "fear_state": 0.389,
      "noise_level": 0.897,
      "scent_trace": 0.823,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 95,
      "action": "work",
      "progress": 47.47,
      "energy": 0.763,
      "injury": 0.0,
      "detection_risk": 0.577,
      "fear_state": 0.423,
      "noise_level": 0.931,
      "scent_trace": 0.847,
      "shelter_security": 0.18,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise"
      ]
    },
    {
      "tick": 100,
      "action": "seek_shelter",
      "progress": 49.02,
      "energy": 0.755,
      "injury": 0.0,
      "detection_risk": 0.607,
      "fear_state": 0.459,
      "noise_level": 0.918,
      "scent_trace": 0.84,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise",
        "shelter lowered exposure"
      ]
    },
    {
      "tick": 105,
      "action": "work",
      "progress": 51.314,
      "energy": 0.748,
      "injury": 0.0,
      "detection_risk": 0.626,
      "fear_state": 0.475,
      "noise_level": 0.951,
      "scent_trace": 0.864,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise",
        "shelter lowered exposure"
      ]
    },
    {
      "tick": 110,
      "action": "work",
      "progress": 53.592,
      "energy": 0.74,
      "injury": 0.0,
      "detection_risk": 0.646,
      "fear_state": 0.494,
      "noise_level": 0.985,
      "scent_trace": 0.888,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise",
        "shelter lowered exposure"
      ]
    },
    {
      "tick": 115,
      "action": "work",
      "progress": 55.856,
      "energy": 0.732,
      "injury": 0.0,
      "detection_risk": 0.668,
      "fear_state": 0.513,
      "noise_level": 1.0,
      "scent_trace": 0.912,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "group warning raised defense",
        "alarm reduced surprise",
        "shelter lowered exposure"
      ]
    },
    {
      "tick": 120,
      "action": "work",
      "progress": 58.122,
      "energy": 0.723,
      "injury": 0.0,
      "detection_risk": 0.62,
      "fear_state": 0.531,
      "noise_level": 1.0,
      "scent_trace": 0.936,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "alarm reduced surprise",
        "shelter lowered exposure",
        "near miss"
      ]
    },
    {
      "tick": 125,
      "action": "work",
      "progress": 60.384,
      "energy": 0.715,
      "injury": 0.0,
      "detection_risk": 0.643,
      "fear_state": 0.549,
      "noise_level": 1.0,
      "scent_trace": 0.96,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "alarm reduced surprise",
        "shelter lowered exposure",
        "near miss"
      ]
    },
    {
      "tick": 130,
      "action": "work",
      "progress": 62.63,
      "energy": 0.707,
      "injury": 0.0,
      "detection_risk": 0.596,
      "fear_state": 0.566,
      "noise_level": 1.0,
      "scent_trace": 0.984,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "shelter lowered exposure",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 135,
      "action": "work",
      "progress": 64.892,
      "energy": 0.699,
      "injury": 0.0,
      "detection_risk": 0.62,
      "fear_state": 0.581,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "shelter lowered exposure",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 140,
      "action": "work",
      "progress": 67.137,
      "energy": 0.69,
      "injury": 0.0,
      "detection_risk": 0.645,
      "fear_state": 0.597,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "shelter lowered exposure",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 145,
      "action": "work",
      "progress": 69.379,
      "energy": 0.682,
      "injury": 0.0,
      "detection_risk": 0.599,
      "fear_state": 0.611,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 150,
      "action": "work",
      "progress": 71.624,
      "energy": 0.673,
      "injury": 0.0,
      "detection_risk": 0.623,
      "fear_state": 0.623,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 155,
      "action": "work",
      "progress": 73.853,
      "energy": 0.665,
      "injury": 0.0,
      "detection_risk": 0.648,
      "fear_state": 0.636,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 160,
      "action": "work",
      "progress": 76.091,
      "energy": 0.656,
      "injury": 0.0,
      "detection_risk": 0.602,
      "fear_state": 0.647,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 165,
      "action": "work",
      "progress": 78.32,
      "energy": 0.648,
      "injury": 0.0,
      "detection_risk": 0.627,
      "fear_state": 0.657,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 170,
      "action": "work",
      "progress": 80.54,
      "energy": 0.639,
      "injury": 0.0,
      "detection_risk": 0.582,
      "fear_state": 0.667,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 175,
      "action": "work",
      "progress": 82.771,
      "energy": 0.63,
      "injury": 0.0,
      "detection_risk": 0.607,
      "fear_state": 0.675,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 180,
      "action": "work",
      "progress": 84.986,
      "energy": 0.622,
      "injury": 0.0,
      "detection_risk": 0.632,
      "fear_state": 0.684,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 185,
      "action": "work",
      "progress": 87.204,
      "energy": 0.613,
      "injury": 0.0,
      "detection_risk": 0.587,
      "fear_state": 0.692,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 190,
      "action": "work",
      "progress": 89.421,
      "energy": 0.604,
      "injury": 0.0,
      "detection_risk": 0.612,
      "fear_state": 0.699,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 195,
      "action": "work",
      "progress": 91.622,
      "energy": 0.595,
      "injury": 0.0,
      "detection_risk": 0.567,
      "fear_state": 0.706,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    },
    {
      "tick": 199,
      "action": "work",
      "progress": 93.398,
      "energy": 0.588,
      "injury": 0.0,
      "detection_risk": 0.587,
      "fear_state": 0.71,
      "noise_level": 1.0,
      "scent_trace": 1.0,
      "shelter_security": 0.614,
      "social_support": 0.678,
      "attacks": 0,
      "notes": [
        "near miss",
        "near miss",
        "near miss"
      ]
    }
  ],
  "trace_note": "Threats, fear-like state, stealth, alarms, shelter, social warning, and continuity are abstract control variables."
};
