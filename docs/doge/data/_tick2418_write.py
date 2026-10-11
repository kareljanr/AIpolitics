#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2418_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_kos_jr2025_nbb_pdf_2418"
SRC_KBO = "src_kos_kbo_2418"
SRC_SBM = "src_kos_sbm_2418"
SRC_SITE = "src_kos_site_2418"
GAP = "gap_kos_opgroeien_matrix_omzet_1_86m_73_empty_pnl_jump_68k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KOS Kinderopvang Scholengroep Stroom deposit 2026-00167075,http://cdn.staatsbladmonitor.be/2026pdf/2026-00167075.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2418; official native PDF 43992 bytes 11p VKT-VZW 25.0.12 m04-f; header 17.06.2026; AV 12.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-21; CreationDate 2026-06-17 07:04:55 UTC OpenPDF 1.3.26; all 11p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO KOS Kinderopvang Scholengroep Stroom 0891.472.362,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0891472362,KBO Public Search FOD Economie,{DAY},official_register,tick2418; Actief; 5 VE Vogelzang 2.166.011.978 Haverstraat 9 8400 Oostende since 30.10.2007 + De Klimop 2.177.050.479 Putbekestraat 30 8470 Gistel since 01.01.2008 + De Lettertuin 2.177.050.578 Ringlaan 18 8680 Koekelare since 01.01.2008 + t Arnoldje 2.177.050.875 Brouwerijstraat 8 8460 Oudenburg since 01.01.2008 + t groeiboompje 2.214.729.338 Hendrik Serruyslaan 28 8400 Oostende since 12.04.2010; naam Kinderopvang Scholengroep Stroom / afkorting KOS since 15.05.2018; begindatum 12.07.2007; zetel Leffingestraat 1 8400 Oostende since 21.06.2021; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ-werkgever since 01.01.2008; 5 bestuurders; FOI info@sterkescholen.be; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche KOS 0891472362 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0891472362,Staatsbladmonitor,{DAY},official_register,tick2418; deposit-id 2026-00167075 YE 2025-01-01>2025-12-31 header 2026-06-17 neerlegging 2026-06-17 and CDN Last-Modified 2026-06-21; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Scholengroep Stroom FOI contact leftover city_oostende CIK,https://www.sterkescholen.be/,VZW Kinderopvang Scholengroep Stroom / KOS,{DAY},foi_contact,tick2418; FOI info@sterkescholen.be; zetel Leffingestraat 1 8400 Oostende; Kind en Gezin 5 KDV Vogelzang + De Klimop + De Lettertuin + t Arnoldje + t groeiboompje; leftover city_oostende after AG-O / IVOO / OVCO / Woonsprong; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
