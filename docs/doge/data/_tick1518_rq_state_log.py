#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1518=done + spawn rq_1519; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1518,"):
        raise SystemExit(f"last row is not rq_1518: {last[:80]!r}")
    if b"rq_1519," in raw:
        raise SystemExit("rq_1519 already present — concurrent tick?")
    done = (
        "rq_1518,CGG Largo JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cglr,"
        "Tick 1518 took leftover recognized Flemish CGG CGG Largo 0471.370.411 live official NBB WVV VKT-VZW 2026-00186340 22p 348406; assets 6034498 opbr 6764354 pers 5512029 60.9 VTE cash 1666321 debt 1287831; FOI ready not sent. Do NOT redo CGG Largo. Named leftover official-41 vein from 1464 fully exhausted. Live-PDF CGG vein now fully exhausted. Next every-10 is 1520.,,"
        f"{TS},{TS},"
        "tick1518 CGG Largo leftover recognized CGG residual; official NBB WVV VKT-VZW 2026-00186340 22p 348406; assets 6034498 opbr 6764354 pers 5512029 60.9 VTE cash 1666321 debt 1287831; FOI ready not sent; next every-10 1520\r\n"
    )
    spawn = (
        "rq_1519,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1519 after 1518 CGG Largo. Do NOT redo CGG Largo. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Live-PDF recognized CGG vein now fully exhausted (Largo TAKEN). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / WV Blankenberge / Vitare / official-41 1464-1505 / leftover Motena Roeselare.,,"
        f"{TS},{TS},"
        "spawned after tick1518 leftover CGG Largo JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; live-PDF CGG vein now fully exhausted; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1520\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1518=done + rq_1519 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1518,1518,no,"
        "tick1518 leftover recognized Flemish CGG CGG Largo residual; KBO 0471.370.411; live JR2025 official NBB WVV VKT-VZW 2026-00186340; sourced euros assets 6034498 opbr 6764354 pers 5512029 60.9 VTE; FOI ready 73 split / bestemde JUMP / kapsubs JUMP / other recv JUMP / PnL DROP; NOT every-10 (next 1520); NOT leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG Integra 1515 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover WV Blankenberge 1506 / leftover CGG umbrella / leftover Motena Roeselare / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1519 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; live-PDF CGG vein now fully exhausted; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1161 answered 9 partial 27 total 1209; inventory budgets 43811 commitments 5118 leaderboard 7321 entities 1263 sources 3209; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1518", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1518_logblock.md").read_text(encoding="utf-8")
    # stamp real UTC into the header if the placeholder is still there
    if "2026-08-20T00:08:00Z" in block:
        block = block.replace("2026-08-20T00:08:00Z", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
