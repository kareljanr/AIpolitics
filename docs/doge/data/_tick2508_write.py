from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2508_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_dagmoed_geraardsbergen_jr2025_nbb_pdf_2508"
SRC_KBO = "src_dagmoed_geraardsbergen_kbo_2508"
SRC_SBM = "src_dagmoed_geraardsbergen_sbm_2508"
SRC_SITE = "src_dagmoed_geraardsbergen_site_2508"
EID = "vzw_dagmoed_geraardsbergen"
GAP = "gap_dagmoed_geraardsbergen_maatwerk_matrix_bruto_3_93m_omzet73_empty_cash_drop_329k_635_9_jump_185k_l5"
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
if "0416.317.070" in ent_raw or "0416317070" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 De Dagmoed Geraardsbergen deposit 2026-00131365",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131365.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2508; official native statutory PDF 50258 bytes 15p VKT-VZW 26.0.11 m04-f; header 02.06.2026; AV 26.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-02 08:53:30 UTC OpenPDF 1.3.26; CDN Last-Modified 10.06.2026; statutory pages native; CDN 2026-00131365 GET 200 50258 MD5 038b081c004cb9b9bd4786636ad7ebad; NBB published-deposits/ids 403 this tick; NBB broker 403 JSON 142 B discarded; VKT-VZW 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Dagmoed 0416.317.070",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416317070",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2508; Actief since 10.06.1976; 1 VE leftover city_geraardsbergen (official zetel Dagmoedstraat(Sch) 107 9506 Geraardsbergen since 28.12.2005; VE 2.154.901.421 De Zonnebloem - Beschutte Werkplaats te Geraardsbergen vzw Dagmoedstraat 107 since 05.07.2006); VZW since 10.06.1976; RSZ-werkgever since 01.10.1976; RSZ2025 88.993; leftover mined city_geraardsbergen leftover maatwerk; NOT Wonozo 0423.555.349 skip jeugdhulp Geraardsbergen; NOT CAR Horizon 0418.529.759 remine leftover city_geraardsbergen CAR; NOT Kringwinkel Zuid-Oost-Vlaanderen 0466.159.432 remine; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Dagmoed 0416317070 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0416317070",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2508; deposit-id 2026-00131365 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial; NBB Consult + SBM CDN used for deposit-id discovery; NBB published-deposits/ids 403 this tick; Companyweb last-balansjaar discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Dagmoed FOI contact leftover city_geraardsbergen leftover maatwerk",
        "url": "https://dagmoed.be/",
        "publisher": "De Dagmoed VZW leftover city_geraardsbergen leftover maatwerk 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2508; FOI info@dagmoed.be / personeel@dagmoed.be from official site contact https://dagmoed.be/contact/ (NBB PDF email empty); leftover mined city_geraardsbergen leftover maatwerk after CAR Horizon@2395 leftover CAR lock; NOT Wonozo skip jeugdhulp; NOT CAR Horizon remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Dagmoed",
    "name_fr": "ASBL De Dagmoed",
    "name_en": "De Dagmoed VZW (leftover city_geraardsbergen leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_geraardsbergen",
    "community_language": "nl",
    "website": "https://dagmoed.be/",
    "foi_email": "info@dagmoed.be",
    "foi_postal": "Dagmoedstraat 107 9506 Geraardsbergen",
    "notes": "tick2508 YE2025 Strong official native NBB PDF deposit 2026-00131365 + Strong KBO 0416.317.070 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3928555; pnl JUMP 122649; 9901 DROP 118329; equity JUMP 2137199; assets JUMP 4296270; debt JUMP 1111269; FTE JUMP 89.3; kapitaalsubsidies empty; destin691 empty; cash DROP 397386; geldbeleggingen JUMP 2000000; 635/9 JUMP 185300; leftover city_geraardsbergen leftover maatwerk 1 VE official zetel Geraardsbergen; prior-year identical; NOT Wonozo 0423.555.349 skip jeugdhulp Geraardsbergen; NOT CAR Horizon 0418.529.759 remine leftover city_geraardsbergen CAR; NOT Kringwinkel Zuid-Oost-Vlaanderen 0466.159.432 remine; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_dagmoed_geraardsbergen_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 3928555 JUMP; FOI WEWIS/VDAB/gemeente matrix behind bruto 3928555"},
    {"budget_id": "bud_dagmoed_geraardsbergen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5 native; YE2024 empty; FOI WEWIS/VDAB matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_dagmoed_geraardsbergen_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3928555", "amount_min_eur": "3928555", "amount_max_eur": "3928555", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +18.99% (VKT because 73 empty and bruto \xe2\x89\xab omzet)".replace("\\xe2\\x89\\xab", "≫"), "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5 native; YE2024 3301704; omzet70 empty; 73 empty; 76A empty"},
    {"budget_id": "bud_dagmoed_geraardsbergen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5/p12 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_dagmoed_geraardsbergen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "122649", "amount_min_eur": "122649", "amount_max_eur": "122649", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +2.68%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5 native; YE2024 119445; bedrijfswinst 9901 118329 DROP; destin691 empty"},
    {"budget_id": "bud_dagmoed_geraardsbergen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "118329", "amount_min_eur": "118329", "amount_max_eur": "118329", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -2.56%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p5 native; YE2024 121438; 62 3478587 JUMP; 630 134547 JUMP; 66A 53 JUMP; 640/8 11739 JUMP; 635/9 185300 JUMP; 631/4 empty"},
    {"budget_id": "bud_dagmoed_geraardsbergen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2137199", "amount_min_eur": "2137199", "amount_max_eur": "2137199", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +6.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p4 native; YE2024 2014550; kapitaalsubsidies 15 empty; overgedragen 14 1791240 JUMP; fondsen 10 203754 FLAT; bestemde 13 142204 FLAT"},
    {"budget_id": "bud_dagmoed_geraardsbergen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4296270", "amount_min_eur": "4296270", "amount_max_eur": "4296270", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +10.31%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p3 native; YE2024 3894633; MVA 22/27 1496252 JUMP; cash 397386 DROP; geldbeleggingen 2000000 JUMP; aanbouw 27 empty"},
    {"budget_id": "bud_dagmoed_geraardsbergen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1111269", "amount_min_eur": "1111269", "amount_max_eur": "1111269", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +9.21%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p4 native; YE2024 1017581; 17 550232 DROP; 42/48 561037 JUMP; voorzieningen 16 1047802 JUMP"},
    {"budget_id": "bud_dagmoed_geraardsbergen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "397386", "amount_min_eur": "397386", "amount_max_eur": "397386", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -45.33%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p3 native; YE2024 726849; geldbeleggingen 50/53 2000000 JUMP was 1500000; combined liquidity 2397386; capex 8169 324771; overdrachten 8179 53669"},
    {"budget_id": "bud_dagmoed_geraardsbergen_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2508; PDF p6 native; YE2024 destin empty; 791 empty; overgedragen 14 1791240 JUMP; bestemde 13 142204 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
