#!/usr/bin/env python3
"""Print the one Proposal Radar item the next cloud tick should score."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "proposal-radar" / "data"
csv.field_size_limit(min(sys.maxsize, 50_000_000))


def _rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _priority(row: dict) -> int:
    try:
        return int(float(row.get("priority") or 0))
    except ValueError:
        return 0


def main() -> int:
    state_rows = _rows(DATA / "loop_state.csv")
    state = state_rows[0] if state_rows else {}
    paused = (state.get("paused") or "").strip().lower()
    print("paused=" + (state.get("paused") or ""))
    print("ticks_completed=" + (state.get("ticks_completed") or "0"))
    print("proposals_scored=" + (state.get("proposals_scored") or "0"))
    print("last_unit_id=" + (state.get("last_unit_id") or ""))
    if paused == "yes":
        print("PAUSED")
        return 0

    header_path = DATA / "proposals.csv"
    if header_path.exists():
        header = header_path.read_text(encoding="utf-8").splitlines()[0]
        print("PROPOSALS_HEADER=" + header)

    queue = _rows(DATA / "ingest_queue.csv")
    active = [
        row
        for row in queue
        if (row.get("status") or "").strip().lower() in {"open", "in_progress"}
        and row.get("ingest_id")
    ]
    active.sort(
        key=lambda row: (
            0 if (row.get("status") or "").strip().lower() == "in_progress" else 1,
            -_priority(row),
            row.get("created_utc") or "",
        )
    )
    if not active:
        print("NO_UNIT")
        return 0

    row = active[0]
    print("---")
    for key in (
        "ingest_id",
        "status",
        "priority",
        "title_hint",
        "url",
        "discovered_via",
        "jurisdiction_guess",
        "created_utc",
        "notes",
    ):
        value = (row.get(key) or "").replace("\n", " ")
        print(f"{key}: {value[:500]}")
    print(f"queue_remaining={len(active)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
