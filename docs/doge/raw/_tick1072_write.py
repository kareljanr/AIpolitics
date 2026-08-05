"""Tick 1072 — Roosdaal GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_roosdaal_jr2025"
ENT = "city_roosdaal"
TICK = "tick1072"
TS = "2026-08-11T01:30:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_roo_assets_2025",ENT,2025,66736527,"bbc_jr_realized",SRC,"strong","Assets YE2025 66.737m JUMP (was 61.258m); tick1072"),
("bud_roo_equity_2025",ENT,2025,42830881,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 42.831m JUMP (was 39.312m); tick1072"),
("bud_roo_debt_total_2025",ENT,2025,23905646,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 23.906m JUMP (was 21.947m); tick1072"),
("bud_roo_fin_debt_2025",ENT,2025,13978949,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 13.979m JUMP (was 10.829m); tick1072"),
("bud_roo_fin_debt_lt_2025",ENT,2025,12884435,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 12.884m JUMP (was 9.831m); tick1072"),
("bud_roo_fin_debt_st_due_2025",ENT,2025,1094514,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 1.095m; tick1072"),
("bud_roo_new_loans_2025",ENT,2025,4196348,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 4.196m JUMP FOI; tick1072"),
("bud_roo_aflossingen_2025",ENT,2025,1046243,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 1.046m; tick1072"),
("bud_roo_mjp_new_loans_2026",ENT,2025,118369,"bbc_jr_realized",SRC,"strong","MJP new loans 2026 planned 0.118m; tick1072"),
("bud_roo_mjp_new_loans_2027",ENT,2025,3117000,"bbc_jr_realized",SRC,"strong","MJP new loans 2027 planned 3.117m FOI; tick1072"),
("bud_roo_mjp_fin_debt_2027",ENT,2025,15127816,"bbc_jr_realized",SRC,"strong","MJP fin debt YE2027 planned 15.128m; tick1072"),
("bud_roo_cash_2025",ENT,2025,4730633,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 4.731m (was 4.439m); tick1072"),
("bud_roo_pension_2025",ENT,2025,6814544,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 6.815m DROP (was 7.759m); tick1072"),
("bud_roo_cap_subs_2025",ENT,2025,7183757,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 7.184m; tick1072"),
("bud_roo_fva_total_2025",ENT,2025,7357271,"bbc_jr_realized",SRC,"strong","FVA total YE2025 7.357m; tick1072"),
("bud_roo_fva_igs_2025",ENT,2025,5641272,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 5.641m; tick1072"),
("bud_roo_leasing_mva_2025",ENT,2025,1058769,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 1.059m; tick1072"),
("bud_roo_expl_rec_2025",ENT,2025,20130304,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 20.130m; tick1072"),
("bud_roo_expl_exp_2025",ENT,2025,17218504,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 17.219m; tick1072"),
("bud_roo_expl_saldo_2025",ENT,2025,2911801,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +2.912m STRONG; tick1072"),
("bud_roo_invest_exp_2025",ENT,2025,6423521,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 6.424m vs MJP 13.701m MASSIVE UNDERSPEND FOI; tick1072"),
("bud_roo_invest_rec_2025",ENT,2025,2426901,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 2.427m; tick1072"),
("bud_roo_invest_saldo_2025",ENT,2025,-3996620,"bbc_jr_realized",SRC,"strong","Investeringssaldo -3.997m; tick1072"),
("bud_roo_mjp_invest_planned_2025",ENT,2025,13700518,"bbc_jr_realized",SRC,"strong","MJP invest planned 13.701m vs realized 6.424m underspend FOI; tick1072"),
("bud_roo_invest_mva_2025",ENT,2025,5826074,"bbc_jr_realized",SRC,"strong","Investeringen MVA 5.826m; tick1072"),
("bud_roo_invest_subs_granted_2025",ENT,2025,543569,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.544m FOI; tick1072"),
("bud_roo_afm_2025",ENT,2025,1945255,"bbc_jr_realized",SRC,"strong","AFM +1.945m STRONG (MJP only 0.088m); tick1072"),
("bud_roo_afm_corr_2025",ENT,2025,2125191,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +2.125m STRONG; tick1072"),
("bud_roo_bbr_2025",ENT,2025,5071230,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +5.071m; tick1072"),
("bud_roo_budget_result_2025",ENT,2025,1994821,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +1.995m STRONG (MJP was -1.206m); tick1072"),
("bud_roo_cum_br_2025",ENT,2025,5611994,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +5.612m; tick1072"),
("bud_roo_onbeschikbaar_2025",ENT,2025,540763,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.541m; tick1072"),
("bud_roo_pnl_2025",ENT,2025,2378661,"bbc_jr_realized",SRC,"strong","P&L +2.379m STRONG (was +1.289m); tick1072"),
("bud_roo_ge_expl_exp_2025",ENT,2025,15888876,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 15.889m; tick1072"),
("bud_roo_ge_expl_rec_2025",ENT,2025,19687703,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 19.688m; tick1072"),
("bud_roo_ocmw_expl_exp_2025",ENT,2025,1329628,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 1.330m; tick1072"),
("bud_roo_ocmw_expl_rec_2025",ENT,2025,442602,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 0.443m; tick1072"),
("bud_roo_ocmw_expl_gap_2025",ENT,2025,-887026,"bbc_jr_realized",SRC,"strong","OCMW expl gap -0.887m HIGH FOI; tick1072"),
("bud_roo_ocmw_cover_2025",ENT,2025,0,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 0 ZERO FOI; tick1072"),
("bud_roo_equity_cum_2025",ENT,2025,6213024,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +6.213m JUMP; tick1072"),
("bud_roo_ocmw_equity_cum_2025",ENT,2025,-1236587,"bbc_jr_realized",SRC,"strong","OCMW equity cum -1.237m WORSENING FOI (was -1.112m; cover 0); tick1072"),
("bud_roo_ge_equity_cum_2025",ENT,2025,7449611,"bbc_jr_realized",SRC,"strong","GE equity cum +7.450m JUMP; tick1072"),
("bud_roo_personnel_2025",ENT,2025,9187165,"bbc_jr_realized",SRC,"strong","Bezoldigingen 9.187m incl education pass-through 2.718m; tick1072"),
("bud_roo_edu_pass_through_2025",ENT,2025,2717661,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 2.718m; tick1072"),
("bud_roo_toelagen_2025",ENT,2025,3084138,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 3.084m FOI residual; tick1072"),
("bud_roo_toelagen_police_2025",ENT,2025,1614387,"bbc_jr_realized",SRC,"strong","Toelage politiezone 1.614m JUMP (was 1.433m); tick1072"),
("bud_roo_toelagen_fire_2025",ENT,2025,717287,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.717m; tick1072"),
("bud_roo_toelagen_agb_2025",ENT,2025,322740,"bbc_jr_realized",SRC,"strong","Toelage AGB 0.323m dual residual; tick1072"),
("bud_roo_toelagen_other_2025",ENT,2025,429724,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+IGS residual 0.430m FOI; tick1072"),
("bud_roo_ocmw_aid_2025",ENT,2025,288307,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 0.288m; tick1072"),
("bud_roo_fiscal_2025",ENT,2025,10417671,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 10.418m; tick1072"),
("bud_roo_fiscal_ov_2025",ENT,2025,3102344,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 3.102m; tick1072"),
("bud_roo_fiscal_pb_2025",ENT,2025,6557114,"bbc_jr_realized",SRC,"strong","Aanvullende PB 6.557m JUMP; tick1072"),
("bud_roo_gemeentefonds_2025",ENT,2025,2931880,"bbc_jr_realized",SRC,"strong","Gemeentefonds 2.932m; tick1072"),
("bud_roo_interest_2025",ENT,2025,294689,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.295m; tick1072"),
("bud_roo_agb_afm_2025",ENT,2025,-40556,"bbc_jr_realized",SRC,"strong","AGB AFM -0.041m NEG dual residual FOI; tick1072"),
("bud_roo_agb_afm_corr_2025",ENT,2025,-271390,"bbc_jr_realized",SRC,"strong","AGB gecorr AFM -0.271m NEG dual residual FOI; tick1072"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_roo_police_toelage_2025","Roosdaal politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,1614387,"{2025:1614387}",0,"active","","Roosdaal politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>toelagen",TICK),
("comm_roo_fire_toelage_2025","Roosdaal HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,717287,"{2025:717287}",0,"active","","Roosdaal HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>toelagen",TICK),
("comm_roo_agb_toelage_2025","Roosdaal AGB toelage 2025",ENT,"AGB Roosdaal","BBC JR2025","",2025,2025,322740,"{2025:322740}",0,"active","","Roosdaal AGB toelage 2025 dual","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>toelagen",TICK),
("comm_roo_new_loans_2025","Roosdaal nieuwe leningen 2025",ENT,"Banks","BBC JR2025 T4","",2025,2025,4196348,"{2025:4196348}",0,"active","","Roosdaal new loans 4.196m JUMP FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>debt",TICK),
("comm_roo_mjp_loans_2027","Roosdaal MJP new loans 2027 planned",ENT,"Banks","BBC JR2025 T4","",2027,2027,3117000,"{2027:3117000}",3117000,"active","","Roosdaal MJP loans 2027 3.117m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>debt",TICK),
("comm_roo_ocmw_gap_2025","Roosdaal OCMW expl gap cover-zero 2025",ENT,"OCMW Roosdaal","BBC JR2025","",2025,2025,887026,"{2025:887026}",0,"active","","Roosdaal OCMW gap cover 0 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>ocmw",TICK),
("comm_roo_agb_afm_neg_2025","Roosdaal AGB corr AFM NEG 2025",ENT,"AGB Roosdaal","BBC JR2025 J2 dual","",2025,2025,271390,"{2025:271390}",0,"active","","Roosdaal AGB corr AFM -0.271m NEG","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Roosdaal>agb",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_roo_ocmw_cover_zero_1_24m_2025","Roosdaal OCMW cover 0 equity cum -1.24m WORSENING FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",1236587,1236587,"OCMW dual residual cover 0","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Cover policy FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_fin_debt_jump_13_98m_2025","Roosdaal fin debt 13.98m JUMP loans 4.20m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",13978949,13978949,"Debt stock residual dual JUMP","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",7.5,5.5,3.5,pi(7.5,5.5,3.5),"Debt path FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_invest_underspend_2025","Roosdaal invest 6.42 vs MJP 13.70 MASSIVE UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",6423521,6423521,"Invest residual dual underspend","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",8.0,5.0,3.5,pi(8.0,5.0,3.5),"Invest path FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_toelagen_3_08m_2025","Roosdaal toelagen 3.08m police 1.61 AGB 0.32 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",3084138,3084138,"Grants residual dual","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Named matrix FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_personnel_9_19m_2025","Roosdaal personnel 9.19m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",9187165,9187165,"Wage bill residual","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"FTE FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_afm_1_95m_2025","Roosdaal AFM +1.95m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",1945255,1945255,"AFM residual dual","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
("lb_roo_agb_afm_corr_neg_0_27m_2025","Roosdaal AGB corr AFM -0.27m NEG dual residual FOI","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",271390,271390,"AGB dual residual NEG AFM","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC dual AGB","8.0",4.0,3.5,pi(8.0,4.0,3.5),"AGB AFM path FOI","active","","tick1072; primary Roosdaal JR2025 dual AGB; not TE-additive"),
("lb_roo_bbr_5_07m_2025","Roosdaal BBR +5.07m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",5071230,5071230,"BBR residual dual","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"BBR path FOI","active","","tick1072; primary Roosdaal JR2025; dual residual after Lebbeke; not TE-additive"),
]
# fix agb row - I accidentally put quotes on absurdity as string in wrong place
lb[6] = ("lb_roo_agb_afm_corr_neg_0_27m_2025","Roosdaal AGB corr AFM -0.27m NEG dual residual FOI","L5","local_budget_line","Vlaanderen>Gemeenten>Roosdaal_L5",271390,271390,"AGB dual residual NEG AFM","strong",SRC,"Roosdaal residents","Local dual residual map VL JR2025","JR2025 BBC Roosdaal GEOC dual AGB",8.0,4.0,3.5,pi(8.0,4.0,3.5),"AGB AFM path FOI","active","","tick1072; primary Roosdaal JR2025 dual AGB; not TE-additive")

with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Roosdaal Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://roosdaal.be/sites/default/files/2026-06/0_Jaarrekening_2025_lokaal_bestuur_Roosdaal.pdf,"
    "Lokaal Bestuur Roosdaal,2026-08-11,primary_pdf,"
    "tick1072; 191p; GR+RMW 28.05.2026 pub 03.06.2026; KBO GE 0207.515.365 / OCMW 0212.166.021; "
    "AD Emma Van der Maelen FD Joos Van Droogenbroeck; Brusselstraat 15 NIS 23097; "
    "assets 66.737m equity 42.831m fin debt 13.979m JUMP new loans 4.196m cash 4.731m "
    "pension DROP 6.815m AFM +1.945m BBR 5.071m budget +1.995m invest 6.424 vs MJP 13.701 "
    "toelagen 3.084m police 1.614 AGB 0.323 personnel 9.187m OCMW cover 0 ZERO equity cum -1.237m "
    "AGB AFM -0.041 corr -0.271 NEG dual; dual residual after Lebbeke"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Roosdaal,Commune de Roosdaal,Municipality of Roosdaal,municipality,vlaanderen_gov,nl,"
    "https://roosdaal.be,financien@roosdaal.be,Brusselstraat 15 1760 Roosdaal,"
    "JR2025 dual residual tick1072; KBO 0207.515.365 / OCMW 0212.166.021; assets 66.737m fin debt 13.979m JUMP "
    "new loans 4.196m; cash 4.731m; pension DROP 6.815m; AFM +1.945m; BBR 5.071m; budget +1.995m; "
    "OCMW cover 0 ZERO OCMW equity cum -1.237m WORSENING; toelagen 3.084m police 1.614 AGB 0.323; "
    "invest underspend 6.42 vs MJP 13.70; AGB corr AFM -0.271 NEG; AD Emma Van der Maelen FD Joos Van Droogenbroeck"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_roo_ocmw_zero_loans_invest_agb_l5,Vlaanderen>Gemeenten>Roosdaal>ocmw_zero_loans_invest_agb_L5,city_roosdaal,'
    '"OCMW cover 0 ZERO vs expl gap -0.887m and OCMW equity cum -1.237m WORSENING (was -1.112m); fin debt JUMP '
    '10.829to13.979m with new loans 4.196m; invest underspend 6.424 vs MJP 13.701 MASSIVE; toelagen 3.084m police '
    '1.614 AGB 0.323; AGB AFM -0.041 / corr AFM -0.271 NEG dual; MJP loans 2027 3.117m",'
    '"Flemish Brabant mun with ZERO OCMW cover and deepening OCMW equity residual, large new loan year, '
    'massive invest underspend, and NEG AGB dual AFM",9,Gemeente Roosdaal,financien@roosdaal.be,'
    "Brusselstraat 15 1760 Roosdaal,docs/doge/foi/drafts/gap_roo_ocmw_zero_loans_invest_agb_l5.md,ready,2026-08-11,,,,,,"
    f"comm_roo_ocmw_gap_2025,lb_roo_ocmw_cover_zero_1_24m_2025,{TS},{TS},"
    "tick1072; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1072":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1072: Roosdaal GE+OCMW JR2025 dual residual done; FOI "
            "gap_roo_ocmw_zero_loans_invest_agb_l5 ready prio9; spawn rq_1073"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1072 not found")
out.append(
    [
        "rq_1073",
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
        "spawned tick1072 after Roosdaal dual residual; residual dual L5 next; progress@1080 in 7",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1072,1072,no,"
    "tick1072 Roosdaal GE+OCMW JR2025 dual residual; FOI gap_roo_ocmw_zero_loans_invest_agb_l5 prio9 ready; "
    "assets 66.737m fin debt 13.979m JUMP new loans 4.196m cash 4.731m pension DROP 6.815m AFM +1.945m "
    "BBR 5.071m budget +1.995m invest 6.424 vs MJP 13.701 toelagen 3.084m police 1.614 AGB 0.323 "
    "personnel 9.187m OCMW cover 0 ZERO equity cum -1.237m AGB corr AFM -0.271 NEG; next residual dual L5 rq_1073; "
    "progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
