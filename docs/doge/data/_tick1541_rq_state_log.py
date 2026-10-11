#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1541=done + spawn rq_1542; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1541,"):
        raise SystemExit(f"last row is not rq_1541: {last[:80]!r}")
    if b"rq_1542," in raw:
        raise SystemExit("rq_1542 already present — concurrent tick?")
    done = (
        "rq_1541,HVZ Midwest JR2025 leftover IGS dual residual,hole_fill,5,done,L5,igs_hvmw,"
        "Tick 1541 took leftover IGS hulpverleningszone HVZ Midwest 0500.929.378 live official zoneraad JR2025 overzicht 27.03.2026 10p 353741; assets 20266035 expl 794672 pnl LOSS 257322 uitz LOSS 1051994 equity 18804221 debt 1461814 vastgelegd_gewone 14801789; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 zoneraad overzicht taken. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost. Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1542 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover other HVZ of mined cities if a 2025 official PDF with euros now downloads (Rivierenland still inzage-only / Waasland 2026_ZR_00030 no euros / Kempen no JR / Centrum no JR2025 / Fluvia no JR2025).,,"
        f"{TS},{TS},"
        "tick1541 HVZ Midwest leftover IGS residual; official zoneraad JR2025 overzicht 27.03.2026 10p 353741; assets 20266035 expl 794672 pnl LOSS 257322 uitz LOSS 1051994; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; next 1542 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover other HVZ\n"
    )
    spawn = (
        "rq_1542,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1542 after 1541 HVZ Midwest. Official 11-CAW vein fully exhausted. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (Inovant still 404/403; Atlas 000/403 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (302 this tick; no APB JR2025 PDF). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR). Leftover IOED PORTIVA / WinAr / Hydra / Stuifzand / VARIANT / Viersprong / Brugge en Ommeland 0554.701.428 / Polderrand / Berg en Nete / Zuid-Hageland only if a 2025 CDN now appears. Leftover Dommelhof 0777.495.085 / leftover RL West-Vlaamse Hart 0800.422.125 still no JR. Leftover Dijk92 0806.383.071 deposit 2026-00377886 still CDN 403 this tick (known-good Erfpunt CDN 200) — retry GET. Leftover Zuidrand 0672.985.901 / leftover Zender 0822.146.066 still JR2024. Leftover Steunfonds CAW ZWVL 0860553415 still no JR (verify public leftover not private). Leftover other HVZ of mined cities if a 2025 official PDF now downloads with sourced euros (Rivierenland 0500.913.839 besluit still inzage-only / Waasland 2026_ZR_00030 names Rekening 2025 but no euros / Brandweerzone Centrum 0500.927.497 still no JR2025 / Kempen 0500.915.126 / Fluvia 0500.929.774 / leftover Brandweerzone Vlaamse Ardennen). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer live official JR2025 PDF. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo HVZ Midwest / HVZ Meetjesland / HVZ1 / HVZ Taxandria / HVZ Oost / Erfpunt / CAW NWVL / CAW ZWVL / CAW CWVL / CAW Oost-Vlaanderen / CAW Limburg / CAW Oost-Brabant / CAW Halle-Vilvoorde / CAW Rivierenland / CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / leftover IVBO 1352 / leftover official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1541 leftover HVZ Midwest JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 2026-00377886 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 PDF with euros now live (Rivierenland/Waasland still no euros / Kempen/Fluvia/Centrum/Vlaamse Ardennen) / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; leftover AGB/Bosgroep/Dijk92/IOED still unpublished as of 1541; official 11-CAW vein fully exhausted; live-PDF CGG vein fully exhausted; HVZ Midwest TAKEN; HVZ Meetjesland TAKEN; HVZ1 TAKEN; HVZ Taxandria TAKEN; HVZ Oost TAKEN; Erfpunt TAKEN; CAW vein TAKEN; IVAREM TAKEN; leftover IVBO already mined; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1550\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    before = len(raw)
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    after = p.stat().st_size
    if after < 60_000_000:
        raise SystemExit(f"research_queue shrank unexpectedly {before} -> {after}")
    print("research_queue surgical rq_1541=done + rq_1542 spawn", before, "->", after)

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1541 leftover IGS hulpverleningszone HVZ Midwest residual; KBO 0500.929.378; live JR2025 official zoneraad overzicht 27.03.2026 10p 353741; sourced euros assets 20266035 expl 794672 pnl -257322 uitz -1051994 equity 18804221 debt 1461814 vastgelegd_gewone 14801789; FOI ready full rekening verslag unpublished / pers VTE / city-share / cash omzet; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 zoneraad overzicht taken; leftover Dijk92 deposit 2026-00377886 still CDN 403; leftover Rivierenland still inzage-only; leftover Waasland 2026_ZR_00030 no euros; leftover Kempen/Fluvia/Centrum still no JR2025 euros; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Kempen / leftover HVZ Fluvia / leftover DVV Midwest / leftover Thuiswest 1493 / leftover Motena Roeselare / leftover CGG Largo 1518 / leftover Erfpunt 1536 / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1542 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 with euros now live / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; next every-10 is 1550; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1541,1541,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1541", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1541_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
