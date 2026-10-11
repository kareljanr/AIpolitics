#!/usr/bin/env python3
"""Surgical tick 2397 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2397_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_waas_jr2025_nbb_pdf_2397"
SRC_KBO = "src_waas_kbo_2397"
SRC_SBM = "src_waas_sbm_2397"
SRC_SITE = "src_waas_site_2397"
GAP = "gap_waas_riziv_vl_vaph_matrix_bruto_1_64m_omzet73_empty_pnl_drop_3k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Waas Revalidatiecentrum Lokeren deposit 2026-00243160,http://cdn.staatsbladmonitor.be/2026pdf/2026-00243160.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2397; official native PDF 49462 bytes 13p VKT-VZW 26.0.15 m04-f; header 30.06.2026; AV 26.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-25; CreationDate 2026-07-03 01:08:13 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO Waas Revalidatiecentrum Lokeren 0415.472.279,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415472279,KBO Public Search FOD Economie,{DAY},official_register,tick2397; Actief; 1 VE 2.153.799.381 Waas Revalidatiecentrum Lokeren Luikstraat 109 Lokeren; zetel Luikstraat 109 9160 Lokeren; RSZ2025 86.959; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759",
    f"{SRC_SBM},Staatsbladmonitor fiche Waas Revalidatiecentrum 0415472279 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0415472279,Staatsbladmonitor,{DAY},official_register,tick2397; deposit-id 2026-00243160 YE 2025-01-01>2025-12-31 neerlegging 2026-06-30 and CDN Last-Modified 2026-07-25; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Waas Revalidatiecentrum FOI contact / leftover city_lokeren ambulante revalidatie,https://www.waasrevalidatiecentrum.be/,Waas Revalidatiecentrum Lokeren vzw,{DAY},foi_contact,tick2397; FOI kaat.degeest@waasrevalidatiecentrum.be; zetel Luikstraat 109 9160 Lokeren; leftover city_lokeren after CAR Accent@2396; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo",
])
print("sources ok")
