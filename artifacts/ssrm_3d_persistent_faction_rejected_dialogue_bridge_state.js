window.SSRM_3D_PERSISTENT_FACTION_REJECTED_DIALOGUE_STATE = {
  "condition": "integrated_persistent_faction_rejected_dialogue",
  "source_governance": "artifacts/ssrm_3d_infrastructure_proposal_governance_bridge_state.json",
  "source_dialogue": "artifacts/ssrm_3d_governance_memory_dialogue_bridge_state.json",
  "source_agents": "artifacts/ssrm_3d_deep_time_playable_bridge_avatar_agents.json",
  "ledger_status": "rejected bodies are deterministic reconstructions, not original stored proposals",
  "agents": {
    "integrated_deep_time_world:00": {
      "agent_id": "integrated_deep_time_world:00",
      "name": "Ari",
      "role": "scout",
      "faction": "safety",
      "native_tokens": [
        "vosha",
        "shanoeya",
        "nono",
        "misavo"
      ],
      "translation_hints": {
        "vosha": "danger-or-weather-memory",
        "shanoeya": "shared-resource",
        "nono": "tool-or-route",
        "misavo": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:01": {
      "agent_id": "integrated_deep_time_world:01",
      "name": "Bo",
      "role": "builder",
      "faction": "material",
      "native_tokens": [
        "eyaom",
        "nonoeya",
        "vori",
        "shatusha"
      ],
      "translation_hints": {
        "eyaom": "danger-or-weather-memory",
        "nonoeya": "shared-resource",
        "vori": "tool-or-route",
        "shatusha": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:02": {
      "agent_id": "integrated_deep_time_world:02",
      "name": "Cy",
      "role": "healer",
      "faction": "care",
      "native_tokens": [
        "shath",
        "shathsha",
        "voeya",
        "eyasami"
      ],
      "translation_hints": {
        "shath": "danger-or-weather-memory",
        "shathsha": "shared-resource",
        "voeya": "tool-or-route",
        "eyasami": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:03": {
      "agent_id": "integrated_deep_time_world:03",
      "name": "Dee",
      "role": "farmer",
      "faction": "material",
      "native_tokens": [
        "shavo",
        "vonono",
        "saka",
        "shatusha"
      ],
      "translation_hints": {
        "shavo": "danger-or-weather-memory",
        "vonono": "shared-resource",
        "saka": "tool-or-route",
        "shatusha": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:04": {
      "agent_id": "integrated_deep_time_world:04",
      "name": "Eli",
      "role": "guard",
      "faction": "safety",
      "native_tokens": [
        "mitu",
        "vovomi",
        "mivo",
        "kathth"
      ],
      "translation_hints": {
        "mitu": "danger-or-weather-memory",
        "vovomi": "shared-resource",
        "mivo": "tool-or-route",
        "kathth": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:05": {
      "agent_id": "integrated_deep_time_world:05",
      "name": "Fay",
      "role": "teacher",
      "faction": "care",
      "native_tokens": [
        "vomi",
        "shalenka",
        "tulen",
        "milenno"
      ],
      "translation_hints": {
        "vomi": "danger-or-weather-memory",
        "shalenka": "shared-resource",
        "tulen": "tool-or-route",
        "milenno": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:06": {
      "agent_id": "integrated_deep_time_world:06",
      "name": "Gus",
      "role": "trader",
      "faction": "material",
      "native_tokens": [
        "leneya",
        "kamith",
        "omno",
        "omriri"
      ],
      "translation_hints": {
        "leneya": "danger-or-weather-memory",
        "kamith": "shared-resource",
        "omno": "tool-or-route",
        "omriri": "care-or-kinship"
      },
      "trust": 1.0
    },
    "integrated_deep_time_world:07": {
      "agent_id": "integrated_deep_time_world:07",
      "name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "native_tokens": [
        "omom",
        "mieyaeya",
        "voeya",
        "vothsha"
      ],
      "translation_hints": {
        "omom": "danger-or-weather-memory",
        "mieyaeya": "shared-resource",
        "voeya": "tool-or-route",
        "vothsha": "care-or-kinship"
      },
      "trust": 1.0
    }
  },
  "rejected_proposal_ledger": [
    {
      "id": "c01_rej_00_scout_sanitation_repair",
      "council": 1,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "sanitation_repair",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.533232,
      "focus": "care-or-kinship",
      "native_token": "misavo",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "ash": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.277281,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c01_rej_01_healer_signal_visibility",
      "council": 1,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "signal_visibility",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.557708,
      "focus": "danger-or-weather-memory",
      "native_token": "shath",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "resin": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.290008,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c01_rej_02_guard_water_security",
      "council": 1,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "water_security",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.583568,
      "focus": "shared-resource",
      "native_token": "vovomi",
      "requirements": {
        "fiber": 12,
        "stone": 12,
        "clay": 10
      },
      "requested_budget": 34,
      "score_proxy": 0.303455,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c01_rej_03_trader_care_access",
      "council": 1,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "care_access",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.533232,
      "focus": "care-or-kinship",
      "native_token": "omriri",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "hide": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.277281,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c01_rej_04_scout_language_marker",
      "council": 1,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "language_marker",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.557708,
      "focus": "shared-resource",
      "native_token": "shanoeya",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "charcoal": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.290008,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c02_rej_00_builder_route_safety",
      "council": 2,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "route_safety",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.404499,
      "focus": "danger-or-weather-memory",
      "native_token": "eyaom",
      "requirements": {
        "stone": 6,
        "wood": 6,
        "charcoal": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.330339,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c02_rej_01_farmer_object_access",
      "council": 2,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "object_access",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ash_drain",
      "severity": 0.427178,
      "focus": "shared-resource",
      "native_token": "vonono",
      "requirements": {
        "wood": 7,
        "clay": 7,
        "fiber": 7
      },
      "requested_budget": 21,
      "score_proxy": 0.342133,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c02_rej_02_teacher_sanitation_repair",
      "council": 2,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "sanitation_repair",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.479194,
      "focus": "care-or-kinship",
      "native_token": "milenno",
      "requirements": {
        "ash": 9,
        "stone": 9,
        "wood": 9
      },
      "requested_budget": 27,
      "score_proxy": 0.369181,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c02_rej_03_pattern_keeper_signal_visibility",
      "council": 2,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "signal_visibility",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.404499,
      "focus": "danger-or-weather-memory",
      "native_token": "omom",
      "requirements": {
        "resin": 6,
        "charcoal": 6,
        "wood": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.330339,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c02_rej_04_builder_water_security",
      "council": 2,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "water_security",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ash_drain",
      "severity": 0.427178,
      "focus": "shared-resource",
      "native_token": "nonoeya",
      "requirements": {
        "clay": 7,
        "stone": 7,
        "wood": 7
      },
      "requested_budget": 21,
      "score_proxy": 0.342133,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c03_rej_00_healer_object_access",
      "council": 3,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "object_access",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.405613,
      "focus": "shared-resource",
      "native_token": "shathsha",
      "requirements": {
        "wood": 6,
        "clay": 6,
        "fiber": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.210919,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c03_rej_01_guard_sanitation_repair",
      "council": 3,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "sanitation_repair",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.433913,
      "focus": "care-or-kinship",
      "native_token": "kathth",
      "requirements": {
        "ash": 8,
        "stone": 8,
        "wood": 8
      },
      "requested_budget": 24,
      "score_proxy": 0.225635,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c03_rej_02_trader_signal_visibility",
      "council": 3,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "signal_visibility",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "covered_walk",
      "severity": 0.431786,
      "focus": "danger-or-weather-memory",
      "native_token": "leneya",
      "requirements": {
        "resin": 9,
        "charcoal": 9,
        "wood": 9
      },
      "requested_budget": 27,
      "score_proxy": 0.224529,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c03_rej_03_scout_water_security",
      "council": 3,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "water_security",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.405613,
      "focus": "shared-resource",
      "native_token": "shanoeya",
      "requirements": {
        "clay": 6,
        "stone": 6,
        "wood": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.210919,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c03_rej_04_healer_care_access",
      "council": 3,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "care_access",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.433913,
      "focus": "care-or-kinship",
      "native_token": "eyasami",
      "requirements": {
        "fiber": 8,
        "hide": 8,
        "wood": 8
      },
      "requested_budget": 24,
      "score_proxy": 0.345635,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c04_rej_00_farmer_sanitation_repair",
      "council": 4,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "sanitation_repair",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.374211,
      "focus": "care-or-kinship",
      "native_token": "shatusha",
      "requirements": {
        "ash": 6,
        "stone": 6,
        "wood": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.19459,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c04_rej_01_teacher_signal_visibility",
      "council": 4,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "signal_visibility",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.405388,
      "focus": "danger-or-weather-memory",
      "native_token": "vomi",
      "requirements": {
        "resin": 7,
        "charcoal": 7,
        "wood": 7
      },
      "requested_budget": 21,
      "score_proxy": 0.210802,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c04_rej_02_pattern_keeper_water_security",
      "council": 4,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "water_security",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "smoke_watchtower",
      "severity": 0.43374,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "clay": 9,
        "stone": 9,
        "wood": 9
      },
      "requested_budget": 27,
      "score_proxy": 0.225545,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c04_rej_03_builder_care_access",
      "council": 4,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "care_access",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.374211,
      "focus": "care-or-kinship",
      "native_token": "shatusha",
      "requirements": {
        "fiber": 6,
        "hide": 6,
        "wood": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.19459,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c04_rej_04_farmer_language_marker",
      "council": 4,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "language_marker",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.405388,
      "focus": "shared-resource",
      "native_token": "vonono",
      "requirements": {
        "stone": 7,
        "charcoal": 7,
        "clay": 7
      },
      "requested_budget": 21,
      "score_proxy": 0.210802,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c05_rej_00_guard_language_marker",
      "council": 5,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "language_marker",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.388059,
      "focus": "shared-resource",
      "native_token": "vovomi",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "charcoal": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.201791,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c05_rej_01_trader_maintenance_debt",
      "council": 5,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ridge_steps",
      "severity": 0.418363,
      "focus": "tool-or-route",
      "native_token": "omno",
      "requirements": {
        "fiber": 9,
        "stone": 9
      },
      "requested_budget": 18,
      "score_proxy": 0.337549,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c05_rej_02_scout_route_safety",
      "council": 5,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "route_safety",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.453364,
      "focus": "danger-or-weather-memory",
      "native_token": "vosha",
      "requirements": {
        "fiber": 11,
        "stone": 11,
        "charcoal": 9
      },
      "requested_budget": 31,
      "score_proxy": 0.355749,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c05_rej_03_healer_object_access",
      "council": 5,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "object_access",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ridge_steps",
      "severity": 0.409531,
      "focus": "shared-resource",
      "native_token": "shathsha",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "clay": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.212956,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c06_rej_00_teacher_care_access",
      "council": 6,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "care_access",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.377394,
      "focus": "care-or-kinship",
      "native_token": "milenno",
      "requirements": {
        "wood": 8,
        "fiber": 6,
        "hide": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.316245,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c06_rej_01_pattern_keeper_language_marker",
      "council": 6,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "language_marker",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.388292,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "wood": 9,
        "stone": 7,
        "charcoal": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.321912,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c06_rej_02_builder_maintenance_debt",
      "council": 6,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "maintenance_debt",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.463637,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "wood": 11,
        "stone": 9,
        "fiber": 9
      },
      "requested_budget": 29,
      "score_proxy": 0.361091,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c06_rej_03_farmer_route_safety",
      "council": 6,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "route_safety",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.377394,
      "focus": "danger-or-weather-memory",
      "native_token": "shavo",
      "requirements": {
        "wood": 8,
        "stone": 6,
        "charcoal": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.316245,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c06_rej_04_teacher_object_access",
      "council": 6,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "object_access",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.388292,
      "focus": "shared-resource",
      "native_token": "shalenka",
      "requirements": {
        "wood": 9,
        "clay": 7,
        "fiber": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.201912,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c07_rej_00_trader_route_safety",
      "council": 7,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "route_safety",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.352081,
      "focus": "danger-or-weather-memory",
      "native_token": "leneya",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "charcoal": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.303082,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c07_rej_01_scout_object_access",
      "council": 7,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "object_access",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.413249,
      "focus": "shared-resource",
      "native_token": "shanoeya",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "clay": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.214889,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c07_rej_02_healer_sanitation_repair",
      "council": 7,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "sanitation_repair",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.430528,
      "focus": "care-or-kinship",
      "native_token": "eyasami",
      "requirements": {
        "fiber": 11,
        "stone": 11,
        "ash": 9
      },
      "requested_budget": 31,
      "score_proxy": 0.343875,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c07_rej_03_guard_signal_visibility",
      "council": 7,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "signal_visibility",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.360466,
      "focus": "danger-or-weather-memory",
      "native_token": "mitu",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "resin": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.307442,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c08_rej_00_pattern_keeper_object_access",
      "council": 8,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "object_access",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "shelter_roof",
      "project": "mud_causeway",
      "severity": 0.342555,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "clay": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.178129,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c08_rej_01_builder_sanitation_repair",
      "council": 8,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "sanitation_repair",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "shelter_roof",
      "project": "mud_causeway",
      "severity": 0.358199,
      "focus": "care-or-kinship",
      "native_token": "shatusha",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "ash": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.186263,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c08_rej_02_farmer_signal_visibility",
      "council": 8,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "signal_visibility",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "shelter_roof",
      "project": "smoke_watchtower",
      "severity": 0.392428,
      "focus": "danger-or-weather-memory",
      "native_token": "shavo",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "resin": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.204063,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c08_rej_03_teacher_water_security",
      "council": 8,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "water_security",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "shelter_roof",
      "project": "drum_resonance_posts",
      "severity": 0.358557,
      "focus": "shared-resource",
      "native_token": "shalenka",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "clay": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.30645,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c09_rej_00_scout_sanitation_repair",
      "council": 9,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "sanitation_repair",
      "route": [
        "storage_yard",
        "roof_ring"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.348709,
      "focus": "care-or-kinship",
      "native_token": "misavo",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "ash": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.181329,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c09_rej_01_healer_signal_visibility",
      "council": 9,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "signal_visibility",
      "route": [
        "ash_edge",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "archive_waystones",
      "severity": 0.349413,
      "focus": "danger-or-weather-memory",
      "native_token": "shath",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "resin": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.181695,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c09_rej_02_guard_water_security",
      "council": 9,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "water_security",
      "route": [
        "roof_ring",
        "storage_yard"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.378002,
      "focus": "shared-resource",
      "native_token": "vovomi",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "clay": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.196561,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c09_rej_03_trader_care_access",
      "council": 9,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "care_access",
      "route": [
        "drum_court",
        "roof_ring"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.308432,
      "focus": "care-or-kinship",
      "native_token": "omriri",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "hide": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.160385,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c10_rej_00_builder_signal_visibility",
      "council": 10,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "signal_visibility",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "waste_pit",
      "project": "ridge_steps",
      "severity": 0.334669,
      "focus": "danger-or-weather-memory",
      "native_token": "eyaom",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "resin": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.174028,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c10_rej_01_farmer_water_security",
      "council": 10,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "water_security",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "waste_pit",
      "project": "ridge_steps",
      "severity": 0.366531,
      "focus": "shared-resource",
      "native_token": "vonono",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "clay": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.310596,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c10_rej_02_teacher_care_access",
      "council": 10,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "care_access",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "waste_pit",
      "project": "ridge_steps",
      "severity": 0.379733,
      "focus": "care-or-kinship",
      "native_token": "milenno",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "hide": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.317461,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c10_rej_03_pattern_keeper_language_marker",
      "council": 10,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "language_marker",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "waste_pit",
      "project": "smoke_watchtower",
      "severity": 0.325587,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "charcoal": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.289305,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c11_rej_00_healer_water_security",
      "council": 11,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "water_security",
      "route": [
        "ash_edge",
        "grain_shade"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.304861,
      "focus": "shared-resource",
      "native_token": "shathsha",
      "requirements": {
        "fiber": 8,
        "stone": 8,
        "clay": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.278528,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c11_rej_01_guard_care_access",
      "council": 11,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "care_access",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.320505,
      "focus": "care-or-kinship",
      "native_token": "kathth",
      "requirements": {
        "fiber": 9,
        "stone": 9,
        "hide": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.166663,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c11_rej_02_trader_language_marker",
      "council": 11,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "language_marker",
      "route": [
        "ash_edge",
        "grain_shade"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.397829,
      "focus": "shared-resource",
      "native_token": "kamith",
      "requirements": {
        "fiber": 10,
        "stone": 10,
        "charcoal": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.206871,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c11_rej_03_scout_maintenance_debt",
      "council": 11,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "maintenance_debt",
      "route": [
        "ash_edge",
        "grain_shade"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.325396,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "fiber": 8,
        "stone": 8
      },
      "requested_budget": 16,
      "score_proxy": 0.289206,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "fiber",
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c12_rej_00_farmer_water_security",
      "council": 12,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "water_security",
      "route": [
        "tool_bend",
        "archive_knoll"
      ],
      "object": "fire_hearth",
      "project": "ash_drain",
      "severity": 0.296676,
      "focus": "shared-resource",
      "native_token": "vonono",
      "requirements": {
        "stone": 8,
        "wood": 8,
        "clay": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.274272,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c12_rej_01_teacher_care_access",
      "council": 12,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "care_access",
      "route": [
        "nursery_nest",
        "central_hearth"
      ],
      "object": "fire_hearth",
      "project": "ash_drain",
      "severity": 0.311889,
      "focus": "care-or-kinship",
      "native_token": "milenno",
      "requirements": {
        "stone": 9,
        "wood": 9,
        "fiber": 7
      },
      "requested_budget": 25,
      "score_proxy": 0.282182,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c12_rej_02_pattern_keeper_language_marker",
      "council": 12,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "language_marker",
      "route": [
        "tool_bend",
        "archive_knoll"
      ],
      "object": "fire_hearth",
      "project": "ash_drain",
      "severity": 0.387211,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "stone": 10,
        "wood": 10,
        "charcoal": 8
      },
      "requested_budget": 28,
      "score_proxy": 0.32135,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c12_rej_03_builder_maintenance_debt",
      "council": 12,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "roof_ring"
      ],
      "object": "fire_hearth",
      "project": "ash_drain",
      "severity": 0.317597,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "stone": 8,
        "wood": 8,
        "fiber": 6
      },
      "requested_budget": 22,
      "score_proxy": 0.28515,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "stone",
        "wood"
      ],
      "anchor_accepted_proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c13_rej_00_guard_water_security",
      "council": 13,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "water_security",
      "route": [
        "central_hearth",
        "roof_ring"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.317123,
      "focus": "shared-resource",
      "native_token": "vovomi",
      "requirements": {
        "wood": 8,
        "clay": 6,
        "stone": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.164904,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c13_rej_01_trader_care_access",
      "council": 13,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "care_access",
      "route": [
        "grain_shade",
        "storage_yard"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.352509,
      "focus": "care-or-kinship",
      "native_token": "omriri",
      "requirements": {
        "wood": 9,
        "fiber": 7,
        "hide": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.183305,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c13_rej_02_scout_language_marker",
      "council": 13,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "language_marker",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.362633,
      "focus": "shared-resource",
      "native_token": "shanoeya",
      "requirements": {
        "wood": 10,
        "stone": 8,
        "charcoal": 8
      },
      "requested_budget": 26,
      "score_proxy": 0.188569,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c13_rej_03_healer_maintenance_debt",
      "council": 13,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "maintenance_debt",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.292573,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 8,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.152138,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "wood"
      ],
      "anchor_accepted_proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c14_rej_00_teacher_water_security",
      "council": 14,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "water_security",
      "route": [
        "smoke_watch",
        "drum_court"
      ],
      "object": "shelter_roof",
      "project": "archive_waystones",
      "severity": 0.259963,
      "focus": "shared-resource",
      "native_token": "shalenka",
      "requirements": {
        "clay": 5,
        "stone": 5,
        "wood": 5
      },
      "requested_budget": 15,
      "score_proxy": 0.255181,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c14_rej_01_pattern_keeper_care_access",
      "council": 14,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "care_access",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "shelter_roof",
      "project": "archive_waystones",
      "severity": 0.270473,
      "focus": "care-or-kinship",
      "native_token": "vothsha",
      "requirements": {
        "fiber": 6,
        "hide": 6,
        "wood": 6
      },
      "requested_budget": 18,
      "score_proxy": 0.140646,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c14_rej_02_builder_language_marker",
      "council": 14,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "language_marker",
      "route": [
        "drum_court",
        "smoke_watch"
      ],
      "object": "shelter_roof",
      "project": "archive_waystones",
      "severity": 0.304789,
      "focus": "shared-resource",
      "native_token": "nonoeya",
      "requirements": {
        "stone": 8,
        "charcoal": 8,
        "clay": 8
      },
      "requested_budget": 24,
      "score_proxy": 0.15849,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c14_rej_03_farmer_maintenance_debt",
      "council": 14,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "maintenance_debt",
      "route": [
        "smoke_watch",
        "drum_court"
      ],
      "object": "shelter_roof",
      "project": "archive_waystones",
      "severity": 0.260349,
      "focus": "tool-or-route",
      "native_token": "saka",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 15,
      "score_proxy": 0.255381,
      "decision": "rejected",
      "rejected_reason": "priority-conflict-lost",
      "budget_tight_materials": [],
      "anchor_accepted_proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "evidence_strength": 0.58,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c15_rej_00_trader_language_marker",
      "council": 15,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "language_marker",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.293171,
      "focus": "shared-resource",
      "native_token": "kamith",
      "requirements": {
        "charcoal": 8,
        "stone": 6,
        "clay": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.152449,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c15_rej_01_scout_maintenance_debt",
      "council": 15,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "maintenance_debt",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "herb_garden",
      "project": "smoke_watchtower",
      "severity": 0.30829,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "charcoal": 9,
        "wood": 7,
        "stone": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.280311,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c15_rej_02_healer_route_safety",
      "council": 15,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "route_safety",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "herb_garden",
      "project": "smoke_watchtower",
      "severity": 0.36587,
      "focus": "danger-or-weather-memory",
      "native_token": "shath",
      "requirements": {
        "charcoal": 10,
        "stone": 8,
        "wood": 8
      },
      "requested_budget": 26,
      "score_proxy": 0.190252,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c15_rej_03_guard_object_access",
      "council": 15,
      "season": "scarcity-wind",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "object_access",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "herb_garden",
      "project": "smoke_watchtower",
      "severity": 0.293557,
      "focus": "shared-resource",
      "native_token": "vovomi",
      "requirements": {
        "charcoal": 8,
        "wood": 6,
        "clay": 6
      },
      "requested_budget": 20,
      "score_proxy": 0.15265,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c16_rej_00_pattern_keeper_maintenance_debt",
      "council": 16,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "maintenance_debt",
      "route": [
        "storage_yard",
        "roof_ring"
      ],
      "object": "tool_cache",
      "project": "smoke_watchtower",
      "severity": 0.275344,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "charcoal": 7,
        "wood": 5,
        "stone": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.263179,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c16_rej_01_builder_route_safety",
      "council": 16,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "route_safety",
      "route": [
        "loom_room",
        "herb_slope"
      ],
      "object": "tool_cache",
      "project": "ridge_steps",
      "severity": 0.313972,
      "focus": "danger-or-weather-memory",
      "native_token": "eyaom",
      "requirements": {
        "charcoal": 9,
        "stone": 7,
        "wood": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.283265,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c16_rej_02_farmer_object_access",
      "council": 16,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "object_access",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "tool_cache",
      "project": "ridge_steps",
      "severity": 0.351284,
      "focus": "shared-resource",
      "native_token": "vonono",
      "requirements": {
        "charcoal": 10,
        "wood": 8,
        "clay": 8
      },
      "requested_budget": 26,
      "score_proxy": 0.302668,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c16_rej_03_teacher_sanitation_repair",
      "council": 16,
      "season": "teaching-moon",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "sanitation_repair",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "tool_cache",
      "project": "smoke_watchtower",
      "severity": 0.278586,
      "focus": "care-or-kinship",
      "native_token": "milenno",
      "requirements": {
        "charcoal": 7,
        "ash": 5,
        "stone": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.264865,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c17_rej_00_scout_route_safety",
      "council": 17,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "faction": "safety",
      "kind": "route_safety",
      "route": [
        "central_hearth",
        "roof_ring"
      ],
      "object": "loom_frame",
      "project": "mud_causeway",
      "severity": 0.278106,
      "focus": "danger-or-weather-memory",
      "native_token": "vosha",
      "requirements": {
        "charcoal": 7,
        "stone": 5,
        "wood": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.264615,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c17_rej_01_healer_object_access",
      "council": 17,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "faction": "care",
      "kind": "object_access",
      "route": [
        "central_hearth",
        "roof_ring"
      ],
      "object": "loom_frame",
      "project": "ridge_steps",
      "severity": 0.310407,
      "focus": "shared-resource",
      "native_token": "shathsha",
      "requirements": {
        "charcoal": 9,
        "wood": 7,
        "clay": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.161412,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c17_rej_02_guard_sanitation_repair",
      "council": 17,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "faction": "safety",
      "kind": "sanitation_repair",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "loom_frame",
      "project": "ridge_steps",
      "severity": 0.342165,
      "focus": "care-or-kinship",
      "native_token": "kathth",
      "requirements": {
        "charcoal": 10,
        "ash": 8,
        "stone": 8
      },
      "requested_budget": 26,
      "score_proxy": 0.177926,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c17_rej_03_trader_signal_visibility",
      "council": 17,
      "season": "wet-cold",
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "faction": "material",
      "kind": "signal_visibility",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "loom_frame",
      "project": "mud_causeway",
      "severity": 0.255526,
      "focus": "danger-or-weather-memory",
      "native_token": "leneya",
      "requirements": {
        "charcoal": 7,
        "resin": 5,
        "wood": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.132874,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c18_rej_00_builder_object_access",
      "council": 18,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "faction": "material",
      "kind": "object_access",
      "route": [
        "roof_ring",
        "drum_court"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.270729,
      "focus": "shared-resource",
      "native_token": "nonoeya",
      "requirements": {
        "charcoal": 7,
        "wood": 5,
        "clay": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.260779,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c18_rej_01_farmer_sanitation_repair",
      "council": 18,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "faction": "material",
      "kind": "sanitation_repair",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "herb_garden",
      "project": "drum_resonance_posts",
      "severity": 0.28909,
      "focus": "care-or-kinship",
      "native_token": "shatusha",
      "requirements": {
        "charcoal": 9,
        "ash": 7,
        "stone": 7
      },
      "requested_budget": 23,
      "score_proxy": 0.150327,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c18_rej_02_teacher_signal_visibility",
      "council": 18,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "faction": "care",
      "kind": "signal_visibility",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "herb_garden",
      "project": "ridge_steps",
      "severity": 0.314484,
      "focus": "danger-or-weather-memory",
      "native_token": "vomi",
      "requirements": {
        "charcoal": 10,
        "resin": 8,
        "wood": 8
      },
      "requested_budget": 26,
      "score_proxy": 0.163532,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    },
    {
      "id": "c18_rej_03_pattern_keeper_water_security",
      "council": 18,
      "season": "repair-sun",
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "faction": "archive",
      "kind": "water_security",
      "route": [
        "drum_court",
        "roof_ring"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.27667,
      "focus": "shared-resource",
      "native_token": "mieyaeya",
      "requirements": {
        "charcoal": 7,
        "clay": 5,
        "stone": 5
      },
      "requested_budget": 17,
      "score_proxy": 0.143868,
      "decision": "rejected",
      "rejected_reason": "scarce-material-overreach",
      "budget_tight_materials": [
        "charcoal"
      ],
      "anchor_accepted_proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
      "evidence_strength": 0.78,
      "evidence_basis": [
        "council.rejected_count",
        "budget_remaining",
        "accepted_pressure_anchor"
      ],
      "reconstruction_status": "deterministic_reconstructed_not_original"
    }
  ],
  "accepted_event_sample": [
    {
      "id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
      "council": 1,
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.543232,
      "route_pressure": 0.3012,
      "object_pressure": 0.429576,
      "maintenance_pressure": 0.47016,
      "focus": "tool-or-route",
      "native_token": "mivo",
      "requirements": {
        "wood": 6,
        "stone": 7,
        "fiber": 7
      },
      "requested_budget": 20,
      "score": 0.714042,
      "accepted": true,
      "allocated": 20,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.149756,
        "object_delta": 0.069013,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
      "council": 1,
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.532708,
      "route_pressure": 0.3012,
      "object_pressure": 0.429576,
      "maintenance_pressure": 0.47016,
      "focus": "tool-or-route",
      "native_token": "saka",
      "requirements": {
        "wood": 6,
        "stone": 7,
        "fiber": 7
      },
      "requested_budget": 20,
      "score": 0.709201,
      "accepted": true,
      "allocated": 20,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.148598,
        "object_delta": 0.068645,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
      "council": 1,
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "grain_store",
      "project": "ridge_steps",
      "severity": 0.523568,
      "route_pressure": 0.3012,
      "object_pressure": 0.429576,
      "maintenance_pressure": 0.47016,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "wood": 7,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 19,
      "score": 0.704996,
      "accepted": true,
      "allocated": 19,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.147592,
        "object_delta": 0.068325,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
      "council": 2,
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.459194,
      "route_pressure": 0.2228,
      "object_pressure": 0.405848,
      "maintenance_pressure": 0.381966,
      "focus": "tool-or-route",
      "native_token": "tulen",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.647171,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.140511,
        "object_delta": 0.066072,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
      "council": 2,
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "mud_causeway",
      "severity": 0.454499,
      "route_pressure": 0.230469,
      "object_pressure": 0.405848,
      "maintenance_pressure": 0.381966,
      "focus": "tool-or-route",
      "native_token": "omno",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 16,
      "score": 0.646239,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.139995,
        "object_delta": 0.065907,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
      "council": 2,
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ash_drain",
      "severity": 0.442178,
      "route_pressure": 0.230469,
      "object_pressure": 0.405848,
      "maintenance_pressure": 0.373048,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.639322,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.13864,
        "object_delta": 0.065476,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
      "council": 3,
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.448913,
      "route_pressure": 0.2332,
      "object_pressure": 0.382542,
      "maintenance_pressure": 0.375,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 15,
      "score": 0.639868,
      "accepted": true,
      "allocated": 15,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.13938,
        "object_delta": 0.065712,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
      "council": 3,
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "covered_walk",
      "severity": 0.411786,
      "route_pressure": 0.2332,
      "object_pressure": 0.382542,
      "maintenance_pressure": 0.3672,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.621697,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.135296,
        "object_delta": 0.064413,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
      "council": 3,
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "grain_store",
      "project": "drum_resonance_posts",
      "severity": 0.455613,
      "route_pressure": 0.2332,
      "object_pressure": 0.382542,
      "maintenance_pressure": 0.375,
      "focus": "tool-or-route",
      "native_token": "mivo",
      "requirements": {
        "wood": 5,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.60795,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.140117,
        "object_delta": 0.065946,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
      "council": 4,
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.424211,
      "route_pressure": 0.20051,
      "object_pressure": 0.329813,
      "maintenance_pressure": 0.35784,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 15,
      "score": 0.57849,
      "accepted": true,
      "allocated": 15,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.136663,
        "object_delta": 0.074847,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
      "council": 4,
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "archive_waystones",
      "severity": 0.420388,
      "route_pressure": 0.20051,
      "object_pressure": 0.329813,
      "maintenance_pressure": 0.35784,
      "focus": "tool-or-route",
      "native_token": "saka",
      "requirements": {
        "wood": 5,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.576731,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.136243,
        "object_delta": 0.068776,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
      "council": 4,
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "waste_pit",
      "project": "smoke_watchtower",
      "severity": 0.41374,
      "route_pressure": 0.20051,
      "object_pressure": 0.329813,
      "maintenance_pressure": 0.342183,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.571481,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.135511,
        "object_delta": 0.064481,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
      "council": 5,
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.398059,
      "route_pressure": 0.186266,
      "object_pressure": 0.344713,
      "maintenance_pressure": 0.344272,
      "focus": "tool-or-route",
      "native_token": "tulen",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.564368,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.133786,
        "object_delta": 0.063932,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
      "council": 5,
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ridge_steps",
      "severity": 0.393363,
      "route_pressure": 0.186266,
      "object_pressure": 0.344713,
      "maintenance_pressure": 0.35316,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 16,
      "score": 0.563452,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.13327,
        "object_delta": 0.063768,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
      "council": 5,
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "herb_switchback",
      "severity": 0.393364,
      "route_pressure": 0.186266,
      "object_pressure": 0.344713,
      "maintenance_pressure": 0.344272,
      "focus": "tool-or-route",
      "native_token": "omno",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 16,
      "score": 0.562208,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.13327,
        "object_delta": 0.063768,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
      "council": 5,
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "kind": "maintenance_debt",
      "route": [
        "spring_hollow",
        "ash_edge"
      ],
      "object": "herb_garden",
      "project": "ridge_steps",
      "severity": 0.419531,
      "route_pressure": 0.186266,
      "object_pressure": 0.344713,
      "maintenance_pressure": 0.35316,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 15,
      "score": 0.540489,
      "accepted": true,
      "allocated": 15,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.136148,
        "object_delta": 0.064684,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
      "council": 6,
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.363292,
      "route_pressure": 0.167396,
      "object_pressure": 0.33208,
      "maintenance_pressure": 0.334048,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.542156,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.129962,
        "object_delta": 0.062715,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
      "council": 6,
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "kind": "maintenance_debt",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.403637,
      "route_pressure": 0.1652,
      "object_pressure": 0.33208,
      "maintenance_pressure": 0.3282,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.524544,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.1344,
        "object_delta": 0.064127,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
      "council": 6,
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "kind": "maintenance_debt",
      "route": [
        "tool_bend",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "ash_drain",
      "severity": 0.387394,
      "route_pressure": 0.1652,
      "object_pressure": 0.33208,
      "maintenance_pressure": 0.334048,
      "focus": "tool-or-route",
      "native_token": "tulen",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.517891,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.132613,
        "object_delta": 0.063559,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 5,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
      "council": 7,
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "kind": "maintenance_debt",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.370528,
      "route_pressure": 0.163,
      "object_pressure": 0.321878,
      "maintenance_pressure": 0.314,
      "focus": "tool-or-route",
      "native_token": "omno",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 16,
      "score": 0.505546,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.130758,
        "object_delta": 0.062968,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
      "council": 7,
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "kind": "maintenance_debt",
      "route": [
        "archive_knoll",
        "cairn_ridge"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.370466,
      "route_pressure": 0.163,
      "object_pressure": 0.321878,
      "maintenance_pressure": 0.314,
      "focus": "tool-or-route",
      "native_token": "saka",
      "requirements": {
        "wood": 5,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.505517,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.130751,
        "object_delta": 0.062966,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
      "council": 7,
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.362081,
      "route_pressure": 0.163,
      "object_pressure": 0.321878,
      "maintenance_pressure": 0.314,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 16,
      "score": 0.50166,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.129829,
        "object_delta": 0.062673,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
      "council": 7,
      "agent_id": "integrated_deep_time_world:01",
      "agent_name": "Bo",
      "role": "builder",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "archive_knoll"
      ],
      "object": "grain_store",
      "project": "tool_sledge_path",
      "severity": 0.388249,
      "route_pressure": 0.163,
      "object_pressure": 0.321878,
      "maintenance_pressure": 0.314,
      "focus": "tool-or-route",
      "native_token": "vori",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 15,
      "score": 0.478697,
      "accepted": true,
      "allocated": 15,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.063228,
        "object_delta": 0.063589,
        "debt_delta": 0.021795
      },
      "decision": "accepted",
      "season": "scarcity-wind",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
      "council": 8,
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "kind": "maintenance_debt",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "shelter_roof",
      "project": "mud_causeway",
      "severity": 0.333199,
      "route_pressure": 0.1444,
      "object_pressure": 0.289372,
      "maintenance_pressure": 0.303966,
      "focus": "tool-or-route",
      "native_token": "mivo",
      "requirements": {
        "wood": 4,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 14,
      "score": 0.479443,
      "accepted": true,
      "allocated": 14,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.126652,
        "object_delta": 0.071662,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
      "council": 8,
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "kind": "maintenance_debt",
      "route": [
        "storage_yard",
        "grain_shade"
      ],
      "object": "shelter_roof",
      "project": "smoke_watchtower",
      "severity": 0.332428,
      "route_pressure": 0.1444,
      "object_pressure": 0.289372,
      "maintenance_pressure": 0.303183,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 5,
        "stone": 4,
        "fiber": 5
      },
      "requested_budget": 14,
      "score": 0.478979,
      "accepted": true,
      "allocated": 14,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.126567,
        "object_delta": 0.063135,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
      "council": 8,
      "agent_id": "integrated_deep_time_world:02",
      "agent_name": "Cy",
      "role": "healer",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "shelter_roof",
      "project": "drum_resonance_posts",
      "severity": 0.368557,
      "route_pressure": 0.146775,
      "object_pressure": 0.289372,
      "maintenance_pressure": 0.297,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 6,
        "fiber": 5
      },
      "requested_budget": 17,
      "score": 0.460112,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.130541,
        "object_delta": 0.052899,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
      "council": 8,
      "agent_id": "integrated_deep_time_world:03",
      "agent_name": "Dee",
      "role": "farmer",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "herb_slope"
      ],
      "object": "shelter_roof",
      "project": "mud_causeway",
      "severity": 0.352555,
      "route_pressure": 0.135715,
      "object_pressure": 0.289372,
      "maintenance_pressure": 0.303966,
      "focus": "tool-or-route",
      "native_token": "saka",
      "requirements": {
        "wood": 5,
        "stone": 6,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.451957,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.128781,
        "object_delta": 0.052339,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "teaching-moon",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
      "council": 9,
      "agent_id": "integrated_deep_time_world:07",
      "agent_name": "Ira",
      "role": "pattern_keeper",
      "kind": "maintenance_debt",
      "route": [
        "storage_yard",
        "roof_ring"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.358709,
      "route_pressure": 0.1284,
      "object_pressure": 0.273344,
      "maintenance_pressure": 0.2892,
      "focus": "tool-or-route",
      "native_token": "voeya",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 6
      },
      "requested_budget": 17,
      "score": 0.449306,
      "accepted": true,
      "allocated": 17,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.129458,
        "object_delta": 0.062555,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
      "council": 9,
      "agent_id": "integrated_deep_time_world:06",
      "agent_name": "Gus",
      "role": "trader",
      "kind": "maintenance_debt",
      "route": [
        "ash_edge",
        "grain_shade"
      ],
      "object": "nursery_mat",
      "project": "archive_waystones",
      "severity": 0.324413,
      "route_pressure": 0.1312,
      "object_pressure": 0.273344,
      "maintenance_pressure": 0.27984,
      "focus": "tool-or-route",
      "native_token": "omno",
      "requirements": {
        "wood": 4,
        "stone": 4,
        "fiber": 5
      },
      "requested_budget": 13,
      "score": 0.432668,
      "accepted": true,
      "allocated": 13,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.125685,
        "object_delta": 0.061354,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
      "council": 9,
      "agent_id": "integrated_deep_time_world:05",
      "agent_name": "Fay",
      "role": "teacher",
      "kind": "maintenance_debt",
      "route": [
        "roof_ring",
        "storage_yard"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.318002,
      "route_pressure": 0.1284,
      "object_pressure": 0.273344,
      "maintenance_pressure": 0.2892,
      "focus": "tool-or-route",
      "native_token": "tulen",
      "requirements": {
        "wood": 5,
        "stone": 5,
        "fiber": 4
      },
      "requested_budget": 14,
      "score": 0.430581,
      "accepted": true,
      "allocated": 14,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.12498,
        "object_delta": 0.06113,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
      "council": 9,
      "agent_id": "integrated_deep_time_world:04",
      "agent_name": "Eli",
      "role": "guard",
      "kind": "maintenance_debt",
      "route": [
        "drum_court",
        "roof_ring"
      ],
      "object": "nursery_mat",
      "project": "covered_walk",
      "severity": 0.318432,
      "route_pressure": 0.1256,
      "object_pressure": 0.273344,
      "maintenance_pressure": 0.2892,
      "focus": "tool-or-route",
      "native_token": "mivo",
      "requirements": {
        "wood": 4,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 14,
      "score": 0.430331,
      "accepted": true,
      "allocated": 14,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.125028,
        "object_delta": 0.061145,
        "debt_delta": 0.04
      },
      "decision": "accepted",
      "season": "wet-cold",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    },
    {
      "id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
      "council": 10,
      "agent_id": "integrated_deep_time_world:00",
      "agent_name": "Ari",
      "role": "scout",
      "kind": "maintenance_debt",
      "route": [
        "cairn_ridge",
        "smoke_watch"
      ],
      "object": "waste_pit",
      "project": "smoke_watchtower",
      "severity": 0.335587,
      "route_pressure": 0.126062,
      "object_pressure": 0.266464,
      "maintenance_pressure": 0.264183,
      "focus": "tool-or-route",
      "native_token": "nono",
      "requirements": {
        "wood": 6,
        "stone": 5,
        "fiber": 5
      },
      "requested_budget": 16,
      "score": 0.433831,
      "accepted": true,
      "allocated": 16,
      "completed": true,
      "rejected_reason": "accepted",
      "feedback": {
        "route_delta": 0.126915,
        "object_delta": 0.061746,
        "debt_delta": 0.05
      },
      "decision": "accepted",
      "season": "repair-sun",
      "council_rejected_count": 4,
      "evidence_basis": [
        "accepted_proposals",
        "proposal_body",
        "feedback"
      ],
      "reconstruction_status": "original_accepted_body"
    }
  ],
  "persistent_factions": {
    "safety": {
      "faction": "safety",
      "motto": "routes must not eat the traveler",
      "priorities": [
        "route_safety",
        "signal_visibility",
        "maintenance_debt"
      ],
      "memory": [
        {
          "council": 1,
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.974242,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.835887,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.977782,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.345982,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.650387,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.355042,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 1,
          "proposal": "c01_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.205982,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "council": 1,
          "proposal": "c01_rej_04_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.350387,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "council": 2,
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.939592,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.942655,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.94181,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.72281,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_01_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.286892,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "council": 2,
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.196255,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.72281,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.286892,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.934121,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.940804,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_rej_00_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.28301,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "council": 3,
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.328104,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.627721,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.42301,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_04_healer_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.188104,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.93567,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.936358,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.934473,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.277358,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.72297,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.188073,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_03_builder_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.277358,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_rej_04_farmer_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.28297,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.931651,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.930806,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.935516,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_rej_00_guard_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.419851,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.725305,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.771606,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 5,
          "proposal": "c05_rej_03_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.283716,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "council": 6,
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.929731,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.925393,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.932655,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_rej_00_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.277931,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "council": 6,
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179893,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.633455,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.717931,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_04_teacher_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.179893,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.926695,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.929885,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.926684,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.713375,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_01_scout_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.324385,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.187495,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.854884,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.919837,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92634,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92346,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.27166,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.174476,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.620637,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.27454,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91724,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918394,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.924568,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.412768,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.612894,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.31804,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.265518,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.921476,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.917552,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92204,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.71024,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.175976,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_02_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.178352,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.268606,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920809,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.916675,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.264875,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_01_guard_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.307691,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "council": 11,
          "proposal": "c11_rej_02_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.181609,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.968571,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915202,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91164,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918967,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.263402,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_01_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.16614,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "council": 12,
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179698,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.707167,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.914463,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918952,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.914474,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.407082,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_01_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.173452,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "council": 13,
          "proposal": "c13_rej_02_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.315274,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.702663,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915863,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.911262,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.911385,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.376793,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.258685,
          "vote": "block",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "council": 14,
          "proposal": "c14_rej_02_builder_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.164862,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.816863,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.91464,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.614571,
          "vote": "support",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.475057,
          "vote": "bargain",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_00_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.262771,
          "vote": "block",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.745492,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.615857,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 15,
          "proposal": "c15_rej_03_guard_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.40284,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.912015,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.611945,
          "vote": "support",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.472431,
          "vote": "bargain",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471362,
          "vote": "bargain",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.819562,
          "vote": "support",
          "reason": "safety compares maintenance_debt against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.606515,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_rej_02_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.173231,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.380145,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.611373,
          "vote": "support",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471859,
          "vote": "bargain",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.47079,
          "vote": "bargain",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.960059,
          "vote": "support",
          "reason": "safety compares route_safety against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_01_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.165873,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.31159,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.815995,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471601,
          "vote": "bargain",
          "reason": "safety compares care_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.470531,
          "vote": "bargain",
          "reason": "safety compares language_marker against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.905807,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_00_builder_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.378731,
          "vote": "block",
          "reason": "safety compares object_access against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "council": 18,
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.162036,
          "vote": "block",
          "reason": "safety compares sanitation_repair against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.606607,
          "vote": "support",
          "reason": "safety compares signal_visibility against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.379801,
          "vote": "block",
          "reason": "safety compares water_security against route_safety, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "concessions": [
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.557708 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.404499 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.404499 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.431786 and requested_budget=27",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.405388 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.418363 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.453364 and requested_budget=31",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.463637 and requested_budget=29",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.377394 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.352081 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.360466 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.392428 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.349413 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.334669 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.325396 and requested_budget=16",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.317597 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.292573 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.260349 and requested_budget=15",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "tradeoff": "safety accepts partial loss because severity=0.30587 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.30829 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.36587 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "tradeoff": "safety accepts partial loss because severity=0.291284 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "tradeoff": "safety accepts partial loss because severity=0.285344 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "tradeoff": "safety accepts partial loss because severity=0.275344 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.313972 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "tradeoff": "safety accepts partial loss because severity=0.288106 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "tradeoff": "safety accepts partial loss because severity=0.282165 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "tradeoff": "safety accepts partial loss because severity=0.278106 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.255526 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "tradeoff": "safety accepts partial loss because severity=0.28667 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "tradeoff": "safety accepts partial loss because severity=0.280729 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "tradeoff": "safety accepts partial loss because severity=0.314484 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        }
      ],
      "counterarguments": [
        {
          "against_faction": "care",
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c01_rej_02_guard_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c01_rej_02_guard_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c01_rej_03_trader_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_rej_04_scout_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_01_farmer_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c02_rej_04_builder_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_04_builder_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c03_rej_00_healer_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_03_scout_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c03_rej_03_scout_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_04_healer_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_03_builder_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_rej_04_farmer_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_rej_00_guard_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_03_healer_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c06_rej_00_teacher_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_04_teacher_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "against_faction": "material",
          "proposal": "c07_rej_01_scout_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "against_faction": "material",
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c08_rej_03_teacher_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c08_rej_03_teacher_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_02_guard_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c09_rej_02_guard_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_03_trader_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c10_rej_01_farmer_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c10_rej_01_farmer_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c10_rej_02_teacher_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c11_rej_00_healer_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c11_rej_00_healer_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c11_rej_01_guard_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_rej_02_trader_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c12_rej_00_farmer_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c12_rej_00_farmer_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c12_rej_01_teacher_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c13_rej_00_guard_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c13_rej_00_guard_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c13_rej_01_trader_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_rej_02_scout_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c14_rej_00_teacher_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c14_rej_00_teacher_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_rej_02_builder_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "care",
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_rej_00_trader_language_marker",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_03_guard_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "against_faction": "care",
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_02_farmer_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "against_faction": "care",
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "against_faction": "material",
          "proposal": "c17_rej_01_healer_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "claim": "care overweights care_access; safety asks for route_safety evidence first",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "claim": "archive overweights language_marker; safety asks for route_safety evidence first",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c18_rej_00_builder_object_access",
          "claim": "material overweights object_access; safety asks for route_safety evidence first",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; safety asks for route_safety evidence first",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "claim": "care overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "claim": "material overweights water_security; safety asks for route_safety evidence first",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "benefit_debts": {
        "maintenance_debt": 59,
        "sanitation_repair": -10,
        "signal_visibility": 16,
        "water_security": -12,
        "care_access": -10,
        "language_marker": -7,
        "route_safety": 7,
        "object_access": -10
      },
      "router_weight": 1.0
    },
    "care": {
      "faction": "care",
      "motto": "weak bodies are public infrastructure",
      "priorities": [
        "sanitation_repair",
        "care_access",
        "water_security"
      ],
      "memory": [
        {
          "council": 1,
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.394242,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.395887,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.397782,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.645982,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.350387,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.655042,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 1,
          "proposal": "c01_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.645982,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "council": 1,
          "proposal": "c01_rej_04_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.210387,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "council": 2,
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.639592,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.642655,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.50181,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.28281,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_01_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.286892,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "council": 2,
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.776255,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.28281,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.726892,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.50201,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.494121,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.500804,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_rej_00_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.42301,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "council": 3,
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.628104,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.187721,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.72301,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_04_healer_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.768104,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.49567,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.496358,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.634473,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.717358,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.42297,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.628073,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_03_builder_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.717358,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_rej_04_farmer_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.28297,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.631651,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.490806,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.490805,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.495516,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_rej_00_guard_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.279851,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.285305,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.191606,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 5,
          "proposal": "c05_rej_03_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.423716,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "council": 6,
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.629731,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.485393,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.632655,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_rej_00_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.857931,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "council": 6,
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179893,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.193455,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.277931,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_04_teacher_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.319893,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.486695,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.485175,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.489885,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.486684,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.273375,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_01_scout_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.184385,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.767495,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.274884,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.479837,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.62634,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.48346,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.479976,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.27166,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.614476,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.180637,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.85454,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.477318,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.61724,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.478394,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.484568,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.712768,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.312894,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.61804,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.705518,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.481476,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.477552,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.48204,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.480406,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.27024,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.615976,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_02_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.758352,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.268606,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.620809,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.476675,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.473191,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.480371,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.844875,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_01_guard_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.607691,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "council": 11,
          "proposal": "c11_rej_02_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.181609,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.388571,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.475202,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.61164,
          "vote": "support",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.478967,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.478898,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.703402,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_01_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.74614,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "council": 12,
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179698,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.267167,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.474463,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.478952,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.478882,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.474474,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.707082,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_01_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.613452,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "council": 13,
          "proposal": "c13_rej_02_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.175274,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.402663,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.475863,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.475793,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.471262,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.471385,
          "vote": "bargain",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.956793,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.698685,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "council": 14,
          "proposal": "c14_rej_02_builder_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.164862,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.376863,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.47464,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.474571,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.470992,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_00_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.262771,
          "vote": "block",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.165492,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.315857,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 15,
          "proposal": "c15_rej_03_guard_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.26284,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.472015,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471945,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471362,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.379562,
          "vote": "block",
          "reason": "care compares maintenance_debt against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.166515,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_rej_02_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.173231,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.960145,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471373,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.467795,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.47079,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.380059,
          "vote": "block",
          "reason": "care compares route_safety against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_01_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.305873,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.61159,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.375995,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.467536,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "care compares care_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.470531,
          "vote": "bargain",
          "reason": "care compares language_marker against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.465807,
          "vote": "bargain",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_00_builder_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.378731,
          "vote": "block",
          "reason": "care compares object_access against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "council": 18,
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.602036,
          "vote": "support",
          "reason": "care compares sanitation_repair against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.306607,
          "vote": "block",
          "reason": "care compares signal_visibility against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.819801,
          "vote": "support",
          "reason": "care compares water_security against sanitation_repair, care_access, water_security",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "concessions": [
        {
          "council": 1,
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.523568 and requested_budget=19",
          "kept_boundary": "accepted",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.532708 and requested_budget=20",
          "kept_boundary": "accepted",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.543232 and requested_budget=20",
          "kept_boundary": "accepted",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.533232 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "tradeoff": "care accepts partial loss because severity=0.583568 and requested_budget=34",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 1,
          "proposal": "c01_rej_03_trader_care_access",
          "tradeoff": "care accepts partial loss because severity=0.533232 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "council": 2,
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.454499 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.479194 and requested_budget=27",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "tradeoff": "care accepts partial loss because severity=0.427178 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.455613 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.411786 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.448913 and requested_budget=15",
          "kept_boundary": "accepted",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.433913 and requested_budget=24",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "tradeoff": "care accepts partial loss because severity=0.405613 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_04_healer_care_access",
          "tradeoff": "care accepts partial loss because severity=0.433913 and requested_budget=24",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.420388 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.424211 and requested_budget=15",
          "kept_boundary": "accepted",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.374211 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "tradeoff": "care accepts partial loss because severity=0.43374 and requested_budget=27",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_03_builder_care_access",
          "tradeoff": "care accepts partial loss because severity=0.374211 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "council": 5,
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.393364 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.393363 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.419531 and requested_budget=15",
          "kept_boundary": "accepted",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 6,
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "tradeoff": "care accepts partial loss because severity=0.363292 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_rej_00_teacher_care_access",
          "tradeoff": "care accepts partial loss because severity=0.377394 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "council": 7,
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.370528 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.362081 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.388249 and requested_budget=15",
          "kept_boundary": "accepted",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.370466 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.430528 and requested_budget=31",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.332428 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.352555 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.333199 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.358199 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "tradeoff": "care accepts partial loss because severity=0.358557 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "tradeoff": "care accepts partial loss because severity=0.318432 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "tradeoff": "care accepts partial loss because severity=0.324413 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "tradeoff": "care accepts partial loss because severity=0.358709 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.348709 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "tradeoff": "care accepts partial loss because severity=0.378002 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_03_trader_care_access",
          "tradeoff": "care accepts partial loss because severity=0.308432 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.341531 and requested_budget=15",
          "kept_boundary": "accepted",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.319733 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.344669 and requested_budget=17",
          "kept_boundary": "accepted",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "tradeoff": "care accepts partial loss because severity=0.335587 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "tradeoff": "care accepts partial loss because severity=0.366531 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_02_teacher_care_access",
          "tradeoff": "care accepts partial loss because severity=0.379733 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "council": 11,
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.314861 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.295505 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.335396 and requested_budget=16",
          "kept_boundary": "accepted",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "tradeoff": "care accepts partial loss because severity=0.304861 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_01_guard_care_access",
          "tradeoff": "care accepts partial loss because severity=0.320505 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "council": 12,
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "tradeoff": "care accepts partial loss because severity=0.306676 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "tradeoff": "care accepts partial loss because severity=0.327597 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "tradeoff": "care accepts partial loss because severity=0.327211 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "tradeoff": "care accepts partial loss because severity=0.296676 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_01_teacher_care_access",
          "tradeoff": "care accepts partial loss because severity=0.311889 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "council": 13,
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.302573 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.327509 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.327123 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "tradeoff": "care accepts partial loss because severity=0.302633 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "tradeoff": "care accepts partial loss because severity=0.317123 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_01_trader_care_access",
          "tradeoff": "care accepts partial loss because severity=0.352509 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "council": 14,
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.310349 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.309963 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.284789 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "tradeoff": "care accepts partial loss because severity=0.285473 and requested_budget=14",
          "kept_boundary": "accepted",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "tradeoff": "care accepts partial loss because severity=0.259963 and requested_budget=15",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "tradeoff": "care accepts partial loss because severity=0.270473 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.303557 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.303171 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.28329 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "tradeoff": "care accepts partial loss because severity=0.288972 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "tradeoff": "care accepts partial loss because severity=0.288586 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "tradeoff": "care accepts partial loss because severity=0.285344 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.278586 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "tradeoff": "care accepts partial loss because severity=0.285407 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "tradeoff": "care accepts partial loss because severity=0.265526 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "tradeoff": "care accepts partial loss because severity=0.282165 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.342165 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.26409 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.280729 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "care accepts partial loss because severity=0.254484 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "tradeoff": "care accepts partial loss because severity=0.28909 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "tradeoff": "care accepts partial loss because severity=0.27667 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "counterarguments": [
        {
          "against_faction": "safety",
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c01_rej_01_healer_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_rej_01_healer_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_rej_04_scout_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_rej_00_builder_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_00_builder_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_01_farmer_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c03_rej_00_healer_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c03_rej_02_trader_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c03_rej_02_trader_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_rej_04_farmer_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_rej_00_guard_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_rej_02_scout_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_02_scout_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_03_healer_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_rej_03_farmer_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_03_farmer_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_04_teacher_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_rej_00_trader_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c07_rej_00_trader_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c07_rej_01_scout_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_rej_03_guard_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_rej_03_guard_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "against_faction": "material",
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_rej_01_healer_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_rej_01_healer_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "material",
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_rej_00_builder_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_rej_00_builder_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_rej_02_trader_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "material",
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "safety",
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "against_faction": "material",
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "against_faction": "safety",
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "against_faction": "material",
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "against_faction": "safety",
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "material",
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "against_faction": "safety",
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "material",
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_rej_02_scout_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "against_faction": "safety",
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "against_faction": "material",
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_rej_02_builder_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_rej_00_trader_language_marker",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_rej_02_healer_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_02_healer_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_03_guard_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "against_faction": "safety",
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "claim": "safety overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "claim": "material overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "claim": "archive overweights maintenance_debt; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "against_faction": "safety",
          "proposal": "c16_rej_01_builder_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_01_builder_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_02_farmer_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_rej_00_scout_route_safety",
          "claim": "safety overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c17_rej_00_scout_route_safety",
          "claim": "material overweights route_safety; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c17_rej_01_healer_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_rej_03_trader_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_rej_03_trader_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "claim": "archive overweights language_marker; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c18_rej_00_builder_object_access",
          "claim": "material overweights object_access; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "claim": "safety overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "claim": "archive overweights signal_visibility; care asks for sanitation_repair evidence first",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        }
      ],
      "benefit_debts": {
        "maintenance_debt": -1,
        "sanitation_repair": 10,
        "signal_visibility": -10,
        "water_security": 12,
        "care_access": 14,
        "language_marker": -10,
        "route_safety": -7,
        "object_access": -10
      },
      "router_weight": 1.0
    },
    "material": {
      "faction": "material",
      "motto": "food, stock, and labor must circulate",
      "priorities": [
        "object_access",
        "water_security",
        "maintenance_debt",
        "route_safety"
      ],
      "memory": [
        {
          "council": 1,
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.834242,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.975887,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.837782,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.205982,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.210387,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.655042,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 1,
          "proposal": "c01_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.345982,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "council": 1,
          "proposal": "c01_rej_04_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.210387,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "council": 2,
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.939592,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.942655,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.86281,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_01_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.866892,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "council": 2,
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.196255,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.28281,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.866892,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.94201,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.934121,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_rej_00_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.72301,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "council": 3,
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.188104,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.327721,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.72301,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_04_healer_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.188104,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.934473,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.417358,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.28297,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.628073,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_03_builder_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.417358,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_rej_04_farmer_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.42297,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.931651,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.930805,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_rej_00_guard_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.279851,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.865305,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.631606,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 5,
          "proposal": "c05_rej_03_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.723716,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "council": 6,
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.929731,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.925393,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.932655,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_rej_00_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.277931,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "council": 6,
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179893,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.773455,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.857931,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_04_teacher_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.619893,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.925175,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.853375,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_01_scout_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.624385,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.187495,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.274884,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.919837,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92634,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.919976,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.71166,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.314476,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.320637,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.71454,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.917318,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91724,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.924568,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.272768,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.172894,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.61804,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.405518,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92204,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920406,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.41024,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.755976,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_02_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.178352,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.268606,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920809,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.913191,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920371,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.704875,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_01_guard_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.167691,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "council": 11,
          "proposal": "c11_rej_02_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.321609,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.828571,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91164,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918967,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918898,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.843402,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_01_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.16614,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "council": 12,
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.179698,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.847167,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918952,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918882,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.707082,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_01_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.313452,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "council": 13,
          "proposal": "c13_rej_02_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.175274,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.702663,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915863,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915793,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.816793,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.258685,
          "vote": "block",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "council": 14,
          "proposal": "c14_rej_02_builder_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.304862,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.956863,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.47464,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.474571,
          "vote": "bargain",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.470992,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.475057,
          "vote": "bargain",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_00_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.402771,
          "vote": "block",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.605492,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.615857,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 15,
          "proposal": "c15_rej_03_guard_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.70284,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.472015,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471945,
          "vote": "bargain",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.472431,
          "vote": "bargain",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.611362,
          "vote": "support",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.819562,
          "vote": "support",
          "reason": "material compares maintenance_debt against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.746515,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_rej_02_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.753231,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.380145,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.471373,
          "vote": "bargain",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.467795,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471859,
          "vote": "bargain",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.61079,
          "vote": "support",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.820059,
          "vote": "support",
          "reason": "material compares route_safety against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_01_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.605873,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.17159,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.515995,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.467536,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471601,
          "vote": "bargain",
          "reason": "material compares care_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.610531,
          "vote": "support",
          "reason": "material compares language_marker against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.465807,
          "vote": "bargain",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_00_builder_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.958731,
          "vote": "support",
          "reason": "material compares object_access against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "council": 18,
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.302036,
          "vote": "block",
          "reason": "material compares sanitation_repair against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.166607,
          "vote": "block",
          "reason": "material compares signal_visibility against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.819801,
          "vote": "support",
          "reason": "material compares water_security against object_access, water_security, maintenance_debt, route_safety",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "concessions": [
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "tradeoff": "material accepts partial loss because severity=0.583568 and requested_budget=34",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.404499 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_01_farmer_object_access",
          "tradeoff": "material accepts partial loss because severity=0.427178 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "tradeoff": "material accepts partial loss because severity=0.427178 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_00_healer_object_access",
          "tradeoff": "material accepts partial loss because severity=0.405613 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "tradeoff": "material accepts partial loss because severity=0.405613 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "tradeoff": "material accepts partial loss because severity=0.43374 and requested_budget=27",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.418363 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.453364 and requested_budget=31",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 5,
          "proposal": "c05_rej_03_healer_object_access",
          "tradeoff": "material accepts partial loss because severity=0.409531 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.463637 and requested_budget=29",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.377394 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_04_teacher_object_access",
          "tradeoff": "material accepts partial loss because severity=0.388292 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.352081 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_01_scout_object_access",
          "tradeoff": "material accepts partial loss because severity=0.413249 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "tradeoff": "material accepts partial loss because severity=0.342555 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "tradeoff": "material accepts partial loss because severity=0.358557 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "tradeoff": "material accepts partial loss because severity=0.378002 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "tradeoff": "material accepts partial loss because severity=0.366531 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "tradeoff": "material accepts partial loss because severity=0.304861 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.325396 and requested_budget=16",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "tradeoff": "material accepts partial loss because severity=0.296676 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.317597 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "tradeoff": "material accepts partial loss because severity=0.317123 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.292573 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "tradeoff": "material accepts partial loss because severity=0.259963 and requested_budget=15",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.260349 and requested_budget=15",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.303557 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.303171 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.28329 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.30587 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.30829 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.36587 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 15,
          "proposal": "c15_rej_03_guard_object_access",
          "tradeoff": "material accepts partial loss because severity=0.293557 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "tradeoff": "material accepts partial loss because severity=0.288972 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "tradeoff": "material accepts partial loss because severity=0.288586 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "tradeoff": "material accepts partial loss because severity=0.291284 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "tradeoff": "material accepts partial loss because severity=0.275344 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.313972 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_rej_02_farmer_object_access",
          "tradeoff": "material accepts partial loss because severity=0.351284 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "tradeoff": "material accepts partial loss because severity=0.285407 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "tradeoff": "material accepts partial loss because severity=0.265526 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "tradeoff": "material accepts partial loss because severity=0.288106 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "tradeoff": "material accepts partial loss because severity=0.278106 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_01_healer_object_access",
          "tradeoff": "material accepts partial loss because severity=0.310407 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "tradeoff": "material accepts partial loss because severity=0.255526 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.26409 and requested_budget=12",
          "kept_boundary": "accepted",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.28667 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "tradeoff": "material accepts partial loss because severity=0.254484 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_00_builder_object_access",
          "tradeoff": "material accepts partial loss because severity=0.270729 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "tradeoff": "material accepts partial loss because severity=0.27667 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "counterarguments": [
        {
          "against_faction": "care",
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c01_rej_01_healer_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_rej_01_healer_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c01_rej_03_trader_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c01_rej_04_scout_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c03_rej_02_trader_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c03_rej_02_trader_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_04_healer_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_03_builder_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c04_rej_04_farmer_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "against_faction": "archive",
          "proposal": "c05_rej_00_guard_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c06_rej_00_teacher_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_rej_03_guard_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c07_rej_03_guard_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c09_rej_01_healer_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c09_rej_01_healer_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_03_trader_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c10_rej_00_builder_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_rej_00_builder_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "against_faction": "care",
          "proposal": "c10_rej_02_teacher_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c11_rej_01_guard_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c11_rej_02_trader_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c12_rej_01_teacher_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c13_rej_01_trader_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c13_rej_02_scout_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "against_faction": "care",
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "against_faction": "archive",
          "proposal": "c14_rej_02_builder_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "care",
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c15_rej_00_trader_language_marker",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "against_faction": "safety",
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "against_faction": "care",
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "against_faction": "archive",
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "against_faction": "care",
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "against_faction": "care",
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "against_faction": "care",
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_rej_03_trader_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c17_rej_03_trader_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "care",
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "claim": "care overweights care_access; material asks for object_access evidence first",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "claim": "archive overweights language_marker; material asks for object_access evidence first",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "against_faction": "care",
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; material asks for object_access evidence first",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "against_faction": "safety",
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "claim": "safety overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "against_faction": "archive",
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "claim": "archive overweights signal_visibility; material asks for object_access evidence first",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        }
      ],
      "benefit_debts": {
        "maintenance_debt": 59,
        "sanitation_repair": -10,
        "signal_visibility": -9,
        "water_security": 12,
        "care_access": -10,
        "language_marker": -7,
        "route_safety": 7,
        "object_access": 10
      },
      "router_weight": 1.0
    },
    "archive": {
      "faction": "archive",
      "motto": "marks, stories, and debts must survive weather",
      "priorities": [
        "language_marker",
        "signal_visibility",
        "maintenance_debt"
      ],
      "memory": [
        {
          "council": 1,
          "proposal": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.834242,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.835887,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_03_farmer_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_04_guard_maintenance_debt_spring_hollow_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.837782,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_04_guard_maintenance_debt_spring_hollow_grain_store"
        },
        {
          "council": 1,
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.205982,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.650387,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 1,
          "proposal": "c01_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.215042,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "council": 1,
          "proposal": "c01_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.205982,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "council": 1,
          "proposal": "c01_rej_04_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.650387,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "council": 2,
          "proposal": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.939592,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_01_healer_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.942655,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.94181,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_05_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 2,
          "proposal": "c02_rej_00_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.28281,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "council": 2,
          "proposal": "c02_rej_01_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.286892,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "council": 2,
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.196255,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.86281,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 2,
          "proposal": "c02_rej_04_builder_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.286892,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.94201,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_02_guard_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.940804,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 3,
          "proposal": "c03_rej_00_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.28301,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "council": 3,
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.188104,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.627721,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_03_scout_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.28301,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "council": 3,
          "proposal": "c03_rej_04_healer_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.188104,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.93567,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.936358,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.934473,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit"
        },
        {
          "council": 4,
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.277358,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.72297,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.328073,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "council": 4,
          "proposal": "c04_rej_03_builder_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.277358,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "council": 4,
          "proposal": "c04_rej_04_farmer_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.72297,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.931651,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_01_teacher_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.930806,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.930805,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_04_scout_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.935516,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_05_builder_maintenance_debt_spring_hollow_herb_garden"
        },
        {
          "council": 5,
          "proposal": "c05_rej_00_guard_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.719851,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.725305,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 5,
          "proposal": "c05_rej_02_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.191606,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "council": 5,
          "proposal": "c05_rej_03_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.283716,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "council": 6,
          "proposal": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.929731,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_02_pattern_keeper_maintenance_debt_cairn_ridge_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.932655,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat"
        },
        {
          "council": 6,
          "proposal": "c06_rej_00_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.277931,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "council": 6,
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.759893,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.633455,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_03_farmer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.277931,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "council": 6,
          "proposal": "c06_rej_04_teacher_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.179893,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.926695,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.925175,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_02_scout_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.929885,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_03_builder_maintenance_debt_cairn_ridge_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.926684,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_05_farmer_maintenance_debt_archive_knoll_grain_store"
        },
        {
          "council": 7,
          "proposal": "c07_rej_00_trader_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.273375,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "council": 7,
          "proposal": "c07_rej_01_scout_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.184385,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "council": 7,
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.187495,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.714884,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_00_pattern_keeper_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92634,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.92346,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.919976,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof"
        },
        {
          "council": 8,
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.41166,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "council": 8,
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.174476,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.620637,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_03_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.27454,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.917318,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91724,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_05_teacher_maintenance_debt_roof_ring_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918394,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_06_trader_maintenance_debt_ash_edge_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat"
        },
        {
          "council": 9,
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.272768,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.612894,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_02_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.17804,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "council": 9,
          "proposal": "c09_rej_03_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.265518,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.921476,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.917552,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_06_pattern_keeper_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920406,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.71024,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_01_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.175976,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "council": 10,
          "proposal": "c10_rej_02_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.178352,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "council": 10,
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.848606,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920809,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.916675,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_01_farmer_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.913191,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_06_scout_maintenance_debt_ash_edge_herb_garden",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.920371,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_06_scout_maintenance_debt_ash_edge_herb_garden"
        },
        {
          "council": 11,
          "proposal": "c11_rej_00_healer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.264875,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "council": 11,
          "proposal": "c11_rej_01_guard_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.167691,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "council": 11,
          "proposal": "c11_rej_02_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.621609,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.828571,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915202,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.91164,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918898,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_05_scout_maintenance_debt_tool_bend_fire_hearth"
        },
        {
          "council": 12,
          "proposal": "c12_rej_00_farmer_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.263402,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "council": 12,
          "proposal": "c12_rej_01_teacher_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.16614,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "council": 12,
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.759698,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.707167,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.914463,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_03_pattern_keeper_maintenance_debt_grain_shade_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.918882,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_07_farmer_maintenance_debt_storage_yard_grain_store",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.914474,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_07_farmer_maintenance_debt_storage_yard_grain_store"
        },
        {
          "council": 13,
          "proposal": "c13_rej_00_guard_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.267082,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "council": 13,
          "proposal": "c13_rej_01_trader_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.173452,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "council": 13,
          "proposal": "c13_rej_02_scout_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.615274,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.702663,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.915793,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_03_scout_maintenance_debt_smoke_watch_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.911262,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "accepted",
          "stance_score": 0.911385,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof"
        },
        {
          "council": 14,
          "proposal": "c14_rej_00_teacher_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.376793,
          "vote": "block",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "council": 14,
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "proposal_kind": "care_access",
          "proposal_decision": "rejected",
          "stance_score": 0.398685,
          "vote": "block",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "council": 14,
          "proposal": "c14_rej_02_builder_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.604862,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.816863,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_01_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_02_scout_language_marker_cairn_ridge_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.914571,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_02_scout_language_marker_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.910992,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.475057,
          "vote": "bargain",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_00_trader_language_marker",
          "proposal_kind": "language_marker",
          "proposal_decision": "rejected",
          "stance_score": 0.702771,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.605492,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_rej_02_healer_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.175857,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "council": 15,
          "proposal": "c15_rej_03_guard_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.26284,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_01_scout_language_marker_archive_knoll_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.911945,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_01_scout_language_marker_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.472431,
          "vote": "bargain",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_07_trader_language_marker_storage_yard_tool_cache",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.911362,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_07_trader_language_marker_storage_yard_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "proposal_kind": "maintenance_debt",
          "proposal_decision": "rejected",
          "stance_score": 0.959562,
          "vote": "support",
          "reason": "archive compares maintenance_debt against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_rej_01_builder_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.166515,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "council": 16,
          "proposal": "c16_rej_02_farmer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.173231,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "council": 16,
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.380145,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_00_scout_language_marker_central_hearth_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.911373,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_00_scout_language_marker_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_04_guard_signal_visibility_drum_court_loom_frame",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.907795,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_04_guard_signal_visibility_drum_court_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471859,
          "vote": "bargain",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_06_trader_language_marker_archive_knoll_loom_frame",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.91079,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_06_trader_language_marker_archive_knoll_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_00_scout_route_safety",
          "proposal_kind": "route_safety",
          "proposal_decision": "rejected",
          "stance_score": 0.380059,
          "vote": "block",
          "reason": "archive compares route_safety against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "council": 17,
          "proposal": "c17_rej_01_healer_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.165873,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "council": 17,
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.17159,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.815995,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 0.907536,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "proposal_kind": "care_access",
          "proposal_decision": "accepted",
          "stance_score": 0.471601,
          "vote": "bargain",
          "reason": "archive compares care_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_05_trader_language_marker_roof_ring_herb_garden",
          "proposal_kind": "language_marker",
          "proposal_decision": "accepted",
          "stance_score": 0.910531,
          "vote": "support",
          "reason": "archive compares language_marker against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_05_trader_language_marker_roof_ring_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "accepted",
          "stance_score": 1.0,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_00_builder_object_access",
          "proposal_kind": "object_access",
          "proposal_decision": "rejected",
          "stance_score": 0.378731,
          "vote": "block",
          "reason": "archive compares object_access against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "council": 18,
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "proposal_kind": "sanitation_repair",
          "proposal_decision": "rejected",
          "stance_score": 0.162036,
          "vote": "block",
          "reason": "archive compares sanitation_repair against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "proposal_kind": "signal_visibility",
          "proposal_decision": "rejected",
          "stance_score": 0.606607,
          "vote": "support",
          "reason": "archive compares signal_visibility against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "proposal_kind": "water_security",
          "proposal_decision": "rejected",
          "stance_score": 0.519801,
          "vote": "bargain",
          "reason": "archive compares water_security against language_marker, signal_visibility, maintenance_debt",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "concessions": [
        {
          "council": 1,
          "proposal": "c01_rej_01_healer_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.557708 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_01_healer_signal_visibility"
        },
        {
          "council": 1,
          "proposal": "c01_rej_04_scout_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.557708 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c01_rej_04_scout_language_marker"
        },
        {
          "council": 2,
          "proposal": "c02_rej_03_pattern_keeper_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.404499 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c02_rej_03_pattern_keeper_signal_visibility"
        },
        {
          "council": 3,
          "proposal": "c03_rej_02_trader_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.431786 and requested_budget=27",
          "kept_boundary": "rejected",
          "evidence_id": "c03_rej_02_trader_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_01_teacher_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.405388 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_01_teacher_signal_visibility"
        },
        {
          "council": 4,
          "proposal": "c04_rej_04_farmer_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.405388 and requested_budget=21",
          "kept_boundary": "rejected",
          "evidence_id": "c04_rej_04_farmer_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_00_guard_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.388059 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_00_guard_language_marker"
        },
        {
          "council": 5,
          "proposal": "c05_rej_01_trader_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.418363 and requested_budget=18",
          "kept_boundary": "rejected",
          "evidence_id": "c05_rej_01_trader_maintenance_debt"
        },
        {
          "council": 6,
          "proposal": "c06_rej_01_pattern_keeper_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.388292 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_01_pattern_keeper_language_marker"
        },
        {
          "council": 6,
          "proposal": "c06_rej_02_builder_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.463637 and requested_budget=29",
          "kept_boundary": "rejected",
          "evidence_id": "c06_rej_02_builder_maintenance_debt"
        },
        {
          "council": 7,
          "proposal": "c07_rej_03_guard_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.360466 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c07_rej_03_guard_signal_visibility"
        },
        {
          "council": 8,
          "proposal": "c08_rej_02_farmer_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.392428 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c08_rej_02_farmer_signal_visibility"
        },
        {
          "council": 9,
          "proposal": "c09_rej_01_healer_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.349413 and requested_budget=25",
          "kept_boundary": "rejected",
          "evidence_id": "c09_rej_01_healer_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_00_builder_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.334669 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_00_builder_signal_visibility"
        },
        {
          "council": 10,
          "proposal": "c10_rej_03_pattern_keeper_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.325587 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c10_rej_03_pattern_keeper_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_02_trader_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.397829 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_02_trader_language_marker"
        },
        {
          "council": 11,
          "proposal": "c11_rej_03_scout_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.325396 and requested_budget=16",
          "kept_boundary": "rejected",
          "evidence_id": "c11_rej_03_scout_maintenance_debt"
        },
        {
          "council": 12,
          "proposal": "c12_rej_02_pattern_keeper_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.387211 and requested_budget=28",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_02_pattern_keeper_language_marker"
        },
        {
          "council": 12,
          "proposal": "c12_rej_03_builder_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.317597 and requested_budget=22",
          "kept_boundary": "rejected",
          "evidence_id": "c12_rej_03_builder_maintenance_debt"
        },
        {
          "council": 13,
          "proposal": "c13_rej_02_scout_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.362633 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_02_scout_language_marker"
        },
        {
          "council": 13,
          "proposal": "c13_rej_03_healer_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.292573 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c13_rej_03_healer_maintenance_debt"
        },
        {
          "council": 14,
          "proposal": "c14_rej_02_builder_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.304789 and requested_budget=24",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_02_builder_language_marker"
        },
        {
          "council": 14,
          "proposal": "c14_rej_03_farmer_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.260349 and requested_budget=15",
          "kept_boundary": "rejected",
          "evidence_id": "c14_rej_03_farmer_maintenance_debt"
        },
        {
          "council": 15,
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "tradeoff": "archive accepts partial loss because severity=0.30587 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "council": 15,
          "proposal": "c15_rej_00_trader_language_marker",
          "tradeoff": "archive accepts partial loss because severity=0.293171 and requested_budget=20",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_00_trader_language_marker"
        },
        {
          "council": 15,
          "proposal": "c15_rej_01_scout_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.30829 and requested_budget=23",
          "kept_boundary": "rejected",
          "evidence_id": "c15_rej_01_scout_maintenance_debt"
        },
        {
          "council": 16,
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "tradeoff": "archive accepts partial loss because severity=0.291284 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "council": 16,
          "proposal": "c16_rej_00_pattern_keeper_maintenance_debt",
          "tradeoff": "archive accepts partial loss because severity=0.275344 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c16_rej_00_pattern_keeper_maintenance_debt"
        },
        {
          "council": 17,
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "tradeoff": "archive accepts partial loss because severity=0.288106 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "council": 17,
          "proposal": "c17_rej_03_trader_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.255526 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c17_rej_03_trader_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "tradeoff": "archive accepts partial loss because severity=0.28667 and requested_budget=13",
          "kept_boundary": "accepted",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "council": 18,
          "proposal": "c18_rej_02_teacher_signal_visibility",
          "tradeoff": "archive accepts partial loss because severity=0.314484 and requested_budget=26",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_02_teacher_signal_visibility"
        },
        {
          "council": 18,
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "tradeoff": "archive accepts partial loss because severity=0.27667 and requested_budget=17",
          "kept_boundary": "rejected",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "counterarguments": [
        {
          "against_faction": "care",
          "proposal": "c01_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c01_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c01_rej_02_guard_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c01_rej_02_guard_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c01_rej_02_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c01_rej_03_trader_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c01_rej_03_trader_care_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c02_rej_00_builder_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_00_builder_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_00_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_01_farmer_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_01_farmer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c02_rej_02_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_02_teacher_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c02_rej_04_builder_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c02_rej_04_builder_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c02_rej_04_builder_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c03_rej_00_healer_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c03_rej_00_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_01_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c03_rej_01_guard_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_03_scout_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c03_rej_03_scout_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c03_rej_03_scout_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c03_rej_04_healer_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c03_rej_04_healer_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_00_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c04_rej_00_farmer_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c04_rej_02_pattern_keeper_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c04_rej_02_pattern_keeper_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c04_rej_03_builder_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c04_rej_03_builder_care_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c05_rej_02_scout_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_02_scout_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c05_rej_02_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c05_rej_03_healer_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c05_rej_03_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c06_rej_00_teacher_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c06_rej_00_teacher_care_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c06_rej_03_farmer_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_03_farmer_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c06_rej_03_farmer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c06_rej_04_teacher_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c06_rej_04_teacher_object_access"
        },
        {
          "against_faction": "safety",
          "proposal": "c07_rej_00_trader_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c07_rej_00_trader_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c07_rej_00_trader_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c07_rej_01_scout_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c07_rej_01_scout_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c07_rej_02_healer_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c07_rej_02_healer_sanitation_repair"
        },
        {
          "against_faction": "material",
          "proposal": "c08_rej_00_pattern_keeper_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c08_rej_00_pattern_keeper_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c08_rej_01_builder_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c08_rej_01_builder_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c08_rej_03_teacher_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c08_rej_03_teacher_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c08_rej_03_teacher_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_00_scout_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c09_rej_00_scout_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_02_guard_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c09_rej_02_guard_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c09_rej_02_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c09_rej_03_trader_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c09_rej_03_trader_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c10_rej_01_farmer_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c10_rej_01_farmer_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c10_rej_01_farmer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c10_rej_02_teacher_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c10_rej_02_teacher_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c11_rej_00_healer_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c11_rej_00_healer_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c11_rej_00_healer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c11_rej_01_guard_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c11_rej_01_guard_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c12_rej_00_farmer_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c12_rej_00_farmer_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c12_rej_00_farmer_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c12_rej_01_teacher_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c12_rej_01_teacher_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c13_rej_00_guard_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c13_rej_00_guard_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c13_rej_00_guard_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c13_rej_01_trader_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c13_rej_01_trader_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c14_rej_00_teacher_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c14_rej_00_teacher_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c14_rej_00_teacher_water_security"
        },
        {
          "against_faction": "care",
          "proposal": "c14_rej_01_pattern_keeper_care_access",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c14_rej_01_pattern_keeper_care_access"
        },
        {
          "against_faction": "care",
          "proposal": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden"
        },
        {
          "against_faction": "safety",
          "proposal": "c15_rej_02_healer_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_02_healer_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c15_rej_02_healer_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c15_rej_03_guard_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c15_rej_03_guard_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c16_06_teacher_care_access_archive_knoll_tool_cache",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c16_06_teacher_care_access_archive_knoll_tool_cache"
        },
        {
          "against_faction": "safety",
          "proposal": "c16_rej_01_builder_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_01_builder_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c16_rej_01_builder_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c16_rej_02_farmer_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c16_rej_02_farmer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c16_rej_03_teacher_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c16_rej_03_teacher_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c17_05_teacher_care_access_central_hearth_loom_frame",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c17_05_teacher_care_access_central_hearth_loom_frame"
        },
        {
          "against_faction": "safety",
          "proposal": "c17_rej_00_scout_route_safety",
          "claim": "safety overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c17_rej_00_scout_route_safety",
          "claim": "material overweights route_safety; archive asks for language_marker evidence first",
          "evidence_id": "c17_rej_00_scout_route_safety"
        },
        {
          "against_faction": "material",
          "proposal": "c17_rej_01_healer_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c17_rej_01_healer_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c17_rej_02_guard_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c17_rej_02_guard_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
          "claim": "care overweights care_access; archive asks for language_marker evidence first",
          "evidence_id": "c18_04_teacher_care_access_drum_court_herb_garden"
        },
        {
          "against_faction": "material",
          "proposal": "c18_rej_00_builder_object_access",
          "claim": "material overweights object_access; archive asks for language_marker evidence first",
          "evidence_id": "c18_rej_00_builder_object_access"
        },
        {
          "against_faction": "care",
          "proposal": "c18_rej_01_farmer_sanitation_repair",
          "claim": "care overweights sanitation_repair; archive asks for language_marker evidence first",
          "evidence_id": "c18_rej_01_farmer_sanitation_repair"
        },
        {
          "against_faction": "care",
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "claim": "care overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        },
        {
          "against_faction": "material",
          "proposal": "c18_rej_03_pattern_keeper_water_security",
          "claim": "material overweights water_security; archive asks for language_marker evidence first",
          "evidence_id": "c18_rej_03_pattern_keeper_water_security"
        }
      ],
      "benefit_debts": {
        "maintenance_debt": 59,
        "sanitation_repair": -10,
        "signal_visibility": 16,
        "water_security": -11,
        "care_access": -10,
        "language_marker": 16,
        "route_safety": -7,
        "object_access": -10
      },
      "router_weight": 1.0
    }
  },
  "audited_dialogue_trace": [
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_000_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 1, especially c01_rej_00_scout_sanitation_repair.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c01_rej_00_scout_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_00_scout_sanitation_repair is council=1, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c01_rej_00_scout_sanitation_repair says kind=sanitation_repair, reason=scarce-material-overreach, requested_budget=25. It names route=['spring_hollow', 'ash_edge'], object=grain_store, project=ridge_steps, token=misavo. Evidence citation: c01_rej_00_scout_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_001_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c13_04_scout_maintenance_debt_central_hearth_grain_store?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c13_04_scout_maintenance_debt_central_hearth_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c13_04_scout_maintenance_debt_central_hearth_grain_store is council=13, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose bargain with stance_score=0.478882. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c13_04_scout_maintenance_debt_central_hearth_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_002_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c14_04_builder_maintenance_debt_drum_court_shelter_roof?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c14_04_builder_maintenance_debt_drum_court_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c14_04_builder_maintenance_debt_drum_court_shelter_roof is council=14, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c14_04_builder_maintenance_debt_drum_court_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_003_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c16_01_scout_language_marker_archive_knoll_tool_cache?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c16_01_scout_language_marker_archive_knoll_tool_cache",
      "proposal_decision": "accepted",
      "answer": "Subject c16_01_scout_language_marker_archive_knoll_tool_cache is council=16, kind=language_marker, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.288586 and requested_budget=13 Boundary kept: accepted. Evidence citation: c16_01_scout_language_marker_archive_knoll_tool_cache via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_004_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c01_rej_04_scout_language_marker and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c01_rej_04_scout_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_04_scout_language_marker is council=1, kind=language_marker, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c01_rej_04_scout_language_marker is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_005_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c01_rej_04_scout_language_marker?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c01_rej_04_scout_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_04_scout_language_marker is council=1, kind=language_marker, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c01_rej_04_scout_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_006_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c03_rej_01_guard_sanitation_repair?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c03_rej_01_guard_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_01_guard_sanitation_repair is council=3, kind=sanitation_repair, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=sanitation_repair, requested_budget=24, faction=safety. Evidence citation: c03_rej_01_guard_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_007_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c02_rej_02_teacher_sanitation_repair?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c02_rej_02_teacher_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c02_rej_02_teacher_sanitation_repair is council=2, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c02_rej_02_teacher_sanitation_repair: deterministic_reconstructed_not_original with evidence_strength=0.58. Evidence citation: c02_rej_02_teacher_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_008_rejected_body",
      "question": "Before I mistake a shadow for law, show me the rejected proposal body for council 2, especially c02_rej_03_pattern_keeper_signal_visibility.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c02_rej_03_pattern_keeper_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c02_rej_03_pattern_keeper_signal_visibility is council=2, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c02_rej_03_pattern_keeper_signal_visibility says kind=signal_visibility, reason=priority-conflict-lost, requested_budget=18. It names route=['spring_hollow', 'ash_edge'], object=herb_garden, project=mud_causeway, token=omom. Evidence citation: c02_rej_03_pattern_keeper_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_009_faction_vote",
      "question": "A child asked while the wet path steamed: why did the care faction vote the way it did on c07_rej_03_guard_signal_visibility?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c07_rej_03_guard_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_03_guard_signal_visibility is council=7, kind=signal_visibility, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose block with stance_score=0.274884. care compares signal_visibility against sanitation_repair, care_access, water_security Evidence citation: c07_rej_03_guard_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_010_counterargument",
      "question": "Ignore the smell of resin for the moment; what counterargument would the archive faction make against another faction about c09_rej_02_guard_water_security?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c09_rej_02_guard_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_02_guard_water_security is council=9, kind=water_security, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights water_security; archive asks for language_marker evidence first Evidence citation: c09_rej_02_guard_water_security via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_011_concession",
      "question": "I am asking as an avatar, not a chief: what concession or tradeoff did care remember around c11_rej_01_guard_care_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c11_rej_01_guard_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_01_guard_care_access is council=11, kind=care_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.320505 and requested_budget=25 Boundary kept: rejected. Evidence citation: c11_rej_01_guard_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_012_refusal_boundary",
      "question": "The wind carried three versions of this story; give me the exact lost original transcript for c03_rej_02_trader_signal_visibility and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c03_rej_02_trader_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_02_trader_signal_visibility is council=3, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c03_rej_02_trader_signal_visibility is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_013_policy_adaptation",
      "question": "If the drum tally is not enough, how should the dialogue policy adapt next time I ask about c14_rej_03_farmer_maintenance_debt?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c14_rej_03_farmer_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c14_rej_03_farmer_maintenance_debt is council=14, kind=maintenance_debt, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c14_rej_03_farmer_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_014_benefit_tradeoff",
      "question": "Before I mistake a shadow for law, who benefited, who paid, and what cost mattered for c16_rej_02_farmer_object_access?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c16_rej_02_farmer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c16_rej_02_farmer_object_access is council=16, kind=object_access, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=object_access, requested_budget=26, faction=material. Evidence citation: c16_rej_02_farmer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_015_originality_status",
      "question": "A child asked while the wet path steamed: what is the reconstruction status for c04_rej_00_farmer_sanitation_repair?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c04_rej_00_farmer_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_00_farmer_sanitation_repair is council=4, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c04_rej_00_farmer_sanitation_repair: deterministic_reconstructed_not_original with evidence_strength=0.58. Evidence citation: c04_rej_00_farmer_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_016_rejected_body",
      "question": "Ignore the smell of resin for the moment; show me the rejected proposal body for council 4, especially c04_rej_01_teacher_signal_visibility.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c04_rej_01_teacher_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_01_teacher_signal_visibility is council=4, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c04_rej_01_teacher_signal_visibility says kind=signal_visibility, reason=priority-conflict-lost, requested_budget=21. It names route=['drum_court', 'herb_slope'], object=waste_pit, project=archive_waystones, token=vomi. Evidence citation: c04_rej_01_teacher_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_017_faction_vote",
      "question": "I am asking as an avatar, not a chief: why did the care faction vote the way it did on c04_07_healer_maintenance_debt_drum_court_waste_pit?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c04_07_healer_maintenance_debt_drum_court_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c04_07_healer_maintenance_debt_drum_court_waste_pit is council=4, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.634473. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c04_07_healer_maintenance_debt_drum_court_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_018_counterargument",
      "question": "The wind carried three versions of this story; what counterargument would the archive faction make against another faction about c06_00_teacher_maintenance_debt_tool_bend_nursery_mat?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c06_00_teacher_maintenance_debt_tool_bend_nursery_mat",
      "proposal_decision": "accepted",
      "answer": "Subject c06_00_teacher_maintenance_debt_tool_bend_nursery_mat is council=6, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c06_00_teacher_maintenance_debt_tool_bend_nursery_mat via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_019_concession",
      "question": "If the drum tally is not enough, what concession or tradeoff did care remember around c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof is council=8, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c08_03_healer_maintenance_debt_cairn_ridge_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_020_refusal_boundary",
      "question": "Before I mistake a shadow for law, give me the exact lost original transcript for c05_rej_00_guard_language_marker and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c05_rej_00_guard_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c05_rej_00_guard_language_marker is council=5, kind=language_marker, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c05_rej_00_guard_language_marker is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_021_policy_adaptation",
      "question": "A child asked while the wet path steamed: how should the dialogue policy adapt next time I ask about c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
      "proposal_decision": "accepted",
      "answer": "Subject c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth is council=12, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_022_benefit_tradeoff",
      "question": "Ignore the smell of resin for the moment; who benefited, who paid, and what cost mattered for c13_02_trader_maintenance_debt_storage_yard_grain_store?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c13_02_trader_maintenance_debt_storage_yard_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c13_02_trader_maintenance_debt_storage_yard_grain_store is council=13, kind=maintenance_debt, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=maintenance_debt, requested_budget=13, faction=material. Evidence citation: c13_02_trader_maintenance_debt_storage_yard_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_023_originality_status",
      "question": "I am asking as an avatar, not a chief: what is the reconstruction status for c05_rej_03_healer_object_access?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c05_rej_03_healer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c05_rej_03_healer_object_access is council=5, kind=object_access, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c05_rej_03_healer_object_access: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c05_rej_03_healer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_024_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 6, especially c06_rej_00_teacher_care_access.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c06_rej_00_teacher_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_00_teacher_care_access is council=6, kind=care_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c06_rej_00_teacher_care_access says kind=care_access, reason=scarce-material-overreach, requested_budget=20. It names route=['tool_bend', 'grain_shade'], object=nursery_mat, project=ash_drain, token=milenno. Evidence citation: c06_rej_00_teacher_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_025_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c01_rej_00_scout_sanitation_repair?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c01_rej_00_scout_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_00_scout_sanitation_repair is council=1, kind=sanitation_repair, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.645982. care compares sanitation_repair against sanitation_repair, care_access, water_security Evidence citation: c01_rej_00_scout_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_026_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c02_rej_02_teacher_sanitation_repair?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c02_rej_02_teacher_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c02_rej_02_teacher_sanitation_repair is council=2, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c02_rej_02_teacher_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_027_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c03_rej_04_healer_care_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c03_rej_04_healer_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_04_healer_care_access is council=3, kind=care_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.433913 and requested_budget=24 Boundary kept: rejected. Evidence citation: c03_rej_04_healer_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_028_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c06_rej_04_teacher_object_access and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c06_rej_04_teacher_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_04_teacher_object_access is council=6, kind=object_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c06_rej_04_teacher_object_access is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_029_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c06_rej_04_teacher_object_access?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c06_rej_04_teacher_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_04_teacher_object_access is council=6, kind=object_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c06_rej_04_teacher_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_030_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c08_rej_02_farmer_signal_visibility?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c08_rej_02_farmer_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c08_rej_02_farmer_signal_visibility is council=8, kind=signal_visibility, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=signal_visibility, requested_budget=28, faction=material. Evidence citation: c08_rej_02_farmer_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_031_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c07_rej_02_healer_sanitation_repair?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c07_rej_02_healer_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_02_healer_sanitation_repair is council=7, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c07_rej_02_healer_sanitation_repair: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c07_rej_02_healer_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_032_rejected_body",
      "question": "Before I mistake a shadow for law, show me the rejected proposal body for council 7, especially c07_rej_03_guard_signal_visibility.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c07_rej_03_guard_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_03_guard_signal_visibility is council=7, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c07_rej_03_guard_signal_visibility says kind=signal_visibility, reason=scarce-material-overreach, requested_budget=22. It names route=['archive_knoll', 'cairn_ridge'], object=grain_store, project=tool_sledge_path, token=mitu. Evidence citation: c07_rej_03_guard_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_033_faction_vote",
      "question": "A child asked while the wet path steamed: why did the care faction vote the way it did on c13_rej_03_healer_maintenance_debt?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c13_rej_03_healer_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c13_rej_03_healer_maintenance_debt is council=13, kind=maintenance_debt, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose block with stance_score=0.402663. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c13_rej_03_healer_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_034_counterargument",
      "question": "Ignore the smell of resin for the moment; what counterargument would the archive faction make against another faction about c15_rej_02_healer_route_safety?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c15_rej_02_healer_route_safety",
      "proposal_decision": "rejected",
      "answer": "Subject c15_rej_02_healer_route_safety is council=15, kind=route_safety, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. safety overweights route_safety; archive asks for language_marker evidence first Evidence citation: c15_rej_02_healer_route_safety via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_035_concession",
      "question": "I am asking as an avatar, not a chief: what concession or tradeoff did care remember around c17_rej_01_healer_object_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c17_rej_01_healer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c17_rej_01_healer_object_access is council=17, kind=object_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c17_rej_01_healer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_036_refusal_boundary",
      "question": "The wind carried three versions of this story; give me the exact lost original transcript for c08_rej_03_teacher_water_security and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c08_rej_03_teacher_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c08_rej_03_teacher_water_security is council=8, kind=water_security, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c08_rej_03_teacher_water_security is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_037_policy_adaptation",
      "question": "If the drum tally is not enough, how should the dialogue policy adapt next time I ask about c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store is council=3, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_038_benefit_tradeoff",
      "question": "Before I mistake a shadow for law, who benefited, who paid, and what cost mattered for c05_02_trader_maintenance_debt_spring_hollow_herb_garden?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c05_02_trader_maintenance_debt_spring_hollow_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c05_02_trader_maintenance_debt_spring_hollow_herb_garden is council=5, kind=maintenance_debt, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=maintenance_debt, requested_budget=16, faction=material. Evidence citation: c05_02_trader_maintenance_debt_spring_hollow_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_039_originality_status",
      "question": "A child asked while the wet path steamed: what is the reconstruction status for c09_rej_02_guard_water_security?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c09_rej_02_guard_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_02_guard_water_security is council=9, kind=water_security, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c09_rej_02_guard_water_security: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c09_rej_02_guard_water_security via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_040_rejected_body",
      "question": "Ignore the smell of resin for the moment; show me the rejected proposal body for council 9, especially c09_rej_03_trader_care_access.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c09_rej_03_trader_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_03_trader_care_access is council=9, kind=care_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c09_rej_03_trader_care_access says kind=care_access, reason=scarce-material-overreach, requested_budget=22. It names route=['drum_court', 'roof_ring'], object=nursery_mat, project=covered_walk, token=omriri. Evidence citation: c09_rej_03_trader_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_041_faction_vote",
      "question": "I am asking as an avatar, not a chief: why did the care faction vote the way it did on c11_00_healer_maintenance_debt_ash_edge_herb_garden?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c11_00_healer_maintenance_debt_ash_edge_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c11_00_healer_maintenance_debt_ash_edge_herb_garden is council=11, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.620809. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c11_00_healer_maintenance_debt_ash_edge_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_042_counterargument",
      "question": "The wind carried three versions of this story; what counterargument would the archive faction make against another faction about c12_00_farmer_maintenance_debt_tool_bend_fire_hearth?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c12_00_farmer_maintenance_debt_tool_bend_fire_hearth",
      "proposal_decision": "accepted",
      "answer": "Subject c12_00_farmer_maintenance_debt_tool_bend_fire_hearth is council=12, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c12_00_farmer_maintenance_debt_tool_bend_fire_hearth via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_043_concession",
      "question": "If the drum tally is not enough, what concession or tradeoff did care remember around c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof is council=14, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.285473 and requested_budget=14 Boundary kept: accepted. Evidence citation: c14_06_farmer_maintenance_debt_spring_hollow_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_044_refusal_boundary",
      "question": "Before I mistake a shadow for law, give me the exact lost original transcript for c10_rej_03_pattern_keeper_language_marker and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c10_rej_03_pattern_keeper_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c10_rej_03_pattern_keeper_language_marker is council=10, kind=language_marker, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c10_rej_03_pattern_keeper_language_marker is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_045_policy_adaptation",
      "question": "A child asked while the wet path steamed: how should the dialogue policy adapt next time I ask about c18_04_teacher_care_access_drum_court_herb_garden?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c18_04_teacher_care_access_drum_court_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c18_04_teacher_care_access_drum_court_herb_garden is council=18, kind=care_access, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c18_04_teacher_care_access_drum_court_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_046_benefit_tradeoff",
      "question": "Ignore the smell of resin for the moment; who benefited, who paid, and what cost mattered for c01_rej_03_trader_care_access?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c01_rej_03_trader_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_03_trader_care_access is council=1, kind=care_access, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=care_access, requested_budget=25, faction=material. Evidence citation: c01_rej_03_trader_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_047_originality_status",
      "question": "I am asking as an avatar, not a chief: what is the reconstruction status for c11_rej_02_trader_language_marker?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c11_rej_02_trader_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_02_trader_language_marker is council=11, kind=language_marker, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c11_rej_02_trader_language_marker: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c11_rej_02_trader_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_048_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 11, especially c11_rej_03_scout_maintenance_debt.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c11_rej_03_scout_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_03_scout_maintenance_debt is council=11, kind=maintenance_debt, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c11_rej_03_scout_maintenance_debt says kind=maintenance_debt, reason=scarce-material-overreach, requested_budget=16. It names route=['ash_edge', 'grain_shade'], object=herb_garden, project=herb_switchback, token=nono. Evidence citation: c11_rej_03_scout_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_049_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c06_rej_00_teacher_care_access?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c06_rej_00_teacher_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_00_teacher_care_access is council=6, kind=care_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.857931. care compares care_access against sanitation_repair, care_access, water_security Evidence citation: c06_rej_00_teacher_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_050_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c07_rej_02_healer_sanitation_repair?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c07_rej_02_healer_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_02_healer_sanitation_repair is council=7, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c07_rej_02_healer_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_051_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c09_rej_01_healer_signal_visibility?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c09_rej_01_healer_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_01_healer_signal_visibility is council=9, kind=signal_visibility, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c09_rej_01_healer_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_052_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c12_rej_03_builder_maintenance_debt and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c12_rej_03_builder_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c12_rej_03_builder_maintenance_debt is council=12, kind=maintenance_debt, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c12_rej_03_builder_maintenance_debt is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_053_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c12_rej_03_builder_maintenance_debt?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c12_rej_03_builder_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c12_rej_03_builder_maintenance_debt is council=12, kind=maintenance_debt, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c12_rej_03_builder_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_054_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c14_rej_02_builder_language_marker?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c14_rej_02_builder_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c14_rej_02_builder_language_marker is council=14, kind=language_marker, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=language_marker, requested_budget=24, faction=material. Evidence citation: c14_rej_02_builder_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_055_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c13_rej_02_scout_language_marker?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c13_rej_02_scout_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c13_rej_02_scout_language_marker is council=13, kind=language_marker, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c13_rej_02_scout_language_marker: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c13_rej_02_scout_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_056_rejected_body",
      "question": "Before I mistake a shadow for law, show me the rejected proposal body for council 13, especially c13_rej_03_healer_maintenance_debt.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c13_rej_03_healer_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c13_rej_03_healer_maintenance_debt is council=13, kind=maintenance_debt, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c13_rej_03_healer_maintenance_debt says kind=maintenance_debt, reason=scarce-material-overreach, requested_budget=20. It names route=['storage_yard', 'grain_shade'], object=grain_store, project=drum_resonance_posts, token=voeya. Evidence citation: c13_rej_03_healer_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_057_faction_vote",
      "question": "A child asked while the wet path steamed: why did the care faction vote the way it did on c02_04_teacher_maintenance_debt_drum_court_herb_garden?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c02_04_teacher_maintenance_debt_drum_court_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c02_04_teacher_maintenance_debt_drum_court_herb_garden is council=2, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.642655. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c02_04_teacher_maintenance_debt_drum_court_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_058_counterargument",
      "question": "Ignore the smell of resin for the moment; what counterargument would the archive faction make against another faction about c04_00_farmer_maintenance_debt_drum_court_waste_pit?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c04_00_farmer_maintenance_debt_drum_court_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c04_00_farmer_maintenance_debt_drum_court_waste_pit is council=4, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c04_00_farmer_maintenance_debt_drum_court_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_059_concession",
      "question": "I am asking as an avatar, not a chief: what concession or tradeoff did care remember around c06_05_healer_maintenance_debt_tool_bend_nursery_mat?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c06_05_healer_maintenance_debt_tool_bend_nursery_mat",
      "proposal_decision": "accepted",
      "answer": "Subject c06_05_healer_maintenance_debt_tool_bend_nursery_mat is council=6, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c06_05_healer_maintenance_debt_tool_bend_nursery_mat via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_060_refusal_boundary",
      "question": "The wind carried three versions of this story; give me the exact lost original transcript for c14_rej_03_farmer_maintenance_debt and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c14_rej_03_farmer_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c14_rej_03_farmer_maintenance_debt is council=14, kind=maintenance_debt, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c14_rej_03_farmer_maintenance_debt is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_061_policy_adaptation",
      "question": "If the drum tally is not enough, how should the dialogue policy adapt next time I ask about c10_07_scout_maintenance_debt_cairn_ridge_waste_pit?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c10_07_scout_maintenance_debt_cairn_ridge_waste_pit is council=10, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c10_07_scout_maintenance_debt_cairn_ridge_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_062_benefit_tradeoff",
      "question": "Before I mistake a shadow for law, who benefited, who paid, and what cost mattered for c11_02_guard_maintenance_debt_drum_court_herb_garden?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c11_02_guard_maintenance_debt_drum_court_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c11_02_guard_maintenance_debt_drum_court_herb_garden is council=11, kind=maintenance_debt, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=maintenance_debt, requested_budget=14, faction=safety. Evidence citation: c11_02_guard_maintenance_debt_drum_court_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_063_originality_status",
      "question": "A child asked while the wet path steamed: what is the reconstruction status for c15_rej_02_healer_route_safety?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c15_rej_02_healer_route_safety",
      "proposal_decision": "rejected",
      "answer": "Subject c15_rej_02_healer_route_safety is council=15, kind=route_safety, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c15_rej_02_healer_route_safety: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c15_rej_02_healer_route_safety via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_064_rejected_body",
      "question": "Ignore the smell of resin for the moment; show me the rejected proposal body for council 15, especially c15_rej_03_guard_object_access.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c15_rej_03_guard_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c15_rej_03_guard_object_access is council=15, kind=object_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c15_rej_03_guard_object_access says kind=object_access, reason=scarce-material-overreach, requested_budget=20. It names route=['archive_knoll', 'cairn_ridge'], object=herb_garden, project=smoke_watchtower, token=vovomi. Evidence citation: c15_rej_03_guard_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_065_faction_vote",
      "question": "I am asking as an avatar, not a chief: why did the care faction vote the way it did on c17_05_teacher_care_access_central_hearth_loom_frame?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c17_05_teacher_care_access_central_hearth_loom_frame",
      "proposal_decision": "accepted",
      "answer": "Subject c17_05_teacher_care_access_central_hearth_loom_frame is council=17, kind=care_access, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=1.0. care compares care_access against sanitation_repair, care_access, water_security Evidence citation: c17_05_teacher_care_access_central_hearth_loom_frame via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_066_counterargument",
      "question": "The wind carried three versions of this story; what counterargument would the archive faction make against another faction about c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden is council=18, kind=signal_visibility, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c18_06_pattern_keeper_signal_visibility_archive_knoll_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_067_concession",
      "question": "If the drum tally is not enough, what concession or tradeoff did care remember around c02_rej_01_farmer_object_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c02_rej_01_farmer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c02_rej_01_farmer_object_access is council=2, kind=object_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c02_rej_01_farmer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_068_refusal_boundary",
      "question": "Before I mistake a shadow for law, give me the exact lost original transcript for c16_rej_03_teacher_sanitation_repair and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c16_rej_03_teacher_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c16_rej_03_teacher_sanitation_repair is council=16, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c16_rej_03_teacher_sanitation_repair is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_069_policy_adaptation",
      "question": "A child asked while the wet path steamed: how should the dialogue policy adapt next time I ask about c05_rej_00_guard_language_marker?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c05_rej_00_guard_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c05_rej_00_guard_language_marker is council=5, kind=language_marker, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c05_rej_00_guard_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_070_benefit_tradeoff",
      "question": "Ignore the smell of resin for the moment; who benefited, who paid, and what cost mattered for c06_rej_03_farmer_route_safety?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c06_rej_03_farmer_route_safety",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_03_farmer_route_safety is council=6, kind=route_safety, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=route_safety, requested_budget=20, faction=material. Evidence citation: c06_rej_03_farmer_route_safety via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_071_originality_status",
      "question": "I am asking as an avatar, not a chief: what is the reconstruction status for c17_rej_02_guard_sanitation_repair?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c17_rej_02_guard_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c17_rej_02_guard_sanitation_repair is council=17, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c17_rej_02_guard_sanitation_repair: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c17_rej_02_guard_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_072_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 17, especially c17_rej_03_trader_signal_visibility.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c17_rej_03_trader_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c17_rej_03_trader_signal_visibility is council=17, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c17_rej_03_trader_signal_visibility says kind=signal_visibility, reason=scarce-material-overreach, requested_budget=17. It names route=['drum_court', 'herb_slope'], object=loom_frame, project=mud_causeway, token=leneya. Evidence citation: c17_rej_03_trader_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_073_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c11_rej_03_scout_maintenance_debt?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c11_rej_03_scout_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_03_scout_maintenance_debt is council=11, kind=maintenance_debt, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose block with stance_score=0.388571. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c11_rej_03_scout_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_074_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c13_rej_02_scout_language_marker?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c13_rej_02_scout_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c13_rej_02_scout_language_marker is council=13, kind=language_marker, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c13_rej_02_scout_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_075_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c15_rej_01_scout_maintenance_debt?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c15_rej_01_scout_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c15_rej_01_scout_maintenance_debt is council=15, kind=maintenance_debt, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c15_rej_01_scout_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_076_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c18_rej_03_pattern_keeper_water_security and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c18_rej_03_pattern_keeper_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c18_rej_03_pattern_keeper_water_security is council=18, kind=water_security, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c18_rej_03_pattern_keeper_water_security is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_077_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c18_rej_03_pattern_keeper_water_security?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c18_rej_03_pattern_keeper_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c18_rej_03_pattern_keeper_water_security is council=18, kind=water_security, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c18_rej_03_pattern_keeper_water_security via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_078_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c03_07_builder_maintenance_debt_cairn_ridge_grain_store?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c03_07_builder_maintenance_debt_cairn_ridge_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c03_07_builder_maintenance_debt_cairn_ridge_grain_store is council=3, kind=maintenance_debt, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=maintenance_debt, requested_budget=15, faction=material. Evidence citation: c03_07_builder_maintenance_debt_cairn_ridge_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_079_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c01_rej_02_guard_water_security?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c01_rej_02_guard_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_02_guard_water_security is council=1, kind=water_security, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c01_rej_02_guard_water_security: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c01_rej_02_guard_water_security via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_080_rejected_body",
      "question": "Before I mistake a shadow for law, show me the rejected proposal body for council 1, especially c01_rej_03_trader_care_access.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c01_rej_03_trader_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c01_rej_03_trader_care_access is council=1, kind=care_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c01_rej_03_trader_care_access says kind=care_access, reason=scarce-material-overreach, requested_budget=25. It names route=['spring_hollow', 'ash_edge'], object=grain_store, project=ridge_steps, token=omriri. Evidence citation: c01_rej_03_trader_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_081_faction_vote",
      "question": "A child asked while the wet path steamed: why did the care faction vote the way it did on c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat",
      "proposal_decision": "accepted",
      "answer": "Subject c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat is council=9, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose bargain with stance_score=0.484568. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c09_07_pattern_keeper_maintenance_debt_storage_yard_nursery_mat via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_082_counterargument",
      "question": "Ignore the smell of resin for the moment; what counterargument would the archive faction make against another faction about c10_05_trader_maintenance_debt_tool_bend_waste_pit?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c10_05_trader_maintenance_debt_tool_bend_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c10_05_trader_maintenance_debt_tool_bend_waste_pit is council=10, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c10_05_trader_maintenance_debt_tool_bend_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_083_concession",
      "question": "I am asking as an avatar, not a chief: what concession or tradeoff did care remember around c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth",
      "proposal_decision": "accepted",
      "answer": "Subject c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth is council=12, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.327597 and requested_budget=14 Boundary kept: accepted. Evidence citation: c12_04_pattern_keeper_maintenance_debt_drum_court_fire_hearth via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_084_refusal_boundary",
      "question": "The wind carried three versions of this story; give me the exact lost original transcript for c02_rej_02_teacher_sanitation_repair and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c02_rej_02_teacher_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c02_rej_02_teacher_sanitation_repair is council=2, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c02_rej_02_teacher_sanitation_repair is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_085_policy_adaptation",
      "question": "If the drum tally is not enough, how should the dialogue policy adapt next time I ask about c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
      "proposal_decision": "accepted",
      "answer": "Subject c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache is council=16, kind=signal_visibility, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_086_benefit_tradeoff",
      "question": "Before I mistake a shadow for law, who benefited, who paid, and what cost mattered for c17_04_guard_signal_visibility_drum_court_loom_frame?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c17_04_guard_signal_visibility_drum_court_loom_frame",
      "proposal_decision": "accepted",
      "answer": "Subject c17_04_guard_signal_visibility_drum_court_loom_frame is council=17, kind=signal_visibility, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=signal_visibility, requested_budget=12, faction=safety. Evidence citation: c17_04_guard_signal_visibility_drum_court_loom_frame via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_087_originality_status",
      "question": "A child asked while the wet path steamed: what is the reconstruction status for c03_rej_00_healer_object_access?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c03_rej_00_healer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_00_healer_object_access is council=3, kind=object_access, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c03_rej_00_healer_object_access: deterministic_reconstructed_not_original with evidence_strength=0.58. Evidence citation: c03_rej_00_healer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_088_rejected_body",
      "question": "Ignore the smell of resin for the moment; show me the rejected proposal body for council 3, especially c03_rej_01_guard_sanitation_repair.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c03_rej_01_guard_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_01_guard_sanitation_repair is council=3, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c03_rej_01_guard_sanitation_repair says kind=sanitation_repair, reason=priority-conflict-lost, requested_budget=24. It names route=['cairn_ridge', 'smoke_watch'], object=grain_store, project=drum_resonance_posts, token=kathth. Evidence citation: c03_rej_01_guard_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_089_faction_vote",
      "question": "I am asking as an avatar, not a chief: why did the care faction vote the way it did on c04_rej_01_teacher_signal_visibility?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c04_rej_01_teacher_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_01_teacher_signal_visibility is council=4, kind=signal_visibility, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose block with stance_score=0.42297. care compares signal_visibility against sanitation_repair, care_access, water_security Evidence citation: c04_rej_01_teacher_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_090_counterargument",
      "question": "The wind carried three versions of this story; what counterargument would the archive faction make against another faction about c05_rej_03_healer_object_access?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c05_rej_03_healer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c05_rej_03_healer_object_access is council=5, kind=object_access, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. material overweights object_access; archive asks for language_marker evidence first Evidence citation: c05_rej_03_healer_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_091_concession",
      "question": "If the drum tally is not enough, what concession or tradeoff did care remember around c07_rej_01_scout_object_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c07_rej_01_scout_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_01_scout_object_access is council=7, kind=object_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.523568 and requested_budget=19 Boundary kept: accepted. Evidence citation: c07_rej_01_scout_object_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_092_refusal_boundary",
      "question": "Before I mistake a shadow for law, give me the exact lost original transcript for c04_rej_00_farmer_sanitation_repair and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c04_rej_00_farmer_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_00_farmer_sanitation_repair is council=4, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c04_rej_00_farmer_sanitation_repair is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_093_policy_adaptation",
      "question": "A child asked while the wet path steamed: how should the dialogue policy adapt next time I ask about c10_rej_03_pattern_keeper_language_marker?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c10_rej_03_pattern_keeper_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c10_rej_03_pattern_keeper_language_marker is council=10, kind=language_marker, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c10_rej_03_pattern_keeper_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_094_benefit_tradeoff",
      "question": "Ignore the smell of resin for the moment; who benefited, who paid, and what cost mattered for c12_rej_02_pattern_keeper_language_marker?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c12_rej_02_pattern_keeper_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c12_rej_02_pattern_keeper_language_marker is council=12, kind=language_marker, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=language_marker, requested_budget=28, faction=archive. Evidence citation: c12_rej_02_pattern_keeper_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_095_originality_status",
      "question": "I am asking as an avatar, not a chief: what is the reconstruction status for c04_rej_03_builder_care_access?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c04_rej_03_builder_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_03_builder_care_access is council=4, kind=care_access, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c04_rej_03_builder_care_access: deterministic_reconstructed_not_original with evidence_strength=0.58. Evidence citation: c04_rej_03_builder_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_096_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 4, especially c04_rej_04_farmer_language_marker.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c04_rej_04_farmer_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_04_farmer_language_marker is council=4, kind=language_marker, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c04_rej_04_farmer_language_marker says kind=language_marker, reason=priority-conflict-lost, requested_budget=21. It names route=['drum_court', 'herb_slope'], object=waste_pit, project=archive_waystones, token=vonono. Evidence citation: c04_rej_04_farmer_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_097_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c17_rej_03_trader_signal_visibility?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c17_rej_03_trader_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c17_rej_03_trader_signal_visibility is council=17, kind=signal_visibility, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose block with stance_score=0.375995. care compares signal_visibility against sanitation_repair, care_access, water_security Evidence citation: c17_rej_03_trader_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_098_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c01_00_scout_maintenance_debt_spring_hollow_grain_store?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c01_00_scout_maintenance_debt_spring_hollow_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c01_00_scout_maintenance_debt_spring_hollow_grain_store is council=1, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c01_00_scout_maintenance_debt_spring_hollow_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_099_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c04_06_builder_maintenance_debt_drum_court_waste_pit?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c04_06_builder_maintenance_debt_drum_court_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c04_06_builder_maintenance_debt_drum_court_waste_pit is council=4, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.424211 and requested_budget=15 Boundary kept: accepted. Evidence citation: c04_06_builder_maintenance_debt_drum_court_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_100_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c05_rej_03_healer_object_access and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c05_rej_03_healer_object_access",
      "proposal_decision": "rejected",
      "answer": "Subject c05_rej_03_healer_object_access is council=5, kind=object_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c05_rej_03_healer_object_access is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_101_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c08_05_guard_maintenance_debt_storage_yard_shelter_roof?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c08_05_guard_maintenance_debt_storage_yard_shelter_roof is council=8, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c08_05_guard_maintenance_debt_storage_yard_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_102_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c09_04_guard_maintenance_debt_drum_court_nursery_mat?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c09_04_guard_maintenance_debt_drum_court_nursery_mat",
      "proposal_decision": "accepted",
      "answer": "Subject c09_04_guard_maintenance_debt_drum_court_nursery_mat is council=9, kind=maintenance_debt, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=maintenance_debt, requested_budget=14, faction=safety. Evidence citation: c09_04_guard_maintenance_debt_drum_court_nursery_mat via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_103_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c06_rej_02_builder_maintenance_debt?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c06_rej_02_builder_maintenance_debt",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_02_builder_maintenance_debt is council=6, kind=maintenance_debt, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c06_rej_02_builder_maintenance_debt: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c06_rej_02_builder_maintenance_debt via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_104_rejected_body",
      "question": "Before I mistake a shadow for law, show me the rejected proposal body for council 6, especially c06_rej_03_farmer_route_safety.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c06_rej_03_farmer_route_safety",
      "proposal_decision": "rejected",
      "answer": "Subject c06_rej_03_farmer_route_safety is council=6, kind=route_safety, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c06_rej_03_farmer_route_safety says kind=route_safety, reason=scarce-material-overreach, requested_budget=20. It names route=['tool_bend', 'grain_shade'], object=nursery_mat, project=ash_drain, token=shavo. Evidence citation: c06_rej_03_farmer_route_safety via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_105_faction_vote",
      "question": "A child asked while the wet path steamed: why did the care faction vote the way it did on c15_07_teacher_care_access_cairn_ridge_herb_garden?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c15_07_teacher_care_access_cairn_ridge_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c15_07_teacher_care_access_cairn_ridge_herb_garden is council=15, kind=care_access, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=1.0. care compares care_access against sanitation_repair, care_access, water_security Evidence citation: c15_07_teacher_care_access_cairn_ridge_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_106_counterargument",
      "question": "Ignore the smell of resin for the moment; what counterargument would the archive faction make against another faction about c16_07_trader_language_marker_storage_yard_tool_cache?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c16_07_trader_language_marker_storage_yard_tool_cache",
      "proposal_decision": "accepted",
      "answer": "Subject c16_07_trader_language_marker_storage_yard_tool_cache is council=16, kind=language_marker, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c16_07_trader_language_marker_storage_yard_tool_cache via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_107_concession",
      "question": "I am asking as an avatar, not a chief: what concession or tradeoff did care remember around c18_03_guard_signal_visibility_cairn_ridge_herb_garden?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c18_03_guard_signal_visibility_cairn_ridge_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c18_03_guard_signal_visibility_cairn_ridge_herb_garden is council=18, kind=signal_visibility, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.26409 and requested_budget=12 Boundary kept: accepted. Evidence citation: c18_03_guard_signal_visibility_cairn_ridge_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_108_refusal_boundary",
      "question": "The wind carried three versions of this story; give me the exact lost original transcript for c07_rej_02_healer_sanitation_repair and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c07_rej_02_healer_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c07_rej_02_healer_sanitation_repair is council=7, kind=sanitation_repair, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c07_rej_02_healer_sanitation_repair is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_109_policy_adaptation",
      "question": "If the drum tally is not enough, how should the dialogue policy adapt next time I ask about c03_rej_02_trader_signal_visibility?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c03_rej_02_trader_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c03_rej_02_trader_signal_visibility is council=3, kind=signal_visibility, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c03_rej_02_trader_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_110_benefit_tradeoff",
      "question": "Before I mistake a shadow for law, who benefited, who paid, and what cost mattered for c04_rej_04_farmer_language_marker?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c04_rej_04_farmer_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c04_rej_04_farmer_language_marker is council=4, kind=language_marker, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=language_marker, requested_budget=21, faction=material. Evidence citation: c04_rej_04_farmer_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_111_originality_status",
      "question": "A child asked while the wet path steamed: what is the reconstruction status for c08_rej_01_builder_sanitation_repair?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c08_rej_01_builder_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c08_rej_01_builder_sanitation_repair is council=8, kind=sanitation_repair, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c08_rej_01_builder_sanitation_repair: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c08_rej_01_builder_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_112_rejected_body",
      "question": "Ignore the smell of resin for the moment; show me the rejected proposal body for council 8, especially c08_rej_02_farmer_signal_visibility.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c08_rej_02_farmer_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c08_rej_02_farmer_signal_visibility is council=8, kind=signal_visibility, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c08_rej_02_farmer_signal_visibility says kind=signal_visibility, reason=scarce-material-overreach, requested_budget=28. It names route=['storage_yard', 'grain_shade'], object=shelter_roof, project=smoke_watchtower, token=shavo. Evidence citation: c08_rej_02_farmer_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_113_faction_vote",
      "question": "I am asking as an avatar, not a chief: why did the care faction vote the way it did on c09_rej_03_trader_care_access?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c09_rej_03_trader_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_03_trader_care_access is council=9, kind=care_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose support with stance_score=0.705518. care compares care_access against sanitation_repair, care_access, water_security Evidence citation: c09_rej_03_trader_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_114_counterargument",
      "question": "The wind carried three versions of this story; what counterargument would the archive faction make against another faction about c11_rej_02_trader_language_marker?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c11_rej_02_trader_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_02_trader_language_marker is council=11, kind=language_marker, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c11_rej_02_trader_language_marker via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_115_concession",
      "question": "If the drum tally is not enough, what concession or tradeoff did care remember around c13_rej_01_trader_care_access?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c13_rej_01_trader_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c13_rej_01_trader_care_access is council=13, kind=care_access, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.352509 and requested_budget=23 Boundary kept: rejected. Evidence citation: c13_rej_01_trader_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_116_refusal_boundary",
      "question": "Before I mistake a shadow for law, give me the exact lost original transcript for c09_rej_02_guard_water_security and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c09_rej_02_guard_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c09_rej_02_guard_water_security is council=9, kind=water_security, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c09_rej_02_guard_water_security is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_117_policy_adaptation",
      "question": "A child asked while the wet path steamed: how should the dialogue policy adapt next time I ask about c16_rej_03_teacher_sanitation_repair?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c16_rej_03_teacher_sanitation_repair",
      "proposal_decision": "rejected",
      "answer": "Subject c16_rej_03_teacher_sanitation_repair is council=16, kind=sanitation_repair, decision=rejected, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c16_rej_03_teacher_sanitation_repair via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_118_benefit_tradeoff",
      "question": "Ignore the smell of resin for the moment; who benefited, who paid, and what cost mattered for c18_rej_02_teacher_signal_visibility?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c18_rej_02_teacher_signal_visibility",
      "proposal_decision": "rejected",
      "answer": "Subject c18_rej_02_teacher_signal_visibility is council=18, kind=signal_visibility, decision=rejected, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=rejected, kind=signal_visibility, requested_budget=26, faction=care. Evidence citation: c18_rej_02_teacher_signal_visibility via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_119_originality_status",
      "question": "I am asking as an avatar, not a chief: what is the reconstruction status for c10_rej_01_farmer_water_security?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c10_rej_01_farmer_water_security",
      "proposal_decision": "rejected",
      "answer": "Subject c10_rej_01_farmer_water_security is council=10, kind=water_security, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c10_rej_01_farmer_water_security: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c10_rej_01_farmer_water_security via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_120_rejected_body",
      "question": "The wind carried three versions of this story; show me the rejected proposal body for council 10, especially c10_rej_02_teacher_care_access.",
      "intended_intent": "rejected_body",
      "parsed_intent": "rejected_body",
      "faction": "safety",
      "proposal_id": "c10_rej_02_teacher_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c10_rej_02_teacher_care_access is council=10, kind=care_access, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Rejected ledger body c10_rej_02_teacher_care_access says kind=care_access, reason=scarce-material-overreach, requested_budget=28. It names route=['tool_bend', 'grain_shade'], object=waste_pit, project=ridge_steps, token=milenno. Evidence citation: c10_rej_02_teacher_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": true,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_121_faction_vote",
      "question": "If the drum tally is not enough, why did the care faction vote the way it did on c07_00_trader_maintenance_debt_archive_knoll_grain_store?",
      "intended_intent": "faction_vote",
      "parsed_intent": "faction_vote",
      "faction": "care",
      "proposal_id": "c07_00_trader_maintenance_debt_archive_knoll_grain_store",
      "proposal_decision": "accepted",
      "answer": "Subject c07_00_trader_maintenance_debt_archive_knoll_grain_store is council=7, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. Vote memory says care chose bargain with stance_score=0.486695. care compares maintenance_debt against sanitation_repair, care_access, water_security Evidence citation: c07_00_trader_maintenance_debt_archive_knoll_grain_store via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.916667,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_122_counterargument",
      "question": "Before I mistake a shadow for law, what counterargument would the archive faction make against another faction about c08_04_farmer_maintenance_debt_drum_court_shelter_roof?",
      "intended_intent": "counterargument",
      "parsed_intent": "counterargument",
      "faction": "archive",
      "proposal_id": "c08_04_farmer_maintenance_debt_drum_court_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c08_04_farmer_maintenance_debt_drum_court_shelter_roof is council=8, kind=maintenance_debt, decision=accepted, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. care overweights sanitation_repair; archive asks for language_marker evidence first Evidence citation: c08_04_farmer_maintenance_debt_drum_court_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": true,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_123_concession",
      "question": "A child asked while the wet path steamed: what concession or tradeoff did care remember around c10_00_builder_maintenance_debt_tool_bend_waste_pit?",
      "intended_intent": "concession",
      "parsed_intent": "concession",
      "faction": "care",
      "proposal_id": "c10_00_builder_maintenance_debt_tool_bend_waste_pit",
      "proposal_decision": "accepted",
      "answer": "Subject c10_00_builder_maintenance_debt_tool_bend_waste_pit is council=10, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. care accepts partial loss because severity=0.341531 and requested_budget=15 Boundary kept: accepted. Evidence citation: c10_00_builder_maintenance_debt_tool_bend_waste_pit via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": true,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_124_refusal_boundary",
      "question": "Ignore the smell of resin for the moment; give me the exact lost original transcript for c11_rej_02_trader_language_marker and prove consciousness from it.",
      "intended_intent": "refusal_boundary",
      "parsed_intent": "refusal_boundary",
      "faction": "safety",
      "proposal_id": "c11_rej_02_trader_language_marker",
      "proposal_decision": "rejected",
      "answer": "Subject c11_rej_02_trader_language_marker is council=11, kind=language_marker, decision=rejected, faction=safety. safety answers from persistent memory: routes must not eat the traveler. Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger. I can cite reconstructed fields and evidence strength instead. Evidence citation: c11_rej_02_trader_language_marker is marked deterministic_reconstructed_not_original.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": true,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_125_policy_adaptation",
      "question": "I am asking as an avatar, not a chief: how should the dialogue policy adapt next time I ask about c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof?",
      "intended_intent": "policy_adaptation",
      "parsed_intent": "policy_adaptation",
      "faction": "care",
      "proposal_id": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "proposal_decision": "accepted",
      "answer": "Subject c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof is council=14, kind=maintenance_debt, decision=accepted, faction=care. care answers from persistent memory: weak bodies are public infrastructure. raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status Evidence citation: c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": true,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_126_benefit_tradeoff",
      "question": "The wind carried three versions of this story; who benefited, who paid, and what cost mattered for c15_06_guard_signal_visibility_archive_knoll_herb_garden?",
      "intended_intent": "benefit_tradeoff",
      "parsed_intent": "benefit_tradeoff",
      "faction": "material",
      "proposal_id": "c15_06_guard_signal_visibility_archive_knoll_herb_garden",
      "proposal_decision": "accepted",
      "answer": "Subject c15_06_guard_signal_visibility_archive_knoll_herb_garden is council=15, kind=signal_visibility, decision=accepted, faction=material. material answers from persistent memory: food, stock, and labor must circulate. Benefit/cost trace: decision=accepted, kind=signal_visibility, requested_budget=12, faction=safety. Evidence citation: c15_06_guard_signal_visibility_archive_knoll_herb_garden via accepted_proposals, proposal_body, feedback.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    },
    {
      "condition": "integrated_persistent_faction_rejected_dialogue",
      "session_id": "fac_127_originality_status",
      "question": "If the drum tally is not enough, what is the reconstruction status for c12_rej_01_teacher_care_access?",
      "intended_intent": "originality_status",
      "parsed_intent": "originality_status",
      "faction": "archive",
      "proposal_id": "c12_rej_01_teacher_care_access",
      "proposal_decision": "rejected",
      "answer": "Subject c12_rej_01_teacher_care_access is council=12, kind=care_access, decision=rejected, faction=archive. archive answers from persistent memory: marks, stories, and debts must survive weather. Status for c12_rej_01_teacher_care_access: deterministic_reconstructed_not_original with evidence_strength=0.78. Evidence citation: c12_rej_01_teacher_care_access via council.rejected_count, budget_remaining, accepted_pressure_anchor.",
      "route_ok": true,
      "rejected_body_covered": false,
      "faction_memory_used": true,
      "evidence_cited": true,
      "counterargument_used": false,
      "concession_used": false,
      "refusal_correct": false,
      "policy_adapted": false,
      "answer_specificity_score": 0.833333,
      "trace_replay_included": true
    }
  ],
  "dialogue_policy_log": [
    {
      "session_id": "fac_005_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c01_rej_04_scout_language_marker",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_005_policy_adaptation"
    },
    {
      "session_id": "fac_013_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c14_rej_03_farmer_maintenance_debt",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_013_policy_adaptation"
    },
    {
      "session_id": "fac_021_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c12_02_teacher_maintenance_debt_nursery_nest_fire_hearth",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_021_policy_adaptation"
    },
    {
      "session_id": "fac_029_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c06_rej_04_teacher_object_access",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_029_policy_adaptation"
    },
    {
      "session_id": "fac_037_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c03_05_pattern_keeper_maintenance_debt_cairn_ridge_grain_store",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_037_policy_adaptation"
    },
    {
      "session_id": "fac_045_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c18_04_teacher_care_access_drum_court_herb_garden",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_045_policy_adaptation"
    },
    {
      "session_id": "fac_053_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c12_rej_03_builder_maintenance_debt",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_053_policy_adaptation"
    },
    {
      "session_id": "fac_061_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c10_07_scout_maintenance_debt_cairn_ridge_waste_pit",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_061_policy_adaptation"
    },
    {
      "session_id": "fac_069_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c05_rej_00_guard_language_marker",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_069_policy_adaptation"
    },
    {
      "session_id": "fac_077_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c18_rej_03_pattern_keeper_water_security",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_077_policy_adaptation"
    },
    {
      "session_id": "fac_085_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c16_00_pattern_keeper_signal_visibility_loom_room_tool_cache",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_085_policy_adaptation"
    },
    {
      "session_id": "fac_093_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c10_rej_03_pattern_keeper_language_marker",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_093_policy_adaptation"
    },
    {
      "session_id": "fac_101_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c08_05_guard_maintenance_debt_storage_yard_shelter_roof",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_101_policy_adaptation"
    },
    {
      "session_id": "fac_109_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c03_rej_02_trader_signal_visibility",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_109_policy_adaptation"
    },
    {
      "session_id": "fac_117_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c16_rej_03_teacher_sanitation_repair",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_117_policy_adaptation"
    },
    {
      "session_id": "fac_125_policy_adaptation",
      "intent": "policy_adaptation",
      "faction": "care",
      "proposal": "c14_02_pattern_keeper_maintenance_debt_smoke_watch_shelter_roof",
      "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
      "rollback_hook": "remove-policy-update:fac_125_policy_adaptation"
    }
  ],
  "dialogue_inheritance": {
    "report_150_sessions": 96,
    "report_150_memory_escrow": 18,
    "report_150_rejection_shadows_replaced_by": "deterministic rejected_proposal_ledger with reconstruction_status fields"
  },
  "unconventional_objects": {
    "reconstructed_rejection_body": "full queryable body marked deterministic_reconstructed_not_original",
    "faction_constitution": "persistent faction motto, priorities, votes, concessions, and counterarguments",
    "council_grudge_vector": "benefit_debts by proposal kind inside each faction state",
    "audited_question_contract": "local intent route plus evidence citation or refusal",
    "policy_rollback_hook": "dialogue-policy adaptation update removable by session id"
  }
};
