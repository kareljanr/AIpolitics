from pathlib import Path

base = Path(r"docs/doge/data")
utc = "2026-08-03T17:00:00Z"
src = "src_kamer_beleid_sante_1282_009_2026"
src_dual = "src_dual_riziv_measures_tick781"

sp = base / "sources.csv"
st = sp.read_text(encoding="utf-8")
for row in [
f"{src},Kamer DOC 56 1282/009 Beleidsnota Volksgezondheid RIZIV residual measures 2026,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Kamer / Minister Volksgezondheid,2026-08-03,parliamentary,Strong tick781: 59p; ZIV/AMI total 41.297bn 2026 (+1.566bn; growth 2pct + index 2.72pct); correction package drugs 227.9 doctors 150 day-hosp 50 other 47 ~474.9 class dual 470.8m; tickets +125m/yr from 1 Jul 2026 reinvested; effic 247m 2028 684m 2029; care envelope 207m 2028 427m 2029; Medicomut GP 21.072m 2026 of 42.5m to 2027; OA mutual 25m 2026 path +100m; prev 24.73m; pharma multi-year 4.7m 2026 path 14.4m 2029; raw 56K1282009_beleid_gezondheid.pdf",
f"{src_dual},Dual RIZIV care 41.3bn vs correction package + tickets reinvest tick781,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,DOGE synthesis,2026-08-03,synthesis,Strong dual not TE-additive: care benefits 41.297 vs drugs/doctors corrections; tickets 125m reinvest vs care-staff path; effic multi-year 247/684",
]:
    sid = row.split(",")[0]
    if f"\n{sid}," not in st:
        with sp.open("a", encoding="utf-8", newline="\n") as f:
            f.write(row + "\n")
        print("src +", sid)

bud = base / "budgets.csv"
bt = bud.read_text(encoding="utf-8")
bud_rows = [
f"bud_riziv_ami_total_beleid_2026,riziv,2026,41297000000,,,budgeted,{src},strong,Beleidsnota: ZIV/AMI total 41.297bn 2026 (+1.566bn); dual care auth 40.986; tick781",
f"bud_riziv_ami_extra_2026,riziv,2026,1566000000,,,budgeted,{src},strong,Extra investment 1.566bn 2026 (growth norm 2pct + index 2.72pct); tick781",
f"bud_riziv_corr_drugs_2026,riziv,2026,227900000,,,budgeted,{src},strong,Pharma sector correction 227.9m 2026 (multi-year framework 17.3pct of net care); tick781",
f"bud_riziv_corr_doctors_2026,riziv,2026,150000000,,,budgeted,{src},strong,Medical doctor prestations correction 150m 2026 (imaging surgery labs); tick781",
f"bud_riziv_corr_dayhosp_2026,riziv,2026,50000000,,,budgeted,{src},strong,Day-hospital prestations correction 50m 2026; tick781",
f"bud_riziv_corr_other_sectors_2026,riziv,2026,47000000,,,budgeted,{src},strong,Other sectors package 47m 2026 (implants rehab home-care orthopedists class); tick781",
f"bud_riziv_corr_package_sum_2026,riziv,2026,474900000,,,budgeted,{src},strong,Sum drugs+doctors+dayhosp+other 474.9m class dual official corrections 470.775m; tick781",
f"bud_riziv_tickets_mod_125m_2026,riziv,2026,125000000,,,budgeted,{src},strong,Tickets moderators +125m/yr from 1 Jul 2026 fully reinvested in care staff/priorities; tick781",
f"bud_riziv_effic_save_2028,riziv,2028,247000000,,,budgeted,{src},strong,Structural efficiency measures 247m 2028 within growth norm; tick781",
f"bud_riziv_effic_save_2029,riziv,2029,684000000,,,budgeted,{src},strong,Structural efficiency measures 684m 2029; tick781",
f"bud_riziv_care_staff_env_2028,riziv,2028,207000000,,,budgeted,{src},strong,Special envelope care staff+priorities 207m 2028 (above growth norm); tick781",
f"bud_riziv_care_staff_env_2029,riziv,2029,427000000,,,budgeted,{src},strong,Special envelope care staff+priorities 427m 2029; tick781",
f"bud_riziv_growth_norm_2028_pct,riziv,2028,2.6,,,budgeted,{src},strong,Growth norm rises to 2.6pct 2028 (amount=pct); tick781",
f"bud_riziv_growth_norm_2029_pct,riziv,2029,3.0,,,budgeted,{src},strong,Growth norm to 3.0pct 2029 (amount=pct); tick781",
f"bud_riziv_medicomut_gp_2026,riziv,2026,21072000,,,budgeted,{src},strong,Medicomut GP cabinet prime share 21.072m 2026 of 42.5m to 2027; tick781",
f"bud_riziv_medicomut_gp_path_2027,riziv,2027,42500000,,,budgeted,{src},strong,Medicomut GP cabinets envelope 42.5m by 2027; tick781",
f"bud_riziv_oa_mutual_extra_2026,riziv,2026,25000000,,,budgeted,{src},strong,Mutualities/OA extra effort 25m 2026 (path gradual +100m class); tick781",
f"bud_riziv_prevention_budget_2026,riziv,2026,24730000,,,budgeted,{src},strong,Prevention envelope class 24.73m 2026; tick781",
f"bud_riziv_rehab_effort_2026,riziv,2026,7000000,,,budgeted,{src},strong,Rehab structural effort >7m 2026; tick781",
f"bud_riziv_pharma_multi_2026,riziv,2026,4700000,,,budgeted,{src},strong,Pharma multi-year first envelope 4.7m 2026 (path 14.4m 2029); tick781",
f"bud_riziv_pharma_multi_2029,riziv,2029,14400000,,,budgeted,{src},strong,Pharma multi-year envelope 14.4m 2029; tick781",
f"bud_riziv_pharma_net_impact_2026,riziv,2026,3000000,,,budgeted,{src},strong,Net budget impact pharma multi-year 3m 2026 path 11m 2029; tick781",
f"bud_riziv_indoor_air_pilot_2026,riziv,2026,600000,,,budgeted,{src},strong,Indoor air quality pilot call 0.6m 2026; tick781",
f"bud_riziv_fed_budget_help_2028,riziv,2028,40000000,,,budgeted,{src},strong,Efficiency share to federal budget help 40m 2028; tick781",
f"bud_riziv_fed_budget_help_2029,riziv,2029,257000000,,,budgeted,{src},strong,Efficiency share to federal budget help 257m 2029 final; tick781",
]
added_b = 0
with bud.open("a", encoding="utf-8", newline="\n") as f:
    for row in bud_rows:
        bid = row.split(",")[0]
        if f"\n{bid}," not in bt:
            f.write(row + "\n")
            added_b += 1
        else:
            print("exists", bid)
print("bud +", added_b)

cmt = base / "commitments.csv"
ct = cmt.read_text(encoding="utf-8")
cmt_rows = [
f'cmt_riziv_ami_2026,RIZIV ZIV/AMI total 41.297bn 2026,riziv,patients providers,Algemene Raad 20 Oct 2025,2025-10-20,2026,2026,41297000000,"{{""total_bn"": 41.297, ""extra_bn"": 1.566, ""growth_pct"": 2.0, ""index_pct"": 2.72}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Compulsory health insurance objective,Programme FOI,{src},strong,Federal>RIZIV>AMI,tick781',
f'cmt_riziv_corr_package_2026,RIZIV correction package ~475m 2026,riziv,pharma doctors hospitals,Conseil general measures,2025-10-20,2026,2026,474900000,"{{""drugs_m"": 227.9, ""doctors_m"": 150.0, ""dayhosp_m"": 50.0, ""other_m"": 47.0, ""official_corr_m"": 470.775}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Efficiency corrections within care budget,Drug FOI,{src},strong,Federal>RIZIV>corrections,tick781',
f'cmt_riziv_tickets_reinvest_2026,Tickets moderators +125m/yr reinvest from Jul 2026,riziv,patients care staff,Budget conclave,2025-11-01,2026,2029,125000000,"{{""annual_m"": 125, ""start"": ""2026-07-01"", ""reinvest"": ""care staff and priorities""}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Patient co-pay increase fully recycled to care,Access FOI,{src},strong,Federal>RIZIV>tickets,tick781',
f'cmt_riziv_effic_path_2028_29,RIZIV efficiency path 247m 2028 / 684m 2029,riziv,care system,Multi-year growth norm framework,2025-11-01,2028,2029,931000000,"{{""2028_m"": 247, ""2029_m"": 684, ""fed_help_2028_m"": 40, ""fed_help_2029_m"": 257, ""care_env_2028_m"": 207, ""care_env_2029_m"": 427}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Structural efficiency within growth norm,Multi-year FOI,{src},strong,Federal>RIZIV>efficiency,tick781',
f'cmt_riziv_medicomut_gp_2026_27,Medicomut GP cabinets 21.1m 2026 of 42.5m to 2027,riziv,GPs,Medicomut agreement,2025-12-22,2026,2027,42500000,"{{""2026_m"": 21.072, ""path_2027_m"": 42.5}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Primary care practice support,GP FOI,{src},strong,Federal>RIZIV>medicomut,tick781',
f'cmt_dual_riziv_tick781,Dual RIZIV 41.3bn care vs corrections+tickets residual tick781,gg_belgium,dual map,Beleidsnota 1282/009,2026-08-03,2026,2026,0,"{{""ami_bn"": 41.297, ""corr_m"": 474.9, ""tickets_m"": 125, ""note"": ""not TE-additive""}}",0,active,https://www.dekamer.be/doc/FLWB/pdf/56/1282/56K1282009.pdf,Map care objective and correction instruments,L5 FOI,{src_dual},strong,Belgium>dual>riziv,tick781',
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
f"lb_riziv_ami_41_3bn_2026,RIZIV ZIV/AMI total 41.297bn 2026,L5,ops,Federal>RIZIV>AMI,41297000000,41297000000,Strong care objective +1.566bn; dual benefits 41.297,strong,{src},patients,see,primary Kamer,3.0,9.5,5.0,6.25,Programme FOI,active,,tick781",
f"lb_riziv_corr_drugs_228m_2026,RIZIV pharma correction 227.9m 2026,L5,ops,Federal>RIZIV>drugs,227900000,227900000,Strong multi-year pharma framework share; waste-reduction claim,strong,{src},pharma,see,primary Kamer,5.0,7.5,4.0,5.85,Drug FOI,active,,tick781",
f"lb_riziv_corr_doctors_150m_2026,RIZIV doctors correction 150m 2026,L5,ops,Federal>RIZIV>doctors,150000000,150000000,Strong imaging surgery labs efficiency package,strong,{src},doctors,see,primary Kamer,4.5,7.0,4.0,5.45,Provider FOI,active,,tick781",
f"lb_riziv_tickets_125m_2026,Tickets moderators +125m reinvest 2026,L5,transfer,Federal>RIZIV>tickets,125000000,125000000,Strong co-pay up fully recycled to care staff; access dual,strong,{src},patients,see,primary Kamer,5.5,7.0,3.5,5.85,Access FOI,active,,tick781",
f"lb_riziv_effic_684m_2029,RIZIV efficiency path peak 684m 2029,L5,ops,Federal>RIZIV>efficiency,684000000,684000000,Strong multi-year structural efficiency within growth norm,strong,{src},care system,see,primary Kamer,4.0,7.5,4.0,5.55,Multi-year FOI,active,,tick781",
f"lb_riziv_medicomut_gp_21m_2026,Medicomut GP cabinets 21.1m 2026,L5,transfer,Federal>RIZIV>GP,21072000,21072000,Strong primary care practice prime of 42.5m path,strong,{src},GPs,see,primary Kamer,3.0,6.0,2.5,4.15,GP FOI,active,,tick781",
f"lb_riziv_corr_package_475m_2026,RIZIV correction package ~475m 2026,L5,ops,Federal>RIZIV>corrections,474900000,474900000,Strong drugs+doctors+dayhosp+other dual official 470.8m,strong,{src},providers,see,primary Kamer,4.5,7.5,3.5,5.65,Package FOI,active,,tick781",
f"lb_dual_riziv_2026,Dual RIZIV 41.3bn vs corrections+tickets map,L5,transfer,Belgium>dual>riziv,41297000000,0,Strong dual not TE-additive care objective instruments,strong,{src_dual},public,see,primary,4.5,9.0,4.0,6.15,L5 FOI,active,,tick781",
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
gap = "gap_riziv_corr_tickets_l5"
ft = foi.read_text(encoding="utf-8")
foi_row = (
    f"{gap},Federal>RIZIV>corrections_tickets_L5,riziv,"
    "Line-by-line drug correction list behind 227.9m; doctor imaging/surgery cuts behind 150m; "
    "ticket-moderator tariff schedule and protected-group exemptions behind 125m reinvest; "
    "efficiency plan 2028/2029 cash path 247/684; Medicomut GP allocation key for 21.072m; "
    "OA mutual extra 25m reconciliation,"
    "RIZIV total public; residual measure L5 and access impacts opaque,9,"
    "RIZIV / FOD Volksgezondheid FOI,,https://www.riziv.fgov.be,"
    f"docs/doge/foi/drafts/{gap}.md,ready,2026-08-03,,,,,"
    "cmt_riziv_corr_package_2026|cmt_riziv_tickets_reinvest_2026|cmt_riziv_effic_path_2028_29|cmt_dual_riziv_tick781,"
    "lb_riziv_corr_package_475m_2026|lb_riziv_tickets_125m_2026|lb_riziv_corr_drugs_228m_2026|lb_dual_riziv_2026,"
    f"{utc},{utc},tick781 Kamer 1282/009 primary; human send only"
)
if f"\n{gap}," not in ft:
    with foi.open("a", encoding="utf-8", newline="\n") as f:
        f.write(foi_row + "\n")
    print("foi +")

rq = base / "research_queue.csv"
rqt = rq.read_text(encoding="utf-8")
old = "rq_772,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual after progress@780: FOI-adjacent dual/L5 or unmined primary PDF; FAGG/OAP wave filled 771-779,,2026-08-03T16:00:00Z,,spawned tick780 after progress@780"
new = "rq_772,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,Next residual after progress@780: FOI-adjacent dual/L5 or unmined primary PDF; FAGG/OAP wave filled 771-779,,2026-08-03T16:00:00Z,2026-08-03T17:00:00Z,tick781: RIZIV beleidsnota 41.297bn corr 475 tickets 125 effic 247/684; spawn rq_773"
if old in rqt:
    rqt = rqt.replace(old, new)
else:
    rqt = rqt.replace(
        "rq_772,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
        "rq_772,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    )
if "rq_773," not in rqt:
    rqt = rqt.rstrip("\n") + "\n" + "rq_773,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Next residual: dual L5 or unmined primary (local/regional/CoA); RIZIV measures filled tick781,,2026-08-03T17:00:00Z,,spawned tick781 after rq_772\n"
rq.write_text(rqt, encoding="utf-8", newline="\n")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_772,781,no,"
    "tick781 RIZIV 41.297bn corr 475 tickets 125 effic 247/684 Medicomut GP 21; next rq_773 residual; progress@790 in 9; rq_116 deferred\n",
    encoding="utf-8",
    newline="\n",
)
print("done 781")
