#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1505=done + spawn rq_1506; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T01:10:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1505,"):
        raise SystemExit(f"last row is not rq_1505: {last[:80]!r}")
    if b"rq_1506," in raw:
        raise SystemExit("rq_1506 already present — concurrent tick?")
    done = (
        "rq_1505,Vitare JR2025 leftover former SHM dual residual,hole_fill,5,done,L5,wm_vitr,"
        "Tick 1505 took leftover former SHM / leftover unpublished official-41 Vitare 0808.101.060 live official NBB WVV VOL-kap 2026-00332427 36p 652219; assets 17056698 omzet 15730 pers 0 pnl 1964420 cash 39058 debt 41297098 nrec 2305848; FOI ready not sent. Do NOT redo Vitare. Named leftover official-41 vein from 1464 now fully exhausted. Next every-10 is 1510.,,"
        f"{TS},{TS},"
        "tick1505 Vitare leftover former SHM residual; official NBB WVV VOL-kap 2026-00332427 36p 652219; assets 17056698 omzet 15730 pers 0 pnl 1964420 cash 39058 debt 41297098 nrec 2305848; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1506,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1506 after 1505 Vitare. Do NOT redo Vitare. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Named leftover official-41 vein from 1464 now fully exhausted (Vitare JR2025 TAKEN 1505). Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Vitare / De Noorderkempen / Woontrots / Het Vlaamse Woonanker / Providentia / Vivus / Dimensa.,,"
        f"{TS},{TS},"
        "spawned after tick1505 Vitare leftover former SHM residual; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1505=done + rq_1506 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-20T01:10:00Z,rq_1505,1505,no,"
        "tick1505 Vitare leftover former SHM residual; KBO 0808.101.060; live JR2025 official NBB WVV VOL-kap PDF; sourced euros assets 17056698 omzet 15730 pers 0 0 VTE pnl 1964420 equity -24315400 cash 39058 debt 41297098 capex 0 dividend 0 nrec 2305848; FOI ready omzet 15.7k DROP / pers 0 / debt 41.30m UP / cash 39.1k UP / nrec WV 2.31m Matexi-takeback / equity -24.32m / PnL 1.96m reval-driven / capex 0 / dividend 0; NOT every-10 (next 1510); NOT leftover Dimensa 1466 / leftover AGB Deinze / leftover Meetjesland 1496 / leftover De Noorderkempen 1504 / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1506 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1510; FOI ready 1148 answered 9 partial 27 total 1196; inventory budgets 43320 commitments 5105 leaderboard 7308 entities 1250 sources 3157; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1505")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1505_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
