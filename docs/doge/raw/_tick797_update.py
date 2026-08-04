# tick 797 — rq_788 Kamer DOC 56 1282/024 Beleidsnota KMO/PME residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T19:30:00Z"
TICK = 797
RQ = "rq_788"
NEXT_RQ = "rq_789"
SRC_MAIN = "src_kamer_beleid_kmo_1282_024_2026"
SRC_DUAL = "src_dual_kmo_skf_tick797"
GAP = "gap_kmo_vat_franchise_skf_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282024.pdf"
ENT = "fod_economy"


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
            "title": "Kamer DOC 56 1282/024 Beleidsnota KMO/PME residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister KMO's",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick797 primary 43p: VAT franchise threshold 25k->30k by 2030 (+1k/yr) "
                "budget impact 1480k 2026 / 2630k 2027 / 4030k 2028 / 7020k 2029; annual accounts "
                "filing fee abolition small cos/ASBL charged to Cost Reduction Law envelope 3571k "
                "from 2026; central SME federal-benefits info service 550k conclave; enterprise "
                "counters re-approval by Jun 2026 integrate social insurance funds by end-2026 law "
                "ops 2028-01-01 free BCE delisting Nov 2026; SKF dual Concertation 2025-10-06 "
                "federal 13.13pct of BE 1.659bn = 218m EU + cofin min 25pct = 72m 2026-2032 of which "
                "1/3 (~24m) vulnerable microenterprise climate accompaniment; dual Klima 1282/026; "
                "raw 56K1282024.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual KMO SKF 218m/72m vs Klima 217m residual tick797",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: KMO note BE SKF 1.659bn federal 218m+72m cofin "
                "dual Klima 1282/026 2.21bn total / 217m fed EU / ~72m cofin (rounding); "
                "1/3 cofin ~24m microenterprise path; VAT franchise taxex dual FPS inventory"
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
        budget_id="bud_vat_franchise_impact_2026_1_48m",
        entity_id="fod_finance",
        year="2026",
        amount_eur="1480000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "VAT franchise threshold raise path budget impact 1.480m 2026 (25k->30k by 2030); "
            "tax revenue foregone class; tick797 1282/024"
        ),
    ),
    B(
        budget_id="bud_vat_franchise_impact_2027_2_63m",
        entity_id="fod_finance",
        year="2027",
        amount_eur="2630000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="VAT franchise path budget impact 2.630m 2027; tick797",
    ),
    B(
        budget_id="bud_vat_franchise_impact_2028_4_03m",
        entity_id="fod_finance",
        year="2028",
        amount_eur="4030000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="VAT franchise path budget impact 4.030m 2028; tick797",
    ),
    B(
        budget_id="bud_vat_franchise_impact_2029_7_02m",
        entity_id="fod_finance",
        year="2029",
        amount_eur="7020000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="VAT franchise path budget impact 7.020m 2029; tick797",
    ),
    B(
        budget_id="bud_vat_franchise_impact_sum_2026_29",
        entity_id="fod_finance",
        year="2029",
        amount_eur="15160000",
        basis="derived",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Sum VAT franchise impacts 2026-2029 1.48+2.63+4.03+7.02=15.16m; tick797",
    ),
    B(
        budget_id="bud_annual_accounts_fee_cut_3_571m_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="3571000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Filing fee abolition small companies/ASBL at NBB Balanscentrale; impact 3.571m from "
            "2026 within Cost Reduction Law envelope; tick797"
        ),
    ),
    B(
        budget_id="bud_sme_central_info_service_550k",
        entity_id=ENT,
        year="2026",
        amount_eur="550000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Central SME/self-employed info service on federal benefits; 550k allocated last "
            "budget conclave; tick797"
        ),
    ),
    B(
        budget_id="bud_skf_be_total_1_659bn_kmo_note",
        entity_id="gg_belgium",
        year="2032",
        amount_eur="1659000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "BE Social Climate Fund total 1.659bn 2026-2032 per KMO note (dual Klima 1.66/2.21); tick797"
        ),
    ),
    B(
        budget_id="bud_skf_fed_eu_218m_kmo_note",
        entity_id=ENT,
        year="2032",
        amount_eur="218000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Federal 13.13pct of BE SKF = 218m 2026-2032 (dual Klima 217m rounding); tick797 1282/024"
        ),
    ),
    B(
        budget_id="bud_skf_fed_cofin_72m_kmo_note",
        entity_id=ENT,
        year="2032",
        amount_eur="72000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Federal SKF cofin min 25pct = 72m 2026-2032; dual Klima; tick797",
    ),
    B(
        budget_id="bud_skf_microenterprise_third_24m",
        entity_id=ENT,
        year="2032",
        amount_eur="24000000",
        basis="derived",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "One third of federal cofin 72m = 24m for vulnerable microenterprise climate "
            "accompaniment (grammar: ce montant=72m); tick797"
        ),
    ),
    B(
        budget_id="bud_dual_kmo_skf_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="1659000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual SKF map KMO 1.659bn/218/72 vs Klima 2.21/217/72 residual; not TE-additive; tick797"
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
        commitment_id="cmt_vat_franchise_25k_30k_path",
        title="VAT franchise threshold 25k to 30k by 2030",
        entity_id="fod_finance",
        beneficiary="micro-enterprises / self-employed under franchise",
        legal_basis="Beleidsnota 1282/024; Finance competence",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2030",
        total_envelope_eur="15160000",
        cash_by_year='{"2026_k": 1480, "2027_k": 2630, "2028_k": 4030, "2029_k": 7020, "step_eur": 1000, "target_2030": 30000}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Raise VAT exemption franchise for small businesses",
        cut_option="Annual impact analysis FOI + taxex inventory dual",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Taxex>VAT_franchise",
        notes="tick797 budget impact is revenue foregone",
    ),
    C(
        commitment_id="cmt_annual_accounts_fee_cut_3_571m",
        title="Abolish annual accounts filing fees small cos/ASBL 3.571m from 2026",
        entity_id=ENT,
        beneficiary="small companies and associations",
        legal_basis="Wet Lagere Kosten / Cost Reduction Law envelope; Beleidsnota 1282/024",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="3571000",
        cash_by_year='{"from_2026_k": 3571, "channel": "NBB_balanscentrale", "was": "greffe"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Cut filing costs for small entities",
        cut_option="Already a cut; monitor envelope FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Simplification>accounts_fees",
        notes="tick797",
    ),
    C(
        commitment_id="cmt_sme_central_info_service_550k",
        title="Central SME federal benefits info service 550k",
        entity_id=ENT,
        beneficiary="SMEs and self-employed",
        legal_basis="Enterprise-friendly charter; budget conclave; Beleidsnota 1282/024",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="550000",
        cash_by_year='{"start_k": 550, "source": "last_budget_conclave"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Single contact point on federal SME advantages",
        cut_option="Scope and FTE FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>SME>info_service",
        notes="tick797",
    ),
    C(
        commitment_id="cmt_skf_microenterprise_24m",
        title="SKF vulnerable microenterprise accompaniment ~24m of 72m cofin",
        entity_id=ENT,
        beneficiary="vulnerable microenterprises climate transition",
        legal_basis="Reg (EU) 2023/955; cooperation 2025-10-06; Beleidsnota 1282/024",
        decision_date="2025-10-06",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="24000000",
        cash_by_year='{"fed_eu_m": 218, "cofin_m": 72, "micro_third_m": 24, "be_total_bn": 1.659}',
        remaining_eur="24000000",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Support vulnerable microenterprises in climate transition",
        cut_option="Measure list FOI dual Klima",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>Climate>SKF>microenterprise",
        notes="tick797 one-third of 72m cofin",
    ),
    C(
        commitment_id="cmt_dual_kmo_skf_tick797",
        title="Dual KMO SKF residual vs Klima 1282/026",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/024 dual 1282/026",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2032",
        total_envelope_eur="1659000000",
        cash_by_year='{"be_bn": 1.659, "fed_eu_m": 218, "cofin_m": 72, "klima_fed_eu_m": 217, "klima_total_bn": 2.21}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map KMO SKF residual dual Klima stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>SKF_KMO",
        notes="tick797",
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
        "lb_vat_franchise_path_15_16m",
        "VAT franchise raise path budget impact 15.16m 2026-29",
        "taxex",
        "Federal>Taxex>VAT_franchise",
        "3790000",
        "15160000",
        "Strong primary cash path 1.48/2.63/4.03/7.02m; tax revenue foregone class not pure waste",
        "strong",
        SRC_MAIN,
        "micro franchise taxpayers",
        "4.0",
        "6.0",
        "2.0",
        "4.80",
        "Publish annual impact analyses FOI",
        "tick797",
        goal="Raise VAT exemption franchise",
    ),
    lb(
        "lb_accounts_fee_cut_3_571m",
        "Annual accounts filing fee cut 3.571m from 2026",
        "ops",
        "Federal>Simplification>accounts_fees",
        "3571000",
        "3571000",
        "Strong primary cut within Cost Reduction Law; residual envelope FOI",
        "strong",
        SRC_MAIN,
        "small companies ASBL",
        "2.0",
        "4.5",
        "1.5",
        "3.10",
        "Already a cut — track delivery",
        "tick797",
        goal="Lower filing costs",
    ),
    lb(
        "lb_sme_central_info_550k",
        "Central SME federal benefits info service 550k",
        "ops",
        "Federal>SME>info_service",
        "550000",
        "550000",
        "Strong primary conclave allocation; FTE/scope residual",
        "strong",
        SRC_MAIN,
        "SMEs self-employed",
        "3.5",
        "3.5",
        "1.5",
        "3.15",
        "Scope FOI",
        "tick797",
        goal="Single federal benefits contact point",
    ),
    lb(
        "lb_skf_microenterprise_24m",
        "SKF vulnerable microenterprise path ~24m",
        "transfer",
        "Federal>Climate>SKF>microenterprise",
        "3428571",
        "24000000",
        "Medium: 1/3 of 72m cofin for microenterprise accompaniment; measure list FOI",
        "medium",
        SRC_MAIN,
        "vulnerable microenterprises",
        "5.0",
        "6.5",
        "2.5",
        "5.45",
        "L5 measure matrix FOI",
        "tick797",
        goal="Climate transition support microenterprises",
    ),
    lb(
        "lb_dual_kmo_skf_2026",
        "Dual KMO SKF 218/72 vs Klima residual",
        "ops",
        "Belgium>dual>SKF_KMO",
        "0",
        "1659000000",
        "Strong dual not TE-additive; KMO 1.659bn/218/72 dual Klima 2.21/217/72",
        "strong",
        SRC_DUAL,
        "multi-level SKF",
        "5.0",
        "8.0",
        "3.0",
        "6.20",
        "Cross-doc L5 FOI",
        "tick797",
        goal="Dual SKF residual map",
    ),
    lb(
        "lb_vat_franchise_2026_1_48m",
        "VAT franchise budget impact 1.48m 2026",
        "taxex",
        "Federal>Taxex>VAT_franchise>2026",
        "1480000",
        "1480000",
        "Strong primary first-year impact",
        "strong",
        SRC_MAIN,
        "franchise regime taxpayers",
        "3.5",
        "4.0",
        "1.5",
        "3.50",
        "Impact analysis FOI",
        "tick797",
        goal="First-year franchise raise",
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
    "hierarchy_path": "Federal>SME>VAT_SKF_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual KMO: VAT franchise raise methodology behind 1.48/2.63/4.03/7.02m path and "
        "annual impact analyses; Cost Reduction Law envelope reconciliation for 3.571m accounts "
        "fee cut; central SME info service 550k FTE and scope; SKF microenterprise 1/3 of 72m "
        "measure list cash-by-year dual Klima 217/72; enterprise counters re-approval decision "
        "Jun 2026 and tariff reform BCE registration fees after integration with social insurance "
        "funds 2028"
    ),
    "why_it_matters": (
        "Primary Kamer gives precise taxex and simplification impacts plus SKF microenterprise "
        "slice; residual L5 needed for honest taxex ranking and dual Klima delivery"
    ),
    "priority": "8",
    "recipient_body": "FOD Economie (KMO) / FOD Financiën FOI",
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
        "cmt_vat_franchise_25k_30k_path|cmt_annual_accounts_fee_cut_3_571m|"
        "cmt_sme_central_info_service_550k|cmt_skf_microenterprise_24m|cmt_dual_kmo_skf_tick797"
    ),
    "linked_leaderboard_id": (
        "lb_vat_franchise_path_15_16m|lb_accounts_fee_cut_3_571m|lb_sme_central_info_550k|"
        "lb_skf_microenterprise_24m|lb_dual_kmo_skf_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick797 Kamer 1282/024 primary; human send only",
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
            "tick797 KMO 1282/024 VAT franchise 15.16m accounts 3.571m SKF micro 24m "
            "FOI gap_kmo_vat_franchise_skf_l5"
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
                "Next residual: dual L5 or unmined primary (Digi 030 thin, local/CoA, other 1282/* "
                "e.g. 001-005 010-013 015 018 020 027-037 039-040); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick797 after KMO024",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} KMO024 VAT franchise 15.16m accounts 3.571 SKF micro24 FOI; "
    f"next {NEXT_RQ} local/CoA residual; progress@800 in 3; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/024 Beleidsnota KMO/PME**, 43p)
- Found (primary 56K1282024):
  - VAT franchise **€25k → €30k by 2030** (+€1k/yr): budget impact **€1.48m** 2026 · **€2.63m** 2027 · **€4.03m** 2028 · **€7.02m** 2029 (**sum €15.16m**)
  - Annual accounts filing fee cut small cos/ASBL **€3.571m** from 2026 (Cost Reduction Law envelope)
  - Central SME federal-benefits info service **€550k** (budget conclave)
  - SKF dual: BE **€1.659bn** 2026–2032 · federal **13.13% = €218m** · cofin **€72m** · **1/3 ≈ €24m** vulnerable microenterprises
  - Dual Klima 1282/026 (217m/72m rounding)
- Wrote: budgets +12; commitments +5; leaderboard +6; sources +2; FOI **{GAP}** prio8 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual local/CoA; deferred **rq_116**; progress@800 in 3
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
