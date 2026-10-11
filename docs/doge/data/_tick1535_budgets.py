#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwnw"
SRC = "src_cwnw_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwnw_assets_2025,{ENT},2025,15981042,,,executed,{SRC},strong,2025 assets 15981042 UP (was 14872726); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_vaste_2025,{ENT},2025,12354881,,,executed,{SRC},strong,2025 vaste activa 21/28 12354881 UP (was 11822166); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_mva_2025,{ENT},2025,12336096,,,executed,{SRC},strong,2025 MVA 22/27 12336096 UP (was 11805083); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_gebouwen_2025,{ENT},2025,10384374,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 10384374 UP (was 9653501; 8161 1303169); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_install_2025,{ENT},2025,1655284,,,executed,{SRC},strong,2025 installaties 23 1655284 DROP (was 1758037); meubilair 24 219236 DROP (was 361735); overige 26 6840 DROP; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_inb_2025,{ENT},2025,70362,,,executed,{SRC},strong,2025 in aanbouw 27 70362 UP (was 22554; aanschaffingen 8166 70362; overdracht 8176 22554); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 21 empty; FVA 28 18785 UP (was 17083; 284 808 + 285/8 17977); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_current_2025,{ENT},2025,3626161,,,executed,{SRC},strong,2025 vlottende 29/58 3626161 UP (was 3050560); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_strecv_2025,{ENT},2025,1185205,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1185205 UP (was 712219); LT recv 29 860158 JUMP (was 55000); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_handelsrecv_2025,{ENT},2025,177791,,,executed,{SRC},strong,2025 handelsvorderingen 40 177791 UP (was 147198); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_otherrecv_2025,{ENT},2025,1007414,,,executed,{SRC},strong,2025 overige ST 41 1007414 JUMP (was 565021); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_beleg_2025,{ENT},2025,1022346,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 1022346 JUMP (was 348292; 51 empty 52 empty 53 empty; 8689 overige 1022346); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_cash_2025,{ENT},2025,430376,,,executed,{SRC},strong,2025 liquide middelen 54/58 430376 DROP (was 1924544); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_prepaid_2025,{ENT},2025,128076,,,executed,{SRC},strong,2025 overlopende 490/1 128076 JUMP (was 10505; 490 128076); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_equity_2025,{ENT},2025,8328831,,,executed,{SRC},strong,2025 eigen vermogen 10/15 8328831 DROP (was 10468614); fondsen 10 1685845; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_bestemde_2025,{ENT},2025,2490437,,,executed,{SRC},strong,2025 bestemde fondsen 13 2490437 DROP (was 4353152); overgedragen 14 empty (was 29313); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_kapsubs_2025,{ENT},2025,4152549,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 4152549 DROP (was 4400304); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_voorzieningen_2025,{ENT},2025,1308026,,,executed,{SRC},strong,2025 voorzieningen 16 1308026 JUMP (was empty; 164/5 1308026; 6620 nrec toevoeging 1308026); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_debt_2025,{ENT},2025,6344185,,,executed,{SRC},strong,2025 schulden 17/49 6344185 JUMP (was 4404112); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_ltdebt_2025,{ENT},2025,1572365,,,executed,{SRC},strong,2025 LT schulden 17 1572365 JUMP (bank 173 1572365 was 960114); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_stdebt_2025,{ENT},2025,3531542,,,executed,{SRC},strong,2025 ST schulden 42/48 3531542 UP (was 3209183; current 57260 / lev 480402 / taxsoc 2658289 / other 335591); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_lev_2025,{ENT},2025,480402,,,executed,{SRC},strong,2025 leveranciers 440/4 480402 JUMP (was 178594); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_taxsoc_2025,{ENT},2025,2658289,,,executed,{SRC},strong,2025 tax/soc 45 2658289 (tax 494711 + bezold 2163578 was 2416236); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_accrued_2025,{ENT},2025,1240278,,,executed,{SRC},strong,2025 overlopend 492/3 1240278 JUMP (was 234815; 493 1240278); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_opbr_2025,{ENT},2025,17987315,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 17987315 UP (was 17076016); annual envelope; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_omzet_2025,{ENT},2025,431305,,,executed,{SRC},strong,2025 omzet 70 431305 DROP (was 502633); 6.9 category split empty; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_subs_2025,{ENT},2025,16119120,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 16119120 DROP (731 40823 + 733 16078297; 730 empty 732 empty); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_subs733_2025,{ENT},2025,16078297,,,executed,{SRC},strong,2025 subsidies 733 16078297 DROP (was 16255531); city vs Departement Zorg split unpublished; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_andere74_2025,{ENT},2025,835962,,,executed,{SRC},strong,2025 andere 74 835962 JUMP (was 228059); nrec 76A 600928 JUMP (7630 524540 + 764/8 76388); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_diensten_2025,{ENT},2025,1946834,,,executed,{SRC},strong,2025 diensten 61 1946834 UP (was 1661275); handelsgoederen 60 168066 DROP (was 189026); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_pers_2025,{ENT},2025,14781014,,,executed,{SRC},strong,2025 pers 62 14781014 / 206.2 VTE DROP (was 14656927 / 209.8; YE 9086 192 was 243 / 271483 uur; social 105 YE 216 / 191.8 VTE); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_afschr_2025,{ENT},2025,833630,,,executed,{SRC},strong,2025 afschrijvingen 630 833630 (was 795858); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_nrec76a_2025,{ENT},2025,600928,,,executed,{SRC},strong,2025 nrec 76A 600928 JUMP (was 43886; 7630 meerwaarden 524540 + 764/8 76388); 66A 1680781 JUMP (6620 1308026 + 664/7 372755); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_expl_2025,{ENT},2025,-1890904,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -1890904 LOSS (was -923739); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_finopbr_2025,{ENT},2025,47410,,,executed,{SRC},strong,2025 financiele opbrengsten 75/76B 47410 DROP (was 107797; 751 47386 + 752/9 24); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_finkost_2025,{ENT},2025,48534,,,executed,{SRC},strong,2025 financiele kosten 65/66B 48534 (schulden 650 46964 + andere 1570); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_pnl_2025,{ENT},2025,-1892028,,,executed,{SRC},strong,2025 verlies 9904 -1892028 LOSS (was -844108); tax 67/77 empty; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 empty; 791 1862714 onttrekking; 14 empty; 14P 29314); tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_capex_2025,{ENT},2025,1427657,,,executed,{SRC},strong,2025 capex IVA 0 + MVA 8161 1303169 + 8162 54126 + 8163 empty + 8165 empty + 8166 70362 = 1427657; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
    f"bud_cwnw_commissaris_2025,{ENT},2025,7657,,,executed,{SRC},strong,2025 commissaris 9505 7657; Callens Vandelanotte NV B00083 0433608707; tick1535; primary official NBB WVV VOL-VZW 2026-00103625",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
