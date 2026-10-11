from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2541_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_de_plek_rotselaar_jr2025_nbb_pdf_2541"
SRC_KBO = "src_de_plek_rotselaar_kbo_2541"
SRC_SBM = "src_de_plek_rotselaar_sbm_2541"
SRC_SITE = "src_de_plek_rotselaar_site_2541"
EID = "vzw_de_plek_rotselaar"
GAP = "gap_de_plek_rotselaar_vaph_matrix_bruto_drop_8964_omzet_drop_17185_73_jump_2322_cash_jump_12686_l5"
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
        if _row.get("entity_id") == EID or "0822.360.357" in blob or "0822360357" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB MIC-VZW jaarrekening 2025 De Plek deposit 2026-00317818",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00317818.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2541; official native statutory PDF 34977 bytes 8p MIC-VZW 26.0.15 m08-f; header 22/07/2026; AV 28.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-22 20:34:21 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00317818 34977 MD5 02fead2e68d2faa0370e1fe0ef97b547; NBB UUID 881dc344-860b-11f1-b284-3baacb2f7291; MIC-VZW 6.1.1 6.1.3 6.2 6.3 6.4 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW De Plek 0822.360.357",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0822360357",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2541; Actief since 12.01.2010; 1 VE leftover city_rotselaar (official zetel Hanewijk 44A 3118 Rotselaar since 01.10.2012; VE 2.228.262.719 Hanewijk 44A 3118 Rotselaar/Werchter); VZW since 12.01.2010; RSZ2025 88.106 Activiteiten van dagcentra voor volwassenen met een mentale handicap; leftover mined city_rotselaar leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB Rotselaar 0865.782.903; NOT leftover-via-VE; leftover city_rotselaar leftover VAPH with official zetel Rotselaar IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche De Plek 0822360357 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0822360357",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2541; deposit-id 2026-00317818 YE 01.01.2025-31.12.2025 filing MIC-VZW header 22.07.2026 AV 28.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB rs-consult published-deposits/ids + broker PDF; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "De Plek Rotselaar FOI contact leftover city_rotselaar leftover VAPH",
        "url": "https://www.vaph.be/organisaties/adressen/de-plek-0",
        "publisher": "Official VAPH adreslijst leftover city_rotselaar leftover VAPH 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2541; FOI deplek@telenet.be from official VAPH (KBO/PDF email empty); leftover mined city_rotselaar leftover VAPH leftover-mined AGB-only unused leftover type after Noorderhart Pelt SCAN Xerox SKIP Toontjeshuis Schelle holding CV NACE 64.210 SKIP Hoeve Megusta/Rommeshoef BV MIC-inb commercial SKIP Ter Loke/Bindkracht/Den Ateljee YE2024-only SKIP Aalternatief 0 deposits SKIP Klaverhof Agten CommV farm SKIP leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael@2535 leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_rotselaar leftover VAPH",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
