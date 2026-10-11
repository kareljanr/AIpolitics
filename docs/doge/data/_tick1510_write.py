#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1510 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T05:00:00Z"
ENT = "cgg_cgzo"
SRC = "src_cgzo_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00195156.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CGG Zuid-Oost-Vlaanderen VZW official NBB WVV VOL-VZW JR2025,{PDF},NBB / CGG ZOV VZW,2026-08-20,budget,tick1510; official NBB WVV VOL-VZW JR2025 PDF 44p / 608631 bytes; deposit 2026-00195156; AV 04.06.2026; header 18.06.2026; pdfinfo created 25.06.2026 03:45:53 UTC; model VOL-VZW 25.0.13 m05-f; euros PDF only",
        "src_cgzo_kbo_0470515425,KBO CGG Zuid-Oost-Vlaanderen VZW 0470.515.425,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0470515425,FPS Economy KBO,2026-08-20,official_register,tick1510; leftover recognized Flemish CGG of mined Aalst + leftover of mined Ninove + leftover of mined Geraardsbergen + leftover of mined Oudenaarde; zetel Keizersplein 4 9300 Aalst; KBO 0470.515.425; prefix cgzo unused",
        "src_cgzo_zorg_erkenning,CGG koepel Zuid-Oost-Vlaanderen recognized Flemish CGG page,https://zov.be/,Departement Zorg / CGG ZOV,2026-08-20,official_register,tick1510; leftover recognized Flemish CGG / leftover zorg EVA of mined Aalst; NOT leftover CGG umbrella cgg_vl / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507",
        "src_cgzo_foi_contact,CGG Zuid-Oost-Vlaanderen FOI channel (Departement Zorg openbaarheid + CGG postal),https://zov.be/,CGG / Departement Zorg,2026-08-20,official_web,tick1510; leftover recognized Flemish CGG; FOI ready not sent; openbaarheid@vlaanderen.be; Keizersplein 4 9300 Aalst; info@zov.be; NOT leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncgg_cgzo," in raw or raw.startswith(b"cgg_cgzo,"):
        raise SystemExit("cgg_cgzo already present")
    if b"0470.515.425" in raw or b"0470515425" in raw:
        raise SystemExit("CGG ZOV KBO already present as entity")
    row = (
        "cgg_cgzo,Centrum voor Geestelijke Gezondheidszorg zuid Oost-Vlaanderen VZW (leftover recognized Flemish CGG / leftover zorg EVA of mined Aalst + leftover of mined Ninove + leftover of mined Geraardsbergen + leftover of mined Oudenaarde; NOT leftover CGG umbrella cgg_vl / leftover CGG VBO 1509 prefix cgvb / leftover CGG SDW 1508 prefix cgsd / leftover CGG NWVL 1507 prefix cgnw / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Centre de sante mentale Flandre orientale-Sud ASBL (CGG residuel Alost / Ninove / Grammont / Audenarde),"
        "CGG Zuid-Oost-Vlaanderen leftover recognized Flemish CGG / leftover care EVA of mined Aalst + leftover mined Ninove Geraardsbergen Oudenaarde (not leftover CGG umbrella / leftover CGG VBO / leftover CGG SDW / leftover CGG NWVL / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_aalst,nl,https://zov.be/,openbaarheid@vlaanderen.be,Keizersplein 4 9300 Aalst,"
        "tick1510 leftover residual recognized Flemish CGG after leftover AGB/APB hunt; KBO 0470.515.425 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 6678603 opbr 7623192 73 5295335 pers 6091984 65.8 VTE cash 139180 debt 1420686 pnl 140404; FOI ready not sent; parent city_aalst; prefix cgzo; EVERY-10; NOT leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella cgg_vl / leftover official-41 1464-1505"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 cgg_cgzo")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
