#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1559 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_knst"
SRC = "src_kunstenpunt_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00065820.pdf"
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
        f"{SRC},Kunstensteunpunt official NBB VKT-VZW JR2025 deposit 2026-00065820,{PDF},Nationale Bank van Belgie / Kunstensteunpunt VZW,2026-08-20,budget,tick1559; official NBB WVV VKT-VZW PDF 15p / 50963 bytes; deposit 2026-00065820 Initial; model VKT-VZW 23.0.6 m04-f; AV 23.03.2026; year-end 31.12.2025; pdfinfo created 30.03.2026 12:49:16 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 1713627 (leftover public koepel VZW; VKT and omzet 70 empty; not VLUHR 1555 omzet-envelope / not VLIR 1556 bedrijfsopbrengsten-envelope)",
        "src_kunstenpunt_nbb_consult,NBB consult Kunstensteunpunt 0544715970 published deposit 2026-00065820,https://consult.cbso.nbb.be/consult-enterprise/0544715970,Nationale Bank van Belgie,2026-08-20,official_register,tick1559; leftover public koepel VZW of mined Flanders; official NBB consult enterprise page; official CDN 50963 bytes / 15p VKT-VZW",
        "src_kunstenpunt_kbo_0544715970_1559,KBO Kunstensteunpunt VZW 0544.715.970 (tick1559),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=544715970,FPS Economy KBO,2026-08-20,official_register,tick1559; leftover public koepel VZW of mined Flanders; KBO 0544.715.970 Actief official kbo-bce.fgov.be; naam KUNSTENSTEUNPUNT; afkorting KSP sinds 17.12.2013; rechtsvorm VZW sinds 17.12.2013; KBO zetel Ravensteingalerij 38 1000 Brussel; 1 VE; RSZ-werkgever sinds 01.11.2014; geen KBO-hoedanigheid aanbestedende overheid; prefix vzw_knst unused",
        "src_kunstenpunt_foi_contact_1559,Kunstenpunt FOI channel (info@kunsten.be / kunsten.be),https://www.kunsten.be/,Kunstensteunpunt VZW,2026-08-20,official_web,tick1559; leftover public koepel VZW of mined Flanders; FOI ready not sent; JR PDF Ravensteingalerij 38 1000 Brussel; official e-mail info@kunsten.be; current site kunsten.be; NOT leftover meemoo 1558 / leftover FARO still JR2024 / leftover VLHORA 1557",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_knst," in raw:
        raise SystemExit("vzw_knst already present")
    if "0544.715.970" in raw or "0544715970" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1559 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 so leftover Kunstensteunpunt with live official CDN taken; KBO 0544.715.970 Actief official kbo-bce.fgov.be; naam KUNSTENSTEUNPUNT; afkorting KSP sinds 17.12.2013; rechtsvorm VZW sinds 17.12.2013; KBO zetel Ravensteingalerij 38 1000 Brussel; RSZ-werkgever sinds 01.11.2014; geen KBO-hoedanigheid aanbestedende overheid; live official NBB VKT-VZW deposit 2026-00065820 15p 50963; sourced euros assets 677951 bruto 1713627 omzet empty 73 empty pers 1742627 vte 20 expl -57096 LOSS pnl -57334 LOSS cash DROP 324544 lev JUMP 70453 accrued JUMP 57176 prepaid JUMP 42818; FOI ready not sent; parent sec_flanders; prefix vzw_knst unused; NOT leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Kunstensteunpunt / Kunstenpunt / KSP (leftover public koepel VZW of mined Flanders; NOT leftover meemoo 1558 / leftover FARO still JR2024 / leftover VLHORA 1557),Point d appui des arts asbl (koepel residuel de la Flandre),Flanders Arts Institute leftover public koepel non-profit of mined Flanders,other,sec_flanders,nl,https://www.kunsten.be/,info@kunsten.be,Ravensteingalerij 38 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_knst", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
