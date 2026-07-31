# tick 318 — AGMJ ETP 801 + FWB DO11 traitements 437.6m + MDJ initiatives (Exposé 2026)
from pathlib import Path
import re

base = Path("docs/doge/data")

def append(name: str, text: str) -> None:
    path = base / name
    with open(path, "a", encoding="utf-8", newline="") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    "src_fwb_expose_gen_dep_2026,FWB Expose general des depenses 2026 Initial AGMJ ETP DO11 traitements,"
    "https://budget-finances.cfwb.be/fileadmin/sites/dgbf/uploads/documents/budget_comptabilite/ressources/budgets/2026/Expose_general_des_depenses_2026_-_Initial.pdf,"
    "Federation Wallonie-Bruxelles Budget,2026-07-30,primary,"
    '"Strong: AGMJ 801 ETP 30jun2025; admin total 6427 ETP; DO11 AB11.03+11.04 traitements 437.6m BI2026; '
    'AGMJ+AGAJ new 5.4m + MDJ carceral 3.4m; ETNIC moyens 123m BI2026; raw fwb_expose_gen_dep_2026.pdf"',
)

# entity update fwb_maisons_justice
ents = (base / "entities.csv").read_text(encoding="utf-8")
m = re.search(r"^fwb_maisons_justice,.*$", ents, re.M)
if m and "tick318" not in m.group(0):
    old = m.group(0)
    parts = old.rstrip("\n").split(",")
    parts[-1] = parts[-1] + "; Expose2026 AGMJ 801 ETP; DO11 traitements pack 437.6m ministry; new 5.4+3.4m; tick318"
    ents = ents.replace(old, ",".join(parts))
    (base / "entities.csv").write_text(ents, encoding="utf-8")

append(
    "entities.csv",
    "agmj,AGMJ Administration generale des Maisons de Justice,AGMJ,"
    "FWB general administration justice houses,agency,fwb_gov,fr,"
    "https://www.maisonsdejustice.be,,,,"
    "801 ETP 30jun2025 strong Expose2026; wage stock FOI inside DO11 437.6m; dual VL AJH; tick318",
)

append(
    "budgets.csv",
    "bud_agmj_etp_2025_06,agmj,2025,801,,,outturn,src_fwb_expose_gen_dep_2026,strong,"
    "AGMJ effectifs 801 ETP courant 30/06/2025 (102+535+149+15 grades) Expose gen 2026\n"
    "bud_agaj_etp_2025_06,fwb_aide_jeunesse,2025,2018,,,outturn,src_fwb_expose_gen_dep_2026,strong,"
    "AGAJ effectifs 2018 ETP 30/06/2025 Expose gen 2026\n"
    "bud_fwb_admin_etp_2025_06,fwb_gov,2025,6427,,,outturn,src_fwb_expose_gen_dep_2026,strong,"
    "FWB administration total 6427 ETP 30/06/2025 (SG 1083 AGE 1332 AGAJ 2018 AGMJ 801 etc)\n"
    "bud_fwb_do11_traitements_2026,fwb_gov,2026,437600000,,,budgeted,src_fwb_expose_gen_dep_2026,strong,"
    "DO11 prog01 AB 11.03+11.04 traitements fonction publique 437.6m BI2026 (+10.9m vs init2025); ministry-wide not AGMJ-only\n"
    "bud_fwb_mdj_agaj_personnel_new_2026,fwb_maisons_justice,2026,5400000,,,budgeted,src_fwb_expose_gen_dep_2026,strong,"
    "New initiatives renforcement services AGMJ et AGAJ 5.4m inside DO11 traitements pack BI2026\n"
    "bud_fwb_mdj_carceral_new_2026,fwb_maisons_justice,2026,3400000,,,budgeted,src_fwb_expose_gen_dep_2026,strong,"
    "Renforcement maisons de justice reforme carcerale 3.4m BI2026\n"
    "bud_fwb_mdj_partner_nonindex_cut_2026,fwb_maisons_justice,2026,-449000,,,budgeted,src_fwb_expose_gen_dep_2026,strong,"
    "Non-indexation temporaire subventions services partenaires MDJ -449k BI2026\n"
    "bud_fwb_mdj_formation_cuts_2026,fwb_maisons_justice,2026,-321000,,,budgeted,src_fwb_expose_gen_dep_2026,strong,"
    "Formation generique -156k + urgences collectives formation -165k BI2026\n"
    "bud_etnic_moyens_bi2026,etnic,2026,123000000,,,budgeted,src_fwb_expose_gen_dep_2026,medium-strong,"
    "ETNIC moyens budgetaires BI2026 123m (from 119.4m init2025 +3.5m); may differ CoA full recettes perimeter tick314",
)

cash_mdj = (
    '"{""agmj_etp_2025_06"":801,""agaj_etp_2025_06"":2018,'
    '""admin_etp_total"":6427,""do11_traitements_2026"":437600000,'
    '""agmj_agaj_new_2026"":5400000,""mdj_carceral_new_2026"":3400000,'
    '""partner_nonindex"":-449000,""formation_cuts"":-321000,'
    '""note"":""AGMJ wage stock still not split from DO11 437.6m""}"'
)

append(
    "commitments.csv",
    "cmt_agmj_etp_do11_path_2025_26,AGMJ ETP 801 and FWB DO11 traitements path dual VL AJH,"
    "agmj,Maisons de Justice justiciables FWB,"
    "Expose general depenses FWB 2026 + prior DO18 path,"
    f"2025-06-30,2025,2026,437600000,{cash_mdj},,active,,"
    "Community justice houses personnel capacity,"
    "Publish AGMJ-only wage bill FTE cash series; dual unit-cost vs VL AJH lonen 164.9m,"
    "src_fwb_expose_gen_dep_2026,strong,FWB>Maisons_de_Justice>AGMJ>personnel,"
    "tick318: ETP 801 strong; new 5.4+3.4m strong; residual AGMJ wage stock inside 437.6m FOI",
)

append(
    "leaderboard.csv",
    "lb_agmj_etp_801,AGMJ Maisons de Justice 801 ETP mid-2025,FWB,ops,"
    "FWB>Maisons_de_Justice>AGMJ>ETP,801,801,"
    "Strong Expose2026: 801 ETP 30jun2025; dual VL AJH personnel slice residual; federal receipt 55.7m DO18 30.1m prior,"
    "strong,src_fwb_expose_gen_dep_2026,Justiciables victims FWB,"
    "Community sentence execution capacity,"
    "Core justice ops; wage EUR stock still FOI inside DO11 437.6m; dual triple with DG Justizhaus,"
    "4,5.5,4,4.9,Publish AGMJ wage bill; dual unit-cost VL AJH,seed,,tick318\n"
    "lb_fwb_do11_traitements_438m,FWB DO11 public function traitements 437.6m BI2026,FWB,ops,"
    "FWB>Fonction_publique>DO11>traitements,437600000,437600000,"
    "Strong Expose2026: AB 11.03+11.04 total 437.6m (+10.9m); includes AGMJ/AGAJ new 8.9m class; not AGMJ-only,"
    "strong,src_fwb_expose_gen_dep_2026,FWB administration staff,"
    "Ministry-wide wage envelope,"
    "Core admin; AGMJ share opaque; dual VL AJH lonen 164.9m comparison needs AGMJ split,"
    "3,8.0,4,5.5,Split by AG (AGMJ AGAJ AGE SG) cash series,seed,,tick318\n"
    "lb_fwb_mdj_personnel_new_8_8m,FWB MDJ/AGAJ personnel new initiatives 8.8m BI2026,FWB,ops,"
    "FWB>Maisons_de_Justice>personnel_new,8800000,8800000,"
    "Strong: 5.4m AGMJ+AGAJ + 3.4m carceral MDJ reinforcement inside DO11; partner cut -449k parallel,"
    "strong,src_fwb_expose_gen_dep_2026,Justiciables prison reform,"
    "Capacity boost community justice,"
    "Incremental only; stock wage FOI; dual VL,"
    "4,5.0,3,4.3,Track outturn vs budget; FTE delivery,seed,,tick318",
)

# FOI update gap_fwb_mdj_personnel_total
foi = (base / "foi_queue.csv").read_text(encoding="utf-8")
# find and update notes field for gap
old_frag = "tick245 draft ready human send; new initiatives public stock residual | tick255: AGMJ 801 ETP public wage residual"
new_frag = (
    "tick245|255|318: AGMJ 801 ETP + DO11 traitements 437.6m + new 5.4+3.4m strong Expose2026; "
    "residual AGMJ-only wage cash stock still FOI human send"
)
if old_frag not in foi:
    # try alternate
    if "gap_fwb_mdj_personnel_total" not in foi:
        raise SystemExit("gap not found")
    # append note via simpler replace on last known
    foi = foi.replace(
        "tick255: AGMJ 801 ETP public wage residual",
        "tick255+318: AGMJ 801 ETP confirmed Expose2026; DO11 437.6m; residual AGMJ wage cash stock FOI",
    )
else:
    foi = foi.replace(old_frag, new_frag)
(base / "foi_queue.csv").write_text(foi, encoding="utf-8")

# research_queue
rq = (base / "research_queue.csv").read_text(encoding="utf-8")
old = (
    "rq_309,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; other FOI-adjacent dual/L5). Prefer before idle. "
    "Note progress@320 soon.,,2026-07-30T21:15:00Z,,Spawned tick317 after NMBS dual FTE; rq_116 SWA deferred"
)
new = (
    "rq_309,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (AGMJ if extractable; other FOI-adjacent dual/L5). Prefer before idle. "
    "Note progress@320 soon.,gap_fwb_mdj_personnel_total,"
    "2026-07-30T21:15:00Z,2026-07-30T21:45:00Z,"
    "tick318: AGMJ 801 ETP + DO11 traitements 437.6m + MDJ new 8.8m; residual wage FOI; spawn rq_310 progress@320 prep\n"
    "rq_310,Mandatory progress@320 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
    "When ticks_completed hits 320: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE and "
    "doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    "2026-07-30T21:45:00Z,,Spawned tick318; do at tick 320\n"
    "rq_311,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@320. Prefer before idle.,,"
    "2026-07-30T21:45:00Z,,Spawned tick318; after progress@320"
)
if old not in rq:
    raise SystemExit("rq_309 not found")
(base / "research_queue.csv").write_text(rq.replace(old, new), encoding="utf-8")

(base / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T21:45:00Z,rq_309,318,no,"
    "Scheduler 60s. Next prio5 rq_311 or progress rq_310 at tick320; rq_116 SWA deferred. "
    "tick318 AGMJ 801 ETP + DO11 437.6m.\n",
    encoding="utf-8",
)

print("tick318 CSV writes OK")
