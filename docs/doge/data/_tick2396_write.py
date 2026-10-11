#!/usr/bin/env python3
"""Surgical tick 2396 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2396_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_accent_jr2025_nbb_pdf_2396"
SRC_KBO = "src_accent_kbo_2396"
SRC_SBM = "src_accent_sbm_2396"
SRC_SITE = "src_accent_site_2396"
GAP = "gap_accent_riziv_vl_vaph_matrix_bruto_1_24m_omzet73_empty_pnl_loss_17k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR Accent Kortrijk deposit 2026-00215981,http://cdn.staatsbladmonitor.be/2026pdf/2026-00215981.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2396; official native PDF 47901 bytes 12p VKT-VZW 25.0.13 m04-f; header 29.06.2026; AV 01.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-12; CreationDate 2026-06-29 23:24:36 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Centrum voor Ambulante Revalidatie Accent 0413.208.122,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413208122,KBO Public Search FOD Economie,{DAY},official_register,tick2396; Actief; 1 VE 2.153.765.531 Revalidatiecentrum ACCENT Lagaeplein 12 Kortrijk; zetel Lagaeplein(Heu) 12/14 8501 Kortrijk since 03.05.2004; RSZ2025 86.959; NOT Zonnebloem 0421.039.386; NOT m-accent Eeklo 0465.841.411; NOT CAR Horizon 0418.529.759",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Accent 0413208122 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0413208122,Staatsbladmonitor,{DAY},official_register,tick2396; deposit-id 2026-00215981 YE 2025-01-01>2025-12-31 neerlegging 2026-06-29 and CDN Last-Modified 2026-07-12; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Accent FOI contact / leftover city_kortrijk ambulante revalidatie,https://www.revaccent.be/,CAR Accent vzw,{DAY},foi_contact,tick2396; FOI info@revaccent.be; zetel Lagaeplein 12/14 8501 Kortrijk-Heule; leftover city_kortrijk after CAR Horizon@2395; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo",
])
print("sources ok")
