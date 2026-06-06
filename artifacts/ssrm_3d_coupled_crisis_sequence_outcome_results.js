window.SSRM_3D_COUPLED_CRISIS_SEQUENCE_OUTCOME_RESULTS = {
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
      7.0
    ],
    "max_plan_examples": 160000,
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
      "tune_coupled_response": 0.03311965811965812,
      "tune_damage": 1.0533372072962783,
      "selection_objective": 0.2585025284961301,
      "selected": false
    },
    {
      "plan_bias": 1.0,
      "tune_total_score": 0.559812054581359,
      "tune_maturation_score": 0.9913708619820111,
      "tune_crisis_score": 0.09229001323065254,
      "tune_resolved_rate": 0.3333333333333333,
      "tune_coupled_response": 0.24893162393162394,
      "tune_damage": 0.5820407436389171,
      "selection_objective": 0.49247614224923675,
      "selected": false
    },
    {
      "plan_bias": 1.75,
      "tune_total_score": 0.6046859400397095,
      "tune_maturation_score": 0.9871289615703013,
      "tune_crisis_score": 0.1903726667149019,
      "tune_resolved_rate": 0.4166666666666667,
      "tune_coupled_response": 0.3311965811965812,
      "tune_damage": 0.5663345053566906,
      "selection_objective": 0.5781376725872763,
      "selected": false
    },
    {
      "plan_bias": 2.75,
      "tune_total_score": 0.6472616856957821,
      "tune_maturation_score": 0.9907986589562898,
      "tune_crisis_score": 0.27509663133023216,
      "tune_resolved_rate": 0.5,
      "tune_coupled_response": 0.3621794871794872,
      "tune_damage": 0.5033258640870047,
      "selection_objective": 0.6657540982623462,
      "selected": false
    },
    {
      "plan_bias": 4.0,
      "tune_total_score": 0.6625173413264052,
      "tune_maturation_score": 0.9894768894226985,
      "tune_crisis_score": 0.3083111642220872,
      "tune_resolved_rate": 0.5,
      "tune_coupled_response": 0.42628205128205127,
      "tune_damage": 0.49267628293078874,
      "selection_objective": 0.6968085429654015,
      "selected": true
    },
    {
      "plan_bias": 5.5,
      "tune_total_score": 0.6630602268691029,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.29804213931063106,
      "tune_resolved_rate": 0.5,
      "tune_coupled_response": 0.4198717948717949,
      "tune_damage": 0.51407984616987,
      "selection_objective": 0.6892329493767477,
      "selected": false
    },
    {
      "plan_bias": 7.0,
      "tune_total_score": 0.6553867062219257,
      "tune_maturation_score": 0.9877644326464817,
      "tune_crisis_score": 0.29531083592865665,
      "tune_resolved_rate": 0.5,
      "tune_coupled_response": 0.39636752136752135,
      "tune_damage": 0.49563204386684195,
      "selection_objective": 0.6832787526341323,
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
    "train_loss": 0.07309090346097946,
    "pairwise_accuracy": 0.6510000228881836,
    "device_used": "mps",
    "parameter_count": 11953,
    "train_examples": 160000,
    "positive_examples": 160000,
    "plan_epochs": 72,
    "plan_hidden_size": 72
  },
  "summary": [
    {
      "controller": "designed",
      "ablation": "none",
      "mean_total_score": 0.8670652196330142,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.7230525409021129,
      "mean_resolved_rate": 1.0,
      "mean_env_response_rate": 0.7794871794871795,
      "mean_social_response_rate": 0.6243589743589744,
      "mean_coupled_response_rate": 0.47435897435897434,
      "mean_crisis_damage": 0.11435537764231485,
      "mean_final_alive": 16.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.0,
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
      "mean_total_score": 0.3301038391196419,
      "mean_maturation_score": 0.6348150752300807,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.25,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.1658555840967666,
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
      "mean_total_score": 0.518472448,
      "mean_maturation_score": 0.9970623999999999,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 0.4185897435897436,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.1162318187961262,
      "mean_final_alive": 16.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.2,
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
      "mean_total_score": 0.2400918333648246,
      "mean_maturation_score": 0.4617150641631242,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.42243589743589743,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.1825695406294492,
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
      "mean_total_score": 0.536406663884397,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.03577174975916016,
      "mean_resolved_rate": 0.2,
      "mean_env_response_rate": 0.29358974358974355,
      "mean_social_response_rate": 0.36858974358974356,
      "mean_coupled_response_rate": 0.08397435897435898,
      "mean_crisis_damage": 0.9365269632874241,
      "mean_final_alive": 16.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
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
      "mean_total_score": 0.536406663884397,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.03577174975916016,
      "mean_resolved_rate": 0.2,
      "mean_env_response_rate": 0.29358974358974355,
      "mean_social_response_rate": 0.36858974358974356,
      "mean_coupled_response_rate": 0.08397435897435898,
      "mean_crisis_damage": 0.9365269632874241,
      "mean_final_alive": 16.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "body",
      "mean_total_score": 0.49919711581337944,
      "mean_maturation_score": 0.9439672382951846,
      "mean_crisis_score": 0.017362816458090475,
      "mean_resolved_rate": 0.25,
      "mean_env_response_rate": 0.27179487179487183,
      "mean_social_response_rate": 0.8884615384615385,
      "mean_coupled_response_rate": 0.24166666666666664,
      "mean_crisis_damage": 0.7799073074841876,
      "mean_final_alive": 15.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 2.4,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "environment",
      "mean_total_score": 0.6457194328071268,
      "mean_maturation_score": 0.9867818453317249,
      "mean_crisis_score": 0.2762351525721457,
      "mean_resolved_rate": 0.5,
      "mean_env_response_rate": 0.49615384615384617,
      "mean_social_response_rate": 0.8948717948717949,
      "mean_coupled_response_rate": 0.43076923076923074,
      "mean_crisis_damage": 0.6034306996107196,
      "mean_final_alive": 16.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.4572131199999999,
      "mean_maturation_score": 0.879256,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.25,
      "mean_env_response_rate": 0.25,
      "mean_social_response_rate": 0.7974358974358975,
      "mean_coupled_response_rate": 0.19871794871794873,
      "mean_crisis_damage": 0.8819729389445226,
      "mean_final_alive": 14.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "none",
      "mean_total_score": 0.6609508542362524,
      "mean_maturation_score": 0.9906905548125655,
      "mean_crisis_score": 0.3037328452785801,
      "mean_resolved_rate": 0.5,
      "mean_env_response_rate": 0.4987179487179487,
      "mean_social_response_rate": 0.8948717948717949,
      "mean_coupled_response_rate": 0.43397435897435893,
      "mean_crisis_damage": 0.5290783175190754,
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
      "controller": "sequence_outcome_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.5990053133579882,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.16459440282914217,
      "mean_resolved_rate": 0.4,
      "mean_env_response_rate": 0.36217948717948717,
      "mean_social_response_rate": 0.8884615384615385,
      "mean_coupled_response_rate": 0.3141025641025641,
      "mean_crisis_damage": 0.5936130615138066,
      "mean_final_alive": 16.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.5988346341940615,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.16423882123762795,
      "mean_resolved_rate": 0.4,
      "mean_env_response_rate": 0.3243589743589744,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.3243589743589744,
      "mean_crisis_damage": 0.6455447598338837,
      "mean_final_alive": 17.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "sequence_outcome_gru",
      "ablation": "tools",
      "mean_total_score": 0.648151764471978,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.26857404264995427,
      "mean_resolved_rate": 0.5,
      "mean_env_response_rate": 0.42628205128205127,
      "mean_social_response_rate": 0.8814102564102564,
      "mean_coupled_response_rate": 0.36217948717948717,
      "mean_crisis_damage": 0.5189093286924386,
      "mean_final_alive": 15.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.2,
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
      "mean_total_score": 0.49919711581337944,
      "total_loss": 0.161753738422873,
      "crisis_score_loss": 0.2863700288204896,
      "resolved_rate_loss": 0.25,
      "env_response_loss": 0.2269230769230769,
      "social_response_loss": 0.0064102564102563875,
      "coupled_response_loss": 0.1923076923076923,
      "damage_increase": 0.25082898996511216
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.4572131199999999,
      "total_loss": 0.20373773423625252,
      "crisis_score_loss": 0.3037328452785801,
      "resolved_rate_loss": 0.25,
      "env_response_loss": 0.24871794871794872,
      "social_response_loss": 0.09743589743589742,
      "coupled_response_loss": 0.2352564102564102,
      "damage_increase": 0.35289462142544714
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.648151764471978,
      "total_loss": 0.012799089764274463,
      "crisis_score_loss": 0.03515880262862581,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.07243589743589746,
      "social_response_loss": 0.013461538461538525,
      "coupled_response_loss": 0.07179487179487176,
      "damage_increase": -0.01016898882663686
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.5988346341940615,
      "total_loss": 0.06211622004219097,
      "crisis_score_loss": 0.13949402404095212,
      "resolved_rate_loss": 0.09999999999999998,
      "env_response_loss": 0.17435897435897435,
      "social_response_loss": -0.10512820512820509,
      "coupled_response_loss": 0.10961538461538456,
      "damage_increase": 0.1164664423148083
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.6457194328071268,
      "total_loss": 0.015231421429125591,
      "crisis_score_loss": 0.027497692706434373,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.002564102564102555,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0032051282051281937,
      "damage_increase": 0.07435238209164419
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.5990053133579882,
      "total_loss": 0.061945540878264205,
      "crisis_score_loss": 0.1391384424494379,
      "resolved_rate_loss": 0.09999999999999998,
      "env_response_loss": 0.13653846153846155,
      "social_response_loss": 0.0064102564102563875,
      "coupled_response_loss": 0.11987179487179483,
      "damage_increase": 0.06453474399473114
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_plan_bias": 4.0,
    "sequence_outcome_total_score": 0.6609508542362524,
    "repair_critic_total_score": 0.536406663884397,
    "return_selected_total_score": 0.536406663884397,
    "base_gru_total_score": 0.518472448,
    "designed_total_score": 0.8670652196330142,
    "frame_total_score": 0.3301038391196419,
    "reactive_total_score": 0.2400918333648246,
    "gain_over_repair_critic": 0.12454419035185549,
    "gain_over_return_selected": 0.12454419035185549,
    "gain_over_base_gru": 0.1424784062362524,
    "gain_over_frame": 0.3308470151166105,
    "gain_over_reactive": 0.42085902087142785,
    "gap_to_designed": 0.20611436539676176,
    "sequence_outcome_crisis_score": 0.3037328452785801,
    "return_selected_crisis_score": 0.03577174975916016,
    "sequence_outcome_resolved_rate": 0.5,
    "return_selected_resolved_rate": 0.2,
    "sequence_outcome_coupled_response": 0.43397435897435893,
    "return_selected_coupled_response": 0.08397435897435898,
    "social_culture_total_loss": 0.06211622004219097,
    "environment_total_loss": 0.015231421429125591,
    "social_culture_crisis_loss": 0.13949402404095212,
    "environment_crisis_loss": 0.027497692706434373,
    "social_culture_coupled_loss": 0.10961538461538456,
    "environment_coupled_loss": 0.0032051282051281937,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "supports_sequence_outcome_selection": true,
    "supports_social_environment_dependency": false,
    "verdict": "partial_or_failed"
  },
  "trace": {
    "seed": 20261021,
    "condition": "sequence_outcome_gru:social_first:bias_4:none",
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
        "food": 0.7539213371453547,
        "water": 0.7396177781232319,
        "materials": 0.5042798946196576,
        "medicine": 0.36,
        "shelter": 0.4831233128483944,
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
        "mean_wisdom": 0.13702243837084607,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.7667795798845659,
        "mean_age": 28.786477564559675,
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
        "food": 0.7235753310094808,
        "water": 0.6694064702661525,
        "materials": 0.2734553178652818,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.6646044821573851,
        "architecture_tier": 2,
        "tools": 0.26497999999999994,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.6029672277378171,
        "granary": 0.5393379736895452,
        "paths": 0.5205530598627834,
        "sanitation": 0.12,
        "garden": 0.5146155085604288,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.12140186805223036,
        "map_knowledge": 0.19268778152097726,
        "contamination": 0.15415917674442237,
        "disease": 0.063730594031397,
        "predators": 0.10305818402038608,
        "route_hazard": 0.08311283239338745,
        "resource_migration": 0.23202183427048653,
        "adaptive_pressure": 0.12864423172778738,
        "pressure_integral": 0.006118046681172659,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.14057446554578293,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.7201735823446285,
        "mean_age": 31.78647756455972,
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
        "food": 0.7928382260257828,
        "water": 0.6891762727550804,
        "materials": 0.037830950092513624,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.27862574119757816,
        "tool_tier": 1,
        "workshop": 0.15570697859063815,
        "waterworks": 1.0,
        "granary": 0.9536279251381685,
        "paths": 0.9357502080694421,
        "sanitation": 0.12,
        "garden": 0.8053515322211695,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.1206146676963142,
        "map_knowledge": 0.19089933958592667,
        "contamination": 0.07277202665304516,
        "disease": 0.023508395708011613,
        "predators": 0.058306458873336284,
        "route_hazard": 0.010749660721845213,
        "resource_migration": 0.2534715839311648,
        "adaptive_pressure": 0.10343003997921763,
        "pressure_integral": 0.010212974969489492,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.14408151667123814,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.6755935823446289,
        "mean_age": 34.78647756455976,
        "actions": {
          "construct": 2,
          "improve_tools": 12
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
        "food": 0.9035428813540968,
        "water": 0.7477133031502121,
        "materials": 0.0008819968526983938,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9967880989870267,
        "architecture_tier": 4,
        "tools": 0.8819975162401826,
        "tool_tier": 4,
        "workshop": 0.6662299541199492,
        "waterworks": 1.0,
        "granary": 0.9546450548186728,
        "paths": 0.936956618079637,
        "sanitation": 0.12,
        "garden": 0.8062219458495573,
        "culture": 0.4304286392558049,
        "symbols": 0.3116455964763239,
        "risk_memory": 0.30875720295432163,
        "map_knowledge": 0.18877415827148616,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.24284688837593896,
        "adaptive_pressure": 0.09199698046388907,
        "pressure_integral": 0.014215211801836656,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.29266905600261883,
        "mean_wisdom": 0.16829807605479793,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.6310135823446291,
        "mean_age": 37.7864775645598,
        "actions": {
          "social_repair": 3,
          "teach": 11
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
        "water": 0.8070404388098138,
        "materials": 0.0046298204180546445,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.993261285189208,
        "architecture_tier": 4,
        "tools": 0.8609975162401816,
        "tool_tier": 4,
        "workshop": 0.6662299541199492,
        "waterworks": 1.0,
        "granary": 0.9546450548186728,
        "paths": 0.936983470557791,
        "sanitation": 0.12,
        "garden": 0.8062219458495573,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.18712692005508974,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.18795845229959313,
        "adaptive_pressure": 0.051878059993169794,
        "pressure_integral": 0.016184059518736735,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.26109668382415857,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.5864335823446296,
        "mean_age": 40.786477564559846,
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
        "water": 0.9936505018780728,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.8189975162401796,
        "tool_tier": 4,
        "workshop": 0.6662299541199492,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.1234315664785826,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.18349736376630532,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.11002947366301426,
        "adaptive_pressure": 0.054086008238503784,
        "pressure_integral": 0.020698822805252322,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.3620754723676485,
        "mean_health": 0.9036675357368071,
        "mean_energy": 0.4972735823446303,
        "mean_age": 46.78647756455994,
        "actions": {
          "construct": 9,
          "harvest_food": 3,
          "teach": 2
        },
        "events": [
          "14.1h: coupled route migration dispute crisis"
        ],
        "active_crisis": "route_migration_dispute",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.00904170899333862
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
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.7749975162401778,
        "tool_tier": 4,
        "workshop": 0.6662299541199492,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.1234315664785826,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 0.9956125174567517,
        "map_knowledge": 0.1799995828752663,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.030803314654007256,
        "adaptive_pressure": 0.047759621509175655,
        "pressure_integral": 0.025171656894528705,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.373195103348784,
        "mean_health": 0.8900897000210201,
        "mean_energy": 0.4049433435216558,
        "mean_age": 49.534045726922685,
        "actions": {
          "construct": 14,
          "learn": 1
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "20.0h: new generation born",
          "21.9h: resolved route migration dispute"
        ],
        "active_crisis": null,
        "crisis_resolved": 1,
        "crisis_unresolved": 0,
        "crisis_damage": 0.00904170899333862
      },
      {
        "label": "36h",
        "hours": 36.0,
        "alive": 15,
        "total_agents": 15,
        "children": 1,
        "births": 1,
        "deaths": 0,
        "major_shocks": 2,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.6849975162401744,
        "tool_tier": 4,
        "workshop": 0.6662299541199492,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.1234315664785826,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.17338339108447684,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.10270007343587674,
        "adaptive_pressure": 0.048597466220440325,
        "pressure_integral": 0.03354899950520276,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.4489354669060986,
        "mean_health": 0.8900897000210201,
        "mean_energy": 0.22662319309161577,
        "mean_age": 61.53404572692265,
        "actions": {
          "construct": 7,
          "learn": 1,
          "teach": 7
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "20.0h: new generation born",
          "21.9h: resolved route migration dispute",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: resolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 2,
        "crisis_unresolved": 0,
        "crisis_damage": 0.028543997889267328
      },
      {
        "label": "48h",
        "hours": 48.0,
        "alive": 15,
        "total_agents": 15,
        "children": 0,
        "births": 1,
        "deaths": 0,
        "major_shocks": 3,
        "next_shock": 172.0,
        "weather": "cold",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.6012501957126667,
        "tool_tier": 4,
        "workshop": 0.6713102561913521,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.18183520992827892,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.16737126548882494,
        "contamination": 0.0010931599655935645,
        "disease": 0.0017403162232265633,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2382559980376979,
        "adaptive_pressure": 0.07018501312043167,
        "pressure_integral": 0.0423808450276307,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5941608263376759,
        "mean_health": 0.8900897000210201,
        "mean_energy": 0.06045077591119852,
        "mean_age": 73.53404572692216,
        "actions": {
          "construct": 8,
          "harvest_food": 5,
          "teach": 2
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "20.0h: new generation born",
          "21.9h: resolved route migration dispute",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: resolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 2,
        "crisis_unresolved": 0,
        "crisis_damage": 0.10383049689708847
      },
      {
        "label": "60h",
        "hours": 60.0,
        "alive": 15,
        "total_agents": 15,
        "children": 0,
        "births": 1,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.5112501957126633,
        "tool_tier": 4,
        "workshop": 0.6713102561913521,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.18183520992827892,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.1618996184790657,
        "contamination": 0.0491418431505527,
        "disease": 0.0025828819455684573,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.31611908583503234,
        "adaptive_pressure": 0.07315277634695479,
        "pressure_integral": 0.05180256517342332,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.7208352597771008,
        "mean_health": 0.8810553201400815,
        "mean_energy": 0.005706219138150713,
        "mean_age": 85.53404572692153,
        "actions": {
          "construct": 8,
          "harvest_food": 5,
          "teach": 2
        },
        "events": [
          "21.9h: resolved route migration dispute",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: resolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: unresolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis"
        ],
        "active_crisis": "contaminated_water_trust",
        "crisis_resolved": 2,
        "crisis_unresolved": 1,
        "crisis_damage": 0.3288941066789574
      },
      {
        "label": "72h",
        "hours": 72.0,
        "alive": 15,
        "total_agents": 15,
        "children": 0,
        "births": 1,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.4212501957126671,
        "tool_tier": 4,
        "workshop": 0.6713102561913521,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.2156677900202398,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.15688352450485465,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.3185589519121221,
        "adaptive_pressure": 0.06340126081245327,
        "pressure_integral": 0.06097720418215639,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.8449033696175305,
        "mean_health": 0.8718115393689729,
        "mean_energy": 0.0,
        "mean_age": 97.53404572692072,
        "actions": {
          "construct": 9,
          "teach": 6
        },
        "events": [
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: resolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: unresolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis",
          "64.8h: unresolved contaminated water trust"
        ],
        "active_crisis": null,
        "crisis_resolved": 2,
        "crisis_unresolved": 2,
        "crisis_damage": 0.5585190485112468
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "env_fraction": 1.0,
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
        "env_fraction": 1.0,
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
        "social_fraction": 1.0,
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
    "20261021:return_selected_gru:none": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.6990196078431371,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6990196078431371,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
        "env_fraction": 0.6990196078431371,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6990196078431371,
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
    "20261021:sequence_outcome_gru:none": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.03369565217391305,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03369565217391305,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:body": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:infrastructure": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:tools": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.011481481481481483,
        "social_fraction": 1.0,
        "coupled_fraction": 0.011481481481481483,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.15724637681159423,
        "social_fraction": 1.0,
        "coupled_fraction": 0.15724637681159423,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:social_culture": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.6100583090379009,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6100583090379009,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:environment": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:sequence_outcome_gru:previous_action": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.03369565217391305,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03369565217391305,
        "resolved": false
      }
    ],
    "20261022:designed:none": [
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
        "env_fraction": 1.0,
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
    "20261022:return_selected_gru:none": [
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
        "social_fraction": 0.34736842105263166,
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
    "20261022:repair_critic_baseline:none": [
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
        "social_fraction": 0.34736842105263166,
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
    "20261022:sequence_outcome_gru:none": [
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
        "env_fraction": 0.1339506172839506,
        "social_fraction": 1.0,
        "coupled_fraction": 0.1339506172839506,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.05615942028985507,
        "social_fraction": 1.0,
        "coupled_fraction": 0.05615942028985507,
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
    "20261022:sequence_outcome_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.12774725274725277,
        "social_fraction": 1.0,
        "coupled_fraction": 0.12774725274725277,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.0123015873015873,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0123015873015873,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.060170807453416145,
        "social_fraction": 1.0,
        "coupled_fraction": 0.060170807453416145,
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
    "20261022:sequence_outcome_gru:infrastructure": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:sequence_outcome_gru:tools": [
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
        "env_fraction": 0.3100000000000001,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3100000000000001,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
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
    "20261022:sequence_outcome_gru:social_culture": [
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
        "env_fraction": 0.04211956521739131,
        "social_fraction": 1.0,
        "coupled_fraction": 0.04211956521739131,
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
    "20261022:sequence_outcome_gru:environment": [
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
        "social_fraction": 1.0,
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
    "20261022:sequence_outcome_gru:previous_action": [
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
        "env_fraction": 0.34444444444444483,
        "social_fraction": 1.0,
        "coupled_fraction": 0.34444444444444483,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.11582880434782611,
        "social_fraction": 1.0,
        "coupled_fraction": 0.11582880434782611,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "env_fraction": 1.0,
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
    "20261023:sequence_outcome_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5043650793650791,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5043650793650791,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.012034161490683228,
        "social_fraction": 1.0,
        "coupled_fraction": 0.012034161490683228,
        "resolved": false
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:sequence_outcome_gru:body": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.38134920634920627,
        "social_fraction": 1.0,
        "coupled_fraction": 0.38134920634920627,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.3489906832298135,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3489906832298135,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:sequence_outcome_gru:infrastructure": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:sequence_outcome_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.44285714285714267,
        "social_fraction": 1.0,
        "coupled_fraction": 0.44285714285714267,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:sequence_outcome_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.27063492063492056,
        "social_fraction": 1.0,
        "coupled_fraction": 0.27063492063492056,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:sequence_outcome_gru:environment": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261023:sequence_outcome_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5289682539682538,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5289682539682538,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.06551932367149758,
        "social_fraction": 1.0,
        "coupled_fraction": 0.06551932367149758,
        "resolved": false
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
        "env_fraction": 0.47195512820512875,
        "social_fraction": 1.0,
        "coupled_fraction": 0.47195512820512875,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "env_fraction": 1.0,
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
        "env_fraction": 1.0,
        "social_fraction": 0.3575851393188854,
        "coupled_fraction": 0.3575851393188854,
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
        "env_fraction": 1.0,
        "social_fraction": 0.3575851393188854,
        "coupled_fraction": 0.3575851393188854,
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
    "20261024:sequence_outcome_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5776397515527949,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5776397515527949,
        "resolved": false
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
    "20261024:sequence_outcome_gru:body": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.43322981366459606,
        "social_fraction": 1.0,
        "coupled_fraction": 0.43322981366459606,
        "resolved": false
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
        "env_fraction": 0.596153846153846,
        "social_fraction": 1.0,
        "coupled_fraction": 0.596153846153846,
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
    "20261024:sequence_outcome_gru:infrastructure": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
    "20261024:sequence_outcome_gru:tools": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.3971273291925464,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3971273291925464,
        "resolved": false
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
    "20261024:sequence_outcome_gru:social_culture": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.1556418219461697,
        "social_fraction": 1.0,
        "coupled_fraction": 0.1556418219461697,
        "resolved": false
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
    "20261024:sequence_outcome_gru:environment": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
    "20261024:sequence_outcome_gru:previous_action": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5776397515527949,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5776397515527949,
        "resolved": false
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
        "env_fraction": 0.49679487179487203,
        "social_fraction": 1.0,
        "coupled_fraction": 0.49679487179487203,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "env_fraction": 1.0,
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
        "env_fraction": 1.0,
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
        "env_fraction": 0.03669801253834867,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03669801253834867,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 0.5812499999999999,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5812499999999999,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.1980555555555556,
        "social_fraction": 0.9326086956521737,
        "coupled_fraction": 0.1980555555555556,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "social_fraction": 0.4641943734015345,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "social_fraction": 0.4641943734015345,
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
    "20261025:sequence_outcome_gru:none": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.06739130434782609,
        "social_fraction": 1.0,
        "coupled_fraction": 0.06739130434782609,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:body": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:infrastructure": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:tools": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.9602769679300289,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9602769679300289,
        "resolved": true
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:social_culture": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5535714285714286,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5535714285714286,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:environment": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:sequence_outcome_gru:previous_action": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.059462915601023014,
        "social_fraction": 1.0,
        "coupled_fraction": 0.059462915601023014,
        "resolved": false
      }
    ]
  },
  "notes": {
    "claim": "counterfactual sequence-plan outcome control for coupled social/environment crisis pressure",
    "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
    "input_discipline": "the plan critic consumes ordinary features, plan identity, current/recent response fractions, and crisis-window timing but not active crisis profile labels"
  }
};
