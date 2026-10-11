#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1509=done + spawn rq_1510; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T04:00:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1509,"):
        raise SystemExit(f"last row is not rq_1509: {last[:80]!r}")
    if b"rq_1510," in raw:
        raise SystemExit("rq_1510 already present — concurrent tick?")
    done = (
        "rq_1509,CGG VBO JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cgvb,"
        "Tick 1509 took leftover recognized Flemish CGG CGG Vlaams-Brabant Oost 0471.366.154 live official NBB WVV VOL-VZW 2026-00227270 39p 2534398; assets 9329271 opbr 9335733 pers 6655129 69.5 VTE cash 2477705 debt 2332348; FOI ready not sent. Do NOT redo CGG VBO. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1510 and MUST do the every-10 refresh.,,"
        f"{TS},{TS},"
        "tick1509 CGG VBO leftover recognized CGG residual; official NBB WVV VOL-VZW 2026-00227270 39p 2534398; assets 9329271 opbr 9335733 pers 6655129 69.5 VTE cash 2477705 debt 2332348; FOI ready not sent\r\n"
    )
    spawn = (
        "rq_1510,leftover AGB/APB/IGS dual residual hole-fill EVERY-10,hole_fill,5,open,L5,,"
        "Tick 1510 after 1509 CGG VBO. MUST do the every-10 refresh of docs/doge/data/progress_every_10_ticks.md and docs/doge/data/doge_waste_top10_current.md. Do NOT redo CGG VBO. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads. Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other recognized CGG of mined cities if unused + live PDF (CGG Kempen 0416.724.470 still JR2024 as of 1508). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG VBO / CGG SDW / CGG NWVL / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1509 leftover CGG VBO JR2025; MUST do every-10 refresh; NEXT leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Kempen still JR2024 as of 1508); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1510 MUST refresh\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1509=done + rq_1510 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-20T04:00:00Z,rq_1509,1509,no,"
        "tick1509 leftover recognized Flemish CGG CGG Vlaams-Brabant Oost residual; KBO 0471.366.154; live JR2025 official NBB WVV VOL-VZW 2026-00227270; sourced euros assets 9329271 opbr 9335733 pers 6655129 69.5 VTE; FOI ready 73 split / andere 74 JUMP / cash DROP; NOT every-10 (next 1510 MUST do every-10 refresh); NOT leftover CGG NWVL 1507 / leftover CGG SDW 1508 / leftover CGG umbrella / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1510 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md then leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Kempen still JR2024 as of 1508); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1152 answered 9 partial 27 total 1200; inventory budgets 43446 commitments 5109 leaderboard 7312 entities 1254 sources 3173; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1509")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1509_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
