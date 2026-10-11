#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T09:10:00Z"
GAP = "gap_kluz_omzet_empty_lease_4_48m_debt_5_76m_l5"

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
    if not last_s.startswith("rq_1414,"):
        raise SystemExit(f"expected last row rq_1414, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1414,AGB De Kluize JR2025 leftover dual residual,hole_fill,5,done,L5,agb_de_kluize_oosterzele,"
        "Completed: AGB De Kluize leftover AGB sport/GC/erfgoed/jeugd of mined city Oosterzele after leftover AGB hunt; KBO 0844.272.162 Actief; live JR2025 official NBB WVV VKT-kap PDF (260838 bytes 17p deposit 2026-00286795; AV 11.05.2026; header 09.07.2026; commissaris Blommaert & Co B 513 Johnny Blommaert N 1541 fee unpublished); sourced euros assets 5831290 brutomarge 342519 omzet empty diensten empty pers empty pnl 73538 equity 69529 cash 724091 debt 5761761 lease 4483958 capex 87700 dividend 50000; FOI ready omzet empty / diensten unpublished / pers empty / lease 4.48m / LT debt 5.32m / commissaris fee unpublished,"
        f"{GAP},2026-08-19T08:45:00Z,{TS},"
        "tick1414 AGB De Kluize leftover AGB residual; KBO 0844.272.162; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1415 residual dual L5 VL"
    )
    spawn = (
        "rq_1415,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1414 done including AGB De Kluize 1414 leftover AGB live NBB WVV / PATRIMONIUM MBS 1413 leftover IOK daughter live NBB WVV / IOK Afvalbeheer 1412 leftover IGS live NBB WVV / AGB Merchtem 1411 leftover AGB live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; skip already-mined AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1414 after AGB De Kluize leftover AGB live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1414=done + rq_1415 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1414 AGB De Kluize leftover AGB residual; KBO 0844.272.162; live JR2025 NBB WVV PDF; sourced euros assets 5831290 brutomarge 342519 omzet empty diensten empty pers empty pnl 73538 equity 69529 cash 724091 debt 5761761 lease 4483958 capex 87700 dividend 50000; FOI ready omzet empty / diensten unpublished / pers empty / lease 4.48m / LT debt 5.32m / commissaris fee unpublished; next rq_1415 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1414,1414,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1414")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1414 - 2026-08-19 - rq_1414 AGB De Kluize dual residual leftover\n"
        "- Unit: Autonoom Gemeentebedrijf De Kluize (leftover AGB / sportaccommodaties + GC De Kluize + erfgoed + jeugdhuis Pallieter of mined city Oosterzele; 0 VE) after residual dual hunt (KBO **0844.272.162**; official oosterzele.be/bestuur/agb-de-kluize; live NBB WVV VKT-kap deposit **2026-00286795** PDF 260838 bytes / 17p; AV **11.05.2026**; header **09.07.2026**; created **14.07.2026**; model **VKT-kap** 23.0.10 m01-f; commissaris Blommaert & Co Bedrijfsrevisor BV B 513 / 0479.875.925 / Johnny Blommaert N 1541 opdracht C; fee unpublished — VKT-kap 6.6 not filed; jaarverslag VKT-kap 10 pp.15-17 text). Leftover AGB first: AGB De Kluize was JR2025 unpublished last ticks 1189/1413 (FOI gap_oosterzele_dual_jr2025_ge_ocmw_agb_kluize_l5); statutory CDN live this tick (HTTP 200 / 260838 / 17p; SBM jaar **2025-12-31**) — taken (preferred leftover AGB of mined city with full WVV balans). Bornem last JR still 2024 SBM 2025pdf only. Hulshout last JR 2022. Trupark ST already mined 1278. VESPA/AGSL 2025 CDNs already mined. leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403. AGB Lille liquidation. Aarschot AGB already BBC dual. Leftover IGS IVAREM 0267.403.264 last JR still 2024 (SBM laatste 2024-01-01 > 2024-12-31; no 2026 deposit). Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 deposit / no jaarrekening. Distinct from already-mined PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / AGB Tielt 1405 / AGB Patri 1407 / ILvA 1344 / SOLVA 1351. First confirmed not already extracted as JR2025 WVV euros: tick 1189 unpublished stub only. KBO Actief / normale toestand since **28.09.2011**; statutaire naam Autonoom Gemeentebedrijf De Kluize / afkorting AGB De Kluize since 28.09.2011; Autonoom gemeentebedrijf since 28.09.2011; zetel Sportstraat 3 9860 Oosterzele since 03.09.2012; **0 VE**; tel 09/363.83.31; e-mail david.delandsheere@oosterzele.be; KBO no web; official site https://oosterzele.be/bestuur/agb-de-kluize; NACE 93.110/90.312/84.119; aanbestedende overheid since 28.09.2011; btw since 01.03.2012. Voorzitter Mia Waterloos (WVV 2.1 since 27.04.2026). Vennoot: Gemeente Oosterzele 0207.454.294 100% (VKT-kap 8). Secretaris David De Landsheere (jaarverslag). Contact david.delandsheere@oosterzele.be / info@oosterzele.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-kap deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (assets 5831291 vs PDF **5831290**). Not every-10 (next 1420).\n"
        "- EUR strong (primary official WVV VKT-kap; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; **pers 62 empty** / VTE unpublished; VKT-kap 6.1.1/6.2/6.4/6.5/6.6/6.7/6.9/7/9/11-17 not filed; 6.6 commissaris empty; jaarverslag VKT-kap 10 text): assets **5831290** (was 5817276); fixed **5009742** / MVA **5009715** (gebouwen **416750**; machines **107612**; meubilair **1395**; leasing **4483958**); IVA empty; FVA **27**; current **821549**; ST recv **97457** (trade **79188** / other **18269**); cash **724091 JUMP** vs 553256; prepaid empty (was 9200); equity **69529** (kapitaal 25000; wettelijke reserve 2257; overgedragen 42272); voorzieningen empty; schulden **5761761** (LT **5317332** waarvan lease/krediet **4932885** + overige leningen **384447**; ST **362077** waarvan LT-due **82065** + leveranciers **206747** + tax 3109 + soc 5645 + other **64512 JUMP** vs 13304; deferred 82352; debt 1-5y 328261 / >5y **4989071**; gov-guaranteed empty); brutomarge **342519** vs 266855; omzet 70 empty; 60/61 empty; pers 62 empty; afschr 191114; andere bedrijfskosten 77867; expl **+73538** vs +8311; fin opbr empty; fin kosten **0**; tax empty; PnL **+73538** vs +8310; vergoeding inbreng **50000**; to overgedragen 42272; capex **87700**; commissaris unpublished.\n"
        "- CSVs: sources +4; entities patch `agb_de_kluize_oosterzele` notes only (no new entity); budgets +45 executed; commitments +1 envelope 342519 AV 11.05.2026; leaderboard +1 annual 342519 / total 5831290; foi_queue +1 status=ready never sent; research_queue surgical rq_1414=done + rq_1415 spawn; loop_state ticks_completed=1414.\n"
        "- FOI: `gap_kluz_omzet_empty_lease_4_48m_debt_5_76m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / pers empty / lease 4.48m counterpart / LT loans 0.38m counterpart / commissaris fee unpublished / fin kosten 0.\n"
        "- Next: rq_1415 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Skip Motena / Trupark / Zorgbedrijf ST / already-mined AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / ECO2050 1360 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1414")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1414 rq/state/log done")
