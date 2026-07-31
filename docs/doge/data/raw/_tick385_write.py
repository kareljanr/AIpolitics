# tick385: FPD/SFP legal pensions L5 — PensionStat 2019-2025 + JV2024 kerncijfers
from pathlib import Path
import csv
import os
from datetime import datetime, timezone

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T07:15:00Z"
TICK = 385
UNIT = "rq_376"


def append_rows(path: Path, rows: list[dict], fieldnames: list[str] | None = None):
    if not rows:
        return
    exists = path.exists() and path.stat().st_size > 0
    if fieldnames is None:
        with path.open(encoding="utf-8", newline="") as f:
            r = csv.DictReader(f)
            fieldnames = r.fieldnames
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        if not exists:
            w.writeheader()
        for row in rows:
            w.writerow(row)


# --- sources ---
src_rows = [
    {
        "source_id": "src_pensionstat_depenses_2025",
        "title": "PensionStat.be depenses annuelles legales 2019-2025 (XLSX data-2025-fr)",
        "url": "https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
        "publisher": "Service federal des Pensions / PensionStat",
        "accessed_date": "2026-08-01",
        "source_class": "primary_official",
        "notes": "XLSX sheet Depenses_annuelles: total 69.047bn 2025 / 66.475bn 2024; regime Sal/Fonct/Ind; raw pensionstat_data_2025_fr.xlsx",
    },
    {
        "source_id": "src_fpd_jv2024_kerncijfers",
        "title": "FPD Jaarverslag 2024 kerncijfers + P&O staff",
        "url": "https://www.sfpd.fgov.be/files/3438/jaarverslag2024-kerncijfers.pdf",
        "publisher": "Federale Pensioendienst",
        "accessed_date": "2026-08-01",
        "source_class": "primary_report",
        "notes": "Paid 68.245bn 2024 WN40.2 Amb22.45 ZS5.59; budgetary total 69.4bn incl Ethias+IGO; staff 2165/2013.75 FTE Smals174; dual pensionstat",
    },
]
append_rows(DATA / "sources.csv", src_rows)

# --- budgets ---
# amounts in EUR full
budgets = []

# multi-year totals PensionStat
path_totals = {
    2019: 48292082943,
    2020: 50053777862,
    2021: 51763305375,
    2022: 57405837331,
    2023: 62783328907,
    2024: 66475420983,
    2025: 69047091066,
}
for y, amt in path_totals.items():
    budgets.append(
        {
            "budget_id": f"bud_pension_legal_total_{y}",
            "entity_id": "fpd",
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_pensionstat_depenses_2025",
            "confidence": "strong",
            "notes": f"PensionStat depenses annuelles 3 regimes sum EUR {amt/1e9:.3f}bn; rights-based legal pensions (not Ethias/IGO full package)",
        }
    )

# regime 2024-2025
regimes = {
    2024: {
        "sal": 38370440000,
        "fonct": 22517466000,
        "ind": 5587515000,
    },
    2025: {
        "sal": 39880868000,
        "fonct": 23428508000,
        "ind": 5737715000,
    },
}
for y, d in regimes.items():
    for key, label, amt in [
        ("sal", "Salaries/werknemers legal pensions", d["sal"]),
        ("fonct", "Fonctionnaires/ambtenaren legal pensions", d["fonct"]),
        ("ind", "Independants/zelfstandigen legal pensions", d["ind"]),
    ]:
        budgets.append(
            {
                "budget_id": f"bud_pension_{key}_{y}",
                "entity_id": "fpd",
                "year": y,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "outturn",
                "source_id": "src_pensionstat_depenses_2025",
                "confidence": "strong",
                "notes": f"{label} {amt/1e6:.1f}m PensionStat",
            }
        )

# type retraite/survie 2024-2025
types = {
    2024: {"retraite": 57985249000, "survie": 8490172000},
    2025: {"retraite": 60519012000, "survie": 8528079000},
}
for y, d in types.items():
    for key, label, amt in [
        ("retraite", "Retirement pensions all regimes", d["retraite"]),
        ("survie", "Survivor + transition pensions all regimes", d["survie"]),
    ]:
        budgets.append(
            {
                "budget_id": f"bud_pension_{key}_{y}",
                "entity_id": "fpd",
                "year": y,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "outturn",
                "source_id": "src_pensionstat_depenses_2025",
                "confidence": "strong",
                "notes": f"{label} {amt/1e6:.1f}m PensionStat",
            }
        )

# detail top L5 2025
details_2025 = [
    ("sal_retraite", 34046283000, "Pension de retraite salarie 34046.3m"),
    ("fonct_retraite", 21444264000, "Pension de retraite fonctionnaire 21444.3m"),
    ("sal_survie", 5410607000, "Pension de survie salarie 5410.6m"),
    ("ind_retraite", 4485835000, "Pension de retraite independant 4485.8m"),
    ("fonct_survie", 1977215000, "Pension de survie fonctionnaire 1977.2m"),
    ("ind_survie", 1039566000, "Pension de survie independant 1039.6m"),
    ("autres", 580014000, "Autres prestations 580.0m"),
    ("alloc_trans_sal", 49375000, "Allocation de transition salarie 49.4m"),
]
for key, amt, note in details_2025:
    budgets.append(
        {
            "budget_id": f"bud_pension_l5_{key}_2025",
            "entity_id": "fpd",
            "year": 2025,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_pensionstat_depenses_2025",
            "confidence": "strong",
            "notes": note,
        }
    )

# min-pension beneficiary total spend
for y, amt in [(2024, 20292733000), (2025, 20751917000)]:
    budgets.append(
        {
            "budget_id": f"bud_pension_min_beneficiary_spend_{y}",
            "entity_id": "fpd",
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": "src_pensionstat_depenses_2025",
            "confidence": "strong",
            "notes": f"Total pension spend for min-pension beneficiaries {amt/1e6:.1f}m (sheet PensionsMin_depenses; subset not additive to total)",
        }
    )

# FPD JV2024 payment vs budgetary package
budgets += [
    {
        "budget_id": "bud_fpd_paid_pensions_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 68244925000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "FPD JV2024 paid rust+overleving 68.245bn to >2.6m pensioners (method differs from PensionStat 66.475bn)",
    },
    {
        "budget_id": "bud_fpd_paid_wn_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 40200140000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Werknemers 40.200bn JV2024",
    },
    {
        "budget_id": "bud_fpd_paid_ambt_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 22451291000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Ambtenaren 22.451bn JV2024",
    },
    {
        "budget_id": "bud_fpd_paid_zs_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 5593494000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Zelfstandigen 5.593bn JV2024 (RSVZ berekent/toekent; FPD betaalt)",
    },
    {
        "budget_id": "bud_fpd_budgetary_package_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 69400000000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Totale budgettaire uitgave 69.4bn = 68.2 paid + Ethias municipal/prov + IGO + AO/oorlogsrenten residual FOI split",
    },
    {
        "budget_id": "bud_fpd_staff_headcount_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 2165,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Headcount 2165 EOY 2024 (not EUR; count unit) — 2013.75 FTE; NL 1040 FR 1125; women 1381 men 847",
    },
    {
        "budget_id": "bud_fpd_staff_fte_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 2014,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "FTE 2013.75 rounded 2014 (count unit not EUR)",
    },
    {
        "budget_id": "bud_fpd_smals_staff_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 174,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "Smals staff seconded 174 (count unit); dual ONSS/RVA Smals path",
    },
    {
        "budget_id": "bud_fpd_min_pension_beneficiaries_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 997562,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "strong",
        "notes": "997562 pensioners on minimum (Jan2024 / 2023 figures class) = 41pct of cohort (count unit)",
    },
    {
        "budget_id": "bud_fpd_pension_rights_count_2024",
        "entity_id": "fpd",
        "year": 2024,
        "amount_eur": 4300000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "confidence": "medium",
        "notes": "4.3m pension rights paid to 2.62m persons (mixed careers dual rights; count unit)",
    },
    {
        "budget_id": "bud_pension_cadastre_y_2025",
        "entity_id": "fpd",
        "year": 2025,
        "amount_eur": 2097295000,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "outturn",
        "source_id": "src_pensionstat_depenses_2025",
        "confidence": "strong",
        "notes": "Cadastre=Y share 2097.3m 2025 (Fonct 1785.2 + Sal 312.0 + Ind 0.07) residual class vs core N",
    },
]

append_rows(DATA / "budgets.csv", budgets)
print("budgets +", len(budgets))

# --- commitment ---
cmt = {
    "commitment_id": "cmt_fpd_legal_pensions_2025",
    "title": "Legal pensions FPD/PensionStat L5 path 2019-2025",
    "entity_id": "fpd",
    "beneficiary": "2.6-2.7m legal pensioners BE",
    "legal_basis": "Wettelijke pensioenen werknemers/ambtenaren/zelfstandigen; FPD payment + RSVZ award for ZS",
    "decision_date": "2025-01-01",
    "start_year": 2019,
    "end_year": 2025,
    "total_envelope_eur": 405820844167,  # sum path 2019-2025
    "cash_by_year": '{"2019":48292082943,"2020":50053777862,"2021":51763305375,"2022":57405837331,"2023":62783328907,"2024":66475420983,"2025":69047091066}',
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.pensionstat.be/fr/chiffres-cles/pension-legale/plus-en-detail/droits-de-pension/depenses-annuelles",
    "stated_goal": "Pay statutory retirement and survivor pensions three regimes",
    "cut_option": "Not abolish; reform parameters (age/career/min) already in CEV/gov path; open beheer+IGO+Ethias residual",
    "source_id": "src_pensionstat_depenses_2025",
    "confidence": "strong",
    "hierarchy_path": "SS>FPD>legal_pensions",
    "notes": "tick385: 69.05bn 2025 PensionStat; dual FPD JV paid 68.2bn 2024 + package 69.4bn; min-benef spend 20.75bn; FOI beheer IGO Ethias",
}
append_rows(DATA / "commitments.csv", [cmt])
print("cmt +1")

# --- leaderboard ---
# priority_index rough: 0.45*absurd + 0.35*cost + 0.2*(10-diff) scaled /10-ish from prior seeds
lb = [
    {
        "item_id": "lb_fpd_legal_pensions_69bn_2025",
        "name": "Legal pensions PensionStat 69.05bn 2025",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>legal_pensions_2025",
        "annual_cost_eur": 69047091066,
        "total_cost_eur": 69047091066,
        "tco_notes": "Strong PensionStat: 69.047bn 2025 (+3.9pct); path 48.3->69.0 2019-25 (+43pct); dual FPD JV paid 68.2bn 2024 method gap",
        "confidence": "strong",
        "source_id": "src_pensionstat_depenses_2025",
        "beneficiaries": "2.7m pensioners (Jan2025 class)",
        "stated_goal": "Statutory retirement + survivor income three regimes",
        "measured_outcome": "Core entitlement mega; fiscal aging driver not pure waste",
        "absurdity_score": 2,
        "cost_score": 10.0,
        "difficulty": 2,
        "priority_index": 6.90,
        "cut_proposal": "Parameter reform path (CEV); not cut benefits blindly; dual admin transparency",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385 largest SS cash flow after TE pie; dual method FPD JV vs PensionStat",
    },
    {
        "item_id": "lb_fpd_sal_pensions_39_9bn_2025",
        "name": "Employee legal pensions 39.88bn 2025",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>salaries_regime",
        "annual_cost_eur": 39880868000,
        "total_cost_eur": 39880868000,
        "tco_notes": "Strong: Sal 39.881bn 2025 of which retraite 34.046 + survie 5.411",
        "confidence": "strong",
        "source_id": "src_pensionstat_depenses_2025",
        "beneficiaries": "Salaries regime pension rights",
        "stated_goal": "Employee statutory pensions",
        "measured_outcome": "Largest regime share ~58pct of legal total",
        "absurdity_score": 2,
        "cost_score": 10.0,
        "difficulty": 3,
        "priority_index": 6.73,
        "cut_proposal": "Career/assimilation rules transparency; protect earned rights",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385",
    },
    {
        "item_id": "lb_fpd_fonct_pensions_23_4bn_2025",
        "name": "Civil servant legal pensions 23.43bn 2025",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>fonctionnaires_regime",
        "annual_cost_eur": 23428508000,
        "total_cost_eur": 23428508000,
        "tco_notes": "Strong: Fonct 23.429bn 2025 (retraite 21.444 + survie 1.984); dual higher average vs salaries",
        "confidence": "strong",
        "source_id": "src_pensionstat_depenses_2025",
        "beneficiaries": "Public sector pensioners",
        "stated_goal": "Civil service statutory pensions",
        "measured_outcome": "Second regime ~34pct; dual vs private careers",
        "absurdity_score": 3,
        "cost_score": 9.5,
        "difficulty": 4,
        "priority_index": 6.48,
        "cut_proposal": "Continue convergence path; open biennial adaptation cash",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385",
    },
    {
        "item_id": "lb_fpd_min_pension_spend_20_8bn_2025",
        "name": "Min-pension beneficiaries total spend 20.75bn 2025",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>minimum_pension_cohort",
        "annual_cost_eur": 20751917000,
        "total_cost_eur": 20751917000,
        "tco_notes": "Strong PensionStat PensionsMin_depenses 20.752bn 2025; FPD: 997k persons ~41pct cohort Jan2024 class",
        "confidence": "strong",
        "source_id": "src_pensionstat_depenses_2025",
        "beneficiaries": "~1m min-pension pensioners class",
        "stated_goal": "Floor against poverty in old age",
        "measured_outcome": "Subset of legal total not additive; high share of cohort",
        "absurdity_score": 3,
        "cost_score": 9.5,
        "difficulty": 5,
        "priority_index": 6.28,
        "cut_proposal": "Keep floor; target fraud/career authenticity; publish unit cost path",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385 safety-net interface not pure waste",
    },
    {
        "item_id": "lb_fpd_ind_pensions_5_74bn_2025",
        "name": "Self-employed legal pensions 5.74bn 2025",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>independants_regime",
        "annual_cost_eur": 5737715000,
        "total_cost_eur": 5737715000,
        "tco_notes": "Strong: Ind 5.738bn 2025; dual RSVZ award + FPD payment; fastest growth regime class",
        "confidence": "strong",
        "source_id": "src_pensionstat_depenses_2025",
        "beneficiaries": "Self-employed pensioners",
        "stated_goal": "Independent statutory pensions",
        "measured_outcome": "Smallest regime ~8pct; dual agency RSVZ/FPD",
        "absurdity_score": 3,
        "cost_score": 8.5,
        "difficulty": 4,
        "priority_index": 6.13,
        "cut_proposal": "Dual RSVZ-FPD process efficiency; not cut benefits",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385",
    },
    {
        "item_id": "lb_fpd_budgetary_package_69_4bn_2024",
        "name": "FPD budgetary pension package 69.4bn 2024",
        "level": "federal",
        "type": "transfer",
        "hierarchy_path": "SS>FPD>budgetary_package_2024",
        "annual_cost_eur": 69400000000,
        "total_cost_eur": 69400000000,
        "tco_notes": "Strong JV2024: 69.4bn = 68.2 paid + Ethias local regimes + IGO + AO/war rents; residual L5 FOI",
        "confidence": "strong",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "beneficiaries": "Legal + residual local/IGO beneficiaries",
        "stated_goal": "Full budgetary pension-class outlays FPD perimeter",
        "measured_outcome": "Package wider than pure legal rights table",
        "absurdity_score": 3,
        "cost_score": 10.0,
        "difficulty": 4,
        "priority_index": 6.70,
        "cut_proposal": "Open Ethias+IGO+rents L5 cash codes; dual gap_fpd_beheer_igo_l5",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385",
    },
    {
        "item_id": "lb_fpd_staff_dual_2165_2024",
        "name": "FPD staff dual NL/FR 2165 headcount 2024",
        "level": "federal",
        "type": "ops",
        "hierarchy_path": "SS>FPD>beheer_staff",
        "annual_cost_eur": 287700000,  # last known CoA beheer 2023 as scale placeholder class
        "total_cost_eur": 287700000,
        "tco_notes": "Strong staff: 2165 HC / 2014 FTE / Smals 174; beheer EUR still 2023 CoA 287.7m — 2024-25 FOI",
        "confidence": "medium",
        "source_id": "src_fpd_jv2024_kerncijfers",
        "beneficiaries": "FPD administration",
        "stated_goal": "Administer legal pension calculation and payment",
        "measured_outcome": "Dual language org; Smals IT dual other OISZ",
        "absurdity_score": 4,
        "cost_score": 7.5,
        "difficulty": 4,
        "priority_index": 6.08,
        "cut_proposal": "Publish beheer 2024-25 L5 + Smals IT EUR; dual process RSVZ",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick385 cost EUR uses CoA 2023 beheer as scale until FOI; staff counts strong",
    },
]
append_rows(DATA / "leaderboard.csv", lb)
print("lb +", len(lb))

# --- FOI gap ---
gap_id = "gap_fpd_beheer_igo_l5"
draft_path = REPO / "docs/doge/foi/drafts" / f"{gap_id}.md"
draft_path.parent.mkdir(parents=True, exist_ok=True)
draft_path.write_text(
    f"""# FOI draft — {gap_id}

Status: **ready** (human send only). Verify contacts before send. Not legal advice.

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Federale Pensioendienst / Service federal des Pensions (FPD/SFP)
t.a.v. de dienst openbaarheid van bestuur / informatieambtenaar
Zuidertoren / Tour du Midi
Esplanade de l'Europe 1
1060 Brussel
E-mail: communicatie@sfpd.fgov.be (of actuele openbaarheid-mailbox)

Betreft: Verzoek om openbaarmaking — FPD beheer 2024-2025, IGO, Ethias/lokale stelsels, Smals

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

1. **Budget / rekeningen van beheer (gestion)** van de FPD voor begrotingsjaren
   **2023, 2024 en 2025** (of laatst afgesloten), met uitsplitsing:
   - personeelskosten (lonen, RSZ, pensioenen);
   - werkingskosten;
   - investeringen;
   - **Smals / ICT** (bedrag en FTE/personeel).
2. **Inkomensgarantie voor ouderen (IGO / GRAPA)** — kasuitgaven per jaar 2022-2025
   en budgetartikel(en) / basisallocatiecodes.
3. **Pensioenen gemeenten/provincies via Ethias** (of ander orgaan) die in de
   FPD-kerncijfers 2024 tot de **totale budgettaire uitgave 69,4 miljard euro**
   behoren: kas per jaar 2022-2025 en methodologische afbakening t.o.v. de
   68,2 miljard rust- en overlevingspensioenen.
4. **Arbeidsongevallenrenten, oorlogsrenten, vergoedingspensioenen** e.d.
   in dezelfde 69,4 miljard-perimeter: bedragen per categorie 2022-2025.
5. Eventuele **evaluatie- of rekenhofdocumenten** over beheerskost per
   uitbetaalde euro / per dossier (indien bestaand).

Periode: 2022-01-01 tot 2025-12-31 (of alle nog beschikbare afgesloten jaren).

### 2. Context

Publiek beschikbaar (PensionStat + FPD jaarverslag 2024):
- wettelijke pensioenuitgaven PensionStat **69,05 miljard euro (2025)** /
  **66,48 miljard (2024)**;
- FPD-betalingen rust+overleving **68,245 miljard (2024)**;
- budgettaire package **69,4 miljard (2024)** inclusief restcategorieën;
- personeel **2.165** / **2.013,75 VTE** / Smals **174** (EOY 2024);
- beheer in euro openbaar tot en met **2023** (Rekenhof 287,7 miljoen).

Ontbrekend: beheer 2024-2025 in euro L5; IGO-kasreeks; Ethias/lokale en
renten-splitsing binnen 69,4 miljard.

Hiërarchisch pad (intern): SS > FPD > beheer_IGO_Ethias_L5.
Dossierreferentie intern: {gap_id}

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail verzoeker].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met rechtsgrond en beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: {gap_id}

Met vriendelijke groet,

[Naam]
```

## Checklist

- [x] Juiste instelling (FPD/SFP)
- [x] Concrete documenten (beheer L5, IGO, Ethias, rents)
- [x] Periode 2022-2025
- [x] Meerjarigheid gevraagd
- [ ] Contactgegevens verzoeker (mens)
- [x] foi_queue ready (draft complete; human send)
""",
    encoding="utf-8",
)
print("draft", draft_path)

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "SS>FPD>beheer_IGO_Ethias_L5",
    "entity_id": "fpd",
    "what_is_missing": "FPD beheer EUR L5 2024-2025 (pers/werking/invest/Smals); IGO cash-by-year; Ethias municipal/prov + AO/war rents split inside 69.4bn package",
    "why_it_matters": "Legal pensions 69bn mapped strong; residual admin+IGO+local package ~1.2bn+ opacity; dual CoA beheer only to 2023",
    "priority": 6,
    "recipient_body": "Federale Pensioendienst / Service federal des Pensions",
    "recipient_email": "communicatie@sfpd.fgov.be",
    "recipient_postal": "Zuidertoren Esplanade de l'Europe 1 1060 Brussel",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-01",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "cmt_fpd_legal_pensions_2025",
    "linked_leaderboard_id": "lb_fpd_budgetary_package_69_4bn_2024",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick385 public fill PensionStat+JV; residual FOI human send only",
}
append_rows(DATA / "foi_queue.csv", [foi_row])
print("foi +1")

# --- entity note ---
ent_path = DATA / "entities.csv"
with ent_path.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fields = rows[0].keys() if rows else []
for r in rows:
    if r.get("entity_id") == "fpd":
        r["notes"] = (
            "Worker public IGO pensions payment; PensionStat legal 69.05bn 2025 / 66.48bn 2024; "
            "JV2024 paid 68.25bn package 69.4bn; staff 2165/2014 FTE Smals174; beheer CoA 287.7m 2023; "
            "FOI gap_fpd_beheer_igo_l5; tick385"
        )
        break
with ent_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("entity fpd updated")

# --- research queue ---
rq_path = DATA / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as f:
    rq = list(csv.DictReader(f))
    rq_fields = list(rq[0].keys())
for r in rq:
    if r["task_id"] == UNIT:
        r["status"] = "done"
        r["updated_utc"] = NOW
        r["blocked_gap_id"] = gap_id
        r["notes"] = (
            "tick385: PensionStat legal 69.05bn 2025 L5 Sal39.88 Fonct23.43 Ind5.74; "
            "FPD JV paid 68.25 package 69.4 staff 2165; FOI beheer/IGO/Ethias; spawn rq_377"
        )
        break
# spawn next
rq.append(
    {
        "task_id": "rq_377",
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
        "notes": "Spawned tick385 after FPD pensions L5; rq_116 SWA deferred",
    }
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq)
print("rq done + spawn rq_377")

# --- loop_state ---
state_path = DATA / "loop_state.csv"
with state_path.open(encoding="utf-8", newline="") as f:
    st = list(csv.DictReader(f))
    stf = list(st[0].keys())
st[0]["mode"] = "continuous"
st[0]["current_sprint"] = "hole_fill"
st[0]["last_tick_utc"] = NOW
st[0]["last_unit_id"] = UNIT
st[0]["ticks_completed"] = str(TICK)
st[0]["paused"] = "no"
st[0]["notes"] = (
    "Scheduler 60s. Next prio5 rq_377; rq_116 SWA deferred. FOI ready. "
    "tick385 FPD pensions PensionStat 69.05bn 2025."
)
with state_path.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=stf, lineterminator="\n")
    w.writeheader()
    w.writerows(st)
print("loop_state", TICK)

# --- loop log ---
log_path = REPO / "docs/doge/loop_log.md"
entry = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **FPD/SFP legal pensions L5 PensionStat + JV2024**)
- Found (strong primary PensionStat XLSX + FPD jaarverslag 2024):
  - Legal pensions **EUR 69,047.1m 2025** / **66,475.4m 2024** (path 48.3→69.0bn 2019-25)
  - **Sal 39,880.9** · **Fonct 23,428.5** · **Ind 5,737.7** m (2025)
  - Retraite **60,519.0** · Survie **8,528.1** m; min-benef spend **20,751.9** m
  - FPD paid **68,244.9m 2024** (WN 40.2 / Ambt 22.45 / ZS 5.59); package **69.4bn**
  - Staff **2,165** HC / **2,013.75 FTE** / Smals **174**; min pensioners **997,562** (41pct)
- Wrote: sources +2; budgets +{len(budgets)}; cmt +1; lb +{len(lb)}; entity note; FOI **{gap_id}** ready + draft; rq_376=done; spawn **rq_377**; ticks={TICK}
- FOI: beheer 2024-25 + IGO + Ethias/rents inside 69.4bn human send only
- Next: prio5 **rq_377**; deferred **rq_116** SWA
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(entry)
print("log appended")
print("DONE tick", TICK)
