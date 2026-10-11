#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2427_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_kisme_jr2025_nbb_pdf_2427"
SRC_KBO = "src_kisme_kbo_2427"
SRC_SBM = "src_kisme_sbm_2427"
SRC_SITE = "src_kisme_site_2427"
GAP = "gap_kisme_opgroeien_matrix_bruto_630k_omzet73_empty_pnl_drop_119k_destin_0_l5"
if not (ROOT / f"docs/doge/foi/drafts/{GAP}.md").is_file():
    raise SystemExit("FOI draft missing")

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KISME deposit 2026-00117266,http://cdn.staatsbladmonitor.be/2026pdf/2026-00117266.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2427; official native PDF 566122 bytes 19p VKT-VZW 26.0.11 m04-f; header 19.05.2026; AV 11.05.2026; SBM neerlegging 22.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-08; CreationDate 2026-05-22 01:09:12 UTC OpenPDF 1.3.26; all 19p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang Scholengroep Meetjesland / KISME 0894.549.440,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0894549440,KBO Public Search FOD Economie,{DAY},official_register,tick2427; Actief; 3 VE; naam Kinderopvang Scholengroep Meetjesland / afkorting KISME since 19.12.2007; VZW since 19.12.2007; begindatum 28.12.2007; zetel Beukenstraat 1 9900 Eeklo since 19.12.2007; RSZ2025 88.911; RSZ-werkgever since 01.09.2008; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 5 functiehouders; voorzitter Kristof De Baere; FOI kinderopvang@go-dynamiek.be; NOT Kinderlach 0450.275.186; NOT Kindercentrum 0408.226.775; NOT KOS 0891.472.362; NOT Kinderopvang Baloo BV 0762.684.274; NOT Helan 0464.151.037; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6 9031 Drongen",
    f"{SRC_SBM},NBB Consult / SBM fiche KISME 0894549440 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0894549440,NBB Consult,{DAY},official_register,tick2427; deposit-id 2026-00117266 YE 31/12/2025 filing header 19/05/2026 VKT-VZW Initial; SBM neerlegging 22.05.2026 used for deposit-id discovery only; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},KISME / GO Dynamiek FOI contact leftover city_eeklo CIK,https://go-dynamiek.be/,VZW Kinderopvang Scholengroep Meetjesland,{DAY},foi_contact,tick2427; FOI kinderopvang@go-dynamiek.be; zetel Beukenstraat 1 9900 Eeklo; leftover mined city_eeklo after Welzijnsband / Woonmaatschappij Meetjesland / HVZ Meetjesland / Ascendere; also leftover mined city_aalter; 3 VE Habibi + Het Klaverwolkje; NOT Kloosterstraat 6 Drongen; NOT Kinderlach YE2024; NOT Kindercentrum; NOT KOS; NOT Vormingscentrum; NOT Helan Kinderopvang",
])
print("sources ok")
