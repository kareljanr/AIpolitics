# tick 235 COCOF + VGC dual structure fill
import csv, os, json

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src_cocof = "src_cocof_budget_2026_coa"
src_vgc = "src_vgc_jaarrekening_2025"
url_cocof = "https://www.ccrek.be/sites/default/files/Docs/2026_21_BI2026_COCOF.pdf"
url_vgc = (
    "https://www.vgc.be/sites/vgc/files/2026-07/"
    "20260710%20Jaarrekening%202025%20Raad%20VGC%2010%20juli%202026%20-%20deel%201.pdf"
)

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src_cocof,
            "Cour des comptes COCOF budgets 2026 (BI) report 31 Mar 2026",
            url_cocof,
            "Cour des comptes Belgique",
            "2026-07-29",
            "court_of_audit",
            "Decret rec 625.6m dep liq 677.5m eng 667.6m; reglement rec 16.1m dep liq 24.3m; SEC -22.7m after sous-util 35.8m; Phare 210.3m; BF 96.2m; debt EOY26 203.7m; tick235; raw cocof_budget_2026_coa.pdf",
        ]
    )
    w.writerow(
        [
            src_vgc,
            "VGC Jaarrekening 2025 Deel I Raad 10 Jul 2026",
            url_vgc,
            "Vlaamse Gemeenschapscommissie",
            "2026-07-29",
            "official_annual_report",
            "Exp outturn 173.6m rec 225.0m saldo 51.3m; inv out 99.5m; debt 242.1m; werksubs 53.9m; dual COCOF; tick235; raw vgc_jaarrekening_2025_deel1.pdf",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cocof",
            "Franse Gemeenschapscommissie COCOF",
            "Commission communautaire francaise COCOF",
            "French Community Commission Brussels",
            "community",
            "brussels_gov",
            "fr",
            "https://ccf.brussels",
            "",
            "",
            "FR community commission dual VGC/COCOM; decret+reglement budgets; Phare handicap; tick235",
        ]
    )
    w.writerow(
        [
            "vgc",
            "Vlaamse Gemeenschapscommissie VGC",
            "Commission communautaire flamande VGC",
            "Flemish Community Commission Brussels",
            "community",
            "brussels_gov",
            "nl",
            "https://www.vgc.be",
            "",
            "",
            "NL community commission dual COCOF/COCOM; BBC MJP; tick235",
        ]
    )
    w.writerow(
        [
            "bruxelles_formation",
            "Bruxelles Formation",
            "Bruxelles Formation",
            "French-speaking Brussels training agency",
            "parastatal",
            "cocof",
            "fr",
            "https://www.bruxellesformation.brussels",
            "",
            "",
            "COCOF OAA; budget 96.2m 2026; dual VDAB/Actiris; tick235",
        ]
    )
    w.writerow(
        [
            "phare_cocof",
            "Phare COCOF personnes handicapees",
            "Phare COCOF personnes handicapees",
            "COCOF disability services agency envelope",
            "agency",
            "cocof",
            "fr",
            "",
            "",
            "",
            "Mission 32 ~210m 2026; L5 residual; tick235",
        ]
    )

rows_b = [
    ("bud_cocof_decret_rec_2026", "cocof", 2026, 625624000, "", "", "budgeted", src_cocof, "strong", "Decret voies et moyens 625.624m: RBC 352.4 FWB 166.8 federal 94.8 divers 7.6 Actiris 3.5"),
    ("bud_cocof_decret_dep_eng_2026", "cocof", 2026, 667610000, "", "", "budgeted", src_cocof, "strong", "Decret eng 667.610m table8"),
    ("bud_cocof_decret_dep_liq_2026", "cocof", 2026, 677505000, "", "", "budgeted", src_cocof, "strong", "Decret liquidation 677.505m headline"),
    ("bud_cocof_regl_rec_2026", "cocof", 2026, 16112000, "", "", "budgeted", src_cocof, "strong", "Reglement rec 16.112m (RBC culture 5.6 CF 10.1 divers 0.4)"),
    ("bud_cocof_regl_dep_liq_2026", "cocof", 2026, 24305000, "", "", "budgeted", src_cocof, "strong", "Reglement dep liq 24.305m eng 24.232m"),
    ("bud_cocof_combined_dep_liq_2026", "cocof", 2026, 701810000, "", "", "budgeted", src_cocof, "strong", "Decret+reglement liq sum 701.810m; not full dual with COCOM/VGC"),
    ("bud_cocof_sec_solde_2026", "cocof", 2026, -22708000, "", "", "budgeted", src_cocof, "strong", "SEC -22.708m after sous-util 35.758m; path 0 by 2029"),
    ("bud_cocof_solde_brut_2026", "cocof", 2026, -60074000, "", "", "budgeted", src_cocof, "strong", "Solde budgetaire brut decret+reglement -60.074m"),
    ("bud_cocof_phare_liq_2026", "cocof", 2026, 210270000, "", "", "budgeted", src_cocof, "strong", "Mission 32 Phare liq 210.270m eng 210.047m ~31.5pct of decret"),
    ("bud_cocof_aide_liq_2026", "cocof", 2026, 113898000, "", "", "budgeted", src_cocof, "strong", "Mission 22 Aide aux personnes liq 113.898m"),
    ("bud_cocof_formation_liq_2026", "cocof", 2026, 91766000, "", "", "budgeted", src_cocof, "strong", "Mission 26 formation pro liq 91.766m incl BF dot 63.2m"),
    ("bud_cocof_sante_liq_2026", "cocof", 2026, 56992000, "", "", "budgeted", src_cocof, "strong", "Mission 23 Sante liq 56.992m"),
    ("bud_cocof_admin_liq_2026", "cocof", 2026, 58442000, "", "", "budgeted", src_cocof, "strong", "Mission 21 Administration liq 58.442m"),
    ("bud_cocof_enseignement_liq_2026", "cocof", 2026, 51664000, "", "", "budgeted", src_cocof, "strong", "Mission 29 Enseignement liq 51.664m"),
    ("bud_cocof_infra_liq_2026", "cocof", 2026, 36757000, "", "", "budgeted", src_cocof, "strong", "Mission 31 Infrastructures liq 36.757m"),
    ("bud_cocof_debt_eoy_2026", "cocof", 2026, 203700000, "", "", "budgeted", src_cocof, "strong", "Debt stock est EOY 2026 203.7m (from 182.7m EOY25); SPABS soudure 180.3m"),
    ("bud_bruxelles_formation_2026", "bruxelles_formation", 2026, 96200000, "", "", "budgeted", src_cocof, "strong", "Bruxelles Formation balanced 96.2m 2026; dual VDAB/Actiris"),
    ("bud_vgc_exp_uit_2025", "vgc", 2025, 173627909, "", "", "outturn", src_vgc, "strong", "Exploitatie uitgaven rek 173.627909m schema J2"),
    ("bud_vgc_exp_ont_2025", "vgc", 2025, 224963076, "", "", "outturn", src_vgc, "strong", "Exploitatie ontvangsten 224.963076m"),
    ("bud_vgc_exp_saldo_2025", "vgc", 2025, 51335168, "", "", "outturn", src_vgc, "strong", "Exploitatiesaldo 51.335m"),
    ("bud_vgc_op_ont_2025", "vgc", 2025, 219418853, "", "", "outturn", src_vgc, "strong", "Operationele ontvangsten 219.419m of which dots 171.0m (BCR 96.8 VL 50.8 fed 23.4)"),
    ("bud_vgc_werksubs_2025", "vgc", 2025, 53883069, "", "", "outturn", src_vgc, "strong", "Toegestane werkingssubsidies 53.883m L4 class"),
    ("bud_vgc_personeel_2025", "vgc", 2025, 89016045, "", "", "outturn", src_vgc, "strong", "Bezoldigingen 89.016m"),
    ("bud_vgc_inv_uit_2025", "vgc", 2025, 99527437, "", "", "outturn", src_vgc, "strong", "Investeringsuitgaven 99.527m incl invsubs granted 17.57m"),
    ("bud_vgc_debt_eoy_2025", "vgc", 2025, 242125466, "", "", "outturn", src_vgc, "strong", "Financiele schulden LT+ST class ~242.1m EOY25 (LT 230.9 + within year 11.2)"),
    ("bud_vgc_afm_2025", "vgc", 2025, 41818619, "", "", "outturn", src_vgc, "strong", "Autofinancieringsmarge 41.819m strong surplus"),
    ("bud_vgc_bbr_2025", "vgc", 2025, 207790290, "", "", "outturn", src_vgc, "strong", "Beschikbaar budgettair resultaat 207.79m before bestemde; after 107.76m"),
    ("bud_vgc_cashout_class_2025", "vgc", 2025, 273155346, "", "", "outturn", src_vgc, "strong", "Exp+inv uit class 173.6+99.5=273.2m same-year; not full financing"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash_cocof = json.dumps(
    {
        "decret_rec": 625624000,
        "decret_dep_eng": 667610000,
        "decret_dep_liq": 677505000,
        "regl_rec": 16112000,
        "regl_dep_liq": 24305000,
        "combined_dep_liq": 701810000,
        "sec_solde": -22708000,
        "sous_util": 35758000,
        "solde_brut": -60074000,
        "phare": 210270000,
        "aide": 113898000,
        "formation": 91766000,
        "sante": 56992000,
        "enseignement": 51664000,
        "admin": 58442000,
        "bf": 96200000,
        "bf_dot_class": 63200000,
        "debt_eoy26": 203700000,
        "path_sec": {2026: -22708000, 2027: -15000000, 2028: -7500000, 2029: 0},
        "hrf_cap_2026_pct": 2.88,
        "hrf_avg_2025_31_pct": 2.97,
        "note": "Strong CoA; dual VGC/COCOM; Phare L5 residual; net primary not in expose",
    }
)
cash_vgc = json.dumps(
    {
        "exp_uit": 173627909,
        "exp_ont": 224963076,
        "exp_saldo": 51335168,
        "op_ont": 219418853,
        "werksubs": 53883069,
        "personeel": 89016045,
        "inv_uit": 99527437,
        "inv_subs_granted": 17566417,
        "debt_eoy": 242125466,
        "afm": 41818619,
        "bbr": 207790290,
        "bbr_after_bestemd": 107761095,
        "dots_bcr": 96785278,
        "dots_vl": 50810927,
        "dots_fed": 23435510,
        "year": "2025_outturn",
        "note": "Strong jaarrekening; dual COCOF; 2026 full MJP residual if new plan",
    }
)
with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_cocof_budget_2026",
            "COCOF decret+reglement budget package 2026",
            "cocof",
            "FR Brussels residents Phare education training",
            "CoA report BI2026 31 Mar 2026",
            "2026-03-31",
            "2026",
            "2029",
            701810000,
            cash_cocof,
            0,
            "active",
            url_cocof,
            "French Community Commission dual VGC social culture education disability",
            "Publish net primary vs HRF 2.88pct; open Phare L5 end-receivers",
            src_cocof,
            "strong",
            "Bruxelles>COCOF",
            "tick235 dual to COCOM/VGC",
        ]
    )
    w.writerow(
        [
            "cmt_vgc_outturn_2025",
            "VGC BBC outturn package 2025 dual COCOF",
            "vgc",
            "NL Brussels residents education culture welfare",
            "Jaarrekening 2025 Raad 10 Jul 2026",
            "2026-07-10",
            "2025",
            "2025",
            273155346,
            cash_vgc,
            0,
            "active",
            url_vgc,
            "Flemish Community Commission dual COCOF social culture education",
            "Publish 2026 MJP totals when final; open top20 werksubs L5",
            src_vgc,
            "strong",
            "Bruxelles>VGC",
            "tick235",
        ]
    )
    w.writerow(
        [
            "cmt_bruxelles_formation_2026",
            "Bruxelles Formation OAA 96.2m 2026",
            "bruxelles_formation",
            "Jobseekers FR Brussels",
            "COCOF consolidation perimeter CoA ch6",
            "2026-03-31",
            "2026",
            "2026",
            96200000,
            json.dumps({"total": 96200000, "cocof_dot_class": 63200000, "note": "Balanced; dual VDAB/Actiris/FOREM"}),
            0,
            "active",
            url_cocof,
            "French-speaking vocational training Brussels",
            "Publish dual unit-cost vs VDAB Actiris",
            src_cocof,
            "strong",
            "Bruxelles>COCOF>BruxellesFormation",
            "tick235",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_cocof_dep_702m",
            "COCOF decret+reglement dep ~702m 2026",
            "Brussels",
            "ops",
            "Bruxelles>COCOF",
            701810000,
            701810000,
            "Strong CoA: decret liq 677.5m + regl 24.3m; rec 641.7m class; SEC -22.7m; dual VGC/COCOM",
            "strong",
            src_cocof,
            "FR Brussels residents",
            "French Community Commission budget",
            "Core dual community layer not pure waste; Phare L5 residual",
            3,
            8.0,
            5,
            6.25,
            "Publish net primary; open Phare L5",
            "seed",
            "",
            "tick235",
        ]
    )
    w.writerow(
        [
            "lb_cocof_phare_210m",
            "COCOF Phare disability 210m 2026",
            "Brussels",
            "ops",
            "Bruxelles>COCOF>Phare",
            210270000,
            210270000,
            "Strong: Mission 32 ~31.5pct decret; indexation + Nos Pilifs infra; L5 end-receivers thin",
            "strong",
            src_cocof,
            "Persons with disabilities FR Brussels",
            "Disability services Phare",
            "Core social; dual VAPH Flanders; residual named operators",
            3,
            7.5,
            4,
            5.7,
            "Open named service operators L5",
            "seed",
            "",
            "tick235",
        ]
    )
    w.writerow(
        [
            "lb_vgc_exp_174m",
            "VGC exploitatie uitgaven 173.6m 2025 outturn",
            "Brussels",
            "ops",
            "Bruxelles>VGC",
            173627909,
            173627909,
            "Strong JR: exp 173.6m rec 225.0m saldo 51.3m; werksubs 53.9m; dual COCOF ~7x smaller opex class",
            "strong",
            src_vgc,
            "NL Brussels residents",
            "Flemish Community Commission operations",
            "Core dual layer; surplus AFM 41.8m; not pure waste",
            2,
            7.0,
            4,
            5.15,
            "Open top20 werksubs L5; dual unit-cost COCOF",
            "seed",
            "",
            "tick235",
        ]
    )
    note = (
        "Strong: COCOM SCR 2.04bn + COCOF 0.70bn + VGC exp 0.17bn class; "
        "do not sum double-count dots; triple dual layer vs BCR"
    )
    w.writerow(
        [
            "lb_bru_community_dual_stack",
            "Brussels community commissions dual stack COCOM COCOF VGC",
            "Brussels",
            "ops",
            "Bruxelles>Community_commissions_dual",
            0,
            0,
            note,
            "strong",
            src_cocof,
            "All Brussels residents",
            "Bicommunal + unilingual community governance stack",
            "Institutional dual/triple overhead mechanism; core services dominate totals",
            6,
            8.5,
            6,
            6.9,
            "Map dual unit costs; rationalise reporting; FOI L5 residual",
            "seed",
            "",
            "tick235 dual stack not additive euros",
        ]
    )

# FOI residual Phare L5 + VGC top werksubs
gap_id = "gap_cocof_phare_vgc_l5"
with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "Bruxelles>COCOF_VGC>Phare_werksubs_L5",
            "cocof",
            "Named Phare operators with EUR 2024-2026; VGC top20 werkingssubsidies machine-readable 2024-2026; COCOF net primary exp growth vs HRF 2.88pct 2026",
            "Phare 210m and VGC werksubs 53.9m aggregates public; end-receiver L5 and HRF metric omitted from expose (CoA)",
            6,
            "COCOF College / VGC College / SPRB transparence",
            "transparence@sprb.brussels",
            "SPRB Place Saint-Lazare 2 1035 Bruxelles",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_cocof_budget_2026|cmt_vgc_outturn_2025",
            "lb_cocof_phare_210m|lb_vgc_exp_174m",
            "2026-07-29T04:35:00Z",
            "2026-07-29T04:35:00Z",
            "tick235 draft ready human send; public totals filled",
        ]
    )

# research queue + loop state
rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_226":
            row["status"] = "done"
            row["updated_utc"] = "2026-07-29T04:35:00Z"
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                "tick235: COCOF decret+regl liq 701.8m Phare 210.3m BF 96.2m SEC -22.7m; "
                "VGC exp outturn 173.6m werksubs 53.9m debt 242m; FOI L5 ready; spawn rq_227"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_227",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "other large FOI-adjacent programmes dual PES residual) if new PDFs appear; "
            "else next open rq; do not idle while public work remains."
        ),
        "blocked_gap_id": "",
        "created_utc": "2026-07-29T04:35:00Z",
        "updated_utc": "",
        "notes": "Spawned tick235 after COCOF 702m VGC 174m dual; rq_116 SWA deferred Oct-Dec 2026",
    }
)

with open(os.path.join(base, "research_queue.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(os.path.join(base, "loop_state.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            "2026-07-29T04:35:00Z",
            "rq_226",
            235,
            "no",
            "Scheduler 60s. Next prio5 rq_227; rq_116 SWA deferred. FOI ready human send. tick235 COCOF 702m Phare 210m VGC exp 174m.",
        ]
    )

print("tick235 writes OK")
