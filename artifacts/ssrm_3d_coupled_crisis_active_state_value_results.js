window.SSRM_3D_COUPLED_CRISIS_ACTIVE_STATE_VALUE_RESULTS = {
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
      20261111,
      20261112,
      20261113
    ],
    "eval_seeds": [
      20261121,
      20261122,
      20261123,
      20261124,
      20261125
    ],
    "hours": 96.0,
    "step_hours": 0.1,
    "population": 14,
    "epochs": 36,
    "hidden_size": 64,
    "action_epochs": 52,
    "action_hidden_size": 64,
    "value_epochs": 80,
    "value_hidden_size": 64,
    "max_value_examples": 120000,
    "value_bias_candidates": [
      0.0,
      0.75,
      1.25,
      1.75,
      2.5
    ],
    "device": "auto",
    "trace_seed": 20261121
  },
  "value_context_names": [
    "elapsed_fraction",
    "remaining_fraction",
    "env_progress",
    "social_progress",
    "env_response_rate",
    "social_response_rate",
    "current_env_fraction",
    "current_social_fraction",
    "candidate_is_environment",
    "candidate_is_social",
    "candidate_is_none"
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
      "phase": "train",
      "seed": 20260914,
      "crisis_count": 7,
      "first_crisis_hour": 16.0,
      "last_crisis_hour": 86.127,
      "profile_sequence": "contaminated_water_trust;quarantine_rumor;contaminated_water_trust;quarantine_rumor;storm_shelter_coordination;quarantine_rumor;route_migration_dispute"
    },
    {
      "phase": "train",
      "seed": 20260915,
      "crisis_count": 6,
      "first_crisis_hour": 15.614,
      "last_crisis_hour": 85.077,
      "profile_sequence": "storm_shelter_coordination;quarantine_rumor;route_migration_dispute;storm_shelter_coordination;quarantine_rumor;route_migration_dispute"
    },
    {
      "phase": "train",
      "seed": 20260916,
      "crisis_count": 6,
      "first_crisis_hour": 17.318,
      "last_crisis_hour": 85.764,
      "profile_sequence": "storm_shelter_coordination;route_migration_dispute;contaminated_water_trust;route_migration_dispute;quarantine_rumor;route_migration_dispute"
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
      "phase": "tune",
      "seed": 20261113,
      "crisis_count": 5,
      "first_crisis_hour": 14.44,
      "last_crisis_hour": 72.786,
      "profile_sequence": "route_migration_dispute;quarantine_rumor;storm_shelter_coordination;quarantine_rumor;route_migration_dispute"
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
    },
    {
      "phase": "eval",
      "seed": 20261124,
      "crisis_count": 6,
      "first_crisis_hour": 15.12,
      "last_crisis_hour": 82.375,
      "profile_sequence": "quarantine_rumor;contaminated_water_trust;route_migration_dispute;storm_shelter_coordination;contaminated_water_trust;quarantine_rumor"
    },
    {
      "phase": "eval",
      "seed": 20261125,
      "crisis_count": 6,
      "first_crisis_hour": 13.72,
      "last_crisis_hour": 79.563,
      "profile_sequence": "contaminated_water_trust;route_migration_dispute;storm_shelter_coordination;quarantine_rumor;contaminated_water_trust;storm_shelter_coordination"
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
      "tune_total_score": 0.5146973752996696,
      "tune_maturation_score": 0.9898026448070572,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.5736786435000576,
      "selection_objective": 0.1999616465996581,
      "selected": false
    },
    {
      "router": "balanced",
      "social_bias": 1.0,
      "environment_bias": 1.0,
      "infrastructure_bias": 1.0,
      "tool_bias": 1.0,
      "teaching_bias": 1.0,
      "tune_total_score": 0.5119628400761947,
      "tune_maturation_score": 0.9845439232234513,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.06666666666666667,
      "tune_coupled_response": 0.05272108843537415,
      "tune_damage": 1.3015187501153587,
      "selection_objective": 0.25769820569938157,
      "selected": false
    },
    {
      "router": "social_env",
      "social_bias": 1.55,
      "environment_bias": 1.45,
      "infrastructure_bias": 0.75,
      "tool_bias": 0.7,
      "teaching_bias": 1.2,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.5027682515509904,
      "selection_objective": 0.21944634968980192,
      "selected": false
    },
    {
      "router": "environment_first",
      "social_bias": 0.55,
      "environment_bias": 2.0,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.65,
      "teaching_bias": 0.55,
      "tune_total_score": 0.519368414117647,
      "tune_maturation_score": 0.9987854117647058,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.05555555555555555,
      "tune_coupled_response": 0.059574468085106386,
      "tune_damage": 1.3893188426617202,
      "selection_objective": 0.24724105220468828,
      "selected": false
    },
    {
      "router": "social_first",
      "social_bias": 2.0,
      "environment_bias": 0.55,
      "infrastructure_bias": 0.6,
      "tool_bias": 0.6,
      "teaching_bias": 1.35,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.18888888888888888,
      "tune_coupled_response": 0.08183166883774785,
      "tune_damage": 1.2890611654056088,
      "selection_objective": 0.2762590809054658,
      "selected": true
    },
    {
      "router": "build_tool",
      "social_bias": 0.45,
      "environment_bias": 0.7,
      "infrastructure_bias": 1.65,
      "tool_bias": 1.7,
      "teaching_bias": 0.55,
      "tune_total_score": 0.5159627607843137,
      "tune_maturation_score": 0.9922360784313726,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.18888888888888888,
      "tune_coupled_response": 0.13525112172528586,
      "tune_damage": 1.3003904550148937,
      "selection_objective": 0.27235985914786176,
      "selected": false
    },
    {
      "router": "teaching_tradition",
      "social_bias": 1.1,
      "environment_bias": 0.75,
      "infrastructure_bias": 0.7,
      "tool_bias": 0.7,
      "teaching_bias": 2.0,
      "tune_total_score": 0.5094429710444244,
      "tune_maturation_score": 0.9796980212392775,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.13333333333333333,
      "tune_coupled_response": 0.02806122448979592,
      "tune_damage": 1.2958681954865672,
      "selection_objective": 0.258865420382485,
      "selected": false
    },
    {
      "router": "high_pressure",
      "social_bias": 1.8,
      "environment_bias": 1.6,
      "infrastructure_bias": 1.3,
      "tool_bias": 1.25,
      "teaching_bias": 1.5,
      "tune_total_score": 0.5140281813333334,
      "tune_maturation_score": 0.9885157333333333,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.12222222222222223,
      "tune_coupled_response": 0.0,
      "tune_damage": 1.4074433058481137,
      "selection_objective": 0.23926174238593284,
      "selected": false
    }
  ],
  "base_training": [
    {
      "architecture": "frame_mlp",
      "train_loss": 1.9108881950378418,
      "train_accuracy": 0.2117511593758913,
      "device_used": "mps",
      "parameter_count": 9932,
      "train_sequences": 105,
      "train_steps": 94663
    },
    {
      "architecture": "gru",
      "train_loss": 1.8946750164031982,
      "train_accuracy": 0.22287482965889524,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_sequences": 105,
      "train_steps": 94663
    }
  ],
  "action_training": [
    {
      "head": "environment",
      "train_loss": 1.189071536064148,
      "accuracy": 0.49665695428848267,
      "crisis_accuracy": 0.49665695428848267,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 49356,
      "crisis_examples": 49356,
      "action_epochs": 52,
      "action_hidden_size": 64
    },
    {
      "head": "social",
      "train_loss": 0.0002957638062071055,
      "accuracy": 1.0,
      "crisis_accuracy": 1.0,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 49356,
      "crisis_examples": 49356,
      "action_epochs": 52,
      "action_hidden_size": 64
    }
  ],
  "value_training": {
    "examples": 120000,
    "epochs": 80,
    "final_loss": 0.007191484794020653,
    "target_mean": 0.024211062118411064,
    "target_std": 0.0932592824101448,
    "train_mae": 0.005470996256917715,
    "positive_rate": 0.6991583333333333
  },
  "value_example_summary": [
    {
      "source_policy": "return_selected",
      "examples": 120000,
      "mean_target": 0.024211061951406303,
      "positive_rate": 0.6991583333333333
    }
  ],
  "value_selection": [
    {
      "value_bias": 0.0,
      "tune_total_score": 0.5133131148652521,
      "tune_maturation_score": 0.9871406055101003,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.07312925170068027,
      "tune_social_response": 0.7772108843537415,
      "tune_coupled_response": 0.005952380952380952,
      "tune_damage": 1.7001180216235718,
      "selection_objective": -0.16408723368755262,
      "selected": false
    },
    {
      "value_bias": 0.75,
      "tune_total_score": 0.5155870133057504,
      "tune_maturation_score": 0.9915134871264432,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.0,
      "tune_env_response": 0.021971341728180632,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.021971341728180632,
      "tune_damage": 1.5879565967806901,
      "selection_objective": -0.12337627649800725,
      "selected": false
    },
    {
      "value_bias": 1.25,
      "tune_total_score": 0.5033617038806958,
      "tune_maturation_score": 0.9680032766936457,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.12222222222222223,
      "tune_env_response": 0.06323273990447242,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.06323273990447242,
      "tune_damage": 1.5090586739992007,
      "selection_objective": -0.004278466050454344,
      "selected": false
    },
    {
      "value_bias": 1.75,
      "tune_total_score": 0.5106806782242048,
      "tune_maturation_score": 0.9820782273542399,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.06666666666666667,
      "tune_env_response": 0.05683528730641193,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.05683528730641193,
      "tune_damage": 1.5735116848606021,
      "selection_objective": -0.05578284190909821,
      "selected": false
    },
    {
      "value_bias": 2.5,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.06666666666666667,
      "tune_env_response": 0.0705963236358373,
      "tune_social_response": 1.0,
      "tune_coupled_response": 0.0705963236358373,
      "tune_damage": 1.412293615549631,
      "selection_objective": -0.000910717536271588,
      "selected": true
    }
  ],
  "summary": [
    {
      "controller": "active_state_value_gru",
      "ablation": "body",
      "mean_total_score": 0.4955814995152716,
      "mean_maturation_score": 0.9530413452216759,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.06666666666666667,
      "mean_env_response_rate": 0.040830284139675654,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.040830284139675654,
      "mean_crisis_damage": 1.7225663200733776,
      "mean_final_alive": 13.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 3.4,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "environment",
      "mean_total_score": 0.5183331245692505,
      "mean_maturation_score": 0.9967944703254819,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.755667936320726,
      "mean_final_alive": 14.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.4,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.46122525323240665,
      "mean_maturation_score": 0.8869716408315513,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.10666666666666666,
      "mean_env_response_rate": 0.07401760650052133,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.07401760650052133,
      "mean_crisis_damage": 1.6099748290657323,
      "mean_final_alive": 13.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.6,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.2505173607124169,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "none",
      "mean_total_score": 0.5181349995688872,
      "mean_maturation_score": 0.9964134607093984,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.13999999999999999,
      "mean_env_response_rate": 0.08478656105347682,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.08478656105347682,
      "mean_crisis_damage": 1.5630019750648696,
      "mean_final_alive": 13.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.8,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.48757196816353404,
      "mean_maturation_score": 0.9376384003144885,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.03333333333333333,
      "mean_env_response_rate": 0.031104582502468392,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.031104582502468392,
      "mean_crisis_damage": 1.5962261438228924,
      "mean_final_alive": 11.4,
      "mean_alive_at_12h": 14.0,
      "mean_births": 0.6,
      "mean_architecture_tier": 3.2,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.4783143613226895,
      "mean_maturation_score": 0.9198353102359412,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.31059503297185526,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.786314083038867,
      "mean_final_alive": 13.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.4,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 2.4,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "active_state_value_gru",
      "ablation": "tools",
      "mean_total_score": 0.49645614880573313,
      "mean_maturation_score": 0.9547233630879483,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.015732032344039394,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.015732032344039394,
      "mean_crisis_damage": 1.6591189467430358,
      "mean_final_alive": 11.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.6,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 0.5196828742090884,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "designed",
      "ablation": "none",
      "mean_total_score": 0.7682771237479213,
      "mean_maturation_score": 0.9960704,
      "mean_crisis_score": 0.5215010744748363,
      "mean_resolved_rate": 1.0,
      "mean_env_response_rate": 0.07651766872896333,
      "mean_social_response_rate": 0.9234823312710366,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 0.05285407292903928,
      "mean_final_alive": 13.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.2,
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
      "mean_total_score": 0.6038471785673908,
      "mean_maturation_score": 0.9959347956712754,
      "mean_crisis_score": 0.17908559337151564,
      "mean_resolved_rate": 0.62,
      "mean_env_response_rate": 0.5886812686858183,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.5886812686858183,
      "mean_crisis_damage": 1.3554527108785557,
      "mean_final_alive": 15.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.2,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "frame_mlp",
      "ablation": "none",
      "mean_total_score": 0.3129160372359328,
      "mean_maturation_score": 0.6017616100691014,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.2799601968446953,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.7147978374947743,
      "mean_final_alive": 12.2,
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
      "mean_total_score": 0.5171962177225838,
      "mean_maturation_score": 0.9946081110049689,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.03333333333333333,
      "mean_env_response_rate": 0.0251063829787234,
      "mean_social_response_rate": 0.9472340425531914,
      "mean_coupled_response_rate": 0.005957446808510639,
      "mean_crisis_damage": 1.7472009061490918,
      "mean_final_alive": 14.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "reactive",
      "ablation": "none",
      "mean_total_score": 0.11704325473635832,
      "mean_maturation_score": 0.2250831821853045,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.17901013908748212,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.4065381446669476,
      "mean_final_alive": 2.8,
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
      "mean_total_score": 0.5196052841781476,
      "mean_maturation_score": 0.9992409311118223,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.03333333333333333,
      "mean_env_response_rate": 0.0934896327415639,
      "mean_social_response_rate": 0.666016702113831,
      "mean_coupled_response_rate": 0.026326963906581742,
      "mean_crisis_damage": 1.8838053371399819,
      "mean_final_alive": 15.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.2,
      "mean_architecture_tier": 3.0,
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
      "mean_total_score": 0.4955814995152716,
      "total_loss": 0.022553500053615616,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.07333333333333332,
      "env_response_loss": 0.04395627691380116,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.04395627691380116,
      "damage_increase": 0.15956434500850802
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.46122525323240665,
      "total_loss": 0.05690974633648055,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.033333333333333326,
      "env_response_loss": 0.010768954552955484,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.010768954552955484,
      "damage_increase": 0.04697285400086271
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.49645614880573313,
      "total_loss": 0.021678850763154067,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.13999999999999999,
      "env_response_loss": 0.06905452870943743,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.06905452870943743,
      "damage_increase": 0.09611697167816624
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.4783143613226895,
      "total_loss": 0.03982063824619769,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.13999999999999999,
      "env_response_loss": -0.22580847191837844,
      "social_response_loss": 1.0,
      "coupled_response_loss": 0.08478656105347682,
      "damage_increase": 1.2233121079739973
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.5183331245692505,
      "total_loss": -0.00019812500036331393,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.13999999999999999,
      "env_response_loss": 0.08478656105347682,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.08478656105347682,
      "damage_increase": 0.19266596125585633
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.48757196816353404,
      "total_loss": 0.030563031405353158,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.10666666666666666,
      "env_response_loss": 0.053681978551008425,
      "social_response_loss": 0.0,
      "coupled_response_loss": 0.053681978551008425,
      "damage_increase": 0.03322416875802281
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_value_bias": 2.5,
    "value_examples": 120000,
    "active_value_total_score": 0.5181349995688872,
    "fixed_joint_total_score": 0.6038471785673908,
    "return_selected_total_score": 0.5196052841781476,
    "active_value_crisis_score": 0.0,
    "fixed_joint_crisis_score": 0.17908559337151564,
    "return_selected_crisis_score": 0.0,
    "active_value_resolved_rate": 0.13999999999999999,
    "fixed_joint_resolved_rate": 0.62,
    "return_selected_resolved_rate": 0.03333333333333333,
    "active_value_coupled_response": 0.08478656105347682,
    "fixed_joint_coupled_response": 0.5886812686858183,
    "return_selected_coupled_response": 0.026326963906581742,
    "gain_over_return_selected": -0.0014702846092603528,
    "gain_over_fixed_joint": -0.08571217899850359,
    "social_culture_crisis_loss": 0.0,
    "environment_crisis_loss": 0.0,
    "social_culture_coupled_loss": 0.08478656105347682,
    "environment_coupled_loss": 0.08478656105347682,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "mean_crisis_count": 5.8,
    "supports_return_baseline_improvement": false,
    "supports_fixed_joint_improvement": false,
    "supports_active_state_value": false,
    "supports_social_environment_dependency": true,
    "verdict": "partial_or_failed"
  },
  "trace": {
    "seed": 20261121,
    "condition": "active_state_value_gru",
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
        "food": 0.7411109807472848,
        "water": 0.7117999913839317,
        "materials": 0.6466196544683094,
        "medicine": 0.3116325970750842,
        "shelter": 0.5121780066768075,
        "architecture": 0.15270104666175355,
        "architecture_tier": 0,
        "tools": 0.2679706261647953,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.09822760525716628,
        "granary": 0.10795481950612543,
        "paths": 0.08102565304913079,
        "sanitation": 0.10080161186677863,
        "garden": 0.22,
        "culture": 0.06,
        "symbols": 0.05,
        "risk_memory": 0.07,
        "map_knowledge": 0.1,
        "contamination": 0.17691565105865975,
        "disease": 0.13490193826526903,
        "predators": 0.17873141748956942,
        "route_hazard": 0.21483042511847328,
        "resource_migration": 0.24327844521533898,
        "adaptive_pressure": 0.1,
        "pressure_integral": 0.0,
        "adaptation_evidence": 0.0,
        "knowledge_transfer": 0.0,
        "mean_wisdom": 0.1325503820677441,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.7634790809826905,
        "mean_age": 28.77614728959912,
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
        "food": 0.7150857237475468,
        "water": 0.6398536327561923,
        "materials": 0.40107662032659785,
        "medicine": 0.3116325970750842,
        "shelter": 1.0,
        "architecture": 0.7309928539037962,
        "architecture_tier": 2,
        "tools": 0.2129506261647952,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 0.5896994926820018,
        "granary": 0.5532123832219902,
        "paths": 0.5269504799530326,
        "sanitation": 0.10080161186677863,
        "garden": 0.5327548374521679,
        "culture": 0.0658407336190382,
        "symbols": 0.054218307613749815,
        "risk_memory": 0.08658739574892356,
        "map_knowledge": 0.12101695308090062,
        "contamination": 0.15556585618108373,
        "disease": 0.10415520536207308,
        "predators": 0.1643652355746093,
        "route_hazard": 0.10426963747463425,
        "resource_migration": 0.241998138896036,
        "adaptive_pressure": 0.1341768897556284,
        "pressure_integral": 0.0063295415215087235,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.00551624841798053,
        "mean_wisdom": 0.1364670242498612,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.7172511959736442,
        "mean_age": 31.77614728959916,
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
        "next_shock": 196.0,
        "weather": "hot",
        "food": 0.7884155235198942,
        "water": 0.6565671001108637,
        "materials": 0.17075728254545564,
        "medicine": 0.3116325970750842,
        "shelter": 1.0,
        "architecture": 1.0,
        "architecture_tier": 4,
        "tools": 0.15793062616479514,
        "tool_tier": 1,
        "workshop": 0.1,
        "waterworks": 1.0,
        "granary": 0.9956596957861303,
        "paths": 0.9697543108270141,
        "sanitation": 0.10080161186677863,
        "garden": 0.8432261667319914,
        "culture": 0.06848228385536667,
        "symbols": 0.05586927651145512,
        "risk_memory": 0.08630910142637425,
        "map_knowledge": 0.11983575489422556,
        "contamination": 0.07908103823249228,
        "disease": 0.0697728730473543,
        "predators": 0.12264731677617463,
        "route_hazard": 0.029736891502932798,
        "resource_migration": 0.26192812443311886,
        "adaptive_pressure": 0.11246819206641077,
        "pressure_integral": 0.010814753703509412,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.00551624841798053,
        "mean_wisdom": 0.13990340374159574,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.6726711959736446,
        "mean_age": 34.7761472895992,
        "actions": {
          "construct": 12,
          "social_repair": 2
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
        "food": 0.9160719763892765,
        "water": 0.7147173072808997,
        "materials": 0.051986828531810636,
        "medicine": 0.3116325970750842,
        "shelter": 1.0,
        "architecture": 0.997322676593736,
        "architecture_tier": 4,
        "tools": 0.438069809468987,
        "tool_tier": 3,
        "workshop": 0.3575009292649574,
        "waterworks": 1.0,
        "granary": 0.999843700882219,
        "paths": 0.9995081541244811,
        "sanitation": 0.10080161186677863,
        "garden": 0.8716424140784655,
        "culture": 0.2985680328832494,
        "symbols": 0.19967286965388192,
        "risk_memory": 0.08574443689740835,
        "map_knowledge": 0.11845204650490236,
        "contamination": 0.0,
        "disease": 0.021930883733145903,
        "predators": 0.06809677366415419,
        "route_hazard": 0.011815664010860347,
        "resource_migration": 0.24782889519281223,
        "adaptive_pressure": 0.10378928501436392,
        "pressure_integral": 0.015285360803084857,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.00551624841798053,
        "mean_wisdom": 0.14291148659208375,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.6280911959736449,
        "mean_age": 37.776147289599244,
        "actions": {
          "improve_tools": 3,
          "social_repair": 11
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
        "water": 0.7740444429405013,
        "materials": 0.0,
        "medicine": 0.3116325970750842,
        "shelter": 1.0,
        "architecture": 0.9937958627959174,
        "architecture_tier": 4,
        "tools": 0.6471453928346105,
        "tool_tier": 4,
        "workshop": 0.5444373407495269,
        "waterworks": 1.0,
        "granary": 0.999843700882219,
        "paths": 0.9989483955284125,
        "sanitation": 0.10080161186677863,
        "garden": 0.8716424140784655,
        "culture": 0.7162414741733063,
        "symbols": 0.4607187704601679,
        "risk_memory": 0.08498682791579901,
        "map_knowledge": 0.11737337161166643,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.18741183776119183,
        "adaptive_pressure": 0.07235773498923095,
        "pressure_integral": 0.0181977343488305,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 0.00551624841798053,
        "mean_wisdom": 0.14627775160796516,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.5835111959736452,
        "mean_age": 40.77614728959929,
        "actions": {
          "improve_tools": 3,
          "social_repair": 11
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
        "water": 0.8923582038672475,
        "materials": 0.006890635622434074,
        "medicine": 0.3116325970750842,
        "shelter": 1.0,
        "architecture": 0.9866883562042664,
        "architecture_tier": 4,
        "tools": 0.6106991480616625,
        "tool_tier": 4,
        "workshop": 0.5489497668715082,
        "waterworks": 1.0,
        "granary": 0.999843700882219,
        "paths": 0.997912915678366,
        "sanitation": 0.4690841072449176,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 0.9914441455661208,
        "map_knowledge": 0.14397206520425865,
        "contamination": 0.0012095863736589895,
        "disease": 0.0018766915857981901,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.11322443624678317,
        "adaptive_pressure": 0.07986846106799572,
        "pressure_integral": 0.02332691391953106,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.24351333597548394,
        "mean_health": 0.9175993712496983,
        "mean_energy": 0.4943511959736461,
        "mean_age": 46.77614728959937,
        "actions": {
          "sanitize": 4,
          "social_repair": 10
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.0517413526025404
      },
      {
        "label": "24h",
        "hours": 24.0,
        "alive": 16,
        "total_agents": 16,
        "children": 2,
        "births": 2,
        "deaths": 0,
        "major_shocks": 1,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 0.9986561496311743,
        "materials": 0.00857169175872399,
        "medicine": 0.3116325970750842,
        "shelter": 0.9544486445635083,
        "architecture": 0.9804506313841527,
        "architecture_tier": 4,
        "tools": 0.5658991480616608,
        "tool_tier": 4,
        "workshop": 0.5489497668715082,
        "waterworks": 1.0,
        "granary": 0.9998267833157285,
        "paths": 0.9970143437091149,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.14113674818012625,
        "contamination": 0.024969701912497137,
        "disease": 0.04312343533795264,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.034209664979076654,
        "adaptive_pressure": 0.05291344941686921,
        "pressure_integral": 0.028076336000740415,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.2393419316754109,
        "mean_health": 0.8812359167097057,
        "mean_energy": 0.4018139256057721,
        "mean_age": 46.52912887839951,
        "actions": {
          "learn": 2,
          "teach": 14
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis",
          "20.7h: new generation born",
          "21.7h: new generation born",
          "23.8h: unresolved quarantine rumor"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 1,
        "crisis_damage": 0.3504729335412749
      },
      {
        "label": "36h",
        "hours": 36.0,
        "alive": 17,
        "total_agents": 17,
        "children": 3,
        "births": 3,
        "deaths": 0,
        "major_shocks": 2,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.2894463410804533,
        "shelter": 0.6672793319145743,
        "architecture": 0.9723784917175216,
        "architecture_tier": 4,
        "tools": 0.6435378037004277,
        "tool_tier": 4,
        "workshop": 0.6940530495780087,
        "waterworks": 1.0,
        "granary": 0.999788186822499,
        "paths": 0.9928367528492378,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.13577344246411938,
        "contamination": 0.01369117163274113,
        "disease": 0.03104842319118971,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.10641914511423858,
        "adaptive_pressure": 0.05712863059359212,
        "pressure_integral": 0.03755654326510165,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.35647711405260174,
        "mean_health": 0.873909117684351,
        "mean_energy": 0.22170628610750862,
        "mean_age": 55.668591885552416,
        "actions": {
          "improve_tools": 2,
          "learn": 3,
          "teach": 12
        },
        "events": [
          "20.7h: new generation born",
          "21.7h: new generation born",
          "23.8h: unresolved quarantine rumor",
          "26.1h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.673333294203951
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
        "next_shock": 196.0,
        "weather": "cold",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.2513449735682415,
        "shelter": 0.6673680794707412,
        "architecture": 0.9600146971345317,
        "architecture_tier": 4,
        "tools": 0.9736499999999995,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9997856587502206,
        "paths": 0.9816987870201123,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 0.9981483457778922,
        "map_knowledge": 0.2238169511425015,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.23555920703077754,
        "adaptive_pressure": 0.08244859117401919,
        "pressure_integral": 0.047148206963435864,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5927808456885262,
        "mean_health": 0.8960645198786295,
        "mean_energy": 0.06595529880627146,
        "mean_age": 67.66859188555205,
        "actions": {
          "sanitize": 2,
          "social_repair": 13,
          "treat": 2
        },
        "events": [
          "21.7h: new generation born",
          "23.8h: unresolved quarantine rumor",
          "26.1h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.698165498668938
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
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.00499340636480075,
        "medicine": 0.21534013675738428,
        "shelter": 0.5699150187029237,
        "architecture": 0.9466694657227672,
        "architecture_tier": 3,
        "tools": 0.9770499999999995,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9997856587502206,
        "paths": 0.9761713574715405,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.5665105126682888,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2861253207220376,
        "adaptive_pressure": 0.06331542127341798,
        "pressure_integral": 0.055540035379505415,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.6952139715271661,
        "mean_health": 0.9157313741631404,
        "mean_energy": 0.017433019995473347,
        "mean_age": 79.66859188555152,
        "actions": {
          "social_repair": 13,
          "treat": 4
        },
        "events": [
          "26.1h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis",
          "52.7h: resolved quarantine rumor",
          "57.3h: coupled storm shelter coordination crisis"
        ],
        "active_crisis": "storm_shelter_coordination",
        "crisis_resolved": 1,
        "crisis_unresolved": 2,
        "crisis_damage": 0.7577611923705656
      },
      {
        "label": "72h",
        "hours": 72.0,
        "alive": 17,
        "total_agents": 17,
        "children": 0,
        "births": 3,
        "deaths": 0,
        "major_shocks": 5,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.019708981581605924,
        "medicine": 0.15269541898093444,
        "shelter": 0.35809657824708163,
        "architecture": 0.9385973260561363,
        "architecture_tier": 3,
        "tools": 0.9566499999999991,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.999763477035139,
        "paths": 0.9884506966195687,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.7576989474009171,
        "contamination": 0.0005649173194976787,
        "disease": 0.0008764777805539744,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2716482411782503,
        "adaptive_pressure": 0.06059373559199371,
        "pressure_integral": 0.06354368363216761,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.7171345346653385,
        "mean_health": 0.9354552027061885,
        "mean_energy": 0.0,
        "mean_age": 91.66859188555098,
        "actions": {
          "social_repair": 17
        },
        "events": [
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis",
          "52.7h: resolved quarantine rumor",
          "57.3h: coupled storm shelter coordination crisis",
          "65.1h: unresolved storm shelter coordination",
          "66.9h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 1,
        "crisis_unresolved": 3,
        "crisis_damage": 1.0869920610820474
      },
      {
        "label": "96h",
        "hours": 96.0,
        "alive": 15,
        "total_agents": 17,
        "children": 0,
        "births": 3,
        "deaths": 2,
        "major_shocks": 6,
        "next_shock": 196.0,
        "weather": "clear",
        "food": 1.0,
        "water": 1.0,
        "materials": 0.0,
        "medicine": 0.148511009594021,
        "shelter": 0.31092518189040486,
        "architecture": 0.9128883000613816,
        "architecture_tier": 3,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9997474045837471,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 0.8716424140784655,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.044538063496048205,
        "adaptive_pressure": 0.05999359088144534,
        "pressure_integral": 0.08469915830610952,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.7484536085684536,
        "mean_health": 0.9143311641820059,
        "mean_energy": 0.0,
        "mean_age": 112.99852131844287,
        "actions": {
          "improve_tools": 5,
          "sanitize": 7,
          "scout": 3
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
        "crisis_resolved": 1,
        "crisis_unresolved": 5,
        "crisis_damage": 1.451131387559426
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
    "20261121:active_state_value_gru:none": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.688888888888889,
        "social_fraction": 1.0,
        "coupled_fraction": 0.688888888888889,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:body": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.9066666666666667,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9066666666666667,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.9822222222222223,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9822222222222223,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:infrastructure": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:tools": [
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.7555555555555561,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7555555555555561,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 77.7,
        "end": 85.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.14625506072874492,
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
        "env_fraction": 0.01720647773279352,
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
        "env_fraction": 0.30364861428934653,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:environment": [
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261121:active_state_value_gru:previous_action": [
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:return_selected_gru:none": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.8061224489795923,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8061224489795923,
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
    "20261122:fixed_joint_gru:none": [
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:none": [
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
        "env_fraction": 0.6296296296296293,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6296296296296293,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:body": [
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
        "env_fraction": 0.009725400457665902,
        "social_fraction": 1.0,
        "coupled_fraction": 0.009725400457665902,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:infrastructure": [
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
        "env_fraction": 0.15347222222222218,
        "social_fraction": 1.0,
        "coupled_fraction": 0.15347222222222218,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:tools": [
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:social_culture": [
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
    "20261122:active_state_value_gru:environment": [
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
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261122:active_state_value_gru:previous_action": [
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
        "env_fraction": 0.7201388888888887,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7201388888888887,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
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
        "social_fraction": 1.0,
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
    "20261123:return_selected_gru:none": [
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
        "env_fraction": 0.8565051020408161,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8565051020408161,
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
    "20261123:fixed_joint_gru:none": [
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
    "20261123:active_state_value_gru:none": [
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
        "env_fraction": 0.021739130434782608,
        "social_fraction": 1.0,
        "coupled_fraction": 0.021739130434782608,
        "resolved": false
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
    "20261123:active_state_value_gru:body": [
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
        "env_fraction": 0.6965277777777776,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6965277777777776,
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
        "env_fraction": 0.53125,
        "social_fraction": 1.0,
        "coupled_fraction": 0.53125,
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
    "20261123:active_state_value_gru:infrastructure": [
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
        "env_fraction": 0.43115942028985477,
        "social_fraction": 1.0,
        "coupled_fraction": 0.43115942028985477,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.05037037037037037,
        "social_fraction": 1.0,
        "coupled_fraction": 0.05037037037037037,
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
        "env_fraction": 0.03777777777777778,
        "social_fraction": 1.0,
        "coupled_fraction": 0.03777777777777778,
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
    "20261123:active_state_value_gru:tools": [
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
    "20261123:active_state_value_gru:social_culture": [
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
        "env_fraction": 0.7559288537549406,
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
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.8069330329534409,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:active_state_value_gru:environment": [
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
    "20261123:active_state_value_gru:previous_action": [
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
        "env_fraction": 0.6995341614906827,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6995341614906827,
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
    "20261124:designed:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261124:reactive:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:frame_mlp:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:return_selected_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:fixed_joint_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.9598639455782298,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9598639455782298,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261124:active_state_value_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.7853260869565216,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7853260869565216,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:body": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.23129251700680273,
        "social_fraction": 1.0,
        "coupled_fraction": 0.23129251700680273,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.07391304347826087,
        "social_fraction": 1.0,
        "coupled_fraction": 0.07391304347826087,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.3148148148148148,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3148148148148148,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:infrastructure": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.023097826086956524,
        "social_fraction": 1.0,
        "coupled_fraction": 0.023097826086956524,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.15013586956521738,
        "social_fraction": 1.0,
        "coupled_fraction": 0.15013586956521738,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.6138888888888887,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6138888888888887,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.5658967391304346,
        "social_fraction": 1.0,
        "coupled_fraction": 0.5658967391304346,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.011548913043478262,
        "social_fraction": 1.0,
        "coupled_fraction": 0.011548913043478262,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.8413425925925923,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8413425925925923,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.02478134110787172,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:environment": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
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
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:active_state_value_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.7514492753623182,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7514492753623182,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 0.026984126984126982,
        "social_fraction": 1.0,
        "coupled_fraction": 0.026984126984126982,
        "resolved": false
      }
    ],
    "20261125:designed:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.9807692307692307,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9807692307692307,
        "resolved": true
      }
    ],
    "20261125:reactive:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:frame_mlp:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 0.1447368421052632,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:return_selected_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:fixed_joint_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:none": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.30818713450292384,
        "social_fraction": 1.0,
        "coupled_fraction": 0.30818713450292384,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:body": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.011564625850340137,
        "social_fraction": 1.0,
        "coupled_fraction": 0.011564625850340137,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.06296296296296297,
        "social_fraction": 1.0,
        "coupled_fraction": 0.06296296296296297,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:infrastructure": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.1451863354037267,
        "social_fraction": 1.0,
        "coupled_fraction": 0.1451863354037267,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0816326530612245,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0816326530612245,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.044444444444444446,
        "social_fraction": 1.0,
        "coupled_fraction": 0.044444444444444446,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:tools": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:social_culture": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:environment": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:active_state_value_gru:previous_action": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.7523291925465836,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7523291925465836,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ]
  },
  "notes": {
    "claim": "active crisis state/action value labels can guide repair choices during coupled crises",
    "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
    "remaining_structure": "candidate repair actions are supplied, action heads are supervised, and value labels are per-step simulator consequences rather than full delayed-return policy gradients"
  }
};
