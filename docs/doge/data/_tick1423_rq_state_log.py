#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T10:30:00Z"
GAP = "gap_bnlg_omzet_1_72m_diensten_1_29m_l5"

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
    if not last_s.startswith("rq_1423,"):
        raise SystemExit(f"expected last row rq_1423, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1423,BIONERGA LOGISTICS JR2025 leftover dual residual,hole_fill,5,done,L5,nv_bnlg,"
        "Completed: BIONERGA LOGISTICS leftover 100pct Bionerga NV daughter / Optimo truck fleet of mined Limburg.net after leftover AGB/IGS hunt; KBO 0553.855.647 Actief; live JR2025 official NBB WVV VOL-kap PDF (2003913 bytes 90p deposit 2026-00119950; AV 20.04.2026; header 13.05.2026; created 26.05.2026; commissaris BDO 3740); sourced euros assets 3510439 omzet 1717525 diensten 1289949 pers empty pnl 142458 equity 1664756 cash 956680 debt 1845683 capex 355000 dividend 0; FOI ready 6.10 omzet category/geo empty / diensten 1.29m split / related-party recv+debt / leveranciers JUMP / pers empty,"
        f"{GAP},2026-08-19T10:15:00Z,{TS},"
        "tick1423 BIONERGA LOGISTICS leftover daughter residual; KBO 0553.855.647; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1424 residual dual L5 VL"
    )
    spawn = (
        "rq_1424,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1423 done including BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand / Zender / Zuidwest — take if a DISTINCT unmined entity has a live 2025 PDF; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Cultuuroverleg IJzervallei / Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS (BIONERGA LOGISTICS 1423 now mined); skip already-mined BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1423 after BIONERGA LOGISTICS leftover daughter live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1423=done + rq_1424 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1423 BIONERGA LOGISTICS leftover daughter residual; KBO 0553.855.647; live JR2025 NBB WVV PDF; sourced euros assets 3510439 omzet 1717525 diensten 1289949 pers empty pnl 142458 equity 1664756 cash 956680 debt 1845683 capex 355000 dividend 0; FOI ready 6.10 omzet category/geo empty / diensten 1.29m split / related-party recv+debt / leveranciers JUMP / pers empty; next rq_1424 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1423,1423,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1423")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1423 - 2026-08-19 - rq_1423 BIONERGA LOGISTICS dual residual leftover\n"
        "- Unit: BIONERGA LOGISTICS NV (leftover 100pct daughter of mined Bionerga NV 1354 / Optimo truck fleet of Limburg.net 1353; 1 VE) after residual dual hunt (KBO **0553.855.647**; official bionerga.be; live NBB WVV VOL-kap deposit **2026-00119950** PDF 2003913 bytes / 90p; AV **20.04.2026**; header **13.05.2026**; created **26.05.2026**; model **VOL-kap** 25.0.12 m02-f; commissaris BDO Bedrijfsrevisoren BV B00023 / 0431.088.289 / Maris Gert A02096 + Gysemberg Sebastiaan A02663 mandate 22.04.2024-20.04.2027 fee **3740**; jaarverslag VOL-kap 7 pp.39-42 text 25.03.2026; commissarisverslag VOL-kap 8 image-only this extract). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening (SBM analyse niet beschikbaar; no 2026pdf). Leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024 filed 2026-02-25). Leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover daughter BIONERGA LOGISTICS leftover-next since 1416; statutory CDN live this tick (HTTP 200 / application/pdf / 2003913 / 90p; SBM jaar **2025-12-31**) — taken (hunt order #6 leftover daughter after leftover AGB/IGS empty of live 2025 PDFs). Distinct from already-mined Bionerga NV 1354 (prefix `bng`; 100% shareholder) / Limburg.net 1353 / Nuhma seam 1355-1365 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419. First confirmed not already extracted as JR2025 WVV euros: no BIONERGA LOGISTICS / 0553.855.647 JR2025 extract in entities/sources/leaderboard (only leftover-next mentions). KBO Actief / normale toestand since **13.06.2014**; statutaire naam BIONERGA LOGISTICS since 13.06.2014; Naamloze vennootschap since 13.06.2014; zetel Herkenrodesingel 14 3500 Hasselt since 01.01.2025 (technical); **1 VE**; KBO no email/web/tel; parent site https://bionerga.be/; NACE 77.120; aanbestedende overheid since 13.06.2014; btw since 13.06.2014; kapitaal KBO **1.000.000**; jaarvergadering april; boekjaar 31 december. WVV 2.1: Bionerga NV 0882.280.227 gedelegeerd bestuurder (Peeters Philip) + Nuhma CV 0472.325.068 bestuurder (Kelchtermans Ludo) since 23.04.2025-21.04.2031. VOL-kap 6.7.2 aandeelhouder: Bionerga NV 0882.280.227 **1000/1000 = 100%**. Contact info@bionerga.be. Jaarverslag: schakel in Optimo-project Limburg.net (1 wagen tot 5 afvalsoorten); wagenpark vrachtwagens; CIP 355k onderbouw nieuwe elektrische vrachtwagen. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1430).\n"
        "- EUR strong (primary official WVV VOL-kap; **omzet 70 filled 1717525** but **6.10 category+geo empty**; **diensten 1289949** unpublished as a split; **pers 62 empty** / VTE unpublished — 6.10 DIMONA empty; uitzend 617 empty; VOL-kap 6.1/6.2/6.3.2/6.3.4-5/6.4.2/6.5.2/6.8/6.17/6.18.2/9/10/12-15 not filed; 6.16 commissaris 3740; jaarverslag VOL-kap 7 text; commissarisverslag VOL-kap 8 image-only): assets **3510439** (was 3671944); fixed **2173442** / MVA **2168237** (gebouwen **13258**; machines empty; meubilair/rollend **1799979**; CIP **355000**); IVA empty; FVA **5205** (verbonden **2000** + borgtochten **3205**); current **1336998**; ST recv **366260** (trade **351381** / other **14879**); geldbeleggingen **10402 DROP** vs 257441 (termijn); cash **956680 JUMP** vs 718496; prepaid **3655**; equity **1664756** (kapitaal 1000000; wettelijke reserve **44473**; overgedragen **597918**; capsub **22365**); voorzieningen empty; schulden **1845683** (LT **1134979** kredietinstellingen; ST **710704** waarvan LT-due **344285** + leveranciers **331702 JUMP** vs 100702 + tax **5428** + other **29289 DROP** vs 250057; deferred empty); omzet **1717525** vs 1966670; othops **344859 JUMP** vs 168286; nrec 76A empty (was 5000); 60 **1387**; diensten **1289949** vs 1367843; pers 62 empty; afschr **467692**; andere bedrijfskosten **109134** (640 **107048**); expl **+194221** vs +205363; fin opbr **8508**; fin kosten **12785**; tax **47486**; PnL **+142458** vs +142983; dividend **0** (694 empty); to wettelijke reserve 7123 / overgedragen 597918; capex **355000**; commissaris **3740**; bestuurders 9503 empty. Related-party: verbonden recv **12775** / debt **153046**; geassocieerde recv **338386**. Zakelijk gewaarborgd bank **1479264**. Off-balance bankgarantie ontvangen **34000**. btw-eenheid lid.\n"
        "- CSVs: sources +4; entities +1 `nv_bnlg` parent `nv_bionerga`; budgets +53 executed; commitments +1 envelope 1717525 AV 20.04.2026; leaderboard +1 annual 1717525 / total 3510439; foi_queue +1 status=ready never sent; research_queue surgical rq_1423=done + rq_1424 spawn; loop_state ticks_completed=1423.\n"
        "- FOI: `gap_bnlg_omzet_1_72m_diensten_1_29m_l5` ready not sent — 6.10 omzet category/geo empty / diensten 1.29m split / related-party recv+debt counterparts / leveranciers JUMP 0.33m / other ST DROP / pers empty / CIP 0.36m.\n"
        "- Next: rq_1424 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand / Zender / Zuidwest if a 2025 CDN is live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1423")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1423 rq/state/log done")
