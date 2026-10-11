#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1494=done + spawn rq_1495; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:40:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1494,"):
        raise SystemExit(f"last row is not rq_1494: {last[:80]!r}")
    if b"rq_1495," in raw:
        raise SystemExit("rq_1495 already present — concurrent tick?")
    done = (
        "rq_1494,IJzer en Zee JR2025 leftover dual residual,hole_fill,5,done,L5,wm_ijez,"
        "Tick 1494 took leftover official-41 woonmaatschappij IJzer en Zee 0405.261.842 live official NBB WVV VOL-inb 2026-00171983 58p 970220; assets 182256295 omzet 17969403 pers 2550095 pnl 1773977 cash 13132132 debt 140520313; FOI ready not sent. Do NOT redo IJzer en Zee.,,"
        f"{TS},{TS},"
        "tick1494 IJzer en Zee leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00171983 58p 970220; assets 182256295 omzet 17969403 pers 2550095 pnl 1773977 cash 13132132 debt 140520313; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1495,Leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1495 after 1494 IJzer en Zee. Do NOT redo IJzer en Zee. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Woonstart 0405.220.963 / Meetjesland / de Thuisbouwer / Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen. Prefer VOL-inb over VKT. Confirm NOT already in entities. Next every-10 is 1500. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474).,,"
        f"{TS},{TS},"
        "spawned after tick1494 IJzer en Zee leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Woonstart 0405.220.963 / leftover Meetjesland / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1494=done + rq_1495 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T20:40:00Z,rq_1494,1494,no,"
        "tick1494 IJzer en Zee leftover woonmaatschappij residual; KBO 0405.261.842; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 182256295 omzet 17969403 pers 2550095 30.6 VTE pnl 1773977 equity 39032061 cash 13132132 debt 140520313 capex 15386690 dividend 0; FOI ready omzet 17.97m DROP / pers 2.55m 30.6 VTE / debt 140.52m DROP / cash 13.13m UP / beleggingen 5.00m JUMP / PnL 1.77m / dividend 0 / 2 VE; NOT leftover AGB Veurne / leftover Thuiswest 1493 / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover Zetus 1490 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1495 leftover APB Inovant/Atlas if PDF live else leftover Woonstart 0405.220.963 / leftover Meetjesland / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1137 answered 9 partial 27 total 1185; inventory budgets 42862 commitments 5094 leaderboard 7297 entities 1239 sources 3113; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1494")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1494_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
