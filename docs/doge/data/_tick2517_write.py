from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2517_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_levensruimte_scherpenheuvel_jr2025_nbb_pdf_2517"
SRC_KBO = "src_levensruimte_scherpenheuvel_kbo_2517"
SRC_SBM = "src_levensruimte_scherpenheuvel_sbm_2517"
SRC_SITE = "src_levensruimte_scherpenheuvel_site_2517"
EID = "vzw_levensruimte_scherpenheuvel"
GAP = "gap_levensruimte_scherpenheuvel_vaph_matrix_bruto_3_97m_omzet73_empty_pnl_drop_33k_cash_jump_486k_l5"
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
        blob = " ".join([_row.get("entity_id",""), _row.get("name_nl",""), _row.get("name_fr",""), _row.get("name_en","")])
        if _row.get("entity_id") == EID or "0407.731.976" in blob or "0407731976" in blob or "levensruimte" in _row.get("entity_id","").lower():
            raise SystemExit(f"entity already present {_row.get('entity_id')}")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Huize Levensruimte Scherpenheuvel-Zichem deposit 2026-00290688",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00290688.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2517; official native statutory PDF 54552 bytes 16p VKT-VZW 23.0.10 m04-f; header 14/07/2026; AV 25.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-14 20:50:43 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00290688 GET 200 54552 MD5 2fb3ed3b0a9fcda7ce984b814dfe4cec; NBB UUID 85d34533-7f9b-11f1-8707-89699e4a9d62; NBB broker 403 this tick; NBB ids list 19; prior-year identical not restated; VKT-VZW 6.5 7 8 niet dienstig; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Huize Levensruimte 0407.731.976",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407731976",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2517; Actief since 29.11.1970; 2 VE leftover city_scherpenheuvel_zichem (official zetel Pater De Grootstraat 6 3271 Scherpenheuvel-Zichem since 03.09.1998; VE 2.200.290.887 Pater De Grootstraat 6 since 01.01.2008; VE 2.371.145.105 Perron Z Statiestraat 59 3200 Aarschot since 03.03.2025 NACE 88.992); VZW since 29.11.1970; RSZ-werkgever since 01.01.1971; RSZ2025 87.991 Integrale jeugdhulp met huisvesting; leftover mined city_scherpenheuvel_zichem leftover VAPH; 1 VE Aarschot is VE of SZ-seated parent not leftover city_aarschot; NOT leftover WZC Huyze Honighsdries 0891.481.666@2516; NOT leftover maatwerk De Vlaspit 0461.019.224@2515; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Huize Levensruimte 0407731976 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0407731976",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2517; deposit-id 2026-00290688 YE 01.01.2025-31.12.2025 filing VKT-VZW ZIP Initial neerlegging 14.07.2026; NBB UUID 85d34533-7f9b-11f1-8707-89699e4a9d62; NBB ids + CDN PDF used for deposit-id discovery; ZIP/XBRL not used for euros; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Huize Levensruimte FOI contact leftover city_scherpenheuvel_zichem leftover VAPH",
        "url": "https://www.huizelevensruimte.be/",
        "publisher": "Huize Levensruimte VZW leftover city_scherpenheuvel_zichem leftover VAPH 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2517; FOI onthaal@huizelevensruimte.be from official contact page https://huizelevensruimte.be/contact/; directeur Eddy Mues eddy.mues@huizelevensruimte.be; leftover mined city_scherpenheuvel_zichem leftover VAPH after leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; leftover WZC Voortberg Armonea SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover CAR none local; leftover CIK still unused-looking; 1 VE Perron Z Aarschot is VE of SZ-seated parent; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Huize Levensruimte",
    "name_fr": "ASBL Huize Levensruimte",
    "name_en": "Huize Levensruimte VZW (leftover city_scherpenheuvel_zichem leftover VAPH)",
    "level": "parastatal",
    "parent_id": "city_scherpenheuvel_zichem",
    "community_language": "nl",
    "website": "https://www.huizelevensruimte.be/",
    "foi_email": "onthaal@huizelevensruimte.be",
    "foi_postal": "Pater De Grootstraat 6 3271 Scherpenheuvel-Zichem",
    "notes": "tick2517 YE2025 Strong official native NBB PDF deposit 2026-00290688 + Strong KBO 0407.731.976 Actief 2 VE; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto9900 JUMP 3970477; 70/76A empty; pnl DROP 33452; 9901 DROP 26750; equity DROP 6156850; assets JUMP 7131536; debt JUMP 974687; FTE JUMP 49.9; kapitaalsubsidies DROP 2712291; destin691 FLAT 150000; cash JUMP 485753; geldbeleggingen JUMP 1309750; leftover city_scherpenheuvel_zichem leftover VAPH 2 VE official zetel Scherpenheuvel-Zichem; 1 VE Perron Z Aarschot is VE of SZ-seated parent; prior-year identical; NOT leftover WZC Huyze Honighsdries 0891.481.666@2516; NOT leftover maatwerk De Vlaspit 0461.019.224@2515; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_levensruimte_scherpenheuvel_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 3970477 JUMP; FOI Opgroeien/VAPH/Scherpenheuvel-Zichem matrix behind bruto 3970477"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5 native; YE2024 empty; FOI Opgroeien/VAPH matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3970477", "amount_min_eur": "3970477", "amount_max_eur": "3970477", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +4.01% (VKT because 73 empty and bruto \u226b omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5 native; YE2024 3817499; omzet70 empty; 73 empty; 76A empty"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5/p12 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "33452", "amount_min_eur": "33452", "amount_max_eur": "33452", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -87.48%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5 native; YE2024 267164; bedrijfswinst 9901 26750 DROP; destin691 FLAT 150000"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "26750", "amount_min_eur": "26750", "amount_max_eur": "26750", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -89.85%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p5 native; YE2024 263468; 62 3650263 JUMP; 630 243984 JUMP; 66A empty; 640/8 49480 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6156850", "amount_min_eur": "6156850", "amount_max_eur": "6156850", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -1.38%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p4 native; YE2024 6243127; kapitaalsubsidies 15 2712291 DROP; fondsen 10 1150000 FLAT; overgedragen 14 1844559 DROP; bestemde 13 450000 JUMP"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "7131536", "amount_min_eur": "7131536", "amount_max_eur": "7131536", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +3.64%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p3 native; YE2024 6881215; MVA 22/27 4909130 DROP; cash 485753 JUMP; geldbeleggingen 1309750 JUMP; aanbouw 27 empty; capex 8169 123235"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "974687", "amount_min_eur": "974687", "amount_max_eur": "974687", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +52.75%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p4 native; YE2024 638088; 17 122152 DROP; 42/48 852535 JUMP; 43 250000 new; 178/9 empty; voorzieningen 16 empty"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "485753", "amount_min_eur": "485753", "amount_max_eur": "485753", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +221.86%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p3 native; YE2024 150920; geldbeleggingen 50/53 1309750 JUMP; combined liquidity 1795503 JUMP vs prior 1400920; capex 8169 123235"},
    {"budget_id": "bud_levensruimte_scherpenheuvel_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "150000", "amount_min_eur": "150000", "amount_max_eur": "150000", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 FLAT 150000", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2517; PDF p6 native; YE2024 691 150000 FLAT; 791 empty; 9905 33452; overgedragen 14 1844559 DROP; bestemde 13 450000 JUMP (provisie energiebesparende investeringen)"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
