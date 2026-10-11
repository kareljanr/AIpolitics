#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:45:00Z"
GAP = "gap_rpsk_omzet_empty_bruto_neg_cash_drop_l5"

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
    if not last_s.startswith("rq_1431,"):
        raise SystemExit(f"expected last row rq_1431, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1431 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1431,Erfgoed Rupelstreek JR2025 leftover dual residual,hole_fill,5,done,L5,igs_rpsk,"
        "Completed: Erfgoed Rupelstreek leftover IGS projectvereniging / IOED of 5 mined Rupelstreek cities after leftover AGB hunt; KBO 0822.286.618 Actief; live JR2025 official NBB WVV MIC-inb PDF (40153 bytes 10p deposit 2026-00079897; AV 23.03.2026; created 15.04.2026; neerlegging 2026-04-15; externe accountant YvR Accountancy no commissaris); sourced euros assets 58035 omzet empty diensten empty pers empty pnl -10998 equity 58035 cash 31653 debt 0 capex 0 dividend 0; FOI ready empty 70/60/61/62 / negative bruto / cash drop / continuity,"
        f"{GAP},2026-08-19T11:30:00Z,{TS},"
        "tick1431 Erfgoed Rupelstreek leftover IGS residual; KBO 0822.286.618; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1432 residual dual L5 VL"
    )
    spawn = (
        "rq_1432,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1431 done including Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover RL Schelde-Durme VZW 0889.859.093 JR2025 CDN 2026-00106166 LIVE — STRONG next leftover IGS (after leftover AGB/IOED; distinct from PV RL Schelde-Durme 0680.397.590 still no JR); leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
        f"{TS},{TS},"
        "spawned tick1431 after Erfgoed Rupelstreek leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Schelde-Durme VZW if 2025 CDN still live"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1431=done + rq_1432 spawned; keep", last_line_start)

def write_loop_state() -> None:
    p = DATA / "loop_state.csv"
    notes = (
        "tick1431 Erfgoed Rupelstreek leftover IGS residual; KBO 0822.286.618; live JR2025 NBB WVV PDF; sourced euros assets 58035 omzet empty diensten empty pers empty pnl -10998 equity 58035 cash 31653 debt 0 capex 0 dividend 0; FOI ready empty 70/60/61/62 / negative bruto / cash drop / continuity; next rq_1432 residual dual L5 VL leftover RL Schelde-Durme VZW if 2025 CDN still live; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1431,1431,no,{notes}\n"
    )
    p.write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1431")

def append_loop_log() -> None:
    p = ROOT / "docs/doge/loop_log.md"
    entry = (
        "\n## Tick 1431 - 2026-08-19 - rq_1431 Erfgoed Rupelstreek dual residual leftover\n"
        "- Unit: Erfgoed Rupelstreek (leftover IGS / projectvereniging / IOED of 5 mined Rupelstreek cities; 0 VE) after residual dual hunt (KBO **0822.286.618**; official erfgoedrupelstreek.be; live NBB WVV MIC-inb deposit **2026-00079897** PDF 40153 bytes / 10p; AV **23.03.2026**; created **15.04.2026**; neerlegging **2026-04-15**; model **MIC-inb** 25.0.11 m87-f; externe accountant YvR Accountancy & Tax 0425.179.011 / lid 50529111 opdracht A+B; no commissaris; MIC-inb 6.1.1/6.1.2/6.1.3/6.2/6.3/6.4/6.6/7-16 not filed; 6.5 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover IGS Erfgoed Rupelstreek statutory CDN live this tick (HTTP 200 / application/pdf / 40153 / 10p; SBM jaar **2025-12-31**; neerlegging 2026-04-15) — taken (hunt order #2 leftover unmined IGS / IOED projectvereniging named STRONG next from 1430 with full WVV balans). Distinct from already-mined RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / IVBO (Brugge-en-Ommeland afval — not this IOED) / Zuidrand. First confirmed not already extracted as JR2025 WVV euros: no Erfgoed Rupelstreek / 0822.286.618 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **13.11.2009**; statutaire naam ERFGOED RUPELSTREEK since 13.11.2009; Projectvereniging since 13.11.2009; zetel Schommelei 1 2850 Boom (Provinciaal Domein De Schorre) since 13.11.2009; **0 VE**; KBO no tel/e-mail/web/NACE/btw; official site https://erfgoedrupelstreek.be/; kantoor Hoogstraat 27 2850 Boom; e-mail info@erfgoedrupelstreek.be; coordinator tom@erfgoedrupelstreek.be; aanbestedende overheid since 13.11.2009. WVV 2.1 voorzitter Goris Vera (Schelle); ondervoorzitter Devlies Els (Rumst); bestuurders Roekaerts Tibo (Boom) / Goossens Rita (Hemiksem) / Breugelmans Kelly (Niel). Official site gemeenten: Boom / Hemiksem / Niel / Rumst / Schelle. Named share-% unpublished. Contact info@erfgoedrupelstreek.be. NBB consult skipped (403/SPA); euros extracted from the official MIC-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1440).\n"
        "- EUR strong (primary official WVV MIC-inb; **omzet 70 empty**; **60/61 empty** so diensten unpublished as a split; **pers 62 empty** / VTE unpublished; only negative brutomarge published): assets **58035** (was 69033); fixed empty / IVA empty / MVA empty / FVA empty; current **58035**; ST recv empty; cash **31653 DROP** vs 38681; prepaid **26382** vs 30352; equity **58035** (inbreng onbeschikbaar 20393; overgedragen 37642 DROP vs 48640); voorzieningen empty; schulden empty / **0**; brutomarge **−10959** vs −6602; omzet empty; 60/61 empty; pers empty; expl **−10959** vs −6602; fin kosten **39**; tax empty; PnL **−10998** vs −6640; dividend **0**; over te dragen **37642**; capex **0**. Continuity note: going-concern retained despite current and prior-year losses because of structural financing by the deelnemende gemeenten.\n"
        "- CSVs: sources +4; entities +1 `igs_rpsk` parent `sec_flanders`; budgets +20 executed; commitments +1 envelope 10959 AV 23.03.2026; leaderboard +1 annual 10959 / total 58035; foi_queue +1 status=ready never sent; research_queue surgical rq_1431=done + rq_1432 spawn; loop_state ticks_completed=1431.\n"
        "- FOI: `gap_rpsk_omzet_empty_bruto_neg_cash_drop_l5` ready not sent — omzet 70 empty / diensten 60/61 empty / pers empty / negative bruto / cash drop / EV drop / continuity two loss years / vennoten share-pct / relation to RL Rivierenland / commissaris unpublished.\n"
        "- Next: rq_1432 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Schelde-Durme VZW **0889.859.093** JR2025 CDN **2026-00106166** LIVE — STRONG next leftover IGS (after leftover AGB/IOED; distinct from PV RL Schelde-Durme 0680.397.590 still no JR). Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR).\n"
    )
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    p.write_bytes(raw + entry.encode("utf-8"))
    print("loop_log appended tick 1431")

if __name__ == "__main__":
    patch_research_queue()
    write_loop_state()
    append_loop_log()
    print("tick1431 rq/state/log done")
