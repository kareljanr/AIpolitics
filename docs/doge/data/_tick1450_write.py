#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1450 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:33:00Z"
ENT = "vzw_bgkn"
SRC = "src_bgkn_jr2025_nbb"
GAP = "gap_bgkn_omzet_empty_bruto_33k_geldbeleg_1_53m_l5"
LB = "lb_bgkn_omzet_empty_bruto_33k_geldbeleg_1_53m"
COMM = "comm_bgkn_jr2025_bruto"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_bgkn_jr2025_nbb,Bosgroep Kempen Noord VZW official NBB WVV VKT-VZW JR2025,http://cdn.staatsbladmonitor.be/2026pdf/2026-00086307.pdf,NBB Central Balance Sheet Office,2026-08-19,budget,tick1450; official NBB WVV VKT-VZW deposit 2026-00086307 PDF 12p / 42632 bytes; pdfinfo created 24.04.2026; header 20.04.2026; AV 28.03.2026; KBO 0476.530.217; assets 2588174 cash 581821 debt 1382447 bruto 32802 omzet empty 73 empty 60/61 empty pers empty 0 VTE pnl 25273 equity 1205727 geldbeleg 1529352",
    "src_bgkn_site,Bosgroep Kempen Noord official site,https://bosgroepen.be/kempennoord/,Bosgroep Kempen Noord VZW,2026-08-19,official_register,tick1450; leftover IGS / Bosgroep of mined Kempen-Noord cities; zetel Polderstraat 33 2360 Oud-Turnhout; contact kempennoord@bosgroep.be; tel 014 85 90 17; official site 20 gemeenten / 3000 leden / 10000 ha",
    "src_kbo_bgkn_0476530217,KBO Bosgroep Kempen Noord 0476.530.217,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0476530217,KBO Public Search FOD Economie,2026-08-19,official_register,tick1450; Actief since 04.12.2001; naam Bosgroep Kempen Noord since 18.06.2016; zetel Polderstraat 33 2360 Oud-Turnhout since 26.03.2022; 0 VE; VZW; NACE 02.100 / 02.200; btw since 01.03.2007; 21 functiehouders; aanbestedende overheid since 04.12.2001",
    "src_bgkn_foi_contact,Bosgroep Kempen Noord FOI channel (kempennoord@bosgroep.be; Polderstraat 33 Oud-Turnhout),https://bosgroepen.be/kempennoord/,Bosgroep Kempen Noord VZW,2026-08-19,official_register,tick1450; Kempen Noord leftover Bosgroep + provincie Antwerpen; NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen / RL de Voorkempen",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_bgkn," in raw or raw.startswith(b"vzw_bgkn,"):
    raise SystemExit("vzw_bgkn already present")
if b"0476.530.217" in raw or b"0476530217" in raw:
    raise SystemExit("Bosgroep Kempen Noord KBO already present")
row = (
    "vzw_bgkn,Bosgroep Kempen Noord VZW (leftover IGS / Bosgroep of mined Kempen-Noord cities; NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen / RL de Voorkempen),"
    "Bosgroep Kempen Noord ASBL (IGS residuel / groupe forestier Campine du Nord),"
    "Bosgroep Kempen Noord leftover IGS / forest-group VZW of mined Kempen-Noord municipalities (not BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen),"
    "other,sec_flanders,nl,https://bosgroepen.be/kempennoord/,kempennoord@bosgroep.be,Polderstraat 33 2360 Oud-Turnhout,"
    "tick1450 leftover residual IGS/Bosgroep VZW of mined Kempen-Noord cities after leftover AGB hunt; KBO 0476.530.217 Actief since 04.12.2001; live JR2025 NBB WVV PDF downloads; sourced euros assets 2588174 omzet empty diensten empty pers empty 0 VTE pnl 25273 equity 1205727 cash 581821 debt 1382447 capex 0 dividend 0 bruto 32802 geldbeleg 1529352; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / 0 VTE / geldbeleg JUMP / cash JUMP / debt JUMP / 0 VE / leden share-pct; distinct from already-mined BGZK 1449 / BGAG 1448 / BVB 1447 / BGOV 1446 / RLKGN 1445 (same Polderstraat 33 address) / RL Lage Kempen 1430 / Erfgoed Noorderkempen 1426 / RL de Voorkempen 1441"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_bgkn")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_bgkn_assets_2025", "2025", "2588174", "2025 assets 2588174 (was 2093808); tick1450; primary official NBB WVV"),
    ("bud_bgkn_fixed_2025", "2025", "227813", "2025 vaste activa 227813 (was 243290); tick1450; primary official NBB WVV"),
    ("bud_bgkn_iva_2025", "2025", "0", "2025 IVA 0; 6.1.1 filed empty; tick1450; primary official NBB WVV"),
    ("bud_bgkn_mva_2025", "2025", "227813", "2025 MVA 227813 terreinen 217474 + meubilair 10339 (was 243290); tick1450; primary official NBB WVV"),
    ("bud_bgkn_terreinen_2025", "2025", "217474", "2025 terreinen/gebouwen 22 217474 (was 227359); tick1450; primary official NBB WVV"),
    ("bud_bgkn_meubilair_2025", "2025", "10339", "2025 meubilair 24 10339 (was 15931); tick1450; primary official NBB WVV"),
    ("bud_bgkn_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1450; primary official NBB WVV"),
    ("bud_bgkn_current_2025", "2025", "2360361", "2025 vlottend 2360361 (was 1850518); tick1450; primary official NBB WVV"),
    ("bud_bgkn_strecv_2025", "2025", "249189", "2025 ST vorderingen 249189 (was 126797); tick1450; primary official NBB WVV"),
    ("bud_bgkn_trade_2025", "2025", "122986", "2025 handelsvorderingen 122986 (was 99641); tick1450; primary official NBB WVV"),
    ("bud_bgkn_othrecv_2025", "2025", "126203", "2025 overige vorderingen 126203 JUMP (was 27156); tick1450; primary official NBB WVV"),
    ("bud_bgkn_geldbeleg_2025", "2025", "1529352", "2025 geldbeleggingen 1529352 JUMP (was 1353164); tick1450; primary official NBB WVV"),
    ("bud_bgkn_cash_2025", "2025", "581821", "2025 liquide middelen 581821 JUMP (was 352856); tick1450; primary official NBB WVV"),
    ("bud_bgkn_prepaid_2025", "2025", "0", "2025 prepaid 0 (was 17702); tick1450; primary official NBB WVV"),
    ("bud_bgkn_equity_2025", "2025", "1205727", "2025 EV 1205727 (was 1186135); tick1450; primary official NBB WVV"),
    ("bud_bgkn_bestemde_2025", "2025", "1080760", "2025 bestemde fondsen 1080760 (was 1055487); tick1450; primary official NBB WVV"),
    ("bud_bgkn_overgedragen_2025", "2025", "0", "2025 overgedragen 0; tick1450; primary official NBB WVV"),
    ("bud_bgkn_kapsubs_2025", "2025", "124967", "2025 kapitaalsubsidies 15 124967 (was 130648); tick1450; primary official NBB WVV"),
    ("bud_bgkn_debt_2025", "2025", "1382447", "2025 schulden 1382447 JUMP (was 907674; LT empty); tick1450; primary official NBB WVV"),
    ("bud_bgkn_stdebt_2025", "2025", "743653", "2025 ST schulden 743653 JUMP (was 503095); tick1450; primary official NBB WVV"),
    ("bud_bgkn_lev_2025", "2025", "649299", "2025 leveranciers 649299 JUMP (was 448869); tick1450; primary official NBB WVV"),
    ("bud_bgkn_wissels_2025", "2025", "500", "2025 te betalen wissels 441 500; tick1450; primary official NBB WVV"),
    ("bud_bgkn_tax_2025", "2025", "0", "2025 belastingen 450/3 0 (was 16841; bezold empty); tick1450; primary official NBB WVV"),
    ("bud_bgkn_othdebt_2025", "2025", "93853", "2025 overige schulden 93853 JUMP (was 37385); tick1450; primary official NBB WVV"),
    ("bud_bgkn_deferred_2025", "2025", "638794", "2025 deferred 638794 JUMP (was 404579); tick1450; primary official NBB WVV"),
    ("bud_bgkn_bruto_2025", "2025", "32802", "2025 brutomarge 9900 32802 DROP (was 96524); tick1450; primary official NBB WVV"),
    ("bud_bgkn_afschr_2025", "2025", "15477", "2025 afschrijvingen 630 15477 (was 16393); tick1450; primary official NBB WVV"),
    ("bud_bgkn_andere_2025", "2025", "9215", "2025 andere bedrijfskosten 640/8 9215 (was 7461); tick1450; primary official NBB WVV"),
    ("bud_bgkn_expl_2025", "2025", "8110", "2025 expl 8110 (was 72671); tick1450; primary official NBB WVV"),
    ("bud_bgkn_finopbr_2025", "2025", "17314", "2025 fin opbr 17314 all recurrent (was 19633); tick1450; primary official NBB WVV"),
    ("bud_bgkn_finkost_2025", "2025", "152", "2025 fin kosten 152 all recurrent (was 136); tick1450; primary official NBB WVV"),
    ("bud_bgkn_pnl_2025", "2025", "25273", "2025 PnL 25273 (was 92168); tick1450; primary official NBB WVV"),
    ("bud_bgkn_div_2025", "2025", "0", "2025 dividend 0; tick1450; primary official NBB WVV"),
    ("bud_bgkn_pers_2025", "2025", "0", "2025 pers 62 empty / 9087 = 0 VTE; 6.7 not filed; tick1450; primary official NBB WVV"),
    ("bud_bgkn_capex_2025", "2025", "0", "2025 capex MVA aanschaf 8169 0; IVA/FVA empty; tick1450; primary official NBB WVV"),
    ("bud_bgkn_onttrekking_2025", "2025", "13690", "2025 onttrekking bestemde 791 13690; tick1450; primary official NBB WVV"),
    ("bud_bgkn_toevoeging_2025", "2025", "38963", "2025 toevoeging bestemde 691 38963; tick1450; primary official NBB WVV"),
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
    f"{COMM},Bosgroep Kempen Noord VZW JR2025 leftover IGS dual (bruto 33k / empty 70-73-60/61 / geldbeleg 1.53m),{ENT},Bosgroep Kempen Noord VZW / mined Kempen-Noord cities,WVV VZW; official NBB VKT-VZW; provincie Antwerpen,2026-03-28,2001,,32802,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00086307.pdf,Local leftover IGS map VL Bosgroep Kempen Noord — bruto 33k / empty omzet / geldbeleg 1.53m,Publish empty 70/73/60-61/pers + 0 VTE + geldbeleg JUMP + cash JUMP + debt JUMP + 0 VE + vennoten share-pct; do not keep leftover BGKN VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>BosgroepKN>JR2025_L5,tick1450; assets 2588174 omzet empty diensten empty pers empty 0 VTE pnl 25273 equity 1205727 cash 581821 debt 1382447 capex 0 dividend 0 bruto 32802 geldbeleg 1529352; FOI ready not sent; not TE-additive of 348bn; NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},Bosgroep Kempen Noord VZW JR2025 leftover IGS: empty 70/73/60-61 / bruto 33k / geldbeleg 1.53m / cash JUMP,L5,local_budget_line,Vlaanderen>Antwerpen>BosgroepKN>JR2025_L5,32802,2588174,Leftover dual IGS/Bosgroep VZW: assets 2.59m / equity 1.21m / pnl +25k / omzet empty / 73 empty / 60-61 empty / pers empty 0 VTE / geldbeleg 1.53m JUMP / cash 0.58m JUMP / debt 1.38m JUMP / dividend 0 / NBB 2026-00086307,strong,{SRC},Bosgroep Kempen Noord VZW / mined Kempen-Noord cities,Local leftover IGS map VL Bosgroep Kempen Noord — JR2025 NBB WVV live; empty 70/73/60-61 FOI,Official NBB WVV 2026-08-19: bruto 33k / empty omzet / geldbeleg 1.53m / PnL +25k,6.6,6.2,2.5,6.3,Publish empty 70/73/60-61/pers + 0 VTE + geldbeleg JUMP + cash JUMP + debt JUMP + 0 VE + vennoten share-pct; do not keep leftover BGKN VZW as dual unpublished vehicle,active,,tick1450; leftover IGS/Bosgroep after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined BGZK 1449 / BGAG 1448 / BVB 1447 / BGOV 1446 / RLKGN 1445 / RL Lage Kempen 1430 / Erfgoed Noorderkempen 1426 / RL de Voorkempen 1441",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>BosgroepKN>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 32802 DROP vs 96524 + pers 62 empty 0 VTE + 0 VE + geldbeleg 1529352 JUMP vs 1353164 + cash 581821 JUMP vs 352856 + other recv JUMP 126203 vs 27156 + lev JUMP 649299 vs 448869 + deferred JUMP 638794 vs 404579 + debt JUMP 1382447 vs 907674 + capex 0 + vennoten share-pct unpublished + relation to BGZK/BGAG/BVB/BGOV/Koepel/RLKGN/RL Lage Kempen/Erfgoed Noorderkempen/provincie unpublished,Leftover BGKN VZW after leftover AGB hunt: bruto 33k / empty omzet 70 hides public-perimeter bosgroep vehicle,8,Bosgroep Kempen Noord vzw / Bestuursorgaan,kempennoord@bosgroep.be,Polderstraat 33 2360 Oud-Turnhout,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1450 leftover IGS/Bosgroep after honest leftover AGB hunt; live JR2025 NBB WVV PDF now extracted (42632 bytes 12p). FOI ready not sent. EVERY-10 this tick. NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen / RL de Voorkempen. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 SBM IP-blacklist or no page this tick. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong/Oost-Haspengouw still no JR2025. Leftover RL Houtland still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening.",
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
if not last_s.startswith("rq_1450,"):
    raise SystemExit(f"expected last row rq_1450, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1450 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1450,Bosgroep Kempen Noord JR2025 leftover dual residual + progress,hole_fill,5,done,L5,vzw_bgkn,"
    "Completed: Bosgroep Kempen Noord VZW leftover IGS / Bosgroep of mined Kempen-Noord cities after leftover AGB hunt; KBO 0476.530.217 Actief; live JR2025 official NBB WVV VKT-VZW PDF (42632 bytes 12p deposit 2026-00086307; AV 28.03.2026; header 20.04.2026; created 24.04.2026; no commissaris listed); sourced euros assets 2588174 omzet empty diensten empty pers empty 0 VTE pnl 25273 equity 1205727 cash 581821 debt 1382447 capex 0 dividend 0 bruto 32802 geldbeleg 1529352; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / 0 VTE / geldbeleg JUMP / cash JUMP / debt JUMP / 0 VE / leden share-pct; EVERY-10 progress refresh; NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen / RL de Voorkempen,"
    f"{GAP},2026-08-19T13:25:00Z,{TS},"
    "tick1450 Bosgroep Kempen Noord leftover IGS/Bosgroep residual + every-10; KBO 0476.530.217; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1451 leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel if CDN live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart"
)
spawn = (
    "rq_1451,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1450 done including Bosgroep Kempen Noord 1450 leftover IGS live NBB WVV + every-10 / Bosgroep Zuiderkempen 1449 leftover IGS live NBB WVV / Bosgroep Antwerpse Gordel 1448 leftover IGS live NBB WVV / Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV / RL Kleine en Grote Nete 1445 leftover IGS live NBB WVV / RL Haspengouw 1444 leftover IGS live NBB WVV / RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (SBM IP-blacklist or no page as of 1450); leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL Houtland still 2024; RL West-Vlaamse Hart still no jaarrekening; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1450 after Bosgroep Kempen Noord leftover IGS live NBB WVV JR2025 + every-10; leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel if CDN live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1450=done + rq_1451 spawned; keep", last_line_start)

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
    f"tick1450 Bosgroep Kempen Noord leftover IGS/Bosgroep residual + every-10; KBO 0476.530.217; live JR2025 NBB WVV PDF; sourced euros assets 2588174 omzet empty diensten empty pers empty 0 VTE pnl 25273 equity 1205727 cash 581821 debt 1382447 capex 0 dividend 0 bruto 32802 geldbeleg 1529352; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / 0 VTE / geldbeleg JUMP / cash JUMP / debt JUMP / 0 VE; NOT BGZK / BGAG / BVB / BGOV / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen; next rq_1451 leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Koepel if CDN live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1450,1450,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1450")

entry = (
    "\n## Tick 1450 - 2026-08-19 - rq_1450 Bosgroep Kempen Noord dual residual leftover + every-10\n"
    "- Unit: Bosgroep Kempen Noord VZW / BGKN (leftover IGS / Bosgroep of mined Kempen-Noord cities; 0 VE) after residual dual hunt (KBO **0476.530.217**; official bosgroepen.be/kempennoord; live official NBB WVV VKT-VZW PDF **42632** bytes / 12p; deposit **2026-00086307**; AV **28.03.2026**; header **20.04.2026**; pdfinfo created **24.04.2026**; model **VKT-VZW** 26.0.10 m04-f; no commissaris listed; VKT-VZW 6.1.3/6.3/6.5/6.6/6.7/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.2 fondsen + 6.4 + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member-region cities already mined (AGB Beerse / AGB Sport en Recreatie Herentals / AGB Herentals patrimonium / AGB Lille liquidation / AGB Sportcentrum t Hofeind Merksplas / AGB Turnhout) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen this tick: WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 SBM IP-blacklist or no page this tick. Leftover IGS Bosgroep Kempen Noord statutory CDN `2026-00086307` live this tick (HTTP 200 / application/pdf / 42632 / 12p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS / Bosgroep of mined Kempen-Noord cities with live 2025 statutory PDF after leftover AGB hunt; CDN live as of 1449 / SBM euros forbidden). Distinct from already-mined **Bosgroep Zuiderkempen** (vzw_bgzk tick 1449; KBO 0860.780.968; NOT this entity) / **Bosgroep Antwerpse Gordel** 1448 / **Bosgroep Vlaams-Brabant** 1447 / **Bosgroep Oost-Vlaanderen** 1446 / **RL Kleine en Grote Nete** (vzw_rlkn tick 1445; KBO 0810.764.897; same Polderstraat 33 2360 Oud-Turnhout address — NOT this entity) / **RL Lage Kempen** 1430 / Erfgoed Noorderkempen 1426 / RL de Voorkempen 1441 / IOK / BIONERGA. First confirmed not already extracted as JR2025 euros: no Bosgroep Kempen Noord / 0476.530.217 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **04.12.2001**; statutaire naam Bosgroep Kempen Noord since 18.06.2016; VZW since 04.12.2001; zetel Polderstraat 33 2360 Oud-Turnhout since 26.03.2022; **0 VE**; official site https://bosgroepen.be/kempennoord/; contact kempennoord@bosgroep.be; tel 014 85 90 17; NACE btw 02.100 / 02.200; btw since 01.03.2007; aanbestedende overheid since 04.12.2001; **21 functiehouders**. Fusion of Bosgroep Noorderkempen + Bosgroep Kempense Heuvelrug (official site 20 gemeenten / 3000 leden / 10.000 ha). PDF bestuurders include Van Rooy / De Witte / Ceulemans (Mol) / Druyts / De Bont / Van Ravestyn / Philips / Verschueren / Van de Velde + gemeenten Beerse / Kasterlee / Lille / Oud-Turnhout / Ravels + provincie Antwerpen. Coordinator Marieke Verreet (provincie Antwerpen). Named member-city share-% unpublished. Contact kempennoord@bosgroep.be. Prior-year figures identical. NBB consult skipped (403/SPA); SBM HTML IP-blacklisted from box curl; SBM euros not used. Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. **Every-10 progress refresh** this tick (progress_every_10_ticks.md + doge_waste_top10_current.md).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 empty / **0 VTE**): assets **2588174** (was 2093808); fixed **227813** / IVA **0** / MVA **227813** (terreinen **217474** / meubilair **10339**) vs 243290 / FVA empty; current **2360361**; ST recv **249189** vs 126797 (trade **122986** vs 99641 / other **126203 JUMP** vs 27156); geldbeleg **1529352 JUMP** vs 1353164; cash **581821 JUMP** vs 352856; prepaid **0** vs 17702; equity **1205727** (bestemde **1080760**; kapitaalsubsidies **124967**; overgedragen **0**); voorzieningen empty; schulden **1382447 JUMP** vs 907674 (LT empty; ST **743653 JUMP** vs 503095 waarvan leveranciers **649299 JUMP** vs 448869 + wissels **500** + tax **0** vs 16841 + overige **93853 JUMP** vs 37385; deferred **638794 JUMP** vs 404579); brutomarge **32802 DROP** vs 96524; omzet empty; 73 empty; 60/61 empty; pers empty / 0 VTE; afschr **15477**; andere **9215**; expl **+8110** vs +72671; fin opbr **17314** all recurrent; fin kosten **152**; tax empty; PnL **+25273** vs +92168; dividend **0**; onttrekking bestemde **13690**; toevoeging bestemde **38963**; over te dragen **0**; capex **0** (MVA aanschaf only). PDF 1-euro rounding: current parts 2360362 vs published 2360361; ST parts 743652 vs published 743653; 8110+17314-152=25272 vs published 25273.\n"
    f"- CSVs: sources +4; entities +1 `vzw_bgkn` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 32802 AV 28.03.2026; leaderboard +1 annual 32802 / total 2588174; foi_queue +1 status=ready never sent; research_queue surgical rq_1450=done + rq_1451 spawn; loop_state ticks_completed=1450. Inventory after write: budgets {{inv_budgets}} · commitments {{inv_commitments}} · leaderboard {{inv_leaderboard}} · entities {{inv_entities}} · sources {{inv_sources}} · FOI ready {{foi_ready}} / answered {{foi_ans}} / partial {{foi_part}} / total {{foi_tot}}.\n"
    "- FOI: `gap_bgkn_omzet_empty_bruto_33k_geldbeleg_1_53m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / empty pers / 0 VTE / geldbeleg JUMP 1.53m / cash JUMP 0.58m / other recv JUMP 0.13m / lev JUMP 0.65m / deferred JUMP 0.64m / debt JUMP 1.38m / bruto DROP 33k / expl +8k / pnl +25k / 0 VE / capex 0 / vennoten share-pct / relation to BGZK / BGAG / BVB / BGOV / Koepel / RLKGN / RL Lage Kempen / Erfgoed Noorderkempen / provincie unpublished.\n"
    "- Every-10: refreshed progress_every_10_ticks.md (layers A–E; TE denominator EUR 347.956 bn; dual NEW since 1440: RL de Voorkempen 4.47m / RL Brabantse Kouters 1.46m / RL Meetjesland 0.87m / RL Haspengouw 2.85m / RLKGN 1.48m / BGOV 0.99m / BVB 0.57m / BGAG 0.79m / BGZK 0.86m / BGKN 2.59m) and doge_waste_top10_current.md (pure annual top10 stable GIP #1; fossil/cars/cheque/reporté #2–10; not TE-additive of ~348bn; Fluvius EG DSO double-count possible).\n"
    "- Next: rq_1451 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (SBM IP-blacklist or no page this tick). Leftover RL Houtland & Polders **0472.947.254** only if JR2025 now live. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
entry = entry.replace("{inv_budgets}", str(inv["budgets.csv"])).replace("{inv_commitments}", str(inv["commitments.csv"])).replace("{inv_leaderboard}", str(inv["leaderboard.csv"])).replace("{inv_entities}", str(inv["entities.csv"])).replace("{inv_sources}", str(inv["sources.csv"])).replace("{foi_ready}", str(foi_ready)).replace("{foi_ans}", str(foi_ans)).replace("{foi_part}", str(foi_part)).replace("{foi_tot}", str(foi_tot))
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1450 -" in lraw:
    raise SystemExit("loop_log already has tick 1450 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1450")
print("DONE tick 1450")
# write inventory sidecar for every-10
(DATA / "_tick1450_inv.txt").write_text(
    f"budgets={inv['budgets.csv']}\ncommitments={inv['commitments.csv']}\nleaderboard={inv['leaderboard.csv']}\nentities={inv['entities.csv']}\nsources={inv['sources.csv']}\nfoi_ready={foi_ready}\nfoi_answered={foi_ans}\nfoi_partial={foi_part}\nfoi_total={foi_tot}\nbudgets_added={len(added)}\n"
)
print("inv sidecar written")
