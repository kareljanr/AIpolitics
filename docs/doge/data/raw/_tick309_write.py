# tick 309 — rq_301 Rekenhof federal consultancy 2.5bn 2020-22
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
utc = "2026-07-30T17:15:00Z"
unit = "rq_301"

src_line = (
    "src_ccrek_consultancy_2025,"
    "Rekenhof Inzet van consultancy door de federale overheid Oct 2025,"
    "docs/doge/data/raw/ccrek_consultancy_2025.pdf; "
    "https://www.ccrek.be/sites/default/files/Docs/2025_39_InzetConsultancyFederaleOverheid.pdf,"
    "Rekenhof / Cour des comptes,2026-07-30,court_audit,"
    "137 orgs: 2.5247bn incl VAT 2020-22; IT 2.032bn (81pct) non-IT 0.492bn; "
    "IT IH 576.9m AO 1455.4m; top NMBS 465 Infrabel 319 Financien 185; tick309\n"
)
with (ROOT / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_line)

ent_path = ROOT / "entities.csv"
ent = ent_path.read_text(encoding="utf-8")
if "fed_consultancy_stack," not in ent:
    ent_path.write_text(
        ent.rstrip("\n")
        + "\n"
        + "fed_consultancy_stack,Federale consultancy inzet stack,"
        "Recours federal a la consultance,"
        "Federal consulting and operational support spend stack,"
        "programme,sec_federal,bi,,,,"
        "CoA 2.52bn 2020-22 class ~0.84bn/yr; IT dominant 81pct; no central inventory; tick309\n",
        encoding="utf-8",
    )

bud_rows = [
    "bud_fed_consultancy_total_2020_22,fed_consultancy_stack,2022,2524700000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "CoA survey 137 orgs: total 2.5247bn incl VAT over 2020-2022 (3y cumulative)",
    "bud_fed_consultancy_annual_class,fed_consultancy_stack,2021,841566667,,,estimate,src_ccrek_consultancy_2025,medium,"
    "Derived annual class 2.5247bn/3 ~841.6m/yr average 2020-22; not year-specific outturn",
    "bud_fed_consultancy_it_2020_22,fed_consultancy_stack,2022,2032300000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "IT 2.0323bn of which IH 576.9m + AO/OO 1455.4m",
    "bud_fed_consultancy_nonit_2020_22,fed_consultancy_stack,2022,492400000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "Non-IT 492.4m of which IH 42.2m + AO/OO 450.1m",
    "bud_fed_consultancy_it_ih_2020_22,fed_consultancy_stack,2022,576900000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "IT in-house Smals/Egov-class detachments 576.9m 2020-22",
    "bud_fed_consultancy_it_external_2020_22,fed_consultancy_stack,2022,1455400000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "IT external contracts/public procurement 1.4554bn 2020-22",
    "bud_fed_consultancy_nmbs_2020_22,nmbs,2022,465100000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "NMBS top buyer 465.1m (IH 104.2 + AO 360.9) = 9pct of NMBS purchase budget",
    "bud_fed_consultancy_infrabel_2020_22,nmbs,2022,318500000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "Infrabel 318.5m (IH 40 + AO 278.5) = 12pct purchase budget; entity under rail dual",
    "bud_fed_consultancy_finances_2020_22,fod_finance,2022,185300000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "FPS Finance 185.3m (IH 32.8 + AO 152.5) = 22pct purchase budget",
    "bud_fed_consultancy_bosa_2020_22,sec_federal,2022,134200000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "FPS BOSA 134.2m (IH 30.8 + AO 103.4) = 45pct purchase budget",
    "bud_fed_consultancy_niras_2020_22,niras,2022,129100000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "NIRAS 129.1m (IH 25.7 + AO 103.4) = 16pct purchase budget",
    "bud_fed_consultancy_smals_buy_2020_22,smals,2022,126100000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "Smals as buyer 126.1m (79pct of its purchase budget) mainly external IT re-sold",
    "bud_fed_consultancy_riziv_2020_22,riziv,2022,115500000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "RIZIV 115.5m (IH 27.7 + AO 87.9) = 48pct purchase budget",
    "bud_fed_cabinets_consultancy_2020_22,sec_federal,2022,6900000,,,estimate,src_ccrek_consultancy_2025,strong,"
    "Beleidsorganen cabinets: 6.9m over 3y; 5.9m from one Energy minister cabinets alone",
]
with (ROOT / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for r in bud_rows:
        f.write(r + "\n")

cmt_rows = [
    (
        "cmt_fed_consultancy_2020_22,Federal consultancy spend CoA survey 2020-2022 2.52bn,"
        "fed_consultancy_stack,Private consultants Smals Egov federal orgs,"
        "No single statute; CoA audit perimeter advisory+ops support incl staff provision,"
        "2020-01-01,2020,2022,2524700000,"
        '"{""total_incl_vat_m"":2524.7,""it_m"":2032.3,""nonit_m"":492.4,'
        '""it_ih_m"":576.9,""it_ao_m"":1455.4,""nonit_ih_m"":42.2,""nonit_ao_m"":450.1,'
        '""annual_class_m"":841.6,""orgs"":137,""confidence"":""declarative survey quality limited"",'
        '""top_m"":{""nmbs"":465.1,""infrabel"":318.5,""finances"":185.3,""bosa"":134.2,'
        '""niras"":129.1,""smals"":126.1,""riziv"":115.5},'
        '""cabinets_m"":6.9,""smals_ext_share_omzet_2014"":0.178,""smals_ext_share_omzet_2024"":0.36,'
        '""note"":""No central inventory; dual Smals omzet ~579m already mapped""}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "Map federal external advice and ops support opacity,"
        "Central inventory + strategy; insource IT core; FOI post-2022 annual series,"
        "src_ccrek_consultancy_2025,strong,Federal>procurement>consultancy,tick309"
    ),
    (
        "cmt_fed_consultancy_it_path,Federal IT consultancy dominance 81pct of 2.52bn,"
        "fed_consultancy_stack,IT consultants Smals broker rail health finance,"
        "Smals frameworks + direct awards + in-house detachments,2020-01-01,2020,2022,2032300000,"
        '"{""it_share_pct"":80.5,""it_ih_m"":576.9,""it_external_m"":1455.4,'
        '""rail_share_it_class"":0.36,""central_admin_it_class"":0.30,""oisz_it_class"":0.25,'
        '""smals_fte_2019"":1395,""smals_fte_2024"":2072}",'
        "0,active,docs/doge/data/raw/ccrek_consultancy_2025.pdf,"
        "IT capacity via consultants vs permanent staff,"
        "Rebuild internal IT; open Smals broker price benchmarks,"
        "src_ccrek_consultancy_2025,strong,Federal>IT>consultancy,tick309 dual Smals"
    ),
]
with (ROOT / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    for r in cmt_rows:
        f.write(r + "\n")

lb_rows = [
    (
        "lb_fed_consultancy_2_5bn,Federal consultancy ~2.52bn 2020-22 (~0.84bn/yr),federal,ops,"
        "Federal>procurement>consultancy,841566667,2524700000,"
        "Strong CoA: 2.5247bn incl VAT 137 orgs 2020-22; IT 81pct; no central inventory; survey medium quality,"
        "strong,src_ccrek_consultancy_2025,Taxpayers federal orgs,External advice and ops support,"
        "Opacity + no strategy + IT dependency; high waste purity on mechanism,"
        "8,8.5,5,7.9,Central inventory; cut non-core; insource IT; open annual series,"
        "seed,,tick309 material waste candidate"
    ),
    (
        "lb_fed_consultancy_it_2_0bn,Federal IT consultancy 2.03bn of 2.52bn 2020-22,federal,ops,"
        "Federal>IT>consultancy,677433333,2032300000,"
        "Strong CoA: IT 2.032bn (IH 577m + external 1455m); Smals external share 18->36pct omzet 2014-24,"
        "strong,src_ccrek_consultancy_2025,Federal IT users,IT capacity gap fill,"
        "Structural IT skill shortage + broker dependence,"
        "7,8.5,5,7.4,Internal IT pool; cap broker; dual Smals,"
        "seed,,tick309"
    ),
    (
        "lb_nmbs_consultancy_465m,NMBS consultancy 465m 2020-22 top buyer,federal,ops,"
        "Federal>NMBS>consultancy,155033333,465100000,"
        "Strong CoA: NMBS 465.1m (9pct purchase budget); dual Infrabel 318.5m,"
        "strong,src_ccrek_consultancy_2025,Rail users taxpayers,Rail digital/ops support,"
        "Largest single buyer; dual rail stack,"
        "6,7.5,4,6.5,Open L5 consultants; dual Infrabel,"
        "seed,,tick309"
    ),
    (
        "lb_cabinets_consultancy_6_9m,Federal cabinets consultancy 6.9m 2020-22,federal,ops,"
        "Federal>cabinets>consultancy,2300000,6900000,"
        "Strong CoA: 6.9m over 3y; 5.9m (85pct) from one Energy minister cabinets alone,"
        "strong,src_ccrek_consultancy_2025,Taxpayers,Ministerial cabinet external advice,"
        "Concentration opacity; dual gap_fed_cabinets_comms,"
        "7,4.0,3,5.5,Charge to cabinet BA only; open register,"
        "seed,,tick309 dual cabinets FOI"
    ),
]
with (ROOT / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for r in lb_rows:
        f.write(r + "\n")

foi_line = (
    "gap_fed_consultancy_annual_post2022,Federal>procurement>consultancy>annual_series,"
    "fed_consultancy_stack,"
    "Official annual series 2023-2026 same CoA perimeter (IT/non-IT; IH vs AO; by org top20); "
    "BOSA inventory with IT included; activate art 3/3 openbaarheid KB,"
    "CoA filled 2020-22 strong but declarative; post-2022 and machine-readable inventory missing; ~0.8bn/yr class,"
    "8,FOD BOSA / Prime Minister / IBZ FOI,,"
    "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_fed_consultancy_annual_post2022.md,ready,2026-07-30,,,,,,"
    "cmt_fed_consultancy_2020_22,lb_fed_consultancy_2_5bn,"
    "2026-07-30T17:15:00Z,2026-07-30T17:15:00Z,tick309 draft ready human send\n"
)
with (ROOT / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_line)

rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_301,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T16:45:00Z,,Spawned tick308; do after progress@310 if concurrent"
)
new = (
    "rq_301,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills after or with progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,"
    "gap_fed_consultancy_annual_post2022,2026-07-30T16:45:00Z,2026-07-30T17:15:00Z,"
    "tick309: CoA consultancy 2.52bn 2020-22 IT 2.03bn; top NMBS 465m; FOI annual post-2022; spawn rq_302; progress@310 next"
)
if old not in text:
    raise SystemExit("rq_301 not found")
text = text.replace(old, new)
text = text.rstrip("\n") + "\n"
text += (
    "rq_302,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills after progress@310 (AGMJ if extractable; other FOI-adjacent). Prefer before idle.,,"
    "2026-07-30T17:15:00Z,,Spawned tick309 after CoA consultancy; do after rq_300 progress@310\n"
)
rq_path.write_text(text, encoding="utf-8")

(ROOT / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},{unit},309,no,"
    "Scheduler 60s. NEXT MANDATORY rq_300 progress@310; then rq_302. "
    "rq_116 SWA deferred. tick309 CoA consultancy 2.52bn 2020-22.\n",
    encoding="utf-8",
)
print("OK")
