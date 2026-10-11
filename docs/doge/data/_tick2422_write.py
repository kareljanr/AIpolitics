#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2422_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_wintershove_jr2025_nbb_pdf_2422"
SRC_KBO = "src_wintershove_kbo_2422"
SRC_SBM = "src_wintershove_sbm_2422"
SRC_SITE = "src_wintershove_site_2422"
GAP = "gap_wintershove_zorg_matrix_omzet_6_65m_73_1_04m_opbr_7_79m_pnl_loss_flip_23k_destin_0_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 WINTERSHOVE deposit 2026-00178085,http://cdn.staatsbladmonitor.be/2026pdf/2026-00178085.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2422; official native PDF 1758177 bytes 48p VOL-VZW 23.0.10 m05-f; header 18.06.2026; AV 17.06.2026; jaarverslag 06.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-22; CreationDate 2026-06-20 02:45:47 UTC OpenPDF 1.3.26; financial + jaarverslag pp.1-41 native text; commissarisverslag pp.42-48 scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO WINTERSHOVE 0459.245.312,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0459245312,KBO Public Search FOD Economie,{DAY},official_register,tick2422; Actief; 1 VE 2.156.473.910 Poperingseweg 288 8908 Ieper since 05.10.2006; naam WINTERSHOVE since 02.09.1996; VZW since 02.09.1996; zetel Poperingseweg 288 8908 Ieper since 25.01.2001; RSZ2025 87.301; RSZ-werkgever since 25.05.2000; aanbestedende overheid since 02.09.1996; 11 functiehouders; voorzitter Willy Traen; FOI info@wintershove.be; NOT Kloosterstraat 6 9031 Drongen; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT WZC De Linde Lievegem 0467.355.403; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche WINTERSHOVE 0459245312 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0459245312,NBB Consult,{DAY},official_register,tick2422; deposit-id 2026-00178085 YE 31/12/2025 filing header 18/06/2026 VOL-VZW Initial; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC Wintershove FOI contact leftover city_ieper Quattro-lid,https://www.wintershove.be/,VZW WINTERSHOVE,{DAY},foi_contact,tick2422; FOI info@wintershove.be; zetel Poperingseweg 288 8908 Vlamertinge; WZC 108 woongelegenheden; leftover city_ieper after Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Quattro; NOT WZC De Ruyschaert; NOT De Pagadder; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
