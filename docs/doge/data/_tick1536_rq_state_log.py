#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1536=done + spawn rq_1537; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1536,"):
        raise SystemExit(f"last row is not rq_1536: {last[:80]!r}")
    if b"rq_1537," in raw:
        raise SystemExit("rq_1537 already present — concurrent tick?")
    done = (
        "rq_1536,Erfpunt JR2025 leftover IOED dual residual,hole_fill,5,done,L5,igs_erfp,"
        "Tick 1536 took leftover recognized IOED Erfpunt 0860.274.885 live official NBB WVV VKT-kap 2026-00165556 Initial 16p 55040; assets 438711 bruto 700561 pers 677959 7.8 VTE cash 61449 debt 297897 expl PROFIT 8742 PnL LOSS 929; FOI ready not sent. Leftover AGB/Bosgroep still unpublished this tick so leftover IOED with live JR2025 taken. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1537 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads.,,"
        f"{TS},{TS},"
        "tick1536 Erfpunt leftover IOED residual; official NBB WVV VKT-kap 2026-00165556 Initial 16p 55040; assets 438711 bruto 700561 pers 677959 7.8 VTE cash 61449 debt 297897 expl PROFIT 8742 PnL LOSS 929; FOI ready not sent; leftover AGB/Bosgroep still unpublished; next 1537 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live\n"
    )
    spawn = (
        "rq_1537,leftover AGB/APB/IGS/Bosgroep/IOED dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1537 after 1536 Erfpunt. Official 11-CAW vein fully exhausted. Do NOT redo Erfpunt. Do NOT redo CAW NWVL. Do NOT redo CAW ZWVL. Do NOT redo CAW CWVL. Do NOT redo CAW Oost-Vlaanderen. Do NOT redo CAW Limburg. Do NOT redo CAW Oost-Brabant. Do NOT redo CAW Halle-Vilvoorde. Do NOT redo CAW Rivierenland. Do NOT redo CAW Brussel. Do NOT redo CAW De Kempen. Do NOT redo CAW Antwerpen. Do NOT redo IVAREM. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (Inovant still 404; Atlas 404 this tick). Leftover Puyenbroeck only if a separate APB 2025 PDF now downloads (302 this tick; no APB JR2025 PDF). Leftover AGB Hoogstraten/Eeklo/Harelbeke unused no AGB JR2025 this tick. Leftover Bosgroep VZWs only if a 2025 CDN now appears (Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR). Leftover IOED PORTIVA / WinAr / Hydra / Stuifzand / VARIANT / Viersprong / Schelde-Durme / Brugge en Ommeland 0554.701.428 only if a 2025 CDN now appears. Leftover Dommelhof 0777.495.085 / leftover RL West-Vlaamse Hart 0800.422.125 still no JR. Leftover Dijk92 0806.383.071 deposit 2026-00377886 VKT-VZW year-end 30.12.2025 exists on NBB consult but CDN 403 this tick — retry GET. Leftover Zuidrand 0672.985.901 / leftover Zender 0822.146.066 still JR2024. Leftover Steunfonds CAW ZWVL 0860553415 still no JR (verify public leftover not private). Live-PDF recognized CGG vein fully exhausted (1507-1523 taken; leftover CGG DAGG STOPPED). Named leftover official-41 vein from 1464 fully exhausted. Prefer VOL-VZW/VOL-inb over VKT. Confirm NOT already in entities. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (Thuisrand 1474). Do NOT redo Erfpunt / CAW NWVL / CAW ZWVL / CAW CWVL / CAW Oost-Vlaanderen / CAW Limburg / CAW Oost-Brabant / CAW Halle-Vilvoorde / CAW Rivierenland / CAW Brussel / CAW De Kempen / CAW Antwerpen / IVAREM / leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover official-41 1464-1505.,,"
        f"{TS},{TS},"
        "spawned after tick1536 leftover Erfpunt JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 2026-00377886 if CDN now 200 / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; leftover AGB/Bosgroep still unpublished as of 1536; official 11-CAW vein fully exhausted; live-PDF CGG vein fully exhausted; Erfpunt TAKEN; CAW NWVL TAKEN; CAW ZWVL TAKEN; CAW CWVL TAKEN; CAW Oost-Vlaanderen TAKEN; CAW Limburg TAKEN; CAW Oost-Brabant TAKEN; CAW Halle-Vilvoorde TAKEN; CAW Rivierenland TAKEN; CAW Brussel TAKEN; CAW De Kempen TAKEN; CAW Antwerpen TAKEN; IVAREM TAKEN; named leftover official-41 vein from 1464 fully exhausted\n"
    )
    for label, row in (("done", done), ("spawn", spawn)):
        n = len(next(csv.reader(io.StringIO(row))))
        if n != 12:
            raise SystemExit(f"{label} ncols {n} != 12")
        fields = next(csv.reader(io.StringIO(row)))
        if any("," in f for f in fields):
            raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1536=done + rq_1537 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1536 leftover recognized IOED Erfpunt residual; KBO 0860.274.885; live JR2025 official NBB WVV VKT-kap 2026-00165556 Initial; sourced euros assets 438711 bruto 700561 pers 677959 7.8 VTE cash 61449 debt 297897 pnl -929 expl PROFIT 8742; FOI ready omzet empty / handelsrecv JUMP / lev JUMP / cash DROP / beleg DROP / prepaid JUMP / pers 62 vs social 102; leftover AGB/Bosgroep still unpublished this tick so leftover IOED with live JR2025 taken; leftover Dijk92 deposit 2026-00377886 exists but CDN 403; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; leftover CGG DAGG STOPPED merged Integra 1515; NOT leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck; next rq_1537 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover Dommelhof/Hart / leftover Steunfonds CAW ZWVL only if leftover public unit with JR2025 now live; named leftover official-41 vein from 1464 fully exhausted; FOI ready 1179 answered 9 partial 27 total 1227; inventory budgets 44547 commitments 5136 leaderboard 7339 entities 1281 sources 3281; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1536,1536,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1536", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1536_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
