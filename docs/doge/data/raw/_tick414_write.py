# tick 414: NBB/NAI COFOG 2024 full function map
import csv
from pathlib import Path

UTC = "2026-08-01T21:45:00Z"
TICK = 414
UNIT = "rq_405"
SRC = "src_nbb_cofog_2024_dec2025"
ROOT = Path(__file__).resolve().parents[3]  # AIpolitics
# raw is docs/doge/data/raw -> parents[0]=raw, [1]=data, [2]=doge, [3]=docs — wrong
# Fix: repo root is parents[4] if file is docs/doge/data/raw/_tick414_write.py
ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"


def load(path):
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
    return rows, fields


def save(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# --- sources ---
sp = DATA / "sources.csv"
srows, sfields = load(sp)
if not any(r.get("source_id") == SRC for r in srows):
    srows.append(
        {
            "source_id": SRC,
            "title": "NBB/NAI COFOG government spending by function 2024 press release 17 Dec 2025",
            "url": "https://www.nbb.be/doc/dq/e/dq3/necf.pdf",
            "publisher": "National Bank of Belgium / National Accounts Institute",
            "accessed_date": "2026-08-01",
            "source_class": "nbb",
            "notes": "Table1 absolute EUR m 2004-2024; TE 335288m; defence 7946m 2.4pct; social 126541m 37.7pct; dual NATO cash vs COFOG delivery; local raw nbb_cofog_defence_2025.pdf; tick414",
        }
    )
    save(sp, srows, sfields)
    print("sources +1")
else:
    print("source exists")

cofog = [
    ("bud_cofog_2024_total", "gg_belgium", 335288000000, "COFOG total GG expenditure 335288m 2024 NBB Table1; dual EDP 335100m class"),
    ("bud_cofog_2024_gps", "gg_belgium", 44306000000, "General public services 44306m 13.2pct incl interest"),
    ("bud_cofog_2024_interest", "gg_interest", 14476000000, "Interest expense COFOG 14476m 4.3pct; dual EDP interest 13524m method gap"),
    ("bud_cofog_2024_gps_ex_int", "gg_belgium", 29830000000, "GPS excl interest 29830m 8.9pct"),
    ("bud_cofog_2024_defence", "mod_defensie", 7946000000, "Defence COFOG 7946m 2.4pct TE 2024 highest share 20y; dual NATO ~1.3pct GDP same year delivery lag F-35"),
    ("bud_cofog_2024_order_safety", "gg_belgium", 10648000000, "Public order and safety 10648m 3.2pct"),
    ("bud_cofog_2024_econ", "gg_belgium", 39854000000, "Economic affairs 39854m 11.9pct (labour market road PT)"),
    ("bud_cofog_2024_env", "gg_belgium", 7176000000, "Environmental protection 7176m 2.1pct"),
    ("bud_cofog_2024_housing", "gg_belgium", 2401000000, "Housing and community amenities 2401m 0.7pct"),
    ("bud_cofog_2024_health", "sec_ss", 49580000000, "Health COFOG 49580m 14.8pct; dual PROMES AMI narrower perimeter"),
    ("bud_cofog_2024_culture", "gg_belgium", 7552000000, "Recreation culture religion 7552m 2.3pct"),
    ("bud_cofog_2024_education", "gg_belgium", 39284000000, "Education 39284m 11.7pct"),
    ("bud_cofog_2024_social", "sec_ss", 126541000000, "Social protection 126541m 37.7pct largest COFOG function"),
    ("bud_cofog_2024_sick_dis", "sec_ss", 24255000000, "Sickness and disability 24255m 7.2pct rising share"),
    ("bud_cofog_2024_old_age", "sec_ss", 71792000000, "Old age and survivors 71792m 21.4pct"),
    ("bud_cofog_2024_unemp", "sec_ss", 6575000000, "Unemployment 6575m 2.0pct; share halved in 20y"),
    ("bud_cofog_2024_social_other", "sec_ss", 23919000000, "Other social protection 23919m 7.1pct"),
]

bp = DATA / "budgets.csv"
brows, bfields = load(bp)
existing = {r["budget_id"] for r in brows}
added = 0
for bid, ent, amt, notes in cofog:
    if bid in existing:
        print("skip", bid)
        continue
    row = {k: "" for k in bfields}
    row.update(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": "2024",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "esa",
            "source_id": SRC,
            "confidence": "strong",
            "notes": notes + "; tick414",
        }
    )
    brows.append(row)
    added += 1
save(bp, brows, bfields)
print("budgets +", added)

cp = DATA / "commitments.csv"
crows, cfields = load(cp)
cid = "cmt_cofog_2024_functions"
if not any(r.get("commitment_id") == cid for r in crows):
    row = {k: "" for k in cfields}
    cash = (
        '{"2024":335288000000,"social":126541000000,"health":49580000000,'
        '"gps":44306000000,"econ":39854000000,"edu":39284000000,'
        '"defence":7946000000,"interest":14476000000}'
    )
    row.update(
        {
            "commitment_id": cid,
            "title": "GG COFOG functional expenditure map 2024 full Table1",
            "entity_id": "gg_belgium",
            "beneficiary": "All COFOG function beneficiaries",
            "legal_basis": "ESA2010 COFOG NAI annual",
            "decision_date": "2025-12-17",
            "start_year": "2024",
            "end_year": "2024",
            "total_envelope_eur": "335288000000",
            "cash_by_year": cash,
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.nbb.be/doc/dq/e/dq3/necf.pdf",
            "stated_goal": "Functional classification of GG spend",
            "cut_option": "Spending reviews by COFOG; dual NATO defence path",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "BE>ESA>COFOG_2024",
            "notes": "Strong primary NBB Dec2025; interest COFOG 14.5bn dual EDP 13.5bn; defence 2.4pct TE 20y high; unemployment share halved; tick414",
        }
    )
    crows.append(row)
    save(cp, crows, cfields)
    print("cmt +1")
else:
    print("cmt exists")

lp = DATA / "leaderboard.csv"
lrows, lfields = load(lp)
existing_lb = {r["item_id"] for r in lrows}


def prio(a, c, d):
    return round(0.45 * a + 0.35 * c + 0.20 * d, 2)


lb_items = [
    (
        "lb_cofog_social_126_5bn",
        "Social protection COFOG 126.5bn 37.7pct 2024",
        "federal",
        "ops",
        "BE>COFOG>social_protection",
        126541000000,
        126541000000,
        "Strong NBB Table1: 126541m largest function; pens 71.8 + sick 24.3 + unemp 6.6 + other 23.9",
        "strong",
        SRC,
        "Pensioners sick unemployed families",
        "Social insurance safety net",
        "Share rising vs 2004 35pct",
        3,
        10,
        8,
        "Function map not pure waste; dual CEV social path",
        "seed",
        "tick414 COFOG; dual pens/AMI L5 residual",
    ),
    (
        "lb_cofog_health_49_6bn",
        "Health COFOG 49.6bn 14.8pct 2024",
        "federal",
        "ops",
        "BE>COFOG>health",
        49580000000,
        49580000000,
        "Strong: 49580m; dual PROMES AMI 37.7bn 2025 real narrower perimeter excl regional/local BMF part",
        "strong",
        SRC,
        "Patients providers",
        "Healthcare",
        "Share 14.0-14.8 2004-24",
        3,
        9.5,
        7,
        "Dual AMI L5 art81 FOI",
        "seed",
        "tick414",
    ),
    (
        "lb_cofog_old_age_71_8bn",
        "Old age+survivors COFOG 71.8bn 21.4pct 2024",
        "federal",
        "ops",
        "BE>COFOG>old_age_survivors",
        71792000000,
        71792000000,
        "Strong: 71792m 21.4pct TE; rising from 18.4pct 2004; dual pension reform 13299/13208",
        "strong",
        SRC,
        "Pensioners survivors",
        "Legal pension system",
        "Dominant social line",
        3,
        10,
        8,
        "Dual fiscal reform incidence",
        "seed",
        "tick414",
    ),
    (
        "lb_cofog_sick_dis_24_3bn",
        "Sickness+disability COFOG 24.3bn 7.2pct 2024",
        "federal",
        "ops",
        "BE>COFOG>sickness_disability",
        24255000000,
        24255000000,
        "Strong: 24255m rising 5.0-7.2pct 2004-24; dual invalidite reform FOI",
        "strong",
        SRC,
        "Long-term sick disabled",
        "Income replacement illness",
        "Share rising dual unemp fall",
        5,
        9,
        6,
        "Activation reforms evaluate deadweight",
        "seed",
        "tick414",
    ),
    (
        "lb_cofog_interest_14_5bn",
        "Interest expense COFOG 14.5bn 4.3pct 2024",
        "federal",
        "ops",
        "BE>COFOG>interest",
        14476000000,
        14476000000,
        "Strong: 14476m; share rebound from 3.2pct 2022 trough; dual EDP 13.5bn dual BDA debt path",
        "strong",
        SRC,
        "Bondholders",
        "Service public debt",
        "r and debt stock rising",
        6,
        9,
        7,
        "Primary surplus path; dual Entity I deficit",
        "seed",
        "tick414 dual EDP method",
    ),
    (
        "lb_cofog_defence_7_9bn",
        "Defence COFOG 7.9bn 2.4pct TE 2024",
        "federal",
        "ops",
        "BE>COFOG>defence",
        7946000000,
        7946000000,
        "Strong: 7946m highest share 20y; 1.3pct GDP; dual NATO cash same 1.3pct GDP after F-35 delivery; 2025 COFOG 8.8bn",
        "strong",
        SRC,
        "Defence personnel industry",
        "NATO capability",
        "Delivery lag F-35 closed 2024 COFOG spike",
        4,
        8.5,
        5,
        "Publish cash vs delivery calendar dual LPM FOI",
        "seed",
        "tick414 dual gap_defence_contract_cash",
    ),
    (
        "lb_cofog_econ_39_9bn",
        "Economic affairs COFOG 39.9bn 11.9pct 2024",
        "federal",
        "ops",
        "BE>COFOG>economic_affairs",
        39854000000,
        39854000000,
        "Strong: 39854m labour market roads PT; dual NBB enterprise subsidies 25.1bn subset class",
        "strong",
        SRC,
        "Firms workers transport users",
        "Labour market infra transport",
        "Share down from 13.2pct 2014 peak",
        5,
        9,
        6,
        "Spending review wage subsidies + PSO",
        "seed",
        "tick414",
    ),
    (
        "lb_cofog_edu_39_3bn",
        "Education COFOG 39.3bn 11.7pct 2024",
        "federal",
        "ops",
        "BE>COFOG>education",
        39284000000,
        39284000000,
        "Strong: 39284m stable ~12pct; dual community budgets VL education VAK ~20bn class part",
        "strong",
        SRC,
        "Pupils students teachers",
        "Education provision",
        "Share stable 11.1-11.8",
        2,
        9.5,
        7,
        "Dual community L5 residual",
        "seed",
        "tick414",
    ),
]

lb_added = 0
for it in lb_items:
    if it[0] in existing_lb:
        print("lb skip", it[0])
        continue
    a, c, d = it[13], it[14], it[15]
    row = {k: "" for k in lfields}
    row.update(
        {
            "item_id": it[0],
            "name": it[1],
            "level": it[2],
            "type": it[3],
            "hierarchy_path": it[4],
            "annual_cost_eur": str(it[5]),
            "total_cost_eur": str(it[6]),
            "tco_notes": it[7],
            "confidence": it[8],
            "source_id": it[9],
            "beneficiaries": it[10],
            "stated_goal": it[11],
            "measured_outcome": it[12],
            "absurdity_score": str(a),
            "cost_score": str(c),
            "difficulty": str(d),
            "priority_index": str(prio(a, c, d)),
            "cut_proposal": it[16],
            "status": it[17],
            "struck_reason": "",
            "notes": it[18],
        }
    )
    lrows.append(row)
    lb_added += 1
save(lp, lrows, lfields)
print("lb +", lb_added)

fp = DATA / "foi_queue.csv"
frows, ffields = load(fp)
updated_foi = False
for r in frows:
    if r.get("gap_id") == "gap_defence_contract_cash":
        note = r.get("notes") or ""
        if "tick414" not in note:
            r["notes"] = (
                note
                + " |tick414: COFOG 2024 7.946bn public; residual signed cash+NATO multi-year still FOI"
            ).strip()
            r["updated_utc"] = UTC
            updated_foi = True
if updated_foi:
    save(fp, frows, ffields)
    print("foi defence note updated")
else:
    print("foi no change or already noted")

rp = DATA / "research_queue.csv"
rrows, rfields = load(rp)
for r in rrows:
    if r.get("task_id") == "rq_405":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["notes"] = (
            "tick414: NBB COFOG 2024 full Table1 TE 335.3bn social 126.5 health 49.6 pens 71.8 def 7.9 interest 14.5; spawn rq_406"
        )
        r["blocked_gap_id"] = "gap_defence_contract_cash"
if not any(r.get("task_id") == "rq_406" for r in rrows):
    row = {k: "" for k in rfields}
    row.update(
        {
            "task_id": "rq_406",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": "",
            "notes": "Spawned tick414 after COFOG 2024; rq_116 SWA deferred",
        }
    )
    rrows.append(row)
save(rp, rrows, rfields)
print("rq_405 done, rq_406 open")

lsp = DATA / "loop_state.csv"
ls, lsfields = load(lsp)
ls[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "notes": "Scheduler 60s. Next prio5 rq_406; rq_116 SWA deferred. tick414 NBB COFOG 2024 functions.",
    }
)
save(lsp, ls, lsfields)
print("loop_state ->", TICK)

logp = ROOT / "docs" / "doge" / "loop_log.md"
entry = f"""
### {UTC} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **NBB/NAI COFOG 2024 full function map Table1**)
- Found (strong primary press 17 Dec 2025 + Table1 mEUR):
  - **TE 335.288bn** 2024 (dual EDP 335.1bn class)
  - **Social protection 126.541bn (37.7%)** — old age/survivors **71.792** · sick/dis **24.255** · unemp **6.575** · other **23.919**
  - **Health 49.580bn (14.8%)** · **GPS 44.306** (interest **14.476** 4.3% rebound from 3.2% 2022) · **econ 39.854** · **edu 39.284**
  - **Defence 7.946bn (2.4% TE)** highest share 20y; **1.3% GDP** both NATO cash and COFOG after F-35 delivery spike
  - Order/safety 10.648 · culture 7.552 · env 7.176 · housing 2.401
  - Unemp share **halved in 20y** (5.3%→2.0%); sick/dis **5.0%→7.2%**; pens **18.4%→21.4%**
- Wrote: sources +1; budgets +17; cmt +1; lb +8; raw PDF; FOI gap_defence note; rq_405=done; spawn **rq_406**; ticks={TICK}
- FOI: no new gap (function L1 complete); residual L5 + defence signed cash still ready human send
- Next: prio5 **rq_406**; deferred **rq_116** SWA
"""
with logp.open("a", encoding="utf-8") as f:
    f.write(entry)
print("log appended")
print("DONE tick", TICK)
print("ROOT", ROOT)
