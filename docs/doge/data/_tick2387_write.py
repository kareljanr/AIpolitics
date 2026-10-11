#!/usr/bin/env python3
"""Surgical tick 2387 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2387_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_car_de_hert"
SRC_PDF = "src_dehert_jr2025_nbb_pdf_2387"
SRC_KBO = "src_dehert_kbo_2387"
SRC_SBM = "src_dehert_sbm_2387"
SRC_SITE = "src_dehert_site_2387"
GAP = "gap_dehert_riziv_vl_vaph_matrix_omzet_1_87m_73_634k_pnl_jump_destin_empty_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR De Hert Aalst deposit 2026-00174560,http://cdn.staatsbladmonitor.be/2026pdf/2026-00174560.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2387; official native PDF 48928 bytes 12p VKT-VZW 26.0.15 m04-f; header 19.06.2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-22; CreationDate 2026-06-19 06:54:18 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope",
    f"{SRC_KBO},KBO CAR DE HERT vzw 0409.371.672,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409371672,KBO Public Search FOD Economie,{DAY},official_register,tick2387; Actief; 1 VE 2.153.754.445 Revalidatiecentrum R. De Hert; zetel Rozendreef 250 9300 Aalst since 30.04.2015; RSZ2025 86.959; voorzitter Kristof Vandenbogaerde; secretaris Marie-Therese De Wael; NOT CGG Kohesi 0472.466.907; NOT REVA Kohesi 0410.121.641",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR De Hert 0409371672 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0409371672,Staatsbladmonitor,{DAY},official_register,tick2387; deposit-id 2026-00174560 YE 2025-01-01>2025-12-31 neerlegging 2026-06-19 and CDN Last-Modified 2026-06-22; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR De Hert FOI contact / VAZG 9.65.105.45 / VAPH R/105,https://www.cardehert.be/,CAR De Hert vzw,{DAY},foi_contact,tick2387; FOI info@cardehert.be; zetel Rozendreef 250 9300 Aalst; leftover city_aalst; NOT CGG Kohesi; NOT REVA Kohesi; NOT Kloosterstraat 6; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")
