from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2532_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_seniorplaza_willebroek_jr2025_nbb_pdf_2532"
EID = "vzw_seniorplaza_willebroek"

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
    "name_nl": "Seniorplaza (WZC Seniorplaza)",
    "name_fr": "ASBL Seniorplaza (MRS Seniorplaza)",
    "name_en": "Seniorplaza VZW (leftover city_willebroek leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_willebroek",
    "community_language": "nl",
    "website": "https://www.korian.be/woonzorgcentra/seniorplaza/woonzorgcentrum-seniorplaza/",
    "foi_email": "info@seniorplaza.be",
    "foi_postal": "Overwinningsstraat 133-135 2830 Willebroek",
    "notes": "tick2532 YE2025 Strong official native NBB PDF deposit 2026-00336704 + Strong KBO 0467.255.829 Actief 2 VE; omzet70 JUMP 5279368 not commercial-only vs 73; 73 JUMP 662411; 76A empty; envelope omzet70 JUMP 5279368; pnl DROP -242696; 9901 DROP -132181; equity DROP 2106622; assets DROP 6456829; debt DROP 4350207; FTE JUMP 64.2; kapitaalsubsidies DROP 2330927; destin691 empty; cash JUMP 568577; leftover city_willebroek leftover WZC 2 VE official zetel Willebroek leftover-mined AGB-only unused leftover type; prior-year identical; Korian Belgium NV 0869.769.702 gedelegeerd bestuurder leftover public VZW WZC not commercial NV FIRST LOCK leftover city_willebroek leftover WZC; NOT leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_seniorplaza_willebroek_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5279368", "amount_min_eur": "5279368", "amount_max_eur": "5279368", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +3.39% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p6 native; YE2024 5106144; 73 662411 JUMP; envelope omzet70 5279368 JUMP; FOI RIZIV/Willebroek matrix behind 70 5279368"},
    {"budget_id": "bud_seniorplaza_willebroek_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "662411", "amount_min_eur": "662411", "amount_max_eur": "662411", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +9.18%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p6 native; YE2024 606694; 733 subsidies 662411 JUMP +9.18%; 73-733 gap 0; 70 5279368 JUMP; FOI WZC matrix behind 73 vs omzet70"},
    {"budget_id": "bud_seniorplaza_willebroek_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5279368", "amount_min_eur": "5279368", "amount_max_eur": "5279368", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +3.39% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p6 native; YE2024 5106144; 70 5279368 JUMP; 73 662411 JUMP; 76A empty; 70/76A 6015542 JUMP; 74 73763 DROP was 134028"},
    {"budget_id": "bud_seniorplaza_willebroek_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p6 native; YE2024 76A empty; 76B empty"},
    {"budget_id": "bud_seniorplaza_willebroek_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-242696", "amount_min_eur": "-242696", "amount_max_eur": "-242696", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 DROP (larger loss; was -186201)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p7 native; YE2024 -186201; 9901 DROP -132181 + 75 33103 - 65 136089 - 67/77 7529 = -242696; destin691 empty"},
    {"budget_id": "bud_seniorplaza_willebroek_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-132181", "amount_min_eur": "-132181", "amount_max_eur": "-132181", "basis": "NBB VOL-VZW code 9901 bedrijfsverlies YE2025 DROP (larger loss; was -57191)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p6 native; YE2024 -57191; 62 3855497 JUMP; 630 264906 JUMP; 66A empty DROP; 640/8 28385 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_seniorplaza_willebroek_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2106622", "amount_min_eur": "2106622", "amount_max_eur": "2106622", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -15.03%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p5 native; YE2024 2479262; overgedragen 14 -224305 DROP; bestemde 13 empty; kapitaalsubsidies 15 2330927 DROP; fondsen 10 empty"},
    {"budget_id": "bud_seniorplaza_willebroek_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6456829", "amount_min_eur": "6456829", "amount_max_eur": "6456829", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -7.62%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p4 native; YE2024 6989674; MVA 22/27 4719453 JUMP; cash 568577 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 314299"},
    {"budget_id": "bud_seniorplaza_willebroek_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4350207", "amount_min_eur": "4350207", "amount_max_eur": "4350207", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -3.55%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p5 native; YE2024 4510412; 17 2619649 DROP; 42/48 1724609 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 5948"},
    {"budget_id": "bud_seniorplaza_willebroek_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "568577", "amount_min_eur": "568577", "amount_max_eur": "568577", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +177.67%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p4 native; YE2024 204770; geldbeleggingen 50/53 empty; combined liquidity 568577 JUMP vs prior 204770; capex 314299"},
    {"budget_id": "bud_seniorplaza_willebroek_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2532; PDF p8 native; YE2024 691 empty; 791 empty; 9905 -242696 DROP; overgedragen 14 -224305 DROP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
