#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1452 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:50:00Z"
ENT = "cv_clmb"
SRC = "src_clmb_jr2025_nbb"
GAP = "gap_clmb_omzet_empty_bruto_0_39m_pers_0_35m_neg_ev_l5"
LB = "lb_clmb_omzet_empty_bruto_0_39m_pers_0_35m_neg_ev"
COMM = "comm_clmb_jr2025_bruto"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_clmb_jr2025_nbb,Cooeperatieve van de Limburgse Bosgroepen official NBB WVV MIC-inb JR2025,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244195.pdf,NBB Central Balance Sheet Office,2026-08-19,budget,tick1452; official NBB WVV MIC-inb deposit 2026-00244195 PDF 14p / 280997 bytes; pdfinfo created 03.07.2026; header 01.07.2026; AV 09.03.2026; KBO 0890.220.171; assets 911880 cash 642128 debt 956910 bruto 388600 omzet empty diensten empty pers 352382 4.2 VTE pnl 34914 equity -45030",
    "src_clmb_site,Bosgroep Limburg / CoLimBo official site,https://bosgroep.limburg.be/,Bosgroep Limburg / Cooeperatieve van de Limburgse Bosgroepen,2026-08-19,official_register,tick1452; leftover Bosgroep Limburg daughter / houtverkoop CV of mined Limburg cities; zetel Universiteitslaan 1 3500 Hasselt; contact bosgroep@limburg.be",
    "src_kbo_clmb_0890220171,KBO Cooeperatieve van de Limburgse Bosgroepen 0890.220.171,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0890220171,KBO Public Search FOD Economie,2026-08-19,official_register,tick1452; Actief since 20.06.2007; naam Cooeperatieve van de Limburgse Bosgroepen since 14.06.2007; CV since 17.11.2023; zetel Universiteitslaan 1 3500 Hasselt since 01.01.2025; 1 VE; Werkgever RSZ since 01.01.2016; 6 functiehouders; bestuurder Bosgroep Limburg VZW 0668.619.317",
    "src_clmb_foi_contact,CoLimBo FOI channel (bosgroep@limburg.be; Universiteitslaan 1 Hasselt),https://bosgroepen.be/limburg/,Cooeperatieve van de Limburgse Bosgroepen CV,2026-08-19,official_register,tick1452; leftover Bosgroep Limburg daughter + provincie Limburg; NOT Bosgroep Limburg VZW / Koepel / RL Kempen en Maasland / RL Lage Kempen",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\ncv_clmb," in raw or raw.startswith(b"cv_clmb,"):
    raise SystemExit("cv_clmb already present")
if b"0890.220.171" in raw or b"0890220171" in raw:
    raise SystemExit("CoLimBo KBO already present")
row = (
    "cv_clmb,Cooeperatieve van de Limburgse Bosgroepen CV (leftover Bosgroep Limburg daughter / houtverkoop CV of mined Limburg cities; NOT Bosgroep Limburg VZW 0668.619.317 / Koepel / RL Kempen en Maasland / RL Lage Kempen),"
    "Cooperative des Groupements forestiers limbourgeois SC (filiale residuelle Bosgroep Limburg),"
    "Cooperative of the Limburg Forest Groups leftover Bosgroep Limburg daughter / timber-sales CV of mined Limburg municipalities (not Bosgroep Limburg VZW / Koepel / RL Kempen en Maasland),"
    "other,sec_flanders,nl,https://bosgroep.limburg.be/,bosgroep@limburg.be,Universiteitslaan 1 3500 Hasselt,"
    "tick1452 leftover residual Bosgroep Limburg daughter CV after leftover AGB/IGS/Bosgroep VZW hunt; KBO 0890.220.171 Actief since 20.06.2007; live JR2025 NBB WVV PDF; sourced euros assets 911880 omzet empty diensten empty pers 352382 4.2 VTE pnl 34914 equity -45030 cash 642128 debt 956910 capex 3200 dividend 0 bruto 388600; FOI ready omzet empty / pers 0.35m / cash JUMP / other-debt JUMP / neg EV alarmbel / 1 VE / vennoten share-pct; distinct from leftover Bosgroep Limburg VZW 0668.619.317 (same Universiteitslaan 1 address) / leftover Koepel 0820.176.768 / already-mined RL Kempen en Maasland 1433 / already-mined RL Lage Kempen 1430"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 cv_clmb")

# --- budgets (PDF integers) ---
BUDGETS = [
    ("bud_clmb_assets_2025", "2025", "911880", "2025 assets 911880 (was 532929); tick1452; primary official NBB WVV"),
    ("bud_clmb_fixed_2025", "2025", "3172", "2025 vaste activa 3172 (was 0); tick1452; primary official NBB WVV"),
    ("bud_clmb_iva_2025", "2025", "0", "2025 IVA empty; 6.1.1 not filed; tick1452; primary official NBB WVV"),
    ("bud_clmb_mva_2025", "2025", "3172", "2025 MVA 3172 installaties 3172 (was 0); tick1452; primary official NBB WVV"),
    ("bud_clmb_install_2025", "2025", "3172", "2025 installaties 23 3172 (was 0); tick1452; primary official NBB WVV"),
    ("bud_clmb_fva_2025", "2025", "0", "2025 FVA empty; 6.1.3 not filed; tick1452; primary official NBB WVV"),
    ("bud_clmb_current_2025", "2025", "908708", "2025 vlottend 908708 (was 532929); tick1452; primary official NBB WVV"),
    ("bud_clmb_voorraden_2025", "2025", "58095", "2025 voorraden 58095 (was 41861); tick1452; primary official NBB WVV"),
    ("bud_clmb_strecv_2025", "2025", "208485", "2025 ST vorderingen 208485 (was 289550); tick1452; primary official NBB WVV"),
    ("bud_clmb_trade_2025", "2025", "199485", "2025 handelsvorderingen 199485 (was 276993); tick1452; primary official NBB WVV"),
    ("bud_clmb_othrecv_2025", "2025", "9000", "2025 overige vorderingen 9000 (was 12557); tick1452; primary official NBB WVV"),
    ("bud_clmb_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty; tick1452; primary official NBB WVV"),
    ("bud_clmb_cash_2025", "2025", "642128", "2025 liquide middelen 642128 JUMP (was 201518); tick1452; primary official NBB WVV"),
    ("bud_clmb_prepaid_2025", "2025", "0", "2025 prepaid empty; tick1452; primary official NBB WVV"),
    ("bud_clmb_equity_2025", "2025", "-45030", "2025 EV -45030 (was -79944); alarmbel art 6:119; tick1452; primary official NBB WVV"),
    ("bud_clmb_inbreng_2025", "2025", "18600", "2025 inbreng onbeschikbaar 18600; tick1452; primary official NBB WVV"),
    ("bud_clmb_reserves_2025", "2025", "1860", "2025 statutair onbeschikbare reserves 1860; tick1452; primary official NBB WVV"),
    ("bud_clmb_overgedragen_2025", "2025", "-65490", "2025 overgedragen -65490 (was -100404); tick1452; primary official NBB WVV"),
    ("bud_clmb_debt_2025", "2025", "956910", "2025 schulden 956910 JUMP (was 612873; LT empty); tick1452; primary official NBB WVV"),
    ("bud_clmb_stdebt_2025", "2025", "932935", "2025 ST schulden 932935 (was 603142); tick1452; primary official NBB WVV"),
    ("bud_clmb_lev_2025", "2025", "115753", "2025 leveranciers 115753 (was 102103); tick1452; primary official NBB WVV"),
    ("bud_clmb_tax_2025", "2025", "7784", "2025 belastingen 450/3 7784 (was 330); tick1452; primary official NBB WVV"),
    ("bud_clmb_bezold_2025", "2025", "42080", "2025 bezoldigingen 454/9 42080 (was 24685); tick1452; primary official NBB WVV"),
    ("bud_clmb_othdebt_2025", "2025", "767318", "2025 overige schulden 767318 JUMP (was 476024); tick1452; primary official NBB WVV"),
    ("bud_clmb_deferred_2025", "2025", "23975", "2025 deferred 23975 (was 9731); tick1452; primary official NBB WVV"),
    ("bud_clmb_bruto_2025", "2025", "388600", "2025 brutomarge 9900 388600 JUMP (was 153973); tick1452; primary official NBB WVV"),
    ("bud_clmb_omzet_2025", "2025", "0", "2025 omzet 70 empty (MIC-inb); tick1452; primary official NBB WVV"),
    ("bud_clmb_diensten_2025", "2025", "0", "2025 60/61 empty (MIC-inb); tick1452; primary official NBB WVV"),
    ("bud_clmb_pers_2025", "2025", "352382", "2025 pers 62 352382 / 100 = 4.2 VTE (was 202193 / 3.2); tick1452; primary official NBB WVV"),
    ("bud_clmb_afschr_2025", "2025", "28", "2025 afschrijvingen 630 28; tick1452; primary official NBB WVV"),
    ("bud_clmb_andere_2025", "2025", "400", "2025 andere bedrijfskosten 640/8 400 (was 387); tick1452; primary official NBB WVV"),
    ("bud_clmb_expl_2025", "2025", "35790", "2025 expl 35790 (was -48607); tick1452; primary official NBB WVV"),
    ("bud_clmb_finopbr_2025", "2025", "285", "2025 fin opbr 285 all recurrent (was 153); tick1452; primary official NBB WVV"),
    ("bud_clmb_finkost_2025", "2025", "1161", "2025 fin kosten 1161 all recurrent (was 1160); tick1452; primary official NBB WVV"),
    ("bud_clmb_pnl_2025", "2025", "34914", "2025 PnL 34914 (was -49615); tick1452; primary official NBB WVV"),
    ("bud_clmb_div_2025", "2025", "0", "2025 dividend 0; 694/7 empty; tick1452; primary official NBB WVV"),
    ("bud_clmb_capex_2025", "2025", "3200", "2025 capex MVA aanschaf 8169 3200; IVA/FVA empty; tick1452; primary official NBB WVV"),
    ("bud_clmb_parentsteun_2025", "2025", "110000", "2025 steun meerderheidsaandeelhouder Bosgroep Limburg VZW 110000 (alarmbel verslag); tick1452; primary official NBB WVV bijzonder verslag"),
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
    f"{COMM},Cooeperatieve van de Limburgse Bosgroepen CV JR2025 leftover Bosgroep daughter dual (bruto 0.39m / pers 0.35m / cash JUMP 0.64m / neg EV alarmbel),{ENT},Cooeperatieve van de Limburgse Bosgroepen CV / mined Limburg cities,WVV CV; official NBB MIC-inb; provincie Limburg,2026-03-09,2007,,388600,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00244195.pdf,Local leftover Bosgroep-daughter map VL CoLimBo — bruto 0.39m / pers 0.35m / cash JUMP 0.64m / neg EV,Publish omzet empty + pers 0.35m + 4.2 VTE + cash JUMP + other-debt JUMP + neg EV alarmbel + parent steun 110k + 1 VE + vennoten share-pct; do not keep leftover CoLimBo CV as dual unpublished vehicle,{SRC},strong,Vlaanderen>Limburg>CoLimBo>JR2025_L5,tick1452; assets 911880 omzet empty diensten empty pers 352382 4.2 VTE pnl 34914 equity -45030 cash 642128 debt 956910 capex 3200 dividend 0 bruto 388600; FOI ready not sent; not TE-additive of 348bn; NOT Bosgroep Limburg VZW / Koepel / RL Kempen en Maasland / RL Lage Kempen",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"{LB},Cooeperatieve van de Limburgse Bosgroepen CV JR2025 leftover Bosgroep daughter: omzet empty / pers 0.35m / cash JUMP 0.64m / neg EV alarmbel,L5,local_budget_line,Vlaanderen>Limburg>CoLimBo>JR2025_L5,388600,911880,Leftover dual Bosgroep-daughter CV: assets 0.91m / equity -45k alarmbel / pnl +35k / omzet empty / 60-61 empty / pers 0.35m 4.2 VTE / cash 0.64m JUMP / debt 0.96m JUMP / dividend 0 / NBB 2026-00244195,strong,{SRC},Cooeperatieve van de Limburgse Bosgroepen CV / mined Limburg cities,Local leftover Bosgroep-daughter map VL CoLimBo — JR2025 NBB WVV live; omzet/pers/neg-EV FOI,Official NBB WVV 2026-08-19: bruto 0.39m / pers 0.35m / cash JUMP 0.64m / PnL +35k / neg EV alarmbel,7.4,6.8,2.5,7.0,Publish omzet empty + pers 0.35m + 4.2 VTE + cash JUMP + other-debt JUMP + neg EV alarmbel + parent steun 110k + 1 VE + vennoten share-pct; do not keep leftover CoLimBo CV as dual unpublished vehicle,active,,tick1452; leftover Bosgroep daughter after leftover AGB/IGS/Bosgroep VZW hunt; FOI ready not sent; not TE-additive of 348bn; distinct from leftover Bosgroep Limburg VZW / leftover Koepel / already-mined RL Kempen en Maasland 1433 / already-mined RL Lage Kempen 1430",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Limburg>CoLimBo>JR2025_L5,{ENT},omzet 70 empty + 60/61 empty + bruto 388600 JUMP vs 153973 + pers 62 352382 4.2 VTE vs 202193 3.2 + 1 VE + cash 642128 JUMP vs 201518 + other debt JUMP 767318 vs 476024 + debt JUMP 956910 vs 612873 + equity -45030 alarmbel art 6:119 + parent VZW steun 110000 + capex 3200 + vennoten share-pct unpublished + relation to Bosgroep Limburg VZW/Koepel/RLKM/RLLK/provincie unpublished,Leftover CoLimBo CV after leftover AGB/IGS/Bosgroep VZW hunt: bruto 0.39m / pers 0.35m / neg EV hides public-perimeter houtverkoop vehicle,8,Cooeperatieve van de Limburgse Bosgroepen cv / Bestuursorgaan,bosgroep@limburg.be,Universiteitslaan 1 3500 Hasselt,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,{COMM},{LB},{TS},{TS},tick1452 leftover Bosgroep Limburg daughter after honest leftover AGB/IGS/Bosgroep VZW hunt; live JR2025 NBB WVV PDF now extracted (280997 bytes 14p). FOI ready not sent. NOT every-10. NOT Bosgroep Limburg VZW / Koepel / RL Kempen en Maasland / RL Lage Kempen. Leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no JR. Leftover IGS IVAREM 0267.403.264 still JR2024 (NBB year-end 31/12/2024). Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92 still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening. AGB Bornem still 2024 HEAD 403.",
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
if not last_s.startswith("rq_1452,"):
    raise SystemExit(f"expected last row rq_1452, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1452 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1452,CoLimBo JR2025 leftover dual residual,hole_fill,5,done,L5,cv_clmb,"
    "Completed: Cooeperatieve van de Limburgse Bosgroepen CV leftover Bosgroep Limburg daughter / houtverkoop CV of mined Limburg cities after leftover AGB/IGS/Bosgroep VZW hunt; KBO 0890.220.171 Actief; live JR2025 official NBB WVV MIC-inb PDF (280997 bytes 14p deposit 2026-00244195; AV 09.03.2026; header 01.07.2026; created 03.07.2026; no commissaris listed); sourced euros assets 911880 omzet empty diensten empty pers 352382 4.2 VTE pnl 34914 equity -45030 cash 642128 debt 956910 capex 3200 dividend 0 bruto 388600; FOI ready omzet empty / pers 0.35m / cash JUMP / other-debt JUMP / neg EV alarmbel / 1 VE / vennoten share-pct; NOT Bosgroep Limburg VZW / Koepel / RL Kempen en Maasland / RL Lage Kempen,"
    f"{GAP},2026-08-19T13:40:00Z,{TS},"
    "tick1452 CoLimBo leftover Bosgroep daughter residual; KBO 0890.220.171; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1453 leftover AGB/Bosgroep VZW if CDN live else IVAREM if JR2025 statutory / leftover IOED/cultuur-IGS/Hart"
)
spawn = (
    "rq_1453,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1452 done including CoLimBo 1452 leftover Bosgroep daughter live NBB WVV / Regionaal Landschap Houtland 1451 leftover IGS live NBB WVV / Bosgroep Kempen Noord 1450 leftover IGS live NBB WVV + every-10 / Bosgroep Zuiderkempen 1449 leftover IGS live NBB WVV / Bosgroep Antwerpse Gordel 1448 leftover IGS live NBB WVV / Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 only if a 2025 CDN is live (still no JR as of 1452); leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS IVAREM 0267.403.264 still JR2024 as of 1452 (NBB year-end 31/12/2024) — take if a true JR2025 statutory PDF now downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening; leftover IGS Zender 0822.146.066 last JR still 2024; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening; leftover IGS Dijk92 0806.383.071 last JR still 2024; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined CoLimBo 1452 / Regionaal Landschap Houtland 1451 / Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL West-Vlaamse Hart still no jaarrekening; IVAREM still JR2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1452 after CoLimBo leftover Bosgroep daughter live NBB WVV JR2025; leftover AGB/Bosgroep VZW if CDN live else IVAREM if JR2025 statutory / leftover IOED/cultuur-IGS/Hart"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1452=done + rq_1453 spawned; keep", last_line_start)

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
    f"tick1452 CoLimBo leftover Bosgroep Limburg daughter residual; KBO 0890.220.171; live JR2025 NBB WVV PDF; sourced euros assets 911880 omzet empty diensten empty pers 352382 4.2 VTE pnl 34914 equity -45030 cash 642128 debt 956910 capex 3200 dividend 0 bruto 388600; FOI ready omzet empty / pers 0.35m / cash JUMP / other-debt JUMP / neg EV alarmbel / 1 VE; NOT Bosgroep Limburg VZW / Koepel / RLKM / RLLK; next rq_1453 leftover AGB/Bosgroep VZW if CDN live else IVAREM if JR2025 statutory / leftover IOED/cultuur-IGS/Hart; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1452,1452,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1452")

entry = (
    "\n## Tick 1452 - 2026-08-19 - rq_1452 CoLimBo dual residual leftover\n"
    "- Unit: Cooeperatieve van de Limburgse Bosgroepen CV / CoLimBo (leftover Bosgroep Limburg daughter / houtverkoop CV of mined Limburg cities; 1 VE) after residual dual hunt (KBO **0890.220.171**; official bosgroep.limburg.be; live official NBB WVV MIC-inb PDF **280997** bytes / 14p; deposit **2026-00244195**; AV **09.03.2026**; header **01.07.2026**; pdfinfo created **03.07.2026**; model **MIC-inb** 23.0.10 m87-f; no commissaris listed; MIC-inb 6.1.1/6.1.3/6.2/6.3/6.4/6.6/7/8/9/10/12-16 not filed; 6.1.2 MVA + 6.5 blank + 11 sociale balans + alarmbel bijzonder verslag 26.02.2026 filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; Zwevegem/Rotselaar already mined. Leftover IGS IVAREM 0267.403.264 NBB consult still year-end **31/12/2024** (2025-00494826 correction / 2025-00188050 initial) — no JR2025 statutory PDF; official ivarem.be BAV 19-06-2025 is JR2024 approval; Belscope still Jaarrekening 2024; not taken. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen this tick: WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Koepel 0820.176.768 still no jaarrekening (Koepel NBB No results). Leftover CoLimBo statutory NBB WVV deposit `2026-00244195` live this tick (official MIC-inb PDF 280997 / 14p; SBM CDN HTTP 200; jaar **2025-12-31**) — taken (hunt order #2 leftover Bosgroep daughter after leftover AGB/IGS/Bosgroep VZW). Distinct from leftover **Bosgroep Limburg VZW** (KBO 0668.619.317; same Universiteitslaan 1 3500 address; bestuurder of this CV since 15.12.2016 — NOT this entity) / leftover **Koepel** 0820.176.768 / already-mined **RL Kempen en Maasland** (vzw_rlkm tick 1433) / already-mined **RL Lage Kempen** 1430. First confirmed not already extracted as JR2025 euros: no CoLimBo / 0890.220.171 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **20.06.2007**; statutaire naam Cooeperatieve van de Limburgse Bosgroepen since 14.06.2007; CV since 17.11.2023 (was CVBA); zetel Universiteitslaan 1 3500 Hasselt since 01.01.2025; **1 VE**; official site https://bosgroep.limburg.be/; contact bosgroep@limburg.be; tel 011 23 83 63; NACE btw 02.400 / 02.100 / 02.200; Werkgever RSZ since 01.01.2016; **6 functiehouders**. PDF bestuurders Cryns / Smeets / Coolens / Vandezande / Bosgroep Limburg VZW + vast vertegenwoordiger Rooyackers. Named vennoten share-% unpublished. Contact bosgroep@limburg.be. Prior-year figures identical. NBB consult SPA/timeout; SBM HTML IP-blacklisted from box curl; SBM CDN HTTP 200 this tick. Euros extracted from the official MIC-inb deposit PDF itself. Belscope/Companyweb/Busibee euros not used. Not every-10 (next 1460 MUST do every-10).\n"
    "- EUR strong (primary official WVV MIC-inb; **omzet 70 empty**; **60/61 empty**; pers 62 **352382** / **4,2 VTE** vs 202193 / 3,2): assets **911880** (was 532929); fixed **3172** vs 0 / IVA empty / MVA **3172** (installaties **3172**) / FVA empty; current **908708** vs 532929; voorraden **58095** vs 41861; ST recv **208485** vs 289550 (trade **199485** vs 276993 / other **9000** vs 12557); geldbeleg empty; cash **642128 JUMP** vs 201518; prepaid empty; equity **-45030** (inbreng **18600**; reserves **1860**; overgedragen **-65490**); voorzieningen empty; schulden **956910 JUMP** vs 612873 (LT empty; ST **932935** vs 603142 waarvan leveranciers **115753** vs 102103 + tax **7784** vs 330 + bezold **42080** vs 24685 + overige **767318 JUMP** vs 476024; deferred **23975** vs 9731); brutomarge **388600 JUMP** vs 153973; omzet empty; 60/61 empty; pers **352382** / **4,2 VTE** / 7308 uur / YE **5**; afschr **28**; andere **400**; expl **+35790** vs -48607; fin opbr **285** all recurrent; fin kosten **1161**; tax empty; PnL **+34914** vs -49615; dividend **0**; over te dragen **-65490**; capex **3200** (MVA aanschaf only). PDF cross-checks: 3172+908708=911880; -45030+956910=911880; 388600-352382-28-400=35790; 35790+285-1161=34914; 34914-100404=-65490. Alarmbel art. 6:119: negatief EV -45030; parent VZW steun 110000; continuiteit niet ontbinding.\n"
    f"- CSVs: sources +4; entities +1 `cv_clmb` parent `sec_flanders`; budgets +{{inv_budgets_added}} executed; commitments +1 envelope 388600 AV 09.03.2026; leaderboard +1 annual 388600 / total 911880; foi_queue +1 status=ready never sent; research_queue surgical rq_1452=done + rq_1453 spawn; loop_state ticks_completed=1452. Inventory after write: budgets {{inv_budgets}} · commitments {{inv_commitments}} · leaderboard {{inv_leaderboard}} · entities {{inv_entities}} · sources {{inv_sources}} · FOI ready {{foi_ready}} / answered {{foi_ans}} / partial {{foi_part}} / total {{foi_tot}}.\n"
    "- FOI: `gap_clmb_omzet_empty_bruto_0_39m_pers_0_35m_neg_ev_l5` ready not sent — omzet empty / 60-61 empty / bruto 0.39m / pers 0.35m 4.2 VTE / cash JUMP 0.64m / other-debt JUMP 0.77m / debt JUMP 0.96m / neg EV alarmbel / parent steun 110k / expl +36k / pnl +35k / 1 VE / capex 3.2k / vennoten share-pct / relation to Bosgroep Limburg VZW / Koepel / RLKM / RLLK / provincie unpublished.\n"
    "- Next: rq_1453 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep WVL Houtland **0866.482.291** / IJzer en Leie **0816.706.346** / Limburg **0668.619.317** / Koepel **0820.176.768** only if a 2025 CDN is live (still no JR this tick). Leftover IGS IVAREM **0267.403.264** still JR2024 (NBB year-end 31/12/2024) — take only if a true JR2025 statutory PDF now downloads. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined CoLimBo 1452 / Regionaal Landschap Houtland 1451 / Bosgroep Kempen Noord 1450 / Bosgroep Zuiderkempen 1449 / Bosgroep Antwerpse Gordel 1448 / Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022. Next every-10 is 1460.\n"
)
entry = entry.replace("{inv_budgets_added}", str(len(added))).replace("{inv_budgets}", str(inv["budgets.csv"])).replace("{inv_commitments}", str(inv["commitments.csv"])).replace("{inv_leaderboard}", str(inv["leaderboard.csv"])).replace("{inv_entities}", str(inv["entities.csv"])).replace("{inv_sources}", str(inv["sources.csv"])).replace("{foi_ready}", str(foi_ready)).replace("{foi_ans}", str(foi_ans)).replace("{foi_part}", str(foi_part)).replace("{foi_tot}", str(foi_tot))
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1452 -" in lraw:
    raise SystemExit("loop_log already has tick 1452 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1452")
print("DONE tick 1452")
