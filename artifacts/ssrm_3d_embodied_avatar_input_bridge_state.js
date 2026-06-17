window.SSRM_3D_EMBODIED_AVATAR_INPUT_BRIDGE_STATE = {
  "condition": "integrated_embodied_avatar_input",
  "avatar": {
    "x": -8.885501,
    "z": 6.13772,
    "fatigue": 0.56124,
    "wetness": 0.1,
    "thermal_comfort": 0.62
  },
  "world": {
    "shared_water": 0.81723,
    "tool_integrity": 0.872282,
    "shelter_warmth": 0.759854,
    "route_confidence": 0.784549,
    "council_acceptance": 0.88559,
    "danger_memory": 0.886366,
    "trace_integrity": 0.66
  },
  "agents": {
    "integrated_deep_time_world:00": {
      "agent_id": "integrated_deep_time_world:00",
      "name": "Ari",
      "role": "scout",
      "trust": 0.8914171246147259,
      "attention": "danger-or-weather-memory",
      "motive": "weather_watch",
      "body_state": 0.8931593351366474,
      "fear": 0.17283162546132025,
      "attachment": 0.8317256600463334,
      "curiosity": 0.6097400000000002,
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
      "last_player_intent": "weather_watch"
    },
    "integrated_deep_time_world:01": {
      "agent_id": "integrated_deep_time_world:01",
      "name": "Bo",
      "role": "builder",
      "trust": 0.9556914607826208,
      "attention": "tool-or-route",
      "motive": "promise",
      "body_state": 0.8565677361254525,
      "fear": 0.16899065577209813,
      "attachment": 0.9040828462679249,
      "curiosity": 0.6919000000000002,
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
      "last_player_intent": "promise"
    },
    "integrated_deep_time_world:02": {
      "agent_id": "integrated_deep_time_world:02",
      "name": "Cy",
      "role": "healer",
      "trust": 0.7941069237509544,
      "attention": "danger-or-weather-memory",
      "motive": "ask_meaning",
      "body_state": 0.8499509558957833,
      "fear": 0.2270125643885712,
      "attachment": 0.8086612007166091,
      "curiosity": 0.5881,
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
      "last_player_intent": "ask_meaning"
    },
    "integrated_deep_time_world:03": {
      "agent_id": "integrated_deep_time_world:03",
      "name": "Dee",
      "role": "farmer",
      "trust": 0.87867719701422,
      "attention": "shared-resource",
      "motive": "offer_resource",
      "body_state": 0.9206398583160347,
      "fear": 0.1459513571150674,
      "attachment": 0.8700640427517504,
      "curiosity": 0.6099,
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
      "last_player_intent": "offer_resource"
    },
    "integrated_deep_time_world:04": {
      "agent_id": "integrated_deep_time_world:04",
      "name": "Eli",
      "role": "guard",
      "trust": 0.818610256057067,
      "attention": "tool-or-route",
      "motive": "promise",
      "body_state": 0.9145110914015805,
      "fear": 0.1571203467544559,
      "attachment": 0.8485288452020788,
      "curiosity": 0.5939,
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
      "last_player_intent": "promise"
    },
    "integrated_deep_time_world:05": {
      "agent_id": "integrated_deep_time_world:05",
      "name": "Fay",
      "role": "teacher",
      "trust": 0.8617465214181947,
      "attention": "care-or-kinship",
      "motive": "comfort",
      "body_state": 0.8896018282485122,
      "fear": 0.14456432361929716,
      "attachment": 0.8477372337803998,
      "curiosity": 0.6454000000000002,
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
      "last_player_intent": "comfort"
    },
    "integrated_deep_time_world:06": {
      "agent_id": "integrated_deep_time_world:06",
      "name": "Gus",
      "role": "trader",
      "trust": 0.8130795288093298,
      "attention": "tool-or-route",
      "motive": "route_request",
      "body_state": 0.8886616926297273,
      "fear": 0.19493639488712236,
      "attachment": 0.8360455309493804,
      "curiosity": 0.5818000000000001,
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
      "last_player_intent": "route_request"
    },
    "integrated_deep_time_world:07": {
      "agent_id": "integrated_deep_time_world:07",
      "name": "Ira",
      "role": "pattern_keeper",
      "trust": 0.8238442079207398,
      "attention": "shared-resource",
      "motive": "share_symbol",
      "body_state": 0.8477239720295974,
      "fear": 0.18020777964749032,
      "attachment": 0.8284124836260316,
      "curiosity": 0.5831000000000001,
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
      "last_player_intent": "share_symbol"
    }
  }
};
