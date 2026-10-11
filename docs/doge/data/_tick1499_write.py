#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1499 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:20:00Z"
ENT = "wm_elan"
SRC = "src_elan_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00144589.pdf"

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
        f"{SRC},WM Elan official NBB WVV VOL-inb JR2025,{PDF},NBB / WM Elan,2026-08-19,primary_pdf,tick1499; leftover woonmaatschappij of mined Zwevegem + leftover of mined Kuurne + leftover of mined Avelgem + leftover of mined Spiere-Helkijn (werkingsgebied Zuid-West-Vlaanderen-Zuid Avelgem Kuurne Spiere-Helkijn Zwevegem); official NBB WVV VOL-inb JR2025 PDF 72p / 992461 bytes; deposit 2026-00144589; AV 02.06.2026; header 04.06.2026; pdfinfo created 09.06.2026 01:01:36 UTC; model VOL-inb 26.0.12 m82-f; KBO 0405.412.092; assets 179416827 cash 9893916 debt 136938057 pers 2241828 omzet 10963582 pnl 1657825 equity 40289353",
        "src_elan_site,WM Elan official pages,https://www.wmelan.be/,WM Elan,2026-08-19,official_register,tick1499; leftover woonmaatschappij of mined Zwevegem + leftover of mined Kuurne + leftover of mined Avelgem + leftover of mined Spiere-Helkijn; site + werkingsgebied Zuid-West-Vlaanderen-Zuid Avelgem Kuurne Spiere-Helkijn Zwevegem; zetel Kortrijkstraat 117 8550 Zwevegem; KBO 0405.412.092; FOI info@wmelan.be",
        "src_kbo_elan_0405412092,KBO WM Elan 0405.412.092,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405412092,KBO,2026-08-19,official_register,tick1499; Actief since 14.01.1923; naam WM Elan since 02.05.2023; BV since 02.05.2023; zetel Kortrijkstraat(Z) 117 8550 Zwevegem since 11.06.2001; 2 VE; 16 functiehouders; Werkgever RSZ since 01.10.1962; aanbestedende overheid since 14.01.1923; NACE 68.202; absorbeerde 0405.336.274 Eigen Gift Eigen Hulp since 02.05.2023",
        "src_elan_foi_contact,WM Elan FOI channel (info@wmelan.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij,WM Elan,2026-08-19,official_register,tick1499; leftover woonmaatschappij of mined Zwevegem + leftover of mined Kuurne + leftover of mined Avelgem + leftover of mined Spiere-Helkijn; FOI ready not sent; NOT leftover AGB Zwevegem already mined / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus / leftover Woonpijler 1498 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_elan," in raw or raw.startswith(b"wm_elan,"):
        raise SystemExit("wm_elan already present")
    if b"0405.412.092" in raw or b"0405412092" in raw:
        raise SystemExit("WM Elan KBO already present as entity")
    row = (
        "wm_elan,WM Elan (leftover woonmaatschappij / social-housing BV of mined Zwevegem + leftover of mined Kuurne + leftover of mined Avelgem + leftover of mined Spiere-Helkijn / Zuid-West-Vlaanderen-Zuid werkingsgebied Avelgem Kuurne Spiere-Helkijn Zwevegem; NOT leftover AGB Zwevegem already mined / leftover SW+ 1472 prefix swpl / leftover !Mpuls 1484 / leftover Vivus / leftover Woonpijler 0400.143.608 prefix wpij / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "WM Elan SRL (logement social residuel Zwevegem / Sud-Flandre-Occidentale),"
        "WM Elan leftover social-housing company of mined Zwevegem + leftover mined Kuurne + leftover mined Avelgem + leftover mined Spiere-Helkijn (not leftover AGB Zwevegem / leftover SW+ / leftover !Mpuls / leftover Vivus / leftover Woonpijler / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_zwevegem,nl,https://www.wmelan.be/,info@wmelan.be,Kortrijkstraat 117 8550 Zwevegem,"
        "tick1499 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.412.092 Actief since 14.01.1923; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 179416827 omzet 10963582 pers 2241828 26.8 VTE pnl 1657825 equity 40289353 cash 9893916 debt 136938057 capex 16411769 dividend 0; 2 VE; parent city_zwevegem; werkingsgebied Avelgem + Kuurne + Spiere-Helkijn + Zwevegem; prefix elan"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_elan")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
