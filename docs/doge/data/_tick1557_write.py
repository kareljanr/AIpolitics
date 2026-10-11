#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1557 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlho"
SRC = "src_vlhora_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00079599.pdf"
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
        f"{SRC},VLHORA official NBB VKT-VZW JR2025 deposit 2026-00079599,{PDF},Nationale Bank van Belgie / VLHORA SON,2026-08-20,budget,tick1557; official NBB WVV VKT-VZW PDF 25p / 246879 bytes; deposit 2026-00079599 Initial; model VKT-VZW 26.0.8 m04-f; AV 27.03.2026; year-end 31.12.2025; pdfinfo created 15.04.2026 06:17:59 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 1200770 (leftover public koepel SON; VKT and omzet 70 empty; not VLUHR 1555 omzet-envelope / not VLIR 1556 bedrijfsopbrengsten-envelope)",
        "src_vlhora_nbb_consult,NBB consult VLHORA 0650536537 published deposit 2026-00079599,https://consult.cbso.nbb.be/consult-enterprise/0650536537,Nationale Bank van Belgie,2026-08-20,official_register,tick1557; leftover public koepel SON of mined Flanders; official NBB consult enterprise page; official CDN 246879 bytes / 25p VKT-VZW",
        "src_vlhora_kbo_0650536537_1557,KBO VLHORA SON 0650.536.537 (tick1557),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=650536537,FPS Economy KBO,2026-08-20,official_register,tick1557; leftover public koepel SON of mined Flanders; KBO 0650.536.537 Actief official kbo-bce.fgov.be; naam Vlaamse Hogescholenraad; afkorting VLHORA sinds 10.12.2015; rechtsvorm Stichting van openbaar nut sinds 10.12.2015; KBO zetel Ravensteingalerij 27 bus 3 1000 Brussel; JR PDF zetel Sinter-Goedeleplein 14 1000 Brussel; prefix son_vlho unused",
        "src_vlhora_foi_contact_1557,VLHORA FOI channel (info@vlhora.be / contact form),https://www.vlaamsehogescholenraad.be,VLHORA SON,2026-08-20,official_web,tick1557; leftover public koepel SON of mined Flanders; FOI ready not sent; JR PDF Sinter-Goedeleplein 14 1000 Brussel; KBO still Ravensteingalerij 27 bus 3; historic official e-mail info@vlhora.be; current site contact form +32 2 211 10 00; NOT leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "son_vlho," in raw:
        raise SystemExit("son_vlho already present")
    if "0650.536.537" in raw or "0650536537" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1557 leftover public koepel SON residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0650.536.537 Actief official kbo-bce.fgov.be; naam Vlaamse Hogescholenraad; afkorting VLHORA; rechtsvorm Stichting van openbaar nut sinds 10.12.2015; KBO zetel Ravensteingalerij 27 bus 3 1000 Brussel; JR PDF zetel Sinter-Goedeleplein 14 1000 Brussel; live official NBB VKT-VZW deposit 2026-00079599 25p 246879; sourced euros assets 11929249 bruto 1200770 omzet empty 73 empty pers 1052307 vte 13.2 expl 144241 PROFIT pnl 143093 PROFIT handelsrecv JUMP 7665740 vooruit JUMP 9370719 cash DROP 2972417 lev DROP 439394; FOI ready not sent; parent sec_flanders; prefix son_vlho unused; NOT leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Vlaamse Hogescholenraad VLHORA (leftover public koepel SON of mined Flanders; NOT leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552),Conseil flamand des hautes ecoles fondation d utilite publique (koepel residuel de la Flandre),Flemish Council of Universities of Applied Sciences leftover public koepel public-utility foundation of mined Flanders,other,sec_flanders,nl,https://www.vlaamsehogescholenraad.be,info@vlhora.be,Sinter-Goedeleplein 14 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 son_vlho", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
