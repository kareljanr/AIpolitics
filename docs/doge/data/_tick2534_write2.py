from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2534_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_meerpaal_willebroek_jr2025_nbb_pdf_2534"
EID = "vzw_meerpaal_willebroek"

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
    "name_nl": "De Meerpaal (VAPH woon- en dagondersteuning)",
    "name_fr": "ASBL De Meerpaal (VAPH)",
    "name_en": "De Meerpaal VZW (leftover city_willebroek leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_willebroek",
    "community_language": "nl",
    "website": "https://demeerpaal.eu/",
    "foi_email": "onthaal@demeerpaal.eu",
    "foi_postal": "Kerkstraat 2B 2830 Willebroek",
    "notes": "tick2534 YE2025 Strong official native NBB PDF deposit 2026-00152128 + Strong KBO 0443.206.559 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A JUMP 427; envelope bruto9900 JUMP 3496689; pnl JUMP 228053; 9901 JUMP 213789; equity JUMP 1819290; assets JUMP 2714324; debt JUMP 895034; FTE JUMP 41.4; kapitaalsubsidies DROP 75307; destin691 empty DROP; cash JUMP 1263424; 1 VE leftover city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_willebroek leftover VAPH; NOT leftover WZC Seniorplaza remine@2532; NOT leftover WZC Ten Weldebrouc OCMW SKIP; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_meerpaal_willebroek_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 70 empty; 73 empty; envelope bruto9900 3496689 JUMP; FOI VAPH/Willebroek matrix behind bruto 3496689"},
    {"budget_id": "bud_meerpaal_willebroek_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 73 empty; 70 empty; envelope bruto9900 3496689 JUMP; FOI VAPH matrix behind 73 empty vs bruto"},
    {"budget_id": "bud_meerpaal_willebroek_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3496689", "amount_min_eur": "3496689", "amount_max_eur": "3496689", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +29.27% (VKT because 73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 2704972; 70 empty; 73 empty; 76A 427 JUMP; 70/76A n/a VKT; 74 empty"},
    {"budget_id": "bud_meerpaal_willebroek_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "427", "amount_min_eur": "427", "amount_max_eur": "427", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (was empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 76A empty; 76B 4068 DROP from 8335"},
    {"budget_id": "bud_meerpaal_willebroek_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "228053", "amount_min_eur": "228053", "amount_max_eur": "228053", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +17.65%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 193838; 9901 213789 JUMP + 75/76B 19111 - 65/66B 4847 = 228053; destin691 empty DROP"},
    {"budget_id": "bud_meerpaal_willebroek_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "213789", "amount_min_eur": "213789", "amount_max_eur": "213789", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +19.41%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p6 native; YE2024 179042; 62 3212694 JUMP; 630 67029 JUMP; 66A empty; 640/8 3176 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_meerpaal_willebroek_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1819290", "amount_min_eur": "1819290", "amount_max_eur": "1819290", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +13.98%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p5 native; YE2024 1596175; overgedragen 14 692414 JUMP; bestemde 13 1051569 DROP; kapitaalsubsidies 15 75307 DROP; fondsen 10 empty"},
    {"budget_id": "bud_meerpaal_willebroek_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2714324", "amount_min_eur": "2714324", "amount_max_eur": "2714324", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +13.69%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p4 native; YE2024 2387452; MVA 22/27 684835 JUMP; cash 1263424 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 77018"},
    {"budget_id": "bud_meerpaal_willebroek_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "895034", "amount_min_eur": "895034", "amount_max_eur": "895034", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +13.11%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p5 native; YE2024 791276; 17 19752 DROP; 42/48 873575 JUMP; voorzieningen 16 empty; overlopende 492/3 1707"},
    {"budget_id": "bud_meerpaal_willebroek_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1263424", "amount_min_eur": "1263424", "amount_max_eur": "1263424", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +1.43%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p4 native; YE2024 1245665; geldbeleggingen 50/53 empty; combined liquidity 1263424 JUMP vs prior 1245665; capex 77018"},
    {"budget_id": "bud_meerpaal_willebroek_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "41.4", "amount_min_eur": "41.4", "amount_max_eur": "41.4", "basis": "NBB VKT-VZW code 9087 FTE YE2025 JUMP +22.85%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2534; PDF p12 native; YE2024 33.7; 62 3212694 JUMP; destin691 empty DROP was 198612"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
