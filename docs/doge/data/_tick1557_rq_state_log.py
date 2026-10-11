#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1557=done + spawn rq_1558; update loop_state; append loop_log.
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
    if not last.startswith(b"rq_1557,"):
        raise SystemExit(f"last row is not rq_1557: {last[:80]!r}")
    if b"rq_1558," in raw:
        raise SystemExit("rq_1558 already present — concurrent tick?")
    done = (
        "rq_1557,VLHORA JR2025 leftover public koepel dual residual,hole_fill,5,done,L5,son_vlho,"
        "Tick 1557 took leftover public koepel VLHORA 0650.536.537 live official NBB VKT-VZW deposit 2026-00079599 25p 246879; bruto 1200770 omzet empty 73 empty pers 1052307 vte 13.2 expl 144241 PROFIT pnl 143093 PROFIT assets 11929249 handelsrecv JUMP 7665740 vooruit JUMP 9370719 cash DROP 2972417 lev DROP 439394; FOI ready not sent. Leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished this tick so leftover public koepel with live official JR2025 euros taken. Official KBO resolved on kbo-bce.fgov.be. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo taken HVZ 1537-1547. Do NOT redo Erfpunt. Official 11-CAW vein fully exhausted. Live-PDF CGG vein remains fully exhausted. IVAREM TAKEN 1524. Named leftover official-41 vein from 1464 fully exhausted. Next tick 1558 leftover AGB/Bosgroep/IOED/Dijk92 if JR2025 PDF now downloads else leftover other HVZ/IGS of mined cities. Next every-10 is 1560.,,"
        f"{TS},{TS},"
        "tick1557 VLHORA leftover public koepel residual; official NBB VKT-VZW 25p 246879; KBO 0650.536.537 official; bruto 1200770 pers 1052307 recv JUMP 7665740 vooruit JUMP 9370719; FOI ready not sent; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished; next 1558 leftover AGB/Bosgroep/IOED/Dijk92 if PDF live else leftover other HVZ/IGS; next every-10 is 1560\n"
    )
    spawn = (
        "rq_1558,leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1558 after 1557 VLHORA. Official 11-CAW vein fully exhausted. Live-PDF CGG vein fully exhausted. Official-41 woonmaatschappijen fully exhausted. Do NOT redo VLHORA. Do NOT redo VLIR. Do NOT redo VLUHR. Do NOT redo VLEVA. Do NOT redo VVP. Do NOT redo VVSG. Do NOT redo Inagro. Do NOT redo CREMABRU. Do NOT redo Intradura. Do NOT redo Brandweerzone Oost OVL. Do NOT redo HVZ Fluvia. Do NOT redo HVZ Zuid-West-Limburg. Do NOT redo HVZ Noord-Limburg. Do NOT redo HVZ Westhoek. Do NOT redo HVZ Kempen. Do NOT redo BVLAR. Do NOT redo HVZ Midwest. Do NOT redo HVZ Meetjesland. Do NOT redo HVZ1. Do NOT redo HVZ Taxandria. Do NOT redo HVZ Oost VB. Do NOT redo Erfpunt. Do NOT redo Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA. Leftover AGB/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Bosgroep if 2025 CDN now. Leftover Dijk92 0806.383.071 deposit 2026-00377886 if CDN now 200. Leftover other IOED if 2025 CDN now. Leftover Cultuur Noordrand 0740.822.256 unused leftover of mined Grimbergen but no NBB JR2025 as of 1557. Leftover Zuidrand 0672.985.901 unused leftover of mined Mortsel/Kontich but no NBB JR2025 as of 1557. Leftover IOED Zuid-Hageland 0680.814.294 unused leftover of mined Landen/Zoutleeuw/Geetbets/Kortenaken but no NBB JR2025 as of 1557. Leftover other HVZ of mined cities if official JR2025 PDF with extractable euros now. Else leftover other IGS/IOED/other public unit of a mined parent with live 2025 statutory/BBC/AV PDF with euros. Next every-10 is 1560.,,"
        f"{TS},{TS},"
        "spawned after tick1557 leftover VLHORA JR2025; NEXT leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN 200 / leftover other HVZ if euros now live / leftover other IGS of mined cities; do NOT redo VLHORA / VLIR / VLUHR / VLEVA / VVP / VVSG / Inagro / CREMABRU / Intradura / Brandweerzone Oost OVL / taken HVZ 1537-1547 / Erfpunt / 11-CAW / CGG / official-41 / Veneco / IGEAN / Haviland / IVAREM / IVAGO / ISVAG / IVBO / INCOVO / INTERZA; next every-10 is 1560\n"
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
    print("research_queue surgical rq_1557=done + rq_1558 spawn", before, "->", after)

def loop_state():
    p = DATA / "loop_state.csv"
    notes = (
        "tick1557 leftover public koepel VLHORA residual; KBO 0650.536.537 official kbo-bce.fgov.be; live official NBB VKT-VZW deposit 2026-00079599 25p 246879; sourced euros assets 11929249 bruto 1200770 omzet empty 73 empty pers 1052307 vte 13.2 expl 144241 PROFIT pnl 143093 PROFIT handelsrecv JUMP 7665740 vooruit JUMP 9370719 cash DROP 2972417 lev DROP 439394; FOI ready 73/70/60/61 unpublished VKT / handelsrecv JUMP / vooruit JUMP / cash DROP / lev DROP / AV notulen; leftover AGB/Bosgroep/Dijk92/IOED/remaining-HVZ still unpublished/inzage-only this tick so leftover public koepel with live official JR2025 euros taken; leftover Dijk92 deposit 2026-00377886 still CDN 403; leftover Cultuur Noordrand 0740.822.256 unused leftover of mined Grimbergen but no NBB JR2025; leftover Zuidrand 0672.985.901 unused leftover of mined Mortsel/Kontich but no NBB JR2025; leftover IOED Zuid-Hageland 0680.814.294 unused leftover of mined Landen/Zoutleeuw/Geetbets/Kortenaken but no NBB JR2025; leftover remaining HVZ still inzage-only; official 11-CAW vein remains fully exhausted; live-PDF CGG vein remains fully exhausted; NOT leftover VLIR 1556 / leftover VLUHR 1555 / leftover VLEVA 1554 / leftover VVP 1553 / leftover VVSG 1552 / leftover Inagro 1551 / leftover CREMABRU 1550 / leftover INTRADURA 1549 / leftover Brandweerzone Oost OVL 1548 / leftover taken HVZ 1537-1547 / leftover Erfpunt 1536 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505; next rq_1558 leftover AGB/APB of mined cities if PDF live else leftover Bosgroep / leftover other IOED / leftover Dijk92 if CDN now 200 / leftover other HVZ if official JR2025 with euros now live / leftover other IGS; next every-10 is 1560; continuous hole_fill"
    )
    if "," in notes:
        raise SystemExit("loop_state notes contain comma")
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1557,1557,no,{notes}\n",
        encoding="utf-8",
    )
    print("loop_state 1557", TS)

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1557_logblock.md").read_text(encoding="utf-8")
    block = block.replace("2026-08-20TPLACEHOLDERZ", TS, 1)
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended", TS)

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
