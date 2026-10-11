#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2407_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_3wplus_jr2025_nbb_pdf_2407"
SRC_KBO = "src_3wplus_kbo_2407"
SRC_SBM = "src_3wplus_sbm_2407"
SRC_SITE = "src_3wplus_site_2407"
GAP = "gap_3wplus_opgroeien_matrix_bruto_7_16m_omzet73_empty_pnl_jump_551k_destin_75k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 3Wplus Kinderopvang deposit 2026-00273048,http://cdn.staatsbladmonitor.be/2026pdf/2026-00273048.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2407; official native PDF 310637 bytes 26p VKT-VZW 26.0.15 m04-f; header 09.07.2026; AV 26.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-28; CreationDate 2026-07-09 14:23:15 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO 3Wplus Kinderopvang 0893.870.539,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0893870539,KBO Public Search FOD Economie,{DAY},official_register,tick2407; Actief; 54 VE; zetel Z. 5 Mollem 250 1730 Asse since 01.03.2020; naam 3Wplus Kinderopvang since 21.12.2010; begindatum 30.11.2007; RSZ2025 88.919; RSZ-werkgever since 18.02.2008; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; btw since 01.10.2017; FOI kinderopvang@3wplus.be; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392",
    f"{SRC_SBM},Staatsbladmonitor fiche 3Wplus Kinderopvang 0893870539 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0893870539,Staatsbladmonitor,{DAY},official_register,tick2407; deposit-id 2026-00273048 YE 2025-01-01>2025-12-31 neerlegging 2026-07-09 and CDN Last-Modified 2026-07-28; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},3Wplus Kinderopvang FOI contact leftover city_asse CIK,https://3wplus.be/kinderopvang,3Wplus Kinderopvang vzw,{DAY},foi_contact,tick2407; FOI kinderopvang@3wplus.be; zetel Z. 5 Mollem 250 1730 Asse; 54 VE Halle-Vilvoorde groepsopvang BKO onthaalouders thuisopvang zieke kinderen; leftover city_asse after De Mereltjes@2406; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
