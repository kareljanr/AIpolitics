from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2530_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_consolata_zaventem_jr2025_nbb_pdf_2530"
EID = "vzw_consolata_zaventem"

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
    "name_nl": "Consolata Regio Zaventem (WZC Sint-Antonius)",
    "name_fr": "ASBL Consolata Regio Zaventem (MRS Sint-Antonius)",
    "name_en": "Consolata Regio Zaventem VZW (leftover city_zaventem leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_zaventem",
    "community_language": "nl",
    "website": "https://www.sintantoniuszaventem.be/",
    "foi_email": "kristien.vogelaers@sintantoniuszaventem.be",
    "foi_postal": "Hoogstraat 52 1930 Zaventem",
    "notes": "tick2530 YE2025 Strong official native NBB PDF deposit 2026-00259909 + Strong KBO 0457.206.827 Actief 1 VE; omzet70 JUMP 8969085 not commercial-only vs 73; 73 JUMP 1672350; 76A DROP 1316; envelope omzet70 JUMP 8969085; pnl JUMP -109012; 9901 JUMP FLIP 86348; equity DROP 7528775; assets DROP 20506369; debt DROP 12977594; FTE DROP 124; kapitaalsubsidies DROP 5686964; destin691 empty; cash JUMP 800197; leftover city_zaventem leftover WZC 1 VE official zetel Zaventem leftover-mined AGB-only unused leftover type; prior-year identical; NOT leftover city_putte leftover WZC CONSOLATA 0457.207.223 remine@2529 SKIP; NOT leftover city_grimbergen leftover WZC Heilig Hart remine@2074; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_consolata_zaventem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8969085", "amount_min_eur": "8969085", "amount_max_eur": "8969085", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +4.03% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p7 native; YE2024 8621308; 73 1672350 JUMP; envelope omzet70 8969085 JUMP; FOI RIZIV/Zaventem matrix behind 70 8969085"},
    {"budget_id": "bud_consolata_zaventem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1672350", "amount_min_eur": "1672350", "amount_max_eur": "1672350", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +2.78%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p7 native; YE2024 1627050; 733 subsidies 1672350 JUMP; 70 8969085 JUMP; FOI WZC matrix behind 73 vs omzet70"},
    {"budget_id": "bud_consolata_zaventem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8969085", "amount_min_eur": "8969085", "amount_max_eur": "8969085", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +4.03% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p7 native; YE2024 8621308; 70 8969085 JUMP; 73 1672350 JUMP; 76A 1316 DROP; 70/76A 10764429 JUMP; 74 121677 DROP"},
    {"budget_id": "bud_consolata_zaventem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1316", "amount_min_eur": "1316", "amount_max_eur": "1316", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -97.92%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p7 native; YE2024 63290; 76B empty"},
    {"budget_id": "bud_consolata_zaventem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-109012", "amount_min_eur": "-109012", "amount_max_eur": "-109012", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 JUMP (smaller loss; was -389295)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p8 native; YE2024 -389295; 9901 FLIP 86348 + 75 220998 - 65 382206 - 67/77 34152 = -109012; destin691 empty"},
    {"budget_id": "bud_consolata_zaventem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "86348", "amount_min_eur": "86348", "amount_max_eur": "86348", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP FLIP from loss (was -181888)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p7 native; YE2024 -181888; 62 7766691 FLAT; 630 752857 DROP; 66A 39741 JUMP; 640/8 13386 DROP; 635/9 empty; 631/4 -15142 FLIP"},
    {"budget_id": "bud_consolata_zaventem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7528775", "amount_min_eur": "7528775", "amount_max_eur": "7528775", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -4.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p6 native; YE2024 7882414; overgedragen 14 806413 DROP; bestemde 13 300000 FLAT; kapitaalsubsidies 15 5686964 DROP; fondsen 10 735398 FLAT"},
    {"budget_id": "bud_consolata_zaventem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "20506369", "amount_min_eur": "20506369", "amount_max_eur": "20506369", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.86%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p5 native; YE2024 21553767; MVA 22/27 15817185 DROP; cash 800197 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 66238"},
    {"budget_id": "bud_consolata_zaventem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12977594", "amount_min_eur": "12977594", "amount_max_eur": "12977594", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -5.07%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p6 native; YE2024 13671353; 17 10175436 DROP; 42/48 2795664 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 6494"},
    {"budget_id": "bud_consolata_zaventem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "800197", "amount_min_eur": "800197", "amount_max_eur": "800197", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +6.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p5 native; YE2024 752033; geldbeleggingen 50/53 empty; combined liquidity 800197 JUMP vs prior 752033; capex 66238"},
    {"budget_id": "bud_consolata_zaventem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2530; PDF p9 native; YE2024 691 empty; 791 empty; 9905 -109012 JUMP; overgedragen 14 806413 DROP; bestemde 13 300000 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
