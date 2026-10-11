from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2533_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_sint_jozef_deinze_jr2025_nbb_pdf_2533"
EID = "vzw_sint_jozef_deinze"

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
    "name_nl": "R.V.T. Sint-Jozef Deinze (WZC Sint-Jozef)",
    "name_fr": "ASBL R.V.T. Sint-Jozef Deinze (MRS Sint-Jozef)",
    "name_en": "R.V.T. Sint-Jozef Deinze VZW (leftover city_deinze leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_deinze",
    "community_language": "nl",
    "website": "https://www.rvtsintjozef.be",
    "foi_email": "directie@rvtsintjozef.be",
    "foi_postal": "Kortrijksesteenweg 61 9800 Deinze",
    "notes": "tick2533 YE2025 Strong official native NBB PDF deposit 2026-00259876 + Strong KBO 0409.698.603 Actief 1 VE; omzet70 JUMP 9471817 not commercial-only vs 73; 73 DROP 1653070; 76A JUMP 11258; envelope omzet70 JUMP 9471817; pnl FLIP 511833; 9901 FLIP 293988; equity JUMP 8597413; assets DROP 13344074; debt DROP 4746661; FTE DROP 124; kapitaalsubsidies DROP 1589968; destin691 JUMP 4418723; cash JUMP 878637; 1 VE leftover city_deinze leftover WZC leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_deinze leftover WZC; NOT leftover VAPH Vierklaver remine@2496; NOT leftover VAPH Ten Dries remine@2499; NOT leftover-via-VE Evergem Franciscanessen 0451.818.080 SKIP; NOT leftover WZC Bejaardenzorg Zusters remine@2066; NOT leftover OCMW Karel Picque SKIP; NOT leftover Zorgbedrijf Ter Leenen SKIP; NOT leftover city_zonnebeke leftover WZC Sint-Jozef remine@2326; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_sint_jozef_deinze_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9471817", "amount_min_eur": "9471817", "amount_max_eur": "9471817", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +7.76% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p7 native; YE2024 8789823; 73 1653070 DROP; envelope omzet70 9471817 JUMP; FOI RIZIV/Deinze matrix behind 70 9471817"},
    {"budget_id": "bud_sint_jozef_deinze_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1653070", "amount_min_eur": "1653070", "amount_max_eur": "1653070", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -5.20%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p7 native; YE2024 1743738; 733 subsidies 1640291 DROP -5.24%; 73-733 gap 12779 = 731 schenkingen 12779; 70 9471817 JUMP; FOI WZC matrix behind 73 vs omzet70"},
    {"budget_id": "bud_sint_jozef_deinze_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9471817", "amount_min_eur": "9471817", "amount_max_eur": "9471817", "basis": "NBB VOL-VZW envelope omzet70 YE2025 JUMP +7.76% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p7 native; YE2024 8789823; 70 9471817 JUMP; 73 1653070 DROP; 76A 11258 JUMP; 70/76A 11372156 JUMP; 74 236011 JUMP"},
    {"budget_id": "bud_sint_jozef_deinze_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "11258", "amount_min_eur": "11258", "amount_max_eur": "11258", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (was empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p7 native; YE2024 76A empty; 76B empty"},
    {"budget_id": "bud_sint_jozef_deinze_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "511833", "amount_min_eur": "511833", "amount_max_eur": "511833", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP (was -411081)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p8 native; YE2024 -411081; 9901 FLIP 293988 + 75 322054 - 65 104209 = 511833; destin691 JUMP 4418723"},
    {"budget_id": "bud_sint_jozef_deinze_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "293988", "amount_min_eur": "293988", "amount_max_eur": "293988", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 FLIP (was -400552)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p7 native; YE2024 -400552; 62 8038951 DROP; 630 566368 DROP; 66A 6322; 640/8 43877 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_sint_jozef_deinze_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8597413", "amount_min_eur": "8597413", "amount_max_eur": "8597413", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +3.92%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p6 native; YE2024 8273197; overgedragen 14 71954 FLIP; bestemde 13 4418723 JUMP; kapitaalsubsidies 15 1589968 DROP; fondsen 10 2516768"},
    {"budget_id": "bud_sint_jozef_deinze_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "13344074", "amount_min_eur": "13344074", "amount_max_eur": "13344074", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -0.75%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p5 native; YE2024 13444371; MVA 22/27 8156555 DROP; cash 878637 JUMP; geldbeleggingen 1887538 JUMP; aanbouw 27 10890; capex 90307"},
    {"budget_id": "bud_sint_jozef_deinze_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4746661", "amount_min_eur": "4746661", "amount_max_eur": "4746661", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -8.21%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p6 native; YE2024 5171174; 17 2671661 DROP; 42/48 2018387 JUMP; 178/9 282222; voorzieningen 16 empty; overlopende 492/3 56613"},
    {"budget_id": "bud_sint_jozef_deinze_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "878637", "amount_min_eur": "878637", "amount_max_eur": "878637", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +39.74%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p5 native; YE2024 628747; geldbeleggingen 50/53 1887538 JUMP; combined liquidity 2766175 JUMP vs prior 2312333; capex 90307"},
    {"budget_id": "bud_sint_jozef_deinze_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4418723", "amount_min_eur": "4418723", "amount_max_eur": "4418723", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2533; PDF p9 native; YE2024 691 empty; 791 4018723 JUMP (was empty); 9905 511833 FLIP; overgedragen 14 71954 FLIP; bestemde 13 4418723 JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
