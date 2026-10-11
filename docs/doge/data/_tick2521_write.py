from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2521_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_torkenshof_wichelen_jr2025_nbb_pdf_2521"
SRC_KBO = "src_torkenshof_wichelen_kbo_2521"
SRC_SBM = "src_torkenshof_wichelen_sbm_2521"
SRC_SITE = "src_torkenshof_wichelen_site_2521"
EID = "vzw_torkenshof_wichelen"
GAP = "gap_torkenshof_wichelen_wzc_matrix_bruto_3_66m_omzet73_empty_cash_drop_148k_investments_jump_1_20m_l5"
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
        if _row.get("entity_id") == EID or "0812.060.838" in blob or "0812060838" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Torkenshof Wichelen deposit 2026-00381878",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00381878.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2521; official native statutory PDF 47613 bytes 12p VKT-VZW 26.0.15 m04-f; header 05/08/2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-08-05 09:17:47 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00381878 GET 200 47613 MD5 792f087d3251d44f246cdd5c4f7dd341; NBB UUID 628288e1-9093-11f1-88de-eb99ea801353; NBB published-deposits PDF 403 this tick; NBB consult list OK; prior-year identical not restated; VKT-VZW 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; Companyweb last-balansjaar 2025 discovery-only YE2025 exists euros NOT OK; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Torkenshof 0812.060.838",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0812060838",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2521; Actief since 04.06.2009; 1 VE leftover city_wichelen (official zetel Anker 15 9260 Wichelen since 01.04.2015; VE 2.230.967.336 TORKENSHOF Anker 15 since 01.08.2014 adres since 01.04.2015); VZW since 05.05.2009; RSZ-werkgever since 01.08.2014; RSZ2025 87.301 Rusthuizen voor ouderen (ROB); official Vlaanderen WZC list CoBRHA HCO 24134 dossier 457.104 52 woongelegenheden WZC Den Anker; leftover mined city_wichelen leftover WZC; NOT leftover WZC Molenkouter OCMW 0212.183.045; NOT leftover city_lebbeke leftover WZC Reva Tersig remine@2520; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Torkenshof 0812060838 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0812060838",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2521; deposit-id 2026-00381878 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 05.08.2026; NBB UUID 628288e1-9093-11f1-88de-eb99ea801353; NBB consult list OK; NBB published-deposits PDF 403 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb last-balansjaar 2025 discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Torkenshof / Den Anker FOI contact leftover city_wichelen leftover WZC",
        "url": "https://denanker-15.be/",
        "publisher": "Torkenshof VZW leftover city_wichelen leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2521; FOI den.anker@torkenshof.be from official site https://denanker-15.be/ + Zorgnet-Icuro https://www.zorgneticuro.be/leden/wzc-den-anker; leftover mined city_wichelen leftover WZC after leftover city_lebbeke leftover WZC Reva Tersig remine@2520 + leftover city_meerhout leftover WZC Ter Kempen remine@2519; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover WZC Molenkouter OCMW SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Torkenshof (WZC Den Anker)",
    "name_fr": "ASBL Torkenshof (MRS Den Anker)",
    "name_en": "Torkenshof VZW / Den Anker (leftover city_wichelen leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_wichelen",
    "community_language": "nl",
    "website": "https://denanker-15.be/",
    "foi_email": "den.anker@torkenshof.be",
    "foi_postal": "Anker 15 9260 Wichelen",
    "notes": "tick2521 YE2025 Strong official native NBB PDF deposit 2026-00381878 + Strong KBO 0812.060.838 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3663093; 70/76A not envelope (73 empty VKT); pnl DROP 224437; 9901 DROP 225437; equity JUMP 2323799; assets JUMP 2994450; debt JUMP 670652; FTE DROP 47.5; kapitaalsubsidies empty; destin691 empty; cash DROP 148212; geldbeleggingen JUMP 1202068; leftover city_wichelen leftover WZC 1 VE official zetel Wichelen; prior-year identical; NOT leftover WZC Molenkouter OCMW 0212.183.045; NOT leftover city_lebbeke leftover WZC Reva Tersig remine@2520; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_torkenshof_wichelen_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 3663093 JUMP; FOI Departement Zorg/RIZIV/Wichelen matrix behind bruto 3663093"},
    {"budget_id": "bud_torkenshof_wichelen_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 empty; FOI Departement Zorg/RIZIV matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_torkenshof_wichelen_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3663093", "amount_min_eur": "3663093", "amount_max_eur": "3663093", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +3.50% (VKT because 73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 3539316; omzet70 empty; 73 empty; 76A empty"},
    {"budget_id": "bud_torkenshof_wichelen_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_torkenshof_wichelen_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "224437", "amount_min_eur": "224437", "amount_max_eur": "224437", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -1.98% (was 228972)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 228972; 9901 225437 + 75 2563 - 65 2981 - 67/77 583 = 224437; destin691 empty"},
    {"budget_id": "bud_torkenshof_wichelen_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "225437", "amount_min_eur": "225437", "amount_max_eur": "225437", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -2.97% (was 232328)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p5 native; YE2024 232328; 62 3327968 JUMP; 630 77729 DROP; 66A empty; 640/8 31959 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_torkenshof_wichelen_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2323799", "amount_min_eur": "2323799", "amount_max_eur": "2323799", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +10.69%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p4 native; YE2024 2099362; overgedragen 14 2323799 JUMP; bestemde 13 empty; kapitaalsubsidies 15 empty; fondsen 10 empty; equity is entirely 14"},
    {"budget_id": "bud_torkenshof_wichelen_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2994450", "amount_min_eur": "2994450", "amount_max_eur": "2994450", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +9.55%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p3 native; YE2024 2733400; MVA 22/27 1110146 DROP; cash 148212 DROP; geldbeleggingen 1202068 JUMP; aanbouw 27 empty; capex 8169 75754"},
    {"budget_id": "bud_torkenshof_wichelen_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "670652", "amount_min_eur": "670652", "amount_max_eur": "670652", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +5.77%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p4 native; YE2024 634038; 17 empty; 42/48 499078 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 171574 DROP"},
    {"budget_id": "bud_torkenshof_wichelen_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "148212", "amount_min_eur": "148212", "amount_max_eur": "148212", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -86.04%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p3 native; YE2024 1061939; geldbeleggingen 50/53 1202068 JUMP was 1058; combined liquidity 1350280 JUMP vs prior 1062997; capex 8169 75754"},
    {"budget_id": "bud_torkenshof_wichelen_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2521; PDF p6 native; YE2024 691 empty; 791 empty; 9905 224437 DROP; overgedragen 14 2323799 JUMP; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
