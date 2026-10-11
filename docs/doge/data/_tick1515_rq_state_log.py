#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1515=done + spawn rq_1516; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path
import csv, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T23:49:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\r\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1515,"):
        raise SystemExit(f"last row is not rq_1515: {last[:80]!r}")
    if b"rq_1516," in raw:
        raise SystemExit("rq_1516 already present — concurrent tick?")
    done = (
        "rq_1515,CGG Integra JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cgin,"
        "Tick 1515 took leftover recognized Flemish CGG CGG Integra 0469.813.065 live official NBB WVV VOL-VZW 2026-00205082 41p 1233798; assets 14975892 opbr 19622796 pers 16532661 191.5 VTE cash 3698941 debt 4852883; FOI ready not sent. Do NOT redo CGG Integra. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1520.,,"
        f"{TS},{TS},"
        "tick1515 CGG Integra leftover recognized CGG residual; official NBB WVV VOL-VZW 2026-00205082 41p 1233798; assets 14975892 opbr 19622796 pers 16532661 191.5 VTE cash 3698941 debt 4852883; FOI ready not sent; next every-10 1520\r\n"
    )
    spawn = (
        "rq_1516,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1516 after 1515 CGG Integra. Do NOT redo CGG Integra. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other recognized CGG of mined cities if unused + live PDF — leftover CGG Kempen 0416.724.470 deposit 2026-00178615 LIVE unused / leftover CGG Ahasverus 0471.364.174 / leftover CGG Largo 0471.370.411. Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1515 leftover CGG Integra JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Kempen 0416.724.470 deposit 2026-00178615 LIVE unused / leftover CGG Ahasverus / leftover CGG Largo); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1520\r\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1515=done + rq_1516 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T23:49:00Z,rq_1515,1515,no,"
        "tick1515 leftover recognized Flemish CGG CGG Integra residual; KBO 0469.813.065; live JR2025 official NBB WVV VOL-VZW 2026-00205082; sourced euros assets 14975892 opbr 19622796 pers 16532661 191.5 VTE; FOI ready in aanbouw JUMP / andere 74 / andere pers 623 JUMP / cash DROP; NOT every-10 (next 1520); NOT leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover WV Blankenberge 1506 / leftover CGG umbrella / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1516 leftover AGB/APB of mined cities if PDF live else leftover recognized CGG of mined cities if unused + live PDF (CGG Kempen 0416.724.470 deposit 2026-00178615 LIVE unused / leftover CGG Ahasverus / leftover CGG Largo); leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1158 answered 9 partial 27 total 1206; inventory budgets 43696 commitments 5115 leaderboard 7318 entities 1260 sources 3197; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1515")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1515_logblock.md").read_text(encoding="utf-8")
    # patch inventory line with counted numbers
    block = block.replace("Inventory after write (counted from disk): see post-write count.",
                          "Inventory after write (counted from disk): budgets 43696 · commitments 5115 · leaderboard 7318 · entities 1260 · sources 3197 · FOI ready 1158 / answered 9 / partial 27 / total 1206.")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
