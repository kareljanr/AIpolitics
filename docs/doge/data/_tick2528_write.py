from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2528_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_gerkenberg_bree_jr2025_nbb_pdf_2528"
SRC_KBO = "src_gerkenberg_bree_kbo_2528"
SRC_SBM = "src_gerkenberg_bree_sbm_2528"
SRC_SITE = "src_gerkenberg_bree_site_2528"
EID = "vzw_gerkenberg_bree"
GAP = "gap_gerkenberg_bree_wzc_matrix_70_jump_3_34m_73_jump_4_76m_pnl_flip_542_cash_drop_553k_l5"
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
        if _row.get("entity_id") == EID or "0867.804.659" in blob or "0867804659" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Welzijnscampus Gerkenberg deposit 2026-00239951",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00239951.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2528; official native statutory PDF 538477 bytes 45p VOL-VZW 26.0.15 m05-f; header 01/07/2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-02 12:36:18 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00239951 GET 200 538477 MD5 8668d713ac054665b40d57594d918199; NBB consult HTML stub 5344 B discarded; NBB broker PDF 403 this tick; NBB publication-ids 403 this tick; prior-year identical not restated; VOL-VZW 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; Companyweb last-balansjaar 2025 last deposit 02.07.2026 discovery-only unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Welzijnscampus Gerkenberg 0867.804.659",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0867804659",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2528; Actief since 13.10.2004; 1 VE leftover city_bree (official zetel Meeuwerkiezel 90A 3960 Bree since 18.01.2007; VE 2.159.459.134 WELZIJNSCAMPUS GERKENBERG Meeuwerkiezel 90A since 13.02.2007 adres since 14.02.2007); VZW since 28.09.2004; naam WELZIJNSCAMPUS GERKENBERG since 28.09.2004; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official WZC list Bree Gerkenberg VZW 0867804659 / CoBRHA HCO 15723 / 95 woongelegenheden; leftover mined city_bree leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover city_bree leftover WZC Boneput SLG 0845.064.196 commercial SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Welzijnscampus Gerkenberg 0867804659 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0867804659",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2528; deposit-id 2026-00239951 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 01/07/2026; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB broker PDF 403 this tick; NBB publication-ids 403 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Welzijnscampus Gerkenberg FOI contact leftover city_bree leftover WZC",
        "url": "https://gerkenberg.be/contact/",
        "publisher": "Welzijnscampus Gerkenberg VZW leftover city_bree leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2528; FOI info@gerkenberg.be from official site https://gerkenberg.be/contact/; leftover mined city_bree leftover WZC leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC+VAPH taken leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK Dol-Fijn leftover-via-VE Turnhout SKIP leftover CIK Toverbos/Kroontje BV commercial SKIP leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Amphora unused leftover WZC type now taken leftover WZC Curando remine leftover WZC Het Laar remine; leftover city_oud_turnhout leftover maatwerk De Troef YE2024 SKIP leftover WZC Smeedeshof Armonea SKIP leftover city_middelkerke leftover WZC Haerlebout Squatina leftover-via-VE Oostende SKIP; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
