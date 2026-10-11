#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1449 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:25:00Z"
ENT = "vzw_bgzk"
SRC = "src_bgzk_jr2025_nbb"
GAP = "gap_bgzk_omzet_empty_bruto_0_21m_geldbeleg_0_71m_l5"
LB = "lb_bgzk_omzet_empty_bruto_0_21m_geldbeleg_0_71m"
COMM = "comm_bgzk_jr2025_bruto"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_bgzk_jr2025_nbb,Bosgroep Zuiderkempen VZW official NBB WVV VKT-VZW JR2025,http://cdn.staatsbladmonitor.be/2026pdf/2026-00104376.pdf,NBB Central Balance Sheet Office,2026-08-19,budget,tick1449; official NBB WVV VKT-VZW deposit 2026-00104376 PDF 11p / 40515 bytes; pdfinfo created 07.05.2026; header 05.05.2026; AV 21.04.2026; KBO 0860.780.968; assets 863760 cash 89632 debt 193180 bruto 206947 omzet empty 73 empty 60/61 empty pers empty pnl 191700 equity 670580 geldbeleg 705990",
    "src_bgzk_site,Bosgroep Zuiderkempen official site,https://bosgroepen.be/zuiderkempen/,Bosgroep Zuiderkempen VZW,2026-08-19,official_register,tick1449; leftover IGS / Bosgroep of mined Zuiderkempen cities; zetel Britselaan 20C 2260 Westerlo; contact zuiderkempen@bosgroep.be; tel 014 27 96 57",
    "src_kbo_bgzk_0860780968,KBO Bosgroep Zuiderkempen 0860.780.968,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860780968,KBO Public Search FOD Economie,2026-08-19,official_register,tick1449; Actief since 30.09.2003; naam BOSGROEP ZUIDERKEMPEN since 30.09.2003; zetel Britselaan 20C 2260 Westerlo since 30.09.2003; 0 VE; VZW; NACE 02.100; btw since 01.03.2007; 20 functiehouders",
    "src_bgzk_foi_contact,Bosgroep Zuiderkempen FOI channel (zuiderkempen@bosgroep.be; Britselaan 20C Westerlo),https://bosgroepen.be/zuiderkempen/,Bosgroep Zuiderkempen VZW,2026-08-19,official_register,tick1449; Zuiderkempen leftover Bosgroep + provincie Antwerpen; NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_bgzk," in raw or raw.startswith(b"vzw_bgzk,"):
    raise SystemExit("vzw_bgzk already present")
if b"0860.780.968" in raw or b"0860780968" in raw:
    raise SystemExit("Bosgroep Zuiderkempen KBO already present")
row = (
    "vzw_bgzk,Bosgroep Zuiderkempen VZW (leftover IGS / Bosgroep of mined Zuiderkempen cities; NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen),"
    "Bosgroep Zuiderkempen ASBL (IGS residuel / groupe forestier Campine du Sud),"
    "Bosgroep Zuiderkempen leftover IGS / forest-group VZW of mined Zuiderkempen municipalities (not BGAG / BVB / BGOV / RLKGN / RLHV / Erfgoed Voorkempen),"
    "other,sec_flanders,nl,https://bosgroepen.be/zuiderkempen/,zuiderkempen@bosgroep.be,Britselaan 20C 2260 Westerlo,"
    "tick1449 leftover residual IGS/Bosgroep VZW of mined Zuiderkempen cities after leftover AGB hunt; KBO 0860.780.968 Actief since 30.09.2003; live JR2025 NBB WVV PDF downloads; sourced euros assets 863760 omzet empty diensten empty pers empty pnl 191700 equity 670580 cash 89632 debt 193180 capex 2579 dividend 0 bruto 206947 geldbeleg 705990; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / geldbeleg JUMP / cash DROP / 0 VE / leden share-pct; distinct from already-mined BGAG 1448 / BVB 1447 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RL de Voorkempen 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_bgzk")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_bgzk_assets_2025", "2025", "863760", "2025 assets 863760 (was 728166); tick1449; primary official NBB WVV"),
    ("bud_bgzk_fixed_2025", "2025", "20844", "2025 vaste activa 20844 (was 18265); tick1449; primary official NBB WVV"),
    ("bud_bgzk_iva_2025", "2025", "0", "2025 IVA empty; 6.1.1 not filed; tick1449; primary official NBB WVV"),
    ("bud_bgzk_mva_2025", "2025", "20844", "2025 MVA 20844 terreinen (was 18265); tick1449; primary official NBB WVV"),
    ("bud_bgzk_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1449; primary official NBB WVV"),
    ("bud_bgzk_current_2025", "2025", "842916", "2025 vlottend 842916 (was 709901); tick1449; primary official NBB WVV"),
    ("bud_bgzk_strecv_2025", "2025", "44956", "2025 ST vorderingen 44956 (was 42308); tick1449; primary official NBB WVV"),
    ("bud_bgzk_trade_2025", "2025", "21404", "2025 handelsvorderingen 21404 (was 27659); tick1449; primary official NBB WVV"),
    ("bud_bgzk_othrecv_2025", "2025", "23552", "2025 overige vorderingen 23552 (was 14649); tick1449; primary official NBB WVV"),
    ("bud_bgzk_geldbeleg_2025", "2025", "705990", "2025 geldbeleggingen 705990 JUMP (was 530940); tick1449; primary official NBB WVV"),
    ("bud_bgzk_cash_2025", "2025", "89632", "2025 liquide middelen 89632 DROP (was 129520); tick1449; primary official NBB WVV"),
    ("bud_bgzk_prepaid_2025", "2025", "2338", "2025 prepaid 2338 (was 7133); tick1449; primary official NBB WVV"),
    ("bud_bgzk_equity_2025", "2025", "670580", "2025 EV 670580 (was 476301); tick1449; primary official NBB WVV"),
    ("bud_bgzk_fondsen_2025", "2025", "2579", "2025 fondsen 10 2579 (was empty); tick1449; primary official NBB WVV"),
    ("bud_bgzk_bestemde_2025", "2025", "668001", "2025 bestemde fondsen 668001 (was 476301); tick1449; primary official NBB WVV"),
    ("bud_bgzk_overgedragen_2025", "2025", "0", "2025 overgedragen 0; tick1449; primary official NBB WVV"),
    ("bud_bgzk_debt_2025", "2025", "193180", "2025 schulden 193180 DROP (was 251865; LT empty); tick1449; primary official NBB WVV"),
    ("bud_bgzk_stdebt_2025", "2025", "148909", "2025 ST schulden 148909 (was 157790); tick1449; primary official NBB WVV"),
    ("bud_bgzk_lev_2025", "2025", "110412", "2025 leveranciers 110412 (was 117407); tick1449; primary official NBB WVV"),
    ("bud_bgzk_tax_2025", "2025", "3659", "2025 belastingen 450/3 3659 (bezold empty; was 280); tick1449; primary official NBB WVV"),
    ("bud_bgzk_othdebt_2025", "2025", "34838", "2025 overige schulden 34838 (was 40103); tick1449; primary official NBB WVV"),
    ("bud_bgzk_deferred_2025", "2025", "44271", "2025 deferred 44271 DROP (was 94075); tick1449; primary official NBB WVV"),
    ("bud_bgzk_bruto_2025", "2025", "206947", "2025 brutomarge 9900 206947 (was 49729); tick1449; primary official NBB WVV"),
    ("bud_bgzk_andere_2025", "2025", "4930", "2025 andere bedrijfskosten 640/8 4930 (was 2142); tick1449; primary official NBB WVV"),
    ("bud_bgzk_expl_2025", "2025", "202017", "2025 expl 202017 (was 47587); tick1449; primary official NBB WVV"),
    ("bud_bgzk_finopbr_2025", "2025", "9749", "2025 fin opbr 9749 (rec 4433 + nrec 5316; was 4236); tick1449; primary official NBB WVV"),
    ("bud_bgzk_finkost_2025", "2025", "20066", "2025 fin kosten 20066 (rec 46 + nrec 20020; was 75); tick1449; primary official NBB WVV"),
    ("bud_bgzk_pnl_2025", "2025", "191700", "2025 PnL 191700 (was 51748); tick1449; primary official NBB WVV"),
    ("bud_bgzk_div_2025", "2025", "0", "2025 dividend 0; tick1449; primary official NBB WVV"),
    ("bud_bgzk_pers_2025", "2025", "0", "2025 pers 62 empty / 9087 empty / no VTE; 6.7 not filed; tick1449; primary official NBB WVV"),
    ("bud_bgzk_capex_2025", "2025", "2579", "2025 capex MVA aanschaf 8169 2579; IVA/FVA empty; tick1449; primary official NBB WVV"),
    ("bud_bgzk_onttrekking_2025", "2025", "7138", "2025 onttrekking bestemde 791 7138; tick1449; primary official NBB WVV"),
    ("bud_bgzk_toevoeging_2025", "2025", "198838", "2025 toevoeging bestemde 691 198838; tick1449; primary official NBB WVV"),
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
    f"{COMM},Bosgroep Zuiderkempen VZW JR2025 leftover IGS dual (bruto 0.21m / empty 70-73-60/61 / geldbeleg 0.71m),{ENT},Bosgroep Zuiderkempen VZW / mined Zuiderkempen cities,WVV VZW; official NBB VKT-VZW; provincie Antwerpen,2026-04-21,2003,,206947,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00104376.pdf,Local leftover IGS map VL Bosgroep Zuiderkempen — bruto 0.21m / empty omzet / geldbeleg 0.71m,Publish empty 70/73/60-61/pers + geldbeleg JUMP + cash DROP + 0 VE + vennoten share-pct; do not keep leftover BGZK VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>BosgroepZK>JR2025_L5,tick1449; assets 863760 omzet empty diensten empty pers empty pnl 191700 equity 670580 cash 89632 debt 193180 capex 2579 dividend 0 bruto 206947 geldbeleg 705990; FOI ready not sent; not TE-additive of 348bn; NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},Bosgroep Zuiderkempen VZW JR2025 leftover IGS: empty 70/73/60-61 / bruto 0.21m / geldbeleg 0.71m / cash DROP,L5,local_budget_line,Vlaanderen>Antwerpen>BosgroepZK>JR2025_L5,206947,863760,Leftover dual IGS/Bosgroep VZW: assets 0.86m / equity 0.67m / pnl +192k / omzet empty / 73 empty / 60-61 empty / pers empty no VTE / geldbeleg 0.71m JUMP / cash 0.09m DROP / debt 0.19m / dividend 0 / NBB 2026-00104376,strong,{SRC},Bosgroep Zuiderkempen VZW / mined Zuiderkempen cities,Local leftover IGS map VL Bosgroep Zuiderkempen — JR2025 NBB WVV live; empty 70/73/60-61 FOI,Official NBB WVV 2026-08-19: bruto 0.21m / empty omzet / geldbeleg 0.71m / PnL +192k,6.5,5.8,2.5,6.1,Publish empty 70/73/60-61/pers + geldbeleg JUMP + cash DROP + 0 VE + vennoten share-pct; do not keep leftover BGZK VZW as dual unpublished vehicle,active,,tick1449; leftover IGS/Bosgroep after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined BGAG 1448 / BVB 1447 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RL de Voorkempen 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>BosgroepZK>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 206947 + pers 62 empty no VTE + 0 VE + geldbeleg 705990 JUMP vs 530940 + cash 89632 DROP vs 129520 + deferred DROP 44271 vs 94075 + debt DROP 193180 vs 251865 + nrec fin kost 20020 + restated PY + capex 2579 + vennoten share-pct unpublished + relation to BGAG/BVB/BGOV/Kempen Noord/Koepel/RLKGN/provincie unpublished,Leftover BGZK VZW after leftover AGB hunt: bruto 0.21m / empty omzet 70 hides public-perimeter bosgroep vehicle,8,Bosgroep Zuiderkempen vzw / Bestuursorgaan,zuiderkempen@bosgroep.be,Britselaan 20C 2260 Westerlo,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1449 leftover IGS/Bosgroep after honest leftover AGB hunt; live JR2025 NBB WVV PDF now extracted (40515 bytes 11p). FOI ready not sent. NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen. Leftover Bosgroep Kempen Noord 0476.530.217 SBM last JR 2025-12-31 CDN 2026-00086307 HEAD HTTP 200 this tick (euros forbidden; take after 1450 every-10). Leftover WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Koepel 0820.176.768 SBM no jaarrekening this tick. Leftover Limburg 0668.619.317 SBM IP-blacklist this tick. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong/Oost-Haspengouw still no JR2025. Leftover RL Houtland still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening.",
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
if not last_s.startswith("rq_1449,"):
    raise SystemExit(f"expected last row rq_1449, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1449 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1449,Bosgroep Zuiderkempen JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_bgzk,"
    "Completed: Bosgroep Zuiderkempen VZW leftover IGS / Bosgroep of mined Zuiderkempen cities after leftover AGB hunt; KBO 0860.780.968 Actief; live JR2025 official NBB WVV VKT-VZW PDF (40515 bytes 11p deposit 2026-00104376; AV 21.04.2026; header 05.05.2026; created 07.05.2026; no commissaris listed); sourced euros assets 863760 omzet empty diensten empty pers empty pnl 191700 equity 670580 cash 89632 debt 193180 capex 2579 dividend 0 bruto 206947 geldbeleg 705990; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / geldbeleg JUMP / cash DROP / 0 VE / leden share-pct; NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen,"
    f"{GAP},2026-08-19T13:20:00Z,{TS},"
    "tick1449 Bosgroep Zuiderkempen leftover IGS/Bosgroep residual; KBO 0860.780.968; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1450 MUST do every-10 then leftover Bosgroep Kempen Noord if CDN 2026-00086307 still live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen"
)
spawn = (
    "rq_1450,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "EVERY-10 MANDATORY this tick: refresh progress_every_10_ticks.md + doge_waste_top10_current.md then residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1449 done including Bosgroep Zuiderkempen 1449 leftover IGS live NBB WVV / Bosgroep Antwerpse Gordel 1448 leftover IGS live NBB WVV / Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV / RL Kleine en Grote Nete 1445 leftover IGS live NBB WVV / RL Haspengouw 1444 leftover IGS live NBB WVV / RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep Kempen Noord 0476.530.217 JR2025 CDN 2026-00086307 HEAD HTTP 200 as of 1449 (STRONG next leftover Bosgroep; SBM euros forbidden — extract PDF only); leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL Houtland still 2024; RL West-Vlaamse Hart still no jaarrekening; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1449 after Bosgroep Zuiderkempen leftover IGS live NBB WVV JR2025; MUST do every-10 then leftover Bosgroep Kempen Noord if CDN 2026-00086307 still live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1449=done + rq_1450 spawned; keep", last_line_start)

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
    f"tick1449 Bosgroep Zuiderkempen leftover IGS/Bosgroep residual; KBO 0860.780.968; live JR2025 NBB WVV PDF; sourced euros assets 863760 omzet empty diensten empty pers empty pnl 191700 equity 670580 cash 89632 debt 193180 capex 2579 dividend 0 bruto 206947 geldbeleg 705990; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / geldbeleg JUMP / cash DROP / 0 VE; NOT BGAG / BVB / BGOV / RLKGN / RLHV / RL de Voorkempen; next rq_1450 MUST do every-10 then leftover Bosgroep Kempen Noord if CDN 2026-00086307 still live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1449,1449,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1449")

entry = (
    "\n## Tick 1449 - 2026-08-19 - rq_1449 Bosgroep Zuiderkempen dual residual leftover\n"
    "- Unit: Bosgroep Zuiderkempen VZW / BGZK (leftover IGS / Bosgroep of mined Zuiderkempen cities; 0 VE) after residual dual hunt (KBO **0860.780.968**; official bosgroepen.be/zuiderkempen; live official NBB WVV VKT-VZW PDF **40515** bytes / 11p; deposit **2026-00104376**; AV **21.04.2026**; header **05.05.2026**; pdfinfo created **07.05.2026**; model **VKT-VZW** 26.0.10 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.3/6.3/6.5/6.6/6.7/7/8 not filed; 6.1.2 MVA + 6.2 fondsen + 6.4 + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022 (SBM laatste jaarrekening 2022-12-31); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member-region cities already mined (AGB Westerlo / AGB Herselt / AGB Sport Geel / AGB Cultuur Geel / AGB Heist-op-den-Berg / AGB Sport en Recreatie Herentals / AGB Herentals patrimonium) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen this tick: WVL Houtland 0866.482.291 SBM jaarrekeninganalyse niet beschikbaar; IJzer en Leie 0816.706.346 SBM no jaarrekening; Limburg 0668.619.317 SBM IP-blacklist; Koepel 0820.176.768 SBM no jaarrekening; Kempen Noord 0476.530.217 SBM last JR 2025-12-31 CDN **2026-00086307** HEAD HTTP 200 this tick (euros forbidden; left for after 1450 every-10). Leftover IGS Bosgroep Zuiderkempen statutory CDN `2026-00104376` live this tick (HTTP 200 / application/pdf / 40515 / 11p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS / Bosgroep of mined Zuiderkempen cities with live 2025 statutory PDF after leftover AGB hunt; Belscope claimed JR2025 as of 1448 / deposit id unpublished as of 1448). Distinct from already-mined **Bosgroep Antwerpse Gordel** (vzw_bgag tick 1448; KBO 0884.382.751; NOT this entity) / **Bosgroep Vlaams-Brabant** 1447 / **Bosgroep Oost-Vlaanderen** 1446 / **RL Kleine en Grote Nete** 1445 / **RL Haspengouw** 1444 / **RL de Voorkempen** 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426 / IOK / BIONERGA. First confirmed not already extracted as JR2025 euros: no Bosgroep Zuiderkempen / 0860.780.968 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **30.09.2003**; statutaire naam BOSGROEP ZUIDERKEMPEN since 30.09.2003; VZW since 30.09.2003; zetel Britselaan 20C 2260 Westerlo since 30.09.2003; **0 VE**; official site https://bosgroepen.be/zuiderkempen/; contact zuiderkempen@bosgroep.be; tel 014 27 96 57; NACE btw 02.100; btw since 01.03.2007; **20 functiehouders**. Bestuurders include Philips / Helsen / Stappaerts / Verrezen / Willems / De Haes / Milis / Hermans / Tordoor / Sybens / Salaets / De Bie / Keymeulen / Verbraecken + gemeenten Herselt / Meerhout / Westerlo / Balen + provincie Antwerpen. Official site Zuiderkempen cities Westerlo / Herselt / Geel / Heist-op-den-Berg / Hulshout / Herentals / Olen / Laakdal / Balen / Mol / Meerhout + provincie. Named member-city share-% unpublished. Contact zuiderkempen@bosgroep.be. Prior-year figures restated (PDF: niet identiek). NBB consult skipped (403/SPA); SBM HTML IP-blacklisted from box curl; WebFetch SBM yielded deposit id only (euros not used). Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 empty / no VTE): assets **863760** (was 728166); fixed **20844** / IVA empty / MVA **20844** terreinen vs 18265 / FVA empty; current **842916**; ST recv **44956** vs 42308 (trade **21404** vs 27659 / other **23552** vs 14649); geldbeleg **705990 JUMP** vs 530940; cash **89632 DROP** vs 129520; prepaid **2338** vs 7133; equity **670580** (fondsen **2579**; bestemde **668001**; overgedragen **0**); voorzieningen empty; schulden **193180 DROP** vs 251865 (LT empty; ST **148909** vs 157790 waarvan leveranciers **110412** vs 117407 + tax **3659** vs 280 + overige **34838** vs 40103; deferred **44271 DROP** vs 94075); brutomarge **206947** vs 49729; omzet empty; 73 empty; 60/61 empty; pers empty; andere **4930** vs 2142; expl **+202017** vs +47587; fin opbr **9749** (rec 4433 + nrec 5316); fin kosten **20066** (rec 46 + nrec 20020); tax empty; PnL **+191700** vs +51748; dividend **0**; onttrekking bestemde **7138**; toevoeging bestemde **198838**; over te dragen **0**; capex **2579** (MVA aanschaf only). PDF cross-checks close (fixed+current=assets; EV+debt=passiva; 9900-andere=9901; 9901+fin-kost=9903).\n"
    f"- CSVs: sources +4; entities +1 `vzw_bgzk` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 206947 AV 21.04.2026; leaderboard +1 annual 206947 / total 863760; foi_queue +1 status=ready never sent; research_queue surgical rq_1449=done + rq_1450 spawn; loop_state ticks_completed=1449. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_bgzk_omzet_empty_bruto_0_21m_geldbeleg_0_71m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / empty pers / geldbeleg JUMP 0.71m / cash DROP 0.09m / deferred DROP 0.04m / debt DROP 0.19m / nrec fin kost 20k / restated PY / expl +202k / pnl +192k / 0 VE / capex 2.6k / vennoten share-pct / relation to BGAG / BVB / BGOV / Kempen Noord / Koepel / RLKGN / provincie unpublished.\n"
    "- Next: rq_1450 MUST do every-10 (progress_every_10_ticks.md + doge_waste_top10_current.md). Dual NEW since 1440: RL de Voorkempen 4.47m / RL Brabantse Kouters 1.46m / RL Meetjesland 0.87m / RL Haspengouw 2.85m / RLKGN 1.48m / BGOV 0.99m / BVB 0.57m / BGAG 0.79m / BGZK 0.86m + 1450 unit. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep Kempen Noord **0476.530.217** JR2025 CDN **2026-00086307** LIVE this tick (STRONG next leftover Bosgroep; SBM euros forbidden). Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel only if a 2025 CDN is live. Leftover RL Houtland & Polders **0472.947.254** only if JR2025 now live. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1449 -" in lraw:
    raise SystemExit("loop_log already has tick 1449 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1449")
print("DONE tick 1449")
