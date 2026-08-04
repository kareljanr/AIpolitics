# tick 791 — rq_782 Kamer DOC 56 1282/026 Beleidsnota Klimaat residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T16:30:00Z"
SRC_MAIN = "src_kamer_beleid_klima_1282_026_2026"
SRC_DUAL = "src_dual_klima_skf_tick791"
GAP = "gap_fed_skf_cofin_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282026.pdf"
ENT = "fod_sante"  # SPF Santé / Environnement admin path for federal climate note


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
            "title": "Kamer DOC 56 1282/026 Beleidsnota Klimaat residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Klimaat Ecologische Transitie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick791: Plan social climat BE envelope estimated 2.21bn EUR 2026-2032 "
                "(1.66bn / 75pct Fonds Social pour le Climat + 0.55bn / 25pct mandatory BE cofin); "
                "Overlegcomité/Comité de Concertation 6 Oct 2025 allocation key: federal 13.13pct "
                "= 217m of EU SKF share (1.66bn*13.13pct~217.96m); federal cofinancing ~72m "
                "2026-2032 inscribed 2026 budget conclave notifications; NEH/NEAP 3rd plan pilot "
                "call Sep 2025 envelope 600k hospital single-use reduction (start Feb class); "
                "dual prior tick698 VL SKF 958.8m + BE EU 1656.3m; raw 56K1282026_beleid_klima.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual federal SKF 217m/72m vs VL SKF 958.8m residual tick791",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: BE SKF total 2.21bn (EU 1.66 + cofin 0.55) dual "
                "VL envelope 958.8m + federal share 217m EU + ~72m cofin + residual WAL/BCR; "
                "prior EC filing lag dual tick698; 600k NEH pilot separate small"
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
        budget_id="bud_be_skf_total_2_21bn_2026_2032",
        entity_id="gg_belgium",
        year="2032",
        amount_eur="2210000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "BE Plan social climat estimated total 2.21bn EUR available 2026-2032 "
            "(1.66bn CSF EU 75pct + 0.55bn BE cofin 25pct); Kamer 1282/026 p10; tick791"
        ),
    ),
    B(
        budget_id="bud_be_skf_eu_1_66bn_2026_2032",
        entity_id="gg_belgium",
        year="2032",
        amount_eur="1660000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "BE SKF EU Fonds Social pour le Climat share 1.66bn 75pct of 2.21bn; "
            "dual prior bud_be_skf_eu_share_1656_3m CoA 1656.3m (rounding); tick791"
        ),
    ),
    B(
        budget_id="bud_be_skf_cofin_0_55bn_2026_2032",
        entity_id="gg_belgium",
        year="2032",
        amount_eur="550000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "BE mandatory national cofinancing 0.55bn 25pct of SKF plan 2026-2032; "
            "entity split residual FOI; tick791"
        ),
    ),
    B(
        budget_id="bud_fed_skf_eu_share_217m_2026_2032",
        entity_id=ENT,
        year="2032",
        amount_eur="217000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Federal allocation 13.13pct of BE SKF EU share = 217m 2026-2032 "
            "(Comité de Concertation 6 Oct 2025); of EU 1.66bn not of total 2.21bn; tick791"
        ),
    ),
    B(
        budget_id="bud_fed_skf_cofin_72m_2026_2032",
        entity_id=ENT,
        year="2032",
        amount_eur="72000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Federal SKF cofinancing ~72m EUR 2026-2032 inscribed 2026 budget conclave "
            "notifications; residual cash-by-year L5 FOI; tick791"
        ),
    ),
    B(
        budget_id="bud_fed_skf_fed_package_289m_class",
        entity_id=ENT,
        year="2032",
        amount_eur="289000000",
        basis="derived",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "Illustrative federal SKF package class 217m EU + ~72m cofin = ~289m 2026-2032; "
            "not separate appropriation; tick791"
        ),
    ),
    B(
        budget_id="bud_neh_hospital_single_use_pilot_600k",
        entity_id=ENT,
        year="2025",
        amount_eur="600000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "3rd National Environment-Health Plan call Sep 2025 envelope 600k for hospital "
            "pilots reducing single-use products (start Feb class); tick791 1282/026 p26"
        ),
    ),
    B(
        budget_id="bud_dual_klima_skf_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="2210000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual map anchor BE SKF 2.21bn residual vs VL 958.8m + federal 217/72; "
            "not TE-additive; tick791"
        ),
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
        commitment_id="cmt_be_skf_plan_2_21bn",
        title="BE Social Climate Plan total envelope 2.21bn 2026-2032",
        entity_id="gg_belgium",
        beneficiary="vulnerable households micro-enterprises ETS2",
        legal_basis="EU Social Climate Fund + Beleidsnota 1282/026; Concertation 2025-10-06",
        decision_date="2025-10-06",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="2210000000",
        cash_by_year='{"total_bn": 2.21, "eu_bn": 1.66, "cofin_bn": 0.55, "eu_pct": 75, "cofin_pct": 25}',
        remaining_eur="2210000000",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="ETS2 social cushion Plan social climat / Sociaal klimaatplan",
        cut_option="Measure L5 FOI + EC filing",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Belgium>EU>SKF",
        notes="tick791 primary Kamer; dual prior CoA 1656.3m EU",
    ),
    C(
        commitment_id="cmt_fed_skf_eu_217m",
        title="Federal SKF EU allocation 217m 13.13pct",
        entity_id=ENT,
        beneficiary="federal SKF measures",
        legal_basis="Comité de Concertation 2025-10-06; Beleidsnota 1282/026",
        decision_date="2025-10-06",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="217000000",
        cash_by_year='{"fed_share_pct": 13.13, "of": "eu_1.66bn", "eur": 217000000}',
        remaining_eur="217000000",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Federal share of BE SKF EU envelope",
        cut_option="Cash-by-year + measure list FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Climate>SKF_EU",
        notes="tick791",
    ),
    C(
        commitment_id="cmt_fed_skf_cofin_72m",
        title="Federal SKF cofinancing ~72m 2026-2032",
        entity_id=ENT,
        beneficiary="federal SKF measures",
        legal_basis="Budget conclave 2026 notifications; Beleidsnota 1282/026",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="72000000",
        cash_by_year='{"cofin_m": 72, "period": "2026-2032", "approx": true}',
        remaining_eur="72000000",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Mandatory national cofinancing federal slice",
        cut_option="Annual path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Climate>SKF_cofin",
        notes="tick791",
    ),
    C(
        commitment_id="cmt_neh_hospital_pilot_600k",
        title="NEH hospital single-use reduction pilot 600k",
        entity_id=ENT,
        beneficiary="hospitals pilot projects",
        legal_basis="3rd Plan National Environnement-Santé; Beleidsnota 1282/026",
        decision_date="2025-09-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="600000",
        cash_by_year='{"envelope_eur": 600000, "call": "2025-09", "start_class": "2026-02"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reduce single-use products in hospitals via pilots",
        cut_option="Project list FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Environment>NEH_pilot",
        notes="tick791",
    ),
    C(
        commitment_id="cmt_dual_klima_skf_tick791",
        title="Dual Klima SKF federal vs VL residual tick791",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/026 dual CoA VL SKF",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="0",
        cash_by_year='{"be_total_bn": 2.21, "fed_eu_m": 217, "fed_cofin_m": 72, "vl_m": 958.8, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map federal SKF residual dual to VL SKF stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>SKF",
        notes="tick791",
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
    goal="see",
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
        "stated_goal": goal,
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


# priority_index rough: (abs+cost)/2 style used in prior ticks — keep moderate
new_l = [
    lb(
        "lb_be_skf_total_2_21bn",
        "BE Social Climate Plan total 2.21bn 2026-2032",
        "transfer",
        "Belgium>EU>SKF",
        "315714286",  # illustrative 2.21bn/7yr
        "2210000000",
        "Strong primary total; EU 1.66 + cofin 0.55; dual VL 958.8; multi-year not pure annual waste",
        "strong",
        SRC_MAIN,
        "ETS2 vulnerable groups",
        "4.0",
        "9.0",
        "4.0",
        "6.50",
        "Publish full measure cash calendar + EC status",
        "tick791",
        goal="ETS2 social cushion national plan",
    ),
    lb(
        "lb_fed_skf_eu_217m",
        "Federal SKF EU allocation 217m opaque L5",
        "transfer",
        "Federal>Climate>SKF_EU",
        "31000000",  # 217/7 approx
        "217000000",
        "Strong primary 13.13pct Concertation; measure list and annual cash FOI residual",
        "strong",
        SRC_MAIN,
        "federal SKF recipients",
        "5.5",
        "7.5",
        "3.0",
        "6.15",
        "L5 measure matrix FOI",
        "tick791",
        goal="Federal EU SKF share",
    ),
    lb(
        "lb_fed_skf_cofin_72m",
        "Federal SKF cofinancing ~72m multi-year",
        "transfer",
        "Federal>Climate>SKF_cofin",
        "10285714",
        "72000000",
        "Strong primary conclave path; annual split Unknown",
        "strong",
        SRC_MAIN,
        "federal SKF recipients",
        "5.0",
        "6.5",
        "2.5",
        "5.50",
        "Annual path FOI",
        "tick791",
        goal="Federal cofin SKF",
    ),
    lb(
        "lb_neh_hospital_pilot_600k",
        "NEH hospital single-use pilot 600k",
        "ops",
        "Federal>Environment>NEH_pilot",
        "600000",
        "600000",
        "Strong primary small pilot envelope; project list residual",
        "strong",
        SRC_MAIN,
        "hospitals",
        "2.0",
        "3.0",
        "1.5",
        "2.35",
        "Project outcomes FOI",
        "tick791",
        goal="Reduce hospital single-use products",
    ),
    lb(
        "lb_dual_klima_skf_2026",
        "Dual federal SKF vs VL SKF residual",
        "ops",
        "Belgium>dual>SKF",
        "0",
        "2210000000",
        "Strong dual not TE-additive; fed 217+72 vs VL 958.8 within BE 2.21",
        "strong",
        SRC_DUAL,
        "multi-level",
        "5.0",
        "8.0",
        "3.5",
        "6.20",
        "Cross-entity cash FOI",
        "tick791",
        goal="Dual climate fund residual map",
    ),
]
exist_l = {r["item_id"] for r in lrows}
for nl in new_l:
    if nl["item_id"] not in exist_l:
        lrows.append(nl)
write_csv(lp, lfields, lrows)

# FOI queue
fp = Path("docs/doge/data/foi_queue.csv")
with fp.open(encoding="utf-8", newline="") as f:
    frows = list(csv.DictReader(f))
    ffields = list(frows[0].keys())

foi_row = {
    "gap_id": GAP,
    "hierarchy_path": "Federal>Climate>SKF_cofin_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "Federal SKF L5: cash-by-year 2026-2032 behind 217m EU share + ~72m cofin; "
        "named federal measures and beneficiary classes; bridge 13.13pct key vs regional "
        "shares (VL 43.4pct prior CoA); EC Social Climate Plan filing status after "
        "beleidsnota; NEH 600k pilot awarded project list and outcomes"
    ),
    "why_it_matters": (
        "Primary Kamer confirms federal slice of multi-bn SKF; residual L5 dual VL stack "
        "and prior EC lag; multi-year opacity"
    ),
    "priority": "8",
    "recipient_body": "FOD Volksgezondheid / Climate office / Begroting",
    "recipient_email": "",
    "recipient_postal": "https://www.health.belgium.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_fed_skf_eu_217m|cmt_fed_skf_cofin_72m|cmt_be_skf_plan_2_21bn",
    "linked_leaderboard_id": "lb_fed_skf_eu_217m|lb_fed_skf_cofin_72m|lb_be_skf_total_2_21bn",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick791 Kamer 1282/026 primary; human send only",
}
# normalize to fields
foi_row = {k: foi_row.get(k, "") for k in ffields}
if not any(r["gap_id"] == GAP for r in frows):
    frows.append(foi_row)
else:
    frows = [foi_row if r["gap_id"] == GAP else r for r in frows]
write_csv(fp, ffields, frows)

# research queue
rp = Path("docs/doge/data/research_queue.csv")
with rp.open(encoding="utf-8", newline="") as f:
    rrows = list(csv.DictReader(f))
    rfields = list(rrows[0].keys())

for r in rrows:
    if r["task_id"] == "rq_782":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick791 Klima 1282/026 SKF 2.21bn fed 217m+72m NEH 600k FOI gap_fed_skf_cofin_l5"
        )

# spawn next residual: Asiel 038 was named in progress@790 notes
NEXT = "rq_783"
if not any(r["task_id"] == NEXT for r in rrows):
    rrows.append(
        {
            "task_id": NEXT,
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (Asiel 1282/038, local/CoA, "
                "or other 1282/* not yet mined); prefer FOI-adjacent L5"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick791 after Klima",
        }
    )
# normalize keys
rrows = [{k: (r.get(k) or "") for k in rfields} for r in rrows]
write_csv(rp, rfields, rrows)

# loop state
lp_state = Path("docs/doge/data/loop_state.csv")
lp_state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},rq_782,791,no,"
    "user paused=no; next rq_783 Asiel038/local; progress@800 in 9; rq_116 deferred\n",
    encoding="utf-8",
)

print("OK tick791 sources/budgets/commitments/leaderboard/foi/rq/loop_state")
print(
    f"counts approx budgets={len(brows)} commitments={len(crows)} lb={len(lrows)} "
    f"src={len(srows)} foi={len(frows)} rq={len(rrows)}"
)
