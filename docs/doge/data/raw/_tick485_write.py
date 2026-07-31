# tick485 write script
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_bru_trajectory_2026_29,CoA BCR Table1 SEC trajectory measures 2026-2029 dual VL/WAL,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_17_BudgetsRBC2026.pdf,"
        "Cour des comptes Budgets RBC 2026,2026-08-03,court_of_audit,"
        "Strong: base -1241; measures 297/565/907/1186 (dep+rec); SEC after -957/-719/-416/0; "
        "personnel 84-274 fonct 127-281 facult 25; mobility reinvest -190 to -37; recettes detail FOI; tick485\n"
    )
    f.write(
        "src_dual_vl_wal_bru_consolidation_tick485,Dual triad VL measures + WAL economies + BRU SEC path measures 2026,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_17_BudgetsRBC2026.pdf,"
        "DOGE synthesis primary VL+WAL+CoA BRU,2026-08-03,synthesis,"
        "Strong dual triad different perimeter: VL 1.832bn + WAL 270m + BRU total measures 297m 2026; "
        "BRU dep-side 177 + rec 120; tick485\n"
    )

buds = [
    "bud_bru_sec_base_2025,brussels_gov,2025,-1241000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU SEC base de depart -1.241bn 2025 (provisions used); CoA Table1; tick485",
    "bud_bru_measures_total_2026,brussels_gov,2026,297000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU new measures dep+rec 297m 2026 path to 1.186bn 2029; tick485",
    "bud_bru_measures_total_2027,brussels_gov,2027,565000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU new measures 565m 2027 (dep 302+rec 263); tick485",
    "bud_bru_measures_total_2028,brussels_gov,2028,907000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU new measures 907m 2028 (dep 607+rec 300); tick485",
    "bud_bru_measures_total_2029,brussels_gov,2029,1186000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU new measures 1.186bn 2029 (dep 845+rec 341) to SEC 0; tick485",
    "bud_bru_measures_dep_2026,brussels_gov,2026,177000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU dep-side measures 177m 2026; tick485",
    "bud_bru_measures_rec_2026,brussels_gov,2026,120000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU recettes-side measures 120m 2026 (detail L5 FOI); tick485",
    "bud_bru_sec_after_2026,brussels_gov,2026,-957000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU SEC after measures -957m 2026 (class matches SGRBC -956.6m); tick485",
    "bud_bru_sec_after_2029,brussels_gov,2029,0,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU SEC balance 0 target 2029 after measures; tick485",
    "bud_bru_personnel_measures_2026,brussels_gov,2026,84000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU personnel effort 84m 2026 path 163/220/274; tick485",
    "bud_bru_personnel_measures_2029,brussels_gov,2029,274000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU personnel effort 274m 2029; tick485",
    "bud_bru_fonct_it_measures_2026,brussels_gov,2026,127000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU fonct+IT effort 127m 2026 path 166/241/281; tick485",
    "bud_bru_facultatives_measures_2026,brussels_gov,2026,25000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU facultative subsidies cut 25m/yr flat 2026-29; tick485",
    "bud_bru_mobilite_reinvest_2026,brussels_gov,2026,-190000000,,,budgeted,src_ccrek_bru_trajectory_2026_29,strong,BRU mobilite net negative measure -190m 2026 (reinvest) path -209/-129/-37; tick485",
    "bud_dual_triad_consol_class_2026,gg_belgium,2026,2399000000,,,derived,src_dual_vl_wal_bru_consolidation_tick485,strong,Dual triad class VL1.832+WAL0.270+BRU0.297=2.399bn 2026 different perimeter not additive TE; tick485",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in buds:
        f.write(r + "\n")

cmt1 = (
    "cmt_bru_sec_trajectory_measures_2026_29,BRU SEC path new measures multi-year 297m to 1.186bn,"
    "brussels_gov,Regional services OAA households firms,"
    "Expose general + CoA Budgets RBC 2026 Table1,2026-03-13,2026,2029,1186000000,"
    '"{""2026"":297000000,""2027"":565000000,""2028"":907000000,""2029"":1186000000,'
    '""dep_path"":[177000000,302000000,607000000,845000000],'
    '""rec_path"":[120000000,263000000,300000000,341000000],'
    '""sec_after"":[-957000000,-719000000,-416000000,0],'
    '""base_2025"":-1241000000,'
    '""personnel_path"":[84000000,163000000,220000000,274000000],'
    '""fonct_it_path"":[127000000,166000000,241000000,281000000],'
    '""facultatives_flat"":25000000,'
    '""mobilite_path"":[-190000000,-209000000,-129000000,-37000000],'
    '""logement_path"":[52000000,15000000,15000000,15000000],'
    '""travail_eco_path"":[30000000,45000000,55000000,65000000],'
    '""env_proprete_path"":[34000000,25000000,57000000,57000000],'
    '""urbanisme_path"":[18000000,82000000,99000000,123000000],'
    '""finops_code8_max"":1000000000,'
    '""note"":""80pct exp mastery 20pct receipts mix DPR; recettes L5 and programme matrix 2027-29 thin CoA""}",'
    "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_17_BudgetsRBC2026.pdf,"
    "Return BCR to SEC balance 2029,Publish recettes L5 + programme matrix FOI,"
    "src_ccrek_bru_trajectory_2026_29,strong,Bruxelles>begroting>trajectoire_SEC_2026_29,tick485 dual triad"
)
cmt2 = (
    "cmt_dual_vl_wal_bru_consolidation_2026,Dual triad VL+WAL+BRU consolidation measures class 2026,"
    "gg_belgium,Entity II regions,"
    "VL centenboekje + WAL press + CoA BCR Table1,2025-01-01,2026,2026,2399000000,"
    '"{""vl_measures_2026"":1832000000,""wal_economies_2026"":270000000,'
    '""bru_measures_2026"":297000000,""sum_class"":2399000000,'
    '""bru_path_2029"":1186000000,'
    '""note"":""not additive TE; different perimeter methodology; FWB still residual; dual Entity II map""}",'
    "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_17_BudgetsRBC2026.pdf,"
    "Regional dual fiscal consolidation transparency Entity II,Publish comparable HRF method all entities,"
    "src_dual_vl_wal_bru_consolidation_tick485,strong,BE>dual>consolidation_VL_WAL_BRU_2026,"
    "tick485 upgrades dual VL+WAL"
)
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt1 + "\n")
    f.write(cmt2 + "\n")

lbs = [
    "lb_bru_sec_measures_297m,BRU SEC path measures 297m 2026 to 1.186bn 2029,regional,subsidy_reform,Bruxelles>begroting>mesures_SEC,297000000,1186000000,Strong CoA Table1; dep 177 rec 120; personnel+fonct dominate; facult 25; mobilite reinvest negative; recettes L5 FOI,strong,src_ccrek_bru_trajectory_2026_29,BCR residents services,SEC balance 2029 path,Reform path dual VL/WAL; opacity recettes,3.5,8.5,5,5.9,gap_bru_mesures_recettes_l5,seed,,tick485",
    "lb_bru_personnel_effort_274m,BRU personnel effort path to 274m 2029,regional,ops,Bruxelles>personnel>moratoire,84000000,274000000,Strong path 84/163/220/274; moratoire DPR; dual VL own-gov 572m class,strong,src_ccrek_bru_trajectory_2026_29,Regional staff,Admin consolidation,Core admin reform,3.0,7.5,5,5.2,Publish FTE impact open,seed,,tick485",
    "lb_bru_fonct_it_effort_281m,BRU fonct+IT effort path to 281m 2029,regional,ops,Bruxelles>fonctionnement_IT,127000000,281000000,Strong path 127/166/241/281; dual admin IT,strong,src_ccrek_bru_trajectory_2026_29,Admin IT vendors,Operating cost cut path,Admin reform dual,3.0,7.5,5,5.2,L5 vendor FOI optional,seed,,tick485",
    "lb_dual_triad_consol_2_4bn,Dual triad VL+WAL+BRU consolidation class 2.4bn 2026,multi,programme,BE>dual>consolidation_triad_2026,2399000000,2399000000,Strong dual method different perimeter; VL1.83 WAL0.27 BRU0.30; upgrades prior 2.1bn dual,strong,src_dual_vl_wal_bru_consolidation_tick485,Entity II,Triad regional consolidation map,Method closes Entity II dual slice,3.5,9.0,5,6.1,FWB residual FOI,seed,,tick485",
    "lb_bru_facultatives_25m,BRU facultative subsidies cut 25m/yr 2026-29,regional,subsidy,Bruxelles>subsidies>facultatives,25000000,100000000,Strong CoA Table1 confirms prior path; named list FOI-class,strong,src_ccrek_bru_trajectory_2026_29,Facultative grant recipients,Discretionary grant cut,Parallel WAL facultatives,4.0,5.5,5,4.9,Named cut list FOI,seed,,tick485",
    "lb_bru_mobilite_reinvest_path,BRU mobilite reinvest negative measure path -190m 2026,regional,ops,Bruxelles>Mobilite>reinvest_path,-190000000,-565000000,Strong negative measures -190/-209/-129/-37; STIB PPI cut 964.6m separate; Metro3 recalibration,strong,src_ccrek_bru_trajectory_2026_29,STIB passengers,Mobility reinvestment inside consolidation,Not pure waste; dual De Lijn/TEC,3.0,8.0,5,5.4,Publish Metro3 cash FOI,seed,,tick485",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lbs:
        f.write(r + "\n")

foi = (
    "gap_bru_mesures_recettes_l5,Bruxelles>begroting>mesures_recettes_L5,brussels_gov,"
    "Cash-by-year L5 split of new recettes measures path 120/263/300/341m 2026-29 "
    "(tax recovery cadastral tariffs fraud) + programme-level matrix of dep measures 2027-2029 "
    "beyond CoA Table1 thematic totals,"
    "CoA flags recettes detail missing and 2027-29 measure info thin; dual VL/WAL transparency incomplete,"
    "7,SPRB Bruxelles Finances et Budget transparence,transparence@sprb.brussels,"
    "Place Saint-Lazare 2 1035 Bruxelles,docs/doge/foi/drafts/gap_bru_mesures_recettes_l5.md,"
    "ready,2026-08-03,,,,,cmt_bru_sec_trajectory_measures_2026_29,lb_bru_sec_measures_297m,"
    "2026-08-03T09:15:00Z,2026-08-03T09:15:00Z,tick485 draft ready human send; Table1 totals filled"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")

print("CSV writes OK")
