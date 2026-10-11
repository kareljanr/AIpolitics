#!/usr/bin/env python3
"""Print the one DOGE queue row the next tick should do. Do not load the CSV into the model."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(min(sys.maxsize, 50_000_000))


def _rows(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        yield from csv.DictReader(handle)


def main() -> int:
    state_path = DATA / "loop_state.csv"
    queue_path = DATA / "research_queue.csv"
    state = next(_rows(state_path))
    print("paused=" + (state.get("paused") or ""))
    print("ticks_completed=" + (state.get("ticks_completed") or ""))
    print("last_unit_id=" + (state.get("last_unit_id") or ""))
    print("notes=" + (state.get("notes") or "")[:500])
    if (state.get("paused") or "").strip().lower() == "yes":
        return 0

    wanted = ""
    notes = state.get("notes") or ""
    marker = "next rq_"
    if marker in notes:
        wanted = "rq_" + notes.split(marker, 1)[1].split()[0].strip(".,;")

    picked = None
    fallback = None
    for row in _rows(queue_path):
        status = (row.get("status") or "").strip().lower()
        task_id = (row.get("task_id") or "").strip()
        if status == "in_progress":
            picked = row
            break
        if wanted and task_id == wanted:
            picked = row
            break
        if fallback is None and status == "open":
            fallback = row
    picked = picked or fallback
    if not picked:
        print("NO_OPEN_UNIT")
        return 0

    print("---")
    for key in (
        "task_id",
        "title",
        "status",
        "priority",
        "sprint",
        "hierarchy_target",
        "entity_id",
        "instructions",
        "notes",
    ):
        value = (picked.get(key) or "").replace("\n", " ")
        print(f"{key}: {value[:700]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
