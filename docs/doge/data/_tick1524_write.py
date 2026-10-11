#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1524 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_ivrm"
SRC = "src_ivrm_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00373329.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},IVAREM official NBB WVV VOL-inb JR2025,{PDF},NBB / IVAREM,2026-08-20,budget,tick1524; official NBB WVV VOL-inb JR2025 PDF 71p / 1241161 bytes; deposit 2026-00373329; AV 19.06.2026; header 03.08.2026; pdfinfo created 03.08.2026 08:44:34 UTC; model VOL-inb 23.0.10 m82-f; euros PDF only",
        "src_ivrm_kbo_0267403264,KBO IVAREM 0267.403.264,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0267403264,FPS Economy KBO,2026-08-20,official_register,tick1524; leftover IGS opdrachthoudende vereniging of mined Mechelen-region cities; zetel Leuvensesteenweg 443 bus D 2812 Muizen (Mechelen); KBO 0267.403.264; prefix ivrm unused",
        "src_ivrm_nbb_consult,NBB Consult IVAREM published deposits 0267403264,https://consult.cbso.nbb.be/consult-enterprise/0267403264,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1524; leftover IGS; JR2025 reference 2026-00373329 filing 03.08.2026 year-end 30.12.2025 Volledig model kapitaalloze vennootschap; prior Busibee 2025 false-alarm as of 1451 now a TRUE NBB filing",
        "src_ivrm_foi_contact,IVAREM FOI channel (boekhouding@ivarem.be),https://www.ivarem.be/,IVAREM,2026-08-20,official_web,tick1524; leftover IGS of mined Mechelen; FOI ready not sent; Leuvensesteenweg 443 bus D 2812 Muizen; NOT leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_ivrm," in raw or raw.startswith(b"igs_ivrm,"):
        raise SystemExit("igs_ivrm already present")
    if b"0267.403.264" in raw or b"0267403264" in raw:
        raise SystemExit("IVAREM KBO already present as entity")
    row = (
        "igs_ivrm,IVAREM / Intergemeentelijke Vereniging voor Duurzaam Afvalbeheer Regio Mechelen (leftover IGS / opdrachthoudende vereniging of mined Mechelen + leftover of mined Lier / Willebroek / Bornem / Puurs-Sint-Amands / Duffel / Berlaar; NOT leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS IVAREM-40pct daughter / leftover CGG De Pont 1514 / leftover Woonmaatschappij Rivierenland 1465 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "IVAREM association missionnee dechets region Malines (IGS residuel),"
        "IVAREM leftover waste IGS / mission association of mined Mechelen-region municipalities (not leftover IGEMO / leftover IOK Afvalbeheer / leftover PMBS / leftover CGG De Pont / leftover Woonmaatschappij Rivierenland / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_mechelen,nl,https://www.ivarem.be/,boekhouding@ivarem.be,Leuvensesteenweg 443 bus D 2812 Muizen (Mechelen),"
        "tick1524 leftover residual IGS of mined Mechelen-region cities after leftover AGB/APB/CGG/Bosgroep hunt; KBO 0267.403.264 Actief; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 61398227 omzet 34824643 opbr 35143041 pers 12430050 165.8 VTE cash 8106299 debt 37235254 pnl -2241145; FOI ready not sent; parent city_mechelen; prefix ivrm; NOT leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS / leftover official-41 1464-1505 / leftover CGG 1507-1523"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_ivrm")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
