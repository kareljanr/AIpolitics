#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1562 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, io, sys, subprocess
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_cult"
SRC = "src_cultuurconnect_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00072195.pdf"
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
        f"{SRC},Cultuurconnect official NBB VOL-VZW JR2025 deposit 2026-00072195,{PDF},Nationale Bank van Belgie / Cultuurconnect VZW,2026-08-20,budget,tick1562; official NBB WVV VOL-VZW PDF 50p / 655018 bytes; deposit 2026-00072195 Initial; model VOL-VZW 26.0.9 m05-f; AV 26.03.2026; year-end 31.12.2025; pdfinfo created 03.04.2026 14:17:25 UTC OpenPDF 1.3.26; euros PDF only; envelope bedrijfsopbrengsten 70/76A 12751502 (leftover public koepel VZW; omzet 70 present but commercial-only 5026615 vs 73 subsidies 7718118; Inagro 1551 / VVSG 1552 / VLIR 1556 pattern not VLUHR 1555 omzet-envelope / not publiq 1561 bruto-empty)",
        "src_cultuurconnect_nbb_consult,NBB consult Cultuurconnect 0629858909 published deposit 2026-00072195,https://consult.cbso.nbb.be/consult-enterprise/0629858909,Nationale Bank van Belgie,2026-08-20,official_register,tick1562; leftover public koepel VZW / Flanders digital culture steunpunt of mined Flanders; official NBB consult enterprise page; official CDN 655018 bytes / 50p VOL-VZW",
        "src_cultuurconnect_kbo_0629858909_1562,KBO Cultuurconnect VZW 0629.858.909 (tick1562),https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0629858909,FPS Economy KBO,2026-08-20,official_register,tick1562; leftover public koepel VZW of mined Flanders; KBO 0629.858.909 Actief official kbo-bce.fgov.be; naam Cultuurconnect sinds 22.06.2016; rechtsvorm VZW sinds 07.05.2015; KBO zetel Miriam Makebaplein 1 9000 Gent sinds 01.01.2024; 1 VE; RSZ-werkgever sinds 01.07.2016; BTW sinds 01.07.2016; aanbestedende overheid sinds 07.05.2015; BIBNET 0472.863.518 and Locus 0476.563.077 absorbed 22.08.2016; prefix vzw_cult unused",
        "src_cultuurconnect_foi_contact_1562,Cultuurconnect FOI channel (servicedesk@cultuurconnect.be / cultuurconnect.be),https://www.cultuurconnect.be/gebruiksvoorwaarden,Cultuurconnect VZW,2026-08-20,official_web,tick1562; leftover public koepel VZW of mined Flanders; FOI ready not sent; JR/KBO zetel Miriam Makebaplein 1 9000 Gent; official gebruiksvoorwaarden e-mail servicedesk@cultuurconnect.be; KBO e-mail empty; NOT leftover publiq 1561 / leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024 / leftover OP-TIL / leftover VI.BE",
    ]
    for r in rows:
        check(r, 7, "sources")
    append_lf(DATA / "sources.csv", rows)
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_text(encoding="utf-8")
    if "vzw_cult," in raw:
        raise SystemExit("vzw_cult already present")
    for line in raw.splitlines()[1:]:
        if not line.strip():
            continue
        eid = line.split(",", 1)[0]
        if "0629.858.909" in line or "0629858909" in line:
            raise SystemExit(f"KBO already present on {eid}")
    notes = (
        "tick1562 leftover public koepel VZW residual of mined Flanders after leftover AGB/APB/Bosgroep/IOED/Dijk92/remaining-HVZ hunt; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official NBB JR2025 euros taken; leftover FARO still JR2024 (SBM last 2024-12-31 / neerlegging 2025-11-24) so leftover Cultuurconnect with live official CDN taken; leftover publiq 1561 TAKEN; leftover Socius 1560 TAKEN; leftover VI.BE 0474.500.442 CDN 2026-00064426 live unused deferred; leftover OP-TIL 0712.776.586 unused not confirmed JR2025 this tick; KBO 0629.858.909 Actief official kbo-bce.fgov.be; naam Cultuurconnect sinds 22.06.2016; rechtsvorm VZW sinds 07.05.2015; KBO zetel Miriam Makebaplein 1 9000 Gent; 1 VE; RSZ-werkgever sinds 01.07.2016; aanbestedende overheid sinds 07.05.2015; live official NBB VOL-VZW deposit 2026-00072195 50p 655018; sourced euros assets 6483521 opbr 12751502 omzet 5026615 commercial-only 73 7718118 pers 5184352 vte 51 expl 1090651 LOSS pnl 1049404 LOSS cash DROP 5103622 60 8128810 onttrekking 2814680; FOI ready not sent; parent sec_flanders; prefix vzw_cult unused; NOT leftover publiq 1561 / leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover IVAREM 1524 / leftover FARO still JR2024 / leftover Cultuur Noordrand / leftover Zuidrand / leftover IOED Zuid-Hageland / leftover OP-TIL / leftover VI.BE"
    )
    if "," in notes:
        raise SystemExit("entity notes contain comma")
    row = (
        f"{ENT},Cultuurconnect (leftover public koepel VZW / Flanders digital culture steunpunt of mined Flanders; NOT leftover publiq 1561 / leftover Socius 1560 / leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover FARO still JR2024 / leftover OP-TIL / leftover VI.BE),Cultuurconnect asbl (koepel residuel digital culture Flandre),Cultuurconnect leftover public koepel digital culture libraries theatres platform of mined Flanders,other,sec_flanders,nl,https://www.cultuurconnect.be/,servicedesk@cultuurconnect.be,Miriam Makebaplein 1 9000 Gent,{notes}"
    )
    check(row, 11, "entities")
    before = pth.stat().st_size
    append_lf(pth, [row])
    after = pth.stat().st_size
    if after < before:
        raise SystemExit(f"entities shrank {before} -> {after}")
    print("entities +1 vzw_cult", before, "->", after)

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
