from pathlib import Path
import csv

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2527_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)

SRC_PDF = "src_talander_arendonk_jr2025_nbb_pdf_2527"
SRC_KBO = "src_talander_arendonk_kbo_2527"
SRC_SBM = "src_talander_arendonk_sbm_2527"
SRC_SITE = "src_talander_arendonk_site_2527"
EID = "vzw_talander_arendonk"
GAP = "gap_talander_arendonk_vaph_matrix_bruto_1_60m_omzet73_empty_pnl_jump_143k_cash_jump_1_05m_l5"
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
        if _row.get("entity_id") == EID or "0433.306.225" in blob or "0433306225" in blob:
            raise SystemExit("entity already present")

src_fields = ["source_id", "title", "url", "publisher", "accessed_date", "source_class", "notes"]
append_rows(DATA / "sources.csv", [
    {
        "source_id": SRC_PDF,
        "title": "NBB VKT-VZW jaarrekening 2025 Talander deposit 2026-00192214",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00192214.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DAY,
        "source_class": "budget",
        "notes": "tick2527; official native statutory PDF 50046 bytes 14p VKT-VZW 26.0.15 m04-f; header 24/06/2026; AV 19.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-24 13:16:42 UTC OpenPDF 1.3.26; statutory pages native; CDN 2026-00192214 GET 200 50046 MD5 8388255c29b86d1fe5b122e440c1b390; NBB consult HTML stub 5344 B discarded; NBB broker PDF 403 this tick; NBB published-deposits 403 this tick; prior-year identical not restated; VKT-VZW 6.1.1 6.5 6.6 7 8 niet dienstig; Companyweb last-balansjaar 2025 last deposit 24.06.2026 discovery-only unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
    },
    {
        "source_id": SRC_KBO,
        "title": "KBO Talander 0433.306.225",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0433306225",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DAY,
        "source_class": "official_register",
        "notes": "tick2527; Actief since 03.12.1986; 2 VE leftover city_arendonk (official zetel De Lusthoven 88 2370 Arendonk since 03.12.1986; confirmed VE 2.156.808.163 Talander De Lusthoven 88 since 18.10.2006; second VE KBO-listed list form 404 this tick leftover city_arendonk); VZW since 03.12.1986; naam Talander since 03.06.1997; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; official CoBRHA VAPH HCO 201281 De Lusthoven 88 2370 Arendonk vergunde zorgaanbieder; leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type; NOT leftover city_arendonk leftover WZC WZGA remine@2526; NOT leftover OCMW Arendonk De Peulder 0212.236.097 SKIP; NOT leftover-via-VE",
    },
    {
        "source_id": SRC_SBM,
        "title": "NBB Consult / SBM fiche Talander 0433306225 (deposit-id only)",
        "url": "https://consult.cbso.nbb.be/consult-enterprise/0433306225",
        "accessed_date": DAY,
        "publisher": "NBB Consult / SBM",
        "source_class": "official_register",
        "notes": "tick2527; deposit-id 2026-00192214 YE 01.01.2025-31.12.2025 filing VKT-VZW Initial header 24/06/2026; NBB consult HTML stub 5344 B discarded; CDN PDF used for euros; ZIP/XBRL not used for euros; NBB broker PDF 403 this tick; NBB published-deposits 403 this tick; Companyweb unused for euros; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
    },
    {
        "source_id": SRC_SITE,
        "title": "Talander FOI contact leftover city_arendonk leftover VAPH",
        "url": "https://www.talander.be/contact",
        "publisher": "Talander VZW leftover city_arendonk leftover VAPH 2 VE",
        "accessed_date": DAY,
        "source_class": "foi_contact",
        "notes": "tick2527; FOI info@talander.be from official site https://www.talander.be/contact; leftover mined city_arendonk leftover VAPH leftover-mined AGB-only unused leftover type after leftover city_arendonk leftover WZC WZGA@2526 leftover OCMW De Peulder SKIP leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk unused-looking leftover CIK unused-looking leftover CIK fallback not taken; leftover city_bertem leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_stabroek leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_wichelen leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_lebbeke leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken; leftover city_meerhout leftover WZC taken leftover VAPH t Volderke SCAN leftover maatwerk DE SPRONG remine leftover CAR/CIK unused-looking leftover CIK fallback not taken; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine",
    },
], src_fields)
print("sources ok")
print("CORE1A DONE")
