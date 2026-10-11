from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2539_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_nloa_pelt_jr2025_nbb_pdf_2539"
SRC_KBO = "src_nloa_pelt_kbo_2539"
SRC_SBM = "src_nloa_pelt_sbm_2539"
SRC_SITE = "src_nloa_pelt_site_2539"
EID = "vzw_nloa_pelt"
GAP = "gap_nloa_pelt_maatwerk_matrix_bruto_jump_2_49m_9901_drop_55k_pnl_drop_63k_cash_jump_362k_l5"
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
        if _row.get("entity_id") == EID or "0451.320.313" in blob or "0451320313" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Noord-Limburgs Open Atelier deposit 2026-00202608",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00202608.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2539; official native statutory PDF 48701 bytes 12p VKT-VZW 23.0.10 m04-f; header 26/06/2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-26 10:33:17 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00202608 48701 MD5 d25bc366b64339febef575644d35960c; VKT-VZW 6.1.1 6.2 6.5 6.6 6.8 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Noord-Limburgs Open Atelier 0451.320.313",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451320313",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2539; Actief since 20.10.1993; 2 VE leftover city_pelt (official zetel Haltstraat 90 bus 1 3900 Pelt since 01.01.2019; VE 2.154.888.949 Noord-Limburgs Open Atelier Pelt Haltstraat 90 3900 Pelt since 01.01.2019; VE 2.292.368.831 Noord-Limburgs Open Atelier Lommel Rembert Dodoensstraat 20 3920 Lommel since 01.01.2002); VZW since 20.10.1993; naam Noord-Limburgs Open Atelier since 20.10.1993; RSZ-werkgever since 01.07.1994; RSZ2025 85.591 Onderwijs voor sociale promotie; leftover mined city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type; NOT leftover AGB Pelt 0876.186.449; NOT leftover maatwerk SBM 0461.814.525 remine@2538; NOT leftover maatwerk t rad remine@2537; NOT leftover-via-VE of leftover city_lommel (extra VE only); leftover city_pelt leftover maatwerk with official zetel Pelt IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Noord-Limburgs Open Atelier 0451320313 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0451320313",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2539; deposit-id 2026-00202608 YE 01.01.2025-31.12.2025 filing VKT-VZW header 26.06.2026 AV 15.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "NLOA Pelt FOI contact leftover city_pelt leftover maatwerk",
        "url": "https://www.openatelier.be/",
        "publisher": "VZW Noord-Limburgs Open Atelier leftover city_pelt leftover maatwerk 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2539; FOI info@openatelier.be from official site https://www.openatelier.be (KBO/PDF email empty); leftover mined city_pelt leftover maatwerk leftover-mined AGB-only unused leftover type after leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV leftover VAPH unused-looking leftover city_pelt leftover maatwerk NLOA YE2024 SKIP@2538 now YE2025 native; NOT leftover-via-VE Lommel; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_pelt leftover maatwerk",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
