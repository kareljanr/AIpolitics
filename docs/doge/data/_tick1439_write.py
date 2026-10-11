#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1439 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:25:00Z"
ENT = "vzw_rlnh"
SRC = "src_rlnh_jr2025_nbb"
GAP = "gap_rlnh_omzet_empty_pers_0_63m_cash_0_53m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlnh_jr2025_nbb,Regionaal Landschap Noord-Hageland VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00112448.pdf,NBB / RL Noord-Hageland VZW,2026-08-19,budget,tick1439; VKT-VZW 25.0.12 m04-f PDF 15p / 53095 bytes deposit 2026-00112448; AV 25.03.2026; header 13.05.2026; pdfinfo 18.05.2026; neerlegging 2026-05-18; KBO 0462.581.716; assets 837562 cash 527323 debt 267624 brutomarge 626331 omzet empty code73 empty code60_61 empty pers 630059 pnl -101; no commissaris listed",
    "src_rlnh_site,Regionaal Landschap Noord-Hageland official site,https://www.rlnh.be/,RL Noord-Hageland VZW,2026-08-19,official_register,tick1439; leftover IGS / regionaal landschap of 11 Noord-Hageland cities; zetel Oudepastoriestraat 22 3390 Tielt-Winge; contact info@rlnh.be; tel +32 (0)16 63 59 54; coordinator Wim Boonen; voorzitter Delaure Julien",
    "src_kbo_rlnh_0462581716,KBO Regionaal Landschap Noord-Hageland 0462.581.716,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0462581716,KBO Public Search FOD Economie,2026-08-19,official_register,tick1439; Actief since 19.12.1997; naam since 19.12.1997; afkorting RLNH since 19.12.1997; zetel Oudepastoriestraat 22 3390 Tielt-Winge since 01.01.2015; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 06.01.1998; aanbestedende overheid since 19.12.1997",
    "src_rlnh_foi_contact,RL Noord-Hageland FOI channel (info@rlnh.be; Oudepastoriestraat 22 Tielt-Winge),https://www.rlnh.be/contact,RL Noord-Hageland VZW,2026-08-19,official_register,tick1439; 11 member cities + provincie Vlaams-Brabant; voorzitter Delaure Julien; coordinator Wim Boonen; NOT IGO Holsbeek",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlnh," in raw or raw.startswith(b"vzw_rlnh,"):
    raise SystemExit("vzw_rlnh already present")
if b"0462.581.716" in raw or b"0462581716" in raw:
    raise SystemExit("RL Noord-Hageland KBO already present")
row = (
    "vzw_rlnh,Regionaal Landschap Noord-Hageland VZW (leftover IGS / regionaal landschap of 11 mined Noord-Hageland cities; NOT IGO Holsbeek),"
    "Regionaal Landschap Noord-Hageland ASBL (IGS residuel / paysage regional Noord-Hageland),"
    "Regionaal Landschap Noord-Hageland leftover IGS / regional landscape VZW of 11 Noord-Hageland municipalities (not IGO Holsbeek),"
    "other,sec_flanders,nl,https://www.rlnh.be/,info@rlnh.be,Oudepastoriestraat 22 3390 Tielt-Winge,"
    "tick1439 leftover residual IGS VZW of mined Noord-Hageland cities after leftover AGB hunt; KBO 0462.581.716 Actief since 19.12.1997; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 837562 omzet empty diensten empty pers 630059 pnl -101 equity 569938 cash 527323 debt 267624 capex 0 dividend 0 brutomarge 626331; FOI ready omzet empty / 73 empty / 60-61 empty / pers 0.63m / cash 0.53m / other recv JUMP / geldbeleg liquidated; distinct from already-mined IGO Holsbeek 1409 / Hofheide 1395 / EcoWerf 1357 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlnh")

# --- budgets ---
BUDGETS = [
    ("bud_rlnh_assets_2025", "2025", "837562", "2025 assets 837562 VKT-VZW 20/58; tick1439; primary official NBB WVV"),
    ("bud_rlnh_assets_2024", "2024", "834115", "2024 assets 834115 comparative; tick1439; primary official NBB WVV 20/58"),
    ("bud_rlnh_fixed_2025", "2025", "250", "2025 vaste activa 250 vs 250; tick1439; primary official NBB WVV 21/28"),
    ("bud_rlnh_iva_2025", "2025", "0", "2025 IVA empty (aanschaf YE 26950 / afschr YE 26950); tick1439; primary official NBB WVV 21"),
    ("bud_rlnh_mva_2025", "2025", "0", "2025 MVA empty (aanschaf YE 57759 / afschr YE 57759); tick1439; primary official NBB WVV 22/27"),
    ("bud_rlnh_fva_2025", "2025", "250", "2025 FVA 250 vs 250; tick1439; primary official NBB WVV 28"),
    ("bud_rlnh_current_2025", "2025", "837312", "2025 vlottend 837312 vs 833865; tick1439; primary official NBB WVV 29/58"),
    ("bud_rlnh_voorraden_2025", "2025", "2127", "2025 voorraden 2127 vs 2203; tick1439; primary official NBB WVV 30/36"),
    ("bud_rlnh_strecv_2025", "2025", "299512", "2025 ST vorderingen 299512 vs 171292; tick1439; primary official NBB WVV 40/41"),
    ("bud_rlnh_strecv_2024", "2024", "171292", "2024 ST vorderingen 171292 comparative; tick1439; primary official NBB WVV 40/41"),
    ("bud_rlnh_trade_2025", "2025", "134983", "2025 handelsvorderingen 134983 vs 123405; tick1439; primary official NBB WVV 40"),
    ("bud_rlnh_trade_2024", "2024", "123405", "2024 handelsvorderingen 123405 comparative; tick1439; primary official NBB WVV 40"),
    ("bud_rlnh_othrecv_2025", "2025", "164529", "2025 overige vorderingen 164529 JUMP vs 47888; tick1439; primary official NBB WVV 41"),
    ("bud_rlnh_othrecv_2024", "2024", "47888", "2024 overige vorderingen 47888 comparative; tick1439; primary official NBB WVV 41"),
    ("bud_rlnh_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen empty (was 220000); tick1439; primary official NBB WVV 50/53"),
    ("bud_rlnh_geldbeleg_2024", "2024", "220000", "2024 geldbeleggingen 220000 comparative; tick1439; primary official NBB WVV 50/53"),
    ("bud_rlnh_cash_2025", "2025", "527323", "2025 liquide middelen 527323 JUMP vs 430994; tick1439; primary official NBB WVV 54/58"),
    ("bud_rlnh_cash_2024", "2024", "430994", "2024 liquide middelen 430994 comparative; tick1439; primary official NBB WVV 54/58"),
    ("bud_rlnh_prepaid_2025", "2025", "8350", "2025 prepaid 8350 vs 9375; tick1439; primary official NBB WVV 490/1"),
    ("bud_rlnh_equity_2025", "2025", "569938", "2025 EV 569938 vs 570038; tick1439; primary official NBB WVV 10/15"),
    ("bud_rlnh_equity_2024", "2024", "570038", "2024 EV 570038 comparative; tick1439; primary official NBB WVV 10/15"),
    ("bud_rlnh_fondsen_2025", "2025", "145880", "2025 fondsen 145880 unchanged; tick1439; primary official NBB WVV 10"),
    ("bud_rlnh_bestemde_2025", "2025", "250687", "2025 bestemde fondsen 250687 unchanged; tick1439; primary official NBB WVV 13"),
    ("bud_rlnh_overgedragen_2025", "2025", "173371", "2025 overgedragen winst 173371 vs 173471; tick1439; primary official NBB WVV 14"),
    ("bud_rlnh_voorz_2025", "2025", "0", "2025 voorzieningen empty; tick1439; primary official NBB WVV 16"),
    ("bud_rlnh_debt_2025", "2025", "267624", "2025 schulden 267624 vs 264076 (LT empty); tick1439; primary official NBB WVV 17/49"),
    ("bud_rlnh_debt_2024", "2024", "264076", "2024 schulden 264076 comparative; tick1439; primary official NBB WVV 17/49"),
    ("bud_rlnh_stdebt_2025", "2025", "144676", "2025 ST schulden 144676 vs 156350; tick1439; primary official NBB WVV 42/48"),
    ("bud_rlnh_lev_2025", "2025", "81186", "2025 leveranciers 81186 DROP vs 91966; tick1439; primary official NBB WVV 440/4"),
    ("bud_rlnh_lev_2024", "2024", "91966", "2024 leveranciers 91966 comparative; tick1439; primary official NBB WVV 440/4"),
    ("bud_rlnh_bezold_2025", "2025", "63490", "2025 bezoldigingen/sociale lasten 63490 vs 64383; tick1439; primary official NBB WVV 454/9"),
    ("bud_rlnh_deferred_2025", "2025", "122949", "2025 overlopend passief 122949 vs 107727; tick1439; primary official NBB WVV 492/3"),
    ("bud_rlnh_deferred_2024", "2024", "107727", "2024 overlopend passief 107727 comparative; tick1439; primary official NBB WVV 492/3"),
    ("bud_rlnh_brutomarge_2025", "2025", "626331", "2025 brutomarge 626331 vs 579353; omzet 70 empty; 73 empty; 60/61 empty; tick1439; primary official NBB WVV 9900"),
    ("bud_rlnh_brutomarge_2024", "2024", "579353", "2024 brutomarge 579353 comparative; tick1439; primary official NBB WVV 9900"),
    ("bud_rlnh_pers_2025", "2025", "630059", "2025 pers 630059 / 8 VTE vs 555959 / 7; tick1439; primary official NBB WVV 62"),
    ("bud_rlnh_pers_2024", "2024", "555959", "2024 pers 555959 / 7 VTE comparative; tick1439; primary official NBB WVV 62"),
    ("bud_rlnh_andere_2025", "2025", "1757", "2025 andere bedrijfskosten 1757 vs 2926; tick1439; primary official NBB WVV 640/8"),
    ("bud_rlnh_expl_2025", "2025", "-5484", "2025 expl -5484 vs -6154; tick1439; primary official NBB WVV 9901"),
    ("bud_rlnh_expl_2024", "2024", "-6154", "2024 expl -6154 comparative; tick1439; primary official NBB WVV 9901"),
    ("bud_rlnh_finopbr_2025", "2025", "5926", "2025 fin opbr 5926 vs 6610; tick1439; primary official NBB WVV 75/76B"),
    ("bud_rlnh_finkost_2025", "2025", "542", "2025 fin kosten 542 vs 456; tick1439; primary official NBB WVV 65/66B"),
    ("bud_rlnh_pnl_2025", "2025", "-101", "2025 PnL -101 vs 0; tick1439; primary official NBB WVV 9904"),
    ("bud_rlnh_pnl_2024", "2024", "0", "2024 PnL 0 comparative; tick1439; primary official NBB WVV 9904"),
    ("bud_rlnh_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1439; primary official NBB WVV"),
    ("bud_rlnh_capex_2025", "2025", "0", "2025 MVA aanschaffingen empty; IVA aanschaf empty; FVA aanschaf empty; tick1439; primary official NBB WVV 8169"),
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
    f"comm_rlnh_jr2025_bruto,Regionaal Landschap Noord-Hageland VZW JR2025 leftover IGS dual (brutomarge 0.63m / pers 0.63m / cash 0.53m),{ENT},RL Noord-Hageland VZW / 11 Noord-Hageland cities,WVV VZW; NBB neerlegging; 11 Noord-Hageland gemeenten + provincie Vlaams-Brabant,2026-03-25,1997,,626331,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00112448.pdf,Local leftover IGS map VL Noord-Hageland landschap — 0.63m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 0.63m,Publish empty 70/73/60-61 split + pers 0.63m + other recv JUMP + geldbeleg liquidated + vennoten share-pct; do not keep leftover RLNH VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Vlaams-Brabant>Noord-Hageland>RLNH>JR2025_L5,tick1439; assets 837562 omzet empty diensten empty pers 630059 pnl -101 equity 569938 cash 527323 debt 267624 capex 0 dividend 0 brutomarge 626331; FOI ready not sent; not TE-additive of 348bn; NOT IGO Holsbeek",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlnh_omzet_empty_pers_0_63m_cash_0_53m,Regionaal Landschap Noord-Hageland VZW JR2025 leftover IGS: empty omzet 70 / pers 0.63m / cash 0.53m / brutomarge 0.63m,L5,local_budget_line,Vlaanderen>Vlaams-Brabant>Noord-Hageland>RLNH>JR2025_L5,626331,837562,Leftover dual IGS VZW: assets 0.84m / equity 0.57m / pnl -101 / omzet empty / 73 empty / 60-61 empty / pers 0.63m 8 VTE / cash 0.53m / debt 0.27m / lev 0.08m / dividend 0,strong,{SRC},RL Noord-Hageland VZW / 11 Noord-Hageland cities,Local leftover IGS map VL Noord-Hageland landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 0.63m / pers 0.63m / cash 0.53m / PnL -101,6.5,6.3,2.2,6.1,Publish empty 70/73/60-61 split + pers 0.63m + other recv JUMP + geldbeleg liquidated + vennoten share-pct; do not keep leftover RLNH VZW as dual unpublished vehicle,active,,tick1439; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined IGO Holsbeek 1409 / Hofheide 1395 / EcoWerf 1357 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Vlaams-Brabant>Noord-Hageland>RLNH>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 626331 + pers 62 630059 / 8 VTE + cash JUMP 527323 vs 430994 + other recv JUMP 164529 vs 47888 + geldbeleg DROP 220000 to 0 + leveranciers DROP 81186 vs 91966 + deferred 122949 vs 107727 + vennoten share-pct unpublished + commissaris unpublished + 1 VE unpublished + relation to IGO Holsbeek unpublished,Leftover RLNH VZW after leftover AGB hunt: 0.63m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Noord-Hageland vzw / Bestuursorgaan,info@rlnh.be,Oudepastoriestraat 22 3390 Tielt-Winge,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlnh_jr2025_bruto,lb_rlnh_omzet_empty_pers_0_63m_cash_0_53m,{TS},{TS},tick1439 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (53095 bytes 15p deposit 2026-00112448). FOI ready not sent. NOT IGO Holsbeek. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Dijleland JR2025 CDN 2026-00122942 live leftover for next.",
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
if not last_s.startswith("rq_1439,"):
    raise SystemExit(f"expected last row rq_1439, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1439 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1439,RL Noord-Hageland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlnh,"
    "Completed: Regionaal Landschap Noord-Hageland VZW leftover IGS / regionaal landschap of 11 mined Noord-Hageland cities after leftover AGB hunt; KBO 0462.581.716 Actief; live JR2025 official NBB WVV VKT-VZW PDF (53095 bytes 15p deposit 2026-00112448; AV 25.03.2026; header 13.05.2026; created 18.05.2026; neerlegging 2026-05-18; no commissaris listed); sourced euros assets 837562 omzet empty diensten empty pers 630059 pnl -101 equity 569938 cash 527323 debt 267624 capex 0 dividend 0 brutomarge 626331; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.63m / cash 0.53m / other recv JUMP / geldbeleg liquidated; NOT IGO Holsbeek,"
    f"{GAP},2026-08-19T12:00:00Z,{TS},"
    "tick1439 RL Noord-Hageland VZW leftover IGS residual; KBO 0462.581.716; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1440 residual dual L5 VL + every-10"
)
spawn = (
    "rq_1440,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "EVERY-10 plus residual dual L5 VL JR2025 hole-fill: MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md this tick; then next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1439 done including RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10 / Kusterfgoed 1429 leftover IGS/IOED live NBB WVV / Erfgoed Brabantse Kouters 1428 leftover IGS/IOED live NBB WVV / Erfgoed Denderland 1427 leftover IGS/IOED live NBB WVV / Erfgoed Noorderkempen 1426 leftover IGS live NBB WVV / Erfgoed Voorkempen 1425 leftover IGS live NBB WVV / Zuidwest 1424 leftover IGS live NBB WVV / BIONERGA LOGISTICS 1423 leftover daughter live NBB WVV / Vrijetijdsregio Druivenstreek 1422 leftover IGS live NBB WVV / Viertoren 1421 leftover IGS live NBB WVV / CO7 1420 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Dijleland 0461.935.675 JR2025 CDN 2026-00122942 LIVE leftover — STRONG next leftover RL; leftover RL de Voorkempen 0898.729.546 JR2025 CDN 2026-00054608 live leftover (NOT Erfgoed Voorkempen IOED 1425); leftover RL Brabantse Kouters VZW 0874.904.564 JR2025 CDN 2026-00321333 live leftover (NOT Erfgoed Brabantse Kouters IOED 1428 / KBO 0741.478.094); leftover RL Meetjesland & Leievallei 0466.277.515 JR2025 CDN 2026-00092026 live leftover (NOT Cultuuroverleg Meetjesland 1416); leftover RL Haspengouw & Voeren 0471.371.597 JR2025 CDN 2026-00070056 live leftover; leftover RL Kleine & Grote Nete 0810.764.897 JR2025 CDN 2026-00054598 live leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 (2026pdf 2026-00043131 is JR2024) — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1439 after RL Noord-Hageland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Dijleland if a 2025 CDN is now live; EVERY-10 progress refresh REQUIRED this tick"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1439=done + rq_1440 spawned; keep", last_line_start)

# --- loop_state ---
notes = (
    "tick1439 RL Noord-Hageland leftover IGS residual; KBO 0462.581.716; live JR2025 NBB WVV PDF; sourced euros assets 837562 omzet empty diensten empty pers 630059 pnl -101 equity 569938 cash 527323 debt 267624 capex 0 dividend 0 brutomarge 626331; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.63m / cash 0.53m / other recv JUMP / geldbeleg liquidated; NOT IGO Holsbeek; next rq_1440 residual dual L5 VL leftover RL Dijleland if 2025 CDN now live + EVERY-10 progress refresh; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1439,1439,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1439")

# --- loop_log ---
entry = (
    "\n## Tick 1439 - 2026-08-19 - rq_1439 RL Noord-Hageland dual residual leftover\n"
    "- Unit: Regionaal Landschap Noord-Hageland VZW / RLNH (leftover IGS / regionaal landschap of 11 mined Noord-Hageland cities; 1 VE) after residual dual hunt (KBO **0462.581.716**; official rlnh.be; live NBB WVV VKT-VZW deposit **2026-00112448** PDF 53095 bytes / 15p; AV **25.03.2026**; header **13.05.2026**; pdfinfo created **18.05.2026**; neerlegging **2026-05-18**; model **VKT-VZW** 25.0.12 m04-f; no commissaris listed; VKT-VZW 6.3/6.5/6.6/6.8/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.2 fondsen + 6.4 + 6.7 sociale balans filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (SBM last table year 2024-12-31; deposit 2025-00553588 only; no 2026pdf); AGB Hulshout 0809.823.801 last JR still 2022 (SBM laatste jaarrekening 2022-01-01 > 2022-12-31; neerlegging 2023-06-15); leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Aarschot / AGB Begijnendijk / AGB CC Diest / AGB Keerbergen / AGB Rotselaar / AGB Patrimonium Scherpenheuvel-Zichem / AGB Tremelo; Tielt-Winge and Bekkevoort no AGB; IGO Holsbeek already mined 1409) — skipped. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024 (2026pdf 2026-00043131 is JR2024). Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 (SBM 2025-00211381; laatste jaarrekening 2024-12-31; neerlegging 2025-07-02). Leftover IGS Regionaal Landschap Noord-Hageland VZW statutory CDN live this tick (HTTP 200 / application/pdf / 53095 / 15p; SBM jaar **2025-12-31**; neerlegging 2026-05-18) — taken (hunt order #2 leftover unmined RL VZW of mined Noord-Hageland cities with full WVV balans; STRONG next leftover RL after RL Westhoek 1438). Distinct from already-mined **IGO Holsbeek** (igs_igoh tick 1409; NOT this entity) / Hofheide 1395 / EcoWerf 1357 / Fluvius Zenne-Dijle 1389 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RLSD VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Noord-Hageland / 0462.581.716 JR2025 extract in entities/sources/leaderboard (0 entity hits). KBO Actief / normale toestand since **19.12.1997**; statutaire naam Regionaal Landschap Noord-Hageland since 19.12.1997; afkorting RLNH since 19.12.1997; VZW since 19.12.1997; zetel Oudepastoriestraat 22 3390 Tielt-Winge since 01.01.2015; **1 VE**; tel 016 63 59 54; e-mail info@rlnh.be; web www.rlnh.be; official site https://www.rlnh.be/; algemeen coordinator Wim Boonen; NACE RSZ 91.420; Werkgever RSZ since 06.01.1998; aanbestedende overheid since 19.12.1997. WVV 2.1 voorzitter Delauré Julien. Official site 11 leden-gemeenten: Aarschot / Begijnendijk / Bekkevoort / Diest / Holsbeek / Keerbergen / Lubbeek / Rotselaar / Scherpenheuvel-Zichem / Tielt-Winge / Tremelo. Plus provincie Vlaams-Brabant. Named share-% unpublished. Contact info@rlnh.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used as source (SBM table assets 837562 matches PDF 837562 — PDF wins). Not every-10 (next 1440 MUST do every-10 progress refresh).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **630059** / **8 VTE**): assets **837562** (was 834115); fixed **250** / IVA empty (aanschaf YE **26950** / afschr YE **26950**) / MVA empty (aanschaf YE **57759** / afschr YE **57759**) / FVA **250**; current **837312**; voorraden **2127**; ST recv **299512** (trade **134983** vs 123405 / other **164529 JUMP** vs 47888); geldbeleg empty (was **220000**); cash **527323 JUMP** vs 430994; prepaid **8350**; equity **569938** (fondsen **145880**; bestemde fondsen **250687**; overgedragen **173371**); voorzieningen empty; schulden **267624** (LT empty; ST **144676** waarvan leveranciers **81186 DROP** vs 91966 + soc/bezold **63490**; deferred **122949** vs 107727); brutomarge **626331** vs 579353; omzet empty; 73 empty; 60/61 empty; pers **630059** / **8 VTE** / 10973 uur / YE **8,7**; afschr empty; andere **1757**; expl **−5484** vs −6154; fin opbr **5926**; fin kosten **542**; tax empty; PnL **−101** vs 0; dividend **0**; over te dragen **173371**; capex **0**.\n"
    "- CSVs: sources +4; entities +1 `vzw_rlnh` parent `sec_flanders`; budgets +46 executed; commitments +1 envelope 626331 AV 25.03.2026; leaderboard +1 annual 626331 / total 837562; foi_queue +1 status=ready never sent; research_queue surgical rq_1439=done + rq_1440 spawn; loop_state ticks_completed=1439.\n"
    "- FOI: `gap_rlnh_omzet_empty_pers_0_63m_cash_0_53m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 0.63m 8 VTE deelwerking unpublished / other recv JUMP 0.16m / cash JUMP 0.53m / geldbeleg 0.22m liquidated / leveranciers DROP 0.08m / vennoten share-pct / relation to IGO Holsbeek unpublished / commissaris unpublished / 1 VE unpublished.\n"
    "- Next: rq_1440 residual dual L5 VL + **EVERY-10 progress refresh** (must update progress_every_10_ticks.md + doge_waste_top10_current.md). Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Dijleland **0461.935.675** JR2025 CDN **2026-00122942** LIVE — STRONG next leftover RL. Leftover RL de Voorkempen 0898.729.546 CDN 2026-00054608 live (NOT Erfgoed Voorkempen IOED 1425). Leftover RL Brabantse Kouters VZW 0874.904.564 CDN 2026-00321333 live (NOT Erfgoed Brabantse Kouters IOED 1428 / KBO 0741.478.094). Leftover RL Meetjesland 0466.277.515 CDN 2026-00092026 live (NOT Cultuuroverleg Meetjesland 1416). Leftover RL Haspengouw 0471.371.597 CDN 2026-00070056 live. Leftover RL Kleine & Grote Nete 0810.764.897 CDN 2026-00054598 live. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 only if a 2025 CDN now appears. Leftover IGS Zender 0822.146.066 only if JR2025 now live. Leftover IGS Zuidrand only if JR2025 now live. Leftover IGS IJzervallei only if a JR2025 PDF now downloads. Leftover IGS Kempens Karakter 0896.244.069 only if a JR2025 PDF now downloads. Leftover IGS Dijk92 only if JR2025 now live. Leftover IGS IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover IOED VARIANT 0738.732.697 still no JR. Leftover IOED Berg en Nete 0671.761.919 still no JR. Leftover PV RL Schelde-Durme 0680.397.590 still no JR. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip Motena / Trupark / Zorgbedrijf ST / already-mined RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / Projectvereniging de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415; AGB Genk JR2025 live but already mined; AGB Lille liquidation; Aarschot AGB already BBC dual; VESPA/AGSL already mined; Bornem still 2024; Hulshout still 2022; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; RL Houtland still 2024; SOLVA already mined; Pajottegem city already mined; IGO Holsbeek already mined).\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1439")
print("tick1439 writes done")
