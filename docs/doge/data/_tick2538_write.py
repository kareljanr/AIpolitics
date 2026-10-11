from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2538_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_sbm_maasmechelen_jr2025_nbb_pdf_2538"
SRC_KBO = "src_sbm_maasmechelen_kbo_2538"
SRC_SBM = "src_sbm_maasmechelen_sbm_2538"
SRC_SITE = "src_sbm_maasmechelen_site_2538"
EID = "vzw_sbm_maasmechelen"
GAP = "gap_sbm_maasmechelen_maatwerk_matrix_bruto_drop_2_41m_9901_drop_143k_pnl_drop_142k_cash_jump_1_76m_l5"
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
        if _row.get("entity_id") == EID or "0461.814.525" in blob or "0461814525" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Sociaal Bedrijvencentrum Maasmechelen deposit 2026-00154620",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00154620.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2538; official native statutory PDF 316241 bytes 23p VKT-VZW 25.0.12 m04-f; header 10/06/2026; AV 04.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-12 01:55:06 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00154620 316241 MD5 565b30128d92a7414044a30b264c8df2; VKT-VZW 6.1.1 6.5 7 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Sociaal Bedrijvencentrum Maasmechelen 0461.814.525",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461814525",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2538; Actief since 03.07.1997; 1 VE leftover city_maasmechelen (official zetel Boorsemstraat(O) 2 3630 Maasmechelen since 10.09.2001; VE 2.154.930.917 Sociaal bedrijvencentrum Maasmechelen Boorsemstraat(O) 2 3630 Maasmechelen since 06.07.2006); VZW since 03.07.1997; naam Sociaal bedrijvencentrum Maasmechelen since 03.07.1997; RSZ-werkgever since 14.04.1998; RSZ2025 88.993 Beschutte en sociale werkplaatsen; leftover mined city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type; NOT leftover AGB Maasmechelen 0882.009.815; NOT leftover maatwerk Kringwinkel Maasland 0417.701.992 remine@2223 parent sec_flanders; NOT leftover maatwerk MAASBIJ 0465.820.031 YE2024; NOT leftover WZC Heyvis OCMW 0212.335.869; NOT leftover WZC Maasmeander BV 0844.871.384 commercial; NOT leftover-via-VE of a DIFFERENT leftover city",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Sociaal Bedrijvencentrum Maasmechelen 0461814525 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0461814525",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2538; deposit-id 2026-00154620 YE 01.01.2025-31.12.2025 filing VKT-VZW header 10.06.2026 AV 04.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub unused this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "SBM Maasmechelen FOI contact leftover city_maasmechelen leftover maatwerk",
        "url": "https://www.vzwsbm.be/",
        "publisher": "VZW Sociaal Bedrijvencentrum Maasmechelen leftover city_maasmechelen leftover maatwerk 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2538; FOI info@sociaalbedrijvencentrum.be from official YE2025 PDF + thomas.grosemans@vzwsbm.be from official KBO + site https://www.vzwsbm.be; leftover mined city_maasmechelen leftover maatwerk leftover-mined AGB-only unused leftover type after leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV commercial; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_maasmechelen leftover maatwerk",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
