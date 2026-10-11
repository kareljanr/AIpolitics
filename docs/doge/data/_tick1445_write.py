#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1445 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:20:00Z"
ENT = "vzw_rlkn"
SRC = "src_rlkn_jr2025_nbb"
GAP = "gap_rlkn_omzet_empty_pers_1_28m_cash_1_06m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlkn_jr2025_nbb,Regionaal Landschap Kleine en Grote Nete VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00054598.pdf,NBB / RL Kleine en Grote Nete VZW,2026-08-19,budget,tick1445; VKT-VZW 25.0.9 m04-f PDF 13p / 46632 bytes deposit 2026-00054598; AV 24.02.2026; header 11.03.2026; pdfinfo 16.03.2026; KBO 0810.764.897; assets 1476658 cash 1064409 DROP debt 755359 brutomarge 1298726 omzet empty code73 empty code60_61 empty pers 1278558 pnl -11228; no commissaris listed",
    "src_rlkn_site,Regionaal Landschap Kleine en Grote Nete official site,https://www.rlkgn.be/,RL Kleine en Grote Nete VZW,2026-08-19,official_register,tick1445; leftover IGS / regionaal landschap of 26 Kempen-Nete cities; zetel Polderstraat 33 2360 Oud-Turnhout; contact info@rlkgn.be; tel 014 25 56 21; coordinator Bas Van der Veken; 26 gemeenten + provincie Antwerpen",
    "src_kbo_rlkn_0810764897,KBO Regionaal Landschap Kleine en Grote Nete 0810.764.897,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0810764897,KBO Public Search FOD Economie,2026-08-19,official_register,tick1445; Actief since 10.03.2009; naam since 10.03.2009; afkorting RLKGN since 10.03.2009; zetel Polderstraat 33 2360 Oud-Turnhout since 23.02.2021; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 01.04.2009; aanbestedende overheid since 18.01.2003; 66 functiehouders; dagelijks bestuur Van der Veken Sebastiaan since 30.03.2009",
    "src_rlkn_foi_contact,RL Kleine en Grote Nete FOI channel (info@rlkgn.be; Polderstraat 33 Oud-Turnhout),https://www.rlkgn.be/over-ons/team,RL Kleine en Grote Nete VZW,2026-08-19,official_register,tick1445; 26 member cities + provincie Antwerpen; voorzitter De Haes Jan; coordinator Bas Van der Veken; NOT IOK / BIONERGA / Erfgoed Noorderkempen",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlkn," in raw or raw.startswith(b"vzw_rlkn,"):
    raise SystemExit("vzw_rlkn already present")
if b"0810.764.897" in raw or b"0810764897" in raw:
    raise SystemExit("RL Kleine en Grote Nete KBO already present")
row = (
    "vzw_rlkn,Regionaal Landschap Kleine en Grote Nete VZW (leftover IGS / regionaal landschap of 26 mined Kempen-Nete cities; NOT IOK / BIONERGA / Erfgoed Noorderkempen),"
    "Regionaal Landschap Kleine et Grote Nete ASBL (IGS residuel / paysage regional Kempen-Nete),"
    "Regionaal Landschap Kleine en Grote Nete leftover IGS / regional landscape VZW of 26 Kempen-Nete municipalities (not IOK / BIONERGA / Erfgoed Noorderkempen),"
    "other,sec_flanders,nl,https://www.rlkgn.be/,info@rlkgn.be,Polderstraat 33 2360 Oud-Turnhout,"
    "tick1445 leftover residual IGS VZW of mined Kempen-Nete cities after leftover AGB hunt; KBO 0810.764.897 Actief since 10.03.2009; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1476658 omzet empty diensten empty pers 1278558 pnl -11228 equity 721299 cash 1064409 debt 755359 capex 0 dividend 0 brutomarge 1298726; FOI ready omzet empty / 73 empty / 60-61 empty / pers 1.28m / cash DROP / trade DROP / deferred DROP / lev JUMP; distinct from already-mined IOK / IOK Afvalbeheer / IOK DV / BIONERGA / IVAREM / AGB Sport Geel / AGB Beerse / Erfgoed Noorderkempen 1426 / RL Lage Kempen 1430 / RLKM 1433 / RLHV 1444 / RLML 1443 / RLBK 1442 / RLDV 1441"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlkn")

# --- budgets ---
BUDGETS = [
    ("bud_rlkn_assets_2025", "2025", "1476658", "2025 assets 1476658 VKT-VZW 20/58; tick1445; primary official NBB WVV"),
    ("bud_rlkn_assets_2024", "2024", "1760387", "2024 assets 1760387 comparative; tick1445; primary official NBB WVV 20/58"),
    ("bud_rlkn_fixed_2025", "2025", "252136", "2025 vaste activa 252136 vs 284089; tick1445; primary official NBB WVV 21/28"),
    ("bud_rlkn_fixed_2024", "2024", "284089", "2024 vaste activa 284089 comparative; tick1445; primary official NBB WVV 21/28"),
    ("bud_rlkn_iva_2025", "2025", "0", "2025 IVA empty (6.1.1 not filed); tick1445; primary official NBB WVV 21"),
    ("bud_rlkn_mva_2025", "2025", "252136", "2025 MVA 252136 vs 284089 (terreinen/gebouwen 228948; meubilair 23188); tick1445; primary official NBB WVV 22/27"),
    ("bud_rlkn_mva_2024", "2024", "284089", "2024 MVA 284089 comparative; tick1445; primary official NBB WVV 22/27"),
    ("bud_rlkn_buildings_2025", "2025", "228948", "2025 terreinen en gebouwen 228948 vs 238395; tick1445; primary official NBB WVV 22"),
    ("bud_rlkn_furniture_2025", "2025", "23188", "2025 meubilair en rollend materieel 23188 vs 45694; tick1445; primary official NBB WVV 24"),
    ("bud_rlkn_fva_2025", "2025", "0", "2025 FVA empty (6.1.3 not filed); tick1445; primary official NBB WVV 28"),
    ("bud_rlkn_current_2025", "2025", "1224522", "2025 vlottend 1224522 vs 1476299; tick1445; primary official NBB WVV 29/58"),
    ("bud_rlkn_current_2024", "2024", "1476299", "2024 vlottend 1476299 comparative; tick1445; primary official NBB WVV 29/58"),
    ("bud_rlkn_strecv_2025", "2025", "160113", "2025 ST vorderingen 160113 vs 319664; tick1445; primary official NBB WVV 40/41"),
    ("bud_rlkn_strecv_2024", "2024", "319664", "2024 ST vorderingen 319664 comparative; tick1445; primary official NBB WVV 40/41"),
    ("bud_rlkn_trade_2025", "2025", "120357", "2025 handelsvorderingen 120357 DROP vs 214087; tick1445; primary official NBB WVV 40"),
    ("bud_rlkn_trade_2024", "2024", "214087", "2024 handelsvorderingen 214087 comparative; tick1445; primary official NBB WVV 40"),
    ("bud_rlkn_othrecv_2025", "2025", "39755", "2025 overige vorderingen 39755 DROP vs 105577; tick1445; primary official NBB WVV 41"),
    ("bud_rlkn_othrecv_2024", "2024", "105577", "2024 overige vorderingen 105577 comparative; tick1445; primary official NBB WVV 41"),
    ("bud_rlkn_cash_2025", "2025", "1064409", "2025 liquide middelen 1064409 DROP vs 1156635; tick1445; primary official NBB WVV 54/58"),
    ("bud_rlkn_cash_2024", "2024", "1156635", "2024 liquide middelen 1156635 comparative; tick1445; primary official NBB WVV 54/58"),
    ("bud_rlkn_prepaid_2025", "2025", "0", "2025 prepaid empty; tick1445; primary official NBB WVV 490/1"),
    ("bud_rlkn_equity_2025", "2025", "721299", "2025 EV 721299 vs 732527; tick1445; primary official NBB WVV 10/15"),
    ("bud_rlkn_equity_2024", "2024", "732527", "2024 EV 732527 comparative; tick1445; primary official NBB WVV 10/15"),
    ("bud_rlkn_bestemde_2025", "2025", "721299", "2025 bestemde fondsen 721299 vs 732527; tick1445; primary official NBB WVV 13"),
    ("bud_rlkn_bestemde_2024", "2024", "732527", "2024 bestemde fondsen 732527 comparative; tick1445; primary official NBB WVV 13"),
    ("bud_rlkn_debt_2025", "2025", "755359", "2025 schulden 755359 DROP vs 1027860 (LT empty); tick1445; primary official NBB WVV 17/49"),
    ("bud_rlkn_debt_2024", "2024", "1027860", "2024 schulden 1027860 comparative; tick1445; primary official NBB WVV 17/49"),
    ("bud_rlkn_stdebt_2025", "2025", "172909", "2025 ST schulden 172909 vs 152080; tick1445; primary official NBB WVV 42/48"),
    ("bud_rlkn_stdebt_2024", "2024", "152080", "2024 ST schulden 152080 comparative; tick1445; primary official NBB WVV 42/48"),
    ("bud_rlkn_lev_2025", "2025", "45939", "2025 leveranciers 45939 JUMP vs 27119; tick1445; primary official NBB WVV 440/4"),
    ("bud_rlkn_lev_2024", "2024", "27119", "2024 leveranciers 27119 comparative; tick1445; primary official NBB WVV 440/4"),
    ("bud_rlkn_bezold_2025", "2025", "126970", "2025 bezoldigingen/sociale lasten 126970 vs 124960; tick1445; primary official NBB WVV 454/9"),
    ("bud_rlkn_deferred_2025", "2025", "582449", "2025 deferred 582449 DROP vs 875780; tick1445; primary official NBB WVV 492/3"),
    ("bud_rlkn_deferred_2024", "2024", "875780", "2024 deferred 875780 comparative; tick1445; primary official NBB WVV 492/3"),
    ("bud_rlkn_brutomarge_2025", "2025", "1298726", "2025 brutomarge 1298726 vs 1281719; omzet 70 empty; 73 empty; 60/61 empty; tick1445; primary official NBB WVV 9900"),
    ("bud_rlkn_brutomarge_2024", "2024", "1281719", "2024 brutomarge 1281719 comparative; tick1445; primary official NBB WVV 9900"),
    ("bud_rlkn_pers_2025", "2025", "1278558", "2025 pers 1278558 / 15.5 VTE vs 1242100 / 16.2; tick1445; primary official NBB WVV 62"),
    ("bud_rlkn_pers_2024", "2024", "1242100", "2024 pers 1242100 / 16.2 VTE comparative; tick1445; primary official NBB WVV 62"),
    ("bud_rlkn_afschr_2025", "2025", "31952", "2025 afschrijvingen 31952 vs 32924; tick1445; primary official NBB WVV 630"),
    ("bud_rlkn_andere_2025", "2025", "998", "2025 andere bedrijfskosten 998 vs 1019; tick1445; primary official NBB WVV 640/8"),
    ("bud_rlkn_nietrec_kost_2025", "2025", "5992", "2025 niet-recurrente bedrijfskosten 5992 vs 3898; tick1445; primary official NBB WVV 66A"),
    ("bud_rlkn_expl_2025", "2025", "-18774", "2025 expl -18774 vs +1778; tick1445; primary official NBB WVV 9901"),
    ("bud_rlkn_expl_2024", "2024", "1778", "2024 expl +1778 comparative; tick1445; primary official NBB WVV 9901"),
    ("bud_rlkn_finopbr_2025", "2025", "9372", "2025 fin opbr 9372 (recurrent 5473; niet-recurrent 76B 3898); tick1445; primary official NBB WVV 75/76B"),
    ("bud_rlkn_finkost_2025", "2025", "184", "2025 fin kosten 184 vs 176; tick1445; primary official NBB WVV 65/66B"),
    ("bud_rlkn_tax_2025", "2025", "1642", "2025 belastingen 1642 vs 488; tick1445; primary official NBB WVV 67/77"),
    ("bud_rlkn_pnl_2025", "2025", "-11228", "2025 PnL -11228 vs +3380; tick1445; primary official NBB WVV 9904"),
    ("bud_rlkn_pnl_2024", "2024", "3380", "2024 PnL +3380 comparative; tick1445; primary official NBB WVV 9904"),
    ("bud_rlkn_onttrekking_2025", "2025", "11228", "2025 onttrekking EV 11228; tick1445; primary official NBB WVV 791"),
    ("bud_rlkn_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1445; primary official NBB WVV"),
    ("bud_rlkn_capex_2025", "2025", "0", "2025 MVA aanschaffingen empty; FVA/IVA empty; overdrachten 2608; tick1445; primary official NBB WVV 8169"),
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
    f"comm_rlkn_jr2025_bruto,Regionaal Landschap Kleine en Grote Nete VZW JR2025 leftover IGS dual (brutomarge 1.30m / pers 1.28m / cash DROP 1.06m),{ENT},RL Kleine en Grote Nete VZW / 26 Kempen-Nete cities,WVV VZW; NBB neerlegging; 26 Kempen-Nete gemeenten + provincie Antwerpen,2026-02-24,2009,,1298726,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00054598.pdf,Local leftover IGS map VL Kempen-Nete landschap — 1.30m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 1.28m,Publish empty 70/73/60-61 split + pers 1.28m + cash DROP + trade DROP + deferred DROP + vennoten share-pct; do not keep leftover RLKGN VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Kempen>RLKGN>JR2025_L5,tick1445; assets 1476658 omzet empty diensten empty pers 1278558 pnl -11228 equity 721299 cash 1064409 debt 755359 capex 0 dividend 0 brutomarge 1298726; FOI ready not sent; not TE-additive of 348bn; NOT IOK / BIONERGA / Erfgoed Noorderkempen",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlkn_omzet_empty_pers_1_28m_cash_1_06m,Regionaal Landschap Kleine en Grote Nete VZW JR2025 leftover IGS: empty omzet 70 / pers 1.28m / cash DROP 1.06m / brutomarge 1.30m,L5,local_budget_line,Vlaanderen>Antwerpen>Kempen>RLKGN>JR2025_L5,1298726,1476658,Leftover dual IGS VZW: assets 1.48m / equity 0.72m / pnl -0.01m / omzet empty / 73 empty / 60-61 empty / pers 1.28m 15.5 VTE / cash 1.06m DROP / debt 0.76m DROP / lev 0.05m JUMP / destin 0.72m / dividend 0,strong,{SRC},RL Kleine en Grote Nete VZW / 26 Kempen-Nete cities,Local leftover IGS map VL Kempen-Nete landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 1.30m / pers 1.28m / cash DROP 1.06m / PnL -0.01m,6.5,6.3,2.2,6.1,Publish empty 70/73/60-61 split + pers 1.28m + cash DROP + trade DROP + deferred DROP + vennoten share-pct; do not keep leftover RLKGN VZW as dual unpublished vehicle,active,,tick1445; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IOK / BIONERGA / Erfgoed Noorderkempen 1426 / RLHV 1444 / RLML 1443 / RLBK 1442 / RLDV 1441",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Kempen>RLKGN>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 1298726 + pers 62 1278558 / 15.5 VTE + cash DROP 1064409 vs 1156635 + trade DROP 120357 vs 214087 + other recv DROP 39755 vs 105577 + leveranciers JUMP 45939 vs 27119 + debt DROP 755359 vs 1027860 + deferred DROP 582449 vs 875780 + assets DROP 1476658 vs 1760387 + expl -18774 + pnl -11228 + onttrekking EV 11228 + capex 0 + commissaris unpublished + vennoten share-pct unpublished + 1 VE unpublished + relation to IOK / leftover IOED Land van Nete en Aa / leftover IOED Stuifzand unpublished,Leftover RLKGN VZW after leftover AGB hunt: 1.30m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Kleine en Grote Nete vzw / Bestuursorgaan,info@rlkgn.be,Polderstraat 33 2360 Oud-Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlkn_jr2025_bruto,lb_rlkn_omzet_empty_pers_1_28m_cash_1_06m,{TS},{TS},tick1445 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (46632 bytes 13p deposit 2026-00054598). FOI ready not sent. NOT IOK / BIONERGA / Erfgoed Noorderkempen. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong/Oost-Haspengouw still no JR2025. Leftover RL Houtland still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 unmined leftover for next if a 2025 CDN is live.",
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
if not last_s.startswith("rq_1445,"):
    raise SystemExit(f"expected last row rq_1445, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1445 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1445,RL Kleine en Grote Nete JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlkn,"
    "Completed: Regionaal Landschap Kleine en Grote Nete VZW leftover IGS / regionaal landschap of 26 mined Kempen-Nete cities after leftover AGB hunt; KBO 0810.764.897 Actief; live JR2025 official NBB WVV VKT-VZW PDF (46632 bytes 13p deposit 2026-00054598; AV 24.02.2026; header 11.03.2026; created 16.03.2026; no commissaris listed); sourced euros assets 1476658 omzet empty diensten empty pers 1278558 pnl -11228 equity 721299 cash 1064409 debt 755359 capex 0 dividend 0 brutomarge 1298726; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash DROP / trade DROP / deferred DROP / lev JUMP; NOT IOK / BIONERGA / Erfgoed Noorderkempen,"
    f"{GAP},2026-08-19T13:05:00Z,{TS},"
    "tick1445 RL Kleine en Grote Nete VZW leftover IGS residual; KBO 0810.764.897; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1446 residual dual L5 VL leftover RL West-Vlaamse Hart if 2025 CDN live else leftover AGB/IOED/cultuur-IGS/Houtland"
)
spawn = (
    "rq_1446,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1445 done including RL Kleine en Grote Nete 1445 leftover IGS live NBB WVV / RL Haspengouw 1444 leftover IGS live NBB WVV / RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL West-Vlaamse Hart 0800.422.125 unmined leftover — take if a JR2025 CDN now downloads (STRONG next leftover RL after named leftover RL list exhausted except Houtland); leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1445 after RL Kleine en Grote Nete leftover IGS live NBB WVV; next residual dual L5 VL leftover RL West-Vlaamse Hart if a 2025 CDN is now live else leftover AGB/IOED/cultuur-IGS/Houtland"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1445=done + rq_1446 spawned; keep", last_line_start)

# --- inventory counts from CSVs (after writes) ---
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

# --- loop_state ---
notes = (
    f"tick1445 RL Kleine en Grote Nete leftover IGS residual; KBO 0810.764.897; live JR2025 NBB WVV PDF; sourced euros assets 1476658 omzet empty diensten empty pers 1278558 pnl -11228 equity 721299 cash 1064409 debt 755359 capex 0 dividend 0 brutomarge 1298726; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash DROP / trade DROP / deferred DROP / lev JUMP; NOT IOK / BIONERGA / Erfgoed Noorderkempen; next rq_1446 residual dual L5 VL leftover RL West-Vlaamse Hart if 2025 CDN live else leftover AGB/IOED/cultuur-IGS/Houtland; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1445,1445,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1445")

# --- loop_log ---
entry = (
    "\n## Tick 1445 - 2026-08-19 - rq_1445 RL Kleine en Grote Nete dual residual leftover\n"
    "- Unit: Regionaal Landschap Kleine en Grote Nete VZW / RLKGN (leftover IGS / regionaal landschap of 26 mined Kempen-Nete cities; 1 VE) after residual dual hunt (KBO **0810.764.897**; official rlkgn.be; live NBB WVV VKT-VZW deposit **2026-00054598** PDF 46632 bytes / 13p; AV **24.02.2026**; header **11.03.2026**; pdfinfo created **16.03.2026**; model **VKT-VZW** 25.0.9 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.3/6.2/6.3/6.5/6.6/7/8 not filed; 6.1.2 MVA + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; last known 1444: 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Turnhout / AGB Westerlo / AGB Sport en Recreatie Herentals / AGB Herentals patrimonium / AGB Arendonk / AGB Sportcentrum t Hofeind Merksplas / AGB Sport Geel / AGB Cultuur Geel / AGB Vosselaar / AGB Lille liquidation / AGB Herselt / AGB Oud-Turnhout / AGB Beerse) — skipped. Baarle-Hertog / Balen / Dessel / Grobbendonk / Herenthout / Kasterlee / Laakdal / Meerhout / Mol / Olen / Ravels / Retie / Rijkevorsel / Vorselaar have no AGB in entities. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover IGS Regionaal Landschap Kleine en Grote Nete VZW statutory CDN live this tick (HTTP 200 / application/pdf / 46632 / 13p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined RL VZW of mined Kempen-Nete cities with full WVV balans; STRONG next leftover RL after RL Haspengouw 1444). Distinct from already-mined **IOK / IOK Afvalbeheer / IOK DV / BIONERGA / IVAREM / AGB Sport Geel / AGB Beerse / Erfgoed Noorderkempen** (igs_enpk tick 1426) / RL Lage Kempen 1430 / RLKM 1433 / RLHV 1444 / RLML 1443 / RLBK 1442 / RLDV 1441 / RLD 1440. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Kleine en Grote Nete / 0810.764.897 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **10.03.2009**; statutaire naam Regionaal Landschap Kleine en Grote Nete since 10.03.2009; afkorting RLKGN since 10.03.2009; VZW since 10.03.2009; zetel Polderstraat 33 2360 Oud-Turnhout since 23.02.2021; **1 VE**; official site https://www.rlkgn.be/; contact info@rlkgn.be; tel 014 25 56 21; coordinator Bas Van der Veken; NACE RSZ 91.420; Werkgever RSZ since 01.04.2009; aanbestedende overheid since 18.01.2003; **66 functiehouders**. WVV 2.1 voorzitter De Haes Jan; penningmeester Gysels Jos. Dagelijks bestuur Van der Veken Sebastiaan since 30.03.2009. Official site 26 leden-gemeenten: Arendonk / Baarle-Hertog / Balen / Beerse / Dessel / Geel / Grobbendonk / Herentals / Herenthout / Herselt / Hulshout / Kasterlee / Laakdal / Lille / Meerhout / Merksplas / Mol / Olen / Oud-Turnhout / Ravels / Retie / Rijkevorsel / Turnhout / Vorselaar / Vosselaar / Westerlo. Plus provincie Antwerpen + Vlaamse Overheid. Named share-% unpublished. Team page staffs leftover IOED Land van Nete en Aa / leftover IOED Stuifzand — relation unpublished. Contact info@rlkgn.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor HTML blocked this tick (IP blacklist) — PDF wins. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **1278558** / **15,5 VTE** vs 1242100 / 16,2): assets **1476658** (was 1760387 DROP); fixed **252136** vs 284089 / IVA empty / MVA **252136** vs 284089 (terreinen/gebouwen **228948**; meubilair **23188**) / FVA empty; current **1224522** vs 1476299; ST recv **160113** vs 319664 (trade **120357 DROP** vs 214087 / other **39755 DROP** vs 105577); geldbeleg empty; cash **1064409 DROP** vs 1156635; prepaid empty; equity **721299** (bestemde fondsen **721299** vs 732527); voorzieningen empty; schulden **755359 DROP** vs 1027860 (LT empty; ST **172909** vs 152080 waarvan leveranciers **45939 JUMP** vs 27119 + soc/bezold **126970** vs 124960; deferred **582449 DROP** vs 875780); brutomarge **1298726** vs 1281719; omzet empty; 73 empty; 60/61 empty; pers **1278558** / **15,5 VTE** / 20896 uur / YE **15,5**; afschr **31952**; andere **998**; niet-recurrente kosten 66A **5992**; expl **−18774** vs +1778; fin opbr **9372** (recurrent **5473**; niet-recurrent 76B **3898**); fin kosten **184**; tax **1642**; PnL **−11228** vs +3380; dividend **0**; onttrekking EV **11228**; capex **0**. PDF 1-euro rounding: trade+other 160112 vs published ST recv 160113. Sociale balans 2024 pers 1242490 vs PnL 62 1242100.\n"
    f"- CSVs: sources +4; entities +1 `vzw_rlkn` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 1298726 AV 24.02.2026; leaderboard +1 annual 1298726 / total 1476658; foi_queue +1 status=ready never sent; research_queue surgical rq_1445=done + rq_1446 spawn; loop_state ticks_completed=1445. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_rlkn_omzet_empty_pers_1_28m_cash_1_06m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 1.28m 15.5 VTE deelwerking unpublished / cash DROP 1.06m / trade DROP 0.12m / other recv DROP 0.04m / deferred DROP 0.58m / debt DROP 0.76m / lev JUMP 0.05m / destin 0.72m / capex 0 / commissaris unpublished / vennoten share-pct / relation to IOK / leftover IOED Land van Nete en Aa / leftover IOED Stuifzand unpublished / 1 VE unpublished.\n"
    "- Next: rq_1446 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Named leftover RL list from 1444 now exhausted except leftover RL Houtland & Polders **0472.947.254** still JR2024 — take only if JR2025 now live. Leftover RL West-Vlaamse Hart **0800.422.125** unmined leftover — take if a JR2025 CDN now downloads (STRONG next leftover RL). Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1445 -" in lraw:
    raise SystemExit("loop_log already has tick 1445 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1445")
print("DONE tick 1445")
