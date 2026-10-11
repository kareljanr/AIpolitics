#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1561 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_pubq"
SRC = "src_publiq_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00086529.pdf"
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
        f"{SRC},publiq official NBB VKT-VZW JR2025 deposit 2026-00086529,{PDF},Nationale Bank van Belgie / publiq VZW,2026-08-20,budget,tick1561; official NBB WVV VKT-VZW PDF 14p / 51580 bytes; deposit 2026-00086529 Initial; model VKT-VZW 23.0.8 m04-f; AV 23.03.2026; year-end 31.12.2025; pdfinfo created 24.04.2026 09:04:31 UTC OpenPDF 1.3.26; euros PDF only; envelope brutomarge 9900 7291932 (leftover public koepel VZW; VKT and omzet 70 empty; not VLUHR 1555 omzet-envelope / not VLIR 1556 bedrijfsopbrengsten-envelope)",
        "src_publiq_nbb_consult,NBB consult publiq 0475250609 published deposit 2026-00086529,https://consult.cbso.nbb.be/consult-enterprise/0475250609,Nationale Bank van Belgie,2026-08-20,official_register,tick1561; leftover public koepel VZW of mined Flanders; official NBB consult enterprise page; official CDN 51580 bytes / 14p VKT-VZW",
        "src_publiq_kbo_0475250609_1561,KBO publiq VZW 0475.250.609 (tick1561),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=475250609,FPS Economy KBO,2026-08-20,official_register,tick1561; leftover public koepel VZW of mined Flanders; KBO 0475.250.609 Actief official kbo-bce.fgov.be; naam publiq sinds 28.03.2017; rechtsvorm VZW sinds 01.06.2001; KBO zetel Henegouwenkaai 41-43 1080 Sint-Jans-Molenbeek sinds 23.12.2016; 2 VE; RSZ-werkgever sinds 03.10.2001; aanbestedende overheid sinds 01.06.2001; prefix vzw_pubq unused",
        "src_publiq_foi_contact_1561,publiq FOI channel (info@publiq.be / publiq.be),https://www.publiq.be/,publiq VZW,2026-08-20,official_web,tick1561; leftover public koepel VZW of mined Flanders; FOI ready not sent; JR PDF Henegouwenkaai 62 1000 Brussel; official KBO zetel Henegouwenkaai 41-43 1080 Sint-Jans-Molenbeek; website e-mail info@publiq.be; KBO e-mail empty; NOT leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_pubq," in raw:
        raise SystemExit("vzw_pubq already present")
    if "0475.250.609" in raw.split("vzw_soci")[0] and False:
        pass
    # KBO may appear in Socius notes as deferred leftover — that is not an entity. Block only if an entity_id already owns it as identity.
    for line in raw.splitlines()[1:]:
        if not line.strip():
            continue
        eid = line.split(",", 1)[0]
        if eid != "vzw_soci" and ("0475.250.609" in line or "0475250609" in line):
            raise SystemExit(f"KBO already present on {eid}")
    notes = (
        "tick1561 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still no confirmed JR2025 so leftover publiq with live official CDN taken; leftover Socius 1560 TAKEN; KBO 0475.250.609 Actief official kbo-bce.fgov.be; naam publiq sinds 28.03.2017; rechtsvorm VZW sinds 01.06.2001; KBO zetel Henegouwenkaai 41-43 1080 Sint-Jans-Molenbeek; 2 VE; RSZ-werkgever sinds 03.10.2001; aanbestedende overheid sinds 01.06.2001; live official NBB VKT-VZW deposit 2026-00086529 14p 51580; sourced euros assets 4196794 bruto 7291932 omzet empty 73 empty pers 6493450 vte 81.2 expl 151937 PROFIT pnl 150686 PROFIT recv JUMP 2328518 beleg JUMP 267028 cash 862453 accrued JUMP 833654 onttrekking 827535; FOI ready not sent; parent sec_flanders; prefix vzw_pubq unused; NOT leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},publiq (leftover public koepel VZW / digital kernspeler of mined Flanders; NOT leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024),publiq asbl (koepel residuel digital de la Flandre),publiq leftover public koepel digital culture leisure platform of mined Flanders,other,sec_flanders,nl,https://www.publiq.be/,info@publiq.be,Henegouwenkaai 41-43 1080 Sint-Jans-Molenbeek,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_pubq", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
