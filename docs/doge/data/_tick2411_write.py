#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2411_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_zonnestraal_jr2025_nbb_pdf_2411"
SRC_KBO = "src_zonnestraal_kbo_2411"
SRC_SBM = "src_zonnestraal_sbm_2411"
SRC_SITE = "src_zonnestraal_site_2411"
GAP = "gap_zonnestraal_opgroeien_matrix_opbr_3_56m_73_2_20m_omzet_1_35m_pnl_drop_112k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KINDEROPVANG ZONNESTRAAL deposit 2026-00244239,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244239.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2411; official native PDF 231632 bytes 21p VKT-VZW 25.0.13 m04-f; header 30.06.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; SBM neerlegging 03.07.2026; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:37:51 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO KINDEROPVANG ZONNESTRAAL 0413.351.642,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413351642,KBO Public Search FOD Economie,{DAY},official_register,tick2411; Actief; 1 VE; zetel Gladiolenstraat 10 9100 Sint-Niklaas since 17.06.1999; naam KINDEROPVANG ZONNESTRAAL since 24.06.2002; begindatum 31.07.1973; RSZ2025 88.911; RSZ-werkgever since 01.07.1973; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@kinderopvangzonnestraal.be; NOT Junior 0866.116.859; NOT Grimbergen VAPH Zonnestraal Havinet; NOT Elfenbankje 0417.638.151; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539",
    f"{SRC_SBM},Staatsbladmonitor fiche KINDEROPVANG ZONNESTRAAL 0413351642 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0413351642,Staatsbladmonitor,{DAY},official_register,tick2411; deposit-id 2026-00244239 YE 2025-01-01>2025-12-31 neerlegging 2026-07-03 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},KINDEROPVANG ZONNESTRAAL FOI contact leftover city_sint_niklaas CIK,https://www.kinderopvangzonnestraal.be/,Kinderopvang Zonnestraal vzw,{DAY},foi_contact,tick2411; FOI info@kinderopvangzonnestraal.be; zetel Gladiolenstraat 10 9100 Sint-Niklaas; 1 VE parent dual vs Junior 0866.116.859 20 VE same address same board; leftover city_sint_niklaas after Junior@2410; NOT Grimbergen VAPH Zonnestraal; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
