#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1493 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:20:00Z"
ENT = "wm_thws"
SRC = "src_thws_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00263016.pdf"

def append_crlf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    block = "".join((r if r.endswith("\n") else r + "\r\n") for r in rows)
    if "\n" in block and "\r\n" not in block:
        block = block.replace("\n", "\r\n")
    # rows may already include \r\n
    out = []
    for r in rows:
        r = r.rstrip("\r\n") + "\r\n"
        out.append(r)
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_crlf(DATA / "sources.csv", [
        f"{SRC},Thuiswest official NBB WVV VOL-inb JR2025,{PDF},NBB / Thuiswest,2026-08-19,primary_pdf,tick1493; leftover woonmaatschappij of mined Roeselare + leftover of mined Izegem / Poperinge / Torhout / Ingelmunster / Ardooie / Hooglede / Lichtervelde / Staden / Moorslede / Langemark-Poelkapelle / Zonnebeke / Ledegem / Vleteren; official NBB WVV VOL-inb JR2025 PDF 52p / 357403 bytes; deposit 2026-00263016; AV 09.06.2026; header 01.07.2026; pdfinfo created 07.07.2026 22:13:00 UTC; model VOL-inb 26.0.15 m82-f; KBO 0405.553.535; assets 603044813 cash 24569716 debt 449999751 pers 7596389 omzet 40776434 pnl -1879750 equity 148379349",
        "src_thws_site,Thuiswest official pages,https://www.thuiswest.be/,Thuiswest,2026-08-19,official_register,tick1493; leftover woonmaatschappij of mined Roeselare + 13 leftover mined Midden-West-Vlaanderen cities; site + werkingsgebied 14 gemeenten; zetel Groenestraat 224 8800 Roeselare; KBO 0405.553.535; FOI info@thuiswest.be",
        "src_kbo_thws_0405553535,KBO Thuiswest 0405.553.535,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405553535,KBO,2026-08-19,official_register,tick1493; Actief since 03.09.1920; naam Thuiswest since 30.06.2023; BV since 30.06.2023; zetel Groenestraat 224 8800 Roeselare since 23.04.2013; 1 VE; 20 functiehouders; Werkgever RSZ since 01.01.1945; aanbestedende overheid since 03.09.1920; NACE 68.202",
        "src_thws_foi_contact,Thuiswest FOI channel (info@thuiswest.be),https://www.thuiswest.be/,Thuiswest,2026-08-19,official_register,tick1493; leftover woonmaatschappij of mined Roeselare + leftover of mined Izegem / Poperinge / Torhout; FOI ready not sent; NOT leftover Motena Roeselare / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_thws," in raw or raw.startswith(b"wm_thws,"):
        raise SystemExit("wm_thws already present")
    if b"0405.553.535" in raw or b"0405553535" in raw:
        raise SystemExit("Thuiswest KBO already present as entity")
    row = (
        "wm_thws,Thuiswest (leftover woonmaatschappij / social-housing BV of mined Roeselare + leftover of mined Izegem / Poperinge / Torhout / Ingelmunster / Ardooie / Hooglede / Lichtervelde / Staden / Moorslede / Langemark-Poelkapelle / Zonnebeke / Ledegem / Vleteren / 14 WVL gemeenten; NOT leftover Motena Roeselare already mined / leftover AGB AGIZ Izegem already mined / leftover AGB De Kouter Poperinge already mined / leftover AGB Ardooie already mined / leftover AGB MMP1917 Zonnebeke already mined / leftover Woonsprong 0405.260.456 / leftover Ons Onderdak 0405.501.570 / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Thuiswest SRL (logement social residuel Roeselare / Midden-West-Vlaanderen),"
        "Thuiswest leftover social-housing company of mined Roeselare + leftover mined Midden-West-Vlaanderen cities (not leftover Motena Roeselare / leftover Woonsprong / leftover Ons Onderdak / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_roeselare,nl,https://www.thuiswest.be/,info@thuiswest.be,Groenestraat 224 8800 Roeselare,"
        "tick1493 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.553.535 Actief since 03.09.1920; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 603044813 omzet 40776434 pers 7596389 90.9 VTE pnl -1879750 equity 148379349 cash 24569716 debt 449999751 capex 19362596 dividend 0; 1 VE; parent city_roeselare; werkingsgebied 14 WVL gemeenten; prefix thws"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_thws")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
