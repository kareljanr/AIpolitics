#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1443 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import csv, sys, io
from collections import Counter

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
TS = "2026-08-19T12:50:00Z"
ENT = "vzw_rlmj"
SRC = "src_rlmj_jr2025_nbb"
GAP = "gap_rlmj_omzet_empty_pers_0_61m_cash_0_77m_l5"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    block = "".join(r if r.endswith("\n") else r + "\n" for r in rows)
    path.write_bytes(raw + block.encode("utf-8"))

# --- sources ---
append_lf(DATA / "sources.csv", [
    "src_rlmj_jr2025_nbb,Regionaal Landschap Meetjesland en Leievallei VZW VKT-VZW jaarrekening 2025 (official NBB PDF),http://cdn.staatsbladmonitor.be/2026pdf/2026-00092026.pdf,NBB / RL Meetjesland en Leievallei VZW,2026-08-19,budget,tick1443; VKT-VZW 25.0.11 m04-f PDF 22p / 489080 bytes deposit 2026-00092026; AV 02.04.2026; header 28.04.2026; pdfinfo 29.04.2026; KBO 0466.277.515; assets 866511 cash 771058 JUMP debt 271191 brutomarge 700170 omzet empty code73 empty code60_61 empty pers 605626 pnl 91584; commissaris Baker Tilly 4977",
    "src_rlmj_site,Regionaal Landschap Meetjesland en Leievallei official site,https://rlml.be/,RL Meetjesland en Leievallei VZW,2026-08-19,official_register,tick1443; leftover IGS / regionaal landschap of 14 Meetjesland-Leievallei cities + Gent districts; zetel Oostveldstraat 91 bus 4 9900 Eeklo; contact info@RLML.be; tel 050 70 00 42; 14 gemeenten + Gent-deelgemeenten",
    "src_kbo_rlmj_0466277515,KBO Regionaal Landschap Meetjesland en Leievallei 0466.277.515,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466277515,KBO Public Search FOD Economie,2026-08-19,official_register,tick1443; Actief since 30.11.1998; naam since 27.01.2022; afkorting RLML since 27.01.2022; zetel Oostveldstraat 91 bus 4 9900 Eeklo since 24.06.2020; 1 VE; VZW; NACE 91.420; Werkgever RSZ since 10.05.1999; 25 functiehouders; info@RLML.be www.RLML.be tel 05070042 since 20.04.2023",
    "src_rlmj_foi_contact,RL Meetjesland FOI channel (info@RLML.be; Oostveldstraat 91 bus 4 Eeklo),https://rlml.be/,RL Meetjesland en Leievallei VZW,2026-08-19,official_register,tick1443; 14 member cities + Gent districts + provincie Oost-Vlaanderen; voorzitter Van Hoecke Lieselotte; NOT Cultuuroverleg Meetjesland / COMEET",
])
print("sources +4")

# --- entities ---
p = DATA / "entities.csv"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
if b"\nvzw_rlmj," in raw or raw.startswith(b"vzw_rlmj,"):
    raise SystemExit("vzw_rlmj already present")
if b"0466.277.515" in raw or b"0466277515" in raw:
    raise SystemExit("RL Meetjesland KBO already present")
row = (
    "vzw_rlmj,Regionaal Landschap Meetjesland en Leievallei VZW (leftover IGS / regionaal landschap of 14 mined Meetjesland-Leievallei cities + Gent districts; NOT Cultuuroverleg Meetjesland / COMEET),"
    "Regionaal Landschap Meetjesland et Leievallei ASBL (IGS residuel / paysage regional Meetjesland-Leievallei),"
    "Regionaal Landschap Meetjesland en Leievallei leftover IGS / regional landscape VZW of 14 Meetjesland-Leievallei municipalities + Ghent districts (not Cultuuroverleg Meetjesland / COMEET),"
    "other,sec_flanders,nl,https://rlml.be/,info@RLML.be,Oostveldstraat 91 bus 4 9900 Eeklo,"
    "tick1443 leftover residual IGS VZW of mined Meetjesland-Leievallei cities after leftover AGB hunt; KBO 0466.277.515 Actief since 30.11.1998; official NBB WVV VKT-VZW PDF downloads; sourced euros assets 866511 omzet empty diensten empty pers 605626 pnl 91584 equity 595320 cash 771058 debt 271191 capex 0 dividend 0 brutomarge 700170; FOI ready omzet empty / 73 empty / 60-61 empty / pers 0.61m / cash JUMP / lev DROP / destin 0.60m; distinct from already-mined Cultuuroverleg Meetjesland 1416 / Zorgbedrijf Meetjesland / Welzijnsband Meetjesland / IVM / Veneco / Westlede / RLBK 1442 / RLDV 1441 / RLD 1440 / RLNH 1439"
    "\n"
)
p.write_bytes(raw + row.encode("utf-8"))
print("entities +1 vzw_rlmj")

# --- budgets ---
BUDGETS = [
    ("bud_rlmj_assets_2025", "2025", "866511", "2025 assets 866511 VKT-VZW 20/58; tick1443; primary official NBB WVV"),
    ("bud_rlmj_assets_2024", "2024", "840898", "2024 assets 840898 comparative; tick1443; primary official NBB WVV 20/58"),
    ("bud_rlmj_fixed_2025", "2025", "919", "2025 vaste activa 919 vs 3651; tick1443; primary official NBB WVV 21/28"),
    ("bud_rlmj_fixed_2024", "2024", "3651", "2024 vaste activa 3651 comparative; tick1443; primary official NBB WVV 21/28"),
    ("bud_rlmj_iva_2025", "2025", "0", "2025 IVA empty (was 501); tick1443; primary official NBB WVV 21"),
    ("bud_rlmj_iva_2024", "2024", "501", "2024 IVA 501 comparative; tick1443; primary official NBB WVV 21"),
    ("bud_rlmj_mva_2025", "2025", "919", "2025 MVA 919 vs 3150 (machines only); tick1443; primary official NBB WVV 22/27"),
    ("bud_rlmj_mva_2024", "2024", "3150", "2024 MVA 3150 comparative; tick1443; primary official NBB WVV 22/27"),
    ("bud_rlmj_fva_2025", "2025", "0", "2025 FVA empty (section 6.1.3 filed aanschaf YE 0); tick1443; primary official NBB WVV 28"),
    ("bud_rlmj_current_2025", "2025", "865592", "2025 vlottend 865592 vs 837248; tick1443; primary official NBB WVV 29/58"),
    ("bud_rlmj_current_2024", "2024", "837248", "2024 vlottend 837248 comparative; tick1443; primary official NBB WVV 29/58"),
    ("bud_rlmj_strecv_2025", "2025", "94313", "2025 ST vorderingen 94313 vs 122122; tick1443; primary official NBB WVV 40/41"),
    ("bud_rlmj_strecv_2024", "2024", "122122", "2024 ST vorderingen 122122 comparative; tick1443; primary official NBB WVV 40/41"),
    ("bud_rlmj_trade_2025", "2025", "34063", "2025 handelsvorderingen 34063 vs 39933; tick1443; primary official NBB WVV 40"),
    ("bud_rlmj_trade_2024", "2024", "39933", "2024 handelsvorderingen 39933 comparative; tick1443; primary official NBB WVV 40"),
    ("bud_rlmj_othrecv_2025", "2025", "60251", "2025 overige vorderingen 60251 DROP vs 82190; tick1443; primary official NBB WVV 41"),
    ("bud_rlmj_othrecv_2024", "2024", "82190", "2024 overige vorderingen 82190 comparative; tick1443; primary official NBB WVV 41"),
    ("bud_rlmj_cash_2025", "2025", "771058", "2025 liquide middelen 771058 JUMP vs 712372; tick1443; primary official NBB WVV 54/58"),
    ("bud_rlmj_cash_2024", "2024", "712372", "2024 liquide middelen 712372 comparative; tick1443; primary official NBB WVV 54/58"),
    ("bud_rlmj_prepaid_2025", "2025", "221", "2025 prepaid 221 vs 2754; tick1443; primary official NBB WVV 490/1"),
    ("bud_rlmj_prepaid_2024", "2024", "2754", "2024 prepaid 2754 comparative; tick1443; primary official NBB WVV 490/1"),
    ("bud_rlmj_equity_2025", "2025", "595320", "2025 EV 595320 vs 503736; tick1443; primary official NBB WVV 10/15"),
    ("bud_rlmj_equity_2024", "2024", "503736", "2024 EV 503736 comparative; tick1443; primary official NBB WVV 10/15"),
    ("bud_rlmj_bestemde_2025", "2025", "595320", "2025 bestemde fondsen 595320 vs 503736; tick1443; primary official NBB WVV 13"),
    ("bud_rlmj_bestemde_2024", "2024", "503736", "2024 bestemde fondsen 503736 comparative; tick1443; primary official NBB WVV 13"),
    ("bud_rlmj_debt_2025", "2025", "271191", "2025 schulden 271191 DROP vs 337163 (LT empty); tick1443; primary official NBB WVV 17/49"),
    ("bud_rlmj_debt_2024", "2024", "337163", "2024 schulden 337163 comparative; tick1443; primary official NBB WVV 17/49"),
    ("bud_rlmj_stdebt_2025", "2025", "232138", "2025 ST schulden 232138 DROP vs 293788; tick1443; primary official NBB WVV 42/48"),
    ("bud_rlmj_stdebt_2024", "2024", "293788", "2024 ST schulden 293788 comparative; tick1443; primary official NBB WVV 42/48"),
    ("bud_rlmj_lev_2025", "2025", "67400", "2025 leveranciers 67400 DROP vs 130070; tick1443; primary official NBB WVV 440/4"),
    ("bud_rlmj_lev_2024", "2024", "130070", "2024 leveranciers 130070 comparative; tick1443; primary official NBB WVV 440/4"),
    ("bud_rlmj_taxdebt_2025", "2025", "17231", "2025 belastingen 17231 vs 17419; tick1443; primary official NBB WVV 450/3"),
    ("bud_rlmj_bezold_2025", "2025", "85942", "2025 bezoldigingen/sociale lasten 85942 vs 82887; tick1443; primary official NBB WVV 454/9"),
    ("bud_rlmj_othdebt_2025", "2025", "61565", "2025 overige schulden 61565 vs 63413; tick1443; primary official NBB WVV 48"),
    ("bud_rlmj_deferred_2025", "2025", "39053", "2025 deferred 39053 vs 43374; tick1443; primary official NBB WVV 492/3"),
    ("bud_rlmj_deferred_2024", "2024", "43374", "2024 deferred 43374 comparative; tick1443; primary official NBB WVV 492/3"),
    ("bud_rlmj_brutomarge_2025", "2025", "700170", "2025 brutomarge 700170 vs 686412; omzet 70 empty; 73 empty; 60/61 empty; tick1443; primary official NBB WVV 9900"),
    ("bud_rlmj_brutomarge_2024", "2024", "686412", "2024 brutomarge 686412 comparative; tick1443; primary official NBB WVV 9900"),
    ("bud_rlmj_nietrec_2025", "2025", "2911", "2025 niet-recurrente bedrijfsopbrengsten 2911; tick1443; primary official NBB WVV 76A"),
    ("bud_rlmj_pers_2025", "2025", "605626", "2025 pers 605626 / 7.6 VTE vs 605582 / 7.9; tick1443; primary official NBB WVV 62"),
    ("bud_rlmj_pers_2024", "2024", "605582", "2024 pers 605582 / 7.9 VTE comparative; tick1443; primary official NBB WVV 62"),
    ("bud_rlmj_afschr_2025", "2025", "2732", "2025 afschrijvingen 2732 vs 3231; tick1443; primary official NBB WVV 630"),
    ("bud_rlmj_expl_2025", "2025", "91812", "2025 expl +91812 vs +77598; tick1443; primary official NBB WVV 9901"),
    ("bud_rlmj_expl_2024", "2024", "77598", "2024 expl +77598 comparative; tick1443; primary official NBB WVV 9901"),
    ("bud_rlmj_finkost_2025", "2025", "228", "2025 fin kosten 228 vs 190; tick1443; primary official NBB WVV 65/66B"),
    ("bud_rlmj_pnl_2025", "2025", "91584", "2025 PnL +91584 vs +77408; tick1443; primary official NBB WVV 9904"),
    ("bud_rlmj_pnl_2024", "2024", "77408", "2024 PnL +77408 comparative; tick1443; primary official NBB WVV 9904"),
    ("bud_rlmj_div_2025", "2025", "0", "2025 dividend 0 / no 694; tick1443; primary official NBB WVV"),
    ("bud_rlmj_capex_2025", "2025", "0", "2025 IVA/MVA/FVA aanschaffingen empty; tick1443; primary official NBB WVV 8029/8169/8365"),
    ("bud_rlmj_commissaris_2025", "2025", "4977", "2025 commissaris Baker Tilly mandaat 4977; tick1443; primary official NBB WVV 6.6"),
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
    f"comm_rlmj_jr2025_bruto,Regionaal Landschap Meetjesland en Leievallei VZW JR2025 leftover IGS dual (brutomarge 0.70m / pers 0.61m / cash JUMP 0.77m),{ENT},RL Meetjesland en Leievallei VZW / 14 Meetjesland-Leievallei cities,WVV VZW; NBB neerlegging; 14 Meetjesland-Leievallei gemeenten + Gent districts + provincie Oost-Vlaanderen,2026-04-02,1998,,700170,,,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00092026.pdf,Local leftover IGS map VL Meetjesland-Leievallei landschap — 0.70m brutomarge / empty omzet 70 / empty 73 / empty 60-61 / pers 0.61m,Publish empty 70/73/60-61 split + pers 0.61m + cash JUMP + lev DROP + destin 0.60m + vennoten share-pct; do not keep leftover RLML VZW as dual unpublished vehicle,{SRC},strong,Vlaanderen>Oost-Vlaanderen>Meetjesland>RLML>JR2025_L5,tick1443; assets 866511 omzet empty diensten empty pers 605626 pnl 91584 equity 595320 cash 771058 debt 271191 capex 0 dividend 0 brutomarge 700170; FOI ready not sent; not TE-additive of 348bn; NOT Cultuuroverleg Meetjesland / COMEET",
])
print("commitments +1")

append_lf(DATA / "leaderboard.csv", [
    f"lb_rlmj_omzet_empty_pers_0_61m_cash_0_77m,Regionaal Landschap Meetjesland en Leievallei VZW JR2025 leftover IGS: empty omzet 70 / pers 0.61m / cash JUMP 0.77m / brutomarge 0.70m,L5,local_budget_line,Vlaanderen>Oost-Vlaanderen>Meetjesland>RLML>JR2025_L5,700170,866511,Leftover dual IGS VZW: assets 0.87m / equity 0.60m / pnl +0.09m / omzet empty / 73 empty / 60-61 empty / pers 0.61m 7.6 VTE / cash 0.77m JUMP / debt 0.27m / lev 0.07m DROP / destin 0.60m / dividend 0,strong,{SRC},RL Meetjesland en Leievallei VZW / 14 Meetjesland-Leievallei cities,Local leftover IGS map VL Meetjesland-Leievallei landschap — JR2025 live; dual empty omzet 70 FOI,Official NBB WVV 2026-08-19: brutomarge 0.70m / pers 0.61m / cash JUMP 0.77m / PnL +0.09m,6.5,6.1,2.2,6.0,Publish empty 70/73/60-61 split + pers 0.61m + cash JUMP + lev DROP + destin 0.60m + vennoten share-pct; do not keep leftover RLML VZW as dual unpublished vehicle,active,,tick1443; leftover IGS after leftover AGB hunt; FOI ready not sent; not TE-additive of 348bn; distinct from already-mined Cultuuroverleg Meetjesland 1416 / RLBK 1442 / RLDV 1441 / RLD 1440 / RLNH 1439",
])
print("leaderboard +1")

append_lf(DATA / "foi_queue.csv", [
    f"{GAP},Vlaanderen>Oost-Vlaanderen>Meetjesland>RLML>JR2025_L5,{ENT},omzet 70 empty + 73 empty + 60/61 empty + bruto 700170 + pers 62 605626 / 7.6 VTE + cash JUMP 771058 vs 712372 + other recv DROP 60251 vs 82190 + leveranciers DROP 67400 vs 130070 + destin 595320 + deferred 39053 + othdebt 61565 + capex 0 + commissaris 4977 + off-balance subsidieafstand 32000 + vennoten share-pct unpublished + 1 VE unpublished + relation to Cultuuroverleg Meetjesland unpublished,Leftover RLML VZW after leftover AGB hunt: 0.70m brutomarge / empty omzet 70 hides public-perimeter landschap vehicle,8,Regionaal Landschap Meetjesland en Leievallei vzw / Bestuursorgaan,info@RLML.be,Oostveldstraat 91 bus 4 9900 Eeklo,docs/doge/foi/drafts/{GAP}.md,ready,2026-08-19,,,,,,comm_rlmj_jr2025_bruto,lb_rlmj_omzet_empty_pers_0_61m_cash_0_77m,{TS},{TS},tick1443 leftover IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VKT-VZW PDF now extracted (489080 bytes 22p deposit 2026-00092026). FOI ready not sent. NOT Cultuuroverleg Meetjesland / COMEET. Leftover cultuur-IGS ECRU/Neteland/Route42/Stuifzand/Noordrand/IJzervallei/Kempens Karakter still no JR. Zender/Zuidrand/Dijk92/IVAREM still JR2024. VARIANT/Berg en Nete still no JR. Dommelhof leftover EVA no jaarrekening. Leftover IOED Erfpunt/PORTIVA/WinAr/Schelde-Durme IOED/Brugge en Ommeland/Nete en Aa/Hydra/Viersprong still no JR2025. Leftover RL Houtland still JR2024. Leftover RL Haspengouw JR2025 CDN 2026-00070056 live leftover for next. Leftover RL Kleine en Grote Nete JR2025 CDN 2026-00054598 live leftover.",
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
if not last_s.startswith("rq_1443,"):
    raise SystemExit(f"expected last row rq_1443, got {last_s[:80]!r}")
parts_head = last_s.split(",", 6)
if len(parts_head) >= 5 and parts_head[4] == "done":
    raise SystemExit("rq_1443 already done — concurrent tick; STOP")
last_line_start = size - (len(stripped) - last_nl)
done = (
    "rq_1443,RL Meetjesland JR2025 leftover dual residual,hole_fill,5,done,L5,vzw_rlmj,"
    "Completed: Regionaal Landschap Meetjesland en Leievallei VZW leftover IGS / regionaal landschap of 14 mined Meetjesland-Leievallei cities + Gent districts after leftover AGB hunt; KBO 0466.277.515 Actief; live JR2025 official NBB WVV VKT-VZW PDF (489080 bytes 22p deposit 2026-00092026; AV 02.04.2026; header 28.04.2026; created 29.04.2026; commissaris Baker Tilly 4977); sourced euros assets 866511 omzet empty diensten empty pers 605626 pnl 91584 equity 595320 cash 771058 debt 271191 capex 0 dividend 0 brutomarge 700170; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.61m / cash JUMP / lev DROP / destin 0.60m; NOT Cultuuroverleg Meetjesland / COMEET,"
    f"{GAP},2026-08-19T12:35:00Z,{TS},"
    "tick1443 RL Meetjesland en Leievallei VZW leftover IGS residual; KBO 0466.277.515; live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1444 residual dual L5 VL leftover RL Haspengouw if 2025 CDN still live"
)
spawn = (
    "rq_1444,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,,"
    "Residual dual L5 VL JR2025 hole-fill: next AGB/GE/zorg/EVA/IGS not yet mined (prior 1255-1443 done including RL Meetjesland 1443 leftover IGS live NBB WVV / RL Brabantse Kouters 1442 leftover IGS live NBB WVV / RL de Voorkempen 1441 leftover IGS live NBB WVV / RL Dijleland 1440 leftover IGS live NBB WVV + every-10 / RL Noord-Hageland 1439 leftover IGS live NBB WVV / RL Westhoek 1438 leftover IGS live NBB WVV / RL Vlaamse Ardennen 1437 leftover IGS live NBB WVV / RL Pajottenland 1436 leftover IGS live NBB WVV / RL Rivierenland 1435 leftover IGS live NBB WVV / RL Zuid-Hageland 1434 leftover IGS live NBB WVV / RL Kempen en Maasland 1433 leftover IGS live NBB WVV / RL Schelde-Durme VZW 1432 leftover IGS live NBB WVV / Erfgoed Rupelstreek 1431 leftover IGS/IOED live NBB WVV / RL Lage Kempen 1430 leftover IGS live NBB WVV + every-10); leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; leftover RL Haspengouw & Voeren 0471.371.597 JR2025 CDN 2026-00070056 LIVE leftover — STRONG next leftover RL; leftover RL Kleine & Grote Nete 0810.764.897 JR2025 CDN 2026-00054598 live leftover; leftover RL Houtland & Polders 0472.947.254 last JR still 2024 — take only if JR2025 now live; leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover cultuur-IGS ECRU 0889.287.288 / Neteland 0687.552.727 / Route42 0743.533.605 / Stuifzand 0809.181.918 still no jaarrekening — take only if a 2025 CDN now appears; leftover IGS Zender 0822.146.066 last JR still 2024 — take only if JR2025 now live; leftover IGS Streekvereniging Zuidrand 0672.985.901 last JR still 2024 — take only if JR2025 now live; leftover IGS Projectvereniging IJzervallei 0736.658.976 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening — take only if a JR2025 PDF now downloads; leftover IGS IVAREM 0267.403.264 last JR still 2024 — take only if a JR2025 PDF now downloads; leftover IGS Dijk92 0806.383.071 last JR still 2024 — take only if JR2025 now live; Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 if a 2025 CDN is live; leftover IOED VARIANT 0738.732.697 still no jaarrekening; leftover IOED Berg en Nete 0671.761.919 still no jaarrekening; leftover PV RL Schelde-Durme 0680.397.590 still no JR — take only if a JR2025 PDF now downloads; leftover daughters / Nuhma-adjacent only after leftover AGB/IGS; skip already-mined RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RL Noord-Hageland 1439 / RL Westhoek 1438 / RL Vlaamse Ardennen 1437 / RL Pajottenland 1436 / RL Rivierenland 1435 / RL Zuid-Hageland 1434 / RL Kempen en Maasland 1433 / RL Schelde-Durme VZW 1432 / Erfgoed Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Zuidwest 1424 / BIONERGA LOGISTICS 1423 / Vrijetijdsregio Druivenstreek 1422 / Viertoren 1421 / CO7 1420 / de Merode 1419 / DVV Midwest 1418 / Cultuurregio Leie Schelde 1417 / Cultuuroverleg Meetjesland 1416 / DVV Westhoek 1415 / AGB De Kluize 1414 / PATRIMONIUM MBS 1413 / IOK Afvalbeheer 1412 / AGB Merchtem 1411 / Sunfin 1410 / IGO 1409 / Rematics 1408 / AGB Patri 1407 / MLSO 1406 / AGB Tielt 1405 / Psilon 1404 / VERKO 1403 / DDS 1402 / OVCO 1401 / IGL 1400 / Otary RS 1399 / IGS IBEG 1398 / IGS IVEBICA 1397 / IGS Pontes 1396 / IGS Hofheide 1395 / IGS Westlede 1394 / HAVICREM 1393 / IVLA 1392 / Fluvius stack 1382-1391 / ILvA 1344 / Aquaduin/IWVA 1349 / ECO2050 1360 / Nuhma cv 1356 / MyCSN 1363 / IOK DV 1368 / Bionerga NV 1354 / Limburg.net 1353 / SOLVA / Interwaas / Veneco / IGEMO / Leiedal / WVI / IOK / Interleuven / Haviland / IGEAN / IDM / IVM / IVVO / IVIO / IVBO / IMOG / IVAGO / MIWA / IVOO / EcoWerf / Zorgbedrijf Rivierenland / Pajottegem city; skip Motena / Trupark / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; IVAREM still 2024; Dommelhof still no 2025 PDF; Dijk92 still 2024; Zuidrand still 2024; Noordrand still no JR; IJzervallei still no JR; ECRU/Neteland/Route42/Stuifzand still no JR; Zender still 2024; Kempens Karakter still no JR; VARIANT still no JR; Berg en Nete still no JR; WinAr still no JR; Brugge-en-Ommeland IOED still no JR; Viersprong still no JR; RL Houtland still 2024; AGB Lille liquidation; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; AGB Genk JR2025 live but already mined; Aarschot AGB already BBC dual; VESPA/AGSL 2025 CDNs already mined; Bornem still 2024; Hulshout still 2022; ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 + iok.be TLS,,"
    f"{TS},{TS},"
    "spawned tick1443 after RL Meetjesland leftover IGS live NBB WVV; next residual dual L5 VL leftover RL Haspengouw if a 2025 CDN is now live"
)
with p.open("r+b") as f:
    f.seek(last_line_start)
    f.truncate()
    f.write(done.encode("utf-8") + b"\n" + spawn.encode("utf-8") + b"\n")
print("research_queue patched: rq_1443=done + rq_1444 spawned; keep", last_line_start)

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
    f"tick1443 RL Meetjesland leftover IGS residual; KBO 0466.277.515; live JR2025 NBB WVV PDF; sourced euros assets 866511 omzet empty diensten empty pers 605626 pnl 91584 equity 595320 cash 771058 debt 271191 capex 0 dividend 0 brutomarge 700170; FOI ready empty 70 / empty 73 / empty 60-61 / pers 0.61m / cash JUMP / lev DROP / destin 0.60m; NOT Cultuuroverleg Meetjesland / COMEET; next rq_1444 residual dual L5 VL leftover RL Haspengouw if 2025 CDN still live; FOI ready {foi_ready} answered {foi_ans} partial {foi_part} total {foi_tot}; continuous hole_fill"
)
text = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1443,1443,no,{notes}\n"
)
(DATA / "loop_state.csv").write_bytes(text.encode("utf-8"))
print("loop_state rewritten LF ticks=1443")

# --- loop_log ---
entry = (
    "\n## Tick 1443 - 2026-08-19 - rq_1443 RL Meetjesland dual residual leftover\n"
    "- Unit: Regionaal Landschap Meetjesland en Leievallei VZW / RLML (leftover IGS / regionaal landschap of 14 mined Meetjesland-Leievallei cities + Gent districts; 1 VE) after residual dual hunt (KBO **0466.277.515**; official rlml.be; live NBB WVV VKT-VZW deposit **2026-00092026** PDF 489080 bytes / 22p; AV **02.04.2026**; header **28.04.2026**; pdfinfo created **29.04.2026**; model **VKT-VZW** 25.0.11 m04-f; commissaris Baker Tilly Bedrijfsrevisoren BV B00190 / 0449.065.260 / De Blander Christel A02258 fee **4977**; VKT-VZW 6.3/7/8 not filed; 6.1.1 IVA + 6.1.2 MVA + 6.1.3 FVA + 6.2 fondsen + 6.4 + 6.5 + 6.6 + 6.7 sociale balans + 6.8 waarderingsregels filed). Leftover AGB first: AGB Bornem 0877.556.624 last JR still 2024 (no 2026pdf; 2025pdf 2025-00553588 is JR2024); AGB Hulshout 0809.823.801 last JR still 2022; leftover Mechelen/Kortrijk/Brugge/Roeselare 404/403; leftover AGB of member cities already mined (AGB Aalter / AGB Assenede / AGB Deinze / AGB Evergem / AGB Kaprijke / AGB Maldegem / AGB Nazareth-De Pinte / sogent / AGB District09 / AGB Erfgoed Gent / AGB Kunsten en Design Gent) — skipped. Eeklo / Lochristi / Lievegem / Zulte / Sint-Laureins / Sint-Martens-Latem have no AGB in entities. Leftover IGS Cultuur Noordrand 0740.822.256 still no jaarrekening. Leftover cultuur-IGS ECRU **0889.287.288** / Neteland **0687.552.727** / Route42 **0743.533.605** / Stuifzand **0809.181.918** still no jaarrekening. Leftover IGS Zender **0822.146.066** last JR still 2024. Leftover IGS Zuidrand 0672.985.901 last JR still 2024. Leftover IGS IJzervallei 0736.658.976 still no jaarrekening. Leftover IGS Kempens Karakter 0896.244.069 still no jaarrekening. Leftover IGS IVAREM 0267.403.264 last JR still 2024. Dijk92 0806.383.071 last JR still 2024. Dommelhof leftover Limburg EVA KBO 0777.495.085 still no jaarrekening. Leftover IOED VARIANT **0738.732.697** still no jaarrekening. Leftover IOED Berg en Nete **0671.761.919** still no jaarrekening. Leftover IOED Erfpunt / PORTIVA / WinAr 0811.517.440 / Schelde-Durme IOED / Brugge en Ommeland 0554.701.428 / Land van Nete en Aa / Hydra / Viersprong 0809.450.251 still no JR2025 CDN this tick. Leftover RL Houtland & Polders **0472.947.254** last JR still 2024 — not taken. Leftover IGS Regionaal Landschap Meetjesland en Leievallei VZW statutory CDN live this tick (HTTP 200 / application/pdf / 489080 / 22p; jaar **2025-12-31**) — taken (hunt order #2 leftover unmined RL VZW of mined Meetjesland-Leievallei cities with full WVV balans; STRONG next leftover RL after RL Brabantse Kouters 1442). Distinct from already-mined **Cultuuroverleg Meetjesland / COMEET** (igs_cmtj tick 1416; KBO 0867.378.552; NOT this entity) / Zorgbedrijf Meetjesland / Welzijnsband Meetjesland / IVM / Veneco / Westlede / RLBK 1442 / RLDV 1441 / RLD 1440 / RLNH 1439. First confirmed not already extracted as JR2025 WVV euros: no Regionaal Landschap Meetjesland / 0466.277.515 JR2025 extract in entities/sources/leaderboard (0 KBO hits). KBO Actief / normale toestand since **30.11.1998**; statutaire naam Regionaal Landschap Meetjesland en Leievallei since 27.01.2022; afkorting RLML since 27.01.2022; VZW since 30.11.1998; zetel Oostveldstraat 91 bus 4 9900 Eeklo since 24.06.2020; **1 VE**; official site https://rlml.be/; contact info@RLML.be; tel 050 70 00 42 since 20.04.2023; NACE RSZ 91.420; Werkgever RSZ since 10.05.1999; **25 functiehouders**. WVV 2.1 voorzitter Van Hoecke Lieselotte. Dagelijks bestuur: De Groote Peter (since 14.03.2017) / Dewulf Loes / Van Hoecke Lieselotte / Verdegem Josse. Official site 14 leden-gemeenten: Aalter / Assenede / Deinze / Eeklo / Evergem / Gent (deelgemeenten Drongen / Sint-Denijs-Westrem / Zwijnaarde) / Kaprijke / Lievegem / Lochristi / Maldegem / Nazareth-De Pinte / Sint-Laureins / Sint-Martens-Latem / Zulte. Named share-% unpublished. Contact info@RLML.be. NBB consult skipped (403/SPA); euros extracted from the official VKT-VZW deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor HTML not used as euro source — PDF wins. Not every-10 (next 1450 MUST do every-10).\n"
    "- EUR strong (primary official WVV VKT-VZW; **omzet 70 empty**; **lidgeld/subsidies 73 empty**; **60/61 empty** so diensten unpublished as a split; only brutomarge published; pers 62 filed **605626** / **7,6 VTE**): assets **866511** (was 840898); fixed **919** vs 3651 / IVA empty (was 501) / MVA **919** vs 3150 (machines only) / FVA empty; current **865592** vs 837248; ST recv **94313** vs 122122 (trade **34063** vs 39933 / other **60251 DROP** vs 82190); geldbeleg empty; cash **771058 JUMP** vs 712372; prepaid **221** vs 2754; equity **595320** (bestemde fondsen **595320** vs 503736); voorzieningen empty; schulden **271191 DROP** vs 337163 (LT empty; ST **232138 DROP** vs 293788 waarvan leveranciers **67400 DROP** vs 130070 + tax **17231** + soc/bezold **85942** + overige **61565**; deferred **39053** vs 43374); brutomarge **700170** vs 686412; niet-recurrente 76A **2911**; omzet empty; 73 empty; 60/61 empty; pers **605626** / **7,6 VTE** / 11832 uur / YE **7,6**; afschr **2732**; expl **+91812** vs +77598; fin opbr empty; fin kosten **228**; tax empty; PnL **+91584** vs +77408; dividend **0**; toevoeging bestemde **91584**; capex **0**; commissaris **4977**. Off-balance: subsidieafstand als waarborg kredietlijn max **32000**. PDF 1-euro rounding: trade+other 94314 vs published ST recv 94313; tax+bezold 103173 vs published 103174.\n"
    f"- CSVs: sources +4; entities +1 `vzw_rlmj` parent `sec_flanders`; budgets +{len(added)} executed; commitments +1 envelope 700170 AV 02.04.2026; leaderboard +1 annual 700170 / total 866511; foi_queue +1 status=ready never sent; research_queue surgical rq_1443=done + rq_1444 spawn; loop_state ticks_completed=1443. Inventory after write: budgets {inv['budgets.csv']} · commitments {inv['commitments.csv']} · leaderboard {inv['leaderboard.csv']} · entities {inv['entities.csv']} · sources {inv['sources.csv']} · FOI ready {foi_ready} / answered {foi_ans} / partial {foi_part} / total {foi_tot}.\n"
    "- FOI: `gap_rlmj_omzet_empty_pers_0_61m_cash_0_77m_l5` ready not sent — omzet 70 empty / 73 empty / diensten 60/61 empty / pers 0.61m 7.6 VTE deelwerking unpublished / cash JUMP 0.77m / lev DROP 0.07m / destin 0.60m / other recv DROP 0.06m / othdebt 0.06m / capex 0 / commissaris 4977 / off-balance 32k / vennoten share-pct / relation to Cultuuroverleg Meetjesland unpublished / 1 VE unpublished.\n"
    "- Next: rq_1444 residual dual L5 VL. Leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads. Leftover RL Haspengouw **0471.371.597** JR2025 CDN **2026-00070056** LIVE — STRONG next leftover RL. Leftover RL Kleine & Grote Nete 0810.764.897 CDN 2026-00054598 live. Leftover RL Houtland & Polders 0472.947.254 only if JR2025 now live. Leftover IGS Cultuur Noordrand 0740.822.256 only if a JR2025 PDF now downloads. Other leftover cultuur-IGS ECRU / Neteland / Route42 / Stuifzand only if a 2025 CDN now appears. Leftover IGS Zender / Zuidrand / IJzervallei / Kempens Karakter / Dijk92 / IVAREM only if JR2025 now live. Dommelhof only if a real 2025 PDF now downloads. Leftover IOED Erfpunt / PORTIVA / WinAr / Schelde-Durme IOED / Brugge en Ommeland / Land van Nete en Aa / Hydra / Viersprong if a 2025 CDN is live. Leftover daughters / Nuhma-adjacent only after leftover AGB/IGS. Skip already-mined RL Meetjesland 1443 / RL Brabantse Kouters 1442 / RL de Voorkempen 1441 / RL Dijleland 1440 / RLNH 1439 / RLWH 1438 / RLVAD 1437 / RLPZ 1436 / RLRL 1435 / RLZH 1434 / RLKM 1433 / RL Schelde-Durme VZW 1432 / Rupelstreek 1431 / RL Lage Kempen 1430 / Kusterfgoed 1429 / Erfgoed Brabantse Kouters 1428 / Erfgoed Denderland 1427 / Erfgoed Noorderkempen 1426 / Erfgoed Voorkempen 1425 / Cultuuroverleg Meetjesland 1416; AGB Genk already mined; Bornem still 2024; Hulshout still 2022; IGO Holsbeek already mined.\n"
)
lp = ROOT / "docs/doge/loop_log.md"
lraw = lp.read_bytes()
if lraw and not lraw.endswith(b"\n"):
    lraw += b"\n"
if b"## Tick 1443 -" in lraw:
    raise SystemExit("loop_log already has tick 1443 — concurrent?")
lp.write_bytes(lraw + entry.encode("utf-8"))
print("loop_log appended tick 1443")
print("DONE tick 1443")
