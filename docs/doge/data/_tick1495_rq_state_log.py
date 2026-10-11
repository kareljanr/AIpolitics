#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1495=done + spawn rq_1496; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:00:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1495,"):
        raise SystemExit(f"last row is not rq_1495: {last[:80]!r}")
    if b"rq_1496," in raw:
        raise SystemExit("rq_1496 already present — concurrent tick?")
    done = (
        "rq_1495,Woonstart JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wstrt,"
        "Tick 1495 took leftover official-41 woonmaatschappij Woonstart 0405.220.963 live official NBB WVV VKT-inb 2026-00159134 38p 746796; assets 97529158 omzet 7325986 pers 1536245 pnl -835178 cash 2036624 debt 81699993; FOI ready not sent. Do NOT redo Woonstart.,,"
        f"{TS},{TS},"
        "tick1495 Woonstart leftover woonmaatschappij residual; official NBB WVV VKT-inb 2026-00159134 38p 746796; assets 97529158 omzet 7325986 pers 1536245 pnl -835178 cash 2036624 debt 81699993; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1496,Leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1496 after 1495 Woonstart. Do NOT redo Woonstart. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Meetjesland / de Thuisbouwer / Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen. Prefer VOL-inb over VKT. Confirm NOT already in entities. Next every-10 is 1500. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Woonstart / IJzer en Zee / Thuiswest.,,"
        f"{TS},{TS},"
        "spawned after tick1495 Woonstart leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Meetjesland / leftover de Thuisbouwer / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1495=done + rq_1496 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T21:00:00Z,rq_1495,1495,no,"
        "tick1495 Woonstart leftover woonmaatschappij residual; KBO 0405.220.963; live JR2025 official NBB WVV VKT-inb PDF; sourced euros assets 97529158 omzet 7325986 pers 1536245 17.1 VTE pnl -835178 equity 15514356 cash 2036624 debt 81699993 capex 31842106 dividend 0; FOI ready omzet 7.33m UP / pers 1.54m 17.1 VTE / debt 81.70m UP / cash 2.04m UP / capex 31.84m JUMP / PnL -0.84m / dividend 0 / 1 VE; NOT leftover AGB Tielt / leftover Woonstroom 1475 / leftover Thuiswest 1493 / leftover IJzer en Zee 1494 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1496 leftover APB Inovant/Atlas if PDF live else leftover Meetjesland / leftover de Thuisbouwer / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1138 answered 9 partial 27 total 1186; inventory budgets 42904 commitments 5095 leaderboard 7298 entities 1240 sources 3117; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1495")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1495_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
