#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2417_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_bkogenkoost_jr2025_nbb_pdf_2417"
SRC_KBO = "src_bkogenkoost_kbo_2417"
SRC_SBM = "src_bkogenkoost_sbm_2417"
SRC_SITE = "src_bkogenkoost_site_2417"
GAP = "gap_bkogenkoost_opgroeien_matrix_bruto_1_28m_omzet73_empty_pnl_jump_217k_destin_0_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 BKO GENK-OOST deposit 2026-00112540,http://cdn.staatsbladmonitor.be/2026pdf/2026-00112540.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2417; official native PDF 45298 bytes 12p VKT-VZW 23.0.9 m04-f; header 13.05.2026; AV 11.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-07; CreationDate 2026-05-18 12:38:28 UTC OpenPDF 1.3.26; all 12p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO BKO GENK-OOST 0475.432.830,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0475432830,KBO Public Search FOD Economie,{DAY},official_register,tick2417; Actief; 2 VE zetel Reinpadstraat 169 3600 Genk since 27.03.2007 + De Bonobo 2.160.424.877 Jaarbeurslaan 12 since 16.03.2007; naam BUITENSCHOOLSE KINDEROPVANG GENK OOST since 14.09.2000; afkorting BKO GENK-OOST since 27.03.2007; begindatum 14.09.2000; RSZ2025 88.919; RSZ-werkgever since 18.03.2002; 4 bestuurders + dagelijks bestuur Coolen Els since 01.05.2026; FOI info@deapenstaart.be; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},Staatsbladmonitor fiche BKO GENK-OOST 0475432830 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0475432830,Staatsbladmonitor,{DAY},official_register,tick2417; deposit-id 2026-00112540 YE 2025-01-01>2025-12-31 header 2026-05-13 neerlegging 2026-05-18 and CDN Last-Modified 2026-06-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},De Apenstaart FOI contact leftover city_genk BKO,https://deapenstaart.be/,VZW BKO GENK-OOST / De Apenstaart,{DAY},foi_contact,tick2417; FOI info@deapenstaart.be; zetel Reinpadstraat 169 3600 Genk; Kind en Gezin erkend IBO De Apenstaart + De Bonobo; leftover city_genk after CAW Limburg / BWOL; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
