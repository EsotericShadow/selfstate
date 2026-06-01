window.SSRM_3D_STRUCTURED_PERCEPTION_TRACE = {
  "scenario": {
    "index": 3,
    "name": "night_multimodal_shelter",
    "pressure": "night route requires cone vision, audio beacons, markers, and memory",
    "expected_vision_pressure": true,
    "expected_audio_pressure": true,
    "expected_tool_pressure": true,
    "expected_self_state_pressure": false,
    "light_level": 0.28,
    "weather_visibility": 0.52,
    "occlusion": 0.38,
    "fov_pressure": 0.7,
    "visual_damage": 0.0,
    "hearing_damage": 0.0,
    "hazard_pressure": 0.58,
    "interruption_pressure": 0.54,
    "resource_audio": 0.52,
    "hazard_audio": 0.62,
    "social_audio": 0.32
  },
  "policy": {
    "name": "multimodal_integrator",
    "vision_enabled": true,
    "audio_enabled": true,
    "visual_memory": true,
    "audio_memory": true,
    "tool_markers": true,
    "tool_alarms": true,
    "attention_focus": true,
    "self_sensor_adapt": false,
    "exploration": 0.42,
    "risk_tolerance": 0.34,
    "tool_cost_tolerance": 0.74
  },
  "frames": [
    {
      "tick": 0,
      "heading": -60.0,
      "fov_center": -60.0,
      "fov_width": 86.0,
      "light_level": 0.23,
      "vision_quality": 0.466,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "water_source",
          "bearing": -24.0,
          "distance_estimate": 34.0,
          "confidence": 0.466,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -35.0,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 1,
      "heading": -48.0,
      "fov_center": -48.0,
      "fov_width": 86.0,
      "light_level": 0.244,
      "vision_quality": 0.423,
      "audio_quality": 1.0,
      "visual_events": [],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -30.5,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 2,
      "heading": -36.0,
      "fov_center": -36.0,
      "fov_width": 86.0,
      "light_level": 0.257,
      "vision_quality": 0.433,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "water_source",
          "bearing": -15.8,
          "distance_estimate": 30.7,
          "confidence": 0.433,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -25.9,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 3,
      "heading": -24.0,
      "fov_center": -24.0,
      "fov_width": 86.0,
      "light_level": 0.268,
      "vision_quality": 0.464,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "hazard",
          "bearing": 30.4,
          "distance_estimate": 20.1,
          "confidence": 0.384,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -21.4,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 4,
      "heading": -12.0,
      "fov_center": -12.0,
      "fov_width": 86.0,
      "light_level": 0.275,
      "vision_quality": 0.459,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "water_source",
          "bearing": -7.6,
          "distance_estimate": 27.5,
          "confidence": 0.459,
          "motion": "still"
        },
        {
          "kind": "hazard",
          "bearing": 27.8,
          "distance_estimate": 19.5,
          "confidence": 0.379,
          "motion": "approaching"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -16.8,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 5,
      "heading": 0.0,
      "fov_center": 0.0,
      "fov_width": 86.0,
      "light_level": 0.279,
      "vision_quality": 0.437,
      "audio_quality": 1.0,
      "visual_events": [],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -12.3,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        },
        {
          "kind": "social_call",
          "loudness": 0.9,
          "direction": 76.0,
          "confidence": 0.98,
          "source_memory": "unknown_agent"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 6,
      "heading": 12.0,
      "fov_center": 12.0,
      "fov_width": 86.0,
      "light_level": 0.279,
      "vision_quality": 0.455,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "water_source",
          "bearing": 0.5,
          "distance_estimate": 24.2,
          "confidence": 0.455,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -7.7,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        },
        {
          "kind": "social_call",
          "loudness": 0.9,
          "direction": 76.0,
          "confidence": 0.98,
          "source_memory": "unknown_agent"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 7,
      "heading": 24.0,
      "fov_center": 24.0,
      "fov_width": 86.0,
      "light_level": 0.275,
      "vision_quality": 0.426,
      "audio_quality": 1.0,
      "visual_events": [],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": -3.2,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 8,
      "heading": 36.0,
      "fov_center": 36.0,
      "fov_width": 86.0,
      "light_level": 0.268,
      "vision_quality": 0.462,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "shelter",
          "bearing": 8.7,
          "distance_estimate": 20.9,
          "confidence": 0.462,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": 1.4,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 9,
      "heading": 48.0,
      "fov_center": 48.0,
      "fov_width": 86.0,
      "light_level": 0.257,
      "vision_quality": 0.447,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "hazard",
          "bearing": 15.1,
          "distance_estimate": 16.3,
          "confidence": 0.367,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": 5.9,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 10,
      "heading": 60.0,
      "fov_center": 60.0,
      "fov_width": 86.0,
      "light_level": 0.244,
      "vision_quality": 0.443,
      "audio_quality": 1.0,
      "visual_events": [
        {
          "kind": "shelter",
          "bearing": 16.9,
          "distance_estimate": 17.6,
          "confidence": 0.443,
          "motion": "still"
        }
      ],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": 10.5,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    },
    {
      "tick": 11,
      "heading": 72.0,
      "fov_center": 72.0,
      "fov_width": 86.0,
      "light_level": 0.23,
      "vision_quality": 0.449,
      "audio_quality": 1.0,
      "visual_events": [],
      "audio_events": [
        {
          "kind": "tool_alarm",
          "loudness": 1.0,
          "direction": 15.0,
          "confidence": 1.0,
          "source_memory": "known_alarm_03"
        }
      ],
      "memory_reads": {
        "visual": 2,
        "audio": 4
      },
      "tool_state": {
        "marker_active": true,
        "alarm_active": true
      }
    }
  ],
  "condition_outcomes": {
    "full_perception": {
      "mean_reward": 131.0870870525218,
      "mean_success_rate": 1.0
    },
    "no_perception": {
      "mean_reward": 56.08706414533406,
      "mean_success_rate": 0.32963024
    },
    "no_vision": {
      "mean_reward": 107.0728162784489,
      "mean_success_rate": 0.7523342400000002
    },
    "no_audio": {
      "mean_reward": 47.539623605384996,
      "mean_success_rate": 0.3659802997666532
    },
    "no_fov_limit": {
      "mean_reward": 131.21426411156872,
      "mean_success_rate": 1.0
    },
    "constant_loudness_audio": {
      "mean_reward": 130.5487484967754,
      "mean_success_rate": 0.9986731624692456
    },
    "no_direction_audio": {
      "mean_reward": 118.90691324213675,
      "mean_success_rate": 0.9724356883726989
    },
    "visual_memory_ablation": {
      "mean_reward": 121.95873847185884,
      "mean_success_rate": 0.9982961506657121
    },
    "audio_memory_ablation": {
      "mean_reward": 121.17437093691672,
      "mean_success_rate": 0.9962596614019193
    },
    "tool_alarm_ablation": {
      "mean_reward": 101.10387012884412,
      "mean_success_rate": 0.8707031041847887
    },
    "body_state_blind_perception": {
      "mean_reward": 131.23328722860893,
      "mean_success_rate": 1.0
    },
    "omniscient_vision_control": {
      "mean_reward": 131.3007329887852,
      "mean_success_rate": 1.0
    }
  }
};
