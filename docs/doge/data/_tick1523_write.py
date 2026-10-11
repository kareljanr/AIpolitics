#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1523 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "cgg_cgkh"
SRC = "src_cgkh_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00242985.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Kohesi VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG Kohesi VZW,2026-08-20,budget,tick1523; official NBB WVV VOL-VZW JR2025 PDF 51p / 1092286 bytes; deposit 2026-00242985; AV 25.06.2026; header 29.06.2026; pdfinfo created 03.07.2026 01:05:10 UTC; model VOL-VZW 25.0.13 m05-f; euros PDF only",
        "src_cgkh_kbo_0472466907,KBO CGG Kohesi VZW 0472.466.907,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472466907,FPS Economy KBO,2026-08-20,official_register,tick1523; leftover recognized Flemish CGG of mined Hasselt; NEW unused recognized CGG not in 1507-1522 list; zetel Ilgatlaan 11 bus 3 3500 Hasselt; KBO 0472.466.907; prefix cgkh unused",
        "src_cgkh_zorg_erkenning,CGG Kohesi recognized Flemish CGG CoBRHA,https://publiek.departementzorg.be/Cobrha/Institutions/Institution/WVG_VAZG/4971,Departement Zorg CoBRHA,2026-08-20,official_register,tick1523; leftover recognized Flemish CGG / leftover zorg EVA of mined Hasselt; HCO 4971 type WVG_VAZG 075; NOT leftover CGG umbrella cgg_vl / leftover CGG Mandel en Leie 1522 / leftover CGG Brussel 1521 / leftover CGG PassAnt 1520 / leftover CGG Andante 1519 / leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG DAGG STOPPED",
        "src_cgkh_foi_contact,CGG Kohesi FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.kohesi.be/,CGG / Departement Zorg,2026-08-20,official_web,tick1523; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Ilgatlaan 11 bus 3 3500 Hasselt; NOT leftover CGG Integra 1515 / leftover CGG Mandel en Leie 1522 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgkh," in raw or raw.startswith(b"cgg_cgkh,"):
        raise SystemExit("cgg_cgkh already present")
    if b"0472.466.907" in raw or b"0472466907" in raw:
        raise SystemExit("CGG Kohesi KBO already present as entity")
    row = (
        "cgg_cgkh,CGG Kohesi VZW / Centrum Geestelijke Gezondheidszorg Kohesi (leftover recognized Flemish CGG / leftover zorg EVA of mined Hasselt; NEW unused recognized CGG not in 1507-1522 list; formerly LITP / CGG West-Limburg; NOT leftover CGG umbrella cgg_vl / leftover CGG Mandel en Leie 1522 prefix cgml / leftover CGG Brussel 1521 prefix cgbr / leftover CGG PassAnt 1520 prefix cgpa / leftover CGG Andante 1519 prefix cgan / leftover CGG Largo 1518 prefix cglr / leftover CGG Ahasverus 1517 prefix cgah / leftover CGG Kempen 1516 prefix cgkp / leftover CGG Integra 1515 prefix cgin / leftover CGG De Pont 1514 prefix cgpt / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover CGG DAGG STOPPED / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Kohesi ASBL (CGG residuel Hasselt / Limbourg-Ouest),"
        "CGG Kohesi leftover recognized Flemish CGG / leftover care EVA of mined Hasselt (NEW unused recognized CGG not in 1507-1522 list; not leftover CGG umbrella / leftover CGG Mandel en Leie / leftover CGG Brussel / leftover CGG PassAnt / leftover CGG Andante / leftover CGG Largo / leftover CGG Ahasverus / leftover CGG Kempen / leftover CGG Integra / leftover CGG De Pont / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover CGG DAGG / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_hasselt,nl,https://www.kohesi.be/,openbaarheid@vlaanderen.be,Ilgatlaan 11 bus 3 3500 Hasselt,"
        "tick1523 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1522 list; KBO 0472.466.907 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 7706860 opbr 8794445 pers 6248426 73.4 VTE cash 1981073 debt 2941952 pnl -5036; FOI ready not sent; parent city_hasselt; prefix cgkh; NOT leftover CGG Integra 1515 / leftover CGG Mandel en Leie 1522 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgkh")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
