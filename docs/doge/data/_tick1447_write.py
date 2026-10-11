#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1447 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T13:10:00Z"
ENT = "vzw_bgvb"
SRC = "src_bgvb_jr2025_av"
GAP = "gap_bgvb_nbb_cdn_403_pers_23k_cash_0_54m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_bgvb_jr2025_av,Bosgroep Vlaams-Brabant VZW official AV ontwerp-balans 2025,https://cms.ice.be/files/160/bvb-ontwerp-balans-2025.pdf,Bosgroep Vlaams-Brabant VZW,2026-08-19,budget,tick1447; official AV ontwerp-balans IJ 31.12.2025 AJ2026 PDF 7p / 126986 bytes; pdfinfo created 13.02.2026; AV 14.03.2026; KBO 0683.509.015; assets 567212 cash 539584 debt 100709 omzet 54599 code73 22741 code60 28448 code61 38977 pers 23400 pnl 8590; NBB Micro 2026-00374479 filed 03.08.2026 CDN HEAD 403",
    "src_bgvb_site,Bosgroep Vlaams-Brabant official site,https://www.bosgroepvlaamsbrabant.be/,Bosgroep Vlaams-Brabant VZW,2026-08-19,official_register,tick1447; leftover IGS / Bosgroep of mined Vlaams-Brabant cities; zetel Diestsevest 54 bus 101 3000 Leuven; contact info@bosgroepvlaamsbrabant.be; tel 016 26 76 00; AV 14.03.2026 documents",
    "src_kbo_bgvb_0683509015,KBO Bosgroep Vlaams-Brabant 0683.509.015,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0683509015,KBO Public Search FOD Economie,2026-08-19,official_register,tick1447; Actief since 19.10.2017; naam/afkorting BVB since 23.09.2017; zetel Diestsevest 54 bus 101 3000 Leuven since 08.09.2021; 0 VE; VZW; NACE 02.400 / 46.832; btw since 01.04.2019; 13 functiehouders; absorbed 0899.429.134 since 10.02.2021",
    "src_bgvb_foi_contact,Bosgroep Vlaams-Brabant FOI channel (info@bosgroepvlaamsbrabant.be; Diestsevest 54 Leuven),https://www.bosgroepvlaamsbrabant.be/nl/av-18-3-documenten/index.htm,Bosgroep Vlaams-Brabant VZW,2026-08-19,official_register,tick1447; province-wide leftover Bosgroep + provincie Vlaams-Brabant; NOT RLBK / RLD / RLNH / RLZH / RLPZ / BGOV",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_bgvb," in raw or raw.startswith(b"vzw_bgvb,"):
    raise SystemExit("vzw_bgvb already present")
if b"0683.509.015" in raw or b"0683509015" in raw:
    raise SystemExit("Bosgroep Vlaams-Brabant KBO already present")
row = (
    "vzw_bgvb,Bosgroep Vlaams-Brabant VZW (leftover IGS / Bosgroep of mined Vlaams-Brabant cities; NOT RL Brabantse Kouters / RL Dijleland / RL Noord-Hageland / RL Zuid-Hageland / RL Pajottenland / BGOV),"
    "Bosgroep Vlaams-Brabant ASBL (IGS residuel / groupe forestier Brabant flamand),"
    "Bosgroep Vlaams-Brabant leftover IGS / forest-group VZW of mined Flemish-Brabant municipalities (not RLBK / RLD / RLNH / RLZH / RLPZ / BGOV),"
    "other,sec_flanders,nl,https://www.bosgroepvlaamsbrabant.be/,info@bosgroepvlaamsbrabant.be,Diestsevest 54 bus 101 3000 Leuven,"
    "tick1447 leftover residual IGS/Bosgroep VZW of mined Vlaams-Brabant cities after leftover AGB hunt; KBO 0683.509.015 Actief since 19.10.2017; official AV ontwerp-balans 2025 PDF downloads; NBB 2026-00374479 filed 03.08.2026 CDN HEAD 403; sourced euros assets 567212 omzet 54599 diensten 38977 pers 23400 pnl 8590 equity 457913 cash 539584 debt 100709 capex unpublished dividend 0 bedrijfsopbr 93888; FOI ready NBB PDF / unallocated result / pers 23k / 0 VE / leden share-pct; distinct from already-mined RLBK 1442 / RLD 1440 / RLNH 1439 / RLZH 1434 / RLPZ 1436 / Erfgoed Brabantse Kouters 1428 / IGO Holsbeek 1409 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RLML 1443"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_bgvb")

# --- budgets (PDF cents rounded nearest euro) ---
BUDGETS = [
    ("bud_bgvb_assets_2025", "2025", "567212", "2025 assets 567211.79 rounded 567212; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_fixed_2025", "2025", "205", "2025 vaste activa 204.73 rounded 205; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_iva_2025", "2025", "0", "2025 IVA empty; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_mva_2025", "2025", "205", "2025 MVA 204.73 computerinstallaties aanschaf YE 4118 afschr YE 3913; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_fva_2025", "2025", "0", "2025 FVA empty; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_current_2025", "2025", "567007", "2025 vlottend 567007.06 rounded 567007; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_strecv_2025", "2025", "20730", "2025 ST vorderingen 20729.71 rounded 20730; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_trade_2025", "2025", "17276", "2025 handelsvorderingen 17276.48 rounded 17276; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_othrecv_2025", "2025", "3453", "2025 overige vorderingen 3453.23 rounded 3453; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_cash_2025", "2025", "539584", "2025 liquide middelen 539584.18 rounded 539584; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_prepaid_2025", "2025", "6693", "2025 prepaid 6693.17 rounded 6693; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_equity_2025", "2025", "457913", "2025 EV published 457913.49 before unallocated result 8590; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_bestemde_2025", "2025", "61999", "2025 bestemde fondsen 61999.05 rounded 61999; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_overgedragen_2025", "2025", "395914", "2025 overgedragen 395914.44 rounded 395914 before result; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_debt_2025", "2025", "100709", "2025 schulden 100708.55 rounded 100709 (LT empty); tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_stdebt_2025", "2025", "100709", "2025 ST schulden 100708.55 rounded 100709; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_lev_2025", "2025", "3758", "2025 leveranciers 3757.58 rounded 3758; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_othdebt_2025", "2025", "96951", "2025 overige schulden 96950.97 (houtverkoop waarborgen / koopsom / beheersubsidies); tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_unalloc_2025", "2025", "8590", "2025 unallocated result (+) 8589.75 on passiva; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_bedrijfsopbr_2025", "2025", "93888", "2025 bedrijfsopbrengsten 93887.90 rounded 93888 (no 9900 brutomarge line); tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_omzet_2025", "2025", "54599", "2025 omzet 54599.29 rounded 54599; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_lidgeld_2025", "2025", "22741", "2025 lidgeld/subsidies 73 22740.80 (provincie 48400 + 96681 - uitgekeerde 121856); tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_andere_2025", "2025", "16548", "2025 andere bedrijfsopbrengsten 16547.81 rounded 16548; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_aankopen_2025", "2025", "28448", "2025 aankopen 60 28448.48 rounded 28448; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_diensten_2025", "2025", "38977", "2025 diensten 61 38977.15 rounded 38977; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_pers_2025", "2025", "23400", "2025 pers 23400 diverse personeelskosten (no VTE); tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_afschr_2025", "2025", "1339", "2025 afschrijvingen 1339.19 rounded 1339; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_expl_2025", "2025", "1723", "2025 expl +1723.08 rounded 1723; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_finopbr_2025", "2025", "7490", "2025 fin opbr 7490.00; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_finkost_2025", "2025", "623", "2025 fin kosten 623.33 rounded 623; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_tax_2025", "2025", "0", "2025 tax empty; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_pnl_2025", "2025", "8590", "2025 PnL +8589.75 rounded 8590; tick1447; primary official AV ontwerp-balans"),
    ("bud_bgvb_div_2025", "2025", "0", "2025 dividend 0; tick1447; primary official AV ontwerp-balans"),
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
    f"comm_bgvb_jr2025_opbr,Bosgroep Vlaams-Brabant VZW JR2025 leftover IGS dual (bedrijfsopbr 0.09m / pers 23k / cash 0.54m),{ENT},Bosgroep Vlaams-Brabant VZW / mined Vlaams-Brabant cities,WVV VZW; official AV ontwerp-balans; provincie Vlaams-Brabant,2026-03-14,2017,,93888,,,active,https://cms.ice.be/files/160/bvb-ontwerp-balans-2025.pdf,Local leftover IGS map VL Bosgroep Vlaams-Brabant — 0.09m bedrijfsopbr / omzet 55k / pers 23k / cash 0.54m,Publish NBB 2026-00374479 PDF + unallocated result + pers 23k + 0 VE + vennoten share-pct; do not keep leftover BVB VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>BosgroepVB>JR2025_L5,tick1447; assets 567212 omzet 54599 diensten 38977 pers 23400 pnl 8590 equity 457913 cash 539584 debt 100709 capex unpublished dividend 0 bedrijfsopbr 93888; NBB CDN 403; FOI ready not sent; not TE-additive of 348bn; NOT RLBK / RLD / RLNH / RLZH / RLPZ / BGOV",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_bgvb_nbb_cdn_403_pers_23k_cash_0_54m,Bosgroep Vlaams-Brabant VZW JR2025 leftover IGS: NBB CDN 403 / pers 23k / cash 0.54m / bedrijfsopbr 0.09m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>BosgroepVB>JR2025_L5,93888,567212,Leftover dual IGS/Bosgroep VZW: assets 0.57m / equity 0.46m / pnl +9k / omzet 55k / 73 23k / 60 28k / 61 39k / pers 23k no VTE / cash 0.54m / debt 0.10m / dividend 0 / NBB 2026-00374479 CDN 403,strong,{SRC},Bosgroep Vlaams-Brabant VZW / mined Vlaams-Brabant cities,Local leftover IGS map VL Bosgroep Vlaams-Brabant — JR2025 official AV balans live; NBB filed CDN 403 FOI,Official AV ontwerp-balans 2026-08-19: bedrijfsopbr 0.09m / pers 23k / cash 0.54m / PnL +9k,6.2,5.4,2.4,5.8,Publish NBB 2026-00374479 PDF + unallocated result + pers 23k + 0 VE + vennoten share-pct; do not keep leftover BVB VZW as dual unpublished vehicle,active,,tick1447; leftover IGS/Bosgroep after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined RLBK 1442 / RLD 1440 / RLNH 1439 / RLZH 1434 / RLPZ 1436 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RLML 1443",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>BosgroepVB>JR2025_L5,{ENT},NBB 2026-00374479 filed 03.08.2026 Micro model CDN HEAD 403 + unallocated result 8590 outside EV + pers 23400 diverse personeelskosten no VTE + 0 VE + cash 539584 + othdebt 96951 houtverkoop/koopsom/beheersubsidies + lidgeld 73 22741 (provincie 48400+96681-121856) + omzet 54599 + diensten 38977 + capex unpublished + vennoten share-pct unpublished + relation to RLBK/RLD/RLNH/RLZH/RLPZ/IGO Holsbeek/Koepel/provincie unpublished,Leftover BVB VZW after leftover AGB hunt: 0.09m bedrijfsopbr / NBB filed but CDN 403 hides public-perimeter bosgroep vehicle,8,Bosgroep Vlaams-Brabant vzw / Bestuursorgaan,info@bosgroepvlaamsbrabant.be,Diestsevest 54 bus 101 3000 Leuven,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_bgvb_jr2025_opbr,lb_bgvb_nbb_cdn_403_pers_23k_cash_0_54m,{TS},{TS},tick1447 leftover IGS/Bosgroep after honest leftover AGB hunt; live JR2025 official AV ontwerp-balans PDF now extracted (126986 bytes 7p). NBB 2026-00374479 CDN 403. FOI ready not sent. NOT RLBK / RLD / RLNH / RLZH / RLPZ / BGOV. Leftover Bosgroep Antwerpse Gordel 0884.382.751 JR2025 filed 09.05.2026 deposit id unpublished. Leftover Zuiderkempen / Houtland WVL / IJzer en Leie / Limburg / Kempen Noord / Koepel still no live CDN. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong/Oost-Haspengouw still no JR2025. Leftover RL Houtland still JR2024. Leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening.",
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
if not last_s.startswith("rq_1447,"):
    raise SystemExit(f"expected last row rq_1447, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1447 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1447,Bosgroep Vlaams-Brabant JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_bgvb,"
    "Completed: Bosgroep Vlaams-Brabant VZW leftover IGS / Bosgroep of mined Vlaams-Brabant cities after leftover AGB hunt; KBO 0683.509.015 Actief; live JR2025 official AV ontwerp-balans PDF (126986 bytes 7p; AV 14.03.2026; created 13.02.2026); NBB Micro 2026-00374479 filed 03.08.2026 CDN HEAD 403; sourced euros assets 567212 omzet 54599 diensten 38977 pers 23400 pnl 8590 equity 457913 cash 539584 debt 100709 capex unpublished dividend 0 bedrijfsopbr 93888; FOI ready NBB PDF / unallocated result / pers 23k / 0 VE / leden share-pct; NOT RLBK / RLD / RLNH / RLZH / RLPZ / BGOV,"
    f"{GAP},2026-08-19T13:05:00Z,{TS},"
    "tick1447 Bosgroep Vlaams-Brabant leftover IGS/Bosgroep residual; KBO 0683.509.015; live JR2025 official AV PDF; NBB CDN 403; sourced euros; FOI ready not sent; next rq_1448 residual dual L5 VL leftover Bosgroep Antwerpse Gordel if CDN id live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen"
)
spawn = (
    "rq_1448,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1447 done including Bosgroep Vlaams-Brabant 1447 leftover IGS official AV JR2025 / Bosgroep Oost-Vlaanderen 1446 leftover IGS live NBB WVV / RL Kleine en Grote Nete 1445 leftover IGS live NBB WVV / RL Haspengouw 1444 leftover IGS live NBB WVV / RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover Bosgroep Antwerpse Gordel 0884.382.751 Companyweb JR2025 neergelegd 09.05.2026 — take if a 2026pdf deposit id now downloads (STRONG next leftover Bosgroep); leftover Bosgroep Zuiderkempen 0860.780.968 only if a 2025 CDN now downloads; leftover Bosgroep WVL Houtland 0866.482.291 / IJzer en Leie 0816.706.346 / Limburg 0668.619.317 / Kempen Noord 0476.530.217 / Koepel 0820.176.768 only if a 2025 CDN is live; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover RL West-Vlaamse Hart 0800.422.125 still no jaarrekening — take only if a 2025 CDN now downloads; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; Oost-Haspengouw IOED still no JR; RL Houtland still 2024; RL West-Vlaamse Hart still no jaarrekening; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1447 after Bosgroep Vlaams-Brabant leftover IGS official AV JR2025; next residual dual L5 VL leftover Bosgroep Antwerpse Gordel if a 2025 CDN is now live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1447=done + rq_1448 spawned; keep", last_line_start)

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
    f"tick1447 Bosgroep Vlaams-Brabant leftover IGS/Bosgroep residual; KBO 0683.509.015; live JR2025 official AV ontwerp-balans PDF; NBB 2026-00374479 CDN 403; sourced euros assets 567212 omzet 54599 diensten 38977 pers 23400 pnl 8590 equity 457913 cash 539584 debt 100709 capex unpublished dividend 0 bedrijfsopbr 93888; FOI ready NBB PDF / unallocated result / pers 23k / 0 VE; NOT RLBK / RLD / RLNH / RLZH / RLPZ / BGOV / RLKGN / RLHV / RLML; next rq_1448 residual dual L5 VL leftover Bosgroep Antwerpse Gordel if CDN id live else leftover AGB/IOED/cultuur-IGS/Houtland/Hart/other Bosgroepen; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1447,1447,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1447")

entry = (
    "\n## Tick 1447 - 2026-08-19 - rq_1447 Bosgroep Vlaams-Brabant dual residual leftover\n"
    "- Unit: Bosgroep Vlaams-Brabant VZW / BVB (leftover IGS / Bosgroep of mined Vlaams-Brabant cities; 0 VE) after residual dual hunt (KBO **0683.509.015**; official bosgroepvlaamsbrabant.be; live official AV ontwerp-balans 2025 PDF **126986** bytes / 7p; AV **14.03.2026**; pdfinfo created **13.02.2026**; NBB Micro model vereniging deposit **2026-00374479** filed **03.08.2026** year-end **30.12.2025** — SBM CDN HEAD **403** this tick). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (2026pdf 2026-00553588 HEAD 403 this tick; 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member-province cities already mined (AGA Asse / AGB Grimbergen / AGB Steenokkerzeel / AGB Zaventem / AGB Zemst / AG Vilvoorde / AGB Merchtem / AGB Haacht / AGB Boortmeerbeek / AGB De Kouter Herent / AG Museum Leuven / AGB Ternat / AGB Tremelo / Aarschot AGB / IGO Holsbeek / Hofheide) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 / Oost-Haspengouw still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover RL West-Vlaamse Hart **0800.422.125** still no jaarrekening — not taken. Other leftover Bosgroepen: WVL Houtland 0866.482.291 no NBB 2025 found; IJzer en Leie 0816.706.346 Companyweb geen jaarrekening; Limburg 0668.619.317 Companyweb geen jaarrekening; Kempen Noord 0476.530.217 Companyweb geen jaarrekening; Koepel 0820.176.768 NBB consult No results; Antwerpse Gordel 0884.382.751 Companyweb JR2025 neergelegd 09.05.2026 but deposit id unpublished / no CDN this tick; Zuiderkempen 0860.780.968 Belscope claims JR2025 (euros forbidden) / Companyweb geen jaarrekening. Leftover IGS Bosgroep Vlaams-Brabant official AV ontwerp-balans live this tick (HTTP 200 / application/pdf / 126986 / 7p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined IGS / Bosgroep of mined Vlaams-Brabant cities with live 2025 statutory-style PDF after leftover AGB hunt). Distinct from already-mined **RL Brabantse Kouters** (vzw_rlbk tick 1442; KBO 0874.904.564; NOT this entity) / **RL Dijleland** 1440 / **RL Noord-Hageland** 1439 / **RL Zuid-Hageland** 1434 / **RL Pajottenland** 1436 / Erfgoed Brabantse Kouters 1428 / IGO Holsbeek 1409 / Hofheide 1395 / BGOV 1446 / RLKGN 1445 / RLHV 1444 / RLML 1443. First confirmed not already extracted as JR2025 euros: no Bosgroep Vlaams-Brabant / 0683.509.015 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **19.10.2017**; statutaire naam Bosgroep Vlaams-Brabant since 23.09.2017; afkorting BVB since 23.09.2017; VZW since 23.09.2017; zetel Diestsevest 54 bus 101 3000 Leuven since 08.09.2021; **0 VE**; official site https://www.bosgroepvlaamsbrabant.be/; contact info@bosgroepvlaamsbrabant.be since 14.03.2026; tel 016 26 76 00; NACE btw 02.400 / 46.832; btw since 01.04.2019; **13 functiehouders**. Bestuurders include Nevens Bart / Hanssens William since 14.03.2026 / Vander Perre Hans since 14.03.2026. Absorbed Bosgroep Zuidwest Brabant 0899.429.134 since 10.02.2021. Official site province-wide Vlaams-Brabant + provincie. Named member-city share-% unpublished. Contact info@bosgroepvlaamsbrabant.be. NBB consult skipped (403/SPA); SBM CDN 2026-00374479 HEAD 403; euros extracted from the official AV ontwerp-balans PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor HTML blocked this tick (IP blacklist) — official AV PDF wins. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official AV ontwerp-balans; PDF cents rounded nearest euro; **omzet 70 filed 54599**; **lidgeld/subsidies 73 filed 22741**; **60 filed 28448** / **61 filed 38977**; no 9900 brutomarge line — bedrijfsopbrengsten **93888**; pers 62 **23400** / **no VTE**): assets **567212**; fixed **205** / IVA **0** / MVA **205** (computerinstallaties aanschaf YE **4118** / afschr YE **3913**) / FVA **0**; current **567007**; ST recv **20730** (trade **17276** / other **3453**); geldbeleg empty; cash **539584**; prepaid **6693**; equity published **457913** (bestemde **61999**; overgedragen **395914**) + unallocated result **(+) 8590** on passiva; voorzieningen empty; schulden **100709** (LT empty; ST **100709** waarvan leveranciers **3758** + overige **96951**); bedrijfsopbrengsten **93888**; omzet **54599**; 73 **22741** (provincie eigen 48400 + werken derden 96681 − uitgekeerde 121856 − Molenbeek −484); andere **16548**; 60 **28448**; 61 **38977**; pers **23400**; afschr **1339**; expl **+1723**; fin opbr **7490**; fin kosten **623**; tax **0**; PnL **+8590**; dividend **0**; capex unpublished. PDF 1-euro rounding: trade+other 20729 vs published ST recv 20730.\n"
    f"- CSVs: sources +4; entities +1 `vzw_bgvb` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 93888 AV 14.03.2026; leaderboard +1 annual 93888 / total 567212; foi_queue +1 status=ready never sent; research_queue surgical rq_1447=done + rq_1448 spawn; loop_state ticks_completed=1447. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_bgvb_nbb_cdn_403_pers_23k_cash_0_54m_l5` ready not sent — NBB 2026-00374479 CDN 403 / unallocated result 8590 / pers 23k no VTE / 0 VE / cash 0.54m / othdebt 0.10m / lidgeld 73 23k / capex unpublished / vennoten share-pct / relation to RLBK / RLD / RLNH / RLZH / RLPZ / IGO Holsbeek / Koepel / provincie unpublished.\n"
    "- Next: rq_1448 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover Bosgroep Antwerpse Gordel **0884.382.751** Companyweb JR2025 neergelegd 09.05.2026 — take if a 2026pdf deposit id now downloads (STRONG next leftover Bosgroep). Leftover Bosgroep Zuiderkempen 0860.780.968 only if a 2025 CDN now downloads. Leftover Bosgroep WVL Houtland / IJzer en Leie / Limburg / Kempen Noord / Koepel only if a 2025 CDN is live. Leftover RL Houtland & Polders **0472.947.254** only if JR2025 now live. Leftover RL West-Vlaamse Hart **0800.422.125** only if a 2025 CDN now downloads. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong / Oost-Haspengouw if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined Bosgroep Vlaams-Brabant 1447 / Bosgroep Oost-Vlaanderen 1446 / RL Kleine en Grote Nete 1445 / RL Haspengouw 1444 / RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1447 -" in lraw:
    raise SystemExit("loop_log already has tick 1447 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1447")
print("DONE tick 1447")
