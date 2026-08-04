# tick 794 — rq_785 Kamer DOC 56 1282/019 Beleidsnota Veiligheid en Binnenlandse Zaken
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T18:00:00Z"
TICK = 794
RQ = "rq_785"
NEXT_RQ = "rq_786"
SRC_MAIN = "src_kamer_beleid_ibz_1282_019_2026"
SRC_DUAL = "src_dual_ibz_security_tick794"
GAP = "gap_ibz_plan_grote_steden_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282019.pdf"
ENT = "fod_ibz"


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
            "title": "Kamer DOC 56 1282/019 Beleidsnota Veiligheid en Binnenlandse Zaken residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Veiligheid en Binnenlandse Zaken",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick794 primary 44p: provisie Versterking veiligheidsdiensten en terugkeerbeleid "
                "nearly 0.5bn EUR; police material+digital >150m over legislature; DSU renfort >30m; "
                "Plan Grote Steden budget 71.3m implementation / 71m package 2025-2029 (liaison 4.3 "
                "campaigns 1.8 detection~9 FGP 4.8 special equipment 11 personal protection 4.9 judicial "
                "tools 8 + cameras mass); cameras+ANPR extra 25m paid to zones (BRU 7.5 ANT 7.5 five "
                "cities 1m each=5 other zones 5); ANPR 5k->platform cap 10k; SNCB 8k cameras access; "
                "FANC structural dot prep 2026; iPolice failure residual digital strategy; RvS 2026 "
                "budget correction amount Unknown; raw 56K1282019.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual IBZ Plan Grote Steden 71.3m vs prior police GV path residual tick794",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary Plan GV 71.3/71m 2025-29 dual prior police "
                "grandes villes cumul 43.6m / eng 9.9 liq 13.2 2026; cameras 25m within package dual "
                "city zones; security provision ~0.5bn dual return/asylum stack; DSU 30m dual fed police"
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
        budget_id="bud_ibz_security_return_provision_0_5bn",
        entity_id=ENT,
        year="2026",
        amount_eur="500000000",
        amount_min_eur="450000000",
        amount_max_eur="500000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Provisie Versterking veiligheidsdiensten en terugkeerbeleid nearly half a billion EUR "
            "(presque un demi-milliard / bijna een half miljard); exact envelope FOI; tick794 1282/019"
        ),
    ),
    B(
        budget_id="bud_police_material_digital_gt150m_legislature",
        entity_id="police_federale",
        year="2029",
        amount_eur="150000000",
        amount_min_eur="150000000",
        amount_max_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Federal+local police material renewal + digital modernization >150m over legislature; "
            "floor figure; tick794"
        ),
    ),
    B(
        budget_id="bud_dsu_renfort_gt30m_legislature",
        entity_id="police_federale",
        year="2029",
        amount_eur="30000000",
        amount_min_eur="30000000",
        amount_max_eur="",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="DSU specialized unit renfort >30m additional over path; tick794",
    ),
    B(
        budget_id="bud_plan_grote_steden_71_3m",
        entity_id=ENT,
        year="2029",
        amount_eur="71300000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Plan Grote Steden / Grandes Villes implementation budget 71.3m; package stated 71m "
            "2025-2029; tick794"
        ),
    ),
    B(
        budget_id="bud_plan_gv_liaison_officers_4_3m",
        entity_id="police_federale",
        year="2029",
        amount_eur="4300000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: international liaison officers network 4.3m within 71m package; tick794",
    ),
    B(
        budget_id="bud_plan_gv_campaigns_1_8m",
        entity_id=ENT,
        year="2029",
        amount_eur="1800000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: targeted campaigns grandes villes 1.8m; tick794",
    ),
    B(
        budget_id="bud_plan_gv_detection_intervention_9m",
        entity_id="police_federale",
        year="2029",
        amount_eur="9000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Plan GV: detection/intervention capacities ~9m (specialized dogs, visible vehicles, "
            "ammo, DSU equipment); tick794"
        ),
    ),
    B(
        budget_id="bud_plan_gv_fgp_training_4_8m",
        entity_id="police_federale",
        year="2029",
        amount_eur="4800000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: FGP/PJF training and expertise 4.8m; tick794",
    ),
    B(
        budget_id="bud_plan_gv_special_equipment_11m",
        entity_id="police_federale",
        year="2029",
        amount_eur="11000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: specialized materials acquisition 11m; tick794",
    ),
    B(
        budget_id="bud_plan_gv_personal_protection_4_9m",
        entity_id="police_federale",
        year="2029",
        amount_eur="4900000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: transversal personal protection investments 4.9m; tick794",
    ),
    B(
        budget_id="bud_plan_gv_judicial_tools_8m",
        entity_id="police_federale",
        year="2029",
        amount_eur="8000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Plan GV: specialized judicial tools 8m; tick794",
    ),
    B(
        budget_id="bud_cameras_anpr_extra_25m",
        entity_id=ENT,
        year="2025",
        amount_eur="25000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Cameras+ANPR extra 25m under Plan GV; paid to police zones; dual BRU/ANT 7.5 each; tick794"
        ),
    ),
    B(
        budget_id="bud_cameras_bru_7_5m",
        entity_id=ENT,
        year="2025",
        amount_eur="7500000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Camera envelope Brussels 7.5m of 25m; tick794",
    ),
    B(
        budget_id="bud_cameras_antwerp_7_5m",
        entity_id=ENT,
        year="2025",
        amount_eur="7500000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Camera envelope Antwerp 7.5m of 25m; tick794",
    ),
    B(
        budget_id="bud_cameras_five_cities_5m",
        entity_id=ENT,
        year="2025",
        amount_eur="5000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Camera envelope Charleroi+Namur+Gent+Liège+Mons 1m each = 5m of 25m; tick794"
        ),
    ),
    B(
        budget_id="bud_cameras_other_zones_5m",
        entity_id=ENT,
        year="2025",
        amount_eur="5000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="Camera envelope other police zones 5m by operational cadre size; tick794",
    ),
    B(
        budget_id="bud_anpr_cameras_stock_5000",
        entity_id="police_federale",
        year="2026",
        amount_eur="5000",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="ANPR existing 5000 cameras connecting to platform capacity 10000; amount=count; tick794",
    ),
    B(
        budget_id="bud_sncb_cameras_access_8000",
        entity_id="police_federale",
        year="2026",
        amount_eur="8000",
        basis="count",
        source_id=SRC_MAIN,
        confidence="strong",
        notes="SNCB/NMBS 8000 cameras access for local police zones; amount=count; tick794",
    ),
    B(
        budget_id="bud_dual_ibz_plan_gv_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="71300000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual Plan GV 71.3m residual vs prior police GV 43.6m cumul path; not TE-additive; tick794"
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
        commitment_id="cmt_ibz_security_return_provision_0_5bn",
        title="Security services + return policy provision ~0.5bn",
        entity_id=ENT,
        beneficiary="GPI + governors + National Crisis Centre + return",
        legal_basis="Budget provision Renforcement services sécurité et politique de retour; Beleidsnota 1282/019",
        decision_date="2026-01-23",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="500000000",
        cash_by_year='{"envelope_class_bn": 0.5, "exact": "FOI", "note": "nearly half billion"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Restore operational capacity modernize tools crisis continuity",
        cut_option="Cash-by-year L5 FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>IBZ>security_return_provision",
        notes="tick794",
    ),
    C(
        commitment_id="cmt_plan_grote_steden_71_3m",
        title="Plan Grote Steden / Grandes Villes 71.3m package 2025-2029",
        entity_id=ENT,
        beneficiary="police zones + federal police + cities",
        legal_basis="Plan Grote Steden Sep 2025 + Beleidsnota 1282/019",
        decision_date="2025-09-01",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="71300000",
        cash_by_year='{"implementation_m": 71.3, "package_m": 71, "period": "2025-2029", "liaison_m": 4.3, "campaigns_m": 1.8, "detection_m": 9, "fgp_m": 4.8, "equipment_m": 11, "ppe_m": 4.9, "judicial_m": 8, "cameras_m": 25}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Whole-of-government urban security extending Plan Canal",
        cut_option="Named L5 measure matrix FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>IBZ>PlanGroteSteden",
        notes="tick794",
    ),
    C(
        commitment_id="cmt_cameras_anpr_25m",
        title="Cameras + ANPR extra 25m paid to police zones",
        entity_id=ENT,
        beneficiary="police zones nationwide",
        legal_basis="Plan Grote Steden camera envelope; Beleidsnota 1282/019",
        decision_date="2025-01-01",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="25000000",
        cash_by_year='{"bru_m": 7.5, "ant_m": 7.5, "five_cities_m": 5, "other_zones_m": 5, "status": "paid_to_zones"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Camera deployment and ANPR modernization",
        cut_option="Zone-level camera counts + unit cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>IBZ>cameras_ANPR",
        notes="tick794 primary: amounts already paid",
    ),
    C(
        commitment_id="cmt_police_digital_material_150m",
        title="Police material + digital modernization >150m legislature",
        entity_id="police_federale",
        beneficiary="federal and local police",
        legal_basis="Beleidsnota 1282/019 security investment path",
        decision_date="2026-01-23",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="150000000",
        cash_by_year='{"floor_m": 150, "scope": "material_and_digital", "period": "legislature"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Renew equipment modernize digital tools",
        cut_option="Cash-by-year dual iPolice residual FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Police>material_digital",
        notes="tick794",
    ),
    C(
        commitment_id="cmt_dsu_renfort_30m",
        title="DSU specialized units renfort >30m",
        entity_id="police_federale",
        beneficiary="DSU special units",
        legal_basis="Beleidsnota 1282/019",
        decision_date="2026-01-23",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="30000000",
        cash_by_year='{"floor_m": 30, "unit": "DSU"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reinforce specialized intervention units",
        cut_option="Line-item FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Police>DSU",
        notes="tick794",
    ),
    C(
        commitment_id="cmt_dual_ibz_security_tick794",
        title="Dual IBZ Plan GV 71.3m vs prior police GV residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/019 dual prior police GV budgets",
        decision_date="2026-08-04",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="71300000",
        cash_by_year='{"plan_gv_m": 71.3, "cameras_m": 25, "provision_class_bn": 0.5, "digital_floor_m": 150, "dsu_floor_m": 30}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map IBZ residual dual prior police stacks",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>IBZ_security",
        notes="tick794",
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
        "lb_ibz_security_return_provision_0_5bn",
        "Security+return provision ~0.5bn opaque L5",
        "transfer",
        "Federal>IBZ>security_return_provision",
        "100000000",
        "500000000",
        "Strong primary nearly half-bn provision; exact envelope and cash-by-year FOI residual",
        "strong",
        SRC_MAIN,
        "GPI governors crisis centre return",
        "6.5",
        "9.0",
        "3.5",
        "7.40",
        "Publish exact provision table FOI",
        "tick794",
        goal="Security and return capacity provision",
    ),
    lb(
        "lb_plan_grote_steden_71_3m",
        "Plan Grote Steden package 71.3m 2025-2029",
        "ops",
        "Federal>IBZ>PlanGroteSteden",
        "14260000",
        "71300000",
        "Strong primary 71.3/71m; L5 lines partial (liaison campaigns detection FGP equipment PPE judicial cameras)",
        "strong",
        SRC_MAIN,
        "cities and police zones",
        "5.5",
        "7.5",
        "3.0",
        "6.25",
        "Full L5 measure cash calendar FOI",
        "tick794",
        goal="Urban whole-of-government security plan",
    ),
    lb(
        "lb_cameras_anpr_25m",
        "Cameras+ANPR extra 25m paid to zones",
        "ops",
        "Federal>IBZ>cameras_ANPR",
        "25000000",
        "25000000",
        "Strong primary paid: BRU/ANT 7.5 each + 5 cities 1m + other zones 5m; unit cost residual",
        "strong",
        SRC_MAIN,
        "police zones",
        "5.0",
        "6.5",
        "2.0",
        "5.40",
        "Camera counts and unit cost FOI",
        "tick794",
        goal="Camera and ANPR modernization",
    ),
    lb(
        "lb_police_digital_material_150m",
        "Police material+digital >150m legislature",
        "ops",
        "Federal>Police>material_digital",
        "30000000",
        "150000000",
        "Strong primary floor >150m; dual iPolice failure residual digital strategy Unknown cash",
        "strong",
        SRC_MAIN,
        "federal and local police",
        "6.0",
        "8.0",
        "3.5",
        "6.80",
        "Cash-by-year after iPolice FOI",
        "tick794",
        goal="Police equipment and digital modernization",
    ),
    lb(
        "lb_dsu_renfort_30m",
        "DSU specialized renfort >30m",
        "ops",
        "Federal>Police>DSU",
        "6000000",
        "30000000",
        "Strong primary floor >30m; line items residual FOI",
        "strong",
        SRC_MAIN,
        "DSU units",
        "4.5",
        "6.5",
        "2.5",
        "5.25",
        "Line-item FOI",
        "tick794",
        goal="Specialized intervention capacity",
    ),
    lb(
        "lb_plan_gv_equipment_11m",
        "Plan GV specialized equipment 11m",
        "ops",
        "Federal>IBZ>PlanGV>equipment",
        "2200000",
        "11000000",
        "Strong primary line within 71m package",
        "strong",
        SRC_MAIN,
        "police specialized units",
        "5.0",
        "6.0",
        "2.0",
        "5.10",
        "Procurement list FOI",
        "tick794",
        goal="Specialized materials acquisition",
    ),
    lb(
        "lb_dual_ibz_security_2026",
        "Dual IBZ Plan GV vs prior police GV residual",
        "ops",
        "Belgium>dual>IBZ_security",
        "0",
        "71300000",
        "Strong dual not TE-additive; 71.3m dual prior 43.6m GV path + 0.5bn provision class",
        "strong",
        SRC_DUAL,
        "multi-level security",
        "5.5",
        "8.0",
        "3.5",
        "6.45",
        "Cross-entity cash FOI",
        "tick794",
        goal="Dual security residual map",
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
    "hierarchy_path": "Federal>IBZ>PlanGroteSteden_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual IBZ security: exact EUR for provision Versterking veiligheidsdiensten en "
        "terugkeerbeleid (nearly 0.5bn) cash-by-year 2025-29 and split GPI/governors/NCCN/return; "
        "Plan Grote Steden 71.3m full measure matrix reconciling 71m package lines (liaison 4.3 "
        "campaigns 1.8 detection~9 FGP 4.8 equipment 11 PPE 4.9 judicial 8 cameras 25) with annual "
        "cash; police material+digital >150m and DSU >30m line items; camera 25m zone-level counts "
        "and unit costs after payment; ANPR platform cost dual iPolice residual; FANC structural "
        "dotation design 2026; RvS 2026 budget correction amount"
    ),
    "why_it_matters": (
        "Primary Kamer confirms multi-hundred-m security stack with partial L5; provision near 0.5bn "
        "and Plan GV dual prior police GV opacity blocks honest waste ranking"
    ),
    "priority": "9",
    "recipient_body": "FOD Binnenlandse Zaken / Federale Politie / Nationaal Crisiscentrum FOI",
    "recipient_email": "",
    "recipient_postal": "https://www.ibz.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_ibz_security_return_provision_0_5bn|cmt_plan_grote_steden_71_3m|cmt_cameras_anpr_25m|"
        "cmt_police_digital_material_150m|cmt_dsu_renfort_30m|cmt_dual_ibz_security_tick794"
    ),
    "linked_leaderboard_id": (
        "lb_ibz_security_return_provision_0_5bn|lb_plan_grote_steden_71_3m|lb_cameras_anpr_25m|"
        "lb_police_digital_material_150m|lb_dsu_renfort_30m|lb_dual_ibz_security_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick794 Kamer 1282/019 primary; human send only",
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
            "tick794 IBZ 1282/019 provision~0.5bn PlanGV 71.3 cameras 25 digital>150 DSU>30 "
            "FOI gap_ibz_plan_grote_steden_l5"
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
                "Next residual: dual L5 or unmined primary (Energie 041, Buitenland 006, Digitalisering "
                "030, KMO 024, local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick794 after IBZ019",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} IBZ019 provision~0.5bn PlanGV71.3 cameras25 digital>150 FOI; "
    f"next {NEXT_RQ} Energie041/Buitenland006 residual; progress@800 in 6; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/019 Beleidsnota Veiligheid en Binnenlandse Zaken**, 44p)
- Found (primary 56K1282019):
  - Provisie **Versterking veiligheidsdiensten en terugkeerbeleid ~€0.5bn** (bijna een half miljard)
  - Police material+digital **>€150m** over legislature; **DSU renfort >€30m**
  - **Plan Grote Steden €71.3m** (package €71m 2025–2029): liaison €4.3m · campaigns €1.8m · detection ~€9m · FGP €4.8m · equipment €11m · PPE €4.9m · judicial tools €8m · cameras mass
  - Cameras+ANPR **€25m paid** to zones: BRU **€7.5m** · ANT **€7.5m** · 5 cities **€1m** each · other zones **€5m**
  - ANPR 5 000→platform cap 10 000; SNCB **8 000** cameras access; iPolice failure residual; FANC structural dot prep 2026
- Wrote: budgets +19; commitments +6; leaderboard +7; sources +2; FOI **{GAP}** prio9 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual Energie041/Buitenland006; deferred **rq_116**; progress@800 in 6
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
