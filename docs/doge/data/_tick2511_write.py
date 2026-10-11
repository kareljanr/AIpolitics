from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2511_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_den_bogaet_grimbergen_jr2025_nbb_pdf_2511"
SRC_KBO = "src_den_bogaet_grimbergen_kbo_2511"
SRC_SBM = "src_den_bogaet_grimbergen_sbm_2511"
SRC_SITE = "src_den_bogaet_grimbergen_site_2511"
EID = "bv_den_bogaet_grimbergen"
GAP = "gap_den_bogaet_grimbergen_wzc_matrix_omzet_7_59m_694_2_50m_equity_drop_4_38m_debt_jump_3_57m_l5"
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
if "0471.673.980" in ent_raw or "0471673980" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-inb jaarrekening 2025 DEN BOGAET Grimbergen deposit 2026-00341036",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00341036.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2511; official native statutory PDF 85525 bytes 30p VOL-inb 23.0.10 m82-f; header 28/07/2026; AV 12.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-28 13:31:18 UTC OpenPDF 1.3.26; CDN Last-Modified 05.08.2026; statutory pages native; CDN 2026-00341036 GET 200 85525 MD5 28f478d2c55c37541feefc8a678f44e2; official NBB UUID 3415d8e0-8a80-11f1-aede-bf63c074ea8d; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO DEN BOGAET 0471.673.980",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0471673980",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2511; Actief since 12.04.2000; 1 VE leftover city_grimbergen (official zetel Dorpsstraat 1 1851 Grimbergen since 15.12.2020; VE 2.100.640.314 SENIORIE-RESIDENTIE-DEN BOGAET Dorpsstraat 1 since 06.08.2002); BV since 28.03.2023; RSZ-werkgever; RSZ2025 87.101 RVT; VE NACE 87.301 ROB; leftover mined city_grimbergen leftover WZC; NOT WZC Heilig Hart Grimbergen 0409.724.238 remine@2074; NOT Havinet 0642.602.234 remine leftover VAPH; NOT Den Diepen Boomgaard 0421.285.252 leftover maatwerk@2510; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche DEN BOGAET 0471673980 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0471673980",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2511; deposit-id 2026-00341036 YE 01.01.2025-31.12.2025 filing VOL-inb Initial neerlegging 2026-07-28; NBB published-deposits/ids + broker PDF + SBM CDN used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Den Bogaet FOI contact leftover city_grimbergen leftover WZC",
        "url": "https://denbogaet.be/",
        "publisher": "DEN BOGAET BV leftover city_grimbergen leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2511; FOI info@denbogaet.be from official contact page https://denbogaet.be/contact/ (HTML-entity mail; NBB PDF email empty; phone 02 260 10 00); leftover mined city_grimbergen leftover WZC after leftover maatwerk Den Diepen Boomgaard@2510 + leftover VAPH Havinet remine@2301 + leftover WZC Heilig Hart remine@2074; NOT WZC Heilig Hart remine; NOT Havinet remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Den Bogaet",
    "name_fr": "Den Bogaet SRL",
    "name_en": "Den Bogaet BV (leftover city_grimbergen leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_grimbergen",
    "community_language": "nl",
    "website": "https://denbogaet.be/",
    "foi_email": "info@denbogaet.be",
    "foi_postal": "Dorpsstraat 1 1851 Grimbergen",
    "notes": "tick2511 YE2025 Strong official native NBB PDF deposit 2026-00341036 + Strong KBO 0471.673.980 Actief 1 VE; omzet70 JUMP 7593721 (6.10 OCMW 51256 + mutualiteit 3677526 + ontvangsten 3692253 + AW 172686; not commercial-only); 73 empty VOL; 76A empty DROP; envelope omzet70 JUMP 7593721; 694 JUMP 2500000; pnl FLIP PROFIT 166838; 9901 DROP 143914; equity DROP 4375649; assets FLAT 7947826; debt JUMP 3572177; FTE DROP 73.8; kapitaalsubsidies empty; destin691 empty; cash DROP 272100; geldbeleggingen JUMP 5417200; leftover city_grimbergen leftover WZC 1 VE official zetel Grimbergen; prior-year identical; NOT WZC Heilig Hart Grimbergen 0409.724.238 remine@2074; NOT Havinet 0642.602.234 remine leftover VAPH; NOT Den Diepen Boomgaard 0421.285.252 leftover maatwerk@2510; NOT Evara remine; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_den_bogaet_grimbergen_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7593721", "amount_min_eur": "7593721", "amount_max_eur": "7593721", "basis": "NBB VOL-inb code 70 omzet YE2025 JUMP +3.66% (not commercial-only; 6.10 OCMW+mutualiteit inside 70)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p8 native; YE2024 7325433; 6.10 Ontvangsten 3692253 + OCMW 51256 + mutualiteit 3677526 + AW 172686; envelope omzet70 7593721 JUMP; FOI RIZIV/zorgkas/OCMW/eigen-bijdrage matrix behind 7593721"},
    {"budget_id": "bud_den_bogaet_grimbergen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-inb code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VOL niet dienstig; VOL uses 74)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p8 native VOL-inb; YE2024 empty; 74 658611 DROP; 740 exploitatiesubsidies empty; FOI RIZIV/VL zorgkas matrix behind empty 73 vs material omzet70"},
    {"budget_id": "bud_den_bogaet_grimbergen_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7593721", "amount_min_eur": "7593721", "amount_max_eur": "7593721", "basis": "NBB VOL-inb envelope omzet 70 YE2025 JUMP +3.66% (70 present and not commercial-only)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p8 native; YE2024 7325433; 70/76A 8252332 JUMP; 76A empty DROP; 74 658611 DROP"},
    {"budget_id": "bud_den_bogaet_grimbergen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-inb code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty DROP (was 12000)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p8 native; YE2024 12000; 76B empty"},
    {"budget_id": "bud_den_bogaet_grimbergen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "166838", "amount_min_eur": "166838", "amount_max_eur": "166838", "basis": "NBB VOL-inb code 9904 winst van het boekjaar YE2025 FLIP PROFIT (was -264935)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p9 native; YE2024 -264935; bedrijfswinst 9901 143914 DROP; destin691 empty; 694 JUMP 2500000"},
    {"budget_id": "bud_den_bogaet_grimbergen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "143914", "amount_min_eur": "143914", "amount_max_eur": "143914", "basis": "NBB VOL-inb code 9901 bedrijfswinst YE2025 DROP -10.35% (was 160535)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p8 native; YE2024 160535; 62 5542523 JUMP; 630 164605 DROP; 66A empty; 640/8 999 DROP; 635/8 empty; 631/4 empty"},
    {"budget_id": "bud_den_bogaet_grimbergen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4375649", "amount_min_eur": "4375649", "amount_max_eur": "4375649", "basis": "NBB VOL-inb code 10/15 eigen vermogen YE2025 DROP -34.78%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p6 native; YE2024 6708811; kapitaalsubsidies 15 empty; inbreng 10/11 31000 FLAT; reserves 13 4344649 DROP; 792 2500000 JUMP"},
    {"budget_id": "bud_den_bogaet_grimbergen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7947826", "amount_min_eur": "7947826", "amount_max_eur": "7947826", "basis": "NBB VOL-inb code 20/58 totaal activa YE2025 FLAT (was 7948153)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p5 native; YE2024 7948153; MVA 22/27 634395 DROP; cash 272100 DROP; geldbeleggingen 5417200 JUMP; aanbouw 27 empty; capex 8161+8162 144164"},
    {"budget_id": "bud_den_bogaet_grimbergen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3572177", "amount_min_eur": "3572177", "amount_max_eur": "3572177", "basis": "NBB VOL-inb code 17/49 schulden YE2025 JUMP +188.23%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p7 native; YE2024 1239341; 17 empty LT; 42/48 3572177 JUMP; 47/48 2767585 JUMP; voorzieningen 16 empty"},
    {"budget_id": "bud_den_bogaet_grimbergen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "272100", "amount_min_eur": "272100", "amount_max_eur": "272100", "basis": "NBB VOL-inb code 54/58 liquide middelen YE2025 DROP -58.76%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p5 native; YE2024 659742; geldbeleggingen 50/53 5417200 JUMP; combined liquidity 5689300 JUMP; capex 144164; overdrachten 817x empty"},
    {"budget_id": "bud_den_bogaet_grimbergen_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2500000", "amount_min_eur": "2500000", "amount_max_eur": "2500000", "basis": "NBB VOL-inb code 694 vergoeding van de inbreng YE2025 JUMP 2.50m from empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2511; PDF p10 native; YE2024 694 empty; 691 empty; 691/2 103688 DROP; 792 2500000 JUMP from empty; destin is the 2.50m dividend extraction"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
