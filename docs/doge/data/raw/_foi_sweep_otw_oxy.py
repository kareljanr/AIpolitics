"""FOI sweep: OTW BI2026 article path + Plan Oxygene commune annexes."""
import csv
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# --- FOI status ---
foi_path = "docs/doge/data/foi_queue.csv"
with open(foi_path, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    fields = rdr.fieldnames
    rows = list(rdr)

updates = {
    "gap_otw_dotatie_cash": {
        "status": "partial",
        "response_summary": (
            "PW answer Nov2025 annex 3472: BI2026 OTW regional interventions by programme "
            "045.xxx CE=CL total 877.456m (045.014 ops 619.277; invest ops 57.943; school 69.251; "
            "Tram Liege 40.015; social 35.736; electrification 22.900; Metro Charleroi 13.284; "
            "infra 11.083; PMR 5.277; Namur 2.690). Residual: 2023-25 outturn same codes; "
            "Henry 960m recon; CSP multi-year cash"
        ),
        "note": "sweep2026-08-05: PW 3472 BI2026 article path 877.456m; residual multi-year outturn",
    },
    "gap_plan_oxygene_cash": {
        "status": "partial",
        "response_summary": (
            "PW answer Apr2024 annex 3102: commune sollicite matrix 2024-2026 (~34 communes); "
            "e.g. Charleroi 121.1/60.5/40.4m; Liege 118.2/59.1/39.4m; Namur 47.6/23.8/15.9m; "
            "Mons 40/21/14m. Regional paid to 31.12.2023: CRAC LT 44.2m + interest 12.6m. "
            "Residual: definitive outturns; CRAC 210m six-city L5; regional cost series 2024-26"
        ),
        "note": "sweep2026-08-05: PW 3102 commune x year sollicite table; residual outturns",
    },
}

for r in rows:
    gid = r.get("gap_id")
    if gid not in updates:
        continue
    u = updates[gid]
    r["status"] = u["status"]
    r["response_summary"] = u["response_summary"]
    r["updated_utc"] = NOW
    notes = r.get("notes") or ""
    if u["note"] not in notes:
        r["notes"] = (notes + " | " + u["note"]).strip(" |")
    print("FOI", gid, "->", u["status"])

with open(foi_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# --- sources ---
sp = "docs/doge/data/sources.csv"
with open(sp, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    sf = rdr.fieldnames
    srows = list(rdr)
sids = {r["source_id"] for r in srows}

new_sources = [
    {
        "source_id": "src_pw_otw_dotatie_bi2026_annex_3472",
        "title": "Parlement Wallonie Q/R OTW BI2026 regional interventions annex 3472",
        "url": "http://nautilus.parlement-wallon.be/Archives_ARQE/3472.pdf",
        "publisher": "Parlement de Wallonie",
        "accessed_date": "2026-08-05",
        "source_class": "parliament",
        "notes": "BI2026 OTW path total 877.456m by 045.xxx; page Q/R https://www.parlement-wallonie.be/pwpages?p=interp-questions-voir&type=28&iddoc=139347; sweep2026-08-05",
    },
    {
        "source_id": "src_pw_plan_oxygene_annex_3102",
        "title": "Parlement Wallonie Q/R Plan Oxygene commune sollicite 2024-26 annex 3102",
        "url": "http://nautilus.parlement-wallon.be/Archives_ARQE/3102.pdf",
        "publisher": "Parlement de Wallonie",
        "accessed_date": "2026-08-05",
        "source_class": "parliament",
        "notes": "Commune x year sollicite table; CRAC paid 44.2m + interest 12.6m to 31.12.2023; Q/R iddoc=127109; sweep2026-08-05",
    },
]
for s in new_sources:
    if s["source_id"] not in sids:
        srows.append(s)
        print("source", s["source_id"])
with open(sp, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf)
    w.writeheader()
    w.writerows(srows)

# --- commitments ---
cp = "docs/doge/data/commitments.csv"
with open(cp, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    cf = rdr.fieldnames
    crows = list(rdr)
cids = {r["commitment_id"] for r in crows}

new_cmts = [
    {
        "commitment_id": "cmt_otw_regional_dot_bi2026_877m",
        "title": "OTW/TEC regional interventions BI2026 article path 877.456m",
        "entity_id": "wallonie_gov",
        "beneficiary": "OTW / TEC network",
        "legal_basis": "Walloon budget BI2026 programmes 045.xxx + PW answer Nov 2025",
        "decision_date": "2025-11-25",
        "start_year": "2026",
        "end_year": "2026",
        "total_envelope_eur": "877456000",
        "cash_by_year": '{"2026":877456000,"ops_045_014":619277000,"school_045_010":69251000,"invest_ops_045_026":57943000,"tram_liege_045_023":40015000,"social_045_016":35736000,"electro_045_050":22900000,"metro_charleroi_045_027":13284000,"infra_045_024":11083000,"pmr_045_011":5277000,"namur_045_031":2690000}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "http://nautilus.parlement-wallon.be/Archives_ARQE/3472.pdf",
        "stated_goal": "Regional public transport operating and investment support",
        "cut_option": "CSP renegotiation; dual De Lijn unit-cost; FOI 2023-25 outturn residual",
        "source_id": "src_pw_otw_dotatie_bi2026_annex_3472",
        "confidence": "strong",
        "hierarchy_path": "Wallonie>Mobilite>OTW>dotation_BI2026",
        "notes": "sweep2026-08-05 partial gap_otw_dotatie_cash; hors PRW/FEDER; dual Henry 960m class residual recon",
    },
    {
        "commitment_id": "cmt_plan_oxygene_commune_sollicite_2024_26",
        "title": "Plan Oxygene commune sollicite matrix 2024-2026 (PW annex 3102)",
        "entity_id": "wallonie_gov",
        "beneficiary": "Walloon communes via CRAC / Plan Oxygene",
        "legal_basis": "Plan Oxygene + CRAC + PW answer Apr 2024",
        "decision_date": "2024-04-19",
        "start_year": "2024",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": '{"charleroi_2024":121056374.29,"charleroi_2025":60528187,"charleroi_2026":40352124.76,"liege_2024":118200000,"liege_2025":59100000,"liege_2026":39400000,"namur_2024":47608591.10,"mons_2024":40000000,"mons_2025":21000000,"mons_2026":14000000,"crac_paid_to_2023_12":44200000,"interest_2022_23":12600000,"note":"sollicite not definitive outturn"}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://nautilus.parlement-wallon.be/Archives_ARQE/3102.pdf",
        "stated_goal": "Local authority financial rescue / debt relief path",
        "cut_option": "Publish definitive outturns; dual CRAC 210m six-city FOI residual",
        "source_id": "src_pw_plan_oxygene_annex_3102",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>CRAC>Plan_Oxygene>commune_sollicite",
        "notes": "sweep2026-08-05 partial gap_plan_oxygene_cash; medium because sollicite not validated cash",
    },
]

for c in new_cmts:
    if c["commitment_id"] in cids:
        print("cmt exists", c["commitment_id"])
        continue
    row = {k: "" for k in cf}
    row.update(c)
    crows.append(row)
    print("cmt", c["commitment_id"])

with open(cp, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf)
    w.writeheader()
    w.writerows(crows)

print("done")
