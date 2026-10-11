#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:00:00Z"
GAP = "gap_ebk_assets_0_20m_lev_0_15m_empty_pnl_l5"

def patch_research_queue() -> None:
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 65536))
        tail = f.read()
    if not tail.endswith(b"\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1428,"):
        raise SystemExit(f"expected last row rq_1428, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1428 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1428,Erfgoed Brabantse Kouters JR2025 leftover dual residual,hole_fill,5,done,L5,igs_ebk,"
        "Completed: Erfgoed Brabantse Kouters leftover IGS projectvereniging / IOED of 12 mined Brabantse Kouters cities after leftover AGB hunt; KBO 0741.478.094 Actief; live JR2025 official NBB WVV MIC-VZW PDF (34843 bytes 7p deposit 2026-00321349; AV 25.03.2026; created 23.07.2026; neerlegging 2026-07-23; no commissaris); sourced euros assets 200838 omzet empty diensten empty lidgeld empty pers empty pnl 0 equity empty cash 172470 debt 200838 capex 0 dividend 0; FOI ready empty 70/73/60/61 / empty EV / leveranciers 0.15m / deferred 0.05m,"
        f"{GAP},2026-08-19T10:50:00Z,{TS},"
        "tick1428 Erfgoed Brabantse Kouters leftover IGS residual; KBO 0741.478.094; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1429 residual dual L5 VL"
    )
    spawn = (
        "rq_1429,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1428 done including Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender / Cultuurregio Pajottenland & Zennevallei 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Kusterfgoed 0552.559.411 JR2025 CDN 2026-00241009 LIVE — STRONG next; leftover RL Lage Kempen 0677.597.755 JR2025 CDN 2026-00158101 live (RL not IOED — after leftover AGB/IGS); leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme / Brugge en Ommeland / Land van Nete en Aa / Hydra / Rupelstreek / Viersprong if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS (BIONERGA LOGISTICS 1423 now mined); skip already-mined Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1428 after Erfgoed Brabantse Kouters leftover IGS live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1428=done + rq_1429 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1428 Erfgoed Brabantse Kouters leftover IGS residual; KBO 0741.478.094; live JR2025 NBB WVV PDF; sourced euros assets 200838 omzet empty diensten empty lidgeld empty pers empty pnl 0 equity empty cash 172470 debt 200838 capex 0 dividend 0; FOI ready empty 70/73/60/61 / empty EV / leveranciers 0.15m / deferred 0.05m; next rq_1429 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1428,1428,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1428")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1428 - 2026-08-19 - rq_1428 Erfgoed Brabantse Kouters dual residual leftover\n"
        "- Unit: Projectvereniging Erfgoed Brabantse Kouters (leftover IGS / projectvereniging / IOED of 12 mined Brabantse Kouters cities + RLBK; 0 VE) after residual dual hunt (KBO **0741.478.094**; official brabantsekouters.be; live NBB WVV MIC-VZW deposit **2026-00321349** PDF 34843 bytes / 7p; AV **25.03.2026**; created **23.07.2026**; neerlegging **2026-07-23**; model **MIC-VZW** 25.0.13 m08-f; no commissaris / no accountant named; MIC-VZW 6.1.1/6.1.2/6.1.3/6.2/6.3/6.4/6.5/7/8 not filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022 (SBM 2023pdf 2023-00125347 only); AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IGS Erfgoed Brabantse Kouters statutory CDN live this tick (HTTP 200 / application/pdf / 34843 / 7p; SBM jaar **2025-12-31**; neerlegging 2026-07-23) — taken (hunt order #2 leftover unmined IGS / IOED projectvereniging named from 1427 with full WVV balans). Distinct from already-mined Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / AGB Merchtem 1411. First confirmed not already extracted as JR2025 WVV euros: no Erfgoed Brabantse Kouters / 0741.478.094 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **06.01.2020**; statutaire naam Projectvereniging Erfgoed Brabantse Kouters since 14.12.2022; Projectvereniging since 06.01.2020; zetel Houtemsesteenweg 23 1800 Vilvoorde since 06.01.2020; **0 VE**; e-mail info@brabantsekouters.be since 06.01.2020; no tel/web/NACE/btw/hoedanigheid in KBO. Official site gemeenten: Asse / Grimbergen / Kraainem / Machelen / Meise / Merchtem / Steenokkerzeel / Vilvoorde / Wemmel / Wezembeek-Oppem / Zaventem / Zemst + RLBK. Named share-% unpublished. Contact info@brabantsekouters.be; coordinator sebastiaan.goovaerts@brabantsekouters.be. NBB consult skipped (403/SPA); euros extracted from the official MIC-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1430).\n"
        "- EUR strong (primary official WVV MIC-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty**; **pers 62 empty** / VTE unpublished — MIC-VZW 6.2 not filed; **EV 10/15 empty**): assets **200838** (was 183780); fixed empty / IVA empty / MVA empty / FVA empty; current **200838**; ST recv empty; cash **172470** vs 158950; prepaid **28368** vs 24829; equity empty / 0 (all 10/15 blank; BS balances via schulden); voorzieningen empty; schulden **200838** (no LT; ST **153718** all leveranciers vs 153718; deferred **47119** vs 30062); brutomarge **0** vs 44; omzet empty; 73 empty; 60/61 empty; pers 62 empty; afschr empty; andere bedrijfskosten empty; expl **0** vs 44; fin opbr empty; fin kosten empty vs 44; tax empty; PnL **0** vs 0; dividend **0**; capex **0**.\n"
        "- CSVs: sources +4; entities +1 `igs_ebk` parent `sec_flanders`; budgets +22 executed; commitments +1 envelope 200838 AV 25.03.2026; leaderboard +1 annual 200838 / total 200838; foi_queue +1 status=ready never sent; research_queue surgical rq_1428=done + rq_1429 spawn; loop_state ticks_completed=1428.\n"
        "- FOI: `gap_ebk_assets_0_20m_lev_0_15m_empty_pnl_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers empty / VTE unpublished / EV empty / leveranciers 0.15m counterpart / deferred 0.05m / prepaid 0.03m / vennoten share-pct / commissaris unpublished / Vlaamse IOED-subsidie 2025 unpublished.\n"
        "- Next: rq_1429 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IOED Kusterfgoed **0552.559.411** JR2025 CDN **2026-00241009** LIVE — STRONG next. Leftover RL Lage Kempen **0677.597.755** JR2025 CDN **2026-00158101** live (RL not IOED — after leftover AGB/IGS). Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme / Brugge en Ommeland / Land van Nete en Aa / Hydra / Rupelstreek / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1428")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1428 rq/state/log done")
