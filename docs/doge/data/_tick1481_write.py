#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1481 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:50:00Z"
ENT = "wm_zkem"
SRC = "src_zkem_jr2025_nbb"
GAP = "gap_zkem_omzet_35_33m_pers_7_12m_debt_476m_l5"
LB = "lb_zkem_omzet_35_33m_pers_7_12m_debt_476m"
COMM = "comm_zkem_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00157303.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},LeefGoed official NBB WVV VOL-inb JR2025,{PDF},NBB / LeefGoed,2026-08-19,budget,tick1481; official NBB WVV VOL-inb JR2025 PDF 73p / 1286171 bytes; deposit 2026-00157303; AV 26.05.2026; header 08.06.2026; pdfinfo created 13.06.2026 00:30:22 UTC; model VOL-inb 26.0.12 m82-f; KBO 0404.144.065; assets 570754360 cash 16924292 debt 476306208 pers 7117830 omzet 35325415 pnl 417118 equity 92517644",
        "src_zkem_site,LeefGoed official pages,https://leefgoed.be/,LeefGoed / mined Geel + Herentals + Westerlo + Herselt + Hulshout + Olen + Grobbendonk + Herenthout + Laakdal + Meerhout + Vorselaar,2026-08-19,official_register,tick1481; leftover woonmaatschappij of mined Zuiderkempen-Neteland; zetel Kameinestraat 3 2440 Geel; KBO 0404.144.065; Busibee used for deposit-id discovery only",
        "src_kbo_zkem_0404144065,KBO LeefGoed 0404.144.065,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0404144065,KBO Public Search FOD Economie,2026-08-19,official_register,tick1481; Actief since 13.12.1947; BV since 06.05.2021; naam LeefGoed since 30.06.2023; zetel Kameinestraat 3 2440 Geel; 5 VE; 17 functiehouders; Werkgever RSZ since 01.01.1972; aanbestedende overheid",
        "src_zkem_foi_contact,LeefGoed FOI channel (info@leefgoed.be),https://leefgoed.be/,LeefGoed,2026-08-19,official_register,tick1481; leftover woonmaatschappij of mined Geel + Zuiderkempen-Neteland 11 gemeenten; NOT Woonboog 1478 / leftover stek92 / leftover Woonin / leftover Wooncompagnie / leftover WoonST / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_zkem," in raw or raw.startswith(b"wm_zkem,"):
        raise SystemExit("wm_zkem already present")
    if b"0404.144.065" in raw or b"0404144065" in raw:
        raise SystemExit("LeefGoed KBO already present as entity")
    row = (
        "wm_zkem,LeefGoed (leftover woonmaatschappij / social-housing BV of mined Geel + Herentals + Westerlo + Herselt + Hulshout + Olen + Grobbendonk + Herenthout + Laakdal + Meerhout + Vorselaar / Zuiderkempen-Neteland; Zonnige Kempen successor; NOT Woonboog 1478 / leftover stek92 / leftover Woonin / leftover Wooncompagnie / leftover WoonST / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof),"
        "LeefGoed SRL (logement social residuel Campine du Sud),"
        "LeefGoed leftover social-housing company of mined Geel + Herentals + Westerlo + Herselt + Hulshout + Olen (Zonnige Kempen successor; not Woonboog / leftover stek92 / leftover Woonin / leftover Wooncompagnie / leftover WoonST / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof),"
        "other,city_geel,nl,https://leefgoed.be/,info@leefgoed.be,Kameinestraat 3 2440 Geel,"
        "tick1481 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0404.144.065 Actief since 13.12.1947; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 570754360 omzet 35325415 pers 7117830 86.6 VTE pnl 417118 equity 92517644 cash 16924292 debt 476306208 capex 34832940 dividend 0; FOI ready omzet 35.33m DROP / pers 7.12m 86.6 VTE / debt 476.31m / cash 16.92m JUMP / PnL JUMP 0.42m / dividend 0 / 5 VE; distinct from already-mined Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_zkem")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
