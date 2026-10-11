#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwhv"
SRC = "src_cwhv_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwhv_assets_2025,{ENT},2025,13485378,,,executed,{SRC},strong,2025 assets 13485378 DROP (was 13937116); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_vaste_2025,{ENT},2025,6038167,,,executed,{SRC},strong,2025 vaste activa 21/28 6038167 UP (was 5648884); IVA 21 net 0; FVA 28 14538; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_mva_2025,{ENT},2025,6023629,,,executed,{SRC},strong,2025 MVA 22/27 6023629 UP (was 5630592); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_gebouwen_2025,{ENT},2025,4610447,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 4610447 DROP (was 4790052); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_install_2025,{ENT},2025,616568,,,executed,{SRC},strong,2025 installaties 23 616568 DROP (was 693542); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_meubilair_2025,{ENT},2025,114892,,,executed,{SRC},strong,2025 meubilair 24 114892 DROP (was 142020); leasing 25 empty; overige 26 empty; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_inb_2025,{ENT},2025,681722,,,executed,{SRC},strong,2025 in aanbouw 27 681722 JUMP (was 4978; aanschaffingen 8166 676744); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 21 net 0 (aanschaffingen 8021 67018 fully depreciated 8071 67018); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_fva_2025,{ENT},2025,14538,,,executed,{SRC},strong,2025 FVA 28 14538 DROP (aandelen 284 558 + borg 285/8 13980); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_current_2025,{ENT},2025,7447211,,,executed,{SRC},strong,2025 vlottende 29/58 7447211 DROP (was 8288232); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_voorraden_2025,{ENT},2025,5656,,,executed,{SRC},strong,2025 voorraden 30/36 5656 (handelsgoederen 34); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_strecv_2025,{ENT},2025,3471383,,,executed,{SRC},strong,2025 ST vorderingen 40/41 3471383 (trade 15755 + other 3455628); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_handelsrecv_2025,{ENT},2025,15755,,,executed,{SRC},strong,2025 handelsvorderingen 40 15755 UP (was 14427); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_otherrecv_2025,{ENT},2025,3455628,,,executed,{SRC},strong,2025 overige ST 41 3455628 DROP (was 3598309); LT other 291 empty; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_beleg_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 empty; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_cash_2025,{ENT},2025,3955937,,,executed,{SRC},strong,2025 liquide middelen 54/58 3955937 DROP (was 4591722); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_prepaid_2025,{ENT},2025,14235,,,executed,{SRC},strong,2025 overlopende 490/1 14235 DROP (was 78709); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_equity_2025,{ENT},2025,10876596,,,executed,{SRC},strong,2025 eigen vermogen 10/15 10876596 DROP (was 11120580); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_fondsen_2025,{ENT},2025,350045,,,executed,{SRC},strong,2025 fondsen 10 350045 stable; bestemde 13 4863524 stable; overgedragen 14 -14873; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_bestemde_2025,{ENT},2025,4863524,,,executed,{SRC},strong,2025 bestemde fondsen 13 4863524 stable; 691 empty this year; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_kapsubs_2025,{ENT},2025,5677900,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 5677900 UP (was 4868332); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_debt_2025,{ENT},2025,2608782,,,executed,{SRC},strong,2025 schulden 17/49 2608782 DROP (was 2816536); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_ltdebt_2025,{ENT},2025,297492,,,executed,{SRC},strong,2025 LT schulden 17 297492 DROP (krediet 173 297492 was 357336); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_stdebt_2025,{ENT},2025,2287048,,,executed,{SRC},strong,2025 ST schulden 42/48 2287048 UP (was 1950037; current portion 59844 / lev 222683 / taxsoc 1999329 / other 5192); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_lev_2025,{ENT},2025,222683,,,executed,{SRC},strong,2025 leveranciers 440/4 222683 DROP (was 273034); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_taxsoc_2025,{ENT},2025,1999329,,,executed,{SRC},strong,2025 tax/soc 45 1999329 JUMP (tax 405539 + bezold 1593790 was 1617273); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_otherst_2025,{ENT},2025,5192,,,executed,{SRC},strong,2025 overige ST 48 5192 UP (was 1445); overlopend 492/3 24242 DROP was 509163; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_opbr_2025,{ENT},2025,12971653,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 12971653 UP (was 12750454); annual envelope; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_omzet_2025,{ENT},2025,75857,,,executed,{SRC},strong,2025 omzet 70 75857 UP (was 75385); 6.9 Verkopen Sociale Winkel; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_subs_2025,{ENT},2025,12731598,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 12731598 UP (all 733 12731598; 730/731/732 empty); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_subs733_2025,{ENT},2025,12731598,,,executed,{SRC},strong,2025 subsidies 733 12731598 UP (was 12089860); city vs Departement Zorg split unpublished; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_andere74_2025,{ENT},2025,143808,,,executed,{SRC},strong,2025 andere 74 143808 DROP (was 574501); nrec 76A 20390 UP (was 10708); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_diensten_2025,{ENT},2025,1726588,,,executed,{SRC},strong,2025 diensten 61 1726588 JUMP (was 1403235); handelsgoederen 60 70130; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_pers_2025,{ENT},2025,11730941,,,executed,{SRC},strong,2025 pers 62 11730941 / 159.2 VTE JUMP (was 10504680 / 141.8; YE 195 was 181 / 234084 uur); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_afschr_2025,{ENT},2025,401772,,,executed,{SRC},strong,2025 afschrijvingen 630 401772 (was 381469); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_nrec66a_2025,{ENT},2025,47816,,,executed,{SRC},strong,2025 nrec 66A 47816 JUMP (was empty); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_expl_2025,{ENT},2025,-1136898,,,executed,{SRC},strong,2025 bedrijfsverlies 9901 -1136898 LOSS (was +325869); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_finopbr_2025,{ENT},2025,96345,,,executed,{SRC},strong,2025 financiele opbrengsten 75 96345 (was 154950; vlottend 751 95573); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_finkost_2025,{ENT},2025,16445,,,executed,{SRC},strong,2025 financiele kosten 65/66B 16445 (rec 13945 + nrec 66B 2500); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_pnl_2025,{ENT},2025,-1053552,,,executed,{SRC},strong,2025 verlies 9904 -1053552 LOSS (was +466761); tax 67/77 -3446 regularisering; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 empty; overgedragen 14 -14873); tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_capex_2025,{ENT},2025,794809,,,executed,{SRC},strong,2025 capex IVA 8021 67018 + MVA 8161 33430 + 8162 17617 + 8166 676744 = 794809; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
    f"bud_cwhv_commissaris_2025,{ENT},2025,9010,,,executed,{SRC},strong,2025 commissaris 9505 9010; BDO Bedrijfsrevisoren BV B00023 via Lenaerts David A02125; tick1529; primary official NBB WVV VOL-VZW 2026-00124483",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
