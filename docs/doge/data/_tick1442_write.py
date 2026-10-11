#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1442 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:35:00Z"
ENT = "vzw_rlbk"
SRC = "src_rlbk_jr2025_nbb"
GAP = "gap_rlbk_omzet_empty_pers_1_35m_cash_drop_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlbk_jr2025_nbb,Regionaal Landschap Brabantse Kouters VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00321333.pdf,NBB / RL Brabantse Kouters VZW,2026-08-19,budget,tick1442; VKT-VZW 25.0.13 m04-f PDF 12p / 48192 bytes deposit 2026-00321333; AV 29.04.2026; header 23.07.2026; pdfinfo 23.07.2026; KBO 0874.904.564; assets 1461569 cash 56447 DROP debt 708837 brutomarge 1420281 omzet empty code73 empty code60_61 empty pers 1353725 pnl 69707; no commissaris listed",
    "src_rlbk_site,Regionaal Landschap Brabantse Kouters official site,https://www.brabantsekouters.be/,RL Brabantse Kouters VZW,2026-08-19,official_register,tick1442; leftover IGS / regionaal landschap of 15 Brabantse Kouters cities; zetel Houtemsesteenweg 23 1800 Vilvoorde; contact info@brabantsekouters.be; coordinator Patrick Endels; 15 gemeenten + provincie Vlaams-Brabant",
    "src_kbo_rlbk_0874904564,KBO Regionaal Landschap Brabantse Kouters 0874.904.564,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0874904564,KBO Public Search FOD Economie,2026-08-19,official_register,tick1442; Actief since 14.06.2005; naam since 20.02.2018; afkorting RLBK since 20.02.2018; zetel Houtemsesteenweg 23 1800 Vilvoorde since 18.02.2013; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 01.01.2006; 25 functiehouders",
    "src_rlbk_foi_contact,RL Brabantse Kouters FOI channel (info@brabantsekouters.be; Houtemsesteenweg 23 Vilvoorde),https://www.brabantsekouters.be/contact/,RL Brabantse Kouters VZW,2026-08-19,official_register,tick1442; 15 member cities + provincie Vlaams-Brabant; coordinator Patrick Endels; NOT Erfgoed Brabantse Kouters IOED",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlbk," in raw or raw.startswith(b"vzw_rlbk,"):
    raise SystemExit("vzw_rlbk already present")
if b"0874.904.564" in raw or b"0874904564" in raw:
    raise SystemExit("RL Brabantse Kouters VZW KBO already present")
row = (
    "vzw_rlbk,Regionaal Landschap Brabantse Kouters VZW (leftover IGS / regionaal landschap of 15 mined Brabantse Kouters cities; NOT Erfgoed Brabantse Kouters IOED),"
    "Regionaal Landschap Brabantse Kouters ASBL (IGS residuel / paysage regional Brabantse Kouters),"
    "Regionaal Landschap Brabantse Kouters leftover IGS / regional landscape VZW of 15 Brabantse Kouters municipalities (not Erfgoed Brabantse Kouters IOED),"
    "other,sec_flanders,nl,https://www.brabantsekouters.be/,info@brabantsekouters.be,Houtemsesteenweg 23 1800 Vilvoorde,"
    "tick1442 leftover residual IGS VZW of mined Brabantse Kouters cities after leftover AGB hunt; KBO 0874.904.564 Actief since 14.06.2005; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1461569 omzet empty diensten empty pers 1353725 pnl 69707 equity 356095 cash 56447 debt 708837 capex 24122 dividend 0 brutomarge 1420281; FOI ready omzet empty / 73 empty / 60-61 empty / pers 1.35m / cash DROP / geldbeleg JUMP / lev JUMP / voorz 0.40m; distinct from already-mined Erfgoed Brabantse Kouters IOED 1428 / AGA Asse / AGB Grimbergen / AGB Steenokkerzeel / AGB Zaventem / AGB Zemst / AG Vilvoorde / AGB Merchtem / RLDV 1441 / RLD 1440 / RLNH 1439 / RLWH 1438"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlbk")

# --- budgets ---
BUDGETS = [
    ("bud_rlbk_assets_2025", "2025", "1461569", "2025 assets 1461569 VKT-VZW 20/58; tick1442; primary official NBB WVV"),
    ("bud_rlbk_assets_2024", "2024", "1347546", "2024 assets 1347546 comparative; tick1442; primary official NBB WVV 20/58"),
    ("bud_rlbk_fixed_2025", "2025", "62406", "2025 vaste activa 62406 vs 38284; tick1442; primary official NBB WVV 21/28"),
    ("bud_rlbk_fixed_2024", "2024", "38284", "2024 vaste activa 38284 comparative; tick1442; primary official NBB WVV 21/28"),
    ("bud_rlbk_iva_2025", "2025", "0", "2025 IVA empty (section 6.1.1 not filed); tick1442; primary official NBB WVV 21"),
    ("bud_rlbk_mva_2025", "2025", "0", "2025 MVA empty (section 6.1.2 not filed); tick1442; primary official NBB WVV 22/27"),
    ("bud_rlbk_fva_2025", "2025", "62406", "2025 FVA 62406 vs 38284; tick1442; primary official NBB WVV 28"),
    ("bud_rlbk_fva_2024", "2024", "38284", "2024 FVA 38284 comparative; tick1442; primary official NBB WVV 28"),
    ("bud_rlbk_current_2025", "2025", "1399163", "2025 vlottend 1399163 vs 1309262; tick1442; primary official NBB WVV 29/58"),
    ("bud_rlbk_stock_2025", "2025", "2906", "2025 voorraden 2906 vs 3433; tick1442; primary official NBB WVV 3"),
    ("bud_rlbk_strecv_2025", "2025", "667736", "2025 ST vorderingen 667736 vs 611646; tick1442; primary official NBB WVV 40/41"),
    ("bud_rlbk_strecv_2024", "2024", "611646", "2024 ST vorderingen 611646 comparative; tick1442; primary official NBB WVV 40/41"),
    ("bud_rlbk_trade_2025", "2025", "617736", "2025 handelsvorderingen 617736 vs 611646; tick1442; primary official NBB WVV 40"),
    ("bud_rlbk_trade_2024", "2024", "611646", "2024 handelsvorderingen 611646 comparative; tick1442; primary official NBB WVV 40"),
    ("bud_rlbk_othrecv_2025", "2025", "50000", "2025 overige vorderingen 50000 (was empty); tick1442; primary official NBB WVV 41"),
    ("bud_rlbk_geldbeleg_2025", "2025", "519025", "2025 geldbeleggingen 519025 JUMP vs 421841; tick1442; primary official NBB WVV 50/53"),
    ("bud_rlbk_geldbeleg_2024", "2024", "421841", "2024 geldbeleggingen 421841 comparative; tick1442; primary official NBB WVV 50/53"),
    ("bud_rlbk_cash_2025", "2025", "56447", "2025 liquide middelen 56447 DROP vs 149542; tick1442; primary official NBB WVV 54/58"),
    ("bud_rlbk_cash_2024", "2024", "149542", "2024 liquide middelen 149542 comparative; tick1442; primary official NBB WVV 54/58"),
    ("bud_rlbk_prepaid_2025", "2025", "153049", "2025 prepaid 153049 vs 122800; tick1442; primary official NBB WVV 490/1"),
    ("bud_rlbk_prepaid_2024", "2024", "122800", "2024 prepaid 122800 comparative; tick1442; primary official NBB WVV 490/1"),
    ("bud_rlbk_equity_2025", "2025", "356095", "2025 EV 356095 vs 286389; tick1442; primary official NBB WVV 10/15"),
    ("bud_rlbk_equity_2024", "2024", "286389", "2024 EV 286389 comparative; tick1442; primary official NBB WVV 10/15"),
    ("bud_rlbk_overgedragen_2025", "2025", "356095", "2025 overgedragen winst 356095 vs 286389; tick1442; primary official NBB WVV 14"),
    ("bud_rlbk_voorz_2025", "2025", "396636", "2025 voorzieningen 396636 (overige risico's 396636 vs 332803; pens empty); tick1442; primary official NBB WVV 16"),
    ("bud_rlbk_voorz_2024", "2024", "332803", "2024 voorzieningen 332803 comparative; tick1442; primary official NBB WVV 16"),
    ("bud_rlbk_voorz_oth_2025", "2025", "396636", "2025 overige risico's en kosten 396636 vs 332803; tick1442; primary official NBB WVV 164/5"),
    ("bud_rlbk_debt_2025", "2025", "708837", "2025 schulden 708837 vs 728354 (LT empty); tick1442; primary official NBB WVV 17/49"),
    ("bud_rlbk_debt_2024", "2024", "728354", "2024 schulden 728354 comparative; tick1442; primary official NBB WVV 17/49"),
    ("bud_rlbk_stdebt_2025", "2025", "403805", "2025 ST schulden 403805 JUMP vs 330926; tick1442; primary official NBB WVV 42/48"),
    ("bud_rlbk_stdebt_2024", "2024", "330926", "2024 ST schulden 330926 comparative; tick1442; primary official NBB WVV 42/48"),
    ("bud_rlbk_lev_2025", "2025", "258767", "2025 leveranciers 258767 JUMP vs 184286; tick1442; primary official NBB WVV 440/4"),
    ("bud_rlbk_lev_2024", "2024", "184286", "2024 leveranciers 184286 comparative; tick1442; primary official NBB WVV 440/4"),
    ("bud_rlbk_bezold_2025", "2025", "145038", "2025 bezoldigingen/sociale lasten 145038 vs 146640; tick1442; primary official NBB WVV 454/9"),
    ("bud_rlbk_deferred_2025", "2025", "305032", "2025 deferred 305032 DROP vs 397428; tick1442; primary official NBB WVV 492/3"),
    ("bud_rlbk_deferred_2024", "2024", "397428", "2024 deferred 397428 comparative; tick1442; primary official NBB WVV 492/3"),
    ("bud_rlbk_brutomarge_2025", "2025", "1420281", "2025 brutomarge 1420281 vs 1291807; omzet 70 empty; 73 empty; 60/61 empty; tick1442; primary official NBB WVV 9900"),
    ("bud_rlbk_brutomarge_2024", "2024", "1291807", "2024 brutomarge 1291807 comparative; tick1442; primary official NBB WVV 9900"),
    ("bud_rlbk_pers_2025", "2025", "1353725", "2025 pers 1353725 / 15.4 VTE vs 1287988 / 14.9; tick1442; primary official NBB WVV 62"),
    ("bud_rlbk_pers_2024", "2024", "1287988", "2024 pers 1287988 / 14.9 VTE comparative; tick1442; primary official NBB WVV 62"),
    ("bud_rlbk_andere_2025", "2025", "152", "2025 andere bedrijfskosten 152; tick1442; primary official NBB WVV 640/8"),
    ("bud_rlbk_expl_2025", "2025", "66404", "2025 expl +66404 vs +3820; tick1442; primary official NBB WVV 9901"),
    ("bud_rlbk_expl_2024", "2024", "3820", "2024 expl +3820 comparative; tick1442; primary official NBB WVV 9901"),
    ("bud_rlbk_finopbr_2025", "2025", "4997", "2025 fin opbr 4997 vs 6016; tick1442; primary official NBB WVV 75/76B"),
    ("bud_rlbk_finkost_2025", "2025", "962", "2025 fin kosten 962 vs 1967; tick1442; primary official NBB WVV 65/66B"),
    ("bud_rlbk_tax_2025", "2025", "733", "2025 tax 733 (was empty); tick1442; primary official NBB WVV 67/77"),
    ("bud_rlbk_pnl_2025", "2025", "69707", "2025 PnL +69707 vs +7869; tick1442; primary official NBB WVV 9904"),
    ("bud_rlbk_pnl_2024", "2024", "7869", "2024 PnL +7869 comparative; tick1442; primary official NBB WVV 9904"),
    ("bud_rlbk_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1442; primary official NBB WVV"),
    ("bud_rlbk_capex_2025", "2025", "24122", "2025 FVA aanschaffingen 24122; IVA/MVA sections not filed; tick1442; primary official NBB WVV 8365"),
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
    f"comm_rlbk_jr2025_bruto,Regionaal Landschap Brabantse Kouters VZW JR2025 leftover IGS dual (brutomarge 1.42m / pers 1.35m / cash DROP 0.06m),{ENT},RL Brabantse Kouters VZW / 15 Brabantse Kouters cities,WVV VZW; NBB neerlegging; 15 Brabantse Kouters gemeenten + provincie Vlaams-Brabant,2026-04-29,2005,,1420281,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00321333.pdf,Local leftover IGS map VL Brabantse Kouters landschap — 1.42m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 1.35m,Publish empty 70/73/60-61 split + pers 1.35m + cash DROP + geldbeleg JUMP + lev JUMP + voorz 0.40m + vennoten share-pct; do not keep leftover RLBK VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>BrabantseKouters>RLBK>JR2025_L5,tick1442; assets 1461569 omzet empty diensten empty pers 1353725 pnl 69707 equity 356095 cash 56447 debt 708837 capex 24122 dividend 0 brutomarge 1420281; FOI ready not sent; not TE-additive of 348bn; NOT Erfgoed Brabantse Kouters IOED",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlbk_omzet_empty_pers_1_35m_cash_drop,Regionaal Landschap Brabantse Kouters VZW JR2025 leftover IGS: empty omzet 70 / pers 1.35m / cash DROP 0.06m / brutomarge 1.42m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>BrabantseKouters>RLBK>JR2025_L5,1420281,1461569,Leftover dual IGS VZW: assets 1.46m / equity 0.36m / pnl +0.07m / omzet empty / 73 empty / 60-61 empty / pers 1.35m 15.4 VTE / cash 0.06m DROP / geldbeleg 0.52m JUMP / debt 0.71m / lev 0.26m JUMP / voorz 0.40m / dividend 0,strong,{SRC},RL Brabantse Kouters VZW / 15 Brabantse Kouters cities,Local leftover IGS map VL Brabantse Kouters landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 1.42m / pers 1.35m / cash DROP 0.06m / PnL +0.07m,6.6,6.4,2.2,6.2,Publish empty 70/73/60-61 split + pers 1.35m + cash DROP + geldbeleg JUMP + lev JUMP + voorz 0.40m + vennoten share-pct; do not keep leftover RLBK VZW as dual unpublished vehicle,active,,tick1442; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Erfgoed Brabantse Kouters IOED 1428 / RLDV 1441 / RLD 1440 / RLNH 1439 / RLWH 1438",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>BrabantseKouters>RLBK>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 1420281 + pers 62 1353725 / 15.4 VTE + cash DROP 56447 vs 149542 + geldbeleg JUMP 519025 vs 421841 + leveranciers JUMP 258767 vs 184286 + voorz 396636 + deferred DROP 305032 vs 397428 + FVA aanschaf 24122 + vennoten share-pct unpublished + commissaris unpublished + 1 VE unpublished + relation to Erfgoed Brabantse Kouters IOED unpublished,Leftover RLBK VZW after leftover AGB hunt: 1.42m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Brabantse Kouters vzw / Bestuursorgaan,info@brabantsekouters.be,Houtemsesteenweg 23 1800 Vilvoorde,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlbk_jr2025_bruto,lb_rlbk_omzet_empty_pers_1_35m_cash_drop,{TS},{TS},tick1442 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (48192 bytes 12p deposit 2026-00321333). FOI ready not sent. NOT Erfgoed Brabantse Kouters IOED. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Meetjesland JR2025 CDN 2026-00092026 live leftover for next (NOT Cultuuroverleg Meetjesland 1416).",
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
if not last_s.startswith("rq_1442,"):
    raise SystemExit(f"expected last row rq_1442, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1442 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1442,RL Brabantse Kouters JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlbk,"
    "Completed: Regionaal Landschap Brabantse Kouters VZW leftover IGS / regionaal landschap of 15 mined Brabantse Kouters cities after leftover AGB hunt; KBO 0874.904.564 Actief; live JR2025 official NBB WVV VKT-VZW PDF (48192 bytes 12p deposit 2026-00321333; AV 29.04.2026; header 23.07.2026; created 23.07.2026; no commissaris listed); sourced euros assets 1461569 omzet empty diensten empty pers 1353725 pnl 69707 equity 356095 cash 56447 debt 708837 capex 24122 dividend 0 brutomarge 1420281; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.35m / cash DROP / geldbeleg JUMP / lev JUMP / voorz 0.40m; NOT Erfgoed Brabantse Kouters IOED,"
    f"{GAP},2026-08-19T12:25:00Z,{TS},"
    "tick1442 RL Brabantse Kouters VZW leftover IGS residual; KBO 0874.904.564; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1443 residual dual L5 VL leftover RL Meetjesland if 2025 CDN still live"
)
spawn = (
    "rq_1443,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1442 done including RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Meetjesland & Leievallei 0466.277.515 JR2025 CDN 2026-00092026 LIVE leftover — STRONG next leftover RL (NOT Cultuuroverleg Meetjesland 1416); leftover RL Haspengouw & Voeren 0471.371.597 JR2025 CDN 2026-00070056 live leftover; leftover RL Kleine & Grote Nete 0810.764.897 JR2025 CDN 2026-00054598 live leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1442 after RL Brabantse Kouters leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Meetjesland if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1442=done + rq_1443 spawned; keep", last_line_start)

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
    f"tick1442 RL Brabantse Kouters leftover IGS residual; KBO 0874.904.564; live JR2025 NBB WVV PDF; sourced euros assets 1461569 omzet empty diensten empty pers 1353725 pnl 69707 equity 356095 cash 56447 debt 708837 capex 24122 dividend 0 brutomarge 1420281; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.35m / cash DROP / geldbeleg JUMP / lev JUMP / voorz 0.40m; NOT Erfgoed Brabantse Kouters IOED; next rq_1443 residual dual L5 VL leftover RL Meetjesland if 2025 CDN still live; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1442,1442,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1442")

# --- loop_log ---
entry = (
    "\n## Tick 1442 - 2026-08-19 - rq_1442 RL Brabantse Kouters dual residual leftover\n"
    "- Unit: Regionaal Landschap Brabantse Kouters VZW / RLBK (leftover IGS / regionaal landschap of 15 mined Brabantse Kouters cities; 1 VE) after residual dual hunt (KBO **0874.904.564**; official brabantsekouters.be; live NBB WVV VKT-VZW deposit **2026-00321333** PDF 48192 bytes / 12p; AV **29.04.2026**; header **23.07.2026**; pdfinfo created **23.07.2026**; model **VKT-VZW** 25.0.13 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.2/6.2/6.3/6.5/6.6/6.8/7/8 not filed; 6.1.3 FVA + 6.4 + 6.7 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM IP-blacklist this tick; last known 1441: SBM last table year 2024-12-31; deposit 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGA Asse / AGB Grimbergen / AGB Steenokkerzeel / AGB Zaventem / AGB Zemst / AG Vilvoorde / AGB Merchtem) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover IGS Regionaal Landschap Brabantse Kouters VZW statutory CDN live this tick (HTTP 200 / application/pdf / 48192 / 12p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined RL VZW of mined Brabantse Kouters cities with full WVV balans; STRONG next leftover RL after RL de Voorkempen 1441). Distinct from already-mined **Erfgoed Brabantse Kouters IOED** (igs_ebk tick 1428; KBO 0741.478.094; NOT this entity) / AGA Asse / AGB Grimbergen / AGB Steenokkerzeel / AGB Zaventem / AGB Zemst / AG Vilvoorde / AGB Merchtem / RLDV 1441 / RLD 1440 / RLNH 1439 / RLWH 1438. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Brabantse Kouters VZW / 0874.904.564 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **14.06.2005**; statutaire naam Regionaal Landschap Brabantse Kouters since 20.02.2018; afkorting RLBK since 20.02.2018; VZW since 14.06.2005; zetel Houtemsesteenweg 23 1800 Vilvoorde since 18.02.2013; **1 VE**; official site https://www.brabantsekouters.be/; contact info@brabantsekouters.be; coordinator Patrick Endels; NACE RSZ 91.420; Werkgever RSZ since 01.01.2006; **25 functiehouders**. Official site 15 leden-gemeenten: Asse / Grimbergen / Kapelle-op-den-Bos / Kraainem / Londerzeel / Machelen / Meise / Merchtem / Opwijk / Steenokkerzeel / Vilvoorde / Wemmel / Wezembeek-Oppem / Zaventem / Zemst. Plus provincie Vlaams-Brabant + Vlaams Gewest + Europa. Named share-% unpublished. Voorzitter unpublished (WVV 2.1 unlabeled; first listed Dewandeleer Bart). Dagelijks bestuur: Cuyle Lukas (since 25.03.2026) / Endels Patrick (since 27.04.2022) / Geeroms Magda / Van den Brande Joeri. Contact info@brabantsekouters.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor HTML blocked this tick (IP blacklist) — PDF wins. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **1353725** / **15,4 VTE**): assets **1461569** (was 1347546); fixed **62406** / IVA empty / MVA empty / FVA **62406** vs 38284; current **1399163**; voorraden **2906** vs 3433; ST recv **667736** (trade **617736** vs 611646 / other **50000** was empty); geldbeleg **519025 JUMP** vs 421841; cash **56447 DROP** vs 149542; prepaid **153049** vs 122800; equity **356095** (overgedragen **356095**); voorzieningen **396636** (overige risico's **396636** vs 332803; pens empty); schulden **708837** vs 728354 (LT empty; ST **403805 JUMP** vs 330926 waarvan leveranciers **258767 JUMP** vs 184286 + soc/bezold **145038**; deferred **305032 DROP** vs 397428); brutomarge **1420281** vs 1291807; omzet empty; 73 empty; 60/61 empty; pers **1353725** / **15,4 VTE** / 23843 uur / YE **15,6**; andere **152**; expl **+66404** vs +3820; fin opbr **4997**; fin kosten **962**; tax **733**; PnL **+69707** vs +7869; dividend **0**; over te dragen **356095**; capex **24122** (FVA aanschaf only). PDF 1-euro rounding: EV+voorz+debt 1461568 vs published totaal 1461569; 9903−tax 69706 vs published 69707; 9905+14P 356096 vs published 356095.\n"
    f"- CSVs: sources +4; entities +1 `vzw_rlbk` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 1420281 AV 29.04.2026; leaderboard +1 annual 1420281 / total 1461569; foi_queue +1 status=ready never sent; research_queue surgical rq_1442=done + rq_1443 spawn; loop_state ticks_completed=1442. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_rlbk_omzet_empty_pers_1_35m_cash_drop_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 1.35m 15.4 VTE deelwerking unpublished / cash DROP 0.06m / geldbeleg JUMP 0.52m / lev JUMP 0.26m / voorz 0.40m / deferred DROP 0.31m / FVA aanschaf 24.1k / vennoten share-pct / relation to Erfgoed Brabantse Kouters IOED unpublished / commissaris unpublished / 1 VE unpublished.\n"
    "- Next: rq_1443 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Meetjesland **0466.277.515** JR2025 CDN **2026-00092026** LIVE — STRONG next leftover RL (NOT Cultuuroverleg Meetjesland 1416). Leftover RL Haspengouw 0471.371.597 CDN 2026-00070056 live. Leftover RL Kleine & Grote Nete 0810.764.897 CDN 2026-00054598 live. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1442 -" in lraw:
    raise SystemExit("loop_log already has tick 1442 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1442")
print("DONE tick 1442")
