# tick 283 — CGVS dual Fedasil asylum decision body
import json
from pathlib import Path

base = Path("docs/doge/data")
now = "2026-07-30T04:15:00Z"

with open(base / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_cgvs_jv_2024,CGVS Jaarverslag 2024 budget VTE Smals dual Fedasil,"
        "docs/doge/data/raw/cgvs_jv_2024.pdf,CGVS Commissariaat-generaal Vluchtelingen,2026-07-30,agency,"
        "Budget available 61.979m spent 57.032m 92pct 2024; personeel 47.005m; Smals/eGOV 1.809m; "
        "VTE 600.9; dual Fedasil 943m; tick283\n"
    )

with open(base / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cgvs,Commissariaat-generaal voor de Vluchtelingen en de Staatlozen CGVS,"
        "Commissariat general aux refugies et aux apatrides CGRA,"
        "Office of the Commissioner General for Refugees and Stateless Persons,agency,sec_federal,bi,"
        "https://www.cgvs.be,,,Asylum status decisions dual Fedasil reception; spend 57.0m 2024; VTE 601; Smals 1.8m; tick283\n"
    )

bud = [
    "bud_cgvs_budget_available_2024,cgvs,2024,61979079,,,budgeted,src_cgvs_jv_2024,strong,Beschikbaar budget 61.979.079 2024 (FOD IBZ)",
    "bud_cgvs_spend_2024,cgvs,2024,57032155,,,outturn,src_cgvs_jv_2024,strong,Gerealiseerde vereffeningskredieten 57.032.155 (92pct of available)",
    "bud_cgvs_statutair_2024,cgvs,2024,35927683,,,outturn,src_cgvs_jv_2024,strong,Statutair personeel 35.927.683",
    "bud_cgvs_contractueel_2024,cgvs,2024,11077167,,,outturn,src_cgvs_jv_2024,strong,Contractueel personeel 11.077.167",
    "bud_cgvs_personeel_total_2024,cgvs,2024,47004850,,,outturn,src_cgvs_jv_2024,strong,Personeel sum 47.004.850 (~82pct of spend)",
    "bud_cgvs_werking_2024,cgvs,2024,6920595,,,outturn,src_cgvs_jv_2024,strong,Algemene werkingsuitgaven 6.920.595",
    "bud_cgvs_ict_2024,cgvs,2024,744361,,,outturn,src_cgvs_jv_2024,strong,Werkingsuitgaven ICT 744.361",
    "bud_cgvs_telewerk_2024,cgvs,2024,369909,,,outturn,src_cgvs_jv_2024,strong,Forfaitaire onkosten telewerk 369.909",
    "bud_cgvs_smals_egov_2024,cgvs,2024,1809222,,,outturn,src_cgvs_jv_2024,strong,Personeel eGOV en Smals 1.809.222 dual Smals 579m",
    "bud_cgvs_invest_2024,cgvs,2024,183218,,,outturn,src_cgvs_jv_2024,strong,Invest general 102.463 + ICT 80.755 = 183.218",
    "bud_cgvs_vte_2024,cgvs,2024,600.9,,,outturn,src_cgvs_jv_2024,strong,VTE total 600.9 end-2024 (A 479.2 + other 121.7); amount is FTE count",
]
with open(base / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for r in bud:
        f.write(r + "\n")

cash = {
    "budget_available_2024": 61979079,
    "spend_2024": 57032155,
    "spend_pct": 92,
    "personeel_2024": 47004850,
    "statutair": 35927683,
    "contractueel": 11077167,
    "werking": 6920595,
    "ict": 744361,
    "smals_egov": 1809222,
    "invest": 183218,
    "vte_2024": 600.9,
    "vte_2023": 582.77,
    "vte_2020": 471.29,
    "hires_2024": 71,
    "leavers_2024": 57,
    "amif_projects": "3 projects 2022-25 residual EUR FOI",
    "note": "Dual Fedasil reception 943m 2024; asylum decision body not reception; Smals dual",
}
j = '"' + json.dumps(cash, separators=(",", ":")).replace('"', '""') + '"'
cmt = (
    "cmt_cgvs_budget_2024,CGVS asylum status decision agency dual Fedasil,"
    "cgvs,Asylum applicants refugees stateless,"
    "Asielwet + FOD IBZ kredieten,2024-01-01,2024,2025,61979079,"
    + j
    + ",0,active,docs/doge/data/raw/cgvs_jv_2024.pdf,"
    "Decide international protection status claims,"
    "FOI AMIF cash multi-year; dual unit-cost Fedasil; track backlog KPI,"
    "src_cgvs_jv_2024,strong,Federal>Asiel>CGVS,tick283 dual Fedasil Smals\n"
)
with open(base / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lb = [
    "lb_cgvs_spend_57m,CGVS spend 57.0m 2024 dual Fedasil,federal,ops,Federal>Asiel>CGVS,57032155,57032155,Strong JV: vereffening 57.032m of 61.979m available 92pct; core asylum decision body not pure waste; dual Fedasil 943m reception,strong,src_cgvs_jv_2024,Asylum applicants,International protection status decisions,Core dual reception stack Fedasil,3,6.5,3,5.15,FOI AMIF; dual unit-cost per decision,seed,,tick283",
    "lb_cgvs_pers_47m,CGVS personnel 47.0m 2024,federal,ops,Federal>Asiel>CGVS>personnel,47004850,47004850,Strong: statutair 35.9 + contractueel 11.1 = 47.0m ~82pct of spend; VTE 600.9,strong,src_cgvs_jv_2024,CGVS staff,Protection officers admin,Core capacity high caseload,3,6.5,3,5.15,Track VTE vs output decisions,seed,,tick283",
    "lb_cgvs_smals_1_8m,CGVS Smals eGOV 1.8m 2024 dual Smals,federal,ops,Federal>Asiel>CGVS>Smals,1809222,1809222,Strong JV line: Personeel eGOV en Smals 1.809m; dual Smals institutional 579m L5 sample,strong,src_cgvs_jv_2024,Smals eGOV,Digital dossier support,Middleman dual Smals stack,4,4.0,3,4.1,Reconcile into gap_smals_l5_members,seed,,tick283 dual Smals",
    "lb_asylum_dual_fedasil_cgvs,Asylum dual Fedasil 943m + CGVS 57m,federal,ops,BE>Asiel>dual_Fedasil_CGVS,0,0,Strong dual: Fedasil reception spend 943m 2024 + CGVS decision 57m; not additive full chain (also DVZ RvV); volume-driven,strong,src_cgvs_jv_2024,Asylum seekers system,Reception + status determination,Institutional dual chain,4,9.0,5,6.5,FOI still gap_fedasil_l5_partners; dual unit-cost,seed,,tick283 dual not additive",
]
with open(base / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        f.write(r + "\n")

# update related FOI
foi_path = base / "foi_queue.csv"
lines = foi_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
out = []
for line in lines:
    if line.startswith("gap_fedasil_l5_partners,") and "tick283" not in line:
        line = line.rstrip() + " | tick283: CGVS decision 57m dual public"
    if line.startswith("gap_smals_l5_members,") and "tick283" not in line:
        line = line.rstrip() + " | tick283: CGVS Smals/eGOV 1.809m public line"
    out.append(line)
gap = "gap_cgvs_amif_2022_25"
if not any(l.startswith(gap + ",") for l in out):
    out.append(
        f"{gap},Federal>CGVS>AMIF_projects,cgvs,"
        "Cash-by-year AMIF EU+national co-finance 2022-2025 for three named CGVS projects "
        "(tolken quality, digitalisation eDossier, GEAS strengthening); multi-year budget 2025-26 path,"
        "National spend 57m strong; AMIF residual; dual Fedasil EU funds,"
        "4,CGVS / FOD Binnenlandse Zaken Cel Europese Fondsen,cgvs.info@ibz.fgov.be,"
        "https://www.cgvs.be,"
        f"docs/doge/foi/drafts/{gap}.md,ready,2026-07-30,,,,,,"
        f"cmt_cgvs_budget_2024,lb_cgvs_spend_57m,{now},{now},"
        "tick283 draft ready human send; national budget filled"
    )
foi_path.write_text("\n".join(out) + "\n", encoding="utf-8")

rq_path = base / "research_queue.csv"
rq = rq_path.read_text(encoding="utf-8").splitlines()
out = []
for line in rq:
    if line.startswith("rq_274,"):
        out.append(
            "rq_274,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after NBB).,"
            f"gap_cgvs_amif_2022_25,2026-07-30T03:45:00Z,{now},"
            "tick283: CGVS spend 57.0m VTE 601 dual Fedasil Smals 1.8m; spawn rq_275"
        )
    else:
        out.append(line)
if not any(l.startswith("rq_275,") for l in out):
    out.append(
        "rq_275,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after CGVS).,,"
        f"{now},,Spawned tick283 after CGVS; rq_116 SWA deferred"
    )
rq_path.write_text("\n".join(out) + "\n", encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},rq_274,283,no,"
    "Scheduler 60s. Next prio5 rq_275; rq_116 SWA deferred. FOI ready human send. tick283 CGVS 57.0m dual Fedasil.\n",
    encoding="utf-8",
)
print("OK tick283")
