#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1519=done + spawn rq_1520; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io, subprocess

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = subprocess.check_output(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], text=True).strip()

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1519,"):
        raise SystemExit(f"last row is not rq_1519: {last[:80]!r}")
    if b"rq_1520," in raw:
        raise SystemExit("rq_1520 already present — concurrent tick?")
    done = (
        "rq_1519,CGG Andante JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cgan,"
        "Tick 1519 took leftover recognized Flemish CGG CGG Andante 0470.375.071 live official NBB WVV VOL-VZW 2026-00103827 45p 594088; assets 10657318 opbr 10796084 pers 9295936 108.7 VTE cash 1540487 debt 2163630; FOI ready not sent. NEW unused recognized CGG not in 1507-1518 list. Do NOT redo CGG Andante. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1520 MUST refresh progress.,,"
        f"{TS},{TS},"
        "tick1519 CGG Andante leftover recognized CGG residual; official NBB WVV VOL-VZW 2026-00103827 45p 594088; assets 10657318 opbr 10796084 pers 9295936 108.7 VTE cash 1540487 debt 2163630; FOI ready not sent; next every-10 1520 MUST refresh progress\r\n"
    )
    spawn = (
        "rq_1520,leftover AGB/APB/IGS dual residual hole-fill EVERY-10,hole_fill,5,open,L5,,"
        "Tick 1520 after 1519 CGG Andante. EVERY-10: must refresh docs/doge/data/progress_every_10_ticks.md and docs/doge/data/doge_waste_top10_current.md. Dual NEW since 1480 starts with LeefGoed 570.75m plus 1482-1520 units including leftover CGGs 1507-1519. Do NOT redo CGG Andante. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover recognized CGG PassAnt 0446.599.876 / leftover CGG Brussel 0471.365.461 only if unused + live JR2025 PDF. Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1519 leftover CGG Andante JR2025; EVERY-10 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md; NEXT leftover AGB/APB of mined cities if PDF live else leftover CGG PassAnt/Brussel if live PDF else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1520\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1519=done + rq_1520 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1519,1519,no,"
        "tick1519 leftover recognized Flemish CGG CGG Andante residual; NEW unused recognized CGG not in 1507-1518 list; KBO 0470.375.071; live JR2025 official NBB WVV VOL-VZW 2026-00103827; sourced euros assets 10657318 opbr 10796084 pers 9295936 108.7 VTE; FOI ready 73 split / kapsubs JUMP / in aanbouw JUMP / other recv JUMP / PnL LOSS; NOT every-10 (next 1520 MUST refresh progress); NOT leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover WV Blankenberge 1506 / leftover CGG umbrella / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1520 leftover AGB/APB of mined cities if PDF live else leftover CGG PassAnt/Brussel if live PDF else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1162 answered 9 partial 27 total 1210; inventory budgets 43851 commitments 5119 leaderboard 7322 entities 1264 sources 3213; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1519", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1519_logblock.md").read_text(encoding="utf-8")
    if "2026-08-20T00:15:12Z" in block:
        block = block.replace("2026-08-20T00:15:12Z", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
