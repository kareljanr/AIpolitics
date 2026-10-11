#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1434 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:55:00Z"
ENT = "vzw_rlzh"
SRC = "src_rlzh_jr2025_nbb"
GAP = "gap_rlzh_omzet_empty_subs_1_52m_diensten_1_04m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlzh_jr2025_nbb,Regionaal Landschap Zuid-Hageland VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00075887.pdf,NBB / RL Zuid-Hageland VZW,2026-08-19,budget,tick1434; VKT-VZW 25.0.9 m04-f PDF 15p / 53572 bytes deposit 2026-00075887; AV 25.03.2026; created 09.04.2026; neerlegging 2026-04-10; KBO 0899.555.630; assets 1079430 cash 473364 debt 688960 brutomarge 999242 code73 1520687 code60_61 1044796 pers 965261 pnl 31008; no commissaris named",
    "src_rlzh_site,Regionaal Landschap Zuid-Hageland official site,https://www.rlzh.be/,RL Zuid-Hageland VZW,2026-08-19,official_register,tick1434; leftover IGS / regionaal landschap of 9 Zuid-Hageland cities; zetel Schoolpad 43 3300 Tienen Pastorij Hakendover; contact info@rlzh.be; tel 016 81 52 77; dagelijks bestuur Kristien Justaert",
    "src_kbo_rlzh_0899555630,KBO Regionaal Landschap Zuid-Hageland 0899.555.630,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0899555630,KBO Public Search FOD Economie,2026-08-19,official_register,tick1434; Actief since 21.05.2008; naam since 21.05.2008; zetel Schoolpad(Hak) 43 3300 Tienen since 18.03.2010; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 19.01.2009",
    "src_rlzh_foi_contact,RL Zuid-Hageland FOI channel (info@rlzh.be; Schoolpad 43 Tienen),https://www.rlzh.be/contact/,RL Zuid-Hageland VZW,2026-08-19,official_register,tick1434; 9 member cities + provincie Vlaams-Brabant; voorzitter Marc Wijnants; ondervoorzitter Hugo Abts; IOED channel mentioned on team page info@ioedzuidhageland.be",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlzh," in raw or raw.startswith(b"vzw_rlzh,"):
    raise SystemExit("vzw_rlzh already present")
if b"0899.555.630" in raw or b"0899555630" in raw:
    raise SystemExit("RL Zuid-Hageland KBO already present")
row = (
    "vzw_rlzh,Regionaal Landschap Zuid-Hageland VZW (leftover IGS / regionaal landschap of 9 mined Zuid-Hageland cities),"
    "Regionaal Landschap Zuid-Hageland ASBL (IGS residuel / paysage regional Hageland sud),"
    "Regionaal Landschap Zuid-Hageland leftover IGS / regional landscape VZW of 9 Zuid-Hageland municipalities,"
    "other,sec_flanders,nl,https://www.rlzh.be/,info@rlzh.be,Schoolpad 43 3300 Tienen,"
    "tick1434 leftover residual IGS VZW of mined Zuid-Hageland cities after leftover AGB hunt; KBO 0899.555.630 Actief since 21.05.2008; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1079430 omzet empty diensten 1044796 pers 965261 pnl 31008 equity 390470 cash 473364 debt 688960 capex 3010 dividend 0 code73 1520687; FOI ready omzet empty / 73 vs 60-61 vs bruto / lev jump / othdebt jump; distinct from already-mined RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Zorgbedrijf Rivierenland / AGB Tienen"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlzh")

# --- budgets ---
BUDGETS = [
    ("bud_rlzh_assets_2025", "2025", "1079430", "2025 assets 1079430 VKT-VZW 20/58; tick1434; primary official NBB WVV"),
    ("bud_rlzh_assets_2024", "2024", "860212", "2024 assets 860212 comparative; tick1434; primary official NBB WVV 20/58"),
    ("bud_rlzh_fixed_2025", "2025", "5839", "2025 vaste activa 5839 vs 5795; tick1434; primary official NBB WVV 21/28"),
    ("bud_rlzh_iva_2025", "2025", "592", "2025 IVA 592 vs 894; tick1434; primary official NBB WVV 21"),
    ("bud_rlzh_mva_2025", "2025", "5247", "2025 MVA 5247 vs 4901; tick1434; primary official NBB WVV 22/27"),
    ("bud_rlzh_machines_2025", "2025", "2855", "2025 machines 2855 vs 1192; tick1434; primary official NBB WVV 23"),
    ("bud_rlzh_meubilair_2025", "2025", "2392", "2025 meubilair/rollend 2392 vs 3710; tick1434; primary official NBB WVV 24"),
    ("bud_rlzh_fva_2025", "2025", "0", "2025 FVA empty after disposal 50; tick1434; primary official NBB WVV 28"),
    ("bud_rlzh_current_2025", "2025", "1073592", "2025 vlottend 1073592 vs 854416; tick1434; primary official NBB WVV 29/58"),
    ("bud_rlzh_strecv_2025", "2025", "596489", "2025 ST vorderingen 596489 vs 453726; tick1434; primary official NBB WVV 40/41"),
    ("bud_rlzh_trade_2025", "2025", "141153", "2025 handelsvorderingen 141153 vs 173164; tick1434; primary official NBB WVV 40"),
    ("bud_rlzh_othrecv_2025", "2025", "455336", "2025 overige vorderingen 455336 JUMP vs 280562; tick1434; primary official NBB WVV 41"),
    ("bud_rlzh_othrecv_2024", "2024", "280562", "2024 overige vorderingen 280562 comparative; tick1434; primary official NBB WVV 41"),
    ("bud_rlzh_cash_2025", "2025", "473364", "2025 liquide middelen 473364 JUMP vs 386494; tick1434; primary official NBB WVV 54/58"),
    ("bud_rlzh_cash_2024", "2024", "386494", "2024 liquide middelen 386494 comparative; tick1434; primary official NBB WVV 54/58"),
    ("bud_rlzh_prepaid_2025", "2025", "3739", "2025 prepaid 3739 vs 14196; tick1434; primary official NBB WVV 490/1"),
    ("bud_rlzh_equity_2025", "2025", "390470", "2025 EV 390470 vs 359462; tick1434; primary official NBB WVV 10/15"),
    ("bud_rlzh_equity_2024", "2024", "359462", "2024 EV 359462 comparative; tick1434; primary official NBB WVV 10/15"),
    ("bud_rlzh_bestemde_2025", "2025", "275944", "2025 bestemde fondsen 275944 vs 268317; tick1434; primary official NBB WVV 13"),
    ("bud_rlzh_overgedragen_2025", "2025", "114527", "2025 overgedragen winst 114527 vs 91146; tick1434; primary official NBB WVV 14"),
    ("bud_rlzh_debt_2025", "2025", "688960", "2025 schulden 688960 JUMP vs 363867 (LT empty); tick1434; primary official NBB WVV 17/49"),
    ("bud_rlzh_debt_2024", "2024", "363867", "2024 schulden 363867 comparative; tick1434; primary official NBB WVV 17/49"),
    ("bud_rlzh_stdebt_2025", "2025", "495867", "2025 ST schulden 495867 vs 152778; tick1434; primary official NBB WVV 42/48"),
    ("bud_rlzh_lev_2025", "2025", "190377", "2025 leveranciers 190377 JUMP vs 24; tick1434; primary official NBB WVV 440/4"),
    ("bud_rlzh_lev_2024", "2024", "24", "2024 leveranciers 24 comparative; tick1434; primary official NBB WVV 440/4"),
    ("bud_rlzh_taxsoc_2025", "2025", "155490", "2025 tax/soc 155490 vs 142184; tick1434; primary official NBB WVV 45"),
    ("bud_rlzh_tax_2025", "2025", "27980", "2025 belastingen 27980 vs 9465; tick1434; primary official NBB WVV 450/3"),
    ("bud_rlzh_bezold_2025", "2025", "127510", "2025 bezoldigingen/sociale lasten 127510 vs 132719; tick1434; primary official NBB WVV 454/9"),
    ("bud_rlzh_othdebt_2025", "2025", "150000", "2025 overige schulden 150000 JUMP vs 10570; tick1434; primary official NBB WVV 48"),
    ("bud_rlzh_othdebt_2024", "2024", "10570", "2024 overige schulden 10570 comparative; tick1434; primary official NBB WVV 48"),
    ("bud_rlzh_deferred_2025", "2025", "193093", "2025 overlopend passief 193093 vs 211089; tick1434; primary official NBB WVV 492/3"),
    ("bud_rlzh_brutomarge_2025", "2025", "999242", "2025 brutomarge 999242 vs 973478; omzet 70 empty; 73 1520687; 60/61 1044796; tick1434; primary official NBB WVV 9900"),
    ("bud_rlzh_brutomarge_2024", "2024", "973478", "2024 brutomarge 973478 comparative; tick1434; primary official NBB WVV 9900"),
    ("bud_rlzh_subs_2025", "2025", "1520687", "2025 lidgeld/schenkingen/subsidies 73 1520687 vs 1419626; tick1434; primary official NBB WVV 73"),
    ("bud_rlzh_subs_2024", "2024", "1419626", "2024 lidgeld/schenkingen/subsidies 73 1419626 comparative; tick1434; primary official NBB WVV 73"),
    ("bud_rlzh_diensten_2025", "2025", "1044796", "2025 goederen/diensten 60/61 1044796 vs 856231; tick1434; primary official NBB WVV 60/61"),
    ("bud_rlzh_diensten_2024", "2024", "856231", "2024 goederen/diensten 60/61 856231 comparative; tick1434; primary official NBB WVV 60/61"),
    ("bud_rlzh_pers_2025", "2025", "965261", "2025 pers 965261 / 11.2 VTE vs 980516 / 11.7; tick1434; primary official NBB WVV 62"),
    ("bud_rlzh_pers_2024", "2024", "980516", "2024 pers 980516 / 11.7 VTE comparative; tick1434; primary official NBB WVV 62"),
    ("bud_rlzh_afschr_2025", "2025", "2967", "2025 afschrijvingen 2967 vs 2140; tick1434; primary official NBB WVV 630"),
    ("bud_rlzh_andere_2025", "2025", "595", "2025 andere bedrijfskosten 595 vs 1627; tick1434; primary official NBB WVV 640/8"),
    ("bud_rlzh_expl_2025", "2025", "30420", "2025 expl 30420 vs -10804; tick1434; primary official NBB WVV 9901"),
    ("bud_rlzh_expl_2024", "2024", "-10804", "2024 expl -10804 comparative; tick1434; primary official NBB WVV 9901"),
    ("bud_rlzh_finopbr_2025", "2025", "897", "2025 fin opbr 897 vs 1754; tick1434; primary official NBB WVV 75/76B"),
    ("bud_rlzh_finkost_2025", "2025", "310", "2025 fin kosten 310 vs 453; tick1434; primary official NBB WVV 65/66B"),
    ("bud_rlzh_pnl_2025", "2025", "31008", "2025 PnL 31008 vs -9502; tick1434; primary official NBB WVV 9904"),
    ("bud_rlzh_pnl_2024", "2024", "-9502", "2024 PnL -9502 comparative; tick1434; primary official NBB WVV 9904"),
    ("bud_rlzh_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1434; primary official NBB WVV"),
    ("bud_rlzh_capex_2025", "2025", "3010", "2025 MVA aanschaffingen 3010; IVA/FVA aanschaf empty; tick1434; primary official NBB WVV 8169"),
    ("bud_rlzh_onttrekking_2025", "2025", "2709", "2025 onttrekking bestemde fondsen 2709; tick1434; primary official NBB WVV 791"),
    ("bud_rlzh_toevoeging_2025", "2025", "10336", "2025 toevoeging bestemde fondsen 10336; tick1434; primary official NBB WVV 691"),
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
    f"comm_rlzh_jr2025_subs,Regionaal Landschap Zuid-Hageland VZW JR2025 leftover IGS dual (subsidies 1.52m / diensten 1.04m / pers 0.97m),{ENT},RL Zuid-Hageland VZW / 9 Zuid-Hageland cities,WVV VZW; NBB neerlegging; 9 Zuid-Hageland gemeenten + provincie Vlaams-Brabant,2026-03-25,2008,,1520687,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00075887.pdf,Local leftover IGS map VL Zuid-Hageland landschap — 1.52m subsidies / empty omzet 70 / diensten 1.04m / pers 0.97m,Publish empty 70 split + 73 vs 60/61 vs bruto + lev jump + othdebt jump + vennoten share-pct + IOED relation; do not keep leftover RLZH VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>VlaamsBrabant>ZuidHageland>RLZH>JR2025_L5,tick1434; assets 1079430 omzet empty diensten 1044796 pers 965261 pnl 31008 equity 390470 cash 473364 debt 688960 capex 3010 dividend 0 code73 1520687; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlzh_omzet_empty_subs_1_52m_diensten_1_04m,Regionaal Landschap Zuid-Hageland VZW JR2025 leftover IGS: subsidies 1.52m / empty omzet 70 / diensten 1.04m / pers 0.97m,L5,local_budget_line,Vlaanderen>VlaamsBrabant>ZuidHageland>RLZH>JR2025_L5,1520687,1079430,Leftover dual IGS VZW: assets 1.08m / equity 0.39m / pnl +0.03m / omzet empty / subsidies 1.52m / diensten 1.04m / pers 0.97m 11.2 VTE / cash 0.47m JUMP / debt 0.69m JUMP / lev 0.19m JUMP vs 24 / dividend 0,strong,{SRC},RL Zuid-Hageland VZW / 9 Zuid-Hageland cities,Local leftover IGS map VL Zuid-Hageland landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: subsidies 1.52m / diensten 1.04m / pers 0.97m / PnL +0.03m,6.6,6.5,2.2,6.1,Publish empty 70 split + 73 vs 60/61 vs bruto + lev jump + othdebt jump + vennoten share-pct + IOED relation; do not keep leftover RLZH VZW as dual unpublished vehicle,active,,tick1434; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Zorgbedrijf Rivierenland / AGB Tienen",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>VlaamsBrabant>ZuidHageland>RLZH>JR2025_L5,{ENT},omzet 70 empty + 73 1520687 + 60/61 1044796 + bruto 999242 != 73-60/61 475891 + pers 62 965261 / 11.2 VTE + cash JUMP 473364 vs 386494 + other recv JUMP 455336 vs 280562 + leveranciers JUMP 190377 vs 24 + othdebt JUMP 150000 vs 10570 + deferred 193093 + IOED relation unpublished + vennoten share-pct unpublished + commissaris unpublished + 2024 passiva/activa mismatch,Leftover RLZH VZW after leftover AGB hunt: 1.52m subsidies / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Zuid-Hageland vzw / Bestuursorgaan,info@rlzh.be,Schoolpad 43 3300 Tienen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlzh_jr2025_subs,lb_rlzh_omzet_empty_subs_1_52m_diensten_1_04m,{TS},{TS},tick1434 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (53572 bytes 15p deposit 2026-00075887). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Rivierenland/Pajottenland/Vlaamse Ardennen JR2025 CDN live leftover for next.",
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
if not last_s.startswith("rq_1434,"):
    raise SystemExit(f"expected last row rq_1434, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1434 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1434,RL Zuid-Hageland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlzh,"
    "Completed: Regionaal Landschap Zuid-Hageland VZW leftover IGS / regionaal landschap of 9 mined Zuid-Hageland cities after leftover AGB hunt; KBO 0899.555.630 Actief; live JR2025 official NBB WVV VKT-VZW PDF (53572 bytes 15p deposit 2026-00075887; AV 25.03.2026; created 09.04.2026; neerlegging 2026-04-10; no commissaris named); sourced euros assets 1079430 omzet empty diensten 1044796 pers 965261 pnl 31008 equity 390470 cash 473364 debt 688960 capex 3010 dividend 0 code73 1520687; FOI ready empty 70 / 73 vs 60-61 vs bruto / pers 0.97m / lev jump / othdebt jump / IOED relation,"
    f"{GAP},2026-08-19T11:40:00Z,{TS},"
    "tick1434 RL Zuid-Hageland VZW leftover IGS residual; KBO 0899.555.630; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1435 residual dual L5 VL"
)
spawn = (
    "rq_1435,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1434 done including RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Rivierenland 0899.152.980 JR2025 CDN 2026-00071020 LIVE leftover — STRONG next leftover RL; leftover RL Pajottenland en Zennevallei 0458.521.374 JR2025 CDN 2026-00101632 LIVE leftover; leftover RL Vlaamse Ardennen tot Dender 0449.013.097 JR2025 CDN 2026-00367158 LIVE leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1434 after RL Zuid-Hageland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Rivierenland/Pajottenland/Vlaamse Ardennen if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1434=done + rq_1435 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1434 RL Zuid-Hageland leftover IGS residual; KBO 0899.555.630; live JR2025 NBB WVV PDF; sourced euros assets 1079430 omzet empty diensten 1044796 pers 965261 pnl 31008 equity 390470 cash 473364 debt 688960 capex 3010 dividend 0 code73 1520687; FOI ready empty 70 / 73 vs 60-61 vs bruto / pers 0.97m / lev jump / othdebt jump / IOED relation; next rq_1435 residual dual L5 VL leftover RL Rivierenland/Pajottenland/Vlaamse Ardennen if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1434,1434,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1434")

# --- loop_log ---
entry = (
    "\n## Tick 1434 - 2026-08-19 - rq_1434 RL Zuid-Hageland dual residual leftover\n"
    "- Unit: Regionaal Landschap Zuid-Hageland VZW / RLZH (leftover IGS / regionaal landschap of 9 mined Zuid-Hageland cities; 1 VE) after residual dual hunt (KBO **0899.555.630**; official rlzh.be; live NBB WVV VKT-VZW deposit **2026-00075887** PDF 53572 bytes / 15p; AV **25.03.2026**; created **09.04.2026**; neerlegging **2026-04-10**; model **VKT-VZW** 25.0.9 m04-f; no commissaris named; VKT-VZW 6.2/6.3/6.5/6.6/6.8/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.4 + 6.7 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; 2025-12-31=0 / no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Tienen / AGB Landen / AGB Glabbeek / AGB Kortenaken) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381). Leftover IGS Regionaal Landschap Zuid-Hageland VZW statutory CDN live this tick (HTTP 200 / application/pdf / 53572 / 15p; SBM jaar **2025-12-31**; neerlegging 2026-04-10) — taken (hunt order #2 leftover unmined RL VZW of mined Zuid-Hageland cities with full WVV balans; STRONG next leftover RL after RLKM 1433). Distinct from already-mined RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Zorgbedrijf Rivierenland / AGB Tienen. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Zuid-Hageland / 0899.555.630 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **21.05.2008**; statutaire naam REGIONAAL LANDSCHAP ZUID-HAGELAND since 21.05.2008; VZW since 21.05.2008; zetel Schoolpad(Hak) 43 3300 Tienen since 18.03.2010; **1 VE**; KBO no tel/e-mail/web; official site https://www.rlzh.be/; e-mail info@rlzh.be; tel 016 81 52 77; dagelijks bestuur Kristien Justaert since 17.03.2022; NACE 91.420; Werkgever RSZ since 19.01.2009. WVV 2.1 voorzitter Provincie Vlaams-Brabant (Wijnants Marc); ondervoorzitter Natuurpunt Oost-Brabant (Abts Hugo). Official site 9 leden-gemeenten: Kortenaken / Geetbets / Zoutleeuw / Landen / Tienen / Hoegaarden / Linter / Boutersem / Glabbeek. IOED Zuid-Hageland mentioned on team page (info@ioedzuidhageland.be) — relation unpublished. Named share-% unpublished. Contact info@rlzh.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 filed 1520687**; **60/61 filed 1044796**; brutomarge 999242 != 73-60/61=475891 so other operating income unpublished; pers 62 filed **965261** / **11,2 VTE**): assets **1079430** (was 860212); fixed **5839** / IVA **592** / MVA **5247** (machines **2855**; meubilair **2392**) / FVA empty; current **1073592**; ST recv **596489** (trade **141153** / other **455336 JUMP** vs 280562); cash **473364 JUMP** vs 386494; prepaid **3739**; equity **390470** (bestemde fondsen **275944**; overgedragen **114527**); voorzieningen empty; schulden **688960 JUMP** vs 363867 (LT empty; ST **495867** waarvan leveranciers **190377 JUMP** vs 24 + tax **27980** + soc/bezold **127510** + overige **150000 JUMP** vs 10570; deferred **193093**); brutomarge **999242** vs 973478; omzet empty; 73 **1520687**; 60/61 **1044796**; pers **965261** / **11,2 VTE** / 17680 uur / YE **11,6**; afschr **2967**; andere bedrijfskosten **595**; expl **30420** vs −10804; fin opbr **897**; fin kosten **310**; tax empty; PnL **31008** vs −9502; dividend **0**; onttrekking EV **2709**; toevoeging bestemde **10336**; capex **3010**. Published 2024 passiva totaal 723329 vs 2024 activa 860212 (PDF inconsistency; 2025 balances).\n"
    "- CSVs: sources +4; entities +1 `vzw_rlzh` parent `sec_flanders`; budgets +51 executed; commitments +1 envelope 1520687 AV 25.03.2026; leaderboard +1 annual 1520687 / total 1079430; foi_queue +1 status=ready never sent; research_queue surgical rq_1434=done + rq_1435 spawn; loop_state ticks_completed=1434.\n"
    "- FOI: `gap_rlzh_omzet_empty_subs_1_52m_diensten_1_04m_l5` ready not sent — omzet 70 empty / 73 1.52m / diensten 1.04m / bruto != 73-60/61 / pers 0.97m 11.2 VTE deelwerking unpublished / other recv JUMP 0.46m / leveranciers JUMP 0.19m vs 24 / othdebt JUMP 0.15m / cash JUMP 0.47m / deferred 0.19m / vennoten share-pct / IOED relation / commissaris unpublished.\n"
    "- Next: rq_1435 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Rivierenland **0899.152.980** JR2025 CDN **2026-00071020** LIVE — STRONG next leftover RL. Leftover RL Pajottenland en Zennevallei **0458.521.374** JR2025 CDN **2026-00101632** LIVE leftover. Leftover RL Vlaamse Ardennen tot Dender **0449.013.097** JR2025 CDN **2026-00367158** LIVE leftover. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1434")
print("tick1434 writes done")
