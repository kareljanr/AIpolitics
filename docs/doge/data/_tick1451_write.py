#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1451 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:40:00Z"
ENT = "vzw_rlhp"
SRC = "src_rlhp_jr2025_nbb"
GAP = "gap_rlhp_omzet_0_47m_pers_1_02m_cash_0_68m_l5"
LB = "lb_rlhp_omzet_0_47m_pers_1_02m_cash_0_68m"
COMM = "comm_rlhp_jr2025_bruto"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlhp_jr2025_nbb,Regionaal Landschap Houtland & Polders VZW official NBB WVV VKT-VZW JR2025,http://cdn.staatsbladmonitor.be/2026pdf/2026-00386406.pdf,NBB Central Balance Sheet Office,2026-08-19,budget,tick1451; official NBB WVV VKT-VZW deposit 2026-00386406 PDF 17p / 55356 bytes; pdfinfo created 07.08.2026; header 03.08.2026; AV 27.05.2026; KBO 0472.947.254; assets 1205135 cash 684137 debt 651114 bruto 1108773 omzet 472153 diensten 701947 pers 1015186 13.7 VTE pnl 69752 equity 554021",
    "src_rlhp_site,Regionaal Landschap Houtland & Polders official site,https://www.rlhp.be/,Regionaal Landschap Houtland & Polders VZW,2026-08-19,official_register,tick1451; leftover IGS / regionaal landschap of mined Houtland-Polders cities; zetel Tillegemstraat 81 8200 Brugge; contact info@rlhp.be",
    "src_kbo_rlhp_0472947254,KBO Regionaal Landschap Houtland & Polders 0472.947.254,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472947254,KBO Public Search FOD Economie,2026-08-19,official_register,tick1451; Actief since 10.05.2000; naam Regionaal Landschap Houtland & Polders since 01.07.2021; afkorting RLHP; zetel Tillegemstraat 81 8200 Brugge since 25.02.2003; 1 VE; VZW; NACE 91.420 / 91.042; Werkgever RSZ since 01.01.2002; 32 functiehouders; replaces 0851.923.482",
    "src_rlhp_foi_contact,Regionaal Landschap Houtland & Polders FOI channel (info@rlhp.be; Tillegemstraat 81 Brugge),https://www.rlhp.be/,Regionaal Landschap Houtland & Polders VZW,2026-08-19,official_register,tick1451; Houtland leftover RL + provincie West-Vlaanderen; NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlhp," in raw or raw.startswith(b"vzw_rlhp,"):
    raise SystemExit("vzw_rlhp already present")
if b"0472.947.254" in raw or b"0472947254" in raw:
    raise SystemExit("RL Houtland KBO already present")
row = (
    "vzw_rlhp,Regionaal Landschap Houtland & Polders VZW (leftover IGS / regionaal landschap of mined Houtland-Polders cities; NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO),"
    "Paysage Regional Houtland et Polders ASBL (IGS residuel / paysage regional Houtland-Polders),"
    "Regionaal Landschap Houtland & Polders leftover IGS / regional-landscape VZW of mined Houtland-Polders municipalities (not Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart),"
    "other,sec_flanders,nl,https://www.rlhp.be/,info@rlhp.be,Tillegemstraat 81 8200 Brugge,"
    "tick1451 leftover residual IGS/RL VZW of mined Houtland-Polders cities after leftover AGB hunt; KBO 0472.947.254 Actief since 10.05.2000; live JR2025 NBB WVV PDF; sourced euros assets 1205135 omzet 472153 diensten 701947 pers 1015186 13.7 VTE pnl 69752 equity 554021 cash 684137 debt 651114 capex 31480 dividend 0 bruto 1108773 subsidies 1195258; FOI ready omzet/subs split / pers 1.02m / cash JUMP / deferred JUMP / debt JUMP / 1 VE / leden share-pct; distinct from leftover Bosgroep Houtland 0866.482.291 (same Tillegemstraat 81 address) / already-mined RL Westhoek 1438 / leftover RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO / AGB Oostkamp"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlhp")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_rlhp_assets_2025", "2025", "1205135", "2025 assets 1205135 (was 961273); tick1451; primary official NBB WVV"),
    ("bud_rlhp_fixed_2025", "2025", "61280", "2025 vaste activa 61280 (was 37774); tick1451; primary official NBB WVV"),
    ("bud_rlhp_iva_2025", "2025", "0", "2025 IVA empty; 6.1.1 not filed; tick1451; primary official NBB WVV"),
    ("bud_rlhp_mva_2025", "2025", "61280", "2025 MVA 61280 installaties 25789 + meubilair 35491 (was 37774); tick1451; primary official NBB WVV"),
    ("bud_rlhp_install_2025", "2025", "25789", "2025 installaties 23 25789 (was 22768); tick1451; primary official NBB WVV"),
    ("bud_rlhp_meubilair_2025", "2025", "35491", "2025 meubilair 24 35491 (was 15006); tick1451; primary official NBB WVV"),
    ("bud_rlhp_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1451; primary official NBB WVV"),
    ("bud_rlhp_current_2025", "2025", "1143855", "2025 vlottend 1143855 (was 923499); tick1451; primary official NBB WVV"),
    ("bud_rlhp_voorraden_2025", "2025", "0", "2025 voorraden 0 DROP (was 58354); tick1451; primary official NBB WVV"),
    ("bud_rlhp_strecv_2025", "2025", "427714", "2025 ST vorderingen 427714 (was 532272); tick1451; primary official NBB WVV"),
    ("bud_rlhp_trade_2025", "2025", "168510", "2025 handelsvorderingen 168510 (was 130290); tick1451; primary official NBB WVV"),
    ("bud_rlhp_othrecv_2025", "2025", "259204", "2025 overige vorderingen 259204 DROP (was 401982); tick1451; primary official NBB WVV"),
    ("bud_rlhp_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1451; primary official NBB WVV"),
    ("bud_rlhp_cash_2025", "2025", "684137", "2025 liquide middelen 684137 JUMP (was 317324); tick1451; primary official NBB WVV"),
    ("bud_rlhp_prepaid_2025", "2025", "32004", "2025 prepaid 32004 (was 15549); tick1451; primary official NBB WVV"),
    ("bud_rlhp_equity_2025", "2025", "554021", "2025 EV 554021 (was 484269); tick1451; primary official NBB WVV"),
    ("bud_rlhp_bestemde_2025", "2025", "554021", "2025 bestemde fondsen 554021 (was 484269); tick1451; primary official NBB WVV"),
    ("bud_rlhp_overgedragen_2025", "2025", "0", "2025 overgedragen 0; tick1451; primary official NBB WVV"),
    ("bud_rlhp_debt_2025", "2025", "651114", "2025 schulden 651114 JUMP (was 477004; LT empty); tick1451; primary official NBB WVV"),
    ("bud_rlhp_stdebt_2025", "2025", "298313", "2025 ST schulden 298313 (was 371095); tick1451; primary official NBB WVV"),
    ("bud_rlhp_lev_2025", "2025", "138102", "2025 leveranciers 138102 (was 119739); tick1451; primary official NBB WVV"),
    ("bud_rlhp_tax_2025", "2025", "0", "2025 belastingen 450/3 0 (was 23457); tick1451; primary official NBB WVV"),
    ("bud_rlhp_bezold_2025", "2025", "107542", "2025 bezoldigingen 454/9 107542 (was 174396); tick1451; primary official NBB WVV"),
    ("bud_rlhp_othdebt_2025", "2025", "52669", "2025 overige schulden 52669 (was 53503); tick1451; primary official NBB WVV"),
    ("bud_rlhp_deferred_2025", "2025", "352801", "2025 deferred 352801 JUMP (was 105909); tick1451; primary official NBB WVV"),
    ("bud_rlhp_bruto_2025", "2025", "1108773", "2025 brutomarge 9900 1108773 (was 1042930); tick1451; primary official NBB WVV"),
    ("bud_rlhp_omzet_2025", "2025", "472153", "2025 omzet 70 472153 (was 427809); tick1451; primary official NBB WVV"),
    ("bud_rlhp_subs_2025", "2025", "1195258", "2025 lidgeld/subsidies 73 1195258 (was 1078602); tick1451; primary official NBB WVV"),
    ("bud_rlhp_diensten_2025", "2025", "701947", "2025 60/61 701947 (was 604292); tick1451; primary official NBB WVV"),
    ("bud_rlhp_pers_2025", "2025", "1015186", "2025 pers 62 1015186 / 9087 = 13.7 VTE (was 982050 / 12.5); tick1451; primary official NBB WVV"),
    ("bud_rlhp_afschr_2025", "2025", "23260", "2025 afschrijvingen 630 23260 (was 18472); tick1451; primary official NBB WVV"),
    ("bud_rlhp_andere_2025", "2025", "784", "2025 andere bedrijfskosten 640/8 784 (was 1545); tick1451; primary official NBB WVV"),
    ("bud_rlhp_expl_2025", "2025", "69543", "2025 expl 69543 (was 40863); tick1451; primary official NBB WVV"),
    ("bud_rlhp_finopbr_2025", "2025", "1257", "2025 fin opbr 1257 all recurrent (was 2560); tick1451; primary official NBB WVV"),
    ("bud_rlhp_finkost_2025", "2025", "728", "2025 fin kosten 728 all recurrent (was 433); tick1451; primary official NBB WVV"),
    ("bud_rlhp_taxpnl_2025", "2025", "320", "2025 tax 67/77 320 (was 430); tick1451; primary official NBB WVV"),
    ("bud_rlhp_pnl_2025", "2025", "69752", "2025 PnL 69752 (was 42560); tick1451; primary official NBB WVV"),
    ("bud_rlhp_div_2025", "2025", "0", "2025 dividend 0; tick1451; primary official NBB WVV"),
    ("bud_rlhp_capex_2025", "2025", "31480", "2025 capex MVA aanschaf 8169 31480; IVA/FVA empty; tick1451; primary official NBB WVV"),
    ("bud_rlhp_onttrekking_2025", "2025", "32936", "2025 onttrekking bestemde 791 32936; tick1451; primary official NBB WVV"),
    ("bud_rlhp_toevoeging_2025", "2025", "102688", "2025 toevoeging bestemde 691 102688; tick1451; primary official NBB WVV"),
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
    f"{COMM},Regionaal Landschap Houtland & Polders VZW JR2025 leftover IGS dual (bruto 1.11m / omzet 0.47m / pers 1.02m / cash JUMP 0.68m),{ENT},Regionaal Landschap Houtland & Polders VZW / mined Houtland-Polders cities,WVV VZW; official NBB VKT-VZW; provincie West-Vlaanderen,2026-05-27,2000,,1108773,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00386406.pdf,Local leftover IGS map VL RL Houtland — bruto 1.11m / omzet 0.47m / pers 1.02m / cash JUMP 0.68m,Publish omzet/subs split + pers 1.02m + 13.7 VTE + cash JUMP + deferred JUMP + debt JUMP + 1 VE + vennoten share-pct; do not keep leftover RLHP VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>WestVlaanderen>RLHoutland>JR2025_L5,tick1451; assets 1205135 omzet 472153 diensten 701947 pers 1015186 13.7 VTE pnl 69752 equity 554021 cash 684137 debt 651114 capex 31480 dividend 0 bruto 1108773 subsidies 1195258; FOI ready not sent; not TE-additive of 348bn; NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},Regionaal Landschap Houtland & Polders VZW JR2025 leftover IGS: omzet 0.47m / pers 1.02m / cash JUMP 0.68m,L5,local_budget_line,Vlaanderen>WestVlaanderen>RLHoutland>JR2025_L5,1108773,1205135,Leftover dual IGS/RL VZW: assets 1.21m / equity 0.55m / pnl +70k / omzet 0.47m / 73 1.20m / 60-61 0.70m / pers 1.02m 13.7 VTE / cash 0.68m JUMP / debt 0.65m JUMP / dividend 0 / NBB 2026-00386406,strong,{SRC},Regionaal Landschap Houtland & Polders VZW / mined Houtland-Polders cities,Local leftover IGS map VL RL Houtland — JR2025 NBB WVV live; omzet/subs/pers FOI,Official NBB WVV 2026-08-19: bruto 1.11m / omzet 0.47m / pers 1.02m / cash JUMP 0.68m / PnL +70k,6.8,6.4,2.5,6.5,Publish omzet/subs split + pers 1.02m + 13.7 VTE + cash JUMP + deferred JUMP + debt JUMP + 1 VE + vennoten share-pct; do not keep leftover RLHP VZW as dual unpublished vehicle,active,,tick1451; leftover IGS/RL after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Bosgroep Houtland / already-mined RL Westhoek 1438 / leftover RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>WestVlaanderen>RLHoutland>JR2025_L5,{ENT},omzet 70 472153 + 73 1195258 + 60/61 701947 + bruto 1108773 + pers 62 1015186 13.7 VTE + 1 VE + cash 684137 JUMP vs 317324 + deferred JUMP 352801 vs 105909 + debt JUMP 651114 vs 477004 + voorraden DROP 0 vs 58354 + other recv DROP 259204 vs 401982 + capex 31480 + vennoten share-pct unpublished + relation to Bosgroep Houtland/RL Westhoek/RL West-Vlaamse Hart/DVV Westhoek/CO7/Viertoren/IVBO/provincie unpublished,Leftover RLHP VZW after leftover AGB hunt: bruto 1.11m / omzet 0.47m / pers 1.02m hides public-perimeter landschap vehicle,8,Regionaal Landschap Houtland & Polders vzw / Bestuursorgaan,info@rlhp.be,Tillegemstraat 81 8200 Brugge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1451 leftover IGS/RL after honest leftover AGB hunt; live JR2025 NBB WVV PDF now extracted (55356 bytes 17p). FOI ready not sent. NOT every-10. NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. IVAREM JR2025 now appears on Busibee (not taken). VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. CoLimBo 0890.220.171 leftover Bosgroep daughter JR2025 live (not taken).",
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
if not last_s.startswith("rq_1451,"):
    raise SystemExit(f"expected last row rq_1451, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1451 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1451,Regionaal Landschap Houtland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlhp,"
    "Completed: Regionaal Landschap Houtland & Polders VZW leftover IGS / RL of mined Houtland-Polders cities after leftover AGB hunt; KBO 0472.947.254 Actief; live JR2025 official NBB WVV VKT-VZW PDF (55356 bytes 17p deposit 2026-00386406; AV 27.05.2026; header 03.08.2026; created 07.08.2026; no commissaris listed); sourced euros assets 1205135 omzet 472153 diensten 701947 pers 1015186 13.7 VTE pnl 69752 equity 554021 cash 684137 debt 651114 capex 31480 dividend 0 bruto 1108773 subsidies 1195258; FOI ready omzet/subs split / pers 1.02m / cash JUMP / deferred JUMP / debt JUMP / 1 VE / leden share-pct; NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO,"
    f"{GAP},2026-08-19T13:25:00Z,{TS},"
    "tick1451 RL Houtland leftover IGS/RL residual; KBO 0472.947.254; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1452 leftover AGB/Bosgroep if CDN live else IVAREM now JR2025 / CoLimBo leftover daughter / leftover IOED/cultuur-IGS/Hart"
)
spawn = (
    "rq_1452,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1451 done including Regionaal Landschap Houtland 1451 leftover IGS live NBB WVV / Bosgroep Kempen Noord 1450 leftover IGS live NBB WVV + every-10 / Bosgroep Zuiderkempen 1449 leftover IGS live NBB WVV / Bosgroep Antwerpse Gordel 1448 leftover IGS live NBB WVV / Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1451); leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS IVAREM 0267.403.264 JR2025 now appears (Busibee 2025 PDF) — take if a 2025 statutory PDF actually downloads (STRONG next leftover IGS); leftover CoLimBo 0890.220.171 leftover Bosgroep Limburg daughter JR2025 live — take only after leftover AGB/IGS/Bosgroep; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening; leftover IGS Zender 0822.146.066 last JR still 2024; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening; leftover IGS Dijk92 0806.383.071 last JR still 2024; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Regionaal Landschap Houtland 1451 / Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL West-Vlaamse Hart still no jaarrekening; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1451 after RL Houtland leftover IGS live NBB WVV JR2025; leftover AGB/Bosgroep if CDN live else IVAREM now JR2025 / CoLimBo leftover daughter / leftover IOED/cultuur-IGS/Hart"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1451=done + rq_1452 spawned; keep", last_line_start)

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
    f"tick1451 Regionaal Landschap Houtland leftover IGS/RL residual; KBO 0472.947.254; live JR2025 NBB WVV PDF; sourced euros assets 1205135 omzet 472153 diensten 701947 pers 1015186 13.7 VTE pnl 69752 equity 554021 cash 684137 debt 651114 capex 31480 dividend 0 bruto 1108773 subsidies 1195258; FOI ready omzet/subs split / pers 1.02m / cash JUMP / deferred JUMP / debt JUMP / 1 VE; NOT Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart; next rq_1452 leftover AGB/Bosgroep if CDN live else IVAREM now JR2025 / CoLimBo leftover daughter / leftover IOED/cultuur-IGS/Hart; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1451,1451,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1451")

entry = (
    "\n## Tick 1451 - 2026-08-19 - rq_1451 Regionaal Landschap Houtland dual residual leftover\n"
    "- Unit: Regionaal Landschap Houtland & Polders VZW / RLHP (leftover IGS / regionaal landschap of mined Houtland-Polders cities; 1 VE) after residual dual hunt (KBO **0472.947.254**; official rlhp.be; live official NBB WVV VKT-VZW PDF **55356** bytes / 17p; deposit **2026-00386406**; AV **27.05.2026**; header **03.08.2026**; pdfinfo created **07.08.2026**; model **VKT-VZW** 23.0.10 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.3/6.3/6.5/6.6/7/8 not filed; 6.1.2 MVA + 6.2 fondsen + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; official bornem.be still JR2024 only); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member-region cities already mined (AGB Oostkamp / AGB Bredene / AGB Blankenberge liquidated / AGSO Knokke / AGB Middelkerke) — skipped. Member cities without AGB in entities (Beernem / De Haan / Ichtegem / Jabbeke / Oudenburg / Zedelgem / Zuienkerke / Damme / Gistel / Torhout) — no new 2025 AGB PDF this tick. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 JR2025 now appears on Busibee (not taken; leftover RL first). Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen this tick: WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no jaarrekening (SBM/Busibee empty). Leftover CoLimBo 0890.220.171 leftover Bosgroep daughter JR2025 live — not taken (leftover RL first). Leftover IGS Regionaal Landschap Houtland & Polders statutory NBB WVV deposit `2026-00386406` live this tick (official VKT-VZW PDF 55356 / 17p; SBM CDN HEAD 403; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined RL of mined Houtland-Polders cities; still JR2024 as of 1450). Distinct from leftover **Bosgroep Houtland** (KBO 0866.482.291; same Tillegemstraat 81 8200 address; bestuurder of this VZW since 20.06.2024 — NOT this entity) / already-mined **RL Westhoek** (vzw_rlwh tick 1438) / leftover **RL West-Vlaamse Hart** 0800.422.125 / DVV Westhoek / CO7 / Viertoren / IVBO / AGB Oostkamp. First confirmed not already extracted as JR2025 euros: no Regionaal Landschap Houtland / 0472.947.254 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **10.05.2000**; statutaire naam Regionaal Landschap Houtland & Polders since 01.07.2021; afkorting **RLHP** since 01.07.2021; VZW since 10.05.2000; zetel Tillegemstraat 81 8200 Brugge since 25.02.2003; **1 VE**; official site https://www.rlhp.be/; contact info@rlhp.be; NACE RSZ 91.420 / 91.042; Werkgever RSZ since 01.01.2002; **32 functiehouders**. Replaces 0851.923.482 closed 11.06.2010. PDF bestuurders include ANB / ABS / Boerenbond WVL / Bosgroep Houtland + gemeenten Beernem / Bredene / De Haan / Ichtegem / Jabbeke / Knokke-Heist / Oostkamp / Oudenburg / Zedelgem / Zuienkerke + steden Blankenberge / Brugge / Damme / Gistel / Torhout + provincie West-Vlaanderen + Natuurpunt afdelingen. Named member-city share-% unpublished. Contact info@rlhp.be. Prior-year figures identical. NBB consult skipped (403/SPA); SBM HTML IP-blacklisted from box curl; SBM CDN 403 this tick. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Not every-10 (next 1460 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 472153**; **lidgeld/subsidies 73 1195258**; **60/61 701947**; pers 62 **1015186** / **13,7 VTE** vs 982050 / 12,5): assets **1205135** (was 961273); fixed **61280** vs 37774 / IVA empty / MVA **61280** (installaties **25789**; meubilair **35491**) / FVA empty; current **1143855** vs 923499; voorraden **0 DROP** vs 58354; ST recv **427714** vs 532272 (trade **168510** vs 130290 / other **259204 DROP** vs 401982); geldbeleg empty; cash **684137 JUMP** vs 317324; prepaid **32004** vs 15549; equity **554021** (bestemde **554021**; overgedragen **0**); voorzieningen empty; schulden **651114 JUMP** vs 477004 (LT empty; ST **298313** vs 371095 waarvan leveranciers **138102** vs 119739 + tax **0** vs 23457 + bezold **107542** vs 174396 + overige **52669** vs 53503; deferred **352801 JUMP** vs 105909); brutomarge **1108773** vs 1042930; omzet **472153** vs 427809; 73 **1195258** vs 1078602; 60/61 **701947** vs 604292; pers **1015186** / **13,7 VTE** / 19920 uur / YE **13,6**; afschr **23260**; andere **784**; expl **+69543** vs +40863; fin opbr **1257** all recurrent; fin kosten **728**; tax **320**; PnL **+69752** vs +42560; dividend **0**; onttrekking bestemde **32936**; toevoeging bestemde **102688**; over te dragen **0**; capex **31480** (MVA aanschaf only). PDF cross-checks: 61280+1143855=1205135; 554021+651114=1205135; 1108773-1015186-23260-784=69543; 69543+1257-728-320=69752; 69752+32936-102688=0.\n"
    f"- CSVs: sources +4; entities +1 `vzw_rlhp` parent `sec_flanders`; budgets +{{inv_budgets_added}} executed; commitments +1 envelope 1108773 AV 27.05.2026; leaderboard +1 annual 1108773 / total 1205135; foi_queue +1 status=ready never sent; research_queue surgical rq_1451=done + rq_1452 spawn; loop_state ticks_completed=1451. Inventory after write: budgets {{inv_budgets}} · commitments {{inv_commitments}} · leaderboard {{inv_leaderboard}} · entities {{inv_entities}} · sources {{inv_sources}} · FOI ready {{foi_ready}} / answered {{foi_ans}} / partial {{foi_part}} / total {{foi_tot}}.\n"
    "- FOI: `gap_rlhp_omzet_0_47m_pers_1_02m_cash_0_68m_l5` ready not sent — omzet 0.47m / 73 1.20m / 60-61 0.70m / pers 1.02m 13.7 VTE / cash JUMP 0.68m / deferred JUMP 0.35m / debt JUMP 0.65m / voorraden DROP 0 / other recv DROP / expl +70k / pnl +70k / 1 VE / capex 31k / vennoten share-pct / relation to Bosgroep Houtland / RL Westhoek / RL West-Vlaamse Hart / DVV Westhoek / CO7 / Viertoren / IVBO / provincie unpublished.\n"
    "- Next: rq_1452 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR this tick). Leftover IGS IVAREM **0267.403.264** JR2025 now appears (STRONG next leftover IGS if statutory PDF downloads). Leftover CoLimBo **0890.220.171** leftover Bosgroep daughter JR2025 live — only after leftover AGB/IGS/Bosgroep. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined Regionaal Landschap Houtland 1451 / Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022. Next every-10 is 1460.\n"
)
entry = entry.replace("{inv_budgets_added}", str(len(added))).replace("{inv_budgets}", str(inv["budgets.csv"])).replace("{inv_commitments}", str(inv["commitments.csv"])).replace("{inv_leaderboard}", str(inv["leaderboard.csv"])).replace("{inv_entities}", str(inv["entities.csv"])).replace("{inv_sources}", str(inv["sources.csv"])).replace("{foi_ready}", str(foi_ready)).replace("{foi_ans}", str(foi_ans)).replace("{foi_part}", str(foi_part)).replace("{foi_tot}", str(foi_tot))
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1451 -" in lraw:
    raise SystemExit("loop_log already has tick 1451 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1451")
print("DONE tick 1451")
