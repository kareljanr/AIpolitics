# tick 799 — rq_790 Kamer DOC 56 1282/020 Beleidsnota Beliris residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T20:30:00Z"
TICK = 799
RQ = "rq_790"
NEXT_RQ = "rq_791"
SRC_MAIN = "src_kamer_beleid_beliris_1282_020_2026"
SRC_DUAL = "src_dual_beliris_metro3_tick799"
GAP = "gap_beliris_metro3_save25_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282020.pdf"
ENT = "beliris"


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
            "title": "Kamer DOC 56 1282/020 Beleidsnota Beliris residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Beliris",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick799 primary 9p: Metro3 Nord works suspended since 2023-03-17 recurrent "
                "costs; cleanup/palisades SM Progrès 126000 EUR excl VAT awarded 2025-06-06; "
                "recognition digs/surveys 180000 EUR excl VAT CoA-recommended still no STIB/BCR "
                "agreement; budget 2026 imposed savings 25m on Beliris metro credits due to delays; "
                "Schuman canopy (auvent) at least 13m not ordered after BCR refused free budgets "
                "Feb 2025; cycle highways along rail line 28 works started; Jubelpark permit pending; "
                "avenant 15 inventory ongoing business no new projects until inventory; dual Metro3 "
                "CoA stacks; raw 56K1282020.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Beliris save 25m metro vs Metro3 multi-bn residual tick799",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary 25m 2026 save on metro credits dual prior "
                "Metro3 Bordet-Nord 3.1-3.4bn and Beliris financed 464m EOY2024; canopy 13m dual "
                "Schuman works; suspension recurrent costs Unknown"
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
        budget_id="bud_beliris_save_metro_25m_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="-25000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Budget 2026: imposed savings 25m on Beliris metro works credits due to delays; tick799 1282/020"
        ),
    ),
    B(
        budget_id="bud_beliris_nord_cleanup_126k_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="126000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Gare du Nord suspended site cleanup+palisades SM Progrès award 2025-06-06 est 126k EUR "
            "excl VAT; tick799"
        ),
    ),
    B(
        budget_id="bud_beliris_nord_surveys_180k_pending",
        entity_id=ENT,
        year="2026",
        amount_eur="180000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Recognition digs/surveys for Nord tunnel variant est 180k EUR excl VAT CoA-recommended; "
            "no STIB/BCR agreement yet; tick799"
        ),
    ),
    B(
        budget_id="bud_beliris_schuman_canopy_min_13m",
        entity_id=ENT,
        year="2025",
        amount_eur="13000000",
        amount_min_eur="13000000",
        amount_max_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Schuman canopy (auvent) realization cost at least 13m EUR; not ordered after BCR refused "
            "to free budgets Feb 2025; tick799"
        ),
    ),
    B(
        budget_id="bud_dual_beliris_metro3_save_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="-25000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual 25m metro credit save residual vs multi-bn Metro3 stack; not TE-additive; tick799"
        ),
    ),
    B(
        budget_id="bud_dual_metro3_class_tick799",
        entity_id="gg_belgium",
        year="2024",
        amount_eur="3436600000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior Metro3 Bordet-Nord full class 3436.6m residual vs Beliris suspension 020; "
            "not new appropriation; tick799"
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
        commitment_id="cmt_beliris_save_metro_25m_2026",
        title="Beliris budget 2026 metro credits save 25m",
        entity_id=ENT,
        beneficiary="federal budget / delayed metro works",
        legal_basis="Budget 2026; Beleidsnota 1282/020",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="-25000000",
        cash_by_year='{"save_m": 25, "on": "metro_works_credits", "reason": "delays"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Inscribe imposed savings on delayed metro credits",
        cut_option="Already a cut — track residual recurrent suspension costs FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Beliris>metro_save",
        notes="tick799",
    ),
    C(
        commitment_id="cmt_beliris_nord_suspension_since_2023",
        title="Metro3 Gare du Nord works suspension since 2023-03-17",
        entity_id=ENT,
        beneficiary="Metro3 Nord section / STIB-BCR decision pending",
        legal_basis="Metro3 protocols; Beleidsnota 1282/020; CoA report",
        decision_date="2023-03-17",
        start_year="2023",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"suspended_since": "2023-03-17", "cleanup_eur": 126000, "surveys_pending_eur": 180000, "recurrent_costs": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Await BCR/STIB decision on resume or stop; manage site safety",
        cut_option="Recurrent cost path + decision FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Beliris>Metro3_Nord",
        notes="tick799",
    ),
    C(
        commitment_id="cmt_beliris_schuman_canopy_13m_cancelled",
        title="Schuman canopy min 13m not ordered after BCR budget refusal",
        entity_id=ENT,
        beneficiary="Schuman square works",
        legal_basis="Protocols with Region; Beleidsnota 1282/020",
        decision_date="2025-02-01",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="13000000",
        cash_by_year='{"min_m": 13, "status": "not_ordered", "reason": "BCR_refused_budgets_Feb2025"}',
        remaining_eur="0",
        status="cancelled",
        evaluation_url=PDF_URL,
        stated_goal="Canopy for Schuman square redevelopment",
        cut_option="Already deferred — residual cost of incomplete design FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Beliris>Schuman_canopy",
        notes="tick799",
    ),
    C(
        commitment_id="cmt_beliris_nord_cleanup_126k",
        title="Nord site cleanup and palisades 126k excl VAT",
        entity_id=ENT,
        beneficiary="public order around suspended Nord sites",
        legal_basis="Beliris initiative; Beleidsnota 1282/020",
        decision_date="2025-06-06",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="126000",
        cash_by_year='{"award_eur_htva": 126000, "contractor": "SM_Progres", "monthly_clean": true}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Safety and public order during suspension",
        cut_option="Monthly clean cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Beliris>Metro3_Nord>cleanup",
        notes="tick799",
    ),
    C(
        commitment_id="cmt_dual_beliris_metro3_tick799",
        title="Dual Beliris 25m save vs Metro3 multi-bn residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/020 dual CoA Metro3",
        decision_date="2026-08-04",
        start_year="2023",
        end_year="2026",
        total_envelope_eur="-25000000",
        cash_by_year='{"save_m": 25, "metro3_class_bn": 3.436, "beliris_financed_m": 464.4, "canopy_m": 13}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map Beliris residual dual Metro3 stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Beliris_Metro3",
        notes="tick799",
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


new_l = [
    lb(
        "lb_beliris_metro_save_25m_2026",
        "Beliris metro credits save 25m 2026",
        "ops",
        "Federal>Beliris>metro_save",
        "-25000000",
        "-25000000",
        "Strong primary imposed save on delayed metro; dual multi-bn Metro3 residual",
        "strong",
        SRC_MAIN,
        "federal budget",
        "4.0",
        "6.5",
        "2.5",
        "5.10",
        "Track residual suspension costs FOI",
        "tick799",
        goal="Inscribe delay-driven savings on metro credits",
    ),
    lb(
        "lb_beliris_nord_suspension_opaque",
        "Metro3 Nord suspension recurrent costs opaque since 2023",
        "ops",
        "Federal>Beliris>Metro3_Nord",
        "0",
        "0",
        "Strong primary suspended since 2023-03-17; cleanup 126k; surveys 180k pending; recurrent Unknown",
        "strong",
        SRC_MAIN,
        "Metro3 / public order",
        "7.5",
        "8.0",
        "3.5",
        "7.35",
        "Recurrent cost path + decision FOI",
        "tick799",
        goal="Resolve Nord resume or stop",
    ),
    lb(
        "lb_beliris_schuman_canopy_13m",
        "Schuman canopy min 13m not ordered",
        "ops",
        "Federal>Beliris>Schuman_canopy",
        "0",
        "13000000",
        "Strong primary min 13m; BCR refused budgets Feb 2025; not ordered",
        "strong",
        SRC_MAIN,
        "Schuman square",
        "6.0",
        "6.5",
        "2.5",
        "5.80",
        "Design sunk cost FOI",
        "tick799",
        goal="Canopy for Schuman redevelopment",
    ),
    lb(
        "lb_beliris_nord_cleanup_126k",
        "Nord suspended site cleanup 126k excl VAT",
        "ops",
        "Federal>Beliris>Metro3_Nord>cleanup",
        "126000",
        "126000",
        "Strong primary award SM Progrès; monthly clean residual",
        "strong",
        SRC_MAIN,
        "local public order",
        "5.5",
        "3.5",
        "1.5",
        "4.00",
        "Monthly cost FOI",
        "tick799",
        goal="Safety around suspended sites",
    ),
    lb(
        "lb_dual_beliris_metro3_2026",
        "Dual Beliris 25m save vs Metro3 multi-bn residual",
        "ops",
        "Belgium>dual>Beliris_Metro3",
        "0",
        "3436600000",
        "Strong dual not TE-additive; 25m save dual 3.4bn class Metro3 and 464m Beliris financed",
        "strong",
        SRC_DUAL,
        "multi-level mobility",
        "6.5",
        "9.0",
        "4.0",
        "7.40",
        "Cross-entity cash FOI",
        "tick799",
        goal="Dual Beliris Metro3 residual map",
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

foi_row = {
    "gap_id": GAP,
    "hierarchy_path": "Federal>Beliris>Metro3_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual Beliris: cash-by-year recurrent costs of Nord suspension since 2023-03-17; "
        "monthly cleanup costs after 126k award; STIB/BCR decision trail on resume/stop and 180k "
        "surveys; budget 2026 25m metro credit save allocation table; unreleased avenant metro "
        "means reserved for Nord studies/works; Schuman canopy 13m+ design sunk costs and BCR "
        "budget refusal correspondence Feb 2025; cycle highway line 28 multi-year capex; avenant 15 "
        "project inventory with EUR; dual CoA Metro3 3.1-3.4bn reconciliation"
    ),
    "why_it_matters": (
        "Primary Kamer confirms multi-year suspension with only small site costs public while "
        "25m save and multi-bn Metro3 dual remain residual; FOI needed for honest waste ranking"
    ),
    "priority": "9",
    "recipient_body": "Beliris / FOD Mobiliteit / STIB-MIVB FOI",
    "recipient_email": "",
    "recipient_postal": "https://www.beliris.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_beliris_save_metro_25m_2026|cmt_beliris_nord_suspension_since_2023|"
        "cmt_beliris_schuman_canopy_13m_cancelled|cmt_dual_beliris_metro3_tick799"
    ),
    "linked_leaderboard_id": (
        "lb_beliris_metro_save_25m_2026|lb_beliris_nord_suspension_opaque|"
        "lb_beliris_schuman_canopy_13m|lb_dual_beliris_metro3_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick799 Kamer 1282/020 primary; human send only",
}
if not any(r["gap_id"] == GAP for r in frows):
    frows.append(foi_row)
else:
    frows = [foi_row if r["gap_id"] == GAP else r for r in frows]
write_csv(fp, ffields, frows)

rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys())

for r in rq_rows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick799 Beliris 1282/020 save 25m Nord suspend canopy 13m FOI "
            "gap_beliris_metro3_save25_l5"
        )

if not any(r.get("task_id") == NEXT_RQ for r in rq_rows):
    rq_rows.append(
        {
            "task_id": NEXT_RQ,
            "title": "MANDATORY progress@800 — coverage % layers A-E + waste top10",
            "sprint": "hole_fill",
            "priority": "10",
            "status": "open",
            "hierarchy_target": "L0",
            "entity_id": "gg_belgium",
            "instructions": (
                "MANDATORY when ticks_completed reaches 800: refresh "
                "docs/doge/data/progress_every_10_ticks.md (layers A-E vs TE 347.956bn) and "
                "docs/doge/data/doge_waste_top10_current.md (top10 by priority_index); append log; "
                "then spawn next residual rq_792"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick799; progress@800 mandatory next",
        }
    )
# also spawn residual after progress if not exists
if not any(r.get("task_id") == "rq_792" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_792",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "After progress@800: residual dual L5 or unmined primary (Regie 029, Loterij 015, "
                "local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick799 after Beliris020; do after rq_791 progress",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Beliris020 save25m Nord suspend canopy13 FOI; "
    f"next {NEXT_RQ} MANDATORY progress@800; then rq_792 Regie029 residual; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/020 Beleidsnota Beliris**, 9p)
- Found (primary 56K1282020):
  - Budget 2026: imposed **save €25m** on Beliris **metro** credits (delays)
  - Metro3 **Gare du Nord** works **suspended since 17 Mar 2023**; recurrent costs Unknown
  - Site cleanup/palisades SM Progrès **€126k** excl VAT (6 Jun 2025); monthly clean ongoing
  - Surveys **€180k** excl VAT CoA-recommended — **no STIB/BCR agreement** yet
  - Schuman **canopy ≥€13m** — **not ordered** after BCR refused budgets Feb 2025
  - Dual prior Metro3 class **€3.44bn** / Beliris financed **€464m** EOY2024
- Wrote: budgets +6; commitments +5; leaderboard +5; sources +2; FOI **{GAP}** prio9 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ} PROGRESS@800** + rq_792; ticks={TICK}
- FOI: ready only — **do not send**
- Next: **{NEXT_RQ} MANDATORY progress@800**; deferred **rq_116**
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
