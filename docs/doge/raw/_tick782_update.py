# tick 782 — rq_773 Sociale Zaken 1282/008 hole-fill
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

TICK = 782
UTC = "2026-08-04T12:05:00Z"
SRC_MAIN = "src_kamer_beleid_sociale_1282_008_2026"
SRC_DUAL = "src_dual_sociale_zaken_tick782"
GAP = "gap_sz_tnw_egov_alt_l5"
PDF_URL = "https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282008.pdf"

# --- sources ---
sp = Path("docs/doge/data/sources.csv")
with sp.open(encoding="utf-8", newline="") as f:
    srows = list(csv.DictReader(f))
    sfields = list(srows[0].keys())
if not any(r["source_id"] == SRC_MAIN for r in srows):
    srows.append(
        {
            "source_id": SRC_MAIN,
            "title": "Kamer DOC 56 1282/008 Beleidsnota Sociale Zaken residual measures 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Sociale Zaken (Vandenbroucke)",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick782: 32p 23jan2026; alt finance +198m 2026 (structural RSZ cuts + "
                "Plus Plans + sports cap exclude + horeca5/collective hours stop); GGMMI +35eur "
                "1apr2026 ->50eur net via fiscal workbonus; meal cheques +2eur employer max; "
                "first-hire RSZ red 3100->2000eur/q first, 1000eur/q 2-5 for 12q; VI TNW envelope "
                "5/7.5/10/15pct 2026-2029; work-resume prime 3000eur/case; illness target 588k by "
                "2030; IVT alone +2pct 2026+2028; centenindex wages>4k benefits>2k; e-Gov3.0 IT "
                "credits 2026-2029 amount Unknown; raw 56K1282008_beleid_sociale_zaken.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Sociale Zaken instruments vs RSZ alt finance / illness TNW residual tick782",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: RSZ alt finance delta 198m vs total alt finance stack; "
                "TNW OA percent path vs illness save path; meal+2 vs cheque economy taxex residual"
            ),
        }
    )
with sp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=sfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in sfields} for r in srows])

# --- budgets ---
bp = Path("docs/doge/data/budgets.csv")
with bp.open(encoding="utf-8", newline="") as f:
    brows = list(csv.DictReader(f))
    bfields = list(brows[0].keys())


def B(**kw):
    return {k: kw.get(k, "") for k in bfields}


new_b = [
    B(
        budget_id="bud_rsz_alt_finance_delta_198m_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="198000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Net +198m alternative financing 2026 (BTW+RV) compensating structural contribution reductions package; tick782 1282/008",
    ),
    B(
        budget_id="bud_ggmmi_raise_35eur_unit_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="35",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="GGMMI +35 EUR/mo gross from 1 Apr 2026 (unit; total fiscal cost Unknown); nets +50 via fiscal workbonus; tick782",
    ),
    B(
        budget_id="bud_meal_cheque_plus2_unit_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="2",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Meal cheque employer max +2 EUR 2026 (unit; total taxex delta Unknown public in note); tick782",
    ),
    B(
        budget_id="bud_first_hire_red_q1_2000_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="2000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="First-hire RSZ reduction 2000 EUR/quarter unlimited (was 3100); unit rate; tick782",
    ),
    B(
        budget_id="bud_first_hire_red_q2_5_1000_2026",
        entity_id="rsz",
        year="2026",
        amount_eur="1000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="2nd-5th hire RSZ reduction 1000 EUR/quarter x12 quarters; unit rate; tick782",
    ),
    B(
        budget_id="bud_werkhervatting_premium_unit_3k_2026",
        entity_id="riziv",
        year="2026",
        amount_eur="3000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Work-resumption employer premium raised to 3000 EUR/case (>=3m partial return); total envelope Unknown; tick782",
    ),
    B(
        budget_id="bud_tnw_oa_envelope_pct_2026",
        entity_id="riziv",
        year="2026",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="VI/OA TNW responsabilization envelope 5pct of TNW-law base 2026 (7.5 2027 / 10 2028 / 15 from 2029); euro base Unknown; tick782",
    ),
    B(
        budget_id="bud_tnw_oa_envelope_pct_2027",
        entity_id="riziv",
        year="2027",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="VI/OA TNW envelope 7.5pct 2027; euro Unknown; tick782",
    ),
    B(
        budget_id="bud_tnw_oa_envelope_pct_2028",
        entity_id="riziv",
        year="2028",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="VI/OA TNW envelope 10pct 2028; euro Unknown; tick782",
    ),
    B(
        budget_id="bud_tnw_oa_envelope_pct_2029",
        entity_id="riziv",
        year="2029",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="VI/OA TNW envelope 15pct from 2029; euro Unknown; tick782",
    ),
    B(
        budget_id="bud_ivt_alone_plus2_2026",
        entity_id="fod_sociale_zekerheid",
        year="2026",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="IVT/ARR alone-living +2pct 2026 (and again 2028); euro fiscal cost Unknown in note; tick782",
    ),
    B(
        budget_id="bud_ivt_alone_plus2_2028",
        entity_id="fod_sociale_zekerheid",
        year="2028",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="IVT/ARR alone-living +2pct 2028; euro Unknown; tick782",
    ),
    B(
        budget_id="bud_illness_target_588k_2030",
        entity_id="riziv",
        year="2030",
        amount_eur="",
        basis="target",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Long-term illness stock target 588000 persons by 2030 (~100k below monitoring committee path); not a euro line; tick782",
    ),
    B(
        budget_id="bud_centenindex_wage_threshold_4k_2026",
        entity_id="sec_ss",
        year="2026",
        amount_eur="4000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Centenindex applies to wages above 4000 EUR/mo FT; benefits/pensions above 2000; tick782",
    ),
    B(
        budget_id="bud_centenindex_benefit_threshold_2k_2026",
        entity_id="sec_ss",
        year="2026",
        amount_eur="2000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Centenindex benefits/pensions threshold 2000 EUR/mo; tick782",
    ),
    B(
        budget_id="bud_egov30_it_credits_2026_29",
        entity_id="rsz",
        year="2026",
        amount_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="weak",
        notes="e-Gov 3.0 IT credits provided 2026-2029 per 1282/008; annual amounts Unknown public; FOI; tick782",
    ),
    B(
        budget_id="bud_employer_solidarity_30pct_m2_3_2026",
        entity_id="riziv",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Employer solidarity 30pct of benefit months 2-3 (or 18pct gross) firms >50 staff age 18-55; extend m4-5 from 2027; yield partial in prior rows; tick782 cross-ref",
    ),
    B(
        budget_id="bud_dual_sociale_zaken_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="198000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor: alt finance delta 198m as public L5 residual of SZ note; not full TE; tick782",
    ),
]
exist_b = {r["budget_id"] for r in brows}
for nb in new_b:
    if nb["budget_id"] not in exist_b:
        brows.append(nb)
with bp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=bfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in bfields} for r in brows])

# --- commitments ---
cp = Path("docs/doge/data/commitments.csv")
with cp.open(encoding="utf-8", newline="") as f:
    crows = list(csv.DictReader(f))
    cfields = list(crows[0].keys())


def C(**kw):
    return {k: kw.get(k, "") for k in cfields}


new_c = [
    C(
        commitment_id="cmt_rsz_alt_finance_delta_198m_2026",
        title="RSZ alternative financing net +198m 2026",
        entity_id="rsz",
        beneficiary="social security global management",
        legal_basis="KB alt finance BTW+RV MR 19 Dec 2025; Beleidsnota 1282/008",
        decision_date="2025-12-19",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="198000000",
        cash_by_year='{"2026_m": 198}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Compensate structural employer contribution reductions package",
        cut_option="Package FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSZ>alt_finance",
        notes="tick782 structural red + Plus Plans + sports exclude + horeca5/collective hours stop",
    ),
    C(
        commitment_id="cmt_tnw_oa_envelope_2026_29",
        title="VI/OA TNW responsabilization envelope 5-15pct path",
        entity_id="riziv",
        beneficiary="mutual OA / VI",
        legal_basis="TNW / ReAT wet; Beleidsnota 1282/008",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="0",
        cash_by_year='{"pct_2026": 5, "pct_2027": 7.5, "pct_2028": 10, "pct_2029": 15, "eur": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Link OA admin finance to return-to-work performance",
        cut_option="Euro base FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>RIZIV>TNW>OA",
        notes="tick782 entry 1 Jan 2027 criteria reform; euro base FOI",
    ),
    C(
        commitment_id="cmt_werkhervatting_premium_3k_2026",
        title="Work-resumption employer premium 3000 EUR/case",
        entity_id="riziv",
        beneficiary="employers",
        legal_basis="TNW policy; Beleidsnota 1282/008",
        decision_date="2026-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"unit_eur": 3000, "total": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Incentivise partial return after long illness",
        cut_option="Envelope FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RIZIV>TNW>premium",
        notes="tick782 unit only",
    ),
    C(
        commitment_id="cmt_ggmmi_raise_2026",
        title="GGMMI +35 EUR/mo 1 Apr 2026 (50 net)",
        entity_id="rsz",
        beneficiary="low-wage workers",
        legal_basis="Government agreement; Beleidsnota 1282/008",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"gross_eur_mo": 35, "net_eur_mo": 50, "total": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Raise minimum wage with net pass-through",
        cut_option="Fiscal cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSZ>GGMMI",
        notes="tick782 compensated via structural contribution reduction",
    ),
    C(
        commitment_id="cmt_ivt_alone_plus2_2026_28",
        title="IVT alone-living +2pct 2026 and 2028",
        entity_id="fod_sociale_zekerheid",
        beneficiary="IVT alone-living",
        legal_basis="Vulnerable groups envelope; Beleidsnota 1282/008",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2028",
        total_envelope_eur="0",
        cash_by_year='{"2026_pct": 2, "2028_pct": 2, "eur": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Poverty risk alone-living IVT",
        cut_option="Fiscal cost FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>SZ>IVT",
        notes="tick782",
    ),
    C(
        commitment_id="cmt_egov30_it_2026_29",
        title="e-Gov 3.0 RSZ digitalisation IT credits 2026-2029",
        entity_id="rsz",
        beneficiary="employers/digital SS",
        legal_basis="Government agreement; Beleidsnota 1282/008",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="0",
        cash_by_year='{"eur": "Unknown public"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Payroll-rhythm data + simplify employer filings",
        cut_option="IT FOI",
        source_id=SRC_MAIN,
        confidence="weak",
        hierarchy_path="Federal>RSZ>eGov30",
        notes="tick782 amounts FOI",
    ),
    C(
        commitment_id="cmt_dual_sociale_zaken_tick782",
        title="Dual Sociale Zaken 198m alt finance vs TNW/illness residual tick782",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/008",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"alt_delta_m": 198, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map SZ instruments dual to RSZ/RIZIV stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>sociale_zaken",
        notes="tick782",
    ),
]
exist_c = {r["commitment_id"] for r in crows}
for nc in new_c:
    if nc["commitment_id"] not in exist_c:
        crows.append(nc)
with cp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in cfields} for r in crows])

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
    return {
        k: v
        for k, v in {
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
        }.items()
        if k in lfields or True
    }


new_l = [
    lb(
        "lb_rsz_alt_finance_delta_198m_2026",
        "RSZ alt finance net +198m 2026",
        "transfer",
        "Federal>RSZ>alt_finance",
        "198000000",
        "198000000",
        "Strong primary net delta compensating employer RSZ cuts package",
        "strong",
        SRC_MAIN,
        "SS global",
        "4.0",
        "7.0",
        "2.5",
        "5.35",
        "Package FOI",
        "tick782",
    ),
    lb(
        "lb_tnw_oa_envelope_path_2026",
        "VI/OA TNW envelope 5-15pct path",
        "ops",
        "Federal>RIZIV>TNW>OA",
        "0",
        "0",
        "Medium percent path; euro base Unknown — FOI; performance-linked OA finance",
        "medium",
        SRC_MAIN,
        "mutual OA",
        "5.5",
        "6.5",
        "3.5",
        "5.45",
        "Euro base FOI",
        "tick782 pct only",
    ),
    lb(
        "lb_werkhervatting_premium_3k_2026",
        "Work-resumption premium 3000 EUR/case",
        "transfer",
        "Federal>RIZIV>TNW>premium",
        "3000",
        "0",
        "Strong unit rate; total cases Unknown",
        "strong",
        SRC_MAIN,
        "employers",
        "3.0",
        "4.0",
        "2.0",
        "3.40",
        "Envelope FOI",
        "tick782 unit",
    ),
    lb(
        "lb_ggmmi_raise_35_2026",
        "GGMMI +35 EUR/mo (50 net) 2026",
        "transfer",
        "Federal>RSZ>GGMMI",
        "0",
        "0",
        "Strong unit; total fiscal cost Unknown; compensated via structural cut",
        "strong",
        SRC_MAIN,
        "low-wage workers",
        "3.5",
        "6.0",
        "3.0",
        "4.40",
        "Fiscal cost FOI",
        "tick782",
    ),
    lb(
        "lb_meal_cheque_plus2_2026",
        "Meal cheques employer max +2 EUR 2026",
        "taxex",
        "Federal>taxex>meal_cheques",
        "0",
        "0",
        "Strong unit policy; stacks on ~1.07bn cheque economy residual",
        "strong",
        SRC_MAIN,
        "employees",
        "6.5",
        "7.5",
        "4.0",
        "6.25",
        "Taxex FOI",
        "tick782 dual cheque",
    ),
    lb(
        "lb_ivt_alone_plus2_2026",
        "IVT alone-living +2pct 2026/2028",
        "transfer",
        "Federal>SZ>IVT",
        "0",
        "0",
        "Medium policy; euro fiscal cost Unknown public",
        "medium",
        SRC_MAIN,
        "IVT alone",
        "2.5",
        "5.0",
        "2.5",
        "3.50",
        "Fiscal FOI",
        "tick782",
    ),
    lb(
        "lb_first_hire_red_reform_2026",
        "First-hire RSZ reduction reform 2026",
        "taxex",
        "Federal>RSZ>first_hires",
        "0",
        "0",
        "Strong unit rates 2000/1000 q; dual to existing 512.5m first-hire class",
        "strong",
        SRC_MAIN,
        "SMEs",
        "4.5",
        "7.0",
        "3.0",
        "5.20",
        "Reconcile FOI",
        "tick782",
    ),
    lb(
        "lb_egov30_it_unknown_2026",
        "e-Gov 3.0 RSZ IT credits 2026-2029 Unknown",
        "ops",
        "Federal>RSZ>eGov30",
        "0",
        "0",
        "Weak — credits stated without euro; FOI-adjacent L5",
        "weak",
        SRC_MAIN,
        "employers",
        "4.0",
        "5.5",
        "2.5",
        "4.20",
        "IT FOI",
        "tick782",
    ),
    lb(
        "lb_dual_sociale_zaken_2026",
        "Dual Sociale Zaken alt finance vs TNW residual",
        "transfer",
        "Belgium>dual>sociale_zaken",
        "198000000",
        "0",
        "Strong dual not TE-additive map SZ instruments",
        "strong",
        SRC_DUAL,
        "public",
        "4.5",
        "7.0",
        "3.5",
        "5.40",
        "L5 FOI",
        "tick782",
    ),
]
exist_l = {r["item_id"] for r in lrows}
for nl in new_l:
    row = {k: nl.get(k, "") for k in lfields}
    if row["item_id"] not in exist_l:
        lrows.append(row)
with lp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in lfields} for r in lrows])

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
                "hierarchy_path": "Federal>SZ>TNW_eGov_alt_L5",
                "entity_id": "fod_sociale_zekerheid",
                "what_is_missing": (
                    "Euro base behind VI/OA TNW envelope 5/7.5/10/15pct 2026-2029; e-Gov 3.0 IT "
                    "credit annual amounts 2026-2029; IVT alone +2pct fiscal cost 2026 and 2028; "
                    "work-resumption premium 3000 EUR total envelope/cases; GGMMI +35 compensation "
                    "cost within structural RSZ cut package; meal-cheque +2 total taxex delta; "
                    "centenindex private 50pct RSZ yield 2026; employer solidarity m4-5 recycle detail"
                ),
                "why_it_matters": (
                    "Sociale Zaken note public on rates/percents; residual euro L5 dual to RSZ alt "
                    "finance and RIZIV illness stacks opaque"
                ),
                "priority": "9",
                "recipient_body": "FOD Sociale Zekerheid / RSZ / RIZIV FOI",
                "recipient_email": "",
                "recipient_postal": "https://socialsecurity.belgium.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_rsz_alt_finance_delta_198m_2026|cmt_tnw_oa_envelope_2026_29|"
                    "cmt_egov30_it_2026_29|cmt_dual_sociale_zaken_tick782"
                ),
                "linked_leaderboard_id": (
                    "lb_rsz_alt_finance_delta_198m_2026|lb_tnw_oa_envelope_path_2026|"
                    "lb_egov30_it_unknown_2026|lb_dual_sociale_zaken_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick782 Kamer 1282/008 primary; human send only",
            }.items()
            if k in ffields
        }
    )
with fp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ffields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in ffields} for r in frows])

# --- research_queue ---
rp = Path("docs/doge/data/research_queue.csv")
with rp.open(encoding="utf-8", newline="") as f:
    rrows = list(csv.DictReader(f))
    rfields = list(rrows[0].keys())
for r in rrows:
    if r["task_id"] == "rq_773":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick782: SZ 1282/008 alt finance +198m GGMMI+35 meal+2 TNW OA 5-15pct "
            "work-resume 3k; FOI ready; spawn rq_774"
        )
if not any(r["task_id"] == "rq_774" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_774",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (local/regional/CoA or unmined "
                    "1282 notes); Sociale Zaken 1282/008 filled tick782"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick782 after rq_773",
            }.items()
            if k in rfields
        }
    )
with rp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in rfields} for r in rrows])

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
        "last_unit_id": "rq_773",
        "ticks_completed": "782",
        "paused": "no",
        "notes": "user paused=no; next rq_774; progress@790 in 8; rq_116 deferred",
    }
)
with lsp.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=lsfields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows([{k: (r.get(k) or "") for k in lsfields} for r in ls])

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
