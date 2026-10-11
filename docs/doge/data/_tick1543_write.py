#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1543 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvzk"
SRC = "src_hvzk_jr2025_bbc"
PDF = "https://kempen.hulpverleningszone.be/storage/JZ16ya31sYaCcDTQxcDSHeoq5zcxR3VW7GlychOl.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Brandweer Zone Kempen official activiteitenrapport 2025,{PDF},HVZ Kempen,2026-08-20,budget,tick1543; official activiteitenrapport 2025; PDF 77p / 21013828 bytes; pdfinfo created 05.05.2026 08:33:53 UTC Canva; Dienst Financiën pages 70-75; euros PDF only; full zoneraad rekening 2025 unpublished",
        "src_hvzk_kbo_0500915126,KBO Hulpverleningszone Brandweer Zone Kempen 0500.915.126,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500915126,FPS Economy KBO,2026-08-20,official_register,tick1543; leftover IGS hulpverleningszone of mined Geel + leftover of Herentals/Mol/Westerlo/Balen/Laakdal/Herselt/Olen/Grobbendonk/Retie/Hulshout/Meerhout/Dessel/Herenthout/Vorselaar; zetel Stelenseweg 92 2440 Geel; KBO 0500.915.126 Actief; prefix hvzk unused",
        "src_hvzk_site,HVZ Kempen official site (activiteitenrapport 2025 published),https://kempen.hulpverleningszone.be/,HVZ Kempen,2026-08-20,official_web,tick1543; leftover IGS of mined Geel; official AV2025 live on kempen.hulpverleningszone.be; full rekening 2025 unpublished (inzage / FOI)",
        "src_hvzk_foi_contact,HVZ Kempen FOI channel (info@brandweerzonekempen.be),https://kempen.hulpverleningszone.be/pagina/contactgegevens,HVZ Kempen,2026-08-20,official_web,tick1543; leftover IGS of mined Geel; FOI ready not sent; Stelenseweg 92 2440 Geel; official e-mail info@brandweerzonekempen.be; zonesecretaris Amelie Janssens; NOT leftover HVZ Taxandria 1538 / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover BVLAR 1542",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvzk," in raw or raw.startswith(b"igs_hvzk,"):
        raise SystemExit("igs_hvzk already present")
    if b"0500.915.126" in raw or b"0500915126" in raw:
        raise SystemExit("HVZ Kempen KBO already present as entity")
    row = (
        "igs_hvzk,Hulpverleningszone Brandweer Zone Kempen / HVZ Kempen (leftover IGS hulpverleningszone of mined Geel + leftover of Herentals/Mol/Westerlo/Balen/Laakdal/Herselt/Olen/Grobbendonk/Retie/Hulshout/Meerhout/Dessel/Herenthout/Vorselaar; NOT leftover HVZ Taxandria 1538 / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover LeefGoed 1481),"
        "Zone de secours Kempen (IGS residuel / zone de secours),"
        "Brandweer Zone Kempen leftover fire-rescue IGS of mined Geel + remaining Kempen municipalities (not leftover HVZ Taxandria / leftover CAW De Kempen / leftover CGG Kempen / leftover BVLAR / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_geel,nl,https://kempen.hulpverleningszone.be/,info@brandweerzonekempen.be,Stelenseweg 92 2440 Geel,"
        "tick1543 leftover residual IGS hulpverleningszone of mined Geel after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official AV2025 taken; KBO 0500.915.126 Actief; zetel Geel 2440; live official activiteitenrapport 2025 77p 21013828 created 05.05.2026; sourced euros uitgaven_gewone 16747636 pers 13742087 werking 3005549 beschikbaar 18986967 gem_totaal 9713805 fed 4394794 invest 2506646; FOI ready not sent; parent city_geel; prefix hvzk; NOT leftover HVZ Taxandria 1538 / leftover CAW De Kempen 1526 / leftover CGG Kempen 1516 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvzk")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
