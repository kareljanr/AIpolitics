"""Recompute cost_score (from EUR) and priority_index; rewrite leaderboard sorted."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LB = ROOT / "leaderboard.csv"
SNAP = ROOT / "leaderboard_top15.md"


def cost_score_from_eur(x) -> float | None:
    if x is None or x == "":
        return None
    try:
        v = float(x)
    except ValueError:
        return None
    if v < 1_000_000:
        return 1.5
    if v < 10_000_000:
        return 3.5
    if v < 100_000_000:
        return 5.5
    if v < 1_000_000_000:
        return 7.5
    return 9.5


def priority(cost_s, abs_s, diff) -> float:
    return round(0.55 * float(cost_s) + 0.35 * float(abs_s) + 0.10 * (10 - float(diff)), 2)


rows = list(csv.DictReader(LB.open(encoding="utf-8-sig")))
for r in rows:
    auto = cost_score_from_eur(r.get("annual_cost_eur") or r.get("total_cost_eur"))
    # keep manual cost_score if auto missing; else refresh from €
    if auto is not None:
        r["cost_score"] = str(auto)
    r["priority_index"] = str(
        priority(r["cost_score"], r["absurdity_score"], r["difficulty"])
    )

rows.sort(key=lambda r: -float(r["priority_index"]))

fieldnames = list(rows[0].keys())
with LB.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

# markdown snapshot top 15
lines = [
    "# DOGE leaderboard top 15 (recomputed)",
    "",
    "Formula: `priority = 0.55*cost_score + 0.35*absurdity + 0.10*(10-difficulty)`",
    "cost_score refreshed from annual_cost_eur where present.",
    "",
    "| Rank | ID | Name | Annual € | Abs | Cost | Diff | Priority |",
    "|------|-----|------|----------|-----|------|------|----------|",
]
for i, r in enumerate(rows[:15], 1):
    eur = r.get("annual_cost_eur") or "—"
    lines.append(
        f"| {i} | `{r['item_id']}` | {r['name'][:50]} | {eur} | {r['absurdity_score']} | {r['cost_score']} | {r['difficulty']} | **{r['priority_index']}** |"
    )
lines.append("")
lines.append(f"_All {len(rows)} rows sorted in `leaderboard.csv`._")
SNAP.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("rewrote", LB)
for i, r in enumerate(rows[:10], 1):
    print(i, r["priority_index"], r["item_id"], r["name"][:40])
