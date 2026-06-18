# Report 361: Browser World v121 Primary Shell Echo-Influenced Choice Refusal

Report 361 keeps the work in the maintained v61 browser shell and makes Fay's bounded echo conversation affect a later resident-facing choice. After Fay carries Milo's accountability echo and answers through the phrasebook-only `Talk` path, `Offer help` now creates an Echo choice receipt: Fay accepts source-bounded help for the remembered obligation while refusing to rewrite the original cause chain or treat the avatar as a direct source command.

Boundary: Browser-local echo-influenced choice/refusal over the maintained v61 shell only; phrasebook-only receipts, no LLM call, no autonomous natural language, no subjective consciousness, no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, no finished gameplay, and no metaphysical claim.

## Result

Verdict: `pass`
Readiness: `1.000`
Weakest channel score: `1.000`
Criteria passed: `20 / 20`

## Browser-smoke evidence

- Maintained shell URL: `http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?report=361&reload=1`
- Before choice: `No echo-influenced choice yet.`
- After choice: `Resident: Fay
Action: offer_help
Choice: accept_source_bounded_help
Refusal: refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory
Source echo: milo-offscreen-water-jars
Source preserved: yes
Direct avatar command: no
No LLM: yes
Autonomous language: no
Phrasebook only: yes
Recoverable: yes`
- After reload: `Resident: Fay
Action: offer_help
Choice: accept_source_bounded_help
Refusal: refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory
Source echo: milo-offscreen-water-jars
Source preserved: yes
Direct avatar command: no
No LLM: yes
Autonomous language: no
Phrasebook only: yes
Recoverable: yes`
- Console errors: `0`

## Criteria

| Criterion | Score | Evidence |
| --- | ---: | --- |
| `report_360_bounded_conversation_gate_passing` | `1.0` | Report 360 verdict=pass weakest=1.0 |
| `source_exposes_echo_choice_state` | `1.0` | app.js exposes echo-influenced choice state, renderer, builder, and boundary |
| `source_binds_choice_to_offer_help` | `1.0` | offerHelp creates a source-aware receipt when the bounded conversation exists |
| `source_preserves_attribution_and_refusal` | `1.0` | choice receipt preserves source attribution and records bounded refusal |
| `visible_echo_choice_panel_wired` | `1.0` | index.html exposes Echo choice dashboard panel |
| `public_state_boundary_includes_echo_choice` | `1.0` | state-boundary audit public world includes echo choice receipt |
| `browser_smoke_artifact_exists` | `1.0` | artifacts/ssrm_3d_browser_world_v121_primary_shell_echo_influenced_choice_refusal_browser_smoke.json |
| `browser_smoke_used_maintained_shell` | `1.0` | http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?report=361&reload=1 |
| `before_choice_empty_after_conversation` | `1.0` | No echo-influenced choice yet. |
| `choice_created_by_fay_offer_help` | `1.0` | choice={'resident': 'Fay', 'action': 'offer_help', 'choice': 'accept_source_bounded_help', 'refusal': "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory", 'sourceEchoId': 'milo-offscreen-water-jars', 'sourceAttributionPreserved': True, 'directAvatarCommand': False, 'noLLM': True, 'autonomousLanguage': False, 'phrasebookOnly': True, 'recoverable': True} |
| `visible_choice_accepts_help_and_refuses_rewrite` | `1.0` | Resident: Fay
Action: offer_help
Choice: accept_source_bounded_help
Refusal: refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory
Source echo: milo-offscreen-water-jars
Source preserved: yes
Direct avatar command: no
No LLM: yes
Autonomous language: no
Phrasebook only: yes
Recoverable: yes |
| `visible_choice_preserves_source_and_not_command` | `1.0` | Resident: Fay
Action: offer_help
Choice: accept_source_bounded_help
Refusal: refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory
Source echo: milo-offscreen-water-jars
Source preserved: yes
Direct avatar command: no
No LLM: yes
Autonomous language: no
Phrasebook only: yes
Recoverable: yes |
| `choice_boundary_flags_preserved` | `1.0` | choice={'resident': 'Fay', 'action': 'offer_help', 'choice': 'accept_source_bounded_help', 'refusal': "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory", 'sourceEchoId': 'milo-offscreen-water-jars', 'sourceAttributionPreserved': True, 'directAvatarCommand': False, 'noLLM': True, 'autonomousLanguage': False, 'phrasebookOnly': True, 'recoverable': True} |
| `resident_history_records_choice_refusal` | `1.0` |   Ari now: debt 1 / trust 0.593 / progress 0.396 / memory: recognized returning avatar; follow-up opened: Ari wants the avatar to check the awning repair after returning
  t5 return recognition: recognized avatar returning through arrival court -> debt 1 trust 0.589 progress 0.384
  t5 promise follow-up: opened remembered obligation after 1 return(s) -> debt 1 trust 0.593 progress 0.396
  t6 resident social memory: Fay: Fay remembered the awning cloth and checked Ari's repair -> debt 1 trust 0.593 progress 0.396
  t6 resident social memory witness: Nia: Ari repaired the shelf Nia uses at dawn -> debt 1 trust 0.593 progress 0.396
* Fay now: debt 0 / trust 0.674 / progress 0.560 / memory: accepted source-bounded help for milo-offscreen-water-jars; refused history rewrite
  t8 bounded echo conversation: Fay says: I heard Milo say milo-offscreen-water-jars stayed resolved/resolved; avatar absence accounted.; no LLM true; phrasebook only true -> debt 0 trust 0.638 progress 0.525
  t8 state update: bounded echo reply referenced milo-offscreen-water-jars -> debt 0 trust 0.65 progress 0.525
  t9 echo-influenced choice/refusal: Fay accepts help only for milo-offscreen-water-jars follow-up and refuses history rewrite; source attribution preserved yes; no LLM true; recoverable true -> debt 0 trust 0.65 progress 0.525
  t9 state update: accepted source-bounded help for milo-offscreen-water-jars; refused history rewrite -> debt 0 trust 0.674 progress 0.56
  Milo now: debt 2 / trust 0.507 / progress 0.314 / memory: return greeting linked milo-offscreen-water-jars and accounted avatar absence
  t5 accountability return greeting: Milo remembers milo-offscreen-water-jars was resolved and your absence was accounted; history preserved yes -> debt 2 trust 0.507 progress 0.314
  t6 resident social memory witness: Fay: Milo carried herb crates before rain -> debt 2 trust 0.507 progress 0.314
  t6 resident social memory: Sera: Sera kept water jars safe for Milo -> debt 2 trust 0.507 progress 0.314
  t6 accountability social echo source: Fay: Fay heard Milo say milo-offscreen-water-jars stayed resolved/resolved and the avatar absence was accounted; preserving Fay changed Milo's obligation while avatar absent -> debt 2 trust 0.507 progress 0.314
  Sera now: debt 1 / trust 0.542 / progress 0.447 / memory: asked for quiet
  t1 state update: trust/debt/progress changed -> debt 1 trust 0.542 progress 0.447
  t6 resident social memory witness: Milo: Sera kept water jars safe for Milo -> debt 1 trust 0.542 progress 0.447
  t6 resident social memory: Tovan: Tovan marked the quiet drying route -> debt 1 trust 0.542 progress 0.447
  Tovan now: debt 1 / trust 0.509 / progress 0.420 / memory: keeps route tokens
  t1 state update: trust/debt/progress changed -> debt 1 trust 0.509 progress 0.42
  t6 resident social memory witness: Sera: Tovan marked the quiet drying route -> debt 1 trust 0.509 progress 0.42
  t6 resident social memory: Nia: Nia sorted route tokens without losing names -> debt 1 trust 0.509 progress 0.42
  Nia now: debt 0 / trust 0.612 / progress 0.503 / memory: remembers quiet greeting
  t1 state update: trust/debt/progress changed -> debt 0 trust 0.612 progress 0.503
  t6 resident social memory witness: Tovan: Nia sorted route tokens without losing names -> debt 0 trust 0.612 progress 0.503
  t6 resident social memory: Ari: Ari repaired the shelf Nia uses at dawn -> debt 0 trust 0.612 progress 0.503 |
| `relationship_memory_still_carries_original_echo` | `1.0` | Selected tie: Fay -> Milo / trust 0.528 / debt 0 / memory: Milo carried herb crates before rain
Persistent key: ssrm_v61_app_shell_resident_relationships
Public resident-to-resident network:
  Ari -> Fay / trust 0.572 / debt 1 / memory: Fay remembered the awning cloth and checked Ari's repair
* Fay -> Milo / trust 0.528 / debt 0 / memory: Milo carried herb crates before rain
  Milo -> Sera / trust 0.502 / debt 1 / memory: Sera kept water jars safe for Milo
  Milo -> Fay / trust 0.514 / debt 0 / memory: Fay heard Milo say milo-offscreen-water-jars stayed resolved/resolved and the avatar absence was accounted; preserving Fay changed Milo's obligation while avatar absent
  Sera -> Tovan / trust 0.558 / debt 1 / memory: Tovan marked the quiet drying route
  Tovan -> Nia / trust 0.512 / debt 1 / memory: Nia sorted route tokens without losing names
  Nia -> Ari / trust 0.578 / debt 0 / memory: Ari repaired the shelf Nia uses at dawn |
| `replay_logs_offer_help_payload` | `1.0` | replayHasEchoChoice=True trace={
  "latest": {
    "event": "offerHelp",
    "tick": 9,
    "selected": "Fay",
    "room": "arrival court",
    "payload": {
      "care": 4,
      "echoInfluencedChoiceReceipt": {
        "reportIntroduced": 361,
        "resident": "Fay",
        "action": "offer_help",
        "choice": "accept_source_bounded_help",
        "refusal": "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory",
        "visibleStatus": "Fay accepts help only for milo-offscreen-water-jars follow-up and refuses history rewrite; source attribution preserved yes",
        "sourceEchoId": "milo-offscreen-water-jars",
        "sourceResident": "Milo",
        "echoResident": "Fay",
        "sourceAttributionPreserved": true,
        "directAvatarCommand": false,
        "noLLM": true,
        "autonomousLanguage": false,
        "phrasebookOnly": true,
        "recoverable": true,
        "boundary": "browser-local-echo-influenced-choice-refusal-only"
      },
      "noLLM": true,
      "autonomousLanguage": false,
      "phrasebookOnly": true
    }
  },
  "world": {
    "entered": true,
    "tick": 10,
    "avatar": {
      "room": "arrival court",
      "x": 180,
      "y": 260
    },
    "selected": "Fay",
    "audit": false,
    "residents": {
      "Ari": {
        "trust": 0.593,
        "debt": 1,
        "schedule": "follow-up opened: check awning repair",
        "memory": "recognized returning avatar; follow-up opened: Ari wants the avatar to check the awning repair after returning",
        "progress": 0.396
      },
      "Fay": {
        "trust": 0.674,
        "debt": 0,
        "schedule": "sort herbs",
        "memory": "accepted source-bounded help for milo-offscreen-water-jars; refused history rewrite",
        "progress": 0.56
      },
      "Milo": {
        "trust": 0.507,
        "debt": 2,
        "schedule": "follow-up resolved: awning repair checked",
        "memory": "return greeting linked milo-offscreen-water-jars and accounted avatar absence",
        "progress": 0.31400000000000006
      },
      "Sera": {
        "trust": 0.542,
        "debt": 1,
        "schedule": "dry cloaks",
        "memory": "asked for quiet",
        "progress": 0.447
      },
      "Tovan": {
        "trust": 0.509,
        "debt": 1,
        "schedule": "map safe route",
        "memory": "keeps route tokens",
        "progress": 0.42000000000000004
      },
      "Nia": {
        "trust": 0.612,
        "debt": 0,
        "schedule": "sort glass jars",
        "memory": "remembers quiet greeting",
        "progress": 0.503
      }
    },
    "resources": {
      "water": 12,
      "fiber": 10,
      "wood": 17,
      "care": 4
    },
    "replay": [
      {
        "event": "enterWorld",
        "tick": 0,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "boundary": "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.",
          "returningVisit": false,
          "returnContinuity": null,
          "returnGreetingContinuity": null,
          "promiseFollowUp": null
        }
      },
      {
        "event": "waitOffscreen",
        "tick": 1,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "offscreenLife": true,
          "offscreenObligation": {
            "reportIntroduced": 354,
            "actor": "Fay",
            "target": "Milo",
            "obligationId": "milo-offscreen-water-jars",
            "replayRowsBeforeEvent": 1,
            "linkedLedger": {
              "scheduleRow": {
                "id": "milo-offscreen-water-jars",
                "reportIntroduced": 353,
                "resident": "Milo",
                "status": "pending",
                "action": "offscreen-resident-action",
                "schedule": "offscreen obligation: inspect leaking water jars",
                "obligation": "Fay found leaking water jars while the avatar was absent",
                "visibleStatus": "Milo schedule pending: offscreen obligation: inspect leaking water jars",
                "boundary": "browser-local-obligation-schedule-queue-only"
              },
              "debtRow": {
                "id": "milo-offscreen-water-jars",
                "reportIntroduced": 353,
                "resident": "Milo",
                "status": "outstanding",
                "action": "offscreen-resident-action",
                "debtAfter": 3,
                "trustAfter": 0.475,
                "obligation": "Fay found leaking water jars while the avatar was absent",
                "visibleStatus": "Milo debt outstanding: 3 after offscreen-resident-action",
                "boundary": "browser-local-obligation-debt-ledger-only"
              }
            },
            "persistedIn": "ssrm_v61_app_shell_world",
            "boundary": "browser-local-offscreen-cross-resident-obligation-event-only"
          },
          "absentTimeSummary": {
            "reportIntroduced": 355,
            "phase": "before-obligation-choice",
            "avatarCaused": [
              "avatar chose Wait offscreen at replay row 1",
              "avatar did not choose the new obligation target"
            ],
            "residentCaused": [
              "Fay changed Milo's obligation while avatar absent",
              "milo-offscreen-water-jars is open / offscreen-pending"
            ],
            "beforeChoice": "Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding",
            "obligationId": "milo-offscreen-water-jars",
            "actor": "Fay",
            "target": "Milo",
            "scheduleQueueStatus": "pending",
            "debtLedgerStatus": "outstanding",
            "boundary": "browser-local-absent-time-summary-only"
          }
        }
      },
      {
        "event": "chooseAbsentTimeThread",
        "tick": 2,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "chosen": true,
          "absentTimeChoiceReceipt": {
            "reportIntroduced": 356,
            "phase": "thread-choice-recorded",
            "chosenThreadId": "milo-offscreen-water-jars",
            "chosenSource": "resident-caused",
            "chosenAction": "handle resident-caused offscreen obligation first",
            "unchosenThreadIds": [
              "avatar-absence-thread"
            ],
            "unchosenThreadStatus": [
              "avatar-absence-thread: pending"
            ],
            "visibleStatus": "resident-caused chosen first; unchosen remains avatar-absence-thread pending",
            "boundary": "browser-local-absent-time-choice-receipt-only"
          },
          "absentTimeThreads": [
            {
              "id": "avatar-absence-thread",
              "reportIntroduced": 356,
              "source": "avatar-caused",
              "status": "accounted",
              "label": "avatar chose Wait offscreen and must decide whether to account for absence first",
              "boundary": "browser-local-absent-time-choice-thread-only"
            },
            {
              "id": "milo-offscreen-water-jars",
              "reportIntroduced": 356,
              "source": "resident-caused",
              "status": "resolved",
              "label": "Fay changed Milo's obligation while avatar absent",
              "obligationStatus": "open",
              "boundary": "browser-local-absent-time-choice-thread-only"
            }
          ],
          "boundary": "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim."
        }
      },
      {
        "event": "resolveSelectedObligation",
        "tick": 3,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "resolved": true,
          "obligation": {
            "id": "milo-offscreen-water-jars",
            "reportIntroduced": 354,
            "resident": "Milo",
            "actor": "Fay",
            "source": "offscreen-resident-action",
            "obligation": "Fay found leaking water jars while the avatar was absent",
            "stage": "resolved",
            "status": "resolved",
            "selected": false,
            "returnCount": 0,
            "visibleStatus": "Milo obligation resolved by avatar help: Fay found leaking water jars while the avatar was absent",
            "boundary": "browser-local-offscreen-cross-resident-obligation-only",
            "scheduleQueueStatus": "resolved",
            "debtLedgerStatus": "settled",
            "scheduleAfter": "follow-up resolved: awning repair checked",
            "debtAfter": 2,
            "resolution": "avatar resolved selected follow-up through bounded help action",
            "resolvedAtTick": 3
          },
          "linkedLedger": {
            "scheduleRow": {
              "id": "milo-offscreen-water-jars",
              "reportIntroduced": 353,
              "resident": "Milo",
              "status": "resolved",
              "action": "resolve",
              "schedule": "follow-up resolved: awning repair checked",
              "obligation": "Fay found leaking water jars while the avatar was absent",
              "visibleStatus": "Milo schedule resolved: follow-up resolved: awning repair checked",
              "boundary": "browser-local-obligation-schedule-queue-only"
            },
            "debtRow": {
              "id": "milo-offscreen-water-jars",
              "reportIntroduced": 353,
              "resident": "Milo",
              "status": "settled",
              "action": "resolve",
              "debtAfter": 2,
              "trustAfter": 0.493,
              "obligation": "Fay found leaking water jars while the avatar was absent",
              "visibleStatus": "Milo debt settled: 2 after resolve",
              "boundary": "browser-local-obligation-debt-ledger-only"
            }
          },
          "absentTimeChoiceReceipt": {
            "reportIntroduced": 356,
            "phase": "obligation-action-recorded",
            "chosenThreadId": "milo-offscreen-water-jars",
            "chosenSource": "resident-caused",
            "chosenAction": "resolve",
            "unchosenThreadIds": [
              "avatar-absence-thread"
            ],
            "unchosenThreadStatus": [
              "avatar-absence-thread: pending"
            ],
            "residentThreadStatus": "resolved",
            "avatarAbsenceStatus": "pending",
            "scheduleQueueStatus": "resolved",
            "debtLedgerStatus": "settled",
            "visibleStatus": "resident-caused offscreen obligation resolve; avatar-caused absence thread pending",
            "boundary": "browser-local-absent-time-choice-receipt-only"
          },
          "boundedAction": true,
          "boundary": "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim."
        }
      },
      {
        "event": "accountForAvatarAbsence",
        "tick": 4,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "accounted": true,
          "avatarAbsenceAccountabilityReceipt": {
            "reportIntroduced": 357,
            "phase": "avatar-absence-accounted",
            "avatarThreadId": "avatar-absence-thread",
            "avatarThreadStatus": "accounted",
            "residentThreadId": "milo-offscreen-water-jars",
            "residentThreadStatus": "resolved",
            "residentObligationStatus": "resolved",
            "residentObligationStage": "resolved",
            "residentHistoryPreserved": true,
            "careAfter": 5,
            "visibleStatus": "avatar-caused absence accounted; resident-caused milo-offscreen-water-jars remains resolved with obligation resolved/resolved",
            "boundary": "browser-local-avatar-absence-accountability-receipt-only"
          },
          "absentTimeThreads": [
            {
              "id": "avatar-absence-thread",
              "reportIntroduced": 356,
              "source": "avatar-caused",
              "status": "accounted",
              "label": "avatar chose Wait offscreen and must decide whether to account for absence first",
              "boundary": "browser-local-absent-time-choice-thread-only"
            },
            {
              "id": "milo-offscreen-water-jars",
              "reportIntroduced": 356,
              "source": "resident-caused",
              "status": "resolved",
              "label": "Fay changed Milo's obligation while avatar absent",
              "obligationStatus": "open",
              "boundary": "browser-local-absent-time-choice-thread-only"
            }
          ],
          "boundary": "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim."
        }
      },
      {
        "event": "enterWorld",
        "tick": 5,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "boundary": "Deterministic browser-local hardened vertical-slice app shell only; no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, production persistence, finished gameplay, complete 3D engine, or metaphysical frequency claim.",
          "returningVisit": true,
          "returnContinuity": {
            "reportIntroduced": 350,
            "resident": "Ari",
            "replayRowsBeforeReturn": 5,
            "memory": "recognized returning avatar after 5 replay row(s)",
            "recognizedAtTick": 5,
            "boundary": "browser-local-return-recognition-public-state-only"
          },
          "returnGreetingContinuity": {
            "reportIntroduced": 358,
            "resident": "Milo",
            "greeting": "Milo remembers milo-offscreen-water-jars was resolved and your absence was accounted",
            "residentThreadId": "milo-offscreen-water-jars",
            "residentObligationStatus": "resolved/resolved",
            "avatarThreadStatus": "accounted",
            "residentHistoryPreserved": true,
            "replayRowsBeforeReturn": 5,
            "boundary": "browser-local-accountability-return-greeting-only"
          },
          "promiseFollowUp": {
            "reportIntroduced": 351,
            "resident": "Ari",
            "obligation": "Ari wants the avatar to check the awning repair after returning",
            "stage": "opened",
            "returnCount": 1,
            "trigger": "return",
            "replayRowsBeforeReturn": 5,
            "advancedAtTick": 5,
            "visibleStatus": "Ari follow-up opened: Ari wants the avatar to check the awning repair after returning (1 return(s))",
            "boundary": "browser-local-public-obligation-thread-only"
          }
        }
      },
      {
        "event": "runSocialMemoryPulse",
        "tick": 6,
        "selected": "Ari",
        "room": "arrival court",
        "payload": {
          "residentToResident": true,
          "pairCount": 6,
          "accountabilitySocialEcho": {
            "reportIntroduced": 359,
            "sourceResident": "Milo",
            "echoResident": "Fay",
            "residentThreadId": "milo-offscreen-water-jars",
            "residentObligationStatus": "resolved/resolved",
            "avatarThreadStatus": "accounted",
            "residentHistoryPreserved": true,
            "directAvatarCommand": false,
            "relationshipTrust": 0.514,
            "echo": "Fay heard Milo say milo-offscreen-water-jars stayed resolved/resolved and the avatar absence was accounted; preserving Fay changed Milo's obligation while avatar absent",
            "boundary": "browser-local-accountability-social-echo-only"
          },
          "persistentKey": "ssrm_v61_app_shell_resident_relationships"
        }
      },
      {
        "event": "selectResident",
        "tick": 7,
        "selected": "Fay",
        "room": "arrival court",
        "payload": {
          "selected": "Fay"
        }
      },
      {
        "event": "talkBounded",
        "tick": 8,
        "selected": "Fay",
        "room": "arrival court",
        "payload": {
          "phrase": "greet",
          "boundedEchoConversation": {
            "reportIntroduced": 360,
            "resident": "Fay",
            "phrase": "greet",
            "reply": "Fay says: I heard Milo say milo-offscreen-water-jars stayed resolved/resolved; avatar absence accounted.",
            "sourceEchoId": "milo-offscreen-water-jars",
            "sourceResident": "Milo",
            "echoResident": "Fay",
            "residentObligationStatus": "resolved/resolved",
            "avatarThreadStatus": "accounted",
            "directAvatarCommand": false,
            "noLLM": true,
            "autonomousLanguage": false,
            "phrasebookOnly": true,
            "boundary": "browser-local-bounded-echo-conversation-only"
          },
          "noLLM": true,
          "autonomousLanguage": false,
          "phrasebookOnly": true
        }
      },
      {
        "event": "offerHelp",
        "tick": 9,
        "selected": "Fay",
        "room": "arrival court",
        "payload": {
          "care": 4,
          "echoInfluencedChoiceReceipt": {
            "reportIntroduced": 361,
            "resident": "Fay",
            "action": "offer_help",
            "choice": "accept_source_bounded_help",
            "refusal": "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory",
            "visibleStatus": "Fay accepts help only for milo-offscreen-water-jars follow-up and refuses history rewrite; source attribution preserved yes",
            "sourceEchoId": "milo-offscreen-water-jars",
            "sourceResident": "Milo",
            "echoResident": "Fay",
            "sourceAttributionPreserved": true,
            "directAvatarCommand": false,
            "noLLM": true,
            "autonomousLanguage": false,
            "phrasebookOnly": true,
            "recoverable": true,
            "boundary": "browser-local-echo-influenced-choice-refusal-only"
          },
          "noLLM": true,
          "autonomousLanguage": false,
          "phrasebookOnly": true
        }
      }
    ],
    "returnContinuity": {
      "reportIntroduced": 350,
      "resident": "Ari",
      "replayRowsBeforeReturn": 5,
      "memory": "recognized returning avatar after 5 replay row(s)",
      "recognizedAtTick": 5,
      "boundary": "browser-local-return-recognition-public-state-only"
    },
    "returnGreetingContinuity": {
      "reportIntroduced": 358,
      "resident": "Milo",
      "greeting": "Milo remembers milo-offscreen-water-jars was resolved and your absence was accounted",
      "residentThreadId": "milo-offscreen-water-jars",
      "residentObligationStatus": "resolved/resolved",
      "avatarThreadStatus": "accounted",
      "residentHistoryPreserved": true,
      "replayRowsBeforeReturn": 5,
      "boundary": "browser-local-accountability-return-greeting-only"
    },
    "accountabilitySocialEcho": {
      "reportIntroduced": 359,
      "sourceResident": "Milo",
      "echoResident": "Fay",
      "residentThreadId": "milo-offscreen-water-jars",
      "residentObligationStatus": "resolved/resolved",
      "avatarThreadStatus": "accounted",
      "residentHistoryPreserved": true,
      "directAvatarCommand": false,
      "relationshipTrust": 0.514,
      "echo": "Fay heard Milo say milo-offscreen-water-jars stayed resolved/resolved and the avatar absence was accounted; preserving Fay changed Milo's obligation while avatar absent",
      "boundary": "browser-local-accountability-social-echo-only"
    },
    "boundedEchoConversation": {
      "reportIntroduced": 360,
      "resident": "Fay",
      "phrase": "greet",
      "reply": "Fay says: I heard Milo say milo-offscreen-water-jars stayed resolved/resolved; avatar absence accounted.",
      "sourceEchoId": "milo-offscreen-water-jars",
      "sourceResident": "Milo",
      "echoResident": "Fay",
      "residentObligationStatus": "resolved/resolved",
      "avatarThreadStatus": "accounted",
      "directAvatarCommand": false,
      "noLLM": true,
      "autonomousLanguage": false,
      "phrasebookOnly": true,
      "boundary": "browser-local-bounded-echo-conversation-only"
    },
    "echoInfluencedChoiceReceipt": {
      "reportIntroduced": 361,
      "resident": "Fay",
      "action": "offer_help",
      "choice": "accept_source_bounded_help",
      "refusal": "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory",
      "visibleStatus": "Fay accepts help only for milo-offscreen-water-jars follow-up and refuses history rewrite; source attribution preserved yes",
      "sourceEchoId": "milo-offscreen-water-jars",
      "sourceResident": "Milo",
      "echoResident": "Fay",
      "sourceAttributionPreserved": true,
      "directAvatarCommand": false,
      "noLLM": true,
      "autonomousLanguage": false,
      "phrasebookOnly": true,
      "recoverable": true,
      "boundary": "browser-local-echo-influenced-choice-refusal-only"
    },
    "promiseFollowUp": {
      "reportIntroduced": 351,
      "resident": "Ari",
      "obligation": "Ari wants the avatar to check the awning repair after returning",
      "stage": "opened",
      "returnCount": 1,
      "trigger": "return",
      "replayRowsBeforeReturn": 5,
      "advancedAtTick": 5,
      "visibleStatus": "Ari follow-up opened: Ari wants the avatar to check the awning repair after returning (1 return(s))",
      "boundary": "browser-local-public-obligation-thread-only"
    },
    "obligationLedger": [
      {
        "id": "milo-offscreen-water-jars",
        "reportIntroduced": 354,
        "resident": "Milo",
        "actor": "Fay",
        "source": "offscreen-resident-action",
        "obligation": "Fay found leaking water jars while the avatar was absent",
        "stage": "resolved",
        "status": "resolved",
        "selected": false,
        "returnCount": 0,
        "visibleStatus": "Milo obligation resolved by avatar help: Fay found leaking water jars while the avatar was absent",
        "boundary": "browser-local-offscreen-cross-resident-obligation-only",
        "scheduleQueueStatus": "resolved",
        "debtLedgerStatus": "settled",
        "scheduleAfter": "follow-up resolved: awning repair checked",
        "debtAfter": 2,
        "resolution": "avatar resolved selected follow-up through bounded help action",
        "resolvedAtTick": 3
      },
      {
        "id": "ari-awning-followup",
        "reportIntroduced": 352,
        "resident": "Ari",
        "obligation": "Ari wants the avatar to check the awning repair after returning",
        "stage": "opened",
        "status": "open",
        "returnCount": 1,
        "selected": true,
        "lastTrigger": "return",
        "lastReplayRowsBeforeReturn": 5,
        "visibleStatus": "Ari obligation open: Ari wants the avatar to check the awning repair after returning / follow-up opened / 1 return(s)",
        "boundary": "browser-local-selectable-obligation-list-only",
        "scheduleQueueStatus": "pending",
        "debtLedgerStatus": "outstanding",
        "scheduleAfter": "follow-up opened: check awning repair",
        "debtAfter": 1
      }
    ],
    "scheduleQueue": [
      {
        "id": "milo-offscreen-water-jars",
        "reportIntroduced": 353,
        "resident": "Milo",
        "status": "resolved",
        "action": "resolve",
        "schedule": "follow-up resolved: awning repair checked",
        "obligation": "Fay found leaking water jars while the avatar was absent",
        "visibleStatus": "Milo schedule resolved: follow-up resolved: awning repair checked",
        "boundary": "browser-local-obligation-schedule-queue-only"
      },
      {
        "id": "ari-awning-followup",
        "reportIntroduced": 353,
        "resident": "Ari",
        "status": "pending",
        "action": "follow-up-opened",
        "schedule": "follow-up opened: check awning repair",
        "obligation": "Ari wants the avatar to check the awning repair after returning",
        "visibleStatus": "Ari schedule pending: follow-up opened: check awning repair",
        "boundary": "browser-local-obligation-schedule-queue-only"
      }
    ],
    "debtLedger": [
      {
        "id": "milo-offscreen-water-jars",
        "reportIntroduced": 353,
        "resident": "Milo",
        "status": "settled",
        "action": "resolve",
        "debtAfter": 2,
        "trustAfter": 0.493,
        "obligation": "Fay found leaking water jars while the avatar was absent",
        "visibleStatus": "Milo debt settled: 2 after resolve",
        "boundary": "browser-local-obligation-debt-ledger-only"
      },
      {
        "id": "ari-awning-followup",
        "reportIntroduced": 353,
        "resident": "Ari",
        "status": "outstanding",
        "action": "follow-up-opened",
        "debtAfter": 1,
        "trustAfter": 0.593,
        "obligation": "Ari wants the avatar to check the awning repair after returning",
        "visibleStatus": "Ari debt outstanding: 1 after follow-up-opened",
        "boundary": "browser-local-obligation-debt-ledger-only"
      }
    ],
    "offscreenObligationEvents": [
      {
        "reportIntroduced": 354,
        "actor": "Fay",
        "target": "Milo",
        "obligationId": "milo-offscreen-water-jars",
        "replayRowsBeforeEvent": 1,
        "linkedLedger": {
          "scheduleRow": {
            "id": "milo-offscreen-water-jars",
            "reportIntroduced": 353,
            "resident": "Milo",
            "status": "pending",
            "action": "offscreen-resident-action",
            "schedule": "offscreen obligation: inspect leaking water jars",
            "obligation": "Fay found leaking water jars while the avatar was absent",
            "visibleStatus": "Milo schedule pending: offscreen obligation: inspect leaking water jars",
            "boundary": "browser-local-obligation-schedule-queue-only"
          },
          "debtRow": {
            "id": "milo-offscreen-water-jars",
            "reportIntroduced": 353,
            "resident": "Milo",
            "status": "outstanding",
            "action": "offscreen-resident-action",
            "debtAfter": 3,
            "trustAfter": 0.475,
            "obligation": "Fay found leaking water jars while the avatar was absent",
            "visibleStatus": "Milo debt outstanding: 3 after offscreen-resident-action",
            "boundary": "browser-local-obligation-debt-ledger-only"
          }
        },
        "persistedIn": "ssrm_v61_app_shell_world",
        "boundary": "browser-local-offscreen-cross-resident-obligation-event-only"
      }
    ],
    "absentTimeSummary": {
      "reportIntroduced": 355,
      "phase": "before-obligation-choice",
      "avatarCaused": [
        "avatar chose Wait offscreen at replay row 1",
        "avatar did not choose the new obligation target"
      ],
      "residentCaused": [
        "Fay changed Milo's obligation while avatar absent",
        "milo-offscreen-water-jars is open / offscreen-pending"
      ],
      "beforeChoice": "Milo obligation is selectable before resolve/defer; schedule pending; debt outstanding",
      "obligationId": "milo-offscreen-water-jars",
      "actor": "Fay",
      "target": "Milo",
      "scheduleQueueStatus": "pending",
      "debtLedgerStatus": "outstanding",
      "boundary": "browser-local-absent-time-summary-only"
    },
    "absentTimeThreads": [
      {
        "id": "avatar-absence-thread",
        "reportIntroduced": 356,
        "source": "avatar-caused",
        "status": "accounted",
        "label": "avatar chose Wait offscreen and must decide whether to account for absence first",
        "boundary": "browser-local-absent-time-choice-thread-only"
      },
      {
        "id": "milo-offscreen-water-jars",
        "reportIntroduced": 356,
        "source": "resident-caused",
        "status": "resolved",
        "label": "Fay changed Milo's obligation while avatar absent",
        "obligationStatus": "open",
        "boundary": "browser-local-absent-time-choice-thread-only"
      }
    ],
    "absentTimeChoiceReceipt": {
      "reportIntroduced": 356,
      "phase": "obligation-action-recorded",
      "chosenThreadId": "milo-offscreen-water-jars",
      "chosenSource": "resident-caused",
      "chosenAction": "resolve",
      "unchosenThreadIds": [
        "avatar-absence-thread"
      ],
      "unchosenThreadStatus": [
        "avatar-absence-thread: pending"
      ],
      "residentThreadStatus": "resolved",
      "avatarAbsenceStatus": "pending",
      "scheduleQueueStatus": "resolved",
      "debtLedgerStatus": "settled",
      "visibleStatus": "resident-caused offscreen obligation resolve; avatar-caused absence thread pending",
      "boundary": "browser-local-absent-time-choice-receipt-only"
    },
    "avatarAbsenceAccountabilityReceipt": {
      "reportIntroduced": 357,
      "phase": "avatar-absence-accounted",
      "avatarThreadId": "avatar-absence-thread",
      "avatarThreadStatus": "accounted",
      "residentThreadId": "milo-offscreen-water-jars",
      "residentThreadStatus": "resolved",
      "residentObligationStatus": "resolved",
      "residentObligationStage": "resolved",
      "residentHistoryPreserved": true,
      "careAfter": 5,
      "visibleStatus": "avatar-caused absence accounted; resident-caused milo-offscreen-water-jars remains resolved with obligation resolved/resolved",
      "boundary": "browser-local-avatar-absence-accountability-receipt-only"
    },
    "selectedObligationId": "ari-awning-followup",
    "lastQA": []
  }
} |
| `echo_choice_survives_reload` | `1.0` | reload_choice={'resident': 'Fay', 'action': 'offer_help', 'choice': 'accept_source_bounded_help', 'refusal': "refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory", 'sourceEchoId': 'milo-offscreen-water-jars', 'sourceAttributionPreserved': True, 'directAvatarCommand': False, 'noLLM': True, 'autonomousLanguage': False, 'phrasebookOnly': True, 'recoverable': True} text=Resident: Fay
Action: offer_help
Choice: accept_source_bounded_help
Refusal: refuses to rewrite Fay as the direct avatar cause or erase Milo's source memory
Source echo: milo-offscreen-water-jars
Source preserved: yes
Direct avatar command: no
No LLM: yes
Autonomous language: no
Phrasebook only: yes
Recoverable: yes |
| `browser_console_clean` | `1.0` | console error count=0 |
| `experiment_index_includes_report_361` | `1.0` | scripts/run_experiments.py includes Report 361 module |
| `claim_boundary_preserved` | `1.0` | Browser-local echo-influenced choice/refusal over the maintained v61 shell only; phrasebook-only receipts, no LLM call, no autonomous natural language, no subjective consciousness, no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, no finished gameplay, and no metaphysical claim. |

## Honest interpretation

This is still deterministic browser-local state. The useful integration step is that resident memory now changes a later action affordance: Fay can accept help in a constrained way and refuse history rewriting, with the refusal visible as a recoverable receipt rather than hidden agent interior or autonomous language.

## Next gate

post-361: make the source-bounded refusal/choice affect one later recoverable trust or task branch while keeping history attribution, replay audit, and no-LLM boundaries visible
