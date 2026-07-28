# tick539 — Kamer exposé federal primary by dept + econ + COFOG + interest
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T08:45:00Z"

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_primary_dept_2026,Kamer expose 2026 federal primary exp by department Tables1-5 + econ Table6 + COFOG Table7,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part III Ch3,2026-07-29,primary_budget,"
        "Strong tick539: VEK primary 99.656bn VLK 90.949bn 2026; Defence VEK 20.1bn vs VLK 10.8bn dual; SS 30.7bn; "
        "econ class SS transfers 26.53bn C&R 17.95bn; COFOG gen admin 41.2 social 24.2 defence 10.9; "
        "provisions 2.128bn L5; interest fed 12.343bn 2026; raw kamer_56k1278_001_expose_2026.pdf\n"
    )
    f.write(
        "src_dual_fed_primary_vek_vlk_tick539,Dual federal primary engagement 99.7bn vs liquidation 90.9bn + Defence 20.1/10.8,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis exposé Tables3-4+7,2026-07-29,synthesis,"
        "Strong dual: VEK-VLK gap 8.7bn federal primary; Defence alone ~9.3bn commit backlog; not ESA TE; tick539\n"
    )

buds = [
    "bud_fed_primary_vek_2026,sec_federal,2026,99656200000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Expose Table3 VEK primary credits 99656.2m 2026 (+6.5pct vs adj 93548.9); tick539",
    "bud_fed_primary_vlk_2026,sec_federal,2026,90949000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Expose Table4/6 VLK primary 90948.6-90949m 2026 (-0.9pct vs adj 91773.9); tick539",
    "bud_fed_primary_vek_adj_2025,sec_federal,2025,93854700000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table1 VEK adj 2025 93854.7m; tick539",
    "bud_fed_primary_vlk_adj_2025,sec_federal,2025,91773900000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table2 VLK adj 2025 91773.9m; tick539",
    "bud_fed_defence_vek_2026,mod_defensie,2026,20112200000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table3 Defence VEK 20112.2m 2026 (+56.5pct / +7262.9m vs 12849.4 adj); tick539",
    "bud_fed_defence_vlk_2026,mod_defensie,2026,10769600000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Defence VLK 10769.6m 2026 (+3.3pct / +341.7m vs 10427.9); dual VEK gap; tick539",
    "bud_fed_ss_dept_vlk_2026,sec_ss,2026,30723500000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table3/4 Social Security dept credits 30723.5m 2026 (-322.6m / -1.0pct); tick539",
    "bud_fed_dotaties_2026,sec_federal,2026,17743600000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table3/4 Dotaties 17743.6m 2026 (+1.3pct); communities class 17273m +229m narrative; tick539",
    "bud_fed_mobility_vlk_2026,nmbs,2026,4704100000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Mobility VLK 4704.1m 2026 (-165.8m); narrative NMBS-driven -171m; tick539",
    "bud_fed_police_vlk_2026,sec_federal,2026,2892900000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Federal police VLK 2892.9m 2026; tick539",
    "bud_fed_justice_vlk_2026,sec_federal,2026,2843700000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Justice VLK 2843.7m 2026; tick539",
    "bud_fed_mi_vlk_2026,sec_federal,2026,2409200000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Social Integration VLK 2409.2m 2026 (+12.9pct); leefloon OCMW +312m narrative; tick539",
    "bud_fed_interior_vlk_2026,sec_federal,2026,2297700000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Interior VLK 2297.7m 2026 (-4.4pct); tick539",
    "bud_fed_finance_vlk_2026,fod_finance,2026,2384300000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Finance VLK 2384.3m 2026 (-3006.5m); IMF capital 2.945bn 2025 exceptional removed; tick539",
    "bud_fed_imf_capital_2025,fod_finance,2025,2945000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Exceptional 2025 IMF quota capital increase 2.945bn in Finance credits; tick539",
    "bud_fed_economy_vlk_2026,sec_federal,2026,1444300000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Economy VLK 1444.3m 2026 (+38.1pct); energy norm +249m narrative; tick539",
    "bud_fed_foreign_vlk_2026,sec_federal,2026,1606000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table4 Foreign+Devcoop VLK 1606.0m 2026 (-5.3pct); devcoop -95m narrative; tick539",
    "bud_fed_bni_eu_2026,sec_federal,2026,4994400000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table3/4 BNI contribution EU 4994.4m 2026 (+30.2pct / +1159.3m); tick539",
    "bud_fed_provisions_vlk_2026,sec_federal,2026,2128000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table5 total provisions VLK 2128.0m 2026; tick539",
    "bud_fed_prov_interdept_829_7m_2026,sec_federal,2026,829700000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table5 interdept provision 829.7m = justice divers 618.3 + bpost 78 + Fedasil 100 + vulnerable 33.5; tick539",
    "bud_fed_prov_ukraine_442_8m_2026,sec_federal,2026,442800000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table5 Ukraine provision 442.8m = 65-wet 298.8 + macro 24 + EPF 120; tick539",
    "bud_fed_prov_security_366_9m_2026,sec_federal,2026,366900000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table5 security provision 366.9m = security/return 250 + prison 60 + Justice transfer 6.2 + Just/Interior 50.7; tick539",
    "bud_fed_prov_index_485_2m_2026,sec_federal,2026,485200000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table5 indexation provision 485.2m 2026; tick539",
    "bud_fed_econ_ss_transfers_26530m_2026,sec_ss,2026,26530000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 econ VLK transfers to SS 26530m 29.2pct of primary; tick539",
    "bud_fed_econ_cr_transfers_17948m_2026,sec_federal,2026,17948000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 transfers Regions/Communities 17948m 19.7pct; tick539",
    "bud_fed_econ_wages_8322m_2026,sec_federal,2026,8322000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 wages+SSC 8322m 9.1pct; tick539",
    "bud_fed_econ_foreign_6603m_2026,sec_federal,2026,6603000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 foreign transfers 6603m 7.3pct; tick539",
    "bud_fed_econ_autonomous_5943m_2026,sec_federal,2026,5943000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 autonomous institutions 5943m 6.5pct; tick539",
    "bud_fed_econ_ops_5235m_2026,sec_federal,2026,5235000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 operating costs 5235m 5.8pct; tick539",
    "bud_fed_econ_hh_asbl_5105m_2026,sec_federal,2026,5105000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 households+ASBL 5105m 5.6pct; tick539",
    "bud_fed_econ_invest_4962m_2026,sec_federal,2026,4962000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 investments incl military 4962m 5.5pct; tick539",
    "bud_fed_econ_local_4056m_2026,sec_federal,2026,4056000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 local gov transfers 4056m 4.5pct; tick539",
    "bud_fed_econ_companies_3233m_2026,sec_federal,2026,3233000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table6 company transfers 3233m 3.6pct; tick539",
    "bud_fed_cofog_genadmin_41169m_2026,sec_federal,2026,41169000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 COFOG general public services 41169m 45.3pct VLK; tick539",
    "bud_fed_cofog_social_24176m_2026,sec_federal,2026,24176000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 COFOG social protection 24176m 26.6pct; tick539",
    "bud_fed_cofog_defence_10879m_2026,mod_defensie,2026,10879000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 COFOG defence 10879m 12.0pct aligns VLK; tick539",
    "bud_fed_cofog_order_6443m_2026,sec_federal,2026,6443000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 public order security 6443m 7.1pct; tick539",
    "bud_fed_cofog_econ_6418m_2026,sec_federal,2026,6418000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 economic affairs 6418m 7.1pct; tick539",
    "bud_fed_cofog_health_1113m_2026,sec_federal,2026,1113000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Table7 health 1113m 1.2pct; tick539",
    "bud_fed_interest_2025,sec_federal,2025,10944000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Fed interest 2025 10944m = Treasury ESR 10760 + consol 60 + FPS Fin 124; 1.7pct GDP; tick539",
    "bud_fed_interest_2026,sec_federal,2026,12343000000,,,budgeted,src_kamer_expose_primary_dept_2026,strong,Fed interest 2026 est 12343m (+1399m vs 2025); dual vs E1 interest 12.17bn Table3; tick539",
    "bud_dual_fed_primary_vek_vlk_gap,sec_federal,2026,8707000000,,,derived,src_dual_fed_primary_vek_vlk_tick539,strong,Dual VEK-VLK primary gap ~8.707bn (99.656-90.949); not cash waste; multi-year commit backlog; tick539",
    "bud_dual_defence_vek_vlk_gap_2026,mod_defensie,2026,9342600000,,,derived,src_dual_fed_primary_vek_vlk_tick539,strong,Dual Defence VEK 20.112 - VLK 10.770 = 9.343bn commit backlog 2026; LPM path; tick539",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_fed_primary_dept_2026,Federal primary exp dual VEK/VLK by department 2026,sec_federal,Federal departments Entity I,"
        "Kamer expose DOC 56 1278/001 Tables1-4,2026-01-28,2025,2026,99656200000,"
        '"{""vek_2026_m"":99656.2,""vlk_2026_m"":90948.6,""vek_adj_2025_m"":93854.7,""vlk_adj_2025_m"":91773.9,'
        '""defence_vek_m"":20112.2,""defence_vlk_m"":10769.6,""ss_dept_m"":30723.5,""dotaties_m"":17743.6,'
        '""bni_eu_m"":4994.4,""provisions_m"":2128.0,""note"":""Strong; VEK+6.5pct VLK-0.9pct; IMF 2.945bn base effect Finance""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map federal primary spend dual commitment liquidation,"
        "Publish VEK multi-year cash path,src_kamer_expose_primary_dept_2026,strong,Federal>Primary_exp>dept_2026,tick539"
    ),
    (
        "cmt_fed_econ_class_vlk_2026,Federal primary economic classification VLK 2026,sec_federal,SS C&R households companies,"
        "Expose Table6 economic nature,2026-01-28,2026,2026,90949000000,"
        '"{""ss_transfers_m"":26530,""cr_transfers_m"":17948,""wages_m"":8322,""foreign_m"":6603,""autonomous_m"":5943,'
        '""ops_m"":5235,""hh_asbl_m"":5105,""invest_m"":4962,""local_m"":4056,""companies_m"":3233,""provisions_m"":2128,'
        '""divers_m"":776,""financial_m"":108,""total_m"":90949}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Economic nature of federal primary,"
        "L5 under SS transfers FOI,src_kamer_expose_primary_dept_2026,strong,Federal>Primary_exp>econ_class_2026,tick539"
    ),
    (
        "cmt_fed_cofog_vlk_2026,Federal primary COFOG functional VLK 2026,sec_federal,Taxpayers multi-function,"
        "Expose Table7 COFOG98,2026-01-28,2026,2026,90949000000,"
        '"{""genadmin_m"":41169,""social_m"":24176,""defence_m"":10879,""order_m"":6443,""econ_m"":6418,'
        '""health_m"":1113,""other_m"":752,""total_m"":90949,""note"":""Gen admin 45.3pct dominates via transfers""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Functional map federal spend,"
        "Dual dept vs function FOI,src_kamer_expose_primary_dept_2026,strong,Federal>Primary_exp>cofog_2026,tick539"
    ),
    (
        "cmt_fed_interest_path_2025_26,Federal power interest charges 2025-2026,sec_federal,Bondholders,"
        "Expose Part III Afdeling2 interest,2026-01-28,2025,2026,12343000000,"
        '"{""2025_m"":10944,""2026_m"":12343,""delta_m"":1399,""treasury_esr_2025_m"":10760,""consol_2025_m"":60,'
        '""fps_fin_2025_m"":124,""pct_gdp_2025"":1.7,""note"":""Dual vs E1 interest 12.17bn and GG 14.3bn""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Service federal debt,"
        "Primary surplus path,src_kamer_expose_primary_dept_2026,strong,Federal>Debt>interest_2026,tick539"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_fed_primary_vek_99_7bn,Federal primary VEK 99.7bn 2026,federal,ops,Federal>Primary_exp>VEK_2026,99656200000,99656200000,Strong exposé: engagement credits 99.7bn vs VLK 90.9bn dual backlog 8.7bn,strong,src_kamer_expose_primary_dept_2026,Federal depts,Commitment-based primary,Core federal mass,3.0,9.5,5,6.45,Dual VLK FOI,seed,,tick539",
    "lb_fed_primary_vlk_90_9bn,Federal primary VLK 90.9bn 2026,federal,ops,Federal>Primary_exp>VLK_2026,90949000000,90949000000,Strong: liquidation primary -0.9pct YoY; IMF base effect; near CoA cells 92bn dual,strong,src_kamer_expose_primary_dept_2026,Federal depts,Cash-like primary,Core federal mass,2.5,9.5,5,6.35,Map vs CoA cells,seed,,tick539",
    "lb_defence_vek_20_1bn,Defence VEK 20.1bn dual VLK 10.8bn 2026,federal,ops,Federal>Defence>VEK_2026,20112200000,20112200000,Strong dual: +56.5pct engagement surge; VLK only +3.3pct; ~9.3bn backlog; LPM path,strong,src_dual_fed_primary_vek_vlk_tick539,Defence,NATO capability rebuild,Hard dual commit cash,7.0,9.0,6,7.5,Multi-year cash FOI,seed,,tick539",
    "lb_fed_ss_dept_30_7bn,Social Security dept credits 30.7bn 2026,federal,ops,Federal>SS>dept_credits_2026,30723500000,30723500000,Strong Table3/4: -1.0pct; evenwichtsdotaties -1122m FPD +531m handicap +194m,strong,src_kamer_expose_primary_dept_2026,SS beneficiaries,Balance financing SS,Bulk federal social,3.0,9.5,6,6.55,L5 evenwicht FOI,seed,,tick539",
    "lb_fed_econ_ss_transfers_26_5bn,Econ class SS transfers 26.53bn 2026,federal,ops,Federal>Primary_exp>econ>SS_transfers,26530000000,26530000000,Strong Table6: 29.2pct of federal primary VLK is SS transfers,strong,src_kamer_expose_primary_dept_2026,SS systems,Fund SS global management,Dual Graph1 54.3bn path,4.0,9.5,5,6.85,Perimeter FOI,seed,,tick539",
    "lb_fed_cofog_genadmin_41_2bn,COFOG general services 41.2bn 45pct,federal,ops,Federal>Primary_exp>cofog>genadmin,41169000000,41169000000,Strong Table7: gen admin 45.3pct dominates via intergov transfers not ops,strong,src_kamer_expose_primary_dept_2026,Multi-level gov,General services COFOG,Transfer-heavy structure,5.5,9.5,5,7.15,Cut transfers not clerks,seed,,tick539",
    "lb_fed_interest_12_3bn,Federal interest 12.3bn 2026,federal,ops,Federal>Debt>interest_2026,12343000000,12343000000,Strong: +1.4bn YoY to 12.343bn; dual E1 12.17 GG 14.3; not waste cut past deficits,strong,src_kamer_expose_primary_dept_2026,Bondholders,Debt service,Snowball risk,4.0,9.0,7,6.4,Primary surplus path,seed,,tick539",
    "lb_fed_provisions_2_1bn,Federal provisions 2.128bn L5 2026,federal,ops,Federal>Primary_exp>provisions_2026,2128000000,2128000000,Strong Table5: interdept 829.7 Ukraine 442.8 security 366.9 index 485.2,strong,src_kamer_expose_primary_dept_2026,Multiple programmes,Contingency packages,Opacity until sectioned,6.0,8.0,4,6.6,Move to sections CoA,seed,,tick539",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_fed_defence_vek_vlk_l5,Federal>Defence>VEK_VLK_dual_L5,mod_defensie,"
        "Multi-year cash schedule reconciling Defence VEK 20.112bn vs VLK 10.770bn 2026 and LPM commitment backlog; "
        "BGD article codes; outturn path 2025-2029,"
        "Dual ~9.3bn engage-liquidate gap is material; LPM transparency,7,"
        "FOD Defensie / BOSA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_fed_defence_vek_vlk_l5.md,ready,2026-07-29,,,,,,"
        "cmt_fed_primary_dept_2026|lb_defence_vek_20_1bn,2026-07-29T08:45:00Z,2026-07-29T08:45:00Z,"
        "tick539 human send; not sent\n"
    )

# research_queue
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_530,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_530,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick538 after exposé Graph1 dual; progress@540 soon; rq_116 deferred",
    "tick539: exposé primary dept+econ+COFOG+interest; spawn rq_531; progress@540 next; rq_116 deferred",
    1,
)
if "rq_531," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_531,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T08:45:00Z,,Spawned tick539 after primary dept Tables1-7; progress@540 next tick; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_530,539,no,"
    "Tick539 exposé primary dept VEK 99.7bn VLK 90.9bn Defence dual 20.1/10.8; "
    "COFOG gen 41.2 social 24.2; interest 12.3bn; next prio5 rq_531; progress@540; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick539")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))
