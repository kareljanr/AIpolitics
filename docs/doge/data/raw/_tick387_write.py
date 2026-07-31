# tick387: ONVA/RJV annual leave pécules L5 + dual CSV + FFE loan
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T08:15:00Z"
TICK = 387
UNIT = "rq_378"
GAP = "gap_onva_csv_l5"


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
            "source_id": "src_ccrek_ss_182e_onva_2025",
            "title": "Cour des comptes Cahier 2025 SS — ONVA vacances annuelles Table11 + comptes 2023 + dual CSV",
            "url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "ONVA rec 6.481bn dep 6.381bn 2024; pecules 6.339bn ONVA-caisse 64.1pct; beheer 23.6m 2023; FFE loan 200m; dual 9 CSV; ESA S1311 not S1314",
        },
    ],
)

# ONVA-caisse share 64.10% of 6338.5m = 4062.9785m; CSV = 2275.5215m
onva_caisse_2024 = int(round(6338.5e6 * 0.6410))
csv_2024 = int(round(6338.5e6 * (1 - 0.6410)))
# reverse 2023: onva-caisse +274m => 2023 caisse = 4062.9785-274 = 3788.9785; CSV +134.9 => 2023 csv = 2275.5215-134.9
onva_caisse_2023 = int(round(onva_caisse_2024 - 274.0e6))
csv_2023 = int(round(csv_2024 - 134.9e6))

budgets = []
rows_data = [
    # multi-year totals Table 11
    (2022, "bud_onva_rec_2022", 5544700000, "ONVA recettes budgetaires 5544.7m 2022"),
    (2023, "bud_onva_rec_2023", 6026100000, "ONVA recettes budgetaires 6026.1m 2023"),
    (2024, "bud_onva_rec_2024", 6481300000, "ONVA recettes budgetaires 6481.3m 2024 (+7.55pct)"),
    (2022, "bud_onva_dep_2022", 5654800000, "ONVA depenses budgetaires 5654.8m 2022"),
    (2023, "bud_onva_dep_2023", 5983900000, "ONVA depenses budgetaires 5983.9m 2023"),
    (2024, "bud_onva_dep_2024", 6381200000, "ONVA depenses budgetaires 6381.2m 2024 (+6.64pct)"),
    (2022, "bud_onva_solde_2022", -110100000, "ONVA solde budgetaire -110.1m 2022"),
    (2023, "bud_onva_solde_2023", 42200000, "ONVA solde budgetaire +42.2m 2023"),
    (2024, "bud_onva_solde_2024", 100100000, "ONVA solde budgetaire +100.1m 2024"),
    # prestations package
    (2024, "bud_onva_pecules_total_2024", 6338500000, "Pecules ONVA-caisse + transferts CSV 6338.5m 2024"),
    (2024, "bud_onva_caisse_pecules_2024", onva_caisse_2024, f"ONVA-caisse publique pecules 64.10pct = {onva_caisse_2024/1e6:.1f}m 2024 (+274m)"),
    (2024, "bud_onva_csv_transfer_2024", csv_2024, f"Transferts 9 caisses speciales vacances (CSV) privees {csv_2024/1e6:.1f}m 2024 (+134.9m)"),
    (2023, "bud_onva_caisse_pecules_2023", onva_caisse_2023, f"ONVA-caisse pecules implied 2023 {onva_caisse_2023/1e6:.1f}m (back from +274m delta strong)"),
    (2023, "bud_onva_csv_transfer_2023", csv_2023, f"CSV transfers implied 2023 {csv_2023/1e6:.1f}m (back from +134.9m delta strong)"),
    # financing
    (2024, "bud_onva_cotis_patronales_2024", 5698500000, "Cotisations patronales via ONSS 5698.5m 2024 (87.92pct recettes; 15.84pct of 108pct brut)"),
    (2024, "bud_onva_onem_contrib_2024", 30700000, "Contribution ONEM 6pct chomage assimile 30.7m 2024 (from 14.3m 2023)"),
    (2023, "bud_onva_onem_contrib_2023", 14300000, "Contribution ONEM 14.3m 2023"),
    (2024, "bud_onva_ffe_loan_2024", 200000000, "Pret FFE sans interets 200m 2024 (remboursement 15y from 2029 @20m/yr)"),
    # beheer / missions comptes
    (2022, "bud_onva_beheer_2022", 22400000, "ONVA depenses gestion 22.4m 2022 CoA Table27"),
    (2023, "bud_onva_beheer_2023", 23600000, "ONVA depenses gestion 23.6m 2023"),
    (2022, "bud_onva_missions_dep_2022", 5632400000, "ONVA missions depenses 5632.4m 2022 comptes"),
    (2023, "bud_onva_missions_dep_2023", 5960400000, "ONVA missions depenses 5960.4m 2023"),
    (2022, "bud_onva_missions_rec_2022", 5544700000, "ONVA missions recettes 5544.7m 2022"),
    (2023, "bud_onva_missions_rec_2023", 6026100000, "ONVA missions recettes 6026.1m 2023"),
    # accounting adjustments CoA (not cash)
    (2023, "bud_onva_dc_debt_pecules_2023", 6338500000, "CoA droits constates: dettes pecules N impact -6338.5m on 2023 results (accounting not cash)"),
    (2023, "bud_onva_dc_creance_cotis_2023", 3904400000, "CoA droits constates: creance cotisations +3904.4m impact 2023"),
    (2023, "bud_onva_provision_unjustified_2023", 1754800000, "CoA: provision risques unjustified 1754.8m to reverse (accounting)"),
    # beneficiaries count
    (2023, "bud_onva_benef_ouvriers_2023", 1682104, "Ouvriers beneficiaires pecules 1682104 2023 (COUNT)"),
    (2024, "bud_onva_benef_ouvriers_2024", 1661304, "Ouvriers beneficiaires pecules 1661304 2024 (-1.24pct; COUNT)"),
    # dual CSV count
    (2024, "bud_onva_csv_count_2024", 9, "9 caisses speciales de vacances privees sectorielles + ONVA-caisse publique (COUNT entities)"),
    # FEDRIS deepen same CoA (adjacent SS L5 free fill same source unit)
    (2022, "bud_fedris_total_2022", 568600000, "Fedris depenses budgetaires 568.6m 2022 Table8"),
    (2023, "bud_fedris_total_2023", 588000000, "Fedris 588.0m 2023"),
    (2024, "bud_fedris_total_2024", 596400000, "Fedris 596.4m 2024 (+1.43pct)"),
    (2024, "bud_fedris_gg_2024", 541900000, "Fedris Gestion globale 541.9m 2024"),
    (2024, "bud_fedris_at_gg_2024", 327100000, "Accidents travail GG 327.1m 2024"),
    (2024, "bud_fedris_mp_gg_2024", 214800000, "Maladies professionnelles GG 214.8m 2024"),
    (2024, "bud_fedris_hors_gg_2024", 54500000, "Fedris hors GG 54.5m 2024"),
    (2024, "bud_fedris_amiante_2024", 23600000, "Fonds amiante 23.6m 2024"),
    # CAAMI missions 2024 Table10 same CoA wave
    (2022, "bud_hziv_missions_2022", 537900000, "CAAMI/HZIV missions 537.9m 2022"),
    (2023, "bud_hziv_missions_2023", 593900000, "CAAMI missions 593.9m 2023"),
    (2024, "bud_hziv_missions_2024", 642600000, "CAAMI missions 642.6m 2024"),
    (2024, "bud_hziv_ami_2024", 534400000, "CAAMI AMI obligatoire 534.4m 2024 (83.16pct)"),
    (2024, "bud_hziv_mediprima_2024", 95000000, "CAAMI Mediprima 95.0m 2024"),
    (2024, "bud_hziv_assures_2024", 166978, "CAAMI assures 166978 2024 (COUNT)"),
]
for y, bid, amt, note in rows_data:
    ent = "rjv"
    if "fedris" in bid:
        ent = "fedris"
    elif "hziv" in bid:
        ent = "hziv"
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": ent,
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_ccrek_ss_182e_onva_2025",
            "confidence": "strong",
            "notes": note,
        }
    )

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": "cmt_onva_pecules_2024",
            "title": "ONVA annual leave holiday pay pecules dual CSV 2022-2024",
            "entity_id": "rjv",
            "beneficiary": "1.66m manual workers + artists via ONVA-caisse + 9 private CSV",
            "legal_basis": "Lois coordonnees 28 juin 1971 vacances annuelles; hors Gestion globale; ESA S.1311",
            "decision_date": "2024-01-01",
            "start_year": 2022,
            "end_year": 2024,
            "total_envelope_eur": 18019900000,
            "cash_by_year": '{"2022":5654800000,"2023":5983900000,"2024":6381200000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "stated_goal": "Pay annual holiday allowance for blue-collar and assimilated workers",
            "cut_option": "Not abolish; dual CSV admin fee transparency; fix droits constates accounting; FFE loan path",
            "source_id": "src_ccrek_ss_182e_onva_2025",
            "confidence": "strong",
            "hierarchy_path": "SS>ONVA>pecules_vacances",
            "notes": "tick387: 6.381bn dep 2024; pecules 6.339 ONVA64pct CSV36pct; FFE loan 200m; FOI CSV L5",
        },
        {
            "commitment_id": "cmt_onva_ffe_loan_200m_2024",
            "title": "FFE interest-free loan to ONVA 200m 2024 (15y repay from 2029)",
            "entity_id": "rjv",
            "beneficiary": "ONVA reserves post-covid/Ukraine assimilation",
            "legal_basis": "Loi-programme 22 dec 2023 art.94-99",
            "decision_date": "2024-01-01",
            "start_year": 2024,
            "end_year": 2043,
            "total_envelope_eur": 200000000,
            "cash_by_year": '{"2024":200000000,"2029":-20000000}',
            "remaining_eur": 200000000,
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "stated_goal": "Stabilise ONVA reserves after temporary unemployment assimilation costs",
            "cut_option": "Track repay schedule; dual FFE-ONVA transparency",
            "source_id": "src_ccrek_ss_182e_onva_2025",
            "confidence": "strong",
            "hierarchy_path": "SS>FFE>loan_ONVA",
            "notes": "tick387: 200m no interest; first repay 20m from 2029 over 15y",
        },
    ],
)

lbs = [
    (
        "lb_onva_dep_6_38bn_2024",
        "ONVA annual leave expenditures 6.38bn 2024",
        6381200000,
        "Strong CoA Table11: dep 6381.2m rec 6481.3m solde +100.1m; dual ESA S1311 not SS S1314",
        2,
        9.0,
        3,
        6.35,
        "Core worker entitlement financed by employer cotis; dual CSV opacity",
        "transfer",
        "strong",
    ),
    (
        "lb_onva_pecules_6_34bn_2024",
        "ONVA pecules package ONVA-caisse+CSV 6.34bn 2024",
        6338500000,
        "Strong: 6338.5m pecules; ONVA-caisse 64.1pct ~4063m; 9 private CSV ~2276m",
        3,
        9.0,
        4,
        6.30,
        "Open named CSV cash L5 dual gap_onva_csv_l5",
        "transfer",
        "strong",
    ),
    (
        "lb_onva_csv_private_2_28bn_2024",
        "Private holiday funds CSV transfers 2.28bn 2024",
        csv_2024,
        "Strong: ~2275.5m to 9 sectoral private CSV; dual ONVA-caisse public; per-CSV Unknown FOI",
        5,
        8.0,
        5,
        6.20,
        "Publish per-CSV EUR + admin fees",
        "transfer",
        "strong",
    ),
    (
        "lb_onva_cotis_5_70bn_2024",
        "ONVA employer cotisations 5.70bn 2024",
        5698500000,
        "Strong: patronales 5698.5m via ONSS (15.84pct of 108pct brut); 87.9pct of ONVA rec",
        2,
        8.5,
        3,
        6.18,
        "Monitor rate/base; dual ONSS transfer timing CoA flags",
        "transfer",
        "strong",
    ),
    (
        "lb_onva_ffe_loan_200m_2024",
        "FFE loan to ONVA 200m interest-free 2024",
        200000000,
        "Strong: unique 200m 0pct 15y from 2029; post-covid assimilation reserve hole",
        6,
        7.0,
        4,
        6.00,
        "Publish repay schedule + reserve path",
        "ops",
        "strong",
    ),
    (
        "lb_onva_beheer_24m_2023",
        "ONVA management costs 23.6m 2023",
        23600000,
        "Strong Table27: gestion 23.6m; dual private CSV admin residual FOI",
        4,
        4.5,
        4,
        4.85,
        "FOI beheer 2024-25 + CSV fees",
        "ops",
        "strong",
    ),
    (
        "lb_fedris_596m_2024",
        "Fedris occupational risks 596.4m 2024",
        596400000,
        "Strong Table8: AT 327.1 + MP 214.8 + hors GG 54.5 (amiante 23.6); path 568.6-596.4",
        3,
        7.0,
        4,
        5.55,
        "Volume AT growth transparency; dual private insurers capitalisation residual",
        "transfer",
        "strong",
    ),
    (
        "lb_hziv_missions_643m_2024",
        "CAAMI/HZIV missions 642.6m 2024",
        642600000,
        "Strong Table10: AMI 534.4 Mediprima 95; dual public mutual vs landsbond",
        4,
        7.0,
        4,
        5.70,
        "Unit cost vs landsbond; Mediprima invoice control",
        "transfer",
        "strong",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ, conf in lbs:
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "SS>ONVA>" + iid.replace("lb_", "") if "onva" in iid or "csv" in iid else (
                "SS>Fedris>" + iid if "fedris" in iid else "SS>HZIV>" + iid
            ),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": conf,
            "source_id": "src_ccrek_ss_182e_onva_2025",
            "beneficiaries": "Blue-collar holiday pay / occupational risks / public mutual",
            "stated_goal": "Statutory holiday pay or occupational risk insurance",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick387",
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

Aan: Rijksdienst voor Jaarlijkse Vakantie (RJV) / Office national des vacances annuelles (ONVA)
t.a.v. dienst openbaarheid van bestuur
E-mail: via contactformulier onva-rjv.fgov.be of actuele openbaarheid-mailbox

Betreft: Openbaarmaking — transfers naar 9 CSV, beheer 2024-2025, FFE-lening

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. **Cash per caisse speciale de vacances (CSV)** 2022-2025: naam CSV, sector,
   bedrag transfer van ONVA, eventuele adminvergoeding/commissie.
2. **Budget/rekeningen van beheer (gestion)** ONVA 2023-2025 (personeel, werking, ICT).
3. **Overeenkomst/lening FFE 200 miljoen euro** (2024): contract, aflossingsplan,
   impact op reserves.
4. Eventuele **evaluaties** unit-cost per begunstigde of per euro pécule.

Periode: 2022-01-01 tot 2025-12-31.
Intern pad: SS > ONVA > CSV_L5. Ref: {GAP}

Context (publiek CoA Cahier 2025):
- uitgaven 6.381,2 miljoen (2024); pécules 6.338,5 miljoen;
- ONVA-caisse ~64,1%; 9 private CSV rest;
- FFE-lening 200 miljoen 0% over 15 jaar vanaf 2029.
Ontbreekt: L5 per CSV in euro.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling ONVA/RJV
- [x] Concrete L5 (CSV named + beheer + FFE loan)
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
            "hierarchy_path": "SS>ONVA>CSV_L5",
            "entity_id": "rjv",
            "what_is_missing": "Named 9 private CSV holiday funds cash-by-year 2022-25 + admin fees; ONVA beheer 2024-25; FFE 200m loan contract schedule",
            "why_it_matters": "2.28bn private CSV dual opacity inside 6.34bn pecules; CoA accounting flags; FFE loan unique",
            "priority": 6,
            "recipient_body": "ONVA / RJV",
            "recipient_email": "",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_onva_pecules_2024",
            "linked_leaderboard_id": "lb_onva_csv_private_2_28bn_2024",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick387 CoA fill; residual CSV named L5 human send",
        }
    ],
)

# entities
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("entity_id") == "rjv":
        row["notes"] = (
            "Worker holiday pay; dep 6.381bn rec 6.481bn 2024; pecules 6.339bn "
            "ONVA-caisse 64pct + 9 CSV; beheer 23.6m 2023; FFE loan 200m; ESA S1311; "
            f"FOI {GAP}; tick387"
        )
    if row.get("entity_id") == "fedris":
        row["notes"] = (
            "Work accidents occupational diseases; total 596.4m 2024 "
            "(AT 327.1 MP 214.8 hors 54.5 amiante 23.6); beheer 54.2m 2023; tick387 CoA"
        )
    if row.get("entity_id") == "hziv":
        row["notes"] = (
            "Public mutual VI; missions 642.6m 2024 AMI 534.4 Mediprima 95; "
            "beheer 38.8m 2023; dual landsbond; tick387 CoA"
        )
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
            "tick387: ONVA 6.381bn dep pecules 6.339 dual CSV 2.28bn; FFE loan 200m; "
            "Fedris 596m CAAMI 643m; FOI CSV L5; spawn rq_379"
        )
        break
if not any(x["task_id"] == "rq_379" for x in rq):
    rq.append(
        {
            "task_id": "rq_379",
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
            "notes": "Spawned tick387 after ONVA/Fedris/CAAMI L5; rq_116 SWA deferred",
        }
    )
rewrite(DATA / "research_queue.csv", rq, list(rq_fields))

# state
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
        "notes": "Scheduler 60s. Next prio5 rq_379; rq_116 SWA deferred. FOI ready. tick387 ONVA 6.38bn dual CSV.",
    }
)
rewrite(DATA / "loop_state.csv", st, list(stf))

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **ONVA/RJV pecules vacances dual CSV + Fedris/CAAMI CoA L5**)
- Found (strong primary CoA Cahier 2025 SS Tables 8/10/11/27):
  - ONVA **dep EUR 6,381.2m** / rec **6,481.3m** / solde **+100.1m** 2024
  - Pecules **6,338.5m**: ONVA-caisse **~64.1% (~4,063m)** · 9 private CSV **~2,276m**
  - Cotis patronales **5,698.5m** · ONEM contrib **30.7m** · **FFE loan 200m** 0% 15y
  - Beheer **23.6m** 2023; beneficiaires **1,661,304** ouvriers 2024
  - Fedris **596.4m** (AT 327.1 MP 214.8 amiante 23.6) · CAAMI missions **642.6m**
- Wrote: sources +1; budgets +{len(budgets)}; cmt +2; lb +{len(lb_rows)}; entities; FOI **{GAP}** ready; rq_378=done; spawn **rq_379**; ticks={TICK}
- FOI: named CSV cash + beheer 2024-25 + FFE contract human send only
- Next: prio5 **rq_379**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)
