#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2426_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_kindercentrum_jr2025_nbb_pdf_2426"
SRC_KBO = "src_kindercentrum_kbo_2426"
SRC_SBM = "src_kindercentrum_sbm_2426"
SRC_SITE = "src_kindercentrum_site_2426"
GAP = "gap_kindercentrum_opgroeien_matrix_opbr_11_40m_omzet_2_19m_74_9_13m_pnl_drop_482k_destin_0_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Kindercentrum deposit 2026-00194179,http://cdn.staatsbladmonitor.be/2026pdf/2026-00194179.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2426; official native PDF 9300990 bytes 45p VOL-VZW 23.0.10 m05-f; header 24.06.2026; AV 23.06.2026; SBM neerlegging 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-09; CreationDate 2026-06-24 23:46:35 UTC OpenPDF 1.3.26; financial + jaarverslag pp.1-40 native text; commissarisverslag pp.41-45 scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kindercentrum 0408.226.775,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408226775,KBO Public Search FOD Economie,{DAY},official_register,tick2426; Actief; 14 VE; naam Kindercentrum since 15.11.2018; VZW since 15.02.1971; zetel Koning Albertstraat 43 8791 Waregem since 26.06.2019; RSZ2025 88.911; RSZ-werkgever since 01.04.1971; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 9 functiehouders; voorzitter Jacques Verhaeghe; dagelijks bestuur Tom Braet; FOI info@kindercentrum.be; NOT WZC De Linde Wortegem-Petegem 0425.773.085; NOT WZC De Linde Lievegem 0467.355.403; NOT De Linde Ronse 0778.279.401; NOT Curando 0445.499.422; NOT Kinderopvang Mariawende 0411.611.184; NOT Helan 0464.151.037; NOT Vormingscentrum 0413.342.338; NOT Kloosterstraat 6 9031 Drongen",
    f"{SRC_SBM},NBB Consult fiche Kindercentrum 0408226775 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0408226775,NBB Consult,{DAY},official_register,tick2426; deposit-id 2026-00194179 YE 31/12/2025 filing header 24/06/2026 VOL-VZW Initial; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Kindercentrum FOI contact leftover city_waregem CIK,https://kindercentrum.be/,VZW Kindercentrum,{DAY},foi_contact,tick2426; FOI info@kindercentrum.be; zetel Koning Albertstraat 43 8791 Waregem; leftover mined city_waregem after WAGSO / Werkplus Maatwerk Waregem@2204; 14 VE KDV+BKO; NOT Kloosterstraat 6 Drongen; NOT WZC De Linde Wortegem-Petegem; NOT Curando; NOT Vormingscentrum; NOT Helan Kinderopvang",
])
print("sources ok")
