# -*- coding: utf-8 -*-
import csv
from pathlib import Path

DATA = Path("docs/doge/data")
csv.field_size_limit(10**7)

# Drop our duplicate IDs; keep concurrent de_lovie_* naming
DROP_PREFIXES = {
    "sources.csv": "source_id",
    "budgets.csv": "budget_id",
    "leaderboard.csv": "item_id",
    "commitments.csv": "commitment_id",
}
DROP_IDS = {
    "src_lovie_jr2025_cw",
    "src_lovie_jr2025_cw_en",
    "src_lovie_jr2025_cw_fr",
    "src_lovie_kbo_2089",
    "src_lovie_site_2089",
    "bud_lovie_omzet_jr2025_statutory",
    "bud_lovie_bruto_jr2025_statutory",
    "bud_lovie_pnl_jr2025_statutory",
    "bud_lovie_equity_jr2025_statutory",
    "bud_lovie_fte_jr2025_statutory",
    "lb_lovie_bruto_jump_67_01m_omzet_8_51m_pnl_drop_jr2025",
    "comm_lovie_jr2025_statutory_disability_care",
}

for fname, key in DROP_PREFIXES.items():
    path = DATA / fname
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    before = len(rows)
    rows = [row for row in rows if row.get(key) not in DROP_IDS]
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(fname, before, "->", len(rows))

# entities: only one vzw_de_lovie_poperinge expected
path = DATA / "entities.csv"
with path.open(encoding="utf-8-sig", newline="") as fh:
    r = csv.DictReader(fh)
    fields = r.fieldnames
    rows = list(r)
seen = set()
out = []
for row in rows:
    eid = row.get("entity_id")
    if eid == "vzw_de_lovie_poperinge":
        if eid in seen:
            continue
        seen.add(eid)
    out.append(row)
with path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(out)
print("entities lovie kept", sum(1 for r in out if r.get("entity_id") == "vzw_de_lovie_poperinge"))
