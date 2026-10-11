#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1482 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:10:00Z"
ENT = "wm_stk9"
SRC = "src_stk9_jr2025_nbb"
GAP = "gap_stk9_omzet_14_56m_pers_5_21m_debt_169m_l5"
LB = "lb_stk9_omzet_14_56m_pers_5_21m_debt_169m"
COMM = "comm_stk9_jr2025_omzet"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00288124.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},stek92 official NBB WVV VOL-inb JR2025,{PDF},NBB / stek92,2026-08-19,budget,tick1482; official NBB WVV VOL-inb JR2025 PDF 57p / 1181166 bytes; deposit 2026-00288124; AV 08.06.2026; header 06.07.2026; pdfinfo created 14.07.2026 04:30:31 UTC; model VOL-inb 23.0.10 m82-f; KBO 0400.189.732; assets 228254549 cash 18887511 debt 168788912 pers 5207321 omzet 14564880 pnl -1546368 equity 58118603",
        "src_stk9_site,stek92 official pages,https://www.stek92.be/,stek92 / mined Dendermonde + Berlare + Buggenhout + Lebbeke,2026-08-19,official_register,tick1482; leftover woonmaatschappij of mined Dendermonde-Dender-Waasland; zetel Pijnderslaan 2 9200 Dendermonde; KBO 0400.189.732; NBB consult used for deposit-id discovery only",
        "src_kbo_stk9_0400189732,KBO stek92 0400.189.732,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400189732,KBO Public Search FOD Economie,2026-08-19,official_register,tick1482; Actief since 24.05.1928; BV since 10.12.2022; naam stek92 since 10.12.2022; zetel Pijnderslaan 2 9200 Dendermonde; 1 VE; 12 functiehouders; Werkgever RSZ since 01.04.1979; aanbestedende overheid",
        "src_stk9_foi_contact,stek92 FOI channel (info@stek92.be),https://www.stek92.be/,stek92,2026-08-19,official_register,tick1482; leftover woonmaatschappij of mined Dendermonde + Berlare + Buggenhout + Lebbeke; NOT leftover WoonST Temse / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_stk9," in raw or raw.startswith(b"wm_stk9,"):
        raise SystemExit("wm_stk9 already present")
    if b"0400.189.732" in raw or b"0400189732" in raw:
        raise SystemExit("stek92 KBO already present as entity")
    row = (
        "wm_stk9,stek92 (leftover woonmaatschappij / social-housing BV of mined Dendermonde + Berlare + Buggenhout + Lebbeke; NOT leftover WoonST Temse / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof),"
        "stek92 SRL (logement social residuel Termonde),"
        "stek92 leftover social-housing company of mined Dendermonde + Berlare + Buggenhout + Lebbeke (not leftover WoonST Temse / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck / leftover Bosgroep / leftover Dommelhof),"
        "other,city_dendermonde,nl,https://www.stek92.be/,info@stek92.be,Pijnderslaan 2 9200 Dendermonde,"
        "tick1482 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.189.732 Actief since 24.05.1928; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 228254549 omzet 14564880 pers 5207321 48.5 VTE pnl -1546368 equity 58118603 cash 18887511 debt 168788912 capex 9157319 dividend 0; FOI ready omzet 14.56m DROP / pers 5.21m 48.5 VTE / debt 168.79m / cash 18.89m DROP / PnL LOSS 1.55m / dividend 0 / 1 VE; distinct from already-mined LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_stk9")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
