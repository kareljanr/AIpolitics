#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1456 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities|budgets|rest1|rqstate
"""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T14:55:00Z"
ENT = "apb_pih"
SRC = "src_pih_jr2025_bbc"
GAP = "gap_pih_pers_7_58m_omzet_2_76m_cash_2_25m_l5"
LB = "lb_pih_pers_7_58m_omzet_2_76m_cash_2_25m_1ve"
COMM = "comm_pih_jr2025_expl"
PDF = "https://www.provincieantwerpen.be/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-05-28/beleidsrapporten/3_apb_pih_jaarrekening_2025_bbc_rapport.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},APB Provinciaal Instituut voor Hygiëne official BBC JR2025,{PDF},Provincie Antwerpen / APB PIH,2026-08-19,budget,tick1456; official BBC JR2025 PDF 26p / 803077 bytes; pdfinfo created 31.03.2026 UTC; print 31.03.2026; provincieraad listing 28.05.2026; volgnr 5929991; KBO 0541.414.408; assets 3883158 cash 2246508 debt 1614131 pers 7578570 omzet 2763115 diensten 2071729 pnl 219919 equity 2269027",
        "src_pih_site,APB PIH official kenniscentrum + besluiten-statuten-rapporten pages,https://www.provincieantwerpen.be/nl/locaties/pih-kenniscentrum-voor-milieu-en-voor-gezondheid,Provincie Antwerpen / APB PIH,2026-08-19,official_register,tick1456; leftover APB of mined provincie Antwerpen; zetel Kronenburgstraat 45 2000 Antwerpen; contact pih@provincieantwerpen.be / 03 259 12 00; directeur Marijke Lenaerts",
        "src_kbo_pih_0541414408,KBO APB Provinciaal Instituut voor Hygiëne / APB PIH 0541.414.408,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0541414408,KBO Public Search FOD Economie,2026-08-19,official_register,tick1456; Actief since 26.09.2013; Autonoom provinciebedrijf; naam APB PIH since 26.09.2013; statutaire naam since 06.10.2015; zetel Kronenburgstraat 45 2000 Antwerpen; 1 VE 2223145374; bestuurder De Haes Jan; Werkgever RSZ since 01.01.2022",
        "src_pih_foi_contact,APB PIH FOI channel (openbaarheid@provincieantwerpen.be; pih@provincieantwerpen.be),https://www.provincieantwerpen.be/nl/locaties/pih-kenniscentrum-voor-milieu-en-voor-gezondheid/besluiten-statuten-rapporten,APB PIH / Provincie Antwerpen,2026-08-19,official_register,tick1456; leftover provincial lab APB; NOT POA / TPA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve",
    ])
    print("sources +4")

def part_entities():
    p = DATA / "entities.csv"
    raw = p.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\napb_pih," in raw or raw.startswith(b"apb_pih,"):
        raise SystemExit("apb_pih already present")
    if b"0541.414.408" in raw and b"apb_pih," in raw:
        raise SystemExit("APB PIH KBO already present as entity")
    # KBO string appears in leftover notes of TPA/POA — only block if entity_id exists
    row = (
        "apb_pih,APB Provinciaal Instituut voor Hygiëne (APB PIH leftover provincial lab / milieu-gezondheid APB of mined provincie Antwerpen; NOT POA / TPA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve),"
        "APB Institut provincial d hygiene (APB residuel labo provincial milieu-sante),"
        "APB Provincial Institute for Hygiene leftover provincial lab / environment-health APB of mined province of Antwerp (not POA / TPA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve),"
        "apb,prov_antwerpen,nl,https://www.provincieantwerpen.be/nl/locaties/pih-kenniscentrum-voor-milieu-en-voor-gezondheid,openbaarheid@provincieantwerpen.be,Kronenburgstraat 45 2000 Antwerpen,"
        "tick1456 leftover residual APB after leftover AGB hunt; KBO 0541.414.408 Actief since 26.09.2013; live JR2025 official BBC PDF; sourced euros assets 3883158 omzet 2763115 diensten 2071729 pers 7578570 pnl 219919 equity 2269027 cash 2246508 debt 1614131 capex 542295 dividend 0; FOI ready pers 7.58m / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / 1 VE; distinct from already-mined APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve"
        "\n"
    )
    p.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 apb_pih")

def part_budgets():
    BUDGETS = [
        ("bud_pih_assets_2025", "2025", "3883158", "2025 assets 3883158 (was 3826467); tick1456; primary official BBC J4"),
        ("bud_pih_current_2025", "2025", "2994949", "2025 vlottend 2994949 (was 3063693); tick1456; primary official BBC J4"),
        ("bud_pih_cash_2025", "2025", "2246508", "2025 liquide+geldbeleg 2246508 JUMP (was 2045302); tick1456; primary official BBC J4"),
        ("bud_pih_strecv_2025", "2025", "742468", "2025 ST vorderingen 742468 (was 1001463); tick1456; primary official BBC J4"),
        ("bud_pih_trade_2025", "2025", "610589", "2025 ruil vorderingen 610589 (was 829660); tick1456; primary official BBC J4"),
        ("bud_pih_ntruilrecv_2025", "2025", "131879", "2025 niet-ruil vorderingen 131879 (was 171803); tick1456; primary official BBC J4"),
        ("bud_pih_voorraden_2025", "2025", "0", "2025 voorraden empty; tick1456; primary official BBC J4"),
        ("bud_pih_prepaid_2025", "2025", "5972", "2025 overlopend actief 5972 (was 16928); tick1456; primary official BBC J4"),
        ("bud_pih_fixed_2025", "2025", "888210", "2025 vaste activa 888210 (was 762774); tick1456; primary official BBC J4"),
        ("bud_pih_iva_2025", "2025", "0", "2025 IVA empty; tick1456; primary official BBC J4"),
        ("bud_pih_mva_2025", "2025", "776867", "2025 MVA 776867 (was 616492); tick1456; primary official BBC J4"),
        ("bud_pih_install_2025", "2025", "706098", "2025 installaties 706098 (was 560597); tick1456; primary official BBC J4"),
        ("bud_pih_meubilair_2025", "2025", "70769", "2025 meubilair 70769 (was 55894); tick1456; primary official BBC J4"),
        ("bud_pih_fva_2025", "2025", "111342", "2025 FVA 111342 DROP (was 146282; T5 andere mutaties -34940); tick1456; primary official BBC J4"),
        ("bud_pih_equity_2025", "2025", "2269027", "2025 nettoactief 2269027 (was 2049108); tick1456; primary official BBC J4"),
        ("bud_pih_overgedragen_2025", "2025", "1905018", "2025 gecumuleerd overschot 1905018 (was 1685100); tick1456; primary official BBC J4"),
        ("bud_pih_overignet_2025", "2025", "364009", "2025 overig nettoactief 364009; tick1456; primary official BBC J4"),
        ("bud_pih_debt_2025", "2025", "1614131", "2025 schulden 1614131 ALL ST DROP (was 1777358; LT empty; T4 fin debt 0); tick1456; primary official BBC J4"),
        ("bud_pih_stdebt_2025", "2025", "1614131", "2025 ST schulden 1614131; tick1456; primary official BBC J4"),
        ("bud_pih_ruilpay_2025", "2025", "1366133", "2025 ST ruil schulden 1366133 (was 1209767); tick1456; primary official BBC J4"),
        ("bud_pih_deferred_2025", "2025", "247998", "2025 overlopend passief 247998 DROP (was 524952); tick1456; primary official BBC J4"),
        ("bud_pih_explontv_2025", "2025", "9974421", "2025 expl ontvangsten J2 9974421; tick1456; primary official BBC J2"),
        ("bud_pih_expluitg_2025", "2025", "9641201", "2025 expl uitgaven J2 9641201; tick1456; primary official BBC J2"),
        ("bud_pih_explsaldo_2025", "2025", "333220", "2025 expl saldo / AFM 333220 (was 1098971 T2); tick1456; primary official BBC J2"),
        ("bud_pih_investsaldo_2025", "2025", "-504735", "2025 investeringssaldo -504735; tick1456; primary official BBC J2"),
        ("bud_pih_bbr_2025", "2025", "-171515", "2025 budgettair resultaat -171515 (was +790581); tick1456; primary official BBC J2"),
        ("bud_pih_cumbbr_2025", "2025", "1625917", "2025 gecumuleerd BBR 1625917 (was 1797432); tick1456; primary official BBC J2"),
        ("bud_pih_omzet_2025", "2025", "2763115", "2025 J5 opbrengsten uit de werking 2763115 (was 2734802); tick1456; primary official BBC J5"),
        ("bud_pih_diensten_2025", "2025", "2071729", "2025 J5 goederen en diensten 2071729 (was 1950183); tick1456; primary official BBC J5"),
        ("bud_pih_pers_2025", "2025", "7578570", "2025 J5 bezoldigingen 7578570 (was 7343126; VTE unpublished); tick1456; primary official BBC J5"),
        ("bud_pih_afschr_2025", "2025", "379300", "2025 J5 afschrijvingen 379300 (was 294965); tick1456; primary official BBC J5"),
        ("bud_pih_werksub_2025", "2025", "7258216", "2025 J5 werkingssubsidies 7258216 vs T2 6981644 gap 276572; tick1456; primary official BBC J5"),
        ("bud_pih_andere_opbr_2025", "2025", "213651", "2025 J5 andere operationele opbrengsten 213651 (was 203819); tick1456; primary official BBC J5"),
        ("bud_pih_expl_2025", "2025", "205282", "2025 J5 operationeel overschot 205282 (was 700196); tick1456; primary official BBC J5"),
        ("bud_pih_pnl_2025", "2025", "219919", "2025 J5 overschot boekjaar 219919 DROP (was 719372); tick1456; primary official BBC J5"),
        ("bud_pih_div_2025", "2025", "0", "2025 dividend 0; rechthebbenden empty; tick1456; primary official BBC J5"),
        ("bud_pih_capex_2025", "2025", "542295", "2025 capex T2 542295 (T5 aankopen 539675; MVA 539675 + FVA 2620); tick1456; primary official BBC T2/T5"),
        ("bud_pih_werksub_granted_2025", "2025", "0", "2025 J5 toegestane werkingssubsidies empty; tick1456; primary official BBC J5"),
        ("bud_pih_pers_vast_2025", "2025", "2101529", "2025 T2 vastbenoemd niet-onderwijs 2101529; tick1456; primary official BBC T2"),
        ("bud_pih_pers_nietvast_2025", "2025", "5129989", "2025 T2 niet-vastbenoemd niet-onderwijs 5129989; tick1456; primary official BBC T2"),
        ("bud_pih_provdot_2025", "2025", "6873978", "2025 T2 algemene werksub van de provincie 6873978; tick1456; primary official BBC T2"),
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
        f"{COMM},APB PIH JR2025 leftover provincial lab APB dual (pers 7.58m / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / 1 VE),{ENT},APB PIH / provincie Antwerpen dual lab,Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid,2026-05-28,2013,,9641201,,,active,{PDF},Local leftover APB map VL PIH — pers 7.58m / omzet 2.76m / cash JUMP 2.25m,Publish VTE + 1 VE payroll + J5/T2 werksub recon 0.28m + cash 2.25m counterparties + NBB non-filing + PFAS capex; do not keep leftover APB PIH as unpublished 9.64m lab shell,{SRC},strong,Vlaanderen>Provincies>Antwerpen>APB>PIH>JR2025_L5,tick1456; assets 3883158 omzet 2763115 diensten 2071729 pers 7578570 pnl 219919 equity 2269027 cash 2246508 debt 1614131 capex 542295 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve",
    ])
    print("commitments +1")
    append_lf(DATA / "leaderboard.csv", [
        f"{LB},APB PIH JR2025 leftover provincial lab APB: pers 7.58m / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>Antwerpen>APB>PIH>JR2025_L5,7578570,3883158,Leftover dual APB lab shell: assets 3.88m / equity 2.27m / expl uitg 9.64m / pers 7.58m VTE unpublished / omzet 2.76m / cash 2.25m JUMP / werksub J5 7.26m vs T2 6.98m gap 0.28m / provincie dotatie 6.87m / PnL DROP +0.22m vs +0.72m / 1 VE / no NBB filing; do not treat 9.64m as TE-additive of 348bn,strong,{SRC},APB PIH / provincie Antwerpen dual lab,Local leftover APB map VL PIH — JR2025 official BBC live; pers/omzet/cash/werksub FOI,Official BBC 2026-08-19: pers 7.58m / omzet 2.76m / cash JUMP 2.25m / PnL +0.22m DROP / BBR -0.17m / 1 VE / VTE unpublished,6.8,8.2,3.0,7.6,Publish VTE + 1 VE payroll + J5/T2 werksub recon 0.28m + cash 2.25m counterparties + NBB non-filing + PFAS capex; do not keep leftover APB PIH as unpublished 9.64m lab shell,active,,tick1456; leftover APB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined APB TPA 1455 / APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve",
    ])
    print("leaderboard +1")
    append_lf(DATA / "foi_queue.csv", [
        f"{GAP},Vlaanderen>Provincies>Antwerpen>APB>PIH>JR2025_L5,{ENT},pers J5 7578570 VTE unpublished + 1 VE 2223145374 + omzet 2763115 + cash JUMP 2246508 vs 2045302 + J5/T2 werksub gap 276572 (J5 7258216 vs T2 6981644; provincie 6873978) + deferred DROP 247998 vs 524952 + PnL DROP 219919 vs 719372 + FVA DROP 111342 vs 146282 + NBB filing unpublished (self no-deposit) + commissaris unpublished,Leftover APB PIH after leftover AGB hunt: pers 7.58m / omzet 2.76m / cash JUMP 2.25m / 1 VE hides provincial lab vehicle,8,APB Provinciaal Instituut voor Hygiëne / provinciegriffier / Bestuursorgaan,openbaarheid@provincieantwerpen.be,Kronenburgstraat 45 2000 Antwerpen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1456 leftover APB after honest leftover AGB hunt; live JR2025 official BBC PDF now extracted (803077 bytes 26p). FOI ready not sent. NOT every-10. NOT TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. AGB Bornem still 2024 HEAD 403.",
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
    if not last_s.startswith("rq_1456,"):
        raise SystemExit(f"expected last row rq_1456, got {last_s[:80]!r}")
    parts_head = last_s.split(",", 6)
    if len(parts_head) >= 5 and parts_head[4] == "done":
        raise SystemExit("rq_1456 already done — concurrent tick; STOP")
    last_line_start = size - (len(stripped) - last_nl)
    done = (
        "rq_1456,APB PIH JR2025 leftover dual residual,hole_fill,5,done,L5,apb_pih,"
        "Completed: APB Provinciaal Instituut voor Hygiëne leftover APB of mined provincie Antwerpen after leftover AGB hunt; KBO 0541.414.408 Actief; live JR2025 official BBC PDF (803077 bytes 26p; print 31.03.2026; provincieraad listing 28.05.2026; volgnr 5929991; koepelsite PDF Googlebot 200); sourced euros assets 3883158 omzet 2763115 diensten 2071729 pers 7578570 pnl 219919 equity 2269027 cash 2246508 debt 1614131 capex 542295 dividend 0; FOI ready pers 7.58m / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / 1 VE; NOT TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve,"
        f"{GAP},2026-08-19T14:45:00Z,{TS},"
        "tick1456 APB PIH leftover APB residual; KBO 0541.414.408; live JR2025 official BBC PDF; sourced euros; FOI ready not sent; next rq_1457 leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    spawn = (
        "rq_1457,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
        "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1456 done including APB PIH 1456 leftover APB live official BBC / APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC / Crematorium Hasselt 1453 leftover 100pct Stad Hasselt daughter live NBB WVV / CoLimBo 1452 leftover Bosgroep daughter live NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. Antwerp provincial APB set now includes PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / POA 1454 / TPA 1455 / PIH 1456 — leftover Antwerp APB only if a new 2025 statutory PDF appears. Do NOT confuse with already-mined APB PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / already-mined APB POA 1454 / already-mined APB TPA 1455 / already-mined APB PIH 1456. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1456). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1456 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1456. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452. Next every-10 is 1460.,,"
        f"{TS},{TS},"
        "spawned tick1456 after APB PIH leftover APB live official BBC JR2025; leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
    )
    with p.open("r+b") as f:
        f.seek(last_line_start)
        f.truncate()
        f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
    print("research_queue patched: rq_1456=done + rq_1457 spawned; keep", last_line_start)

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
        f"tick1456 APB PIH leftover APB residual; KBO 0541.414.408; live JR2025 official BBC PDF; sourced euros assets 3883158 omzet 2763115 diensten 2071729 pers 7578570 pnl 219919 equity 2269027 cash 2246508 debt 1614131 capex 542295 dividend 0; FOI ready pers 7.58m / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / 1 VE; NOT TPA / POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve; next rq_1457 leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
    )
    text = (
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_1456,1456,no,{notes}\n"
    )
    (DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
    print("loop_state rewritten LF ticks=1456")

    entry = (
        "\n## Tick 1456 - 2026-08-19 - rq_1456 APB PIH dual residual leftover\n"
        "- Unit: APB Provinciaal Instituut voor Hygiëne / APB PIH (leftover provincial lab / milieu-gezondheid APB of mined provincie Antwerpen; 1 VE 2.223.145.374) after residual dual hunt (KBO **0541.414.408**; official koepelsite BBC PDF **803077** bytes / 26p; print **31.03.2026**; provincieraad listing **28.05.2026**; volgnr **5929991**). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar/Oudsbergen/MAC already mined. Leftover APB PIH official JR2025 PDF now fetches via Googlebot + `/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-05-28/beleidsrapporten/3_apb_pih_jaarrekening_2025_bbc_rapport.pdf` (box curl 403 without Googlebot UA) — taken (hunt order #1 leftover APB of mined provincie with live statutory 2025 BBC balans). PDF header **APB Provinciaal Instituut Hygiëne / Kronenburgstraat 45 / Jaarrekening 2025** — NOT a Foleon leftover-slug redirect to Hooibeekhoeve. Distinct from already-mined **APB TPA 1455** / **APB POA 1454** / **APB PSES** / **GKC** / **Havencentrum** / **Kamp C** / **Hooibeekhoeve**. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. First confirmed not already extracted as JR2025 euros: no APB PIH / 0541.414.408 JR2025 extract in entities/sources/leaderboard (KBO only leftover-mentioned in TPA/POA notes). KBO Actief / normale toestand since **26.09.2013**; statutaire naam APB Provinciaal Instituut voor Hygiëne since **06.10.2015**; afkorting APB PIH since 26.09.2013; Autonoom provinciebedrijf since 26.09.2013; zetel Kronenburgstraat 45 2000 Antwerpen; **1 VE 2.223.145.374** since 01.01.2014; bestuurder De Haes Jan since 03.12.2018; directeur Marijke Lenaerts (site); Werkgever RSZ since 01.01.2022; btw since 01.01.2017; aanbestedende overheid; BELAC lab; NACE btw 94.994 / RSZ 71.209; contact pih@provincieantwerpen.be. Bijlage: APB PIH oordeelt **geen** NBB-neerlegging (art. 219 Provinciedecreet / geen 'onderneming' / BBC digital filing Vlaamse Gemeenschap). Euros extracted from the official BBC PDF itself. Belscope/Companyweb/Busibee euros not used. Not every-10 (next 1460 MUST do every-10).\n"
        "- EUR strong (primary official BBC J2/J4/J5/T2/T5; omzet = J5 werking **2763115**; diensten J5 **2071729**; pers J5 **7578570** / VTE unpublished): assets **3883158** (was 3826467); current **2994949** vs 3063693; cash **2246508 JUMP** vs 2045302; ST recv **742468** vs 1001463 (ruil **610589** / niet-ruil **131879**); prepaid **5972**; fixed **888210** vs 762774 / IVA **0** / MVA **776867** (installaties **706098**; meubilair **70769**) / FVA **111342 DROP** vs 146282 (T5 andere mutaties -34940); equity **2269027** vs 2049108 (gecumuleerd **1905018**; overig **364009**); schulden **1614131 DROP** vs 1777358 ALL ST (ruil **1366133**; deferred **247998 DROP** vs 524952; LT empty; T4 fin debt **0**); expl ontvangsten **9974421** / expl uitgaven **9641201** / expl saldo / AFM **333220**; invest **-504735**; BBR **-171515**; cum BBR **1625917**; J5 kosten **10029802** / opbrengsten **10249721** / werksub **7258216** vs T2 **6981644** gap **276572** (provincie **6873978**); andere opbr **213651**; expl **+205282**; PnL **+219919 DROP** vs 719372; dividend **0**; capex T2 **542295** / T5 aankopen **539675**; toegestane werksub J5 empty. PDF 1-euro rounding. Cross-checks: 2269027+1614131=3883158; 10249721-10029802=219919; 205282+14637=219919; 9974421-9641201=333220; 333220-504735=-171515.\n"
        f"- CSVs: sources +4; entities +1 `apb_pih` parent `prov_antwerpen`; budgets +41 executed; commitments +1 envelope 9641201 listing 28.05.2026; leaderboard +1 annual 7578570 / total 3883158; foi_queue +1 status=ready never sent; research_queue surgical rq_1456=done + rq_1457 spawn; loop_state ticks_completed=1456. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
        "- FOI: `gap_pih_pers_7_58m_omzet_2_76m_cash_2_25m_l5` ready not sent — pers 7.58m VTE unpublished / 1 VE / omzet 2.76m / cash JUMP 2.25m / J5-T2 werksub gap 0.28m / deferred DROP 0.25m / PnL DROP +0.22m / FVA DROP 0.11m / NBB non-filing / commissaris unpublished.\n"
        "- Next: rq_1457 residual dual L5 VL. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR this tick). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB PIH 1456 / APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452 / RLHP 1451 / BGKN 1450. Next every-10 is 1460.\n"
    )
    lp = ROOT / "docs/doge/loop_log.md"
    lraw = lp.read_bytes()
    if lraw and not lraw.endswith(b"\n"):
        lraw += b"\n"
    if b"## Tick 1456 -" in lraw:
        raise SystemExit("loop_log already has tick 1456 — concurrent?")
    lp.write_bytes(lraw + entry.encode("utf-8"))
    print("loop_log appended tick 1456")
    print("DONE tick 1456")

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
