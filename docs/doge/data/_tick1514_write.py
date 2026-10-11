#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1514 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:50:00Z"
ENT = "cgg_cgpt"
SRC = "src_cgpt_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00167849.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG De Pont VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG De Pont VZW,2026-08-20,budget,tick1514; official NBB WVV VOL-VZW JR2025 PDF 41p / 640277 bytes; deposit 2026-00167849; AV 03.06.2026; header 15.06.2026; pdfinfo created 17.06.2026 11:12:56 UTC; model VOL-VZW 23.0.9 m05-f; euros PDF only",
        "src_cgpt_kbo_0472106225,KBO CGG De Pont VZW 0472.106.225,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472106225,FPS Economy KBO,2026-08-20,official_register,tick1514; leftover recognized Flemish CGG of mined Mechelen + leftover of mined Lier + leftover of mined Boom; zetel Lange Ridderstraat 20 2800 Mechelen; KBO 0472.106.225; prefix cgpt unused",
        "src_cgpt_zorg_erkenning,CGG De Pont recognized Flemish CGG page,https://www.cggdepont.be,Departement Zorg / CGG De Pont,2026-08-20,official_register,tick1514; leftover recognized Flemish CGG / leftover zorg EVA of mined Mechelen; NOT leftover CGG umbrella cgg_vl / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgpt_foi_contact,CGG De Pont FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.cggdepont.be,CGG / Departement Zorg,2026-08-20,official_web,tick1514; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Lange Ridderstraat 20 2800 Mechelen; mechelen@cggdepont.be; NOT leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgpt," in raw or raw.startswith(b"cgg_cgpt,"):
        raise SystemExit("cgg_cgpt already present")
    if b"0472.106.225" in raw or b"0472106225" in raw:
        raise SystemExit("CGG De Pont KBO already present as entity")
    row = (
        "cgg_cgpt,Centrum voor Geestelijke Gezondheidszorg De Pont VZW (leftover recognized Flemish CGG / leftover zorg EVA of mined Mechelen + leftover of mined Lier + leftover of mined Boom; NOT leftover CGG umbrella cgg_vl / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover AGB MAC Mechelen),"
        "Centre de sante mentale De Pont ASBL (CGG residuel Malines / Lierre / Boom),"
        "CGG De Pont leftover recognized Flemish CGG / leftover care EVA of mined Mechelen + leftover mined Lier Boom (not leftover CGG umbrella / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover AGB MAC),"
        "eva,city_mechelen,nl,https://www.cggdepont.be,openbaarheid@vlaanderen.be,Lange Ridderstraat 20 2800 Mechelen,"
        "tick1514 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0472.106.225 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 7371989 opbr 10287468 pers 9380342 103.3 VTE cash 955481 debt 2634118 pnl -61881; FOI ready not sent; parent city_mechelen; prefix cgpt; NOT leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgpt")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
