from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2525_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_het_laar_wingene_jr2025_nbb_pdf_2525"
EID = "vzw_het_laar_wingene"

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
    "name_nl": "Het Laar (WZC Maria ter Ruste)",
    "name_fr": "ASBL Het Laar (MRS Maria ter Ruste)",
    "name_en": "Het Laar VZW (leftover city_wingene leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_wingene",
    "community_language": "nl",
    "website": "https://www.hetlaar.gvo.be/nl/",
    "foi_email": "hetlaar@gvo.be",
    "foi_postal": "Pastorijstraat 56 8750 Wingene",
    "notes": "tick2525 YE2025 Strong official native NBB PDF deposit 2026-00216674 + Strong KBO 0469.123.870 Actief 1 VE; omzet70 JUMP 6634002 not commercial-only vs 73; 73 JUMP 943247; 76A DROP 39781; envelope omzet70 JUMP 6634002; 70/76A JUMP 7752280; pnl DROP 215832; 9901 DROP 332059; equity JUMP 3727774; assets DROP 13833205; debt DROP 10105432; FTE JUMP 76.9; kapitaalsubsidies empty; destin691 empty; cash JUMP 2393834; geldbeleggingen empty; leftover city_wingene leftover WZC 1 VE official zetel Wingene leftover-mined AGB-only; prior-year identical; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_het_laar_wingene_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6634002", "amount_min_eur": "6634002", "amount_max_eur": "6634002", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +0.91% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p7 native; YE2024 6573951; 73 943247 JUMP; envelope omzet70 6634002 JUMP; FOI Departement Zorg/RIZIV/Wingene matrix behind omzet 6634002"},
    {"budget_id": "bud_het_laar_wingene_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "943247", "amount_min_eur": "943247", "amount_max_eur": "943247", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.44%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p7 native; YE2024 894610; 733 subsidies 943247; FOI Departement Zorg/RIZIV matrix behind 73 JUMP vs omzet JUMP"},
    {"budget_id": "bud_het_laar_wingene_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6634002", "amount_min_eur": "6634002", "amount_max_eur": "6634002", "basis": "NBB VOL-VZW envelope omzet 70 YE2025 JUMP +0.91% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p7 native; YE2024 6573951; 70/76A bedrijfsopbrengsten 7752280 JUMP; 73 943247; 76A 39781 DROP; 74 135250 JUMP"},
    {"budget_id": "bud_het_laar_wingene_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "39781", "amount_min_eur": "39781", "amount_max_eur": "39781", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -54.58%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p7 native; YE2024 87590; 76B empty"},
    {"budget_id": "bud_het_laar_wingene_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "215832", "amount_min_eur": "215832", "amount_max_eur": "215832", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -39.00% (was 353774)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p8 native; YE2024 353774; 9901 332059 + 75 23385 - 65 139355 - 67/77 256 = 215832; destin691 empty"},
    {"budget_id": "bud_het_laar_wingene_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "332059", "amount_min_eur": "332059", "amount_max_eur": "332059", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -30.56% (was 478207)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p7 native; YE2024 478207; 62 5138482 JUMP; 630 800777 JUMP; 66A 0 DROP; 640/8 9732 DROP; 635/9 0; 631/4 empty"},
    {"budget_id": "bud_het_laar_wingene_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3727774", "amount_min_eur": "3727774", "amount_max_eur": "3727774", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +6.15%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p6 native; YE2024 3511941; overgedragen 14 1177865 JUMP; bestemde 13 2196757 FLAT; kapitaalsubsidies 15 empty; fondsen 10 353152 FLAT"},
    {"budget_id": "bud_het_laar_wingene_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "13833205", "amount_min_eur": "13833205", "amount_max_eur": "13833205", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -2.28%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p5 native; YE2024 14155911; MVA 22/27 10673260 DROP; cash 2393834 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 166225"},
    {"budget_id": "bud_het_laar_wingene_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "10105432", "amount_min_eur": "10105432", "amount_max_eur": "10105432", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -5.06%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p6 native; YE2024 10643970; 17 7980000 DROP; 42/48 2119604 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 5827 DROP"},
    {"budget_id": "bud_het_laar_wingene_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2393834", "amount_min_eur": "2393834", "amount_max_eur": "2393834", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +9.89%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p5 native; YE2024 2178385; geldbeleggingen 50/53 empty; combined liquidity 2393834 JUMP vs prior 2178385; capex 166225"},
    {"budget_id": "bud_het_laar_wingene_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2525; PDF p9 native; YE2024 691 empty; 791 empty; 9905 215832 DROP; overgedragen 14 1177865 JUMP; bestemde 13 2196757 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
