#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1511=done + spawn rq_1512; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-20T06:00:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1511,"):
        raise SystemExit(f"last row is not rq_1511: {last[:80]!r}")
    if b"rq_1512," in raw:
        raise SystemExit("rq_1512 already present — concurrent tick?")
    done = (
        "rq_1511,CGG Adentro JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cgad,"
        "Tick 1511 took leftover recognized Flemish CGG CGG Adentro 0470.717.046 live official NBB WVV VOL-VZW 2026-00188352 44p 630352; assets 9833698 opbr 13798629 pers 11157856 121.1 VTE cash 2905244 debt 2344595; FOI ready not sent. Do NOT redo CGG Adentro. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1520.,,"
        f"{TS},{TS},"
        "tick1511 CGG Adentro leftover recognized CGG residual; official NBB WVV VOL-VZW 2026-00188352 44p 630352; assets 9833698 opbr 13798629 pers 11157856 121.1 VTE cash 2905244 debt 2344595; FOI ready not sent; next every-10 1520\r\n"
    )
    spawn = (
        "rq_1512,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1512 after 1511 CGG Adentro. Do NOT redo CGG Adentro. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick; Foleon leftover slugs redirect Hooibeekhoeve). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other recognized CGG of mined cities if unused + live PDF (CGG Ahasverus 0471.364.174 / leftover CGG VAGGA 0473.488.474 / leftover CGG Prisma 0472.448.101 / leftover CGG Largo 0471.370.411 / leftover CGG De Pont 0472.106.225 / leftover CGG Integra 0469.813.065 / leftover CGG Kempen 0416.724.470 still no unused live JR2025 CDN as of 1511; SBM Prisma/Integra still JR2024). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1511 leftover CGG Adentro JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Ahasverus / VAGGA / Prisma / Largo / De Pont / Integra / Kempen still no unused live JR2025 CDN as of 1511); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1520\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1511=done + rq_1512 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-20T06:00:00Z,rq_1511,1511,no,"
        "tick1511 leftover recognized Flemish CGG CGG Adentro residual; KBO 0470.717.046; live JR2025 official NBB WVV VOL-VZW 2026-00188352; sourced euros assets 9833698 opbr 13798629 pers 11157856 121.1 VTE; FOI ready 73 split / cash JUMP / bestemde JUMP; NOT every-10 (next 1520); NOT leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1512 leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Ahasverus / VAGGA / Prisma / Largo / De Pont / Integra / Kempen still no unused live JR2025 CDN as of 1511); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1154 answered 9 partial 27 total 1202; inventory budgets 43533 commitments 5111 leaderboard 7314 entities 1256 sources 3181; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1511")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1511_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
