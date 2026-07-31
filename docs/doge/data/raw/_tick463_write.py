# tick463 — NL definitive verdelingsplan 2025 (240m)
from pathlib import Path

root = Path(__file__).resolve().parents[4]
data = root / "docs" / "doge" / "data"
utc = "2026-08-02T22:15:00Z"

src_rows = [
    "src_nloterij_kb_definitief_2025,KB 5 jun 2026 definitief verdelingsplan NL subsidies 2025 (240m L5 full table),https://refli.be/nl/lex/2026004330,Belgisch Staatsblad / Refli,2026-08-02,official_legal,Definitive plan 2025 TOTAL 240m (vs provisional 200m +40m); communities 65.856m; DGD 84.709 KBF 10.3; Prestige 10.000016; LOV2030 10.5; Pro League 3.5; women sport 2.0; culture triple 7.0 confirmed; SARC 1.616; tick463",
    "src_nl_2025_def_vs_prov_recon,NL 2025 definitive vs provisional dual recon,https://refli.be/nl/lex/2026004330,DOGE synthesis primary KB definitief+voorlopig,2026-08-02,synthesis,Strong: total +40m; Prestige 6.176->10.000; women sport 1->2; new LOV2030 10.5 Pro League 3.5 EYOF 1.0 BPC Road LA 1.1; culture named confirmed; residual prestige bulk + Art5 sub-notes FOI; tick463",
]
with (data / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(src_rows) + "\n")

bud_rows = [
    "bud_nloterij_plan_def_2025_total,nationale_loterij,2025,240000000,,,budget,src_nloterij_kb_definitief_2025,strong,Definitive verdelingsplan 2025 TOTAL 240m (KB 5 Jun 2026); +40m vs provisional 200m; tick463",
    "bud_nloterij_def_vs_prov_uplift_2025,nationale_loterij,2025,40000000,,,derived,src_nl_2025_def_vs_prov_recon,strong,Definitive minus provisional plan total 240-200=40m uplift; tick463",
    "bud_nloterij_communities_def_2025,nationale_loterij,2025,65856000,,,budget,src_nloterij_kb_definitief_2025,strong,Cat1 federated entities sum: DG 555034 + VL 39842078 + FR 25458888 = 65.856m definitive; tick463",
    "bud_nloterij_dg_def_2025,dg,2025,555034,,,budget,src_nloterij_kb_definitief_2025,strong,German-speaking Community NL definitive 0.555034m 2025; tick463",
    "bud_nloterij_vl_def_2025,vlaanderen_gov,2025,39842078,,,budget,src_nloterij_kb_definitief_2025,strong,Flemish Community NL definitive 39.842078m 2025; tick463",
    "bud_nloterij_fr_def_2025,fwb,2025,25458888,,,budget,src_nloterij_kb_definitief_2025,strong,French Community NL definitive 25.458888m 2025; tick463",
    "bud_nloterij_kbf_def_2025,kbf,2025,10300000,,,budget,src_nloterij_kb_definitief_2025,strong,Koning Boudewijnstichting definitive 10.3m (prov 9.8m); tick463",
    "bud_nloterij_dgd_def_2025,dgd,2025,84708565,,,budget,src_nloterij_kb_definitief_2025,strong,DGD definitive 84.708565m same as provisional path; tick463",
    "bud_nloterij_prestige_def_2025,nationale_loterij,2025,10000016,,,budget,src_nloterij_kb_definitief_2025,strong,Nationaal Prestige definitive 10.000016m (prov 6.176m uplift; bulk sub-L5 residual); tick463",
    "bud_nloterij_lov2030_def_2025,nationale_loterij,2025,10500000,,,budget,src_nloterij_kb_definitief_2025,strong,LOV2030 Leuven European Capital of Culture projects 10.5m definitive NEW large L5; frame to 2030; tick463",
    "bud_nloterij_proleague_def_2025,nationale_loterij,2025,3500000,,,budget,src_nloterij_kb_definitief_2025,strong,Pro League FSR safety innovation 3.5m definitive NEW; tick463",
    "bud_nloterij_women_sport_def_2025,nationale_loterij,2025,2000000,,,budget,src_nloterij_kb_definitief_2025,strong,Women high-level sport 2.0m definitive (prov 1.0m); tick463",
    "bud_nloterij_bpc_road_la_def_2025,bpc,2025,1100000,,,budget,src_nloterij_kb_definitief_2025,strong,BPC Road to LA and paralympic medals 1.1m definitive NEW; dual BPC werking 0.45; tick463",
    "bud_nloterij_eyof2029_def_2025,nationale_loterij,2025,1000000,,,budget,src_nloterij_kb_definitief_2025,strong,European Youth Olympic Festival 2029 1.0m definitive multi-year frame to 2029; tick463",
    "bud_nloterij_sports_fed_def_2025,nationale_loterij,2025,2700000,,,budget,src_nloterij_kb_definitief_2025,strong,Belgian Sports Federations and National Teams 2.7m definitive; Art5 sub-note residual; tick463",
    "bud_nloterij_local_heritage_call_def_2025,nationale_loterij,2025,4000000,,,budget,src_nloterij_kb_definitief_2025,strong,Project call Local Heritage 4.0m definitive cat4; tick463",
    "bud_nloterij_poverty_call_def_2025,nationale_loterij,2025,2500000,,,budget,src_nloterij_kb_definitief_2025,strong,Project call poverty and social inclusion 2.5m definitive cat4; tick463",
    "bud_nloterij_childfocus_extra_def_2025,child_focus,2025,240000,,,budget,src_nloterij_kb_definitief_2025,strong,Child Focus exceptional support 0.24m + base 1.76m = 2.0m stack; tick463",
    "bud_nloterij_culture_triple_def_2025,nationale_loterij,2025,7000000,,,budget,src_nloterij_kb_definitief_2025,strong,Culture triple definitive Bozar 3.5 Munt 1.75 NOB 1.75 = 7.0 confirmed vs provisional; tick463",
    "bud_nloterij_flagey_def_2025,flagey,2025,250000,,,budget,src_nloterij_kb_definitief_2025,strong,Flagey definitive 0.25m confirmed; tick463",
    "bud_nloterij_europalia_def_2025,europalia,2025,500000,,,budget,src_nloterij_kb_definitief_2025,strong,Europalia definitive 0.5m confirmed; tick463",
    "bud_nloterij_cinematek_def_2025,cinematek,2025,700000,,,budget,src_nloterij_kb_definitief_2025,strong,Cinematek/KBF Filmarchief definitive 0.7m confirmed dual BELSPO residual; tick463",
    "bud_nloterij_sarc_def_2025,iefh,2025,1616180,,,budget,src_nloterij_kb_definitief_2025,strong,SARC/CPVS project definitive 1.616180m confirmed dual CPVS stack tick462; tick463",
    "bud_nloterij_unia_def_2025,unia,2025,4308698,,,budget,src_nloterij_kb_definitief_2025,strong,Unia definitive 4.308698m 2025; tick463",
    "bud_nloterij_myria_def_2025,myria,2025,1077174,,,budget,src_nloterij_kb_definitief_2025,strong,Myria definitive 1.077174m confirmed dual AB path; tick463",
    "bud_nloterij_boic_def_2025,boic,2025,2000000,,,budget,src_nloterij_kb_definitief_2025,strong,BOIC werking definitive 2.0m confirmed; tick463",
    "bud_nloterij_reading_def_2025,nationale_loterij,2025,1500000,,,budget,src_nloterij_kb_definitief_2025,strong,Leesbevordering + financial literacy 1.5m definitive Art5 sub residual; tick463",
    "bud_nloterij_chinese_pavilion_def_2025,nationale_loterij,2025,500000,,,budget,src_nloterij_kb_definitief_2025,strong,Histoire des Belges 2030 Chinese Pavilion 0.5m multi-year to 2031; tick463",
]
with (data / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(bud_rows) + "\n")

ent_rows = [
    "europalia,Stichting Europalia International,Fondation Europalia International,Europalia international arts festival foundation,agency,sec_federal,bi,https://europalia.eu,,,NL definitive 0.5m 2025; end-receiver AR TCO residual; tick463",
    "cinematek,Koninklijk Belgisch Filmarchief CINEMATEK,Cinematheque royale de Belgique CINEMATEK,Royal Belgian Film Archive,agency,belspo,bi,https://cinematek.be,,,NL definitive 0.7m 2025 + BELSPO structural dual residual FOI gap_digit04/vaf; tick463",
    "pro_league,Pro League vzw,Pro League ASBL,Belgian professional football league association,agency,sec_federal,bi,https://www.proleague.be,,,NL definitive 3.5m FSR safety innovation 2025 NEW; tick463",
]
with (data / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + "\n".join(ent_rows) + "\n")

cash = (
    '"{""2025_total_def"":240000000,""2025_prov"":200000000,""uplift"":40000000,'
    '""communities"":65856000,""dgd"":84708565,""kbf"":10300000,""prestige"":10000016,'
    '""lov2030"":10500000,""pro_league"":3500000,""culture_triple"":7000000,'
    '""women_sport"":2000000,""sarc"":1616180,""note"":""KB 5 Jun 2026 definitive""}"'
)
cmt = (
    "cmt_nloterij_plan_definitief_2025,NL definitive verdelingsplan subsidies 2025 240m L5,nationale_loterij,"
    "Multiple statutory and named grantees,Law 19 Apr 2002 art 22-23 + KB 5 Jun 2026,2026-06-05,2025,2025,240000000,"
    + cash
    + ",0,active,https://refli.be/nl/lex/2026004330,Statutory lottery redistribution definitive 2025,"
    "Publish open-data L5; FOI prestige bulk + Art5 sub-notes,src_nloterij_kb_definitief_2025,strong,"
    "Federal>Nationale_Loterij>verdelingsplan_2025_definitief,"
    "tick463 dual vs provisional 200m; residual prestige 10m sub-L5 and Art5 committee notes"
)
with (data / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write("\n" + cmt + "\n")

lb = data / "leaderboard.csv"
text = lb.read_text(encoding="utf-8")
old_plan = (
    "lb_nloterij_plan_2025_200m,NL provisional verdelingsplan 2025 200m named L5 table,federal,programme,"
    "Federal>Nationale_Loterij>verdelingsplan_2025,200000000,200000000,Strong KB 28 Jul 2025 full L5; dual 2024 plan; "
    "culture protocol 7m embedded,strong,src_nloterij_kb_voorlopig_2025,Communities DGD KBF culture sport,"
    "Statutory lottery redistribution,Core public path; residual definitive,3.5,7.5,4,5.7,"
    "Publish definitive KB open data,seed,,tick461"
)
new_plan = (
    "lb_nloterij_plan_2025_200m,NL provisional verdelingsplan 2025 200m (superseded by definitive 240m),federal,programme,"
    "Federal>Nationale_Loterij>verdelingsplan_2025_prov,200000000,200000000,Strong provisional KB; superseded tick463 "
    "definitive 240m (+40m),strong,src_nl_2025_def_vs_prov_recon,Communities DGD KBF culture sport,"
    "Statutory lottery redistribution provisional,Superseded by definitive,3.5,7.5,4,5.7,Use definitive rows,seed,,tick463 dual"
)
if old_plan in text:
    text = text.replace(old_plan, new_plan)
else:
    print("WARN plan200 not exact")

old_pres = (
    "lb_nl_prestige_6_18m_2025,Nationaal Prestige pot 6.176m provisional 2025 (cut vs 10.7m 2024),federal,ops,"
    "Federal>NL>prestige_2025,6176015,6176015,Strong plan L5; large cut vs 2024 provisional 10.656m; bulk opacity residual,"
    "strong,src_nloterij_kb_voorlopig_2025,Culture/sport prestige orgs,Discretionary prestige envelope,Opacity high; dual 2024,"
    "5.0,5.5,5,5.2,Publish named prestige L5,seed,,tick461"
)
new_pres = (
    "lb_nl_prestige_6_18m_2025,Nationaal Prestige pot provisional 6.176m 2025 (definitive 10.000m),federal,ops,"
    "Federal>NL>prestige_2025_prov,6176015,6176015,Provisional only; definitive KB restored pot to 10.000016m tick463; "
    "bulk sub-L5 still opaque,strong,src_nloterij_kb_definitief_2025,Culture/sport prestige orgs,"
    "Discretionary prestige envelope,Opacity high bulk,5.0,5.5,5,5.2,FOI prestige sub-list,seed,,tick463 dual"
)
if old_pres in text:
    text = text.replace(old_pres, new_pres)
else:
    print("WARN prestige not exact")

lb_new = [
    "lb_nl_plan_def_240m_2025,NL definitive verdelingsplan 2025 240m full L5 table,federal,programme,"
    "Federal>Nationale_Loterij>verdelingsplan_2025_def,240000000,240000000,Strong KB 5 Jun 2026; +40m vs provisional; "
    "dual culture equality sport health named,strong,src_nloterij_kb_definitief_2025,"
    "Communities DGD KBF culture sport society,Statutory lottery redistribution definitive,"
    "Core public path; residual prestige bulk + Art5 notes,3.5,8.0,3,5.9,Open-data L5 table; FOI prestige sub,seed,,tick463",
    "lb_nl_lov2030_10_5m,LOV2030 Leuven European Capital of Culture 10.5m definitive 2025,federal,ops,"
    "Federal>NL>LOV2030,10500000,10500000,Strong named L5 multi-year frame to 2030; largest new definitive line vs provisional,"
    "strong,src_nloterij_kb_definitief_2025,Leuven cultural capital partners,EU capital of culture co-finance,"
    "Large multi-year lottery culture; outcome KPIs residual,4.0,6.5,4,5.3,Publish multi-year cash schedule,seed,,tick463",
    "lb_nl_prestige_def_10m_2025,Nationaal Prestige pot 10.000m definitive 2025,federal,ops,"
    "Federal>NL>prestige_2025_def,10000016,10000016,Strong pot total; sub-allocation residual (ministerial discretion opacity),"
    "strong,src_nloterij_kb_definitief_2025,Various prestige projects,Discretionary national prestige grants,"
    "Highest opacity inside definitive plan,5.5,6.0,5,5.6,FOI sub-list L5 names,seed,,tick463",
    "lb_nl_proleague_3_5m,Pro League FSR safety innovation 3.5m definitive 2025,federal,ops,"
    "Federal>NL>Pro_League,3500000,3500000,Strong named NEW definitive; dual sport lottery stack,"
    "strong,src_nloterij_kb_definitief_2025,Professional football clubs public,Football social responsibility safety innovation,"
    "Named L5; private-league public lottery,4.0,5.0,3,4.5,Publish use of funds report,seed,,tick463",
    "lb_nl_def_vs_prov_40m,NL 2025 definitive vs provisional uplift 40m,federal,ops,"
    "Federal>NL>def_vs_prov_2025,40000000,40000000,Strong recon 240-200; LOV2030 Pro League prestige women sport drive uplift class,"
    "strong,src_nl_2025_def_vs_prov_recon,Belgian society grantees,Plan revision transparency,"
    "Method: always dual definitive when published,3.5,7.0,3,5.3,Track future definitive lags,seed,,tick463",
]
text = text.rstrip("\n") + "\n" + "\n".join(lb_new) + "\n"
lb.write_text(text, encoding="utf-8")

rq = data / "research_queue.csv"
rq_text = rq.read_text(encoding="utf-8")
old_rq = (
    "rq_454,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T21:45:00Z,,"
    "Spawned tick462 after CPVS dual; rq_116 SWA deferred"
)
new_rq = (
    "rq_454,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T21:45:00Z,2026-08-02T22:15:00Z,"
    "tick463: NL definitive 2025 plan 240m (+40m vs prov); Prestige 10m LOV2030 10.5 Pro League 3.5; rq_116 deferred"
)
if old_rq in rq_text:
    rq_text = rq_text.replace(old_rq, new_rq)
else:
    print("WARN rq_454")
    for line in rq_text.splitlines():
        if line.startswith("rq_454,"):
            print(line[:160])
rq_text = rq_text.rstrip("\n") + "\n"
rq_text += (
    "rq_455,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,2026-08-02T22:15:00Z,,"
    "Spawned tick463 after NL definitive 240m; rq_116 SWA deferred\n"
)
rq.write_text(rq_text, encoding="utf-8")

foi = data / "foi_queue.csv"
foi_text = foi.read_text(encoding="utf-8")
if "gap_nl_prestige_l5" not in foi_text:
    foi_row = (
        "gap_nl_prestige_l5,Federal>Nationale_Loterij>Nationaal_Prestige>L5,nationale_loterij,"
        "Named L5 list of Nationaal Prestige 10.000016m definitive 2025 beneficiaries amounts; "
        "Art5 sub-notes for cats 3.17 3.31 3.32 5.3 5.5 5.6 5.10,"
        "Largest opacity pot inside 240m definitive plan; multi-year LOV/EYOF frames partly named,"
        "6,Nationale Loterij / FOD Financien / Kanselarij FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
        "docs/doge/foi/drafts/gap_nl_prestige_l5.md,ready,2026-08-02,,,,,"
        "cmt_nloterij_plan_definitief_2025,lb_nl_prestige_def_10m_2025,"
        "2026-08-02T22:15:00Z,2026-08-02T22:15:00Z,"
        "tick463 draft ready human send; pot total strong public sub-L5 residual"
    )
    foi_text = foi_text.rstrip("\n") + "\n" + foi_row + "\n"
    foi.write_text(foi_text, encoding="utf-8")
    print("FOI gap_nl_prestige_l5 added")
else:
    print("FOI prestige exists")

(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_454,463,no,"
    "Scheduler 60s. Next prio5 rq_455; rq_116 SWA deferred. tick463 NL definitive 240m.\n",
    encoding="utf-8",
)
print("OK", root)
