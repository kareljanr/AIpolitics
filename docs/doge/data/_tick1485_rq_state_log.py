#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Surgical rq_1485=done + spawn rq_1486; update loop_state; append loop_log.
NEVER rewrite whole research_queue.csv.
"""
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T18:55:00Z"

def surgical_rq():
    p = DATA / "research_queue.csv"
    raw = p.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    idx = raw.rfind(b"\n", 0, len(raw)-1)
    last = raw[idx+1:]
    if not last.startswith(b"rq_1485,"):
        raise SystemExit(f"last row is not rq_1485: {last[:80]!r}")
    if b"rq_1486," in raw:
        raise SystemExit("rq_1486 already present — concurrent tick?")
    done = (
        "rq_1485,Woonpunt Zennevallei JR2025 leftover dual residual,hole_fill,5,done,L5,wm_wpzn,"
        "Tick 1485 took leftover official-41 woonmaatschappij Woonpunt Zennevallei 0400.898.624 live official NBB WVV VOL-inb 2026-00145529 after leftover AGB/APB hunt (Inovant/Atlas still 403/404). Do NOT redo Woonpunt Zennevallei. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 PDF actually downloads. Leftover OTHER provincial APBs (Puyenbroeck still 302). Leftover unmined IGS/RL/Bosgroepen/daughters/woonmaatschappijen if a 2025 CDN or official AV PDF is live. Leftover other official-41 of mined cities if JR2025 live. Leftover IOED/cultuur-IGS only if a 2025 CDN now appears. IVAREM/Hart/Dommelhof only if a true JR2025 statutory PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / AGB Tienen / AGB Menen / Erfgoed Rupelstreek IOED 1431 / RL Vlaamse Ardennen 1437 / SOLVA. Next every-10 is 1490.,,"
        f"{TS},{TS},"
        "tick1485 Woonpunt Zennevallei leftover woonmaatschappij residual; official NBB WVV VOL-inb 2026-00145529 64p 1344945; assets 162911198 omzet 15271056 pers 3128980 pnl 741465 cash 4801403 debt 108036213; FOI ready not sent\n"
    )
    spawn = (
        "rq_1486,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "EVERY-10 just closed at 1480 (Kanvaz leftover woonmaatschappij live official NBB WVV). Next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1485 done including Woonpunt Zennevallei 1485 leftover woonmaatschappij live official NBB WVV / !Mpuls 1484 leftover woonmaatschappij live official NBB WVV / WoonST 1483 leftover woonmaatschappij live official NBB WVV / stek92 1482 leftover woonmaatschappij live official NBB WVV / LeefGoed 1481 leftover woonmaatschappij live official NBB WVV / Kanvaz 1480 leftover woonmaatschappij live official NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Leftover Antwerp APB Inovant/Atlas only if a 2025 PDF actually downloads. Leftover OTHER provincial APBs (Puyenbroeck still 302). Leftover Bosgroep VZWs only if a 2025 CDN is live. Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1471. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1461. Leftover other woonmaatschappijen of mined cities only if a 2025 CDN now downloads (Woonpunt Zennevallei TAKEN 1485; !Mpuls TAKEN 1484; WoonST TAKEN 1483; stek92 TAKEN 1482; LeefGoed TAKEN 1481; Kanvaz TAKEN 1480; WMVA TAKEN 1479; Woonboog TAKEN 1478; Woonveer TAKEN 1477; Woonkade TAKEN 1476; Woonstroom TAKEN 1475; Thuisrand TAKEN 1474; Vivendo TAKEN 1473; SW+ TAKEN 1472; Woonhaven TAKEN 1471; leftover other official-41 only if JR2025 live). Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined Woonpunt Zennevallei 1485 / !Mpuls 1484 / WoonST 1483 / stek92 1482 / LeefGoed 1481 / Kanvaz 1480 / WMVA 1479 / Woonboog 1478 / Woonveer 1477 / Woonkade 1476 / Woonstroom 1475 / Thuisrand 1474 / Vivendo 1473 / SW+ 1472 / Woonhaven 1471 / Thuispunt Gent 1470 / Tuinwijk 1469 / Dijledal 1468 / Dender-Zuid 1467 / Dimensa 1466 / Woonmaatschappij Rivierenland 1465 / Woonpunt Waas 1464 / AGB Tienen / AGB Menen / Erfgoed Rupelstreek IOED 1431 / RL Vlaamse Ardennen 1437 / SOLVA. Next every-10 is 1490.,,"
        f"{TS},{TS},"
        "spawned after tick1485 Woonpunt Zennevallei leftover woonmaatschappij residual; next leftover APB Inovant/Atlas if PDF live else leftover other official-41 if JR2025 live else leftover AGB / leftover Bosgroep\n"
    )
    p.write_bytes(raw[:idx+1] + done.encode("utf-8") + spawn.encode("utf-8"))
    print("research_queue surgical rq_1485=done + rq_1486 spawn")

def loop_state():
    p = DATA / "loop_state.csv"
    p.write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-19T18:55:00Z,rq_1485,1485,no,"
        "tick1485 Woonpunt Zennevallei leftover woonmaatschappij residual; KBO 0400.898.624; live JR2025 official NBB WVV VOL-inb PDF; sourced euros assets 162911198 omzet 15271056 pers 3128980 37.3 VTE pnl 741465 equity 47335265 cash 4801403 debt 108036213 capex 10461618 dividend 0; FOI ready omzet 15.27m JUMP / pers 3.13m 37.3 VTE / debt 108.04m / cash 4.80m JUMP / PnL JUMP 0.74m / dividend 0 / 1 VE; NOT leftover Woonpunt Waas 1464 / leftover !Mpuls 1484 / leftover WoonST 1483 / leftover Woonin / leftover De Ideale Woning / leftover Wooncompagnie / leftover APB Inovant / Atlas / Puyenbroeck; next rq_1486 leftover APB Inovant/Atlas if PDF live else leftover other official-41 / leftover AGB / leftover Bosgroep / leftover IOED / leftover IVAREM/Hart only if JR2025 now live; FOI ready 1128 answered 9 partial 27 total 1176; continuous hole_fill\n",
        encoding="utf-8",
    )
    print("loop_state 1485")

def loop_log():
    p = ROOT / "docs/doge/loop_log.md"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = (DATA / "_tick1485_logblock.md").read_text(encoding="utf-8")
    if not block.endswith("\n"):
        block += "\n"
    p.write_bytes(raw + block.encode("utf-8"))
    print("loop_log appended")

if __name__ == "__main__":
    surgical_rq()
    loop_state()
    loop_log()
