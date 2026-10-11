#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2413_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_bengelhof_jr2025_nbb_pdf_2413"
SRC_KBO = "src_bengelhof_kbo_2413"
SRC_SBM = "src_bengelhof_sbm_2413"
SRC_SITE = "src_bengelhof_site_2413"
GAP = "gap_bengelhof_opgroeien_matrix_bruto_933k_omzet73_empty_pnl_drop_11k_destin_0_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"
if not (ROOT / DRAFT).is_file():
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Bengelhof deposit 2026-00191897,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191897.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2413; official native PDF 326914 bytes 16p VKT-VZW 26.0.15 m04-f; header 24.06.2026; AV 28.05.2026; jaarverslag 22.04.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 11:33:38 UTC OpenPDF 1.3.26; native text all pages; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Bengelhof 0455.442.813,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455442813,KBO Public Search FOD Economie,{DAY},official_register,tick2413; Actief; 1 VE 2.159.891.971; zetel Sint-Margrietstraat 36 9000 Gent since 13.11.2013; naam Bengelhof since 15.12.1994; begindatum 15.12.1994; RSZ2025 88.911; RSZ-werkgever since 01.01.1995; btw since 01.04.2022; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI bengelhof@dominovzw.be; NOT Elfenbankje 0417.638.151; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche Bengelhof 0455442813 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0455442813,Staatsbladmonitor,{DAY},official_register,tick2413; deposit-id 2026-00191897 YE 2025-01-01>2025-12-31 header 2026-06-24 and CDN Last-Modified 2026-07-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Bengelhof FOI contact leftover city_gent CIK groepsopvang,https://www.bengelhofvzw.be/,Bengelhof VZW,{DAY},foi_contact,tick2413; FOI bengelhof@dominovzw.be; zetel Sint-Margrietstraat 36 9000 Gent; 72 gesubsidieerde plaatsen inkomenstarief; leftover city_gent after Elfenbankje@2409; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
