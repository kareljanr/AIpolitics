#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1500 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:40:00Z"
ENT = "wm_vivs"
SRC = "src_vivs_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00122331.pdf"

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
        f"{SRC},Woonmaatschappij Vivus official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonmaatschappij Vivus,2026-08-19,primary_pdf,tick1500; leftover woonmaatschappij of mined Harelbeke + leftover of mined Waregem + leftover of mined Deerlijk + leftover of mined Anzegem + leftover of mined Wielsbeke + leftover of mined Dentergem + leftover of mined Oostrozebeke + leftover of mined Lendelede (werkingsgebied Zuid-West-Vlaanderen-Midden Anzegem Deerlijk Dentergem Harelbeke Lendelede Oostrozebeke Waregem Wielsbeke); official NBB WVV VOL-inb JR2025 PDF 58p / 1038131 bytes; deposit 2026-00122331; AV 26.05.2026; header 27.05.2026; pdfinfo created 27.05.2026 21:57:23 UTC; model VOL-inb 26.0.11 m82-f; KBO 0405.430.603; assets 303989219 cash 10772582 debt 237728579 pers 3214483 omzet 19547175 pnl 1023260 equity 63760761",
        "src_vivs_site,Woonmaatschappij Vivus official pages,https://www.vivus.be/,Woonmaatschappij Vivus,2026-08-19,official_register,tick1500; leftover woonmaatschappij of mined Harelbeke + leftover of mined Waregem + leftover of mined Deerlijk + leftover of mined Anzegem + leftover of mined Wielsbeke + leftover of mined Dentergem + leftover of mined Oostrozebeke + leftover of mined Lendelede; site + werkingsgebied Zuid-West-Vlaanderen-Midden Anzegem Deerlijk Dentergem Harelbeke Lendelede Oostrozebeke Waregem Wielsbeke; zetel Marktstraat 80 8530 Harelbeke; KBO 0405.430.603; FOI info@vivus.be",
        "src_kbo_vivs_0405430603,KBO Woonmaatschappij Vivus 0405.430.603,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405430603,KBO,2026-08-19,official_register,tick1500; Actief since 01.01.1968; naam Woonmaatschappij VIVUS since 01.06.2023; BV since 01.06.2023; zetel Marktstraat 80 8530 Harelbeke since 01.10.1990; 1 VE; 16 functiehouders; Werkgever RSZ since 01.04.1952; aanbestedende overheid since 01.01.1968; NACE 68.202; absorbeerde 0405.419.913 Helpt Elkander since 01.06.2023",
        "src_vivs_foi_contact,Woonmaatschappij Vivus FOI channel (info@vivus.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij/woonmaatschappij-vivus,Woonmaatschappij Vivus,2026-08-19,official_register,tick1500; leftover woonmaatschappij of mined Harelbeke + leftover of mined Waregem + leftover of mined Deerlijk + leftover of mined Anzegem + leftover of mined Wielsbeke + leftover of mined Dentergem + leftover of mined Oostrozebeke + leftover of mined Lendelede; FOI ready not sent; NOT leftover WM Elan 1499 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_vivs," in raw or raw.startswith(b"wm_vivs,"):
        raise SystemExit("wm_vivs already present")
    if b"0405.430.603" in raw or b"0405430603" in raw:
        raise SystemExit("Vivus KBO already present as entity")
    row = (
        "wm_vivs,Woonmaatschappij Vivus (leftover woonmaatschappij / social-housing BV of mined Harelbeke + leftover of mined Waregem + leftover of mined Deerlijk + leftover of mined Anzegem + leftover of mined Wielsbeke + leftover of mined Dentergem + leftover of mined Oostrozebeke + leftover of mined Lendelede / Zuid-West-Vlaanderen-Midden werkingsgebied Anzegem Deerlijk Dentergem Harelbeke Lendelede Oostrozebeke Waregem Wielsbeke; NOT leftover WM Elan 1499 prefix elan / leftover SW+ 1472 prefix swpl / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonstart 1495 / leftover Thuiswest 1493 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonmaatschappij Vivus SRL (logement social residuel Harelbeke / Centre-Flandre-Occidentale),"
        "Woonmaatschappij Vivus leftover social-housing company of mined Harelbeke + leftover mined Waregem + leftover mined Deerlijk + leftover mined Anzegem + leftover mined Wielsbeke + leftover mined Dentergem + leftover mined Oostrozebeke + leftover mined Lendelede (not leftover WM Elan / leftover SW+ / leftover !Mpuls / leftover WAGSO / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_harelbeke,nl,https://www.vivus.be/,info@vivus.be,Marktstraat 80 8530 Harelbeke,"
        "tick1500 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.430.603 Actief since 01.01.1968; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 303989219 omzet 19547175 pers 3214483 34.8 VTE pnl 1023260 equity 63760761 cash 10772582 debt 237728579 capex 18581782 dividend 0; 1 VE; parent city_harelbeke; werkingsgebied Anzegem + Deerlijk + Dentergem + Harelbeke + Lendelede + Oostrozebeke + Waregem + Wielsbeke; prefix vivs"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_vivs")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
