from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2540_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_mvc_diest_jr2025_nbb_pdf_2540"
EID = "vzw_martine_van_camp_diest"

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
    "name_nl": "Martine Van Camp (VAPH woon- en dagondersteuning)",
    "name_fr": "ASBL Martine Van Camp (VAPH)",
    "name_en": "Martine Van Camp Diest VZW (leftover city_diest leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_diest",
    "community_language": "nl",
    "website": "https://www.martinevancamp.be/",
    "foi_email": "info@martinevancamp.be",
    "foi_postal": "Turnhoutsebaan 57 3294 Diest",
    "notes": "tick2540 YE2025 Strong official native NBB PDF deposit 2026-00289013 + Strong KBO 0424.784.378 Actief 1 VE; omzet70 JUMP 1675451 commercial-only vs large 73; 73 JUMP 10986567; 76A DROP 8314; envelope 70/76A JUMP 12918434; pnl DROP 758488; 9901 DROP 708808; equity JUMP 9853159; assets JUMP 17282003; debt JUMP 7318178; FTE JUMP 134.5; kapitaalsubsidies DROP 2816870; destin691 DROP 750000; cash JUMP 1240159; geldbeleggingen DROP 3513855; aanbouw JUMP 736412; capex 1228548; 1 VE leftover city_diest leftover VAPH leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_diest leftover VAPH; NOT leftover-via-VE; leftover WZC Annendael remine@2535 leftover hospital same KBO leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_aalter leftover VAPH Aalternatief 0 deposits SKIP leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover VAPH unused-looking leftover WZC unused-not-hardskip 0 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only; NOT Armonea commercial; NOT Korian commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_mvc_diest_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1675451", "amount_min_eur": "1675451", "amount_max_eur": "1675451", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +7.09% (commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p7 native; YE2024 1564555 identical; 73 10986567 JUMP; envelope 70/76A 12918434 JUMP; FOI VAPH matrix behind 12918434"},
    {"budget_id": "bud_mvc_diest_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "10986567", "amount_min_eur": "10986567", "amount_max_eur": "10986567", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +6.75%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p7 native; YE2024 10292011 identical; 733 10942562 JUMP; 73-733 gap 44005 FOI; 76A 8314 DROP"},
    {"budget_id": "bud_mvc_diest_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "12918434", "amount_min_eur": "12918434", "amount_max_eur": "12918434", "basis": "NBB VOL-VZW envelope 70/76A YE2025 JUMP +6.28% (VZW because 70 present and commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p7 native; YE2024 12155345 identical; 70 1675451 JUMP; 73 10986567 JUMP; 76A 8314 DROP"},
    {"budget_id": "bud_mvc_diest_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8314", "amount_min_eur": "8314", "amount_max_eur": "8314", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -46.83%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p7 native; YE2024 15638 identical; 66A 5370 JUMP; 74 248102 DROP"},
    {"budget_id": "bud_mvc_diest_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "758488", "amount_min_eur": "758488", "amount_max_eur": "758488", "basis": "NBB VOL-VZW code 9904 winst (verlies) van het boekjaar YE2025 DROP -2.18%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p8 native; YE2024 775362 identical; 9901 708808 DROP; destin691 750000 DROP"},
    {"budget_id": "bud_mvc_diest_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "708808", "amount_min_eur": "708808", "amount_max_eur": "708808", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -2.65%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p7 native; YE2024 728103 identical; 62 10086622 JUMP; 630 641882 JUMP; 66A 5370 JUMP; 640/8 103959 DROP; 635/9 110666 JUMP; 631/4 empty"},
    {"budget_id": "bud_mvc_diest_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9853159", "amount_min_eur": "9853159", "amount_max_eur": "9853159", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +6.38%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p5 native; YE2024 9262601 identical; overgedragen 14 1627248 JUMP; bestemde 13 3947039 JUMP; kapitaalsubsidies 15 2816870 DROP; fondsen 10 1462002"},
    {"budget_id": "bud_mvc_diest_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "17282003", "amount_min_eur": "17282003", "amount_max_eur": "17282003", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +4.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p5 native; YE2024 16484910 identical; MVA 22/27 10100453 JUMP; cash 1240159 JUMP; geldbeleggingen 3513855 DROP; aanbouw 27 736412 JUMP; capex 1228548"},
    {"budget_id": "bud_mvc_diest_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7318178", "amount_min_eur": "7318178", "amount_max_eur": "7318178", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +1.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p5 native; YE2024 7222309 identical; 17 3641720 DROP; voorzieningen 16 110666 JUMP; 635/9 110666 JUMP"},
    {"budget_id": "bud_mvc_diest_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1240159", "amount_min_eur": "1240159", "amount_max_eur": "1240159", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +66.39%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF p5 native; YE2024 745316 identical; geldbeleggingen 50/53 3513855 DROP; combined liquidity 4754014 DROP; capex 1228548"},
    {"budget_id": "bud_mvc_diest_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "134.5", "amount_min_eur": "134.5", "amount_max_eur": "134.5", "basis": "NBB VOL-VZW code 9087 FTE YE2025 JUMP +1.20%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2540; PDF native; YE2024 132.9 identical; 1003 134.5; 105 YE 142.2; 9086 YE 171; 62 10086622 JUMP; destin691 750000 DROP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
