#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2424_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_olv_gasthuis_jr2025_nbb_pdf_2424"
SRC_KBO = "src_olv_gasthuis_kbo_2424"
SRC_SBM = "src_olv_gasthuis_sbm_2424"
SRC_SITE = "src_olv_gasthuis_site_2424"
GAP = "gap_olv_gasthuis_poperinge_zorg_matrix_omzet_14_15m_73_2_64m_opbr_17_01m_pnl_loss_improve_95k_destin_0_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 OLV Gasthuis Poperinge deposit 2026-00306712,http://cdn.staatsbladmonitor.be/2026pdf/2026-00306712.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2424; official native PDF 1571427 bytes 48p VOL-VZW 25.0.13 m05-f; header 15.07.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-02; CreationDate 2026-07-18 01:08:27 UTC OpenPDF 1.3.26; financial + waarderingsregels pp.1-38 native text; jaarverslag pp.40-41 scan; commissarisverslag pp.42-48 scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Onze-Lieve-Vrouw Gasthuis 0445.066.385,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445066385,KBO Public Search FOD Economie,{DAY},official_register,tick2424; Actief; 2 VE 2.150.784.463 WZC OLV Gasthuis Ieperstraat 130 8970 Poperinge since 03.01.2006 + 2.272.821.549 WZC Emmaus Oostlaan 15 8970 Poperinge since 08.01.2018; naam Onze-Lieve-Vrouw Gasthuis since 15.04.2015; afkorting O.L.V. Gasthuis since 24.04.2000; VZW since 13.05.1991; zetel Ieperstraat 130 8970 Poperinge since 24.09.1997; RSZ2025 87.101; RSZ-werkgever since 01.01.1994; aanbestedende overheid since 13.05.1991; 9 functiehouders; voorzitter Lieven Delvoye; FOI info@gasthuis.be; NOT WZC OLV Roosdaal 0421.031.171; NOT Emmaus AZ 0411.515.075; NOT Huize Zonnelied 0415.082.497; NOT Wintershove 0459.245.312; NOT Quattro 0555.667.072; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT WZC De Linde Lievegem 0467.355.403; NOT Kloosterstraat 6 9031 Drongen; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche OLV Gasthuis 0445066385 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0445066385,NBB Consult,{DAY},official_register,tick2424; deposit-id 2026-00306712 YE 31/12/2025 filing header 15/07/2026 VOL-VZW Initial; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC OLV Gasthuis Poperinge FOI contact leftover city_poperinge Quattro-lid,https://www.gasthuis.be/,VZW Onze-Lieve-Vrouw Gasthuis,{DAY},foi_contact,tick2424; FOI info@gasthuis.be; zetel Ieperstraat 130 8970 Poperinge; WZC OLV Gasthuis + WZC Emmaus; leftover city_poperinge after AGB De Kouter / De Lovie; Quattro-lid after Huize Zonnelied@2423 / Wintershove@2422 / Quattro@2421; NOT Kloosterstraat 6 Drongen; NOT WZC OLV Roosdaal; NOT Emmaus AZ; NOT Huize Zonnelied; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Wintershove; NOT Quattro; NOT WZC De Ruyschaert; NOT De Pagadder; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
