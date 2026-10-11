#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1498 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:00:00Z"
ENT = "wm_wpij"
SRC = "src_wpij_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00297388.pdf"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    out = []
    for r in rows:
        out.append(r.rstrip("\r\n") + "\r\n")
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_crlf(DATA / "sources.csv", [
        f"{SRC},Woonpijler official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonpijler,2026-08-19,primary_pdf,tick1498; leftover woonmaatschappij of mined Wetteren + leftover of mined Laarne + leftover of mined Lochristi (werkingsgebied Gent-Oost Wetteren Laarne Lochristi); official NBB WVV VOL-inb JR2025 PDF 140p / 4489764 bytes; deposit 2026-00297388; AV 03.07.2026; header 14.07.2026; pdfinfo created 16.07.2026 02:20:15 UTC; model VOL-inb 26.0.15 m82-f; KBO 0400.143.608; assets 105006637 cash 2667094 debt 92437291 pers 1513868 omzet 7083881 pnl -463096 equity 12170207",
        "src_wpij_site,Woonpijler official pages,https://woonpijler.be/,Woonpijler,2026-08-19,official_register,tick1498; leftover woonmaatschappij of mined Wetteren + leftover of mined Laarne + leftover of mined Lochristi; site + werkingsgebied Gent-Oost Wetteren Laarne Lochristi; zetel Felix Beernaertsplein 55/01 9230 Wetteren; KBO 0400.143.608; FOI info@woonpijler.be",
        "src_kbo_wpij_0400143608,KBO Woonpijler 0400.143.608,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400143608,KBO,2026-08-19,official_register,tick1498; Actief since 25.04.1922; naam WOONPIJLER since 09.06.2023; BV since 09.06.2023; zetel Felix Beernaertsplein 55 bus 01 9230 Wetteren since 27.01.2000; 1 VE; 14 functiehouders; Werkgever RSZ since 01.07.1951; aanbestedende overheid since 25.04.1922; NACE 68.202; ex Gewestelijke Vennootschap Eigen DAK",
        "src_wpij_foi_contact,Woonpijler FOI channel (info@woonpijler.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij/woonpijler,Woonpijler,2026-08-19,official_register,tick1498; leftover woonmaatschappij of mined Wetteren + leftover of mined Laarne + leftover of mined Lochristi; FOI ready not sent; NOT leftover AGB Wetteren already mined / leftover de Thuisbouwer 1497 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_wpij," in raw or raw.startswith(b"wm_wpij,"):
        raise SystemExit("wm_wpij already present")
    if b"0400.143.608" in raw or b"0400143608" in raw:
        raise SystemExit("Woonpijler KBO already present as entity")
    row = (
        "wm_wpij,Woonpijler (leftover woonmaatschappij / social-housing BV of mined Wetteren + leftover of mined Laarne + leftover of mined Lochristi / Gent-Oost werkingsgebied Wetteren Laarne Lochristi; NOT leftover AGB Wetteren already mined / leftover de Thuisbouwer 0405.085.262 prefix thbw / leftover Meetjesland 0401.033.236 / leftover Woonstart 0405.220.963 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonpijler SRL (logement social residuel Wetteren / Gent-Est),"
        "Woonpijler leftover social-housing company of mined Wetteren + leftover mined Laarne + leftover mined Lochristi (not leftover AGB Wetteren / leftover de Thuisbouwer / leftover Meetjesland / leftover Woonstart / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_wetteren,nl,https://woonpijler.be/,info@woonpijler.be,Felix Beernaertsplein 55/01 9230 Wetteren,"
        "tick1498 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.143.608 Actief since 25.04.1922; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 105006637 omzet 7083881 pers 1513868 17.4 VTE pnl -463096 equity 12170207 cash 2667094 debt 92437291 capex 19327583 dividend 0; 1 VE; parent city_wetteren; werkingsgebied Wetteren + Laarne + Lochristi; prefix wpij"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wpij")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
