# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ENT="city_steenokkerzeel"
OCMW="ocmw_steenokkerzeel"
SRC="src_stnok_jr2025_bbc"
TICK=1298
rows = [
    ("bud_stnok_assets_2025", ENT, "2025", 95073091, "J4 assets 95.073091m vs 88.550669m"),
    ("bud_stnok_assets_2024", ENT, "2024", 88550669, "J4 YE2024 assets 88.550669m"),
    ("bud_stnok_cash_2025", ENT, "2025", 8646848, "J4 cash+beleg 8.646848m vs 12.885050m DROP"),
    ("bud_stnok_cash_2024", ENT, "2024", 12885050, "J4 YE2024 cash+beleg 12.885050m"),
    ("bud_stnok_fva_2025", ENT, "2025", 23925192, "J4/T5 FVA 23.925192m (EVA 0 + IGS 18.370 + other 5.549)"),
    ("bud_stnok_eva_2025", ENT, "2025", 0, "T5 EVA 0 on city books; AGB exists (already 1167)"),
    ("bud_stnok_igs_2025", ENT, "2025", 18370187, "T5 IGS 18.370187m vs 8.860016m"),
    ("bud_stnok_igs_reval_2025", ENT, "2025", 9510058, "T5 IGS herwaardering +9.510058m no cash"),
    ("bud_stnok_mva_2025", ENT, "2025", 54147646, "J4/T5 MVA 54.147646m; leasing 0.797829m"),
    ("bud_stnok_leasing_2025", ENT, "2025", 797829, "T5 leasing MVA 0.797829m; aankoop 0.173963m"),
    ("bud_stnok_equity_2025", ENT, "2025", 87059542, "J4 nettoactief 87.059542m vs 75.679116m"),
    ("bud_stnok_cap_subs_2025", ENT, "2025", 5873569, "J4/T5 cap subs 5.873569m"),
    ("bud_stnok_cum_pnl_2025", ENT, "2025", 13778227, "J4/T5 cum PnL 13.778227m"),
    ("bud_stnok_reval_2025", ENT, "2025", 10814961, "J4/T5 herwaardering 10.814961m vs 1.304903m"),
    ("bud_stnok_fin_debt_2025", ENT, "2025", 2491751, "T4 fin debt 2.491751m (LT 1.648686 + ST due 0.843065)"),
    ("bud_stnok_fin_debt_2024", ENT, "2024", 3529609, "T4 YE2024 fin debt 3.529609m"),
    ("bud_stnok_fin_debt_lt_2025", ENT, "2025", 1648686, "T4 LT fin debt 1.648686m"),
    ("bud_stnok_fin_debt_st_2025", ENT, "2025", 843065, "T4 ST due 0.843065m; ST fin 0"),
    ("bud_stnok_new_loans_2025", ENT, "2025", 173963, "T4 new loans 0.173963m leasing; no new bank loans"),
    ("bud_stnok_pension_2025", ENT, "2025", 2587398, "J4 LT pension 2.587398m vs 6.094951m (respo takeback)"),
    ("bud_stnok_expl_2025", ENT, "2025", 1023731, "J2 exploitatiesaldo +1.023731m"),
    ("bud_stnok_expl_ontv_2025", ENT, "2025", 25533422, "J2 expl ontv 25.533422m"),
    ("bud_stnok_expl_uitg_2025", ENT, "2025", 24509691, "J2 expl uitg 24.509691m"),
    ("bud_stnok_city_expl_2025", ENT, "2025", 2192186, "Kengetallen city expl +2.192186m"),
    ("bud_stnok_ocmw_expl_2025", OCMW, "2025", -1168455, "Kengetallen OCMW expl -1.168455m"),
    ("bud_stnok_invest_2025", ENT, "2025", -4391444, "J2 invest -4.391444m vs MJP -6.593m"),
    ("bud_stnok_bbr_2025", ENT, "2025", -4688211, "J2 budgettair resultaat boekjaar -4.688211m"),
    ("bud_stnok_avail_2025", ENT, "2025", 9976574, "J2 beschikbaar BBR 9.976574m"),
    ("bud_stnok_afm_2025", ENT, "2025", -51434, "J2 AFM -0.051434m (TAK26 herbelegging 1.027m)"),
    ("bud_stnok_gecorr_2025", ENT, "2025", 878017, "J2 gecorr AFM +0.878017m"),
    ("bud_stnok_pnl_2025", ENT, "2025", 2032304, "J5 PnL +2.032304m (city +3.460 / OCMW -1.428)"),
    ("bud_stnok_pers_2025", ENT, "2025", 13322470, "J5/T2 bezoldigingen 13.322470m; VTE unpublished"),
    ("bud_stnok_fiscal_2025", ENT, "2025", 14480183, "T2 fiscale 14.480183m (OV 5.929 + APB 6.220)"),
    ("bud_stnok_gemfonds_2025", ENT, "2025", 2586756, "T2 gemeentefonds 2.586756m"),
    ("bud_stnok_politie_2025", ENT, "2025", 2108011, "T2 politiezone 2.108011m; zone-naam unpublished"),
    ("bud_stnok_hvz_2025", ENT, "2025", 1090130, "T2 HVZ/brandweer 1.090130m"),
    ("bud_stnok_agb_werksub_2025", ENT, "2025", 259001, "T2 city werksub aan AGB 0.259001m vs AGB 1167 prijssub 0.244m"),
    ("bud_stnok_ocmw_equity_2025", OCMW, "2025", 38505, "T5 OCMW equity 0.038505m / cum PnL -1.428375m NEG"),
    ("bud_stnok_afl_2025", ENT, "2025", 1211820, "T4/J2 periodieke aflossingen 1.211820m"),
    ("bud_stnok_tussen_2025", ENT, "2025", 1194900, "GR/T5 tussenkomst OCMW 1.194900m"),
]
assert abs((25533422 - 24509691) - 1023731) < 2
assert abs((14851452 + (-4688211)) - 10163241) < 2
assert abs((10163241 - 186667) - 9976574) < 2
assert abs((3460195 + (-1427891)) - 2032304) < 2
assert abs((87059542 + 8013548) - 95073091) < 2
assert abs((5873569 + 13778227 + 10814961 + 56592785) - 87059542) < 2
assert abs((1648686 + 843065) - 2491751) < 2
assert abs((5929277 + 6219541 + 212832 + 2118533) - 14480183) < 3
print("asserts ok")
with open(DATA/"budgets.csv", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    existing = {row.get(fields[0]) for row in reader}
added=0
with open(DATA/"budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    for bid, ent, year, amt, note in rows:
        if bid in existing:
            continue
        w.writerow({"budget_id":bid,"entity_id":ent,"year":year,"amount_eur":amt,"amount_min_eur":"","amount_max_eur":"","basis":"executed","source_id":SRC,"confidence":"strong","notes":note+f"; tick{TICK}; primary BBC"})
        added += 1
print("budgets", added)
