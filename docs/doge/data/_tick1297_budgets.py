# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path(__file__).resolve().parent
ENT="city_diepenbeek"
OCMW="ocmw_diepenbeek"
SRC="src_diepbk_jr2025_bbc"
TICK=1297
rows = [
    ("bud_diepbk_assets_2025", ENT, "2025", 190495607, "J4 assets 190.495607m vs 169.323416m"),
    ("bud_diepbk_assets_2024", ENT, "2024", 169323416, "J4 YE2024 assets 169.323416m"),
    ("bud_diepbk_cash_2025", ENT, "2025", 25046685, "J4 cash+beleg 25.046685m vs 25.039786m"),
    ("bud_diepbk_cash_2024", ENT, "2024", 25039786, "J4 YE2024 cash+beleg 25.039786m"),
    ("bud_diepbk_fva_2025", ENT, "2025", 55152635, "J4/T5 FVA 55.152635m (EVA 7.010 + IGS 45.774 + other 2.369)"),
    ("bud_diepbk_eva_2025", ENT, "2025", 7010000, "T5 EVA AGBD kapitaal 7.010000m frozen"),
    ("bud_diepbk_igs_2025", ENT, "2025", 45774081, "T5 IGS 45.774081m vs 26.349014m"),
    ("bud_diepbk_igs_reval_2025", ENT, "2025", 19425066, "T5 IGS herwaardering +19.425066m no cash"),
    ("bud_diepbk_mva_2025", ENT, "2025", 99220970, "J4/T5 MVA 99.220970m; leasing 7.812713m"),
    ("bud_diepbk_leasing_2025", ENT, "2025", 7812713, "T5 leasing MVA 1.727+6.085=7.813m"),
    ("bud_diepbk_equity_2025", ENT, "2025", 166893147, "J4 nettoactief 166.893147m vs 144.225242m"),
    ("bud_diepbk_cap_subs_2025", ENT, "2025", 10977432, "J4/T5 cap subs 10.977432m"),
    ("bud_diepbk_cum_pnl_2025", ENT, "2025", 26993831, "J4/T5 cum PnL 26.993831m"),
    ("bud_diepbk_reval_2025", ENT, "2025", 19445051, "J4/T5 herwaardering 19.445051m vs 0.020m"),
    ("bud_diepbk_fin_debt_2025", ENT, "2025", 13592179, "T4 fin debt 13.592179m (LT 11.712 + ST due 1.850 + ST 0.030)"),
    ("bud_diepbk_fin_debt_2024", ENT, "2024", 14915568, "T4 YE2024 fin debt 14.915568m"),
    ("bud_diepbk_fin_debt_lt_2025", ENT, "2025", 11712103, "T4 LT fin debt 11.712103m"),
    ("bud_diepbk_fin_debt_st_2025", ENT, "2025", 1880077, "T4 ST due 1.849636m + ST 0.030441m"),
    ("bud_diepbk_new_loans_2025", ENT, "2025", 576680, "T4 new loans 0.576680m leasing; no new bank loans"),
    ("bud_diepbk_pension_2025", ENT, "2025", 3093433, "J4 LT pension 3.093433m vs 3.292983m"),
    ("bud_diepbk_expl_2025", ENT, "2025", 6222031, "J2 exploitatiesaldo +6.222031m"),
    ("bud_diepbk_expl_ontv_2025", ENT, "2025", 45425962, "J2 expl ontv 45.425962m"),
    ("bud_diepbk_expl_uitg_2025", ENT, "2025", 39203931, "J2 expl uitg 39.203931m"),
    ("bud_diepbk_city_expl_2025", ENT, "2025", 7776203, "J3 city expl +7.776203m"),
    ("bud_diepbk_ocmw_expl_2025", OCMW, "2025", -1554171, "J3 OCMW expl -1.554171m"),
    ("bud_diepbk_invest_2025", ENT, "2025", -5231327, "J2 invest -5.231327m vs MJP -8.476m"),
    ("bud_diepbk_bbr_2025", ENT, "2025", 364399, "J2 budgettair resultaat boekjaar +0.364399m"),
    ("bud_diepbk_avail_2025", ENT, "2025", 21858004, "J2 beschikbaar BBR 21.858004m"),
    ("bud_diepbk_afm_2025", ENT, "2025", 5047040, "J2 AFM +5.047040m"),
    ("bud_diepbk_gecorr_2025", ENT, "2025", 5784304, "J2 gecorr AFM +5.784304m"),
    ("bud_diepbk_pnl_2025", ENT, "2025", 3153685, "J5 PnL +3.153685m (city +4.983 / OCMW -1.830)"),
    ("bud_diepbk_pers_2025", ENT, "2025", 24853856, "J5/T2 bezoldigingen 24.853856m; VTE unpublished"),
    ("bud_diepbk_fiscal_2025", ENT, "2025", 18601363, "T2 fiscale 18.601363m (OV 7.335 + APB 9.372)"),
    ("bud_diepbk_gemfonds_2025", ENT, "2025", 7009148, "T2 gemeentefonds 7.009148m"),
    ("bud_diepbk_politie_2025", ENT, "2025", 2765711, "T2 politiezone Limburg regio Hoofdstad 2.765711m"),
    ("bud_diepbk_hvz_2025", ENT, "2025", 952387, "T2 HVZ Zuid-West-Limburg 0.952387m"),
    ("bud_diepbk_agb_werksub_2025", ENT, "2025", 698706, "T2 city werksub aan AGB 0.698706m vs AGBD 0.385m"),
    ("bud_diepbk_ocmw_equity_2025", OCMW, "2025", -708459, "T5 OCMW equity -0.708459m NEG"),
    ("bud_diepbk_afl_2025", ENT, "2025", 1930509, "T4/J2 periodieke aflossingen 1.930509m"),
]
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
