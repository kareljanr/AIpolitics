"""Tick 1069 — Aartselaar GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_aartselaar_jr2025"
ENT = "city_aartselaar"
TICK = "tick1069"
TS = "2026-08-11T00:00:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")
if not DATA.exists():
    DATA = Path(__file__).resolve().parents[1] / "data"

bud_rows = [
("bud_aar_assets_2025",ENT,2025,73995362,"bbc_jr_realized",SRC,"strong","Assets YE2025 73.995m (was 72.073m); tick1069"),
("bud_aar_equity_2025",ENT,2025,56841913,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 56.842m (was 57.099m slight DROP); tick1069"),
("bud_aar_debt_total_2025",ENT,2025,17153448,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 17.15m JUMP (was 14.97m pension+debt); tick1069"),
("bud_aar_fin_debt_2025",ENT,2025,6008035,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 6.008m JUMP (was 5.161m after multi-year decline); tick1069"),
("bud_aar_fin_debt_lt_2025",ENT,2025,4819469,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 4.819m JUMP (was 3.808m); tick1069"),
("bud_aar_fin_debt_st_due_2025",ENT,2025,1188565,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 1.189m; tick1069"),
("bud_aar_new_loans_2025",ENT,2025,2200000,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 2.20m JUMP FOI (prior years 0); tick1069"),
("bud_aar_aflossingen_2025",ENT,2025,1352738,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 1.353m; tick1069"),
("bud_aar_mjp_new_loans_2026",ENT,2025,1400000,"bbc_jr_realized",SRC,"strong","MJP new loans 2026 planned 1.40m; tick1069"),
("bud_aar_mjp_new_loans_2027",ENT,2025,2800000,"bbc_jr_realized",SRC,"strong","MJP new loans 2027 planned 2.80m FOI; tick1069"),
("bud_aar_mjp_fin_debt_2027",ENT,2025,8141311,"bbc_jr_realized",SRC,"strong","MJP fin debt YE2027 planned 8.14m path FOI; tick1069"),
("bud_aar_cash_2025",ENT,2025,9914695,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 9.915m (was 9.682m); tick1069"),
("bud_aar_pension_2025",ENT,2025,7071097,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 7.071m JUMP FOI (was 5.318m +1.753m); tick1069"),
("bud_aar_cap_subs_2025",ENT,2025,3797175,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 3.797m; tick1069"),
("bud_aar_fva_total_2025",ENT,2025,9630838,"bbc_jr_realized",SRC,"strong","FVA total YE2025 9.631m; tick1069"),
("bud_aar_fva_igs_2025",ENT,2025,8415799,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 8.416m; tick1069"),
("bud_aar_expl_rec_2025",ENT,2025,29653740,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 29.654m; tick1069"),
("bud_aar_expl_exp_2025",ENT,2025,25570822,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 25.571m; tick1069"),
("bud_aar_expl_saldo_2025",ENT,2025,4082918,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +4.083m STRONG; tick1069"),
("bud_aar_invest_exp_2025",ENT,2025,4323726,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 4.324m vs MJP 7.420m UNDERSPEND FOI; tick1069"),
("bud_aar_invest_rec_2025",ENT,2025,454788,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 0.455m; tick1069"),
("bud_aar_invest_saldo_2025",ENT,2025,-3868938,"bbc_jr_realized",SRC,"strong","Investeringssaldo -3.869m; tick1069"),
("bud_aar_mjp_invest_planned_2025",ENT,2025,7419881,"bbc_jr_realized",SRC,"strong","MJP invest planned 7.420m vs realized 4.324m underspend FOI; tick1069"),
("bud_aar_invest_mva_2025",ENT,2025,3317569,"bbc_jr_realized",SRC,"strong","Investeringen MVA 3.318m; tick1069"),
("bud_aar_invest_subs_granted_2025",ENT,2025,1006097,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 1.006m FOI (regen/afvalwater 0.955m); tick1069"),
("bud_aar_afm_2025",ENT,2025,2963751,"bbc_jr_realized",SRC,"strong","AFM +2.964m STRONG (MJP only 0.340m); tick1069"),
("bud_aar_afm_corr_2025",ENT,2025,3903627,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +3.904m STRONG; tick1069"),
("bud_aar_bbr_2025",ENT,2025,6452569,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +6.453m; tick1069"),
("bud_aar_budget_result_2025",ENT,2025,1294814,"bbc_jr_realized",SRC,"strong","Budgettair resultaat +1.295m STRONG (MJP was -3.563m); tick1069"),
("bud_aar_cum_br_2025",ENT,2025,9763556,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +9.764m; tick1069"),
("bud_aar_onbeschikbaar_2025",ENT,2025,3310987,"bbc_jr_realized",SRC,"strong","Onbeschikbare gelden 3.311m HIGH FOI; tick1069"),
("bud_aar_pnl_2025",ENT,2025,-516918,"bbc_jr_realized",SRC,"strong","P&L -0.517m IMPROVING (was -2.416m; pension jump); tick1069"),
("bud_aar_ge_expl_exp_2025",ENT,2025,22810021,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 22.810m; tick1069"),
("bud_aar_ge_expl_rec_2025",ENT,2025,28005647,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 28.006m; tick1069"),
("bud_aar_ocmw_expl_exp_2025",ENT,2025,2760802,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 2.761m; tick1069"),
("bud_aar_ocmw_expl_rec_2025",ENT,2025,1648093,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 1.648m; tick1069"),
("bud_aar_ocmw_expl_gap_2025",ENT,2025,-1112708,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -1.113m; tick1069"),
("bud_aar_ocmw_cover_2025",ENT,2025,1152366,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 1.152m FULL; tick1069"),
("bud_aar_equity_cum_2025",ENT,2025,16661327,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +16.661m; tick1069"),
("bud_aar_ocmw_equity_cum_2025",ENT,2025,-1683406,"bbc_jr_realized",SRC,"strong","OCMW equity cum -1.683m IMPROVING (was -2.131m; cover full); tick1069"),
("bud_aar_ge_equity_cum_2025",ENT,2025,18344733,"bbc_jr_realized",SRC,"strong","GE equity cum +18.345m; tick1069"),
("bud_aar_personnel_2025",ENT,2025,14133691,"bbc_jr_realized",SRC,"strong","Bezoldigingen 14.134m incl education pass-through 2.939m; tick1069"),
("bud_aar_edu_pass_through_2025",ENT,2025,2938622,"bbc_jr_realized",SRC,"strong","Onderwijzend personeel ten laste andere overheden 2.939m; tick1069"),
("bud_aar_toelagen_2025",ENT,2025,3527550,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 3.528m FOI residual; tick1069"),
("bud_aar_toelagen_police_2025",ENT,2025,2529169,"bbc_jr_realized",SRC,"strong","Toelage politiezone 2.529m JUMP (was 2.347m); tick1069"),
("bud_aar_toelagen_fire_2025",ENT,2025,705512,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.706m flat; tick1069"),
("bud_aar_toelagen_igs_2025",ENT,2025,30609,"bbc_jr_realized",SRC,"strong","Toelage IGS 0.031m; tick1069"),
("bud_aar_toelagen_other_2025",ENT,2025,262260,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst+welzijn residual 0.262m FOI; tick1069"),
("bud_aar_ocmw_aid_2025",ENT,2025,807282,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 0.807m; tick1069"),
("bud_aar_fiscal_2025",ENT,2025,16533581,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 16.534m; tick1069"),
("bud_aar_fiscal_ov_2025",ENT,2025,7830563,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 7.831m; tick1069"),
("bud_aar_fiscal_pb_2025",ENT,2025,5663202,"bbc_jr_realized",SRC,"strong","Aanvullende PB 5.663m JUMP; tick1069"),
("bud_aar_gemeentefonds_2025",ENT,2025,3068126,"bbc_jr_realized",SRC,"strong","Gemeentefonds 3.068m; tick1069"),
("bud_aar_interest_2025",ENT,2025,108949,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.109m; tick1069"),
("bud_aar_invest_subs_water_2025",ENT,2025,955213,"bbc_jr_realized",SRC,"strong","Invest-subs regen/afvalwater 0.955m of 1.006m FOI; tick1069"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_aar_police_toelage_2025","Aartselaar politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,2529169,"{2025:2529169}",0,"active","","Aartselaar politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>toelagen",TICK),
("comm_aar_fire_toelage_2025","Aartselaar HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,705512,"{2025:705512}",0,"active","","Aartselaar HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>toelagen",TICK),
("comm_aar_invest_subs_water_2025","Aartselaar invest-subs regen/afvalwater 2025",ENT,"Water/IGS","BBC JR2025 SUB","",2025,2025,955213,"{2025:955213}",0,"active","","Aartselaar invest-subs water 0.955m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>invest_subs",TICK),
("comm_aar_new_loans_2025","Aartselaar nieuwe leningen 2025",ENT,"Banks","BBC JR2025 T4","",2025,2025,2200000,"{2025:2200000}",0,"active","","Aartselaar new loans 2.20m JUMP FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>debt",TICK),
("comm_aar_mjp_loans_2026_27","Aartselaar MJP new loans 2026-27 planned",ENT,"Banks","BBC JR2025 T4","",2026,2027,4200000,"{2026:1400000,2027:2800000}",4200000,"active","","Aartselaar MJP loans 1.4m+2.8m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>debt",TICK),
("comm_aar_pension_jump_2025","Aartselaar pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,7071097,"{2025:7071097}",0,"active","","Aartselaar pension 7.071m JUMP +1.75m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>pension",TICK),
("comm_aar_ocmw_cover_2025","Aartselaar OCMW cover full 2025",ENT,"OCMW Aartselaar","BBC JR2025","",2025,2025,1152366,"{2025:1152366}",0,"active","","Aartselaar OCMW cover 1.152m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Aartselaar>ocmw",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_aar_pension_jump_7_07m_2025","Aartselaar pension 7.07m JUMP +1.75m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",7071097,7071097,"Pension residual dual JUMP","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Pension FOI jump","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_fin_debt_jump_6_01m_2025","Aartselaar fin debt 6.01m JUMP new loans 2.20m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",6008035,6008035,"Debt stock residual dual JUMP","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",7.5,5.0,3.5,pi(7.5,5.0,3.5),"Debt path FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_invest_subs_1_01m_2025","Aartselaar invest-subs 1.01m water 0.955 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",1006097,1006097,"Invest-subs residual dual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Named matrix FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_toelagen_3_53m_2025","Aartselaar toelagen 3.53m police 2.53 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",3527550,3527550,"Grants residual dual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Named matrix FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_personnel_14_13m_2025","Aartselaar personnel 14.13m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",14133691,14133691,"Wage bill residual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",6.0,5.5,3.5,pi(6.0,5.5,3.5),"FTE FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_afm_2_96m_2025","Aartselaar AFM +2.96m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",2963751,2963751,"AFM residual dual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_bbr_6_45m_2025","Aartselaar BBR +6.45m onbeschikbaar 3.31 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",6452569,6452569,"BBR residual dual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"BBR path FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
("lb_aar_mjp_loans_4_2m_2026_27","Aartselaar MJP new loans 1.4m+2.8m 2026-27 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Aartselaar_L5",4200000,4200000,"Planned loan residual dual","strong",SRC,"Aartselaar residents","Local dual residual map VL JR2025","JR2025 BBC Aartselaar GEOC realized figures",6.5,5.0,3.5,pi(6.5,5.0,3.5),"Loan path FOI","active","","tick1069; primary Aartselaar JR2025; dual residual after Overijse; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Aartselaar Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://www.aartselaar.be/jaarrekening-2025,"
    "Lokaal Bestuur Aartselaar,2026-08-11,primary_pdf,"
    "tick1069; 126p; GR+RMW 18.05.2026 pub 20.05.2026; KBO GE 0207.508.932 / OCMW 0212.234.812; "
    "AD Peter Van Mechelen FD Arno Van Velsen; Baron van Ertbornstraat 1 NIS 11001; "
    "assets 73.995m equity 56.842m fin debt 6.008m JUMP new loans 2.20m cash 9.915m "
    "pension JUMP 7.071m AFM +2.964m BBR 6.453m budget +1.295m invest 4.324 vs MJP 7.420 "
    "toelagen 3.528m police 2.529 invest-subs 1.006 water 0.955 personnel 14.134m "
    "OCMW cover 1.152 FULL OCMW equity cum -1.683 IMPROVING; MJP loans 2026 1.4m / 2027 2.8m; "
    "dual residual after Overijse"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Aartselaar,Commune d'Aartselaar,Municipality of Aartselaar,municipality,vlaanderen_gov,nl,"
    "https://www.aartselaar.be,info@aartselaar.be,Baron van Ertbornstraat 1 2630 Aartselaar,"
    "JR2025 dual residual tick1069; KBO 0207.508.932 / OCMW 0212.234.812; assets 73.995m fin debt 6.008m JUMP "
    "new loans 2.20m; cash 9.915m; pension JUMP 7.071m; AFM +2.964m; BBR 6.453m; budget +1.295m; "
    "OCMW cover 1.152 FULL OCMW equity cum -1.683 IMPROVING; toelagen 3.528m police 2.529; "
    "invest-subs 1.006 water 0.955; MJP loans 2026 1.4m / 2027 2.8m; AD Peter Van Mechelen FD Arno Van Velsen"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_aar_pension_loans_invest_subs_l5,Vlaanderen>Gemeenten>Aartselaar>pension_loans_invest_subs_L5,city_aartselaar,'
    '"Pension JUMP 5.318to7.071m (+1.753m) with P&L still -0.517m; fin debt JUMP 5.161to6.008m after multi-year decline '
    'with new loans 2.20m (prior years 0) and MJP 2026 1.40m / 2027 2.80m to path YE2027 8.14m; invest underspend '
    '4.324 vs MJP 7.420; invest-subs 1.006m of which regen/afvalwater 0.955m named residual; toelagen 3.528m police '
    '2.529 JUMP; onbeschikbaar 3.311m of BBR 6.453m",'
    '"Antwerp mun with sharp pension provision jump and reverse of multi-year debt decline via 2.2m new loans, '
    'large water invest-subs line, and material invest underspend",9,Gemeente Aartselaar,info@aartselaar.be,'
    "Baron van Ertbornstraat 1 2630 Aartselaar,docs/doge/foi/drafts/gap_aar_pension_loans_invest_subs_l5.md,ready,2026-08-11,,,,,,"
    f"comm_aar_pension_jump_2025,lb_aar_pension_jump_7_07m_2025,{TS},{TS},"
    "tick1069; ready not sent; do not send without human OK"
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
    "skip rq_116; progress@1070"
)
for r in body:
    if r and r[0] == "rq_1069":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1069: Aartselaar GE+OCMW JR2025 dual residual done; FOI "
            "gap_aar_pension_loans_invest_subs_l5 ready prio9; spawn rq_1070"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1069 not found")
out.append(
    [
        "rq_1070",
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
        "spawned tick1069 after Aartselaar dual residual; residual dual L5 next; progress@1070 due this tick decade",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1069,1069,no,"
    "tick1069 Aartselaar GE+OCMW JR2025 dual residual; FOI gap_aar_pension_loans_invest_subs_l5 prio9 ready; "
    "assets 73.995m fin debt 6.008m JUMP new loans 2.20m cash 9.915m pension JUMP 7.071m AFM +2.964m "
    "BBR 6.453m budget +1.295m invest 4.324 vs MJP 7.420 toelagen 3.528m police 2.529 invest-subs 1.006 "
    "water 0.955 personnel 14.134m OCMW cover 1.152 FULL equity cum -1.683 IMPROVING MJP loans 2026 1.4m/2027 2.8m; "
    "next residual dual L5 rq_1070; progress@1070 due; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
