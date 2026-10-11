from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2528_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_gerkenberg_bree_jr2025_nbb_pdf_2528"
EID = "vzw_gerkenberg_bree"

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
    "name_nl": "Welzijnscampus Gerkenberg",
    "name_fr": "ASBL Campus de bien-être Gerkenberg",
    "name_en": "Welzijnscampus Gerkenberg VZW (leftover city_bree leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_bree",
    "community_language": "nl",
    "website": "https://gerkenberg.be/",
    "foi_email": "info@gerkenberg.be",
    "foi_postal": "Meeuwerkiezel 90A 3960 Bree",
    "notes": "tick2528 YE2025 Strong official native NBB PDF deposit 2026-00239951 + Strong KBO 0867.804.659 Actief 1 VE; omzet70 JUMP 3341320 not commercial-only vs 73; 73 JUMP 4764956; 76A DROP 0; envelope omzet70 JUMP 3341320; 70/76A JUMP 8626038; pnl FLIP 542; 9901 JUMP 267165; equity DROP 1628000; assets DROP 14245271; debt DROP 12617271; FTE DROP 97.3; kapitaalsubsidies DROP 63013; destin691 empty; cash DROP 553077; geldbeleggingen empty; leftover city_bree leftover WZC 1 VE official zetel Bree leftover-mined AGB-only unused leftover type; prior-year identical; NOT leftover city_bree leftover WZC Boneput SLG 0845.064.196 commercial SKIP; NOT leftover city_arendonk leftover VAPH Talander remine@2527; NOT leftover city_middelkerke leftover WZC Haerlebout Squatina leftover-via-VE Oostende SKIP; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_gerkenberg_bree_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3341320", "amount_min_eur": "3341320", "amount_max_eur": "3341320", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +4.92% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p6 native; YE2024 3184464; 73 4764956 JUMP; envelope omzet70 3341320 JUMP; FOI RIZIV/Bree matrix behind 70 3341320"},
    {"budget_id": "bud_gerkenberg_bree_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4764956", "amount_min_eur": "4764956", "amount_max_eur": "4764956", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +0.35%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p6 native; YE2024 4748560; 733 subsidies 4764956; 70 3341320 JUMP; FOI WZC matrix behind 73 vs omzet70"},
    {"budget_id": "bud_gerkenberg_bree_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3341320", "amount_min_eur": "3341320", "amount_max_eur": "3341320", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +4.92% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p6 native; YE2024 3184464; 70 3341320 JUMP; 73 4764956 JUMP; 76A 0 DROP; 70/76A 8626038 JUMP; 74 519763 JUMP"},
    {"budget_id": "bud_gerkenberg_bree_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP to 0", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p6 native; YE2024 1543; 76B empty"},
    {"budget_id": "bud_gerkenberg_bree_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "542", "amount_min_eur": "542", "amount_max_eur": "542", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP PROFIT (was -112002)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p7 native; YE2024 -112002; 9901 267165 + 75 7041 - 65 273664 = 542; destin691 empty"},
    {"budget_id": "bud_gerkenberg_bree_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "267165", "amount_min_eur": "267165", "amount_max_eur": "267165", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +31.62% (was 202986)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p6 native; YE2024 202986; 62 6162053 JUMP; 630 774120 DROP; 66A 0 DROP; 640/8 19431 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_gerkenberg_bree_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1628000", "amount_min_eur": "1628000", "amount_max_eur": "1628000", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -0.27%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p5 native; YE2024 1632375; overgedragen 14 1314988 JUMP; bestemde 13 empty; kapitaalsubsidies 15 63013 DROP; fondsen 10 250000 FLAT"},
    {"budget_id": "bud_gerkenberg_bree_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14245271", "amount_min_eur": "14245271", "amount_max_eur": "14245271", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -3.22%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p4 native; YE2024 14719525; MVA 22/27 12858304 DROP; cash 553077 DROP; geldbeleggingen empty; aanbouw 27 514120 JUMP; capex 276645"},
    {"budget_id": "bud_gerkenberg_bree_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12617271", "amount_min_eur": "12617271", "amount_max_eur": "12617271", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -3.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p5 native; YE2024 13087151; 17 10772590 DROP; 42/48 1824816 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 19865 DROP"},
    {"budget_id": "bud_gerkenberg_bree_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "553077", "amount_min_eur": "553077", "amount_max_eur": "553077", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -5.76%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p4 native; YE2024 586854; geldbeleggingen 50/53 empty; combined liquidity 553077 DROP vs prior 586854; capex 276645"},
    {"budget_id": "bud_gerkenberg_bree_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2528; PDF p8 native; YE2024 691 empty; 791 empty; 9905 542 FLIP; overgedragen 14 1314988 JUMP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
