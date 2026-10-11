from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2544_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_ritmica_hove_jr2025_nbb_pdf_2544"
SRC_KBO = "src_ritmica_hove_kbo_2544"
SRC_SBM = "src_ritmica_hove_sbm_2544"
SRC_SITE = "src_ritmica_hove_site_2544"
EID = "vzw_ritmica_hove"
GAP = "gap_ritmica_hove_vaph_matrix_70_76a_jump_5_42m_73_jump_5_22m_pnl_loss_narrower_53k_cash_drop_254k_l5"
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
        if _row.get("entity_id") == EID or "0408.389.794" in blob or "0408389794" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Ritmica deposit 2026-00226136",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00226136.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2544; official native statutory PDF 1348852 bytes 41p VOL-VZW 25.0.13 m05-f; header 30/06/2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-30 23:28:15 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00226136 1348852 MD5 67dcaa8ebd1cb5bad732e789d19d418e; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.16 7 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Medisch - Pedagogisch Instituut Ritmica 0408.389.794",
        "url": "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0408389794&actionLu=Rechercher",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2544; Actief since 27.05.1971; 3 VE leftover city_hove (official zetel Wouwstraat 44 2540 Hove since 20.09.1972; VE 2.154.850.644 Wouwstraat 44 2540 Hove since 04.07.2006 + VE 2.198.933.976 Kasteelstraat 28 2540 Hove since 01.01.2008 + VE 2.366.636.880 Liersesteenweg 45 2800 Mechelen since 01.01.2025 leftover-via-VE FROM leftover city_hove); VZW since 27.05.1971; RSZ2025 88.105 Activiteiten van dagcentra voor minderjarigen met een mentale handicap, met inbegrip van ambulante hulpverlening; leftover mined city_hove leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB Hove 0834.868.508; NOT leftover Stijn 0439.452.461 leftover-via-VE Hasselt; leftover city_hove leftover VAPH with official zetel Hove IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Ritmica 0408389794 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0408389794",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2544; deposit-id 2026-00226136 YE 01.01.2025-31.12.2025 filing VOL-VZW header 30.06.2026 AV 17.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Ritmica Hove FOI contact leftover city_hove leftover VAPH",
        "url": "https://www.vaph.be/organisaties/adressen/ritmica",
        "publisher": "Official VAPH adreslijst leftover city_hove leftover VAPH 3 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2544; FOI personeel@ritmica.be from official VAPH; leftover mined city_hove leftover VAPH leftover-mined AGB-only unused leftover type after Aalternatief 0 deposits Apojo remine@2336 Therapiedier 0 deposits Kodiel 0 deposits Blend BV commercial Madee leftover-via-VE Turnhout CARrewiel remine Megusta/Rommeshoef BV Toontjeshuis holding CV Ter Loke YE2024 SoulHorses leftover city_lille leftover city_nijlen leftover VAPH Iona remine@2543 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael@2535 leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover Stijn Sint-Oda/Klimroos leftover-via-VE Hasselt leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_hove leftover VAPH",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
