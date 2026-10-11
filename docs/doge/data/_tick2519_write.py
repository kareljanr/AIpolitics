from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2519_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_ter_kempen_meerhout_jr2025_nbb_pdf_2519"
SRC_KBO = "src_ter_kempen_meerhout_kbo_2519"
SRC_SBM = "src_ter_kempen_meerhout_sbm_2519"
SRC_SITE = "src_ter_kempen_meerhout_site_2519"
EID = "vzw_ter_kempen_meerhout"
GAP = "gap_ter_kempen_meerhout_wzc_matrix_bruto_3_19m_omzet73_empty_pnl_empty_cash_drop_55k_equity_drop_916k_l5"
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
        if _row.get("entity_id") == EID or "0871.619.135" in blob or "0871619135" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Ter Kempen Meerhout deposit 2026-00251692",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00251692.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2519; official native statutory PDF 53636 bytes 16p VKT-VZW 26.0.15 m04-f; header 30/06/2026; AV 04.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-04 05:14:29 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00251692 GET 200 53636 MD5 59fd19afc7109504d2187b8a90ac0594; NBB UUID a853cf1d-747b-11f1-846f-959060aeeb11; NBB published-deposits PDF 403 this tick; NBB consult list OK; prior-year identical not restated; VKT-VZW 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Ter Kempen 0871.619.135",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0871619135",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2519; Actief since 02.02.2005; 1 VE leftover city_meerhout (official zetel Smissestraat 8 2450 Meerhout since 11.01.2005; VE 2.148.263.849 TER KEMPEN VZW Smissestraat 8 since 16.03.2005); VZW since 11.01.2005; RSZ-werkgever since 16.03.2005; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); leftover mined city_meerhout leftover WZC; NOT leftover WZC De Berk OCMW Meerhout 0212.196.705; NOT leftover maatwerk De Sprong 0466.328.686 remine@2286; NOT leftover city_oosterzele leftover WZC Groep Sint-Franciscus 0412.763.704 remine@2142; NOT leftover city_herselt leftover WZC Sint-Barbara 0422.152.314 remine@2019; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Ter Kempen 0871619135 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0871619135",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2519; deposit-id 2026-00251692 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 30.06.2026; NBB UUID a853cf1d-747b-11f1-846f-959060aeeb11; NBB consult list OK; NBB published-deposits PDF 403 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Ter Kempen FOI contact leftover city_meerhout leftover WZC",
        "url": "https://www.terkempen.be/",
        "publisher": "Ter Kempen VZW leftover city_meerhout leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2519; FOI info@terkempen.be from official NBB PDF identification; leftover mined city_meerhout leftover WZC after leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 + leftover city_herselt leftover WZC Sint-Barbara remine@2019; leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518; leftover maatwerk De Sprong remine@2286; leftover WZC De Berk OCMW SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Ter Kempen",
    "name_fr": "ASBL Ter Kempen",
    "name_en": "Ter Kempen VZW (leftover city_meerhout leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_meerhout",
    "community_language": "nl",
    "website": "https://www.terkempen.be/",
    "foi_email": "info@terkempen.be",
    "foi_postal": "Smissestraat 8 2450 Meerhout",
    "notes": "tick2519 YE2025 Strong official native NBB PDF deposit 2026-00251692 + Strong KBO 0871.619.135 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3190771; 70/76A empty; pnl empty break-even; 9901 DROP 8203; equity DROP 916229; assets DROP 2457213; debt DROP 1532610; FTE DROP 40; kapitaalsubsidies DROP 916229; destin691 empty; cash DROP 55356; leftover city_meerhout leftover WZC 1 VE official zetel Meerhout; prior-year identical; NOT leftover WZC De Berk OCMW 0212.196.705; NOT leftover maatwerk De Sprong 0466.328.686 remine@2286; NOT leftover city_oosterzele leftover WZC Groep Sint-Franciscus 0412.763.704 remine@2142; NOT leftover city_herselt leftover WZC Sint-Barbara 0422.152.314 remine@2019; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_ter_kempen_meerhout_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6 native; YE2024 empty; 73 empty; envelope bruto9900 3190771 JUMP; FOI Departement Zorg/RIZIV/Meerhout matrix behind bruto 3190771"},
    {"budget_id": "bud_ter_kempen_meerhout_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6 native; YE2024 empty; FOI Departement Zorg/RIZIV matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_ter_kempen_meerhout_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3190771", "amount_min_eur": "3190771", "amount_max_eur": "3190771", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +3.69% (VKT because 73 empty and bruto \u226b omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6 native; YE2024 3077246; omzet70 empty; 73 empty; 76A empty"},
    {"budget_id": "bud_ter_kempen_meerhout_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6/p11 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_ter_kempen_meerhout_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 empty (break-even 0)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6 native; YE2024 empty; 9901 8203 DROP + 75 1 - 65 8204 = 0; destin691 empty"},
    {"budget_id": "bud_ter_kempen_meerhout_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "8203", "amount_min_eur": "8203", "amount_max_eur": "8203", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -6.05%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p6 native; YE2024 8731; 62 2980040 JUMP; 630 186072 DROP; 66A empty; 640/8 16456 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_ter_kempen_meerhout_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "916229", "amount_min_eur": "916229", "amount_max_eur": "916229", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -6.78%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p5 native; YE2024 982917; kapitaalsubsidies 15 916229 DROP (equity is entirely 15); fondsen 10 empty; overgedragen 14 empty; bestemde 13 empty"},
    {"budget_id": "bud_ter_kempen_meerhout_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2457213", "amount_min_eur": "2457213", "amount_max_eur": "2457213", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -12.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p4 native; YE2024 2796334; MVA 22/27 2258245 DROP; cash 55356 DROP; geldbeleggingen empty; aanbouw 27 empty; capex 8169 14001"},
    {"budget_id": "bud_ter_kempen_meerhout_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1532610", "amount_min_eur": "1532610", "amount_max_eur": "1532610", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -15.09%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p5 native; YE2024 1805042; 17 775346 DROP; 42/48 757264 DROP; 178/9 228356 DROP; voorzieningen 16 8374 FLAT"},
    {"budget_id": "bud_ter_kempen_meerhout_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "55356", "amount_min_eur": "55356", "amount_max_eur": "55356", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -33.71%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p4 native; YE2024 83505; geldbeleggingen 50/53 empty; combined liquidity 55356 DROP vs prior 83505; capex 8169 14001"},
    {"budget_id": "bud_ter_kempen_meerhout_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2519; PDF p7 native; YE2024 691 empty; 791 empty; 9905 empty; overgedragen 14 empty; bestemde 13 empty"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
