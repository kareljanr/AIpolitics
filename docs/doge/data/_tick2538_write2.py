from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2538_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_sbm_maasmechelen_jr2025_nbb_pdf_2538"
EID = "vzw_sbm_maasmechelen"

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
    "name_nl": "Sociaal Bedrijvencentrum Maasmechelen (SBM / maatwerk)",
    "name_fr": "ASBL Sociaal Bedrijvencentrum Maasmechelen (SBM)",
    "name_en": "SBM Maasmechelen VZW (leftover city_maasmechelen leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_maasmechelen",
    "community_language": "nl",
    "website": "https://www.vzwsbm.be/",
    "foi_email": "info@sociaalbedrijvencentrum.be",
    "foi_postal": "Boorsemstraat 2 3630 Maasmechelen",
    "notes": "tick2538 YE2025 Strong official native NBB PDF deposit 2026-00154620 + Strong KBO 0461.814.525 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 DROP 2414981; pnl DROP 141998; 9901 DROP 142905; equity JUMP 3146562; assets JUMP 3853791; debt JUMP 646153; FTE JUMP 49.1; kapitaalsubsidies JUMP 1035604; destin691 JUMP 108486; cash JUMP 1761744; geldbeleggingen empty; aanbouw empty; capex 290871; leasing JUMP 219464; 1 VE leftover city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type; prior-year identical; FIRST LOCK leftover city_maasmechelen leftover maatwerk; NOT leftover-via-VE of a DIFFERENT leftover city; leftover maatwerk Kringwinkel Maasland remine@2223 parent sec_flanders leftover maatwerk MAASBIJ YE2024 leftover WZC Heyvis OCMW leftover WZC Maasmeander BV commercial leftover WZC unused-not-hardskip 0 leftover VAPH unused-looking leftover CIK HARD SKIP leftover maatwerk type now taken; NOT Armonea commercial; NOT Vulpia commercial; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_sbm_maasmechelen_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 70 empty; 73 empty; envelope bruto9900 2414981 DROP; FOI WSE/maatwerk matrix behind 2414981"},
    {"budget_id": "bud_sbm_maasmechelen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 73 empty; 76A empty; envelope bruto9900 2414981 DROP"},
    {"budget_id": "bud_sbm_maasmechelen_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2414981", "amount_min_eur": "2414981", "amount_max_eur": "2414981", "basis": "NBB VKT-VZW envelope bruto9900 YE2025 DROP -3.17% (VKT because 73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 2493955 identical; 70 empty; 73 empty; 76A empty; 74 empty"},
    {"budget_id": "bud_sbm_maasmechelen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 76A empty; 66A empty"},
    {"budget_id": "bud_sbm_maasmechelen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "141998", "amount_min_eur": "141998", "amount_max_eur": "141998", "basis": "NBB VKT-VZW code 9904 winst (verlies) van het boekjaar YE2025 DROP -62.28%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 376408 identical; 9901 142905 DROP; destin691 108486 JUMP"},
    {"budget_id": "bud_sbm_maasmechelen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "142905", "amount_min_eur": "142905", "amount_max_eur": "142905", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -62.36%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p7 native; YE2024 379662 identical; 62 2073468 JUMP; 630 189163 JUMP; 66A empty; 640/8 9446 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_sbm_maasmechelen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3146562", "amount_min_eur": "3146562", "amount_max_eur": "3146562", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +9.96%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p6 native; YE2024 2861618 identical; overgedragen 14 621380 JUMP; bestemde 13 1489578 JUMP; kapitaalsubsidies 15 1035604 JUMP; fondsen 10 empty"},
    {"budget_id": "bud_sbm_maasmechelen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3853791", "amount_min_eur": "3853791", "amount_max_eur": "3853791", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +13.44%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p5 native; YE2024 3397278 identical; MVA 22/27 1495095 JUMP; cash 1761744 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 290871; leasing 25 219464 JUMP"},
    {"budget_id": "bud_sbm_maasmechelen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "646153", "amount_min_eur": "646153", "amount_max_eur": "646153", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +36.15%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p6 native; YE2024 474584 identical; 17 261974 JUMP; 42/48 379229 JUMP; voorzieningen 16 61076; overlopende 492/3 4950"},
    {"budget_id": "bud_sbm_maasmechelen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1761744", "amount_min_eur": "1761744", "amount_max_eur": "1761744", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +16.49%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p5 native; YE2024 1512332 identical; geldbeleggingen 50/53 empty; combined liquidity 1761744 JUMP; capex 290871"},
    {"budget_id": "bud_sbm_maasmechelen_fte_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "49.1", "amount_min_eur": "49.1", "amount_max_eur": "49.1", "basis": "NBB VKT-VZW code 100 FTE YE2025 JUMP +5.36%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2538; PDF p15 native; YE2024 46.6 identical; 105 YE 51.4; 62 2073468 JUMP; destin691 108486 JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
