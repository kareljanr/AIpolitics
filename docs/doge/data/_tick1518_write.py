#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1518 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:08:00Z"
ENT = "cgg_cglr"
SRC = "src_cglr_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00186340.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Largo VZW official NBB WVV VKT-VZW JR2025,{PDF},NBB / CGG Largo VZW,2026-08-20,budget,tick1518; official NBB WVV VKT-VZW JR2025 PDF 22p / 348406 bytes; deposit 2026-00186340; AV 22.06.2026; header 23.06.2026; pdfinfo created 23.06.2026 09:40:30 UTC; model VKT-VZW 23.0.10 m04-f; euros PDF only",
        "src_cglr_kbo_0471370411,KBO CGG Largo VZW 0471.370.411,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0471370411,FPS Economy KBO,2026-08-20,official_register,tick1518; leftover recognized Flemish CGG of mined Roeselare + leftover of mined Ieper + leftover of mined Veurne; zetel Jules Lagaelaan 21 8800 Roeselare; KBO 0471.370.411; prefix cglr unused",
        "src_cglr_zorg_erkenning,CGG Largo recognized Flemish CGG page,https://www.cgglargo.be,Departement Zorg / CGG Largo,2026-08-20,official_register,tick1518; leftover recognized Flemish CGG / leftover zorg EVA of mined Roeselare; NOT leftover CGG umbrella cgg_vl / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover Motena Roeselare",
        "src_cglr_foi_contact,CGG Largo FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.cgglargo.be,CGG / Departement Zorg,2026-08-20,official_web,tick1518; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Jules Lagaelaan 21 8800 Roeselare; NOT leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover Motena Roeselare",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cglr," in raw or raw.startswith(b"cgg_cglr,"):
        raise SystemExit("cgg_cglr already present")
    if b"0471.370.411" in raw or b"0471370411" in raw:
        raise SystemExit("CGG Largo KBO already present as entity")
    row = (
        "cgg_cglr,CGG Largo VZW / Centrum Geestelijke Gezondheidszorg Ieper-Roeselare-Veurne (leftover recognized Flemish CGG / leftover zorg EVA of mined Roeselare + leftover of mined Ieper + leftover of mined Veurne; NOT leftover CGG umbrella cgg_vl / leftover CGG Ahasverus 1517 prefix cgah / leftover CGG Kempen 1516 prefix cgkp / leftover CGG Integra 1515 prefix cgin / leftover CGG De Pont 1514 prefix cgpt / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover Motena Roeselare / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Largo ASBL (CGG residuel Roulers / Ypres / Furnes),"
        "CGG Largo leftover recognized Flemish CGG / leftover care EVA of mined Roeselare + leftover mined Ieper Veurne (not leftover CGG umbrella / leftover CGG Ahasverus / leftover CGG Kempen / leftover CGG Integra / leftover CGG De Pont / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover Motena / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_roeselare,nl,https://www.cgglargo.be,openbaarheid@vlaanderen.be,Jules Lagaelaan 21 8800 Roeselare,"
        "tick1518 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0471.370.411 Actief; live JR2025 official NBB WVV VKT-VZW PDF; sourced euros assets 6034498 opbr 6764354 pers 5512029 60.9 VTE cash 1666321 debt 1287831 pnl 165138; FOI ready not sent; parent city_roeselare; prefix cglr; NOT leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover Motena Roeselare / leftover official-41 1464-1505"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cglr")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
