#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1504 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:35:00Z"
ENT = "wm_dnkm"
SRC = "src_dnkm_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00131989.pdf"

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
        f"{SRC},Woonmaatschappij De Noorderkempen official NBB WVV VOL-inb JR2025,{PDF},NBB / Woonmaatschappij De Noorderkempen,2026-08-20,primary_pdf,tick1504; leftover woonmaatschappij of mined Merksplas + leftover of mined Hoogstraten + leftover of mined Arendonk + leftover of mined Ravels + leftover of mined Rijkevorsel (werkingsgebied Kempen-Noord Arendonk Hoogstraten Merksplas Ravels Rijkevorsel); official NBB WVV VOL-inb JR2025 PDF 70p / 842176 bytes; deposit 2026-00131989; AV 12.05.2026; header 28.05.2026; pdfinfo created 02.06.2026 13:58:38 UTC; model VOL-inb 26.0.11 m82-f; KBO 0427.003.106; assets 129317196 cash 2718970 debt 109233846 pers 1372325 omzet 7793810 pnl 853059 equity 19508599",
        "src_dnkm_site,Woonmaatschappij De Noorderkempen official pages,https://www.denoorderkempen.be/,Woonmaatschappij De Noorderkempen,2026-08-20,official_register,tick1504; leftover woonmaatschappij of mined Merksplas + leftover of mined Hoogstraten + leftover of mined Arendonk + leftover of mined Ravels + leftover of mined Rijkevorsel; site + werkingsgebied Arendonk Hoogstraten Merksplas Ravels Rijkevorsel; zetel Kweekstraat 4 bus b 2330 Merksplas; KBO 0427.003.106; FOI info@denoorderkempen.be",
        "src_kbo_dnkm_0427003106,KBO Woonmaatschappij De Noorderkempen 0427.003.106,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0427003106,KBO,2026-08-20,official_register,tick1504; Actief since 23.06.1984; naam Woonmaatschappij De Noorderkempen since 09.05.2023; BV since 01.06.2023; zetel Kweekstraat 4 bus b 2330 Merksplas since 12.06.2012; 1 VE; 11 functiehouders; voorzitter Hans Heylen since 09.05.2023; dagelijks bestuur Christophe Dekoninck since 01.07.2022; Werkgever RSZ since 15.06.1984; aanbestedende overheid since 23.06.1984; NACE 68.202",
        "src_dnkm_foi_contact,Woonmaatschappij De Noorderkempen FOI channel (info@denoorderkempen.be),https://denoorderkempen.be/contact/contacteer-ons,Woonmaatschappij De Noorderkempen,2026-08-20,official_register,tick1504; leftover woonmaatschappij of mined Merksplas + leftover of mined Hoogstraten + leftover of mined Arendonk + leftover of mined Ravels + leftover of mined Rijkevorsel; FOI ready not sent; NOT leftover Erfgoed Noorderkempen 1426 / leftover Bosgroep Kempen Noord 1450 / leftover Woonboog 1478 / leftover De Voorkempen 1487 / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_dnkm," in raw or raw.startswith(b"wm_dnkm,"):
        raise SystemExit("wm_dnkm already present")
    if b"0427.003.106" in raw or b"0427003106" in raw:
        raise SystemExit("De Noorderkempen KBO already present as entity")
    row = (
        "wm_dnkm,Woonmaatschappij De Noorderkempen (leftover woonmaatschappij / social-housing BV of mined Merksplas + leftover of mined Hoogstraten + leftover of mined Arendonk + leftover of mined Ravels + leftover of mined Rijkevorsel / Kempen-Noord werkingsgebied Arendonk Hoogstraten Merksplas Ravels Rijkevorsel; NOT leftover Erfgoed Noorderkempen 1426 prefix enpk / leftover Bosgroep Kempen Noord 1450 prefix bgkn / leftover Woonboog 1478 prefix wbog / leftover De Voorkempen 1487 prefix dvpk / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots 1503 prefix wtrt / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Woonmaatschappij De Noorderkempen SRL (logement social residuel Merksplas / Kempen-Nord),"
        "Woonmaatschappij De Noorderkempen leftover social-housing company of mined Merksplas + leftover mined Hoogstraten + leftover mined Arendonk + leftover mined Ravels + leftover mined Rijkevorsel (not leftover Erfgoed Noorderkempen / leftover Bosgroep Kempen Noord / leftover Woonboog / leftover De Voorkempen / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_merksplas,nl,https://www.denoorderkempen.be/,info@denoorderkempen.be,Kweekstraat 4 bus b 2330 Merksplas,"
        "tick1504 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0427.003.106 Actief since 23.06.1984; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 129317196 omzet 7793810 pers 1372325 18.3 VTE pnl 853059 equity 19508599 cash 2718970 debt 109233846 capex 42448162 dividend 0; 1 VE; parent city_merksplas; werkingsgebied Arendonk + Hoogstraten + Merksplas + Ravels + Rijkevorsel; prefix dnkm"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_dnkm")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
