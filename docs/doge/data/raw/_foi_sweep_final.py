"""FOI sweep tail: ranks 301-end material partials."""
import csv
from datetime import datetime, timezone
from collections import Counter

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

UPDATES = {
    "gap_afmps_budget_2025_26": (
        "Kamer 1281/022 OAP 2026: pers 81.6m fees 104.8m CF00 15.748m CF02 12.113m "
        "NAT 8.987m BCFI 2.929m ICT 6.435m Sciensano class 10.79m. Residual: 2025 outturn + AMM root cause"
    ),
    "gap_actiris_2025_26_l5": (
        "Institutional 2025 727m / 2026 689m; ACS 276m partners 67m (press path); BCR prog 648.1m. "
        "Residual: full L5 matrix same structure as RA2024"
    ),
    "gap_kce_jaarrekening_2024_26": (
        "Kamer 1281/023: pers 12.398m goods 12.224m (Trials 10.119m) receipts class 25.546m. "
        "Residual: statutory outturn 2024-25 + Trials contractor L5"
    ),
    "gap_nbn_antennes_l5": (
        "Kamer 1281/023: NBN pers 3.778m ops 3.703m antennas 4.462m sales 6.1m state sub 6.545m. "
        "Residual: named Antennes-Normes beneficiaries"
    ),
    "gap_forem_budget": (
        "APE cadastre open XLSX named employers+EUR 2024-25 (e.g. Mons 11.3m CPAS Liege 9.7m). "
        "Residual: full institutional RA TCO recon SEC"
    ),
    "gap_forem_ra_outturn_2024_25": (
        "APE cadastre open data fills named channel; RA2023 structure known. "
        "Residual: institutional RA/accounts 2024-25 same structure"
    ),
    "gap_forem_sec_ra_recon_l5_2025": (
        "APE open cadastre + CoA SEC ~3.033bn dep class. Residual: full recon RA to SEC + non-APE partners"
    ),
    "gap_screen_brussels_l5": (
        "Session/year aggregates: 2025 ~3m/26 projects; last session 960k/8; Mar2026 session 715k/8. "
        "Residual: full named L5 matrix + BCR article codes"
    ),
}

path = "docs/doge/data/foi_queue.csv"
with open(path, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    fields = rdr.fieldnames
    rows = list(rdr)

n = 0
for r in rows:
    gid = r.get("gap_id")
    if gid not in UPDATES:
        continue
    if r.get("status") in ("answered", "cancelled"):
        continue
    r["status"] = "partial"
    r["response_summary"] = UPDATES[gid]
    r["updated_utc"] = NOW
    notes = r.get("notes") or ""
    if "sweep2026-08-05" not in notes:
        r["notes"] = (notes + " | sweep2026-08-05: status partial material public fill").strip(" |")
    n += 1
    print("partial", gid)

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

c = Counter(r.get("status") for r in rows)
print("updated", n)
print(dict(c))
print("ready", c.get("ready", 0), "partial", c.get("partial", 0), "answered", c.get("answered", 0))
