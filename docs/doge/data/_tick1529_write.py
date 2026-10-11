#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1529 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwhv"
SRC = "src_cwhv_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00124483.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Halle-Vilvoorde official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Halle-Vilvoorde,2026-08-20,budget,tick1529; official NBB WVV VOL-VZW JR2025 PDF 45p / 1304481 bytes; deposit 2026-00124483 Initial (no later Aanpassing on NBB consult); AV 26.05.2026; header 27.05.2026; pdfinfo created 28.05.2026 23:49:30 UTC; model VOL-VZW 26.0.11 m05-f; euros PDF only",
        "src_cwhv_kbo_0469702605,KBO CAW Halle-Vilvoorde 0469.702.605,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0469702605,FPS Economy KBO,2026-08-20,official_register,tick1529; leftover recognized Flemish CAW / leftover zorg EVA of mined Asse + leftover of 35 Halle-Vilvoorde municipalities; zetel Poverstraat 75 bus 48 1731 Asse (Zellik); KBO 0469.702.605 Actief; prefix cwhv unused",
        "src_cwhv_nbb_consult,NBB Consult CAW Halle-Vilvoorde published deposits 0469702605,https://consult.cbso.nbb.be/consult-enterprise/0469702605,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1529; leftover zorg EVA; JR2025 reference 2026-00124483 Initial filing 27.05.2026 year-end 30.12.2025 Volledig model vereniging; no later Aanpassing",
        "src_cwhv_foi_contact,CAW Halle-Vilvoorde FOI channel (onthaal@cawhallevilvoorde.be),https://www.caw.be/over-caw/organisatie/caw-halle-vilvoorde/,CAW Halle-Vilvoorde,2026-08-20,official_web,tick1529; leftover recognized CAW of mined Asse; FOI ready not sent; Poverstraat 75 bus 48 1731 Asse; official location email onthaal@cawhallevilvoorde.be (KBO email empty); NOT leftover CGG Ahasverus 1517 / leftover AGA Asse / leftover Providentia 1501 / leftover AGB Vilvoorde / leftover Inter-Vilvoordse 1489 / leftover Woonpunt Zennevallei 1485 / leftover CAW Rivierenland 1528 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwhv," in raw or raw.startswith(b"caw_cwhv,"):
        raise SystemExit("caw_cwhv already present")
    if b"0469.702.605" in raw or b"0469702605" in raw:
        raise SystemExit("CAW Halle-Vilvoorde KBO already present as entity")
    row = (
        "caw_cwhv,CAW Halle-Vilvoorde VZW / Centrum Algemeen Welzijnswerk Halle - Vilvoorde (leftover recognized Flemish CAW / leftover zorg EVA of mined Asse + leftover of 35 Halle-Vilvoorde municipalities; NOT leftover CGG Ahasverus 1517 / leftover AGA Asse / leftover Providentia 1501 / leftover AGB Vilvoorde / leftover Inter-Vilvoordse 1489 / leftover Woonpunt Zennevallei 1485 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Halle-Vilvoorde ASBL (EVA bien-etre residuel),"
        "CAW Halle-Vilvoorde leftover recognized Flemish CAW / zorg EVA of mined Asse + 35 Halle-Vilvoorde municipalities (not leftover CGG Ahasverus / leftover AGA Asse / leftover Providentia / leftover AGB Vilvoorde / leftover Inter-Vilvoordse / leftover Woonpunt Zennevallei / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_asse,nl,https://www.caw.be/over-caw/organisatie/caw-halle-vilvoorde/,onthaal@cawhallevilvoorde.be,Poverstraat 75 bus 48 1731 Asse,"
        "tick1529 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Asse after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland hunt; KBO 0469.702.605 Actief; zetel Zellik 1731 Asse; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 13485378 opbr 12971653 omzet 75857 73 12731598 pers 11730941 159.2 VTE cash 3955937 debt 2608782 pnl -1053552; FOI ready not sent; parent city_asse; prefix cwhv; NOT leftover CGG Ahasverus 1517 / leftover AGA Asse / leftover Providentia 1501 / leftover AGB Vilvoorde / leftover Inter-Vilvoordse 1489 / leftover Woonpunt Zennevallei 1485 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwhv")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
