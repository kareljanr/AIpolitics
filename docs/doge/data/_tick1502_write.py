#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1502 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:40:00Z"
ENT = "wm_wvwa"
SRC = "src_wvwa_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00145176.pdf"

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
        f"{SRC},Het Vlaamse Woonanker official NBB WVV VOL-inb JR2025,{PDF},NBB / Het Vlaamse Woonanker,2026-08-19,primary_pdf,tick1502; leftover woonmaatschappij of mined Grimbergen + leftover of mined Kampenhout + leftover of mined Kapelle-op-den-Bos + leftover of mined Meise + leftover of mined Steenokkerzeel + leftover of mined Zemst + leftover of mined Sint-Pieters-Leeuw + leftover of Londerzeel + leftover of Drogenbos (werkingsgebied Halle-Vilvoorde-Noord / Brabantse Kouters Grimbergen Kampenhout Kapelle-op-den-Bos Londerzeel Meise Steenokkerzeel Zemst Drogenbos Sint-Pieters-Leeuw); official NBB WVV VOL-inb JR2025 PDF 61p / 998995 bytes; deposit 2026-00145176; AV 27.05.2026; header 02.06.2026; pdfinfo created 09.06.2026 02:15:13 UTC; model VOL-inb 23.0.9 m82-f; KBO 0403.304.026; assets 116281420 cash 2894405 debt 98315832 pers 1918960 omzet 11795988 pnl -960306 equity 16952289",
        "src_wvwa_site,Het Vlaamse Woonanker official pages,https://www.hetvlaamsewoonanker.be/,Het Vlaamse Woonanker,2026-08-19,official_register,tick1502; leftover woonmaatschappij of mined Grimbergen + leftover of mined Kampenhout + leftover of mined Kapelle-op-den-Bos + leftover of mined Meise + leftover of mined Steenokkerzeel + leftover of mined Zemst + leftover of mined Sint-Pieters-Leeuw + leftover of Londerzeel + leftover of Drogenbos; site + werkingsgebied Grimbergen Kampenhout Kapelle-op-den-Bos Londerzeel Meise Steenokkerzeel Zemst Drogenbos Sint-Pieters-Leeuw; zetel Bezemstraat 83 bus A 1600 Sint-Pieters-Leeuw; KBO 0403.304.026; FOI Ann@hvw.vlaanderen",
        "src_kbo_wvwa_0403304026,KBO Het Vlaamse Woonanker 0403.304.026,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0403304026,KBO,2026-08-19,official_register,tick1502; Actief since 17.11.1922; naam Het Vlaamse Woonanker since 05.08.2024; BV since 09.06.2023; zetel Bezemstraat 83 bus A 1600 Sint-Pieters-Leeuw since 14.10.2014; 1 VE; 16 functiehouders; voorzitter Bart Laeremans since 11.02.2025; dagelijks bestuur Elsje Du Bois since 01.11.2019 + Marc Paesmans since 01.01.2009; Werkgever RSZ since 01.01.1960; aanbestedende overheid since 17.11.1922; NACE 68.202",
        "src_wvwa_foi_contact,Het Vlaamse Woonanker FOI channel (Ann@hvw.vlaanderen),https://www.vlaanderen.be/organisaties/wonen-in-vlaanderen/zoek-een-woonmaatschappij,Het Vlaamse Woonanker,2026-08-19,official_register,tick1502; leftover woonmaatschappij of mined Grimbergen + leftover of mined Kampenhout + leftover of mined Kapelle-op-den-Bos + leftover of mined Meise + leftover of mined Steenokkerzeel + leftover of mined Zemst + leftover of mined Sint-Pieters-Leeuw + leftover of Londerzeel + leftover of Drogenbos; FOI ready not sent; NOT leftover Providentia 1501 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGB Grimbergen / leftover AGB Steenokkerzeel / leftover AGB Sint-Pieters-Leeuw / leftover AGB Zemst / leftover Erfgoed Brabantse Kouters 1428 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_wvwa," in raw or raw.startswith(b"wm_wvwa,"):
        raise SystemExit("wm_wvwa already present")
    if b"0403.304.026" in raw or b"0403304026" in raw:
        raise SystemExit("Het Vlaamse Woonanker KBO already present as entity")
    row = (
        "wm_wvwa,Het Vlaamse Woonanker (leftover woonmaatschappij / social-housing BV of mined Grimbergen + leftover of mined Kampenhout + leftover of mined Kapelle-op-den-Bos + leftover of mined Meise + leftover of mined Steenokkerzeel + leftover of mined Zemst + leftover of mined Sint-Pieters-Leeuw + leftover of Londerzeel + leftover of Drogenbos / Halle-Vilvoorde-Noord werkingsgebied Grimbergen Kampenhout Kapelle-op-den-Bos Londerzeel Meise Steenokkerzeel Zemst Drogenbos Sint-Pieters-Leeuw; NOT leftover Providentia 1501 prefix prvd / leftover Woonpunt Zennevallei 1485 prefix wpzn / leftover Inter-Vilvoordse 1489 prefix ivlv / leftover Fluvius Halle-Vilvoorde / leftover Haviland / leftover AGB Grimbergen / leftover AGB Steenokkerzeel / leftover AGB Sint-Pieters-Leeuw / leftover AGB Zemst / leftover Erfgoed Brabantse Kouters 1428 / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Het Vlaamse Woonanker SRL (logement social residuel Grimbergen / Halle-Vilvorde-Nord),"
        "Het Vlaamse Woonanker leftover social-housing company of mined Grimbergen + leftover mined Kampenhout + leftover mined Kapelle-op-den-Bos + leftover mined Meise + leftover mined Steenokkerzeel + leftover mined Zemst + leftover mined Sint-Pieters-Leeuw + leftover Londerzeel + leftover Drogenbos (not leftover Providentia / leftover Woonpunt Zennevallei / leftover Inter-Vilvoordse / leftover Fluvius Halle-Vilvoorde / leftover AGB Grimbergen / leftover Erfgoed Brabantse Kouters / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_sint_pieters_leeuw,nl,https://www.hetvlaamsewoonanker.be/,Ann@hvw.vlaanderen,Bezemstraat 83 bus A 1600 Sint-Pieters-Leeuw,"
        "tick1502 leftover residual woonmaatschappij after leftover AGB/APB hunt; KBO 0403.304.026 Actief since 17.11.1922; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 116281420 omzet 11795988 pers 1918960 22.7 VTE pnl -960306 equity 16952289 cash 2894405 debt 98315832 capex 1292536 dividend 0; 1 VE; parent city_sint_pieters_leeuw; werkingsgebied Grimbergen + Kampenhout + Kapelle-op-den-Bos + Londerzeel + Meise + Steenokkerzeel + Zemst + Drogenbos + Sint-Pieters-Leeuw; prefix wvwa"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_wvwa")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
