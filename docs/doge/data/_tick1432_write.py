#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1432 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:20:00Z"
ENT = "vzw_rlsd"
SRC = "src_rlsd_jr2025_nbb"
GAP = "gap_rlsd_omzet_empty_pers_1_21m_cash_1_23m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlsd_jr2025_nbb,Regionaal Landschap Schelde-Durme VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00106166.pdf,NBB / RL Schelde-Durme VZW,2026-08-19,budget,tick1432; VKT-VZW 25.0.11 m04-f PDF 17p / 56230 bytes deposit 2026-00106166; AV 21.04.2026; created 08.05.2026; neerlegging 2026-05-08; KBO 0889.859.093; assets 1745189 cash 1233970 debt 629291 brutomarge 1435020 pers 1213789 pnl 188062; commissaris Baker Tilly 4977",
    "src_rlsd_site,Regionaal Landschap Schelde-Durme official site,https://www.rlsd.be/,RL Schelde-Durme VZW,2026-08-19,official_register,tick1432; leftover IGS / regionaal landschap of 21 Schelde-Durme cities; zetel Serskampsteenweg 52 9230 Wetteren; contact info@rlsd.be; coordinator Barbara Depril; IOED channel ioedscheldedurme@rlsd.be",
    "src_kbo_rlsd_0889859093,KBO Regionaal Landschap Schelde-Durme 0889.859.093,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0889859093,KBO Public Search FOD Economie,2026-08-19,official_register,tick1432; Actief since 05.06.2007; naam/afkorting RLSD since 23.05.2007; zetel Serskampsteenweg 52 9230 Wetteren since 26.01.2026; 1 VE; VZW; NACE RSZ 91.420; Werkgever RSZ since 22.10.2007",
    "src_rlsd_foi_contact,RL Schelde-Durme FOI channel (info@rlsd.be; Serskampsteenweg 52 Wetteren),https://www.rlsd.be/contact-nieuw/,RL Schelde-Durme VZW,2026-08-19,official_register,tick1432; 21 member cities + provincies Oost-Vlaanderen/Antwerpen; voorzitter Eva Rombaut; commissaris Baker Tilly 0449.065.260; distinct from PV 0680.397.590",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlsd," in raw or raw.startswith(b"vzw_rlsd,"):
    raise SystemExit("vzw_rlsd already present")
if b"0889.859.093" in raw or b"0889859093" in raw:
    raise SystemExit("RL Schelde-Durme VZW KBO already present")
row = (
    "vzw_rlsd,Regionaal Landschap Schelde-Durme VZW (leftover IGS / regionaal landschap of 21 mined Schelde-Durme cities),"
    "Regionaal Landschap Schelde-Durme ASBL (IGS residuel / paysage regional Schelde-Durme),"
    "Regionaal Landschap Schelde-Durme leftover IGS / regional landscape VZW of 21 Schelde-Durme municipalities,"
    "other,sec_flanders,nl,https://www.rlsd.be/,info@rlsd.be,Serskampsteenweg 52 9230 Wetteren,"
    "tick1432 leftover residual IGS VZW of mined Schelde-Durme cities after leftover AGB hunt; KBO 0889.859.093 Actief since 05.06.2007; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1745189 omzet empty diensten empty pers 1213789 pnl 188062 equity 1115898 cash 1233970 debt 629291 capex 72455 dividend 0; FOI ready empty 70/73/60/61 / pers 1.21m / cash jump / leveranciers jump; distinct from PV RL Schelde-Durme 0680.397.590 and already-mined Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlsd")

# --- budgets ---
BUDGETS = [
    ("bud_rlsd_assets_2025", "2025", "1745189", "2025 assets 1745189 VKT-VZW 20/58; tick1432; primary official NBB WVV"),
    ("bud_rlsd_assets_2024", "2024", "1602085", "2024 assets 1602085 comparative; tick1432; primary official NBB WVV 20/58"),
    ("bud_rlsd_fixed_2025", "2025", "141821", "2025 vaste activa 141821 vs 88479; tick1432; primary official NBB WVV 21/28"),
    ("bud_rlsd_iva_2025", "2025", "26109", "2025 IVA 26109 vs 40223; tick1432; primary official NBB WVV 21"),
    ("bud_rlsd_mva_2025", "2025", "105727", "2025 MVA 105727 vs 46622; tick1432; primary official NBB WVV 22/27"),
    ("bud_rlsd_machines_2025", "2025", "34909", "2025 machines 34909 vs 8334; tick1432; primary official NBB WVV 23"),
    ("bud_rlsd_meubilair_2025", "2025", "56172", "2025 meubilair/rollend 56172 vs 38287; tick1432; primary official NBB WVV 24"),
    ("bud_rlsd_overige_mva_2025", "2025", "5332", "2025 overige MVA 5332 vs 0; tick1432; primary official NBB WVV 26"),
    ("bud_rlsd_cip_2025", "2025", "9314", "2025 CIP 9314 vs 0; tick1432; primary official NBB WVV 27"),
    ("bud_rlsd_fva_2025", "2025", "9985", "2025 FVA 9985 vs 1635; tick1432; primary official NBB WVV 28"),
    ("bud_rlsd_current_2025", "2025", "1603368", "2025 vlottend 1603368 vs 1513606; tick1432; primary official NBB WVV 29/58"),
    ("bud_rlsd_strecv_2025", "2025", "333969", "2025 ST vorderingen 333969 vs 373638; tick1432; primary official NBB WVV 40/41"),
    ("bud_rlsd_trade_2025", "2025", "223234", "2025 handelsvorderingen 223234 vs 262874; tick1432; primary official NBB WVV 40"),
    ("bud_rlsd_othrecv_2025", "2025", "110735", "2025 overige vorderingen 110735 vs 110764; tick1432; primary official NBB WVV 41"),
    ("bud_rlsd_cash_2025", "2025", "1233970", "2025 liquide middelen 1233970 JUMP vs 1107722; tick1432; primary official NBB WVV 54/58"),
    ("bud_rlsd_cash_2024", "2024", "1107722", "2024 liquide middelen 1107722 comparative; tick1432; primary official NBB WVV 54/58"),
    ("bud_rlsd_prepaid_2025", "2025", "35429", "2025 prepaid 35429 vs 32246; tick1432; primary official NBB WVV 490/1"),
    ("bud_rlsd_equity_2025", "2025", "1115898", "2025 EV 1115898 overgedragen only vs 927836; tick1432; primary official NBB WVV 10/15"),
    ("bud_rlsd_equity_2024", "2024", "927836", "2024 EV 927836 comparative; tick1432; primary official NBB WVV 10/15"),
    ("bud_rlsd_overgedragen_2025", "2025", "1115898", "2025 overgedragen 1115898 vs 927836; tick1432; primary official NBB WVV 14"),
    ("bud_rlsd_debt_2025", "2025", "629291", "2025 schulden 629291 vs 674250 (no LT); tick1432; primary official NBB WVV 17/49"),
    ("bud_rlsd_stdebt_2025", "2025", "399183", "2025 ST schulden 399183 vs 390328; tick1432; primary official NBB WVV 42/48"),
    ("bud_rlsd_lev_2025", "2025", "228789", "2025 leveranciers 228789 JUMP vs 149994; tick1432; primary official NBB WVV 440/4"),
    ("bud_rlsd_taxsoc_2025", "2025", "170393", "2025 tax/soc 170393 vs 177801; tick1432; primary official NBB WVV 45"),
    ("bud_rlsd_tax_2025", "2025", "12410", "2025 belastingen 12410 vs 28820; tick1432; primary official NBB WVV 450/3"),
    ("bud_rlsd_bezold_2025", "2025", "157984", "2025 bezoldigingen/sociale lasten 157984 vs 148981; tick1432; primary official NBB WVV 454/9"),
    ("bud_rlsd_deferred_2025", "2025", "230108", "2025 overlopend passief 230108 vs 283921; tick1432; primary official NBB WVV 492/3"),
    ("bud_rlsd_brutomarge_2025", "2025", "1435020", "2025 brutomarge 1435020 vs 1433896; omzet 70 empty; 73 empty; 60/61 empty; tick1432; primary official NBB WVV 9900"),
    ("bud_rlsd_brutomarge_2024", "2024", "1433896", "2024 brutomarge 1433896 comparative; tick1432; primary official NBB WVV 9900"),
    ("bud_rlsd_pers_2025", "2025", "1213789", "2025 pers 1213789 / 17.4 VTE vs 1204320 / 16.4; tick1432; primary official NBB WVV 62"),
    ("bud_rlsd_pers_2024", "2024", "1204320", "2024 pers 1204320 / 16.4 VTE comparative; tick1432; primary official NBB WVV 62"),
    ("bud_rlsd_afschr_2025", "2025", "27463", "2025 afschrijvingen 27463 vs 17272; tick1432; primary official NBB WVV 630"),
    ("bud_rlsd_andere_2025", "2025", "2240", "2025 andere bedrijfskosten 2240 vs 283; tick1432; primary official NBB WVV 640/8"),
    ("bud_rlsd_expl_2025", "2025", "191528", "2025 expl 191528 vs 212021; tick1432; primary official NBB WVV 9901"),
    ("bud_rlsd_expl_2024", "2024", "212021", "2024 expl 212021 comparative; tick1432; primary official NBB WVV 9901"),
    ("bud_rlsd_finopbr_2025", "2025", "2830", "2025 fin opbr 2830 vs 1603; tick1432; primary official NBB WVV 75/76B"),
    ("bud_rlsd_finkost_2025", "2025", "1354", "2025 fin kosten 1354 vs 651; tick1432; primary official NBB WVV 65/66B"),
    ("bud_rlsd_taxpnl_2025", "2025", "4942", "2025 belastingen resultaat 4942 vs 4175; tick1432; primary official NBB WVV 67/77"),
    ("bud_rlsd_pnl_2025", "2025", "188062", "2025 PnL 188062 vs 208798; tick1432; primary official NBB WVV 9904"),
    ("bud_rlsd_pnl_2024", "2024", "208798", "2024 PnL 208798 comparative; tick1432; primary official NBB WVV 9904"),
    ("bud_rlsd_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1432; primary official NBB WVV"),
    ("bud_rlsd_capex_2025", "2025", "72455", "2025 MVA aanschaffingen 72455; FVA aanschaf 8850 extra; tick1432; primary official NBB WVV 8169"),
    ("bud_rlsd_commissaris_2025", "2025", "4977", "2025 commissaris Baker Tilly mandaat 4977 excl btw; tick1432; primary official NBB WVV 6.6"),
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
    f"comm_rlsd_jr2025_bruto,Regionaal Landschap Schelde-Durme VZW JR2025 leftover IGS dual (brutomarge 1.44m / pers 1.21m / cash 1.23m),{ENT},RL Schelde-Durme VZW / 21 Schelde-Durme cities,WVV VZW; NBB neerlegging; 21 Schelde-Durme gemeenten + 2 provincies,2026-04-21,2007,,1435020,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00106166.pdf,Local leftover IGS map VL Schelde-Durme landschap — 1.44m brutomarge / empty 70/73/60/61 / pers 1.21m,Publish empty 70/73/60/61 split + cash jump + vennoten share-pct + PV/IOED relation; do not keep leftover RLSD VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>OostVlaanderen>ScheldeDurme>RLSD>JR2025_L5,tick1432; assets 1745189 omzet empty diensten empty pers 1213789 pnl 188062 equity 1115898 cash 1233970 debt 629291 capex 72455 dividend 0; FOI ready not sent; not TE-additive of 348bn",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlsd_omzet_empty_pers_1_21m_cash_1_23m,Regionaal Landschap Schelde-Durme VZW JR2025 leftover IGS: brutomarge 1.44m / empty 70-73-60/61 / pers 1.21m / cash 1.23m,L5,local_budget_line,Vlaanderen>OostVlaanderen>ScheldeDurme>RLSD>JR2025_L5,1435020,1745189,Leftover dual IGS VZW: assets 1.75m / equity 1.12m / pnl +0.19m / omzet empty / diensten empty / pers 1.21m 17.4 VTE / cash 1.23m JUMP / debt 0.63m / dividend 0,strong,{SRC},RL Schelde-Durme VZW / 21 Schelde-Durme cities,Local leftover IGS map VL Schelde-Durme landschap — JR2025 live; dual empty 70/73/60/61 FOI,Official NBB WVV 2026-08-19: brutomarge 1.44m / pers 1.21m / cash 1.23m / PnL +0.19m,6.8,6.4,2.2,5.8,Publish empty 70/73/60/61 split + cash jump + leveranciers jump + vennoten share-pct + PV/IOED relation; do not keep leftover RLSD VZW as dual unpublished vehicle,active,,tick1432; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from PV 0680.397.590 and already-mined Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>OostVlaanderen>ScheldeDurme>RLSD>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + pers 62 1213789 / 17.4 VTE + cash JUMP 1233970 vs 1107722 + leveranciers JUMP 228789 vs 149994 + other recv 110735 + deferred 230108 + PV 0680.397.590 relation unpublished + vennoten share-pct unpublished + commissarisverslag page empty,Leftover RLSD VZW after leftover AGB hunt: 1.44m brutomarge / empty 70/73/60/61 hides public-perimeter landschap vehicle,8,Regionaal Landschap Schelde-Durme vzw / Bestuursorgaan,info@rlsd.be,Serskampsteenweg 52 9230 Wetteren,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlsd_jr2025_bruto,lb_rlsd_omzet_empty_pers_1_21m_cash_1_23m,{TS},{TS},tick1432 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (56230 bytes 17p deposit 2026-00106166). FOI ready not sent. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. PV RL Schelde-Durme 0680.397.590 still no JR.",
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
if not last_s.startswith("rq_1432,"):
    raise SystemExit(f"expected last row rq_1432, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1432 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1432,RL Schelde-Durme VZW JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlsd,"
    "Completed: Regionaal Landschap Schelde-Durme VZW leftover IGS / regionaal landschap of 21 mined Schelde-Durme cities after leftover AGB hunt; KBO 0889.859.093 Actief; live JR2025 official NBB WVV VKT-VZW PDF (56230 bytes 17p deposit 2026-00106166; AV 21.04.2026; created 08.05.2026; neerlegging 2026-05-08; commissaris Baker Tilly 4977); sourced euros assets 1745189 omzet empty diensten empty pers 1213789 pnl 188062 equity 1115898 cash 1233970 debt 629291 capex 72455 dividend 0; FOI ready empty 70/73/60/61 / pers 1.21m / cash jump / leveranciers jump / PV-IOED relation,"
    f"{GAP},2026-08-19T11:14:00Z,{TS},"
    "tick1432 RL Schelde-Durme VZW leftover IGS residual; KBO 0889.859.093; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1433 residual dual L5 VL"
)
spawn = (
    "rq_1433,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1432 done including RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1432 after RL Schelde-Durme VZW leftover IGS live NBB WVV; next residual dual L5 VL leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge-en-Ommeland/Nete en Aa/Hydra/Viersprong if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1432=done + rq_1433 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1432 RL Schelde-Durme VZW leftover IGS residual; KBO 0889.859.093; live JR2025 NBB WVV PDF; sourced euros assets 1745189 omzet empty diensten empty pers 1213789 pnl 188062 equity 1115898 cash 1233970 debt 629291 capex 72455 dividend 0; FOI ready empty 70/73/60/61 / pers 1.21m / cash jump / leveranciers jump / PV-IOED relation; next rq_1433 residual dual L5 VL leftover IOED if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1432,1432,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1432")

# --- loop_log ---
entry = (
    "\n## Tick 1432 - 2026-08-19 - rq_1432 RL Schelde-Durme VZW dual residual leftover\n"
    "- Unit: Regionaal Landschap Schelde-Durme VZW / RLSD (leftover IGS / regionaal landschap of 21 mined Schelde-Durme cities; 1 VE) after residual dual hunt (KBO **0889.859.093**; official rlsd.be; live NBB WVV VKT-VZW deposit **2026-00106166** PDF 56230 bytes / 17p; AV **21.04.2026**; created **08.05.2026**; neerlegging **2026-05-08**; model **VKT-VZW** 25.0.11 m04-f; commissaris Baker Tilly bedrijfsrevisoren BV B00190 / 0449.065.260 / De Blander Christel A02258 mandate 29.04.2025-29.04.2027 fee **4977**; VKT-VZW 6.2/6.3/6.5/7 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.4 + 6.6 + 6.7 sociale balans + 6.8 waarderingsregels filed; VKT-VZW 8 commissarisverslag page empty this extract). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Lille liquidation; VESPA/AGSL already mined — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (CDN 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover IGS Regionaal Landschap Schelde-Durme VZW statutory CDN live this tick (HTTP 200 / application/pdf / 56230 / 17p; SBM jaar **2025-12-31**; neerlegging 2026-05-08) — taken (hunt order #2 leftover unmined IGS named STRONG next from 1431 with full WVV balans). Distinct from PV Regionaal Landschap Schelde-Durme **0680.397.590** (still no jaarrekening) and already-mined Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / IVBO (Brugge-en-Ommeland afval — not this IOED). First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Schelde-Durme VZW / 0889.859.093 JR2025 extract in entities/sources/leaderboard (0 entity hits; only leftover-next mention). KBO Actief / normale toestand since **05.06.2007**; statutaire naam Regionaal Landschap Schelde-Durme / afkorting RLSD since 23.05.2007; VZW since 23.05.2007; zetel Serskampsteenweg 52 9230 Wetteren since 26.01.2026; **1 VE**; KBO no tel/e-mail/web; official site https://www.rlsd.be/; e-mail info@rlsd.be; coordinator Barbara Depril barbara@rlsd.be; NACE RSZ 91.420; Werkgever RSZ since 22.10.2007. Official site voorzitter Eva Rombaut (Provincie Oost-Vlaanderen); ondervoorzitter Paul Cerpentier (Algemeen Boerensyndicaat). Official site gemeenten: Aalst / Berlare / Beveren-Kruibeke-Zwijndrecht / Bornem / Buggenhout / Dendermonde / Destelbergen / Hamme / Laarne / Lebbeke / Lede / Lokeren / Puurs-Sint-Amands / Sint-Gillis-Waas / Sint-Niklaas / Stekene / Temse / Waasmunster / Wetteren / Wichelen / Zele. Named share-% unpublished. Contact info@rlsd.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source. Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **1213789** / **17,4 VTE**): assets **1745189** (was 1602085); fixed **141821** / IVA **26109** / MVA **105727** (machines **34909**; meubilair **56172**; overige **5332**; CIP **9314**) / FVA **9985**; current **1603368**; ST recv **333969** (trade **223234** / other **110735**); cash **1233970 JUMP** vs 1107722; prepaid **35429**; equity **1115898** (overgedragen 1115898); voorzieningen empty; schulden **629291** (no LT; ST **399183** waarvan leveranciers **228789 JUMP** vs 149994 + tax **12410** + soc/bezold **157984**; deferred **230108**); brutomarge **1435020** vs 1433896; omzet empty; 73 empty; 60/61 empty; pers **1213789** / **17,4 VTE** / 23766 uur / YE **18,2**; afschr **27463**; andere bedrijfskosten **2240**; expl **+191528** vs +212021; fin opbr **2830**; fin kosten **1354**; tax **4942**; PnL **+188062** vs +208798; dividend **0**; over te dragen **1115898**; capex **72455**; FVA aanschaf **8850**; commissaris **4977**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlsd` parent `sec_flanders`; budgets +43 executed; commitments +1 envelope 1435020 AV 21.04.2026; leaderboard +1 annual 1435020 / total 1745189; foi_queue +1 status=ready never sent; research_queue surgical rq_1432=done + rq_1433 spawn; loop_state ticks_completed=1432.\n"
    "- FOI: `gap_rlsd_omzet_empty_pers_1_21m_cash_1_23m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 1.21m 17.4 VTE deelwerking unpublished / cash JUMP / leveranciers JUMP 0.23m / other recv 0.11m / deferred 0.23m / vennoten share-pct / relation to PV 0680.397.590 and IOED Schelde-Durme / commissarisverslag page empty.\n"
    "- Next: rq_1433 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1432")
print("tick1432 writes done")
