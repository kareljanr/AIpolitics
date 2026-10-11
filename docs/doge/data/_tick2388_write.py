#!/usr/bin/env python3
"""Surgical tick 2388 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2388_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_reva_kohesi"
SRC_PDF = "src_revakohesi_jr2025_nbb_pdf_2388"
SRC_KBO = "src_revakohesi_kbo_2388"
SRC_SBM = "src_revakohesi_sbm_2388"
SRC_SITE = "src_revakohesi_site_2388"
GAP = "gap_revakohesi_riziv_vl_vaph_matrix_omzet_5_96m_73_1_86m_pnl_drop_destin_54k_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 REVA Kohesi deposit 2026-00244637,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244637.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2388; official native PDF 660026 bytes 52p VOL-VZW 25.0.13 m05-f; header 29.06.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 02:11:24 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO REVA Kohesi vzw 0410.121.641,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410121641,KBO Public Search FOD Economie,{DAY},official_register,tick2388; Actief; 8 VE CAR Hasselt 2.138.290.764 + Reval Hasselt 2.138.290.863 + Campus Harmonie 2.138.290.962 + Reval Noord-Limburg 2.138.291.061 + Reval Genk 2.138.291.160 + CAR Genk 2.147.477.852 + KDV Maasmechelen 2.183.900.857 + CAR Beringen 2.331.471.214; zetel Ilgatlaan 11 bus 4 3500 Hasselt; RSZ2025 88.999; voorzitter Erik Ottenbourgs; gedelegeerd bestuurder Johan Gommers; NOT CGG Kohesi 0472.466.907",
    f"{SRC_SBM},Staatsbladmonitor fiche REVA Kohesi 0410121641 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0410121641,Staatsbladmonitor,{DAY},official_register,tick2388; deposit-id 2026-00244637 YE 2025-01-01>2025-12-31 neerlegging 2026-06-29 and CDN Last-Modified 2026-07-25; NBB consult reference 2026-00244637 year-end 30.12.2025; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},REVA Kohesi FOI contact / CAR+Reval+KDV campuses,https://www.kohesi.be/,REVA Kohesi vzw,{DAY},foi_contact,tick2388; FOI info@kohesi.be; zetel Ilgatlaan 11 bus 4 3500 Hasselt; leftover city_hasselt; NOT CGG Kohesi 0472.466.907; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")
