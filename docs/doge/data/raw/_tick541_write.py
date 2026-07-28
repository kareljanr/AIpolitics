# tick541 — exposé Ch4 dual federal transfers to C&R / SS / local Tables 1-5
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T09:15:00Z"

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_intergov_2026,Kamer expose 2026 Ch4 federal transfers to C&R SS local Tables1-5,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part III Ch4,2026-07-29,primary_budget,"
        "Strong tick541: federal to C&R total 76.810bn 2026 (C 50.418 R 26.392); VL community 30.769 FR 17.612; "
        "SS federal means 53.879bn (fiscal 27.325 + budget credits 26.554); local 4.257bn; "
        "dual Graph1 E2 81.5 vs C&R 76.8; tick541\n"
    )
    f.write(
        "src_dual_fed_cr_ss_local_tick541,Dual federal financing stack C&R 76.8 + SS 53.9 + local 4.3 vs Graph1,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis exposé Ch4 Tables1-5,2026-07-29,synthesis,"
        "Strong dual: C&R 76.8 != Graph1 E2 81.5; SS 53.9 aligns Graph1 54.3; local separate 4.3; tick541\n"
    )

buds = [
    # Table 1 grand
    "bud_fed_to_cr_total_2026,sec_federal,2026,76810100000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table1 federal means to C&R total 76810.1m 2026 (receipts 59433.7 + budget credits 17376.4); tick541",
    "bud_fed_to_cr_total_2025,sec_federal,2025,75533700000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table1 federal to C&R 75533.7m 2025; tick541",
    "bud_fed_to_cr_total_2024,sec_federal,2024,73205700000,,,outturn,src_kamer_expose_intergov_2026,strong,Table1 federal to C&R 73205.7m 2024; tick541",
    "bud_fed_to_communities_2026,sec_federal,2026,50418400000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table1 communities total 50418.4m 2026 (shared tax 33563.2 + credits 16855.2); tick541",
    "bud_fed_to_regions_2026,sec_federal,2026,26391700000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table1 regions total 26391.7m 2026 (fiscal 25870.5 + credits 521.2); tick541",
    "bud_fed_to_communities_receipts_2026,sec_federal,2026,33563200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Communities shared-tax receipts 33563.2m 2026; tick541",
    "bud_fed_to_communities_credits_2026,sec_federal,2026,16855200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Communities budget credits 16855.2m 2026 (family 9170 eldercare 5677 etc); tick541",
    # Communities by entity Table 2
    "bud_fed_to_vl_community_2026,sec_flanders,2026,30768500000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 VL Community total means 30768.5m 2026; tick541",
    "bud_fed_to_fr_community_2026,fwb_gov,2026,17611600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 FR Community total 17611.6m 2026; tick541",
    "bud_fed_to_dg_community_2026,sec_dg,2026,345000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 DG Community total 345.0m 2026; tick541",
    "bud_fed_to_ggc_2026,brussels_gov,2026,1576100000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 GGC/COCOM total 1576.1m 2026 (budget credits); tick541",
    "bud_fed_comm_btw_2026,sec_federal,2026,22503600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 communities VAT shared 22503.6m 2026; tick541",
    "bud_fed_comm_pb_2026,sec_federal,2026,10942300000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 communities PB/IPP shared 10942.3m 2026; tick541",
    "bud_fed_comm_family_benefits_2026,sec_federal,2026,9170000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 family benefits credits total 9170.0m 2026; tick541",
    "bud_fed_comm_eldercare_2026,sec_federal,2026,5676600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 eldercare credits total 5676.6m 2026; tick541",
    "bud_fed_comm_health_aid_2026,sec_federal,2026,1184500000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 health+personal aid credits 1184.5m 2026; tick541",
    "bud_fed_comm_hospitals_2026,sec_federal,2026,400700000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 hospital infra credits 400.7m 2026; tick541",
    "bud_fed_comm_justitiehuizen_2026,sec_federal,2026,147000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table2 justice houses credits 147.0m 2026; tick541",
    # Regions Table 3
    "bud_fed_to_vl_region_2026,sec_flanders,2026,12729200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 VL Region total ~12729.2m 2026 (fiscal 12665.3 + credits 63.9); tick541",
    "bud_fed_to_wal_region_2026,wallonie_gov,2026,9257000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 WAL Region total ~9257.0m 2026 (fiscal 9238.2 + credits 18.8); tick541",
    "bud_fed_to_bru_region_2026,brussels_gov,2026,4405400000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 BRU Region total ~4405.4m 2026 (fiscal 3966.9 + credits 438.5 heavy); tick541",
    "bud_fed_bru_mobility_dot_2026,brussels_gov,2026,195200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 BRU mobility dotation 195.2m 2026; tick541",
    "bud_fed_bru_invest_dot_2026,brussels_gov,2026,68400000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 BRU investments credit 68.4m 2026; tick541",
    "bud_fed_bru_city_dot_2026,brussels_gov,2026,145600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 Ville de Bruxelles credit 145.6m 2026; tick541",
    "bud_fed_region_add_pb_2026,sec_federal,2026,14466600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table3 regional additional PB tax 14466.6m 2026; tick541",
    # SS Table 4
    "bud_fed_to_ss_total_2026,sec_ss,2026,53878900000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 federal means to SS total 53878.9m 2026 (credits 26553.9 + fiscal 27325.0); dual Graph1 54.3; tick541",
    "bud_fed_to_ss_total_2025,sec_ss,2025,53978000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 federal to SS 53978.0m 2025; tick541",
    "bud_fed_to_ss_total_2024,sec_ss,2024,50540700000,,,outturn,src_kamer_expose_intergov_2026,strong,Table4 federal to SS 50540.7m 2024; tick541",
    "bud_fed_ss_credits_2026,sec_ss,2026,26553900000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 SS budget credits/dotations 26553.9m 2026; tick541",
    "bud_fed_ss_fiscal_transfers_2026,sec_ss,2026,27325000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 SS fiscal transfers (alt financing) 27325.0m 2026; tick541",
    "bud_fed_ss_employees_dot_2026,sec_ss,2026,8335200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 employee normal+balance dots 8335.2m 2026; tick541",
    "bud_fed_ss_selfemp_dot_2026,sec_ss,2026,1076000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 self-employed dots 1076.0m 2026; tick541",
    "bud_fed_ss_public_pensions_2026,sec_ss,2026,16150300000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 public-sector pension dots 16150.3m 2026; tick541",
    "bud_fed_ss_dibiss_2026,sec_ss,2026,271200000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 DIBISS/ORPSS 271.2m 2026; tick541",
    "bud_fed_ss_diverse_2026,sec_ss,2026,721100000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table4 SS diverse credits 721.1m 2026; tick541",
    # Local Table 5
    "bud_fed_to_local_total_2026,sec_federal,2026,4257400000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 federal to local total 4257.4m 2026 (current 4050.1 + capital 207.3); tick541",
    "bud_fed_to_local_total_2025,sec_federal,2025,3998000000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 federal to local 3998.0m 2025; tick541",
    "bud_fed_ocmw_leefloon_2026,sec_federal,2026,2085100000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 OCMW/CPAS leefloon/RIS 2085.1m 2026 (+312m class vs prior narrative); tick541",
    "bud_fed_ocmw_refugees_2026,sec_federal,2026,155800000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 OCMW refugee reception 155.8m 2026 (down from 451.6 2024); tick541",
    "bud_fed_police_zones_dot_2026,sec_federal,2026,1270600000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 police zone dots 1270.6m 2026; tick541",
    "bud_fed_local_other_current_2026,sec_federal,2026,523400000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 other current local transfers 523.4m 2026; tick541",
    "bud_fed_local_capital_2026,sec_federal,2026,207300000,,,budgeted,src_kamer_expose_intergov_2026,strong,Table5 local capital transfers 207.3m 2026; tick541",
    # Dual
    "bud_dual_graph1_e2_vs_cr_table1,sec_federal,2026,4689000000,,,derived,src_dual_fed_cr_ss_local_tick541,medium,Dual Graph1 E2 81.5bn vs Table1 C&R 76.810bn gap ~4.7bn class perimeter/items; tick541",
    "bud_dual_graph1_ss_vs_table4,sec_ss,2026,421000000,,,derived,src_dual_fed_cr_ss_local_tick541,strong,Dual Graph1 SS federal 54.3bn vs Table4 53.879bn ~0.42bn residual; tick541",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_fed_to_cr_path_2024_26,Federal financing stack to Communities and Regions 2024-2026,sec_federal,C&R entities,"
        "Expose Ch4 Table1 special financing law path,2026-01-28,2024,2026,76810100000,"
        '"{""2024_m"":73205.7,""2025_m"":75533.7,""2026_m"":76810.1,""communities_2026_m"":50418.4,'
        '""regions_2026_m"":26391.7,""comm_receipts_2026_m"":33563.2,""comm_credits_2026_m"":16855.2,'
        '""reg_fiscal_2026_m"":25870.5,""reg_credits_2026_m"":521.2,""note"":""Strong Table1; dual Graph1 E2 81.5""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Fund federated entities via BFW,"
        "Perimeter FOI vs Graph1 81.5,src_kamer_expose_intergov_2026,strong,Federal>Intergov>C_R_2026,tick541"
    ),
    (
        "cmt_fed_to_communities_l5_2026,Federal means to communities by entity and competence 2026,sec_federal,VL FR DG GGC,"
        "Expose Table2 community breakdown,2026-01-28,2026,2026,50418400000,"
        '"{""vl_m"":30768.5,""fr_m"":17611.6,""dg_m"":345.0,""ggc_m"":1576.1,""vat_m"":22503.6,""pb_m"":10942.3,'
        '""family_m"":9170.0,""eldercare_m"":5676.6,""health_aid_m"":1184.5,""hospitals_m"":400.7,'
        '""justice_houses_m"":147.0,""note"":""Strong Table2; family+elder dominate credits""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Sixth reform competence financing,"
        "Residual sub-L5 FOI,src_kamer_expose_intergov_2026,strong,Federal>Intergov>communities_2026,tick541"
    ),
    (
        "cmt_fed_to_ss_path_2017_26,Federal financing of SS budget credits + fiscal 2017-2026,sec_ss,SS global management FPD,"
        "Expose Table4 SS federal means,2026-01-28,2017,2026,53878900000,"
        '"{""2024_m"":50540.7,""2025_m"":53978.0,""2026_m"":53878.9,""credits_2026_m"":26553.9,'
        '""fiscal_2026_m"":27325.0,""employees_2026_m"":8335.2,""selfemp_2026_m"":1076.0,'
        '""public_pensions_2026_m"":16150.3,""dibiss_2026_m"":271.2,""diverse_2026_m"":721.1,'
        '""note"":""Strong; dual Graph1 54.3; fiscal alt financing half of stack""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Fund SS post-2017 reform,"
        "Fiscal transfer L5 FOI,src_kamer_expose_intergov_2026,strong,Federal>Intergov>SS_2026,tick541"
    ),
    (
        "cmt_fed_to_local_path_2024_26,Federal transfers to local gov OCMW police 2024-2026,sec_federal,CPAS police zones,"
        "Expose Table5 local transfers,2026-01-28,2024,2026,4257400000,"
        '"{""2024_m"":3665.8,""2025_m"":3998.0,""2026_m"":4257.4,""leefloon_2026_m"":2085.1,'
        '""refugees_2026_m"":155.8,""police_2026_m"":1270.6,""other_current_2026_m"":523.4,'
        '""capital_2026_m"":207.3,""note"":""Strong Table5; leefloon surge; refugee grants fall post-peak""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Local social+police financing,"
        "Zone-level L5 FOI,src_kamer_expose_intergov_2026,strong,Federal>Intergov>local_2026,tick541"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_fed_to_cr_76_8bn,Federal to C&R stack 76.8bn 2026,federal,ops,Federal>Intergov>C_R_2026,76810100000,76810100000,Strong Table1: communities 50.4 + regions 26.4; dual Graph1 E2 81.5 gap,strong,src_kamer_expose_intergov_2026,C&R taxpayers,BFW financing,Core dual federalism,4.0,9.5,5,6.85,Perimeter FOI,seed,,tick541",
    "lb_fed_to_communities_50_4bn,Federal to communities 50.4bn 2026,federal,ops,Federal>Intergov>communities_2026,50418400000,50418400000,Strong: VL 30.8 FR 17.6 DG 0.35 GGC 1.58; family 9.17 elder 5.68,strong,src_kamer_expose_intergov_2026,Communities,Sixth reform stack,Largest intergov block,3.5,9.5,5,6.7,Entity dual FOI,seed,,tick541",
    "lb_fed_to_ss_53_9bn,Federal means to SS 53.9bn 2026,federal,ops,Federal>Intergov>SS_2026,53878900000,53878900000,Strong Table4: fiscal 27.3 + credits 26.6; dual Graph1 54.3; public pensions 16.2,strong,src_kamer_expose_intergov_2026,SS systems,Fund SS dual,Aligns Graph1,3.5,9.5,5,6.7,Fiscal L5 FOI,seed,,tick541",
    "lb_fed_ss_fiscal_27_3bn,SS alternative fiscal transfers 27.3bn 2026,federal,ops,Federal>Intergov>SS_fiscal_2026,27325000000,27325000000,Strong: half of federal-SS stack is fiscal afdrachten not section credits,strong,src_kamer_expose_intergov_2026,SS,Alt financing SS,Opacity vs dots,5.5,9.5,6,7.15,Article codes FOI,seed,,tick541",
    "lb_fed_ss_public_pensions_16_2bn,Public pension dots via SS path 16.2bn 2026,federal,ops,Federal>Intergov>SS_public_pensions,16150300000,16150300000,Strong Table4 largest single credit line to SS perimeter,strong,src_kamer_expose_intergov_2026,Public retirees,Civil service pensions,Structural,3.0,9.5,7,6.2,Dual FPD FOI,seed,,tick541",
    "lb_fed_to_local_4_3bn,Federal to local 4.26bn 2026,federal,ops,Federal>Intergov>local_2026,4257400000,4257400000,Strong Table5: leefloon 2.09 police 1.27 refugees 0.16 capital 0.21,strong,src_kamer_expose_intergov_2026,CPAS police,Local social+security,Rising leefloon,4.5,8.0,4,6.4,Zone L5 FOI,seed,,tick541",
    "lb_fed_ocmw_leefloon_2_09bn,OCMW leefloon federal 2.09bn 2026,federal,ops,Federal>Intergov>local>leefloon,2085100000,2085100000,Strong Table5: 2.085bn 2026 path up from 1.68 2024; UI time-limit dual,strong,src_kamer_expose_intergov_2026,RIS beneficiaries,Minimum income,Activation dual,5.5,8.0,5,6.65,Caseload FOI,seed,,tick541",
    "lb_dual_e2_graph1_vs_cr,Dual Graph1 E2 81.5 vs Table1 C&R 76.8,multi,ops,BE>dual>E2_vs_CR_table,76810100000,81500000000,Medium dual ~4.7bn gap Graph1 Entity II vs exposé C&R table perimeter,medium,src_dual_fed_cr_ss_local_tick541,Multi-level,Dual financing map,Perimeter opacity,6.5,9.5,5,7.55,Reconcile FOI,seed,,tick541",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_fed_e2_cr_perimeter_l5,Federal>Intergov>E2_vs_CR_perimeter_L5,sec_federal,"
        "Reconcile Graph1 Entity II transfer 81.5bn vs exposé Table1 C&R 76.810bn 2026 (~4.7bn gap): "
        "item list of inclusions/exclusions; machine-readable bridge; also SS fiscal afdrachten 27.325bn article codes,"
        "Dual perimeter opacity material for dual-federalism map and SS alt financing,7,"
        "FOD BOSA / FOD Financiën / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_fed_e2_cr_perimeter_l5.md,ready,2026-07-29,,,,,,"
        "cmt_fed_to_cr_path_2024_26|lb_dual_e2_graph1_vs_cr,2026-07-29T09:15:00Z,2026-07-29T09:15:00Z,"
        "tick541 human send; not sent\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_532,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_532,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick540 after ODA+debt+progress; next hole-fill; rq_116 deferred",
    "tick541: exposé Ch4 C&R/SS/local dual; spawn rq_533; rq_116 deferred",
    1,
)
if "rq_533," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_533,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T09:15:00Z,,Spawned tick541 after Ch4 intergov dual; next hole-fill; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_532,541,no,"
    "Tick541 exposé Ch4 dual fed to C&R 76.8bn SS 53.9bn local 4.3bn; Graph1 E2 gap FOI; "
    "next prio5 rq_533; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick541")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))
