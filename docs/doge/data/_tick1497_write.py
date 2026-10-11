#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1497 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:40:00Z"
ENT = "wm_thbw"
SRC = "src_thbw_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00200690.pdf"

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
        f"{SRC},de Thuisbouwer official NBB WVV VOL-inb JR2025,{PDF},NBB / de Thuisbouwer,2026-08-19,primary_pdf,tick1497; leftover woonmaatschappij of mined Hamme + leftover of mined Zele (werkingsgebied Dender-Noord Hamme Zele); official NBB WVV VOL-inb JR2025 PDF 53p / 1108201 bytes; deposit 2026-00200690; AV 11.06.2026; header 23.06.2026; pdfinfo created 26.06.2026 03:45:41 UTC; model VOL-inb 23.0.10 m82-f; KBO 0405.085.262; assets 202554297 cash 10773820 debt 125064700 pers 1868369 omzet 12474312 pnl 2048234 equity 75921924",
        "src_thbw_site,de Thuisbouwer official pages,https://dethuisbouwer.be/,de Thuisbouwer,2026-08-19,official_register,tick1497; leftover woonmaatschappij of mined Hamme + leftover of mined Zele; site + werkingsgebied Dender-Noord Hamme Zele (Moerzeke); zetel Rozenhoed 1 9220 Hamme; kantoor Acacialaan 49 bus W13 9240 Zele; KBO 0405.085.262; FOI info@dethuisbouwer.be",
        "src_kbo_thbw_0405085262,KBO de Thuisbouwer 0405.085.262,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405085262,KBO,2026-08-19,official_register,tick1497; Actief since 01.01.1968; naam DE THUISBOUWER since 30.06.2023; BV since 30.06.2023; zetel Rozenhoed 1 9220 Hamme since 01.10.1990; 2 VE; 17 functiehouders; Werkgever RSZ since 01.04.1955; aanbestedende overheid since 01.01.1968; NACE 68.202 / 68.121; absorbeerde GMVW 0400.189.930 since 08.06.2023",
        "src_thbw_foi_contact,de Thuisbouwer FOI channel (info@dethuisbouwer.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij/de-thuisbouwer,de Thuisbouwer,2026-08-19,official_register,tick1497; leftover woonmaatschappij of mined Hamme + leftover of mined Zele; FOI ready not sent; NOT leftover AGB HIM Hamme / leftover AGB Zele / leftover stek92 1482 / leftover Dender-Zuid 1467 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_thbw," in raw or raw.startswith(b"wm_thbw,"):
        raise SystemExit("wm_thbw already present")
    if b"0405.085.262" in raw or b"0405085262" in raw:
        raise SystemExit("de Thuisbouwer KBO already present as entity")
    row = (
        "wm_thbw,de Thuisbouwer (leftover woonmaatschappij / social-housing BV of mined Hamme + leftover of mined Zele / Dender-Noord werkingsgebied Hamme Zele; NOT leftover AGB HIM Hamme already mined / leftover AGB Zele already mined / leftover stek92 0400.189.732 prefix stk9 / leftover Dender-Zuid 1467 / leftover WoonST 1483 / leftover Tuinwijk 1469 / leftover Meetjesland 0401.033.236 / leftover Woonstart 0405.220.963 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "de Thuisbouwer SRL (logement social residuel Hamme / Dender-Nord),"
        "de Thuisbouwer leftover social-housing company of mined Hamme + leftover mined Zele (not leftover AGB HIM Hamme / leftover AGB Zele / leftover stek92 / leftover Dender-Zuid / leftover Meetjesland / leftover Woonstart / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_hamme,nl,https://dethuisbouwer.be/,info@dethuisbouwer.be,Rozenhoed 1 9220 Hamme,"
        "tick1497 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.085.262 Actief since 01.01.1968; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 202554297 omzet 12474312 pers 1868369 20.1 VTE pnl 2048234 equity 75921924 cash 10773820 debt 125064700 capex 12121406 dividend 1075; 2 VE; parent city_hamme; werkingsgebied Hamme + Zele; prefix thbw"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_thbw")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
