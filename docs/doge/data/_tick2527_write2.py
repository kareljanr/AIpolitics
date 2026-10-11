from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2527_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_talander_arendonk_jr2025_nbb_pdf_2527"
EID = "vzw_talander_arendonk"

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
    "name_nl": "Talander",
    "name_fr": "ASBL Talander",
    "name_en": "Talander VZW (leftover city_arendonk leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_arendonk",
    "community_language": "nl",
    "website": "https://www.talander.be/",
    "foi_email": "info@talander.be",
    "foi_postal": "De Lusthoven 88 2370 Arendonk",
    "notes": "tick2527 YE2025 Strong official native NBB PDF deposit 2026-00192214 + Strong KBO 0433.306.225 Actief 2 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 1603209; pnl JUMP 142992; 9901 JUMP 140447; equity JUMP 1662056; assets JUMP 2205622; debt DROP 543566; FTE JUMP 18.8; kapitaalsubsidies DROP 297292; destin691 empty; cash JUMP 1050120; geldbeleggingen empty; leftover city_arendonk leftover VAPH 2 VE official zetel Arendonk leftover-mined AGB-only unused leftover type; prior-year identical; NOT leftover city_arendonk leftover WZC WZGA remine@2526; NOT leftover OCMW Arendonk De Peulder 0212.236.097 SKIP; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_talander_arendonk_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 1603209 JUMP; FOI VAPH/Arendonk matrix behind bruto 1603209"},
    {"budget_id": "bud_talander_arendonk_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 empty; 70 empty; FOI VAPH matrix behind empty 73 vs bruto JUMP"},
    {"budget_id": "bud_talander_arendonk_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1603209", "amount_min_eur": "1603209", "amount_max_eur": "1603209", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +11.50% (VKT because omzet70+73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 1437845; 70 empty; 73 empty; 76A empty; 74 empty"},
    {"budget_id": "bud_talander_arendonk_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_talander_arendonk_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "142992", "amount_min_eur": "142992", "amount_max_eur": "142992", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +20.90% (was 118277)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 118277; 9901 140447 + 75 12037 - 65 6780 - 67/77 2712 = 142992; destin691 empty"},
    {"budget_id": "bud_talander_arendonk_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "140447", "amount_min_eur": "140447", "amount_max_eur": "140447", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +22.47% (was 114678)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p5 native; YE2024 114678; 62 1383895 JUMP; 630 67977 JUMP; 66A empty; 640/8 10890 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_talander_arendonk_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1662056", "amount_min_eur": "1662056", "amount_max_eur": "1662056", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +8.34%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p4 native; YE2024 1534181; overgedragen 14 1364764 JUMP; bestemde 13 empty; kapitaalsubsidies 15 297292 DROP; fondsen 10 empty"},
    {"budget_id": "bud_talander_arendonk_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2205622", "amount_min_eur": "2205622", "amount_max_eur": "2205622", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.43%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p3 native; YE2024 2112021; MVA 22/27 882868 JUMP; cash 1050120 JUMP; geldbeleggingen empty; aanbouw 27 29492 JUMP; capex 70814"},
    {"budget_id": "bud_talander_arendonk_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "543566", "amount_min_eur": "543566", "amount_max_eur": "543566", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -5.93%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p4 native; YE2024 577840; 17 136542 DROP; 42/48 234367 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 172657 DROP"},
    {"budget_id": "bud_talander_arendonk_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1050120", "amount_min_eur": "1050120", "amount_max_eur": "1050120", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +12.64%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p3 native; YE2024 932246; geldbeleggingen 50/53 empty; combined liquidity 1050120 JUMP vs prior 932246; capex 70814"},
    {"budget_id": "bud_talander_arendonk_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2527; PDF p6 native; YE2024 691 empty; 791 empty; 9905 142992 JUMP; overgedragen 14 1364764 JUMP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
