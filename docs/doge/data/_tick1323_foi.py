
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
# drop last row if first field empty
raw = p.read_bytes()
if raw.endswith(b"\n"):
    parts = raw.rsplit(b"\n", 2)
    body, last = parts[0], parts[1]
else:
    body, last = raw.rsplit(b"\n", 1)
if last.startswith(b","):
    p.write_bytes(body + b"\n")
    print("dropped empty")
else:
    print("kept last")

# copy contact from existing city_blankenberge row if any
email = ""
postal = ""
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row.get("entity_id") == "city_blankenberge" and row.get("recipient_email"):
            email = row["recipient_email"]
            postal = row.get("recipient_postal","")
            break
if not email:
    # fallback from entities
    ep = Path("/workspace/AIpolitics/docs/doge/data/entities.csv")
    with ep.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            if row.get("entity_id") == "city_blankenberge":
                email = row.get("foi_email","")
                postal = row.get("foi_postal","")
                break
print("got_contact", bool(email), bool(postal))

row = {k: "" for k in fields}
row.update({
    "gap_id": "gap_agbblb_liquidated_jr2019only_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Blankenberge>AGB>liquidatie_L5",
    "entity_id": "agb_blankenberge",
    "what_is_missing": "Final BBC after 2019 plus liquidation slotbalans plus successor transfer plus confirmation no AGB JR2025 exists. Official last AGB JR 2019.",
    "why_it_matters": "Leftover unmined AGB of mined city Blankenberge. KBO 0877.301.751 stopgezet 21.03.2023. No primary JR2025 PDF. Do not invent euros.",
    "priority": "8",
    "recipient_body": "Stad Blankenberge / ex-AGB Blankenberge",
    "recipient_email": email,
    "recipient_postal": postal,
    "draft_letter_path": "docs/doge/foi/drafts/gap_agbblb_liquidated_jr2019only_l5.md",
    "status": "ready",
    "date_ready": "2026-08-17",
    "date_sent": "",
    "linked_commitment_id": "comm_agbblb_liquidated_jr_unpublished",
    "linked_leaderboard_id": "lb_agbblb_liquidated_jr2019only",
    "created_utc": "2026-08-17T18:25:00Z",
    "updated_utc": "2026-08-17T18:25:00Z",
    "notes": "tick1323; ready not sent; no sourced euros; not every-10",
})
# skip if already present
with p.open(encoding="utf-8", newline="") as f:
    ids = set(r["gap_id"] for r in csv.DictReader(f))
if row["gap_id"] in ids:
    print("exists")
else:
    with p.open("a", encoding="utf-8", newline="") as f:
        csv.DictWriter(f, fieldnames=fields, extrasaction="ignore").writerow(row)
    print("added")
