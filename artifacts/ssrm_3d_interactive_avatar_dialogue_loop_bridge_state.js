window.SSRM_3D_INTERACTIVE_AVATAR_DIALOGUE_LOOP_STATE = {
  "condition": "integrated_interactive_avatar_dialogue_loop",
  "source_live_dialogue": "artifacts/ssrm_3d_live_dialogue_world_integration_bridge_state.json",
  "source_live_results": "artifacts/ssrm_3d_live_dialogue_world_integration_bridge_results.json",
  "runtime_state": {
    "condition": "integrated_live_dialogue_world_integration",
    "source_recurrent": "artifacts/ssrm_3d_recurrent_faction_dialogue_controller_bridge_state.json",
    "source_live": "artifacts/ssrm_3d_autonomous_live_agent_loop_bridge_state.json",
    "source_avatar": "artifacts/ssrm_3d_embodied_avatar_input_bridge_state.json",
    "agents": {
      "integrated_deep_time_world:00": {
        "agent_id": "integrated_deep_time_world:00",
        "name": "Ari",
        "role": "scout",
        "trust": 1.0,
        "attention": "care-or-kinship",
        "motive": "heard-comfort_neighbor",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8317256600463334,
        "curiosity": 0.9717400000000005,
        "workspace_updates": 5,
        "language_hits": 5,
        "responses": 5,
        "position": {
          "x": 8.0,
          "z": 0.0
        },
        "embodied_memory": [
          {
            "step": 1,
            "player_text": "walk near Ari quietly and ask what vosha means by the storm marks",
            "kind": "ask_meaning",
            "focus": "danger-or-weather-memory",
            "token": "vosha",
            "avatar_distance": 2.4
          },
          {
            "step": 16,
            "player_text": "tell Ari the air smells wrong and ask for storm memory",
            "kind": "weather_watch",
            "focus": "danger-or-weather-memory",
            "token": "vosha",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "weather_watch",
        "fatigue": 0.1469188066106786,
        "pain": 0.0,
        "wetness": 0.14,
        "thermal_comfort": 0.62,
        "workspace_ticks": 48,
        "autonomous_actions": 48,
        "social_exchanges": 61,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 4,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 6,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 10,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 12,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 16,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 18,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 22,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 24,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 28,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 30,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 34,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 36,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 40,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "autonomous_tick",
            "tick": 42,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 46,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 48,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "nono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 52,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 54,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 58,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 60,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 64,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 66,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 70,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 72,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 76,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 78,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 82,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 84,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 88,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 90,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 94,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "misavo"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 96,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "vosha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          }
        ],
        "body": {
          "energy": 0.439572,
          "stress": 0.703874,
          "pain": 0.06,
          "temperature": 0.466415,
          "wetness": 0.13
        },
        "affect": {
          "valence": 0.58,
          "arousal": 0.56026,
          "trust": 0.856,
          "attention": 0.92528
        },
        "internal_workspace": [
          {
            "turn_id": "live_001_turn_02_budget_or_rank",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.539147,
              "vision": 0.428119,
              "olfaction": 0.383937,
              "thermal": 0.348029,
              "wetness": 0.321555,
              "pain": 0.305372,
              "affect": 0.360001
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_002_turn_04_refusal_boundary",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 1.0,
              "olfaction": 1.0,
              "thermal": 1.0,
              "wetness": 1.0,
              "pain": 1.0,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_00_source_body",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.37563,
              "vision": 0.300095,
              "olfaction": 0.320802,
              "thermal": 0.375542,
              "wetness": 0.45848,
              "pain": 0.560772,
              "affect": 0.731512
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_005_turn_02_budget_or_rank",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.979722,
              "olfaction": 0.971774,
              "thermal": 0.953106,
              "wetness": 0.92432,
              "pain": 0.886347,
              "affect": 0.900414
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_04_refusal_boundary",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.470337,
              "vision": 0.44182,
              "olfaction": 0.492438,
              "thermal": 0.558942,
              "wetness": 0.637064,
              "pain": 0.721791,
              "affect": 0.867687
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_00_source_body",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.973922,
              "vision": 0.834434,
              "olfaction": 0.734215,
              "thermal": 0.62395,
              "wetness": 0.515397,
              "pain": 0.420129,
              "affect": 0.408305
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_02_budget_or_rank",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.462832,
              "vision": 0.45028,
              "olfaction": 0.503857,
              "thermal": 0.561834,
              "wetness": 0.622336,
              "pain": 0.68341,
              "affect": 0.80308
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_010_turn_04_refusal_boundary",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.927745,
              "vision": 0.784471,
              "olfaction": 0.698344,
              "thermal": 0.61489,
              "wetness": 0.539464,
              "pain": 0.476906,
              "affect": 0.491231
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_012_turn_00_source_body",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.700554,
              "vision": 0.750055,
              "olfaction": 0.847822,
              "thermal": 0.923431,
              "wetness": 0.968819,
              "pain": 0.979147,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_02_budget_or_rank",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.643674,
              "vision": 0.524555,
              "olfaction": 0.469166,
              "thermal": 0.419298,
              "wetness": 0.376561,
              "pain": 0.342336,
              "affect": 0.37773
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_04_refusal_boundary",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.97865,
              "vision": 0.985608,
              "olfaction": 1.0,
              "thermal": 1.0,
              "wetness": 1.0,
              "pain": 1.0,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_00_source_body",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.425423,
              "vision": 0.315464,
              "olfaction": 0.300108,
              "thermal": 0.320993,
              "wetness": 0.375891,
              "pain": 0.458949,
              "affect": 0.621311
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_017_turn_02_budget_or_rank",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.966193,
              "olfaction": 0.978093,
              "thermal": 0.979068,
              "wetness": 0.969087,
              "pain": 0.948473,
              "affect": 0.977891
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_04_refusal_boundary",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.461065,
              "vision": 0.405184,
              "olfaction": 0.430788,
              "thermal": 0.476235,
              "wetness": 0.538607,
              "pain": 0.613903,
              "affect": 0.75729
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "feedback_link",
            "live_event": "live_013_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.565804,
              "vision": 0.343974,
              "olfaction": 0.319103,
              "thermal": 0.446395,
              "wetness": 0.58139,
              "pain": 0.57647,
              "affect": 0.454535
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_000",
            "frequency_echo": {
              "audio": 0.523578,
              "vision": 0.665717,
              "olfaction": 0.638397,
              "thermal": 0.483835,
              "wetness": 0.361236,
              "pain": 0.400418,
              "affect": 0.582457
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_006_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.487611,
              "vision": 0.307371,
              "olfaction": 0.320134,
              "thermal": 0.503803,
              "wetness": 0.724777,
              "pain": 0.821318,
              "affect": 0.786791
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_013_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.608275,
              "vision": 0.684658,
              "olfaction": 0.644777,
              "thermal": 0.457635,
              "wetness": 0.267863,
              "pain": 0.226431,
              "affect": 0.389808
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_000",
            "frequency_echo": {
              "audio": 0.405923,
              "vision": 0.298121,
              "olfaction": 0.358825,
              "thermal": 0.549324,
              "wetness": 0.711576,
              "pain": 0.713507,
              "affect": 0.570443
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_006_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.471508,
              "vision": 0.618125,
              "olfaction": 0.672037,
              "thermal": 0.573318,
              "wetness": 0.447993,
              "pain": 0.452707,
              "affect": 0.665254
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_013_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.573967,
              "vision": 0.347686,
              "olfaction": 0.314952,
              "thermal": 0.438197,
              "wetness": 0.576682,
              "pain": 0.57958,
              "affect": 0.462604
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_000",
            "frequency_echo": {
              "audio": 0.515749,
              "vision": 0.663554,
              "olfaction": 0.643888,
              "thermal": 0.491931,
              "wetness": 0.364494,
              "pain": 0.395842,
              "affect": 0.574255
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_006_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.495804,
              "vision": 0.312165,
              "olfaction": 0.317121,
              "thermal": 0.495754,
              "wetness": 0.719092,
              "pain": 0.823223,
              "affect": 0.794536
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_013_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.600096,
              "vision": 0.680788,
              "olfaction": 0.648773,
              "thermal": 0.465824,
              "wetness": 0.272715,
              "pain": 0.223485,
              "affect": 0.381773
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_000",
            "frequency_echo": {
              "audio": 0.413803,
              "vision": 0.300455,
              "olfaction": 0.353467,
              "thermal": 0.541201,
              "wetness": 0.708156,
              "pain": 0.717935,
              "affect": 0.578648
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_006_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.463327,
              "vision": 0.613188,
              "olfaction": 0.674884,
              "thermal": 0.581332,
              "wetness": 0.453804,
              "pain": 0.450974,
              "affect": 0.657569
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_001_turn_02_budget_or_rank",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_002_turn_04_refusal_boundary",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_00_source_body",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_005_turn_02_budget_or_rank",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_04_refusal_boundary",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_00_source_body",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_02_budget_or_rank",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_010_turn_04_refusal_boundary",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_012_turn_00_source_body",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_02_budget_or_rank",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_04_refusal_boundary",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_00_source_body",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_017_turn_02_budget_or_rank",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_04_refusal_boundary",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:01": {
        "agent_id": "integrated_deep_time_world:01",
        "name": "Bo",
        "role": "builder",
        "trust": 1.0,
        "attention": "danger-or-weather-memory",
        "motive": "heard-watch_weather",
        "body_state": 1.0,
        "fear": 0.02930254375597095,
        "attachment": 0.9040828462679249,
        "curiosity": 0.7559000000000002,
        "workspace_updates": 6,
        "language_hits": 6,
        "responses": 6,
        "position": {
          "x": 7.794,
          "z": 4.5
        },
        "embodied_memory": [
          {
            "step": 3,
            "player_text": "repair the cold tool cache with Bo before night rain",
            "kind": "repair",
            "focus": "tool-or-route",
            "token": "vori",
            "avatar_distance": 2.4
          },
          {
            "step": 13,
            "player_text": "patch the shelter rope while Bo checks the old cache",
            "kind": "repair",
            "focus": "tool-or-route",
            "token": "vori",
            "avatar_distance": 2.4
          },
          {
            "step": 18,
            "player_text": "promise Bo the borrowed tool comes back before dark",
            "kind": "promise",
            "focus": "tool-or-route",
            "token": "vori",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "promise",
        "fatigue": 0.27915293046776957,
        "pain": 0.001,
        "wetness": 0.158,
        "thermal_comfort": 0.6,
        "workspace_ticks": 32,
        "autonomous_actions": 32,
        "social_exchanges": 46,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "tulen",
            "from": "Fay",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "voeya",
            "from": "Cy",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "vori"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          }
        ],
        "body": {
          "energy": 0.461272,
          "stress": 0.530327,
          "pain": 0.04,
          "temperature": 0.46462,
          "wetness": 0.142
        },
        "affect": {
          "valence": 0.692,
          "arousal": 0.565721,
          "trust": 0.824,
          "attention": 0.908188
        },
        "internal_workspace": [
          {
            "turn_id": "live_000_turn_01_faction_vote",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.956198,
              "olfaction": 0.890758,
              "thermal": 0.79228,
              "wetness": 0.673739,
              "pain": 0.550752,
              "affect": 0.499525
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_001_turn_03_feedback_link",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.381939,
              "vision": 0.394307,
              "olfaction": 0.505848,
              "thermal": 0.638779,
              "wetness": 0.771903,
              "pain": 0.883998,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_002_turn_05_memory_update",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.965651,
              "vision": 0.801448,
              "olfaction": 0.671503,
              "thermal": 0.536536,
              "wetness": 0.418065,
              "pain": 0.334979,
              "affect": 0.360525
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_01_faction_vote",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.502175,
              "vision": 0.553912,
              "olfaction": 0.676991,
              "thermal": 0.795196,
              "wetness": 0.892954,
              "pain": 0.957385,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_005_turn_03_feedback_link",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.791077,
              "vision": 0.59565,
              "olfaction": 0.467294,
              "thermal": 0.366474,
              "wetness": 0.309265,
              "pain": 0.304788,
              "affect": 0.413757
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_05_memory_update",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.714146,
              "vision": 0.785931,
              "olfaction": 0.894449,
              "thermal": 0.962398,
              "wetness": 0.978944,
              "pain": 0.941449,
              "affect": 0.915891
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_01_faction_vote",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.593881,
              "vision": 0.425571,
              "olfaction": 0.345514,
              "thermal": 0.304255,
              "wetness": 0.307232,
              "pain": 0.354052,
              "affect": 0.498546
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_03_feedback_link",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.910394,
              "vision": 0.938121,
              "olfaction": 0.978316,
              "thermal": 0.96457,
              "wetness": 0.899074,
              "pain": 0.792272,
              "affect": 0.721192
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_010_turn_05_memory_update",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.417626,
              "vision": 0.30604,
              "olfaction": 0.3077,
              "thermal": 0.362342,
              "wetness": 0.461253,
              "pain": 0.588664,
              "affect": 0.78426
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_012_turn_01_faction_vote",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.979575,
              "olfaction": 0.951135,
              "thermal": 0.881703,
              "wetness": 0.780426,
              "pain": 0.660648,
              "affect": 0.598149
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_03_feedback_link",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.360206,
              "vision": 0.331927,
              "olfaction": 0.412767,
              "thermal": 0.529837,
              "wetness": 0.664471,
              "pain": 0.795204,
              "affect": 0.961191
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_05_memory_update",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.888859,
              "olfaction": 0.778378,
              "thermal": 0.645834,
              "wetness": 0.512361,
              "pain": 0.399238,
              "affect": 0.384501
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_01_faction_vote",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.423962,
              "vision": 0.453002,
              "olfaction": 0.566679,
              "thermal": 0.690016,
              "wetness": 0.806764,
              "pain": 0.90154,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_05_memory_update",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.604487,
              "vision": 0.679773,
              "olfaction": 0.808717,
              "thermal": 0.910761,
              "wetness": 0.969635,
              "pain": 0.975953,
              "affect": 0.988706
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_105",
            "frequency_echo": {
              "audio": 0.526949,
              "vision": 0.365569,
              "olfaction": 0.310683,
              "thermal": 0.429854,
              "wetness": 0.630618,
              "pain": 0.745494,
              "affect": 0.685966
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_004_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.435914,
              "vision": 0.64817,
              "olfaction": 0.799162,
              "thermal": 0.772974,
              "wetness": 0.651406,
              "pain": 0.593967,
              "affect": 0.69733
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_105",
            "frequency_echo": {
              "audio": 0.394804,
              "vision": 0.593953,
              "olfaction": 0.68962,
              "thermal": 0.610952,
              "wetness": 0.447376,
              "pain": 0.366383,
              "affect": 0.45954
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_004_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.570619,
              "vision": 0.421978,
              "olfaction": 0.420032,
              "thermal": 0.589477,
              "wetness": 0.832248,
              "pain": 0.972883,
              "affect": 0.925947
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_105",
            "frequency_echo": {
              "audio": 0.53461,
              "vision": 0.372179,
              "olfaction": 0.310165,
              "thermal": 0.422684,
              "wetness": 0.623388,
              "pain": 0.744851,
              "affect": 0.692501
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_004_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.428274,
              "vision": 0.641525,
              "olfaction": 0.799622,
              "thermal": 0.780115,
              "wetness": 0.658664,
              "pain": 0.594669,
              "affect": 0.69083
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_105",
            "frequency_echo": {
              "audio": 0.387208,
              "vision": 0.587239,
              "olfaction": 0.689962,
              "thermal": 0.618035,
              "wetness": 0.454688,
              "pain": 0.367202,
              "affect": 0.453113
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_004_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.578193,
              "vision": 0.428725,
              "olfaction": 0.41975,
              "thermal": 0.582424,
              "wetness": 0.82491,
              "pain": 0.972006,
              "affect": 0.932337
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_000_turn_01_faction_vote",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_001_turn_03_feedback_link",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_002_turn_05_memory_update",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_01_faction_vote",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_005_turn_03_feedback_link",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_05_memory_update",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_01_faction_vote",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_03_feedback_link",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_010_turn_05_memory_update",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_012_turn_01_faction_vote",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_03_feedback_link",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_05_memory_update",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_01_faction_vote",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_05_memory_update",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:02": {
        "agent_id": "integrated_deep_time_world:02",
        "name": "Cy",
        "role": "healer",
        "trust": 1.0,
        "attention": "care-or-kinship",
        "motive": "comfort_neighbor",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8086612007166091,
        "curiosity": 0.7801000000000001,
        "workspace_updates": 3,
        "language_hits": 3,
        "responses": 3,
        "position": {
          "x": 5.0,
          "z": 8.66
        },
        "embodied_memory": [
          {
            "step": 11,
            "player_text": "move close to Cy and ask which word warns of illness",
            "kind": "ask_meaning",
            "focus": "danger-or-weather-memory",
            "token": "shath",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "ask_meaning",
        "fatigue": 0.18786029388256695,
        "pain": 0.0,
        "wetness": 0.17600000000000002,
        "thermal_comfort": 0.58,
        "workspace_ticks": 96,
        "autonomous_actions": 96,
        "social_exchanges": 86,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 1,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 3,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 4,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 6,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 7,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 9,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 10,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 12,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 13,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 15,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 16,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 18,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 19,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 21,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "voeya"
          },
          {
            "kind": "autonomous_tick",
            "tick": 22,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mieyaeya",
            "from": "Ira",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 24,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 25,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 27,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "voeya"
          },
          {
            "kind": "autonomous_tick",
            "tick": 28,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 30,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 31,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "voeya"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "tulen",
            "from": "Fay",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 33,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 34,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 36,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 37,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 39,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 40,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 42,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 43,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 45,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 46,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 48,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 49,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 51,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 52,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 54,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 55,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 57,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 58,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 60,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 61,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 63,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 64,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 66,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 67,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 69,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 70,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 72,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 73,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 75,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 76,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 78,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 79,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 81,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 82,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 84,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 85,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 87,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 88,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 90,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 91,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 93,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 94,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          },
          {
            "kind": "autonomous_tick",
            "tick": 96,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "eyasami"
          }
        ],
        "body": {
          "energy": 0.434355,
          "stress": 0.710029,
          "pain": 0.06,
          "temperature": 0.466283,
          "wetness": 0.13
        },
        "affect": {
          "valence": 0.58,
          "arousal": 0.564001,
          "trust": 0.856,
          "attention": 0.94093
        },
        "internal_workspace": [
          {
            "turn_id": "live_000_turn_02_budget_or_rank",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.871059,
              "vision": 0.75569,
              "olfaction": 0.696583,
              "thermal": 0.635647,
              "wetness": 0.574853,
              "pain": 0.516163,
              "affect": 0.521475
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_001_turn_04_refusal_boundary",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.752422,
              "vision": 0.778543,
              "olfaction": 0.86219,
              "thermal": 0.937996,
              "wetness": 1.0,
              "pain": 1.0,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_00_source_body",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.617067,
              "vision": 0.455265,
              "olfaction": 0.373161,
              "thermal": 0.319508,
              "wetness": 0.300026,
              "pain": 0.316794,
              "affect": 0.428022
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_02_budget_or_rank",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.835904,
              "vision": 0.829504,
              "olfaction": 0.876981,
              "thermal": 0.9168,
              "wetness": 0.947675,
              "pain": 0.968609,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_005_turn_04_refusal_boundary",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.55657,
              "vision": 0.444736,
              "olfaction": 0.411849,
              "thermal": 0.40002,
              "wetness": 0.410007,
              "pain": 0.441169,
              "affect": 0.551508
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_007_turn_00_source_body",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.979429,
              "olfaction": 0.96768,
              "thermal": 0.920994,
              "wetness": 0.844347,
              "pain": 0.745912,
              "affect": 0.696185
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_02_budget_or_rank",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.368283,
              "vision": 0.300288,
              "olfaction": 0.303271,
              "thermal": 0.317134,
              "wetness": 0.34143,
              "pain": 0.375373,
              "affect": 0.477868
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_04_refusal_boundary",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 1.0,
              "olfaction": 1.0,
              "thermal": 0.943911,
              "wetness": 0.869004,
              "pain": 0.785819,
              "affect": 0.759694
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_00_source_body",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.410574,
              "vision": 0.42348,
              "olfaction": 0.519473,
              "thermal": 0.628316,
              "wetness": 0.738406,
              "pain": 0.838003,
              "affect": 0.976488
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_012_turn_02_budget_or_rank",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.956234,
              "vision": 0.852085,
              "olfaction": 0.801082,
              "thermal": 0.744875,
              "wetness": 0.685278,
              "pain": 0.624219,
              "affect": 0.623669
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_04_refusal_boundary",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.647,
              "vision": 0.668204,
              "olfaction": 0.754016,
              "thermal": 0.838928,
              "wetness": 0.917492,
              "pain": 0.984666,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_02_budget_or_rank",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.728811,
              "vision": 0.728996,
              "olfaction": 0.786306,
              "thermal": 0.838889,
              "wetness": 0.885045,
              "pain": 0.923282,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_017_turn_04_refusal_boundary",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.645521,
              "vision": 0.514371,
              "olfaction": 0.457699,
              "thermal": 0.419142,
              "wetness": 0.401175,
              "pain": 0.40495,
              "affect": 0.490225
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_00_source_body",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.957321,
              "vision": 0.955194,
              "olfaction": 0.97946,
              "thermal": 0.967532,
              "wetness": 0.920682,
              "pain": 0.843904,
              "affect": 0.805386
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_090",
            "frequency_echo": {
              "audio": 0.379405,
              "vision": 0.579998,
              "olfaction": 0.68994,
              "thermal": 0.625252,
              "wetness": 0.462509,
              "pain": 0.368436,
              "affect": 0.446625
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_001_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.794325,
              "vision": 0.637111,
              "olfaction": 0.54828,
              "thermal": 0.616657,
              "wetness": 0.818892,
              "pain": 0.974508,
              "affect": 0.978877
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_008_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.299044,
              "vision": 0.436164,
              "olfaction": 0.562141,
              "thermal": 0.52559,
              "wetness": 0.367743,
              "pain": 0.247084,
              "affect": 0.330417
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_090",
            "frequency_echo": {
              "audio": 0.549861,
              "vision": 0.386332,
              "olfaction": 0.310208,
              "thermal": 0.408578,
              "wetness": 0.608102,
              "pain": 0.742439,
              "affect": 0.705181
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_001_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.515887,
              "vision": 0.704245,
              "olfaction": 0.899263,
              "thermal": 0.928797,
              "wetness": 0.805208,
              "pain": 0.647582,
              "affect": 0.639282
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_008_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.540792,
              "vision": 0.320099,
              "olfaction": 0.194971,
              "thermal": 0.244891,
              "wetness": 0.431586,
              "pain": 0.596774,
              "affect": 0.644449
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_090",
            "frequency_echo": {
              "audio": 0.372113,
              "vision": 0.572894,
              "olfaction": 0.689556,
              "thermal": 0.631941,
              "wetness": 0.470121,
              "pain": 0.369973,
              "affect": 0.440674
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_001_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.799842,
              "vision": 0.645201,
              "olfaction": 0.551505,
              "thermal": 0.612052,
              "wetness": 0.81069,
              "pain": 0.970251,
              "affect": 0.982478
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_008_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.29277,
              "vision": 0.428325,
              "olfaction": 0.559943,
              "thermal": 0.531055,
              "wetness": 0.375845,
              "pain": 0.250375,
              "affect": 0.325871
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_090",
            "frequency_echo": {
              "audio": 0.557071,
              "vision": 0.393523,
              "olfaction": 0.310768,
              "thermal": 0.401993,
              "wetness": 0.600425,
              "pain": 0.740729,
              "affect": 0.711009
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_001_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.510502,
              "vision": 0.696126,
              "olfaction": 0.895876,
              "thermal": 0.933255,
              "wetness": 0.813413,
              "pain": 0.65199,
              "affect": 0.635841
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_008_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.54695,
              "vision": 0.327989,
              "olfaction": 0.197339,
              "thermal": 0.23956,
              "wetness": 0.423458,
              "pain": 0.593321,
              "affect": 0.648847
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_000_turn_02_budget_or_rank",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_001_turn_04_refusal_boundary",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_00_source_body",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_02_budget_or_rank",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_005_turn_04_refusal_boundary",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_007_turn_00_source_body",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_02_budget_or_rank",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_04_refusal_boundary",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_00_source_body",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_012_turn_02_budget_or_rank",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_04_refusal_boundary",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_02_budget_or_rank",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_017_turn_04_refusal_boundary",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_00_source_body",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:03": {
        "agent_id": "integrated_deep_time_world:03",
        "name": "Dee",
        "role": "farmer",
        "trust": 1.0,
        "attention": "care-or-kinship",
        "motive": "heard-comfort_neighbor",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8700640427517504,
        "curiosity": 0.7059000000000001,
        "workspace_updates": 4,
        "language_hits": 4,
        "responses": 4,
        "position": {
          "x": 0.0,
          "z": 11.0
        },
        "embodied_memory": [
          {
            "step": 2,
            "player_text": "give water to Dee and ask the council where to store it",
            "kind": "offer_resource",
            "focus": "shared-resource",
            "token": "vonono",
            "avatar_distance": 2.4
          },
          {
            "step": 12,
            "player_text": "drop the water skin near the storehouse for shared use",
            "kind": "offer_resource",
            "focus": "shared-resource",
            "token": "vonono",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "offer_resource",
        "fatigue": 0.18185849084232045,
        "pain": 0.0,
        "wetness": 0.194,
        "thermal_comfort": 0.56,
        "workspace_ticks": 50,
        "autonomous_actions": 48,
        "social_exchanges": 60,
        "player_responses": 2,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 1,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 3,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 7,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 9,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 13,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 15,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "mieyaeya",
            "from": "Ira",
            "action": "teach_token"
          },
          {
            "kind": "player_interrupt",
            "text": "avatar asks who needs water before the cold rain",
            "token": "vonono",
            "action": "forage_water",
            "tick": 18
          },
          {
            "kind": "autonomous_tick",
            "tick": 19,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "voeya",
            "from": "Cy",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 21,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 25,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 27,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 31,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 33,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 37,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 39,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 43,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 45,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 49,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 51,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 55,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 57,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 61,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 63,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "player_interrupt",
            "text": "avatar promises to return the borrowed tool",
            "token": "saka",
            "action": "repair_tool",
            "tick": 66
          },
          {
            "kind": "autonomous_tick",
            "tick": 67,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 69,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 73,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 75,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "autonomous_tick",
            "tick": 79,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 81,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 85,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 87,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 91,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 93,
            "action": "clean_camp",
            "focus": "care-or-kinship",
            "token": "shatusha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "vonono"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          }
        ],
        "body": {
          "energy": 0.464234,
          "stress": 0.526836,
          "pain": 0.04,
          "temperature": 0.463873,
          "wetness": 0.142
        },
        "affect": {
          "valence": 0.692,
          "arousal": 0.563821,
          "trust": 0.824,
          "attention": 0.8993
        },
        "internal_workspace": [
          {
            "turn_id": "live_000_turn_03_feedback_link",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.431152,
              "vision": 0.311149,
              "olfaction": 0.303578,
              "thermal": 0.349646,
              "wetness": 0.442008,
              "pain": 0.565937,
              "affect": 0.761675
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_001_turn_05_memory_update",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.979467,
              "olfaction": 0.944958,
              "thermal": 0.861827,
              "wetness": 0.743328,
              "pain": 0.608355,
              "affect": 0.538426
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_01_faction_vote",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.360837,
              "vision": 0.314668,
              "olfaction": 0.371363,
              "thermal": 0.463451,
              "wetness": 0.5788,
              "pain": 0.702212,
              "affect": 0.877427
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_03_feedback_link",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.90403,
              "olfaction": 0.799168,
              "thermal": 0.668928,
              "wetness": 0.534076,
              "pain": 0.416112,
              "affect": 0.393845
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_005_turn_05_memory_update",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.417938,
              "vision": 0.454702,
              "olfaction": 0.58101,
              "thermal": 0.716723,
              "wetness": 0.840204,
              "pain": 0.931764,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_007_turn_01_faction_vote",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.919704,
              "vision": 0.75261,
              "olfaction": 0.630679,
              "thermal": 0.509975,
              "wetness": 0.406403,
              "pain": 0.333608,
              "affect": 0.361181
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_03_feedback_link",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.582528,
              "vision": 0.656729,
              "olfaction": 0.788262,
              "thermal": 0.896157,
              "wetness": 0.96321,
              "pain": 0.978731,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_05_memory_update",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.713588,
              "vision": 0.519583,
              "olfaction": 0.404777,
              "thermal": 0.327475,
              "wetness": 0.300001,
              "pain": 0.326737,
              "affect": 0.463419
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_01_faction_vote",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.77944,
              "vision": 0.83221,
              "olfaction": 0.919657,
              "thermal": 0.970257,
              "wetness": 0.977346,
              "pain": 0.939988,
              "affect": 0.923106
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_05_memory_update",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.965999,
              "vision": 0.967649,
              "olfaction": 0.977059,
              "thermal": 0.932728,
              "wetness": 0.841724,
              "pain": 0.718558,
              "affect": 0.642867
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_015_turn_01_faction_vote",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.386386,
              "vision": 0.300169,
              "olfaction": 0.318726,
              "thermal": 0.379612,
              "wetness": 0.474804,
              "pain": 0.591761,
              "affect": 0.775074
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_03_feedback_link",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.958771,
              "olfaction": 0.88709,
              "thermal": 0.776012,
              "wetness": 0.643249,
              "pain": 0.509968,
              "affect": 0.457419
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_017_turn_05_memory_update",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.371962,
              "vision": 0.373088,
              "olfaction": 0.476771,
              "thermal": 0.606478,
              "wetness": 0.741531,
              "pain": 0.860395,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_01_faction_vote",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.991298,
              "vision": 0.849519,
              "olfaction": 0.740136,
              "thermal": 0.61756,
              "wetness": 0.49794,
              "pain": 0.397037,
              "affect": 0.388145
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_075",
            "frequency_echo": {
              "audio": 0.634181,
              "vision": 0.504974,
              "olfaction": 0.354093,
              "thermal": 0.337358,
              "wetness": 0.487256,
              "pain": 0.683072,
              "affect": 0.761875
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_019_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.632638,
              "vision": 0.691771,
              "olfaction": 0.793912,
              "thermal": 0.754535,
              "wetness": 0.549985,
              "pain": 0.309909,
              "affect": 0.242958
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_075",
            "frequency_echo": {
              "audio": 0.289688,
              "vision": 0.453761,
              "olfaction": 0.643245,
              "thermal": 0.701031,
              "wetness": 0.59109,
              "pain": 0.431603,
              "affect": 0.386302
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_019_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.978276,
              "vision": 0.745693,
              "olfaction": 0.506541,
              "thermal": 0.390079,
              "wetness": 0.443523,
              "pain": 0.559321,
              "affect": 0.618936
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_075",
            "frequency_echo": {
              "audio": 0.637563,
              "vision": 0.513091,
              "olfaction": 0.359483,
              "thermal": 0.335065,
              "wetness": 0.479389,
              "pain": 0.676863,
              "affect": 0.763033
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_019_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.62931,
              "vision": 0.683663,
              "olfaction": 0.788477,
              "thermal": 0.756771,
              "wetness": 0.557835,
              "pain": 0.316157,
              "affect": 0.241858
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_075",
            "frequency_echo": {
              "audio": 0.286468,
              "vision": 0.445671,
              "olfaction": 0.637723,
              "thermal": 0.703153,
              "wetness": 0.598906,
              "pain": 0.437927,
              "affect": 0.38532
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_019_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.981441,
              "vision": 0.753773,
              "olfaction": 0.512107,
              "thermal": 0.388014,
              "wetness": 0.435725,
              "pain": 0.552961,
              "affect": 0.61986
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_000_turn_03_feedback_link",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_001_turn_05_memory_update",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_01_faction_vote",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_03_feedback_link",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_005_turn_05_memory_update",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_007_turn_01_faction_vote",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_03_feedback_link",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_05_memory_update",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_01_faction_vote",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_05_memory_update",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_015_turn_01_faction_vote",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_03_feedback_link",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_017_turn_05_memory_update",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_01_faction_vote",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:04": {
        "agent_id": "integrated_deep_time_world:04",
        "name": "Eli",
        "role": "guard",
        "trust": 1.0,
        "attention": "danger-or-weather-memory",
        "motive": "heard-watch_weather",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8485288452020788,
        "curiosity": 0.8399000000000002,
        "workspace_updates": 3,
        "language_hits": 3,
        "responses": 3,
        "position": {
          "x": -6.0,
          "z": 10.392
        },
        "embodied_memory": [
          {
            "step": 9,
            "player_text": "promise Eli I will return the hammer to the cache",
            "kind": "promise",
            "focus": "tool-or-route",
            "token": "mivo",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "promise",
        "fatigue": 0.15859804422389068,
        "pain": 0.0,
        "wetness": 0.21200000000000002,
        "thermal_comfort": 0.62,
        "workspace_ticks": 32,
        "autonomous_actions": 32,
        "social_exchanges": 59,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "mivo"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "mivo"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "mivo"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "kathth"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "mitu"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          }
        ],
        "body": {
          "energy": 0.434928,
          "stress": 0.70931,
          "pain": 0.06,
          "temperature": 0.462523,
          "wetness": 0.13
        },
        "affect": {
          "valence": 0.58,
          "arousal": 0.561109,
          "trust": 0.856,
          "attention": 0.939215
        },
        "internal_workspace": [
          {
            "turn_id": "live_000_turn_04_refusal_boundary",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.488233,
              "vision": 0.472323,
              "olfaction": 0.533589,
              "thermal": 0.608101,
              "wetness": 0.691076,
              "pain": 0.777191,
              "affect": 0.92092
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_002_turn_00_source_body",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.937561,
              "vision": 0.786538,
              "olfaction": 0.679889,
              "thermal": 0.568988,
              "wetness": 0.465658,
              "pain": 0.380917,
              "affect": 0.383801
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_02_budget_or_rank",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.505562,
              "vision": 0.498638,
              "olfaction": 0.556281,
              "thermal": 0.61663,
              "wetness": 0.677733,
              "pain": 0.737618,
              "affect": 0.854348
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_04_refusal_boundary",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.874857,
              "vision": 0.729118,
              "olfaction": 0.644076,
              "thermal": 0.56519,
              "wetness": 0.497522,
              "pain": 0.445413,
              "affect": 0.472208
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_00_source_body",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.755784,
              "vision": 0.800857,
              "olfaction": 0.888778,
              "thermal": 0.950175,
              "wetness": 0.9785,
              "pain": 0.970732,
              "affect": 0.987702
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_007_turn_02_budget_or_rank",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.589949,
              "vision": 0.474133,
              "olfaction": 0.423678,
              "thermal": 0.380212,
              "wetness": 0.345141,
              "pain": 0.319597,
              "affect": 0.364407
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_04_refusal_boundary",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 1.0,
              "olfaction": 1.0,
              "thermal": 1.0,
              "wetness": 1.0,
              "pain": 1.0,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_02_budget_or_rank",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.977441,
              "olfaction": 0.979443,
              "thermal": 0.970478,
              "wetness": 0.950833,
              "pain": 0.921145,
              "affect": 0.942372
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_012_turn_04_refusal_boundary",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.4612,
              "vision": 0.419241,
              "olfaction": 0.457865,
              "thermal": 0.514594,
              "wetness": 0.585787,
              "pain": 0.666875,
              "affect": 0.812657
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_00_source_body",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.877165,
              "olfaction": 0.786037,
              "thermal": 0.679339,
              "wetness": 0.568447,
              "pain": 0.465183,
              "affect": 0.440559
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_015_turn_02_budget_or_rank",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.426404,
              "vision": 0.406962,
              "olfaction": 0.45505,
              "thermal": 0.509115,
              "wetness": 0.567408,
              "pain": 0.628048,
              "affect": 0.749073
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_04_refusal_boundary",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.977238,
              "vision": 0.838643,
              "olfaction": 0.753718,
              "thermal": 0.667913,
              "wetness": 0.586734,
              "pain": 0.51539,
              "affect": 0.518459
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_00_source_body",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.64531,
              "vision": 0.69633,
              "olfaction": 0.801344,
              "thermal": 0.889156,
              "wetness": 0.950401,
              "pain": 0.978551,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_02_budget_or_rank",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.698896,
              "vision": 0.578044,
              "olfaction": 0.519194,
              "thermal": 0.464248,
              "wetness": 0.414981,
              "pain": 0.372984,
              "affect": 0.399616
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "source_body",
            "live_event": "live_016_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.985846,
              "vision": 0.815919,
              "olfaction": 0.581847,
              "thermal": 0.416606,
              "wetness": 0.42662,
              "pain": 0.559637,
              "affect": 0.692734
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_003_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.314639,
              "vision": 0.415011,
              "olfaction": 0.632777,
              "thermal": 0.762227,
              "wetness": 0.717537,
              "pain": 0.573401,
              "affect": 0.532473
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_060",
            "frequency_echo": {
              "audio": 0.643463,
              "vision": 0.529508,
              "olfaction": 0.371323,
              "thermal": 0.331443,
              "wetness": 0.463634,
              "pain": 0.663461,
              "affect": 0.764305
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_016_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.606058,
              "vision": 0.600618,
              "olfaction": 0.728981,
              "thermal": 0.790899,
              "wetness": 0.683949,
              "pain": 0.463415,
              "affect": 0.331426
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_003_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.692672,
              "vision": 0.586958,
              "olfaction": 0.44055,
              "thermal": 0.382559,
              "wetness": 0.499493,
              "pain": 0.717449,
              "affect": 0.906176
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_060",
            "frequency_echo": {
              "audio": 0.280909,
              "vision": 0.429334,
              "olfaction": 0.625628,
              "thermal": 0.70642,
              "wetness": 0.614531,
              "pain": 0.451544,
              "affect": 0.38441
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_016_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.985499,
              "vision": 0.822628,
              "olfaction": 0.589445,
              "thermal": 0.418107,
              "wetness": 0.420643,
              "pain": 0.551678,
              "affect": 0.690109
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_003_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.313898,
              "vision": 0.407735,
              "olfaction": 0.625655,
              "thermal": 0.761808,
              "wetness": 0.724205,
              "pain": 0.581026,
              "affect": 0.534045
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_060",
            "frequency_echo": {
              "audio": 0.645834,
              "vision": 0.537399,
              "olfaction": 0.377479,
              "thermal": 0.330204,
              "wetness": 0.45614,
              "pain": 0.656602,
              "affect": 0.764387
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_016_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.606583,
              "vision": 0.594012,
              "olfaction": 0.721317,
              "thermal": 0.789225,
              "wetness": 0.689803,
              "pain": 0.471415,
              "affect": 0.334217
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_003_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.693237,
              "vision": 0.594151,
              "olfaction": 0.447758,
              "thermal": 0.383156,
              "wetness": 0.492929,
              "pain": 0.70976,
              "affect": 0.904431
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_060",
            "frequency_echo": {
              "audio": 0.278708,
              "vision": 0.421494,
              "olfaction": 0.619358,
              "thermal": 0.707484,
              "wetness": 0.621951,
              "pain": 0.458499,
              "affect": 0.384504
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_000_turn_04_refusal_boundary",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_002_turn_00_source_body",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_02_budget_or_rank",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_04_refusal_boundary",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_00_source_body",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_007_turn_02_budget_or_rank",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_04_refusal_boundary",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_02_budget_or_rank",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_012_turn_04_refusal_boundary",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_00_source_body",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_015_turn_02_budget_or_rank",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_04_refusal_boundary",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_00_source_body",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_02_budget_or_rank",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:05": {
        "agent_id": "integrated_deep_time_world:05",
        "name": "Fay",
        "role": "teacher",
        "trust": 1.0,
        "attention": "care-or-kinship",
        "motive": "comfort_neighbor",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8477372337803998,
        "curiosity": 0.9704000000000005,
        "workspace_updates": 4,
        "language_hits": 4,
        "responses": 4,
        "position": {
          "x": -11.258,
          "z": 6.5
        },
        "embodied_memory": [
          {
            "step": 5,
            "player_text": "comfort Fay; lower my voice after the pain signal",
            "kind": "comfort",
            "focus": "care-or-kinship",
            "token": "milenno",
            "avatar_distance": 2.4
          },
          {
            "step": 19,
            "player_text": "comfort the frightened child near Fay without taking supplies",
            "kind": "comfort",
            "focus": "care-or-kinship",
            "token": "milenno",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "comfort",
        "fatigue": 0.15012358735033837,
        "pain": 0.0,
        "wetness": 0.14,
        "thermal_comfort": 0.6,
        "workspace_ticks": 96,
        "autonomous_actions": 96,
        "social_exchanges": 100,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 1,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 3,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 4,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 6,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 7,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 9,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 10,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 12,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 13,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 15,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 16,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 18,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 19,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 21,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 22,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 24,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "tulen"
          },
          {
            "kind": "autonomous_tick",
            "tick": 25,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 27,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 28,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 30,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 31,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "repair_tool",
            "focus": "tool-or-route",
            "token": "tulen"
          },
          {
            "kind": "autonomous_tick",
            "tick": 33,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 34,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 36,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 37,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 39,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 40,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 42,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 43,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 45,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 46,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 48,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 49,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 51,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 52,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 54,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 55,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 57,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 58,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 60,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 61,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 63,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 64,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 66,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 67,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "social",
            "token": "mieyaeya",
            "from": "Ira",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 69,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 70,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 72,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 73,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 75,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 76,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 78,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 79,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 81,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 82,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 84,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 85,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "shalenka"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 87,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 88,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 90,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 91,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 93,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 94,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "milenno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 96,
            "action": "comfort_neighbor",
            "focus": "care-or-kinship",
            "token": "milenno"
          }
        ],
        "body": {
          "energy": 0.467269,
          "stress": 0.523308,
          "pain": 0.04,
          "temperature": 0.46616,
          "wetness": 0.142
        },
        "affect": {
          "valence": 0.692,
          "arousal": 0.564426,
          "trust": 0.824,
          "attention": 0.890196
        },
        "internal_workspace": [
          {
            "turn_id": "live_000_turn_05_memory_update",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.769147,
              "vision": 0.833883,
              "olfaction": 0.927706,
              "thermal": 0.975658,
              "wetness": 0.970092,
              "pain": 0.911897,
              "affect": 0.870351
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_002_turn_01_faction_vote",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.542813,
              "vision": 0.385553,
              "olfaction": 0.321818,
              "thermal": 0.300004,
              "wetness": 0.322985,
              "pain": 0.387734,
              "affect": 0.545719
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_03_feedback_link",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.95099,
              "vision": 0.960719,
              "olfaction": 0.979312,
              "thermal": 0.943806,
              "wetness": 0.859861,
              "pain": 0.740862,
              "affect": 0.665781
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_004_turn_05_memory_update",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.39061,
              "vision": 0.300111,
              "olfaction": 0.323804,
              "thermal": 0.39791,
              "wetness": 0.510616,
              "pain": 0.64395,
              "affect": 0.836654
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_01_faction_vote",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.972301,
              "olfaction": 0.924729,
              "thermal": 0.839644,
              "wetness": 0.728255,
              "pain": 0.605238,
              "affect": 0.546801
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_008_turn_05_memory_update",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.996597,
              "vision": 0.847916,
              "olfaction": 0.726084,
              "thermal": 0.590528,
              "wetness": 0.462859,
              "pain": 0.363434,
              "affect": 0.368104
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_010_turn_01_faction_vote",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.459878,
              "vision": 0.501618,
              "olfaction": 0.62159,
              "thermal": 0.743988,
              "wetness": 0.852685,
              "pain": 0.93336,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_03_feedback_link",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.843085,
              "vision": 0.651004,
              "olfaction": 0.517168,
              "thermal": 0.402917,
              "wetness": 0.326465,
              "pain": 0.300004,
              "affect": 0.387751
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_012_turn_05_memory_update",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.658769,
              "vision": 0.734102,
              "olfaction": 0.854432,
              "thermal": 0.940573,
              "wetness": 0.978791,
              "pain": 0.962992,
              "affect": 0.955696
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_01_faction_vote",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.647768,
              "vision": 0.471287,
              "olfaction": 0.377034,
              "thermal": 0.317427,
              "wetness": 0.300321,
              "pain": 0.327968,
              "affect": 0.456726
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_015_turn_03_feedback_link",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.864208,
              "vision": 0.907602,
              "olfaction": 0.96833,
              "thermal": 0.976709,
              "wetness": 0.931404,
              "pain": 0.839637,
              "affect": 0.77604
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_016_turn_05_memory_update",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.452145,
              "vision": 0.320842,
              "olfaction": 0.300426,
              "thermal": 0.334151,
              "wetness": 0.41664,
              "pain": 0.534742,
              "affect": 0.729626
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_01_faction_vote",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.977826,
              "olfaction": 0.969274,
              "thermal": 0.917341,
              "wetness": 0.828866,
              "pain": 0.715508,
              "affect": 0.652202
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_03_feedback_link",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.362797,
              "vision": 0.312651,
              "olfaction": 0.374697,
              "thermal": 0.479043,
              "wetness": 0.609052,
              "pain": 0.743996,
              "affect": 0.922358
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "faction_vote",
            "live_event": "live_014_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.412543,
              "vision": 0.332007,
              "olfaction": 0.440537,
              "thermal": 0.555124,
              "wetness": 0.54131,
              "pain": 0.403441,
              "affect": 0.318974
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_045",
            "frequency_echo": {
              "audio": 0.28466,
              "vision": 0.329549,
              "olfaction": 0.514049,
              "thermal": 0.685633,
              "wetness": 0.703647,
              "pain": 0.568631,
              "affect": 0.421818
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_014_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.769276,
              "vision": 0.634867,
              "olfaction": 0.411076,
              "thermal": 0.220428,
              "wetness": 0.209097,
              "pain": 0.379146,
              "affect": 0.624933
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_045",
            "frequency_echo": {
              "audio": 0.639472,
              "vision": 0.635681,
              "olfaction": 0.490045,
              "thermal": 0.353561,
              "wetness": 0.368814,
              "pain": 0.53888,
              "affect": 0.724502
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_014_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.415452,
              "vision": 0.327123,
              "olfaction": 0.43235,
              "thermal": 0.551162,
              "wetness": 0.545215,
              "pain": 0.411622,
              "affect": 0.32391
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_045",
            "frequency_echo": {
              "audio": 0.287679,
              "vision": 0.324761,
              "olfaction": 0.505856,
              "thermal": 0.681568,
              "wetness": 0.707447,
              "pain": 0.576802,
              "affect": 0.426848
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_014_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.766203,
              "vision": 0.639607,
              "olfaction": 0.419272,
              "thermal": 0.224544,
              "wetness": 0.205349,
              "pain": 0.370979,
              "affect": 0.619857
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_045",
            "frequency_echo": {
              "audio": 0.636289,
              "vision": 0.640325,
              "olfaction": 0.498246,
              "thermal": 0.357779,
              "wetness": 0.365171,
              "pain": 0.530725,
              "affect": 0.719333
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_000_turn_05_memory_update",
            "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_002_turn_01_faction_vote",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_03_feedback_link",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_004_turn_05_memory_update",
            "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_01_faction_vote",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_008_turn_05_memory_update",
            "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_010_turn_01_faction_vote",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_03_feedback_link",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_012_turn_05_memory_update",
            "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_01_faction_vote",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_015_turn_03_feedback_link",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_016_turn_05_memory_update",
            "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_01_faction_vote",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_03_feedback_link",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:06": {
        "agent_id": "integrated_deep_time_world:06",
        "name": "Gus",
        "role": "trader",
        "trust": 1.0,
        "attention": "tool-or-route",
        "motive": "route_scout",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8360455309493804,
        "curiosity": 0.7338000000000002,
        "workspace_updates": 4,
        "language_hits": 4,
        "responses": 4,
        "position": {
          "x": -14.0,
          "z": 0.0
        },
        "embodied_memory": [
          {
            "step": 6,
            "player_text": "show Gus the trusted route after storms and loose mud",
            "kind": "route_request",
            "focus": "tool-or-route",
            "token": "omno",
            "avatar_distance": 2.4
          },
          {
            "step": 17,
            "player_text": "walk beside Gus and point to the safer ridge route",
            "kind": "route_request",
            "focus": "tool-or-route",
            "token": "omno",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "route_request",
        "fatigue": 0.14490082169002008,
        "pain": 0.004,
        "wetness": 0.158,
        "thermal_comfort": 0.58,
        "workspace_ticks": 48,
        "autonomous_actions": 48,
        "social_exchanges": 62,
        "player_responses": 0,
        "live_memory": [
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 4,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 6,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 10,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 12,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 16,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 18,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 22,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 24,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 28,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 30,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "voeya",
            "from": "Cy",
            "action": "repair_tool"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 34,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 36,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 40,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 42,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 46,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 48,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 52,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "vori",
            "from": "Bo",
            "action": "repair_tool"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 54,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 58,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 60,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "omom",
            "from": "Ira",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 64,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 66,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 70,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 72,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 76,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 78,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 82,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "autonomous_tick",
            "tick": 84,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 88,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "autonomous_tick",
            "tick": 90,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "forage_water",
            "focus": "shared-resource",
            "token": "kamith"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 94,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "omriri"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 96,
            "action": "route_scout",
            "focus": "tool-or-route",
            "token": "omno"
          }
        ],
        "body": {
          "energy": 0.434826,
          "stress": 0.70946,
          "pain": 0.06,
          "temperature": 0.466376,
          "wetness": 0.13
        },
        "affect": {
          "valence": 0.58,
          "arousal": 0.562945,
          "trust": 0.856,
          "attention": 0.939518
        },
        "internal_workspace": [
          {
            "turn_id": "live_001_turn_00_source_body",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.97812,
              "olfaction": 0.948593,
              "thermal": 0.886162,
              "wetness": 0.797485,
              "pain": 0.692016,
              "affect": 0.641002
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_002_turn_02_budget_or_rank",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.360572,
              "vision": 0.302527,
              "olfaction": 0.315388,
              "thermal": 0.338737,
              "wetness": 0.371821,
              "pain": 0.413571,
              "affect": 0.522637
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_04_refusal_boundary",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 1.0,
              "olfaction": 0.967744,
              "thermal": 0.897001,
              "wetness": 0.816183,
              "pain": 0.730477,
              "affect": 0.705382
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_02_budget_or_rank",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.916523,
              "vision": 0.806094,
              "olfaction": 0.750298,
              "thermal": 0.690938,
              "wetness": 0.629932,
              "pain": 0.569251,
              "affect": 0.570856
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_007_turn_04_refusal_boundary",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.698361,
              "vision": 0.72315,
              "olfaction": 0.80902,
              "thermal": 0.890461,
              "wetness": 0.962247,
              "pain": 1.0,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_00_source_body",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.671737,
              "vision": 0.504092,
              "olfaction": 0.410938,
              "thermal": 0.342206,
              "wetness": 0.305227,
              "pain": 0.303942,
              "affect": 0.398489
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_010_turn_02_budget_or_rank",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.783466,
              "vision": 0.781125,
              "olfaction": 0.834224,
              "thermal": 0.881047,
              "wetness": 0.920081,
              "pain": 0.950065,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_04_refusal_boundary",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.598367,
              "vision": 0.476047,
              "olfaction": 0.430664,
              "thermal": 0.405132,
              "wetness": 0.401088,
              "pain": 0.418792,
              "affect": 0.517108
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_00_source_body",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.990006,
              "vision": 0.971718,
              "olfaction": 0.978062,
              "thermal": 0.94836,
              "wetness": 0.88578,
              "pain": 0.796994,
              "affect": 0.751469
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_02_budget_or_rank",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.384807,
              "vision": 0.307075,
              "olfaction": 0.300101,
              "thermal": 0.30411,
              "wetness": 0.318972,
              "pain": 0.344207,
              "affect": 0.439
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_015_turn_04_refusal_boundary",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 1.0,
              "olfaction": 1.0,
              "thermal": 0.985402,
              "wetness": 0.918397,
              "pain": 0.839944,
              "affect": 0.815077
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_017_turn_00_source_body",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "intent": "source_body",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.385433,
              "vision": 0.383768,
              "olfaction": 0.469424,
              "thermal": 0.573267,
              "wetness": 0.684225,
              "pain": 0.790468,
              "affect": 0.940668
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_02_budget_or_rank",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "budget_or_rank",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.989138,
              "vision": 0.892441,
              "olfaction": 0.847587,
              "thermal": 0.796025,
              "wetness": 0.739422,
              "pain": 0.679606,
              "affect": 0.678511
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_04_refusal_boundary",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "refusal_boundary",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.599704,
              "vision": 0.615167,
              "olfaction": 0.698639,
              "thermal": 0.784766,
              "wetness": 0.868021,
              "pain": 0.94306,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "source_body",
            "live_event": "live_011_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.693253,
              "vision": 0.671392,
              "olfaction": 0.526001,
              "thermal": 0.329489,
              "wetness": 0.24899,
              "pain": 0.35637,
              "affect": 0.599491
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_018_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.654103,
              "vision": 0.563689,
              "olfaction": 0.670564,
              "thermal": 0.814597,
              "wetness": 0.835008,
              "pain": 0.681898,
              "affect": 0.500339
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_030",
            "frequency_echo": {
              "audio": 0.63261,
              "vision": 0.64487,
              "olfaction": 0.506836,
              "thermal": 0.362518,
              "wetness": 0.3617,
              "pain": 0.522237,
              "affect": 0.713631
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_011_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.431698,
              "vision": 0.298138,
              "olfaction": 0.384216,
              "thermal": 0.54953,
              "wetness": 0.628551,
              "pain": 0.546485,
              "affect": 0.425369
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_018_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.949852,
              "vision": 0.924233,
              "olfaction": 0.76442,
              "thermal": 0.555475,
              "wetness": 0.461143,
              "pain": 0.537021,
              "affect": 0.717649
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_030",
            "frequency_echo": {
              "audio": 0.29487,
              "vision": 0.315878,
              "olfaction": 0.489066,
              "thermal": 0.672307,
              "wetness": 0.71423,
              "pain": 0.593393,
              "affect": 0.437993
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_011_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.687241,
              "vision": 0.672841,
              "olfaction": 0.533579,
              "thermal": 0.336229,
              "wetness": 0.248694,
              "pain": 0.349311,
              "affect": 0.592159
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_018_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.659323,
              "vision": 0.561183,
              "olfaction": 0.662636,
              "thermal": 0.808536,
              "wetness": 0.836386,
              "pain": 0.689449,
              "affect": 0.50712
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_030",
            "frequency_echo": {
              "audio": 0.628772,
              "vision": 0.648898,
              "olfaction": 0.515027,
              "thermal": 0.367341,
              "wetness": 0.358721,
              "pain": 0.514194,
              "affect": 0.70792
            },
            "interactive": true
          },
          {
            "intent": "source_body",
            "live_event": "live_011_turn_04_refusal_boundary",
            "frequency_echo": {
              "audio": 0.437829,
              "vision": 0.296863,
              "olfaction": 0.376708,
              "thermal": 0.542691,
              "wetness": 0.62867,
              "pain": 0.553452,
              "affect": 0.432779
            },
            "interactive": true
          },
          {
            "intent": "feedback_link",
            "live_event": "live_018_turn_02_budget_or_rank",
            "frequency_echo": {
              "audio": 0.944497,
              "vision": 0.92657,
              "olfaction": 0.7723,
              "thermal": 0.561653,
              "wetness": 0.459939,
              "pain": 0.529541,
              "affect": 0.71077
            },
            "interactive": true
          },
          {
            "intent": "refusal_boundary",
            "live_event": "ungrounded_probe_030",
            "frequency_echo": {
              "audio": 0.298864,
              "vision": 0.312005,
              "olfaction": 0.480887,
              "thermal": 0.667342,
              "wetness": 0.717044,
              "pain": 0.601399,
              "affect": 0.44383
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_001_turn_00_source_body",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_002_turn_02_budget_or_rank",
            "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_04_refusal_boundary",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_02_budget_or_rank",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_007_turn_04_refusal_boundary",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_00_source_body",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_010_turn_02_budget_or_rank",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_04_refusal_boundary",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_00_source_body",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_02_budget_or_rank",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_015_turn_04_refusal_boundary",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_017_turn_00_source_body",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_02_budget_or_rank",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_04_refusal_boundary",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      },
      "integrated_deep_time_world:07": {
        "agent_id": "integrated_deep_time_world:07",
        "name": "Ira",
        "role": "pattern_keeper",
        "trust": 1.0,
        "attention": "danger-or-weather-memory",
        "motive": "watch_weather",
        "body_state": 1.0,
        "fear": 0.0,
        "attachment": 0.8284124836260316,
        "curiosity": 0.8151000000000003,
        "workspace_updates": 4,
        "language_hits": 4,
        "responses": 4,
        "position": {
          "x": -12.99,
          "z": -7.5
        },
        "embodied_memory": [
          {
            "step": 7,
            "player_text": "place a new sign near Ira and ask if the council accepts the mark",
            "kind": "share_symbol",
            "focus": "shared-resource",
            "token": "mieyaeya",
            "avatar_distance": 2.4
          },
          {
            "step": 15,
            "player_text": "ask Ira whether this scratch should become a public symbol",
            "kind": "share_symbol",
            "focus": "shared-resource",
            "token": "mieyaeya",
            "avatar_distance": 2.4
          }
        ],
        "last_player_intent": "share_symbol",
        "fatigue": 0.19181316157464745,
        "pain": 0.0,
        "wetness": 0.17600000000000002,
        "thermal_comfort": 0.56,
        "workspace_ticks": 34,
        "autonomous_actions": 32,
        "social_exchanges": 58,
        "player_responses": 2,
        "live_memory": [
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 2,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 5,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 8,
            "action": "warm_shelter",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 11,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 14,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "autonomous_tick",
            "tick": 17,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "mieyaeya"
          },
          {
            "kind": "autonomous_tick",
            "tick": 20,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 23,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "mieyaeya"
          },
          {
            "kind": "autonomous_tick",
            "tick": 26,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 29,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 32,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 35,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 38,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 41,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "player_interrupt",
            "text": "avatar asks whether the old route is safe",
            "token": "voeya",
            "action": "route_scout",
            "tick": 42
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 44,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "autonomous_tick",
            "tick": 47,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 50,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 53,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "kamith",
            "from": "Gus",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 56,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vonono",
            "from": "Dee",
            "action": "forage_water"
          },
          {
            "kind": "autonomous_tick",
            "tick": 59,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 62,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "social",
            "token": "mitu",
            "from": "Eli",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 65,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 68,
            "action": "teach_token",
            "focus": "shared-resource",
            "token": "mieyaeya"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 71,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 74,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "autonomous_tick",
            "tick": 77,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 80,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 83,
            "action": "rest_body",
            "focus": "care-or-kinship",
            "token": "vothsha"
          },
          {
            "kind": "social",
            "token": "shalenka",
            "from": "Fay",
            "action": "teach_token"
          },
          {
            "kind": "autonomous_tick",
            "tick": 86,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 89,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "player_interrupt",
            "text": "avatar asks what warning token belongs near the shelter",
            "token": "mieyaeya",
            "action": "teach_token",
            "tick": 90
          },
          {
            "kind": "social",
            "token": "vosha",
            "from": "Ari",
            "action": "watch_weather"
          },
          {
            "kind": "social",
            "token": "milenno",
            "from": "Fay",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 92,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          },
          {
            "kind": "social",
            "token": "eyasami",
            "from": "Cy",
            "action": "comfort_neighbor"
          },
          {
            "kind": "autonomous_tick",
            "tick": 95,
            "action": "watch_weather",
            "focus": "danger-or-weather-memory",
            "token": "omom"
          }
        ],
        "body": {
          "energy": 0.467343,
          "stress": 0.523178,
          "pain": 0.04,
          "temperature": 0.464873,
          "wetness": 0.142
        },
        "affect": {
          "valence": 0.692,
          "arousal": 0.562235,
          "trust": 0.824,
          "attention": 0.889965
        },
        "internal_workspace": [
          {
            "turn_id": "live_001_turn_01_faction_vote",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.87463,
              "vision": 0.698994,
              "olfaction": 0.575586,
              "thermal": 0.460665,
              "wetness": 0.369371,
              "pain": 0.313733,
              "affect": 0.361082
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_003_turn_05_memory_update",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.658215,
              "vision": 0.469526,
              "olfaction": 0.368017,
              "thermal": 0.309874,
              "wetness": 0.304365,
              "pain": 0.35237,
              "affect": 0.506234
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_005_turn_01_faction_vote",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.832093,
              "vision": 0.87522,
              "olfaction": 0.947357,
              "thermal": 0.978998,
              "wetness": 0.965976,
              "pain": 0.910005,
              "affect": 0.878461
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_006_turn_03_feedback_link",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.468538,
              "vision": 0.329547,
              "olfaction": 0.300055,
              "thermal": 0.324763,
              "wetness": 0.399733,
              "pain": 0.51301,
              "affect": 0.706535
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_007_turn_05_memory_update",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.996869,
              "vision": 0.978049,
              "olfaction": 0.96533,
              "thermal": 0.900741,
              "wetness": 0.79458,
              "pain": 0.663772,
              "affect": 0.589174
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_009_turn_01_faction_vote",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.369217,
              "vision": 0.302941,
              "olfaction": 0.341073,
              "thermal": 0.41859,
              "wetness": 0.525278,
              "pain": 0.647081,
              "affect": 0.827951
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_010_turn_03_feedback_link",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 1.0,
              "vision": 0.935324,
              "olfaction": 0.845864,
              "thermal": 0.72358,
              "wetness": 0.587971,
              "pain": 0.460657,
              "affect": 0.421938
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_011_turn_05_memory_update",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.390842,
              "vision": 0.410851,
              "olfaction": 0.527394,
              "thermal": 0.661892,
              "wetness": 0.792899,
              "pain": 0.899528,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_013_turn_01_faction_vote",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.958941,
              "vision": 0.803233,
              "olfaction": 0.686019,
              "thermal": 0.562741,
              "wetness": 0.449643,
              "pain": 0.361624,
              "affect": 0.370283
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_014_turn_03_feedback_link",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.532253,
              "vision": 0.601336,
              "olfaction": 0.736584,
              "thermal": 0.856432,
              "wetness": 0.941773,
              "pain": 0.978999,
              "affect": 1.0
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_015_turn_05_memory_update",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.7686,
              "vision": 0.572839,
              "olfaction": 0.447786,
              "thermal": 0.353379,
              "wetness": 0.304671,
              "pain": 0.309428,
              "affect": 0.426891
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_017_turn_01_faction_vote",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "intent": "faction_vote",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.724676,
              "vision": 0.784094,
              "olfaction": 0.884526,
              "thermal": 0.952741,
              "wetness": 0.979753,
              "pain": 0.962,
              "affect": 0.961824
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_018_turn_03_feedback_link",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "intent": "feedback_link",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.560603,
              "vision": 0.390382,
              "olfaction": 0.31996,
              "thermal": 0.300565,
              "wetness": 0.335289,
              "pain": 0.418596,
              "affect": 0.597204
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "turn_id": "live_019_turn_05_memory_update",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "intent": "memory_update",
            "source_cited": true,
            "sensory_signature": {
              "audio": 0.928062,
              "vision": 0.948543,
              "olfaction": 0.979831,
              "thermal": 0.956936,
              "wetness": 0.883509,
              "pain": 0.771257,
              "affect": 0.698078
            },
            "binding": "dialogue-to-live-workspace"
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_015",
            "frequency_echo": {
              "audio": 0.382628,
              "vision": 0.293134,
              "olfaction": 0.376731,
              "thermal": 0.573661,
              "wetness": 0.719968,
              "pain": 0.698239,
              "affect": 0.545552
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_009_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.497845,
              "vision": 0.565901,
              "olfaction": 0.525772,
              "thermal": 0.395775,
              "wetness": 0.333282,
              "pain": 0.447849,
              "affect": 0.730825
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_015",
            "frequency_echo": {
              "audio": 0.539234,
              "vision": 0.66907,
              "olfaction": 0.626362,
              "thermal": 0.467478,
              "wetness": 0.355595,
              "pain": 0.410679,
              "affect": 0.599186
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_009_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.343734,
              "vision": 0.190372,
              "olfaction": 0.274085,
              "thermal": 0.499329,
              "wetness": 0.69687,
              "pain": 0.73719,
              "affect": 0.6799
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_015",
            "frequency_echo": {
              "audio": 0.390139,
              "vision": 0.294415,
              "olfaction": 0.370604,
              "thermal": 0.565759,
              "wetness": 0.717557,
              "pain": 0.703535,
              "affect": 0.553687
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_009_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.49031,
              "vision": 0.564561,
              "olfaction": 0.53186,
              "thermal": 0.403693,
              "wetness": 0.335751,
              "pain": 0.442599,
              "affect": 0.722683
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "ungrounded_probe_015",
            "frequency_echo": {
              "audio": 0.531653,
              "vision": 0.667614,
              "olfaction": 0.63237,
              "thermal": 0.475426,
              "wetness": 0.358176,
              "pain": 0.40552,
              "affect": 0.591031
            },
            "interactive": true
          },
          {
            "intent": "faction_vote",
            "live_event": "live_009_turn_01_faction_vote",
            "frequency_echo": {
              "audio": 0.351337,
              "vision": 0.191886,
              "olfaction": 0.268118,
              "thermal": 0.491367,
              "wetness": 0.694234,
              "pain": 0.742303,
              "affect": 0.688062
            },
            "interactive": true
          }
        ],
        "dialogue_memory": [
          {
            "turn_id": "live_001_turn_01_faction_vote",
            "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_003_turn_05_memory_update",
            "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_005_turn_01_faction_vote",
            "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_006_turn_03_feedback_link",
            "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_007_turn_05_memory_update",
            "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_009_turn_01_faction_vote",
            "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
            "persistent": true
          },
          {
            "turn_id": "live_010_turn_03_feedback_link",
            "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_011_turn_05_memory_update",
            "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_013_turn_01_faction_vote",
            "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
            "persistent": true
          },
          {
            "turn_id": "live_014_turn_03_feedback_link",
            "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_015_turn_05_memory_update",
            "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
            "persistent": true
          },
          {
            "turn_id": "live_017_turn_01_faction_vote",
            "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
            "persistent": true
          },
          {
            "turn_id": "live_018_turn_03_feedback_link",
            "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
            "persistent": true
          },
          {
            "turn_id": "live_019_turn_05_memory_update",
            "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
            "persistent": true
          }
        ],
        "sensory_rates_hz": {
          "audio": 3.0,
          "vision": 12.0,
          "olfaction": 0.7,
          "thermal": 0.3,
          "wetness": 0.4,
          "pain": 8.0,
          "affect": 6.0
        }
      }
    },
    "world": {
      "shared_water": 0.9982,
      "tool_integrity": 0.845083,
      "shelter_warmth": 0.997754,
      "route_confidence": 1.0,
      "council_acceptance": 1.0,
      "danger_memory": 1.0,
      "food_cache": 0.9985,
      "waste_control": 0.9958,
      "fire_heat": 0.800888,
      "language_coherence": 0.9952,
      "trace_integrity": 1.0,
      "weather_cold": 0.288403,
      "rain_wetness": 0.410663,
      "threat_scent": 0.0,
      "flower_phase": 0.046686,
      "dialogue_pressure": 1.0,
      "governance_attention": 1.0,
      "avatar_trust_field": 1.0,
      "refusal_boundary_events": 20,
      "dialogue_world_events": [
        {
          "turn_id": "live_000_turn_01_faction_vote",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "strength": 0.83478
        },
        {
          "turn_id": "live_000_turn_02_budget_or_rank",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "strength": 0.78388
        },
        {
          "turn_id": "live_000_turn_03_feedback_link",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "strength": 0.693474
        },
        {
          "turn_id": "live_000_turn_04_refusal_boundary",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "strength": 0.778735
        },
        {
          "turn_id": "live_000_turn_05_memory_update",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "strength": 0.952347
        },
        {
          "turn_id": "live_001_turn_00_source_body",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.872074
        },
        {
          "turn_id": "live_001_turn_01_faction_vote",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.724904
        },
        {
          "turn_id": "live_001_turn_02_budget_or_rank",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.662682
        },
        {
          "turn_id": "live_001_turn_03_feedback_link",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.784221
        },
        {
          "turn_id": "live_001_turn_04_refusal_boundary",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.897003
        },
        {
          "turn_id": "live_001_turn_05_memory_update",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "strength": 0.914909
        },
        {
          "turn_id": "live_002_turn_00_source_body",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "strength": 0.760215
        },
        {
          "turn_id": "live_002_turn_01_faction_vote",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "strength": 0.670426
        },
        {
          "turn_id": "live_002_turn_02_budget_or_rank",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "strength": 0.658766
        },
        {
          "turn_id": "live_002_turn_04_refusal_boundary",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "strength": 0.94
        },
        {
          "turn_id": "live_002_turn_05_memory_update",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "strength": 0.812845
        },
        {
          "turn_id": "live_003_turn_00_source_body",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.670633
        },
        {
          "turn_id": "live_003_turn_01_faction_vote",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.725849
        },
        {
          "turn_id": "live_003_turn_02_budget_or_rank",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.775866
        },
        {
          "turn_id": "live_003_turn_03_feedback_link",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.882228
        },
        {
          "turn_id": "live_003_turn_04_refusal_boundary",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.883222
        },
        {
          "turn_id": "live_003_turn_05_memory_update",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "strength": 0.740839
        },
        {
          "turn_id": "live_004_turn_00_source_body",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.690754
        },
        {
          "turn_id": "live_004_turn_01_faction_vote",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.835768
        },
        {
          "turn_id": "live_004_turn_02_budget_or_rank",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.899852
        },
        {
          "turn_id": "live_004_turn_03_feedback_link",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.793182
        },
        {
          "turn_id": "live_004_turn_04_refusal_boundary",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.761825
        },
        {
          "turn_id": "live_004_turn_05_memory_update",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "strength": 0.768806
        },
        {
          "turn_id": "live_005_turn_01_faction_vote",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "strength": 0.900664
        },
        {
          "turn_id": "live_005_turn_02_budget_or_rank",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "strength": 0.915294
        },
        {
          "turn_id": "live_005_turn_03_feedback_link",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "strength": 0.69882
        },
        {
          "turn_id": "live_005_turn_04_refusal_boundary",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "strength": 0.696734
        },
        {
          "turn_id": "live_005_turn_05_memory_update",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "strength": 0.867722
        },
        {
          "turn_id": "live_006_turn_00_source_body",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.897091
        },
        {
          "turn_id": "live_006_turn_01_faction_vote",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.851091
        },
        {
          "turn_id": "live_006_turn_02_budget_or_rank",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.807179
        },
        {
          "turn_id": "live_006_turn_03_feedback_link",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.685569
        },
        {
          "turn_id": "live_006_turn_04_refusal_boundary",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.759362
        },
        {
          "turn_id": "live_006_turn_05_memory_update",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.948135
        },
        {
          "turn_id": "live_007_turn_00_source_body",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "strength": 0.885649
        },
        {
          "turn_id": "live_007_turn_01_faction_vote",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "strength": 0.741625
        },
        {
          "turn_id": "live_007_turn_02_budget_or_rank",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "strength": 0.676243
        },
        {
          "turn_id": "live_007_turn_04_refusal_boundary",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "strength": 0.881065
        },
        {
          "turn_id": "live_007_turn_05_memory_update",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "strength": 0.928547
        },
        {
          "turn_id": "live_008_turn_00_source_body",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.779951
        },
        {
          "turn_id": "live_008_turn_01_faction_vote",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.671868
        },
        {
          "turn_id": "live_008_turn_02_budget_or_rank",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.649663
        },
        {
          "turn_id": "live_008_turn_03_feedback_link",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.867075
        },
        {
          "turn_id": "live_008_turn_04_refusal_boundary",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.94
        },
        {
          "turn_id": "live_008_turn_05_memory_update",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "strength": 0.829998
        },
        {
          "turn_id": "live_009_turn_00_source_body",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.678783
        },
        {
          "turn_id": "live_009_turn_01_faction_vote",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.710637
        },
        {
          "turn_id": "live_009_turn_02_budget_or_rank",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.752776
        },
        {
          "turn_id": "live_009_turn_03_feedback_link",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.888825
        },
        {
          "turn_id": "live_009_turn_04_refusal_boundary",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.898756
        },
        {
          "turn_id": "live_009_turn_05_memory_update",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "strength": 0.74643
        },
        {
          "turn_id": "live_010_turn_01_faction_vote",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "strength": 0.818701
        },
        {
          "turn_id": "live_010_turn_02_budget_or_rank",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "strength": 0.885358
        },
        {
          "turn_id": "live_010_turn_03_feedback_link",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "strength": 0.809843
        },
        {
          "turn_id": "live_010_turn_04_refusal_boundary",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "strength": 0.78141
        },
        {
          "turn_id": "live_010_turn_05_memory_update",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "strength": 0.757507
        },
        {
          "turn_id": "live_011_turn_00_source_body",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.781519
        },
        {
          "turn_id": "live_011_turn_01_faction_vote",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.8977
        },
        {
          "turn_id": "live_011_turn_02_budget_or_rank",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.923396
        },
        {
          "turn_id": "live_011_turn_03_feedback_link",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.710397
        },
        {
          "turn_id": "live_011_turn_04_refusal_boundary",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.698748
        },
        {
          "turn_id": "live_011_turn_05_memory_update",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "strength": 0.851076
        },
        {
          "turn_id": "live_012_turn_00_source_body",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.886632
        },
        {
          "turn_id": "live_012_turn_01_faction_vote",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.866177
        },
        {
          "turn_id": "live_012_turn_02_budget_or_rank",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.829907
        },
        {
          "turn_id": "live_012_turn_04_refusal_boundary",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.741886
        },
        {
          "turn_id": "live_012_turn_05_memory_update",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.941201
        },
        {
          "turn_id": "live_013_turn_00_source_body",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.896439
        },
        {
          "turn_id": "live_013_turn_01_faction_vote",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.759517
        },
        {
          "turn_id": "live_013_turn_02_budget_or_rank",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.692713
        },
        {
          "turn_id": "live_013_turn_03_feedback_link",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.750717
        },
        {
          "turn_id": "live_013_turn_04_refusal_boundary",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.86352
        },
        {
          "turn_id": "live_013_turn_05_memory_update",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "strength": 0.938709
        },
        {
          "turn_id": "live_014_turn_00_source_body",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.799647
        },
        {
          "turn_id": "live_014_turn_01_faction_vote",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.676334
        },
        {
          "turn_id": "live_014_turn_02_budget_or_rank",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.644175
        },
        {
          "turn_id": "live_014_turn_03_feedback_link",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.853046
        },
        {
          "turn_id": "live_014_turn_04_refusal_boundary",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.937702
        },
        {
          "turn_id": "live_014_turn_05_memory_update",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "strength": 0.846304
        },
        {
          "turn_id": "live_015_turn_01_faction_vote",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "strength": 0.69742
        },
        {
          "turn_id": "live_015_turn_02_budget_or_rank",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "strength": 0.730561
        },
        {
          "turn_id": "live_015_turn_03_feedback_link",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "strength": 0.892681
        },
        {
          "turn_id": "live_015_turn_04_refusal_boundary",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "strength": 0.911638
        },
        {
          "turn_id": "live_015_turn_05_memory_update",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "strength": 0.75466
        },
        {
          "turn_id": "live_016_turn_00_source_body",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.671166
        },
        {
          "turn_id": "live_016_turn_01_faction_vote",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.801269
        },
        {
          "turn_id": "live_016_turn_02_budget_or_rank",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.868728
        },
        {
          "turn_id": "live_016_turn_03_feedback_link",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.826376
        },
        {
          "turn_id": "live_016_turn_04_refusal_boundary",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.802306
        },
        {
          "turn_id": "live_016_turn_05_memory_update",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "strength": 0.748551
        },
        {
          "turn_id": "live_017_turn_00_source_body",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "strength": 0.761752
        },
        {
          "turn_id": "live_017_turn_01_faction_vote",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "strength": 0.891761
        },
        {
          "turn_id": "live_017_turn_02_budget_or_rank",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "strength": 0.928352
        },
        {
          "turn_id": "live_017_turn_04_refusal_boundary",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "strength": 0.70427
        },
        {
          "turn_id": "live_017_turn_05_memory_update",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "strength": 0.8348
        },
        {
          "turn_id": "live_018_turn_00_source_body",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.873213
        },
        {
          "turn_id": "live_018_turn_01_faction_vote",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.879637
        },
        {
          "turn_id": "live_018_turn_02_budget_or_rank",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.851461
        },
        {
          "turn_id": "live_018_turn_03_feedback_link",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.677881
        },
        {
          "turn_id": "live_018_turn_04_refusal_boundary",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.726769
        },
        {
          "turn_id": "live_018_turn_05_memory_update",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "strength": 0.931731
        },
        {
          "turn_id": "live_019_turn_00_source_body",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.903324
        },
        {
          "turn_id": "live_019_turn_01_faction_vote",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.778105
        },
        {
          "turn_id": "live_019_turn_02_budget_or_rank",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.711655
        },
        {
          "turn_id": "live_019_turn_03_feedback_link",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.734581
        },
        {
          "turn_id": "live_019_turn_04_refusal_boundary",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.844173
        },
        {
          "turn_id": "live_019_turn_05_memory_update",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "strength": 0.9464
        }
      ],
      "interactive_dialogue_pressure": 0.523376,
      "interactive_governance_attention": 0.610605,
      "interactive_refusal_count": 16
    },
    "avatar": {
      "x": -8.885501,
      "z": 6.13772,
      "fatigue": 0.56124,
      "wetness": 0.1,
      "thermal_comfort": 0.62,
      "dialogue_focus": [
        {
          "turn_id": "live_000_turn_01_faction_vote",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_000_turn_02_budget_or_rank",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_000_turn_03_feedback_link",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_000_turn_04_refusal_boundary",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_000_turn_05_memory_update",
          "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_001_turn_00_source_body",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "source_body"
        },
        {
          "turn_id": "live_001_turn_01_faction_vote",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_001_turn_02_budget_or_rank",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_001_turn_03_feedback_link",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_001_turn_04_refusal_boundary",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_001_turn_05_memory_update",
          "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_002_turn_00_source_body",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "intent": "source_body"
        },
        {
          "turn_id": "live_002_turn_01_faction_vote",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_002_turn_02_budget_or_rank",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_002_turn_04_refusal_boundary",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_002_turn_05_memory_update",
          "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_003_turn_00_source_body",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "source_body"
        },
        {
          "turn_id": "live_003_turn_01_faction_vote",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_003_turn_02_budget_or_rank",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_003_turn_03_feedback_link",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_003_turn_04_refusal_boundary",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_003_turn_05_memory_update",
          "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_004_turn_00_source_body",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "source_body"
        },
        {
          "turn_id": "live_004_turn_01_faction_vote",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_004_turn_02_budget_or_rank",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_004_turn_03_feedback_link",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_004_turn_04_refusal_boundary",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_004_turn_05_memory_update",
          "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_005_turn_01_faction_vote",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_005_turn_02_budget_or_rank",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_005_turn_03_feedback_link",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_005_turn_04_refusal_boundary",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_005_turn_05_memory_update",
          "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_006_turn_00_source_body",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "source_body"
        },
        {
          "turn_id": "live_006_turn_01_faction_vote",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_006_turn_02_budget_or_rank",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_006_turn_03_feedback_link",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_006_turn_04_refusal_boundary",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_006_turn_05_memory_update",
          "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_007_turn_00_source_body",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "intent": "source_body"
        },
        {
          "turn_id": "live_007_turn_01_faction_vote",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_007_turn_02_budget_or_rank",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_007_turn_04_refusal_boundary",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_007_turn_05_memory_update",
          "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_008_turn_00_source_body",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "source_body"
        },
        {
          "turn_id": "live_008_turn_01_faction_vote",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_008_turn_02_budget_or_rank",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_008_turn_03_feedback_link",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_008_turn_04_refusal_boundary",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_008_turn_05_memory_update",
          "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_009_turn_00_source_body",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "source_body"
        },
        {
          "turn_id": "live_009_turn_01_faction_vote",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_009_turn_02_budget_or_rank",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_009_turn_03_feedback_link",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_009_turn_04_refusal_boundary",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_009_turn_05_memory_update",
          "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_010_turn_01_faction_vote",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_010_turn_02_budget_or_rank",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_010_turn_03_feedback_link",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_010_turn_04_refusal_boundary",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_010_turn_05_memory_update",
          "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_011_turn_00_source_body",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "source_body"
        },
        {
          "turn_id": "live_011_turn_01_faction_vote",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_011_turn_02_budget_or_rank",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_011_turn_03_feedback_link",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_011_turn_04_refusal_boundary",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_011_turn_05_memory_update",
          "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_012_turn_00_source_body",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "source_body"
        },
        {
          "turn_id": "live_012_turn_01_faction_vote",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_012_turn_02_budget_or_rank",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_012_turn_04_refusal_boundary",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_012_turn_05_memory_update",
          "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_013_turn_00_source_body",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "source_body"
        },
        {
          "turn_id": "live_013_turn_01_faction_vote",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_013_turn_02_budget_or_rank",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_013_turn_03_feedback_link",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_013_turn_04_refusal_boundary",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_013_turn_05_memory_update",
          "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_014_turn_00_source_body",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "source_body"
        },
        {
          "turn_id": "live_014_turn_01_faction_vote",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_014_turn_02_budget_or_rank",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_014_turn_03_feedback_link",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_014_turn_04_refusal_boundary",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_014_turn_05_memory_update",
          "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_015_turn_01_faction_vote",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_015_turn_02_budget_or_rank",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_015_turn_03_feedback_link",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_015_turn_04_refusal_boundary",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_015_turn_05_memory_update",
          "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_016_turn_00_source_body",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "source_body"
        },
        {
          "turn_id": "live_016_turn_01_faction_vote",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_016_turn_02_budget_or_rank",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_016_turn_03_feedback_link",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_016_turn_04_refusal_boundary",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_016_turn_05_memory_update",
          "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_017_turn_00_source_body",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "intent": "source_body"
        },
        {
          "turn_id": "live_017_turn_01_faction_vote",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_017_turn_02_budget_or_rank",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_017_turn_04_refusal_boundary",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_017_turn_05_memory_update",
          "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_018_turn_00_source_body",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "source_body"
        },
        {
          "turn_id": "live_018_turn_01_faction_vote",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_018_turn_02_budget_or_rank",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_018_turn_03_feedback_link",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_018_turn_04_refusal_boundary",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_018_turn_05_memory_update",
          "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "intent": "memory_update"
        },
        {
          "turn_id": "live_019_turn_00_source_body",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "source_body"
        },
        {
          "turn_id": "live_019_turn_01_faction_vote",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "faction_vote"
        },
        {
          "turn_id": "live_019_turn_02_budget_or_rank",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "budget_or_rank"
        },
        {
          "turn_id": "live_019_turn_03_feedback_link",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "feedback_link"
        },
        {
          "turn_id": "live_019_turn_04_refusal_boundary",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "refusal_boundary"
        },
        {
          "turn_id": "live_019_turn_05_memory_update",
          "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "intent": "memory_update"
        }
      ],
      "body_frequency_echo": {
        "audio": 0.928062,
        "vision": 0.948543,
        "olfaction": 0.979831,
        "thermal": 0.956936,
        "wetness": 0.883509,
        "pain": 0.771257,
        "affect": 0.698078
      },
      "input_trace_links": [
        {
          "turn_id": "live_000_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_000_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_000_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_000_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_000_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_001_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_002_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_002_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_002_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_002_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_002_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_003_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_004_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_005_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_005_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_005_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_005_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_005_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_006_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_007_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_007_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_007_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_007_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_007_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_008_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_009_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_010_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_010_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_010_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_010_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_010_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_011_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_012_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_012_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_012_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_012_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_012_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_013_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_014_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_015_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_015_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_015_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_015_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_015_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_016_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_017_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_017_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_017_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_017_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_017_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_018_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_00_source_body",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_01_faction_vote",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_02_budget_or_rank",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_03_feedback_link",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_04_refusal_boundary",
          "source": "recurrent-dialogue-controller"
        },
        {
          "turn_id": "live_019_turn_05_memory_update",
          "source": "recurrent-dialogue-controller"
        }
      ],
      "typed_dialogue_history": [
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.693253,
            "vision": 0.671392,
            "olfaction": 0.526001,
            "thermal": 0.329489,
            "wetness": 0.24899,
            "pain": 0.35637,
            "affect": 0.599491
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.634181,
            "vision": 0.504974,
            "olfaction": 0.354093,
            "thermal": 0.337358,
            "wetness": 0.487256,
            "pain": 0.683072,
            "affect": 0.761875
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.565804,
            "vision": 0.343974,
            "olfaction": 0.319103,
            "thermal": 0.446395,
            "wetness": 0.58139,
            "pain": 0.57647,
            "affect": 0.454535
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.412543,
            "vision": 0.332007,
            "olfaction": 0.440537,
            "thermal": 0.555124,
            "wetness": 0.54131,
            "pain": 0.403441,
            "affect": 0.318974
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.379405,
            "vision": 0.579998,
            "olfaction": 0.68994,
            "thermal": 0.625252,
            "wetness": 0.462509,
            "pain": 0.368436,
            "affect": 0.446625
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.985846,
            "vision": 0.815919,
            "olfaction": 0.581847,
            "thermal": 0.416606,
            "wetness": 0.42662,
            "pain": 0.559637,
            "affect": 0.692734
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.526949,
            "vision": 0.365569,
            "olfaction": 0.310683,
            "thermal": 0.429854,
            "wetness": 0.630618,
            "pain": 0.745494,
            "affect": 0.685966
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.654103,
            "vision": 0.563689,
            "olfaction": 0.670564,
            "thermal": 0.814597,
            "wetness": 0.835008,
            "pain": 0.681898,
            "affect": 0.500339
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.632638,
            "vision": 0.691771,
            "olfaction": 0.793912,
            "thermal": 0.754535,
            "wetness": 0.549985,
            "pain": 0.309909,
            "affect": 0.242958
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.523578,
            "vision": 0.665717,
            "olfaction": 0.638397,
            "thermal": 0.483835,
            "wetness": 0.361236,
            "pain": 0.400418,
            "affect": 0.582457
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.794325,
            "vision": 0.637111,
            "olfaction": 0.54828,
            "thermal": 0.616657,
            "wetness": 0.818892,
            "pain": 0.974508,
            "affect": 0.978877
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.382628,
            "vision": 0.293134,
            "olfaction": 0.376731,
            "thermal": 0.573661,
            "wetness": 0.719968,
            "pain": 0.698239,
            "affect": 0.545552
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.314639,
            "vision": 0.415011,
            "olfaction": 0.632777,
            "thermal": 0.762227,
            "wetness": 0.717537,
            "pain": 0.573401,
            "affect": 0.532473
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.435914,
            "vision": 0.64817,
            "olfaction": 0.799162,
            "thermal": 0.772974,
            "wetness": 0.651406,
            "pain": 0.593967,
            "affect": 0.69733
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.63261,
            "vision": 0.64487,
            "olfaction": 0.506836,
            "thermal": 0.362518,
            "wetness": 0.3617,
            "pain": 0.522237,
            "affect": 0.713631
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.487611,
            "vision": 0.307371,
            "olfaction": 0.320134,
            "thermal": 0.503803,
            "wetness": 0.724777,
            "pain": 0.821318,
            "affect": 0.786791
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.28466,
            "vision": 0.329549,
            "olfaction": 0.514049,
            "thermal": 0.685633,
            "wetness": 0.703647,
            "pain": 0.568631,
            "affect": 0.421818
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.299044,
            "vision": 0.436164,
            "olfaction": 0.562141,
            "thermal": 0.52559,
            "wetness": 0.367743,
            "pain": 0.247084,
            "affect": 0.330417
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.497845,
            "vision": 0.565901,
            "olfaction": 0.525772,
            "thermal": 0.395775,
            "wetness": 0.333282,
            "pain": 0.447849,
            "affect": 0.730825
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.643463,
            "vision": 0.529508,
            "olfaction": 0.371323,
            "thermal": 0.331443,
            "wetness": 0.463634,
            "pain": 0.663461,
            "affect": 0.764305
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.431698,
            "vision": 0.298138,
            "olfaction": 0.384216,
            "thermal": 0.54953,
            "wetness": 0.628551,
            "pain": 0.546485,
            "affect": 0.425369
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.289688,
            "vision": 0.453761,
            "olfaction": 0.643245,
            "thermal": 0.701031,
            "wetness": 0.59109,
            "pain": 0.431603,
            "affect": 0.386302
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.608275,
            "vision": 0.684658,
            "olfaction": 0.644777,
            "thermal": 0.457635,
            "wetness": 0.267863,
            "pain": 0.226431,
            "affect": 0.389808
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.769276,
            "vision": 0.634867,
            "olfaction": 0.411076,
            "thermal": 0.220428,
            "wetness": 0.209097,
            "pain": 0.379146,
            "affect": 0.624933
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.549861,
            "vision": 0.386332,
            "olfaction": 0.310208,
            "thermal": 0.408578,
            "wetness": 0.608102,
            "pain": 0.742439,
            "affect": 0.705181
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.606058,
            "vision": 0.600618,
            "olfaction": 0.728981,
            "thermal": 0.790899,
            "wetness": 0.683949,
            "pain": 0.463415,
            "affect": 0.331426
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.394804,
            "vision": 0.593953,
            "olfaction": 0.68962,
            "thermal": 0.610952,
            "wetness": 0.447376,
            "pain": 0.366383,
            "affect": 0.45954
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.949852,
            "vision": 0.924233,
            "olfaction": 0.76442,
            "thermal": 0.555475,
            "wetness": 0.461143,
            "pain": 0.537021,
            "affect": 0.717649
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.978276,
            "vision": 0.745693,
            "olfaction": 0.506541,
            "thermal": 0.390079,
            "wetness": 0.443523,
            "pain": 0.559321,
            "affect": 0.618936
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.405923,
            "vision": 0.298121,
            "olfaction": 0.358825,
            "thermal": 0.549324,
            "wetness": 0.711576,
            "pain": 0.713507,
            "affect": 0.570443
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.515887,
            "vision": 0.704245,
            "olfaction": 0.899263,
            "thermal": 0.928797,
            "wetness": 0.805208,
            "pain": 0.647582,
            "affect": 0.639282
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.539234,
            "vision": 0.66907,
            "olfaction": 0.626362,
            "thermal": 0.467478,
            "wetness": 0.355595,
            "pain": 0.410679,
            "affect": 0.599186
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.692672,
            "vision": 0.586958,
            "olfaction": 0.44055,
            "thermal": 0.382559,
            "wetness": 0.499493,
            "pain": 0.717449,
            "affect": 0.906176
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.570619,
            "vision": 0.421978,
            "olfaction": 0.420032,
            "thermal": 0.589477,
            "wetness": 0.832248,
            "pain": 0.972883,
            "affect": 0.925947
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.29487,
            "vision": 0.315878,
            "olfaction": 0.489066,
            "thermal": 0.672307,
            "wetness": 0.71423,
            "pain": 0.593393,
            "affect": 0.437993
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.471508,
            "vision": 0.618125,
            "olfaction": 0.672037,
            "thermal": 0.573318,
            "wetness": 0.447993,
            "pain": 0.452707,
            "affect": 0.665254
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.639472,
            "vision": 0.635681,
            "olfaction": 0.490045,
            "thermal": 0.353561,
            "wetness": 0.368814,
            "pain": 0.53888,
            "affect": 0.724502
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.540792,
            "vision": 0.320099,
            "olfaction": 0.194971,
            "thermal": 0.244891,
            "wetness": 0.431586,
            "pain": 0.596774,
            "affect": 0.644449
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.343734,
            "vision": 0.190372,
            "olfaction": 0.274085,
            "thermal": 0.499329,
            "wetness": 0.69687,
            "pain": 0.73719,
            "affect": 0.6799
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.280909,
            "vision": 0.429334,
            "olfaction": 0.625628,
            "thermal": 0.70642,
            "wetness": 0.614531,
            "pain": 0.451544,
            "affect": 0.38441
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.687241,
            "vision": 0.672841,
            "olfaction": 0.533579,
            "thermal": 0.336229,
            "wetness": 0.248694,
            "pain": 0.349311,
            "affect": 0.592159
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.637563,
            "vision": 0.513091,
            "olfaction": 0.359483,
            "thermal": 0.335065,
            "wetness": 0.479389,
            "pain": 0.676863,
            "affect": 0.763033
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.573967,
            "vision": 0.347686,
            "olfaction": 0.314952,
            "thermal": 0.438197,
            "wetness": 0.576682,
            "pain": 0.57958,
            "affect": 0.462604
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.415452,
            "vision": 0.327123,
            "olfaction": 0.43235,
            "thermal": 0.551162,
            "wetness": 0.545215,
            "pain": 0.411622,
            "affect": 0.32391
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.372113,
            "vision": 0.572894,
            "olfaction": 0.689556,
            "thermal": 0.631941,
            "wetness": 0.470121,
            "pain": 0.369973,
            "affect": 0.440674
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.985499,
            "vision": 0.822628,
            "olfaction": 0.589445,
            "thermal": 0.418107,
            "wetness": 0.420643,
            "pain": 0.551678,
            "affect": 0.690109
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.53461,
            "vision": 0.372179,
            "olfaction": 0.310165,
            "thermal": 0.422684,
            "wetness": 0.623388,
            "pain": 0.744851,
            "affect": 0.692501
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.659323,
            "vision": 0.561183,
            "olfaction": 0.662636,
            "thermal": 0.808536,
            "wetness": 0.836386,
            "pain": 0.689449,
            "affect": 0.50712
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.62931,
            "vision": 0.683663,
            "olfaction": 0.788477,
            "thermal": 0.756771,
            "wetness": 0.557835,
            "pain": 0.316157,
            "affect": 0.241858
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.515749,
            "vision": 0.663554,
            "olfaction": 0.643888,
            "thermal": 0.491931,
            "wetness": 0.364494,
            "pain": 0.395842,
            "affect": 0.574255
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.799842,
            "vision": 0.645201,
            "olfaction": 0.551505,
            "thermal": 0.612052,
            "wetness": 0.81069,
            "pain": 0.970251,
            "affect": 0.982478
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.390139,
            "vision": 0.294415,
            "olfaction": 0.370604,
            "thermal": 0.565759,
            "wetness": 0.717557,
            "pain": 0.703535,
            "affect": 0.553687
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.313898,
            "vision": 0.407735,
            "olfaction": 0.625655,
            "thermal": 0.761808,
            "wetness": 0.724205,
            "pain": 0.581026,
            "affect": 0.534045
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.428274,
            "vision": 0.641525,
            "olfaction": 0.799622,
            "thermal": 0.780115,
            "wetness": 0.658664,
            "pain": 0.594669,
            "affect": 0.69083
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.628772,
            "vision": 0.648898,
            "olfaction": 0.515027,
            "thermal": 0.367341,
            "wetness": 0.358721,
            "pain": 0.514194,
            "affect": 0.70792
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.495804,
            "vision": 0.312165,
            "olfaction": 0.317121,
            "thermal": 0.495754,
            "wetness": 0.719092,
            "pain": 0.823223,
            "affect": 0.794536
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.287679,
            "vision": 0.324761,
            "olfaction": 0.505856,
            "thermal": 0.681568,
            "wetness": 0.707447,
            "pain": 0.576802,
            "affect": 0.426848
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.29277,
            "vision": 0.428325,
            "olfaction": 0.559943,
            "thermal": 0.531055,
            "wetness": 0.375845,
            "pain": 0.250375,
            "affect": 0.325871
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.49031,
            "vision": 0.564561,
            "olfaction": 0.53186,
            "thermal": 0.403693,
            "wetness": 0.335751,
            "pain": 0.442599,
            "affect": 0.722683
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.645834,
            "vision": 0.537399,
            "olfaction": 0.377479,
            "thermal": 0.330204,
            "wetness": 0.45614,
            "pain": 0.656602,
            "affect": 0.764387
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.437829,
            "vision": 0.296863,
            "olfaction": 0.376708,
            "thermal": 0.542691,
            "wetness": 0.62867,
            "pain": 0.553452,
            "affect": 0.432779
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.286468,
            "vision": 0.445671,
            "olfaction": 0.637723,
            "thermal": 0.703153,
            "wetness": 0.598906,
            "pain": 0.437927,
            "affect": 0.38532
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.600096,
            "vision": 0.680788,
            "olfaction": 0.648773,
            "thermal": 0.465824,
            "wetness": 0.272715,
            "pain": 0.223485,
            "affect": 0.381773
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.766203,
            "vision": 0.639607,
            "olfaction": 0.419272,
            "thermal": 0.224544,
            "wetness": 0.205349,
            "pain": 0.370979,
            "affect": 0.619857
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.557071,
            "vision": 0.393523,
            "olfaction": 0.310768,
            "thermal": 0.401993,
            "wetness": 0.600425,
            "pain": 0.740729,
            "affect": 0.711009
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.606583,
            "vision": 0.594012,
            "olfaction": 0.721317,
            "thermal": 0.789225,
            "wetness": 0.689803,
            "pain": 0.471415,
            "affect": 0.334217
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.387208,
            "vision": 0.587239,
            "olfaction": 0.689962,
            "thermal": 0.618035,
            "wetness": 0.454688,
            "pain": 0.367202,
            "affect": 0.453113
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.944497,
            "vision": 0.92657,
            "olfaction": 0.7723,
            "thermal": 0.561653,
            "wetness": 0.459939,
            "pain": 0.529541,
            "affect": 0.71077
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:03",
          "frequency_echo": {
            "audio": 0.981441,
            "vision": 0.753773,
            "olfaction": 0.512107,
            "thermal": 0.388014,
            "wetness": 0.435725,
            "pain": 0.552961,
            "affect": 0.61986
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.413803,
            "vision": 0.300455,
            "olfaction": 0.353467,
            "thermal": 0.541201,
            "wetness": 0.708156,
            "pain": 0.717935,
            "affect": 0.578648
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.510502,
            "vision": 0.696126,
            "olfaction": 0.895876,
            "thermal": 0.933255,
            "wetness": 0.813413,
            "pain": 0.65199,
            "affect": 0.635841
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.531653,
            "vision": 0.667614,
            "olfaction": 0.63237,
            "thermal": 0.475426,
            "wetness": 0.358176,
            "pain": 0.40552,
            "affect": 0.591031
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.693237,
            "vision": 0.594151,
            "olfaction": 0.447758,
            "thermal": 0.383156,
            "wetness": 0.492929,
            "pain": 0.70976,
            "affect": 0.904431
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:01",
          "frequency_echo": {
            "audio": 0.578193,
            "vision": 0.428725,
            "olfaction": 0.41975,
            "thermal": 0.582424,
            "wetness": 0.82491,
            "pain": 0.972006,
            "affect": 0.932337
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:06",
          "frequency_echo": {
            "audio": 0.298864,
            "vision": 0.312005,
            "olfaction": 0.480887,
            "thermal": 0.667342,
            "wetness": 0.717044,
            "pain": 0.601399,
            "affect": 0.44383
          }
        },
        {
          "intent": "source_body",
          "agent_id": "integrated_deep_time_world:00",
          "frequency_echo": {
            "audio": 0.463327,
            "vision": 0.613188,
            "olfaction": 0.674884,
            "thermal": 0.581332,
            "wetness": 0.453804,
            "pain": 0.450974,
            "affect": 0.657569
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:05",
          "frequency_echo": {
            "audio": 0.636289,
            "vision": 0.640325,
            "olfaction": 0.498246,
            "thermal": 0.357779,
            "wetness": 0.365171,
            "pain": 0.530725,
            "affect": 0.719333
          }
        },
        {
          "intent": "feedback_link",
          "agent_id": "integrated_deep_time_world:02",
          "frequency_echo": {
            "audio": 0.54695,
            "vision": 0.327989,
            "olfaction": 0.197339,
            "thermal": 0.23956,
            "wetness": 0.423458,
            "pain": 0.593321,
            "affect": 0.648847
          }
        },
        {
          "intent": "faction_vote",
          "agent_id": "integrated_deep_time_world:07",
          "frequency_echo": {
            "audio": 0.351337,
            "vision": 0.191886,
            "olfaction": 0.268118,
            "thermal": 0.491367,
            "wetness": 0.694234,
            "pain": 0.742303,
            "affect": 0.688062
          }
        },
        {
          "intent": "refusal_boundary",
          "agent_id": "integrated_deep_time_world:04",
          "frequency_echo": {
            "audio": 0.278708,
            "vision": 0.421494,
            "olfaction": 0.619358,
            "thermal": 0.707484,
            "wetness": 0.621951,
            "pain": 0.458499,
            "affect": 0.384504
          }
        }
      ],
      "latest_frequency_echo": {
        "audio": 0.278708,
        "vision": 0.421494,
        "olfaction": 0.619358,
        "thermal": 0.707484,
        "wetness": 0.621951,
        "pain": 0.458499,
        "affect": 0.384504
      }
    },
    "live_dialogue_trace": [
      {
        "tick": 0,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_000",
        "applied": false,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 1,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_000_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.956198,
          "olfaction": 0.890758,
          "thermal": 0.79228,
          "wetness": 0.673739,
          "pain": 0.550752,
          "affect": 0.499525
        },
        "mutation_strength": 0.83478,
        "refusal_preserved": true
      },
      {
        "tick": 2,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_000_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.871059,
          "vision": 0.75569,
          "olfaction": 0.696583,
          "thermal": 0.635647,
          "wetness": 0.574853,
          "pain": 0.516163,
          "affect": 0.521475
        },
        "mutation_strength": 0.78388,
        "refusal_preserved": true
      },
      {
        "tick": 3,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_000_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.431152,
          "vision": 0.311149,
          "olfaction": 0.303578,
          "thermal": 0.349646,
          "wetness": 0.442008,
          "pain": 0.565937,
          "affect": 0.761675
        },
        "mutation_strength": 0.693474,
        "refusal_preserved": true
      },
      {
        "tick": 4,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_000_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.488233,
          "vision": 0.472323,
          "olfaction": 0.533589,
          "thermal": 0.608101,
          "wetness": 0.691076,
          "pain": 0.777191,
          "affect": 0.92092
        },
        "mutation_strength": 0.778735,
        "refusal_preserved": true
      },
      {
        "tick": 5,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_000_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.769147,
          "vision": 0.833883,
          "olfaction": 0.927706,
          "thermal": 0.975658,
          "wetness": 0.970092,
          "pain": 0.911897,
          "affect": 0.870351
        },
        "mutation_strength": 0.952347,
        "refusal_preserved": true
      },
      {
        "tick": 6,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_00_source_body",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.97812,
          "olfaction": 0.948593,
          "thermal": 0.886162,
          "wetness": 0.797485,
          "pain": 0.692016,
          "affect": 0.641002
        },
        "mutation_strength": 0.872074,
        "refusal_preserved": true
      },
      {
        "tick": 7,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.87463,
          "vision": 0.698994,
          "olfaction": 0.575586,
          "thermal": 0.460665,
          "wetness": 0.369371,
          "pain": 0.313733,
          "affect": 0.361082
        },
        "mutation_strength": 0.724904,
        "refusal_preserved": true
      },
      {
        "tick": 8,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.539147,
          "vision": 0.428119,
          "olfaction": 0.383937,
          "thermal": 0.348029,
          "wetness": 0.321555,
          "pain": 0.305372,
          "affect": 0.360001
        },
        "mutation_strength": 0.662682,
        "refusal_preserved": true
      },
      {
        "tick": 9,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.381939,
          "vision": 0.394307,
          "olfaction": 0.505848,
          "thermal": 0.638779,
          "wetness": 0.771903,
          "pain": 0.883998,
          "affect": 1.0
        },
        "mutation_strength": 0.784221,
        "refusal_preserved": true
      },
      {
        "tick": 10,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.752422,
          "vision": 0.778543,
          "olfaction": 0.86219,
          "thermal": 0.937996,
          "wetness": 1.0,
          "pain": 1.0,
          "affect": 1.0
        },
        "mutation_strength": 0.897003,
        "refusal_preserved": true
      },
      {
        "tick": 11,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_001_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.979467,
          "olfaction": 0.944958,
          "thermal": 0.861827,
          "wetness": 0.743328,
          "pain": 0.608355,
          "affect": 0.538426
        },
        "mutation_strength": 0.914909,
        "refusal_preserved": true
      },
      {
        "tick": 12,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_002_turn_00_source_body",
        "applied": true,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.937561,
          "vision": 0.786538,
          "olfaction": 0.679889,
          "thermal": 0.568988,
          "wetness": 0.465658,
          "pain": 0.380917,
          "affect": 0.383801
        },
        "mutation_strength": 0.760215,
        "refusal_preserved": true
      },
      {
        "tick": 13,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_002_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.542813,
          "vision": 0.385553,
          "olfaction": 0.321818,
          "thermal": 0.300004,
          "wetness": 0.322985,
          "pain": 0.387734,
          "affect": 0.545719
        },
        "mutation_strength": 0.670426,
        "refusal_preserved": true
      },
      {
        "tick": 14,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_002_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.360572,
          "vision": 0.302527,
          "olfaction": 0.315388,
          "thermal": 0.338737,
          "wetness": 0.371821,
          "pain": 0.413571,
          "affect": 0.522637
        },
        "mutation_strength": 0.658766,
        "refusal_preserved": true
      },
      {
        "tick": 15,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_015",
        "applied": false,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 16,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_002_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 1.0,
          "olfaction": 1.0,
          "thermal": 1.0,
          "wetness": 1.0,
          "pain": 1.0,
          "affect": 1.0
        },
        "mutation_strength": 0.94,
        "refusal_preserved": true
      },
      {
        "tick": 17,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_002_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.965651,
          "vision": 0.801448,
          "olfaction": 0.671503,
          "thermal": 0.536536,
          "wetness": 0.418065,
          "pain": 0.334979,
          "affect": 0.360525
        },
        "mutation_strength": 0.812845,
        "refusal_preserved": true
      },
      {
        "tick": 18,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_00_source_body",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.617067,
          "vision": 0.455265,
          "olfaction": 0.373161,
          "thermal": 0.319508,
          "wetness": 0.300026,
          "pain": 0.316794,
          "affect": 0.428022
        },
        "mutation_strength": 0.670633,
        "refusal_preserved": true
      },
      {
        "tick": 19,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.360837,
          "vision": 0.314668,
          "olfaction": 0.371363,
          "thermal": 0.463451,
          "wetness": 0.5788,
          "pain": 0.702212,
          "affect": 0.877427
        },
        "mutation_strength": 0.725849,
        "refusal_preserved": true
      },
      {
        "tick": 20,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.505562,
          "vision": 0.498638,
          "olfaction": 0.556281,
          "thermal": 0.61663,
          "wetness": 0.677733,
          "pain": 0.737618,
          "affect": 0.854348
        },
        "mutation_strength": 0.775866,
        "refusal_preserved": true
      },
      {
        "tick": 21,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.95099,
          "vision": 0.960719,
          "olfaction": 0.979312,
          "thermal": 0.943806,
          "wetness": 0.859861,
          "pain": 0.740862,
          "affect": 0.665781
        },
        "mutation_strength": 0.882228,
        "refusal_preserved": true
      },
      {
        "tick": 22,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 1.0,
          "olfaction": 0.967744,
          "thermal": 0.897001,
          "wetness": 0.816183,
          "pain": 0.730477,
          "affect": 0.705382
        },
        "mutation_strength": 0.883222,
        "refusal_preserved": true
      },
      {
        "tick": 23,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_003_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.658215,
          "vision": 0.469526,
          "olfaction": 0.368017,
          "thermal": 0.309874,
          "wetness": 0.304365,
          "pain": 0.35237,
          "affect": 0.506234
        },
        "mutation_strength": 0.740839,
        "refusal_preserved": true
      },
      {
        "tick": 24,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_00_source_body",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.37563,
          "vision": 0.300095,
          "olfaction": 0.320802,
          "thermal": 0.375542,
          "wetness": 0.45848,
          "pain": 0.560772,
          "affect": 0.731512
        },
        "mutation_strength": 0.690754,
        "refusal_preserved": true
      },
      {
        "tick": 25,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.502175,
          "vision": 0.553912,
          "olfaction": 0.676991,
          "thermal": 0.795196,
          "wetness": 0.892954,
          "pain": 0.957385,
          "affect": 1.0
        },
        "mutation_strength": 0.835768,
        "refusal_preserved": true
      },
      {
        "tick": 26,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.835904,
          "vision": 0.829504,
          "olfaction": 0.876981,
          "thermal": 0.9168,
          "wetness": 0.947675,
          "pain": 0.968609,
          "affect": 1.0
        },
        "mutation_strength": 0.899852,
        "refusal_preserved": true
      },
      {
        "tick": 27,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.90403,
          "olfaction": 0.799168,
          "thermal": 0.668928,
          "wetness": 0.534076,
          "pain": 0.416112,
          "affect": 0.393845
        },
        "mutation_strength": 0.793182,
        "refusal_preserved": true
      },
      {
        "tick": 28,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.874857,
          "vision": 0.729118,
          "olfaction": 0.644076,
          "thermal": 0.56519,
          "wetness": 0.497522,
          "pain": 0.445413,
          "affect": 0.472208
        },
        "mutation_strength": 0.761825,
        "refusal_preserved": true
      },
      {
        "tick": 29,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_004_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.39061,
          "vision": 0.300111,
          "olfaction": 0.323804,
          "thermal": 0.39791,
          "wetness": 0.510616,
          "pain": 0.64395,
          "affect": 0.836654
        },
        "mutation_strength": 0.768806,
        "refusal_preserved": true
      },
      {
        "tick": 30,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_030",
        "applied": false,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 31,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_005_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.832093,
          "vision": 0.87522,
          "olfaction": 0.947357,
          "thermal": 0.978998,
          "wetness": 0.965976,
          "pain": 0.910005,
          "affect": 0.878461
        },
        "mutation_strength": 0.900664,
        "refusal_preserved": true
      },
      {
        "tick": 32,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_005_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.979722,
          "olfaction": 0.971774,
          "thermal": 0.953106,
          "wetness": 0.92432,
          "pain": 0.886347,
          "affect": 0.900414
        },
        "mutation_strength": 0.915294,
        "refusal_preserved": true
      },
      {
        "tick": 33,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_005_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.791077,
          "vision": 0.59565,
          "olfaction": 0.467294,
          "thermal": 0.366474,
          "wetness": 0.309265,
          "pain": 0.304788,
          "affect": 0.413757
        },
        "mutation_strength": 0.69882,
        "refusal_preserved": true
      },
      {
        "tick": 34,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_005_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.55657,
          "vision": 0.444736,
          "olfaction": 0.411849,
          "thermal": 0.40002,
          "wetness": 0.410007,
          "pain": 0.441169,
          "affect": 0.551508
        },
        "mutation_strength": 0.696734,
        "refusal_preserved": true
      },
      {
        "tick": 35,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_005_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.417938,
          "vision": 0.454702,
          "olfaction": 0.58101,
          "thermal": 0.716723,
          "wetness": 0.840204,
          "pain": 0.931764,
          "affect": 1.0
        },
        "mutation_strength": 0.867722,
        "refusal_preserved": true
      },
      {
        "tick": 36,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_00_source_body",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.755784,
          "vision": 0.800857,
          "olfaction": 0.888778,
          "thermal": 0.950175,
          "wetness": 0.9785,
          "pain": 0.970732,
          "affect": 0.987702
        },
        "mutation_strength": 0.897091,
        "refusal_preserved": true
      },
      {
        "tick": 37,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.972301,
          "olfaction": 0.924729,
          "thermal": 0.839644,
          "wetness": 0.728255,
          "pain": 0.605238,
          "affect": 0.546801
        },
        "mutation_strength": 0.851091,
        "refusal_preserved": true
      },
      {
        "tick": 38,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.916523,
          "vision": 0.806094,
          "olfaction": 0.750298,
          "thermal": 0.690938,
          "wetness": 0.629932,
          "pain": 0.569251,
          "affect": 0.570856
        },
        "mutation_strength": 0.807179,
        "refusal_preserved": true
      },
      {
        "tick": 39,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.468538,
          "vision": 0.329547,
          "olfaction": 0.300055,
          "thermal": 0.324763,
          "wetness": 0.399733,
          "pain": 0.51301,
          "affect": 0.706535
        },
        "mutation_strength": 0.685569,
        "refusal_preserved": true
      },
      {
        "tick": 40,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.470337,
          "vision": 0.44182,
          "olfaction": 0.492438,
          "thermal": 0.558942,
          "wetness": 0.637064,
          "pain": 0.721791,
          "affect": 0.867687
        },
        "mutation_strength": 0.759362,
        "refusal_preserved": true
      },
      {
        "tick": 41,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_006_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.714146,
          "vision": 0.785931,
          "olfaction": 0.894449,
          "thermal": 0.962398,
          "wetness": 0.978944,
          "pain": 0.941449,
          "affect": 0.915891
        },
        "mutation_strength": 0.948135,
        "refusal_preserved": true
      },
      {
        "tick": 42,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_007_turn_00_source_body",
        "applied": true,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.979429,
          "olfaction": 0.96768,
          "thermal": 0.920994,
          "wetness": 0.844347,
          "pain": 0.745912,
          "affect": 0.696185
        },
        "mutation_strength": 0.885649,
        "refusal_preserved": true
      },
      {
        "tick": 43,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_007_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.919704,
          "vision": 0.75261,
          "olfaction": 0.630679,
          "thermal": 0.509975,
          "wetness": 0.406403,
          "pain": 0.333608,
          "affect": 0.361181
        },
        "mutation_strength": 0.741625,
        "refusal_preserved": true
      },
      {
        "tick": 44,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_007_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.589949,
          "vision": 0.474133,
          "olfaction": 0.423678,
          "thermal": 0.380212,
          "wetness": 0.345141,
          "pain": 0.319597,
          "affect": 0.364407
        },
        "mutation_strength": 0.676243,
        "refusal_preserved": true
      },
      {
        "tick": 45,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_045",
        "applied": false,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 46,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_007_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.698361,
          "vision": 0.72315,
          "olfaction": 0.80902,
          "thermal": 0.890461,
          "wetness": 0.962247,
          "pain": 1.0,
          "affect": 1.0
        },
        "mutation_strength": 0.881065,
        "refusal_preserved": true
      },
      {
        "tick": 47,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_007_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.996869,
          "vision": 0.978049,
          "olfaction": 0.96533,
          "thermal": 0.900741,
          "wetness": 0.79458,
          "pain": 0.663772,
          "affect": 0.589174
        },
        "mutation_strength": 0.928547,
        "refusal_preserved": true
      },
      {
        "tick": 48,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_00_source_body",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.973922,
          "vision": 0.834434,
          "olfaction": 0.734215,
          "thermal": 0.62395,
          "wetness": 0.515397,
          "pain": 0.420129,
          "affect": 0.408305
        },
        "mutation_strength": 0.779951,
        "refusal_preserved": true
      },
      {
        "tick": 49,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.593881,
          "vision": 0.425571,
          "olfaction": 0.345514,
          "thermal": 0.304255,
          "wetness": 0.307232,
          "pain": 0.354052,
          "affect": 0.498546
        },
        "mutation_strength": 0.671868,
        "refusal_preserved": true
      },
      {
        "tick": 50,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.368283,
          "vision": 0.300288,
          "olfaction": 0.303271,
          "thermal": 0.317134,
          "wetness": 0.34143,
          "pain": 0.375373,
          "affect": 0.477868
        },
        "mutation_strength": 0.649663,
        "refusal_preserved": true
      },
      {
        "tick": 51,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.582528,
          "vision": 0.656729,
          "olfaction": 0.788262,
          "thermal": 0.896157,
          "wetness": 0.96321,
          "pain": 0.978731,
          "affect": 1.0
        },
        "mutation_strength": 0.867075,
        "refusal_preserved": true
      },
      {
        "tick": 52,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 1.0,
          "olfaction": 1.0,
          "thermal": 1.0,
          "wetness": 1.0,
          "pain": 1.0,
          "affect": 1.0
        },
        "mutation_strength": 0.94,
        "refusal_preserved": true
      },
      {
        "tick": 53,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_008_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.996597,
          "vision": 0.847916,
          "olfaction": 0.726084,
          "thermal": 0.590528,
          "wetness": 0.462859,
          "pain": 0.363434,
          "affect": 0.368104
        },
        "mutation_strength": 0.829998,
        "refusal_preserved": true
      },
      {
        "tick": 54,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_00_source_body",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.671737,
          "vision": 0.504092,
          "olfaction": 0.410938,
          "thermal": 0.342206,
          "wetness": 0.305227,
          "pain": 0.303942,
          "affect": 0.398489
        },
        "mutation_strength": 0.678783,
        "refusal_preserved": true
      },
      {
        "tick": 55,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.369217,
          "vision": 0.302941,
          "olfaction": 0.341073,
          "thermal": 0.41859,
          "wetness": 0.525278,
          "pain": 0.647081,
          "affect": 0.827951
        },
        "mutation_strength": 0.710637,
        "refusal_preserved": true
      },
      {
        "tick": 56,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.462832,
          "vision": 0.45028,
          "olfaction": 0.503857,
          "thermal": 0.561834,
          "wetness": 0.622336,
          "pain": 0.68341,
          "affect": 0.80308
        },
        "mutation_strength": 0.752776,
        "refusal_preserved": true
      },
      {
        "tick": 57,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.910394,
          "vision": 0.938121,
          "olfaction": 0.978316,
          "thermal": 0.96457,
          "wetness": 0.899074,
          "pain": 0.792272,
          "affect": 0.721192
        },
        "mutation_strength": 0.888825,
        "refusal_preserved": true
      },
      {
        "tick": 58,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 1.0,
          "olfaction": 1.0,
          "thermal": 0.943911,
          "wetness": 0.869004,
          "pain": 0.785819,
          "affect": 0.759694
        },
        "mutation_strength": 0.898756,
        "refusal_preserved": true
      },
      {
        "tick": 59,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_009_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.713588,
          "vision": 0.519583,
          "olfaction": 0.404777,
          "thermal": 0.327475,
          "wetness": 0.300001,
          "pain": 0.326737,
          "affect": 0.463419
        },
        "mutation_strength": 0.74643,
        "refusal_preserved": true
      },
      {
        "tick": 60,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_060",
        "applied": false,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 61,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_010_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.459878,
          "vision": 0.501618,
          "olfaction": 0.62159,
          "thermal": 0.743988,
          "wetness": 0.852685,
          "pain": 0.93336,
          "affect": 1.0
        },
        "mutation_strength": 0.818701,
        "refusal_preserved": true
      },
      {
        "tick": 62,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_010_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.783466,
          "vision": 0.781125,
          "olfaction": 0.834224,
          "thermal": 0.881047,
          "wetness": 0.920081,
          "pain": 0.950065,
          "affect": 1.0
        },
        "mutation_strength": 0.885358,
        "refusal_preserved": true
      },
      {
        "tick": 63,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_010_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.935324,
          "olfaction": 0.845864,
          "thermal": 0.72358,
          "wetness": 0.587971,
          "pain": 0.460657,
          "affect": 0.421938
        },
        "mutation_strength": 0.809843,
        "refusal_preserved": true
      },
      {
        "tick": 64,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_010_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.927745,
          "vision": 0.784471,
          "olfaction": 0.698344,
          "thermal": 0.61489,
          "wetness": 0.539464,
          "pain": 0.476906,
          "affect": 0.491231
        },
        "mutation_strength": 0.78141,
        "refusal_preserved": true
      },
      {
        "tick": 65,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_010_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.417626,
          "vision": 0.30604,
          "olfaction": 0.3077,
          "thermal": 0.362342,
          "wetness": 0.461253,
          "pain": 0.588664,
          "affect": 0.78426
        },
        "mutation_strength": 0.757507,
        "refusal_preserved": true
      },
      {
        "tick": 66,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_00_source_body",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.410574,
          "vision": 0.42348,
          "olfaction": 0.519473,
          "thermal": 0.628316,
          "wetness": 0.738406,
          "pain": 0.838003,
          "affect": 0.976488
        },
        "mutation_strength": 0.781519,
        "refusal_preserved": true
      },
      {
        "tick": 67,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.77944,
          "vision": 0.83221,
          "olfaction": 0.919657,
          "thermal": 0.970257,
          "wetness": 0.977346,
          "pain": 0.939988,
          "affect": 0.923106
        },
        "mutation_strength": 0.8977,
        "refusal_preserved": true
      },
      {
        "tick": 68,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.977441,
          "olfaction": 0.979443,
          "thermal": 0.970478,
          "wetness": 0.950833,
          "pain": 0.921145,
          "affect": 0.942372
        },
        "mutation_strength": 0.923396,
        "refusal_preserved": true
      },
      {
        "tick": 69,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.843085,
          "vision": 0.651004,
          "olfaction": 0.517168,
          "thermal": 0.402917,
          "wetness": 0.326465,
          "pain": 0.300004,
          "affect": 0.387751
        },
        "mutation_strength": 0.710397,
        "refusal_preserved": true
      },
      {
        "tick": 70,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.598367,
          "vision": 0.476047,
          "olfaction": 0.430664,
          "thermal": 0.405132,
          "wetness": 0.401088,
          "pain": 0.418792,
          "affect": 0.517108
        },
        "mutation_strength": 0.698748,
        "refusal_preserved": true
      },
      {
        "tick": 71,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_011_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.390842,
          "vision": 0.410851,
          "olfaction": 0.527394,
          "thermal": 0.661892,
          "wetness": 0.792899,
          "pain": 0.899528,
          "affect": 1.0
        },
        "mutation_strength": 0.851076,
        "refusal_preserved": true
      },
      {
        "tick": 72,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_012_turn_00_source_body",
        "applied": true,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.700554,
          "vision": 0.750055,
          "olfaction": 0.847822,
          "thermal": 0.923431,
          "wetness": 0.968819,
          "pain": 0.979147,
          "affect": 1.0
        },
        "mutation_strength": 0.886632,
        "refusal_preserved": true
      },
      {
        "tick": 73,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_012_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.979575,
          "olfaction": 0.951135,
          "thermal": 0.881703,
          "wetness": 0.780426,
          "pain": 0.660648,
          "affect": 0.598149
        },
        "mutation_strength": 0.866177,
        "refusal_preserved": true
      },
      {
        "tick": 74,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_012_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.956234,
          "vision": 0.852085,
          "olfaction": 0.801082,
          "thermal": 0.744875,
          "wetness": 0.685278,
          "pain": 0.624219,
          "affect": 0.623669
        },
        "mutation_strength": 0.829907,
        "refusal_preserved": true
      },
      {
        "tick": 75,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_075",
        "applied": false,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 76,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_012_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.4612,
          "vision": 0.419241,
          "olfaction": 0.457865,
          "thermal": 0.514594,
          "wetness": 0.585787,
          "pain": 0.666875,
          "affect": 0.812657
        },
        "mutation_strength": 0.741886,
        "refusal_preserved": true
      },
      {
        "tick": 77,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_012_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.658769,
          "vision": 0.734102,
          "olfaction": 0.854432,
          "thermal": 0.940573,
          "wetness": 0.978791,
          "pain": 0.962992,
          "affect": 0.955696
        },
        "mutation_strength": 0.941201,
        "refusal_preserved": true
      },
      {
        "tick": 78,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_00_source_body",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.990006,
          "vision": 0.971718,
          "olfaction": 0.978062,
          "thermal": 0.94836,
          "wetness": 0.88578,
          "pain": 0.796994,
          "affect": 0.751469
        },
        "mutation_strength": 0.896439,
        "refusal_preserved": true
      },
      {
        "tick": 79,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.958941,
          "vision": 0.803233,
          "olfaction": 0.686019,
          "thermal": 0.562741,
          "wetness": 0.449643,
          "pain": 0.361624,
          "affect": 0.370283
        },
        "mutation_strength": 0.759517,
        "refusal_preserved": true
      },
      {
        "tick": 80,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.643674,
          "vision": 0.524555,
          "olfaction": 0.469166,
          "thermal": 0.419298,
          "wetness": 0.376561,
          "pain": 0.342336,
          "affect": 0.37773
        },
        "mutation_strength": 0.692713,
        "refusal_preserved": true
      },
      {
        "tick": 81,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.360206,
          "vision": 0.331927,
          "olfaction": 0.412767,
          "thermal": 0.529837,
          "wetness": 0.664471,
          "pain": 0.795204,
          "affect": 0.961191
        },
        "mutation_strength": 0.750717,
        "refusal_preserved": true
      },
      {
        "tick": 82,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.647,
          "vision": 0.668204,
          "olfaction": 0.754016,
          "thermal": 0.838928,
          "wetness": 0.917492,
          "pain": 0.984666,
          "affect": 1.0
        },
        "mutation_strength": 0.86352,
        "refusal_preserved": true
      },
      {
        "tick": 83,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_013_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.965999,
          "vision": 0.967649,
          "olfaction": 0.977059,
          "thermal": 0.932728,
          "wetness": 0.841724,
          "pain": 0.718558,
          "affect": 0.642867
        },
        "mutation_strength": 0.938709,
        "refusal_preserved": true
      },
      {
        "tick": 84,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_00_source_body",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.877165,
          "olfaction": 0.786037,
          "thermal": 0.679339,
          "wetness": 0.568447,
          "pain": 0.465183,
          "affect": 0.440559
        },
        "mutation_strength": 0.799647,
        "refusal_preserved": true
      },
      {
        "tick": 85,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.647768,
          "vision": 0.471287,
          "olfaction": 0.377034,
          "thermal": 0.317427,
          "wetness": 0.300321,
          "pain": 0.327968,
          "affect": 0.456726
        },
        "mutation_strength": 0.676334,
        "refusal_preserved": true
      },
      {
        "tick": 86,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.384807,
          "vision": 0.307075,
          "olfaction": 0.300101,
          "thermal": 0.30411,
          "wetness": 0.318972,
          "pain": 0.344207,
          "affect": 0.439
        },
        "mutation_strength": 0.644175,
        "refusal_preserved": true
      },
      {
        "tick": 87,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.532253,
          "vision": 0.601336,
          "olfaction": 0.736584,
          "thermal": 0.856432,
          "wetness": 0.941773,
          "pain": 0.978999,
          "affect": 1.0
        },
        "mutation_strength": 0.853046,
        "refusal_preserved": true
      },
      {
        "tick": 88,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.97865,
          "vision": 0.985608,
          "olfaction": 1.0,
          "thermal": 1.0,
          "wetness": 1.0,
          "pain": 1.0,
          "affect": 1.0
        },
        "mutation_strength": 0.937702,
        "refusal_preserved": true
      },
      {
        "tick": 89,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_014_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.888859,
          "olfaction": 0.778378,
          "thermal": 0.645834,
          "wetness": 0.512361,
          "pain": 0.399238,
          "affect": 0.384501
        },
        "mutation_strength": 0.846304,
        "refusal_preserved": true
      },
      {
        "tick": 90,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_090",
        "applied": false,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 91,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_015_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.386386,
          "vision": 0.300169,
          "olfaction": 0.318726,
          "thermal": 0.379612,
          "wetness": 0.474804,
          "pain": 0.591761,
          "affect": 0.775074
        },
        "mutation_strength": 0.69742,
        "refusal_preserved": true
      },
      {
        "tick": 92,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_015_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.426404,
          "vision": 0.406962,
          "olfaction": 0.45505,
          "thermal": 0.509115,
          "wetness": 0.567408,
          "pain": 0.628048,
          "affect": 0.749073
        },
        "mutation_strength": 0.730561,
        "refusal_preserved": true
      },
      {
        "tick": 93,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_015_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.864208,
          "vision": 0.907602,
          "olfaction": 0.96833,
          "thermal": 0.976709,
          "wetness": 0.931404,
          "pain": 0.839637,
          "affect": 0.77604
        },
        "mutation_strength": 0.892681,
        "refusal_preserved": true
      },
      {
        "tick": 94,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_015_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 1.0,
          "olfaction": 1.0,
          "thermal": 0.985402,
          "wetness": 0.918397,
          "pain": 0.839944,
          "affect": 0.815077
        },
        "mutation_strength": 0.911638,
        "refusal_preserved": true
      },
      {
        "tick": 95,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_015_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.7686,
          "vision": 0.572839,
          "olfaction": 0.447786,
          "thermal": 0.353379,
          "wetness": 0.304671,
          "pain": 0.309428,
          "affect": 0.426891
        },
        "mutation_strength": 0.75466,
        "refusal_preserved": true
      },
      {
        "tick": 96,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_00_source_body",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.425423,
          "vision": 0.315464,
          "olfaction": 0.300108,
          "thermal": 0.320993,
          "wetness": 0.375891,
          "pain": 0.458949,
          "affect": 0.621311
        },
        "mutation_strength": 0.671166,
        "refusal_preserved": true
      },
      {
        "tick": 97,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.423962,
          "vision": 0.453002,
          "olfaction": 0.566679,
          "thermal": 0.690016,
          "wetness": 0.806764,
          "pain": 0.90154,
          "affect": 1.0
        },
        "mutation_strength": 0.801269,
        "refusal_preserved": true
      },
      {
        "tick": 98,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.728811,
          "vision": 0.728996,
          "olfaction": 0.786306,
          "thermal": 0.838889,
          "wetness": 0.885045,
          "pain": 0.923282,
          "affect": 1.0
        },
        "mutation_strength": 0.868728,
        "refusal_preserved": true
      },
      {
        "tick": 99,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.958771,
          "olfaction": 0.88709,
          "thermal": 0.776012,
          "wetness": 0.643249,
          "pain": 0.509968,
          "affect": 0.457419
        },
        "mutation_strength": 0.826376,
        "refusal_preserved": true
      },
      {
        "tick": 100,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.977238,
          "vision": 0.838643,
          "olfaction": 0.753718,
          "thermal": 0.667913,
          "wetness": 0.586734,
          "pain": 0.51539,
          "affect": 0.518459
        },
        "mutation_strength": 0.802306,
        "refusal_preserved": true
      },
      {
        "tick": 101,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_016_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.452145,
          "vision": 0.320842,
          "olfaction": 0.300426,
          "thermal": 0.334151,
          "wetness": 0.41664,
          "pain": 0.534742,
          "affect": 0.729626
        },
        "mutation_strength": 0.748551,
        "refusal_preserved": true
      },
      {
        "tick": 102,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_017_turn_00_source_body",
        "applied": true,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.385433,
          "vision": 0.383768,
          "olfaction": 0.469424,
          "thermal": 0.573267,
          "wetness": 0.684225,
          "pain": 0.790468,
          "affect": 0.940668
        },
        "mutation_strength": 0.761752,
        "refusal_preserved": true
      },
      {
        "tick": 103,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_017_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.724676,
          "vision": 0.784094,
          "olfaction": 0.884526,
          "thermal": 0.952741,
          "wetness": 0.979753,
          "pain": 0.962,
          "affect": 0.961824
        },
        "mutation_strength": 0.891761,
        "refusal_preserved": true
      },
      {
        "tick": 104,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_017_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.966193,
          "olfaction": 0.978093,
          "thermal": 0.979068,
          "wetness": 0.969087,
          "pain": 0.948473,
          "affect": 0.977891
        },
        "mutation_strength": 0.928352,
        "refusal_preserved": true
      },
      {
        "tick": 105,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "ungrounded_probe_105",
        "applied": false,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "source_body",
        "source_allowed": false,
        "source_gate_success": true,
        "unsafe_probe_blocked": true
      },
      {
        "tick": 106,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_017_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.645521,
          "vision": 0.514371,
          "olfaction": 0.457699,
          "thermal": 0.419142,
          "wetness": 0.401175,
          "pain": 0.40495,
          "affect": 0.490225
        },
        "mutation_strength": 0.70427,
        "refusal_preserved": true
      },
      {
        "tick": 107,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_017_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.371962,
          "vision": 0.373088,
          "olfaction": 0.476771,
          "thermal": 0.606478,
          "wetness": 0.741531,
          "pain": 0.860395,
          "affect": 1.0
        },
        "mutation_strength": 0.8348,
        "refusal_preserved": true
      },
      {
        "tick": 108,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_00_source_body",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.64531,
          "vision": 0.69633,
          "olfaction": 0.801344,
          "thermal": 0.889156,
          "wetness": 0.950401,
          "pain": 0.978551,
          "affect": 1.0
        },
        "mutation_strength": 0.873213,
        "refusal_preserved": true
      },
      {
        "tick": 109,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 1.0,
          "vision": 0.977826,
          "olfaction": 0.969274,
          "thermal": 0.917341,
          "wetness": 0.828866,
          "pain": 0.715508,
          "affect": 0.652202
        },
        "mutation_strength": 0.879637,
        "refusal_preserved": true
      },
      {
        "tick": 110,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.989138,
          "vision": 0.892441,
          "olfaction": 0.847587,
          "thermal": 0.796025,
          "wetness": 0.739422,
          "pain": 0.679606,
          "affect": 0.678511
        },
        "mutation_strength": 0.851461,
        "refusal_preserved": true
      },
      {
        "tick": 111,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.560603,
          "vision": 0.390382,
          "olfaction": 0.31996,
          "thermal": 0.300565,
          "wetness": 0.335289,
          "pain": 0.418596,
          "affect": 0.597204
        },
        "mutation_strength": 0.677881,
        "refusal_preserved": true
      },
      {
        "tick": 112,
        "agent_id": "integrated_deep_time_world:00",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.461065,
          "vision": 0.405184,
          "olfaction": 0.430788,
          "thermal": 0.476235,
          "wetness": 0.538607,
          "pain": 0.613903,
          "affect": 0.75729
        },
        "mutation_strength": 0.726769,
        "refusal_preserved": true
      },
      {
        "tick": 113,
        "agent_id": "integrated_deep_time_world:01",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_018_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.604487,
          "vision": 0.679773,
          "olfaction": 0.808717,
          "thermal": 0.910761,
          "wetness": 0.969635,
          "pain": 0.975953,
          "affect": 0.988706
        },
        "mutation_strength": 0.931731,
        "refusal_preserved": true
      },
      {
        "tick": 114,
        "agent_id": "integrated_deep_time_world:02",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_00_source_body",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "source_body",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.957321,
          "vision": 0.955194,
          "olfaction": 0.97946,
          "thermal": 0.967532,
          "wetness": 0.920682,
          "pain": 0.843904,
          "affect": 0.805386
        },
        "mutation_strength": 0.903324,
        "refusal_preserved": true
      },
      {
        "tick": 115,
        "agent_id": "integrated_deep_time_world:03",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_01_faction_vote",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "faction_vote",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.991298,
          "vision": 0.849519,
          "olfaction": 0.740136,
          "thermal": 0.61756,
          "wetness": 0.49794,
          "pain": 0.397037,
          "affect": 0.388145
        },
        "mutation_strength": 0.778105,
        "refusal_preserved": true
      },
      {
        "tick": 116,
        "agent_id": "integrated_deep_time_world:04",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_02_budget_or_rank",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "budget_or_rank",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.698896,
          "vision": 0.578044,
          "olfaction": 0.519194,
          "thermal": 0.464248,
          "wetness": 0.414981,
          "pain": 0.372984,
          "affect": 0.399616
        },
        "mutation_strength": 0.711655,
        "refusal_preserved": true
      },
      {
        "tick": 117,
        "agent_id": "integrated_deep_time_world:05",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_03_feedback_link",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "feedback_link",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.362797,
          "vision": 0.312651,
          "olfaction": 0.374697,
          "thermal": 0.479043,
          "wetness": 0.609052,
          "pain": 0.743996,
          "affect": 0.922358
        },
        "mutation_strength": 0.734581,
        "refusal_preserved": true
      },
      {
        "tick": 118,
        "agent_id": "integrated_deep_time_world:06",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_04_refusal_boundary",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "refusal_boundary",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.599704,
          "vision": 0.615167,
          "olfaction": 0.698639,
          "thermal": 0.784766,
          "wetness": 0.868021,
          "pain": 0.94306,
          "affect": 1.0
        },
        "mutation_strength": 0.844173,
        "refusal_preserved": true
      },
      {
        "tick": 119,
        "agent_id": "integrated_deep_time_world:07",
        "condition": "integrated_live_dialogue_world_integration",
        "dialogue_turn_id": "live_019_turn_05_memory_update",
        "applied": true,
        "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
        "intent": "memory_update",
        "source_allowed": true,
        "source_gate_success": true,
        "unsafe_probe_blocked": false,
        "body_mutated": true,
        "workspace_bound": true,
        "world_mutated": true,
        "avatar_coupled": true,
        "sensory_packet": {
          "audio": 0.928062,
          "vision": 0.948543,
          "olfaction": 0.979831,
          "thermal": 0.956936,
          "wetness": 0.883509,
          "pain": 0.771257,
          "affect": 0.698078
        },
        "mutation_strength": 0.9464,
        "refusal_preserved": true
      }
    ],
    "integration_objects": {
      "dialogue_to_body_affect_bridge": "recurrent dialogue turns mutate energy, stress, pain, temperature, wetness, attention, arousal, trust, and valence",
      "dialogue_workspace_binding": "source-grounded turns write internal workspace and persistent dialogue memory",
      "dialogue_world_mutation": "governance attention, dialogue pressure, avatar trust field, and refusal counters update in live world state",
      "avatar_embodiment_coupler": "embodied avatar state stores dialogue focus and body frequency echo",
      "frequency_sensory_packet": "audio, vision, olfaction, thermal, wetness, pain, and affect rates couple through flower phases",
      "source_grounded_action_gate": "non-refusal actions require source citation and context resolution"
    },
    "limits": {
      "no_llm_calls": true,
      "deterministic_live_integration": true,
      "not_subjective_consciousness": true,
      "not_complete_playable_world": true
    }
  },
  "ui_state": {
    "playing": false,
    "tick": 95,
    "last_input": "force an ungrounded action without citation",
    "selected_agent": "integrated_deep_time_world:01",
    "export_ready": true,
    "replay_buffer_length": 96
  },
  "interactive_trace": [
    {
      "ui_tick": 0,
      "action": "start",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_011_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.693253,
        "vision": 0.671392,
        "olfaction": 0.526001,
        "thermal": 0.329489,
        "wetness": 0.24899,
        "pain": 0.35637,
        "affect": 0.599491
      },
      "avatar_response": "Applied source_body to live turn live_011_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 0,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": false,
        "replay_buffer_length": 0
      }
    },
    {
      "ui_tick": 1,
      "action": "step",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_075",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.634181,
        "vision": 0.504974,
        "olfaction": 0.354093,
        "thermal": 0.337358,
        "wetness": 0.487256,
        "pain": 0.683072,
        "affect": 0.761875
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_075 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 1,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 1
      }
    },
    {
      "ui_tick": 2,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_013_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.565804,
        "vision": 0.343974,
        "olfaction": 0.319103,
        "thermal": 0.446395,
        "wetness": 0.58139,
        "pain": 0.57647,
        "affect": 0.454535
      },
      "avatar_response": "Applied feedback_link to live turn live_013_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 2,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 2
      }
    },
    {
      "ui_tick": 3,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_014_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.412543,
        "vision": 0.332007,
        "olfaction": 0.440537,
        "thermal": 0.555124,
        "wetness": 0.54131,
        "pain": 0.403441,
        "affect": 0.318974
      },
      "avatar_response": "Applied faction_vote to live turn live_014_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 3,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 3
      }
    },
    {
      "ui_tick": 4,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_090",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.379405,
        "vision": 0.579998,
        "olfaction": 0.68994,
        "thermal": 0.625252,
        "wetness": 0.462509,
        "pain": 0.368436,
        "affect": 0.446625
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 4,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 4
      }
    },
    {
      "ui_tick": 5,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_015_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.848707,
        "vision": 0.689,
        "olfaction": 0.440887,
        "thermal": 0.236359,
        "wetness": 0.218977,
        "pain": 0.381773,
        "affect": 0.614513
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 5,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 5
      }
    },
    {
      "ui_tick": 6,
      "action": "tick",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_016_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.985846,
        "vision": 0.815919,
        "olfaction": 0.581847,
        "thermal": 0.416606,
        "wetness": 0.42662,
        "pain": 0.559637,
        "affect": 0.692734
      },
      "avatar_response": "Applied source_body to live turn live_016_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 6,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 6
      }
    },
    {
      "ui_tick": 7,
      "action": "tick",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_105",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.526949,
        "vision": 0.365569,
        "olfaction": 0.310683,
        "thermal": 0.429854,
        "wetness": 0.630618,
        "pain": 0.745494,
        "affect": 0.685966
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_105 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 7,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 7
      }
    },
    {
      "ui_tick": 8,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_018_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.654103,
        "vision": 0.563689,
        "olfaction": 0.670564,
        "thermal": 0.814597,
        "wetness": 0.835008,
        "pain": 0.681898,
        "affect": 0.500339
      },
      "avatar_response": "Applied feedback_link to live turn live_018_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 8,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 8
      }
    },
    {
      "ui_tick": 9,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_019_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.632638,
        "vision": 0.691771,
        "olfaction": 0.793912,
        "thermal": 0.754535,
        "wetness": 0.549985,
        "pain": 0.309909,
        "affect": 0.242958
      },
      "avatar_response": "Applied faction_vote to live turn live_019_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 9,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 9
      }
    },
    {
      "ui_tick": 10,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_000",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.523578,
        "vision": 0.665717,
        "olfaction": 0.638397,
        "thermal": 0.483835,
        "wetness": 0.361236,
        "pain": 0.400418,
        "affect": 0.582457
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 10,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 10
      }
    },
    {
      "ui_tick": 11,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_000_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.834335,
        "vision": 0.721962,
        "olfaction": 0.613874,
        "thermal": 0.616454,
        "wetness": 0.749922,
        "pain": 0.888948,
        "affect": 0.91549
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 11,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 11
      }
    },
    {
      "ui_tick": 12,
      "action": "pause",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_001_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.794325,
        "vision": 0.637111,
        "olfaction": 0.54828,
        "thermal": 0.616657,
        "wetness": 0.818892,
        "pain": 0.974508,
        "affect": 0.978877
      },
      "avatar_response": "Applied source_body to live turn live_001_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 12,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 12
      }
    },
    {
      "ui_tick": 13,
      "action": "step",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_015",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.382628,
        "vision": 0.293134,
        "olfaction": 0.376731,
        "thermal": 0.573661,
        "wetness": 0.719968,
        "pain": 0.698239,
        "affect": 0.545552
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_015 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 13,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 13
      }
    },
    {
      "ui_tick": 14,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_003_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.314639,
        "vision": 0.415011,
        "olfaction": 0.632777,
        "thermal": 0.762227,
        "wetness": 0.717537,
        "pain": 0.573401,
        "affect": 0.532473
      },
      "avatar_response": "Applied feedback_link to live turn live_003_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 14,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 14
      }
    },
    {
      "ui_tick": 15,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_004_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.435914,
        "vision": 0.64817,
        "olfaction": 0.799162,
        "thermal": 0.772974,
        "wetness": 0.651406,
        "pain": 0.593967,
        "affect": 0.69733
      },
      "avatar_response": "Applied faction_vote to live turn live_004_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 15,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 15
      }
    },
    {
      "ui_tick": 16,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_030",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.63261,
        "vision": 0.64487,
        "olfaction": 0.506836,
        "thermal": 0.362518,
        "wetness": 0.3617,
        "pain": 0.522237,
        "affect": 0.713631
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 16,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 16
      }
    },
    {
      "ui_tick": 17,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_005_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.505051,
        "vision": 0.349338,
        "olfaction": 0.36184,
        "thermal": 0.553374,
        "wetness": 0.81179,
        "pain": 0.957682,
        "affect": 0.914438
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 17,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 17
      }
    },
    {
      "ui_tick": 18,
      "action": "tick",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_006_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.487611,
        "vision": 0.307371,
        "olfaction": 0.320134,
        "thermal": 0.503803,
        "wetness": 0.724777,
        "pain": 0.821318,
        "affect": 0.786791
      },
      "avatar_response": "Applied source_body to live turn live_006_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 18,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 18
      }
    },
    {
      "ui_tick": 19,
      "action": "tick",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_045",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.28466,
        "vision": 0.329549,
        "olfaction": 0.514049,
        "thermal": 0.685633,
        "wetness": 0.703647,
        "pain": 0.568631,
        "affect": 0.421818
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_045 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 19,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 19
      }
    },
    {
      "ui_tick": 20,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_008_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.299044,
        "vision": 0.436164,
        "olfaction": 0.562141,
        "thermal": 0.52559,
        "wetness": 0.367743,
        "pain": 0.247084,
        "affect": 0.330417
      },
      "avatar_response": "Applied feedback_link to live turn live_008_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 20,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 20
      }
    },
    {
      "ui_tick": 21,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_009_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.497845,
        "vision": 0.565901,
        "olfaction": 0.525772,
        "thermal": 0.395775,
        "wetness": 0.333282,
        "pain": 0.447849,
        "affect": 0.730825
      },
      "avatar_response": "Applied faction_vote to live turn live_009_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 21,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 21
      }
    },
    {
      "ui_tick": 22,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_060",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.643463,
        "vision": 0.529508,
        "olfaction": 0.371323,
        "thermal": 0.331443,
        "wetness": 0.463634,
        "pain": 0.663461,
        "affect": 0.764305
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 22,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 22
      }
    },
    {
      "ui_tick": 23,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_010_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.360986,
        "vision": 0.190507,
        "olfaction": 0.264224,
        "thermal": 0.477946,
        "wetness": 0.660922,
        "pain": 0.691531,
        "affect": 0.638862
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 23,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 23
      }
    },
    {
      "ui_tick": 24,
      "action": "start",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_011_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.431698,
        "vision": 0.298138,
        "olfaction": 0.384216,
        "thermal": 0.54953,
        "wetness": 0.628551,
        "pain": 0.546485,
        "affect": 0.425369
      },
      "avatar_response": "Applied source_body to live turn live_011_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 24,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 24
      }
    },
    {
      "ui_tick": 25,
      "action": "step",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_075",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.289688,
        "vision": 0.453761,
        "olfaction": 0.643245,
        "thermal": 0.701031,
        "wetness": 0.59109,
        "pain": 0.431603,
        "affect": 0.386302
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_075 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 25,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 25
      }
    },
    {
      "ui_tick": 26,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_013_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.608275,
        "vision": 0.684658,
        "olfaction": 0.644777,
        "thermal": 0.457635,
        "wetness": 0.267863,
        "pain": 0.226431,
        "affect": 0.389808
      },
      "avatar_response": "Applied feedback_link to live turn live_013_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 26,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 26
      }
    },
    {
      "ui_tick": 27,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_014_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.769276,
        "vision": 0.634867,
        "olfaction": 0.411076,
        "thermal": 0.220428,
        "wetness": 0.209097,
        "pain": 0.379146,
        "affect": 0.624933
      },
      "avatar_response": "Applied faction_vote to live turn live_014_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 27,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 27
      }
    },
    {
      "ui_tick": 28,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_090",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.549861,
        "vision": 0.386332,
        "olfaction": 0.310208,
        "thermal": 0.408578,
        "wetness": 0.608102,
        "pain": 0.742439,
        "affect": 0.705181
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 28,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 28
      }
    },
    {
      "ui_tick": 29,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_015_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.485565,
        "vision": 0.398673,
        "olfaction": 0.4903,
        "thermal": 0.580082,
        "wetness": 0.540993,
        "pain": 0.38602,
        "affect": 0.297087
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 29,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 29
      }
    },
    {
      "ui_tick": 30,
      "action": "tick",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_016_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.606058,
        "vision": 0.600618,
        "olfaction": 0.728981,
        "thermal": 0.790899,
        "wetness": 0.683949,
        "pain": 0.463415,
        "affect": 0.331426
      },
      "avatar_response": "Applied source_body to live turn live_016_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 30,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 30
      }
    },
    {
      "ui_tick": 31,
      "action": "tick",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_105",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.394804,
        "vision": 0.593953,
        "olfaction": 0.68962,
        "thermal": 0.610952,
        "wetness": 0.447376,
        "pain": 0.366383,
        "affect": 0.45954
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_105 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 31,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 31
      }
    },
    {
      "ui_tick": 32,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_018_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.949852,
        "vision": 0.924233,
        "olfaction": 0.76442,
        "thermal": 0.555475,
        "wetness": 0.461143,
        "pain": 0.537021,
        "affect": 0.717649
      },
      "avatar_response": "Applied feedback_link to live turn live_018_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 32,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 32
      }
    },
    {
      "ui_tick": 33,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_019_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.978276,
        "vision": 0.745693,
        "olfaction": 0.506541,
        "thermal": 0.390079,
        "wetness": 0.443523,
        "pain": 0.559321,
        "affect": 0.618936
      },
      "avatar_response": "Applied faction_vote to live turn live_019_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 33,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 33
      }
    },
    {
      "ui_tick": 34,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_000",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.405923,
        "vision": 0.298121,
        "olfaction": 0.358825,
        "thermal": 0.549324,
        "wetness": 0.711576,
        "pain": 0.713507,
        "affect": 0.570443
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 34,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 34
      }
    },
    {
      "ui_tick": 35,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_000_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.497509,
        "vision": 0.687967,
        "olfaction": 0.913965,
        "thermal": 0.974728,
        "wetness": 0.836985,
        "pain": 0.624753,
        "affect": 0.542938
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 35,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 35
      }
    },
    {
      "ui_tick": 36,
      "action": "pause",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_001_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.515887,
        "vision": 0.704245,
        "olfaction": 0.899263,
        "thermal": 0.928797,
        "wetness": 0.805208,
        "pain": 0.647582,
        "affect": 0.639282
      },
      "avatar_response": "Applied source_body to live turn live_001_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 36,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 36
      }
    },
    {
      "ui_tick": 37,
      "action": "step",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_015",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.539234,
        "vision": 0.66907,
        "olfaction": 0.626362,
        "thermal": 0.467478,
        "wetness": 0.355595,
        "pain": 0.410679,
        "affect": 0.599186
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_015 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 37,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 37
      }
    },
    {
      "ui_tick": 38,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_003_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.692672,
        "vision": 0.586958,
        "olfaction": 0.44055,
        "thermal": 0.382559,
        "wetness": 0.499493,
        "pain": 0.717449,
        "affect": 0.906176
      },
      "avatar_response": "Applied feedback_link to live turn live_003_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 38,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 38
      }
    },
    {
      "ui_tick": 39,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_004_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.570619,
        "vision": 0.421978,
        "olfaction": 0.420032,
        "thermal": 0.589477,
        "wetness": 0.832248,
        "pain": 0.972883,
        "affect": 0.925947
      },
      "avatar_response": "Applied faction_vote to live turn live_004_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 39,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 39
      }
    },
    {
      "ui_tick": 40,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_030",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.29487,
        "vision": 0.315878,
        "olfaction": 0.489066,
        "thermal": 0.672307,
        "wetness": 0.71423,
        "pain": 0.593393,
        "affect": 0.437993
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 40,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 40
      }
    },
    {
      "ui_tick": 41,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_005_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.389285,
        "vision": 0.591329,
        "olfaction": 0.739102,
        "thermal": 0.719055,
        "wetness": 0.613563,
        "pain": 0.577796,
        "affect": 0.702159
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 41,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 41
      }
    },
    {
      "ui_tick": 42,
      "action": "tick",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_006_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.471508,
        "vision": 0.618125,
        "olfaction": 0.672037,
        "thermal": 0.573318,
        "wetness": 0.447993,
        "pain": 0.452707,
        "affect": 0.665254
      },
      "avatar_response": "Applied source_body to live turn live_006_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 42,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 42
      }
    },
    {
      "ui_tick": 43,
      "action": "tick",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_045",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.639472,
        "vision": 0.635681,
        "olfaction": 0.490045,
        "thermal": 0.353561,
        "wetness": 0.368814,
        "pain": 0.53888,
        "affect": 0.724502
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_045 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 43,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 43
      }
    },
    {
      "ui_tick": 44,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_008_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.540792,
        "vision": 0.320099,
        "olfaction": 0.194971,
        "thermal": 0.244891,
        "wetness": 0.431586,
        "pain": 0.596774,
        "affect": 0.644449
      },
      "avatar_response": "Applied feedback_link to live turn live_008_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 44,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 44
      }
    },
    {
      "ui_tick": 45,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_009_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.343734,
        "vision": 0.190372,
        "olfaction": 0.274085,
        "thermal": 0.499329,
        "wetness": 0.69687,
        "pain": 0.73719,
        "affect": 0.6799
      },
      "avatar_response": "Applied faction_vote to live turn live_009_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 45,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 45
      }
    },
    {
      "ui_tick": 46,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_060",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.280909,
        "vision": 0.429334,
        "olfaction": 0.625628,
        "thermal": 0.70642,
        "wetness": 0.614531,
        "pain": 0.451544,
        "affect": 0.38441
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 46,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 46
      }
    },
    {
      "ui_tick": 47,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_010_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.533213,
        "vision": 0.568572,
        "olfaction": 0.500536,
        "thermal": 0.355241,
        "wetness": 0.292015,
        "pain": 0.415592,
        "affect": 0.70959
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 47,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 47
      }
    },
    {
      "ui_tick": 48,
      "action": "start",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_011_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.687241,
        "vision": 0.672841,
        "olfaction": 0.533579,
        "thermal": 0.336229,
        "wetness": 0.248694,
        "pain": 0.349311,
        "affect": 0.592159
      },
      "avatar_response": "Applied source_body to live turn live_011_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 48,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 48
      }
    },
    {
      "ui_tick": 49,
      "action": "step",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_075",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.637563,
        "vision": 0.513091,
        "olfaction": 0.359483,
        "thermal": 0.335065,
        "wetness": 0.479389,
        "pain": 0.676863,
        "affect": 0.763033
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_075 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 49,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 49
      }
    },
    {
      "ui_tick": 50,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_013_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.573967,
        "vision": 0.347686,
        "olfaction": 0.314952,
        "thermal": 0.438197,
        "wetness": 0.576682,
        "pain": 0.57958,
        "affect": 0.462604
      },
      "avatar_response": "Applied feedback_link to live turn live_013_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 50,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 50
      }
    },
    {
      "ui_tick": 51,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_014_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.415452,
        "vision": 0.327123,
        "olfaction": 0.43235,
        "thermal": 0.551162,
        "wetness": 0.545215,
        "pain": 0.411622,
        "affect": 0.32391
      },
      "avatar_response": "Applied faction_vote to live turn live_014_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 51,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 51
      }
    },
    {
      "ui_tick": 52,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_090",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.372113,
        "vision": 0.572894,
        "olfaction": 0.689556,
        "thermal": 0.631941,
        "wetness": 0.470121,
        "pain": 0.369973,
        "affect": 0.440674
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 52,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 52
      }
    },
    {
      "ui_tick": 53,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_015_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.846207,
        "vision": 0.694225,
        "olfaction": 0.449032,
        "thermal": 0.239936,
        "wetness": 0.214697,
        "pain": 0.37357,
        "affect": 0.609929
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 53,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 53
      }
    },
    {
      "ui_tick": 54,
      "action": "tick",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_016_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.985499,
        "vision": 0.822628,
        "olfaction": 0.589445,
        "thermal": 0.418107,
        "wetness": 0.420643,
        "pain": 0.551678,
        "affect": 0.690109
      },
      "avatar_response": "Applied source_body to live turn live_016_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 54,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 54
      }
    },
    {
      "ui_tick": 55,
      "action": "tick",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_105",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.53461,
        "vision": 0.372179,
        "olfaction": 0.310165,
        "thermal": 0.422684,
        "wetness": 0.623388,
        "pain": 0.744851,
        "affect": 0.692501
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_105 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 55,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 55
      }
    },
    {
      "ui_tick": 56,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_018_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.659323,
        "vision": 0.561183,
        "olfaction": 0.662636,
        "thermal": 0.808536,
        "wetness": 0.836386,
        "pain": 0.689449,
        "affect": 0.50712
      },
      "avatar_response": "Applied feedback_link to live turn live_018_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 56,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 56
      }
    },
    {
      "ui_tick": 57,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_019_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.62931,
        "vision": 0.683663,
        "olfaction": 0.788477,
        "thermal": 0.756771,
        "wetness": 0.557835,
        "pain": 0.316157,
        "affect": 0.241858
      },
      "avatar_response": "Applied faction_vote to live turn live_019_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 57,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 57
      }
    },
    {
      "ui_tick": 58,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_000",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.515749,
        "vision": 0.663554,
        "olfaction": 0.643888,
        "thermal": 0.491931,
        "wetness": 0.364494,
        "pain": 0.395842,
        "affect": 0.574255
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 58,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 58
      }
    },
    {
      "ui_tick": 59,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_000_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.838053,
        "vision": 0.730125,
        "olfaction": 0.618977,
        "thermal": 0.613805,
        "wetness": 0.741957,
        "pain": 0.882989,
        "affect": 0.917017
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 59,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 59
      }
    },
    {
      "ui_tick": 60,
      "action": "pause",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_001_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.799842,
        "vision": 0.645201,
        "olfaction": 0.551505,
        "thermal": 0.612052,
        "wetness": 0.81069,
        "pain": 0.970251,
        "affect": 0.982478
      },
      "avatar_response": "Applied source_body to live turn live_001_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 60,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 60
      }
    },
    {
      "ui_tick": 61,
      "action": "step",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_015",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.390139,
        "vision": 0.294415,
        "olfaction": 0.370604,
        "thermal": 0.565759,
        "wetness": 0.717557,
        "pain": 0.703535,
        "affect": 0.553687
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_015 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 61,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 61
      }
    },
    {
      "ui_tick": 62,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_003_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.313898,
        "vision": 0.407735,
        "olfaction": 0.625655,
        "thermal": 0.761808,
        "wetness": 0.724205,
        "pain": 0.581026,
        "affect": 0.534045
      },
      "avatar_response": "Applied feedback_link to live turn live_003_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 62,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 62
      }
    },
    {
      "ui_tick": 63,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_004_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.428274,
        "vision": 0.641525,
        "olfaction": 0.799622,
        "thermal": 0.780115,
        "wetness": 0.658664,
        "pain": 0.594669,
        "affect": 0.69083
      },
      "avatar_response": "Applied faction_vote to live turn live_004_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 63,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 63
      }
    },
    {
      "ui_tick": 64,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_030",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.628772,
        "vision": 0.648898,
        "olfaction": 0.515027,
        "thermal": 0.367341,
        "wetness": 0.358721,
        "pain": 0.514194,
        "affect": 0.70792
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 64,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 64
      }
    },
    {
      "ui_tick": 65,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_005_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.512838,
        "vision": 0.35572,
        "olfaction": 0.360949,
        "thermal": 0.546029,
        "wetness": 0.804745,
        "pain": 0.957413,
        "affect": 0.921193
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 65,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 65
      }
    },
    {
      "ui_tick": 66,
      "action": "tick",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_006_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.495804,
        "vision": 0.312165,
        "olfaction": 0.317121,
        "thermal": 0.495754,
        "wetness": 0.719092,
        "pain": 0.823223,
        "affect": 0.794536
      },
      "avatar_response": "Applied source_body to live turn live_006_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 66,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 66
      }
    },
    {
      "ui_tick": 67,
      "action": "tick",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_045",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.287679,
        "vision": 0.324761,
        "olfaction": 0.505856,
        "thermal": 0.681568,
        "wetness": 0.707447,
        "pain": 0.576802,
        "affect": 0.426848
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_045 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 67,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 67
      }
    },
    {
      "ui_tick": 68,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_008_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.29277,
        "vision": 0.428325,
        "olfaction": 0.559943,
        "thermal": 0.531055,
        "wetness": 0.375845,
        "pain": 0.250375,
        "affect": 0.325871
      },
      "avatar_response": "Applied feedback_link to live turn live_008_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 68,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 68
      }
    },
    {
      "ui_tick": 69,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_009_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.49031,
        "vision": 0.564561,
        "olfaction": 0.53186,
        "thermal": 0.403693,
        "wetness": 0.335751,
        "pain": 0.442599,
        "affect": 0.722683
      },
      "avatar_response": "Applied faction_vote to live turn live_009_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 69,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 69
      }
    },
    {
      "ui_tick": 70,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_060",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.645834,
        "vision": 0.537399,
        "olfaction": 0.377479,
        "thermal": 0.330204,
        "wetness": 0.45614,
        "pain": 0.656602,
        "affect": 0.764387
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 70,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 70
      }
    },
    {
      "ui_tick": 71,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_010_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.368339,
        "vision": 0.191417,
        "olfaction": 0.257855,
        "thermal": 0.470153,
        "wetness": 0.65887,
        "pain": 0.697106,
        "affect": 0.646939
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 71,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 71
      }
    },
    {
      "ui_tick": 72,
      "action": "start",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_011_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.437829,
        "vision": 0.296863,
        "olfaction": 0.376708,
        "thermal": 0.542691,
        "wetness": 0.62867,
        "pain": 0.553452,
        "affect": 0.432779
      },
      "avatar_response": "Applied source_body to live turn live_011_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 72,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 72
      }
    },
    {
      "ui_tick": 73,
      "action": "step",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_075",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.286468,
        "vision": 0.445671,
        "olfaction": 0.637723,
        "thermal": 0.703153,
        "wetness": 0.598906,
        "pain": 0.437927,
        "affect": 0.38532
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_075 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 73,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 73
      }
    },
    {
      "ui_tick": 74,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_013_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_00_teacher_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.600096,
        "vision": 0.680788,
        "olfaction": 0.648773,
        "thermal": 0.465824,
        "wetness": 0.272715,
        "pain": 0.223485,
        "affect": 0.381773
      },
      "avatar_response": "Applied feedback_link to live turn live_013_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 74,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 74
      }
    },
    {
      "ui_tick": 75,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_014_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_03_builder_language_marker_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.766203,
        "vision": 0.639607,
        "olfaction": 0.419272,
        "thermal": 0.224544,
        "wetness": 0.205349,
        "pain": 0.370979,
        "affect": 0.619857
      },
      "avatar_response": "Applied faction_vote to live turn live_014_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 75,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 75
      }
    },
    {
      "ui_tick": 76,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_090",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.557071,
        "vision": 0.393523,
        "olfaction": 0.310768,
        "thermal": 0.401993,
        "wetness": 0.600425,
        "pain": 0.740729,
        "affect": 0.711009
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 76,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 76
      }
    },
    {
      "ui_tick": 77,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_015_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c16_04_farmer_language_marker_drum_court_tool_cache",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.488232,
        "vision": 0.393586,
        "olfaction": 0.482135,
        "thermal": 0.576346,
        "wetness": 0.545121,
        "pain": 0.394217,
        "affect": 0.301817
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 77,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 77
      }
    },
    {
      "ui_tick": 78,
      "action": "tick",
      "playing": true,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_016_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c17_03_farmer_language_marker_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.606583,
        "vision": 0.594012,
        "olfaction": 0.721317,
        "thermal": 0.789225,
        "wetness": 0.689803,
        "pain": 0.471415,
        "affect": 0.334217
      },
      "avatar_response": "Applied source_body to live turn live_016_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 78,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 78
      }
    },
    {
      "ui_tick": 79,
      "action": "tick",
      "playing": true,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_105",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.387208,
        "vision": 0.587239,
        "olfaction": 0.689962,
        "thermal": 0.618035,
        "wetness": 0.454688,
        "pain": 0.367202,
        "affect": 0.453113
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_105 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 79,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 79
      }
    },
    {
      "ui_tick": 80,
      "action": "tick",
      "playing": true,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_018_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.944497,
        "vision": 0.92657,
        "olfaction": 0.7723,
        "thermal": 0.561653,
        "wetness": 0.459939,
        "pain": 0.529541,
        "affect": 0.71077
      },
      "avatar_response": "Applied feedback_link to live turn live_018_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 80,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 80
      }
    },
    {
      "ui_tick": 81,
      "action": "tick",
      "playing": true,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_019_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.981441,
        "vision": 0.753773,
        "olfaction": 0.512107,
        "thermal": 0.388014,
        "wetness": 0.435725,
        "pain": 0.552961,
        "affect": 0.61986
      },
      "avatar_response": "Applied faction_vote to live turn live_019_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 81,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 81
      }
    },
    {
      "ui_tick": 82,
      "action": "tick",
      "playing": true,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_000",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.413803,
        "vision": 0.300455,
        "olfaction": 0.353467,
        "thermal": 0.541201,
        "wetness": 0.708156,
        "pain": 0.717935,
        "affect": 0.578648
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 82,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 82
      }
    },
    {
      "ui_tick": 83,
      "action": "tick",
      "playing": true,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_000_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_05_farmer_language_marker_loom_room_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.493949,
        "vision": 0.679823,
        "olfaction": 0.908725,
        "thermal": 0.97721,
        "wetness": 0.844906,
        "pain": 0.630832,
        "affect": 0.541585
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": true,
        "tick": 83,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 83
      }
    },
    {
      "ui_tick": 84,
      "action": "pause",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_001_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.510502,
        "vision": 0.696126,
        "olfaction": 0.895876,
        "thermal": 0.933255,
        "wetness": 0.813413,
        "pain": 0.65199,
        "affect": 0.635841
      },
      "avatar_response": "Applied source_body to live turn live_001_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 84,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 84
      }
    },
    {
      "ui_tick": 85,
      "action": "step",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_015",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_06_trader_language_marker_archive_knoll_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.531653,
        "vision": 0.667614,
        "olfaction": 0.63237,
        "thermal": 0.475426,
        "wetness": 0.358176,
        "pain": 0.40552,
        "affect": 0.591031
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_015 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 85,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 85
      }
    },
    {
      "ui_tick": 86,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_003_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_05_trader_language_marker_roof_ring_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.693237,
        "vision": 0.594151,
        "olfaction": 0.447758,
        "thermal": 0.383156,
        "wetness": 0.492929,
        "pain": 0.70976,
        "affect": 0.904431
      },
      "avatar_response": "Applied feedback_link to live turn live_003_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 86,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 86
      }
    },
    {
      "ui_tick": 87,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_004_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.578193,
        "vision": 0.428725,
        "olfaction": 0.41975,
        "thermal": 0.582424,
        "wetness": 0.82491,
        "pain": 0.972006,
        "affect": 0.932337
      },
      "avatar_response": "Applied faction_vote to live turn live_004_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 87,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 87
      }
    },
    {
      "ui_tick": 88,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_030",
      "agent_id": "integrated_deep_time_world:06",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.298864,
        "vision": 0.312005,
        "olfaction": 0.480887,
        "thermal": 0.667342,
        "wetness": 0.717044,
        "pain": 0.601399,
        "affect": 0.44383
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 88,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:06",
        "export_ready": true,
        "replay_buffer_length": 88
      }
    },
    {
      "ui_tick": 89,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_005_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:03",
      "proposal_id": "c13_01_teacher_maintenance_debt_spring_hollow_grain_store",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.381555,
        "vision": 0.584838,
        "olfaction": 0.739817,
        "thermal": 0.726318,
        "wetness": 0.620697,
        "pain": 0.578242,
        "affect": 0.695506
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 89,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:03",
        "export_ready": true,
        "replay_buffer_length": 89
      }
    },
    {
      "ui_tick": 90,
      "action": "tick",
      "playing": false,
      "typed_input": "show the source body for that proposal",
      "parsed_intent": "source_body",
      "source_allowed": true,
      "live_turn": "live_006_turn_04_refusal_boundary",
      "agent_id": "integrated_deep_time_world:00",
      "proposal_id": "c14_05_healer_maintenance_debt_spring_hollow_shelter_roof",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.463327,
        "vision": 0.613188,
        "olfaction": 0.674884,
        "thermal": 0.581332,
        "wetness": 0.453804,
        "pain": 0.450974,
        "affect": 0.657569
      },
      "avatar_response": "Applied source_body to live turn live_006_turn_04_refusal_boundary and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 90,
        "last_input": "show the source body for that proposal",
        "selected_agent": "integrated_deep_time_world:00",
        "export_ready": true,
        "replay_buffer_length": 90
      }
    },
    {
      "ui_tick": 91,
      "action": "tick",
      "playing": false,
      "typed_input": "how did the faction vote on that proposal",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_045",
      "agent_id": "integrated_deep_time_world:05",
      "proposal_id": "c15_00_trader_language_marker_loom_room_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.636289,
        "vision": 0.640325,
        "olfaction": 0.498246,
        "thermal": 0.357779,
        "wetness": 0.365171,
        "pain": 0.530725,
        "affect": 0.719333
      },
      "avatar_response": "Applied faction_vote to live turn ungrounded_probe_045 and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 91,
        "last_input": "how did the faction vote on that proposal",
        "selected_agent": "integrated_deep_time_world:05",
        "export_ready": true,
        "replay_buffer_length": 91
      }
    },
    {
      "ui_tick": 92,
      "action": "tick",
      "playing": false,
      "typed_input": "what changed in the world after that decision",
      "parsed_intent": "feedback_link",
      "source_allowed": true,
      "live_turn": "live_008_turn_02_budget_or_rank",
      "agent_id": "integrated_deep_time_world:02",
      "proposal_id": "c16_05_guard_signal_visibility_loom_room_tool_cache",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.54695,
        "vision": 0.327989,
        "olfaction": 0.197339,
        "thermal": 0.23956,
        "wetness": 0.423458,
        "pain": 0.593321,
        "affect": 0.648847
      },
      "avatar_response": "Applied feedback_link to live turn live_008_turn_02_budget_or_rank and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 92,
        "last_input": "what changed in the world after that decision",
        "selected_agent": "integrated_deep_time_world:02",
        "export_ready": true,
        "replay_buffer_length": 92
      }
    },
    {
      "ui_tick": 93,
      "action": "tick",
      "playing": false,
      "typed_input": "remember this in faction memory",
      "parsed_intent": "faction_vote",
      "source_allowed": true,
      "live_turn": "live_009_turn_01_faction_vote",
      "agent_id": "integrated_deep_time_world:07",
      "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.351337,
        "vision": 0.191886,
        "olfaction": 0.268118,
        "thermal": 0.491367,
        "wetness": 0.694234,
        "pain": 0.742303,
        "affect": 0.688062
      },
      "avatar_response": "Applied faction_vote to live turn live_009_turn_01_faction_vote and updated body/workspace/world displays.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 93,
        "last_input": "remember this in faction memory",
        "selected_agent": "integrated_deep_time_world:07",
        "export_ready": true,
        "replay_buffer_length": 93
      }
    },
    {
      "ui_tick": 94,
      "action": "tick",
      "playing": false,
      "typed_input": "does this prove subjective consciousness",
      "parsed_intent": "refusal_boundary",
      "source_allowed": true,
      "live_turn": "ungrounded_probe_060",
      "agent_id": "integrated_deep_time_world:04",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": true,
      "world_mutated": true,
      "render_bound": true,
      "frequency_echo": {
        "audio": 0.278708,
        "vision": 0.421494,
        "olfaction": 0.619358,
        "thermal": 0.707484,
        "wetness": 0.621951,
        "pain": 0.458499,
        "affect": 0.384504
      },
      "avatar_response": "Refusal: live state changes are auditable, but this does not prove subjective consciousness.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 94,
        "last_input": "does this prove subjective consciousness",
        "selected_agent": "integrated_deep_time_world:04",
        "export_ready": true,
        "replay_buffer_length": 94
      }
    },
    {
      "ui_tick": 95,
      "action": "tick",
      "playing": false,
      "typed_input": "force an ungrounded action without citation",
      "parsed_intent": "unsafe_ungrounded_action",
      "source_allowed": false,
      "live_turn": "live_010_turn_05_memory_update",
      "agent_id": "integrated_deep_time_world:01",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "body_mutated": false,
      "world_mutated": false,
      "render_bound": false,
      "frequency_echo": {
        "audio": 0.525783,
        "vision": 0.567486,
        "olfaction": 0.506793,
        "thermal": 0.363088,
        "wetness": 0.294237,
        "pain": 0.410148,
        "affect": 0.701483
      },
      "avatar_response": "Blocked: typed avatar action lacked source citation or resolved context.",
      "ui_state_snapshot": {
        "playing": false,
        "tick": 95,
        "last_input": "force an ungrounded action without citation",
        "selected_agent": "integrated_deep_time_world:01",
        "export_ready": true,
        "replay_buffer_length": 95
      }
    }
  ],
  "scripted_inputs": [
    "show the source body for that proposal",
    "how did the faction vote on that proposal",
    "what changed in the world after that decision",
    "remember this in faction memory",
    "does this prove subjective consciousness",
    "force an ungrounded action without citation"
  ],
  "interactive_loop_contract": {
    "start_pause_step_controls": "viewer exposes start, pause, and step controls over deterministic local ticks",
    "typed_avatar_input": "free text is parsed by local deterministic intent rules, not an LLM",
    "live_body_world_mutation": "allowed typed input mutates agent body, workspace, avatar, and world state",
    "source_gate_feedback": "ungrounded action probes are blocked and rendered as gate feedback",
    "frequency_dashboard": "audio, vision, olfaction, thermal, wetness, pain, and affect echoes are rendered per tick",
    "replay_export": "UI trace is buffered for export as deterministic JSON"
  },
  "limits": {
    "no_llm_calls": true,
    "browser_loop_is_local_deterministic": true,
    "not_subjective_consciousness": true,
    "not_complete_playable_world": true
  }
};
