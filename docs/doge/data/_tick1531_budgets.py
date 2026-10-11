#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "caw_cwlm"
SRC = "src_cwlm_jr2025_nbb"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

rows = [
    f"bud_cwlm_assets_2025,{ENT},2025,17396760,,,executed,{SRC},strong,2025 assets 17396760 DROP (was 17664836); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_vaste_2025,{ENT},2025,10980664,,,executed,{SRC},strong,2025 vaste activa 21/28 10980664 UP (was 10840340); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_mva_2025,{ENT},2025,10709288,,,executed,{SRC},strong,2025 MVA 22/27 10709288 DROP (was 10758711); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_gebouwen_2025,{ENT},2025,10104729,,,executed,{SRC},strong,2025 terreinen/gebouwen 22 10104729 DROP (was 10228936); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_install_2025,{ENT},2025,176529,,,executed,{SRC},strong,2025 installaties 23 176529 UP (was 171569); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_meubilair_2025,{ENT},2025,310207,,,executed,{SRC},strong,2025 meubilair 24 310207 DROP (was 317399); leasing 25 empty; overige 26 empty; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_inb_2025,{ENT},2025,117823,,,executed,{SRC},strong,2025 in aanbouw 27 117823 JUMP (was 40807; aanschaffingen 8166 117823; transfer 8181 40807 to 22); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_iva_2025,{ENT},2025,189762,,,executed,{SRC},strong,2025 IVA 21 189762 JUMP (was empty/0; aanschaffingen 8022 206555; afschr 8072 16793); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_fva_2025,{ENT},2025,81614,,,executed,{SRC},strong,2025 FVA 28 81614 (deelneming 282 6996 + borg 285/8 74618); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_current_2025,{ENT},2025,6416096,,,executed,{SRC},strong,2025 vlottende 29/58 6416096 DROP (was 6824496); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_strecv_2025,{ENT},2025,3174491,,,executed,{SRC},strong,2025 ST vorderingen 40/41 3174491 JUMP (was 1727374); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_handelsrecv_2025,{ENT},2025,1548222,,,executed,{SRC},strong,2025 handelsvorderingen 40 1548222 JUMP (was 802449); LT recv 29 empty; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_otherrecv_2025,{ENT},2025,1626269,,,executed,{SRC},strong,2025 overige ST 41 1626269 JUMP (was 924925); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_beleg_2025,{ENT},2025,426779,,,executed,{SRC},strong,2025 geldbeleggingen 50/53 426779 DROP (was 427011; all 51 aandelen; termijn 53 empty); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_cash_2025,{ENT},2025,2737774,,,executed,{SRC},strong,2025 liquide middelen 54/58 2737774 DROP (was 4502757); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_prepaid_2025,{ENT},2025,77052,,,executed,{SRC},strong,2025 overlopende 490/1 77052 DROP (was 167354; over te dragen 69791 + verkregen 7260); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_equity_2025,{ENT},2025,9082939,,,executed,{SRC},strong,2025 eigen vermogen 10/15 9082939 DROP (was 9313603); fondsen 10 empty; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_bestemde_2025,{ENT},2025,4055448,,,executed,{SRC},strong,2025 bestemde fondsen 13 4055448 DROP (was 4142193); overgedragen 14 -25642; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_kapsubs_2025,{ENT},2025,5053133,,,executed,{SRC},strong,2025 kapitaalsubsidies 15 5053133 DROP (was 5401220; vrijval 348087); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_debt_2025,{ENT},2025,8313821,,,executed,{SRC},strong,2025 schulden 17/49 8313821 DROP (was 8322007); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_ltdebt_2025,{ENT},2025,1330444,,,executed,{SRC},strong,2025 LT schulden 17 1330444 DROP (krediet 173 1155444 + overige 174 175000 was 1644217); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_stdebt_2025,{ENT},2025,6612648,,,executed,{SRC},strong,2025 ST schulden 42/48 6612648 JUMP (was 5408849; current portion 313024 / lev 755253 / taxsoc 3248258 / other 2296113); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_lev_2025,{ENT},2025,755253,,,executed,{SRC},strong,2025 leveranciers 440/4 755253 JUMP (was 571610); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_taxsoc_2025,{ENT},2025,3248258,,,executed,{SRC},strong,2025 tax/soc 45 3248258 DROP (tax 596736 + bezold 2651522 was 3357225); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_otherst_2025,{ENT},2025,2296113,,,executed,{SRC},strong,2025 overige ST 48 2296113 JUMP (was 1172644); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_accrued_2025,{ENT},2025,370729,,,executed,{SRC},strong,2025 overlopend 492/3 370729 DROP (was 1268941; 6.8 over te dragen opbrengsten projecten 370728); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_opbr_2025,{ENT},2025,25346747,,,executed,{SRC},strong,2025 bedrijfsopbrengsten 70/76A 25346747 UP (was 25287300); annual envelope; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_omzet_2025,{ENT},2025,2047768,,,executed,{SRC},strong,2025 omzet 70 2047768 DROP (was 2068238); 6.9 category split empty; jaarverslag verblijf clienten vergelijkbaar; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_subs_2025,{ENT},2025,23037493,,,executed,{SRC},strong,2025 lidgeld/subsidies 73 23037493 UP (730 24162 + 733 23013331; 731/732 empty); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_subs733_2025,{ENT},2025,23013331,,,executed,{SRC},strong,2025 subsidies 733 23013331 UP (was 22931613); city vs Departement Zorg split unpublished; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_andere74_2025,{ENT},2025,139490,,,executed,{SRC},strong,2025 andere 74 139490 DROP (was 161303); nrec 76A 121996 UP (764/8); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_diensten_2025,{ENT},2025,3428070,,,executed,{SRC},strong,2025 diensten 61 3428070 JUMP (was 3022670; index + ingehuurd boekhouding/ICT/infra + onderhoud); handelsgoederen 60 902348; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_pers_2025,{ENT},2025,20148522,,,executed,{SRC},strong,2025 pers 62 20148522 / 271.8 VTE DROP (was 20288075 / 276; YE 333 was 343 / 367825 uur); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_afschr_2025,{ENT},2025,818676,,,executed,{SRC},strong,2025 afschrijvingen 630 818676 (was 788576); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_nrec66a_2025,{ENT},2025,30650,,,executed,{SRC},strong,2025 nrec 66A 30650 DROP (was 147232; all 664/7); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_expl_2025,{ENT},2025,80999,,,executed,{SRC},strong,2025 bedrijfswinst 9901 80999 UP (was 13250); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_finopbr_2025,{ENT},2025,78438,,,executed,{SRC},strong,2025 financiele opbrengsten 75 78438 DROP (was 163177; vlottend 751 76600); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_finkost_2025,{ENT},2025,40914,,,executed,{SRC},strong,2025 financiele kosten 65 40914 (schulden 650 37005 + andere 3909); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_pnl_2025,{ENT},2025,117423,,,executed,{SRC},strong,2025 winst 9904 117423 DROP (was 129324); tax 67/77 1100; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_div_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 dividend 0 (VZW; 691 empty; onttrekking 791 86745; overgedragen 14 -25642); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_capex_2025,{ENT},2025,959014,,,executed,{SRC},strong,2025 capex IVA 8022 206555 + MVA 8161 472204 + 8162 48253 + 8163 114179 + 8166 117823 = 959014; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_commissaris_2025,{ENT},2025,13950,,,executed,{SRC},strong,2025 commissaris 9505 13950; Foederer Bedrijfsrevisoren B00466 via Robbeets Christophe A02680; tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
    f"bud_cwlm_voorzieningen_2025,{ENT},2025,0,,,executed,{SRC},strong,2025 voorzieningen 16 empty (was 29226 pensioenen; 635/9 -29226); tick1531; primary official NBB WVV VOL-VZW 2026-00099651",
]
for r in rows:
    n = len(next(csv.reader(io.StringIO(r))))
    if n != 10:
        raise SystemExit(f"bad ncols {n}: {r[:80]}")
    if any("," in f for f in next(csv.reader(io.StringIO(r)))):
        raise SystemExit(f"comma in field: {r[:80]}")
append_lf(DATA / "budgets.csv", rows)
print(f"budgets +{len(rows)}")
