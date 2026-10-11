#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwbr"
SRC = "src_cwbr_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwbr_assets_2025,{ENT},2025,6760334,,,executed,{SRC},strong,2025 assets 6760334 DROP (was 7503597); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_vaste_2025,{ENT},2025,4913156,,,executed,{SRC},strong,2025 vaste activa 21/28 4913156 DROP (was 5032802); IVA 21 74657 JUMP; FVA 28 15100; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_mva_2025,{ENT},2025,4823399,,,executed,{SRC},strong,2025 MVA 22/27 4823399 DROP (was 5006614); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_gebouwen_2025,{ENT},2025,4703997,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 4703997 DROP (was 4902817); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_install_2025,{ENT},2025,58064,,,executed,{SRC},strong,2025 installaties 23 58064 UP (was 35472); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_meubilair_2025,{ENT},2025,61338,,,executed,{SRC},strong,2025 meubilair 24 61338 DROP (was 68325); leasing 25 empty; overige 26 empty; in aanbouw 27 empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_iva_2025,{ENT},2025,74657,,,executed,{SRC},strong,2025 IVA 21 74657 JUMP (was 11088; aanschaffingen 8022 74979); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_fva_2025,{ENT},2025,15100,,,executed,{SRC},strong,2025 FVA 28 15100 (aandelen 284 1000 + borg 285/8 14100); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_current_2025,{ENT},2025,1847178,,,executed,{SRC},strong,2025 vlottende 29/58 1847178 DROP (was 2470795); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_strecv_2025,{ENT},2025,788151,,,executed,{SRC},strong,2025 ST vorderingen 40/41 788151 (trade 241433 + other 546718); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_handelsrecv_2025,{ENT},2025,241433,,,executed,{SRC},strong,2025 handelsvorderingen 40 241433 JUMP (was 142907); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_otherrecv_2025,{ENT},2025,546718,,,executed,{SRC},strong,2025 overige ST 41 546718 DROP (was 694826); LT other 291 empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_cash_2025,{ENT},2025,926690,,,executed,{SRC},strong,2025 liquide middelen 54/58 926690 DROP (was 1582721); beleggingen 50/53 empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_prepaid_2025,{ENT},2025,132336,,,executed,{SRC},strong,2025 overlopende 490/1 132336 JUMP (was 50340); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_equity_2025,{ENT},2025,3246857,,,executed,{SRC},strong,2025 eigen vermogen 10/15 3246857 DROP (was 3455002); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_fondsen_2025,{ENT},2025,257683,,,executed,{SRC},strong,2025 fondsen 10 257683 stable; bestemde 13 empty; overgedragen 14 -36816; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_kapsubs_2025,{ENT},2025,3025990,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 3025990 DROP (was 3209228); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_prov_2025,{ENT},2025,4520,,,executed,{SRC},strong,2025 voorzieningen 16 4520 DROP (pensioen 160 4520 was 8394); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_debt_2025,{ENT},2025,3508957,,,executed,{SRC},strong,2025 schulden 17/49 3508957 DROP (was 4040201); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_ltdebt_2025,{ENT},2025,1009368,,,executed,{SRC},strong,2025 LT schulden 17 1009368 DROP (krediet 173 215925 + overige 174 793442); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_stdebt_2025,{ENT},2025,2417967,,,executed,{SRC},strong,2025 ST schulden 42/48 2417967 UP (was 2215450; current portion 83439 / lev 307576 / taxsoc 1764044 / other 262908); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_lev_2025,{ENT},2025,307576,,,executed,{SRC},strong,2025 leveranciers 440/4 307576 JUMP (was 209629); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_taxsoc_2025,{ENT},2025,1764044,,,executed,{SRC},strong,2025 tax/soc 45 1764044 DROP (tax 363068 + bezold 1400976 was 1816060); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_otherst_2025,{ENT},2025,262908,,,executed,{SRC},strong,2025 overige ST 48 262908 JUMP (was 109058); overlopend 492/3 81622 DROP was 728280; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_opbr_2025,{ENT},2025,13378953,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 13378953 DROP (was 13557161); annual envelope; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_omzet_2025,{ENT},2025,458249,,,executed,{SRC},strong,2025 omzet 70 458249 UP (was 438688); 6.9 category/geo empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_subs_2025,{ENT},2025,12807697,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 12807697 UP (731 7232 + 733 12800465); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_subs733_2025,{ENT},2025,12800465,,,executed,{SRC},strong,2025 subsidies 733 12800465 (was 12636833); schenkingen 731 7232; lidgelden 730 empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_andere74_2025,{ENT},2025,102909,,,executed,{SRC},strong,2025 andere 74 102909 DROP (was 406624); nrec 76A 10098 DROP (was 60862); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_diensten_2025,{ENT},2025,1298452,,,executed,{SRC},strong,2025 diensten 61 1298452 (was 1270686); handelsgoederen 60 142095; uitzend 617 70638; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_pers_2025,{ENT},2025,11589623,,,executed,{SRC},strong,2025 pers 62 11589623 / 160.2 VTE DROP (was 11718014 / 163.7); YE 190 was 195 / 206885 uur; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_afschr_2025,{ENT},2025,299421,,,executed,{SRC},strong,2025 afschrijvingen 630 299421 (was 312531); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_expl_2025,{ENT},2025,-23645,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -23645 LOSS (was -2403); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_finopbr_2025,{ENT},2025,29424,,,executed,{SRC},strong,2025 financiele opbrengsten 75 29424 (was 49449; FVA 750 29424); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_finkost_2025,{ENT},2025,30685,,,executed,{SRC},strong,2025 financiele kosten 65 30685 (schulden 30035); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_nrec_2025,{ENT},2025,25339,,,executed,{SRC},strong,2025 nrec 66A 25339 DROP (was 85789); 76A 10098; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_pnl_2025,{ENT},2025,-24907,,,executed,{SRC},strong,2025 verlies 9904 -24907 LOSS (was +11067); tax 67/77 empty; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; uit te keren winst empty); tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_capex_2025,{ENT},2025,179775,,,executed,{SRC},strong,2025 capex IVA 8022 74979 + MVA 8161 45279 + 8162 55037 + 8163 4480 = 179775; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
    f"bud_cwbr_commissaris_2025,{ENT},2025,6516,,,executed,{SRC},strong,2025 commissaris 9505 6516; Achiel Clybouw Andre Clybouw & C Bedrijfsrevisoren BV B00162; tick1527; primary official NBB WVV VOL-VZW 2026-00101211",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
