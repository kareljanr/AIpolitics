# tick508 — CoA 2026_22 residual POD MI + SS receipts/spend dual prior SS
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ccrek_fed_aju_ss_podmi_2026,CoA fed budget aju 2026 SS + POD MI residual 2026_22,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Rekenhof AG 21 May 2026,2026-07-28,court_of_audit,"
        "Strong residual tick508: SS rec 148002 exp 148027; OCMW 2309; integ save slip to 13.1 not deliverable; "
        "healthcare 43857; unemp 4836; dual prior SS; tick508\n"
    )
    f.write(
        "src_dual_ss_podmi_aju_tick508,Dual SS macro BC + POD MI integration savings slip,"
        "https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "DOGE synthesis CoA 2026_22 residual SS/POD MI,2026-07-28,synthesis,"
        "Strong dual: SS near-balance 148bn + soft OCMW savings 13m will not land 2026; tick508\n"
    )

buds = [
    "bud_ss_rec_bc_2026,sec_ss,2026,148002400000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS consolidated receipts BC2026 148002.4m (-14.8 vs IB); tick508",
    "bud_ss_exp_bc_2026,sec_ss,2026,148026600000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS consolidated expenditure BC2026 148026.6m (+168.1 vs IB); tick508",
    "bud_ss_contrib_bc_2026,sec_ss,2026,85328000000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS contributions BC 85328m (-197.3); tick508",
    "bud_ss_gov_transfer_bc_2026,sec_ss,2026,27443800000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS government transfers BC 27443.8m (-234.9); tick508",
    "bud_ss_altfin_bc_2026,sec_ss,2026,27583400000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS alternative financing BC 27583.4m (+361.8; BTW 19634.7 RV 7948.7); tick508",
    "bud_ss_benefits_bc_2026,sec_ss,2026,137624300000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS social benefits BC 137624.3m (+2132); tick508",
    "bud_ss_healthcare_bc_2026,sec_ss,2026,43857400000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,RIZIV healthcare benefits BC 43857.4m (+2560.2 vs IB); tick508",
    "bud_ss_unemp_bc_2026,sec_ss,2026,4836400000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Unemployment benefits employee GB BC 4836.4m (+198.5); tick508",
    "bud_ss_pens_employee_bc_2026,sec_ss,2026,43036600000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Employee pensions BC 43036.6m; tick508",
    "bud_ss_invalidity_employee_bc_2026,sec_ss,2026,14839400000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Employee invalidity BC 14839.4m; tick508",
    "bud_ss_public_pens_bc_2026,sec_ss,2026,22526800000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Public sector pensions BC 22526.8m; tick508",
    "bud_ss_admin_bc_2026,sec_ss,2026,3006800000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,SS management+payment costs BC 3006.8m; tick508",
    "bud_rsz_contrib_bc_2026,sec_ss,2026,69474700000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,RSZ Globaal Beheer contributions 69474.7m BC (-116.8); tick508",
    "bud_rsz_contrib_reductions_bc_2026,sec_ss,2026,5142500000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Federal SS contribution reductions total class 5142.5m (struct 4294.1 + targeted exp 848.4); tick508",
    "bud_rsz_workbonus_bc_2026,sec_ss,2026,1827300000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Workbonus contribution reduction 1827.3m BC; tick508",
    "bud_rsz_struct_reductions_bc_2026,sec_ss,2026,2419500000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Structural employer contribution reductions 2419.5m BC; tick508",
    "bud_rsz_wage_ceiling_exemp_58m,sec_ss,2026,58200000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Employer contribution exemption above 85k/quarter 58.2m BC; tick508",
    "bud_rsz_gov_dot_bc_2026,sec_ss,2026,8656100000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,RSZ government dots 8656.1m BC (-195; equilibrium -207.3); tick508",
    "bud_rsz_eq_overfin_2025,sec_ss,2025,547500000,,,outturn,src_ccrek_fed_aju_ss_podmi_2026,strong,Equilibrium dot overfinance 2025 547.5m booked as 2026 GB expenditure; tick508",
    "bud_zuidertoren_renov_177m,sec_ss,2031,177700000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Zuidertoren renovation 177.7m 2026-31 of which 168.8 from RSZ reserves; 2026 study 2.5m; tick508",
    "bud_podmi_ocmw_total_bc_2026,sec_federal,2026,2309000000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,OCMW RMI+wet65 total BC 2309m (RMI 2133 wet65 176); tick508",
    "bud_podmi_rmi_bc_2026,sec_federal,2026,2133000000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,RMI OCMW grants BC 2133m; tick508",
    "bud_podmi_wet65_bc_2026,sec_federal,2026,176000000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Wet 65 social assistance OCMW BC 176m; tick508",
    "bud_podmi_integ_wait_save_bc_2026,sec_federal,2026,13100000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,medium,Integration amount +5y wait savings BC only 13.1m (was 40.2 IB); CoA: will not be achieved 2026; tick508",
    "bud_riziv_save_miss_183m_2026,sec_ss,2026,183100000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,RIZIV of 801.4m savings package 183.1m not realized 2026 (145.7 drugs); tick508",
    "bud_invalidity_followup_save_slip_110m,sec_ss,2026,-110200000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Strengthened invalidity follow-up save slip -110.2m vs IB (16.7 vs 126.9); exclusions 4197; tick508",
    "bud_pens_reform_path_2030_2212m,sec_ss,2030,2212000000,,,budgeted,src_ccrek_fed_aju_ss_podmi_2026,strong,Pension reform package save path to 2030 2212m (was 2229 IB); tick508",
    "bud_dual_ss_podmi_2026,gg_belgium,2026,148026600000,,,derived,src_dual_ss_podmi_aju_tick508,strong,Dual SS exp 148bn + POD MI 2.3bn OCMW stack; tick508",
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for b in buds:
        f.write(b + "\n")

cmts = [
    (
        "cmt_ss_bc_2026_macro,SS consolidated BC2026 receipts and expenditure CoA,"
        "sec_ss,Beneficiaries contributors,"
        "CoA 2026_22 Deel III,"
        "2026-05-21,2026,2026,148026600000,"
        '"{""rec_m"":148002.4,""exp_m"":148026.6,""contrib_m"":85328,""altfin_m"":27583.4,'
        '""benefits_m"":137624.3,""healthcare_m"":43857.4,""unemp_m"":4836.4,'
        '""pens_emp_m"":43036.6,""invalidity_m"":14839.4,""public_pens_m"":22526.8,'
        '""note"":""Strong CoA; near balance; early spilindex risk unpriced""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "SS financing balance,Price June index risk; dual prior SS,src_ccrek_fed_aju_ss_podmi_2026,strong,Federal>SS>BC2026,tick508"
    ),
    (
        "cmt_podmi_integ_wait_slip,POD MI integration amount +5y wait savings will not land 2026,"
        "sec_federal,OCMW beneficiaries refugees,"
        "CoA 2026_22 POD MI + Council of State advice,"
        "2026-01-01,2026,2026,13100000,"
        '"{""save_ib_m"":40.2,""save_bc_m"":13.1,""integ_bc_m"":10.0,""wait_bc_m"":3.1,'
        '""deliverable_2026"":false,""ocmw_total_m"":2309,'
        '""note"":""Strong CoA: legislation delay; soft savings classic""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Social assistance reform savings,Do not book undeliverable saves; FOI law status,"
        "src_ccrek_fed_aju_ss_podmi_2026,strong,Federal>POD_MI>integ_wait,tick508"
    ),
    (
        "cmt_riziv_invalidity_save_slip,RIZIV healthcare miss + invalidity follow-up save slip,"
        "sec_ss,Patients invalids,"
        "CoA 2026_22 RIZIV tables,"
        "2026-02-01,2026,2029,183100000,"
        '"{""healthcare_miss_m"":183.1,""drugs_miss_m"":145.7,""package_ib_m"":801.4,'
        '""invalidity_slip_2026_m"":110.2,""exclusions_n"":4197,'
        '""note"":""Strong CoA; implementation not ready Sep2026 risk""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Health and invalidity consolidation,Concrete measures FOI; dual prior RTW,"
        "src_ccrek_fed_aju_ss_podmi_2026,strong,Federal>RIZIV>save_slip,tick508"
    ),
    (
        "cmt_dual_ss_podmi_aju,Dual SS 148bn macro + POD MI soft savings,"
        "gg_belgium,SS and OCMW beneficiaries,"
        "CoA 2026_22 residual,"
        "2026-05-21,2026,2026,148026600000,"
        '"{""ss_exp_m"":148026.6,""ocmw_m"":2309,""soft_save_m"":13.1,'
        '""note"":""not additive pure TE; dual social stack""}",'
        "0,active,https://www.ccrek.be/sites/default/files/Docs/2026_22_Begroting2026A1.pdf,"
        "Map dual social expenditure governance,Honest savings booking FOI,"
        "src_dual_ss_podmi_aju_tick508,strong,BE>dual>SS_PODMI,tick508"
    ),
]
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for c in cmts:
        f.write(c + "\n")

lbs = [
    "lb_ss_exp_148bn_bc2026,SS consolidated expenditure 148.0bn BC2026,federal,ops,Federal>SS>exp_BC2026,148026600000,148026600000,Strong CoA: 148026.6m exp / 148002.4m rec near balance; dual prior SS,strong,src_ccrek_fed_aju_ss_podmi_2026,SS beneficiaries,Social protection system,Core entitlement mega-mass,2.0,9.5,6,6.3,Monitor index risk; dual,seed,,tick508",
    "lb_ss_healthcare_43_9bn,RIZIV healthcare benefits 43.9bn BC2026,federal,ops,Federal>RIZIV>healthcare_BC2026,43857400000,43857400000,Strong CoA: 43857.4m (+2.56bn vs IB); 183m savings miss,strong,src_ccrek_fed_aju_ss_podmi_2026,Patients,Health insurance benefits,Core health mass,2.5,9.5,6,6.45,Close drug savings FOI,seed,,tick508",
    "lb_podmi_ocmw_2_3bn,OCMW RMI+wet65 grants 2.309bn BC2026,federal,ops,Federal>POD_MI>OCMW_2026,2309000000,2309000000,Strong CoA: RMI 2133 + wet65 176; integration savings soft,strong,src_ccrek_fed_aju_ss_podmi_2026,OCMW clients,Social assistance,Core safety net,2.5,9.0,5,6.15,Track reform law FOI,seed,,tick508",
    "lb_podmi_save_slip_13m,POD MI integ+wait savings 13m will not deliver 2026,federal,savings,Federal>POD_MI>save_slip,13100000,13100000,Strong CoA: BC 13.1m vs IB 40.2; legislation delay; classic soft save,strong,src_ccrek_fed_aju_ss_podmi_2026,Taxpayers,Social assistance reform,Booked save not achievable,7.5,5.5,4,6.65,Remove undeliverable from path,seed,,tick508",
    "lb_riziv_save_miss_183m,RIZIV 183m of 801m savings package miss 2026,federal,savings,Federal>RIZIV>save_miss,183100000,183100000,Strong CoA: 183.1m unrealized of which 145.7 drugs; dual invalidity slip,strong,src_ccrek_fed_aju_ss_podmi_2026,Patients taxpayers,Health savings package,Soft health saves,6.5,7.5,5,6.75,Compensating measures FOI,seed,,tick508",
    "lb_invalidity_followup_slip_110m,Invalidity follow-up save slip 110m 2026,federal,savings,Federal>RIZIV>invalidity_followup,110200000,110200000,Strong CoA: save 16.7 vs IB 126.9; exclusions 4197; implementation incomplete,strong,src_ccrek_fed_aju_ss_podmi_2026,Invalids,RTW control,Soft RTW savings dual prior,6.5,7.5,5,6.75,Finish regulation FOI,seed,,tick508",
    "lb_rsz_reductions_5_1bn,RSZ contribution reductions ~5.14bn BC2026,federal,taxex,Federal>RSZ>contrib_reductions,5142500000,5142500000,Strong CoA: struct 4.29bn + targeted exp 0.85bn; workbonus 1.83; dual wage subsidies,strong,src_ccrek_fed_aju_ss_podmi_2026,Employers,Wage cost reduction,Large TE-adjacent stack,5.0,9.5,5,7.0,Publish L5 instruments FOI,seed,,tick508",
    "lb_dual_ss_podmi,Dual SS 148bn + POD MI 2.3bn OCMW,multi,ops,BE>dual>SS_PODMI,2309000000,148026600000,Strong dual CoA residual social stack,strong,src_dual_ss_podmi_aju_tick508,Social beneficiaries,Social dual map,Scale dual,3.0,9.5,5,6.55,Honest soft-save accounting,seed,,tick508",
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for lb in lbs:
        f.write(lb + "\n")

foi = (
    "gap_podmi_ss_save_slip_l5,Federal>POD_MI_RIZIV>save_slip_L5,sec_federal,"
    "Legal status and revised cash impact 2026-29 for integration amount +5y wait; RIZIV 183m miss "
    "compensating measures list; invalidity follow-up regulation timeline and exclusion counts; "
    "Zuidertoren RSZ asset sale timing,"
    "CoA 2026_22: soft saves strong aggregates; residual law/measure L5,7,"
    "POD MI / RIZIV / RSZ,info@mi-is.be,"
    ",docs/doge/foi/drafts/gap_podmi_ss_save_slip_l5.md,"
    "ready,2026-07-28,,,,,cmt_podmi_integ_wait_slip,"
    "lb_podmi_save_slip_13m|lb_riziv_save_miss_183m,"
    "2026-07-28T23:30:00Z,2026-07-28T23:30:00Z,"
    "tick508: CoA 2026_22 residual POD MI+SS; FOI L5 human send only\n"
)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi)

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_499,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:10:00Z,,Spawned tick507 after CoA Justice/Fedasil residual; progress@510 next ticks; rq_116 deferred"
)
new = (
    "rq_499,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,"
    "gap_podmi_ss_save_slip_l5,"
    "2026-07-28T23:10:00Z,2026-07-28T23:30:00Z,"
    "tick508: CoA 2026_22 residual SS 148bn POD MI soft saves dual; FOI; progress@510 next; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_499 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_500,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-28T23:30:00Z,,Spawned tick508 after CoA SS/POD MI residual; progress@510 next tick; rq_116 deferred\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-28T23:30:00Z,rq_499,508,no,"
    "Tick508 CoA SS 148bn POD MI soft saves residual; next prio5 rq_500; progress@510 next; rq_116 SWA deferred.\n",
    encoding="utf-8",
)
print("tick508 OK")
