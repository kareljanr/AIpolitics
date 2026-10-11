#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2423_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_huize_zonnelied_jr2025_nbb_pdf_2423"
SRC_KBO = "src_huize_zonnelied_kbo_2423"
SRC_SBM = "src_huize_zonnelied_sbm_2423"
SRC_SITE = "src_huize_zonnelied_site_2423"
GAP = "gap_zonnelied_ieper_zorg_matrix_omzet_10_95m_73_2_43m_opbr_13_61m_pnl_jump_280k_destin_240k_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Huize Zonnelied Ieper deposit 2026-00185108,http://cdn.staatsbladmonitor.be/2026pdf/2026-00185108.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2423; official native PDF 189107 bytes 45p VOL-VZW 23.0.10 m05-f; header 18.06.2026; AV 17.06.2026; jaarverslag 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-29; CreationDate 2026-06-23 03:15:40 UTC OpenPDF 1.3.26; all 45p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Huize Zonnelied 0415.082.497,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415082497,KBO Public Search FOD Economie,{DAY},official_register,tick2423; Actief; 1 VE 2.150.803.764 Stationsstraat 24 8900 Ieper since 04.01.2006; naam Huize Zonnelied since 15.10.1974; VZW since 15.10.1974; zetel Stationsstraat 24 8900 Ieper since 08.11.2023; RSZ2025 87.301; RSZ-werkgever since 01.10.1974; aanbestedende overheid since 15.10.1974; 11 functiehouders; voorzitter Rozanne Philippe; FOI info@huizezonnelied.be; NOT Zonnelied Roosdaal 0420.607.638; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT WZC De Linde Lievegem 0467.355.403; NOT Kloosterstraat 6 9031 Drongen; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche Huize Zonnelied 0415082497 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0415082497,NBB Consult,{DAY},official_register,tick2423; deposit-id 2026-00185108 YE 31/12/2025 filing header 18/06/2026 VOL-VZW Initial; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC Huize Zonnelied FOI contact leftover city_ieper Quattro-lid,https://huizezonnelied.be/,VZW Huize Zonnelied,{DAY},foi_contact,tick2423; FOI info@huizezonnelied.be; zetel Stationsstraat 24 8900 Ieper; WZC + DVC Zonnegloed / kortverblijf / zorgflats; leftover city_ieper after Wintershove / Buitenschoolse Opvang Ieper / CAR De Klinker / Home Vrijzicht / Huize Sint-Jozef; Quattro-lid after Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT Zonnelied Roosdaal; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Wintershove; NOT Quattro; NOT WZC De Ruyschaert; NOT De Pagadder; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
