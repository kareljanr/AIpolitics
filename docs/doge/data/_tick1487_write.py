#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1487 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:20:00Z"
ENT = "wm_dvpk"
SRC = "src_dvpk_jr2025_nbb"
GAP = "gap_dvpk_omzet_19_57m_pers_4_72m_debt_307m_l5"
LB = "lb_dvpk_omzet_19_57m_pers_4_72m_debt_307m"
COMM = "comm_dvpk_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00192551.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},De Voorkempen official NBB WVV VOL-inb JR2025,{PDF},NBB / De Voorkempen,2026-08-19,primary_pdf,tick1487; leftover woonmaatschappij of mined Brecht + Kalmthout/Kapellen/Zoersel/Brasschaat/Schoten/Malle; official NBB WVV VOL-inb JR2025 PDF 66p / 2156809 bytes; deposit 2026-00192551; AV 15.06.2026; header 22.06.2026; pdfinfo created 24.06.2026 14:03:27 UTC; model VOL-inb 26.0.15 m82-f; KBO 0426.798.911; assets 352377695 cash 5091590 debt 306985521 pers 4716427 omzet 19566170 pnl 4666 equity 42644547",
        "src_dvpk_site,De Voorkempen official pages,https://www.devoorkempen-he.be/,De Voorkempen,2026-08-19,official_register,tick1487; leftover woonmaatschappij of mined Brecht + Voorkempen 15 gemeenten; site + werkingsgebied Brasschaat Brecht Essen Kalmthout Kapellen Malle Ranst Schilde Schoten Stabroek Wijnegem Wommelgem Wuustwezel Zandhoven Zoersel; zetel Nijverheidsstraat 3 2960 Brecht; KBO 0426.798.911",
        "src_kbo_dvpk_0426798911,KBO De Voorkempen 0426.798.911,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0426798911,KBO,2026-08-19,official_register,tick1487; Actief since 11.01.1985; naam DE VOORKEMPEN - H.E. since 24.07.1991; BV since 06.06.2023; zetel Nijverheidsstraat 3 2960 Brecht since 20.09.2004; 1 VE; 15 functiehouders; Werkgever RSZ since 01.01.1985; aanbestedende overheid",
        "src_dvpk_foi_contact,De Voorkempen FOI channel (info@devoorkempen-he.be),https://www.devoorkempen-he.be/,De Voorkempen,2026-08-19,official_register,tick1487; leftover woonmaatschappij of mined Brecht + Voorkempen 15 gemeenten; FOI ready not sent; NOT leftover RL de Voorkempen 1441 / leftover Erfgoed Voorkempen IOED 1425 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Wonen in Limburg 1486 / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_dvpk," in raw or raw.startswith(b"wm_dvpk,"):
        raise SystemExit("wm_dvpk already present")
    if b"0426.798.911" in raw or b"0426798911" in raw:
        raise SystemExit("De Voorkempen KBO already present as entity")
    row = (
        "wm_dvpk,De Voorkempen - H.E. (leftover woonmaatschappij / social-housing BV of mined Brecht + leftover of mined Kalmthout + Kapellen + Zoersel + Brasschaat + Schoten + Malle / Voorkempen 15 gemeenten; NOT leftover RL de Voorkempen 1441 / leftover Erfgoed Voorkempen IOED 1425 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover Wonen in Limburg 1486 / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "De Voorkempen - H.E. SRL (logement social residuel Voorkempen / Brecht),"
        "De Voorkempen leftover social-housing company of mined Brecht + Kalmthout/Kapellen/Zoersel/Brasschaat/Schoten/Malle (not leftover RL de Voorkempen / leftover Erfgoed Voorkempen / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover Wonen in Limburg / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_brecht,nl,https://www.devoorkempen-he.be/,info@devoorkempen-he.be,Nijverheidsstraat 3 2960 Brecht,"
        "tick1487 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0426.798.911 Actief since 11.01.1985; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 352377695 omzet 19566170 pers 4716427 58.5 VTE pnl 4666 equity 42644547 cash 5091590 debt 306985521 capex 32271841 dividend 0; 1 VE; parent city_brecht; werkingsgebied Voorkempen 15 gemeenten; prefix dvpk"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_dvpk")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
