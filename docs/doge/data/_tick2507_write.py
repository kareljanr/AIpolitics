from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2507_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_capelderij_buggenhout_jr2025_nbb_pdf_2507"
SRC_KBO = "src_capelderij_buggenhout_kbo_2507"
SRC_SBM = "src_capelderij_buggenhout_sbm_2507"
SRC_SITE = "src_capelderij_buggenhout_site_2507"
EID = "vzw_capelderij_buggenhout"
GAP = "gap_capelderij_buggenhout_vaph_matrix_bruto_3_84m_omzet73_empty_cash_drop_1_02m_pnl_improved_loss_2_6k_l5"
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

ent_raw = (DATA / "entities.csv").read_text(encoding="utf-8")
if "0417.002.505" in ent_raw or "0417002505" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Capelderij Buggenhout deposit 2026-00310005",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00310005.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2507; official native statutory PDF 53689 bytes 15p VKT-VZW 26.0.15 m04-f; header 20.07.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-20 09:47:18 UTC OpenPDF 1.3.26; CDN Last-Modified 02.08.2026; statutory pages native; CDN 2026-00310005 GET 200 53689 MD5 ffabdfa6670be77e9f75b5e0ad993035; official NBB UUID e8fd7c5d-8127-11f1-8707-b99fdd398e54; NBB broker HTML stub 5344 B discarded; VKT-VZW 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Begeleidingscentrum Capelderij 0417.002.505",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417002505",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2507; Actief since 31.03.1977; 1 VE leftover city_buggenhout (official zetel Vekenstraat 1 9255 Buggenhout since 01.10.1990; VE 2.153.812.348 Begeleidingscentrum Capelderij Vekenstraat 1 since 01.06.2006); VZW since 31.03.1977; RSZ-werkgever since 01.07.1977; RSZ2025 87.201 + 87.991; leftover mined city_buggenhout leftover VAPH MFC/BuSO; NOT Avalon 0464.778.666 remine leftover city_buggenhout VAPH; NOT De Heymeulen 0420.669.303 leftover city_buggenhout WZC YE2024; NOT CAR Buggenhout 0412.404.903 leftover-via-VE Gent SKIP; NOT Blijdorp 0409.371.771 remine parent sec_flanders; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Capelderij 0417002505 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0417002505",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2507; deposit-id 2026-00310005 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial UUID e8fd7c5d-8127-11f1-8707-b99fdd398e54; NBB published-deposits/ids + SBM CDN used for deposit-id discovery; Companyweb last-balansjaar discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Capelderij FOI contact leftover city_buggenhout leftover VAPH",
        "url": "https://www.capelderij.be/",
        "publisher": "Capelderij VZW leftover city_buggenhout leftover VAPH MFC/BuSO 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2507; FOI info@capelderij.be / raad.van.bestuur@capelderij.be from official site contact (NBB PDF email empty); leftover mined city_buggenhout leftover VAPH MFC/BuSO after Avalon@2503 leftover VAPH lock; NOT Avalon remine; NOT De Heymeulen YE2024; NOT CAR Buggenhout leftover-via-VE; NOT Blijdorp remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Capelderij",
    "name_fr": "ASBL Capelderij",
    "name_en": "Capelderij VZW (leftover city_buggenhout leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_buggenhout",
    "community_language": "nl",
    "website": "https://www.capelderij.be/",
    "foi_email": "info@capelderij.be",
    "foi_postal": "Vekenstraat 1 9255 Buggenhout",
    "notes": "tick2507 YE2025 Strong official native NBB PDF deposit 2026-00310005 + Strong KBO 0417.002.505 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A 0 DROP; envelope bruto9900 JUMP 3841282; pnl IMPROVED LOSS -2621; 9901 IMPROVED LOSS -22415; equity DROP 2764099; assets DROP 3376776; debt JUMP 612676; FTE JUMP 48.1 from empty/0; kapitaalsubsidies DROP 981457; destin691 empty; cash DROP 100666; geldbeleggingen JUMP 1500000; leftover city_buggenhout leftover VAPH MFC/BuSO 1 VE official zetel Buggenhout; prior-year identical; NOT Avalon 0464.778.666 remine leftover city_buggenhout VAPH; NOT De Heymeulen 0420.669.303 leftover city_buggenhout WZC YE2024; NOT CAR Buggenhout 0412.404.903 leftover-via-VE Gent SKIP; NOT Blijdorp 0409.371.771 remine parent sec_flanders; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_capelderij_buggenhout_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 3841282 JUMP; FOI VAPH/Opgroeien/gemeente/BuSO matrix behind bruto 3841282"},
    {"budget_id": "bud_capelderij_buggenhout_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5 native; YE2024 empty; FOI VAPH/Opgroeien matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_capelderij_buggenhout_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3841282", "amount_min_eur": "3841282", "amount_max_eur": "3841282", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +6.17% (VKT because 73 empty and bruto ≫ omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5 native; YE2024 3617984; omzet70 empty; 73 empty; 76A 0 DROP"},
    {"budget_id": "bud_capelderij_buggenhout_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP to 0", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5/p12 native; YE2024 10257; 76B empty"},
    {"budget_id": "bud_capelderij_buggenhout_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-2621", "amount_min_eur": "-2621", "amount_max_eur": "-2621", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 IMPROVED LOSS", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5 native; YE2024 -9384; bedrijfswinst 9901 -22415 IMPROVED LOSS; destin691 empty"},
    {"budget_id": "bud_capelderij_buggenhout_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-22415", "amount_min_eur": "-22415", "amount_max_eur": "-22415", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 IMPROVED LOSS", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p5 native; YE2024 -25578; 62 3506508 JUMP; 630 327591 JUMP; 66A empty; 640/8 29598 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_capelderij_buggenhout_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2764099", "amount_min_eur": "2764099", "amount_max_eur": "2764099", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -6.50%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p4 native; YE2024 2956384; kapitaalsubsidies 15 981457 DROP; overgedragen 14 1782642 DROP; fondsen 10 empty; bestemde 13 empty"},
    {"budget_id": "bud_capelderij_buggenhout_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3376776", "amount_min_eur": "3376776", "amount_max_eur": "3376776", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -5.25%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p3 native; YE2024 3564015; MVA 22/27 1312473 DROP; cash 100666 DROP; geldbeleggingen 1500000 JUMP; aanbouw 27 empty"},
    {"budget_id": "bud_capelderij_buggenhout_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "612676", "amount_min_eur": "612676", "amount_max_eur": "612676", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.83%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p4 native; YE2024 607631; 17 empty LT; 42/48 608160 JUMP"},
    {"budget_id": "bud_capelderij_buggenhout_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "100666", "amount_min_eur": "100666", "amount_max_eur": "100666", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -91.00%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p3 native; YE2024 1118612; geldbeleggingen 50/53 1500000 JUMP was 500000; combined liquidity 1600666; capex 8169 69237; overdrachten 8179 3168382"},
    {"budget_id": "bud_capelderij_buggenhout_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2507; PDF p6 native; YE2024 destin empty; 791 empty; overgedragen 14 1782642 DROP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
