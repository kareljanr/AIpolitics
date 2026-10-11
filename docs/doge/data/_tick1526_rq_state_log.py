#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1526=done + spawn rq_1527; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1526,"):
        raise SystemExit(f"last row is not rq_1526: {last[:80]!r}")
    if b"rq_1527," in raw:
        raise SystemExit("rq_1527 already present — concurrent tick?")
    done = (
        "rq_1526,CAW De Kempen JR2025 leftover zorg EVA dual residual,hole_fill,5,done,L5,caw_cwkp,"
        "Tick 1526 took leftover recognized Flemish CAW De Kempen 0464.222.895 live official NBB WVV VOL-VZW 2026-00128692 Aanpassing 42p 3801416; assets 19957060 opbr 13824525 pers 10852214 148 VTE cash 674251 debt 7514813; FOI ready not sent. Second per-CAW L5 after CAW Antwerpen 1525. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1526 CAW De Kempen leftover zorg EVA residual; official NBB WVV VOL-VZW 2026-00128692 Aanpassing 42p 3801416; assets 19957060 opbr 13824525 pers 10852214 148 VTE cash 674251 debt 7514813; FOI ready not sent; next every-10 1530\n"
    )
    spawn = (
        "rq_1527,leftover AGB/APB/CAW/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1527 after 1526 CAW De Kempen. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover other regional CAWs (9 remaining) only if a 2025 CDN now appears — leftover CAW Brussel 0464.230.122 deposit 2026-00101211 LIVE unused / leftover CAW Rivierenland 0466.852.882 deposit 2026-00090859 LIVE unused. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland no JR; IJzer en Leie/Limburg/Koepel still unpublished). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CAW De Kempen / CAW Antwerpen / IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1526 leftover CAW De Kempen JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (CAW Brussel 2026-00101211 LIVE / CAW Rivierenland 2026-00090859 LIVE) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1526=done + rq_1527 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1526,1526,no,"
        "tick1526 leftover recognized Flemish CAW De Kempen residual; KBO 0464.222.895; live JR2025 official NBB WVV VOL-VZW 2026-00128692 Aanpassing; sourced euros assets 19957060 opbr 13824525 omzet 595237 73 12796950 pers 10852214 148 VTE cash 674251 debt 7514813 pnl 109444; FOI ready 73 split / expl DROP / taxsoc JUMP / beleg JUMP / 70 category empty / commissaris fee / VIPA; second per-CAW L5 after CAW Antwerpen 1525; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover CGG Kempen 1516 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover Welzijnszorg Kempen / leftover De Noorderkempen 1504 / leftover Erfgoed Noorderkempen 1426 / leftover IVAREM 1524 / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1527 leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (CAW Brussel 2026-00101211 LIVE / CAW Rivierenland 2026-00090859 LIVE) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1169 answered 9 partial 27 total 1217; inventory budgets 44137 commitments 5126 leaderboard 7329 entities 1271 sources 3241; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1526", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1526_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
