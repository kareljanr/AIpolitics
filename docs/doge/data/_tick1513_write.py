#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1513 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:40:00Z"
ENT = "cgg_cgpr"
SRC = "src_cgpr_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00209149.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Prisma VZW official NBB WVV VKT-VZW JR2025,{PDF},NBB / CGG Prisma VZW,2026-08-20,budget,tick1513; official NBB WVV VKT-VZW JR2025 PDF 21p / 306867 bytes; deposit 2026-00209149; AV 09.06.2026; header 29.06.2026; pdfinfo created 29.06.2026 06:24:08 UTC; model VKT-VZW 26.0.15 m04-f; euros PDF only",
        "src_cgpr_kbo_0472448101,KBO CGG Prisma VZW 0472.448.101,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472448101,FPS Economy KBO,2026-08-20,official_register,tick1513; leftover recognized Flemish CGG of mined Blankenberge + leftover of mined Oostende + leftover of mined Torhout + leftover of mined Beernem; zetel Astridlaan 35 8370 Blankenberge; KBO 0472.448.101; prefix cgpr unused",
        "src_cgpr_zorg_erkenning,CGG Prisma recognized Flemish CGG page,https://www.cggprisma.org,Departement Zorg / CGG Prisma,2026-08-20,official_register,tick1513; leftover recognized Flemish CGG / leftover zorg EVA of mined Blankenberge; NOT leftover CGG umbrella cgg_vl / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgpr_foi_contact,CGG Prisma FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.cggprisma.org,CGG / Departement Zorg,2026-08-20,official_web,tick1513; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Astridlaan 35 8370 Blankenberge; info@cggprisma.be; NOT leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgpr," in raw or raw.startswith(b"cgg_cgpr,"):
        raise SystemExit("cgg_cgpr already present")
    if b"0472.448.101" in raw or b"0472448101" in raw:
        raise SystemExit("CGG Prisma KBO already present as entity")
    row = (
        "cgg_cgpr,Centrum Geestelijke Gezondheidszorg Prisma VZW (leftover recognized Flemish CGG / leftover zorg EVA of mined Blankenberge + leftover of mined Oostende + leftover of mined Torhout + leftover of mined Beernem; NOT leftover CGG umbrella cgg_vl / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover WV Blankenberge 1506 prefix wvbl / leftover AGB Blankenberge 1323 / leftover Zetus 1490 prefix ztus / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Prisma ASBL (CGG residuel Blankenberge / Ostende / Thourout / Beernem),"
        "CGG Prisma leftover recognized Flemish CGG / leftover care EVA of mined Blankenberge + leftover mined Oostende Torhout Beernem (not leftover CGG umbrella / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover WV Blankenberge / leftover AGB Blankenberge / leftover Zetus / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_blankenberge,nl,https://www.cggprisma.org,openbaarheid@vlaanderen.be,Astridlaan 35 8370 Blankenberge,"
        "tick1513 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0472.448.101 Actief; live JR2025 official NBB WVV VKT-VZW PDF; sourced euros assets 8441644 bruto 4186449 pers 4142732 47.8 VTE cash 288830 debt 3234189 pnl -90558; FOI ready not sent; parent city_blankenberge; prefix cgpr; NOT leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover WV Blankenberge 1506 / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgpr")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
