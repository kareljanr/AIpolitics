#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2419_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_pagadder_jr2025_nbb_pdf_2419"
SRC_KBO = "src_pagadder_kbo_2419"
SRC_SBM = "src_pagadder_sbm_2419"
SRC_SITE = "src_pagadder_site_2419"
GAP = "gap_pagadder_opgroeien_matrix_opbr_1_61m_73_1_31m_omzet_298k_pnl_drop_83k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang De Pagadder deposit 2026-00133513,http://cdn.staatsbladmonitor.be/2026pdf/2026-00133513.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2419; official native PDF 52917 bytes 14p VKT-VZW 25.0.12 m04-f; header 02.06.2026; AV 01.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-11; CreationDate 2026-06-03 01:38:19 UTC OpenPDF 1.3.26; all 14p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang De Pagadder 0888.028.268,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0888028268,KBO Public Search FOD Economie,{DAY},official_register,tick2419; Actief; 2 VE zetel 2.163.753.759 Kloosterstraat(Mar) 18 8510 Kortrijk since 16.07.2007 + Marktstraat 2.278.022.927 Marktstraat(Mar) 14 8510 Kortrijk since 01.09.2018; naam vzw Kinderopvang De Pagadder since 16.03.2007; begindatum 16.03.2007; zetel Kloosterstraat(Mar) 18 8510 Kortrijk; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ-werkgever since 01.05.2007; 5 bestuurders; FOI boekhouding@de-ruyschaert.be; NOT Kloosterstraat 6 9031 Drongen; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche De Pagadder 0888028268 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0888028268,Staatsbladmonitor,{DAY},official_register,tick2419; deposit-id 2026-00133513 YE 2025-01-01>2025-12-31 header 2026-06-02 neerlegging 2026-06-02 and CDN Last-Modified 2026-06-11; NBB consult year-end 30/12/2025 filing 02/06/2026; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},De Pagadder FOI contact leftover city_kortrijk CIK,https://de-pagadder.be/,VZW Kinderopvang De Pagadder,{DAY},foi_contact,tick2419; FOI boekhouding@de-ruyschaert.be + kloosterstraat@de-pagadder.be; zetel Kloosterstraat 18 8510 Marke; Kind en Gezin 2 groepsopvang Kloosterstraat + Marktstraat; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent; NOT Kloosterstraat 6 Drongen; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
