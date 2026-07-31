# tick386: RSVZ/INASTI gestion globale independants + dual CAS L5
from pathlib import Path
import csv
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"
NOW = "2026-08-01T07:45:00Z"
TICK = 386
UNIT = "rq_377"
GAP = "gap_rsvz_cas_admin_l5"


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
            "source_id": "src_ccrek_ss_182e_inasti_2025",
            "title": "Cour des comptes Cahier 2025 SS — INASTI + gestion globale independants 2022-2024",
            "url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "publisher": "Cour des comptes / Rekenhof",
            "accessed_date": "2026-08-01",
            "source_class": "primary_audit",
            "notes": "Table31 INASTI beheer 106.9m 2023 missions 9.71bn; GG indep dep 6.52bn rec 10.29bn cotis 5.63bn 2024; unpaid 1.55bn hors bilan",
        },
        {
            "source_id": "src_rsvz_chiffres_tendances_2024",
            "title": "RSVZ/INASTI Chiffres et tendances 2024 — affiliates CAS societes",
            "url": "https://www.rsvz.be/sites/rsvz/files/2025-05/Chiffres_et_tendances_2024.pdf",
            "publisher": "RSVZ / INASTI",
            "accessed_date": "2026-08-01",
            "source_class": "primary_report",
            "notes": "1.299825 independants; ACERTA 341k XERIUS 247k LIANTIS 241k; societes 707073; pensionnes 611342",
        },
    ],
)

budgets = []

# GG independants multi-year
gg_rows = [
    # year, dep, pens, inv, rec, cot, solde
    (2022, 5544200000, 4698900000, 722800000, 8615800000, 4843600000, -884300000),
    (2023, 6011800000, 5211200000, 822100000, 9757400000, 5333700000, 425900000),
    (2024, 6523100000, 5597800000, 915400000, 10293000000, 5627800000, -71400000),
]
for y, dep, pens, inv, rec, cot, solde in gg_rows:
    for bid, amt, note in [
        (f"bud_gg_indep_dep_{y}", dep, f"Gestion globale independants depenses consolidees {dep/1e6:.1f}m CoA SPF SS"),
        (f"bud_gg_indep_pens_{y}", pens, f"GG indep pensions {pens/1e6:.1f}m (paid via FPD dual)"),
        (f"bud_gg_indep_invalidite_{y}", inv, f"GG indep invalidite/incapacite {inv/1e6:.1f}m"),
        (f"bud_gg_indep_rec_{y}", rec, f"GG indep recettes consolidees {rec/1e6:.1f}m"),
        (f"bud_gg_indep_cotis_{y}", cot, f"GG indep cotisations sociales {cot/1e6:.1f}m"),
        (f"bud_gg_indep_solde_{y}", solde, f"GG indep solde provisoire {solde/1e6:.1f}m"),
    ]:
        budgets.append(
            {
                "budget_id": bid,
                "entity_id": "rsvz",
                "year": y,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "outturn",
                "source_id": "src_ccrek_ss_182e_inasti_2025",
                "confidence": "strong",
                "notes": note,
            }
        )

extra = [
    (2024, "bud_gg_indep_cotis_personnes_2024", 5322300000, "Cotisations independants personnes 5322.3m 2024 (94.57pct)", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_cotis_societes_2024", 297900000, "Cotisations societes 297.9m 2024 (5.29pct)", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_cotis_other_2024", 7500000, "Cotisations mandataires + 2e pilier 7.5m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_dot_ordinaire_2024", 457600000, "Dotation ordinaire Etat INASTI-GG 457.6m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_dot_equilibre_2024", 477500000, "Dotation equilibre Etat INASTI-GG 477.5m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_dot_total_2024", 935100000, "Dotations Etat total INASTI-GG 935.1m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2022, "bud_gg_indep_dot_total_2022", 860000000, "Dotations Etat INASTI-GG 860.0m 2022", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_gg_indep_dot_total_2023", 1190900000, "Dotations Etat INASTI-GG 1190.9m 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_altfin_2024", 3650900000, "Financement alternatif INASTI-GG 3650.9m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2022, "bud_gg_indep_altfin_2022", 2898500000, "Altfin INASTI-GG 2898.5m 2022", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_gg_indep_altfin_2023", 3180700000, "Altfin INASTI-GG 3180.7m 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_altfin_tva_base_2024", 1794600000, "Altfin TVA base 1794.6m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_altfin_pm_2024", 1182400000, "Altfin precompte mobilier 1182.4m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_altfin_sante_2024", 673900000, "Altfin TVA soins sante 673.9m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_droit_passerelle_2024", 4700000, "Droit passerelle 4.7m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_gg_indep_encours_societes_2024", 133500000, "Encours cotisations societes 133.5m EOY 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2022, "bud_inasti_missions_dep_2022", 9550700000, "INASTI depenses missions 9550.7m 2022 CoA comptes", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_missions_dep_2023", 9712400000, "INASTI depenses missions 9712.4m 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2022, "bud_inasti_missions_rec_2022", 8731000000, "INASTI recettes missions 8731.0m 2022", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_missions_rec_2023", 9901000000, "INASTI recettes missions 9901.0m 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2022, "bud_inasti_beheer_2022", 92200000, "INASTI depenses gestion 92.2m 2022", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_beheer_2023", 106900000, "INASTI depenses gestion 106.9m 2023 (+16pct)", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_beheer_rec_2023", 6800000, "INASTI recettes gestion 6.8m 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_unpaid_cotis_2023", 1552600000, "Cotisations impayees hors bilan 1552.6m EOY 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2023, "bud_inasti_unpaid_ind_2023", 104900000, "Indemnites non remboursees hors bilan 104.9m EOY 2023", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_ss_consol_dep_2024", 139257400000, "SS depenses consolidees 139257.4m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_ss_consol_rec_2024", 139794800000, "SS recettes consolidees 139794.8m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_ss_consol_solde_2024", 537300000, "SS solde provisoire +537.3m 2024", "src_ccrek_ss_182e_inasti_2025"),
    (2024, "bud_ss_frais_gestion_2024", 2790600000, "SS frais de gestion consolides 2790.6m 2024", "src_ccrek_ss_182e_inasti_2025"),
    # counts
    (2024, "bud_rsvz_affilies_2024", 1299825, "Independants affiliates 1299825 EOY 2024 (+20655; COUNT unit)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_act_principale_2024", 801544, "Activite principale 801544 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_act_compl_2024", 341591, "Activite complementaire 341591 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_apres_pension_2024", 156690, "Actifs apres pension 156690 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_societes_2024", 707073, "Societes redevables cotisation 707073 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_pensionnes_2024", 611342, "Pensionnes regime indep 611342 1.1.2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_starters_2024", 123088, "Starters 123088 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_stoppers_2024", 67188, "Stoppers 67188 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_etudiants_2024", 8716, "Etudiants-independants 8716 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_rsvz_conjoints_2024", 15620, "Conjoints aidants 15620 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_acerta_aff_2024", 341015, "CAS ACERTA affiliates 341015 2024 largest private (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_xerius_aff_2024", 246581, "CAS XERIUS 246581 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_liantis_aff_2024", 241349, "CAS LIANTIS 241349 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_partena_aff_2024", 136304, "CAS PARTENA 136304 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_securex_aff_2024", 138509, "CAS SECUREX INTEGRITY 138509 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_ucm_aff_2024", 118026, "CAS UCM Wallonne 118026 2024 (COUNT)", "src_rsvz_chiffres_tendances_2024"),
    (2024, "bud_cas_cna_aff_2024", 8721, "Caisse nationale auxiliaire CNA 8721 2024 public residual (COUNT)", "src_rsvz_chiffres_tendances_2024"),
]
for y, bid, amt, note, src in extra:
    budgets.append(
        {
            "budget_id": bid,
            "entity_id": "rsvz",
            "year": y,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "outturn",
            "source_id": src,
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
            "commitment_id": "cmt_rsvz_gg_indep_2024",
            "title": "INASTI gestion globale independants + dual CAS 2022-2024",
            "entity_id": "rsvz",
            "beneficiary": "1.3m independants + 0.7m societes + 0.61m pensionnes indep",
            "legal_basis": "Loi 21 dec 1970 INASTI; AR CAS; gestion financiere globale independants",
            "decision_date": "2024-01-01",
            "start_year": 2022,
            "end_year": 2024,
            "total_envelope_eur": 18079100000,
            "cash_by_year": '{"2022":5544200000,"2023":6011800000,"2024":6523100000}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.ccrek.be/sites/default/files/Docs/182e_c_II_SecSoc.pdf",
            "stated_goal": "Collect cotisations and finance self-employed social security branches",
            "cut_option": "Open CAS admin fee L5; recover unpaid 1.55bn; dual process efficiency with FPD",
            "source_id": "src_ccrek_ss_182e_inasti_2025",
            "confidence": "strong",
            "hierarchy_path": "SS>RSVZ>gestion_globale_independants",
            "notes": "tick386: GG dep 6.52bn 2024 pens 5.60 invalidite 0.92; cotis 5.63; beheer 106.9 2023; FOI CAS admin",
        }
    ],
)

lbs = [
    (
        "lb_gg_indep_dep_6_52bn_2024",
        "Gestion globale independants dep 6.52bn 2024",
        6523100000,
        "Strong CoA: 6.523bn prestations GG indep (+8.5pct); pens 5.598 + inv 0.915",
        2,
        9.0,
        3,
        6.35,
        "Core entitlement; dual FPD payment",
        "transfer",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_gg_indep_cotis_5_63bn_2024",
        "INASTI GG cotisations 5.63bn 2024",
        5627800000,
        "Strong: cotis 5.628bn (personnes 5.322 societes 0.298); dual private CAS collection",
        3,
        8.5,
        4,
        6.13,
        "Open CAS collection unit costs L5",
        "transfer",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_gg_indep_altfin_3_65bn_2024",
        "INASTI GG financement alternatif 3.65bn 2024",
        3650900000,
        "Strong: altfin 3650.9m TVA+PM+sante path from 2898m 2022",
        3,
        8.0,
        4,
        5.95,
        "Tax-financed SS wedge transparency",
        "transfer",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_inasti_missions_9_71bn_2023",
        "INASTI missions depenses 9.71bn 2023",
        9712400000,
        "Strong CoA comptes: missions 9712.4m / beheer 106.9m; dual GG perimeter narrower",
        3,
        9.0,
        4,
        6.30,
        "Publish 2024-25 comptes certification path",
        "transfer",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_inasti_unpaid_1_55bn_2023",
        "INASTI unpaid cotisations hors bilan 1.55bn 2023",
        1552600000,
        "Strong CoA: 1552.6m cotis unpaid + 104.9m indemnites; not on annual accounts balance",
        7,
        8.0,
        5,
        6.70,
        "Force CAS recovery transparency + class 0 in accounts",
        "ops",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_inasti_beheer_107m_2023",
        "INASTI beheer/gestion 106.9m 2023",
        106900000,
        "Strong: gestion 106.9m (+16pct vs 92.2); dual private CAS admin fees residual FOI",
        4,
        6.5,
        4,
        5.55,
        "FOI 2024-25 beheer + CAS rem fees",
        "ops",
        "strong",
        "src_ccrek_ss_182e_inasti_2025",
    ),
    (
        "lb_cas_dual_private_2024",
        "Private social insurance funds dual CAS 9 entities 2024",
        "",
        "Strong RSVZ: 1.30m affiliates across 8 private CAS + CNA; ACERTA 341k largest; admin fees Unknown FOI",
        6,
        5.0,
        5,
        5.40,
        "Publish CAS admin fee EUR per affiliate L5",
        "ops",
        "medium",
        "src_rsvz_chiffres_tendances_2024",
    ),
]
lb_rows = []
for iid, name, cost, tco, ab, cs, df, pi, cut, typ, conf, src in lbs:
    lb_rows.append(
        {
            "item_id": iid,
            "name": name,
            "level": "federal",
            "type": typ,
            "hierarchy_path": "SS>RSVZ>" + iid.replace("lb_", ""),
            "annual_cost_eur": cost,
            "total_cost_eur": cost,
            "tco_notes": tco,
            "confidence": conf,
            "source_id": src,
            "beneficiaries": "Self-employed SS system",
            "stated_goal": "Self-employed social insurance",
            "measured_outcome": tco[:90],
            "absurdity_score": ab,
            "cost_score": cs,
            "difficulty": df,
            "priority_index": pi,
            "cut_proposal": cut,
            "status": "seed",
            "struck_reason": "",
            "notes": "tick386",
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

Aan: Rijksinstituut voor de Sociale Verzekeringen der Zelfstandigen (RSVZ) / INASTI
t.a.v. dienst openbaarheid van bestuur
E-mail: info@rsvz-inasti.fgov.be (of actuele openbaarheid-mailbox)

Betreft: Openbaarmaking — beheer RSVZ 2024-2025, adminvergoedingen CAS, invordering cotisations

Geachte,

Op grond van de wet 11 april 1994 openbaarheid van bestuur vraag ik afschrift van:

1. Budget/rekeningen van beheer (gestion) RSVZ/INASTI 2023-2025:
   personeel, werking, ICT/Smals, investeringen (L5).
2. Vergoedingen / commissies / adminkosten die de caisses d'assurances sociales (CAS)
   ontvangen of inhouden voor inning van sociale bijdragen, per CAS en per jaar 2022-2025
   (ACERTA, XERIUS, LIANTIS, PARTENA, SECUREX, UCM, GROUP S, AVIXI, CNA).
3. Invorderingsstatistieken: uitstaande cotisations per CAS (aansluiting op hors-bilan
   1.552,6 miljoen euro eind 2023) en inningen 2024-2025.
4. Eventuele evaluaties unit-cost per aangeslotene of per euro geind.

Periode: 2022-01-01 tot 2025-12-31.
Intern pad: SS > RSVZ > CAS_admin_L5. Ref: {GAP}

Context (publiek): CoA beheer 106,9m 2023; GG indep 6,52bn dep / 5,63bn cotis 2024;
1.299.825 aangeslotenen; CAS-markt top ACERTA 341k. Ontbreekt: CAS-admin in euro L5.

Vorm: PDF/CSV per e-mail naar [e-mail].

Met vriendelijke groet,
[Naam]
```

## Checklist
- [x] Instelling RSVZ/INASTI
- [x] Concrete L5 (beheer + CAS fees + arrears)
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
            "hierarchy_path": "SS>RSVZ>CAS_admin_L5",
            "entity_id": "rsvz",
            "what_is_missing": "RSVZ beheer EUR L5 2024-25; CAS admin fees/commissions per fund 2022-25; unpaid cotisations recovery path vs 1.55bn hors bilan",
            "why_it_matters": "Private dual CAS collect 5.6bn cotis; admin fee opacity; CoA flags unpaid 1.55bn off-balance",
            "priority": 6,
            "recipient_body": "RSVZ / INASTI",
            "recipient_email": "info@rsvz-inasti.fgov.be",
            "recipient_postal": "",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-01",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": "cmt_rsvz_gg_indep_2024",
            "linked_leaderboard_id": "lb_inasti_unpaid_1_55bn_2023",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick386 public fill CoA+RSVZ trends; residual CAS fees human send",
        }
    ],
)

# entity
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("entity_id") == "rsvz":
        row["notes"] = (
            "Self-employed SS; GG indep dep 6.52bn cotis 5.63bn 2024 strong CoA; "
            "beheer 106.9m 2023; 1.30m affiliates dual CAS; unpaid 1.55bn hors bilan; "
            f"FOI {GAP}; tick386"
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
            "tick386: GG indep 6.52bn dep 5.63 cotis; INASTI missions 9.71 beheer 106.9; "
            "dual CAS L5 counts; unpaid 1.55bn; FOI CAS admin; spawn rq_378"
        )
        break
if not any(x["task_id"] == "rq_378" for x in rq):
    rq.append(
        {
            "task_id": "rq_378",
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
            "notes": "Spawned tick386 after RSVZ/INASTI L5; rq_116 SWA deferred",
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
        "notes": "Scheduler 60s. Next prio5 rq_378; rq_116 SWA deferred. FOI ready. tick386 RSVZ GG indep 6.52bn.",
    }
)
rewrite(DATA / "loop_state.csv", st, list(stf))

log = f"""
### {NOW} - tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill - **RSVZ/INASTI gestion globale independants + dual CAS L5**)
- Found (strong primary CoA Cahier 2025 SS + RSVZ Chiffres 2024):
  - GG indep **dep EUR 6,523.1m 2024** (pens 5,597.8 · invalidite 915.4 · path 5.54/6.01/6.52)
  - GG indep **rec 10,293.0m** · **cotis 5,627.8m** (personnes 5,322.3 · societes 297.9) · solde **-71.4m**
  - Dotations Etat **935.1m** · altfin **3,650.9m** · unpaid hors bilan **1,552.6m** cotis + **104.9m**
  - INASTI missions **9,712.4m** / beheer **106.9m** 2023
  - Affiliates **1,299,825** · CAS top ACERTA 341k · XERIUS 247k · LIANTIS 241k · societes 707k
- Wrote: sources +2; budgets +{len(budgets)}; cmt +1; lb +{len(lb_rows)}; entity; FOI **{GAP}** ready; rq_377=done; spawn **rq_378**; ticks={TICK}
- FOI: CAS admin fees + beheer 2024-25 + recovery path human send only
- Next: prio5 **rq_378**; deferred **rq_116** SWA
"""
with (REPO / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log)
print("DONE tick", TICK)
