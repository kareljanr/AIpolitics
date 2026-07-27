#!/usr/bin/env python3
"""Full auto pipeline: RSS harvest → optional export.

Scoring of proposals is done by the Proposal Radar agent (truth-seeking memos);
this script handles machine ingest + public board regeneration.

  python docs/proposal-radar/scripts/run_pipeline.py
  python docs/proposal-radar/scripts/run_pipeline.py --export-only
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(script: str, extra: list[str] | None = None) -> int:
    cmd = [sys.executable, str(HERE / script)] + (extra or [])
    print(">", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--export-only", action="store_true")
    ap.add_argument("--min-priority", type=int, default=4)
    args = ap.parse_args()

    if not args.export_only:
        rc = run("rss_harvest.py", ["--min-priority", str(args.min_priority)])
        if rc != 0:
            return rc
    return run("export_leaderboard.py")


if __name__ == "__main__":
    raise SystemExit(main())
