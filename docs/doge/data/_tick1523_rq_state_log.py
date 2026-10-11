#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1523=done + spawn rq_1524; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1523,"):
        raise SystemExit(f"last row is not rq_1523: {last[:80]!r}")
    if b"rq_1524," in raw:
        raise SystemExit("rq_1524 already present — concurrent tick?")
    done = (
        "rq_1523,CGG Kohesi JR2025 leftover recognized CGG dual residual,hole_fill,5,done,L5,cgg_cgkh,"
        "Tick 1523 took leftover recognized Flemish CGG CGG Kohesi 0472.466.907 live official NBB WVV VOL-VZW 2026-00242985 51p 1092286; assets 7706860 opbr 8794445 pers 6248426 73.4 VTE cash 1981073 debt 2941952; FOI ready not sent. NEW unused recognized CGG not in 1507-1522 list. Live-PDF CGG vein now fully exhausted. Do NOT redo CGG Kohesi. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1523 CGG Kohesi leftover recognized CGG residual; official NBB WVV VOL-VZW 2026-00242985 51p 1092286; assets 7706860 opbr 8794445 pers 6248426 73.4 VTE cash 1981073 debt 2941952; FOI ready not sent; live-PDF CGG vein fully exhausted; next every-10 1530\n"
    )
    spawn = (
        "rq_1524,leftover AGB/APB/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1524 after 1523 CGG Kohesi. Do NOT redo CGG Kohesi. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still fail this tick). Leftover AGB Hoogstraten/Ravels/Rijkevorsel/Eeklo/Zelzate/Laarne/Kuurne/Avelgem/Spiere/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / WV Blankenberge / Vitare / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1523 leftover CGG Kohesi JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; live-PDF CGG vein fully exhausted; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1523=done + rq_1524 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1523,1523,no,"
        "tick1523 leftover recognized Flemish CGG CGG Kohesi residual; NEW unused recognized CGG not in 1507-1522 list; KBO 0472.466.907; live JR2025 official NBB WVV VOL-VZW 2026-00242985; sourced euros assets 7706860 opbr 8794445 pers 6248426 73.4 VTE cash 1981073 debt 2941952 pnl -5036; FOI ready 73 split / cash JUMP / beleg DROP / other ST JUMP / expl DROP / PnL LOSS / diensten JUMP; live-PDF CGG vein now fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover CGG Integra 1515 / leftover CGG Mandel en Leie 1522 / leftover CGG Brussel 1521 / leftover CGG PassAnt 1520 / leftover CGG Andante 1519 / leftover CGG Largo 1518 / leftover CGG Ahasverus 1517 / leftover CGG Kempen 1516 / leftover CGG De Pont 1514 / leftover CGG Prisma 1513 / leftover CGG VAGGA 1512 / leftover CGG Adentro 1511 / leftover CGG ZOV 1510 / leftover CGG VBO 1509 / leftover CGG SDW 1508 / leftover CGG NWVL 1507 / leftover CGG umbrella / leftover official-41 1464-1505 / leftover AGB Kortrijk / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1524 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover IOED / leftover IVAREM/Hart/Dommelhof only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1166 answered 9 partial 27 total 1214; inventory budgets 44016 commitments 5123 leaderboard 7326 entities 1268 sources 3229; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1523", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1523_logblock.md").read_text(encoding="utf-8")
    if "2026-08-20T00:40:35Z" in block:
        block = block.replace("2026-08-20T00:40:35Z", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
