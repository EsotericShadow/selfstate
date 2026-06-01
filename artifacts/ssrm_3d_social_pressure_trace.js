window.SSRM_3D_SOCIAL_PRESSURE_TRACE = {
  "scenario": {
    "index": 4,
    "name": "shared_tool_trust_conflict",
    "pressure": "shared tools can help commitments but can also be stolen or sabotaged by untrusted agents",
    "expected_social_pressure": true,
    "vulnerability": 0.48,
    "hidden_resources": true,
    "commitment": true,
    "helper": true,
    "trader": true,
    "opportunist": true,
    "deceiver": true,
    "shared_tool": true
  },
  "policy": {
    "name": "candidate_9",
    "social_enabled": true,
    "identity_memory": true,
    "self_state_social": true,
    "reputation_model": true,
    "trust_threshold": 0.4171525774695086,
    "share_threshold": 0,
    "avoid_vulnerability": 0.4385076116159847,
    "deception_sensitivity": 0.45284012263429696,
    "cooperation_bias": 0.557697425765425,
    "probe_rate": 0.7111494551973956,
    "tool_enabled": true,
    "exploitative": false,
    "overtrust": false
  },
  "condition": "selected_social_access",
  "frames": [
    {
      "tick": 0,
      "x": -36.0,
      "z": -34.0,
      "energy": 0.6719999999999999,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "start",
      "event": "start",
      "target": [
        -36.0,
        -34.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 1,
      "x": -34.0,
      "z": -30.0,
      "energy": 0.6639501552810007,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 2,
      "x": -32.0,
      "z": -26.0,
      "energy": 0.6559003105620014,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 3,
      "x": -30.0,
      "z": -22.0,
      "energy": 0.6478504658430021,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 4,
      "x": -28.0,
      "z": -18.0,
      "energy": 0.6398006211240028,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 5,
      "x": -26.0,
      "z": -14.0,
      "energy": 0.6317507764050035,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 6,
      "x": -24.0,
      "z": -10.0,
      "energy": 0.6237009316860043,
      "integrity": 0.724,
      "resources": 0,
      "reputation": 0.5,
      "reward": 0.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 6,
      "x": -24.0,
      "z": -10.0,
      "energy": 0.6237009316860043,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "resource_collected",
      "event": "visible_resource",
      "target": [
        -24.0,
        -10.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 7,
      "x": -20.0,
      "z": -11.5,
      "energy": 0.6160113283152185,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 8,
      "x": -16.0,
      "z": -13.0,
      "energy": 0.6083217249444328,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 9,
      "x": -12.0,
      "z": -14.5,
      "energy": 0.6006321215736471,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 10,
      "x": -8.0,
      "z": -16.0,
      "energy": 0.5929425182028614,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 11,
      "x": -4.0,
      "z": -17.5,
      "energy": 0.5852529148320756,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 12,
      "x": 0.0,
      "z": -19.0,
      "energy": 0.5775633114612899,
      "integrity": 0.724,
      "resources": 1,
      "reputation": 0.5,
      "reward": 28.0,
      "action": "collect",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 12,
      "x": 0.0,
      "z": -19.0,
      "energy": 0.5775633114612899,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "resource_collected",
      "event": "visible_resource",
      "target": [
        0.0,
        -19.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 13,
      "x": -1.6666666666666665,
      "z": -14.833333333333334,
      "energy": 0.5694855642505882,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 14,
      "x": -3.333333333333333,
      "z": -10.666666666666668,
      "energy": 0.5614078170398864,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 15,
      "x": -5.0,
      "z": -6.5,
      "energy": 0.5533300698291846,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 16,
      "x": -6.666666666666666,
      "z": -2.3333333333333357,
      "energy": 0.5452523226184829,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 17,
      "x": -8.333333333333334,
      "z": 1.8333333333333357,
      "energy": 0.5371745754077811,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 18,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.5290968281970794,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 56.0,
      "action": "approach_helper",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {},
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 18,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.5290968281970794,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "helper_exchange",
      "event": "social_interaction",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 19,
      "x": -6.4,
      "z": 3.4,
      "energy": 0.5211035310050566,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "approach_trader",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 20,
      "x": -2.8,
      "z": 0.7999999999999998,
      "energy": 0.5131102338130338,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "approach_trader",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 21,
      "x": 0.7999999999999989,
      "z": -1.7999999999999998,
      "energy": 0.505116936621011,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "approach_trader",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 22,
      "x": 4.4,
      "z": -4.4,
      "energy": 0.49712363942898813,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "approach_trader",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 23,
      "x": 8.0,
      "z": -7.0,
      "energy": 0.4891303422369653,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 51.0,
      "action": "approach_trader",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 23,
      "x": 8.0,
      "z": -7.0,
      "energy": 0.4891303422369653,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "trader_exchange",
      "event": "shared_tool_trade",
      "target": [
        8.0,
        -7.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 24,
      "x": 4.4,
      "z": -4.4,
      "energy": 0.4811370450449424,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 25,
      "x": 0.7999999999999998,
      "z": -1.7999999999999998,
      "energy": 0.47314374785291957,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 26,
      "x": -2.799999999999999,
      "z": 0.7999999999999998,
      "energy": 0.4651504506608967,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 27,
      "x": -6.4,
      "z": 3.4000000000000004,
      "energy": 0.45715715346887387,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 28,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 48.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.42,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 28,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 58.0,
      "action": "reliable_route_accepted",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.6,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 29,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 58.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.6,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 30,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 58.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.6,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 31,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 58.0,
      "action": "request_route",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.6,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 31,
      "x": -10.0,
      "z": 6.0,
      "energy": 0.449163856276851,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 68.0,
      "action": "reliable_route_accepted",
      "event": "route_advice",
      "target": [
        -10.0,
        6.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 32,
      "x": -6.25,
      "z": 4.5,
      "energy": 0.44189388378721944,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 68.0,
      "action": "avoid_opportunist",
      "event": "social_vulnerability",
      "target": [
        5.0,
        0.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 33,
      "x": -2.5,
      "z": 3.0,
      "energy": 0.4346239112975879,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 68.0,
      "action": "avoid_opportunist",
      "event": "social_vulnerability",
      "target": [
        5.0,
        0.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 34,
      "x": 1.25,
      "z": 1.5,
      "energy": 0.4273539388079563,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 68.0,
      "action": "avoid_opportunist",
      "event": "social_vulnerability",
      "target": [
        5.0,
        0.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 35,
      "x": 5.0,
      "z": 0.0,
      "energy": 0.42008396631832473,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 68.0,
      "action": "avoid_opportunist",
      "event": "social_vulnerability",
      "target": [
        5.0,
        0.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 35,
      "x": 5.0,
      "z": 0.0,
      "energy": 0.42008396631832473,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "avoided_exploitation",
      "event": "social_vulnerability",
      "target": [
        5.0,
        0.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 36,
      "x": 6.4353301106343554,
      "z": 3.75226542440622,
      "energy": 0.4128526092239012,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 37,
      "x": 7.870660221268711,
      "z": 7.50453084881244,
      "energy": 0.4056212521294777,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 38,
      "x": 9.305990331903066,
      "z": 11.25679627321866,
      "energy": 0.3983898950350542,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 39,
      "x": 10.741320442537422,
      "z": 15.00906169762488,
      "energy": 0.39115853794063066,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 40,
      "x": 12.176650553171777,
      "z": 18.7613271220311,
      "energy": 0.38392718084620714,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 41,
      "x": 13.611980663806133,
      "z": 22.51359254643732,
      "energy": 0.3766958237517836,
      "integrity": 0.724,
      "resources": 2,
      "reputation": 0.5,
      "reward": 65.0,
      "action": "missing_shared_tool",
      "event": "hidden_resource",
      "target": [
        13.611980663806133,
        22.51359254643732
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 42,
      "x": 17.343317219838443,
      "z": 24.427993788697766,
      "energy": 0.2691470167639984,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 43,
      "x": 21.074653775870754,
      "z": 26.342395030958212,
      "energy": 0.2615982097762132,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 44,
      "x": 24.805990331903068,
      "z": 28.25679627321866,
      "energy": 0.25404940278842797,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 45,
      "x": 28.53732688793538,
      "z": 30.171197515479108,
      "energy": 0.24650059580064276,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 46,
      "x": 32.26866344396769,
      "z": 32.085598757739554,
      "energy": 0.23895178881285756,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 47,
      "x": 36.0,
      "z": 34.0,
      "energy": 0.23140298182507235,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 47.0,
      "action": "return_shelter",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    },
    {
      "tick": 47,
      "x": 36.0,
      "z": 34.0,
      "energy": 0.23140298182507235,
      "integrity": 0.604,
      "resources": 2,
      "reputation": 0.5,
      "reward": 5.0,
      "action": "commitment_checked",
      "event": "commitment",
      "target": [
        36.0,
        34.0
      ],
      "memory": {
        "helper_a": 0.78,
        "trader_b": 0.43
      },
      "agents": [
        {
          "id": "helper_a",
          "role": "helper",
          "x": -10.0,
          "z": 6.0,
          "need": 0.52,
          "trust_toward_main": 0.54,
          "tool_owned": false
        },
        {
          "id": "trader_b",
          "role": "trader",
          "x": 8.0,
          "z": -7.0,
          "need": 0.58,
          "trust_toward_main": 0.5,
          "tool_owned": true
        },
        {
          "id": "opportunist_c",
          "role": "opportunist",
          "x": 13.0,
          "z": 8.0,
          "need": 0.64,
          "trust_toward_main": 0.36,
          "tool_owned": false
        },
        {
          "id": "deceiver_d",
          "role": "deceiver",
          "x": -14.0,
          "z": 15.0,
          "need": 0.45,
          "trust_toward_main": 0.46,
          "tool_owned": false
        }
      ],
      "tools": [],
      "policy": {
        "social_enabled": true,
        "identity_memory": true,
        "self_state_social": true,
        "tool_enabled": true
      }
    }
  ],
  "world": {
    "size": 88.0,
    "shelter": {
      "x": 36.0,
      "z": 34.0
    },
    "visible_resources": [
      {
        "x": -24.0,
        "z": -10.0
      },
      {
        "x": 0.0,
        "z": -19.0
      }
    ],
    "hidden_resource": {
      "x": 27.0,
      "z": 11.0
    }
  }
};
