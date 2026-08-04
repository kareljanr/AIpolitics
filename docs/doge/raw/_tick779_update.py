from pathlib import Path

base = Path(r"docs/doge/data")
utc = "2026-08-03T15:00:00Z"
src = "src_kamer_fagg_oap_1281_022_2026"
src_dual = "src_dual_fagg_fees_tick779"

sp = base / "sources.csv"
st = sp.read_text(encoding="utf-8")
for row in [
f"{src},Kamer DOC 56 1281/022 OAP Annex I FAGG/AFMPS residual budget 2026,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Kamer / Chambre,2026-08-03,parliamentary,Strong tick779: Annex I p203-275; pers baremes 44.295 other 6.389 social 29.857 stack ~81.6m; ops lim 8.393 ICT 6.435 1FM 1.930 private third 3.297 Sciensano class 10.790; NAT 8.987 BCFI 2.929 patient orgs 0.197 CF_02 12.113; CF_00 dot 15.748 (path 22.224->15.748 CTR one-offs off); fees 36.20 41.645 + 36.90 63.187 ~104.8m; ATMP +1.023 package; dual Sciensano Smals; raw 56K1281022_oap.pdf",
f"{src_dual},Dual FAGG fee-funded stack vs Sciensano/INAMI/Smals residual tick779,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,DOGE synthesis,2026-08-03,synthesis,Strong dual not TE-additive: FAGG fees ~104.8m + dots ~27.9m; NAT blood dual transfusion; Sciensano expertise dual; Smals ICT dual",
]:
    sid = row.split(",")[0]
    if f"\n{sid}," not in st:
        with sp.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("src +", sid)

bud = base / "budgets.csv"
bt = bud.read_text(encoding="utf-8")
bud_rows = [
# Personnel
f"bud_afmps_pers_baremes_2026,afmps,2026,44294697,,,budgeted,{src},strong,11.11 baremes 44.295m 2026; tick779",
f"bud_afmps_pers_other_2026,afmps,2026,6388795,,,budgeted,{src},strong,11.12 other remun 6.389m 2026; tick779",
f"bud_afmps_social_contrib_2026,afmps,2026,29857012,,,budgeted,{src},strong,11.20 social contrib total 29.857m 2026; tick779",
f"bud_afmps_social_030_2026,afmps,2026,24466272,,,budgeted,{src},strong,11.20/001 24.466m 2026; tick779",
f"bud_afmps_social_patron_2026,afmps,2026,5390740,,,budgeted,{src},strong,Employer SS part 5.391m 2026; tick779",
f"bud_afmps_pers_stack_2026,afmps,2026,81554071,,,budgeted,{src},strong,Pers stack baremes+other+social ~81.554m 2026; tick779",
# Ops
f"bud_afmps_ops_lim_2026,afmps,2026,8393141,,,budgeted,{src},strong,12.11 lim ops 8.393m 2026; tick779",
f"bud_afmps_ict_nlim_2026,afmps,2026,6435000,,,budgeted,{src},strong,ICT n.lim 6.435m 2026 (Smals framework class); tick779",
f"bud_afmps_private_third_2026,afmps,2026,3297220,,,budgeted,{src},strong,Private-sector third-party 3.297m 2026; tick779",
f"bud_afmps_1fm_2026,afmps,2026,1930302,,,budgeted,{src},strong,1FM Galilee facility share 1.930m 2026 dual Sante/INAMI; tick779",
f"bud_afmps_sciensano_ops_2026,afmps,2026,10790094,,,budgeted,{src},strong,12.21 public-sector ops/Sciensano class 10.790m 2026; tick779",
f"bud_afmps_smals_eu_2026,afmps,2026,216000,,,budgeted,{src},strong,SMALS/EU projects ICT 0.216m 2026; tick779",
f"bud_afmps_atmp_package_2026,afmps,2026,1023000,,,budgeted,{src},strong,ATMP expertise package +1.023m embedded across lines 2026; tick779",
# Subsidies earmarked
f"bud_afmps_nat_tests_2026,afmps,2026,8987265,,,budgeted,{src},strong,NAT blood tests subsidies 8.987m 2026 dual transfusion; tick779",
f"bud_afmps_bcfi_2026,afmps,2026,2928860,,,budgeted,{src},strong,BCFI/CBIP subsidy 2.929m 2026; tick779",
f"bud_afmps_patient_orgs_2026,afmps,2026,197268,,,budgeted,{src},strong,Patient orgs LUSS+VPP 0.197m 2026; tick779",
f"bud_afmps_earmark_cf02_2026,afmps,2026,12113394,,,budgeted,{src},strong,46.10 CF_02 earmarked NAT+BCFI+patients 12.113m 2026; tick779",
# Dotations
f"bud_afmps_dot_cf00_2026,afmps,2026,15747722,,,budgeted,{src},strong,46.10 CF_00 main federal dot 15.748m 2026 (path 22.224 2025->15.748 CTR one-offs off); tick779",
f"bud_afmps_dot_total_2026,afmps,2026,27861116,,,budgeted,{src},strong,CF_00 15.748 + CF_02 12.113 = 27.861m federal transfer stack 2026; tick779",
f"bud_afmps_dot_cf00_2025,afmps,2025,22224474,,,budgeted,{src},strong,CF_00 total 22.224m 2025 (incl CTR summer deal advances); tick779",
# Fee revenues
f"bud_afmps_fees_3620_2026,afmps,2026,41644558,,,budgeted,{src},strong,36.20 consumption taxes/redev stack 41.645m 2026; tick779",
f"bud_afmps_fees_packaging_2026,afmps,2026,14044983,,,budgeted,{src},strong,Packaging/conditionnements class 14.045m 2026; tick779",
f"bud_afmps_fees_dm_3620_2026,afmps,2026,18074670,,,budgeted,{src},strong,Medical devices 36.20 line 18.075m 2026; tick779",
f"bud_afmps_fees_3690_2026,afmps,2026,63186508,,,budgeted,{src},strong,36.90 redevances/fees stack 63.187m 2026; tick779",
f"bud_afmps_fees_amm_2026,afmps,2026,18805674,,,budgeted,{src},strong,AMM authorisations 18.806m 2026; tick779",
f"bud_afmps_fees_registrations_2026,afmps,2026,12725547,,,budgeted,{src},strong,Drug registrations 12.726m 2026; tick779",
f"bud_afmps_fees_mdr_2026,afmps,2026,9872659,,,budgeted,{src},strong,MDR devices fees 9.873m 2026; tick779",
f"bud_afmps_fees_total_2026,afmps,2026,104831066,,,budgeted,{src},strong,Fee stack 36.20+36.90 104.831m 2026; tick779",
f"bud_afmps_interest_2026,afmps,2026,959388,,,budgeted,{src},strong,Debt Agency reserve interest 0.959m 2026; tick779",
f"bud_afmps_eu_projects_rec_2026,afmps,2026,888400,,,budgeted,{src},strong,EU project receipts 0.888m 2026; tick779",
f"bud_afmps_spend_class_2026,afmps,2026,110519400,,,budgeted,{src},medium,Approx spend class pers 81.6 + ops lim 8.4 + ICT 6.4 + Sciensano 10.8 + earmark subs 12.1 + private/1FM ~5.2 ~110.5m; medium sum of OAP lines not full P&L; tick779",
]
added_b = 0
with bud.open("a", encoding="utf-8", newline="\n") as f:
    for row in bud_rows:
        bid = row.split(",")[0]
        if f"\n{bid}," not in bt:
            f.write(row + "\n")
            added_b += 1
print("bud +", added_b)

cmt = base / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
cmt_rows = [
f'cmt_afmps_oap_2026,FAGG/AFMPS OAP 2026 fee+dot package,afmps,pharma medtech,Kamer 1281/022 Annex I,2026-01-28,2026,2026,0,"{{""pers_m"": 81.6, ""fees_m"": 104.8, ""dot_cf00_m"": 15.748, ""dot_cf02_m"": 12.113, ""nat_m"": 8.987, ""bcfi_m"": 2.929, ""ict_m"": 6.435, ""sciensano_class_m"": 10.790, ""atmp_m"": 1.023}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Medicines and devices agency fee-funded model,Fee FOI,{src},strong,Federal>AFMPS>OAP,tick779',
f'cmt_afmps_nat_2026,FAGG NAT blood test subsidies 8.987m 2026,afmps,blood transfusion centers,OAP CF_02,2026-01-28,2026,2026,8987265,"{{""nat_m"": 8.987}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,NAT testing dual transfusion network,Health FOI,{src},strong,Federal>AFMPS>NAT,tick779',
f'cmt_afmps_dot_path_2026,FAGG CF_00 dot 22.2->15.7m path 2025-26,afmps,FAGG,CTR summer deal off,2026-01-28,2025,2026,0,"{{""2025_m"": 22.224, ""2026_m"": 15.748, ""delta_m"": -6.476, ""note"": ""CTR advances off one-offs""}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Dotation path after clinical trial advances,Transparency,{src},strong,Federal>AFMPS>dot,tick779',
f'cmt_dual_fagg_tick779,Dual FAGG fees/dots vs Sciensano Smals residual tick779,gg_belgium,dual map,OAP022 FAGG,2026-08-03,2026,2026,0,"{{""fees_m"": 104.8, ""dots_m"": 27.9, ""sciensano_class_m"": 10.8, ""ict_m"": 6.4, ""note"": ""not TE-additive""}}",0,active,https://www.dekamer.be/FLWB/PDF/56/1281/56K1281022.pdf,Map fee-funded health regulator dual,L5 FOI,{src_dual},strong,Belgium>dual>fagg,tick779',
]
added_c = 0
with cmt.open("a", encoding="utf-8", newline="\n") as f:
    for row in cmt_rows:
        cid = row.split(",")[0]
        if f"\n{cid}," not in ct:
            f.write(row + "\n")
            added_c += 1
print("cmt +", added_c)

lb = base / "leaderboard.csv"
lt = lb.read_text(encoding="utf-8")
lb_rows = [
f"lb_afmps_fees_105m_2026,FAGG fee stack 104.8m 2026,L5,ops,Federal>AFMPS>fees,104831066,104831066,Strong 36.20 41.6 + 36.90 63.2; fee-funded regulator dual,strong,{src},industry,see,primary Kamer,4.0,8.0,3.0,5.5,Fee FOI,active,,tick779",
f"lb_afmps_pers_82m_2026,FAGG personnel stack 81.6m 2026,L5,ops,Federal>AFMPS>personnel,81554071,81554071,Strong baremes 44.3 + social 29.9 + other 6.4,strong,{src},staff,see,primary Kamer,3.0,7.5,3.0,4.95,FTE FOI,active,,tick779",
f"lb_afmps_nat_9m_2026,FAGG NAT blood subsidies 8.987m 2026,L5,transfer,Federal>AFMPS>NAT,8987265,8987265,Strong dual transfusion network pass-through,strong,{src},blood centers,see,primary Kamer,3.5,5.0,2.5,3.95,Health FOI,active,,tick779",
f"lb_afmps_sciensano_11m_2026,FAGG Sciensano/public ops class 10.8m 2026,L5,ops,Federal>AFMPS>Sciensano,10790094,10790094,Strong dual Sciensano expertise channel,strong,{src},Sciensano,see,primary Kamer,4.0,5.5,2.5,4.35,Dual FOI,active,,tick779",
f"lb_afmps_ict_6_4m_2026,FAGG ICT 6.435m 2026,L5,ops,Federal>AFMPS>ICT,6435000,6435000,Strong Smals framework class dual Smals broker,strong,{src},IT,see,primary Kamer,4.0,4.5,2.5,4.05,Smals FOI,active,,tick779",
f"lb_afmps_dot_15_7m_2026,FAGG CF_00 dot 15.748m 2026,L5,transfer,Federal>AFMPS>dot,15747722,15747722,Strong path down from 22.2m after CTR one-offs,strong,{src},agency,see,primary Kamer,3.0,5.5,2.0,3.85,Transparency,active,,tick779",
f"lb_afmps_amm_19m_2026,FAGG AMM authorisation fees 18.8m 2026,L5,ops,Federal>AFMPS>AMM,18805674,18805674,Strong largest single fee line dual pharma,strong,{src},pharma,see,primary Kamer,3.5,6.0,2.5,4.35,Fee FOI,active,,tick779",
f"lb_dual_fagg_2026,Dual FAGG fee/dot vs Sciensano Smals map,L5,transfer,Belgium>dual>fagg,104831066,0,Strong dual not TE-additive fee regulator,strong,{src_dual},public,see,primary,4.5,8.0,3.0,5.55,L5 FOI,active,,tick779",
]
added_l = 0
with lb.open("a", encoding="utf-8", newline="\n") as f:
    for row in lb_rows:
        lid = row.split(",")[0]
        if f"\n{lid}," not in lt:
            f.write(row + "\n")
            added_l += 1
print("lb +", added_l)

foi = base / "foi_queue.csv"
gap = "gap_fagg_fees_nat_sciensano_l5"
ft = foi.read_text(encoding="utf-8")
foi_row = (
    f"{gap},Federal>AFMPS>fees_NAT_Sciensano_L5,afmps,"
    "Fee tariff schedule behind 104.8m; AMM under-collection path vs budget; NAT beneficiary list behind 8.987m; "
    "Sciensano contract FTE behind 10.8m; Smals ICT detail behind 6.4m; ATMP +1.023 package scope; "
    "CTR summer-deal recon 2025 one-offs vs 2026 dot 15.7m,"
    "Fee-funded regulator public at aggregate; dual health-science residual,8,"
    "FAGG/AFMPS / FOD Volksgezondheid FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-03,,,,,"
    "cmt_afmps_oap_2026|cmt_afmps_nat_2026|cmt_afmps_dot_path_2026|cmt_dual_fagg_tick779,"
    "lb_afmps_fees_105m_2026|lb_afmps_nat_9m_2026|lb_afmps_sciensano_11m_2026|lb_dual_fagg_2026,"
    f"{utc},{utc},tick779 Kamer 1281/022 FAGG annex primary; human send only"
)
if f"\n{gap}," not in ft:
    with foi.open("a", encoding="utf-8", newline="\n") as f:
        f.write(foi_row + "\n")
    print("foi +")

rq = base / "research_queue.csv"
rqt = rq.read_text(encoding="utf-8")
old = "rq_770,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: FAGG annex OAP022 residual or flexi annual fiscal cost FOI-adjacent or Entity II L5; Fedasil OAP L5 filled tick778; progress@780 after +2,,2026-08-03T14:00:00Z,,spawned tick778 after rq_769"
new = "rq_770,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Next residual: FAGG annex OAP022 residual or flexi annual fiscal cost FOI-adjacent or Entity II L5; Fedasil OAP L5 filled tick778; progress@780 after +2,,2026-08-03T14:00:00Z,2026-08-03T15:00:00Z,tick779: FAGG fees 104.8 pers 81.6 NAT 9.0 Sciensano 10.8 dot 15.7; spawn rq_771 PROGRESS@780"
if old in rqt:
    rqt = rqt.replace(old, new)
else:
    rqt = rqt.replace(
        "rq_770,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
        "rq_770,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    )
rq_771 = "rq_771,Progress@780 coverage % layers A-E + waste top10,continuous,5,open,L0,gg_belgium,Mandatory progress@780: refresh progress_every_10_ticks.md and doge_waste_top10_current.md; then spawn next residual,,2026-08-03T15:00:00Z,,spawned tick779 after rq_770 for progress@780\n"
if "rq_771," not in rqt:
    rqt = rqt.rstrip("\n") + "\n" + rq_771
rq.write_text(rqt, encoding="utf-8", newline="\n")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_770,779,no,"
    "tick779 FAGG fees 104.8 pers 81.6 NAT 9 Sciensano 10.8 dot 15.7; next rq_771 PROGRESS@780; rq_116 deferred\n",
    encoding="utf-8",
    newline="\n",
)
print("done ticks=779")
