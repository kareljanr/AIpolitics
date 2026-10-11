#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1491=done + spawn rq_1492; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T19:55:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1491,"):
        raise SystemExit(f"last row is not rq_1491: {last[:80]!r}")
    if b"rq_1492," in raw:
        raise SystemExit("rq_1492 already present — concurrent tick?")
    done = (
        "rq_1491,Ons Onderdak JR2025 leftover dual residual,hole_fill,5,done,L5,wm_onod,"
        "Tick 1491 took leftover official-41 woonmaatschappij Ons Onderdak 0405.501.570 live official NBB WVV VOL-inb 2026-00189814 after leftover AGB/APB hunt (Inovant/Atlas still 403/404). Do NOT redo Ons Onderdak. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 PDF actually downloads. Leftover OTHER provincial APBs (Puyenbroeck still 302). Leftover unmined IGS/RL/Bosgroepen/daughters/woonmaatschappijen if a 2025 CDN or official AV PDF is live. Leftover other official-41 of mined cities if JR2025 live (Woonsprong / Woonstart / Thuiswest / Meetjesland / de Thuisbouwer / Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen / IJzer en Zee). Leftover IOED/cultuur-IGS only if a 2025 CDN now appears. IVAREM/Hart/Dommelhof only if a true JR2025 statutory PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / AGB Vauban Ieper / AGB Musea Ieper / AGB Tienen / AGB Menen / AGB Vilvoorde / AGB Blankenberge / AGSO Knokke / Erfgoed Rupelstreek IOED 1431 / RL Vlaamse Ardennen 1437 / leftover cultuur-IGS Berg en Nete / SOLVA. Next every-10 is 1500.,,"
        f"{TS},{TS},"
        "tick1491 Ons Onderdak leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00189814 62p 1423605; assets 136782795 omzet 11511389 pers 1919909 pnl 321927 cash 5008962 debt 101590448; FOI ready not sent\n"
    )
    spawn = (
        "rq_1492,Leftover AGB/APB/official-41 dual residual hole-fill,hole_fill,5,open,L5,,"
        "Tick 1492 after 1491 Ons Onderdak. Do NOT redo Ons Onderdak. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover APB Inovant/Atlas only if a 2025 PDF now downloads (still 403/404 as of 1491). Leftover Puyenbroeck still 302 / no separate APB 2025 PDF as of 1491. Leftover Bosgroep VZWs only if a 2025 CDN now appears. Leftover other official-41 if JR2025 live: Woonsprong / Woonstart / Thuiswest / Meetjesland / de Thuisbouwer / Woonpijler / WM Elan / Vivus / Providentia / Het Vlaamse Woonanker / Woontrots / De Noorderkempen / IJzer en Zee. Leftover IOED/cultuur-IGS only if a 2025 CDN now appears. IVAREM/Hart only if JR2025 now live. Next every-10 is 1500. Provincial tourism VZWs exhausted. Ons Onderdak 1491 / Zetus 1490 / Inter-Vilvoordse 1489 / Woonschakel 1488 / De Voorkempen 1487 / Wonen in Limburg 1486 / Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 TAKEN. Do not hunt Woonin / Wooncompagnie (Dutch) or De Ideale Woning (already Thuisrand 1474).,,"
        f"{TS},{TS},"
        "spawned after tick1491 Ons Onderdak leftover woonmaatschappij residual; NEXT leftover APB Inovant/Atlas if PDF live else leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live\n"
    )
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1491=done + rq_1492 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T19:55:00Z,rq_1491,1491,no,"
        "tick1491 Ons Onderdak leftover woonmaatschappij residual; KBO 0405.501.570; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 136782795 omzet 11511389 pers 1919909 23.3 VTE pnl 321927 equity 34735657 cash 5008962 debt 101590448 capex 11194008 dividend 0; FOI ready omzet 11.51m / pers 1.92m 23.3 VTE / debt 101.59m / cash 5.01m DROP / PnL DROP 0.32m / dividend 0 / 1 VE; NOT leftover AGB Vauban Ieper / leftover AGB Musea Ieper / leftover Zetus 1490 / leftover IJzer en Zee / leftover Thuiswest / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1492 leftover APB Inovant/Atlas if PDF live else leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1134 answered 9 partial 27 total 1182; inventory budgets 42737 commitments 5091 leaderboard 7294 entities 1236 sources 3101; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1491")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1491_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
