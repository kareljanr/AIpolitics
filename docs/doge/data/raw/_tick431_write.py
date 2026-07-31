# tick 431: SPP Integration sociale / federal CPAS DIS+RIS grants 2026 CoA
import csv, json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T06:15:00Z"
TICK = 431
UNIT = "rq_422"
SRC = "src_ccrek_budget2026_spp_is_cpas"

# CoA Budget Etat 2026 Table p67 — millions EUR
dis_base = 1_841.7e6
dis_index = -36.8e6
dis_comp = 300.0e6
dis_reform = -16.6e6
dis_wait = -3.8e6
dis_total = 2_084.5e6

loi65_base = 179.8e6
loi65_index = -3.6e6
loi65_reform = -16.9e6
loi65_wait = -2.9e6
loi65_total = 156.4e6

total_base = 2_021.5e6
total_index = -40.4e6
total_comp = 300.0e6
total_reform = -33.5e6
total_wait = -6.7e6
total_2026 = 2_240.9e6

# Compensation path SPP IS calc vs budget notifications
comp_spp = {2026: 295.7e6, 2027: 819.8e6, 2028: 887.8e6, 2029: 709.3e6}
comp_budget = {2026: 300.0e6, 2027: 300.0e6, 2028: 302.3e6, 2029: 342.6e6}
new_ris_2026 = 52_400  # approx persons from unemployment
# regular cost of inflow vs top-up compensation
regular_inflow = {2026: 212.1e6, 2027: 638.7e6, 2028: 723.9e6, 2029: 556.1e6}
aug_comp = {2026: 83.6e6, 2027: 181.1e6, 2028: 163.9e6, 2029: 153.2e6}

dossier_fee = 518  # EUR per RIS beneficiary normal
dossier_fee_temp = 1036  # for compensated cohort 2026 H1

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "Cour des comptes Budget Etat 2026 section 44 SPP Integration sociale DIS CPAS RIS",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-02",
            "source_class": "primary_audit",
            "notes": f"DIS 2084.5m + loi1965 156.4m = 2240.9m 2026; +300m CPAS compensation unemployment reform; tick{TICK}",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "entities.csv", encoding="utf-8", newline="") as f:
    ent = list(csv.DictReader(f))
    ef = list(ent[0].keys())
if not any(r.get("entity_id") == "spp_is" for r in ent):
    ent.append(
        {
            "entity_id": "spp_is",
            "name_nl": "POD Maatschappelijke Integratie POD MI",
            "name_fr": "SPP Integration sociale SPP IS",
            "name_en": "PPS Social Integration",
            "level": "agency",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://www.mi-is.be",
            "foi_email": "",
            "foi_postal": "https://www.ibz.be/nl/openbaarheid-van-bestuur",
            "notes": f"Federal CPAS grants DIS/RIS + loi 1965 2.241bn 2026; dual local CPAS residual; tick{TICK}",
        }
    )
with open(DATA / "entities.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ef, extrasaction="ignore")
    w.writeheader()
    w.writerows(ent)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add(bid, entity, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return
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


add(
    "bud_spp_is_cpas_total_2026",
    "spp_is",
    2026,
    total_2026,
    "budgeted",
    f"Federal CPAS grants DIS+loi1965 total 2240.9m 2026 CoA table; tick{TICK}",
)
add(
    "bud_spp_is_dis_ris_2026",
    "spp_is",
    2026,
    dis_total,
    "budgeted",
    f"DIS (revenu integration / leefloon federal share) 2084.5m 2026; tick{TICK}",
)
add(
    "bud_spp_is_loi1965_2026",
    "spp_is",
    2026,
    loi65_total,
    "budgeted",
    f"Loi 1965 social aid (equivalent RIS) federal share 156.4m 2026; tick{TICK}",
)
add(
    "bud_spp_is_dis_base_2026",
    "spp_is",
    2026,
    dis_base,
    "budgeted",
    f"DIS base CM Jul 2025 1841.7m before index/comp/reforms; tick{TICK}",
)
add(
    "bud_spp_is_comp_unemp_2026",
    "spp_is",
    2026,
    dis_comp,
    "budgeted",
    f"CPAS compensation +300m 2026 for unemployment-to-RIS inflow (~52400 persons class); open envelope; tick{TICK}",
)
add(
    "bud_spp_is_ris_reform_save_2026",
    "spp_is",
    2026,
    abs(total_reform),
    "budgeted_saving",
    f"RIS reform to montant integration save -33.5m 2026 (DIS -16.6 + loi1965 -16.9); tick{TICK}",
)
add(
    "bud_spp_is_wait5y_save_2026",
    "spp_is",
    2026,
    abs(total_wait),
    "budgeted_saving",
    f"5-year wait for social aid save -6.7m 2026; tick{TICK}",
)
add(
    "bud_spp_is_index_corr_2026",
    "spp_is",
    2026,
    abs(total_index),
    "budgeted",
    f"Index correction -40.4m on DIS+loi1965 base; tick{TICK}",
)
# multi-year compensation path
for y, a in comp_budget.items():
    add(
        f"bud_spp_is_comp_envelope_{y}",
        "spp_is",
        y,
        a,
        "budgeted",
        f"CPAS unemp compensation budget envelope {a/1e6:.1f}m {y} (SPP IS calc {comp_spp[y]/1e6:.1f}m); tick{TICK}",
        conf="strong" if y == 2026 else "medium",
    )
for y, a in regular_inflow.items():
    add(
        f"bud_spp_is_regular_inflow_cost_{y}",
        "spp_is",
        y,
        a,
        "projection",
        f"SPP IS regular federal cost of unemp-to-RIS inflow {a/1e6:.1f}m {y}; tick{TICK}",
        conf="medium",
    )
add(
    "bud_spp_is_new_ris_persons_2026",
    "spp_is",
    2026,
    new_ris_2026,
    "beneficiary_stock",
    f"Expected ~52400 new RIS from unemployment limitation 2026 (CoA footnote); tick{TICK}",
)
add(
    "bud_spp_is_dossier_fee_2026",
    "spp_is",
    2026,
    dossier_fee,
    "unit_cost_eur",
    f"CPAS dossier fee 518 EUR/RIS beneficiary/year (temp 1036 for compensated H1-2026 cohort); tick{TICK}",
)

with open(DATA / "budgets.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bf, extrasaction="ignore")
    w.writeheader()
    w.writerows(bud)

with open(DATA / "commitments.csv", encoding="utf-8", newline="") as f:
    cmt = list(csv.DictReader(f))
    cf = list(cmt[0].keys())


def addc(cid, **kw):
    if any(r["commitment_id"] == cid for r in cmt):
        return
    row = {k: "" for k in cf}
    row.update(kw)
    cmt.append(row)


addc(
    "cmt_spp_is_cpas_dis_2026",
    title="Federal CPAS grants DIS+loi1965 (RIS/leefloon federal share) 2026",
    entity_id="spp_is",
    beneficiary="CPAS/OCMW (pass-through to RIS and equivalent social aid beneficiaries)",
    legal_basis="Loi 26 mai 2002 DIS + loi 2 avril 1965; federal 55-70pct of RIS",
    decision_date="2025-12-01",
    start_year="2026",
    end_year="2026",
    total_envelope_eur=str(int(total_2026)),
    cash_by_year=json.dumps(
        {
            "total_2026": int(total_2026),
            "DIS_2026": int(dis_total),
            "loi1965_2026": int(loi65_total),
            "base_pre_measures": int(total_base),
            "compensation_unemp": int(total_comp),
            "ris_reform_save": int(total_reform),
            "wait5y_save": int(total_wait),
            "index_corr": int(total_index),
            "new_ris_persons_class": new_ris_2026,
            "comp_path_budget": {str(y): int(a) for y, a in comp_budget.items()},
            "comp_path_spp_is_calc": {str(y): int(a) for y, a in comp_spp.items()},
            "note": "Federal share only; CPAS fund residual 30-45pct of RIS locally — not full beneficiary cash",
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
    stated_goal="Federal co-financing of CPAS integration income and social aid",
    cut_option="Core safety net; dual unemp reform spillover risk; open envelope compensation may need top-ups 2027+",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="Federal>SPP_IS>CPAS_DIS_RIS",
    notes=f"2.241bn total; DIS 2.085bn includes +300m compensation; full RIS cash to people higher (local share); tick{TICK}",
)

addc(
    "cmt_spp_is_comp_unemp_ris_2026_29",
    title="CPAS compensation for unemployment-to-RIS inflow path 2026-2029",
    entity_id="spp_is",
    beneficiary="CPAS receiving long-term unemployed after benefit time-limit",
    legal_basis="Coalition unemp reform + SPP IS compensation scheme",
    decision_date="2025-07-18",
    start_year="2026",
    end_year="2029",
    total_envelope_eur=str(int(sum(comp_budget.values()))),
    cash_by_year=json.dumps(
        {
            "budget_envelope": {str(y): int(a) for y, a in comp_budget.items()},
            "spp_is_calc": {str(y): int(a) for y, a in comp_spp.items()},
            "regular_inflow_cost": {str(y): int(a) for y, a in regular_inflow.items()},
            "augmented_comp": {str(y): int(a) for y, a in aug_comp.items()},
            "gap_2027_m": int(comp_spp[2027] - comp_budget[2027]),
            "hypothesis": "1/3 unemp to RIS; CoA flags understate risk",
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
    stated_goal="Shield local finances from unemp time-limit spillover",
    cut_option="Open envelope; 2027+ budget understates SPP IS calc by ~0.5bn/yr class",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="Federal>SPP_IS>compensation_unemp_RIS",
    notes=f"Budget 300m flat 2026-27 vs SPP IS 296/820m; dual ONEM reform; tick{TICK}",
)

with open(DATA / "commitments.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction="ignore")
    w.writeheader()
    w.writerows(cmt)

with open(DATA / "leaderboard.csv", encoding="utf-8", newline="") as f:
    lb = list(csv.DictReader(f))
    lf = list(lb[0].keys())


def addl(iid, **kw):
    if any(r["item_id"] == iid for r in lb):
        return
    row = {k: "" for k in lf}
    row.update(kw)
    lb.append(row)


addl(
    "lb_spp_is_cpas_2_24bn_2026",
    name="Federal CPAS grants DIS+loi1965 2.24bn 2026",
    level="federal",
    type="social_transfer",
    hierarchy_path="Federal>SPP_IS>CPAS_grants_2026",
    annual_cost_eur=str(int(total_2026)),
    total_cost_eur=str(int(total_2026)),
    tco_notes="Strong CoA: 2240.9m (DIS 2084.5 + loi1965 156.4); federal 55-70pct of RIS only — full beneficiary cash higher",
    confidence="strong",
    source_id=SRC,
    beneficiaries="CPAS then RIS/equivalent social aid recipients",
    stated_goal="Federal co-finance of local integration income",
    measured_outcome="Core safety net; dual unemp reform +300m compensation",
    absurdity_score="2",
    cost_score="9.0",
    difficulty="5",
    priority_index="5.9",
    cut_proposal="Core; publish full RIS cash stock (federal+local); dual CPAS unit cost",
    status="seed",
    notes=f"tick{TICK} not pure waste",
)

addl(
    "lb_spp_is_dis_ris_2_08bn_2026",
    name="Federal DIS/RIS co-finance 2.08bn 2026",
    level="federal",
    type="social_transfer",
    hierarchy_path="Federal>SPP_IS>DIS_RIS_2026",
    annual_cost_eur=str(int(dis_total)),
    total_cost_eur=str(int(dis_total)),
    tco_notes="Strong: 2084.5m DIS including +300m unemp compensation and reform/wait adjustments",
    confidence="strong",
    source_id=SRC,
    beneficiaries="RIS (leefloon) via CPAS",
    stated_goal="Revenu d integration sociale federal share",
    measured_outcome="Base 1841.7 +comp 300 -reform/wait/index; ~52400 new from unemp class",
    absurdity_score="2",
    cost_score="9.0",
    difficulty="5",
    priority_index="5.9",
    cut_proposal="Track activation rates; dual DG HAN/ARR overlap residual",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_spp_is_comp_300m_2026",
    name="CPAS unemp-to-RIS compensation 300m 2026",
    level="federal",
    type="transfer",
    hierarchy_path="Federal>SPP_IS>comp_unemp_2026",
    annual_cost_eur=str(int(dis_comp)),
    total_cost_eur=str(int(dis_comp)),
    tco_notes="Strong budget 300m 2026; SPP IS calc 295.7m OK 2026 but 820m 2027 vs budget 300 — open envelope risk",
    confidence="strong",
    source_id=SRC,
    beneficiaries="CPAS absorbing long-term unemployed",
    stated_goal="100pct RIS compensation H1-2026 wave then taper; +15pct later entrants",
    measured_outcome="Hypothesis 1/3 unemp to RIS may understate (CoA/VVSG)",
    absurdity_score="5",
    cost_score="7.5",
    difficulty="4",
    priority_index="6.0",
    cut_proposal="Reconcile 2027+ envelope with SPP IS; dual ONEM outflow KPIs",
    status="seed",
    notes=f"tick{TICK} fiscal risk if envelope insufficient",
)

addl(
    "lb_spp_is_loi1965_156m_2026",
    name="Loi 1965 social aid federal share 156m 2026",
    level="federal",
    type="social_transfer",
    hierarchy_path="Federal>SPP_IS>loi1965_2026",
    annual_cost_eur=str(int(loi65_total)),
    total_cost_eur=str(int(loi65_total)),
    tco_notes="Strong: 156.4m after reform/wait; equivalent RIS for non-population-register cases",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Indigents via CPAS outside DIS perimeter",
    stated_goal="Federal refund of loi 1965 social aid costs",
    measured_outcome="Smaller than DIS; dual DIS reforms apply",
    absurdity_score="2",
    cost_score="6.5",
    difficulty="5",
    priority_index="4.7",
    cut_proposal="Monitor 5y wait impact; dual migration perimeter",
    status="seed",
    notes=f"tick{TICK}",
)

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r["task_id"] == "rq_422":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = f"tick{TICK}: SPP IS CPAS DIS+loi1965 2.241bn 2026 +comp 300m; spawn rq_423"
if not any(r["task_id"] == "rq_423" for r in rq):
    rq.append(
        {
            "task_id": "rq_423",
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
            "notes": f"Spawned tick{TICK} after SPP IS CPAS 2.24bn; rq_116 SWA deferred",
        }
    )
with open(DATA / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rf, extrasaction="ignore")
    w.writeheader()
    w.writerows(rq)

with open(DATA / "loop_state.csv", encoding="utf-8", newline="") as f:
    st = list(csv.DictReader(f))
    sfields = list(st[0].keys())
st[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "notes": f"Scheduler 60s. Next prio5 rq_423; rq_116 SWA deferred. tick{TICK} SPP IS CPAS 2.24bn +comp 300m.",
    }
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, extrasaction="ignore")
    w.writeheader()
    w.writerows(st)

print("OK", TICK, "total", int(total_2026), "DIS", int(dis_total), "loi65", int(loi65_total))
print("bud", len(bud), "cmt", len(cmt), "lb", len(lb))
