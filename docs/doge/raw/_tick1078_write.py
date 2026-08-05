"""Tick 1078 — Bonheiden GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_bonheiden_jr2025"
ENT = "city_bonheiden"
TICK = "tick1078"
TS = "2026-08-11T04:30:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_bon_assets_2025",ENT,2025,81650422,"bbc_jr_realized",SRC,"strong","Assets YE2025 81.650m (was 79.337m); tick1078"),
("bud_bon_equity_2025",ENT,2025,63309822,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 63.310m (was 61.918m); tick1078"),
("bud_bon_debt_total_2025",ENT,2025,18340599,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 18.341m slight up (was 17.419m); tick1078"),
("bud_bon_fin_debt_2025",ENT,2025,7089729,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 7.090m DECLINE (was 7.425m); tick1078"),
("bud_bon_fin_debt_lt_2025",ENT,2025,6436540,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 6.437m DECLINE (was 6.703m); tick1078"),
("bud_bon_fin_debt_st_due_2025",ENT,2025,653190,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 0.653m; tick1078"),
("bud_bon_new_loans_2025",ENT,2025,358636,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 0.359m LOW (leasing-heavy); tick1078"),
("bud_bon_aflossingen_2025",ENT,2025,693914,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 0.694m; tick1078"),
("bud_bon_cash_2025",ENT,2025,8068264,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 8.068m JUMP (was 6.564m); tick1078"),
("bud_bon_pension_2025",ENT,2025,7650424,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 7.650m JUMP FOI (was 6.593m); tick1078"),
("bud_bon_cap_subs_2025",ENT,2025,6153634,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 6.154m; tick1078"),
("bud_bon_fva_total_2025",ENT,2025,7818277,"bbc_jr_realized",SRC,"strong","FVA total YE2025 7.818m; tick1078"),
("bud_bon_fva_igs_2025",ENT,2025,7788774,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 7.789m; tick1078"),
("bud_bon_leasing_mva_2025",ENT,2025,1379766,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 1.380m; tick1078"),
("bud_bon_expl_rec_2025",ENT,2025,31558340,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 31.558m; tick1078"),
("bud_bon_expl_exp_2025",ENT,2025,26586905,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 26.587m; tick1078"),
("bud_bon_expl_saldo_2025",ENT,2025,4971435,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +4.971m STRONG; tick1078"),
("bud_bon_invest_exp_2025",ENT,2025,3811768,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 3.812m vs MJP 18.070m MASSIVE UNDERSPEND FOI; tick1078"),
("bud_bon_invest_rec_2025",ENT,2025,482157,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.482m; tick1078"),
("bud_bon_invest_saldo_2025",ENT,2025,-3329611,"bbc_jr_realized",SRC,"strong","Investeringssaldo -3.330m; tick1078"),
("bud_bon_mjp_invest_planned_2025",ENT,2025,18070462,"bbc_jr_realized",SRC,"strong","MJP invest planned 18.070m vs realized 3.812m MASSIVE underspend FOI; tick1078"),
("bud_bon_invest_mva_2025",ENT,2025,3536663,"bbc_jr_realized",SRC,"strong","Investeringen MVA 3.537m; tick1078"),
("bud_bon_invest_subs_granted_2025",ENT,2025,229705,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.230m; tick1078"),
("bud_bon_afm_2025",ENT,2025,4322398,"bbc_jr_realized",SRC,"strong","AFM +4.322m STRONG; tick1078"),
("bud_bon_afm_corr_2025",ENT,2025,4422311,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +4.422m STRONG; tick1078"),
("bud_bon_bbr_2025",ENT,2025,8164215,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +8.164m; tick1078"),
("bud_bon_budget_result_2025",ENT,2025,1351423,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +1.351m STRONG; tick1078"),
("bud_bon_cum_br_2025",ENT,2025,8350881,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +8.351m; tick1078"),
("bud_bon_onbeschikbaar_2025",ENT,2025,186667,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.187m; tick1078"),
("bud_bon_pnl_2025",ENT,2025,1160952,"bbc_jr_realized",SRC,"strong","P&L +1.161m IMPROVING (was -0.624m); tick1078"),
("bud_bon_ge_expl_exp_2025",ENT,2025,22791479,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 22.791m; tick1078"),
("bud_bon_ge_expl_rec_2025",ENT,2025,29049867,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 29.050m; tick1078"),
("bud_bon_ocmw_expl_exp_2025",ENT,2025,3795426,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 3.795m; tick1078"),
("bud_bon_ocmw_expl_rec_2025",ENT,2025,2508473,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 2.508m; tick1078"),
("bud_bon_ocmw_expl_gap_2025",ENT,2025,-1286953,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -1.287m; tick1078"),
("bud_bon_ocmw_cover_2025",ENT,2025,0,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 0.000 ZERO FOI; OCMW equity -4.370m; tick1078"),
("bud_bon_ocmw_equity_cum_2025",ENT,2025,-5866450,"bbc_jr_realized",SRC,"strong","OCMW gecumuleerd tekort YE2025 -5.866m WORSENING FOI; tick1078"),
("bud_bon_ocmw_pnl_2025",ENT,2025,-1383491,"bbc_jr_realized",SRC,"strong","OCMW P&L -1.383m FOI; tick1078"),
("bud_bon_equity_cum_2025",ENT,2025,6921088,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +6.921m; tick1078"),
("bud_bon_personnel_2025",ENT,2025,14645287,"bbc_jr_realized",SRC,"strong","Bezoldigingen T2 14.645m incl education pass-through 2.598m; tick1078"),
("bud_bon_edu_pass_through_2025",ENT,2025,2597807,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 2.598m JUMP; tick1078"),
("bud_bon_toelagen_2025",ENT,2025,5733328,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 5.733m FOI residual; tick1078"),
("bud_bon_toelagen_police_2025",ENT,2025,1950590,"bbc_jr_realized",SRC,"strong","Toelage politiezone 1.951m DROP (was 2.372m); tick1078"),
("bud_bon_toelagen_fire_2025",ENT,2025,734478,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.734m; tick1078"),
("bud_bon_toelagen_igs_2025",ENT,2025,1678936,"bbc_jr_realized",SRC,"strong","Toelage IGS 1.679m; tick1078"),
("bud_bon_toelagen_other_2025",ENT,2025,1367858,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst residual 1.368m FOI; tick1078"),
("bud_bon_ocmw_aid_2025",ENT,2025,1270488,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 1.270m; tick1078"),
("bud_bon_fiscal_2025",ENT,2025,19432882,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 19.433m; tick1078"),
("bud_bon_fiscal_ov_2025",ENT,2025,5337204,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 5.337m; tick1078"),
("bud_bon_fiscal_pb_2025",ENT,2025,10346305,"bbc_jr_realized",SRC,"strong","Aanvullende PB 10.346m; tick1078"),
("bud_bon_gemeentefonds_2025",ENT,2025,3399994,"bbc_jr_realized",SRC,"strong","Gemeentefonds 3.400m; tick1078"),
("bud_bon_interest_2025",ENT,2025,141717,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.142m; tick1078"),
("bud_bon_agb_afm_corr_2025",ENT,2025,-10410,"bbc_jr_realized",SRC,"strong","AGB Bonheiden corr AFM -0.010m NEG FOI; tick1078"),
("bud_bon_agb_bbr_2025",ENT,2025,-5420,"bbc_jr_realized",SRC,"strong","AGB BBR -0.005m NEG FOI; tick1078"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_bon_police_toelage_2025","Bonheiden politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,1950590,"{2025:1950590}",0,"active","","Bonheiden politiezone toelage 2025 DROP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>toelagen",TICK),
("comm_bon_igs_toelage_2025","Bonheiden IGS toelage 2025",ENT,"IGS","BBC JR2025","",2025,2025,1678936,"{2025:1678936}",0,"active","","Bonheiden IGS toelage 1.679m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>toelagen",TICK),
("comm_bon_other_toelagen_2025","Bonheiden andere toelagen 2025",ENT,"Various","BBC JR2025","",2025,2025,1367858,"{2025:1367858}",0,"active","","Bonheiden other toelagen 1.368m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>toelagen",TICK),
("comm_bon_pension_jump_2025","Bonheiden pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,7650424,"{2025:7650424}",0,"active","","Bonheiden pension 7.650m JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>pension",TICK),
("comm_bon_ocmw_zero_cover_2025","Bonheiden OCMW cover ZERO 2025",ENT,"OCMW Bonheiden","BBC JR2025","",2025,2025,0,"{2025:0}",0,"active","","Bonheiden OCMW cover 0 ZERO equity -4.370m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>ocmw",TICK),
("comm_bon_invest_underspend_2025","Bonheiden invest MASSIVE underspend 2025",ENT,"Capital program","BBC JR2025","",2025,2025,3811768,"{2025:3811768}",0,"active","","Bonheiden invest 3.81 vs MJP 18.07 FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Bonheiden>invest",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_bon_invest_underspend_2025","Bonheiden invest 3.81 vs MJP 18.07 MASSIVE UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",3811768,3811768,"Invest residual dual MASSIVE underspend","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",9.5,5.5,3.5,pi(9.5,5.5,3.5),"Invest path FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_ocmw_zero_cover_2025","Bonheiden OCMW cover ZERO equity -4.37m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",5866450,0,"OCMW dual residual ZERO cover equity sink","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",9.0,5.0,3.5,pi(9.0,5.0,3.5),"Cover policy FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_pension_7_65m_2025","Bonheiden pension 7.65m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",7650424,7650424,"Pension residual dual JUMP","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",8.0,5.5,3.5,pi(8.0,5.5,3.5),"Pension FOI jump","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_toelagen_5_73m_2025","Bonheiden toelagen 5.73m IGS 1.68 police 1.95 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",5733328,5733328,"Grants residual dual","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",7.0,5.5,3.5,pi(7.0,5.5,3.5),"Named matrix FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_personnel_14_65m_2025","Bonheiden personnel 14.65m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",14645287,14645287,"Wage bill residual","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"FTE FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_afm_4_32m_2025","Bonheiden AFM +4.32m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",4322398,4322398,"AFM residual dual","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"Keep AFM path","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_fin_debt_7_09m_2025","Bonheiden fin debt 7.09m DECLINE FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",7089729,7089729,"Debt stock residual dual DECLINE","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Debt path FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
("lb_bon_agb_afm_neg_2025","Bonheiden AGB corr AFM -0.01m NEG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Bonheiden_L5",10410,10410,"AGB dual residual NEG AFM","strong",SRC,"Bonheiden residents","Local dual residual map VL JR2025","JR2025 BBC Bonheiden GEOC realized figures",6.5,3.5,3.5,pi(6.5,3.5,3.5),"AGB path FOI","active","","tick1078; primary Bonheiden JR2025; dual residual after Duffel; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Bonheiden Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.bonheiden.be/rekening-gemeente,"
    "Lokaal Bestuur Bonheiden,2026-08-11,primary_pdf,"
    "tick1078; 182p+doc; pub 05.06.2026; KBO GE 0207.534.171 / OCMW 0212.242.037; "
    "AD Ethel Van den Wijngaert FD Els Van Bever; Jacques Morrensplein 10 NIS 12005; "
    "assets 81.650m equity 63.310m fin debt 7.090m DECLINE new loans 0.359m cash JUMP 8.068m "
    "pension JUMP 7.650m AFM +4.322m BBR 8.164m budget +1.351m P&L +1.161 IMPROVING invest 3.812 vs MJP 18.070 MASSIVE "
    "toelagen 5.733m police 1.951 DROP IGS 1.679 OCMW cover 0 ZERO equity -4.370m; dual residual after Duffel"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Bonheiden,Commune de Bonheiden,Municipality of Bonheiden,municipality,vlaanderen_gov,nl,"
    "https://www.bonheiden.be,info@bonheiden.be,Jacques Morrensplein 10 2820 Bonheiden,"
    "JR2025 dual residual tick1078; KBO 0207.534.171 / OCMW 0212.242.037; assets 81.650m fin debt 7.090m DECLINE "
    "new loans 0.359m; cash JUMP 8.068m; pension JUMP 7.650m; AFM +4.322m; BBR 8.164m; budget +1.351m; "
    "OCMW cover 0 ZERO equity -4.370m; toelagen 5.733m police 1.951 DROP IGS 1.679; invest MASSIVE underspend 3.81 vs MJP 18.07; "
    "AD Ethel Van den Wijngaert FD Els Van Bever"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_bon_invest_pension_ocmw_zero_l5,Vlaanderen>Gemeenten>Bonheiden>invest_pension_ocmw_zero_L5,city_bonheiden,'
    '"Invest MASSIVE underspend 3.812 vs MJP 18.070; pension JUMP 6.593to7.650m; OCMW cover ZERO while equity '
    '-4.370m cum deficit -5.866m P&L -1.383m; toelagen 5.733m police 1.951 DROP IGS 1.679 other 1.368; '
    'AFM +4.322m budget +1.351m; AGB corr AFM -0.010",'
    '"Antwerp mun with extreme invest underspend, pension provision jump, and zero OCMW cover while OCMW '
    'equity sinks despite strong dual AFM",9,Gemeente Bonheiden,info@bonheiden.be,'
    "Jacques Morrensplein 10 2820 Bonheiden,docs/doge/foi/drafts/gap_bon_invest_pension_ocmw_zero_l5.md,ready,2026-08-11,,,,,,"
    f"comm_bon_invest_underspend_2025,lb_bon_invest_underspend_2025,{TS},{TS},"
    "tick1078; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1078":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1078: Bonheiden GE+OCMW JR2025 dual residual done; FOI "
            "gap_bon_invest_pension_ocmw_zero_l5 ready prio9; spawn rq_1079"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1078 not found")
out.append(
    [
        "rq_1079",
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
        "spawned tick1078 after Bonheiden dual residual; residual dual L5 next; progress@1080 in 1",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1078,1078,no,"
    "tick1078 Bonheiden GE+OCMW JR2025 dual residual; FOI gap_bon_invest_pension_ocmw_zero_l5 prio9 ready; "
    "assets 81.650m fin debt 7.090m DECLINE new loans 0.359m cash JUMP 8.068m pension JUMP 7.650m "
    "AFM +4.322m BBR 8.164m budget +1.351m P&L +1.161 IMPROVING invest 3.812 vs MJP 18.070 MASSIVE "
    "toelagen 5.733m police 1.951 DROP IGS 1.679 OCMW cover 0 ZERO equity -4.370m; next residual dual L5 "
    "rq_1079; progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
