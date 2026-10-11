#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2420_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_ruyschaert_jr2025_nbb_pdf_2420"
SRC_KBO = "src_ruyschaert_kbo_2420"
SRC_SBM = "src_ruyschaert_sbm_2420"
SRC_SITE = "src_ruyschaert_site_2420"
GAP = "gap_ruyschaert_zorg_matrix_omzet_8_83m_73_1_68m_opbr_11_21m_pnl_flip_242k_destin_0_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Integrale Bejaardenzorg Sint-Jozef / WZC De Ruyschaert deposit 2026-00183610,http://cdn.staatsbladmonitor.be/2026pdf/2026-00183610.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2420; official native PDF 3405373 bytes 40p VOL-VZW 26.0.15 m05-f; header 22.06.2026; AV 10.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-29; CreationDate 2026-06-22 23:44:46 UTC OpenPDF 1.3.26; financial + jaarverslag pp.1-33 native text; commissarisverslag pp.34-40 scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Integrale Bejaardenzorg Sint-Jozef / WZC De Ruyschaert 0434.996.993,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0434996993,KBO Public Search FOD Economie,{DAY},official_register,tick2420; Actief; 1 VE 2.191.002.247 Kloosterstraat(Mar) 25 8510 Kortrijk since 01.01.2008; naam Integrale Bejaardenzorg Sint-Jozef since 04.02.1988; VZW since 04.02.1988; zetel Kloosterstraat(Mar) 25 8510 Kortrijk; RSZ2025 87.301; RSZ-werkgever since 01.01.1989; 9 functiehouders; gedelegeerd bestuurder Mario Eeckhout since 08.01.2015; FOI boekhouding@de-ruyschaert.be; NOT Kloosterstraat 6 9031 Drongen; NOT De Pagadder 0888.028.268; NOT KOS 0891.472.362; NOT BKO GENK-OOST 0475.432.830; NOT Denderkind 0479.127.045; NOT Kinderopvang Mariawende 0411.611.184; NOT Buitenschoolse Opvang Ieper 0431.691.669; NOT Bengelhof 0455.442.813; NOT Kinderopvang Turnhout 0465.284.947; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037",
    f"{SRC_SBM},NBB Consult fiche De Ruyschaert 0434996993 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0434996993,NBB Consult,{DAY},official_register,tick2420; deposit-id 2026-00183610 YE 30/12/2025 filing 22/06/2026 Volledig model vereniging Initial; prior 2025-00202419 YE 30/12/2024; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},WZC De Ruyschaert FOI contact leftover city_kortrijk WZC,https://de-ruyschaert.be/,VZW Integrale Bejaardenzorg Sint-Jozef / WZC De Ruyschaert,{DAY},foi_contact,tick2420; FOI boekhouding@de-ruyschaert.be + info@de-ruyschaert.be; zetel Kloosterstraat 25 8510 Marke; WZC + dagverzorging De Pendel + kortverblijf + assistentiewoningen Residentie het Kloosterhof; leftover city_kortrijk after Hangar K / SW+ / CGG Mandel en Leie / CAW ZWVL / HVZ Fluvia / Zonnebloem / CAR Accent / De Pagadder; NOT Kloosterstraat 6 Drongen; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT De Pagadder; NOT KOS; NOT BKO GENK-OOST; NOT Denderkind; NOT Kinderopvang Mariawende; NOT Buitenschoolse Opvang Ieper; NOT Bengelhof; NOT Kinderopvang Turnhout; NOT KINDEROPVANG ZONNESTRAAL; NOT Zonnestraal Junior; NOT Elfenbankje; NOT t Eekhoorntje; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
