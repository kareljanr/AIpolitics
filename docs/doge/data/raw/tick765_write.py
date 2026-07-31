# tick765 Kamer DOC 56 1281/019 SPF Finances public debt residual
import csv
from pathlib import Path

base = Path("docs/doge/data")
SRC = "src_kamer_debt_1281_019_2026"
SRC_DUAL = "src_dual_debt_interest_tick765"
URL = "https://www.dekamer.be/FLWB/PDF/56/1281/56K1281019.pdf"
TS = "2026-08-03T01:00:00Z"

# kEUR * 1000; 2026 = 3rd year of 2024-2029 series where complete
bud_rows = [
    # Interest
    ("bud_debt_interest_lt_eur_2026", "fod_debt", 2026, 10799836000, "", "", "budgeted", SRC, "strong", "BA 45.10.211001 LT/MT euro interest incl OLO SURE RRF FIF 10799836 kEUR 2026; tick765"),
    ("bud_debt_interest_st_eur_2026", "fod_debt", 2026, 1135070000, "", "", "budgeted", SRC, "strong", "ST treasury certificates etc interest 1135070 kEUR 2026; tick765"),
    ("bud_debt_interest_lt_fx_2026", "fod_debt", 2026, 174312000, "", "", "budgeted", SRC, "strong", "LT/MT FX interest 174312 kEUR 2026; tick765"),
    ("bud_debt_interest_st_fx_2026", "fod_debt", 2026, 55611000, "", "", "budgeted", SRC, "strong", "ST FX interest 55611 kEUR 2026; tick765"),
    ("bud_debt_swap_interest_2026", "fod_debt", 2026, 325510000, "", "", "budgeted", SRC, "strong", "Swap interest costs primes 325510 kEUR 2026; tick765"),
    ("bud_debt_fx_diff_2026", "fod_debt", 2026, 161891000, "", "", "budgeted", SRC, "strong", "BA 45.11.817013 FX differences 161891 kEUR 2026; tick765"),
    ("bud_debt_olo_commissions_2026", "fod_debt", 2026, 45722000, "", "", "budgeted", SRC, "strong", "OLO syndication commissions 45722 kEUR 2026; tick765"),
    ("bud_debt_securities_tax_2026", "fod_debt", 2026, 3480000, "", "", "budgeted", SRC, "strong", "Annual securities account tax on OLO holdings 3480 kEUR 2026; tick765"),
    ("bud_debt_buyback_cost_2026", "fod_debt", 2026, 4421000, "", "", "budgeted", SRC, "strong", "BA 45.11.817014 buyback cost 4421 kEUR 2026; tick765"),
    # Principal / financial ops (not interest expense)
    ("bud_debt_principal_repay_lt_2026", "fod_debt", 2026, 31193197000, "", "", "budgeted", SRC, "strong", "BA 45.11.911001 LT principal repayments 31193197 kEUR 2026 (+7.74bn vs 2025 calendar); tick765"),
    ("bud_debt_securities_purchases_2026", "fod_debt", 2026, 7236958000, "", "", "budgeted", SRC, "strong", "BA 45.11.817015 securities purchases nominal 7236958 kEUR 2026; tick765"),
    # Agency and facilities
    ("bud_debt_agency_dot_2026", "fod_debt", 2026, 7873000, "", "", "budgeted", SRC, "strong", "BA 45.40.414001 Federal Debt Agency dot 7873 kEUR 2026; tick765"),
    ("bud_debt_infrabel_credit_2026", "fod_debt", 2026, 200000000, "", "", "budgeted", SRC, "strong", "BA 45.40.851401 Infrabel refinance credit facility 200000 kEUR 2026; tick765"),
    ("bud_debt_fx_risk_mgmt_2026", "fod_debt", 2026, 480665000, "", "", "budgeted", SRC, "strong", "BA 45.50.817016 FX risk management 480665 kEUR 2026; tick765"),
    ("bud_debt_fx_risk_other_2026", "fod_debt", 2026, 20000000, "", "", "budgeted", SRC, "strong", "BA 45.50.817017 FX risk other 20000 kEUR 2026; tick765"),
    # Derived stacks
    ("bud_debt_interest_core_stack_2026", "fod_debt", 2026, 12490339000, "", "", "derived", SRC, "strong", "Core interest LT+ST+FX+swap 12490.3m 2026 excl FX diff commissions; tick765"),
    ("bud_debt_interest_plus_costs_2026", "fod_debt", 2026, 12705432000, "", "", "derived", SRC, "strong", "Interest core + FX diff + commissions + tax + buyback cost ~12.705bn 2026; tick765"),
    ("bud_debt_principal_plus_purchases_2026", "fod_debt", 2026, 38430155000, "", "", "derived", SRC, "strong", "Principal repay + securities purchases ~38.43bn 2026 financing roll; tick765"),
    ("bud_dual_debt_gg_interest_2026", "gg_belgium", 2026, 12490339000, "", "", "derived", SRC_DUAL, "strong", "Dual federal debt interest core 12.49bn vs GG EDP interest 14.28bn 2025 class; not TE-additive; tick765"),
]

cmt_rows = [
    (
        "cmt_debt_interest_core_2026",
        "Federal public debt core interest stack ~12.49bn 2026",
        "fod_debt",
        "Treasury bond and bill holders",
        "Kamer DOC 56 1281/019 interest BAs",
        "2026-01-28",
        2026,
        2026,
        12490339000,
        '{"lt_eur":10799836000,"st_eur":1135070000,"lt_fx":174312000,"st_fx":55611000,"swap":325510000,"sum":12490339000,"path_lt_from_2025_plus_m":1336.9,"note":"accrual ESA interest; OLO curve 29/08/2025"}',
        0,
        "active",
        URL,
        "Service federal debt interest",
        "Implicit rate FOI dual Entity II",
        SRC,
        "strong",
        "Federal>Debt>interest_core",
        "tick765 major residual",
    ),
    (
        "cmt_debt_interest_lt_olo_2026",
        "LT/MT euro interest OLO SURE RRF FIF 10.80bn 2026",
        "fod_debt",
        "OLO and MTN holders",
        "Kamer 1281/019 BA 45.10.211001",
        "2026-01-28",
        2026,
        2026,
        10799836000,
        '{"2024":8870982000,"2025":9462889000,"2026":10799836000,"2027":12567736000,"path_plus_m":1336.9,"table_olo_interest_m":10457.6,"other_m":32.1,"fif_m":10.5,"class_k":"page13 table partial"}',
        0,
        "active",
        URL,
        "Pay long-term euro debt interest",
        "Maturity profile FOI",
        SRC,
        "strong",
        "Federal>Debt>interest_lt",
        "tick765",
    ),
    (
        "cmt_debt_principal_repay_2026",
        "LT principal repayments 31.19bn 2026 (+7.74bn vs 2025)",
        "fod_debt",
        "Debt refinancing calendar",
        "Kamer 1281/019 BA 45.11.911001",
        "2026-01-28",
        2026,
        2026,
        31193197000,
        '{"2024":52433632000,"2025":23456660000,"2026":31193197000,"path_plus_bn":7.74,"olo_maturities_2026_bn":28.6,"sure_m":1300,"note":"roll not pure waste; two OLOs mature 2026"}',
        0,
        "active",
        URL,
        "Repay maturing long-term debt capital",
        "Issuance plan FOI dual BDA stock",
        SRC,
        "strong",
        "Federal>Debt>principal_repay",
        "tick765",
    ),
    (
        "cmt_debt_securities_purchases_2026",
        "Treasury securities purchases nominal 7.24bn 2026",
        "fod_debt",
        "Debt management buybacks",
        "Kamer 1281/019 BA 45.11.817015",
        "2026-01-28",
        2026,
        2026,
        7236958000,
        '{"2024":815000000,"2025":3591000000,"2026":7236958000,"maturing_buy_m":4649.75,"post_maturing_m":2587.21}',
        0,
        "active",
        URL,
        "Buy securities for debt management",
        "Buyback policy FOI",
        SRC,
        "strong",
        "Federal>Debt>securities_purchases",
        "tick765",
    ),
    (
        "cmt_debt_st_interest_2026",
        "Short-term euro interest (TC etc) 1.135bn 2026",
        "fod_debt",
        "Treasury certificate holders",
        "Kamer 1281/019 ST interest BA",
        "2026-01-28",
        2026,
        2026,
        1135070000,
        '{"2024":838734000,"2025":1090045000,"2026":1135070000}',
        0,
        "active",
        URL,
        "Pay short-term euro debt interest",
        "Optional dual FOI",
        SRC,
        "strong",
        "Federal>Debt>interest_st",
        "tick765",
    ),
    (
        "cmt_debt_agency_2026",
        "Federal Debt Agency dotation 7.87m 2026",
        "fod_debt",
        "Agence federale de la Dette",
        "Kamer 1281/019 BA 45.40.414001",
        "2026-01-28",
        2026,
        2026,
        7873000,
        '{"2024":7936000,"2025":8207000,"2026":7873000}',
        0,
        "active",
        URL,
        "Fund federal debt agency operations",
        "FTE FOI optional",
        SRC,
        "strong",
        "Federal>Debt>agency",
        "tick765",
    ),
    (
        "cmt_debt_fx_risk_2026",
        "FX risk management facilities 500.7m 2026",
        "fod_debt",
        "FX hedge counterparties",
        "Kamer 1281/019 BA 45.50.817016/017",
        "2026-01-28",
        2026,
        2026,
        500665000,
        '{"fx_mgmt":480665000,"fx_other":20000000}',
        0,
        "active",
        URL,
        "Manage FX risk on debt book",
        "Hedge yield FOI",
        SRC,
        "strong",
        "Federal>Debt>fx_risk",
        "tick765",
    ),
    (
        "cmt_dual_debt_interest_tick765",
        "Dual federal debt interest 12.49bn vs GG EDP interest 14.28bn 2025",
        "gg_belgium",
        "Interest multi-level map",
        "Kamer 1281/019 + NBB EDP",
        "2026-01-28",
        2026,
        2026,
        0,
        '{"fed_interest_core_bn":12.49,"fed_interest_plus_costs_bn":12.71,"gg_interest_2025_bn":14.28,"principal_repay_bn":31.19,"securities_purchases_bn":7.24,"bda_stock_2025_bn":552.7,"note":"not TE-additive; Entity II residual"}',
        0,
        "active",
        URL,
        "Comparable debt service transparency",
        "Entity II interest FOI dual",
        SRC_DUAL,
        "strong",
        "Belgium>dual>debt_interest",
        "tick765",
    ),
]

lb_rows = [
    (
        "lb_debt_interest_core_12_49bn_2026",
        "Federal debt core interest ~12.49bn 2026",
        "L5",
        "debt_service",
        "Federal>Debt>interest_core",
        12490339000,
        12490339000,
        "Strong Kamer LT 10.80 + ST 1.14 + FX 0.23 + swap 0.33; path LT +1.34bn vs 2025",
        "strong",
        SRC,
        "Debt holders taxpayers",
        "Service federal interest",
        "Largest pure federal cash-like cost of past deficits; not discretionary waste",
        5.5,
        9.5,
        7,
        7.25,
        "Primary surplus path; publish implicit rate FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_debt_interest_lt_10_80bn_2026",
        "LT/MT euro debt interest 10.80bn 2026",
        "L5",
        "debt_service",
        "Federal>Debt>interest_lt",
        10799836000,
        10799836000,
        "Strong BA 45.10.211001 OLO SURE RRF FIF; path +1.34bn",
        "strong",
        SRC,
        "OLO holders",
        "Pay long-term euro interest",
        "Dominant interest line",
        5.0,
        9.5,
        6,
        7.05,
        "Issuance maturity FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_debt_principal_repay_31_19bn_2026",
        "LT principal repayments 31.19bn 2026",
        "L5",
        "debt_service",
        "Federal>Debt>principal_repay",
        31193197000,
        31193197000,
        "Strong roll +7.74bn vs 2025; two OLOs 28.6bn + SURE 1.3bn; not pure waste",
        "strong",
        SRC,
        "Refinancing market",
        "Repay maturing capital",
        "Calendar roll not spending waste",
        3.0,
        9.0,
        5,
        5.7,
        "Track refinancing risk FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_debt_securities_purchases_7_24bn_2026",
        "Treasury securities purchases 7.24bn 2026",
        "L5",
        "debt_ops",
        "Federal>Debt>securities_purchases",
        7236958000,
        7236958000,
        "Strong financing plan buybacks; financial management not interest",
        "strong",
        SRC,
        "Debt management",
        "Buy securities for management",
        "Ops roll residual",
        4.0,
        8.0,
        4,
        5.7,
        "Buyback policy FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_debt_st_interest_1_14bn_2026",
        "ST euro interest 1.135bn 2026",
        "L5",
        "debt_service",
        "Federal>Debt>interest_st",
        1135070000,
        1135070000,
        "Strong treasury certificates interest path +45m",
        "strong",
        SRC,
        "TC holders",
        "Pay short-term interest",
        "Material ST cost",
        4.5,
        7.5,
        4,
        5.75,
        "Optional dual FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_debt_swap_fx_0_66bn_2026",
        "Swap interest + FX risk facilities ~0.83bn 2026",
        "L5",
        "debt_ops",
        "Federal>Debt>swap_fx",
        826175000,
        826175000,
        "Strong swap 326 + FX risk 501 class; residual hedge transparency",
        "strong",
        SRC,
        "Derivative counterparties",
        "Hedge and swap debt book",
        "Complexity residual",
        5.5,
        7.0,
        4,
        5.95,
        "Hedge L5 FOI",
        "active",
        "",
        "tick765",
    ),
    (
        "lb_dual_debt_interest_2026",
        "Dual federal debt interest map 12.49bn vs GG 14.28bn",
        "L5",
        "debt_service",
        "Belgium>dual>debt_interest",
        12490339000,
        0,
        "Strong dual fed 12.49 vs GG EDP 14.28 2025; Entity II residual; not TE-additive",
        "strong",
        SRC_DUAL,
        "BE multi-level debt service",
        "Map dual interest cost",
        "Primary dual residual",
        5.5,
        9.0,
        4,
        6.7,
        "Entity II interest FOI",
        "active",
        "",
        "tick765",
    ),
]

src_rows = [
    (
        SRC,
        "Kamer DOC 56 1281/019 FOD Financien Rijksschuld public debt budget justification 2026",
        URL,
        "Kamer / Chambre",
        "2026-08-03",
        "parliamentary",
        "Strong tick765: LT interest 10.80bn ST 1.14 FX+swap 0.56 core interest 12.49bn; principal repay 31.19bn (+7.74bn); securities purchases 7.24bn; Debt Agency 7.87m; Infrabel credit 200m; FX risk 481m; OLO commissions 45.7m; raw 56K1281019.pdf 33p",
    ),
    (
        SRC_DUAL,
        "Dual federal debt interest vs GG EDP interest tick765",
        URL,
        "DOGE synthesis Kamer debt + NBB EDP",
        "2026-08-03",
        "synthesis",
        "Strong dual tick765 not TE-additive: fed interest core 12.49bn vs GG interest 14.28bn 2025; BDA stock 552.7bn 2025; Entity II residual",
    ),
]

foi_row = (
    "gap_debt_interest_implicit_rate_l5",
    "Federal>Debt>interest_implicit_rate_L5",
    "fod_debt",
    "Implicit average interest rate by instrument (OLO TC EMTN SURE RRF FIF) 2024-2026; full split of BA 45.10.211001 vs page13 table; hedge/swap P&L cash 2023-2025; dual Entity II interest residual; recon BDA stock path vs principal repay 31.19bn",
    "Kamer 1281/019 interest and principal channels now public; instrument-level rate and hedge residual",
    8,
    "Federaal Agentschap van de Schuld / FOD Financien / IBZ FOI",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_debt_interest_implicit_rate_l5.md",
    "ready",
    "2026-08-03",
    "",
    "",
    "",
    "",
    "cmt_debt_interest_core_2026|cmt_debt_principal_repay_2026|cmt_dual_debt_interest_tick765",
    "lb_debt_interest_core_12_49bn_2026|lb_debt_interest_lt_10_80bn_2026|lb_debt_principal_repay_31_19bn_2026",
    TS,
    TS,
    "tick765 Kamer 1281/019 primary; human send only",
)


def ensure_entities():
    path = base / "entities.csv"
    text = path.read_text(encoding="utf-8")
    n = 0
    rows = []
    if "\nfod_debt," not in text and not text.startswith("fod_debt,"):
        rows.append(
            (
                "fod_debt",
                "FOD Financien Rijksschuld / Federaal Agentschap van de Schuld",
                "SPF Finances Dette publique / Agence federale de la Dette",
                "FPS Finance Public Debt / Federal Debt Agency",
                "ministry",
                "fod_finance",
                "bi",
                "https://www.debtagency.be",
                "",
                "",
                "Federal debt service; tick765",
            )
        )
    if rows:
        with path.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            for r in rows:
                w.writerow(r)
                n += 1
    return n


def main():
    n = ensure_entities()
    for fname, rows in [
        ("budgets.csv", bud_rows),
        ("commitments.csv", cmt_rows),
        ("leaderboard.csv", lb_rows),
        ("sources.csv", src_rows),
    ]:
        with (base / fname).open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            for r in rows:
                w.writerow(r)
    with (base / "foi_queue.csv").open("a", newline="", encoding="utf-8") as f:
        csv.writer(f, lineterminator="\n").writerow(foi_row)

    rq = base / "research_queue.csv"
    lines = rq.read_text(encoding="utf-8").splitlines()
    out = []
    for ln in lines:
        if ln.startswith("rq_756,"):
            out.append(
                "rq_756,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                "Next residual: public debt 1281/019 or OAP 022/023 or residual dual OISZ; SS filled tick764,,"
                f"2026-08-03T00:00:00Z,{TS},"
                "tick765 Debt 1281/019: interest core 12.49bn LT 10.80 principal 31.19 purchases 7.24; FOI ready"
            )
        else:
            out.append(ln)
    out.append(
        "rq_757,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Next residual: OAP 1281/022 or 023 or EU financing 020 or residual dual; Debt filled tick765,,"
        f"{TS},,"
        "spawned tick765 after rq_756"
    )
    rq.write_text("\n".join(out) + "\n", encoding="utf-8")

    (base / "loop_state.csv").write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_756,765,no,"
        "tick765 Debt interest core 12.49bn LT 10.80 principal 31.19; next rq_757 OAP/EU; progress@770 in 5; rq_116 deferred\n",
        encoding="utf-8",
    )
    print(
        f"OK tick765 entities+{n} budgets+{len(bud_rows)} cmt+{len(cmt_rows)} "
        f"lb+{len(lb_rows)} src+{len(src_rows)} foi+1"
    )


if __name__ == "__main__":
    main()
