from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2523_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sint_bernardus_bertem_jr2025_nbb_pdf_2523"
SRC_KBO = "src_sint_bernardus_bertem_kbo_2523"
SRC_SBM = "src_sint_bernardus_bertem_sbm_2523"
SRC_SITE = "src_sint_bernardus_bertem_site_2523"
EID = "vzw_sint_bernardus_bertem"
GAP = "gap_sint_bernardus_bertem_wzc_matrix_omzet_14_53m_73_drop_2_66m_pnl_flip_loss_284k_cash_drop_1_26m_l5"
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
        if _row.get("entity_id") == EID or "0435.723.406" in blob or "0435723406" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Sint-Bernardus Bertem deposit 2026-00268836",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00268836.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2523; official native statutory PDF 3487925 bytes 36p VOL-VZW 25.0.13 m05-f; header 08/07/2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-08 23:05:22 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00268836 GET 200 3487925 MD5 f0d34379f01444ac31b6612e105bbf11; NBB UUID 5e66e3a1-5292-11f1-9c8e-aba481ba3e59; NBB broker PDF GET 200 3487925 same MD5; NBB ids list 20 / nonmig-recent 2 this tick; NBB published-deposits 500 500 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.7 6.10 6.13 6.14 6.16 niet dienstig; Companyweb last-balansjaar 2025 discovery-only unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Woon en Zorgcentrum Sint-Bernardus Bertem 0435.723.406",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435723406",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2523; Actief since 27.06.1988; 2 VE leftover city_bertem (official zetel Egenhovenstraat 22 3060 Bertem since 15.07.1997; VE 2.150.163.267 Rust- en Verzorgingstehuis Sint-Bernardus te Bertem Egenhovenstraat 22 since 29.11.2005 + VE 2.360.271.504 Het Elfenbosje Egenhovenstraat 26 since 01.07.2024); VZW since 27.06.1988; naam Woon en Zorgcentrum Sint-Bernardus Bertem since 17.10.2005; RSZ-werkgever since 01.10.1993; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official Vlaanderen WZC list CoBRHA HCO 3638 dossier 207.101 201 woongelegenheden WZC Sint-Bernardus; leftover mined city_bertem leftover WZC leftover-mined AGB-only; NOT leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522; NOT leftover WZC Sint-Bernardus Assenede 0445.106.274 remine; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Sint-Bernardus Bertem 0435723406 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0435723406",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2523; deposit-id 2026-00268836 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial neerlegging 08.07.2026; NBB UUID 5e66e3a1-5292-11f1-9c8e-aba481ba3e59; NBB ids list 20 this tick; CDN+broker PDF used for euros; ZIP/XBRL not used for euros; Companyweb last-balansjaar 2025 discovery-only unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Sint-Bernardus Bertem FOI contact leftover city_bertem leftover WZC",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435723406",
        "publisher": "Woon en Zorgcentrum Sint-Bernardus Bertem VZW leftover city_bertem leftover WZC 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2523; FOI boekhouding@stbernardus.be from official NBB PDF identification; leftover mined city_bertem leftover WZC leftover-mined AGB-only after leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking leftover CIK fallback not taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Sint-Bernardus Bertem (Woon en Zorgcentrum Sint-Bernardus Bertem)",
    "name_fr": "ASBL Centre de soins Sint-Bernardus Bertem (MRS Sint-Bernardus)",
    "name_en": "Sint-Bernardus Bertem VZW (leftover city_bertem leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_bertem",
    "community_language": "nl",
    "website": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435723406",
    "foi_email": "boekhouding@stbernardus.be",
    "foi_postal": "Egenhovenstraat 22 3060 Bertem",
    "notes": "tick2523 YE2025 Strong official native NBB PDF deposit 2026-00268836 + Strong KBO 0435.723.406 Actief 2 VE; omzet70 DROP 14533086 not commercial-only; 73 DROP 2661412; 76A empty; envelope omzet70 DROP 14533086; pnl FLIP LOSS -283512; 9901 FLIP LOSS -254666; equity DROP 11925827; assets JUMP 17198350; debt JUMP 5272522; FTE DROP 189; kapitaalsubsidies DROP 31528; destin691 empty (was 1398444); cash DROP 1258185; geldbeleggingen JUMP 4237589; leftover city_bertem leftover WZC 2 VE official zetel Bertem leftover-mined AGB-only; prior-year identical; NOT leftover city_stabroek leftover WZC Aalmoezenier Cuypers remine@2522; NOT leftover WZC Sint-Bernardus Assenede remine; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_sint_bernardus_bertem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14533086", "amount_min_eur": "14533086", "amount_max_eur": "14533086", "basis": "NBB VOL-VZW code 70 omzet YE2025 DROP -1.11% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p7 native; YE2024 14696348; 73 2661412 DROP; envelope omzet70 14533086 DROP; FOI Departement Zorg/RIZIV/Bertem matrix behind omzet 14533086"},
    {"budget_id": "bud_sint_bernardus_bertem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2661412", "amount_min_eur": "2661412", "amount_max_eur": "2661412", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 DROP -21.66%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p7 native; YE2024 3397449; 733 subsidies empty; FOI Departement Zorg/RIZIV matrix behind 73 DROP vs omzet DROP"},
    {"budget_id": "bud_sint_bernardus_bertem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "14533086", "amount_min_eur": "14533086", "amount_max_eur": "14533086", "basis": "NBB VOL-VZW envelope omzet 70 YE2025 DROP -1.11% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p7 native; YE2024 14696348; 70/76A bedrijfsopbrengsten 17532054 DROP; 73 2661412; 76A empty; 74 337555 JUMP"},
    {"budget_id": "bud_sint_bernardus_bertem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p7 native; YE2024 76A empty; 76B empty"},
    {"budget_id": "bud_sint_bernardus_bertem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-283512", "amount_min_eur": "-283512", "amount_max_eur": "-283512", "basis": "NBB VOL-VZW code 9904 verlies van het boekjaar YE2025 FLIP LOSS (was 1398444)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p8 native; YE2024 1398444; 9901 -254666 + 75 20435 - 65 75986 + 67/77 26706 = -283512; destin691 empty"},
    {"budget_id": "bud_sint_bernardus_bertem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-254666", "amount_min_eur": "-254666", "amount_max_eur": "-254666", "basis": "NBB VOL-VZW code 9901 bedrijfsverlies YE2025 FLIP LOSS (was 1390308)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p7 native; YE2024 1390308; 62 13484952 JUMP; 630 1035591 JUMP; 66A 118678 JUMP; 640/8 10256 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_sint_bernardus_bertem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "11925827", "amount_min_eur": "11925827", "amount_max_eur": "11925827", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 DROP -2.52%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p6 native; YE2024 12234360; overgedragen 14 4536144 DROP; bestemde 13 5326719 FLAT; kapitaalsubsidies 15 31528 DROP; fondsen 10 2031437 FLAT"},
    {"budget_id": "bud_sint_bernardus_bertem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "17198350", "amount_min_eur": "17198350", "amount_max_eur": "17198350", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +2.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p5 native; YE2024 16794915; MVA 22/27 9925833 JUMP; cash 1258185 DROP; geldbeleggingen 4237589 JUMP; aanbouw 2033423 JUMP; capex 1506779"},
    {"budget_id": "bud_sint_bernardus_bertem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5272522", "amount_min_eur": "5272522", "amount_max_eur": "5272522", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +15.61%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p6 native; YE2024 4560555; 17 1709919 JUMP; 42/48 3488989 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 73614 DROP"},
    {"budget_id": "bud_sint_bernardus_bertem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1258185", "amount_min_eur": "1258185", "amount_max_eur": "1258185", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -27.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p5 native; YE2024 1727317; geldbeleggingen 50/53 4237589 JUMP; combined liquidity 5495774 JUMP vs prior 5647722; capex 1506779"},
    {"budget_id": "bud_sint_bernardus_bertem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (was 1398444)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2523; PDF p9 native; YE2024 691 1398444; 791 empty; 9905 -283512 FLIP LOSS; overgedragen 14 4536144 DROP; bestemde 13 5326719 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
