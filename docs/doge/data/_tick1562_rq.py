#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1562=done + spawn rq_1563. NEVER rewrite whole research_queue.csv."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T08:07:13Z"
p = DATA / "research_queue.csv"
raw = p.read_bytes()
if not raw.endswith(b"\n"):
    raw += b"\n"
idx = raw.rfind(b"\n", 0, len(raw)-1)
last = raw[idx+1:]
if not last.startswith(b"rq_1562,"):
    raise SystemExit(f"last row is not rq_1562: {last[:80]!r}")
if b"rq_1563," in raw:
    raise SystemExit("rq_1563 already present — concurrent tick?")
done = (
    "rq_1562,Cultuurconnect JR2025 leftover public koepel dual residual,hole_fill,5,done,L5,vzw_cult,"
    "Tick 1562 took leftover public koepel Cultuurconnect 0629.858.909 live official NBB VOL-VZW deposit 2026-00072195 50p 655018; opbr 12751502 omzet 5026615 commercial-only 73 7718118 pers 5184352 vte 51 expl LOSS 1090651 pnl LOSS 1049404 assets 6483521 cash DROP 5103622 60 8128810 onttrekking 2814680; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick so leftover public koepel with live official JR2025 euros taken. Leftover FARO still JR2024 so leftover Cultuurconnect taken. Official KBO resolved on kbo-bce.fgov.be. Do NOT redo Cultuurconnect. Do NOT redo publiq. Do NOT redo Socius. Do NOT redo Kunstensteunpunt. Do NOT redo meemoo. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo taken HVZ 1537-1547. Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1563 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover FARO if JR2025 now else leftover OP-TIL/VI.BE if unused live JR2025 else leftover other HVZ/IGS of mined cities. Next every-10 is 1570.,,"
    f"{TS},{TS},"
    "tick1562 Cultuurconnect leftover public koepel residual; official NBB VOL-VZW 50p 655018; KBO 0629.858.909 official; opbr 12751502 pers 5184352 expl LOSS 1090651 cash DROP 5103622 60 8128810 onttrekking 2814680; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished; leftover FARO still JR2024; leftover VI.BE CDN live unused deferred; leftover OP-TIL unused not confirmed JR2025; next 1563 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover FARO if JR2025 now else leftover OP-TIL/VI.BE if unused live else leftover other HVZ/IGS; next every-10 is 1570\n"
)
spawn = (
    "rq_1563,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
    "Tick 1563 after 1562 Cultuurconnect. Next every-10 is 1570. Official 11-CAW vein fully exhausted. Live-PDF CGG vein fully exhausted. Official-41 woonmaatschappijen fully exhausted. Do NOT redo Cultuurconnect. Do NOT redo publiq. Do NOT redo Socius. Do NOT redo Kunstensteunpunt. Do NOT redo meemoo. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB. Do NOT redo Erfpunt. Do NOT redo Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA. Leftover AGB/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Bosgroep if 2025 CDN now. Leftover Dijk92 0806.383.071 deposit 2026-00377886 if CDN now 200. Leftover other IOED if 2025 CDN now. Leftover Cultuur Noordrand 0740.822.256 unused leftover of mined Grimbergen but no NBB JR2025 as of 1562. Leftover Zuidrand 0672.985.901 unused leftover of mined Mortsel/Kontich but no NBB JR2025 as of 1562. Leftover IOED Zuid-Hageland 0680.814.294 unused leftover of mined Landen/Zoutleeuw/Geetbets/Kortenaken but no NBB JR2025 as of 1562. Leftover FARO 0893.863.017 unused leftover public koepel of mined Flanders but still JR2024 as of 1562. Leftover OP-TIL / leftover VI.BE 0474.500.442 CDN 2026-00064426 live unused as of 1562 — take only if unused leftover + live JR2025. Leftover other HVZ of mined cities if official JR2025 PDF with extractable euros now. Else leftover other IGS/IOED/other public unit of a mined parent with live 2025 statutory/BBC/AV PDF with euros.,,"
    f"{TS},{TS},"
    "spawned after tick1562 leftover Cultuurconnect JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN 200 / leftover FARO if JR2025 now / leftover OP-TIL/VI.BE if unused live / leftover other HVZ if euros now live / leftover other IGS of mined cities; do NOT redo Cultuurconnect / publiq / Socius / Kunstensteunpunt / meemoo / VLHORA / VLIR / VLUHR / VLEVA / VVP / VVSG / Inagro / CREMABRU / Intradura / Brandweerzone Oost OVL / taken HVZ 1537-1547 / Erfpunt / 11-CAW / CGG / official-41 / Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA; next every-10 is 1570\n"
)
for label, row in (("done", done), ("spawn", spawn)):
    n = len(next(csv.reader(io.StringIO(row))))
    if n != 12:
        raise SystemExit(f"{label} ncols {n} != 12")
    fields = next(csv.reader(io.StringIO(row)))
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
before = len(raw)
p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
after = p.stat().st_size
if after < 60_000_000:
    raise SystemExit(f"research_queue shrank unexpectedly {before} -> {after}")
print("research_queue surgical rq_1562=done + rq_1563 spawn", before, "->", after)
