#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import csv, io
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "wm_wpzn"
SRC = "src_wpzn_jr2025_nbb"
BUDGETS = [
    ("bud_wpzn_assets_2025", "2025", "162911198", "2025 assets 162911198 UP (was 157704493); tick1485; primary official NBB WVV VOL-inb 2026-00145529"),
    ("bud_wpzn_current_2025", "2025", "7790854", "2025 vlottend 7790854 DROP (was 8189860); tick1485; primary official NBB WVV"),
    ("bud_wpzn_cash_2025", "2025", "4801403", "2025 liquide middelen 4801403 JUMP (was 3516094); tick1485; primary official NBB WVV"),
    ("bud_wpzn_strecv_2025", "2025", "1221489", "2025 ST vorderingen 1221489 JUMP (was 874270); tick1485; primary official NBB WVV"),
    ("bud_wpzn_trade_2025", "2025", "1022428", "2025 handelsvorderingen 1022428 (was 699158); tick1485; primary official NBB WVV"),
    ("bud_wpzn_othrecv_2025", "2025", "199061", "2025 overige ST vorderingen 199061 (was 175112); tick1485; primary official NBB WVV"),
    ("bud_wpzn_ltrecv_2025", "2025", "311865", "2025 LT vorderingen 311865 (was 304799); tick1485; primary official NBB WVV"),
    ("bud_wpzn_voorraden_2025", "2025", "648189", "2025 voorraden 648189 DROP (was 2657485; onroerend verkoop 648189); tick1485; primary official NBB WVV"),
    ("bud_wpzn_prepaid_2025", "2025", "807908", "2025 overlopend actief 807908 (was 837212); tick1485; primary official NBB WVV"),
    ("bud_wpzn_fixed_2025", "2025", "155120344", "2025 vaste activa 155120344 (was 149514633); tick1485; primary official NBB WVV"),
    ("bud_wpzn_iva_2025", "2025", "0", "2025 IVA 0 (was 0); tick1485; primary official NBB WVV"),
    ("bud_wpzn_mva_2025", "2025", "155083344", "2025 MVA 155083344 (was 149507633; terreinen/gebouwen 137434487 installaties 3703 meubilair 134177 leasing 2114 overige 764970 in aanbouw 16743893); tick1485; primary official NBB WVV"),
    ("bud_wpzn_fva_2025", "2025", "37000", "2025 FVA 37000 (was 7000); tick1485; primary official NBB WVV"),
    ("bud_wpzn_equity_2025", "2025", "47335265", "2025 eigen vermogen 47335265 (was 47111874); tick1485; primary official NBB WVV"),
    ("bud_wpzn_inbreng_2025", "2025", "29912", "2025 inbreng 29912 onbeschikbaar; tick1485; primary official NBB WVV"),
    ("bud_wpzn_reserves_2025", "2025", "18258912", "2025 reserves 18258912 (was 18590401); tick1485; primary official NBB WVV"),
    ("bud_wpzn_overgedr_2025", "2025", "12361055", "2025 overgedragen winst 12361055 (was 11288102); tick1485; primary official NBB WVV"),
    ("bud_wpzn_kapsubs_2025", "2025", "16685386", "2025 kapitaalsubsidies 16685386 DROP (was 17203459); tick1485; primary official NBB WVV"),
    ("bud_wpzn_voorz_2025", "2025", "7539720", "2025 voorzieningen+uitgestelde belasting 7539720 (herstel 6245938; uitgestelde 1293782); tick1485; primary official NBB WVV"),
    ("bud_wpzn_debt_2025", "2025", "108036213", "2025 schulden 108036213 JUMP (was 103008688); tick1485; primary official NBB WVV"),
    ("bud_wpzn_ltdebt_2025", "2025", "99106429", "2025 LT schulden 99106429 (was 95273299; fin krediet 84984146); tick1485; primary official NBB WVV"),
    ("bud_wpzn_stdebt_2025", "2025", "8103945", "2025 ST schulden 8103945 (42 4171934 + leveranciers 2216110); tick1485; primary official NBB WVV"),
    ("bud_wpzn_lev_2025", "2025", "2216110", "2025 leveranciers 2216110 JUMP (was 1262631); tick1485; primary official NBB WVV"),
    ("bud_wpzn_bezold_2025", "2025", "349264", "2025 bezoldigingen-schulden 349264 (was 315154); tick1485; primary official NBB WVV"),
    ("bud_wpzn_taxpay_2025", "2025", "1146937", "2025 belastingschulden 1146937 (was 1179216); tick1485; primary official NBB WVV"),
    ("bud_wpzn_deferred_2025", "2025", "825839", "2025 overlopend passief 825839 (was 820219); tick1485; primary official NBB WVV"),
    ("bud_wpzn_omzet_2025", "2025", "15271056", "2025 omzet 70 15271056 JUMP (was 11209053; 6.10 split unpublished); tick1485; primary official NBB WVV"),
    ("bud_wpzn_diensten_2025", "2025", "6315121", "2025 diensten 61 6315121 JUMP (was 5633044); tick1485; primary official NBB WVV"),
    ("bud_wpzn_pers_2025", "2025", "3128980", "2025 pers 62 3128980; 37.3 VTE vs 35.2; 56794 uur; YE 41; tick1485; primary official NBB WVV"),
    ("bud_wpzn_afschr_2025", "2025", "4576558", "2025 afschrijvingen 4576558; tick1485; primary official NBB WVV"),
    ("bud_wpzn_expl_2025", "2025", "1180063", "2025 bedrijfswinst 1180063 (was 890026); tick1485; primary official NBB WVV"),
    ("bud_wpzn_finopbr_2025", "2025", "1637581", "2025 financiele opbrengsten 1637581 (interestsubs 1060007); tick1485; primary official NBB WVV"),
    ("bud_wpzn_finkost_2025", "2025", "2028728", "2025 financiele kosten 2028728; tick1485; primary official NBB WVV"),
    ("bud_wpzn_pnl_2025", "2025", "741465", "2025 PnL 741465 JUMP (was 405723); tick1485; primary official NBB WVV"),
    ("bud_wpzn_div_2025", "2025", "0", "2025 dividend 0; tick1485; primary official NBB WVV"),
    ("bud_wpzn_capex_2025", "2025", "10461618", "2025 capex MVA aanschaf 10461618 (terreinen 4894613 installaties 1097 meubilair 6275 in aanbouw 5559633); tick1485; primary official NBB WVV"),
    ("bud_wpzn_in_aanbouw_2025", "2025", "16743893", "2025 activa in aanbouw 16743893 JUMP (was 11191665); tick1485; primary official NBB WVV"),
    ("bud_wpzn_krediet_2025", "2025", "84984146", "2025 LT kredietinstellingen 84984146 (was 81647588); tick1485; primary official NBB WVV"),
    ("bud_wpzn_terreinen_2025", "2025", "137434487", "2025 terreinen en gebouwen 137434487 (was 137359639); tick1485; primary official NBB WVV"),
    ("bud_wpzn_commissaris_2025", "2025", "19148", "2025 commissaris fee 19148 Moore Audit BV + belastingadvies 6779; tick1485; primary official NBB WVV"),
    ("bud_wpzn_tax_2025", "2025", "91662", "2025 belastingen op het resultaat 91662; tick1485; primary official NBB WVV"),
    ("bud_wpzn_interestsubs_2025", "2025", "1060007", "2025 interestsubsidies 9126 1060007 (was 865768); tick1485; primary official NBB WVV 6.11"),
    ("bud_wpzn_explsubs_2025", "2025", "1244041", "2025 exploitatiesubsidies 740 1244041 (was 1143714); tick1485; primary official NBB WVV 6.10"),
    ("bud_wpzn_geldbeleg_2025", "2025", "0", "2025 geldbeleggingen 50/53 empty; tick1485; primary official NBB WVV"),
    ("bud_wpzn_bestuurders_2025", "2025", "92796", "2025 bestuurders 9503 92796; tick1485; primary official NBB WVV"),
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
