# tick 428: FPD PensionStat L5 menage + transition + retraite/survie split
import csv, json, openpyxl
from pathlib import Path
from collections import defaultdict

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T04:45:00Z"
TICK = 428
UNIT = "rq_419"
SRC = "src_pensionstat_depenses_2025"

wb = openpyxl.load_workbook(
    Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw\pensionstat_data_2025_fr.xlsx"),
    data_only=True,
)
ws = wb["Dépenses_annuelles"]

by_year = defaultdict(float)
by_regime_y = defaultdict(float)
by_type_y = defaultdict(float)
menage_y = defaultdict(float)
trans_y = defaultdict(float)
autres_y = defaultdict(float)
for row in ws.iter_rows(min_row=2, values_only=True):
    y, cad, reg, typ, taux, name, amt = row
    if amt is None:
        continue
    by_year[y] += amt
    by_regime_y[(y, reg)] += amt
    by_type_y[(y, typ)] += amt
    if taux == "Taux Marié":
        menage_y[(y, reg)] += amt
    if name and "transition" in (name or "").lower():
        trans_y[(y, reg)] += amt
    if name and "Autres prestations" in (name or ""):
        autres_y[(y, reg, typ)] += amt

menage_2025_sal = menage_y[(2025, "Sal.")]
menage_2025_ind = menage_y[(2025, "Ind.")]
menage_2025 = menage_2025_sal + menage_2025_ind
trans_2025 = sum(v for (y, r), v in trans_y.items() if y == 2025)
retraite_2025 = by_type_y[(2025, "Pension de Retraite")]
survie_2025 = by_type_y[(2025, "Pension de Survie")]

menage_path = {y: sum(v for (yy, r), v in menage_y.items() if yy == y) for y in range(2019, 2026)}
trans_path = {y: sum(v for (yy, r), v in trans_y.items() if yy == y) for y in range(2019, 2026)}
retraite_path = {y: by_type_y[(y, "Pension de Retraite")] for y in range(2019, 2026)}
survie_path = {y: by_type_y[(y, "Pension de Survie")] for y in range(2019, 2026)}
total_path = {y: by_year[y] for y in range(2019, 2026)}

tot_nat = 0
for row in wb["Pensionnés_nationalité"].iter_rows(min_row=2, values_only=True):
    if row[0] == 2025:
        tot_nat += row[2] or 0
grapa_n = 0
for row in wb["GRAPA"].iter_rows(min_row=2, values_only=True):
    if row[0] == 2025 and row[8]:
        grapa_n += row[8]

autres_sal_ret = autres_y.get((2025, "Sal.", "Pension de Retraite"), 0)
autres_ind_ret = autres_y.get((2025, "Ind.", "Pension de Retraite"), 0)
ts = trans_y[(2025, "Sal.")]
ti = trans_y[(2025, "Ind.")]
tf = trans_y[(2025, "Fonct.")]

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
found = False
for r in src:
    if r["source_id"] == SRC:
        r["notes"] = (r.get("notes") or "") + f" | tick{TICK} L5 menage 5.92bn transition 63m retraite/survie split"
        found = True
        break
if not found:
    src.append(
        {
            "source_id": SRC,
            "title": "PensionStat.be depenses annuelles legales 2019-2025",
            "url": "https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
            "publisher": "Service federal des Pensions",
            "accessed_date": "2026-08-02",
            "source_class": "primary_official",
            "notes": f"tick{TICK} L5 menage+transition+type split",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add(bid, year, amount, basis, notes, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return
    bud.append(
        {
            "budget_id": bid,
            "entity_id": "fpd",
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


for y, a in total_path.items():
    add(
        f"bud_fpd_legal_total_{y}",
        y,
        a,
        "outturn_indemnities",
        f"PensionStat legal pensions total {a:.0f} ({a/1e9:.3f}bn); tick{TICK} path reconfirm",
    )
for y, a in retraite_path.items():
    add(f"bud_fpd_retraite_{y}", y, a, "outturn_indemnities", f"Retirement pensions total {a:.0f}; tick{TICK}")
for y, a in survie_path.items():
    add(
        f"bud_fpd_survie_{y}",
        y,
        a,
        "outturn_indemnities",
        f"Survivor pensions+transition total {a:.0f}; tick{TICK}",
    )
for y, a in menage_path.items():
    add(
        f"bud_fpd_taux_menage_{y}",
        y,
        a,
        "outturn_indemnities",
        f"Household-rate (taux menage) retirement cash {a:.0f} sal+indep only; tick{TICK}",
    )
for y, a in trans_path.items():
    add(
        f"bud_fpd_alloc_transition_{y}",
        y,
        a,
        "outturn_indemnities",
        f"Transition allocation (widow/er bridge) cash {a:.0f}; tick{TICK}",
    )

add(
    "bud_fpd_taux_menage_sal_2025",
    2025,
    menage_2025_sal,
    "outturn_indemnities",
    f"Sal household-rate retirement {menage_2025_sal:.0f} of menage total; tick{TICK}",
)
add(
    "bud_fpd_taux_menage_ind_2025",
    2025,
    menage_2025_ind,
    "outturn_indemnities",
    f"Indep household-rate retirement {menage_2025_ind:.0f}; tick{TICK}",
)
add("bud_fpd_trans_sal_2025", 2025, ts, "outturn_indemnities", f"Sal transition allocation {ts:.0f}; tick{TICK}")
add("bud_fpd_trans_ind_2025", 2025, ti, "outturn_indemnities", f"Indep transition allocation {ti:.0f}; tick{TICK}")
add("bud_fpd_trans_fonct_2025", 2025, tf, "outturn_indemnities", f"Fonct transition allocation {tf:.0f}; tick{TICK}")
add(
    "bud_fpd_autres_sal_ret_2025",
    2025,
    autres_sal_ret,
    "outturn_indemnities",
    f"Sal retirement autres prestations {autres_sal_ret:.0f}; tick{TICK}",
)
add(
    "bud_fpd_autres_ind_ret_2025",
    2025,
    autres_ind_ret,
    "outturn_indemnities",
    f"Indep retirement autres prestations {autres_ind_ret:.0f}; tick{TICK}",
)
for reg, label in [("Sal.", "sal"), ("Fonct.", "fonct"), ("Ind.", "ind")]:
    add(
        f"bud_fpd_regime_{label}_2025",
        2025,
        by_regime_y[(2025, reg)],
        "outturn_indemnities",
        f"Regime {reg} total {by_regime_y[(2025, reg)]:.0f} 2025; tick{TICK}",
    )
add(
    "bud_fpd_pensionnes_stock_2025",
    2025,
    tot_nat,
    "beneficiary_stock",
    f"Pensionnes stock nationality-sum 2025 {tot_nat} (site ~2.7m); tick{TICK}",
)
add(
    "bud_fpd_grapa_stock_2025",
    2025,
    grapa_n,
    "beneficiary_stock",
    f"GRAPA stock 2025 {grapa_n} beneficiaries microdata sum; tick{TICK}",
)
g5 = 100 * (total_path[2025] / total_path[2019] - 1)
add(
    "bud_fpd_legal_growth_2019_25",
    2025,
    total_path[2025] - total_path[2019],
    "delta_eur",
    f"Legal pensions +{g5:.1f}pct 2019-25 (+{(total_path[2025]-total_path[2019])/1e9:.2f}bn); tick{TICK}",
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


cb_menage = {str(y): int(round(menage_path[y])) for y in range(2019, 2026)}
cb_menage["sal_2025"] = int(round(menage_2025_sal))
cb_menage["ind_2025"] = int(round(menage_2025_ind))
cb_menage["share_of_legal_2025_pct"] = round(100 * menage_2025 / total_path[2025], 2)

cb_trans = {str(y): int(round(trans_path[y])) for y in range(2019, 2026)}
cb_trans["sal_2025"] = int(round(ts))
cb_trans["ind_2025"] = int(round(ti))
cb_trans["fonct_2025"] = int(round(tf))

cb_split = {
    "total": {str(y): int(round(total_path[y])) for y in range(2019, 2026)},
    "retraite": {str(y): int(round(retraite_path[y])) for y in range(2019, 2026)},
    "survie": {str(y): int(round(survie_path[y])) for y in range(2019, 2026)},
    "retraite_share_2025_pct": round(100 * retraite_2025 / total_path[2025], 2),
    "growth_2019_25_pct": round(100 * (total_path[2025] / total_path[2019] - 1), 1),
    "stock_2025": tot_nat,
    "grapa_stock_2025": grapa_n,
}

addc(
    "cmt_fpd_taux_menage_2019_25",
    title="FPD household-rate (taux menage) retirement cash path 2019-2025",
    entity_id="fpd",
    beneficiary="Married pensioners with dependent spouse (sal+indep)",
    legal_basis="Pension au taux menage AMI/SFP rules",
    decision_date="2026-03-25",
    start_year="2019",
    end_year="2025",
    total_envelope_eur=str(int(round(menage_2025))),
    cash_by_year=json.dumps(cb_menage, separators=(",", ":")),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
    stated_goal="Higher rate when spouse has little/no own income",
    cut_option="Convergence/individualization debate; dual survival pensions; protect genuine dependency",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="SS>FPD>taux_menage",
    notes=f"5.92bn 2025 (~8.6pct of legal total); sal 4.75 + indep 1.17; fonct no menage rate in table; tick{TICK}",
)

addc(
    "cmt_fpd_alloc_transition_2019_25",
    title="FPD transition allocation (allocation de transition) path 2019-2025",
    entity_id="fpd",
    beneficiary="Recent widow(er)s below age threshold",
    legal_basis="Allocation de transition survivor bridge",
    decision_date="2026-03-25",
    start_year="2019",
    end_year="2025",
    total_envelope_eur=str(int(round(trans_2025))),
    cash_by_year=json.dumps(cb_trans, separators=(",", ":")),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
    stated_goal="Temporary income bridge before retirement age for survivors",
    cut_option="Core bridge; monitor take-up vs survival pension substitution",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="SS>FPD>allocation_transition",
    notes=f"~63.3m 2025 mostly sal; inside survie perimeter; tick{TICK}",
)

addc(
    "cmt_fpd_retraite_survie_split_2019_25",
    title="FPD legal pensions retraite vs survie split 2019-2025",
    entity_id="fpd",
    beneficiary="Retirees and survivors",
    legal_basis="Statutory pension rights three regimes",
    decision_date="2026-03-25",
    start_year="2019",
    end_year="2025",
    total_envelope_eur=str(int(round(total_path[2025]))),
    cash_by_year=json.dumps(cb_split, separators=(",", ":")),
    remaining_eur="",
    status="active",
    evaluation_url="https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
    stated_goal="Old-age and survivor income security",
    cut_option="Parameter reform (CEV); not cut earned rights; dual ESSPROS old-age broader",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="SS>FPD>retraite_survie_split",
    notes=f"Retraite 60.52bn (87.6pct) survie 8.53bn (12.4pct) of 69.05bn; +43pct since 2019; tick{TICK}",
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
    "lb_fpd_taux_menage_5_92bn_2025",
    name="FPD household-rate pensions 5.92bn 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>FPD>taux_menage_2025",
    annual_cost_eur=str(int(round(menage_2025))),
    total_cost_eur=str(int(round(menage_2025))),
    tco_notes="Strong: 5.923bn (sal 4.750 + indep 1.173); ~8.6pct of legal 69.05bn; dual individualization debate",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Married pensioners with dependent spouse",
    stated_goal="Household-rate old-age income when spouse has limited income",
    measured_outcome="Material dual-earner transition residual; fonct not in menage table",
    absurdity_score="4",
    cost_score="9.0",
    difficulty="7",
    priority_index="6.2",
    cut_proposal="Gradual individualization with floor protection; open dual survival interaction",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_fpd_survie_8_53bn_2025",
    name="FPD survivor pensions package 8.53bn 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>FPD>survie_2025",
    annual_cost_eur=str(int(round(survie_2025))),
    total_cost_eur=str(int(round(survie_2025))),
    tco_notes="Strong: 8.528bn survivor+transition (12.4pct of legal); slower growth than retirement per SFP note",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Surviving spouses / transition recipients",
    stated_goal="Survivor income security",
    measured_outcome="Marriage decline + dual careers reduce survival growth vs retirement",
    absurdity_score="3",
    cost_score="9.0",
    difficulty="7",
    priority_index="5.9",
    cut_proposal="Core; dual transition vs full survival design",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_fpd_retraite_60_5bn_2025",
    name="FPD retirement pensions 60.52bn 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>FPD>retraite_2025",
    annual_cost_eur=str(int(round(retraite_2025))),
    total_cost_eur=str(int(round(retraite_2025))),
    tco_notes="Strong: 60.519bn retirement (87.6pct of 69.05bn legal); core entitlement mega",
    confidence="strong",
    source_id=SRC,
    beneficiaries="~2.67m pensioners stock class",
    stated_goal="Old-age earned rights",
    measured_outcome="Dominant share; dual ESSPROS old-age EE ~74.5bn broader",
    absurdity_score="2",
    cost_score="10.0",
    difficulty="3",
    priority_index="6.5",
    cut_proposal="Parameter reform not slash benefits; dual CEV path",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_fpd_alloc_transition_63m_2025",
    name="FPD transition allocation 63m 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>FPD>alloc_transition_2025",
    annual_cost_eur=str(int(round(trans_2025))),
    total_cost_eur=str(int(round(trans_2025))),
    tco_notes=f"Strong: {trans_2025/1e6:.1f}m (sal {ts/1e6:.1f} ind {ti/1e6:.1f} fonct {tf/1e6:.1f})",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Younger widow(er)s on bridge benefit",
    stated_goal="Temporary bridge before pension age",
    measured_outcome="Small vs survival stock; path rising with reform design",
    absurdity_score="3",
    cost_score="5.5",
    difficulty="5",
    priority_index="4.5",
    cut_proposal="Monitor duration and substitution into full survival",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_fpd_autres_prest_sal_354m_2025",
    name="FPD sal retirement autres prestations 354m 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>FPD>autres_sal_ret_2025",
    annual_cost_eur=str(int(round(autres_sal_ret))),
    total_cost_eur=str(int(round(autres_sal_ret))),
    tco_notes="Strong: 354.0m autres inside sal retirement; residual opacity of composition",
    confidence="strong",
    source_id=SRC,
    beneficiaries="Sal retirees residual lines",
    stated_goal="Ancillary retirement payments",
    measured_outcome="~0.9pct of sal regime; L5 composition not public in aggregate sheet",
    absurdity_score="5",
    cost_score="7.0",
    difficulty="6",
    priority_index="5.4",
    cut_proposal="Publish composition of autres prestations",
    status="seed",
    notes=f"tick{TICK} residual method opacity inside strong total",
)

with open(DATA / "leaderboard.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lf, extrasaction="ignore")
    w.writeheader()
    w.writerows(lb)

with open(DATA / "research_queue.csv", encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rf = list(rq[0].keys())
for r in rq:
    if r["task_id"] == "rq_419":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = f"tick{TICK}: PensionStat L5 menage 5.92bn transition 63m retraite/survie split; spawn rq_420"
if not any(r["task_id"] == "rq_420" for r in rq):
    rq.append(
        {
            "task_id": "rq_420",
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
            "notes": f"Spawned tick{TICK} after FPD L5 menage/transition; rq_116 SWA deferred",
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
        "notes": f"Scheduler 60s. Next prio5 rq_420; rq_116 SWA deferred. tick{TICK} FPD menage 5.92bn transition 63m.",
    }
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, extrasaction="ignore")
    w.writeheader()
    w.writerows(st)

print("OK", TICK, "bud", len(bud), "cmt", len(cmt), "lb", len(lb))
print("menage", int(menage_2025), "trans", int(trans_2025), "ret", int(retraite_2025), "surv", int(survie_2025))
