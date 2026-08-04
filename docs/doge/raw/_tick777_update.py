from pathlib import Path

base = Path(r"docs/doge/data")
utc = "2026-08-03T13:00:00Z"
src = "src_kamer_oap_1281_022_2026"
src_hr = "src_fpb_hermreg_pdf_jul2026_tick777"
src_dual = "src_dual_entity2_oap_tick777"

# entities notes updates via append only new
ents = base / "entities.csv"
et = ents.read_text(encoding="utf-8")
# no new entities needed if exist - debt_agency_be, favv, fpb_planbureau exist

# sources
src_path = base / "sources.csv"
src_rows = [
f"{src},Kamer DOC 56 1281/022 OAP ministerial residual (FPB FAVV Debt Agency non-Regie),https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Kamer / Chambre,2026-08-03,parliamentary,Strong tick777: 306p OAP; FPB pers 12.454m ops ~1.89m dot 14.445m (+1.4m CM 12/12/2025); FAVV baremes 70.568 other 16.054 social 44.987 ops 81.132 BMO vet 45.192 ICT 9.553 labs 7.933 retributions 65.582 heffingen 42.425 dot 114.506 RFF digi 1.274; Debt Agency pers 3.832 ops 3.638 dot 7.873 Euronext listing class; Regie already ticks740-743; raw 56K1281022_oap.pdf",
f"{src_hr},FPB HermReg Perspectives economiques regionales 2026-2031 PDF Jul 2026 ch5 finances,https://www.plan.be/sites/default/files/documents/FOR_HermReg_2631_13335_FR.pdf,Bureau federal du Plan / IBSA / IWEPS / Statistiek Vlaanderen,2026-08-03,official_outlook,Strong tick777: T14-17 solde 2026 VL -3.0 WAL -2.1 FWB -1.8 BCR+COCOM -1.0 bn; C&R ensemble -1.2pct GDP; interest path VL 1.3->2.2 WAL 1.0->1.5 FWB 0.4->0.8 BCR 0.5->0.8; dual xlsx tick405; raw fpb_hermreg_2631_fr.pdf",
f"{src_dual},Dual Entity II HermReg soldes + OAP FAVV/FPB residual tick777,https://www.plan.be/sites/default/files/documents/FOR_HermReg_2631_13335_FR.pdf,DOGE synthesis,2026-08-03,synthesis,Strong dual not TE-additive: Entity II 2026 deficit stack VL3.0+WAL2.1+FWB1.8+BCR1.0=7.9bn; FAVV fee-funded dual Sciensano/Sante; FPB +1.4m CM transfer",
]
st = src_path.read_text(encoding="utf-8")
for row in src_rows:
    sid = row.split(",")[0]
    if f"\n{sid}," not in st:
        with src_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("source +", sid)

# budgets
bud = base / "budgets.csv"
bud_rows = [
# FPB OAP 022
f"bud_fpb_pers_baremes_2026,fpb_planbureau,2026,12453954,,,budgeted,{src},strong,11.11 baremes stack 12.454m 2026 (base 11.014 +1.4m CM 12/12/2025 +index -savings); tick777",
f"bud_fpb_ops_2026,fpb_planbureau,2026,1889389,,,budgeted,{src},strong,12.11 ops ~1.889m 2026; tick777",
f"bud_fpb_dot_oap_2026,fpb_planbureau,2026,14445000,,,budgeted,{src},strong,46.10 OAP dot 14.445m 2026 (Econ+SS+index +1.4m CM); supersedes older path 11.858m class; tick777",
f"bud_fpb_own_sales_2026,fpb_planbureau,2026,500000,,,budgeted,{src},strong,Own sales/conventions 0.5m 2026; tick777",
f"bud_fpb_cm_extra_1_4m_2026,fpb_planbureau,2026,1400000,,,budgeted,{src},strong,CM 12/12/2025 notification +1.4m in FPB 2026 package; tick777",
# FAVV deepen 2026
f"bud_favv_pers_baremes_2026,favv,2026,70568294,,,budgeted,{src},strong,11.11 baremes 70.568m 2026 (index +2.855 Brexit -3.067); tick777",
f"bud_favv_pers_other_2026,favv,2026,16053788,,,budgeted,{src},strong,Other remun elements 16.054m 2026; tick777",
f"bud_favv_social_contrib_2026,favv,2026,44986833,,,budgeted,{src},strong,Employer social contrib 44.987m 2026; tick777",
f"bud_favv_wages_nature_2026,favv,2026,1469905,,,budgeted,{src},strong,Wages in kind 1.470m 2026; tick777",
f"bud_favv_pers_stack_2026,favv,2026,133078820,,,budgeted,{src},strong,Pers stack baremes+other+social+nature ~133.079m 2026; tick777",
f"bud_favv_ops_total_2026,favv,2026,81131988,,,budgeted,{src},strong,12.11 ops total 81.132m 2026; tick777",
f"bud_favv_ops_bmo_vet_2026,favv,2026,45191900,,,budgeted,{src},strong,BMO veterinarian third-party 45.192m 2026 (Pax Veterinaria +2.651); tick777",
f"bud_favv_ops_ict_2026,favv,2026,9552910,,,budgeted,{src},strong,ICT 9.553m 2026 (+Smals consultancy reclass 2.601); tick777",
f"bud_favv_ops_labs_ext_2026,favv,2026,7933316,,,budgeted,{src},strong,External labs 7.933m 2026; tick777",
f"bud_favv_ops_labs_int_2026,favv,2026,2974654,,,budgeted,{src},strong,Internal labs 2.975m 2026; tick777",
f"bud_favv_ops_third_other_2026,favv,2026,3574160,,,budgeted,{src},strong,Other third-party 3.574m 2026; tick777",
f"bud_favv_ops_building_2026,favv,2026,3832286,,,budgeted,{src},strong,Building/ops 3.832m 2026; tick777",
f"bud_favv_invest_2026,favv,2026,2528418,,,budgeted,{src},strong,74.22 invest 2.528m 2026; tick777",
f"bud_favv_retributions_2026,favv,2026,65581917,,,budgeted,{src},strong,16.11 retributions 65.582m 2026 (Brexit -6.077 Pax +2.651); tick777",
f"bud_favv_heffingen_2026,favv,2026,42425170,,,budgeted,{src},strong,36.90 heffingen 42.425m 2026; tick777",
f"bud_favv_dot_oap_confirm_2026,favv,2026,114506196,,,budgeted,{src},strong,46.10 OAP dot 114.506m confirms 014 path 114.507kEUR; tick777",
f"bud_favv_rff_digi_2026,favv,2026,1274365,,,budgeted,{src},strong,RRF digi FAVV excl VAT 1.274m 2026 (was 3.2 path); tick777",
f"bud_favv_spend_class_2026,favv,2026,216739226,,,budgeted,{src},strong,Pers 133.079 + ops 81.132 + invest 2.528 = 216.739m spend class 2026; tick777",
# Debt Agency
f"bud_afd_pers_2026,debt_agency_be,2026,3832385,,,budgeted,{src},strong,11.11 pers total 3.832m 2026; tick777",
f"bud_afd_ops_2026,debt_agency_be,2026,3638407,,,budgeted,{src},strong,12.11 ops 3.638m 2026 (Bloomberg LSEG Euronext class); tick777",
f"bud_afd_dot_2026,debt_agency_be,2026,7873000,,,budgeted,{src},strong,46.10 federal dot 7.873m 2026 (path 7.936/8.207/7.873); tick777",
f"bud_afd_euronext_listing_2026,debt_agency_be,2026,687000,,,budgeted,{src},strong,Euronext listing fees class 0.687m within ops 2026; tick777",
f"bud_afd_bloomberg_2026,debt_agency_be,2026,476806,,,budgeted,{src},strong,Bloomberg terminals 0.477m 2026; tick777",
# HermReg Entity II dual confirm (PDF bn -> m, match xlsx where present)
f"bud_hermreg_pdf_vl_solde_2026,vlaanderen_gov,2026,-3000000000,,,esa_outlook,{src_hr},strong,HermReg T14 PDF solde -3.0bn 2026 (xlsx -3049m); tick777",
f"bud_hermreg_pdf_vl_solde_2027,vlaanderen_gov,2027,-900000000,,,esa_outlook,{src_hr},strong,HermReg T14 solde -0.9bn 2027 near balance excl Oosterweel narrative; tick777",
f"bud_hermreg_pdf_vl_solde_2029,vlaanderen_gov,2029,-2000000000,,,esa_outlook,{src_hr},strong,HermReg T14 solde -2.0bn 2029; tick777",
f"bud_hermreg_pdf_vl_interest_2026,vlaanderen_gov,2026,1300000000,,,esa_outlook,{src_hr},strong,T14 interest 1.3bn 2026 path to 2.2bn 2031; tick777",
f"bud_hermreg_pdf_wal_solde_2026,wallonie_gov,2026,-2100000000,,,esa_outlook,{src_hr},strong,T16 solde -2.1bn 2026; tick777",
f"bud_hermreg_pdf_wal_solde_2027,wallonie_gov,2027,-1500000000,,,esa_outlook,{src_hr},strong,T16 solde -1.5bn 2027; tick777",
f"bud_hermreg_pdf_wal_solde_2029,wallonie_gov,2029,-1600000000,,,esa_outlook,{src_hr},strong,T16 solde -1.6bn 2029-31 plateau; tick777",
f"bud_hermreg_pdf_fwb_solde_2026,fwb_gov,2026,-1800000000,,,esa_outlook,{src_hr},strong,T15 solde -1.8bn 2026 (LSF lag + school invest); tick777",
f"bud_hermreg_pdf_fwb_solde_2029,fwb_gov,2029,-1200000000,,,esa_outlook,{src_hr},strong,T15 solde -1.2bn 2029; tick777",
f"bud_hermreg_pdf_bcr_solde_2026,brussels_gov,2026,-1000000000,,,esa_outlook,{src_hr},strong,T17 BCR+COCOM solde -1.0bn 2026; tick777",
f"bud_hermreg_pdf_bcr_solde_2029,brussels_gov,2029,-800000000,,,esa_outlook,{src_hr},strong,T17 solde -0.8bn 2029; tick777",
f"bud_hermreg_pdf_e2_stack_2026,sec_s1312,2026,-7900000000,,,esa_outlook,{src_hr},strong,Entity II deficit stack 2026 VL3+WAL2.1+FWB1.8+BCR1.0=7.9bn (not TE-additive to GG); tick777",
f"bud_hermreg_pdf_cr_solde_pct_2026,sec_s1312,2026,-1.2,,,esa_outlook_pct,{src_hr},strong,T13 C&R ensemble solde -1.2pct GDP 2026 path to -0.5 by 2029-31; amount is pct; tick777",
f"bud_hermreg_pdf_vl_rec_2026,vlaanderen_gov,2026,73200000000,,,esa_outlook,{src_hr},strong,T14 rec 73.2bn 2026; tick777",
f"bud_hermreg_pdf_vl_dep_2026,vlaanderen_gov,2026,76300000000,,,esa_outlook,{src_hr},strong,T14 dep 76.3bn 2026; tick777",
f"bud_hermreg_pdf_wal_rec_2026,wallonie_gov,2026,19100000000,,,esa_outlook,{src_hr},strong,T16 rec 19.1bn 2026; tick777",
f"bud_hermreg_pdf_wal_dep_2026,wallonie_gov,2026,21300000000,,,esa_outlook,{src_hr},strong,T16 dep 21.3bn 2026; tick777",
f"bud_hermreg_pdf_fwb_rec_2026,fwb_gov,2026,26300000000,,,esa_outlook,{src_hr},strong,T15 rec 26.3bn 2026; tick777",
f"bud_hermreg_pdf_fwb_dep_2026,fwb_gov,2026,28100000000,,,esa_outlook,{src_hr},strong,T15 dep 28.1bn 2026; tick777",
f"bud_hermreg_pdf_bcr_rec_2026,brussels_gov,2026,8300000000,,,esa_outlook,{src_hr},strong,T17 rec 8.3bn 2026; tick777",
f"bud_hermreg_pdf_bcr_dep_2026,brussels_gov,2026,9300000000,,,esa_outlook,{src_hr},strong,T17 dep 9.3bn 2026; tick777",
]
bt = bud.read_text(encoding="utf-8")
added_b = 0
with bud.open("a", encoding="utf-8", newline="\n") as f:
    for row in bud_rows:
        bid = row.split(",")[0]
        if f"\n{bid}," not in bt:
            f.write(row + "\n")
            added_b += 1
        else:
            print("bud exists", bid)
print("budgets added", added_b)

# commitments
cmt = base / "commitments.csv"
cmt_rows = [
f'cmt_fpb_dot_oap_2026,FPB OAP dot 14.445m 2026 (+1.4m CM),fpb_planbureau,FPB,Kamer 1281/022 EN_62003,2025-12-12,2026,2026,14445000,"{{""pers"": 12453954, ""ops"": 1889389, ""cm_extra"": 1400000}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Federal Planning Bureau operations,Transparency FOI,{src},strong,Federal>FPB,tick777',
f'cmt_favv_spend_class_2026,FAVV spend class 216.7m 2026,favv,food chain operators,Kamer 1281/022 EN_62004,2026-01-28,2026,2026,216739226,"{{""pers"": 133078820, ""ops"": 81131988, ""invest"": 2528418, ""dot"": 114506196, ""retributions"": 65581917, ""heffingen"": 42425170, ""bmo_vet"": 45191900}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Food chain safety agency fee+dot model,Smals dual FOI,{src},strong,Federal>FAVV,tick777',
f'cmt_afd_dot_2026,Debt Agency OAP ops package 2026,debt_agency_be,Belgian Debt Agency,Kamer 1281/022 EN_62050,2026-01-28,2026,2026,7873000,"{{""dot"": 7873000, ""pers"": 3832385, ""ops"": 3638407}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Debt agency administrative envelope not debt service,Dual debt 1281/019,{src},strong,Federal>DebtAgency,tick777',
f'cmt_entity2_hermreg_stack_2026,Entity II HermReg deficit stack 7.9bn 2026,sec_s1312,VL WAL FWB BCR,HermReg Jul 2026 T14-17,2026-07-16,2026,2026,7900000000,"{{""vl_bn"": -3.0, ""wal_bn"": -2.1, ""fwb_bn"": -1.8, ""bcr_bn"": -1.0, ""cr_pct_gdp"": -1.2, ""note"": ""not TE-additive""}}",0,active,https://www.plan.be/sites/default/files/documents/FOR_HermReg_2631_13335_FR.pdf,Map federated entity financing balances,L5 FOI,{src_hr},strong,Belgium>EntityII>hermreg,tick777',
f'cmt_dual_e2_oap_tick777,Dual Entity II HermReg + OAP FAVV/FPB residual tick777,gg_belgium,dual map,HermReg+Kamer 022,2026-08-03,2026,2026,0,"{{""e2_stack_bn"": 7.9, ""favv_spend_m"": 216.7, ""fpb_dot_m"": 14.445, ""afd_dot_m"": 7.873, ""note"": ""not TE-additive""}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Map Entity II and residual OAP agencies,L5 FOI,{src_dual},strong,Belgium>dual>e2_oap,tick777',
]
ct = cmt.read_text(encoding="utf-8")
added_c = 0
with cmt.open("a", encoding="utf-8", newline="\n") as f:
    for row in cmt_rows:
        cid = row.split(",")[0]
        if f"\n{cid}," not in ct:
            f.write(row + "\n")
            added_c += 1
print("commitments added", added_c)

# leaderboard
lb = base / "leaderboard.csv"
lb_rows = [
f"lb_favv_spend_217m_2026,FAVV spend class 216.7m 2026,L5,ops,Federal>FAVV,216739226,216739226,Strong pers 133 + ops 81.1 (BMO vet 45.2 ICT 9.6) invest 2.5; fee+dot dual,strong,{src},operators,see,primary Kamer,4.0,8.0,3.0,5.5,Smals/lab FOI,active,,tick777",
f"lb_favv_bmo_vet_45m_2026,FAVV BMO veterinarian third-party 45.2m 2026,L5,ops,Federal>FAVV>BMO,45191900,45191900,Strong largest ops line Pax Veterinaria +2.65; dual private vets,strong,{src},vets,see,primary Kamer,4.5,7.0,2.5,5.15,Unit cost FOI,active,,tick777",
f"lb_entity2_deficit_stack_7_9bn_2026,Entity II HermReg deficit stack 7.9bn 2026,L5,transfer,Belgium>EntityII,7900000000,7900000000,Strong VL3+WAL2.1+FWB1.8+BCR1.0; C&R -1.2pct GDP; not TE-additive,strong,{src_hr},federated entities,see,primary FPB,5.0,9.5,4.0,6.65,Consolidation FOI,active,,tick777",
f"lb_fpb_dot_14_4m_2026,FPB OAP dot 14.445m 2026,L5,transfer,Federal>FPB,14445000,14445000,Strong +1.4m CM 12/12/2025 vs older path 11.9m,strong,{src},public,see,primary Kamer,3.0,5.0,2.0,3.7,Transparency,active,,tick777",
f"lb_afd_ops_dot_7_9m_2026,Debt Agency admin package ~7.9m 2026,L5,ops,Federal>DebtAgency,7873000,7873000,Strong admin envelope not debt service; Bloomberg/Euronext class,strong,{src},markets,see,primary Kamer,3.0,4.5,2.0,3.5,Dual debt FOI,active,,tick777",
f"lb_favv_ict_smals_9_6m_2026,FAVV ICT 9.55m incl Smals reclass 2026,L5,ops,Federal>FAVV>ICT,9552910,9552910,Strong +2.6m Smals consultancy reclass dual Smals broker,strong,{src},IT,see,primary Kamer,4.0,5.0,2.5,4.25,Smals dual FOI,active,,tick777",
f"lb_hermreg_vl_interest_1_3bn_2026,Flanders HermReg interest 1.3bn 2026 path 2.2bn,L5,ops,Flanders>interest,1300000000,1300000000,Strong snowball dual Entity II interest path,strong,{src_hr},public,see,primary FPB,4.5,8.0,3.5,5.7,Debt FOI,active,,tick777",
f"lb_dual_e2_oap_2026,Dual Entity II + OAP FAVV residual map,L5,transfer,Belgium>dual>e2_oap,7900000000,0,Strong dual not TE-additive HermReg E2 + FAVV 217m,strong,{src_dual},public,see,primary,4.5,9.0,3.0,5.85,L5 FOI,active,,tick777",
]
lt = lb.read_text(encoding="utf-8")
added_l = 0
with lb.open("a", encoding="utf-8", newline="\n") as f:
    for row in lb_rows:
        lid = row.split(",")[0]
        if f"\n{lid}," not in lt:
            f.write(row + "\n")
            added_l += 1
print("leaderboard added", added_l)

# foi
foi = base / "foi_queue.csv"
gap = "gap_oap_favv_fpb_afd_l5"
foi_row = (
    f"{gap},Federal>OAP>FAVV_FPB_AFD_L5,favv,"
    "FAVV unit cost BMO/vet behind 45.2m; Smals FTE behind ICT 9.55m; fee vs dot split recon; "
    "FPB CM +1.4m purpose; Debt Agency listing/terminal contract list; dual HermReg Entity II interest path FTE,"
    "OAP residual public at aggregate; largest fee-funded food agency L5 opaque,8,"
    "FAVV / FPB / Debt Agency / FOD Economie FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-03,,,,,"
    "cmt_favv_spend_class_2026|cmt_fpb_dot_oap_2026|cmt_afd_dot_2026|cmt_entity2_hermreg_stack_2026,"
    "lb_favv_spend_217m_2026|lb_favv_bmo_vet_45m_2026|lb_entity2_deficit_stack_7_9bn_2026|lb_dual_e2_oap_2026,"
    f"{utc},{utc},tick777 Kamer 1281/022 + HermReg primary; human send only"
)
ft = foi.read_text(encoding="utf-8")
if f"\n{gap}," not in ft:
    with foi.open("a", encoding="utf-8", newline="\n") as f:
        f.write(foi_row + "\n")
    print("foi added")

# research queue
rq = base / "research_queue.csv"
rqt = rq.read_text(encoding="utf-8")
old = "rq_768,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: Entity II dual hole-fill or unmined Kamer 011/012/016 or FOI-adjacent L5; SACA 021 non-RGA filled tick776,,2026-08-03T12:00:00Z,,spawned tick776 after rq_767"
new = "rq_768,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Next residual: Entity II dual hole-fill or unmined Kamer 011/012/016 or FOI-adjacent L5; SACA 021 non-RGA filled tick776,,2026-08-03T12:00:00Z,2026-08-03T13:00:00Z,tick777: OAP022 FAVV 216.7 FPB 14.4 AFD 7.9 + HermReg E2 stack 7.9bn; spawn rq_769"
if old in rqt:
    rqt = rqt.replace(old, new)
    print("rq_768 done")
else:
    rqt = rqt.replace(
        "rq_768,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
        "rq_768,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    )
    print("rq_768 status-only")
rq_769 = "rq_769,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: flexi-jobs CoA/FPB eval or OAP022 Fedasil residual or FOI-adjacent L5; OAP022 non-Regie+HermReg E2 filled tick777,,2026-08-03T13:00:00Z,,spawned tick777 after rq_768\n"
if "rq_769," not in rqt:
    rqt = rqt.rstrip("\n") + "\n" + rq_769
    print("rq_769 spawned")
rq.write_text(rqt, encoding="utf-8", newline="\n")

# loop_state
(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_768,777,no,"
    "tick777 OAP022 FAVV 216.7 FPB 14.4 AFD 7.9 HermReg E2 7.9bn; next rq_769 flexi-jobs/Fedasil residual; progress@780 in 3; rq_116 deferred\n",
    encoding="utf-8",
    newline="\n",
)
print("loop_state ok")
