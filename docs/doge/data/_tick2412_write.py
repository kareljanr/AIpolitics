#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2412_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_koturnhout_jr2025_nbb_pdf_2412"
SRC_KBO = "src_koturnhout_kbo_2412"
SRC_SBM = "src_koturnhout_sbm_2412"
SRC_SITE = "src_koturnhout_site_2412"
GAP = "gap_koturnhout_opgroeien_matrix_opbr_2_55m_73_2_23m_omzet_314k_pnl_flip_260_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang Turnhout deposit 2026-00286204,http://cdn.staatsbladmonitor.be/2026pdf/2026-00286204.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2412; official native PDF 1792686 bytes 20p VKT-VZW 26.0.15 m04-f; header 10.07.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-31; CreationDate 2026-07-13 23:00:41 UTC OpenPDF 1.3.26; financial pp.1-16 native text; commissarisverslag pp.17-20 scan; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang Turnhout 0465.284.947,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465284947,KBO Public Search FOD Economie,{DAY},official_register,tick2412; Actief; 5 VE; zetel Druivenstraat 19 2300 Turnhout since 10.09.2015; naam Kinderopvang Turnhout since 05.06.2008; begindatum 27.10.1998; RSZ2025 88.911; RSZ-werkgever since 01.03.1999; Stad Turnhout 0207.533.082 bestuurder since 06.03.2025; FOI kinderopvang@turnhout.be; NOT Zonnestraal 0413.351.642; NOT Junior 0866.116.859; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche Kinderopvang Turnhout 0465284947 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0465284947,Staatsbladmonitor,{DAY},official_register,tick2412; deposit-id 2026-00286204 YE 2025-01-01>2025-12-31 header 2026-07-10 and CDN Last-Modified 2026-07-31; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Kinderopvang Turnhout FOI contact leftover city_turnhout CIK/BKO EVA,https://www.turnhout.be/nl/kinderopvang,Stad Turnhout,{DAY},foi_contact,tick2412; FOI kinderopvang@turnhout.be; city FOI stad@turnhout.be; zetel Druivenstraat 19 / contact Fabriekstraat 14 2300 Turnhout; EVA privaatrechtelijk BKO 2.5-12; leftover city_turnhout after VERBINT@2401; creches to Orion 01.04.2024; NOT Helan Kinderopvang; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
