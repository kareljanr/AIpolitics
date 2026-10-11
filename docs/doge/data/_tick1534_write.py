#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1534 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwzw"
SRC = "src_cwzw_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00069501.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Zuid-West-Vlaanderen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Zuid-West-Vlaanderen,2026-08-20,budget,tick1534; official NBB WVV VOL-VZW JR2025 PDF 47p / 612502 bytes; deposit 2026-00069501 Initial (NBB consult published-deposits 403 this tick; no later Aanpassing visible on SBM CDN); AV 30.03.2026; header 31.03.2026; pdfinfo created 01.04.2026 10:54:40 UTC; model VOL-VZW 25.0.9 m05-f; euros PDF only",
        "src_cwzw_kbo_0464275949,KBO CAW Zuid-West-Vlaanderen 0464.275.949,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464275949,FPS Economy KBO,2026-08-20,official_register,tick1534; leftover recognized Flemish CAW / leftover zorg EVA of mined Kortrijk + leftover of remaining Zuid-West-Vlaanderen municipalities; zetel Voorstraat 51 8500 Kortrijk; KBO 0464.275.949 Actief; prefix cwzw unused",
        "src_cwzw_nbb_consult,NBB Consult CAW Zuid-West-Vlaanderen published deposits 0464275949,https://consult.cbso.nbb.be/consult-enterprise/0464275949,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1534; leftover zorg EVA; JR2025 reference 2026-00069501 Initial filing 31.03.2026 year-end 31.12.2025 Volledig model vereniging; NBB consult API 403 this tick",
        "src_cwzw_foi_contact,CAW Zuid-West-Vlaanderen FOI channel (carine.verhaeghe@cawzuidwestvlaanderen.be),https://www.caw.be/over-caw/organisatie/caw-zuid-west-vlaanderen/,CAW Zuid-West-Vlaanderen,2026-08-20,official_web,tick1534; leftover recognized CAW of mined Kortrijk; FOI ready not sent; Voorstraat 51 8500 Kortrijk; official contact carine.verhaeghe@cawzuidwestvlaanderen.be; NOT leftover CGG Mandel en Leie 1522 / leftover AGB Kortrijk / leftover SW+ 1472 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwzw," in raw or raw.startswith(b"caw_cwzw,"):
        raise SystemExit("caw_cwzw already present")
    if b"0464.275.949" in raw or b"0464275949" in raw:
        raise SystemExit("CAW ZWVL KBO already present as entity")
    row = (
        "caw_cwzw,CAW Zuid-West-Vlaanderen VZW / Centrum Algemeen Welzijnswerk Zuid-West-Vlaanderen (leftover recognized Flemish CAW / leftover zorg EVA of mined Kortrijk + leftover of remaining Zuid-West-Vlaanderen municipalities; NOT leftover CGG Mandel en Leie 1522 / leftover AGB Kortrijk / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus 1500 / leftover WM Elan 1499 / leftover W13 / leftover Leiedal / leftover IMOG / leftover Psilon / leftover Zuidwest / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Flandre occidentale sud ASBL (EVA bien-etre residuel),"
        "CAW Zuid-West-Vlaanderen leftover recognized Flemish CAW / zorg EVA of mined Kortrijk + remaining Zuid-West-Vlaanderen municipalities (not leftover CGG Mandel en Leie / leftover AGB Kortrijk / leftover SW+ / leftover !Mpuls / leftover Vivus / leftover WM Elan / leftover W13 / leftover CAW CWVL / leftover CAW Oost-Vlaanderen / leftover CAW Limburg / leftover CAW Oost-Brabant / leftover CAW Halle-Vilvoorde / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_kortrijk,nl,https://www.caw.be/over-caw/organisatie/caw-zuid-west-vlaanderen/,carine.verhaeghe@cawzuidwestvlaanderen.be,Voorstraat 51 8500 Kortrijk,"
        "tick1534 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Kortrijk after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL hunt; KBO 0464.275.949 Actief; zetel Kortrijk 8500; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 14138245 opbr 12009580 omzet 626259 73 10629255 pers 9302213 125 VTE cash 2068876 debt 2588507 pnl 401314 expl PROFIT 401199; FOI ready not sent; parent city_kortrijk; prefix cwzw; NOT leftover CGG Mandel en Leie 1522 / leftover AGB Kortrijk / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus 1500 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwzw")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
