#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1501 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:15:00Z"
ENT = "wm_prvd"
SRC = "src_prvd_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00121288.pdf"

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
        f"{SRC},Providentia official NBB WVV VOL-inb JR2025,{PDF},NBB / Providentia,2026-08-19,primary_pdf,tick1501; leftover woonmaatschappij of mined Asse + leftover of mined Dilbeek + leftover of mined Affligem + leftover of mined Bever + leftover of mined Lennik + leftover of mined Liedekerke + leftover of mined Merchtem + leftover of mined Opwijk + leftover of mined Roosdaal + leftover of mined Ternat + leftover of mined Wemmel + leftover of mined Pajottegem (werkingsgebied Halle-Vilvoorde-Midden Affligem Asse Bever Dilbeek Lennik Liedekerke Merchtem Opwijk Pajottegem Roosdaal Ternat Wemmel); official NBB WVV VOL-inb JR2025 PDF 80p / 1196609 bytes; deposit 2026-00121288; AV 07.05.2026; header 22.05.2026; pdfinfo created 27.05.2026 01:06:02 UTC; model VOL-inb 23.0.9 m82-f; KBO 0403.320.060; assets 228332050 cash 5321913 debt 195927025 pers 3571584 omzet 20807498 pnl 1625580 equity 29021932",
        "src_prvd_site,Providentia official pages,https://www.providentia.be/,Providentia,2026-08-19,official_register,tick1501; leftover woonmaatschappij of mined Asse + leftover of mined Dilbeek + leftover of mined Affligem + leftover of mined Bever + leftover of mined Lennik + leftover of mined Liedekerke + leftover of mined Merchtem + leftover of mined Opwijk + leftover of mined Roosdaal + leftover of mined Ternat + leftover of mined Wemmel + leftover of mined Pajottegem; site + werkingsgebied Halle-Vilvoorde-Midden Affligem Asse Bever Dilbeek Lennik Liedekerke Merchtem Opwijk Pajottegem Roosdaal Ternat Wemmel; zetel Brusselsesteenweg 191 1730 Asse; KBO 0403.320.060; FOI info@providentia.be",
        "src_kbo_prvd_0403320060,KBO Providentia 0403.320.060,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0403320060,KBO,2026-08-19,official_register,tick1501; Actief since 01.01.1968; naam Providentia since 01.01.1968; BV since 15.06.2023; zetel Brusselsesteenweg 191 1730 Asse since 11.04.2005; 1 VE; 17 functiehouders; dagelijks bestuur Leen Deraedt since 15.06.2023; Werkgever RSZ since 01.01.1963; aanbestedende overheid since 01.01.1968; NACE 68.202",
        "src_prvd_foi_contact,Providentia FOI channel (info@providentia.be),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij,Providentia,2026-08-19,official_register,tick1501; leftover woonmaatschappij of mined Asse + leftover of mined Dilbeek + leftover of mined Affligem + leftover of mined Bever + leftover of mined Lennik + leftover of mined Liedekerke + leftover of mined Merchtem + leftover of mined Opwijk + leftover of mined Roosdaal + leftover of mined Ternat + leftover of mined Wemmel + leftover of mined Pajottegem; FOI ready not sent; NOT leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGA Asse / leftover Vivus 1500 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_prvd," in raw or raw.startswith(b"wm_prvd,"):
        raise SystemExit("wm_prvd already present")
    if b"0403.320.060" in raw or b"0403320060" in raw:
        raise SystemExit("Providentia KBO already present as entity")
    row = (
        "wm_prvd,Providentia (leftover woonmaatschappij / social-housing BV of mined Asse + leftover of mined Dilbeek + leftover of mined Affligem + leftover of mined Bever + leftover of mined Lennik + leftover of mined Liedekerke + leftover of mined Merchtem + leftover of mined Opwijk + leftover of mined Roosdaal + leftover of mined Ternat + leftover of mined Wemmel + leftover of mined Pajottegem / Halle-Vilvoorde-Midden werkingsgebied Affligem Asse Bever Dilbeek Lennik Liedekerke Merchtem Opwijk Pajottegem Roosdaal Ternat Wemmel; NOT leftover Woonpunt Zennevallei 1485 prefix wpzn / leftover Inter-Vilvoordse 1489 prefix ivlv / leftover Fluvius Halle-Vilvoorde / leftover Haviland / leftover AGA Asse / leftover AGB Ternat / leftover AGB Roosdaal / leftover AGB Merchtem / leftover Vivus 1500 prefix vivs / leftover WM Elan 1499 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Providentia SRL (logement social residuel Asse / Halle-Vilvorde-Centre),"
        "Providentia leftover social-housing company of mined Asse + leftover mined Dilbeek + leftover mined Affligem + leftover mined Bever + leftover mined Lennik + leftover mined Liedekerke + leftover mined Merchtem + leftover mined Opwijk + leftover mined Roosdaal + leftover mined Ternat + leftover mined Wemmel + leftover mined Pajottegem (not leftover Woonpunt Zennevallei / leftover Inter-Vilvoordse / leftover Fluvius Halle-Vilvoorde / leftover AGA Asse / leftover Vivus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_asse,nl,https://www.providentia.be/,info@providentia.be,Brusselsesteenweg 191 1730 Asse,"
        "tick1501 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0403.320.060 Actief since 01.01.1968; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 228332050 omzet 20807498 pers 3571584 39.1 VTE pnl 1625580 equity 29021932 cash 5321913 debt 195927025 capex 92686585 dividend 0; 1 VE; parent city_asse; werkingsgebied Affligem + Asse + Bever + Dilbeek + Lennik + Liedekerke + Merchtem + Opwijk + Pajottegem + Roosdaal + Ternat + Wemmel; prefix prvd"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_prvd")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
