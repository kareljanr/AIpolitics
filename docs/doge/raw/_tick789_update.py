# tick 789 — rq_781 Kamer DOC 56 1282/017 Beleidsnota Justitie residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T15:30:00Z"
SRC_MAIN = "src_kamer_beleid_justitie_1282_017_2026"
SRC_DUAL = "src_dual_justitie_tick789"
GAP = "gap_just_hefboom_childfocus_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282017.pdf"
ENT = "fod_justice"


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=fields, lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows([{k: (r.get(k) or "") for k in fields} for r in rows])


# entity check soft: fod_justice used widely
sp = Path("docs/doge/data/sources.csv")
with sp.open(encoding="utf-8", newline="") as f:
    srows = list(csv.DictReader(f))
    sfields = list(srows[0].keys())
if not any(r["source_id"] == SRC_MAIN for r in srows):
    srows.append(
        {
            "source_id": SRC_MAIN,
            "title": "Kamer DOC 56 1282/017 Beleidsnota Justitie residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Justitie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick789: Hefboomplan/Plan d'impulsion 21m extra magistrates/clerks; "
                "6.4m Brussels first-instance + courts of appeal; 7.2m fiscal/social fraud stack; "
                "financial prosecutor office under federal prosecutor; 1m victims financial aid "
                "commission + Childfocus legal subsidy; prison surpop recurrent 50m 2026 dual; "
                "interdept prison infra package 600m dual; 2025 one-off 55m of which 24.916m "
                "Justice; 4m 2025 staff safety (jammers/drones); 5m FOD Health + 5m Asylum "
                "internees/returns; 5m Regie buildings; nationality declaration fee 1000 EUR; "
                "raw 56K1282017_beleid_justitie.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Justitie Hefboom/courts vs prison package residual tick789",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: Hefboom 21m + courts 6.4m vs prison 50m/600m "
                "stacks already partial; fraud 7.2m dual"
            ),
        }
    )
write_csv(sp, sfields, srows)

bp = Path("docs/doge/data/budgets.csv")
with bp.open(encoding="utf-8", newline="") as f:
    brows = list(csv.DictReader(f))
    bfields = list(brows[0].keys())


def B(**kw):
    return {k: kw.get(k, "") for k in bfields}


new_b = [
    B(
        budget_id="bud_just_hefboom_21m",
        entity_id=ENT,
        year="2026",
        amount_eur="21000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Hefboomplan/Plan d'impulsion 21m extra for magistrates, greffiers, judicial staff; 186 magistrate + 1053 staff vacancies published; tick789 1282/017",
    ),
    B(
        budget_id="bud_just_courts_bru_appeal_6_4m",
        entity_id=ENT,
        year="2026",
        amount_eur="6400000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="6.4m invest NL+FR Brussels first instance + courts of appeal strengthen; tick789",
    ),
    B(
        budget_id="bud_just_fiscal_social_fraud_7_2m",
        entity_id=ENT,
        year="2026",
        amount_eur="7200000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="7.2m fiscal and social fraud combating strengthen + financial prosecutor office under federal prosecutor; tick789",
    ),
    B(
        budget_id="bud_just_victims_aid_commission_1m",
        entity_id=ENT,
        year="2026",
        amount_eur="1000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="1m strengthen Commission financial aid to victims; Childfocus legal subsidy organised (amount Unknown); tick789",
    ),
    B(
        budget_id="bud_just_prison_staff_safety_4m_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="4000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="4m 2025 short-term prison staff safety: ICT dogs, secure cells, GSM/drone jammers, 5G sweepers, drone detection; tick789",
    ),
    B(
        budget_id="bud_just_health_internees_5m_yr",
        entity_id="fod_sante",
        year="2026",
        amount_eur="5000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Annual 5m FOD Health for flow of internees to care institutions; dual 5m Asylum returns; tick789",
    ),
    B(
        budget_id="bud_just_asylum_returns_5m_yr",
        entity_id="fedasil",
        year="2026",
        amount_eur="5000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Annual 5m Asylum and Migration for return of sentenced without residence right; tick789 (entity dual IBZ/Fedasil class)",
    ),
    B(
        budget_id="bud_just_regie_5m_victim_spaces",
        entity_id="regie_gebouwen",
        year="2026",
        amount_eur="5000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="5m provided for Regie der Gebouwen (victim spaces / courthouse adaptations class in note); tick789",
    ),
    B(
        budget_id="bud_just_surpop_oneoff_justice_share_24_9m_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="24916000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Of 55m one-off 2025 surpop envelope MR 18 Jul 2025, 24.916m allocated to Justice; dual prior 55m total; tick789",
    ),
    B(
        budget_id="bud_nationality_declaration_fee_1000",
        entity_id=ENT,
        year="2025",
        amount_eur="1000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Nationality declaration contribution raised to 1000 EUR 2025; citizenship/language tests reform explore 2026 with federated entities; tick789",
    ),
    B(
        budget_id="bud_dual_justitie_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="21000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor Hefboom 21m class residual vs prison stacks; not TE-additive; tick789",
    ),
]
exist_b = {r["budget_id"] for r in brows}
for nb in new_b:
    if nb["budget_id"] not in exist_b:
        brows.append(nb)
write_csv(bp, bfields, brows)

cp = Path("docs/doge/data/commitments.csv")
with cp.open(encoding="utf-8", newline="") as f:
    crows = list(csv.DictReader(f))
    cfields = list(crows[0].keys())


def C(**kw):
    return {k: kw.get(k, "") for k in cfields}


new_c = [
    C(
        commitment_id="cmt_just_hefboom_21m",
        title="Hefboomplan 21m judicial recruitment",
        entity_id=ENT,
        beneficiary="judiciary staff",
        legal_basis="Hefboomplan / Plan d'impulsion; Beleidsnota 1282/017",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="21000000",
        cash_by_year='{"envelope_m": 21, "vacancies_mag": 186, "vacancies_staff": 1053}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Strengthen judicial order with extra magistrates and staff",
        cut_option="Recruitment FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Justice>Hefboom",
        notes="tick789",
    ),
    C(
        commitment_id="cmt_just_financial_prosecutor",
        title="Financial prosecutor office under federal prosecutor",
        entity_id=ENT,
        beneficiary="economic crime enforcement",
        legal_basis="Beleidsnota 1282/017; 7.2m fraud stack",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="7200000",
        cash_by_year='{"fraud_stack_m": 7.2}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Exclusive independent prosecute economic/financial/fiscal/social fraud/corruption",
        cut_option="Org FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Justice>financial_prosecutor",
        notes="tick789",
    ),
    C(
        commitment_id="cmt_childfocus_legal_subsidy",
        title="Childfocus legal subsidy structural anchoring",
        entity_id=ENT,
        beneficiary="Child Focus",
        legal_basis="Beleidsnota 1282/017",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"eur": "Unknown public", "with_victims_1m": true}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Statutory subsidy for Childfocus general-interest tasks",
        cut_option="Amount FOI",
        source_id=SRC_MAIN,
        confidence="weak",
        hierarchy_path="Federal>Justice>Childfocus",
        notes="tick789 amount FOI",
    ),
    C(
        commitment_id="cmt_just_internees_returns_5m_5m",
        title="Internees care 5m + returns 5m annual",
        entity_id=ENT,
        beneficiary="internees / foreign sentenced",
        legal_basis="Beleidsnota 1282/017",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="10000000",
        cash_by_year='{"health_m": 5, "asylum_m": 5}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Flow internees to care and return non-resident convicts",
        cut_option="Outcome FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Justice>detention_flow",
        notes="tick789",
    ),
    C(
        commitment_id="cmt_dual_justitie_tick789",
        title="Dual Justitie Hefboom vs prison residual tick789",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/017",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"hefboom_m": 21, "courts_m": 6.4, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map justice recruitment dual to prison stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>justitie",
        notes="tick789",
    ),
]
exist_c = {r["commitment_id"] for r in crows}
for nc in new_c:
    if nc["commitment_id"] not in exist_c:
        crows.append(nc)
write_csv(cp, cfields, crows)

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
        "lb_just_hefboom_21m",
        "Hefboomplan judicial recruitment 21m",
        "ops",
        "Federal>Justice>Hefboom",
        "21000000",
        "21000000",
        "Strong primary extra staff envelope; vacancy path 186+1053",
        "strong",
        SRC_MAIN,
        "judiciary",
        "3.0",
        "6.0",
        "2.5",
        "4.35",
        "Recruitment FOI",
        "tick789",
    ),
    lb(
        "lb_just_courts_6_4m",
        "Brussels courts + appeals strengthen 6.4m",
        "ops",
        "Federal>Justice>courts",
        "6400000",
        "6400000",
        "Strong primary invest",
        "strong",
        SRC_MAIN,
        "courts",
        "2.5",
        "5.0",
        "2.0",
        "3.55",
        "Ops FOI",
        "tick789",
    ),
    lb(
        "lb_just_fraud_7_2m",
        "Fiscal/social fraud + financial prosecutor 7.2m",
        "ops",
        "Federal>Justice>fraud",
        "7200000",
        "7200000",
        "Strong primary stack for financial prosecutor path",
        "strong",
        SRC_MAIN,
        "public",
        "3.5",
        "5.0",
        "3.0",
        "4.15",
        "Org FOI",
        "tick789",
    ),
    lb(
        "lb_just_victims_1m_childfocus",
        "Victims aid 1m + Childfocus subsidy Unknown",
        "transfer",
        "Federal>Justice>victims",
        "1000000",
        "1000000",
        "Strong 1m; Childfocus legal subsidy amount FOI",
        "medium",
        SRC_MAIN,
        "victims/children",
        "2.5",
        "4.0",
        "2.0",
        "3.20",
        "Subsidy FOI",
        "tick789",
    ),
    lb(
        "lb_just_internees_returns_10m",
        "Internees care + returns 5m+5m annual",
        "transfer",
        "Federal>Justice>detention_flow",
        "10000000",
        "10000000",
        "Strong dual Health/Asylum envelopes",
        "strong",
        SRC_MAIN,
        "internees",
        "4.0",
        "5.5",
        "3.0",
        "4.55",
        "Outcome FOI",
        "tick789",
    ),
    lb(
        "lb_just_prison_safety_4m_2025",
        "Prison staff safety investments 4m 2025",
        "ops",
        "Federal>Justice>prisons",
        "4000000",
        "4000000",
        "Strong primary short-term security kit",
        "strong",
        SRC_MAIN,
        "prison staff",
        "3.0",
        "4.0",
        "2.0",
        "3.40",
        "Ops FOI",
        "tick789",
    ),
    lb(
        "lb_dual_justitie_2026",
        "Dual Justitie Hefboom vs prison residual",
        "ops",
        "Belgium>dual>justitie",
        "21000000",
        "0",
        "Strong dual not TE-additive map justice instruments",
        "strong",
        SRC_DUAL,
        "public",
        "4.0",
        "6.0",
        "3.0",
        "4.80",
        "L5 FOI",
        "tick789",
    ),
]
exist_l = {r["item_id"] for r in lrows}
for nl in new_l:
    if nl["item_id"] not in exist_l:
        lrows.append(nl)
write_csv(lp, lfields, lrows)

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
                "hierarchy_path": "Federal>Justice>Hefboom_Childfocus_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Hefboom 21m: FTE fill rate vs 186/1053 vacancies and multi-year cash; "
                    "Childfocus legal subsidy annual amount and conditions; financial prosecutor "
                    "office budget/FTE within 7.2m; 6.4m courts allocation detail; Regie 5m "
                    "victim-space works list; internees/returns 5+5m outcome KPIs; nationality "
                    "fee 1000 EUR volume and revenue 2025-26"
                ),
                "why_it_matters": (
                    "Justice note fills recruitment residual; Childfocus and financial prosecutor "
                    "euro detail dual to prison stacks opaque"
                ),
                "priority": "8",
                "recipient_body": "FOD Justitie FOI",
                "recipient_email": "",
                "recipient_postal": "https://justitie.belgium.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_just_hefboom_21m|cmt_just_financial_prosecutor|"
                    "cmt_childfocus_legal_subsidy|cmt_dual_justitie_tick789"
                ),
                "linked_leaderboard_id": (
                    "lb_just_hefboom_21m|lb_just_fraud_7_2m|"
                    "lb_just_victims_1m_childfocus|lb_dual_justitie_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick789 Kamer 1282/017 primary; human send only",
            }.items()
            if k in ffields
        }
    )
write_csv(fp, ffields, frows)

rp = Path("docs/doge/data/research_queue.csv")
with rp.open(encoding="utf-8", newline="") as f:
    rrows = list(csv.DictReader(f))
    rfields = list(rrows[0].keys())
for r in rrows:
    if r["task_id"] == "rq_781":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick789: Justitie 1282/017 Hefboom 21m courts 6.4m fraud 7.2m victims 1m; "
            "FOI ready; next rq_780 PROGRESS@790"
        )
write_csv(rp, rfields, rrows)

lsp = Path("docs/doge/data/loop_state.csv")
with lsp.open(encoding="utf-8", newline="") as f:
    ls = list(csv.DictReader(f))
    lsfields = list(ls[0].keys())
ls[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_781",
        "ticks_completed": "789",
        "paused": "no",
        "notes": "user paused=no; NEXT rq_780 MANDATORY progress@790; then residual; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
