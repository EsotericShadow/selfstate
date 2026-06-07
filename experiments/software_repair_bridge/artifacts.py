"""Artifact writers for the software repair bridge benchmark."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

from .models import EvalRow, RepairTask, SummaryRow, VerdictRow


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = "software_repair_bridge"


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    if not data:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def task_payload(tasks: Sequence[RepairTask]) -> list[dict[str, object]]:
    return [
        {
            **asdict(task),
            "candidate_repairs": [asdict(candidate) for candidate in task.candidate_repairs],
        }
        for task in tasks
    ]


def write_artifacts(
    tasks: Sequence[RepairTask],
    eval_rows: Sequence[EvalRow],
    summary_rows: Sequence[SummaryRow],
    verdict: VerdictRow,
) -> dict[str, object]:
    payload = {
        "report": 139,
        "name": "Programmable Repair Bridge / WrongFix Arena Spec",
        "task_count": len(tasks),
        "tasks": task_payload(tasks),
        "summary": [asdict(row) for row in summary_rows],
        "verdict": asdict(verdict),
        "notes": {
            "claim": "structured software-shaped proof surface for weakest-channel repair judgment",
            "not_claimed": "real repo coding, frontier LLM improvement, or autonomous software engineering",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", eval_rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary_rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    return payload
