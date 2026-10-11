#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1486 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:12:00Z"
ENT = "wm_wlim"
SRC = "src_wlim_jr2025_nbb"
GAP = "gap_wlim_omzet_149_76m_pers_32_78m_debt_1459m_l5"
LB = "lb_wlim_omzet_149_76m_pers_32_78m_debt_1459m"
COMM = "comm_wlim_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206025.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Wonen in Limburg official NBB WVV VOL-inb JR2025,{PDF},NBB / Wonen in Limburg,2026-08-19,primary_pdf,tick1486; leftover woonmaatschappij of mined Houthalen-Helchteren + Hasselt/Genk/Beringen/Maasmechelen; official NBB WVV VOL-inb JR2025 PDF 72p / 4703685 bytes; deposit 2026-00206025; AV 15.06.2026; header 22.06.2026; pdfinfo created 27.06.2026 01:12:29 UTC; model VOL-inb 23.0.10 m82-f; KBO 0401.314.140; assets 2060381293 cash 96287038 debt 1459270191 pers 32782938 omzet 149755087 pnl 5708426 equity 591815458",
        "src_wlim_site,Wonen in Limburg official pages,https://wil.be,Wonen in Limburg,2026-08-19,official_register,tick1486; leftover woonmaatschappij of mined Houthalen-Helchteren + Hasselt/Genk/Beringen/Maasmechelen; site + werkingsgebied provincie Limburg; zetel Ringlaan 20 3530 Houthalen-Helchteren; KBO 0401.314.140",
        "src_kbo_wlim_0401314140,KBO Wonen in Limburg 0401.314.140,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0401314140,KBO,2026-08-19,official_register,tick1486; Actief since 05.12.1953; naam Wonen in Limburg since 30.06.2023; BV since 30.06.2023; zetel Ringlaan 20 3530 Houthalen-Helchteren since 17.05.1986; 19 VE; 20 functiehouders; Werkgever RSZ since 01.10.1965; aanbestedende overheid",
        "src_wlim_foi_contact,Wonen in Limburg FOI channel (info@wil.be),https://wil.be,Wonen in Limburg,2026-08-19,official_register,tick1486; leftover woonmaatschappij of mined Houthalen-Helchteren + Hasselt/Genk/Beringen/Maasmechelen; FOI ready not sent; NOT leftover Dutch Wonen Limburg NL / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Woonpunt Zennevallei 1485 / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_wlim," in raw or raw.startswith(b"wm_wlim,"):
        raise SystemExit("wm_wlim already present")
    if b"0401.314.140" in raw or b"0401314140" in raw:
        raise SystemExit("Wonen in Limburg KBO already present as entity")
    row = (
        "wm_wlim,Wonen in Limburg (leftover woonmaatschappij / social-housing BV of mined Houthalen-Helchteren + leftover of mined Hasselt + Genk + Beringen + Maasmechelen / provincie Limburg; NOT leftover Dutch Wonen Limburg NL / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover Woonpunt Zennevallei 1485 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Wonen in Limburg SRL (logement social residuel Limbourg / Houthalen-Helchteren),"
        "Wonen in Limburg leftover social-housing company of mined Houthalen-Helchteren + Hasselt/Genk/Beringen/Maasmechelen (not leftover Dutch Wonen Limburg / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Woonpunt Zennevallei / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_houthalen_helchteren,nl,https://wil.be,info@wil.be,Ringlaan 20 3530 Houthalen-Helchteren,"
        "tick1486 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0401.314.140 Actief since 05.12.1953; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 2060381293 omzet 149755087 pers 32782938 397.5 VTE pnl 5708426 equity 591815458 cash 96287038 debt 1459270191 capex 106984224 dividend 0; 19 VE; parent city_houthalen_helchteren; werkingsgebied provincie Limburg; prefix wlim"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wlim")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
