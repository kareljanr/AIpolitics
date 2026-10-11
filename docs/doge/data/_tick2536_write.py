from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2536_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_terluchte_oostkamp_jr2025_nbb_pdf_2536"
SRC_KBO = "src_terluchte_oostkamp_kbo_2536"
SRC_SBM = "src_terluchte_oostkamp_sbm_2536"
SRC_SITE = "src_terluchte_oostkamp_site_2536"
EID = "vzw_terluchte_oostkamp"
GAP = "gap_terluchte_oostkamp_wzc_matrix_70_jump_6_15m_73_jump_1_10m_pnl_drop_25k_cash_jump_901k_l5"
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
        if _row.get("entity_id") == EID or "0738.896.510" in blob or "0738896510" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Ter Luchte deposit 2026-00183286",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00183286.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2536; official native statutory PDF 991421 bytes 44p VOL-VZW 26.0.15 m05-f; header 22/06/2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-22 22:59:44 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00183286 991421 MD5 519c80b774e0cab01dec01976a05251c; NBB UUID 15a8c037-5430-11f1-9c8e-fbff5c899bf3; NBB published-deposits list 6 this tick with sort=depositDate,desc; prior-year RESTATED not identical; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.7 6.10 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Ter Luchte 0738.896.510",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0738896510",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2536; Actief since 07.12.2019; 1 VE leftover city_oostkamp (official zetel Sint-Elooisstraat 87 8020 Oostkamp since 07.12.2019; VE 2.296.823.309 Ter Luchte Sint-Elooisstraat 87 8020 Oostkamp since 01.01.2020); VZW since 07.12.2019; naam Ter Luchte since 07.12.2019; RSZ-werkgever since 01.01.2020; RSZ2025 87.301 Rusthuizen voor ouderen (ROB); leftover mined city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover AGB Oostkamp 0894.294.369; NOT leftover WZC Sint-Jozef Groep Zorg H. Familie 0414.693.113 remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie; NOT leftover-via-VE of a DIFFERENT leftover city",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Ter Luchte 0738896510 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0738896510",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2536; deposit-id 2026-00183286 YE 01.01.2025-31.12.2025 filing VOL-VZW XBRL Initial header 22.06.2026; NBB UUID 15a8c037-5430-11f1-9c8e-fbff5c899bf3; NBB company zetel Sint-Elooisstraat 87 8020 Oostkamp VZW 017; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 6 this tick; NBB consult HTML stub 5344 B discarded; NBB broker without /api 5344 B discarded; NBB /api/external/broker PDF 991421; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Ter Luchte FOI contact leftover city_oostkamp leftover WZC",
        "url": "https://terluchte.be/contact",
        "publisher": "VZW Ter Luchte leftover city_oostkamp leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2536; FOI info@terluchte.be from official site https://terluchte.be/contact; leftover mined city_oostkamp leftover WZC leftover-mined AGB-only unused leftover type after leftover city_diest leftover WZC taken leftover hospital same KBO Annendael SKIP leftover VAPH/CAR/maatwerk unused-looking leftover CIK HARD SKIP leftover WZC type now taken leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover WZC Sint-Jozef Groep Zorg H. Familie remine@2057 leftover-via-VE of already-mined Groep Zorg H. Familie; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_oostkamp leftover WZC",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
