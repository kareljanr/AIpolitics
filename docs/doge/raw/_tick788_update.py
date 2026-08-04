# tick 788 — rq_779 Kamer DOC 56 1282/025 Beleidsnota Mobiliteit
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T15:00:00Z"
SRC_MAIN = "src_kamer_beleid_mobiliteit_1282_025_2026"
SRC_DUAL = "src_dual_mobiliteit_tick788"
GAP = "gap_rail_rer_overrun_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282025.pdf"


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
            "title": "Kamer DOC 56 1282/025 Beleidsnota Mobiliteit residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Mobiliteit",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick788: rail public spend save 100m inscribed budget 2026; RER/GEN "
                "completion overrun 308.4m current EUR (PSPI) third notified after Swedish "
                "virtuous billion and Vivaldi 204.6m; IF audit Apr2025; SFPIM loan 61m to rail "
                "freight operator MR 21Jul2025 EU notification; congestion cost 5.3bn 2024 dual "
                "prior; SNCB fares max 14 EUR off-peak train+ 5.5 EUR with 64pct youth/senior/BIM "
                "stack; PSO/performance contracts to 2032; raw 56K1282025_beleid_mobiliteit.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Mobiliteit rail save/RER overrun residual tick788",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: rail 100m save vs RER 308.4m overrun stack; "
                "SFPIM 61m freight loan dual; congestion 5.3bn external cost residual"
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
        budget_id="bud_rail_save_100m_2026",
        entity_id="nmbs",
        year="2026",
        amount_eur="100000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Budget 2026 rail system savings 100m EUR inscribed (efficiency under fixed envelope; NMBS/Infrabel dual); tick788 1282/025",
    ),
    B(
        budget_id="bud_rer_gen_overrun_308_4m",
        entity_id="infrabel",
        year="2025",
        amount_eur="308400000",
        basis="estimated",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="RER/GEN completion overrun 308.4m current EUR notified Mar2025 in PSPI; 3rd gov notice after Swedish virtuous bn and Vivaldi 204.6m; IF audit Apr2025; tick788",
    ),
    B(
        budget_id="bud_rer_vivaldi_overrun_204_6m",
        entity_id="infrabel",
        year="2024",
        amount_eur="204600000",
        basis="reported",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Prior Vivaldi-era RER cost overrun cited 204.6m EUR (note historical dual); tick788",
    ),
    B(
        budget_id="bud_sfpim_rail_freight_loan_61m_2025",
        entity_id="sfpim",
        year="2025",
        amount_eur="61000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="MR 21 Jul 2025 SFPIM loan 61m EUR to rail freight operator (strategic role); EU state-aid notification; tick788",
    ),
    B(
        budget_id="bud_congestion_cost_5_3bn_2024_mob",
        entity_id="fod_mobiliteit",
        year="2024",
        amount_eur="5300000000",
        basis="estimated",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Road congestion economic impact 5.3bn EUR 2024 cited; dual bud_ec_cr_congestion_2024; tick788 cross-ref",
    ),
    B(
        budget_id="bud_sncb_fare_cap_14eur_offpeak",
        entity_id="nmbs",
        year="2026",
        amount_eur="14",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="SNCB off-peak/weekend fare max 14 EUR/trip; train+ formula max 5.5 EUR with stacked 40+40pct youth/senior/BIM; tick788",
    ),
    B(
        budget_id="bud_sncb_train_plus_cap_5_5eur",
        entity_id="nmbs",
        year="2026",
        amount_eur="5.5",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="train+ formula max 5.5 EUR/trip after 64pct stacked reductions; tick788",
    ),
    B(
        budget_id="bud_dual_mobiliteit_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="100000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor rail 100m save vs RER 308.4m overrun residual; not TE-additive; tick788",
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
        commitment_id="cmt_rail_save_100m_2026",
        title="Rail public companies savings 100m 2026",
        entity_id="nmbs",
        beneficiary="rail system",
        legal_basis="Budget 2026; Beleidsnota Mobiliteit 1282/025",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="100000000",
        cash_by_year='{"2026_m": 100, "note": "efficiency under fixed rail envelope"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Confirm rail means while contributing to spending restraint",
        cut_option="Board accountability FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Mobiliteit>rail",
        notes="tick788 NMBS/Infrabel dual",
    ),
    C(
        commitment_id="cmt_rer_gen_overrun_308_4m",
        title="RER/GEN completion overrun 308.4m current EUR",
        entity_id="infrabel",
        beneficiary="RER/GEN project",
        legal_basis="PSPI; Beleidsnota 1282/025; IF audit mission Apr2025",
        decision_date="2025-03-01",
        start_year="2025",
        end_year="2030",
        total_envelope_eur="308400000",
        cash_by_year='{"overrun_m": 308.4, "prior_vivaldi_m": 204.6}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Complete RER with cost control programme in Infrabel performance contract",
        cut_option="Audit FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Infrabel>RER",
        notes="tick788 TUC RAIL/Infrabel analytic accounting transparency",
    ),
    C(
        commitment_id="cmt_sfpim_rail_freight_loan_61m",
        title="SFPIM loan 61m to rail freight operator Jul 2025",
        entity_id="sfpim",
        beneficiary="rail freight operator",
        legal_basis="MR 21 Jul 2025; Beleidsnota 1282/025",
        decision_date="2025-07-21",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="61000000",
        cash_by_year='{"loan_m": 61, "eu_notification": "pending/follow-up"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Support strategic rail freight competitiveness",
        cut_option="State-aid FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>SFPIM>rail_freight",
        notes="tick788",
    ),
    C(
        commitment_id="cmt_nmbs_infrabel_contracts_to_2032",
        title="NMBS PSO + Infrabel performance contracts to 2032",
        entity_id="nmbs",
        beneficiary="rail users",
        legal_basis="Openbaredienst/performantiecontracten; Beleidsnota 1282/025",
        decision_date="2023-01-01",
        start_year="2023",
        end_year="2032",
        total_envelope_eur="0",
        cash_by_year='{"end": 2032, "eur": "multi-year compensations in contracts"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Framework public service and network performance",
        cut_option="Contract FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Mobiliteit>contracts",
        notes="tick788",
    ),
    C(
        commitment_id="cmt_dual_mobiliteit_tick788",
        title="Dual Mobiliteit rail 100m save vs RER 308m residual tick788",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/025",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"save_m": 100, "rer_overrun_m": 308.4, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map rail efficiency vs investment overrun dual",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>mobiliteit",
        notes="tick788",
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
        "lb_rail_save_100m_2026",
        "Rail public spend save 100m 2026",
        "ops",
        "Federal>Mobiliteit>rail",
        "100000000",
        "100000000",
        "Strong budget inscription; efficiency under fixed rail envelope",
        "strong",
        SRC_MAIN,
        "taxpayers",
        "3.5",
        "7.0",
        "3.0",
        "5.05",
        "Board FOI",
        "tick788",
    ),
    lb(
        "lb_rer_gen_overrun_308_4m",
        "RER/GEN completion overrun 308.4m",
        "ops",
        "Federal>Infrabel>RER",
        "308400000",
        "308400000",
        "Strong primary notified overrun; 3rd government; IF audit path",
        "strong",
        SRC_MAIN,
        "rail users",
        "7.5",
        "7.5",
        "4.0",
        "6.85",
        "Audit FOI",
        "tick788 high absurdity cost stack",
    ),
    lb(
        "lb_rer_vivaldi_overrun_204_6m",
        "RER prior Vivaldi overrun 204.6m cited",
        "ops",
        "Federal>Infrabel>RER",
        "204600000",
        "204600000",
        "Medium historical cite in 1282/025",
        "medium",
        SRC_MAIN,
        "rail users",
        "6.5",
        "7.0",
        "3.5",
        "6.15",
        "History FOI",
        "tick788",
    ),
    lb(
        "lb_sfpim_rail_freight_loan_61m",
        "SFPIM rail freight loan 61m 2025",
        "transfer",
        "Federal>SFPIM>rail_freight",
        "61000000",
        "61000000",
        "Strong loan not grant; EU notification residual",
        "strong",
        SRC_MAIN,
        "rail freight",
        "4.0",
        "6.0",
        "2.5",
        "4.70",
        "State-aid FOI",
        "tick788",
    ),
    lb(
        "lb_sncb_fare_cap_14_trainplus_5_5",
        "SNCB fare caps 14 EUR / train+ 5.5 EUR",
        "ops",
        "Federal>NMBS>tariffs",
        "0",
        "0",
        "Strong policy unit fares; fiscal impact Unknown",
        "strong",
        SRC_MAIN,
        "passengers",
        "3.0",
        "4.5",
        "2.0",
        "3.55",
        "Tariff FOI",
        "tick788",
    ),
    lb(
        "lb_dual_mobiliteit_2026",
        "Dual Mobiliteit rail save vs RER overrun",
        "ops",
        "Belgium>dual>mobiliteit",
        "100000000",
        "0",
        "Strong dual not TE-additive: 100m save vs 308m overrun",
        "strong",
        SRC_DUAL,
        "public",
        "6.0",
        "7.5",
        "3.5",
        "6.25",
        "L5 FOI",
        "tick788",
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
                "hierarchy_path": "Federal>Mobiliteit>RER_rail_L5",
                "entity_id": "infrabel",
                "what_is_missing": (
                    "IF audit report on RER/GEN cost overruns (mission 30 Apr 2025); full cost "
                    "evolution TUC RAIL/Infrabel analytic accounts; 308.4m overrun line items and "
                    "remaining contingency; rail 100m 2026 savings allocation NMBS vs Infrabel; "
                    "SFPIM 61m freight loan terms beneficiary and EU state-aid status; multi-year "
                    "PSO/performance contract cash tables to 2032"
                ),
                "why_it_matters": (
                    "RER third-generation overrun public at aggregate; residual L5 dual to rail "
                    "save and prior 204.6m opaque"
                ),
                "priority": "9",
                "recipient_body": "FOD Mobiliteit / Infrabel / Inspectie van Financiën FOI",
                "recipient_email": "",
                "recipient_postal": "https://mobilit.belgium.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_rer_gen_overrun_308_4m|cmt_rail_save_100m_2026|"
                    "cmt_sfpim_rail_freight_loan_61m|cmt_dual_mobiliteit_tick788"
                ),
                "linked_leaderboard_id": (
                    "lb_rer_gen_overrun_308_4m|lb_rail_save_100m_2026|"
                    "lb_sfpim_rail_freight_loan_61m|lb_dual_mobiliteit_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick788 Kamer 1282/025 primary; human send only",
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
    if r["task_id"] == "rq_779":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick788: Mobiliteit 1282/025 rail save 100m RER overrun 308.4m SFPIM 61m; "
            "FOI ready; spawn rq_780 PROGRESS@790"
        )
if not any(r["task_id"] == "rq_780" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_780",
                "title": "Mandatory progress@790 coverage % + waste top10",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L0-L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "When ticks_completed hits 790: refresh progress_every_10_ticks.md layers "
                    "A-E vs EUR 347.956bn TE and doge_waste_top10_current.md by priority_index; "
                    "append log; no invent euros; then spawn next hole-fill."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick788 after rq_779; progress@790 after +2 more ticks or if next is 790",
            }.items()
            if k in rfields
        }
    )
# Also spawn residual hole-fill after progress
if not any(r["task_id"] == "rq_781" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_781",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "After progress@790 (rq_780): residual dual L5 or unmined primary "
                    "(Justitie 017, Asiel 038, local/CoA); Mobiliteit 1282/025 filled tick788"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick788; do after rq_780",
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
        "last_unit_id": "rq_779",
        "ticks_completed": "788",
        "paused": "no",
        "notes": "user paused=no; next rq_780 PROGRESS@790 after +2; or hole-fill if not 790 yet; progress@790 in 2; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
