from pathlib import Path

base = Path(r"docs/doge/data")
utc = "2026-08-03T14:00:00Z"
src = "src_kamer_fedasil_oap_1281_022_2026"
src_flex = "src_fpb_flexijobs_coa_2026_tick778"
src_dual = "src_dual_fedasil_flexi_tick778"

# sources
sp = base / "sources.csv"
st = sp.read_text(encoding="utf-8")
src_rows = [
f"{src},Kamer DOC 56 1281/022 OAP Fedasil EN_62005 residual L5 budget 2026,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Kamer / Chambre,2026-08-03,parliamentary,Strong tick778: Fedasil OAP p156-200; pers wages 201.462 other 3.170 nature 3.739 stack ~208.4m; ops 12.11 38.515 rent 23.974; transfers 33.00 120.018 (orgs 117.880 cut from 274.780); LOI 67.071 medical 17.754 pocket 9.073 inkind centers 54.635; VT package 11.575; invest bldg 7.090; federal places 13434; dot 702.205 confirms 006; raw 56K1281022_oap.pdf",
f"{src_flex},FPB+CoA flexi-jobs evaluation art.192 programmawet (Jan 2026 report Jul pub),https://www.plan.be/sites/default/files/documents/REP_FLEXIJOBS_13336_MIX.pdf,Federaal Planbureau / Rekenhof,2026-08-03,official_eval,Strong tick778 residual vs tick407: Q4-2024 184360 workers 13.996m hours wage mass 220.071m FTE 29500; error flags 11k-17k/q; inspections 270/154 infringe 57pct; HERMES horeca abolish V1/V2 saldo +105.8/+212.9m 2030; raw fpb_flexijobs_13336.pdf",
f"{src_dual},Dual Fedasil OAP L5 cut path vs flexi taxex residual tick778,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,DOGE synthesis,2026-08-03,synthesis,Strong dual not TE-additive: Fedasil org transfers 274.8->117.9m; flexi wage mass 220m Q4 tax-free dual SS; capacity 13434 federal places",
]
for row in src_rows:
    sid = row.split(",")[0]
    if f"\n{sid}," not in st:
        with sp.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("source +", sid)

# budgets
bud = base / "budgets.csv"
bt = bud.read_text(encoding="utf-8")
bud_rows = [
# Fedasil personnel
f"bud_fedasil_wages_main_2026,fedasil,2026,194062124,,,budgeted,{src},strong,11.11/001 wages main 194.062m 2026; tick778",
f"bud_fedasil_wages_eu_2026,fedasil,2026,7399794,,,budgeted,{src},strong,11.11/002 EU project wages 7.400m 2026; tick778",
f"bud_fedasil_wages_total_2026,fedasil,2026,201461918,,,budgeted,{src},strong,11.11 total wages 201.462m 2026; tick778",
f"bud_fedasil_other_remun_2026,fedasil,2026,3169757,,,budgeted,{src},strong,11.12 other remun 3.170m 2026; tick778",
f"bud_fedasil_wages_nature_2026,fedasil,2026,3738720,,,budgeted,{src},strong,11.40 wages in kind 3.739m 2026; tick778",
f"bud_fedasil_pers_stack_2026,fedasil,2026,208411174,,,budgeted,{src},strong,Pers stack wages+other+nature+allow ~208.4m 2026; tick778",
# Fedasil ops
f"bud_fedasil_ops_1211_2026,fedasil,2026,38515218,,,budgeted,{src},strong,12.11 ops total 38.515m 2026 (varia 24.117 third-party 4.176 litigation 2.215); tick778",
f"bud_fedasil_ops_varia_bld_2026,fedasil,2026,24116507,,,budgeted,{src},strong,12.11/003 building/varia/insurance 24.117m 2026; tick778",
f"bud_fedasil_ops_third_2026,fedasil,2026,4175710,,,budgeted,{src},strong,12.11/008 third-party 4.176m 2026; tick778",
f"bud_fedasil_ops_litigation_2026,fedasil,2026,2214970,,,budgeted,{src},strong,12.11/006 litigation 2.215m 2026; tick778",
f"bud_fedasil_rent_2026,fedasil,2026,23973610,,,budgeted,{src},strong,12.12 building rent total 23.974m 2026 (main 23.893); tick778",
f"bud_fedasil_ops_rent_stack_2026,fedasil,2026,62488828,,,budgeted,{src},strong,Ops 38.515 + rent 23.974 = 62.489m 2026; tick778",
# Transfers / reception
f"bud_fedasil_xfer_orgs_2026,fedasil,2026,117879644,,,budgeted,{src},strong,33.00/002 grants to orgs 117.880m 2026 (cut from 274.780m 2025); tick778",
f"bud_fedasil_xfer_33_total_2026,fedasil,2026,120017814,,,budgeted,{src},strong,33.00 total transfers 120.018m 2026 (was 281.211); tick778",
f"bud_fedasil_xfer_conventions_2026,fedasil,2026,848770,,,budgeted,{src},strong,33.00/001 specific conventions 0.849m 2026 (-7.9pct); tick778",
f"bud_fedasil_future_orient_2026,fedasil,2026,1289400,,,budgeted,{src},strong,33.00/004 Toekomstorientatie 1.289m 2026; tick778",
f"bud_fedasil_loi_2026,fedasil,2026,67071200,,,budgeted,{src},strong,LOI local reception init 67.071m 2026; tick778",
f"bud_fedasil_pocket_money_2026,fedasil,2026,9073358,,,budgeted,{src},strong,34.31 cash pocket/community 9.073m 2026; capacity 13434 places; tick778",
f"bud_fedasil_inkind_centers_2026,fedasil,2026,54635423,,,budgeted,{src},strong,34.32 in-kind federal centers food/hygiene 54.635m 2026; tick778",
f"bud_fedasil_medical_2026,fedasil,2026,17753686,,,budgeted,{src},strong,Medical costs asylum 17.754m 2026; tick778",
f"bud_fedasil_vt_package_2026,fedasil,2026,11574822,,,budgeted,{src},strong,Voluntary return package 11.575m 2026 (VT 4.680 IOM-Reab 3.875 reinteg 4.008); tick778",
f"bud_fedasil_vt_iom_caritas_2026,fedasil,2026,3785156,,,budgeted,{src},strong,IOM 1.908 + Caritas 1.877 = 3.785m within VT stack; tick778",
f"bud_fedasil_invest_bldg_2026,fedasil,2026,7090002,,,budgeted,{src},strong,Building invest 7.090m 2026; tick778",
f"bud_fedasil_dot_oap_2026,fedasil,2026,702205147,,,budgeted,{src},strong,46.10 OAP federal dot total 702.205m 2026 confirms 006/CoA path; tick778",
f"bud_fedasil_dot_eu_cofin_2026,fedasil,2026,2306892,,,budgeted,{src},strong,46.10/002 EU cofin portion of federal dot 2.307m 2026; tick778",
f"bud_fedasil_capacity_places_2026,fedasil,2026,13434,,,budgeted,{src},strong,Federal centers capacity 13434 places 2026 (count not EUR); tick778",
f"bud_fedasil_org_cut_yoy_2026,fedasil,2026,-156899962,,,budgeted,{src},strong,YoY cut orgs transfer 274.780-117.880 = -156.900m 2026; tick778",
# Flexi residual
f"bud_flexi_workers_q4_2024,sec_ss,2024,184360,,,outturn_onss,{src_flex},strong,Q4-2024 flexi workers 184360 (count); tick778",
f"bud_flexi_hours_q4_2024,sec_ss,2024,13995721,,,outturn_onss,{src_flex},strong,Q4-2024 flexi hours 13.995721m; tick778",
f"bud_flexi_wage_mass_q4_2024_confirm,sec_ss,2024,220071000,,,outturn_onss,{src_flex},strong,Q4-2024 wage mass 220.071m confirms tick407; tick778",
f"bud_flexi_hourly_men_2024,sec_ss,2024,16.38,,,outturn_onss,{src_flex},strong,Avg flexi hourly men 16.38 EUR Q4-2024; tick778",
f"bud_flexi_hourly_women_2024,sec_ss,2024,15.00,,,outturn_onss,{src_flex},strong,Avg flexi hourly women 15.00 EUR Q4-2024; tick778",
f"bud_flexi_error_flags_q4_2024,sec_ss,2024,17130,,,outturn_onss,{src_flex},strong,Q4-2024 DmfA error flags 17130 (of 184360 jobs ~9pct); tick778",
f"bud_flexi_inspections_2024,sec_ss,2024,270,,,outturn,{src_flex},strong,Flexi inspections 270 in 2024 of which 154 infringe 57pct; tick778",
f"bud_flexi_infringe_2024,sec_ss,2024,154,,,outturn,{src_flex},strong,Flexi inspection infringements 154 2024; tick778",
f"bud_flexi_cap_nonretire_2024,sec_ss,2024,12000,,,budgeted,{src_flex},strong,Annual flexi pay cap non-retirees 12000 EUR (path raise 18000 planned); tick778",
]
added_b = 0
with bud.open("a", encoding="utf-8", newline="\n") as f:
    for row in bud_rows:
        bid = row.split(",")[0]
        if f"\n{bid}," not in bt:
            f.write(row + "\n")
            added_b += 1
        else:
            print("bud exists", bid)
print("budgets +", added_b)

# commitments
cmt = base / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
cmt_rows = [
f'cmt_fedasil_oap_l5_2026,Fedasil OAP L5 structure 2026 (pers 208 ops+rent 62 xfer 120),fedasil,asylum seekers,Kamer 1281/022 EN_62005,2026-01-28,2026,2026,702205147,"{{""pers_m"": 208.4, ""ops_rent_m"": 62.5, ""xfer_33_m"": 120.0, ""orgs_m"": 117.9, ""loi_m"": 67.1, ""inkind_m"": 54.6, ""medical_m"": 17.8, ""vt_m"": 11.6, ""places"": 13434, ""dot_m"": 702.2}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Asylum reception network L5,Capacity FOI,{src},strong,Federal>Fedasil>OAP,tick778',
f'cmt_fedasil_org_cut_2026,Fedasil org grants cut 156.9m YoY 2026,fedasil,reception NGOs,OAP 33.00/002,2026-01-28,2026,2026,-156899962,"{{""2025_m"": 274.780, ""2026_m"": 117.880, ""cut_m"": -156.900, ""note"": ""capacity-driven savings path""}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Reception partner network contraction,LOI dual FOI,{src},strong,Federal>Fedasil>orgs,tick778',
f'cmt_fedasil_loi_2026,Fedasil LOI local reception 67.071m 2026,fedasil,communes,OAP 533-03,2026-01-28,2026,2026,67071200,"{{""loi_m"": 67.071, ""places_fed"": 13434}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Local reception initiatives,Municipal FOI,{src},strong,Federal>Fedasil>LOI,tick778',
f'cmt_fedasil_vt_2026,Fedasil voluntary return package 11.575m 2026,fedasil,IOM Caritas,OAP VT stack,2026-01-28,2026,2026,11574822,"{{""vt"": 4680076, ""iom_reab"": 3874626, ""reinteg"": 4007978, ""iom"": 1908000, ""caritas"": 1877156}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Voluntary return and reintegration,Partner FOI,{src},strong,Federal>Fedasil>return,tick778',
f'cmt_flexi_enforcement_2024,Flexi enforcement residual 2024 (flags+inspections),sec_ss,ONSS inspection,FPB+CoA flexi report,2026-01-01,2024,2024,0,"{{""workers_q4"": 184360, ""error_flags_q4"": 17130, ""inspections"": 270, ""infringe"": 154, ""wage_mass_q4_m"": 220.071}}",0,active,https://www.plan.be/sites/default/files/documents/REP_FLEXIJOBS_13336_MIX.pdf,Flexi compliance residual,Taxex FOI,{src_flex},strong,Federal>SS>flexi,tick778',
f'cmt_dual_fedasil_flexi_tick778,Dual Fedasil L5 cut vs flexi wage-mass residual tick778,gg_belgium,dual map,OAP022+flexi report,2026-08-03,2026,2026,0,"{{""fedasil_org_cut_m"": -156.9, ""fedasil_dot_m"": 702.2, ""flexi_wage_q4_m"": 220.1, ""note"": ""not TE-additive""}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Map reception cuts and flexi taxex,L5 FOI,{src_dual},strong,Belgium>dual>fedasil_flexi,tick778',
]
added_c = 0
with cmt.open("a", encoding="utf-8", newline="\n") as f:
    for row in cmt_rows:
        cid = row.split(",")[0]
        if f"\n{cid}," not in ct:
            f.write(row + "\n")
            added_c += 1
print("cmt +", added_c)

# leaderboard
lb = base / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
lb_rows = [
f"lb_fedasil_pers_208m_2026,Fedasil personnel stack 208.4m 2026,L5,ops,Federal>Fedasil>personnel,208411174,208411174,Strong wages 201.5 + other 3.2 + nature 3.7; dual package 702,strong,{src},staff,see,primary Kamer,3.5,8.0,3.0,5.35,FTE FOI,active,,tick778",
f"lb_fedasil_org_cut_157m_2026,Fedasil org grants cut 156.9m YoY 2026,L5,transfer,Federal>Fedasil>orgs,-156899962,0,Strong 274.8->117.9m orgs; capacity path dual LOI,strong,{src},NGOs,see,primary Kamer,5.0,8.5,3.5,6.15,Partner FOI,active,,tick778",
f"lb_fedasil_loi_67m_2026,Fedasil LOI local reception 67.1m 2026,L5,transfer,Federal>Fedasil>LOI,67071200,67071200,Strong local reception initiatives dual communes,strong,{src},communes,see,primary Kamer,3.5,7.0,3.0,4.9,Municipal FOI,active,,tick778",
f"lb_fedasil_inkind_55m_2026,Fedasil federal centers in-kind 54.6m 2026,L5,ops,Federal>Fedasil>centers,54635423,54635423,Strong food/hygiene centers; capacity 13434 places,strong,{src},asylum seekers,see,primary Kamer,3.0,7.0,2.5,4.55,Unit cost FOI,active,,tick778",
f"lb_fedasil_ops_rent_62m_2026,Fedasil ops+rent 62.5m 2026,L5,ops,Federal>Fedasil>ops,62488828,62488828,Strong ops 38.5 (varia 24.1) + rent 24.0,strong,{src},agency,see,primary Kamer,3.5,6.5,2.5,4.6,L5 FOI,active,,tick778",
f"lb_fedasil_vt_11_6m_2026,Fedasil voluntary return 11.6m 2026,L5,transfer,Federal>Fedasil>return,11574822,11574822,Strong IOM+Caritas+reinteg package,strong,{src},returnees,see,primary Kamer,3.0,5.0,2.5,3.85,Partner FOI,active,,tick778",
f"lb_flexi_wage_220m_q4_2024,Flexi wage mass 220.1m Q4-2024,L5,taxex,Federal>SS>flexi,220071000,220071000,Strong ONSS Q4 mass; tax-free worker side dual SS,strong,{src_flex},flexi workers,see,primary CoA/FPB,5.0,8.0,3.5,5.95,Reform FOI,active,,tick778",
f"lb_flexi_enforce_gap_2024,Flexi enforcement residual flags+inspections 2024,L5,ops,Federal>SS>flexi_enforce,0,0,Strong 17k flags/q + 270 insp 57pct infringe vs 184k jobs; amount 0=count residual,strong,{src_flex},ONSS,see,primary CoA/FPB,4.5,5.0,2.5,4.35,Compliance FOI,active,,tick778",
f"lb_dual_fedasil_flexi_2026,Dual Fedasil cut path vs flexi taxex residual,L5,transfer,Belgium>dual>fedasil_flexi,702205147,0,Strong dual not TE-additive reception L5 vs flexi wage-mass,strong,{src_dual},public,see,primary,4.5,8.5,3.0,5.8,L5 FOI,active,,tick778",
]
added_l = 0
with lb.open("a", encoding="utf-8", newline="\n") as f:
    for row in lb_rows:
        lid = row.split(",")[0]
        if f"\n{lid}," not in lt:
            f.write(row + "\n")
            added_l += 1
print("lb +", added_l)

# foi
foi = base / "foi_queue.csv"
gap = "gap_fedasil_oap_loi_org_l5"
ft = foi.read_text(encoding="utf-8")
foi_row = (
    f"{gap},Federal>Fedasil>OAP_LOI_org_L5,fedasil,"
    "Unit cost per federal place behind in-kind 54.6m and capacity 13434; LOI commune list behind 67.1m; "
    "org partner ranking behind 117.9m (cut 156.9); VT IOM/Caritas contract detail; medical residual; "
    "flexi dual taxex annual fiscal cost beyond Q4 mass,"
    "Fedasil package public at aggregate; OAP L5 partner/capacity residual,9,"
    "Fedasil / FOD IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-03,,,,,"
    "cmt_fedasil_oap_l5_2026|cmt_fedasil_org_cut_2026|cmt_fedasil_loi_2026|cmt_fedasil_vt_2026,"
    "lb_fedasil_org_cut_157m_2026|lb_fedasil_loi_67m_2026|lb_fedasil_inkind_55m_2026|lb_dual_fedasil_flexi_2026,"
    f"{utc},{utc},tick778 Kamer 1281/022 Fedasil primary; human send only"
)
if f"\n{gap}," not in ft:
    with foi.open("a", encoding="utf-8", newline="\n") as f:
        f.write(foi_row + "\n")
    print("foi +")

# research queue
rq = base / "research_queue.csv"
rqt = rq.read_text(encoding="utf-8")
old = "rq_769,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: flexi-jobs CoA/FPB eval or OAP022 Fedasil residual or FOI-adjacent L5; OAP022 non-Regie+HermReg E2 filled tick777,,2026-08-03T13:00:00Z,,spawned tick777 after rq_768"
new = "rq_769,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Next residual: flexi-jobs CoA/FPB eval or OAP022 Fedasil residual or FOI-adjacent L5; OAP022 non-Regie+HermReg E2 filled tick777,,2026-08-03T13:00:00Z,2026-08-03T14:00:00Z,tick778: Fedasil OAP L5 pers 208 org cut 157 LOI 67 + flexi residual; spawn rq_770"
if old in rqt:
    rqt = rqt.replace(old, new)
else:
    rqt = rqt.replace(
        "rq_769,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
        "rq_769,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    )
rq_770 = "rq_770,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: FAGG annex OAP022 residual or flexi annual fiscal cost FOI-adjacent or Entity II L5; Fedasil OAP L5 filled tick778; progress@780 after +2,,2026-08-03T14:00:00Z,,spawned tick778 after rq_769\n"
if "rq_770," not in rqt:
    rqt = rqt.rstrip("\n") + "\n" + rq_770
rq.write_text(rqt, encoding="utf-8", newline="\n")
print("rq ok")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_769,778,no,"
    "tick778 Fedasil OAP L5 pers 208 org cut 157 LOI 67 VT 11.6 places 13434 + flexi residual; "
    "next rq_770 FAGG/EntityII; progress@780 in 2; rq_116 deferred\n",
    encoding="utf-8",
    newline="\n",
)
print("state ok")
