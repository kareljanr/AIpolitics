from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2509_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_kinderpret_asse_jr2025_nbb_pdf_2509"
SRC_KBO = "src_kinderpret_asse_kbo_2509"
SRC_SBM = "src_kinderpret_asse_sbm_2509"
SRC_SITE = "src_kinderpret_asse_site_2509"
EID = "vzw_kinderpret_asse"
GAP = "gap_kinderpret_asse_cik_matrix_bruto_1_68m_omzet73_empty_cash_jump_715k_pnl_jump_164k_l5"
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
if "0421.200.724" in ent_raw or "0421200724" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Kribbe Kinderpret Asse deposit 2026-00338297",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00338297.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2509; official native statutory PDF 45641 bytes 12p VKT-VZW 26.0.15 m04-f; header 22.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-28 02:34:42 UTC OpenPDF 1.3.26; CDN Last-Modified 05.08.2026; statutory pages native; CDN 2026-00338297 GET 200 45641 MD5 b3f3e93d5f0cef2fcaee654b2a7ee464; NBB broker HTML unused this tick; VKT-VZW 6.1.1 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; official PDF assets 3679473 not SBM table 3679474; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Kribbe Kinderpret 0421.200.724",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421200724",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2509; Actief since 05.02.1981; 1 VE leftover city_asse (official zetel Keesdal 13 1730 Asse since 25.08.2017; VE 2.150.809.407 Kribbe Kinderpret Keesdal 13 since 03.01.2006 address since 25.08.2017); VZW since 05.02.1981; RSZ-werkgever since 01.01.1983; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover mined city_asse leftover CIK; NOT 3Wplus Kinderopvang 0893.870.539 remine leftover city_asse leftover CIK; NOT Vijverbeek 0448.164.744 remine leftover city_asse leftover CIK; NOT Hopperank 0434.363.921 remine leftover city_asse leftover VAPH; NOT 3Wplus Werk 0467.004.520 remine leftover city_asse leftover maatwerk; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Kribbe Kinderpret 0421200724 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0421200724",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2509; deposit-id 2026-00338297 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 2026-07-28; NBB Consult + SBM CDN used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; official PDF assets 3679473 not SBM table 3679474; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Kribbe Kinderpret FOI contact leftover city_asse leftover CIK",
        "url": "https://kribbekinderpret.be/",
        "publisher": "Kribbe Kinderpret VZW leftover city_asse leftover CIK 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2509; FOI via official site contact form https://kribbekinderpret.be/contact/ (NBB PDF email empty; no public mailbox on site; phone +32 2 452 79 87); leftover mined city_asse leftover CIK after 3Wplus Kinderopvang@2407 + Vijverbeek@2469 leftover CIK locks; NOT 3Wplus Kinderopvang remine; NOT Vijverbeek remine; NOT Hopperank remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Kribbe Kinderpret",
    "name_fr": "ASBL Kribbe Kinderpret",
    "name_en": "Kribbe Kinderpret VZW (leftover city_asse leftover CIK)",
    "level": "parastatal",
    "parent_id": "city_asse",
    "community_language": "nl",
    "website": "https://kribbekinderpret.be/",
    "foi_email": "",
    "foi_postal": "Keesdal 13 1730 Asse",
    "notes": "tick2509 YE2025 Strong official native NBB PDF deposit 2026-00338297 + Strong KBO 0421.200.724 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 1681501; pnl JUMP 163831; 9901 JUMP 177966; equity JUMP 2769915; assets DROP 3679473; debt DROP 909558; FTE DROP 21.2; kapitaalsubsidies DROP 1322230; destin691 empty; cash JUMP 714672; geldbeleggingen 373688; leftover city_asse leftover CIK 1 VE official zetel Asse; prior-year identical; NOT 3Wplus Kinderopvang 0893.870.539 remine leftover city_asse leftover CIK; NOT Vijverbeek 0448.164.744 remine leftover city_asse leftover CIK; NOT Hopperank 0434.363.921 remine leftover city_asse leftover VAPH; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_kinderpret_asse_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 1681501 JUMP; FOI Opgroeien/gemeente matrix behind bruto 1681501"},
    {"budget_id": "bud_kinderpret_asse_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_kinderpret_asse_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1681501", "amount_min_eur": "1681501", "amount_max_eur": "1681501", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +6.88% (VKT because 73 empty and bruto ≫ omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5 native; YE2024 1573304; omzet70 empty; 73 empty; 76A empty"},
    {"budget_id": "bud_kinderpret_asse_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5/p9 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_kinderpret_asse_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "163831", "amount_min_eur": "163831", "amount_max_eur": "163831", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +16.62%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5 native; YE2024 140480; bedrijfswinst 9901 177966 JUMP; destin691 empty"},
    {"budget_id": "bud_kinderpret_asse_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "177966", "amount_min_eur": "177966", "amount_max_eur": "177966", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +14.53%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p5 native; YE2024 155392; 62 1383369 JUMP; 630 120111 DROP; 66A empty; 640/8 55 FLAT; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_kinderpret_asse_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2769915", "amount_min_eur": "2769915", "amount_max_eur": "2769915", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +3.85%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p4 native; YE2024 2667128; kapitaalsubsidies 15 1322230 DROP; overgedragen 14 1244752 JUMP; fondsen 10 150073 FLAT; bestemde 13 52860 FLAT"},
    {"budget_id": "bud_kinderpret_asse_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3679473", "amount_min_eur": "3679473", "amount_max_eur": "3679473", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -0.52%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p3 native; YE2024 3698839; MVA 22/27 2488496 DROP; cash 714672 JUMP; geldbeleggingen 373688; aanbouw 27 empty; official PDF 3679473 not SBM 3679474"},
    {"budget_id": "bud_kinderpret_asse_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "909558", "amount_min_eur": "909558", "amount_max_eur": "909558", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -11.84%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p4 native; YE2024 1031711; 17 660741 DROP; 42/48 248817 DROP; voorzieningen 16 empty"},
    {"budget_id": "bud_kinderpret_asse_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "714672", "amount_min_eur": "714672", "amount_max_eur": "714672", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +19.38%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p3 native; YE2024 598653; geldbeleggingen 50/53 373688 was 373431; combined liquidity 1088360; capex 8169 empty; overdrachten 8179 empty"},
    {"budget_id": "bud_kinderpret_asse_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2509; PDF p6 native; YE2024 destin empty; 791 empty; overgedragen 14 1244752 JUMP; bestemde 13 52860 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
