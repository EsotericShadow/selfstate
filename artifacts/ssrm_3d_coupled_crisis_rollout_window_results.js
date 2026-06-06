window.SSRM_3D_COUPLED_CRISIS_ENVIRONMENT_BOTTLENECK_RESULTS = {
  "config": {
    "train_seeds": [
      20260911,
      20260912,
      20260913,
      20260914,
      20260915,
      20260916
    ],
    "tune_seeds": [
      20261011,
      20261012,
      20261013
    ],
    "eval_seeds": [
      20261021,
      20261022,
      20261023,
      20261024,
      20261025
    ],
    "hours": 72.0,
    "step_hours": 0.1,
    "population": 14,
    "epochs": 42,
    "hidden_size": 64,
    "plan_epochs": 72,
    "plan_hidden_size": 72,
    "plan_bias_candidates": [
      0.0,
      1.0,
      1.75,
      2.75,
      4.0,
      5.5,
      7.0,
      9.0,
      11.0
    ],
    "max_plan_examples": 48000,
    "device": "auto",
    "trace_seed": 20261021
  },
  "crisis_profiles": [
    {
      "name": "contaminated_water_trust",
      "env_actions": [
        "sanitize",
        "treat"
      ],
      "social_actions": [
        "social_repair",
        "teach"
      ],
      "env_need": 0.92,
      "social_need": 0.7,
      "contamination_rate": 0.036,
      "disease_rate": 0.03,
      "conflict_rate": 0.016,
      "trust_loss_rate": 0.016,
      "route_rate": 0.0,
      "predator_rate": 0.0,
      "migration_rate": 0.0,
      "water_loss_rate": 0.014,
      "food_loss_rate": 0.0,
      "shelter_loss_rate": 0.0,
      "visibility_loss_rate": 0.0
    },
    {
      "name": "route_migration_dispute",
      "env_actions": [
        "scout",
        "harvest_food",
        "collect_water"
      ],
      "social_actions": [
        "social_repair",
        "teach"
      ],
      "env_need": 0.98,
      "social_need": 0.72,
      "contamination_rate": 0.0,
      "disease_rate": 0.0,
      "conflict_rate": 0.02,
      "trust_loss_rate": 0.0,
      "route_rate": 0.034,
      "predator_rate": 0.02,
      "migration_rate": 0.04,
      "water_loss_rate": 0.01,
      "food_loss_rate": 0.014,
      "shelter_loss_rate": 0.0,
      "visibility_loss_rate": 0.0
    },
    {
      "name": "storm_shelter_coordination",
      "env_actions": [
        "construct",
        "scout"
      ],
      "social_actions": [
        "social_repair",
        "teach"
      ],
      "env_need": 1.04,
      "social_need": 0.76,
      "contamination_rate": 0.0,
      "disease_rate": 0.0,
      "conflict_rate": 0.018,
      "trust_loss_rate": 0.012,
      "route_rate": 0.018,
      "predator_rate": 0.0,
      "migration_rate": 0.0,
      "water_loss_rate": 0.0,
      "food_loss_rate": 0.0,
      "shelter_loss_rate": 0.034,
      "visibility_loss_rate": 0.032
    },
    {
      "name": "quarantine_rumor",
      "env_actions": [
        "sanitize",
        "treat"
      ],
      "social_actions": [
        "social_repair",
        "teach",
        "learn"
      ],
      "env_need": 0.9,
      "social_need": 0.92,
      "contamination_rate": 0.022,
      "disease_rate": 0.032,
      "conflict_rate": 0.038,
      "trust_loss_rate": 0.03,
      "route_rate": 0.0,
      "predator_rate": 0.0,
      "migration_rate": 0.0,
      "water_loss_rate": 0.0,
      "food_loss_rate": 0.0,
      "shelter_loss_rate": 0.0,
      "visibility_loss_rate": 0.0
    }
  ],
  "routers": [
    {
      "name": "none",
      "social_bias": 0.0,
      "environment_bias": 0.0,
      "infrastructure_bias": 0.0,
      "tool_bias": 0.0,
      "teaching_bias": 0.0
    },
    {
      "name": "balanced",
      "social_bias": 1.0,
      "environment_bias": 1.0,
      "infrastructure_bias": 1.0,
      "tool_bias": 1.0,
      "teaching_bias": 1.0
    },
    {
      "name": "social_env",
      "social_bias": 1.55,
      "environment_bias": 1.45,
      "infrastructure_bias": 0.75,
      "tool_bias": 0.7,
      "teaching_bias": 1.2
    },
    {
      "name": "environment_first",
      "social_bias": 0.55,
      "environment_bias": 2.0,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.65,
      "teaching_bias": 0.55
    },
    {
      "name": "social_first",
      "social_bias": 2.0,
      "environment_bias": 0.55,
      "infrastructure_bias": 0.6,
      "tool_bias": 0.6,
      "teaching_bias": 1.35
    },
    {
      "name": "build_tool",
      "social_bias": 0.45,
      "environment_bias": 0.7,
      "infrastructure_bias": 1.65,
      "tool_bias": 1.7,
      "teaching_bias": 0.55
    },
    {
      "name": "teaching_tradition",
      "social_bias": 1.1,
      "environment_bias": 0.75,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.7,
      "teaching_bias": 2.0
    },
    {
      "name": "high_pressure",
      "social_bias": 1.8,
      "environment_bias": 1.6,
      "infrastructure_bias": 1.3,
      "tool_bias": 1.25,
      "teaching_bias": 1.5
    }
  ],
  "plans": [
    {
      "name": "balanced_repair",
      "env_weight": 0.66,
      "social_weight": 0.66,
      "sustain_weight": 0.08,
      "tool_weight": 0.05,
      "infrastructure_weight": 0.08,
      "teaching_weight": 0.2,
      "horizon_hours": 1.8
    },
    {
      "name": "environment_first",
      "env_weight": 0.92,
      "social_weight": 0.28,
      "sustain_weight": 0.06,
      "tool_weight": 0.06,
      "infrastructure_weight": 0.16,
      "teaching_weight": 0.06,
      "horizon_hours": 1.6
    },
    {
      "name": "social_first",
      "env_weight": 0.3,
      "social_weight": 0.92,
      "sustain_weight": 0.06,
      "tool_weight": 0.04,
      "infrastructure_weight": 0.05,
      "teaching_weight": 0.36,
      "horizon_hours": 1.6
    },
    {
      "name": "sanitize_care_window",
      "env_weight": 0.84,
      "social_weight": 0.52,
      "sustain_weight": 0.1,
      "tool_weight": 0.04,
      "infrastructure_weight": 0.03,
      "teaching_weight": 0.16,
      "horizon_hours": 1.9
    },
    {
      "name": "route_supply_window",
      "env_weight": 0.76,
      "social_weight": 0.36,
      "sustain_weight": 0.28,
      "tool_weight": 0.1,
      "infrastructure_weight": 0.08,
      "teaching_weight": 0.08,
      "horizon_hours": 1.8
    },
    {
      "name": "storm_infrastructure_window",
      "env_weight": 0.8,
      "social_weight": 0.38,
      "sustain_weight": 0.12,
      "tool_weight": 0.08,
      "infrastructure_weight": 0.5,
      "teaching_weight": 0.08,
      "horizon_hours": 2.0
    },
    {
      "name": "teaching_repair_window",
      "env_weight": 0.38,
      "social_weight": 0.86,
      "sustain_weight": 0.06,
      "tool_weight": 0.05,
      "infrastructure_weight": 0.04,
      "teaching_weight": 0.52,
      "horizon_hours": 1.8
    },
    {
      "name": "recovery_sustain_window",
      "env_weight": 0.42,
      "social_weight": 0.42,
      "sustain_weight": 0.58,
      "tool_weight": 0.24,
      "infrastructure_weight": 0.2,
      "teaching_weight": 0.16,
      "horizon_hours": 2.2
    }
  ],
  "router_selection": [
    {
      "router": "none",
      "social_bias": 0.0,
      "environment_bias": 0.0,
      "infrastructure_bias": 0.0,
      "tool_bias": 0.0,
      "teaching_bias": 0.0,
      "tune_total_score": 0.5174540799999999,
      "tune_maturation_score": 0.9951039999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.1462280213375575,
      "selection_objective": 0.2882084757324884,
      "selected": false
    },
    {
      "router": "balanced",
      "social_bias": 1.0,
      "environment_bias": 1.0,
      "infrastructure_bias": 1.0,
      "tool_bias": 1.0,
      "teaching_bias": 1.0,
      "tune_total_score": 0.5185909245122988,
      "tune_maturation_score": 0.9972902394467286,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.013888888888888888,
      "tune_damage": 1.0979721243308889,
      "selection_objective": 0.30420483297945444,
      "selected": false
    },
    {
      "router": "social_env",
      "social_bias": 1.55,
      "environment_bias": 1.45,
      "infrastructure_bias": 0.75,
      "tool_bias": 0.7,
      "teaching_bias": 1.2,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.007478632478632479,
      "tune_damage": 1.0528463163647603,
      "selection_objective": 0.31307764852191977,
      "selected": false
    },
    {
      "router": "environment_first",
      "social_bias": 0.55,
      "environment_bias": 2.0,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.65,
      "teaching_bias": 0.55,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.007478632478632479,
      "tune_damage": 1.0510386254618906,
      "selection_objective": 0.3134391867024937,
      "selected": false
    },
    {
      "router": "social_first",
      "social_bias": 2.0,
      "environment_bias": 0.55,
      "infrastructure_bias": 0.6,
      "tool_bias": 0.6,
      "teaching_bias": 1.35,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.022435897435897436,
      "tune_damage": 1.042795133177876,
      "selection_objective": 0.3157609620823736,
      "selected": true
    },
    {
      "router": "build_tool",
      "social_bias": 0.45,
      "environment_bias": 0.7,
      "infrastructure_bias": 1.65,
      "tool_bias": 1.7,
      "teaching_bias": 0.55,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.016025641025641028,
      "tune_damage": 1.113328145481561,
      "selection_objective": 0.29678256474984177,
      "selected": false
    },
    {
      "router": "teaching_tradition",
      "social_bias": 1.1,
      "environment_bias": 0.75,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.7,
      "teaching_bias": 2.0,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.010683760683760682,
      "tune_damage": 1.0528066744944313,
      "selection_objective": 0.31322980766521635,
      "selected": false
    },
    {
      "router": "high_pressure",
      "social_bias": 1.8,
      "environment_bias": 1.6,
      "infrastructure_bias": 1.3,
      "tool_bias": 1.25,
      "teaching_bias": 1.5,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.013888888888888888,
      "tune_damage": 1.078529311954724,
      "selection_objective": 0.3082295109423886,
      "selected": false
    }
  ],
  "plan_selection": [
    {
      "plan_bias": 0.0,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.016025641025641028,
      "tune_damage": 1.3790173385172657,
      "selection_objective": -0.014218068426974595,
      "selected": true
    },
    {
      "plan_bias": 1.0,
      "tune_total_score": 0.5070278720763486,
      "tune_maturation_score": 0.9750536001468241,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.021367521367521364,
      "tune_damage": 1.716013755909895,
      "selection_objective": -0.12110256503747319,
      "selected": false
    },
    {
      "plan_bias": 1.75,
      "tune_total_score": 0.5134343955607094,
      "tune_maturation_score": 0.9873738376167487,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.02777777777777778,
      "tune_damage": 1.698472041320499,
      "selection_objective": -0.10847086883698648,
      "selected": false
    },
    {
      "plan_bias": 2.75,
      "tune_total_score": 0.5135553576546349,
      "tune_maturation_score": 0.9876064570281439,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.02884615384615385,
      "tune_damage": 1.7008894965555823,
      "selection_objective": -0.10863066271099431,
      "selected": false
    },
    {
      "plan_bias": 4.0,
      "tune_total_score": 0.5136852738314136,
      "tune_maturation_score": 0.9878562958296414,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.02991452991452992,
      "tune_damage": 1.6604751368469248,
      "selection_objective": -0.09593464424388276,
      "selected": false
    },
    {
      "plan_bias": 5.5,
      "tune_total_score": 0.5134178140946736,
      "tune_maturation_score": 0.9873419501820645,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.035256410256410256,
      "tune_damage": 1.5884334236439805,
      "selection_objective": -0.07210550594487136,
      "selected": false
    },
    {
      "plan_bias": 7.0,
      "tune_total_score": 0.5128822238467848,
      "tune_maturation_score": 0.9863119689361245,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.030982905982905984,
      "tune_damage": 1.589137498639378,
      "selection_objective": -0.07461471854008966,
      "selected": false
    },
    {
      "plan_bias": 9.0,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.03739316239316239,
      "tune_damage": 1.535769029347683,
      "selection_objective": -0.0507371190607151,
      "selected": false
    },
    {
      "plan_bias": 11.0,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.16666666666666666,
      "tune_coupled_response": 0.04594017094017094,
      "tune_damage": 1.5264443908881742,
      "selection_objective": -0.014926907010042012,
      "selected": false
    }
  ],
  "base_training": [
    {
      "architecture": "frame_mlp",
      "train_loss": 1.8162533044815063,
      "train_accuracy": 0.25658294153359595,
      "device_used": "mps",
      "parameter_count": 9932,
      "train_sequences": 105,
      "train_steps": 70827
    },
    {
      "architecture": "gru",
      "train_loss": 1.7891311645507812,
      "train_accuracy": 0.2634729693478476,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_sequences": 105,
      "train_steps": 70827
    }
  ],
  "plan_training": {
    "train_loss": 0.04499490186572075,
    "pairwise_accuracy": 0.5239999890327454,
    "device_used": "mps",
    "parameter_count": 11953,
    "train_examples": 9248,
    "positive_examples": 8776,
    "plan_epochs": 72,
    "plan_hidden_size": 72
  },
  "summary": [
    {
      "controller": "designed",
      "ablation": "none",
      "mean_total_score": 0.7732349188006651,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.5275727475013856,
      "mean_resolved_rate": 1.0,
      "mean_env_response_rate": 0.07692307692307693,
      "mean_social_response_rate": 0.9230769230769231,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 0.03550643571032692,
      "mean_final_alive": 16.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.6,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "frame_mlp",
      "ablation": "none",
      "mean_total_score": 0.32986810374413483,
      "mean_maturation_score": 0.63436173796949,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.25,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.8765732459322357,
      "mean_final_alive": 14.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "gru",
      "ablation": "none",
      "mean_total_score": 0.5192362239999999,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 0.25,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.2649199334987213,
      "mean_final_alive": 15.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.6,
      "mean_architecture_tier": 3.4,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "reactive",
      "ablation": "none",
      "mean_total_score": 0.24007509448982875,
      "mean_maturation_score": 0.4616828740189014,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.11730769230769231,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.8788575588279564,
      "mean_final_alive": 14.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.0,
      "mean_architecture_tier": 0.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "repair_critic_baseline",
      "ablation": "none",
      "mean_total_score": 0.518472448,
      "mean_maturation_score": 0.9970623999999999,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.1,
      "mean_env_response_rate": 0.1794871794871795,
      "mean_social_response_rate": 0.2551282051282051,
      "mean_coupled_response_rate": 0.029487179487179487,
      "mean_crisis_damage": 1.3038520830534956,
      "mean_final_alive": 15.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "return_selected_gru",
      "ablation": "none",
      "mean_total_score": 0.518472448,
      "mean_maturation_score": 0.9970623999999999,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.1,
      "mean_env_response_rate": 0.1794871794871795,
      "mean_social_response_rate": 0.2551282051282051,
      "mean_coupled_response_rate": 0.029487179487179487,
      "mean_crisis_damage": 1.3038520830534956,
      "mean_final_alive": 15.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "body",
      "mean_total_score": 0.517708672,
      "mean_maturation_score": 0.9955936,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.05,
      "mean_env_response_rate": 0.16282051282051282,
      "mean_social_response_rate": 0.3243589743589744,
      "mean_coupled_response_rate": 0.009615384615384616,
      "mean_crisis_damage": 1.3676080517110656,
      "mean_final_alive": 15.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.2,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "environment",
      "mean_total_score": 0.5169283433622353,
      "mean_maturation_score": 0.9940929680042985,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.05,
      "mean_env_response_rate": 0.12692307692307692,
      "mean_social_response_rate": 0.16025641025641027,
      "mean_coupled_response_rate": 0.011538461538461539,
      "mean_crisis_damage": 1.3777076880811656,
      "mean_final_alive": 15.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.8,
      "mean_architecture_tier": 3.2,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.3306328576039062,
      "mean_maturation_score": 0.6358324184690504,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.25,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.8763445057162182,
      "mean_final_alive": 14.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "none",
      "mean_total_score": 0.518472448,
      "mean_maturation_score": 0.9970623999999999,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.1,
      "mean_env_response_rate": 0.08012820512820513,
      "mean_social_response_rate": 0.23397435897435898,
      "mean_coupled_response_rate": 0.030128205128205132,
      "mean_crisis_damage": 1.3020555960295606,
      "mean_final_alive": 15.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.0,
      "mean_architecture_tier": 3.4,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.15,
      "mean_env_response_rate": 0.10705128205128205,
      "mean_social_response_rate": 0.38974358974358975,
      "mean_coupled_response_rate": 0.035897435897435895,
      "mean_crisis_damage": 1.1354758435970156,
      "mean_final_alive": 16.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
      "mean_architecture_tier": 3.8,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.5172952761175487,
      "mean_maturation_score": 0.9947986079183628,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 0.11987179487179486,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.2265049627946358,
      "mean_final_alive": 16.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "rollout_window_gru",
      "ablation": "tools",
      "mean_total_score": 0.516056703139444,
      "mean_maturation_score": 0.992416736806623,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.05,
      "mean_env_response_rate": 0.23846153846153845,
      "mean_social_response_rate": 0.12435897435897436,
      "mean_coupled_response_rate": 0.004487179487179487,
      "mean_crisis_damage": 1.7431531287617807,
      "mean_final_alive": 15.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    }
  ],
  "ablations": [
    {
      "ablation": "body",
      "mean_total_score": 0.517708672,
      "total_loss": 0.0007637759999999938,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.05,
      "env_response_loss": -0.08269230769230769,
      "social_response_loss": -0.0903846153846154,
      "coupled_response_loss": 0.020512820512820516,
      "damage_increase": 0.06555245568150503
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.3306328576039062,
      "total_loss": 0.18783959039609383,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.1,
      "env_response_loss": -0.16987179487179488,
      "social_response_loss": 0.23397435897435898,
      "coupled_response_loss": 0.030128205128205132,
      "damage_increase": 0.5742889096866577
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.516056703139444,
      "total_loss": 0.0024157448605560683,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.05,
      "env_response_loss": -0.15833333333333333,
      "social_response_loss": 0.10961538461538461,
      "coupled_response_loss": 0.025641025641025647,
      "damage_increase": 0.4410975327322202
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.5172952761175487,
      "total_loss": 0.0011771718824513666,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.1,
      "env_response_loss": 0.08012820512820513,
      "social_response_loss": 0.11410256410256411,
      "coupled_response_loss": 0.030128205128205132,
      "damage_increase": -0.07555063323492472
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.5169283433622353,
      "total_loss": 0.001544104637764776,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.05,
      "env_response_loss": -0.04679487179487178,
      "social_response_loss": 0.0737179487179487,
      "coupled_response_loss": 0.018589743589743593,
      "damage_increase": 0.07565209205160506
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.52,
      "total_loss": -0.0015275519999999876,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": -0.04999999999999999,
      "env_response_loss": -0.02692307692307691,
      "social_response_loss": -0.15576923076923077,
      "coupled_response_loss": -0.005769230769230763,
      "damage_increase": -0.16657975243254497
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_plan_bias": 0.0,
    "rollout_window_total_score": 0.518472448,
    "repair_critic_total_score": 0.518472448,
    "return_selected_total_score": 0.518472448,
    "base_gru_total_score": 0.5192362239999999,
    "designed_total_score": 0.7732349188006651,
    "frame_total_score": 0.32986810374413483,
    "reactive_total_score": 0.24007509448982875,
    "gain_over_repair_critic": 0.0,
    "gain_over_return_selected": 0.0,
    "gain_over_base_gru": -0.0007637759999998828,
    "gain_over_frame": 0.1886043442558652,
    "gain_over_reactive": 0.27839735351017125,
    "gap_to_designed": 0.25476247080066505,
    "rollout_window_crisis_score": 0.0,
    "return_selected_crisis_score": 0.0,
    "rollout_window_resolved_rate": 0.1,
    "return_selected_resolved_rate": 0.1,
    "rollout_window_coupled_response": 0.030128205128205132,
    "return_selected_coupled_response": 0.029487179487179487,
    "social_culture_total_loss": 0.0011771718824513666,
    "environment_total_loss": 0.001544104637764776,
    "social_culture_crisis_loss": 0.0,
    "environment_crisis_loss": 0.0,
    "social_culture_coupled_loss": 0.030128205128205132,
    "environment_coupled_loss": 0.018589743589743593,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "supports_rollout_window_selection": false,
    "supports_social_environment_dependency": false,
    "verdict": "partial_or_failed"
  },
  "trace": {
    "seed": 20261021,
    "condition": "rollout_window_gru:social_first:bias_0:none",
    "frames": [
      {
        "label": "0h",
        "hours": 0.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 0,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 0.7722728211182229,
        "water": 0.7464664022867248,
        "materials": 0.5407283081901255,
        "medicine": 0.36,
        "shelter": 0.4711839061853737,
        "architecture": 0.12,
        "architecture_tier": 0,
        "tools": 0.32,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.14,
        "granary": 0.12,
        "paths": 0.1,
        "sanitation": 0.12,
        "garden": 0.22,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.07,
        "map_knowledge": 0.1,
        "contamination": 0.18000000000000002,
        "disease": 0.1,
        "predators": 0.12,
        "route_hazard": 0.2,
        "resource_migration": 0.18,
        "adaptive_pressure": 0.1,
        "pressure_integral": 0.0,
        "adaptation_evidence": 0.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.12447535805763103,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.7650592184385666,
        "mean_age": 32.39970636302022,
        "actions": {
          "idle": 14
        },
        "events": []
      },
      {
        "label": "3h",
        "hours": 3.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 0,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 0.741801429157692,
        "water": 0.676167943430624,
        "materials": 0.3110849056789635,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.6614636875476236,
        "architecture_tier": 2,
        "tools": 0.26497999999999994,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.6003096322987884,
        "granary": 0.5369306098799599,
        "paths": 0.5181355207337227,
        "sanitation": 0.12,
        "garden": 0.5129243114628655,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.12130956466669023,
        "map_knowledge": 0.19247992152572901,
        "contamination": 0.15233305080708046,
        "disease": 0.06366153767877374,
        "predators": 0.10309867532618294,
        "route_hazard": 0.0835338420239956,
        "resource_migration": 0.23227163366236703,
        "adaptive_pressure": 0.12878693229115257,
        "pressure_integral": 0.006129019697934978,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.1280080730794154,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.7183826059721509,
        "mean_age": 35.399706363020265,
        "actions": {
          "construct": 14
        },
        "events": [],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.0
      },
      {
        "label": "6h",
        "hours": 6.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 0,
        "next_shock": 172.0,
        "weather": "hot",
        "food": 0.810228633442802,
        "water": 0.6950896080986901,
        "materials": 0.07887768214203202,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.22370175141418933,
        "tool_tier": 1,
        "workshop": 0.11116230661035625,
        "waterworks": 1.0,
        "granary": 0.9784246888061366,
        "paths": 0.9605122457334577,
        "sanitation": 0.12,
        "garden": 0.8226872286453453,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.12052974969581982,
        "map_knowledge": 0.19069231929987762,
        "contamination": 0.06954651364785658,
        "disease": 0.023256531211981443,
        "predators": 0.05867765095234502,
        "route_hazard": 0.007699223493658817,
        "resource_migration": 0.2516588814386459,
        "adaptive_pressure": 0.1037380274148932,
        "pressure_integral": 0.010232377929743589,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.131482504902062,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.6738026059721511,
        "mean_age": 38.39970636302031,
        "actions": {
          "construct": 8,
          "improve_tools": 6
        },
        "events": [],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.0
      },
      {
        "label": "9h",
        "hours": 9.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 0,
        "next_shock": 172.0,
        "weather": "hot",
        "food": 0.9294351217440391,
        "water": 0.7538059759065334,
        "materials": 0.0009800627850760563,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9971077644693338,
        "architecture_tier": 4,
        "tools": 0.8441783894605625,
        "tool_tier": 4,
        "workshop": 0.6386394529124634,
        "waterworks": 1.0,
        "granary": 0.9922821272130606,
        "paths": 0.9745331963445804,
        "sanitation": 0.12,
        "garden": 0.8325290104609683,
        "culture": 0.4038478947565145,
        "symbols": 0.2983345906574829,
        "risk_memory": 0.3293940103535668,
        "map_knowledge": 0.18857738836095447,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2391049940149158,
        "adaptive_pressure": 0.09529032667715959,
        "pressure_integral": 0.014357710515232457,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.32474523393670846,
        "mean_wisdom": 0.15786096867678406,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.6292226059721516,
        "mean_age": 41.39970636302035,
        "actions": {
          "teach": 14
        },
        "events": [],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.0
      },
      {
        "label": "12h",
        "hours": 12.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 0,
        "next_shock": 172.0,
        "weather": "hot",
        "food": 1.0,
        "water": 0.8131331115661351,
        "materials": 0.005849396618955124,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9935809506715152,
        "architecture_tier": 4,
        "tools": 0.8231783894605614,
        "tool_tier": 4,
        "workshop": 0.6386394529124634,
        "waterworks": 1.0,
        "granary": 0.9922821272130606,
        "paths": 0.9745583491561834,
        "sanitation": 0.12,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.18693974812746425,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.18421595900809234,
        "adaptive_pressure": 0.05417143428130734,
        "pressure_integral": 0.01642169699075101,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.25424236613309775,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.584642605972152,
        "mean_age": 44.3997063630204,
        "actions": {
          "teach": 14
        },
        "events": [],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.0
      },
      {
        "label": "18h",
        "hours": 18.0,
        "alive": 14,
        "total_agents": 14,
        "children": 0,
        "births": 0,
        "deaths": 0,
        "major_shocks": 1,
        "next_shock": 172.0,
        "weather": "hot",
        "food": 1.0,
        "water": 0.8929162895388867,
        "materials": 0.015426268247575023,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9863374440798642,
        "architecture_tier": 4,
        "tools": 0.7811783894605594,
        "tool_tier": 4,
        "workshop": 0.6386394529124634,
        "waterworks": 1.0,
        "granary": 0.9922821272130606,
        "paths": 0.9744551178059494,
        "sanitation": 0.12,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.1833173635810029,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.11258617956331944,
        "adaptive_pressure": 0.0542828337935396,
        "pressure_integral": 0.02096746722310159,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.45177875618347857,
        "mean_health": 0.9121575065775452,
        "mean_energy": 0.49548233160446803,
        "mean_age": 50.39970636302048,
        "actions": {
          "teach": 14
        },
        "events": [
          "14.1h: coupled route migration dispute crisis"
        ],
        "active_crisis": "route_migration_dispute",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.06416351007071425
      },
      {
        "label": "24h",
        "hours": 24.0,
        "alive": 15,
        "total_agents": 15,
        "children": 1,
        "births": 1,
        "deaths": 0,
        "major_shocks": 1,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 0.9749707334310717,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9800997192597505,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9922821272130606,
        "paths": 0.980520546645884,
        "sanitation": 0.12,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.9990347415876993,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.0,
        "adaptive_pressure": 0.028357329781188427,
        "pressure_integral": 0.024377052640226472,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5165455619422269,
        "mean_health": 0.898013672805709,
        "mean_energy": 0.40703604283083755,
        "mean_age": 52.65305927215251,
        "actions": {
          "improve_tools": 11,
          "learn": 1,
          "scout": 1,
          "teach": 2
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "21.9h: resolved route migration dispute",
          "23.8h: new generation born"
        ],
        "active_crisis": null,
        "crisis_resolved": 1,
        "crisis_unresolved": 0,
        "crisis_damage": 0.101041819645259
      },
      {
        "label": "36h",
        "hours": 36.0,
        "alive": 16,
        "total_agents": 16,
        "children": 2,
        "births": 2,
        "deaths": 0,
        "major_shocks": 2,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 0.6734461205773381,
        "architecture": 0.9720275795931194,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9922037412215696,
        "paths": 1.0,
        "sanitation": 0.12,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.003445716294244769,
        "disease": 0.012305655915853232,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.036574344254165045,
        "adaptive_pressure": 0.03084638290913664,
        "pressure_integral": 0.029409408381203154,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5565472614508779,
        "mean_health": 0.8748113902580317,
        "mean_energy": 0.2265018062521838,
        "mean_age": 61.268493067642815,
        "actions": {
          "improve_tools": 11,
          "learn": 2,
          "scout": 2,
          "teach": 1
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "21.9h: resolved route migration dispute",
          "23.8h: new generation born",
          "25.5h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 1,
        "crisis_unresolved": 1,
        "crisis_damage": 0.46144254842165056
      },
      {
        "label": "48h",
        "hours": 48.0,
        "alive": 16,
        "total_agents": 16,
        "children": 0,
        "births": 2,
        "deaths": 0,
        "major_shocks": 3,
        "next_shock": 172.0,
        "weather": "cold",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 0.6735011805695621,
        "architecture": 0.9596637850101295,
        "architecture_tier": 3,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9922036057324273,
        "paths": 1.0,
        "sanitation": 0.22222755906044983,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0012653524120394607,
        "disease": 0.009632610985952254,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.171649716975302,
        "adaptive_pressure": 0.052250354915615194,
        "pressure_integral": 0.03514062353976592,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5995916564518482,
        "mean_health": 0.8748113902580317,
        "mean_energy": 0.06515625010708967,
        "mean_age": 73.26849306764228,
        "actions": {
          "improve_tools": 13,
          "scout": 3
        },
        "events": [
          "21.9h: resolved route migration dispute",
          "23.8h: new generation born",
          "25.5h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 1,
        "crisis_unresolved": 1,
        "crisis_damage": 0.5838337329894229
      },
      {
        "label": "60h",
        "hours": 60.0,
        "alive": 16,
        "total_agents": 16,
        "children": 0,
        "births": 2,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 0.6208876426714238,
        "architecture": 0.946318553598365,
        "architecture_tier": 3,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9918946753938223,
        "paths": 1.0,
        "sanitation": 0.22222755906044983,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.056774404667058374,
        "disease": 0.0067258218280215765,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.24907517224526693,
        "adaptive_pressure": 0.054215009740111224,
        "pressure_integral": 0.04196271905003778,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.6228310929108491,
        "mean_health": 0.8652253871365206,
        "mean_energy": 0.0156559184878758,
        "mean_age": 85.2684930676417,
        "actions": {
          "improve_tools": 13,
          "scout": 3
        },
        "events": [
          "25.5h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: unresolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis"
        ],
        "active_crisis": "contaminated_water_trust",
        "crisis_resolved": 1,
        "crisis_unresolved": 2,
        "crisis_damage": 0.8562366135053705
      },
      {
        "label": "72h",
        "hours": 72.0,
        "alive": 16,
        "total_agents": 16,
        "children": 0,
        "births": 2,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 0.5856380867900789,
        "architecture": 0.9382464139317344,
        "architecture_tier": 3,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9892451239964162,
        "paths": 1.0,
        "sanitation": 0.22222755906044983,
        "garden": 0.8325290104609683,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.25111347133957357,
        "adaptive_pressure": 0.04378124605239493,
        "pressure_integral": 0.04824602947070214,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.6461408909651606,
        "mean_health": 0.8553776211772829,
        "mean_energy": 0.0,
        "mean_age": 97.26849306764095,
        "actions": {
          "improve_tools": 13,
          "scout": 3
        },
        "events": [
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: unresolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis",
          "64.8h: unresolved contaminated water trust"
        ],
        "active_crisis": null,
        "crisis_resolved": 1,
        "crisis_unresolved": 3,
        "crisis_damage": 1.1343565843864232
      }
    ]
  },
  "crisis_logs": {
    "20261021:designed:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261021:reactive:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:frame_mlp:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.414741847826087,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:return_selected_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.9569727891156462,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9569727891156462,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.3164961636828644,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:repair_critic_baseline:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.9569727891156462,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9569727891156462,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.3164961636828644,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.07846467391304347,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:body": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.08095238095238096,
        "social_fraction": 1.0,
        "coupled_fraction": 0.08095238095238096,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:infrastructure": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:tools": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.033627717391304345,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:social_culture": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.8967391304347808,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:environment": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:rollout_window_gru:previous_action": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.24781341107871724,
        "social_fraction": 1.0,
        "coupled_fraction": 0.24781341107871724,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261022:designed:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261022:reactive:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:frame_mlp:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.9326086956521744,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:return_selected_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.7846153846153844,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7846153846153844,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.9326086956521744,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.2671428571428572,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.9020408163265292,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:repair_critic_baseline:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.7846153846153844,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7846153846153844,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.9326086956521744,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.2671428571428572,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.9020408163265292,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:infrastructure": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:tools": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:social_culture": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:environment": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:rollout_window_gru:previous_action": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:designed:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      }
    ],
    "20261023:reactive:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:frame_mlp:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:return_selected_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:repair_critic_baseline:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:body": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:infrastructure": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.9479813664596274,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:environment": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:rollout_window_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.6516806722689076,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:designed:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261024:reactive:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:frame_mlp:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.8499999999999986,
        "social_fraction": 0.31842105263157905,
        "coupled_fraction": 0.31842105263157905,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:return_selected_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.9107142857142847,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:repair_critic_baseline:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.9107142857142847,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:body": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.8051242236024847,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8051242236024847,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:infrastructure": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:tools": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:social_culture": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.7576530612244898,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:environment": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261024:rollout_window_gru:previous_action": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:designed:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261025:reactive:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:frame_mlp:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.953028250773993,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:return_selected_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.7979591836734696,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7979591836734696,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.8861892583120218,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:repair_critic_baseline:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.7979591836734696,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7979591836734696,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.8861892583120218,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.7968749999999998,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.12330163043478261,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:body": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5748724489795919,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5748724489795919,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:infrastructure": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:tools": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:social_culture": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:environment": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.047826086956521734,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:rollout_window_gru:previous_action": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.2540760869565217,
        "social_fraction": 1.0,
        "coupled_fraction": 0.2540760869565217,
        "resolved": false
      }
    ]
  },
  "notes": {
    "claim": "rollout-window sequence control for coupled social/environment crisis pressure",
    "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
    "input_discipline": "the plan critic consumes ordinary features, plan identity, current/recent response fractions, and crisis-window timing but not active crisis profile labels"
  }
};
