#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1528 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwrv"
SRC = "src_cwrv_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00090859.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Rivierenland official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Rivierenland,2026-08-20,budget,tick1528; official NBB WVV VOL-VZW JR2025 PDF 50p / 3097588 bytes; deposit 2026-00090859 Initial (no later Aanpassing on NBB consult); AV 27.04.2026; header 28.04.2026; pdfinfo created 28.04.2026 21:20:57 UTC; model VOL-VZW 25.0.11 m05-f; euros PDF only",
        "src_cwrv_kbo_0466852882,KBO CAW Rivierenland 0466.852.882,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466852882,FPS Economy KBO,2026-08-20,official_register,tick1528; leftover recognized Flemish CAW / leftover zorg EVA of mined Mechelen + leftover of 11 other Rivierenland municipalities; zetel Maurits Sabbestraat 119 2800 Mechelen; KBO 0466.852.882 Actief; renamed from CAW Boom-Mechelen-Lier 22.04.2024; prefix cwrv unused",
        "src_cwrv_nbb_consult,NBB Consult CAW Rivierenland published deposits 0466852882,https://consult.cbso.nbb.be/consult-enterprise/0466852882,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1528; leftover zorg EVA; JR2025 reference 2026-00090859 Initial filing 28.04.2026 year-end 31.12.2025 Volledig model vereniging; no later Aanpassing",
        "src_cwrv_foi_contact,CAW Rivierenland FOI channel (centraal.secretariaat@cawboommechelenlier.be),https://www.caw.be/over-caw/organisatie/caw-rivierenland/,CAW Rivierenland,2026-08-20,official_web,tick1528; leftover recognized CAW of mined Mechelen; FOI ready not sent; Maurits Sabbestraat 119 2800 Mechelen; KBO email centraal.secretariaat@cawboommechelenlier.be; NOT leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwrv," in raw or raw.startswith(b"caw_cwrv,"):
        raise SystemExit("caw_cwrv already present")
    if b"0466.852.882" in raw or b"0466852882" in raw:
        raise SystemExit("CAW Rivierenland KBO already present as entity")
    row = (
        "caw_cwrv,CAW Rivierenland VZW / Centrum Algemeen Welzijnswerk Rivierenland (leftover recognized Flemish CAW / leftover zorg EVA of mined Mechelen + leftover of 11 other Rivierenland municipalities; NOT leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Rivierenland ASBL (EVA bien-etre residuel),"
        "CAW Rivierenland leftover recognized Flemish CAW / zorg EVA of mined Mechelen + 11 other Rivierenland municipalities (not leftover Woonmaatschappij Rivierenland / leftover CGG De Pont / leftover IVAREM / leftover CAW Antwerpen / leftover CAW De Kempen / leftover CAW Brussel / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_mechelen,nl,https://www.caw.be/over-caw/organisatie/caw-rivierenland/,centraal.secretariaat@cawboommechelenlier.be,Maurits Sabbestraat 119 2800 Mechelen,"
        "tick1528 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Mechelen after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel hunt; KBO 0466.852.882 Actief; renamed from CAW Boom-Mechelen-Lier 22.04.2024; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 9362853 opbr 8432403 omzet 371409 73 7780184 pers 7006469 95.1 VTE cash 312739 debt 3564445 pnl 11558; FOI ready not sent; parent city_mechelen; prefix cwrv; NOT leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwrv")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
