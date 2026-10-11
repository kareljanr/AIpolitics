#!/usr/bin/env python3
"""Surgical tick 2398 writes — sources append only."""
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2398_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
SRC_PDF = "src_halleasse_jr2025_nbb_pdf_2398"
SRC_KBO = "src_halleasse_kbo_2398"
SRC_SBM = "src_halleasse_sbm_2398"
SRC_SITE = "src_halleasse_site_2398"
GAP = "gap_halleasse_riziv_vl_vaph_matrix_bruto_2_34m_omzet73_empty_pnl_jump_destin_505k_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR Land van Halle en Asse deposit 2026-00364866,http://cdn.staatsbladmonitor.be/2026pdf/2026-00364866.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2398; official native PDF 50482 bytes 13p VKT-VZW 26.0.15 m04-f; header 31.07.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-07; CreationDate 2026-07-31 14:02:40 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
    f"{SRC_KBO},KBO CAR Land van Halle en Asse 0425.788.230,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0425788230,KBO Public Search FOD Economie,{DAY},official_register,tick2398; Actief; 1 VE 2.155.707.808 Revalidatiecentrum Land van Halle-Pajottenland Ziekenhuislaan 35 Halle; zetel Ziekenhuislaan 35 1500 Halle; RSZ2025 86.959; NOT Waas 0415.472.279; NOT CAR Accent 0413.208.122; NOT CAR Horizon 0418.529.759",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Halle Asse 0425788230 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0425788230,Staatsbladmonitor,{DAY},official_register,tick2398; deposit-id 2026-00364866 YE 2025-01-01>2025-12-31 neerlegging 2026-07-31 and CDN Last-Modified 2026-08-07; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Halle Asse FOI contact / leftover city_halle + leftover city_asse ambulante revalidatie,https://www.car-halle-asse.be/prijslijst/,CAR Land van Halle en Asse vzw,{DAY},foi_contact,tick2398; FOI halle@car-halle-asse.be; zetel Ziekenhuislaan 35 1500 Halle; RIZIV 96557263; VAZG HCO 29588; leftover city_halle after Waas@2397; NOT Waas; NOT CAR Accent; NOT CAR Horizon; NOT ZWZ; NOT Zonnebloem; NOT CAR Houtland; NOT De Schans; NOT LDSST; NOT BW Kohesi; NOT REVA Kohesi; NOT CGG Kohesi; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; NOT m-accent Eeklo",
])
print("sources ok")
