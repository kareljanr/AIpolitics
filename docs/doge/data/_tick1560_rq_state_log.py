#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1560=done + spawn rq_1561; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1560,"):
        raise SystemExit(f"last row is not rq_1560: {last[:80]!r}")
    if b"rq_1561," in raw:
        raise SystemExit("rq_1561 already present — concurrent tick?")
    done = (
        "rq_1560,Socius JR2025 leftover public koepel dual residual PLUS every-10 refresh,hole_fill,5,done,L5,vzw_soci,"
        "Tick 1560 took leftover public koepel Socius 0430.838.564 live official NBB VKT-VZW deposit 2026-00065726 13p 50636; bruto 1380002 omzet empty 73 empty pers 1265278 vte 12.2 expl 91179 PROFIT pnl 103727 PROFIT assets 1356462 beleg 1044949 cash 74193 mva JUMP 39032 lev DROP 70980; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick so leftover public koepel with live official JR2025 euros taken. Leftover FARO still JR2024 so leftover Socius taken. Leftover publiq 0475.250.609 also live unused deferred. Official KBO resolved on kbo-bce.fgov.be. EVERY-10 refresh done (progress_every_10_ticks.md + doge_waste_top10_current.md). Do NOT redo Socius. Do NOT redo Kunstensteunpunt. Do NOT redo meemoo. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo taken HVZ 1537-1547. Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1561 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover FARO if JR2025 now else leftover publiq if unused else leftover other HVZ/IGS of mined cities. Next every-10 is 1570.,,"
        f"{TS},{TS},"
        "tick1560 Socius leftover public koepel residual PLUS every-10; official NBB VKT-VZW 13p 50636; KBO 0430.838.564 official; bruto 1380002 pers 1265278 expl PROFIT 91179 beleg 1044949 mva JUMP 39032; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished; leftover FARO still JR2024; leftover publiq unused live deferred; next 1561 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover FARO if JR2025 now else leftover publiq if unused else leftover other HVZ/IGS; next every-10 is 1570\n"
    )
    spawn = (
        "rq_1561,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1561 after 1560 Socius + every-10 refresh. Next every-10 is 1570. Official 11-CAW vein fully exhausted. Live-PDF CGG vein fully exhausted. Official-41 woonmaatschappijen fully exhausted. Do NOT redo Socius. Do NOT redo Kunstensteunpunt. Do NOT redo meemoo. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB. Do NOT redo Erfpunt. Do NOT redo Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA. Leftover AGB/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Bosgroep if 2025 CDN now. Leftover Dijk92 0806.383.071 deposit 2026-00377886 if CDN now 200. Leftover other IOED if 2025 CDN now. Leftover Cultuur Noordrand 0740.822.256 unused leftover of mined Grimbergen but no NBB JR2025 as of 1560. Leftover Zuidrand 0672.985.901 unused leftover of mined Mortsel/Kontich but no NBB JR2025 as of 1560. Leftover IOED Zuid-Hageland 0680.814.294 unused leftover of mined Landen/Zoutleeuw/Geetbets/Kortenaken but no NBB JR2025 as of 1560. Leftover FARO 0893.863.017 unused leftover public koepel of mined Flanders but still JR2024 as of 1560. Leftover publiq 0475.250.609 unused leftover public digital kernspeler with live official CDN 2026-00086529 as of 1560. Leftover other HVZ of mined cities if official JR2025 PDF with extractable euros now. Else leftover other IGS/IOED/other public unit of a mined parent with live 2025 statutory/BBC/AV PDF with euros.,,"
        f"{TS},{TS},"
        "spawned after tick1560 leftover Socius JR2025 + every-10; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN 200 / leftover FARO if JR2025 now / leftover publiq 0475.250.609 if unused / leftover other HVZ if euros now live / leftover other IGS of mined cities; do NOT redo Socius / Kunstensteunpunt / meemoo / VLHORA / VLIR / VLUHR / VLEVA / VVP / VVSG / Inagro / CREMABRU / Intradura / Brandweerzone Oost OVL / taken HVZ 1537-1547 / Erfpunt / 11-CAW / CGG / official-41 / Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA; next every-10 is 1570\n"
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
    print("research_queue surgical rq_1560=done + rq_1561 spawn", before, "->", after)

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1560 leftover public koepel Socius residual PLUS every-10; KBO 0430.838.564 official kbo-bce.fgov.be; live official NBB VKT-VZW deposit 2026-00065726 13p 50636; sourced euros assets 1356462 bruto 1380002 omzet empty 73 empty pers 1265278 vte 12.2 expl 91179 PROFIT pnl 103727 PROFIT beleg 1044949 cash 74193 mva JUMP 39032 lev DROP 70980; FOI ready 73/70/60/61 unpublished VKT / beleg 1.04m / MVA JUMP / lev DROP / other ST JUMP / commissaris unpublished / AV notulen; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official JR2025 euros taken; leftover FARO still JR2024 so leftover Socius taken; leftover publiq 0475.250.609 also live unused deferred; leftover Dijk92 deposit 2026-00377886 still CDN 403; leftover Cultuur Noordrand 0740.822.256 unused leftover of mined Grimbergen but no NBB JR2025; leftover Zuidrand 0672.985.901 unused leftover of mined Mortsel/Kontich but no NBB JR2025; leftover IOED Zuid-Hageland 0680.814.294 unused leftover of mined Landen/Zoutleeuw/Geetbets/Kortenaken but no NBB JR2025; leftover FARO 0893.863.017 unused leftover public koepel but still JR2024; leftover remaining HVZ still inzage-only; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; EVERY-10 refresh done (progress_every_10_ticks.md + doge_waste_top10_current.md); next every-10 is 1570; NOT leftover Kunstensteunpunt 1559 / leftover meemoo 1558 / leftover VLHORA 1557 / leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505; next rq_1561 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover FARO if JR2025 now / leftover publiq if unused / leftover other HVZ if official JR2025 with euros now live / leftover other IGS; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1560,1560,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1560", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1560_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
