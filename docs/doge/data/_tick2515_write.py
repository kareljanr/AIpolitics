from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2515_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_vlaspit_scherpenheuvel_jr2025_nbb_pdf_2515"
SRC_KBO = "src_vlaspit_scherpenheuvel_kbo_2515"
SRC_SBM = "src_vlaspit_scherpenheuvel_sbm_2515"
SRC_SITE = "src_vlaspit_scherpenheuvel_site_2515"
EID = "vzw_vlaspit_scherpenheuvel"
GAP = "gap_vlaspit_scherpenheuvel_maatwerk_matrix_omzet_2_25m_73_jump_1_62m_pnl_flip_loss_49k_cash_jump_863k_l5"
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
        if _row.get("entity_id") == EID or "0461.019.224" in " ".join(_row.values()) or "0461019224" in " ".join(_row.values()):
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 De Vlaspit Scherpenheuvel-Zichem deposit 2026-00196614",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00196614.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2515; official native statutory PDF 286949 bytes 20p VKT-VZW 25.0.13 m04-f; header 25/06/2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-25 08:59:15 UTC OpenPDF 1.3.26; CDN Last-Modified 09.07.2026; statutory pages native; CDN 2026-00196614 GET 200 286949 MD5 6ad8efc6a62c1ea6dc84b583efc30c39; NBB UUID 4b59a525-109a-11f1-b070-59cd73ada9a5; prior-year identical not restated; commissaris CDO Leuven BV oordeel zonder voorbehoud; VKT-VZW 6.2 6.5 7 niet dienstig; NBB published-deposits list 500 this tick; NBB broker HTML unused; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO De Vlaspit 0461.019.224",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461019224",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2515; Actief since 20.03.1997; 4 VE leftover city_scherpenheuvel_zichem (official zetel Basilieklaan 53 3270 Scherpenheuvel-Zichem since 25.06.2008; VE 2.157.197.747 Basilieklaan 53 since 25.06.2008; VE 2.183.828.405 Albertusplein 19 since 01.01.2010; VE 2.185.155.325 Isabellaplein 19 since 01.01.2010; VE 2.257.380.238 Het Beverbeekhuis Tulpenstraat 10 3290 Diest since 20.12.2021); VZW since 20.03.1997; RSZ-werkgever; RSZ2025 88.993; BTW2025 32.990+47.789+88.993; official Flanders maatwerk CMW05 toekenningsnummer 0461019224; leftover mined city_scherpenheuvel_zichem leftover maatwerk; NOT De Vlaspit Dienstencheques 0463.655.941 sister; NOT leftover-via-VE Diest of a Diest-seated parent; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Vlaspit 0461019224 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0461019224",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2515; deposit-id 2026-00196614 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 25.06.2026; NBB UUID 4b59a525-109a-11f1-b070-59cd73ada9a5; SBM CDN + NBB broker used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Vlaspit FOI contact leftover city_scherpenheuvel_zichem leftover maatwerk",
        "url": "https://www.devlaspit.be/",
        "publisher": "De Vlaspit VZW leftover city_scherpenheuvel_zichem leftover maatwerk 4 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2515; FOI info@devlaspit.be from official KBO VE email since 01.01.2023; leftover mined city_scherpenheuvel_zichem leftover maatwerk after leftover city_zottegem leftover WZC/VAPH/CIK 2512-2514; leftover WZC/VAPH/CAR/CIK of city_scherpenheuvel_zichem still unused-looking; NOT De Vlaspit Dienstencheques sister; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "De Vlaspit",
    "name_fr": "ASBL De Vlaspit",
    "name_en": "De Vlaspit VZW (leftover city_scherpenheuvel_zichem leftover maatwerk)",
    "level": "parastatal",
    "parent_id": "city_scherpenheuvel_zichem",
    "community_language": "nl",
    "website": "https://www.devlaspit.be/",
    "foi_email": "info@devlaspit.be",
    "foi_postal": "Basilieklaan 53 3270 Scherpenheuvel-Zichem",
    "notes": "tick2515 YE2025 Strong official native NBB PDF deposit 2026-00196614 + Strong KBO 0461.019.224 Actief 4 VE; omzet70 JUMP 2246566 (not commercial-only vs 73 JUMP 1618984); 76A JUMP 9800; envelope omzet70 JUMP 2246566; 70/76A JUMP 2256366; bruto9900 JUMP 2796278; pnl FLIP LOSS -49340; 9901 FLIP LOSS -48031; equity DROP 1219243; assets DROP 2398819; debt DROP 1136291; FTE JUMP 63.3; kapitaalsubsidies DROP 150107; destin691 empty; cash JUMP 862927; geldbeleggingen DROP empty (was 650000); leftover city_scherpenheuvel_zichem leftover maatwerk 4 VE official zetel Scherpenheuvel-Zichem; prior-year identical; NOT De Vlaspit Dienstencheques 0463.655.941 sister; NOT leftover-via-VE Diest of a Diest-seated parent; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_vlaspit_scherpenheuvel_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2246566", "amount_min_eur": "2246566", "amount_max_eur": "2246566", "basis": "NBB VKT-VZW code 70 omzet YE2025 JUMP +3.25% (not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 2175928; envelope omzet70 2246566 JUMP because VZW and 70 present and not commercial-only vs 73 JUMP 1618984; FOI WEWIS/VDAB/Scherpenheuvel-Zichem matrix behind 70 vs 73"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1618984", "amount_min_eur": "1618984", "amount_max_eur": "1618984", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +11.41%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 1453185; FOI WEWIS/VDAB matrix behind JUMP 1618984"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2246566", "amount_min_eur": "2246566", "amount_max_eur": "2246566", "basis": "NBB VKT-VZW envelope omzet70 YE2025 JUMP +3.25% (VZW because 70 present and not commercial-only vs 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 2175928; 70 2246566 JUMP; 73 1618984 JUMP; 76A 9800 JUMP; 70/76A 2256366 JUMP"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "9800", "amount_min_eur": "9800", "amount_max_eur": "9800", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +517.13%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 1588; 76B empty"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-49340", "amount_min_eur": "-49340", "amount_max_eur": "-49340", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was 168871)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 168871; bedrijfswinst 9901 -48031 FLIP LOSS; destin691 empty"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "-48031", "amount_min_eur": "-48031", "amount_max_eur": "-48031", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP LOSS (was 177754)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p5 native; YE2024 177754; 62 2615515 JUMP; 630 198381 JUMP; 66A 13038 JUMP; 640/8 13849 JUMP; 635/9 empty (was -51714); 631/4 3525 JUMP"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1219243", "amount_min_eur": "1219243", "amount_max_eur": "1219243", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -6.40%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p4 native; YE2024 1302586; kapitaalsubsidies 15 150107 DROP; fondsen 10 empty; overgedragen 14 949136 DROP; bestemde 13 120000"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "2398819", "amount_min_eur": "2398819", "amount_max_eur": "2398819", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -4.21%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p3 native; YE2024 2504219; MVA 22/27 1149004 JUMP; cash 862927 JUMP; geldbeleggingen empty DROP (was 650000); aanbouw 27 empty; capex 331386"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "1136291", "amount_min_eur": "1136291", "amount_max_eur": "1136291", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.90%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p4 native; YE2024 1158347; 17 105222 DROP; 42/48 991113 JUMP; 178/9 empty; voorzieningen 16 43286"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "862927", "amount_min_eur": "862927", "amount_max_eur": "862927", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +155.63%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p3 native; YE2024 337575; geldbeleggingen 50/53 empty DROP (was 650000); combined liquidity 862927 JUMP vs prior 987575; capex 331386"},
    {"budget_id": "bud_vlaspit_scherpenheuvel_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2515; PDF p6 native; YE2024 691 empty; 791 empty; 9905 -49340 overgedragen to 14"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
