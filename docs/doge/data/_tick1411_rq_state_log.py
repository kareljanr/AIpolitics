#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T08:10:00Z"
GAP = "gap_mrch_omzet_empty_recv_1_33m_debt_3_38m_l5"

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
    if not last_s.startswith("rq_1411,"):
        raise SystemExit(f"expected last row rq_1411, got {last_s[:80]!r}")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1411,AGB Merchtem JR2025 leftover dual residual,hole_fill,5,done,L5,agb_merchtem,"
        "Completed: AGB Merchtem leftover AGB vrijetijd of mined city Merchtem after leftover AGB hunt; KBO 0824.869.093 Actief; live JR2025 official NBB WVV VKT-inb PDF (264500 bytes 22p deposit 2026-00317853; AV 29.06.2026; header 22.07.2026; commissaris Bedrijfsrevisoren SD B00240 fee 3705; accountant Moore Finance & Tax prepared B); sourced euros assets 4925278 brutomarge 313807 omzet empty diensten empty pers empty pnl 46516 equity 1413160 cash 57860 debt 3382104 recv 1328425 capex 48876 dividend 25000; FOI ready omzet empty / diensten unpublished / pers empty / ST recv 1.33m / LT loans 2.73m / jaarverslag not filed,"
        f"{GAP},2026-08-19T07:45:00Z,{TS},"
        "tick1411 AGB Merchtem leftover AGB residual; KBO 0824.869.093; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1412 residual dual L5 VL"
    )
    spawn = (
        "rq_1412,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1411 done including AGB Merchtem 1411 leftover AGB live NBB WVV / Sunfin 1410 leftover Nuhma daughter live NBB WVV / IGO 1409 leftover IGS live NBB WVV / Rematics 1408 leftover Nuhma daughter live NBB WVV / AGB Patri 1407 leftover AGB live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS IOK Afvalbeheer 0862.457.484 CDN 2026-00306548 live — take if leftover AGB first empty; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; other leftover IGS only if a DISTINCT unmined entity has a live 2025 PDF; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; skip already-mined AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Limburg.net; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot still 2024; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403,,"
        f"{TS},{TS},"
        "spawned tick1411 after AGB Merchtem leftover AGB live NBB WVV; next residual dual L5 VL"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1411=done + rq_1412 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1411 AGB Merchtem leftover AGB residual; KBO 0824.869.093; live JR2025 NBB WVV PDF; sourced euros assets 4925278 brutomarge 313807 omzet empty diensten empty pers empty pnl 46516 equity 1413160 cash 57860 debt 3382104 recv 1328425 capex 48876 dividend 25000; FOI ready omzet empty / diensten unpublished / pers empty / ST recv 1.33m / LT loans 2.73m / jaarverslag not filed; next rq_1412 residual dual L5 VL; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1411,1411,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1411")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1411 - 2026-08-19 - rq_1411 AGB Merchtem dual residual leftover\n"
        "- Unit: Autonoom Gemeentebedrijf Merchtem (leftover AGB / vrijetijdsinfrastructuur + sportaccommodaties of mined city Merchtem; 0 VE) after residual dual hunt (KBO **0824.869.093**; official merchtem.be/AGB; live NBB WVV VKT-inb deposit **2026-00317853** PDF 264500 bytes / 22p; AV **29.06.2026**; header **22.07.2026**; model **VKT-inb** 26.0.15 m81-f; commissaris Bedrijfsrevisoren SD B00240 / Koningin Astridlaan 49 1780 Wemmel mandate 01.01.2025-31.12.2026 fee **3705**; accountant Moore Finance & Tax BV 0451.657.041 prepared B; commissarisverslag pp.19-21 image-only this extract). Leftover AGB first: AGB Merchtem was JR2025 unpublished last tick 1313 (MJP 2026-2031 live; no BBC/NBB PDF); statutory CDN live this tick (HTTP 200 / 264500 / 22p) — taken (preferred leftover AGB of mined city with full WVV balans). Aarschot last JR still 2024. Dendermonde/VESPA/AGSL Leuven now have 2025 CDNs but already mined. AGB Genk already mined. AGB Lille liquidation. Leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. IOK Afvalbeheer 0862.457.484 CDN 2026-00306548 also live — leftover-next (not taken; leftover AGB first). Distinct from already-mined AGB Tielt 1405 / AGB Patri 1407 / Sunfin 1410 / IGO 1409. First confirmed not already extracted as JR2025 WVV euros: tick 1313 unpublished stub only. KBO Actief / normale toestand since **26.10.2009**; statutaire naam Autonoom Gemeentebedrijf Merchtem / afkorting AGB Merchtem since 26.10.2009; Autonoom gemeentebedrijf since 26.10.2009; zetel Nieuwstraat 1 1785 Merchtem since 26.10.2009; **0 VE**; tel 052/38.11.75; fax 052/37.41.55; KBO no email/web; official site https://www.merchtem.be/AGB; NACE 93.110; aanbestedende overheid since 26.10.2009; btw since 13.04.2010. Voorzitter David De Valck (WVV 2.1 since 14.12.2009). Vennoot: Gemeente Merchtem 0207.511.110 (VKT-inb 8). Remuneratieverslag NIHIL. Contact financies@merchtem.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (assets 4925277 vs PDF **4925278**). Not every-10 (next 1420).\n"
        "- EUR strong (primary official WVV VKT-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; **pers 62 empty** / VTE unpublished; VKT-inb 6.1.1/6.2/6.4/6.5/6.7/6.9/7/9/10/12/14-17 not filed; 6.6 commissaris 3705; jaarverslag VKT-inb 7 not filed; commissarisverslag image-only): assets **4925278** (was 5130914); fixed **3505527** / MVA **3504252** (gebouwen **3392597**; machines **85525**; meubilair **23520**; CIP **2611**); IVA empty; FVA **1275** (aanschaf 5025 / niet-opgevraagd 3750); current **1419750**; ST recv **1357567** (trade **29143** / other **1328425**); cash **57860 DROP** vs 110022; prepaid 4323; equity **1413160** (inbreng 5000 onbeschikbaar; reserves 26122; overgedragen 565400; capsub **816638**); uitgestelde belastingen **130013**; schulden **3382104** (LT overige leningen **2734894**; ST **635523** waarvan LT-due **488754** + leveranciers **103167** + tax 4936 + other **38668**; deferred 11687; debt 1-5y 848163 / >5y **1886731**; gov-guaranteed empty); brutomarge **313807** vs 256796; omzet 70 empty; 60/61 empty; pers 62 empty; afschr 285127; andere bedrijfskosten 12744; expl **+16722** vs −38399; fin opbr 23364 (capsub 19476); fin kosten 100; tax −38 (onttrekking uitgestelde 6492); PnL **+46516** vs −7310; vergoeding inbreng **25000** vs 0; to overgedragen 565400; capex **48876**; commissaris **3705**; remuneratieverslag NIHIL.\n"
        "- CSVs: sources +4; entities patch `agb_merchtem` notes only (no new entity); budgets +48 executed; commitments +1 envelope 313807 AV 29.06.2026; leaderboard +1 annual 313807 / total 4925278; foi_queue +1 status=ready never sent; research_queue surgical rq_1411=done + rq_1412 spawn; loop_state ticks_completed=1411.\n"
        "- FOI: `gap_mrch_omzet_empty_recv_1_33m_debt_3_38m_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / pers empty / ST recv 1328425 counterpart / LT loans 2734894 counterpart / jaarverslag VKT-inb 7 not filed / commissarisverslag image-only.\n"
        "- Next: rq_1412 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IGS IOK Afvalbeheer 0862.457.484 CDN 2026-00306548 live — take if leftover AGB first empty. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Skip Motena / Trupark / Zorgbedrijf ST / already-mined AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Haviland 1370 / Aquaduin/IWVA 1349 / ECO2050 1360 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot still 2024).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1411")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1411 rq/state/log done")
