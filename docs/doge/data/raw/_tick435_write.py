# tick 435: CoA Budget 2026 RTW invalidity L5 multi-year 2026-2029 + chomage wave exclusions
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T08:15:00Z"
TICK = 435
UNIT = "rq_426"
SRC = "src_ccrek_budget2026_rtw_l5"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

YEARS = (2026, 2027, 2028, 2029)

# Overview table p85 — net contribution to "diminution des dépenses" (m EUR)
# Contrôles thématiques = recontrol gross savings+receipts net of staff cost
# Économies + personnel are the breakdown of contrôles (do not triple-add into total)
MEAS = {
    "recontrol_net": (34.3, 185.0, 538.3, 1045.0),  # contrôles thématiques net
    "recontrol_gross": (38.7, 195.8, 558.3, 1065.6),  # économies indemnités + recettes
    "recontrol_staff_cost": (-4.4, -10.8, -20.3, -20.6),  # personnel mutualités/INAMI
    "annual_ext": (126.9, 373.6, 618.9, 868.8),  # suivi renforcé
    "solidarity_cotis": (0.0, 72.0, 75.0, 77.0),
    "psycho_firstline_net": (2.9, 6.3, 9.1, 11.3),
    "eta_adapted_work": (4.8, 11.7, 17.3, 22.3),
    "whp_workplace": (0.0, 2.8, 6.3, 6.7),
    "maladie_fonct_net": (34.0, 2.0, 54.0, 89.0),  # table sign as published; see notes
    "total": (202.9, 643.8, 1198.3, 1928.7),
}

# Recontrol detail p86 (cumulative where noted)
RECONTROL_DOSSIERS_YR = (19672, 50015, 94030, 94030)
RECONTROL_EXCL_CUM = (2634, 10539, 26347, 43056)
RECONTROL_EXCL_SAL = (2512, 10048, 25120, 41034)
RECONTROL_EXCL_INDEP = (122, 491, 1227, 2022)
RECONTROL_IND_SAVE = (28.9, 145.7, 415.0, 791.2)  # m EUR cum
RECONTROL_SSC = (5.7, 29.1, 83.5, 159.6)
RECONTROL_TAX = (4.1, 20.9, 60.0, 114.8)
# Total 38.7/195.8/558.6/1065.6 (p86 uses 558.6 vs overview 558.3)

# Annual extension p88
EXT_EXCL_CUM = (12390, 24394, 35577, 47148)
EXT_EXCL_SAL = (11578, 22785, 33215, 43998)
EXT_EXCL_INDEP = (812, 1609, 2362, 3150)
EXT_SAVE_SAL = (119.0, 349.8, 579.1, 812.6)
EXT_SAVE_INDEP = (7.9, 23.8, 39.7, 56.2)

# Pension maladie fonctionnaires p89-90
MAL_COST_INDEM = (16.5, 48.8, 94.3, 124.3)  # extra indemnity cost m
MAL_COST_ADMIN = (0.1, 0.1, 0.8, 2.2)
MAL_COTIS = (51.0, 47.0, 41.0, 37.0)  # responsabilisation cotis
MAL_INFLOW_YR = 1538  # INAMI est; SFP dual 2534

# Psycho: cost 16.9m cum to 2029; receipts 30.4m; net path in table
PSYCHO_COST_END = 16.9
PSYCHO_REC_END = 30.4

# Work resumption prime cost p89 (not net save)
WORK_PRIME_COST = (28.0, 34.7, 38.2, 38.5)  # m EUR cost

# Sample controls 2024: 8.8% and 23.7% exclusion rates on 920+920
# CoA overstate: INAMI extra 39k dossiers / 5.7k excl error → +48.1m overstate 2029
COA_OVERSTATE_2029_M = 48.1
TARGET_EXITS = 90204  # 43056 recontrol + 47148 annual ext

# Chomage wave exclusions p94 (persons, not EUR)
WAVES = {
    "v1_2026_01_01": {"date": "2026-01-01", "type": "chomage", "BRU": 3021, "DG": 31, "VL": 1672, "WAL": 4494, "total": 9218},
    "v2_2026_h1": {"date": "2026-H1", "type": "insertion", "BRU": 1400, "DG": 64, "VL": 2783, "WAL": 11072, "total": 15319},
    "v3_2026_03_01": {"date": "2026-03-01", "type": "chomage", "BRU": 11926, "DG": 164, "VL": 8883, "WAL": 18624, "total": 39597},
    "v4_2026_04_01": {"date": "2026-04-01", "type": "chomage", "BRU": 13152, "DG": 227, "VL": 15331, "WAL": 22806, "total": 51516},
    "v5_2026_07_01": {"date": "2026-07-01", "type": "chomage", "BRU": 6922, "DG": 271, "VL": 16473, "WAL": 18329, "total": 41995},
    "v6_2026_07_to_2027_07": {
        "date": "2026-07→2027-07",
        "type": "chomage",
        "BRU": 4648,
        "DG": 164,
        "VL": 14154,
        "WAL": 10833,
        "total": 29799,
    },
    "v_final_2027_07_01": {"date": "2027-07-01", "type": "chomage", "BRU": 640, "DG": 32, "VL": 3380, "WAL": 2408, "total": 6460},
}
# Regional totals from table: BRU 41709 DG 953 VL 62676 WAL 88566 TOTAL 193904

LABELS = {
    "recontrol_net": "Controles thematiques mutualites/INAMI (net of staff)",
    "recontrol_gross": "Recontrol indemnity savings + SSC/tax receipts (gross)",
    "recontrol_staff_cost": "Extra staff cost mutualites/INAMI for recontrols",
    "annual_ext": "Annual incapacity extension obligation (suivi renforce)",
    "solidarity_cotis": "Employer solidarity cotis months 2-5 sickness (>50 FTE)",
    "psycho_firstline_net": "First-line psychological care net (cost vs claimed receipts)",
    "eta_adapted_work": "Adapted-work enterprises indemnity cumulation reform",
    "whp_workplace": "Workplace health promotion extension (WHP)",
    "maladie_fonct_net": "Public-sector sickness pension transfer to AMI (table net)",
    "total": "RTW plan total indemnity-expenditure reduction",
}

# --- sources ---
with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 RTW invalidity L5 multi-year + chomage waves",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"p84-90 RTW plan tables; p94 chomage exclusion waves; "
                f"totals 202.9→1928.7m 2026-29; CoA overstate flags; tick{TICK}"
            ),
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

# --- budgets ---
with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add_bud(bid, entity, year, amount, basis, notes, conf="medium"):
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
for key, vals in MEAS.items():
    for y, v in zip(YEARS, vals):
        bid = f"bud_rtw_l5_{key}_{y}"
        note = (
            f"{LABELS[key]}: {v}m EUR {y} CoA p85 overview "
            f"(positive=indemnity reduction / net save class; staff negative=cost). "
            f"Most measures undeveloped CoA; dual prior bud_rtw_*. tick{TICK}"
        )
        conf = "medium"  # CoA: most measures still to design; sample overstate risk
        if add_bud(bid, "riziv", y, v * 1e6, "budgeted", note, conf):
            n_bud += 1

# Recontrol operational L5 (headcount + cash components)
for i, y in enumerate(YEARS):
    if add_bud(
        f"bud_rtw_recontrol_dossiers_{y}",
        "riziv",
        y,
        RECONTROL_DOSSIERS_YR[i],
        "estimate",
        f"Recontrol dossiers to check {RECONTROL_DOSSIERS_YR[i]} in {y} CoA p86 (headcount not EUR); tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_recontrol_excl_cum_{y}",
        "riziv",
        y,
        RECONTROL_EXCL_CUM[i],
        "estimate",
        (
            f"Recontrol exclusions cumulative {RECONTROL_EXCL_CUM[i]} by EOY {y} "
            f"(sal {RECONTROL_EXCL_SAL[i]} indep {RECONTROL_EXCL_INDEP[i]}); headcount; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_recontrol_indem_save_{y}",
        "riziv",
        y,
        RECONTROL_IND_SAVE[i] * 1e6,
        "budgeted",
        f"Recontrol indemnity savings cumulative {RECONTROL_IND_SAVE[i]}m {y} CoA p86; tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_recontrol_ssc_{y}",
        "riziv",
        y,
        RECONTROL_SSC[i] * 1e6,
        "budgeted",
        f"Recontrol return-to-work SSC receipts {RECONTROL_SSC[i]}m {y}; tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_recontrol_tax_{y}",
        "riziv",
        y,
        RECONTROL_TAX[i] * 1e6,
        "budgeted",
        f"Recontrol return-to-work tax receipts (IPP+VAT) {RECONTROL_TAX[i]}m {y}; tick{TICK}",
        "medium",
    ):
        n_bud += 1

# Annual extension headcount + sal/indep split
for i, y in enumerate(YEARS):
    if add_bud(
        f"bud_rtw_ext_excl_cum_{y}",
        "riziv",
        y,
        EXT_EXCL_CUM[i],
        "estimate",
        (
            f"Annual-extension exclusions cum {EXT_EXCL_CUM[i]} by EOY {y} "
            f"(sal {EXT_EXCL_SAL[i]} indep {EXT_EXCL_INDEP[i]}); ~3pct/yr exit hyp; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_ext_save_sal_{y}",
        "riziv",
        y,
        EXT_SAVE_SAL[i] * 1e6,
        "budgeted",
        f"Annual-ext save salaried {EXT_SAVE_SAL[i]}m {y} CoA p88; tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_ext_save_indep_{y}",
        "riziv",
        y,
        EXT_SAVE_INDEP[i] * 1e6,
        "budgeted",
        f"Annual-ext save independants {EXT_SAVE_INDEP[i]}m {y}; tick{TICK}",
        "medium",
    ):
        n_bud += 1

# Maladie fonctionnaires dual cost/cotis
for i, y in enumerate(YEARS):
    if add_bud(
        f"bud_rtw_mal_fonct_indem_cost_{y}",
        "riziv",
        y,
        MAL_COST_INDEM[i] * 1e6,
        "budgeted",
        (
            f"Public sickness-pension → AMI indemnity cost {MAL_COST_INDEM[i]}m {y} "
            f"(inflow ~{MAL_INFLOW_YR}/yr INAMI vs SFP dual 2534); law not yet Kamer; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_mal_fonct_admin_{y}",
        "riziv",
        y,
        MAL_COST_ADMIN[i] * 1e6,
        "budgeted",
        f"Maladie fonct admin/staff cost {MAL_COST_ADMIN[i]}m {y}; tick{TICK}",
        "medium",
    ):
        n_bud += 1
    if add_bud(
        f"bud_rtw_mal_fonct_cotis_{y}",
        "riziv",
        y,
        MAL_COTIS[i] * 1e6,
        "budgeted",
        (
            f"Entity responsabilisation cotis {MAL_COTIS[i]}m {y} (notif; INAMI calc 47.2m/yr class); "
            f"max 62800 EUR/case; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

# Work prime cost path
for i, y in enumerate(YEARS):
    if add_bud(
        f"bud_rtw_work_prime_cost_{y}",
        "riziv",
        y,
        WORK_PRIME_COST[i] * 1e6,
        "budgeted",
        (
            f"Work-resumption employer prime cost {WORK_PRIME_COST[i]}m {y} "
            f"(prime 3000 EUR; 5x 2025 uptake hyp 10.48pct base); not in p85 net total; tick{TICK}"
        ),
        "medium",
    ):
        n_bud += 1

# CoA overstate flag row
if add_bud(
    "bud_rtw_coa_overstate_recontrol_2029",
    "riziv",
    2029,
    COA_OVERSTATE_2029_M * 1e6,
    "derived",
    (
        f"CoA: INAMI recontrol indemnity-save overstated by ~{COA_OVERSTATE_2029_M}m 2029 "
        f"(5.7k excl calc error vs 2.7k at 10pct of 27k dossiers); tick{TICK}"
    ),
    "medium",
):
    n_bud += 1

# Baseline path without reform
if add_bud(
    "bud_rtw_baseline_incapacity_2029",
    "riziv",
    2029,
    18346700000,
    "estimate",
    (
        "Policy-unchanged incapacity (sal+indep) path 18346.7m 2029 (+28pct vs 2024); "
        "invalidity alone +31.4pct to 13.4bn / stock 656164; tick{TICK}"
    ),
    "strong",
):
    n_bud += 1
if add_bud(
    "bud_rtw_target_exits_2029",
    "riziv",
    2029,
    TARGET_EXITS,
    "estimate",
    f"Gov target invalid exits by 2029: {TARGET_EXITS} (recontrol 43056 + annual-ext 47148); headcount; tick{TICK}",
    "medium",
):
    n_bud += 1

# Chomage wave exclusions (headcount stored as amount_eur for consistency with prior pattern)
for wname, w in WAVES.items():
    for reg in ("BRU", "DG", "VL", "WAL", "total"):
        bid = f"bud_chom_wave_{wname}_{reg.lower()}"
        note = (
            f"UI exclusion wave {wname} region {reg}: {w[reg]} persons "
            f"(type {w['type']}; end-right {w['date']}) CoA p94 ONEM Sep2025 est; headcount not EUR; tick{TICK}"
        )
        if add_bud(bid, "rva", 2026 if "2027" not in w["date"] else 2027, w[reg], "estimate", note, "strong"):
            n_bud += 1

# Dual recon totals by region already exist; add grand check
if add_bud(
    "bud_chom_waves_sum_check",
    "rva",
    2026,
    193904,
    "derived",
    "Sum of CoA p94 wave totals 9218+15319+39597+51516+41995+29799+6460=193904 (matches regional sum); tick{TICK}",
    "strong",
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
cid = "cmt_rtw_l5_2026_2029"
if not any(r.get("commitment_id") == cid for r in cmt):
    cmt.append(
        {
            "commitment_id": cid,
            "title": "Return-to-work invalidity plan L5 multi-year 2026-2029",
            "entity_id": "riziv",
            "beneficiary": "Invalids / mutualities / employers / public entities (maladie fonct)",
            "legal_basis": "Vision note 27 Nov 2025; law 19 Dec 2025 solidarity wave; fourth wave still design",
            "decision_date": "2025-11-27",
            "start_year": "2026",
            "end_year": "2029",
            "total_envelope_eur": str(int(sum(MEAS["total"]) * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "totals_m": {str(y): MEAS["total"][i] for i, y in enumerate(YEARS)},
                    "recontrol_net_m": list(MEAS["recontrol_net"]),
                    "recontrol_gross_m": list(MEAS["recontrol_gross"]),
                    "recontrol_staff_cost_m": list(MEAS["recontrol_staff_cost"]),
                    "annual_ext_m": list(MEAS["annual_ext"]),
                    "solidarity_m": list(MEAS["solidarity_cotis"]),
                    "psycho_net_m": list(MEAS["psycho_firstline_net"]),
                    "eta_m": list(MEAS["eta_adapted_work"]),
                    "whp_m": list(MEAS["whp_workplace"]),
                    "maladie_fonct_net_m": list(MEAS["maladie_fonct_net"]),
                    "maladie_cost_indem_m": list(MAL_COST_INDEM),
                    "maladie_cotis_m": list(MAL_COTIS),
                    "work_prime_cost_m": list(WORK_PRIME_COST),
                    "exits_target": TARGET_EXITS,
                    "recontrol_excl_2029": 43056,
                    "ext_excl_2029": 47148,
                    "coa_overstate_recontrol_2029_m": COA_OVERSTATE_2029_M,
                    "coa_flags": [
                        "most measures undeveloped",
                        "sample exclusion rates may not scale",
                        "annual-ext 3pct method not disclosed",
                        "psycho ROI study is for still-at-work population",
                        "maladie fonct law not deposited as of 13 Feb 2026",
                        "no spillover from chomage reform modelled",
                    ],
                }
            ),
            "remaining_eur": "",
            "status": "planned",
            "evaluation_url": URL,
            "stated_goal": "Slow invalidity stock growth; reintegration / recontrol / annual extension",
            "cut_option": "Legislate before booking 2026; independent method audit; dual chomage-RIS spillover",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "SS>INAMI>retour_au_travail_l5",
            "notes": f"CoA p84-90 full L5; dual cmt_rtw_invalidite_2026_29; tick{TICK}",
        }
    )
    n_cmt += 1

cid2 = "cmt_chom_exclusion_waves_2026_27"
if not any(r.get("commitment_id") == cid2 for r in cmt):
    cmt.append(
        {
            "commitment_id": cid2,
            "title": "Chomage reform exclusion waves by region 2026-2027 (193904 persons)",
            "entity_id": "rva",
            "beneficiary": "Unemployed losing UI right (spillover RIS/CPAS class ~1/3)",
            "legal_basis": "Loi-programme 18 Jul 2025; ONEM notifications Sep2025",
            "decision_date": "2025-07-18",
            "start_year": "2026",
            "end_year": "2027",
            "total_envelope_eur": "",
            "cash_by_year": json.dumps(
                {
                    "persons_total": 193904,
                    "region": {"BRU": 41709, "DG": 953, "VL": 62676, "WAL": 88566},
                    "waves": WAVES,
                    "euro_path_m": {"2026": 1685.2, "2027": 2286.7, "2028": 2440.6, "2029": 2447.8, "2030": 2453.3},
                    "note": "Headcount L5; euro path dual cmt_chom_reform_multiyear; dual RIS +300m compensation",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Implement UI time-limit reform with transitional waves",
            "cut_option": "Track outturn per wave; dual SPP IS CPAS compensation path",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "SS>ONEM>chomage_exclusion_waves",
            "notes": f"CoA p94 wave x region matrix; tick{TICK}",
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
# annual = 2029 path (largest year) or first material year
rows = [
    (
        "lb_rtw_recontrol_1_07bn_2029",
        "RTW recontrol mutualities/INAMI path 1.07bn 2029",
        1065.6e6,
        sum(MEAS["recontrol_gross"]) * 1e6,
        "Medium CoA: gross 38.7→1065.6m; 43k excl; sample 8.8/23.7pct may not scale; CoA +48.1m overstate 2029",
        "medium",
        "Long-term invalids selected for thematic recontrol",
        "Re-verify invalidity recognition / exit unjustified cases",
        "Depends on staff hire + law; 1/3 work 1/3 RIS 1/3 exit hyp",
        6.5,
        8.5,
        7,
        7.4,
        "Independent method audit; publish exclusion rates by pathology",
        f"tick{TICK}",
        "SS>INAMI>rtw_recontrol",
    ),
    (
        "lb_rtw_annual_ext_869m_2029",
        "RTW annual incapacity-extension obligation save 869m 2029",
        868.8e6,
        sum(MEAS["annual_ext"]) * 1e6,
        "Medium CoA: 126.9→868.8m; 47k excl; 3pct exit hyp not disclosed; GP collaboration incomplete",
        "medium",
        "Invalids >1y without annual work-capacity review",
        "Force annual medical prolongation request",
        "No extra capacity budgeted for GPs/mutualities CoA",
        6.0,
        8.0,
        7,
        7.0,
        "Fund admin capacity; publish exit destinations",
        f"tick{TICK}",
        "SS>INAMI>rtw_annual_extension",
    ),
    (
        "lb_rtw_total_1_93bn_2029_l5",
        "RTW plan total save path 203m to 1.93bn 2026-29 (L5 deep)",
        1928.7e6,
        sum(MEAS["total"]) * 1e6,
        "Medium dual lb_rtw_1_93bn_2029; full L5 matrix; CoA most measures undeveloped + sample risk",
        "medium",
        "Invalids mutualities employers",
        "Fourth-wave return-to-work plan",
        "Baseline incapacity 18.3bn 2029 without reform",
        5.5,
        9.0,
        8,
        7.35,
        "Legislate before booking; dual chomage spillover FOI",
        f"tick{TICK}",
        "SS>INAMI>retour_au_travail",
    ),
    (
        "lb_rtw_solidarity_72m",
        "Employer solidarity cotis months 2-5 sickness 72m 2027",
        72e6,
        sum(MEAS["solidarity_cotis"]) * 1e6,
        "Medium: law 19 Dec 2025; path 0/72/75/77; CoA partial-year risk (due from Aug 2027)",
        "medium",
        "Employers >50 FTE with sick workers 18-55",
        "Employer co-responsibility early sickness",
        "30pct of indemnity months 2-3 then 4-5 from 2027",
        4.0,
        5.0,
        4,
        4.4,
        "Publish firm-size incidence; avoid SME spillover",
        f"tick{TICK}",
        "SS>INAMI>solidarity_cotis",
    ),
    (
        "lb_rtw_psycho_roi_fragile",
        "First-line psychology RTW net 2.9→11.3m (ROI study fragile)",
        11.3e6,
        sum(MEAS["psycho_firstline_net"]) * 1e6,
        "Weak-medium: cost 16.9m receipts 30.4m claimed; CoA: EPCAP study is for still-at-work days not invalids",
        "medium",
        "Workers with mental-health needs / invalids",
        "Preventive and recovery first-line psychology",
        "Psychologist supply constraint CoA",
        7.0,
        3.5,
        5,
        5.3,
        "Re-score ROI on invalid population; expand supply first",
        f"tick{TICK}",
        "SS>INAMI>psycho_firstline",
    ),
    (
        "lb_rtw_maladie_fonct_transfer",
        "Public sickness-pension → AMI transfer dual FPD/INAMI",
        124.3e6,
        sum(MAL_COST_INDEM) * 1e6,
        "Medium: indemnity cost 16.5→124.3m + cotis 51→37; net table 34/2/54/89; law not deposited Feb2026; dual FPD save 94→302m",
        "medium",
        "Civil servants long-term sick / federal entities",
        "End public maladie pension; shift to AMI + entity cotis",
        "INAMI inflow 1538 vs SFP 2534 dual; avg indemnity gap 912 EUR/mo",
        5.5,
        6.0,
        7,
        6.0,
        "Pass law; reconcile FPD-INAMI dual stock",
        f"tick{TICK}",
        "SS>INAMI>maladie_fonctionnaires",
    ),
    (
        "lb_rtw_work_prime_cost_28m",
        "Work-resumption employer prime cost 28m 2026 path 38.5m",
        28e6,
        sum(WORK_PRIME_COST) * 1e6,
        "Medium: prime to 3000 EUR; 5x uptake from 10.48pct 2025 base; law still needed; no conditions CoA",
        "medium",
        "Employers offering adapted work 3+ months",
        "Incentivise adapted-work reintegration",
        "2025 uptake only ~10pct of eligible resumes",
        5.0,
        4.5,
        5,
        4.7,
        "Add outcome conditions; dual ETA reform",
        f"tick{TICK}",
        "SS>INAMI>work_resumption_prime",
    ),
    (
        "lb_chom_wave_exclusions_193k",
        "Chomage exclusion waves 193904 persons 2026-27 by region",
        193904,
        193904,
        "Strong CoA p94 ONEM: BRU 41.7k VL 62.7k WAL 88.6k DG 0.95k; dual euro 1.69→2.45bn; dual RIS +300m",
        "strong",
        "UI recipients losing right in 7 waves",
        "Implement 24-month UI time-limit",
        "Waves Jan2026→Jul2027; ~1/3 to RIS class (INAMI dual hyp)",
        4.0,
        9.0,
        6,
        6.5,
        "Publish outturn per wave; dual CPAS cash",
        f"tick{TICK}",
        "SS>ONEM>chomage_exclusion_waves",
    ),
    (
        "lb_chom_wave_wal_89k",
        "Wallonia UI exclusions 88566 of 193904 (45.7pct)",
        88566,
        88566,
        "Strong CoA regional L5: WAL 88566 largest share; dual RIS/CPAS pressure",
        "strong",
        "Walloon UI recipients in exclusion waves",
        "UI time-limit regional incidence",
        "Disproportionate vs population share class",
        5.0,
        7.5,
        5,
        6.0,
        "Track FOREM activation + CPAS dual",
        f"tick{TICK}",
        "SS>ONEM>chomage_exclusions_WAL",
    ),
    (
        "lb_inami_save_pharma_residual_149m",
        "INAMI pharma savings residual 148.9m still to design 2026",
        148.9e6,
        148.9e6,
        "Strong CoA p84: of 401.9m pharma effort only part proposed; residual 148.9m measures missing",
        "strong",
        "Pharma / patients / hospitals",
        "Keep drugs <=17.3pct of health objective",
        "Price cuts 80.3 antiacids 65.8 lipid 29.4 partial bill 42 TM 27.9 proposed",
        6.0,
        7.0,
        6,
        6.4,
        "Publish residual measure list before booking full 401.9",
        f"tick{TICK}",
        "SS>INAMI>pharma_savings_residual",
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
            f"tick{TICK}: RTW invalidity L5 202.9→1928.7m 2026-29 (recontrol net 34→1045; "
            f"annual-ext 127→869; exits 90.2k) + chomage waves 193904 by region; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_427" for r in rq):
    rq.append(
        {
            "task_id": "rq_427",
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
            "notes": f"Spawned tick{TICK} after RTW L5 + chomage waves; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_427; rq_116 SWA deferred. "
    f"tick{TICK} RTW L5 203-1929m + chom waves 194k."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **RTW invalidity L5 multi-year 2026-2029 + chomage waves**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p84-90 + p94):
  - **RTW total indemnity reduction:** **EUR 202.9 / 643.8 / 1.198 / 1.929bn** (2026-2029)
  - L5: **recontrol net 34.3→1.045bn** (gross 38.7→1.066; staff −4.4→−20.6) · **annual-ext 126.9→868.8m** · solidarité **0→77m** · psycho **2.9→11.3m** · ETA **4.8→22.3m** · WHP **0→6.7m** · maladie fonct table **34/2/54/89m**
  - Exits target **90.204** (recontrol **43.056** + annual-ext **47.148**); dossiers recontrol **19.7k→94k/yr**
  - **CoA flags:** most measures undeveloped; sample excl rates 8.8/23.7pct may not scale; **+48.1m overstate** recontrol 2029; psycho ROI study not for invalids; maladie fonct law not deposited; no chomage spillover modelled
  - Baseline incapacity path **18.347bn 2029** (+28pct vs 2024); invalidity alone **13.4bn / 656k stock**
  - Dual: work-prime cost **28→38.5m** (outside net table); maladie indem cost **16.5→124.3m** vs cotis **51→37m**
  - **Chomage waves p94:** **193.904** exclusions (BRU **41.709** · VL **62.676** · WAL **88.566** · DG **953**); 7 waves Jan2026→Jul2027
  - Pharma residual: of **401.9m** effort **148.9m** still to design (CoA p84)
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_426=done; spawn **rq_427**; ticks={TICK}
- FOI: none new (package primary; residual is legislative design + method audit not opacity)
- Next: prio5 **rq_427**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")
print(f"total_path_m={list(MEAS['total'])} exits={TARGET_EXITS}")
