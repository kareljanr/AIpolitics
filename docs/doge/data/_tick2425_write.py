#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2425_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_de_linde_wortegem_jr2025_nbb_pdf_2425"
SRC_KBO = "src_de_linde_wortegem_kbo_2425"
SRC_SBM = "src_de_linde_wortegem_sbm_2425"
SRC_SITE = "src_de_linde_wortegem_site_2425"
GAP = "gap_de_linde_wortegem_zorg_matrix_omzet_5_52m_73_1_05m_opbr_6_68m_pnl_flip_62k_destin_62k_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 WZC De Linde Wortegem-Petegem deposit 2026-00162292,http://cdn.staatsbladmonitor.be/2026pdf/2026-00162292.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2425; official native PDF 4437983 bytes 45p VOL-VZW 25.0.12 m05-f; header 10.06.2026; AV 08.06.2026; SBM neerlegging 16.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-20; CreationDate 2026-06-16 01:25:03 UTC OpenPDF 1.3.26; financial + jaarverslag pp.1-39 native text; commissarisverslag pp.40-45 scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO De Linde 0425.773.085,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0425773085,KBO Public Search FOD Economie,{DAY},official_register,tick2425; Actief; 1 VE 2.189.365.521 De Linde vzw Lindestraat (P.) 16 9790 Wortegem-Petegem since 01.07.2010; naam De Linde since 10.11.1987; VZW since 16.08.1983; zetel Lindestraat (P.) 16 9790 Wortegem-Petegem since 16.08.1983; RSZ2025 87.301; RSZ-werkgever since 01.10.1983; 7 functiehouders; voorzitter Rik Vandamme; FOI nadine@wzcdelinde.be; NOT WZC De Linde Lievegem 0467.355.403; NOT OLV Gasthuis Poperinge 0445.066.385; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT Kloosterstraat 6 9031 Drongen; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche De Linde 0425773085 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0425773085,NBB Consult,{DAY},official_register,tick2425; deposit-id 2026-00162292 YE 31/12/2025 filing header 10/06/2026 VOL-VZW Initial; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC De Linde Wortegem-Petegem FOI contact leftover city_oudenaarde Quattro-lid,https://wzc-de-linde.be/,VZW De Linde,{DAY},foi_contact,tick2425; FOI nadine@wzcdelinde.be; zetel Lindestraat 16 9790 Wortegem-Petegem; WZC 89 woongelegenheden; leftover nearby mined city_oudenaarde after SOLVA / HVVA; leftover unmined city_wortegem_petegem city GE; Quattro-lid after OLV Gasthuis Poperinge@2424 / Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC De Linde Lievegem; NOT OLV Gasthuis Poperinge; NOT Huize Zonnelied; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Wintershove; NOT Quattro; NOT WZC De Ruyschaert; NOT De Pagadder",
])
print("sources ok")
