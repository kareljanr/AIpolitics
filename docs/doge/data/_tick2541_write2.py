from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2541_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_de_plek_rotselaar_jr2025_nbb_pdf_2541"
EID = "vzw_de_plek_rotselaar"

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
    "name_nl": "De Plek (VAPH dagcentrum volwassenen mentale handicap)",
    "name_fr": "ASBL De Plek (VAPH)",
    "name_en": "De Plek Rotselaar VZW (leftover city_rotselaar leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_rotselaar",
    "community_language": "nl",
    "website": "",
    "foi_email": "deplek@telenet.be",
    "foi_postal": "Hanewijk 44A 3118 Rotselaar",
    "notes": "tick2541 YE2025 Strong official native NBB PDF deposit 2026-00317818 + Strong KBO 0822.360.357 Actief 1 VE; bruto9900 DROP 8964; omzet70 DROP 17185; 73 JUMP 2322; 76A JUMP 216; envelope bruto9900 DROP 8964; pnl DROP 2750; 9901 DROP 2822; equity JUMP 23262; assets JUMP 39124; debt JUMP 15863; cash JUMP 12686; kapitaalsubsidies JUMP 9556; 62 DROP 289; 630 JUMP 5580; MVA JUMP 19432; capex 21649; FTE n/a MIC; 1 VE leftover city_rotselaar leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_rotselaar leftover VAPH; NOT leftover-via-VE; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_de_plek_rotselaar_bruto_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8964", "amount_min_eur": "8964", "amount_max_eur": "8964", "basis": "NBB MIC-VZW code 9900 brutomarge YE2025 DROP -32.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 13360 identical; envelope bruto9900 for MIC-VZW; FOI VAPH matrix behind 8964"},
    {"budget_id": "bud_de_plek_rotselaar_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "17185", "amount_min_eur": "17185", "amount_max_eur": "17185", "basis": "NBB MIC-VZW code 70 omzet YE2025 DROP -25.47%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 23059 identical; 73 JUMP 2322 from empty; 76A JUMP 216"},
    {"budget_id": "bud_de_plek_rotselaar_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2322", "amount_min_eur": "2322", "amount_max_eur": "2322", "basis": "NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP from empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 empty; FOI VAPH/gemeente matrix behind 2322"},
    {"budget_id": "bud_de_plek_rotselaar_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2750", "amount_min_eur": "2750", "amount_max_eur": "2750", "basis": "NBB MIC-VZW code 9904 winst (verlies) van het boekjaar YE2025 DROP -46.39%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 5130 identical; 9901 2822 DROP"},
    {"budget_id": "bud_de_plek_rotselaar_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2822", "amount_min_eur": "2822", "amount_max_eur": "2822", "basis": "NBB MIC-VZW code 9901 bedrijfswinst YE2025 DROP -45.70%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 5197 identical; 62 289 DROP; 630 5580 JUMP; 640/8 273 JUMP"},
    {"budget_id": "bud_de_plek_rotselaar_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "23262", "amount_min_eur": "23262", "amount_max_eur": "23262", "basis": "NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +112.32%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p4 native; YE2024 10956 identical; overgedragen 14 13706 JUMP; kapitaalsubsidies 15 9556 JUMP from empty"},
    {"budget_id": "bud_de_plek_rotselaar_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "39124", "amount_min_eur": "39124", "amount_max_eur": "39124", "basis": "NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +209.97%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p3 native; YE2024 12622 identical; MVA 22/27 19432 JUMP; cash 12686 JUMP; capex 21649"},
    {"budget_id": "bud_de_plek_rotselaar_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "15863", "amount_min_eur": "15863", "amount_max_eur": "15863", "basis": "NBB MIC-VZW code 17/49 schulden YE2025 JUMP +852.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p4 native; YE2024 1666 identical; ST 42/48 14942 JUMP; overige 48 11501 JUMP"},
    {"budget_id": "bud_de_plek_rotselaar_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12686", "amount_min_eur": "12686", "amount_max_eur": "12686", "basis": "NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +189.44%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p3 native; YE2024 4383 identical; kapitaalsubsidies JUMP 9556; debt JUMP 15863"},
    {"budget_id": "bud_de_plek_rotselaar_kapitaalsubsidies_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9556", "amount_min_eur": "9556", "amount_max_eur": "9556", "basis": "NBB MIC-VZW code 15 kapitaalsubsidies YE2025 JUMP from empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p4 native; YE2024 empty; linked to MVA aanschaffingen 21649"},
    {"budget_id": "bud_de_plek_rotselaar_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "289", "amount_min_eur": "289", "amount_max_eur": "289", "basis": "NBB MIC-VZW code 62 bezoldigingen YE2025 DROP -95.63%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2541; PDF p5 native; YE2024 6608 identical; FOI why personnel collapsed while cash JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
