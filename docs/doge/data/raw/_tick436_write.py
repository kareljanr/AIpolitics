# tick 436: CoA Budget 2026 Fedasil multi-year L5 + development coop + ONSS SSC measures residual
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T08:45:00Z"
TICK = 436
UNIT = "rq_427"
SRC = "src_ccrek_budget2026_fedasil_coop_onss"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

# --- Fedasil economy path p61-62 (m EUR) ---
# Years 2025-2029
FED_YEARS = (2025, 2026, 2027, 2028, 2029)
FED_ACCUEIL = (0, 172, 303, 452, 538)
FED_RETOURS = (0, 75, 100, 125, 150)
FED_TOTAL = (0, 247, 403, 577, 688)
# Package dual
FED_DOT = {2025: 828.9, 2026: 702.2}
FED_PROV = {2025: 126.6, 2026: 100.0}
FED_PKG = {2025: 955.6, 2026: 802.2}
# Applications IBZ
FED_APPS = {2024: 39615, 2025: 34439}  # -13.1pct; SY -4163 PAL -2297

# --- Development cooperation p62-63 (m EUR liquidation credits DO 14.54) ---
COOP_YEARS = (2025, 2026, 2027)
COOP_MONITOR = (1235.3, 1252.6, 1274.3)  # CM Jul 2024 baseline
COOP_BUDGET = (1129.3, 1040.3, 957.0)
COOP_GAP = (106.0, 211.7, 317.3)  # vs monitor = savings path
FAD17 = 64.2  # voluntary ADF-17 reconstitution; pay over 10y not 3y (lose ~6m early-pay discount)
SEC_CORR_2027 = 27.0  # SEC net +27m first-year full booking of bank contribs

# --- ONSS labour-market measures residual p75-78 (m EUR) ---
# Group-target suppressions (collective RTT + Horeca fixed workers) from 1 Apr 2026
GROUP_CIBLE_GOV = 28.0  # notified 2026
GROUP_CIBLE_FULL_YR = 32.0  # ONSS 8.9 + 23.1
GROUP_CIBLE_COA_9M = 24.0  # CoA estimate partial year
GROUP_CIBLE_RTT = 8.9
GROUP_CIBLE_HORECA = 23.1

# High-wage employer cotis cap sports double-dip fix
SPORTS_CAP_FIX = 10.0  # /yr from measure

# Overtime voluntary SSC cost (dual prior 43m)
OVERTIME_SSC = 43.0  # /yr; CoA flags Apr1 start overstate vs full year ONSS 43.9
OVERTIME_FISCAL = 28.9  # IPP receipt loss already in CM Sep2025

# ONSS gestion budget boost 2026
ONSS_IT = 27.5
ONSS_INSP = 2.8  # 34 FTE social inspection
ONSS_GEST_BOOST = 30.3

# Plans-plus reform yields
PLANS_BUDGET = (53.0, 67.0, 52.0, 39.0)  # 2026-29 initial 2025 budget
PLANS_REEST = (64.2, 85.1, 78.2, None)  # ONSS Dec 2025; 2029 n.d.
PLANS_YEARS = (2026, 2027, 2028, 2029)

# Forward-looking cost measures (negative = cost to SS/budget)
CSSS_CUT = 415.0  # special SSC reduction from 2028 (was 2029)
BONUS_EMPLOI_BOOST_2028 = 357.5  # 210.5 fiscal + 147 social
STRUCT_LOW_WAGE_2026 = 584.0  # was 563 + 21 wage reval compensation reallocated
WAGE_REVAL_REALLOC = 21.0

# CSSS stock class
CSSS_2025_EST = 1430.1

# with open sources
with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 Fedasil multi-year L5 + development coop + ONSS SSC residual",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"p61-63 Fedasil 247→688m path accueil/retours; coop 1129→957; "
                f"p75-78 ONSS group-cible Plans-plus altfin dual; tick{TICK}"
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

# Fedasil L5 path
for i, y in enumerate(FED_YEARS):
    if FED_TOTAL[i] == 0 and y == 2025:
        # still record zero baseline year for series continuity
        pass
    if add_bud(
        f"bud_fedasil_save_total_{y}",
        "fedasil",
        y,
        FED_TOTAL[i] * 1e6,
        "budgeted",
        (
            f"Fedasil asylum-tightening total save {FED_TOTAL[i]}m {y} CoA p62 CM 14 Feb 2025 "
            f"(accueil {FED_ACCUEIL[i]} + retours {FED_RETOURS[i]}); method plan still Q1-2026 CoA; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_fedasil_save_accueil_{y}",
        "fedasil",
        y,
        FED_ACCUEIL[i] * 1e6,
        "budgeted",
        f"Reception-network reduction save {FED_ACCUEIL[i]}m {y} (path to 538m 2029); tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_fedasil_save_retours_{y}",
        "fedasil",
        y,
        FED_RETOURS[i] * 1e6,
        "budgeted",
        f"More-efficient returns / fewer entries save {FED_RETOURS[i]}m {y} (path to 150m 2029); tick{TICK}",
        "medium",
    ):
        n_bud += 1

# Application volumes
for y, n in FED_APPS.items():
    if add_bud(
        f"bud_fedasil_apps_{y}",
        "fedasil",
        y,
        n,
        "outturn" if y == 2025 else "outturn",
        (
            f"International protection applications {n} in {y} CoA p62 from IBZ "
            f"(2025 -13.1pct vs 2024; SY -4163 PAL -2297); headcount not EUR; tick{TICK}"
        ),
        "strong",
    ):
        n_bud += 1

# Development coop
for i, y in enumerate(COOP_YEARS):
    if add_bud(
        f"bud_coop_dev_liq_{y}",
        "sec_federal",
        y,
        COOP_BUDGET[i] * 1e6,
        "budgeted",
        (
            f"Development cooperation liquidation credits DO14.54 {COOP_BUDGET[i]}m {y} CoA p63 "
            f"(vs CM Jul2024 monitor {COOP_MONITOR[i]}m; gap/save {COOP_GAP[i]}m); tick{TICK}"
        ),
        "strong",
    ):
        n_bud += 1
    if add_bud(
        f"bud_coop_dev_monitor_{y}",
        "sec_federal",
        y,
        COOP_MONITOR[i] * 1e6,
        "estimate",
        f"CM Jul2024 monitoring baseline coop liq {COOP_MONITOR[i]}m {y}; dual budget path; tick{TICK}",
        "strong",
    ):
        n_bud += 1
    if add_bud(
        f"bud_coop_dev_gap_{y}",
        "sec_federal",
        y,
        COOP_GAP[i] * 1e6,
        "derived",
        (
            f"Coop savings vs Jul2024 monitor {COOP_GAP[i]}m {y} "
            f"(~25pct cut by 2027 vs monitor); new commitments only CoA; tick{TICK}"
        ),
        "strong",
    ):
        n_bud += 1

if add_bud(
    "bud_coop_fad17_2026",
    "sec_federal",
    2026,
    FAD17 * 1e6,
    "budgeted",
    (
        f"ADF-17 voluntary reconstitution limited to {FAD17}m AB 14.54.33.54.42.07; "
        f"engage 2026 pay over 10y (not 3y; forgo ~6m early-pay discount); tick{TICK}"
    ),
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_coop_sec_corr_2027",
    "sec_federal",
    2027,
    SEC_CORR_2027 * 1e6,
    "budgeted",
    f"SEC net correction +{SEC_CORR_2027}m 2027 for development-bank contributions (code 5 full first year); tick{TICK}",
    "strong",
):
    n_bud += 1

# ONSS residual measures
if add_bud(
    "bud_onss_group_cible_save_2026_gov",
    "rsz",
    2026,
    GROUP_CIBLE_GOV * 1e6,
    "budgeted",
    (
        f"Suppress group-target reductions RTT+Horeca from 1 Apr 2026: gov notify {GROUP_CIBLE_GOV}m; "
        f"ONSS full-yr RTT {GROUP_CIBLE_RTT}+Horeca {GROUP_CIBLE_HORECA}={GROUP_CIBLE_FULL_YR}m; "
        f"CoA 9-month est {GROUP_CIBLE_COA_9M}m (under-delivery risk); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_onss_group_cible_rtt_full",
    "rsz",
    2026,
    GROUP_CIBLE_RTT * 1e6,
    "estimate",
    f"Group-target collective working-time reduction full-year stock {GROUP_CIBLE_RTT}m ONSS; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_onss_group_cible_horeca_full",
    "rsz",
    2026,
    GROUP_CIBLE_HORECA * 1e6,
    "estimate",
    f"Group-target Horeca fixed workers full-year stock {GROUP_CIBLE_HORECA}m ONSS; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_onss_sports_cap_fix_2026",
    "rsz",
    2026,
    SPORTS_CAP_FIX * 1e6,
    "budgeted",
    (
        f"Block double-dip high-wage employer cotis cap + sports group-target: +{SPORTS_CAP_FIX}m/yr; "
        f"cap from Jul2025 at 85k EUR/quarter base wage; tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_onss_gest_it_2026",
    "rsz",
    2026,
    ONSS_IT * 1e6,
    "budgeted",
    f"ONSS gestion IT modernisation extra {ONSS_IT}m 2026; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_onss_gest_insp_2026",
    "rsz",
    2026,
    ONSS_INSP * 1e6,
    "budgeted",
    f"ONSS social inspection +34 FTE cost {ONSS_INSP}m 2026 (antifraud dual); tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_onss_gest_boost_total_2026",
    "rsz",
    2026,
    ONSS_GEST_BOOST * 1e6,
    "budgeted",
    f"ONSS gestion package IT+insp {ONSS_GEST_BOOST}m 2026; tick{TICK}",
    "strong",
):
    n_bud += 1

for i, y in enumerate(PLANS_YEARS):
    if add_bud(
        f"bud_plans_plus_budget_{y}",
        "rsz",
        y,
        PLANS_BUDGET[i] * 1e6,
        "budgeted",
        f"Plans-plus reform budgeted yield {PLANS_BUDGET[i]}m {y} (BI2025 path; expose understates ONSS reest); tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if PLANS_REEST[i] is not None:
        if add_bud(
            f"bud_plans_plus_reest_{y}",
            "rsz",
            y,
            PLANS_REEST[i] * 1e6,
            "estimate",
            (
                f"Plans-plus ONSS Dec2025 reest {PLANS_REEST[i]}m {y} "
                f"(vs budget {PLANS_BUDGET[i]}; delta +{PLANS_REEST[i]-PLANS_BUDGET[i]:.1f}); "
                f"not in CM/expose; tick{TICK}"
            ),
            "medium",
        ):
            n_bud += 1

if add_bud(
    "bud_csss_reduction_2028",
    "rsz",
    2028,
    CSSS_CUT * 1e6,
    "budgeted",
    (
        f"Special SSC (CSSS) reduction cost {CSSS_CUT}m from 2028 (advanced from 2029); "
        f"CSSS stock class ~{CSSS_2025_EST}m 2025; tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_bonus_emploi_boost_total_2028",
    "rsz",
    2028,
    BONUS_EMPLOI_BOOST_2028 * 1e6,
    "budgeted",
    (
        f"Bonus emploi reinforce cost {BONUS_EMPLOI_BOOST_2028}m 2028 "
        f"(fiscal 210.5 + social 147; advanced from 2029); dual prior bud_bonus_emploi_boost_2028; tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_onss_struct_low_wage_2026",
    "rsz",
    2026,
    STRUCT_LOW_WAGE_2026 * 1e6,
    "budgeted",
    (
        f"Structural low/mid-wage employer cotis reduction path {STRUCT_LOW_WAGE_2026}m 2026 "
        f"(was 563 + {WAGE_REVAL_REALLOC} wage-reval compensation reallocated); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1
if add_bud(
    "bud_onss_overtime_fiscal_dual_2026",
    "fod_finance",
    2026,
    OVERTIME_FISCAL * 1e6,
    "budgeted",
    f"Voluntary overtime IPP receipt loss {OVERTIME_FISCAL}m 2026 (CM Sep2025; dual SSC cost ~43m); tick{TICK}",
    "medium",
):
    n_bud += 1

# Altfin multi-year L5 fill from p79 table (if missing years)
ALTFIN = {
    # year: (onss_total, onss_tva_base, onss_tva_sante, onss_pm, inasti_total, inasti_tva_base, inasti_tva_sante, inasti_pm, total)
    2024: (21367.4, 8577.9, 6841.0, 5948.5, 3650.9, 1794.6, 673.9, 1182.4, 25018.3),
    2025: (22471.5, 9072.3, 7327.9, 6071.3, 3747.7, 1840.8, 724.0, 1182.9, 26219.2),
    2026: (23392.2, 9343.8, 7645.2, 6403.2, 3829.4, 1876.5, 714.1, 1238.8, 27221.6),
}
for y, vals in ALTFIN.items():
    labels = (
        "onss_total",
        "onss_tva_base",
        "onss_tva_sante",
        "onss_pm",
        "inasti_total",
        "inasti_tva_base",
        "inasti_tva_sante",
        "inasti_pm",
        "total",
    )
    entities = {
        "onss_total": "rsz",
        "onss_tva_base": "rsz",
        "onss_tva_sante": "rsz",
        "onss_pm": "rsz",
        "inasti_total": "rsvz",
        "inasti_tva_base": "rsvz",
        "inasti_tva_sante": "rsvz",
        "inasti_pm": "rsvz",
        "total": "sec_ss",
    }
    for lab, v in zip(labels, vals):
        bid = f"bud_altfin_l5_{lab}_{y}"
        conf = "strong"
        basis = "outturn" if y == 2024 else ("provisional" if y == 2025 else "budgeted")
        if add_bud(
            bid,
            entities[lab],
            y,
            v * 1e6,
            basis,
            f"Altfin L5 {lab} {v}m {y} CoA p79 table; dual prior 2026 aggregates; tick{TICK}",
            conf,
        ):
            n_bud += 1

# Attribution funds extras
if add_bud(
    "bud_altfin_csss_attrib_2026",
    "sec_ss",
    2026,
    102.4 * 1e6,
    "budgeted",
    f"CSSS via attribution funds 102.4m 2026 CoA p79; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_altfin_fonds_total_2026",
    "sec_ss",
    2026,
    27325 * 1e6,
    "budgeted",
    f"SS via attribution funds total 27325m 2026 (altfin 27221.6 + CSSS 102.4 + collab eco 1); tick{TICK}",
    "strong",
):
    n_bud += 1

# Prison food underfund residual (small L5)
if add_bud(
    "bud_prison_food_credit_2026",
    "fod_justice",
    2026,
    25.2 * 1e6,
    "budgeted",
    f"Detainee food/maintenance credits 25.2m eng+liq 2026 CoA p61; tick{TICK}",
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_prison_food_underfund_2026",
    "fod_justice",
    2026,
    10.18 * 1e6,
    "estimate",
    f"Admin estimate food/maintenance underfund 10.18m 2026 to draw from interdept security provision; tick{TICK}",
    "medium",
):
    n_bud += 1

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

# --- commitments ---
with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())

n_cmt = 0
if not any(r.get("commitment_id") == "cmt_fedasil_save_path_2025_29" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_fedasil_save_path_2025_29",
            "title": "Fedasil asylum-tightening multi-year save path 0-688m 2025-2029",
            "entity_id": "fedasil",
            "beneficiary": "Federal budget (reduced reception network / returns)",
            "legal_basis": "CM 14 Feb 2025 notification 8 trajet 2025-2029; CM 12 Dec 2025 budget",
            "decision_date": "2025-02-14",
            "start_year": "2025",
            "end_year": "2029",
            "total_envelope_eur": str(int(sum(FED_TOTAL) * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "total_m": {str(y): FED_TOTAL[i] for i, y in enumerate(FED_YEARS)},
                    "accueil_m": {str(y): FED_ACCUEIL[i] for i, y in enumerate(FED_YEARS)},
                    "retours_m": {str(y): FED_RETOURS[i] for i, y in enumerate(FED_YEARS)},
                    "package_m": FED_PKG,
                    "dot_m": FED_DOT,
                    "prov_m": FED_PROV,
                    "apps": FED_APPS,
                    "coa_flag": "no quantified delivery plan yet; Q1-2026 ministerial cell",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Tighten asylum policy; shrink reception network via lower inflow + returns",
            "cut_option": "Publish place-network and partner L5 cuts; dual FOI gap_fedasil_l5_partners",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "Federal>Interior>Fedasil>save_path_2025_29",
            "notes": f"CoA p61-62 full L5; dual cmt_fedasil_dot_2026; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_coop_dev_path_2025_27" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_coop_dev_path_2025_27",
            "title": "Development cooperation liquidation credits path 1.13bn to 0.96bn 2025-27",
            "entity_id": "sec_federal",
            "beneficiary": "Partner countries / multilaterals / Enabel class",
            "legal_basis": "Budget general DO 14.54; CM savings on new commitments",
            "decision_date": "2025-12-12",
            "start_year": "2025",
            "end_year": "2027",
            "total_envelope_eur": str(int(sum(COOP_BUDGET) * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "budget_m": {str(y): COOP_BUDGET[i] for i, y in enumerate(COOP_YEARS)},
                    "monitor_m": {str(y): COOP_MONITOR[i] for i, y in enumerate(COOP_YEARS)},
                    "gap_m": {str(y): COOP_GAP[i] for i, y in enumerate(COOP_YEARS)},
                    "fad17_m": FAD17,
                    "fad17_pay_years": 10,
                    "sec_corr_2027_m": SEC_CORR_2027,
                    "note": "Cuts on new commitments not prior legal obligations; ~25pct vs Jul2024 monitor by 2027",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Budget consolidation via lower new ODA commitments",
            "cut_option": "Publish Enabel/multilateral L5; track ADF/IDA share",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>AE>cooperation_development",
            "notes": f"CoA p62-63; tick{TICK}",
        }
    )
    n_cmt += 1

if not any(r.get("commitment_id") == "cmt_onss_ssc_measures_residual_2026_29" for r in cmt):
    cmt.append(
        {
            "commitment_id": "cmt_onss_ssc_measures_residual_2026_29",
            "title": "ONSS residual labour-market SSC measures 2026-29 L5",
            "entity_id": "rsz",
            "beneficiary": "Employers / low-wage workers / Horeca / sports / ONSS ops",
            "legal_basis": "Coalition + CM Dec2025; programme law drafts; group-target ARs",
            "decision_date": "2025-12-12",
            "start_year": "2026",
            "end_year": "2029",
            "total_envelope_eur": "",
            "cash_by_year": json.dumps(
                {
                    "group_cible_save_2026_gov_m": GROUP_CIBLE_GOV,
                    "group_cible_full_yr_m": GROUP_CIBLE_FULL_YR,
                    "group_cible_coa_9m_m": GROUP_CIBLE_COA_9M,
                    "sports_cap_fix_m": SPORTS_CAP_FIX,
                    "overtime_ssc_cost_m": OVERTIME_SSC,
                    "overtime_fiscal_m": OVERTIME_FISCAL,
                    "onss_gest_boost_2026_m": ONSS_GEST_BOOST,
                    "plans_plus_budget_m": list(PLANS_BUDGET),
                    "plans_plus_reest_m": list(PLANS_REEST),
                    "csss_cut_2028_m": CSSS_CUT,
                    "bonus_emploi_boost_2028_m": BONUS_EMPLOI_BOOST_2028,
                    "struct_low_wage_2026_m": STRUCT_LOW_WAGE_2026,
                    "csss_stock_2025_m": CSSS_2025_EST,
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Rebalance SSC reductions / finance ONSS ops / labour flexibility",
            "cut_option": "Score deadweight of remaining structurelles 2.4bn; dual EIWT TE",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "SS>ONSS>ssc_measures_residual",
            "notes": f"CoA p75-78 residual after tick396 package totals; tick{TICK}",
        }
    )
    n_cmt += 1

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

# --- leaderboard ---
with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, hpath, typ="policy"):
    if any(r.get("item_id") == iid for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": hpath,
            "annual_cost_eur": str(int(round(annual))),
            "total_cost_eur": str(int(round(total))),
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
rows = [
    (
        "lb_fedasil_save_path_688m",
        "Fedasil asylum-tightening save path to 688m 2029",
        247e6,
        sum(FED_TOTAL) * 1e6,
        "Medium CoA: 0/247/403/577/688; accueil 172→538 + retours 75→150; no quantified delivery plan yet",
        "medium",
        "Federal budget / asylum seekers / reception partners",
        "Shrink reception via lower inflow and returns",
        "Apps already -13% 2025; international context risk",
        5.0,
        8.0,
        7,
        6.7,
        "Publish place cuts L5; dual partner FOI; protect legal obligations",
        f"tick{TICK}",
        "Federal>Interior>Fedasil>save_path",
    ),
    (
        "lb_fedasil_accueil_538m_2029",
        "Fedasil reception-network reduction path 538m 2029",
        172e6,
        sum(FED_ACCUEIL) * 1e6,
        "Medium: 0/172/303/452/538 of total 688m path; largest Fedasil save lever",
        "medium",
        "Reception places / partners",
        "Reduce reception capacity with lower inflow",
        "Depends on international protection demand",
        5.5,
        7.5,
        7,
        6.6,
        "Unit cost per place; dual third-party 559m FOI",
        f"tick{TICK}",
        "Federal>Interior>Fedasil>accueil_cut",
    ),
    (
        "lb_coop_dev_1_04bn_2026",
        "Development cooperation credits 1.04bn 2026 path 0.96bn 2027",
        1040.3e6,
        sum(COOP_BUDGET) * 1e6,
        "Strong CoA: 1129.3/1040.3/957 vs monitor 1235/1253/1274; gap 106→317m (~25pct by 2027)",
        "strong",
        "Partner countries multilaterals Enabel",
        "ODA via DO14.54 liquidation credits",
        "Cuts on new commitments only; prior legal obligations kept",
        3.5,
        8.5,
        5,
        6.1,
        "Publish multilateral/bilateral L5; ADF-17 64.2m track",
        f"tick{TICK}",
        "Federal>AE>cooperation_development",
    ),
    (
        "lb_coop_dev_cut_path_317m",
        "Development coop cut vs monitor path to 317m 2027",
        211.7e6,
        sum(COOP_GAP) * 1e6,
        "Strong: savings gap 106/211.7/317.3 vs Jul2024 CM; FAD17 limited 64.2m 10y pay",
        "strong",
        "Federal budget",
        "Consolidate via lower new ODA",
        "SEC +27m 2027 bank contribs dual cash",
        4.0,
        6.5,
        4,
        5.1,
        "Keep legal multiyear; open new-commitment freeze list",
        f"tick{TICK}",
        "Federal>AE>coop_savings",
    ),
    (
        "lb_onss_group_cible_cut_28m",
        "Suppress RTT+Horeca group-target SSC reductions ~28m 2026",
        28e6,
        32e6,
        "Medium: gov 28m; ONSS full-yr 32m (RTT 8.9+Horeca 23.1); CoA 9-month ~24m under-delivery",
        "medium",
        "Employers with collective RTT / Horeca fixed staff",
        "End two 2003 group-target employer reductions",
        "From 1 Apr 2026; partial-year risk",
        4.0,
        4.0,
        3,
        3.8,
        "Score additionality of remaining group-targets",
        f"tick{TICK}",
        "SS>ONSS>group_cible_suppress",
    ),
    (
        "lb_plans_plus_reest_64m",
        "Plans-plus first-hire reform reest 64m 2026 (expose 53m)",
        64.2e6,
        (64.2 + 85.1 + 78.2) * 1e6,
        "Medium ONSS Dec2025: 64.2/85.1/78.2 vs budgeted 53/67/52; expose understates; 1 Apr 2026 start",
        "medium",
        "New small employers first hires",
        "Retarget first-hire SSC reductions (Plans-plus)",
        "1st hire cut 3100→2000; extend to 4th-5th hires",
        4.5,
        5.5,
        5,
        5.0,
        "Book ONSS reest at BA2026; dual first-hire TE",
        f"tick{TICK}",
        "SS>ONSS>plans_plus",
    ),
    (
        "lb_onss_struct_low_wage_584m",
        "Structural low/mid-wage SSC reduction boost 584m 2026",
        584e6,
        584e6,
        "Medium: 563 + 21 wage-reval compensation reallocated; no reest; dual structurelles 2.43bn stock",
        "medium",
        "Employers of low/mid-wage workers",
        "Progressive employer cotis cut low/mid wages",
        "Part of broader 5.17bn reduction package",
        5.0,
        7.5,
        5,
        6.1,
        "Evaluate deadweight vs employment; dual EIWT",
        f"tick{TICK}",
        "SS>ONSS>structurelles_low_wage",
    ),
    (
        "lb_csss_cut_415m_2028",
        "Special SSC (CSSS) reduction 415m from 2028",
        415e6,
        415e6,
        "Medium: advanced from 2029 in Dec2025 notifs; CSSS stock ~1.43bn 2025 class",
        "medium",
        "Workers paying CSSS (income-tested)",
        "Reduce special personal SSC",
        "Dual IPP reform package",
        4.0,
        7.0,
        5,
        5.5,
        "Publish distributional impact vs progressive rates",
        f"tick{TICK}",
        "SS>ONSS>csss_reduction",
    ),
    (
        "lb_altfin_ss_27_2bn_2026",
        "SS alternative financing 27.2bn 2026 (TVA+PM)",
        27221.6e6,
        27221.6e6,
        "Strong CoA p79: ONSS 23.39 + INASTI 3.83; multi-year 25.0→26.2→27.2 2024-26; floors activated",
        "strong",
        "SS beneficiaries via tax-funded altfin",
        "Finance SS via earmarked tax shares",
        "Tobacco 2.8bn + PP 0.9bn cover TVA shortfall class",
        2.0,
        9.5,
        4,
        5.9,
        "Keep floors transparent; dual Entity I tax",
        f"tick{TICK}",
        "SS>financing>alternatif",
    ),
    (
        "lb_prison_food_underfund_10m",
        "Prison food/maintenance underfund 10.2m 2026",
        10.18e6,
        10.18e6,
        "Medium CoA p61: credits 25.2m vs need; draw from security provision",
        "medium",
        "Detainees / DG EPI",
        "Feed and maintain prison population",
        "Structural under-budgeting class",
        6.5,
        3.5,
        3,
        4.5,
        "Inscribe full need in Justice section not provision",
        f"tick{TICK}",
        "Federal>Justice>prison_food",
    ),
]
for args in rows:
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
            f"tick{TICK}: Fedasil save L5 0/247/403/577/688 (accueil/retours) + coop 1129→957 "
            f"+ ONSS group-cible/Plans-plus/struct 584/CSSS 415 + altfin multi-year; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_428" for r in rq):
    rq.append(
        {
            "task_id": "rq_428",
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
            "notes": f"Spawned tick{TICK} after Fedasil/coop/ONSS residual; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_428; rq_116 SWA deferred. "
    f"tick{TICK} Fedasil 247-688 + coop 1.04bn + ONSS residual."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **Fedasil multi-year L5 + development coop + ONSS SSC residual**)
- Found (strong/medium primary Cour des comptes Budget Etat 2026 p61-63 + p75-79):
  - **Fedasil save path:** **0 / 247 / 403 / 577 / 688m** (2025-2029)
    - Accueil network **0/172/303/452/538** · Retours **0/75/100/125/150**
    - Package dual **955.6→802.2m** (dot 828.9→702.2 + prov 126.6→100); apps **39.6k→34.4k** (−13.1%)
    - CoA: no quantified delivery plan yet (ministerial cell Q1-2026)
  - **Development coop DO14.54:** liq **1.129 / 1.040 / 0.957bn** vs monitor **1.235 / 1.253 / 1.274** (gap **106/212/317m**; ~25pct by 2027)
    - FAD-17 voluntary **64.2m** pay over **10y** (forgo ~6m 3y discount); SEC **+27m** 2027
  - **ONSS residual measures:** group-cible RTT+Horeca cut gov **28m** (full-yr **32**; CoA 9m **24**); sports cap fix **10m**; gestion IT+insp **30.3m**
    - Plans-plus reest **64.2/85.1/78.2** vs budgeted **53/67/52** (expose understates)
    - Struct low-wage path **584m** 2026; CSSS cut **415m** from 2028; bonus emploi boost dual **357.5m** 2028
  - **Altfin multi-year L5:** total **25.0 / 26.2 / 27.2bn** 2024-26; ONSS/INASTI TVA+PM matrix; fonds total **27.325bn**
  - Prison food underfund **10.18m** on **25.2m** credits
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_427=done; spawn **rq_428**; ticks={TICK}
- FOI: none new (Fedasil partner L5 already ready gap_fedasil_l5_partners; delivery plan residual is policy design)
- Next: prio5 **rq_428**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")
