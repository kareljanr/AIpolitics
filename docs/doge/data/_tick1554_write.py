#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1554 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vleva"
SRC = "src_vleva_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00075254.pdf"
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
        f"{SRC},VLEVA official NBB VKT-VZW JR2025 deposit 2026-00075254,{PDF},Nationale Bank van Belgie / VLEVA vzw,2026-08-20,budget,tick1554; official NBB WVV VKT-VZW PDF 23p / 444845 bytes; deposit 2026-00075254 Initial; model VKT-VZW 26.0.8 m04-f; AV 26.03.2026; year-end 31.12.2025; pdfinfo created 09.04.2026 07:39:36 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 1077899 (leftover public koepel VZW; VKT and omzet 70 empty; not VVSG bedrijfsopbrengsten-envelope)",
        "src_vleva_nbb_consult,NBB consult VLEVA 0880913715 published deposit 2026-00075254,https://consult.cbso.nbb.be/consult-enterprise/0880913715,Nationale Bank van Belgie,2026-08-20,official_register,tick1554; leftover public koepel VZW of mined Flanders; official NBB consult enterprise page; official CDN 444845 bytes / 23p VKT-VZW",
        "src_vleva_kbo_0880913715_1554,KBO VLEVA vzw 0880.913.715 (tick1554),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=880913715,FPS Economy KBO,2026-08-20,official_register,tick1554; leftover public koepel VZW of mined Flanders; KBO 0880.913.715 Actief official kbo-bce.fgov.be; zetel Aarlenstraat 80 1000 Brussel sinds 25.06.2021; afkorting vleva sinds 05.05.2008; prefix vzw_vleva unused",
        "src_vleva_foi_contact_1554,VLEVA FOI channel (info@vleva.eu),https://vleva.eu,VLEVA vzw,2026-08-20,official_web,tick1554; leftover public koepel VZW of mined Flanders; FOI ready not sent; Aarlenstraat 80 1000 Brussel; official e-mail info@vleva.eu; NOT leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_vleva," in raw:
        raise SystemExit("vzw_vleva already present")
    if "0880.913.715" in raw or "0880913715" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1554 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0880.913.715 Actief official kbo-bce.fgov.be; zetel Aarlenstraat 80 1000 Brussel sinds 25.06.2021; live official NBB VKT-VZW deposit 2026-00075254 23p 444845; sourced euros assets 433039 bruto 1077899 omzet empty 73 empty pers 1021920 vte 8.8 expl -54822 LOSS pnl -56289 LOSS cash 104066 DROP va 262987 DROP lev 20596 JUMP; FOI ready not sent; parent sec_flanders; prefix vzw_vleva unused; NOT leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand / leftover Zuidrand"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Vlaams-Europees Verbindingsagentschap VLEVA (leftover public koepel VZW of mined Flanders; NOT leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551),Agence de liaison Flandre-Europe ASBL (koepel residuel de la Flandre),Flanders-Europe Liaison Agency leftover public koepel VZW of mined Flanders,other,sec_flanders,nl,https://vleva.eu,info@vleva.eu,Aarlenstraat 80 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_vleva", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
