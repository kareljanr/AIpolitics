# tick 798 — rq_789 Kamer DOC 56 1282/013 Beleidsnota Financiën residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T20:00:00Z"
TICK = 798
RQ = "rq_789"
NEXT_RQ = "rq_790"
SRC_MAIN = "src_kamer_beleid_financien_1282_013_2026"
SRC_DUAL = "src_dual_fin_taxex_tick798"
GAP = "gap_fin_vat_demo_sfpim_defence_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282013.pdf"
ENT = "fod_finance"


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
            "title": "Kamer DOC 56 1282/013 Beleidsnota Financiën residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister van Financiën",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick798 primary 12p: programmawet BS 2025-07-29 VAT demolition/rebuild "
                "reduction cruise-speed tax cut 250m EUR avg saving 48k/taxpayer; heat-pump VAT "
                "reduction reintroduced 2026-01-01 cost 10.1m; equity tax credit doubled 3750->7500; "
                "capital gains tax annual exemption 10k/person (up to 15k); SRFF +100 staff fraud; "
                "admin sites path to 21 buildings; Cost Reduction Law II planned; SFPIM Defence "
                "entity to be created/operationalised (capital Unknown); EU customs reform abolishes "
                "150 EUR franchise + handling fee; dual prior heatpump taxex -10.1m; raw 56K1282013.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Fin taxex demo 250m + heatpump 10.1m residual tick798",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary demo/rebuild VAT cruise 250m dual heatpump "
                "10.1m and FPS taxex inventory; SFPIM Defence capital dual prior defence invest stacks"
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
        budget_id="bud_vat_demo_rebuild_cruise_250m",
        entity_id=ENT,
        year="2029",
        amount_eur="250000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "VAT reduction demolition/rebuild: cruise-speed tax cut 250m EUR (programmawet BS "
            "2025-07-29); avg taxpayer saving 48k; tick798 1282/013"
        ),
    ),
    B(
        budget_id="bud_vat_demo_rebuild_avg_save_48k",
        entity_id=ENT,
        year="2026",
        amount_eur="48000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Average taxpayer saving from demo/rebuild VAT cut 48k EUR; unit figure; tick798",
    ),
    B(
        budget_id="bud_vat_heatpump_10_1m_2026_fin_note",
        entity_id=ENT,
        year="2026",
        amount_eur="10100000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Heat-pump supply+install VAT reduction reintroduced 2026-01-01; budget cost 10.1m; "
            "dual prior CoA/table -10.1m; tick798"
        ),
    ),
    B(
        budget_id="bud_equity_tax_credit_doubled_7500",
        entity_id=ENT,
        year="2026",
        amount_eur="7500",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Tax credit for own funds / equity doubled 3750->7500 EUR via wet diverse bepalingen; "
            "unit ceiling not aggregate; tick798"
        ),
    ),
    B(
        budget_id="bud_cgt_exemption_10k_person",
        entity_id=ENT,
        year="2026",
        amount_eur="10000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Capital gains tax annual exemption 10k EUR/person (can reach 15k); unit ceiling; "
            "aggregate taxex Unknown FOI; tick798"
        ),
    ),
    B(
        budget_id="bud_cgt_exemption_max_15k_person",
        entity_id=ENT,
        year="2026",
        amount_eur="15000",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="CGT exemption can reach 15k EUR/person; unit max; tick798",
    ),
    B(
        budget_id="bud_srff_extra_staff_100",
        entity_id=ENT,
        year="2026",
        amount_eur="100",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "SRFF (service recherches fiscales et financières) +100 extra staff for fraud fight; "
            "payroll cost Unknown FOI; amount=count; tick798"
        ),
    ),
    B(
        budget_id="bud_fod_finance_admin_sites_target_21",
        entity_id=ENT,
        year="2029",
        amount_eur="21",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="FOD Finance admin buildings path target 21 sites; amount=count; tick798",
    ),
    B(
        budget_id="bud_sfpim_defence_capital_unknown",
        entity_id="sfpim",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "SFPIM Defence entity creation/ops forthcoming; risk capital for defence/aerospace/"
            "dual-use startups; capital envelope Unknown FOI; tick798"
        ),
    ),
    B(
        budget_id="bud_dual_fin_taxex_demo_heatpump_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="260100000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="medium",
        notes=(
            "Illustrative dual stack cruise demo 250m + heatpump 10.1m class; not same-year additive "
            "without path FOI; tick798"
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
        commitment_id="cmt_vat_demo_rebuild_250m",
        title="VAT demolition/rebuild reduction cruise-speed 250m tax cut",
        entity_id=ENT,
        beneficiary="taxpayers renovating/rebuilding",
        legal_basis="Programmawet BS 2025-07-29; Beleidsnota 1282/013",
        decision_date="2025-07-29",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="250000000",
        cash_by_year='{"cruise_m": 250, "avg_save_eur": 48000, "note": "tax_revenue_foregone"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Support demolition and reconstruction via reduced VAT",
        cut_option="Path to cruise FOI + beneficiary volume",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Taxex>VAT_demo_rebuild",
        notes="tick798",
    ),
    C(
        commitment_id="cmt_vat_heatpump_10_1m_2026",
        title="Heat-pump VAT reduction reintroduced 10.1m 2026",
        entity_id=ENT,
        beneficiary="households installing heat pumps",
        legal_basis="Regeerakkoord; Beleidsnota 1282/013",
        decision_date="2026-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="10100000",
        cash_by_year='{"2026_m": 10.1, "from": "2026-01-01"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reintroduce reduced VAT on heat pump supply and install",
        cut_option="Dual CoA path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Taxex>VAT_heatpump",
        notes="tick798 dual prior -10.1m",
    ),
    C(
        commitment_id="cmt_equity_tax_credit_7500",
        title="Equity tax credit doubled to 7500 EUR",
        entity_id=ENT,
        beneficiary="self-employed / SMEs with equity credit",
        legal_basis="Wet diverse bepalingen; Beleidsnota 1282/013",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"from_eur": 3750, "to_eur": 7500, "aggregate": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Support self-employed equity / own funds",
        cut_option="Aggregate taxex FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Taxex>equity_credit",
        notes="tick798",
    ),
    C(
        commitment_id="cmt_cgt_exemption_10k_15k",
        title="Capital gains tax annual exemption 10k-15k per person",
        entity_id=ENT,
        beneficiary="small/medium long-term savers",
        legal_basis="Summer agreement / CGT reform; Beleidsnota 1282/013",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"base_eur": 10000, "max_eur": 15000, "aggregate_taxex": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Protect small long-term investors under CGT",
        cut_option="Aggregate FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Taxex>CGT_exemption",
        notes="tick798",
    ),
    C(
        commitment_id="cmt_sfpim_defence_entity",
        title="SFPIM Defence entity creation and risk capital",
        entity_id="sfpim",
        beneficiary="BE defence/aerospace/dual-use firms and startups",
        legal_basis="Beleidsnota 1282/013; SFPIM group",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"status": "create_ops_coming_months", "capital": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Strengthen BE defence industry via risk capital",
        cut_option="Capital + investment policy FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>SFPIM>Defence",
        notes="tick798",
    ),
    C(
        commitment_id="cmt_srff_plus_100_staff",
        title="SRFF fiscal-financial investigation service +100 staff",
        entity_id=ENT,
        beneficiary="tax/financial fraud enforcement",
        legal_basis="Beleidsnota 1282/013; fraud law forthcoming",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"fte_plus": 100, "payroll": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Accelerate fight against fiscal and financial fraud",
        cut_option="Payroll path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Finance>SRFF",
        notes="tick798",
    ),
    C(
        commitment_id="cmt_dual_fin_taxex_tick798",
        title="Dual Fin demo VAT 250m + heatpump 10.1m residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/013 dual prior CoA taxex",
        decision_date="2026-08-04",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="260100000",
        cash_by_year='{"demo_cruise_m": 250, "heatpump_m": 10.1, "cgt_aggregate": "Unknown", "sfpim_def": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map Fin taxex residual dual prior inventory",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Fin_taxex",
        notes="tick798",
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
        "lb_vat_demo_rebuild_250m",
        "VAT demolition/rebuild cruise tax cut 250m",
        "taxex",
        "Federal>Taxex>VAT_demo_rebuild",
        "250000000",
        "250000000",
        "Strong primary cruise-speed 250m; path to cruise and volume residual FOI; not pure waste",
        "strong",
        SRC_MAIN,
        "rebuild taxpayers",
        "5.0",
        "8.5",
        "3.0",
        "6.50",
        "Publish cash-by-year to cruise FOI",
        "tick798",
        goal="Support demo/rebuild via VAT cut",
    ),
    lb(
        "lb_vat_heatpump_10_1m_2026",
        "Heat-pump VAT reduction 10.1m 2026",
        "taxex",
        "Federal>Taxex>VAT_heatpump",
        "10100000",
        "10100000",
        "Strong primary reintroduced 2026-01-01; dual prior CoA -10.1m",
        "strong",
        SRC_MAIN,
        "heat pump installers/households",
        "4.0",
        "5.5",
        "2.0",
        "4.50",
        "Already dual CoA; track volume",
        "tick798",
        goal="Reintroduce heat-pump reduced VAT",
    ),
    lb(
        "lb_sfpim_defence_opaque",
        "SFPIM Defence capital opaque residual",
        "ops",
        "Federal>SFPIM>Defence",
        "0",
        "0",
        "Strong primary entity creation; capital and investment policy Unknown FOI",
        "strong",
        SRC_MAIN,
        "defence dual-use industry",
        "6.5",
        "7.5",
        "3.5",
        "6.70",
        "Capital envelope FOI",
        "tick798",
        goal="Risk capital for defence industry",
    ),
    lb(
        "lb_cgt_exemption_aggregate_opaque",
        "CGT exemption 10k-15k aggregate taxex opaque",
        "taxex",
        "Federal>Taxex>CGT_exemption",
        "0",
        "0",
        "Strong primary unit ceilings; aggregate revenue impact Unknown FOI",
        "strong",
        SRC_MAIN,
        "small investors",
        "5.5",
        "7.0",
        "3.0",
        "5.95",
        "Aggregate taxex estimate FOI",
        "tick798",
        goal="Protect small savers under CGT",
    ),
    lb(
        "lb_srff_plus_100_staff",
        "SRFF fraud unit +100 staff payroll opaque",
        "ops",
        "Federal>Finance>SRFF",
        "0",
        "0",
        "Strong primary FTE +100; payroll Unknown FOI",
        "strong",
        SRC_MAIN,
        "fraud enforcement",
        "3.5",
        "5.0",
        "2.0",
        "4.00",
        "Payroll FOI",
        "tick798",
        goal="Accelerate fiscal-financial fraud fight",
    ),
    lb(
        "lb_dual_fin_taxex_2026",
        "Dual Fin demo 250m + heatpump 10.1m residual",
        "taxex",
        "Belgium>dual>Fin_taxex",
        "260100000",
        "260100000",
        "Strong dual not TE-additive without path; demo cruise + heatpump year class",
        "strong",
        SRC_DUAL,
        "taxpayers multi-measure",
        "5.0",
        "8.5",
        "3.5",
        "6.55",
        "Cross-measure cash FOI",
        "tick798",
        goal="Dual Fin taxex residual map",
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
    "hierarchy_path": "Federal>Finance>taxex_SFPIM_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual Financiën: cash-by-year path to cruise 250m for VAT demo/rebuild and "
        "taxpayer volume behind 48k avg; heatpump 10.1m volume dual CoA; aggregate taxex for "
        "equity credit 7500 and CGT exemption 10k-15k; SRFF +100 staff payroll multi-year; "
        "SFPIM Defence capitalisation and investment policy/statutes; Cost Reduction Law II "
        "measure list; admin sites reduction to 21 savings path"
    ),
    "why_it_matters": (
        "Primary Kamer locks large taxex cruise 250m and new SFPIM Defence vehicle with opaque "
        "capital; residual L5 needed for honest taxex ranking dual FPS inventory"
    ),
    "priority": "9",
    "recipient_body": "FOD Financiën / SFPIM FOI",
    "recipient_email": "",
    "recipient_postal": "https://financien.belgium.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_vat_demo_rebuild_250m|cmt_vat_heatpump_10_1m_2026|cmt_sfpim_defence_entity|"
        "cmt_cgt_exemption_10k_15k|cmt_srff_plus_100_staff|cmt_dual_fin_taxex_tick798"
    ),
    "linked_leaderboard_id": (
        "lb_vat_demo_rebuild_250m|lb_vat_heatpump_10_1m_2026|lb_sfpim_defence_opaque|"
        "lb_cgt_exemption_aggregate_opaque|lb_dual_fin_taxex_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick798 Kamer 1282/013 primary; human send only",
}
if not any(r["gap_id"] == GAP for r in frows):
    frows.append(foi_row)
else:
    frows = [foi_row if r["gap_id"] == GAP else r for r in frows]
write_csv(fp, ffields, frows)

# entity sfpim check - may need fallback
rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys())

for r in rq_rows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick798 Fin 1282/013 VAT demo 250m heatpump 10.1m SFPIM Defence FOI "
            "gap_fin_vat_demo_sfpim_defence_l5"
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
                "Next residual: dual L5 or unmined primary (Beliris 020, Regie 029, Loterij 015, "
                "local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116; progress@800 next "
                "after +2 if ticks hit 800"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick798 after Fin013",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Fin013 VAT demo 250m heatpump 10.1 SFPIM Defence FOI; "
    f"next {NEXT_RQ} Beliris020/Regie029 residual; progress@800 in 2; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/013 Beleidsnota Financiën**, 12p)
- Found (primary 56K1282013):
  - VAT **sloop/heropbouw** reduction: cruise-speed tax cut **€250m**; avg saving **€48k**/taxpayer (programmawet BS 29 Jul 2025)
  - Heat-pump VAT reduction reintroduced **1 Jan 2026**: budget cost **€10.1m** (dual prior CoA)
  - Equity tax credit doubled **€3,750 → €7,500**; CGT annual exemption **€10k** (up to **€15k**)/person
  - **SRFF** + **100** staff for fraud fight (payroll Unknown)
  - Admin sites path to **21** buildings; Cost Reduction Law II planned
  - **SFPIM Defence** entity create/ops (capital Unknown); EU customs abolishes **€150** franchise
- Wrote: budgets +10; commitments +7; leaderboard +6; sources +2; FOI **{GAP}** prio9 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual Beliris020/Regie029; deferred **rq_116**; progress@800 in 2
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
