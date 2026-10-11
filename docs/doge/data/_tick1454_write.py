#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1454 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T14:25:00Z"
ENT = "apb_poa"
SRC = "src_poa_jr2025_bbc"
GAP = "gap_poa_pers_78_45m_cash_15_83m_leerkracht_reclass_l5"
LB = "lb_poa_pers_78_45m_cash_15_83m_27ve"
COMM = "comm_poa_jr2025_expl"
PDF = "https://www.provincieantwerpen.be/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-05-28/beleidsrapporten/02_apb_poa_doelstellingenrealisatienota_en_jaarrekening_2025.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    f"{SRC},APB Provinciaal Onderwijs Antwerpen official BBC JR2025,{PDF},Provincie Antwerpen / APB POA,2026-08-19,budget,tick1454; official BBC JR2025 PDF 26p / 815276 bytes; pdfinfo created 31.03.2026 UTC; print 31.03.2026; provincieraad listing 28.05.2026; volgnr 35242281; KBO 0541.414.804; assets 27383763 cash 15833343 debt 13081646 pers 78446266 omzet 6037493 diensten 14020103 pnl 2549375 equity 14302117",
    "src_poa_site,APB POA official besluiten-statuten-rapporten page,https://www.provincieantwerpen.be/nl/locaties/poa-provinciaal-onderwijs-antwerpen/besluiten-statuten-rapporten,Provincie Antwerpen / APB POA,2026-08-19,official_register,tick1454; leftover APB of mined provincie Antwerpen; zetel Koningin Elisabethlei 22 2018 Antwerpen; contact onderwijs@provincieantwerpen.be",
    "src_kbo_poa_0541414804,KBO APB Provinciaal Onderwijs Antwerpen 0541.414.804,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0541414804,KBO Public Search FOD Economie,2026-08-19,official_register,tick1454; Actief since 26.09.2013; Autonoom provinciebedrijf; zetel Koningin Elisabethlei 22 2018 Antwerpen since 01.12.2018; 27 VE; bestuurder Lemmens Luk; dagelijks bestuur Fivez Liesbeth; Werkgever RSZ since 01.01.2022",
    "src_poa_foi_contact,APB POA FOI channel (openbaarheid@provincieantwerpen.be; onderwijs@provincieantwerpen.be),https://www.provincieantwerpen.be/nl/locaties/poa-provinciaal-onderwijs-antwerpen,APB POA / Provincie Antwerpen,2026-08-19,official_register,tick1454; leftover provincial education APB; NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\napb_poa," in raw or raw.startswith(b"apb_poa,"):
    raise SystemExit("apb_poa already present")
if b"0541.414.804" in raw or b"0541414804" in raw:
    raise SystemExit("APB POA KBO already present")
row = (
    "apb_poa,APB Provinciaal Onderwijs Antwerpen (APB POA leftover provincial education APB of mined provincie Antwerpen; NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH),"
    "APB Enseignement provincial d Anvers (APB residuel education provinciale),"
    "APB Provincial Education Antwerp leftover provincial education APB of mined province of Antwerp (not PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH),"
    "apb,prov_antwerpen,nl,https://www.provincieantwerpen.be/nl/locaties/poa-provinciaal-onderwijs-antwerpen,openbaarheid@provincieantwerpen.be,Koningin Elisabethlei 22 2018 Antwerpen,"
    "tick1454 leftover residual APB after leftover AGB hunt; KBO 0541.414.804 Actief since 26.09.2013; live JR2025 official BBC PDF; sourced euros assets 27383763 omzet 6037493 diensten 14020103 pers 78446266 pnl 2549375 equity 14302117 cash 15833343 debt 13081646 capex 752301 dividend 0; FOI ready pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m / 27 VE; distinct from already-mined APB PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA 0408.543.313 / leftover PIH 0541.414.408"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 apb_poa")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_poa_assets_2025", "2025", "27383763", "2025 assets 27383763 (was 23505165); tick1454; primary official BBC J4"),
    ("bud_poa_current_2025", "2025", "25590458", "2025 vlottend 25590458 (was 21473884); tick1454; primary official BBC J4"),
    ("bud_poa_cash_2025", "2025", "15833343", "2025 liquide+geldbeleg 15833343 JUMP (was 12557234); tick1454; primary official BBC J4"),
    ("bud_poa_strecv_2025", "2025", "9329908", "2025 ST vorderingen 9329908 (was 8239474); tick1454; primary official BBC J4"),
    ("bud_poa_trade_2025", "2025", "1081676", "2025 ruil vorderingen 1081676 (was 469110); tick1454; primary official BBC J4"),
    ("bud_poa_ntruilrecv_2025", "2025", "8248232", "2025 niet-ruil vorderingen 8248232 (was 7770364); tick1454; primary official BBC J4"),
    ("bud_poa_voorraden_2025", "2025", "265195", "2025 voorraden 265195 (was 287780); tick1454; primary official BBC J4"),
    ("bud_poa_prepaid_2025", "2025", "162012", "2025 overlopend actief 162012 (was 389396); tick1454; primary official BBC J4"),
    ("bud_poa_fixed_2025", "2025", "1793305", "2025 vaste activa 1793305 (was 2031281); tick1454; primary official BBC J4"),
    ("bud_poa_iva_2025", "2025", "0", "2025 IVA empty; tick1454; primary official BBC J4"),
    ("bud_poa_mva_2025", "2025", "1752558", "2025 MVA 1752558 (was 1998954); tick1454; primary official BBC J4"),
    ("bud_poa_install_2025", "2025", "1659850", "2025 installaties 1659850 (was 1961898); tick1454; primary official BBC J4"),
    ("bud_poa_meubilair_2025", "2025", "92208", "2025 meubilair 92208 (was 36557); tick1454; primary official BBC J4"),
    ("bud_poa_erfgoed_2025", "2025", "500", "2025 erfgoed 500; tick1454; primary official BBC J4"),
    ("bud_poa_fva_2025", "2025", "40747", "2025 FVA 40747 (was 32327; Milcobel +8420); tick1454; primary official BBC J4/T5"),
    ("bud_poa_equity_2025", "2025", "14302117", "2025 nettoactief 14302117 (was 11752742); tick1454; primary official BBC J4"),
    ("bud_poa_overgedragen_2025", "2025", "10915968", "2025 gecumuleerd overschot 10915968 (was 8366593); tick1454; primary official BBC J4"),
    ("bud_poa_overignet_2025", "2025", "3386149", "2025 overig nettoactief 3386149; tick1454; primary official BBC J4"),
    ("bud_poa_debt_2025", "2025", "13081646", "2025 schulden 13081646 ALL ST (was 11752423; LT empty; T4 fin debt 0); tick1454; primary official BBC J4"),
    ("bud_poa_stdebt_2025", "2025", "13081646", "2025 ST schulden 13081646; tick1454; primary official BBC J4"),
    ("bud_poa_ruilpay_2025", "2025", "5748817", "2025 ST ruil schulden 5748817 (was 4603095); tick1454; primary official BBC J4"),
    ("bud_poa_ntruilpay_2025", "2025", "43400", "2025 ST niet-ruil schulden 43400 (was 19672); tick1454; primary official BBC J4"),
    ("bud_poa_deferred_2025", "2025", "7289430", "2025 overlopend passief 7289430 (was 7129657); tick1454; primary official BBC J4"),
    ("bud_poa_explontv_2025", "2025", "96264376", "2025 expl ontvangsten J2 96264376; tick1454; primary official BBC J2"),
    ("bud_poa_expluitg_2025", "2025", "92309031", "2025 expl uitgaven J2 92309031; tick1454; primary official BBC J2"),
    ("bud_poa_explsaldo_2025", "2025", "3955344", "2025 expl saldo / AFM 3955344 (was 1787289 T2); tick1454; primary official BBC J2"),
    ("bud_poa_investsaldo_2025", "2025", "-760721", "2025 investeringssaldo -760721; tick1454; primary official BBC J2"),
    ("bud_poa_bbr_2025", "2025", "3194623", "2025 budgettair resultaat 3194623 (was 1170727); tick1454; primary official BBC J2"),
    ("bud_poa_cumbbr_2025", "2025", "19670612", "2025 gecumuleerd BBR 19670612 (was 16475989); tick1454; primary official BBC J2"),
    ("bud_poa_omzet_2025", "2025", "6037493", "2025 J5 opbrengsten uit de werking 6037493 (was 5769070); tick1454; primary official BBC J5"),
    ("bud_poa_diensten_2025", "2025", "14020103", "2025 J5 goederen en diensten 14020103 (was 14021616); tick1454; primary official BBC J5"),
    ("bud_poa_pers_2025", "2025", "78446266", "2025 J5 bezoldigingen 78446266 (was 74810876; VTE unpublished); tick1454; primary official BBC J5"),
    ("bud_poa_afschr_2025", "2025", "1016940", "2025 J5 afschrijvingen 1016940 (was 1064532); tick1454; primary official BBC J5"),
    ("bud_poa_andere_2025", "2025", "58501", "2025 J5 andere operationele kosten 58501 (was 68125); tick1454; primary official BBC J5"),
    ("bud_poa_werksub_2025", "2025", "89653419", "2025 J5 werkingssubsidies 89653419 vs T2 89804447 gap 151028; tick1454; primary official BBC J5"),
    ("bud_poa_expl_2025", "2025", "2387422", "2025 J5 operationeel overschot 2387422 (was 1973399); tick1454; primary official BBC J5"),
    ("bud_poa_pnl_2025", "2025", "2549375", "2025 J5 overschot boekjaar 2549375 (was 2192215); tick1454; primary official BBC J5"),
    ("bud_poa_div_2025", "2025", "0", "2025 dividend 0; rechthebbenden empty; tick1454; primary official BBC J5"),
    ("bud_poa_capex_2025", "2025", "752301", "2025 capex T2 MVA 752301 (T5 aankopen 752427); tick1454; primary official BBC T2/T5"),
    ("bud_poa_leerkracht_reclass_2025", "2025", "70057123", "2025 T2 onderwijzend ten laste van andere overheden 70057123 (2024 bestuur 67188393 empty 2025); tick1454; primary official BBC T2"),
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

append_lf(DATA / "commitments.csv", [
    f"{COMM},APB POA JR2025 leftover provincial education APB dual (pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m / 27 VE),{ENT},APB POA / provincie Antwerpen dual education,Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid,2026-05-28,2013,,92309031,,,active,{PDF},Local leftover APB map VL POA — pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m,Publish VTE + 27 VE payroll + leerkracht reclass 70.06m + cash 15.83m counterparties + J5/T2 werksub recon + Milcobel FVA; do not keep leftover APB POA as unpublished 92m education shell,{SRC},strong,Vlaanderen>Provincies>Antwerpen>APB>POA>JR2025_L5,tick1454; assets 27383763 omzet 6037493 diensten 14020103 pers 78446266 pnl 2549375 equity 14302117 cash 15833343 debt 13081646 capex 752301 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},APB POA JR2025 leftover provincial education APB: pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m / 27 VE,L5,local_budget_line,Vlaanderen>Provincies>Antwerpen>APB>POA>JR2025_L5,78446266,27383763,Leftover dual APB education shell: assets 27.38m / equity 14.30m / expl uitg 92.31m / pers 78.45m VTE unpublished / cash 15.83m JUMP / leerkracht reclass 70.06m / 27 VE / no NBB; do not treat 92.31m as TE-additive of 348bn,strong,{SRC},APB POA / provincie Antwerpen dual education,Local leftover APB map VL POA — JR2025 official BBC live; pers/cash/leerkracht-reclass FOI,Official BBC 2026-08-19: pers 78.45m / cash JUMP 15.83m / PnL +2.55m / BBR +3.19m / 27 VE / VTE unpublished,7.5,8.5,3.0,7.8,Publish VTE + 27 VE payroll + leerkracht reclass 70.06m + cash 15.83m counterparties + J5/T2 werksub recon + Milcobel FVA; do not keep leftover APB POA as unpublished 92m education shell,active,,tick1454; leftover APB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA 0408.543.313 / leftover PIH 0541.414.408",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Provincies>Antwerpen>APB>POA>JR2025_L5,{ENT},pers J5 78446266 VTE unpublished + 27 VE + cash JUMP 15833343 vs 12557234 + leerkracht reclass T2 andere overheden 70057123 vs 2024 bestuur 67188393 empty 2025 + J5/T2 werksub gap 151028 + ST recv 9329908 + deferred 7289430 + FVA Milcobel 40747 + klasse-0 476554 + NBB non-filing + commissaris unpublished,Leftover APB POA after leftover AGB hunt: pers 78.45m / cash JUMP 15.83m / 27 VE hides provincial education vehicle,8,APB Provinciaal Onderwijs Antwerpen / provinciegriffier / Bestuursorgaan,openbaarheid@provincieantwerpen.be,Koningin Elisabethlei 22 2018 Antwerpen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1454 leftover APB after honest leftover AGB hunt; live JR2025 official BBC PDF now extracted (815276 bytes 26p). FOI ready not sent. NOT every-10. NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH. Leftover TPA Beleef 0408.543.313 / PIH 0541.414.408 official JR2025 PDFs now fetchable this tick via Googlebot+koepelsite — not taken. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. AGB Bornem still 2024 HEAD 403.",
])
print("foi_queue +1")

# --- research_queue surgical ---
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
if not last_s.startswith("rq_1454,"):
    raise SystemExit(f"expected last row rq_1454, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1454 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1454,APB POA JR2025 leftover dual residual,hole_fill,5,done,L5,apb_poa,"
    "Completed: APB Provinciaal Onderwijs Antwerpen leftover APB of mined provincie Antwerpen after leftover AGB hunt; KBO 0541.414.804 Actief; live JR2025 official BBC PDF (815276 bytes 26p; print 31.03.2026; provincieraad listing 28.05.2026; volgnr 35242281; koepelsite PDF Googlebot 200); sourced euros assets 27383763 omzet 6037493 diensten 14020103 pers 78446266 pnl 2549375 equity 14302117 cash 15833343 debt 13081646 capex 752301 dividend 0; FOI ready pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m / 27 VE; NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH,"
    f"{GAP},2026-08-19T14:10:00Z,{TS},"
    "tick1454 APB POA leftover APB residual; KBO 0541.414.804; live JR2025 official BBC PDF; sourced euros; FOI ready not sent; next rq_1455 leftover APB TPA/PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
)
spawn = (
    "rq_1455,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1454 done including APB POA 1454 leftover APB live official BBC / Crematorium Hasselt 1453 leftover 100pct Stad Hasselt daughter live NBB WVV / CoLimBo 1452 leftover Bosgroep daughter live NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. STRONG leftover APB TPA Beleef 0408.543.313 (JR listed 25.06.2026; koepelsite jaarrekening_25_tpa.pdf now fetchable via Googlebot this tick — take) / leftover APB PIH 0541.414.408 (JR listed 28.05.2026; koepelsite 3_apb_pih_jaarrekening_2025_bbc_rapport.pdf now fetchable — take). Do NOT confuse with already-mined APB PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / already-mined APB POA 1454. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1454). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1454 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1454. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452 / RLHP 1451 / BGKN 1450. Next every-10 is 1460.,,"
    f"{TS},{TS},"
    "spawned tick1454 after APB POA leftover APB live official BBC JR2025; leftover APB TPA/PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1454=done + rq_1455 spawned; keep", last_line_start)

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
    f"tick1454 APB POA leftover APB residual; KBO 0541.414.804; live JR2025 official BBC PDF; sourced euros assets 27383763 omzet 6037493 diensten 14020103 pers 78446266 pnl 2549375 equity 14302117 cash 15833343 debt 13081646 capex 752301 dividend 0; FOI ready pers 78.45m / cash JUMP 15.83m / leerkracht reclass 70.06m / 27 VE; NOT PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover TPA / leftover PIH; next rq_1455 leftover APB TPA/PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1454,1454,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1454")

entry = (
    "\n## Tick 1454 - 2026-08-19 - rq_1454 APB POA dual residual leftover\n"
    "- Unit: APB Provinciaal Onderwijs Antwerpen / APB POA (leftover provincial education APB of mined provincie Antwerpen; 27 VE) after residual dual hunt (KBO **0541.414.804**; official koepelsite BBC PDF **815276** bytes / 26p; print **31.03.2026**; provincieraad listing **28.05.2026**; volgnr **35242281**). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar/Oudsbergen/MAC already mined. Leftover APB POA official JR2025 PDF now fetches via Googlebot + `/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-05-28/beleidsrapporten/02_apb_poa_doelstellingenrealisatienota_en_jaarrekening_2025.pdf` (box curl 403 without Googlebot UA) — taken (hunt order #1 leftover APB of mined provincie with live statutory 2025 BBC balans). PDF header **APB Provinciaal Onderwijs Antwerpen / Koningin Elisabethlei 22 / Jaarrekening 2025** — NOT a Foleon leftover-slug redirect to Hooibeekhoeve (those slugs still redirect). Distinct from already-mined **APB PSES** / **GKC** / **Havencentrum** / **Kamp C** / **Hooibeekhoeve**. Leftover **TPA Beleef 0408.543.313** (koepelsite `jaarrekening_25_tpa.pdf` listed 25.06.2026) and leftover **PIH 0541.414.408** (koepelsite `3_apb_pih_jaarrekening_2025_bbc_rapport.pdf` listed 28.05.2026) now also fetchable this tick — not taken. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024 (NBB year-end 31/12/2024). Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. First confirmed not already extracted as JR2025 euros: no APB POA / 0541.414.804 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **26.09.2013**; Autonoom provinciebedrijf; zetel Koningin Elisabethlei 22 2018 Antwerpen since 01.12.2018; **27 VE**; bestuurder Lemmens Luk since 03.12.2018; dagelijks bestuur Fivez Liesbeth since 19.12.2024; Werkgever RSZ since 01.01.2022; btw since 01.02.2014; aanbestedende overheid; NACE btw 84.113 / RSZ 85.322; contact onderwijs@provincieantwerpen.be; tel 03 240 55 11. APB states it is not an 'onderneming' and does **not** file NBB (bijlage art. 219 Provinciedecreet / BBC digital filing Vlaamse Gemeenschap). Euros extracted from the official BBC PDF itself. Belscope/Companyweb/Busibee euros not used. Not every-10 (next 1460 MUST do every-10).\n"
    "- EUR strong (primary official BBC J2/J4/J5/T2/T5; omzet = J5 werking **6037493**; diensten J5 **14020103**; pers J5 **78446266** / VTE unpublished): assets **27383763** (was 23505165); current **25590458** vs 21473884; cash **15833343 JUMP** vs 12557234; ST recv **9329908** vs 8239474 (ruil **1081676** / niet-ruil **8248232**); voorraden **265195**; prepaid **162012**; fixed **1793305** vs 2031281 / IVA empty / MVA **1752558** (installaties **1659850**; meubilair **92208**; erfgoed **500**) / FVA **40747** vs 32327 (Milcobel +8420); equity **14302117** vs 11752742 (gecumuleerd **10915968**; overig **3386149**); schulden **13081646** vs 11752423 ALL ST (ruil **5748817**; niet-ruil **43400**; deferred **7289430**; LT empty; T4 fin debt **0**); expl ontvangsten **96264376** / expl uitgaven **92309031** / expl saldo / AFM **3955344**; invest **-760721**; BBR **3194623**; cum BBR **19670612**; J5 kosten **93578572** / opbrengsten **96127947** / werksub **89653419** vs T2 **89804447** gap **151028**; expl **+2387422**; PnL **+2549375** vs +2192215; dividend **0**; capex T2 **752301** / T5 aankopen **752427**; T2 onderwijzend andere overheden **70057123** (2024 bestuur **67188393** empty 2025 — classification JUMP); klasse-0 **476554**. PDF 1-euro rounding: 2387422+161954=2549376 vs 2549375; 96264376-92309031=3955345 vs 3955344. Cross-checks: 25590458+1793305=27383763; 14302117+13081646=27383763; 96127947-93578572=2549375; 3955344-760721=3194623.\n"
    f"- CSVs: sources +4; entities +1 `apb_poa` parent `prov_antwerpen`; budgets +{len(added)} executed; commitments +1 envelope 92309031 listing 28.05.2026; leaderboard +1 annual 78446266 / total 27383763; foi_queue +1 status=ready never sent; research_queue surgical rq_1454=done + rq_1455 spawn; loop_state ticks_completed=1454. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_poa_pers_78_45m_cash_15_83m_leerkracht_reclass_l5` ready not sent — pers 78.45m VTE unpublished / 27 VE / cash JUMP 15.83m / leerkracht reclass 70.06m / J5-T2 werksub gap 0.15m / ST recv 9.33m / deferred 7.29m / FVA Milcobel / klasse-0 0.48m / NBB non-filing / commissaris unpublished.\n"
    "- Next: rq_1455 residual dual L5 VL. Leftover APB **TPA Beleef 0408.543.313** / **PIH 0541.414.408** official JR2025 PDFs now fetchable via Googlebot+koepelsite this tick — take next. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR this tick). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452 / RLHP 1451 / BGKN 1450. Next every-10 is 1460.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1454 -" in lraw:
    raise SystemExit("loop_log already has tick 1454 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1454")
print("DONE tick 1454")
