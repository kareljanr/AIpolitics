from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2526_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_wzga_arendonk_jr2025_nbb_pdf_2526"
EID = "vzw_wzga_arendonk"

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
    "name_nl": "WoonZorgGroep Arendonk (WZGA)",
    "name_fr": "ASBL WoonZorgGroep Arendonk (WZGA)",
    "name_en": "WoonZorgGroep Arendonk VZW (leftover city_arendonk leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_arendonk",
    "community_language": "nl",
    "website": "https://wzga.be/",
    "foi_email": "info@wzga.be",
    "foi_postal": "Vrijheid 100 2370 Arendonk",
    "notes": "tick2526 YE2025 Strong official native NBB PDF deposit 2026-00239172 + Strong KBO 0696.665.975 Actief 2 VE; omzet70 JUMP 9984424 not commercial-only vs 73; 73 JUMP 2447880; 76A JUMP 1; envelope omzet70 JUMP 9984424; 70/76A JUMP 12676553; pnl JUMP 631859; 9901 JUMP 621238; equity JUMP 718945; assets JUMP 3576196; debt DROP 2857251; FTE JUMP 139.1; kapitaalsubsidies empty; destin691 empty; cash JUMP 1391879; geldbeleggingen empty; leftover city_arendonk leftover WZC 2 VE official zetel Arendonk leftover-mined AGB-only unused leftover type; prior-year identical; NOT leftover city_wingene leftover WZC Het Laar remine@2525; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_meerhout leftover maatwerk DE SPRONG remine@2286; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_wzga_arendonk_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9984424", "amount_min_eur": "9984424", "amount_max_eur": "9984424", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +9.64% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p7 native; YE2024 9106668; 73 2447880 JUMP; envelope omzet70 9984424 JUMP; FOI Departement Zorg/RIZIV/Arendonk matrix behind omzet 9984424"},
    {"budget_id": "bud_wzga_arendonk_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2447880", "amount_min_eur": "2447880", "amount_max_eur": "2447880", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.78%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p7 native; YE2024 2336242; 733 subsidies 2447880; FOI Departement Zorg/RIZIV matrix behind 73 JUMP vs omzet JUMP"},
    {"budget_id": "bud_wzga_arendonk_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9984424", "amount_min_eur": "9984424", "amount_max_eur": "9984424", "basis": "NBB VOL-VZW envelope omzet 70 YE2025 JUMP +9.64% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p7 native; YE2024 9106668; 70/76A bedrijfsopbrengsten 12676553 JUMP; 73 2447880; 76A 1 JUMP; 74 244248 JUMP"},
    {"budget_id": "bud_wzga_arendonk_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1", "amount_min_eur": "1", "amount_max_eur": "1", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP from empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p7 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_wzga_arendonk_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "631859", "amount_min_eur": "631859", "amount_max_eur": "631859", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +1017.56% (was 56539)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p8 native; YE2024 56539; 9901 621238 + 75 11226 - 65 605 = 631859; destin691 empty"},
    {"budget_id": "bud_wzga_arendonk_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "621238", "amount_min_eur": "621238", "amount_max_eur": "621238", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +1303.39% (was 44267)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p7 native; YE2024 44267; 62 9322064 JUMP; 630 167681 DROP; 66A empty; 640/8 23781 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_wzga_arendonk_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "718945", "amount_min_eur": "718945", "amount_max_eur": "718945", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +725.55%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p6 native; YE2024 87087; overgedragen 14 181732 JUMP from -450127; bestemde 13 empty; kapitaalsubsidies 15 empty; fondsen 10 537213 FLAT"},
    {"budget_id": "bud_wzga_arendonk_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3576196", "amount_min_eur": "3576196", "amount_max_eur": "3576196", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +6.27%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p5 native; YE2024 3365232; MVA 22/27 677890 DROP; cash 1391879 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 35766"},
    {"budget_id": "bud_wzga_arendonk_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2857251", "amount_min_eur": "2857251", "amount_max_eur": "2857251", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -12.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p6 native; YE2024 3278145; 17 empty; 42/48 2846515 DROP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 10736 DROP"},
    {"budget_id": "bud_wzga_arendonk_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1391879", "amount_min_eur": "1391879", "amount_max_eur": "1391879", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +7.95%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p5 native; YE2024 1289324; geldbeleggingen 50/53 empty; combined liquidity 1391879 JUMP vs prior 1289324; capex 35766"},
    {"budget_id": "bud_wzga_arendonk_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2526; PDF p9 native; YE2024 691 empty; 791 empty; 9905 631859 JUMP; overgedragen 14 181732 JUMP from -450127; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1B DONE")
