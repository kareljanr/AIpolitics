#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1505 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:10:00Z"
ENT = "wm_vitr"
SRC = "src_vitr_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00332427.pdf"

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
        f"{SRC},Vitare in vereffening official NBB WVV VOL-kap JR2025,{PDF},NBB / Vitare vereffenaars,2026-08-20,primary_pdf,tick1505; leftover former SHM / leftover unpublished official-41 of mined Deinze (lost SHM recognition 01.01.2023; Flemish-appointed liquidators); official NBB WVV VOL-kap JR2025 PDF 36p / 652219 bytes; deposit 2026-00332427; AV empty in vereffening; header 24.07.2026; vereffenaars signed 15.07.2026; pdfinfo created 27.07.2026 01:37:28 UTC; model VOL-kap 23.0.10 m02-f; KBO 0808.101.060; assets 17056698 cash 39058 debt 41297098 pers 0 omzet 15730 pnl 1964420 equity -24315400 nrec 2305848",
        "src_vitr_kbo_0808101060,KBO Vitare 0808.101.060,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0808101060,KBO,2026-08-20,official_register,tick1505; leftover former SHM of mined Deinze; NV in vereffening; KBO 0808.101.060; historic zetel Achiel Van Eechautestraat 13 bus 2 9800 Deinze; current zetel Coupure 88 9000 Gent; vereffenaars Paul Van Der Putten + Pieter Wouters Loksumstraat 25 1000 Brussel since 03.02.2023",
        "src_vitr_bvr_vereffening,BVR 03.02.2023 aanstelling vereffenaars Vitare NV,https://etaamb.openjustice.be/nl/besluit-van-de-vlaamse-regering-van-03-februari-2023_n2023030563.html,Vlaamse Regering / eJustice,2026-08-20,official_register,tick1505; leftover former SHM Vitare 0808.101.060; lost SHM recognition 01.01.2023; Flemish Government appointed liquidators; historic zetel Deinze",
        "src_vitr_foi_contact,Vitare vereffenaars FOI channel (postal Loksumstraat 25 1000 Brussel),https://etaamb.openjustice.be/nl/besluit-van-de-vlaamse-regering-van-03-februari-2023_n2023030563.html,Vitare vereffenaars / Vlaamse Regering,2026-08-20,official_register,tick1505; leftover former SHM of mined Deinze; FOI ready not sent; email unpublished; NOT leftover Dimensa 1466 / leftover AGB Deinze / leftover De Noorderkempen 1504 / leftover Meetjesland 1496 / leftover APB Inovant / Atlas / leftover Puyenbroeck",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\r\n"
    if b"\nwm_vitr," in raw or raw.startswith(b"wm_vitr,"):
        raise SystemExit("wm_vitr already present")
    if b"0808.101.060" in raw or b"0808101060" in raw:
        raise SystemExit("Vitare KBO already present as entity")
    row = (
        "wm_vitr,Vitare in vereffening (leftover former SHM / leftover unpublished official-41 of mined Deinze; lost SHM recognition 01.01.2023; Flemish-appointed liquidators; NOT leftover Dimensa 1466 prefix dmsa / leftover AGB Deinze / leftover Woonmaatschappij Meetjesland 1496 prefix wmml / leftover De Noorderkempen 1504 prefix dnkm / leftover Woontrots 1503 prefix wtrt / leftover Woonin / leftover De Ideale Woning=Thuisrand 1474 / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Vitare SA en liquidation (ancien SHM residuel Deinze),"
        "Vitare in liquidation leftover former social-housing company of mined Deinze (not leftover Dimensa / leftover AGB Deinze / leftover Meetjesland / leftover De Noorderkempen / leftover Woontrots / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover IVAREM / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_deinze,nl,,unpublished,Loksumstraat 25 1000 Brussel / Coupure 88 9000 Gent / historic Achiel Van Eechautestraat 13 bus 2 9800 Deinze,"
        "tick1505 leftover residual former SHM after leftover AGB/APB hunt; KBO 0808.101.060 NV in vereffening; live JR2025 official NBB WVV VOL-kap PDF; sourced euros assets 17056698 omzet 15730 pers 0 0 VTE pnl 1964420 equity -24315400 cash 39058 debt 41297098 capex 0 dividend 0 nrec 2305848; parent city_deinze; prefix vitr"
        "\r\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 wm_vitr")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
