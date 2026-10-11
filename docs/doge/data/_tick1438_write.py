#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1438 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:10:00Z"
ENT = "vzw_rlwh"
SRC = "src_rlwh_jr2025_nbb"
GAP = "gap_rlwh_omzet_empty_pers_1_28m_cash_1_24m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlwh_jr2025_nbb,Regionaal Landschap Westhoek VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00109364.pdf,NBB / RL Westhoek VZW,2026-08-19,budget,tick1438; VKT-VZW 23.0.9 m04-f PDF 19p / 63056 bytes deposit 2026-00109364; AV 07.05.2026; created 12.05.2026; pdfinfo 12.05.2026; neerlegging 2026-05-13; KBO 0469.129.810; assets 1737911 cash 1237464 debt 694016 brutomarge 1462915 omzet empty code73 empty code60_61 empty pers 1282901 pnl 123056; no commissaris listed",
    "src_rlwh_site,Regionaal Landschap Westhoek official site,https://www.rlwesthoek.be/,RL Westhoek VZW,2026-08-19,official_register,tick1438; leftover IGS / regionaal landschap of 17 Westhoek cities; zetel Iepersteenweg 56 8600 Diksmuide; contact info@rlwesthoek.be; tel 0489 86 66 83; coordinator Niels Dabaut; voorzitter Jurgen Vanlerberghe",
    "src_kbo_rlwh_0469129810,KBO Regionaal Landschap Westhoek 0469.129.810,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0469129810,KBO Public Search FOD Economie,2026-08-19,official_register,tick1438; Actief since 11.06.1999; naam since 05.12.2017; afkorting RLW since 01.07.2023; zetel Iepersteenweg(W) 56 8600 Diksmuide since 05.12.2017; 2 VE; VZW; NACE 91.420; Werkgever RSZ since 15.06.2001; aanbestedende overheid since 11.06.1999",
    "src_rlwh_foi_contact,RL Westhoek FOI channel (info@rlwesthoek.be; Iepersteenweg 56 Diksmuide),https://www.rlwesthoek.be/contact/,RL Westhoek VZW,2026-08-19,official_register,tick1438; 17 member cities + provincie West-Vlaanderen; voorzitter Jurgen Vanlerberghe; coordinator Niels Dabaut; NOT DVV Westhoek igs_westhoek_dv",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlwh," in raw or raw.startswith(b"vzw_rlwh,"):
    raise SystemExit("vzw_rlwh already present")
if b"0469.129.810" in raw or b"0469129810" in raw:
    raise SystemExit("RL Westhoek KBO already present")
row = (
    "vzw_rlwh,Regionaal Landschap Westhoek VZW (leftover IGS / regionaal landschap of 17 mined Westhoek cities; NOT DVV Westhoek),"
    "Regionaal Landschap Westhoek ASBL (IGS residuel / paysage regional Westhoek),"
    "Regionaal Landschap Westhoek leftover IGS / regional landscape VZW of 17 Westhoek municipalities (not DVV Westhoek),"
    "other,sec_flanders,nl,https://www.rlwesthoek.be/,info@rlwesthoek.be,Iepersteenweg 56 8600 Diksmuide,"
    "tick1438 leftover residual IGS VZW of mined Westhoek cities after leftover AGB hunt; KBO 0469.129.810 Actief since 11.06.1999; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1737911 omzet empty diensten empty pers 1282901 pnl 123056 equity 785330 cash 1237464 debt 694016 capex 120377 dividend 0 brutomarge 1462915; FOI ready omzet empty / 73 empty / 60-61 empty / pers 1.28m / cash 1.24m / trade JUMP / deferred JUMP; distinct from already-mined DVV Westhoek 1415 / CO7 1420 / Viertoren 1421 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlwh")

# --- budgets ---
BUDGETS = [
    ("bud_rlwh_assets_2025", "2025", "1737911", "2025 assets 1737911 VKT-VZW 20/58; tick1438; primary official NBB WVV"),
    ("bud_rlwh_assets_2024", "2024", "1477379", "2024 assets 1477379 comparative; tick1438; primary official NBB WVV 20/58"),
    ("bud_rlwh_fixed_2025", "2025", "168736", "2025 vaste activa 168736 vs 105540; tick1438; primary official NBB WVV 21/28"),
    ("bud_rlwh_iva_2025", "2025", "0", "2025 IVA empty; tick1438; primary official NBB WVV 21"),
    ("bud_rlwh_mva_2025", "2025", "168736", "2025 MVA 168736 vs 105540; tick1438; primary official NBB WVV 22/27"),
    ("bud_rlwh_machines_2025", "2025", "2904", "2025 machines 2904 vs 1122; tick1438; primary official NBB WVV 23"),
    ("bud_rlwh_meubilair_2025", "2025", "154235", "2025 meubilair 154235 vs 104418; tick1438; primary official NBB WVV 24"),
    ("bud_rlwh_overige_mva_2025", "2025", "11596", "2025 overige MVA 11596 vs empty; tick1438; primary official NBB WVV 26"),
    ("bud_rlwh_fva_2025", "2025", "0", "2025 FVA empty; tick1438; primary official NBB WVV 28"),
    ("bud_rlwh_current_2025", "2025", "1569175", "2025 vlottend 1569175 vs 1371839; tick1438; primary official NBB WVV 29/58"),
    ("bud_rlwh_voorraden_2025", "2025", "1536", "2025 voorraden 1536 vs 1015; tick1438; primary official NBB WVV 30/36"),
    ("bud_rlwh_strecv_2025", "2025", "324732", "2025 ST vorderingen 324732 vs 214769; tick1438; primary official NBB WVV 40/41"),
    ("bud_rlwh_strecv_2024", "2024", "214769", "2024 ST vorderingen 214769 comparative; tick1438; primary official NBB WVV 40/41"),
    ("bud_rlwh_trade_2025", "2025", "202195", "2025 handelsvorderingen 202195 JUMP vs 66607; tick1438; primary official NBB WVV 40"),
    ("bud_rlwh_trade_2024", "2024", "66607", "2024 handelsvorderingen 66607 comparative; tick1438; primary official NBB WVV 40"),
    ("bud_rlwh_othrecv_2025", "2025", "122537", "2025 overige vorderingen 122537 vs 148162; tick1438; primary official NBB WVV 41"),
    ("bud_rlwh_cash_2025", "2025", "1237464", "2025 liquide middelen 1237464 vs 1151609; tick1438; primary official NBB WVV 54/58"),
    ("bud_rlwh_cash_2024", "2024", "1151609", "2024 liquide middelen 1151609 comparative; tick1438; primary official NBB WVV 54/58"),
    ("bud_rlwh_prepaid_2025", "2025", "5443", "2025 prepaid 5443 vs 4446; tick1438; primary official NBB WVV 490/1"),
    ("bud_rlwh_equity_2025", "2025", "785330", "2025 EV 785330 vs 662273; tick1438; primary official NBB WVV 10/15"),
    ("bud_rlwh_equity_2024", "2024", "662273", "2024 EV 662273 comparative; tick1438; primary official NBB WVV 10/15"),
    ("bud_rlwh_bestemde_2025", "2025", "347692", "2025 bestemde fondsen 347692 unchanged; tick1438; primary official NBB WVV 13"),
    ("bud_rlwh_overgedragen_2025", "2025", "437638", "2025 overgedragen winst 437638 vs 314582; tick1438; primary official NBB WVV 14"),
    ("bud_rlwh_voorz_2025", "2025", "258565", "2025 voorzieningen 258565 all pensions unchanged; tick1438; primary official NBB WVV 16/160"),
    ("bud_rlwh_debt_2025", "2025", "694016", "2025 schulden 694016 vs 556540 (LT empty); tick1438; primary official NBB WVV 17/49"),
    ("bud_rlwh_debt_2024", "2024", "556540", "2024 schulden 556540 comparative; tick1438; primary official NBB WVV 17/49"),
    ("bud_rlwh_stdebt_2025", "2025", "293907", "2025 ST schulden 293907 vs 294183; tick1438; primary official NBB WVV 42/48"),
    ("bud_rlwh_lev_2025", "2025", "89494", "2025 leveranciers 89494 DROP vs 128917; tick1438; primary official NBB WVV 440/4"),
    ("bud_rlwh_lev_2024", "2024", "128917", "2024 leveranciers 128917 comparative; tick1438; primary official NBB WVV 440/4"),
    ("bud_rlwh_tax_2025", "2025", "35778", "2025 belastingen 35778 vs 34075; tick1438; primary official NBB WVV 450/3"),
    ("bud_rlwh_bezold_2025", "2025", "168634", "2025 bezoldigingen/sociale lasten 168634 vs 131191; tick1438; primary official NBB WVV 454/9"),
    ("bud_rlwh_deferred_2025", "2025", "400109", "2025 overlopend passief 400109 JUMP vs 262357; tick1438; primary official NBB WVV 492/3"),
    ("bud_rlwh_deferred_2024", "2024", "262357", "2024 overlopend passief 262357 comparative; tick1438; primary official NBB WVV 492/3"),
    ("bud_rlwh_brutomarge_2025", "2025", "1462915", "2025 brutomarge 1462915 vs 1172208; omzet 70 empty; 73 empty; 60/61 empty; tick1438; primary official NBB WVV 9900"),
    ("bud_rlwh_brutomarge_2024", "2024", "1172208", "2024 brutomarge 1172208 comparative; tick1438; primary official NBB WVV 9900"),
    ("bud_rlwh_pers_2025", "2025", "1282901", "2025 pers 1282901 / 18 VTE vs 1073274 / 16.4; tick1438; primary official NBB WVV 62"),
    ("bud_rlwh_pers_2024", "2024", "1073274", "2024 pers 1073274 / 16.4 VTE comparative; tick1438; primary official NBB WVV 62"),
    ("bud_rlwh_afschr_2025", "2025", "57180", "2025 afschrijvingen 57180 vs 29077; tick1438; primary official NBB WVV 630"),
    ("bud_rlwh_andere_2025", "2025", "307", "2025 andere bedrijfskosten 307 vs 31; tick1438; primary official NBB WVV 640/8"),
    ("bud_rlwh_expl_2025", "2025", "122527", "2025 expl 122527 vs 69826; tick1438; primary official NBB WVV 9901"),
    ("bud_rlwh_expl_2024", "2024", "69826", "2024 expl 69826 comparative; tick1438; primary official NBB WVV 9901"),
    ("bud_rlwh_finopbr_2025", "2025", "804", "2025 fin opbr 804 vs 0; tick1438; primary official NBB WVV 75/76B"),
    ("bud_rlwh_finkost_2025", "2025", "275", "2025 fin kosten 275 vs 275; tick1438; primary official NBB WVV 65/66B"),
    ("bud_rlwh_pnl_2025", "2025", "123056", "2025 PnL 123056 vs 69552; tick1438; primary official NBB WVV 9904"),
    ("bud_rlwh_pnl_2024", "2024", "69552", "2024 PnL 69552 comparative; tick1438; primary official NBB WVV 9904"),
    ("bud_rlwh_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1438; primary official NBB WVV"),
    ("bud_rlwh_capex_2025", "2025", "120377", "2025 MVA aanschaffingen 120377; FVA aanschaf empty; tick1438; primary official NBB WVV 8169"),
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
    f"comm_rlwh_jr2025_bruto,Regionaal Landschap Westhoek VZW JR2025 leftover IGS dual (brutomarge 1.46m / pers 1.28m / cash 1.24m),{ENT},RL Westhoek VZW / 17 Westhoek cities,WVV VZW; NBB neerlegging; 17 Westhoek gemeenten + provincie West-Vlaanderen,2026-05-07,1999,,1462915,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00109364.pdf,Local leftover IGS map VL Westhoek landschap — 1.46m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 1.28m,Publish empty 70/73/60-61 split + pers 1.28m + trade JUMP + deferred JUMP + vennoten share-pct; do not keep leftover RLWH VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>West-Vlaanderen>Westhoek>RLWH>JR2025_L5,tick1438; assets 1737911 omzet empty diensten empty pers 1282901 pnl 123056 equity 785330 cash 1237464 debt 694016 capex 120377 dividend 0 brutomarge 1462915; FOI ready not sent; not TE-additive of 348bn; NOT DVV Westhoek",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlwh_omzet_empty_pers_1_28m_cash_1_24m,Regionaal Landschap Westhoek VZW JR2025 leftover IGS: empty omzet 70 / pers 1.28m / cash 1.24m / brutomarge 1.46m,L5,local_budget_line,Vlaanderen>West-Vlaanderen>Westhoek>RLWH>JR2025_L5,1462915,1737911,Leftover dual IGS VZW: assets 1.74m / equity 0.79m / pnl 0.12m / omzet empty / 73 empty / 60-61 empty / pers 1.28m 18 VTE / cash 1.24m / debt 0.69m / lev 0.09m / dividend 0,strong,{SRC},RL Westhoek VZW / 17 Westhoek cities,Local leftover IGS map VL Westhoek landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 1.46m / pers 1.28m / cash 1.24m / PnL 0.12m,6.6,6.5,2.2,6.2,Publish empty 70/73/60-61 split + pers 1.28m + trade JUMP + deferred JUMP + vennoten share-pct; do not keep leftover RLWH VZW as dual unpublished vehicle,active,,tick1438; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined DVV Westhoek 1415 / CO7 1420 / Viertoren 1421 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>West-Vlaanderen>Westhoek>RLWH>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 1462915 + pers 62 1282901 / 18 VTE + cash 1237464 vs 1151609 + trade JUMP 202195 vs 66607 + other recv 122537 + leveranciers DROP 89494 vs 128917 + deferred JUMP 400109 vs 262357 + voorzieningen pensions 258565 + vennoten share-pct unpublished + commissaris unpublished + 2 VE unpublished + relation to DVV Westhoek unpublished,Leftover RLWH VZW after leftover AGB hunt: 1.46m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Westhoek vzw / Bestuursorgaan,info@rlwesthoek.be,Iepersteenweg 56 8600 Diksmuide,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlwh_jr2025_bruto,lb_rlwh_omzet_empty_pers_1_28m_cash_1_24m,{TS},{TS},tick1438 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (63056 bytes 19p deposit 2026-00109364). FOI ready not sent. NOT DVV Westhoek. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Noord-Hageland JR2025 CDN 2026-00112448 live leftover for next.",
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
if not last_s.startswith("rq_1438,"):
    raise SystemExit(f"expected last row rq_1438, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1438 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1438,RL Westhoek JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlwh,"
    "Completed: Regionaal Landschap Westhoek VZW leftover IGS / regionaal landschap of 17 mined Westhoek cities after leftover AGB hunt; KBO 0469.129.810 Actief; live JR2025 official NBB WVV VKT-VZW PDF (63056 bytes 19p deposit 2026-00109364; AV 07.05.2026; created 12.05.2026; neerlegging 2026-05-13; no commissaris listed); sourced euros assets 1737911 omzet empty diensten empty pers 1282901 pnl 123056 equity 785330 cash 1237464 debt 694016 capex 120377 dividend 0 brutomarge 1462915; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash 1.24m / trade JUMP / deferred JUMP; NOT DVV Westhoek,"
    f"{GAP},2026-08-19T12:00:00Z,{TS},"
    "tick1438 RL Westhoek VZW leftover IGS residual; KBO 0469.129.810; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1439 residual dual L5 VL"
)
spawn = (
    "rq_1439,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1438 done including RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Noord-Hageland 0462.581.716 JR2025 CDN 2026-00112448 LIVE leftover — STRONG next leftover RL; leftover RL Dijleland 0461.935.675 JR2025 CDN 2026-00122942 live leftover; leftover RL de Voorkempen 0898.729.546 JR2025 CDN 2026-00054608 live leftover; leftover RL Brabantse Kouters VZW 0874.904.564 JR2025 CDN 2026-00321333 live leftover (NOT Erfgoed Brabantse Kouters IOED 1428); leftover RL Meetjesland & Leievallei 0466.277.515 JR2025 CDN 2026-00092026 live leftover; leftover RL Haspengouw & Voeren 0471.371.597 JR2025 CDN 2026-00070056 live leftover; leftover RL Kleine & Grote Nete 0810.764.897 JR2025 CDN 2026-00054598 live leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (2026pdf 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1438 after RL Westhoek leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Noord-Hageland if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1438=done + rq_1439 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1438 RL Westhoek leftover IGS residual; KBO 0469.129.810; live JR2025 NBB WVV PDF; sourced euros assets 1737911 omzet empty diensten empty pers 1282901 pnl 123056 equity 785330 cash 1237464 debt 694016 capex 120377 dividend 0 brutomarge 1462915; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash 1.24m / trade JUMP / deferred JUMP; NOT DVV Westhoek; next rq_1439 residual dual L5 VL leftover RL Noord-Hageland if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1438,1438,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1438")

# --- loop_log ---
entry = (
    "\n## Tick 1438 - 2026-08-19 - rq_1438 RL Westhoek dual residual leftover\n"
    "- Unit: Regionaal Landschap Westhoek VZW / RLW (leftover IGS / regionaal landschap of 17 mined Westhoek cities; 2 VE) after residual dual hunt (KBO **0469.129.810**; official rlwesthoek.be; live NBB WVV VKT-VZW deposit **2026-00109364** PDF 63056 bytes / 19p; AV **07.05.2026**; created **12.05.2026**; pdfinfo **12.05.2026**; neerlegging **2026-05-13**; model **VKT-VZW** 23.0.9 m04-f; no commissaris listed; VKT-VZW 6.1.1/6.1.3/6.2/6.3/6.5/6.6/7/8 not filed; 6.1.2 MVA + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022 (SBM last 2023-00125347); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Vauban Ieper / AGB Musea Ieper / AGB De Kouter Poperinge / AGB Veurne / AGB Koksijde / AGB De Panne / AGB Nieuwpoort / AGB MMP1917 Zonnebeke) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (2026pdf 2026-00043131 is JR2024 AV 11.03.2025 year 2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381). Leftover IGS Regionaal Landschap Westhoek VZW statutory CDN live this tick (HTTP 200 / application/pdf / 63056 / 19p; SBM jaar **2025-12-31**; neerlegging 2026-05-13) — taken (hunt order #2 leftover unmined RL VZW of mined Westhoek cities with full WVV balans; leftover RL Westhoek named after Houtland still unpublished). Distinct from already-mined **DVV Westhoek** (igs_westhoek_dv tick 1415; NOT this entity) / CO7 1420 / Viertoren 1421 / IVVO / Aquaduin / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Westhoek / 0469.129.810 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **11.06.1999**; statutaire naam REGIONAAL LANDSCHAP WESTHOEK since 05.12.2017; afkorting RLW since 01.07.2023; VZW since 11.06.1999; zetel Iepersteenweg(W) 56 8600 Diksmuide since 05.12.2017; **2 VE**; KBO no tel/e-mail/web; official site https://www.rlwesthoek.be/; e-mail info@rlwesthoek.be; tel 0489 86 66 83; algemeen coordinator Niels Dabaut; NACE RSZ/btw 91.420; Werkgever RSZ since 15.06.2001; btw since 01.11.2022; aanbestedende overheid since 11.06.1999. WVV 2.1 voorzitter Jurgen Vanlerberghe. Official site 17 leden-gemeenten: Alveringem / De Panne / Diksmuide / Heuvelland / Houthulst / Ieper / Koekelare / Koksijde / Kortemark / Langemark-Poelkapelle / Lo-Reninge / Mesen / Nieuwpoort / Poperinge / Veurne / Vleteren / Zonnebeke. Plus provincie West-Vlaanderen. Named share-% unpublished. Contact info@rlwesthoek.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (SBM table assets 1737911 matches PDF 1737911 — PDF wins). Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **1282901** / **18 VTE**): assets **1737911** (was 1477379); fixed **168736** / IVA empty / MVA **168736** (machines **2904**; meubilair **154235**; overige **11596**; aanschaf YE **262049** / afschr YE **93313**; aanschaffingen **120377**; overdrachten **19543**) / FVA empty; current **1569175**; voorraden **1536**; ST recv **324732** (trade **202195 JUMP** vs 66607 / other **122537** vs 148162); cash **1237464** vs 1151609; prepaid **5443**; equity **785330** (bestemde fondsen **347692**; overgedragen **437638**); voorzieningen **258565** (all pensions); schulden **694016** (LT empty; ST **293907** waarvan leveranciers **89494 DROP** vs 128917 + tax **35778** + soc/bezold **168634**; deferred **400109 JUMP** vs 262357); brutomarge **1462915** vs 1172208; omzet empty; 73 empty; 60/61 empty; pers **1282901** / **18 VTE** / 26204 uur / YE **18,1**; afschr **57180**; andere **307**; expl **122527** vs 69826; fin opbr **804**; fin kosten **275**; tax empty; PnL **123056** vs 69552; dividend **0**; over te dragen **437638**; capex **120377**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlwh` parent `sec_flanders`; budgets +47 executed; commitments +1 envelope 1462915 AV 07.05.2026; leaderboard +1 annual 1462915 / total 1737911; foi_queue +1 status=ready never sent; research_queue surgical rq_1438=done + rq_1439 spawn; loop_state ticks_completed=1438.\n"
    "- FOI: `gap_rlwh_omzet_empty_pers_1_28m_cash_1_24m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 1.28m 18 VTE deelwerking unpublished / trade JUMP 0.20m / deferred JUMP 0.40m / cash 1.24m / pensions 0.26m / vennoten share-pct / relation to DVV Westhoek unpublished / commissaris unpublished / 2 VE unpublished.\n"
    "- Next: rq_1439 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Noord-Hageland **0462.581.716** JR2025 CDN **2026-00112448** LIVE — STRONG next leftover RL. Leftover RL Dijleland 0461.935.675 CDN 2026-00122942 live. Leftover RL de Voorkempen 0898.729.546 CDN 2026-00054608 live. Leftover RL Brabantse Kouters VZW 0874.904.564 CDN 2026-00321333 live (NOT Erfgoed Brabantse Kouters IOED 1428). Leftover RL Meetjesland 0466.277.515 CDN 2026-00092026 live. Leftover RL Haspengouw 0471.371.597 CDN 2026-00070056 live. Leftover RL Kleine & Grote Nete 0810.764.897 CDN 2026-00054598 live. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024; SOLVA already mined; Pajottegem city already mined).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1438")
print("tick1438 writes done")
