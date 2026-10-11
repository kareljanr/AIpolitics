#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1560 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_soci"
SRC = "src_socius_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00065726.pdf"
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
        f"{SRC},Socius official NBB VKT-VZW JR2025 deposit 2026-00065726,{PDF},Nationale Bank van Belgie / Socius VZW,2026-08-20,budget,tick1560; official NBB WVV VKT-VZW PDF 13p / 50636 bytes; deposit 2026-00065726 Initial; model VKT-VZW 26.0.8 m04-f; AV 25.03.2026; year-end 31.12.2025; pdfinfo created 30.03.2026 12:29:28 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 1380002 (leftover public koepel VZW; VKT and omzet 70 empty; not VLUHR 1555 omzet-envelope / not VLIR 1556 bedrijfsopbrengsten-envelope)",
        "src_socius_nbb_consult,NBB consult Socius 0430838564 published deposit 2026-00065726,https://consult.cbso.nbb.be/consult-enterprise/0430838564,Nationale Bank van Belgie,2026-08-20,official_register,tick1560; leftover public koepel VZW of mined Flanders; official NBB consult enterprise page; official CDN 50636 bytes / 13p VKT-VZW",
        "src_socius_kbo_0430838564_1560,KBO Socius VZW 0430.838.564 (tick1560),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=430838564,FPS Economy KBO,2026-08-20,official_register,tick1560; leftover public koepel VZW of mined Flanders; KBO 0430.838.564 Actief official kbo-bce.fgov.be; naam Socius - Steunpunt Sociaal-Cultureel Werk sinds 16.10.2019; afkorting Socius sinds 11.10.2017; rechtsvorm VZW sinds 13.02.1986; KBO zetel Sainctelettesquare 19 1000 Brussel sinds 11.10.2017; 1 VE; RSZ-werkgever sinds 01.03.1985; aanbestedende overheid sinds 18.01.2003; prefix vzw_soci unused",
        "src_socius_foi_contact_1560,Socius FOI channel (debbie.bevers@socius.be / socius.be),https://www.socius.be/,Socius VZW,2026-08-20,official_web,tick1560; leftover public koepel VZW of mined Flanders; FOI ready not sent; JR PDF Sainctelettesquare 19 1000 Brussel; official KBO e-mail debbie.bevers@socius.be; current site socius.be; NOT leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_soci," in raw:
        raise SystemExit("vzw_soci already present")
    if "0430.838.564" in raw or "0430838564" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1560 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 so leftover Socius with live official CDN taken; leftover publiq 0475.250.609 also live unused (CDN 2026-00086529) deferred; KBO 0430.838.564 Actief official kbo-bce.fgov.be; naam Socius - Steunpunt Sociaal-Cultureel Werk sinds 16.10.2019; afkorting Socius sinds 11.10.2017; rechtsvorm VZW sinds 13.02.1986; KBO zetel Sainctelettesquare 19 1000 Brussel; RSZ-werkgever sinds 01.03.1985; aanbestedende overheid sinds 18.01.2003; live official NBB VKT-VZW deposit 2026-00065726 13p 50636; sourced euros assets 1356462 bruto 1380002 omzet empty 73 empty pers 1265278 vte 12.2 expl 91179 PROFIT pnl 103727 PROFIT beleg 1044949 cash 74193 mva JUMP 39032 lev DROP 70980; FOI ready not sent; parent sec_flanders; prefix vzw_soci unused; NOT leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland / leftover publiq unused live"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Socius / Steunpunt Sociaal-Cultureel Werk (leftover public koepel VZW of mined Flanders; NOT leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024),Point d appui du travail socio-culturel asbl (koepel residuel de la Flandre),Socius leftover public koepel socio-cultural support point of mined Flanders,other,sec_flanders,nl,https://www.socius.be/,debbie.bevers@socius.be,Sainctelettesquare 19 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_soci", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
