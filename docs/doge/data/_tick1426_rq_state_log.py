#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T10:35:00Z"
GAP = "gap_enpk_omzet_empty_pers_0_77m_recv_0_07m_l5"

def patch_research_queue() -> None:
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 32768))
        tail = f.read()
    if not tail.endswith(b"\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1426,"):
        raise SystemExit(f"expected last row rq_1426, got {last_s[:80]!r}")
    if ",done," in last_s.split(",", 5)[4] if False else False:
        pass
    # status is field 5 (0-index 4). Cheap check:
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1426 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1426,Erfgoed Noorderkempen JR2025 leftover dual residual,hole_fill,5,done,L5,igs_enpk,"
        "Completed: Erfgoed Noorderkempen leftover IGS projectvereniging of 11 mined Noorderkempen cities after leftover AGB hunt; KBO 0863.327.714 Actief; live JR2025 official NBB WVV VKT-inb PDF (56875 bytes 17p deposit 2026-00061596; AV 24.03.2026; created 25.03.2026; neerlegging 2026-03-25; no commissaris); sourced euros assets 480193 brutomarge 831915 omzet empty diensten empty pers 767960 pnl 56632 equity 401292 cash 376948 debt 78901 capex 4084 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.77m / other recv 0.07m / cash jump,"
        f"{GAP},2026-08-19T10:25:00Z,{TS},"
        "tick1426 Erfgoed Noorderkempen leftover IGS residual; KBO 0863.327.714; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1427 residual dual L5 VL"
    )
    spawn = (
        "rq_1427,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1426 done including Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender / Cultuurregio Pajottenland & Zennevallei 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS (BIONERGA LOGISTICS 1423 now mined); skip already-mined Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1426 after Erfgoed Noorderkempen leftover IGS live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1426=done + rq_1427 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1426 Erfgoed Noorderkempen leftover IGS residual; KBO 0863.327.714; live JR2025 NBB WVV PDF; sourced euros assets 480193 brutomarge 831915 omzet empty diensten empty pers 767960 pnl 56632 equity 401292 cash 376948 debt 78901 capex 4084 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.77m / other recv 0.07m / cash jump; next rq_1427 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1426,1426,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1426")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1426 - 2026-08-19 - rq_1426 Erfgoed Noorderkempen dual residual leftover\n"
        "- Unit: Erfgoed Noorderkempen / Projectvereniging Erfgoed Noorderkempen (leftover IGS / projectvereniging of 11 mined Noorderkempen cities; 1 VE) after residual dual hunt (KBO **0863.327.714**; official erfgoednoorderkempen.be; live NBB WVV VKT-inb deposit **2026-00061596** PDF 56875 bytes / 17p; AV **24.03.2026**; created **25.03.2026**; neerlegging **2026-03-25**; model **VKT-inb** 26.0.8 m81-f; no commissaris / no accountant named; VKT-inb 6.2/6.3/6.5/6.6/6.7/6.9/7-11/13-17 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.4 + 6.8 + 12 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IGS Erfgoed Noorderkempen statutory CDN live this tick (HTTP 200 / application/pdf / 56875 / 17p; SBM jaar **2025-12-31**; neerlegging 2026-03-25) — taken (hunt order #2 leftover unmined IGS projectvereniging with full WVV balans; leftover-next after Voorkempen 1425; analogous leftover to Erfgoed Voorkempen 1425 / Zuidwest 1424 / CO7 1420 / Cultuuroverleg Meetjesland 1416). Distinct from already-mined Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422. First confirmed not already extracted as JR2025 WVV euros: no Erfgoed Noorderkempen / 0863.327.714 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **10.02.2004**; statutaire naam ERFGOED NOORDERKEMPEN since 23.01.2009; Projectvereniging since 10.02.2004 (WVV header Instelling van openbaar nut); zetel Grote Markt 1 2300 Turnhout since 10.02.2004; **1 VE**; KBO no tel/e-mail/web; official site https://erfgoednoorderkempen.be/; kantoor Druivenstraat 18 2300 Turnhout; tel 014 44 33 62; e-mail info@erfgoednoorderkempen.be; NACE 91.220; Werkgever RSZ since 01.01.2022; btw since 01.06.2010; aanbestedende overheid since 10.02.2004. WVV 2.1 voorzitter Arnold Wittenberg; ondervoorzitter Nathalie Cuylaerts. Official site gemeenten: Arendonk / Baarle-Hertog / Beerse / Hoogstraten / Kasterlee / Merksplas / Oud-Turnhout / Ravels / Rijkevorsel / Turnhout / Vosselaar (Lille from 01.2027). Named share-% unpublished. Contact info@erfgoednoorderkempen.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1430).\n"
        "- EUR strong (primary official WVV VKT-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 **767960** / VTE **9,2** vs 11,7): assets **480193** (was 426347); fixed **9553** / IVA **654** / MVA **8824** (machines **1887** / meubilair **6938**; MVA aanschaf YE **87559** / afschr YE **78735**) / FVA **74**; current **470640**; ST recv **74951** (trade **3349** / other **71602**); cash **376948 UP** vs 325115; prepaid **18741**; equity **401292** (overgedragen winst 401292); voorzieningen empty; schulden **78901** (no LT; ST **78901**; leveranciers **14258**; tax/soc **64643** waarvan bezoldigingen **56529**); brutomarge **831915** vs 844635; omzet 70 empty; 60/61 empty; pers **767960** vs 778231; afschr **6936**; andere bedrijfskosten 0; expl **+57018** vs +59582; fin opbr 0; fin kosten **386**; tax empty; PnL **+56632** vs +59212; dividend **0** (694 empty); over te dragen **401292**; capex **4084**.\n"
        "- CSVs: sources +4; entities +1 `igs_enpk` parent `sec_flanders`; budgets +41 executed; commitments +1 envelope 831915 AV 24.03.2026; leaderboard +1 annual 831915 / total 480193; foi_queue +1 status=ready never sent; research_queue surgical rq_1426=done + rq_1427 spawn; loop_state ticks_completed=1426.\n"
        "- FOI: `gap_enpk_omzet_empty_pers_0_77m_recv_0_07m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / pers 0.77m deelwerking unpublished / other recv 0.07m counterpart / cash jump unpublished / VTE drop 11.7→9.2 / vennoten share-pct / commissaris unpublished.\n"
        "- Next: rq_1427 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1426")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1426 rq/state/log done")
