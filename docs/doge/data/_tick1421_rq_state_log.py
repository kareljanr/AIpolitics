#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T10:05:00Z"
GAP = "gap_vtrt_omzet_empty_pers_0_08m_cash_0_19m_l5"

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
    if not last_s.startswith("rq_1421,"):
        raise SystemExit(f"expected last row rq_1421, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1421,Viertoren JR2025 leftover dual residual,hole_fill,5,done,L5,igs_vtrt,"
        "Completed: Viertoren leftover IGS projectvereniging of 4 mined Westhoek kust cities after leftover AGB hunt; KBO 0744.514.689 Actief; live JR2025 official NBB WVV MIC-inb PDF (41364 bytes 10p deposit 2026-00070101; AV 31.03.2026; created 02.04.2026; no commissaris); sourced euros assets 211378 brutomarge 110397 omzet empty diensten empty pers 79534 pnl 30657 equity 202586 cash 189139 debt 8791 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.08m VTE unpublished / other recv 0.02m / cash drop unpublished,"
        f"{GAP},2026-08-19T09:55:00Z,{TS},"
        "tick1421 Viertoren leftover IGS residual; KBO 0744.514.689; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1422 residual dual L5 VL"
    )
    spawn = (
        "rq_1422,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1421 done including Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10 / de Merode 1419 leftover IGS live NBB WVV / DVV Midwest 1418 leftover IGS live NBB WVV / Cultuurregio Leie Schelde 1417 leftover IGS live NBB WVV / Cultuuroverleg Meetjesland 1416 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Vrijetijdsregio Druivenstreek 0733.925.457 CDN 2026-00122944 live — take if leftover AGB first empty; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; other leftover cultuur-IGS / DVV / projectvereniging not in entities.csv (Noordrand / ECRU / Neteland / Route42 / Stuifzand / Zender / Zuidrand / Zuidwest) — take if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent (BIONERGA LOGISTICS 0553.855.647 has 2025 CDN) only after leftover AGB/IGS; skip already-mined Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1421 after Viertoren leftover IGS live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1421=done + rq_1422 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1421 Viertoren leftover IGS residual; KBO 0744.514.689; live JR2025 NBB WVV PDF; sourced euros assets 211378 brutomarge 110397 omzet empty diensten empty pers 79534 pnl 30657 equity 202586 cash 189139 debt 8791 capex 0 dividend 0; FOI ready omzet empty / diensten unpublished / pers 0.08m VTE unpublished / other recv 0.02m / cash drop unpublished; next rq_1422 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1421,1421,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1421")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1421 - 2026-08-19 - rq_1421 Viertoren dual residual leftover\n"
        "- Unit: Viertoren (leftover IGS / projectvereniging of 4 mined Westhoek kust cities; 0 VE) after residual dual hunt (KBO **0744.514.689**; official viertoren.be; live NBB WVV MIC-inb deposit **2026-00070101** PDF 41364 bytes / 10p; AV **31.03.2026**; created **02.04.2026**; model **MIC-inb** 23.0.6 m87-f; no commissaris / no accountant named; MIC-inb 6.6 not filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (city site JR2024 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; AGB Aarschot NBB last still 2024 (already BBC dual); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IGS Viertoren statutory CDN live this tick (HTTP 200 / 41364 / 10p; SBM jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS projectvereniging with full WVV balans; analogous leftover to CO7 1420 / Cultuuroverleg Meetjesland 1416 / Cultuurregio Leie Schelde 1417 / de Merode 1419). Distinct from already-mined CO7 1420 / DVV Westhoek 1415 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / AGB De Panne / IVVO / Aquaduin. First confirmed not already extracted as JR2025 WVV euros: no Viertoren / 0744.514.689 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **01.10.2019**; statutaire naam Viertoren since 01.10.2019; Projectvereniging since 01.10.2019; zetel Zeelaan(Kok) 303 8670 Koksijde since 01.10.2019; **0 VE**; KBO tel 058/53 30 93; KBO no email/web; official site https://viertoren.be/; e-mail info@viertoren.be; coordinator Mathieu Karreman; tel 0494 56 74 94. WVV 2.1 voorzitter Frederic Devos (since 11.02.2026) + ondervoorzitters Ann Gheeraert + Greta Verhaeghe + bestuurder Nicolas Luyssen. Official site gemeenten: De Panne / Koksijde / Nieuwpoort / Veurne. Named share-% unpublished. Contact info@viertoren.be. Leftover-next Vrijetijdsregio Druivenstreek 0733.925.457 CDN 2026-00122944 live — not taken (one unit; leftover Viertoren first). Dijk92 last JR still 2024. BIONERGA LOGISTICS leftover daughter not taken (hunt leftover IGS first). NBB consult skipped (403/SPA); euros extracted from the official MIC-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (assets 211378 / brutomarge 110397 / expl 30863 / equity 202586 / debt 8791 match PDF). Not every-10 (next 1430).\n"
        "- EUR strong (primary official WVV MIC-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **79534** / VTE unpublished — MIC-inb 6.2 not filed; MIC-inb 6.1.1/6.1.2/6.1.3/6.2/6.3/6.4/6.6/7/8/9/10/11/12-16 not filed; 6.5 waarderingsregels template only): assets **211378** (was 229857); fixed empty; MVA empty; IVA empty; FVA empty; current **211378**; ST recv **22238** (trade empty / other **22238**); cash **189139 DROP** vs 229857; prepaid empty; equity **202586** (beschikbare reserves **226050**; overgedragen **−23464**); voorzieningen empty; schulden **8791** (no LT; ST **8791** waarvan leveranciers **47** + soc **8744**; deferred empty was 38136); brutomarge **110397** vs 68882; omzet 70 empty; 60/61 empty; pers **79534** vs 44359; afschr empty; expl **+30863** vs +24523; fin opbr empty; fin kosten **206**; tax empty; PnL **+30657** vs +24317; dividend **0** (694 empty); over te dragen **−23464**; capex **0**.\n"
        "- CSVs: sources +4; entities +1 `igs_vtrt` parent `sec_flanders`; budgets +33 executed; commitments +1 envelope 110397 AV 31.03.2026; leaderboard +1 annual 110397 / total 211378; foi_queue +1 status=ready never sent; research_queue surgical rq_1421=done + rq_1422 spawn; loop_state ticks_completed=1421.\n"
        "- FOI: `gap_vtrt_omzet_empty_pers_0_08m_cash_0_19m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / pers 0.08m VTE unpublished / other recv 0.02m counterpart / cash drop unpublished / soc 8.7k.\n"
        "- Next: rq_1422 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS Vrijetijdsregio Druivenstreek 0733.925.457 CDN 2026-00122944 if still unmined and PDF downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent (BIONERGA LOGISTICS 0553.855.647 has 2025 CDN) only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / IOK DV 1368 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1421")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1421 rq/state/log done")
