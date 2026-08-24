# -*- coding: utf-8 -*-
"""Remove concurrent-tick race duplicates for Entraide Jolimont / rq_2119."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[2]  # docs/doge/data
csv.field_size_limit(10**7)

DROP_PREFIXES = {
    "sources": {
        "src_efj_jr2025_cw",
        "src_efj_jr2025_cw_en",
        "src_efj_jr2025_cw_fr",
        "src_efj_kbo_2118",
        "src_efj_site_2118",
    },
    "budgets": {
        "bud_efj_omzet_jr2025_statutory",
        "bud_efj_bruto_jr2025_statutory",
        "bud_efj_pnl_jr2025_statutory",
        "bud_efj_equity_jr2025_statutory",
        "bud_efj_fte_jr2025_statutory",
    },
    "commitments": {"comm_efj_jr2025_statutory_mrs"},
    "leaderboard": {"lb_efj_omzet_jump_28_73m_pnl_drop_jr2025"},
    "foi_queue": {"gap_efj_nbb_pdf_assets_debt_pnl_drop_matrix_l5"},
}


def rewrite(path: Path, key: str, drop_ids: set[str] | None = None, dedupe_key: str | None = None):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    before = len(rows)
    if drop_ids:
        rows = [r for r in rows if r.get(key) not in drop_ids]
    if dedupe_key:
        seen = set()
        out = []
        for r in rows:
            vid = r.get(dedupe_key)
            if vid in seen:
                continue
            if vid:
                seen.add(vid)
            out.append(r)
        rows = out
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(path.name, before, "->", len(rows))


for name, drops in DROP_PREFIXES.items():
    rewrite(DATA / f"{name}.csv", list(csv.DictReader(open(DATA / f"{name}.csv", encoding="utf-8-sig", newline="")).fieldnames)[0], drops)

rewrite(DATA / "entities.csv", "entity_id", dedupe_key="entity_id")
rewrite(DATA / "research_queue.csv", "task_id", dedupe_key="task_id")

# drop race FOI draft if present
foi = DATA.parent / "foi" / "drafts" / "gap_efj_nbb_pdf_assets_debt_pnl_drop_matrix_l5.md"
if foi.exists():
    foi.unlink()
    print("removed", foi.name)
