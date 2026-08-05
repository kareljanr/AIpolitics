"""Tick 1071 — Lebbeke GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_lebbeke_jr2025"
ENT = "city_lebbeke"
TICK = "tick1071"
TS = "2026-08-11T01:00:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_leb_assets_2025",ENT,2025,108341280,"bbc_jr_realized",SRC,"strong","Assets YE2025 108.341m JUMP (was 104.758m); tick1071"),
("bud_leb_equity_2025",ENT,2025,70124009,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 70.124m (was 69.620m); tick1071"),
("bud_leb_debt_total_2025",ENT,2025,38217270,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 38.217m JUMP (was 35.138m); tick1071"),
("bud_leb_fin_debt_2025",ENT,2025,23735746,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 23.736m JUMP (was 22.024m); tick1071"),
("bud_leb_fin_debt_lt_2025",ENT,2025,21562546,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 21.563m JUMP (was 19.684m); tick1071"),
("bud_leb_fin_debt_st_due_2025",ENT,2025,2173200,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 2.173m; tick1071"),
("bud_leb_new_loans_2025",ENT,2025,4195377,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 4.195m JUMP FOI (bank 3.0m + leasing); tick1071"),
("bud_leb_aflossingen_2025",ENT,2025,2483731,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 2.484m; tick1071"),
("bud_leb_mjp_new_loans_2026",ENT,2025,11279156,"bbc_jr_realized",SRC,"strong","MJP new loans 2026 planned 11.279m MASSIVE JUMP FOI; tick1071"),
("bud_leb_mjp_fin_debt_2026",ENT,2025,32622677,"bbc_jr_realized",SRC,"strong","MJP fin debt YE2026 planned 32.623m FOI path; tick1071"),
("bud_leb_cash_2025",ENT,2025,6138214,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 6.138m JUMP (was 5.496m); tick1071"),
("bud_leb_pension_2025",ENT,2025,7210438,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 7.210m JUMP FOI (was 6.595m); tick1071"),
("bud_leb_cap_subs_2025",ENT,2025,4145865,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 4.146m; tick1071"),
("bud_leb_fva_total_2025",ENT,2025,18462813,"bbc_jr_realized",SRC,"strong","FVA total YE2025 18.463m; tick1071"),
("bud_leb_fva_igs_2025",ENT,2025,18236722,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 18.237m; tick1071"),
("bud_leb_leasing_mva_2025",ENT,2025,16140582,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 16.141m HIGH FOI; tick1071"),
("bud_leb_expl_rec_2025",ENT,2025,42088489,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 42.088m; tick1071"),
("bud_leb_expl_exp_2025",ENT,2025,37515846,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 37.516m; tick1071"),
("bud_leb_expl_saldo_2025",ENT,2025,4572643,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +4.573m STRONG; tick1071"),
("bud_leb_invest_exp_2025",ENT,2025,6332609,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 6.333m vs MJP 9.584m UNDERSPEND FOI; tick1071"),
("bud_leb_invest_rec_2025",ENT,2025,683510,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.684m; tick1071"),
("bud_leb_invest_saldo_2025",ENT,2025,-5649098,"bbc_jr_realized",SRC,"strong","Investeringssaldo -5.649m; tick1071"),
("bud_leb_mjp_invest_planned_2025",ENT,2025,9583551,"bbc_jr_realized",SRC,"strong","MJP invest planned 9.584m vs realized 6.333m underspend FOI; tick1071"),
("bud_leb_invest_mva_2025",ENT,2025,5636432,"bbc_jr_realized",SRC,"strong","Investeringen MVA 5.636m; tick1071"),
("bud_leb_invest_subs_granted_2025",ENT,2025,592092,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.592m (police 0.432m) FOI; tick1071"),
("bud_leb_afm_2025",ENT,2025,2227964,"bbc_jr_realized",SRC,"strong","AFM +2.228m STRONG (MJP only 0.130m); tick1071"),
("bud_leb_afm_corr_2025",ENT,2025,2949766,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +2.950m STRONG; tick1071"),
("bud_leb_bbr_2025",ENT,2025,4947196,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +4.947m; tick1071"),
("bud_leb_budget_result_2025",ENT,2025,638983,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +0.639m STRONG (MJP was -2.555m); tick1071"),
("bud_leb_cum_br_2025",ENT,2025,5133863,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +5.134m; tick1071"),
("bud_leb_onbeschikbaar_2025",ENT,2025,186667,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 0.187m; tick1071"),
("bud_leb_pnl_2025",ENT,2025,274841,"bbc_jr_realized",SRC,"strong","P&L +0.275m IMPROVING (was -1.723m); tick1071"),
("bud_leb_ge_expl_exp_2025",ENT,2025,25784192,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 25.784m; tick1071"),
("bud_leb_ge_expl_rec_2025",ENT,2025,31682223,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 31.682m; tick1071"),
("bud_leb_ocmw_expl_exp_2025",ENT,2025,11731654,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 11.732m; tick1071"),
("bud_leb_ocmw_expl_rec_2025",ENT,2025,10406266,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 10.406m; tick1071"),
("bud_leb_ocmw_expl_gap_2025",ENT,2025,-1325388,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -1.325m; tick1071"),
("bud_leb_ocmw_cover_2025",ENT,2025,1690347,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 1.690m FULL; tick1071"),
("bud_leb_equity_cum_2025",ENT,2025,12025156,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +12.025m; tick1071"),
("bud_leb_ocmw_equity_cum_2025",ENT,2025,-3585349,"bbc_jr_realized",SRC,"strong","OCMW equity cum -3.585m still NEG FOI (was -3.507m; cover full); tick1071"),
("bud_leb_ge_equity_cum_2025",ENT,2025,15610505,"bbc_jr_realized",SRC,"strong","GE equity cum +15.611m; tick1071"),
("bud_leb_personnel_2025",ENT,2025,22653351,"bbc_jr_realized",SRC,"strong","Bezoldigingen 22.653m JUMP incl education pass-through 3.226m JUMP; tick1071"),
("bud_leb_edu_pass_through_2025",ENT,2025,3226200,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 3.226m JUMP (was 1.370m); tick1071"),
("bud_leb_toelagen_2025",ENT,2025,6682828,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 6.683m FOI residual; tick1071"),
("bud_leb_toelagen_police_2025",ENT,2025,3138055,"bbc_jr_realized",SRC,"strong","Toelage politiezone 3.138m; tick1071"),
("bud_leb_toelagen_fire_2025",ENT,2025,492706,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.493m; tick1071"),
("bud_leb_toelagen_igs_2025",ENT,2025,2537078,"bbc_jr_realized",SRC,"strong","Toelage IGS 2.537m HIGH FOI; tick1071"),
("bud_leb_toelagen_other_2025",ENT,2025,514989,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.515m FOI; tick1071"),
("bud_leb_ocmw_aid_2025",ENT,2025,1143512,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 1.144m JUMP; tick1071"),
("bud_leb_fiscal_2025",ENT,2025,18853748,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 18.854m; tick1071"),
("bud_leb_fiscal_ov_2025",ENT,2025,7517566,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 7.518m; tick1071"),
("bud_leb_fiscal_pb_2025",ENT,2025,9176428,"bbc_jr_realized",SRC,"strong","Aanvullende PB 9.176m JUMP; tick1071"),
("bud_leb_gemeentefonds_2025",ENT,2025,5237119,"bbc_jr_realized",SRC,"strong","Gemeentefonds 5.237m; tick1071"),
("bud_leb_interest_2025",ENT,2025,624775,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.625m; tick1071"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_leb_police_toelage_2025","Lebbeke politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,3138055,"{2025:3138055}",0,"active","","Lebbeke politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>toelagen",TICK),
("comm_leb_fire_toelage_2025","Lebbeke HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,492706,"{2025:492706}",0,"active","","Lebbeke HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>toelagen",TICK),
("comm_leb_igs_toelage_2025","Lebbeke IGS toelage 2025",ENT,"IGS","BBC JR2025","",2025,2025,2537078,"{2025:2537078}",0,"active","","Lebbeke IGS toelage 2.537m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>toelagen",TICK),
("comm_leb_new_loans_2025","Lebbeke nieuwe leningen 2025",ENT,"Banks/leasing","BBC JR2025 T4","",2025,2025,4195377,"{2025:4195377}",0,"active","","Lebbeke new loans 4.195m JUMP FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>debt",TICK),
("comm_leb_mjp_loans_2026","Lebbeke MJP new loans 2026 planned",ENT,"Banks","BBC JR2025 T4","",2026,2026,11279156,"{2026:11279156}",11279156,"active","","Lebbeke MJP loans 11.28m MASSIVE FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>debt",TICK),
("comm_leb_pension_jump_2025","Lebbeke pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,7210438,"{2025:7210438}",0,"active","","Lebbeke pension 7.210m JUMP","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>pension",TICK),
("comm_leb_ocmw_cover_2025","Lebbeke OCMW cover full 2025",ENT,"OCMW Lebbeke","BBC JR2025","",2025,2025,1690347,"{2025:1690347}",0,"active","","Lebbeke OCMW cover 1.690m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Lebbeke>ocmw",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_leb_mjp_loans_11_28m_2026","Lebbeke MJP new loans 11.28m 2026 MASSIVE FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",11279156,11279156,"Planned loan residual dual MASSIVE","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",8.5,5.5,3.5,pi(8.5,5.5,3.5),"Loan path FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_fin_debt_jump_23_74m_2025","Lebbeke fin debt 23.74m JUMP loans 4.20m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",23735746,23735746,"Debt stock residual dual JUMP","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",7.5,5.5,3.5,pi(7.5,5.5,3.5),"Debt path FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_toelagen_6_68m_2025","Lebbeke toelagen 6.68m police 3.14 IGS 2.54 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",6682828,6682828,"Grants residual dual","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Named matrix FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_personnel_22_65m_2025","Lebbeke personnel 22.65m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",22653351,22653351,"Wage bill residual JUMP","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"FTE FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_pension_jump_7_21m_2025","Lebbeke pension 7.21m JUMP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",7210438,7210438,"Pension residual dual JUMP","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",7.5,5.0,3.5,pi(7.5,5.0,3.5),"Pension FOI jump","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_leasing_mva_16_14m_2025","Lebbeke leasing MVA 16.14m HIGH FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",16140582,16140582,"Leasing residual dual","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",7.0,5.5,3.5,pi(7.0,5.5,3.5),"Leasing FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_afm_2_23m_2025","Lebbeke AFM +2.23m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",2227964,2227964,"AFM residual dual","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
("lb_leb_ocmw_equity_neg_3_59m_2025","Lebbeke OCMW equity cum -3.59m NEG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Lebbeke_L5",3585349,3585349,"OCMW dual residual NEG","strong",SRC,"Lebbeke residents","Local dual residual map VL JR2025","JR2025 BBC Lebbeke GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Cover policy FOI","active","","tick1071; primary Lebbeke JR2025; dual residual after SML; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Lebbeke Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://lblod.lebbeke.be/LBLODWeb/Home/Overzicht/cfe84a7f48fbe4a4176e047955bd3fd013f26a17753c9dc888e2f2e289188f00/GetPublication?filename=Gemeente%20en%20OCMW%20Lebbeke%20-%20Jaarrekening%202025_03-06-2026_56891.pdf,"
    "Lokaal Bestuur Lebbeke,2026-08-11,primary_pdf,"
    "tick1071; 216p; GR 03.06.2026 pub 09.06.2026; KBO GE 0207.446.079 / OCMW 0212.192.151; "
    "AD Luc Vermeir FD Jeroen Bosman BM Jan Vanderstraeten; Flor Hofmanslaan 1 NIS 42011; "
    "assets 108.341m equity 70.124m fin debt 23.736m JUMP new loans 4.195m cash 6.138m "
    "pension JUMP 7.210m AFM +2.228m BBR 4.947m budget +0.639m invest 6.333 vs MJP 9.584 "
    "toelagen 6.683m police 3.138 IGS 2.537 personnel 22.653m OCMW cover 1.690 FULL "
    "OCMW equity cum -3.585m; MJP loans 2026 11.279m to debt 32.623m; leasing MVA 16.141m; "
    "dual residual after SML"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Lebbeke,Commune de Lebbeke,Municipality of Lebbeke,municipality,vlaanderen_gov,nl,"
    "https://www.lebbeke.be,financieledienst@lebbeke.be,Flor Hofmanslaan 1 9280 Lebbeke,"
    "JR2025 dual residual tick1071; KBO 0207.446.079 / OCMW 0212.192.151; assets 108.341m fin debt 23.736m JUMP "
    "new loans 4.195m; cash 6.138m; pension JUMP 7.210m; AFM +2.228m; BBR 4.947m; budget +0.639m; "
    "OCMW cover 1.690 FULL OCMW equity cum -3.585m; toelagen 6.683m police 3.138 IGS 2.537; "
    "MJP loans 2026 11.279m path YE2026 32.623m; leasing MVA 16.141m; AD Luc Vermeir FD Jeroen Bosman"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_leb_mjp_loans_pension_toelagen_l5,Vlaanderen>Gemeenten>Lebbeke>mjp_loans_pension_toelagen_L5,city_lebbeke,'
    '"MJP new loans 2026 11.279m MASSIVE after 2025 new loans 4.195m (bank 3.0m + Fluvius/Farys/kerk leasing) '
    'path fin debt YE2026 32.623m from 23.736m; pension JUMP 6.595to7.210m; toelagen 6.683m police 3.138 IGS 2.537; '
    'invest underspend 6.333 vs MJP 9.584; leasing MVA 16.141m; OCMW equity cum still -3.585m despite cover 1.690 FULL; '
    'personnel JUMP 22.653m edu pass-through 3.226m",'
    '"East-Flanders mun with massive 2026 loan ramp (+11.3m planned), large IGS/police grant matrix, '
    'leasing-heavy asset base, and persistent OCMW equity residual",9,Gemeente Lebbeke,financieledienst@lebbeke.be,'
    "Flor Hofmanslaan 1 9280 Lebbeke,docs/doge/foi/drafts/gap_leb_mjp_loans_pension_toelagen_l5.md,ready,2026-08-11,,,,,,"
    f"comm_leb_mjp_loans_2026,lb_leb_mjp_loans_11_28m_2026,{TS},{TS},"
    "tick1071; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1071":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1071: Lebbeke GE+OCMW JR2025 dual residual done; FOI "
            "gap_leb_mjp_loans_pension_toelagen_l5 ready prio9; spawn rq_1072"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1071 not found")
out.append(
    [
        "rq_1072",
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
        "spawned tick1071 after Lebbeke dual residual; residual dual L5 next; progress@1080 in 8",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1071,1071,no,"
    "tick1071 Lebbeke GE+OCMW JR2025 dual residual; FOI gap_leb_mjp_loans_pension_toelagen_l5 prio9 ready; "
    "assets 108.341m fin debt 23.736m JUMP new loans 4.195m cash 6.138m pension JUMP 7.210m AFM +2.228m "
    "BBR 4.947m budget +0.639m invest 6.333 vs MJP 9.584 toelagen 6.683m police 3.138 IGS 2.537 "
    "personnel 22.653m OCMW cover 1.690 FULL equity cum -3.585m MJP loans 2026 11.279m to debt 32.623m "
    "leasing MVA 16.141m; next residual dual L5 rq_1072; progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
