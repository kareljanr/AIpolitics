#!/usr/bin/env python3
"""Surgical tick 2392 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2392_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_car_houtland"
SRC_PDF = "src_houtland_jr2025_nbb_pdf_2392"
SRC_KBO = "src_houtland_kbo_2392"
SRC_SBM = "src_houtland_sbm_2392"
SRC_SITE = "src_houtland_site_2392"
GAP = "gap_houtland_riziv_vl_vaph_matrix_omzet_4_93m_73_1_06m_pnl_flip_destin_empty_l5"
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
    f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 CAR Houtland-Westkust deposit 2026-00115391,http://cdn.staatsbladmonitor.be/2026pdf/2026-00115391.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2392; official native PDF 958246 bytes 47p VOL-VZW 26.0.11 m05-f; header 20.05.2026; AV 21.04.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-07; CreationDate 2026-05-20 15:48:58 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO CAR Houtland-Westkust vzw 0408.436.019,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408436019,KBO Public Search FOD Economie,{DAY},official_register,tick2392; Actief; 2 VE 2.153.764.244 t Veld Zedelgem + 2.338.771.354 Elora Nieuwpoort; zetel Ichtegemsestraat 32 8211 Zedelgem since 01.10.1990; RSZ2025 86.959; BTW2025 86.959+35.140; Aanbestedende overheid since 18.01.2003; 8 bestuurders; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Houtland-Westkust 0408436019 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0408436019,Staatsbladmonitor,{DAY},official_register,tick2392; deposit-id 2026-00115391 YE 2025-01-01>2025-12-31 neerlegging 2026-05-20 and CDN Last-Modified 2026-06-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Houtland-Westkust FOI contact / leftover city_zedelgem + city_nieuwpoort,https://www.carelora.be/,CAR Houtland-Westkust vzw,{DAY},foi_contact,tick2392; FOI info@carelora.be; zetel Ichtegemsestraat 32 8211 Zedelgem; leftover city_zedelgem + leftover city_nieuwpoort after De Schans@2391; fusie CAR Elora Nieuwpoort + CAR t Veld Aartrijke; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")
