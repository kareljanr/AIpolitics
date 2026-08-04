# tick 796 — rq_787 Kamer DOC 56 1282/041 Beleidsnota Energie residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T19:00:00Z"
TICK = 796
RQ = "rq_787"
NEXT_RQ = "rq_788"
SRC_MAIN = "src_kamer_beleid_energie_1282_041_2026"
SRC_DUAL = "src_dual_energie_etf_tick796"
GAP = "gap_energie_etf10_phoenix_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282041.pdf"
ENT = "fod_economy"
ETF = "etf_energy_transition_fund"


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
            "title": "Kamer DOC 56 1282/041 Beleidsnota Energie residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Energie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick796 primary 22p: ETF 9th call MR 2025-07-04 award 14 projects total "
                "16_970_986.81 EUR (call Nov 2024); 10th ETF call launched 6 Nov residual fund amount "
                "to be made available 2026 (projects select May 2026 start Sep-Nov 2026 end by 2029); "
                "first 8 ETF calls 2017-2023: 118 projects supported of which 70 still ongoing; CRM "
                "re-evaluate post-2035; Phoenix Doel4/Tihange3 extended ops in BE-NUC with financial "
                "support mechanism (amount Unknown); BE-WATT structure; FANC benchmark; MYRRHA "
                "continuation decisions pending; Hedera nuclear waste operationalisation; NIRAS "
                "state nuclear liabilities financing continues; market surveillance fund exploration; "
                "raw 56K1282041.pdf + _tmp_tick793_energie_full.txt"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Energie ETF call9 16.97m vs BA path 24.75m residual tick796",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary call9 16.97m dual prior ETF BA path ~24.75m/yr "
                "and eng 24.56m 2026; remaining fund 10th call Unknown; dual CRM auctions 125.4m "
                "and nuclear Phoenix support opaque"
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
        budget_id="bud_etf_call9_award_16_97m",
        entity_id=ETF,
        year="2025",
        amount_eur="16970986.81",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "ETF 9th call (Nov 2024): MR 4 Jul 2025 awards 14 projects total 16_970_986.81 EUR; "
            "tick796 1282/041"
        ),
    ),
    B(
        budget_id="bud_etf_call9_projects_count_14",
        entity_id=ETF,
        year="2025",
        amount_eur="14",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="ETF call9 projects awarded count 14; amount=count; tick796",
    ),
    B(
        budget_id="bud_etf_calls1_8_projects_118",
        entity_id=ETF,
        year="2023",
        amount_eur="118",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="ETF first 8 calls 2017-2023 supported 118 projects; amount=count; tick796",
    ),
    B(
        budget_id="bud_etf_calls1_8_ongoing_70",
        entity_id=ETF,
        year="2026",
        amount_eur="70",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="ETF first 8 calls: 70 projects still ongoing 2026 follow-up; amount=count; tick796",
    ),
    B(
        budget_id="bud_etf_call10_residual_fund_2026_unknown",
        entity_id=ETF,
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "ETF 10th call: remaining fund amount made available 2026 (MR 4 Jul 2025); select May "
            "2026 start Sep-Nov 2026 end by 2029; EUR residual FOI; tick796"
        ),
    ),
    B(
        budget_id="bud_dual_etf_call9_vs_ba_path_2026",
        entity_id=ETF,
        year="2026",
        amount_eur="16970986.81",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual call9 award 16.97m residual vs prior ETF BA path ~24.75m/eng 24.56m 2026; "
            "not TE-additive double-count of stock; tick796"
        ),
    ),
    B(
        budget_id="bud_phoenix_support_mechanism_unknown",
        entity_id=ENT,
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Phoenix Doel4/Tihange3 extended ops in BE-NUC with financial support mechanism "
            "deployment ongoing; amount Unknown FOI; tick796"
        ),
    ),
    B(
        budget_id="bud_crm_reeval_post_2035_policy",
        entity_id=ENT,
        year="2035",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "CRM to be re-evaluated incl utility of prolongation after 2035; techno-economic study; "
            "dual prior CRM auction 125.4m Oct 2025; tick796"
        ),
    ),
    B(
        budget_id="bud_dual_energie_crm_125_4m_class",
        entity_id="elia",
        year="2025",
        amount_eur="125400000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior CRM multi-auction package 125.4m Oct 2025 residual vs 041 re-eval path; "
            "not new from 041; tick796"
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
        commitment_id="cmt_etf_call9_16_97m",
        title="ETF 9th call awards 14 projects 16.97m",
        entity_id=ETF,
        beneficiary="14 selected energy transition projects",
        legal_basis="Energietransitiefonds; MR 2025-07-04; Beleidsnota 1282/041",
        decision_date="2025-07-04",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="16970986.81",
        cash_by_year='{"award_eur": 16970986.81, "projects": 14, "call": 9, "call_date": "2024-11"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Support energy transition innovation projects",
        cut_option="Named project list + unit awards FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Energy>ETF>call9",
        notes="tick796",
    ),
    C(
        commitment_id="cmt_etf_call10_residual_2026",
        title="ETF 10th call residual fund amount available 2026",
        entity_id=ETF,
        beneficiary="projects selected May 2026",
        legal_basis="MR 2025-07-04; Beleidsnota 1282/041",
        decision_date="2025-07-04",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"select": "2026-05", "start": "2026-09/11", "end": "2029", "amount": "remaining_fund_Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Deploy remaining ETF resources via 10th call",
        cut_option="Publish remaining fund EUR FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Energy>ETF>call10",
        notes="tick796",
    ),
    C(
        commitment_id="cmt_phoenix_doel4_tihange3_support",
        title="Phoenix Doel4/Tihange3 BE-NUC financial support mechanism",
        entity_id=ENT,
        beneficiary="BE-NUC joint venture / nuclear capacity",
        legal_basis="Phoenix agreements; nuclear exit law amendments; Beleidsnota 1282/041",
        decision_date="2026-01-23",
        start_year="2025",
        end_year="2035",
        total_envelope_eur="",
        cash_by_year='{"jv": "BE-NUC", "units": ["Doel4", "Tihange3"], "support_mechanism": "deploying", "eur": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Extended nuclear ops with financial support and risk strategy",
        cut_option="Support mechanism cash path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Energy>Nuclear>Phoenix",
        notes="tick796",
    ),
    C(
        commitment_id="cmt_crm_reeval_post_2035",
        title="CRM capacity mechanism re-evaluation post-2035",
        entity_id=ENT,
        beneficiary="electricity adequacy / capacity providers",
        legal_basis="CRM framework; Beleidsnota 1282/041",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2035",
        total_envelope_eur="",
        cash_by_year='{"reeval": true, "post_2035_utility": "study", "techno_economic_study": true}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Security of supply aligned with climate and flexibility",
        cut_option="Auction cost path dual FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Energy>CRM",
        notes="tick796 dual prior 125.4m auction package",
    ),
    C(
        commitment_id="cmt_dual_energie_etf_tick796",
        title="Dual Energie ETF call9 16.97m vs BA path residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/041 dual prior ETF BA / CRM",
        decision_date="2026-08-04",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="16970986.81",
        cash_by_year='{"call9_m": 16.97, "etf_ba_path_m": 24.75, "crm_auction_m": 125.4, "phoenix_eur": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map Energie residual dual ETF/CRM stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Energy",
        notes="tick796",
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
        "lb_etf_call9_16_97m",
        "ETF 9th call awards 16.97m (14 projects)",
        "transfer",
        "Federal>Energy>ETF>call9",
        "16970986.81",
        "16970986.81",
        "Strong primary MR award total; named project list residual FOI",
        "strong",
        SRC_MAIN,
        "14 energy transition projects",
        "4.5",
        "6.0",
        "2.0",
        "4.90",
        "Publish project matrix FOI",
        "tick796",
        goal="ETF innovation project awards",
    ),
    lb(
        "lb_etf_call10_residual_opaque",
        "ETF 10th call residual fund amount opaque",
        "transfer",
        "Federal>Energy>ETF>call10",
        "0",
        "0",
        "Strong primary: remaining fund available 2026 but EUR Unknown; dual BA path ~24.6m",
        "strong",
        SRC_MAIN,
        "future ETF projects",
        "6.0",
        "6.5",
        "2.0",
        "5.70",
        "Publish remaining fund EUR FOI",
        "tick796",
        goal="Deploy residual ETF resources",
    ),
    lb(
        "lb_phoenix_support_opaque",
        "Phoenix Doel4/Tihange3 support mechanism opaque",
        "ops",
        "Federal>Energy>Nuclear>Phoenix",
        "0",
        "0",
        "Strong primary commitment BE-NUC support mechanism; multi-year EUR residual FOI",
        "strong",
        SRC_MAIN,
        "nuclear JV BE-NUC",
        "7.0",
        "8.5",
        "4.0",
        "7.35",
        "Publish support mechanism cash FOI",
        "tick796",
        goal="Extended nuclear capacity with support",
    ),
    lb(
        "lb_dual_energie_etf_2026",
        "Dual ETF call9 16.97m vs BA path residual",
        "ops",
        "Belgium>dual>Energy_ETF",
        "16970986.81",
        "16970986.81",
        "Strong dual not TE-additive; call9 dual BA ~24.75m path and CRM 125.4m class",
        "strong",
        SRC_DUAL,
        "energy transition stack",
        "5.0",
        "7.0",
        "3.0",
        "5.80",
        "Cross-instrument L5 FOI",
        "tick796",
        goal="Dual energy residual map",
    ),
    lb(
        "lb_crm_reeval_post_2035",
        "CRM re-evaluation post-2035 residual",
        "ops",
        "Federal>Energy>CRM",
        "0",
        "125400000",
        "Strong primary policy; dual prior auction package 125.4m as scale class not new award",
        "strong",
        SRC_MAIN,
        "capacity providers",
        "5.5",
        "7.5",
        "3.5",
        "6.25",
        "Auction multi-year cost FOI",
        "tick796",
        goal="CRM adequacy post-2035 design",
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
    "hierarchy_path": "Federal>Energy>ETF_Phoenix_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual Energie: ETF call9 named 14-project award matrix reconciling 16_970_986.81; "
        "ETF 10th call remaining fund exact EUR and selection criteria; cash-by-year ETF stock "
        "(70 ongoing of 118 historical projects); Phoenix/BE-NUC financial support mechanism "
        "multi-year EUR path for Doel4/Tihange3; BE-WATT structure budget; MYRRHA continuation "
        "decision envelope; Hedera operationalisation budget; NIRAS BP1/BP2 state nuclear "
        "liabilities annual cash; market surveillance fund design if pursued; CRM post-2035 "
        "techno-economic study and auction cost path dual prior 125.4m"
    ),
    "why_it_matters": (
        "Primary Kamer publishes one precise ETF award but residual fund and nuclear support "
        "mechanism are material opaque; dual BA path and CRM auctions need residual L5"
    ),
    "priority": "8",
    "recipient_body": "FOD Economie (Energie) / Energietransitiefonds / FANC FOI",
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
        "cmt_etf_call9_16_97m|cmt_etf_call10_residual_2026|cmt_phoenix_doel4_tihange3_support|"
        "cmt_crm_reeval_post_2035|cmt_dual_energie_etf_tick796"
    ),
    "linked_leaderboard_id": (
        "lb_etf_call9_16_97m|lb_etf_call10_residual_opaque|lb_phoenix_support_opaque|"
        "lb_dual_energie_etf_2026|lb_crm_reeval_post_2035"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick796 Kamer 1282/041 primary; human send only",
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
            "tick796 Energie 1282/041 ETF call9 16.97m call10 residual Phoenix FOI "
            "gap_energie_etf10_phoenix_l5"
        )

if not any(r.get("task_id") == NEXT_RQ for r in rq_rows):
    rq_rows.append(
        {
            "task_id": NEXT_RQ,
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": (
                "Next residual: dual L5 or unmined primary (KMO 024, Digi 030 thin, local/CoA, "
                "other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick796 after Energie041",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Energie041 ETF call9 16.97m call10 residual Phoenix FOI; "
    f"next {NEXT_RQ} KMO024/local residual; progress@800 in 4; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/041 Beleidsnota Energie**, 22p)
- Found (primary 56K1282041):
  - ETF **9th call** (Nov 2024): MR 4 Jul 2025 awards **14 projects = €16,970,986.81**
  - ETF **10th call**: remaining fund available **2026** (select May 2026; start Sep–Nov 2026; end 2029) — EUR **Unknown**
  - First 8 ETF calls: **118** projects supported; **70** still ongoing
  - **Phoenix** Doel 4 / Tihange 3 in **BE-NUC** + financial support mechanism (EUR Unknown)
  - CRM re-evaluation incl. utility after **2035**; dual prior CRM auction package **€125.4m**
  - Dual prior ETF BA path **~€24.75m**/yr (eng **€24.56m** 2026)
- Wrote: budgets +9; commitments +5; leaderboard +5; sources +2; FOI **{GAP}** prio8 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual KMO024/local; deferred **rq_116**; progress@800 in 4
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
