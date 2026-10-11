#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2429_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_windekind_jr2025_nbb_pdf_2429"
SRC_KBO = "src_windekind_kbo_2429"
SRC_SBM = "src_windekind_sbm_2429"
SRC_SITE = "src_windekind_site_2429"
GAP = "gap_windekind_opgroeien_matrix_bruto_1_18m_omzet73_empty_pnl_drop_61k_destin_61k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KINDERDAGVERBLIJF WINDEKIND deposit 2026-00320133,http://cdn.staatsbladmonitor.be/2026pdf/2026-00320133.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2429; official native PDF 47476 bytes 13p VKT-VZW 26.0.15 m04-f; header 23.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-04; CreationDate 2026-07-23 08:40:42 UTC OpenPDF 1.3.26; all 13p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO KINDERDAGVERBLIJF WINDEKIND 0431.806.386,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431806386,KBO Public Search FOD Economie,{DAY},official_register,tick2429; Actief; 1 VE 2.154.448.588 Roggestraat 17 9000 Gent since 14.06.2006; naam KINDERDAGVERBLIJF WINDEKIND since 10.12.1985; VZW since 10.12.1985; begindatum 10.12.1985; zetel Roggestraat 17 9000 Gent since 10.12.1985; RSZ2025 88.911; RSZ-werkgever since 01.01.1986; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 2 bestuurders Filip De Muynck + Koenraad Van Sumere; FOI info@windekind.gent; NOT Elfenbankje 0417.638.151; NOT Beregoed 0447.515.042; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT Kloosterstraat 6 9031 Drongen",
    f"{SRC_SBM},NBB Consult / SBM fiche Windekind 0431806386 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0431806386,NBB Consult,{DAY},official_register,tick2429; deposit-id 2026-00320133 YE 31/12/2025 filing header 23/07/2026 VKT-VZW Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Windekind FOI contact leftover city_gent CIK,https://windekind.gent/,VZW KINDERDAGVERBLIJF WINDEKIND,{DAY},foi_contact,tick2429; FOI info@windekind.gent; zetel Roggestraat 17 9000 Gent; leftover mined city_gent after Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE 69 Opgroeien plaatsen 0-3 jaar IKT; NOT Kloosterstraat 6 Drongen; NOT Elfenbankje; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Duinhuisjes; NOT t Bremhuisje stopgezet 1993",
])
print("sources ok")
