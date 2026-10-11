from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2520_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_reva_tersig_lebbeke_jr2025_nbb_pdf_2520"
SRC_KBO = "src_reva_tersig_lebbeke_kbo_2520"
SRC_SBM = "src_reva_tersig_lebbeke_sbm_2520"
SRC_SITE = "src_reva_tersig_lebbeke_site_2520"
EID = "vzw_reva_tersig_lebbeke"
GAP = "gap_reva_tersig_lebbeke_wzc_matrix_bruto_3_12m_omzet73_empty_pnl_flip_454k_loss_cash_drop_163k_equity_drop_958k_l5"
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
        if _row.get("entity_id") == EID or "0860.679.020" in blob or "0860679020" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Reva Tersig Lebbeke deposit 2026-00307029",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00307029.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2520; official native statutory PDF 48290 bytes 13p VKT-VZW 26.0.15 m04-f; header 13/07/2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-18 01:18:02 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00307029 GET 200 48290 MD5 99b59166928926df5a086ff779192899; NBB UUID 0ddc4893-7e80-11f1-bb07-9b5b960de055; NBB published-deposits PDF 403 this tick; NBB consult list OK; prior-year identical not restated; VKT-VZW 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; Companyweb NL last-balansjaar 2024 STALE / FR 2025 discovery-only YE2025 exists; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Reva Tersig 0860.679.020",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860679020",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2520; Actief since 24.09.2003; 1 VE leftover city_lebbeke (official zetel Hoeksken 3 9280 Lebbeke since 26.05.2003; VE 2.159.341.249 Reva Tersig Hoeksken 3 since 08.02.2007); VZW since 26.05.2003; RSZ-werkgever since 01.07.2004; RSZ2025 86.101/86.103 ziekenhuis/gespecialiseerde ziekenhuizen; official Vlaanderen WZC list CoBRHA HCO 16545 dossier 429.104 20 woongelegenheden; leftover mined city_lebbeke leftover WZC; NOT leftover WZC Hof ter Veldeken OCMW 0212.192.151; NOT leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial; NOT leftover WZC Seniorie Minneveld BV 0840.544.095 commercial; NOT leftover city_lennik leftover maatwerk Pajottenland 0413.313.535 remine@2201; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Reva Tersig 0860679020 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0860679020",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2520; deposit-id 2026-00307029 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 13.07.2026; NBB UUID 0ddc4893-7e80-11f1-bb07-9b5b960de055; NBB consult list OK; NBB published-deposits PDF 403 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb NL last-balansjaar 2024 STALE / FR 2025 discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Reva Tersig FOI contact leftover city_lebbeke leftover WZC",
        "url": "https://www.tersig.be/",
        "publisher": "Reva Tersig VZW leftover city_lebbeke leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2520; FOI info@tersig.be from official site https://www.tersig.be/contact/; leftover mined city_lebbeke leftover WZC after leftover city_meerhout leftover WZC Ter Kempen remine@2519 + leftover city_lennik leftover maatwerk Pajottenland remine@2201; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover WZC Hof ter Veldeken OCMW SKIP; leftover WZC Seniorie Ter Minne/Minneveld BV commercial SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Reva Tersig",
    "name_fr": "ASBL Reva Tersig",
    "name_en": "Reva Tersig VZW (leftover city_lebbeke leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_lebbeke",
    "community_language": "nl",
    "website": "https://www.tersig.be/",
    "foi_email": "info@tersig.be",
    "foi_postal": "Hoeksken 3 9280 Lebbeke",
    "notes": "tick2520 YE2025 Strong official native NBB PDF deposit 2026-00307029 + Strong KBO 0860.679.020 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A JUMP 66043; envelope bruto9900 DROP 3117153; 70/76A not envelope (73 empty VKT); pnl FLIP -454073; 9901 FLIP -453340; equity DROP 958018; assets DROP 2483710; debt JUMP 1525692; FTE JUMP 50.8; kapitaalsubsidies empty; destin691 empty; cash DROP 162617; leftover city_lebbeke leftover WZC 1 VE official zetel Lebbeke; prior-year identical; NOT leftover WZC Hof ter Veldeken OCMW 0212.192.151; NOT leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial; NOT leftover WZC Seniorie Minneveld BV 0840.544.095 commercial; NOT leftover city_lennik leftover maatwerk Pajottenland 0413.313.535 remine@2201; NOT leftover city_meerhout leftover WZC Ter Kempen remine@2519; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_reva_tersig_lebbeke_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 3117153 DROP; FOI Departement Zorg/RIZIV/Lebbeke matrix behind bruto 3117153"},
    {"budget_id": "bud_reva_tersig_lebbeke_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 empty; FOI Departement Zorg/RIZIV matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_reva_tersig_lebbeke_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3117153", "amount_min_eur": "3117153", "amount_max_eur": "3117153", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 DROP -3.23% (VKT because 73 empty and bruto >> omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 3221361; omzet70 empty; 73 empty; 76A JUMP 66043"},
    {"budget_id": "bud_reva_tersig_lebbeke_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "66043", "amount_min_eur": "66043", "amount_max_eur": "66043", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP (was empty)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_reva_tersig_lebbeke_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-454073", "amount_min_eur": "-454073", "amount_max_eur": "-454073", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP (was +27599)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 27599; 9901 -453340 + 75 1846 - 65 1172 - 67/77 1408 = -454073; destin691 empty"},
    {"budget_id": "bud_reva_tersig_lebbeke_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-453340", "amount_min_eur": "-453340", "amount_max_eur": "-453340", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP (was +26963)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p5 native; YE2024 26963; 62 3336858 JUMP; 630 123125 JUMP; 66A 41664 JUMP; 640/8 68846 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_reva_tersig_lebbeke_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "958018", "amount_min_eur": "958018", "amount_max_eur": "958018", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -32.16%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p4 native; YE2024 1412092; overgedragen 14 678018 DROP; bestemde 13 280000 FLAT; kapitaalsubsidies 15 empty; fondsen 10 empty"},
    {"budget_id": "bud_reva_tersig_lebbeke_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2483710", "amount_min_eur": "2483710", "amount_max_eur": "2483710", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -9.27%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p3 native; YE2024 2737413; MVA 22/27 945174 DROP; cash 162617 DROP; geldbeleggingen empty; aanbouw 27 empty; capex 8169 101725"},
    {"budget_id": "bud_reva_tersig_lebbeke_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1525692", "amount_min_eur": "1525692", "amount_max_eur": "1525692", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +15.12%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p4 native; YE2024 1325322; 17 3320; 42/48 1522372 JUMP; 178/9 3320; voorzieningen 16 empty; overlopende 492/3 empty DROP was 324117"},
    {"budget_id": "bud_reva_tersig_lebbeke_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "162617", "amount_min_eur": "162617", "amount_max_eur": "162617", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -65.60%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p3 native; YE2024 472775; geldbeleggingen 50/53 empty; combined liquidity 162617 DROP vs prior 472775; capex 8169 101725"},
    {"budget_id": "bud_reva_tersig_lebbeke_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2520; PDF p6 native; YE2024 691 empty; 791 empty; 9905 -454073 FLIP; overgedragen 14 678018 DROP; bestemde 13 280000 FLAT"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
