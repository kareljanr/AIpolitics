# tick543 — exposé Part IV social protection Tables I.1-I.3 dual SS 148bn
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
now = "2026-07-29T09:45:00Z"

# amounts in source are thousand EUR -> convert to EUR integers

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_kamer_expose_ss_protection_2026,Kamer expose 2026 Part IV social protection Tables I.1-I.3,"
        "https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Kamer DOC 56 1278/001 Part IV Ch1,2026-07-29,primary_budget,"
        "Strong tick543: social protection total rec 194.673bn exp 194.514bn 2026; SS own rec 148.017bn matches Graph1; "
        "SSC 85.525bn; benefits 142.053bn (SS 135.492); healthcare 41.297; fed transfers SS 54.617 + assistance 6.563 = 61.181; "
        "alt financing VAT+RV path; tick543\n"
    )
    f.write(
        "src_dual_ss_protection_graph1_tick543,Dual social protection consol vs Graph1 SS 148 + federal 54.3,"
        "docs/doge/data/raw/kamer_56k1278_001_expose_2026.pdf,DOGE synthesis Part IV + Graph1,2026-07-29,synthesis,"
        "Strong dual: Table I.2 SS own 148.017 vs Graph1 148.0; fed transfers I.3.1 54.617 vs Graph1 54.3; tick543\n"
    )

buds = [
    # 2026 totals (from thousand EUR)
    "bud_socprot_total_rec_2026,sec_ss,2026,194672691000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 total social protection current receipts 194672.691m EUR 2026 IB; tick543",
    "bud_socprot_total_exp_2026,sec_ss,2026,194513960000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 total social protection current exp 194513.960m 2026; tick543",
    "bud_socprot_budget_result_2026,sec_ss,2026,97099000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 budgetary result +97.099m 2026 (near balance); tick543",
    "bud_socprot_benefits_2026,sec_ss,2026,142053349000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 benefits/prestaties 142053.349m 2026 (SS 135492 + assistance 6561); tick543",
    "bud_ss_benefits_2026,sec_ss,2026,135492286000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 SS benefits excl assistance 135492.286m 2026; dual E1 Table3; tick543",
    "bud_ss_own_receipts_2026,sec_ss,2026,148017196000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 SS own receipts 148017.196m 2026; dual Graph1 SS 148.0; tick543",
    "bud_ss_ssc_contrib_2026,sec_ss,2026,85525348000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 social contributions 85525.348m 2026; dual Graph1 SSC 85.5; tick543",
    "bud_ss_admin_costs_2026,sec_ss,2026,2995577000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 admin costs total protection 2995.577m 2026 (central 1242 + third-party 1754); tick543",
    "bud_ss_interregime_transfers_2026,sec_ss,2026,40092247000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2 inter-regime transfers 40092.247m 2026 (eliminated in consol total); tick543",
    # Branches benefits 2026
    "bud_ss_employees_benefits_2026,sec_ss,2026,63341987000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Employees global management benefits 63341.987m 2026; tick543",
    "bud_ss_selfemp_benefits_2026,sec_ss,2026,7012055000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Self-employed global benefits 7012.055m 2026; tick543",
    "bud_ss_healthcare_benefits_2026,sec_ss,2026,41297169000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Healthcare branch benefits 41297.169m 2026 (RIZIV care); tick543",
    "bud_ss_public_pension_benefits_2026,sec_ss,2026,22827520000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Civil service pension benefits 22827.520m 2026; tick543",
    "bud_ss_other_regimes_benefits_2026,sec_ss,2026,1013554000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Other SS regimes benefits 1013.554m 2026; tick543",
    "bud_socassist_benefits_2026,sec_ss,2026,6561063000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Social assistance benefits 6561.063m 2026; tick543",
    # 2025 for path
    "bud_socprot_total_rec_2025,sec_ss,2025,190162274000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.1 total social protection receipts 190162.274m 2025 adj; tick543",
    "bud_socprot_total_exp_2025,sec_ss,2025,191588586000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.1 total exp 191588.586m 2025; budget result -1495.844m; tick543",
    "bud_socprot_benefits_2025,sec_ss,2025,138922920000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.1 benefits 138922.920m 2025; tick543",
    "bud_ss_ssc_contrib_2025,sec_ss,2025,83159628000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.1 contributions 83159.628m 2025; tick543",
    "bud_ss_healthcare_benefits_2025,sec_ss,2025,39812150000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Healthcare benefits 39812.150m 2025; tick543",
    # Federal transfers I.3
    "bud_fed_transfers_ss_2026,sec_ss,2026,54617401000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.3.1 federal transfers to SS 54617.401m 2026; dual Graph1 54.3; tick543",
    "bud_fed_transfers_ss_2025,sec_ss,2025,54187689000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.3.1 federal to SS 54187.689m 2025; tick543",
    "bud_fed_transfers_socassist_2026,sec_ss,2026,6563248000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.3.2 social assistance transfers 6563.248m 2026; tick543",
    "bud_fed_transfers_households_total_2026,sec_federal,2026,61180649000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.3 grand total fed transfers SS+assistance 61180.649m 2026; tick543",
    "bud_fed_ss_alt_financing_2026,sec_ss,2026,27221583000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,Table I.2/I.3 alt financing 27221.583m 2026 (employees 23392 + selfemp 3829); tick543",
    "bud_fed_ss_alt_vat_employees_2026,sec_ss,2026,16989010000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.1 employees alt VAT 16989.010m 2026 (base 9344 + healthcare 7645); tick543",
    "bud_fed_ss_alt_rv_employees_2026,sec_ss,2026,6403174000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.1 employees alt withholding tax on movable 6403.174m 2026; tick543",
    "bud_fed_ss_balance_dot_2026,sec_ss,2026,6251448000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.1 evenwichtsdotatie total 6251.448m 2026 (emp 5653 + self 598); tick543",
    "bud_fed_ss_public_pension_dot_2026,sec_ss,2026,16392033000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.1 civil service pension state grant 16392.033m 2026; tick543",
    "bud_igo_2026,sec_ss,2026,1036827000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.2 IGO/GRAPA 1036.827m 2026 (incl FPD opex); tick543",
    "bud_handicap_allowance_2026,sec_ss,2026,3285541000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.2 handicap allowances 3285.541m 2026; tick543",
    "bud_leefloon_ris_2026,sec_ss,2026,2085102000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.2 leefloon/RIS 2085.102m 2026 (excl Ukraine provision); dual local Table5; tick543",
    "bud_zorgpersoneelfonds_2026,sec_ss,2026,347498000,,,budgeted,src_kamer_expose_ss_protection_2026,strong,I.3.1 Zorgpersoneelfonds/Blouses blanches 347.498m 2026; tick543",
    # Dual
    "bud_dual_ss_own_vs_graph1_2026,sec_ss,2026,148017196000,,,derived,src_dual_ss_protection_graph1_tick543,strong,Dual SS own receipts 148.017bn vs Graph1 148.0bn; tick543",
    "bud_dual_fed_ss_transfers_i3_vs_graph1,sec_ss,2026,54617401000,,,derived,src_dual_ss_protection_graph1_tick543,strong,Dual I.3.1 54.617bn vs Graph1 federal to SS 54.3bn residual ~0.3bn; tick543",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for line in buds:
        f.write(line + "\n")

cmts = [
    (
        "cmt_socprot_consol_2025_26,Social protection consolidated budgets 2025-2026 dual SS,sec_ss,Households beneficiaries,"
        "Expose Part IV Tables I.1-I.2,2026-01-28,2025,2026,194672691000,"
        '"{""rec_2025_m"":190162.3,""rec_2026_m"":194672.7,""exp_2025_m"":191588.6,""exp_2026_m"":194514.0,'
        '""result_2025_m"":-1495.8,""result_2026_m"":97.1,""benefits_2026_m"":142053.3,""ss_benefits_2026_m"":135492.3,'
        '""ssc_2026_m"":85525.3,""ss_own_2026_m"":148017.2,""healthcare_2026_m"":41297.2,""admin_2026_m"":2995.6,'
        '""note"":""Strong; amounts from thousand-EUR tables; dual Graph1 SS 148""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Map social protection stack,"
        "Branch L5 residual FOI,src_kamer_expose_ss_protection_2026,strong,SS>Protection>consol_2026,tick543"
    ),
    (
        "cmt_fed_transfers_ss_assist_2026,Federal transfers to SS and social assistance 2025-2026,sec_federal,SS + CPAS households,"
        "Expose Tables I.3.1-I.3.2,2026-01-28,2025,2026,61180649000,"
        '"{""ss_2025_m"":54187.7,""ss_2026_m"":54617.4,""assist_2025_m"":6045.7,""assist_2026_m"":6563.2,'
        '""total_2026_m"":61180.6,""alt_fin_2026_m"":27221.6,""balance_dot_2026_m"":6251.4,'
        '""public_pensions_2026_m"":16392.0,""igo_2026_m"":1036.8,""handicap_2026_m"":3285.5,'
        '""leefloon_2026_m"":2085.1,""note"":""Strong; dual Graph1 54.3; Ukraine aid outside leefloon""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Federal financing of social stack,"
        "Alt financing article FOI,src_kamer_expose_ss_protection_2026,strong,Federal>SS>transfers_I3_2026,tick543"
    ),
    (
        "cmt_ss_alt_financing_vat_rv_2026,SS alternative financing VAT and RV split 2026,sec_ss,Employees self-employed global,"
        "Expose Table I.3.1 alt financing detail,2026-01-28,2026,2026,27221583000,"
        '"{""employees_alt_m"":23392.2,""selfemp_alt_m"":3829.4,""emp_vat_m"":16989.0,""emp_vat_base_m"":9343.8,'
        '""emp_vat_health_m"":7645.2,""emp_rv_m"":6403.2,""special_ssc_m"":102.4,""self_vat_m"":2590.6,'
        '""self_rv_m"":1238.8,""note"":""Strong L4 alt financing map""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Alt fiscal financing of SS,"
        "Residual plastic/other FOI,src_kamer_expose_ss_protection_2026,strong,SS>Alt_financing>2026,tick543"
    ),
    (
        "cmt_healthcare_branch_benefits_2026,RIZIV healthcare branch benefits path 2025-2026,sec_ss,Patients providers,"
        "Expose Table I.1-I.2 healthcare column,2026-01-28,2025,2026,41297169000,"
        '"{""benefits_2025_m"":39812.2,""benefits_2026_m"":41297.2,""delta_m"":1485.0,""admin_2026_m"":1236.5,'
        '""note"":""Strong; dual prior RIZIV global ~45bn class includes more""}",'
        "0,active,https://www.dekamer.be/FLWB/PDF/56/1278/56K1278001.pdf,Healthcare benefits envelope,"
        "L5 provider FOI,src_kamer_expose_ss_protection_2026,strong,SS>Healthcare>benefits_2026,tick543"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for line in cmts:
        f.write(line + "\n")

lbs = [
    "lb_socprot_total_194_7bn,Social protection total receipts 194.7bn 2026,federal,ops,SS>Protection>total_2026,194672691000,194672691000,Strong Table I.2: exp 194.5bn near-balance +97m; dual Graph1 SS 148 own,strong,src_kamer_expose_ss_protection_2026,Households,Social protection stack,Core BE social mass,3.0,9.5,6,6.45,Branch FOI,seed,,tick543",
    "lb_ss_benefits_135_5bn,SS benefits 135.5bn 2026 excl assistance,federal,ops,SS>Benefits>2026,135492286000,135492286000,Strong: employees 63.3 health 41.3 public pensions 22.8 self 7.0 other 1.0,strong,src_kamer_expose_ss_protection_2026,Beneficiaries,Core SS prestations,Structural,3.0,9.5,7,6.2,Activation FOI,seed,,tick543",
    "lb_ss_ssc_85_5bn,Social contributions 85.5bn 2026,federal,ops,SS>SSC>2026,85525348000,85525348000,Strong dual Graph1 SSC 85.5; largest SS own receipt,strong,src_dual_ss_protection_graph1_tick543,Workers employers,Fund SS,Payroll dual,2.5,9.5,6,6.25,Base FOI,seed,,tick543",
    "lb_healthcare_benefits_41_3bn,Healthcare benefits 41.3bn 2026,federal,ops,SS>Healthcare>benefits_2026,41297169000,41297169000,Strong +1.49bn YoY; dual RIZIV global higher perimeter,strong,src_kamer_expose_ss_protection_2026,Patients,Health insurance benefits,Growth driver,4.0,9.5,6,6.75,Provider L5 FOI,seed,,tick543",
    "lb_fed_transfers_ss_54_6bn,Federal transfers to SS 54.6bn 2026,federal,ops,Federal>SS>transfers_I3_2026,54617401000,54617401000,Strong I.3.1 dual Graph1 54.3; alt 27.2 balance 6.3 pensions 16.4,strong,src_dual_ss_protection_graph1_tick543,SS systems,Federal SS stack,Dual financing,3.5,9.5,5,6.7,Article FOI,seed,,tick543",
    "lb_ss_alt_financing_27_2bn,SS alt financing VAT+RV 27.2bn 2026,federal,ops,SS>Alt_financing>2026,27221583000,27221583000,Strong: emp VAT 17.0 RV 6.4; self VAT+RV 3.8; fiscal dual not pure TE,strong,src_kamer_expose_ss_protection_2026,SS,Alt fiscal financing,Half federal-SS stack,5.0,9.5,5,7.15,Code FOI,seed,,tick543",
    "lb_socassist_6_56bn,Social assistance federal 6.56bn 2026,federal,ops,Federal>Assistance>2026,6563248000,6563248000,Strong I.3.2: handicap 3.29 leefloon 2.09 IGO 1.04; excl Ukraine provision,strong,src_kamer_expose_ss_protection_2026,Vulnerable,Min income stack,Rising leefloon,4.5,9.0,5,6.75,Caseload FOI,seed,,tick543",
    "lb_dual_socprot_graph1,Dual socprot consol vs Graph1 SS 148,multi,ops,BE>dual>socprot_Graph1,148017196000,194672691000,Strong dual: SS own 148.017=Graph1; protection total 194.7 includes inter-regime+assistance,strong,src_dual_ss_protection_graph1_tick543,Multi,Dual SS architecture,Map clarity,5.5,9.5,5,7.15,Annual FOI,seed,,tick543",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for line in lbs:
        f.write(line + "\n")

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_ss_branch_l5_detail,SS>Protection>branch_L5_detail,sec_ss,"
        "L5 split within employees global benefits 63.3bn 2026 (pensions unemployment illness family etc); "
        "reconcile healthcare 41.3bn vs RIZIV global ~45bn perimeter; third-party admin 1.75bn by organism,"
        "Branch aggregates public; L5 benefit-type and payment-channel opacity remains,6,"
        "FOD Sociale Zekerheid / RIZIV / RVA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_ss_branch_l5_detail.md,ready,2026-07-29,,,,,,"
        "cmt_socprot_consol_2025_26|lb_ss_benefits_135_5bn,2026-07-29T09:45:00Z,2026-07-29T09:45:00Z,"
        "tick543 human send; not sent\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
text = text.replace(
    "rq_534,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,",
    "rq_534,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,",
    1,
)
text = text.replace(
    "Spawned tick542 after EU+consol dual; next Part IV SS systems or residual; rq_116 deferred",
    "tick543: Part IV socprot Tables I.1-I.3 dual; spawn rq_535; rq_116 deferred",
    1,
)
if "rq_535," not in text:
    text = text.rstrip("\n") + "\n"
    text += (
        "rq_535,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        "2026-07-29T09:45:00Z,,Spawned tick543 after Part IV socprot; next RIZIV/employees detail or new public hole; rq_116 deferred\n"
    )
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_534,543,no,"
    "Tick543 Part IV socprot 194.7bn benefits 142 SS own 148 SSC 85.5 fed transfers 61.2; "
    "next prio5 rq_535; rq_116 SWA deferred.\n",
    encoding="utf-8",
)

print("OK tick543")
print("sources +2 budgets +", len(buds), "cmt +", len(cmts), "lb +", len(lbs))
