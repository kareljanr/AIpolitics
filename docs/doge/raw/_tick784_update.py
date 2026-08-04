# tick 784 — rq_775 Kamer DOC 56 1282/042 Beleidsnota Zelfstandigen
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T13:00:00Z"
SRC_MAIN = "src_kamer_beleid_zelfstandigen_1282_042_2026"
SRC_DUAL = "src_dual_zelfstandigen_tick784"
GAP = "gap_rsvz_dot_vuln_egov_l5"
PDF_URL = "https://www.lachambre.be/FLWB/PDF/56/1282/56K1282042.pdf"


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
            "title": "Kamer DOC 56 1282/042 Beleidsnota Zelfstandigen residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Zelfstandigen",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick784: evenwichtsdotatie zelfstandigen 612.744m EUR 2025 "
                "(final at budget control Mar 2026); vulnerable envelope 25m 2026 all schemes "
                "path +25m/yr to 100m 2029; RSVZ pension-reform IT/staff 0.602m 2025 + 1.047m "
                "2026 + structural 0.352m/yr from 2027; RSVZ digitalisation RRP 10m by Jul 2026; "
                "VAPZ max 8.17->8.5pct 2026; birth SS exemption 1->2 quarters; maternity leave "
                "12->15 weeks planned; 105 free service cheques maternity aid kept; raw "
                "56K1282042_beleid_zelfstandigen.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Zelfstandigen RSVZ dot vs vuln envelope / eGov residual tick784",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: RSVZ equilibrium dot 612.7m vs employee SS; "
                "vuln envelope 25-100m dual IVT/illness; VAPZ taxex residual"
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
        budget_id="bud_rsvz_evenwicht_dot_612_7m_2025",
        entity_id="rsvz",
        year="2025",
        amount_eur="612744000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Evenwichtsdotatie zelfstandigenstelsel 612.744k EUR 2025 (algemene uitgavenbegroting 30 Jun 2025 + KB 2 Jul 2025); final Mar 2026 control; tick784",
    ),
    B(
        budget_id="bud_vuln_envelope_all_schemes_25m_2026",
        entity_id="sec_ss",
        year="2026",
        amount_eur="25000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Vulnerable groups envelope 25m 2026 all schemes (replaces welvaartsenveloppe path); tick784 1282/042",
    ),
    B(
        budget_id="bud_vuln_envelope_all_schemes_50m_2027",
        entity_id="sec_ss",
        year="2027",
        amount_eur="50000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Vulnerable envelope path +25m/yr = 50m 2027; tick784",
    ),
    B(
        budget_id="bud_vuln_envelope_all_schemes_75m_2028",
        entity_id="sec_ss",
        year="2028",
        amount_eur="75000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Vulnerable envelope path 75m 2028; tick784",
    ),
    B(
        budget_id="bud_vuln_envelope_all_schemes_100m_2029",
        entity_id="sec_ss",
        year="2029",
        amount_eur="100000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Vulnerable envelope peak 100m 2029; tick784",
    ),
    B(
        budget_id="bud_rsvz_pension_reform_it_0_602m_2025",
        entity_id="rsvz",
        year="2025",
        amount_eur="602304",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="RSVZ extra for pension reform (IT+maintenance+staff) 602304 EUR 2025; tick784",
    ),
    B(
        budget_id="bud_rsvz_pension_reform_it_1_047m_2026",
        entity_id="rsvz",
        year="2026",
        amount_eur="1047216",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="RSVZ pension reform package 1.047m EUR 2026; tick784",
    ),
    B(
        budget_id="bud_rsvz_pension_reform_structural_0_352m_2027",
        entity_id="rsvz",
        year="2027",
        amount_eur="352088",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="RSVZ structural post-reform resources 352088 EUR/yr from 2027; tick784",
    ),
    B(
        budget_id="bud_rsvz_digital_rrp_10m_2026",
        entity_id="rsvz",
        year="2026",
        amount_eur="10000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="RSVZ digitalisation for self-employed RRP/eGov 10m budget finalize by 1 Jul 2026; tick784",
    ),
    B(
        budget_id="bud_vapz_max_rate_8_5pct_2026",
        entity_id="rsvz",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="VAPZ max contribution rate 8.17pct to 8.5pct 2026; social VAPZ adjusted; taxex total Unknown; tick784",
    ),
    B(
        budget_id="bud_maternity_service_cheques_105_unit",
        entity_id="rsvz",
        year="2026",
        amount_eur="105",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Maternity aid: 105 free service cheques after return to work (kept); unit; total Unknown; tick784",
    ),
    B(
        budget_id="bud_selfemp_stock_1_3m_2026",
        entity_id="rsvz",
        year="2026",
        amount_eur="",
        basis="stock",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="1.3 million self-employed under social status; students 10715 end Sep 2025; women 471k (36pct); tick784",
    ),
    B(
        budget_id="bud_dual_zelfstandigen_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="612744000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes="Dual map anchor RSVZ equilibrium dot 612.7m 2025 class; not full TE; tick784",
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
        commitment_id="cmt_rsvz_evenwicht_dot_2025",
        title="RSVZ/self-employed equilibrium dot 612.7m 2025",
        entity_id="rsvz",
        beneficiary="self-employed social status",
        legal_basis="Algemene uitgavenbegroting 30 Jun 2025; KB 2 Jul 2025; Beleidsnota 1282/042",
        decision_date="2025-06-30",
        start_year="2025",
        end_year="2025",
        total_envelope_eur="612744000",
        cash_by_year='{"2025_m": 612.744, "final": "budget control Mar 2026"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Balance self-employed social security system",
        cut_option="Dot FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSVZ>evenwicht",
        notes="tick784",
    ),
    C(
        commitment_id="cmt_vuln_envelope_25_to_100m",
        title="Vulnerable groups envelope 25m 2026 path 100m 2029",
        entity_id="sec_ss",
        beneficiary="vulnerable benefit recipients all schemes",
        legal_basis="Government agreement; Beleidsnota Zelfstandigen 1282/042",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="250000000",
        cash_by_year='{"2026_m": 25, "2027_m": 50, "2028_m": 75, "2029_m": 100}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Replace welvaartsenveloppe with targeted vulnerable envelope",
        cut_option="Allocation FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>SS>vulnerable_envelope",
        notes="tick784 includes self-employed forfait align from 7th month 2027",
    ),
    C(
        commitment_id="cmt_rsvz_pension_reform_ops_2025_27",
        title="RSVZ pension reform IT/staff 0.6m/1.0m/0.35m",
        entity_id="rsvz",
        beneficiary="RSVZ administration",
        legal_basis="Pension reform implementation; Beleidsnota 1282/042",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2027",
        total_envelope_eur="0",
        cash_by_year='{"2025": 602304, "2026": 1047216, "2027_struct": 352088}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="IT maintenance and staff for pension reform execution",
        cut_option="Ops FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSVZ>pension_reform_ops",
        notes="tick784",
    ),
    C(
        commitment_id="cmt_rsvz_digital_rrp_10m",
        title="RSVZ self-employed digitalisation RRP 10m to Jul 2026",
        entity_id="rsvz",
        beneficiary="self-employed digital SS",
        legal_basis="RRP / eGov 3.0; Beleidsnota 1282/042",
        decision_date="2021-01-01",
        start_year="2021",
        end_year="2026",
        total_envelope_eur="10000000",
        cash_by_year='{"envelope_m": 10, "deadline": "2026-07-01"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Source data quality + SS platform for self-employed",
        cut_option="IT FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>RSVZ>eGov",
        notes="tick784",
    ),
    C(
        commitment_id="cmt_vapz_rate_8_5_2026",
        title="VAPZ max rate to 8.5pct 2026 + access all self-employed",
        entity_id="rsvz",
        beneficiary="self-employed 2nd pillar",
        legal_basis="Beleidsnota 1282/042; fiscal/parafiscal standstill 15 Mar 2023",
        decision_date="2025-01-01",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"rate_from": 8.17, "rate_to": 8.5, "taxex": "Unknown"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Strengthen 2nd pillar for self-employed",
        cut_option="Taxex FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>taxex>VAPZ",
        notes="tick784",
    ),
    C(
        commitment_id="cmt_dual_zelfstandigen_tick784",
        title="Dual Zelfstandigen 612.7m dot vs vuln/eGov residual tick784",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/042",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="0",
        cash_by_year='{"dot_m": 612.744, "vuln_2026_m": 25, "digital_m": 10, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map self-employed instruments dual to employee SS",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>zelfstandigen",
        notes="tick784",
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
        "lb_rsvz_evenwicht_612_7m_2025",
        "RSVZ equilibrium dot 612.7m 2025",
        "transfer",
        "Federal>RSVZ>evenwicht",
        "612744000",
        "612744000",
        "Strong primary budget law figure; final at Mar 2026 control",
        "strong",
        SRC_MAIN,
        "self-employed SS",
        "4.0",
        "7.5",
        "3.0",
        "5.55",
        "Dot FOI",
        "tick784",
    ),
    lb(
        "lb_vuln_envelope_25m_2026",
        "Vulnerable envelope all schemes 25m 2026",
        "transfer",
        "Federal>SS>vulnerable",
        "25000000",
        "25000000",
        "Strong path 25/50/75/100m to 2029; dual IVT/illness residual",
        "strong",
        SRC_MAIN,
        "vulnerable",
        "3.0",
        "6.0",
        "2.5",
        "4.35",
        "Allocation FOI",
        "tick784",
    ),
    lb(
        "lb_vuln_envelope_path_100m_2029",
        "Vulnerable envelope path peak 100m 2029",
        "transfer",
        "Federal>SS>vulnerable",
        "100000000",
        "100000000",
        "Strong multi-year path; replaces welvaartsenveloppe logic",
        "strong",
        SRC_MAIN,
        "vulnerable",
        "3.5",
        "7.0",
        "2.5",
        "4.80",
        "Path FOI",
        "tick784",
    ),
    lb(
        "lb_rsvz_digital_rrp_10m",
        "RSVZ digitalisation RRP 10m to Jul 2026",
        "ops",
        "Federal>RSVZ>eGov",
        "10000000",
        "10000000",
        "Strong RRP envelope; dual eGov3.0 residual",
        "strong",
        SRC_MAIN,
        "self-employed",
        "3.5",
        "5.5",
        "2.0",
        "4.15",
        "IT FOI",
        "tick784",
    ),
    lb(
        "lb_rsvz_pension_ops_1_0m_2026",
        "RSVZ pension reform ops 1.047m 2026",
        "ops",
        "Federal>RSVZ>pension_ops",
        "1047216",
        "1047216",
        "Strong IT/staff package peak 2026",
        "strong",
        SRC_MAIN,
        "RSVZ admin",
        "2.5",
        "4.0",
        "1.5",
        "3.05",
        "Ops FOI",
        "tick784",
    ),
    lb(
        "lb_vapz_rate_8_5_2026",
        "VAPZ max rate 8.5pct 2026 taxex residual",
        "taxex",
        "Federal>taxex>VAPZ",
        "0",
        "0",
        "Strong rate policy; aggregate taxex Unknown — FOI",
        "medium",
        SRC_MAIN,
        "self-employed",
        "4.5",
        "6.0",
        "3.5",
        "5.00",
        "Taxex FOI",
        "tick784",
    ),
    lb(
        "lb_maternity_aid_105_cheques",
        "Maternity aid 105 free service cheques kept",
        "transfer",
        "Federal>RSVZ>maternity",
        "0",
        "0",
        "Strong unit 105 cheques; total fiscal cost Unknown",
        "medium",
        SRC_MAIN,
        "self-employed mothers",
        "3.0",
        "4.5",
        "2.0",
        "3.55",
        "Cost FOI",
        "tick784",
    ),
    lb(
        "lb_dual_zelfstandigen_2026",
        "Dual Zelfstandigen 612.7m vs vuln/eGov residual",
        "transfer",
        "Belgium>dual>zelfstandigen",
        "612744000",
        "0",
        "Strong dual not TE-additive map self-employed instruments",
        "strong",
        SRC_DUAL,
        "public",
        "4.0",
        "7.5",
        "3.0",
        "5.55",
        "L5 FOI",
        "tick784",
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
                "hierarchy_path": "Federal>RSVZ>dot_vuln_egov_L5",
                "entity_id": "rsvz",
                "what_is_missing": (
                    "Final 2025 and budgeted 2026 evenwichtsdotatie zelfstandigen after Mar 2026 "
                    "control; vulnerable envelope 25-100m allocation by scheme (employee vs "
                    "self-employed vs handicap) and measures list; VAPZ 8.5pct aggregate taxex/"
                    "parafiscal cost 2026; birth 2-quarter SS exemption fiscal cost; maternity "
                    "12to15 weeks cost and 105 service-cheques annual spend; company contribution "
                    "reform by balance-sheet total yield; alt finance %/min-amount KB deltas; "
                    "RSVZ digital 10m spend-to-date and remaining"
                ),
                "why_it_matters": (
                    "Self-employed SS public at aggregate; residual L5 dual to employee SS and "
                    "taxex opaque"
                ),
                "priority": "8",
                "recipient_body": "RSVZ / FOD Sociale Zekerheid FOI",
                "recipient_email": "",
                "recipient_postal": "https://www.rsvz.be",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": "2026-08-04",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": (
                    "cmt_rsvz_evenwicht_dot_2025|cmt_vuln_envelope_25_to_100m|"
                    "cmt_rsvz_digital_rrp_10m|cmt_dual_zelfstandigen_tick784"
                ),
                "linked_leaderboard_id": (
                    "lb_rsvz_evenwicht_612_7m_2025|lb_vuln_envelope_25m_2026|"
                    "lb_rsvz_digital_rrp_10m|lb_dual_zelfstandigen_2026"
                ),
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "tick784 Kamer 1282/042 primary; human send only",
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
    if r["task_id"] == "rq_775":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick784: Zelfstandigen 1282/042 dot 612.7m vuln 25-100m digital 10m "
            "VAPZ 8.5pct; FOI ready; spawn rq_776"
        )
if not any(r["task_id"] == "rq_776" for r in rrows):
    rrows.append(
        {
            k: v
            for k, v in {
                "task_id": "rq_776",
                "title": "Continuous FOI-adjacent public hole-fill batch",
                "sprint": "continuous",
                "priority": "5",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "gg_belgium",
                "instructions": (
                    "Next residual: dual L5 or unmined primary (Pensioenen 1282/014, Asiel "
                    "038, Economie 004, local/CoA); Zelfstandigen 1282/042 filled tick784"
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": "",
                "notes": "spawned tick784 after rq_775",
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
        "last_unit_id": "rq_775",
        "ticks_completed": "784",
        "paused": "no",
        "notes": "user paused=no; next rq_776; progress@790 in 6; rq_116 deferred",
    }
)
write_csv(lsp, lsfields, ls)

print("OK", len(srows), len(brows), len(crows), len(lrows), len(frows), len(rrows))
