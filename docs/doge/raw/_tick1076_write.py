"""Tick 1076 — Kampenhout GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_kampenhout_jr2025"
ENT = "city_kampenhout"
TICK = "tick1076"
TS = "2026-08-11T03:30:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_kam_assets_2025",ENT,2025,102356542,"bbc_jr_realized",SRC,"strong","Assets YE2025 102.357m (was 99.481m); tick1076"),
("bud_kam_equity_2025",ENT,2025,84746702,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 84.747m (was 79.791m); tick1076"),
("bud_kam_debt_total_2025",ENT,2025,17609840,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 17.610m DECLINE (was 19.689m); tick1076"),
("bud_kam_fin_debt_2025",ENT,2025,8206115,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 8.206m DECLINE (was 9.470m); tick1076"),
("bud_kam_fin_debt_lt_2025",ENT,2025,6787171,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 6.787m DECLINE (was 7.864m); tick1076"),
("bud_kam_fin_debt_st_due_2025",ENT,2025,1418945,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 1.419m; tick1076"),
("bud_kam_new_loans_2025",ENT,2025,356947,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 0.357m; tick1076"),
("bud_kam_aflossingen_2025",ENT,2025,1620493,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 1.620m; tick1076"),
("bud_kam_cash_2025",ENT,2025,3143317,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 3.143m MASSIVE DROP FOI (was 8.295m); tick1076"),
("bud_kam_pension_2025",ENT,2025,3712227,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 3.712m slight up (was 3.605m); tick1076"),
("bud_kam_cap_subs_2025",ENT,2025,7148476,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 7.148m; tick1076"),
("bud_kam_fva_total_2025",ENT,2025,15582726,"bbc_jr_realized",SRC,"strong","FVA total YE2025 15.583m JUMP; tick1076"),
("bud_kam_fva_igs_2025",ENT,2025,9666273,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 9.666m JUMP herwaardering FOI (was 0.933m); tick1076"),
("bud_kam_leasing_mva_2025",ENT,2025,1051306,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 1.051m; tick1076"),
("bud_kam_expl_rec_2025",ENT,2025,31316540,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 31.317m; tick1076"),
("bud_kam_expl_exp_2025",ENT,2025,27914044,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 27.914m; tick1076"),
("bud_kam_expl_saldo_2025",ENT,2025,3402496,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +3.402m STRONG; tick1076"),
("bud_kam_invest_exp_2025",ENT,2025,5425421,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 5.425m vs MJP 8.291m UNDERSPEND FOI; tick1076"),
("bud_kam_invest_rec_2025",ENT,2025,116519,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.117m; tick1076"),
("bud_kam_invest_saldo_2025",ENT,2025,-5308902,"bbc_jr_realized",SRC,"strong","Investeringssaldo -5.309m; tick1076"),
("bud_kam_mjp_invest_planned_2025",ENT,2025,8290937,"bbc_jr_realized",SRC,"strong","MJP invest planned 8.291m vs realized 5.425m underspend FOI; tick1076"),
("bud_kam_invest_mva_2025",ENT,2025,4898585,"bbc_jr_realized",SRC,"strong","Investeringen MVA 4.899m; tick1076"),
("bud_kam_invest_subs_granted_2025",ENT,2025,522032,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.522m; tick1076"),
("bud_kam_afm_2025",ENT,2025,1805655,"bbc_jr_realized",SRC,"strong","AFM +1.806m STRONG; tick1076"),
("bud_kam_afm_corr_2025",ENT,2025,2668575,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +2.669m STRONG; tick1076"),
("bud_kam_bbr_2025",ENT,2025,4032035,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +4.032m; tick1076"),
("bud_kam_budget_result_2025",ENT,2025,-3042050,"bbc_jr_realized",SRC,"strong","Budgettair resultaat -3.042m NEG HIGH FOI; tick1076"),
("bud_kam_cum_br_2025",ENT,2025,4032035,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +4.032m; tick1076"),
("bud_kam_pnl_2025",ENT,2025,-3462172,"bbc_jr_realized",SRC,"strong","P&L -3.462m FLIP FOI (was +2.937m); tick1076"),
("bud_kam_ge_expl_exp_2025",ENT,2025,17908976,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 17.909m; tick1076"),
("bud_kam_ge_expl_rec_2025",ENT,2025,23905493,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 23.905m; tick1076"),
("bud_kam_ocmw_expl_exp_2025",ENT,2025,10005068,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 10.005m; tick1076"),
("bud_kam_ocmw_expl_rec_2025",ENT,2025,7411047,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 7.411m; tick1076"),
("bud_kam_ocmw_expl_gap_2025",ENT,2025,-2594021,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -2.594m; tick1076"),
("bud_kam_ocmw_cover_2025",ENT,2025,0,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 0.000 ZERO FOI; OCMW equity -4.657m; tick1076"),
("bud_kam_ocmw_equity_cum_2025",ENT,2025,-10664935,"bbc_jr_realized",SRC,"strong","OCMW gecumuleerd tekort YE2025 -10.665m WORSENING FOI; tick1076"),
("bud_kam_ocmw_pnl_2025",ENT,2025,-3257826,"bbc_jr_realized",SRC,"strong","OCMW P&L -3.258m FOI; tick1076"),
("bud_kam_equity_cum_2025",ENT,2025,19461666,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +19.462m; tick1076"),
("bud_kam_personnel_2025",ENT,2025,16248163,"bbc_jr_realized",SRC,"strong","Bezoldigingen T2 16.248m incl education pass-through 1.832m; tick1076"),
("bud_kam_edu_pass_through_2025",ENT,2025,1831561,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 1.832m; tick1076"),
("bud_kam_toelagen_2025",ENT,2025,3998710,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 3.999m FOI residual; tick1076"),
("bud_kam_toelagen_police_2025",ENT,2025,2010390,"bbc_jr_realized",SRC,"strong","Toelage politiezone 2.010m JUMP; tick1076"),
("bud_kam_toelagen_fire_2025",ENT,2025,752069,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.752m; tick1076"),
("bud_kam_toelagen_igs_2025",ENT,2025,818268,"bbc_jr_realized",SRC,"strong","Toelage IGS 0.818m; tick1076"),
("bud_kam_toelagen_other_2025",ENT,2025,417983,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.418m FOI; tick1076"),
("bud_kam_ocmw_aid_2025",ENT,2025,617636,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 0.618m; tick1076"),
("bud_kam_fiscal_2025",ENT,2025,15318835,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 15.319m; tick1076"),
("bud_kam_fiscal_ov_2025",ENT,2025,6299025,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 6.299m; tick1076"),
("bud_kam_fiscal_pb_2025",ENT,2025,7200396,"bbc_jr_realized",SRC,"strong","Aanvullende PB 7.200m; tick1076"),
("bud_kam_gemeentefonds_2025",ENT,2025,2783442,"bbc_jr_realized",SRC,"strong","Gemeentefonds 2.783m; tick1076"),
("bud_kam_interest_2025",ENT,2025,223239,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.223m; tick1076"),
("bud_kam_herwaardering_fva_2025",ENT,2025,8730049,"bbc_jr_realized",SRC,"strong","Herwaardering FVA/reserves +8.730m FOI; tick1076"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_kam_police_toelage_2025","Kampenhout politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,2010390,"{2025:2010390}",0,"active","","Kampenhout politiezone toelage 2025 JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>toelagen",TICK),
("comm_kam_fire_toelage_2025","Kampenhout HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,752069,"{2025:752069}",0,"active","","Kampenhout HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>toelagen",TICK),
("comm_kam_other_toelagen_2025","Kampenhout andere toelagen 2025",ENT,"Various","BBC JR2025","",2025,2025,417983,"{2025:417983}",0,"active","","Kampenhout other toelagen 0.418m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>toelagen",TICK),
("comm_kam_cash_drop_2025","Kampenhout cash MASSIVE DROP 2025",ENT,"Liquidity","BBC JR2025","",2025,2025,3143317,"{2025:3143317}",0,"active","","Kampenhout cash 3.143m from 8.295m DROP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>cash",TICK),
("comm_kam_ocmw_zero_cover_2025","Kampenhout OCMW cover ZERO 2025",ENT,"OCMW Kampenhout","BBC JR2025","",2025,2025,0,"{2025:0}",0,"active","","Kampenhout OCMW cover 0 ZERO equity -4.657m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>ocmw",TICK),
("comm_kam_invest_underspend_2025","Kampenhout invest underspend 2025",ENT,"Capital program","BBC JR2025","",2025,2025,5425421,"{2025:5425421}",0,"active","","Kampenhout invest 5.43 vs MJP 8.29 FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>invest",TICK),
("comm_kam_budget_neg_2025","Kampenhout budget NEG -3.04m 2025",ENT,"Budget path","BBC JR2025 J2","",2025,2025,3042050,"{2025:3042050}",0,"active","","Kampenhout budget -3.04m NEG HIGH FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Kampenhout>budget",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_kam_cash_drop_3_14m_2025","Kampenhout cash 3.14m MASSIVE DROP from 8.30m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",3143317,3143317,"Cash residual dual MASSIVE DROP","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",9.0,5.5,3.5,pi(9.0,5.5,3.5),"Cash path FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_budget_neg_3_04m_2025","Kampenhout budget -3.04m NEG HIGH FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",3042050,3042050,"Budget residual dual NEG HIGH","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Budget path FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_ocmw_zero_cover_2025","Kampenhout OCMW cover ZERO equity -4.66m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",10664935,0,"OCMW dual residual ZERO cover equity sink","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",9.0,5.0,3.5,pi(9.0,5.0,3.5),"Cover policy FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_toelagen_3_99m_2025","Kampenhout toelagen 3.99m police 2.01 JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",3998710,3998710,"Grants residual dual","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Named matrix FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_invest_underspend_2025","Kampenhout invest 5.43 vs MJP 8.29 UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",5425421,5425421,"Invest residual dual underspend","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",7.5,5.0,3.5,pi(7.5,5.0,3.5),"Invest path FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_fin_debt_8_21m_2025","Kampenhout fin debt 8.21m DECLINE FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",8206115,8206115,"Debt stock residual dual DECLINE","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",6.0,5.5,3.5,pi(6.0,5.5,3.5),"Debt path FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_personnel_16_25m_2025","Kampenhout personnel 16.25m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",16248163,16248163,"Wage bill residual","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"FTE FOI","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
("lb_kam_afm_1_81m_2025","Kampenhout AFM +1.81m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Kampenhout_L5",1805655,1805655,"AFM residual dual","strong",SRC,"Kampenhout residents","Local dual residual map VL JR2025","JR2025 BBC Kampenhout GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1076; primary Kampenhout JR2025; dual residual after Lennik; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Kampenhout Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.kampenhout.be/jaarrekening-2025,"
    "Lokaal Bestuur Kampenhout,2026-08-11,primary_pdf,"
    "tick1076; 131p; GR 25.06.2026 pub 01.07.2026; KBO GE 0207.533.280 / OCMW 0212.223.033; "
    "AD Veerle Van Sweevelt FD Daisy Vannuffelen; Gemeentehuisstraat 32 / Dorpsstraat 9 NIS 23038; "
    "assets 102.357m equity 84.747m fin debt 8.206m DECLINE new loans 0.357m cash MASSIVE DROP 3.143m "
    "pension 3.712m AFM +1.806m BBR 4.032m budget -3.042m NEG HIGH P&L -3.462m FLIP invest 5.425 vs MJP 8.291 "
    "toelagen 3.999m police 2.010 JUMP OCMW cover 0 ZERO equity -4.657m; dual residual after Lennik"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Kampenhout,Commune de Kampenhout,Municipality of Kampenhout,municipality,vlaanderen_gov,nl,"
    "https://www.kampenhout.be,info@kampenhout.be,Gemeentehuisstraat 32 1910 Kampenhout,"
    "JR2025 dual residual tick1076; KBO 0207.533.280 / OCMW 0212.223.033; assets 102.357m fin debt 8.206m DECLINE "
    "new loans 0.357m; cash MASSIVE DROP 3.143m; pension 3.712m; AFM +1.806m; BBR 4.032m; budget -3.042m NEG HIGH; "
    "OCMW cover 0 ZERO equity -4.657m; toelagen 3.999m police 2.010 JUMP; invest underspend 5.43 vs MJP 8.29; "
    "AD Veerle Van Sweevelt FD Daisy Vannuffelen"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_kam_cash_budget_ocmw_zero_l5,Vlaanderen>Gemeenten>Kampenhout>cash_budget_ocmw_zero_L5,city_kampenhout,'
    '"Cash MASSIVE DROP 8.295to3.143m; budget -3.042m NEG HIGH despite AFM +1.806m and expl +3.402m; OCMW cover '
    'ZERO while OCMW equity -4.657m cum deficit -10.665m P&L -3.258m; toelagen 3.999m police 2.010 JUMP; invest '
    '5.425 vs MJP 8.291; FVA IGS herwaardering +8.730m; fin debt DECLINE 8.206m",'
    '"Flemish Brabant mun with cash collapse, large negative budget result despite strong AFM, and zero OCMW '
    'cover while OCMW equity sinks",9,Gemeente Kampenhout,info@kampenhout.be,'
    "Gemeentehuisstraat 32 1910 Kampenhout,docs/doge/foi/drafts/gap_kam_cash_budget_ocmw_zero_l5.md,ready,2026-08-11,,,,,,"
    f"comm_kam_cash_drop_2025,lb_kam_cash_drop_3_14m_2025,{TS},{TS},"
    "tick1076; ready not sent; do not send without human OK"
)
with open(DATA / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")
print("foi +1")

rq_path = DATA / "research_queue.csv"
rows = list(csv.reader(rq_path.open(encoding="utf-8")))
header, body = rows[0], rows[1:]
out = [header]
found = False
residual = (
    "PROGRESS residual: dual L5 or unmined primary (Torhout full BBC / Oosterzele / Nijlen if public / "
    "Vorselaar / Kalmthout / Schelle / Ronse city GE+OCMW if public / other); prefer FOI-adjacent L5; "
    "skip rq_116; progress@1080"
)
for r in body:
    if r and r[0] == "rq_1076":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1076: Kampenhout GE+OCMW JR2025 dual residual done; FOI "
            "gap_kam_cash_budget_ocmw_zero_l5 ready prio9; spawn rq_1077"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1076 not found")
out.append(
    [
        "rq_1077",
        "Continuous FOI-adjacent public hole-fill batch",
        "hole_fill",
        "5",
        "open",
        "L5",
        "gg_belgium",
        residual,
        "",
        TS,
        TS,
        "spawned tick1076 after Kampenhout dual residual; residual dual L5 next; progress@1080 in 3",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1076,1076,no,"
    "tick1076 Kampenhout GE+OCMW JR2025 dual residual; FOI gap_kam_cash_budget_ocmw_zero_l5 prio9 ready; "
    "assets 102.357m fin debt 8.206m DECLINE new loans 0.357m cash MASSIVE DROP 3.143m pension 3.712m "
    "AFM +1.806m BBR 4.032m budget -3.042m NEG HIGH P&L -3.462m FLIP invest 5.425 vs MJP 8.291 "
    "toelagen 3.999m police 2.010 JUMP OCMW cover 0 ZERO equity -4.657m; next residual dual L5 rq_1077; "
    "progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
