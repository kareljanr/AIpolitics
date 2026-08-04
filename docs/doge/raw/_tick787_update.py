# tick 787 — rq_778 Kamer DOC 56 1282/022 Beleidsnota Defensie
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T14:30:00Z"
SRC_MAIN = "src_kamer_beleid_defensie_1282_022_2026"
SRC_DUAL = "src_dual_defensie_tick787"
GAP = "gap_def_safe_ukraine_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282022.pdf"
ENT = "mod_defensie"


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
            "title": "Kamer DOC 56 1282/022 Beleidsnota Defensie residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Defensie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick787: NATO path to 2035 core military 3.5pct GDP + broader security "
                "1.5pct GDP; SAFE EU 150bn loans BE provisional allocation 8.34bn Sep2025 for "
                "Strategic Vision programmes; Paasakkoord 11Apr2025 Ukraine support 1bn/yr to end "
                "legislature; List/Ukraine Security Initiative 100m BE contrib (Jul2025 pack); "
                "NGI base grant +2.58m 2025; CDSCA holiday centers >1.5m modernisation 3yrs; "
                "CDSCA housing masterplan extra 4m 2025; raw 56K1282022_beleid_defensie.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Defensie SAFE 8.34bn vs NATO 2pct/3.5pct residual tick787",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: SAFE loan allocation 8.34bn vs existing NATO effort "
                "~13bn 2026; Ukraine 1bn/yr dual prior defence packages; 3.5+1.5pct path vs 2pct"
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
        budget_id="bud_nato_core_3_5pct_gdp_2035",
        entity_id=ENT,
        year="2035",
        amount_eur="",
        basis="target",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="NATO path by 2035: invest 3.5pct GDP core military spend + 1.5pct broader security/resilience; tick787 1282/022",
    ),
    B(
        budget_id="bud_nato_broader_security_1_5pct_gdp_2035",
        entity_id=ENT,
        year="2035",
        amount_eur="",
        basis="target",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Broader security-related investments 1.5pct GDP by 2035 (critical infra, networks, civil resilience, defence industry); tick787",
    ),
    B(
        budget_id="bud_safe_eu_envelope_150bn",
        entity_id=ENT,
        year="2026",
        amount_eur="150000000000",
        basis="programme",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="EU SAFE Security Action for Europe 150bn EUR loans at favourable rates for joint purchases (EU-level pool not BE spend); tick787",
    ),
    B(
        budget_id="bud_safe_be_allocation_8_34bn_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="8340000000",
        basis="indicative",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="EC Sep2025 provisional SAFE allocation BE 8.34bn EUR loans for Strategic Vision programmes; dual with FOD Fin/Eco/BZ; tick787",
    ),
    B(
        budget_id="bud_ukraine_paasakkoord_1bn_yr_2025_29",
        entity_id=ENT,
        year="2026",
        amount_eur="1000000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Paasakkoord 11 Apr 2025: 1bn EUR/year Ukraine support to end legislature; MR 16 May 2025 urgent military purchases; tick787",
    ),
    B(
        budget_id="bud_ukraine_list_contrib_100m",
        entity_id=ENT,
        year="2025",
        amount_eur="100000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="BE contrib 100m EUR to List/Ukraine Security Initiative 5th support package (approved Jul2025); continued 2026; tick787",
    ),
    B(
        budget_id="bud_ngi_dot_plus_2_58m_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="2580000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="NGI/IGN base grant increased +2.58m EUR 2025 (staff + high-value geospatial services directive); tick787",
    ),
    B(
        budget_id="bud_cdsca_holiday_modern_1_5m_3yr",
        entity_id=ENT,
        year="2025",
        amount_eur="1500000",
        basis="spent",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="CDSCA >1.5m EUR spent last 3 years modernising Defence holiday centres in BE; tick787",
    ),
    B(
        budget_id="bud_cdsca_housing_extra_4m_2025",
        entity_id=ENT,
        year="2025",
        amount_eur="4000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="CDSCA extra budget 4m EUR 2025 for housing masterplan / quartier plan; credits by investment need; tick787",
    ),
    B(
        budget_id="bud_dual_defensie_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="8340000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor SAFE BE 8.34bn loan allocation class; not TE-additive cash; tick787",
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
        commitment_id="cmt_nato_3_5_1_5_path_2035",
        title="NATO spend path 3.5pct core + 1.5pct broader by 2035",
        entity_id=ENT,
        beneficiary="Defence / security",
        legal_basis="NATO commitment; Beleidsnota Defensie 1282/022",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2035",
        total_envelope_eur="0",
        cash_by_year='{"core_gdp_pct_2035": 3.5, "broader_gdp_pct_2035": 1.5}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Ambition path beyond 2pct NATO cash",
        cut_option="Path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Defence>NATO_path",
        notes="tick787 dual existing ~2pct 2026 effort",
    ),
    C(
        commitment_id="cmt_safe_be_8_34bn",
        title="SAFE provisional BE allocation 8.34bn loans",
        entity_id=ENT,
        beneficiary="Defence programmes Strategic Vision",
        legal_basis="EU SAFE; EC Sep2025 allocation; Beleidsnota 1282/022",
        decision_date="2025-09-01",
        start_year="2025",
        end_year="2030",
        total_envelope_eur="8340000000",
        cash_by_year='{"provisional_bn": 8.34, "type": "loans", "eu_pool_bn": 150}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Finance Strategic Vision programmes via joint purchases",
        cut_option="Programme FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Defence>SAFE",
        notes="tick787 not free cash grant",
    ),
    C(
        commitment_id="cmt_ukraine_1bn_yr_legislature",
        title="Ukraine support 1bn EUR/year to end legislature",
        entity_id=ENT,
        beneficiary="Ukraine",
        legal_basis="Paasakkoord 11 Apr 2025; Beleidsnota 1282/022",
        decision_date="2025-04-11",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="0",
        cash_by_year='{"annual_m": 1000, "list_pack_m": 100}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Military materiel and services for Ukraine",
        cut_option="Package FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Defence>Ukraine",
        notes="tick787 + List 100m fifth package",
    ),
    C(
        commitment_id="cmt_cdsca_housing_4m_2025",
        title="CDSCA housing masterplan extra 4m 2025",
        entity_id=ENT,
        beneficiary="military housing",
        legal_basis="Beleidsnota 1282/022",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="4000000",
        cash_by_year='{"2025_m": 4}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Housing / quartier plan for personnel",
        cut_option="Ops FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Defence>CDSCA",
        notes="tick787",
    ),
    C(
        commitment_id="cmt_dual_defensie_tick787",
        title="Dual Defensie SAFE 8.34bn vs NATO residual tick787",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/022",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"safe_bn": 8.34, "ukraine_bn_yr": 1, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map SAFE/Ukraine dual to NATO effort stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>defensie",
        notes="tick787",
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
        "lb_nato_3_5pct_path_2035",
        "NATO core defence path 3.5pct GDP by 2035",
        "ops",
        "Federal>Defence>NATO",
        "0",
        "0",
        "Strong primary target; dual existing ~2pct 2026 ~13bn stack",
        "strong",
        SRC_MAIN,
        "public",
        "5.5",
        "9.5",
        "5.0",
        "7.20",
        "Path FOI",
        "tick787",
    ),
    lb(
        "lb_safe_be_8_34bn",
        "SAFE BE provisional loan allocation 8.34bn",
        "ops",
        "Federal>Defence>SAFE",
        "0",
        "8340000000",
        "Strong EC provisional loan not grant; Strategic Vision dual",
        "strong",
        SRC_MAIN,
        "Defence industry",
        "5.0",
        "9.0",
        "4.0",
        "6.70",
        "Programme FOI",
        "tick787",
    ),
    lb(
        "lb_ukraine_1bn_yr_legislature",
        "Ukraine support 1bn EUR/year Paasakkoord",
        "transfer",
        "Federal>Defence>Ukraine",
        "1000000000",
        "1000000000",
        "Strong annual commitment to end legislature",
        "strong",
        SRC_MAIN,
        "Ukraine",
        "4.5",
        "8.0",
        "3.5",
        "6.05",
        "Package FOI",
        "tick787",
    ),
    lb(
        "lb_ukraine_list_100m",
        "List/Ukraine Security Initiative 100m BE",
        "transfer",
        "Federal>Defence>Ukraine",
        "100000000",
        "100000000",
        "Strong primary fifth package contrib",
        "strong",
        SRC_MAIN,
        "Ukraine",
        "3.5",
        "6.5",
        "2.5",
        "4.75",
        "Package FOI",
        "tick787",
    ),
    lb(
        "lb_cdsca_housing_4m_2025",
        "CDSCA housing masterplan extra 4m 2025",
        "ops",
        "Federal>Defence>CDSCA",
        "4000000",
        "4000000",
        "Strong primary small L5 residual",
        "strong",
        SRC_MAIN,
        "military personnel",
        "2.5",
        "4.0",
        "1.5",
        "3.05",
        "Ops FOI",
        "tick787",
    ),
    lb(
        "lb_ngi_plus_2_58m_2025",
        "NGI base grant +2.58m 2025",
        "ops",
        "Federal>Defence>NGI",
        "2580000",
        "2580000",
        "Strong primary geospatial service uplift",
        "strong",
        SRC_MAIN,
        "public data",
        "2.5",
        "3.5",
        "1.5",
        "2.85",
        "Ops FOI",
        "tick787",
    ),
    lb(
        "lb_dual_defensie_2026",
        "Dual Defensie SAFE 8.34bn vs NATO residual",
        "ops",
        "Belgium>dual>defensie",
        "8340000000",
        "0",
        "Strong dual not TE-additive map loans vs cash effort",
        "strong",
        SRC_DUAL,
        "public",
        "5.0",
        "9.0",
        "4.0",
        "6.70",
        "L5 FOI",
        "tick787",
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
                "hierarchy_path": "Federal>Defence>SAFE_Ukraine_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "SAFE BE 8.34bn: programme list, drawdown schedule, interest terms, "
                    "Strategic Vision mapping; Ukraine 1bn/yr cash path 2025-2029 line items "
                    "(national industry vs other); List 100m reconciliation with 1bn envelope; "
                    "NATO 3.5+1.5pct GDP euro bridge vs existing ~13bn 2026 effort; CDSCA multi-year "
                    "housing investment plan beyond 4m; NGI 2026 grant after +2.58m"
                ),
                "why_it_matters": (
                    "Defence note adds SAFE loans and Ukraine annual 1bn; residual L5 dual to "
                    "NATO cash stack opaque"
                ),
                "priority": "9",
                "recipient_body": "Ministerie van Defensie / FOD Financiën FOI",
                "recipient_email": "",
                "recipient_postal": "https://www.mil.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_safe_be_8_34bn|cmt_ukraine_1bn_yr_legislature|"
                    "cmt_nato_3_5_1_5_path_2035|cmt_dual_defensie_tick787"
                ),
                "linked_leaderboard_id": (
                    "lb_safe_be_8_34bn|lb_ukraine_1bn_yr_legislature|"
                    "lb_nato_3_5pct_path_2035|lb_dual_defensie_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick787 Kamer 1282/022 primary; human send only",
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
    if r["task_id"] == "rq_778":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick787: Defensie 1282/022 SAFE 8.34bn Ukraine 1bn/yr NATO 3.5+1.5pct "
            "List 100m; FOI ready; spawn rq_779"
        )
if not any(r["task_id"] == "rq_779" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_779",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (Mobiliteit 025, Asiel 038, "
                    "Justitie 017, local/CoA); Defensie 1282/022 filled tick787; progress@790 after +3"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick787 after rq_778",
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
        "last_unit_id": "rq_778",
        "ticks_completed": "787",
        "paused": "no",
        "notes": "user paused=no; next rq_779; progress@790 in 3; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
