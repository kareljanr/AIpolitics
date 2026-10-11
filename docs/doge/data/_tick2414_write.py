#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2414_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_boi_jr2025_nbb_pdf_2414"
SRC_KBO = "src_boi_kbo_2414"
SRC_SBM = "src_boi_sbm_2414"
SRC_SITE = "src_boi_site_2414"
GAP = "gap_boi_opgroeien_matrix_bruto_484k_omzet73_empty_pnl_drop_3k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Buitenschoolse Opvang Ieper deposit 2026-00173514,http://cdn.staatsbladmonitor.be/2026pdf/2026-00173514.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2414; official native PDF 39675 bytes 9p VKT-VZW 23.0.10 m04-f; header 18.06.2026; AV 03.06.2026; YE 01.01.2025-31.12.2025; SBM neerlegging 2026-06-19; CDN Last-Modified 2026-06-21; CreationDate 2026-06-19 01:18:24 UTC OpenPDF 1.3.26; native text all pages; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Buitenschoolse Opvang Ieper 0431.691.669,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431691669,KBO Public Search FOD Economie,{DAY},official_register,tick2414; Actief; 3 VE 2.155.709.192 Appelstraat 1 since 10.10.2023 / 2.216.097.236 Holderdebolder Oude Veurnestraat 24A since 01.01.2013 / 2.216.097.533 Klavertje 4 Augustijnenstraat 67 since 01.01.2013; zetel Appelstraat 1 8900 Ieper since 10.10.2023; naam Buitenschoolse Opvang Ieper since 10.10.2023; afkorting B.O.I since 10.10.2023; begindatum 30.08.1985; RSZ2025 88.911; RSZ-werkgever since 01.01.1995; 9 functiehouders; FOI info@buitenschoolseopvangieper.be; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Mariawende 0411.611.184",
    f"{SRC_SBM},Staatsbladmonitor fiche Buitenschoolse Opvang Ieper 0431691669 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0431691669,Staatsbladmonitor,{DAY},official_register,tick2414; deposit-id 2026-00173514 YE 2025-01-01>2025-12-31 header 2026-06-18 SBM neerlegging 2026-06-19 and CDN Last-Modified 2026-06-21; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Buitenschoolse Opvang Ieper FOI contact leftover city_ieper BKO,https://www.buitenschoolseopvangieper.be/,VZW Buitenschoolse Opvang Ieper,{DAY},foi_contact,tick2414; FOI info@buitenschoolseopvangieper.be; zetel Appelstraat 1 8900 Ieper; Klavertje 4 61 + Holderdebolder 55 vakantie / 35 schooldagen; leftover city_ieper after CAR De Klinker@2386; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
