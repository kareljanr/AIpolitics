#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2415_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_mariawende_jr2025_nbb_pdf_2415"
SRC_KBO = "src_mariawende_kbo_2415"
SRC_SBM = "src_mariawende_sbm_2415"
SRC_SITE = "src_mariawende_site_2415"
GAP = "gap_mariawende_opgroeien_matrix_bruto_3_35m_omzet73_empty_pnl_jump_736k_destin_736k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang Mariawende deposit 2026-00302442,http://cdn.staatsbladmonitor.be/2026pdf/2026-00302442.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2415; official native PDF 1709511 bytes 19p VKT-VZW 26.0.15 m04-f; header 17.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-02; CreationDate 2026-07-17 05:38:09 UTC OpenPDF 1.3.26; financial pp.1-11 native text; jaarverslag pp.12-19 no extractable text; prior-year restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang Mariawende 0411.611.184,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411611184,KBO Public Search FOD Economie,{DAY},official_register,tick2415; Actief; 2 VE 2.153.783.446 Ons Tuintje Keizerstraat 14 since 01.05.2014 / 2.212.055.306 t speelhuis Pastorieweg 15 since 02.02.2026; zetel Keizerstraat 14 A 8310 Brugge since 03.06.2014; naam Kinderopvang Mariawende since 24.01.2012; begindatum 20.10.1971; RSZ2025 88.911; RSZ-werkgever since 01.01.1973; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 7 functiehouders; FOI directeur@ko-mariawende.be; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche Kinderopvang Mariawende 0411611184 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0411611184,Staatsbladmonitor,{DAY},official_register,tick2415; deposit-id 2026-00302442 YE 2025-01-01>2025-12-31 header 2026-07-17 and CDN Last-Modified 2026-08-02; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Kinderopvang Mariawende FOI contact leftover city_brugge CIK+BKO,https://www.ko-mariawende.be/,VZW Kinderopvang Mariawende,{DAY},foi_contact,tick2415; FOI directeur@ko-mariawende.be; zetel Keizerstraat 14 A 8310 Brugge; Ons Tuintje 140 (merge Ons Huisje 01.01.2026 post-YE2025) + BKO t Speelhuis 2.5-12; leftover city_brugge after Mintus@1269; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
