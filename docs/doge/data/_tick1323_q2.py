import csv,sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p=Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
with p.open(encoding="utf-8", newline="") as f:
    r=csv.DictReader(f); fields=r.fieldnames; ids=set(row[fields[0]] for row in r)
row={k:"" for k in fields}
row["gap_id"]="gap_agbblb_liquidated_jr2019only_l5"
row["hierarchy_path"]="Vlaanderen>Gemeenten>Blankenberge>AGB>liquidatie_L5"
row["entity_id"]="agb_blankenberge"
row["what_is_missing"]="Final BBC after 2019 plus liquidation slotbalans plus successor transfer plus confirmation no AGB JR2025 exists"
row["why_it_matters"]="Leftover unmined AGB of mined city. KBO 0877.301.751 stopgezet 21.03.2023. No primary JR2025 PDF."
row["priority"]="8"
row["recipient_body"]="Stad Blankenberge / ex-AGB Blankenberge"
row["draft_letter_path"]="docs/doge/foi/drafts/gap_agbblb_liquidated_jr2019only_l5.md"
row["status"]="ready"
row["date_ready"]="2026-08-17"
row["linked_commitment_id"]="comm_agbblb_liquidated_jr_unpublished"
row["linked_leaderboard_id"]="lb_agbblb_liquidated_jr2019only"
row["created_utc"]="2026-08-17T18:25:00Z"
row["updated_utc"]="2026-08-17T18:25:00Z"
row["notes"]="tick1323; ready not sent; no sourced euros; not every-10"
if row["gap_id"] not in ids:
    with p.open("a", encoding="utf-8", newline="") as f:
        csv.DictWriter(f, fieldnames=fields, extrasaction="ignore").writerow(row)
    print("added")
else:
    print("exists")
