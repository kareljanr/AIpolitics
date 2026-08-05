"""Tick 1073 — Ternat GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_ternat_jr2025"
ENT = "city_ternat"
TICK = "tick1073"
TS = "2026-08-11T02:00:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_ter_assets_2025",ENT,2025,81552241,"bbc_jr_realized",SRC,"strong","Assets YE2025 81.552m JUMP (was 78.225m); tick1073"),
("bud_ter_equity_2025",ENT,2025,47377115,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 47.377m JUMP (was 45.705m); tick1073"),
("bud_ter_debt_total_2025",ENT,2025,34175126,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 34.175m JUMP (was 32.519m); tick1073"),
("bud_ter_fin_debt_2025",ENT,2025,23475372,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 23.475m slight JUMP (was 23.220m); tick1073"),
("bud_ter_fin_debt_lt_2025",ENT,2025,21824298,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 21.824m; tick1073"),
("bud_ter_fin_debt_st_due_2025",ENT,2025,1651074,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 1.651m; tick1073"),
("bud_ter_new_loans_2025",ENT,2025,2311240,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 2.311m FOI; tick1073"),
("bud_ter_aflossingen_2025",ENT,2025,2055953,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 2.056m; tick1073"),
("bud_ter_cash_2025",ENT,2025,4195950,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 4.196m JUMP (was 3.002m); tick1073"),
("bud_ter_pension_2025",ENT,2025,5880860,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 5.881m DROP (was 6.076m); tick1073"),
("bud_ter_cap_subs_2025",ENT,2025,4163979,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 4.164m; tick1073"),
("bud_ter_fva_total_2025",ENT,2025,16976025,"bbc_jr_realized",SRC,"strong","FVA total YE2025 16.976m; tick1073"),
("bud_ter_fva_igs_2025",ENT,2025,15646665,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 15.647m; tick1073"),
("bud_ter_leasing_mva_2025",ENT,2025,9294848,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 9.295m HIGH FOI; tick1073"),
("bud_ter_expl_rec_2025",ENT,2025,29811301,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 29.811m; tick1073"),
("bud_ter_expl_exp_2025",ENT,2025,26437314,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 26.437m; tick1073"),
("bud_ter_expl_saldo_2025",ENT,2025,3373987,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +3.374m STRONG; tick1073"),
("bud_ter_invest_exp_2025",ENT,2025,4848169,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 4.848m vs MJP 5.047m; tick1073"),
("bud_ter_invest_rec_2025",ENT,2025,1156096,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 1.156m; tick1073"),
("bud_ter_invest_saldo_2025",ENT,2025,-3692074,"bbc_jr_realized",SRC,"strong","Investeringssaldo -3.692m; tick1073"),
("bud_ter_invest_mva_2025",ENT,2025,4560598,"bbc_jr_realized",SRC,"strong","Investeringen MVA 4.561m; tick1073"),
("bud_ter_invest_subs_granted_2025",ENT,2025,251031,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.251m; tick1073"),
("bud_ter_afm_2025",ENT,2025,1455399,"bbc_jr_realized",SRC,"strong","AFM +1.455m STRONG; tick1073"),
("bud_ter_afm_corr_2025",ENT,2025,1653745,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +1.654m STRONG; tick1073"),
("bud_ter_bbr_2025",ENT,2025,3686463,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +3.686m; tick1073"),
("bud_ter_budget_result_2025",ENT,2025,13009,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +0.013m THIN FOI (near zero); tick1073"),
("bud_ter_cum_br_2025",ENT,2025,3873130,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +3.873m; tick1073"),
("bud_ter_onbeschikbaar_2025",ENT,2025,186667,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.187m; tick1073"),
("bud_ter_pnl_2025",ENT,2025,794856,"bbc_jr_realized",SRC,"strong","P&L +0.795m IMPROVING (was -2.040m); tick1073"),
("bud_ter_ge_expl_exp_2025",ENT,2025,22137490,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven 22.137m; tick1073"),
("bud_ter_ge_expl_rec_2025",ENT,2025,27729808,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten 27.730m; tick1073"),
("bud_ter_ocmw_expl_exp_2025",ENT,2025,4299825,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven 4.300m; tick1073"),
("bud_ter_ocmw_expl_rec_2025",ENT,2025,2081493,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten 2.081m; tick1073"),
("bud_ter_ocmw_expl_gap_2025",ENT,2025,-2218332,"bbc_jr_realized",SRC,"strong","OCMW expl gap -2.218m HIGH FOI; tick1073"),
("bud_ter_ocmw_cover_2025",ENT,2025,2295509,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 2.296m FULL; tick1073"),
("bud_ter_equity_cum_2025",ENT,2025,4645297,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +4.645m; tick1073"),
("bud_ter_ocmw_equity_cum_2025",ENT,2025,-1565740,"bbc_jr_realized",SRC,"strong","OCMW equity cum -1.566m WORSENING FOI (was -1.281m; cover full); tick1073"),
("bud_ter_ge_equity_cum_2025",ENT,2025,6211037,"bbc_jr_realized",SRC,"strong","GE equity cum +6.211m; tick1073"),
("bud_ter_personnel_2025",ENT,2025,14218885,"bbc_jr_realized",SRC,"strong","Bezoldigingen 14.219m JUMP incl education pass-through 2.891m JUMP; tick1073"),
("bud_ter_edu_pass_through_2025",ENT,2025,2890810,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 2.891m JUMP (was 2.085m); tick1073"),
("bud_ter_toelagen_2025",ENT,2025,5263093,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 5.263m FOI residual; tick1073"),
("bud_ter_toelagen_police_2025",ENT,2025,2487876,"bbc_jr_realized",SRC,"strong","Toelage politiezone 2.488m JUMP (was 2.208m); tick1073"),
("bud_ter_toelagen_fire_2025",ENT,2025,1045688,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 1.046m; tick1073"),
("bud_ter_toelagen_igs_2025",ENT,2025,925792,"bbc_jr_realized",SRC,"strong","Toelage IGS 0.926m FOI; tick1073"),
("bud_ter_toelagen_agb_2025",ENT,2025,385391,"bbc_jr_realized",SRC,"strong","Toelage AGB 0.385m dual residual; tick1073"),
("bud_ter_toelagen_other_2025",ENT,2025,418346,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.418m FOI; tick1073"),
("bud_ter_ocmw_aid_2025",ENT,2025,1750906,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 1.751m HIGH; tick1073"),
("bud_ter_fiscal_2025",ENT,2025,16732611,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 16.733m; tick1073"),
("bud_ter_fiscal_ov_2025",ENT,2025,7567001,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 7.567m; tick1073"),
("bud_ter_fiscal_pb_2025",ENT,2025,7962798,"bbc_jr_realized",SRC,"strong","Aanvullende PB 7.963m JUMP; tick1073"),
("bud_ter_gemeentefonds_2025",ENT,2025,4358798,"bbc_jr_realized",SRC,"strong","Gemeentefonds 4.359m; tick1073"),
("bud_ter_interest_2025",ENT,2025,776001,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.776m JUMP FOI; tick1073"),
("bud_ter_agb_afm_2025",ENT,2025,-12074,"bbc_jr_realized",SRC,"strong","AGB AFM -0.012m NEG dual residual FOI; tick1073"),
("bud_ter_debt_per_inhab_2025",ENT,2025,1406,"bbc_jr_realized",SRC,"strong","Openstaande schuld per inwoner EUR1406; tick1073"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_ter_police_toelage_2025","Ternat politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,2487876,"{2025:2487876}",0,"active","","Ternat politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>toelagen",TICK),
("comm_ter_fire_toelage_2025","Ternat HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,1045688,"{2025:1045688}",0,"active","","Ternat HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>toelagen",TICK),
("comm_ter_igs_toelage_2025","Ternat IGS toelage 2025",ENT,"IGS","BBC JR2025","",2025,2025,925792,"{2025:925792}",0,"active","","Ternat IGS toelage 0.926m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>toelagen",TICK),
("comm_ter_agb_toelage_2025","Ternat AGB toelage 2025",ENT,"AGB Ternat","BBC JR2025","",2025,2025,385391,"{2025:385391}",0,"active","","Ternat AGB toelage 2025 dual","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>toelagen",TICK),
("comm_ter_new_loans_2025","Ternat nieuwe leningen 2025",ENT,"Banks","BBC JR2025 T4","",2025,2025,2311240,"{2025:2311240}",0,"active","","Ternat new loans 2.311m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>debt",TICK),
("comm_ter_ocmw_cover_2025","Ternat OCMW cover full 2025",ENT,"OCMW Ternat","BBC JR2025","",2025,2025,2295509,"{2025:2295509}",0,"active","","Ternat OCMW cover 2.296m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Ternat>ocmw",TICK),
("comm_ter_ocmw_equity_neg_2025","Ternat OCMW equity cum NEG -1.57m 2025",ENT,"OCMW Ternat","BBC JR2025","",2025,2025,1565740,"{2025:1565740}",0,"active","","Ternat OCMW equity -1.57m WORSENING FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Ternat>ocmw",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_ter_ocmw_equity_neg_1_57m_2025","Ternat OCMW equity cum -1.57m WORSENING despite cover 2.30m FULL FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",1565740,1565740,"OCMW dual residual NEG despite FULL cover","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Cover vs equity path FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_toelagen_5_26m_2025","Ternat toelagen 5.26m police 2.49 IGS 0.93 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",5263093,5263093,"Grants residual dual","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Named matrix FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_fin_debt_23_48m_2025","Ternat fin debt 23.48m loans 2.31m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",23475372,23475372,"Debt stock residual dual","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",7.0,5.5,3.5,pi(7.0,5.5,3.5),"Debt path FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_personnel_14_22m_2025","Ternat personnel 14.22m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",14218885,14218885,"Wage bill residual JUMP","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"FTE FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_leasing_mva_9_30m_2025","Ternat leasing MVA 9.30m HIGH FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",9294848,9294848,"Leasing residual dual","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Leasing FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_interest_jump_0_78m_2025","Ternat interest 0.78m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",776001,776001,"Interest residual dual JUMP","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",7.0,4.5,3.5,pi(7.0,4.5,3.5),"Interest path FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_afm_1_46m_2025","Ternat AFM +1.46m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",1455399,1455399,"AFM residual dual","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
("lb_ter_budget_thin_0_01m_2025","Ternat budget +0.013m THIN FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Ternat_L5",13009,13009,"Budget residual dual THIN","strong",SRC,"Ternat residents","Local dual residual map VL JR2025","JR2025 BBC Ternat GEOC realized figures",7.0,3.5,3.5,pi(7.0,3.5,3.5),"Budget path FOI","active","","tick1073; primary Ternat JR2025; dual residual after Roosdaal; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Ternat Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.ternat.be/beleidsdocumenten,"
    "Lokaal Bestuur Ternat,2026-08-11,primary_pdf,"
    "tick1073; 404p; GR+RMW 28.05.2026; KBO GE 0207.514.276 / OCMW 0212.174.434; "
    "AD Sieglinde De Mulder FD Jorn Buggenhoudt; Gemeentehuisstraat 21 NIS 23086; "
    "assets 81.552m equity 47.377m fin debt 23.475m new loans 2.311m cash JUMP 4.196m "
    "pension DROP 5.881m AFM +1.455m BBR 3.686m budget +0.013m THIN invest 4.848 "
    "toelagen 5.263m police 2.488 IGS 0.926 AGB 0.385 personnel 14.219m "
    "OCMW cover 2.296 FULL OCMW equity cum -1.566m WORSENING; leasing MVA 9.295m; "
    "AGB AFM -0.012 NEG dual; dual residual after Roosdaal"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Ternat,Commune de Ternat,Municipality of Ternat,municipality,vlaanderen_gov,nl,"
    "https://www.ternat.be,info@ternat.be,Gemeentehuisstraat 21 1740 Ternat,"
    "JR2025 dual residual tick1073; KBO 0207.514.276 / OCMW 0212.174.434; assets 81.552m fin debt 23.475m "
    "new loans 2.311m; cash JUMP 4.196m; pension DROP 5.881m; AFM +1.455m; BBR 3.686m; budget +0.013m THIN; "
    "OCMW cover 2.296 FULL OCMW equity cum -1.566m WORSENING; toelagen 5.263m police 2.488 IGS 0.926; "
    "leasing MVA 9.295m; AD Sieglinde De Mulder FD Jorn Buggenhoudt"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_ter_ocmw_equity_toelagen_leasing_l5,Vlaanderen>Gemeenten>Ternat>ocmw_equity_toelagen_leasing_L5,city_ternat,'
    '"OCMW equity cum -1.566m WORSENING (was -1.281m) despite cover 2.296m FULL and expl gap -2.218m; toelagen '
    '5.263m police JUMP 2.208to2.488 IGS 0.926 AGB 0.385; leasing MVA 9.295m; interest JUMP 0.776m; budget '
    '+0.013m THIN near zero; personnel JUMP 14.219m edu pass-through 2.891m; new loans 2.311m; AGB AFM -0.012 NEG",'
    '"Flemish Brabant mun with FULL OCMW cover that still fails to stop deepening OCMW equity residual, '
    'large grant matrix, high leasing stock, and thin budget result",9,Gemeente Ternat,info@ternat.be,'
    "Gemeentehuisstraat 21 1740 Ternat,docs/doge/foi/drafts/gap_ter_ocmw_equity_toelagen_leasing_l5.md,ready,2026-08-11,,,,,,"
    f"comm_ter_ocmw_equity_neg_2025,lb_ter_ocmw_equity_neg_1_57m_2025,{TS},{TS},"
    "tick1073; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1073":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1073: Ternat GE+OCMW JR2025 dual residual done; FOI "
            "gap_ter_ocmw_equity_toelagen_leasing_l5 ready prio9; spawn rq_1074"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1073 not found")
out.append(
    [
        "rq_1074",
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
        "spawned tick1073 after Ternat dual residual; residual dual L5 next; progress@1080 in 6",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1073,1073,no,"
    "tick1073 Ternat GE+OCMW JR2025 dual residual; FOI gap_ter_ocmw_equity_toelagen_leasing_l5 prio9 ready; "
    "assets 81.552m fin debt 23.475m new loans 2.311m cash JUMP 4.196m pension DROP 5.881m AFM +1.455m "
    "BBR 3.686m budget +0.013m THIN invest 4.848 toelagen 5.263m police 2.488 IGS 0.926 personnel 14.219m "
    "OCMW cover 2.296 FULL equity cum -1.566m WORSENING leasing MVA 9.295m; next residual dual L5 rq_1074; "
    "progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
