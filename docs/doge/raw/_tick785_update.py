# tick 785 — rq_776 Kamer DOC 56 1282/014 Beleidsnota Pensioenen
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T13:30:00Z"
SRC_MAIN = "src_kamer_beleid_pensioenen_1282_014_2026"
SRC_DUAL = "src_dual_pensioenen_tick785"
GAP = "gap_pens_wijninckx_statut_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282014.pdf"


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=fields, lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows([{k: (r.get(k) or "") for k in fields} for r in rows])


sp = Path("docs/doge/data/sources.csv")
with sp.open(encoding="utf-8", newline="") as f:
    srows = list(csv.DictReader(f))
    sfields = list(srows[0].keys())
if not any(r["source_id"] == SRC_MAIN for r in srows):
    srows.append(
        {
            "source_id": SRC_MAIN,
            "title": "Kamer DOC 56 1282/014 Beleidsnota Pensioenen residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Pensioenen (Jambon)",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick785: pension spend 8.7pct GDP 2005 to 11.3pct 2024; SCvV Jul2025 "
                "Arizona reform halves ageing-cost rise 3.6pp to 1.7pp GDP 2024-70 (path still "
                "27.05pct GDP ageing social 2070); EC Ageing Report uncorrected 31.9pct GDP 2070 "
                "and +5.1pp vs EU +1.2pp; Wijninckx contrib 3to12.5pct from 2026; solidarity "
                "2to4pct above 150k capital from Jul2027; high pension index freeze above 5250eur "
                "and Wijninckx ceiling 8291eur freeze; new federal statutory employer pension "
                "contrib to 38pct by 2029 from Jul2026; 2nd pillar 3pct employer by 2035; "
                "POZ 4.4pct insurance tax abolished; raw 56K1282014_beleid_pensioenen.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Pensioenen reform instruments vs SCvV path residual tick785",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: 11.3pct GDP pension stack vs Wijninckx/solidarity "
                "rates; statutory 38pct contrib dual FPD; SCvV 3.6to1.7pp vs prior 1.3-1.4pp notes"
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
        budget_id="bud_pens_gdp_share_11_3pct_2024_note",
        entity_id="fpd",
        year="2024",
        amount_eur="",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Pension spend share GDP 11.3pct 2024 (from 8.7pct 2005 NAR 2023); dual existing CEV ~72.5bn; tick785 1282/014",
    ),
    B(
        budget_id="bud_scvv_ageing_cost_path_3_6pp_uncorrected",
        entity_id="fpd",
        year="2070",
        amount_eur="",
        basis="projected",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="SCvV Jul2025: uncorrected ageing-cost rise +3.6pp GDP 2024-2070; Arizona reform cuts to +1.7pp; tick785",
    ),
    B(
        budget_id="bud_scvv_ageing_cost_path_1_7pp_reformed",
        entity_id="fpd",
        year="2070",
        amount_eur="",
        basis="projected",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="SCvV Jul2025 reformed path +1.7pp GDP ageing cost 2024-70; ageing social still 27.05pct GDP 2070; tick785",
    ),
    B(
        budget_id="bud_ec_ageing_social_31_9pct_gdp_2070",
        entity_id="fpd",
        year="2070",
        amount_eur="",
        basis="projected",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="EC Ageing Report 2024: BE ageing-related social spend 31.9pct GDP 2070 uncorrected; +5.1pp 2022-70 vs EU +1.2pp; tick785",
    ),
    B(
        budget_id="bud_wijninckx_contrib_rate_12_5pct_2026",
        entity_id="fpd",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Wijninckx social contribution on high supplementary capital premia 3pct to 12.5pct from contribution year 2026; yield Unknown; tick785",
    ),
    B(
        budget_id="bud_solidarity_capital_rate_4pct_2027",
        entity_id="fpd",
        year="2027",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Solidarity contribution on high pension capital 2pct to 4pct above 150000 EUR threshold from 1 Jul 2027; yield Unknown; tick785",
    ),
    B(
        budget_id="bud_solidarity_capital_threshold_150k",
        entity_id="fpd",
        year="2027",
        amount_eur="150000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Solidarity contribution threshold capital 150000 EUR; tick785",
    ),
    B(
        budget_id="bud_high_pension_index_freeze_threshold_5250",
        entity_id="fpd",
        year="2026",
        amount_eur="5250",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Indexation of legal pensions temporarily limited above 5250 EUR/mo this legislature; tick785",
    ),
    B(
        budget_id="bud_wijninckx_ceiling_8291_freeze",
        entity_id="fpd",
        year="2026",
        amount_eur="8291",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Absolute Wijninckx ceiling public servants 8291 EUR index freeze temporary this legislature; tick785",
    ),
    B(
        budget_id="bud_statut_employer_pens_contrib_38pct_2029",
        entity_id="fpd",
        year="2029",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="New federal statutory appointments after 31 May 2026: employer pension contribution rising to 38pct by 2029 from 1 Jul 2026; collected RSZ to FPD; yield Unknown; tick785",
    ),
    B(
        budget_id="bud_pillar2_employer_target_3pct_2035",
        entity_id="fod_emploi",
        year="2035",
        amount_eur="",
        basis="target",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Policy target all private employees supplementary pension employer contrib min 3pct by 2035; NAR advice by 1 Sep 2026; tick785",
    ),
    B(
        budget_id="bud_poz_insurance_tax_4_4pct_abolished",
        entity_id="fod_finance",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="POZ/CPTI insurance operations tax 4.4pct abolished (government agreement); yield foregone Unknown; tick785",
    ),
    B(
        budget_id="bud_centenindex_pension_threshold_2000_014",
        entity_id="fpd",
        year="2026",
        amount_eur="2000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Centenindex applies pensions above 2000 EUR/mo (2026 and 2028); dual SZ note; tick785",
    ),
    B(
        budget_id="bud_dual_pensioenen_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="72547356000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor existing CEV pension ~72.5bn / 11.3pct GDP class + reform rates; not TE-additive; tick785",
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
        commitment_id="cmt_arizona_pension_reform_2026_27",
        title="Arizona pension reform implement 2026 / main 2027",
        entity_id="fpd",
        beneficiary="all pension regimes",
        legal_basis="Summer deal 2025; Arizona pensioenwet draft; Beleidsnota 1282/014",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2031",
        total_envelope_eur="0",
        cash_by_year='{"scvv_pp_uncorrected": 3.6, "scvv_pp_reformed": 1.7, "ageing_social_2070_pct": 27.05}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Halve ageing-cost rise; strengthen work-pension link",
        cut_option="Impact FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>FPD>arizona_reform",
        notes="tick785 bonus/malus from 2027; assimilated periods 40to20pct path",
    ),
    C(
        commitment_id="cmt_wijninckx_12_5pct_2026",
        title="Wijninckx contribution 3 to 12.5pct from 2026",
        entity_id="fpd",
        beneficiary="high supplementary capital",
        legal_basis="Wet diverse bepalingen; Beleidsnota 1282/014",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"rate_from": 3, "rate_to": 12.5, "yield": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Higher SS contribution on very high 2nd-pillar premia",
        cut_option="Yield FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>FPD>wijninckx",
        notes="tick785",
    ),
    C(
        commitment_id="cmt_solidarity_capital_4pct_2027",
        title="Solidarity contrib 4pct above 150k capital from Jul 2027",
        entity_id="fpd",
        beneficiary="high pension capital holders",
        legal_basis="Wet diverse bepalingen; Beleidsnota 1282/014",
        decision_date="2025-01-01",
        start_year="2027",
        end_year="2027",
        total_envelope_eur="0",
        cash_by_year='{"rate_from": 2, "rate_to": 4, "threshold_eur": 150000, "yield": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Mobilise high pension capital for system financing",
        cut_option="Yield FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>FPD>solidarity_capital",
        notes="tick785",
    ),
    C(
        commitment_id="cmt_statut_employer_pens_38pct_2029",
        title="Federal statutory employer pension contrib to 38pct 2029",
        entity_id="fpd",
        beneficiary="new federal statutory staff",
        legal_basis="Beleidsnota 1282/014",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="0",
        cash_by_year='{"start": "2026-07-01", "peak_pct": 38, "eligible": "new after 2026-05-31 federal only"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Full cost coverage of statutory retirement pension",
        cut_option="Yield FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>FPD>statut_employer",
        notes="tick785 RSZ collects to FPD; not regions/pool parastatals",
    ),
    C(
        commitment_id="cmt_pillar2_3pct_2035",
        title="Private 2nd pillar employer min 3pct by 2035",
        entity_id="fod_emploi",
        beneficiary="private employees",
        legal_basis="Government agreement; Beleidsnota 1282/014",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2035",
        total_envelope_eur="0",
        cash_by_year='{"target_pct": 3, "nar_advice_due": "2026-09-01"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Universal supplementary pension coverage",
        cut_option="Path FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>WASO>pillar2",
        notes="tick785 dual workers/employees harmonisation by 2029",
    ),
    C(
        commitment_id="cmt_dual_pensioenen_tick785",
        title="Dual Pensioenen 11.3pct GDP vs Wijninckx/statut residual tick785",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/014",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"gdp_pct_2024": 11.3, "scvv_pp": "3.6to1.7", "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map pension reform rates dual to spend stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>pensioenen",
        notes="tick785",
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
        "lb_scvv_ageing_3_6_to_1_7pp",
        "SCvV ageing cost 3.6pp to 1.7pp GDP via Arizona",
        "ops",
        "Federal>FPD>ageing_path",
        "0",
        "0",
        "Strong SCvV Jul2025 primary; dual prior 1.3-1.4pp reform notes",
        "strong",
        SRC_MAIN,
        "public finance",
        "5.0",
        "9.0",
        "5.0",
        "6.80",
        "Impact FOI",
        "tick785",
    ),
    lb(
        "lb_wijninckx_12_5pct_2026",
        "Wijninckx high capital contrib 12.5pct 2026",
        "taxex",
        "Federal>FPD>wijninckx",
        "0",
        "0",
        "Strong rate 3to12.5pct; absolute yield Unknown — FOI",
        "strong",
        SRC_MAIN,
        "high 2nd pillar",
        "4.5",
        "6.5",
        "3.0",
        "5.20",
        "Yield FOI",
        "tick785",
    ),
    lb(
        "lb_solidarity_capital_4pct_2027",
        "Solidarity 4pct above 150k pension capital 2027",
        "taxex",
        "Federal>FPD>solidarity",
        "0",
        "0",
        "Strong rate/threshold; yield Unknown",
        "strong",
        SRC_MAIN,
        "high capital",
        "4.0",
        "6.0",
        "3.0",
        "4.90",
        "Yield FOI",
        "tick785",
    ),
    lb(
        "lb_statut_employer_pens_38pct",
        "Federal statutory employer pens contrib to 38pct",
        "ops",
        "Federal>FPD>statut",
        "0",
        "0",
        "Strong policy path Jul2026-2029; euro yield Unknown",
        "strong",
        SRC_MAIN,
        "federal employers",
        "5.0",
        "7.0",
        "3.5",
        "5.65",
        "Yield FOI",
        "tick785",
    ),
    lb(
        "lb_high_pension_index_freeze_5250",
        "High pension index freeze above 5250 EUR/mo",
        "transfer",
        "Federal>FPD>index",
        "0",
        "0",
        "Strong temporary freeze this legislature; savings Unknown",
        "strong",
        SRC_MAIN,
        "high pensioners",
        "4.0",
        "6.5",
        "2.5",
        "4.95",
        "Savings FOI",
        "tick785",
    ),
    lb(
        "lb_pillar2_3pct_target_2035",
        "2nd pillar employer min 3pct target 2035",
        "taxex",
        "Federal>WASO>pillar2",
        "0",
        "0",
        "Medium multi-year target; NAR path pending",
        "medium",
        SRC_MAIN,
        "private employees",
        "3.5",
        "7.0",
        "4.0",
        "5.15",
        "Path FOI",
        "tick785",
    ),
    lb(
        "lb_poz_tax_4_4pct_abolished",
        "POZ insurance tax 4.4pct abolished",
        "taxex",
        "Federal>taxex>POZ",
        "0",
        "0",
        "Strong abolition; foregone revenue Unknown",
        "strong",
        SRC_MAIN,
        "self-employed",
        "4.0",
        "5.0",
        "2.5",
        "4.25",
        "Revenue FOI",
        "tick785",
    ),
    lb(
        "lb_dual_pensioenen_2026",
        "Dual Pensioenen 11.3pct GDP vs reform rates",
        "transfer",
        "Belgium>dual>pensioenen",
        "72547356000",
        "0",
        "Strong dual not TE-additive map reform instruments",
        "strong",
        SRC_DUAL,
        "public",
        "4.5",
        "9.0",
        "4.0",
        "6.45",
        "L5 FOI",
        "tick785",
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
                "hierarchy_path": "Federal>FPD>wijninckx_statut_L5",
                "entity_id": "fpd",
                "what_is_missing": (
                    "Absolute euro yield of Wijninckx 12.5pct 2026+; solidarity 4pct above "
                    "150k from Jul2027; federal statutory employer pension contribution ramp "
                    "to 38pct (2026-2029 cash path and FTE base); savings from high-pension "
                    "index freeze above 5250 and Wijninckx ceiling 8291 freeze; POZ 4.4pct tax "
                    "foregone revenue; SCvV Arizona reform euro bridge from 3.6pp to 1.7pp GDP; "
                    "reconcile with existing ~72.5bn pension stack"
                ),
                "why_it_matters": (
                    "Pension reform rates public; residual euro yields dual to 11.3pct GDP "
                    "stack opaque"
                ),
                "priority": "9",
                "recipient_body": "Federale Pensioendienst / FOD Financiën FOI",
                "recipient_email": "",
                "recipient_postal": "https://www.sfpd.fgov.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_arizona_pension_reform_2026_27|cmt_wijninckx_12_5pct_2026|"
                    "cmt_solidarity_capital_4pct_2027|cmt_statut_employer_pens_38pct_2029|"
                    "cmt_dual_pensioenen_tick785"
                ),
                "linked_leaderboard_id": (
                    "lb_scvv_ageing_3_6_to_1_7pp|lb_wijninckx_12_5pct_2026|"
                    "lb_statut_employer_pens_38pct|lb_dual_pensioenen_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick785 Kamer 1282/014 primary; human send only",
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
    if r["task_id"] == "rq_776":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick785: Pensioenen 1282/014 Wijninckx 12.5pct solidarity 4pct statut 38pct "
            "SCvV 3.6to1.7pp; FOI ready; spawn rq_777"
        )
if not any(r["task_id"] == "rq_777" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_777",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (Asiel 1282/038, Economie 004, "
                    "Defensie 022, local/CoA); Pensioenen 1282/014 filled tick785"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick785 after rq_776",
            }.items()
            if k in rfields
        }
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
        "last_unit_id": "rq_776",
        "ticks_completed": "785",
        "paused": "no",
        "notes": "user paused=no; next rq_777; progress@790 in 5; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
