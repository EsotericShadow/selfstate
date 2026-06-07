"""Run the Report 139 programmable repair bridge benchmark."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .artifacts import write_artifacts
from .evaluator import evaluate
from .task_bank import TASKS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-tasks", type=int, default=10, help="Minimum task count expected in the bank.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if len(TASKS) < args.min_tasks:
        raise ValueError(f"expected at least {args.min_tasks} tasks, found {len(TASKS)}")

    eval_rows, summary_rows, verdict = evaluate(TASKS)
    write_artifacts(TASKS, eval_rows, summary_rows, verdict)
    print(json.dumps(asdict(verdict), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
