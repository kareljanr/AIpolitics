#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1553 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_vvp"
SRC = "src_vvp_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00138938.pdf"
GAP = "gap_vvp_bruto_0_59m_pers_0_56m_mva_jump_l5"
LB = "lb_vvp_bruto_0_59m_pers_0_56m_mva_jump"
COMM = "comm_vvp_jr2025_bruto"
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
        f"{SRC},VVP official NBB VKT-VZW JR2025 deposit 2026-00138938,{PDF},Nationale Bank van Belgie / VVP vzw,2026-08-20,budget,tick1553; official NBB WVV VKT-VZW PDF 25p / 180069 bytes; deposit 2026-00138938 Initial; model VKT-VZW 26.0.12 m04-f; AV 08.05.2026; year-end 31.12.2025; pdfinfo created 05.06.2026 07:42:27 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 589640 (leftover public koepel VZW; VKT and omzet 70 empty; not VVSG bedrijfsopbrengsten-envelope)",
        "src_vvp_nbb_consult,NBB consult VVP 0445212083 published deposit 2026-00138938,https://consult.cbso.nbb.be/consult-enterprise/0445212083,Nationale Bank van Belgie,2026-08-20,official_register,tick1553; leftover public koepel VZW of mined Flemish provinces; official NBB consult enterprise page; official CDN 180069 bytes / 25p VKT-VZW",
        "src_vvp_kbo_0445212083_1553,KBO VVP vzw 0445.212.083 (tick1553),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=445212083,FPS Economy KBO,2026-08-20,official_register,tick1553; leftover public koepel VZW of mined Flemish provinces; KBO 0445.212.083 Actief official kbo-bce.fgov.be; zetel Groendreef 1 1000 Brussel sinds 08.05.2026; JR/website still Picardstraat 7 bus 100; prefix vzw_vvp unused",
        "src_vvp_foi_contact_1553,VVP FOI channel (info@vlaamseprovincies.be),https://vlaamseprovincies.be,VVP vzw,2026-08-20,official_web,tick1553; leftover public koepel VZW of mined Flemish provinces; FOI ready not sent; Groendreef 1 1000 Brussel; official e-mail info@vlaamseprovincies.be; NOT leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_vvp," in raw:
        raise SystemExit("vzw_vvp already present")
    if "0445.212.083" in raw or "0445212083" in raw:
        raise SystemExit("KBO already present")
    notes = (
        "tick1553 leftover public koepel VZW residual of mined Flemish provinces after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; KBO 0445.212.083 Actief official kbo-bce.fgov.be; zetel Groendreef 1 1000 Brussel sinds 08.05.2026; JR Picardstraat 7 bus 100; live official NBB VKT-VZW deposit 2026-00138938 25p 180069; sourced euros assets 3412677 bruto 589640 omzet empty 73 empty pers 558980 vte 6.8 expl -6198 LOSS pnl -10588 LOSS cash 2256569 DROP mva 582447 JUMP lev 95590 JUMP; FOI ready not sent; parent sec_flanders; prefix vzw_vvp unused; NOT leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover Cultuur Noordrand"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Vereniging van de Vlaamse Provincies V.V.P. (leftover public koepel VZW of mined Flemish provinces; NOT leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549),Association des Provinces flamandes ASBL (koepel residuel des provinces flamandes),Association of Flemish Provinces leftover public koepel VZW of mined Flemish provinces,other,sec_flanders,nl,https://vlaamseprovincies.be,info@vlaamseprovincies.be,Groendreef 1 1000 Brussel,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_vvp", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
