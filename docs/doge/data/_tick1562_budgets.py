#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1562 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "vzw_cult"
SRC = "src_cultuurconnect_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def check(row, n, label):
    fields = next(csv.reader(io.StringIO(row)))
    got = len(fields)
    if got != n:
        raise SystemExit(f"{label} ncols {got} != {n}: {row[:180]}")
    if any("," in f for f in fields):
        raise SystemExit(f"{label} has comma inside a field: {[f for f in fields if ',' in f]}")

rows = [
    f"bud_cult_opbr_2025,{ENT},2025,12751502,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 12751502 envelope (leftover public koepel VZW; omzet 70 present but commercial-only); JUMP was 10435697; tick1562; primary official NBB VOL-VZW AV 26.03.2026",
    f"bud_cult_omzet_2025,{ENT},2025,5026615,,,executed,{SRC},strong,2025 omzet 70 5026615 UP was 4608836; commercial-only vs 73 7718118; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_subsid_2025,{ENT},2025,7718118,,,executed,{SRC},strong,2025 lidgeld/schenkingen/legaten/subsidies 73 7718118 JUMP was 5813768; 730 empty; 733 7718118; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_733_2025,{ENT},2025,7718118,,,executed,{SRC},strong,2025 subsidies 733 7718118 JUMP was 5813768; split Flanders/other unpublished; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_74_2025,{ENT},2025,6728,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 6728 DROP was 13094; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_76a_2025,{ENT},2025,41,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 41 (was 0); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_assets_2025,{ENT},2025,6483521,,,executed,{SRC},strong,2025 balanstotaal 20/58 6483521 DROP was 7429391; VA+vlottend holds; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_va_2025,{ENT},2025,22644,,,executed,{SRC},strong,2025 vaste activa 21/28 22644 DROP was 77922; IVA+MVA+FVA holds; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 21 0 DROP was 39671; aanschaf YE 799234 fully written off; capex 8021 0; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_mva_2025,{ENT},2025,21300,,,executed,{SRC},strong,2025 MVA 22/27 21300 DROP was 33147; install 21300 DROP; meubilair 0; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_install_2025,{ENT},2025,21300,,,executed,{SRC},strong,2025 installaties machines uitrusting 23 21300 DROP was 32790; capex 8162 9151; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_fva_2025,{ENT},2025,1344,,,executed,{SRC},strong,2025 FVA 28 1344 DROP was 5104 (285/8 borgtochten); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_vlottend_2025,{ENT},2025,6460877,,,executed,{SRC},strong,2025 vlottende 29/58 6460877 DROP was 7351469; recv+cash+prepaid holds; beleg empty; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_recv_2025,{ENT},2025,1274493,,,executed,{SRC},strong,2025 vorderingen ST 40/41 1274493 JUMP was 947940; handelsrecv 40 396745 JUMP; other recv 41 877748 UP; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_handelsrecv_2025,{ENT},2025,396745,,,executed,{SRC},strong,2025 handelsvorderingen 40 396745 JUMP was 171281; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_otherrecv_2025,{ENT},2025,877748,,,executed,{SRC},strong,2025 overige vorderingen 41 877748 UP was 776659; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_cash_2025,{ENT},2025,5103622,,,executed,{SRC},strong,2025 liquide middelen 54/58 5103622 DROP was 6315997; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_prepaid_2025,{ENT},2025,82762,,,executed,{SRC},strong,2025 overlopend actief 490/1 82762 DROP was 87532 (over te dragen kosten 70698 + verkregen opbr 12064); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_equity_2025,{ENT},2025,5294808,,,executed,{SRC},strong,2025 eigen vermogen 10/15 5294808 DROP was 6383883; fondsen empty; reserves 13 4106351; overgedragen 14 1188457; kapsubs 15 0; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_reserves_2025,{ENT},2025,4106351,,,executed,{SRC},strong,2025 bestemde fondsen 13 4106351 DROP was 4640912; sociaal passief 1400000 + chargeback bib 494881 + Digitaal Podium 11470 + innovatieagenda 2200000; 791 onttrekking 2814680; 691 toevoeging 2280119; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_overgedragen_2025,{ENT},2025,1188457,,,executed,{SRC},strong,2025 overgedragen resultaat 14 1188457 DROP was 1703299; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_kapsubs_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 0 DROP was 39671 (IVA fully written off); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_debt_2025,{ENT},2025,1188713,,,executed,{SRC},strong,2025 schulden 17/49 1188713 UP was 1045509; ST+accrued holds; LT empty; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_st_2025,{ENT},2025,969510,,,executed,{SRC},strong,2025 ST 42/48 969510 DROP was 1045076; lev+taxsoc holds; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_lev_2025,{ENT},2025,406391,,,executed,{SRC},strong,2025 handelsschulden 44 / leveranciers 440/4 406391 DROP was 524807; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_taxsoc_2025,{ENT},2025,563119,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 563119 UP was 520269; tax 395 + bezold 562724 holds; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_accrued_2025,{ENT},2025,219203,,,executed,{SRC},strong,2025 overlopend passief 492/3 219203 JUMP was 433 (toe te rekenen 4100 + over te dragen opbr 215103); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_costs_2025,{ENT},2025,13842153,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 13842153 UP was 13500224; 60+61+62+630+640/8 holds; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_60_2025,{ENT},2025,8128810,,,executed,{SRC},strong,2025 handelsgoederen 60 8128810 UP was 8005600 (digital content/licenses pass-through vs omzet 5.03m); tick1562; primary official NBB VOL-VZW",
    f"bud_cult_61_2025,{ENT},2025,460127,,,executed,{SRC},strong,2025 diensten 61 460127 DROP was 530719; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_pers_2025,{ENT},2025,5184352,,,executed,{SRC},strong,2025 bezoldigingen 62 5184352 / 51 VTE UP was 4786795 / 48.9; YE 50.9 / 38 voltijds + 17 deeltijds / 55 koppen 9086 / 81079 uur; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_afschr_2025,{ENT},2025,60669,,,executed,{SRC},strong,2025 afschrijvingen 630 60669 DROP was 156616; IVA 8071 39671 + MVA install 8272 20642 + meubilair 8273 356; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_othercosts_2025,{ENT},2025,8195,,,executed,{SRC},strong,2025 andere bedrijfskosten 640/8 8195 DROP was 20493; 66A empty; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_expl_2025,{ENT},2025,1090651,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 1090651 LOSS was 3064527 LOSS; opbr-costs holds; two consecutive years LOSS; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_fininc_2025,{ENT},2025,41529,,,executed,{SRC},strong,2025 financiele opbrengsten 75 41529 DROP was 1288856 (751 41178 + 752/9 351); prior-year 752/9 1247042 one-off; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_fincost_2025,{ENT},2025,282,,,executed,{SRC},strong,2025 financiele kosten 65 282 DROP was 441; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_pnl_2025,{ENT},2025,1049404,,,executed,{SRC},strong,2025 resultaat 9903/9904/9905 1049404 LOSS was 1776112 LOSS; tax empty; expl+fin-fincost holds; 9906 653896 official 1-euro vs 14P+9905 653895; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_commissaris_2025,{ENT},2025,7930,,,executed,{SRC},strong,2025 commissaris 9505 7930 (Bedrijfsrevisoren BV B00240 0456.567.023 / Debraekeleer Gerre A02633); extra empty; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_capex_2025,{ENT},2025,9151,,,executed,{SRC},strong,2025 capex IVA 8021 0 + MVA install 8162 9151 + meubilair 8163 0 = 9151; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_onttrek_2025,{ENT},2025,2814680,,,executed,{SRC},strong,2025 onttrekking eigen vermogen 791 2814680; 691 toevoeging 2280119; 9906 653896; tick1562; primary official NBB VOL-VZW",
    f"bud_cult_uren_2025,{ENT},2025,81079,,,executed,{SRC},strong,2025 sociale balans uren 1013 81079; in 6 VTE / uit 5.7 VTE; PC 32901; opleiding 6151; groepsverzekering 130340; tick1562; primary official NBB VOL-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)
