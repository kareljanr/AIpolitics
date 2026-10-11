from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2539_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_nloa_pelt_jr2025_nbb_pdf_2539"
EID = "vzw_nloa_pelt"

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Noord-Limburgs Open Atelier (NLOA / maatwerk)",
    "name_fr": "ASBL Noord-Limburgs Open Atelier (NLOA)",
    "name_en": "NLOA Pelt VZW (leftover city_pelt leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_pelt",
    "community_language": "nl",
    "website": "https://www.openatelier.be/",
    "foi_email": "info@openatelier.be",
    "foi_postal": "Haltstraat 90 bus 1 3900 Pelt",
    "notes": "tick2539 YE2025 Strong official native NBB PDF deposit 2026-00202608 + Strong KBO 0451.320.313 Actief 2 VE; omzet70 empty VKT; 73 empty VKT; 76A JUMP 12640; envelope bruto9900 JUMP 2492647; pnl DROP 187972; 9901 DROP 204001; equity JUMP 1138826; assets JUMP 2231233; debt JUMP 1092407; FTE JUMP 55; kapitaalsubsidies DROP 80775; destin691 empty; cash JUMP 831185; geldbeleggingen empty; aanbouw empty; capex 373330; leasing JUMP 223009; LT JUMP 310241; 2 VE leftover city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_pelt leftover maatwerk; NOT leftover-via-VE of leftover city_lommel; leftover maatwerk SBM remine@2538 leftover maatwerk t rad remine@2537 leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC unused-not-hardskip 0 leftover CIK HARD SKIP leftover maatwerk type now taken; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_nloa_pelt_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 70 empty; 73 empty; envelope bruto9900 2492647 JUMP; FOI WSE/maatwerk matrix behind 2492647"},
    {"budget_id": "bud_nloa_pelt_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 73 empty; 76A JUMP 12640; envelope bruto9900 2492647 JUMP"},
    {"budget_id": "bud_nloa_pelt_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2492647", "amount_min_eur": "2492647", "amount_max_eur": "2492647", "basis": "NBB VKT-VZW envelope bruto9900 YE2025 JUMP +9.66% (VKT because 73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 2272999 identical; 70 empty; 73 empty; 76A JUMP 12640"},
    {"budget_id": "bud_nloa_pelt_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12640", "amount_min_eur": "12640", "amount_max_eur": "12640", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (was empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 76A empty; 66A 2474 DROP"},
    {"budget_id": "bud_nloa_pelt_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "187972", "amount_min_eur": "187972", "amount_max_eur": "187972", "basis": "NBB VKT-VZW code 9904 winst (verlies) van het boekjaar YE2025 DROP -25.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 250684 identical; 9901 204001 DROP; destin691 empty"},
    {"budget_id": "bud_nloa_pelt_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "204001", "amount_min_eur": "204001", "amount_max_eur": "204001", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -21.10%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p5 native; YE2024 258566 identical; 62 2100801 JUMP; 630 163222 JUMP; 66A 2474 DROP; 640/8 22149 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_nloa_pelt_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1138826", "amount_min_eur": "1138826", "amount_max_eur": "1138826", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +17.34%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p4 native; YE2024 970537 identical; overgedragen 14 215143 JUMP; bestemde 13 337132; kapitaalsubsidies 15 80775 DROP; fondsen 10 505776"},
    {"budget_id": "bud_nloa_pelt_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2231233", "amount_min_eur": "2231233", "amount_max_eur": "2231233", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +29.57%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p3 native; YE2024 1722092 identical; MVA 22/27 899963 JUMP; cash 831185 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 373330; leasing 25 223009 JUMP"},
    {"budget_id": "bud_nloa_pelt_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1092407", "amount_min_eur": "1092407", "amount_max_eur": "1092407", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +45.35%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p4 native; YE2024 751555 identical; 17 310241 JUMP; 42/48 771573 JUMP; voorzieningen 16 empty; overlopende 492/3 10593"},
    {"budget_id": "bud_nloa_pelt_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "831185", "amount_min_eur": "831185", "amount_max_eur": "831185", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +77.36%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p3 native; YE2024 468647 identical; geldbeleggingen 50/53 empty; combined liquidity 831185 JUMP; capex 373330"},
    {"budget_id": "bud_nloa_pelt_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "55", "amount_min_eur": "55", "amount_max_eur": "55", "basis": "NBB VKT-VZW code 9087/100 FTE YE2025 JUMP +15.06%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2539; PDF p10-11 native; YE2024 47.8 identical; 105 YE 58.4; 62 2100801 JUMP; destin691 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
