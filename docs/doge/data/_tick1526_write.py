#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1526 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwkp"
SRC = "src_cwkp_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00128692.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW De Kempen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW De Kempen,2026-08-20,budget,tick1526; official NBB WVV VOL-VZW JR2025 PDF 42p / 3801416 bytes; deposit 2026-00128692 Aanpassing; prior deposit 2026-00117588 39p superseded; AV 12.05.2026; header 01.06.2026; pdfinfo created 01.06.2026 09:55:43 UTC; model VOL-VZW 26.0.11 m05-f; euros PDF only",
        "src_cwkp_kbo_0464222895,KBO CAW De Kempen 0464.222.895,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464222895,FPS Economy KBO,2026-08-20,official_register,tick1526; leftover recognized Flemish CAW / leftover zorg EVA of mined Herentals + leftover of 27 Turnhout-arrondissement municipalities; zetel Hofkwartier 23 2200 Herentals; KBO 0464.222.895; prefix cwkp unused",
        "src_cwkp_nbb_consult,NBB Consult CAW De Kempen published deposits 0464222895,https://consult.cbso.nbb.be/consult-enterprise/0464222895,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1526; leftover zorg EVA; JR2025 reference 2026-00128692 Aanpassing filing 01.06.2026 year-end 31.12.2025 Volledig model vereniging; prior 2026-00117588 22.05.2026 superseded",
        "src_cwkp_foi_contact,CAW De Kempen FOI channel (onthaal@cawdekempen.be),https://www.caw.be/over-caw/organisatie/caw-de-kempen/,CAW De Kempen,2026-08-20,official_web,tick1526; leftover recognized CAW of mined Herentals; FOI ready not sent; Hofkwartier 23 2200 Herentals; NOT leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen 1504 / leftover Erfgoed Noorderkempen 1426",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwkp," in raw or raw.startswith(b"caw_cwkp,"):
        raise SystemExit("caw_cwkp already present")
    if b"0464.222.895" in raw or b"0464222895" in raw:
        raise SystemExit("CAW De Kempen KBO already present as entity")
    row = (
        "caw_cwkp,CAW De Kempen VZW / Centrum Algemeen Welzijnswerk De Kempen (leftover recognized Flemish CAW / leftover zorg EVA of mined Herentals + leftover of 27 Turnhout-arrondissement municipalities; NOT leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen 1504 / leftover Erfgoed Noorderkempen 1426 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW De Kempen ASBL (EVA bien-etre residuel),"
        "CAW De Kempen leftover recognized Flemish CAW / zorg EVA of mined Herentals + 27 Turnhout-arrondissement municipalities (not leftover CGG Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen / leftover Erfgoed Noorderkempen / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_herentals,nl,https://www.caw.be/over-caw/organisatie/caw-de-kempen/,onthaal@cawdekempen.be,Hofkwartier 23 2200 Herentals,"
        "tick1526 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Herentals after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen hunt; KBO 0464.222.895 Actief; live JR2025 official NBB WVV VOL-VZW PDF Aanpassing; sourced euros assets 19957060 opbr 13824525 omzet 595237 73 12796950 pers 10852214 148 VTE cash 674251 debt 7514813 pnl 109444; FOI ready not sent; parent city_herentals; prefix cwkp; NOT leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwkp")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
