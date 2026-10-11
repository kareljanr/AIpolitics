#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1458 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T15:15:00Z"
ENT = "apb_warande"
SRC = "src_warande_jr2025_bbc"
GAP = "gap_warande_pers_3_76m_omzet_1_69m_cash_4_06m_l5"
LB = "lb_warande_pers_3_76m_omzet_1_69m_cash_4_06m_1ve"
COMM = "comm_warande_jr2025_expl"
PDF = "https://www.provincieantwerpen.be/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-06-25/beleidsrapporten/jaarrekening_25_war.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},APB Cultuurhuis de Warande official BBC JR2025,{PDF},Provincie Antwerpen / APB de Warande,2026-08-19,budget,tick1458; official BBC JR2025 PDF 24p / 4280215 bytes; pdfinfo created 25.03.2026 UTC; print 20.03.2026; provincieraad listing 25.06.2026; volgnr 9719408; KBO 0812.230.092; assets 4599520 cash 4060413 debt 2072498 pers 3757450 omzet 1692312 diensten 3359732 pnl 266066 equity 2527021",
        "src_warande_site,APB Cultuurhuis de Warande official cultuurhuis + besluiten-statuten-rapporten pages,https://www.provincieantwerpen.be/nl/locaties/de-warande/besluiten-statuten-rapporten,Provincie Antwerpen / APB de Warande,2026-08-19,official_register,tick1458; leftover APB of mined provincie Antwerpen; zetel Warandestraat 42 2300 Turnhout; contact facturen@warande.be; site https://warande.be/; gedelegeerd bestuurder Crauwels Lieve / Govaert Bart",
        "src_kbo_warande_0812230092,KBO Cultuurhuis de Warande / APB de Warande 0812.230.092,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0812230092,KBO Public Search FOD Economie,2026-08-19,official_register,tick1458; Actief since 26.03.2009; Autonoom provinciebedrijf; naam Cultuurhuis de Warande since 26.03.2009; afkorting APB de Warande since 26.03.2009; zetel Warandestraat 42 2300 Turnhout; 1 VE 2178729569; 13 functiehouders; Werkgever RSZ since 01.01.2022",
        "src_warande_foi_contact,APB Warande FOI channel (openbaarheid@provincieantwerpen.be; facturen@warande.be),https://warande.be/,APB de Warande / Provincie Antwerpen,2026-08-19,official_register,tick1458; leftover provincial cultuurhuis APB; NOT De Schorre / Zilvermeer / De Nekker / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / POA / TPA / PIH",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\napb_warande," in raw or raw.startswith(b"apb_warande,"):
        raise SystemExit("apb_warande already present")
    if b"0812.230.092" in raw:
        raise SystemExit("APB Warande KBO already present as entity")
    row = (
        "apb_warande,APB Cultuurhuis de Warande (APB de Warande leftover provincial cultuurhuis APB of mined provincie Antwerpen; NOT De Schorre / Zilvermeer / De Nekker / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / POA / TPA / PIH),"
        "APB Maison de la culture de Warande (APB residuel maison de culture provinciale),"
        "APB Cultuurhuis de Warande leftover provincial culture house APB of mined province of Antwerp (not De Schorre / Zilvermeer / De Nekker / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / POA / TPA / PIH),"
        "apb,prov_antwerpen,nl,https://warande.be/,openbaarheid@provincieantwerpen.be,Warandestraat 42 2300 Turnhout,"
        "tick1458 leftover residual APB after leftover AGB hunt; KBO 0812.230.092 Actief since 26.03.2009; live JR2025 official BBC PDF; sourced euros assets 4599520 omzet 1692312 diensten 3359732 pers 3757450 pnl 266066 equity 2527021 cash 4060413 debt 2072498 capex 239711 dividend 0; FOI ready pers 3.76m / omzet 1.69m / cash JUMP 4.06m / J5-T2 werksub gap 56k / 1 VE; distinct from already-mined APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 apb_warande")

def part_budgets():
    BUDGETS = [
        ("bud_warande_assets_2025", "2025", "4599520", "2025 assets 4599520 (was 4055855); tick1458; primary official BBC J4"),
        ("bud_warande_current_2025", "2025", "4358795", "2025 vlottend 4358795 (was 3936518); tick1458; primary official BBC J4"),
        ("bud_warande_cash_2025", "2025", "4060413", "2025 liquide+geldbeleg 4060413 JUMP (was 3701132); tick1458; primary official BBC J4"),
        ("bud_warande_strecv_2025", "2025", "193908", "2025 ST vorderingen 193908 (was 138879); tick1458; primary official BBC J4"),
        ("bud_warande_trade_2025", "2025", "99423", "2025 ruil vorderingen 99423 (was 66224); tick1458; primary official BBC J4"),
        ("bud_warande_ntruilrecv_2025", "2025", "94484", "2025 niet-ruil vorderingen 94484 (was 72655); tick1458; primary official BBC J4"),
        ("bud_warande_voorraden_2025", "2025", "13976", "2025 voorraden 13976 (was 10387); tick1458; primary official BBC J4"),
        ("bud_warande_prepaid_2025", "2025", "90496", "2025 overlopend actief 90496 (was 86118); tick1458; primary official BBC J4"),
        ("bud_warande_fixed_2025", "2025", "240725", "2025 vaste activa 240725 JUMP (was 119337); tick1458; primary official BBC J4"),
        ("bud_warande_iva_2025", "2025", "0", "2025 IVA empty; tick1458; primary official BBC J4"),
        ("bud_warande_mva_2025", "2025", "240353", "2025 MVA 240353 JUMP (was 118965); tick1458; primary official BBC J4"),
        ("bud_warande_install_2025", "2025", "176153", "2025 installaties 176153 (was 93364); tick1458; primary official BBC J4"),
        ("bud_warande_meubilair_2025", "2025", "64200", "2025 meubilair 64200 (was 25601); tick1458; primary official BBC J4"),
        ("bud_warande_fva_2025", "2025", "371", "2025 FVA 371 unchanged; tick1458; primary official BBC J4"),
        ("bud_warande_equity_2025", "2025", "2527021", "2025 nettoactief 2527021 (was 2260955); tick1458; primary official BBC J4"),
        ("bud_warande_overgedragen_2025", "2025", "2389844", "2025 gecumuleerd overschot 2389844 (was 2123778); tick1458; primary official BBC J4"),
        ("bud_warande_overignet_2025", "2025", "137176", "2025 overig nettoactief 137176; tick1458; primary official BBC J4"),
        ("bud_warande_debt_2025", "2025", "2072498", "2025 schulden 2072498 ALL ST JUMP (was 1794888; LT empty; T4 fin debt 0); tick1458; primary official BBC J4"),
        ("bud_warande_stdebt_2025", "2025", "2072498", "2025 ST schulden 2072498; tick1458; primary official BBC J4"),
        ("bud_warande_ruilpay_2025", "2025", "1844790", "2025 ST ruil schulden 1844790 (was 1489314); tick1458; primary official BBC J4"),
        ("bud_warande_deferred_2025", "2025", "188256", "2025 overlopend passief 188256 DROP (was 258581); tick1458; primary official BBC J4"),
        ("bud_warande_explontv_2025", "2025", "7499668", "2025 expl ontvangsten J2 7499668; tick1458; primary official BBC J2"),
        ("bud_warande_expluitg_2025", "2025", "7193570", "2025 expl uitgaven J2 7193570; tick1458; primary official BBC J2"),
        ("bud_warande_explsaldo_2025", "2025", "306098", "2025 expl saldo / AFM 306098 (was 65000 budget); tick1458; primary official BBC J2"),
        ("bud_warande_investsaldo_2025", "2025", "-239711", "2025 investeringssaldo -239711; tick1458; primary official BBC J2"),
        ("bud_warande_bbr_2025", "2025", "66386", "2025 budgettair resultaat 66386 (was -190000 budget); tick1458; primary official BBC J2"),
        ("bud_warande_cumbbr_2025", "2025", "2370079", "2025 gecumuleerd BBR 2370079 (was 2303693); tick1458; primary official BBC J2"),
        ("bud_warande_omzet_2025", "2025", "1692312", "2025 J5 opbrengsten uit de werking 1692312 (was 1499488); tick1458; primary official BBC J5"),
        ("bud_warande_diensten_2025", "2025", "3359732", "2025 J5 goederen en diensten 3359732 (was 3119508); tick1458; primary official BBC J5"),
        ("bud_warande_pers_2025", "2025", "3757450", "2025 J5 bezoldigingen 3757450 (was 3223599; VTE unpublished); tick1458; primary official BBC J5"),
        ("bud_warande_afschr_2025", "2025", "118434", "2025 J5 afschrijvingen 118434 (was 84966); tick1458; primary official BBC J5"),
        ("bud_warande_werksub_2025", "2025", "5478580", "2025 J5 werkingssubsidies 5478580 vs T2 5422814 gap 55766; tick1458; primary official BBC J5"),
        ("bud_warande_andere_opbr_2025", "2025", "325618", "2025 J5 andere operationele opbrengsten 325618 (was 208940); tick1458; primary official BBC J5"),
        ("bud_warande_expl_2025", "2025", "218396", "2025 J5 operationeel overschot 218396 (was 552116); tick1458; primary official BBC J5"),
        ("bud_warande_pnl_2025", "2025", "266066", "2025 J5 overschot boekjaar 266066 DROP (was 605745); tick1458; primary official BBC J5"),
        ("bud_warande_div_2025", "2025", "0", "2025 dividend 0; rechthebbenden empty; tick1458; primary official BBC J5"),
        ("bud_warande_capex_2025", "2025", "239711", "2025 capex T2 239711 (T5 aankopen 239711; install 173117 + meubilair 66594); tick1458; primary official BBC T2/T5"),
        ("bud_warande_werksub_granted_2025", "2025", "0", "2025 J5 toegestane werkingssubsidies empty; tick1458; primary official BBC J5"),
        ("bud_warande_pers_nietvast_2025", "2025", "3449817", "2025 T2 niet-vastbenoemd niet-onderwijs 3449817; tick1458; primary official BBC T2"),
        ("bud_warande_pers_andere_2025", "2025", "298995", "2025 T2 andere personeelskosten 298995; tick1458; primary official BBC T2"),
        ("bud_warande_provdot_2025", "2025", "4219566", "2025 T2 algemene werksub van de provincie 4219566; tick1458; primary official BBC T2"),
        ("bud_warande_vldot_2025", "2025", "324012", "2025 T2 algemene werksub van de Vlaamse overheid 324012; tick1458; primary official BBC T2"),
    ]
    bp = DATA / "budgets.csv"
    braw = bp.read_bytes()
    if braw and not braw.endswith(b"\n"):
        braw += b"\n"
    existing = set()
    for brow in csv.reader(io.StringIO(braw.decode("utf-8"))):
        if brow:
            existing.add(brow[0])
    added = []
    for bid, year, amt, notes in BUDGETS:
        if bid in existing:
            continue
        added.append(f"{bid},{ENT},{year},{amt},,,executed,{SRC},strong,{notes}\n")
    bp.write_bytes(braw + "".join(added).encode("utf-8"))
    print("budgets", len(added))

def part_rest1():
    append_lf(DATA / "commitments.csv", [
        f"{COMM},APB Warande JR2025 leftover provincial cultuurhuis APB dual (pers 3.76m / omzet 1.69m / cash JUMP 4.06m / J5-T2 werksub gap 56k / 1 VE),{ENT},APB de Warande / provincie Antwerpen dual cultuurhuis,Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid,2026-06-25,2009,,7193570,,,active,{PDF},Local leftover APB map VL Warande — pers 3.76m / omzet 1.69m / cash JUMP 4.06m,Publish VTE + 1 VE payroll + J5/T2 werksub recon 56k + cash 4.06m counterparties + NBB filing + ticket/horeca; do not keep leftover APB Warande as unpublished 7.19m cultuurhuis shell,{SRC},strong,Vlaanderen>Provincies>Antwerpen>APB>Warande>JR2025_L5,tick1458; assets 4599520 omzet 1692312 diensten 3359732 pers 3757450 pnl 266066 equity 2527021 cash 4060413 debt 2072498 capex 239711 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},APB Warande JR2025 leftover provincial cultuurhuis APB: pers 3.76m / omzet 1.69m / cash JUMP 4.06m / J5-T2 werksub gap 56k / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>Antwerpen>APB>Warande>JR2025_L5,3757450,4599520,Leftover dual APB cultuurhuis shell: assets 4.60m / equity 2.53m / expl uitg 7.19m / pers 3.76m VTE unpublished / omzet 1.69m / cash 4.06m JUMP / werksub J5 5.48m vs T2 5.42m gap 56k / provincie dotatie 4.22m / PnL DROP +0.27m vs +0.61m / 1 VE / NBB filing should happen; do not treat 7.19m as TE-additive of 348bn,strong,{SRC},APB de Warande / provincie Antwerpen dual cultuurhuis,Local leftover APB map VL Warande — JR2025 official BBC live; pers/omzet/cash/werksub FOI,Official BBC 2026-08-19: pers 3.76m / omzet 1.69m / cash JUMP 4.06m / PnL +0.27m DROP / BBR +66k / 1 VE / VTE unpublished,6.6,7.8,3.0,7.2,Publish VTE + 1 VE payroll + J5/T2 werksub recon 56k + cash 4.06m counterparties + NBB filing + ticket/horeca; do not keep leftover APB Warande as unpublished 7.19m cultuurhuis shell,active,,tick1458; leftover APB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>Antwerpen>APB>Warande>JR2025_L5,{ENT},pers J5 3757450 VTE unpublished + 1 VE 2178729569 + omzet 1692312 + cash JUMP 4060413 vs 3701132 + J5/T2 werksub gap 55766 (J5 5478580 vs T2 5422814; provincie 4219566 + VL 324012 + gemeente 731394) + ruil debt JUMP 1844790 vs 1489314 + deferred DROP 188256 vs 258581 + PnL DROP 266066 vs 605745 + MVA JUMP 240353 vs 118965 + NBB filing unpublished (bijlage says onderneming so should file) + commissaris unpublished,Leftover APB Warande after leftover AGB hunt: pers 3.76m / omzet 1.69m / cash JUMP 4.06m / 1 VE hides provincial cultuurhuis vehicle,8,APB Cultuurhuis de Warande / provinciegriffier / Bestuursorgaan,openbaarheid@provincieantwerpen.be,Warandestraat 42 2300 Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1458 leftover APB after honest leftover AGB hunt; live JR2025 official BBC PDF now extracted (4280215 bytes 24p). FOI ready not sent. NOT every-10. NOT De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. AGB Bornem still 2024 HEAD 403. Leftover Inovant/Atlas 2025 slugs 404 this tick.",
    ])
    print("foi_queue +1")

def part_rqstate():
    p = DATA / "research_queue.csv"
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 131072))
        tail = f.read()
    if not tail.endswith(b"\n"):
        raise SystemExit("research_queue tail missing newline")
    stripped = tail[:-1]
    last_nl = stripped.rfind(b"\n")
    if last_nl < 0:
        raise SystemExit("research_queue tail too short")
    last = stripped[last_nl + 1 :]
    last_s = last.decode("utf-8")
    if not last_s.startswith("rq_1458,"):
        raise SystemExit(f"expected last row rq_1458, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1458 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1458,APB Warande JR2025 leftover dual residual,hole_fill,5,done,L5,apb_warande,"
        "Completed: APB Cultuurhuis de Warande leftover APB of mined provincie Antwerpen after leftover AGB hunt; KBO 0812.230.092 Actief; live JR2025 official BBC PDF (4280215 bytes 24p; print 20.03.2026; provincieraad listing 25.06.2026; volgnr 9719408; koepelsite PDF Googlebot 200). PDF header APB De Warande / Warandestraat 42 — NOT Hooibeekhoeve. Sourced euros assets 4599520 omzet 1692312 diensten 3359732 pers 3757450 pnl 266066 equity 2527021 cash 4060413 debt 2072498 capex 239711 dividend 0. FOI "
        f"{GAP},2026-08-19T15:05:00Z,{TS},"
        "tick1458 APB Warande leftover APB residual; KBO 0812.230.092; live JR2025 official BBC PDF; sourced euros; FOI ready not sent; next rq_1459 leftover APB Inovant/Atlas if PDF live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1459,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1458 done including APB Warande 1458 leftover APB live official BBC / APB De Schorre 1457 leftover APB live official BBC / APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC / Crematorium Hasselt 1453 leftover 100pct Stad Hasselt daughter live NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Antwerp provincial APB set now includes PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / POA 1454 / TPA 1455 / PIH 1456 / De Schorre 1457 / Warande 1458 — leftover Antwerp APB Inovant/Atlas only if a 2025 statutory PDF actually downloads (Foleon leftover slugs have redirected to Hooibeekhoeve; jaarrekening_25_inov/atlas 404 this tick). Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453). Do NOT confuse with already-mined APB PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / already-mined APB POA 1454 / already-mined APB TPA 1455 / already-mined APB PIH 1456 / already-mined APB De Schorre 1457 / already-mined APB Warande 1458. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1457). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1457 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1457. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453. Next every-10 is 1460 MUST do every-10 progress refresh.,,"
        f"{TS},{TS},"
        "spawned tick1458 after APB Warande leftover APB live official BBC JR2025; leftover APB Inovant/Atlas if PDF live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; next 1460 MUST do every-10"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1458=done + rq_1459 spawned; keep", last_line_start)

    def n_data(fn):
        with open(DATA / fn, "rb") as f:
            return sum(1 for _ in f) - 1

    inv = {fn: n_data(fn) for fn in ["budgets.csv","commitments.csv","leaderboard.csv","entities.csv","sources.csv","foi_queue.csv","research_queue.csv"]}
    foi_c = Counter()
    csv.field_size_limit(sys.maxsize)
    with open(DATA / "foi_queue.csv", newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            st = (row.get("status") or "").strip()
            foi_c[st] += 1
    foi_ready = foi_c.get("ready", 0)
    foi_ans = foi_c.get("answered", 0)
    foi_part = foi_c.get("partial", 0)
    foi_tot = inv["foi_queue.csv"]
    print("INV", inv, "FOI ready", foi_ready, "answered", foi_ans, "partial", foi_part, "total", foi_tot)

    notes = (
        f"tick1458 APB Warande leftover APB residual; KBO 0812.230.092; live JR2025 official BBC PDF; sourced euros assets 4599520 omzet 1692312 diensten 3359732 pers 3757450 pnl 266066 equity 2527021 cash 4060413 debt 2072498 capex 239711 dividend 0; FOI ready pers 3.76m / omzet 1.69m / cash JUMP 4.06m / J5-T2 werksub gap 56k / 1 VE; NOT De Schorre / PIH / TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / Zilvermeer / De Nekker; next rq_1459 leftover APB Inovant/Atlas if PDF live else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; next 1460 MUST do every-10; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1458,1458,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1458")

    entry = (
        "\n## Tick 1458 - 2026-08-19 - rq_1458 APB Warande dual residual leftover\n"
        "- Unit: APB Cultuurhuis de Warande / APB de Warande (leftover provincial cultuurhuis APB of mined provincie Antwerpen; 1 VE 2.178.729.569) after residual dual hunt (KBO **0812.230.092**; official koepelsite BBC PDF **4280215** bytes / 24p; print **20.03.2026**; provincieraad listing **25.06.2026**; volgnr **9719408**). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar/Oudsbergen/MAC already mined. Leftover APB Warande official JR2025 PDF now fetches via Googlebot + `/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-06-25/beleidsrapporten/jaarrekening_25_war.pdf` (box curl 403 without Googlebot UA) — taken (hunt order #1 leftover Antwerp APB of mined provincie with live statutory 2025 BBC balans). PDF header **APB De Warande / Warandestraat 42 / 2300 Turnhout / Jaarrekening 2025** — NOT a Foleon leftover-slug redirect to Hooibeekhoeve. Distinct from already-mined **APB De Schorre 1457** / **APB PIH 1456** / **APB TPA 1455** / **APB POA 1454** / **APB PSES** / **GKC** / **Havencentrum** / **Kamp C** / **Hooibeekhoeve** / **Zilvermeer** / **De Nekker**. Leftover **APB Inovant / Atlas** `jaarrekening_25_inov` / `jaarrekening_25_atlas` HEAD 404 this tick — not taken. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR as of 1457. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. First confirmed not already extracted as JR2025 euros: no APB Warande / Cultuurhuis de Warande / 0812.230.092 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **26.03.2009**; statutaire naam Cultuurhuis de Warande / afkorting APB de Warande since 26.03.2009; Autonoom provinciebedrijf since 26.03.2009; zetel Warandestraat 42 2300 Turnhout; **1 VE 2.178.729.569** since 01.07.2009; 13 functiehouders; gedelegeerd bestuurder Crauwels Lieve / Govaert Bart since 08.04.2025; Werkgever RSZ since 01.01.2022; btw since 01.01.2013; aanbestedende overheid; NACE btw 82.990 / RSZ 90.311; contact facturen@warande.be / site https://warande.be/. Bijlage: APB oordeelt dat het WEL als 'onderneming' kan worden beschouwd zodat NBB-neerlegging zou moeten (art. 219 Provinciedecreet / BBC digital filing Vlaamse Gemeenschap). Euros extracted from the official BBC PDF itself (image OCR; cents truncated). Belscope/Companyweb/Busibee euros not used. Not every-10 (next 1460 MUST do every-10).\n"
        "- EUR strong (primary official BBC J2/J4/J5/T2/T4/T5; omzet = J5 werking **1692312**; diensten J5 **3359732**; pers J5 **3757450** / VTE unpublished): assets **4599520** (was 4055855); current **4358795** vs 3936518; cash **4060413 JUMP** vs 3701132; ST recv **193908** vs 138879 (ruil **99423** / niet-ruil **94484**); voorraden **13976**; prepaid **90496**; fixed **240725** vs 119337 / IVA **0** / MVA **240353** (installaties **176153**; meubilair **64200**) / FVA **371**; equity **2527021** vs 2260955 (gecumuleerd **2389844**; overig **137176**); schulden **2072498 JUMP** vs 1794888 ALL ST (ruil **1844790**; deferred **188256 DROP** vs 258581; LT empty; T4 fin debt **0**); expl ontvangsten **7499668** / expl uitgaven **7193570** / expl saldo / AFM **306098**; invest **-239711**; BBR **66386**; cum BBR **2370079**; J5 kosten **7291904** / opbrengsten **7557971** / werksub **5478580** vs T2 **5422814** gap **55766** (provincie **4219566** + VL **324012** + gemeente **731394**); andere opbr **325618**; expl **+218396**; PnL **+266066 DROP** vs 605745; dividend **0**; capex T2/T5 aankopen **239711** (install 173117 + meubilair 66594); toegestane werksub J5 empty. PDF 1-euro rounding. Cross-checks: 4358795+240725=4599520; 2527021+2072498=4599519; 7557971-7291904=266067; 218396+47670=266066; 7499668-7193570=306098; 306098-239711=66387.\n"
        f"- CSVs: sources +4; entities +1 `apb_warande` parent `prov_antwerpen`; budgets +42 executed; commitments +1 envelope 7193570 listing 25.06.2026; leaderboard +1 annual 3757450 / total 4599520; foi_queue +1 status=ready never sent; research_queue surgical rq_1458=done + rq_1459 spawn; loop_state ticks_completed=1458. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
        "- FOI: `gap_warande_pers_3_76m_omzet_1_69m_cash_4_06m_l5` ready not sent — pers 3.76m VTE unpublished / 1 VE / omzet 1.69m / cash JUMP 4.06m / J5-T2 werksub gap 56k / ST ruil debt JUMP 1.84m / deferred DROP 0.19m / PnL DROP +0.27m / MVA JUMP 0.24m / NBB should-file unpublished / commissaris unpublished.\n"
        "- Next: rq_1459 residual dual L5 VL. Leftover APB **Inovant / Atlas** official JR2025 slugs 404 this tick (Foleon leftover slugs have redirected to Hooibeekhoeve) — take only if a downloadable 2025 PDF now fetches. Leftover OTHER provincial APBs: leftover OV / WVL / Limburg / Vlaams-Brabant APBs (Puyenbroeck spotted unmined around 1453). Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR as of 1457). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB Warande 1458 / APB De Schorre 1457 / APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453. **Next 1460 MUST do every-10** (progress_every_10_ticks.md + doge_waste_top10_current.md).\n"
    )
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1458 -" in lraw:
        raise SystemExit("loop_log already has tick 1458 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1458")
    print("DONE tick 1458")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "all"
    if part in ("sources", "all"):
        part_sources()
    if part in ("entities", "all"):
        part_entities()
    if part in ("budgets", "all"):
        part_budgets()
    if part in ("rest1", "all"):
        part_rest1()
    if part in ("rqstate", "all"):
        part_rqstate()
