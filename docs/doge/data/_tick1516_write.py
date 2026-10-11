#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1516 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:54:00Z"
ENT = "cgg_cgkp"
SRC = "src_cgkp_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00178615.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Kempen VZW official NBB WVV VKT-VZW JR2025,{PDF},NBB / CGG Kempen VZW,2026-08-20,budget,tick1516; official NBB WVV VKT-VZW JR2025 PDF 16p / 55363 bytes; deposit 2026-00178615; AV 10.06.2026; header 17.06.2026; pdfinfo created 20.06.2026 05:45:52 UTC; model VKT-VZW 26.0.15 m04-f; euros PDF only",
        "src_cgkp_kbo_0416724470,KBO CGG Kempen VZW 0416.724.470,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416724470,FPS Economy KBO,2026-08-20,official_register,tick1516; leftover recognized Flemish CGG of mined Geel + leftover of mined Kempen cities; zetel Antwerpseweg 1 2440 Geel; KBO 0416.724.470; prefix cgkp unused",
        "src_cgkp_zorg_erkenning,CGG Kempen recognized Flemish CGG page,https://www.cggkempen.be,Departement Zorg / CGG Kempen,2026-08-20,official_register,tick1516; leftover recognized Flemish CGG / leftover zorg EVA of mined Geel; NOT leftover CGG umbrella cgg_vl / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgkp_foi_contact,CGG Kempen FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.cggkempen.be,CGG / Departement Zorg,2026-08-20,official_web,tick1516; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Antwerpseweg 1 2440 Geel; info@cggkempen.be; NOT leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgkp," in raw or raw.startswith(b"cgg_cgkp,"):
        raise SystemExit("cgg_cgkp already present")
    if b"0416.724.470" in raw or b"0416724470" in raw:
        raise SystemExit("CGG Kempen KBO already present as entity")
    row = (
        "cgg_cgkp,CGG Kempen VZW / Centrum voor Geestelijke Gezondheidszorg Kempen (leftover recognized Flemish CGG / leftover zorg EVA of mined Geel + leftover of mined Kempen cities; NOT leftover CGG umbrella cgg_vl / leftover CGG Integra 1515 prefix cgin / leftover CGG De Pont 1514 prefix cgpt / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover Welzijnszorg Kempen / leftover LeefGoed 1481 prefix zkem / leftover Woonboog 1478 prefix wbog / leftover De Noorderkempen 1504 prefix dnkm / leftover Erfgoed Noorderkempen 1426 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Kempen ASBL (CGG residuel Geel / Campine),"
        "CGG Kempen leftover recognized Flemish CGG / leftover care EVA of mined Geel + leftover mined Kempen cities (not leftover CGG umbrella / leftover CGG Integra / leftover CGG De Pont / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover Welzijnszorg Kempen / leftover LeefGoed / leftover Woonboog / leftover De Noorderkempen / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_geel,nl,https://www.cggkempen.be,openbaarheid@vlaanderen.be,Antwerpseweg 1 2440 Geel,"
        "tick1516 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0416.724.470 Actief; live JR2025 official NBB WVV VKT-VZW PDF; sourced euros assets 10466965 bruto 10124140 pers 8390551 99.5 VTE cash 1534479 debt 4057491 pnl 688968; FOI ready not sent; parent city_geel; prefix cgkp; NOT leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgkp")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
