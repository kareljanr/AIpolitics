#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1527=done + spawn rq_1528; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1527,"):
        raise SystemExit(f"last row is not rq_1527: {last[:80]!r}")
    if b"rq_1528," in raw:
        raise SystemExit("rq_1528 already present — concurrent tick?")
    done = (
        "rq_1527,CAW Brussel JR2025 leftover zorg EVA dual residual,hole_fill,5,done,L5,caw_cwbr,"
        "Tick 1527 took leftover recognized Flemish CAW Brussel 0464.230.122 live official NBB WVV VOL-VZW 2026-00101211 Initial 54p 9312176; assets 6760334 opbr 13378953 pers 11589623 160.2 VTE cash 926690 debt 3508957; FOI ready not sent. Third per-CAW L5 after CAW Antwerpen 1525 and CAW De Kempen 1526. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1527 CAW Brussel leftover zorg EVA residual; official NBB WVV VOL-VZW 2026-00101211 Initial 54p 9312176; assets 6760334 opbr 13378953 pers 11589623 160.2 VTE cash 926690 debt 3508957; FOI ready not sent; next every-10 1530\n"
    )
    spawn = (
        "rq_1528,leftover AGB/APB/CAW/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1528 after 1527 CAW Brussel. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover other regional CAWs (8 remaining) only if a 2025 CDN now appears — leftover CAW Rivierenland 0466.852.882 deposit 2026-00090859 LIVE unused (zetel Maurits Sabbestraat 119 2800 Mechelen; parent city_mechelen; prefix cwrv unused). Leftover CAW Halle-Vilvoorde / Oost-Brabant / Limburg / Oost-Vlaanderen / NWVL / CWVL / ZWVL: look up official names/KBOs — do NOT invent. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1527 leftover CAW Brussel JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (CAW Rivierenland 2026-00090859 LIVE unused) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; CAW Brussel TAKEN; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1527=done + rq_1528 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1527,1527,no,"
        "tick1527 leftover recognized Flemish CAW Brussel residual; KBO 0464.230.122; live JR2025 official NBB WVV VOL-VZW 2026-00101211 Initial; sourced euros assets 6760334 opbr 13378953 omzet 458249 73 12807697 pers 11589623 160.2 VTE cash 926690 debt 3508957 pnl -24907; FOI ready 73 split / cash DROP / other ST JUMP / prepaid JUMP / 74 DROP / 70 category empty / commissaris fee / PnL LOSS; third per-CAW L5 after CAW Antwerpen 1525 and CAW De Kempen 1526; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover CGG Brussel 1521 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover umbrella caw_vl / leftover IVAREM 1524 / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1528 leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (CAW Rivierenland 2026-00090859 LIVE unused) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1170 answered 9 partial 27 total 1218; inventory budgets 44177 commitments 5127 leaderboard 7330 entities 1272 sources 3245; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1527", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1527_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
