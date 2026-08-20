#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1537=done + spawn rq_1538; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1537,"):
        raise SystemExit(f"last row is not rq_1537: {last[:80]!r}")
    if b"rq_1538," in raw:
        raise SystemExit("rq_1538 already present — concurrent tick?")
    done = (
        "rq_1537,HVZ Oost Vlaams-Brabant JR2025 leftover IGS dual residual,hole_fill,5,done,L5,igs_hvzo,"
        "Tick 1537 took leftover IGS hulpverleningszone HVZ Oost Vlaams-Brabant 0500.928.982 live official zoneraad JR2025 besluit 2026_ZR_00026 3p 130439; assets 48137974 expl 4279776 pnl PROFIT 3557913 uitz_kosten 6887696; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 besluit taken. Do NOT redo HVZ Oost. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1538 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover other HVZ of mined cities if a 2025 official PDF now downloads.,,"
        f"{TS},{TS},"
        "tick1537 HVZ Oost leftover IGS residual; official zoneraad JR2025 besluit 2026_ZR_00026 3p 130439; assets 48137974 expl 4279776 pnl PROFIT 3557913 uitz_kosten 6887696; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED still unpublished; next 1538 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover other HVZ\n"
    )
    spawn = (
        "rq_1538,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1538 after 1537 HVZ Oost Vlaams-Brabant. Official 11-CAW vein fully exhausted. Do NOT redo HVZ Oost. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (Inovant still 403/404; Atlas 403/404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (302 this tick; no APB JR2025 PDF). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR). Leftover IOED PORTIVA / WinAr 0811.517.440 / Hydra / Stuifzand / VARIANT / Viersprong 0809.450.251 / Brugge en Ommeland 0554.701.428 / Polderrand 0649.827.150 / Berg en Nete 0671.761.919 / Zuid-Hageland 0680.814.294 only if a 2025 CDN now appears (Busibee financials=0 this tick). Leftover Dommelhof 0777.495.085 / leftover RL West-Vlaamse Hart 0800.422.125 still no JR. Leftover Dijk92 0806.383.071 deposit 2026-00377886 still CDN 403 this tick (known-good Erfpunt CDN 200; Busibee last JR 2024) — retry GET. Leftover Zuidrand 0672.985.901 / leftover Zender 0822.146.066 still JR2024. Leftover Steunfonds CAW ZWVL 0860553415 still no JR (verify public leftover not private). Leftover other HVZ of mined cities if a 2025 official PDF now downloads (Brandweerzone Centrum 0500.927.497 / Rivierenland / Kempen 0500.915.126 / Waasland / HVZ1 WVL 0500.929.279). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer live official JR2025 PDF. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo HVZ Oost / Erfpunt / CAW NWVL / CAW ZWVL / CAW CWVL / CAW Oost-Vlaanderen / CAW Limburg / CAW Oost-Brabant / CAW Halle-Vilvoorde / CAW Rivierenland / CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1537 leftover HVZ Oost JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 2026-00377886 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 PDF now live / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; leftover AGB/Bosgroep/Dijk92/IOED still unpublished as of 1537; official 11-CAW vein fully exhausted; live-PDF CGG vein fully exhausted; HVZ Oost TAKEN; Erfpunt TAKEN; CAW NWVL TAKEN; CAW ZWVL TAKEN; CAW CWVL TAKEN; CAW Oost-Vlaanderen TAKEN; CAW Limburg TAKEN; CAW Oost-Brabant TAKEN; CAW Halle-Vilvoorde TAKEN; CAW Rivierenland TAKEN; CAW Brussel TAKEN; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1537=done + rq_1538 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1537 leftover IGS hulpverleningszone HVZ Oost Vlaams-Brabant residual; KBO 0500.928.982; live JR2025 official zoneraad besluit 2026_ZR_00026 22.04.2026; sourced euros assets 48137974 expl 4279776 pnl 3557913 uitz_kosten 6887696 uitz_opbr 6165833 begroting_gewone 6378403; FOI ready Rekening_2025_deel_1/2/3 unpublished / pers VTE / city-share 32 gemeenten / cash debt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official JR2025 besluit taken; leftover Dijk92 deposit 2026-00377886 still CDN 403; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover Brandweerzone Antwerpen / leftover CAW Oost-Brabant 1530 / leftover CGG VBO 1509 / leftover Kanvaz / leftover Erfpunt 1536 / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1538 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover other HVZ of mined cities if official JR2025 now live / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1180 answered 9 partial 27 total 1228; inventory budgets 44556 commitments 5137 leaderboard 7340 entities 1282 sources 3285; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1537,1537,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1537", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1537_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
