# tick 786 — rq_777 Kamer DOC 56 1282/004 Beleidsnota Economie
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T14:00:00Z"
SRC_MAIN = "src_kamer_beleid_economie_1282_004_2026"
SRC_DUAL = "src_dual_economie_tick786"
GAP = "gap_economie_make_procurement_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282004.pdf"


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
            "title": "Kamer DOC 56 1282/004 Beleidsnota Economie residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Economie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick786: FPB path 2026 growth 1.1pct +38k jobs employment 72.6pct "
                "inflation 1.4pct; MAKE2025-2030 interfederal industrial plan launched Jun2025; "
                "public procurement reform threshold simplified proc 50000eur indexable direct "
                "award 15000eur; life insurance max rate 3.75pct 2026 plan abolish ceiling; "
                "CSRD first wave ~40 BE firms; Omnibus CSRD scope 5100-7800 EU firms; CS3D "
                "5000 FTE + 1.5bn turnover; gambling commission transfer Justice to Economy; "
                "raw 56K1282004_beleid_economie.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Economie procurement/MAKE vs defense invest residual tick786",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: procurement threshold reform vs public spend; "
                "MAKE industrial plan vs defense economic return residual; CSRD burden residual"
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
        budget_id="bud_fpb_growth_1_1pct_2026_eco",
        entity_id="fod_economie",
        year="2026",
        amount_eur="",
        basis="projected",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="FPB Economic Budget Sep2025 cited: growth 1.1pct 2026; +38000 jobs; employment 20-64 72.6pct; inflation ~1.4pct; tick786",
    ),
    B(
        budget_id="bud_procurement_simplified_threshold_50k_2026",
        entity_id="fod_economie",
        year="2026",
        amount_eur="50000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Public procurement reform: simplified low-value procedure threshold raised to 50000 EUR (indexable); tick786",
    ),
    B(
        budget_id="bud_procurement_direct_award_15k_2026",
        entity_id="fod_economie",
        year="2026",
        amount_eur="15000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Public procurement: direct award allowed up to 15000 EUR; tick786",
    ),
    B(
        budget_id="bud_life_ins_max_rate_3_75pct_2026",
        entity_id="fod_economie",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Ministerial decision: max rate long-term life insurance (>8y) set at legal ceiling 3.75pct 2026; plan to abolish ceiling system; tick786",
    ),
    B(
        budget_id="bud_csrd_first_wave_40_firms_be",
        entity_id="fod_economie",
        year="2025",
        amount_eur="",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="CSRD first wave ~40 Belgian large listed/EIP >500 FTE published 2025 on FY2024; tick786",
    ),
    B(
        budget_id="bud_csrd_omnibus_scope_5_1_7_8k_eu",
        entity_id="fod_economie",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Omnibus Dec2025: CSRD EU scope reduced to about 5100-7800 firms; stop-the-clock +2y waves 2-3; tick786",
    ),
    B(
        budget_id="bud_cs3d_threshold_1_5bn_turnover",
        entity_id="fod_economie",
        year="2027",
        amount_eur="1500000000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="CS3D simplified: applies firms with >=5000 staff and turnover from 1.5bn EUR; transposition by Jul2027; tick786",
    ),
    B(
        budget_id="bud_make_plan_2025_2030",
        entity_id="fod_economie",
        year="2026",
        amount_eur="",
        basis="programme",
        source_id=SRC_MAIN,
        confidence="weak",
        notes="MAKE2025-2030 interfederal industrial plan launched Jun2025; operational recs early 2026; euro envelope Unknown; FOI; tick786",
    ),
    B(
        budget_id="bud_dual_economie_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="50000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor procurement threshold reform class; not TE-additive; tick786",
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
        commitment_id="cmt_make_2025_2030",
        title="MAKE2025-2030 interfederal industrial plan",
        entity_id="fod_economie",
        beneficiary="industry",
        legal_basis="Interfederal plan Jun2025; Beleidsnota Economie 1282/004",
        decision_date="2025-06-01",
        start_year="2025",
        end_year="2030",
        total_envelope_eur="0",
        cash_by_year='{"eur": "Unknown public", "recs": "early 2026"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Industry at core of growth strategy competitiveness",
        cut_option="Envelope FOI",
        source_id=SRC_MAIN,
        confidence="weak",
        hierarchy_path="Federal>Economie>MAKE",
        notes="tick786 euro FOI",
    ),
    C(
        commitment_id="cmt_procurement_thresholds_2026",
        title="Public procurement thresholds 50k simplified / 15k direct",
        entity_id="fod_economie",
        beneficiary="SMEs / contracting authorities",
        legal_basis="Government agreement; Beleidsnota 1282/004",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"simplified_eur": 50000, "direct_eur": 15000}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Simplify public contracts for SMEs; short-chain specs",
        cut_option="Impact FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Economie>procurement",
        notes="tick786",
    ),
    C(
        commitment_id="cmt_life_ins_max_rate_abolish",
        title="Abolish life insurance max rate ceiling (temp 3.75pct 2026)",
        entity_id="fod_economie",
        beneficiary="life insurers/savers",
        legal_basis="Beleidsnota 1282/004",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"2026_max_pct": 3.75, "plan": "abolish ceiling"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Restore competition; NBB tools for unrealistic rates",
        cut_option="Market FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Economie>insurance",
        notes="tick786",
    ),
    C(
        commitment_id="cmt_csrd_stop_clock_omnibus",
        title="CSRD stop-the-clock + Omnibus scope cut 2025-27",
        entity_id="fod_economie",
        beneficiary="enterprises",
        legal_basis="EU Stop the clock; Omnibus Dec2025; Beleidsnota 1282/004",
        decision_date="2025-12-04",
        start_year="2025",
        end_year="2027",
        total_envelope_eur="0",
        cash_by_year='{"be_wave1_firms": 40, "eu_scope": "5100-7800", "transposition": "2027-01"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reduce admin burden sustainability reporting",
        cut_option="Burden FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Economie>CSRD",
        notes="tick786",
    ),
    C(
        commitment_id="cmt_kansspel_transfer_economy",
        title="Gambling Commission competence transfer to Economy",
        entity_id="kansspelcommissie",
        beneficiary="gambling sector",
        legal_basis="Beleidsnota Economie 1282/004",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"from": "Justice", "to": "Economy"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Transfer Kansspelcommissie from Justice to Economy",
        cut_option="Budget FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>Economie>kansspelen",
        notes="tick786 budget impact Unknown",
    ),
    C(
        commitment_id="cmt_dual_economie_tick786",
        title="Dual Economie procurement/MAKE residual tick786",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/004",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map economy instruments dual to public spend/defense",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>economie",
        notes="tick786",
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
        "lb_make_plan_unknown_2026",
        "MAKE2025-2030 industrial plan euro Unknown",
        "ops",
        "Federal>Economie>MAKE",
        "0",
        "0",
        "Weak — plan public without euro envelope; FOI-adjacent",
        "weak",
        SRC_MAIN,
        "industry",
        "4.5",
        "6.0",
        "3.0",
        "4.95",
        "Envelope FOI",
        "tick786",
    ),
    lb(
        "lb_procurement_threshold_50k_2026",
        "Procurement simplified threshold 50k EUR",
        "ops",
        "Federal>Economie>procurement",
        "50000",
        "0",
        "Strong unit threshold reform; volume impact Unknown",
        "strong",
        SRC_MAIN,
        "SMEs",
        "3.0",
        "5.0",
        "2.5",
        "3.95",
        "Impact FOI",
        "tick786",
    ),
    lb(
        "lb_procurement_direct_15k_2026",
        "Procurement direct award up to 15k EUR",
        "ops",
        "Federal>Economie>procurement",
        "15000",
        "0",
        "Strong unit; transparency residual for low-value contracts",
        "strong",
        SRC_MAIN,
        "contracting authorities",
        "4.0",
        "4.5",
        "2.0",
        "3.95",
        "Monitor FOI",
        "tick786",
    ),
    lb(
        "lb_life_ins_max_3_75_2026",
        "Life insurance max rate ceiling 3.75pct 2026",
        "taxex",
        "Federal>Economie>insurance",
        "0",
        "0",
        "Strong temporary ceiling; abolish planned; market distortion note",
        "strong",
        SRC_MAIN,
        "savers/insurers",
        "4.0",
        "5.0",
        "2.5",
        "4.25",
        "Market FOI",
        "tick786",
    ),
    lb(
        "lb_csrd_omnibus_burden_2026",
        "CSRD Omnibus scope cut + stop-the-clock",
        "ops",
        "Federal>Economie>CSRD",
        "0",
        "0",
        "Strong regulatory relief; residual ~40 BE wave1 still obligated",
        "strong",
        SRC_MAIN,
        "enterprises",
        "3.5",
        "5.5",
        "3.0",
        "4.35",
        "Burden FOI",
        "tick786",
    ),
    lb(
        "lb_cs3d_1_5bn_threshold",
        "CS3D threshold 5000 FTE / 1.5bn turnover",
        "ops",
        "Federal>Economie>CS3D",
        "1500000000",
        "0",
        "Strong simplified threshold unit; transposition Jul2027",
        "strong",
        SRC_MAIN,
        "large firms",
        "3.0",
        "5.0",
        "3.0",
        "4.00",
        "Scope FOI",
        "tick786",
    ),
    lb(
        "lb_kansspel_transfer_2026",
        "Gambling Commission transfer to Economy",
        "ops",
        "Federal>Economie>kansspelen",
        "0",
        "0",
        "Medium institutional transfer; budget Unknown",
        "medium",
        SRC_MAIN,
        "gambling sector",
        "3.5",
        "4.5",
        "2.5",
        "3.80",
        "Budget FOI",
        "tick786",
    ),
    lb(
        "lb_dual_economie_2026",
        "Dual Economie procurement/MAKE residual",
        "ops",
        "Belgium>dual>economie",
        "0",
        "0",
        "Strong dual not TE-additive map economy instruments",
        "strong",
        SRC_DUAL,
        "public",
        "4.0",
        "5.5",
        "3.0",
        "4.55",
        "L5 FOI",
        "tick786",
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
                "hierarchy_path": "Federal>Economie>MAKE_procurement_L5",
                "entity_id": "fod_economie",
                "what_is_missing": (
                    "MAKE2025-2030 euro envelope and federal/regional co-financing; FOD "
                    "Economie total budget L5 2026; public procurement reform expected volume "
                    "shift under 15k/50k thresholds; gambling commission transfer budget and "
                    "staff FTE; defense industrial return targets if quantified; e-commerce "
                    "taskforce extra inspection budget"
                ),
                "why_it_matters": (
                    "Economy note policy-heavy; residual programme and admin euros dual to "
                    "public spend opaque"
                ),
                "priority": "7",
                "recipient_body": "FOD Economie FOI",
                "recipient_email": "",
                "recipient_postal": "https://economie.fgov.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_make_2025_2030|cmt_procurement_thresholds_2026|"
                    "cmt_kansspel_transfer_economy|cmt_dual_economie_tick786"
                ),
                "linked_leaderboard_id": (
                    "lb_make_plan_unknown_2026|lb_procurement_threshold_50k_2026|"
                    "lb_kansspel_transfer_2026|lb_dual_economie_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick786 Kamer 1282/004 primary; human send only",
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
    if r["task_id"] == "rq_777":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick786: Economie 1282/004 procurement 50k/15k MAKE plan life-ins 3.75 "
            "CSRD/CS3D; FOI ready; spawn rq_778"
        )
if not any(r["task_id"] == "rq_778" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_778",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (Defensie 1282/022, Asiel 038, "
                    "Mobiliteit 025, local/CoA); Economie 1282/004 filled tick786"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick786 after rq_777",
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
        "last_unit_id": "rq_777",
        "ticks_completed": "786",
        "paused": "no",
        "notes": "user paused=no; next rq_778; progress@790 in 4; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
