#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1509 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T04:00:00Z"
ENT = "cgg_cgvb"
SRC = "src_cgvb_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00227270.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Vlaams-Brabant Oost VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG VBO VZW,2026-08-20,budget,tick1509; official NBB WVV VOL-VZW JR2025 PDF 39p / 2534398 bytes; deposit 2026-00227270; AV 24.06.2026; header 25.06.2026; pdfinfo created 01.07.2026 01:04:22 UTC; model VOL-VZW 25.0.13 m05-f; euros PDF only",
        "src_cgvb_kbo_0471366154,KBO CGG Vlaams-Brabant Oost VZW 0471.366.154,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0471366154,FPS Economy KBO,2026-08-20,official_register,tick1509; leftover recognized Flemish CGG of mined Leuven + leftover of mined Tienen; zetel Kapucijnenvoer 16 3000 Leuven; KBO 0471.366.154; prefix cgvb unused",
        "src_cgvb_zorg_erkenning,CGG koepel Vlaams-Brabant Oost recognized Flemish CGG page,https://www.centrageestelijkegezondheidszorg.be/cgg/vlaams-brabant-oost,Departement Zorg / CGG koepel,2026-08-20,official_register,tick1509; leftover recognized Flemish CGG / leftover zorg EVA of mined Leuven; NOT leftover CGG umbrella cgg_vl / leftover CGG NWVL 1507 / leftover CGG SDW 1508",
        "src_cgvb_foi_contact,CGG Vlaams-Brabant Oost FOI channel (Departement Zorg openbaarheid + CGG postal),https://www.centrageestelijkegezondheidszorg.be/cgg/vlaams-brabant-oost,CGG / Departement Zorg,2026-08-20,official_web,tick1509; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Kapucijnenvoer 16 3000 Leuven; vzw@cgg-vbo.be; NOT leftover CGG NWVL 1507 / leftover CGG SDW 1508 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgvb," in raw or raw.startswith(b"cgg_cgvb,"):
        raise SystemExit("cgg_cgvb already present")
    if b"0471.366.154" in raw or b"0471366154" in raw:
        raise SystemExit("CGG VBO KBO already present as entity")
    row = (
        "cgg_cgvb,Centrum voor Geestelijke Gezondheidszorg Vlaams-Brabant Oost VZW (leftover recognized Flemish CGG / leftover zorg EVA of mined Leuven + leftover of mined Tienen / Oost-Brabant; NOT leftover CGG umbrella cgg_vl / leftover CGG NWVL 1507 prefix cgnw / leftover CGG SDW 1508 prefix cgsd / leftover Woontrots 1503 prefix wtrt / leftover Het Vlaamse Woonanker 1502 prefix wvwa / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Brabant flamand-Est ASBL (CGG residuel Louvain / Tirlemont),"
        "CGG Vlaams-Brabant Oost leftover recognized Flemish CGG / leftover care EVA of mined Leuven + leftover mined Tienen (not leftover CGG umbrella / leftover CGG NWVL / leftover CGG SDW / leftover Woontrots / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_leuven,nl,https://www.centrageestelijkegezondheidszorg.be/cgg/vlaams-brabant-oost,openbaarheid@vlaanderen.be,Kapucijnenvoer 16 3000 Leuven,"
        "tick1509 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0471.366.154 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 9329271 omzet 1083816 73 6717617 pers 6655129 69.5 VTE cash 2477705 debt 2332348 pnl 34423; FOI ready not sent; parent city_leuven; prefix cgvb; NOT leftover CGG NWVL 1507 / leftover CGG SDW 1508 / leftover CGG umbrella cgg_vl / leftover Woontrots 1503 / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgvb")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
