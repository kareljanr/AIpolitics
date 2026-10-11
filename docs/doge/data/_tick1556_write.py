#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1556 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlir"
SRC = "src_vlir_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072863.pdf"
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
        f"{SRC},VLIR official NBB VOL-VZW JR2025 deposit 2026-00072863,{PDF},Nationale Bank van Belgie / VLIR SON,2026-08-20,budget,tick1556; official NBB WVV VOL-VZW PDF 44p / 475000 bytes; deposit 2026-00072863 Initial; model VOL-VZW 25.0.10 m05-f; AV 27.03.2026; year-end 31.12.2025; pdfinfo created 07.04.2026 07:27:15 UTC OpenPDF 1.3.26; euros PDF only; envelope bedrijfsopbrengsten 70/76A 36809788 (leftover public koepel SON; omzet 70 present but commercial-only 1742031 vs 73 subsidies 34095480; Inagro 1551 / VVSG 1552 pattern not VLUHR 1555 omzet-envelope)",
        "src_vlir_nbb_consult,NBB consult VLIR 0418766123 published deposit 2026-00072863,https://consult.cbso.nbb.be/consult-enterprise/0418766123,Nationale Bank van Belgie,2026-08-20,official_register,tick1556; leftover public koepel SON of mined Flanders; official NBB consult enterprise page; official CDN 475000 bytes / 44p VOL-VZW",
        "src_vlir_kbo_0418766123_1556,KBO VLIR SON 0418.766.123 (tick1556),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=418766123,FPS Economy KBO,2026-08-20,official_register,tick1556; leftover public koepel SON of mined Flanders; KBO 0418.766.123 Actief official kbo-bce.fgov.be; zetel Sinter-Goedeleplein 14 1000 Brussel sinds 01.01.2026; rechtsvorm Stichting van openbaar nut sinds 13.12.2005; aanbestedende overheid; prefix son_vlir unused",
        "src_vlir_foi_contact_1556,VLIR FOI channel (administratie@vlir.be),https://vlir.be/contact/,VLIR SON,2026-08-20,official_web,tick1556; leftover public koepel SON of mined Flanders; FOI ready not sent; Sinter-Goedeleplein 14 1000 Brussel; official e-mail administratie@vlir.be; NOT leftover VLUHR 1555 / leftover VLHORA / leftover VLEVA 1554",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "son_vlir," in raw:
        raise SystemExit("son_vlir already present")
    if "0418.766.123" in raw or "0418766123" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1556 leftover public koepel SON residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0418.766.123 Actief official kbo-bce.fgov.be; zetel Sinter-Goedeleplein 14 1000 Brussel sinds 01.01.2026; live official NBB VOL-VZW deposit 2026-00072863 44p 475000; sourced euros assets 20061015 opbr 36809788 omzet 1742031 subsid 34095480 pers 4013097 vte 37.9 expl 60746 PROFIT pnl 312676 PROFIT cash 4929904 JUMP beleg 9092658 DROP vooruit 15996948 othercosts 30005208 JUMP; FOI ready not sent; parent sec_flanders; prefix son_vlir unused; NOT leftover VLUHR 1555 / leftover VLHORA / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Vlaamse Interuniversitaire Raad VLIR (leftover public koepel SON of mined Flanders; NOT leftover VLUHR 1555 / leftover VLHORA / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552),Conseil interuniversitaire flamand fondation d utilite publique (koepel residuel de la Flandre),Flemish Interuniversity Council leftover public koepel public-utility foundation of mined Flanders,other,sec_flanders,nl,https://vlir.be,administratie@vlir.be,Sinter-Goedeleplein 14 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 son_vlir", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
