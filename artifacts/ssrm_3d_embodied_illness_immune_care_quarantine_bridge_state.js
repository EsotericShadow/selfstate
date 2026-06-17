window.SSRM_3D_EMBODIED_ILLNESS_IMMUNE_CARE_QUARANTINE_STATE = {
  "condition": "integrated_embodied_illness_immune_care_quarantine",
  "config": {
    "days": 9,
    "seed": 20260801,
    "source_state": "artifacts/ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_state.json"
  },
  "health_state": {
    "bodies": {
      "Ari": {
        "agent_id": "Ari",
        "care_received": 4,
        "contagiousness": 0.0317121000000001,
        "energy": 1.0,
        "fatigue": 0.005812110000000019,
        "fever": 0.0,
        "home": "hearth_vale",
        "hydration": 0.9299999999999999,
        "immune_strength": 1.0,
        "infection_load": 0.07550500000000024,
        "quarantined": false,
        "social_access": 0.9773485
      },
      "Fay": {
        "agent_id": "Fay",
        "care_received": 5,
        "contagiousness": 0.03203256000000007,
        "energy": 1.0,
        "fatigue": 0.005710680000000013,
        "fever": 0.0,
        "home": "moss_hollow",
        "hydration": 0.9299999999999999,
        "immune_strength": 1.0,
        "infection_load": 0.07626800000000017,
        "quarantined": false,
        "social_access": 0.9771196
      },
      "Milo": {
        "agent_id": "Milo",
        "care_received": 6,
        "contagiousness": 0.0,
        "energy": 1.0,
        "fatigue": 0.0,
        "fever": 0.0,
        "home": "stone_ridge",
        "hydration": 1.0,
        "immune_strength": 1.0,
        "infection_load": 0.0,
        "quarantined": false,
        "social_access": 1.0
      }
    },
    "condition": "integrated_embodied_illness_immune_care_quarantine",
    "ecology_nodes": {
      "compost_bed": {
        "capacity": 1.0,
        "cleaning_events": 0,
        "events": 10,
        "flower_node": "work_petal",
        "frequency_hz": 0.244,
        "initial_stock": 0.25,
        "kind": "compost",
        "maturity": 1.0,
        "node_id": "compost_bed",
        "place": "clay_basin",
        "regrowth": 0.06,
        "spoilage": 0.0,
        "stock": 1.0
      },
      "hearth_cistern": {
        "capacity": 0.9,
        "cleaning_events": 0,
        "cleanliness": 0.6199999999999998,
        "events": 10,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.214,
        "initial_stock": 0.58,
        "kind": "water",
        "node_id": "hearth_cistern",
        "place": "hearth_vale",
        "regrowth": 0.035,
        "spoilage": 0.02,
        "stock": 0.9
      },
      "moss_food_cache": {
        "capacity": 1.0,
        "cleaning_events": 0,
        "events": 10,
        "flower_node": "root_rest",
        "frequency_hz": 0.218,
        "freshness": 0.6099999999999998,
        "initial_stock": 0.62,
        "kind": "food",
        "node_id": "moss_food_cache",
        "place": "moss_hollow",
        "regrowth": 0.07,
        "spoilage": 0.055,
        "stock": 1.0
      },
      "reed_water_channel": {
        "capacity": 1.0,
        "cleaning_events": 0,
        "cleanliness": 0.2799999999999998,
        "events": 10,
        "flower_node": "return_petal",
        "frequency_hz": 0.233,
        "initial_stock": 0.74,
        "kind": "water",
        "node_id": "reed_water_channel",
        "place": "reed_wetland",
        "regrowth": 0.08,
        "spoilage": 0.03,
        "stock": 1.0
      },
      "sleeping_moss": {
        "capacity": 1.0,
        "cleaning_events": 0,
        "cleanliness": 0.4099999999999997,
        "events": 10,
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "initial_stock": 0.6,
        "kind": "habitat",
        "node_id": "sleeping_moss",
        "place": "moss_hollow",
        "regrowth": 0.045,
        "spoilage": 0.035,
        "stock": 1.0
      },
      "waste_pit": {
        "capacity": 0.9,
        "cleaning_events": 4,
        "contamination": 0.11499999999999996,
        "events": 10,
        "flower_node": "explore_petal",
        "frequency_hz": 0.267,
        "initial_stock": 0.18,
        "kind": "waste",
        "node_id": "waste_pit",
        "place": "glass_mire",
        "regrowth": 0.0,
        "spoilage": 0.065,
        "stock": 0.2899999999999999
      }
    },
    "events": [
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11588823999999998,
          "fever": 0.05530720000000001,
          "home": "stone_ridge",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.663,
          "infection_load": 0.21125200000000008,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 0,
          "contagiousness": 0.02,
          "energy": 0.72,
          "fatigue": 0.24,
          "fever": 0.04,
          "home": "stone_ridge",
          "hydration": 0.7,
          "immune_strength": 0.56,
          "infection_load": 0.26,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.592351,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.18,
          "remaining_doses": 26
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.02,
          "contained": true
        },
        "day": 0,
        "event_id": 0,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5632,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.211252
        },
        "illness_packet": {
          "delta": 0.093072,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.592351,
            "triaged": true
          },
          "day": 0,
          "fever": 0.05530720000000001,
          "infection_load": 0.21125200000000008,
          "quarantined": true,
          "replay_index": 0
        },
        "rest_packet": {
          "energy_delta": 0.16,
          "remaining_slots": 26,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.115888,
          "fever": 0.055307
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11373183999999997,
          "fever": 0.0505152,
          "home": "moss_hollow",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.783,
          "infection_load": 0.16333200000000006,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 0,
          "contagiousness": 0.02,
          "energy": 0.72,
          "fatigue": 0.24,
          "fever": 0.04,
          "home": "moss_hollow",
          "hydration": 0.7,
          "immune_strength": 0.68,
          "infection_load": 0.22,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.5391,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.18,
          "remaining_doses": 25
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.02,
          "contained": true
        },
        "day": 0,
        "event_id": 1,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5512,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.163332
        },
        "illness_packet": {
          "delta": 0.085152,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "high",
            "triage_score": 0.5391,
            "triaged": true
          },
          "day": 0,
          "fever": 0.0505152,
          "infection_load": 0.16333200000000006,
          "quarantined": true,
          "replay_index": 1
        },
        "rest_packet": {
          "energy_delta": 0.16,
          "remaining_slots": 25,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.113732,
          "fever": 0.050515
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11098323999999998,
          "fever": 0.04440720000000001,
          "home": "hearth_vale",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.723,
          "infection_load": 0.10225200000000009,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 0,
          "contagiousness": 0.02,
          "energy": 0.72,
          "fatigue": 0.24,
          "fever": 0.04,
          "home": "hearth_vale",
          "hydration": 0.7,
          "immune_strength": 0.62,
          "infection_load": 0.16,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.471225,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.18,
          "remaining_doses": 24
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.02,
          "contained": true
        },
        "day": 0,
        "event_id": 2,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5332,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.102252
        },
        "illness_packet": {
          "delta": 0.084072,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "high",
            "triage_score": 0.471225,
            "triaged": true
          },
          "day": 0,
          "fever": 0.04440720000000001,
          "infection_load": 0.10225200000000009,
          "quarantined": true,
          "replay_index": 2
        },
        "rest_packet": {
          "energy_delta": 0.16,
          "remaining_slots": 24,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.110983,
          "fever": 0.044407
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.06077610000000002,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.766,
          "infection_load": 0.11286900000000014,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11588823999999998,
          "fever": 0.05530720000000001,
          "home": "stone_ridge",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.663,
          "infection_load": 0.21125200000000008,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.395302,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.12,
          "remaining_doses": 23
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": true
        },
        "day": 1,
        "event_id": 3,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5632,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.112869
        },
        "illness_packet": {
          "delta": 0.043437,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.395302,
            "triaged": true
          },
          "day": 1,
          "fever": 0.06077610000000002,
          "infection_load": 0.11286900000000014,
          "quarantined": true,
          "replay_index": 3
        },
        "rest_packet": {
          "energy_delta": 0.12,
          "remaining_slots": 23,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.060776
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.05040010000000001,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 0.886,
          "infection_load": 0.057029000000000135,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11373183999999997,
          "fever": 0.0505152,
          "home": "moss_hollow",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.783,
          "infection_load": 0.16333200000000006,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.327919,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.12,
          "remaining_doses": 22
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": true
        },
        "day": 1,
        "event_id": 4,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5512,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.057029
        },
        "illness_packet": {
          "delta": 0.035517,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "high",
            "triage_score": 0.327919,
            "triaged": true
          },
          "day": 1,
          "fever": 0.05040010000000001,
          "infection_load": 0.057029000000000135,
          "quarantined": true,
          "replay_index": 4
        },
        "rest_packet": {
          "energy_delta": 0.12,
          "remaining_slots": 22,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.0504
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.03807610000000002,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 0.826,
          "infection_load": 0.0,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 1,
          "contagiousness": 0.0,
          "energy": 0.88,
          "fatigue": 0.11098323999999998,
          "fever": 0.04440720000000001,
          "home": "hearth_vale",
          "hydration": 0.8799999999999999,
          "immune_strength": 0.723,
          "infection_load": 0.10225200000000009,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.252049,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.12,
          "remaining_doses": 21
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": true
        },
        "day": 1,
        "event_id": 5,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5332,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.034437,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "high",
            "triage_score": 0.252049,
            "triaged": true
          },
          "day": 1,
          "fever": 0.03807610000000002,
          "infection_load": 0.0,
          "quarantined": true,
          "replay_index": 5
        },
        "rest_packet": {
          "energy_delta": 0.12,
          "remaining_slots": 21,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.038076
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.05720320000000004,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.869,
          "infection_load": 0.02245100000000018,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.06077610000000002,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.766,
          "infection_load": 0.11286900000000014,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.223322,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.0,
          "remaining_doses": 20
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": true
        },
        "day": 2,
        "event_id": 6,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6232,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.022451
        },
        "illness_packet": {
          "delta": 0.051402,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.223322,
            "triaged": true
          },
          "day": 2,
          "fever": 0.05720320000000004,
          "infection_load": 0.02245100000000018,
          "quarantined": true,
          "replay_index": 6
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 20,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.057203
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.04045120000000003,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 0.989,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.05040010000000001,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 0.886,
          "infection_load": 0.057029000000000135,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.142093,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.0,
          "remaining_doses": 19
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": false
        },
        "day": 2,
        "event_id": 7,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6112,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.043482,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "high",
            "triage_score": 0.142093,
            "triaged": true
          },
          "day": 2,
          "fever": 0.04045120000000003,
          "infection_load": 0.0,
          "quarantined": false,
          "replay_index": 7
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 19,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 1.0,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.040451
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 2,
          "contagiousness": 0.017808840000000013,
          "energy": 1.0,
          "fatigue": 0.0019080900000000016,
          "fever": 0.022316300000000025,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 0.826,
          "infection_load": 0.04240200000000004,
          "quarantined": false,
          "social_access": 0.9872794
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 2,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.03807610000000002,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 0.826,
          "infection_load": 0.0,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.065195,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 19
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.017809,
          "contained": false
        },
        "day": 2,
        "event_id": 8,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5932,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.042402
        },
        "illness_packet": {
          "delta": 0.042402,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.0,
          "recovered": false
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "monitor",
            "triage_score": 0.065195,
            "triaged": false
          },
          "day": 2,
          "fever": 0.022316300000000025,
          "infection_load": 0.04240200000000004,
          "quarantined": false,
          "replay_index": 8
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 19,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.987279,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": false,
          "fatigue": 0.001908,
          "fever": 0.022316
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 3,
          "contagiousness": 0.029071560000000093,
          "energy": 1.0,
          "fatigue": 0.00311481000000001,
          "fever": 0.04412500000000006,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 0.869,
          "infection_load": 0.06921800000000022,
          "quarantined": false,
          "social_access": 0.9792346
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.05720320000000004,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.869,
          "infection_load": 0.02245100000000018,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.114122,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 19
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.029072,
          "contained": false
        },
        "day": 3,
        "event_id": 9,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6232,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.069218
        },
        "illness_packet": {
          "delta": 0.046767,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.0,
          "recovered": false
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "monitor",
            "triage_score": 0.114122,
            "triaged": false
          },
          "day": 3,
          "fever": 0.04412500000000006,
          "infection_load": 0.06921800000000022,
          "quarantined": false,
          "replay_index": 9
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 19,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.979235,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.003115,
          "fever": 0.044125
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.015296700000000031,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 0.9289999999999999,
          "infection_load": 0.0,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 2,
          "contagiousness": 0.017808840000000013,
          "energy": 1.0,
          "fatigue": 0.0019080900000000016,
          "fever": 0.022316300000000025,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 0.826,
          "infection_load": 0.04240200000000004,
          "quarantined": false,
          "social_access": 0.9872794
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.161038,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 18
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.017809,
          "contained": true
        },
        "day": 3,
        "event_id": 10,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5932,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.087402,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "high",
            "triage_score": 0.161038,
            "triaged": true
          },
          "day": 3,
          "fever": 0.015296700000000031,
          "infection_load": 0.0,
          "quarantined": true,
          "replay_index": 10
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 18,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.015297
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0037731150000000014,
          "fever": 0.02883590000000003,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 0.989,
          "infection_load": 0.08384700000000003,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.04045120000000003,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 0.989,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.113626,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 18
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": true
        },
        "day": 3,
        "event_id": 11,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6112,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.083847
        },
        "illness_packet": {
          "delta": 0.083847,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.0,
          "recovered": false
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "monitor",
            "triage_score": 0.113626,
            "triaged": false
          },
          "day": 3,
          "fever": 0.02883590000000003,
          "infection_load": 0.08384700000000003,
          "quarantined": true,
          "replay_index": 11
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 18,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.003773,
          "fever": 0.028836
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.03896350000000008,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.972,
          "infection_load": 0.006565000000000279,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 3,
          "contagiousness": 0.029071560000000093,
          "energy": 1.0,
          "fatigue": 0.00311481000000001,
          "fever": 0.04412500000000006,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 0.869,
          "infection_load": 0.06921800000000022,
          "quarantined": false,
          "social_access": 0.9792346
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.203797,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 17
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.029072,
          "contained": true
        },
        "day": 4,
        "event_id": 12,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5632,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.006565
        },
        "illness_packet": {
          "delta": 0.079167,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.203797,
            "triaged": true
          },
          "day": 4,
          "fever": 0.03896350000000008,
          "infection_load": 0.006565000000000279,
          "quarantined": true,
          "replay_index": 12
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 17,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.038964
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.019845300000000038,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0037731150000000014,
          "fever": 0.02883590000000003,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 0.989,
          "infection_load": 0.08384700000000003,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.146121,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 16
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.0,
          "contained": false
        },
        "day": 4,
        "event_id": 13,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5512,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.026247,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "high",
            "triage_score": 0.146121,
            "triaged": true
          },
          "day": 4,
          "fever": 0.019845300000000038,
          "infection_load": 0.0,
          "quarantined": false,
          "replay_index": 13
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 16,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 1.0,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.019845
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.004253340000000021,
          "energy": 1.0,
          "fatigue": 0.0011325150000000021,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 0.945,
          "infection_load": 0.010127000000000051,
          "quarantined": false,
          "social_access": 0.9969619
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.015296700000000031,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 0.9289999999999999,
          "infection_load": 0.0,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.02545,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 16
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.004253,
          "contained": false
        },
        "day": 4,
        "event_id": 14,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5332,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.010127
        },
        "illness_packet": {
          "delta": 0.025167,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "monitor",
            "triage_score": 0.02545,
            "triaged": false
          },
          "day": 4,
          "fever": 0.0,
          "infection_load": 0.010127000000000051,
          "quarantined": false,
          "replay_index": 14
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 16,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.996962,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": false,
          "fatigue": 0.001133,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 4,
          "contagiousness": 0.014135940000000137,
          "energy": 1.0,
          "fatigue": 0.0021913650000000146,
          "fever": 0.02383320000000011,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 0.988,
          "infection_load": 0.033657000000000326,
          "quarantined": false,
          "social_access": 0.9899028999999999
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.03896350000000008,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 0.972,
          "infection_load": 0.006565000000000279,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.073078,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 16
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.014136,
          "contained": false
        },
        "day": 5,
        "event_id": 15,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6232,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.033657
        },
        "illness_packet": {
          "delta": 0.042132,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "monitor",
            "triage_score": 0.073078,
            "triaged": false
          },
          "day": 5,
          "fever": 0.02383320000000011,
          "infection_load": 0.033657000000000326,
          "quarantined": false,
          "replay_index": 15
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 16,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.989903,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": false,
          "fatigue": 0.002191,
          "fever": 0.023833
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 4,
          "contagiousness": 0.028691040000000008,
          "energy": 1.0,
          "fatigue": 0.003750840000000001,
          "fever": 0.008180500000000038,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.06831200000000003,
          "quarantined": false,
          "social_access": 0.9795064
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.019845300000000038,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.09247,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 16
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.028691,
          "contained": false
        },
        "day": 5,
        "event_id": 16,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6112,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.068312
        },
        "illness_packet": {
          "delta": 0.083352,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "monitor",
            "triage_score": 0.09247,
            "triaged": false
          },
          "day": 5,
          "fever": 0.008180500000000038,
          "infection_load": 0.06831200000000003,
          "quarantined": false,
          "replay_index": 16
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 16,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.979506,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.003751,
          "fever": 0.008181
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.032396280000000034,
          "energy": 1.0,
          "fatigue": 0.005280345000000007,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.9299999999999999,
          "immune_strength": 0.961,
          "infection_load": 0.07713400000000009,
          "quarantined": false,
          "social_access": 0.9768598
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.004253340000000021,
          "energy": 1.0,
          "fatigue": 0.0011325150000000021,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 0.945,
          "infection_load": 0.010127000000000051,
          "quarantined": false,
          "social_access": 0.9969619
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.107494,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 16
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.028143,
          "contained": false
        },
        "day": 5,
        "event_id": 17,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5932,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.077134
        },
        "illness_packet": {
          "delta": 0.082047,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "monitor",
            "triage_score": 0.107494,
            "triaged": false
          },
          "day": 5,
          "fever": 0.0,
          "infection_load": 0.07713400000000009,
          "quarantined": false,
          "replay_index": 17
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 16,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.97686,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.00528,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.016641000000000142,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 3,
          "contagiousness": 0.032396280000000034,
          "energy": 1.0,
          "fatigue": 0.005280345000000007,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.9299999999999999,
          "immune_strength": 0.961,
          "infection_load": 0.07713400000000009,
          "quarantined": false,
          "social_access": 0.9768598
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.189564,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.07,
          "remaining_doses": 15
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.032396,
          "contained": true
        },
        "day": 6,
        "event_id": 18,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5932,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.016641
        },
        "illness_packet": {
          "delta": 0.081327,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "high",
            "triage_score": 0.189564,
            "triaged": true
          },
          "day": 6,
          "fever": 0.0,
          "infection_load": 0.016641000000000142,
          "quarantined": true,
          "replay_index": 18
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 15,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 5,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.0033469000000000415,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.009844000000000061,
          "quarantined": true,
          "social_access": 0.34
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 4,
          "contagiousness": 0.028691040000000008,
          "energy": 1.0,
          "fatigue": 0.003750840000000001,
          "fever": 0.008180500000000038,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.06831200000000003,
          "quarantined": false,
          "social_access": 0.9795064
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.171655,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 14
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.028691,
          "contained": true
        },
        "day": 6,
        "event_id": 19,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6112,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.009844
        },
        "illness_packet": {
          "delta": 0.083352,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": true,
          "reason": "infection_load"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "high",
            "triage_score": 0.171655,
            "triaged": true
          },
          "day": 6,
          "fever": 0.0033469000000000415,
          "infection_load": 0.009844000000000061,
          "quarantined": true,
          "replay_index": 19
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 14,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.34,
          "modulated": true
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.003347
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 5,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.015840100000000145,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 4,
          "contagiousness": 0.014135940000000137,
          "energy": 1.0,
          "fatigue": 0.0021913650000000146,
          "fever": 0.02383320000000011,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 0.988,
          "infection_load": 0.033657000000000326,
          "quarantined": false,
          "social_access": 0.9899028999999999
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.151808,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 13
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.014136,
          "contained": false
        },
        "day": 6,
        "event_id": 20,
        "exposure_packet": {
          "bound": true,
          "risk": 0.6232,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5632000000000001,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.086412,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.151808,
            "triaged": true
          },
          "day": 6,
          "fever": 0.015840100000000145,
          "infection_load": 0.0,
          "quarantined": false,
          "replay_index": 20
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 13,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 1.0,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.01584
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 4,
          "contagiousness": 0.00990066000000008,
          "energy": 1.0,
          "fatigue": 0.0017375850000000085,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.02357300000000019,
          "quarantined": false,
          "social_access": 0.9929281
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 4,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.016641000000000142,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.039047,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 13
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.009901,
          "contained": false
        },
        "day": 7,
        "event_id": 21,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5332,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.023573
        },
        "illness_packet": {
          "delta": 0.021972,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "monitor",
            "triage_score": 0.039047,
            "triaged": false
          },
          "day": 7,
          "fever": 0.0,
          "infection_load": 0.02357300000000019,
          "quarantined": false,
          "replay_index": 21
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 13,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.992928,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": false,
          "fatigue": 0.001738,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 5,
          "contagiousness": 0.024457440000000014,
          "energy": 1.0,
          "fatigue": 0.003297240000000001,
          "fever": 0.003167300000000147,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.058232000000000034,
          "quarantined": false,
          "social_access": 0.9825304
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 5,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.015840100000000145,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.077264,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 13
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.024457,
          "contained": false
        },
        "day": 7,
        "event_id": 22,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5632,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.058232
        },
        "illness_packet": {
          "delta": 0.073272,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "monitor",
            "triage_score": 0.077264,
            "triaged": false
          },
          "day": 7,
          "fever": 0.003167300000000147,
          "infection_load": 0.058232000000000034,
          "quarantined": false,
          "replay_index": 22
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 13,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.98253,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.003297,
          "fever": 0.003167
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 5,
          "contagiousness": 0.008633520000000049,
          "energy": 1.0,
          "fatigue": 0.001601820000000005,
          "fever": 0.0,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.020556000000000116,
          "quarantined": false,
          "social_access": 0.9938332
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 5,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.0033469000000000415,
          "home": "moss_hollow",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.009844000000000061,
          "quarantined": true,
          "social_access": 0.34
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.035996,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 13
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.008634,
          "contained": false
        },
        "day": 7,
        "event_id": 23,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5512,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.020556
        },
        "illness_packet": {
          "delta": 0.025752,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "monitor",
            "triage_score": 0.035996,
            "triaged": false
          },
          "day": 7,
          "fever": 0.0,
          "infection_load": 0.020556000000000116,
          "quarantined": false,
          "replay_index": 23
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 13,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.993833,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": false,
          "fatigue": 0.001602,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Milo",
        "body_after": {
          "agent_id": "Milo",
          "care_received": 6,
          "contagiousness": 0.0,
          "energy": 1.0,
          "fatigue": 0.0,
          "fever": 0.0,
          "home": "stone_ridge",
          "hydration": 1.0,
          "immune_strength": 1.0,
          "infection_load": 0.0,
          "quarantined": false,
          "social_access": 1.0
        },
        "body_before": {
          "agent_id": "Milo",
          "care_received": 5,
          "contagiousness": 0.024457440000000014,
          "energy": 1.0,
          "fatigue": 0.003297240000000001,
          "fever": 0.003167300000000147,
          "home": "stone_ridge",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.058232000000000034,
          "quarantined": false,
          "social_access": 0.9825304
        },
        "care_packet": {
          "priority": "high",
          "triage_score": 0.147808,
          "triaged": true
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": true,
          "hydration_delta": 0.035,
          "remaining_doses": 12
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": -0.024457,
          "contained": false
        },
        "day": 8,
        "event_id": 24,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5632,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.0
        },
        "illness_packet": {
          "delta": 0.073272,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.103,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Milo",
          "care": {
            "priority": "high",
            "triage_score": 0.147808,
            "triaged": true
          },
          "day": 8,
          "fever": 0.0,
          "infection_load": 0.0,
          "quarantined": false,
          "replay_index": 24
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 12,
          "rested": true
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 1.0,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.0,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Ari",
        "body_after": {
          "agent_id": "Ari",
          "care_received": 4,
          "contagiousness": 0.0317121000000001,
          "energy": 1.0,
          "fatigue": 0.005812110000000019,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.9299999999999999,
          "immune_strength": 1.0,
          "infection_load": 0.07550500000000024,
          "quarantined": false,
          "social_access": 0.9773485
        },
        "body_before": {
          "agent_id": "Ari",
          "care_received": 4,
          "contagiousness": 0.00990066000000008,
          "energy": 1.0,
          "fatigue": 0.0017375850000000085,
          "fever": 0.0,
          "home": "hearth_vale",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.02357300000000019,
          "quarantined": false,
          "social_access": 0.9929281
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.105998,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 12
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.021811,
          "contained": false
        },
        "day": 8,
        "event_id": 25,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5332,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.075505
        },
        "illness_packet": {
          "delta": 0.066972,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Ari",
          "care": {
            "priority": "monitor",
            "triage_score": 0.105998,
            "triaged": false
          },
          "day": 8,
          "fever": 0.0,
          "infection_load": 0.07550500000000024,
          "quarantined": false,
          "replay_index": 25
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 12,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.977348,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.005812,
          "fever": 0.0
        }
      },
      {
        "agent_id": "Fay",
        "body_after": {
          "agent_id": "Fay",
          "care_received": 5,
          "contagiousness": 0.03203256000000007,
          "energy": 1.0,
          "fatigue": 0.005710680000000013,
          "fever": 0.0,
          "home": "moss_hollow",
          "hydration": 0.9299999999999999,
          "immune_strength": 1.0,
          "infection_load": 0.07626800000000017,
          "quarantined": false,
          "social_access": 0.9771196
        },
        "body_before": {
          "agent_id": "Fay",
          "care_received": 5,
          "contagiousness": 0.008633520000000049,
          "energy": 1.0,
          "fatigue": 0.001601820000000005,
          "fever": 0.0,
          "home": "moss_hollow",
          "hydration": 0.965,
          "immune_strength": 1.0,
          "infection_load": 0.020556000000000116,
          "quarantined": false,
          "social_access": 0.9938332
        },
        "care_packet": {
          "priority": "monitor",
          "triage_score": 0.106736,
          "triaged": false
        },
        "claim_boundary": {
          "complete_3d_world": false,
          "complete_playable_world": false,
          "moral_patienthood": false,
          "subjective_consciousness": false,
          "subjective_illness": false
        },
        "clean_water_packet": {
          "given": false,
          "hydration_delta": -0.035,
          "remaining_doses": 12
        },
        "condition": "integrated_embodied_illness_immune_care_quarantine",
        "containment_packet": {
          "contagion_delta": 0.023399,
          "contained": false
        },
        "day": 8,
        "event_id": 26,
        "exposure_packet": {
          "bound": true,
          "risk": 0.5512,
          "sources": {
            "food_risk": 0.39000000000000024,
            "sleep_risk": 0.5900000000000003,
            "total": 0.5032000000000002,
            "waste_risk": 0.11499999999999996,
            "water_risk": 0.7200000000000002
          }
        },
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "health_guardrail_packet": {
          "bounded": true,
          "max_infection": 0.076268
        },
        "illness_packet": {
          "delta": 0.070752,
          "progressed": true
        },
        "immune_packet": {
          "immune_delta": 0.016,
          "recovered": true
        },
        "private_health_hidden": true,
        "quarantine_packet": {
          "chosen": false,
          "reason": "none"
        },
        "replay_frame": {
          "agent_id": "Fay",
          "care": {
            "priority": "monitor",
            "triage_score": 0.106736,
            "triaged": false
          },
          "day": 8,
          "fever": 0.0,
          "infection_load": 0.07626800000000017,
          "quarantined": false,
          "replay_index": 26
        },
        "rest_packet": {
          "energy_delta": 0.0,
          "remaining_slots": 12,
          "rested": false
        },
        "sanitation_feedback_packet": {
          "bound": true,
          "risk_source": "ecology_nodes",
          "waste_risk": 0.115,
          "water_risk": 0.72
        },
        "social_access_packet": {
          "access": 0.97712,
          "modulated": false
        },
        "symptom_packet": {
          "expressed": true,
          "fatigue": 0.005711,
          "fever": 0.0
        }
      }
    ],
    "health_kernel": {
      "care_water_doses_remaining": 12,
      "not_subjective_illness": true,
      "rest_slots_remaining": 12
    },
    "replay": [
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.592351,
          "triaged": true
        },
        "day": 0,
        "fever": 0.05530720000000001,
        "infection_load": 0.21125200000000008,
        "quarantined": true,
        "replay_index": 0
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "high",
          "triage_score": 0.5391,
          "triaged": true
        },
        "day": 0,
        "fever": 0.0505152,
        "infection_load": 0.16333200000000006,
        "quarantined": true,
        "replay_index": 1
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "high",
          "triage_score": 0.471225,
          "triaged": true
        },
        "day": 0,
        "fever": 0.04440720000000001,
        "infection_load": 0.10225200000000009,
        "quarantined": true,
        "replay_index": 2
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.395302,
          "triaged": true
        },
        "day": 1,
        "fever": 0.06077610000000002,
        "infection_load": 0.11286900000000014,
        "quarantined": true,
        "replay_index": 3
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "high",
          "triage_score": 0.327919,
          "triaged": true
        },
        "day": 1,
        "fever": 0.05040010000000001,
        "infection_load": 0.057029000000000135,
        "quarantined": true,
        "replay_index": 4
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "high",
          "triage_score": 0.252049,
          "triaged": true
        },
        "day": 1,
        "fever": 0.03807610000000002,
        "infection_load": 0.0,
        "quarantined": true,
        "replay_index": 5
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.223322,
          "triaged": true
        },
        "day": 2,
        "fever": 0.05720320000000004,
        "infection_load": 0.02245100000000018,
        "quarantined": true,
        "replay_index": 6
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "high",
          "triage_score": 0.142093,
          "triaged": true
        },
        "day": 2,
        "fever": 0.04045120000000003,
        "infection_load": 0.0,
        "quarantined": false,
        "replay_index": 7
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "monitor",
          "triage_score": 0.065195,
          "triaged": false
        },
        "day": 2,
        "fever": 0.022316300000000025,
        "infection_load": 0.04240200000000004,
        "quarantined": false,
        "replay_index": 8
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "monitor",
          "triage_score": 0.114122,
          "triaged": false
        },
        "day": 3,
        "fever": 0.04412500000000006,
        "infection_load": 0.06921800000000022,
        "quarantined": false,
        "replay_index": 9
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "high",
          "triage_score": 0.161038,
          "triaged": true
        },
        "day": 3,
        "fever": 0.015296700000000031,
        "infection_load": 0.0,
        "quarantined": true,
        "replay_index": 10
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "monitor",
          "triage_score": 0.113626,
          "triaged": false
        },
        "day": 3,
        "fever": 0.02883590000000003,
        "infection_load": 0.08384700000000003,
        "quarantined": true,
        "replay_index": 11
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.203797,
          "triaged": true
        },
        "day": 4,
        "fever": 0.03896350000000008,
        "infection_load": 0.006565000000000279,
        "quarantined": true,
        "replay_index": 12
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "high",
          "triage_score": 0.146121,
          "triaged": true
        },
        "day": 4,
        "fever": 0.019845300000000038,
        "infection_load": 0.0,
        "quarantined": false,
        "replay_index": 13
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "monitor",
          "triage_score": 0.02545,
          "triaged": false
        },
        "day": 4,
        "fever": 0.0,
        "infection_load": 0.010127000000000051,
        "quarantined": false,
        "replay_index": 14
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "monitor",
          "triage_score": 0.073078,
          "triaged": false
        },
        "day": 5,
        "fever": 0.02383320000000011,
        "infection_load": 0.033657000000000326,
        "quarantined": false,
        "replay_index": 15
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "monitor",
          "triage_score": 0.09247,
          "triaged": false
        },
        "day": 5,
        "fever": 0.008180500000000038,
        "infection_load": 0.06831200000000003,
        "quarantined": false,
        "replay_index": 16
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "monitor",
          "triage_score": 0.107494,
          "triaged": false
        },
        "day": 5,
        "fever": 0.0,
        "infection_load": 0.07713400000000009,
        "quarantined": false,
        "replay_index": 17
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "high",
          "triage_score": 0.189564,
          "triaged": true
        },
        "day": 6,
        "fever": 0.0,
        "infection_load": 0.016641000000000142,
        "quarantined": true,
        "replay_index": 18
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "high",
          "triage_score": 0.171655,
          "triaged": true
        },
        "day": 6,
        "fever": 0.0033469000000000415,
        "infection_load": 0.009844000000000061,
        "quarantined": true,
        "replay_index": 19
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.151808,
          "triaged": true
        },
        "day": 6,
        "fever": 0.015840100000000145,
        "infection_load": 0.0,
        "quarantined": false,
        "replay_index": 20
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "monitor",
          "triage_score": 0.039047,
          "triaged": false
        },
        "day": 7,
        "fever": 0.0,
        "infection_load": 0.02357300000000019,
        "quarantined": false,
        "replay_index": 21
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "monitor",
          "triage_score": 0.077264,
          "triaged": false
        },
        "day": 7,
        "fever": 0.003167300000000147,
        "infection_load": 0.058232000000000034,
        "quarantined": false,
        "replay_index": 22
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "monitor",
          "triage_score": 0.035996,
          "triaged": false
        },
        "day": 7,
        "fever": 0.0,
        "infection_load": 0.020556000000000116,
        "quarantined": false,
        "replay_index": 23
      },
      {
        "agent_id": "Milo",
        "care": {
          "priority": "high",
          "triage_score": 0.147808,
          "triaged": true
        },
        "day": 8,
        "fever": 0.0,
        "infection_load": 0.0,
        "quarantined": false,
        "replay_index": 24
      },
      {
        "agent_id": "Ari",
        "care": {
          "priority": "monitor",
          "triage_score": 0.105998,
          "triaged": false
        },
        "day": 8,
        "fever": 0.0,
        "infection_load": 0.07550500000000024,
        "quarantined": false,
        "replay_index": 25
      },
      {
        "agent_id": "Fay",
        "care": {
          "priority": "monitor",
          "triage_score": 0.106736,
          "triaged": false
        },
        "day": 8,
        "fever": 0.0,
        "infection_load": 0.07626800000000017,
        "quarantined": false,
        "replay_index": 26
      }
    ],
    "source_condition": "integrated_ecological_regeneration_spoilage_waste_sanitation"
  },
  "moral_boundary": {
    "care_triage_policy_not_moral_patienthood": true,
    "functional_health_seed_not_complete_gameplay": true,
    "infection_load_not_subjective_illness": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "quarantine_not_social_punishment": true
  },
  "source_condition": "integrated_ecological_regeneration_spoilage_waste_sanitation",
  "trace_events": 27
};
