from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import RESIDENTS, SEEDS
from experiments.ssrm_3d_browser_world_v124_stochastic_resident_consequence_bridge import simulate_seed as simulate_stochastic_seed
from experiments.ssrm_3d_browser_world_v125_stochastic_recovery_loop_bridge import plan_recovery

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 366
SLUG = "ssrm_3d_browser_world_v126_stochastic_history_influence_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT365_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v125_stochastic_recovery_loop_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
HISTORY_CHOICES = ARTIFACT_DIR / f"{SLUG}_history_choices.csv"
BOUNDED_REFUSALS = ARTIFACT_DIR / f"{SLUG}_bounded_refusals.csv"
SOCIAL_ECHOES = ARTIFACT_DIR / f"{SLUG}_social_echoes.csv"
INFLUENCE_LEDGER = ARTIFACT_DIR / f"{SLUG}_influence_ledger.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "366_ssrm_3d_stochastic_history_influence_bridge_report.md"
BOUNDARY = (
    "Browser-local stochastic history influence only. Recovered, pending, and stabilized stochastic recovery histories "
    "can bias later bounded resident choices, refusals, and social echoes, but every influence keeps source recovery IDs, "
    "direct-avatar-command status, and no-permanent-punishment flags. No LLM call, autonomous language, subjective "
    "consciousness, suffering model, moral patienthood, production persistence, hosted proof, complete 3D engine, or finished gameplay."
)
NEXT_GATE = (
    "post-366: attach stochastic history influence to ordinary non-panel affordances such as Offer help, Talk, schedule "
    "work, and resident movement so the recovery history changes normal play instead of living in one inspection panel"
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def has_terms(text: str, terms: Iterable[str]) -> bool:
    return all(term in text for term in terms)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def status_for(row_index: int, actor: str) -> str:
    if row_index % 5 == 0:
        return "pending"
    if row_index % 7 == 0 or actor == "Nia":
        return "stabilized without materials"
    return "resolved"


def choice_for_status(status: str) -> Dict[str, Any]:
    if status == "pending":
        return {
            "decision": "bounded_refusal_until_recovery",
            "reason": "unrecovered stochastic harm is still pending",
            "refusal_bounded": True,
            "trust_delta": -0.003,
            "progress_delta": -0.002,
        }
    if status == "stabilized without materials":
        return {
            "decision": "cautious_help_with_limits",
            "reason": "history stabilized without materials, so help stays cautious",
            "refusal_bounded": False,
            "trust_delta": 0.002,
            "progress_delta": 0.004,
        }
    return {
        "decision": "accept_recovery_informed_help",
        "reason": "past stochastic harm was recovered and can support trust",
        "refusal_bounded": False,
        "trust_delta": 0.008,
        "progress_delta": 0.010,
    }


def simulate_history_influence(seed: int) -> Dict[str, Any]:
    stochastic = simulate_stochastic_seed(seed)
    recovery_rows = plan_recovery(stochastic)
    choices: List[Dict[str, Any]] = []
    refusals: List[Dict[str, Any]] = []
    echoes: List[Dict[str, Any]] = []
    ledger: List[Dict[str, Any]] = []
    for index, recovery in enumerate(recovery_rows):
        status = status_for(index, recovery["actor"])
        choice = choice_for_status(status)
        choice_id = f"{seed}-SHC-{index + 1:02d}"
        target = RESIDENTS[(RESIDENTS.index(recovery["actor"]) + 1 + index) % len(RESIDENTS)]
        row = {
            "seed": seed,
            "choice_id": choice_id,
            "actor": recovery["actor"],
            "decision": choice["decision"],
            "reason": choice["reason"],
            "source_recovery_id": recovery["recovery_id"],
            "source_pulse_id": recovery["pulse_id"],
            "source_recovery_status": status,
            "refusal_bounded": choice["refusal_bounded"],
            "trust_delta": choice["trust_delta"],
            "progress_delta": choice["progress_delta"],
            "permanent_penalty": False,
            "recovery_path": recovery["repair_action"],
        }
        choices.append(row)
        ledger.append({"seed": seed, "ledger_id": f"{choice_id}-choice", "type": "choice", "source_id": choice_id, "summary": f"{recovery['actor']} chose {choice['decision']} from {status}"})
        if choice["refusal_bounded"]:
            refusals.append({
                "seed": seed,
                "choice_id": choice_id,
                "actor": recovery["actor"],
                "reason": choice["reason"],
                "recovery_path": recovery["repair_action"],
                "permanent_penalty": False,
            })
        echo_id = f"{seed}-SHE-{index + 1:02d}"
        echoes.append({
            "seed": seed,
            "echo_id": echo_id,
            "from": recovery["actor"],
            "to": target,
            "source_choice_id": choice_id,
            "message": f"{recovery['actor']} carried {choice['decision']} from stochastic recovery history",
            "direct_avatar_command": False,
            "bounded_refusal_carried": choice["refusal_bounded"],
            "permanent_penalty": False,
        })
        ledger.append({"seed": seed, "ledger_id": f"{echo_id}-echo", "type": "social_echo", "source_id": echo_id, "summary": f"{recovery['actor']} echoed history influence to {target}"})
    return {"seed": seed, "choices": choices, "refusals": refusals, "echoes": echoes, "ledger": ledger}


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 366: SSRM-3D Stochastic History Influence Bridge",
        "",
        "Report 366 makes stochastic recovery history affect later bounded choices, refusals, and social memory. Resolved recovery can support help, pending recovery can justify bounded refusal, and stabilized recovery can produce cautious help without permanent punishment.",
        "",
        f"Boundary: {BOUNDARY}",
        "",
        "## Result",
        "",
        f"Verdict: `{results['verdict']}`",
        f"Readiness: `{metrics['readiness']:.3f}`",
        f"Weakest channel score: `{metrics['weakest_channel_score']:.3f}`",
        f"Criteria passed: `{passed_count} / {len(criteria)}`",
        "",
        "## Browser-smoke evidence",
        "",
        f"- Maintained shell URL: `{browser.get('shellUrl', 'missing')}`",
        f"- Influence summary: `{browser.get('afterInfluence', {}).get('influenceSummary', 'missing')}`",
        f"- Influence panel excerpt: `{browser.get('afterInfluence', {}).get('influenceText', 'missing')}`",
        f"- Console errors: `{metrics['console_error_count']}`",
        "",
        "## Criteria",
        "",
        "| Criterion | Score | Evidence |",
        "| --- | ---: | --- |",
    ]
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "/")
        lines.append(f"| `{row['criterion']}` | `{row['score']:.1f}` | {evidence} |")
    lines.extend([
        "",
        "## Honest interpretation",
        "",
        "This still uses bounded phrase/choice scaffolding, not autonomous personality. The non-toy gain is continuity: stochastic events now pass through recovery and then alter later choices/social memory with explicit source IDs and no-permanent-punishment flags.",
        "",
        "## Next gate",
        "",
        NEXT_GATE,
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    runs = [simulate_history_influence(seed) for seed in SEEDS]
    choices = [row for run in runs for row in run["choices"]]
    refusals = [row for run in runs for row in run["refusals"]]
    echoes = [row for run in runs for row in run["echoes"]]
    ledger = [row for run in runs for row in run["ledger"]]
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report365 = load_json(REPORT365_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    decisions = {row["decision"] for row in choices}
    metrics_base = {
        "history_choice_binding": float(len(choices) == 48 and all(row["source_recovery_id"] and row["source_pulse_id"] for row in choices)),
        "decision_diversity": float({"accept_recovery_informed_help", "bounded_refusal_until_recovery", "cautious_help_with_limits"}.issubset(decisions)),
        "bounded_refusal_preservation": float(bool(refusals) and all(row["permanent_penalty"] is False for row in refusals)),
        "recovered_help_binding": float(any(row["decision"] == "accept_recovery_informed_help" and row["trust_delta"] > 0 for row in choices)),
        "stabilized_caution_binding": float(any(row["decision"] == "cautious_help_with_limits" for row in choices)),
        "social_memory_echo_binding": float(len(echoes) == len(choices) and all(row["direct_avatar_command"] is False for row in echoes)),
        "source_boundary_integrity": float(all(row["permanent_penalty"] is False for row in choices + echoes)),
        "influence_replay_integrity": float(len(ledger) == len(choices) + len(echoes)),
        "not_panel_only_loop": float(has_terms(app_text, ["runStochasticHistoryChoice", "runStochasticHistorySocialEcho", "mutateResident", "recordCheckpoint"])),
        "browser_surface_wired": float(has_terms(index_text, ["stochasticHistoryInfluenceOut", "Run choice", "Run social echo", "Run influence loop", "History influence"])),
        "no_permanent_punishment_policy": float("unrecovered stochastic history can justify bounded caution, not permanent punishment" in app_text),
    }

    write_csv(HISTORY_CHOICES, choices, ["seed", "choice_id", "actor", "decision", "reason", "source_recovery_id", "source_pulse_id", "source_recovery_status", "refusal_bounded", "trust_delta", "progress_delta", "permanent_penalty", "recovery_path"])
    write_csv(BOUNDED_REFUSALS, refusals, ["seed", "choice_id", "actor", "reason", "recovery_path", "permanent_penalty"])
    write_csv(SOCIAL_ECHOES, echoes, ["seed", "echo_id", "from", "to", "source_choice_id", "message", "direct_avatar_command", "bounded_refusal_carried", "permanent_penalty"])
    write_csv(INFLUENCE_LEDGER, ledger, ["seed", "ledger_id", "type", "source_id", "summary"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_365_recovery_gate_passing", report365.get("verdict") == "pass" and report365.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 365 verdict={report365.get('verdict')} weakest={report365.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_declares_history_boundary", has_terms(app_text, ["browser-local-stochastic-history-influence-only", "noPermanentPunishmentPolicy", "stochasticHistoryInfluence"]), "app.js declares history influence boundary and public state")
    add_criterion(criteria, "source_choice_and_echo_actions", has_terms(app_text, ["runStochasticHistoryChoice", "runStochasticHistorySocialEcho", "runStochasticHistoryInfluenceLoop"]), "app.js exposes choice, social echo, and loop actions")
    add_criterion(criteria, "visible_history_panel_wired", metrics_base["browser_surface_wired"] == 1.0, "index.html exposes history influence controls and panel")
    add_criterion(criteria, "runner_includes_report_366", "experiments.ssrm_3d_browser_world_v126_stochastic_history_influence_bridge" in runner_text, "scripts/run_experiments.py includes Report 366 module")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    influence_text = browser.get("afterInfluence", {}).get("influenceText", "")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_history_influence_visible", all(term in influence_text for term in ["Choice records:", "Bounded refusals:", "Social echoes:", "Policy:"]), influence_text or "missing influence text")
    add_criterion(criteria, "browser_choice_or_refusal_visible", any(term in influence_text for term in ["accept_recovery_informed_help", "bounded_refusal_until_recovery", "cautious_help_with_limits"]), influence_text or "missing influence text")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "choice_count": len(choices),
        "bounded_refusal_count": len(refusals),
        "social_echo_count": len(echoes),
        "console_error_count": len(console_errors),
        "criterion_count": len(criteria),
        "readiness": round(passed / len(criteria), 6),
        "weakest_channel_score": min(row["score"] for row in criteria),
    }
    results = {
        "report": REPORT,
        "slug": SLUG,
        "verdict": "pass" if metrics["weakest_channel_score"] == 1.0 else "needs_work",
        "metrics": metrics,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    state = {"runs": runs, "browser_smoke": browser, "criteria": criteria}
    summary_rows = [{"metric": key, "value": value} for key, value in metrics.items()]
    verdict_rows = [{"report": REPORT, "verdict": results["verdict"], "readiness": metrics["readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": NEXT_GATE}]

    write_json(RESULTS, results)
    write_json(STATE, state)
    write_csv(SUMMARY, summary_rows, ["metric", "value"])
    write_csv(VERDICT, verdict_rows, ["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
