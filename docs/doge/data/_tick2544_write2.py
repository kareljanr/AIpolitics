from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2544_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_ritmica_hove_jr2025_nbb_pdf_2544"
EID = "vzw_ritmica_hove"

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
    "name_nl": "Medisch - Pedagogisch Instituut Ritmica (VAPH RTH+MFC dagcentra minderjarigen mentale handicap)",
    "name_fr": "ASBL Ritmica (VAPH)",
    "name_en": "Ritmica Hove VZW (leftover city_hove leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_hove",
    "community_language": "nl",
    "website": "https://www.ritmica.be/",
    "foi_email": "personeel@ritmica.be",
    "foi_postal": "Wouwstraat 44 2540 Hove",
    "notes": "tick2544 YE2025 Strong official native NBB PDF deposit 2026-00226136 + Strong KBO 0408.389.794 Actief 3 VE; 70/76A JUMP 5420432; omzet70 JUMP 168625 commercial-only vs large 73; 73 JUMP 5215346; 76A empty; envelope 70/76A JUMP 5420432; pnl LOSS narrower -53443; 9901 LOSS narrower -53079; equity DROP 751941; assets DROP 1767362; debt DROP 1015420; cash DROP 205034; kapitaalsubsidies DROP 51625; 62 JUMP 4599885; 630 DROP 52678; 66A DROP 7514; MVA DROP 294040; capex 9669; FTE JUMP 64.7; 3 VE leftover city_hove leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_hove leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_ritmica_hove_70_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5420432", "amount_min_eur": "5420432", "amount_max_eur": "5420432", "basis": "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +8.51%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 4995178 identical; envelope 70/76A for VZW because 70 present and commercial-only vs large 73; FOI VAPH matrix behind 5420432"},
    {"budget_id": "bud_ritmica_hove_omzet70_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "168625", "amount_min_eur": "168625", "amount_max_eur": "168625", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +2.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 164261 identical; commercial-only vs large 73 5215346"},
    {"budget_id": "bud_ritmica_hove_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5215346", "amount_min_eur": "5215346", "amount_max_eur": "5215346", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +8.88%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 4789809 identical; 733 5129729 JUMP +7.68%; 73-733 gap 85517 FOI"},
    {"budget_id": "bud_ritmica_hove_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4599885", "amount_min_eur": "4599885", "amount_max_eur": "4599885", "basis": "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +9.22%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 4211483 identical; FTE 9087 64.7 JUMP from 58.5"},
    {"budget_id": "bud_ritmica_hove_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "52678", "amount_min_eur": "52678", "amount_max_eur": "52678", "basis": "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP -25.51%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 70714 identical; capex 9669; MVA 294040 DROP"},
    {"budget_id": "bud_ritmica_hove_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-53079", "amount_min_eur": "-53079", "amount_max_eur": "-53079", "basis": "NBB VOL-VZW code 9901 bedrijfsverlies YE2025 JUMP LOSS narrower", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p6 native; YE2024 -129832 identical; 66A 7514 DROP; 640/8 43461 JUMP"},
    {"budget_id": "bud_ritmica_hove_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-53443", "amount_min_eur": "-53443", "amount_max_eur": "-53443", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 JUMP LOSS narrower", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p7 native; YE2024 -130112 identical; 9903 -53443 JUMP LOSS narrower"},
    {"budget_id": "bud_ritmica_hove_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "751941", "amount_min_eur": "751941", "amount_max_eur": "751941", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -7.01%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p5 native; YE2024 808611 identical; overgedragen 14 624627 DROP; kapitaalsubsidies 15 51625 DROP"},
    {"budget_id": "bud_ritmica_hove_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1767362", "amount_min_eur": "1767362", "amount_max_eur": "1767362", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -15.26%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p4 native; YE2024 2085594 identical; MVA 22/27 294040 DROP; cash 205034 DROP; capex 9669"},
    {"budget_id": "bud_ritmica_hove_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1015420", "amount_min_eur": "1015420", "amount_max_eur": "1015420", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -20.48%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p5 native; YE2024 1276983 identical; ST 42/48 905622 DROP"},
    {"budget_id": "bud_ritmica_hove_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "205034", "amount_min_eur": "205034", "amount_max_eur": "205034", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -55.31%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2544; PDF p4 native; YE2024 458809 identical; geldbeleggingen empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
