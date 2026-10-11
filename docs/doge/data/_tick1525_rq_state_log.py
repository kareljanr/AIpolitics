#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1525=done + spawn rq_1526; update loop_state; append loop_log.
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
        raw += b"\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1525,"):
        raise SystemExit(f"last row is not rq_1525: {last[:80]!r}")
    if b"rq_1526," in raw:
        raise SystemExit("rq_1526 already present — concurrent tick?")
    done = (
        "rq_1525,CAW Antwerpen JR2025 leftover zorg EVA dual residual,hole_fill,5,done,L5,caw_cwan,"
        "Tick 1525 took leftover recognized Flemish CAW Antwerpen 0455.608.604 live official NBB WVV VOL-VZW 2026-00112717 48p 282027; assets 16778368 opbr 52460317 pers 43212061 596.7 VTE cash 1004443 debt 10594656; FOI ready not sent. First per-CAW L5 after umbrella caw_vl. Do NOT redo CAW Antwerpen. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1525 CAW Antwerpen leftover zorg EVA residual; official NBB WVV VOL-VZW 2026-00112717 48p 282027; assets 16778368 opbr 52460317 pers 43212061 596.7 VTE cash 1004443 debt 10594656; FOI ready not sent; next every-10 1530\n"
    )
    spawn = (
        "rq_1526,leftover AGB/APB/CAW/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1526 after 1525 CAW Antwerpen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover other regional CAWs (10 remaining) only if a 2025 CDN now appears. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland no JR; IJzer en Leie/Limburg/Koepel still unpublished). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CAW Antwerpen / IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1525 leftover CAW Antwerpen JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1525=done + rq_1526 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1525,1525,no,"
        "tick1525 leftover recognized Flemish CAW Antwerpen residual; KBO 0455.608.604; live JR2025 official NBB WVV VOL-VZW 2026-00112717; sourced euros assets 16778368 opbr 52460317 omzet 3691060 73 47451115 pers 43212061 596.7 VTE cash 1004443 debt 10594656 pnl -76893; FOI ready 73 split / cash DROP / in-aanbouw JUMP / diensten JUMP / nrec 66A JUMP / 70 category empty / commissaris fee; first per-CAW L5 after umbrella caw_vl; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover CGG VAGGA 1512 / leftover CGG Andante 1519 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1526 leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1168 answered 9 partial 27 total 1216; inventory budgets 44097 commitments 5125 leaderboard 7328 entities 1270 sources 3237; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1525", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1525_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
