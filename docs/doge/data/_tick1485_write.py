#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1485 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:55:00Z"
ENT = "wm_wpzn"
SRC = "src_wpzn_jr2025_nbb"
GAP = "gap_wpzn_omzet_15_27m_pers_3_13m_debt_108m_l5"
LB = "lb_wpzn_omzet_15_27m_pers_3_13m_debt_108m"
COMM = "comm_wpzn_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00145529.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Woonpunt Zennevallei official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonpunt Zennevallei,2026-08-19,primary_pdf,tick1485; leftover woonmaatschappij of mined Halle + Beersel; official NBB WVV VOL-inb JR2025 PDF 64p / 1344945 bytes; deposit 2026-00145529; AV 01.06.2026; header 08.06.2026; pdfinfo created 09.06.2026 07:29:35 UTC; model VOL-inb 23.0.9 m82-f; KBO 0400.898.624; assets 162911198 cash 4801403 debt 108036213 pers 3128980 omzet 15271056 pnl 741465 equity 47335265",
        "src_wpzn_site,Woonpunt Zennevallei official pages,https://www.wpz.be,Woonpunt Zennevallei,2026-08-19,official_register,tick1485; leftover woonmaatschappij of mined Halle + Beersel; site + werkingsgebied Beersel + Drogenbos + Halle + Linkebeek + Pepingen + Sint-Genesius-Rode + Sint-Pieters-Leeuw; zetel Molenborre 26 bus 1 1500 Halle; KBO 0400.898.624",
        "src_kbo_wpzn_0400898624,KBO Woonpunt Zennevallei 0400.898.624,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400898624,KBO,2026-08-19,official_register,tick1485; Actief since 21.09.1920; naam WOONPUNT ZENNEVALLEI since 22.12.2009; BV since 08.11.2022; zetel Molenborre 26 bus 1 1500 Halle since 21.05.2007; 1 VE; 16 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_wpzn_foi_contact,Woonpunt Zennevallei FOI channel (info@wpz.be),https://www.wpz.be,Woonpunt Zennevallei,2026-08-19,official_register,tick1485; leftover woonmaatschappij of mined Halle + Beersel; FOI ready not sent; NOT leftover Woonpunt Waas 1464 / leftover !Mpuls 1484 / leftover WoonST 1483 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wpzn," in raw or raw.startswith(b"wm_wpzn,"):
        raise SystemExit("wm_wpzn already present")
    if b"0400.898.624" in raw or b"0400898624" in raw:
        raise SystemExit("Woonpunt Zennevallei KBO already present as entity")
    row = (
        "wm_wpzn,Woonpunt Zennevallei (leftover woonmaatschappij / social-housing BV of mined Halle + leftover of mined Beersel / Halle-Vilvoorde-Zuid; NOT leftover Woonpunt Waas 1464 / leftover !Mpuls 1484 / leftover WoonST 1483 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonpunt Zennevallei SRL (logement social residuel Hal + Beersel),"
        "Woonpunt Zennevallei leftover social-housing company of mined Halle + Beersel (not leftover Woonpunt Waas / leftover !Mpuls / leftover WoonST / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_halle,nl,https://www.wpz.be,info@wpz.be,Molenborre 26 bus 1 1500 Halle,"
        "tick1485 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.898.624 Actief since 21.09.1920; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 162911198 omzet 15271056 pers 3128980 37.3 VTE pnl 741465 equity 47335265 cash 4801403 debt 108036213 capex 10461618 dividend 0; 1 VE; parent city_halle; werkingsgebied Beersel + Drogenbos + Halle + Linkebeek + Pepingen + Sint-Genesius-Rode + Sint-Pieters-Leeuw; prefix wpzn"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wpzn")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
