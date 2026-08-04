# tick 795 — rq_786 Kamer DOC 56 1282/006 Beleidsnota Buitenlandse Zaken / ODA residual
import csv
from pathlib import Path

csv.field_size_limit(10_000_000)

UTC = "2026-08-04T18:30:00Z"
TICK = 795
RQ = "rq_786"
NEXT_RQ = "rq_787"
SRC_MAIN = "src_kamer_beleid_bz_1282_006_2026"
SRC_DUAL = "src_dual_bz_oda_tick795"
GAP = "gap_bz_refi_oda25_l5"
PDF_URL = "https://www.dekamer.be/FLWB/PDF/56/1282/56K1282006.pdf"
ENT = "fod_bz"


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
            "title": "Kamer DOC 56 1282/006 Beleidsnota Buitenlandse Zaken ODA residual 2026",
            "url": PDF_URL,
            "publisher": "Kamer / Minister Buitenlandse Zaken Europese Zaken Ontwikkelingssamenwerking",
            "accessed_date": "2026-08-04",
            "source_class": "parliamentary",
            "notes": (
                "Strong tick795 primary 44p thin euro lines: FOD BZ security-department status "
                "exempt linear budget efforts (except operating costs) and/or non-replacement of staff; "
                "complementary refinancing 35m EUR over legislature especially to reinforce posts; "
                "ODA/cooperation budget -25pct savings path decisions presented Kamer May 2025 "
                "implementation continues 2026+ possible legal-frame review partner-country approach; "
                "EU MFF 2028-2034 Commission proposal cited 1.985 trillion-class EUR (1.26pct GNI) "
                "BZ leads BE negotiation with BOSA (EU-level not BE TE); 3D diplomacy-defence-development; "
                "raw 56K1282006.pdf"
            ),
        }
    )
if not any(r["source_id"] == SRC_DUAL for r in srows):
    srows.append(
        {
            "source_id": SRC_DUAL,
            "title": "Dual BZ 35m refi + ODA -25pct vs DGD 1.118bn residual tick795",
            "url": PDF_URL,
            "publisher": "DOGE synthesis",
            "accessed_date": "2026-08-04",
            "source_class": "synthesis",
            "notes": (
                "Strong dual not TE-additive: primary 35m legislature refi dual DGD channel 1117.97m "
                "2025 and progressive -25pct path (prior cut -106m 2025); ODA decisions May 2025 "
                "channel matrix residual FOI; EU MFF 1.985tn class dual not BE TE"
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
        budget_id="bud_bz_refi_posts_35m_legislature",
        entity_id=ENT,
        year="2029",
        amount_eur="35000000",
        basis="budgeted",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "FOD BZ complementary refinancing 35m EUR over legislature (o.a. reinforce posts); "
            "security-department exemption from linear cuts except operating costs; tick795 1282/006"
        ),
    ),
    B(
        budget_id="bud_bz_refi_posts_annual_class_7m",
        entity_id=ENT,
        year="2026",
        amount_eur="7000000",
        basis="derived",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "Illustrative annual class 35m/5yr legislature ~7m/yr if flat; cash-by-year FOI residual; tick795"
        ),
    ),
    B(
        budget_id="bud_oda_cut_path_minus_25pct_class",
        entity_id="dgd",
        year="2027",
        amount_eur="",
        basis="policy",
        source_id=SRC_MAIN,
        confidence="strong",
        notes=(
            "ODA/cooperation budget -25pct savings path (decisions Kamer May 2025); implementation "
            "continues 2026+; absolute multi-year EUR residual dual prior -106m 2025; tick795"
        ),
    ),
    B(
        budget_id="bud_dual_oda_dgd_2025_1118m_class",
        entity_id="dgd",
        year="2025",
        amount_eur="1117970000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior DGD total 1117.97m 2025 residual vs 006 -25pct path; not new appropriation; tick795"
        ),
    ),
    B(
        budget_id="bud_dual_oda_cut_2025_minus_106m",
        entity_id="dgd",
        year="2025",
        amount_eur="-106000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual prior first-year ODA cut -106m 2025 on progressive -25pct path to 2027; tick795"
        ),
    ),
    B(
        budget_id="bud_eu_mff_2028_2034_proposal_1985bn_class",
        entity_id="gg_belgium",
        year="2034",
        amount_eur="1985000000000",
        basis="parliamentary",
        source_id=SRC_MAIN,
        confidence="medium",
        notes=(
            "EU MFF 2028-2034 Commission proposal cited in 1282/006 as 1.985 milliard/mrd-scale "
            "(1.26pct GNI); interpreted as 1.985 trillion EUR EU-level package (BE share Unknown); "
            "not BE TE; tick795"
        ),
    ),
    B(
        budget_id="bud_dual_bz_oda_map_2026",
        entity_id="gg_belgium",
        year="2026",
        amount_eur="35000000",
        basis="synthesis",
        source_id=SRC_DUAL,
        confidence="strong",
        notes=(
            "Dual map anchor BZ 35m refi residual vs DGD 1.118bn and -25pct ODA path; not TE-additive; tick795"
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
        commitment_id="cmt_bz_refi_35m_legislature",
        title="FOD BZ complementary refinancing 35m legislature (posts)",
        entity_id=ENT,
        beneficiary="diplomatic network / security diplomacy",
        legal_basis="Beleidsnota 1282/006; security-department budget status",
        decision_date="2026-01-23",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="35000000",
        cash_by_year='{"total_m": 35, "period": "legislature", "purpose": "reinforce_posts", "linear_exempt": true, "ops_exception": true}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Reinforce posts and security diplomacy capacity",
        cut_option="Cash-by-year and post list FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>BZ>refi_posts",
        notes="tick795",
    ),
    C(
        commitment_id="cmt_oda_cut_minus_25pct_path",
        title="ODA / development cooperation budget -25pct path",
        entity_id="dgd",
        beneficiary="partner countries / multilateral / civil society channels",
        legal_basis="Budget savings path; decisions presented Kamer May 2025; Beleidsnota 1282/006",
        decision_date="2025-05-01",
        start_year="2025",
        end_year="2027",
        total_envelope_eur="",
        cash_by_year='{"cut_pct": -25, "kamer_presentation": "2025-05", "implementation": "2026+", "legal_frame_review": "possible"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Predictable multi-year financing after large ODA cuts",
        cut_option="Channel matrix + multi-year cash FOI",
        source_id=SRC_MAIN,
        confidence="strong",
        hierarchy_path="Federal>ODA>cut_path",
        notes="tick795 dual prior -106m 2025",
    ),
    C(
        commitment_id="cmt_eu_mff_2028_2034_be_negotiation",
        title="EU MFF 2028-2034 negotiation (Commission proposal ~1.985tn class)",
        entity_id=ENT,
        beneficiary="EU budget / BE contribution residual",
        legal_basis="Commission MFF proposal Jul 2025; Beleidsnota 1282/006",
        decision_date="2025-07-01",
        start_year="2028",
        end_year="2034",
        total_envelope_eur="1985000000000",
        cash_by_year='{"eu_total_class": 1985000000000, "gni_pct": 1.26, "be_share": "Unknown", "target_agreement": "2026-12"}',
        remaining_eur="",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="BE negotiation lead with BOSA on modern flexible MFF",
        cut_option="BE net contribution path FOI",
        source_id=SRC_MAIN,
        confidence="medium",
        hierarchy_path="EU>MFF>2028_2034",
        notes="tick795 EU-level not BE TE",
    ),
    C(
        commitment_id="cmt_dual_bz_oda_tick795",
        title="Dual BZ 35m refi vs DGD ODA -25pct residual",
        entity_id="gg_belgium",
        beneficiary="dual map",
        legal_basis="Beleidsnota 1282/006 dual prior DGD AR",
        decision_date="2026-08-04",
        start_year="2025",
        end_year="2029",
        total_envelope_eur="35000000",
        cash_by_year='{"bz_refi_m": 35, "dgd_2025_m": 1117.97, "oda_cut_2025_m": -106, "oda_cut_pct": -25}',
        remaining_eur="0",
        status="active",
        evaluation_url=PDF_URL,
        stated_goal="Map BZ residual dual ODA stack",
        cut_option="L5 FOI",
        source_id=SRC_DUAL,
        confidence="strong",
        hierarchy_path="Belgium>dual>BZ_ODA",
        notes="tick795",
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
        "lb_bz_refi_35m_legislature",
        "FOD BZ refinancing 35m legislature (posts)",
        "ops",
        "Federal>BZ>refi_posts",
        "7000000",
        "35000000",
        "Strong primary 35m complementary refi; exempt linear cuts except ops; cash-by-year FOI",
        "strong",
        SRC_MAIN,
        "diplomatic posts network",
        "4.5",
        "6.0",
        "2.0",
        "4.90",
        "Post list + annual cash FOI",
        "tick795",
        goal="Reinforce security diplomacy posts",
    ),
    lb(
        "lb_oda_cut_minus_25pct_path",
        "ODA budget -25pct path residual L5",
        "transfer",
        "Federal>ODA>cut_path",
        "0",
        "0",
        "Strong primary -25pct; dual prior -106m 2025 and DGD 1.118bn; channel matrix residual FOI",
        "strong",
        SRC_MAIN,
        "development cooperation actors",
        "6.5",
        "8.5",
        "3.0",
        "7.10",
        "Publish May 2025 decision table + multi-year cash FOI",
        "tick795",
        goal="Predictable ODA after large cuts",
    ),
    lb(
        "lb_dual_bz_oda_2026",
        "Dual BZ 35m refi vs DGD ODA stack residual",
        "ops",
        "Belgium>dual>BZ_ODA",
        "0",
        "1117970000",
        "Strong dual not TE-additive; 35m refi dual 1.118bn DGD and -25pct path",
        "strong",
        SRC_DUAL,
        "multi-channel foreign affairs",
        "5.5",
        "8.5",
        "3.5",
        "6.70",
        "Cross-channel L5 FOI",
        "tick795",
        goal="Dual foreign affairs residual map",
    ),
    lb(
        "lb_eu_mff_2028_2034_class",
        "EU MFF 2028-2034 proposal ~1.985tn class (EU-level)",
        "transfer",
        "EU>MFF>2028_2034",
        "0",
        "1985000000000",
        "Medium: primary cites 1.985 mrd-scale at 1.26pct GNI; EU-level not BE TE; BE share Unknown",
        "medium",
        SRC_MAIN,
        "EU member states",
        "3.0",
        "9.5",
        "4.5",
        "5.85",
        "BE net contribution path FOI",
        "tick795",
        goal="EU multi-annual financial framework negotiation",
    ),
    lb(
        "lb_oda_cut_2025_minus_106m_dual",
        "Dual ODA first-year cut -106m 2025 class",
        "transfer",
        "Federal>ODA>cut_2025",
        "-106000000",
        "-106000000",
        "Strong dual prior cut path residual vs 006 -25pct narrative",
        "strong",
        SRC_DUAL,
        "DGD channels",
        "5.0",
        "7.5",
        "2.5",
        "5.85",
        "Channel allocation FOI",
        "tick795",
        goal="First-year ODA cut delivery",
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
    "hierarchy_path": "Federal>BZ>refi_ODA_L5",
    "entity_id": ENT,
    "what_is_missing": (
        "L5 residual BZ/ODA: cash-by-year 2025-2029 behind FOD BZ complementary refinancing "
        "35m (posts reinforced named list); ODA -25pct May 2025 Kamer decision full channel matrix "
        "(governmental Enabel/NGO/multilateral/humanitarian/climate) multi-year EUR vs prior 1117.97m "
        "2025 and -106m first year; possible legal-frame and partner-country list revision documents; "
        "BE net contribution scenarios under EU MFF 2028-2034 proposal (1.985tn class / 1.26pct GNI)"
    ),
    "why_it_matters": (
        "Primary Kamer thin on euros but locks 35m refi exemption and multi-year ODA -25pct; dual "
        "DGD 1bn+ stack needs residual L5 for honest ranking and cut delivery tracking"
    ),
    "priority": "8",
    "recipient_body": "FOD Buitenlandse Zaken / DGD / Enabel FOI",
    "recipient_email": "",
    "recipient_postal": "https://diplomatie.belgium.be",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-04",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": (
        "cmt_bz_refi_35m_legislature|cmt_oda_cut_minus_25pct_path|cmt_eu_mff_2028_2034_be_negotiation|"
        "cmt_dual_bz_oda_tick795"
    ),
    "linked_leaderboard_id": (
        "lb_bz_refi_35m_legislature|lb_oda_cut_minus_25pct_path|lb_dual_bz_oda_2026|"
        "lb_oda_cut_2025_minus_106m_dual"
    ),
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick795 Kamer 1282/006 primary; human send only",
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
            "tick795 BZ 1282/006 refi 35m ODA -25pct dual DGD 1.118bn FOI gap_bz_refi_oda25_l5"
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
                "Next residual: dual L5 or unmined primary (Energie 041, Digitalisering 030, KMO 024, "
                "local/CoA, other 1282/*); prefer FOI-adjacent L5; skip rq_116"
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned tick795 after BZ006",
        }
    )
write_csv(rq_path, rq_fields, rq_rows)

ls = Path("docs/doge/data/loop_state.csv")
notes = (
    f"tick{TICK} BZ006 refi35m ODA-25pct dual DGD1.118bn FOI; "
    f"next {NEXT_RQ} Energie041/Digi030 residual; progress@800 in 5; rq_116 deferred"
)
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{UTC},{RQ},{TICK},no,{notes}\n",
    encoding="utf-8",
)

log = Path("docs/doge/loop_log.md")
entry = f"""
## Tick {TICK} — {UTC}

- Unit: **{RQ}** (FOI-adjacent residual — **Kamer DOC 56 1282/006 Beleidsnota Buitenlandse Zaken / Ontwikkelingssamenwerking**, 44p)
- Found (primary 56K1282006):
  - FOD BZ security-department status: **exempt linear cuts** (except operating costs) + non-replacement exemption
  - Complementary **refinancing €35m** over legislature (o.a. reinforce posts)
  - ODA/cooperation budget **−25%** path; decisions Kamer **May 2025**; implementation **2026+**; possible legal-frame review
  - Dual prior DGD total **€1,117.97m** 2025 and first-year cut **−€106m**
  - EU MFF 2028–2034 Commission proposal **~€1.985tn class** (1.26% GNI); BZ leads BE negotiation with BOSA (EU-level not BE TE)
- Wrote: budgets +7; commitments +4; leaderboard +5; sources +2; FOI **{GAP}** prio8 ready; raw PDF; {RQ}=done; spawn **{NEXT_RQ}**; ticks={TICK}
- FOI: ready only — **do not send**
- Next: prio5 **{NEXT_RQ}** residual Energie041/Digi030; deferred **rq_116**; progress@800 in 5
"""
text = log.read_text(encoding="utf-8")
if f"## Tick {TICK} " not in text:
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")

print(f"tick {TICK} complete: {RQ} -> {NEXT_RQ}; FOI {GAP}")
