#!/usr/bin/env python3
"""Surgical tick 2395 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2395_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_horizon_jr2025_nbb_pdf_2395"
SRC_KBO = "src_horizon_kbo_2395"
SRC_SBM = "src_horizon_sbm_2395"
SRC_SITE = "src_horizon_site_2395"
GAP = "gap_horizon_riziv_vl_vaph_matrix_omzet_3_00m_73_464k_pnl_drop_destin_246k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR Horizon Geraardsbergen deposit 2026-00268911,http://cdn.staatsbladmonitor.be/2026pdf/2026-00268911.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2395; official native PDF 44340 bytes 11p VKT-VZW 26.0.15 m04-f; header 08.07.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-29; CreationDate 2026-07-08 23:12:36 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Horizon vzw 0418.529.759,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418529759,KBO Public Search FOD Economie,{DAY},official_register,tick2395; Actief; 1 VE 2.154.325.854 Oudenaardsestraat 215 Geraardsbergen; zetel Oudenaardsestraat 215 9500 Geraardsbergen since 14.04.1995; RSZ2025 86.959; Psychologencommissie; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019",
    f"{SRC_SBM},Staatsbladmonitor fiche Horizon 0418529759 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0418529759,Staatsbladmonitor,{DAY},official_register,tick2395; deposit-id 2026-00268911 YE 2025-01-01>2025-12-31 neerlegging 2026-07-08 and CDN Last-Modified 2026-07-29; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Horizon FOI contact / leftover city_geraardsbergen ambulante revalidatie,https://www.horizonvzw.be/,Horizon vzw,{DAY},foi_contact,tick2395; FOI erwin.franceus@horizonvzw.be; zetel Oudenaardsestraat 215 9500 Geraardsbergen; leftover city_geraardsbergen after ZWZ@2394; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker",
])
print("sources ok")
