window.SSRM_3D_COUPLED_CRISIS_TEMPORAL_RETURN_VALUE_RESULTS = {
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
      2.5,
      3.5
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
      "train_loss": 1.0086464881896973,
      "accuracy": 0.5696572065353394,
      "crisis_accuracy": 0.5696572065353394,
      "device_used": "mps",
      "parameter_count": 28236,
      "train_examples": 49356,
      "crisis_examples": 49356,
      "action_epochs": 52,
      "action_hidden_size": 64
    },
    {
      "head": "social",
      "train_loss": 0.00039639766328036785,
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
    "final_loss": 0.0007166634895838797,
    "target_mean": 0.5604713559150696,
    "target_std": 1.554236650466919,
    "train_mae": 0.03070034645497799,
    "positive_rate": 0.5292916666666667
  },
  "temporal_example_summary": [
    {
      "source_policy": "fixed_joint",
      "examples": 47258,
      "mean_target": 1.41713625070023,
      "positive_rate": 0.7970502348808667
    },
    {
      "source_policy": "high_env_joint",
      "examples": 24473,
      "mean_target": 1.50313550704621,
      "positive_rate": 0.8330813549626118
    },
    {
      "source_policy": "return_selected",
      "examples": 48269,
      "mean_target": -0.7561933859831893,
      "positive_rate": 0.11311607864260706
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
      "selection_objective": -0.25900225420889345,
      "selected": false
    },
    {
      "value_bias": 0.75,
      "tune_total_score": 0.5106901973333333,
      "tune_maturation_score": 0.9820965333333334,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.24444444444444446,
      "tune_env_response": 0.24669633810971195,
      "tune_social_response": 0.45647344044000576,
      "tune_coupled_response": 0.12900202634245186,
      "tune_damage": 1.591253649264263,
      "selection_objective": 0.03948789159894461,
      "selected": false
    },
    {
      "value_bias": 1.25,
      "tune_total_score": 0.5040142293333333,
      "tune_maturation_score": 0.9692581333333333,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.12222222222222223,
      "tune_env_response": 0.16542553191489362,
      "tune_social_response": 0.4672998986828774,
      "tune_coupled_response": 0.08321754233608337,
      "tune_damage": 1.7689298799813074,
      "selection_objective": -0.13828689533669158,
      "selected": false
    },
    {
      "value_bias": 1.75,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.18888888888888888,
      "tune_env_response": 0.20005065856129686,
      "tune_social_response": 0.4269829208279057,
      "tune_coupled_response": 0.1141156462585034,
      "tune_damage": 1.5810653596874342,
      "selection_objective": -0.003487181602375433,
      "selected": false
    },
    {
      "value_bias": 2.5,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.37777777777777777,
      "tune_env_response": 0.2556158633666233,
      "tune_social_response": 0.4822622666087712,
      "tune_coupled_response": 0.1328303661890288,
      "tune_damage": 1.4828766352551197,
      "selection_objective": 0.17278913949535102,
      "selected": true
    },
    {
      "value_bias": 3.5,
      "tune_total_score": 0.52,
      "tune_maturation_score": 1.0,
      "tune_crisis_score": 0.0,
      "tune_resolved_rate": 0.17777777777777778,
      "tune_env_response": 0.20470039079461574,
      "tune_social_response": 0.37673324649008544,
      "tune_coupled_response": 0.07146475611521204,
      "tune_damage": 1.7295538186825397,
      "selection_objective": -0.08907919139045206,
      "selected": false
    }
  ],
  "summary": [
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
      "mean_total_score": 0.6522779582843417,
      "mean_maturation_score": 0.99696096,
      "mean_crisis_score": 0.2788713730923786,
      "mean_resolved_rate": 0.6866666666666668,
      "mean_env_response_rate": 0.6303492398450097,
      "mean_social_response_rate": 1.0,
      "mean_coupled_response_rate": 0.6303492398450097,
      "mean_crisis_damage": 1.1810568957051228,
      "mean_final_alive": 15.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.2,
      "mean_architecture_tier": 3.8,
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
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "body",
      "mean_total_score": 0.5087019005947448,
      "mean_maturation_score": 0.9782728857591246,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.17333333333333334,
      "mean_env_response_rate": 0.2007026005957336,
      "mean_social_response_rate": 0.20454113668776902,
      "mean_coupled_response_rate": 0.08486438348208236,
      "mean_crisis_damage": 2.2850093670001117,
      "mean_final_alive": 15.2,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 3.4,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "environment",
      "mean_total_score": 0.52,
      "mean_maturation_score": 1.0,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.0,
      "mean_social_response_rate": 0.982229686562252,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 1.7692725729247634,
      "mean_final_alive": 14.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 4.0,
      "mean_architecture_tier": 3.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "infrastructure",
      "mean_total_score": 0.4511120048032874,
      "mean_maturation_score": 0.8675230861601682,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.21333333333333332,
      "mean_env_response_rate": 0.38724177731805554,
      "mean_social_response_rate": 0.29188462754664135,
      "mean_coupled_response_rate": 0.10008058813713858,
      "mean_crisis_damage": 2.168273388483599,
      "mean_final_alive": 13.8,
      "mean_alive_at_12h": 14.0,
      "mean_births": 3.0,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 0.0,
      "mean_knowledge_transfer": 0.19075248056231314,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "none",
      "mean_total_score": 0.517827648,
      "mean_maturation_score": 0.9958224,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.27999999999999997,
      "mean_env_response_rate": 0.18225147112646387,
      "mean_social_response_rate": 0.46572374904698294,
      "mean_coupled_response_rate": 0.08519693688560938,
      "mean_crisis_damage": 1.7986712996757397,
      "mean_final_alive": 14.2,
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
      "controller": "temporal_return_value_gru",
      "ablation": "previous_action",
      "mean_total_score": 0.5027231570595032,
      "mean_maturation_score": 0.9667753020375061,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.27999999999999997,
      "mean_env_response_rate": 0.16565085879859465,
      "mean_social_response_rate": 0.45624139749408366,
      "mean_coupled_response_rate": 0.07555375016248538,
      "mean_crisis_damage": 1.6647654255576214,
      "mean_final_alive": 12.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 1.2,
      "mean_architecture_tier": 3.8,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "social_culture",
      "mean_total_score": 0.5168840864883767,
      "mean_maturation_score": 0.9940078586314935,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.0,
      "mean_env_response_rate": 0.37794363117248525,
      "mean_social_response_rate": 0.0,
      "mean_coupled_response_rate": 0.0,
      "mean_crisis_damage": 2.5695028450296418,
      "mean_final_alive": 20.0,
      "mean_alive_at_12h": 14.0,
      "mean_births": 9.8,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 3.6,
      "mean_knowledge_transfer": 1.0,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    },
    {
      "controller": "temporal_return_value_gru",
      "ablation": "tools",
      "mean_total_score": 0.5061795716528592,
      "mean_maturation_score": 0.9734222531785754,
      "mean_crisis_score": 0.0,
      "mean_resolved_rate": 0.31333333333333335,
      "mean_env_response_rate": 0.25287833279402017,
      "mean_social_response_rate": 0.277394748657018,
      "mean_coupled_response_rate": 0.12991689506809637,
      "mean_crisis_damage": 1.7915294489430842,
      "mean_final_alive": 12.6,
      "mean_alive_at_12h": 14.0,
      "mean_births": 2.4,
      "mean_architecture_tier": 4.0,
      "mean_tool_tier": 4.0,
      "mean_knowledge_transfer": 0.9019519322932709,
      "mean_adaptation_evidence": 1.0,
      "shock_gate_pass_rate": 1.0,
      "post_gate_shock_rate": 1.0
    }
  ],
  "ablations": [
    {
      "ablation": "body",
      "mean_total_score": 0.5087019005947448,
      "total_loss": 0.00912574740525518,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.10666666666666663,
      "env_response_loss": -0.018451129469269745,
      "social_response_loss": 0.2611826123592139,
      "coupled_response_loss": 0.0003325534035270167,
      "damage_increase": 0.486338067324372
    },
    {
      "ablation": "infrastructure",
      "mean_total_score": 0.4511120048032874,
      "total_loss": 0.06671564319671264,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.06666666666666665,
      "env_response_loss": -0.20499030619159167,
      "social_response_loss": 0.1738391215003416,
      "coupled_response_loss": -0.014883651251529198,
      "damage_increase": 0.3696020888078595
    },
    {
      "ablation": "tools",
      "mean_total_score": 0.5061795716528592,
      "total_loss": 0.011648076347140823,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": -0.03333333333333338,
      "env_response_loss": -0.0706268616675563,
      "social_response_loss": 0.18832900038996492,
      "coupled_response_loss": -0.04471995818248699,
      "damage_increase": -0.007141850732655497
    },
    {
      "ablation": "social_culture",
      "mean_total_score": 0.5168840864883767,
      "total_loss": 0.0009435615116233365,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.27999999999999997,
      "env_response_loss": -0.19569216004602139,
      "social_response_loss": 0.46572374904698294,
      "coupled_response_loss": 0.08519693688560938,
      "damage_increase": 0.7708315453539021
    },
    {
      "ablation": "environment",
      "mean_total_score": 0.52,
      "total_loss": -0.0021723519999999885,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.27999999999999997,
      "env_response_loss": 0.18225147112646387,
      "social_response_loss": -0.516505937515269,
      "coupled_response_loss": 0.08519693688560938,
      "damage_increase": -0.029398726750976323
    },
    {
      "ablation": "previous_action",
      "mean_total_score": 0.5027231570595032,
      "total_loss": 0.015104490940496818,
      "crisis_score_loss": 0.0,
      "resolved_rate_loss": 0.0,
      "env_response_loss": 0.01660061232786922,
      "social_response_loss": 0.009482351552899282,
      "coupled_response_loss": 0.009643186723124003,
      "damage_increase": -0.13390587411811827
    }
  ],
  "verdict": {
    "selected_router": "social_first",
    "selected_value_bias": 2.5,
    "temporal_value_examples": 120000,
    "temporal_value_total_score": 0.517827648,
    "fixed_joint_total_score": 0.6522779582843417,
    "return_selected_total_score": 0.5196052841781476,
    "temporal_value_crisis_score": 0.0,
    "fixed_joint_crisis_score": 0.2788713730923786,
    "return_selected_crisis_score": 0.0,
    "temporal_value_resolved_rate": 0.27999999999999997,
    "fixed_joint_resolved_rate": 0.6866666666666668,
    "return_selected_resolved_rate": 0.03333333333333333,
    "temporal_value_coupled_response": 0.08519693688560938,
    "fixed_joint_coupled_response": 0.6303492398450097,
    "return_selected_coupled_response": 0.026326963906581742,
    "gain_over_return_selected": -0.0017776361781475236,
    "gain_over_fixed_joint": -0.13445031028434162,
    "social_culture_crisis_loss": 0.0,
    "environment_crisis_loss": 0.0,
    "social_culture_coupled_loss": 0.08519693688560938,
    "environment_coupled_loss": 0.08519693688560938,
    "shock_gate_pass_rate": 1.0,
    "post_gate_shock_rate": 1.0,
    "survival_at_12h": 14.0,
    "mean_crisis_count": 5.8,
    "supports_return_baseline_improvement": false,
    "supports_fixed_joint_improvement": false,
    "supports_temporal_return_value": false,
    "supports_social_environment_dependency": false,
    "verdict": "partial_or_failed"
  },
  "trace": {
    "seed": 20261121,
    "condition": "temporal_return_value_gru",
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
        "water": 0.8923659439086521,
        "materials": 0.0,
        "medicine": 0.2994129726666149,
        "shelter": 1.0,
        "architecture": 0.9995413018233638,
        "architecture_tier": 4,
        "tools": 0.6400574953534357,
        "tool_tier": 4,
        "workshop": 0.5728034240460738,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 0.9999254124084253,
        "sanitation": 0.19776383824876415,
        "garden": 0.9948511502985331,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.11831152108461099,
        "contamination": 0.0006547126244725644,
        "disease": 0.0010157965567574334,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.11507591305987427,
        "adaptive_pressure": 0.08043587252986918,
        "pressure_integral": 0.023342638812557458,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.25048920566989624,
        "mean_health": 0.9263276743986049,
        "mean_energy": 0.4943511959736461,
        "mean_age": 46.77614728959937,
        "actions": {
          "improve_tools": 4,
          "learn": 1,
          "sanitize": 1,
          "teach": 8
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 0,
        "crisis_damage": 0.045564895342901555
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
        "materials": 0.0,
        "medicine": 0.29826089664505995,
        "shelter": 0.9772219858449341,
        "architecture": 0.9957672842274046,
        "architecture_tier": 4,
        "tools": 0.7494917806756274,
        "tool_tier": 4,
        "workshop": 0.6966562808703564,
        "waterworks": 1.0,
        "granary": 0.9999944809820159,
        "paths": 0.99953573061728,
        "sanitation": 1.0,
        "garden": 0.9961777618807701,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.11596213190697072,
        "contamination": 0.005906133806880794,
        "disease": 0.01488208332150344,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.035971290208716165,
        "adaptive_pressure": 0.05305798721049771,
        "pressure_integral": 0.0281441968581499,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.2655298034055846,
        "mean_health": 0.907393447246663,
        "mean_energy": 0.40418340569967365,
        "mean_age": 49.39107080362615,
        "actions": {
          "improve_tools": 9,
          "learn": 1,
          "teach": 5
        },
        "events": [
          "16.0h: coupled quarantine rumor crisis",
          "22.0h: new generation born",
          "23.8h: unresolved quarantine rumor"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 1,
        "crisis_damage": 0.29990428624544285
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
        "medicine": 0.0,
        "shelter": 0.7600133636794376,
        "architecture": 0.9996993345170444,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9999832660721136,
        "paths": 0.9997123994378281,
        "sanitation": 1.0,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.11541370366963481,
        "contamination": 0.004364203078923842,
        "disease": 0.020966004589256064,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.10736019055131533,
        "adaptive_pressure": 0.05998400933718724,
        "pressure_integral": 0.03794227088249699,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.3140801978963827,
        "mean_health": 0.9795066398513063,
        "mean_energy": 0.22856664147956188,
        "mean_age": 55.28623894437595,
        "actions": {
          "improve_tools": 9,
          "learn": 3,
          "teach": 5
        },
        "events": [
          "22.0h: new generation born",
          "23.8h: unresolved quarantine rumor",
          "25.1h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "27.9h: new generation born",
          "35.6h: unresolved storm shelter coordination"
        ],
        "active_crisis": null,
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.7392253006575981
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
        "materials": 0.0011322932774940001,
        "medicine": 0.0,
        "shelter": 0.8167535076762825,
        "architecture": 0.9997611787012477,
        "architecture_tier": 4,
        "tools": 0.9934512907570523,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.8857018566926722,
        "contamination": 0.0010624734237110612,
        "disease": 0.0016484436149698891,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.1807718111202407,
        "adaptive_pressure": 0.06929314556618772,
        "pressure_integral": 0.04744841648093973,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.4397334617320268,
        "mean_health": 0.9834745514842997,
        "mean_energy": 0.07104979670171258,
        "mean_age": 67.28623894437557,
        "actions": {
          "learn": 6,
          "sanitize": 2,
          "social_repair": 4,
          "teach": 5
        },
        "events": [
          "23.8h: unresolved quarantine rumor",
          "25.1h: new generation born",
          "27.8h: coupled storm shelter coordination crisis",
          "27.9h: new generation born",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis"
        ],
        "active_crisis": "quarantine_rumor",
        "crisis_resolved": 0,
        "crisis_unresolved": 2,
        "crisis_damage": 0.8183282924982235
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
        "materials": 0.01618396458475492,
        "medicine": 0.0,
        "shelter": 0.7045992582144283,
        "architecture": 0.9915538330013095,
        "architecture_tier": 4,
        "tools": 0.9802499999999995,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 0.9999889916467861,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 0.9923469859018744,
        "contamination": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.24966383611591572,
        "adaptive_pressure": 0.0614636636180411,
        "pressure_integral": 0.05409799775375743,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.4800337106815507,
        "mean_health": 0.9988672844171639,
        "mean_energy": 0.024880517322157285,
        "mean_age": 79.28623894437503,
        "actions": {
          "treat": 17
        },
        "events": [
          "27.8h: coupled storm shelter coordination crisis",
          "27.9h: new generation born",
          "35.6h: unresolved storm shelter coordination",
          "44.9h: coupled quarantine rumor crisis",
          "52.7h: unresolved quarantine rumor",
          "57.3h: coupled storm shelter coordination crisis"
        ],
        "active_crisis": "storm_shelter_coordination",
        "crisis_resolved": 0,
        "crisis_unresolved": 3,
        "crisis_damage": 1.1181203835956575
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
        "materials": 0.0,
        "medicine": 0.0,
        "shelter": 1.0,
        "architecture": 0.999479980167348,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 1.0,
        "garden": 1.0,
        "culture": 1.0,
        "symbols": 1.0,
        "risk_memory": 1.0,
        "map_knowledge": 1.0,
        "contamination": 0.00019411251519637588,
        "disease": 0.0003011685084258923,
        "predators": 0.0,
        "route_hazard": 0.0,
        "resource_migration": 0.2511134713395807,
        "adaptive_pressure": 0.05293433792285466,
        "pressure_integral": 0.06118247351703149,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5043381282080164,
        "mean_health": 0.9946839743715721,
        "mean_energy": 0.0,
        "mean_age": 91.28623894437452,
        "actions": {
          "improve_tools": 13,
          "learn": 1,
          "scout": 3
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
        "crisis_damage": 1.6575984256346674
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
        "medicine": 0.0,
        "shelter": 1.0,
        "architecture": 0.981656667381487,
        "architecture_tier": 4,
        "tools": 1.0,
        "tool_tier": 4,
        "workshop": 1.0,
        "waterworks": 1.0,
        "granary": 1.0,
        "paths": 1.0,
        "sanitation": 1.0,
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
        "adaptive_pressure": 0.0521254886278472,
        "pressure_integral": 0.07989834619641946,
        "adaptation_evidence": 1.0,
        "knowledge_transfer": 1.0,
        "mean_wisdom": 0.5667161251123187,
        "mean_health": 1.0,
        "mean_energy": 0.0,
        "mean_age": 112.56518798510955,
        "actions": {
          "improve_tools": 2,
          "sanitize": 10,
          "scout": 3
        },
        "events": [
          "57.3h: coupled storm shelter coordination crisis",
          "65.1h: unresolved storm shelter coordination",
          "66.9h: coupled quarantine rumor crisis",
          "74.8h: unresolved quarantine rumor",
          "77.7h: coupled contaminated water trust crisis",
          "85.6h: resolved contaminated water trust"
        ],
        "active_crisis": null,
        "crisis_resolved": 1,
        "crisis_unresolved": 5,
        "crisis_damage": 1.8330159499989414
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
        "env_fraction": 0.31402777777777774,
        "social_fraction": 1.0,
        "coupled_fraction": 0.31402777777777774,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.32692307692307676,
        "social_fraction": 1.0,
        "coupled_fraction": 0.32692307692307676,
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
        "env_fraction": 0.2724358974358974,
        "social_fraction": 1.0,
        "coupled_fraction": 0.2724358974358974,
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
    "20261121:temporal_return_value_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.4965079365079364,
        "social_fraction": 1.0,
        "coupled_fraction": 0.4965079365079364,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.31730769230769224,
        "social_fraction": 1.0,
        "coupled_fraction": 0.31730769230769224,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.40000000000000013,
        "social_fraction": 1.0,
        "coupled_fraction": 0.40000000000000013,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.34481424148606815,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.8444444444444444,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8444444444444444,
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
    "20261121:temporal_return_value_gru:body": [
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
        "env_fraction": 0.00908119658119658,
        "social_fraction": 1.0,
        "coupled_fraction": 0.00908119658119658,
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
        "env_fraction": 0.8623188405797102,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8623188405797102,
        "resolved": false
      }
    ],
    "20261121:temporal_return_value_gru:infrastructure": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
        "env_fraction": 1.0,
        "social_fraction": 0.02554179566563467,
        "coupled_fraction": 0.02554179566563467,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.8111111111111114,
        "social_fraction": 0.0,
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
    "20261121:temporal_return_value_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.6090542328042327,
        "social_fraction": 0.2831133540372671,
        "coupled_fraction": 0.2831133540372671,
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
        "env_fraction": 0.7777777777777779,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7777777777777779,
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
        "env_fraction": 1.0,
        "social_fraction": 0.03164961636828645,
        "coupled_fraction": 0.03164961636828645,
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
    "20261121:temporal_return_value_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 0.822116402116402,
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
        "env_fraction": 1.0,
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
    "20261121:temporal_return_value_gru:environment": [
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
    "20261121:temporal_return_value_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 16.0,
        "end": 23.8,
        "env_fraction": 1.0,
        "social_fraction": 0.9607919254658386,
        "coupled_fraction": 0.9607919254658386,
        "resolved": true
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 27.8,
        "end": 35.6,
        "env_fraction": 0.35144230769230766,
        "social_fraction": 1.0,
        "coupled_fraction": 0.35144230769230766,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 44.9,
        "end": 52.7,
        "env_fraction": 0.4722222222222221,
        "social_fraction": 1.0,
        "coupled_fraction": 0.4722222222222221,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 57.3,
        "end": 65.1,
        "env_fraction": 0.0,
        "social_fraction": 0.14925986842105265,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 66.9,
        "end": 74.8,
        "env_fraction": 0.6965277777777776,
        "social_fraction": 1.0,
        "coupled_fraction": 0.6965277777777776,
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
    "20261122:temporal_return_value_gru:none": [
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
        "env_fraction": 0.3358024691358024,
        "social_fraction": 1.0,
        "coupled_fraction": 0.3358024691358024,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.020531400966183576,
        "social_fraction": 0.3011904761904761,
        "coupled_fraction": 0.020531400966183576,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.45294784580498854,
        "social_fraction": 0.0763888888888889,
        "coupled_fraction": 0.0763888888888889,
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
    "20261122:temporal_return_value_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 15.3,
        "end": 23.1,
        "env_fraction": 0.479057720422852,
        "social_fraction": 0.0,
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
        "env_fraction": 0.0,
        "social_fraction": 0.1178571428571429,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.3556122448979593,
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
    "20261122:temporal_return_value_gru:infrastructure": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.07857142857142858,
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
    "20261122:temporal_return_value_gru:tools": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.0,
        "social_fraction": 0.20625000000000002,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 63.0,
        "end": 70.9,
        "env_fraction": 0.14094387755102042,
        "social_fraction": 0.014322916666666668,
        "coupled_fraction": 0.014322916666666668,
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
    "20261122:temporal_return_value_gru:social_culture": [
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
        "env_fraction": 0.8980092592592585,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 46.9,
        "end": 54.7,
        "env_fraction": 0.3002717391304347,
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
    "20261122:temporal_return_value_gru:environment": [
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
    "20261122:temporal_return_value_gru:previous_action": [
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
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
        "social_fraction": 0.5958333333333335,
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
    "20261123:temporal_return_value_gru:none": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.9192765567765567,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9192765567765567,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.8752860411899314,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8752860411899314,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 0.44736842105263175,
        "social_fraction": 1.0,
        "coupled_fraction": 0.44736842105263175,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.6573576799140706,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 1.0,
        "social_fraction": 0.018878718535469106,
        "coupled_fraction": 0.018878718535469106,
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
    "20261123:temporal_return_value_gru:body": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 0.010897435897435899,
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
        "env_fraction": 0.7777777777777779,
        "social_fraction": 1.0,
        "coupled_fraction": 0.7777777777777779,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.34693877551020413,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 77.3,
        "end": 85.2,
        "env_fraction": 0.3111111111111111,
        "social_fraction": 0.30594629156010233,
        "coupled_fraction": 0.30594629156010233,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 87.8,
        "end": 95.7,
        "env_fraction": 0.3469387755102042,
        "social_fraction": 0.040441176470588244,
        "coupled_fraction": 0.040441176470588244,
        "resolved": false
      }
    ],
    "20261123:temporal_return_value_gru:infrastructure": [
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
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 46.7,
        "end": 54.5,
        "env_fraction": 1.0,
        "social_fraction": 0.029891304347826084,
        "coupled_fraction": 0.029891304347826084,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 62.8,
        "end": 70.7,
        "env_fraction": 0.0,
        "social_fraction": 0.9675925925925923,
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
        "env_fraction": 0.0,
        "social_fraction": 1.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261123:temporal_return_value_gru:tools": [
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
        "social_fraction": 0.2828571428571429,
        "coupled_fraction": 0.0,
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
        "env_fraction": 0.1272108843537415,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
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
        "env_fraction": 0.09912536443148688,
        "social_fraction": 0.04910714285714285,
        "coupled_fraction": 0.04910714285714285,
        "resolved": false
      }
    ],
    "20261123:temporal_return_value_gru:social_culture": [
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
        "env_fraction": 0.8794379467186482,
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
        "env_fraction": 1.0,
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
    "20261123:temporal_return_value_gru:environment": [
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
    "20261123:temporal_return_value_gru:previous_action": [
      {
        "crisis": "storm_shelter_coordination",
        "start": 17.2,
        "end": 25.0,
        "env_fraction": 1.0,
        "social_fraction": 0.837406015037594,
        "coupled_fraction": 0.837406015037594,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 1.0,
        "social_fraction": 0.8957142857142858,
        "coupled_fraction": 0.8957142857142858,
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
        "env_fraction": 0.1619047619047619,
        "social_fraction": 1.0,
        "coupled_fraction": 0.1619047619047619,
        "resolved": false
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
        "env_fraction": 0.0,
        "social_fraction": 0.0,
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
        "env_fraction": 0.19615384615384615,
        "social_fraction": 1.0,
        "coupled_fraction": 0.19615384615384615,
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
    "20261124:temporal_return_value_gru:none": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.44523809523809516,
        "social_fraction": 1.0,
        "coupled_fraction": 0.44523809523809516,
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
        "env_fraction": 0.0,
        "social_fraction": 0.014322916666666668,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.8070913461538459,
        "social_fraction": 1.0,
        "coupled_fraction": 0.8070913461538459,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 70.6,
        "end": 78.5,
        "env_fraction": 0.034646739130434784,
        "social_fraction": 0.6629464285714287,
        "coupled_fraction": 0.034646739130434784,
        "resolved": false
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
    "20261124:temporal_return_value_gru:body": [
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
        "env_fraction": 0.043478260869565216,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.0,
        "social_fraction": 0.49652777777777746,
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
        "env_fraction": 0.42089371980676316,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 82.4,
        "end": 90.3,
        "env_fraction": 1.0,
        "social_fraction": 0.16938405797101447,
        "coupled_fraction": 0.16938405797101447,
        "resolved": false
      }
    ],
    "20261124:temporal_return_value_gru:infrastructure": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.916560846560846,
        "social_fraction": 1.0,
        "coupled_fraction": 0.916560846560846,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.0,
        "social_fraction": 0.804201680672269,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.31632653061224497,
        "social_fraction": 0.24264705882352938,
        "coupled_fraction": 0.24264705882352938,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 1.0,
        "social_fraction": 0.05108359133126934,
        "coupled_fraction": 0.05108359133126934,
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
        "env_fraction": 0.7555555555555558,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:temporal_return_value_gru:tools": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.6961904761904752,
        "social_fraction": 0.7541149068322982,
        "coupled_fraction": 0.6961904761904752,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.10394021739130432,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.3577806122448979,
        "social_fraction": 0.9453124999999991,
        "coupled_fraction": 0.3577806122448979,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.2554086538461538,
        "social_fraction": 0.0,
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
        "env_fraction": 0.42275132275132277,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261124:temporal_return_value_gru:social_culture": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.7555555555555554,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.019450800915331804,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 59.4,
        "end": 67.3,
        "env_fraction": 0.8030936454849499,
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
    "20261124:temporal_return_value_gru:environment": [
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
    "20261124:temporal_return_value_gru:previous_action": [
      {
        "crisis": "quarantine_rumor",
        "start": 15.2,
        "end": 23.0,
        "env_fraction": 0.9066666666666666,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9066666666666666,
        "resolved": false
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 30.8,
        "end": 38.6,
        "env_fraction": 0.981657608695652,
        "social_fraction": 1.0,
        "coupled_fraction": 0.981657608695652,
        "resolved": true
      },
      {
        "crisis": "route_migration_dispute",
        "start": 46.1,
        "end": 53.9,
        "env_fraction": 0.36862244897959173,
        "social_fraction": 1.0,
        "coupled_fraction": 0.36862244897959173,
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
        "env_fraction": 1.0,
        "social_fraction": 0.7413043478260871,
        "coupled_fraction": 0.7413043478260871,
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
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
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
        "env_fraction": 0.028846153846153844,
        "social_fraction": 1.0,
        "coupled_fraction": 0.028846153846153844,
        "resolved": false
      }
    ],
    "20261125:temporal_return_value_gru:none": [
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
        "env_fraction": 0.10119047619047619,
        "social_fraction": 0.34375000000000006,
        "coupled_fraction": 0.10119047619047619,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.19411057692307693,
        "social_fraction": 1.0,
        "coupled_fraction": 0.19411057692307693,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.9562499999999997,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9562499999999997,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.16168478260869565,
        "social_fraction": 0.44196428571428575,
        "coupled_fraction": 0.16168478260869565,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 79.6,
        "end": 87.5,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      }
    ],
    "20261125:temporal_return_value_gru:body": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.039596273291925464,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 0.2619047619047619,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.5254120879120879,
        "social_fraction": 0.5737781954887219,
        "coupled_fraction": 0.5254120879120879,
        "resolved": false
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 0.9849206349206342,
        "social_fraction": 1.0,
        "coupled_fraction": 0.9849206349206342,
        "resolved": true
      },
      {
        "crisis": "contaminated_water_trust",
        "start": 64.9,
        "end": 72.8,
        "env_fraction": 0.42236024844720493,
        "social_fraction": 0.10102040816326531,
        "coupled_fraction": 0.10102040816326531,
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
    "20261125:temporal_return_value_gru:infrastructure": [
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
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 1.0,
        "social_fraction": 1.0,
        "coupled_fraction": 1.0,
        "resolved": true
      },
      {
        "crisis": "quarantine_rumor",
        "start": 52.5,
        "end": 60.3,
        "env_fraction": 1.0,
        "social_fraction": 0.45434782608695673,
        "coupled_fraction": 0.45434782608695673,
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
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:temporal_return_value_gru:tools": [
      {
        "crisis": "contaminated_water_trust",
        "start": 13.8,
        "end": 21.6,
        "env_fraction": 0.05279503105590062,
        "social_fraction": 0.2693877551020408,
        "coupled_fraction": 0.05279503105590062,
        "resolved": false
      },
      {
        "crisis": "route_migration_dispute",
        "start": 25.2,
        "end": 33.0,
        "env_fraction": 0.0,
        "social_fraction": 0.4133986928104574,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.4086538461538459,
        "social_fraction": 0.6151315789473681,
        "coupled_fraction": 0.4086538461538459,
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
        "env_fraction": 0.0,
        "social_fraction": 0.40595238095238073,
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
    "20261125:temporal_return_value_gru:social_culture": [
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
        "env_fraction": 1.0,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      }
    ],
    "20261125:temporal_return_value_gru:environment": [
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
    "20261125:temporal_return_value_gru:previous_action": [
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
        "env_fraction": 0.4956268221574344,
        "social_fraction": 0.0,
        "coupled_fraction": 0.0,
        "resolved": false
      },
      {
        "crisis": "storm_shelter_coordination",
        "start": 37.9,
        "end": 45.7,
        "env_fraction": 0.26854395604395603,
        "social_fraction": 1.0,
        "coupled_fraction": 0.26854395604395603,
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
        "env_fraction": 0.17158385093167702,
        "social_fraction": 1.0,
        "coupled_fraction": 0.17158385093167702,
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
    ]
  },
  "notes": {
    "claim": "temporal crisis-window return labels can guide active repair choices during coupled crises",
    "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
    "remaining_structure": "candidate repair actions are supplied, action heads are supervised, and temporal value labels come from completed crisis rollouts rather than online policy-gradient exploration"
  }
};
