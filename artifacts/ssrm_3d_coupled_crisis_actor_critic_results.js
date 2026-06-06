window.SSRM_3D_COUPLED_CRISIS_ACTOR_CRITIC_RESULTS = {
  "config": {
    "train_seeds": [
      20260911,
      20260912,
      20260913
    ],
    "tune_seeds": [
      20261111,
      20261112
    ],
    "eval_seeds": [
      20261121,
      20261122,
      20261123
    ],
    "hours": 96.0,
    "step_hours": 0.1,
    "population": 14,
    "epochs": 24,
    "hidden_size": 64,
    "action_epochs": 32,
    "action_hidden_size": 64,
    "actor_critic_epochs": 4,
    "actor_critic_hidden_size": 64,
    "actor_critic_learning_rate": 0.003,
    "entropy_coef": 0.008,
    "value_coef": 0.45,
    "policy_temperature": 1.0,
    "policy_bias_candidates": [
      0.0,
      0.2,
      0.4,
      0.7,
      1.0
    ],
    "device": "auto",
    "trace_seed": 20261121
  },
  "policy_context_names": [
    "elapsed_fraction",
    "remaining_fraction",
    "env_progress",
    "social_progress",
    "env_response_rate",
    "social_response_rate",
    "current_env_fraction",
    "current_social_fraction"
  ],
  "action_candidates": [
    "none",
    "sanitize",
    "treat",
    "scout",
    "construct",
    "social_repair",
    "teach",
    "learn"
  ],
  "schedule": [
    {
      "phase": "train",
      "seed": 20260911,
      "crisis_count": 7,
      "first_crisis_hour": 14.837,
      "last_crisis_hour": 87.626,
      "profile_sequence": "quarantine_rumor;contaminated_water_trust;quarantine_rumor;route_migration_dispute;contaminated_water_trust;route_migration_dispute;contaminated_water_trust"
    },
    {
      "phase": "train",
      "seed": 20260912,
      "crisis_count": 6,
      "first_crisis_hour": 13.447,
      "last_crisis_hour": 78.823,
      "profile_sequence": "contaminated_water_trust;quarantine_rumor;route_migration_dispute;quarantine_rumor;contaminated_water_trust;storm_shelter_coordination"
    },
    {
      "phase": "train",
      "seed": 20260913,
      "crisis_count": 6,
      "first_crisis_hour": 17.43,
      "last_crisis_hour": 85.03,
      "profile_sequence": "storm_shelter_coordination;contaminated_water_trust;route_migration_dispute;quarantine_rumor;storm_shelter_coordination;contaminated_water_trust"
    },
    {
      "phase": "tune",
      "seed": 20261111,
      "crisis_count": 6,
      "first_crisis_hour": 17.291,
      "last_crisis_hour": 81.495,
      "profile_sequence": "quarantine_rumor;contaminated_water_trust;storm_shelter_coordination;quarantine_rumor;storm_shelter_coordination;contaminated_water_trust"
    },
    {
      "phase": "tune",
      "seed": 20261112,
      "crisis_count": 5,
      "first_crisis_hour": 13.997,
      "last_crisis_hour": 73.905,
      "profile_sequence": "contaminated_water_trust;route_migration_dispute;quarantine_rumor;contaminated_water_trust;quarantine_rumor"
    },
    {
      "phase": "eval",
      "seed": 20261121,
      "crisis_count": 6,
      "first_crisis_hour": 15.985,
      "last_crisis_hour": 77.641,
      "profile_sequence": "quarantine_rumor;storm_shelter_coordination;quarantine_rumor;storm_shelter_coordination;quarantine_rumor;contaminated_water_trust"
    },
    {
      "phase": "eval",
      "seed": 20261122,
      "crisis_count": 5,
      "first_crisis_hour": 15.283,
      "last_crisis_hour": 77.612,
      "profile_sequence": "storm_shelter_coordination;quarantine_rumor;contaminated_water_trust;route_migration_dispute;storm_shelter_coordination"
    },
    {
      "phase": "eval",
      "seed": 20261123,
      "crisis_count": 6,
      "first_crisis_hour": 17.134,
      "last_crisis_hour": 87.749,
      "profile_sequence": "storm_shelter_coordination;contaminated_water_trust;quarantine_rumor;route_migration_dispute;quarantine_rumor;route_migration_dispute"
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
      "tune_total_score": 0.33789449653533526,
      "tune_maturation_score": 0.6497971087217986,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.5658538743643489,
      "selection_objective": 0.024723721662465448,
      "selected": false
    },
    {
      "router": "balanced",
      "social_bias": 1.0,
      "environment_bias": 1.0,
      "infrastructure_bias": 1.0,
      "tool_bias": 1.0,
      "teaching_bias": 1.0,
      "tune_total_score": 0.47857196719737405,
      "tune_maturation_score": 0.9203307061487962,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.6008034514803995,
      "selection_objective": 0.15841127690129414,
      "selected": false
    },
    {
      "router": "social_env",
      "social_bias": 1.55,
      "environment_bias": 1.45,
      "infrastructure_bias": 0.75,
      "tool_bias": 0.7,
      "teaching_bias": 1.2,
      "tune_total_score": 0.49362125413242786,
      "tune_maturation_score": 0.9492716425623613,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.4693556163021042,
      "selection_objective": 0.20433346420534032,
      "selected": false
    },
    {
      "router": "environment_first",
      "social_bias": 0.55,
      "environment_bias": 2.0,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.65,
      "teaching_bias": 0.55,
      "tune_total_score": 0.43294519387689523,
      "tune_maturation_score": 0.8325869113017215,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.647088302213385,
      "selection_objective": 0.10352753343421817,
      "selected": false
    },
    {
      "router": "social_first",
      "social_bias": 2.0,
      "environment_bias": 0.55,
      "infrastructure_bias": 0.6,
      "tool_bias": 0.6,
      "teaching_bias": 1.35,
      "tune_total_score": 0.5110422720000001,
      "tune_maturation_score": 0.9827736,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.08333333333333333,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.4795659294352268,
      "selection_objective": 0.2197124194462881,
      "selected": true
    },
    {
      "router": "build_tool",
      "social_bias": 0.45,
      "environment_bias": 0.7,
      "infrastructure_bias": 1.65,
      "tool_bias": 1.7,
      "teaching_bias": 0.55,
      "tune_total_score": 0.4551213630874053,
      "tune_maturation_score": 0.8752333905527026,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.600753482125354,
      "selection_objective": 0.13497066666233448,
      "selected": false
    },
    {
      "router": "teaching_tradition",
      "social_bias": 1.1,
      "environment_bias": 0.75,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.7,
      "teaching_bias": 2.0,
      "tune_total_score": 0.4955384310363755,
      "tune_maturation_score": 0.952958521223799,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.5772573819816156,
      "selection_objective": 0.18008695464005237,
      "selected": false
    },
    {
      "router": "high_pressure",
      "social_bias": 1.8,
      "environment_bias": 1.6,
      "infrastructure_bias": 1.3,
      "tool_bias": 1.25,
      "teaching_bias": 1.5,
      "tune_total_score": 0.5176910115958624,
      "tune_maturation_score": 0.9955596376843507,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.599471522121532,
      "selection_objective": 0.19779670717155595,
      "selected": false
    }
  ],
  "base_training": [
    {
      "architecture": "frame_mlp",
      "train_loss": 2.033389091491699,
      "train_accuracy": 0.19714455428741143,
      "device_used": "mps",
      "parameter_count": 9932,
      "train_sequences": 52,
      "train_steps": 47138
    },
    {
      "architecture": "gru",
      "train_loss": 1.9481220245361328,
      "train_accuracy": 0.2012389155246298,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_sequences": 52,
      "train_steps": 47138
    }
  ],
  "action_training": [
    {
      "head": "environment",
      "train_loss": 1.284205436706543,
      "accuracy": 0.3714165687561035,
      "crisis_accuracy": 0.3714165687561035,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 23790,
      "crisis_examples": 23790,
      "action_epochs": 32,
      "action_hidden_size": 64
    },
    {
      "head": "social",
      "train_loss": 0.0006799261318519711,
      "accuracy": 1.0,
      "crisis_accuracy": 1.0,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 23790,
      "crisis_examples": 23790,
      "action_epochs": 32,
      "action_hidden_size": 64
    }
  ],
  "active_policy_training": {
    "episodes": 12,
    "crises": 73,
    "epochs": 4,
    "final_loss": 0.5550292134284973,
    "mean_return": 1.4876616289390523,
    "return_std": 1.0898192738508323,
    "moving_baseline": 1.751864624573109,
    "mean_entropy": 1.5104497241979604,
    "policy_temperature": 1.0,
    "entropy_coef": 0.008,
    "device_used": "mps",
    "parameter_count": 10312
  },
  "active_policy_selection": [
    {
      "policy_bias": 0.0,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.16702127659574467,
      "tune_social_response": 0.11486647850629614,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.564162800819049,
      "selection_objective": -0.5709320962620956,
      "selected": true
    },
    {
      "policy_bias": 0.2,
      "tune_total_score": 0.51895780546709,
      "tune_maturation_score": 0.9979957797444037,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.16702127659574467,
      "tune_social_response": 0.08659357359965263,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.6248475210892517,
      "selection_objective": -0.5908514601243574,
      "selected": false
    },
    {
      "policy_bias": 0.4,
      "tune_total_score": 0.5059683267139945,
      "tune_maturation_score": 0.973016012911528,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.16702127659574467,
      "tune_social_response": 0.08679982631350412,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.555219123469665,
      "selection_objective": -0.5748053226875754,
      "selected": false
    },
    {
      "policy_bias": 0.7,
      "tune_total_score": 0.49561885711222187,
      "tune_maturation_score": 0.9531131867542728,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.16702127659574467,
      "tune_social_response": 0.07701910551454624,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.646858570326386,
      "selection_objective": -0.609097691090577,
      "selected": false
    },
    {
      "policy_bias": 1.0,
      "tune_total_score": 0.5032498151469521,
      "tune_maturation_score": 0.967788106051831,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.16702127659574467,
      "tune_social_response": 0.17948871037776815,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.66029569729322,
      "selection_objective": -0.6097347118632934,
      "selected": false
    }
  ],
  "actor_critic_training": {
    "episodes": 12,
    "crises": 71,
    "epochs": 4,
    "final_loss": 0.11719121783971786,
    "final_policy_loss": 0.13176655769348145,
    "final_value_loss": 0.004153331741690636,
    "mean_return": 2.2555034557199427,
    "return_std": 0.4487538158888897,
    "mean_value_prediction": 2.2997266992333447,
    "mean_abs_advantage": 0.3862354914271257,
    "mean_entropy": 1.9885718377743882,
    "policy_temperature": 1.0,
    "entropy_coef": 0.008,
    "value_coef": 0.45,
    "device_used": "mps",
    "parameter_count": 10377
  },
  "actor_critic_selection": [
    {
      "policy_bias": 0.0,
      "tune_total_score": 0.49861397485714287,
      "tune_maturation_score": 0.9588730285714286,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.09948979591836735,
      "tune_social_response": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.7556118691657896,
      "selection_objective": -0.6424610902016241,
      "selected": false
    },
    {
      "policy_bias": 0.2,
      "tune_total_score": 0.5023122742857142,
      "tune_maturation_score": 0.9659851428571429,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.09948979591836735,
      "tune_social_response": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.755945467457038,
      "selection_objective": -0.6407926579291094,
      "selected": true
    },
    {
      "policy_bias": 0.4,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.09948979591836735,
      "tune_social_response": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.783219057203658,
      "selection_objective": -0.6410300983051707,
      "selected": false
    },
    {
      "policy_bias": 0.7,
      "tune_total_score": 0.5100553979070133,
      "tune_maturation_score": 0.9808757652057947,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.09948979591836735,
      "tune_social_response": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.87670294497286,
      "selection_objective": -0.6757183513959488,
      "selected": false
    },
    {
      "policy_bias": 1.0,
      "tune_total_score": 0.5110422720000001,
      "tune_maturation_score": 0.9827736,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.09948979591836735,
      "tune_social_response": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 2.7726986491334062,
      "selection_objective": -0.64196327716269,
      "selected": false
    }
  ],
  "summary": [
    {
      "controller": "active_policy_gru",
      "ablation": "none",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.17777777777777778,
      "mean_env_response_rate": 0.26973495139574555,
      "mean_social_response_rate": 0.2286204277076056,
      "mean_coupled_response_rate": 0.147238931711276,
      "mean_crisis_damage": 2.264503737549232,
      "mean_final_alive": 15.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.6666666666666665,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "body",
      "mean_total_score": 0.4911945861008468,
      "mean_maturation_score": 0.9446049732708593,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17899569594292067,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.794281918516124,
      "mean_final_alive": 11.333333333333334,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.6666666666666666,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "environment",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 0.49890112253963337,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.7243369780726683,
      "mean_final_alive": 24.666666666666668,
      "mean_alive_at_12h": 14.0,
      "mean_births": 13.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.41229837953129067,
      "mean_maturation_score": 0.7928814990986358,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17899569594292067,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.762940890059351,
      "mean_final_alive": 13.666666666666666,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.3412121485537362,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "none",
      "mean_total_score": 0.504093824,
      "mean_maturation_score": 0.9694112,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17899569594292067,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.6620215089566504,
      "mean_final_alive": 12.333333333333334,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.3333333333333335,
      "mean_architecture_tier": 3.6666666666666665,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 0.9503778005573188,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17899569594292067,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.700503775329277,
      "mean_final_alive": 14.666666666666666,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 0.9636441198094868,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.2817969104451164,
      "mean_maturation_score": 0.5419171354713778,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.11530142842699713,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.575321696151782,
      "mean_final_alive": 0.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.0,
      "mean_architecture_tier": 2.0,
      "mean_tool_tier": 0.6666666666666666,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "actor_critic_gru",
      "ablation": "tools",
      "mean_total_score": 0.4864673459106708,
      "mean_maturation_score": 0.93551412675129,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17899569594292067,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.7975499207956864,
      "mean_final_alive": 11.666666666666666,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 0.5898081402087049,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "designed",
      "ablation": "none",
      "mean_total_score": 0.7703955568308388,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.5216574100642474,
      "mean_resolved_rate": 1.0,
      "mean_env_response_rate": 0.0765198259816191,
      "mean_social_response_rate": 0.923480174018381,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 0.0524073998164361,
      "mean_final_alive": 14.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.3333333333333335,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "fixed_joint_gru",
      "ablation": "none",
      "mean_total_score": 0.5943017629605518,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.15479533950114957,
      "mean_resolved_rate": 0.5888888888888889,
      "mean_env_response_rate": 0.5516270202348456,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.5516270202348456,
      "mean_crisis_damage": 1.3287282546664871,
      "mean_final_alive": 15.666666666666666,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.6666666666666665,
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
      "mean_total_score": 0.31458269964962504,
      "mean_maturation_score": 0.6049667300954327,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.29934339774668506,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.604050261967762,
      "mean_final_alive": 12.333333333333334,
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
      "mean_total_score": 0.32292327319542674,
      "mean_maturation_score": 0.6210062946065898,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.29934339774668506,
      "mean_social_response_rate": 0.008503401360544218,
      "mean_coupled_response_rate": 0.008503401360544218,
      "mean_crisis_damage": 2.5791929457290776,
      "mean_final_alive": 11.333333333333334,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.3333333333333333,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.0746038359187468,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "reactive",
      "ablation": "none",
      "mean_total_score": 0.10399880894589868,
      "mean_maturation_score": 0.19999770951134363,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.20481452236674583,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.316648791443782,
      "mean_final_alive": 1.6666666666666667,
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
      "mean_total_score": 0.5196716512741703,
      "mean_maturation_score": 0.9993685601426351,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.1111111111111111,
      "mean_env_response_rate": 0.29934339774668506,
      "mean_social_response_rate": 0.37229542130806337,
      "mean_coupled_response_rate": 0.02760084925690021,
      "mean_crisis_damage": 2.041827090011732,
      "mean_final_alive": 13.666666666666666,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.0,
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
      "mean_total_score": 0.4911945861008468,
      "total_loss": 0.012899237899153204,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.0,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0,
      "damage_increase": 0.1322604095594735
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.41229837953129067,
      "total_loss": 0.09179544446870935,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.0,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0,
      "damage_increase": 0.10091938110270071
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.4864673459106708,
      "total_loss": 0.01762647808932921,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.0,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0,
      "damage_increase": 0.13552841183903608
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.2817969104451164,
      "total_loss": 0.22229691355488362,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.06369426751592354,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0,
      "damage_increase": -0.08669981280486816
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.52,
      "total_loss": -0.015906175999999994,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.17899569594292067,
      "social_response_loss": -0.49890112253963337,
      "coupled_response_loss": 0.0,
      "damage_increase": -0.9376845308839821
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.52,
      "total_loss": -0.015906175999999994,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.0,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.0,
      "damage_increase": 0.03848226637262675
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_policy_bias": 0.2,
    "training_crises": 71,
    "actor_critic_total_score": 0.504093824,
    "active_policy_total_score": 0.52,
    "fixed_joint_total_score": 0.5943017629605518,
    "return_selected_total_score": 0.5196716512741703,
    "actor_critic_crisis_score": 0.0,
    "active_policy_crisis_score": 0.0,
    "fixed_joint_crisis_score": 0.15479533950114957,
    "return_selected_crisis_score": 0.0,
    "actor_critic_resolved_rate": 0.0,
    "active_policy_resolved_rate": 0.17777777777777778,
    "fixed_joint_resolved_rate": 0.5888888888888889,
    "return_selected_resolved_rate": 0.1111111111111111,
    "actor_critic_coupled_response": 0.0,
    "active_policy_coupled_response": 0.147238931711276,
    "fixed_joint_coupled_response": 0.5516270202348456,
    "return_selected_coupled_response": 0.02760084925690021,
    "gain_over_active_policy": -0.015906175999999994,
    "gain_over_return_selected": -0.01557782727417023,
    "gain_over_fixed_joint": -0.09020793896055179,
    "social_culture_crisis_loss": 0.0,
    "environment_crisis_loss": 0.0,
    "social_culture_coupled_loss": 0.0,
    "environment_coupled_loss": 0.0,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "mean_crisis_count": 5.666666666666667,
    "supports_active_policy_improvement": false,
    "supports_return_baseline_improvement": false,
    "supports_fixed_joint_improvement": false,
    "supports_actor_critic_learning": false,
    "supports_social_environment_dependency": false,
    "verdict": "partial_or_failed"
  },
  "trace": {
    "seed": 20261121,
    "condition": "actor_critic_gru",
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 0.7070995505557607,
        "water": 0.7125448459037187,
        "materials": 0.46244507647450894,
        "medicine": 0.35792787256702324,
        "shelter": 0.41090000236624014,
        "architecture": 0.07158821658765707,
        "architecture_tier": 0,
        "tools": 0.3490707763909711,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.130065623950411,
        "granary": 0.07183621593066952,
        "paths": 0.12789932957928463,
        "sanitation": 0.12404707178080332,
        "garden": 0.22,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.07,
        "map_knowledge": 0.1,
        "contamination": 0.15170298855592135,
        "disease": 0.16222392707570174,
        "predators": 0.19729983036283605,
        "route_hazard": 0.2288908644546986,
        "resource_migration": 0.14975068746158834,
        "adaptive_pressure": 0.1,
        "pressure_integral": 0.0,
        "adaptation_evidence": 0.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.1367063658096414,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.7782561059807932,
        "mean_age": 33.25783963951937,
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 0.6817422115655282,
        "water": 0.6490182687522975,
        "materials": 0.2171874168140842,
        "medicine": 0.35792787256702324,
        "shelter": 1.0,
        "architecture": 0.6543111206542623,
        "architecture_tier": 2,
        "tools": 0.30077077639097066,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.6252869009960301,
        "granary": 0.5207593605645922,
        "paths": 0.577056175442636,
        "sanitation": 0.12404707178080332,
        "garden": 0.5351408126653936,
        "culture": 0.11060971847885553,
        "symbols": 0.08456429730985697,
        "risk_memory": 0.08897646751386688,
        "map_knowledge": 0.09872868774930538,
        "contamination": 0.12341906186462595,
        "disease": 0.12100542377721418,
        "predators": 0.17793380448201015,
        "route_hazard": 0.10070062666228294,
        "resource_migration": 0.23947976777402033,
        "adaptive_pressure": 0.13659773513787102,
        "pressure_integral": 0.006528544207394126,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.02849416881698781,
        "mean_wisdom": 0.1423475742257425,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.7316341186252027,
        "mean_age": 36.25783963951941,
        "actions": {
          "construct": 10,
          "social_repair": 4
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
        "next_shock": 196.0,
        "weather": "hot",
        "food": 0.73756735649039,
        "water": 0.6593009467003175,
        "materials": 0.05562994255858214,
        "medicine": 0.35792787256702324,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.2457507763909706,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.9590150742717923,
        "granary": 0.823356651399351,
        "paths": 0.879536180494786,
        "sanitation": 0.12404707178080332,
        "garden": 0.7475132865681505,
        "culture": 0.24799119832111335,
        "symbols": 0.17042772221126817,
        "risk_memory": 0.08875725449558063,
        "map_knowledge": 0.0977376604438157,
        "contamination": 0.04857245404438992,
        "disease": 0.06803331910818566,
        "predators": 0.13538004380968394,
        "route_hazard": 0.049983482786082396,
        "resource_migration": 0.2734754962802847,
        "adaptive_pressure": 0.1023065187638943,
        "pressure_integral": 0.01057444544500911,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.02849416881698781,
        "mean_wisdom": 0.145460776394906,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.687054118625203,
        "mean_age": 39.25783963951945,
        "actions": {
          "construct": 9,
          "social_repair": 5
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
        "next_shock": 196.0,
        "weather": "hot",
        "food": 0.8570125886955082,
        "water": 0.7180384711564041,
        "materials": 0.0,
        "medicine": 0.35792787256702324,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.19073077639097052,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.12404707178080332,
        "garden": 0.9588549833954001,
        "culture": 0.38584068189561416,
        "symbols": 0.2565836494453311,
        "risk_memory": 0.08826055353507728,
        "map_knowledge": 0.09658157899950555,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.08679740132672989,
        "route_hazard": 0.018492352343223252,
        "resource_migration": 0.2510005848170721,
        "adaptive_pressure": 0.10236440586336358,
        "pressure_integral": 0.014903874859800574,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.02849416881698781,
        "mean_wisdom": 0.14856525150096594,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.6424741186252033,
        "mean_age": 42.257839639519496,
        "actions": {
          "construct": 9,
          "social_repair": 5
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
        "next_shock": 196.0,
        "weather": "hot",
        "food": 1.0,
        "water": 0.7773656068160057,
        "materials": 0.0,
        "medicine": 0.35792787256702324,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.13571077639097046,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.12404707178080332,
        "garden": 1.0,
        "culture": 0.5223164706612349,
        "symbols": 0.3418810174238445,
        "risk_memory": 0.08749824679951758,
        "map_knowledge": 0.0956768939421257,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.03221799720572365,
        "route_hazard": 0.0011229040431386741,
        "resource_migration": 0.19169022311782968,
        "adaptive_pressure": 0.0863601613540292,
        "pressure_integral": 0.01842111745110239,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.02849416881698781,
        "mean_wisdom": 0.15167460419208045,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.5978941186252038,
        "mean_age": 45.25783963951954,
        "actions": {
          "construct": 9,
          "social_repair": 5
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
        "next_shock": 196.0,
        "weather": "hot",
        "food": 1.0,
        "water": 0.8956750603281369,
        "materials": 0.006710156163931513,
        "medicine": 0.35792787256702324,
        "shelter": 1.0,
        "architecture": 0.9976735232945879,
        "architecture_tier": 4,
        "tools": 0.2979584071507418,
        "tool_tier": 2,
        "workshop": 0.30419995470726807,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.12404707178080332,
        "garden": 1.0,
        "culture": 0.5828392033357055,
        "symbols": 0.3797077253453887,
        "risk_memory": 0.4714942872964181,
        "map_knowledge": 0.8146130915957256,
        "contamination": 0.0012653501173185927,
        "disease": 0.03685258444441749,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.06227892395106809,
        "adaptive_pressure": 0.089667750159586,
        "pressure_integral": 0.025222442152334695,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.02849416881698781,
        "mean_wisdom": 0.15873127635658396,
        "mean_health": 0.9056092506235344,
        "mean_energy": 0.5087341186252046,
        "mean_age": 51.257839639519624,
        "actions": {
          "scout": 14
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.08417801095445185
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.040040858341499626,
        "medicine": 0.35792787256702324,
        "shelter": 0.9867998361249471,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.2483907517224681,
        "tool_tier": 2,
        "workshop": 0.3210446039958739,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 0.12404707178080332,
        "garden": 1.0,
        "culture": 0.5828392033357055,
        "symbols": 0.3797077253453887,
        "risk_memory": 0.999560066,
        "map_knowledge": 0.9996001199999999,
        "contamination": 0.03575483985789239,
        "disease": 0.19472324653907688,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.0,
        "adaptive_pressure": 0.058103187857439974,
        "pressure_integral": 0.02995118968247196,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.08022636157314599,
        "mean_wisdom": 0.1577994037091073,
        "mean_health": 0.8823159815113699,
        "mean_energy": 0.41849963040564364,
        "mean_age": 53.5139836635517,
        "actions": {
          "construct": 9,
          "improve_tools": 5,
          "learn": 1
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis",
          "22.9h: new generation born",
          "23.8h: unresolved quarantine rumor"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 1,
        "crisis_damage": 0.5006644677386854
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.045381168502832615,
        "medicine": 0.35792787256702324,
        "shelter": 0.709364534818617,
        "architecture": 0.9950023259417127,
        "architecture_tier": 4,
        "tools": 0.6800118534531842,
        "tool_tier": 4,
        "workshop": 0.7512574859406883,
        "waterworks": 1.0,
        "granary": 0.9999624151139088,
        "paths": 1.0,
        "sanitation": 0.12404707178080332,
        "garden": 1.0,
        "culture": 0.6875858252184234,
        "symbols": 0.45535806337179596,
        "risk_memory": 1.0,
        "map_knowledge": 0.9991060852372045,
        "contamination": 0.026844180835671576,
        "disease": 0.045213461336031414,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.03662871873754618,
        "adaptive_pressure": 0.04592916239478171,
        "pressure_integral": 0.038048128369457465,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.2629874455542783,
        "mean_wisdom": 0.1778400952573664,
        "mean_health": 0.8612276469299185,
        "mean_energy": 0.23845192144266447,
        "mean_age": 62.07560968457953,
        "actions": {
          "improve_tools": 5,
          "learn": 2,
          "teach": 9
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis",
          "22.9h: new generation born",
          "23.8h: unresolved quarantine rumor",
          "25.5h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 1.007128264470281
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
        "next_shock": 196.0,
        "weather": "cold",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.023537781061380415,
        "medicine": 0.35792787256702324,
        "shelter": 0.7111437304603059,
        "architecture": 0.9825025313587228,
        "architecture_tier": 4,
        "tools": 0.9751999999999993,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9998999419141654,
        "paths": 1.0,
        "sanitation": 0.12728749665362846,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 0.8037437944748592,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.007727942484922216,
        "disease": 0.011544956363127051,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.171649716975302,
        "adaptive_pressure": 0.06848629623794104,
        "pressure_integral": 0.04514032251784648,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.8373810051951859,
        "mean_wisdom": 0.23837522940709002,
        "mean_health": 0.8612276469299185,
        "mean_energy": 0.07150812178519192,
        "mean_age": 74.07560968457898,
        "actions": {
          "scout": 16
        },
        "events": [
          "22.9h: new generation born",
          "23.8h: unresolved quarantine rumor",
          "25.5h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 1.1308503195278166
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.02050875875620673,
        "medicine": 0.35792787256702324,
        "shelter": 0.5675973974686754,
        "architecture": 0.9691572999469583,
        "architecture_tier": 4,
        "tools": 0.9783999999999994,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9995998522626571,
        "paths": 1.0,
        "sanitation": 0.12728749665362846,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 0.8037437944748592,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.24907517224526693,
        "adaptive_pressure": 0.07618638942392002,
        "pressure_integral": 0.054368731233564144,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.899987033988694,
        "mean_wisdom": 0.2635839373547447,
        "mean_health": 0.8521378632930382,
        "mean_energy": 0.015334083545216998,
        "mean_age": 86.07560968457841,
        "actions": {
          "scout": 16
        },
        "events": [
          "25.5h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis",
          "52.7h: unresolved quarantine rumor",
          "57.3h: coupled storm shelter coordination crisis"
        ],
        "active_crisis": "storm_shelter_coordination",
        "crisis_resolved": 0,
        "crisis_unresolved": 3,
        "crisis_damage": 1.6055089239240186
      },
      {
        "label": "72h",
        "hours": 72.0,
        "alive": 16,
        "total_agents": 16,
        "children": 0,
        "births": 2,
        "deaths": 0,
        "major_shocks": 5,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.03875463639014414,
        "medicine": 0.35792787256702324,
        "shelter": 0.35111609214507994,
        "architecture": 0.9610851602803274,
        "architecture_tier": 4,
        "tools": 0.9591999999999988,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9995256849890924,
        "paths": 1.0,
        "sanitation": 0.12728749665362846,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 0.8037437944748592,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.001243029789825829,
        "disease": 0.03368263469016952,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2511134713395807,
        "adaptive_pressure": 0.09348557383655659,
        "pressure_integral": 0.06603288559530825,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.9246332033645673,
        "mean_wisdom": 0.28622564652691523,
        "mean_health": 0.8415650146463516,
        "mean_energy": 0.0,
        "mean_age": 98.07560968457783,
        "actions": {
          "scout": 16
        },
        "events": [
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis",
          "52.7h: unresolved quarantine rumor",
          "57.3h: coupled storm shelter coordination crisis",
          "65.1h: unresolved storm shelter coordination",
          "66.9h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 4,
        "crisis_damage": 2.237049573553964
      },
      {
        "label": "96h",
        "hours": 96.0,
        "alive": 11,
        "total_agents": 16,
        "children": 0,
        "births": 2,
        "deaths": 5,
        "major_shocks": 6,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.18166701833329738,
        "medicine": 0.35792787256702324,
        "shelter": 0.27394957321176555,
        "architecture": 0.9352401342855726,
        "architecture_tier": 3,
        "tools": 0.8715999999999938,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9953056870800606,
        "paths": 1.0,
        "sanitation": 0.17119643954579572,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.044538063496048205,
        "adaptive_pressure": 0.09634339472874018,
        "pressure_integral": 0.10279298173746117,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.6515456863834799,
        "mean_health": 0.7982876845699564,
        "mean_energy": 0.0,
        "mean_age": 116.61911892994902,
        "actions": {
          "sanitize": 2,
          "scout": 2,
          "teach": 7
        },
        "events": [
          "57.3h: coupled storm shelter coordination crisis",
          "65.1h: unresolved storm shelter coordination",
          "66.9h: coupled quarantine rumor crisis",
          "74.8h: unresolved quarantine rumor",
          "77.7h: coupled contaminated water trust crisis",
          "85.6h: unresolved contaminated water trust"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 6,
        "crisis_damage": 3.042633396695091
      }
    ]
  },
  "crisis_logs": {
    "20261121:designed:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261121:reactive:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:frame_mlp:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.3074534161490683,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:return_selected_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 1.0,
        "social_fraction": 0.96611842105263,
        "coupled_fraction": 0.96611842105263,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:fixed_joint_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261121:active_policy_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:body": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:infrastructure": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:environment": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.9172932330827064,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.7902631578947374,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.7354285714285712,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:actor_critic_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:designed:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      }
    ],
    "20261122:reactive:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:frame_mlp:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 1.0,
        "social_fraction": 0.48073308270676696,
        "coupled_fraction": 0.48073308270676696,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.9326086956521744,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:return_selected_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:fixed_joint_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.03854875283446712,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03854875283446712,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261122:active_policy_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:infrastructure": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:tools": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:social_culture": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:environment": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.6846938775510203,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.48848684210526316,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:actor_critic_gru:previous_action": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 31.1,
        "end": 38.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:designed:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261123:reactive:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:frame_mlp:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:return_selected_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:fixed_joint_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261123:active_policy_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:infrastructure": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:tools": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:social_culture": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:environment": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:actor_critic_gru:previous_action": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ]
  },
  "notes": {
    "claim": "a learned critic baseline can improve sampled crisis-window policy learning",
    "not_claimed": "subjective consciousness, open-ended civilization, real-world competence, or full recurrent actor-critic training",
    "remaining_structure": "candidate repair actions are supplied, the base controller is imitation trained, and the actor-critic update uses completed crisis-window returns in an abstract simulator"
  }
};
