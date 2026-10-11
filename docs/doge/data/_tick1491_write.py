#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1491 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:55:00Z"
ENT = "wm_onod"
SRC = "src_onod_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00189814.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Ons Onderdak official NBB WVV VOL-inb JR2025,{PDF},NBB / Ons Onderdak,2026-08-19,primary_pdf,tick1491; leftover woonmaatschappij of mined Ieper + leftover of mined Heuvelland + leftover of mined Poperinge; official NBB WVV VOL-inb JR2025 PDF 62p / 1423605 bytes; deposit 2026-00189814; AV 12.06.2026; header 15.06.2026; pdfinfo created 24.06.2026 01:30:21 UTC; model VOL-inb 25.0.13 m82-f; KBO 0405.501.570; assets 136782795 cash 5008962 debt 101590448 pers 1919909 omzet 11511389 pnl 321927 equity 34735657",
        "src_onod_site,Ons Onderdak official pages,https://onsonderdak.be/,Ons Onderdak,2026-08-19,official_register,tick1491; leftover woonmaatschappij of mined Ieper + Heuvelland + Poperinge; site + werkingsgebied Ieper-Heuvelland-Mesen; zetel Ter Waarde 65 8900 Ieper; KBO 0405.501.570; FOI info@onsonderdak.be; official jaarverslag-2025.pdf is narrative not the statutory WVV",
        "src_kbo_onod_0405501570,KBO Ons Onderdak 0405.501.570,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405501570,KBO,2026-08-19,official_register,tick1491; Actief since 29.05.1929; naam Ons Onderdak since 29.05.1929; BV since 16.12.2022; zetel Ter Waarde 65 8900 Ieper since 21.05.2014; 1 VE; 14 functiehouders; Werkgever RSZ since 01.01.1960; aanbestedende overheid since 29.05.1929; NACE 68.121 / 68.202",
        "src_onod_foi_contact,Ons Onderdak FOI channel (info@onsonderdak.be),https://onsonderdak.be/,Ons Onderdak,2026-08-19,official_register,tick1491; leftover woonmaatschappij of mined Ieper + leftover of mined Heuvelland + leftover of mined Poperinge; FOI ready not sent; NOT leftover AGB Vauban Ieper / leftover AGB Musea Ieper / leftover Zetus 1490 / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_onod," in raw or raw.startswith(b"wm_onod,"):
        raise SystemExit("wm_onod already present")
    if b"0405.501.570" in raw or b"0405501570" in raw:
        raise SystemExit("Ons Onderdak KBO already present as entity")
    row = (
        "wm_onod,Ons Onderdak (leftover woonmaatschappij / social-housing BV of mined Ieper + leftover of mined Heuvelland + leftover of mined Poperinge / Ieper-Heuvelland-Mesen; NOT leftover AGB Vauban Ieper already mined / leftover AGB Musea Ieper already mined / leftover Zetus 0405.196.516 / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Ons Onderdak SRL (logement social residuel Ieper / Heuvelland / Mesen),"
        "Ons Onderdak leftover social-housing company of mined Ieper + Heuvelland + Poperinge (not leftover AGB Vauban Ieper / leftover AGB Musea Ieper / leftover Zetus / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_ieper,nl,https://onsonderdak.be/,info@onsonderdak.be,Ter Waarde 65 8900 Ieper,"
        "tick1491 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.501.570 Actief since 29.05.1929; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 136782795 omzet 11511389 pers 1919909 23.3 VTE pnl 321927 equity 34735657 cash 5008962 debt 101590448 capex 11194008 dividend 0; 1 VE; parent city_ieper; werkingsgebied Ieper + Heuvelland + Mesen; prefix onod"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_onod")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
