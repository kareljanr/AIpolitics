#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwzw"
SRC = "src_cwzw_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwzw_assets_2025,{ENT},2025,14138245,,,executed,{SRC},strong,2025 assets 14138245 UP (was 13353780); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_vaste_2025,{ENT},2025,9533082,,,executed,{SRC},strong,2025 vaste activa 21/28 9533082 DROP (was 10012071); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_mva_2025,{ENT},2025,9533082,,,executed,{SRC},strong,2025 MVA 22/27 9533082 DROP (was 10012071); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_gebouwen_2025,{ENT},2025,9047340,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 9047340 UP (was 7441448; 8181 overboeking 2236348); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_install_2025,{ENT},2025,19397,,,executed,{SRC},strong,2025 installaties 23 19397 UP (was 18544); meubilair 24 375548 UP (was 280431); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_inb_2025,{ENT},2025,90797,,,executed,{SRC},strong,2025 in aanbouw 27 90797 DROP (was 2271648; aanschaffingen 8166 347386; overboeking 8186 -2359595); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_iva_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 IVA 21 empty; FVA 28 empty; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_current_2025,{ENT},2025,4605163,,,executed,{SRC},strong,2025 vlottende 29/58 4605163 UP (was 3341709); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_strecv_2025,{ENT},2025,1970490,,,executed,{SRC},strong,2025 ST vorderingen 40/41 1970490 JUMP (was 830554); LT recv 29 empty; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_handelsrecv_2025,{ENT},2025,341596,,,executed,{SRC},strong,2025 handelsvorderingen 40 341596 UP (was 289367); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_otherrecv_2025,{ENT},2025,1628894,,,executed,{SRC},strong,2025 overige ST 41 1628894 JUMP (was 541187); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_beleg_2025,{ENT},2025,565797,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 565797 DROP (was 1400404; 51 empty 52 empty 53 empty; 8689 overige 565797); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_cash_2025,{ENT},2025,2068876,,,executed,{SRC},strong,2025 liquide middelen 54/58 2068876 JUMP (was 1110751); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_prepaid_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 overlopende 490/1 empty; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_equity_2025,{ENT},2025,11169738,,,executed,{SRC},strong,2025 eigen vermogen 10/15 11169738 UP (was 10103494); fondsen 10 50000; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_bestemde_2025,{ENT},2025,3956448,,,executed,{SRC},strong,2025 bestemde fondsen 13 3956448 UP (was 3555134); overgedragen 14 39933; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_kapsubs_2025,{ENT},2025,7123357,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 7123357 UP (was 6458427); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_voorzieningen_2025,{ENT},2025,380000,,,executed,{SRC},strong,2025 voorzieningen 16 380000 DROP (was 428000; 164/5 inhaalwerk 380000); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_debt_2025,{ENT},2025,2588507,,,executed,{SRC},strong,2025 schulden 17/49 2588507 DROP (was 2822286); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_ltdebt_2025,{ENT},2025,370670,,,executed,{SRC},strong,2025 LT schulden 17 370670 DROP (bank 173 370670; 174 empty was 10200); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_stdebt_2025,{ENT},2025,1900183,,,executed,{SRC},strong,2025 ST schulden 42/48 1900183 DROP (was 2034476; current 88812 / lev 177588 / taxsoc 1633783 / other empty); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_lev_2025,{ENT},2025,177588,,,executed,{SRC},strong,2025 leveranciers 440/4 177588 DROP (was 307113); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_taxsoc_2025,{ENT},2025,1633783,,,executed,{SRC},strong,2025 tax/soc 45 1633783 (tax 279034 + bezold 1354749 was 1357197); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_accrued_2025,{ENT},2025,317654,,,executed,{SRC},strong,2025 overlopend 492/3 317654 DROP (was 328328); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_opbr_2025,{ENT},2025,12009580,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 12009580 UP (was 10974583); annual envelope; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_omzet_2025,{ENT},2025,626259,,,executed,{SRC},strong,2025 omzet 70 626259 UP (was 510844); 6.9 category split empty; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_subs_2025,{ENT},2025,10629255,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 10629255 UP (731 16694 + 733 10612561; 730 empty 732 empty); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_subs733_2025,{ENT},2025,10612561,,,executed,{SRC},strong,2025 subsidies 733 10612561 UP (was 10231908); city vs Departement Zorg split unpublished; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_andere74_2025,{ENT},2025,277277,,,executed,{SRC},strong,2025 andere 74 277277 UP (was 193834); nrec 76A 476789 JUMP (7630 476789); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_diensten_2025,{ENT},2025,1259008,,,executed,{SRC},strong,2025 diensten 61 1259008 UP (was 1076102); handelsgoederen 60 230024 JUMP (was 62924); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_pers_2025,{ENT},2025,9302213,,,executed,{SRC},strong,2025 pers 62 9302213 / 125 VTE UP (was 8943446 / 122; YE 147 was 145 / 184075 uur); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_afschr_2025,{ENT},2025,589940,,,executed,{SRC},strong,2025 afschrijvingen 630 589940 (was 502627); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_nrec76a_2025,{ENT},2025,476789,,,executed,{SRC},strong,2025 nrec 76A 476789 JUMP (was 16771; 7630 meerwaarden 476789); 66A 170345 (6630 169689 + 664/7 656); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_expl_2025,{ENT},2025,401199,,,executed,{SRC},strong,2025 bedrijfswinst 9901 401199 PROFIT (was 243314); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_finopbr_2025,{ENT},2025,13837,,,executed,{SRC},strong,2025 financiele opbrengsten 75/76B 13837 DROP (was 49931; FVA 750 13837); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_finkost_2025,{ENT},2025,13722,,,executed,{SRC},strong,2025 financiele kosten 65/66B 13722 (schulden 650 10490 + andere 3232); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_pnl_2025,{ENT},2025,401314,,,executed,{SRC},strong,2025 winst 9904 401314 PROFIT (was 276946); tax 67/77 empty; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 563469 toevoeging; 791 162155 onttrekking; overgedragen 14 39933); tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_capex_2025,{ENT},2025,478865,,,executed,{SRC},strong,2025 capex IVA 0 + MVA 8161 42591 + 8162 10003 + 8163 78885 + 8166 347386 = 478865; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
    f"bud_cwzw_commissaris_2025,{ENT},2025,6655,,,executed,{SRC},strong,2025 commissaris 9505 6655; MOORE AUDIT BV B00212 0453925059 via Vandenabeele Liesbet A02306; tick1534; primary official NBB WVV VOL-VZW 2026-00069501",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
