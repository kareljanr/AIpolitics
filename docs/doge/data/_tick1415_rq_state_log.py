#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T10:50:00Z"
GAP = "gap_whdv_omzet_empty_pers_2_65m_recv_0_54m_l5"

def patch_research_queue() -> None:
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 16384))
        tail = f.read()
    if not tail.endswith(b"\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1415,"):
        raise SystemExit(f"expected last row rq_1415, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1415,DVV Westhoek JR2025 leftover dual residual,hole_fill,5,done,L5,igs_westhoek_dv,"
        "Completed: DVV Westhoek leftover IGS of 17 mined Westhoek cities + WVI after leftover AGB hunt; KBO 0695.496.928 Actief; live JR2025 official NBB WVV VKT-inb PDF (786056 bytes 27p deposit 2026-00300232; AV 23.06.2026; header 16.07.2026; commissaris Walter Hosten Bedrijfsrevisor BV B196 fee 7277); sourced euros assets 3145801 brutomarge 2859900 omzet empty diensten empty pers 2648974 pnl 101860 equity 1987351 cash 1859774 debt 1158449 capex 17881 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.54m / other ST 0.22m / expl drop unpublished,"
        f"{GAP},2026-08-19T10:20:00Z,{TS},"
        "tick1415 DVV Westhoek leftover IGS residual; KBO 0695.496.928; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1416 residual dual L5 VL"
    )
    spawn = (
        "rq_1416,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1415 done including DVV Westhoek 1415 leftover IGS live NBB WVV / AGB De Kluize 1414 leftover AGB live NBB WVV / PATRIMONIUM MBS 1413 leftover IOK daughter live NBB WVV / IOK Afvalbeheer 1412 leftover IGS live NBB WVV / AGB Merchtem 1411 leftover AGB live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Cultuuroverleg Meetjesland 0867.378.552 CDN 2026-00073178 / Cultuurregio Leie Schelde 0826.486.520 CDN 2026-00079660 — take if still unmined and PDF downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent (BIONERGA LOGISTICS 0553.855.647 has 2025 CDN) only after leftover AGB/IGS; skip already-mined DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1415 after DVV Westhoek leftover IGS live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1415=done + rq_1416 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1415 DVV Westhoek leftover IGS residual; KBO 0695.496.928; live JR2025 NBB WVV PDF; sourced euros assets 3145801 brutomarge 2859900 omzet empty diensten empty pers 2648974 pnl 101860 equity 1987351 cash 1859774 debt 1158449 capex 17881 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.54m / other ST 0.22m / expl drop unpublished; next rq_1416 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1415,1415,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1415")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1415 - 2026-08-19 - rq_1415 DVV Westhoek dual residual leftover\n"
        "- Unit: Dienstverlenende Vereniging Westhoek / DVV Westhoek (leftover IGS / dienstverlenende vereniging of 17 mined Westhoek cities + WVI; 2 VE) after residual dual hunt (KBO **0695.496.928**; official dvvwesthoek.be; live NBB WVV VKT-inb deposit **2026-00300232** PDF 786056 bytes / 27p; AV **23.06.2026**; header **16.07.2026**; created **16.07.2026**; model **VKT-inb** 25.0.13 m81-f; commissaris Walter Hosten Bedrijfsrevisor BV B196 / 0450.010.318 / Hosten Walter fee **7277**; oordeel zonder voorbehoud). Leftover AGB first: no unmined AGB with a live distinct 2025 statutory PDF this tick (AGB De Kluize already 1414; Vismijn Oostende / Hockeystadion no jaarrekening; Dendermonde / AGSL / AGSA / De Panne / Kapellen already mined). Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 deposit / no jaarrekening. Leftover IGS DVV Westhoek statutory CDN live this tick (HTTP 200 / 786056 / 27p; SBM jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS with full WVV balans). Distinct from already-mined IVVO 1345 / WVI 1346 / Aquaduin 1349 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412. First confirmed not already extracted as JR2025 WVV euros. KBO Actief / normale toestand since **22.12.2017**; statutaire naam Dienstverlenende vereniging Westhoek / afkorting DVV Westhoek since 22.12.2017; Dienstverlenende vereniging (Vlaams Gewest) since 22.12.2017; zetel Grote Markt 6 8600 Diksmuide since 22.12.2017; **2 VE**; tel 051/970400; e-mail info@dvvwesthoek.be; KBO no web; official site https://dvvwesthoek.be/; NACE 84.130; aanbestedende overheid since 22.12.2017; RSZ since 01.01.2022. Vennoten 18 x 80 aandelen (17 gemeenten + WVI 0205.157.869). Contact info@dvvwesthoek.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used. Commissaris assets 3145800.75 vs form **3145801**. Not every-10 (next 1420).\n"
        "- EUR strong (primary official WVV VKT-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **2648974** / **34,2 VTE**; VKT-inb 6.1.1/6.2/6.3/6.5/6.7/6.9/7/9/10/13-17 not filed; 6.6 commissaris 7277): assets **3145801** (was 2988210); fixed **89342** / MVA **87795** (machines **69588**; meubilair **18207**); IVA empty; FVA **1547**; current **3056458**; ST recv **660589** (trade **121364** / other **539225 JUMP** vs 380413); geldbeleggingen **500000**; cash **1859774** vs 1706742; prepaid 36096; equity **1987351** (inbreng 543455; reserves 1396929; overgedragen 46967); voorzieningen empty; schulden **1158449** (no LT; ST **787498** waarvan leveranciers **135198** + vooruit 3599 + tax 70324 + soc 354597 + other **223780**; deferred **370952 JUMP** vs 209401); brutomarge **2859900** vs 3661785 (niet-recurrente 39299); omzet 70 empty; 60/61 empty; pers **2648974**; afschr 11393; andere bedrijfskosten 117720; expl **+81814** vs +917226; fin opbr 29264; fin kosten **451**; tax 8766; PnL **+101860** vs +945511; dividend **0**; to reserves 220879 / overgedragen 46967; capex **17881**; commissaris 7277.\n"
        "- CSVs: sources +4; entities +1 `igs_westhoek_dv`; budgets +46 executed; commitments +1 envelope 2859900 AV 23.06.2026; leaderboard +1 annual 2859900 / total 3145801; foi_queue +1 status=ready never sent; research_queue surgical rq_1415=done + rq_1416 spawn; loop_state ticks_completed=1415.\n"
        "- FOI: `gap_whdv_omzet_empty_pers_2_65m_recv_0_54m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / other recv 0.54m counterpart / other ST 0.22m counterpart / expl drop unpublished.\n"
        "- Next: rq_1416 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Cultuuroverleg Meetjesland / Cultuurregio Leie Schelde if still unmined and PDF downloads. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1415")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1415 rq/state/log done")
