# tick394: Military programming law 2026-2034 investments 33.784bn L5 + staff path
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T11:45:00Z"
TICK = 394
UNIT = "rq_385"
GAP = "gap_lpm_contract_cash_2026_34"


def append_rows(path: Path, rows: list[dict]):
    with path.open(encoding="utf-8", newline="") as f:
        fields = csv.DictReader(f).fieldnames
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def rewrite(path: Path, rows: list[dict], fields: list[str]):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_kamer_56k1143_lpm_2026_2034",
            "title": "Kamer 56K1143 loi programmation militaire investissements personnel 2026-2034",
            "url": "https://www.lachambre.be/FLWB/PDF/56/1143/56K1143001.pdf",
            "publisher": "Chambre des representants / Ministere Defense",
            "accessed_date": "2026-08-01",
            "source_class": "primary_budget",
            "notes": "Art.8 eng 33.784bn EUR constant 2026; staff targets 34500 active 12800 reserve 8500 civil 2034; annex II capacity packages; dual NATO 2pct path",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, conf="strong", basis="budgeted"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": "mod_defensie",
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": "src_kamer_56k1143_lpm_2026_2034",
            "confidence": conf,
            "notes": note,
        }
    )


# Total envelope art.8
add(2026, "bud_lpm_invest_total_2026_2034", 33784153531, "LPM art.8 major material investments eng 33784.153531m EUR constants 2026 for 2026-2034")

# Staff targets end-2034
add(2034, "bud_lpm_staff_active_2034", 34500, "Military active cadre target 34500 ETP 2034 (COUNT)", basis="budgeted")
add(2034, "bud_lpm_staff_reserve_2034", 12800, "Military reserve target 12800 incl voluntary military year 2034 (COUNT)")
add(2034, "bud_lpm_staff_civil_2034", 8500, "Civilian staff target 8500 2034 (COUNT)")

# Recruitment annex I
recruits = [
    (2026, 2800, 1050, 960),
    (2027, 3100, 1500, 960),
    (2028, 3100, 1500, 960),
    (2029, 3300, 1500, 960),
    (2030, 3300, 1500, 960),
    (2031, 3500, 1500, 960),
    (2032, 3600, 1500, 960),
    (2033, 3600, 1500, 960),
    (2034, 3600, 1500, 960),
]
for y, act, res, civ in recruits:
    add(y, f"bud_lpm_recruit_active_{y}", act, f"External recruitment active military {act} {y} (COUNT)")
    add(y, f"bud_lpm_recruit_reserve_{y}", res, f"External recruitment reserve {res} {y} (COUNT)")
    add(y, f"bud_lpm_recruit_civil_{y}", civ, f"External recruitment civilian {civ} {y} (COUNT)")

# Major L5 packages annex II (MEUR const 2026) — multi-year envelope attributed to start year 2026 for commitment class
packages = [
    ("ici_intel", 290630000, "ICI Intelligence SIGINT/OSINT 290.63m 2026-34"),
    ("ici_cyber", 489980000, "ICI Cyber capabilities 489.98m 2026-34"),
    ("ici_influence", 10870000, "ICI Influence PsyOps/CIMIC 10.87m"),
    ("ici_space", 616660000, "ICI Space SATCOM/ISR/SSA/PNT 616.66m 2026-34"),
    ("land_c2", 892160000, "Land Motorized C2 vehicles/shelters 892.16m"),
    ("land_manoeuvre", 6003820000, "Land Combat Manoeuvre additional vehicles/drones 6003.82m LARGEST land"),
    ("land_fires", 417900000, "Land Combat Support Fires radars/mortars/MLRS 417.90m"),
    ("land_force_prot", 226740000, "Land CS Force Protection EW/CBRN/VSHORAD 226.74m"),
    ("land_isr", 79700000, "Land CS ISR tactical UAS/sensors 79.70m"),
    ("land_eng", 842040000, "Land CS Military Engineering vehicles/mines 842.04m"),
    ("land_css", 1352640000, "Land CSS trucks/recovery/containers 1352.64m"),
    ("sof_c2", 140250000, "Special Ops C2 radios/AI/AR 140.25m"),
    ("joint_land_support", 1535490000, "Joint General Support Land logistics/infra 1535.49m"),
    ("air_f35_extra11", 3387410000, "Air Combat +11 F-35A package 3387.41m (2026)"),
    ("air_sbamd", 4013990000, "Surface-Based Air Missile Defence 10+3 firing units 4013.99m"),
    ("air_fixed_wing_transport", 1047970000, "Fixed wing transport light/long-range/A400M 1047.97m"),
    ("air_force_prot", 244480000, "Air Force Protection bases 244.48m"),
    ("air_sar", 193070000, "Air SAR 4 helicopters 193.07m (2026)"),
    ("air_base_support", 124340000, "Airbase general support ILS/meteo 124.34m"),
    ("sea_aswf3", 1918240000, "Surface Combatant 3rd ASWF frigate + NFH 1918.24m (2026)"),
    ("sea_mine", 1170880000, "Naval Mine Warfare logistics/toolbox 1170.88m"),
    ("sea_coastal", 135400000, "Coastal Security ISR/CPV 135.40m"),
    ("sea_harbour", 64090000, "Harbour Protection 64.09m"),
    ("joint_force_prot", 544740000, "Joint Force Protection CBRN/C-UAS/EOD 544.74m"),
    ("general_support_soldier", 936060000, "General Support soldier kit/digitalization/homeland 936.06m"),
    ("unmanned_systems", 367020000, "Unmanned systems land/sea/air 367.02m"),
    ("enablement", 82570000, "Enablement air terminal/rail wagons 82.57m"),
]
for key, amt, note in packages:
    add(2026, f"bud_lpm_{key}_2026_34", amt, note + " (const EUR 2026; multi-year eng)")

# DIRS complementary annex IV
dirs = {2026: 35, 2027: 39, 2028: 46, 2029: 51, 2030: 51, 2031: 50, 2032: 50, 2033: 50, 2034: 49}
for y, m in dirs.items():
    add(y, f"bud_lpm_dirs_complement_{y}", m * 1000000, f"DIRS industrial base complement {m}m const 2026 (art.14: 3pct defence budget + complement)")

# sum of mapped packages
mapped = sum(a for _, a, _ in packages)
add(2026, "bud_lpm_mapped_packages_sum", mapped, f"Sum of extracted annex II named packages {mapped/1e6:.2f}m of 33784 total (residual RPAS/SOF/refuel/maritime C2/medical etc in law)")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets), "mapped packages mEUR", mapped / 1e6)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_lpm_invest_2026_2034",
            "title": "Military programming major equipment investments 33.784bn 2026-2034",
            "entity_id": "mod_defensie",
            "beneficiary": "Belgian armed forces / industry suppliers",
            "legal_basis": "Loi programmation militaire 2026-2034 (Kamer 56K1143); replaces 2017/2022 LPM",
            "decision_date": "2025-11-19",
            "start_year": 2026,
            "end_year": 2034,
            "total_envelope_eur": 33784153531,
            "cash_by_year": '{"note":"constants_2026_engagement_cap_art8","total_m":33784.15}',
            "remaining_eur": 33784153531,
            "status": "active",
            "evaluation_url": "https://www.lachambre.be/FLWB/PDF/56/1143/56K1143001.pdf",
            "stated_goal": "Plan major equipment, personnel growth and defence industrial base to 2034 / NATO 2pct",
            "cut_option": "Annual report art.17; dual contract cash FOI; not abolish alliance path",
            "source_id": "src_kamer_56k1143_lpm_2026_2034",
            "confidence": "strong",
            "hierarchy_path": "Federal>Defence>LPM_2026_2034",
            "notes": "tick394: 33.784bn const26; F-35+11 3.39 SBAMD 4.01 manoeuvre 6.00 ASWF3 1.92; staff 34.5k/12.8k/8.5k 2034",
        }
    ],
)

lbs = [
    (
        "lb_lpm_invest_33_8bn_2026_34",
        "LPM major equipment investments 33.78bn 2026-2034",
        33784153531 / 9,  # illustrative annual average for ranking
        "Strong Kamer law art.8: 33784m EUR constants 2026 eng cap; dual NATO effort path",
        3,
        9.5,
        4,
        6.30,
        "Publish annual contract cash; dual capacity FOI residual",
        "ops",
    ),
    (
        "lb_lpm_land_manoeuvre_6_0bn",
        "LPM Land Combat Manoeuvre vehicles 6.00bn",
        6003820000,
        "Strong annex II: 6003.82m additional motorized vehicles/drones/simulators",
        3,
        9.0,
        5,
        6.15,
        "Unit cost per vehicle class when contracts signed",
        "ops",
    ),
    (
        "lb_lpm_sbamd_4_0bn",
        "LPM Surface-Based Air Missile Defence 4.01bn",
        4013990000,
        "Strong: SBAMD 10 short/med + 3 long-range firing units 4013.99m",
        3,
        9.0,
        5,
        6.15,
        "Dual NASAMS/prior air defence FOI cash",
        "ops",
    ),
    (
        "lb_lpm_f35_extra11_3_39bn",
        "LPM +11 F-35A package 3.39bn",
        3387410000,
        "Strong: 11 extra F-35A + support/spares 3387.41m start 2026; dual prior F-35 fleet",
        3,
        8.5,
        4,
        6.13,
        "Publish signed contract cash-by-year",
        "ops",
    ),
    (
        "lb_lpm_aswf3_1_92bn",
        "LPM 3rd ASWF frigate package 1.92bn",
        1918240000,
        "Strong: third Anti-Submarine Warfare Frigate + NFH support 1918.24m",
        3,
        8.5,
        5,
        6.00,
        "Dual prior ASWF FOI residual",
        "ops",
    ),
    (
        "lb_lpm_staff_growth_2034",
        "LPM staff targets 34.5k active + 12.8k reserve + 8.5k civil 2034",
        0,
        "Strong art.5: 34500/12800/8500; recruit path 2800-3600 active/yr; SSC cost path CoA",
        4,
        5.0,
        5,
        5.15,
        "Publish wage bill cash path dual patronale ONSS",
        "ops",
    ),
    (
        "lb_lpm_dirs_3pct_defence",
        "DIRS defence industrial base 3pct defence budget + complements",
        35000000,
        "Strong art.14: 3pct of defence budget + annex IV complement 35-51m/yr const26",
        4,
        4.5,
        4,
        4.95,
        "Name beneficiary firms/projects L5",
        "ops",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ in lbs:
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "Federal>Defence>LPM>" + iid.replace("lb_lpm_", ""),
            "annual_cost_eur": cost if cost else "",
            "total_cost_eur": 33784153531 if "33_8bn" in iid else (cost if cost else ""),
            "tco_notes": tco + ("; annual=envelope/9 illustrative" if "33_8bn" in iid else "") + ("; staff COUNT not EUR" if "staff" in iid else ""),
            "confidence": "strong",
            "source_id": "src_kamer_56k1143_lpm_2026_2034",
            "beneficiaries": "Belgian Defence / industry",
            "stated_goal": "Major equipment and force growth to 2034",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick394",
        }
    )
# fix total for big packages
for r in lb_rows:
    if r["item_id"] == "lb_lpm_invest_33_8bn_2026_34":
        r["total_cost_eur"] = 33784153531
        r["annual_cost_eur"] = round(33784153531 / 9)
append_rows(DATA / "leaderboard.csv", lb_rows)
print("lb +", len(lb_rows))

draft = REPO / "docs/doge/foi/drafts" / f"{GAP}.md"
draft.parent.mkdir(parents=True, exist_ok=True)
draft.write_text(
    f"""# FOI draft — {GAP}

Status: **ready** (human send only). Not legal advice.

## Brief

```text
[Naam verzoeker]
[Adres / e-mail / telefoon]
[Datum]

Aan: Ministerie van Defensie / Ministere de la Defense
t.a.v. dienst openbaarheid van bestuur

Betreft: Openbaarmaking — LPM 2026-2034: getekende contracten en kaspaden

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Lijst van getekende of in onderhandeling zijnde contracten** onder annex II LPM
   (minstens: F-35A +11, SBAMD, Combat Manoeuvre voertuigen, ASWF-3, CaMo Griffon/Serval)
   met contractwaarde, leverancier, cash-by-year 2025-2034.
2. **Jaarlijks engagement vs art.8 plafond** 33.784 miljard (constante euro 2026).
3. **DIRS** (3% + annex IV): begunstigden/projecten 2025-2026 met bedragen.
4. Eventuele **evaluaties** unit-cost per capaciteit.

Periode: 2025-01-01 tot 2034-12-31.
Intern pad: Federal > Defence > LPM_cash. Ref: {GAP}

Context (publiek Kamer 56K1143):
- eng plafond 33.784 miljard constante 2026;
- packages o.a. manoeuvre 6.004, SBAMD 4.014, F-35 3.387, ASWF 1.918;
- personeel 34.500/12.800/8.500 in 2034.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling Defensie
- [x] Concrete contract cash L5
- [x] Periode
- [ ] Contact verzoeker (mens)
- [x] ready draft complete
""",
    encoding="utf-8",
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Federal>Defence>LPM_contract_cash",
            "entity_id": "mod_defensie",
            "what_is_missing": "Signed/negotiated contract values and cash-by-year 2025-34 for LPM annex II programmes (F-35+11 SBAMD manoeuvre ASWF3 CaMo etc); annual eng vs 33.784bn cap; DIRS beneficiaries",
            "why_it_matters": "33.8bn multi-year equipment envelope; programme names public but signed cash opaque",
            "priority": 7,
            "recipient_body": "Ministerie van Defensie",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_lpm_invest_2026_2034",
            "linked_leaderboard_id": "lb_lpm_invest_33_8bn_2026_34",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick394 LPM public packages strong; residual signed cash human send; dual gap_defence_contract_cash",
        }
    ],
)

with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    efields = list(r.fieldnames)
    ents = list(r)
for row in ents:
    if row.get("entity_id") == "mod_defensie":
        row["notes"] = (
            "NATO 2pct; s16 liq 10.77bn 2026; LPM 2026-34 invest 33.784bn const26; "
            "staff targets 34.5k/12.8k/8.5k; FOI gap_lpm_contract_cash; tick394"
        )
        break
rewrite(DATA / "entities.csv", ents, efields)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = list(r.fieldnames)
    rq = list(r)
for row in rq:
    if row["task_id"] == UNIT:
        row["status"] = "done"
        row["updated_utc"] = NOW
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            "tick394: LPM 33.784bn eng; F-35 3.39 SBAMD 4.01 manoeuvre 6.00 ASWF 1.92; "
            "staff 34.5k; FOI contract cash; spawn rq_386"
        )
        break
if not any(x["task_id"] == "rq_386" for x in rq):
    rq.append(
        {
            "task_id": "rq_386",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "continuous",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "gg_belgium",
            "instructions": "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": "",
            "notes": "Spawned tick394 after LPM 33.8bn; rq_116 SWA deferred",
        }
    )
rewrite(DATA / "research_queue.csv", rq, rq_fields)

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    stf = list(r.fieldnames)
    st = list(r)
st[0].update(
    {
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "notes": "Scheduler 60s. Next prio5 rq_386; rq_116 SWA deferred. FOI ready. tick394 LPM 33.8bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, stf)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **LPM militaire 2026-2034 investissements 33.784bn L5**)
- Found (strong primary Kamer 56K1143):
  - **Engagement plafond art.8: EUR 33,784.15m** constants 2026 for major equipment 2026-2034
  - Staff 2034: **34,500** active · **12,800** reserve · **8,500** civil; recruit 2026: 2800/1050/960
  - Largest packages: Combat Manoeuvre **6,003.8m** · SBAMD **4,014.0m** · F-35+11 **3,387.4m** · ASWF-3 **1,918.2m** · CSS **1,352.6m** · Joint land **1,535.5m** · mine warfare **1,170.9m**
  - Mapped named packages sum **~27.1bn** of 33.8bn (residual RPAS/SOF/refuel/medical etc)
  - DIRS: 3pct defence budget + complements **35-51m/yr** const26
- Wrote: sources +1; budgets +{len(budgets)}; cmt +1; lb +{len(lb_rows)}; entity; FOI **{GAP}** ready prio7; rq_385=done; spawn **rq_386**; ticks={TICK}
- FOI: signed contract cash-by-year human send only
- Next: prio5 **rq_386**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)
