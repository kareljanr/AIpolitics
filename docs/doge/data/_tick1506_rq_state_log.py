#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1506=done + spawn rq_1507; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T02:20:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1506,"):
        raise SystemExit(f"last row is not rq_1506: {last[:80]!r}")
    if b"rq_1507," in raw:
        raise SystemExit("rq_1507 already present — concurrent tick?")
    done = (
        "rq_1506,Welzijnsvereniging Blankenberge leftover zorg unpublished FOI,hole_fill,5,done,L5,zorg_wvbl,"
        "Tick 1506 took leftover zorg Welzijnsvereniging Blankenberge 1013.719.482 after leftover AGB/APB hunt; no live JR2025 BBC/NBB PDF; FOI ready not sent. Do NOT redo WV Blankenberge. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1510.,,"
        f"{TS},{TS},"
        "tick1506 leftover zorg residual of mined Blankenberge; KBO 1013.719.482; no JR2025 PDF; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1507,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1507 after 1506 Welzijnsvereniging Blankenberge. Do NOT redo WV Blankenberge. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo WV Blankenberge / Vitare / De Noorderkempen / Woontrots / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1506 leftover zorg WV Blankenberge unpublished; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1506=done + rq_1507 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-20T02:20:00Z,rq_1506,1506,no,"
        "tick1506 leftover zorg Welzijnsvereniging Blankenberge residual; KBO 1013.719.482; no live JR2025 BBC/NBB PDF; no sourced euros; FOI ready unpublished JR2025; NOT every-10 (next 1510); NOT leftover AGB Blankenberge 1323 / leftover Zetus 1490 / leftover Motena / leftover Vitare 1505 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1507 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1510; FOI ready 1149 answered 9 partial 27 total 1197; inventory budgets 43320 commitments 5106 leaderboard 7309 entities 1251 sources 3161; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1506")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1506_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
