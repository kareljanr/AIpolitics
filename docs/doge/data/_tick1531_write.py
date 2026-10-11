#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1531 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwlm"
SRC = "src_cwlm_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00099651.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Limburg official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Limburg,2026-08-20,budget,tick1531; official NBB WVV VOL-VZW JR2025 PDF 49p / 528761 bytes; deposit 2026-00099651 Initial (SBM single 2025 deposit filed 2026-05-04; NBB consult published-deposits API 403 this tick; no later Aanpassing visible); AV 29.04.2026; header 04.05.2026; pdfinfo created 04.05.2026 06:38:41 UTC; model VOL-VZW 26.0.10 m05-f; euros PDF only",
        "src_cwlm_kbo_0464328310,KBO CAW Limburg 0464.328.310,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464328310,FPS Economy KBO,2026-08-20,official_register,tick1531; leftover recognized Flemish CAW / leftover zorg EVA of mined Genk + leftover of remaining Limburg municipalities (province-wide); zetel Welzijnscampus 19 bus 2 3600 Genk; KBO 0464.328.310 Actief; prefix cwlm unused",
        "src_cwlm_nbb_consult,NBB Consult CAW Limburg published deposits 0464328310,https://consult.cbso.nbb.be/consult-enterprise/0464328310,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1531; leftover zorg EVA; JR2025 reference 2026-00099651 Initial filing 04.05.2026 year-end 31.12.2025 Volledig model vereniging; SBM single 2025 deposit; NBB consult API 403 this tick",
        "src_cwlm_foi_contact,CAW Limburg FOI channel (guy.guisson@cawlimburg.be),https://www.caw.be/over-caw/organisatie/caw-limburg/,CAW Limburg,2026-08-20,official_web,tick1531; leftover recognized CAW of mined Genk; FOI ready not sent; Welzijnscampus 19 bus 2 3600 Genk; official WVV identification email guy.guisson@cawlimburg.be; NOT leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwlm," in raw or raw.startswith(b"caw_cwlm,"):
        raise SystemExit("caw_cwlm already present")
    if b"0464.328.310" in raw or b"0464328310" in raw:
        raise SystemExit("CAW Limburg KBO already present as entity")
    row = (
        "caw_cwlm,CAW Limburg VZW / Centrum voor Algemeen Welzijnswerk Limburg (leftover recognized Flemish CAW / leftover zorg EVA of mined Genk + leftover of remaining Limburg municipalities province-wide; NOT leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Limburg ASBL (EVA bien-etre residuel),"
        "CAW Limburg leftover recognized Flemish CAW / zorg EVA of mined Genk + remaining Limburg municipalities (not leftover CGG Integra / leftover CGG Kohesi / leftover Wonen in Limburg / leftover LeefGoed / leftover CAW Oost-Brabant / leftover CAW Halle-Vilvoorde / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_genk,nl,https://www.caw.be/over-caw/organisatie/caw-limburg/,guy.guisson@cawlimburg.be,Welzijnscampus 19 bus 2 3600 Genk,"
        "tick1531 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Genk after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant hunt; KBO 0464.328.310 Actief; zetel Genk 3600; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 17396760 opbr 25346747 omzet 2047768 73 23037493 pers 20148522 271.8 VTE cash 2737774 debt 8313821 pnl 117423; FOI ready not sent; parent city_genk; prefix cwlm; NOT leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwlm")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
