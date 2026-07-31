# tick763 Kamer DOC 56 1281/012 SPF Emploi residual ops + RVA federal dot + dual SIOD
import csv
from pathlib import Path

base = Path("docs/doge/data")
SRC = "src_kamer_emploi_1281_012_2026"
SRC_DUAL = "src_dual_emploi_inspection_tick763"
URL = "https://www.dekamer.be/FLWB/PDF/56/1281/56K1281012.pdf"
TS = "2026-08-02T23:00:00Z"

bud_rows = [
    # OA21 Support services
    ("bud_emp_oa21_statutair_2026", "fod_emploi", 2026, 10143000, "", "", "budgeted", SRC, "strong", "OA21 support statutair 10143 kEUR 2026; tick763"),
    ("bud_emp_oa21_contract_2026", "fod_emploi", 2026, 3606000, "", "", "budgeted", SRC, "strong", "OA21 support non-statutair 3606 kEUR 2026; tick763"),
    ("bud_emp_oa21_ops_perm_2026", "fod_emploi", 2026, 6914000, "", "", "budgeted", SRC, "strong", "OA21 permanente ops 6914 kEUR 2026; tick763"),
    ("bud_emp_oa21_it_invest_2026", "fod_emploi", 2026, 5723000, "", "", "budgeted", SRC, "strong", "OA21 IT/invest spike 5723 kEUR 2026 (was 2600 2025); tick763"),
    # OA40 President services
    ("bud_emp_oa40_statutair_2026", "fod_emploi", 2026, 1183000, "", "", "budgeted", SRC, "strong", "OA40 president services statutair 1183 kEUR 2026; tick763"),
    ("bud_emp_oa40_contract_2026", "fod_emploi", 2026, 302000, "", "", "budgeted", SRC, "strong", "OA40 non-statutair 302 kEUR 2026; tick763"),
    # OA51 Collective labour relations
    ("bud_emp_oa51_statutair_2026", "fod_emploi", 2026, 6705000, "", "", "budgeted", SRC, "strong", "OA51 collective relations statutair 6705 kEUR 2026; tick763"),
    ("bud_emp_oa51_contract_2026", "fod_emploi", 2026, 934000, "", "", "budgeted", SRC, "strong", "OA51 non-statutair 934 kEUR 2026; tick763"),
    ("bud_emp_oa51_mediation_2026", "fod_emploi", 2026, 4246000, "", "", "budgeted", SRC, "strong", "OA51 prog 51/1 social mediation class 4246 kEUR 2026; tick763"),
    # OA52 Humanisation of work
    ("bud_emp_oa52_statutair_2026", "fod_emploi", 2026, 4736000, "", "", "budgeted", SRC, "strong", "OA52 humanisation statutair 4736 kEUR 2026; tick763"),
    ("bud_emp_oa52_contract_2026", "fod_emploi", 2026, 792000, "", "", "budgeted", SRC, "strong", "OA52 non-statutair 792 kEUR 2026; tick763"),
    ("bud_emp_oa52_anti_discrim_2026", "fod_emploi", 2026, 577000, "", "", "budgeted", SRC, "strong", "OA52/5 anti-discrimination service 577 kEUR 2026; tick763"),
    ("bud_emp_oa52_union_org_2026", "fod_emploi", 2026, 650000, "", "", "budgeted", SRC, "strong", "OA52 toelage representative orgs 650 kEUR 2026 flat; tick763"),
    # OA54 Wellbeing at work inspection
    ("bud_emp_oa54_statutair_2026", "fod_emploi", 2026, 14593000, "", "", "budgeted", SRC, "strong", "OA54 wellbeing inspection statutair 14593 kEUR 2026; tick763"),
    ("bud_emp_oa54_contract_2026", "fod_emploi", 2026, 335000, "", "", "budgeted", SRC, "strong", "OA54 non-statutair 335 kEUR 2026; tick763"),
    ("bud_emp_oa54_ops_2026", "fod_emploi", 2026, 1555000, "", "", "budgeted", SRC, "strong", "OA54 permanente ops 1555 kEUR 2026; tick763"),
    ("bud_emp_oa54_fonds_tech_2026", "fod_emploi", 2026, 2160000, "", "", "budgeted", SRC, "strong", "OA54/3 Fonds tech veiligheid statutair class 2160 kEUR 2026; tick763"),
    # OA57 Social laws inspection (largest inspectorate payroll)
    ("bud_emp_oa57_statutair_2026", "fod_emploi", 2026, 26474000, "", "", "budgeted", SRC, "strong", "OA57 social laws inspection statutair 26474 kEUR 2026; tick763"),
    ("bud_emp_oa57_contract_2026", "fod_emploi", 2026, 698000, "", "", "budgeted", SRC, "strong", "OA57 non-statutair 698 kEUR 2026; tick763"),
    ("bud_emp_oa57_ops_2026", "fod_emploi", 2026, 2787000, "", "", "budgeted", SRC, "strong", "OA57 permanente ops 2787 kEUR 2026; tick763"),
    # OA58 SIOD/SIRS
    ("bud_emp_oa58_siod_statutair_2026", "fod_emploi", 2026, 2307000, "", "", "budgeted", SRC, "strong", "OA58 SIOD/SIRS statutair 2307 kEUR 2026; tick763"),
    ("bud_emp_oa58_ops_perm_2026", "fod_emploi", 2026, 237000, "", "", "budgeted", SRC, "strong", "OA58 permanente ops 237 kEUR 2026; tick763"),
    ("bud_emp_oa58_ops_div_2026", "fod_emploi", 2026, 250000, "", "", "budgeted", SRC, "strong", "OA58 diverse ops 250 kEUR 2026; tick763"),
    ("bud_emp_oa58_ops_extra_2026", "fod_emploi", 2026, 164000, "", "", "budgeted", SRC, "strong", "OA58 permanente extra 164 kEUR 2026; tick763"),
    # OA59 Individual labour relations + dots
    ("bud_emp_oa59_statutair_2026", "fod_emploi", 2026, 2540000, "", "", "budgeted", SRC, "strong", "OA59 individual relations statutair 2540 kEUR 2026; tick763"),
    ("bud_emp_oa59_legal_2026", "fod_emploi", 2026, 4001000, "", "", "budgeted", SRC, "strong", "OA59/2 legal studies class 4001 kEUR 2026; tick763"),
    ("bud_emp_oa59_legal_contract_2026", "fod_emploi", 2026, 770000, "", "", "budgeted", SRC, "strong", "OA59/2 non-statutair 770 kEUR 2026; tick763"),
    ("bud_emp_oa59_rva_fed_dot_2026", "rva", 2026, 167664000, "", "", "budgeted", SRC, "strong", "OA59/3 BA 23.59.30424002 RVA/ONEM federal expenditure dot 167664 kEUR 2026; tick763"),
    ("bud_emp_oa59_samenleving_2026", "fod_emploi", 2026, 3630000, "", "", "budgeted", SRC, "strong", "OA59/3 Samenlevingsdienst/service citoyen 3630 kEUR 2026; tick763"),
    # Derived stacks
    ("bud_emp_payroll_major_2026", "fod_emploi", 2026, 80696000, "", "", "derived", SRC, "strong", "Major statutair+contract payroll OA21/40/51/52/54/57/58/59 class ~80.7m 2026; tick763"),
    ("bud_emp_inspection_stack_2026", "fod_emploi", 2026, 49400000, "", "", "derived", SRC, "strong", "Inspection stack OA54+57+58 core ~49.4m 2026 excl fonds tech; tick763"),
    ("bud_emp_ops_core_excl_rva_2026", "fod_emploi", 2026, 105382000, "", "", "derived", SRC, "strong", "SPF Emploi ops core excl RVA federal dot ~105.4m 2026; tick763"),
    ("bud_emp_section23_with_rva_2026", "fod_emploi", 2026, 276676000, "", "", "derived", SRC, "strong", "Section23 class ops+RVA+Samenleving ~276.7m 2026; not full unemployment benefits; tick763"),
    ("bud_dual_emp_inspection_siod_2026", "gg_belgium", 2026, 49400000, "", "", "derived", SRC_DUAL, "strong", "Dual federal labour inspection stack 49.4m SIOD+TWW+TSW vs regional residual; not TE-additive; tick763"),
]

cmt_rows = [
    (
        "cmt_emp_ops_core_2026",
        "FPS Emploi ops core ~105.4m 2026 excl RVA federal dotation",
        "fod_emploi",
        "Labour inspection social dialogue and support",
        "Kamer DOC 56 1281/012 multi OA",
        "2026-01-28",
        2026,
        2026,
        105382000,
        '{"oa21_support":26386000,"oa40":1485000,"oa51":11885000,"oa52":6755000,"oa54":18643000,"oa57":29959000,"oa58":2958000,"oa59_excl_dots":7311000,"sum":105382000,"note":"derived from main BA lines"}',
        0,
        "active",
        URL,
        "Run federal employment labour and social dialogue administration",
        "FTE by inspectorate FOI; dual regional inspection residual",
        SRC,
        "strong",
        "Federal>Emploi>ops_core",
        "tick763 major residual",
    ),
    (
        "cmt_emp_inspection_stack_2026",
        "Federal labour inspection stack OA54+57+58 ~49.4m 2026",
        "fod_emploi",
        "Wellbeing social-laws SIOD inspectors",
        "Kamer 1281/012 OA54 57 58",
        "2026-01-28",
        2026,
        2026,
        49400000,
        '{"oa54_core":16483000,"oa57_core":29959000,"oa58_core":2958000,"fonds_tech_extra":2160000,"note":"core excl fonds tech 2.16m"}',
        0,
        "active",
        URL,
        "Enforce labour wellbeing and social laws and coordinate SIOD",
        "FTE and audit yield FOI dual regional",
        SRC,
        "strong",
        "Federal>Emploi>inspection",
        "tick763",
    ),
    (
        "cmt_emp_rva_fed_dot_2026",
        "RVA/ONEM federal expenditure dotation via SPF Emploi 167.7m 2026",
        "rva",
        "ONEM federal expense channel",
        "Kamer 1281/012 BA 23.59.30424002",
        "2026-01-28",
        2026,
        2026,
        167664000,
        '{"2024":158351000,"2025":165245000,"2026":167664000,"2027":166537000,"note":"federal expenditure channel not full unemployment benefits mass which sits in SS/ONEM institutional"}',
        0,
        "active",
        URL,
        "Channel federal expenditure through ONEM",
        "Reconcile full ONEM TCO with SS 1281/013 FOI",
        SRC,
        "strong",
        "Federal>Emploi>RVA_fed_dot",
        "tick763",
    ),
    (
        "cmt_emp_payroll_2026",
        "FPS Emploi major payroll class ~80.7m 2026",
        "fod_emploi",
        "FPS Emploi staff",
        "Kamer 1281/012 statutair+contract lines",
        "2026-01-28",
        2026,
        2026,
        80696000,
        '{"oa21":13749000,"oa40":1485000,"oa51":7639000,"oa52":5528000,"oa52_anti":577000,"oa54":14928000,"oa57":27172000,"oa58":2307000,"oa59":7311000,"sum":80696000}',
        0,
        "active",
        URL,
        "Pay employment administration and inspectorate staff",
        "FTE recon FOI dual Finance/Police",
        SRC,
        "strong",
        "Federal>Emploi>payroll",
        "tick763",
    ),
    (
        "cmt_emp_siod_2026",
        "SIOD/SIRS social fraud coordination OA58 ~3.0m 2026",
        "fod_emploi",
        "SIOD staff and partners",
        "Kamer 1281/012 OA58",
        "2026-01-28",
        2026,
        2026,
        2958000,
        '{"statutair":2307000,"ops_sum":651000,"note":"coordination body; bulk inspection in OA54/57"}',
        0,
        "active",
        URL,
        "Coordinate fight against illegal work and social fraud",
        "KPI yield FOI dual ONSS/INAMI",
        SRC,
        "strong",
        "Federal>Emploi>SIOD",
        "tick763",
    ),
    (
        "cmt_emp_samenleving_2026",
        "Samenlevingsdienst / service citoyen 3.63m 2026",
        "fod_emploi",
        "Citizen service programme",
        "Kamer 1281/012 BA 23.59.30416001",
        "2026-01-28",
        2026,
        2026,
        3630000,
        '{"2026":3630000}',
        0,
        "active",
        URL,
        "Stand up federal citizen service",
        "Take-up KPI FOI",
        SRC,
        "strong",
        "Federal>Emploi>samenleving",
        "tick763",
    ),
    (
        "cmt_dual_emp_inspection_tick763",
        "Dual federal labour inspection 49.4m SIOD stack vs regional residual",
        "gg_belgium",
        "Labour inspection multi-level map",
        "Kamer 1281/012 + dual PES residual",
        "2026-01-28",
        2026,
        2026,
        0,
        '{"fed_insp_m":49.4,"social_laws_m":29.96,"wellbeing_m":16.48,"siod_m":2.96,"rva_fed_dot_m":167.7,"ops_excl_rva_m":105.4,"note":"not TE-additive; dual regional inspection and full ONEM residual"}',
        0,
        "active",
        URL,
        "Comparable multi-level labour enforcement transparency",
        "Regional dual unit-cost FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>labour_inspection",
        "tick763",
    ),
]

lb_rows = [
    (
        "lb_emp_rva_fed_dot_167_7m_2026",
        "RVA federal expenditure dot via SPF Emploi 167.7m 2026",
        "L5",
        "transfer",
        "Federal>Emploi>RVA_fed_dot",
        167664000,
        167664000,
        "Strong Kamer BA 23.59.30424002; channel not full unemployment benefits",
        "strong",
        SRC,
        "ONEM federal expense channel",
        "Federal expenditure through ONEM",
        "Full ONEM TCO residual FOI dual SS",
        4.0,
        8.0,
        4,
        5.7,
        "Publish ONEM recon FOI with 1281/013",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_emp_ops_core_105_4m_2026",
        "FPS Emploi ops core ~105.4m 2026 excl RVA dot",
        "L5",
        "programme",
        "Federal>Emploi>ops_core",
        105382000,
        105382000,
        "Strong Kamer multi-OA derived stack; inspectorates dominate",
        "strong",
        SRC,
        "Workers employers social partners",
        "Run federal employment administration",
        "FTE efficiency residual",
        4.0,
        7.0,
        4,
        5.3,
        "Publish FTE by OA FOI",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_emp_inspection_49_4m_2026",
        "Federal labour inspection stack ~49.4m 2026",
        "L5",
        "ops",
        "Federal>Emploi>inspection",
        49400000,
        49400000,
        "Strong OA54+57+58; social laws 26.5m payroll alone",
        "strong",
        SRC,
        "Employers workers",
        "Enforce labour wellbeing and social laws",
        "Audit yield residual dual regional",
        5.0,
        6.5,
        4,
        5.55,
        "FTE+yield FOI dual SIOD",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_emp_social_laws_insp_26_5m_2026",
        "Social laws inspection OA57 statutair 26.5m 2026",
        "L5",
        "personnel",
        "Federal>Emploi>TSW_inspection",
        26474000,
        26474000,
        "Strong largest single inspectorate payroll line",
        "strong",
        SRC,
        "Social law inspectors",
        "Control social legislation compliance",
        "Unit cost per control FOI",
        5.0,
        6.0,
        3,
        5.2,
        "Publish controls/yield FOI",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_emp_payroll_80_7m_2026",
        "FPS Emploi major payroll ~80.7m 2026",
        "L5",
        "personnel",
        "Federal>Emploi>payroll",
        80696000,
        80696000,
        "Strong statutair+contract major OA lines",
        "strong",
        SRC,
        "Emploi staff",
        "Staff employment department",
        "FTE residual dual",
        3.5,
        6.5,
        4,
        4.85,
        "FTE publish FOI",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_emp_siod_3_0m_2026",
        "SIOD/SIRS coordination ~3.0m 2026",
        "L5",
        "agency",
        "Federal>Emploi>SIOD",
        2958000,
        2958000,
        "Strong OA58; coordination only bulk in TSW/TWW",
        "strong",
        SRC,
        "Social fraud partners",
        "Coordinate social fraud fight",
        "KPI yield residual",
        5.5,
        4.5,
        3,
        4.85,
        "Fraud yield FOI dual ONSS",
        "active",
        "",
        "tick763",
    ),
    (
        "lb_dual_emp_inspection_2026",
        "Dual federal labour inspection map 49.4m 2026",
        "L5",
        "ops",
        "Belgium>dual>labour_inspection",
        49400000,
        0,
        "Strong dual SIOD stack vs regional residual; not TE-additive",
        "strong",
        SRC_DUAL,
        "BE multi-level enforcement",
        "Map dual labour inspection cost",
        "Primary dual residual FOI",
        5.5,
        6.5,
        3,
        5.7,
        "Cross-entity unit-cost FOI",
        "active",
        "",
        "tick763",
    ),
]

src_rows = [
    (
        SRC,
        "Kamer DOC 56 1281/012 FOD Werkgelegenheid SPF Emploi budget justification 2026",
        URL,
        "Kamer / Chambre",
        "2026-08-02",
        "parliamentary",
        "Strong tick763: ops core excl RVA ~105.4m (OA21 support 26.4 OA51 11.9 OA54 18.6 OA57 30.0 OA58 SIOD 3.0); payroll ~80.7m; social laws insp 26.5m; RVA federal dot 167.7m; Samenleving 3.63m; section class ~277m; raw 56K1281012.pdf 151p",
    ),
    (
        SRC_DUAL,
        "Dual FPS Emploi inspection SIOD vs regional residual tick763",
        URL,
        "DOGE synthesis Kamer emploi dual PES/inspection",
        "2026-08-02",
        "synthesis",
        "Strong dual tick763 not TE-additive: fed inspection 49.4m social laws 26.5 SIOD 3.0 RVA fed channel 167.7 ops 105.4 vs regional labour inspection residual and full ONEM",
    ),
]

foi_row = (
    "gap_emploi_fte_inspection_rva_l5",
    "Federal>Emploi>FTE_inspection_RVA_L5",
    "fod_emploi",
    "FTE by OA 21/40/51/52/54/57/58/59 2024-2026 statutair vs contract; controls and recovery yield TSW/TWW/SIOD 2023-2025; full recon RVA federal 167.7m vs ONEM institutional budget and SS 1281/013; dual regional labour inspection unit-cost residual",
    "SPF Emploi OA totals and RVA federal channel now public; FTE yield and full ONEM TCO residual dual SS",
    8,
    "FOD Werkgelegenheid / RVA-ONEM / FOD Sociale Zekerheid / IBZ FOI",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_emploi_fte_inspection_rva_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_emp_ops_core_2026|cmt_emp_inspection_stack_2026|cmt_emp_rva_fed_dot_2026|cmt_dual_emp_inspection_tick763",
    "lb_emp_ops_core_105_4m_2026|lb_emp_inspection_49_4m_2026|lb_emp_rva_fed_dot_167_7m_2026",
    TS,
    TS,
    "tick763 Kamer 1281/012 primary; human send only",
)


def ensure_entities():
    path = base / "entities.csv"
    text = path.read_text(encoding="utf-8")
    n = 0
    rows = []
    if "\nfod_emploi," not in text:
        rows.append(
            (
                "fod_emploi",
                "FOD Werkgelegenheid Arbeid en Sociaal Overleg",
                "SPF Emploi Travail et Concertation sociale",
                "FPS Employment Labour and Social Dialogue",
                "ministry",
                "sec_federal",
                "bi",
                "https://emploi.belgique.be",
                "",
                "",
                "Labour inspection SIOD social dialogue; tick763",
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
        if ln.startswith("rq_754,"):
            out.append(
                "rq_754,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                "Next residual: Emploi 1281/012 or SS 1281/013 or public debt 1281/019 residual; Finance ops filled tick762,,"
                f"2026-08-02T22:00:00Z,{TS},"
                "tick763 Emploi 1281/012: ops 105.4m payroll 80.7 inspection 49.4 social laws 26.5 RVA fed 167.7 SIOD 3.0; FOI ready"
            )
        else:
            out.append(ln)
    out.append(
        "rq_755,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Next residual: SS 1281/013 or public debt 1281/019 or residual dual inspection/ONEM; Emploi filled tick763,,"
        f"{TS},,"
        "spawned tick763 after rq_754"
    )
    rq.write_text("\n".join(out) + "\n", encoding="utf-8")

    (base / "loop_state.csv").write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_754,763,no,"
        "tick763 Emploi ops 105.4m payroll 80.7 inspection 49.4 RVA fed 167.7; next rq_755 SS/Debt; progress@770 in 7; rq_116 deferred\n",
        encoding="utf-8",
    )
    print(
        f"OK tick763 entities+{n} budgets+{len(bud_rows)} cmt+{len(cmt_rows)} "
        f"lb+{len(lb_rows)} src+{len(src_rows)} foi+1"
    )


if __name__ == "__main__":
    main()
