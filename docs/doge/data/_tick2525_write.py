from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2525_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_het_laar_wingene_jr2025_nbb_pdf_2525"
SRC_KBO = "src_het_laar_wingene_kbo_2525"
SRC_SBM = "src_het_laar_wingene_sbm_2525"
SRC_SITE = "src_het_laar_wingene_site_2525"
EID = "vzw_het_laar_wingene"
GAP = "gap_het_laar_wingene_wzc_matrix_70_jump_6_63m_73_jump_943k_pnl_drop_216k_cash_jump_2_39m_l5"
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
        if _row.get("entity_id") == EID or "0469.123.870" in blob or "0469123870" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Het Laar Wingene deposit 2026-00216674",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00216674.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2525; official native statutory PDF 624059 bytes 49p VOL-VZW 25.0.13 m05-f; header 25/06/2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-30 00:43:10 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00216674 GET 200 624059 MD5 990c02147ba0043a5baad771a500c330; NBB UUID 0d5c4534-5f4c-11f1-a87c-69329edd0987; NBB broker PDF GET 200 624059 same MD5; NBB ids list 21 / nonmig 6 this tick; NBB published-deposits list 500 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.16 niet dienstig; Companyweb last deposit 30.06.2026 YE2025 discovery-only unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Het Laar 0469.123.870",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0469123870",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2525; Actief since 16.09.1999; 1 VE leftover city_wingene (official zetel Pastorijstraat 56 8750 Wingene since 01.01.2025 technical; VE 2.156.465.594 Woon- en verzorgingscentrum Maria ter Ruste Pastorijstraat 56 since 05.10.2006); VZW since 16.09.1999; naam Het Laar since 01.09.2020; RSZ2025 87.301 Rusthuizen voor ouderen (ROB); official WZC list Wingene Het Laar VZW 0469123870; leftover mined city_wingene leftover WZC leftover-mined AGB-only; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_wichelen leftover WZC Torkenshof remine@2521; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Het Laar 0469123870 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0469123870",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2525; deposit-id 2026-00216674 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 25/06/2026; NBB UUID 0d5c4534-5f4c-11f1-a87c-69329edd0987; NBB ids list 21 this tick; CDN+broker PDF used for euros; ZIP/XBRL not used for euros; Companyweb last deposit 30.06.2026 YE2025 discovery-only unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Het Laar FOI contact leftover city_wingene leftover WZC",
        "url": "https://www.hetlaar.gvo.be/nl/",
        "publisher": "Het Laar VZW leftover city_wingene leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2525; FOI hetlaar@gvo.be from official site https://www.hetlaar.gvo.be/nl/ + Zorgnet-Icuro; leftover mined city_wingene leftover WZC leftover-mined AGB-only after leftover city_bertem leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine@2523 leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken; leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
