#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1435 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:20:00Z"
ENT = "vzw_rlrl"
SRC = "src_rlrl_jr2025_nbb"
GAP = "gap_rlrl_omzet_empty_pers_1_28m_cash_1_19m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlrl_jr2025_nbb,Regionaal Landschap Rivierenland VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00071020.pdf,NBB / RL Rivierenland VZW,2026-08-19,budget,tick1435; VKT-VZW 23.0.6 m04-f PDF 17p / 55888 bytes deposit 2026-00071020; AV 04.03.2026; created 02.04.2026; neerlegging 2026-04-02; KBO 0899.152.980; assets 1619526 cash 1194116 debt 1039953 brutomarge 1223912 omzet empty code73 empty code60_61 empty pers 1279237 pnl -55419; no commissaris named",
    "src_rlrl_site,Regionaal Landschap Rivierenland official site,https://www.rlrl.be/,RL Rivierenland VZW,2026-08-19,official_register,tick1435; leftover IGS / regionaal landschap of 23 Rivierenland cities + Wilrijk; zetel Hallestraat 6 2800 Mechelen; kantoor Van Benedenlaan 12; contact info@rlrl.be; tel 015 21 98 53; dagelijks bestuur Jelle Claes",
    "src_kbo_rlrl_0899152980,KBO Regionaal Landschap Rivierenland 0899.152.980,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0899152980,KBO Public Search FOD Economie,2026-08-19,official_register,tick1435; Actief since 03.07.2008; naam since 03.07.2008; afkorting RLRL vzw since 23.02.2015; zetel Hallestraat 6 2800 Mechelen since 23.02.2015; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 01.11.2008",
    "src_rlrl_foi_contact,RL Rivierenland FOI channel (info@rlrl.be; Hallestraat 6 Mechelen),https://www.rlrl.be/contact,RL Rivierenland VZW,2026-08-19,official_register,tick1435; 23 member cities + Wilrijk + provincie Antwerpen; voorzitter Jan De Haes; ondervoorzitter Bert Delanoeije; NOT Zorgbedrijf Rivierenland 0680.439.360",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlrl," in raw or raw.startswith(b"vzw_rlrl,"):
    raise SystemExit("vzw_rlrl already present")
if b"0899.152.980" in raw or b"0899152980" in raw:
    raise SystemExit("RL Rivierenland KBO already present")
row = (
    "vzw_rlrl,Regionaal Landschap Rivierenland VZW (leftover IGS / regionaal landschap of 23 mined Rivierenland cities + Wilrijk),"
    "Regionaal Landschap Rivierenland ASBL (IGS residuel / paysage regional Rivierenland),"
    "Regionaal Landschap Rivierenland leftover IGS / regional landscape VZW of 23 Rivierenland municipalities + Wilrijk,"
    "other,sec_flanders,nl,https://www.rlrl.be/,info@rlrl.be,Hallestraat 6 2800 Mechelen,"
    "tick1435 leftover residual IGS VZW of mined Rivierenland cities after leftover AGB hunt; KBO 0899.152.980 Actief since 03.07.2008; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 1619526 omzet empty diensten empty pers 1279237 pnl -55419 equity 579573 cash 1194116 debt 1039953 capex 3802 dividend 0 brutomarge 1223912; FOI ready omzet empty / 73 empty / 60-61 empty / pers 1.28m / cash 1.19m / lev jump / geldbeleg liquidated; distinct from already-mined Zorgbedrijf Rivierenland 0680.439.360 / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / IGEMO / De Nekker"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlrl")

# --- budgets ---
BUDGETS = [
    ("bud_rlrl_assets_2025", "2025", "1619526", "2025 assets 1619526 VKT-VZW 20/58; tick1435; primary official NBB WVV"),
    ("bud_rlrl_assets_2024", "2024", "2034478", "2024 assets 2034478 comparative; tick1435; primary official NBB WVV 20/58"),
    ("bud_rlrl_fixed_2025", "2025", "8968", "2025 vaste activa 8968 vs 12679; tick1435; primary official NBB WVV 21/28"),
    ("bud_rlrl_iva_2025", "2025", "0", "2025 IVA empty; tick1435; primary official NBB WVV 21"),
    ("bud_rlrl_mva_2025", "2025", "8218", "2025 MVA 8218 vs 11929; tick1435; primary official NBB WVV 22/27"),
    ("bud_rlrl_meubilair_2025", "2025", "7742", "2025 meubilair/rollend 7742 vs 11295; tick1435; primary official NBB WVV 24"),
    ("bud_rlrl_overigemva_2025", "2025", "476", "2025 overige MVA 476 vs 634; tick1435; primary official NBB WVV 26"),
    ("bud_rlrl_fva_2025", "2025", "750", "2025 FVA 750 unchanged; tick1435; primary official NBB WVV 28"),
    ("bud_rlrl_current_2025", "2025", "1610559", "2025 vlottend 1610559 vs 2021799; tick1435; primary official NBB WVV 29/58"),
    ("bud_rlrl_voorraden_2025", "2025", "6008", "2025 voorraden 6008 vs 6981; tick1435; primary official NBB WVV 30/36"),
    ("bud_rlrl_strecv_2025", "2025", "394155", "2025 ST vorderingen 394155 vs 344194; tick1435; primary official NBB WVV 40/41"),
    ("bud_rlrl_trade_2025", "2025", "218986", "2025 handelsvorderingen 218986 vs 185124; tick1435; primary official NBB WVV 40"),
    ("bud_rlrl_othrecv_2025", "2025", "175169", "2025 overige vorderingen 175169 vs 159070; tick1435; primary official NBB WVV 41"),
    ("bud_rlrl_othrecv_2024", "2024", "159070", "2024 overige vorderingen 159070 comparative; tick1435; primary official NBB WVV 41"),
    ("bud_rlrl_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty after 769470; tick1435; primary official NBB WVV 50/53"),
    ("bud_rlrl_geldbeleg_2024", "2024", "769470", "2024 geldbeleggingen 769470 comparative; tick1435; primary official NBB WVV 50/53"),
    ("bud_rlrl_cash_2025", "2025", "1194116", "2025 liquide middelen 1194116 JUMP vs 849263; tick1435; primary official NBB WVV 54/58"),
    ("bud_rlrl_cash_2024", "2024", "849263", "2024 liquide middelen 849263 comparative; tick1435; primary official NBB WVV 54/58"),
    ("bud_rlrl_prepaid_2025", "2025", "16280", "2025 prepaid 16280 vs 51891; tick1435; primary official NBB WVV 490/1"),
    ("bud_rlrl_equity_2025", "2025", "579573", "2025 EV 579573 vs 634992; tick1435; primary official NBB WVV 10/15"),
    ("bud_rlrl_equity_2024", "2024", "634992", "2024 EV 634992 comparative; tick1435; primary official NBB WVV 10/15"),
    ("bud_rlrl_bestemde_2025", "2025", "235000", "2025 bestemde fondsen 235000 unchanged; tick1435; primary official NBB WVV 13"),
    ("bud_rlrl_overgedragen_2025", "2025", "344573", "2025 overgedragen winst 344573 vs 399992; tick1435; primary official NBB WVV 14"),
    ("bud_rlrl_debt_2025", "2025", "1039953", "2025 schulden 1039953 vs 1399486 (LT empty); tick1435; primary official NBB WVV 17/49"),
    ("bud_rlrl_debt_2024", "2024", "1399486", "2024 schulden 1399486 comparative; tick1435; primary official NBB WVV 17/49"),
    ("bud_rlrl_stdebt_2025", "2025", "388695", "2025 ST schulden 388695 vs 280344; tick1435; primary official NBB WVV 42/48"),
    ("bud_rlrl_lev_2025", "2025", "251756", "2025 leveranciers 251756 JUMP vs 141044; tick1435; primary official NBB WVV 440/4"),
    ("bud_rlrl_lev_2024", "2024", "141044", "2024 leveranciers 141044 comparative; tick1435; primary official NBB WVV 440/4"),
    ("bud_rlrl_taxsoc_2025", "2025", "136939", "2025 tax/soc 136939 all bezoldigingen vs 115088; tick1435; primary official NBB WVV 45"),
    ("bud_rlrl_bezold_2025", "2025", "136939", "2025 bezoldigingen/sociale lasten 136939 vs 115088; tick1435; primary official NBB WVV 454/9"),
    ("bud_rlrl_othdebt_2025", "2025", "0", "2025 overige schulden empty vs 24212; tick1435; primary official NBB WVV 48"),
    ("bud_rlrl_othdebt_2024", "2024", "24212", "2024 overige schulden 24212 comparative; tick1435; primary official NBB WVV 48"),
    ("bud_rlrl_deferred_2025", "2025", "651259", "2025 overlopend passief 651259 DROP vs 1119142; tick1435; primary official NBB WVV 492/3"),
    ("bud_rlrl_deferred_2024", "2024", "1119142", "2024 overlopend passief 1119142 comparative; tick1435; primary official NBB WVV 492/3"),
    ("bud_rlrl_brutomarge_2025", "2025", "1223912", "2025 brutomarge 1223912 vs 1186470; omzet 70 empty; 73 empty; 60/61 empty; tick1435; primary official NBB WVV 9900"),
    ("bud_rlrl_brutomarge_2024", "2024", "1186470", "2024 brutomarge 1186470 comparative; tick1435; primary official NBB WVV 9900"),
    ("bud_rlrl_pers_2025", "2025", "1279237", "2025 pers 1279237 / 16.7 VTE vs 1123170 / 15.4; tick1435; primary official NBB WVV 62"),
    ("bud_rlrl_pers_2024", "2024", "1123170", "2024 pers 1123170 / 15.4 VTE comparative; tick1435; primary official NBB WVV 62"),
    ("bud_rlrl_afschr_2025", "2025", "7514", "2025 afschrijvingen 7514 vs 10030; tick1435; primary official NBB WVV 630"),
    ("bud_rlrl_expl_2025", "2025", "-62838", "2025 expl -62838 vs 53270; tick1435; primary official NBB WVV 9901"),
    ("bud_rlrl_expl_2024", "2024", "53270", "2024 expl 53270 comparative; tick1435; primary official NBB WVV 9901"),
    ("bud_rlrl_finopbr_2025", "2025", "8345", "2025 fin opbr 8345 vs 568; tick1435; primary official NBB WVV 75/76B"),
    ("bud_rlrl_finkost_2025", "2025", "926", "2025 fin kosten 926 vs 514; tick1435; primary official NBB WVV 65/66B"),
    ("bud_rlrl_pnl_2025", "2025", "-55419", "2025 PnL -55419 vs 53323; tick1435; primary official NBB WVV 9904"),
    ("bud_rlrl_pnl_2024", "2024", "53323", "2024 PnL 53323 comparative; tick1435; primary official NBB WVV 9904"),
    ("bud_rlrl_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1435; primary official NBB WVV"),
    ("bud_rlrl_capex_2025", "2025", "3802", "2025 MVA aanschaffingen 3802; FVA aanschaf empty; tick1435; primary official NBB WVV 8169"),
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
    f"comm_rlrl_jr2025_bruto,Regionaal Landschap Rivierenland VZW JR2025 leftover IGS dual (brutomarge 1.22m / pers 1.28m / cash 1.19m),{ENT},RL Rivierenland VZW / 23 Rivierenland cities + Wilrijk,WVV VZW; NBB neerlegging; 23 Rivierenland gemeenten + Wilrijk + provincie Antwerpen,2026-03-04,2008,,1223912,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00071020.pdf,Local leftover IGS map VL Rivierenland landschap — 1.22m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 1.28m,Publish empty 70/73/60-61 split + pers 1.28m + cash jump + geldbeleg liquidated + lev jump + vennoten share-pct; do not keep leftover RLRL VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Antwerpen>Rivierenland>RLRL>JR2025_L5,tick1435; assets 1619526 omzet empty diensten empty pers 1279237 pnl -55419 equity 579573 cash 1194116 debt 1039953 capex 3802 dividend 0 brutomarge 1223912; FOI ready not sent; not TE-additive of 348bn; NOT Zorgbedrijf Rivierenland",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlrl_omzet_empty_pers_1_28m_cash_1_19m,Regionaal Landschap Rivierenland VZW JR2025 leftover IGS: empty omzet 70 / pers 1.28m / cash 1.19m / brutomarge 1.22m,L5,local_budget_line,Vlaanderen>Antwerpen>Rivierenland>RLRL>JR2025_L5,1223912,1619526,Leftover dual IGS VZW: assets 1.62m / equity 0.58m / pnl -0.06m / omzet empty / 73 empty / 60-61 empty / pers 1.28m 16.7 VTE / cash 1.19m JUMP / geldbeleg 0.77m liquidated / debt 1.04m / lev 0.25m JUMP / dividend 0,strong,{SRC},RL Rivierenland VZW / 23 Rivierenland cities + Wilrijk,Local leftover IGS map VL Rivierenland landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 1.22m / pers 1.28m / cash 1.19m / PnL -0.06m,6.6,6.6,2.2,6.2,Publish empty 70/73/60-61 split + pers 1.28m + cash jump + geldbeleg liquidated + lev jump + vennoten share-pct; do not keep leftover RLRL VZW as dual unpublished vehicle,active,,tick1435; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Zorgbedrijf Rivierenland / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Antwerpen>Rivierenland>RLRL>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 1223912 + pers 62 1279237 / 16.7 VTE + cash JUMP 1194116 vs 849263 + geldbeleg DROP 769470 to 0 + other recv 175169 + leveranciers JUMP 251756 vs 141044 + deferred DROP 651259 vs 1119142 + vennoten share-pct unpublished + commissaris unpublished + relation to Zorgbedrijf Rivierenland unpublished,Leftover RLRL VZW after leftover AGB hunt: 1.22m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Rivierenland vzw / Bestuursorgaan,info@rlrl.be,Hallestraat 6 2800 Mechelen,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlrl_jr2025_bruto,lb_rlrl_omzet_empty_pers_1_28m_cash_1_19m,{TS},{TS},tick1435 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (55888 bytes 17p deposit 2026-00071020). FOI ready not sent. NOT Zorgbedrijf Rivierenland. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Pajottenland/Vlaamse Ardennen JR2025 CDN live leftover for next.",
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
if not last_s.startswith("rq_1435,"):
    raise SystemExit(f"expected last row rq_1435, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1435 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1435,RL Rivierenland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlrl,"
    "Completed: Regionaal Landschap Rivierenland VZW leftover IGS / regionaal landschap of 23 mined Rivierenland cities + Wilrijk after leftover AGB hunt; KBO 0899.152.980 Actief; live JR2025 official NBB WVV VKT-VZW PDF (55888 bytes 17p deposit 2026-00071020; AV 04.03.2026; created 02.04.2026; neerlegging 2026-04-02; no commissaris named); sourced euros assets 1619526 omzet empty diensten empty pers 1279237 pnl -55419 equity 579573 cash 1194116 debt 1039953 capex 3802 dividend 0 brutomarge 1223912; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash 1.19m / lev jump / geldbeleg liquidated; NOT Zorgbedrijf Rivierenland,"
    f"{GAP},2026-08-19T11:55:00Z,{TS},"
    "tick1435 RL Rivierenland VZW leftover IGS residual; KBO 0899.152.980; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1436 residual dual L5 VL"
)
spawn = (
    "rq_1436,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1435 done including RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Pajottenland en Zennevallei 0458.521.374 JR2025 CDN 2026-00101632 LIVE leftover — STRONG next leftover RL; leftover RL Vlaamse Ardennen tot Dender 0449.013.097 JR2025 CDN 2026-00367158 LIVE leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1435 after RL Rivierenland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Pajottenland/Vlaamse Ardennen if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1435=done + rq_1436 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1435 RL Rivierenland leftover IGS residual; KBO 0899.152.980; live JR2025 NBB WVV PDF; sourced euros assets 1619526 omzet empty diensten empty pers 1279237 pnl -55419 equity 579573 cash 1194116 debt 1039953 capex 3802 dividend 0 brutomarge 1223912; FOI ready empty 70 / empty 73 / empty 60-61 / pers 1.28m / cash 1.19m / lev jump / geldbeleg liquidated; NOT Zorgbedrijf Rivierenland; next rq_1436 residual dual L5 VL leftover RL Pajottenland/Vlaamse Ardennen if 2025 CDN now live; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1435,1435,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1435")

# --- loop_log ---
entry = (
    "\n## Tick 1435 - 2026-08-19 - rq_1435 RL Rivierenland dual residual leftover\n"
    "- Unit: Regionaal Landschap Rivierenland VZW / RLRL (leftover IGS / regionaal landschap of 23 mined Rivierenland cities + Wilrijk; 1 VE) after residual dual hunt (KBO **0899.152.980**; official rlrl.be; live NBB WVV VKT-VZW deposit **2026-00071020** PDF 55888 bytes / 17p; AV **04.03.2026**; created **02.04.2026**; neerlegging **2026-04-02**; model **VKT-VZW** 23.0.6 m04-f; no commissaris named; VKT-VZW 6.1.1/6.2/6.3/6.5/6.6/7/8 not filed; 6.1.2 MVA + 6.1.3 FVA + 6.4 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM 2025pdf 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022 (SBM last 2023-00125347); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Mortsel / AGB Duffel / AGB Heist-op-den-Berg / De Nekker) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381). Leftover IGS Regionaal Landschap Rivierenland VZW statutory CDN live this tick (HTTP 200 / application/pdf / 55888 / 17p; SBM jaar **2025-12-31**; neerlegging 2026-04-02) — taken (hunt order #2 leftover unmined RL VZW of mined Rivierenland cities with full WVV balans; STRONG next leftover RL after RLZH 1434). Distinct from already-mined **Zorgbedrijf Rivierenland** (KBO 0680.439.360; NOT this entity) / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / IGEMO / De Nekker. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Rivierenland / 0899.152.980 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **03.07.2008**; statutaire naam Regionaal Landschap Rivierenland since 03.07.2008; afkorting RLRL vzw since 23.02.2015; VZW since 03.07.2008; zetel Hallestraat 6 2800 Mechelen since 23.02.2015; **1 VE**; e-mail info@rlrl.be since 04.03.2026; web www.rlrl.be since 04.03.2026; official kantoor Van Benedenlaan 12 2800 Mechelen; tel 015 21 98 53; dagelijks bestuur Claes Jelle since 22.02.2022; NACE RSZ 91.420; Werkgever RSZ since 01.11.2008; aanbestedende overheid since 03.07.2008. WVV 2.1 voorzitter Jan De Haes (since 20.02.2019); ondervoorzitter Bert Delanoeije. Official site 23 leden-gemeenten + Wilrijk: Aartselaar / Berlaar / Boechout / Boom / Bonheiden / Borsbeek / Duffel / Hemiksem / Edegem / Heist-op-den-Berg / Hove / Kontich / Lier / Lint / Mechelen / Mortsel / Niel / Nijlen / Putte / Rumst / Schelle / Sint-Katelijne-Waver / Willebroek + Wilrijk. Plus provincie Antwerpen + Vlaamse Overheid. Named share-% unpublished. Contact info@rlrl.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (SBM table assets 1619527 vs PDF 1619526 — PDF wins). Not every-10 (next 1440).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **1279237** / **16,7 VTE**): assets **1619526** (was 2034478); fixed **8968** / IVA empty / MVA **8218** (meubilair **7742**; overige **476**) / FVA **750**; current **1610559**; voorraden **6008**; ST recv **394155** (trade **218986** / other **175169**); geldbeleggingen empty (was **769470**); cash **1194116 JUMP** vs 849263; prepaid **16280**; equity **579573** (bestemde fondsen **235000**; overgedragen **344573**); voorzieningen empty; schulden **1039953** (LT empty; ST **388695** waarvan leveranciers **251756 JUMP** vs 141044 + soc/bezold **136939**; deferred **651259 DROP** vs 1119142); brutomarge **1223912** vs 1186470; omzet empty; 73 empty; 60/61 empty; pers **1279237** / **16,7 VTE** / 25527 uur / YE **17**; afschr **7514**; andere bedrijfskosten empty; expl **−62838** vs +53270; fin opbr **8345**; fin kosten **926**; tax empty; PnL **−55419** vs +53323; dividend **0**; over te dragen **344573**; capex **3802**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlrl` parent `sec_flanders`; budgets +47 executed; commitments +1 envelope 1223912 AV 04.03.2026; leaderboard +1 annual 1223912 / total 1619526; foi_queue +1 status=ready never sent; research_queue surgical rq_1435=done + rq_1436 spawn; loop_state ticks_completed=1435.\n"
    "- FOI: `gap_rlrl_omzet_empty_pers_1_28m_cash_1_19m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 1.28m 16.7 VTE deelwerking unpublished / cash JUMP 1.19m / geldbeleg 0.77m liquidated / leveranciers JUMP 0.25m / deferred DROP 0.65m / vennoten share-pct / relation to Zorgbedrijf Rivierenland unpublished / commissaris unpublished.\n"
    "- Next: rq_1436 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Pajottenland en Zennevallei **0458.521.374** JR2025 CDN **2026-00101632** LIVE — STRONG next leftover RL. Leftover RL Vlaamse Ardennen tot Dender **0449.013.097** JR2025 CDN **2026-00367158** LIVE leftover. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024; Zorgbedrijf Rivierenland already mined).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1435")
print("tick1435 writes done")
