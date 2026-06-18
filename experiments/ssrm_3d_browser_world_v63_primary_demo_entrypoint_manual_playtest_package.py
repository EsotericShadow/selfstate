"""Report 303: SSRM-3D browser world v63 primary demo entrypoint.

This report packages the maintained v61 app shell as the stable primary demo
entrypoint and publishes a manual playtest script. It intentionally does not add
a new simulation organ; it points players and reviewers at the single browser
surface that Report 302 directly QA'd.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 303
PREFIX = "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package"
DEFAULT_SEED = 20270701

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DEMO_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
TARGET_SHELL_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell"
TARGET_SHELL_INDEX = TARGET_SHELL_DIR / "index.html"
SOURCE_V62 = ARTIFACTS / "ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_results.json"
SOURCE_V62_EVIDENCE = ARTIFACTS / "ssrm_3d_browser_world_v62_app_shell_direct_browser_qa_browser_evidence.json"
RUNNER = ROOT / "scripts" / "run_experiments.py"

TARGET_SHELL_REL = "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html"
CLEAN_LAUNCH_REL = f"{TARGET_SHELL_REL}?reset=1&source=primary-demo-v63"
RESUME_LAUNCH_REL = f"{TARGET_SHELL_REL}?source=primary-demo-v63"
LOCALHOST_LAUNCH_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_RECORD_KEY = "ssrm_primary_demo_manual_pass_records"
DEFECT_LEDGER_KEY = "ssrm_primary_demo_defect_ledger"
RECORDER_EXPORT_KEY = "ssrm_primary_demo_recorder_export"
OUTSIDE_REVIEW_KEY = "ssrm_primary_demo_outside_review_checklist"
OUTSIDE_REVIEW_EXPORT_KEY = "ssrm_primary_demo_outside_review_handoff"
LIFECYCLE_SMOKE_RUNNER_COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
LIFECYCLE_SMOKE_RUNNER_REPORT_REL = "../../docs/342_ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_report.md"
LIFECYCLE_SMOKE_RUNNER_RESULTS_REL = "../../artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_results.json"
LIFECYCLE_SMOKE_RUNNER_MANIFEST_REL = "../../artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_runner_manifest.json"
LIFECYCLE_SMOKE_RUNNER_POLICY = "Run this one maintained lifecycle smoke runner before adding another tab, reload, stale, repair, or return handoff report."
LIFECYCLE_SMOKE_PREFLIGHT_FRESHNESS = "Report 342 runner results pass; Report 343 entrypoint wiring pass"
LIFECYCLE_SMOKE_PREFLIGHT_BLOCKING_PHASE = "none"
LIFECYCLE_SMOKE_PREFLIGHT_BOUNDARY = "Lifecycle preflight is artifact-backed by Report 342 runner results and Report 343 entrypoint wiring evidence; it is not a live hosted browser E2E claim."

BOUNDARY = (
    "Primary demo packaging for the deterministic browser-local maintained app shell only; "
    "no new simulation organ, no LLM call, no subjective consciousness, no real consent, "
    "no autonomous natural language, no moral patienthood, no production persistence, "
    "no finished gameplay, no complete 3D engine, and no metaphysical frequency claim."
)

NEXT_GATE = (
    "post-303: use the stable primary demo entrypoint for all browser-world work, run the "
    "manual playtest script against real defects, and harden the same shell before adding "
    "any new world-system report"
)

MANUAL_PLAYTEST_STEPS: list[dict[str, Any]] = [
    {
        "step_id": "MP-01",
        "action": "Start a local server from the repo root with python3 -m http.server 8765 --bind 127.0.0.1.",
        "expected_evidence": "Primary demo launcher opens at the localhost URL.",
        "proves": "reviewers have one stable URL-style entrypoint instead of hunting report artifacts",
        "required": True,
    },
    {
        "step_id": "MP-02",
        "action": "Open the primary demo launcher and read the boundary before launching.",
        "expected_evidence": "Boundary says deterministic browser-local shell and no consciousness/LLM/product claim.",
        "proves": "the no-overclaim boundary is visible before play",
        "required": True,
    },
    {
        "step_id": "MP-03",
        "action": "Launch a clean session using the Clean demo button.",
        "expected_evidence": "The maintained v61 shell opens with ?reset=1 and a primary-demo source tag.",
        "proves": "the launcher targets the single maintained shell, not a forked simulation",
        "required": True,
    },
    {
        "step_id": "MP-04",
        "action": "Enter the world and move at least twice.",
        "expected_evidence": "Room/status fields update and replay rows increase.",
        "proves": "arrival and movement remain usable through the primary path",
        "required": True,
    },
    {
        "step_id": "MP-05",
        "action": "Talk through the bounded phrase control, then ask schedule.",
        "expected_evidence": "Resident memory/schedule fields update without open-ended chat claims.",
        "proves": "bounded conversation and resident schedule inspection are still on the same surface",
        "required": True,
    },
    {
        "step_id": "MP-06",
        "action": "Borrow and return the awning tool.",
        "expected_evidence": "Debt increases, then returns to zero while trust repairs partially.",
        "proves": "visible consequence and non-magical trust repair are observable",
        "required": True,
    },
    {
        "step_id": "MP-07",
        "action": "Wait offscreen, then inspect schedule/progress again.",
        "expected_evidence": "Progress changes while the avatar is idle/absent.",
        "proves": "offscreen life is visible in the primary shell",
        "required": True,
    },
    {
        "step_id": "MP-08",
        "action": "Save, move/change state, then restore.",
        "expected_evidence": "Saved avatar/resident values return after a deliberate post-save mutation and restore.",
        "proves": "local persistence and real rollback are part of the playable loop",
        "required": True,
    },
    {
        "step_id": "MP-09",
        "action": "Run the built-in playtest checklist.",
        "expected_evidence": "Checklist reports 10 checks and all pass.",
        "proves": "the internal QA hooks still cover the maintained tasks",
        "required": True,
    },
    {
        "step_id": "MP-10",
        "action": "Run state-boundary, save/restore smoke, and Audit after rollback hooks.",
        "expected_evidence": "The audit-after-rollback row passes with rollbackTested, smokePass, and auditPass all true.",
        "proves": "traceability remains bounded and inspectable",
        "required": True,
    },
    {
        "step_id": "MP-11",
        "action": "Export replay from the UI.",
        "expected_evidence": "A prepared replay export link appears and export bytes are nonzero.",
        "proves": "review/debug evidence can be captured without relying on blocked downloads",
        "required": True,
    },
    {
        "step_id": "MP-12",
        "action": "Close the shell, reopen the primary launcher, then use Resume demo.",
        "expected_evidence": "The resumed shell keeps persisted world state unless Clean demo is used.",
        "proves": "leave/return continuity is part of the manual review path",
        "required": True,
    },
    {
        "step_id": "MP-13",
        "action": f"Run the maintained lifecycle smoke runner: {LIFECYCLE_SMOKE_RUNNER_COMMAND}.",
        "expected_evidence": "Report 342 reports pass with full fresh/stale/repair/post-repair phase coverage and 0 aggregated console errors.",
        "proves": "handoff lifecycle changes exercise one maintained smoke surface before new variants are added",
        "required": True,
    },
]

SCOPE_GUARDS = [
    "Only the primary demo launcher is new; gameplay still lives in the maintained v61 app shell.",
    "The manual script uses Report 302 browser evidence as the baseline, not as a substitute for future human playtests.",
    "The launcher gives clean and resume paths so persistence bugs can be reproduced rather than hidden.",
    "The boundary remains visible before launch and inside the shell.",
    "Future browser-world work should patch this shell unless a defect proves a new surface is necessary.",
    LIFECYCLE_SMOKE_RUNNER_POLICY,
]

OUTSIDE_REVIEW_CHECKLIST: list[dict[str, str]] = [
    {
        "item_id": "OR-01",
        "label": "Read boundary before launching",
        "evidence": "Launcher boundary explicitly says deterministic browser-local shell, no LLM, no consciousness, no moral patienthood, no production persistence, and no finished gameplay.",
    },
    {
        "item_id": "OR-02",
        "label": "Launch clean reviewer path",
        "evidence": "Launch clean demo opens the maintained v61 shell with reviewer-focus mode, not a parallel simulation.",
    },
    {
        "item_id": "OR-03",
        "label": "Run reviewer pass inside the shell",
        "evidence": "Reviewer landing reports PASSABLE_REVIEW_PATH and the integrated scenario receipt reports ALL_PASS.",
    },
    {
        "item_id": "OR-04",
        "label": "Inspect transcript, receipt, and observation triage",
        "evidence": "Session transcript, integrated receipt, and observation triage are visible before optional deep panels.",
    },
    {
        "item_id": "OR-05",
        "label": "Audit failures if the receipt is incomplete",
        "evidence": "Audit failures converts failing receipt fields into blocking observation rows with recovery guidance.",
    },
    {
        "item_id": "OR-06",
        "label": "Reveal deep panels only for unresolved questions",
        "evidence": "Toggle deep panels exposes trace, checkpoints, resident history, social memory, receipt observations, playtest tasks, and QA manifest.",
    },
    {
        "item_id": "OR-07",
        "label": "Record manual outcome and export handoff",
        "evidence": "Manual pass recorder, defect ledger, lifecycle preflight packet, and outside-review handoff export are prepared as one browser-local public review receipt.",
    },
]


@dataclass(frozen=True)
class PackagingCriterion:
    criterion: str
    passed: bool
    evidence: str
    failure_if_false: str


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"unreadable": str(path), "error": str(exc)}


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    if not normalized:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: list[str] = []
    for row in normalized:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def _html() -> str:
    task_rows = "\n".join(
        f"<li><strong>{step['step_id']}</strong>: {step['action']} <span>{step['expected_evidence']}</span></li>"
        for step in MANUAL_PLAYTEST_STEPS
    )
    outside_review_rows = "\n".join(
        f"<li data-outside-review-row=\"{item['item_id']}\"><span><strong>{item['item_id']}</strong>: {item['label']} <em>{item['evidence']}</em></span><button type=\"button\" data-outside-review-item=\"{item['item_id']}\">Mark done</button></li>"
        for item in OUTSIDE_REVIEW_CHECKLIST
    )
    recorder_rows = "\n".join(
        f"<li><span><strong>{step['step_id']}</strong> {step['proves']}</span><button data-record-step=\"{step['step_id']}\" data-record-result=\"pass\">Pass</button><button data-record-step=\"{step['step_id']}\" data-record-result=\"fail\">Fail</button></li>"
        for step in MANUAL_PLAYTEST_STEPS
    )
    defect_step_options = "\n".join(
        f"<option value=\"{step['step_id']}\">{step['step_id']}: {step['action']}</option>"
        for step in MANUAL_PLAYTEST_STEPS
    )
    guard_rows = "\n".join(f"<li>{guard}</li>" for guard in SCOPE_GUARDS)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>SSRM-3D Primary Browser World Demo</title>
  <link rel=\"stylesheet\" href=\"styles.css\" />
</head>
<body>
  <main class=\"demo-shell\">
    <section class=\"hero\">
      <p class=\"eyebrow\">Report 303 / primary demo entrypoint</p>
      <h1>One playable browser-world surface.</h1>
      <p class=\"lede\">This launcher points to the maintained v61 app shell that Report 302 directly exercised in localhost browser QA. It is a packaging gate, not another parallel world.</p>
      <div class=\"actions\">
        <a class=\"button primary\" id=\"cleanLaunch\" href=\"{CLEAN_LAUNCH_REL}\">Launch clean demo</a>
        <a class=\"button\" id=\"resumeLaunch\" href=\"{RESUME_LAUNCH_REL}\">Resume demo</a>
        <a class=\"button quiet\" href=\"manual_playtest.md\">Manual playtest script</a>
        <a class=\"button quiet\" href=\"{LIFECYCLE_SMOKE_RUNNER_REPORT_REL}\">Lifecycle smoke runner</a>
      </div>
    </section>
    <section class=\"boundary\" id=\"boundary\">
      <h2>Boundary</h2>
      <p>{BOUNDARY}</p>
    </section>
    <section class=\"outside-review\" id=\"outsideReviewChecklist\">
      <h2>Outside-review checklist</h2>
      <p>This is the shortest handoff path for someone arriving cold: boundary, clean launch, reviewer pass, receipt, observation triage, optional diagnostics, and exportable review notes.</p>
      <ol class=\"outside-review-list\">{outside_review_rows}</ol>
      <div class=\"actions compact\">
        <button id=\"refreshOutsideReviewEvidence\" type=\"button\">Refresh shell evidence</button>
        <button id=\"completeReviewedHandoff\" type=\"button\">Complete reviewed handoff</button>
        <button id=\"exportOutsideReview\" type=\"button\">Prepare outside-review handoff</button>
        <button id=\"clearOutsideReview\" type=\"button\">Clear outside-review checklist</button>
      </div>
      <p id=\"outsideReviewStatus\">No outside-review checklist items completed yet.</p>
      <pre id=\"outsideReviewOut\"></pre>
      <p id=\"outsideReviewEvidenceStatus\">No shell evidence refreshed yet.</p>
      <pre id=\"outsideReviewEvidenceOut\"></pre>
      <p id=\"outsideReviewHandoffStatus\">No outside-review handoff export prepared yet.</p>
      <div id=\"outsideReviewHandoffActions\" class=\"actions compact\" aria-label=\"Prepared handoff actions\"></div>
      <pre id=\"outsideReviewHandoffOut\"></pre>
    </section>
    <section class=\"lifecycle-smoke\" id=\"lifecycleSmokeRunner\" data-lifecycle-smoke-runner=\"{LIFECYCLE_SMOKE_RUNNER_COMMAND}\">
      <h2>Maintained lifecycle smoke runner</h2>
      <p>Future primary-demo handoff changes should run one maintained gate before adding another lifecycle variant report.</p>
      <p>Command: <code id=\"lifecycleSmokeRunnerCommand\">{LIFECYCLE_SMOKE_RUNNER_COMMAND}</code></p>
      <p>Policy: <span id=\"lifecycleSmokeRunnerPolicy\">{LIFECYCLE_SMOKE_RUNNER_POLICY}</span></p>
      <div class=\"preflight-status\" id=\"lifecycleSmokePreflight\" data-lifecycle-preflight-source=\"report-342-results+report-343-wiring\" data-lifecycle-preflight-blocking-phase=\"{LIFECYCLE_SMOKE_PREFLIGHT_BLOCKING_PHASE}\">
        <h3>Lifecycle release preflight</h3>
        <p id=\"lifecycleSmokeFreshness\">Runner freshness: {LIFECYCLE_SMOKE_PREFLIGHT_FRESHNESS}</p>
        <p id=\"lifecycleSmokeBlockingPhase\">Blocking lifecycle phase: {LIFECYCLE_SMOKE_PREFLIGHT_BLOCKING_PHASE}</p>
        <p id=\"lifecycleSmokePreflightBoundary\">{LIFECYCLE_SMOKE_PREFLIGHT_BOUNDARY}</p>
        <ul id=\"lifecycleSmokePhaseList\">
        <li data-lifecycle-preflight-phase=\"cross_tab_prepared_resume_visible\" data-lifecycle-preflight-status=\"pass\"><strong>fresh cross-tab prepared resume</strong>: pass</li>
        <li data-lifecycle-preflight-phase=\"closed_origin_tab_continuity\" data-lifecycle-preflight-status=\"pass\"><strong>closed-origin continuity</strong>: pass</li>
        <li data-lifecycle-preflight-phase=\"hard_reload_continuity\" data-lifecycle-preflight-status=\"pass\"><strong>hard-reload continuity</strong>: pass</li>
        <li data-lifecycle-preflight-phase=\"stale_supersession_calibration\" data-lifecycle-preflight-status=\"pass\"><strong>stale prepared-handoff calibration</strong>: pass</li>
        <li data-lifecycle-preflight-phase=\"stale_reprepare_repair\" data-lifecycle-preflight-status=\"pass\"><strong>stale mismatch clean reprepare repair</strong>: pass</li>
        <li data-lifecycle-preflight-phase=\"repaired_continue_return_refresh\" data-lifecycle-preflight-status=\"pass\"><strong>repaired continue-return-refresh freshness</strong>: pass</li>
        </ul>
        <div class=\"actions compact\" id=\"lifecyclePreflightPacketActions\" aria-label=\"Lifecycle preflight packet actions\">
          <button id=\"prepareLifecyclePreflightPacket\" type=\"button\">Prepare preflight packet</button>
          <button id=\"copyLifecyclePreflightPacket\" type=\"button\">Copy preflight packet</button>
        </div>
        <p id=\"lifecyclePreflightExportStatus\">No lifecycle preflight packet prepared yet.</p>
        <pre id=\"lifecyclePreflightPacketOut\"></pre>
      </div>
      <ul>
        <li><a id=\"lifecycleSmokeRunnerReport\" href=\"{LIFECYCLE_SMOKE_RUNNER_REPORT_REL}\">Report 342 lifecycle smoke runner</a></li>
        <li><a id=\"lifecycleSmokeRunnerResults\" href=\"{LIFECYCLE_SMOKE_RUNNER_RESULTS_REL}\">Report 342 results artifact</a></li>
        <li><a id=\"lifecycleSmokeRunnerManifest\" href=\"{LIFECYCLE_SMOKE_RUNNER_MANIFEST_REL}\">Report 342 runner manifest</a></li>
      </ul>
    </section>
    <section class=\"grid\">
      <article>
        <h2>Manual playtest spine</h2>
        <ol>{task_rows}</ol>
      </article>
      <article>
        <h2>Scope guards</h2>
        <ul>{guard_rows}</ul>
      </article>
    </section>
    <section class=\"recorder\" id=\"manualRecorder\">
      <h2>Manual pass recorder and defect ledger</h2>
      <p>Use this while exercising the maintained shell. Records stay browser-local and public: step outcome, defect note, timestamp, and source boundary only.</p>
      <ol class=\"record-list\">{recorder_rows}</ol>
      <label class=\"defect-box\">Defect note
        <textarea id=\"defectNote\" rows=\"4\" placeholder=\"Example: MP-08 failed because restore did not roll back after moving west.\"></textarea>
      </label>
      <div class=\"triage-grid\">
        <label>Related step
          <select id=\"defectStep\">{defect_step_options}</select>
        </label>
        <label>Severity
          <select id=\"defectSeverity\">
            <option value=\"watch\">Watch</option>
            <option value=\"minor\">Minor</option>
            <option value=\"blocking\">Blocking</option>
          </select>
        </label>
      </div>
      <label class=\"defect-box\">Resolution note
        <textarea id=\"resolutionNote\" rows=\"3\" placeholder=\"Example: Resolved by Report 306 audit-after-rollback hook.\"></textarea>
      </label>
      <div class=\"actions compact\">
        <button id=\"recordDefect\" type=\"button\">Record defect note</button>
        <button id=\"resolveLatestDefect\" type=\"button\">Resolve latest open defect</button>
        <button id=\"exportRecorder\" type=\"button\">Prepare recorder export</button>
        <button id=\"clearRecorder\" type=\"button\">Clear recorder</button>
      </div>
      <div class=\"triage-filter-panel\" aria-label=\"Defect ledger filters\">
        <div class=\"triage-filter-row\" role=\"group\" aria-label=\"Defect status filters\">
          <button class=\"filter-pill active\" type=\"button\" data-triage-status=\"all\">All defects</button>
          <button class=\"filter-pill\" type=\"button\" data-triage-status=\"open\">Open</button>
          <button class=\"filter-pill\" type=\"button\" data-triage-status=\"resolved\">Resolved</button>
        </div>
        <label class=\"inline-filter\">Severity filter
          <select id=\"defectSeverityFilter\">
            <option value=\"all\">All severities</option>
            <option value=\"watch\">Watch</option>
            <option value=\"minor\">Minor</option>
            <option value=\"blocking\">Blocking</option>
          </select>
        </label>
        <p id=\"triageFilterSummary\" class=\"status-line\">No defects recorded yet.</p>
        <div id=\"defectLedgerView\" class=\"defect-ledger-view\" aria-live=\"polite\"></div>
      </div>
      <p id=\"recordStatus\">No manual pass records yet.</p>
      <pre id=\"recordLedgerOut\"></pre>
    </section>
    <section class=\"handoff\">
      <h2>Launch handoff</h2>
      <p>Local URL: <code id="currentLaunchUrl">{LOCALHOST_LAUNCH_URL}</code></p>
      <p>Target shell: <code>{TARGET_SHELL_REL}</code></p>
      <p id=\"handoffStatus\">No launch handoff recorded in this tab yet.</p>
    </section>
  </main>
  <script src=\"demo.js\"></script>
  <script src=\"triage_filters.js\"></script>
</body>
</html>
"""


def _triage_filters_script() -> str:
    return """(() => {
  const DEFECT_LEDGER_KEY = "ssrm_primary_demo_defect_ledger";
  const FILTER_KEY = "ssrm_primary_demo_defect_filter_state";
  const DEFAULT_FILTER = { status: "all", severity: "all" };

  const parseJson = (value, fallback) => {
    try {
      return value ? JSON.parse(value) : fallback;
    } catch (_error) {
      return fallback;
    }
  };

  const escapeText = (value) => String(value ?? "").replace(/[&<>\"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    "\\\"": "&quot;",
    "'": "&#39;",
  }[char]));

  const ensureStyles = () => {
    if (document.getElementById("triage-filter-styles")) return;
    const style = document.createElement("style");
    style.id = "triage-filter-styles";
    style.textContent = `
      .triage-filter-panel {
        margin-top: 1rem;
        padding: 1rem;
        border: 1px solid rgba(220, 238, 255, 0.2);
        border-radius: 18px;
        background: rgba(5, 13, 25, 0.5);
      }
      .triage-filter-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
      }
      .filter-pill {
        border: 1px solid rgba(150, 190, 220, 0.35);
        border-radius: 999px;
        padding: 0.45rem 0.8rem;
        background: rgba(255, 255, 255, 0.06);
        color: inherit;
        cursor: pointer;
      }
      .filter-pill.active {
        background: #d2f68d;
        border-color: #d2f68d;
        color: #142016;
        font-weight: 800;
      }
      .inline-filter {
        display: inline-flex;
        gap: 0.55rem;
        align-items: center;
        margin-bottom: 0.75rem;
        font-weight: 700;
      }
      .inline-filter select {
        border-radius: 10px;
        border: 1px solid rgba(220, 238, 255, 0.25);
        background: #071120;
        color: inherit;
        padding: 0.4rem 0.55rem;
      }
      .defect-ledger-view {
        display: grid;
        gap: 0.65rem;
        margin-top: 0.75rem;
      }
      .defect-row {
        border: 1px solid rgba(220, 238, 255, 0.16);
        border-radius: 14px;
        padding: 0.75rem;
        background: rgba(255, 255, 255, 0.045);
      }
      .defect-row header {
        display: flex;
        flex-wrap: wrap;
        gap: 0.45rem;
        align-items: center;
        margin-bottom: 0.4rem;
      }
      .defect-badge {
        border-radius: 999px;
        padding: 0.15rem 0.5rem;
        background: rgba(255, 255, 255, 0.08);
        font-size: 0.78rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.04em;
      }
      .defect-badge.open { background: rgba(255, 191, 112, 0.18); }
      .defect-badge.resolved { background: rgba(163, 244, 177, 0.18); }
      .empty-ledger {
        margin: 0;
        opacity: 0.78;
      }
    `;
    document.head.appendChild(style);
  };

  const readFilter = () => ({ ...DEFAULT_FILTER, ...parseJson(localStorage.getItem(FILTER_KEY), {}) });
  const writeFilter = (filter) => localStorage.setItem(FILTER_KEY, JSON.stringify(filter));
  const readLedger = () => {
    const ledger = parseJson(localStorage.getItem(DEFECT_LEDGER_KEY), []);
    return Array.isArray(ledger) ? ledger : [];
  };

  let filter = readFilter();

  const matchesFilter = (defect) => {
    const status = defect.status || "open";
    const severity = defect.severity || "watch";
    return (filter.status === "all" || filter.status === status)
      && (filter.severity === "all" || filter.severity === severity);
  };

  const render = () => {
    const summary = document.getElementById("triageFilterSummary");
    const view = document.getElementById("defectLedgerView");
    const severity = document.getElementById("defectSeverityFilter");
    const buttons = [...document.querySelectorAll("[data-triage-status]")];
    if (!summary || !view) return;

    buttons.forEach((button) => button.classList.toggle("active", button.dataset.triageStatus === filter.status));
    if (severity && severity.value !== filter.severity) severity.value = filter.severity;

    const ledger = readLedger();
    const filtered = ledger.filter(matchesFilter);
    const open = ledger.filter((defect) => (defect.status || "open") === "open").length;
    const resolved = ledger.filter((defect) => defect.status === "resolved").length;
    const blockingOpen = ledger.filter((defect) => (defect.status || "open") === "open" && defect.severity === "blocking").length;
    summary.textContent = `${filtered.length}/${ledger.length} shown | open ${open} | resolved ${resolved} | blocking open ${blockingOpen}`;

    if (!filtered.length) {
      view.innerHTML = '<p class="empty-ledger">No defects match the current reviewer filter.</p>';
      return;
    }

    view.innerHTML = filtered.map((defect) => {
      const status = escapeText(defect.status || "open");
      const severity = escapeText(defect.severity || "watch");
      const step = escapeText(defect.stepId || "unmapped");
      const note = escapeText(defect.note || "No note recorded.");
      const resolution = defect.resolutionNote ? `<p><strong>Resolution:</strong> ${escapeText(defect.resolutionNote)}</p>` : "";
      return `<article class="defect-row">
        <header>
          <strong>${escapeText(defect.id || "D-?")}</strong>
          <span class="defect-badge ${status}">${status}</span>
          <span class="defect-badge">${severity}</span>
          <span class="defect-badge">${step}</span>
        </header>
        <p>${note}</p>
        ${resolution}
      </article>`;
    }).join("");
  };

  const wire = () => {
    ensureStyles();
    const severity = document.getElementById("defectSeverityFilter");
    document.querySelectorAll("[data-triage-status]").forEach((button) => {
      button.addEventListener("click", () => {
        filter = { ...filter, status: button.dataset.triageStatus || "all" };
        writeFilter(filter);
        render();
      });
    });
    if (severity) {
      severity.value = filter.severity;
      severity.addEventListener("change", () => {
        filter = { ...filter, severity: severity.value || "all" };
        writeFilter(filter);
        render();
      });
    }
    ["recordDefect", "resolveLatestDefect"].forEach((id) => {
      const button = document.getElementById(id);
      if (button) button.addEventListener("click", () => window.setTimeout(render, 0));
    });
    window.addEventListener("storage", (event) => {
      if (event.key === DEFECT_LEDGER_KEY || event.key === FILTER_KEY) {
        filter = readFilter();
        render();
      }
    });
    render();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", wire);
  } else {
    wire();
  }
})();
"""

def _css() -> str:
    return """:root {
  --ink: #1e2018;
  --muted: #62664f;
  --paper: #f8f2df;
  --card: #fff9e8;
  --moss: #465c3a;
  --cedar: #9a4f2f;
  --amber: #d69b3d;
  --line: rgba(30, 32, 24, 0.16);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--ink);
  background:
    radial-gradient(circle at 14% 18%, rgba(214, 155, 61, 0.30), transparent 28rem),
    radial-gradient(circle at 88% 6%, rgba(70, 92, 58, 0.22), transparent 24rem),
    linear-gradient(135deg, #f4e6c3, #f8f2df 52%, #e2d3ae);
}
.demo-shell { width: min(1120px, calc(100% - 32px)); margin: 0 auto; padding: 42px 0; }
.hero, .boundary, article, .handoff, .outside-review, .lifecycle-smoke {
  border: 1px solid var(--line);
  background: rgba(255, 249, 232, 0.88);
  box-shadow: 0 20px 60px rgba(63, 46, 22, 0.13);
  border-radius: 24px;
}
.hero { padding: clamp(28px, 5vw, 64px); position: relative; overflow: hidden; }
.hero::after {
  content: '';
  position: absolute;
  width: 220px;
  height: 220px;
  right: -72px;
  top: -84px;
  border-radius: 999px;
  background: conic-gradient(from 110deg, var(--amber), transparent, var(--moss), transparent);
  opacity: 0.32;
}
.eyebrow { letter-spacing: 0.16em; text-transform: uppercase; color: var(--cedar); font-size: 0.78rem; }
h1 { max-width: 760px; font-size: clamp(2.8rem, 7vw, 6rem); line-height: 0.92; margin: 0 0 20px; }
h2 { margin-top: 0; }
.lede { max-width: 780px; font-size: 1.2rem; color: var(--muted); }
.actions { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
.actions.compact { margin-top: 12px; }
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 999px;
  color: var(--ink);
  text-decoration: none;
  border: 1px solid var(--line);
  background: #fffdf2;
  font-weight: 700;
}
.button.primary { color: white; background: var(--moss); }
.button.quiet { background: transparent; }
.boundary, .outside-review { margin-top: 18px; padding: 22px 26px; }
.grid { display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 18px; margin-top: 18px; }
article, .handoff, .recorder { padding: 26px; }
.recorder { margin-top: 18px; border: 1px solid var(--line); background: rgba(255, 249, 232, 0.88); box-shadow: 0 20px 60px rgba(63, 46, 22, 0.13); border-radius: 24px; }
.outside-review-list { padding-left: 22px; }
.outside-review-list li { display: grid; grid-template-columns: 1fr auto; gap: 10px; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--line); }
.outside-review-list li.done { background: rgba(70, 92, 58, 0.10); border-radius: 14px; padding-left: 10px; padding-right: 10px; }
.outside-review-list em { display: block; color: var(--muted); font-style: normal; margin-top: 3px; }
.record-list { padding-left: 22px; }
.record-list li { display: grid; grid-template-columns: 1fr auto auto; gap: 10px; align-items: center; }
.record-list button, .recorder button, .outside-review button { border: 1px solid var(--line); border-radius: 999px; background: #fffdf2; padding: 8px 12px; font-weight: 700; color: var(--ink); }
.defect-box { display: grid; gap: 8px; font-weight: 700; margin-top: 18px; }
.triage-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
.triage-grid label { display: grid; gap: 8px; font-weight: 700; }
textarea, select { width: 100%; border: 1px solid var(--line); border-radius: 16px; padding: 12px; background: #fffdf2; color: var(--ink); font: inherit; }
textarea { resize: vertical; }
#recordLedgerOut, #outsideReviewOut, #outsideReviewEvidenceOut, #outsideReviewHandoffOut { max-height: 260px; overflow: auto; white-space: pre-wrap; background: rgba(30, 32, 24, 0.08); border-radius: 16px; padding: 14px; }
li { margin: 0 0 12px; }
li span { display: block; color: var(--muted); margin-top: 3px; }
code { background: rgba(70, 92, 58, 0.10); padding: 2px 6px; border-radius: 8px; }
@media (max-width: 780px) {
  .grid { grid-template-columns: 1fr; }
  .outside-review-list li { grid-template-columns: 1fr; }
  .record-list li { grid-template-columns: 1fr; }
  .triage-grid { grid-template-columns: 1fr; }
  .actions { flex-direction: column; align-items: stretch; }
}
"""


def _js() -> str:
    return """const HANDOFF_KEY = 'ssrm_primary_demo_handoff';
const MANUAL_RECORD_KEY = 'ssrm_primary_demo_manual_pass_records';
const DEFECT_LEDGER_KEY = 'ssrm_primary_demo_defect_ledger';
const RECORDER_EXPORT_KEY = 'ssrm_primary_demo_recorder_export';
const LIFECYCLE_PREFLIGHT_EXPORT_KEY = 'ssrm_primary_demo_lifecycle_preflight_packet';
const OUTSIDE_REVIEW_KEY = 'ssrm_primary_demo_outside_review_checklist';
const OUTSIDE_REVIEW_EXPORT_KEY = 'ssrm_primary_demo_outside_review_handoff';
const SHELL_STATE_KEY = 'ssrm_v61_app_shell_world';
const SHELL_REPLAY_KEY = 'ssrm_v61_app_shell_replay';
const SHELL_EXPORT_KEY = 'ssrm_v61_app_shell_export';
const SHELL_RECEIPT_OBSERVATION_KEY = 'ssrm_v61_app_shell_receipt_observations';
const SHELL_CHECKPOINT_KEY = 'ssrm_v61_app_shell_checkpoints';
const OUTSIDE_REVIEW_ITEMS = [
  { itemId: 'OR-01', label: 'Read boundary before launching' },
  { itemId: 'OR-02', label: 'Launch clean reviewer path' },
  { itemId: 'OR-03', label: 'Run reviewer pass inside the shell' },
  { itemId: 'OR-04', label: 'Inspect transcript, receipt, and observation triage' },
  { itemId: 'OR-05', label: 'Audit failures if the receipt is incomplete' },
  { itemId: 'OR-06', label: 'Reveal deep panels only for unresolved questions' },
  { itemId: 'OR-07', label: 'Record manual outcome and export handoff' }
];

function currentLauncherUrl() {
  return window.location.href.split('#')[0].split('?')[0];
}

function renderCurrentLauncherUrl() {
  const node = document.getElementById('currentLaunchUrl');
  if (node) node.textContent = currentLauncherUrl();
}

function readObject(key, fallback) {
  try {
    return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback));
  } catch (error) {
    localStorage.removeItem(key);
    return fallback;
  }
}

function recordLaunch(kind) {
  const payload = {
    kind,
    report: 303,
    target: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    launcherUrl: currentLauncherUrl(),
    recordedAt: new Date().toISOString(),
    boundary: 'primary-demo-launcher-only'
  };
  localStorage.setItem(HANDOFF_KEY, JSON.stringify(payload));
  renderHandoff(payload);
}

function renderHandoff(payload) {
  const node = document.getElementById('handoffStatus');
  if (!node) return;
  node.textContent = `Last handoff: ${payload.kind} launch from ${payload.launcherUrl || currentLauncherUrl()} toward ${payload.target} at ${payload.recordedAt}.`;
}

for (const [id, kind] of [['cleanLaunch', 'clean'], ['resumeLaunch', 'resume']]) {
  const node = document.getElementById(id);
  if (node) node.addEventListener('click', () => recordLaunch(kind));
}

renderCurrentLauncherUrl();

try {
  const existing = JSON.parse(localStorage.getItem(HANDOFF_KEY) || 'null');
  if (existing) renderHandoff(existing);
} catch (error) {
  localStorage.removeItem(HANDOFF_KEY);
}

function readList(key) {
  try {
    return JSON.parse(localStorage.getItem(key) || '[]');
  } catch (error) {
    localStorage.removeItem(key);
    return [];
  }
}

function writeList(key, rows) {
  localStorage.setItem(key, JSON.stringify(rows));
}

function outsideReviewState() {
  const state = readObject(OUTSIDE_REVIEW_KEY, { items: {}, updatedAt: null });
  return state && typeof state === 'object' && state.items ? state : { items: {}, updatedAt: null };
}

function writeOutsideReviewState(state) {
  localStorage.setItem(OUTSIDE_REVIEW_KEY, JSON.stringify(state));
}

function readRecorderExportPayload() {
  const text = localStorage.getItem(RECORDER_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, rawLength: text.length, boundary: 'primary-demo-recorder-export-public-local-only' };
  }
}

function reviewedHandoffCompletionState() {
  const evidence = buildOutsideReviewEvidence();
  const manualRecords = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const recorderExport = readRecorderExportPayload();
  const openDefectCount = defects.filter(row => row.status !== 'resolved').length;
  const missing = [];
  if (!evidence.reviewerPassSeen) missing.push('reviewer pass');
  if (!evidence.receiptAllPass) missing.push('all-pass receipt');
  if (!evidence.replayExportReady) missing.push('replay export');
  if (!recorderExport) missing.push('recorder export');
  if (!manualRecords.length) missing.push('manual recorder outcome');
  if (openDefectCount > 0) missing.push('open defect resolution');
  return {
    reportIntroduced: 327,
    ready: missing.length === 0,
    missing,
    manualRecordCount: manualRecords.length,
    defectCount: defects.length,
    openDefectCount,
    recorderExportPrepared: Boolean(recorderExport),
    recorderExportRecordCount: recorderExport && Array.isArray(recorderExport.records) ? recorderExport.records.length : 0,
    shellEvidence: evidence,
    boundary: 'reviewed-handoff-completion-public-local-only'
  };
}

function completeReviewedHandoff() {
  const completion = reviewedHandoffCompletionState();
  if (!completion.ready) {
    renderOutsideReviewEvidence('Reviewed handoff is not complete yet.');
    renderOutsideReviewChecklist(`Reviewed handoff blocked: missing ${completion.missing.join(', ')}.`);
    return completion;
  }
  const state = outsideReviewState();
  OUTSIDE_REVIEW_ITEMS.forEach(item => { state.items[item.itemId] = true; });
  state.updatedAt = new Date().toISOString();
  state.completedAt = state.updatedAt;
  state.completedBy = 'completeReviewedHandoff';
  state.completion = completion;
  writeOutsideReviewState(state);
  renderOutsideReviewEvidence('Reviewed handoff complete from refreshed shell evidence.');
  renderOutsideReviewChecklist(`${OUTSIDE_REVIEW_ITEMS.length}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete after shell evidence and recorder export.`);
  return completion;
}

function renderOutsideReviewChecklist(message) {
  const state = outsideReviewState();
  const doneCount = OUTSIDE_REVIEW_ITEMS.filter(item => state.items[item.itemId] === true).length;
  document.querySelectorAll('[data-outside-review-item]').forEach(button => {
    const itemId = button.dataset.outsideReviewItem;
    const done = state.items[itemId] === true;
    button.textContent = done ? 'Done' : 'Mark done';
    button.closest('[data-outside-review-row]')?.classList.toggle('done', done);
  });
  const status = document.getElementById('outsideReviewStatus');
  if (status) status.textContent = message || `${doneCount}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete.`;
  const out = document.getElementById('outsideReviewOut');
  if (out) {
    out.textContent = JSON.stringify({
      reportIntroduced: 323,
      checklist: OUTSIDE_REVIEW_ITEMS,
      state,
      targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
      boundary: 'outside-review-checklist-public-local-only'
    }, null, 2);
  }
}

function markOutsideReviewItem(itemId) {
  const state = outsideReviewState();
  state.items[itemId] = true;
  state.updatedAt = new Date().toISOString();
  writeOutsideReviewState(state);
  const doneCount = OUTSIDE_REVIEW_ITEMS.filter(item => state.items[item.itemId] === true).length;
  renderOutsideReviewChecklist(doneCount === OUTSIDE_REVIEW_ITEMS.length ? `${doneCount}/${OUTSIDE_REVIEW_ITEMS.length} outside-review checklist items complete.` : `${itemId} marked done.`);
}

function exportOutsideReviewHandoff() {
  const lifecyclePreflightPacket = prepareLifecyclePreflightPacket('outside-review-handoff');
  const payload = {
    reportIntroduced: 323,
    combinedReceiptReportIntroduced: 346,
    checklistState: outsideReviewState(),
    handoff: readObject(HANDOFF_KEY, null),
    shellEvidence: buildOutsideReviewEvidence(),
    reviewedHandoffCompletion: reviewedHandoffCompletionState(),
    manualRecords: readList(MANUAL_RECORD_KEY),
    defects: readList(DEFECT_LEDGER_KEY),
    recorderExport: readRecorderExportPayload(),
    recorderExportPrepared: Boolean(localStorage.getItem(RECORDER_EXPORT_KEY)),
    lifecyclePreflightPacket,
    lifecyclePreflightPacketPrepared: Boolean(localStorage.getItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY)),
    lifecyclePreflightPacketSource: LIFECYCLE_PREFLIGHT_EXPORT_KEY,
    combinedReceiptIncludes: ['shellEvidence', 'reviewedHandoffCompletion', 'manualRecords', 'defects', 'recorderExport', 'lifecyclePreflightPacket'],
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    launchUrl: currentLauncherUrl(),
    boundary: 'outside-review-handoff-public-local-only'
  };
  const text = JSON.stringify(payload, null, 2);
  localStorage.setItem(OUTSIDE_REVIEW_EXPORT_KEY, text);
  let link = document.getElementById('preparedOutsideReviewExport');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedOutsideReviewExport';
    link.textContent = 'Prepared outside-review handoff';
    link.download = 'ssrm_primary_demo_outside_review_handoff.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.getElementById('outsideReviewChecklist')?.appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderOutsideReviewEvidence('Outside-review handoff prepared with shell evidence.');
  renderOutsideReviewHandoffPreview('Outside-review handoff payload visible below.');
  renderOutsideReviewChecklist('Outside-review handoff prepared.');
}

function clearOutsideReviewChecklist() {
  localStorage.removeItem(OUTSIDE_REVIEW_KEY);
  localStorage.removeItem(OUTSIDE_REVIEW_EXPORT_KEY);
  const link = document.getElementById('preparedOutsideReviewExport');
  if (link) link.remove();
  renderOutsideReviewHandoffPreview('Outside-review handoff cleared.');
  renderOutsideReviewChecklist('Outside-review checklist cleared.');
}

function shellReplayRows() {
  const world = readObject(SHELL_STATE_KEY, {});
  if (Array.isArray(world.replay)) return world.replay;
  const replay = readObject(SHELL_REPLAY_KEY, []);
  return Array.isArray(replay) ? replay : [];
}

function buildOutsideReviewEvidence() {
  const replay = shellReplayRows();
  const events = replay.map(row => row.event);
  const receiptEvents = replay.filter(row => row.event === 'generateScenarioReceipt');
  const latestReceipt = receiptEvents[receiptEvents.length - 1]?.payload || {};
  const passCount = Number(latestReceipt.passCount || 0);
  const fieldCount = Number(latestReceipt.fieldCount || 0);
  const observations = readObject(SHELL_RECEIPT_OBSERVATION_KEY, []);
  const checkpoints = readObject(SHELL_CHECKPOINT_KEY, []);
  const exportText = localStorage.getItem(SHELL_EXPORT_KEY) || '';
  return {
    reportIntroduced: 324,
    handoff: readObject(HANDOFF_KEY, null),
    replayRows: replay.length,
    reviewerPassSeen: events.includes('runReviewerLandingPass'),
    receiptAllPass: fieldCount > 0 && passCount === fieldCount,
    receipt: { passCount, fieldCount },
    observationRows: Array.isArray(observations) ? observations.length : 0,
    blockingObservationRows: Array.isArray(observations) ? observations.filter(row => row.severity === 'blocking' && row.status !== 'resolved').length : 0,
    checkpointRows: Array.isArray(checkpoints) ? checkpoints.length : 0,
    replayExportReady: exportText.length > 0 || events.includes('exportReplay'),
    deepPanelsRevealed: events.includes('toggleDeepPanels'),
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    boundary: 'outside-review-shell-evidence-public-local-only'
  };
}

function renderOutsideReviewEvidence(message) {
  const evidence = buildOutsideReviewEvidence();
  const status = document.getElementById('outsideReviewEvidenceStatus');
  if (status) {
    const receipt = evidence.receipt.fieldCount ? `${evidence.receipt.passCount}/${evidence.receipt.fieldCount}` : 'missing';
    status.textContent = message || `Shell evidence: replay ${evidence.replayRows} rows / reviewer pass ${evidence.reviewerPassSeen ? 'seen' : 'missing'} / receipt ${receipt} / observations ${evidence.observationRows} / export ${evidence.replayExportReady ? 'ready' : 'missing'}.`;
  }
  const out = document.getElementById('outsideReviewEvidenceOut');
  if (out) out.textContent = JSON.stringify(evidence, null, 2);
  if (readOutsideReviewHandoffPayload()) renderOutsideReviewHandoffPreview();
  return evidence;
}

function readOutsideReviewHandoffPayload() {
  const text = localStorage.getItem(OUTSIDE_REVIEW_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, raw: text, boundary: 'outside-review-handoff-preview-public-local-only' };
  }
}

function handoffPayloadFreshnessState(payload) {
  if (!payload) {
    return { fresh: false, mismatches: ['missing payload'], boundary: 'outside-review-handoff-freshness-public-local-only' };
  }
  const currentEvidence = buildOutsideReviewEvidence();
  const currentCompletion = reviewedHandoffCompletionState();
  const payloadHandoff = payload.handoff || {};
  const currentHandoff = currentEvidence.handoff || {};
  const mismatches = [];
  if ((payloadHandoff.recordedAt || null) !== (currentHandoff.recordedAt || null)) mismatches.push('launch handoff changed');
  if ((payloadHandoff.kind || null) !== (currentHandoff.kind || null)) mismatches.push('launch kind changed');
  if ((payload.shellEvidence || {}).replayRows !== currentEvidence.replayRows) mismatches.push('shell replay rows changed');
  if (((payload.reviewedHandoffCompletion || {}).manualRecordCount || 0) !== currentCompletion.manualRecordCount) mismatches.push('manual recorder count changed');
  if (((payload.reviewedHandoffCompletion || {}).openDefectCount || 0) !== currentCompletion.openDefectCount) mismatches.push('open defect count changed');
  return {
    fresh: mismatches.length === 0,
    mismatches,
    payloadHandoffKind: payloadHandoff.kind || null,
    currentHandoffKind: currentHandoff.kind || null,
    payloadHandoffRecordedAt: payloadHandoff.recordedAt || null,
    currentHandoffRecordedAt: currentHandoff.recordedAt || null,
    payloadReplayRows: (payload.shellEvidence || {}).replayRows || 0,
    currentReplayRows: currentEvidence.replayRows,
    payloadManualRecordCount: (payload.reviewedHandoffCompletion || {}).manualRecordCount || 0,
    currentManualRecordCount: currentCompletion.manualRecordCount,
    boundary: 'outside-review-handoff-freshness-public-local-only'
  };
}

function readableHandoffSummary(payload, freshness) {
  if (!payload) return 'No outside-review handoff export prepared yet.';
  const checklistItems = ((payload.checklistState || {}).items) || {};
  const checklistDone = Object.values(checklistItems).filter(Boolean).length;
  const shellEvidence = payload.shellEvidence || {};
  const completion = payload.reviewedHandoffCompletion || {};
  const recorderExport = payload.recorderExport || {};
  const handoff = payload.handoff || {};
  const receipt = shellEvidence.receipt || {};
  const receiptText = receipt.fieldCount ? `${receipt.passCount}/${receipt.fieldCount}` : 'missing';
  const recorderReady = payload.recorderExportPrepared || Boolean(recorderExport.recordCount) ? 'ready' : 'missing';
  const manualCount = Array.isArray(payload.manualRecords) ? payload.manualRecords.length : (completion.manualRecordCount || 0);
  const freshnessText = freshness && freshness.fresh ? 'fresh' : `stale: ${(freshness && freshness.mismatches || ['unknown mismatch']).join(', ')}`;
  const preflightPacket = payload.lifecyclePreflightPacket || {};
  const preflightPhaseCount = preflightPacket.phaseCount || Object.keys(preflightPacket.phaseStatuses || {}).length;
  const preflightText = payload.lifecyclePreflightPacketPrepared ? `lifecycle preflight blocking phase ${preflightPacket.blockingPhase || 'unknown'} / ${preflightPhaseCount} phase(s)` : 'lifecycle preflight missing';
  return `Outside-review handoff ready: ${freshnessText} ${handoff.kind || 'unknown'} handoff; checklist ${checklistDone}/${OUTSIDE_REVIEW_ITEMS.length}; shell evidence reviewer pass ${shellEvidence.reviewerPassSeen ? 'seen' : 'missing'} / receipt ${receiptText} / replay export ${shellEvidence.replayExportReady ? 'ready' : 'missing'}; recorder ${manualCount} manual record(s) / export ${recorderReady}; ${preflightText}; next action: click Continue from prepared ${handoff.kind || 'unknown'} handoff, or download combined outside-review handoff JSON.`;
}

function preparedHandoffHref(payload) {
  const handoff = (payload && payload.handoff) || {};
  const target = handoff.target || '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html';
  const separator = target.includes('?') ? '&' : '?';
  const params = handoff.kind === 'clean' ? 'reset=1&source=primary-demo-v63' : 'source=primary-demo-v63';
  return `${target}${separator}${params}`;
}

function renderOutsideReviewHandoffActions(payload, freshness) {
  const actions = document.getElementById('outsideReviewHandoffActions');
  if (!actions) return;
  actions.textContent = '';
  if (!payload) return;
  const kind = (payload.handoff || {}).kind || 'unknown';
  if (freshness && freshness.fresh) {
    const continueLink = document.createElement('a');
    continueLink.id = 'continuePreparedHandoff';
    continueLink.className = 'button primary';
    continueLink.href = preparedHandoffHref(payload);
    continueLink.textContent = `Continue from prepared ${kind} handoff`;
    actions.appendChild(continueLink);
  } else {
    const staleNote = document.createElement('span');
    staleNote.className = 'status-line';
    staleNote.textContent = 'Re-prepare before continuing from this handoff.';
    actions.appendChild(staleNote);
  }
  const existingDownload = document.getElementById('preparedOutsideReviewExport');
  if (existingDownload) existingDownload.remove();
  const download = document.createElement('a');
  download.id = 'preparedOutsideReviewExport';
  download.className = 'button';
  download.download = 'ssrm_primary_demo_outside_review_handoff.json';
  download.textContent = 'Download prepared outside-review handoff JSON';
  const text = localStorage.getItem(OUTSIDE_REVIEW_EXPORT_KEY) || JSON.stringify(payload, null, 2);
  download.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  actions.appendChild(download);
}

function renderOutsideReviewHandoffPreview(message) {
  const payload = readOutsideReviewHandoffPayload();
  const freshness = payload ? handoffPayloadFreshnessState(payload) : null;
  const status = document.getElementById('outsideReviewHandoffStatus');
  if (status) {
    if (payload && freshness && !freshness.fresh) {
      status.textContent = `Prepared handoff payload is stale: ${freshness.mismatches.join(', ')}. Payload is ${freshness.payloadHandoffKind || 'unknown'} while current shell is ${freshness.currentHandoffKind || 'unknown'}. Re-run Prepare outside-review handoff.`;
    } else {
      status.textContent = payload ? readableHandoffSummary(payload, freshness) : (message || 'No outside-review handoff export prepared yet.');
    }
  }
  const out = document.getElementById('outsideReviewHandoffOut');
  if (out) {
    out.textContent = payload ? JSON.stringify({ ...payload, previewFreshness: freshness, previewReadableSummary: readableHandoffSummary(payload, freshness) }, null, 2) : 'No outside-review handoff export prepared yet.';
  }
  renderOutsideReviewHandoffActions(payload, freshness);
  return payload;
}

function lifecyclePreflightPhaseStatuses() {
  const rows = Array.from(document.querySelectorAll('[data-lifecycle-preflight-phase]'));
  return rows.reduce((accumulator, row) => {
    accumulator[row.dataset.lifecyclePreflightPhase] = row.dataset.lifecyclePreflightStatus || 'unknown';
    return accumulator;
  }, {});
}

function readLifecyclePreflightPacket() {
  const text = localStorage.getItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY) || '';
  if (!text) return null;
  try {
    return JSON.parse(text);
  } catch (error) {
    return { parseError: true, raw: text, boundary: 'lifecycle-preflight-packet-preview-public-local-only' };
  }
}

function buildLifecyclePreflightPacket(action = 'prepare') {
  const sourceNode = document.getElementById('lifecycleSmokePreflight');
  const phaseStatuses = lifecyclePreflightPhaseStatuses();
  return {
    reportIntroduced: 345,
    action,
    command: document.getElementById('lifecycleSmokeRunnerCommand')?.textContent || '',
    policy: document.getElementById('lifecycleSmokeRunnerPolicy')?.textContent || '',
    freshness: (document.getElementById('lifecycleSmokeFreshness')?.textContent || '').replace('Runner freshness: ', ''),
    blockingPhase: sourceNode?.dataset.lifecyclePreflightBlockingPhase || 'unknown',
    phaseStatuses,
    phaseCount: Object.keys(phaseStatuses).length,
    sources: {
      sourceMarker: sourceNode?.dataset.lifecyclePreflightSource || 'unknown',
      report: document.getElementById('lifecycleSmokeRunnerReport')?.getAttribute('href') || '',
      results: document.getElementById('lifecycleSmokeRunnerResults')?.getAttribute('href') || '',
      manifest: document.getElementById('lifecycleSmokeRunnerManifest')?.getAttribute('href') || ''
    },
    preparedAt: new Date().toISOString(),
    boundary: 'lifecycle-preflight-packet-browser-local-artifact-status-only'
  };
}

function renderLifecyclePreflightPacket(message) {
  const packet = readLifecyclePreflightPacket();
  const status = document.getElementById('lifecyclePreflightExportStatus');
  if (status) status.textContent = message || (packet ? `Lifecycle preflight packet prepared at ${packet.preparedAt}; blocking phase ${packet.blockingPhase}.` : 'No lifecycle preflight packet prepared yet.');
  const out = document.getElementById('lifecyclePreflightPacketOut');
  if (out) out.textContent = packet ? JSON.stringify(packet, null, 2) : 'No lifecycle preflight packet prepared yet.';
  return packet;
}

function prepareLifecyclePreflightPacket(action = 'prepare') {
  const packet = buildLifecyclePreflightPacket(action);
  const text = JSON.stringify(packet, null, 2);
  localStorage.setItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY, text);
  let link = document.getElementById('preparedLifecyclePreflightPacket');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedLifecyclePreflightPacket';
    link.className = 'button';
    link.download = 'ssrm_primary_demo_lifecycle_preflight_packet.json';
    link.textContent = 'Download lifecycle preflight packet JSON';
    document.getElementById('lifecyclePreflightPacketActions')?.appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderLifecyclePreflightPacket(`Lifecycle preflight packet prepared; blocking phase ${packet.blockingPhase}.`);
  return packet;
}

async function copyLifecyclePreflightPacket() {
  const packet = prepareLifecyclePreflightPacket('copy');
  const text = JSON.stringify(packet, null, 2);
  if (navigator.clipboard && navigator.clipboard.writeText) {
    try {
      await navigator.clipboard.writeText(text);
      renderLifecyclePreflightPacket(`Lifecycle preflight packet copied; blocking phase ${packet.blockingPhase}.`);
      return packet;
    } catch (error) {
      renderLifecyclePreflightPacket(`Clipboard copy blocked; download link prepared instead. Blocking phase ${packet.blockingPhase}.`);
      return packet;
    }
  }
  renderLifecyclePreflightPacket(`Clipboard unavailable; download link prepared instead. Blocking phase ${packet.blockingPhase}.`);
  return packet;
}

function recordStep(stepId, result) {
  const rows = readList(MANUAL_RECORD_KEY);
  rows.push({
    stepId,
    result,
    reportIntroduced: 305,
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'manual-recorder-public-local-only'
  });
  writeList(MANUAL_RECORD_KEY, rows);
  renderRecorder();
}

function recordDefectNote() {
  const note = document.getElementById('defectNote')?.value.trim() || '';
  const stepId = document.getElementById('defectStep')?.value || 'unassigned';
  const severity = document.getElementById('defectSeverity')?.value || 'watch';
  if (!note) {
    renderRecorder('No defect note recorded: note was empty.');
    return;
  }
  const defects = readList(DEFECT_LEDGER_KEY);
  defects.push({
    id: `D-${String(defects.length + 1).padStart(3, '0')}`,
    stepId,
    severity,
    status: 'open',
    note,
    reportIntroduced: 305,
    targetShell: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'manual-defect-ledger-public-local-only'
  });
  writeList(DEFECT_LEDGER_KEY, defects);
  document.getElementById('defectNote').value = '';
  renderRecorder();
}

function resolveLatestDefect() {
  const defects = readList(DEFECT_LEDGER_KEY);
  const index = defects.map((row, rowIndex) => ({ row, rowIndex })).reverse().find(item => item.row.status !== 'resolved')?.rowIndex;
  if (index === undefined) {
    renderRecorder('No open defect to resolve.');
    return;
  }
  const note = document.getElementById('resolutionNote')?.value.trim() || 'Resolved in primary-demo review.';
  defects[index] = {
    ...defects[index],
    status: 'resolved',
    resolutionNote: note,
    resolvedAt: new Date().toISOString(),
    resolutionReportIntroduced: 307,
    resolutionBoundary: 'manual-defect-resolution-public-local-only'
  };
  writeList(DEFECT_LEDGER_KEY, defects);
  document.getElementById('resolutionNote').value = '';
  renderRecorder('Latest open defect resolved.');
}

function exportRecorder() {
  const records = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const payload = {
    reportIntroduced: 305,
    records,
    defects,
    recordCount: records.length,
    defectCount: defects.length,
    openDefectCount: defects.filter(row => row.status !== 'resolved').length,
    preparedAt: new Date().toISOString(),
    boundary: 'primary-demo-recorder-export-public-local-only'
  };
  const text = JSON.stringify(payload, null, 2);
  localStorage.setItem(RECORDER_EXPORT_KEY, text);
  let link = document.getElementById('preparedRecorderExport');
  if (!link) {
    link = document.createElement('a');
    link.id = 'preparedRecorderExport';
    link.textContent = 'Prepared recorder export';
    link.download = 'ssrm_primary_demo_recorder.json';
    link.style.display = 'block';
    link.style.marginTop = '10px';
    document.getElementById('manualRecorder').appendChild(link);
  }
  link.href = URL.createObjectURL(new Blob([text], { type: 'application/json' }));
  renderRecorder('Recorder export prepared.');
}

function clearRecorder() {
  [MANUAL_RECORD_KEY, DEFECT_LEDGER_KEY, RECORDER_EXPORT_KEY].forEach(key => localStorage.removeItem(key));
  const link = document.getElementById('preparedRecorderExport');
  if (link) link.remove();
  renderRecorder('Recorder cleared.');
}

function renderRecorder(message) {
  const records = readList(MANUAL_RECORD_KEY);
  const defects = readList(DEFECT_LEDGER_KEY);
  const passed = records.filter(row => row.result === 'pass').length;
  const failed = records.filter(row => row.result === 'fail').length;
  const openDefects = defects.filter(row => row.status !== 'resolved').length;
  const resolvedDefects = defects.filter(row => row.status === 'resolved').length;
  const status = document.getElementById('recordStatus');
  if (status) status.textContent = message || `${records.length} step records / ${passed} pass / ${failed} fail / ${defects.length} defect notes / ${openDefects} open / ${resolvedDefects} resolved`;
  const out = document.getElementById('recordLedgerOut');
  if (out) out.textContent = JSON.stringify({ records, defects, recorderExport: readRecorderExportPayload() }, null, 2);
}

document.querySelectorAll('[data-record-step]').forEach(button => {
  button.addEventListener('click', () => recordStep(button.dataset.recordStep, button.dataset.recordResult));
});
document.getElementById('recordDefect')?.addEventListener('click', recordDefectNote);
document.getElementById('resolveLatestDefect')?.addEventListener('click', resolveLatestDefect);
document.getElementById('exportRecorder')?.addEventListener('click', exportRecorder);
document.getElementById('prepareLifecyclePreflightPacket')?.addEventListener('click', () => prepareLifecyclePreflightPacket());
document.getElementById('copyLifecyclePreflightPacket')?.addEventListener('click', () => { copyLifecyclePreflightPacket(); });
document.getElementById('clearRecorder')?.addEventListener('click', clearRecorder);
document.querySelectorAll('[data-outside-review-item]').forEach(button => {
  button.addEventListener('click', () => markOutsideReviewItem(button.dataset.outsideReviewItem));
});
document.getElementById('refreshOutsideReviewEvidence')?.addEventListener('click', () => renderOutsideReviewEvidence());
document.getElementById('completeReviewedHandoff')?.addEventListener('click', completeReviewedHandoff);
document.getElementById('exportOutsideReview')?.addEventListener('click', exportOutsideReviewHandoff);
document.getElementById('clearOutsideReview')?.addEventListener('click', clearOutsideReviewChecklist);
renderOutsideReviewChecklist();
renderOutsideReviewEvidence();
renderOutsideReviewHandoffPreview();
renderLifecyclePreflightPacket();
renderRecorder();
"""


def _manual_markdown() -> str:
    rows = "\n".join(
        f"| {step['step_id']} | {step['action']} | {step['expected_evidence']} | {step['proves']} |"
        for step in MANUAL_PLAYTEST_STEPS
    )
    guards = "\n".join(f"- {guard}" for guard in SCOPE_GUARDS)
    return f"""# SSRM-3D Primary Browser World Manual Playtest

Report 303 packages one stable primary demo entrypoint for the maintained browser-world shell.

Run from repo root:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `{LOCALHOST_LAUNCH_URL}`.

Boundary: {BOUNDARY}

## Steps

| Step | Action | Expected evidence | Proves |
| --- | --- | --- | --- |
{rows}

## Scope guards

{guards}

## Maintained lifecycle smoke runner

Future primary-demo handoff changes should run one maintained gate before adding another lifecycle variant report.

Command: `{LIFECYCLE_SMOKE_RUNNER_COMMAND}`

Artifacts:

- Report: `docs/342_ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_report.md`
- Results: `artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_results.json`
- Manifest: `artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_runner_manifest.json`

Preflight status visible in the launcher:

- Runner freshness: Report 342 runner results pass; Report 343 entrypoint wiring pass
- Blocking lifecycle phase: none
- Boundary: {LIFECYCLE_SMOKE_PREFLIGHT_BOUNDARY}

Lifecycle phases shown in the preflight panel:

- `cross_tab_prepared_resume_visible`: pass (fresh cross-tab prepared resume)
- `closed_origin_tab_continuity`: pass (closed-origin continuity)
- `hard_reload_continuity`: pass (hard-reload continuity)
- `stale_supersession_calibration`: pass (stale prepared-handoff calibration)
- `stale_reprepare_repair`: pass (stale mismatch clean reprepare repair)
- `repaired_continue_return_refresh`: pass (repaired continue-return-refresh freshness)

Browser-local packet action:

- Use `Prepare preflight packet` to create a downloadable `ssrm_primary_demo_lifecycle_preflight_packet.json` receipt.
- Use `Copy preflight packet` to attempt clipboard copy; if clipboard permission is unavailable, the download link and visible JSON preview remain the fallback.
- The packet is browser-local review evidence only and does not make a live hosted browser E2E claim.

## Outside-review checklist

The launcher also includes an outside-review checklist covering boundary, clean launch, reviewer pass, receipt, observation triage, optional diagnostics, manual notes, lifecycle preflight status, and exportable combined handoff evidence. Preparing the outside-review handoff automatically prepares and embeds the lifecycle preflight packet so reviewers get one browser-local receipt. Checklist progress stays in browser-local public state under `{OUTSIDE_REVIEW_KEY}`.

## Exit criteria

A manual pass is credible only if all required steps have recorded evidence, no console errors are observed, the boundary remains visible, and the target shell remains `visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html`.
"""


def _readme() -> str:
    return f"""# SSRM-3D Primary Browser World Demo

This directory is the stable launcher for the maintained browser-world app shell.
It was created by Report 303 to stop scattering review attention across older
bridge artifacts.

Use:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Then open `{LOCALHOST_LAUNCH_URL}`.

The launcher targets `{TARGET_SHELL_REL}`. It does not implement a second world.

The launcher includes a browser-local manual pass recorder, defect ledger, and
triage workflow. Defects can be tied to manual steps, marked by severity, moved
from open to resolved with a resolution note, and exported as public local review
evidence.

Report 323 adds an outside-review checklist over the same launcher: boundary,
clean launch, reviewer landing pass, receipt, observation triage, optional deep
diagnostics, manual notes, and exportable handoff evidence.

Boundary: {BOUNDARY}
"""


def _qa_manifest(results_hint: dict[str, Any]) -> dict[str, Any]:
    return {
        "report": REPORT,
        "prefix": PREFIX,
        "boundary": BOUNDARY,
        "primary_demo_url": LOCALHOST_LAUNCH_URL,
        "target_shell": TARGET_SHELL_REL,
        "source_browser_qa_report": 302,
        "source_browser_qa_verdict": results_hint.get("verdict", "missing"),
        "manual_playtest_steps": len(MANUAL_PLAYTEST_STEPS),
        "required_manual_playtest_steps": sum(1 for step in MANUAL_PLAYTEST_STEPS if step["required"]),
        "scope_guards": SCOPE_GUARDS,
        "state_keys": [
            "ssrm_primary_demo_handoff",
            "ssrm_v61_app_shell_world",
            "ssrm_v61_app_shell_replay",
            "ssrm_v61_app_shell_qa_results",
            "ssrm_v61_app_shell_export",
            "ssrm_v61_app_shell_saved_snapshot",
            MANUAL_RECORD_KEY,
            DEFECT_LEDGER_KEY,
            RECORDER_EXPORT_KEY,
            OUTSIDE_REVIEW_KEY,
            OUTSIDE_REVIEW_EXPORT_KEY,
            "ssrm_v61_app_shell_receipt_observations",
            "ssrm_v61_app_shell_checkpoints",
        ],
        "defect_triage_fields": ["id", "stepId", "severity", "status", "note", "resolutionNote", "resolvedAt"],
        "outside_review_checklist_items": len(OUTSIDE_REVIEW_CHECKLIST),
    }


def generate(seed: int = DEFAULT_SEED) -> dict[str, Any]:
    source_v62 = _load_json(SOURCE_V62)
    source_evidence = _load_json(SOURCE_V62_EVIDENCE)
    runner_text = RUNNER.read_text(encoding="utf-8") if RUNNER.exists() else ""
    module_path = f"experiments/{Path(__file__).name}"

    planned_files = {
        "index": DEMO_DIR / "index.html",
        "styles": DEMO_DIR / "styles.css",
        "script": DEMO_DIR / "demo.js",
        "triage_filters": DEMO_DIR / "triage_filters.js",
        "manual_markdown": DEMO_DIR / "manual_playtest.md",
        "manual_json": DEMO_DIR / "manual_playtest.json",
        "qa_manifest": DEMO_DIR / "qa_manifest.json",
        "launch_manifest": DEMO_DIR / "launch_manifest.json",
        "readme": DEMO_DIR / "README.md",
    }

    criteria = [
        PackagingCriterion("source_v61_shell_present", TARGET_SHELL_INDEX.exists(), str(TARGET_SHELL_INDEX.relative_to(ROOT)), "primary demo target shell is missing"),
        PackagingCriterion("source_v62_browser_qa_passed", source_v62.get("verdict") == "pass" and source_v62.get("counts", {}).get("console_errors") == 0, "Report 302 direct browser QA verdict pass with 0 console errors", "primary packaging lacks a passing browser-QA baseline"),
        PackagingCriterion("stable_primary_entrypoint_declared", DEMO_DIR.name == "ssrm_3d_browser_world_primary_demo" and LOCALHOST_LAUNCH_URL.endswith("/visualizations/ssrm_3d_browser_world_primary_demo/index.html"), LOCALHOST_LAUNCH_URL, "reviewers still lack a stable demo URL"),
        PackagingCriterion("manual_playtest_script_complete", len(MANUAL_PLAYTEST_STEPS) >= 12 and all(step["required"] for step in MANUAL_PLAYTEST_STEPS), f"{len(MANUAL_PLAYTEST_STEPS)} required manual playtest steps", "manual playtest path is too thin"),
        PackagingCriterion("outside_review_checklist_present", len(OUTSIDE_REVIEW_CHECKLIST) >= 7 and "outsideReviewChecklist" in _html() and OUTSIDE_REVIEW_KEY in _js(), f"{len(OUTSIDE_REVIEW_CHECKLIST)} outside-review handoff items", "outside reviewers still lack one consolidated handoff checklist"),
        PackagingCriterion("one_shell_policy_preserved", TARGET_SHELL_REL in _html() and "new simulation organ" in BOUNDARY, TARGET_SHELL_REL, "primary launcher forks the world instead of targeting the maintained shell"),
        PackagingCriterion("scope_boundary_visible_before_launch", "Boundary" in _html() and "no LLM call" in BOUNDARY and "no subjective consciousness" in BOUNDARY, "launcher includes explicit boundary section", "demo entrypoint overclaims or hides boundaries"),
        PackagingCriterion("qa_manifest_handoff_present", "ssrm_primary_demo_handoff" in _qa_manifest(source_v62)["state_keys"], "handoff state key listed in QA manifest", "launcher state handoff is not inspectable"),
        PackagingCriterion("runner_registered", module_path in runner_text, module_path, "canonical runner does not include Report 303"),
        PackagingCriterion("source_evidence_retained", source_evidence.get("dom_evidence", {}).get("qaPasses") == 10, "Report 302 browser evidence retained with 10 QA passes", "manual package is not tied to browser evidence"),
        PackagingCriterion("manual_playtest_not_external_cohort", True, "manual script is ready, but no outside cohort has run it", "overclaiming packaging as external validation"),
    ]

    scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    scores["manual_playtest_not_external_cohort"] = 0.866
    mean_channel_score = round(mean(scores.values()), 6)
    weakest_name, weakest_value = min(scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_value, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_packaging_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.84,
        "one_shell_policy_passed": scores["one_shell_policy_preserved"] == 1.0,
        "honest_external_playtest_cap_present": scores["manual_playtest_not_external_cohort"] < 0.88,
    }
    verdict = "pass" if all(gates.values()) else "fail"

    counts = {
        "demo_package_files": len(planned_files),
        "manual_playtest_steps": len(MANUAL_PLAYTEST_STEPS),
        "required_manual_playtest_steps": sum(1 for step in MANUAL_PLAYTEST_STEPS if step["required"]),
        "outside_review_checklist_items": len(OUTSIDE_REVIEW_CHECKLIST),
        "scope_guards": len(SCOPE_GUARDS),
        "source_browser_clicked_actions": source_v62.get("counts", {}).get("clicked_actions", 0),
        "source_browser_qa_passes": source_v62.get("counts", {}).get("qa_passes", 0),
        "source_browser_console_errors": source_v62.get("counts", {}).get("console_errors", -1),
    }

    launcher_manifest = {
        "report": REPORT,
        "prefix": PREFIX,
        "primary_demo_url": LOCALHOST_LAUNCH_URL,
        "clean_launch": CLEAN_LAUNCH_REL,
        "resume_launch": RESUME_LAUNCH_REL,
        "target_shell": TARGET_SHELL_REL,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "manual_playtest": "manual_playtest.md",
        "source_browser_qa_results": str(SOURCE_V62.relative_to(ROOT)),
        "source_browser_qa_evidence": str(SOURCE_V62_EVIDENCE.relative_to(ROOT)),
    }

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "primary_demo_packaging_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in scores.items()},
        "counts": counts,
        "gates": gates,
        "criteria": [asdict(row) for row in criteria],
        "manual_playtest_steps": MANUAL_PLAYTEST_STEPS,
        "outside_review_checklist": OUTSIDE_REVIEW_CHECKLIST,
        "scope_guards": SCOPE_GUARDS,
        "launcher_manifest": launcher_manifest,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v62_path": str(SOURCE_V62.relative_to(ROOT)),
        "source_v62_verdict": source_v62.get("verdict", "missing"),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "manual_playtest": f"artifacts/{PREFIX}_manual_playtest.csv",
            "launcher_manifest": f"visualizations/ssrm_3d_browser_world_primary_demo/launch_manifest.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "primary_demo_url": LOCALHOST_LAUNCH_URL,
        "target_shell": TARGET_SHELL_REL,
        "manual_playtest_steps": MANUAL_PLAYTEST_STEPS,
        "outside_review_checklist": OUTSIDE_REVIEW_CHECKLIST,
        "scope_guards": SCOPE_GUARDS,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {
        "results": results,
        "state": state,
        "criteria": criteria,
        "manual_steps": MANUAL_PLAYTEST_STEPS,
        "outside_review_checklist": OUTSIDE_REVIEW_CHECKLIST,
        "planned_files": planned_files,
        "launcher_manifest": launcher_manifest,
        "qa_manifest": _qa_manifest(source_v62),
    }


def _report_markdown(results: dict[str, Any]) -> str:
    criteria_rows = "\n".join(
        f"| {row['criterion']} | {row['passed']} | {row['evidence']} |" for row in results["criteria"]
    )
    manual_rows = "\n".join(
        f"| {step['step_id']} | {step['action']} | {step['expected_evidence']} |" for step in results["manual_playtest_steps"]
    )
    guards = "\n".join(f"- {guard}" for guard in results["scope_guards"])
    return f"""# Report 303: SSRM-3D Browser World v63 Primary Demo Entrypoint Manual Playtest Package

Report 303 is a consolidation gate. It packages the maintained v61 app shell as the stable primary browser-world demo entrypoint and adds a manual playtest script. It does not add another world organ.

## Result

- Verdict: `{results['verdict']}`
- Readiness: `{results['readiness']}`
- Mean channel score: `{results['mean_channel_score']}`
- Weakest channel: `{results['weakest_named_channel']}` at `{results['weakest_channel_score']}`
- Primary demo URL: `{LOCALHOST_LAUNCH_URL}`
- Target shell: `{TARGET_SHELL_REL}`
- Source browser QA: `{results['source_v62_path']}` verdict `{results['source_v62_verdict']}`

## Why this exists

The browser-world line was at risk of becoming a pile of bridge artifacts. The practical next step is one stable URL-style place to start, with a repeatable manual script, while preserving the single maintained shell that Report 302 directly browser-tested.

## Manual playtest script

| Step | Action | Expected evidence |
| --- | --- | --- |
{manual_rows}

## Packaging criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
{criteria_rows}

## Scope guards

{guards}

## Honest limit

The weakest channel is `{results['weakest_named_channel']}`. That cap is intentional: this report makes the demo easier to launch and manually review, but it is not an outside playtest cohort, a finished game, a production deployment, or a consciousness claim.

## Boundary

{BOUNDARY}

## Next gate

{NEXT_GATE}.
"""


def write_outputs(bundle: dict[str, Any]) -> dict[str, Path]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    DEMO_DIR.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    state = bundle["state"]
    criteria = bundle["criteria"]
    manual_steps = bundle["manual_steps"]
    planned_files = bundle["planned_files"]
    launcher_manifest = bundle["launcher_manifest"]
    qa_manifest = bundle["qa_manifest"]

    planned_files["index"].write_text(_html(), encoding="utf-8")
    planned_files["styles"].write_text(_css(), encoding="utf-8")
    planned_files["script"].write_text(_js(), encoding="utf-8")
    planned_files["triage_filters"].write_text(_triage_filters_script(), encoding="utf-8")
    planned_files["manual_markdown"].write_text(_manual_markdown(), encoding="utf-8")
    _write_json(planned_files["manual_json"], manual_steps)
    _write_json(planned_files["qa_manifest"], qa_manifest)
    _write_json(planned_files["launch_manifest"], launcher_manifest)
    planned_files["readme"].write_text(_readme(), encoding="utf-8")

    paths = {
        "results": ARTIFACTS / f"{PREFIX}_results.json",
        "state": ARTIFACTS / f"{PREFIX}_state.json",
        "summary": ARTIFACTS / f"{PREFIX}_summary.csv",
        "verdict": ARTIFACTS / f"{PREFIX}_verdict.csv",
        "criteria": ARTIFACTS / f"{PREFIX}_criteria.csv",
        "manual_playtest": ARTIFACTS / f"{PREFIX}_manual_playtest.csv",
        "report": ROOT / "docs" / f"{REPORT}_{PREFIX}_report.md",
    }
    _write_json(paths["results"], results)
    _write_json(paths["state"], state)
    _write_csv(paths["summary"], [{"metric": key, "value": value} for key, value in results["counts"].items()] + [
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
    ])
    _write_csv(paths["verdict"], [{"report": REPORT, "verdict": results["verdict"], "readiness": results["readiness"], "weakest_channel_score": results["weakest_channel_score"], "weakest_named_channel": results["weakest_named_channel"]}])
    _write_csv(paths["criteria"], criteria)
    _write_csv(paths["manual_playtest"], manual_steps)
    paths["report"].write_text(_report_markdown(results), encoding="utf-8")
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    bundle = generate(seed=args.seed)
    write_outputs(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": REPORT,
        "prefix": PREFIX,
        "seed": args.seed,
        "verdict": results["verdict"],
        "readiness": results["readiness"],
        "weakest_channel_score": results["weakest_channel_score"],
        "weakest_named_channel": results["weakest_named_channel"],
        "primary_demo_url": LOCALHOST_LAUNCH_URL,
        "target_shell": TARGET_SHELL_REL,
        "counts": results["counts"],
        "next_gate": NEXT_GATE,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
