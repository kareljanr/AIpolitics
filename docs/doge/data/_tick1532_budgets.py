#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwov"
SRC = "src_cwov_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwov_assets_2025,{ENT},2025,32814654,,,executed,{SRC},strong,2025 assets 32814654 DROP (was 34372190); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_vaste_2025,{ENT},2025,19094464,,,executed,{SRC},strong,2025 vaste activa 21/28 19094464 DROP (was 19888306); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_mva_2025,{ENT},2025,19037504,,,executed,{SRC},strong,2025 MVA 22/27 19037504 DROP (was 19837240); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_gebouwen_2025,{ENT},2025,15785801,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 15785801 DROP (was 17000777); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_install_2025,{ENT},2025,723189,,,executed,{SRC},strong,2025 installaties 23 723189 UP (was 688409); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_meubilair_2025,{ENT},2025,397095,,,executed,{SRC},strong,2025 meubilair 24 397095 DROP (was 482692); leasing 25 574000; overige 26 13196; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_inb_2025,{ENT},2025,1544223,,,executed,{SRC},strong,2025 in aanbouw 27 1544223 JUMP (was 1048987; aanschaffingen 8166 495236); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_iva_2025,{ENT},2025,6966,,,executed,{SRC},strong,2025 IVA 21 6966 JUMP (was 2740; aanschaffingen 8022 7024; afschr 8072 2798); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_fva_2025,{ENT},2025,49995,,,executed,{SRC},strong,2025 FVA 28 49995 (aandelen 284 500 + borg 285/8 49495); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_current_2025,{ENT},2025,13720190,,,executed,{SRC},strong,2025 vlottende 29/58 13720190 DROP (was 14483884); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_strecv_2025,{ENT},2025,5098013,,,executed,{SRC},strong,2025 ST vorderingen 40/41 5098013 JUMP (was 4244435); LT recv 29 12662; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_handelsrecv_2025,{ENT},2025,3142271,,,executed,{SRC},strong,2025 handelsvorderingen 40 3142271 JUMP (was 1326010); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_otherrecv_2025,{ENT},2025,1955741,,,executed,{SRC},strong,2025 overige ST 41 1955741 DROP (was 2918425); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_beleg_2025,{ENT},2025,558,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 558 (all 51 aandelen; termijn 53 empty); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_cash_2025,{ENT},2025,8405654,,,executed,{SRC},strong,2025 liquide middelen 54/58 8405654 DROP (was 10210384); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_prepaid_2025,{ENT},2025,203304,,,executed,{SRC},strong,2025 overlopende 490/1 203304 JUMP (was 13634; verzekering 128457 + licenties 40551 + reservering 9904 + andere 17538 + intresten 6854); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_equity_2025,{ENT},2025,21806046,,,executed,{SRC},strong,2025 eigen vermogen 10/15 21806046 DROP (was 22422495); fondsen 10 4435640; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_bestemde_2025,{ENT},2025,6098749,,,executed,{SRC},strong,2025 bestemde fondsen 13 6098749; overgedragen 14 3323900 DROP (was 4345114); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_kapsubs_2025,{ENT},2025,7947758,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 7947758 UP (was 7542993; WVV 6.18 VIPA belofte 1094460); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_voorzieningen_2025,{ENT},2025,198386,,,executed,{SRC},strong,2025 voorzieningen 16 198386 DROP (was 455556; 6.7 terug te betalen subsidies 198386); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_debt_2025,{ENT},2025,10810222,,,executed,{SRC},strong,2025 schulden 17/49 10810222 DROP (was 11494138); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_ltdebt_2025,{ENT},2025,440000,,,executed,{SRC},strong,2025 LT schulden 17 440000 DROP (all leasing 172 was 460000; >5y 360000 / 1-5y 80000); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_stdebt_2025,{ENT},2025,9937595,,,executed,{SRC},strong,2025 ST schulden 42/48 9937595 UP (was 9847625; current portion 20000 / lev 1612237 / taxsoc 7813209 / other 492149); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_lev_2025,{ENT},2025,1612237,,,executed,{SRC},strong,2025 leveranciers 440/4 1612237 UP (was 1569173); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_taxsoc_2025,{ENT},2025,7813209,,,executed,{SRC},strong,2025 tax/soc 45 7813209 UP (tax 1086989 + bezold 6726220 was 7708869); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_otherst_2025,{ENT},2025,492149,,,executed,{SRC},strong,2025 overige ST 48 492149 DROP (was 549583); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_accrued_2025,{ENT},2025,432627,,,executed,{SRC},strong,2025 overlopend 492/3 432627 DROP (was 1186514; 6.8 over te dragen subsidies 2026 419737 + giften 11235); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_opbr_2025,{ENT},2025,43872173,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 43872173 UP (was 42837887); annual envelope; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_omzet_2025,{ENT},2025,2041949,,,executed,{SRC},strong,2025 omzet 70 2041949 UP (was 2026597); 6.9 category split empty; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_subs_2025,{ENT},2025,40332909,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 40332909 UP (731 76347 + 732 42207 + 733 40214356; 730 empty); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_subs733_2025,{ENT},2025,40214356,,,executed,{SRC},strong,2025 subsidies 733 40214356 UP (was 39409281); city vs Departement Zorg split unpublished; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_andere74_2025,{ENT},2025,963836,,,executed,{SRC},strong,2025 andere 74 963836 UP (was 953469); nrec 76A 533479 JUMP (7630 194177 + 764/8 339301); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_diensten_2025,{ENT},2025,5212292,,,executed,{SRC},strong,2025 diensten 61 5212292 JUMP (was 4745890); handelsgoederen 60 533116; uitzend 617 164771; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_pers_2025,{ENT},2025,37299480,,,executed,{SRC},strong,2025 pers 62 37299480 / 506.3 VTE DROP (was 36370199 / 511.3; YE 602 was 632 / 686351 uur); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_afschr_2025,{ENT},2025,1517945,,,executed,{SRC},strong,2025 afschrijvingen 630 1517945 (was 1486422); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_nrec66a_2025,{ENT},2025,328855,,,executed,{SRC},strong,2025 nrec 66A 328855 DROP (was 757423; 6630 156045 + 664/7 166022 + 660 6788); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_expl_2025,{ENT},2025,-1217212,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -1217212 LOSS (was -2211649); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_finopbr_2025,{ENT},2025,219836,,,executed,{SRC},strong,2025 financiele opbrengsten 75/76B 219836 DROP (was 435136; vlottend 751 218529); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_finkost_2025,{ENT},2025,23839,,,executed,{SRC},strong,2025 financiele kosten 65/66B 23839 (schulden 650 18250 + andere 5023 + 66B 567); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_pnl_2025,{ENT},2025,-1021215,,,executed,{SRC},strong,2025 verlies 9904 -1021215 LOSS (was -1807234); tax 67/77 empty; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 empty; 791 empty; overgedragen 14 3323900); tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_capex_2025,{ENT},2025,885268,,,executed,{SRC},strong,2025 capex IVA 8022 7024 + MVA 8161 36367 + 8162 306253 + 8163 40388 + 8166 495236 = 885268; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
    f"bud_cwov_commissaris_2025,{ENT},2025,14791,,,executed,{SRC},strong,2025 commissaris 9505 14791; KPMG Bedrijfsrevisoren B00001 via Heyndrickx Wim A01925; tick1532; primary official NBB WVV VOL-VZW 2026-00117344",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
