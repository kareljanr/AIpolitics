#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2408_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_eekhoorntje_jr2025_nbb_pdf_2408"
SRC_KBO = "src_eekhoorntje_kbo_2408"
SRC_SBM = "src_eekhoorntje_sbm_2408"
SRC_SITE = "src_eekhoorntje_site_2408"
GAP = "gap_eekhoorntje_opgroeien_matrix_bruto_2_14m_omzet_433k_73_empty_pnl_drop_271k_destin_271k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderopvang t Eekhoorntje deposit 2026-00131193,http://cdn.staatsbladmonitor.be/2026pdf/2026-00131193.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2408; official native PDF 51130 bytes 13p VKT-VZW 26.0.11 m04-f; header 29.05.2026; AV 28.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-10; CreationDate 2026-06-02 08:17:03 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Kinderopvang t Eekhoorntje 0414.453.680,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414453680,KBO Public Search FOD Economie,{DAY},official_register,tick2408; Actief; 2 VE; first VE 2.150.803.269; zetel Guldensporenlaan 65 3010 Leuven since 21.02.2001; naam VZW KINDEROPVANG T EEKHOORNTJE since 14.12.2005; begindatum 21.06.1974; RSZ2025 88.911; RSZ-werkgever since 01.07.1974; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; slorpte Het Kinderhofje 0459.530.471 since 01.01.2025; FOI info@eekhoorntje.be; NOT 3Wplus 0893.870.539; NOT De Mereltjes 0412.778.352; NOT De Hoeksteen 0765.439.866",
    f"{SRC_SBM},Staatsbladmonitor fiche t Eekhoorntje 0414453680 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0414453680,Staatsbladmonitor,{DAY},official_register,tick2408; deposit-id 2026-00131193 YE 2025-01-01>2025-12-31 neerlegging 2026-05-29 and CDN Last-Modified 2026-06-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},t Eekhoorntje FOI contact leftover city_leuven CIK,https://eekhoorntje.eu/,Kinderopvang t Eekhoorntje vzw,{DAY},foi_contact,tick2408; FOI info@eekhoorntje.be; zetel Guldensporenlaan 65 3010 Leuven; 2 VE groepsopvang 85 + BKO 45 Kessel-Lo + BKO 30 Kinderhofje Weldadigheidsstraat 71 3000 Leuven; leftover city_leuven after 3Wplus@2407; NOT 3Wplus; NOT De Mereltjes; NOT De Hoeksteen; NOT Ter Eecken; NOT De Kade; NOT CFR Zelzate; NOT VERBINT; NOT ARC; NOT Heuvelheem; NOT CAR Halle Asse; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR Noorderkempen scan; NOT Antenne 3000",
])
print("sources ok")
