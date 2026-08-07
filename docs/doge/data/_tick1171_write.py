# tick1171: AGB Merelbeke-Melle JR2025 Entity II dual residual
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = "src_agb_merelbeke_melle_jr2025"
ENT = "agb_merelbeke_melle"
TICK = "tick1171"
UTC = "2026-08-08T03:00:00Z"
GAP = "gap_agb_mm_afm_neg_city_loan_18_5m_prijssub_factor_l5"
URL = "https://www.merelbeke-melle.be/jaarrekening-2025-agb"

csv.field_size_limit(10_000_000)

with open(ROOT / "sources.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            SRC,
            "AGB Merelbeke-Melle Jaarrekening BBC 2025 (59p) RVB 17.06.2026 pub 22.06.2026",
            URL,
            "AGB Merelbeke-Melle / Gemeente Merelbeke-Melle",
            "2026-08-08",
            "official_pdf",
            "Entity II dual residual; KBO 0661.984.022; assets 20.906m fin debt 18.525m "
            "city renteloos AFM -0.185m prijssub 1.509m dividend while loss; " + TICK,
        ]
    )

with open(ROOT / "entities.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            ENT,
            "AGB Merelbeke-Melle",
            "AGB Merelbeke-Melle",
            "AGB Merelbeke-Melle",
            "local_entity",
            "city_merelbeke_melle",
            "nl",
            URL,
            "info@merelbeke-melle.be",
            "Hundelgemsesteenweg 353 9820 Merelbeke-Melle",
            "JR2025 Entity II dual residual "
            + TICK
            + "; KBO 0661.984.022; fusion sport/culture AGB; assets 20.906m equity 1.518m "
            "cash 0.685m fin debt 18.525m city renteloos (LT 17.533 + ST due 0.992) "
            "prijssub 1.509m AFM -0.185m NEG BBR 0.501m PnL -0.187m dividend 0.005m "
            "while loss; Secr Michaël Pector FD Frank Vanhove Voorzitter Tim De Keukelaere; FOI "
            + GAP,
        ]
    )

budgets = [
    ("bud_agbmm_assets_2025", 20905658, "Assets balanstotaal YE2025 20.906m"),
    ("bud_agbmm_equity_2025", 1517532, "Nettoactief YE2025 1.518m"),
    ("bud_agbmm_cum_pnl_2025", 27638, "Gecumuleerd overschot YE2025 0.028m DROP from 0.220m"),
    ("bud_agbmm_cap_subs_2025", 1464893, "Kapitaalssubsidies YE2025 1.465m"),
    ("bud_agbmm_other_netto_2025", 25000, "Overig nettoactief/kapitaal YE2025 0.025m"),
    ("bud_agbmm_debt_total_2025", 19388126, "Schulden total YE2025 19.388m"),
    ("bud_agbmm_fin_debt_2025", 18524695, "Fin schulden T3 total YE2025 18.525m city renteloos"),
    ("bud_agbmm_fin_debt_lt_2025", 17532782, "Fin schulden LT YE2025 17.533m andere leningen"),
    ("bud_agbmm_fin_debt_st_due_2025", 991913, "Fin schulden LT vervallend YE2025 0.992m"),
    ("bud_agbmm_cash_2025", 685223, "Liquide middelen YE2025 0.685m"),
    ("bud_agbmm_mva_2025", 19960508, "MVA YE2025 19.961m"),
    ("bud_agbmm_mva_buildings_2025", 19253766, "MVA terreinen/gebouwen YE2025 19.254m"),
    ("bud_agbmm_st_recv_2025", 243038, "ST vorderingen YE2025 0.243m"),
    ("bud_agbmm_expl_rec_2025", 2815693, "Exploitatieontvangsten 2.816m"),
    ("bud_agbmm_expl_exp_2025", 2036772, "Exploitatieuitgaven 2.037m (incl dividend 5k)"),
    ("bud_agbmm_expl_saldo_2025", 778921, "Exploitatiesaldo +0.779m"),
    ("bud_agbmm_prijssub_2025", 1508732, "Prijssubsidie gemeente 1.509m (factor cut 4.76->0.22)"),
    ("bud_agbmm_retributies_2025", 1275111, "Ontvangsten retributies T2 1.275m"),
    ("bud_agbmm_invest_exp_2025", 1227960, "Investeringsuitgaven 1.228m UNDER vs MJP 3.344m"),
    ("bud_agbmm_invest_saldo_2025", -1227960, "Investeringssaldo -1.228m (no invest receipts)"),
    ("bud_agbmm_molenkouter_invest_2025", 987383, "Molenkouter-Zuid fase 1 invest 0.987m"),
    ("bud_agbmm_new_loans_2025", 1227960, "Nieuwe city doorgeeflening 1.228m (= invest)"),
    ("bud_agbmm_repay_2025", 963546, "Periodieke aflossingen city loans 0.964m"),
    ("bud_agbmm_fin_saldo_2025", 264414, "Financieringssaldo +0.264m"),
    ("bud_agbmm_budget_result_2025", -184625, "Budgettair resultaat boekjaar -0.185m NEG"),
    ("bud_agbmm_bbr_2025", 501337, "Beschikbaar BBR YE2025 0.501m"),
    ("bud_agbmm_afm_2025", -184625, "AFM -0.185m NEG CRITICAL equals budget result"),
    ("bud_agbmm_afm_gecorr_2025", 778921, "Gecorr AFM +0.779m POS (aangewezen 1.511m)"),
    ("bud_agbmm_aangewezen_amort_2025", 1510548, "Gecorrigeerde aflossingen o.b.v. fin schulden 1.511m"),
    ("bud_agbmm_pnl_2025", -187359, "P&L -0.187m NEG"),
    ("bud_agbmm_dividend_2025", 5000, "Dividend to city 0.005m WHILE LOSS (BTW winstoogmerk)"),
    ("bud_agbmm_interest_2025", 387, "Financiele kosten 0.0004m thin (renteloze city loans)"),
    ("bud_agbmm_depr_2025", 1090401, "Afschrijvingen 1.090m"),
]
with open(ROOT / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for bid, amt, notes in budgets:
        w.writerow(
            [bid, ENT, 2025, amt, "", "", "BBC JR2025 primary", SRC, "strong", notes + "; " + TICK]
        )

cmts = [
    (
        "comm_agbmm_city_loan_18_5m_2025",
        "AGB Merelbeke-Melle city renteloze loan stock 18.5m",
        "100pct andere leningen gemeente; amort tracks investments",
        18524695,
    ),
    (
        "comm_agbmm_afm_neg_0_18m_2025",
        "AGB Merelbeke-Melle AFM -0.18m NEG",
        "Expl saldo 0.779m < repay 0.964m; prijssub factor cut underfunded",
        184625,
    ),
    (
        "comm_agbmm_prijssub_1_51m_2025",
        "AGB Merelbeke-Melle prijssubsidie 1.51m",
        "Factor 4.76->2.95->0.22 Nov-Dec underfunding path dual residual",
        1508732,
    ),
    (
        "comm_agbmm_dividend_while_loss_2025",
        "AGB Merelbeke-Melle dividend 5k while PnL -187k",
        "BTW winstoogmerk dividend despite book loss",
        5000,
    ),
    (
        "comm_agbmm_molenkouter_0_99m_2025",
        "AGB Merelbeke-Melle Molenkouter invest 0.99m",
        "Realisatie recreatiezone Molenkouter-Zuid fase 1",
        987383,
    ),
    (
        "comm_agbmm_invest_under_1_23m_vs_3_34m_2025",
        "AGB Merelbeke-Melle invest UNDER 1.23 vs MJP 3.34m",
        "Zwembad energy sub 0.42m not drawn; large MJP gap",
        1227960,
    ),
]
with open(ROOT / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for cid, title, goal, env in cmts:
        w.writerow(
            [
                cid,
                title,
                ENT,
                "AGB dual residual",
                "BBC JR2025",
                "2026-06-17",
                2025,
                2025,
                env,
                f"{{2025:{env}}}",
                0,
                "active",
                URL,
                goal,
                "Entity II FOI residual",
                SRC,
                "strong",
                "Vlaanderen>Gemeenten>Merelbeke-Melle>AGB",
                TICK,
            ]
        )

lbs = [
    ("lb_agbmm_city_loan_18_5m_2025", "AGB Merelbeke-Melle city loan debt 18.5m shell", 18524695, 7.5, 7.5, 3.0, "City loan FOI residual"),
    ("lb_agbmm_afm_neg_0_18m_2025", "AGB Merelbeke-Melle AFM -0.18m NEG", 184625, 8.5, 4.0, 3.0, "AFM path FOI residual"),
    ("lb_agbmm_prijssub_1_51m_2025", "AGB Merelbeke-Melle prijssub 1.51m", 1508732, 7.5, 6.0, 3.0, "Subsidy FOI residual"),
    ("lb_agbmm_assets_20_9m_2025", "AGB Merelbeke-Melle assets 20.9m Entity II", 20905658, 5.5, 7.5, 3.0, "Map residual"),
    ("lb_agbmm_dividend_while_loss_2025", "AGB Merelbeke-Melle dividend while PnL loss", 5000, 9.0, 2.5, 3.0, "BTW policy FOI"),
    ("lb_agbmm_pnl_neg_0_19m_2025", "AGB Merelbeke-Melle PnL -0.19m NEG", 187359, 8.0, 4.0, 3.0, "Loss FOI residual"),
    ("lb_agbmm_invest_under_1_23m_2025", "AGB Merelbeke-Melle invest UNDER 1.23m", 1227960, 6.5, 6.0, 3.0, "Capex FOI residual"),
    ("lb_agbmm_st_due_0_99m_2025", "AGB Merelbeke-Melle ST due 0.99m wall", 991913, 7.0, 5.5, 3.0, "Amort wall FOI"),
]
with open(ROOT / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for lid, name, cost, abs_s, cost_s, diff, cut in lbs:
        prio = round((abs_s * cost_s * (10 - diff)) / 10.0, 1)
        w.writerow(
            [
                lid,
                name,
                "L5",
                "local_budget_line",
                "Vlaanderen>Gemeenten>Merelbeke-Melle>AGB_L5",
                cost,
                cost,
                "JR2025 Entity II dual residual VL strong primary BBC fusion city loan AFM NEG dividend while loss",
                "strong",
                SRC,
                "Merelbeke-Melle residents / sport-culture users",
                "Local dual residual map VL JR2025 AGB Merelbeke-Melle",
                "BBC J2/J4/J5/T2/T3 primary",
                abs_s,
                cost_s,
                diff,
                prio,
                cut,
                "active",
                "",
                TICK,
            ]
        )

with open(ROOT / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            GAP,
            "Vlaanderen>Gemeenten>Merelbeke-Melle>AGB>city_loan_afm_prijssub_L5",
            ENT,
            "City renteloze doorgeeflening schedule behind fin debt 18.525m (ST due 0.992m); "
            "AFM -0.185m multi-year path and 2027 zwembad works factor plan; prijssubsidie factor "
            "history 4.76/2.95/0.22 multi-year formula and over/underfunding controls; dividend 5k "
            "while PnL -187k BTW winstoogmerk legal basis; invest UNDER 1.228 vs MJP 3.344 and "
            "Sport VL 0.42m energy sub not drawn; 40y erfpacht city residual; Molenkouter remaining "
            "capex; zero own staff SLA cash flows",
            "Entity II fusion AGB dual residual: EUR18.5m city-debt shell with AFM NEG and dividend "
            "while book loss after prijssub factor cut; material dual ranking vs city GE tick924",
            9,
            "Gemeente / AGB Merelbeke-Melle",
            "info@merelbeke-melle.be",
            "Hundelgemsesteenweg 353 9820 Merelbeke-Melle",
            f"docs/doge/foi/drafts/{GAP}.md",
            "ready",
            "2026-08-08",
            "",
            "",
            "",
            "",
            "comm_agbmm_city_loan_18_5m_2025|comm_agbmm_afm_neg_0_18m_2025",
            "lb_agbmm_city_loan_18_5m_2025|lb_agbmm_afm_neg_0_18m_2025|lb_agbmm_dividend_while_loss_2025",
            UTC,
            UTC,
            TICK + "; ready not sent; do not send without human OK",
        ]
    )

rows = []
with open(ROOT / "research_queue.csv", "r", encoding="utf-8", errors="replace", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_1171":
            row["status"] = "done"
            row["entity_id"] = ENT
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick1171 AGB Merelbeke-Melle JR2025 Entity II dual residual; city loan 18.5m "
                "AFM NEG prijssub 1.51m dividend while loss; FOI " + GAP
            )
        rows.append(row)
if not any(r["task_id"] == "rq_1172" for r in rows):
    rows.append(
        {
            "task_id": "rq_1172",
            "title": "Continuous FOI-adjacent public hole-fill batch",
            "sprint": "hole_fill",
            "priority": "5",
            "status": "open",
            "hierarchy_target": "Vlaanderen>Gemeenten>residual_dual_L5",
            "entity_id": "",
            "instructions": "Residual dual L5 VL JR2025 (GE/OCMW + AGB). Prefer unmined AGB after city GE. Primary BBC only.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned by tick1171; next residual dual L5 after AGB Merelbeke-Melle",
        }
    )
with open(ROOT / "research_queue.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print("tick1171 write OK", len(budgets), "budgets", len(cmts), "cmts", len(lbs), "lbs")
