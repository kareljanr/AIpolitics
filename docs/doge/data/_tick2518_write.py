from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2518_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_schommel_scherpenheuvel_jr2025_nbb_pdf_2518"
SRC_KBO = "src_schommel_scherpenheuvel_kbo_2518"
SRC_SBM = "src_schommel_scherpenheuvel_sbm_2518"
SRC_SITE = "src_schommel_scherpenheuvel_site_2518"
EID = "vzw_schommel_scherpenheuvel"
GAP = "gap_schommel_scherpenheuvel_cik_matrix_70_76A_6_34m_73_jump_6_19m_pnl_drop_265k_cash_jump_1_02m_l5"
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
        if _row.get("entity_id") == EID or "0462.203.119" in blob or "0462203119" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 De Schommel Scherpenheuvel-Zichem deposit 2026-00270709",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00270709.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2518; official native statutory PDF 89072 bytes 31p VOL-VZW 25.0.13 m05-f; header 07/07/2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-09 05:30:51 UTC OpenPDF 1.3.26; Last-Modified 29.07.2026; statutory pages native; CDN 2026-00270709 GET 200 89072 MD5 73dd6a29bee03bbd2f52f99b3ea1ba73; NBB consult HTML stub 5344 B discarded; NBB published-deposits 403 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 7 8 niet dienstig; commissaris Moore Audit BV B00212 / Vandenabeele Liesbet; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Schommel 0462.203.119",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0462203119",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2518; Actief since 14.11.1997; 2 VE leftover city_scherpenheuvel_zichem (official zetel Westelsebaan 108 3271 Scherpenheuvel-Zichem since 14.11.1997; VE 2.138.488.526 CKG De Schommel Westelsebaan 108 since 01.01.1998; VE 2.138.488.625 CKG De Schommel afdeling Tienen Waaibergstraat 50-52 3300 Tienen since 09.01.2000 adres since 28.04.2011); VZW since 14.11.1997; RSZ-werkgever since 01.01.1998; RSZ2025 87.991 Integrale jeugdhulp met huisvesting; leftover mined city_scherpenheuvel_zichem leftover CIK / CKG Opgroeien; 1 VE Tienen is VE of SZ-seated parent not leftover-via-VE; site Leuven Celestijnenlaan 66 is NOT a KBO VE; NOT leftover VAPH Huize Levensruimte 0407.731.976@2517; NOT leftover WZC Huyze Honighsdries 0891.481.666@2516; NOT leftover maatwerk De Vlaspit 0461.019.224@2515; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Schommel 0462203119 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0462203119",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2518; deposit-id 2026-00270709 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial neerlegging 07.07.2026; NBB consult HTML stub 5344 B discarded; NBB published-deposits 403 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb last-balansjaar 2024 STALE discovery-only YE2025 exists euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Schommel FOI contact leftover city_scherpenheuvel_zichem leftover CIK",
        "url": "https://www.deschommel.org/",
        "publisher": "De Schommel VZW leftover city_scherpenheuvel_zichem leftover CIK 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2518; FOI averbode@deschommel.org from official vestigingen page https://deschommel.org/over-de-schommel/vestigingen; leftover mined city_scherpenheuvel_zichem leftover CIK after leftover VAPH Huize Levensruimte@2517 + leftover WZC Huyze Honighsdries@2516 + leftover maatwerk De Vlaspit@2515; leftover WZC Voortberg Armonea SKIP; leftover WZC OLV Ster der Zee still unused-looking likely OCMW; leftover CAR none local; 1 VE Tienen is VE of SZ-seated parent; site Leuven mobile afdeling NOT a KBO VE; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Schommel, Centrum voor Kinderzorg en Gezinsondersteuning",
    "name_fr": "ASBL De Schommel",
    "name_en": "De Schommel VZW (leftover city_scherpenheuvel_zichem leftover CIK)",
    "level": "parastatal",
    "parent_id": "city_scherpenheuvel_zichem",
    "community_language": "nl",
    "website": "https://www.deschommel.org/",
    "foi_email": "averbode@deschommel.org",
    "foi_postal": "Westelsebaan 108 3271 Scherpenheuvel-Zichem",
    "notes": "tick2518 YE2025 Strong official native NBB PDF deposit 2026-00270709 + Strong KBO 0462.203.119 Actief 2 VE; omzet70 JUMP 47971 (commercial-only vs 73 JUMP 6186326); 76A JUMP 9000; envelope 70/76A JUMP 6341052; pnl DROP 265345; 9901 DROP 269556; equity JUMP 4000132; assets JUMP 5526522; debt JUMP 1260751; FTE JUMP 63; kapitaalsubsidies DROP 40622; destin691 DROP 66337; cash JUMP 1022183; leftover city_scherpenheuvel_zichem leftover CIK 2 VE official zetel Scherpenheuvel-Zichem; 1 VE Tienen is VE of SZ-seated parent; site Leuven not a KBO VE; prior-year identical; NOT leftover VAPH Huize Levensruimte 0407.731.976@2517; NOT leftover WZC Huyze Honighsdries 0891.481.666@2516; NOT leftover maatwerk De Vlaspit 0461.019.224@2515; NOT leftover-via-VE Brussels/Hasselt/Gent/Drongen/Leuven/Diest; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Wonozo leftover jeugdhulp; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_schommel_scherpenheuvel_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "47971", "amount_min_eur": "47971", "amount_max_eur": "47971", "basis": "NBB VOL-VZW code 70 omzet YE2025 JUMP +12.49% (commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p6 native; YE2024 42646; 73 6186326 JUMP; envelope 70/76A 6341052 JUMP; FOI Opgroeien/CKG/Scherpenheuvel-Zichem matrix behind 70/76A 6341052"},
    {"budget_id": "bud_schommel_scherpenheuvel_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6186326", "amount_min_eur": "6186326", "amount_max_eur": "6186326", "basis": "NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +5.57%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p6 native; YE2024 5859726; 733 subsidies 6145696 JUMP; 731 schenkingen 40630 JUMP; FOI Opgroeien/CKG matrix behind 73 vs commercial-only omzet"},
    {"budget_id": "bud_schommel_scherpenheuvel_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "6341052", "amount_min_eur": "6341052", "amount_max_eur": "6341052", "basis": "NBB VOL-VZW envelope 70/76A YE2025 JUMP +5.96% (VZW because omzet commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p6 native; YE2024 5984330; omzet70 47971 JUMP commercial-only; 73 6186326 JUMP; 76A 9000 JUMP; 74 97755 JUMP"},
    {"budget_id": "bud_schommel_scherpenheuvel_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9000", "amount_min_eur": "9000", "amount_max_eur": "9000", "basis": "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP from empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p6 native; YE2024 empty; 76B empty"},
    {"budget_id": "bud_schommel_scherpenheuvel_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "265345", "amount_min_eur": "265345", "amount_max_eur": "265345", "basis": "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -35.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p7 native; YE2024 410752; bedrijfswinst 9901 269556 DROP; destin691 DROP 66337"},
    {"budget_id": "bud_schommel_scherpenheuvel_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "269556", "amount_min_eur": "269556", "amount_max_eur": "269556", "basis": "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -32.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p6 native; YE2024 401717; 62 5177863 JUMP; 630 171859 JUMP; 66A empty; 640/8 26152 DROP; 635/9 57696 JUMP; 631/4 empty"},
    {"budget_id": "bud_schommel_scherpenheuvel_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "4000132", "amount_min_eur": "4000132", "amount_max_eur": "4000132", "basis": "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +7.07%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p5 native; YE2024 3735853; kapitaalsubsidies 15 40622 DROP; fondsen 10 51976 FLAT; overgedragen 14 2808070 JUMP; bestemde 13 1099464 JUMP"},
    {"budget_id": "bud_schommel_scherpenheuvel_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "5526522", "amount_min_eur": "5526522", "amount_max_eur": "5526522", "basis": "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +12.68%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p4 native; YE2024 4904805; MVA 22/27 3736195 DROP; cash 1022183 JUMP; geldbeleggingen empty; aanbouw 27 empty; capex 8161+8163 132494"},
    {"budget_id": "bud_schommel_scherpenheuvel_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1260751", "amount_min_eur": "1260751", "amount_max_eur": "1260751", "basis": "NBB VOL-VZW code 17/49 schulden YE2025 JUMP +31.19%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p5 native; YE2024 961010; 17 289708 DROP; 42/48 971043 JUMP; 43 empty; 178/9 empty; voorzieningen 16 265638 JUMP"},
    {"budget_id": "bud_schommel_scherpenheuvel_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1022183", "amount_min_eur": "1022183", "amount_max_eur": "1022183", "basis": "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +117.26%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p4 native; YE2024 470483; geldbeleggingen 50/53 empty; combined liquidity 1022183 JUMP vs prior 470483; capex 8161+8163 132494"},
    {"budget_id": "bud_schommel_scherpenheuvel_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "66337", "amount_min_eur": "66337", "amount_max_eur": "66337", "basis": "NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -55.31%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2518; PDF p8 native; YE2024 691 148438 DROP; 791 empty; 9905 265345; overgedragen 14 2808070 JUMP; bestemde 13 1099464 JUMP"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
