#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2405_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_hoeksteen_jr2025_nbb_pdf_2405"
SRC_KBO = "src_hoeksteen_kbo_2405"
SRC_SBM = "src_hoeksteen_sbm_2405"
SRC_SITE = "src_hoeksteen_site_2405"
GAP = "gap_hoeksteen_opgroeien_t2_matrix_bruto_1_87m_omzet73_empty_pnl_loss_flip_7k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang De Hoeksteen deposit 2026-00224895,http://cdn.staatsbladmonitor.be/2026pdf/2026-00224895.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2405; official native PDF 52544 bytes 14p VKT-VZW 26.0.15 m04-f; header 29.06.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-18; CreationDate 2026-06-30 22:09:34 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang De Hoeksteen 0765.439.866,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0765439866,KBO Public Search FOD Economie,{DAY},official_register,tick2405; Actief; 9 VE; zetel Beerststraat 36 8600 Diksmuide since 20.03.2021; naam Kinderopvang De Hoeksteen / KoDH since 20.03.2021; begindatum 20.03.2021; RSZ2025 88.911; RSZ-werkgever since 05.09.2022; Kinderopvang Vlaamse Gemeenschap since 16.08.2022; FOI gerdy.desmedt@de-hoeksteen.be; NOT Ter Eecken 0432.465.392; NOT De Kade 0413.650.659; NOT CFR Zelzate 0419.645.952",
    f"{SRC_SBM},Staatsbladmonitor fiche Kinderopvang De Hoeksteen 0765439866 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0765439866,Staatsbladmonitor,{DAY},official_register,tick2405; deposit-id 2026-00224895 YE 2025-01-01>2025-12-31 neerlegging 2026-07-01 and CDN Last-Modified 2026-07-18; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CoBRHA Kinderopvang De Hoeksteen FOI contact leftover city_diksmuide CIK,https://publiek.departementzorg.be/Cobrha/Companies/Company/0765439866,Departement Zorg CoBRHA,{DAY},foi_contact,tick2405; FOI gerdy.desmedt@de-hoeksteen.be; zetel Beerststraat 36 8600 Diksmuide; 9 zorgvoorzieningen; leftover city_diksmuide after Ter Eecken@2404; no public website in KBO; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
