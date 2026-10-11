#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1515 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:49:00Z"
ENT = "cgg_cgin"
SRC = "src_cgin_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00205082.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Integra VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG Integra VZW,2026-08-20,budget,tick1515; official NBB WVV VOL-VZW JR2025 PDF 41p / 1233798 bytes; deposit 2026-00205082; AV 25.06.2026; header 26.06.2026; pdfinfo created 26.06.2026 23:00:35 UTC; model VOL-VZW 25.0.13 m05-f; euros PDF only; aggregator 2025 euros unused",
        "src_cgin_kbo_0469813065,KBO CGG Integra VZW 0469.813.065,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0469813065,FPS Economy KBO,2026-08-20,official_register,tick1515; leftover recognized Flemish CGG of mined Hasselt + leftover of mined Limburg cities; zetel Pater Valentinuslaan 32 3500 Hasselt; KBO 0469.813.065; prefix cgin unused",
        "src_cgin_zorg_erkenning,CGG Integra recognized Flemish CGG page,https://www.integra-limburg.be,Departement Zorg / CGG Integra,2026-08-20,official_register,tick1515; leftover recognized Flemish CGG / leftover zorg EVA of mined Hasselt; NOT leftover CGG umbrella cgg_vl / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgin_foi_contact,CGG Integra FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.integra-limburg.be,CGG / Departement Zorg,2026-08-20,official_web,tick1515; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Pater Valentinuslaan 32 3500 Hasselt; info@integra-limburg.be; NOT leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgin," in raw or raw.startswith(b"cgg_cgin,"):
        raise SystemExit("cgg_cgin already present")
    if b"0469.813.065" in raw or b"0469813065" in raw:
        raise SystemExit("CGG Integra KBO already present as entity")
    row = (
        "cgg_cgin,Integra VZW / Centrum Geestelijke Gezondheidszorg Integra (leftover recognized Flemish CGG / leftover zorg EVA of mined Hasselt + leftover of mined Limburg cities; NOT leftover CGG umbrella cgg_vl / leftover CGG De Pont 1514 prefix cgpt / leftover CGG Prisma 1513 prefix cgpr / leftover CGG VAGGA 1512 prefix cgvg / leftover CGG Adentro 1511 prefix cgad / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover CGG Kempen),"
        "Centre de sante mentale Integra ASBL (CGG residuel Hasselt / Limbourg),"
        "CGG Integra leftover recognized Flemish CGG / leftover care EVA of mined Hasselt + leftover mined Limburg cities (not leftover CGG umbrella / leftover CGG De Pont / leftover CGG Prisma / leftover CGG VAGGA / leftover CGG Adentro / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover CGG Kempen),"
        "eva,city_hasselt,nl,https://www.integra-limburg.be,openbaarheid@vlaanderen.be,Pater Valentinuslaan 32 3500 Hasselt,"
        "tick1515 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0469.813.065 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 14975892 opbr 19622796 pers 16532661 191.5 VTE cash 3698941 debt 4852883 pnl 102706; FOI ready not sent; parent city_hasselt; prefix cgin; NOT leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgin")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
