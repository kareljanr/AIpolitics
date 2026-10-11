#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1531=done + spawn rq_1532; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1531,"):
        raise SystemExit(f"last row is not rq_1531: {last[:80]!r}")
    if b"rq_1532," in raw:
        raise SystemExit("rq_1532 already present — concurrent tick?")
    done = (
        "rq_1531,CAW Limburg JR2025 leftover zorg EVA dual residual,hole_fill,5,done,L5,caw_cwlm,"
        "Tick 1531 took leftover recognized Flemish CAW Limburg 0464.328.310 live official NBB WVV VOL-VZW 2026-00099651 Initial 49p 528761; assets 17396760 opbr 25346747 pers 20148522 271.8 VTE cash 2737774 debt 8313821; FOI ready not sent. Seventh per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 and CAW Oost-Brabant 1530. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1532 leftover other regional CAWs.,,"
        f"{TS},{TS},"
        "tick1531 CAW Limburg leftover zorg EVA residual; official NBB WVV VOL-VZW 2026-00099651 Initial 49p 528761; assets 17396760 opbr 25346747 pers 20148522 271.8 VTE cash 2737774 debt 8313821; FOI ready not sent; next 1532 leftover regional CAWs\n"
    )
    spawn = (
        "rq_1532,leftover AGB/APB/CAW/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1532 after 1531 CAW Limburg. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover other regional CAWs (4 remaining) only if a 2025 CDN now appears — leftover CAW Oost-Vlaanderen 0508.774.601 deposit 2026-00117344 LIVE unused (1969916; Gent; prefix cwov) / leftover CAW Centraal-West-Vlaanderen 0464.580.708 deposit 2026-00088320 LIVE unused (1834911; Izegem; prefix cwcw) / leftover CAW Zuid-West-Vlaanderen 0464.275.949 deposit 2026-00069501 LIVE unused (612502; Kortrijk; prefix cwzw) / leftover CAW Noord-West-Vlaanderen 0464.229.231 (no unused live PDF confirmed tick 1529). Prefer first leftover CAW with live PDF (Oost-Vlaanderen). Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CAW Limburg / CAW Oost-Brabant / CAW Halle-Vilvoorde / CAW Rivierenland / CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / leftover Woonmaatschappij Rivierenland / leftover Wonen in Limburg / leftover AGB MAC Mechelen / leftover AGA Asse / leftover AGB Vilvoorde / leftover Inter-Vilvoordse / leftover Woonpunt Zennevallei / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1531 leftover CAW Limburg JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (Oost-Vlaanderen 0508.774.601 2026-00117344 LIVE / CWVL 0464.580.708 2026-00088320 LIVE / ZWVL 0464.275.949 2026-00069501 LIVE / NWVL 0464.229.231 no live PDF confirmed) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; CAW Limburg TAKEN; CAW Oost-Brabant TAKEN; CAW Halle-Vilvoorde TAKEN; CAW Rivierenland TAKEN; CAW Brussel TAKEN; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1531=done + rq_1532 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1531 leftover recognized Flemish CAW Limburg residual; KBO 0464.328.310; live JR2025 official NBB WVV VOL-VZW 2026-00099651 Initial; sourced euros assets 17396760 opbr 25346747 omzet 2047768 73 23037493 pers 20148522 271.8 VTE cash 2737774 debt 8313821 pnl 117423; FOI ready 73 split / cash DROP / handelsrecv JUMP / other recv JUMP / other ST JUMP / accrued DROP / IVA JUMP / in-aanbouw JUMP / diensten JUMP / commissaris fee; seventh per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 CAW Brussel 1527 CAW Rivierenland 1528 CAW Halle-Vilvoorde 1529 and CAW Oost-Brabant 1530; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover CGG Integra 1515 / leftover CGG Kohesi 1523 / leftover Wonen in Limburg 1486 / leftover LeefGoed 1481 / leftover CAW Oost-Brabant 1530 / leftover CAW Halle-Vilvoorde 1529 / leftover CAW Rivierenland 1528 / leftover CAW Brussel 1527 / leftover CAW De Kempen 1526 / leftover CAW Antwerpen 1525 / leftover umbrella caw_vl / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1532 leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (Oost-Vlaanderen 0508.774.601 2026-00117344 LIVE / CWVL 0464.580.708 2026-00088320 LIVE / ZWVL 0464.275.949 2026-00069501 LIVE / NWVL 0464.229.231 no live PDF) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1174 answered 9 partial 27 total 1222; inventory budgets 44350 commitments 5131 leaderboard 7334 entities 1276 sources 3261; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1531,1531,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1531", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1531_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
