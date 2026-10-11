#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1552 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvsg"
SRC = "src_vvsg_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00217075.pdf"
GAP = "gap_vvsg_opbr_31_27m_pers_23_00m_accrued_jump_l5"
LB = "lb_vvsg_opbr_31_27m_pers_23_00m_accrued_jump"
COMM = "comm_vvsg_jr2025_opbr"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

def part_sources():
    rows = [
        f"{SRC},VVSG official NBB VOL-VZW JR2025 deposit 2026-00217075,{PDF},Nationale Bank van Belgie / VVSG vzw,2026-08-20,budget,tick1552; official NBB WVV VOL-VZW PDF 125p / 2164004 bytes; deposit 2026-00217075 Initial; model VOL-VZW 25.0.13 m05-f; AV 24.06.2026; year-end 31.12.2025; pdfinfo created 30.06.2026 01:06:32 UTC OpenPDF 1.3.26; euros PDF only; envelope bedrijfsopbrengsten 70/76A 31266193 (leftover public koepel VZW; omzet 70 present but commercial-only 2672153; not CREMABRU omzet-envelope)",
        "src_vvsg_nbb_consult,NBB consult VVSG 0451857573 published deposit 2026-00217075,https://consult.cbso.nbb.be/consult-enterprise/0451857573,Nationale Bank van Belgie,2026-08-20,official_register,tick1552; leftover public koepel VZW of mined Flemish cities; official NBB consult lists JR2025 deposit 2026-00217075 year-end 31.12.2025 Volledig model vereniging; official CDN 2164004 bytes",
        "src_vvsg_kbo_0451857573_1552,KBO VVSG vzw 0451.857.573 (tick1552),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451857573,FPS Economy KBO,2026-08-20,official_register,tick1552; leftover public koepel VZW of mined Flemish cities; KBO 0451.857.573 Actief official kbo-bce.fgov.be; zetel Bischoffsheimlaan 1-8 1000 Brussel; prefix vzw_vvsg unused",
        "src_vvsg_foi_contact_1552,VVSG FOI channel (info@vvsg.be),https://www.vvsg.be,VVSG vzw,2026-08-20,official_web,tick1552; leftover public koepel VZW of mined Flemish cities; FOI ready not sent; Bischoffsheimlaan 1-8 1000 Brussel; official e-mail info@vvsg.be; NOT leftover VVP / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_vvsg," in raw:
        raise SystemExit("vzw_vvsg already present")
    if "0451.857.573" in raw or "0451857573" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1552 leftover public koepel VZW residual of mined Flemish cities after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0451.857.573 Actief official kbo-bce.fgov.be; zetel Bischoffsheimlaan 1-8 1000 Brussel; live official NBB VOL-VZW deposit 2026-00217075 125p 2164004; sourced euros assets 43332320 opbr 31266193 omzet 2672153 subsid 27759906 pers 22996957 vte 208.5 expl 103938 PROFIT pnl 45220 PROFIT cash 1857566 DROP handelsrecv 9690908 JUMP accrued 28627254 JUMP; FOI ready not sent; parent sec_flanders; prefix vzw_vvsg unused; NOT leftover VVP / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Vereniging van Vlaamse Steden en Gemeenten V.V.S.G. (leftover public koepel VZW of mined Flemish cities; NOT leftover VVP / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549),Association des Villes et Communes flamandes ASBL (koepel residuel des villes flamandes),Association of Flemish Cities and Municipalities leftover public koepel VZW of mined Flemish cities,other,sec_flanders,nl,https://www.vvsg.be,info@vvsg.be,Bischoffsheimlaan 1-8 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_vvsg", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
