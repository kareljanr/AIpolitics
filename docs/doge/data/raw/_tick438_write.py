# tick 438: CoA Budget 2026 IPP reform annex L5 multi-year 2026-2030 (total + federal + entity split)
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T09:45:00Z"
TICK = 438
UNIT = "rq_429"
SRC = "src_ccrek_budget2026_ipp_annex_l5"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

YEARS = (2026, 2027, 2028, 2029, 2030)

# Annexe 1 p100 — TOTAL incidence (all powers) m EUR; negative = cost / lower receipts
# Source: SPF Finances + Cour des comptes
TOTAL = {
    "incidence_totale": (-420.93, -669.46, -1534.96, -3978.37, -5350.90),  # top block
    "quotite_exemptee": (-531.00, -714.70, -1057.74, -3483.97, -4988.40),
    "bonus_emploi_fiscal": (-60.00, -60.00, -218.00, -218.00, -218.00),
    "csss": (0.0, 0.0, -422.99, -422.99, -422.99),
    "subtotal_I_strict": (-591.00, -774.70, -1698.73, -4124.96, -5629.39),
    "enfants_charge": (6.76, -5.24, 10.86, -30.34, -30.34),
    "parents_isoles": (0.0, 0.0, 0.0, 134.60, 134.60),
    "reduction_ipp_chomage": (257.40, 253.40, 245.90, 215.50, 215.50),
    "extinct_quotient_conjugal": (66.29, 114.59, 145.59, 78.79, 78.79),
    "extinct_quotient_pens": (13.02, 29.02, 47.22, 26.72, 26.72),
    "suppr_red_pens_elevees": (33.95, 33.55, 32.75, 22.35, 22.35),
    "dim_impot_pensions": (0.0, -26.50, -26.50, -26.50, -26.50),
    "deduction_entrepreneurs": (0.0, -89.75, -89.75, -114.40, -114.40),
    "suppr_maj_vers_anticip": (-12.42, -12.42, -12.42, -12.42, -12.42),
    "augm_remun_dirigeants": (19.17, 19.17, 19.17, 19.17, 19.17),
    "sanction_20pct_trav": (10.57, 11.88, 12.44, 12.44, 12.44),
    "sanction_20pct_dir": (18.30, 20.51, 21.48, 21.48, 21.48),
    "droits_auteur": (-142.13, -142.13, -142.13, -142.13, -142.13),
    "heures_sup": (-100.84, -100.84, -100.84, -100.84, -100.84),
    "facteur_correctif_communes": (0.0, 0.0, 0.0, 42.17, 174.07),
    "subtotal_II_autres": (170.07, 105.24, 163.77, 146.59, 278.49),
}

# Federal power only
FED = {
    "pouvoir_federal": (-320.26, -493.70, -1273.80, -3017.01, -4072.12),
    "quotite_exemptee": (-372.20, -501.24, -741.83, -2443.44, -3498.55),
    "bonus_emploi_fiscal": (-60.00, -60.00, -218.00, -218.00, -218.00),
    "csss": (0.0, 0.0, -422.99, -422.99, -422.99),
    "subtotal_I_strict": (-432.20, -561.24, -1382.82, -3084.43, -4139.54),
    "enfants_charge": (4.74, -3.67, 7.61, -21.27, -21.27),
    "parents_isoles": (0.0, 0.0, 0.0, 94.35, 94.35),
    "reduction_ipp_chomage": (180.42, 177.62, 172.36, 151.05, 151.05),
    "extinct_quotient_conjugal": (46.46, 80.32, 102.05, 55.23, 55.23),
    "extinct_quotient_pens": (9.13, 20.34, 33.10, 18.73, 18.73),
    "suppr_red_pens_elevees": (23.80, 23.52, 22.96, 15.67, 15.67),
    "dim_impot_pensions": (0.0, -18.57, -18.57, -18.57, -18.57),
    "deduction_entrepreneurs": (0.0, -62.91, -62.91, -80.19, -80.19),
    "suppr_maj_vers_anticip": (-12.42, -12.42, -12.42, -12.42, -12.42),
    "augm_remun_dirigeants": (13.44, 13.44, 13.44, 13.44, 13.44),
    "sanction_20pct_trav": (10.57, 11.88, 12.44, 12.44, 12.44),
    "sanction_20pct_dir": (18.30, 20.51, 21.48, 21.48, 21.48),
    "droits_auteur": (-99.62, -99.62, -99.62, -99.62, -99.62),
    "heures_sup": (-82.88, -82.88, -82.88, -82.88, -82.88),
    "subtotal_II_autres": (111.93, 67.54, 109.02, 67.42, 67.42),
}

# Bottom recon table entity split (note 2029/2030 totals differ slightly from top block)
ENTITY = {
    "total_recon": (-420.93, -669.46, -1534.96, -4020.54, -5524.97),
    "federal": (-320.26, -493.70, -1273.80, -3017.01, -4072.12),
    "regions": (-75.62, -134.23, -200.92, -780.69, -1131.59),
    "communes": (-25.04, -41.53, -60.24, -222.85, -321.27),
}

LABELS = {
    "incidence_totale": "IPP reform total incidence all powers",
    "quotite_exemptee": "Raise tax-free allowance (quotite exemptee)",
    "bonus_emploi_fiscal": "Fiscal employment bonus reinforce",
    "csss": "Special SSC (CSSS) reduction",
    "subtotal_I_strict": "Subtotal I fiscal reform strictu sensu",
    "enfants_charge": "Dependent children reform",
    "parents_isoles": "Single-parent supplement only true isolés",
    "reduction_ipp_chomage": "Phase-out / cut tax credit on UI benefits",
    "extinct_quotient_conjugal": "Extinguish marital quotient by 2029",
    "extinct_quotient_pens": "Extinguish marital quotient for pensioners",
    "suppr_red_pens_elevees": "Phase out tax reduction on high pensions",
    "dim_impot_pensions": "Lower tax on pensions (cost)",
    "deduction_entrepreneurs": "Entrepreneur deduction (cost)",
    "suppr_maj_vers_anticip": "Abolish advance-payment tax surcharge",
    "augm_remun_dirigeants": "Higher company-director remuneration (revenue)",
    "sanction_20pct_trav": "20pct rule sanction -7.5pp workers share",
    "sanction_20pct_dir": "20pct rule sanction -7.5pp directors share",
    "droits_auteur": "Copyright income tax regime (cost)",
    "heures_sup": "Overtime tax treatment (cost)",
    "facteur_correctif_communes": "Communal corrective factor",
    "subtotal_II_autres": "Subtotal II other accompanying measures",
    "pouvoir_federal": "Federal power total IPP reform incidence",
}

# Employment rate path (p10) — credibility dual for return-effects
EMP_PATH = {
    "coalition_target": (73.0, 74.0, 75.0, 76.0, 78.0),  # 2025-2029
    "bfp_jun2025": (72.4, 72.6, 73.0, 73.5, 74.1),
    "bfp_feb2026": (72.8, 72.9, 73.3, 73.9, 74.3),
    "years": (2025, 2026, 2027, 2028, 2029),
}

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 Annexe 1 IPP reform L5 multi-year 2026-2030",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof + SPF Finances",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"p100 full measure matrix total+federal+entity split; "
                f"2030 total cost ~5.35-5.52bn class; dual gap_ipp_reform_aurora_l5 partial; tick{TICK}"
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

# Total (all powers) L5
for key, vals in TOTAL.items():
    for i, y in enumerate(YEARS):
        v = vals[i]
        if v == 0.0 and key in ("csss", "parents_isoles", "dim_impot_pensions", "deduction_entrepreneurs", "facteur_correctif_communes"):
            # still record zeros for series continuity on multi-year packages that start later
            pass
        conf = "medium"  # Aurora model + timing flags
        if add_bud(
            f"bud_ipp_l5_tot_{key}_{y}",
            "fod_finance",
            y,
            v * 1e6,
            "budgeted",
            (
                f"{LABELS.get(key, key)} TOTAL all-powers {v}m EUR {y} CoA p100 annex "
                f"(negative=cost/lower tax). dual cmt_ipp_reform; tick{TICK}"
            ),
            conf,
        ):
            n_bud += 1

# Federal L5
for key, vals in FED.items():
    for i, y in enumerate(YEARS):
        v = vals[i]
        if add_bud(
            f"bud_ipp_l5_fed_{key}_{y}",
            "fod_finance",
            y,
            v * 1e6,
            "budgeted",
            (
                f"{LABELS.get(key, key)} FEDERAL power {v}m EUR {y} CoA p100 "
                f"(negative=cost). tick{TICK}"
            ),
            "medium",
        ):
            n_bud += 1

# Entity split recon
for key, vals in ENTITY.items():
    ent = {
        "total_recon": "gg_belgium",
        "federal": "sec_federal",
        "regions": "sec_s1312",
        "communes": "sec_s1313",
    }[key]
    for i, y in enumerate(YEARS):
        v = vals[i]
        note = (
            f"IPP reform incidence entity-split {key} {v}m {y} CoA p100 bottom recon; "
            f"note top-block 2029/30 totals differ slightly (-3978/-5351 vs -4021/-5525); tick{TICK}"
        )
        if add_bud(
            f"bud_ipp_l5_entity_{key}_{y}",
            ent,
            y,
            v * 1e6,
            "budgeted",
            note,
            "medium",
        ):
            n_bud += 1

# Cumulative cost class (sum of annual total recon absolute costs where negative)
cum = 0.0
for i, y in enumerate(YEARS):
    cum += ENTITY["total_recon"][i]
    if add_bud(
        f"bud_ipp_l5_cum_total_{y}",
        "fod_finance",
        y,
        cum * 1e6,
        "derived",
        f"Cumulative sum of annual total-recon incidences through {y} = {cum:.2f}m (not NPV); tick{TICK}",
        "medium",
    ):
        n_bud += 1

# Employment rate path (store as basis points * 100 for amount_eur = rate*100 so 7280 = 72.80%)
for i, y in enumerate(EMP_PATH["years"]):
    for series, vals in (
        ("coalition", EMP_PATH["coalition_target"]),
        ("bfp_jun2025", EMP_PATH["bfp_jun2025"]),
        ("bfp_feb2026", EMP_PATH["bfp_feb2026"]),
    ):
        rate = vals[i]
        if add_bud(
            f"bud_emp_rate_{series}_{y}",
            "gg_belgium",
            y,
            int(round(rate * 100)),  # e.g. 7290 = 72.90%
            "estimate",
            (
                f"Employment rate 20-64 {series} {rate}pct {y} CoA p10 "
                f"(amount_eur=rate*100; coalition target 78pct 2029 vs BFP Feb2026 74.3); tick{TICK}"
            ),
            "strong" if series.startswith("bfp") else "medium",
        ):
            n_bud += 1
    gap = EMP_PATH["coalition_target"][i] - EMP_PATH["bfp_feb2026"][i]
    if add_bud(
        f"bud_emp_rate_gap_coalition_bfp_{y}",
        "gg_belgium",
        y,
        int(round(gap * 100)),
        "derived",
        f"Employment rate gap coalition target minus BFP Feb2026 = {gap:.1f}pp {y}; return-effect credibility; tick{TICK}",
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
cid = "cmt_ipp_reform_l5_2026_2030"
if not any(r.get("commitment_id") == cid for r in cmt):
    cmt.append(
        {
            "commitment_id": cid,
            "title": "IPP reform multi-year L5 annex path 2026-2030 (~5.4-5.5bn cum class)",
            "entity_id": "fod_finance",
            "beneficiary": "Workers / entrepreneurs / isolés / dual regions communes",
            "legal_basis": "DOC 56/1243 + summer 2025 accord; Aurora model; CoA Annex 1 Budget 2026",
            "decision_date": "2025-07-01",
            "start_year": "2026",
            "end_year": "2030",
            "total_envelope_eur": str(int(abs(ENTITY["total_recon"][-1]) * 1e6)),
            "cash_by_year": json.dumps(
                {
                    "total_top_m": {str(y): TOTAL["incidence_totale"][i] for i, y in enumerate(YEARS)},
                    "total_recon_m": {str(y): ENTITY["total_recon"][i] for i, y in enumerate(YEARS)},
                    "federal_m": {str(y): FED["pouvoir_federal"][i] for i, y in enumerate(YEARS)},
                    "regions_m": {str(y): ENTITY["regions"][i] for i, y in enumerate(YEARS)},
                    "communes_m": {str(y): ENTITY["communes"][i] for i, y in enumerate(YEARS)},
                    "quotite_tot_m": list(TOTAL["quotite_exemptee"]),
                    "chomage_tax_cut_tot_m": list(TOTAL["reduction_ipp_chomage"]),
                    "droits_auteur_tot_m": list(TOTAL["droits_auteur"]),
                    "heures_sup_tot_m": list(TOTAL["heures_sup"]),
                    "csss_tot_m": list(TOTAL["csss"]),
                    "coa_note": "Top vs bottom 2029/30 totals differ; H1 PP deferral and Aurora interactions residual",
                }
            ),
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": URL,
            "stated_goal": "Raise net income from work; low/median wages; broaden shoulders side-measures",
            "cut_option": "Reestimate BA2026; dual chomage tax-credit phase-out delivery; protect true isolés",
            "source_id": SRC,
            "confidence": "medium",
            "hierarchy_path": "Federal>tax>IPP_reform_l5",
            "notes": f"CoA p100 full annex; dual cmt_ipp_reform_2026_30; partial answer gap_ipp_reform_aurora_l5; tick{TICK}",
        }
    )
    n_cmt += 1

# update prior commitment notes if present
for r in cmt:
    if r.get("commitment_id") == "cmt_ipp_reform_2026_30":
        r["notes"] = (r.get("notes") or "") + f" | tick{TICK}: full annex L5 in cmt_ipp_reform_l5_2026_2030"
        r["confidence"] = "medium"

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
# annual_cost as absolute of 2030 or first material year cost
rows = [
    (
        "lb_ipp_reform_path_5_5bn_l5",
        "IPP reform total path to ~5.4-5.5bn annual cost 2030 L5",
        5350.9e6,
        abs(sum(ENTITY["total_recon"])) * 1e6,
        "Medium CoA annex: annual -421→-5351 (top) / -5525 (recon); federal -320→-4072; dual prior 5.6bn class",
        "medium",
        "Workers low/median wages dual regions communes",
        "Raise net work income progressive reform",
        "H1 deferral + Aurora interaction residual FOI",
        3.0,
        9.5,
        7,
        6.8,
        "Lock parameters; quarterly cash vs model; dual chomage credit",
        f"tick{TICK}",
        "Federal>tax>IPP_reform_l5",
    ),
    (
        "lb_ipp_quotite_path_5bn",
        "Tax-free allowance raise path to ~5.0bn cost 2030",
        4988.4e6,
        abs(sum(TOTAL["quotite_exemptee"])) * 1e6,
        "Medium CoA: largest single line -531→-4988 total; federal -372→-3499; stretch drives 2029 cliff",
        "medium",
        "All personal income taxpayers",
        "Raise quotité exemptée",
        "2029 jump after multi-year phase",
        2.5,
        9.0,
        6,
        6.4,
        "Publish distributional tables; dual regional share",
        f"tick{TICK}",
        "Federal>tax>quotite_exemptee",
    ),
    (
        "lb_ipp_chomage_tax_cut_257m",
        "Cut/phase UI tax credit save ~257m 2026 path 216m",
        257.4e6,
        sum(TOTAL["reduction_ipp_chomage"]) * 1e6,
        "Strong CoA annex positive revenue 257→216; dual chomage time-limit reform 1.69bn",
        "strong",
        "UI recipients (tax credit reduced)",
        "End preferential tax treatment of unemployment benefits",
        "Aligns with benefit time-limit; social stack",
        4.0,
        6.5,
        4,
        5.2,
        "Track dual with RIS spillover compensation",
        f"tick{TICK}",
        "Federal>tax>UI_tax_credit",
    ),
    (
        "lb_ipp_droits_auteur_142m",
        "Copyright income regime cost 142m/yr flat",
        142.13e6,
        142.13e6 * 5,
        "Strong CoA annex -142m/yr total all years; federal -99.6m; dual creative sector TE",
        "strong",
        "Copyright income recipients",
        "Preferential tax on droits d auteur",
        "Stable annual cost in table",
        6.0,
        6.0,
        4,
        5.6,
        "Cap regime; dual overtime -101m package",
        f"tick{TICK}",
        "Federal>tax>droits_auteur",
    ),
    (
        "lb_ipp_heures_sup_101m",
        "Overtime tax treatment cost 101m/yr flat",
        100.84e6,
        100.84e6 * 5,
        "Strong CoA -100.8m/yr total; federal -82.9; dual ONSS SSC overtime cost 43m",
        "strong",
        "Workers/employers using voluntary overtime",
        "Preferential tax on overtime hours",
        "Dual labour reform 360h voluntary cap",
        5.0,
        5.5,
        4,
        5.0,
        "Score additionality vs wage bill",
        f"tick{TICK}",
        "Federal>tax>heures_sup",
    ),
    (
        "lb_ipp_conjugal_extinct_path",
        "Marital quotient extinction path +66→+79m (revenue)",
        66.29e6,
        sum(TOTAL["extinct_quotient_conjugal"]) * 1e6,
        "Strong CoA positive 66/115/146/79/79; dual pensioner branch separate",
        "strong",
        "Two-earner / one-earner couples (phase-out)",
        "End marital quotient by 2029",
        "Peaks mid-path then stabilises",
        3.5,
        5.5,
        5,
        4.8,
        "Publish household distributional impact",
        f"tick{TICK}",
        "Federal>tax>quotient_conjugal",
    ),
    (
        "lb_ipp_entity_split_regions_1_13bn",
        "IPP reform regional share cost path to 1.13bn 2030",
        1131.59e6,
        abs(sum(ENTITY["regions"])) * 1e6,
        "Medium CoA recon: regions -76→-1132; communes -25→-321; federal -320→-4072",
        "medium",
        "Regional treasuries via IPP add-ons",
        "Share personal tax reform cost across powers",
        "2029 cliff after stretch",
        4.0,
        8.0,
        6,
        6.2,
        "Coordinate Entity I/II; dual LSF",
        f"tick{TICK}",
        "Federal>tax>IPP_entity_split",
    ),
    (
        "lb_ipp_csss_cut_423m_from_2028",
        "CSSS cut inside IPP package 423m from 2028",
        422.99e6,
        422.99e6 * 3,
        "Medium CoA annex; dual ONSS CSSS 415m notif path; starts 2028 in table",
        "medium",
        "Workers paying special SSC",
        "Reduce CSSS as part of tax reform",
        "Aligned with bonus emploi fiscal boost 2028",
        4.0,
        7.0,
        5,
        5.5,
        "Publish interaction with progressive rates",
        f"tick{TICK}",
        "Federal>tax>csss_in_ipp",
    ),
    (
        "lb_emp_rate_gap_78_vs_74",
        "Coalition employment-rate 78pct 2029 vs BFP 74.3 (gap 3.7pp)",
        370,
        370,
        "Strong CoA p10: coalition 73→78 vs BFP Feb2026 72.8→74.3; return-effects overstated class",
        "strong",
        "Labour market policy credibility",
        "Raise employment rate to 80pct class path",
        "NBB 10-20pct re-employment vs gov 1/3 hyp dual",
        7.5,
        6.0,
        8,
        7.2,
        "Rebase return-effects on BFP/NBB; dual chomage waves",
        f"tick{TICK}",
        "BE>labour>employment_rate_target",
    ),
    (
        "lb_ipp_parents_isoles_135m",
        "True single-parent supplement +135m from 2029",
        134.6e6,
        134.6e6 * 2,
        "Strong CoA: only true isolés; federal 94.35; starts 2029",
        "strong",
        "Genuine single parents",
        "Target isolé supplement away from false isolés",
        "Revenue-positive targeting",
        3.0,
        5.0,
        4,
        4.2,
        "Define administrative test early",
        f"tick{TICK}",
        "Federal>tax>parents_isoles",
    ),
]
for args in rows:
    if add_lb(*args):
        n_lb += 1

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

# --- foi_queue: note partial public fill on gap_ipp ---
with open(DATA / "foi_queue.csv", encoding="utf-8", newline="") as f:
    foi = list(csv.DictReader(f))
    ff = list(foi[0].keys())
for r in foi:
    if r.get("gap_id") == "gap_ipp_reform_aurora_l5":
        r["updated_utc"] = NOW
        r["notes"] = (
            (r.get("notes") or "")
            + f" | tick{TICK}: CoA p100 annex measure-by-measure EUR now public; residual Aurora interactions/H1 cash/model still FOI ready"
        )
        r["what_is_missing"] = (
            "Aurora model code/assumptions; H1 2026 PP deferral cash path; interaction with chomage time-limit and centimes; "
            "reconcile top vs bottom 2029/30 annex totals"
        )
with open(DATA / "foi_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ff, extrasaction="ignore")
    w.writeheader()
    w.writerows(foi)

# --- research_queue ---
with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())

for r in rq:
    if r.get("task_id") == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = (
            f"tick{TICK}: IPP reform annex L5 full (total -421→-5351; federal -320→-4072; "
            f"quotite -531→-4988; entity split) + emp-rate gap 78 vs 74.3; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_430" for r in rq):
    rq.append(
        {
            "task_id": "rq_430",
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
            "notes": f"Spawned tick{TICK} after IPP annex L5; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_430; rq_116 SWA deferred. "
    f"tick{TICK} IPP annex L5 -421 to -5.4bn path."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **IPP reform annex L5 multi-year 2026-2030**)
- Found (medium-strong primary Cour des comptes Budget Etat 2026 p100 Annexe 1 + p10 emp path):
  - **Total incidence (top):** **-421 / -669 / -1.535 / -3.978 / -5.351bn** (2026-2030)
  - **Federal:** **-320 / -494 / -1.274 / -3.017 / -4.072bn**
  - **Entity recon bottom:** total **-421→-5.525**; regions **-76→-1.132**; communes **-25→-321** (2029/30 top vs bottom totals differ slightly)
  - Largest cost: **quotité exemptée -531→-4.988bn**; CSSS **-423m from 2028**; droits d'auteur **-142m/yr**; heures sup **-101m/yr**; bonus emploi fiscal **-60→-218**
  - Revenue side: **UI tax-credit cut +257→+216**; conjugal extinction **+66→+79**; high-pension red. phase **+34→+22**; true isolés **+135 from 2029**
  - **Employment-rate credibility:** coalition **73→78% 2025-29** vs BFP Feb2026 **72.8→74.3** (gap **3.7pp 2029**); dual return-effects overstated
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; foi gap_ipp note partial; rq_429=done; spawn **rq_430**; ticks={TICK}
- FOI: gap_ipp_reform_aurora_l5 residual narrowed (annex public; Aurora interactions/H1 still ready human send)
- Next: prio5 **rq_430**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")
print(f"2030 total top={TOTAL['incidence_totale'][-1]} recon={ENTITY['total_recon'][-1]} fed={FED['pouvoir_federal'][-1]}")
