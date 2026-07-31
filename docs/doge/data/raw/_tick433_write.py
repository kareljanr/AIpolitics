# tick 433: CoA Budget 2026 SS consol L5 residual + ONEM reform residual costs
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T07:15:00Z"
TICK = 433
UNIT = "rq_424"
SRC = "src_ccrek_budget2026_ss_l5_onem"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

# --- CoA p80 SS consolidated expenditure 2026 initial (m EUR -> EUR) ---
ss_total_2026 = 147_858.5e6
ss_total_2025 = 146_757.2e6
ss_total_2024 = 139_257.4e6
prest_2026 = 135_492.3e6
prest_2025 = 132_879.4e6
gg_sal_prest = 63_342.0e6
gg_sal_pens = 43_270.7e6
gg_sal_mi = 14_879.4e6
gg_sal_chom = 4_637.9e6
gg_sal_autres = 554.0e6
gg_indep_prest = 7_012.1e6
gg_indep_pens = 5_919.9e6
gg_indep_mi = 1_070.0e6
gg_indep_autres = 22.2e6
soins_sante = 41_297.2e6
pens_pub = 22_827.5e6
autres_prest = 1_013.6e6
frais_gestion = 2_996.3e6
autres_dep = 9_369.9e6

# Dual recon
mi_dual = gg_sal_mi + gg_indep_mi  # 15.9494bn
pens_stack = gg_sal_pens + gg_indep_pens + pens_pub  # 72.0181bn 2026 budget
# FPD legal cash 69.05bn 2025 (tick428) — year/perimeter differ

# Altfin p79
altfin_total = 27_221.6e6
altfin_onss = 23_392.2e6
altfin_inasti = 3_829.4e6
altfin_onss_tva_base = 9_343.8e6
altfin_onss_tva_sante = 7_645.2e6
altfin_onss_pm = 6_403.2e6

# ONEM residual reforms p95-98
rcc_save_2026 = 5.2e6  # already may exist
demission_cost_2026 = 33.6e6  # was "save" 45m initial 2025; now cost
demission_cost_steady = 34.0e6  # 2027-30
credit_temps_save_2026 = 1.6e6  # already may exist
credit_familial_2026 = 40.0e6  # CoA: overestimate risk vs 50m full-year
parental_foster = 1.1e6  # already may exist
pension_reform_delay = 64e6  # savings deferred (not realized 2026)

# Fedasil economy path already largely mapped — skip re-add

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 SS consol L5 + ONEM residual reforms",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"SS dep 147858.5m; prest L5 pens/MI/chom/soins/pub; "
                f"demission 33.6m cost; credit familial 40m; tick{TICK}"
            ),
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add_bud(bid, entity, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return False
    bud.append(
        {
            "budget_id": bid,
            "entity_id": entity,
            "year": str(year),
            "amount_eur": str(int(round(amount))),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": SRC,
            "confidence": conf,
            "notes": notes,
        }
    )
    return True


n_bud = 0
rows_b = [
    (
        "bud_ss_gg_sal_autres_2026",
        "onss",
        2026,
        gg_sal_autres,
        "budgeted",
        f"GG salaries autres prestations 554.0m 2026 CoA p80; tick{TICK}",
    ),
    (
        "bud_ss_gg_indep_mi_2026",
        "inasti",
        2026,
        gg_indep_mi,
        "budgeted",
        f"GG indep maladie/invalidite 1070.0m 2026 CoA p80 (+6.4pct); tick{TICK}",
    ),
    (
        "bud_ss_gg_indep_autres_2026",
        "inasti",
        2026,
        gg_indep_autres,
        "budgeted",
        f"GG indep autres prestations 22.2m 2026 CoA p80; tick{TICK}",
    ),
    (
        "bud_ss_soins_sante_41297m_2026",
        "inami",
        2026,
        soins_sante,
        "budgeted",
        f"INAMI soins de sante 41297.2m 2026 CoA p80 (+3.7pct vs 39812.1); dual entity1 ~41.3bn; tick{TICK}",
    ),
    (
        "bud_ss_autres_prest_2026",
        "sec_ss",
        2026,
        autres_prest,
        "budgeted",
        f"SS autres prestations sociales 1013.6m 2026 CoA p80 (-7.8pct); tick{TICK}",
    ),
    (
        "bud_ss_frais_gestion_2026",
        "sec_ss",
        2026,
        frais_gestion,
        "budgeted",
        f"SS frais gestion+paiement 2996.3m 2026 CoA p80; dual SPF SS gestion 2.9bn 2025 outturn; tick{TICK}",
    ),
    (
        "bud_ss_autres_dep_2026",
        "sec_ss",
        2026,
        autres_dep,
        "budgeted",
        f"SS autres depenses 9369.9m 2026 CoA p80 (-14.6pct vs 10967.8); residual L5 composition opaque; tick{TICK}",
    ),
    (
        "bud_ss_mi_dual_sal_indep_2026",
        "sec_ss",
        2026,
        mi_dual,
        "budgeted",
        f"Dual MI sal 14879.4 + indep 1070.0 = 15949.4m 2026 CoA; tick{TICK}",
    ),
    (
        "bud_ss_pens_stack_sal_indep_pub_2026",
        "sec_ss",
        2026,
        pens_stack,
        "budgeted",
        f"Pension stack GG sal 43270.7 + indep 5919.9 + publiques 22827.5 = 72018.1m 2026; dual FPD legal 69.05bn 2025 cash; tick{TICK}",
    ),
    (
        "bud_altfin_onss_gg_2026",
        "onss",
        2026,
        altfin_onss,
        "budgeted",
        f"ONSS GG financement alternatif 23392.2m 2026 CoA p79 (TVA base 9343.8 + sante 7645.2 + PM 6403.2); tick{TICK}",
    ),
    (
        "bud_altfin_inasti_gg_2026",
        "inasti",
        2026,
        altfin_inasti,
        "budgeted",
        f"INASTI GG financement alternatif 3829.4m 2026 CoA p79; tick{TICK}",
    ),
    (
        "bud_altfin_total_2026",
        "sec_ss",
        2026,
        altfin_total,
        "budgeted",
        f"SS financement alternatif total 27221.6m 2026 CoA p79 (+3.8pct); tick{TICK}",
    ),
    (
        "bud_demission_volontaire_cost_2026",
        "onem",
        2026,
        demission_cost_2026,
        "budgeted",
        f"Demission volontaire avec alloc chomage: cost 33.6m 2026 (reest Jun 2025; was +45m save initial 2025); CoA p97; tick{TICK}",
    ),
    (
        "bud_demission_volontaire_cost_steady",
        "onem",
        2027,
        demission_cost_steady,
        "budgeted",
        f"Demission volontaire steady cost ~34m/yr 2027-2030 CoA p97; tick{TICK}",
    ),
    (
        "bud_credit_familial_envelope_2026",
        "onem",
        2026,
        credit_familial_2026,
        "budgeted",
        f"Credit familial envelope 40m 2026 (plan cohesion 15 + deferred path); CoA p96 flags overestimate vs 50m full-year; tick{TICK}",
    ),
    (
        "bud_pension_reform_delay_64m_2026",
        "fpd",
        2026,
        pension_reform_delay,
        "budgeted",
        f"Pension reform 2026 savings reduced by 64m (laws not yet before Kamer; sal 33+indep 5+fonct 26); CoA p81; tick{TICK}",
    ),
    (
        "bud_ss_gg_sal_mi_2025",
        "onss",
        2025,
        14_206.9e6,
        "budgeted",
        f"GG sal maladie/invalidite BA 14206.9m 2025 path to 14879.4 2026; tick{TICK}",
    ),
    (
        "bud_ss_gg_sal_chom_2025",
        "onem",
        2025,
        6_458.7e6,
        "budgeted",
        f"GG sal chomage BA 6458.7m 2025 -> 4637.9 2026 (-28.2pct time-limit); tick{TICK}",
    ),
    (
        "bud_ss_soins_sante_2025",
        "inami",
        2025,
        39_812.1e6,
        "budgeted",
        f"Soins de sante BA 39812.1m 2025 path; tick{TICK}",
    ),
    (
        "bud_ss_pens_pub_2025",
        "fpd",
        2025,
        22_153.1e6,
        "budgeted",
        f"Pensions publiques BA 22153.1m 2025 path to 22827.5 2026; tick{TICK}",
    ),
]
for args in rows_b:
    if add_bud(*args):
        n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# --- commitments ---
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())


def add_cmt(cid, title, entity, beneficiary, legal, ddate, sy, ey, total, cash, status, goal, cut, notes, conf="strong"):
    if any(r.get("commitment_id") == cid for r in cmt):
        return False
    cmt.append(
        {
            "commitment_id": cid,
            "title": title,
            "entity_id": entity,
            "beneficiary": beneficiary,
            "legal_basis": legal,
            "decision_date": ddate,
            "start_year": str(sy),
            "end_year": str(ey),
            "total_envelope_eur": str(int(round(total))) if total else "",
            "cash_by_year": json.dumps(cash) if isinstance(cash, dict) else cash,
            "remaining_eur": "",
            "status": status,
            "evaluation_url": URL,
            "stated_goal": goal,
            "cut_option": cut,
            "source_id": SRC,
            "confidence": conf,
            "hierarchy_path": f"Federal>SS>{entity}",
            "notes": notes,
        }
    )
    return True


n_cmt = 0
if add_cmt(
    "cmt_ss_consol_l5_2026",
    "SS consolidated expenditure L5 residual fill 2026",
    "sec_ss",
    "SS beneficiaries (pensions, MI, chomage, soins, publiques)",
    "Budget SS consol CoA/SPF SS exposé général 2026",
    "2025-12-01",
    2026,
    2026,
    ss_total_2026,
    {
        "total": int(ss_total_2026),
        "prestations": int(prest_2026),
        "gg_sal": int(gg_sal_prest),
        "gg_sal_pens": int(gg_sal_pens),
        "gg_sal_mi": int(gg_sal_mi),
        "gg_sal_chom": int(gg_sal_chom),
        "gg_sal_autres": int(gg_sal_autres),
        "gg_indep": int(gg_indep_prest),
        "gg_indep_pens": int(gg_indep_pens),
        "gg_indep_mi": int(gg_indep_mi),
        "soins": int(soins_sante),
        "pens_pub": int(pens_pub),
        "autres_prest": int(autres_prest),
        "frais_gestion": int(frais_gestion),
        "autres_dep": int(autres_dep),
        "pens_stack": int(pens_stack),
        "mi_dual": int(mi_dual),
    },
    "active",
    "Social security consolidated budget presentation",
    "Publish full L5 for autres_dep 9.37bn; dual FPD vs GG pens perimeter note",
    f"CoA p80 full table residual fills; tick{TICK}",
):
    n_cmt += 1

if add_cmt(
    "cmt_onem_reform_residual_2026",
    "ONEM residual reforms: demission cost + credit familial + RCC/credit-temps paths",
    "onem",
    "Workers using voluntary resignation UI / family credit / RCC stock",
    "Loi-programme 18 Jul 2025; AR RCC 5 Sep 2025; coalition 31 Jan 2025",
    "2025-07-18",
    2026,
    2030,
    demission_cost_2026 + credit_familial_2026,
    {
        "demission_2026": int(demission_cost_2026),
        "demission_steady": int(demission_cost_steady),
        "credit_familial_2026": int(credit_familial_2026),
        "rcc_save_2026": int(rcc_save_2026),
        "credit_temps_save_2026": int(credit_temps_save_2026),
        "note": "demission flipped from +45m save to -33.6m cost",
    },
    "active",
    "Labour market flexibility / family leave / RCC phase-out",
    "Re-score demission incentive design; tighten credit familial modalities before full year",
    f"CoA p95-98 residual ONEM; tick{TICK}",
):
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# --- leaderboard ---
with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, level, typ, path, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes):
    if any(r.get("item_id") == iid for r in lb):
        return False
    # also skip if same name already exists with empty id matching annual
    if any(r.get("name") == name and r.get("annual_cost_eur") == str(int(round(annual))) for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": level,
            "type": typ,
            "hierarchy_path": path,
            "annual_cost_eur": str(int(round(annual))),
            "total_cost_eur": str(int(round(total))) if total else str(int(round(annual))),
            "tco_notes": tco,
            "confidence": conf,
            "source_id": SRC,
            "beneficiaries": benef,
            "stated_goal": goal,
            "measured_outcome": outcome,
            "absurdity_score": str(abs_s),
            "cost_score": str(cost_s),
            "difficulty": str(diff),
            "priority_index": str(prio),
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": notes,
        }
    )
    return True


n_lb = 0
lb_rows = [
    (
        "lb_ss_frais_gestion_3bn_2026",
        "SS management and payment costs 3.0bn 2026",
        "federal",
        "ops",
        "Federal>SS>frais_gestion_2026",
        frais_gestion,
        frais_gestion,
        "Strong CoA: 2996.3m 2026 (+3.0pct); dual SPF SS gestion 2.9bn 2025",
        "strong",
        "SS institutions admin",
        "Administer and pay social benefits",
        "Stable ~2% of SS dep",
        3,
        7,
        6,
        5.5,
        "Benchmark IPSS admin ratios; dual Smals IT stacks",
        f"tick{TICK}",
    ),
    (
        "lb_ss_autres_dep_9_37bn_2026",
        "SS other expenditure residual 9.37bn 2026",
        "federal",
        "transfer",
        "Federal>SS>autres_depenses_2026",
        autres_dep,
        autres_dep,
        "Strong aggregate CoA; L5 composition not in table (-14.6pct YoY)",
        "strong",
        "Mixed SS residual",
        "Non-benefit SS spending residual class",
        "Large residual opacity vs prestations",
        6,
        8,
        5,
        6.5,
        "Publish L5 decomposition of autres depenses",
        f"tick{TICK}; optional FOI if IPSS annex absent",
    ),
    (
        "lb_ss_soins_41_30bn_2026",
        "INAMI healthcare spending 41.30bn 2026",
        "federal",
        "transfer",
        "Federal>INAMI>soins_sante_2026",
        soins_sante,
        soins_sante,
        "Strong CoA p80: 41297.2m (+3.7pct vs 39812.1)",
        "strong",
        "Patients / providers",
        "Mandatory health insurance care",
        "Growth above general SS dep 0.8pct",
        2,
        9,
        8,
        6.0,
        "Norm growth dual; long-term sick reactivation path separate",
        f"tick{TICK}",
    ),
    (
        "lb_ss_pens_pub_22_83bn_2026",
        "Public-sector pensions 22.83bn 2026",
        "federal",
        "transfer",
        "Federal>FPD>pensions_publiques_2026",
        pens_pub,
        pens_pub,
        "Strong CoA: 22827.5m (+3.0pct); dual FPD fonct stock",
        "strong",
        "Civil servants pensioners",
        "Legal public pensions",
        "Part of 72.0bn pension stack 2026",
        2,
        8.5,
        8,
        5.5,
        "Pension reform laws still pending 2026 savings delay 64m",
        f"tick{TICK}",
    ),
    (
        "lb_ss_pens_stack_72bn_2026",
        "SS pension stack sal+indep+pub 72.0bn 2026",
        "federal",
        "transfer",
        "Federal>SS>pensions_stack_2026",
        pens_stack,
        pens_stack,
        "Strong sum CoA lines; dual FPD legal 69.05bn 2025 cash (year/perimeter)",
        "strong",
        "All legal pensioners",
        "Legal pensions three regimes",
        "Largest SS block",
        1,
        9.5,
        9,
        5.0,
        "Reform delivery risk (64m 2026 delay); dual FPD menage 5.92bn",
        f"tick{TICK}",
    ),
    (
        "lb_ss_mi_dual_15_95bn_2026",
        "SS sickness-invalidity dual sal+indep 15.95bn 2026",
        "federal",
        "transfer",
        "Federal>SS>MI_dual_2026",
        mi_dual,
        mi_dual,
        "Strong: sal 14879.4 + indep 1070.0; dual INAMI primaire/inv cash paths",
        "strong",
        "Long-term sick / invalidity",
        "Primary incapacity and invalidity benefits",
        "MI growing faster than chomage (chom -28pct)",
        4,
        8.5,
        7,
        6.5,
        "Reactivation long-term sick path 202m 2026 to 1.9bn 2029 dual",
        f"tick{TICK}",
    ),
    (
        "lb_demission_volontaire_cost_34m",
        "Voluntary resignation UI cost 33.6m 2026 (flipped save)",
        "federal",
        "transfer",
        "Federal>ONEM>demission_volontaire_2026",
        demission_cost_2026,
        demission_cost_2026 * 5,  # rough multi-year class
        "Strong CoA p97: cost 33.6m 2026 / ~34m steady (was +45m save in BI2025)",
        "strong",
        "Workers with 10y career using one-time quit UI",
        "Labour mobility without exclusion period",
        "Design flipped budget sign after loi-programme",
        7,
        4,
        4,
        5.5,
        "Revisit exclusion swap; measure take-up vs activation",
        f"tick{TICK}",
    ),
    (
        "lb_credit_familial_40m_2026",
        "Family credit envelope 40m 2026 (CoA overestimate risk)",
        "federal",
        "transfer",
        "Federal>ONEM>credit_familial_2026",
        credit_familial_2026,
        200e6,  # path 40+40+60+60 rough
        "Strong CoA p96: 40m 2026; full-year class 50m; modalities unfinished",
        "strong",
        "Parents taking family credit week",
        "One-week family leave credit",
        "CoA: inscription likely overstated vs implementation date",
        5,
        3.5,
        3,
        4.0,
        "Align credit to real start date; publish take-up",
        f"tick{TICK}",
    ),
    (
        "lb_ss_chom_drop_28pct_2026",
        "GG salaries unemployment 4.64bn 2026 (-28.2pct)",
        "federal",
        "transfer",
        "Federal>ONEM>chomage_gg_sal_2026",
        gg_sal_chom,
        gg_sal_chom,
        "Strong CoA: 4637.9m vs 6458.7m 2025; dual time-limit 1.69bn class",
        "strong",
        "Unemployed (time-limited)",
        "Unemployment benefits GG salaries",
        "Largest single-year SS line drop from reform",
        3,
        7.5,
        6,
        5.5,
        "Track RIS spillover (SPP IS 300m envelope understates 2027+)",
        f"tick{TICK}",
    ),
    (
        "lb_pension_reform_delay_64m",
        "Pension reform 2026 savings delay 64m",
        "federal",
        "policy",
        "Federal>FPD>pension_reform_delay_2026",
        pension_reform_delay,
        pension_reform_delay,
        "Strong CoA p81: laws not yet at Kamer; sal33+indep5+fonct26",
        "strong",
        "Future pension reform cohorts",
        "Coalition pension package 2026 entry",
        "Delivery slip reduces near-term save",
        5,
        4,
        5,
        4.5,
        "Pass reform bills; avoid further bonus-malus reestimates",
        f"tick{TICK}",
    ),
]
for args in lb_rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# --- research_queue ---
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())

for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: SS consol L5 residual (frais 3.0bn autres_dep 9.37bn soins 41.30 "
            f"pens stack 72.0 MI dual 15.95) + demission cost 33.6m + credit familial 40m; "
            f"rq_116 SWA deferred"
        )

if not any(r.get("task_id") == "rq_425" for r in rq):
    rq.append(
        {
            "task_id": "rq_425",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": f"Spawned tick{TICK} after SS L5 residual+ONEM; rq_116 SWA deferred",
        }
    )

with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

# --- loop_state ---
with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsf = list(ls[0].keys())
ls[-1]["last_tick_utc"] = NOW
ls[-1]["last_unit_id"] = UNIT
ls[-1]["ticks_completed"] = str(TICK)
ls[-1]["mode"] = "continuous"
ls[-1]["current_sprint"] = "hole_fill"
ls[-1]["paused"] = "no"
ls[-1]["notes"] = (
    f"Scheduler 60s. Next prio5 rq_425; rq_116 SWA deferred. "
    f"tick{TICK} SS L5 residual + demission/credit familial."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

# --- loop_log append (binary utf-8 for encoding safety) ---
log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **SS consol 2026 L5 residual + ONEM reform residual**)
- Found (strong primary Cour des comptes Budget Etat 2026 p79-80 + p95-98):
  - **SS consol dep 2026:** **EUR 147.8585bn** (+0.8% vs 146.76 adj 2025)
  - Prestations **135.492bn**; GG sal **63.342** (pens **43.271** · MI **14.879** · chom **4.638** · autres **0.554**)
  - GG indep **7.012** (pens **5.920** · MI **1.070** · autres **0.022**)
  - **Soins 41.297bn** · **pens publiques 22.828bn** · autres prest **1.014** · **frais gestion 2.996** · **autres dep 9.370**
  - Dual: pens stack **72.018bn**; MI dual **15.949bn**; chom **-28.2%** YoY
  - Altfin **27.222bn** (ONSS **23.392** · INASTI **3.829**)
  - **Demission volontaire cost EUR 33.6m 2026** (flipped from +45m "save"); steady ~34m
  - **Credit familial envelope 40m** (CoA overestimate risk vs 50m full-year)
  - Pension reform 2026 savings **−64m delay** (laws not yet Kamer)
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_424=done; spawn **rq_425**; ticks={TICK}
- FOI: none new (autres_dep 9.37bn L5 optional later if annex absent)
- Next: prio5 **rq_425**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")
print(f"pens_stack={pens_stack/1e9:.3f}bn mi_dual={mi_dual/1e9:.3f}bn")
