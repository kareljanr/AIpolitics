#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1499=done + spawn rq_1500; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:20:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1499,"):
        raise SystemExit(f"last row is not rq_1499: {last[:80]!r}")
    if b"rq_1500," in raw:
        raise SystemExit("rq_1500 already present — concurrent tick?")
    done = (
        "rq_1499,WM Elan JR2025 leftover dual residual,hole_fill,5,done,L5,wm_elan,"
        "Tick 1499 took leftover official-41 woonmaatschappij WM Elan 0405.412.092 live official NBB WVV VOL-inb 2026-00144589 72p 992461; assets 179416827 omzet 10963582 pers 2241828 pnl 1657825 cash 9893916 debt 136938057; FOI ready not sent. Do NOT redo WM Elan. Next tick 1500 MUST do every-10 refresh.,,"
        f"{TS},{TS},"
        "tick1499 WM Elan leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00144589 72p 992461; assets 179416827 omzet 10963582 pers 2241828 pnl 1657825 cash 9893916 debt 136938057; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1500,EVERY-10 leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1500 after 1499 WM Elan. MUST refresh docs/doge/data/progress_every_10_ticks.md and docs/doge/data/doge_waste_top10_current.md (every-10). Do NOT redo WM Elan. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Vivus 0405.430.603 deposit 2026-00122331 LIVE unused / Providentia 0403.320.060 deposit 2026-00121288 LIVE unused / Het Vlaamse Woonanker / Woontrots / De Noorderkempen / Vitare. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo WM Elan / Woonpijler / de Thuisbouwer / Meetjesland / Woonstart.,,"
        f"{TS},{TS},"
        "spawned after tick1499 WM Elan leftover woonmaatschappij residual; EVERY-10 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md; NEXT leftover APB Inovant/Atlas if PDF live else leftover Vivus 2026-00122331 LIVE / leftover Providentia 2026-00121288 LIVE / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover Vitare / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1499=done + rq_1500 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T22:20:00Z,rq_1499,1499,no,"
        "tick1499 WM Elan leftover woonmaatschappij residual; KBO 0405.412.092; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 179416827 omzet 10963582 pers 2241828 26.8 VTE pnl 1657825 equity 40289353 cash 9893916 debt 136938057 capex 16411769 dividend 0; FOI ready omzet 10.96m UP / pers 2.24m 26.8 VTE / debt 136.94m UP / cash 9.89m DROP / beleggingen 15.00m JUMP / capex 16.41m / in aanbouw 18.38m / PnL 1.66m / dividend 0 / 2 VE; NOT leftover AGB Zwevegem / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover Vivus / leftover Woonpijler 1498 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1500 EVERY-10 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md then leftover APB Inovant/Atlas if PDF live else leftover Vivus 2026-00122331 LIVE / leftover Providentia 2026-00121288 LIVE / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover Vitare / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1142 answered 9 partial 27 total 1190; inventory budgets 43072 commitments 5099 leaderboard 7302 entities 1244 sources 3133; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1499")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1499_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
