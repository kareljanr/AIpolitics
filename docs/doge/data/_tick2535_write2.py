from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2535_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_annendael_diest_jr2025_nbb_pdf_2535"
EID = "vzw_annendael_diest"

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
    "name_nl": "Zorggroep Annendael (WZC Huis August / Huis Sterre)",
    "name_fr": "ASBL Zorggroep Annendael (MRS)",
    "name_en": "Zorggroep Annendael VZW (leftover city_diest leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_diest",
    "community_language": "nl",
    "website": "https://annendael.be/",
    "foi_email": "info@annendael.be",
    "foi_postal": "Vestenstraat 1 3290 Diest",
    "notes": "tick2535 YE2025 Strong official native NBB PDF deposit 2026-00283395 + Strong KBO 0414.604.526 Actief 4 VE; omzet70 JUMP 36063571; 73 JUMP 5994527; 76A JUMP 853984; envelope omzet70 JUMP 36063571; pnl FLIP -451172; 9901 DROP 808373; equity DROP 42367160; assets DROP 97618819; debt DROP 51863562; FTE JUMP 398.9; kapitaalsubsidies DROP 12754931; destin691 JUMP 3211567; cash DROP 8929733; 4 VE leftover city_diest leftover WZC leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_diest leftover WZC; NOT leftover-via-VE of a DIFFERENT leftover city; leftover city_scherpenheuvel_zichem leftover Huis Sterre same KBO leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_annendael_diest_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "36063571", "amount_min_eur": "36063571", "amount_max_eur": "36063571", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +3.52% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p7 native; YE2024 70 34835893; 73 5994527 JUMP; envelope omzet70 36063571 JUMP; FOI RIZIV/Diest matrix behind 36063571"},
    {"budget_id": "bud_annendael_diest_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5994527", "amount_min_eur": "5994527", "amount_max_eur": "5994527", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.05%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p7 native; YE2024 73 5706424; 733 5994527 JUMP; 73-733 gap 0; 70 36063571 JUMP"},
    {"budget_id": "bud_annendael_diest_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "36063571", "amount_min_eur": "36063571", "amount_max_eur": "36063571", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +3.52% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p7 native; YE2024 34835893; 70 36063571; 73 5994527; 76A 853984 JUMP; 70/76A 44673288 JUMP +4.60%; 74 1761206 JUMP"},
    {"budget_id": "bud_annendael_diest_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "853984", "amount_min_eur": "853984", "amount_max_eur": "853984", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +68.43%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p7 native; YE2024 76A 507155; 66A 158602 DROP"},
    {"budget_id": "bud_annendael_diest_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-451172", "amount_min_eur": "-451172", "amount_max_eur": "-451172", "basis": "NBB VOL-VZW code 9904 winst (verlies) van het boekjaar YE2025 FLIP LOSS", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p8 native; YE2024 1554771; 9901 808373 DROP; destin691 3211567 JUMP"},
    {"budget_id": "bud_annendael_diest_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "808373", "amount_min_eur": "808373", "amount_max_eur": "808373", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -63.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p7 native; YE2024 2235596; 62 29570212 JUMP; 630 3615625 JUMP; 66A 158602 DROP; 640/8 68883 DROP; 635/9 -769795; 631/4 40405 JUMP"},
    {"budget_id": "bud_annendael_diest_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "42367160", "amount_min_eur": "42367160", "amount_max_eur": "42367160", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -1.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p6 native; YE2024 43116949; overgedragen 14 7598432 DROP; bestemde 13 16915256 JUMP; kapitaalsubsidies 15 12754931 DROP; fondsen 10 5098540"},
    {"budget_id": "bud_annendael_diest_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "97618819", "amount_min_eur": "97618819", "amount_max_eur": "97618819", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -9.01%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p5 native; YE2024 107283804; MVA 22/27 69105962 DROP; cash 8929733 DROP; geldbeleggingen 3292665 JUMP; aanbouw 27 171357 DROP; capex 2781746"},
    {"budget_id": "bud_annendael_diest_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "51863562", "amount_min_eur": "51863562", "amount_max_eur": "51863562", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -12.61%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p6 native; YE2024 59348141; 17 37684864 DROP; 42/48 12637201 DROP; voorzieningen 16 3388097 DROP; overlopende 492/3 1541497"},
    {"budget_id": "bud_annendael_diest_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8929733", "amount_min_eur": "8929733", "amount_max_eur": "8929733", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -46.58%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF p5 native; YE2024 16716549; geldbeleggingen 50/53 3292665 JUMP; combined liquidity 12222398 DROP vs prior 19893813; capex 2781746"},
    {"budget_id": "bud_annendael_diest_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "398.9", "amount_min_eur": "398.9", "amount_max_eur": "398.9", "basis": "NBB VOL-VZW code 9087 FTE YE2025 JUMP +1.71%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2535; PDF native; YE2024 392.2; 1003 395.5; 9086 561 koppen was 581; 62 29570212 JUMP; destin691 3211567 JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
