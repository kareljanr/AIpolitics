#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1502=done + spawn rq_1503; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:40:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1502,"):
        raise SystemExit(f"last row is not rq_1502: {last[:80]!r}")
    if b"rq_1503," in raw:
        raise SystemExit("rq_1503 already present — concurrent tick?")
    done = (
        "rq_1502,Het Vlaamse Woonanker JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wvwa,"
        "Tick 1502 took leftover official-41 woonmaatschappij Het Vlaamse Woonanker 0403.304.026 live official NBB WVV VOL-inb 2026-00145176 61p 998995; assets 116281420 omzet 11795988 pers 1918960 pnl -960306 cash 2894405 debt 98315832; FOI ready not sent. Do NOT redo Het Vlaamse Woonanker. Next every-10 is 1510.,,"
        f"{TS},{TS},"
        "tick1502 Het Vlaamse Woonanker leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00145176 61p 998995; assets 116281420 omzet 11795988 pers 1918960 pnl -960306 cash 2894405 debt 98315832; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1503,leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1503 after 1502 Het Vlaamse Woonanker. Do NOT redo Het Vlaamse Woonanker. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Woontrots 0400.629.794 deposit 2026-00170888 LIVE unused / De Noorderkempen 0427.003.106 deposit 2026-00131989 LIVE unused / Vitare 0808.101.060. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Het Vlaamse Woonanker / Providentia / Vivus / WM Elan / Woonpijler / de Thuisbouwer / Meetjesland.,,"
        f"{TS},{TS},"
        "spawned after tick1502 Het Vlaamse Woonanker leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Woontrots 0400.629.794 deposit 2026-00170888 LIVE unused / leftover De Noorderkempen 0427.003.106 deposit 2026-00131989 LIVE unused / leftover Vitare 0808.101.060 / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1502=done + rq_1503 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T23:40:00Z,rq_1502,1502,no,"
        "tick1502 Het Vlaamse Woonanker leftover woonmaatschappij residual; KBO 0403.304.026; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 116281420 omzet 11795988 pers 1918960 22.7 VTE pnl -960306 equity 16952289 cash 2894405 debt 98315832 capex 1292536 dividend 0; FOI ready omzet 11.80m UP / pers 1.92m 22.7 VTE / debt 98.32m DROP / cash 2.89m DROP / capex 1.29m / in aanbouw 1.02m DROP / PnL LOSS 0.96m / patrimonial split / dividend 0 / 1 VE; NOT every-10 (next 1510); NOT leftover Providentia 1501 / leftover Woonpunt Zennevallei 1485 / leftover Inter-Vilvoordse 1489 / leftover Fluvius Halle-Vilvoorde / leftover AGB Grimbergen / leftover Erfgoed Brabantse Kouters 1428 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1503 leftover APB Inovant/Atlas if PDF live else leftover Woontrots 0400.629.794 deposit 2026-00170888 LIVE unused / leftover De Noorderkempen 0427.003.106 deposit 2026-00131989 LIVE unused / leftover Vitare 0808.101.060 / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; next every-10 is 1510; FOI ready 1145 answered 9 partial 27 total 1193; inventory budgets 43198 commitments 5102 leaderboard 7305 entities 1247 sources 3145; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1502")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1502_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
