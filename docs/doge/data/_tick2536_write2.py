from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2536_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_terluchte_oostkamp_jr2025_nbb_pdf_2536"
EID = "vzw_terluchte_oostkamp"

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
    "name_nl": "Ter Luchte (WZC Ter Luchte)",
    "name_fr": "ASBL Ter Luchte (MRS)",
    "name_en": "Ter Luchte VZW (leftover city_oostkamp leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_oostkamp",
    "community_language": "nl",
    "website": "https://terluchte.be/",
    "foi_email": "info@terluchte.be",
    "foi_postal": "Sint-Elooisstraat 87 8020 Oostkamp",
    "notes": "tick2536 YE2025 Strong official native NBB PDF deposit 2026-00183286 + Strong KBO 0738.896.510 Actief 1 VE; omzet70 JUMP 6149223; 73 JUMP 1101466; 76A DROP 10750; envelope omzet70 JUMP 6149223; pnl DROP 25442; 9901 DROP 102104; equity JUMP 2174137; assets DROP 6337256; debt DROP 4163119; FTE JUMP 79.5; kapitaalsubsidies JUMP 750000; destin691 empty; cash JUMP 901089; geldbeleggingen DROP empty was 1550000; aanbouw JUMP 1460611; capex 1393578; 1 VE leftover city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type; prior-year RESTATED; FIRST LOCK leftover city_oostkamp leftover WZC; NOT leftover-via-VE of a DIFFERENT leftover city; leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie leftover WZC type now taken; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_terluchte_oostkamp_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6149223", "amount_min_eur": "6149223", "amount_max_eur": "6149223", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +0.61% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p7 native; YE2024 70 6111705 restated; 73 1101466 JUMP; envelope omzet70 6149223 JUMP; FOI RIZIV/Oostkamp matrix behind 6149223"},
    {"budget_id": "bud_terluchte_oostkamp_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1101466", "amount_min_eur": "1101466", "amount_max_eur": "1101466", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +8.50%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p7 native; YE2024 73 1015211 restated; 733 1101466 JUMP; 73-733 gap 0; 70 6149223 JUMP"},
    {"budget_id": "bud_terluchte_oostkamp_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6149223", "amount_min_eur": "6149223", "amount_max_eur": "6149223", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +0.61% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p7 native; YE2024 6111705 restated; 70 6149223; 73 1101466; 76A 10750 DROP; 70/76A 7698977 JUMP +0.85%; 74 437537 DROP"},
    {"budget_id": "bud_terluchte_oostkamp_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "10750", "amount_min_eur": "10750", "amount_max_eur": "10750", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -45.28%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p7 native; YE2024 76A 19645 restated; 66A 12952 JUMP"},
    {"budget_id": "bud_terluchte_oostkamp_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "25442", "amount_min_eur": "25442", "amount_max_eur": "25442", "basis": "NBB VOL-VZW code 9904 winst (verlies) van het boekjaar YE2025 DROP -94.70%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p8 native; YE2024 480474 restated; 9901 102104 DROP; destin691 empty"},
    {"budget_id": "bud_terluchte_oostkamp_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "102104", "amount_min_eur": "102104", "amount_max_eur": "102104", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -79.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p7 native; YE2024 501893 restated; 62 5216486 JUMP; 630 201203 JUMP; 66A 12952 JUMP; 640/8 24567 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_terluchte_oostkamp_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2174137", "amount_min_eur": "2174137", "amount_max_eur": "2174137", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +55.44%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p6 native; YE2024 1398695 restated; overgedragen 14 1424137 JUMP; bestemde 13 empty; kapitaalsubsidies 15 750000 JUMP (was empty); fondsen 10 empty"},
    {"budget_id": "bud_terluchte_oostkamp_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6337256", "amount_min_eur": "6337256", "amount_max_eur": "6337256", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -3.93%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p5 native; YE2024 6596475 restated; MVA 22/27 4455619 JUMP; cash 901089 JUMP; geldbeleggingen empty DROP was 1550000; aanbouw 27 1460611 JUMP; capex 1393578"},
    {"budget_id": "bud_terluchte_oostkamp_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4163119", "amount_min_eur": "4163119", "amount_max_eur": "4163119", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -19.91%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p6 native; YE2024 5197780 restated; 17 2625000 DROP; 42/48 1306402 DROP; voorzieningen 16 empty; overlopende 492/3 231717"},
    {"budget_id": "bud_terluchte_oostkamp_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "901089", "amount_min_eur": "901089", "amount_max_eur": "901089", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +77.79%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF p5 native; YE2024 506828 restated; geldbeleggingen 50/53 empty DROP was 1550000; combined liquidity 901089 DROP vs prior 2056828; capex 1393578"},
    {"budget_id": "bud_terluchte_oostkamp_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "79.5", "amount_min_eur": "79.5", "amount_max_eur": "79.5", "basis": "NBB VOL-VZW code 9087 FTE YE2025 JUMP +2.05%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2536; PDF native; YE2024 77.9 restated; 1003 YE 79.5; 9086 107 koppen was 112; 62 5216486 JUMP; destin691 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
