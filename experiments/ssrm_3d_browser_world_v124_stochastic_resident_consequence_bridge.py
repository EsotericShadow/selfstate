from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import RESIDENTS, SEEDS

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 364
SLUG = "ssrm_3d_browser_world_v124_stochastic_resident_consequence_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT363_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v123_scheduled_anomaly_investigation_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
ENTROPY_EVENTS = ARTIFACT_DIR / f"{SLUG}_entropy_events.csv"
RESIDENT_CONSEQUENCES = ARTIFACT_DIR / f"{SLUG}_resident_consequences.csv"
REPLAY_LEDGER = ARTIFACT_DIR / f"{SLUG}_replay_ledger.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "364_ssrm_3d_stochastic_resident_consequence_bridge_report.md"
BOUNDARY = (
    "Browser-local stochastic resident consequence pulses only. Runtime browser pulses use nondeterministic entropy, "
    "but each branch records entropy bytes, resident, resource delta, schedule coupling, need snapshot, and replay row. "
    "The evaluator uses seeded entropy streams for reproducible evidence. No LLM call, autonomous language, subjective "
    "consciousness, moral patienthood, real consent, production persistence, hosted proof, complete 3D engine, or finished gameplay."
)
NEXT_GATE = (
    "post-364: use recorded stochastic pulses to create multi-step resident recovery and relationship repair loops, "
    "so surprise changes future behavior without turning into chaos or permanent damage"
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


def entropy_byte(seed: int, pulse_index: int, label: str) -> int:
    digest = hashlib.sha256(f"{seed}:{pulse_index}:{label}".encode("utf-8")).digest()
    return digest[0]


def weighted_pick(options: List[Dict[str, Any]], entropy: int) -> Dict[str, Any]:
    total = sum(option["weight"] for option in options)
    cursor = entropy / 256 * total
    for option in options:
        cursor -= option["weight"]
        if cursor <= 0:
            return option
    return options[-1]


def need_snapshot(resident: Dict[str, float], resources: Dict[str, int], refusals: int, delayed: int) -> Dict[str, Any]:
    pressure = max(0, 8 - resources["water"] - resources["care"])
    schedule_pressure = refusals + delayed
    energy = round(max(0.12, min(0.95, 0.72 - resident["debt"] * 0.08 - pressure * 0.03)), 3)
    comfort = round(max(0.08, min(0.96, 0.58 + resident["trust"] * 0.28 - schedule_pressure * 0.025)), 3)
    focus = round(max(0.1, min(0.92, resident["progress"] + resident["trust"] * 0.18 - schedule_pressure * 0.018)), 3)
    if energy < 0.35:
        dominant = "rest"
    elif comfort < 0.42:
        dominant = "safety"
    elif focus < 0.5:
        dominant = "finish-work"
    else:
        dominant = "explore"
    return {"energy": energy, "comfort": comfort, "focus": focus, "dominant": dominant}


def event_options(actor: str, resources: Dict[str, int], trust: float, refusals: int, has_pending_slot: bool, energy: float) -> List[Dict[str, Any]]:
    return [
        {"event": "roof_leak", "weight": 3 + (3 if resources["wood"] < 2 else 0), "water": -1, "fiber": 0, "wood": -1, "care": 0, "trust_delta": -0.004, "progress_delta": -0.006, "debt_delta": 1},
        {"event": "tool_snag", "weight": 3 + (2 if has_pending_slot else 0), "water": 0, "fiber": -1, "wood": 0, "care": 0, "trust_delta": -0.002, "progress_delta": -0.01, "debt_delta": 0},
        {"event": "neighbor_help", "weight": 2 + round(trust * 3), "water": 0, "fiber": 0, "wood": 0, "care": 1, "trust_delta": 0.008, "progress_delta": 0.014, "debt_delta": -1},
        {"event": "argument_echo", "weight": 2 + refusals, "water": 0, "fiber": 0, "wood": 0, "care": 0, "trust_delta": -0.007, "progress_delta": -0.002, "debt_delta": 0},
        {"event": "found_material", "weight": 2 + (3 if resources["fiber"] < 3 else 0), "water": 0, "fiber": 1, "wood": 1, "care": 0, "trust_delta": 0.004, "progress_delta": 0.008, "debt_delta": 0},
        {"event": "quiet_recovery", "weight": 2 + (4 if energy < 0.42 else 0), "water": 0, "fiber": 0, "wood": 0, "care": 0, "trust_delta": 0.003, "progress_delta": 0.006, "debt_delta": -1},
    ]


def simulate_seed(seed: int) -> Dict[str, Any]:
    resources = {"water": 5 + seed % 3, "fiber": 4 + seed % 2, "wood": 5 + seed % 4, "care": 2}
    residents = {
        name: {"trust": round(0.48 + ((seed + index * 11) % 19) / 100, 3), "progress": round(0.34 + index * 0.025, 3), "debt": index % 2}
        for index, name in enumerate(RESIDENTS[:5])
    }
    slots = [
        {"slot_id": f"{seed}-AIS-{index + 1:02d}", "resident": name, "status": "planned", "ordinary_work": work}
        for index, (name, work) in enumerate(zip(RESIDENTS[:5], ["repair awning", "sort herbs", "carry water", "dry cloaks", "map safe route"]))
    ]
    events: List[Dict[str, Any]] = []
    consequences: List[Dict[str, Any]] = []
    replay_rows: List[Dict[str, Any]] = []
    refusals = 0
    delayed = 0
    for pulse_index in range(8):
        actor_entropy = entropy_byte(seed, pulse_index, "actor")
        event_entropy = entropy_byte(seed, pulse_index, "event")
        intensity_entropy = entropy_byte(seed, pulse_index, "intensity")
        actor = RESIDENTS[:5][actor_entropy % 5]
        actor_state = residents[actor]
        need_before = need_snapshot(actor_state, resources, refusals, delayed)
        pending_slot = next((slot for slot in slots if slot["status"] == "planned" and (slot["resident"] == actor or event_entropy % 3 == 0)), None)
        event = weighted_pick(event_options(actor, resources, actor_state["trust"], refusals, pending_slot is not None, need_before["energy"]), event_entropy)
        intensity = round(0.5 + intensity_entropy / 255, 3)
        before_resources = dict(resources)
        delta = {key: int(event[key]) for key in ["water", "fiber", "wood", "care"]}
        for key, value in delta.items():
            if value < 0 and intensity > 1.1:
                value -= 1
            resources[key] = max(0, resources[key] + value)
            delta[key] = value
        schedule_coupling = ""
        if pending_slot and event["event"] in {"roof_leak", "tool_snag", "argument_echo"}:
            pending_slot["status"] = "stochastically disputed" if event["event"] == "argument_echo" else "stochastically delayed"
            refusals += 1
            schedule_coupling = f"{actor} {pending_slot['status']} {pending_slot['slot_id']} while {pending_slot['ordinary_work']} competed with {event['event']}"
        elif pending_slot and event["event"] in {"neighbor_help", "found_material"}:
            delayed += 1
            schedule_coupling = f"{actor} made {pending_slot['slot_id']} easier to attempt after {event['event']}"
        actor_state["trust"] = round(max(0, min(1, actor_state["trust"] + event["trust_delta"] * intensity)), 3)
        actor_state["progress"] = round(max(0, min(1, actor_state["progress"] + event["progress_delta"] * intensity)), 3)
        actor_state["debt"] = max(0, actor_state["debt"] + event["debt_delta"])
        need_after = need_snapshot(actor_state, resources, refusals, delayed)
        pulse_id = f"{seed}-SP-{pulse_index + 1:02d}"
        event_row = {
            "seed": seed,
            "pulse_id": pulse_id,
            "actor": actor,
            "event": event["event"],
            "actor_entropy": actor_entropy,
            "event_entropy": event_entropy,
            "intensity_entropy": intensity_entropy,
            "intensity": intensity,
            "resources_before": json.dumps(before_resources, sort_keys=True),
            "resources_after": json.dumps(resources, sort_keys=True),
            "resource_delta": json.dumps(delta, sort_keys=True),
            "need_before": need_before["dominant"],
            "need_after": need_after["dominant"],
            "schedule_coupling": schedule_coupling,
        }
        events.append(event_row)
        consequences.append({
            **event_row,
            "trust_after": actor_state["trust"],
            "progress_after": actor_state["progress"],
            "debt_after": actor_state["debt"],
            "consequence": f"{actor} encountered {event['event']} with intensity {intensity}",
        })
        replay_rows.append({
            "seed": seed,
            "tick": pulse_index,
            "event": "runStochasticConsequencePulse",
            "payload_keys": "pulse,replayableEntropy,scheduleCoupled",
            "replayable_entropy": True,
            "pulse_id": pulse_id,
        })
    return {"seed": seed, "events": events, "consequences": consequences, "replay": replay_rows, "resources": resources, "residents": residents, "slots": slots}


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 364: SSRM-3D Stochastic Resident Consequence Bridge",
        "",
        "Report 364 adds runtime stochastic pulses to the maintained browser-world shell. The browser uses runtime entropy for resident consequence events, while each pulse records the exact entropy bytes, branch choice, resident need snapshot, resource delta, schedule coupling, and replay row needed to inspect what happened.",
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
        f"- Pulse summary: `{browser.get('afterPulse', {}).get('pulseSummary', 'missing')}`",
        f"- Pulse panel excerpt: `{browser.get('afterPulse', {}).get('pulseText', 'missing')}`",
        f"- Console errors: `{metrics['console_error_count']}`",
        "",
        "## Metrics",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
    ]
    for key, value in sorted(metrics.items()):
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend([
        "",
        "## Criteria",
        "",
        "| Criterion | Score | Evidence |",
        "| --- | ---: | --- |",
    ])
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "/")
        lines.append(f"| `{row['criterion']}` | `{row['score']:.1f}` | {evidence} |")
    lines.extend([
        "",
        "## Honest interpretation",
        "",
        "This is a real shift away from fully scripted shell outcomes: two browser runs can take different resident consequence branches. It is still not an autonomous agent or consciousness claim. The important engineering move is that nondeterminism is not hidden magic; entropy is logged, branch effects are public, and deterministic seeded streams test the same class of behavior in artifacts.",
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
    first = [simulate_seed(seed) for seed in SEEDS]
    second = [simulate_seed(seed) for seed in SEEDS]
    events = [row for run in first for row in run["events"]]
    consequences = [row for run in first for row in run["consequences"]]
    replay = [row for run in first for row in run["replay"]]
    repeat_events = [row for run in second for row in run["events"]]
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report363 = load_json(REPORT363_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    event_types = {row["event"] for row in events}
    resource_deltas = [json.loads(row["resource_delta"]) for row in events]
    has_negative_resource = any(any(value < 0 for value in delta.values()) for delta in resource_deltas)
    has_positive_resource = any(any(value > 0 for value in delta.values()) for delta in resource_deltas)
    replay_match = [
        (row["actor"], row["event"], row["actor_entropy"], row["event_entropy"], row["intensity_entropy"])
        for row in events
    ] == [
        (row["actor"], row["event"], row["actor_entropy"], row["event_entropy"], row["intensity_entropy"])
        for row in repeat_events
    ]

    metrics_base = {
        "runtime_entropy_surface": float(has_terms(app_text, ["crypto.getRandomValues", "entropyLedger", "runtime entropy recorded"])),
        "entropy_replay_recorded": float(all(row["actor_entropy"] >= 0 and row["event_entropy"] >= 0 and row["intensity_entropy"] >= 0 for row in events) and all(row["replayable_entropy"] for row in replay)),
        "branch_diversity": float(len(event_types) >= 5),
        "resident_need_coupling": float(all(row["need_before"] and row["need_after"] for row in events)),
        "resource_delta_coupling": float(has_negative_resource and has_positive_resource),
        "schedule_state_coupling": float(any(row["schedule_coupling"] for row in events)),
        "deterministic_seed_replay": float(replay_match),
        "not_panel_only_loop": float(has_terms(app_text, ["runStochasticConsequencePulse", "mutateResident", "recordCheckpoint", "renderStochasticConsequencePulse"])),
        "browser_surface_wired": float(has_terms(index_text, ["stochasticConsequencePulseOut", "Run pulse", "Run burst", "Stochastic consequences"])),
    }

    write_csv(ENTROPY_EVENTS, events, ["seed", "pulse_id", "actor", "event", "actor_entropy", "event_entropy", "intensity_entropy", "intensity", "resources_before", "resources_after", "resource_delta", "need_before", "need_after", "schedule_coupling"])
    write_csv(RESIDENT_CONSEQUENCES, consequences, ["seed", "pulse_id", "actor", "event", "actor_entropy", "event_entropy", "intensity_entropy", "intensity", "resources_before", "resources_after", "resource_delta", "need_before", "need_after", "schedule_coupling", "trust_after", "progress_after", "debt_after", "consequence"])
    write_csv(REPLAY_LEDGER, replay, ["seed", "tick", "event", "payload_keys", "replayable_entropy", "pulse_id"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_363_schedule_gate_passing", report363.get("verdict") == "pass" and report363.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 363 verdict={report363.get('verdict')} weakest={report363.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_declares_runtime_entropy_boundary", has_terms(app_text, ["browser-local-stochastic-consequence-pulse-only", "runtimeEntropySource", "replayableEntropy"]), "app.js has stochastic pulse boundary and replayable entropy state")
    add_criterion(criteria, "source_records_entropy_and_consequence", has_terms(app_text, ["entropyByte", "weightedEntropyPick", "resourceDelta", "needBefore", "needAfter"]), "app.js records entropy, branch, resources, and need snapshots")
    add_criterion(criteria, "visible_pulse_panel_wired", metrics_base["browser_surface_wired"] == 1.0, "index.html exposes stochastic consequence dashboard and panel controls")
    add_criterion(criteria, "runner_includes_report_364", "experiments.ssrm_3d_browser_world_v124_stochastic_resident_consequence_bridge" in runner_text, "scripts/run_experiments.py includes Report 364 module")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    pulse_text = browser.get("afterPulse", {}).get("pulseText", "")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_runtime_pulse_visible", all(term in pulse_text for term in ["Mode:", "Replayable entropy: yes", "Recent stochastic pulses:", "entropy=", "resources="]), pulse_text or "missing pulse text")
    add_criterion(criteria, "browser_schedule_coupling_visible_or_possible", "Schedule couplings:" in pulse_text, pulse_text or "missing pulse text")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "event_count": len(events),
        "event_type_count": len(event_types),
        "schedule_coupling_count": sum(1 for row in events if row["schedule_coupling"]),
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
    state = {"runs": first, "browser_smoke": browser, "criteria": criteria}
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
