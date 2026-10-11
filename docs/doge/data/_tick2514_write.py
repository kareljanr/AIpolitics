from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2514_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sint_elisabeth_zottegem_jr2025_nbb_pdf_2514"
SRC_KBO = "src_sint_elisabeth_zottegem_kbo_2514"
SRC_SBM = "src_sint_elisabeth_zottegem_sbm_2514"
SRC_SITE = "src_sint_elisabeth_zottegem_site_2514"
EID = "vzw_kdv_sint_elisabeth_zottegem"
GAP = "gap_sint_elisabeth_zottegem_cik_matrix_70_76A_822k_73_jump_811k_pnl_drop_30k_cash_drop_66k_l5"
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

import csv as _csv
_csv.field_size_limit(10_000_000)
with (DATA / "entities.csv").open(encoding="utf-8") as _fh:
    for _row in _csv.DictReader(_fh):
        if _row.get("entity_id") == EID:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Sint-Elisabeth Zottegem deposit 2026-00271050",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00271050.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2514; official native statutory PDF 638924 bytes 17p VKT-VZW 25.0.13 m04-f; header 06/07/2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-09 06:33:49 UTC OpenPDF 1.3.26; CDN Last-Modified 29.07.2026; statutory pages native; CDN 2026-00271050 GET 200 638924 MD5 d18f3327c5e3d4bd94c836c2b319d23a; prior-year identical not restated; no commissaris on VKT-VZW 2; VKT-VZW 6.2 6.5 6.6 7 8 niet dienstig; NBB published-deposits/ids 403 this tick; NBB broker 403 discarded; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Kinderdagverblijf Sint-Elisabeth Zottegem 0452.614.767",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0452614767",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2514; Actief since 22.04.1994; 1 VE 2.157.304.942 leftover city_zottegem (official zetel Godveerdegemstraat 69 9620 Zottegem since 15.10.2004; VE Godveerdegemstraat 67 since 14.11.2006); VZW since 22.04.1994; BTW since 01.11.2017; RSZ since 01.10.1997; BTW2025 88.911; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover mined city_zottegem leftover CIK; NOT De Hoop 0870.779.490 leftover VAPH@2513; NOT De Bron 0892.673.479 leftover WZC@2512; NOT WZC Egmont OCMW 0212.187.302; NOT De Bolster 0861.680.989 leftover-via-VE Zwalm; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Kinderdagverblijf Sint-Elisabeth 0452614767 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0452614767",
        "publisher": "NBB Consult / SBM",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2514; deposit-id 2026-00271050 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial neerlegging 09.07.2026; SBM fiche + Companyweb last-balansjaar 2025 + neerlegging 09.07.2026 used for deposit-id discovery; Companyweb last-balansjaar 2025 discovery OK euros NOT OK; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Kinderdagverblijf Sint-Elisabeth / Piet Konijn FOI contact leftover city_zottegem leftover CIK",
        "url": "https://www.sezz.be/over-ons/samenwerkingen/",
        "publisher": "AZ Sint-Elisabeth Zottegem SEZZ / leftover city_zottegem leftover CIK 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2514; FOI yvan.lenssens@sezz.be from official NBB PDF header / piet.konijn@sezz.be from official kinderopvangwijzer; leftover mined city_zottegem leftover CIK after leftover city_zottegem leftover WZC De Bron@2512 + leftover VAPH De Hoop@2513; CoBRHA HCO 910000749 Piet Konijn groepsopvang; NOT De Hoop leftover VAPH; NOT De Bron leftover WZC; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
    },
], src_fields)
print("sources ok")

ent_fields = ["entity_id", "name_nl", "name_fr", "name_en", "level", "parent_id", "community_language", "website", "foi_email", "foi_postal", "notes"]
append_rows(DATA / "entities.csv", [{
    "entity_id": EID,
    "name_nl": "Kinderdagverblijf Sint-Elisabeth, Zottegem",
    "name_fr": "Creche Sainte-Elisabeth Zottegem ASBL",
    "name_en": "Kinderdagverblijf Sint-Elisabeth VZW (leftover city_zottegem leftover CIK)",
    "level": "parastatal",
    "parent_id": "city_zottegem",
    "community_language": "nl",
    "website": "https://www.sezz.be/over-ons/samenwerkingen/",
    "foi_email": "yvan.lenssens@sezz.be",
    "foi_postal": "Godveerdegemstraat 69 9620 Zottegem",
    "notes": "tick2514 YE2025 Strong official native NBB PDF deposit 2026-00271050 + Strong KBO 0452.614.767 Actief 1 VE; omzet70 JUMP 10657 (commercial-only vs large 73 JUMP 811093); 76A DROP 448; envelope 70/76A JUMP 822198; bruto9900 JUMP 750639; pnl DROP 29849; 9901 DROP 26552; equity JUMP 360023; assets JUMP 690321; debt JUMP 330298; FTE DROP 9.8; kapitaalsubsidies DROP 75221; destin691 empty; cash DROP 65765; geldbeleggingen JUMP 275000; leftover city_zottegem leftover CIK 1 VE official zetel Zottegem; prior-year identical; NOT De Hoop leftover VAPH@2513; NOT De Bron leftover WZC@2512; NOT WZC Egmont OCMW; NOT De Bolster leftover-via-VE Zwalm; NOT leftover-via-VE Brussels/Hasselt/Gent; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; not TE-additive",
}], ent_fields)

bud_fields = ["budget_id", "entity_id", "year", "amount_eur", "amount_min_eur", "amount_max_eur", "basis", "source_id", "confidence", "notes"]
append_rows(DATA / "budgets.csv", [
    {"budget_id": "bud_sint_elisabeth_zottegem_omzet_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "10657", "amount_min_eur": "10657", "amount_max_eur": "10657", "basis": "NBB VKT-VZW code 70 omzet YE2025 JUMP +5.45% (commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 10106; envelope 70/76A 822198 JUMP because VZW and omzet commercial-only vs large 73; FOI Opgroeien/Zottegem/SEZZ matrix behind 70 vs 73"},
    {"budget_id": "bud_sint_elisabeth_zottegem_73_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "811093", "amount_min_eur": "811093", "amount_max_eur": "811093", "basis": "NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +1.91%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 795913; FOI Opgroeien matrix behind JUMP 811093"},
    {"budget_id": "bud_sint_elisabeth_zottegem_opbr_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "822198", "amount_min_eur": "822198", "amount_max_eur": "822198", "basis": "NBB VKT-VZW envelope 70/76A YE2025 JUMP +1.82% (VZW because omzet commercial-only vs large 73)", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 807533; 70 10657 JUMP; 73 811093 JUMP; 76A 448 DROP"},
    {"budget_id": "bud_sint_elisabeth_zottegem_76A_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "448", "amount_min_eur": "448", "amount_max_eur": "448", "basis": "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -70.41%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 1514; 76B empty"},
    {"budget_id": "bud_sint_elisabeth_zottegem_pnl_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "29849", "amount_min_eur": "29849", "amount_max_eur": "29849", "basis": "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -63.47%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 81721; bedrijfswinst 9901 26552 DROP; destin691 empty"},
    {"budget_id": "bud_sint_elisabeth_zottegem_bedrijfswinst_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "26552", "amount_min_eur": "26552", "amount_max_eur": "26552", "basis": "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -65.72%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p6 native; YE2024 77460; 62 671815 JUMP; 630 41303 JUMP; 66A 3143 JUMP; 640/8 7826 DROP; 635/9 empty; 631/4 empty"},
    {"budget_id": "bud_sint_elisabeth_zottegem_equity_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "360023", "amount_min_eur": "360023", "amount_max_eur": "360023", "basis": "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +4.57%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p5 native; YE2024 344278; kapitaalsubsidies 15 75221 DROP; fondsen 10 empty; overgedragen 14 284802 JUMP"},
    {"budget_id": "bud_sint_elisabeth_zottegem_assets_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "690321", "amount_min_eur": "690321", "amount_max_eur": "690321", "basis": "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.59%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p4 native; YE2024 647617; MVA 22/27 262988 DROP; cash 65765 DROP; geldbeleggingen 275000 JUMP; aanbouw 27 8218 JUMP; capex 28646"},
    {"budget_id": "bud_sint_elisabeth_zottegem_debt_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "330298", "amount_min_eur": "330298", "amount_max_eur": "330298", "basis": "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +8.89%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p5 native; YE2024 303339; 17 114560 DROP; 42/48 213828 JUMP; 178/9 114560; voorzieningen 16 empty"},
    {"budget_id": "bud_sint_elisabeth_zottegem_cash_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "65765", "amount_min_eur": "65765", "amount_max_eur": "65765", "basis": "NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -27.65%", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p4 native; YE2024 90893; geldbeleggingen 50/53 275000 JUMP (was 200000); combined liquidity 340765 JUMP; capex 28646"},
    {"budget_id": "bud_sint_elisabeth_zottegem_destin_jr2025_statutory", "entity_id": EID, "year": "2025", "amount_eur": "0", "amount_min_eur": "0", "amount_max_eur": "0", "basis": "NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty", "source_id": SRC_PDF, "confidence": "strong", "notes": "tick2514; PDF p7 native; YE2024 691 empty; 791 empty; 9905 29849 overgedragen to 14"},
], bud_fields)
print("entities+budgets ok")
print("CORE1 DONE")
