"""FOI sweep: VLAIO CIE multi-year cash path -> gap_vl_cie_l5_beneficiaries partial."""
import csv
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# FOI
path = "docs/doge/data/foi_queue.csv"
with open(path, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    fields = rdr.fieldnames
    rows = list(rdr)

for r in rows:
    if r.get("gap_id") != "gap_vl_cie_l5_beneficiaries":
        continue
    r["status"] = "partial"
    r["response_summary"] = (
        "VLAIO uitgaventoetsing 22-07-2026: cash path 75/150/229/259m 2022-25 "
        "(+45m exception 2025); raming 217.5/240/258.3/263.6/269/268.5m 2026-31; "
        "EY2025 ref 197.7m to 41 installaties. Residual: named beneficiary EUR table "
        "(Bijlage1/Excel) + KBO + exception list"
    )
    r["updated_utc"] = NOW
    notes = r.get("notes") or ""
    if "sweep2026-08-05" not in notes:
        r["notes"] = (notes + " | sweep2026-08-05: multi-year cash path strong; named L5 residual").strip(" |")
    print("FOI partial")

with open(path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# source
sp = "docs/doge/data/sources.csv"
with open(sp, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    sf = rdr.fieldnames
    srows = list(rdr)
sid = "src_vlaio_cie_uitgaventoetsing_2026"
if sid not in {r["source_id"] for r in srows}:
    srows.append(
        {
            "source_id": sid,
            "title": "VLAIO Uitgaventoetsing CIE Carbon Leakage internationale vergelijking 2026",
            "url": "https://www.vlaio.be/nl/media/3087",
            "publisher": "VLAIO / Vlaamse overheid",
            "accessed_date": "2026-08-05",
            "source_class": "agency",
            "notes": "Cash path 2022-31 + scenarios; named beneficiaries annex not fully public HTML; sweep2026-08-05",
        }
    )
    with open(sp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=sf)
        w.writeheader()
        w.writerows(srows)
    print("source added")

# commitment
cp = "docs/doge/data/commitments.csv"
with open(cp, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    cf = rdr.fieldnames
    crows = list(rdr)
cid = "cmt_vl_cie_cash_path_2022_31"
if cid not in {r["commitment_id"] for r in crows}:
    row = {k: "" for k in cf}
    row.update(
        {
            "commitment_id": cid,
            "title": "Flanders CIE carbon leakage compensation multi-year cash path 2022-2031",
            "entity_id": "vlaanderen_gov",
            "beneficiary": "Energy-intensive industry CIE/ICL installations",
            "legal_basis": "Vlaamse CIE regeling + VLAIO uitgaventoetsing 22 Jul 2026",
            "decision_date": "2026-07-22",
            "start_year": "2022",
            "end_year": "2031",
            "total_envelope_eur": "",
            "cash_by_year": '{"2022":75000000,"2023":150000000,"2024":229000000,"2025":259000000,"2025_exception":45000000,"2026_raming":217500000,"2027":240000000,"2028":258300000,"2029":263600000,"2030":269000000,"2031":268500000,"ey2025_ref_installations":41,"ey2025_ref_m":197700000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.vlaio.be/nl/media/3087",
            "stated_goal": "Carbon leakage risk compensation for exposed industry",
            "cut_option": "Publish named beneficiary table; scenario cuts (refinery NACE / CO2 factor)",
            "source_id": sid,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>Energie>CIE>cash_path",
            "notes": "sweep2026-08-05 partial gap_vl_cie_l5_beneficiaries; named L5 residual FOI",
        }
    )
    crows.append(row)
    with open(cp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cf)
        w.writeheader()
        w.writerows(crows)
    print("cmt added")
else:
    print("cmt exists")
