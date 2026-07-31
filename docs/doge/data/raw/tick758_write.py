# tick758 Kamer DOC 56 1281/016 Mobility residual: NMBS/Infrabel/bpost/skeyes dual
import csv
from pathlib import Path

base = Path("docs/doge/data")
SRC = "src_kamer_mobility_1281_016_2026"
SRC_DUAL = "src_dual_mobility_rail_bpost_tick758"
URL = "https://www.dekamer.be/FLWB/PDF/56/1281/56K1281016.pdf"
# Tables in kEUR; store full EUR

bud_rows = [
    # bpost
    ("bud_bpost_sgei_rem_2024", "bpost", 2024, 153233000, "", "", "outturn", SRC, "strong", "BA 33.41.52.312207 bpost SGEI rem 153233 kEUR 2024; tick758"),
    ("bud_bpost_sgei_rem_2025", "bpost", 2025, 153300000, "", "", "budgeted", SRC, "strong", "bpost SGEI 153300 kEUR 2025; tick758"),
    ("bud_bpost_sgei_rem_2026", "bpost", 2026, 154917000, "", "", "budgeted", SRC, "strong", "bpost SGEI rem eng=liq 154917 kEUR 2026; path falls to 104917 from 2027; tick758"),
    ("bud_bpost_sgei_rem_2027", "bpost", 2027, 104917000, "", "", "budgeted", SRC, "strong", "bpost SGEI path 104917 kEUR 2027-29 after USO reform; tick758"),
    ("bud_bpost_advance_detail_2026", "bpost", 2026, 154916692, "", "", "budgeted", SRC, "strong", "Exact cash class 154916692.02 EUR 2026 of which advance path 124926220 by 31Dec2026; tick758"),
    # NMBS opex stack
    ("bud_nmbs_measures_312107_2026", "nmbs", 2026, 42500000, "", "", "budgeted", SRC, "strong", "BA 312107 free/staff measures for NMBS 42500 kEUR 2026; tick758"),
    ("bud_nmbs_fixed_opex_312202_2024", "nmbs", 2024, 645545000, "", "", "outturn", SRC, "strong", "BA 312202 fixed exploitation compensation 645545 kEUR 2024; tick758"),
    ("bud_nmbs_fixed_opex_312202_2025", "nmbs", 2025, 715195000, "", "", "budgeted", SRC, "strong", "NMBS fixed opex 715195 kEUR 2025; tick758"),
    ("bud_nmbs_fixed_opex_312202_2026", "nmbs", 2026, 706713000, "", "", "budgeted", SRC, "strong", "NMBS fixed opex 706713 kEUR 2026 (path down to 599389 2029); tick758"),
    ("bud_nmbs_fixed_opex_312202_2029", "nmbs", 2029, 599389000, "", "", "budgeted", SRC, "strong", "NMBS fixed opex path 599389 kEUR 2029; tick758"),
    ("bud_nmbs_var_opex_312218_2024", "nmbs", 2024, 440063000, "", "", "outturn", SRC, "strong", "BA 312218 variable opex 440063 kEUR 2024; tick758"),
    ("bud_nmbs_var_opex_312218_2025", "nmbs", 2025, 550032000, "", "", "budgeted", SRC, "strong", "NMBS variable opex 550032 kEUR 2025; tick758"),
    ("bud_nmbs_var_opex_312218_2026", "nmbs", 2026, 556750000, "", "", "budgeted", SRC, "strong", "NMBS variable opex 556750 kEUR 2026; tick758"),
    ("bud_nmbs_var_opex_312218_2029", "nmbs", 2029, 646856000, "", "", "budgeted", SRC, "strong", "NMBS variable opex path 646856 kEUR 2029; tick758"),
    ("bud_nmbs_opex_stack_2026", "nmbs", 2026, 1305963000, "", "", "derived", SRC, "strong", "NMBS opex stack 42.5+706.713+556.75=1305.963m 2026 excl invest/loans; tick758"),
    ("bud_nmbs_safe_stations_opex_2026", "nmbs", 2026, 4400000, "", "", "budgeted", SRC, "strong", "BA 312220 safe/livable stations opex 4400 kEUR 2026; tick758"),
    # NMBS invest
    ("bud_nmbs_invest_capital_511101_2024", "nmbs", 2024, 807087000, "", "", "outturn", SRC, "strong", "BA 511101 State capital for NMBS invest 807087 kEUR 2024; tick758"),
    ("bud_nmbs_invest_capital_511101_2025", "nmbs", 2025, 1009413000, "", "", "budgeted", SRC, "strong", "NMBS invest capital 1009413 kEUR 2025; tick758"),
    ("bud_nmbs_invest_capital_511101_2026", "nmbs", 2026, 904874000, "", "", "budgeted", SRC, "strong", "NMBS invest capital 904874 kEUR 2026 after MR saves -65m provisional +27m Dec path; tick758"),
    ("bud_nmbs_invest_capital_511101_2029", "nmbs", 2029, 645961000, "", "", "budgeted", SRC, "strong", "NMBS invest capital path 645961 kEUR 2029; tick758"),
    ("bud_nmbs_gen_capacity_511104_2026", "nmbs", 2026, 7667000, "", "", "budgeted", SRC, "strong", "BA 511104 GEN/priority capacity NMBS 7667 kEUR 2026 of MIA 1bn envelope 2018-31; tick758"),
    # Infrabel opex
    ("bud_infrabel_opex_414051_2024", "infrabel", 2024, 516954000, "", "", "outturn", SRC, "strong", "BA 414051 Infrabel maintenance/manage 516954 kEUR 2024; tick758"),
    ("bud_infrabel_opex_414051_2025", "infrabel", 2025, 582875000, "", "", "budgeted", SRC, "strong", "Infrabel opex 582875 kEUR 2025; tick758"),
    ("bud_infrabel_opex_414051_2026", "infrabel", 2026, 564527000, "", "", "budgeted", SRC, "strong", "Infrabel opex 564527 kEUR 2026 (path to 487715 2029); tick758"),
    ("bud_infrabel_diabolo_414053_2026", "infrabel", 2026, 13231000, "", "", "budgeted", SRC, "strong", "BA 414053 Diabolo 13231 kEUR 2026 flat path; tick758"),
    ("bud_infrabel_liefkenshoek_414054_2026", "infrabel", 2026, 51880000, "", "", "budgeted", SRC, "strong", "BA 414054 PPP Liefkenshoek 51880 kEUR 2026; tick758"),
    ("bud_infrabel_opex_stack_2026", "infrabel", 2026, 629638000, "", "", "derived", SRC, "strong", "Infrabel opex stack 564.527+13.231+51.880=629.638m 2026; tick758"),
    # Infrabel invest
    ("bud_infrabel_invest_614151_2024", "infrabel", 2024, 1178744000, "", "", "outturn", SRC, "strong", "BA 614151 Infrabel invest 1178744 kEUR 2024; tick758"),
    ("bud_infrabel_invest_614151_2025", "infrabel", 2025, 1227048000, "", "", "budgeted", SRC, "strong", "Infrabel invest 1227048 kEUR 2025; tick758"),
    ("bud_infrabel_invest_614151_2026", "infrabel", 2026, 1268646000, "", "", "budgeted", SRC, "strong", "Infrabel invest 1268646 kEUR 2026 (contract base 1203855k EUR2023 + index/RRP); tick758"),
    ("bud_infrabel_invest_614151_2029", "infrabel", 2029, 1279049000, "", "", "budgeted", SRC, "strong", "Infrabel invest path 1279049 kEUR 2029; tick758"),
    ("bud_infrabel_capacity_614153_2026", "infrabel", 2026, 33906000, "", "", "budgeted", SRC, "strong", "BA 614153 Infrabel extra capacity MIA 33906 kEUR 2026; tick758"),
    ("bud_infrabel_prefin_614256_2026", "infrabel", 2026, 7970000, "", "", "budgeted", SRC, "strong", "BA 614256 Infrabel loan prefin repay flat 7970 kEUR/yr 2021-2049; tick758"),
    # Loans
    ("bud_nmbs_loan_interest_2026", "nmbs", 2026, 12864000, "", "", "budgeted", SRC, "strong", "BA 211001 NMBS loan interest 12864 kEUR 2026; tick758"),
    ("bud_nmbs_loan_capital_2026", "nmbs", 2026, 29063000, "", "", "budgeted", SRC, "strong", "BA 911001 NMBS loan capital 29063 kEUR 2026; tick758"),
    ("bud_infrabel_loan_interest_2026", "infrabel", 2026, 4753000, "", "", "budgeted", SRC, "strong", "BA 211051 Infrabel loan interest 4753 kEUR 2026; tick758"),
    ("bud_infrabel_loan_capital_2026", "infrabel", 2026, 7926000, "", "", "budgeted", SRC, "strong", "BA 911051 Infrabel loan capital 7926 kEUR 2026; tick758"),
    # HR Rail
    ("bud_hr_rail_contrib_2026", "hr_rail", 2026, 1635000, "", "", "budgeted", SRC, "strong", "BA 312201 HR Rail ops contrib 1635 kEUR 2026 (base 1.2m + index); tick758"),
    # Modal shift + skeyes
    ("bud_modal_shift_rail_2026", "fod_mobility", 2026, 11246000, "", "", "budgeted", SRC, "strong", "BA 312203 modal shift rail support 11246 kEUR 2026 (was 24846 2024); tick758"),
    ("bud_skeyes_public_service_2024", "skeyes", 2024, 30102000, "", "", "outturn", SRC, "strong", "BA 312101 skeyes public service eng 30102 kEUR 2024; tick758"),
    ("bud_skeyes_public_service_2025", "skeyes", 2025, 34157000, "", "", "budgeted", SRC, "strong", "skeyes 34157 kEUR eng 2025; tick758"),
    ("bud_skeyes_public_service_2026", "skeyes", 2026, 35705000, "", "", "budgeted", SRC, "strong", "skeyes eng 35705 / liq 35559 kEUR 2026 4th management contract; tick758"),
    # Combined stacks
    ("bud_rail_nmbs_class_2026", "nmbs", 2026, 2264841000, "", "", "derived", SRC, "strong", "NMBS class opex1.306+invest0.905+capacity0.008+loans0.042+safe0.004=2.265bn 2026; tick758"),
    ("bud_rail_infrabel_class_2026", "infrabel", 2026, 1952838000, "", "", "derived", SRC, "strong", "Infrabel class opex0.630+invest1.269+capacity0.034+prefin0.008+loans0.013=1.953bn 2026; tick758"),
    ("bud_rail_federal_stack_2026", "fod_mobility", 2026, 4219314000, "", "", "derived", SRC, "strong", "Federal rail stack NMBS+Infrabel+HR Rail class ~4.221bn 2026; tick758"),
    ("bud_dual_rail_bpost_skeyes_2026", "gg_belgium", 2026, 4409936000, "", "", "derived", SRC_DUAL, "strong", "Dual rail 4.221 + bpost 0.155 + skeyes 0.036 = 4.410bn class not full TE; dual De Lijn/OTW separate; tick758"),
    # Beliris residual sample
    ("bud_beliris_personnel_2026", "beliris", 2026, 11769000, "", "", "budgeted", SRC, "strong", "Beliris personnel statutair+contract 11281+488=11769 kEUR 2026; tick758"),
    ("bud_beliris_coop_bru_liq_2026", "beliris", 2026, 6768000, "", "", "budgeted", SRC, "strong", "BA 512105 Beliris-BRU coop liq 6768 kEUR 2026 (eng 0); tick758"),
    ("bud_beliris_slrb_liq_2026", "beliris", 2026, 4518000, "", "", "budgeted", SRC, "strong", "BA 512220 SLRB/BGHM toelage liq 4518 kEUR 2026; tick758"),
]

cmt_rows = [
    (
        "cmt_nmbs_opex_path_2024_29",
        "NMBS fixed+variable opex + measures path 2024-2029",
        "nmbs",
        "NMBS public service passengers",
        "ODC 2023-2032 + Kamer DOC 56 1281/016",
        "2023-01-01",
        2024,
        2029,
        0,
        '{"fixed_2026":706713000,"var_2026":556750000,"measures_2026":42500000,"stack_2026":1305963000,"fixed_2025":715195000,"var_2025":550032000,"fixed_2029":599389000,"var_2029":646856000}',
        0,
        "active",
        URL,
        "Fund NMBS PSO exploitation under ODC 2023-32",
        "Publish unit cost per pkm FOI; dual De Lijn/OTW",
        SRC,
        "strong",
        "Federal>Mobiliteit>NMBS>opex",
        "tick758",
    ),
    (
        "cmt_nmbs_invest_capital_2024_29",
        "NMBS State capital investment path 0.81-1.01bn/yr",
        "nmbs",
        "Rolling stock and stations invest",
        "ODC art117 + Kamer 1281/016 BA 511101",
        "2026-01-28",
        2024,
        2029,
        0,
        '{"2024":807087000,"2025":1009413000,"2026":904874000,"2027":661280000,"2028":633508000,"2029":645961000,"mr_save_2026_provisional":-65000000,"mr_dec_2026":27000000}',
        0,
        "active",
        URL,
        "Finance NMBS multi-year investment plan",
        "CAPEX project L5 FOI; savings split residual",
        SRC,
        "strong",
        "Federal>Mobiliteit>NMBS>invest",
        "tick758",
    ),
    (
        "cmt_infrabel_opex_invest_2026",
        "Infrabel opex stack 0.630bn + invest 1.269bn 2026",
        "infrabel",
        "Rail infrastructure network",
        "Performance contract 2023-2032 + Kamer 1281/016",
        "2026-01-28",
        2024,
        2029,
        0,
        '{"opex_414051_2026":564527000,"diabolo":13231000,"liefkenshoek":51880000,"opex_stack":629638000,"invest_2026":1268646000,"capacity_mia":33906000,"prefin":7970000,"contract_base_eur2023_2026":1203855000}',
        0,
        "active",
        URL,
        "Maintain and renew national rail infrastructure",
        "Network unit cost FOI dual NMBS",
        SRC,
        "strong",
        "Federal>Mobiliteit>Infrabel",
        "tick758",
    ),
    (
        "cmt_rail_federal_stack_2026",
        "Federal rail NMBS+Infrabel+HR class ~4.22bn 2026",
        "fod_mobility",
        "NMBS Infrabel HR Rail",
        "Kamer DOC 56 1281/016 prog 51",
        "2026-01-28",
        2026,
        2026,
        4219314000,
        '{"nmbs_class":2264841000,"infrabel_class":1952838000,"hr_rail":1635000,"total":4219314000,"note":"budget article sum not full ESA D.31"}',
        0,
        "active",
        URL,
        "Transparent federal rail financing stack",
        "Reconcile FPS cash codes FOI dual gap_nmbs",
        SRC,
        "strong",
        "Federal>Mobiliteit>rail_stack",
        "tick758 major residual fill",
    ),
    (
        "cmt_bpost_sgei_2026_path",
        "bpost SGEI remuneration 154.9m 2026 then 104.9m 2027+",
        "bpost",
        "bpost USO / network SGEI",
        "Management contract State-bpost + Kamer 1281/016 BA 312207",
        "2026-01-28",
        2024,
        2029,
        0,
        '{"2024":153233000,"2025":153300000,"2026":154917000,"2027":104917000,"2028":104917000,"2029":104917000,"exact_2026":154916692}',
        0,
        "active",
        URL,
        "Compensate bpost public service obligations",
        "L5 USO vs network split FOI dual gap_bpost",
        SRC,
        "strong",
        "Federal>Mobiliteit>bpost_SGEI",
        "tick758 dual prior AR SGEI",
    ),
    (
        "cmt_skeyes_public_service_2026",
        "skeyes public-service financing 35.7m eng 2026",
        "skeyes",
        "Air navigation service users / State",
        "4th management contract State-skeyes + BA 312101",
        "2026-01-28",
        2024,
        2029,
        0,
        '{"eng_2024":30102000,"eng_2025":34157000,"eng_2026":35705000,"liq_2026":35559000,"eng_2027":37837000}',
        0,
        "active",
        URL,
        "Fund ATM public service obligations skeyes",
        "Cost recovery vs user fees FOI",
        SRC,
        "strong",
        "Federal>Mobiliteit>skeyes",
        "tick758",
    ),
    (
        "cmt_mia_gen_1bn_2018_31",
        "MIA/GEN strategic rail capacity envelope ~1bn 2018-2031",
        "gg_belgium",
        "NMBS Infrabel GEN projects",
        "Coop agreement 5 Oct 2018 + CM 13 Jul 2018 + Kamer 1281/016",
        "2018-10-05",
        2016,
        2031,
        996886000,
        '{"mia_total_use_keur":996886,"mia_infrabel":859546,"mia_nmbs":137340,"gen_fonds_total_keur":228444,"reserve_unallocated":3114000,"2026_mia_total_keur":41573}',
        0,
        "active",
        URL,
        "Strategic rail capacity GEN and priority infrastructure",
        "Project L5 residual FOI",
        SRC,
        "strong",
        "Federal>Mobiliteit>MIA_GEN",
        "tick758",
    ),
    (
        "cmt_dual_rail_regional_pes_tick758",
        "Dual federal rail ~4.22bn vs De Lijn/OTW regional stacks",
        "gg_belgium",
        "BE public transport dual map",
        "Kamer 1281/016 + prior De Lijn/OTW fills",
        "2026-01-28",
        2026,
        2026,
        0,
        '{"fed_rail_class_m":4221,"bpost_m":155,"skeyes_m":36,"de_lijn_omzet_class_m":1420,"otw_financing_class_m":960,"note":"not TE-additive different perimeters"}',
        0,
        "active",
        URL,
        "Comparable PT financing transparency",
        "Unified PT TCO dashboard FOI",
        SRC_DUAL,
        "strong",
        "Belgium>dual>public_transport",
        "tick758",
    ),
    (
        "cmt_rail_loan_service_2026",
        "NMBS+Infrabel loan service interest+capital 54.6m 2026",
        "fod_mobility",
        "Historic GEN/Desiro and Infrabel loans",
        "Kamer 1281/016 prog 12",
        "2026-01-28",
        2024,
        2029,
        0,
        '{"nmbs_int":12864000,"nmbs_cap":29063000,"infrabel_int":4753000,"infrabel_cap":7926000,"total":54606000}',
        0,
        "active",
        URL,
        "Service historic rail prefinancing loans",
        "Full amortisation schedule FOI",
        SRC,
        "strong",
        "Federal>Mobiliteit>rail_loans",
        "tick758",
    ),
    (
        "cmt_beliris_personnel_projects_2026",
        "Beliris personnel 11.8m + project toelagen residual 2026",
        "beliris",
        "Brussels federal capital function projects",
        "Kamer 1281/016 OA55",
        "2026-01-28",
        2026,
        2026,
        0,
        '{"personnel":11769000,"coop_liq":6768000,"slrb_liq":4518000,"new_projects_count":15}',
        0,
        "active",
        URL,
        "Federal-Brussels capital function cooperation",
        "Full project L5 matrix FOI dual Metro3",
        SRC,
        "strong",
        "Federal>Mobiliteit>Beliris",
        "tick758 residual sample",
    ),
]

lb_rows = [
    (
        "lb_rail_federal_stack_4_22bn_2026",
        "Federal rail NMBS+Infrabel+HR stack ~4.22bn 2026",
        "L5",
        "programme",
        "Federal>Mobiliteit>rail_stack",
        4219314000,
        4219314000,
        "Strong Kamer BA sum; not full ESA; dual regional PT",
        "strong",
        SRC,
        "Rail passengers / freight",
        "Fund national rail PSO and infrastructure",
        "Largest federal mobility residual now public",
        5.0,
        9.0,
        5,
        6.6,
        "Unit cost + CAPEX L5 FOI dual regional",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_nmbs_opex_1_31bn_2026",
        "NMBS opex stack fixed+var+measures 1.306bn 2026",
        "L5",
        "programme",
        "Federal>Mobiliteit>NMBS>opex",
        1305963000,
        1305963000,
        "Strong ODC path; dual De Lijn 1.2bn VL tussenkomst class",
        "strong",
        SRC,
        "NMBS passengers",
        "PSO exploitation compensation",
        "Unit subsidy residual FOI",
        5.0,
        8.5,
        5,
        6.4,
        "pkm unit cost FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_infrabel_invest_1_27bn_2026",
        "Infrabel investment toelage 1.269bn 2026",
        "L5",
        "invest",
        "Federal>Mobiliteit>Infrabel>invest",
        1268646000,
        1268646000,
        "Strong performance contract path; dual NMBS invest 0.90bn",
        "strong",
        SRC,
        "Network users / contractors",
        "Renew and expand rail network",
        "Project L5 residual",
        4.5,
        8.5,
        5,
        6.2,
        "Project portfolio FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_nmbs_invest_0_90bn_2026",
        "NMBS State capital investment 904.9m 2026",
        "L5",
        "invest",
        "Federal>Mobiliteit>NMBS>invest",
        904874000,
        904874000,
        "Strong; MR save path -65/+27m partial; dual Infrabel",
        "strong",
        SRC,
        "NMBS fleet and stations",
        "Multi-year investment plan",
        "ETCS rolling stock residual FOI",
        4.5,
        8.0,
        5,
        6.0,
        "ETCS and fleet L5 FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_infrabel_opex_0_63bn_2026",
        "Infrabel opex stack 629.6m (ops+Diabolo+Liefkenshoek) 2026",
        "L5",
        "programme",
        "Federal>Mobiliteit>Infrabel>opex",
        629638000,
        629638000,
        "Strong; PPP Liefkenshoek 51.9m lock-in dual DBFM",
        "strong",
        SRC,
        "Infrastructure maintenance",
        "Network maintenance and special PPP charges",
        "PPP residual FOI",
        5.0,
        7.5,
        4,
        6.1,
        "PPP cash path FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_bpost_sgei_154_9m_2026",
        "bpost SGEI rem 154.9m 2026 then step-down 104.9m",
        "L5",
        "programme",
        "Federal>Mobiliteit>bpost_SGEI",
        154917000,
        154917000,
        "Strong Kamer; dual prior AR 227.8/311.9m different perimeter",
        "strong",
        SRC,
        "Postal users / network",
        "SGEI compensation post-press reform",
        "Component L5 still FOI",
        5.5,
        7.0,
        5,
        6.0,
        "USO component split FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_skeyes_35_7m_2026",
        "skeyes public-service financing 35.7m 2026",
        "L5",
        "programme",
        "Federal>Mobiliteit>skeyes",
        35705000,
        35705000,
        "Strong 4th management contract path",
        "strong",
        SRC,
        "Aviation / ATM",
        "Air navigation public service",
        "User fee dual residual",
        4.0,
        6.0,
        4,
        5.2,
        "Cost recovery FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_dual_pt_fed_regional_tick758",
        "Dual federal rail 4.22bn + bpost/skeyes vs regional PT",
        "L5",
        "dual",
        "Belgium>dual>public_transport_stack",
        4409936000,
        0,
        "Strong dual not TE-additive; De Lijn/OTW separate books",
        "strong",
        SRC_DUAL,
        "BE public transport users",
        "Comparable PT financing transparency",
        "Fragmented books hide full TCO",
        6.0,
        9.0,
        5,
        7.0,
        "Unified PT TCO FOI",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_mia_gen_1bn_envelope",
        "MIA/GEN strategic rail envelope ~997m use 2016-31",
        "L5",
        "commitment",
        "Federal>Mobiliteit>MIA_GEN",
        996886000,
        996886000,
        "Strong table sum kEUR courants; 2026 slice 41.6m",
        "strong",
        SRC,
        "GEN corridors / regions",
        "Strategic rail capacity financing",
        "Project L5 residual",
        4.5,
        8.0,
        5,
        6.0,
        "Project delivery FOI dual Metro3",
        "active",
        "",
        "tick758",
    ),
    (
        "lb_infrabel_liefkenshoek_51_9m",
        "Infrabel Liefkenshoek PPP charge 51.9m/yr 2026",
        "L5",
        "programme",
        "Federal>Mobiliteit>Infrabel>Liefkenshoek_PPP",
        51880000,
        51880000,
        "Strong multi-year flat; dual prison DBFM fee pattern",
        "strong",
        SRC,
        "PPP partners",
        "Pay availability for rail PPP tunnel",
        "Full PPP TCO residual FOI",
        5.5,
        6.5,
        4,
        5.9,
        "PPP contract FOI dual DBFM",
        "active",
        "",
        "tick758",
    ),
]

src_rows = [
    (
        SRC,
        "Kamer DOC 56 1281/016 FOD Mobiliteit en Vervoer budget justification 2026",
        URL,
        "Kamer / Chambre",
        "2026-08-02",
        "parliamentary",
        "Strong tick758: NMBS opex stack 1.306bn invest 0.905; Infrabel opex 0.630 invest 1.269; rail stack ~4.22bn; bpost SGEI 154.9; skeyes 35.7; MIA/GEN table; HR Rail 1.635; raw 56K1281016.pdf 440p kEUR",
    ),
    (
        SRC_DUAL,
        "Dual federal rail/bpost/skeyes vs regional PT De Lijn OTW tick758",
        URL,
        "DOGE synthesis Kamer mobility + prior regional PT",
        "2026-08-02",
        "synthesis",
        "Strong dual tick758 not TE-additive: fed rail 4.22bn + bpost 0.155 + skeyes 0.036 vs De Lijn/OTW separate",
    ),
]

foi_row = (
    "gap_mobility_rail_contract_l5",
    "Federal>Mobiliteit>rail_NMBS_Infrabel>L5",
    "fod_mobility",
    "NMBS/Infrabel CAPEX project L5 under invest 0.90/1.27bn; ETCS rolling stock BA 511102 cash path; MR savings -65m/+27m allocation CAPEX vs OPEX; full Beliris project matrix; skeyes cost-recovery vs user fees; reconcile FPS cash codes to ODC path",
    "Major rail aggregates now public from Kamer 1281/016; project and savings-split L5 residual dual prior gap_nmbs",
    8,
    "FOD Mobiliteit en Vervoer / NMBS / Infrabel / FOD BOSA",
    "",
    "https://www.ibz.be/nl/openbaarheid-van-bestuur",
    "docs/doge/foi/drafts/gap_mobility_rail_contract_l5.md",
    "ready",
    "2026-08-02",
    "",
    "",
    "",
    "",
    "cmt_rail_federal_stack_2026|cmt_nmbs_invest_capital_2024_29|cmt_infrabel_opex_invest_2026",
    "lb_rail_federal_stack_4_22bn_2026|lb_nmbs_opex_1_31bn_2026|lb_infrabel_invest_1_27bn_2026",
    "2026-08-02T18:00:00Z",
    "2026-08-02T18:00:00Z",
    "tick758 Kamer 1281/016 primary; human send only; also updates gap_nmbs_annual_toelage notes partial fill",
)


def ensure_entities():
    ent_path = base / "entities.csv"
    text = ent_path.read_text(encoding="utf-8")
    rows = []
    if "hr_rail," not in text and "\nhr_rail," not in text:
        rows.append(
            (
                "hr_rail",
                "HR Rail",
                "HR Rail",
                "HR Rail public-law personnel vehicle rail",
                "parastatal",
                "fod_mobility",
                "bi",
                "",
                "",
                "",
                "NV publiek recht rail HR; fed contrib 1.635m 2026; tick758",
            )
        )
    if "skeyes," not in text and "\nskeyes," not in text:
        rows.append(
            (
                "skeyes",
                "skeyes (ex Belgocontrol)",
                "skeyes",
                "Belgian air navigation service provider",
                "parastatal",
                "fod_mobility",
                "bi",
                "https://www.skeyes.be",
                "",
                "",
                "ATM ANSP; fed public service 35.7m 2026; tick758",
            )
        )
    if "beliris," not in text and "\nbeliris," not in text:
        rows.append(
            (
                "beliris",
                "Beliris",
                "Beliris",
                "Federal-Brussels capital function cooperation office",
                "agency",
                "fod_mobility",
                "bi",
                "https://www.beliris.be",
                "",
                "",
                "Federal-BRU coop projects; personnel 11.8m 2026; tick758",
            )
        )
    if "fod_mobility," not in text and "\nfod_mobility," not in text:
        rows.append(
            (
                "fod_mobility",
                "FOD Mobiliteit en Vervoer",
                "SPF Mobilite et Transports",
                "FPS Mobility and Transport",
                "ministry",
                "sec_federal",
                "bi",
                "https://mobilit.belgium.be",
                "",
                "",
                "Federal mobility ministry; tick758",
            )
        )
    if rows:
        with ent_path.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            for r in rows:
                w.writerow(r)
    return len(rows)


def main():
    n_ent = ensure_entities()
    with (base / "budgets.csv").open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        for r in bud_rows:
            w.writerow(r)
    with (base / "commitments.csv").open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        for r in cmt_rows:
            w.writerow(r)
    with (base / "leaderboard.csv").open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        for r in lb_rows:
            w.writerow(r)
    with (base / "sources.csv").open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        for r in src_rows:
            w.writerow(r)
    with (base / "foi_queue.csv").open("a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(foi_row)

    rq = base / "research_queue.csv"
    lines = rq.read_text(encoding="utf-8").splitlines()
    out = []
    for ln in lines:
        if ln.startswith("rq_749,"):
            out.append(
                "rq_749,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                "Next residual: new CoA/primary PDF not yet mined (prefer Mobility 1281/016 or Economy 1281/015 or BELSPO 018 residual) or Entity II dual; Defence 1281/008 filled tick757,,"
                "2026-08-02T17:00:00Z,2026-08-02T18:00:00Z,"
                "tick758 Mobility 1281/016: rail stack 4.22bn NMBS opex 1.306 invest 0.905 Infrabel 0.630/1.269 bpost 154.9 skeyes 35.7; FOI ready"
            )
        else:
            out.append(ln)
    out.append(
        "rq_750,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Next residual: prefer Economy 1281/015 or BELSPO 018 or Finance 1281/010 residual or Entity II dual; Mobility rail stack filled tick758; progress@760 after next tick+2,,"
        "2026-08-02T18:00:00Z,,"
        "spawned tick758 after rq_749"
    )
    rq.write_text("\n".join(out) + "\n", encoding="utf-8")

    (base / "loop_state.csv").write_text(
        "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
        "main,continuous,hole_fill,2026-08-02T18:00:00Z,rq_749,758,no,"
        "tick758 Mobility rail 4.22bn NMBS 1.31/0.90 Infrabel 0.63/1.27 bpost 154.9; next rq_750; progress@760 in 2; rq_116 deferred\n",
        encoding="utf-8",
    )
    print(f"OK tick758 entities+{n_ent} budgets+{len(bud_rows)} cmt+{len(cmt_rows)} lb+{len(lb_rows)} src+{len(src_rows)} foi+1")


if __name__ == "__main__":
    main()
