from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2531_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_capenberg_boechout_jr2025_nbb_pdf_2531"
SRC_KBO = "src_capenberg_boechout_kbo_2531"
SRC_SBM = "src_capenberg_boechout_sbm_2531"
SRC_SITE = "src_capenberg_boechout_site_2531"
EID = "vzw_capenberg_boechout"
GAP = "gap_capenberg_boechout_wzc_matrix_73_jump_1_39m_9901_jump_200k_cash_drop_553k_l5"
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
        if _row.get("entity_id") == EID or "0408.159.370" in blob or "0408159370" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VOL-VZW jaarrekening 2025 Capenberg Oxaco-Center deposit 2026-00166949",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00166949.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2531; official native statutory PDF 894124 bytes 38p VOL-VZW 25.0.12 m05-f; header 10/06/2026; AV 07.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-17 06:15:33 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00166949 894124 MD5 ae6aa002a1202a434f53dad538a33347; NBB UUID f5a5610d-46e4-11f1-9926-6f83ef8463d5; NBB consult HTML stub 5344 B discarded; NBB published-deposits list 20 this tick; prior-year identical not restated; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO VZW Capenberg Oxaco-Center 0408.159.370",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408159370",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2531; Actief since 07.03.1971; 1 VE leftover city_boechout (official zetel Borsbeeksesteenweg 45 2530 Boechout since 29.03.1981; VE 2.154.473.235 Capenberg Oxaco-Center vzw Borsbeeksesteenweg 45 since 15.06.2006); VZW since 07.03.1971; naam Capenberg, Oxaco-Center since 07.03.1971; RSZ-werkgever since 01.07.1971; RSZ2025 87.101 Rust- en verzorgingstehuizen (RVT); official WZC list Boechout Huize Stracke VZW Capenberg Oxaco-Center 0408159370 / CoBRHA 115.102 / HCO 3766 / 75 woongelegenheden; leftover mined city_boechout leftover WZC leftover-mined AGB-only unused leftover type; NOT leftover WZC Avondvrede NV 0446.506.836 remine@2166 Anima commercial SKIP; NOT leftover WZC Sint-Mathildis De Medemens 0428.692.191 leftover-via-VE Antwerpen remine@2086 SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Capenberg Oxaco-Center 0408159370 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0408159370",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2531; deposit-id 2026-00166949 YE 01.01.2025-31.12.2025 filing VOL-VZW Initial header 10.06.2026; NBB UUID f5a5610d-46e4-11f1-9926-6f83ef8463d5; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB published-deposits list 20 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "WZC Huize Stracke Capenberg Oxaco-Center FOI contact leftover city_boechout leftover WZC",
        "url": "https://www.capenberg.com/",
        "publisher": "VZW Capenberg Oxaco-Center leftover city_boechout leftover WZC 1 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2531; FOI m.roggen@capenberg.com from official YE2025 PDF; site https://www.capenberg.com/; leftover mined city_boechout leftover WZC leftover-mined AGB-only unused leftover type after leftover city_zaventem leftover WZC taken@2530 leftover maatwerk TWI remine@2282 leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 m140-f-p CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover city_boechout leftover WZC Avondvrede remine@2166 leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_willebroek leftover WZC Seniorplaza YE2025 unused leftover city_deinze leftover WZC Sint-Jozef YE2025 unused leftover VAPH taken@2496/2499; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT leftover WZC Avondvrede remine@2166; NOT leftover WZC De Medemens leftover-via-VE remine@2086",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
