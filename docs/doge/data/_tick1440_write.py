#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1440 surgical writes + every-10. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:10:00Z"
ENT = "vzw_rldj"
SRC = "src_rldj_jr2025_nbb"
GAP = "gap_rldj_omzet_empty_pers_0_60m_cash_0_72m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rldj_jr2025_nbb,Regionaal Landschap Dijleland VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00122942.pdf,NBB / RL Dijleland VZW,2026-08-19,budget,tick1440; VKT-VZW 23.0.9 m04-f PDF 11p / 45482 bytes deposit 2026-00122942; AV 26.03.2026; header 26.05.2026; pdfinfo 28.05.2026; KBO 0461.935.675; assets 803646 cash 722390 debt 79146 brutomarge 822487 omzet empty code73 empty code60_61 empty pers 602168 pnl 225592; no commissaris listed",
    "src_rldj_site,Regionaal Landschap Dijleland official site,https://www.rld.be/,RL Dijleland VZW,2026-08-19,official_register,tick1440; leftover IGS / regionaal landschap of 13 Dijleland cities; zetel Witte Bomendreef 1 3050 Oud-Heverlee; contact info@rld.be; tel +32 (0)460 94 97 36; voorzitter Eerlingen Tine; Streekhuis Dijleland",
    "src_kbo_rldj_0461935675,KBO Regionaal Landschap Dijleland 0461.935.675,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461935675,KBO Public Search FOD Economie,2026-08-19,official_register,tick1440; Actief since 03.10.1997; naam since 03.10.1997; afkorting RLD since 03.10.1997; zetel Witte Bomendreef 1 3050 Oud-Heverlee since 26.03.2021; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 01.01.1998",
    "src_rldj_foi_contact,RL Dijleland FOI channel (info@rld.be; Witte Bomendreef 1 Oud-Heverlee),https://www.rld.be/contact,RL Dijleland VZW,2026-08-19,official_register,tick1440; 13 member cities + provincie Vlaams-Brabant; voorzitter Eerlingen Tine; NOT IGO Holsbeek; NOT Erfgoed Druivenstreek",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rldj," in raw or raw.startswith(b"vzw_rldj,"):
    raise SystemExit("vzw_rldj already present")
if b"0461.935.675" in raw or b"0461935675" in raw:
    raise SystemExit("RL Dijleland KBO already present")
row = (
    "vzw_rldj,Regionaal Landschap Dijleland VZW (leftover IGS / regionaal landschap of 13 mined Dijleland cities; NOT IGO Holsbeek; NOT Erfgoed Druivenstreek),"
    "Regionaal Landschap Dijleland ASBL (IGS residuel / paysage regional Dijleland),"
    "Regionaal Landschap Dijleland leftover IGS / regional landscape VZW of 13 Dijleland municipalities (not IGO Holsbeek),"
    "other,sec_flanders,nl,https://www.rld.be/,info@rld.be,Witte Bomendreef 1 3050 Oud-Heverlee,"
    "tick1440 leftover residual IGS VZW of mined Dijleland cities after leftover AGB hunt; KBO 0461.935.675 Actief since 03.10.1997; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 803646 omzet empty diensten empty pers 602168 pnl 225592 equity 613332 cash 722390 debt 79146 capex 3456 dividend 0 brutomarge 822487; FOI ready omzet empty / 73 empty / 60-61 empty / pers 0.60m / cash 0.72m JUMP / lev DROP / pens 0.11m; distinct from already-mined IGO Holsbeek 1409 / Hofheide 1395 / EcoWerf 1357 / AG Museum Leuven / AGB Haacht / AGB Boortmeerbeek / AGB De Kouter Herent / Erfgoed Druivenstreek 1422 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rldj")

# --- budgets ---
BUDGETS = [
    ("bud_rldj_assets_2025", "2025", "803646", "2025 assets 803646 VKT-VZW 20/58; tick1440; primary official NBB WVV"),
    ("bud_rldj_assets_2024", "2024", "640250", "2024 assets 640250 comparative; tick1440; primary official NBB WVV 20/58"),
    ("bud_rldj_fixed_2025", "2025", "21846", "2025 vaste activa 21846 vs 18390; tick1440; primary official NBB WVV 21/28"),
    ("bud_rldj_iva_2025", "2025", "0", "2025 IVA empty (section 6.1.1 not filed); tick1440; primary official NBB WVV 21"),
    ("bud_rldj_mva_2025", "2025", "0", "2025 MVA empty (section 6.1.2 not filed); tick1440; primary official NBB WVV 22/27"),
    ("bud_rldj_fva_2025", "2025", "21846", "2025 FVA 21846 vs 18390; tick1440; primary official NBB WVV 28"),
    ("bud_rldj_fva_2024", "2024", "18390", "2024 FVA 18390 comparative; tick1440; primary official NBB WVV 28"),
    ("bud_rldj_current_2025", "2025", "781800", "2025 vlottend 781800 vs 621859; tick1440; primary official NBB WVV 29/58"),
    ("bud_rldj_strecv_2025", "2025", "51598", "2025 ST vorderingen 51598 vs 43321; tick1440; primary official NBB WVV 40/41"),
    ("bud_rldj_strecv_2024", "2024", "43321", "2024 ST vorderingen 43321 comparative; tick1440; primary official NBB WVV 40/41"),
    ("bud_rldj_trade_2025", "2025", "51598", "2025 handelsvorderingen 51598 vs 43321; tick1440; primary official NBB WVV 40"),
    ("bud_rldj_trade_2024", "2024", "43321", "2024 handelsvorderingen 43321 comparative; tick1440; primary official NBB WVV 40"),
    ("bud_rldj_cash_2025", "2025", "722390", "2025 liquide middelen 722390 JUMP vs 578539; tick1440; primary official NBB WVV 54/58"),
    ("bud_rldj_cash_2024", "2024", "578539", "2024 liquide middelen 578539 comparative; tick1440; primary official NBB WVV 54/58"),
    ("bud_rldj_prepaid_2025", "2025", "7811", "2025 prepaid 7811 (was empty); tick1440; primary official NBB WVV 490/1"),
    ("bud_rldj_equity_2025", "2025", "613332", "2025 EV 613332 vs 387740; tick1440; primary official NBB WVV 10/15"),
    ("bud_rldj_equity_2024", "2024", "387740", "2024 EV 387740 comparative; tick1440; primary official NBB WVV 10/15"),
    ("bud_rldj_fondsen_2025", "2025", "35858", "2025 fondsen 35858 unchanged; tick1440; primary official NBB WVV 10"),
    ("bud_rldj_overgedragen_2025", "2025", "577474", "2025 overgedragen winst 577474 vs 351882; tick1440; primary official NBB WVV 14"),
    ("bud_rldj_voorz_2025", "2025", "111168", "2025 voorzieningen 111168 (pensioenen 111168 unchanged); tick1440; primary official NBB WVV 16"),
    ("bud_rldj_pens_2025", "2025", "111168", "2025 pensioenvoorziening 111168 unchanged; tick1440; primary official NBB WVV 160"),
    ("bud_rldj_debt_2025", "2025", "79146", "2025 schulden 79146 DROP vs 141341 (LT empty); tick1440; primary official NBB WVV 17/49"),
    ("bud_rldj_debt_2024", "2024", "141341", "2024 schulden 141341 comparative; tick1440; primary official NBB WVV 17/49"),
    ("bud_rldj_stdebt_2025", "2025", "79146", "2025 ST schulden 79146 vs 141341; tick1440; primary official NBB WVV 42/48"),
    ("bud_rldj_lev_2025", "2025", "26783", "2025 leveranciers 26783 DROP vs 79593; tick1440; primary official NBB WVV 440/4"),
    ("bud_rldj_lev_2024", "2024", "79593", "2024 leveranciers 79593 comparative; tick1440; primary official NBB WVV 440/4"),
    ("bud_rldj_bezold_2025", "2025", "52162", "2025 bezoldigingen/sociale lasten 52162 vs 61649; tick1440; primary official NBB WVV 454/9"),
    ("bud_rldj_othdebt_2025", "2025", "200", "2025 overige schulden 200 vs 100; tick1440; primary official NBB WVV 48"),
    ("bud_rldj_brutomarge_2025", "2025", "822487", "2025 brutomarge 822487 vs 693405; omzet 70 empty; 73 empty; 60/61 empty; tick1440; primary official NBB WVV 9900"),
    ("bud_rldj_brutomarge_2024", "2024", "693405", "2024 brutomarge 693405 comparative; tick1440; primary official NBB WVV 9900"),
    ("bud_rldj_pers_2025", "2025", "602168", "2025 pers 602168 / 6.9 VTE vs 585454 / 6.8; tick1440; primary official NBB WVV 62"),
    ("bud_rldj_pers_2024", "2024", "585454", "2024 pers 585454 / 6.8 VTE comparative; tick1440; primary official NBB WVV 62"),
    ("bud_rldj_expl_2025", "2025", "220319", "2025 expl +220319 vs +107951; tick1440; primary official NBB WVV 9901"),
    ("bud_rldj_expl_2024", "2024", "107951", "2024 expl +107951 comparative; tick1440; primary official NBB WVV 9901"),
    ("bud_rldj_finopbr_2025", "2025", "5834", "2025 fin opbr 5834 vs 848; tick1440; primary official NBB WVV 75/76B"),
    ("bud_rldj_finkost_2025", "2025", "561", "2025 fin kosten 561 vs 567; tick1440; primary official NBB WVV 65/66B"),
    ("bud_rldj_pnl_2025", "2025", "225592", "2025 PnL +225592 vs +108232; tick1440; primary official NBB WVV 9904"),
    ("bud_rldj_pnl_2024", "2024", "108232", "2024 PnL +108232 comparative; tick1440; primary official NBB WVV 9904"),
    ("bud_rldj_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1440; primary official NBB WVV"),
    ("bud_rldj_capex_2025", "2025", "3456", "2025 FVA aanschaffingen 3456; IVA/MVA sections not filed; tick1440; primary official NBB WVV 8365"),
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
    f"comm_rldj_jr2025_bruto,Regionaal Landschap Dijleland VZW JR2025 leftover IGS dual (brutomarge 0.82m / pers 0.60m / cash 0.72m),{ENT},RL Dijleland VZW / 13 Dijleland cities,WVV VZW; NBB neerlegging; 13 Dijleland gemeenten + provincie Vlaams-Brabant,2026-03-26,1997,,822487,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00122942.pdf,Local leftover IGS map VL Dijleland landschap — 0.82m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 0.60m,Publish empty 70/73/60-61 split + pers 0.60m + cash JUMP + lev DROP + pens 0.11m + vennoten share-pct; do not keep leftover RLD VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>Dijleland>RLD>JR2025_L5,tick1440; assets 803646 omzet empty diensten empty pers 602168 pnl 225592 equity 613332 cash 722390 debt 79146 capex 3456 dividend 0 brutomarge 822487; FOI ready not sent; not TE-additive of 348bn; NOT IGO Holsbeek; every-10",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rldj_omzet_empty_pers_0_60m_cash_0_72m,Regionaal Landschap Dijleland VZW JR2025 leftover IGS: empty omzet 70 / pers 0.60m / cash 0.72m / brutomarge 0.82m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>Dijleland>RLD>JR2025_L5,822487,803646,Leftover dual IGS VZW: assets 0.80m / equity 0.61m / pnl +0.23m / omzet empty / 73 empty / 60-61 empty / pers 0.60m 6.9 VTE / cash 0.72m JUMP / debt 0.08m DROP / lev 0.03m DROP / pens 0.11m / dividend 0,strong,{SRC},RL Dijleland VZW / 13 Dijleland cities,Local leftover IGS map VL Dijleland landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 0.82m / pers 0.60m / cash 0.72m / PnL +0.23m,6.6,6.4,2.2,6.2,Publish empty 70/73/60-61 split + pers 0.60m + cash JUMP + lev DROP + pens 0.11m + vennoten share-pct; do not keep leftover RLD VZW as dual unpublished vehicle,active,,tick1440 every-10; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IGO Holsbeek 1409 / Hofheide 1395 / EcoWerf 1357 / Erfgoed Druivenstreek 1422 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>Dijleland>RLD>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 822487 + pers 62 602168 / 6.9 VTE + cash JUMP 722390 vs 578539 + leveranciers DROP 26783 vs 79593 + debt DROP 79146 vs 141341 + pens 111168 + prepaid 7811 + FVA aanschaf 3456 + vennoten share-pct unpublished + commissaris unpublished + 1 VE unpublished + relation to IGO Holsbeek unpublished,Leftover RLD VZW after leftover AGB hunt: 0.82m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Dijleland vzw / Bestuursorgaan,info@rld.be,Witte Bomendreef 1 3050 Oud-Heverlee,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rldj_jr2025_bruto,lb_rldj_omzet_empty_pers_0_60m_cash_0_72m,{TS},{TS},tick1440 leftover IGS after honest leftover AGB hunt + every-10; live JR2025 official NBB WVV VKT-VZW PDF now extracted (45482 bytes 11p deposit 2026-00122942). FOI ready not sent. NOT IGO Holsbeek. NOT Erfgoed Druivenstreek. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL de Voorkempen JR2025 CDN 2026-00054608 live leftover for next (NOT Erfgoed Voorkempen IOED 1425).",
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
if not last_s.startswith("rq_1440,"):
    raise SystemExit(f"expected last row rq_1440, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1440 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1440,RL Dijleland JR2025 leftover dual residual + progress,hole_fill,5,done,L5,vzw_rldj,"
    "Completed: Regionaal Landschap Dijleland VZW leftover IGS / regionaal landschap of 13 mined Dijleland cities after leftover AGB hunt; KBO 0461.935.675 Actief; live JR2025 official NBB WVV VKT-VZW PDF (45482 bytes 11p deposit 2026-00122942; AV 26.03.2026; header 26.05.2026; created 28.05.2026; no commissaris listed); sourced euros assets 803646 omzet empty diensten empty pers 602168 pnl 225592 equity 613332 cash 722390 debt 79146 capex 3456 dividend 0 brutomarge 822487; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.60m / cash 0.72m JUMP / lev DROP / pens 0.11m; NOT IGO Holsbeek; EVERY-10 progress refresh,"
    f"{GAP},2026-08-19T12:00:00Z,{TS},"
    "tick1440 RL Dijleland VZW leftover IGS residual + every-10; KBO 0461.935.675; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1441 residual dual L5 VL leftover RL de Voorkempen if 2025 CDN still live"
)
spawn = (
    "rq_1441,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1440 done including RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL de Voorkempen 0898.729.546 JR2025 CDN 2026-00054608 LIVE leftover — STRONG next leftover RL (NOT Erfgoed Voorkempen IOED 1425); leftover RL Brabantse Kouters VZW 0874.904.564 JR2025 CDN 2026-00321333 live leftover (NOT Erfgoed Brabantse Kouters IOED 1428 / KBO 0741.478.094); leftover RL Meetjesland & Leievallei 0466.277.515 JR2025 CDN 2026-00092026 live leftover (NOT Cultuuroverleg Meetjesland 1416); leftover RL Haspengouw & Voeren 0471.371.597 JR2025 CDN 2026-00070056 live leftover; leftover RL Kleine & Grote Nete 0810.764.897 JR2025 CDN 2026-00054598 live leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1440 after RL Dijleland leftover IGS live NBB WVV + every-10; next residual dual L5 VL leftover RL de Voorkempen if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1440=done + rq_1441 spawned; keep", last_line_start)

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
    f"tick1440 RL Dijleland leftover IGS residual + every-10; KBO 0461.935.675; live JR2025 NBB WVV PDF; sourced euros assets 803646 omzet empty diensten empty pers 602168 pnl 225592 equity 613332 cash 722390 debt 79146 capex 3456 dividend 0 brutomarge 822487; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.60m / cash 0.72m JUMP / lev DROP / pens 0.11m; NOT IGO Holsbeek; next rq_1441 residual dual L5 VL leftover RL de Voorkempen if 2025 CDN still live; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1440,1440,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1440")

# --- every-10 progress_every_10_ticks.md ---
snap = f"""## Snapshot at **tick 1440** (2026-08-19)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1431-1440 leftover IGS: **Rupelstreek** · **RL Schelde-Durme** · **RLKM** · **RLZH** · **RLRL** · **RLPZ** · **RLVAD** · **RL Westhoek** · **RL Noord-Hageland** · **RL Dijleland** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1431-1440 is VL residual dual L5 leftover IGS (not near-complete of 348bn):** **RLKM** assets **4.74m** · **RL Schelde-Durme** assets **1.75m** · **RL Westhoek** assets **1.74m** · **RLRL** assets **1.62m** · **RLZH** assets **1.08m** · **RLPZ** assets **1.06m** · **RLVAD** assets **0.87m** · **RL Noord-Hageland** assets **0.84m** · **RL Dijleland** assets **0.80m** · **Rupelstreek** assets **0.06m** · prior leftover IGS/AGB/NV/Fluvius stack retained |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek/klimaat-holding/energy-DSO/zorg/cultuur/landschap shells** (**NEW RL Dijleland** assets **EUR0.80m** brutomarge **EUR0.82m** pers **EUR0.60m** cash JUMP **EUR0.72m** · **RL Noord-Hageland** assets **EUR0.84m** · **RL Westhoek** assets **EUR1.74m** · **RLVAD** assets **EUR0.87m** · **RLPZ** assets **EUR1.06m** · **RLRL** assets **EUR1.62m** · **RLZH** assets **EUR1.08m** · **RLKM** assets **EUR4.74m** · **RL Schelde-Durme** assets **EUR1.75m** · **Rupelstreek** assets **EUR0.06m** · prior leftover RL Lage Kempen 0.08m / Kusterfgoed 0.16m / Brabantse Kouters 0.20m / Denderland 0.45m / Noorderkempen 0.48m / Voorkempen 0.62m / Zuidwest 0.95m / BIONERGA LOGISTICS 3.51m / Druivenstreek 0.05m / Viertoren 0.21m / CO7 0.69m / de Merode 0.37m / Kluize 5.83m / IOK Afvalbeheer 70.50m / Sunfin 6.29m / MLSO 227.28m / Fluvius DNB + IGS stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs Fluvius EG possible on DSO holdings.**

### Inventory (tick 1440)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {inv['budgets.csv']} |
| commitments.csv | {inv['commitments.csv']} |
| leaderboard.csv | {inv['leaderboard.csv']} |
| entities.csv | {inv['entities.csv']} |
| sources.csv | {inv['sources.csv']} |
| FOI ready | {foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | {foi_tot} |
| research_queue open | rq_116 deferred + rq_1441 hole-fill after progress |

### What improved since tick 1430

- **VL residual dual JR2025 leftover IGS (tick1431-1439):** **RLKM** assets **4.74m** · **RL Schelde-Durme** assets **1.75m** · **RL Westhoek** assets **1.74m** · **RLRL** assets **1.62m** · **RLZH** assets **1.08m** · **RLPZ** assets **1.06m** · **RLVAD** assets **0.87m** · **RL Noord-Hageland** assets **0.84m** · **Rupelstreek** assets **0.06m** — no invented euros.
- **NEW (tick1440):** **Regionaal Landschap Dijleland VZW** (KBO 0461.935.675) leftover IGS / regionaal landschap of 13 mined Dijleland municipalities. Official NBB WVV VKT-VZW deposit **2026-00122942** PDF (45482 bytes / 11p; AV 26.03.2026; header 26.05.2026; created 28.05.2026). Assets **803.646** · brutomarge **822.487** (omzet 70 empty; 73 empty; 60/61 empty) · pers **602.168** / **6,9 VTE** · cash **722.390 JUMP** vs 578539 · leveranciers **26.783 DROP** vs 79593 · debt **79.146 DROP** vs 141341 · pensioenvoorziening **111.168** · PnL **+225.592**. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover landschap IGS** (RL Dijleland 0.80m / RLNH 0.84m / RLWH 1.74m / RLVAD 0.87m / RLPZ 1.06m / RLRL 1.62m / RLZH 1.08m / RLKM 4.74m / RL Schelde-Durme 1.75m / Rupelstreek 0.06m) · prior leftover cultuur IGS + leftover waste daughter + leftover AGB + Nuhma + Fluvius DNB stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10. Not TE-additive of ~348bn.

"""

prog = DATA / "progress_every_10_ticks.md"
ptxt = prog.read_text(encoding="utf-8")
marker = "## Snapshot at **tick 1430**"
if marker not in ptxt:
    raise SystemExit("progress file missing tick 1430 marker")
if "## Snapshot at **tick 1440**" in ptxt:
    raise SystemExit("tick 1440 snapshot already present — concurrent?")
ptxt = ptxt.replace(marker, snap + marker, 1)
prog.write_text(ptxt, encoding="utf-8")
print("progress_every_10_ticks.md prepended tick 1440 snapshot")

# --- every-10 waste top10 ---
waste = DATA / "doge_waste_top10_current.md"
wtxt = waste.read_text(encoding="utf-8")
wtxt = wtxt.replace(
    "**As-of:** tick **1420** (2026-08-19) · **7223** leaderboard rows",
    f"**As-of:** tick **1440** (2026-08-19) · **{inv['leaderboard.csv']}** leaderboard rows",
    1,
)
old_stock_new = "(**NEW RL Lage Kempen** assets **€0.08m**"
new_stock_new = (
    "(**NEW RL Dijleland** assets **€0.80m** brutomarge **€0.82m** pers **€0.60m** cash JUMP **€0.72m**"
    " · **RL Noord-Hageland** assets **€0.84m** · **RL Westhoek** assets **€1.74m**"
    " · **RLVAD** assets **€0.87m** · **RLPZ** assets **€1.06m** · **RLRL** assets **€1.62m**"
    " · **RLZH** assets **€1.08m** · **RLKM** assets **€4.74m** · **RL Schelde-Durme** assets **€1.75m**"
    " · **Rupelstreek** assets **€0.06m** · **RL Lage Kempen** assets **€0.08m**"
)
if old_stock_new not in wtxt:
    raise SystemExit("waste top10 stock-filter NEW marker missing")
wtxt = wtxt.replace(old_stock_new, new_stock_new, 1)
old_change = "**Change vs tick 1420:**"
new_change = (
    "**Change vs tick 1430:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
    "Re-verified from current leaderboard: GIP 8.7 · fossil direct 8.55 · fossil accises 8.5 · company cars 8.5 · heatoil 8.43 · cheque 8.4 · CO2 SSC gap 8.4 · OAA reporté 8.4 · BCR reporté 8.4 · dual cars SSC 8.4. "
    "**Major NEW residual 1431–1440 (off pure top10 / dual):** **RLKM** assets **EUR4.74m** · **RL Schelde-Durme** assets **EUR1.75m** · **RL Westhoek** assets **EUR1.74m** · **RLRL** assets **EUR1.62m** · **RLZH** assets **EUR1.08m** · **RLPZ** assets **EUR1.06m** · **RLVAD** assets **EUR0.87m** · **RL Noord-Hageland** assets **EUR0.84m** · **RL Dijleland** assets **EUR0.80m** · **Rupelstreek** assets **EUR0.06m**. "
    "Gain is **leftover landschap IGS**. Count only NEW since 1430: Rupelstreek 1431 + RL Schelde-Durme 1432 + RLKM 1433 + RLZH 1434 + RLRL 1435 + RLPZ 1436 + RLVAD 1437 + RL Westhoek 1438 + RL Noord-Hageland 1439 + **RL Dijleland 1440**. "
    "**Prior 1421–1430 retained:** BIONERGA LOGISTICS 3.51m · Zuidwest 0.95m · Voorkempen 0.62m · Noorderkempen 0.48m · Denderland 0.45m · Viertoren 0.21m · Brabantse Kouters 0.20m · Kusterfgoed 0.16m · RL Lage Kempen 0.08m · Druivenstreek 0.05m. "
    "Not TE-additive of ~348bn. Double-count vs Fluvius EG possible on DSO holdings.\n\n"
    "<!-- prior change vs 1420 retained below as history -->\n"
    "**Change vs tick 1420:**"
)
if old_change not in wtxt:
    raise SystemExit("waste top10 change marker missing")
wtxt = wtxt.replace(old_change, new_change, 1)
old_just = "|| — | `lb_rllk_omzet_empty_bruto_0_14m_lev_0_05m` |"
# file uses | not ||
old_just = "| — | `lb_rllk_omzet_empty_bruto_0_14m_lev_0_05m` |"
new_just = (
    "| — | `lb_rldj_omzet_empty_pers_0_60m_cash_0_72m` | **0.80 m stock** | **~6.2 dual** | **NEW 1440** RL Dijleland leftover landschap IGS brutomarge 0.82m / pers 0.60m / cash JUMP 0.72m / lev DROP 0.03m / pens 0.11m |\n"
    "| — | `lb_rlnh_omzet_empty_pers_0_63m_cash_0_53m` | **0.84 m stock** | **~6.1 dual** | 1439 RL Noord-Hageland leftover IGS brutomarge 0.63m / pers 0.63m / cash 0.53m |\n"
    "| — | `lb_rlwh_omzet_empty_pers_1_28m_cash_1_24m` | **1.74 m stock** | **~6.2 dual** | 1438 RL Westhoek leftover IGS pers 1.28m / cash 1.24m |\n"
    "| — | `lb_rllk_omzet_empty_bruto_0_14m_lev_0_05m` |"
)
if old_just not in wtxt:
    raise SystemExit("waste top10 just-outside marker missing")
wtxt = wtxt.replace(old_just, new_just, 1)
waste.write_text(wtxt, encoding="utf-8")
print("doge_waste_top10_current.md refreshed tick 1440")

# --- loop_log ---
entry = (
    "\n## Tick 1440 - 2026-08-19 - rq_1440 RL Dijleland dual residual leftover + every-10\n"
    "- Unit: Regionaal Landschap Dijleland VZW / RLD (leftover IGS / regionaal landschap of 13 mined Dijleland cities; 1 VE) after residual dual hunt (KBO **0461.935.675**; official rld.be; live NBB WVV VKT-VZW deposit **2026-00122942** PDF 45482 bytes / 11p; AV **26.03.2026**; header **26.05.2026**; pdfinfo created **28.05.2026**; model **VKT-VZW** 23.0.9 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.2/6.2/6.3/6.5/6.6/6.8/7/8 not filed; 6.1.3 FVA + 6.4 + 6.7 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM IP-blacklist this tick; last known 1439: SBM last table year 2024-12-31; deposit 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Haacht / AGB Boortmeerbeek / AGB De Kouter Herent / AG Museum Leuven) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover IGS Regionaal Landschap Dijleland VZW statutory CDN live this tick (HTTP 200 / application/pdf / 45482 / 11p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined RL VZW of mined Dijleland cities with full WVV balans; STRONG next leftover RL after RL Noord-Hageland 1439). Distinct from already-mined **IGO Holsbeek** (igs_igoh tick 1409; NOT this entity) / Hofheide 1395 / EcoWerf 1357 / AG Museum Leuven / AGB Haacht / AGB Boortmeerbeek / AGB De Kouter Herent / Erfgoed Druivenstreek 1422 / Fluvius Zenne-Dijle 1389 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Dijleland / 0461.935.675 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **03.10.1997**; statutaire naam Regionaal Landschap Dijleland since 03.10.1997; afkorting RLD since 03.10.1997; VZW since 03.10.1997; zetel Witte Bomendreef 1 3050 Oud-Heverlee since 26.03.2021; **1 VE**; official site https://www.rld.be/; contact info@rld.be; tel +32 (0)460 94 97 36; Streekhuis Dijleland; NACE RSZ 91.420; Werkgever RSZ since 01.01.1998. Official site voorzitter Eerlingen Tine (Provincie Vlaams-Brabant); ondervoorzitter Hendrickx Jan; secretaris Steeno Maggy; penningmeester Verbeke Willy. Official site 13 leden-gemeenten: Bertem / Bierbeek / Boortmeerbeek / Haacht / Herent / Hoeilaart / Huldenberg / Kampenhout / Kortenberg / Leuven / Oud-Heverlee / Overijse / Tervuren. Plus provincie Vlaams-Brabant. Named share-% unpublished. Contact info@rld.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor HTML blocked this tick (IP blacklist) — PDF wins. **Every-10 progress refresh** this tick (progress_every_10_ticks.md + doge_waste_top10_current.md).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **602168** / **6,9 VTE**): assets **803646** (was 640250); fixed **21846** / IVA empty / MVA empty / FVA **21846** vs 18390; current **781800**; ST recv **51598** (trade **51598** vs 43321 / other empty); geldbeleg empty; cash **722390 JUMP** vs 578539; prepaid **7811** (was empty); equity **613332** (fondsen **35858**; overgedragen **577474**); voorzieningen **111168** (pensioenen **111168** unchanged); schulden **79146 DROP** vs 141341 (LT empty; ST **79146** waarvan leveranciers **26783 DROP** vs 79593 + soc/bezold **52162**; overige **200**); brutomarge **822487** vs 693405; omzet empty; 73 empty; 60/61 empty; pers **602168** / **6,9 VTE** / 11215 uur / YE **7,1**; expl **+220319** vs +107951; fin opbr **5834**; fin kosten **561**; tax empty; PnL **+225592** vs +108232; dividend **0**; over te dragen **577474**; capex **3456** (FVA aanschaf only).\n"
    f"- CSVs: sources +4; entities +1 `vzw_rldj` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 822487 AV 26.03.2026; leaderboard +1 annual 822487 / total 803646; foi_queue +1 status=ready never sent; research_queue surgical rq_1440=done + rq_1441 spawn; loop_state ticks_completed=1440. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_rldj_omzet_empty_pers_0_60m_cash_0_72m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 0.60m 6.9 VTE deelwerking unpublished / cash JUMP 0.72m / lev DROP 0.03m / debt DROP 0.08m / pens 0.11m / FVA aanschaf 3.5k / vennoten share-pct / relation to IGO Holsbeek unpublished / commissaris unpublished / 1 VE unpublished.\n"
    "- Every-10: refreshed progress_every_10_ticks.md (layers A–E; TE denominator EUR 347.956 bn; dual NEW since 1430: Rupelstreek 58k / RL Schelde-Durme 1.75m / RLKM 4.74m / RLZH 1.08m / RLRL 1.62m / RLPZ 1.06m / RLVAD 0.87m / RL Westhoek 1.74m / RL Noord-Hageland 0.84m / RL Dijleland 0.80m) and doge_waste_top10_current.md (pure annual top10 stable GIP #1; fossil/cars/cheque/reporté #2–10; not TE-additive of ~348bn; Fluvius EG DSO double-count possible).\n"
    "- Next: rq_1441 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL de Voorkempen **0898.729.546** JR2025 CDN **2026-00054608** LIVE — STRONG next leftover RL (NOT Erfgoed Voorkempen IOED 1425). Leftover RL Brabantse Kouters VZW 0874.904.564 CDN 2026-00321333 live (NOT Erfgoed Brabantse Kouters IOED 1428 / KBO 0741.478.094). Leftover RL Meetjesland 0466.277.515 CDN 2026-00092026 live (NOT Cultuuroverleg Meetjesland 1416). Leftover RL Haspengouw 0471.371.597 CDN 2026-00070056 live. Leftover RL Kleine & Grote Nete 0810.764.897 CDN 2026-00054598 live. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1440")
print("tick1440 writes done")
