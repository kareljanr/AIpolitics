from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2512_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_de_bron_zottegem_jr2025_nbb_pdf_2512"
SRC_KBO = "src_de_bron_zottegem_kbo_2512"
SRC_SBM = "src_de_bron_zottegem_sbm_2512"
SRC_SITE = "src_de_bron_zottegem_site_2512"
EID = "vzw_de_bron_zottegem"
GAP = "gap_de_bron_zottegem_wzc_matrix_omzet_7_45m_73_jump_1_07m_pnl_jump_317k_cash_drop_201k_l5"
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
if "0892.673.479" in ent_raw or "0892673479" in ent_raw or EID in ent_raw:
    raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 De Bron Zottegem deposit 2026-00244305",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00244305.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2512; official native statutory PDF 533008 bytes 44p VOL-VZW 25.0.13 m05-f; header 29/06/2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-03 01:40:29 UTC OpenPDF 1.3.26; CDN Last-Modified 24.07.2026; statutory pages native; CDN 2026-00244305 GET 200 533008 MD5 997d58533cc7b062c8ff660713f1dbc6; official NBB UUID b233a36d-3e45-11f1-84fe-893fb4017eb7; prior-year identical not restated; commissaris VYVEY & C BEDRIJFDREVISOR BVBA B00523 / Vyvey Steven A01917; VOL-VZW 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 niet dienstig; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Bron 0892.673.479",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0892673479",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2512; Actief since 09.10.2007; 3 VE leftover city_zottegem (official zetel Marie Popelinstraat 8 9620 Zottegem since 26.06.2023; VE 2.192.304.423 WZC De Bron Marie Popelinstraat 8 since 21.06.2021 + 2.194.479.993 DVC De Bron Marie Popelinstraat 8A since 21.06.2021 + 2.265.007.804 GAW De Bron Marie Popelinstraat 4 since 01.06.2017); VZW since 21.09.2007; RSZ-werkgever; RSZ2025 87.302 Serviceflats voor ouderen; VE NACE 87.301 ROB; leftover mined city_zottegem leftover WZC; NOT WZC Egmont OCMW 0212.187.302; NOT De Hoop 0870.779.490 unused leftover VAPH sister; NOT Werkplus 0466.950.179 remine@2204; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Bron 0892673479 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0892673479",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2512; deposit-id 2026-00244305 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial neerlegging 03.07.2026; NBB published-deposits/ids + broker PDF + SBM CDN used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Bron FOI contact leftover city_zottegem leftover WZC",
        "url": "https://www.debronzorgtvooru.be/",
        "publisher": "De Bron VZW leftover city_zottegem leftover WZC 3 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2512; FOI boekhoudng.debron@sezz.be from official NBB PDF header; leftover mined city_zottegem leftover WZC after leftover city_grimbergen leftover WZC Den Bogaet@2511 + leftover maatwerk Den Diepen Boomgaard@2510; NOT WZC Egmont OCMW; NOT De Hoop leftover VAPH unused sister; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Bron",
    "name_fr": "De Bron ASBL",
    "name_en": "De Bron VZW (leftover city_zottegem leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_zottegem",
    "community_language": "nl",
    "website": "https://www.debronzorgtvooru.be/",
    "foi_email": "boekhoudng.debron@sezz.be",
    "foi_postal": "Marie Popelinstraat 8 9620 Zottegem",
    "notes": "tick2512 YE2025 Strong official native NBB PDF deposit 2026-00244305 + Strong KBO 0892.673.479 Actief 3 VE; omzet70 JUMP 7450435 (not commercial-only vs 73 JUMP 1070214); 76A DROP 8251; envelope omzet70 JUMP 7450435; 70/76A JUMP 8987103; pnl JUMP 316649; 9901 JUMP 511019; equity JUMP 9977020; assets DROP 23805911; debt DROP 13828891; FTE DROP 82.7; kapitaalsubsidies JUMP 911560; destin691 empty; cash DROP 201059; geldbeleggingen JUMP 2166587; leftover city_zottegem leftover WZC 3 VE official zetel Zottegem; prior-year identical; NOT WZC Egmont OCMW 0212.187.302; NOT De Hoop 0870.779.490 unused leftover VAPH sister; NOT Werkplus remine@2204; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_de_bron_zottegem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7450435", "amount_min_eur": "7450435", "amount_max_eur": "7450435", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +1.46% (not commercial-only vs 73 1.07m)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p7 native; YE2024 7343120; envelope omzet70 7450435 JUMP; FOI RIZIV/zorgkas/OCMW/eigen-bijdrage matrix behind 7450435"},
    {"budget_id": "bud_de_bron_zottegem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1070214", "amount_min_eur": "1070214", "amount_max_eur": "1070214", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.31%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p7 native; YE2024 1016231; 733 1070214 JUMP; 732 empty vs YE2024 12411; FOI RIZIV/VL zorgkas matrix behind 1070214"},
    {"budget_id": "bud_de_bron_zottegem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7450435", "amount_min_eur": "7450435", "amount_max_eur": "7450435", "basis": "NBB VOL-VZW envelope omzet 70 YE2025 JUMP +1.46% (70 present and not commercial-only)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p7 native; YE2024 7343120; 70/76A 8987103 JUMP; 76A 8251 DROP; 74 458203 JUMP"},
    {"budget_id": "bud_de_bron_zottegem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8251", "amount_min_eur": "8251", "amount_max_eur": "8251", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -65.54%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p7 native; YE2024 23940; 76B empty"},
    {"budget_id": "bud_de_bron_zottegem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "316649", "amount_min_eur": "316649", "amount_max_eur": "316649", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +28.85%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p8 native; YE2024 245758; bedrijfswinst 9901 511019 JUMP; destin691 empty"},
    {"budget_id": "bud_de_bron_zottegem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "511019", "amount_min_eur": "511019", "amount_max_eur": "511019", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +12.42%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p7 native; YE2024 454549; 62 5729109 JUMP; 630 936438 JUMP; 66A 11339 DROP; 640/8 38144 JUMP; 635/9 empty; 631/4 0 DROP"},
    {"budget_id": "bud_de_bron_zottegem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9977020", "amount_min_eur": "9977020", "amount_max_eur": "9977020", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +3.42%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p6 native; YE2024 9647360; kapitaalsubsidies 15 911560 JUMP; fondsen 10 6633279 FLAT; overgedragen 14 2052224 JUMP"},
    {"budget_id": "bud_de_bron_zottegem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "23805911", "amount_min_eur": "23805911", "amount_max_eur": "23805911", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.98%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p5 native; YE2024 24287024; MVA 22/27 20546719 DROP; cash 201059 DROP; geldbeleggingen 2166587 JUMP; aanbouw 27 40660 JUMP; capex 288007"},
    {"budget_id": "bud_de_bron_zottegem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "13828891", "amount_min_eur": "13828891", "amount_max_eur": "13828891", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 DROP -5.54%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p6 native; YE2024 14639664; 17 11320272 DROP; 42/48 2472674 JUMP; 173 10440272; voorzieningen 16 empty"},
    {"budget_id": "bud_de_bron_zottegem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "201059", "amount_min_eur": "201059", "amount_max_eur": "201059", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -35.07%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p5 native; YE2024 309649; geldbeleggingen 50/53 2166587 JUMP; combined liquidity 2367646 JUMP; capex 288007"},
    {"budget_id": "bud_de_bron_zottegem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2512; PDF p9 native; YE2024 691 empty; 791 empty; 9905 316649 overgedragen to 14"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
