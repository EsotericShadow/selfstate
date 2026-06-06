window.SSRM_3D_COUPLED_CRISIS_JOINT_ARBITRATION_RESULTS = {
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
    "action_epochs": 64,
    "action_hidden_size": 64,
    "joint_candidates": [
      [
        0.0,
        0.0,
        0.0
      ],
      [
        0.12,
        0.12,
        0.7
      ],
      [
        0.14,
        0.14,
        0.85
      ],
      [
        0.16,
        0.14,
        1.0
      ],
      [
        0.14,
        0.16,
        1.0
      ],
      [
        0.18,
        0.16,
        1.1
      ],
      [
        0.16,
        0.18,
        1.1
      ],
      [
        0.2,
        0.18,
        1.2
      ]
    ],
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
  "primary_env_actions": {
    "contaminated_water_trust": "sanitize",
    "route_migration_dispute": "scout",
    "storm_shelter_coordination": "construct",
    "quarantine_rumor": "treat"
  },
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
  "joint_selection": [
    {
      "env_quota": 0.0,
      "social_quota": 0.0,
      "coordinator_strength": 0.0,
      "tune_total_score": 0.51872704,
      "tune_maturation_score": 0.9975519999999999,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_env_response": 0.18696581196581197,
      "tune_social_response": 0.22435897435897437,
      "tune_coupled_response": 0.014957264957264958,
      "tune_damage": 1.3751838360693405,
      "selection_objective": -0.06481938138490467,
      "selected": false
    },
    {
      "env_quota": 0.12,
      "social_quota": 0.12,
      "coordinator_strength": 0.7,
      "tune_total_score": 0.7348664304547166,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.44763839678065936,
      "tune_resolved_rate": 0.6666666666666666,
      "tune_env_response": 0.6912393162393163,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6912393162393163,
      "tune_damage": 0.756136937159044,
      "selection_objective": 1.5583814132477145,
      "selected": false
    },
    {
      "env_quota": 0.14,
      "social_quota": 0.14,
      "coordinator_strength": 0.85,
      "tune_total_score": 0.7608701964112047,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.5018129091900098,
      "tune_resolved_rate": 0.75,
      "tune_env_response": 0.7061965811965812,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.7061965811965812,
      "tune_damage": 0.7465296611665169,
      "selection_objective": 1.6948848027872563,
      "selected": true
    },
    {
      "env_quota": 0.16,
      "social_quota": 0.14,
      "coordinator_strength": 1.0,
      "tune_total_score": 0.7525858599707512,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.48455387493906493,
      "tune_resolved_rate": 0.75,
      "tune_env_response": 0.6709401709401709,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6709401709401709,
      "tune_damage": 0.7454748872314875,
      "selection_objective": 1.6471382485774082,
      "selected": false
    },
    {
      "env_quota": 0.14,
      "social_quota": 0.16,
      "coordinator_strength": 1.0,
      "tune_total_score": 0.7311051594530552,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.4398024155271986,
      "tune_resolved_rate": 0.6666666666666666,
      "tune_env_response": 0.6709401709401709,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6709401709401709,
      "tune_damage": 0.7495266760272958,
      "selection_objective": 1.5354526276048064,
      "selected": false
    },
    {
      "env_quota": 0.18,
      "social_quota": 0.16,
      "coordinator_strength": 1.1,
      "tune_total_score": 0.7206972558934153,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.4181192831112816,
      "tune_resolved_rate": 0.6666666666666666,
      "tune_env_response": 0.6602564102564102,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6602564102564102,
      "tune_damage": 0.7962159676674007,
      "selection_objective": 1.4852618964259527,
      "selected": false
    },
    {
      "env_quota": 0.16,
      "social_quota": 0.18,
      "coordinator_strength": 1.1,
      "tune_total_score": 0.7174709389049886,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.41139778938539306,
      "tune_resolved_rate": 0.6666666666666666,
      "tune_env_response": 0.6506410256410257,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6506410256410257,
      "tune_damage": 0.8016839717193899,
      "selection_objective": 1.4678663755314614,
      "selected": false
    },
    {
      "env_quota": 0.2,
      "social_quota": 0.18,
      "coordinator_strength": 1.2,
      "tune_total_score": 0.6979108893645019,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.37064768617604565,
      "tune_resolved_rate": 0.6666666666666666,
      "tune_env_response": 0.6378205128205129,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.6378205128205129,
      "tune_damage": 0.8997978197167925,
      "selection_objective": 1.375655816284389,
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
  "action_training": [
    {
      "head": "environment",
      "train_loss": 0.915516197681427,
      "accuracy": 0.626181423664093,
      "crisis_accuracy": 0.626181423664093,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 30472,
      "crisis_examples": 30472,
      "action_epochs": 64,
      "action_hidden_size": 64
    },
    {
      "head": "social",
      "train_loss": 0.0003357464156579226,
      "accuracy": 1.0,
      "crisis_accuracy": 1.0,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 30472,
      "crisis_examples": 30472,
      "action_epochs": 64,
      "action_hidden_size": 64
    }
  ],
  "summary": [
    {
      "controller": "designed",
      "ablation": "none",
      "mean_total_score": 0.7731740215566465,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.5274458782430135,
      "mean_resolved_rate": 1.0,
      "mean_env_response_rate": 0.07692307692307693,
      "mean_social_response_rate": 0.9230769230769231,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 0.035868919305675796,
      "mean_final_alive": 17.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.2,
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
      "mean_total_score": 0.32991530473270797,
      "mean_maturation_score": 0.6344525091013613,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.25,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.8783355352905318,
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
      "mean_social_response_rate": 0.267948717948718,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.2327649353288412,
      "mean_final_alive": 15.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.4,
      "mean_architecture_tier": 3.2,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "body",
      "mean_total_score": 0.6643114402381205,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.30064883382941765,
      "mean_resolved_rate": 0.6,
      "mean_env_response_rate": 0.5378205128205128,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.5378205128205128,
      "mean_crisis_damage": 0.8578897788023964,
      "mean_final_alive": 16.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
      "mean_architecture_tier": 3.6,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "environment",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.1987170858746894,
      "mean_final_alive": 16.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.6047701618250633,
      "mean_maturation_score": 0.8416241799063151,
      "mean_crisis_score": 0.34817830890370716,
      "mean_resolved_rate": 0.65,
      "mean_env_response_rate": 0.635897435897436,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.635897435897436,
      "mean_crisis_damage": 0.9364868829857451,
      "mean_final_alive": 16.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.6,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.06235845187789468,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "none",
      "mean_total_score": 0.7023386932742274,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.3798722776546403,
      "mean_resolved_rate": 0.65,
      "mean_env_response_rate": 0.6455128205128206,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.6455128205128206,
      "mean_crisis_damage": 0.8596689502907712,
      "mean_final_alive": 18.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 4.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.6761696201851382,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.3269445753857045,
      "mean_resolved_rate": 0.65,
      "mean_env_response_rate": 0.5262820512820513,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.5262820512820513,
      "mean_crisis_damage": 0.8405612864437748,
      "mean_final_alive": 16.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
      "mean_architecture_tier": 3.2,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.3301282051282051,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.405647372830233,
      "mean_final_alive": 16.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
      "mean_architecture_tier": 3.8,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "joint_arbitration_gru",
      "ablation": "tools",
      "mean_total_score": 0.6654667806296561,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.3030557929784504,
      "mean_resolved_rate": 0.55,
      "mean_env_response_rate": 0.49935897435897436,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.49935897435897436,
      "mean_crisis_damage": 0.7217819834315335,
      "mean_final_alive": 16.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.6,
      "mean_architecture_tier": 3.8,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "reactive",
      "ablation": "none",
      "mean_total_score": 0.24020394999024508,
      "mean_maturation_score": 0.4619306730581636,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.12243589743589745,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.8679809470955386,
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
      "controller": "return_selected_gru",
      "ablation": "none",
      "mean_total_score": 0.5192362239999999,
      "mean_maturation_score": 0.9985312000000001,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.1,
      "mean_env_response_rate": 0.27692307692307694,
      "mean_social_response_rate": 0.31346153846153846,
      "mean_coupled_response_rate": 0.02692307692307692,
      "mean_crisis_damage": 1.3217387820097712,
      "mean_final_alive": 16.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
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
      "mean_total_score": 0.6643114402381205,
      "total_loss": 0.03802725303610688,
      "crisis_score_loss": 0.07922344382522267,
      "resolved_rate_loss": 0.050000000000000044,
      "env_response_loss": 0.10769230769230775,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.10769230769230775,
      "damage_increase": -0.0017791714883748089
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.6047701618250633,
      "total_loss": 0.09756853144916411,
      "crisis_score_loss": 0.031693968750933166,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.009615384615384581,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.009615384615384581,
      "damage_increase": 0.07681793269497394
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.6654667806296561,
      "total_loss": 0.036871912644571236,
      "crisis_score_loss": 0.0768164846761899,
      "resolved_rate_loss": 0.09999999999999998,
      "env_response_loss": 0.1461538461538462,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.1461538461538462,
      "damage_increase": -0.13788696685923763
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.52,
      "total_loss": 0.18233869327422736,
      "crisis_score_loss": 0.3798722776546403,
      "resolved_rate_loss": 0.65,
      "env_response_loss": 0.31538461538461543,
      "social_response_loss": 1.0,
      "coupled_response_loss": 0.6455128205128206,
      "damage_increase": 0.5459784225394618
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.52,
      "total_loss": 0.18233869327422736,
      "crisis_score_loss": 0.3798722776546403,
      "resolved_rate_loss": 0.65,
      "env_response_loss": 0.6455128205128206,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.6455128205128206,
      "damage_increase": 0.3390481355839182
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.6761696201851382,
      "total_loss": 0.026169073089089223,
      "crisis_score_loss": 0.05292770226893584,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.11923076923076925,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.11923076923076925,
      "damage_increase": -0.01910766384699636
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_env_quota": 0.14,
    "selected_social_quota": 0.14,
    "selected_coordinator_strength": 0.85,
    "joint_arbitration_total_score": 0.7023386932742274,
    "return_selected_total_score": 0.5192362239999999,
    "base_gru_total_score": 0.5192362239999999,
    "designed_total_score": 0.7731740215566465,
    "frame_total_score": 0.32991530473270797,
    "reactive_total_score": 0.24020394999024508,
    "gain_over_return_selected": 0.18310246927422746,
    "gain_over_base_gru": 0.18310246927422746,
    "gain_over_frame": 0.3724233885415194,
    "gain_over_reactive": 0.4621347432839823,
    "gap_to_designed": 0.07083532828241912,
    "joint_arbitration_crisis_score": 0.3798722776546403,
    "return_selected_crisis_score": 0.0,
    "joint_arbitration_resolved_rate": 0.65,
    "return_selected_resolved_rate": 0.1,
    "joint_arbitration_env_response": 0.6455128205128206,
    "return_selected_env_response": 0.27692307692307694,
    "joint_arbitration_social_response": 1.0,
    "return_selected_social_response": 0.31346153846153846,
    "joint_arbitration_coupled_response": 0.6455128205128206,
    "return_selected_coupled_response": 0.02692307692307692,
    "social_culture_total_loss": 0.18233869327422736,
    "environment_total_loss": 0.18233869327422736,
    "social_culture_crisis_loss": 0.3798722776546403,
    "environment_crisis_loss": 0.3798722776546403,
    "social_culture_coupled_loss": 0.6455128205128206,
    "environment_coupled_loss": 0.6455128205128206,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "supports_joint_selection": true,
    "supports_social_environment_dependency": true,
    "verdict": "pass"
  },
  "trace": {
    "seed": 20261021,
    "condition": "joint_arbitration_gru:social_first:joint_0.14_0.14_0.85:none",
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
        "food": 0.7218768969716715,
        "water": 0.7773353609426376,
        "materials": 0.5486011229065013,
        "medicine": 0.36,
        "shelter": 0.44722743078287913,
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
        "mean_wisdom": 0.1263760141184936,
        "mean_health": 0.9082319505303424,
        "mean_energy": 0.7698269211401068,
        "mean_age": 27.604259636695343,
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
        "food": 0.6917116350950369,
        "water": 0.7072965203539177,
        "materials": 0.31688775548743126,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.6669826756616399,
        "architecture_tier": 2,
        "tools": 0.26497999999999994,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.6049795453183413,
        "granary": 0.5411717521079934,
        "paths": 0.5223826601627919,
        "sanitation": 0.12,
        "garden": 0.5158960742934897,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.12143475199096057,
        "map_knowledge": 0.192759830411322,
        "contamination": 0.1531563416696692,
        "disease": 0.06369540363307583,
        "predators": 0.1030148057884163,
        "route_hazard": 0.08273543721944399,
        "resource_migration": 0.2318008473405054,
        "adaptive_pressure": 0.12875650525644766,
        "pressure_integral": 0.006138250194024521,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.12994238553705115,
        "mean_health": 0.9082319505303424,
        "mean_energy": 0.7230387588516657,
        "mean_age": 30.604259636695385,
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
        "food": 0.7615252736437186,
        "water": 0.7283947006047528,
        "materials": 0.08277295289798102,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.2245918323846777,
        "tool_tier": 1,
        "workshop": 0.11188157586180705,
        "waterworks": 1.0,
        "granary": 0.9863082693613121,
        "paths": 0.9682440905151318,
        "sanitation": 0.12,
        "garden": 0.8282156864083101,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.1206578395180841,
        "map_knowledge": 0.19097130199644538,
        "contamination": 0.07149115330477418,
        "disease": 0.02337026120447371,
        "predators": 0.05826301802372735,
        "route_hazard": 0.006479058874654588,
        "resource_migration": 0.2509613839683115,
        "adaptive_pressure": 0.10365773113078106,
        "pressure_integral": 0.010237544009287206,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.13344890568996667,
        "mean_health": 0.9082319505303424,
        "mean_energy": 0.6784587588516661,
        "mean_age": 33.60425963669543,
        "actions": {
          "construct": 9,
          "improve_tools": 5
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
        "food": 0.8814111475407987,
        "water": 0.7870073827005813,
        "materials": 0.0009956749933002918,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9970008444610735,
        "architecture_tier": 4,
        "tools": 0.8476476537876009,
        "tool_tier": 4,
        "workshop": 0.6410474181035902,
        "waterworks": 1.0,
        "granary": 0.9947429156194565,
        "paths": 0.976858432183442,
        "sanitation": 0.12,
        "garden": 0.8342712431494816,
        "culture": 0.38386126638660634,
        "symbols": 0.28211003508901267,
        "risk_memory": 0.3060860873112211,
        "map_knowledge": 0.1888542022249052,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.23885032718677954,
        "adaptive_pressure": 0.09462702087028625,
        "pressure_integral": 0.014338449634453548,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.2884826520888714,
        "mean_wisdom": 0.15728534138322278,
        "mean_health": 0.9082319505303424,
        "mean_energy": 0.6338787588516663,
        "mean_age": 36.604259636695474,
        "actions": {
          "social_repair": 1,
          "teach": 13
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
        "water": 0.847491878360183,
        "materials": 0.00593984742372778,
        "medicine": 0.36,
        "shelter": 1.0,
        "architecture": 0.9933380306632549,
        "architecture_tier": 4,
        "tools": 0.8266476537875999,
        "tool_tier": 4,
        "workshop": 0.6410474181035902,
        "waterworks": 1.0,
        "granary": 0.9947429156194565,
        "paths": 0.9767158690157344,
        "sanitation": 0.12,
        "garden": 0.8342712431494816,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.187214801297498,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.1839782051001846,
        "adaptive_pressure": 0.05260169066302965,
        "pressure_integral": 0.016340439285775006,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.25182312275279684,
        "mean_health": 0.9082319505303424,
        "mean_energy": 0.5892984982135464,
        "mean_age": 39.60425963669552,
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
        "water": 0.9254647241424766,
        "materials": 0.012901931944978556,
        "medicine": 0.3190511737095609,
        "shelter": 1.0,
        "architecture": 0.9940027702280558,
        "architecture_tier": 4,
        "tools": 0.7846476537875978,
        "tool_tier": 4,
        "workshop": 0.6410474181035902,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 0.9827658565964572,
        "sanitation": 0.5034312802148846,
        "garden": 0.8384562987721865,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.18358994675659598,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.11173598455441026,
        "adaptive_pressure": 0.054501716972290525,
        "pressure_integral": 0.020849430689260217,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.3720011024207758,
        "mean_health": 0.9310469317577811,
        "mean_energy": 0.5001384982135472,
        "mean_age": 45.604259636695595,
        "actions": {
          "sanitize": 3,
          "social_repair": 3,
          "teach": 5,
          "treat": 3
        },
        "events": [
          "14.1h: coupled route migration dispute crisis"
        ],
        "active_crisis": "route_migration_dispute",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.11150143053119477
      },
      {
        "label": "24h",
        "hours": 24.0,
        "alive": 17,
        "total_agents": 17,
        "children": 3,
        "births": 3,
        "deaths": 0,
        "major_shocks": 1,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 0.9931175628871762,
        "materials": 0.0,
        "medicine": 0.274096558141843,
        "shelter": 0.9523108505522478,
        "architecture": 0.9979800877325995,
        "architecture_tier": 4,
        "tools": 0.9367691913820692,
        "tool_tier": 4,
        "workshop": 0.8008024173991002,
        "waterworks": 1.0,
        "granary": 0.9999656933803791,
        "paths": 1.0,
        "sanitation": 0.9031371759115555,
        "garden": 0.869351839351982,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.4949866678770388,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.007093982018340862,
        "adaptive_pressure": 0.04465638978585234,
        "pressure_integral": 0.02532689053676025,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.4007934106760966,
        "mean_health": 0.8819827906927362,
        "mean_energy": 0.4079218262891419,
        "mean_age": 42.79174323021996,
        "actions": {
          "improve_tools": 7,
          "learn": 3,
          "scout": 5,
          "teach": 2
        },
        "events": [
          "14.1h: coupled route migration dispute crisis",
          "19.6h: new generation born",
          "21.9h: unresolved route migration dispute",
          "23.6h: new generation born",
          "23.8h: new generation born"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 1,
        "crisis_damage": 0.40956035195860263
      },
      {
        "label": "36h",
        "hours": 36.0,
        "alive": 17,
        "total_agents": 17,
        "children": 2,
        "births": 3,
        "deaths": 0,
        "major_shocks": 2,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.1817102557194402,
        "shelter": 0.6775506076986043,
        "architecture": 0.9899079480659684,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9999379478624045,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 0.869351839351982,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.036574344254165045,
        "adaptive_pressure": 0.03403709911038465,
        "pressure_integral": 0.03100201326623963,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.44618495301965744,
        "mean_health": 0.8743937797297575,
        "mean_energy": 0.23131538090047446,
        "mean_age": 54.791743230219936,
        "actions": {
          "improve_tools": 8,
          "learn": 3,
          "scout": 5,
          "teach": 1
        },
        "events": [
          "19.6h: new generation born",
          "21.9h: unresolved route migration dispute",
          "23.6h: new generation born",
          "23.8h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.8277457939975298
      },
      {
        "label": "48h",
        "hours": 48.0,
        "alive": 17,
        "total_agents": 17,
        "children": 0,
        "births": 3,
        "deaths": 0,
        "major_shocks": 3,
        "next_shock": 172.0,
        "weather": "cold",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.03840000000000005,
        "medicine": 0.11203439550055756,
        "shelter": 0.679322183064221,
        "architecture": 0.9775441534829785,
        "architecture_tier": 4,
        "tools": 0.948999999999999,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9999379478624045,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 0.869351839351982,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.171649716975302,
        "adaptive_pressure": 0.05241277545006247,
        "pressure_integral": 0.03709922478167689,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5036584941602927,
        "mean_health": 0.8760484212615156,
        "mean_energy": 0.0700009932744905,
        "mean_age": 66.7917432302196,
        "actions": {
          "sanitize": 3,
          "scout": 8,
          "social_repair": 3,
          "treat": 3
        },
        "events": [
          "21.9h: unresolved route migration dispute",
          "23.6h: new generation born",
          "23.8h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.9467095944386807
      },
      {
        "label": "60h",
        "hours": 60.0,
        "alive": 17,
        "total_agents": 17,
        "children": 0,
        "births": 3,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.019200000000000002,
        "medicine": 0.05633958546082065,
        "shelter": 0.6763551761470319,
        "architecture": 0.964198922071214,
        "architecture_tier": 4,
        "tools": 0.9744999999999995,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9999379478624045,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 0.869351839351982,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 4.6046560326344994e-05,
        "disease": 4.093027584564e-05,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.24907517224526693,
        "adaptive_pressure": 0.05934151339884976,
        "pressure_integral": 0.04392440166927355,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5242499024944378,
        "mean_health": 0.8760484212615156,
        "mean_energy": 0.01617325406773435,
        "mean_age": 78.79174323021907,
        "actions": {
          "sanitize": 3,
          "scout": 8,
          "social_repair": 3,
          "treat": 3
        },
        "events": [
          "23.8h: new generation born",
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: resolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis"
        ],
        "active_crisis": "contaminated_water_trust",
        "crisis_resolved": 1,
        "crisis_unresolved": 2,
        "crisis_damage": 1.0530161177997024
      },
      {
        "label": "72h",
        "hours": 72.0,
        "alive": 17,
        "total_agents": 17,
        "children": 0,
        "births": 3,
        "deaths": 0,
        "major_shocks": 4,
        "next_shock": 172.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.000780709665166591,
        "shelter": 0.894465135492153,
        "architecture": 0.9956726388032948,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 0.969070112841291,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.25111347133957357,
        "adaptive_pressure": 0.04874950339098698,
        "pressure_integral": 0.05076504777522448,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5445446371241563,
        "mean_health": 0.8834466833614165,
        "mean_energy": 0.0,
        "mean_age": 90.79174323021834,
        "actions": {
          "improve_tools": 6,
          "sanitize": 4,
          "scout": 7
        },
        "events": [
          "27.0h: coupled storm shelter coordination crisis",
          "34.8h: unresolved storm shelter coordination",
          "42.0h: coupled quarantine rumor crisis",
          "49.8h: resolved quarantine rumor",
          "57.0h: coupled contaminated water trust crisis",
          "64.8h: resolved contaminated water trust"
        ],
        "active_crisis": null,
        "crisis_resolved": 2,
        "crisis_unresolved": 2,
        "crisis_damage": 1.1361766404660685
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 42.0,
        "end": 49.8,
        "env_fraction": 0.0,
        "social_fraction": 0.8519021739130429,
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
        "env_fraction": 0.9598639455782312,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9598639455782312,
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
        "social_fraction": 0.7398097826086949,
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
    "20261021:joint_arbitration_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.023129251700680274,
        "social_fraction": 1.0,
        "coupled_fraction": 0.023129251700680274,
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
    "20261021:joint_arbitration_gru:body": [
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
    "20261021:joint_arbitration_gru:infrastructure": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.7144927536231882,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7144927536231882,
        "resolved": false
      }
    ],
    "20261021:joint_arbitration_gru:tools": [
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
        "env_fraction": 0.8288862179487176,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8288862179487176,
        "resolved": false
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
    "20261021:joint_arbitration_gru:social_culture": [
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
    "20261021:joint_arbitration_gru:environment": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261021:joint_arbitration_gru:previous_action": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.5451895043731779,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5451895043731779,
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
        "env_fraction": 0.1968349358974359,
        "social_fraction": 1.0,
        "coupled_fraction": 0.1968349358974359,
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
        "social_fraction": 0.17678571428571432,
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
    "20261022:joint_arbitration_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.08755151098901097,
        "social_fraction": 1.0,
        "coupled_fraction": 0.08755151098901097,
        "resolved": false
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
    "20261022:joint_arbitration_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.10508241758241758,
        "social_fraction": 1.0,
        "coupled_fraction": 0.10508241758241758,
        "resolved": false
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
        "env_fraction": 0.9020408163265292,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9020408163265292,
        "resolved": false
      }
    ],
    "20261022:joint_arbitration_gru:infrastructure": [
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:joint_arbitration_gru:tools": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.3969780219780216,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3969780219780216,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:joint_arbitration_gru:social_culture": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.11948260073260071,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 27.0,
        "end": 34.8,
        "env_fraction": 1.0,
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
        "env_fraction": 0.27551020408163274,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261022:joint_arbitration_gru:environment": [
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
    "20261022:joint_arbitration_gru:previous_action": [
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
    "20261023:joint_arbitration_gru:none": [
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
        "env_fraction": 0.44497863247863234,
        "social_fraction": 1.0,
        "coupled_fraction": 0.44497863247863234,
        "resolved": false
      }
    ],
    "20261023:joint_arbitration_gru:body": [
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:joint_arbitration_gru:infrastructure": [
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
    "20261023:joint_arbitration_gru:tools": [
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
        "env_fraction": 0.7083333333333337,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7083333333333337,
        "resolved": false
      }
    ],
    "20261023:joint_arbitration_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 1.0,
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
        "env_fraction": 0.9020408163265292,
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
    "20261023:joint_arbitration_gru:environment": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261023:joint_arbitration_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.715079365079365,
        "social_fraction": 1.0,
        "coupled_fraction": 0.715079365079365,
        "resolved": false
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
        "social_fraction": 0.09649122807017546,
        "coupled_fraction": 0.09649122807017546,
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
    "20261024:joint_arbitration_gru:none": [
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
        "env_fraction": 0.6710526315789468,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6710526315789468,
        "resolved": false
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
    "20261024:joint_arbitration_gru:body": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.9806677018633532,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9806677018633532,
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
    "20261024:joint_arbitration_gru:infrastructure": [
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
        "env_fraction": 0.15178571428571425,
        "social_fraction": 1.0,
        "coupled_fraction": 0.15178571428571425,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261024:joint_arbitration_gru:tools": [
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
    "20261024:joint_arbitration_gru:social_culture": [
      {
        "crisis": "contaminated_water_trust",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.2833333333333334,
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
    "20261024:joint_arbitration_gru:environment": [
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
        "social_fraction": 1.0,
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
    "20261024:joint_arbitration_gru:previous_action": [
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
        "env_fraction": 0.3269230769230769,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3269230769230769,
        "resolved": false
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
    "20261025:return_selected_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.8685860058309036,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8685860058309036,
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
        "social_fraction": 0.5181159420289854,
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
    "20261025:joint_arbitration_gru:none": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.48571428571428593,
        "social_fraction": 1.0,
        "coupled_fraction": 0.48571428571428593,
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
    "20261025:joint_arbitration_gru:body": [
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
        "env_fraction": 0.22329059829059833,
        "social_fraction": 1.0,
        "coupled_fraction": 0.22329059829059833,
        "resolved": false
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
    "20261025:joint_arbitration_gru:infrastructure": [
      {
        "crisis": "route_migration_dispute",
        "start": 14.1,
        "end": 21.9,
        "env_fraction": 0.03469387755102041,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03469387755102041,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 57.0,
        "end": 64.8,
        "env_fraction": 0.6630434782608698,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6630434782608698,
        "resolved": false
      }
    ],
    "20261025:joint_arbitration_gru:tools": [
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
        "env_fraction": 0.7500000000000004,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7500000000000004,
        "resolved": false
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
    "20261025:joint_arbitration_gru:social_culture": [
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
    "20261025:joint_arbitration_gru:environment": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261025:joint_arbitration_gru:previous_action": [
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
    ]
  },
  "notes": {
    "claim": "joint environmental/social crisis arbitration for 72h SSRM-3D coupled crises",
    "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
    "input_discipline": "action heads consume ordinary observation features and previous-action context, but not active crisis profile labels at runtime"
  }
};
