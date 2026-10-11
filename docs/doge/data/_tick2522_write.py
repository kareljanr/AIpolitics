from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2522_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_cuypers_stabroek_jr2025_nbb_pdf_2522"
SRC_KBO = "src_cuypers_stabroek_kbo_2522"
SRC_SBM = "src_cuypers_stabroek_sbm_2522"
SRC_SITE = "src_cuypers_stabroek_site_2522"
EID = "vzw_cuypers_stabroek"
GAP = "gap_cuypers_stabroek_wzc_matrix_omzet_6_27m_73_drop_1_16m_pnl_drop_102k_cash_drop_49k_l5"
assert (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_rows(path, rows, fieldnames):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} no LF")
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", lineterminator="\n")
        for row in rows:
            w.writerow(row)
    print("appended", len(rows), "->", path.name)

csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in csv.DictReader(_fh):
        blob = " ".join(_row.values())
        if _row.get("entity_id") == EID or "0408.704.847" in blob or "0408704847" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Aalmoezenier Cuypers Stabroek deposit 2026-00325553",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00325553.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2522; official native statutory PDF 1360776 bytes 54p VOL-VZW 26.0.15 m05-f; header 23/07/2026; AV 09.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-24 08:29:21 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00325553 GET 200 1360776 MD5 214c5ba875b25f3f1db28303e81b9a64; NBB UUID 29e01bbd-8698-11f1-84dc-b771d53d7359; NBB broker PDF GET 200 1360776 same MD5; NBB published-deposits list 500 this tick; NBB consult list OK; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.16 6.18 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Vrienden van Aalmoezenier Cuypers 0408.704.847",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408704847",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2522; Actief since 15.01.1970; 1 VE leftover city_stabroek (official zetel Torense Weg 1 2940 Stabroek since 15.12.2005; VE 2.154.459.476 Woon en zorgcentrum aalmoezenier cuypers vzw Torense Weg 1 since 14.06.2006); VZW since 15.01.1970; naam De Vrienden van Aalmoezenier Cuypers since 12.06.2026; RSZ-werkgever since 01.01.1970; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official Vlaanderen WZC list CoBRHA HCO 3157 dossier 166.101 87 woongelegenheden WZC Aalmoezenier Cuypers; leftover mined city_stabroek leftover WZC leftover-mined AGB-only; NOT leftover WZC Villa ter Molen Vulpia 0521.970.559; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover city_meerhout leftover VAPH t Volderke 0432.224.080 SCAN; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Aalmoezenier Cuypers 0408704847 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0408704847",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2522; deposit-id 2026-00325553 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial neerlegging 23.07.2026; NBB UUID 29e01bbd-8698-11f1-84dc-b771d53d7359; NBB consult list OK; NBB published-deposits list 500 this tick; CDN+broker PDF used for euros; ZIP/XBRL not used for euros; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Aalmoezenier Cuypers FOI contact leftover city_stabroek leftover WZC",
        "url": "https://aalmoezeniercuyperswzc.be/",
        "publisher": "De Vrienden van Aalmoezenier Cuypers VZW leftover city_stabroek leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2522; FOI info@wzcac.be from official site https://aalmoezeniercuyperswzc.be/ + Sociale Kaart; leftover mined city_stabroek leftover WZC after leftover city_wichelen leftover VAPH/CAR/maatwerk none local + leftover city_lebbeke leftover VAPH/CAR/maatwerk none local + leftover city_meerhout leftover VAPH t Volderke 0432.224.080 SCAN SKIP; leftover WZC Villa ter Molen Vulpia SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Aalmoezenier Cuypers (De Vrienden van Aalmoezenier Cuypers)",
    "name_fr": "ASBL Les Amis de l aumonier Cuypers (MRS Aalmoezenier Cuypers)",
    "name_en": "Aalmoezenier Cuypers VZW (leftover city_stabroek leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_stabroek",
    "community_language": "nl",
    "website": "https://aalmoezeniercuyperswzc.be/",
    "foi_email": "info@wzcac.be",
    "foi_postal": "Torense Weg 1 2940 Stabroek",
    "notes": "tick2522 YE2025 Strong official native NBB PDF deposit 2026-00325553 + Strong KBO 0408.704.847 Actief 1 VE; omzet70 JUMP 6273758 not commercial-only; 73 DROP 1161030; 76A DROP 8890; envelope omzet70 JUMP 6273758; pnl DROP -101734; 9901 DROP 148842; equity DROP 2629512; assets DROP 9598296; debt DROP 6878783; FTE JUMP 75.9; kapitaalsubsidies DROP 1070581; destin691 empty; cash DROP 49222; geldbeleggingen FLAT 704504; leftover city_stabroek leftover WZC 1 VE official zetel Stabroek leftover-mined AGB-only; prior-year identical; NOT leftover WZC Villa ter Molen Vulpia; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover city_meerhout leftover VAPH t Volderke SCAN; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_cuypers_stabroek_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6273758", "amount_min_eur": "6273758", "amount_max_eur": "6273758", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +8.27% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p6 native; YE2024 5794361; 73 1161030 DROP; envelope omzet70 6273758 JUMP; FOI Departement Zorg/RIZIV/Stabroek matrix behind omzet 6273758"},
    {"budget_id": "bud_cuypers_stabroek_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1161030", "amount_min_eur": "1161030", "amount_max_eur": "1161030", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -14.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p6 native; YE2024 1352069; 733 subsidies 1160830 DROP was 1351919; FOI Departement Zorg/RIZIV matrix behind 73 DROP vs omzet JUMP"},
    {"budget_id": "bud_cuypers_stabroek_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6273758", "amount_min_eur": "6273758", "amount_max_eur": "6273758", "basis": "NBB VOL-VZW envelope omzet 70 YE2025 JUMP +8.27% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p6 native; YE2024 5794361; 70/76A bedrijfsopbrengsten 7568448 JUMP; 73 1161030; 76A 8890; 74 124770"},
    {"budget_id": "bud_cuypers_stabroek_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8890", "amount_min_eur": "8890", "amount_max_eur": "8890", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -62.94%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p6 native; YE2024 23991; 76B empty"},
    {"budget_id": "bud_cuypers_stabroek_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-101734", "amount_min_eur": "-101734", "amount_max_eur": "-101734", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 DROP deeper loss (was -45907)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p7 native; YE2024 -45907; 9901 148842 + 75 1925 - 65 252277 - 67/77 224 = -101734; destin691 empty"},
    {"budget_id": "bud_cuypers_stabroek_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "148842", "amount_min_eur": "148842", "amount_max_eur": "148842", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -26.39% (was 202203)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p6 native; YE2024 202203; 62 5346431 JUMP; 630 641878 DROP; 66A 75487 JUMP; 640/8 4323 DROP; 635/9 -1000; 631/4 empty"},
    {"budget_id": "bud_cuypers_stabroek_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2629512", "amount_min_eur": "2629512", "amount_max_eur": "2629512", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -6.99%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p5 native; YE2024 2827230; overgedragen 14 -35581 DROP; bestemde 13 701028 FLAT; kapitaalsubsidies 15 1070581 DROP; fondsen 10 893485 FLAT"},
    {"budget_id": "bud_cuypers_stabroek_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9598296", "amount_min_eur": "9598296", "amount_max_eur": "9598296", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -5.17%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p3 native; YE2024 10121337; MVA 22/27 8041369 DROP; cash 49222 DROP; geldbeleggingen 704504 FLAT; aanbouw empty; capex 71328"},
    {"budget_id": "bud_cuypers_stabroek_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6878783", "amount_min_eur": "6878783", "amount_max_eur": "6878783", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -4.50%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p5 native; YE2024 7203107; 17 5257621 DROP; 42/48 1614231 JUMP; 178/9 empty; voorzieningen 16 90000 DROP; overlopende 492/3 6931 DROP"},
    {"budget_id": "bud_cuypers_stabroek_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "49222", "amount_min_eur": "49222", "amount_max_eur": "49222", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -43.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p3 native; YE2024 86556; geldbeleggingen 50/53 704504 FLAT; combined liquidity 753726 DROP vs prior 791060; capex 71328"},
    {"budget_id": "bud_cuypers_stabroek_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2522; PDF p8 native; YE2024 691 empty; 791 empty; 9905 -101734 DROP; overgedragen 14 -35581 DROP; bestemde 13 701028 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
