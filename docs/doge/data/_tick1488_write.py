#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1488 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:26:00Z"
ENT = "wm_wsbn"
SRC = "src_wsbn_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131692.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonschakel Berg en Nete official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonschakel Berg en Nete,2026-08-19,primary_pdf,tick1488; leftover woonmaatschappij of mined Heist-op-den-Berg + leftover of mined Berlaar/Nijlen/Putte; official NBB WVV VOL-inb JR2025 PDF 91p / 2752616 bytes; deposit 2026-00131692; AV 24.04.2026; header 01.06.2026; pdfinfo created 02.06.2026 11:54:12 UTC; model VOL-inb 23.0.9 m82-f; KBO 0400.846.560; assets 155658879 cash 3462126 debt 136065192 pers 1957328 omzet 10995862 pnl 348212 equity 19159867",
        "src_wsbn_site,Woonschakel Berg en Nete official pages,https://www.woonschakelbergennete.be/,Woonschakel Berg en Nete,2026-08-19,official_register,tick1488; leftover woonmaatschappij of mined Heist-op-den-Berg + Berlaar/Nijlen/Putte; site + werkingsgebied Rivierenland-Oost 4 gemeenten; zetel Plantijnlaan 2 2220 Heist-op-den-Berg; KBO 0400.846.560; FOI info@wsben.vlaanderen",
        "src_kbo_wsbn_0400846560,KBO Woonschakel Berg en Nete 0400.846.560,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400846560,KBO,2026-08-19,official_register,tick1488; Actief since 01.01.1968; naam Woonschakel Berg en Nete since 01.07.2023; BV since 01.07.2023; zetel Plantijnlaan 2 2220 Heist-op-den-Berg since 25.11.1993; 2 VE; 16 functiehouders; Werkgever RSZ since 01.01.1959; aanbestedende overheid",
        "src_wsbn_foi_contact,Woonschakel Berg en Nete FOI channel (info@wsben.vlaanderen),https://www.woonschakelbergennete.be/,Woonschakel Berg en Nete,2026-08-19,official_register,tick1488; leftover woonmaatschappij of mined Heist-op-den-Berg + leftover of mined Berlaar/Nijlen/Putte; FOI ready not sent; NOT leftover cultuur-IGS Berg en Nete 0671.761.919 / leftover De Voorkempen 1487 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wsbn," in raw or raw.startswith(b"wm_wsbn,"):
        raise SystemExit("wm_wsbn already present")
    if b"0400.846.560" in raw or b"0400846560" in raw:
        raise SystemExit("Woonschakel KBO already present as entity")
    row = (
        "wm_wsbn,Woonschakel Berg en Nete (leftover woonmaatschappij / social-housing BV of mined Heist-op-den-Berg + leftover of mined Berlaar + Nijlen + Putte / Rivierenland-Oost 4 gemeenten; NOT leftover cultuur-IGS Berg en Nete 0671.761.919 / leftover De Voorkempen 1487 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover Inter-Vilvoordse / leftover Zetus / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonschakel Berg en Nete SRL (logement social residuel Heist-op-den-Berg / Rivierenland-Oost),"
        "Woonschakel Berg en Nete leftover social-housing company of mined Heist-op-den-Berg + Berlaar/Nijlen/Putte (not leftover cultuur-IGS Berg en Nete / leftover De Voorkempen / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Inter-Vilvoordse / leftover Zetus / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_heist_op_den_berg,nl,https://www.woonschakelbergennete.be/,info@wsben.vlaanderen,Plantijnlaan 2 2220 Heist-op-den-Berg,"
        "tick1488 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.846.560 Actief since 01.01.1968; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 155658879 omzet 10995862 pers 1957328 21.7 VTE pnl 348212 equity 19159867 cash 3462126 debt 136065192 capex 13398259 dividend 0; 2 VE; parent city_heist_op_den_berg; werkingsgebied Rivierenland-Oost 4 gemeenten; prefix wsbn"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wsbn")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
