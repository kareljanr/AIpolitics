#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1501=done + spawn rq_1502; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:15:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1501,"):
        raise SystemExit(f"last row is not rq_1501: {last[:80]!r}")
    if b"rq_1502," in raw:
        raise SystemExit("rq_1502 already present — concurrent tick?")
    done = (
        "rq_1501,Providentia JR2025 leftover dual residual,hole_fill,5,done,L5,wm_prvd,"
        "Tick 1501 took leftover official-41 woonmaatschappij Providentia 0403.320.060 live official NBB WVV VOL-inb 2026-00121288 80p 1196609; assets 228332050 omzet 20807498 pers 3571584 pnl 1625580 cash 5321913 debt 195927025; FOI ready not sent. Do NOT redo Providentia. Next every-10 is 1510.,,"
        f"{TS},{TS},"
        "tick1501 Providentia leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00121288 80p 1196609; assets 228332050 omzet 20807498 pers 3571584 pnl 1625580 cash 5321913 debt 195927025; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1502,leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1502 after 1501 Providentia. Do NOT redo Providentia. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Het Vlaamse Woonanker 0403.304.026 / Woontrots 0400.629.794 / De Noorderkempen 0427.003.106 / Vitare 0808.101.060. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Providentia / Vivus / WM Elan / Woonpijler / de Thuisbouwer / Meetjesland.,,"
        f"{TS},{TS},"
        "spawned after tick1501 Providentia leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Het Vlaamse Woonanker 0403.304.026 / leftover Woontrots 0400.629.794 / leftover De Noorderkempen 0427.003.106 / leftover Vitare 0808.101.060 / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1501=done + rq_1502 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T23:15:00Z,rq_1501,1501,no,"
        "tick1501 Providentia leftover woonmaatschappij residual; KBO 0403.320.060; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 228332050 omzet 20807498 pers 3571584 39.1 VTE pnl 1625580 equity 29021932 cash 5321913 debt 195927025 capex 92686585 dividend 0; FOI ready omzet 20.81m DROP / pers 3.57m 39.1 VTE / debt 195.93m UP / cash 5.32m UP / capex 92.69m / in aanbouw 6.17m / PnL 1.63m DROP / dividend 0 / 1 VE; NOT every-10 (next 1510); NOT leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGA Asse / leftover Vivus 1500 / leftover WM Elan 1499 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1502 leftover APB Inovant/Atlas if PDF live else leftover Het Vlaamse Woonanker 0403.304.026 / leftover Woontrots 0400.629.794 / leftover De Noorderkempen 0427.003.106 / leftover Vitare 0808.101.060 / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510; FOI ready 1144 answered 9 partial 27 total 1192; inventory budgets 43156 commitments 5101 leaderboard 7304 entities 1246 sources 3141; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1501")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1501_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
