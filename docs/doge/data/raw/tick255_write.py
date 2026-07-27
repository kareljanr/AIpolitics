# tick 255 — rq_246 dual tourism Toerisme Vlaanderen + Visit.brussels; AGMJ FTE
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
now = "2026-07-29T14:30:00Z"
tick = 255
unit = "rq_246"

# --- sources ---
src = root / "docs/doge/data/sources.csv"
with open(src, "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_toerisme_bbt_presentation,Toerisme Vlaanderen BBT presentation werkings+investerings toelage + lonen,"
        "docs/doge/data/raw/vl_toerisme_vlaanderen_bbt.pdf,Vlaams Parlement docs.vlaamsparlement.be pfile 2086302,"
        "2026-07-29,budget,"
        "Werkingstoelage 39.357m + investeringstoelage 32.333m; lonen 19.967m werking 5.026m; "
        "EventFlanders 1m+7.5m; saldo desaffect 80.208m; post-regeerakkoord path; year class 2025-26; tick255\n"
    )
    f.write(
        "src_vl_toerisme_bbt_bo2024,Beleids- en begrotingstoelichting Toerisme BO2024 programme SQ totals,"
        "docs/doge/data/raw/vl_toerisme_bbt_begroting_2024.pdf,Vlaams Parlement 13-R (2023-2024) Nr.1,"
        "2026-07-29,budget,"
        "Programme SQ Toerisme BO2024 VAK 66.466m VEK 74.816m (excl apparaat); EventFlanders werk 1.0m inv VAK 3.5m VEK 4.357m; tick255\n"
    )
    f.write(
        "src_ccrek_bru_credits_prov_2025_visit,Cour des comptes BCR credits provisoires 2025 Visit.brussels prog 302 14.9m,"
        "https://www.ccrek.be/sites/default/files/Docs/2025_02_CreditsProvisoires.pdf,Cour des comptes / BCR,"
        "2026-07-29,audit,"
        "VISIT.39.302.08 programme 302 Soutenir le tourisme BI2024 initial 14.9m eng; partial agency not full package; dual Toerisme VL; tick255\n"
    )
    f.write(
        "src_fwb_expgen_agmj_etp_2025,FWB ExpGen BI2026 effectifs AGMJ ETP 30jun2025,"
        "docs/doge/data/raw/fwb_expgen_2026_extract.txt,MFWB DGBF ExpGen BI2026,"
        "2026-07-29,budget,"
        "AGMJ 801 ETP courant 30/06/2025 (cat1 102 +2+ 535 +2 149 +3 15); wage bill residual FOI; dual VL AJH; tick255\n"
    )
print("sources ok")

# --- entities ---
ent_path = root / "docs/doge/data/entities.csv"
ent = ent_path.read_text(encoding="utf-8")
lines = [L for L in ent.splitlines() if L.strip()]
# update / add
new_lines = []
has_tv = False
has_vb = False
for L in lines:
    if L.startswith("toerisme_vlaanderen,"):
        has_tv = True
        L = (
            "toerisme_vlaanderen,Toerisme Vlaanderen,Tourisme Flandre,VisitFlanders / Tourism Flanders,"
            "agency,vlaanderen_gov,nl,https://www.toerismevlaanderen.be,,,"
            "Werkingstoelage 39.357m + invest 32.333m class; BO2024 SQ VEK 74.816m; dual visit.brussels; tick255"
        )
    if L.startswith("visit_brussels,"):
        has_vb = True
        L = (
            "visit_brussels,visit.brussels ASBL,visit.brussels ASBL,Brussels tourism promotion agency,"
            "asbl,brussels_gov,bi,https://www.visit.brussels,,,"
            "Prog 302 tourism 14.9m BI2024 Cour; full package residual FOI; dual Toerisme VL; tick255"
        )
    new_lines.append(L)
if not has_tv:
    new_lines.append(
        "toerisme_vlaanderen,Toerisme Vlaanderen,Tourisme Flandre,VisitFlanders / Tourism Flanders,"
        "agency,vlaanderen_gov,nl,https://www.toerismevlaanderen.be,,,"
        "Werkingstoelage 39.357m + invest 32.333m class; BO2024 SQ VEK 74.816m; dual visit.brussels; tick255"
    )
if not has_vb:
    new_lines.append(
        "visit_brussels,visit.brussels ASBL,visit.brussels ASBL,Brussels tourism promotion agency,"
        "asbl,brussels_gov,bi,https://www.visit.brussels,,,"
        "Prog 302 tourism 14.9m BI2024 Cour; full package residual FOI; dual Toerisme VL; tick255"
    )
# note AGMJ on fwb if present
out_ent = []
for L in new_lines:
    if L.startswith("fwb_maisons_justice,") or "maisons_justice" in L[:40]:
        if "tick255" not in L and "AGMJ" not in L:
            L = L.rstrip() + "; AGMJ 801 ETP 30jun2025 ExpGen; tick255"
    out_ent.append(L)
with open(ent_path, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(out_ent) + "\n")
print("entities", len(out_ent))

# --- budgets ---
bud = root / "docs/doge/data/budgets.csv"
bud_rows = [
    "bud_tv_werkingstoelage_class,toerisme_vlaanderen,2025,39357000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,BBT presentation werkings toelage 39.357m; year class 2025-26 post-regeerakkoord EventFlanders 7.5m path",
    "bud_tv_investeringstoelage_class,toerisme_vlaanderen,2025,32333000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,BBT presentation investerings toelage 32.333m; year class 2025-26",
    "bud_tv_toelage_package_class,toerisme_vlaanderen,2025,71690000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,Sum werkings+invest toelage 71.690m; dual Visit.brussels; not full TCO with own receipts",
    "bud_tv_lonen_class,toerisme_vlaanderen,2025,19967000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,Lonen 19.967m presentation class year",
    "bud_tv_werking_class,toerisme_vlaanderen,2025,5026000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,Werking 5.026m presentation class year",
    "bud_tv_eventflanders_ops_class,toerisme_vlaanderen,2025,1000000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,EventFlanders loon+werking 1.0m",
    "bud_tv_eventflanders_topevents_class,toerisme_vlaanderen,2025,7500000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,Topevenementen 7.5m recurrent regeerakkoord path; legislatuur min 37.5m",
    "bud_tv_saldo_desaffect_class,toerisme_vlaanderen,2025,80208000,,,budgeted,src_vl_toerisme_bbt_presentation,medium,Saldo 80.208m desaffect to algemene middelen; no daily ops impact claimed",
    "bud_tv_sq_vak_bo2024,toerisme_vlaanderen,2024,66466000,,,budgeted,src_vl_toerisme_bbt_bo2024,strong,Programme SQ Toerisme BO2024 VAK 66.466m excl apparaat",
    "bud_tv_sq_vek_bo2024,toerisme_vlaanderen,2024,74816000,,,budgeted,src_vl_toerisme_bbt_bo2024,strong,Programme SQ Toerisme BO2024 VEK 74.816m excl apparaat",
    "bud_tv_eventflanders_vak_bo2024,toerisme_vlaanderen,2024,3500000,,,budgeted,src_vl_toerisme_bbt_bo2024,strong,EventFlanders invest VAK 3.5m BO2024 (+0.5m VAK-ruiter possible)",
    "bud_tv_eventflanders_vek_bo2024,toerisme_vlaanderen,2024,4357000,,,budgeted,src_vl_toerisme_bbt_bo2024,strong,EventFlanders invest VEK 4.357m BO2024; werk 1.0m separate",
    "bud_visit_brussels_prog302_2024,visit_brussels,2024,14900000,,,budgeted,src_ccrek_bru_credits_prov_2025_visit,strong,Cour: VISIT.39.302.08 Soutenir le tourisme BI2024 initial 14.9m; partial not full agency package",
]
with open(bud, "a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")
print("budgets", len(bud_rows))

# --- commitments ---
cmt = root / "docs/doge/data/commitments.csv"
cash_tv = (
    '{"werkingstoelage_class": 39357000, "investeringstoelage_class": 32333000, '
    '"package_toelage_class": 71690000, "lonen_class": 19967000, "werking_class": 5026000, '
    '"eventflanders_ops": 1000000, "eventflanders_topevents": 7500000, '
    '"saldo_desaffect": 80208000, "bo2024_sq_vak": 66466000, "bo2024_sq_vek": 74816000, '
    '"note": "Presentation year class 2025-26; BO2024 SQ strong; dual visit.brussels 14.9m prog partial"}'
).replace('"', '""')
cash_vb = (
    '{"prog302_2024": 14900000, "note": "Cour BI2024 partial programme; full agency 2025-26 FOI; '
    'press cut 5.7m secondary not used as primary"}'
).replace('"', '""')
with open(cmt, "a", encoding="utf-8", newline="") as f:
    f.write(
        "cmt_toerisme_vlaanderen_package,Toerisme Vlaanderen dual tourism package vs visit.brussels,"
        "toerisme_vlaanderen,Flemish tourism sector EventFlanders partners,BBT + agency presentation,"
        f"2024-01-01,2024,2029,71690000,\"{cash_tv}\",0,active,"
        "docs/doge/data/raw/vl_toerisme_vlaanderen_bbt.pdf,"
        "Destination promotion social tourism EventFlanders,"
        "Confirm presentation year BBT stamp; dual unit-cost vs Visit.brussels full package; WBT WAL residual,"
        "src_vl_toerisme_bbt_presentation,medium,Vlaanderen>Toerisme>Toerisme_Vlaanderen,"
        "tick255 dual tourism; BO2024 SQ also strong\n"
    )
    f.write(
        "cmt_visit_brussels_prog302_2024,visit.brussels tourism programme 302 dual Toerisme VL,"
        "visit_brussels,Brussels leisure and MICE tourism sector,Cour credits provisoires footnote BI2024,"
        f"2024-01-01,2024,2026,14900000,\"{cash_vb}\",0,active,"
        "https://www.ccrek.be/sites/default/files/Docs/2025_02_CreditsProvisoires.pdf,"
        "Regional tourism promotion,"
        "FOI full ASBL budget 2025-26 after announced cuts; dual TV,"
        "src_ccrek_bru_credits_prov_2025_visit,strong,Bruxelles>Tourisme>visit.brussels,"
        "tick255 dual tourism partial\n"
    )
    f.write(
        "cmt_agmj_etp_2025,FWB AGMJ Maisons de justice headcount 801 ETP dual VL AJH,"
        "fwb_maisons_justice,AGMJ staff justice assistants,ExpGen effectifs 30/06/2025,"
        "2025-06-30,2025,2026,0,"
        "\"{\"\"etp_total\"\": 801, \"\"cat1\"\": 102, \"\"cat2plus\"\": 535, \"\"cat2\"\": 149, \"\"cat3\"\": 15, "
        "\"\"note\"\": \"Wage bill residual FOI; dual VL AJH lonen 164.9m context not unit-cost\"}\","
        "0,active,docs/doge/data/raw/fwb_expgen_2026_extract.txt,"
        "Community justice houses staffing,"
        "FOI full wage bill multi-year still gap_fwb_mdj_personnel_total,"
        "src_fwb_expgen_agmj_etp_2025,strong,FWB>Maisons_de_Justice>AGMJ_ETP,"
        "tick255 FTE fill wage residual\n"
    )
print("cmt ok")

# --- leaderboard ---
lb = root / "docs/doge/data/leaderboard.csv"
lb_rows = [
    "lb_tv_toelage_71_7m,Toerisme Vlaanderen toelage package ~71.7m dual Visit,Flanders,ops,Vlaanderen>Toerisme>Toerisme_Vlaanderen,71690000,71690000,Medium presentation: werkings 39.357 + invest 32.333; BO2024 SQ VEK 74.816m strong cross-check class; dual visit.brussels,medium,src_vl_toerisme_bbt_presentation,Flemish tourism sector EventFlanders,Destination promotion + social tourism,Core dual tourism agency; not pure waste,3,7.0,5,5.65,Confirm year stamp; publish dual Visit matrix,seed,,tick255",
    "lb_tv_sq_vek_74_8m,Toerisme programme SQ VEK 74.8m BO2024,Flanders,ops,Vlaanderen>Toerisme>SQ_VEK,74816000,74816000,Strong BBT BO2024: SQ VAK 66.466m VEK 74.816m excl apparaat,strong,src_vl_toerisme_bbt_bo2024,Tourism actors Flanders,Policy tourism programme credits,Programme envelope dual Visit,3,7.0,4,5.75,Cross-check BA2025/BO2026 when public,seed,,tick255",
    "lb_tourism_dual_tv_visit,Tourism dual Toerisme VL ~72-75m vs Visit prog 14.9m,Belgium,ops,BE>Tourism>dual_TV_Visit,0,0,Strong dual: VL SQ VEK 74.8m 2024 + Visit prog302 14.9m partial 2024; full Visit package FOI; not additive scopes differ,strong,src_vl_toerisme_bbt_bo2024,Tourism BE regional,Regional dual tourism promotion,Institutional dual tourism stack,4,7.5,5,5.85,FOI Visit full package; WBT Wallonia residual,seed,,tick255 dual not additive",
    "lb_visit_brussels_prog302_14_9m,visit.brussels prog 302 tourism 14.9m 2024,Brussels,ops,Bruxelles>Tourisme>visit.brussels_prog302,14900000,14900000,Strong Cour footnote BI2024 VISIT.39.302.08 14.9m; full ASBL residual FOI; press cut path secondary,strong,src_ccrek_bru_credits_prov_2025_visit,Brussels tourism businesses visitors,Tourism promotion programme,Partial agency line dual TV,3,5.5,5,4.95,FOI full budget 2025-26 after cuts,seed,,tick255",
    "lb_agmj_etp_801,AGMJ Maisons de justice 801 ETP dual VL AJH,FWB,ops,FWB>Maisons_de_Justice>AGMJ_ETP,0,0,Strong ExpGen: 801 ETP 30jun2025; wage bill still FOI; dual VL AJH lonen 164.9m context,strong,src_fwb_expgen_agmj_etp_2025,Justiciables FR community,Community justice houses staff,FTE public wage residual dual opacity,4,5.0,4,4.85,FOI wage bill still gap_fwb_mdj_personnel_total,seed,,tick255",
]
with open(lb, "a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")
print("lb", len(lb_rows))

# --- foi_queue ---
foi = root / "docs/doge/data/foi_queue.csv"
with open(foi, "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_visit_brussels_budget_full,Bruxelles>visit.brussels>budget_full,visit_brussels,"
        "visit.brussels full ASBL budget recettes/depenses 2024-2026 (beyond Cour prog 302 14.9m BI2024) "
        "and EUR amount of 2026 announced cut; L5 grant lines if public,"
        "Prog 302 14.9m strong partial; dual Toerisme VL SQ VEK 74.8m needs comparable full agency package; "
        "press cites ~22m/5.7m cut secondary only,6,"
        "Region de Bruxelles-Capitale / visit.brussels service openbaarheid,,"
        "visit.brussels Brussels,"
        "docs/doge/foi/drafts/gap_visit_brussels_budget_full.md,ready,2026-07-29,,,,,"
        "cmt_visit_brussels_prog302_2024,lb_visit_brussels_prog302_14_9m|lb_tourism_dual_tv_visit,"
        f"{now},{now},tick255 draft ready human send; prog302 filled\n"
    )
    f.write(
        "gap_tv_presentation_year_confirm,Vlaanderen>Toerisme>BBT_year_stamp,toerisme_vlaanderen,"
        "Confirm budget year stamp for Toerisme Vlaanderen presentation (werking 39.357 + invest 32.333) "
        "and latest BO2025/BO2026 SQ VAK/VEK if published beyond BO2024 74.816m VEK,"
        "Presentation strong figures but year class 2025-26; dual map needs exact year,4,"
        "Vlaamse overheid Team Openbaarheid / Toerisme Vlaanderen,openbaarheid@vlaanderen.be,"
        "Havenlaan 88 bus 20 1000 Brussel,"
        "docs/doge/foi/drafts/gap_tv_presentation_year_confirm.md,ready,2026-07-29,,,,,"
        "cmt_toerisme_vlaanderen_package,lb_tv_toelage_71_7m,"
        f"{now},{now},tick255 optional year confirm; BO2024 already strong\n"
    )
print("foi ok")

# narrow AGMJ personnel FOI note
foi_text = foi.read_text(encoding="utf-8")
old_agmj = None
for line in foi_text.splitlines():
    if line.startswith("gap_fwb_mdj_personnel_total,"):
        old_agmj = line
        break
if old_agmj and "tick255" not in old_agmj:
    new_agmj = old_agmj
    # update notes field at end
    if new_agmj.endswith("\n"):
        new_agmj = new_agmj[:-1]
    # replace last notes portion carefully - append to notes
    parts = new_agmj.rsplit(",", 1)
    if len(parts) == 2:
        new_agmj = parts[0] + "," + parts[1] + " | tick255: AGMJ 801 ETP public wage residual"
    foi_text = foi_text.replace(old_agmj, new_agmj)
    foi.write_text(foi_text, encoding="utf-8")
    print("foi agmj updated")

# --- research_queue ---
rq_path = root / "docs/doge/data/research_queue.csv"
rq = rq_path.read_text(encoding="utf-8")
old = (
    "rq_246,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "other FOI-adjacent after hub.brussels).,,2026-07-29T14:00:00Z,,"
    "Spawned tick254 after hub.brussels 46.2m; rq_116 SWA deferred"
)
new = (
    "rq_246,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
    "other FOI-adjacent after hub.brussels).,gap_visit_brussels_budget_full|gap_tv_presentation_year_confirm,"
    "2026-07-29T14:00:00Z,2026-07-29T14:30:00Z,"
    "tick255: Toerisme VL SQ VEK 74.8m + toelage class 71.7m dual Visit prog302 14.9m; AGMJ 801 ETP; spawn rq_247"
)
if old not in rq:
    raise SystemExit("rq_246 not found")
rq = rq.replace(old, new)
if "rq_247," not in rq:
    rq = (
        rq.rstrip("\n")
        + "\nrq_247,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (Mons ASBL L5 if public; AGMJ wage if public; FIT public PDF if appears; "
        "WBT Wallonia tourism dual residual; other FOI-adjacent).,,2026-07-29T14:30:00Z,,"
        "Spawned tick255 after dual tourism TV+Visit; rq_116 SWA deferred\n"
    )
rq_path.write_text(rq, encoding="utf-8")
print("rq ok")

# --- loop_state ---
ls = root / "docs/doge/data/loop_state.csv"
ls.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{now},{unit},{tick},no,"
    "Scheduler 60s. Next prio5 rq_247; rq_116 SWA deferred. FOI ready human send. "
    "tick255 dual tourism TV 74.8m Visit 14.9m AGMJ 801 ETP.\n",
    encoding="utf-8",
)
print("DONE", tick)
