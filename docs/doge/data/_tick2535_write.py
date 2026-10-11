from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2535_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_annendael_diest_jr2025_nbb_pdf_2535"
SRC_KBO = "src_annendael_diest_kbo_2535"
SRC_SBM = "src_annendael_diest_sbm_2535"
SRC_SITE = "src_annendael_diest_site_2535"
EID = "vzw_annendael_diest"
GAP = "gap_annendael_diest_wzc_matrix_70_jump_36_06m_73_jump_5_99m_pnl_flip_451k_cash_drop_8_93m_l5"
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
        if _row.get("entity_id") == EID or "0414.604.526" in blob or "0414604526" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Zorggroep Annendael deposit 2026-00283395",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00283395.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2535; official native statutory PDF 992637 bytes 53p VOL-VZW 25.0.13 m05-f; header 10/07/2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-13 07:31:35 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00283395 992637 MD5 61c986673bef29c2330d47f58757f53b; NBB UUID e1f8c3bf-4bbb-11f1-aad4-4dc89131aed6; NBB published-deposits list 8 this tick with sort=depositDate,desc; prior-year identical not restated; VOL-VZW 6.2.1 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Zorggroep Annendael 0414.604.526",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414604526",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2535; Actief since 07.09.1974; 4 VE leftover city_diest (official zetel Vestenstraat 1 3290 Diest since 07.09.1974; VE 2.143.610.324 Zorggroep Annendael Vestenstraat 1 since 01.12.2004 + VE 2.138.402.018 Huis August Fabiolalaan 2A since 07.09.1974 adres since 20.01.2025 + VE 2.205.597.678 Zorg aan huis Begijnenstraat 8 since 01.01.2012 + VE 2.138.402.117 Huis Sterre Prins Alexanderstraat 55 3270 Scherpenheuvel-Zichem since 07.09.1974 adres since 11.07.2015 leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC); VZW since 07.09.1974; naam Zorggroep Annendael since 20.05.2025; RSZ-werkgever since 01.01.1945; RSZ2025 86.104 Activiteiten van psychiatrische ziekenhuizen; BTW2025 87.205 + 86.104 + 87.301 ROB; aanbestedende overheid since 07.09.1974; leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover AGB CC Diest 0845.332.432; NOT leftover-via-VE of a DIFFERENT leftover city",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Zorggroep Annendael 0414604526 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0414604526",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2535; deposit-id 2026-00283395 YE 01.01.2025-31.12.2025 filing VOL-VZW XBRL Initial header 10.07.2026; NBB UUID e1f8c3bf-4bbb-11f1-aad4-4dc89131aed6; NBB company zetel Vestenstraat 1 3290 Diest VZW 017; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 8 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Annendael FOI contact leftover city_diest leftover WZC",
        "url": "https://annendael.be/contact/",
        "publisher": "VZW Zorggroep Annendael leftover city_diest leftover WZC 4 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2535; FOI info@annendael.be from official site https://annendael.be/contact/ + eerstelijnszone; leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type after leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_oostkamp leftover WZC Ter Luchte unused leftover WZC type unused leftover-mined AGB-only leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_diest leftover WZC",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
