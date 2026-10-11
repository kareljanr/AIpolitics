#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1542 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvva"
SRC = "src_hvva_jr2025_bbc"
PDF = "https://bvlar.be/wp-content/uploads/2026/03/BVLAR-Activiteitenverslag-2025.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Brandweerzone Vlaamse Ardennen official activiteitenverslag 2025,{PDF},BVLAR,2026-08-20,budget,tick1542; official activiteitenverslag 2025; PDF 48p / 2899656 bytes; pdfinfo created 11.03.2026 13:24:42 UTC PowerPoint; Financiën Overzicht GEWONE + BUITENGEWONE DIENST; euros PDF only; full zoneraad rekening 2025 unpublished",
        "src_hvva_kbo_0500928190,KBO Brandweerzone Vlaamse Ardennen 0500.928.190,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500928190,FPS Economy KBO,2026-08-20,official_register,tick1542; leftover IGS hulpverleningszone of mined Oudenaarde + leftover of Brakel/Herzele/Horebeke/Kluisbergen/Kruisem/Lierde/Maarkedal/Ronse/Sint-Lievens-Houtem/Wortegem-Petegem/Zottegem/Zwalm; zetel Bedrijvenpark Coupure 21 9700 Oudenaarde; KBO 0500.928.190 Actief; prefix hvva unused",
        "src_hvva_site,BVLAR official site (activiteitenverslag 2025 published),https://bvlar.be/,BVLAR,2026-08-20,official_web,tick1542; leftover IGS of mined Oudenaarde; official AV2025 live on bvlar.be; full rekening 2025 unpublished (inzage / FOI)",
        "src_hvva_foi_contact,BVLAR FOI channel (administratie@bvlar.be),https://bvlar.be/over-ons/,BVLAR,2026-08-20,official_web,tick1542; leftover IGS of mined Oudenaarde; FOI ready not sent; Bedrijvenpark Coupure 21 9700 Oudenaarde; official KBO e-mail administratie@bvlar.be; NOT leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvva," in raw or raw.startswith(b"igs_hvva,"):
        raise SystemExit("igs_hvva already present")
    if b"0500.928.190" in raw or b"0500928190" in raw:
        raise SystemExit("BVLAR KBO already present as entity")
    row = (
        "igs_hvva,Brandweerzone Vlaamse Ardennen / BVLAR / Hulpverleningszone Vlaamse Ardennen (leftover IGS hulpverleningszone of mined Oudenaarde + leftover of Brakel/Herzele/Horebeke/Kluisbergen/Kruisem/Lierde/Maarkedal/Ronse/Sint-Lievens-Houtem/Wortegem-Petegem/Zottegem/Zwalm; NOT leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Waasland / leftover HVZ Fluvia / leftover Brandweerzone Centrum / leftover CAW Oost-Vlaanderen 1532 / leftover CGG Adentro 1511 / leftover Thuispunt Gent 1470 / leftover SOLVA / leftover IVLA / leftover RL Vlaamse Ardennen 1437 / leftover WM Vlaamse Ardennen 1479),"
        "Zone de secours Ardennes flamandes (IGS residuel / zone de secours),"
        "Brandweerzone Vlaamse Ardennen leftover fire-rescue IGS of mined Oudenaarde + remaining Vlaamse Ardennen municipalities (not leftover HVZ Midwest / leftover HVZ Meetjesland / leftover HVZ1 / leftover CAW Oost-Vlaanderen / leftover CGG Adentro / leftover Thuispunt Gent / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_oudenaarde,nl,https://bvlar.be/,administratie@bvlar.be,Bedrijvenpark Coupure 21 9700 Oudenaarde,"
        "tick1542 leftover residual IGS hulpverleningszone of mined Oudenaarde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official AV2025 taken; KBO 0500.928.190 Actief; zetel Oudenaarde 9700; live official activiteitenverslag 2025 48p 2899656 created 11.03.2026; sourced euros uitgaven_gewone 10999722 pers 7238089 werking 3339750 overdrachten 222609 inkomsten_gewone 9390635 toelagen_gem 5751118 invest 3565917; FOI ready not sent; parent city_oudenaarde; prefix hvva; NOT leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover CAW Oost-Vlaanderen 1532 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvva")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
