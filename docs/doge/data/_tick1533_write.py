#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1533 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwcw"
SRC = "src_cwcw_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00088320.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Centraal-West-Vlaanderen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Centraal-West-Vlaanderen,2026-08-20,budget,tick1533; official NBB WVV VOL-VZW JR2025 PDF 49p / 1834911 bytes; deposit 2026-00088320 Initial (NBB consult published-deposits timed out this tick; no later Aanpassing visible on SBM CDN); AV 22.04.2026; header 27.04.2026; pdfinfo created 27.04.2026 12:18:19 UTC; model VOL-VZW 26.0.10 m05-f; euros PDF only",
        "src_cwcw_kbo_0464580708,KBO CAW Centraal-West-Vlaanderen 0464.580.708,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464580708,FPS Economy KBO,2026-08-20,official_register,tick1533; leftover recognized Flemish CAW / leftover zorg EVA of mined Izegem + leftover of remaining Centraal-West-Vlaanderen municipalities; zetel Krekelstraat 56 8870 Izegem; KBO 0464.580.708 Actief; prefix cwcw unused",
        "src_cwcw_nbb_consult,NBB Consult CAW Centraal-West-Vlaanderen published deposits 0464580708,https://consult.cbso.nbb.be/consult-enterprise/0464580708,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1533; leftover zorg EVA; JR2025 reference 2026-00088320 Initial filing 27.04.2026 year-end 31.12.2025 Volledig model vereniging; NBB consult API timeout this tick",
        "src_cwcw_foi_contact,CAW Centraal-West-Vlaanderen FOI channel (administratie@cawcentraalwestvlaanderen.be),https://www.caw.be/over-caw/organisatie/caw-centraal-west-vlaanderen/,CAW Centraal-West-Vlaanderen,2026-08-20,official_web,tick1533; leftover recognized CAW of mined Izegem; FOI ready not sent; Krekelstraat 56 8870 Izegem; official contact administratie@cawcentraalwestvlaanderen.be; NOT leftover CGG Largo 1518 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwcw," in raw or raw.startswith(b"caw_cwcw,"):
        raise SystemExit("caw_cwcw already present")
    if b"0464.580.708" in raw or b"0464580708" in raw:
        raise SystemExit("CAW CWVL KBO already present as entity")
    row = (
        "caw_cwcw,CAW Centraal-West-Vlaanderen VZW / Centrum Algemeen Welzijnswerk Centraal-West-Vlaanderen (leftover recognized Flemish CAW / leftover zorg EVA of mined Izegem + leftover of remaining Centraal-West-Vlaanderen municipalities; NOT leftover CGG Largo 1518 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Flandre occidentale centrale ASBL (EVA bien-etre residuel),"
        "CAW Centraal-West-Vlaanderen leftover recognized Flemish CAW / zorg EVA of mined Izegem + remaining Centraal-West-Vlaanderen municipalities (not leftover CGG Largo / leftover Motena Roeselare / leftover Thuiswest / leftover CAW Oost-Vlaanderen / leftover CAW Limburg / leftover CAW Oost-Brabant / leftover CAW Halle-Vilvoorde / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_izegem,nl,https://www.caw.be/over-caw/organisatie/caw-centraal-west-vlaanderen/,administratie@cawcentraalwestvlaanderen.be,Krekelstraat 56 8870 Izegem,"
        "tick1533 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Izegem after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen hunt; KBO 0464.580.708 Actief; zetel Izegem 8870; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 8483960 opbr 9188129 omzet 187872 73 8739673 pers 7318691 108.9 VTE cash 901859 debt 3002354 pnl -99538; FOI ready not sent; parent city_izegem; prefix cwcw; NOT leftover CGG Largo 1518 / leftover Motena Roeselare / leftover Thuiswest 1493 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwcw")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
