#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1550=done + spawn rq_1551; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io, subprocess

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1550,"):
        raise SystemExit(f"last row is not rq_1550: {last[:80]!r}")
    if b"rq_1551," in raw:
        raise SystemExit("rq_1551 already present — concurrent tick?")
    done = (
        "rq_1550,CREMABRU JR2025 leftover IGS dual residual,hole_fill,5,done,L5,igs_crbr,"
        "Tick 1550 took leftover IGS crematorium CREMABRU 0203.389.204 live official NBB C-cap deposit 2026-00178051 49p 1261272; omzet 4531359 opbr 4645123 pers 2583529 vte 31.8 expl -270295 LOSS pnl -216386 LOSS assets 12679309 beleg 888671 JUMP kapsubs 3023908 JUMP; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick so leftover IGS with live official JR2025 euros taken. Official KBO resolved on kbo-bce.fgov.be. EVERY-10 refresh done. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo taken HVZ 1537-1547. Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1551 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover other HVZ of mined cities if a 2025 official PDF with euros now downloads else leftover other IGS of mined cities. Next every-10 is 1560.,,"
        f"{TS},{TS},"
        "tick1550 CREMABRU leftover IGS residual; official NBB C-cap 49p 1261272; KBO 0203.389.204 official; omzet 4531359 pers 2583529 expl LOSS 270295; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished; EVERY-10 refresh done; next 1551 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover other HVZ/IGS; next every-10 is 1560\n"
    )
    spawn = (
        "rq_1551,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1551 after 1550 CREMABRU. Official 11-CAW vein fully exhausted. Live-PDF CGG vein fully exhausted. Official-41 woonmaatschappijen fully exhausted. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB. Do NOT redo Erfpunt. Do NOT redo Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA. Leftover AGB/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Bosgroep if 2025 CDN now. Leftover Dijk92 0806.383.071 deposit 2026-00377886 if CDN now 200. Leftover other IOED if 2025 CDN now. Leftover other HVZ of mined cities if official JR2025 PDF with extractable euros now (Rivierenland/Waasland/Centrum/Oost-Limburg/Rand/VB West/Zuid-Oost still no extractable euros as of 1550). Else leftover other IGS/IOED/other public unit of a mined parent with live 2025 statutory/BBC/AV PDF with euros. Next every-10 is 1560.,,"
        f"{TS},{TS},"
        "spawned after tick1550 leftover CREMABRU JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN 200 / leftover other HVZ if euros now live / leftover other IGS of mined cities; do NOT redo CREMABRU / Intradura / Brandweerzone Oost OVL / taken HVZ 1537-1547 / Erfpunt / 11-CAW / CGG / official-41 / Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA; next every-10 is 1560\n"
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
    print("research_queue surgical rq_1550=done + rq_1551 spawn", before, "->", after)

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1550 leftover IGS CREMABRU residual; KBO 0203.389.204 official kbo-bce.fgov.be; live official NBB C-cap deposit 2026-00178051 49p 1261272; sourced euros assets 12679309 omzet 4531359 opbr 4645123 pers 2583529 vte 31.8 expl -270295 LOSS pnl -216386 LOSS cash 258846 UP beleg 888671 JUMP kapsubs 3023908 JUMP; FOI ready per-gemeente split / beleg JUMP / kapsubs JUMP / expl LOSS / commissaris extra 14k / AV notulen; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover IGS with live official JR2025 euros taken; leftover Dijk92 deposit 2026-00377886 still CDN 403; leftover Rivierenland still inzage-only; leftover Waasland/Centrum/Rand/VB West/Oost-Limburg/Zuid-Oost still no euros; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; NOT leftover Haviland crematorium / leftover Westlede / leftover Hofheide / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505; EVERY-10 refresh done; next rq_1551 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover other HVZ if official JR2025 with euros now live / leftover other IGS; next every-10 is 1560; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1550,1550,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1550", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1550_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
