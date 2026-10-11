#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1528=done + spawn rq_1529; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1528,"):
        raise SystemExit(f"last row is not rq_1528: {last[:80]!r}")
    if b"rq_1529," in raw:
        raise SystemExit("rq_1529 already present — concurrent tick?")
    done = (
        "rq_1528,CAW Rivierenland JR2025 leftover zorg EVA dual residual,hole_fill,5,done,L5,caw_cwrv,"
        "Tick 1528 took leftover recognized Flemish CAW Rivierenland 0466.852.882 live official NBB WVV VOL-VZW 2026-00090859 Initial 50p 3097588; assets 9362853 opbr 8432403 pers 7006469 95.1 VTE cash 312739 debt 3564445; FOI ready not sent. Fourth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 and CAW Brussel 1527. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next every-10 is 1530.,,"
        f"{TS},{TS},"
        "tick1528 CAW Rivierenland leftover zorg EVA residual; official NBB WVV VOL-VZW 2026-00090859 Initial 50p 3097588; assets 9362853 opbr 8432403 pers 7006469 95.1 VTE cash 312739 debt 3564445; FOI ready not sent; next every-10 1530\n"
    )
    spawn = (
        "rq_1529,leftover AGB/APB/CAW/IGS dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1529 after 1528 CAW Rivierenland. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. EVERY-10 was 1520 next 1530. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover other regional CAWs (7 remaining) only if a 2025 CDN now appears — leftover CAW Halle-Vilvoorde 0469.702.605 / leftover CAW Oost-Brabant 0465.044.031 / leftover CAW Limburg 0464.328.310 / leftover CAW Oost-Vlaanderen 0508.774.601 / leftover CAW Noord-West-Vlaanderen 0464.229.231 / leftover CAW Centraal-West-Vlaanderen 0464.580.708 / leftover CAW Zuid-West-Vlaanderen 0464.275.949 (official names/KBOs from Vlaams Parlement pfile 1694090; confirm unused + live PDF — do NOT invent deposits). Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (still 302 this tick). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo CAW Rivierenland / CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / CGG Kohesi / CGG Mandel en Leie / CGG Brussel / CGG PassAnt / CGG Andante / CGG Largo / CGG Ahasverus / CGG Kempen / CGG Integra / CGG De Pont / CGG Prisma / CGG VAGGA / CGG Adentro / CGG ZOV / CGG VBO / CGG SDW / CGG NWVL / leftover CGG DAGG / leftover Woonmaatschappij Rivierenland / leftover AGB MAC Mechelen / official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1528 leftover CAW Rivierenland JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (Halle-Vilvoorde 0469.702.605 / Oost-Brabant 0465.044.031 / Limburg 0464.328.310 / Oost-Vlaanderen 0508.774.601 / NWVL 0464.229.231 / CWVL 0464.580.708 / ZWVL 0464.275.949) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; live-PDF CGG vein fully exhausted; CAW Rivierenland TAKEN; CAW Brussel TAKEN; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1530\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1528=done + rq_1529 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1528,1528,no,"
        "tick1528 leftover recognized Flemish CAW Rivierenland residual; KBO 0466.852.882; live JR2025 official NBB WVV VOL-VZW 2026-00090859 Initial; sourced euros assets 9362853 opbr 8432403 omzet 371409 73 7780184 pers 7006469 95.1 VTE cash 312739 debt 3564445 pnl 11558; FOI ready 73 split / cash DROP / beleg DROP / 74 JUMP / other recv JUMP / vooruit JUMP / 70 category empty / commissaris fee / expl LOSS; fourth per-CAW L5 after CAW Antwerpen 1525 CAW De Kempen 1526 and CAW Brussel 1527; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover Woonmaatschappij Rivierenland 1465 / leftover CGG De Pont 1514 / leftover IVAREM 1524 / leftover CAW Antwerpen 1525 / leftover CAW De Kempen 1526 / leftover CAW Brussel 1527 / leftover umbrella caw_vl / leftover CGG 1507-1523 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1529 leftover AGB/APB of mined cities if PDF live else leftover other regional CAWs if JR2025 live (Halle-Vilvoorde 0469.702.605 / Oost-Brabant 0465.044.031 / Limburg 0464.328.310 / Oost-Vlaanderen 0508.774.601 / NWVL 0464.229.231 / CWVL 0464.580.708 / ZWVL 0464.275.949) else leftover Bosgroep / leftover IOED / leftover Dommelhof/Hart only if JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1171 answered 9 partial 27 total 1219; inventory budgets 44219 commitments 5128 leaderboard 7331 entities 1273 sources 3249; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1528", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1528_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
