#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1548=done + spawn rq_1549; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1548,"):
        raise SystemExit(f"last row is not rq_1548: {last[:80]!r}")
    if b"rq_1549," in raw:
        raise SystemExit("rq_1549 already present — concurrent tick?")
    done = (
        "rq_1548,HVZ Oost OVL JR2025 leftover IGS dual residual,hole_fill,5,done,L5,igs_hvoo,"
        "Tick 1548 took leftover IGS hulpverleningszone Brandweerzone Oost Oost-Vlaanderen 0500.927.893 live official zoneraad 22.05.2026 Beknopte lijst Vaststelling rekening 2025 7p 1126629; balans 13589234 resultaat_gewone_begroting 2011808 resultaat_gewone_boek 2481692 resultaat_buit_begroting -2897489 resultaat_buit_boek 703832 pnl_nadelig 25226; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official rekening 2025 euros taken. Official KBO resolved on kbo-bce.fgov.be. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB (do NOT reuse hvzo). Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1549 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover other HVZ of mined cities if a 2025 official PDF with euros now downloads (Rivierenland still inzage-only / Waasland still no euros / Centrum / Oost-Limburg JV2025 live no clean spend table / Rand JR2025 unpublished / Vlaams-Brabant West / Zuid-Oost inzage-only). 1549 is NOT every-10; 1550 MUST refresh progress.,,"
        f"{TS},{TS},"
        "tick1548 HVZ Oost OVL leftover IGS residual; official zoneraad 22.05.2026 7p 1126629; KBO 0500.927.893 official; balans 13589234 resultaat_gewone 2011808; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; next 1549 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover other HVZ; 1549 NOT every-10; 1550 MUST refresh progress\n"
    )
    spawn = (
        "rq_1549,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1549 after 1548 Brandweerzone Oost OVL. Official 11-CAW vein fully exhausted. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (Inovant still 301/404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (302 this tick). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR). Leftover IOED PORTIVA / WinAr / Hydra / Stuifzand / VARIANT / Viersprong / Brugge en Ommeland 0554.701.428 / Polderrand / Berg en Nete / Zuid-Hageland only if a 2025 CDN now appears. Leftover Dommelhof 0777.495.085 / leftover RL West-Vlaamse Hart 0800.422.125 still no JR. Leftover Dijk92 0806.383.071 deposit 2026-00377886 still CDN 403 this tick — retry GET. Leftover Zuidrand 0672.985.901 / leftover Zender 0822.146.066 still JR2024. Leftover Steunfonds CAW ZWVL 0860553415 still no JR (verify public leftover not private). Leftover other HVZ of mined cities if a 2025 official PDF now downloads with sourced euros (Rivierenland 0500.913.839 still inzage-only / Waasland still no euros / Brandweerzone Centrum 0500.927.497 still no JR2025 / leftover HVZ Oost-Limburg JV2025 now live no clean spend table / leftover HVZ Rand JR2025 unpublished / leftover HVZ Vlaams-Brabant West / leftover HVZ Zuid-Oost 2026_ZR_00032 inzage-only). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer live official JR2025 PDF. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Brandweerzone Oost OVL / HVZ Fluvia / HVZ Zuid-West-Limburg / HVZ Noord-Limburg / HVZ Westhoek / HVZ Kempen / BVLAR / HVZ Midwest / HVZ Meetjesland / HVZ1 / HVZ Taxandria / HVZ Oost VB / Erfpunt / CAW vein / IVAREM / leftover IVBO 1352 / leftover official-41 1464-1505. 1549 is NOT every-10; 1550 MUST refresh progress.,,"
        f"{TS},{TS},"
        "spawned after tick1548 leftover HVZ Oost OVL JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 2026-00377886 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 PDF with euros now live (Rivierenland/Waasland still no euros / Centrum / Oost-Limburg JV2025 live no clean spend / Rand/Vlaams-Brabant West/Zuid-Oost inzage-only) / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; leftover AGB/Bosgroep/Dijk92/IOED still unpublished as of 1548; official 11-CAW vein fully exhausted; live-PDF CGG vein fully exhausted; Brandweerzone Oost OVL TAKEN; HVZ Fluvia TAKEN; HVZ Zuid-West-Limburg TAKEN; HVZ Noord-Limburg TAKEN; HVZ Westhoek TAKEN; HVZ Kempen TAKEN; BVLAR TAKEN; HVZ Midwest TAKEN; HVZ Meetjesland TAKEN; HVZ1 TAKEN; HVZ Taxandria TAKEN; HVZ Oost VB TAKEN; Erfpunt TAKEN; CAW vein TAKEN; IVAREM TAKEN; leftover IVBO already mined; named leftover official-41 vein from 1464 fully exhausted; 1549 is NOT every-10; 1550 MUST refresh progress\n"
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
    print("research_queue surgical rq_1548=done + rq_1549 spawn", before, "->", after)

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1548 leftover IGS hulpverleningszone Brandweerzone Oost Oost-Vlaanderen residual; KBO 0500.927.893 official kbo-bce.fgov.be; live official zoneraad 22.05.2026 Beknopte lijst 7p 1126629; sourced euros balans 13589234 resultaat_gewone_begroting 2011808 resultaat_gewone_boek 2481692 resultaat_buit_begroting -2897489 resultaat_buit_boek 703832 pnl_nadelig 25226; FOI ready full rekening verslag unpublished / uitgaven ontvangsten gewone / pers werking / operational VTE / per-gemeente split / cash debt equity / BBC M2; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official rekening 2025 euros taken; leftover Dijk92 deposit 2026-00377886 still CDN 403; leftover Rivierenland still inzage-only; leftover Waasland still no euros; leftover Centrum still no JR2025 euros; leftover Oost-Limburg JV2025 live no clean spend table; leftover Zuid-Oost 2026_ZR_00032 inzage-only; leftover Rand JR2025 unpublished; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover HVZ Oost VB 1537 / leftover HVZ Fluvia 1547 / leftover HVZ ZWL 1546 / leftover HVZ Noord-Limburg 1545 / leftover HVZ Westhoek 1544 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 1539 / leftover HVZ Taxandria 1538 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover HVZ Zuid-Oost / leftover Dijk92 / leftover Erfpunt 1536 / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1549 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 with euros now live / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; 1549 is NOT every-10; 1550 MUST refresh progress; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1548,1548,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1548", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1548_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
