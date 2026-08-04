# tick 783 — rq_774 Kamer DOC 56 1282/003 Beleidsnota Werk
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T12:30:00Z"
SRC_MAIN = "src_kamer_beleid_werk_1282_003_2026"
SRC_DUAL = "src_dual_werk_illness_tick783"
GAP = "gap_werk_unemp_illness_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282003.pdf"


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=fields, lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows([{k: (r.get(k) or "") for k in fields} for r in rows])


# --- sources ---
sp = Path("docs/doge/data/sources.csv")
with sp.open(encoding="utf-8", newline="") as f:
    srows = list(csv.DictReader(f))
    sfields = list(srows[0].keys())
if not any(r["source_id"] == SRC_MAIN for r in srows):
    srows.append(
        {
            "source_id": SRC_MAIN,
            "title": "Kamer DOC 56 1282/003 Beleidsnota Werk residual measures 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister van Werk",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick783: illness benefits employees primary+invalidity 14.2bn 2025 "
                "path 18.2bn 2030 (monitoring committee Jul 2025); long-term sick stock 549996 "
                "end2024; employee/unemp long-term 514551 (420504 Dec2019); SS spend 140.2bn "
                "of state 274bn 2024; SS deficit 6.2bn 2024; labor cost 48.2eur/hr; tax wedge "
                "52.6pct; work-benefits net gap target 500eur/mo; familiekrediet base 25m/yr + "
                "15m 2026-27 + 35m from 2028; meal cheque +2 face + deduct 2to4 = 440eur net/yr; "
                "index 5.5pct dual-income +1250eur net/yr; flexi cap 18k; raw 56K1282003_beleid_werk.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Werk illness/unemp path vs RIZIV/SZ residual tick783",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: illness 14.2bn stack vs RIZIV AMI 41.3bn; "
                "unemp reform vs RVA spend residual; familiekrediet dual leave reform"
            ),
        }
    )
write_csv(sp, sfields, srows)

# --- budgets ---
bp = Path("docs/doge/data/budgets.csv")
with bp.open(encoding="utf-8", newline="") as f:
    brows = list(csv.DictReader(f))
    bfields = list(brows[0].keys())


def B(**kw):
    return {k: kw.get(k, "") for k in bfields}


new_b = [
    B(
        budget_id="bud_illness_benefits_emp_14_2bn_2025",
        entity_id="riziv",
        year="2025",
        amount_eur="14200000000",
        basis="estimated",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monitoring committee estimate illness benefits employees primary+invalidity 14.2bn 2025; tick783 1282/003",
    ),
    B(
        budget_id="bud_illness_benefits_emp_path_18_2bn_2030",
        entity_id="riziv",
        year="2030",
        amount_eur="18200000000",
        basis="projected",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Monitoring committee path without policy: illness benefits employees 18.2bn 2030; tick783",
    ),
    B(
        budget_id="bud_ss_spend_140_2bn_2024",
        entity_id="sec_ss",
        year="2024",
        amount_eur="140200000000",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Social security expenditure 140.2bn of state total 274bn 2024 (note citation); tick783",
    ),
    B(
        budget_id="bud_state_spend_total_274bn_2024",
        entity_id="sec_federal",
        year="2024",
        amount_eur="274000000000",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="State total expenditure 274bn 2024 as cited in Werk note vs SS 140.2bn; tick783 cross-check",
    ),
    B(
        budget_id="bud_ss_deficit_6_2bn_2024",
        entity_id="sec_ss",
        year="2024",
        amount_eur="6200000000",
        basis="estimated",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="SS deficit estimated 6.2bn 2024 (note); illness path major driver; tick783",
    ),
    B(
        budget_id="bud_familiekrediet_base_25m_2026",
        entity_id="fod_emploi",
        year="2026",
        amount_eur="25000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Familiekrediet annual base envelope 25m multi-year budget; tick783",
    ),
    B(
        budget_id="bud_familiekrediet_extra_15m_2026",
        entity_id="fod_emploi",
        year="2026",
        amount_eur="15000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Familiekrediet complementary financing 15m 2026 (and 2027); tick783",
    ),
    B(
        budget_id="bud_familiekrediet_extra_15m_2027",
        entity_id="fod_emploi",
        year="2027",
        amount_eur="15000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Familiekrediet complementary 15m 2027; tick783",
    ),
    B(
        budget_id="bud_familiekrediet_extra_35m_2028",
        entity_id="fod_emploi",
        year="2028",
        amount_eur="35000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Familiekrediet complementary raised to 35m from 2028; tick783",
    ),
    B(
        budget_id="bud_meal_cheque_gain_unit_440_2026",
        entity_id="fod_emploi",
        year="2026",
        amount_eur="440",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Meal cheque +2 face (8to10) + fiscal deduct 2to4 = 440 EUR net/yr per beneficiary; total Unknown; tick783",
    ),
    B(
        budget_id="bud_index_gain_dual_income_1250_2026",
        entity_id="fod_emploi",
        year="2026",
        amount_eur="1250",
        basis="illustrative",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Illustrative: low/mid wage index 5.5pct 2025-26 = 1250 EUR net/yr dual-income avg household end 2026; tick783",
    ),
    B(
        budget_id="bud_work_benefit_gap_target_500_mo",
        entity_id="fod_emploi",
        year="2029",
        amount_eur="500",
        basis="target",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Policy target: net gap work income vs replacement benefit >=500 EUR/mo by end legislature; tick783",
    ),
    B(
        budget_id="bud_flexi_income_cap_18k_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="18000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Flexi-jobs max annual income raised to 18000 EUR; horeca max hourly 21 EUR; tick783",
    ),
    B(
        budget_id="bud_labor_cost_hourly_48_2_2024",
        entity_id="fod_emploi",
        year="2024",
        amount_eur="48.2",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Average hourly labour cost BE 48.2 EUR vs eurozone 37.3 EU 33.5 2024; tick783",
    ),
    B(
        budget_id="bud_longterm_sick_stock_549996_2024",
        entity_id="riziv",
        year="2024",
        amount_eur="",
        basis="stock",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Long-term incapacity stock employees+self-employed 549996 end 2024; tick783",
    ),
    B(
        budget_id="bud_dual_werk_illness_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="14200000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor illness benefits 14.2bn 2025 class; not full TE; tick783",
    ),
]
exist_b = {r["budget_id"] for r in brows}
for nb in new_b:
    if nb["budget_id"] not in exist_b:
        brows.append(nb)
write_csv(bp, bfields, brows)

# --- commitments ---
cp = Path("docs/doge/data/commitments.csv")
with cp.open(encoding="utf-8", newline="") as f:
    crows = list(csv.DictReader(f))
    cfields = list(crows[0].keys())


def C(**kw):
    return {k: kw.get(k, "") for k in cfields}


new_c = [
    C(
        commitment_id="cmt_illness_path_14_2_to_18_2bn",
        title="Employee illness benefits 14.2bn 2025 path 18.2bn 2030",
        entity_id="riziv",
        beneficiary="incapacity beneficiaries",
        legal_basis="Monitoring committee Jul 2025; Beleidsnota Werk 1282/003",
        decision_date="2025-07-01",
        start_year="2025",
        end_year="2030",
        total_envelope_eur="0",
        cash_by_year='{"2025_bn": 14.2, "2030_bn": 18.2, "delta_bn": 4.0}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Document uncorrected illness spend path vs TNW reforms",
        cut_option="TNW package FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RIZIV>illness_benefits",
        notes="tick783 path without policy; dual SZ target -100k invalids",
    ),
    C(
        commitment_id="cmt_familiekrediet_2026_28",
        title="Familiekrediet leave reform envelopes 25m+15m/35m",
        entity_id="fod_emploi",
        beneficiary="parents/caregivers",
        legal_basis="Government agreement; Beleidsnota Werk 1282/003",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2028",
        total_envelope_eur="0",
        cash_by_year='{"base_m": 25, "extra_2026_m": 15, "extra_2027_m": 15, "extra_2028_m": 35}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Harmonise child-related leave as right of the child",
        cut_option="Envelope FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>WASO>familiekrediet",
        notes="tick783 draft law Jul 2026; extra week birth leave first step",
    ),
    C(
        commitment_id="cmt_unemp_duration_cap_2026",
        title="Unemployment benefit duration cap reform from 1 Jan 2026",
        entity_id="rva",
        beneficiary="unemployed",
        legal_basis="Unemployment reform; Beleidsnota Werk 1282/003",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="0",
        cash_by_year='{"savings_eur": "Unknown public", "access_days": 312, "window_months": 36}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="End unlimited unemployment duration; align eurozone",
        cut_option="Savings FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>RVA>unemployment",
        notes="tick783 waves from 1 Jan 2026; OCMW support plan amount FOI",
    ),
    C(
        commitment_id="cmt_meal_cheque_plus2_werk_2026",
        title="Meal cheques +2 face / deduct 2to4 (440 net/yr unit)",
        entity_id="fod_emploi",
        beneficiary="employees",
        legal_basis="Wage norm 96 adapted; Beleidsnota Werk 1282/003",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"unit_net_eur": 440, "total": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Purchasing power via meal cheques outside wage margin",
        cut_option="Taxex FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>taxex>meal_cheques",
        notes="tick783 dual cheque economy residual",
    ),
    C(
        commitment_id="cmt_flexi_cap_18k_2026",
        title="Flexi-jobs income cap 18k + sector extension",
        entity_id="rsz",
        beneficiary="flexi workers/employers",
        legal_basis="Government agreement; Beleidsnota Werk 1282/003",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"cap_eur": 18000, "horeca_hourly": 21}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Expand flexi with annual evaluation CoA/FPB/NAR",
        cut_option="Fiscal cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSZ>flexi",
        notes="tick783 dual flexi residual",
    ),
    C(
        commitment_id="cmt_dual_werk_tick783",
        title="Dual Werk illness 14.2bn vs unemp reform residual tick783",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/003",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"illness_2025_bn": 14.2, "path_2030_bn": 18.2, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map Werk instruments dual to RIZIV/RVA stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>werk",
        notes="tick783",
    ),
]
exist_c = {r["commitment_id"] for r in crows}
for nc in new_c:
    if nc["commitment_id"] not in exist_c:
        crows.append(nc)
write_csv(cp, cfields, crows)

# --- leaderboard ---
lp = Path("docs/doge/data/leaderboard.csv")
with lp.open(encoding="utf-8", newline="") as f:
    lrows = list(csv.DictReader(f))
    lfields = list(lrows[0].keys())


def lb(
    item_id,
    name,
    typ,
    path,
    annual,
    total,
    tco,
    conf,
    src,
    ben,
    abs_,
    cost,
    diff,
    prio,
    cut,
    notes,
):
    d = {
        "item_id": item_id,
        "name": name,
        "level": "L5",
        "type": typ,
        "hierarchy_path": path,
        "annual_cost_eur": annual,
        "total_cost_eur": total,
        "tco_notes": tco,
        "confidence": conf,
        "source_id": src,
        "beneficiaries": ben,
        "stated_goal": "see",
        "measured_outcome": "primary Kamer",
        "absurdity_score": abs_,
        "cost_score": cost,
        "difficulty": diff,
        "priority_index": prio,
        "cut_proposal": cut,
        "status": "active",
        "struck_reason": "",
        "notes": notes,
    }
    return {k: d.get(k, "") for k in lfields}


new_l = [
    lb(
        "lb_illness_benefits_14_2bn_2025",
        "Employee illness benefits 14.2bn 2025",
        "transfer",
        "Federal>RIZIV>illness",
        "14200000000",
        "14200000000",
        "Strong primary monitoring estimate primary+invalidity; path 18.2bn 2030",
        "strong",
        SRC_MAIN,
        "incapacity",
        "6.5",
        "9.5",
        "5.0",
        "7.50",
        "TNW FOI",
        "tick783",
    ),
    lb(
        "lb_illness_path_18_2bn_2030",
        "Illness benefits path peak 18.2bn 2030",
        "transfer",
        "Federal>RIZIV>illness",
        "18200000000",
        "18200000000",
        "Medium projection without policy; dual -100k invalid target",
        "medium",
        SRC_MAIN,
        "incapacity",
        "7.0",
        "9.5",
        "5.0",
        "7.65",
        "Path FOI",
        "tick783",
    ),
    lb(
        "lb_ss_spend_140_2bn_2024",
        "Social security spend 140.2bn 2024",
        "transfer",
        "Federal>SS>total",
        "140200000000",
        "140200000000",
        "Strong note citation of SS share of 274bn state; L1-class",
        "strong",
        SRC_MAIN,
        "public",
        "4.0",
        "10.0",
        "4.0",
        "6.80",
        "Reconcile FOI",
        "tick783",
    ),
    lb(
        "lb_ss_deficit_6_2bn_2024",
        "SS deficit 6.2bn 2024",
        "ops",
        "Federal>SS>deficit",
        "6200000000",
        "6200000000",
        "Strong note estimate; illness major driver",
        "strong",
        SRC_MAIN,
        "public",
        "5.5",
        "9.0",
        "4.5",
        "6.85",
        "Structure FOI",
        "tick783",
    ),
    lb(
        "lb_familiekrediet_40m_class_2026",
        "Familiekrediet 25+15m class 2026",
        "transfer",
        "Federal>WASO>familiekrediet",
        "40000000",
        "40000000",
        "Strong base 25m + extra 15m 2026; path extra 35m from 2028",
        "strong",
        SRC_MAIN,
        "parents",
        "3.0",
        "6.0",
        "2.5",
        "4.35",
        "Envelope FOI",
        "tick783",
    ),
    lb(
        "lb_meal_cheque_440_unit_2026",
        "Meal cheque +2 reform 440 net/yr unit",
        "taxex",
        "Federal>taxex>meal_cheques",
        "440",
        "0",
        "Strong unit; stacks cheque economy ~1.07bn residual",
        "strong",
        SRC_MAIN,
        "employees",
        "6.5",
        "5.0",
        "3.5",
        "5.45",
        "Taxex FOI",
        "tick783 dual cheque",
    ),
    lb(
        "lb_unemp_duration_cap_2026",
        "Unemployment duration cap reform 2026",
        "transfer",
        "Federal>RVA>unemployment",
        "0",
        "0",
        "Medium policy; euro savings Unknown public — FOI; OCMW support opaque",
        "medium",
        SRC_MAIN,
        "unemployed",
        "5.0",
        "8.0",
        "4.0",
        "6.00",
        "Savings FOI",
        "tick783",
    ),
    lb(
        "lb_flexi_cap_18k_2026",
        "Flexi income cap 18k + sector expand 2026",
        "taxex",
        "Federal>RSZ>flexi",
        "0",
        "0",
        "Strong policy params; fiscal cost residual FOI/CoA eval",
        "strong",
        SRC_MAIN,
        "flexi",
        "5.5",
        "6.5",
        "3.5",
        "5.55",
        "Fiscal FOI",
        "tick783",
    ),
    lb(
        "lb_dual_werk_2026",
        "Dual Werk illness 14.2bn vs unemp residual",
        "transfer",
        "Belgium>dual>werk",
        "14200000000",
        "0",
        "Strong dual not TE-additive map Werk instruments",
        "strong",
        SRC_DUAL,
        "public",
        "5.0",
        "9.0",
        "4.0",
        "6.60",
        "L5 FOI",
        "tick783",
    ),
]
exist_l = {r["item_id"] for r in lrows}
for nl in new_l:
    if nl["item_id"] not in exist_l:
        lrows.append(nl)
write_csv(lp, lfields, lrows)

# --- foi_queue ---
fp = Path("docs/doge/data/foi_queue.csv")
with fp.open(encoding="utf-8", newline="") as f:
    frows = list(csv.DictReader(f))
    ffields = list(frows[0].keys())
if not any(r["gap_id"] == GAP for r in frows):
    frows.append(
        {
            k: v
            for k, v in {
                "gap_id": GAP,
                "hierarchy_path": "Federal>WASO>unemp_illness_L5",
                "entity_id": "fod_waso",
                "what_is_missing": (
                    "RVA unemployment spend cash path pre/post duration-cap reform 2026-2029; "
                    "OCMW support plan (leefloon reimbursement rate delta + temporary subsidies) "
                    "euro amounts; regional social-economy compensation for disability-job path; "
                    "meal-cheque +2 aggregate taxex/parafiscal cost 2026; familiekrediet full "
                    "multi-year cash reconciliation; illness 14.2bn line composition primary vs "
                    "invalidity; projected savings from TNW wave vs 18.2bn 2030 path"
                ),
                "why_it_matters": (
                    "Werk note public on large illness stack and reform design; residual euro "
                    "savings and OCMW dual opaque"
                ),
                "priority": "9",
                "recipient_body": "FOD WASO / RVA / RIZIV FOI",
                "recipient_email": "",
                "recipient_postal": "https://emploi.belgique.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_illness_path_14_2_to_18_2bn|cmt_unemp_duration_cap_2026|"
                    "cmt_familiekrediet_2026_28|cmt_dual_werk_tick783"
                ),
                "linked_leaderboard_id": (
                    "lb_illness_benefits_14_2bn_2025|lb_illness_path_18_2bn_2030|"
                    "lb_unemp_duration_cap_2026|lb_dual_werk_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick783 Kamer 1282/003 primary; human send only",
            }.items()
            if k in ffields
        }
    )
write_csv(fp, ffields, frows)

# --- research_queue ---
rp = Path("docs/doge/data/research_queue.csv")
with rp.open(encoding="utf-8", newline="") as f:
    rrows = list(csv.DictReader(f))
    rfields = list(rrows[0].keys())
for r in rrows:
    if r["task_id"] == "rq_774":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick783: Werk 1282/003 illness 14.2bn path 18.2bn familiekrediet 25+15m "
            "unemp cap FOI ready; spawn rq_775"
        )
if not any(r["task_id"] == "rq_775" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_775",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (local/regional/CoA or unmined "
                    "1282 notes e.g. Zelfstandigen/Pensioenen/Asiel); Werk 1282/003 filled tick783"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick783 after rq_774",
            }.items()
            if k in rfields
        }
    )
write_csv(rp, rfields, rrows)

# --- loop_state ---
lsp = Path("docs/doge/data/loop_state.csv")
with lsp.open(encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
ls[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_774",
        "ticks_completed": "783",
        "paused": "no",
        "notes": "user paused=no; next rq_775; progress@790 in 7; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print(
    "OK sources",
    len(srows),
    "budgets",
    len(brows),
    "cmt",
    len(crows),
    "lb",
    len(lrows),
    "foi",
    len(frows),
    "rq",
    len(rrows),
)
