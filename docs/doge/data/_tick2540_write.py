from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2540_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_mvc_diest_jr2025_nbb_pdf_2540"
SRC_KBO = "src_mvc_diest_kbo_2540"
SRC_SBM = "src_mvc_diest_sbm_2540"
SRC_SITE = "src_mvc_diest_site_2540"
EID = "vzw_martine_van_camp_diest"
GAP = "gap_mvc_diest_vaph_matrix_70_76A_jump_12_92m_73_jump_10_99m_cash_jump_1_24m_l5"
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
        if _row.get("entity_id") == EID or "0424.784.378" in blob or "0424784378" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Martine Van Camp deposit 2026-00289013",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00289013.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2540; official native statutory PDF 1506025 bytes 47p VOL-VZW 25.0.13 m05-f; header 14/07/2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-14 09:09:51 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00289013 1506025 MD5 75cce184977c348bf2c49dc9f738e092; NBB UUID 1e6d48fa-3ee4-11f1-931a-0d7dcef9e89f; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.18 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Martine Van Camp 0424.784.378",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0424784378",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2540; Actief since 01.07.1983; 1 VE leftover city_diest (official zetel Turnhoutsebaan 57 3294 Diest since 01.07.1983; VE 2.155.046.723 Martine Van Camp vzw Turnhoutsebaan 57 3294 Diest since 12.07.2006); VZW since 01.07.1983; naam Martine Van Camp since 26.10.1995; RSZ-werkgever since 01.07.1983; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; leftover mined city_diest leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB CC Diest 0845.332.432; NOT leftover WZC Annendael 0414.604.526 remine@2535; NOT leftover-via-VE; leftover city_diest leftover VAPH with official zetel Diest IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Martine Van Camp 0424784378 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0424784378",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2540; deposit-id 2026-00289013 YE 01.01.2025-31.12.2025 filing VOL-VZW header 14.07.2026 AV 18.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B unused this tick; NBB rs-consult published-deposits listed YE2025; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Martine Van Camp Diest FOI contact leftover city_diest leftover VAPH",
        "url": "https://www.vaph.be/organisaties/diensten-rechtstreeks-toegankelijke-hulp-rth-aanbieders/martine-van-camp",
        "publisher": "Official VAPH + site martinevancamp.be leftover city_diest leftover VAPH 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2540; FOI info@martinevancamp.be from official VAPH + site https://www.martinevancamp.be/contact (KBO/PDF email empty); leftover mined city_diest leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_aalter leftover VAPH Aalternatief YE none SKIP leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover city_diest leftover VAPH Martine Van Camp YE2024 SKIP@2538/2539 now YE2025 native leftover WZC Annendael@2535 leftover hospital same KBO SKIP leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE leftover CIK HARD SKIP leftover city_oostkamp leftover VAPH leftover-via-VE SKIP leftover maatwerk t rad remine@2537 leftover WZC Ter Luchte@2536 leftover city_willebroek leftover VAPH+WZC taken leftover CAR leftover-via-VE SKIP leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP leftover VAPH unused leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover WZC unused-not-hardskip 0 leftover-mined AGB-only leftover city_maasmechelen leftover VAPH unused-looking leftover maatwerk MAASBIJ YE2024 leftover maatwerk Kringwinkel Maasland remine leftover WZC Heyvis OCMW leftover WZC Maasmeander BV leftover city_pelt leftover VAPH unused leftover WZC unused leftover CIK HARD SKIP leftover maatwerk type now taken leftover city_diest leftover VAPH unused leftover type YE2025 now native; NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_diest leftover VAPH",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
