#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1489=done + spawn rq_1490; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:40:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1489,"):
        raise SystemExit(f"last row is not rq_1489: {last[:80]!r}")
    if b"rq_1490," in raw:
        raise SystemExit("rq_1490 already present — concurrent tick?")
    done = (
        "rq_1489,Inter-Vilvoordse JR2025 leftover dual residual,hole_fill,5,done,L5,wm_ivlv,"
        "Tick 1489 took leftover official-41 woonmaatschappij Inter-Vilvoordse 0400.676.613 live official NBB WVV VOL-inb 2026-00138038 after leftover AGB/APB hunt (Inovant/Atlas still 404/403). Do NOT redo Inter-Vilvoordse. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 PDF actually downloads. Leftover OTHER provincial APBs (Puyenbroeck still 302). Leftover unmined IGS/RL/Bosgroepen/daughters/woonmaatschappijen if a 2025 CDN or official AV PDF is live. Leftover other official-41 of mined cities if JR2025 live (Zetus 0405.196.516 deposit 2026-00117246 live unused). Leftover IOED/cultuur-IGS only if a 2025 CDN now appears. IVAREM/Hart/Dommelhof only if a true JR2025 statutory PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / AGB Tienen / AGB Menen / AGB Vilvoorde / Erfgoed Rupelstreek IOED 1431 / RL Vlaamse Ardennen 1437 / leftover cultuur-IGS Berg en Nete / SOLVA. NEXT TICK 1490 IS EVERY-10.,,"
        f"{TS},{TS},"
        "tick1489 Inter-Vilvoordse leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00138038 57p 4820480; assets 175606699 omzet 9370627 pers 1996874 pnl 961462 cash 22766208 debt 135881516; FOI ready not sent\n"
    )
    spawn = (
        "rq_1490,Every-10 progress coverage percent plus waste top10,hole_fill,5,open,L5,,"
        "EVERY-10 at 1490. Refresh docs/doge/data/progress_every_10_ticks.md (layers A-E percent of 3477.956bn TE) and docs/doge/data/doge_waste_top10_current.md (top 10 by priority_index). Then leftover AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1489 done including Inter-Vilvoordse 1489 leftover woonmaatschappij live official NBB WVV / Woonschakel 1488 leftover woonmaatschappij live official NBB WVV / De Voorkempen 1487 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 PDF actually downloads. Leftover OTHER provincial APBs (Puyenbroeck still 302). Leftover Bosgroep VZWs only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Inter-Vilvoordse TAKEN 1489; Woonschakel TAKEN 1488; De Voorkempen TAKEN 1487; Wonen in Limburg TAKEN 1486; Woonpunt Zennevallei TAKEN 1485; !Mpuls TAKEN 1484; WoonST TAKEN 1483; stek92 TAKEN 1482; LeefGoed TAKEN 1481; Kanvaz TAKEN 1480; WMVA TAKEN 1479; Woonboog TAKEN 1478; Woonveer TAKEN 1477; Woonkade TAKEN 1476; Woonstroom TAKEN 1475; Thuisrand TAKEN 1474; Vivendo TAKEN 1473; SW+ TAKEN 1472; Woonhaven TAKEN 1471; leftover Zetus 0405.196.516 deposit 2026-00117246 live unused; leftover other official-41 only if JR2025 live). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / AGB Tienen / AGB Menen / AGB Vilvoorde / Erfgoed Rupelstreek IOED 1431 / RL Vlaamse Ardennen 1437 / leftover cultuur-IGS Berg en Nete / SOLVA. Next every-10 after 1490 is 1500.,,"
        f"{TS},{TS},"
        "spawned after tick1489 Inter-Vilvoordse leftover woonmaatschappij residual; NEXT IS EVERY-10 — refresh progress_every_10_ticks.md + doge_waste_top10_current.md; then leftover APB Inovant/Atlas if PDF live else leftover Zetus 2026-00117246 / leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep\n"
    )
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1489=done + rq_1490 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T19:40:00Z,rq_1489,1489,no,"
        "tick1489 Inter-Vilvoordse leftover woonmaatschappij residual; KBO 0400.676.613; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 175606699 omzet 9370627 pers 1996874 20.8 VTE pnl 961462 equity 38667098 cash 22766208 debt 135881516 capex 12018842 dividend 0; FOI ready omzet 9.37m / pers 2.00m 20.8 VTE / debt 135.88m / cash 22.77m JUMP / PnL DROP 0.96m / dividend 0 / 1 VE; NOT leftover AGB Vilvoorde / leftover Zetus / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1490 EVERY-10 then leftover APB Inovant/Atlas if PDF live else leftover Zetus 2026-00117246 / leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1132 answered 9 partial 27 total 1180; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1489")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1489_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
