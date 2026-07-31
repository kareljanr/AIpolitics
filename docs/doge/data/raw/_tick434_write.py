# tick 434: CoA Budget 2026 pension reform L5 multi-year 2027-2030
import csv
import json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T07:45:00Z"
TICK = 434
UNIT = "rq_425"
SRC = "src_ccrek_budget2026_pens_reform_l5"
URL = "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf"

# CoA p82-83 — estimated pension reform savings (m EUR) by measure
# Source: cellule strategique Pensions; CoA Budget 2026
# Years: 2027, 2028, 2029, 2030
MEAS = {
    "bonus_malus": (273, 330, 379, 473),
    "periodes_assimilees": (12, 39, 72, 112),
    "autres_assimilations": (3, 12, 24, 39),
    "age_flexible": (-47, -83, -79, -77),  # cost (negative save)
    "calc_fonctionnaires": (50, 154, 250, 337),
    "extinct_pens_maladie_pub": (94, 171, 245, 302),
    "harmon_carriere_anticip": (136, 274, 313, 323),
    "suppr_perequation_fonct": (64, 90, 156, 156),
    "limit_index_pens_elevees": (97, 152, 201, 253),
    "mesures_diverses": (-3, -3, -5, -3),
    "reforme_calcul_pension": (679, 1136, 1556, 1915),
    "grapa_conditions": (42, 60, 76, 92),
    "alloc_trans_vs_survie": (-36, -3, 29, 55),
    "extinct_pens_menage_sal": (22, 64, 104, 141),
    "convergence_regimes": (125, 125, 125, 125),
    "autres_transitoires": (-25, -78, -103, -99),
    "autres_reformes": (128, 168, 231, 314),
    "total": (807, 1304, 1787, 2229),
}
YEARS = (2027, 2028, 2029, 2030)

# CoA flags: still need legislation for Grapa, alloc transition, menage extinction, assimilées
LEGIS_PENDING = {
    "grapa_conditions",
    "alloc_trans_vs_survie",
    "extinct_pens_menage_sal",
    "periodes_assimilees",
}

LABELS = {
    "bonus_malus": "Nouveau systeme bonus-malus",
    "periodes_assimilees": "Periodes assimilees",
    "autres_assimilations": "Autres assimilations",
    "age_flexible": "Age flexible de la retraite (net cost)",
    "calc_fonctionnaires": "Adaptations calcul pension fonctionnaires",
    "extinct_pens_maladie_pub": "Extinction pension de maladie secteur public",
    "harmon_carriere_anticip": "Harmonisation conditions carriere retraite anticipee",
    "suppr_perequation_fonct": "Suppression perequation pensions fonctionnaires",
    "limit_index_pens_elevees": "Limitation indexation pensions plus elevees (LP 18 Jul 2025)",
    "mesures_diverses": "Mesures diverses",
    "reforme_calcul_pension": "Reforme du calcul de la pension (aggregate block)",
    "grapa_conditions": "Conditions d octroi GRAPA",
    "alloc_trans_vs_survie": "Allocation de transition en remplacement pension de survie",
    "extinct_pens_menage_sal": "Extinction pension de menage regime salaries",
    "convergence_regimes": "Convergence entre les regimes",
    "autres_transitoires": "Autres mesures transitoires",
    "autres_reformes": "Autres reformes",
    "total": "Pension reform total estimated savings",
}

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 pension reform L5 multi-year 2027-2030",
            "url": URL,
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": (
                f"Table p82-83 cellule Pensions; totals 807/1304/1787/2229m; "
                f"delivery risk if laws late; tick{TICK}"
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
# Full L5 for each measure x year (signed save; negative = cost)
for key, vals in MEAS.items():
    if key == "total":
        # totals already exist as bud_pens_reform_save_YYYY — skip re-add if present
        for y, v in zip(YEARS, vals):
            bid = f"bud_pens_reform_l5_total_{y}"
            note = (
                f"Pension reform total estimated savings {v}m {y} CoA p83 "
                f"(dual bud_pens_reform_save_{y}); legislation delivery risk; tick{TICK}"
            )
            if add_bud(bid, "fpd", y, v * 1e6, "budgeted", note, "strong"):
                n_bud += 1
        continue
    for y, v in zip(YEARS, vals):
        bid = f"bud_pens_reform_{key}_{y}"
        legis = " LEGISLATION PENDING CoA." if key in LEGIS_PENDING else ""
        note = (
            f"{LABELS[key]}: estimated save {v}m EUR {y} CoA p82-83 "
            f"(negative=net cost).{legis} tick{TICK}"
        )
        conf = "medium" if key in LEGIS_PENDING else "strong"
        # costs stay signed negative in amount for honesty; use int
        if add_bud(bid, "fpd", y, v * 1e6, "budgeted", note, conf):
            n_bud += 1

# Dual recon note row: sum of components vs total 2027
comp_2027 = sum(v[0] for k, v in MEAS.items() if k != "total")
if add_bud(
    "bud_pens_reform_l5_sum_check_2027",
    "fpd",
    2027,
    comp_2027 * 1e6,
    "derived",
    f"Sum of L5 reform lines 2027 = {comp_2027}m (should match total 807); tick{TICK}",
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

cash = {str(y): int(MEAS["total"][i] * 1e6) for i, y in enumerate(YEARS)}
for key, vals in MEAS.items():
    if key == "total":
        continue
    cash[key] = {str(y): int(vals[i] * 1e6) for i, y in enumerate(YEARS)}

n_cmt = 0
cid = "cmt_pens_reform_l5_2027_2030"
if not any(r.get("commitment_id") == cid for r in cmt):
    cmt.append(
        {
            "commitment_id": cid,
            "title": "Pension reform multi-year L5 savings path 2027-2030",
            "entity_id": "fpd",
            "beneficiary": "Future pension cohorts (net public save; some transitional costs)",
            "legal_basis": "Coalition 31 Jan 2025 pension package; partial LP 18 Jul 2025; many bills still pending 2026",
            "decision_date": "2025-01-31",
            "start_year": "2027",
            "end_year": "2030",
            "total_envelope_eur": str(int(sum(MEAS["total"]) * 1e6)),  # sum annual saves (not NPV)
            "cash_by_year": json.dumps(
                {
                    "totals_m": {str(y): MEAS["total"][i] for i, y in enumerate(YEARS)},
                    "bonus_malus_m": list(MEAS["bonus_malus"]),
                    "reforme_calcul_m": list(MEAS["reforme_calcul_pension"]),
                    "extinct_maladie_pub_m": list(MEAS["extinct_pens_maladie_pub"]),
                    "harmon_carriere_m": list(MEAS["harmon_carriere_anticip"]),
                    "age_flexible_cost_m": list(MEAS["age_flexible"]),
                    "legis_pending": list(LEGIS_PENDING),
                    "coa_note": "SFP models need major updates; late laws risk partial delivery",
                }
            ),
            "remaining_eur": "",
            "status": "planned",
            "evaluation_url": URL,
            "stated_goal": "Contain pension expenditure growth; career length and fairness across regimes",
            "cut_option": "Pass pending laws on time; track mypension communication; dual FPD cash vs budget estimates",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Federal>FPD>pension_reform_2027_2030",
            "notes": f"CoA p82-83 full L5; tick{TICK}",
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


def add_lb(iid, name, annual, total, tco, conf, benef, goal, outcome, abs_s, cost_s, diff, prio, cut, notes, typ="policy"):
    if any(r.get("item_id") == iid for r in lb):
        return False
    lb.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "Federal>FPD>pension_reform_l5",
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
# annual_cost as first full year 2027 save (positive = public save, not spend)
rows = [
    (
        "lb_pens_reform_bonus_malus_273m",
        "Pension bonus-malus system save 273m 2027 path 473m 2030",
        273e6,
        (273 + 330 + 379 + 473) * 1e6,
        "Strong CoA: 273/330/379/473m 2027-30; largest design lever after calc reform",
        "strong",
        "Future retirees (bonus/malus on career)",
        "Reward longer careers / penalise early exit",
        "Depends on timely legislation and mypension UX",
        3,
        7,
        7,
        5.5,
        "Adopt law early 2026; publish distributional impact",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_calc_679m",
        "Pension calculation reform save 679m 2027 path 1.92bn 2030",
        679e6,
        (679 + 1136 + 1556 + 1915) * 1e6,
        "Strong CoA aggregate block 679→1915m; largest single reform line",
        "strong",
        "Future pensioners all regimes",
        "New pension calculation rules",
        "SFP flags major model changes needed",
        2,
        8.5,
        8,
        6.0,
        "Lock parameters; avoid further reestimates like 2026 -64m delay",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_maladie_pub_94m",
        "Public-sector sickness pension extinction save 94m 2027 path 302m",
        94e6,
        (94 + 171 + 245 + 302) * 1e6,
        "Strong CoA: 94/171/245/302m; dual INAMI maladie pension estimates",
        "strong",
        "Civil servants previously on sickness pension path",
        "End public sickness-pension regime",
        "Partial INAMI cross-effects available",
        4,
        6,
        6,
        5.0,
        "Coordinate FPD-INAMI dual; track stock runoff",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_carriere_anticip_136m",
        "Early-retirement career harmonisation save 136m 2027 path 323m",
        136e6,
        (136 + 274 + 313 + 323) * 1e6,
        "Strong CoA: 136/274/313/323m 2027-30",
        "strong",
        "Early retirees across regimes",
        "Harmonise early retirement career conditions",
        "Delivery risk if rules unclear",
        3,
        6.5,
        6,
        5.0,
        "Publish career-condition tables early",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_perequation_64m",
        "Civil-servant pension perequation abolition save 64m 2027 path 156m",
        64e6,
        (64 + 90 + 156 + 156) * 1e6,
        "Strong CoA: 64/90/156/156m",
        "strong",
        "Civil servant pensioners (perequation link)",
        "End automatic wage-linked perequation",
        "Stable from 2029 in table",
        4,
        5.5,
        5,
        4.5,
        "Complete legal end; dual Fonct stock",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_index_high_97m",
        "High-pension indexation cap save 97m 2027 path 253m",
        97e6,
        (97 + 152 + 201 + 253) * 1e6,
        "Strong CoA: 97/152/201/253m; LP 18 Jul 2025 already partially in force",
        "strong",
        "Higher pension recipients",
        "Limit full indexation of highest pensions",
        "Already started via programme law",
        3,
        5.5,
        4,
        4.5,
        "Monitor distributional threshold design",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_age_flex_cost_47m",
        "Flexible retirement age net cost 47m 2027 path ~77m",
        47e6,
        (47 + 83 + 79 + 77) * 1e6,
        "Strong CoA negative saves -47/-83/-79/-77m (policy cost)",
        "strong",
        "Workers choosing flexible pension age",
        "Flexible retirement age option",
        "Offsets other reform saves",
        5,
        4,
        5,
        4.5,
        "Score take-up vs activation; dual bonus-malus",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_menage_extinct_22m",
        "Household pension rate extinction save 22m 2027 path 141m",
        22e6,
        (22 + 64 + 104 + 141) * 1e6,
        "Medium: legislation still pending CoA; dual FPD menage 5.92bn 2025 stock",
        "medium",
        "Household-rate pensioners (new cohorts)",
        "Phase out household pension rate for employees",
        "Needs law; large stock dual menage 5.92bn",
        5,
        5,
        7,
        5.5,
        "Pass law; dual FPD taux menage path",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_grapa_42m",
        "GRAPA entitlement reform save 42m 2027 path 92m",
        42e6,
        (42 + 60 + 76 + 92) * 1e6,
        "Medium: legislation pending CoA; dual GRAPA stock ~120k",
        "medium",
        "GRAPA / IGO elderly minimum recipients",
        "Tighten GRAPA award conditions",
        "Delivery depends on 2026 bills",
        4,
        4,
        6,
        4.5,
        "Legislate; protect true poverty cases",
        f"tick{TICK}",
    ),
    (
        "lb_pens_reform_total_path_2_23bn",
        "Pension reform total save path 0.81 to 2.23bn 2027-2030",
        807e6,
        (807 + 1304 + 1787 + 2229) * 1e6,
        "Strong CoA totals; dual prior lb_pens_reform_2_2bn_2030; 2026 delay -64m already logged",
        "strong",
        "Public finances / future retirees",
        "Coalition multi-year pension package",
        "High delivery risk if laws slip (SFP/CoA warning)",
        3,
        9,
        8,
        6.5,
        "Front-load legislation; quarterly delivery scorecard",
        f"tick{TICK}",
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
            f"tick{TICK}: pension reform L5 2027-2030 (bonus-malus 273→473; calc 679→1915; "
            f"total 807→2229m); legis pending Grapa/menage/survie/assim; rq_116 deferred"
        )

if not any(r.get("task_id") == "rq_426" for r in rq):
    rq.append(
        {
            "task_id": "rq_426",
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
            "notes": f"Spawned tick{TICK} after pens reform L5; rq_116 SWA deferred",
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
    f"Scheduler 60s. Next prio5 rq_426; rq_116 SWA deferred. "
    f"tick{TICK} pens reform L5 807-2229m path."
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsf, extrasaction="ignore")
    w.writeheader()
    w.writerows(ls)

log_entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **pension reform L5 multi-year 2027-2030**)
- Found (strong primary Cour des comptes Budget Etat 2026 p82-83, cellule Pensions):
  - **Total estimated saves:** **EUR 807 / 1.304 / 1.787 / 2.229bn** (2027-2030)
  - Largest lines 2027→2030: **reforme calcul 679→1.915bn** · **bonus-malus 273→473m** · **carriere anticip 136→323m** · **pens maladie pub extinct 94→302m** · **index hautes pens 97→253m** · **perequation 64→156m** · **convergence 125m/yr flat**
  - Net **costs**: age flexible **−47→−77m** · alloc trans vs survie **−36m 2027** then positive · transitoires **−25→−99m**
  - **Legislation still pending (CoA):** GRAPA conditions · survie→transition · menage extinction · periodes assimilees
  - SFP: models need major updates; late laws → partial non-delivery risk (2026 already −64m delay dual)
  - Dual: prior totals bud_pens_reform_save_*; FPD menage 5.92bn stock; FPD transition 63m
- Wrote: sources +1; budgets +{n_bud}; cmt +{n_cmt}; lb +{n_lb}; rq_425=done; spawn **rq_426**; ticks={TICK}
- FOI: none new (package primary; residual is legislative delivery not opacity)
- Next: prio5 **rq_426**; deferred **rq_116** SWA
"""
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
with open(log_path, "ab") as f:
    f.write(log_entry.encode("utf-8"))

print(f"OK tick{TICK} unit={UNIT} bud+{n_bud} cmt+{n_cmt} lb+{n_lb}")
print(f"sum2027={comp_2027} total2027={MEAS['total'][0]}")
