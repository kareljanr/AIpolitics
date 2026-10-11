from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2543_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_iona_nijlen_jr2025_nbb_pdf_2543"
SRC_KBO = "src_iona_nijlen_kbo_2543"
SRC_SBM = "src_iona_nijlen_sbm_2543"
SRC_SITE = "src_iona_nijlen_site_2543"
EID = "vzw_iona_nijlen"
GAP = "gap_iona_nijlen_vaph_matrix_bruto_jump_5_57m_9901_jump_219k_pnl_jump_96k_cash_jump_150k_l5"
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
        if _row.get("entity_id") == EID or "0410.269.814" in blob or "0410269814" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Iona deposit 2026-00186964",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00186964.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2543; official native statutory PDF 56658 bytes 15p VKT-VZW 25.0.13 m04-f; header 23/06/2026; AV 06.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-23 12:54:23 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN 2026-00186964 56658 MD5 097f1e869f5418361d45fc277ee08cdb; NBB consult HTML stub 5344 B discarded; NBB broker 403; VKT-VZW 6.5 6.6 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee; NOT Xerox SCAN",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Iona voor heilpedagogie en sociaaltherapie 0410.269.814",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410269814",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2543; Actief since 07.10.1966; 1 VE leftover city_nijlen (official zetel Nieuwe Bevelsesteenweg(Kessel) 66 2560 Nijlen since 01.10.1990; VE 2.154.453.934 Iona vzw Nieuwe Bevelsesteenweg(Kessel) 66 2560 Nijlen since 14.06.2006 adres since 23.04.2010); VZW since 07.10.1966; RSZ2025 87.201 Instellingen met huisvesting voor minderjarigen met een mentale handicap; leftover mined city_nijlen leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover AGB Nijlen 0863.925.550; NOT leftover-via-VE; leftover city_nijlen leftover VAPH with official zetel Nijlen IS enough",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Iona 0410269814 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0410269814",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2543; deposit-id 2026-00186964 YE 01.01.2025-31.12.2025 filing VKT-VZW header 23.06.2026 AV 06.06.2026; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB consult HTML stub 5344 B discarded; NBB broker 403; deposit-id from Northdata Cbso publication discovery-only unused for euros; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Iona Nijlen FOI contact leftover city_nijlen leftover VAPH",
        "url": "https://www.vaph.be/organisaties/adressen/iona",
        "publisher": "Official VAPH adreslijst leftover city_nijlen leftover VAPH 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2543; FOI info@ionavzw.be from official YE2025 PDF + official VAPH; leftover mined city_nijlen leftover VAPH leftover-mined AGB-only unused leftover type after Aalternatief 0 deposits Apojo remine@2336 Therapiedier 0 deposits Kodiel 0 deposits Blend BV commercial Madee leftover-via-VE Turnhout CARrewiel/VERBINT remine Megusta/Rommeshoef BV Toontjeshuis holding CV Ter Loke YE2024 SoulHorses small leftover city_lille leftover city_rotselaar leftover VAPH De Plek remine@2541 leftover city_landen leftover VAPH Bindkracht remine@2542 leftover city_diest leftover VAPH Martine Van Camp remine@2540 leftover WZC Annendael@2535 leftover city_pelt leftover maatwerk NLOA remine@2539 leftover city_maasmechelen leftover maatwerk SBM remine@2538 leftover CIK HARD SKIP leftover CAR website wander HARD SKIP leftover KBO-activity HARD SKIP leftover city_bonheiden leftover hospital Imelda 403 leftover city_oud_heverlee leftover WZC De Kouter Korian SKIP; NOT leftover-via-VE; NOT Armonea; NOT Korian; NOT Vulpia; FIRST LOCK leftover city_nijlen leftover VAPH",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
