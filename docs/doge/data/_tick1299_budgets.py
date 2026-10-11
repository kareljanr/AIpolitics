# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ENT="agb_kortenaken"
SRC="src_agbktn_jr2025_bbc"
TICK=1299
rows = [
    ("bud_agbktn_assets_2025", ENT, "2025", 3479256, "J4 assets 3.479256m vs 3.503923m"),
    ("bud_agbktn_assets_2024", ENT, "2024", 3503923, "J4 YE2024 assets 3.503923m"),
    ("bud_agbktn_cash_2025", ENT, "2025", 103630, "J4 cash+beleg 0.103630m JUMP vs 0.069293m"),
    ("bud_agbktn_cash_2024", ENT, "2024", 69293, "J4 YE2024 cash+beleg 0.069293m"),
    ("bud_agbktn_fva_2025", ENT, "2025", 0, "T5 FVA 0; EVA 0 + IGS 0"),
    ("bud_agbktn_mva_2025", ENT, "2025", 3287804, "J4/T5 MVA 3.287804m; leasing 3.216363m"),
    ("bud_agbktn_leasing_2025", ENT, "2025", 3216363, "T5 leasing MVA 3.216363m (sporthal De Vruen)"),
    ("bud_agbktn_iva_2025", ENT, "2025", 1163, "J4/T5 IVA 0.001163m"),
    ("bud_agbktn_equity_2025", ENT, "2025", 103184, "J4 nettoactief 0.103184m vs 0.097754m"),
    ("bud_agbktn_cum_pnl_2025", ENT, "2025", 78184, "J4/T5 cum PnL 0.078184m (year retained 0.005431m)"),
    ("bud_agbktn_other_eq_2025", ENT, "2025", 25000, "J4 overig nettoactief 0.025000m"),
    ("bud_agbktn_fin_debt_2025", ENT, "2025", 3280771, "T4 fin debt 3.280771m (LT 3.233 + ST due 0.047)"),
    ("bud_agbktn_fin_debt_2024", ENT, "2024", 3310891, "T4 YE2024 fin debt 3.310891m"),
    ("bud_agbktn_fin_debt_lt_2025", ENT, "2025", 3233422, "T4/J4 LT fin debt 3.233422m"),
    ("bud_agbktn_fin_debt_st_2025", ENT, "2025", 47348, "T4/J4 ST due 0.047348m; ST fin 0"),
    ("bud_agbktn_new_loans_2025", ENT, "2025", 16500, "T4 new loans 0.016500m renteloze stadslening; no bank"),
    ("bud_agbktn_pension_2025", ENT, "2025", 0, "J4 no pension voorziening; 0"),
    ("bud_agbktn_expl_2025", ENT, "2025", 55792, "J2 exploitatiesaldo +0.055792m"),
    ("bud_agbktn_expl_ontv_2025", ENT, "2025", 193795, "J2 expl ontv 0.193795m"),
    ("bud_agbktn_expl_uitg_2025", ENT, "2025", 138003, "J2 expl uitg 0.138003m"),
    ("bud_agbktn_invest_2025", ENT, "2025", -16500, "J2 invest -0.016500m (spinningfietsen)"),
    ("bud_agbktn_bbr_2025", ENT, "2025", 9171, "J2 budgettair resultaat boekjaar +0.009171m"),
    ("bud_agbktn_avail_2025", ENT, "2025", 94988, "J2 beschikbaar BBR 0.094988m"),
    ("bud_agbktn_afm_2025", ENT, "2025", 9171, "J2 AFM +0.009171m"),
    ("bud_agbktn_gecorr_2025", ENT, "2025", -209080, "J2 gecorr AFM -0.209080m (aangewezen 0.264871m)"),
    ("bud_agbktn_pnl_2025", ENT, "2025", 15431, "J5 PnL +0.015431m; dividend 0.010m / retained 0.005431m"),
    ("bud_agbktn_pers_2025", ENT, "2025", 0, "J5 no bezoldigingen; pers 0 on AGB books"),
    ("bud_agbktn_prijssub_2025", ENT, "2025", 157062, "T2/D2 prijssub 0.157062m (city 0.156547 + Bekkevoort 0.000515)"),
    ("bud_agbktn_werking_2025", ENT, "2025", 190398, "J5/T2 ontvangsten uit de werking 0.190398m"),
    ("bud_agbktn_client_2025", ENT, "2025", 22410, "D2 klantentarieven 0.022410m excl btw"),
    ("bud_agbktn_afl_2025", ENT, "2025", 46621, "T4/J2 periodieke aflossingen 0.046621m (canon 0.036550 + city 0.010071)"),
    ("bud_agbktn_dividend_2025", ENT, "2025", 10000, "J5/RVB winstuitkering gemeente 0.010000m"),
    ("bud_agbktn_maint_2025", ENT, "2025", 67229, "D2 Sport Vlaanderen onderhoud 0.067229m"),
    ("bud_agbktn_schulden_2025", ENT, "2025", 3376072, "J4 schulden total 3.376072m"),
    ("bud_agbktn_aangewezen_2025", ENT, "2025", 264871, "J2 aangewezen aflossingen 0.264871m vs actual 0.046621m"),
]
assert abs((190289 + 3288967) - 3479256) < 2
assert abs((0 + 3287804 + 1163) - 3288967) < 2
assert abs((103184 + 3376072) - 3479256) < 2
assert abs((3233422 + 47348) - 3280771) < 2
assert abs((193795 - 138003) - 55792) < 2
assert abs((85817 + 9171) - 94988) < 2
assert abs((0 + 78184 + 25000) - 103184) < 2
assert abs((10000 + 5431) - 15431) < 2
assert abs((156547 + 515) - 157062) < 2
assert abs((36550 + 10071) - 46621) < 2
assert abs((9171 + (46621 - 264871)) - (-209080)) < 2
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
