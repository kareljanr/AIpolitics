from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2530_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_consolata_zaventem_jr2025_nbb_pdf_2530"
SRC_KBO = "src_consolata_zaventem_kbo_2530"
SRC_SBM = "src_consolata_zaventem_sbm_2530"
SRC_SITE = "src_consolata_zaventem_site_2530"
EID = "vzw_consolata_zaventem"
GAP = "gap_consolata_zaventem_wzc_matrix_70_jump_8_97m_9901_flip_86k_pnl_jump_109k_equity_drop_7_53m_l5"
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
        if _row.get("entity_id") == EID or "0457.206.827" in blob or "0457206827" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Consolata Regio Zaventem deposit 2026-00259909",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00259909.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2530; official native statutory PDF 521538 bytes 44p VOL-VZW 26.0.15 m05-f; header 06/07/2026; AV 23.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-07 06:40:07 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00259909 521538 MD5 9a7e627ded3e95b52e55bcfe77a191f4; NBB UUID bc7e936d-7937-11f1-b790-35cb631eb602; NBB consult HTML stub 5344 B discarded; NBB published-deposits list 200 this tick; prior-year identical not restated; VOL-VZW 6.2.1 6.2.3 6.2.4 6.3.4 6.3.6 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Consolata Regio Zaventem 0457.206.827",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0457206827",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2530; Actief since 11.12.1995; 1 VE leftover city_zaventem (official zetel Hoogstraat 52 1930 Zaventem since 25.07.2001; VE 2.150.785.948 Consolata Regio Zaventem Hoogstraat 52 since 03.01.2006); VZW since 11.12.1995; naam Consolata Regio Zaventem since 11.12.1995; RSZ-werkgever since 01.01.1996; Aanbestedende overheid since 11.12.1995; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official WZC list Zaventem Sint-Antonius VZW Consolata Regio Zaventem 0457206827 / CoBRHA HCO 3630 / 127 woongelegenheden; leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover city_putte leftover WZC CONSOLATA 0457.207.223 remine@2529 SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Consolata Regio Zaventem 0457206827 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0457206827",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2530; deposit-id 2026-00259909 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 06.07.2026; NBB UUID bc7e936d-7937-11f1-b790-35cb631eb602; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 200 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "WZC Sint-Antonius Consolata Regio Zaventem FOI contact leftover city_zaventem leftover WZC",
        "url": "https://www.sintantoniuszaventem.be/",
        "publisher": "VZW Consolata Regio Zaventem leftover city_zaventem leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2530; FOI kristien.vogelaers@sintantoniuszaventem.be from official YE2025 PDF; site https://www.sintantoniuszaventem.be/; leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type after leftover city_putte leftover WZC taken@2529 leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial leftover WZC Gerkenberg@2528 leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_zaventem leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT leftover city_putte leftover WZC CONSOLATA remine@2529",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
