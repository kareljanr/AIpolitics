#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2416_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_denderkind_jr2025_nbb_pdf_2416"
SRC_KBO = "src_denderkind_kbo_2416"
SRC_SBM = "src_denderkind_sbm_2416"
SRC_SITE = "src_denderkind_site_2416"
GAP = "gap_denderkind_opgroeien_matrix_bruto_3_96m_omzet73_empty_pnl_drop_25k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Denderkind deposit 2026-00065367,http://cdn.staatsbladmonitor.be/2026pdf/2026-00065367.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2416; official native PDF 50802 bytes 14p VKT-VZW 25.0.9 m04-f; header 30.03.2026; AV 19.03.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-04-10; CreationDate 2026-03-30 08:08:13 UTC OpenPDF 1.3.26; all 14p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Denderkind 0479.127.045,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0479127045,KBO Public Search FOD Economie,{DAY},official_register,tick2416; Actief; 16 VE HQ 2.157.744.016 DENDERKIND vzw Korte Zoutstraat 32/K since 01.08.2015 (begindatum VE 05.12.2006) + 15 KDV-sites incl. Ede-kind 2.388.220.073 since 05.01.2026 post-YE2025; zetel Korte Zoutstraat 32 bus K 9300 Aalst since 01.08.2015; naam DENDERKIND since 07.06.2002; begindatum 07.06.2002; RSZ2025 88.911; RSZ-werkgever since 02.09.2002; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; 7 functiehouders; FOI info@denderkind.be; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche Denderkind 0479127045 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0479127045,Staatsbladmonitor,{DAY},official_register,tick2416; deposit-id 2026-00065367 YE 2025-01-01>2025-12-31 header 2026-03-30 and CDN Last-Modified 2026-04-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Denderkind FOI contact leftover city_aalst CIK+BKO,https://www.denderkind.be/,VZW Denderkind,{DAY},foi_contact,tick2416; FOI info@denderkind.be; zetel Korte Zoutstraat 32 bus K 9300 Aalst; 12 KDV + BKO inkomenstarief in/rond Aalst; leftover city_aalst after CAR De Hert; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
