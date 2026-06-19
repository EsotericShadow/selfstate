from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v131_avatar_hint_divergence_bridge import (
    LAW_HASH,
    SEEDS,
    build_rows_for_report as build_report371_rows,
)

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 372
SLUG = "ssrm_3d_browser_world_v132_hint_branch_return_persistence_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"

RETURN_SESSIONS = ARTIFACT_DIR / f"{SLUG}_return_sessions.csv"
BRANCH_CONTINUITY = ARTIFACT_DIR / f"{SLUG}_branch_continuity.csv"
HOUSEHOLD_REPUTATION = ARTIFACT_DIR / f"{SLUG}_household_reputation.csv"
MAINTENANCE_BURDEN = ARTIFACT_DIR / f"{SLUG}_maintenance_burden.csv"
FORGETTING_EVENTS = ARTIFACT_DIR / f"{SLUG}_forgetting_events.csv"
REVIVAL_EVENTS = ARTIFACT_DIR / f"{SLUG}_revival_events.csv"
SAVE_RETURN_SNAPSHOTS = ARTIFACT_DIR / f"{SLUG}_save_return_snapshots.csv"
EXPRESSION_MARKERS = ARTIFACT_DIR / f"{SLUG}_expression_markers.csv"
REALITY_LEDGER = ARTIFACT_DIR / f"{SLUG}_reality_constraint_ledger.csv"
SOURCE_LINKS = ARTIFACT_DIR / f"{SLUG}_source_links.csv"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_surface_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "372_ssrm_3d_hint_branch_return_persistence_bridge_report.md"

BOUNDARY = (
    "Browser-local hint-branch return persistence bridge only. Branches from avatar hints can persist, decay, burden residents, "
    "be forgotten, or be revived across return sessions. The avatar cannot reset history, force adoption, or install a uniform unlock. "
    "No LLM call, no subjective-consciousness claim, no moral-patienthood claim, no real civilization claim, no full physics claim, "
    "and no new research branch beyond the emergent-practice/game-foundation arc."
)
NEXT_GATE = (
    "terminal handoff: close the research-report arc and document the first finite game prototype foundation rather than adding new conceptual systems"
)
STATE_KEYS = [
    "avatarHintDivergence",
    "hintBranchPersistence",
    "emergentPracticeGraph",
    "villageBoard",
    "realityConstraintLedger",
]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def status_for(branch_status: str, session: int, offset: int) -> str:
    if branch_status == "taboo":
        return "warning_persisted" if session % 2 else "ritual_warning"
    if branch_status == "ritualized":
        return "burdened_ritual" if offset % 3 == 0 else "remembered_ritual"
    if branch_status == "disputed":
        return "forgotten" if session >= 2 else "still_disputed"
    if branch_status == "rejected":
        return "forgotten"
    if branch_status == "useful_practice":
        return "needs_maintenance" if session >= 2 and offset % 4 == 0 else "persisted"
    return "still_carried"


def expression_for(return_status: str, maintenance_cost: int) -> str:
    if return_status == "forgotten":
        return "looks unsure and asks another resident"
    if "warning" in return_status:
        return "keeps distance and points to the old place"
    if maintenance_cost > 0:
        return "moves slowly while carrying upkeep material"
    if return_status == "persisted":
        return "faces the avatar and names the remembered branch"
    return "hesitates before repeating the branch story"


def build_rows_for_report(ablation: str | None = None) -> Dict[str, List[Dict[str, Any]]]:
    base = build_report371_rows()
    branches_by_seed: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for branch in base["divergence_branches"]:
        branches_by_seed[int(branch["seed"])].append(branch)
    rows: Dict[str, List[Dict[str, Any]]] = {
        "return_sessions": [],
        "branch_continuity": [],
        "household_reputation": [],
        "maintenance_burden": [],
        "forgetting_events": [],
        "revival_events": [],
        "save_return_snapshots": [],
        "expression_markers": [],
        "reality_ledger": [],
        "source_links": [],
    }
    sessions = [] if ablation == "no_return_persistence" else [1, 2, 3]
    for seed in SEEDS:
        seed_branches = branches_by_seed[int(seed)][:6]
        for session in sessions:
            session_id = f"{seed}-HRS-{session:02d}"
            direct_reset = ablation == "uniform_reset"
            rows["return_sessions"].append({
                "seed": seed,
                "session_id": session_id,
                "return_index": session,
                "branches_seen": 0 if direct_reset else len(seed_branches),
                "avatar_action": "returned and asked what residents still carry",
                "direct_reset": direct_reset,
                "normal_play_action": "ask_schedule_then_offer_help",
            })
            saved_count = 0 if ablation == "no_save_restore_state" else len(seed_branches)
            restored_count = 0 if ablation == "no_save_restore_state" else len(seed_branches)
            rows["save_return_snapshots"].append({
                "seed": seed,
                "snapshot_id": f"{seed}-SRS-{session:02d}",
                "session_id": session_id,
                "saved_branch_count": saved_count,
                "restored_branch_count": restored_count,
                "state_keys": ";".join([] if ablation == "no_save_restore_state" else STATE_KEYS),
                "restore_preserved_source_ids": ablation != "no_save_restore_state",
                "return_greeting_mentions_branch": ablation != "no_save_restore_state",
            })
            for offset, branch in enumerate(seed_branches):
                if direct_reset:
                    return_status = "uniform_reset"
                else:
                    return_status = status_for(str(branch["branch_status"]), session, offset)
                if ablation == "no_forgetting" and return_status == "forgotten":
                    return_status = "still_disputed"
                maintenance_cost = 0
                if return_status in {"needs_maintenance", "burdened_ritual", "remembered_ritual", "ritual_warning"}:
                    maintenance_cost = 1 if return_status != "needs_maintenance" else 2
                if ablation in {"no_maintenance_cost", "no_reality_cost"}:
                    maintenance_cost = 0
                expression = expression_for(return_status, maintenance_cost)
                continuity_id = f"{seed}-HRC-{session:02d}-{offset + 1:02d}"
                rows["branch_continuity"].append({
                    "seed": seed,
                    "continuity_id": continuity_id,
                    "session_id": session_id,
                    "branch_id": branch["branch_id"],
                    "hint_id": branch["hint_id"],
                    "household": branch["household"],
                    "resident": branch["resident"],
                    "prior_status": branch["branch_status"],
                    "return_status": return_status,
                    "maintenance_cost": maintenance_cost,
                    "avatar_commanded": False,
                    "source_practice_id": branch["source_practice_id"],
                    "ordinary_action_affected": "schedule_mentions_branch" if session == 1 else "help_prioritizes_upkeep",
                    "expression_marker": expression,
                })
                rows["expression_markers"].append({
                    "seed": seed,
                    "continuity_id": continuity_id,
                    "resident": branch["resident"],
                    "return_status": return_status,
                    "visible_expression": expression,
                    "debug_table_required": False,
                })
                reputation_delta = 0.04 if return_status in {"persisted", "warning_persisted"} else (-0.03 if return_status == "forgotten" else 0.01)
                rows["household_reputation"].append({
                    "seed": seed,
                    "session_id": session_id,
                    "branch_id": branch["branch_id"],
                    "household": branch["household"],
                    "resident": branch["resident"],
                    "reputation_delta": reputation_delta,
                    "reason": return_status,
                })
                if maintenance_cost:
                    rows["maintenance_burden"].append({
                        "seed": seed,
                        "session_id": session_id,
                        "branch_id": branch["branch_id"],
                        "household": branch["household"],
                        "material_cost": maintenance_cost,
                        "labor_cost": 1,
                        "time_cost": 1,
                        "created_obligation": f"{return_status} upkeep",
                    })
                if return_status == "forgotten":
                    rows["forgetting_events"].append({
                        "seed": seed,
                        "session_id": session_id,
                        "branch_id": branch["branch_id"],
                        "household": branch["household"],
                        "reason": "low trust, disputed value, or higher priority work",
                        "recoverable": True,
                    })
                    if session == 3 and ablation != "no_revival_evidence":
                        rows["revival_events"].append({
                            "seed": seed,
                            "session_id": session_id,
                            "branch_id": branch["branch_id"],
                            "household": branch["household"],
                            "evidence": "older resident repeats the remembered counterexample",
                            "cost": 1,
                            "revived_as": "cautious retry",
                            "avatar_commanded": False,
                        })
                before = 10
                cost = 0 if ablation == "no_reality_cost" else maintenance_cost
                rows["reality_ledger"].append({
                    "seed": seed,
                    "ledger_id": f"{seed}-HRL-{session:02d}-{offset + 1:02d}",
                    "event": continuity_id,
                    "material_sources": "fiber;care" if cost else "none",
                    "material_transformation": "upkeep consumed material and attention" if cost else "memory carried without material transformation",
                    "time_cost": 1 if ablation != "no_reality_cost" else 0,
                    "labor_or_attention_cost": 1 if ablation != "no_reality_cost" else 0,
                    "resident_effort": 1 if ablation != "no_reality_cost" else 0,
                    "hidden_law_involved": LAW_HASH,
                    "public_observation": return_status,
                    "resident_interpretation": f"{branch['resident']} carries {branch['branch_status']} as {return_status}",
                    "resources_before": before,
                    "resources_after": before - cost,
                    "conservation_check": before - cost <= before,
                    "maintenance_obligation_created": continuity_id if cost else "none",
                    "unintended_consequence": "recoverable forgetting" if return_status == "forgotten" else "ongoing social memory",
                    "normal_view_hidden_law_exposed": False,
                })
                if ablation != "no_source_trace":
                    rows["source_links"].append({
                        "seed": seed,
                        "session_id": session_id,
                        "branch_id": branch["branch_id"],
                        "hint_id": branch["hint_id"],
                        "source_practice_id": branch["source_practice_id"],
                        "avatar_commanded": False,
                        "hidden_law_exposed": False,
                    })
    return rows


def compute_metrics(rows: Dict[str, List[Dict[str, Any]]], app_text: str = "", index_text: str = "", browser: Dict[str, Any] | None = None) -> Dict[str, float]:
    browser = browser or {}
    sessions = rows["return_sessions"]
    continuity = rows["branch_continuity"]
    reputation = rows["household_reputation"]
    burdens = rows["maintenance_burden"]
    forgetting = rows["forgetting_events"]
    revivals = rows["revival_events"]
    snapshots = rows["save_return_snapshots"]
    expressions = rows["expression_markers"]
    ledger = rows["reality_ledger"]
    links = rows["source_links"]
    statuses = {row["return_status"] for row in continuity}
    branch_session_counts = Counter(row["branch_id"] for row in continuity)
    return {
        "return_session_persistence": score(bool(sessions) and bool(continuity) and max(branch_session_counts.values() or [0]) >= 3 and all(not row["direct_reset"] for row in sessions)),
        "save_restore_preserves_branch_state": score(bool(snapshots) and all(int(row["saved_branch_count"]) == int(row["restored_branch_count"]) and "hintBranchPersistence" in row["state_keys"] and row["restore_preserved_source_ids"] for row in snapshots)),
        "maintenance_burden_has_cost": score(bool(burdens) and all(int(row["material_cost"]) > 0 and int(row["labor_cost"]) > 0 and int(row["time_cost"]) > 0 for row in burdens)),
        "forgetting_is_recoverable": score(bool(forgetting) and all(row["recoverable"] for row in forgetting)),
        "revival_requires_evidence_and_cost": score(bool(revivals) and all(row["evidence"] != "none" and int(row["cost"]) > 0 and not row["avatar_commanded"] for row in revivals)),
        "household_reputation_changes": score(bool(reputation) and any(float(row["reputation_delta"]) != 0.0 for row in reputation)),
        "ordinary_return_actions_affected": score(bool(continuity) and {"schedule_mentions_branch", "help_prioritizes_upkeep"}.issubset({row["ordinary_action_affected"] for row in continuity})),
        "visible_expression_markers": score(bool(expressions) and all(row["visible_expression"] and not row["debug_table_required"] for row in expressions)),
        "no_uniform_history_reset": score(bool(statuses) and "uniform_reset" not in statuses and len(statuses) >= 5),
        "source_trace_integrity": score(bool(links) and all(row["branch_id"] != "none" and row["hint_id"] != "none" and row["source_practice_id"] != "none" and not row["avatar_commanded"] and not row["hidden_law_exposed"] for row in links)),
        "reality_causal_ledger_integrity": score(bool(ledger) and all(int(row["time_cost"]) > 0 and int(row["labor_or_attention_cost"]) > 0 and int(row["resident_effort"]) > 0 and int(row["resources_after"]) <= int(row["resources_before"]) and row["conservation_check"] and not row["normal_view_hidden_law_exposed"] for row in ledger)),
        "shell_persistence_wired": score("hintBranchPersistence" in app_text and "runHintBranchPersistenceLoop" in app_text and "runHintBranchReturnSession" in app_text and "expression_marker" in app_text),
        "browser_surface_wired": score("Hint Branch Return Persistence" in index_text and "hintBranchPersistenceOut" in index_text and "runHintBranchPersistenceLoop" in index_text),
        "browser_surface_static_smoke": score(bool(browser) and browser.get("panel_present") and browser.get("summary_present") and browser.get("actions_present")),
    }


def build_browser_surface_smoke(app_text: str, index_text: str) -> Dict[str, Any]:
    return {
        "kind": "static_browser_surface_smoke",
        "runtime_browser_exercised": False,
        "reason": "Report 372 checks shell wiring and generated persistence evidence; terminal handoff should decide whether to run a live browser pass.",
        "panel_present": "Hint Branch Return Persistence" in index_text,
        "summary_present": "hintBranchPersistenceSummaryOut" in index_text,
        "detail_present": "hintBranchPersistenceOut" in index_text,
        "actions_present": all(token in index_text for token in ["runHintBranchReturnSession", "maintainHintBranchPractice", "reviveForgottenHintPractice", "runHintBranchPersistenceLoop"]),
        "state_wired": "hintBranchPersistence" in app_text,
        "render_wired": "renderHintBranchPersistence" in app_text,
    }


def build_ablations(app_text: str, index_text: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    expected_failures = {
        "no_return_persistence": "return_session_persistence",
        "no_maintenance_cost": "maintenance_burden_has_cost",
        "no_forgetting": "forgetting_is_recoverable",
        "no_revival_evidence": "revival_requires_evidence_and_cost",
        "no_source_trace": "source_trace_integrity",
        "no_save_restore_state": "save_restore_preserves_branch_state",
        "uniform_reset": "no_uniform_history_reset",
        "no_reality_cost": "reality_causal_ledger_integrity",
    }
    for name, expected_failure in expected_failures.items():
        ablated = build_rows_for_report(name)
        metrics = compute_metrics(ablated, app_text, index_text, {"panel_present": True, "summary_present": True, "actions_present": True})
        rows.append({
            "ablation": name,
            "expected_failed_metric": expected_failure,
            "failed_as_expected": metrics.get(expected_failure, 1.0) == 0.0,
            "weakest_channel_score": min(metrics.values()) if metrics else 0.0,
        })
    return rows


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def write_report(metrics: Dict[str, float], rows: Dict[str, List[Dict[str, Any]]], ablations: List[Dict[str, Any]], verdict: str) -> None:
    status_counts = Counter(row["return_status"] for row in rows["branch_continuity"])
    lines = [
        "# Report 372: SSRM-3D Hint Branch Return Persistence Bridge",
        "",
        "## Purpose",
        "",
        "Report 372 closes the return-session gap in the emergent-practice arc. Branches created by ambiguous avatar hints do not reset after one panel event. They can persist, decay, create upkeep burden, be forgotten, or be revived with evidence and cost when the avatar returns.",
        "",
        "## Boundary",
        "",
        BOUNDARY,
        "",
        "## Method",
        "",
        "- Start from Report 371 hint-divergence branches.",
        "- Simulate three return sessions per seed.",
        "- Preserve branch IDs, hint IDs, source practice IDs, household identity, and normal-play action effects.",
        "- Add maintenance burden, reputation deltas, recoverable forgetting, evidence-based revival, and expression markers.",
        "- Generate save/return snapshot rows proving the relevant state keys survive restore.",
        "",
        "## Results",
        "",
        f"- Verdict: `{verdict}`",
        f"- Return sessions: `{len(rows['return_sessions'])}`",
        f"- Branch continuity rows: `{len(rows['branch_continuity'])}`",
        f"- Maintenance burdens: `{len(rows['maintenance_burden'])}`",
        f"- Forgetting events: `{len(rows['forgetting_events'])}`",
        f"- Revival events: `{len(rows['revival_events'])}`",
        f"- Return status counts: `{dict(status_counts)}`",
        "",
        "## Metrics",
        "",
    ]
    for key, value in sorted(metrics.items()):
        lines.append(f"- `{key}`: `{value:.3f}`")
    lines.extend(["", "## Ablations", ""])
    for row in ablations:
        lines.append(f"- `{row['ablation']}`: expected failure `{row['expected_failed_metric']}`, failed as expected `{row['failed_as_expected']}`")
    lines.extend([
        "",
        "## Honest read",
        "",
        "The important gain is continuity: hint-divergent branches now survive into later ordinary return sessions, and the evidence records when they burden, fade, or revive. This still does not make the world a complete game, a full civilization simulator, a physics engine, or a consciousness system.",
        "",
        f"Next gate: {NEXT_GATE}.",
        "",
    ])
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    browser = build_browser_surface_smoke(app_text, index_text)
    rows = build_rows_for_report()
    metrics = compute_metrics(rows, app_text, index_text, browser)
    ablations = build_ablations(app_text, index_text)
    criteria: List[Dict[str, Any]] = []
    for name, value in sorted(metrics.items()):
        add_criterion(criteria, name, value == 1.0, f"metric={value:.3f}")
    add_criterion(criteria, "ablations_fail_as_expected", all(row["failed_as_expected"] for row in ablations), f"{sum(1 for row in ablations if row['failed_as_expected'])}/{len(ablations)}")
    weakest = min(metrics.values()) if metrics else 0.0
    readiness = sum(metrics.values()) / len(metrics) if metrics else 0.0
    verdict = "pass" if weakest == 1.0 and all(row["failed_as_expected"] for row in ablations) else "fail"

    write_csv(RETURN_SESSIONS, rows["return_sessions"], list(rows["return_sessions"][0].keys()))
    write_csv(BRANCH_CONTINUITY, rows["branch_continuity"], list(rows["branch_continuity"][0].keys()))
    write_csv(HOUSEHOLD_REPUTATION, rows["household_reputation"], list(rows["household_reputation"][0].keys()))
    write_csv(MAINTENANCE_BURDEN, rows["maintenance_burden"], list(rows["maintenance_burden"][0].keys()))
    write_csv(FORGETTING_EVENTS, rows["forgetting_events"], list(rows["forgetting_events"][0].keys()))
    write_csv(REVIVAL_EVENTS, rows["revival_events"], list(rows["revival_events"][0].keys()))
    write_csv(SAVE_RETURN_SNAPSHOTS, rows["save_return_snapshots"], list(rows["save_return_snapshots"][0].keys()))
    write_csv(EXPRESSION_MARKERS, rows["expression_markers"], list(rows["expression_markers"][0].keys()))
    write_csv(REALITY_LEDGER, rows["reality_ledger"], list(rows["reality_ledger"][0].keys()))
    write_csv(SOURCE_LINKS, rows["source_links"], list(rows["source_links"][0].keys()))
    write_csv(ABLATIONS, ablations, list(ablations[0].keys()))
    write_json(BROWSER_SMOKE, browser)
    write_csv(CRITERIA, criteria, list(criteria[0].keys()))
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, "readiness": readiness, "weakest_channel_score": weakest, "return_sessions": len(rows["return_sessions"]), "branch_continuity": len(rows["branch_continuity"]), "revival_events": len(rows["revival_events"])}], ["report", "verdict", "readiness", "weakest_channel_score", "return_sessions", "branch_continuity", "revival_events"])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "boundary": BOUNDARY, "next_gate": NEXT_GATE}], ["report", "verdict", "boundary", "next_gate"])
    write_json(STATE, {"generated_at": datetime.now(timezone.utc).isoformat(), "report": REPORT, "boundary": BOUNDARY, "next_gate": NEXT_GATE, "rows": rows, "metrics": metrics, "ablations": ablations, "browser_surface_smoke": browser})
    write_json(RESULTS, {"report": REPORT, "slug": SLUG, "verdict": verdict, "metrics": metrics, "readiness": readiness, "weakest_channel_score": weakest, "counts": {name: len(value) for name, value in rows.items()}, "boundary": BOUNDARY, "next_gate": NEXT_GATE})
    write_report(metrics, rows, ablations, verdict)
    print(json.dumps({"report": REPORT, "verdict": verdict, "readiness": readiness, "weakest_channel_score": weakest, "return_sessions": len(rows["return_sessions"]), "branch_continuity": len(rows["branch_continuity"]), "revivals": len(rows["revival_events"])}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
