# tick 254 — rq_245 hub.brussels budget 2024
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T14:00:00Z"
tick = 254
unit = "rq_245"

# --- sources.csv ---
src_path = root / "docs/doge/data/sources.csv"
src_line = (
    "src_hub_brussels_rapport_2024,"
    "hub.brussels Rapport activite 2024 Annexe 2 budget recettes/depenses,"
    "docs/doge/data/raw/hub_brussels_rapport_activite_2024.pdf,"
    "hub.brussels / ABE,2026-07-29,agency,"
    "Total 46.166m 2024 (dot 42.007 + EU 1.353 + RBC 1.040 + FEDER 0.762 + autres 0.604 + propres 0.400); "
    "dep remun 31.875 actions 6.186 fonct 5.897; dual AWEX/FIT; tick254\n"
)
with open(src_path, "a", encoding="utf-8", newline="") as f:
    f.write(src_line)
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
ent_text = ent_path.read_text(encoding="utf-8")
if "hub_brussels," not in ent_text:
    ent_path.write_text(
        ent_text.rstrip("\n")
        + "\nhub_brussels,hub.brussels Agence bruxelloise pour l Entrepreneuriat ABE,"
        "hub.brussels Agence bruxelloise pour l Entrepreneuriat,"
        "Brussels Agency for Entrepreneurship (export FDI + enterprise support),"
        "parastatal,brussels_gov,bi,https://hub.brussels,,,"
        "Budget 46.166m 2024 strong; dual AWEX 76.8m + FIT FOI; 2026 intl office cut 33to21; tick254\n",
        encoding="utf-8",
    )
    print("entity added")
else:
    print("entity exists")

ent_text = ent_path.read_text(encoding="utf-8")
ent_text = ent_text.replace(
    "fit_flanders,Flanders Investment and Trade FIT,Flanders Investment and Trade,"
    "Flemish export and FDI agency,parastatal,vlaanderen_gov,nl,"
    "https://www.flandersinvestmentandtrade.com,,,Dual AWEX; official VEK residual FOI; tick253",
    "fit_flanders,Flanders Investment and Trade FIT,Flanders Investment and Trade,"
    "Flemish export and FDI agency,parastatal,vlaanderen_gov,nl,"
    "https://www.flandersinvestmentandtrade.com,,,"
    "Dual AWEX 76.8m + hub.brussels 46.2m 2024; official VEK residual FOI; tick254",
)
ent_text = ent_text.replace(
    "awex,AWEX Agence wallonne a l Exportation,"
    "AWEX Agence wallonne a l Exportation et aux Investissements etrangers,"
    "Wallonia Export and Investment Agency,parastatal,wallonie_gov,fr,https://www.awex.be,,,"
    "UAP; package 76.843m 2026; dual FIT Flanders + hub.brussels; tick253",
    "awex,AWEX Agence wallonne a l Exportation,"
    "AWEX Agence wallonne a l Exportation et aux Investissements etrangers,"
    "Wallonia Export and Investment Agency,parastatal,wallonie_gov,fr,https://www.awex.be,,,"
    "UAP; package 76.843m 2026; dual FIT FOI + hub.brussels 46.2m 2024; tick254",
)
ent_path.write_text(ent_text, encoding="utf-8")
print("entities updated")

# --- budgets ---
bud_path = root / "docs/doge/data/budgets.csv"
bud_rows = [
    "bud_hub_brussels_total_2024,hub_brussels,2024,46166000,,,outturn,src_hub_brussels_rapport_2024,strong,Rapport activite 2024 Annexe 2: recettes=depenses total 46.166m; dual AWEX/FIT export stack",
    "bud_hub_brussels_dotation_2024,hub_brussels,2024,42007000,,,outturn,src_hub_brussels_rapport_2024,strong,Regional dotation 42.007m of total 46.166m (~91pct)",
    "bud_hub_brussels_eu_fin_2024,hub_brussels,2024,1353000,,,outturn,src_hub_brussels_rapport_2024,strong,Financement EU 1.353m",
    "bud_hub_brussels_rbc_fin_2024,hub_brussels,2024,1040000,,,outturn,src_hub_brussels_rapport_2024,strong,Financement RBC other regional 1.040m",
    "bud_hub_brussels_feder_2024,hub_brussels,2024,762000,,,outturn,src_hub_brussels_rapport_2024,strong,Financement FEDER 0.762m",
    "bud_hub_brussels_autres_rec_2024,hub_brussels,2024,604000,,,outturn,src_hub_brussels_rapport_2024,strong,Autres recettes 0.604m",
    "bud_hub_brussels_propres_2024,hub_brussels,2024,400000,,,outturn,src_hub_brussels_rapport_2024,strong,Recettes propres 0.400m",
    "bud_hub_brussels_remun_2024,hub_brussels,2024,31875000,,,outturn,src_hub_brussels_rapport_2024,strong,Remunerations 31.875m (~69pct of total spend)",
    "bud_hub_brussels_actions_2024,hub_brussels,2024,6186000,,,outturn,src_hub_brussels_rapport_2024,strong,Frais d actions 6.186m",
    "bud_hub_brussels_fonct_2024,hub_brussels,2024,5897000,,,outturn,src_hub_brussels_rapport_2024,strong,Fonctionnement 5.897m",
    "bud_hub_brussels_loyers_2024,hub_brussels,2024,1383000,,,outturn,src_hub_brussels_rapport_2024,strong,Loyers 1.383m",
    "bud_hub_brussels_invest_2024,hub_brussels,2024,305000,,,outturn,src_hub_brussels_rapport_2024,strong,Investissements 0.305m",
    "bud_hub_brussels_transferts_2024,hub_brussels,2024,509000,,,outturn,src_hub_brussels_rapport_2024,strong,Transferts 0.509m",
]
with open(bud_path, "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")
print("budgets", len(bud_rows))

# --- commitments ---
cmt_path = root / "docs/doge/data/commitments.csv"
cash_json = (
    '{"total_2024": 46166000, "dotation_2024": 42007000, "eu": 1353000, '
    '"rbc": 1040000, "feder": 762000, "autres": 604000, "propres": 400000, '
    '"remun": 31875000, "actions": 6186000, "fonct": 5897000, "loyers": 1383000, '
    '"invest": 305000, "transferts": 509000, "intl_offices_pre_cut": 33, '
    '"intl_offices_post_2026": 21, '
    '"note": "2025-26 EUR package residual FOI after announced budget cuts; dual AWEX 76.8m 2026 FIT residual"}'
)
# escape quotes for CSV
cash_csv = cash_json.replace('"', '""')
cmt = (
    "cmt_hub_brussels_budget_2024,"
    "hub.brussels ABE Brussels export-enterprise agency package 2024 dual AWEX/FIT,"
    "hub_brussels,Brussels exporters starters FDI attraction network abroad,"
    "Ordonnance ABE; Rapport activite 2024 Annexe 2,2024-01-01,2024,2026,46166000,"
    f'"{cash_csv}",0,active,docs/doge/data/raw/hub_brussels_rapport_activite_2024.pdf,'
    "Export FDI + entrepreneurship support BCR,"
    "Map 2025-26 after cuts; dual unit-cost vs AWEX/FIT; L5 grants FOI,"
    "src_hub_brussels_rapport_2024,strong,Bruxelles>Economie>hub.brussels,"
    "tick254 triple export map; 2026 office network cut\n"
)
with open(cmt_path, "a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt ok")

# --- leaderboard ---
lb_path = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_hub_brussels_46_2m,hub.brussels package 46.2m 2024 dual AWEX/FIT export,Brussels,ops,Bruxelles>Economie>hub.brussels,46166000,46166000,Strong Rapport 2024: total 46.166m (dot 42.007 + EU/RBC/FEDER/autres/propres); remun 31.875m 69pct; 2026 cuts intl 33to21 EUR residual FOI,strong,src_hub_brussels_rapport_2024,Brussels exporters starters investors,Export FDI + enterprise support,Core dual/triple export agency; not pure waste,3,7.0,5,5.65,Publish dual matrix AWEX+FIT+hub; open 2025-26 after cuts,seed,,tick254",
    "lb_export_agencies_triple_awex_fit_hub,Export agencies triple AWEX 76.8 hub 46.2 FIT residual,Belgium,ops,BE>Export>triple_AWEX_FIT_hub,0,0,Strong triple: AWEX 76.843m 2026 + hub.brussels 46.166m 2024 + FIT Flanders VEK residual FOI; ACE 0.438m WAL; years differ not additive,strong,src_hub_brussels_rapport_2024,Exporters BE regional,Regional triple export promotion post-federalisation,Three regional export agencies + federal ACE layer,4,8.0,5,6.2,FOI FIT VEK + hub 2025-26; unit-cost exports per euro,seed,,tick254 triple not additive",
    "lb_hub_brussels_remun_share,hub.brussels remunerations 69pct of package,Brussels,ops,Bruxelles>hub.brussels>personnel,31875000,31875000,Strong: remun 31.875m of 46.166m total 2024 (~69pct); dual opacity on FTE,strong,src_hub_brussels_rapport_2024,Agency staff,Wage bill of entrepreneurship agency,High wage share typical agency; FTE residual,4,6.5,4,5.55,Publish FTE and dual unit-cost vs AWEX/FIT,seed,,tick254",
]
with open(lb_path, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb", len(lb_rows))

# --- foi_queue ---
foi_path = root / "docs/doge/data/foi_queue.csv"
foi = (
    "gap_hub_brussels_budget_2025_26,Bruxelles>hub.brussels>budget_2025_26,hub_brussels,"
    "hub.brussels / ABE full budget 2025 and 2026 (dotation + EU/RBC/FEDER + spend split remun/actions/fonct) "
    "and EUR amount of announced international network cut; L5 grant lines if public,"
    "2024 total 46.166m strong; 2026 blog confirms cuts (33to21 offices) without euro amount; "
    "dual triple with AWEX 76.8m and FIT FOI needs comparable years,6,"
    "Region de Bruxelles-Capitale / hub.brussels service openbaarheid,,"
    "Chaussee de Charleroi 110 1060 Saint-Gilles,"
    "docs/doge/foi/drafts/gap_hub_brussels_budget_2025_26.md,ready,2026-07-29,,,,,"
    "cmt_hub_brussels_budget_2024,lb_hub_brussels_46_2m|lb_export_agencies_triple_awex_fit_hub,"
    f"{now},{now},tick254 draft ready human send; 2024 filled\n"
)
with open(foi_path, "a", encoding="utf-8", newline="") as f:
    f.write(foi)
print("foi ok")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_245,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "hub.brussels budget; other FOI-adjacent).,,2026-07-29T13:30:00Z,,"
    "Spawned tick253 after AWEX 76.8m dual FIT; rq_116 SWA deferred"
)
new = (
    "rq_245,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "hub.brussels budget; other FOI-adjacent).,gap_hub_brussels_budget_2025_26,"
    "2026-07-29T13:30:00Z,2026-07-29T14:00:00Z,"
    "tick254: hub.brussels 46.166m 2024 dual AWEX; remun 31.875m; FOI 2025-26; spawn rq_246"
)
if old not in rq:
    raise SystemExit("rq_245 row not found")
rq = rq.replace(old, new)
if "rq_246," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_246,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
        "other FOI-adjacent after hub.brussels).,,2026-07-29T14:00:00Z,,"
        "Spawned tick254 after hub.brussels 46.2m; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
ls_path = root / "docs/doge/data/loop_state.csv"
ls_path.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_246; rq_116 SWA deferred. FOI ready human send. "
    "tick254 hub.brussels 46.2m dual AWEX/FIT.\n",
    encoding="utf-8",
)
print("loop_state ok")
print("DONE tick", tick)
