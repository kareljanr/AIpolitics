#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2409_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_elfenbankje_jr2025_nbb_pdf_2409"
SRC_KBO = "src_elfenbankje_kbo_2409"
SRC_SBM = "src_elfenbankje_sbm_2409"
SRC_SITE = "src_elfenbankje_site_2409"
GAP = "gap_elfenbankje_opgroeien_matrix_bruto_2_19m_omzet73_empty_pnl_drop_197k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang Elfenbankje deposit 2026-00072866,http://cdn.staatsbladmonitor.be/2026pdf/2026-00072866.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2409; official native PDF 51066 bytes 13p VKT-VZW 26.0.8 m04-f; header 03.04.2026; AV 30.03.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-04-11; CreationDate 2026-04-07 07:27:25 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang Elfenbankje 0417.638.151,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417638151,KBO Public Search FOD Economie,{DAY},official_register,tick2409; Actief; 1 VE 2.153.866.093; zetel Sint-Pietersaalststraat 80 9000 Gent since 15.12.2015; naam Kinderopvang Elfenbankje since 08.06.2026; begindatum 26.09.1977; RSZ2025 88.911; RSZ-werkgever since 02.01.1978; Kinderopvang Vlaamse Gemeenschap since 12.12.2025; slorpte ELFENBANKJE D.V.O. 0862.573.884 since 30.03.2026 post-YE2025; FOI kdv@elfenbankje.be; NOT t Eekhoorntje 0414.453.680; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866",
    f"{SRC_SBM},Staatsbladmonitor fiche Elfenbankje 0417638151 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0417638151,Staatsbladmonitor,{DAY},official_register,tick2409; deposit-id 2026-00072866 YE 2025-01-01>2025-12-31 neerlegging 2026-04-03 and CDN Last-Modified 2026-04-11; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Elfenbankje FOI contact leftover city_gent CIK,https://www.elfenbankje.be/,Kinderopvang Elfenbankje vzw,{DAY},foi_contact,tick2409; FOI kdv@elfenbankje.be + dvo@elfenbankje.be; zetel Sint-Pietersaalststraat 80 9000 Gent; 1 VE groepsopvang 120+ 8 leefgroepen + 29 onthaalouders; leftover city_gent after t Eekhoorntje@2408; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
