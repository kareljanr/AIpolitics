#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1556 surgical budgets. Do not rewrite large CSVs whole-file."""
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "son_vlir"
SRC = "src_vlir_jr2025_nbb"

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
    f"bud_vlir_opbr_2025,{ENT},2025,36809788,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 36809788 envelope (leftover public koepel SON; omzet 70 present but commercial-only); JUMP was 29255193; tick1556; primary official NBB VOL-VZW AV 27.03.2026",
    f"bud_vlir_omzet_2025,{ENT},2025,1742031,,,executed,{SRC},strong,2025 omzet 70 1742031 UP was 1739591; commercial-only; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_71_2025,{ENT},2025,954334,,,executed,{SRC},strong,2025 bestellingen in uitvoering toename 71 954334 was -6463392; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_subsid_2025,{ENT},2025,34095480,,,executed,{SRC},strong,2025 lidgeld/schenkingen/legaten/subsidies 73 34095480 UP was 33886224; 730 empty; 733 34095480; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_733_2025,{ENT},2025,34095480,,,executed,{SRC},strong,2025 subsidies 733 34095480 (VLIR-secretariaat 1204939 + VLIR-UOS 32890541); tick1556; primary official NBB VOL-VZW toelichting",
    f"bud_vlir_74_2025,{ENT},2025,14948,,,executed,{SRC},strong,2025 andere bedrijfsopbrengsten 74 14948 DROP was 92117; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_76a_2025,{ENT},2025,2995,,,executed,{SRC},strong,2025 niet-recurrente bedrijfsopbrengsten 76A 2995 UP was 652; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_assets_2025,{ENT},2025,20061015,,,executed,{SRC},strong,2025 balanstotaal 20/58 20061015 DROP was 21865742; VA+vlottend holds; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_va_2025,{ENT},2025,683,,,executed,{SRC},strong,2025 vaste activa 21/28 683 DROP was 773 (FVA only); tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_fva_2025,{ENT},2025,683,,,executed,{SRC},strong,2025 FVA 28 683 DROP was 773 (285/8 borgtochten); tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_vlottend_2025,{ENT},2025,20060332,,,executed,{SRC},strong,2025 vlottende 29/58 20060332 DROP was 21864969; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_wip_2025,{ENT},2025,97848,,,executed,{SRC},strong,2025 bestellingen in uitvoering 37 97848 DROP was 190036; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_recv_2025,{ENT},2025,5774232,,,executed,{SRC},strong,2025 vorderingen ST 40/41 5774232 DROP was 6081653; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_handelsrecv_2025,{ENT},2025,171446,,,executed,{SRC},strong,2025 handelsvorderingen 40 171446 DROP was 872137; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_otherrecv_2025,{ENT},2025,5602786,,,executed,{SRC},strong,2025 overige vorderingen 41 5602786 UP was 5209516; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_beleg_2025,{ENT},2025,9092658,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 9092658 DROP was 14014048; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_cash_2025,{ENT},2025,4929904,,,executed,{SRC},strong,2025 liquide middelen 54/58 4929904 JUMP was 1262768; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_prepaid_2025,{ENT},2025,165690,,,executed,{SRC},strong,2025 overlopend actief 490/1 165690 DROP was 316464; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_equity_2025,{ENT},2025,1250854,,,executed,{SRC},strong,2025 eigen vermogen 10/15 1250854 UP was 938178; fondsen 384957 + bestemde 494109 + overgedragen 371788; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_fondsen_2025,{ENT},2025,384957,,,executed,{SRC},strong,2025 fondsen 10 384957 identiek; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_reserves_2025,{ENT},2025,494109,,,executed,{SRC},strong,2025 bestemde fondsen 13 494109 identiek; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_overgedragen_2025,{ENT},2025,371788,,,executed,{SRC},strong,2025 overgedragen resultaat 14 371788 UP was 59111; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_debt_2025,{ENT},2025,18810160,,,executed,{SRC},strong,2025 schulden 17/49 18810160 DROP was 20927564; EV+debt official 1-euro vs assets; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_st_2025,{ENT},2025,18806970,,,executed,{SRC},strong,2025 ST 42/48 18806970 DROP was 20904044; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_lev_2025,{ENT},2025,280000,,,executed,{SRC},strong,2025 handelsschulden 44 280000 DROP was 1262676; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_vooruit_2025,{ENT},2025,15996948,,,executed,{SRC},strong,2025 vooruitbetalingen 46 15996948 DROP was 17048541; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_taxsoc_2025,{ENT},2025,548413,,,executed,{SRC},strong,2025 belastingen/bezoldigingen 45 548413 DROP was 598497; tax 117740 + pers 430673; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_otherdebt_2025,{ENT},2025,1981608,,,executed,{SRC},strong,2025 overige schulden 48 1981608 DROP was 1994330; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_accrued_2025,{ENT},2025,3191,,,executed,{SRC},strong,2025 overlopend passief 492/3 3191 DROP was 23520; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_costs_2025,{ENT},2025,36749042,,,executed,{SRC},strong,2025 bedrijfskosten 60/66A 36749042 JUMP was 29646426; 61+62+630+640/8 holds; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_61_2025,{ENT},2025,2705917,,,executed,{SRC},strong,2025 diensten 61 2705917 UP was 2692723; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_pers_2025,{ENT},2025,4013097,,,executed,{SRC},strong,2025 bezoldigingen 62 4013097 / 37.9 VTE DROP was 3795133 / 38.1; YE 35.4 / 39 koppen / 58502 uur; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_afschr_2025,{ENT},2025,24820,,,executed,{SRC},strong,2025 afschrijvingen 630 24820 DROP was 31210; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_othercosts_2025,{ENT},2025,30005208,,,executed,{SRC},strong,2025 andere bedrijfskosten 640 30005208 JUMP was 23186574 (VLIR-UOS pass-through); tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_expl_2025,{ENT},2025,60746,,,executed,{SRC},strong,2025 bedrijfswinst 9901 60746 PROFIT was -391233 LOSS; opbr-costs holds; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_fin_2025,{ENT},2025,362454,,,executed,{SRC},strong,2025 financiele opbrengsten 75 362454 DROP was 646656 (751 362438 + 752/9 16); tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_fincost_2025,{ENT},2025,110524,,,executed,{SRC},strong,2025 financiele kosten 65 110524 DROP was 194371 (bankkosten 110524); tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_pnl_2025,{ENT},2025,312676,,,executed,{SRC},strong,2025 resultaat 9903/9904/9905 312676 PROFIT was 61052; tax empty; expl+fin holds; VLIR-secretariaat 93286 + VLIR-UOS 219390; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_commissaris_2025,{ENT},2025,14128,,,executed,{SRC},strong,2025 commissaris 9505 14128 (EY Bedrijfsrevisoren B00160 0438.703.284); extra 95081 19500; tick1556; primary official NBB VOL-VZW",
    f"bud_vlir_capex_2025,{ENT},2025,24820,,,executed,{SRC},strong,2025 MVA meubilair aanschaffingen 8163 24820 (volledig afgeschreven); IVA net 0; tick1556; primary official NBB VOL-VZW",
]
for r in rows:
    check(r, 10, "budgets")
before = (DATA / "budgets.csv").stat().st_size
append_lf(DATA / "budgets.csv", rows)
after = (DATA / "budgets.csv").stat().st_size
if after < before:
    raise SystemExit(f"budgets shrank {before} -> {after}")
print("budgets +%d" % len(rows), before, "->", after)
