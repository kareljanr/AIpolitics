#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1436 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T11:50:00Z"
ENT = "vzw_rlpz"
SRC = "src_rlpz_jr2025_nbb"
GAP = "gap_rlpz_omzet_empty_pers_0_82m_cash_0_81m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlpz_jr2025_nbb,Regionaal Landschap Pajottenland en Zennevallei VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00101632.pdf,NBB / RL Pajottenland en Zennevallei VZW,2026-08-19,budget,tick1436; VKT-VZW 23.0.8 m04-f PDF 13p / 49199 bytes deposit 2026-00101632; AV 19.03.2026; created 04.05.2026; pdfinfo 05.05.2026; neerlegging 2026-05-05; KBO 0458.521.374; assets 1055984 cash 813995 debt 498552 brutomarge 842762 omzet empty code73 empty code60_61 empty pers 816419 pnl 26992; commissaris Impacct Accountants 0687.783.745 / Vanderwegen Kris",
    "src_rlpz_site,Regionaal Landschap Pajottenland en Zennevallei official site,https://www.pajot-zenne.be/,RL Pajottenland en Zennevallei VZW,2026-08-19,official_register,tick1436; leftover IGS / regionaal landschap of 16 Pajottenland-Zennevallei cities; zetel Donkerstraat 23 1750 Lennik (Gaasbeek); contact info@pajot-zenne.be; tel 02 452 60 45; directeur Alwin Loeckx; voorzitter Elke Zelderloo",
    "src_kbo_rlpz_0458521374,KBO Regionaal Landschap Pajottenland en Zennevallei 0458.521.374,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458521374,KBO Public Search FOD Economie,2026-08-19,official_register,tick1436; Actief since 19.04.1996; naam since 05.12.2011; afkorting RL P&Z since 05.12.2011; zetel Donkerstraat 23 1750 Lennik since 01.01.2025; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 16.10.1996",
    "src_rlpz_foi_contact,RL Pajottenland en Zennevallei FOI channel (info@pajot-zenne.be; Donkerstraat 23 Lennik),https://www.pajot-zenne.be/contact,RL Pajottenland en Zennevallei VZW,2026-08-19,official_register,tick1436; 16 member cities + provincie Vlaams-Brabant; voorzitter Elke Zelderloo; directeur Alwin Loeckx; NOT Gemeente Pajottegem city 1010.784.540",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlpz," in raw or raw.startswith(b"vzw_rlpz,"):
    raise SystemExit("vzw_rlpz already present")
if b"0458.521.374" in raw or b"0458521374" in raw:
    raise SystemExit("RL Pajottenland KBO already present")
row = (
    "vzw_rlpz,Regionaal Landschap Pajottenland en Zennevallei VZW (leftover IGS / regionaal landschap of 16 mined Pajottenland-Zennevallei cities; NOT Pajottegem city),"
    "Regionaal Landschap Pajottenland et Zennevallei ASBL (IGS residuel / paysage regional Pajottenland-Zenne),"
    "Regionaal Landschap Pajottenland en Zennevallei leftover IGS / regional landscape VZW of 16 Pajottenland-Zennevallei municipalities (not Pajottegem city),"
    "other,sec_flanders,nl,https://www.pajot-zenne.be/,info@pajot-zenne.be,Donkerstraat 23 1750 Lennik,"
    "tick1436 leftover residual IGS VZW of mined Pajottenland-Zennevallei cities after leftover AGB hunt; KBO 0458.521.374 Actief since 19.04.1996; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1055984 omzet empty diensten empty pers 816419 pnl 26992 equity 557432 cash 813995 debt 498552 capex 0 dividend 0 brutomarge 842762; FOI ready omzet empty / 73 empty / 60-61 empty / pers 0.82m / cash 0.81m / trade drop / deferred drop; distinct from already-mined Gemeente Pajottegem 1010.784.540 / AGB Gooik / AGB Herne / RLRL 1435 / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Erfgoed Brabantse Kouters 1428"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlpz")

# --- budgets ---
BUDGETS = [
    ("bud_rlpz_assets_2025", "2025", "1055984", "2025 assets 1055984 VKT-VZW 20/58; tick1436; primary official NBB WVV"),
    ("bud_rlpz_assets_2024", "2024", "1119910", "2024 assets 1119910 comparative; tick1436; primary official NBB WVV 20/58"),
    ("bud_rlpz_fixed_2025", "2025", "1701", "2025 vaste activa 1701 vs 2496; tick1436; primary official NBB WVV 21/28"),
    ("bud_rlpz_iva_2025", "2025", "0", "2025 IVA empty fully depreciated 2801; tick1436; primary official NBB WVV 21"),
    ("bud_rlpz_mva_2025", "2025", "451", "2025 MVA 451 vs 1246; tick1436; primary official NBB WVV 22/27"),
    ("bud_rlpz_machines_2025", "2025", "451", "2025 machines 451 vs 1246; tick1436; primary official NBB WVV 23"),
    ("bud_rlpz_fva_2025", "2025", "1250", "2025 FVA 1250 unchanged; tick1436; primary official NBB WVV 28"),
    ("bud_rlpz_current_2025", "2025", "1054284", "2025 vlottend 1054284 vs 1117414; tick1436; primary official NBB WVV 29/58"),
    ("bud_rlpz_strecv_2025", "2025", "230070", "2025 ST vorderingen 230070 vs 295163; tick1436; primary official NBB WVV 40/41"),
    ("bud_rlpz_strecv_2024", "2024", "295163", "2024 ST vorderingen 295163 comparative; tick1436; primary official NBB WVV 40/41"),
    ("bud_rlpz_trade_2025", "2025", "189311", "2025 handelsvorderingen 189311 DROP vs 246816; tick1436; primary official NBB WVV 40"),
    ("bud_rlpz_trade_2024", "2024", "246816", "2024 handelsvorderingen 246816 comparative; tick1436; primary official NBB WVV 40"),
    ("bud_rlpz_othrecv_2025", "2025", "40759", "2025 overige vorderingen 40759 vs 48347; tick1436; primary official NBB WVV 41"),
    ("bud_rlpz_cash_2025", "2025", "813995", "2025 liquide middelen 813995 vs 813508; tick1436; primary official NBB WVV 54/58"),
    ("bud_rlpz_cash_2024", "2024", "813508", "2024 liquide middelen 813508 comparative; tick1436; primary official NBB WVV 54/58"),
    ("bud_rlpz_prepaid_2025", "2025", "10219", "2025 prepaid 10219 vs 8743; tick1436; primary official NBB WVV 490/1"),
    ("bud_rlpz_equity_2025", "2025", "557432", "2025 EV 557432 vs 530440; tick1436; primary official NBB WVV 10/15"),
    ("bud_rlpz_equity_2024", "2024", "530440", "2024 EV 530440 comparative; tick1436; primary official NBB WVV 10/15"),
    ("bud_rlpz_bestemde_2025", "2025", "294378", "2025 bestemde fondsen 294378 unchanged; tick1436; primary official NBB WVV 13"),
    ("bud_rlpz_overgedragen_2025", "2025", "263054", "2025 overgedragen winst 263054 vs 236062; tick1436; primary official NBB WVV 14"),
    ("bud_rlpz_debt_2025", "2025", "498552", "2025 schulden 498552 vs 589470 (LT empty); tick1436; primary official NBB WVV 17/49"),
    ("bud_rlpz_debt_2024", "2024", "589470", "2024 schulden 589470 comparative; tick1436; primary official NBB WVV 17/49"),
    ("bud_rlpz_stdebt_2025", "2025", "222228", "2025 ST schulden 222228 vs 220360; tick1436; primary official NBB WVV 42/48"),
    ("bud_rlpz_lev_2025", "2025", "151502", "2025 leveranciers 151502 vs 150122; tick1436; primary official NBB WVV 440/4"),
    ("bud_rlpz_lev_2024", "2024", "150122", "2024 leveranciers 150122 comparative; tick1436; primary official NBB WVV 440/4"),
    ("bud_rlpz_taxsoc_2025", "2025", "70725", "2025 tax/soc 70725 all bezoldigingen vs 70238; tick1436; primary official NBB WVV 45"),
    ("bud_rlpz_bezold_2025", "2025", "70725", "2025 bezoldigingen/sociale lasten 70725 vs 70238; tick1436; primary official NBB WVV 454/9"),
    ("bud_rlpz_deferred_2025", "2025", "276324", "2025 overlopend passief 276324 DROP vs 369109; tick1436; primary official NBB WVV 492/3"),
    ("bud_rlpz_deferred_2024", "2024", "369109", "2024 overlopend passief 369109 comparative; tick1436; primary official NBB WVV 492/3"),
    ("bud_rlpz_brutomarge_2025", "2025", "842762", "2025 brutomarge 842762 vs 787702; omzet 70 empty; 73 empty; 60/61 empty; tick1436; primary official NBB WVV 9900"),
    ("bud_rlpz_brutomarge_2024", "2024", "787702", "2024 brutomarge 787702 comparative; tick1436; primary official NBB WVV 9900"),
    ("bud_rlpz_pers_2025", "2025", "816419", "2025 pers 816419 / 10.6 VTE vs 785616 / 11; tick1436; primary official NBB WVV 62"),
    ("bud_rlpz_pers_2024", "2024", "785616", "2024 pers 785616 / 11 VTE comparative; tick1436; primary official NBB WVV 62"),
    ("bud_rlpz_afschr_2025", "2025", "796", "2025 afschrijvingen 796 vs empty; tick1436; primary official NBB WVV 630"),
    ("bud_rlpz_expl_2025", "2025", "25548", "2025 expl 25548 vs 2085; tick1436; primary official NBB WVV 9901"),
    ("bud_rlpz_expl_2024", "2024", "2085", "2024 expl 2085 comparative; tick1436; primary official NBB WVV 9901"),
    ("bud_rlpz_finopbr_2025", "2025", "1822", "2025 fin opbr 1822 vs 879; tick1436; primary official NBB WVV 75/76B"),
    ("bud_rlpz_finkost_2025", "2025", "378", "2025 fin kosten 378 vs 173; tick1436; primary official NBB WVV 65/66B"),
    ("bud_rlpz_pnl_2025", "2025", "26992", "2025 PnL 26992 vs 2792; tick1436; primary official NBB WVV 9904"),
    ("bud_rlpz_pnl_2024", "2024", "2792", "2024 PnL 2792 comparative; tick1436; primary official NBB WVV 9904"),
    ("bud_rlpz_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1436; primary official NBB WVV"),
    ("bud_rlpz_capex_2025", "2025", "0", "2025 MVA aanschaffingen empty; FVA aanschaf empty; tick1436; primary official NBB WVV 8169"),
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
    f"comm_rlpz_jr2025_bruto,Regionaal Landschap Pajottenland en Zennevallei VZW JR2025 leftover IGS dual (brutomarge 0.84m / pers 0.82m / cash 0.81m),{ENT},RL Pajottenland en Zennevallei VZW / 16 Pajottenland-Zennevallei cities,WVV VZW; NBB neerlegging; 16 Pajottenland-Zennevallei gemeenten + provincie Vlaams-Brabant,2026-03-19,1996,,842762,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00101632.pdf,Local leftover IGS map VL Pajottenland-Zennevallei landschap — 0.84m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 0.82m,Publish empty 70/73/60-61 split + pers 0.82m + trade drop + deferred drop + vennoten share-pct; do not keep leftover RLPZ VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>Pajottenland-Zennevallei>RLPZ>JR2025_L5,tick1436; assets 1055984 omzet empty diensten empty pers 816419 pnl 26992 equity 557432 cash 813995 debt 498552 capex 0 dividend 0 brutomarge 842762; FOI ready not sent; not TE-additive of 348bn; NOT Pajottegem city",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlpz_omzet_empty_pers_0_82m_cash_0_81m,Regionaal Landschap Pajottenland en Zennevallei VZW JR2025 leftover IGS: empty omzet 70 / pers 0.82m / cash 0.81m / brutomarge 0.84m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>Pajottenland-Zennevallei>RLPZ>JR2025_L5,842762,1055984,Leftover dual IGS VZW: assets 1.06m / equity 0.56m / pnl 0.03m / omzet empty / 73 empty / 60-61 empty / pers 0.82m 10.6 VTE / cash 0.81m / debt 0.50m / lev 0.15m / dividend 0,strong,{SRC},RL Pajottenland en Zennevallei VZW / 16 Pajottenland-Zennevallei cities,Local leftover IGS map VL Pajottenland-Zennevallei landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 0.84m / pers 0.82m / cash 0.81m / PnL 0.03m,6.6,6.4,2.2,6.1,Publish empty 70/73/60-61 split + pers 0.82m + trade drop + deferred drop + vennoten share-pct; do not keep leftover RLPZ VZW as dual unpublished vehicle,active,,tick1436; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Pajottegem city / AGB Gooik / AGB Herne / RLRL 1435 / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>Pajottenland-Zennevallei>RLPZ>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 842762 + pers 62 816419 / 10.6 VTE + cash 813995 vs 813508 + trade DROP 189311 vs 246816 + other recv 40759 + leveranciers 151502 vs 150122 + deferred DROP 276324 vs 369109 + vennoten share-pct unpublished + commissaris fee unpublished + relation to Pajottegem city unpublished,Leftover RLPZ VZW after leftover AGB hunt: 0.84m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Pajottenland en Zennevallei vzw / Bestuursorgaan,info@pajot-zenne.be,Donkerstraat 23 1750 Lennik,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlpz_jr2025_bruto,lb_rlpz_omzet_empty_pers_0_82m_cash_0_81m,{TS},{TS},tick1436 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (49199 bytes 13p deposit 2026-00101632). FOI ready not sent. NOT Pajottegem city. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Vlaamse Ardennen JR2025 CDN 2026-00367158 live leftover for next.",
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
if not last_s.startswith("rq_1436,"):
    raise SystemExit(f"expected last row rq_1436, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1436 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1436,RL Pajottenland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlpz,"
    "Completed: Regionaal Landschap Pajottenland en Zennevallei VZW leftover IGS / regionaal landschap of 16 mined Pajottenland-Zennevallei cities after leftover AGB hunt; KBO 0458.521.374 Actief; live JR2025 official NBB WVV VKT-VZW PDF (49199 bytes 13p deposit 2026-00101632; AV 19.03.2026; created 04.05.2026; neerlegging 2026-05-05; commissaris Impacct Accountants); sourced euros assets 1055984 omzet empty diensten empty pers 816419 pnl 26992 equity 557432 cash 813995 debt 498552 capex 0 dividend 0 brutomarge 842762; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.82m / cash 0.81m / trade drop / deferred drop; NOT Pajottegem city,"
    f"{GAP},2026-08-19T12:20:00Z,{TS},"
    "tick1436 RL Pajottenland en Zennevallei VZW leftover IGS residual; KBO 0458.521.374; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1437 residual dual L5 VL"
)
spawn = (
    "rq_1437,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1436 done including RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Vlaamse Ardennen tot Dender 0449.013.097 JR2025 CDN 2026-00367158 LIVE leftover — STRONG next leftover RL; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1436 after RL Pajottenland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Vlaamse Ardennen if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1436=done + rq_1437 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1436 RL Pajottenland leftover IGS residual; KBO 0458.521.374; live JR2025 NBB WVV PDF; sourced euros assets 1055984 omzet empty diensten empty pers 816419 pnl 26992 equity 557432 cash 813995 debt 498552 capex 0 dividend 0 brutomarge 842762; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.82m / cash 0.81m / trade drop / deferred drop; NOT Pajottegem city; next rq_1437 residual dual L5 VL leftover RL Vlaamse Ardennen if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1436,1436,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1436")

# --- loop_log ---
entry = (
    "\n## Tick 1436 - 2026-08-19 - rq_1436 RL Pajottenland dual residual leftover\n"
    "- Unit: Regionaal Landschap Pajottenland en Zennevallei VZW / RLPZ (leftover IGS / regionaal landschap of 16 mined Pajottenland-Zennevallei cities; 1 VE) after residual dual hunt (KBO **0458.521.374**; official pajot-zenne.be; live NBB WVV VKT-VZW deposit **2026-00101632** PDF 49199 bytes / 13p; AV **19.03.2026**; created **04.05.2026**; pdfinfo **05.05.2026**; neerlegging **2026-05-05**; model **VKT-VZW** 23.0.8 m04-f; commissaris Impacct Accountants 0687.783.745 / Vanderwegen Kris ITAA 11 374 864; VKT-VZW 6.2/6.3/6.5/6.6/6.8/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.4 + 6.7 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022 (SBM last 2023-00125347); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Gooik / AGB Herne / AGB Ternat / AGB Beersel / EVA Kinderopvang Dilbeek) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381). Leftover IGS Regionaal Landschap Pajottenland en Zennevallei VZW statutory CDN live this tick (HTTP 200 / application/pdf / 49199 / 13p; SBM jaar **2025-12-31**; neerlegging 2026-05-05) — taken (hunt order #2 leftover unmined RL VZW of mined Pajottenland-Zennevallei cities with full WVV balans; STRONG next leftover RL after RLRL 1435). Distinct from already-mined **Gemeente Pajottegem** (fusion Gooik+Galmaarden+Herne; KBO GE 1010.784.540; NOT this entity) / AGB Gooik / AGB Herne / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Erfgoed Brabantse Kouters 1428. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Pajottenland / 0458.521.374 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **19.04.1996**; statutaire naam REGIONAAL LANDSCHAP PAJOTTENLAND EN ZENNEVALLEI since 05.12.2011; afkorting RL P&Z since 05.12.2011; VZW since 19.04.1996; zetel Donkerstraat 23 1750 Lennik since 01.01.2025; **1 VE**; KBO no tel/e-mail/web; official site https://www.pajot-zenne.be/; e-mail info@pajot-zenne.be; tel 02 452 60 45; directeur Alwin Loeckx; NACE RSZ 91.420; Werkgever RSZ since 16.10.1996; btw since 01.01.2018. WVV 2.1 voorzitter Elke Zelderloo. Dilbeek official page 16 leden-gemeenten: Affligem / Beersel / Bever / Dilbeek / Drogenbos / Galmaarden / Gooik / Halle / Herne / Lennik / Liedekerke / Pepingen / Roosdaal / Sint-Genesius-Rode / Sint-Pieters-Leeuw / Ternat. Plus provincie Vlaams-Brabant. Named share-% unpublished. Contact info@pajot-zenne.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (SBM table assets 1055985 vs PDF 1055984 — PDF wins). Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **816419** / **10,6 VTE**): assets **1055984** (was 1119910); fixed **1701** / IVA empty / MVA **451** (machines **451**) / FVA **1250**; current **1054284**; ST recv **230070** (trade **189311 DROP** vs 246816 / other **40759**); cash **813995** vs 813508; prepaid **10219**; equity **557432** (bestemde fondsen **294378**; overgedragen **263054**); voorzieningen empty; schulden **498552** (LT empty; ST **222228** waarvan leveranciers **151502** vs 150122 + soc/bezold **70725**; deferred **276324 DROP** vs 369109); brutomarge **842762** vs 787702; omzet empty; 73 empty; 60/61 empty; pers **816419** / **10,6 VTE** / 16269 uur / YE **10,4**; afschr **796**; andere bedrijfskosten empty; expl **25548** vs 2085; fin opbr **1822**; fin kosten **378**; tax empty; PnL **26992** vs 2792; dividend **0**; over te dragen **263054**; capex **0**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlpz` parent `sec_flanders`; budgets +42 executed; commitments +1 envelope 842762 AV 19.03.2026; leaderboard +1 annual 842762 / total 1055984; foi_queue +1 status=ready never sent; research_queue surgical rq_1436=done + rq_1437 spawn; loop_state ticks_completed=1436.\n"
    "- FOI: `gap_rlpz_omzet_empty_pers_0_82m_cash_0_81m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 0.82m 10.6 VTE deelwerking unpublished / trade DROP 0.19m / deferred DROP 0.28m / cash 0.81m / vennoten share-pct / relation to Pajottegem city unpublished / commissaris fee unpublished.\n"
    "- Next: rq_1437 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Vlaamse Ardennen tot Dender **0449.013.097** JR2025 CDN **2026-00367158** LIVE — STRONG next leftover RL. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024; Pajottegem city already mined).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1436")
print("tick1436 writes done")
