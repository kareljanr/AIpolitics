#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T08:45:00Z"
GAP = "gap_pmbs_omzet_0_11m_diensten_0_11m_vrucht_l5"

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
    if not last_s.startswith("rq_1413,"):
        raise SystemExit(f"expected last row rq_1413, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1413,PATRIMONIUM MBS JR2025 leftover dual residual,hole_fill,5,done,L5,nv_pmbs,"
        "Completed: PATRIMONIUM MBS leftover IOK Afvalbeheer 60pct / IVAREM 40pct daughter NV after leftover AGB/IGS hunt; KBO 0886.391.839 Actief; live JR2025 official NBB WVV VOL-kap PDF (1814120 bytes 41p deposit 2026-00136170; AV 08.05.2026; header 01.06.2026; commissaris EY B160 Christoph Oris A02341 fee 4356); sourced euros assets 1600122 omzet 107101 diensten 112337 pnl 1072 equity 1599050 cash 528367 debt 1072 capex 0 dividend 1072; FOI ready omzet 6.10 empty / diensten split / vruchtgebruik Maatschap MBS / commissaris image-only,"
        f"{GAP},2026-08-19T08:20:00Z,{TS},"
        "tick1413 PATRIMONIUM MBS leftover IOK daughter residual; KBO 0886.391.839; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1414 residual dual L5 VL"
    )
    spawn = (
        "rq_1414,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1413 done including PATRIMONIUM MBS 1413 leftover IOK daughter live NBB WVV / IOK Afvalbeheer 1412 leftover IGS live NBB WVV / AGB Merchtem 1411 leftover AGB live NBB WVV / Sunfin 1410 leftover Nuhma daughter live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; skip already-mined PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1413 after PATRIMONIUM MBS leftover IOK daughter live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1413=done + rq_1414 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1413 PATRIMONIUM MBS leftover IOK daughter residual; KBO 0886.391.839; live JR2025 NBB WVV PDF; sourced euros assets 1600122 omzet 107101 diensten 112337 pnl 1072 equity 1599050 cash 528367 debt 1072 capex 0 dividend 1072; FOI ready omzet 6.10 empty / diensten split / vruchtgebruik Maatschap MBS / commissaris image-only; next rq_1414 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1413,1413,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1413")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1413 - 2026-08-19 - rq_1413 PATRIMONIUM MBS dual residual leftover\n"
        "- Unit: PATRIMONIUM MBS NV (leftover IOK Afvalbeheer 60pct / IVAREM 40pct daughter NV / MBS patrimonium + vruchtgebruik Maatschap MBS of mined Kempen+Mechelen waste IGS; 0 VE) after residual dual hunt (KBO **0886.391.839**; parent iok.be; live NBB WVV VOL-kap deposit **2026-00136170** PDF 1814120 bytes / 41p; AV **08.05.2026**; header **01.06.2026**; model **VOL-kap** 25.0.12 m02-f; commissaris EY Bedrijfsrevisoren BV B160 / 0446.334.711 / Christoph Oris A02341 mandate 09.05.2025-16.05.2028 fee **4356**; jaarverslag VOL-kap 7 pp.24-32 text; commissarisverslag VOL-kap 8 pp.34-37 image-only this extract). Leftover AGB first: leftover AGB of mined cities already mined / extract-only / still 2024 this hunt (Bornem last JR still 2024 SBM 2025pdf only; Hulshout last JR 2022; Trupark ST already mined 1278 even though CDN 2026-00256628 now live HTTP 200 / 66554 — do-not-redo; AGB Ieper Sport=Vauban already mined 1186; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; Aarschot AGB already BBC dual; AGB De Kluize Oosterzele JR2025 not public) — skipped. Leftover IGS IVAREM 0267.403.264 last JR still 2024 (SBM laatste 2024-01-01 > 2024-12-31; no 2026 deposit). Dommelhof leftover Limburg EVA KBO 0777.495.085 still no 2026 deposit / no jaarrekening. Leftover daughter NV PATRIMONIUM MBS leftover-next last tick 1412; statutory CDN live this tick (HTTP 200 / 1814120 / 41p) — taken (hunt order #4 after leftover AGB/IGS/Dommelhof). Distinct from already-mined IOK Afvalbeheer 1412 (prefix `ioka`; 60% shareholder / FVA 600000) / IOK DV 1368 / IGEAN / IDM / IVM / ILvA / IVLA / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / VERKO 1403 / AGB Merchtem 1411. First confirmed not already mined: no PATRIMONIUM MBS / 0886.391.839 JR2025 extract in entities/sources/leaderboard (only leftover-next + IOK Afvalbeheer 60% FVA mention). KBO Actief / normale toestand since **15.01.2007**; statutaire naam PATRIMONIUM MBS since 28.12.2006; Naamloze vennootschap since 01.11.2018; zetel Antwerpseweg 1 2440 Geel since 28.12.2006; **0 VE**; KBO no email/web/tel; parent site https://www.iok.be; NACE 81.100; aanbestedende overheid since 28.12.2006; btw since 01.02.2007; kapitaal KBO **1.000.000**; jaarvergadering mei; boekjaar 31 december. Voorzitters WVV 2.1: Ivan Blauwhoff + Eduardus (Ward) Kennes (beide Voorzitter van de Raad van Bestuur). Bestuurders IOK: Ward Kennes + Stijn Adriaensens + Sander Ooms; IVAREM: Ivan Blauwhoff + Pia Indigne + Eric Janssens. Secretaris alternerend Toon Otten (IOK) + Luc Poot (IVAREM). Contact info@iok.be; jaarverslag T 014 53 53 00. Vennoten VOL-kap 6.7.2: IOK Afvalbeheer 0862.457.484 Klasse A **255156/425260 = 60%** + IVAREM 0267.403.264 Klasse A **170104/425260 = 40%**. Remuneratieverslag presentiegeld **5539,05** + reis **162,13** + SVZ **863,70**; WVV 9503 empty. NBB consult skipped (403/SPA); euros extracted from the official VOL-kap deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (assets 1600122 / omzet 107101 / equity 1599050 / debt 1072 match PDF). Not every-10 (next 1420).\n"
        "- EUR strong (primary official WVV VOL-kap; **omzet 70 filled 107101** but **6.10 category+geo empty**; **diensten 112337** unpublished as a split; **overige vorderingen 9143** counterpart unpublished; **overige schulden 750** counterpart unpublished; **vruchtgebruik Maatschap MBS** (IOK+IVAREM) on MBS installatie — omzet counterpart unpublished; commissarisverslag VOL-kap 8 image-only; VOL-kap 6.1/6.2/6.3.1-4/6.3.6/6.4/6.5/6.8/6.9/6.11/6.12/6.14/6.17/6.18.2/6.20/9/10/12-15 not filed): assets **1600122** (was 1608777); fixed **1058150** / MVA **1058150** (overige MVA only; aanschaf **42326000** / afschr **41267850**; terreinen/machines/meubilair/leasing/CIP empty); IVA empty; FVA empty; current **541972**; ST recv **9347** (trade **204** / other **9143**); geldbeleggingen **522**; cash **528367 DROP** vs 542681; prepaid **3737 JUMP** vs 1; equity **1599050** (kapitaal 1000000; wettelijke reserve 599050); voorzieningen empty; schulden **1072 DROP** vs 9727 (no LT; ST tax **322** + other **750**); omzet **107101** vs 103825; othops empty; diensten **112337** vs 109511; pers empty / VTE empty; andere bedrijfskosten **120**; expl **−5356** vs −5804; fin opbr **7024** (vlottend); fin kosten **206**; tax **390**; PnL **+1072** vs +9439 all as vergoeding inbreng **1072**; capex aanschaf empty **0**; commissaris **4356**; bestuurders 9503 empty. Waarderingsregel: vruchtgebruik 28.12.2006 max 30y to Maatschap MBS; naakte eigendom niet afgeschreven.\n"
        "- CSVs: sources +4; entities +1 `nv_pmbs` parent `igs_ioka`; budgets +41 executed; commitments +1 envelope 107101 AV 08.05.2026; leaderboard +1 annual 107101 / total 1600122; foi_queue +1 status=ready never sent; research_queue surgical rq_1413=done + rq_1414 spawn; loop_state ticks_completed=1413.\n"
        "- FOI: `gap_pmbs_omzet_0_11m_diensten_0_11m_vrucht_l5` ready not sent — 6.10 omzet category/geo empty / diensten 112337 split / vruchtgebruik Maatschap MBS counterpart / other recv 9143 / other debt 750 / commissarisverslag image-only.\n"
        "- Next: rq_1414 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Skip Motena / Trupark / Zorgbedrijf ST / already-mined PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / ECO2050 1360 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1413")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1413 rq/state/log done")
