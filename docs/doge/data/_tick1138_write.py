# tick 1138 — AGB Herk-de-Stad JR2025 Entity II dual residual after city
from pathlib import Path

ts = "2026-08-12T10:30:00Z"
src = "src_herk_agb_jr2025"
ent = "agb_herk_de_stad"
gap = "gap_agh_afm_neg_lt_recv_loans_jump_cash_drop_l5"

# EUR from BBC JR2025 primary KBO 0537.728.111 (image tables + summary)
assets = 1807875
equity = 660033
debt_total = 1147842
fin_debt = 1140000  # LT 1080000 + ST due 60000
fin_debt_lt = 1080000
fin_debt_st_due = 60000
cash = 155640
lt_recv = 866464
mva = 724587
expl_rec = 105687
expl_exp = 67796
expl_saldo = 37891
invest = 17697
afm = -22109
afm_gecorr = 13891
bbr = 209311
budget = -6270
pl = 1598
cum_pl = -339967
new_loans = 900000  # fin receipts
repay = 60000  # periodieke aflossingen
fin_exp = 926464  # includes non-periodic?
interest = 3617
omzet = 78920
goederen = 63991
andere_opbr = 26768
overig_equity = 1000000

with open("docs/doge/data/sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f"{src},AGB Herk-de-Stad BBC Jaarrekening 2025,"
        "https://www.herk-de-stad.be/sites/default/files/public/Jaarrekening%202025%20ABB.pdf,"
        "AGB Herk-de-Stad,2026-08-12,primary_pdf,"
        "tick1138; 41p AGB (tables image OCR); KBO 0537.728.111; Pikkeleerstraat 14 3540; "
        "AD Nathalie Creten FD Ive Vanderlee; assets 1.808m JUMP LT recv 0.866m new loans 0.900m "
        "fin debt 1.140m cash DROP AFM -0.022m BBR 0.209m; dual residual after city Herk-de-Stad\n"
    )

with open("docs/doge/data/entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f"{ent},AGB Herk-de-Stad,Regie communale autonome Herk-de-Stad,"
        "Autonomous municipal company Herk-de-Stad,municipal_agency,city_herk_de_stad,nl,"
        "https://www.herk-de-stad.be,info@herk-de-stad.be,Pikkeleerstraat 14 3540 Herk-de-Stad,"
        f"JR2025 Entity II dual residual tick1138; KBO 0537.728.111; assets 1.808m LT recv 0.866m "
        f"new loans 0.900m fin debt 1.14m AFM -0.022m; FOI {gap}\n"
    )

budgets = [
    ("bud_agh_assets_2025", assets, "Total assets YE2025 1.808m JUMP (was 1.053m); tick1138"),
    ("bud_agh_equity_2025", equity, "Nettoactief YE2025 0.660m; tick1138"),
    ("bud_agh_debt_total_2025", debt_total, "Total schulden YE2025 1.148m JUMP; tick1138"),
    (
        "bud_agh_fin_debt_2025",
        fin_debt,
        "Financiele schulden total YE2025 1.140m (LT 1.080 + ST due 0.060); tick1138",
    ),
    ("bud_agh_fin_debt_lt_2025", fin_debt_lt, "Fin schulden LT YE2025 1.080m JUMP (was 0.240m); tick1138"),
    (
        "bud_agh_fin_debt_st_due_2025",
        fin_debt_st_due,
        "Schulden LT vervallend binnen jaar YE2025 0.060m; tick1138",
    ),
    ("bud_agh_cash_2025", cash, "Liquide middelen YE2025 0.156m DROP (was 0.261m); tick1138"),
    (
        "bud_agh_lt_recv_2025",
        lt_recv,
        "Vorderingen LT ruil 0.866m JUMP FOI (was 0); tick1138",
    ),
    ("bud_agh_mva_2025", mva, "Materiele vaste activa YE2025 0.725m; tick1138"),
    ("bud_agh_expl_rec_2025", expl_rec, "Exploitatieontvangsten 0.106m; tick1138"),
    ("bud_agh_expl_exp_2025", expl_exp, "Exploitatieuitgaven 0.068m; tick1138"),
    ("bud_agh_expl_saldo_2025", expl_saldo, "Exploitatiesaldo +0.038m; tick1138"),
    ("bud_agh_invest_2025", invest, "Investeringsuitgaven 0.018m; tick1138"),
    ("bud_agh_afm_2025", afm, "AFM -0.022m NEG FOI; tick1138"),
    (
        "bud_agh_afm_gecorr_2025",
        afm_gecorr,
        "Gecorr AFM +0.014m; tick1138",
    ),
    ("bud_agh_bbr_2025", bbr, "BBR 0.209m; tick1138"),
    ("bud_agh_budget_result_2025", budget, "Budgettair resultaat -0.006m NEG; tick1138"),
    ("bud_agh_pl_2025", pl, "P&L +0.002m; tick1138"),
    ("bud_agh_cum_pl_2025", cum_pl, "Gecumuleerd tekort -0.340m; tick1138"),
    (
        "bud_agh_new_loans_2025",
        new_loans,
        "Financieringsontvangsten/nieuwe leningen 0.900m MASSIVE FOI; tick1138",
    ),
    ("bud_agh_repay_2025", repay, "Periodieke aflossingen 0.060m; tick1138"),
    ("bud_agh_interest_2025", interest, "Financiele kosten 0.004m; tick1138"),
    ("bud_agh_omzet_2025", omzet, "Opbrengsten uit werking 0.079m; tick1138"),
    ("bud_agh_goederen_2025", goederen, "Goederen en diensten 0.064m; tick1138"),
    (
        "bud_agh_andere_opbr_2025",
        andere_opbr,
        "Andere ops opbrengsten 0.027m; tick1138",
    ),
]
with open("docs/doge/data/budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, amt, notes in budgets:
        f.write(
            f"{bid},{ent},2025,{amt},,,jaarrekening_realized,{src},strong,{notes}\n"
        )

comms = [
    (
        "comm_agh_fin_debt_1_14m_2025",
        "AGB Herk-de-Stad fin debt 1.140m YE2025 JUMP",
        "creditors",
        fin_debt,
        f"2025stock:{fin_debt}",
        "stock",
        "Debt jump with new loans",
        "Lender FOI",
        "Vlaanderen>Gemeenten>Herk_de_Stad>AGB>debt",
    ),
    (
        "comm_agh_lt_recv_0_87m_2025",
        "AGB Herk-de-Stad LT receivables 0.866m new YE2025",
        "counterparties",
        lt_recv,
        f"2025stock:{lt_recv}",
        "stock",
        "New loans-out stock",
        "Schedule FOI",
        "Vlaanderen>Gemeenten>Herk_de_Stad>AGB>loans_out",
    ),
    (
        "comm_agh_new_loans_0_90m_2025",
        "AGB Herk-de-Stad new financing receipts 0.900m 2025",
        "lenders",
        new_loans,
        f"2025new:{new_loans}",
        "outturn",
        "Debt raise / refinance",
        "Purpose FOI",
        "Vlaanderen>Gemeenten>Herk_de_Stad>AGB>loans",
    ),
    (
        "comm_agh_afm_neg_0_022m_2025",
        "AGB Herk-de-Stad AFM -0.022m NEG 2025",
        "fiscal equilibrium",
        22109,
        f"2025AFM:{afm};BBR:{bbr}",
        "outturn",
        "AFM structural NEG",
        "Path FOI",
        "Vlaanderen>Gemeenten>Herk_de_Stad>AGB>AFM",
    ),
    (
        "comm_agh_cash_drop_0_11m_2025",
        "AGB Herk-de-Stad cash DROP 0.106m to 0.156m",
        "treasury",
        105857,
        f"2025cash:{cash}",
        "outturn",
        "Liquidity after debt raise",
        "Treasury FOI",
        "Vlaanderen>Gemeenten>Herk_de_Stad>AGB>cash",
    ),
]
with open("docs/doge/data/commitments.csv", "a", encoding="utf-8", newline="") as f:
    for cid, title, ben, total, cash_y, status, goal, cut, path in comms:
        rem = total if status == "stock" else 0
        f.write(
            f"{cid},{title},{ent},{ben},BBC JR2025,2026-06-01,2025,2025,{total},"
            f"{cash_y},{rem},{status},"
            "https://www.herk-de-stad.be/sites/default/files/public/Jaarrekening%202025%20ABB.pdf,"
            f"{goal},{cut},{src},strong,{path},tick1138 primary JR2025 AGB Herk\n"
        )

lbs = [
    (
        "lb_agh_new_loans_0_90m_2025",
        "AGB Herk new loans/financing 0.90m FOI residual",
        new_loans,
        new_loans,
        6.5,
        4.5,
        3.0,
        "FOI purpose vs LT recv; dual residual",
    ),
    (
        "lb_agh_lt_recv_0_87m_2025",
        "AGB Herk LT receivables 0.87m NEW FOI residual",
        lt_recv,
        lt_recv,
        7.0,
        4.5,
        3.5,
        "FOI loans-out counterparties; dual residual",
    ),
    (
        "lb_agh_fin_debt_1_14m_2025",
        "AGB Herk fin debt 1.14m JUMP FOI residual",
        fin_debt,
        fin_debt,
        6.0,
        4.5,
        3.0,
        "FOI debt path; dual residual",
    ),
    (
        "lb_agh_afm_neg_0_022m_2025",
        "AGB Herk AFM -0.022m NEG FOI residual",
        22109,
        22109,
        5.5,
        3.0,
        2.5,
        "FOI AFM path; dual residual",
    ),
    (
        "lb_agh_cash_drop_0_11m_2025",
        "AGB Herk cash DROP 0.11m FOI residual",
        105857,
        cash,
        5.5,
        3.5,
        2.5,
        "Treasury FOI; dual residual",
    ),
    (
        "lb_agh_assets_jump_0_75m_2025",
        "AGB Herk assets JUMP 0.75m to 1.81m FOI residual",
        754778,
        assets,
        5.0,
        4.0,
        2.5,
        "Balance expansion FOI; dual residual",
    ),
    (
        "lb_agh_bbr_0_21m_2025",
        "AGB Herk BBR 0.21m FOI residual",
        bbr,
        bbr,
        3.0,
        3.5,
        2.0,
        "Keep BBR; dual residual",
    ),
    (
        "lb_agh_cum_pl_neg_0_34m_2025",
        "AGB Herk cum P&L -0.34m FOI residual",
        339967,
        339967,
        5.0,
        3.5,
        2.5,
        "Equity structure FOI; dual residual",
    ),
    (
        "lb_agh_omzet_0_08m_2025",
        "AGB Herk omzet 0.08m FOI residual",
        omzet,
        omzet,
        3.5,
        3.0,
        2.5,
        "Ops revenue; dual residual",
    ),
    (
        "lb_agh_pl_pos_0_002m_2025",
        "AGB Herk P&L +0.002m FOI residual",
        pl,
        pl,
        3.0,
        2.5,
        2.0,
        "Thin profit; dual residual",
    ),
]
with open("docs/doge/data/leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lid, name, annual, total, abs_s, cost_s, diff, cut in lbs:
        prio = round((abs_s * 0.4) + (cost_s * 0.35) + ((10 - diff) * 0.25), 2)
        f.write(
            f"{lid},{name},L5,local_budget_line,Vlaanderen>Gemeenten>Herk_de_Stad_AGB_L5,"
            f"{annual},{total},JR2025 Entity II dual residual map VL,strong,{src},"
            f"Herk-de-Stad residents,Local dual residual map VL JR2025 AGB,"
            f"JR2025 BBC AGB Herk realized figures,{abs_s},{cost_s},{diff},{prio},"
            f"{cut},active,,tick1138; not TE-additive\n"
        )

with open("docs/doge/data/foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f"{gap},Vlaanderen>Gemeenten>Herk_de_Stad>agb_afm_lt_recv_loans_cash_L5,{ent},"
        "AFM -0.022m NEG; new financing receipts 0.900m + fin debt LT JUMP 0.240 to 1.080m; "
        "LT receivables 0.866m NEW (was 0) counterparties/schedule; cash DROP 0.261 to 0.156m "
        "despite debt raise; assets JUMP 1.053 to 1.808m; fin uitgaven 0.926m vs periodieke 0.060m "
        "composition; BBR 0.209m; budget -0.006m,"
        "Limburg Entity II dual: small AGB balance sheet nearly doubled via 0.9m new financing and "
        "new 0.87m LT receivables while cash fell and AFM stayed NEG — FOI package,9,"
        "AGB Herk-de-Stad / Gemeente Herk-de-Stad,info@herk-de-stad.be,"
        "Pikkeleerstraat 14 3540 Herk-de-Stad,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-12,,,,,"
        "comm_agh_lt_recv_0_87m_2025,lb_agh_lt_recv_0_87m_2025,"
        "2026-08-12T10:30:00Z,2026-08-12T10:30:00Z,"
        "tick1138; ready not sent; do not send without human OK\n"
    )

rq_path = Path("docs/doge/data/research_queue.csv")
lines = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in lines:
    if line.startswith("rq_1138,"):
        out.append(
            "rq_1138,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,done,L5,gg_belgium,"
            f"AGB Herk-de-Stad JR2025 Entity II dual residual after city,{gap},"
            "2026-08-12T10:00:00Z,2026-08-12T10:30:00Z,"
            "tick1138 AGB Herk assets 1.808m JUMP LT recv 0.866m new loans 0.900m fin debt 1.14m "
            "cash DROP AFM -0.022m BBR 0.209m; "
            f"FOI {gap} prio9 ready"
        )
    else:
        out.append(line)
out.append(
    "rq_1139,Continuous FOI-adjacent public hole-fill batch,hole_fill,5,open,L5,gg_belgium,"
    "PROGRESS residual: dual L5 or unmined primary (Oosterzele / Nijlen / Vorselaar / Bornem / "
    "De Panne OCR / Schelle GE+OCMW / Erpe-Mere full JR / Brakel GE+OCMW / Puurs full JR / "
    "AGB Galmaarden / AGB Herentals S&R / other); prefer FOI-adjacent L5; skip rq_116,,"
    "2026-08-12T10:30:00Z,2026-08-12T10:30:00Z,"
    "spawned tick1138 after AGB Herk dual residual; next residual dual L5; progress@1140 in 1"
)
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

Path("docs/doge/data/loop_state.csv").write_text(
    '"state_id","mode","current_sprint","last_tick_utc","last_unit_id","ticks_completed","paused","notes"\n'
    f'"main","continuous","hole_fill","{ts}","rq_1138","1138","no",'
    '"last tick1138 AGB Herk-de-Stad Entity II LT recv/loans JUMP; next rq_1139 residual dual L5; '
    'progress@1140 NEXT; rq_116 deferred; continuous hole_fill"\n',
    encoding="utf-8-sig",
)

print("OK tick1138", len(budgets), "budgets", len(comms), "comms", len(lbs), "lbs")
