"""Tick 1077 — Duffel GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_duffel_jr2025"
ENT = "city_duffel"
TICK = "tick1077"
TS = "2026-08-11T04:00:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_duf_assets_2025",ENT,2025,143101601,"bbc_jr_realized",SRC,"strong","Assets YE2025 143.102m (was 135.184m); tick1077"),
("bud_duf_equity_2025",ENT,2025,78700984,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 78.701m (was 78.051m); tick1077"),
("bud_duf_debt_total_2025",ENT,2025,64400617,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 64.401m JUMP (was 57.133m); tick1077"),
("bud_duf_fin_debt_2025",ENT,2025,39470190,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 39.470m JUMP FOI (was 33.136m); tick1077"),
("bud_duf_fin_debt_lt_2025",ENT,2025,37376524,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 37.377m JUMP (was 30.149m); tick1077"),
("bud_duf_fin_debt_st_due_2025",ENT,2025,2093666,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 2.094m; tick1077"),
("bud_duf_new_loans_2025",ENT,2025,9330337,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 9.330m MASSIVE JUMP FOI; tick1077"),
("bud_duf_aflossingen_2025",ENT,2025,2995822,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 2.996m; tick1077"),
("bud_duf_cash_2025",ENT,2025,6704684,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 6.705m JUMP (was 3.734m); tick1077"),
("bud_duf_pension_2025",ENT,2025,16695147,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 16.695m JUMP FOI (was 15.486m); tick1077"),
("bud_duf_cap_subs_2025",ENT,2025,15825445,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 15.825m; tick1077"),
("bud_duf_fva_total_2025",ENT,2025,15870094,"bbc_jr_realized",SRC,"strong","FVA total YE2025 15.870m; tick1077"),
("bud_duf_fva_igs_2025",ENT,2025,15685378,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 15.685m; tick1077"),
("bud_duf_leasing_mva_2025",ENT,2025,12326587,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 12.327m (gem 5.708+bedrijf 6.619); tick1077"),
("bud_duf_expl_rec_2025",ENT,2025,51188117,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 51.188m; tick1077"),
("bud_duf_expl_exp_2025",ENT,2025,45474227,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 45.474m; tick1077"),
("bud_duf_expl_saldo_2025",ENT,2025,5713890,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +5.714m STRONG; tick1077"),
("bud_duf_invest_exp_2025",ENT,2025,9722149,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 9.722m vs MJP 17.722m UNDERSPEND FOI; tick1077"),
("bud_duf_invest_rec_2025",ENT,2025,1688013,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 1.688m; tick1077"),
("bud_duf_invest_saldo_2025",ENT,2025,-8034137,"bbc_jr_realized",SRC,"strong","Investeringssaldo -8.034m; tick1077"),
("bud_duf_mjp_invest_planned_2025",ENT,2025,17721612,"bbc_jr_realized",SRC,"strong","MJP invest planned 17.722m vs realized 9.722m underspend FOI; tick1077"),
("bud_duf_invest_mva_2025",ENT,2025,8192716,"bbc_jr_realized",SRC,"strong","Investeringen MVA 8.193m; tick1077"),
("bud_duf_invest_subs_granted_2025",ENT,2025,1389663,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 1.390m; tick1077"),
("bud_duf_afm_2025",ENT,2025,3110911,"bbc_jr_realized",SRC,"strong","AFM +3.111m STRONG; tick1077"),
("bud_duf_afm_corr_2025",ENT,2025,3455879,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +3.456m STRONG; tick1077"),
("bud_duf_bbr_2025",ENT,2025,8815541,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +8.816m; tick1077"),
("bud_duf_budget_result_2025",ENT,2025,4158946,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +4.159m STRONG; tick1077"),
("bud_duf_cum_br_2025",ENT,2025,9069709,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +9.070m; tick1077"),
("bud_duf_onbeschikbaar_2025",ENT,2025,254168,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.254m; tick1077"),
("bud_duf_pnl_2025",ENT,2025,-183423,"bbc_jr_realized",SRC,"strong","P&L -0.183m IMPROVING (was -7.510m); tick1077"),
("bud_duf_ge_expl_exp_2025",ENT,2025,32490661,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 32.491m; tick1077"),
("bud_duf_ge_expl_rec_2025",ENT,2025,39643148,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 39.643m; tick1077"),
("bud_duf_ocmw_expl_exp_2025",ENT,2025,12983567,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 12.984m; tick1077"),
("bud_duf_ocmw_expl_rec_2025",ENT,2025,11544969,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 11.545m; tick1077"),
("bud_duf_ocmw_expl_gap_2025",ENT,2025,-1438598,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -1.439m; tick1077"),
("bud_duf_ocmw_cover_2025",ENT,2025,2317504,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 2.318m FULL; tick1077"),
("bud_duf_ocmw_equity_cum_2025",ENT,2025,-5696600,"bbc_jr_realized",SRC,"strong","OCMW gecumuleerd tekort YE2025 -5.697m; tick1077"),
("bud_duf_ocmw_pnl_2025",ENT,2025,-2513366,"bbc_jr_realized",SRC,"strong","OCMW P&L -2.513m; tick1077"),
("bud_duf_equity_cum_2025",ENT,2025,-8210591,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity tekort YE2025 -8.211m; tick1077"),
("bud_duf_personnel_2025",ENT,2025,27844602,"bbc_jr_realized",SRC,"strong","Bezoldigingen 27.845m incl education pass-through 7.553m; tick1077"),
("bud_duf_edu_pass_through_2025",ENT,2025,7553233,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 7.553m JUMP; tick1077"),
("bud_duf_toelagen_2025",ENT,2025,4582366,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 4.582m FOI residual; tick1077"),
("bud_duf_toelagen_police_2025",ENT,2025,2618848,"bbc_jr_realized",SRC,"strong","Toelage politiezone 2.619m DROP (was 3.185m); tick1077"),
("bud_duf_toelagen_fire_2025",ENT,2025,856546,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.857m; tick1077"),
("bud_duf_toelagen_agb_2025",ENT,2025,582881,"bbc_jr_realized",SRC,"strong","Toelage AGB Duffel 0.583m; tick1077"),
("bud_duf_toelagen_other_2025",ENT,2025,524091,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst residual 0.524m FOI; tick1077"),
("bud_duf_ocmw_aid_2025",ENT,2025,1526415,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 1.526m; tick1077"),
("bud_duf_fiscal_2025",ENT,2025,20325701,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 20.326m; tick1077"),
("bud_duf_fiscal_ov_2025",ENT,2025,7321500,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 7.322m; tick1077"),
("bud_duf_fiscal_pb_2025",ENT,2025,7978614,"bbc_jr_realized",SRC,"strong","Aanvullende PB 7.979m; tick1077"),
("bud_duf_gemeentefonds_2025",ENT,2025,4663454,"bbc_jr_realized",SRC,"strong","Gemeentefonds 4.663m; tick1077"),
("bud_duf_interest_2025",ENT,2025,1511567,"bbc_jr_realized",SRC,"strong","Intresten op leningen 1.512m; tick1077"),
("bud_duf_agb_afm_corr_2025",ENT,2025,-367780,"bbc_jr_realized",SRC,"strong","AGB Duffel corr AFM -0.368m NEG FOI; tick1077"),
("bud_duf_consol_afm_corr_2025",ENT,2025,3088100,"bbc_jr_realized",SRC,"strong","Consol GE+OCMW+AGB corr AFM +3.088m; tick1077"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_duf_police_toelage_2025","Duffel politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,2618848,"{2025:2618848}",0,"active","","Duffel politiezone toelage 2025 DROP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>toelagen",TICK),
("comm_duf_fire_toelage_2025","Duffel HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,856546,"{2025:856546}",0,"active","","Duffel HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>toelagen",TICK),
("comm_duf_agb_toelage_2025","Duffel AGB toelage 2025",ENT,"AGB Duffel","BBC JR2025","",2025,2025,582881,"{2025:582881}",0,"active","","Duffel AGB toelage 0.583m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>agb",TICK),
("comm_duf_new_loans_2025","Duffel new loans JUMP 2025",ENT,"Debt program","BBC JR2025 T4","",2025,2025,9330337,"{2025:9330337}",0,"active","","Duffel new loans 9.330m MASSIVE JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>debt",TICK),
("comm_duf_pension_jump_2025","Duffel pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,16695147,"{2025:16695147}",0,"active","","Duffel pension 16.695m JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>pension",TICK),
("comm_duf_ocmw_cover_2025","Duffel OCMW cover full 2025",ENT,"OCMW Duffel","BBC JR2025","",2025,2025,2317504,"{2025:2317504}",0,"active","","Duffel OCMW cover 2.318m FULL","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Duffel>ocmw",TICK),
("comm_duf_invest_underspend_2025","Duffel invest underspend 2025",ENT,"Capital program","BBC JR2025","",2025,2025,9722149,"{2025:9722149}",0,"active","","Duffel invest 9.72 vs MJP 17.72 FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Duffel>invest",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_duf_new_loans_9_33m_2025","Duffel new loans 9.33m MASSIVE JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",9330337,9330337,"Debt residual dual MASSIVE new loans","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",9.0,6.0,3.5,pi(9.0,6.0,3.5),"Loan purpose FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_fin_debt_39_47m_2025","Duffel fin debt 39.47m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",39470190,39470190,"Debt stock residual dual JUMP","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",8.0,6.0,3.5,pi(8.0,6.0,3.5),"Debt path FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_pension_16_70m_2025","Duffel pension 16.70m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",16695147,16695147,"Pension residual dual JUMP","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",8.0,5.5,3.5,pi(8.0,5.5,3.5),"Pension FOI jump","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_invest_underspend_2025","Duffel invest 9.72 vs MJP 17.72 UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",9722149,9722149,"Invest residual dual underspend","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",7.5,5.5,3.5,pi(7.5,5.5,3.5),"Invest path FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_toelagen_4_58m_2025","Duffel toelagen 4.58m police 2.62 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",4582366,4582366,"Grants residual dual","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Named matrix FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_personnel_27_85m_2025","Duffel personnel 27.85m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",27844602,27844602,"Wage bill residual","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"FTE FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_ocmw_cover_2_32m_2025","Duffel OCMW cover 2.32m FULL FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",2317504,2317504,"OCMW dual residual FULL cover","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",6.5,4.5,3.5,pi(6.5,4.5,3.5),"Cover policy FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
("lb_duf_agb_afm_neg_0_37m_2025","Duffel AGB corr AFM -0.37m NEG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Duffel_L5",367780,367780,"AGB dual residual NEG AFM","strong",SRC,"Duffel residents","Local dual residual map VL JR2025","JR2025 BBC Duffel GEOC realized figures",7.0,4.0,3.5,pi(7.0,4.0,3.5),"AGB path FOI","active","","tick1077; primary Duffel JR2025; dual residual after Kampenhout; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Duffel Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.duffel.be/budgetmeerjarenplan,"
    "Lokaal Bestuur Duffel,2026-08-11,primary_pdf,"
    "tick1077; 239p; GR+RMW 22.06.2026 pub 24.06.2026; NIS 12009; "
    "AD Tim Op de Beeck FD Steven Walckiers; Gemeentestraat 21 2570; "
    "assets 143.102m equity 78.701m fin debt 39.470m JUMP new loans 9.330m MASSIVE cash JUMP 6.705m "
    "pension JUMP 16.695m AFM +3.111m BBR 8.816m budget +4.159m P&L -0.183 IMPROVING invest 9.722 vs MJP 17.722 "
    "toelagen 4.582m police 2.619 DROP OCMW cover 2.318 FULL AGB corr AFM -0.368 NEG; dual residual after Kampenhout"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Duffel,Commune de Duffel,Municipality of Duffel,municipality,vlaanderen_gov,nl,"
    "https://www.duffel.be,financien@duffel.be,Gemeentestraat 21 2570 Duffel,"
    "JR2025 dual residual tick1077; NIS 12009; assets 143.102m fin debt 39.470m JUMP "
    "new loans 9.330m MASSIVE; cash JUMP 6.705m; pension JUMP 16.695m; AFM +3.111m; BBR 8.816m; budget +4.159m; "
    "OCMW cover 2.318 FULL; toelagen 4.582m police 2.619 DROP; invest underspend 9.72 vs MJP 17.72; "
    "AGB corr AFM -0.368 NEG; AD Tim Op de Beeck FD Steven Walckiers"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_duf_loans_pension_invest_agb_l5,Vlaanderen>Gemeenten>Duffel>loans_pension_invest_agb_L5,city_duffel,'
    '"New loans 9.330m MASSIVE JUMP fin debt to 39.470m; pension JUMP 15.486to16.695m; invest underspend '
    '9.722 vs MJP 17.722; toelagen 4.582m police 2.619 DROP AGB 0.583; OCMW cover 2.318 FULL cum -5.697m; '
    'AGB corr AFM -0.368 NEG; budget +4.159m AFM +3.111m",'
    '"Antwerp mun with massive new-loan ramp, pension provision jump, invest underspend, and negative AGB '
    'corrected AFM despite strong dual AFM",9,Gemeente Duffel,financien@duffel.be,'
    "Gemeentestraat 21 2570 Duffel,docs/doge/foi/drafts/gap_duf_loans_pension_invest_agb_l5.md,ready,2026-08-11,,,,,,"
    f"comm_duf_new_loans_2025,lb_duf_new_loans_9_33m_2025,{TS},{TS},"
    "tick1077; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1077":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1077: Duffel GE+OCMW JR2025 dual residual done; FOI "
            "gap_duf_loans_pension_invest_agb_l5 ready prio9; spawn rq_1078"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1077 not found")
out.append(
    [
        "rq_1078",
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
        "spawned tick1077 after Duffel dual residual; residual dual L5 next; progress@1080 in 2",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1077,1077,no,"
    "tick1077 Duffel GE+OCMW JR2025 dual residual; FOI gap_duf_loans_pension_invest_agb_l5 prio9 ready; "
    "assets 143.102m fin debt 39.470m JUMP new loans 9.330m MASSIVE cash JUMP 6.705m pension JUMP 16.695m "
    "AFM +3.111m BBR 8.816m budget +4.159m P&L -0.183 IMPROVING invest 9.722 vs MJP 17.722 "
    "toelagen 4.582m police 2.619 DROP OCMW cover 2.318 FULL AGB corr AFM -0.368 NEG; next residual dual L5 "
    "rq_1078; progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
