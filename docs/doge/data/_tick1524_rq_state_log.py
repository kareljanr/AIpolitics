#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1524=done + spawn rq_1525; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1524,"):
        raise SystemExit(f"last row is not rq_1524: {last[:80]!r}")
    if b"rq_1525," in raw:
        raise SystemExit("rq_1525 already present — concurrent tick?")
    done = (
        "rq_1524,IVAREM JR2025 leftover IGS dual residual,hole_fill,5,done,L5,igs_ivrm,"
        "Tick 1524 took leftover IGS IVAREM 0267.403.264 live official NBB WVV VOL-inb 2026-00373329 71p 1241161; assets 61398227 omzet 34824643 pers 12430050 165.8 VTE cash 8106299 debt 37235254; FOI ready not sent. TRUE JR2025 after prior Busibee false-alarm. Do NOT redo IVAREM. Live-PDF CGG vein remains fully exhausted. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1524 IVAREM leftover IGS residual; official NBB WVV VOL-inb 2026-00373329 71p 1241161; assets 61398227 omzet 34824643 pers 12430050 165.8 VTE cash 8106299 debt 37235254; FOI ready not sent; next every-10 1530\n"
    )
    spawn = (
        "rq_1525,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1525 after 1524 IVAREM. Do NOT redo IVAREM. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (IJzer en Leie still no JR; Houtland/Limburg/Koepel SBM blacklisted + Busibee financials=0). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1524 leftover IVAREM JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1524=done + rq_1525 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1524,1524,no,"
        "tick1524 leftover IGS IVAREM residual; KBO 0267.403.264; live JR2025 official NBB WVV VOL-inb 2026-00373329; sourced euros assets 61398227 omzet 34824643 opbr 35143041 pers 12430050 165.8 VTE cash 8106299 debt 37235254 pnl -2241145; FOI ready 70 split / LT-bank JUMP / capex 16.37m / commissaris fee / IRS / vennoten; TRUE JR2025 after prior Busibee false-alarm; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover IGEMO 1372 / leftover IOK Afvalbeheer / leftover PMBS / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1525 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1167 answered 9 partial 27 total 1215; inventory budgets 44055 commitments 5124 leaderboard 7327 entities 1269 sources 3233; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1524", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1524_logblock.md").read_text(encoding="utf-8")
    if "2026-08-20T00:49:22Z" in block:
        block = block.replace("2026-08-20T00:49:22Z", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
