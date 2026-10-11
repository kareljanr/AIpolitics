#!/usr/bin/env python3
"""Surgical tick 2386 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2386_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_car_deklinker"
SRC_PDF = "src_deklinker_jr2025_nbb_pdf_2386"
SRC_KBO = "src_deklinker_kbo_2386"
SRC_SBM = "src_deklinker_sbm_2386"
SRC_SITE = "src_deklinker_site_2386"
GAP = "gap_deklinker_riziv_vl_vaph_matrix_bruto_1_62m_omzet73_empty_destin_179k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR De Klinker Ieper deposit 2026-00241698,http://cdn.staatsbladmonitor.be/2026pdf/2026-00241698.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2386; official native PDF 55691 bytes 16p VKT-VZW 23.0.10 m04-f; header 02.07.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-02 22:10:11 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope",
    f"{SRC_KBO},KBO De Klinker Centrum voor Ambulante Revalidatie vzw 0430.535.290,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0430535290,KBO Public Search FOD Economie,{DAY},official_register,tick2386; Actief; 1 VE 2.154.433.940; zetel Cartonstraat 53 8900 Ieper since 01.10.2015; RSZ2025 86.959; voorzitter Luc Colman; gedelegeerd bestuurder Johan Messely; NOT school De Klinker Rotselaar 0464.016.326",
    f"{SRC_SBM},Staatsbladmonitor fiche De Klinker 0430535290 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0430535290,Staatsbladmonitor,{DAY},official_register,tick2386; deposit-id 2026-00241698 YE 2025-01-01>2025-12-31 neerlegging 2026-07-03 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR De Klinker FOI contact / RIZIV 9.53.579.28 / VAPH 579,https://www.cardeklinker.be/,CAR De Klinker vzw,{DAY},foi_contact,tick2386; FOI info@cardeklinker.be; zetel Cartonstraat 53 8900 Ieper; leftover city_ieper; NOT deklinker.be school Rotselaar; NOT Kloosterstraat 6; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")
