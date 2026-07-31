# tick764 Kamer DOC 56 1281/013 SPF Securite sociale residual mega dots + ops
import csv
from pathlib import Path

base = Path("docs/doge/data")
SRC = "src_kamer_ss_1281_013_2026"
SRC_DUAL = "src_dual_ss_dots_tick764"
URL = "https://www.dekamer.be/FLWB/PDF/56/1281/56K1281013.pdf"
TS = "2026-08-03T00:00:00Z"

# All amounts: kEUR * 1000 from 2026 column (3rd of 2024..2029 series)
bud_rows = [
    # OA21 support
    ("bud_ss_oa21_statutair_2026", "fod_ss", 2026, 39228000, "", "", "budgeted", SRC, "strong", "OA21 statutair 39228 kEUR 2026; tick764"),
    ("bud_ss_oa21_contract_2026", "fod_ss", 2026, 5079000, "", "", "budgeted", SRC, "strong", "OA21 non-statutair 5079 kEUR 2026; tick764"),
    ("bud_ss_oa21_egov_smals_2026", "fod_ss", 2026, 4330000, "", "", "budgeted", SRC, "strong", "OA21 eGov+Smals detached 4330 kEUR 2026 dual Smals; tick764"),
    ("bud_ss_oa21_ops_2026", "fod_ss", 2026, 7038000, "", "", "budgeted", SRC, "strong", "OA21 diverse ops 7038 kEUR 2026; tick764"),
    ("bud_ss_oa21_it_invest_2026", "fod_ss", 2026, 680000, "", "", "budgeted", SRC, "strong", "OA21 IT invest 680 kEUR 2026; tick764"),
    ("bud_ss_oa21_oisz_revisor_2026", "fod_ss", 2026, 532000, "", "", "budgeted", SRC, "strong", "OA21 OISZ auditors 532 kEUR 2026 flat; tick764"),
    ("bud_ss_oa21_fonct_2026", "fod_ss", 2026, 3804000, "", "", "budgeted", SRC, "strong", "OA21 general fonct 3804 kEUR 2026; tick764"),
    # Handicap
    ("bud_ss_handicap_alloc_2026", "fod_ss", 2026, 3285541000, "", "", "budgeted", SRC, "strong", "OA55 BA 55.31.343106 handicap allocations 3285541 kEUR 2026; tick764"),
    ("bud_ss_handicap_eval_doctors_2026", "fod_ss", 2026, 6227000, "", "", "budgeted", SRC, "strong", "OA55 handicap eval doctor admin 6227 kEUR 2026; tick764"),
    ("bud_ss_handicap_contentieux_2026", "fod_ss", 2026, 1688000, "", "", "budgeted", SRC, "strong", "OA55 handicap litigation 1688 kEUR 2026; tick764"),
    # KCE SIGEDIS
    ("bud_ss_sigedis_2026", "fod_ss", 2026, 4285000, "", "", "budgeted", SRC, "strong", "BA 58.41.421013 SIGeDIS 4285 kEUR 2026; tick764"),
    ("bud_ss_kce_2026", "fod_ss", 2026, 1338000, "", "", "budgeted", SRC, "strong", "BA 58.41.422001 KCE 1338 kEUR 2026; tick764"),
    # RSZ/ONSS
    ("bud_ss_rsz_osz_funds_2026", "rsz", 2026, 271225000, "", "", "budgeted", SRC, "strong", "BA 58.42.421009 RSZ OSZ 3 funds 271225 kEUR 2026; tick764"),
    ("bud_ss_rsz_globale_2026", "rsz", 2026, 2665625000, "", "", "budgeted", SRC, "strong", "BA 58.42.428003 RSZ Globale rijkstoelage 2665625 kEUR 2026; tick764"),
    ("bud_ss_rsz_evenwicht_2026", "rsz", 2026, 5644566000, "", "", "budgeted", SRC, "strong", "BA 58.42.428004 RSZ evenwichtsdotatie 5644566 kEUR 2026 (was 6751m 2025); tick764"),
    # RSVZ/INASTI
    ("bud_ss_rsvz_globale_2026", "rsvz", 2026, 478080000, "", "", "budgeted", SRC, "strong", "BA 58.43.428001 RSVZ globale 478080 kEUR 2026; tick764"),
    ("bud_ss_rsvz_evenwicht_2026", "rsvz", 2026, 597961000, "", "", "budgeted", SRC, "strong", "BA 58.43.428002 RSVZ evenwicht 597961 kEUR 2026; tick764"),
    # FPD
    ("bud_ss_fpd_igo_2026", "fpd", 2026, 1034642000, "", "", "budgeted", SRC, "strong", "BA 58.44.343108 FPD IGO/GRAPA 1034642 kEUR 2026; tick764"),
    ("bud_ss_fpd_igo_ops_2026", "fpd", 2026, 2185000, "", "", "budgeted", SRC, "strong", "BA 58.44.421006 FPD IGO ops 2185 kEUR 2026; tick764"),
    ("bud_ss_fpd_public_pensions_2026", "fpd", 2026, 14584187000, "", "", "budgeted", SRC, "strong", "BA 58.45.421001 FPD public-sector pensions 14584187 kEUR 2026; tick764"),
    ("bud_ss_fpd_war_repair_2026", "fpd", 2026, 61315000, "", "", "budgeted", SRC, "strong", "BA 58.45.421002 war/repair pensions 61315 kEUR 2026; tick764"),
    ("bud_ss_fpd_work_accidents_2026", "fpd", 2026, 61029000, "", "", "budgeted", SRC, "strong", "BA 58.45.421003 work accident rents 61029 kEUR 2026; tick764"),
    ("bud_ss_fpd_public_ops_2026", "fpd", 2026, 56302000, "", "", "budgeted", SRC, "strong", "BA 58.45.421004 public pension ops 56302 kEUR 2026; tick764"),
    ("bud_ss_fpd_hr_rail_2026", "fpd", 2026, 1325778000, "", "", "budgeted", SRC, "strong", "BA 58.45.421005 HR-Rail pensions 1325778 kEUR 2026; tick764"),
    ("bud_ss_fpd_war_victims_2026", "fpd", 2026, 11706000, "", "", "budgeted", SRC, "strong", "BA 58.45.421006 war victims civil 11706 kEUR 2026; tick764"),
    ("bud_ss_fpd_local_solidarity_2026", "fpd", 2026, 50000000, "", "", "budgeted", SRC, "strong", "BA 58.45.421020 local gov solidarity pension fund 50000 kEUR 2026; tick764"),
    # FEDRIS HZIV RIZIV
    ("bud_ss_fedris_2026", "fedris", 2026, 9148000, "", "", "budgeted", SRC, "strong", "BA 58.46.426001 FEDRIS 9148 kEUR 2026; tick764"),
    ("bud_ss_hziv_2026", "fod_ss", 2026, 8457000, "", "", "budgeted", SRC, "strong", "BA 58.47.422035 HZIV/CAAMI war invalids 8457 kEUR 2026; tick764"),
    ("bud_ss_riziv_care_dot_2026", "riziv", 2026, 487950000, "", "", "budgeted", SRC, "strong", "BA 58.48.422001 RIZIV care state grant 487950 kEUR 2026; tick764"),
    # Derived stacks
    ("bud_ss_rsz_dots_stack_2026", "rsz", 2026, 8581416000, "", "", "derived", SRC, "strong", "RSZ dots sum OSZ+globale+evenwicht 8581.4m 2026; tick764"),
    ("bud_ss_rsvz_dots_stack_2026", "rsvz", 2026, 1076041000, "", "", "derived", SRC, "strong", "RSVZ dots globale+evenwicht 1076.0m 2026; tick764"),
    ("bud_ss_fpd_channel_stack_2026", "fpd", 2026, 17187144000, "", "", "derived", SRC, "strong", "FPD channel public+HR-Rail+IGO+ops+war+local ~17.187bn 2026; tick764"),
    ("bud_ss_mega_dots_stack_2026", "fod_ss", 2026, 30641320000, "", "", "derived", SRC, "strong", "Section24 mega dots+handicap+RIZIV care ~30.641bn 2026 excl pure SPF ops; tick764"),
    ("bud_ss_ops_core_2026", "fod_ss", 2026, 60691000, "", "", "derived", SRC, "strong", "OA21 major ops+payroll+eGov class ~60.7m 2026 excl mega transfers; tick764"),
    ("bud_dual_ss_smals_egov_2026", "gg_belgium", 2026, 4330000, "", "", "derived", SRC_DUAL, "strong", "Dual SS eGov/Smals 4.33m vs Finance 39.6 Emploi residual; not TE-additive; tick764"),
]

cmt_rows = [
    (
        "cmt_ss_mega_dots_2026",
        "SPF SS section24 mega dots+handicap ~30.64bn 2026",
        "fod_ss",
        "RSZ RSVZ FPD RIZIV handicap beneficiaries",
        "Kamer DOC 56 1281/013 OA58+OA55",
        "2026-01-28",
        2026,
        2026,
        30641320000,
        '{"rsz_m":8581.4,"rsvz_m":1076.0,"fpd_m":17187.1,"handicap_m":3285.5,"riziv_care_m":488.0,"sigedis_kce_m":5.6,"fedris_hziv_m":17.6,"sum_m":30641.3,"note":"state transfers channel; not full SS institutional TCO; dual RSZ/ONSS residual"}',
        0,
        "active",
        URL,
        "Finance social security via state dots and federal benefit channels",
        "Full OISZ institutional recon FOI dual",
        SRC,
        "strong",
        "Federal>SS>mega_dots",
        "tick764 major residual",
    ),
    (
        "cmt_ss_fpd_public_pensions_2026",
        "FPD public-sector pensions channel ~14.58bn 2026",
        "fpd",
        "Public-sector pensioners",
        "Kamer 1281/013 BA 58.45.421001",
        "2026-01-28",
        2026,
        2026,
        14584187000,
        '{"2024":13898001000,"2025":14096676000,"2026":14584187000,"path_plus_m":487.5}',
        0,
        "active",
        URL,
        "Pay public-sector pensions via FPD",
        "Reform path FOI dual private regime",
        SRC,
        "strong",
        "Federal>SS>FPD_public",
        "tick764",
    ),
    (
        "cmt_ss_rsz_evenwicht_2026",
        "RSZ evenwichtsdotatie 5.645bn 2026 (down from 6.751bn 2025)",
        "rsz",
        "ONSS global management workers regime",
        "Kamer 1281/013 BA 58.42.428004",
        "2026-01-28",
        2026,
        2026,
        5644566000,
        '{"2024":6142268000,"2025":6751113000,"2026":5644566000,"path_minus_m":1106.5}',
        0,
        "active",
        URL,
        "Balance workers social security global management",
        "Path drivers FOI",
        SRC,
        "strong",
        "Federal>SS>RSZ_evenwicht",
        "tick764",
    ),
    (
        "cmt_ss_handicap_alloc_2026",
        "Federal handicap allocations 3.286bn 2026",
        "fod_ss",
        "Persons with disabilities",
        "Kamer 1281/013 BA 55.31.343106",
        "2026-01-28",
        2026,
        2026,
        3285541000,
        '{"2024":2956943000,"2025":3091060000,"2026":3285541000,"path_plus_m":194.5,"law":"27/02/1987"}',
        0,
        "active",
        URL,
        "Pay income replacement and integration allowances",
        "Caseload unit-cost FOI dual regional disability",
        SRC,
        "strong",
        "Federal>SS>handicap_alloc",
        "tick764",
    ),
    (
        "cmt_ss_rsz_globale_2026",
        "RSZ globale rijkstoelage 2.666bn 2026",
        "rsz",
        "ONSS global management",
        "Kamer 1281/013 BA 58.42.428003",
        "2026-01-28",
        2026,
        2026,
        2665625000,
        '{"2024":2565587000,"2025":2632621000,"2026":2665625000}',
        0,
        "active",
        URL,
        "Base state subsidy to workers SS global management",
        "Optional dual FOI",
        SRC,
        "strong",
        "Federal>SS>RSZ_globale",
        "tick764",
    ),
    (
        "cmt_ss_fpd_hr_rail_2026",
        "FPD HR-Rail pensions 1.326bn 2026",
        "fpd",
        "Former HR-Rail staff pensioners",
        "Kamer 1281/013 BA 58.45.421005",
        "2026-01-28",
        2026,
        2026,
        1325778000,
        '{"2024":1291485000,"2025":1280300000,"2026":1325778000}',
        0,
        "active",
        URL,
        "Pay former railway staff public pensions",
        "Dual SNCB residual FOI",
        SRC,
        "strong",
        "Federal>SS>FPD_HR_Rail",
        "tick764",
    ),
    (
        "cmt_ss_fpd_igo_2026",
        "FPD IGO/GRAPA income guarantee elderly 1.035bn 2026",
        "fpd",
        "Elderly with low income",
        "Kamer 1281/013 BA 58.44.343108",
        "2026-01-28",
        2026,
        2026,
        1034642000,
        '{"2024":1014729000,"2025":1006104000,"2026":1034642000}',
        0,
        "active",
        URL,
        "Income guarantee for the elderly via FPD",
        "Take-up FOI dual regional min income",
        SRC,
        "strong",
        "Federal>SS>FPD_IGO",
        "tick764",
    ),
    (
        "cmt_ss_ops_core_2026",
        "SPF SS OA21 ops core ~60.7m 2026 excl mega dots",
        "fod_ss",
        "SS administration staff and support",
        "Kamer 1281/013 OA21",
        "2026-01-28",
        2026,
        2026,
        60691000,
        '{"statutair":39228000,"contract":5079000,"egov_smals":4330000,"ops":7038000,"it":680000,"revisor":532000,"fonct":3804000}',
        0,
        "active",
        URL,
        "Run federal social security department support",
        "FTE FOI dual Emploi",
        SRC,
        "strong",
        "Federal>SS>ops_core",
        "tick764",
    ),
    (
        "cmt_dual_ss_dots_tick764",
        "Dual SPF SS mega dots 30.64bn vs Emploi ops residual and Smals dual",
        "gg_belgium",
        "SS transfer architecture map",
        "Kamer 1281/013 + prior Emploi/Finance",
        "2026-01-28",
        2026,
        2026,
        0,
        '{"mega_dots_bn":30.64,"fpd_bn":17.19,"rsz_bn":8.58,"handicap_bn":3.29,"rsvz_bn":1.08,"riziv_care_m":488,"ops_m":60.7,"smals_m":4.33,"note":"not TE-additive; institutional OISZ TCO residual"}',
        0,
        "active",
        URL,
        "Comparable multi-channel SS financing transparency",
        "OISZ recon FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>ss_dots",
        "tick764",
    ),
]

lb_rows = [
    (
        "lb_ss_mega_dots_30_64bn_2026",
        "SPF SS mega dots+handicap channel ~30.64bn 2026",
        "L5",
        "transfer",
        "Federal>SS>mega_dots",
        30641320000,
        30641320000,
        "Strong Kamer OA58+OA55; state transfer channel not full OISZ TCO",
        "strong",
        SRC,
        "SS beneficiaries and OISZ",
        "Channel federal financing of social security",
        "Core entitlement stack; not pure waste",
        3.5,
        9.5,
        6,
        6.35,
        "Publish OISZ recon FOI dual",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_fpd_public_14_58bn_2026",
        "FPD public-sector pensions 14.58bn 2026",
        "L5",
        "transfer",
        "Federal>SS>FPD_public",
        14584187000,
        14584187000,
        "Strong BA 58.45.421001 path +488m vs 2025",
        "strong",
        SRC,
        "Public-sector pensioners",
        "Pay public-sector pensions",
        "Largest single SS channel line",
        4.0,
        9.5,
        6,
        6.55,
        "Reform path FOI dual private",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_rsz_evenwicht_5_65bn_2026",
        "RSZ evenwichtsdotatie 5.645bn 2026",
        "L5",
        "transfer",
        "Federal>SS>RSZ_evenwicht",
        5644566000,
        5644566000,
        "Strong path -1.11bn vs 2025 6.751bn",
        "strong",
        SRC,
        "Workers SS global management",
        "Balance workers regime financing",
        "Material path drop residual drivers",
        4.5,
        9.0,
        5,
        6.55,
        "Publish path drivers FOI",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_handicap_3_29bn_2026",
        "Federal handicap allocations 3.286bn 2026",
        "L5",
        "transfer",
        "Federal>SS>handicap_alloc",
        3285541000,
        3285541000,
        "Strong BA 55.31.343106 path +194m; dual regional disability residual",
        "strong",
        SRC,
        "Persons with disabilities",
        "Income replacement and integration allowances",
        "Core social protection; unit-cost residual",
        3.5,
        8.5,
        4,
        5.75,
        "Caseload unit-cost FOI dual",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_rsz_globale_2_67bn_2026",
        "RSZ globale rijkstoelage 2.666bn 2026",
        "L5",
        "transfer",
        "Federal>SS>RSZ_globale",
        2665625000,
        2665625000,
        "Strong BA 58.42.428003",
        "strong",
        SRC,
        "Workers SS",
        "Base state subsidy ONSS global",
        "Core financing channel",
        3.5,
        8.5,
        4,
        5.75,
        "Optional dual FOI",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_fpd_hr_rail_1_33bn_2026",
        "FPD HR-Rail pensions 1.326bn 2026",
        "L5",
        "transfer",
        "Federal>SS>FPD_HR_Rail",
        1325778000,
        1325778000,
        "Strong BA 58.45.421005 dual SNCB residual",
        "strong",
        SRC,
        "Former railway pensioners",
        "Pay HR-Rail public pensions",
        "Sector legacy pension channel",
        4.5,
        8.0,
        4,
        5.95,
        "Dual SNCB FOI",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_fpd_igo_1_03bn_2026",
        "FPD IGO/GRAPA 1.035bn 2026",
        "L5",
        "transfer",
        "Federal>SS>FPD_IGO",
        1034642000,
        1034642000,
        "Strong BA 58.44.343108 elderly income guarantee",
        "strong",
        SRC,
        "Low-income elderly",
        "Income guarantee elderly",
        "Safety net; dual regional residual",
        3.0,
        7.5,
        3,
        5.0,
        "Take-up FOI dual",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_rsvz_dots_1_08bn_2026",
        "RSVZ/INASTI dots stack 1.076bn 2026",
        "L5",
        "transfer",
        "Federal>SS>RSVZ_dots",
        1076041000,
        1076041000,
        "Strong globale 478m + evenwicht 598m",
        "strong",
        SRC,
        "Self-employed SS",
        "Finance self-employed SS regime",
        "Dual workers/self-employed",
        4.0,
        7.5,
        4,
        5.55,
        "Dual FOI optional",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_ss_ops_core_60_7m_2026",
        "SPF SS OA21 ops core ~60.7m 2026",
        "L5",
        "ops",
        "Federal>SS>ops_core",
        60691000,
        60691000,
        "Strong payroll 44.3 + eGov 4.33 + ops; excl mega dots",
        "strong",
        SRC,
        "SS admin",
        "Run SPF SS support",
        "Overhead vs mega transfer scale",
        4.0,
        6.0,
        3,
        4.85,
        "FTE FOI dual Emploi",
        "active",
        "",
        "tick764",
    ),
    (
        "lb_dual_ss_dots_2026",
        "Dual SPF SS mega dots map 30.64bn 2026",
        "L5",
        "transfer",
        "Belgium>dual>ss_dots",
        30641320000,
        0,
        "Strong dual FPD/RSZ/handicap vs Emploi residual Smals; not TE-additive",
        "strong",
        SRC_DUAL,
        "BE SS multi-channel",
        "Map dual SS financing",
        "Primary dual mega residual",
        5.0,
        9.0,
        4,
        6.5,
        "OISZ recon FOI",
        "active",
        "",
        "tick764",
    ),
]

src_rows = [
    (
        SRC,
        "Kamer DOC 56 1281/013 FOD Sociale Zekerheid SPF SS budget justification 2026",
        URL,
        "Kamer / Chambre",
        "2026-08-03",
        "parliamentary",
        "Strong tick764: mega dots+handicap ~30.64bn (FPD public 14.58 HR-Rail 1.33 IGO 1.03; RSZ evenwicht 5.645 globale 2.666 OSZ 0.271; RSVZ 1.076; handicap 3.286; RIZIV care 0.488); ops OA21 ~60.7m eGov/Smals 4.33; raw 56K1281013.pdf 51p",
    ),
    (
        SRC_DUAL,
        "Dual SPF SS mega dots vs Emploi residual and Smals tick764",
        URL,
        "DOGE synthesis Kamer SS dual Emploi/Finance Smals",
        "2026-08-03",
        "synthesis",
        "Strong dual tick764 not TE-additive: mega 30.64bn FPD 17.19 RSZ 8.58 handicap 3.29 vs Emploi ops 105m RVA channel 168m; Smals SS 4.33 vs Finance 39.6",
    ),
]

foi_row = (
    "gap_ss_oisz_recon_fte_l5",
    "Federal>SS>OISZ_recon_FTE_L5",
    "fod_ss",
    "Reconcile section24 mega dots ~30.64bn with institutional OISZ budgets (RSZ RSVZ FPD RIZIV FEDRIS) cash 2024-2026 no double-count; FTE OA21/50/52/55/56/57; caseload unit-cost handicap allocations; path drivers RSZ evenwicht -1.11bn 2025-26; dual regional disability and private pension residual",
    "Kamer 1281/013 transfer channels now public; institutional recon and FTE residual",
    9,
    "FOD Sociale Zekerheid / RSZ / FPD / RIZIV / IBZ FOI",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_ss_oisz_recon_fte_l5.md",
    "ready",
    "2026-08-03",
    "",
    "",
    "",
    "",
    "cmt_ss_mega_dots_2026|cmt_ss_fpd_public_pensions_2026|cmt_ss_rsz_evenwicht_2026|cmt_dual_ss_dots_tick764",
    "lb_ss_mega_dots_30_64bn_2026|lb_ss_fpd_public_14_58bn_2026|lb_ss_rsz_evenwicht_5_65bn_2026",
    TS,
    TS,
    "tick764 Kamer 1281/013 primary; human send only",
)


def ensure_entities():
    path = base / "entities.csv"
    text = path.read_text(encoding="utf-8")
    n = 0
    rows = []
    candidates = [
        ("fod_ss", "FOD Sociale Zekerheid", "SPF Securite sociale", "FPS Social Security", "ministry", "sec_federal", "bi", "https://socialsecurity.belgium.be", "", "", "SS mega dots channel; tick764"),
        ("rsz", "Rijksdienst voor Sociale Zekerheid RSZ", "ONSS", "National Social Security Office", "parastatal", "sec_ss", "bi", "https://www.rsz.be", "", "", "Workers SS global management; tick764"),
        ("rsvz", "Rijksinstituut voor de Sociale Verzekeringen der Zelfstandigen RSVZ", "INASTI", "National Institute for Social Insurance of Self-employed", "parastatal", "sec_ss", "bi", "https://www.rsvz.be", "", "", "Self-employed SS; tick764"),
        ("fpd", "Federale Pensioendienst FPD", "Service federal des Pensions SFP", "Federal Pension Service", "parastatal", "sec_ss", "bi", "https://www.sfpd.fgov.be", "", "", "Public pensions IGO HR-Rail; tick764"),
        ("fedris", "Federaal agentschap voor beroepsrisico's FEDRIS", "FEDRIS", "Federal Agency for Occupational Risks", "parastatal", "sec_ss", "bi", "https://www.fedris.be", "", "", "Occupational risks; tick764"),
    ]
    for r in candidates:
        if f"\n{r[0]}," not in text and not text.startswith(f"{r[0]},"):
            rows.append(r)
    # riziv may already exist
    if "\nriziv," not in text and not text.startswith("riziv,"):
        rows.append(
            ("riziv", "RIZIV", "INAMI", "National Institute for Health and Disability Insurance", "parastatal", "sec_ss", "bi", "https://www.riziv.fgov.be", "", "", "Health insurance; tick764 care grant")
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
        if ln.startswith("rq_755,"):
            out.append(
                "rq_755,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                "Next residual: SS 1281/013 or public debt 1281/019 or residual dual inspection/ONEM; Emploi filled tick763,,"
                f"2026-08-02T23:00:00Z,{TS},"
                "tick764 SS 1281/013: mega dots 30.64bn FPD public 14.58 RSZ eq 5.65 handicap 3.29; FOI prio9 ready"
            )
        else:
            out.append(ln)
    out.append(
        "rq_756,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Next residual: public debt 1281/019 or OAP 022/023 or residual dual OISZ; SS filled tick764,,"
        f"{TS},,"
        "spawned tick764 after rq_755"
    )
    rq.write_text("\n".join(out) + "\n", encoding="utf-8")

    (base / "loop_state.csv").write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        f"main,continuous,hole_fill,{TS},rq_755,764,no,"
        "tick764 SS mega dots 30.64bn FPD 14.58 RSZ eq 5.65 handicap 3.29; next rq_756 Debt/OAP; progress@770 in 6; rq_116 deferred\n",
        encoding="utf-8",
    )
    print(
        f"OK tick764 entities+{n} budgets+{len(bud_rows)} cmt+{len(cmt_rows)} "
        f"lb+{len(lb_rows)} src+{len(src_rows)} foi+1"
    )


if __name__ == "__main__":
    main()
