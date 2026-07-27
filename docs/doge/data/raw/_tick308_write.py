# tick 308 — rq_299 Raad van State + IBZ-hosted independents pack
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T16:45:00Z"
unit = "rq_299"

src_line = (
    "src_ibz_rvs_hosted_2025,"
    "FOD IBZ Strategisch plan 2025-2029 hosted Raad van State AIG OCAD table,"
    "docs/doge/data/raw/ibz_strategisch_plan_2025_2029.pdf,"
    "FOD Binnenlandse Zaken,2026-07-30,official_budget,"
    "INI2025 parliament 26Jun2025: Raad van State VL 49.978m VE 49.971m; "
    "AIG 9.052/9.045; OCAD 4.121/4.123; dual CGVS RVV already mapped; tick308\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

# entities
ent_path = ROOT / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
adds = []
if "raad_van_state," not in ent:
    adds.append(
        "raad_van_state,Raad van State,Conseil d'Etat,"
        "Council of State administrative court and legislative advisory,"
        "court,sec_federal,bi,https://www.raadvst-consetat.be,,,,"
        "IBZ-hosted kredieten ~50m 2025 (not Kamer-dotatie); dual Grondwettelijk Hof ~14.5m Kamer-dotatie; tick308\n"
    )
if "aig_politie," not in ent:
    adds.append(
        "aig_politie,Algemene Inspectie federale en lokale politie AIG,"
        "Inspection generale police federale et locale,"
        "General Inspectorate of federal and local police,agency,sec_federal,bi,"
        "https://www.aigpol.be,,,,"
        "IBZ-hosted ~9.05m 2025; dual Comite P Kamer-dotatie police oversight; tick308\n"
    )
if "ocad_cuta," not in ent:
    adds.append(
        "ocad_cuta,Coordinatieorgaan voor de dreigingsanalyse OCAD,"
        "Organe de coordination pour l'analyse de la menace OCAM,"
        "Coordination Unit for Threat Analysis,agency,sec_federal,bi,"
        "https://www.ocam.belgium.be,,,,"
        "IBZ-hosted ~4.12m 2025; threat analysis dual intelligence Comite I; tick308\n"
    )
if adds:
    ent_path.write_text(ent.rstrip("\n") + "\n" + "".join(adds), encoding="utf-8")

bud_rows = [
    "bud_rvs_vl_2025,raad_van_state,2025,49978000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ INI2025 VL 49.978m hosted under FOD Binnenlandse Zaken",
    "bud_rvs_ve_2025,raad_van_state,2025,49971000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ INI2025 VE 49.971m; matches prior bud_ibz_raad_van_state_2025 on sec_federal",
    "bud_aig_vl_2025,aig_politie,2025,9052000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ hosted AIG VL 9.052m 2025",
    "bud_aig_ve_2025,aig_politie,2025,9045000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ hosted AIG VE 9.045m 2025",
    "bud_ocad_vl_2025,ocad_cuta,2025,4121000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ hosted OCAD VL 4.121m 2025",
    "bud_ocad_ve_2025,ocad_cuta,2025,4123000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "IBZ hosted OCAD VE 4.123m 2025",
    "bud_ibz_hosted_judicial_pack_2025,gg_belgium,2025,139009000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "Sum VE 2025: RvS 49.971 + CGVS 58.801 + RVV 30.236 = 139.008m class judicial/admin independents hosted IBZ",
    "bud_ibz_hosted_oversight_pack_2025,gg_belgium,2025,63139000,,,budgeted,src_ibz_rvs_hosted_2025,strong,"
    "Sum VE: RvS 49.971 + AIG 9.045 + OCAD 4.123 = 63.139m non-asylum oversight/judicial hosted IBZ",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_raad_van_state_2025,Raad van State IBZ-hosted budget 2025 ~50m,raad_van_state,"
        "Litigants administration legislators (advisory+contentious),"
        "Coordinated laws Council of State + FOD IBZ hosted kredieten,1831-01-01,2025,2025,49971000,"
        '"{""vl_2025_k"":49978,""ve_2025_k"":49971,""host"":""FOD_IBZ_not_Kamer_dotatie"",'
        '""dual_gwh_kamer_kred_2026"":14520720,'
        '""dual_rvv_2025"":30236000,'
        '""note"":""Administrative supreme court + legislative advisory; financing via IBZ not Kamer Comptabiliteit pack""}",'
        "0,active,docs/doge/data/raw/ibz_strategisch_plan_2025_2029.pdf,"
        "Administrative justice and legislative advisory opinions,"
        "Core judiciary; FOI multi-year FTE personnel/ops L5; dual Hof Kamer-dotatie model,"
        "src_ibz_rvs_hosted_2025,strong,Federal>IBZ_hosted>Raad_van_State,tick308"
    ),
    (
        "cmt_aig_politie_2025,AIG police inspectorate IBZ-hosted ~9.05m 2025,aig_politie,"
        "Police accountability citizens,Police inspection statute + IBZ host,1998-01-01,2025,2025,9045000,"
        '"{""vl_2025_k"":9052,""ve_2025_k"":9045,""dual_comite_p_approved_2026"":14272213,'
        '""note"":""Internal/admin police inspection dual Comite P external parliamentary oversight""}",'
        "0,active,docs/doge/data/raw/ibz_strategisch_plan_2025_2029.pdf,"
        "General inspection federal and local police,"
        "Dual Comite P ~14.3m Kamer-dotatie; FOI L5 optional,"
        "src_ibz_rvs_hosted_2025,strong,Federal>IBZ_hosted>AIG,tick308"
    ),
    (
        "cmt_ocad_2025,OCAD threat analysis IBZ-hosted ~4.12m 2025,ocad_cuta,"
        "Security services coordination,OCAD law + IBZ host,2006-01-01,2025,2025,4123000,"
        '"{""vl_2025_k"":4121,""ve_2025_k"":4123,""dual_comite_i_approved_2026"":6187100,'
        '""note"":""Threat analysis dual Comite I intelligence parliamentary oversight""}",'
        "0,active,docs/doge/data/raw/ibz_strategisch_plan_2025_2029.pdf,"
        "Coordinate terrorism threat analysis,"
        "Core security; dual Comite I,"
        "src_ibz_rvs_hosted_2025,strong,Federal>IBZ_hosted>OCAD,tick308"
    ),
    (
        "cmt_ibz_hosted_independents_2025,IBZ-hosted independent organs pack 2025,"
        "gg_belgium,Independent judicial and oversight bodies hosted on IBZ budget,"
        "FOD IBZ INI2025 global table,2025-06-26,2025,2025,152188000,"
        '"{""rvs_ve"":49971,""aig_ve"":9045,""ocad_ve"":4123,""cgvs_ve"":58801,""rvv_ve"":30236,'
        '""vclp_ve"":1745,""tuchtraad_ve"":68,""vct_ve"":44,""beleidsorganen_ve"":6604,'
        '""sum_named_ve_k"":160637,""note"":""Hosted credits not FOD own missions; dual Kamer-dotatie pack 149m 2026 separate financing channel""}",'
        "0,active,docs/doge/data/raw/ibz_strategisch_plan_2025_2029.pdf,"
        "Map dual financing of democratic control bodies IBZ host vs Kamer dots,"
        "Do not double-count with Kamer 9-inst pack; publish multi-year,"
        "src_ibz_rvs_hosted_2025,strong,Federal>IBZ>hosted_independents,tick308"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_raad_van_state_50m,Raad van State IBZ-hosted ~50.0m 2025,federal,ops,"
        "Federal>IBZ_hosted>Raad_van_State,49971000,49971000,"
        "Strong IBZ: VL 49.978m VE 49.971m INI2025; dual Grondwettelijk Hof ~14.5m Kamer-dotatie different finance,"
        "strong,src_ibz_rvs_hosted_2025,Litigants legislators,Administrative justice + legislative advice,"
        "Core judiciary; financing opacity multi-year FTE residual,"
        "2,6.5,2,4.0,FOI multi-year personnel/ops; dual Hof model,"
        "seed,,tick308"
    ),
    (
        "lb_dual_rvs_vs_gwh_finance,Dual finance Raad van State 50m IBZ vs Hof 14.5m Kamer-dotatie,federal,ops,"
        "Federal>Courts>dual_finance_models,49971000,64491720,"
        "Strong dual: RvS ~50m IBZ-hosted 2025 + GWH approved kred 14.52m 2026; not additive same function; different channels,"
        "strong,src_ibz_rvs_hosted_2025,Taxpayers courts,Two apex court financing models,"
        "Institutional dual financing opacity; not pure waste,"
        "5,7.0,3,5.5,Publish comparative TCO both courts same method,"
        "seed,,tick308 dual structure"
    ),
    (
        "lb_aig_9m,AIG police inspectorate ~9.05m 2025,federal,ops,"
        "Federal>IBZ_hosted>AIG,9045000,9045000,"
        "Strong IBZ: 9.052/9.045m VL/VE 2025; dual Comite P ~14.3m Kamer-dotatie external,"
        "strong,src_ibz_rvs_hosted_2025,Citizens police,Police general inspection,"
        "Dual oversight stack with Comite P,"
        "3,4.5,2,3.5,Map dual unit cost Comite P vs AIG,"
        "seed,,tick308"
    ),
    (
        "lb_ocad_4_1m,OCAD threat analysis ~4.12m 2025,federal,ops,"
        "Federal>IBZ_hosted>OCAD,4123000,4123000,"
        "Strong IBZ: 4.121/4.123m 2025; dual Comite I ~6.2m Kamer-dotatie,"
        "strong,src_ibz_rvs_hosted_2025,Security services,Threat analysis coordination,"
        "Core security dual Comite I,"
        "2,3.5,2,2.8,Keep; dual intelligence map,"
        "seed,,tick308"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

# FOI
foi_line = (
    "gap_rvs_accounts_l5,Federal>IBZ_hosted>Raad_van_State>L5,raad_van_state,"
    "Multi-year budget/outturn 2022-2026 personnel vs ops vs invest; FTE magistrates and staff; "
    "reconcile IBZ hosted line 49.971m with institutional jaarrekening if separate; "
    "compare financing model to Grondwettelijk Hof Kamer-dotatie,"
    "2025 total strong from IBZ plan; L5 structure and multi-year path opaque; dual Hof ~14.5m material,"
    "5,Raad van State / FOD Binnenlandse Zaken openbaarheid,,"
    "https://www.raadvst-consetat.be,"
    "docs/doge/foi/drafts/gap_rvs_accounts_l5.md,ready,2026-07-30,,,,,,"
    "cmt_raad_van_state_2025,lb_raad_van_state_50m|lb_dual_rvs_vs_gwh_finance,"
    "2026-07-30T16:45:00Z,2026-07-30T16:45:00Z,tick308 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

# research queue
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_299,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Raad van State budget; AGMJ if extractable; other FOI-adjacent). Prefer before idle. Note progress@310 soon.,,"
    "2026-07-30T16:15:00Z,,Spawned tick307 after FIRM/CTRG + full Kamer table; rq_116 SWA deferred"
)
new = (
    "rq_299,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Raad van State budget; AGMJ if extractable; other FOI-adjacent). Prefer before idle. Note progress@310 soon.,"
    "gap_rvs_accounts_l5,2026-07-30T16:15:00Z,2026-07-30T16:45:00Z,"
    "tick308: RvS ~50m IBZ-hosted + AIG 9.05m OCAD 4.12m dual Hof/ComiteP/I; FOI L5; spawn rq_300 progress@310 next"
)
if old not in text:
    raise SystemExit("rq_299 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_300,Mandatory progress@310 coverage % + waste top10,continuous,6,open,L0,gg_belgium,"
    "When ticks_completed hits 310: refresh progress_every_10_ticks.md layers A-E vs EUR 347.956bn TE and doge_waste_top10_current.md by priority_index; append log; no invent euros.,,"
    "2026-07-30T16:45:00Z,,Spawned tick308 after RvS; progress@310 next after 2 more ticks or do at 310\n"
)
text += (
    "rq_301,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T16:45:00Z,,Spawned tick308; do after progress@310 if concurrent\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},308,no,"
    "Scheduler 60s. Next rq_301 hole-fill (or progress@310 at tick 310 via rq_300); "
    "rq_116 SWA deferred. tick308 RvS ~50m IBZ-hosted dual Hof.\n",
    encoding="utf-8",
)
print("OK")
