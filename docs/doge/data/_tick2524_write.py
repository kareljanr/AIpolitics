from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2524_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_eglantier_bertem_jr2025_nbb_pdf_2524"
SRC_KBO = "src_eglantier_bertem_kbo_2524"
SRC_SBM = "src_eglantier_bertem_sbm_2524"
SRC_SITE = "src_eglantier_bertem_site_2524"
EID = "vzw_eglantier_bertem"
GAP = "gap_eglantier_bertem_vaph_matrix_70_76A_1_95m_73_jump_1_73m_pnl_flip_18k_cash_drop_120k_l5"
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
        if _row.get("entity_id") == EID or "0418.747.911" in blob or "0418747911" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 De Eglantier Bertem deposit 2026-00119829",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00119829.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2524; official native statutory PDF 53823 bytes 13p VKT-VZW 25.0.12 m04-f; header 21/05/2026; AV 23.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-26 07:23:18 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00119829 GET 200 53823 MD5 e613c32f5f89a2f3f35b673fbec1f251 Last-Modified 09.06.2026; NBB UUID c1598648-2117-11f1-98bb-9b1150461c27; NBB broker PDF 403 this tick; NBB ids list 22 / nonmig 6 this tick; NBB published-deposits list 200 this tick; prior-year identical not restated; VKT-VZW 6.1.1 6.1.3 6.5 6.6 7 8 niet dienstig; Companyweb last deposit 26.05.2026 YE2025 discovery-only unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Eglantier 0418.747.911",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418747911",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2524; Actief since 30.06.1978; 1 VE leftover city_bertem (official zetel Coige-steenweg 19 3061 Bertem since 18.11.1981; VE 2.154.333.475 DE EGLANTIER Coige-steenweg 19 since 08.06.2006); VZW since 30.06.1978; naam DE EGLANTIER since 17.04.1989; RSZ-werkgever since 01.08.1979; RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting n.e.g.; official VAPH organisaties-adressen De Eglantier Coigesteenweg 19 3061 BERTEM; leftover mined city_bertem leftover VAPH leftover-mined AGB-only; NOT leftover city_bertem leftover WZC Sint-Bernardus remine@2523; NOT leftover VAPH A-Tipi 0788.729.170 leftover-via-VE Leuven SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Eglantier 0418747911 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0418747911",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2524; deposit-id 2026-00119829 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 21.05.2026; NBB UUID c1598648-2117-11f1-98bb-9b1150461c27; NBB ids list 22 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb last deposit 26.05.2026 YE2025 discovery-only unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Eglantier FOI contact leftover city_bertem leftover VAPH",
        "url": "http://web.eglantier.org/",
        "publisher": "De Eglantier VZW leftover city_bertem leftover VAPH 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2524; FOI info@eglantier.be from official site http://web.eglantier.org/ / www.eglantier.be tel 02 767 47 05; leftover mined city_bertem leftover VAPH leftover-mined AGB-only after leftover WZC Sint-Bernardus@2523; leftover city_bertem leftover VAPH A-Tipi leftover-via-VE Leuven SKIP; leftover city_bertem leftover CAR none local; leftover city_bertem leftover maatwerk none local; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking leftover CIK fallback not taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Eglantier (MFC De Eglantier)",
    "name_fr": "ASBL De Eglantier (CMF De Eglantier)",
    "name_en": "De Eglantier VZW (leftover city_bertem leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_bertem",
    "community_language": "nl",
    "website": "http://web.eglantier.org/",
    "foi_email": "info@eglantier.be",
    "foi_postal": "Coige-steenweg 19 3061 Bertem",
    "notes": "tick2524 YE2025 Strong official native NBB PDF deposit 2026-00119829 + Strong KBO 0418.747.911 Actief 1 VE; omzet70 DROP 88481 commercial-only vs large 73; 73 JUMP 1732649; 76A JUMP 130588; envelope 70/76A JUMP 1951718; bruto9900 JUMP 1800928; pnl FLIP 18173; 9901 FLIP LOSS -3269; equity JUMP 4228756; assets JUMP 5219768; debt JUMP 991012; FTE JUMP 24.1; kapitaalsubsidies DROP 838237; destin691 JUMP 43130; cash DROP 119855; geldbeleggingen JUMP 1664865; leftover city_bertem leftover VAPH 1 VE official zetel Bertem leftover-mined AGB-only; prior-year identical; NOT leftover city_bertem leftover WZC Sint-Bernardus remine@2523; NOT leftover VAPH A-Tipi leftover-via-VE Leuven; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_eglantier_bertem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "88481", "amount_min_eur": "88481", "amount_max_eur": "88481", "basis": "NBB VKT-VZW code 70 omzet YE2025 DROP -5.04% (commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5 native; YE2024 93176; 73 1732649 JUMP; envelope 70/76A 1951718 JUMP; FOI VAPH/Bertem matrix behind 70/76A 1951718"},
    {"budget_id": "bud_eglantier_bertem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1732649", "amount_min_eur": "1732649", "amount_max_eur": "1732649", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.25%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5 native; YE2024 1646175; FOI VAPH matrix behind 73 JUMP vs commercial-only omzet DROP"},
    {"budget_id": "bud_eglantier_bertem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1951718", "amount_min_eur": "1951718", "amount_max_eur": "1951718", "basis": "NBB VKT-VZW envelope 70/76A YE2025 JUMP +7.98% (VZW because omzet commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5 native; YE2024 1807469; 70+73+76A; 70 88481 commercial-only; 73 1732649; 76A 130588; bruto9900 1800928 JUMP"},
    {"budget_id": "bud_eglantier_bertem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "130588", "amount_min_eur": "130588", "amount_max_eur": "130588", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +91.71%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5/p10 native; YE2024 68118; 76B empty"},
    {"budget_id": "bud_eglantier_bertem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "18173", "amount_min_eur": "18173", "amount_max_eur": "18173", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP PROFIT (was -27430)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5 native; YE2024 -27430; 9901 -3269 + 75 29579 - 65 8137 = 18173; destin691 43130 JUMP"},
    {"budget_id": "bud_eglantier_bertem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-3269", "amount_min_eur": "-3269", "amount_max_eur": "-3269", "basis": "NBB VKT-VZW code 9901 bedrijfsverlies YE2025 FLIP LOSS (was 33301)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p5 native; YE2024 33301; 62 1649088 JUMP; 630 129052 JUMP; 66A 13365 JUMP; 640/8 12692 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_eglantier_bertem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4228756", "amount_min_eur": "4228756", "amount_max_eur": "4228756", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p4 native; YE2024 4109756; overgedragen 14 1863952 DROP; bestemde 13 171130 JUMP; kapitaalsubsidies 15 838237 DROP; fondsen 10 1207743 FLAT; herwaardering 12 147695 new"},
    {"budget_id": "bud_eglantier_bertem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5219768", "amount_min_eur": "5219768", "amount_max_eur": "5219768", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.39%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p3 native; YE2024 5097760; MVA 22/27 3130307 JUMP; cash 119855 DROP; geldbeleggingen 1664865 JUMP; aanbouw 27 empty; capex 8169 68620"},
    {"budget_id": "bud_eglantier_bertem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "991012", "amount_min_eur": "991012", "amount_max_eur": "991012", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.30%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p4 native; YE2024 988004; 17 533333 DROP; 42/48 452574 JUMP; 178/9 empty; voorzieningen 16 empty; overlopende 492/3 5104 new"},
    {"budget_id": "bud_eglantier_bertem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "119855", "amount_min_eur": "119855", "amount_max_eur": "119855", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -42.52%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p3 native; YE2024 208500; geldbeleggingen 50/53 1664865 JUMP; combined liquidity 1784720 JUMP vs prior 1724456; capex 8169 68620"},
    {"budget_id": "bud_eglantier_bertem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "43130", "amount_min_eur": "43130", "amount_max_eur": "43130", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (was 16000)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2524; PDF p6 native; YE2024 691 16000; 791 empty; 9905 18173 FLIP; overgedragen 14 1863952 DROP; bestemde 13 171130 JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
