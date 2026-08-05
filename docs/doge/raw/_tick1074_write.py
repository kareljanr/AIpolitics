"""Tick 1074 — Hoeilaart GE+OCMW JR2025 dual residual."""
from pathlib import Path
import csv
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)

SRC = "src_hoeilaart_jr2025"
ENT = "city_hoeilaart"
TICK = "tick1074"
TS = "2026-08-11T02:30:00Z"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path("docs/doge/data")

bud_rows = [
("bud_hoe_assets_2025",ENT,2025,74013785,"bbc_jr_realized",SRC,"strong","Assets YE2025 74.014m DROP (was 75.872m); tick1074"),
("bud_hoe_equity_2025",ENT,2025,44707156,"bbc_jr_realized",SRC,"strong","Nettoactief YE2025 44.707m DROP (was 45.095m); tick1074"),
("bud_hoe_debt_total_2025",ENT,2025,29306628,"bbc_jr_realized",SRC,"strong","Total schulden YE2025 29.307m DECLINE (was 30.777m); tick1074"),
("bud_hoe_fin_debt_2025",ENT,2025,18524861,"bbc_jr_realized",SRC,"strong","Fin debt total YE2025 18.525m DECLINE (was 20.452m); tick1074"),
("bud_hoe_fin_debt_lt_2025",ENT,2025,16417442,"bbc_jr_realized",SRC,"strong","Fin debt LT YE2025 16.417m DECLINE (was 18.276m); tick1074"),
("bud_hoe_fin_debt_st_due_2025",ENT,2025,2107419,"bbc_jr_realized",SRC,"strong","Fin debt ST due YE2025 2.107m; tick1074"),
("bud_hoe_new_loans_2025",ENT,2025,263121,"bbc_jr_realized",SRC,"strong","Nieuwe leningen 2025 0.263m LOW; tick1074"),
("bud_hoe_aflossingen_2025",ENT,2025,2190245,"bbc_jr_realized",SRC,"strong","Periodieke aflossingen 2025 2.190m; tick1074"),
("bud_hoe_cash_2025",ENT,2025,2240215,"bbc_jr_realized",SRC,"strong","Liquide middelen YE2025 2.240m MASSIVE DROP FOI (was 4.291m); tick1074"),
("bud_hoe_pension_2025",ENT,2025,7612489,"bbc_jr_realized",SRC,"strong","Pensioenvoorzieningen LT YE2025 7.612m JUMP FOI (was 6.044m +1.569m); tick1074"),
("bud_hoe_cap_subs_2025",ENT,2025,13536307,"bbc_jr_realized",SRC,"strong","Kapitaalsubsidies YE2025 13.536m; tick1074"),
("bud_hoe_fva_total_2025",ENT,2025,7846588,"bbc_jr_realized",SRC,"strong","FVA total YE2025 7.847m; tick1074"),
("bud_hoe_fva_igs_2025",ENT,2025,7807442,"bbc_jr_realized",SRC,"strong","FVA IGS YE2025 7.807m; tick1074"),
("bud_hoe_leasing_mva_2025",ENT,2025,4010635,"bbc_jr_realized",SRC,"strong","Leasing MVA YE2025 4.011m; tick1074"),
("bud_hoe_expl_rec_2025",ENT,2025,28971438,"bbc_jr_realized",SRC,"strong","Exploitatieontvangsten 28.971m; tick1074"),
("bud_hoe_expl_exp_2025",ENT,2025,25894718,"bbc_jr_realized",SRC,"strong","Exploitatieuitgaven 25.895m; tick1074"),
("bud_hoe_expl_saldo_2025",ENT,2025,3076720,"bbc_jr_realized",SRC,"strong","Exploitatiesaldo +3.077m STRONG; tick1074"),
("bud_hoe_invest_exp_2025",ENT,2025,3214292,"bbc_jr_realized",SRC,"strong","Investeringsuitgaven 3.214m vs MJP 5.981m UNDERSPEND FOI; tick1074"),
("bud_hoe_invest_rec_2025",ENT,2025,1351466,"bbc_jr_realized",SRC,"strong","Investeringsontvangsten 1.351m; tick1074"),
("bud_hoe_invest_saldo_2025",ENT,2025,-1862826,"bbc_jr_realized",SRC,"strong","Investeringssaldo -1.863m; tick1074"),
("bud_hoe_mjp_invest_planned_2025",ENT,2025,5981477,"bbc_jr_realized",SRC,"strong","MJP invest planned 5.981m vs realized 3.214m underspend FOI; tick1074"),
("bud_hoe_invest_mva_2025",ENT,2025,2779423,"bbc_jr_realized",SRC,"strong","Investeringen MVA 2.779m; tick1074"),
("bud_hoe_invest_subs_granted_2025",ENT,2025,171749,"bbc_jr_realized",SRC,"strong","Toegestane invest-subs 0.172m; tick1074"),
("bud_hoe_afm_2025",ENT,2025,1817860,"bbc_jr_realized",SRC,"strong","AFM +1.818m STRONG; tick1074"),
("bud_hoe_afm_corr_2025",ENT,2025,2371946,"bbc_jr_realized",SRC,"strong","Gecorrigeerde AFM +2.372m STRONG; tick1074"),
("bud_hoe_bbr_2025",ENT,2025,5506344,"bbc_jr_realized",SRC,"strong","BBR beschikbaar +5.506m; tick1074"),
("bud_hoe_budget_result_2025",ENT,2025,-15418,"bbc_jr_realized",SRC,"strong","Budgettair resultaat -0.015m THIN/NEG FOI; tick1074"),
("bud_hoe_cum_br_2025",ENT,2025,5506344,"bbc_jr_realized",SRC,"strong","Gecumuleerd budgettair resultaat +5.506m; tick1074"),
("bud_hoe_pnl_2025",ENT,2025,-1152514,"bbc_jr_realized",SRC,"strong","P&L -1.153m IMPROVING (was -1.547m); tick1074"),
("bud_hoe_ge_expl_exp_2025",ENT,2025,14967541,"bbc_jr_realized",SRC,"strong","GE exploitatieuitgaven J3 14.968m; tick1074"),
("bud_hoe_ge_expl_rec_2025",ENT,2025,20013566,"bbc_jr_realized",SRC,"strong","GE exploitatieontvangsten J3 20.014m; tick1074"),
("bud_hoe_ocmw_expl_exp_2025",ENT,2025,10927178,"bbc_jr_realized",SRC,"strong","OCMW exploitatieuitgaven J3 10.927m; tick1074"),
("bud_hoe_ocmw_expl_rec_2025",ENT,2025,8957873,"bbc_jr_realized",SRC,"strong","OCMW exploitatieontvangsten J3 8.958m; tick1074"),
("bud_hoe_ocmw_expl_gap_2025",ENT,2025,-1969305,"bbc_jr_realized",SRC,"strong","OCMW expl gap J3 -1.969m; tick1074"),
("bud_hoe_ocmw_cover_2025",ENT,2025,2903630,"bbc_jr_realized",SRC,"strong","OCMW cover tussenkomst 2.904m FULL; tick1074"),
("bud_hoe_equity_cum_2025",ENT,2025,3327894,"bbc_jr_realized",SRC,"strong","Gecumuleerd equity overschot YE2025 +3.328m DROP (was +4.480m); tick1074"),
("bud_hoe_ocmw_equity_cum_2025",ENT,2025,1793800,"bbc_jr_realized",SRC,"strong","OCMW equity cum +1.794m (cover full; P&L -3.403m); tick1074"),
("bud_hoe_ge_equity_cum_2025",ENT,2025,1534093,"bbc_jr_realized",SRC,"strong","GE equity cum +1.534m DROP after cover 2.904m; tick1074"),
("bud_hoe_personnel_2025",ENT,2025,13752140,"bbc_jr_realized",SRC,"strong","Bezoldigingen 13.752m; tick1074"),
("bud_hoe_toelagen_2025",ENT,2025,3918190,"bbc_jr_realized",SRC,"strong","Toegestane werkingssubsidies 3.918m FOI residual; tick1074"),
("bud_hoe_toelagen_police_2025",ENT,2025,1129389,"bbc_jr_realized",SRC,"strong","Toelage politiezone 1.129m JUMP (was 0.763m); tick1074"),
("bud_hoe_toelagen_fire_2025",ENT,2025,614735,"bbc_jr_realized",SRC,"strong","Toelage hulpverleningszone 0.615m; tick1074"),
("bud_hoe_toelagen_igs_2025",ENT,2025,1165065,"bbc_jr_realized",SRC,"strong","Toelage IGS 1.165m FOI; tick1074"),
("bud_hoe_toelagen_agb_2025",ENT,2025,536143,"bbc_jr_realized",SRC,"strong","Toelage AGB Holar 0.536m dual residual; tick1074"),
("bud_hoe_toelagen_other_2025",ENT,2025,472858,"bbc_jr_realized",SRC,"strong","Toelage other+eredienst residual 0.473m FOI; tick1074"),
("bud_hoe_ocmw_aid_2025",ENT,2025,902324,"bbc_jr_realized",SRC,"strong","OCMW individuele hulp 0.902m; tick1074"),
("bud_hoe_fiscal_2025",ENT,2025,14144189,"bbc_jr_realized",SRC,"strong","Fiscale opbrengsten 14.144m; tick1074"),
("bud_hoe_fiscal_ov_2025",ENT,2025,5985087,"bbc_jr_realized",SRC,"strong","Opcentiemen OV 5.985m; tick1074"),
("bud_hoe_fiscal_pb_2025",ENT,2025,6874838,"bbc_jr_realized",SRC,"strong","Aanvullende PB 6.875m JUMP; tick1074"),
("bud_hoe_gemeentefonds_2025",ENT,2025,2390262,"bbc_jr_realized",SRC,"strong","Gemeentefonds 2.390m; tick1074"),
("bud_hoe_interest_2025",ENT,2025,541708,"bbc_jr_realized",SRC,"strong","Intresten op leningen 0.542m; tick1074"),
("bud_hoe_agb_afm_corr_2025",ENT,2025,-66042,"bbc_jr_realized",SRC,"strong","AGB Holar corr AFM -0.066m NEG dual residual FOI; tick1074"),
("bud_hoe_debt_per_inhab_2025",ENT,2025,1461,"bbc_jr_realized",SRC,"strong","Openstaande schuld per inwoner EUR1461; tick1074"),
]

with open(DATA / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(f"{r[0]},{r[1]},{r[2]},{r[3]},,,{r[4]},{r[5]},{r[6]},{r[7]}\n")
print("budgets +", len(bud_rows))

comm = [
("comm_hoe_police_toelage_2025","Hoeilaart politiezone toelage 2025",ENT,"Politiezone","BBC JR2025","",2025,2025,1129389,"{2025:1129389}",0,"active","","Hoeilaart politiezone toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>toelagen",TICK),
("comm_hoe_fire_toelage_2025","Hoeilaart HVZ toelage 2025",ENT,"Hulpverleningszone","BBC JR2025","",2025,2025,614735,"{2025:614735}",0,"active","","Hoeilaart HVZ toelage 2025","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>toelagen",TICK),
("comm_hoe_igs_toelage_2025","Hoeilaart IGS toelage 2025",ENT,"IGS","BBC JR2025","",2025,2025,1165065,"{2025:1165065}",0,"active","","Hoeilaart IGS toelage 1.165m FOI","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>toelagen",TICK),
("comm_hoe_agb_toelage_2025","Hoeilaart AGB Holar toelage 2025",ENT,"AGB Holar","BBC JR2025","",2025,2025,536143,"{2025:536143}",0,"active","","Hoeilaart AGB toelage 2025 dual","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>toelagen",TICK),
("comm_hoe_pension_jump_2025","Hoeilaart pension JUMP 2025",ENT,"Pension provision","BBC JR2025","",2025,2025,7612489,"{2025:7612489}",0,"active","","Hoeilaart pension 7.612m JUMP +1.57m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>pension",TICK),
("comm_hoe_ocmw_cover_2025","Hoeilaart OCMW cover full 2025",ENT,"OCMW Hoeilaart","BBC JR2025","",2025,2025,2903630,"{2025:2903630}",0,"active","","Hoeilaart OCMW cover 2.904m full","Keep cover path",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>ocmw",TICK),
("comm_hoe_cash_drop_2025","Hoeilaart cash DROP 2025",ENT,"Treasury","BBC JR2025","",2025,2025,2240215,"{2025:2240215}",0,"active","","Hoeilaart cash 2.240m DROP from 4.291m","FOI residual",SRC,"strong","Vlaanderen>Gemeenten>Hoeilaart>cash",TICK),
]
with open(DATA / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    for r in comm:
        f.write(",".join(str(x) for x in r) + "\n")
print("commitments +", len(comm))

def pi(abs_s, cost_s, diff):
    return round(0.55 * cost_s + 0.35 * abs_s + 0.10 * (10 - diff), 2)

lb = [
("lb_hoe_cash_drop_2_24m_2025","Hoeilaart cash 2.24m MASSIVE DROP FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",2240215,2240215,"Cash residual dual DROP","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Cash path FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_pension_jump_7_61m_2025","Hoeilaart pension 7.61m JUMP +1.57m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",7612489,7612489,"Pension residual dual JUMP","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",8.5,5.0,3.5,pi(8.5,5.0,3.5),"Pension FOI jump","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_toelagen_3_92m_2025","Hoeilaart toelagen 3.92m police 1.13 IGS 1.17 AGB 0.54 FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",3918190,3918190,"Grants residual dual","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Named matrix FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_fin_debt_18_53m_2025","Hoeilaart fin debt 18.53m DECLINE FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",18524861,18524861,"Debt stock residual dual DECLINE","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",6.5,5.5,3.5,pi(6.5,5.5,3.5),"Debt path FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_personnel_13_75m_2025","Hoeilaart personnel 13.75m FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",13752140,13752140,"Wage bill residual","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",6.0,5.5,3.5,pi(6.0,5.5,3.5),"FTE FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_afm_1_82m_2025","Hoeilaart AFM +1.82m STRONG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",1817860,1817860,"AFM residual dual","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",6.0,5.0,3.5,pi(6.0,5.0,3.5),"Keep AFM path","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_budget_neg_thin_2025","Hoeilaart budget -0.015m THIN/NEG FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",15418,15418,"Budget residual dual THIN","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",7.0,3.5,3.5,pi(7.0,3.5,3.5),"Budget path FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
("lb_hoe_invest_underspend_2025","Hoeilaart invest 3.21 vs MJP 5.98 UNDERSPEND FOI residual","L5","local_budget_line","Vlaanderen>Gemeenten>Hoeilaart_L5",3214292,3214292,"Invest residual dual underspend","strong",SRC,"Hoeilaart residents","Local dual residual map VL JR2025","JR2025 BBC Hoeilaart GEOC realized figures",7.0,5.0,3.5,pi(7.0,5.0,3.5),"Invest path FOI","active","","tick1074; primary Hoeilaart JR2025; dual residual after Ternat; not TE-additive"),
]
with open(DATA / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(",".join(str(x) for x in r) + "\n")
print("leaderboard +", len(lb), "pi0", lb[0][16])

src = (
    f"{SRC},Hoeilaart Gemeente+OCMW BBC Jaarrekening 2025,"
    "https://hoeilaart.be/sites/default/files/G%26O%20-%20JR%202025.pdf,"
    "Lokaal Bestuur Hoeilaart,2026-08-11,primary_pdf,"
    "tick1074; 167p; GR+RMW 22.06.2026 pub 23.06.2026; KBO GE 0206.562.092 / OCMW 0212.219.469; "
    "AD wnd Christophe Joly FD Brecht Van den Bogaert; Jan van Ruusbroecpark NIS 23033; "
    "assets 74.014m equity 44.707m fin debt 18.525m DECLINE new loans 0.263m cash MASSIVE DROP 2.240m "
    "pension JUMP 7.612m AFM +1.818m BBR 5.506m budget -0.015m THIN invest 3.214 vs MJP 5.981 "
    "toelagen 3.918m police 1.129 IGS 1.165 AGB 0.536 personnel 13.752m OCMW cover 2.904 FULL; "
    "AGB corr AFM -0.066 NEG dual; dual residual after Ternat"
)
with open(DATA / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

ent = (
    f"{ENT},Gemeente Hoeilaart,Commune de Hoeilaart,Municipality of Hoeilaart,municipality,vlaanderen_gov,nl,"
    "https://hoeilaart.be,financien@hoeilaart.be,Jan van Ruusbroecpark 1560 Hoeilaart,"
    "JR2025 dual residual tick1074; KBO 0206.562.092 / OCMW 0212.219.469; assets 74.014m fin debt 18.525m DECLINE "
    "new loans 0.263m; cash MASSIVE DROP 2.240m; pension JUMP 7.612m; AFM +1.818m; BBR 5.506m; budget -0.015m THIN; "
    "OCMW cover 2.904 FULL; toelagen 3.918m police 1.129 IGS 1.165 AGB 0.536; AD wnd Christophe Joly FD Brecht Van den Bogaert"
)
with open(DATA / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(ent + "\n")
print("entities +1")

foi = (
    'gap_hoe_cash_pension_toelagen_budget_l5,Vlaanderen>Gemeenten>Hoeilaart>cash_pension_toelagen_budget_L5,city_hoeilaart,'
    '"Cash MASSIVE DROP 4.291to2.240m; pension JUMP 6.044to7.612m (+1.569m) with P&L still -1.153m; budget -0.015m THIN; '
    'toelagen 3.918m police JUMP 0.763to1.129 IGS 1.165 AGB 0.536; invest underspend 3.214 vs MJP 5.981; OCMW cover '
    '2.904 FULL with OCMW P&L -3.403m; AGB corr AFM -0.066 NEG dual",'
    '"Flemish Brabant mun with sharp cash drop and pension provision jump, thin budget despite strong AFM, '
    'and large IGS/police/AGB grant matrix",9,Gemeente Hoeilaart,financien@hoeilaart.be,'
    "Jan van Ruusbroecpark 1560 Hoeilaart,docs/doge/foi/drafts/gap_hoe_cash_pension_toelagen_budget_l5.md,ready,2026-08-11,,,,,,"
    f"comm_hoe_cash_drop_2025,lb_hoe_cash_drop_2_24m_2025,{TS},{TS},"
    "tick1074; ready not sent; do not send without human OK"
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
    if r and r[0] == "rq_1074":
        r[4] = "done"
        r[7] = residual
        r[9] = TS
        r[10] = (
            "tick1074: Hoeilaart GE+OCMW JR2025 dual residual done; FOI "
            "gap_hoe_cash_pension_toelagen_budget_l5 ready prio9; spawn rq_1075"
        )
        found = True
    out.append(r)
if not found:
    raise SystemExit("rq_1074 not found")
out.append(
    [
        "rq_1075",
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
        "spawned tick1074 after Hoeilaart dual residual; residual dual L5 next; progress@1080 in 5",
    ]
)
with rq_path.open("w", encoding="utf-8", newline="") as f:
    csv.writer(f).writerows(out)
print("rq updated")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},rq_1074,1074,no,"
    "tick1074 Hoeilaart GE+OCMW JR2025 dual residual; FOI gap_hoe_cash_pension_toelagen_budget_l5 prio9 ready; "
    "assets 74.014m fin debt 18.525m DECLINE new loans 0.263m cash MASSIVE DROP 2.240m pension JUMP 7.612m "
    "AFM +1.818m BBR 5.506m budget -0.015m THIN invest 3.214 vs MJP 5.981 toelagen 3.918m police 1.129 IGS 1.165 "
    "AGB 0.536 personnel 13.752m OCMW cover 2.904 FULL; next residual dual L5 rq_1075; progress@1080; rq_116 deferred\n",
    encoding="utf-8",
)
print("loop_state ok")
print("done", NOW)
