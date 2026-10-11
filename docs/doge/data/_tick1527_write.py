#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1527 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwbr"
SRC = "src_cwbr_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00101211.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Brussel official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Brussel,2026-08-20,budget,tick1527; official NBB WVV VOL-VZW JR2025 PDF 54p / 9312176 bytes; deposit 2026-00101211 Initial (no later Aanpassing on NBB consult); AV 20.04.2026; header 29.04.2026; pdfinfo created 05.05.2026 03:04:48 UTC; model VOL-VZW 25.0.11 m05-f; euros PDF only",
        "src_cwbr_kbo_0464230122,KBO CAW Brussel 0464.230.122,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464230122,FPS Economy KBO,2026-08-20,official_register,tick1527; leftover recognized Flemish CAW / leftover zorg EVA of mined Brussel + leftover of 18 other BHG municipalities; zetel Priemstraat 19A 1000 Brussel; KBO 0464.230.122 Actief; prefix cwbr unused",
        "src_cwbr_nbb_consult,NBB Consult CAW Brussel published deposits 0464230122,https://consult.cbso.nbb.be/consult-enterprise/0464230122,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1527; leftover zorg EVA; JR2025 reference 2026-00101211 Initial filing 29.04.2026 year-end 30.12.2025 Volledig model vereniging; no later Aanpassing",
        "src_cwbr_foi_contact,CAW Brussel FOI channel (algmeen@cawbrussel.be),https://www.caw.be/over-caw/organisatie/caw-brussel/,CAW Brussel,2026-08-20,official_web,tick1527; leftover recognized CAW of mined Brussel; FOI ready not sent; Priemstraat 19A 1000 Brussel; KBO email algmeen@cawbrussel.be; NOT leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwbr," in raw or raw.startswith(b"caw_cwbr,"):
        raise SystemExit("caw_cwbr already present")
    if b"0464.230.122" in raw or b"0464230122" in raw:
        raise SystemExit("CAW Brussel KBO already present as entity")
    row = (
        "caw_cwbr,CAW Brussel VZW / Centrum Algemeen Welzijnswerk Brussel (leftover recognized Flemish CAW / leftover zorg EVA of mined Brussel + leftover of 18 other BHG municipalities; NOT leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Bruxelles ASBL (EVA bien-etre residuel),"
        "CAW Brussel leftover recognized Flemish CAW / zorg EVA of mined Brussel + 18 other BHG municipalities (not leftover CGG Brussel / leftover CAW Antwerpen / leftover CAW De Kempen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_brussel,nl,https://www.caw.be/over-caw/organisatie/caw-brussel/,algmeen@cawbrussel.be,Priemstraat 19A 1000 Brussel,"
        "tick1527 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Brussel after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen hunt; KBO 0464.230.122 Actief; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 6760334 opbr 13378953 omzet 458249 73 12807697 pers 11589623 160.2 VTE cash 926690 debt 3508957 pnl -24907; FOI ready not sent; parent city_brussel; prefix cwbr; NOT leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwbr")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
