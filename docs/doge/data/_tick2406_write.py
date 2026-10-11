#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2406_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_mereltjes_jr2025_nbb_pdf_2406"
SRC_KBO = "src_mereltjes_kbo_2406"
SRC_SBM = "src_mereltjes_sbm_2406"
SRC_SITE = "src_mereltjes_site_2406"
GAP = "gap_mereltjes_opgroeien_matrix_bruto_3_03m_omzet73_empty_pnl_jump_105k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang De Mereltjes deposit 2026-00216076,http://cdn.staatsbladmonitor.be/2026pdf/2026-00216076.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2406; official native PDF 44153 bytes 10p VKT-VZW 26.0.15 m04-f; header 29.06.2026; AV 25.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-11; CreationDate 2026-06-29 23:31:22 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang De Mereltjes 0412.778.352,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412778352,KBO Public Search FOD Economie,{DAY},official_register,tick2406; Actief; 1 VE 2.150.768.627; zetel Hasseltsesteenweg 16 3700 Tongeren-Borgloon since 01.01.2025; naam KINDEROPVANG DE MERELTJES since 05.07.2021; begindatum 16.11.1972; RSZ2025 88.911; RSZ-werkgever since 01.01.1973; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; Aanbestedende overheid since 18.01.2003; FOI kinderdagverblijf@mereltjes.be; NOT De Hoeksteen 0765.439.866; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659",
    f"{SRC_SBM},Staatsbladmonitor fiche Kinderopvang De Mereltjes 0412778352 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0412778352,Staatsbladmonitor,{DAY},official_register,tick2406; deposit-id 2026-00216076 YE 2025-01-01>2025-12-31 neerlegging 2026-06-29 and CDN Last-Modified 2026-07-11; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Kinderopvang De Mereltjes FOI contact leftover city_tongeren_borgloon CIK,https://mereltjes.be/,Kinderopvang De Mereltjes vzw,{DAY},foi_contact,tick2406; FOI kinderdagverblijf@mereltjes.be; zetel Hasseltsesteenweg 16 3700 Tongeren-Borgloon; 135 plaatsen groepsopvang inkomenstarief; leftover city_tongeren_borgloon after De Hoeksteen@2405; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
