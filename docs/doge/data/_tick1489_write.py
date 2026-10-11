#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1489 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:40:00Z"
ENT = "wm_ivlv"
SRC = "src_ivlv_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00138038.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Inter-Vilvoordse official NBB WVV VOL-inb JR2025,{PDF},NBB / Inter-Vilvoordse,2026-08-19,primary_pdf,tick1489; leftover woonmaatschappij of mined Vilvoorde + leftover of mined Machelen; official NBB WVV VOL-inb JR2025 PDF 57p / 4820480 bytes; deposit 2026-00138038; AV 27.05.2026; header 03.06.2026; pdfinfo created 05.06.2026 01:00:20 UTC; model VOL-inb 25.0.12 m82-f; KBO 0400.676.613; assets 175606699 cash 22766208 debt 135881516 pers 1996874 omzet 9370627 pnl 961462 equity 38667098",
        "src_ivlv_site,Inter-Vilvoordse official pages,https://intervilvoordse.be/,Inter-Vilvoordse,2026-08-19,official_register,tick1489; leftover woonmaatschappij of mined Vilvoorde + Machelen; site + werkingsgebied Vilvoorde-Machelen 2 gemeenten; zetel Parkstraat 115 1800 Vilvoorde; KBO 0400.676.613; FOI onthaal@intervilvoordse.be",
        "src_kbo_ivlv_0400676613,KBO Inter-Vilvoordse 0400.676.613,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400676613,KBO,2026-08-19,official_register,tick1489; Actief since 11.09.1920; naam Inter Vilvoordse Maatschappij voor Huisvesting since 29.04.1973; BV since 22.03.2023; zetel Parkstraat 115 1800 Vilvoorde since 24.06.1986; 1 VE; 11 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid",
        "src_ivlv_foi_contact,Inter-Vilvoordse FOI channel (onthaal@intervilvoordse.be),https://intervilvoordse.be/,Inter-Vilvoordse,2026-08-19,official_register,tick1489; leftover woonmaatschappij of mined Vilvoorde + leftover of mined Machelen; FOI ready not sent; NOT leftover AGB Vilvoorde / leftover Zetus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nwm_ivlv," in raw or raw.startswith(b"wm_ivlv,"):
        raise SystemExit("wm_ivlv already present")
    if b"0400.676.613" in raw or b"0400676613" in raw:
        raise SystemExit("Inter-Vilvoordse KBO already present as entity")
    row = (
        "wm_ivlv,Inter-Vilvoordse Maatschappij voor Huisvesting (leftover woonmaatschappij / social-housing BV of mined Vilvoorde + leftover of mined Machelen / Vilvoorde-Machelen 2 gemeenten; NOT leftover AGB Vilvoorde already mined / leftover Zetus 0405.196.516 / leftover Woonpunt Zennevallei 1485 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Inter-Vilvoordse SRL (logement social residuel Vilvoorde / Machelen),"
        "Inter-Vilvoordse leftover social-housing company of mined Vilvoorde + Machelen (not leftover AGB Vilvoorde / leftover Zetus / leftover Woonpunt Zennevallei / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_vilvoorde,nl,https://intervilvoordse.be/,onthaal@intervilvoordse.be,Parkstraat 115 1800 Vilvoorde,"
        "tick1489 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0400.676.613 Actief since 11.09.1920; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 175606699 omzet 9370627 pers 1996874 20.8 VTE pnl 961462 equity 38667098 cash 22766208 debt 135881516 capex 12018842 dividend 0; 1 VE; parent city_vilvoorde; werkingsgebied Vilvoorde + Machelen; prefix ivlv"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_ivlv")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
