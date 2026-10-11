#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1525 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwan"
SRC = "src_cwan_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00112717.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Antwerpen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Antwerpen,2026-08-20,budget,tick1525; official NBB WVV VOL-VZW JR2025 PDF 48p / 282027 bytes; deposit 2026-00112717; AV 28.04.2026; header 18.05.2026; pdfinfo created 18.05.2026 16:03:16 UTC; model VOL-VZW 25.0.12 m05-f; euros PDF only",
        "src_cwan_kbo_0455608604,KBO CAW Antwerpen 0455.608.604,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0455608604,FPS Economy KBO,2026-08-20,official_register,tick1525; leftover recognized Flemish CAW / leftover zorg EVA of mined Antwerpen; zetel Lange Lozanastraat 200 2018 Antwerpen; KBO 0455.608.604; prefix cwan unused",
        "src_cwan_nbb_consult,NBB Consult CAW Antwerpen published deposits 0455608604,https://consult.cbso.nbb.be/consult-enterprise/0455608604,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1525; leftover zorg EVA; JR2025 reference 2026-00112717 filing 18.05.2026 year-end 30.12.2025 Volledig model vereniging",
        "src_cwan_foi_contact,CAW Antwerpen FOI channel (info@cawantwerpen.be),https://www.caw.be/over-caw/organisatie/caw-antwerpen/,CAW Antwerpen,2026-08-20,official_web,tick1525; leftover recognized CAW of mined Antwerpen; FOI ready not sent; Lange Lozanastraat 200 2018 Antwerpen; NOT leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwan," in raw or raw.startswith(b"caw_cwan,"):
        raise SystemExit("caw_cwan already present")
    if b"0455.608.604" in raw or b"0455608604" in raw:
        raise SystemExit("CAW Antwerpen KBO already present as entity")
    row = (
        "caw_cwan,CAW Antwerpen VZW / Centrum voor Algemeen Welzijnswerk Antwerpen (leftover recognized Flemish CAW / leftover zorg EVA of mined Antwerpen + leftover of 28 Antwerp-region municipalities; NOT leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Anvers ASBL (EVA bien-etre residuel),"
        "CAW Antwerpen leftover recognized Flemish CAW / zorg EVA of mined Antwerp-region municipalities (not leftover CGG VAGGA / leftover CGG Andante / leftover umbrella caw_vl / leftover IVAREM / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_antwerpen,nl,https://www.caw.be/over-caw/organisatie/caw-antwerpen/,info@cawantwerpen.be,Lange Lozanastraat 200 2018 Antwerpen,"
        "tick1525 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Antwerpen after leftover AGB/APB/CGG/Bosgroep/IVAREM hunt; KBO 0455.608.604 Actief; live JR2025 official NBB WVV VOL-VZW PDF; sourced euros assets 16778368 opbr 52460317 omzet 3691060 73 47451115 pers 43212061 596.7 VTE cash 1004443 debt 10594656 pnl -76893; FOI ready not sent; parent city_antwerpen; prefix cwan; NOT leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwan")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
