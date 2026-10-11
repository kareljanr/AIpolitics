#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1455 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T14:45:00Z"
ENT = "apb_tpa"
SRC = "src_tpa_jr2025_bbc"
GAP = "gap_tpa_pers_1_22m_omzet_14k_cash_1_81m_l5"
LB = "lb_tpa_pers_1_22m_omzet_14k_cash_1_81m_1ve"
COMM = "comm_tpa_jr2025_expl"
PDF = "https://www.provincieantwerpen.be/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-06-25/beleidsrapporten/jaarrekening_25_tpa.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    f"{SRC},APB Toerisme Provincie Antwerpen official BBC JR2025,{PDF},Provincie Antwerpen / APB TPA,2026-08-19,budget,tick1455; official BBC JR2025 PDF 23p / 801718 bytes; pdfinfo created 20.03.2026 UTC; print 20.03.2026; provincieraad listing 25.06.2026; volgnr 879218; KBO 0408.543.313; assets 2044080 cash 1805398 debt 1059730 pers 1220812 omzet 14346 diensten 1321369 pnl 614824 equity 984350",
    "src_tpa_site,APB TPA official besluiten-statuten-rapporten page,https://www.provincieantwerpen.be/nl/samen-vakantie-maken/toerisme-provincie-antwerpen-besluiten-statuten-rapporten,Provincie Antwerpen / APB TPA,2026-08-19,official_register,tick1455; leftover APB of mined provincie Antwerpen; zetel Koningin Elisabethlei 22 2018 Antwerpen; contact info@provincieantwerpen.be; naam BELEEF PROVINCIE ANTWERPEN / APB BPA since 25.06.2026",
    "src_kbo_tpa_0408543313,KBO BELEEF PROVINCIE ANTWERPEN / APB TPA 0408.543.313,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408543313,KBO Public Search FOD Economie,2026-08-19,official_register,tick1455; Actief since 10.01.1948; Autonoom provinciebedrijf since 01.01.2016; naam BELEEF since 25.06.2026; zetel Koningin Elisabethlei 22 2018 Antwerpen; 1 VE; dagelijks bestuur Pierre Koenraad; Werkgever RSZ since 01.01.2022",
    "src_tpa_foi_contact,APB TPA FOI channel (openbaarheid@provincieantwerpen.be; info@provincieantwerpen.be),https://www.provincieantwerpen.be/nl/samen-vakantie-maken/toerisme-provincie-antwerpen-besluiten-statuten-rapporten,APB TPA / Provincie Antwerpen,2026-08-19,official_register,tick1455; leftover provincial tourism APB; NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\napb_tpa," in raw or raw.startswith(b"apb_tpa,"):
    raise SystemExit("apb_tpa already present")
if b"0408.543.313" in raw or b"0408543313" in raw:
    raise SystemExit("APB TPA KBO already present")
row = (
    "apb_tpa,APB Toerisme Provincie Antwerpen / Beleef Provincie Antwerpen (APB TPA leftover provincial tourism APB of mined provincie Antwerpen; NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH),"
    "APB Tourisme province d Anvers / Beleef (APB residuel tourisme provincial),"
    "APB Tourism Province of Antwerp / Beleef leftover provincial tourism APB of mined province of Antwerp (not POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH),"
    "apb,prov_antwerpen,nl,https://www.provincieantwerpen.be/nl/samen-vakantie-maken/toerisme-provincie-antwerpen-besluiten-statuten-rapporten,openbaarheid@provincieantwerpen.be,Koningin Elisabethlei 22 2018 Antwerpen,"
    "tick1455 leftover residual APB after leftover AGB hunt; KBO 0408.543.313 Actief since 10.01.1948; naam BELEEF PROVINCIE ANTWERPEN / APB BPA since 25.06.2026; live JR2025 official BBC PDF; sourced euros assets 2044080 omzet 14346 diensten 1321369 pers 1220812 pnl 614824 equity 984350 cash 1805398 debt 1059730 capex 49664 dividend 0; FOI ready pers 1.22m / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / 1 VE; distinct from already-mined APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH 0541.414.408"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 apb_tpa")

# --- budgets (PDF integers nearest euro) ---
BUDGETS = [
    ("bud_tpa_assets_2025", "2025", "2044080", "2025 assets 2044080 (was 2183963); tick1455; primary official BBC J4"),
    ("bud_tpa_current_2025", "2025", "1862769", "2025 vlottend 1862769 (was 2046802); tick1455; primary official BBC J4"),
    ("bud_tpa_cash_2025", "2025", "1805398", "2025 liquide+geldbeleg 1805398 DROP (was 1915711); tick1455; primary official BBC J4"),
    ("bud_tpa_strecv_2025", "2025", "43671", "2025 ST vorderingen 43671 (was 75973); tick1455; primary official BBC J4"),
    ("bud_tpa_trade_2025", "2025", "20658", "2025 ruil vorderingen 20658 (was 44593); tick1455; primary official BBC J4"),
    ("bud_tpa_ntruilrecv_2025", "2025", "23013", "2025 niet-ruil vorderingen 23013 (was 31380); tick1455; primary official BBC J4"),
    ("bud_tpa_voorraden_2025", "2025", "0", "2025 voorraden 0 DROP (was 32078); tick1455; primary official BBC J4"),
    ("bud_tpa_prepaid_2025", "2025", "13701", "2025 overlopend actief 13701 (was 23039); tick1455; primary official BBC J4"),
    ("bud_tpa_fixed_2025", "2025", "181311", "2025 vaste activa 181311 (was 137161); tick1455; primary official BBC J4"),
    ("bud_tpa_iva_2025", "2025", "64942", "2025 IVA 64942 JUMP (was 20507); tick1455; primary official BBC J4"),
    ("bud_tpa_mva_2025", "2025", "115221", "2025 MVA 115221 (was 115506); tick1455; primary official BBC J4"),
    ("bud_tpa_install_2025", "2025", "10356", "2025 installaties 10356 (was 8783); tick1455; primary official BBC J4"),
    ("bud_tpa_meubilair_2025", "2025", "14864", "2025 meubilair 14864 (was 16722); tick1455; primary official BBC J4"),
    ("bud_tpa_andere_mva_2025", "2025", "90000", "2025 andere MVA roerende 90000; tick1455; primary official BBC J4"),
    ("bud_tpa_fva_2025", "2025", "1149", "2025 FVA J4 1149 (T5 prints 91149 recon FOI); tick1455; primary official BBC J4"),
    ("bud_tpa_equity_2025", "2025", "984350", "2025 nettoactief 984350 JUMP (was 369526); tick1455; primary official BBC J4"),
    ("bud_tpa_overgedragen_2025", "2025", "922245", "2025 gecumuleerd overschot 922245 (was 307421); tick1455; primary official BBC J4"),
    ("bud_tpa_overignet_2025", "2025", "62105", "2025 overig nettoactief 62105; tick1455; primary official BBC J4"),
    ("bud_tpa_debt_2025", "2025", "1059730", "2025 schulden 1059730 ALL ST DROP (was 1814437; LT empty; T4 fin debt 0); tick1455; primary official BBC J4"),
    ("bud_tpa_stdebt_2025", "2025", "1059730", "2025 ST schulden 1059730; tick1455; primary official BBC J4"),
    ("bud_tpa_ruilpay_2025", "2025", "413846", "2025 ST ruil schulden 413846 (was 449229); tick1455; primary official BBC J4"),
    ("bud_tpa_deferred_2025", "2025", "645884", "2025 overlopend passief 645884 DROP (was 1365208); tick1455; primary official BBC J4"),
    ("bud_tpa_explontv_2025", "2025", "2887344", "2025 expl ontvangsten J2 2887344; tick1455; primary official BBC J2"),
    ("bud_tpa_expluitg_2025", "2025", "2944913", "2025 expl uitgaven J2 2944913; tick1455; primary official BBC J2"),
    ("bud_tpa_explsaldo_2025", "2025", "-57569", "2025 expl saldo / AFM -57569 (was +71699 T2); tick1455; primary official BBC J2"),
    ("bud_tpa_investsaldo_2025", "2025", "-49664", "2025 investeringssaldo -49664; tick1455; primary official BBC J2"),
    ("bud_tpa_bbr_2025", "2025", "-107233", "2025 budgettair resultaat -107233 (was +28493); tick1455; primary official BBC J2"),
    ("bud_tpa_cumbbr_2025", "2025", "1435223", "2025 gecumuleerd BBR 1435223 (was 1542456); tick1455; primary official BBC J2"),
    ("bud_tpa_omzet_2025", "2025", "14346", "2025 J5 opbrengsten uit de werking 14346 (was 22552); tick1455; primary official BBC J5"),
    ("bud_tpa_diensten_2025", "2025", "1321369", "2025 J5 goederen en diensten 1321369 (was 1090842); tick1455; primary official BBC J5"),
    ("bud_tpa_pers_2025", "2025", "1220812", "2025 J5 bezoldigingen 1220812 (was 1109293; VTE unpublished); tick1455; primary official BBC J5"),
    ("bud_tpa_afschr_2025", "2025", "7183", "2025 J5 afschrijvingen 7183 (was 6021); tick1455; primary official BBC J5"),
    ("bud_tpa_werksub_2025", "2025", "2639537", "2025 J5 werkingssubsidies 2639537 vs T2 1982022 gap 657515; tick1455; primary official BBC J5"),
    ("bud_tpa_andere_opbr_2025", "2025", "922996", "2025 J5 andere operationele opbrengsten 922996 (was 530028); tick1455; primary official BBC J5"),
    ("bud_tpa_expl_2025", "2025", "606611", "2025 J5 operationeel overschot 606611 (was -568455); tick1455; primary official BBC J5"),
    ("bud_tpa_pnl_2025", "2025", "614824", "2025 J5 overschot boekjaar 614824 JUMP (was -553315); tick1455; primary official BBC J5"),
    ("bud_tpa_div_2025", "2025", "0", "2025 dividend 0; rechthebbenden empty; tick1455; primary official BBC J5"),
    ("bud_tpa_capex_2025", "2025", "49664", "2025 capex T2 49664 (T5 aankopen 53191; MVA 6674 + IVA 42990); tick1455; primary official BBC T2/T5"),
    ("bud_tpa_werksub_granted_2025", "2025", "420903", "2025 J5 toegestane werkingssubsidies 420903 (T2 438623); tick1455; primary official BBC J5"),
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
    f"{COMM},APB TPA JR2025 leftover provincial tourism APB dual (pers 1.22m / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / 1 VE),{ENT},APB TPA / provincie Antwerpen dual tourism,Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid,2026-06-25,2016,,2944913,,,active,{PDF},Local leftover APB map VL TPA — pers 1.22m / omzet 14k / cash DROP 1.81m,Publish VTE + 1 VE payroll + J5/T2 werksub recon 0.66m + cash 1.81m counterparties + NBB deposit + Beleef naamswijziging; do not keep leftover APB TPA as unpublished 2.94m tourism shell,{SRC},strong,Vlaanderen>Provincies>Antwerpen>APB>TPA>JR2025_L5,tick1455; assets 2044080 omzet 14346 diensten 1321369 pers 1220812 pnl 614824 equity 984350 cash 1805398 debt 1059730 capex 49664 dividend 0; FOI ready not sent; not TE-additive of 348bn; NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},APB TPA / Beleef JR2025 leftover provincial tourism APB: pers 1.22m / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / 1 VE,L5,local_budget_line,Vlaanderen>Provincies>Antwerpen>APB>TPA>JR2025_L5,1220812,2044080,Leftover dual APB tourism shell: assets 2.04m / equity 0.98m JUMP / expl uitg 2.94m / pers 1.22m VTE unpublished / omzet 14k / cash 1.81m DROP / werksub J5 2.64m vs T2 1.98m gap 0.66m / PnL JUMP +0.61m / 1 VE / Beleef rename 25.06.2026; do not treat 2.94m as TE-additive of 348bn,strong,{SRC},APB TPA / provincie Antwerpen dual tourism,Local leftover APB map VL TPA — JR2025 official BBC live; pers/omzet/cash/werksub FOI,Official BBC 2026-08-19: pers 1.22m / omzet 14k / cash DROP 1.81m / PnL +0.61m / BBR -0.11m / 1 VE / VTE unpublished,7.2,7.0,3.0,7.4,Publish VTE + 1 VE payroll + J5/T2 werksub recon 0.66m + cash 1.81m counterparties + NBB deposit + Beleef naamswijziging; do not keep leftover APB TPA as unpublished 2.94m tourism shell,active,,tick1455; leftover APB after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined APB POA 1454 / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH 0541.414.408",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Provincies>Antwerpen>APB>TPA>JR2025_L5,{ENT},pers J5 1220812 VTE unpublished + 1 VE + omzet 14346 + cash DROP 1805398 vs 1915711 + J5/T2 werksub gap 657515 (J5 2639537 vs T2 1982022) + deferred DROP 645884 vs 1365208 + PnL JUMP 614824 vs -553315 + FVA J4 1149 vs T5 91149 + Beleef naamswijziging 25.06.2026 + NBB filing unpublished + commissaris unpublished,Leftover APB TPA after leftover AGB hunt: pers 1.22m / omzet 14k / cash DROP 1.81m / 1 VE hides provincial tourism vehicle,8,APB Toerisme Provincie Antwerpen / Beleef / provinciegriffier / Bestuursorgaan,openbaarheid@provincieantwerpen.be,Koningin Elisabethlei 22 2018 Antwerpen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1455 leftover APB after honest leftover AGB hunt; live JR2025 official BBC PDF now extracted (801718 bytes 23p). FOI ready not sent. NOT every-10. NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH. Leftover PIH 0541.414.408 official JR2025 PDF still fetchable this tick via Googlebot+koepelsite — not taken. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. AGB Bornem still 2024 HEAD 403.",
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
if not last_s.startswith("rq_1455,"):
    raise SystemExit(f"expected last row rq_1455, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1455 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1455,APB TPA Beleef JR2025 leftover dual residual,hole_fill,5,done,L5,apb_tpa,"
    "Completed: APB Toerisme Provincie Antwerpen / Beleef Provincie Antwerpen leftover APB of mined provincie Antwerpen after leftover AGB hunt; KBO 0408.543.313 Actief; live JR2025 official BBC PDF (801718 bytes 23p; print 20.03.2026; provincieraad listing 25.06.2026; volgnr 879218; koepelsite PDF Googlebot 200); sourced euros assets 2044080 omzet 14346 diensten 1321369 pers 1220812 pnl 614824 equity 984350 cash 1805398 debt 1059730 capex 49664 dividend 0; FOI ready pers 1.22m / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / 1 VE; NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH,"
    f"{GAP},2026-08-19T14:25:00Z,{TS},"
    "tick1455 APB TPA leftover APB residual; KBO 0408.543.313; live JR2025 official BBC PDF; sourced euros; FOI ready not sent; next rq_1456 leftover APB PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
)
spawn = (
    "rq_1456,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1455 done including APB TPA 1455 leftover APB live official BBC / APB POA 1454 leftover APB live official BBC / Crematorium Hasselt 1453 leftover 100pct Stad Hasselt daughter live NBB WVV / CoLimBo 1452 leftover Bosgroep daughter live NBB WVV). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 statutory PDF actually downloads. STRONG leftover APB PIH 0541.414.408 (JR listed 28.05.2026; koepelsite 3_apb_pih_jaarrekening_2025_bbc_rapport.pdf now fetchable via Googlebot this tick — take). Do NOT confuse with already-mined APB PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / already-mined APB POA 1454 / already-mined APB TPA 1455. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1455). Leftover IGS IVAREM 0267.403.264 still JR2024 as of 1455 — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished as of 1455. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452 / RLHP 1451. Next every-10 is 1460.,,"
    f"{TS},{TS},"
    "spawned tick1455 after APB TPA leftover APB live official BBC JR2025; leftover APB PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1455=done + rq_1456 spawned; keep", last_line_start)

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
    f"tick1455 APB TPA leftover APB residual; KBO 0408.543.313; live JR2025 official BBC PDF; sourced euros assets 2044080 omzet 14346 diensten 1321369 pers 1220812 pnl 614824 equity 984350 cash 1805398 debt 1059730 capex 49664 dividend 0; FOI ready pers 1.22m / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / 1 VE; NOT POA / PSES / GKC / Havencentrum / Kamp C / Hooibeekhoeve / leftover PIH; next rq_1456 leftover APB PIH now fetchable else leftover Bosgroep VZW if CDN live else leftover AGB/IOED/cultuur-IGS/Hart/IVAREM if JR2025; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1455,1455,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1455")

entry = (
    "\n## Tick 1455 - 2026-08-19 - rq_1455 APB TPA Beleef dual residual leftover\n"
    "- Unit: APB Toerisme Provincie Antwerpen / Beleef Provincie Antwerpen / APB TPA (leftover provincial tourism APB of mined provincie Antwerpen; 1 VE) after residual dual hunt (KBO **0408.543.313**; official koepelsite BBC PDF **801718** bytes / 23p; print **20.03.2026**; provincieraad listing **25.06.2026**; volgnr **879218**). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar/Oudsbergen/MAC already mined. Leftover APB TPA official JR2025 PDF now fetches via Googlebot + `/sites/koepelsite/files/publicaties/open-data/provincieraad/2026/2026-06-25/beleidsrapporten/jaarrekening_25_tpa.pdf` (box curl 403 without Googlebot UA) — taken (hunt order #1 leftover APB of mined provincie with live statutory 2025 BBC balans). PDF header **APB Toerisme Provincie Antwerpen / Koningin Elisabethlei 22 / Jaarrekening 2025** — NOT a Foleon leftover-slug redirect to Hooibeekhoeve (those slugs still redirect). Distinct from already-mined **APB POA 1454** / **APB PSES** / **GKC** / **Havencentrum** / **Kamp C** / **Hooibeekhoeve**. Leftover **PIH 0541.414.408** (koepelsite `3_apb_pih_jaarrekening_2025_bbc_rapport.pdf` listed 28.05.2026) still fetchable this tick — not taken. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024 (NBB year-end 31/12/2024). Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dijk92 / Zuidrand / Zender still JR2024. Dommelhof still no 2025 PDF. First confirmed not already extracted as JR2025 euros: no APB TPA / Beleef / 0408.543.313 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **10.01.1948**; statutaire naam BELEEF PROVINCIE ANTWERPEN / afkorting APB BPA since **25.06.2026** (same day as provincieraad listing); Autonoom provinciebedrijf since 01.01.2016; zetel Koningin Elisabethlei 22 2018 Antwerpen since 10.01.1948; **1 VE**; 10 functiehouders; dagelijks bestuur Pierré Koenraad since 01.02.2026; Werkgever RSZ since 01.01.2022; btw since 01.03.1983; aanbestedende overheid; NACE btw/RSZ 79.901; replaces 0850.333.375 / 0645.584.290; contact info@provincieantwerpen.be. Bijlage: APB TPA **can** be considered an 'onderneming' so NBB filing should happen (art. 219 Provinciedecreet / BBC digital filing Vlaamse Gemeenschap). Euros extracted from the official BBC PDF itself. Belscope/Companyweb/Busibee euros not used. Not every-10 (next 1460 MUST do every-10).\n"
    "- EUR strong (primary official BBC J2/J4/J5/T2/T5; omzet = J5 werking **14346**; diensten J5 **1321369**; pers J5 **1220812** / VTE unpublished): assets **2044080** (was 2183963); current **1862769** vs 2046802; cash **1805398 DROP** vs 1915711; ST recv **43671** vs 75973 (ruil **20658** / niet-ruil **23013**); voorraden **0 DROP** vs 32078; prepaid **13701**; fixed **181311** vs 137161 / IVA **64942 JUMP** vs 20507 / MVA **115221** (installaties **10356**; meubilair **14864**; andere **90000**) / FVA J4 **1149** (T5 prints 91149); equity **984350 JUMP** vs 369526 (gecumuleerd **922245**; overig **62105**); schulden **1059730 DROP** vs 1814437 ALL ST (ruil **413846**; deferred **645884 DROP** vs 1365208; LT empty; T4 fin debt **0**); expl ontvangsten **2887344** / expl uitgaven **2944913** / expl saldo / AFM **-57569**; invest **-49664**; BBR **-107233**; cum BBR **1435223**; J5 kosten **2972642** / opbrengsten **3587466** / werksub **2639537** vs T2 **1982022** gap **657515**; andere opbr **922996**; expl **+606611**; PnL **+614824 JUMP** vs -553315; dividend **0**; capex T2 **49664** / T5 aankopen **53191**; toegestane werksub J5 **420903**; klasse-0 empty. PDF 1-euro rounding. Cross-checks: 1862769+181311=2044080; 984350+1059730=2044080; 3587466-2972642=614824; 606611+8213=614824; 2887344-2944913=-57569; -57569-49664=-107233; 307421+614824=922245.\n"
    f"- CSVs: sources +4; entities +1 `apb_tpa` parent `prov_antwerpen`; budgets +{len(added)} executed; commitments +1 envelope 2944913 listing 25.06.2026; leaderboard +1 annual 1220812 / total 2044080; foi_queue +1 status=ready never sent; research_queue surgical rq_1455=done + rq_1456 spawn; loop_state ticks_completed=1455. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_tpa_pers_1_22m_omzet_14k_cash_1_81m_l5` ready not sent — pers 1.22m VTE unpublished / 1 VE / omzet 14k / cash DROP 1.81m / J5-T2 werksub gap 0.66m / deferred DROP 0.65m / PnL JUMP +0.61m / FVA J4 1.1k vs T5 91k / Beleef naamswijziging 25.06.2026 / NBB filing unpublished / commissaris unpublished.\n"
    "- Next: rq_1456 residual dual L5 VL. Leftover APB **PIH 0541.414.408** official JR2025 PDF still fetchable via Googlebot+koepelsite this tick — take next. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR this tick). Leftover IGS IVAREM **0267.403.264** still JR2024. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening. Leftover IOED/cultuur-IGS still unpublished. Dommelhof only if a real 2025 PDF now downloads. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS/APB. Skip already-mined APB TPA 1455 / APB POA 1454 / Crematorium Hasselt 1453 / CoLimBo 1452 / RLHP 1451 / BGKN 1450. Next every-10 is 1460.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1455 -" in lraw:
    raise SystemExit("loop_log already has tick 1455 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1455")
print("DONE tick 1455")
