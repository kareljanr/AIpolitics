# tick388: ONSS Gestion globale salariés L5 + pensions publiques + SS consol dual
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T08:45:00Z"
TICK = 388
UNIT = "rq_379"
GAP = "gap_onss_gg_transfer_l5"


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
            "source_id": "src_ccrek_ss_182e_gg_salaries_2025",
            "title": "Cour des comptes Cahier 2025 SS — ONSS Gestion globale salaries Tables 1-3 12-16 + altfin",
            "url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "GG sal prestations 60.515bn 2024 rec 99.198bn cotis 65.769bn dots 9.489 altfin 21.367; pens pub 21.041; dual indep tick386",
        },
    ],
)

budgets = []


def add(y, bid, amt, note, ent="rsz"):
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_ccrek_ss_182e_gg_salaries_2025",
            "confidence": "strong",
            "notes": note,
        }
    )


# GG salaries prestations multi-year Table2
for y, tot, pens, inv, chom, at, mp, autres in [
    (2022, 52248400000, 34047300000, 11229100000, 6449500000, 296200000, 219000000, 7200000),
    (2023, 56417700000, 37487000000, 12213600000, 6179500000, 312800000, 217300000, 7500000),
    (2024, 60514700000, 40125200000, 13449000000, 6391000000, 327100000, 214800000, 7700000),
]:
    add(y, f"bud_gg_sal_prest_{y}", tot, f"GG salaries prestations consolidees {tot/1e6:.1f}m CoA Table2")
    add(y, f"bud_gg_sal_pens_{y}", pens, f"GG sal pensions {pens/1e6:.1f}m (via FPD dual)")
    add(y, f"bud_gg_sal_invalidite_{y}", inv, f"GG sal invalidite {inv/1e6:.1f}m")
    add(y, f"bud_gg_sal_chomage_{y}", chom, f"GG sal chomage {chom/1e6:.1f}m (via RVA dual)")
    add(y, f"bud_gg_sal_at_{y}", at, f"GG sal accidents travail {at/1e6:.1f}m (Fedris dual)")
    add(y, f"bud_gg_sal_mp_{y}", mp, f"GG sal maladies pro {mp/1e6:.1f}m")
    add(y, f"bud_gg_sal_autres_prest_{y}", autres, f"GG sal autres prestations {autres/1e6:.1f}m")

# soldes Table1
for y, s in [(2022, -849700000), (2023, 240700000), (2024, 83900000)]:
    add(y, f"bud_gg_sal_solde_{y}", s, f"GG salaries solde provisoire {s/1e6:.1f}m")

# recettes Table13
for y, rec in [(2022, 85442900000), (2023, 93430500000), (2024, 99197800000)]:
    add(y, f"bud_gg_sal_rec_{y}", rec, f"GG salaries recettes consolidees {rec/1e6:.1f}m")

# cotisations Table14 + L5 2024
for y, cot in [(2022, 58532800000), (2023, 62867900000), (2024, 65768600000)]:
    add(y, f"bud_gg_sal_cotis_{y}", cot, f"GG sal cotisations sociales {cot/1e6:.1f}m")

add(2024, "bud_gg_sal_cotis_salaries_2024", 60186000000, "Cotisations travailleurs salaries 60186.0m 2024 (91.51pct)")
add(2024, "bud_gg_sal_cotis_locaux_2024", 5126200000, "Cotisations pouvoirs locaux 5126.2m 2024 (7.79pct)")
add(2024, "bud_gg_sal_cotis_onss_gg_2024", 65677600000, "ONSS-GG proper cotis 65677.6m 2024 (99.86pct of GG sal cotis)")
add(2024, "bud_gg_sal_cotis_other_ipss_2024", 90900000, "Cotis other IPSS 90.9m (SFP 57.7 Fedris 32.6 INAMI 0.6)")

# dots Table16
for y, tot, ord_, eq, fed in [
    (2022, 7434300000, 2551000000, 4076900000, 806400000),
    (2023, 8986600000, 2674700000, 5603700000, 708200000),
    (2024, 9488800000, 2764600000, 6142200000, 582000000),
]:
    add(y, f"bud_gg_sal_dots_total_{y}", tot, f"ONSS-GG dots+subventions {tot/1e6:.1f}m")
    add(y, f"bud_gg_sal_dot_ord_{y}", ord_, f"Dotation ordinaire Etat ONSS-GG {ord_/1e6:.1f}m")
    add(y, f"bud_gg_sal_dot_equilibre_{y}", eq, f"Dotation equilibre Etat ONSS-GG {eq/1e6:.1f}m")
    add(y, f"bud_gg_sal_sub_federees_{y}", fed, f"Subventions entites federees ONSS-GG {fed/1e6:.1f}m")

add(2024, "bud_gg_sal_dot_ord_core_2024", 2565600000, "Dotation ordinaire core 2565.6m 2024 (excl police)")
add(2024, "bud_gg_sal_police_salaires_2024", 199000000, "Subvention salaires zones police 199.0m 2024 (within ord package)")
add(2024, "bud_gg_sal_sub_ages_2024", 351300000, "Reductions groupe-cible ages 351.3m 2024 (of 582 federees)")
add(2024, "bud_gg_sal_sub_acs_2024", 72000000, "Reductions contractuels subventionnes ACS 72.0m 2024")
add(2024, "bud_gg_sal_sub_art60_2024", 60100000, "Reductions article 60 60.1m 2024")
add(2025, "bud_gg_sal_rembourse_exc_2025", 623100000, "ONSS-GG rembourse 623.1m en 2025 (excedent 2023 equilibre+altfin sante)")

# altfin ONSS
for y, alt in [(2022, 17265700000), (2023, 19361500000), (2024, 21367400000)]:
    add(y, f"bud_gg_sal_altfin_{y}", alt, f"Financement alternatif ONSS-GG {alt/1e6:.1f}m")
add(2024, "bud_gg_sal_altfin_tva_base_2024", 8577900000, "Altfin TVA base/plancher 8577.9m 2024")
add(2024, "bud_gg_sal_altfin_tva_sante_2024", 6841000000, "Altfin TVA soins sante 6841.0m 2024")
add(2024, "bud_gg_sal_altfin_pm_2024", 5948500000, "Altfin precompte mobilier 5948.5m 2024")

# reductions cotis TE-adjacent
add(2024, "bud_gg_sal_red_fed_2024", 3592600000, "Reductions federales cotisations (moindres recettes) 3592.6m 2024")
add(2024, "bud_gg_sal_bonus_emploi_2024", 1679200000, "Bonus a l emploi 1679.2m 2024")
add(2024, "bud_gg_sal_red_structurelles_2024", 1866200000, "Reductions structurelles patronales 1866.2m 2024")
add(2024, "bud_gg_sal_red_cibles_dep_2024", 920200000, "Reductions cibles as social dep 920.2m 2024 (premiers engagements class)")
add(2023, "bud_gg_sal_exoneration_707_2023", 1082200000, "Exoneration exceptionnelle 7.07pct Q1-Q2 2023 1082.2m (moindre recette)")

# pensions publiques
for y, dep, rec, cot, dot in [
    (2022, 18722400000, 19456200000, 5792700000, 13566200000),
    (2023, 20233200000, 21766900000, 6747000000, 14899100000),
    (2024, 21041000000, 22438500000, 6853600000, 15471500000),
]:
    add(y, f"bud_pens_pub_dep_{y}", dep, f"Pensions publiques depenses {dep/1e6:.1f}m", "fpd")
    add(y, f"bud_pens_pub_rec_{y}", rec, f"Pensions publiques recettes {rec/1e6:.1f}m", "fpd")
    add(y, f"bud_pens_pub_cotis_{y}", cot, f"Pensions publiques cotisations {cot/1e6:.1f}m", "fpd")
    add(y, f"bud_pens_pub_dot_{y}", dot, f"Dotation Etat pensions publiques {dot/1e6:.1f}m", "fpd")
add(2024, "bud_pens_pub_fonds_solidarise_2024", 3436200000, "Cotisations fonds pension solidarise APL 3436.2m 2024", "fpd")
add(2024, "bud_pens_pub_solde_{}".format(2024), 350500000, "Pensions publiques solde +350.5m 2024", "fpd")

# INAMI soins branch consol (not full RIZIV matrix)
for y, dep, rec, solde in [
    (2022, 31544500000, 6264500000, 1271200000),
    (2023, 34497300000, 6043300000, 240900000),
    (2024, 37040900000, 6693100000, 300100000),
]:
    add(y, f"bud_inami_ss_dep_{y}", dep, f"INAMI soins sante depenses consolidees {dep/1e6:.1f}m (87pct of branch class)", "riziv_care")
    add(y, f"bud_inami_ss_rec_{y}", rec, f"INAMI soins sante recettes propres {rec/1e6:.1f}m", "riziv_care")
    add(y, f"bud_inami_ss_solde_{y}", solde, f"INAMI soins sante solde {solde/1e6:.1f}m", "riziv_care")
add(2024, "bud_inami_retenue_pensions_2024", 1752900000, "Retenue 3.55pct sur pensions 1752.9m 2024 (99.4pct INAMI cotis rec)", "riziv_care")

# hors GG + frais gestion + autres
for y, dep, rec in [(2022, 731500000, 1010600000), (2023, 842700000, 1160900000), (2024, 873500000, 1172400000)]:
    add(y, f"bud_ss_hors_gg_dep_{y}", dep, f"Regimes hors Gestion globale dep {dep/1e6:.1f}m", "sec_ss")
    add(y, f"bud_ss_hors_gg_rec_{y}", rec, f"Regimes hors GG rec {rec/1e6:.1f}m", "sec_ss")
for y, amt in [(2022, 2528100000), (2023, 2698500000), (2024, 2790600000)]:
    add(y, f"bud_ss_frais_gestion_{y}", amt, f"SS frais de gestion consolides {amt/1e6:.1f}m", "sec_ss")
for y, amt in [(2022, 10237100000), (2023, 10136000000), (2024, 10473500000)]:
    add(y, f"bud_ss_autres_dep_{y}", amt, f"SS autres depenses consolidees {amt/1e6:.1f}m", "sec_ss")

# FFE cotis
add(2024, "bud_ffe_cotis_employeurs_2024", 275400000, "FFE cotisations employeurs 275.4m 2024 (74.37pct hors-GG cotis)", "sec_ss")

# beneficiaries pension retraite salaries
add(2023, "bud_gg_sal_pens_benef_2023", 2112213, "Beneficiaires pension retraite salaries moyen 2112213 2023 (COUNT)", "fpd")
add(2024, "bud_gg_sal_pens_benef_2024", 2178093, "Beneficiaires pension retraite salaries moyen 2178093 2024 (+3.12pct; COUNT)", "fpd")

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_onss_gg_salaries_2024",
            "title": "ONSS Gestion globale salaries prestations + financing 2022-2024",
            "entity_id": "rsz",
            "beneficiary": "Employees pensions invalidity unemployment Fedris path",
            "legal_basis": "Gestion financiere globale regime salaries; ONSS centralise recettes",
            "decision_date": "2024-01-01",
            "start_year": 2022,
            "end_year": 2024,
            "total_envelope_eur": 169180800000,
            "cash_by_year": '{"2022":52248400000,"2023":56417700000,"2024":60514700000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "stated_goal": "Finance employee social security branches via global management",
            "cut_option": "Open IPSS transfer L5 codes; dual reduction TE path; not cut core benefits blindly",
            "source_id": "src_ccrek_ss_182e_gg_salaries_2025",
            "confidence": "strong",
            "hierarchy_path": "SS>ONSS>gestion_globale_salaries",
            "notes": "tick388: prest 60.515bn pens40.1 inv13.4 chom6.4; cotis65.8 dots9.5 altfin21.4; FOI transfer L5",
        }
    ],
)

lbs = [
    (
        "lb_gg_sal_prest_60_5bn_2024",
        "ONSS GG salaries prestations 60.51bn 2024",
        60514700000,
        "Strong CoA: 60514.7m (+7.26pct); pens 40.1 inv 13.4 chom 6.4 AT/MP 0.54; dual FPD/RVA/Fedris",
        2,
        10.0,
        2,
        6.90,
        "Core entitlement mega; dual residual IPSS cash codes FOI",
        "transfer",
    ),
    (
        "lb_gg_sal_pens_40_1bn_2024",
        "GG salaries pensions 40.13bn 2024",
        40125200000,
        "Strong: 40125.2m; dual PensionStat/FPD; +7.04pct volume-driven 2024",
        2,
        10.0,
        2,
        6.90,
        "Parameter reform path; dual FPD payment already mapped",
        "transfer",
    ),
    (
        "lb_gg_sal_invalidite_13_4bn_2024",
        "GG salaries invalidity 13.45bn 2024",
        13449000000,
        "Strong: 13449m (+10.11pct); dual RIZIV indemnites; psych 38pct osteo 32pct causes 2023",
        3,
        9.0,
        4,
        6.30,
        "ReAT path transparency; dual mutual admin",
        "transfer",
    ),
    (
        "lb_gg_sal_cotis_65_8bn_2024",
        "ONSS GG cotisations 65.77bn 2024",
        65768600000,
        "Strong: 65768.6m (salaries 60.2 locaux 5.1); dual reductions 3.59bn structural",
        3,
        10.0,
        3,
        6.75,
        "Publish reduction TE dual FPS inventory link",
        "transfer",
    ),
    (
        "lb_gg_sal_altfin_21_4bn_2024",
        "ONSS GG financement alternatif 21.37bn 2024",
        21367400000,
        "Strong: 21367.4m TVA+PM+sante; path from 17.3bn 2022",
        3,
        9.5,
        3,
        6.55,
        "Tax wedge transparency dual budget general",
        "transfer",
    ),
    (
        "lb_gg_sal_dots_9_49bn_2024",
        "ONSS GG state dots+regional 9.49bn 2024",
        9488800000,
        "Strong: equilibre 6.14 + ord 2.76 + federees 0.58; repay excess 623m 2025",
        4,
        9.0,
        4,
        6.40,
        "Publish equilibre methodology cash path",
        "transfer",
    ),
    (
        "lb_gg_sal_red_cotis_3_59bn_2024",
        "Federal cotisation reductions 3.59bn 2024",
        3592600000,
        "Strong: 3592.6m moindres recettes; bonus emploi 1.68 + structurelles 1.87; +cibles dep 0.92",
        5,
        8.5,
        4,
        6.35,
        "Dual taxex inventory; evaluate employment additionality",
        "tax_expenditure",
    ),
    (
        "lb_pens_pub_21_0bn_2024",
        "Public sector pensions 21.04bn 2024",
        21041000000,
        "Strong: 21041m; dot Etat 15.47; cotis 6.85 incl fonds solidarise 3.44; dual FPD",
        2,
        9.5,
        3,
        6.55,
        "Convergence path with private regimes",
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
            "hierarchy_path": "SS>ONSS>" + iid.replace("lb_", ""),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": "strong",
            "source_id": "src_ccrek_ss_182e_gg_salaries_2025",
            "beneficiaries": "Employees / public pensioners",
            "stated_goal": "Employee and public sector social insurance",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick388",
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

Aan: Rijksdienst voor Sociale Zekerheid (RSZ) / ONSS
t.a.v. dienst openbaarheid van bestuur
E-mail: via onss.be openbaarheid of actuele mailbox

Betreft: Openbaarmaking — transfers Globaal Beheer werknemers naar OISZ 2022-2025

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Cash-by-year transfers** uit de Gestion globale des travailleurs salaries / Globaal
   Beheer werknemers naar elke OISZ (FPD, RVA, Fedris, RIZIV, e.a.) 2022-2025,
   met budgetcodes/basisallocaties.
2. **Uitsplitsing cotisations** 2024-2025: werknemers / werkgevers / lokale besturen /
   andere, en residuale 90,9 miljoen via FPD/Fedris/INAMI.
3. **Dotation d equilibre** methodologie en cash-pad 2022-2025 inclusief
   terugbetaling 623,1 miljoen (2025).
4. Eventuele **machine-readable export** van de grootste 50 transferlijnen.

Periode: 2022-01-01 tot 2025-12-31.
Intern pad: SS > ONSS > GG_salaries_transfer_L5. Ref: {GAP}

Context (publiek CoA Cahier 2025):
- prestaties GG 60,515 miljard (2024); cotis 65,769; dots 9,489; altfin 21,367;
- residuale transfer L5 per OISZ niet in publieke tabel.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling ONSS/RSZ
- [x] Concrete transfer L5 + cotis + equilibre
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
            "hierarchy_path": "SS>ONSS>GG_salaries_transfer_L5",
            "entity_id": "rsz",
            "what_is_missing": "Cash-by-year ONSS GG salaries transfers to each IPSS 2022-25 with budget codes; cotis residual split; equilibre methodology + 623m 2025 repay",
            "why_it_matters": "60.5bn prestations mapped by branch; end-receiver IPSS transfer codes still opaque",
            "priority": 6,
            "recipient_body": "ONSS / RSZ",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_onss_gg_salaries_2024",
            "linked_leaderboard_id": "lb_gg_sal_prest_60_5bn_2024",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick388 CoA public fill; residual transfer L5 human send",
        }
    ],
)

# entity rsz
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("entity_id") == "rsz":
        row["notes"] = (
            "ONSS/RSZ employee SS; GG sal prest 60.515bn cotis 65.77bn dots 9.49 "
            "altfin 21.37 2024 strong CoA; beheer path prior; dual indep RSVZ; "
            f"FOI {GAP}; tick388"
        )
        break
rewrite(DATA / "entities.csv", rows, list(fields))

# research queue
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq = list(r)
for row in rq:
    if row["task_id"] == UNIT:
        row["status"] = "done"
        row["updated_utc"] = NOW
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            "tick388: GG sal prest 60.5bn pens40.1 inv13.4 chom6.4; cotis65.8 "
            "dots9.5 altfin21.4; pens pub 21.0; FOI transfer L5; spawn rq_380"
        )
        break
if not any(x["task_id"] == "rq_380" for x in rq):
    rq.append(
        {
            "task_id": "rq_380",
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
            "notes": "Spawned tick388 after ONSS GG salaries L5; rq_116 SWA deferred",
        }
    )
# progress milestone due at tick 390 - no special action now
rewrite(DATA / "research_queue.csv", rq, list(rq_fields))

with (DATA / "loop_state.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    stf = r.fieldnames
    st = list(r)
st[0].update(
    {
        "last_tick_utc": NOW,
        "last_unit_id": UNIT,
        "ticks_completed": str(TICK),
        "paused": "no",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "notes": "Scheduler 60s. Next prio5 rq_380; progress@390 soon; rq_116 SWA deferred. tick388 GG sal 60.5bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, list(stf))

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **ONSS Gestion globale salaries L5 + pensions publiques**)
- Found (strong primary CoA Cahier 2025 SS Tables 1-3 12-16):
  - GG sal **prestations EUR 60,514.7m 2024** (pens **40,125** · inv **13,449** · chom **6,391** · AT/MP **542**)
  - Rec **99,197.8m** · cotis **65,768.6m** (sal 60,186 · locaux 5,126) · solde **+83.9m**
  - Dots **9,488.8m** (equilibre 6,142 · ord 2,765 · federees 582) · altfin **21,367.4m**
  - Reductions cotis **3,592.6m** (bonus emploi 1,679 · structurelles 1,866) + cibles dep **920m**
  - Pensions publiques **21,041m** · dot Etat **15,472m** · fonds solidarise **3,436m**
  - INAMI soins consol dep **37,041m** · retenue pensions **1,753m**
- Wrote: sources +1; budgets +{len(budgets)}; cmt +1; lb +{len(lb_rows)}; entity; FOI **{GAP}** ready; rq_379=done; spawn **rq_380**; ticks={TICK}
- FOI: IPSS transfer cash codes + equilibre path human send only
- Next: prio5 **rq_380** (progress@390 next); deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)
