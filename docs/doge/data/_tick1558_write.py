#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1558 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_meem"
SRC = "src_meemoo_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00090751.pdf"
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
        f"{SRC},meemoo official NBB VKT-VZW JR2025 deposit 2026-00090751,{PDF},Nationale Bank van Belgie / meemoo VZW,2026-08-20,budget,tick1558; official NBB WVV VKT-VZW PDF 24p / 1217241 bytes; deposit 2026-00090751 Initial; model VKT-VZW 23.0.8 m04-f; AV 23.04.2026; year-end 31.12.2025; pdfinfo created 28.04.2026 16:53:57 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 5412745 (leftover public koepel VZW; VKT and omzet 70 empty; not VLUHR 1555 omzet-envelope / not VLIR 1556 bedrijfsopbrengsten-envelope)",
        "src_meemoo_nbb_consult,NBB consult meemoo 0644450380 published deposit 2026-00090751,https://consult.cbso.nbb.be/consult-enterprise/0644450380,Nationale Bank van Belgie,2026-08-20,official_register,tick1558; leftover public koepel VZW of mined Flanders; official NBB consult enterprise page; official CDN 1217241 bytes / 24p VKT-VZW",
        "src_meemoo_kbo_0644450380_1558,KBO meemoo VZW 0644.450.380 (tick1558),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=644450380,FPS Economy KBO,2026-08-20,official_register,tick1558; leftover public koepel VZW of mined Flanders; KBO 0644.450.380 Actief official kbo-bce.fgov.be; naam meemoo Vlaams instituut voor het archief; afkorting meemoo sinds 02.09.2020; rechtsvorm VZW sinds 11.12.2015; KBO zetel Ham 175 9000 Gent; 1 VE; aanbestedende overheid sinds 11.12.2015; prefix vzw_meem unused",
        "src_meemoo_foi_contact_1558,meemoo FOI channel (info@meemoo.be / contact form),https://meemoo.be,meemoo VZW,2026-08-20,official_web,tick1558; leftover public koepel VZW of mined Flanders; FOI ready not sent; JR PDF Ham 175 9000 Gent; historic official e-mail info@meemoo.be; current site meemoo.be; NOT leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover FARO still JR2024",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_meem," in raw:
        raise SystemExit("vzw_meem already present")
    if "0644.450.380" in raw or "0644450380" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1558 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0644.450.380 Actief official kbo-bce.fgov.be; naam meemoo Vlaams instituut voor het archief; afkorting meemoo sinds 02.09.2020; rechtsvorm VZW sinds 11.12.2015; KBO zetel Ham 175 9000 Gent; aanbestedende overheid sinds 11.12.2015; live official NBB VKT-VZW deposit 2026-00090751 24p 1217241; sourced euros assets 3435584 bruto 5412745 omzet empty 73 empty pers 4927717 vte 64.9 expl -4546 LOSS pnl 11551 PROFIT cash DROP 994688 lev JUMP 1076339 accrued DROP 970841 otherrecv 1209119; FOI ready not sent; parent sec_flanders; prefix vzw_meem unused; NOT leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},meemoo Vlaams instituut voor het archief (leftover public koepel VZW of mined Flanders; NOT leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover FARO still JR2024),Institut flamand des archives asbl (koepel residuel de la Flandre),Flemish Institute for the Archive leftover public koepel non-profit of mined Flanders,other,sec_flanders,nl,https://meemoo.be,info@meemoo.be,Ham 175 9000 Gent,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_meem", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
