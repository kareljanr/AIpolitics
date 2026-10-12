#!/usr/bin/env python3
"""Regenerate public leaderboard markdown from proposals.csv."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RADAR = ROOT / "docs" / "proposal-radar"
DATA = RADAR / "data" / "proposals.csv"
PUBLIC = RADAR / "public"


def load_proposals() -> list[dict]:
    if not DATA.exists():
        return []
    with DATA.open(encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("proposal_id")]
    return rows


def fnum(x: str) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return float("-inf")


def publishable(r: dict) -> bool:
    conf = (r.get("score_confidence") or "").lower()
    if conf not in ("medium", "strong"):
        return False
    # allow needs_human during calibration review if scores present
    if not r.get("clownpoints") and r.get("clownpoints") != "0":
        return False
    return True


def memo_link(r: dict) -> str:
    p = r.get("analysis_path") or ""
    if not p:
        return "—"
    return f"[memo](../{p})"


def write_clowns(rows: list[dict], path: Path) -> None:
    ranked = sorted(rows, key=lambda r: (-fnum(r.get("clownpoints")), fnum(r.get("policy_index"))))
    lines = [
        "# Clowns leaderboard (Proposal Radar)",
        "",
        "Highest **clownpoints** among scored proposals (medium/strong confidence).",
        "Rubric: [docs/09-proposal-radar.md](../../09-proposal-radar.md)",
        "",
        f"Last refresh: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "| Rank | Clown | Genius | Index | Belasting-FTE | Nettoloon-jaren | Werkminuten | Title | Memo |",
        "|------|------:|-------:|------:|--------------:|----------------:|------------:|-------|------|",
    ]
    if not ranked:
        lines.append("| — | — | — | — | — | — | — | *no rows yet* | |")
    else:
        for i, r in enumerate(ranked[:15], 1):
            lines.append(
                f"| {i} | {r.get('clownpoints','')} | {r.get('genius_score','')} | "
                f"{r.get('policy_index','')} | {r.get('pain_tax_fte','')} | {r.get('pain_net_years','')} | "
                f"{r.get('pain_work_minutes','')} | {r.get('title','')} | {memo_link(r)} |"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_genius(rows: list[dict], path: Path) -> None:
    ranked = sorted(
        rows,
        key=lambda r: (-fnum(r.get("genius_score")), -fnum(r.get("policy_index")), fnum(r.get("clownpoints"))),
    )
    lines = [
        "# Genius leaderboard (Proposal Radar)",
        "",
        "Highest **genius_score** among scored proposals (medium/strong confidence).",
        "Genius is rare — solid reforms often land mid-high, not 9–10.",
        "Rubric: [docs/09-proposal-radar.md](../../09-proposal-radar.md)",
        "",
        f"Last refresh: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "| Rank | Genius | Clown | Index | Belasting-FTE | Nettoloon-jaren | Werkminuten | Title | Memo |",
        "|------|-------:|------:|------:|--------------:|----------------:|------------:|-------|------|",
    ]
    if not ranked:
        lines.append("| — | — | — | — | — | — | — | *no rows yet* | |")
    else:
        for i, r in enumerate(ranked[:15], 1):
            lines.append(
                f"| {i} | {r.get('genius_score','')} | {r.get('clownpoints','')} | "
                f"{r.get('policy_index','')} | {r.get('pain_tax_fte','')} | {r.get('pain_net_years','')} | "
                f"{r.get('pain_work_minutes','')} | {r.get('title','')} | {memo_link(r)} |"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _recent(rows: list[dict], days: int = 21) -> list[dict]:
    cutoff = datetime.now(timezone.utc).timestamp() - days * 86400
    picked: list[dict] = []
    for row in rows:
        stamp = (row.get("updated_utc") or row.get("created_utc") or "").strip()
        if not stamp:
            continue
        try:
            seen = datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp()
        except ValueError:
            continue
        if seen >= cutoff:
            picked.append(row)
    picked.sort(key=lambda row: row.get("updated_utc") or "", reverse=True)
    return picked


def write_weekly(rows: list[dict], path: Path) -> None:
    recent = _recent(rows)
    ingest_path = RADAR / "data" / "ingest_queue.csv"
    waiting: list[dict] = []
    if ingest_path.exists():
        with ingest_path.open(encoding="utf-8", newline="") as handle:
            waiting = [
                row
                for row in csv.DictReader(handle)
                if (row.get("status") or "").strip().lower() == "open"
            ]
    waiting.sort(key=lambda row: row.get("created_utc") or "", reverse=True)

    def bullet(r: dict) -> str:
        return (
            f"- **{r.get('title')}** — clown {r.get('clownpoints')} / genius {r.get('genius_score')} "
            f"(index {r.get('policy_index')}, {r.get('score_confidence') or 'unscored'}) — "
            f"{r.get('actor_name')} · {r.get('status')} · {r.get('jurisdiction')} · {memo_link(r)}"
        )

    lines = [
        "# Proposal Radar — what is new",
        "",
        "New and recently re-scored proposals. The all-time lists stay in "
        "[leaderboard_clowns.md](leaderboard_clowns.md) and "
        "[leaderboard_genius.md](leaderboard_genius.md).",
        "",
        f"Scored in the last 21 days: **{len(recent)}**. "
        f"Still open in the queue: **{len(waiting)}**.",
        "",
        "## New ratings",
        "",
    ]
    lines += [bullet(r) for r in recent] or ["No proposal was scored or re-scored in the last 21 days."]
    lines += ["", "## In the queue, not scored yet", ""]
    if waiting:
        for row in waiting[:15]:
            lines.append(f"- {row.get('title_hint')} ({row.get('created_utc','')[:10]})")
    else:
        lines.append("Queue is empty.")
    lines += [
        "",
        "## Method",
        "",
        "[docs/09-proposal-radar.md](../../09-proposal-radar.md)",
        "",
    ]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    rows = [r for r in load_proposals() if publishable(r)]
    PUBLIC.mkdir(parents=True, exist_ok=True)
    write_clowns(rows, PUBLIC / "leaderboard_clowns.md")
    write_genius(rows, PUBLIC / "leaderboard_genius.md")
    write_weekly(rows, PUBLIC / "weekly_latest.md")
    print(f"Exported leaderboards for {len(rows)} publishable proposals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
