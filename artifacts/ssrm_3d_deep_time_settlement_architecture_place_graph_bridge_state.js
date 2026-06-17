window.SSRM_3D_DEEP_TIME_SETTLEMENT_GRAPH_STATE = {
  "condition": "integrated_deep_time_settlement_architecture_place_graph",
  "config": {
    "eras": 12,
    "generations_per_era": 200,
    "seed": 20260723,
    "source_state": "artifacts/ssrm_3d_deep_time_habitat_climate_multisensory_bridge_state.json"
  },
  "moral_boundary": {
    "avatar_topology_seed_not_complete_gameplay": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "settlement_graph_seed_not_complete_3d_world": true
  },
  "settlement_state": {
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "lineage": [
      {
        "era": 0,
        "parent_hash": "settlement-root",
        "settlement_hash": "5517320a6519ae92",
        "year_end": 200,
        "year_start": 0
      },
      {
        "era": 1,
        "parent_hash": "5517320a6519ae92",
        "settlement_hash": "c7e306a0d36f1c1b",
        "year_end": 400,
        "year_start": 200
      },
      {
        "era": 2,
        "parent_hash": "c7e306a0d36f1c1b",
        "settlement_hash": "87c50c4d1f9d685a",
        "year_end": 600,
        "year_start": 400
      },
      {
        "era": 3,
        "parent_hash": "87c50c4d1f9d685a",
        "settlement_hash": "01ed7dbbf066d245",
        "year_end": 800,
        "year_start": 600
      },
      {
        "era": 4,
        "parent_hash": "01ed7dbbf066d245",
        "settlement_hash": "906ed7c644ad5131",
        "year_end": 1000,
        "year_start": 800
      },
      {
        "era": 5,
        "parent_hash": "906ed7c644ad5131",
        "settlement_hash": "897d9072a647ede3",
        "year_end": 1200,
        "year_start": 1000
      },
      {
        "era": 6,
        "parent_hash": "897d9072a647ede3",
        "settlement_hash": "241173d2355fc0ba",
        "year_end": 1400,
        "year_start": 1200
      },
      {
        "era": 7,
        "parent_hash": "241173d2355fc0ba",
        "settlement_hash": "bef4e15edcadaeac",
        "year_end": 1600,
        "year_start": 1400
      },
      {
        "era": 8,
        "parent_hash": "bef4e15edcadaeac",
        "settlement_hash": "d0187daf769cd0be",
        "year_end": 1800,
        "year_start": 1600
      },
      {
        "era": 9,
        "parent_hash": "d0187daf769cd0be",
        "settlement_hash": "a57b7c389d103640",
        "year_end": 2000,
        "year_start": 1800
      },
      {
        "era": 10,
        "parent_hash": "a57b7c389d103640",
        "settlement_hash": "caec0c61979f2de5",
        "year_end": 2200,
        "year_start": 2000
      },
      {
        "era": 11,
        "parent_hash": "caec0c61979f2de5",
        "settlement_hash": "5aaa2bacd34a14ba",
        "year_end": 2400,
        "year_start": 2200
      }
    ],
    "places": {
      "clay_basin": {
        "biome": "clay_heat_basin",
        "coord": [
          0.52,
          0.48
        ],
        "functions": [
          "work",
          "storage",
          "repair"
        ],
        "group": "work_band",
        "hazard_level": 0.231104,
        "place": "clay_basin",
        "safety_refuge": true,
        "storage_capacity": 0.615291,
        "work_capacity": 0.47282
      },
      "glass_mire": {
        "biome": "glass_reed_mire",
        "coord": [
          0.78,
          0.66
        ],
        "functions": [
          "hazard",
          "observe",
          "work"
        ],
        "group": "edge_watch",
        "hazard_level": 0.337858,
        "place": "glass_mire",
        "safety_refuge": false,
        "storage_capacity": 0.0,
        "work_capacity": 0.429705
      },
      "hearth_vale": {
        "biome": "warm_shelter_vale",
        "coord": [
          0.18,
          0.36
        ],
        "functions": [
          "shelter",
          "social",
          "storage"
        ],
        "group": "hearth_circle",
        "hazard_level": 0.165549,
        "place": "hearth_vale",
        "safety_refuge": true,
        "storage_capacity": 0.633646,
        "work_capacity": 0.0
      },
      "moss_hollow": {
        "biome": "soft_moss_hollow",
        "coord": [
          0.3,
          0.66
        ],
        "functions": [
          "shelter",
          "food_cache",
          "rest"
        ],
        "group": "hearth_circle",
        "hazard_level": 0.236973,
        "place": "moss_hollow",
        "safety_refuge": true,
        "storage_capacity": 0.613648,
        "work_capacity": 0.0
      },
      "reed_wetland": {
        "biome": "water_reed_marsh",
        "coord": [
          0.58,
          0.76
        ],
        "functions": [
          "water",
          "fiber_work",
          "hazard"
        ],
        "group": "work_band",
        "hazard_level": 0.319828,
        "place": "reed_wetland",
        "safety_refuge": true,
        "storage_capacity": 0.0,
        "work_capacity": 0.445809
      },
      "stone_ridge": {
        "biome": "wind_stone_ridge",
        "coord": [
          0.82,
          0.28
        ],
        "functions": [
          "watch",
          "hazard",
          "signal"
        ],
        "group": "edge_watch",
        "hazard_level": 0.245373,
        "place": "stone_ridge",
        "safety_refuge": false,
        "storage_capacity": 0.0,
        "work_capacity": 0.0
      }
    },
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "return_petal",
        "frequency_hz": 0.256115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "8461c58b00f85c14",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "root_rest",
        "frequency_hz": 0.238286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "b96570a5f8f2c276",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.25738,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "4e84b5e47f370852",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "work_petal",
        "frequency_hz": 0.257662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "7b9e14e3e452a59a",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "social_petal",
        "frequency_hz": 0.2618,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "afafa45735bc7c2f",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "explore_petal",
        "frequency_hz": 0.264425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "13ad5c02ec2a90f6",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "return_petal",
        "frequency_hz": 0.277336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "8bcf52a67befbb27",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "root_rest",
        "frequency_hz": 0.259501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "b45ff0955a2776d3",
        "to": "stone_ridge"
      }
    ],
    "simulated_years": 2400,
    "source_habitat_boundary": {
      "body_exposure_requires_safety_refuge": true,
      "no_moral_patienthood_claim": true,
      "no_subjective_consciousness_claim": true,
      "private_workspace_not_debug_leaked": true,
      "world_metabolism_seed_not_complete_3d_world": true
    }
  },
  "trace_events": 12
};
