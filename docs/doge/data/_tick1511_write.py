#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1511 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T06:00:00Z"
ENT = "cgg_cgad"
SRC = "src_cgad_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188352.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Adentro VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG Adentro VZW,2026-08-20,budget,tick1511; official NBB WVV VOL-VZW JR2025 PDF 44p / 630352 bytes; deposit 2026-00188352; AV 22.06.2026; header 23.06.2026; pdfinfo created 23.06.2026 22:40:10 UTC; model VOL-VZW 26.0.15 m05-f; euros PDF only",
        "src_cgad_kbo_0470717046,KBO CGG Adentro VZW 0470.717.046,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0470717046,FPS Economy KBO,2026-08-20,official_register,tick1511; leftover recognized Flemish CGG of mined Gent + leftover of mined Deinze + leftover of mined Eeklo; zetel Elyzeese Velden 74 9000 Gent; KBO 0470.717.046; prefix cgad unused",
        "src_cgad_zorg_erkenning,CGG koepel Adentro recognized Flemish CGG page,https://cggadentro.be/,Departement Zorg / CGG Adentro,2026-08-20,official_register,tick1511; leftover recognized Flemish CGG / leftover zorg EVA of mined Gent; NOT leftover CGG umbrella cgg_vl / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgad_foi_contact,CGG Adentro FOI channel (Departement Zorg openbaarheid + CGG postal),https://cggadentro.be/,CGG / Departement Zorg,2026-08-20,official_web,tick1511; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Elyzeese Velden 74 9000 Gent; dirk.aelbrecht@cggadentro.be; NOT leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgad," in raw or raw.startswith(b"cgg_cgad,"):
        raise SystemExit("cgg_cgad already present")
    if b"0470.717.046" in raw or b"0470717046" in raw:
        raise SystemExit("CGG Adentro KBO already present as entity")
    row = (
        "cgg_cgad,Centrum Geestelijke Gezondheidszorg Adentro VZW (leftover recognized Flemish CGG / leftover zorg EVA of mined Gent + leftover of mined Deinze + leftover of mined Eeklo; NOT leftover CGG umbrella cgg_vl / leftover CGG ZOV 1510 prefix cgzo / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover AGB Deinze / leftover Dimensa 1466),"
        "Centre de sante mentale Adentro ASBL (CGG residuel Gand / Deinze / Eeklo),"
        "CGG Adentro leftover recognized Flemish CGG / leftover care EVA of mined Gent + leftover mined Deinze Eeklo (not leftover CGG umbrella / leftover CGG ZOV / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_gent,nl,https://cggadentro.be/,openbaarheid@vlaanderen.be,Elyzeese Velden 74 9000 Gent,"
        "tick1511 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0470.717.046 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 9833698 opbr 13798629 73 13172501 pers 11157856 121.1 VTE cash 2905244 debt 2344595 pnl 598359; FOI ready not sent; parent city_gent; prefix cgad; NOT leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgad")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
