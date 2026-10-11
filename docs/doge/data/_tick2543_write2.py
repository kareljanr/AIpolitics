from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2543_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_iona_nijlen_jr2025_nbb_pdf_2543"
EID = "vzw_iona_nijlen"

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
    "name_nl": "Iona voor heilpedagogie en sociaaltherapie (VAPH woonondersteuning minderjarigen mentale handicap)",
    "name_fr": "ASBL Iona (VAPH)",
    "name_en": "Iona Nijlen VZW (leftover city_nijlen leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_nijlen",
    "community_language": "nl",
    "website": "https://www.ionavzw.be/",
    "foi_email": "info@ionavzw.be",
    "foi_postal": "Nieuwe Bevelsesteenweg 66 2560 Nijlen",
    "notes": "tick2543 YE2025 Strong official native NBB PDF deposit 2026-00186964 + Strong KBO 0410.269.814 Actief 1 VE; bruto9900 JUMP 5573753; omzet70 empty VKT; 73 empty VKT; 76A DROP 3155; envelope bruto9900 JUMP 5573753; pnl JUMP 252169; 9901 JUMP 219000; equity JUMP 2951999; assets JUMP 4055293; debt JUMP 1080294; cash JUMP 958823; kapitaalsubsidies DROP 13159; 62 JUMP 5160505; 630 DROP 101262; 66A JUMP 56009; MVA JUMP 919927; capex 147795; FTE 70; 1 VE leftover city_nijlen leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_nijlen leftover VAPH; NOT leftover-via-VE; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_iona_nijlen_bruto_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5573753", "amount_min_eur": "5573753", "amount_max_eur": "5573753", "basis": "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +4.82%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 5317391 identical; envelope bruto9900 for VKT-VZW because 73 empty; FOI VAPH matrix behind 5573753"},
    {"budget_id": "bud_iona_nijlen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3155", "amount_min_eur": "3155", "amount_max_eur": "3155", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -65.48%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 9139 identical; omzet70 empty VKT; 73 empty VKT"},
    {"budget_id": "bud_iona_nijlen_personnel62_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5160505", "amount_min_eur": "5160505", "amount_max_eur": "5160505", "basis": "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +3.07%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 5006886 identical; FTE 9087 70 JUMP from 69.9"},
    {"budget_id": "bud_iona_nijlen_630_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "101262", "amount_min_eur": "101262", "amount_max_eur": "101262", "basis": "NBB VKT-VZW code 630 afschrijvingen YE2025 DROP -16.02%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 120580 identical; capex 147795; MVA 919927 JUMP"},
    {"budget_id": "bud_iona_nijlen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "219000", "amount_min_eur": "219000", "amount_max_eur": "219000", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +91.58%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 114312 identical; 66A 56009 JUMP; 640/8 39795 JUMP"},
    {"budget_id": "bud_iona_nijlen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "252169", "amount_min_eur": "252169", "amount_max_eur": "252169", "basis": "NBB VKT-VZW code 9904 winst (verlies) van het boekjaar YE2025 JUMP +61.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p5 native; YE2024 156055 identical; 9903 252169 JUMP"},
    {"budget_id": "bud_iona_nijlen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2951999", "amount_min_eur": "2951999", "amount_max_eur": "2951999", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +8.70%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p4 native; YE2024 2715739 identical; overgedragen 14 1731760 JUMP; kapitaalsubsidies 15 13159 DROP"},
    {"budget_id": "bud_iona_nijlen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4055293", "amount_min_eur": "4055293", "amount_max_eur": "4055293", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +10.81%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p3 native; YE2024 3659615 identical; MVA 22/27 919927 JUMP; cash 958823 JUMP; capex 147795"},
    {"budget_id": "bud_iona_nijlen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1080294", "amount_min_eur": "1080294", "amount_max_eur": "1080294", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +17.31%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p4 native; YE2024 920876 identical; ST 42/48 1065294 JUMP; leveranciers 264765 JUMP"},
    {"budget_id": "bud_iona_nijlen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "958823", "amount_min_eur": "958823", "amount_max_eur": "958823", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +18.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p3 native; YE2024 809171 identical; geldbeleggingen 1776201 JUMP"},
    {"budget_id": "bud_iona_nijlen_kapitaalsubsidies_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "13159", "amount_min_eur": "13159", "amount_max_eur": "13159", "basis": "NBB VKT-VZW code 15 kapitaalsubsidies YE2025 DROP -54.73%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2543; PDF p4 native; YE2024 29068 identical; FOI why DROP while capex 147795 aanbouw JUMP 84450"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
