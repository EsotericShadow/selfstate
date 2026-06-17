window.SSRM_3D_DEEP_TIME_SETTLEMENT_GRAPH_TRACE = [
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 0,
    "event_id": 0,
    "lineage": {
      "era": 0,
      "parent_hash": "settlement-root",
      "settlement_hash": "5517320a6519ae92",
      "year_end": 200,
      "year_start": 0
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "root_rest",
        "frequency_hz": 0.236115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "5a25add97b759eae",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.242286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "28878faef8550bdc",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "work_petal",
        "frequency_hz": 0.26138,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "fce84dc7135442f2",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "social_petal",
        "frequency_hz": 0.261662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "8439e3317f56fa93",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "explore_petal",
        "frequency_hz": 0.2658,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "713bd17f6631da76",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "return_petal",
        "frequency_hz": 0.268425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "fe73681a99366ebc",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "root_rest",
        "frequency_hz": 0.257336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "fadd2dfafdf33891",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.263501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "15597eb7a3663622",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 200,
    "year_start": 0
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 1,
    "event_id": 1,
    "lineage": {
      "era": 1,
      "parent_hash": "5517320a6519ae92",
      "settlement_hash": "c7e306a0d36f1c1b",
      "year_end": 400,
      "year_start": 200
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.240115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "94cadb66133d48e9",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "work_petal",
        "frequency_hz": 0.246286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "4ec0bef4e9fc3fd9",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "social_petal",
        "frequency_hz": 0.26538,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "117a1168b28be0da",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "explore_petal",
        "frequency_hz": 0.265662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "7c7db100b4fd9590",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "return_petal",
        "frequency_hz": 0.2698,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "6f6b3d30be266821",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "root_rest",
        "frequency_hz": 0.248425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "d8792e0bf9c2ab58",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.261336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "e30e2abb669180df",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "work_petal",
        "frequency_hz": 0.267501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "cb01b235bf7b2460",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 400,
    "year_start": 200
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 2,
    "event_id": 2,
    "lineage": {
      "era": 2,
      "parent_hash": "c7e306a0d36f1c1b",
      "settlement_hash": "87c50c4d1f9d685a",
      "year_end": 600,
      "year_start": 400
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "work_petal",
        "frequency_hz": 0.244115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "374147c5780d4654",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "social_petal",
        "frequency_hz": 0.250286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "c35ad3fdcd839d91",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "explore_petal",
        "frequency_hz": 0.26938,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "5cd19cba3d5798b6",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "return_petal",
        "frequency_hz": 0.269662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "f619b18bf1e9e406",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "root_rest",
        "frequency_hz": 0.2498,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "75824e0e95af22d8",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.252425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "c3acaa04b9222f10",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "work_petal",
        "frequency_hz": 0.265336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "3da7347e32b33f46",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "social_petal",
        "frequency_hz": 0.271501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "e0e9dde883ad01cc",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 600,
    "year_start": 400
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 3,
    "event_id": 3,
    "lineage": {
      "era": 3,
      "parent_hash": "87c50c4d1f9d685a",
      "settlement_hash": "01ed7dbbf066d245",
      "year_end": 800,
      "year_start": 600
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "social_petal",
        "frequency_hz": 0.248115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "6a2b3d8254c60580",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "explore_petal",
        "frequency_hz": 0.254286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "949776e4f670dce1",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "return_petal",
        "frequency_hz": 0.27338,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "0839482552505186",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "root_rest",
        "frequency_hz": 0.249662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "74abfba13486e7e7",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.2538,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "fd1aff244bb347ff",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "work_petal",
        "frequency_hz": 0.256425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "5a48a75e7b0f49b2",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "social_petal",
        "frequency_hz": 0.269336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "f882265e0d1a83c7",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "explore_petal",
        "frequency_hz": 0.275501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "ca47d3d7a204ff00",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 800,
    "year_start": 600
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 4,
    "event_id": 4,
    "lineage": {
      "era": 4,
      "parent_hash": "01ed7dbbf066d245",
      "settlement_hash": "906ed7c644ad5131",
      "year_end": 1000,
      "year_start": 800
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "explore_petal",
        "frequency_hz": 0.252115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "53795141a6a99860",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "return_petal",
        "frequency_hz": 0.258286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "7919d3494a812e7b",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "root_rest",
        "frequency_hz": 0.25338,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "935c53259aecd7ab",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.253662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "583f4ce107fe168f",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "work_petal",
        "frequency_hz": 0.2578,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "9254a2f170c1a9a8",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "social_petal",
        "frequency_hz": 0.260425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "b538a19235a24a90",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "explore_petal",
        "frequency_hz": 0.273336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "6f5235ce72787207",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "return_petal",
        "frequency_hz": 0.279501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "91d2ce524195cfcf",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 1000,
    "year_start": 800
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 5,
    "event_id": 5,
    "lineage": {
      "era": 5,
      "parent_hash": "906ed7c644ad5131",
      "settlement_hash": "897d9072a647ede3",
      "year_end": 1200,
      "year_start": 1000
    },
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
    "private_workspace_hidden": true,
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
        "route_hash": "51e2bda92fee4b9c",
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
        "route_hash": "37787abaeb8c0ea8",
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
        "route_hash": "c32f6c84cf36e33e",
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
        "route_hash": "e4867f3a1fe3c814",
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
        "route_hash": "95d098466acc03c1",
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
        "route_hash": "80ce663740c9b865",
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
        "route_hash": "b69dcd52d9c5d141",
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
        "route_hash": "edde2745b56958bb",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 1200,
    "year_start": 1000
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 6,
    "event_id": 6,
    "lineage": {
      "era": 6,
      "parent_hash": "897d9072a647ede3",
      "settlement_hash": "241173d2355fc0ba",
      "year_end": 1400,
      "year_start": 1200
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "root_rest",
        "frequency_hz": 0.236115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "16cf29cb324eea60",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.242286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "ad1a81f5d7ab0b73",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "work_petal",
        "frequency_hz": 0.26138,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "8218223ba7d69770",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "social_petal",
        "frequency_hz": 0.261662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "edd4162e588e1c01",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "explore_petal",
        "frequency_hz": 0.2658,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "164007023f9fa9b2",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "return_petal",
        "frequency_hz": 0.268425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "3fa5df9e6b80ea5d",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "root_rest",
        "frequency_hz": 0.257336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "a2a0700a8899e185",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.263501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "015d88b11e9d60c9",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 1400,
    "year_start": 1200
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 7,
    "event_id": 7,
    "lineage": {
      "era": 7,
      "parent_hash": "241173d2355fc0ba",
      "settlement_hash": "bef4e15edcadaeac",
      "year_end": 1600,
      "year_start": 1400
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.240115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "215d8b4e650ce3ea",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "work_petal",
        "frequency_hz": 0.246286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "a4cb4c780ab504bc",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "social_petal",
        "frequency_hz": 0.26538,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "c2603bcabd56f12c",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "explore_petal",
        "frequency_hz": 0.265662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "396da22f3bc9bd12",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "return_petal",
        "frequency_hz": 0.2698,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "27f659c7cf0671a6",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "root_rest",
        "frequency_hz": 0.248425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "1ea3441a5d10134d",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.261336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "ec77ab093911c5a7",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "work_petal",
        "frequency_hz": 0.267501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "a6b43b14dfe0d15e",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 1600,
    "year_start": 1400
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 8,
    "event_id": 8,
    "lineage": {
      "era": 8,
      "parent_hash": "bef4e15edcadaeac",
      "settlement_hash": "d0187daf769cd0be",
      "year_end": 1800,
      "year_start": 1600
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "work_petal",
        "frequency_hz": 0.244115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "2767511ac2baecc7",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "social_petal",
        "frequency_hz": 0.250286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "df68d98cf0e6774d",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "explore_petal",
        "frequency_hz": 0.26938,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "7a8838273a440022",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "return_petal",
        "frequency_hz": 0.269662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "5becf341dfd73216",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "root_rest",
        "frequency_hz": 0.2498,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "5098ff3c802a47dd",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.252425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "e38b77d6782d0ebb",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "work_petal",
        "frequency_hz": 0.265336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "38ccd0c868741f6d",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "social_petal",
        "frequency_hz": 0.271501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "a7cd96aaad1603f6",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 1800,
    "year_start": 1600
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 9,
    "event_id": 9,
    "lineage": {
      "era": 9,
      "parent_hash": "d0187daf769cd0be",
      "settlement_hash": "a57b7c389d103640",
      "year_end": 2000,
      "year_start": 1800
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "social_petal",
        "frequency_hz": 0.248115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "eeb366161b1d305f",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "explore_petal",
        "frequency_hz": 0.254286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "34ddb2086659f339",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "return_petal",
        "frequency_hz": 0.27338,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "683322b85465954b",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "root_rest",
        "frequency_hz": 0.249662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "9e9192a6773a7c73",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.2538,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "fe3642bb5c9ab893",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "work_petal",
        "frequency_hz": 0.256425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "99309fc89c3c7ad6",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "social_petal",
        "frequency_hz": 0.269336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "082a449e1dee6744",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "explore_petal",
        "frequency_hz": 0.275501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "de53069e841a0b1b",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 2000,
    "year_start": 1800
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 10,
    "event_id": 10,
    "lineage": {
      "era": 10,
      "parent_hash": "a57b7c389d103640",
      "settlement_hash": "caec0c61979f2de5",
      "year_end": 2200,
      "year_start": 2000
    },
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
    "private_workspace_hidden": true,
    "routes": [
      {
        "avatar_traversable": true,
        "distance": 0.32311,
        "flower_node": "explore_petal",
        "frequency_hz": 0.252115,
        "from": "hearth_vale",
        "hazard": 0.201261,
        "kind": "shelter_path",
        "route_cost": 0.600138,
        "route_hash": "1ba2f1666468c8ff",
        "to": "moss_hollow"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "return_petal",
        "frequency_hz": 0.258286,
        "from": "hearth_vale",
        "hazard": 0.198327,
        "kind": "work_path",
        "route_cost": 0.624197,
        "route_hash": "cfd839f3e0c1c152",
        "to": "clay_basin"
      },
      {
        "avatar_traversable": false,
        "distance": 0.644981,
        "flower_node": "root_rest",
        "frequency_hz": 0.25338,
        "from": "hearth_vale",
        "hazard": 0.205461,
        "kind": "watch_path",
        "route_cost": 0.769427,
        "route_hash": "2a0f4fabce41c949",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.297321,
        "flower_node": "dawn_breath",
        "frequency_hz": 0.253662,
        "from": "moss_hollow",
        "hazard": 0.2784,
        "kind": "soft_moss_path",
        "route_cost": 0.673899,
        "route_hash": "7d5404413ee6ffe0",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.286356,
        "flower_node": "work_petal",
        "frequency_hz": 0.2578,
        "from": "clay_basin",
        "hazard": 0.275466,
        "kind": "water_clay_path",
        "route_cost": 0.677626,
        "route_hash": "b547e07588642810",
        "to": "reed_wetland"
      },
      {
        "avatar_traversable": true,
        "distance": 0.360555,
        "flower_node": "social_petal",
        "frequency_hz": 0.260425,
        "from": "clay_basin",
        "hazard": 0.238239,
        "kind": "ridge_work_path",
        "route_cost": 0.693658,
        "route_hash": "208af10fafe8ddb2",
        "to": "stone_ridge"
      },
      {
        "avatar_traversable": true,
        "distance": 0.223607,
        "flower_node": "explore_petal",
        "frequency_hz": 0.273336,
        "from": "reed_wetland",
        "hazard": 0.328843,
        "kind": "wetland_glass_path",
        "route_cost": 0.710285,
        "route_hash": "79caca23b1006aea",
        "to": "glass_mire"
      },
      {
        "avatar_traversable": false,
        "distance": 0.382099,
        "flower_node": "return_petal",
        "frequency_hz": 0.279501,
        "from": "glass_mire",
        "hazard": 0.291616,
        "kind": "edge_watch_path",
        "route_cost": 0.76172,
        "route_hash": "d47e74eee3b9ed12",
        "to": "stone_ridge"
      }
    ],
    "safe_refuge_paths": true,
    "year_end": 2200,
    "year_start": 2000
  },
  {
    "avatar_traversal_packet": {
      "entry_place": "hearth_vale",
      "reachable_places": [
        "clay_basin",
        "glass_mire",
        "hearth_vale",
        "moss_hollow",
        "reed_wetland",
        "stone_ridge"
      ],
      "requires_embodied_costs": true,
      "route_count": 6
    },
    "claim_boundary": {
      "complete_3d_world": false,
      "complete_playable_world": false,
      "moral_patienthood": false,
      "subjective_consciousness": false
    },
    "condition": "integrated_deep_time_settlement_architecture_place_graph",
    "connected": true,
    "era": 11,
    "event_id": 11,
    "lineage": {
      "era": 11,
      "parent_hash": "caec0c61979f2de5",
      "settlement_hash": "5aaa2bacd34a14ba",
      "year_end": 2400,
      "year_start": 2200
    },
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
    "private_workspace_hidden": true,
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
    "safe_refuge_paths": true,
    "year_end": 2400,
    "year_start": 2200
  }
];
