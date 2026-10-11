#!/usr/bin/env python3
"""Surgical tick 2393 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2393_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_zonnebloem_jr2025_nbb_pdf_2393"
SRC_KBO = "src_zonnebloem_kbo_2393"
SRC_SBM = "src_zonnebloem_sbm_2393"
SRC_SITE = "src_zonnebloem_site_2393"
GAP = "gap_zonnebloem_vaph_mfc_matrix_bruto_4_58m_omzet73_empty_pnl_drop_destin_empty_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Zonnebloem deposit 2026-00254348,http://cdn.staatsbladmonitor.be/2026pdf/2026-00254348.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2393; official native PDF 49599 bytes 13p VKT-VZW 26.0.15 m04-f; header 06.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-26; CreationDate 2026-07-06 08:56:33 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Zonnebloem vzw 0421.039.386,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421039386,KBO Public Search FOD Economie,{DAY},official_register,tick2393; Actief; 2 VE 2.155.011.089 Steenstraat 14 Kortrijk + 2.365.797.138 KDV Madelief Zeger van Heulestraat 2; zetel Steenstraat 14 8501 Kortrijk since 30.01.2001; RSZ2025 87.201; Aanbestedende overheid since 18.01.2003; Kinderopvang VG since 14.09.2022; 9 functiehouders; NOT CAR Houtland-Westkust 0408.436.019; NOT Leieborg; NOT CAR Overleie 0454.250.505",
    f"{SRC_SBM},Staatsbladmonitor fiche Zonnebloem 0421039386 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0421039386,Staatsbladmonitor,{DAY},official_register,tick2393; deposit-id 2026-00254348 YE 2025-01-01>2025-12-31 neerlegging 2026-07-06 and CDN Last-Modified 2026-07-26; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Zonnebloem FOI contact / leftover city_kortrijk VAPH MFC + KDV Madelief,https://www.zonnebloemvzw.be/,Zonnebloem vzw,{DAY},foi_contact,tick2393; FOI algemeen@zonnebloemvzw.be; zetel Steenstraat 14 8501 Kortrijk Heule; leftover city_kortrijk after Houtland@2392; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker",
])
print("sources ok")
