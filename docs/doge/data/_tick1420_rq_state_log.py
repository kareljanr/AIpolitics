#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T09:55:00Z"
GAP = "gap_co7_omzet_0_90m_diensten_0_90m_prepaid_0_12m_l5"

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
    if not last_s.startswith("rq_1420,"):
        raise SystemExit(f"expected last row rq_1420, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1420,CultuurOverleg Zeven / CO7 JR2025 leftover dual residual + progress,hole_fill,5,done,L5,igs_co7,"
        "Completed: CultuurOverleg Zeven / CO7 leftover IGS projectvereniging of 7 mined Zuidelijke Westhoek cities after leftover AGB hunt; KBO 0877.372.225 Actief; live JR2025 official NBB WVV MIC-inb PDF (43209 bytes 11p deposit 2026-00080644; AV 26.03.2026; created 16.04.2026; no commissaris); sourced euros assets 691225 omzet 899440 diensten 900356 pers empty pnl -7140 equity 393922 cash 552517 debt 297303 capex 17712 dividend 0; FOI ready 6.10 empty / diensten unpublished split / prepaid 0.12m / pers empty; EVERY-10 progress refresh,"
        f"{GAP},2026-08-19T09:40:00Z,{TS},"
        "tick1420 CO7 leftover IGS residual + every-10; KBO 0877.372.225; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1421 residual dual L5 VL"
    )
    spawn = (
        "rq_1421,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1420 done including CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 last JR still 2024 — take only if JR2025 now live; other leftover cultuur-IGS / DVV / projectvereniging not in entities.csv — take if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent (BIONERGA LOGISTICS 0553.855.647 has 2025 CDN) only after leftover AGB/IGS; skip already-mined CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1420 after CO7 leftover IGS live NBB WVV + every-10; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1420=done + rq_1421 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1420 CultuurOverleg Zeven / CO7 leftover IGS residual + every-10; KBO 0877.372.225; live JR2025 NBB WVV PDF; sourced euros assets 691225 omzet 899440 diensten 900356 pers empty pnl -7140 equity 393922 cash 552517 debt 297303 capex 17712 dividend 0; FOI ready 6.10 empty / diensten unpublished split / prepaid 0.12m / pers empty; next rq_1421 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1420,1420,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1420")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1420 - 2026-08-19 - rq_1420 CultuurOverleg Zeven / CO7 dual residual leftover + every-10\n"
        "- Unit: CultuurOverleg Zeven / CO7 (leftover IGS / projectvereniging of 7 mined Zuidelijke Westhoek cities; 0 VE) after residual dual hunt (KBO **0877.372.225**; official co7.be; live NBB WVV MIC-inb deposit **2026-00080644** PDF 43209 bytes / 11p; AV **26.03.2026**; created **16.04.2026**; model **MIC-inb** 25.0.11 m87-f; no commissaris / no accountant named; MIC-inb 6.6 not filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IGS CultuurOverleg Zeven / CO7 leftover-next last tick 1419; statutory CDN live this tick (HTTP 200 / 43209 / 11p; SBM jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS projectvereniging with full WVV balans; analogous leftover to Cultuuroverleg Meetjesland 1416 / Cultuurregio Leie Schelde 1417 / de Merode 1419). Distinct from already-mined DVV Westhoek 1415 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / AGB Vauban Ieper. First confirmed not already extracted as JR2025 WVV euros: no CultuurOverleg Zeven / CO7 / 0877.372.225 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **17.11.2005**; statutaire naam CultuurOverleg Zeven / afkorting CO7 since 08.11.2005; Projectvereniging since 08.11.2005; zetel Grote Markt 1 8970 Poperinge since 08.11.2005; **0 VE**; KBO no email/web/tel; official site https://www.co7.be/; tel 057 34 66 94; e-mail info@co7.be; NACE 68.203 / 84.210; aanbestedende overheid since 08.11.2005; btw since 01.01.2022. WVV 2.1 bestuurders (no labeled voorzitter on form): Vanacker Bart / Meeuw Bram / Bogaert Brecht / Vandeputte Christophe / Talpe Emmily / Goubeir Gerda / Fonteyne Ivo / Jonckheere Joachim / Verbeke Klaas / Hoornaert Laurent / Stubbe Lieven / Wydooghe Liselot / Verdru Melanie. Official/HLN voorzitter Klaas Verbeke. Official site gemeenten: Heuvelland / Ieper / Langemark-Poelkapelle / Mesen / Poperinge / Vleteren / Zonnebeke. Named share-% unpublished. Contact info@co7.be. Leftover-next Dijk92 last JR still 2024. BIONERGA LOGISTICS leftover daughter not taken (hunt leftover IGS first). NBB consult skipped (403/SPA); euros extracted from the official MIC-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Every-10 (last 1410 Sunfin).\n"
        "- EUR strong (primary official WVV MIC-inb; **omzet 70 filled 899440** but **6.10 category/geo not filed**; **60/61 filled 900356** unpublished as a split; **pers 62 empty** / VTE unpublished — MIC-inb 6.2 not filed; MIC-inb 6.1.1/6.1.3/6.2/6.3/6.4/6.6/7/8/9/10/11/12-16 not filed; 6.1.2 MVA + 6.5 waarderingsregels only): assets **691225** (was 615702); fixed **14026** / MVA **14026** (meubilair only; aanschaf YE **76332** / afschr YE **62306**); IVA empty; FVA empty; current **677199**; ST recv **5183** (trade **5183** / other empty); cash **552517** vs 511474; prepaid **119499 JUMP** vs 96041; equity **393922** (overgedragen 393922); voorzieningen empty; schulden **297303** (no LT; ST **284516** all leveranciers vs 202219; deferred **12787**); brutomarge **−917** vs +20438; omzet **899440** vs 869377; 60/61 **900356** vs 848939; pers 62 empty; afschr 8062; expl **−8979** vs +16529; fin opbr 3429; fin kosten **561**; tax 1029; PnL **−7140** vs +20751; dividend **0** (694 empty); capex **17712**; disposal 1235.\n"
        "- CSVs: sources +4; entities +1 `igs_co7` parent `sec_flanders`; budgets +39 executed; commitments +1 envelope 899440 AV 26.03.2026; leaderboard +1 annual 899440 / total 691225; foi_queue +1 status=ready never sent; research_queue surgical rq_1420=done + rq_1421 spawn; loop_state ticks_completed=1420.\n"
        "- FOI: `gap_co7_omzet_0_90m_diensten_0_90m_prepaid_0_12m_l5` ready not sent — 6.10 omzet category/geo empty / diensten 900356 split / prepaid 0.12m counterpart / leveranciers 0.28m counterpart / pers empty / VTE unpublished.\n"
        "- Coverage: residual dual L5 (CO7 leftover cultuur IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs DVV Westhoek 1415 / AGB Vauban Ieper / member-city GE possible.\n"
        "- Every-10 progress (recount from disk after this tick writes): **A 100** / **B 100** / **C ~99** / **D ~74-88** (generous; not near-complete of 348bn) / **E ready 1063** (answered 9 / partial 27 / total 1111). Inventory: budgets 39779 · commitments 5020 · leaderboard 7223 · entities 1165 · sources 2816. Waste top10 **stable** (GIP #1; fossil / cars / cheque / reporté #2-10). Dual off-top10 NEW since 1410: AGB Merchtem 4.93m · IOK Afvalbeheer 70.50m · PATRIMONIUM MBS 1.60m · AGB De Kluize 5.83m · DVV Westhoek 3.15m · Cultuuroverleg Meetjesland 0.44m · Cultuurregio Leie Schelde 0.39m · DVV Midwest 2.86m · de Merode 0.37m · **CO7 0.69m**. Progress files refreshed: `progress_every_10_ticks.md` + `doge_waste_top10_current.md`.\n"
        "- Next: rq_1421 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent (BIONERGA LOGISTICS 0553.855.647 has 2025 CDN) only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1420")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1420 rq/state/log done")
