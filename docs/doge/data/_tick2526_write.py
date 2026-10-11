from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2526_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_wzga_arendonk_jr2025_nbb_pdf_2526"
SRC_KBO = "src_wzga_arendonk_kbo_2526"
SRC_SBM = "src_wzga_arendonk_sbm_2526"
SRC_SITE = "src_wzga_arendonk_site_2526"
EID = "vzw_wzga_arendonk"
GAP = "gap_wzga_arendonk_wzc_matrix_70_jump_9_98m_73_jump_2_45m_pnl_jump_632k_equity_jump_719k_l5"
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
        if _row.get("entity_id") == EID or "0696.665.975" in blob or "0696665975" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 WoonZorgGroep Arendonk deposit 2026-00239172",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00239172.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2526; official native statutory PDF 1518630 bytes 46p VOL-VZW 26.0.15 m05-f; header 30/06/2026; AV 03.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-02 10:20:25 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00239172 GET 200 1518630 MD5 6b14d767955983fcd95448d80976c3d9; NBB UUID e1261a45-1d47-11f1-b8ca-cb873e0b731e; NBB broker PDF 403 this tick; NBB ids list 8 / nonmig 5 this tick; NBB published-deposits list 200 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.10 6.13 6.16 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO WoonZorgGroep Arendonk 0696.665.975",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0696665975",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2526; Actief since 22.05.2018; 2 VE leftover city_arendonk (official zetel Vrijheid 100 2370 Arendonk since 22.05.2018; VE 2.276.165.178 De Vrijheid Vrijheid 100 since 01.07.2018 + VE 2.330.503.192 Bellekens Bellekens 10 since 28.04.2022); VZW since 22.05.2018; afkorting WZGA since 22.05.2018; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official WZC list Arendonk WZGA VZW 0696665975 163 woongelegenheden HCO 3667; leftover mined city_arendonk leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover city_wingene leftover WZC Het Laar remine@2525; NOT leftover city_wingene leftover WZC Curando remine@2046; NOT leftover city_wingene leftover WZC Amphora unused leftover WZC type now taken; NOT leftover city_meerhout leftover maatwerk DE SPRONG remine@2286; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche WoonZorgGroep Arendonk 0696665975 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0696665975",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2526; deposit-id 2026-00239172 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 30/06/2026; NBB UUID e1261a45-1d47-11f1-b8ca-cb873e0b731e; NBB ids list 8 this tick; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB broker PDF 403 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "WZGA FOI contact leftover city_arendonk leftover WZC",
        "url": "https://wzga.be/",
        "publisher": "WoonZorgGroep Arendonk VZW leftover city_arendonk leftover WZC 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2526; FOI info@wzga.be from official site https://wzga.be/ + official KBO email since 28.04.2022; leftover mined city_arendonk leftover WZC leftover-mined AGB-only unused leftover type after leftover city_wingene leftover WZC Het Laar@2525 leftover WZC Curando remine@2046 leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP leftover VAPH t Volderke SCAN leftover CAR/CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
