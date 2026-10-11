#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1493=done + spawn rq_1494; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T20:20:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1493,"):
        raise SystemExit(f"last row is not rq_1493: {last[:80]!r}")
    if b"rq_1494," in raw:
        raise SystemExit("rq_1494 already present — concurrent tick?")
    done = (
        "rq_1493,Thuiswest JR2025 leftover dual residual,hole_fill,5,done,L5,wm_thws,"
        "Tick 1493 took leftover official-41 woonmaatschappij Thuiswest 0405.553.535 live official NBB WVV VOL-inb 2026-00263016 52p 357403; assets 603044813 omzet 40776434 pers 7596389 pnl -1879750 cash 24569716 debt 449999751; FOI ready not sent. Do NOT redo Thuiswest.,,"
        f"{TS},{TS},"
        "tick1493 Thuiswest leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00263016 52p 357403; assets 603044813 omzet 40776434 pers 7596389 pnl -1879750 cash 24569716 debt 449999751; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1494,Leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1494 after 1493 Thuiswest. Do NOT redo Thuiswest. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Woonstart / Meetjesland / de Thuisbouwer / Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen / IJzer en Zee. Prefer VOL-inb over VKT. Confirm NOT already in entities. Next every-10 is 1500. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474).,,"
        f"{TS},{TS},"
        "spawned after tick1493 Thuiswest leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover IJzer en Zee / leftover Woonstart / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1493=done + rq_1494 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T20:20:00Z,rq_1493,1493,no,"
        "tick1493 Thuiswest leftover woonmaatschappij residual; KBO 0405.553.535; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 603044813 omzet 40776434 pers 7596389 90.9 VTE pnl -1879750 equity 148379349 cash 24569716 debt 449999751 capex 19362596 dividend 0; FOI ready omzet 40.78m / pers 7.60m 90.9 VTE / debt 450.00m / cash 24.57m UP / beleggingen 15.26m DROP / PnL LOSS 1.88m / dividend 0 / 1 VE; NOT leftover Motena Roeselare / leftover Woonsprong 1492 / leftover Ons Onderdak 1491 / leftover IJzer en Zee / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1494 leftover APB Inovant/Atlas if PDF live else leftover IJzer en Zee / leftover Woonstart / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1136 answered 9 partial 27 total 1184; inventory budgets 42820 commitments 5093 leaderboard 7296 entities 1238 sources 3109; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1493")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1493_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
