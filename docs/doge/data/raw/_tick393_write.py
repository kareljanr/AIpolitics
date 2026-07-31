# tick393: BOSA interdept provisions 2.13bn L5 map + budget specialty derogations
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T11:15:00Z"
TICK = 393
UNIT = "rq_384"
GAP = "gap_bosa_provisions_l5_2026"


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


# entity bosa if needed
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    efields = list(r.fieldnames)
    ents = list(r)
if not any(e.get("entity_id") == "fod_bosa" for e in ents):
    ents.append(
        {
            "entity_id": "fod_bosa",
            "name_nl": "FOD Beleid en Ondersteuning BOSA",
            "name_fr": "SPF Strategie et Appui BOSA",
            "name_en": "FPS Policy and Support BOSA",
            "level": "ministry",
            "parent_id": "sec_federal",
            "community_language": "bi",
            "website": "https://bosa.belgium.be",
            "foi_email": "",
            "foi_postal": "",
            "notes": "Hosts interdept provisions 2.13bn 2026; tick393",
        }
    )
    rewrite(DATA / "entities.csv", ents, efields)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_ccrek_budget2026_bosa_provisions",
            "title": "Cour des comptes budget Etat 2026 — BOSA provisions interdept 2.13bn + specialite derogations",
            "url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "Provisions eng 2125.8 liq 2128.0; generale 829.8 (justice divers 618.3 ESA 176 Fedasil 100 bpost 78); securite 366.9; Defence transfer power 20.1bn eng",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, ent="fod_bosa", conf="strong", basis="budgeted"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": "src_ccrek_budget2026_bosa_provisions",
            "confidence": conf,
            "notes": note,
        }
    )


# Interdept provisions totals
add(2026, "bud_bosa_prov_interdept_eng_2026", 2125800000, "BOSA programme 06.90.1 interdept provisions engagement 2125.8m 2026 (5 credit lines)")
add(2026, "bud_bosa_prov_interdept_liq_2026", 2128000000, "BOSA interdept provisions liquidation 2128.0m 2026")

# General provision Table
add(2025, "bud_bosa_prov_generale_init_2025", 607300000, "Provision generale initial 607.3m 2025")
add(2025, "bud_bosa_prov_generale_adj_2025", 599700000, "Provision generale adjusted 599.7m 2025")
add(2026, "bud_bosa_prov_generale_2026", 829800000, "Provision generale 829.8m 2026 (+230.1 vs adj 2025)")
add(2026, "bud_bosa_prov_gen_justice_divers_2026", 618300000, "Generale: Frais de justice et divers 618.3m 2026 (was 131.7 adj 2025)")
add(2026, "bud_bosa_prov_gen_fedasil_2026", 100000000, "Generale: Fedasil line 100.0m 2026 (dual package tick391)")
add(2026, "bud_bosa_prov_gen_bpost_2026", 78000000, "Generale: Nouveaux contrats bpost 78.0m 2026 (from 85.4)")
add(2026, "bud_bosa_prov_gen_vulnerables_2026", 33500000, "Generale: Bien-etre groupes vulnerables + cohesion sociale 33.5m 2026")
add(2025, "bud_bosa_prov_gen_pecule_2025", 66000000, "Generale adj 2025: Pecule de vacances 66.0m (0 in 2026 init)")
add(2025, "bud_bosa_prov_gen_decom_2025", 190000000, "Generale adj 2025: Decommissioning dyssinergies 190m (0 in 2026 init)")
# justice divers breakdown
add(2026, "bud_bosa_prov_gen_prison_infra_2026", 259000000, "Within justice divers: prison infra/ops overcrowding 259m 2026")
add(2026, "bud_bosa_prov_gen_esa_2026", 176000000, "Within justice divers: ESA participation 176m 2026")
add(2026, "bud_bosa_prov_gen_econ_sociale_2026", 50000000, "Within justice divers: economie sociale 50m 2026")
add(2026, "bud_bosa_prov_gen_admin_reorg_2026", 36000000, "Within justice divers: federal admin reorg + support centralisation 36m 2026")
add(2026, "bud_bosa_prov_gen_tria_2026", 5300000, "Within justice divers: Tria handicap IT SPF SZ 5.3m 2026")
add(2026, "bud_bosa_prov_gen_cpl_modules_2026", 2700000, "Within justice divers: modular units forensic psychiatry CPL 2.7m 2026")
# multi-year path generale
add(2027, "bud_bosa_prov_generale_2027", 630700000, "Provision generale path 630.7m 2027", conf="medium")
add(2028, "bud_bosa_prov_generale_2028", 1374700000, "Provision generale path 1374.7m 2028 (justice divers spike 1206.7)", conf="medium")
add(2029, "bud_bosa_prov_generale_2029", 1005200000, "Provision generale path 1005.2m 2029", conf="medium")
add(2028, "bud_bosa_prov_gen_justice_divers_2028", 1206700000, "Frais justice et divers line 1206.7m 2028", conf="medium")
add(2029, "bud_bosa_prov_gen_justice_divers_2029", 812200000, "Frais justice et divers line 812.2m 2029", conf="medium")

# Security provision (refresh + total package with generale)
add(2026, "bud_bosa_prov_securite_2026", 366900000, "Provision securite+retour 366.9m 2026")
add(2026, "bud_bosa_prov_pack_gen_sec_2026", 1196700000, "Sum generale+securite provisions 829.8+366.9=1196.7m 2026 (subset of 2.13bn)")

# Specialty derogations - transferable envelopes (governance opacity)
add(2024, "bud_credit_redistrib_2024", 454000000, "Inter-programme credit redistributions 454m engagement 2024 (specialty erosion)", basis="outturn")
add(2026, "bud_defence_eng_redistributable_2026", 20100000000, "Defence s16 engagement credits redistributable freely 20.1bn 2026 (ex cells/fonds)", ent="mod_defensie")
add(2026, "bud_justice_eng_redistributable_2026", 2500000000, "Justice s12 personnel/ops/invest redistributable freely 2.5bn class 2026", ent="fod_justice")
add(2026, "bud_police_eng_redistributable_2026", 1600000000, "Police s17 personnel/ops/invest redistributable freely 1.6bn 2026", ent="police_federale")

# bpost contracts in provision
add(2026, "bud_bpost_new_contracts_prov_2026", 78000000, "bpost new contracts via generale provision 78m 2026", ent="sec_federal")

# Ukraine / EPF residual if in provisions - mention from earlier 120m Ukraine provision
# From tick392: Ukraine provision 06.90.10.01.00.09 120m for EPF - check if we should add
add(2026, "bud_bosa_prov_ukraine_epf_2026", 120000000, "Ukraine interdept provision for EPF 120m class (Affaires etrangeres EPF dual Defence 8.2m military)", conf="medium")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_bosa_provisions_2026",
            "title": "BOSA interdepartmental provisions package 2.13bn 2026",
            "entity_id": "fod_bosa",
            "beneficiary": "Justice prisons ESA Fedasil bpost admin reorg police migration",
            "legal_basis": "Budget general programme 06.90.1; CM transfers without parliament",
            "decision_date": "2026-01-01",
            "start_year": 2026,
            "end_year": 2026,
            "total_envelope_eur": 2128000000,
            "cash_by_year": '{"2026":2128000000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/2026_16_Budget2026.pdf",
            "stated_goal": "Flexible interdept financing when destination not fixed at budget vote",
            "cut_option": "Inscribe known amounts in recipient sections; restore specialty; annuality",
            "source_id": "src_ccrek_budget2026_bosa_provisions",
            "confidence": "strong",
            "hierarchy_path": "Federal>BOSA>provisions_interdept",
            "notes": "tick393: eng 2125.8 liq 2128; generale 829.8 + securite 366.9 mapped L5; residual lines FOI",
        }
    ],
)

lbs = [
    (
        "lb_bosa_provisions_2_13bn_2026",
        "BOSA interdept provisions 2.13bn 2026",
        2128000000,
        "Strong CoA: liq 2128m eng 2125.8; 5 provisional credits; CM transfer without parliament",
        7,
        8.5,
        4,
        7.05,
        "Force on-section booking for known destinations; publish L5 table",
        "ops",
    ),
    (
        "lb_bosa_prov_generale_830m_2026",
        "BOSA general provision 829.8m 2026",
        829800000,
        "Strong: +230m vs 2025; justice divers 618.3 dominates; path spikes 1.37bn 2028",
        7,
        7.5,
        4,
        6.70,
        "Split justice divers into named section lines",
        "ops",
    ),
    (
        "lb_bosa_justice_divers_618m_2026",
        "Provision justice et divers 618.3m 2026",
        618300000,
        "Strong L5: prison infra 259 + ESA 176 + social econ 50 + admin reorg 36 + Tria 5.3 + CPL 2.7",
        6,
        7.5,
        4,
        6.55,
        "Move prison/ESA to section budgets; residual FOI",
        "ops",
    ),
    (
        "lb_bosa_esa_176m_2026",
        "ESA participation via general provision 176m 2026",
        176000000,
        "Strong: Belgian ESA contribution parked in BOSA justice-divers provision",
        6,
        7.0,
        3,
        6.25,
        "Book under science/space section not justice divers",
        "transfer",
    ),
    (
        "lb_defence_redistrib_20bn_2026",
        "Defence engagement credits freely redistributable 20.1bn 2026",
        20100000000,
        "Strong CoA: specialty derogation entire s16 eng (ex cells); parliament control hollowed",
        7,
        9.5,
        5,
        7.35,
        "Restore programme constraints; publish reallocation log",
        "ops",
    ),
    (
        "lb_justice_police_redistrib_4_1bn_2026",
        "Justice+Police free redistrib powers 2.5+1.6bn 2026",
        4100000000,
        "Strong: s12 2.5bn + s17 1.6bn personnel/ops/invest freely movable within section",
        6,
        8.5,
        5,
        6.80,
        "Limit redistributions; report to CoA/parliament",
        "ops",
    ),
    (
        "lb_credit_redistrib_454m_2024",
        "Inter-programme credit redistributions 454m 2024",
        454000000,
        "Strong outturn: 454m engagement moved across programmes 2024 under cumulative derogations",
        6,
        7.5,
        4,
        6.55,
        "Publish annual reallocation ledger",
        "ops",
    ),
    (
        "lb_bpost_prov_78m_2026",
        "bpost new contracts via BOSA provision 78m 2026",
        78000000,
        "Strong: 78m in generale (from 85.4); dual bpost PSO FOI residual",
        5,
        5.5,
        4,
        5.55,
        "Book under postal PSO section",
        "transfer",
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
            "hierarchy_path": "Federal>BOSA>" + iid.replace("lb_", ""),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": "strong",
            "source_id": "src_ccrek_budget2026_bosa_provisions",
            "beneficiaries": "Multiple federal departments via flexible provisions",
            "stated_goal": "Budget flexibility / interdept contingency",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick393",
        }
    )
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

Aan: FOD BOSA / SPF Strategie et Appui
t.a.v. dienst openbaarheid van bestuur

Betreft: Openbaarmaking — 5 interdepartementale provisies 2026 (2,13 miljard) L5 splits

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Volledige tabel** van de vijf provisiekredieten in programma 06.90.1 (engagement en
   liquidatie 2026), met per lijn: bestemming, begunstigde FOD/SPP, basisallocatie.
2. **Splitsing** van de lijn "Frais de justice et divers" (618,3 miljoen) tot op projectniveau
   (naast de publieke 259/176/50/36/5,3/2,7 miljoen).
3. **CM-besluiten** die transfers vanuit provisies naar secties in 2025-2026 autoriseerden
   (bedrag, datum, bestemming).
4. **Meerjarenraming** 2027-2029 per provisielijn (path 630.7 / 1374.7 / 1005.2 generale).

Periode: 2025-01-01 tot 2029-12-31.
Intern pad: Federal > BOSA > provisions_L5. Ref: {GAP}

Context (publiek CoA budget 2026):
- provisies eng 2.125,8 / liq 2.128,0 miljoen;
- generale 829,8; securite 366,9;
- Rekenhof: bekende bestemmingen horen in secties, niet in provisie.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling BOSA
- [x] Concrete 5-line provision L5
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
            "hierarchy_path": "Federal>BOSA>provisions_interdept_L5",
            "entity_id": "fod_bosa",
            "what_is_missing": "Full 5-line interdept provision table 2026 with recipient SPF and AB codes; residual justice-divers L5 beyond published 259/176/50/36/5.3/2.7; CM transfer log 2025-26; multi-year path detail",
            "why_it_matters": "2.13bn flexible pot weakens parliamentary specialty; known destinations parked off-section",
            "priority": 7,
            "recipient_body": "FOD BOSA",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_bosa_provisions_2026",
            "linked_leaderboard_id": "lb_bosa_provisions_2_13bn_2026",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick393 CoA public fill major lines; residual L5 human send",
        }
    ],
)

with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    efields = list(r.fieldnames)
    ents = list(r)
for row in ents:
    if row.get("entity_id") == "fod_bosa":
        row["notes"] = (
            "Hosts interdept provisions eng 2.13bn liq 2.13bn 2026; generale 829.8; "
            "securite 366.9; FOI gap_bosa_provisions_l5_2026; tick393"
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
            "tick393: BOSA provisions 2.13bn; generale 829.8 (prison 259 ESA 176); "
            "defence redistrib 20.1bn; FOI residual L5; spawn rq_385"
        )
        break
if not any(x["task_id"] == "rq_385" for x in rq):
    rq.append(
        {
            "task_id": "rq_385",
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
            "notes": "Spawned tick393 after BOSA provisions; rq_116 SWA deferred",
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
        "notes": "Scheduler 60s. Next prio5 rq_385; rq_116 SWA deferred. FOI ready. tick393 BOSA provisions 2.13bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, stf)

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **BOSA interdept provisions 2.13bn L5 + specialty derogations**)
- Found (strong primary CoA Budget 2026):
  - Interdept provisions **eng EUR 2,125.8m** / **liq 2,128.0m** (prog 06.90.1)
  - **Generale 829.8m**: justice divers **618.3** (prison infra **259** · ESA **176** · econ sociale **50** · admin reorg **36** · Tria **5.3** · CPL **2.7**) · Fedasil **100** · bpost **78** · vulnerables **33.5**
  - **Securite 366.9m** (already dual Justice/Police/Migration)
  - Path generale **630.7 / 1,374.7 / 1,005.2** 2027-29; justice divers spike **1,206.7** 2028
  - Specialty hollowed: Defence eng redistributable **20.1bn**; Justice **2.5bn**; Police **1.6bn**; 2024 redistribs **454m**
- Wrote: sources +1; budgets +{len(budgets)}; cmt +1; lb +{len(lb_rows)}; entity fod_bosa; FOI **{GAP}** ready prio7; rq_384=done; spawn **rq_385**; ticks={TICK}
- FOI: residual provision lines + CM transfer log human send only
- Next: prio5 **rq_385**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)
