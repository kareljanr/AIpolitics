#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2421_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_quattro_jr2025_nbb_pdf_2421"
SRC_KBO = "src_quattro_kbo_2421"
SRC_SBM = "src_quattro_sbm_2421"
SRC_SITE = "src_quattro_site_2421"
GAP = "gap_quattro_zorg_matrix_omzet_247k_73_empty_bruto_239k_pnl_loss_9k_destin_0_l5"
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
    f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 QUATTRO deposit 2026-00188800,http://cdn.staatsbladmonitor.be/2026pdf/2026-00188800.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2421; official native PDF 48150 bytes 12p MIC-VZW 23.0.10 m08-f; header 23.06.2026; AV 19.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-23 23:49:06 UTC OpenPDF 1.3.26; all 12p native text; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO QUATTRO 0555.667.072,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0555667072,KBO Public Search FOD Economie,{DAY},official_register,tick2421; Actief; 1 VE 2.239.182.147 Kloosterstraat(Mar) 18 8510 Kortrijk since 23.02.2015; naam QUATTRO since 31.03.2014; VZW since 31.03.2014; zetel Kloosterstraat(Mar) 18 8510 Kortrijk; RSZ2025 88.109; RSZ-werkgever since 23.02.2015; 10 functiehouders; voorzitter Bart Man; bestuurders Mario Eeckhout Peter Reynaert Mieke Vandeputte Ken Wagner; FOI boekhouding@de-ruyschaert.be; NOT Kloosterstraat 6 9031 Drongen; NOT WZC De Ruyschaert 0434.996.993; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche QUATTRO 0555667072 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0555667072,NBB Consult,{DAY},official_register,tick2421; deposit-id 2026-00188800 YE 30/12/2025 filing 23/06/2026 Micro model vereniging Initial; prior 2025-00203405 YE 30/12/2024; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Quattro Samen Werken aan Zorg FOI contact leftover city_kortrijk WZC-collab,https://quattrosamenwerkenaanzorg.be/,VZW QUATTRO,{DAY},foi_contact,tick2421; FOI boekhouding@de-ruyschaert.be; zetel Kloosterstraat 18 8510 Marke; samenwerkingsverband 8 WZC (De Ruyschaert Marke Wintershove Vlamertinge Huize Zonnelied Ieper St Jozef Zonnebeke St Vincentius Avelgem OLV Gasthuis Poperinge WZC De Linde +1); leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder / WZC De Ruyschaert; NOT Kloosterstraat 6 Drongen; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT WZC De Ruyschaert; NOT De Pagadder; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
