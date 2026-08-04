# tick 793 — rq_784 Kamer DOC 56 1282/016 Beleidsnota Federale Culturele Instellingen
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T17:30:00Z"
TICK = 793
RQ = "rq_784"
NEXT_RQ = "rq_785"
SRC_MAIN = "src_kamer_beleid_cultuur_1282_016_2026"
SRC_DUAL = "src_dual_fed_culture_tick793"
GAP = "gap_fed_culture_3inst_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282016.pdf"


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
            "title": "Kamer DOC 56 1282/016 Beleidsnota Federale Culturele Instellingen residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Federale Culturele Instellingen",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick793 primary 38p: three federal cultural institutions federal dots IB2026 "
                "NOB 10.943m (2025 total 11.061m); La Monnaie 42.248m (2025 42.754834m); Bozar 15.523m "
                "(2025 15.660m); linear economy 1.8pct + index jump less 2026; Nationale Loterij "
                "NOB 1.75m Monnaie 1.75m Bozar 3.5m (2024 definitive / 2025 provisional plan figures); "
                "Monnaie total exp 64.7m 2026 (struct 44.5 artistic 11.7 ops 2.5 tax shelter exp 6.0); "
                "struct rev 44.5 of which federal staff 31.8m 49.1pct + Beliris building 2.4m; federal "
                "dot 42.8m =66.2pct; Tax Shelter 4.4m 2026; Bozar 2025 exp 37.8m (ops 34.7 relance 1.5 "
                "invest 1.6 Beliris 0.8); 2026 ops 35.6m (+0.9); commercial 13.7m path; VL cut 107k; "
                "Cyprus EU presidency collab ~150k; NOB staff +737k; raw 56K1282016.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual federal culture 3-inst dots ~68.7m vs city culture residual tick793",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: federal dots NOB+Monnaie+Bozar 68.714m IB2026 "
                "(+ lottery ~7m class) dual city culture stacks (Antwerp 35m prior) and Beliris "
                "building lines; L5 residual management contracts 2026-29 cash and lottery year split"
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
        budget_id="bud_nob_dot_2025_total",
        entity_id="nob_orchestre",
        year="2025",
        amount_eur="11061000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="NOB/BNO totale federale dotatie 2025 11.061m; tick793 1282/016",
    ),
    B(
        budget_id="bud_nob_dot_ib2026",
        entity_id="nob_orchestre",
        year="2026",
        amount_eur="10943000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="NOB initiële begroting 2026 10.943m (1.8pct linear + index jump less); tick793",
    ),
    B(
        budget_id="bud_monnaie_dot_2025_total",
        entity_id="la_monnaie",
        year="2025",
        amount_eur="42754834",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="La Monnaie/Munt totale federale dotatie 2025 42.754834m; tick793",
    ),
    B(
        budget_id="bud_monnaie_dot_ib2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="42248000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="La Monnaie initiële begroting 2026 42.248m; tick793",
    ),
    B(
        budget_id="bud_bozar_dot_2025_total",
        entity_id="bozar",
        year="2025",
        amount_eur="15660000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar/PSK totale federale dotatie 2025 15.660m; tick793",
    ),
    B(
        budget_id="bud_bozar_dot_ib2026",
        entity_id="bozar",
        year="2026",
        amount_eur="15523000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar initiële begroting 2026 15.523m; tick793",
    ),
    B(
        budget_id="bud_fed_culture_3inst_dots_ib2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="68714000",
        basis="derived",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Sum federal dots IB2026 NOB 10.943 + Monnaie 42.248 + Bozar 15.523 = 68.714m; tick793"
        ),
    ),
    B(
        budget_id="bud_nob_loterie_1_75m",
        entity_id="nob_orchestre",
        year="2025",
        amount_eur="1750000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "Nationale Loterij subsidy NOB 1.75m from 2024 definitive / 2025 provisional plan "
            "figures in 1282/016 (year split residual FOI); tick793"
        ),
    ),
    B(
        budget_id="bud_monnaie_loterie_1_75m",
        entity_id="la_monnaie",
        year="2025",
        amount_eur="1750000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Nationale Loterij subsidy Monnaie 1.75m (plan figures 1282/016); tick793",
    ),
    B(
        budget_id="bud_bozar_loterie_3_5m",
        entity_id="bozar",
        year="2025",
        amount_eur="3500000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="medium",
        notes="Nationale Loterij subsidy Bozar 3.5m (plan figures 1282/016); tick793",
    ),
    B(
        budget_id="bud_monnaie_total_exp_64_7m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="64700000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="De Munt totale uitgaven 2026 64.7m; tick793",
    ),
    B(
        budget_id="bud_monnaie_struct_exp_44_5m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="44500000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monnaie structurele uitgaven 44.5m 2026; tick793",
    ),
    B(
        budget_id="bud_monnaie_artistic_exp_11_7m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="11700000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monnaie artistieke uitgaven 11.7m 2026; tick793",
    ),
    B(
        budget_id="bud_monnaie_tax_shelter_exp_6m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="6000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monnaie Tax Shelter uitgaven 6.0m 2026; tick793",
    ),
    B(
        budget_id="bud_monnaie_tax_shelter_rev_4_4m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="4400000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monnaie Tax Shelter inkomsten boekjaar 2026 4.4m (6.8pct); tick793",
    ),
    B(
        budget_id="bud_monnaie_federal_staff_rev_31_8m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="31800000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Monnaie structurele inkomsten federal staff path 31.8m =49.1pct of total exp; tick793"
        ),
    ),
    B(
        budget_id="bud_monnaie_beliris_building_2_4m_2026",
        entity_id="la_monnaie",
        year="2026",
        amount_eur="2400000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Monnaie Beliris gebouw 2.4m 2026 (3.8pct); tick793",
    ),
    B(
        budget_id="bud_bozar_exp_2025_37_8m",
        entity_id="bozar",
        year="2025",
        amount_eur="37800000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Bozar uitgavenbudget 2025 37.8m (ops 34.7 + relance 1.5 + invest 1.6); tick793"
        ),
    ),
    B(
        budget_id="bud_bozar_ops_2025_34_7m",
        entity_id="bozar",
        year="2025",
        amount_eur="34700000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar operationele kosten 2025 34.7m; tick793",
    ),
    B(
        budget_id="bud_bozar_ops_2026_35_6m",
        entity_id="bozar",
        year="2026",
        amount_eur="35600000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar werkingsuitgaven 2026 35.6m (+0.9m / +2.6pct); tick793",
    ),
    B(
        budget_id="bud_bozar_commercial_rev_13_7m_2026",
        entity_id="bozar",
        year="2026",
        amount_eur="13700000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar tickets+zaalverhuur+mecenaat path 13.7m 2026 (13.5m 2025); tick793",
    ),
    B(
        budget_id="bud_bozar_vl_cut_107k_2026",
        entity_id="bozar",
        year="2026",
        amount_eur="-107000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Vlaamse Gemeenschap projectsteun Bozar cut 107k 2026; tick793",
    ),
    B(
        budget_id="bud_bozar_cyprus_presidency_150k_2026",
        entity_id="bozar",
        year="2026",
        amount_eur="150000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Bozar Cypriotisch EU-voorzitterschap collab ~150k H1 2026; tick793",
    ),
    B(
        budget_id="bud_nob_staff_plus_737k_2026",
        entity_id="nob_orchestre",
        year="2026",
        amount_eur="737000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="NOB personeelskost +737k 2026 path; tick793",
    ),
    B(
        budget_id="bud_dual_fed_culture_3inst_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="68714000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual map federal culture 3-inst dots 68.714m IB2026 vs city culture residual; "
            "not TE-additive; tick793"
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
        commitment_id="cmt_fed_culture_3inst_dots_2026",
        title="Federal culture 3 institutions dots IB2026 68.714m",
        entity_id="gg_belgium",
        beneficiary="NOB + La Monnaie + Bozar",
        legal_basis="Beheersovereenkomsten + Beleidsnota 1282/016; linear 1.8pct RA",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="68714000",
        cash_by_year='{"nob_m": 10.943, "monnaie_m": 42.248, "bozar_m": 15.523, "linear_pct": 1.8}',
        remaining_eur="68714000",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Federal operating dots three cultural institutions",
        cut_option="Management contract KPIs + dual city FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Culture>3institutions",
        notes="tick793",
    ),
    C(
        commitment_id="cmt_monnaie_budget_64_7m_2026",
        title="La Monnaie total expenditure budget 64.7m 2026",
        entity_id="la_monnaie",
        beneficiary="opera public + artists",
        legal_basis="Wet 19 apr 1963 + Beleidsnota 1282/016",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="64700000",
        cash_by_year='{"total_m": 64.7, "struct_m": 44.5, "artistic_m": 11.7, "ops_m": 2.5, "tax_shelter_exp_m": 6.0, "fed_dot_m": 42.8}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Opera house full TCO 2026",
        cut_option="L5 artistic vs structure FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Culture>Monnaie",
        notes="tick793",
    ),
    C(
        commitment_id="cmt_bozar_ops_35_6m_2026",
        title="Bozar operating expenditure 35.6m 2026",
        entity_id="bozar",
        beneficiary="multidisciplinary arts audiences",
        legal_basis="Wet 7 mei 1999 PSK + Beleidsnota 1282/016",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="35600000",
        cash_by_year='{"ops_2026_m": 35.6, "ops_2025_m": 34.7, "fed_dot_m": 15.523, "commercial_m": 13.7}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Bozar operating balance / positive ESA",
        cut_option="Project subsidies dual FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Culture>Bozar",
        notes="tick793",
    ),
    C(
        commitment_id="cmt_fed_culture_management_2026_29",
        title="New management contracts 3 federal culture institutions 2026-2029",
        entity_id="gg_belgium",
        beneficiary="NOB Monnaie Bozar",
        legal_basis="Organic laws + Beleidsnota 1282/016",
        decision_date="2026-01-23",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"period": "2026-2029", "prior_expired": "2024-12-31", "extended_until_new": true}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="New performance management contracts",
        cut_option="Publish contracts + KPI cash FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Culture>management_contracts",
        notes="tick793",
    ),
    C(
        commitment_id="cmt_loterie_culture_3inst",
        title="Nationale Loterij subsidies 3 federal culture institutions ~7m class",
        entity_id="gg_belgium",
        beneficiary="NOB 1.75 + Monnaie 1.75 + Bozar 3.5",
        legal_basis="Loterie verdelingsplan + Beleidsnota 1282/016",
        decision_date="2025-01-01",
        start_year="2024",
        end_year="2025",
        total_envelope_eur="7000000",
        cash_by_year='{"nob": 1750000, "monnaie": 1750000, "bozar": 3500000, "year_split": "FOI"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Lottery top-up federal culture dots",
        cut_option="Year-split FOI 2024 vs 2025",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="Federal>Culture>Loterie",
        notes="tick793",
    ),
    C(
        commitment_id="cmt_dual_fed_culture_tick793",
        title="Dual federal culture 68.7m vs city culture residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/016 dual city culture prior",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="68714000",
        cash_by_year='{"fed_dots_m": 68.714, "loterie_class_m": 7.0, "monnaie_tco_m": 64.7, "bozar_ops_m": 35.6}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map federal culture residual dual city stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Culture",
        notes="tick793",
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
        "lb_fed_culture_3inst_68_7m_2026",
        "Federal culture 3-inst dots 68.7m IB2026",
        "transfer",
        "Federal>Culture>3institutions",
        "68714000",
        "68714000",
        "Strong primary sum NOB+Monnaie+Bozar; linear 1.8pct already applied; L5 residual contracts",
        "strong",
        SRC_MAIN,
        "3 federal cultural institutions",
        "5.0",
        "7.5",
        "2.5",
        "6.00",
        "Publish management contracts 2026-29 + outcome KPIs",
        "tick793",
        goal="Federal cultural public-service dots",
    ),
    lb(
        "lb_monnaie_dot_42_2m_2026",
        "La Monnaie federal dot 42.2m IB2026",
        "transfer",
        "Federal>Culture>Monnaie>dot",
        "42248000",
        "42248000",
        "Strong primary; TCO 64.7m with tax shelter and Beliris dual",
        "strong",
        SRC_MAIN,
        "opera audiences Brussels",
        "5.5",
        "7.0",
        "2.5",
        "5.85",
        "TCO transparency FOI",
        "tick793",
        goal="Opera federal operating grant",
    ),
    lb(
        "lb_monnaie_tco_64_7m_2026",
        "La Monnaie total expenditure TCO 64.7m 2026",
        "ops",
        "Federal>Culture>Monnaie>TCO",
        "64700000",
        "64700000",
        "Strong primary full house budget; federal dot 66.2pct; tax shelter 6m exp / 4.4m rev",
        "strong",
        SRC_MAIN,
        "opera house",
        "5.5",
        "7.5",
        "3.0",
        "6.10",
        "Artistic vs structure L5 FOI",
        "tick793",
        goal="Full Monnaie TCO",
    ),
    lb(
        "lb_bozar_dot_15_5m_2026",
        "Bozar federal dot 15.5m IB2026",
        "transfer",
        "Federal>Culture>Bozar>dot",
        "15523000",
        "15523000",
        "Strong primary; ops 35.6m dual commercial 13.7m",
        "strong",
        SRC_MAIN,
        "multidisciplinary arts",
        "5.0",
        "6.5",
        "2.0",
        "5.40",
        "Project list dual FOI",
        "tick793",
        goal="Bozar federal operating grant",
    ),
    lb(
        "lb_bozar_ops_35_6m_2026",
        "Bozar operating expenditure 35.6m 2026",
        "ops",
        "Federal>Culture>Bozar>ops",
        "35600000",
        "35600000",
        "Strong primary ops path +0.9m; dual VL cut 107k and EU projects",
        "strong",
        SRC_MAIN,
        "Bozar audiences",
        "5.0",
        "7.0",
        "2.5",
        "5.70",
        "EU project cash FOI",
        "tick793",
        goal="Bozar operating balance",
    ),
    lb(
        "lb_nob_dot_10_9m_2026",
        "NOB federal dot 10.9m IB2026",
        "transfer",
        "Federal>Culture>NOB>dot",
        "10943000",
        "10943000",
        "Strong primary; staff +737k residual; lottery 1.75m dual",
        "strong",
        SRC_MAIN,
        "national orchestra",
        "4.5",
        "6.0",
        "2.0",
        "4.90",
        "Synergy with Monnaie FOI",
        "tick793",
        goal="National orchestra federal grant",
    ),
    lb(
        "lb_loterie_culture_7m_class",
        "Nationale Loterij culture top-up ~7m class",
        "transfer",
        "Federal>Culture>Loterie",
        "7000000",
        "7000000",
        "Medium: plan figures 1.75+1.75+3.5; year 2024 vs 2025 split residual FOI",
        "medium",
        SRC_MAIN,
        "3 institutions",
        "5.5",
        "5.5",
        "1.5",
        "5.05",
        "Publish definitive year matrix FOI",
        "tick793",
        goal="Lottery culture subsidies",
    ),
    lb(
        "lb_dual_fed_culture_2026",
        "Dual federal culture 68.7m vs city culture residual",
        "ops",
        "Belgium>dual>Culture",
        "68714000",
        "68714000",
        "Strong dual not TE-additive; fed 3-inst vs Antwerp 35m class prior",
        "strong",
        SRC_DUAL,
        "multi-level culture",
        "5.0",
        "7.5",
        "3.0",
        "5.95",
        "Cross-level L5 FOI",
        "tick793",
        goal="Dual culture residual map",
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
    "hierarchy_path": "Federal>Culture>3inst_L5",
    "entity_id": "bozar",
    "what_is_missing": (
        "L5 residual federal culture: signed management contracts 2026-2029 for NOB/Monnaie/Bozar "
        "with KPI cash tables; Nationale Loterij year-split 2024 definitive vs 2025 provisional "
        "amounts and 2026 plan; Monnaie Tax Shelter 4.4m/6.0m counterparties; Beliris Monnaie 2.4m "
        "+ Bozar invest lines detail; Bozar EU project cash (PIT CARE Beautifood Halaqat Studiotopia) "
        "and Cyprus presidency 150k financing matrix; VL 107k cut base amount before cut; NOB "
        "parastataux pool contribution inside 10.943m; linear 1.8pct application method per institution"
    ),
    "why_it_matters": (
        "Primary Kamer publishes dots and TCO aggregates but management-contract L5 and lottery "
        "year split remain opaque; dual city culture stacks need federal residual for honest ranking"
    ),
    "priority": "8",
    "recipient_body": "Kabinet Federale Culturele Instellingen / NOB / La Monnaie / Bozar / Nationale Loterij FOI",
    "recipient_email": "",
    "recipient_postal": "https://www.bozar.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_fed_culture_3inst_dots_2026|cmt_monnaie_budget_64_7m_2026|cmt_bozar_ops_35_6m_2026|"
        "cmt_loterie_culture_3inst|cmt_fed_culture_management_2026_29"
    ),
    "linked_leaderboard_id": (
        "lb_fed_culture_3inst_68_7m_2026|lb_monnaie_tco_64_7m_2026|lb_bozar_ops_35_6m_2026|"
        "lb_loterie_culture_7m_class|lb_dual_fed_culture_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick793 Kamer 1282/016 primary; human send only",
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
            "tick793 Cultuur 1282/016 3-inst dots 68.714m Monnaie TCO 64.7 Bozar ops 35.6 "
            "FOI gap_fed_culture_3inst_l5"
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
                "Next residual: dual L5 or unmined primary (Energie 041, IBZ 019, Buitenland 006, "
                "Digitalisering 030, local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick793 after Cultuur016",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Cultuur016 3inst 68.714m Monnaie64.7 Bozar35.6 FOI; "
    f"next {NEXT_RQ} Energie041/IBZ019 residual; progress@800 in 7; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/016 Beleidsnota Federale Culturele Instellingen**, 38p)
- Found (primary 56K1282016):
  - Federal dots IB2026: **NOB €10.943m** (2025 total €11.061m); **La Monnaie €42.248m** (2025 €42.755m); **Bozar €15.523m** (2025 €15.660m)
  - **Sum 3-inst dots €68.714m**; linear economy **1.8%** + index jump less 2026
  - Nationale Loterij: NOB **€1.75m** + Monnaie **€1.75m** + Bozar **€3.5m** (~€7m class; year split FOI)
  - Monnaie **TCO €64.7m** 2026 (struct €44.5 / artistic €11.7 / ops €2.5 / Tax Shelter exp €6.0); fed dot 66.2%; Tax Shelter rev **€4.4m**
  - Bozar ops **€35.6m** 2026 (+€0.9m); 2025 total exp **€37.8m**; commercial path **€13.7m**; VL cut **€107k**; Cyprus collab **~€150k**
  - NOB staff **+€737k**; management contracts **2026–2029** pending
- Wrote: budgets +25; commitments +6; leaderboard +8; sources +2; FOI **{GAP}** prio8 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual Energie041/IBZ019; deferred **rq_116**; progress@800 in 7
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
