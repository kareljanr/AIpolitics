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
        "| Rank | Clown | Genius | Index | Belasting-FTE | Nettoloon-jaren | Title | Actor | Memo |",
        "|------|------:|-------:|------:|--------------:|----------------:|-------|-------|------|",
    ]
    if not ranked:
        lines.append("| — | — | — | — | — | — | *no rows yet* | | |")
    else:
        for i, r in enumerate(ranked[:15], 1):
            lines.append(
                f"| {i} | {r.get('clownpoints','')} | {r.get('genius_score','')} | "
                f"{r.get('policy_index','')} | {r.get('pain_tax_fte','')} | {r.get('pain_net_years','')} | "
                f"{r.get('title','')} | {r.get('actor_name','')} | {memo_link(r)} |"
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
        "| Rank | Genius | Clown | Index | Belasting-FTE | Nettoloon-jaren | Title | Actor | Memo |",
        "|------|-------:|------:|------:|--------------:|----------------:|-------|-------|------|",
    ]
    if not ranked:
        lines.append("| — | — | — | — | — | — | *no rows yet* | | |")
    else:
        for i, r in enumerate(ranked[:15], 1):
            lines.append(
                f"| {i} | {r.get('genius_score','')} | {r.get('clownpoints','')} | "
                f"{r.get('policy_index','')} | {r.get('pain_tax_fte','')} | {r.get('pain_net_years','')} | "
                f"{r.get('title','')} | {r.get('actor_name','')} | {memo_link(r)} |"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_weekly(rows: list[dict], path: Path) -> None:
    by_clown = sorted(rows, key=lambda r: -fnum(r.get("clownpoints")))[:5]
    by_genius = sorted(rows, key=lambda r: -fnum(r.get("genius_score")))[:3]
    mixed = [
        r
        for r in rows
        if -2 <= fnum(r.get("policy_index")) <= 2 and fnum(r.get("genius_score")) >= 3
    ][:3]

    def bullet(r: dict) -> str:
        pain = ""
        if r.get("pain_tax_fte"):
            pain = f" · **{r.get('pain_tax_fte')} Belasting-FTE** / {r.get('pain_net_years')} nettoloon-jaren"
        return (
            f"- **{r.get('title')}** — clown {r.get('clownpoints')} / genius {r.get('genius_score')} "
            f"(index {r.get('policy_index')}){pain} — {r.get('actor_name')} · {r.get('jurisdiction')} · "
            f"{memo_link(r)}"
        )

    lines = [
        "# Clowns & Genius — weekly pack",
        "",
        f"Auto-generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}.",
        f"Scored proposals in pack universe: **{len(rows)}**.",
        "",
        "## This week’s clowns",
        "",
    ]
    lines += [bullet(r) for r in by_clown] or ["*(none)*"]
    lines += ["", "## This week’s solid / genius", ""]
    lines += [bullet(r) for r in by_genius] or ["*(none)*"]
    lines += ["", "## Mixed but fixable", ""]
    lines += [bullet(r) for r in mixed] or ["*(none in mixed band)*"]
    lines += [
        "",
        "## Draft X thread (human or auto-draft)",
        "",
        "1. Hook: same exam for every Belgian proposal",
        "2. Top clown card (instrument + mechanism + score)",
        "3. Top solid/genius card",
        "4. Method: falsifier + confidence tags",
        "5. Bridge to DOGE if money already exists",
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
