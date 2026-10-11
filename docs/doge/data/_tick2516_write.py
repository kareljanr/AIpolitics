from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2516_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_honighsdries_scherpenheuvel_jr2025_nbb_pdf_2516"
SRC_KBO = "src_honighsdries_scherpenheuvel_kbo_2516"
SRC_SBM = "src_honighsdries_scherpenheuvel_sbm_2516"
SRC_SITE = "src_honighsdries_scherpenheuvel_site_2516"
EID = "vzw_honighsdries_scherpenheuvel"
GAP = "gap_honighsdries_scherpenheuvel_wzc_matrix_bruto_6_31m_omzet73_empty_pnl_jump_127k_cash_jump_878k_l5"
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
        if _row.get("entity_id") == EID or "0891.481.666" in " ".join(_row.values()) or "0891481666" in " ".join(_row.values()):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Huyze Honighsdries Scherpenheuvel-Zichem deposit 2026-00393713",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00393713.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2516; official native statutory PDF 50697 bytes 14p VKT-VZW 23.0.10 m04-f; header 12/08/2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-08-12 05:07:11 UTC OpenPDF 1.3.26; statutory pages native; NBB broker PDF GET 200 50697 MD5 9efba8f3079fc96ec0aa7159b44132fa; NBB UUID 5acf0839-960b-11f1-97d4-b332a1eb9963; CDN 2026-00393713 403 this tick; NBB published-deposits page 500 this tick; NBB ids list 17 / nonmig 5; prior-year identical not restated; VKT-VZW 6.2 6.5 6.6 7 8 niet dienstig; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Huyze Honighsdries 0891.481.666",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0891481666",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2516; Actief since 17.08.2007; 1 VE leftover city_scherpenheuvel_zichem (official zetel Prins De Merodelaan 1 3271 Scherpenheuvel-Zichem since 30.06.2008; VE 2.172.780.006 Prins De Merodelaan 1 since 01.07.2008); VZW since 27.07.2007; RSZ-werkgever since 01.07.2008; RSZ2025 87.302 Serviceflats voor ouderen; BTW2025 87.301 Rusthuizen voor ouderen (ROB); leftover mined city_scherpenheuvel_zichem leftover WZC; CoBRHA HCO 22558 RIZIV 76215076; NOT WZC Voortberg Armonea 0889.421.308; NOT leftover VAPH Huize Levensruimte 0407.731.976; NOT De Vlaspit 0461.019.224 leftover maatwerk@2515; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Huyze Honighsdries 0891481666 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0891481666",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2516; deposit-id 2026-00393713 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 12.08.2026; NBB UUID 5acf0839-960b-11f1-97d4-b332a1eb9963; NBB ids + broker PDF used for deposit-id discovery; SBM IP blacklist this tick; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Huyze Honighsdries FOI contact leftover city_scherpenheuvel_zichem leftover WZC",
        "url": "https://www.huyzehonighsdries.be/",
        "publisher": "Huyze Honighsdries VZW leftover city_scherpenheuvel_zichem leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2516; FOI postbus@huyzehonighsdries.be from Sociale Kaart / official site contact form; phone 013 53 96 00; leftover mined city_scherpenheuvel_zichem leftover WZC after leftover maatwerk De Vlaspit@2515; leftover WZC Voortberg Armonea SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover VAPH Huize Levensruimte 0407.731.976 unused + YE2025 ZIP 2026-07-14; leftover CAR none local; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Huyze Honighsdries",
    "name_fr": "ASBL Huyze Honighsdries",
    "name_en": "Huyze Honighsdries VZW (leftover city_scherpenheuvel_zichem leftover WZC)",
    "level": "parastatal",
    "parent_id": "city_scherpenheuvel_zichem",
    "community_language": "nl",
    "website": "https://www.huyzehonighsdries.be/",
    "foi_email": "postbus@huyzehonighsdries.be",
    "foi_postal": "Prins De Merodelaan 1 3271 Scherpenheuvel-Zichem",
    "notes": "tick2516 YE2025 Strong official native NBB PDF deposit 2026-00393713 + Strong KBO 0891.481.666 Actief 1 VE; omzet70 empty VKT; 73 empty VKT; 76A empty DROP (was 425); envelope bruto9900 JUMP 6311576; 70/76A empty; pnl JUMP 126816; 9901 DROP 170450; equity JUMP -113700 still negative; assets JUMP 3990698; debt JUMP 4104398; FTE DROP 80.5; kapitaalsubsidies empty; destin691 empty; cash JUMP 877928; geldbeleggingen JUMP 1893976; leftover city_scherpenheuvel_zichem leftover WZC 1 VE official zetel Scherpenheuvel-Zichem; prior-year identical; NOT WZC Voortberg Armonea; NOT leftover VAPH Huize Levensruimte 0407.731.976; NOT De Vlaspit 0461.019.224 leftover maatwerk@2515; NOT leftover-via-VE Brussels/Hasselt/Gent/Diest; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_honighsdries_scherpenheuvel_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 70 omzet YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5 native; YE2024 empty; 73 empty; envelope bruto9900 6311576 JUMP; FOI Departement Zorg/RIZIV/Scherpenheuvel-Zichem matrix behind bruto 6311576"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5 native; YE2024 empty; FOI Departement Zorg/RIZIV matrix behind empty 73 vs material bruto"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6311576", "amount_min_eur": "6311576", "amount_max_eur": "6311576", "basis": "NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +3.14% (VKT because 73 empty and bruto \u226b omzet)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5 native; YE2024 6119409; omzet70 empty; 73 empty; 76A empty DROP (was 425)"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty DROP (was 425)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5/p11 native; YE2024 425; 76B empty"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "126816", "amount_min_eur": "126816", "amount_max_eur": "126816", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +121.86%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5 native; YE2024 57161; bedrijfswinst 9901 170450 DROP; destin691 empty"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "170450", "amount_min_eur": "170450", "amount_max_eur": "170450", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -3.96%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p5 native; YE2024 177484; 62 6050220 JUMP; 630 81997 DROP; 66A empty; 640/8 8909 JUMP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-113700", "amount_min_eur": "-113700", "amount_max_eur": "-113700", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP (still negative; was -240516)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p4 native; YE2024 -240516; kapitaalsubsidies 15 empty; fondsen 10 empty; overgedragen 14 -113700 JUMP still negative; bestemde 13 empty"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "3990698", "amount_min_eur": "3990698", "amount_max_eur": "3990698", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p3 native; YE2024 3822651; MVA 22/27 201602 DROP; cash 877928 JUMP; geldbeleggingen 1893976 JUMP; aanbouw 27 empty; capex 8169 76053"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4104398", "amount_min_eur": "4104398", "amount_max_eur": "4104398", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +1.01%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p4 native; YE2024 4063166; 17 1000000 FLAT; 42/48 2975917 JUMP; 178/9 empty; voorzieningen 16 empty"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "877928", "amount_min_eur": "877928", "amount_max_eur": "877928", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +4.26%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p3 native; YE2024 842088; geldbeleggingen 50/53 1893976 JUMP; combined liquidity 2771904 JUMP vs prior 2650449; capex 8169 76053"},
    {"budget_id": "bud_honighsdries_scherpenheuvel_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2516; PDF p6 native; YE2024 691 empty; 791 empty; 9905 126816 overgedragen to 14"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
