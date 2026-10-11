#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1535 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwnw"
SRC = "src_cwnw_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00103625.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},CAW Noord-West-Vlaanderen official NBB WVV VOL-VZW JR2025,{PDF},NBB / CAW Noord-West-Vlaanderen,2026-08-20,budget,tick1535; official NBB WVV VOL-VZW JR2025 PDF 50p / 3458002 bytes; deposit 2026-00103625 Initial (NBB consult published-deposits 403 this tick; SBM HTML via WebFetch listed this single 2025 deposit neerlegging 2026-05-06; no later Aanpassing visible on SBM CDN; box-IP SBM HTML blacklisted 262b; Busibee PDF URL same 3458002 bytes used for ID/URL confirm only); AV 22.04.2026; header 30.04.2026; pdfinfo created 06.05.2026 07:35:09 UTC; model VOL-VZW 26.0.10 m05-f; euros PDF only",
        "src_cwnw_kbo_0464229231,KBO CAW Noord-West-Vlaanderen 0464.229.231,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0464229231,FPS Economy KBO,2026-08-20,official_register,tick1535; leftover recognized Flemish CAW / leftover zorg EVA of mined Brugge + leftover of remaining Noord-West-Vlaanderen municipalities; zetel Ruddershove 8 8000 Brugge; KBO 0464.229.231 Actief; prefix cwnw unused",
        "src_cwnw_nbb_consult,NBB Consult CAW Noord-West-Vlaanderen published deposits 0464229231,https://consult.cbso.nbb.be/consult-enterprise/0464229231,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1535; leftover zorg EVA; JR2025 reference 2026-00103625 Initial filing 06.05.2026 year-end 31.12.2025 Volledig model vereniging; NBB consult API 403 this tick",
        "src_cwnw_foi_contact,CAW Noord-West-Vlaanderen FOI channel (nele.haers@cawnoordwestvlaanderen.be),https://cawnoordwestvlaanderen.be/,CAW Noord-West-Vlaanderen,2026-08-20,official_web,tick1535; leftover recognized CAW of mined Brugge; FOI ready not sent; Ruddershove 8 8000 Brugge; official contact nele.haers@cawnoordwestvlaanderen.be; NOT leftover CGG NWVL 1507 / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma 1513 / leftover umbrella caw_vl",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\ncaw_cwnw," in raw or raw.startswith(b"caw_cwnw,"):
        raise SystemExit("caw_cwnw already present")
    if b"0464.229.231" in raw or b"0464229231" in raw:
        raise SystemExit("CAW NWVL KBO already present as entity")
    row = (
        "caw_cwnw,CAW Noord-West-Vlaanderen VZW / Centrum Algemeen Welzijnswerk Noord-West-Vlaanderen (leftover recognized Flemish CAW / leftover zorg EVA of mined Brugge + leftover of remaining Noord-West-Vlaanderen municipalities; last official 11-CAW unit; NOT leftover CGG NWVL 1507 / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma 1513 / leftover WV Blankenberge 1506 / leftover AGB Blankenberge 1323 / leftover CAW ZWVL 1534 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "CAW Flandre occidentale nord ASBL (EVA bien-etre residuel),"
        "CAW Noord-West-Vlaanderen leftover recognized Flemish CAW / zorg EVA of mined Brugge + remaining Noord-West-Vlaanderen municipalities (not leftover CGG NWVL / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma / leftover WV Blankenberge / leftover AGB Blankenberge / leftover CAW ZWVL / leftover CAW CWVL / leftover CAW Oost-Vlaanderen / leftover CAW Limburg / leftover CAW Oost-Brabant / leftover CAW Halle-Vilvoorde / leftover CAW Rivierenland / leftover CAW Brussel / leftover CAW De Kempen / leftover CAW Antwerpen / leftover umbrella caw_vl / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "eva,city_brugge,nl,https://cawnoordwestvlaanderen.be/,nele.haers@cawnoordwestvlaanderen.be,Ruddershove 8 8000 Brugge,"
        "tick1535 leftover residual recognized Flemish CAW / leftover zorg EVA of mined Brugge after leftover AGB/APB/CGG/Bosgroep/IVAREM/CAW-Antwerpen/CAW-De-Kempen/CAW-Brussel/CAW-Rivierenland/CAW-Halle-Vilvoorde/CAW-Oost-Brabant/CAW-Limburg/CAW-Oost-Vlaanderen/CAW-CWVL/CAW-ZWVL hunt; last official 11-CAW unit; KBO 0464.229.231 Actief; zetel Brugge 8000; live JR2025 official NBB WVV VOL-VZW PDF Initial; sourced euros assets 15981042 opbr 17987315 omzet 431305 73 16119120 pers 14781014 206.2 VTE cash 430376 debt 6344185 pnl -1892028 expl LOSS 1890904; FOI ready not sent; parent city_brugge; prefix cwnw; NOT leftover CGG NWVL 1507 / leftover Mintus Brugge / leftover AGB Brugge / leftover CGG Prisma 1513 / leftover CAW ZWVL 1534 / leftover CAW CWVL 1533 / leftover CAW Oost-Vlaanderen 1532 / leftover CAW Limburg 1531 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 caw_cwnw")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
