# tick 429: DG HAN ARR/AI 2.93bn 2025 + SPF SS macro from annual report
import csv, json
from pathlib import Path

DATA = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
NOW = "2026-08-02T05:15:00Z"
TICK = 429
UNIT = "rq_420"
SRC = "src_spfss_ra_2025_dghan"
SRC_SS = "src_spfss_ra_2025_ss_macro"

# Official key figures SPF SS RA 2025
cash_total = 2_930_000_000  # 2,93 milliards prix courants
benef = 264_250
arr_only = 27_608
ai_only = 106_868
both = 129_774
avg_month = 938
ai_only_avg = 349
arr_only_avg = 924
both_avg = 1425
both_arr = 934
both_ai = 491
yoy_benef_pct = 4.0
vs_2021_pct = 17.8
evals = 155_334
recognized = 581_987
parking_cards = 507_301
parking_new = 71_440
first_requests = 36_980
refusal_rate = 66.1
median_days_first = 157
eval_days = 136
# regional shares of ARR/AI recipients
share_vl = 52.1
share_wal = 37.9
share_bru = 9.2
share_dg = 0.7

# reconstructed component annual (medium) from monthly avg * stock * 12
ai_only_cash = int(round(ai_only * ai_only_avg * 12))
arr_only_cash = int(round(arr_only * arr_only_avg * 12))
both_cash = int(round(both * both_avg * 12))
recon_sum = ai_only_cash + arr_only_cash + both_cash

# SS macro 2025
ss_total = 146_800_000_000
ss_prest = 132_900_000_000
ss_gestion = 2_900_000_000
ss_divers = 10_970_000_000
ss_cotis = 83_200_000_000
ss_state = 20_500_000_000
ss_fed = 400_000_000
ss_altfin = 26_200_000_000
ss_other = 7_700_000_000
ss_equilibre = 7_400_000_000

with open(DATA / "sources.csv", encoding="utf-8", newline="") as f:
    src = list(csv.DictReader(f))
    sf = list(src[0].keys())
if not any(r["source_id"] == SRC for r in src):
    src.append(
        {
            "source_id": SRC,
            "title": "SPF Securite sociale Rapport annuel 2025 DG HAN ARR/AI allocations 2.93bn",
            "url": "https://socialsecurity.belgium.be/sites/default/files/content/docs/fr/publications/rapports-annuels/rapport-annuel-spfss-2025-fr.pdf",
            "publisher": "SPF Securite sociale / DG Personnes handicapees",
            "accessed_date": "2026-08-02",
            "source_class": "primary_agency",
            "notes": f"2.93bn current prices; 264250 monthly benef; ARR/AI split; dual VAPH regional care; tick{TICK}",
        }
    )
if not any(r["source_id"] == SRC_SS for r in src):
    src.append(
        {
            "source_id": SRC_SS,
            "title": "SPF Securite sociale Rapport annuel 2025 SS depenses 146.8bn et financement",
            "url": "https://socialsecurity.belgium.be/sites/default/files/content/docs/fr/publications/rapports-annuels/rapport-annuel-spfss-2025-fr.pdf",
            "publisher": "SPF Securite sociale DG Analyse & Monitoring",
            "accessed_date": "2026-08-02",
            "source_class": "primary_agency",
            "notes": f"SS exp 146.8bn prest 132.9 gestion 2.9 divers 10.97; cotis 83.2 altfin 26.2; tick{TICK}",
        }
    )
with open(DATA / "sources.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sf, extrasaction="ignore")
    w.writeheader()
    w.writerows(src)

# entities
with open(DATA / "entities.csv", encoding="utf-8", newline="") as f:
    ent = list(csv.DictReader(f))
    ef = list(ent[0].keys())
if not any(r.get("entity_id") == "dg_han" for r in ent):
    ent.append(
        {
            "entity_id": "dg_han",
            "name_nl": "DG Personen met een handicap DG HAN",
            "name_fr": "DG Personnes handicapees DG HAN",
            "name_en": "DG Persons with Disabilities",
            "type": "agency",
            "parent_id": "sec_ss",
            "lang": "bi",
            "url": "https://handicap.belgium.be",
            "foi_email": "",
            "foi_url": "https://www.ibz.be/nl/openbaarheid-van-bestuur",
            "notes": f"ARR+AI federal disability allowances 2.93bn 2025; 264k monthly; dual VAPH/AViQ regional care; tick{TICK}",
        }
    )
with open(DATA / "entities.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ef, extrasaction="ignore")
    w.writeheader()
    w.writerows(ent)

with open(DATA / "budgets.csv", encoding="utf-8", newline="") as f:
    bud = list(csv.DictReader(f))
    bf = list(bud[0].keys())


def add(bid, entity, year, amount, basis, notes, source=SRC, conf="strong"):
    if any(r["budget_id"] == bid for r in bud):
        return
    bud.append(
        {
            "budget_id": bid,
            "entity_id": entity,
            "year": str(year),
            "amount_eur": str(int(amount)),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": source,
            "confidence": conf,
            "notes": notes,
        }
    )


add(
    "bud_dghan_arr_ai_total_2025",
    "dg_han",
    2025,
    cash_total,
    "outturn_indemnities",
    f"DG HAN ARR+AI cash 2.93bn current prices 2025; 264250 monthly benef (+4pct); tick{TICK}",
)
add(
    "bud_dghan_benef_monthly_2025",
    "dg_han",
    2025,
    benef,
    "beneficiary_stock",
    f"Monthly allocation recipients 264250 (+4pct YoY; +17.8pct vs 2021); tick{TICK}",
)
add(
    "bud_dghan_arr_only_stock_2025",
    "dg_han",
    2025,
    arr_only,
    "beneficiary_stock",
    f"ARR-only recipients 27608; tick{TICK}",
)
add(
    "bud_dghan_ai_only_stock_2025",
    "dg_han",
    2025,
    ai_only,
    "beneficiary_stock",
    f"AI-only recipients 106868; tick{TICK}",
)
add(
    "bud_dghan_both_stock_2025",
    "dg_han",
    2025,
    both,
    "beneficiary_stock",
    f"ARR+AI combined recipients 129774; tick{TICK}",
)
add(
    "bud_dghan_avg_month_2025",
    "dg_han",
    2025,
    avg_month,
    "unit_cost_eur",
    f"Average monthly allocation EUR 938 current prices; tick{TICK}",
)
add(
    "bud_dghan_ai_only_avg_2025",
    "dg_han",
    2025,
    ai_only_avg,
    "unit_cost_eur",
    f"AI-only avg monthly EUR 349; tick{TICK}",
)
add(
    "bud_dghan_arr_only_avg_2025",
    "dg_han",
    2025,
    arr_only_avg,
    "unit_cost_eur",
    f"ARR-only avg monthly EUR 924; tick{TICK}",
)
add(
    "bud_dghan_both_avg_2025",
    "dg_han",
    2025,
    both_avg,
    "unit_cost_eur",
    f"Both avg monthly EUR 1425 (ARR 934 + AI 491); tick{TICK}",
)
add(
    "bud_dghan_ai_only_cash_recon_2025",
    "dg_han",
    2025,
    ai_only_cash,
    "reconstructed_annual",
    f"Recon AI-only ~{ai_only_cash} (stock*avg*12); medium; tick{TICK}",
    conf="medium",
)
add(
    "bud_dghan_arr_only_cash_recon_2025",
    "dg_han",
    2025,
    arr_only_cash,
    "reconstructed_annual",
    f"Recon ARR-only ~{arr_only_cash}; medium; tick{TICK}",
    conf="medium",
)
add(
    "bud_dghan_both_cash_recon_2025",
    "dg_han",
    2025,
    both_cash,
    "reconstructed_annual",
    f"Recon both ~{both_cash}; sum recon {recon_sum} vs official 2.93bn; medium; tick{TICK}",
    conf="medium",
)
add(
    "bud_dghan_evals_2025",
    "dg_han",
    2025,
    evals,
    "case_volume",
    f"Disability evaluations 155334 in 2025; tick{TICK}",
)
add(
    "bud_dghan_recognized_stock_2025",
    "dg_han",
    2025,
    recognized,
    "beneficiary_stock",
    f"Persons with disability recognition 581987; tick{TICK}",
)
add(
    "bud_dghan_parking_stock_2025",
    "dg_han",
    2025,
    parking_cards,
    "volume_cards",
    f"Parking cards in circulation 507301 (new 71440 in 2025); tick{TICK}",
)
add(
    "bud_dghan_first_req_2025",
    "dg_han",
    2025,
    first_requests,
    "case_volume",
    f"First allocation requests decided 36980; refusal 66.1pct; tick{TICK}",
)

# SS macro
add(
    "bud_ss_total_exp_2025_spf",
    "sec_ss",
    2025,
    ss_total,
    "budget_aggregate",
    f"SS total expenditure 146.8bn 2025 SPF RA (~51pct state exp); dual CoA/NBB perimeters; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_prestations_2025_spf",
    "sec_ss",
    2025,
    ss_prest,
    "budget_aggregate",
    f"SS social benefits 132.9bn of 146.8; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_gestion_2025_spf",
    "sec_ss",
    2025,
    ss_gestion,
    "budget_aggregate",
    f"SS management costs 2.9bn 2025; dual mutual/OISZ beheer; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_divers_2025_spf",
    "sec_ss",
    2025,
    ss_divers,
    "budget_aggregate",
    f"SS various exp 10.97bn; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_cotis_2025_spf",
    "sec_ss",
    2025,
    ss_cotis,
    "receipts",
    f"SS social contributions 83.2bn 2025; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_state_sub_2025_spf",
    "sec_ss",
    2025,
    ss_state,
    "receipts",
    f"SS ordinary state subsidies 20.5bn; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_altfin_2025_spf",
    "sec_ss",
    2025,
    ss_altfin,
    "receipts",
    f"SS alternative financing 26.2bn; tick{TICK}",
    source=SRC_SS,
)
add(
    "bud_ss_equilibre_2025_spf",
    "sec_ss",
    2025,
    ss_equilibre,
    "receipts",
    f"SS equilibrium endowments 7.4bn; tick{TICK}",
    source=SRC_SS,
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
    "cmt_dghan_arr_ai_2025",
    title="DG HAN federal disability allowances ARR+AI 2025",
    entity_id="dg_han",
    beneficiary="Persons with disabilities (ARR income replacement + AI integration)",
    legal_basis="Loi 27 fev 1987 ARR/AI",
    decision_date="2026-01-01",
    start_year="2025",
    end_year="2025",
    total_envelope_eur=str(cash_total),
    cash_by_year=json.dumps(
        {
            "2025": cash_total,
            "benef_monthly": benef,
            "arr_only": arr_only,
            "ai_only": ai_only,
            "both": both,
            "avg_month": avg_month,
            "ai_only_avg": ai_only_avg,
            "arr_only_avg": arr_only_avg,
            "both_avg": both_avg,
            "recon_ai_only": ai_only_cash,
            "recon_arr_only": arr_only_cash,
            "recon_both": both_cash,
            "regions_pct": {"VL": share_vl, "WAL": share_wal, "BRU": share_bru, "DG": share_dg},
            "yoy_benef_pct": yoy_benef_pct,
            "vs_2021_pct": vs_2021_pct,
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://socialsecurity.belgium.be/sites/default/files/content/docs/fr/publications/rapports-annuels/rapport-annuel-spfss-2025-fr.pdf",
    stated_goal="Income replacement and autonomy cost compensation for disability",
    cut_option="Core safety net; reform 1987 law in progress; dual regional care (VAPH/AViQ); not pure waste",
    source_id=SRC,
    confidence="strong",
    hierarchy_path="SS>SPF_SS>DG_HAN>ARR_AI",
    notes=f"2.93bn strong; component recon medium from averages; dual INAMI inv + regional care not additive; tick{TICK}",
)

addc(
    "cmt_ss_macro_2025_spf",
    title="Belgian social security expenditure and financing 2025 SPF RA",
    entity_id="sec_ss",
    beneficiary="SS schemes aggregate",
    legal_basis="Social security financing architecture",
    decision_date="2026-01-01",
    start_year="2025",
    end_year="2025",
    total_envelope_eur=str(ss_total),
    cash_by_year=json.dumps(
        {
            "total_exp": ss_total,
            "prestations": ss_prest,
            "gestion": ss_gestion,
            "divers": ss_divers,
            "cotis": ss_cotis,
            "state_sub": ss_state,
            "federated_sub": ss_fed,
            "altfin": ss_altfin,
            "other_rec": ss_other,
            "equilibre": ss_equilibre,
        },
        separators=(",", ":"),
    ),
    remaining_eur="",
    status="active",
    evaluation_url="https://socialsecurity.belgium.be/sites/default/files/content/docs/fr/publications/rapports-annuels/rapport-annuel-spfss-2025-fr.pdf",
    stated_goal="SS financing snapshot",
    cut_option="Dual NBB EDP / CoA perimeters; track altfin and equilibre dependence",
    source_id=SRC_SS,
    confidence="strong",
    hierarchy_path="SS>aggregate>2025_spf_ra",
    notes=f"146.8bn ~51pct state exp; dual ESSPROS 174bn broader social protection; tick{TICK}",
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
    "lb_dghan_arr_ai_2_93bn_2025",
    name="DG HAN ARR+AI disability allowances 2.93bn 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>DG_HAN>ARR_AI_2025",
    annual_cost_eur=str(cash_total),
    total_cost_eur=str(cash_total),
    tco_notes="Strong SPF RA: 2.93bn current prices; 264250 monthly (+4%); avg 938/mo; dual VAPH care not additive",
    confidence="strong",
    source_id=SRC,
    beneficiaries="264250 monthly ARR/AI recipients",
    stated_goal="Federal disability income replacement and integration allowance",
    measured_outcome="Benef +17.8% since 2021; VL 52.1% WAL 37.9% BRU 9.2%; first-request refusal 66%",
    absurdity_score="2",
    cost_score="9.0",
    difficulty="6",
    priority_index="5.8",
    cut_proposal="Core safety net; finish 1987 reform with evidence; dual regional care unit-cost",
    status="seed",
    notes=f"tick{TICK} not pure waste",
)

addl(
    "lb_dghan_ai_only_recon_2025",
    name="DG HAN AI-only recon ~448m 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>DG_HAN>AI_only",
    annual_cost_eur=str(ai_only_cash),
    total_cost_eur=str(ai_only_cash),
    tco_notes=f"Medium recon: 106868*{ai_only_avg}*12={ai_only_cash}; autonomy cost compensation",
    confidence="medium",
    source_id=SRC,
    beneficiaries="106868 AI-only",
    stated_goal="Integration allowance for reduced autonomy",
    measured_outcome="Largest single-benefit cohort",
    absurdity_score="2",
    cost_score="7.5",
    difficulty="5",
    priority_index="5.0",
    cut_proposal="Publish official cash split ARR vs AI",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_dghan_arr_only_recon_2025",
    name="DG HAN ARR-only recon ~306m 2025",
    level="federal",
    type="social_transfer",
    hierarchy_path="SS>DG_HAN>ARR_only",
    annual_cost_eur=str(arr_only_cash),
    total_cost_eur=str(arr_only_cash),
    tco_notes=f"Medium recon: 27608*{arr_only_avg}*12={arr_only_cash}",
    confidence="medium",
    source_id=SRC,
    beneficiaries="27608 ARR-only",
    stated_goal="Income replacement for reduced earning capacity",
    measured_outcome="Smaller cohort than AI-only; dual both 129774",
    absurdity_score="2",
    cost_score="7.0",
    difficulty="5",
    priority_index="4.8",
    cut_proposal="Publish official cash split",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_ss_total_146_8bn_2025",
    name="Belgian SS total expenditure 146.8bn 2025 SPF",
    level="federal",
    type="aggregate",
    hierarchy_path="SS>aggregate>total_2025",
    annual_cost_eur=str(ss_total),
    total_cost_eur=str(ss_total),
    tco_notes="Strong SPF RA: 146.8bn (~51% state exp); prest 132.9 gestion 2.9 divers 11.0; dual NBB S1314",
    confidence="strong",
    source_id=SRC_SS,
    beneficiaries="SS schemes",
    stated_goal="Social security financing aggregate",
    measured_outcome="Cotis 83.2 altfin 26.2 state 20.5 equilibre 7.4",
    absurdity_score="2",
    cost_score="10.0",
    difficulty="3",
    priority_index="6.5",
    cut_proposal="Track equilibre and altfin path; dual EDP TE pie",
    status="seed",
    notes=f"tick{TICK}",
)

addl(
    "lb_ss_gestion_2_9bn_2025",
    name="SS management costs 2.9bn 2025 SPF",
    level="federal",
    type="ops",
    hierarchy_path="SS>aggregate>gestion_2025",
    annual_cost_eur=str(ss_gestion),
    total_cost_eur=str(ss_gestion),
    tco_notes="Strong: 2.9bn gestion of 146.8; dual CoA beheers 2.8bn 2024 class + mutual admin 1.3-1.4bn path",
    confidence="strong",
    source_id=SRC_SS,
    beneficiaries="OISZ mutualities admin path",
    stated_goal="SS administration overhead",
    measured_outcome="~2% of SS exp; dual landsbond residual FOI",
    absurdity_score="5",
    cost_score="8.5",
    difficulty="5",
    priority_index="6.0",
    cut_proposal="Publish full OISZ beheer breakdown; dual mutual L5",
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
    if r["task_id"] == "rq_420":
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["notes"] = f"tick{TICK}: DG HAN ARR/AI 2.93bn + SS macro 146.8bn; spawn rq_421"
if not any(r["task_id"] == "rq_421" for r in rq):
    rq.append(
        {
            "task_id": "rq_421",
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
            "notes": f"Spawned tick{TICK} after DG HAN 2.93bn; rq_116 SWA deferred",
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
        "notes": f"Scheduler 60s. Next prio5 rq_421; rq_116 SWA deferred. tick{TICK} DG HAN 2.93bn + SS 146.8bn.",
    }
)
with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, extrasaction="ignore")
    w.writeheader()
    w.writerows(st)

print("OK", TICK, "bud", len(bud), "cmt", len(cmt), "lb", len(lb))
print("cash", cash_total, "recon", recon_sum, "ss", ss_total)
