"""Tick 1070 — Sint-Martens-Latem GE+OCMW JR2025 dual residual + progress@1070."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_sml_jr2025"
ENT = "city_sint_martens_latem"
TICK = "tick1070"
TS = "2026-08-11T00:30:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_sml_assets_2025",ENT,2025,64153542,"bbc_jr_realized",SRC,"strong","Assets YE2025 64.154m DROP (was 64.763m); tick1070"),
("bud_sml_equity_2025",ENT,2025,39142979,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 39.143m DROP (was 39.758m); tick1070"),
("bud_sml_debt_total_2025",ENT,2025,25010564,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 25.011m flat (was 25.005m); tick1070"),
("bud_sml_fin_debt_2025",ENT,2025,18407850,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 18.408m slight DECLINE (was 18.553m); tick1070"),
("bud_sml_fin_debt_lt_2025",ENT,2025,17554747,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 17.555m DECLINE (was 17.750m); tick1070"),
("bud_sml_fin_debt_st_due_2025",ENT,2025,853103,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 0.853m; tick1070"),
("bud_sml_new_loans_2025",ENT,2025,675668,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 0.676m mostly leasing FOI; tick1070"),
("bud_sml_aflossingen_2025",ENT,2025,820993,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 0.821m; tick1070"),
("bud_sml_cash_2025",ENT,2025,2488219,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 2.488m DROP FOI (was 3.686m); tick1070"),
("bud_sml_pension_2025",ENT,2025,3687296,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 3.687m DROP (was 4.154m); tick1070"),
("bud_sml_cap_subs_2025",ENT,2025,3767282,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 3.767m; tick1070"),
("bud_sml_fva_total_2025",ENT,2025,9554207,"bbc_jr_realized",SRC,"strong","FVA total YE2025 9.554m; tick1070"),
("bud_sml_fva_igs_2025",ENT,2025,9496976,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 9.497m; tick1070"),
("bud_sml_leasing_mva_2025",ENT,2025,1943238,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 1.943m JUMP; tick1070"),
("bud_sml_expl_rec_2025",ENT,2025,17352319,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 17.352m; tick1070"),
("bud_sml_expl_exp_2025",ENT,2025,16298222,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 16.298m; tick1070"),
("bud_sml_expl_saldo_2025",ENT,2025,1054097,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +1.054m; tick1070"),
("bud_sml_invest_exp_2025",ENT,2025,2919205,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 2.919m (MVA+subs+lease); tick1070"),
("bud_sml_invest_rec_2025",ENT,2025,622665,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.623m; tick1070"),
("bud_sml_invest_saldo_2025",ENT,2025,-2296541,"bbc_jr_realized",SRC,"strong","Investeringssaldo -2.297m; tick1070"),
("bud_sml_invest_mva_2025",ENT,2025,1895492,"bbc_jr_realized",SRC,"strong","Investeringen MVA 1.895m; tick1070"),
("bud_sml_invest_subs_granted_2025",ENT,2025,800932,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.801m FOI (IGS 0.703m); tick1070"),
("bud_sml_invest_subs_igs_2025",ENT,2025,703458,"bbc_jr_realized",SRC,"strong","Invest-subs IGS 0.703m of 0.801m FOI; tick1070"),
("bud_sml_afm_2025",ENT,2025,252840,"bbc_jr_realized",SRC,"strong","AFM +0.253m THIN FOI; tick1070"),
("bud_sml_afm_corr_2025",ENT,2025,-410421,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM -0.410m NEG HIGH FOI; tick1070"),
("bud_sml_bbr_2025",ENT,2025,2460605,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +2.461m; tick1070"),
("bud_sml_budget_result_2025",ENT,2025,-1368032,"bbc_jr_realized",SRC,"strong","Budgettair resultaat -1.368m NEG HIGH FOI; tick1070"),
("bud_sml_cum_br_2025",ENT,2025,2460605,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +2.461m; tick1070"),
("bud_sml_pnl_2025",ENT,2025,-1120799,"bbc_jr_realized",SRC,"strong","P&L -1.121m IMPROVING (was -5.213m); tick1070"),
("bud_sml_ge_expl_exp_2025",ENT,2025,14753174,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 14.753m; tick1070"),
("bud_sml_ge_expl_rec_2025",ENT,2025,16384835,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 16.385m; tick1070"),
("bud_sml_ocmw_expl_exp_2025",ENT,2025,1545048,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 1.545m; tick1070"),
("bud_sml_ocmw_expl_rec_2025",ENT,2025,967484,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 0.967m; tick1070"),
("bud_sml_ocmw_expl_gap_2025",ENT,2025,-577564,"bbc_jr_realized",SRC,"strong","OCMW expl gap ~-0.578m; tick1070"),
("bud_sml_ocmw_cover_2025",ENT,2025,577565,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 0.578m FULL; tick1070"),
("bud_sml_equity_cum_2025",ENT,2025,-6213201,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity YE2025 -6.213m WORSENING FOI (was -5.092m); tick1070"),
("bud_sml_ocmw_equity_cum_2025",ENT,2025,-62772,"bbc_jr_realized",SRC,"strong","OCMW equity cum -0.063m IMPROVING (was -0.181m; cover full); tick1070"),
("bud_sml_ge_equity_cum_2025",ENT,2025,-6150430,"bbc_jr_realized",SRC,"strong","GE equity cum -6.150m WORSENING FOI; tick1070"),
("bud_sml_personnel_2025",ENT,2025,8580236,"bbc_jr_realized",SRC,"strong","Bezoldigingen 8.580m incl education pass-through 2.390m; tick1070"),
("bud_sml_edu_pass_through_2025",ENT,2025,2390369,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 2.390m; tick1070"),
("bud_sml_toelagen_2025",ENT,2025,1967187,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 1.967m FOI residual; tick1070"),
("bud_sml_toelagen_police_2025",ENT,2025,1303367,"bbc_jr_realized",SRC,"strong","Toelage politiezone 1.303m DROP (was 1.448m); tick1070"),
("bud_sml_toelagen_fire_2025",ENT,2025,345798,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.346m; tick1070"),
("bud_sml_toelagen_other_2025",ENT,2025,318022,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.318m FOI; tick1070"),
("bud_sml_ocmw_aid_2025",ENT,2025,488493,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 0.488m; tick1070"),
("bud_sml_fiscal_2025",ENT,2025,10187434,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 10.187m; tick1070"),
("bud_sml_fiscal_ov_2025",ENT,2025,4081296,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 4.081m; tick1070"),
("bud_sml_fiscal_pb_2025",ENT,2025,4532170,"bbc_jr_realized",SRC,"strong","Aanvullende PB 4.532m JUMP; tick1070"),
("bud_sml_gemeentefonds_2025",ENT,2025,1332014,"bbc_jr_realized",SRC,"strong","Gemeentefonds 1.332m; tick1070"),
("bud_sml_interest_2025",ENT,2025,507883,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.508m JUMP FOI; tick1070"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_sml_police_toelage_2025","SML politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,1303367,"{2025:1303367}",0,"active","","SML politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>toelagen",TICK),
("comm_sml_fire_toelage_2025","SML HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,345798,"{2025:345798}",0,"active","","SML HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>toelagen",TICK),
("comm_sml_invest_subs_igs_2025","SML invest-subs IGS 2025",ENT,"IGS","BBC JR2025 T2","",2025,2025,703458,"{2025:703458}",0,"active","","SML invest-subs IGS 0.703m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>invest_subs",TICK),
("comm_sml_leasing_loans_2025","SML new leasing loans 2025",ENT,"Leasing/banks","BBC JR2025 T4","",2025,2025,675668,"{2025:675668}",0,"active","","SML new loans/leasing 0.676m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>debt",TICK),
("comm_sml_ocmw_cover_2025","SML OCMW cover full 2025",ENT,"OCMW SML","BBC JR2025","",2025,2025,577565,"{2025:577565}",0,"active","","SML OCMW cover 0.578m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>ocmw",TICK),
("comm_sml_equity_cum_neg_2025","SML equity cum NEG -6.21m 2025",ENT,"Equity residual","BBC JR2025","",2025,2025,6213201,"{2025:6213201}",0,"active","","SML equity cum -6.21m WORSENING FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>equity",TICK),
("comm_sml_afm_corr_neg_2025","SML gecorr AFM NEG -0.41m 2025",ENT,"AFM path","BBC JR2025 J2","",2025,2025,410421,"{2025:410421}",0,"active","","SML corr AFM -0.41m NEG FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Sint-Martens-Latem>afm",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_sml_afm_corr_neg_0_41m_2025","SML gecorr AFM -0.41m NEG HIGH FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",410421,410421,"AFM corr residual dual NEG","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",8.5,4.0,3.5,pi(8.5,4.0,3.5),"Correct AFM path FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_equity_cum_neg_6_21m_2025","SML equity cum -6.21m WORSENING FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",6213201,6213201,"Equity residual dual NEG","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Equity path FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_budget_neg_1_37m_2025","SML budget -1.37m NEG HIGH FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",1368032,1368032,"Budget residual dual NEG","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",8.0,5.0,3.5,pi(8.0,5.0,3.5),"Budget path FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_fin_debt_18_41m_2025","SML fin debt 18.41m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",18407850,18407850,"Debt stock residual dual","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",7.0,5.5,3.5,pi(7.0,5.5,3.5),"Debt path FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_cash_drop_2_49m_2025","SML cash 2.49m DROP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",2488219,2488219,"Cash residual dual DROP","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",7.5,5.0,3.5,pi(7.5,5.0,3.5),"Cash path FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_toelagen_1_97m_2025","SML toelagen 1.97m police 1.30 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",1967187,1967187,"Grants residual dual","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Named matrix FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_personnel_8_58m_2025","SML personnel 8.58m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",8580236,8580236,"Wage bill residual","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"FTE FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
("lb_sml_invest_subs_igs_0_70m_2025","SML invest-subs IGS 0.70m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Sint-Martens-Latem_L5",703458,703458,"Invest-subs residual dual","strong",SRC,"SML residents","Local dual residual map VL JR2025","JR2025 BBC SML GEOC realized figures",6.5,4.5,3.5,pi(6.5,4.5,3.5),"Named matrix FOI","active","","tick1070; primary SML JR2025; dual residual after Aartselaar; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Sint-Martens-Latem Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://sint-martens-latem.paddlecms.net/sites/default/files/2026-05/Jaarrekening-2025.pdf,"
    "Lokaal Bestuur Sint-Martens-Latem,2026-08-11,primary_pdf,"
    "tick1070; 243p; GR 18.05.2026 pub 21.05.2026; KBO GE 0207.542.782 / OCMW 0212.171.563; "
    "AD Pieter Delbarge FD Wim De Bruyne; Dorp 1 / Vennelaan 23 NIS 44064; "
    "assets 64.154m equity 39.143m fin debt 18.408m DECLINE new loans/leasing 0.676m cash DROP 2.488m "
    "pension DROP 3.687m AFM +0.253m thin corr AFM -0.410m NEG BBR 2.461m budget -1.368m NEG "
    "toelagen 1.967m police 1.303 invest-subs IGS 0.703m personnel 8.580m equity cum -6.213m WORSENING "
    "OCMW cover 0.578 FULL; dual residual after Aartselaar; progress@1070"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Sint-Martens-Latem,Commune de Saint-Martin-Latem,Municipality of Sint-Martens-Latem,"
    "municipality,vlaanderen_gov,nl,https://www.sint-martens-latem.be,gemeente@sint-martens-latem.be,"
    "Dorp 1 9830 Sint-Martens-Latem,"
    "JR2025 dual residual tick1070; KBO 0207.542.782 / OCMW 0212.171.563; assets 64.154m fin debt 18.408m "
    "slight DECLINE leasing new 0.676m; cash DROP 2.488m; pension DROP 3.687m; AFM +0.253m thin; "
    "corr AFM -0.410m NEG; BBR 2.461m; budget -1.368m NEG; equity cum -6.213m WORSENING; "
    "OCMW cover 0.578 FULL; toelagen 1.967m police 1.303; AD Pieter Delbarge FD Wim De Bruyne"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_sml_afm_corr_equity_budget_cash_l5,Vlaanderen>Gemeenten>Sint-Martens-Latem>afm_equity_budget_cash_L5,city_sint_martens_latem,'
    '"Gecorr AFM -0.410m NEG while raw AFM only +0.253m thin; equity cum -6.213m WORSENING (was -5.092m) with GE '
    'equity cum -6.150m; budget -1.368m NEG; cash DROP 3.686to2.488m; fin debt still 18.408m with interest 0.508m JUMP; '
    'invest-subs IGS 0.703 of 0.801; toelagen 1.967m police 1.303; leasing MVA 1.943m",'
    '"East-Flanders mun with negative corrected AFM, deepening negative equity residual, negative budget result, '
    'and cash drop while carrying ~18.4m fin debt",9,Gemeente Sint-Martens-Latem,gemeente@sint-martens-latem.be,'
    "Dorp 1 9830 Sint-Martens-Latem,docs/doge/foi/drafts/gap_sml_afm_corr_equity_budget_cash_l5.md,ready,2026-08-11,,,,,,"
    f"comm_sml_afm_corr_neg_2025,lb_sml_afm_corr_neg_0_41m_2025,{TS},{TS},"
    "tick1070; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1070":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1070: Sint-Martens-Latem GE+OCMW JR2025 dual residual done + progress@1070; FOI "
            "gap_sml_afm_corr_equity_budget_cash_l5 ready prio9; spawn rq_1071"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1070 not found")
out.append(
    [
        "rq_1071",
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
        "spawned tick1070 after SML dual residual + progress@1070; residual dual L5 next",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1070,1070,no,"
    "tick1070 Sint-Martens-Latem GE+OCMW JR2025 dual residual + progress@1070; FOI gap_sml_afm_corr_equity_budget_cash_l5 "
    "prio9 ready; assets 64.154m fin debt 18.408m cash DROP 2.488m AFM +0.253m corr AFM -0.410m NEG budget -1.368m "
    "equity cum -6.213m WORSENING OCMW cover 0.578 FULL toelagen 1.967m police 1.303; next residual dual L5 rq_1071; "
    "progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
