window.SSRM_3D_GUILD_MEMORY_CRAFT_STANDARDS_TOOL_INHERITANCE_STATE = {
  "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
  "config": {
    "cycles": 6,
    "seed": 20260807,
    "source_state": "artifacts/ssrm_3d_multi_week_apprenticeship_skill_transfer_tool_career_bridge_state.json"
  },
  "guild_state": {
    "careers": {
      "Ari": {
        "agent_id": "Ari",
        "autonomy": 0.5199999999999999,
        "career_identity": [
          "I am learning the repair_lead path.",
          "I am becoming repair_lead through repair.",
          "I am becoming repair_lead through construction.",
          "I am becoming repair_lead through teaching."
        ],
        "career_memories": [
          "week 0: schedule memory guided repair",
          "week 1: schedule memory guided construction",
          "week 2: schedule memory guided teaching",
          "week 3: schedule memory guided repair",
          "week 4: schedule memory guided construction",
          "week 5: schedule memory guided teaching",
          "week 6: schedule memory guided repair",
          "week 7: schedule memory guided construction"
        ],
        "fatigue": 0.6140000000000003,
        "last_mentor": "Fay",
        "last_skill": "construction",
        "primary_skill": "repair",
        "role": "repair_lead",
        "skills": {
          "care": 0.28,
          "construction": 0.6550000000000001,
          "medicine": 0.28,
          "repair": 0.8200000000000002,
          "routing": 0.28,
          "teaching": 0.4208
        },
        "source_schedule_memories": 18,
        "teaching_lineage": [
          "Fay->Ari:repair:week0",
          "Fay->Ari:construction:week1",
          "Fay->Ari:teaching:week2",
          "Fay->Ari:repair:week3",
          "Fay->Ari:construction:week4",
          "Fay->Ari:teaching:week5",
          "Fay->Ari:repair:week6",
          "Fay->Ari:construction:week7"
        ],
        "tool": "resonant_mallet",
        "tool_affinity": 0.6267659999999999
      },
      "Fay": {
        "agent_id": "Fay",
        "autonomy": 0.61,
        "career_identity": [
          "I am learning the care_steward path.",
          "I am becoming care_steward through care.",
          "I am becoming care_steward through medicine."
        ],
        "career_memories": [
          "week 0: schedule memory guided care",
          "week 1: schedule memory guided medicine",
          "week 2: schedule memory guided care",
          "week 3: schedule memory guided care",
          "week 4: schedule memory guided medicine",
          "week 5: schedule memory guided care",
          "week 6: schedule memory guided care",
          "week 7: schedule memory guided medicine"
        ],
        "fatigue": 0.5980000000000001,
        "last_mentor": "Milo",
        "last_skill": "medicine",
        "primary_skill": "care",
        "role": "care_steward",
        "skills": {
          "care": 0.9050000000000002,
          "construction": 0.28,
          "medicine": 0.6750000000000002,
          "repair": 0.28,
          "routing": 0.28,
          "teaching": 0.44
        },
        "source_schedule_memories": 18,
        "teaching_lineage": [
          "Milo->Fay:care:week0",
          "Milo->Fay:medicine:week1",
          "Milo->Fay:care:week2",
          "Milo->Fay:care:week3",
          "Milo->Fay:medicine:week4",
          "Milo->Fay:care:week5",
          "Milo->Fay:care:week6",
          "Milo->Fay:medicine:week7"
        ],
        "tool": "root_satchel",
        "tool_affinity": 0.63705
      },
      "Milo": {
        "agent_id": "Milo",
        "autonomy": 0.565,
        "career_identity": [
          "I am learning the route_keeper path.",
          "I am becoming route_keeper through routing.",
          "I am becoming route_keeper through teaching."
        ],
        "career_memories": [
          "week 0: schedule memory guided routing",
          "week 1: schedule memory guided teaching",
          "week 2: schedule memory guided routing",
          "week 3: schedule memory guided routing",
          "week 4: schedule memory guided teaching",
          "week 5: schedule memory guided routing",
          "week 6: schedule memory guided routing",
          "week 7: schedule memory guided teaching"
        ],
        "fatigue": 0.4430000000000005,
        "last_mentor": "Ari",
        "last_skill": "teaching",
        "primary_skill": "routing",
        "role": "route_keeper",
        "skills": {
          "care": 0.28,
          "construction": 0.28,
          "medicine": 0.28,
          "repair": 0.28,
          "routing": 0.9050000000000002,
          "teaching": 0.5750000000000001
        },
        "source_schedule_memories": 18,
        "teaching_lineage": [
          "Ari->Milo:routing:week0",
          "Ari->Milo:teaching:week1",
          "Ari->Milo:routing:week2",
          "Ari->Milo:routing:week3",
          "Ari->Milo:teaching:week4",
          "Ari->Milo:routing:week5",
          "Ari->Milo:routing:week6",
          "Ari->Milo:teaching:week7"
        ],
        "tool": "path_chisel",
        "tool_affinity": 0.63405
      }
    },
    "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
    "events": [
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 0,
        "event_id": 0,
        "flower_node": "work_petal",
        "frequency_hz": 0.242,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 1,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.585,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 2,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.660019
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle0",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 9,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 0,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.660019,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "7d1dad37e3fd3b68"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 0,
        "event_id": 1,
        "flower_node": "root_rest",
        "frequency_hz": 0.219,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 1,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.6075,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 2,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.716728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle0",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 9,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 0,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.716728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "f410c93718dc94a4"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 0,
        "event_id": 2,
        "flower_node": "social_petal",
        "frequency_hz": 0.258,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 1,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.59625,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 2,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.716114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle0",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 9,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 0,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.716114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "6fac87b8e57fc7ce"
      },
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 1,
        "event_id": 3,
        "flower_node": "work_petal",
        "frequency_hz": 0.2435,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 2,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.62,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 4,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.672019
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle1",
            "remedial": true,
            "violation": true
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 10,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 1,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.672019,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "2772b95dff6752f8"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 1,
        "event_id": 4,
        "flower_node": "root_rest",
        "frequency_hz": 0.2205,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 2,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.6425,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 4,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.728728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle1",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 10,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 1,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.728728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "481077fbd9f9f08d"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 1,
        "event_id": 5,
        "flower_node": "social_petal",
        "frequency_hz": 0.2595,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 2,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.63125,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 4,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.728114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle1",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 10,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 1,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.728114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "04f9d557b4e2bd43"
      },
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 2,
        "event_id": 6,
        "flower_node": "work_petal",
        "frequency_hz": 0.245,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 3,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.655,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 6,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.702919
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle2",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Fay",
            "lineage_marks": 12,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 2,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.702919,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "bb445119b854e393"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 2,
        "event_id": 7,
        "flower_node": "root_rest",
        "frequency_hz": 0.222,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 3,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.6775,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 6,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.740728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle2",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Milo",
            "lineage_marks": 12,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 2,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.740728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "af0cab3a1f20570f"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 2,
        "event_id": 8,
        "flower_node": "social_petal",
        "frequency_hz": 0.261,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 3,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.66625,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 6,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.740114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle2",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Ari",
            "lineage_marks": 12,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 2,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.740114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "9f8e22075b0abf2e"
      },
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 3,
        "event_id": 9,
        "flower_node": "work_petal",
        "frequency_hz": 0.2465,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 4,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.69,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 8,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.714919
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle3",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 13,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 3,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.714919,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "5d7d487e8381f4ed"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 3,
        "event_id": 10,
        "flower_node": "root_rest",
        "frequency_hz": 0.2235,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 4,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.7125,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 8,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.752728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle3",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 13,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 3,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.752728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "84872d4dba705a74"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 3,
        "event_id": 11,
        "flower_node": "social_petal",
        "frequency_hz": 0.2625,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 4,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.70125,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 8,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.752114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle3",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 13,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 3,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.752114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "66da52b5db68f700"
      },
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 4,
        "event_id": 12,
        "flower_node": "work_petal",
        "frequency_hz": 0.248,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 5,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.725,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 10,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.726919
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle4",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 14,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 4,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.726919,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "7a0b066545f0e664"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 4,
        "event_id": 13,
        "flower_node": "root_rest",
        "frequency_hz": 0.225,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 5,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.7475,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 10,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.764728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle4",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 14,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 4,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.764728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "d6eb428ff74ffbdf"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 4,
        "event_id": 14,
        "flower_node": "social_petal",
        "frequency_hz": 0.264,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 5,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.73625,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 10,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.764114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle4",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": null,
            "lineage_marks": 14,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 4,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.764114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "717a8d38eb549159"
      },
      {
        "agent_id": "Ari",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 5,
        "event_id": 15,
        "flower_node": "work_petal",
        "frequency_hz": 0.2495,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 6,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Shelterwrights",
            "reputation": 0.76,
            "standard": "sealed_joint"
          },
          "memory": {
            "guild_memory_count": 12,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.738919
          },
          "standards": {
            "craft_mark": "sealed_joint@resonant_mallet:cycle5",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Fay",
            "lineage_marks": 16,
            "name": "resonant_mallet",
            "owner": "Ari",
            "quality": 0.652062
          }
        },
        "replay_frame": {
          "agent_id": "Ari",
          "cycle": 5,
          "flower_node": "work_petal",
          "frequency_hz": 0.242,
          "guild": "Shelterwrights",
          "quality": 0.738919,
          "standard": "sealed_joint",
          "tool": "resonant_mallet"
        },
        "trace_hash": "7f5e6fe5747b305b"
      },
      {
        "agent_id": "Fay",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 5,
        "event_id": 16,
        "flower_node": "root_rest",
        "frequency_hz": 0.2265,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 6,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Rootkeepers",
            "reputation": 0.7825,
            "standard": "clean_care_bundle"
          },
          "memory": {
            "guild_memory_count": 12,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.776728
          },
          "standards": {
            "craft_mark": "clean_care_bundle@root_satchel:cycle5",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Milo",
            "lineage_marks": 16,
            "name": "root_satchel",
            "owner": "Fay",
            "quality": 0.65282
          }
        },
        "replay_frame": {
          "agent_id": "Fay",
          "cycle": 5,
          "flower_node": "root_rest",
          "frequency_hz": 0.219,
          "guild": "Rootkeepers",
          "quality": 0.776728,
          "standard": "clean_care_bundle",
          "tool": "root_satchel"
        },
        "trace_hash": "b143fc1be8879beb"
      },
      {
        "agent_id": "Milo",
        "claim_boundary": {
          "complete_3d_world": false,
          "moral_patienthood": false,
          "real_credentialing": false,
          "real_labor": false,
          "subjective_consciousness": false,
          "subjective_vocation": false
        },
        "condition": "integrated_guild_memory_craft_standards_tool_inheritance",
        "cycle": 5,
        "event_id": 17,
        "flower_node": "social_petal",
        "frequency_hz": 0.2655,
        "private_workspace": {
          "hidden": true
        },
        "private_workspace_hidden": true,
        "public_packets": {
          "certificate": {
            "count": 6,
            "issued": true
          },
          "guild": {
            "certified": true,
            "name": "Pathmarkers",
            "reputation": 0.77125,
            "standard": "safe_waymark"
          },
          "memory": {
            "guild_memory_count": 12,
            "source_career_memories": 8,
            "source_lineage_marks": 8
          },
          "quality": {
            "evaluated": true,
            "score": 0.776114
          },
          "standards": {
            "craft_mark": "safe_waymark@path_chisel:cycle5",
            "remedial": false,
            "violation": false
          },
          "tool": {
            "inherited_to": "Ari",
            "lineage_marks": 16,
            "name": "path_chisel",
            "owner": "Milo",
            "quality": 0.652604
          }
        },
        "replay_frame": {
          "agent_id": "Milo",
          "cycle": 5,
          "flower_node": "social_petal",
          "frequency_hz": 0.258,
          "guild": "Pathmarkers",
          "quality": 0.776114,
          "standard": "safe_waymark",
          "tool": "path_chisel"
        },
        "trace_hash": "486638cddeb52c06"
      }
    ],
    "guild_kernel": {
      "apprentice_cohort": true,
      "browser_replay": true,
      "certification": true,
      "craft_mark": true,
      "craft_standards": true,
      "frequency_flower_binding": true,
      "guild_memory": true,
      "intergenerational_memory": true,
      "lineage_trace": true,
      "name": "integrated_guild_memory_craft_standards_tool_inheritance",
      "privacy_filter": true,
      "quality_evaluation": true,
      "remedial_training": true,
      "reputation_binding": true,
      "tool_inheritance": true,
      "violation_detection": true
    },
    "guilds": {
      "Ari": {
        "certificates": [
          "Shelterwrights:Ari:sealed_joint:cycle0",
          "Shelterwrights:Ari:sealed_joint:cycle1",
          "Shelterwrights:Ari:sealed_joint:cycle2",
          "Shelterwrights:Ari:sealed_joint:cycle3",
          "Shelterwrights:Ari:sealed_joint:cycle4",
          "Shelterwrights:Ari:sealed_joint:cycle5"
        ],
        "certified": true,
        "craft_marks": [
          "week 0: Ari practiced repair",
          "week 1: Ari practiced construction",
          "sealed_joint@resonant_mallet:cycle0",
          "sealed_joint@resonant_mallet:cycle1",
          "sealed_joint@resonant_mallet:cycle2",
          "sealed_joint@resonant_mallet:cycle3",
          "sealed_joint@resonant_mallet:cycle4",
          "sealed_joint@resonant_mallet:cycle5"
        ],
        "guild": "Shelterwrights",
        "guild_memory": [
          "cycle 0: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 0",
          "cycle 1: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 1",
          "cycle 2: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 2",
          "cycle 3: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 3",
          "cycle 4: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 4",
          "cycle 5: Ari submitted sealed_joint",
          "generation memory: Ari entrusted sealed_joint in cycle 5"
        ],
        "inherited_tools": [
          "resonant_mallet->Fay:cycle2",
          "resonant_mallet->Fay:cycle5"
        ],
        "remediation": [
          "cycle 1: remedial practice in repair"
        ],
        "reputation": 0.7600000000000001,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "sealed_joint",
        "violations": [
          "cycle 1: revise sealed_joint"
        ]
      },
      "Fay": {
        "certificates": [
          "Rootkeepers:Fay:clean_care_bundle:cycle0",
          "Rootkeepers:Fay:clean_care_bundle:cycle1",
          "Rootkeepers:Fay:clean_care_bundle:cycle2",
          "Rootkeepers:Fay:clean_care_bundle:cycle3",
          "Rootkeepers:Fay:clean_care_bundle:cycle4",
          "Rootkeepers:Fay:clean_care_bundle:cycle5"
        ],
        "certified": true,
        "craft_marks": [
          "week 0: Fay practiced care",
          "week 1: Fay practiced medicine",
          "clean_care_bundle@root_satchel:cycle0",
          "clean_care_bundle@root_satchel:cycle1",
          "clean_care_bundle@root_satchel:cycle2",
          "clean_care_bundle@root_satchel:cycle3",
          "clean_care_bundle@root_satchel:cycle4",
          "clean_care_bundle@root_satchel:cycle5"
        ],
        "guild": "Rootkeepers",
        "guild_memory": [
          "cycle 0: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 0",
          "cycle 1: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 1",
          "cycle 2: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 2",
          "cycle 3: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 3",
          "cycle 4: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 4",
          "cycle 5: Fay submitted clean_care_bundle",
          "generation memory: Fay entrusted clean_care_bundle in cycle 5"
        ],
        "inherited_tools": [
          "root_satchel->Milo:cycle2",
          "root_satchel->Milo:cycle5"
        ],
        "remediation": [],
        "reputation": 0.7825000000000002,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "clean_care_bundle",
        "violations": []
      },
      "Milo": {
        "certificates": [
          "Pathmarkers:Milo:safe_waymark:cycle0",
          "Pathmarkers:Milo:safe_waymark:cycle1",
          "Pathmarkers:Milo:safe_waymark:cycle2",
          "Pathmarkers:Milo:safe_waymark:cycle3",
          "Pathmarkers:Milo:safe_waymark:cycle4",
          "Pathmarkers:Milo:safe_waymark:cycle5"
        ],
        "certified": true,
        "craft_marks": [
          "week 0: Milo practiced routing",
          "week 1: Milo practiced teaching",
          "safe_waymark@path_chisel:cycle0",
          "safe_waymark@path_chisel:cycle1",
          "safe_waymark@path_chisel:cycle2",
          "safe_waymark@path_chisel:cycle3",
          "safe_waymark@path_chisel:cycle4",
          "safe_waymark@path_chisel:cycle5"
        ],
        "guild": "Pathmarkers",
        "guild_memory": [
          "cycle 0: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 0",
          "cycle 1: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 1",
          "cycle 2: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 2",
          "cycle 3: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 3",
          "cycle 4: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 4",
          "cycle 5: Milo submitted safe_waymark",
          "generation memory: Milo entrusted safe_waymark in cycle 5"
        ],
        "inherited_tools": [
          "path_chisel->Ari:cycle2",
          "path_chisel->Ari:cycle5"
        ],
        "remediation": [],
        "reputation": 0.7712500000000002,
        "source_career_memories": 8,
        "source_lineage_marks": 8,
        "standard": "safe_waymark",
        "violations": []
      }
    },
    "source_condition": "integrated_multi_week_apprenticeship_skill_transfer_tool_career",
    "tools": {
      "path_chisel": {
        "lineage_marks": [
          "week 0: Milo practiced routing",
          "week 1: Milo practiced teaching",
          "week 2: Milo practiced routing",
          "week 3: Milo practiced routing",
          "week 4: Milo practiced teaching",
          "week 5: Milo practiced routing",
          "week 6: Milo practiced routing",
          "week 7: Milo practiced teaching",
          "safe_waymark@path_chisel:cycle0",
          "safe_waymark@path_chisel:cycle1",
          "safe_waymark@path_chisel:cycle2",
          "inheritance:Milo->Ari:cycle2",
          "safe_waymark@path_chisel:cycle3",
          "safe_waymark@path_chisel:cycle4",
          "safe_waymark@path_chisel:cycle5",
          "inheritance:Milo->Ari:cycle5"
        ],
        "owner": "Milo",
        "quality": 0.6526039
      },
      "resonant_mallet": {
        "lineage_marks": [
          "week 0: Ari practiced repair",
          "week 1: Ari practiced construction",
          "week 2: Ari practiced teaching",
          "week 3: Ari practiced repair",
          "week 4: Ari practiced construction",
          "week 5: Ari practiced teaching",
          "week 6: Ari practiced repair",
          "week 7: Ari practiced construction",
          "sealed_joint@resonant_mallet:cycle0",
          "sealed_joint@resonant_mallet:cycle1",
          "sealed_joint@resonant_mallet:cycle2",
          "inheritance:Ari->Fay:cycle2",
          "sealed_joint@resonant_mallet:cycle3",
          "sealed_joint@resonant_mallet:cycle4",
          "sealed_joint@resonant_mallet:cycle5",
          "inheritance:Ari->Fay:cycle5"
        ],
        "owner": "Ari",
        "quality": 0.6520624960000001
      },
      "root_satchel": {
        "lineage_marks": [
          "week 0: Fay practiced care",
          "week 1: Fay practiced medicine",
          "week 2: Fay practiced care",
          "week 3: Fay practiced care",
          "week 4: Fay practiced medicine",
          "week 5: Fay practiced care",
          "week 6: Fay practiced care",
          "week 7: Fay practiced medicine",
          "clean_care_bundle@root_satchel:cycle0",
          "clean_care_bundle@root_satchel:cycle1",
          "clean_care_bundle@root_satchel:cycle2",
          "inheritance:Fay->Milo:cycle2",
          "clean_care_bundle@root_satchel:cycle3",
          "clean_care_bundle@root_satchel:cycle4",
          "clean_care_bundle@root_satchel:cycle5",
          "inheritance:Fay->Milo:cycle5"
        ],
        "owner": "Fay",
        "quality": 0.6528199
      }
    }
  },
  "moral_boundary": {
    "craft_standards_not_subjective_status": true,
    "guild_certification_not_real_credentialing": true,
    "no_moral_patienthood_claim": true,
    "no_subjective_consciousness_claim": true,
    "private_workspace_not_debug_leaked": true,
    "tool_inheritance_not_moral_status": true
  },
  "source_condition": "integrated_multi_week_apprenticeship_skill_transfer_tool_career",
  "trace_events": 18
};
