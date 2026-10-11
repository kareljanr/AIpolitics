#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1494 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:40:00Z"
ENT = "wm_ijez"
SRC = "src_ijez_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00171983.pdf"

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
        f"{SRC},IJzer en Zee official NBB WVV VOL-inb JR2025,{PDF},NBB / IJzer en Zee,2026-08-19,primary_pdf,tick1494; leftover woonmaatschappij of mined Veurne + leftover of mined De Panne / Diksmuide / Koksijde / Nieuwpoort / Alveringem / Houthulst / Koekelare / Kortemark / Lo-Reninge; official NBB WVV VOL-inb JR2025 PDF 58p / 970220 bytes; deposit 2026-00171983; AV 05.06.2026; header 18.06.2026; pdfinfo created 18.06.2026 13:47:57 UTC; model VOL-inb 25.0.12 m82-f; KBO 0405.261.842; assets 182256295 cash 13132132 debt 140520313 pers 2550095 omzet 17969403 pnl 1773977 equity 39032061",
        "src_ijez_site,IJzer en Zee official pages,https://www.ijzerenzee.be/,IJzer en Zee,2026-08-19,official_register,tick1494; leftover woonmaatschappij of mined Veurne + leftover of mined westkust-westhoek 10 gemeenten; site + werkingsgebied Alveringem De Panne Diksmuide Houthulst Koekelare Koksijde Kortemark Lo-Reninge Nieuwpoort Veurne; zetel Brugse Steenweg 2 8630 Veurne; KBO 0405.261.842; FOI info@ijzerenzee.be",
        "src_kbo_ijez_0405261842,KBO IJzer en Zee 0405.261.842,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405261842,KBO,2026-08-19,official_register,tick1494; Actief since 20.08.1920; naam WOONMAATSCHAPPIJ IJZER EN ZEE since 16.12.2022; BV since 16.12.2022; zetel Brugse Steenweg 2 8630 Veurne since 05.06.2015; 2 VE; 18 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid since 20.08.1920; NACE 68.121 / 68.202",
        "src_ijez_foi_contact,IJzer en Zee FOI channel (info@ijzerenzee.be),https://www.ijzerenzee.be/contact/,IJzer en Zee,2026-08-19,official_register,tick1494; leftover woonmaatschappij of mined Veurne + leftover of mined westkust-westhoek; FOI ready not sent; NOT leftover AGB Veurne / leftover Thuiswest 1493 / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover Zetus 1490 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_ijez," in raw or raw.startswith(b"wm_ijez,"):
        raise SystemExit("wm_ijez already present")
    if b"0405.261.842" in raw or b"0405261842" in raw:
        raise SystemExit("IJzer en Zee KBO already present as entity")
    row = (
        "wm_ijez,Woonmaatschappij IJzer en Zee (leftover woonmaatschappij / social-housing BV of mined Veurne + leftover of mined De Panne / Diksmuide / Koksijde / Nieuwpoort / Alveringem / Houthulst / Koekelare / Kortemark / Lo-Reninge / westkust-westhoek 10 gemeenten; NOT leftover AGB Veurne already mined / leftover AGB Koksijde already mined / leftover AGB De Panne already mined / leftover AGB Vrije Tijd Nieuwpoort already mined / leftover IVVO already mined / leftover Viertoren 1421 / leftover Thuiswest 0405.553.535 / leftover Woonsprong 0405.260.456 / leftover Ons Onderdak 0405.501.570 / leftover Zetus 0405.196.516 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonmaatschappij IJzer et Zee SRL (logement social residuel Veurne / cote ouest / Westhoek),"
        "IJzer en Zee leftover social-housing company of mined Veurne + leftover mined westkust-westhoek cities (not leftover AGB Veurne / leftover Thuiswest / leftover Woonsprong / leftover Ons Onderdak / leftover Zetus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_veurne,nl,https://www.ijzerenzee.be/,info@ijzerenzee.be,Brugse Steenweg 2 8630 Veurne,"
        "tick1494 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.261.842 Actief since 20.08.1920; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 182256295 omzet 17969403 pers 2550095 30.6 VTE pnl 1773977 equity 39032061 cash 13132132 debt 140520313 capex 15386690 dividend 0; 2 VE; parent city_veurne; werkingsgebied 10 westkust-westhoek gemeenten; prefix ijez"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_ijez")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
