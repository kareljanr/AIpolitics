#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1448 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:20:00Z"
ENT = "vzw_bgag"
SRC = "src_bgag_jr2025_nbb"
GAP = "gap_bgag_omzet_empty_bruto_neg_25k_cash_0_35m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_bgag_jr2025_nbb,Bosgroep Antwerpse Gordel VZW official NBB WVV VKT-VZW JR2025,http://cdn.staatsbladmonitor.be/2026pdf/2026-00106416.pdf,NBB Central Balance Sheet Office,2026-08-19,budget,tick1448; official NBB WVV VKT-VZW deposit 2026-00106416 PDF 9p / 38900 bytes; pdfinfo created 08.05.2026; header 08.05.2026; AV 26.04.2026; KBO 0884.382.751; assets 793410 cash 346879 debt 259022 bruto -25593 omzet empty 73 empty 60/61 empty pers empty pnl -26580 equity 534389",
    "src_bgag_site,Bosgroep Antwerpse Gordel official site,https://bosgroepen.be/antwerpsegordel/,Bosgroep Antwerpse Gordel VZW,2026-08-19,official_register,tick1448; leftover IGS / Bosgroep of mined Antwerp-belt cities; zetel Schildesteenweg 99 2520 Ranst; contact antwerpsegordel@bosgroep.be; tel 03 355 09 40",
    "src_kbo_bgag_0884382751,KBO Bosgroep Antwerpse Gordel 0884.382.751,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0884382751,KBO Public Search FOD Economie,2026-08-19,official_register,tick1448; Actief since 07.09.2006; naam/afkorting BGAG of BAG since 10.10.2021; zetel Schildesteenweg 99 2520 Ranst since 26.03.2015; 0 VE; VZW; NACE 02.100; btw since 01.03.2007; 27 functiehouders; absorbed 0898.403.805 since 10.10.2021",
    "src_bgag_foi_contact,Bosgroep Antwerpse Gordel FOI channel (antwerpsegordel@bosgroep.be; Schildesteenweg 99 Ranst),https://bosgroepen.be/antwerpsegordel/,Bosgroep Antwerpse Gordel VZW,2026-08-19,official_register,tick1448; Antwerp-belt leftover Bosgroep + provincie Antwerpen; NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_bgag," in raw or raw.startswith(b"vzw_bgag,"):
    raise SystemExit("vzw_bgag already present")
if b"0884.382.751" in raw or b"0884382751" in raw:
    raise SystemExit("Bosgroep Antwerpse Gordel KBO already present")
row = (
    "vzw_bgag,Bosgroep Antwerpse Gordel VZW (leftover IGS / Bosgroep of mined Antwerp-belt cities; NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen),"
    "Bosgroep Antwerpse Gordel ASBL (IGS residuel / groupe forestier ceinture anversoise),"
    "Bosgroep Antwerpse Gordel leftover IGS / forest-group VZW of mined Antwerp-belt municipalities (not BVB / BGOV / RLKGN / RLHV / Erfgoed Voorkempen),"
    "other,sec_flanders,nl,https://bosgroepen.be/antwerpsegordel/,antwerpsegordel@bosgroep.be,Schildesteenweg 99 2520 Ranst,"
    "tick1448 leftover residual IGS/Bosgroep VZW of mined Antwerp-belt cities after leftover AGB hunt; KBO 0884.382.751 Actief since 07.09.2006; live JR2025 NBB WVV PDF downloads; sourced euros assets 793410 omzet empty diensten empty pers empty pnl -26580 equity 534389 cash 346879 debt 259022 capex unpublished dividend 0 bruto -25593; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / cash JUMP / lev JUMP / 0 VE / leden share-pct; distinct from already-mined BVB 1447 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RL de Voorkempen 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_bgag")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_bgag_assets_2025", "2025", "793410", "2025 assets 793410 (was 752880); tick1448; primary official NBB WVV"),
    ("bud_bgag_fixed_2025", "2025", "0", "2025 vaste activa empty; tick1448; primary official NBB WVV"),
    ("bud_bgag_iva_2025", "2025", "0", "2025 IVA empty; tick1448; primary official NBB WVV"),
    ("bud_bgag_mva_2025", "2025", "0", "2025 MVA empty; 6.1.2 not filed; tick1448; primary official NBB WVV"),
    ("bud_bgag_fva_2025", "2025", "0", "2025 FVA empty; tick1448; primary official NBB WVV"),
    ("bud_bgag_current_2025", "2025", "793410", "2025 vlottend 793410; tick1448; primary official NBB WVV"),
    ("bud_bgag_strecv_2025", "2025", "223047", "2025 ST vorderingen 223047 (was 294356); tick1448; primary official NBB WVV"),
    ("bud_bgag_trade_2025", "2025", "146160", "2025 handelsvorderingen 146160 DROP (was 219320); tick1448; primary official NBB WVV"),
    ("bud_bgag_othrecv_2025", "2025", "76887", "2025 overige vorderingen 76887 (was 75035); tick1448; primary official NBB WVV"),
    ("bud_bgag_geldbeleg_2025", "2025", "222226", "2025 geldbeleggingen 222226 (was 200834); tick1448; primary official NBB WVV"),
    ("bud_bgag_cash_2025", "2025", "346879", "2025 liquide middelen 346879 JUMP (was 257516); tick1448; primary official NBB WVV"),
    ("bud_bgag_prepaid_2025", "2025", "1259", "2025 prepaid 1259 (was 175); tick1448; primary official NBB WVV"),
    ("bud_bgag_equity_2025", "2025", "534389", "2025 EV 534389 DROP (was 560968); tick1448; primary official NBB WVV"),
    ("bud_bgag_bestemde_2025", "2025", "534389", "2025 bestemde fondsen 534389; tick1448; primary official NBB WVV"),
    ("bud_bgag_overgedragen_2025", "2025", "0", "2025 overgedragen 0; tick1448; primary official NBB WVV"),
    ("bud_bgag_debt_2025", "2025", "259022", "2025 schulden 259022 JUMP (was 191911; LT empty); tick1448; primary official NBB WVV"),
    ("bud_bgag_stdebt_2025", "2025", "211804", "2025 ST schulden 211804 JUMP (was 90864); tick1448; primary official NBB WVV"),
    ("bud_bgag_lev_2025", "2025", "187474", "2025 leveranciers 187474 JUMP (was 53896); tick1448; primary official NBB WVV"),
    ("bud_bgag_tax_2025", "2025", "5058", "2025 belastingen 450/3 5058 (bezold empty; was 10558); tick1448; primary official NBB WVV"),
    ("bud_bgag_othdebt_2025", "2025", "19272", "2025 overige schulden 19272 (was 26410); tick1448; primary official NBB WVV"),
    ("bud_bgag_deferred_2025", "2025", "47217", "2025 deferred 47217 DROP (was 101047); tick1448; primary official NBB WVV"),
    ("bud_bgag_bruto_2025", "2025", "-25593", "2025 brutomarge 9900 -25593 (was 2390); tick1448; primary official NBB WVV"),
    ("bud_bgag_andere_2025", "2025", "1683", "2025 andere bedrijfskosten 640/8 1683 (was 2536); tick1448; primary official NBB WVV"),
    ("bud_bgag_expl_2025", "2025", "-27276", "2025 expl -27276 (was -146); tick1448; primary official NBB WVV"),
    ("bud_bgag_finopbr_2025", "2025", "1004", "2025 fin opbr 1004 (was 788); tick1448; primary official NBB WVV"),
    ("bud_bgag_finkost_2025", "2025", "308", "2025 fin kosten 308 (was 291); tick1448; primary official NBB WVV"),
    ("bud_bgag_pnl_2025", "2025", "-26580", "2025 PnL -26580 (was +352); tick1448; primary official NBB WVV"),
    ("bud_bgag_div_2025", "2025", "0", "2025 dividend 0; tick1448; primary official NBB WVV"),
    ("bud_bgag_onttrekking_2025", "2025", "33993", "2025 onttrekking bestemde 791 33993; tick1448; primary official NBB WVV"),
    ("bud_bgag_toevoeging_2025", "2025", "7414", "2025 toevoeging bestemde 691 7414; tick1448; primary official NBB WVV"),
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
    f"comm_bgag_jr2025_bruto,Bosgroep Antwerpse Gordel VZW JR2025 leftover IGS dual (bruto -25k / empty 70-73-60/61 / cash 0.35m),{ENT},Bosgroep Antwerpse Gordel VZW / mined Antwerp-belt cities,WVV VZW; official NBB VKT-VZW; provincie Antwerpen,2026-04-26,2006,,25593,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00106416.pdf,Local leftover IGS map VL Bosgroep Antwerpse Gordel — abs bruto 25k / empty omzet / cash 0.35m,Publish empty 70/73/60-61/pers + cash JUMP + lev JUMP + 0 VE + vennoten share-pct; do not keep leftover BGAG VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>BosgroepAG>JR2025_L5,tick1448; assets 793410 omzet empty diensten empty pers empty pnl -26580 equity 534389 cash 346879 debt 259022 capex unpublished dividend 0 bruto -25593; FOI ready not sent; not TE-additive of 348bn; NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_bgag_omzet_empty_bruto_neg_25k_cash_0_35m,Bosgroep Antwerpse Gordel VZW JR2025 leftover IGS: empty 70/73/60-61 / bruto -25k / cash 0.35m / lev JUMP,L5,local_budget_line,Vlaanderen>Antwerpen>BosgroepAG>JR2025_L5,25593,793410,Leftover dual IGS/Bosgroep VZW: assets 0.79m / equity 0.53m / pnl -27k / omzet empty / 73 empty / 60-61 empty / pers empty no VTE / cash 0.35m JUMP / debt 0.26m / lev 0.19m JUMP / dividend 0 / NBB 2026-00106416,strong,{SRC},Bosgroep Antwerpse Gordel VZW / mined Antwerp-belt cities,Local leftover IGS map VL Bosgroep Antwerpse Gordel — JR2025 NBB WVV live; empty 70/73/60-61 FOI,Official NBB WVV 2026-08-19: abs bruto 25k / empty omzet / cash 0.35m / PnL -27k,6.4,5.5,2.5,5.9,Publish empty 70/73/60-61/pers + cash JUMP + lev JUMP + 0 VE + vennoten share-pct; do not keep leftover BGAG VZW as dual unpublished vehicle,active,,tick1448; leftover IGS/Bosgroep after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined BVB 1447 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RL de Voorkempen 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>BosgroepAG>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto -25593 + pers 62 empty no VTE + 0 VE + cash 346879 JUMP vs 257516 + lev 187474 JUMP vs 53896 + ST debt 211804 JUMP vs 90864 + equity DROP 534389 vs 560968 + deferred DROP 47217 vs 101047 + expl -27276 + pnl -26580 + capex unpublished + vennoten share-pct unpublished + relation to BVB/BGOV/Zuiderkempen/Kempen Noord/Koepel/RL Voorkempen/RLKGN/provincie unpublished,Leftover BGAG VZW after leftover AGB hunt: abs bruto 25k / empty omzet 70 hides public-perimeter bosgroep vehicle,8,Bosgroep Antwerpse Gordel vzw / Bestuursorgaan,antwerpsegordel@bosgroep.be,Schildesteenweg 99 2520 Ranst,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_bgag_jr2025_bruto,lb_bgag_omzet_empty_bruto_neg_25k_cash_0_35m,{TS},{TS},tick1448 leftover IGS/Bosgroep after honest leftover AGB hunt; live JR2025 NBB WVV PDF now extracted (38900 bytes 9p). FOI ready not sent. NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen. Leftover Bosgroep Zuiderkempen 0860.780.968 Belscope claims JR2025 (euros forbidden) / deposit id unpublished. Leftover WVL Houtland / IJzer en Leie / Limburg / Kempen Noord / Koepel still no live CDN. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong/Oost-Haspengouw still no JR2025. Leftover RL Houtland still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening.",
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
if not last_s.startswith("rq_1448,"):
    raise SystemExit(f"expected last row rq_1448, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1448 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1448,Bosgroep Antwerpse Gordel JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_bgag,"
    "Completed: Bosgroep Antwerpse Gordel VZW leftover IGS / Bosgroep of mined Antwerp-belt cities after leftover AGB hunt; KBO 0884.382.751 Actief; live JR2025 official NBB WVV VKT-VZW PDF (38900 bytes 9p deposit 2026-00106416; AV 26.04.2026; header 08.05.2026; created 08.05.2026; no commissaris listed); sourced euros assets 793410 omzet empty diensten empty pers empty pnl -26580 equity 534389 cash 346879 debt 259022 capex unpublished dividend 0 bruto -25593; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / cash JUMP / lev JUMP / 0 VE / leden share-pct; NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen / Erfgoed Voorkempen / Erfgoed Noorderkempen,"
    f"{GAP},2026-08-19T13:10:00Z,{TS},"
    "tick1448 Bosgroep Antwerpse Gordel leftover IGS/Bosgroep residual; KBO 0884.382.751; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1449 residual dual L5 VL leftover Bosgroep Zuiderkempen if CDN id live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen"
)
spawn = (
    "rq_1449,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1448 done including Bosgroep Antwerpse Gordel 1448 leftover IGS live NBB WVV / Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV / RL Kleine en Grote Nete 1445 leftover IGS live NBB WVV / RL Haspengouw 1444 leftover IGS live NBB WVV / RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep Zuiderkempen 0860.780.968 Belscope claims JR2025 (euros forbidden) — take if a 2026pdf deposit id now downloads (STRONG next leftover Bosgroep); leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Kempen Noord 0476.530.217 / Koepel 0820.176.768 only if a 2025 CDN is live; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL Houtland still 2024; RL West-Vlaamse Hart still no jaarrekening; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1448 after Bosgroep Antwerpse Gordel leftover IGS live NBB WVV JR2025; next residual dual L5 VL leftover Bosgroep Zuiderkempen if a 2025 CDN is now live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen; NOTE next 1450 MUST do every-10"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1448=done + rq_1449 spawned; keep", last_line_start)

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
    f"tick1448 Bosgroep Antwerpse Gordel leftover IGS/Bosgroep residual; KBO 0884.382.751; live JR2025 NBB WVV PDF; sourced euros assets 793410 omzet empty diensten empty pers empty pnl -26580 equity 534389 cash 346879 debt 259022 capex unpublished dividend 0 bruto -25593; FOI ready empty 70 / empty 73 / empty 60-61 / empty pers / cash JUMP / lev JUMP / 0 VE; NOT BVB / BGOV / RLKGN / RLHV / RL de Voorkempen; next rq_1449 residual dual L5 VL leftover Bosgroep Zuiderkempen if CDN id live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen; NOTE next 1450 MUST do every-10; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1448,1448,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1448")

entry = (
    "\n## Tick 1448 - 2026-08-19 - rq_1448 Bosgroep Antwerpse Gordel dual residual leftover\n"
    "- Unit: Bosgroep Antwerpse Gordel VZW / BGAG (leftover IGS / Bosgroep of mined Antwerp-belt cities; 0 VE) after residual dual hunt (KBO **0884.382.751**; official bosgroepen.be/antwerpsegordel; live official NBB WVV VKT-VZW PDF **38900** bytes / 9p; deposit **2026-00106416**; AV **26.04.2026**; header **08.05.2026**; pdfinfo created **08.05.2026**; no commissaris listed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member-region cities already mined (AGB Zoersel / AGB Duffel / AGB Kapellen / AGB Mortsel / AGB Beerse / Heist-op-den-Berg AGB / AGB Sport Geel) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen: WVL Houtland 0866.482.291 no NBB 2025 found; IJzer en Leie 0816.706.346 Companyweb geen jaarrekening as of 1447; Limburg 0668.619.317 Companyweb geen jaarrekening as of 1447; Kempen Noord 0476.530.217 Companyweb geen jaarrekening as of 1447; Koepel 0820.176.768 NBB consult No results as of 1447; Zuiderkempen 0860.780.968 Belscope claims JR2025 (euros forbidden) / deposit id unpublished this tick. Leftover IGS Bosgroep Antwerpse Gordel statutory CDN `2026-00106416` live this tick (HTTP 200 / application/pdf / 38900 / 9p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS / Bosgroep of mined Antwerp-belt cities with live 2025 statutory PDF after leftover AGB hunt; deposit id unpublished as of 1447). Distinct from already-mined **Bosgroep Vlaams-Brabant** (vzw_bgvb tick 1447; KBO 0683.509.015; NOT this entity) / **Bosgroep Oost-Vlaanderen** 1446 / **RL Kleine en Grote Nete** 1445 / **RL Haspengouw** 1444 / **RL de Voorkempen** 1441 / Erfgoed Voorkempen 1425 / Erfgoed Noorderkempen 1426 / IOK / BIONERGA. First confirmed not already extracted as JR2025 euros: no Bosgroep Antwerpse Gordel / 0884.382.751 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **07.09.2006**; statutaire naam Bosgroep Antwerpse Gordel since 10.10.2021; afkorting BGAG of BAG since 10.10.2021; VZW since 07.09.2006; zetel Schildesteenweg 99 2520 Ranst since 26.03.2015; **0 VE**; official site https://bosgroepen.be/antwerpsegordel/; contact antwerpsegordel@bosgroep.be; tel 03 355 09 40; NACE btw 02.100; btw since 01.03.2007; **27 functiehouders**. Bestuurders include Van de Peer / Van Brabant / van Haaren / Van der Haegen / Van Goethem / Van den Bossche / Geuens / Cant / Ryelandt / Impens + gemeenten Boechout / Bornem / Essen / Zoersel + provincie Antwerpen. Absorbed Bosgroep Antwerpen Zuid 0898.403.805 since 10.10.2021. Official site Antwerp-belt + provincie. Named member-city share-% unpublished. Contact antwerpsegordel@bosgroep.be. NBB consult skipped (403/SPA); SBM HTML IP-blacklisted from box curl; WebFetch SBM yielded deposit id only (euros not used). Euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty**; brutomarge **−25593**; pers 62 empty / no VTE): assets **793410** (was 752880); fixed empty / IVA empty / MVA empty / FVA empty; current **793410**; ST recv **223047** vs 294356 (trade **146160 DROP** vs 219320 / other **76887** vs 75035); geldbeleg **222226** vs 200834; cash **346879 JUMP** vs 257516; prepaid **1259** vs 175; equity **534389 DROP** vs 560968 (bestemde **534389**; overgedragen **0**); voorzieningen empty; schulden **259022 JUMP** vs 191911 (LT empty; ST **211804 JUMP** vs 90864 waarvan leveranciers **187474 JUMP** vs 53896 + tax **5058** vs 10558 + overige **19272** vs 26410; deferred **47217 DROP** vs 101047); brutomarge **−25593** vs 2390; omzet empty; 73 empty; 60/61 empty; pers empty; andere **1683** vs 2536; expl **−27276** vs −146; fin opbr **1004**; fin kosten **308**; tax empty; PnL **−26580** vs +352; dividend **0**; onttrekking bestemde **33993**; toevoeging bestemde **7414**; over te dragen **0**; capex unpublished (6.1.x not filed). PDF 1-euro rounding: trade+other+geldbeleg+cash+prepaid 793411 vs published assets 793410; ST+deferred 259021 vs published schulden 259022.\n"
    f"- CSVs: sources +4; entities +1 `vzw_bgag` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 25593 AV 26.04.2026; leaderboard +1 annual 25593 / total 793410; foi_queue +1 status=ready never sent; research_queue surgical rq_1448=done + rq_1449 spawn; loop_state ticks_completed=1448. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_bgag_omzet_empty_bruto_neg_25k_cash_0_35m_l5` ready not sent — empty 70 / empty 73 / empty 60-61 / empty pers / cash JUMP 0.35m / lev JUMP 0.19m / ST debt JUMP 0.21m / equity DROP 0.53m / deferred DROP / expl -27k / pnl -27k / 0 VE / capex unpublished / vennoten share-pct / relation to BVB / BGOV / Zuiderkempen / Kempen Noord / Koepel / RL Voorkempen / RLKGN / provincie unpublished.\n"
    "- Next: rq_1449 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep Zuiderkempen **0860.780.968** Belscope claims JR2025 (euros forbidden) — take if a 2026pdf deposit id now downloads (STRONG next leftover Bosgroep). Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Kempen Noord / Koepel only if a 2025 CDN is live. Leftover RL Houtland & Polders **0472.947.254** only if JR2025 now live. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined. NOTE next 1450 MUST do every-10.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1448 -" in lraw:
    raise SystemExit("loop_log already has tick 1448 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1448")
print("DONE tick 1448")
