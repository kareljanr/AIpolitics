"""Tick 1075 — Lennik GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_lennik_jr2025"
ENT = "city_lennik"
TICK = "tick1075"
TS = "2026-08-11T03:00:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_len_assets_2025",ENT,2025,53454580,"bbc_jr_realized",SRC,"strong","Assets YE2025 53.455m (was 53.273m); tick1075"),
("bud_len_equity_2025",ENT,2025,35200324,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 35.200m (was 34.932m); tick1075"),
("bud_len_debt_total_2025",ENT,2025,18254256,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 18.254m slight DECLINE (was 18.341m); tick1075"),
("bud_len_fin_debt_2025",ENT,2025,11461329,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 11.461m DECLINE (was 12.541m); tick1075"),
("bud_len_fin_debt_lt_2025",ENT,2025,10286556,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 10.287m DECLINE (was 11.384m); tick1075"),
("bud_len_fin_debt_st_due_2025",ENT,2025,1174772,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 1.175m; tick1075"),
("bud_len_new_loans_2025",ENT,2025,80892,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 0.081m LOW; tick1075"),
("bud_len_aflossingen_2025",ENT,2025,1137438,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 1.137m; tick1075"),
("bud_len_cash_2025",ENT,2025,2862037,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 2.862m JUMP (was 2.332m); tick1075"),
("bud_len_pension_2025",ENT,2025,3828352,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 3.828m JUMP FOI (was 3.251m); tick1075"),
("bud_len_cap_subs_2025",ENT,2025,5626870,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 5.627m; tick1075"),
("bud_len_fva_total_2025",ENT,2025,11673867,"bbc_jr_realized",SRC,"strong","FVA total YE2025 11.674m; tick1075"),
("bud_len_fva_igs_2025",ENT,2025,10252480,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 10.252m; tick1075"),
("bud_len_leasing_mva_2025",ENT,2025,641676,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 0.642m; tick1075"),
("bud_len_expl_rec_2025",ENT,2025,20370636,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 20.371m; tick1075"),
("bud_len_expl_exp_2025",ENT,2025,17658589,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 17.659m; tick1075"),
("bud_len_expl_saldo_2025",ENT,2025,2712048,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +2.712m STRONG; tick1075"),
("bud_len_invest_exp_2025",ENT,2025,2055780,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 2.056m vs MJP 5.430m MASSIVE UNDERSPEND FOI; tick1075"),
("bud_len_invest_rec_2025",ENT,2025,233298,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.233m; tick1075"),
("bud_len_invest_saldo_2025",ENT,2025,-1822482,"bbc_jr_realized",SRC,"strong","Investeringssaldo -1.822m; tick1075"),
("bud_len_mjp_invest_planned_2025",ENT,2025,5429943,"bbc_jr_realized",SRC,"strong","MJP invest planned 5.430m vs realized 2.056m underspend FOI; tick1075"),
("bud_len_invest_mva_2025",ENT,2025,1875585,"bbc_jr_realized",SRC,"strong","Investeringen MVA 1.876m; tick1075"),
("bud_len_invest_subs_granted_2025",ENT,2025,66353,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.066m; tick1075"),
("bud_len_afm_2025",ENT,2025,1574609,"bbc_jr_realized",SRC,"strong","AFM +1.575m STRONG; tick1075"),
("bud_len_afm_corr_2025",ENT,2025,1708769,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +1.709m STRONG; tick1075"),
("bud_len_bbr_2025",ENT,2025,1745650,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +1.746m; tick1075"),
("bud_len_budget_result_2025",ENT,2025,-169981,"bbc_jr_realized",SRC,"strong","Budgettair resultaat -0.170m NEG FOI; tick1075"),
("bud_len_cum_br_2025",ENT,2025,2243136,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +2.243m; tick1075"),
("bud_len_onbeschikbaar_2025",ENT,2025,497486,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.497m; tick1075"),
("bud_len_pnl_2025",ENT,2025,317027,"bbc_jr_realized",SRC,"strong","P&L +0.317m IMPROVING (was -0.653m); tick1075"),
("bud_len_ge_expl_exp_2025",ENT,2025,13900602,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 13.901m; tick1075"),
("bud_len_ge_expl_rec_2025",ENT,2025,17607919,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 17.608m; tick1075"),
("bud_len_ocmw_expl_exp_2025",ENT,2025,3757987,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 3.758m; tick1075"),
("bud_len_ocmw_expl_rec_2025",ENT,2025,2762717,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 2.763m; tick1075"),
("bud_len_ocmw_expl_gap_2025",ENT,2025,-995270,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -0.995m; tick1075"),
("bud_len_ocmw_cover_2025",ENT,2025,996733,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 0.997m FULL (budget result principle); tick1075"),
("bud_len_equity_cum_2025",ENT,2025,11594778,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +11.595m; tick1075"),
("bud_len_personnel_2025",ENT,2025,8841354,"bbc_jr_realized",SRC,"strong","Bezoldigingen 8.841m incl education pass-through 1.875m; tick1075"),
("bud_len_edu_pass_through_2025",ENT,2025,1874903,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 1.875m; tick1075"),
("bud_len_toelagen_2025",ENT,2025,2919855,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 2.920m FOI residual; tick1075"),
("bud_len_toelagen_police_2025",ENT,2025,1568716,"bbc_jr_realized",SRC,"strong","Toelage politiezone 1.569m; tick1075"),
("bud_len_toelagen_fire_2025",ENT,2025,679599,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.680m; tick1075"),
("bud_len_toelagen_igs_2025",ENT,2025,33035,"bbc_jr_realized",SRC,"strong","Toelage IGS 0.033m; tick1075"),
("bud_len_toelagen_other_2025",ENT,2025,638505,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.639m FOI; tick1075"),
("bud_len_ocmw_aid_2025",ENT,2025,1037133,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 1.037m; tick1075"),
("bud_len_fiscal_2025",ENT,2025,10605555,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 10.606m; tick1075"),
("bud_len_fiscal_ov_2025",ENT,2025,3238750,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 3.239m; tick1075"),
("bud_len_fiscal_pb_2025",ENT,2025,6442339,"bbc_jr_realized",SRC,"strong","Aanvullende PB 6.442m JUMP; tick1075"),
("bud_len_gemeentefonds_2025",ENT,2025,2539369,"bbc_jr_realized",SRC,"strong","Gemeentefonds 2.539m; tick1075"),
("bud_len_interest_2025",ENT,2025,388989,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.389m; tick1075"),
("bud_len_debt_per_inhab_2025",ENT,2025,1220,"bbc_jr_realized",SRC,"strong","Fin debt per inwoner EUR1220; tick1075"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_len_police_toelage_2025","Lennik politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,1568716,"{2025:1568716}",0,"active","","Lennik politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>toelagen",TICK),
("comm_len_fire_toelage_2025","Lennik HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,679599,"{2025:679599}",0,"active","","Lennik HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>toelagen",TICK),
("comm_len_other_toelagen_2025","Lennik andere toelagen 2025",ENT,"Various","BBC JR2025","",2025,2025,638505,"{2025:638505}",0,"active","","Lennik other toelagen 0.639m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>toelagen",TICK),
("comm_len_pension_jump_2025","Lennik pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,3828352,"{2025:3828352}",0,"active","","Lennik pension 3.828m JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>pension",TICK),
("comm_len_ocmw_cover_2025","Lennik OCMW cover full 2025",ENT,"OCMW Lennik","BBC JR2025","",2025,2025,996733,"{2025:996733}",0,"active","","Lennik OCMW cover 0.997m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Lennik>ocmw",TICK),
("comm_len_invest_underspend_2025","Lennik invest underspend 2025",ENT,"Capital program","BBC JR2025","",2025,2025,2055780,"{2025:2055780}",0,"active","","Lennik invest 2.06 vs MJP 5.43 FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>invest",TICK),
("comm_len_budget_neg_2025","Lennik budget NEG -0.17m 2025",ENT,"Budget path","BBC JR2025 J2","",2025,2025,169981,"{2025:169981}",0,"active","","Lennik budget -0.17m NEG FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lennik>budget",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_len_invest_underspend_2025","Lennik invest 2.06 vs MJP 5.43 MASSIVE UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",2055780,2055780,"Invest residual dual underspend","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",8.0,5.0,3.5,pi(8.0,5.0,3.5),"Invest path FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_toelagen_2_92m_2025","Lennik toelagen 2.92m police 1.57 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",2919855,2919855,"Grants residual dual","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Named matrix FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_pension_jump_3_83m_2025","Lennik pension 3.83m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",3828352,3828352,"Pension residual dual JUMP","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",7.5,5.0,3.5,pi(7.5,5.0,3.5),"Pension FOI jump","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_fin_debt_11_46m_2025","Lennik fin debt 11.46m DECLINE FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",11461329,11461329,"Debt stock residual dual DECLINE","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"Debt path FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_personnel_8_84m_2025","Lennik personnel 8.84m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",8841354,8841354,"Wage bill residual","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"FTE FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_afm_1_57m_2025","Lennik AFM +1.57m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",1574609,1574609,"AFM residual dual","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_budget_neg_0_17m_2025","Lennik budget -0.17m NEG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",169981,169981,"Budget residual dual NEG","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",7.0,4.0,3.5,pi(7.0,4.0,3.5),"Budget path FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
("lb_len_ocmw_cover_1_00m_2025","Lennik OCMW cover 1.00m FULL FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lennik_L5",996733,996733,"OCMW dual residual FULL cover","strong",SRC,"Lennik residents","Local dual residual map VL JR2025","JR2025 BBC Lennik GEOC realized figures",6.5,4.5,3.5,pi(6.5,4.5,3.5),"Cover policy FOI","active","","tick1075; primary Lennik JR2025; dual residual after Hoeilaart; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Lennik Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.lennik.be/bekendmakingen/detail/36/jaarrekening,"
    "Lokaal Bestuur Lennik,2026-08-11,primary_pdf,"
    "tick1075; 186p; pub 18.06.2026; KBO GE 0216.769.264 / OCMW 0216.769.363; "
    "AD Anaïs Nies FD Patrick Bombaert; Markt 18 NIS 23045; "
    "assets 53.455m equity 35.200m fin debt 11.461m DECLINE new loans 0.081m cash JUMP 2.862m "
    "pension JUMP 3.828m AFM +1.575m BBR 1.746m budget -0.170m NEG invest 2.056 vs MJP 5.430 "
    "toelagen 2.920m police 1.569 personnel 8.841m OCMW cover 0.997 FULL; dual residual after Hoeilaart"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Lennik,Commune de Lennik,Municipality of Lennik,municipality,vlaanderen_gov,nl,"
    "https://www.lennik.be,info@lennik.be,Markt 18 1750 Lennik,"
    "JR2025 dual residual tick1075; KBO 0216.769.264 / OCMW 0216.769.363; assets 53.455m fin debt 11.461m DECLINE "
    "new loans 0.081m; cash JUMP 2.862m; pension JUMP 3.828m; AFM +1.575m; BBR 1.746m; budget -0.170m NEG; "
    "OCMW cover 0.997 FULL; toelagen 2.920m police 1.569; invest underspend 2.06 vs MJP 5.43; "
    "AD Anaïs Nies FD Patrick Bombaert"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_len_invest_pension_budget_toelagen_l5,Vlaanderen>Gemeenten>Lennik>invest_pension_budget_toelagen_L5,city_lennik,'
    '"Invest underspend 2.056 vs MJP 5.430 MASSIVE; pension JUMP 3.251to3.828m; budget -0.170m NEG despite AFM '
    '+1.575m and expl +2.712m; toelagen 2.920m police 1.569 other 0.639; OCMW cover 0.997 FULL on budget-result '
    'principle; new loans only 0.081m with fin debt DECLINE to 11.461m",'
    '"Flemish Brabant mun with massive invest underspend, pension provision jump, and negative budget result '
    'despite strong structural AFM",9,Gemeente Lennik,info@lennik.be,'
    "Markt 18 1750 Lennik,docs/doge/foi/drafts/gap_len_invest_pension_budget_toelagen_l5.md,ready,2026-08-11,,,,,,"
    f"comm_len_invest_underspend_2025,lb_len_invest_underspend_2025,{TS},{TS},"
    "tick1075; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1075":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1075: Lennik GE+OCMW JR2025 dual residual done; FOI "
            "gap_len_invest_pension_budget_toelagen_l5 ready prio9; spawn rq_1076"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1075 not found")
out.append(
    [
        "rq_1076",
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
        "spawned tick1075 after Lennik dual residual; residual dual L5 next; progress@1080 in 4",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1075,1075,no,"
    "tick1075 Lennik GE+OCMW JR2025 dual residual; FOI gap_len_invest_pension_budget_toelagen_l5 prio9 ready; "
    "assets 53.455m fin debt 11.461m DECLINE new loans 0.081m cash JUMP 2.862m pension JUMP 3.828m AFM +1.575m "
    "BBR 1.746m budget -0.170m NEG invest 2.056 vs MJP 5.430 toelagen 2.920m police 1.569 personnel 8.841m "
    "OCMW cover 0.997 FULL; next residual dual L5 rq_1076; progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
