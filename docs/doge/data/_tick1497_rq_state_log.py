#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1497=done + spawn rq_1498; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T21:40:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1497,"):
        raise SystemExit(f"last row is not rq_1497: {last[:80]!r}")
    if b"rq_1498," in raw:
        raise SystemExit("rq_1498 already present — concurrent tick?")
    done = (
        "rq_1497,de Thuisbouwer JR2025 leftover dual residual,hole_fill,5,done,L5,wm_thbw,"
        "Tick 1497 took leftover official-41 woonmaatschappij de Thuisbouwer 0405.085.262 live official NBB WVV VOL-inb 2026-00200690 53p 1108201; assets 202554297 omzet 12474312 pers 1868369 pnl 2048234 cash 10773820 debt 125064700; FOI ready not sent. Do NOT redo de Thuisbouwer.,,"
        f"{TS},{TS},"
        "tick1497 de Thuisbouwer leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00200690 53p 1108201; assets 202554297 omzet 12474312 pers 1868369 pnl 2048234 cash 10773820 debt 125064700; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1498,Leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1498 after 1497 de Thuisbouwer. Do NOT redo de Thuisbouwer. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen. Prefer VOL-inb over VKT. Confirm NOT already in entities. Next every-10 is 1500. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo de Thuisbouwer / Meetjesland / Woonstart.,,"
        f"{TS},{TS},"
        "spawned after tick1497 de Thuisbouwer leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Woonpijler / leftover WM Elan / leftover Vivus / leftover Providentia / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1497=done + rq_1498 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T21:40:00Z,rq_1497,1497,no,"
        "tick1497 de Thuisbouwer leftover woonmaatschappij residual; KBO 0405.085.262; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 202554297 omzet 12474312 pers 1868369 20.1 VTE pnl 2048234 equity 75921924 cash 10773820 debt 125064700 capex 12121406 dividend 1075; FOI ready omzet 12.47m DROP / pers 1.87m 20.1 VTE / debt 125.06m DROP / cash 10.77m DROP / capex 12.12m / PnL 2.05m / dividend 1075 / 2 VE; NOT leftover AGB HIM Hamme / leftover AGB Zele / leftover stek92 1482 / leftover Dender-Zuid 1467 / leftover Meetjesland 1496 / leftover Woonstart 1495 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1498 leftover APB Inovant/Atlas if PDF live else leftover Woonpijler / leftover WM Elan / leftover Vivus / leftover Providentia / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1140 answered 9 partial 27 total 1188; inventory budgets 42988 commitments 5097 leaderboard 7300 entities 1242 sources 3125; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1497")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1497_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
