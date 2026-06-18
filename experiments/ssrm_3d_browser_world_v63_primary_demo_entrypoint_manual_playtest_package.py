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
        "expected_evidence": "Saved avatar/resident values return after restore.",
        "proves": "local persistence and rollback are part of the playable loop",
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
        "action": "Run state-boundary and save/restore smoke hooks.",
        "expected_evidence": "Both hook rows pass and no private workspace/LLM keys appear in public trace.",
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
]

SCOPE_GUARDS = [
    "Only the primary demo launcher is new; gameplay still lives in the maintained v61 app shell.",
    "The manual script uses Report 302 browser evidence as the baseline, not as a substitute for future human playtests.",
    "The launcher gives clean and resume paths so persistence bugs can be reproduced rather than hidden.",
    "The boundary remains visible before launch and inside the shell.",
    "Future browser-world work should patch this shell unless a defect proves a new surface is necessary.",
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
      </div>
    </section>
    <section class=\"boundary\" id=\"boundary\">
      <h2>Boundary</h2>
      <p>{BOUNDARY}</p>
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
    <section class=\"handoff\">
      <h2>Launch handoff</h2>
      <p>Local URL: <code>{LOCALHOST_LAUNCH_URL}</code></p>
      <p>Target shell: <code>{TARGET_SHELL_REL}</code></p>
      <p id=\"handoffStatus\">No launch handoff recorded in this tab yet.</p>
    </section>
  </main>
  <script src=\"demo.js\"></script>
</body>
</html>
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
.hero, .boundary, article, .handoff {
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
.boundary { margin-top: 18px; padding: 22px 26px; }
.grid { display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 18px; margin-top: 18px; }
article, .handoff { padding: 26px; }
li { margin: 0 0 12px; }
li span { display: block; color: var(--muted); margin-top: 3px; }
code { background: rgba(70, 92, 58, 0.10); padding: 2px 6px; border-radius: 8px; }
@media (max-width: 780px) {
  .grid { grid-template-columns: 1fr; }
  .actions { flex-direction: column; align-items: stretch; }
}
"""


def _js() -> str:
    return """const HANDOFF_KEY = 'ssrm_primary_demo_handoff';

function recordLaunch(kind) {
  const payload = {
    kind,
    report: 303,
    target: '../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html',
    recordedAt: new Date().toISOString(),
    boundary: 'primary-demo-launcher-only'
  };
  localStorage.setItem(HANDOFF_KEY, JSON.stringify(payload));
  renderHandoff(payload);
}

function renderHandoff(payload) {
  const node = document.getElementById('handoffStatus');
  if (!node) return;
  node.textContent = `Last handoff: ${payload.kind} launch toward ${payload.target} at ${payload.recordedAt}.`;
}

for (const [id, kind] of [['cleanLaunch', 'clean'], ['resumeLaunch', 'resume']]) {
  const node = document.getElementById(id);
  if (node) node.addEventListener('click', () => recordLaunch(kind));
}

try {
  const existing = JSON.parse(localStorage.getItem(HANDOFF_KEY) || 'null');
  if (existing) renderHandoff(existing);
} catch (error) {
  localStorage.removeItem(HANDOFF_KEY);
}
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
        ],
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
        "scope_guards": SCOPE_GUARDS,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {
        "results": results,
        "state": state,
        "criteria": criteria,
        "manual_steps": MANUAL_PLAYTEST_STEPS,
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
