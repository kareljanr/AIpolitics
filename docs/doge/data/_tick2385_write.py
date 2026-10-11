#!/usr/bin/env python3
"""Surgical tick 2385 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_ascendere"
SRC_PDF = "src_ascendere_jr2025_nbb_pdf_2385"
SRC_KBO = "src_ascendere_kbo_2385"
SRC_SBM = "src_ascendere_sbm_2385"
SRC_SITE = "src_ascendere_site_2385"
COMM = "comm_ascendere_jr2025_statutory_omzet_4_34m_73_866k_pnl_drop"
LB = "lb_ascendere_omzet_4_34m_73_866k_pnl_drop_jr2025"
GAP = "gap_ascendere_riziv_vl_vaph_matrix_omzet_4_34m_73_866k_pnl_drop_destin_empty_l5"
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
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Ascendere deposit 2026-00209823,http://cdn.staatsbladmonitor.be/2026pdf/2026-00209823.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2385; official native PDF 551394 bytes 31p VKT-VZW 25.0.13 m04-f; header 29.06.2026; AV 16.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-11; CreationDate 2026-06-29 07:57:47 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope",
    f"{SRC_KBO},KBO Ascendere vzw 0409.470.553,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409470553,KBO Public Search FOD Economie,{DAY},official_register,tick2385; Actief; 4 VE; zetel Melkerij 25 9900 Eeklo since 18.11.2002; RSZ2025 86.959; voorzitter Guido Schelfaut; dagelijks bestuur Bart Volders; VE 2.146.406.991 CAR De Springplank Kasteeldreef 16 9340 Lede",
    f"{SRC_SBM},Staatsbladmonitor fiche Ascendere 0409470553 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0409470553,Staatsbladmonitor,{DAY},official_register,tick2385; deposit-id 2026-00209823 and CDN Last-Modified 2026-07-11; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Ascendere FOI contact / Departement Zorg VAZG 9.53.608.96,https://ascendere.be/,Ascendere vzw,{DAY},foi_contact,tick2385; FOI info@ascendere.be / bart.volders@ascendere.be; zetel Melkerij 25 9900 Eeklo; leftover city_eeklo; 4 CAR campussen; NOT Kloosterstraat 6; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie",
])
print("sources ok")
