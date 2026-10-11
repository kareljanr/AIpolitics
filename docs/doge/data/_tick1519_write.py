#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1519 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:15:12Z"
ENT = "cgg_cgan"
SRC = "src_cgan_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00103827.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Andante VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG Andante VZW,2026-08-20,budget,tick1519; official NBB WVV VOL-VZW JR2025 PDF 45p / 594088 bytes; deposit 2026-00103827; AV 04.05.2026; header 06.05.2026; pdfinfo created 06.05.2026 11:04:07 UTC; model VOL-VZW 23.0.8 m05-f; euros PDF only",
        "src_cgan_kbo_0470375071,KBO CGG Andante VZW 0470.375.071,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0470375071,FPS Economy KBO,2026-08-20,official_register,tick1519; leftover recognized Flemish CGG of mined Antwerpen; NEW unused recognized CGG not in 1507-1518 list; zetel Herculusstraat 17 2600 Berchem (Antwerpen); KBO 0470.375.071; prefix cgan unused",
        "src_cgan_zorg_erkenning,CGG Andante recognized Flemish CGG page,https://www.centrageestelijkegezondheidszorg.be/cgg/andante,Departement Zorg / CGG Andante,2026-08-20,official_register,tick1519; leftover recognized Flemish CGG / leftover zorg EVA of mined Antwerpen; NOT leftover CGG umbrella cgg_vl / leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgan_foi_contact,CGG Andante FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.centrageestelijkegezondheidszorg.be/cgg/andante,CGG / Departement Zorg,2026-08-20,official_web,tick1519; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Herculusstraat 17 2600 Berchem (Antwerpen); NOT leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgan," in raw or raw.startswith(b"cgg_cgan,"):
        raise SystemExit("cgg_cgan already present")
    if b"0470.375.071" in raw or b"0470375071" in raw:
        raise SystemExit("CGG Andante KBO already present as entity")
    row = (
        "cgg_cgan,CGG Andante VZW / Centrum voor Geestelijke Gezondheidszorg Andante (leftover recognized Flemish CGG / leftover zorg EVA of mined Antwerpen; NEW unused recognized CGG not in 1507-1518 list; NOT leftover CGG umbrella cgg_vl / leftover CGG Largo 1518 prefix cglr / leftover CGG Ahasverus 1517 prefix cgah / leftover CGG Kempen 1516 prefix cgkp / leftover CGG Integra 1515 prefix cgin / leftover CGG De Pont 1514 prefix cgpt / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Andante ASBL (CGG residuel Anvers-Berchem),"
        "CGG Andante leftover recognized Flemish CGG / leftover care EVA of mined Antwerpen (NEW unused recognized CGG not in 1507-1518 list; not leftover CGG umbrella / leftover CGG Largo / leftover CGG Ahasverus / leftover CGG Kempen / leftover CGG Integra / leftover CGG De Pont / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_antwerpen,nl,https://www.centrageestelijkegezondheidszorg.be/cgg/andante,openbaarheid@vlaanderen.be,Herculusstraat 17 2600 Berchem (Antwerpen),"
        "tick1519 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; NEW unused recognized CGG not in 1507-1518 list; KBO 0470.375.071 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 10657318 opbr 10796084 pers 9295936 108.7 VTE cash 1540487 debt 2163630 pnl -38833; FOI ready not sent; parent city_antwerpen; prefix cgan; NOT leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgan")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
