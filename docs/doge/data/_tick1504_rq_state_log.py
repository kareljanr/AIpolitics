#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1504=done + spawn rq_1505; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T00:35:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1504,"):
        raise SystemExit(f"last row is not rq_1504: {last[:80]!r}")
    if b"rq_1505," in raw:
        raise SystemExit("rq_1505 already present — concurrent tick?")
    done = (
        "rq_1504,De Noorderkempen JR2025 leftover dual residual,hole_fill,5,done,L5,wm_dnkm,"
        "Tick 1504 took leftover official-41 woonmaatschappij De Noorderkempen 0427.003.106 live official NBB WVV VOL-inb 2026-00131989 70p 842176; assets 129317196 omzet 7793810 pers 1372325 pnl 853059 cash 2718970 debt 109233846; FOI ready not sent. Do NOT redo De Noorderkempen. Next every-10 is 1510.,,"
        f"{TS},{TS},"
        "tick1504 De Noorderkempen leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00131989 70p 842176; assets 129317196 omzet 7793810 pers 1372325 pnl 853059 cash 2718970 debt 109233846; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1505,leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1505 after 1504 De Noorderkempen. Do NOT redo De Noorderkempen. Next every-10 is 1510. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Named leftover official-41 vein from 1464 now exhausted except unpublished Vitare 0808.101.060 (in liquidation; last JR 2024). Re-scan official-41 xlsx for unused names. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo De Noorderkempen / Woontrots / Het Vlaamse Woonanker / Providentia / Vivus.,,"
        f"{TS},{TS},"
        "spawned after tick1504 De Noorderkempen leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover Vitare 0808.101.060 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; named leftover official-41 vein from 1464 exhausted except unpublished Vitare; next every-10 is 1510\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        if any("," in f for f in next(csv.reader(io.StringIO(row)))):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1504=done + rq_1505 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-20T00:35:00Z,rq_1504,1504,no,"
        "tick1504 De Noorderkempen leftover woonmaatschappij residual; KBO 0427.003.106; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 129317196 omzet 7793810 pers 1372325 18.3 VTE pnl 853059 equity 19508599 cash 2718970 debt 109233846 capex 42448162 dividend 0; FOI ready omzet 7.79m DROP / pers 1.37m 18.3 VTE / debt 109.23m DROP / cash 2.72m UP / capex 42.45m transfer-driven / in aanbouw 2.55m DROP / PnL 0.85m UP / dividend 0 / 1 VE; NOT every-10 (next 1510); NOT leftover Erfgoed Noorderkempen 1426 / leftover Bosgroep Kempen Noord 1450 / leftover Woonboog 1478 / leftover De Voorkempen 1487 / leftover AGB Arendonk / leftover AGB Merksplas / leftover Woontrots 1503 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1505 leftover APB Inovant/Atlas if PDF live else leftover Vitare 0808.101.060 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; named leftover official-41 vein from 1464 exhausted except unpublished Vitare; next every-10 is 1510; FOI ready 1147 answered 9 partial 27 total 1195; inventory budgets 43282 commitments 5104 leaderboard 7307 entities 1249 sources 3153; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1504")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1504_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
