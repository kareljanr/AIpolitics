# tick 792 — rq_783 Kamer DOC 56 1282/038 Beleidsnota Asiel residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T17:00:00Z"
TICK = 792
RQ = "rq_783"
NEXT_RQ = "rq_784"
SRC_MAIN = "src_kamer_beleid_asiel_1282_038_2026"
SRC_DUAL = "src_dual_asiel_fedasil_tick792"
GAP = "gap_asiel_dublin_masterplan_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282038.pdf"
ENT = "fedasil"


def write_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f, fieldnames=fields, lineterminator="\n", extrasaction="ignore"
        )
        w.writeheader()
        w.writerows([{k: (r.get(k) or "") for k in fields} for r in rows])


# --- sources ---
sp = Path("docs/doge/data/sources.csv")
with sp.open(encoding="utf-8", newline="") as f:
    srows = list(csv.DictReader(f))
    sfields = list(srows[0].keys())
if not any(r["source_id"] == SRC_MAIN for r in srows):
    srows.append(
        {
            "source_id": SRC_MAIN,
            "title": "Kamer DOC 56 1282/038 Beleidsnota Asiel residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Asiel en Migratie",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick792 primary 26p policy note (22 Jan 2026) almost no euro lines. "
                "Ops commitments: Fedasil theoretical reception phase-out (hotels first then LOI); "
                "2nd Dublin centre 2026 (after Zaventem); Fast Track pilot centre 2026; new "
                "registration/aanmeldcentrum dossier to Ministerraad before summer 2026; food-only "
                "cards replace meal cheques early 2026; recognized-refugee transition stay max 2m; "
                "contribution duty for working asylum seekers (enforcement investment); Fedasil "
                "budget-framework exercise continues 2026 with spending review + Inspectie van "
                "Financiën recommendations; Federal Police +72 escort officers by end-2026; DVZ "
                "escorts by end-2026/early-2027; Frontex escort ramp 2026; Masterplan closed "
                "centres: Merksplas extra wing 2025; Steenokkerzeel departure-centre first stone; "
                "Jabbeke works start 2026; family reunification income +10pct per extra person; "
                "partner age 21; unconditional period 12->6 months; Dublin capacity strengthen "
                "end-2026; ODA/return conditionality WOG; EU Pact implement by 12 Jun 2026. "
                "raw 56K1282038.pdf + _tmp_tick792_asiel_full.txt"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual Asiel 038 ops residual vs Fedasil package 802.2m tick792",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: 038 has almost zero euro lines; dual prior Fedasil "
                "package 802.2m 2026 (dot 702.2 + provision 100) + admin chain DVZ/CGVS/RVV ~244m "
                "+ closed-centre Masterplan opex/capex Unknown; hotel/LOI phase-out and Dublin2/"
                "FastTrack/registration centre L5 cash residual FOI; +72 police escorts cost Unknown"
            ),
        }
    )
write_csv(sp, sfields, srows)

# --- budgets ---
bp = Path("docs/doge/data/budgets.csv")
with bp.open(encoding="utf-8", newline="") as f:
    brows = list(csv.DictReader(f))
    bfields = list(brows[0].keys())


def B(**kw):
    return {k: kw.get(k, "") for k in bfields}


new_b = [
    B(
        budget_id="bud_asiel_038_policy_note_anchor_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="0",
        basis="parliamentary",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Primary 1282/038: almost no euro lines; anchor for residual ops FOI; dual Fedasil "
            "package 802.2m prior; tick792"
        ),
    ),
    B(
        budget_id="bud_dual_asiel_fedasil_package_802_2m_2026",
        entity_id=ENT,
        year="2026",
        amount_eur="802200000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual map: prior Fedasil package 802.2m 2026 (dot 702.2 + prov 100) residual vs "
            "038 phase-out/Dublin2/FastTrack/Masterplan L5; not TE-additive double-count; tick792"
        ),
    ),
    B(
        budget_id="bud_fedasil_dot_702_2m_dual_038",
        entity_id=ENT,
        year="2026",
        amount_eur="702200000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior Fedasil initial dotation 702.2m 2026 class for 038 residual map; "
            "not new appropriation; tick792"
        ),
    ),
    B(
        budget_id="bud_police_escorts_plus_72_fte_2026",
        entity_id="police_federale",
        year="2026",
        amount_eur="",
        amount_min_eur="",
        amount_max_eur="",
        basis="policy_fte",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Federal Police escort reinforcement +72 officers by end-2026 (Beleidsnota 038); "
            "cash/salary path Unknown FOI; tick792"
        ),
    ),
    B(
        budget_id="bud_dublin2_centre_2026_unknown",
        entity_id=ENT,
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Second Dublin centre opening targeted 2026 (after Zaventem); capex/opex Unknown; tick792"
        ),
    ),
    B(
        budget_id="bud_fast_track_centre_pilot_2026_unknown",
        entity_id=ENT,
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Fast Track asylum pilot centre 2026 for low protection-chance cases; cost Unknown; tick792"
        ),
    ),
    B(
        budget_id="bud_aanmeldcentrum_dossier_2026_unknown",
        entity_id="dvz",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Renewed registration/aanmeldcentrum dossier to Ministerraad before summer 2026; "
            "budget Unknown; tick792"
        ),
    ),
    B(
        budget_id="bud_masterplan_closed_jabbeke_start_2026_unknown",
        entity_id="dvz",
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Masterplan closed centres: Jabbeke works start 2026; Merksplas extra wing 2025; "
            "Steenokkerzeel departure centre first stone; multi-year capex Unknown; tick792"
        ),
    ),
    B(
        budget_id="bud_asiel_food_card_rollout_2026_unknown",
        entity_id=ENT,
        year="2026",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "Meal cheques -> food-only cards early 2026 (voluntary exit or self-cook centres); "
            "programme cost Unknown; tick792"
        ),
    ),
    B(
        budget_id="bud_dual_asiel_admin_chain_244m_class",
        entity_id="gg_belgium",
        year="2025",
        amount_eur="243881000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior admin chain DVZ+CGVS+RVV ~243.9m 2025 class vs 038 Dublin/CGVS reinforce; "
            "not TE-additive; tick792"
        ),
    ),
]
exist_b = {r["budget_id"] for r in brows}
for nb in new_b:
    if nb["budget_id"] not in exist_b:
        brows.append(nb)
write_csv(bp, bfields, brows)

# --- commitments ---
cp = Path("docs/doge/data/commitments.csv")
with cp.open(encoding="utf-8", newline="") as f:
    crows = list(csv.DictReader(f))
    cfields = list(crows[0].keys())


def C(**kw):
    return {k: kw.get(k, "") for k in cfields}


new_c = [
    C(
        commitment_id="cmt_fedasil_phaseout_plan_038",
        title="Fedasil theoretical reception phase-out plan (hotels then LOI)",
        entity_id=ENT,
        beneficiary="reception network / local governments",
        legal_basis="Regeerakkoord + Beleidsnota 1282/038",
        decision_date="2026-01-22",
        start_year="2026",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"order": ["hotels", "LOI", "collective_buffer"], "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Gradual reception network reduction after structural inflow drop",
        cut_option="Publish place counts + cash path FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>Fedasil>phaseout",
        notes="tick792 primary; dual package 802.2m",
    ),
    C(
        commitment_id="cmt_dublin2_centre_2026",
        title="Second Dublin centre opening 2026",
        entity_id=ENT,
        beneficiary="Dublin transfer applicants",
        legal_basis="Beleidsnota 1282/038; EU Dublin framework",
        decision_date="2026-01-22",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"site": "second_after_Zaventem", "year": 2026, "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Relieve regular reception; accelerate Dublin returns",
        cut_option="Capex opex FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>Dublin2",
        notes="tick792",
    ),
    C(
        commitment_id="cmt_fast_track_pilot_2026",
        title="Fast Track asylum pilot centre 2026",
        entity_id=ENT,
        beneficiary="low protection-chance / safe-country applicants",
        legal_basis="Beleidsnota 1282/038; EU Pact",
        decision_date="2026-01-22",
        start_year="2026",
        end_year="2027",
        total_envelope_eur="",
        cash_by_year='{"pilot": 2026, "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Short procedure + return focus for low protection chance",
        cut_option="Pilot budget FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>FastTrack",
        notes="tick792",
    ),
    C(
        commitment_id="cmt_aanmeldcentrum_mr_2026",
        title="Renewed registration centre dossier before summer 2026",
        entity_id="dvz",
        beneficiary="asylum chain services",
        legal_basis="Beleidsnota 1282/038",
        decision_date="2026-01-22",
        start_year="2026",
        end_year="2028",
        total_envelope_eur="",
        cash_by_year='{"dossier_to_MR": "before_summer_2026", "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Integrated registration centre / chain collaboration",
        cut_option="MR dossier cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>Aanmeldcentrum",
        notes="tick792",
    ),
    C(
        commitment_id="cmt_police_escorts_plus_72_2026",
        title="Federal Police +72 escort officers by end-2026",
        entity_id="police_federale",
        beneficiary="forced return operations",
        legal_basis="Beleidsnota 1282/038 + IBZ escort action plan",
        decision_date="2026-01-22",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"fte_plus": 72, "deadline": "2026-12", "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Accelerate forced return of non-cooperative irregular stays",
        cut_option="Payroll/unit cost FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>Escorts>Police",
        notes="tick792; also DVZ escorts + Frontex ramp 2026",
    ),
    C(
        commitment_id="cmt_masterplan_closed_centres_038",
        title="Masterplan closed centres Merksplas/Steenokkerzeel/Jabbeke residual",
        entity_id="dvz",
        beneficiary="detention/return capacity",
        legal_basis="Masterplan Gesloten Centra + Beleidsnota 1282/038",
        decision_date="2026-01-22",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="",
        cash_by_year='{"merksplas_wing": 2025, "steenokkerzeel_first_stone": true, "jabbeke_start": 2026, "euro": "Unknown"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Expand closed-centre capacity for more returns",
        cut_option="Multi-year capex FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>ClosedCentres>Masterplan",
        notes="tick792",
    ),
    C(
        commitment_id="cmt_fedasil_budget_framework_2026",
        title="Fedasil better budget framework exercise 2026 (SR+IF)",
        entity_id=ENT,
        beneficiary="reception network financing",
        legal_basis="Beleidsnota 1282/038; spending review + Inspectie van Financiën",
        decision_date="2026-01-22",
        start_year="2025",
        end_year="2026",
        total_envelope_eur="",
        cash_by_year='{"exercise": "continues_2026", "inputs": ["spending_review", "IF"]}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Financing mechanism adapted to asylum inflow fluctuations",
        cut_option="Publish SR/IF recommendations + amounts FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>Asiel>Fedasil>budget_framework",
        notes="tick792",
    ),
    C(
        commitment_id="cmt_dual_asiel_fedasil_tick792",
        title="Dual Asiel 038 residual vs Fedasil 802.2m package",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/038 dual prior Fedasil/IBZ budgets",
        decision_date="2026-08-04",
        start_year="2026",
        end_year="2026",
        total_envelope_eur="802200000",
        cash_by_year='{"fedasil_package_m": 802.2, "admin_chain_m": 243.9, "escorts_fte": 72, "note": "not TE-additive"}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map policy residual dual to known Fedasil euro stacks",
        cut_option="L5 FOI Dublin/Masterplan/escorts",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>Asiel",
        notes="tick792",
    ),
]
exist_c = {r["commitment_id"] for r in crows}
for nc in new_c:
    if nc["commitment_id"] not in exist_c:
        crows.append(nc)
write_csv(cp, cfields, crows)

# --- leaderboard ---
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
        "lb_asiel_038_euro_opaque",
        "Asiel beleidsnota 038 almost euro-opaque residual",
        "ops",
        "Federal>Asiel>Beleidsnota038",
        "0",
        "0",
        "Strong primary: 26p note confirms multi-programme residual without euro tables; dual Fedasil 802.2m",
        "strong",
        SRC_MAIN,
        "asylum chain",
        "7.0",
        "8.0",
        "2.5",
        "7.15",
        "Force budget annex FOI Dublin/Masterplan/escorts",
        "tick792",
        goal="Transparent cash behind asylum policy residual",
    ),
    lb(
        "lb_dual_asiel_fedasil_802m_2026",
        "Dual Asiel 038 vs Fedasil package 802.2m 2026",
        "ops",
        "Belgium>dual>Asiel_Fedasil",
        "802200000",
        "802200000",
        "Strong dual not TE-additive; prior package dual policy residual phase-out/Dublin/FastTrack",
        "strong",
        SRC_DUAL,
        "multi-level asylum",
        "5.5",
        "9.0",
        "3.5",
        "7.00",
        "Cross-entity L5 cash FOI",
        "tick792",
        goal="Dual map reception stack",
    ),
    lb(
        "lb_dublin2_centre_2026",
        "Second Dublin centre 2026 cost Unknown",
        "ops",
        "Federal>Asiel>Dublin2",
        "0",
        "0",
        "Strong primary commitment; capex/opex Unknown FOI residual",
        "strong",
        SRC_MAIN,
        "Dublin applicants",
        "6.0",
        "6.5",
        "2.5",
        "5.90",
        "Publish site budget FOI",
        "tick792",
        goal="Second Dublin centre",
    ),
    lb(
        "lb_fast_track_pilot_2026",
        "Fast Track asylum pilot centre 2026 cost Unknown",
        "ops",
        "Federal>Asiel>FastTrack",
        "0",
        "0",
        "Strong primary pilot; cost/KPI residual FOI",
        "strong",
        SRC_MAIN,
        "low protection-chance applicants",
        "5.5",
        "6.0",
        "2.5",
        "5.45",
        "Pilot envelope FOI",
        "tick792",
        goal="Accelerated procedure pilot",
    ),
    lb(
        "lb_police_escorts_plus_72",
        "Federal Police +72 escorts end-2026 cash Unknown",
        "ops",
        "Federal>Asiel>Escorts>Police",
        "0",
        "0",
        "Strong primary FTE +72; payroll/unit cost Unknown; dual DVZ+Frontex escort ramp",
        "strong",
        SRC_MAIN,
        "forced return ops",
        "5.0",
        "5.5",
        "2.0",
        "4.90",
        "Payroll FOI",
        "tick792",
        goal="Forced return escort capacity",
    ),
    lb(
        "lb_masterplan_closed_038",
        "Masterplan closed centres Merksplas/Steenokkerzeel/Jabbeke residual",
        "ops",
        "Federal>Asiel>ClosedCentres>Masterplan",
        "0",
        "0",
        "Strong primary milestones; multi-year capex Unknown FOI residual",
        "strong",
        SRC_MAIN,
        "detention return capacity",
        "6.5",
        "7.5",
        "3.0",
        "6.50",
        "Capex calendar FOI",
        "tick792",
        goal="Closed-centre capacity expansion",
    ),
    lb(
        "lb_fedasil_budget_framework_2026",
        "Fedasil budget-framework exercise 2026 (SR+IF) opaque",
        "ops",
        "Federal>Asiel>Fedasil>budget_framework",
        "0",
        "0",
        "Strong primary: SR and IF recommendations to reshape financing; amounts Unknown",
        "strong",
        SRC_MAIN,
        "Fedasil network",
        "6.0",
        "7.0",
        "2.5",
        "6.05",
        "Publish SR/IF reports FOI",
        "tick792",
        goal="Adaptive financing mechanism",
    ),
]
exist_l = {r["item_id"] for r in lrows}
for nl in new_l:
    if nl["item_id"] not in exist_l:
        lrows.append(nl)
write_csv(lp, lfields, lrows)

# --- FOI queue ---
fp = Path("docs/doge/data/foi_queue.csv")
with fp.open(encoding="utf-8", newline="") as f:
    frows = list(csv.DictReader(f))
    ffields = list(frows[0].keys())

foi_row = {
    "gap_id": GAP,
    "hierarchy_path": "Federal>Asiel>Dublin_Masterplan_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 cash behind 038 residual: 2nd Dublin centre site/capex/opex 2026-29; Fast Track pilot "
        "budget and KPIs; aanmeldcentrum MR dossier envelope; Masterplan closed centres cash-by-year "
        "Merksplas wing + Steenokkerzeel departure + Jabbeke works; +72 Federal Police escorts "
        "payroll path + DVZ escort training KB cost + Frontex ramp; food-card programme cost vs "
        "meal cheques; contribution duty cash recovered 2024-26; Fedasil budget-framework study + "
        "spending review + IF recommendations and amounts; hotel/LOI phase-out place counts and "
        "unit cost trajectory dual prior 702.2/802.2m package"
    ),
    "why_it_matters": (
        "Primary Kamer Asiel note is euro-opaque while dual Fedasil package ~802m and closed-centre "
        "Masterplan are material; residual L5 prevents honest waste ranking of reception/return stack"
    ),
    "priority": "9",
    "recipient_body": "Fedasil / DVZ / FOD Binnenlandse Zaken / Federale Politie FOI",
    "recipient_email": "",
    "recipient_postal": "https://www.fedasil.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_dublin2_centre_2026|cmt_fast_track_pilot_2026|cmt_masterplan_closed_centres_038|"
        "cmt_police_escorts_plus_72_2026|cmt_fedasil_budget_framework_2026|cmt_dual_asiel_fedasil_tick792"
    ),
    "linked_leaderboard_id": (
        "lb_asiel_038_euro_opaque|lb_dublin2_centre_2026|lb_fast_track_pilot_2026|"
        "lb_masterplan_closed_038|lb_police_escorts_plus_72|lb_dual_asiel_fedasil_802m_2026"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick792 Kamer 1282/038 primary; human send only",
}
if not any(r["gap_id"] == GAP for r in frows):
    frows.append(foi_row)
else:
    frows = [foi_row if r["gap_id"] == GAP else r for r in frows]
write_csv(fp, ffields, frows)

# --- research queue ---
rq_path = Path("docs/doge/data/research_queue.csv")
with rq_path.open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys())

for r in rq_rows:
    if r.get("task_id") == RQ:
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick792 Asiel 1282/038 euro-opaque; dual Fedasil 802.2m; Dublin2/FastTrack/Masterplan/"
            "escorts+72 FOI gap_asiel_dublin_masterplan_l5 ready"
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
                "Next residual: dual L5 or unmined primary (local/CoA, other 1282/* not yet mined, "
                "or FOI-adjacent programme residual); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick792 after Asiel038",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

# --- loop_state ---
ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} Asiel038 euro-opaque dual Fedasil802.2m Dublin2/Masterplan FOI; "
    f"next {NEXT_RQ} local/CoA residual; progress@800 in 8; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

# --- loop_log append ---
log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/038 Beleidsnota Asiel**, 26p)
- Found (primary 56K1282038):
  - **Almost no euro lines** in policy note (strong opacity residual)
  - Fedasil theoretical **phase-out**: hotels first, then LOI/local; buffer places retained
  - **2nd Dublin centre** 2026 (after Zaventem); **Fast Track** pilot centre 2026
  - New **aanmeldcentrum** dossier to Ministerraad before summer 2026
  - Meal cheques → **food-only cards** early 2026; contribution duty enforcement for working asylum seekers
  - Fedasil **budget-framework** exercise continues 2026 (spending review + IF recommendations)
  - Federal Police escorts **+72** by end-2026; DVZ escorts end-2026/early-2027; Frontex ramp 2026
  - Masterplan closed centres: Merksplas wing 2025; Steenokkerzeel first stone; **Jabbeke works 2026**
  - Dual prior Fedasil package **€802.2m** 2026 (dot 702.2 + prov 100) + admin chain ~€244m class
- Wrote: budgets +10; commitments +8; leaderboard +7; sources +2; FOI **{GAP}** prio9 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual local/CoA; deferred **rq_116**; progress@800 in 8
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
