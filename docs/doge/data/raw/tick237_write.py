# tick 237 AViQ dual VAPH from Wallonie EPCO 17.093 + minister PQ annex
import csv, os, json, shutil

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src_epco = "src_wal_epco_coppieters_2026"
src_pq = "src_wal_pq_aviq_inexec_2025"
url_epco = "https://finances.wallonie.be/files/Budget%202026/Budget%202026/coppieters/epco.pdf"
url_pq = "https://www.parlement-wallonie.be/content/print.php?print=interp-questions-voir.php&iddoc=139949&type=32"
utc = "2026-07-29T05:35:00Z"
gap_id = "gap_aviq_branch_l5"

# AViQ dots 2026 kEUR from EPCO table (CL = CE for most current lines)
fonct = 88455000
paritaires = 1749566000
reglementees = 1848969000
fac_sante = 27719000
fac_handicap = 7799000
fac_communes = 4297000
eu = 1157000
af = 3008488000
caisses_af = 41351000
cap_sante_cl = 18665000
cap_handicap_cl = 7210000
cap_paritaires = 6481000
cap_invest = 675000

aviq_current_ce = (
    fonct + paritaires + reglementees + fac_sante + fac_handicap
    + fac_communes + eu + af + caisses_af
)
aviq_current_cl = aviq_current_ce  # same per table
aviq_cap_cl = cap_sante_cl + cap_handicap_cl + cap_paritaires + cap_invest
aviq_cap_ce = cap_paritaires + cap_invest  # capital eng mostly 0 on fac lines
aviq_dots_cl = aviq_current_cl + aviq_cap_cl
aviq_dots_ce = aviq_current_ce + aviq_cap_ce

prog_total_ce = 7026601000
prog_total_cl = 7062476000

# inexec from annex: amount and %
inexec_2023 = 389908463.52
inexec_2024 = 316804606.96
pct_2023 = 0.0573
pct_2024 = 0.0443
budget_implied_2023 = round(inexec_2023 / pct_2023)
budget_implied_2024 = round(inexec_2024 / pct_2024)

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src_epco,
            "Wallonie Budget 2026 EPCO Coppieters prog 17.093 AViQ dots table",
            url_epco,
            "SPW Finances / Ministre Coppieters",
            "2026-07-29",
            "budget_justification",
            "Prog 17.093 CE 7026.6m CL 7062.5m; pure AViQ dots CL ~6810.8m (AF 3008.5 fonct 88.5 parit 1749.6 regl 1849.0); treasury refund 230m 2026; tick237; raw wal_epco.pdf",
        ]
    )
    w.writerow(
        [
            src_pq,
            "Parlement Wallonie PQ Roberty/Coppieters AViQ inexecution Nov 2025 + annex",
            url_pq,
            "Parlement de Wallonie",
            "2026-07-29",
            "parliament",
            "Inexec 2023 389.9m 5.73pct 2024 316.8m 4.43pct; recurring 219/202m; managed budget ~7bn; rates protection 94.21 sante 92.76 handicap 97.46 familles 98.46 gestion 90.11; tick237",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "aviq",
            "AViQ Agentschap voor een Kwaliteitsvol Leven",
            "AViQ Agence pour une Vie de Qualite",
            "Walloon Agency for a Quality Life (health social disability family)",
            "parastatal",
            "wallonie_gov",
            "fr",
            "https://www.aviq.be",
            "",
            "",
            "UAP multi-branch; regional dots CL ~6.81bn 2026; AF 3.01bn; dual VAPH/VSB/Opgroeien/Iriscare; tick237",
        ]
    )

rows_b = [
    ("bud_aviq_dots_cl_2026", "aviq", 2026, aviq_dots_cl, "", "", "budgeted", src_epco, "strong", f"Sum pure AViQ DF 093.015-024 + capital CL = {aviq_dots_cl}; excludes federal hospital 179.6m Famiwal 36.4m CRAC WallonieSante"),
    ("bud_aviq_dots_ce_2026", "aviq", 2026, aviq_dots_ce, "", "", "budgeted", src_epco, "strong", f"Pure AViQ CE current+capital eng class {aviq_dots_ce}"),
    ("bud_aviq_fonct_2026", "aviq", 2026, fonct, "", "", "budgeted", src_epco, "strong", "DF 093.015 fonctionnement 88.455m (-3.5m vs 91.94m 2025 RH)"),
    ("bud_aviq_paritaires_2026", "aviq", 2026, paritaires, "", "", "budgeted", src_epco, "strong", "DF 093.016 missions paritaires 1749.566m"),
    ("bud_aviq_reglementees_2026", "aviq", 2026, reglementees, "", "", "budgeted", src_epco, "strong", "DF 093.017 missions reglementees 1848.969m (health disability aging class)"),
    ("bud_aviq_af_2026", "aviq", 2026, af, "", "", "budgeted", src_epco, "strong", "DF 093.023 allocations familiales 3008.488m; dual Iriscare AF 1081m COCOM"),
    ("bud_aviq_caisses_af_2026", "aviq", 2026, caisses_af, "", "", "budgeted", src_epco, "strong", "DF 093.024 remuneration caisses privees AF 41.351m"),
    ("bud_aviq_fac_handicap_2026", "aviq", 2026, fac_handicap, "", "", "budgeted", src_epco, "strong", "DF 093.019 facultatives handicap 7.799m"),
    ("bud_aviq_fac_sante_2026", "aviq", 2026, fac_sante, "", "", "budgeted", src_epco, "strong", "DF 093.018 facultatives sante bien-etre 27.719m (-5m)"),
    ("bud_prog_17093_ce_2026", "wallonie_gov", 2026, prog_total_ce, "", "", "budgeted", src_epco, "strong", "Prog 17.093 total CE 7026.601m (AViQ + federal hospital + Famiwal + CRAC + WallonieSante)"),
    ("bud_prog_17093_cl_2026", "wallonie_gov", 2026, prog_total_cl, "", "", "budgeted", src_epco, "strong", "Prog 17.093 total CL 7062.476m"),
    ("bud_aviq_inexec_2024", "aviq", 2024, inexec_2024, "", "", "outturn", src_pq, "strong", "Inexecution SEC 316.8m 4.43pct annex; implies budget base ~7.15bn"),
    ("bud_aviq_inexec_2023", "aviq", 2023, inexec_2023, "", "", "outturn", src_pq, "strong", "Inexecution SEC 389.9m 5.73pct annex; implies budget base ~6.80bn"),
    ("bud_aviq_budget_implied_2024", "aviq", 2024, budget_implied_2024, "", "", "outturn", src_pq, "medium", f"Implied total budget from inexec/pct = {budget_implied_2024}; aligns minister ~7bn"),
    ("bud_aviq_treasury_refund_2026", "aviq", 2026, 230000000, "", "", "budgeted", src_epco, "strong", "Region receives 230m treasury surplus refund from AViQ 2026 (335.3m in 2025)"),
    ("bud_aviq_effort_2026", "aviq", 2026, 33900000, "", "", "budgeted", src_epco, "strong", "Effort package 33.9m class: fonct -3.5m + mission recentrage path (press 5.6+28.3); structural path 24.54m 2027 / 29.54m 2028"),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "dots_cl_2026": aviq_dots_cl,
        "dots_ce_2026": aviq_dots_ce,
        "fonct": fonct,
        "paritaires": paritaires,
        "reglementees": reglementees,
        "allocations_familiales": af,
        "caisses_af": caisses_af,
        "fac_sante": fac_sante,
        "fac_handicap": fac_handicap,
        "prog_17093_ce": prog_total_ce,
        "prog_17093_cl": prog_total_cl,
        "inexec_2023": inexec_2023,
        "inexec_2024": inexec_2024,
        "inexec_pct_2023": 5.73,
        "inexec_pct_2024": 4.43,
        "recurring_inexec_2023_24": [219000000, 202000000],
        "implied_budget_2024": budget_implied_2024,
        "treasury_refund_2026": 230000000,
        "dual_vaph_vek": 2865400000,
        "dual_vsb_vek": 4748450000,
        "dual_opgroeien_vek": 7611411000,
        "dual_iriscare_af": 1081400000,
        "note": "Strong EPCO L5 dots + PQ annex; multi-branch not pure disability; dual VL IVAs",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_aviq_dots_2026",
            "AViQ regional dots package 2026 dual VL disability social",
            "aviq",
            "Walloon residents health disability family aging",
            "Budget RW 2026 EPCO prog 17.093 + PQ Nov 2025",
            "2025-10-20",
            "2026",
            "2026",
            aviq_dots_cl,
            cash,
            0,
            "active",
            url_epco,
            "Walloon multi-branch social protection agency",
            "Publish branch split handicap vs sante vs AF cash; dual unit-cost VAPH; open operator L5",
            src_epco,
            "strong",
            "Wallonie>Sante>AVIQ",
            "tick237 dual VAPH 2.87bn VSB 4.75bn Opgroeien 7.61bn",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_aviq_dots_6_81bn",
            "AViQ pure regional dots ~6.81bn 2026",
            "Wallonia",
            "ops",
            "Wallonie>AVIQ",
            aviq_dots_cl,
            aviq_dots_cl,
            "Strong EPCO: sum DF 093.015-024+capital CL; AF 3.01bn inside; dual VL WVG IVAs; core social multi-branch",
            "strong",
            src_epco,
            "Walloon residents",
            "Health social disability family aging agency",
            "Core social not pure waste; L5 operators residual; inexec ~4-6pct",
            3,
            9.5,
            5,
            7.0,
            "Open branch L5 and operator lists; dual unit-cost VAPH/Phare",
            "seed",
            "",
            "tick237",
        ]
    )
    w.writerow(
        [
            "lb_aviq_af_3_01bn",
            "AViQ family benefits 3.01bn 2026",
            "Wallonia",
            "transfer",
            "Wallonie>AVIQ>AF",
            af,
            af,
            "Strong DF 093.023 3008.5m; dual Iriscare AF 1081m COCOM; statutory transfer",
            "strong",
            src_epco,
            "Households with children Wallonia",
            "Family benefits 6th reform Walloon",
            "Statutory not pure waste; dual community residual",
            2,
            9.0,
            3,
            5.7,
            "Publish dual unit-cost vs Iriscare FWB residual",
            "seed",
            "",
            "tick237",
        ]
    )
    w.writerow(
        [
            "lb_disability_social_dual_be",
            "Disability-social dual VAPH 2.87bn AViQ ~6.8bn Phare 0.21bn",
            "Belgium",
            "ops",
            "BE>Disability_social>dual_VL_WAL_BRU",
            0,
            0,
            "Strong dual map: VL VAPH disability 2.87bn; WAL AViQ multi-branch dots 6.81bn (not pure handicap); BRU Phare 0.21bn; do not sum",
            "strong",
            src_epco,
            "Persons with disabilities and care users BE",
            "Community dual social protection stack",
            "Institutional dual/triple mechanism; unit-cost FOI residual",
            5,
            9.0,
            6,
            6.95,
            "Publish dual unit-cost per beneficiary by entity",
            "seed",
            "",
            "tick237 dual not additive",
        ]
    )
    w.writerow(
        [
            "lb_aviq_inexec_317m",
            "AViQ inexecution 316.8m 2024 (4.43pct)",
            "Wallonia",
            "ops",
            "Wallonie>AVIQ>inexecution",
            inexec_2024,
            inexec_2024,
            "Strong PQ annex; recurring class ~202m after one-offs; feeds 2026 under-execution budget assumption",
            "strong",
            src_pq,
            "RW taxpayers",
            "Budget under-execution monitoring",
            "Not pure waste; cash not spent; risk of structural over-budgeting",
            4,
            7.5,
            4,
            5.7,
            "Publish multi-year corrected inexec series open data",
            "seed",
            "",
            "tick237",
        ]
    )

with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_id,
            "Wallonie>AVIQ>branches_operators_L5",
            "aviq",
            "Cash-by-year split inside reglementees 1.849bn and paritaires 1.750bn: handicap vs sante vs aging; top operators EUR 2024-2026; reconcile institutional total vs 6.81bn dots + own income",
            "Dots strong public EPCO; multi-branch bulk hides disability dual vs VAPH; operator L5 opaque",
            7,
            "AViQ / SPW publicite administration",
            "",
            "https://www.wallonie.be",
            f"docs/doge/foi/drafts/{gap_id}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_aviq_dots_2026",
            "lb_aviq_dots_6_81bn|lb_disability_social_dual_be",
            utc,
            utc,
            "tick237 draft ready human send",
        ]
    )

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_228":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = gap_id
            row["notes"] = (
                f"tick237: AViQ dots CL {aviq_dots_cl} AF {af} fonct {fonct}; inexec 2024 316.8m; dual VAPH; FOI branch L5 ready; spawn rq_229"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_229",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "Famiwal dual AF; other large FOI-adjacent) if new PDFs appear; "
            "else next open rq; do not idle while public work remains."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick237 after AViQ 6.81bn dual VAPH; rq_116 SWA deferred; progress@240 in 3 ticks",
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
            utc,
            "rq_228",
            237,
            "no",
            f"Scheduler 60s. Next prio5 rq_229; rq_116 SWA deferred. FOI ready human send. tick237 AViQ dots 6.81bn AF 3.01bn dual VAPH.",
        ]
    )

print("tick237 OK", "dots_cl", aviq_dots_cl, "af", af, "implied2024", budget_implied_2024)
