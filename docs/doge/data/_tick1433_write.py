#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1433 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:40:00Z"
ENT = "vzw_rlkm"
SRC = "src_rlkm_jr2025_nbb"
GAP = "gap_rlkm_omzet_empty_pers_2_51m_cash_1_80m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlkm_jr2025_nbb,Regionaal Landschap Kempen en Maasland VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00094832.pdf,NBB / RL Kempen en Maasland VZW,2026-08-19,budget,tick1433; VKT-VZW 23.0.8 m04-f PDF 15p / 53190 bytes deposit 2026-00094832; AV 01.04.2026; created 30.04.2026; neerlegging 2026-04-30; KBO 0443.302.272; assets 4741120 cash 1802565 debt 2886066 brutomarge 2443912 pers 2505888 pnl -96043; no commissaris named",
    "src_rlkm_site,Regionaal Landschap Kempen en Maasland official site,https://rlkm.be/,RL Kempen en Maasland VZW,2026-08-19,official_register,tick1433; leftover IGS / regionaal landschap of 11 Kempen-Maasland cities; zetel Winterslagstraat 87 3600 Genk; contact info@rlkm.be; dagelijks bestuur Ignace Schops; IOED channel greetje.vandekerckhove@rlkm.be",
    "src_kbo_rlkm_0443302272,KBO Regionaal Landschap Kempen en Maasland 0443.302.272,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443302272,KBO Public Search FOD Economie,2026-08-19,official_register,tick1433; Actief since 19.06.1990; naam since 19.01.1994; zetel Winterslagstraat 87 3600 Genk since 28.03.2000; 2 VE; VZW; NACE 91.420; Werkgever RSZ since 01.07.1990; btw since 01.01.2016; aanbestedende overheid since 19.06.1990",
    "src_rlkm_foi_contact,RL Kempen en Maasland FOI channel (info@rlkm.be; Winterslagstraat 87 Genk),https://rlkm.be/contact/,RL Kempen en Maasland VZW,2026-08-19,official_register,tick1433; 11 member cities + provincie Limburg; voorzitter Laura Olaerts; ondervoorzitter Rik Brys; IOED 9-city channel of same VZW",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlkm," in raw or raw.startswith(b"vzw_rlkm,"):
    raise SystemExit("vzw_rlkm already present")
if b"0443.302.272" in raw or b"0443302272" in raw:
    raise SystemExit("RL Kempen en Maasland KBO already present")
row = (
    "vzw_rlkm,Regionaal Landschap Kempen en Maasland VZW (leftover IGS / regionaal landschap of 11 mined Kempen-Maasland cities),"
    "Regionaal Landschap Kempen en Maasland ASBL (IGS residuel / paysage regional Campine et Meuse),"
    "Regionaal Landschap Kempen en Maasland leftover IGS / regional landscape VZW of 11 Kempen-Maasland municipalities,"
    "other,sec_flanders,nl,https://rlkm.be/,info@rlkm.be,Winterslagstraat 87 3600 Genk,"
    "tick1433 leftover residual IGS VZW of mined Kempen-Maasland cities after leftover AGB hunt; KBO 0443.302.272 Actief since 19.06.1990; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 4741120 omzet empty diensten empty pers 2505888 pnl -96043 equity 1855054 cash 1802565 debt 2886066 capex 287199 dividend 0; FOI ready empty 70/73/60/61 / pers 2.51m / other recv drop / leveranciers jump; distinct from already-mined RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / AGB Genk / AGBIM"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlkm")

# --- budgets ---
BUDGETS = [
    ("bud_rlkm_assets_2025", "2025", "4741120", "2025 assets 4741120 VKT-VZW 20/58; tick1433; primary official NBB WVV"),
    ("bud_rlkm_assets_2024", "2024", "5208182", "2024 assets 5208182 comparative; tick1433; primary official NBB WVV 20/58"),
    ("bud_rlkm_fixed_2025", "2025", "1195488", "2025 vaste activa 1195488 vs 1091126; tick1433; primary official NBB WVV 21/28"),
    ("bud_rlkm_iva_2025", "2025", "27488", "2025 IVA 27488 vs 43218; tick1433; primary official NBB WVV 21"),
    ("bud_rlkm_mva_2025", "2025", "1167800", "2025 MVA 1167800 vs 1047708; tick1433; primary official NBB WVV 22/27"),
    ("bud_rlkm_gebouwen_2025", "2025", "833852", "2025 terreinen/gebouwen 833852 vs 891501; tick1433; primary official NBB WVV 22"),
    ("bud_rlkm_machines_2025", "2025", "84737", "2025 machines 84737 vs 71395; tick1433; primary official NBB WVV 23"),
    ("bud_rlkm_meubilair_2025", "2025", "26194", "2025 meubilair/rollend 26194 vs 18447; tick1433; primary official NBB WVV 24"),
    ("bud_rlkm_leasing_2025", "2025", "259", "2025 leasing 259 vs 1071; tick1433; primary official NBB WVV 25"),
    ("bud_rlkm_overige_mva_2025", "2025", "4159", "2025 overige MVA 4159 vs 4640; tick1433; primary official NBB WVV 26"),
    ("bud_rlkm_cip_2025", "2025", "218599", "2025 CIP 218599 vs 60654; tick1433; primary official NBB WVV 27"),
    ("bud_rlkm_fva_2025", "2025", "200", "2025 FVA 200 vs 200; tick1433; primary official NBB WVV 28"),
    ("bud_rlkm_current_2025", "2025", "3545632", "2025 vlottend 3545632 vs 4117056; tick1433; primary official NBB WVV 29/58"),
    ("bud_rlkm_voorraden_2025", "2025", "191257", "2025 voorraden 191257 vs 142633; tick1433; primary official NBB WVV 30/36"),
    ("bud_rlkm_strecv_2025", "2025", "1008915", "2025 ST vorderingen 1008915 vs 1986625; tick1433; primary official NBB WVV 40/41"),
    ("bud_rlkm_trade_2025", "2025", "173690", "2025 handelsvorderingen 173690 vs 191327; tick1433; primary official NBB WVV 40"),
    ("bud_rlkm_othrecv_2025", "2025", "835225", "2025 overige vorderingen 835225 DROP vs 1795297; tick1433; primary official NBB WVV 41"),
    ("bud_rlkm_othrecv_2024", "2024", "1795297", "2024 overige vorderingen 1795297 comparative; tick1433; primary official NBB WVV 41"),
    ("bud_rlkm_invest_2025", "2025", "500000", "2025 geldbeleggingen 500000 vs 300000; tick1433; primary official NBB WVV 50/53"),
    ("bud_rlkm_cash_2025", "2025", "1802565", "2025 liquide middelen 1802565 JUMP vs 1639737; tick1433; primary official NBB WVV 54/58"),
    ("bud_rlkm_cash_2024", "2024", "1639737", "2024 liquide middelen 1639737 comparative; tick1433; primary official NBB WVV 54/58"),
    ("bud_rlkm_prepaid_2025", "2025", "42895", "2025 prepaid 42895 vs 48061; tick1433; primary official NBB WVV 490/1"),
    ("bud_rlkm_equity_2025", "2025", "1855054", "2025 EV 1855054 vs 2016806; tick1433; primary official NBB WVV 10/15"),
    ("bud_rlkm_equity_2024", "2024", "2016806", "2024 EV 2016806 comparative; tick1433; primary official NBB WVV 10/15"),
    ("bud_rlkm_bestemde_2025", "2025", "1038694", "2025 bestemde fondsen 1038694 vs 1134737; tick1433; primary official NBB WVV 13"),
    ("bud_rlkm_capsub_2025", "2025", "816360", "2025 kapitaalsubsidies 816360 vs 882069; tick1433; primary official NBB WVV 15"),
    ("bud_rlkm_debt_2025", "2025", "2886066", "2025 schulden 2886066 vs 3191376 (LT empty); tick1433; primary official NBB WVV 17/49"),
    ("bud_rlkm_stdebt_2025", "2025", "1079664", "2025 ST schulden 1079664 vs 820455; tick1433; primary official NBB WVV 42/48"),
    ("bud_rlkm_lev_2025", "2025", "706688", "2025 leveranciers 706688 JUMP vs 447393; tick1433; primary official NBB WVV 440/4"),
    ("bud_rlkm_lev_2024", "2024", "447393", "2024 leveranciers 447393 comparative; tick1433; primary official NBB WVV 440/4"),
    ("bud_rlkm_taxsoc_2025", "2025", "372716", "2025 tax/soc 372716 vs 371964; tick1433; primary official NBB WVV 45"),
    ("bud_rlkm_tax_2025", "2025", "78533", "2025 belastingen 78533 vs 76987; tick1433; primary official NBB WVV 450/3"),
    ("bud_rlkm_bezold_2025", "2025", "294183", "2025 bezoldigingen/sociale lasten 294183 vs 294977; tick1433; primary official NBB WVV 454/9"),
    ("bud_rlkm_deferred_2025", "2025", "1806402", "2025 overlopend passief 1806402 vs 2370660; tick1433; primary official NBB WVV 492/3"),
    ("bud_rlkm_brutomarge_2025", "2025", "2443912", "2025 brutomarge 2443912 vs 2576463; omzet 70 empty; 73 empty; 60/61 empty; tick1433; primary official NBB WVV 9900"),
    ("bud_rlkm_brutomarge_2024", "2024", "2576463", "2024 brutomarge 2576463 comparative; tick1433; primary official NBB WVV 9900"),
    ("bud_rlkm_pers_2025", "2025", "2505888", "2025 pers 2505888 / 30.3 VTE vs 2484310 / 30.3; tick1433; primary official NBB WVV 62"),
    ("bud_rlkm_pers_2024", "2024", "2484310", "2024 pers 2484310 / 30.3 VTE comparative; tick1433; primary official NBB WVV 62"),
    ("bud_rlkm_afschr_2025", "2025", "122183", "2025 afschrijvingen 122183 vs 117861; tick1433; primary official NBB WVV 630"),
    ("bud_rlkm_andere_2025", "2025", "21990", "2025 andere bedrijfskosten 21990 vs 35467; tick1433; primary official NBB WVV 640/8"),
    ("bud_rlkm_expl_2025", "2025", "-206149", "2025 expl -206149 vs -73675; tick1433; primary official NBB WVV 9901"),
    ("bud_rlkm_expl_2024", "2024", "-73675", "2024 expl -73675 comparative; tick1433; primary official NBB WVV 9901"),
    ("bud_rlkm_finopbr_2025", "2025", "123293", "2025 fin opbr 123293 vs 120716; tick1433; primary official NBB WVV 75/76B"),
    ("bud_rlkm_finkost_2025", "2025", "6768", "2025 fin kosten 6768 vs 5802; tick1433; primary official NBB WVV 65/66B"),
    ("bud_rlkm_taxpnl_2025", "2025", "6418", "2025 belastingen resultaat 6418 vs 9229; tick1433; primary official NBB WVV 67/77"),
    ("bud_rlkm_pnl_2025", "2025", "-96043", "2025 PnL -96043 vs 32010; tick1433; primary official NBB WVV 9904"),
    ("bud_rlkm_pnl_2024", "2024", "32010", "2024 PnL 32010 comparative; tick1433; primary official NBB WVV 9904"),
    ("bud_rlkm_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1433; primary official NBB WVV"),
    ("bud_rlkm_capex_2025", "2025", "287199", "2025 MVA aanschaffingen 287199; IVA/FVA aanschaf empty; tick1433; primary official NBB WVV 8169"),
    ("bud_rlkm_onttrekking_2025", "2025", "96043", "2025 onttrekking bestemde fondsen 96043; tick1433; primary official NBB WVV 791"),
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

# --- commitments / leaderboard / foi ---
append_lf(DATA / "commitments.csv", [
    f"comm_rlkm_jr2025_bruto,Regionaal Landschap Kempen en Maasland VZW JR2025 leftover IGS dual (brutomarge 2.44m / pers 2.51m / cash 1.80m),{ENT},RL Kempen en Maasland VZW / 11 Kempen-Maasland cities,WVV VZW; NBB neerlegging; 11 Kempen-Maasland gemeenten + provincie Limburg,2026-04-01,1990,,2443912,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00094832.pdf,Local leftover IGS map VL Kempen-Maasland landschap — 2.44m brutomarge / empty 70/73/60/61 / pers 2.51m,Publish empty 70/73/60/61 split + other recv drop + leveranciers jump + vennoten share-pct + IOED relation; do not keep leftover RLKM VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Limburg>KempenMaasland>RLKM>JR2025_L5,tick1433; assets 4741120 omzet empty diensten empty pers 2505888 pnl -96043 equity 1855054 cash 1802565 debt 2886066 capex 287199 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlkm_omzet_empty_pers_2_51m_cash_1_80m,Regionaal Landschap Kempen en Maasland VZW JR2025 leftover IGS: brutomarge 2.44m / empty 70-73-60/61 / pers 2.51m / cash 1.80m,L5,local_budget_line,Vlaanderen>Limburg>KempenMaasland>RLKM>JR2025_L5,2443912,4741120,Leftover dual IGS VZW: assets 4.74m / equity 1.86m / pnl -0.10m / omzet empty / diensten empty / pers 2.51m 30.3 VTE / cash 1.80m JUMP / debt 2.89m / dividend 0,strong,{SRC},RL Kempen en Maasland VZW / 11 Kempen-Maasland cities,Local leftover IGS map VL Kempen-Maasland landschap — JR2025 live; dual empty 70/73/60/61 FOI,Official NBB WVV 2026-08-19: brutomarge 2.44m / pers 2.51m / cash 1.80m / PnL -0.10m,6.8,7.2,2.2,6.4,Publish empty 70/73/60/61 split + other recv drop + leveranciers jump + vennoten share-pct + IOED relation; do not keep leftover RLKM VZW as dual unpublished vehicle,active,,tick1433; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / AGB Genk / AGBIM",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Limburg>KempenMaasland>RLKM>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + pers 62 2505888 / 30.3 VTE + cash JUMP 1802565 vs 1639737 + other recv DROP 835225 vs 1795297 + leveranciers JUMP 706688 vs 447393 + deferred 1806402 + CIP 218599 + IOED same-VZW relation unpublished + vennoten share-pct unpublished + commissaris unpublished,Leftover RLKM VZW after leftover AGB hunt: 2.44m brutomarge / empty 70/73/60/61 hides public-perimeter landschap vehicle,8,Regionaal Landschap Kempen en Maasland vzw / Bestuursorgaan,info@rlkm.be,Winterslagstraat 87 3600 Genk,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlkm_jr2025_bruto,lb_rlkm_omzet_empty_pers_2_51m_cash_1_80m,{TS},{TS},tick1433 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (53190 bytes 15p deposit 2026-00094832). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Zuid-Hageland/Rivierenland/Pajottenland/Vlaamse Ardennen JR2025 CDN live leftover for next.",
])
print("foi_queue +1")

# --- research_queue surgical ---
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
if not last_s.startswith("rq_1433,"):
    raise SystemExit(f"expected last row rq_1433, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1433 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1433,RL Kempen en Maasland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlkm,"
    "Completed: Regionaal Landschap Kempen en Maasland VZW leftover IGS / regionaal landschap of 11 mined Kempen-Maasland cities after leftover AGB hunt; KBO 0443.302.272 Actief; live JR2025 official NBB WVV VKT-VZW PDF (53190 bytes 15p deposit 2026-00094832; AV 01.04.2026; created 30.04.2026; neerlegging 2026-04-30; no commissaris named); sourced euros assets 4741120 omzet empty diensten empty pers 2505888 pnl -96043 equity 1855054 cash 1802565 debt 2886066 capex 287199 dividend 0; FOI ready empty 70/73/60/61 / pers 2.51m / other recv drop / leveranciers jump / IOED relation,"
    f"{GAP},2026-08-19T11:21:00Z,{TS},"
    "tick1433 RL Kempen en Maasland VZW leftover IGS residual; KBO 0443.302.272; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1434 residual dual L5 VL"
)
spawn = (
    "rq_1434,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1433 done including RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Zuid-Hageland 0899.555.630 JR2025 CDN 2026-00075887 LIVE leftover; leftover RL Rivierenland 0899.152.980 JR2025 CDN 2026-00071020 LIVE leftover; leftover RL Pajottenland en Zennevallei 0458.521.374 JR2025 CDN 2026-00101632 LIVE leftover; leftover RL Vlaamse Ardennen tot Dender 0449.013.097 JR2025 CDN 2026-00367158 LIVE leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1433 after RL Kempen en Maasland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Zuid-Hageland/Rivierenland/Pajottenland/Vlaamse Ardennen if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1433=done + rq_1434 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1433 RL Kempen en Maasland leftover IGS residual; KBO 0443.302.272; live JR2025 NBB WVV PDF; sourced euros assets 4741120 omzet empty diensten empty pers 2505888 pnl -96043 equity 1855054 cash 1802565 debt 2886066 capex 287199 dividend 0; FOI ready empty 70/73/60/61 / pers 2.51m / other recv drop / leveranciers jump / IOED relation; next rq_1434 residual dual L5 VL leftover RL Zuid-Hageland/Rivierenland/Pajottenland/Vlaamse Ardennen if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1433,1433,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1433")

# --- loop_log ---
entry = (
    "\n## Tick 1433 - 2026-08-19 - rq_1433 RL Kempen en Maasland dual residual leftover\n"
    "- Unit: Regionaal Landschap Kempen en Maasland VZW / RLKM (leftover IGS / regionaal landschap of 11 mined Kempen-Maasland cities; 2 VE) after residual dual hunt (KBO **0443.302.272**; official rlkm.be; live NBB WVV VKT-VZW deposit **2026-00094832** PDF 53190 bytes / 15p; AV **01.04.2026**; created **30.04.2026**; neerlegging **2026-04-30**; model **VKT-VZW** 23.0.8 m04-f; no commissaris named; VKT-VZW 6.2/6.5/6.6/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.3 + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined; leftover AGB of member cities already mined (AGB Genk / AGBIM Maaseik / AGB Diepenbeek) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381). Leftover IGS Regionaal Landschap Kempen en Maasland VZW statutory CDN live this tick (HTTP 200 / application/pdf / 53190 / 15p; SBM jaar **2025-12-31**; neerlegging 2026-04-30) — taken (hunt order #2 leftover unmined RL VZW of mined Kempen-Maasland cities with full WVV balans; second named leftover RL after Houtland still JR2024). Distinct from already-mined RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / AGB Genk / AGBIM. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Kempen en Maasland / 0443.302.272 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **19.06.1990**; statutaire naam REGIONAAL LANDSCHAP KEMPEN EN MAASLAND since 19.01.1994; VZW since 19.06.1990; zetel Winterslagstraat 87 3600 Genk since 28.03.2000; **2 VE**; KBO no tel/e-mail/web; official site https://rlkm.be/; e-mail info@rlkm.be; tel +32 (0)89 69 11 20; dagelijks bestuur Ignace Schops; NACE 91.420; Werkgever RSZ since 01.07.1990; btw since 01.01.2016; aanbestedende overheid since 19.06.1990. WVV 2.1 voorzitter Olaerts Laura; ondervoorzitter Brys Rik. Official site 11 leden-gemeenten: As / Bree / Dilsen-Stokkem / Genk / Kinrooi / Lanaken / Maaseik / Maasmechelen / Oudsbergen / Peer / Zutendaal. IOED Kempen en Maasland is a 9-city channel of the same VZW. Named share-% unpublished. Contact info@rlkm.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **2505888** / **30,3 VTE**): assets **4741120** (was 5208182); fixed **1195488** / IVA **27488** / MVA **1167800** (gebouwen **833852**; machines **84737**; meubilair **26194**; leasing **259**; overige **4159**; CIP **218599**) / FVA **200**; current **3545632**; voorraden **191257**; ST recv **1008915** (trade **173690** / other **835225 DROP** vs 1795297); geldbeleggingen **500000**; cash **1802565 JUMP** vs 1639737; prepaid **42895**; equity **1855054** (bestemde fondsen **1038694**; capsub **816360**); voorzieningen empty; schulden **2886066** (LT empty vs 261; ST **1079664** waarvan LT-due **261** + leveranciers **706688 JUMP** vs 447393 + tax **78533** + soc/bezold **294183**; deferred **1806402** vs 2370660); brutomarge **2443912** vs 2576463; omzet empty; 73 empty; 60/61 empty; pers **2505888** / **30,3 VTE** / 46036 uur / YE **30,7**; afschr **122183**; andere bedrijfskosten **21990**; expl **−206149** vs −73675; fin opbr **123293**; fin kosten **6768**; tax **6418**; PnL **−96043** vs +32010; dividend **0**; onttrekking EV **96043**; capex **287199**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlkm` parent `sec_flanders`; budgets +50 executed; commitments +1 envelope 2443912 AV 01.04.2026; leaderboard +1 annual 2443912 / total 4741120; foi_queue +1 status=ready never sent; research_queue surgical rq_1433=done + rq_1434 spawn; loop_state ticks_completed=1433.\n"
    "- FOI: `gap_rlkm_omzet_empty_pers_2_51m_cash_1_80m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 2.51m 30.3 VTE deelwerking unpublished / other recv DROP 0.84m / leveranciers JUMP 0.71m / cash JUMP 1.80m / deferred 1.81m / CIP 0.22m / vennoten share-pct / IOED same-VZW relation / commissaris unpublished.\n"
    "- Next: rq_1434 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Zuid-Hageland **0899.555.630** JR2025 CDN **2026-00075887** LIVE — STRONG next leftover RL. Leftover RL Rivierenland **0899.152.980** JR2025 CDN **2026-00071020** LIVE leftover. Leftover RL Pajottenland en Zennevallei **0458.521.374** JR2025 CDN **2026-00101632** LIVE leftover. Leftover RL Vlaamse Ardennen tot Dender **0449.013.097** JR2025 CDN **2026-00367158** LIVE leftover. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1433")
print("tick1433 writes done")
