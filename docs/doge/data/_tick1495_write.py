#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1495 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:00:00Z"
ENT = "wm_wstrt"
SRC = "src_wstrt_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00159134.pdf"

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
        f"{SRC},Woonstart official NBB WVV VKT-inb JR2025,{PDF},NBB / Woonstart,2026-08-19,primary_pdf,tick1495; leftover woonmaatschappij of mined Tielt + leftover of mined Pittem / Wingene (werkingsgebied also Meulebeke / Ruiselede); official NBB WVV VKT-inb JR2025 PDF 38p / 746796 bytes; deposit 2026-00159134; AV 09.06.2026; header 15.06.2026; pdfinfo created 15.06.2026 07:36:18 UTC; model VKT-inb 25.0.12 m81-f; KBO 0405.220.963; assets 97529158 cash 2036624 debt 81699993 pers 1536245 omzet 7325986 pnl -835178 equity 15514356",
        "src_wstrt_site,Woonstart official pages,https://woonstart.be/,Woonstart,2026-08-19,official_register,tick1495; leftover woonmaatschappij of mined Tielt + leftover of mined Pittem / Wingene; site + werkingsgebied Tielt Pittem Wingene Meulebeke Ruiselede (deels Aarsele Egem Kanegem Schuiferskapelle Zwevezele); zetel Sint-Michielstraat 1A 8700 Tielt; KBO 0405.220.963; FOI info@woonstart.be",
        "src_kbo_wstrt_0405220963,KBO Woonstart 0405.220.963,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0405220963,KBO,2026-08-19,official_register,tick1495; Actief since 30.08.1923; naam Woonstart since 09.06.2023; BV since 09.06.2023; zetel Sint-Michielstraat 1A 8700 Tielt since 01.01.2025; 1 VE; 17 functiehouders; Werkgever RSZ since 01.04.1999; aanbestedende overheid since 30.08.1923; NACE 68.202 / 68.121; absorbeerde IZI Wonen 0405.553.634 since 30.06.2023",
        "src_wstrt_foi_contact,Woonstart FOI channel (info@woonstart.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij/woonstart,Woonstart,2026-08-19,official_register,tick1495; leftover woonmaatschappij of mined Tielt + leftover of mined Pittem / Wingene; FOI ready not sent; NOT leftover AGB Tielt / leftover Woonstroom 1475 / leftover Thuiswest 1493 / leftover IJzer en Zee 1494 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_wstrt," in raw or raw.startswith(b"wm_wstrt,"):
        raise SystemExit("wm_wstrt already present")
    if b"0405.220.963" in raw or b"0405220963" in raw:
        raise SystemExit("Woonstart KBO already present as entity")
    row = (
        "wm_wstrt,Woonstart (leftover woonmaatschappij / social-housing BV of mined Tielt + leftover of mined Pittem / Wingene / Midwest-Oost werkingsgebied Tielt Pittem Wingene Meulebeke Ruiselede; NOT leftover AGB Tielt already mined / leftover AGB Wingene already mined / leftover Woonstroom 0404.033.605 prefix wstr / leftover Thuiswest 0405.553.535 / leftover IJzer en Zee 0405.261.842 / leftover Vivendo 1473 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonstart SRL (logement social residuel Tielt / Midwest-Est),"
        "Woonstart leftover social-housing company of mined Tielt + leftover mined Pittem / Wingene (not leftover AGB Tielt / leftover Woonstroom / leftover Thuiswest / leftover IJzer en Zee / leftover Vivendo / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_tielt,nl,https://woonstart.be/,info@woonstart.be,Sint-Michielstraat 1A 8700 Tielt,"
        "tick1495 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0405.220.963 Actief since 30.08.1923; live JR2025 official NBB WVV VKT-inb PDF; sourced euros assets 97529158 omzet 7325986 pers 1536245 17.1 VTE pnl -835178 equity 15514356 cash 2036624 debt 81699993 capex 31842106 dividend 0; 1 VE; parent city_tielt; werkingsgebied Tielt Pittem Wingene Meulebeke Ruiselede; prefix wstrt not wstr"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wstrt")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
