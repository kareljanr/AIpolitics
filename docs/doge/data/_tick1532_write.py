#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1532 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwov"
SRC = "src_cwov_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00117344.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Oost-Vlaanderen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Oost-Vlaanderen,2026-08-20,budget,tick1532; official NBB WVV VOL-VZW JR2025 PDF 49p / 1969916 bytes; deposit 2026-00117344 Initial (SBM HTML blacklisted this tick; NBB consult published-deposits API 403 this tick; no later Aanpassing visible); AV 23.04.2026; header 19.05.2026; pdfinfo created 22.05.2026 01:45:18 UTC; model VOL-VZW 26.0.11 m05-f; euros PDF only",
        "src_cwov_kbo_0508774601,KBO CAW Oost-Vlaanderen 0508.774.601,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0508774601,FPS Economy KBO,2026-08-20,official_register,tick1532; leftover recognized Flemish CAW / leftover zorg EVA of mined Gent + leftover of remaining Oost-Vlaanderen municipalities (province-wide); zetel Visserij 153 9000 Gent; KBO 0508.774.601 Actief; prefix cwov unused",
        "src_cwov_nbb_consult,NBB Consult CAW Oost-Vlaanderen published deposits 0508774601,https://consult.cbso.nbb.be/consult-enterprise/0508774601,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1532; leftover zorg EVA; JR2025 reference 2026-00117344 Initial filing 19.05.2026 year-end 31.12.2025 Volledig model vereniging; SBM HTML blacklisted; NBB consult API 403 this tick",
        "src_cwov_foi_contact,CAW Oost-Vlaanderen FOI channel (marleenverhasselt@cawoostvlaanderen.be),https://www.caw.be/over-caw/organisatie/caw-oost-vlaanderen/,CAW Oost-Vlaanderen,2026-08-20,official_web,tick1532; leftover recognized CAW of mined Gent; FOI ready not sent; Visserij 153 9000 Gent; official WVV identification email marleenverhasselt@cawoostvlaanderen.be; NOT leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Dimensa 1466 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwov," in raw or raw.startswith(b"caw_cwov,"):
        raise SystemExit("caw_cwov already present")
    if b"0508.774.601" in raw or b"0508774601" in raw:
        raise SystemExit("CAW Oost-Vlaanderen KBO already present as entity")
    row = (
        "caw_cwov,CAW Oost-Vlaanderen VZW / Centrum Algemeen Welzijnswerk Oost-Vlaanderen (leftover recognized Flemish CAW / leftover zorg EVA of mined Gent + leftover of remaining Oost-Vlaanderen municipalities province-wide; NOT leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Dimensa 1466 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Flandre orientale ASBL (EVA bien-etre residuel),"
        "CAW Oost-Vlaanderen leftover recognized Flemish CAW / zorg EVA of mined Gent + remaining Oost-Vlaanderen municipalities (not leftover CGG Adentro / leftover Thuispunt Gent / leftover Dimensa / leftover CAW Limburg / leftover CAW Oost-Brabant / leftover CAW Halle-Vilvoorde / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_gent,nl,https://www.caw.be/over-caw/organisatie/caw-oost-vlaanderen/,marleenverhasselt@cawoostvlaanderen.be,Visserij 153 9000 Gent,"
        "tick1532 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Gent after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg hunt; KBO 0508.774.601 Actief; zetel Gent 9000; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 32814654 opbr 43872173 omzet 2041949 73 40332909 pers 37299480 506.3 VTE cash 8405654 debt 10810222 pnl -1021215; FOI ready not sent; parent city_gent; prefix cwov; NOT leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover Dimensa 1466 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwov")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
