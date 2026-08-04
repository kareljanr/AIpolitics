# tick 801 — rq_792 Kamer DOC 56 1282/029 Beleidsnota Regie der Gebouwen residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T21:30:00Z"
TICK = 801
RQ = "rq_792"
NEXT_RQ = "rq_793"
SRC_MAIN = "src_kamer_beleid_regie_1282_029_2026"
SRC_DUAL = "src_dual_regie_prison_tick801"
GAP = "gap_regie_nekp_3bn_prison_264m_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282029.pdf"
ENT = "regie_gebouwen"


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
            "title": "Kamer DOC 56 1282/029 Beleidsnota Regie der Gebouwen residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Gebouwenbeheer van de Staat",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick801 primary 23p: federal portfolio >7m m2; NEKP climate-neutral 2050 "
                "internal estimate >3bn EUR to comply; accessibility study Brussels 350k; rented "
                "surface -1.68pct 2025; 2026 further -1.69pct structural save 13.78m; Arlon/"
                "Neufchateau end lease ~4m free 14838 m2; Jardins Couronne lease ~9m / 38210 m2 "
                "to terminate after Fed Police to Finto; sales 2025 28 buildings 52278 m2; 2026 "
                "target 108166 m2 unused dispose >50m revenue; Justice capacity taskforce credits "
                "264m 2026 and 336m by 2028 (MR 2025-07-18); DBFM prisons avg annual 96.5m; "
                "Vresse-sur-Semois prison construction 2027-28 available early 2029; multi-year "
                "invest plan projects >3m each 15yr horizon; dual prior prison package 600m; "
                "raw 56K1282029.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Regie prison 264m/336m vs package 600m residual tick801",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary Justice capacity credits 264m 2026 / 336m "
                "2028 dual prior prison infra package 600m 2026-29 and DBFM 96.5m/yr; NEKP >3bn "
                "stock dual energy renovation; rent save 13.78m dual FOD Finance sites path"
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
        budget_id="bud_regie_nekp_compliance_gt3bn",
        entity_id=ENT,
        year="2050",
        amount_eur="3000000000",
        amount_min_eur="3000000000",
        amount_max_eur="",
        basis="estimate",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Internal estimate >3bn EUR to bring federal building stock in line with NEKP/"
            "climate-neutral 2050; multi-year stock not pure annual TE; tick801 1282/029"
        ),
    ),
    B(
        budget_id="bud_regie_accessibility_study_bru_350k",
        entity_id=ENT,
        year="2026",
        amount_eur="350000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Accessibility study contract for buildings in Brussels 350k EUR; tick801",
    ),
    B(
        budget_id="bud_regie_rent_save_13_78m_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="13780000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "2026 additional rented surface reduction 1.69pct generating structural save 13.78m; "
            "after 2025 -1.68pct; tick801"
        ),
    ),
    B(
        budget_id="bud_regie_arlon_lease_end_4m",
        entity_id=ENT,
        year="2025",
        amount_eur="4000000",
        amount_min_eur="",
        amount_max_eur="4000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Arlon+Neufchateau: end Finance lease almost 4m EUR; free 14838 m2 to state buildings; tick801"
        ),
    ),
    B(
        budget_id="bud_regie_jardins_couronne_rent_9m",
        entity_id=ENT,
        year="2026",
        amount_eur="9000000",
        amount_min_eur="",
        amount_max_eur="9000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Jardins de la Couronne / Kroontuinen lease almost 9m EUR for 38210 m2 brut; terminate "
            "after Fed Police to Finto; tick801"
        ),
    ),
    B(
        budget_id="bud_regie_sales_revenue_gt50m_2026_target",
        entity_id=ENT,
        year="2026",
        amount_eur="50000000",
        amount_min_eur="50000000",
        amount_max_eur="",
        basis="estimate",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "2026 target dispose unused area 108166 m2 (double 2025 52278 m2 / 28 buildings) "
            "could generate >50m revenue; tick801"
        ),
    ),
    B(
        budget_id="bud_regie_justice_capacity_264m_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="264000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Extra budget credits for Justice real-estate capacity/overcrowding taskforce 264m 2026 "
            "(MR 2025-07-18 action plan); tick801"
        ),
    ),
    B(
        budget_id="bud_regie_justice_capacity_336m_2028",
        entity_id=ENT,
        year="2028",
        amount_eur="336000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Same Justice capacity path 336m by 2028 for new initiatives and prison/FPC capacity; tick801"
        ),
    ),
    B(
        budget_id="bud_regie_dbfm_prisons_avg_96_5m",
        entity_id=ENT,
        year="2026",
        amount_eur="96500000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "DBFM prison commitments average annual investment 96.5m EUR; dual prior fee tables; tick801"
        ),
    ),
    B(
        budget_id="bud_dual_regie_prison_capacity_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="264000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual Justice capacity 264m residual vs prior prison package 600m 2026-29; not TE-additive; tick801"
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
        commitment_id="cmt_regie_nekp_gt3bn",
        title="Regie NEKP building stock compliance estimate >3bn",
        entity_id=ENT,
        beneficiary="federal building portfolio climate compliance",
        legal_basis="NEKP / climate-neutral 2050; Beleidsnota 1282/029",
        decision_date="2026-01-24",
        start_year="2026",
        end_year="2050",
        total_envelope_eur="3000000000",
        cash_by_year='{"estimate_bn": 3, "basis": "internal", "horizon": 2050}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Bring federal buildings to NEKP energy performance",
        cut_option="Project list and cash path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Regie>NEKP",
        notes="tick801 multi-year stock estimate",
    ),
    C(
        commitment_id="cmt_regie_rent_rationalisation_13_78m",
        title="Rented surface rationalisation structural save 13.78m 2026",
        entity_id=ENT,
        beneficiary="federal budget (lower rents)",
        legal_basis="Multi-year rental reduction plan; Beleidsnota 1282/029",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="13780000",
        cash_by_year='{"2025_surface_pct": -1.68, "2026_surface_pct": -1.69, "save_2026_m": 13.78}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reduce rented office area and rental costs",
        cut_option="Already a save — dashboard FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Regie>rent_rationalisation",
        notes="tick801",
    ),
    C(
        commitment_id="cmt_regie_justice_capacity_264_336m",
        title="Justice capacity/overcrowding real-estate credits 264m 2026 / 336m 2028",
        entity_id=ENT,
        beneficiary="prison and FPC capacity + Justice buildings",
        legal_basis="Taskforce Capaciteit; MR 2025-07-18; Beleidsnota 1282/029",
        decision_date="2025-07-18",
        start_year="2026",
        end_year="2028",
        total_envelope_eur="336000000",
        cash_by_year='{"2026_m": 264, "by_2028_m": 336, "includes_FPC": true}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Structural detention capacity and Justice real estate",
        cut_option="Priority project list FOI dual 600m package",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Regie>Justice_capacity",
        notes="tick801",
    ),
    C(
        commitment_id="cmt_regie_dbfm_prisons_96_5m",
        title="DBFM prisons average annual investment 96.5m",
        entity_id=ENT,
        beneficiary="DBFM prison SPVs",
        legal_basis="DBFM prison contracts; Beleidsnota 1282/029",
        decision_date="2026-01-24",
        start_year="2025",
        end_year="2035",
        total_envelope_eur="",
        cash_by_year='{"avg_annual_m": 96.5, "vresse_build": "2027-2028", "vresse_available": "2029-begin"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Continue DBFM prison commitments; Vresse new prison",
        cut_option="Fee table dual prior FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Regie>DBFM_prisons",
        notes="tick801",
    ),
    C(
        commitment_id="cmt_regie_sales_gt50m_2026",
        title="Dispose unused buildings target revenue >50m 2026",
        entity_id=ENT,
        beneficiary="State renovation reinvestment",
        legal_basis="Asset reduction plan; Beleidsnota 1282/029",
        decision_date="2026-01-24",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="50000000",
        cash_by_year='{"target_m2": 108166, "2025_m2": 52278, "2025_buildings": 28, "revenue_gt_m": 50}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Sell/repurpose unused federal buildings",
        cut_option="Sale list and proceeds FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>Regie>disposals",
        notes="tick801 estimate",
    ),
    C(
        commitment_id="cmt_dual_regie_prison_tick801",
        title="Dual Regie Justice capacity vs prison package residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/029 dual prior prison package",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2028",
        total_envelope_eur="336000000",
        cash_by_year='{"2026_m": 264, "2028_m": 336, "prior_package_m": 600, "dbfm_annual_m": 96.5}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map Regie residual dual prison stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Regie_prison",
        notes="tick801",
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
        "lb_regie_nekp_gt3bn",
        "Regie NEKP building compliance estimate >3bn",
        "ops",
        "Federal>Regie>NEKP",
        "0",
        "3000000000",
        "Strong primary internal estimate multi-year stock; project list FOI residual",
        "strong",
        SRC_MAIN,
        "federal building portfolio",
        "6.0",
        "9.0",
        "4.5",
        "7.05",
        "Publish multi-year project cash FOI",
        "tick801",
        goal="Climate-neutral federal buildings by 2050",
    ),
    lb(
        "lb_regie_justice_capacity_264m_2026",
        "Regie Justice capacity credits 264m 2026",
        "ops",
        "Federal>Regie>Justice_capacity",
        "264000000",
        "336000000",
        "Strong primary MR taskforce path 264m 2026 / 336m 2028; dual prior 600m package",
        "strong",
        SRC_MAIN,
        "prisons FPC Justice buildings",
        "5.5",
        "8.0",
        "3.0",
        "6.55",
        "Priority project matrix FOI",
        "tick801",
        goal="Detention capacity and Justice real estate",
    ),
    lb(
        "lb_regie_dbfm_prisons_96_5m",
        "DBFM prisons average annual 96.5m",
        "ops",
        "Federal>Regie>DBFM_prisons",
        "96500000",
        "96500000",
        "Strong primary avg annual; dual prior fee tables Vresse 2029",
        "strong",
        SRC_MAIN,
        "DBFM SPVs",
        "5.0",
        "7.5",
        "3.0",
        "6.05",
        "Annual fee reconciliation FOI",
        "tick801",
        goal="Continue DBFM prison lock-in",
    ),
    lb(
        "lb_regie_rent_save_13_78m",
        "Rented surface rationalisation save 13.78m 2026",
        "ops",
        "Federal>Regie>rent_rationalisation",
        "13780000",
        "13780000",
        "Strong primary structural save from -1.69pct surface; already a cut",
        "strong",
        SRC_MAIN,
        "federal budget",
        "3.0",
        "6.0",
        "2.0",
        "4.35",
        "Dashboard verification FOI",
        "tick801",
        goal="Reduce rental costs",
    ),
    lb(
        "lb_regie_jardins_couronne_9m",
        "Jardins Couronne lease ~9m to terminate",
        "ops",
        "Federal>Regie>leases>Couronne",
        "9000000",
        "9000000",
        "Strong primary almost 9m rent for 38210 m2; terminate after Fed Police move",
        "strong",
        SRC_MAIN,
        "federal police housing",
        "4.5",
        "5.5",
        "2.0",
        "4.70",
        "Confirm termination date FOI",
        "tick801",
        goal="End expensive lease after consolidation",
    ),
    lb(
        "lb_dual_regie_prison_2026",
        "Dual Regie Justice 264m vs prison package residual",
        "ops",
        "Belgium>dual>Regie_prison",
        "264000000",
        "600000000",
        "Strong dual not TE-additive; 264/336 vs prior 600m package + DBFM 96.5",
        "strong",
        SRC_DUAL,
        "multi-channel detention infra",
        "5.5",
        "8.0",
        "3.5",
        "6.50",
        "Cross-doc cash FOI",
        "tick801",
        goal="Dual Regie prison residual map",
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
    "hierarchy_path": "Federal>Regie>NEKP_Justice_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual Regie: multi-year project cash behind NEKP >3bn estimate; investment plan "
        "15yr list of projects >3m each with EUR; Justice capacity 264m 2026 and 336m by 2028 "
        "named priority projects dual prior 600m package; DBFM 96.5m/yr fee reconciliation and "
        "Vresse SPV terms; rent dashboard 13.78m save verification; Jardins Couronne 9m "
        "termination date; 2026 disposal list for >50m revenue target; accessibility study 350k "
        "deliverables"
    ),
    "why_it_matters": (
        "Primary Kamer locks multi-hundred-m Justice real-estate path and multi-bn NEKP estimate "
        "with only aggregates public; residual L5 dual DBFM/prison packages for honest ranking"
    ),
    "priority": "9",
    "recipient_body": "Regie der Gebouwen / FOD Justitie FOI",
    "recipient_email": "",
    "recipient_postal": "https://www.regiedesbatiments.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_regie_nekp_gt3bn|cmt_regie_justice_capacity_264_336m|cmt_regie_dbfm_prisons_96_5m|"
        "cmt_regie_rent_rationalisation_13_78m|cmt_dual_regie_prison_tick801"
    ),
    "linked_leaderboard_id": (
        "lb_regie_nekp_gt3bn|lb_regie_justice_capacity_264m_2026|lb_regie_dbfm_prisons_96_5m|"
        "lb_regie_rent_save_13_78m|lb_dual_regie_prison_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick801 Kamer 1282/029 primary; human send only",
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
            "tick801 Regie 1282/029 NEKP >3bn Justice 264m/336m DBFM 96.5 rent save 13.78 "
            "FOI gap_regie_nekp_3bn_prison_264m_l5"
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
                "Next residual: dual L5 or unmined primary (Loterij 015, POD MI 039, local/CoA, "
                "other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick801 after Regie029",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Regie029 NEKP>3bn Justice264/336 DBFM96.5 rent save13.78 FOI; "
    f"next {NEXT_RQ} Loterij015/PODMI039 residual; progress@810 in 9; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/029 Beleidsnota Regie der Gebouwen**, 23p)
- Found (primary 56K1282029):
  - Federal portfolio **>7m m²**; NEKP compliance internal estimate **>€3bn** to 2050
  - Accessibility study Brussels **€350k**
  - Rented surface **−1.68%** 2025; 2026 further **−1.69%** → structural save **€13.78m**
  - Arlon/Neufchâteau end lease **~€4m** (free **14,838 m²**); Jardins Couronne lease **~€9m** / **38,210 m²** to terminate
  - Sales target 2026: **108,166 m²** unused → revenue **>€50m** (2025: 28 buildings / 52,278 m²)
  - Justice capacity taskforce credits **€264m** 2026 · **€336m** by 2028 (MR 18 Jul 2025)
  - DBFM prisons avg **€96.5m**/yr; Vresse prison build **2027–28** available early **2029**
- Wrote: budgets +10; commitments +6; leaderboard +6; sources +2; FOI **{GAP}** prio9 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual Loterij015/PODMI; deferred **rq_116**; progress@810 in 9
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
