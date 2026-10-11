#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T10:25:00Z"
GAP = "gap_evpk_omzet_empty_recv_0_11m_trade_0_45m_l5"

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
    if not last_s.startswith("rq_1425,"):
        raise SystemExit(f"expected last row rq_1425, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1425,Erfgoed Voorkempen JR2025 leftover dual residual,hole_fill,5,done,L5,igs_evpk,"
        "Completed: Erfgoed Voorkempen leftover IGS projectvereniging of 14 mined Voorkempen cities after leftover AGB hunt; KBO 0650.649.076 Actief; live JR2025 official NBB WVV MIC-inb PDF (44523 bytes 12p deposit 2026-00151989; AV 27.03.2026; header 09.06.2026; created 11.06.2026; no commissaris); sourced euros assets 623422 brutomarge 49498 omzet empty diensten empty pers empty pnl 48253 equity 125438 cash 499042 debt 497984 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.11m / leveranciers 0.45m / cash drop / pers empty,"
        f"{GAP},2026-08-19T10:45:00Z,{TS},"
        "tick1425 Erfgoed Voorkempen leftover IGS residual; KBO 0650.649.076; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1426 residual dual L5 VL"
    )
    spawn = (
        "rq_1426,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1425 done including Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Erfgoed Noorderkempen 0863.327.714 CDN 2026-00061596 live — take if leftover AGB first empty; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender / Cultuurregio Pajottenland & Zennevallei 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS (BIONERGA LOGISTICS 1423 now mined); skip already-mined Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1425 after Erfgoed Voorkempen leftover IGS live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1425=done + rq_1426 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1425 Erfgoed Voorkempen leftover IGS residual; KBO 0650.649.076; live JR2025 NBB WVV PDF; sourced euros assets 623422 brutomarge 49498 omzet empty diensten empty pers empty pnl 48253 equity 125438 cash 499042 debt 497984 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / other recv 0.11m / leveranciers 0.45m / cash drop / pers empty; next rq_1426 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1425,1425,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1425")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1425 - 2026-08-19 - rq_1425 Erfgoed Voorkempen dual residual leftover\n"
        "- Unit: Erfgoed Voorkempen / Projectvereniging erfgoed Voorkempen (leftover IGS / projectvereniging of 14 mined Voorkempen cities; 0 VE) after residual dual hunt (KBO **0650.649.076**; official rldv.be/erfgoed-voorkempen; live NBB WVV MIC-inb deposit **2026-00151989** PDF 44523 bytes / 12p; AV **27.03.2026**; header **09.06.2026**; created **11.06.2026**; model **MIC-inb** 26.0.12 m87-f; no commissaris / no accountant named; MIC-inb 6.6 not filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IGS Erfgoed Voorkempen statutory CDN live this tick (HTTP 200 / application/pdf / 44523 / 12p; SBM jaar **2025-12-31**; neerlegging 2026-06-11) — taken (hunt order #2 leftover unmined IGS projectvereniging with full WVV balans; not in the named unpublished cultuur list; analogous leftover to Zuidwest 1424 / CO7 1420 / Cultuuroverleg Meetjesland 1416 / Cultuurregio Leie Schelde 1417 / de Merode 1419 / Viertoren 1421 / Druivenstreek 1422). Distinct from already-mined Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / AGB Zoersel / AGB Kapellen / IGEAN. First confirmed not already extracted as JR2025 WVV euros: no Erfgoed Voorkempen / 0650.649.076 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **01.01.2016**; statutaire naam Projectvereniging erfgoed Voorkempen since 01.01.2016; Projectvereniging since 01.01.2016 (WVV header Dienstverlenende intergemeentelijke vereniging); zetel Schildesteenweg 99 2520 Ranst since 01.01.2016; **0 VE**; tel 03 312 87 11; e-mail info@rldevoorkempen.be; KBO no web; official site https://www.rldv.be/erfgoed-voorkempen/; no NACE/btw/hoedanigheden in KBO. WVV 2.1 bestuurders (no labeled voorzitter on form). Official site gemeenten: Brasschaat / Brecht / Essen / Kalmthout / Kapellen / Malle / Ranst / Schilde / Schoten / Wijnegem / Wommelgem / Wuustwezel / Zandhoven / Zoersel. Named share-% unpublished. Contact info@rldevoorkempen.be. Leftover-next Erfgoed Noorderkempen 0863.327.714 CDN 2026-00061596 live — not taken (one unit; leftover Voorkempen first). NBB consult skipped (403/SPA); euros extracted from the official MIC-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1430).\n"
        "- EUR strong (primary official WVV MIC-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; **pers 62 empty** / VTE unpublished — MIC-inb 6.2 not filed; MIC-inb 6.1.1/6.1.3/6.2/6.3/6.4/6.6/7/8/9/10/11/12-16 not filed; 6.1.2 MVA + 6.5 waarderingsregels only): assets **623422** (was 713350); fixed **1056** / MVA **1056** (machines only; aanschaf YE **3532** / afschr YE **2476**); IVA empty; FVA empty; current **622365**; ST recv **122961** (trade **8682** / other **114279**); cash **499042 DROP** vs 555586; prepaid **362**; equity **125438** (beschikbare reserves 125438); voorzieningen empty; schulden **497984** (no LT; ST **453765** all leveranciers vs 433046; deferred **44219** vs 203120); brutomarge **49498** vs 22224; omzet 70 empty; 60/61 empty; pers 62 empty; afschr 1177; andere bedrijfskosten 0; expl **+48321** vs +20890; fin opbr **69**; fin kosten **136**; tax empty; PnL **+48253** vs +20744; dividend **0** (694 empty); toevoeging overige reserves **48253**; capex **0**.\n"
        "- CSVs: sources +4; entities +1 `igs_evpk` parent `sec_flanders`; budgets +38 executed; commitments +1 envelope 49498 AV 27.03.2026; leaderboard +1 annual 49498 / total 623422; foi_queue +1 status=ready never sent; research_queue surgical rq_1425=done + rq_1426 spawn; loop_state ticks_completed=1425.\n"
        "- FOI: `gap_evpk_omzet_empty_recv_0_11m_trade_0_45m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / other recv 0.11m counterpart / leveranciers 0.45m counterpart / cash drop unpublished / pers empty / VTE unpublished / vennoten share-pct / commissaris unpublished.\n"
        "- Next: rq_1426 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Erfgoed Noorderkempen 0863.327.714 CDN 2026-00061596 if still unmined and PDF downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1425")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1425 rq/state/log done")
