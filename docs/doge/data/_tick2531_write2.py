from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2531_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_capenberg_boechout_jr2025_nbb_pdf_2531"
EID = "vzw_capenberg_boechout"

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
    "name_nl": "Capenberg, Oxaco-Center (WZC Huize Stracke)",
    "name_fr": "ASBL Capenberg Oxaco-Center (MRS Huize Stracke)",
    "name_en": "Capenberg Oxaco-Center VZW (leftover city_boechout leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_boechout",
    "community_language": "nl",
    "website": "https://www.capenberg.com/",
    "foi_email": "m.roggen@capenberg.com",
    "foi_postal": "Borsbeeksesteenweg 45 2530 Boechout",
    "notes": "tick2531 YE2025 Strong official native NBB PDF deposit 2026-00166949 + Strong KBO 0408.159.370 Actief 1 VE; omzet70 DROP 6320109 not commercial-only vs 73; 73 JUMP 1387170; 76A empty; envelope omzet70 DROP 6320109; pnl JUMP -398270; 9901 JUMP -199500; equity DROP 3643724; assets DROP 14261777; debt DROP 10618053; FTE DROP 83.4; kapitaalsubsidies empty; destin691 empty; cash DROP 553009; leftover city_boechout leftover WZC 1 VE official zetel Boechout leftover-mined AGB-only unused leftover type; prior-year identical; NOT leftover WZC Avondvrede NV 0446.506.836 remine@2166 SKIP; NOT leftover WZC Sint-Mathildis De Medemens 0428.692.191 leftover-via-VE Antwerpen remine@2086 SKIP; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_capenberg_boechout_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6320109", "amount_min_eur": "6320109", "amount_max_eur": "6320109", "basis": "NBB VOL-VZW code 70 omzet YE2025 DROP -0.84% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p6 native; YE2024 6373547; 73 1387170 JUMP; envelope omzet70 6320109 DROP; FOI RIZIV/Boechout matrix behind 70 6320109"},
    {"budget_id": "bud_capenberg_boechout_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1387170", "amount_min_eur": "1387170", "amount_max_eur": "1387170", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +24.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p6 native; YE2024 1110585; 733 subsidies 1157024 JUMP +4.18%; 73-733 gap 230146 FOI; 70 6320109 DROP; FOI WZC matrix behind 73 vs omzet70"},
    {"budget_id": "bud_capenberg_boechout_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6320109", "amount_min_eur": "6320109", "amount_max_eur": "6320109", "basis": "NBB VOL-VZW envelope omzet70 YE2025 DROP -0.84% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p6 native; YE2024 6373547; 70 6320109 DROP; 73 1387170 JUMP; 76A empty; 70/76A 7707279 DROP; 74 empty DROP was 235480"},
    {"budget_id": "bud_capenberg_boechout_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p6 native; YE2024 76A empty; 76B empty"},
    {"budget_id": "bud_capenberg_boechout_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-398270", "amount_min_eur": "-398270", "amount_max_eur": "-398270", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 JUMP (smaller loss; was -428160)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p7 native; YE2024 -428160; 9901 JUMP -199500 + 75 278 - 65 199048 = -398270; destin691 empty"},
    {"budget_id": "bud_capenberg_boechout_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-199500", "amount_min_eur": "-199500", "amount_max_eur": "-199500", "basis": "NBB VOL-VZW code 9901 bedrijfsverlies YE2025 JUMP (smaller loss; was -252208)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p6 native; YE2024 -252208; 62 5687192 JUMP; 630 641644 DROP; 66A empty DROP; 640/8 15609 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_capenberg_boechout_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3643724", "amount_min_eur": "3643724", "amount_max_eur": "3643724", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -9.85%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p5 native; YE2024 4041994; overgedragen 14 -336777 DROP; bestemde 13 empty; kapitaalsubsidies 15 empty; fondsen 10 3980501 FLAT"},
    {"budget_id": "bud_capenberg_boechout_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14261777", "amount_min_eur": "14261777", "amount_max_eur": "14261777", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -4.92%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p4 native; YE2024 14999008; MVA 22/27 12749773 DROP; cash 553009 DROP; geldbeleggingen empty DROP was 46619; aanbouw 27 empty; capex 12905"},
    {"budget_id": "bud_capenberg_boechout_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "10618053", "amount_min_eur": "10618053", "amount_max_eur": "10618053", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -3.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p5 native; YE2024 10957014; 17 8550240 DROP; 42/48 1771875 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 295938"},
    {"budget_id": "bud_capenberg_boechout_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "553009", "amount_min_eur": "553009", "amount_max_eur": "553009", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -28.30%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p4 native; YE2024 771244; geldbeleggingen 50/53 empty DROP was 46619; combined liquidity 553009 DROP vs prior 817863; capex 12905"},
    {"budget_id": "bud_capenberg_boechout_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2531; PDF p8 native; YE2024 691 empty; 791 empty; 9905 -398270 JUMP; overgedragen 14 -336777 DROP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
