#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1500=done + spawn rq_1501; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T22:40:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1500,"):
        raise SystemExit(f"last row is not rq_1500: {last[:80]!r}")
    if b"rq_1501," in raw:
        raise SystemExit("rq_1501 already present — concurrent tick?")
    done = (
        "rq_1500,Vivus JR2025 leftover dual residual + every-10,hole_fill,5,done,L5,wm_vivs,"
        "Tick 1500 took leftover official-41 woonmaatschappij Vivus 0405.430.603 live official NBB WVV VOL-inb 2026-00122331 58p 1038131; assets 303989219 omzet 19547175 pers 3214483 pnl 1023260 cash 10772582 debt 237728579; FOI ready not sent. Every-10 refresh done. Do NOT redo Vivus.,,"
        f"{TS},{TS},"
        "tick1500 Vivus leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00122331 58p 1038131; assets 303989219 omzet 19547175 pers 3214483 pnl 1023260 cash 10772582 debt 237728579; FOI ready not sent; every-10 refresh\r\n"
    )
    spawn = (
        "rq_1501,leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1501 after 1500 Vivus + every-10. Do NOT redo Vivus. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Providentia 0403.320.060 deposit 2026-00121288 LIVE unused / Het Vlaamse Woonanker / Woontrots / De Noorderkempen / Vitare. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Vivus / WM Elan / Woonpijler / de Thuisbouwer / Meetjesland.,,"
        f"{TS},{TS},"
        "spawned after tick1500 Vivus leftover woonmaatschappij residual + every-10; NEXT leftover APB Inovant/Atlas if PDF live else leftover Providentia 2026-00121288 LIVE / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover Vitare / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1500=done + rq_1501 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T22:40:00Z,rq_1500,1500,no,"
        "tick1500 Woonmaatschappij Vivus leftover woonmaatschappij residual; KBO 0405.430.603; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 303989219 omzet 19547175 pers 3214483 34.8 VTE pnl 1023260 equity 63760761 cash 10772582 debt 237728579 capex 18581782 dividend 0; FOI ready omzet 19.55m UP / pers 3.21m 34.8 VTE / debt 237.73m UP / cash 10.77m DROP / beleggingen 2.00m / capex 18.58m / in aanbouw 3.42m DROP / PnL 1.02m / dividend 0 / 1 VE; EVERY-10 refresh done (TE 347.956bn; waste top10 stable); NOT leftover WM Elan 1499 / leftover SW+ 1472 / leftover !Mpuls 1484 / leftover WAGSO Waregem / leftover AGB Wielsbeke / leftover AGL Lendelede / leftover zorg Harelbeke / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1501 leftover APB Inovant/Atlas if PDF live else leftover Providentia 2026-00121288 LIVE / leftover Het Vlaamse Woonanker / leftover Woontrots / leftover De Noorderkempen / leftover Vitare / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510; FOI ready 1143 answered 9 partial 27 total 1191; inventory budgets 43114 commitments 5100 leaderboard 7303 entities 1245 sources 3137; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1500")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1500_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
