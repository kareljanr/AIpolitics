# tick375: Groeipakket + Geïntegreerd gezinsbeleid BU2025 L5
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge/data/raw -> repo? 
# raw is docs/doge/data/raw -> parents[0]=raw, [1]=data, [2]=doge, [3]=docs — wrong
# Better: cwd is repo when we run from repo
import os
REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

# --- entities ---
ent_rows = [
    "vl_groeipakket,ISE Groeipakket Vlaanderen,Pack croissance Flandre,Flanders Growth Package family benefits ISE dual WAL/BRU,programme,opgroeien,nl,https://www.groeipakket.be,openbaarheid@vlaanderen.be,,ISE VEK BU 4906.672m 2025; GEF2QX 4797.1 GEF2QY 109.57; dual AF; tick375",
    "vl_gezinsbeleid,ISE Geintegreerd gezinsbeleid Vlaanderen,Politique familiale integree Flandre,Flanders integrated family policy KO+PGJO+adoptie,programme,opgroeien,nl,https://www.opgroeien.be,openbaarheid@vlaanderen.be,,ISE VEK BU 1369.467m 2025 GEF2UX; parent fees 233.5m; tick375",
    "fons_vl,Fons publieke uitbetalingsactor Groeipakket,Fons acteur public Pack croissance,Flanders public Groeipakket payment actor under VUTG,agency,vutg,nl,https://www.groeipakket.be,,,Public channel Fons; VUTG GP benefits path 1147.7m 2025; tick375",
]
with (DATA / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    for r in ent_rows:
        f.write(r + "\n")
print("entities +", len(ent_rows))

# --- sources ---
src_row = (
    "src_vl_bbt_wvg_bu2025_gp_ko,"
    "BBT WVG BU2025 Groeipakket + Geintegreerd gezinsbeleid L5,"
    "https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "Vlaamse Regering / Opgroeien / VUTG / minister Gennez,"
    "2026-08-01,primary_budget,"
    '"BBT WVG execution 2025; ISE Groeipakket p89-95 ISE Gezinsbeleid p96-101; keuro tables; dual WAL AF prior"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_row + "\n")
print("sources +1")

# --- budgets ---
budgets = [
    ("bud_vl_groeipakket_ise_vek_ba_2025", "vl_groeipakket", 2025, 4906129000, "budgeted", "ISE Groeipakket BA2025 VEK 4906.129m"),
    ("bud_vl_groeipakket_ise_vek_bu_2025", "vl_groeipakket", 2025, 4906672000, "outturn", "ISE Groeipakket BA-JR=BU VEK 4906.672m"),
    ("bud_vl_groeipakket_ise_vak_ba_2025", "vl_groeipakket", 2025, 4906156000, "budgeted", "ISE Groeipakket BA2025 VAK 4906.156m"),
    ("bud_vl_groeipakket_ise_vak_bu_2025", "vl_groeipakket", 2025, 4906699000, "outturn", "ISE Groeipakket BA-JR=BU VAK 4906.699m"),
    ("bud_vl_gef2qx_opgroeien_gp_2025", "opgroeien", 2025, 4797102000, "outturn", "GB0-1GEF2QX-IS policy credits Opgroeien Groeipakket VAK=VEK BA=BU 4797.102m"),
    ("bud_vl_gef2qy_vutg_2025_vek_bu", "vutg", 2025, 109570000, "outturn", "GB0-1GEF2QY-IS VUTG toelage VEK BU 109.570m (VAK BU 109.597m)"),
    ("bud_vl_gef2qy_vutg_2025_vak_bu", "vutg", 2025, 109597000, "outturn", "GB0-1GEF2QY-IS VUTG toelage VAK BU 109.597m"),
    ("bud_vl_gef2qy_vutg_2025_vek_ba", "vutg", 2025, 109027000, "budgeted", "GB0-1GEF2QY-IS VUTG VEK BA 109.027m"),
    ("bud_opgroeien_gp_exp_2025", "opgroeien", 2025, 4859865000, "outturn", "Opgroeien Groeipakket beleidskrediet exp AGEF2QB+QY+QW 4859.865m (+32.103m vs credit)"),
    ("bud_opgroeien_gp_recoveries_2025", "opgroeien", 2025, 32972000, "outturn", "GDF-BGEFAQB-OW recoveries private UA 32.972m (raming 30.660m)"),
    ("bud_vutg_admin_lonen_2025", "vutg", 2025, 38047000, "outturn", "VUTG lonen en werking VEK BU 38.047m"),
    ("bud_vutg_admin_invest_2025", "vutg", 2025, 4342000, "outturn", "VUTG investeringen GPA VEK BU 4.342m"),
    ("bud_vutg_private_ua_subsidy_2025", "vutg", 2025, 67082000, "outturn", "Werkingssubsidie 4 private uitbetalingsactoren 67.082m VAK=VEK full"),
    ("bud_vutg_algemene_werking_2025", "vutg", 2025, 109471000, "outturn", "VUTG algemene werking total VEK BU 109.471m (lonen+invest+private UA)"),
    ("bud_vutg_gp_benefits_2025", "vutg", 2025, 1147696000, "outturn", "VUTG/Fons channel Groeipakket toelagen Gezinsbeleid VEK BU 1147.696m"),
    ("bud_vutg_toelage_opgroeien_gp_2025", "vutg", 2025, 1131694000, "outturn", "Toelage Opgroeien Regie to VUTG for GP 1131.694m"),
    ("bud_vutg_family_recoveries_2025", "vutg", 2025, 15998000, "outturn", "Terugvorderingen gezinnen Groeipakket 15.998m"),
    ("bud_vl_gezinsbeleid_ise_vek_ba_2025", "vl_gezinsbeleid", 2025, 1349455000, "budgeted", "ISE Geintegreerd gezinsbeleid BA2025 VEK 1349.455m"),
    ("bud_vl_gezinsbeleid_ise_vek_bu_2025", "vl_gezinsbeleid", 2025, 1369467000, "outturn", "ISE Geintegreerd gezinsbeleid BA-JR=BU VEK 1369.467m"),
    ("bud_vl_gezinsbeleid_ise_vak_ba_2025", "vl_gezinsbeleid", 2025, 1372560000, "budgeted", "ISE Geintegreerd gezinsbeleid BA2025 VAK 1372.560m"),
    ("bud_vl_gezinsbeleid_ise_vak_bu_2025", "vl_gezinsbeleid", 2025, 1392279000, "outturn", "ISE Geintegreerd gezinsbeleid BA-JR=BU VAK 1392.279m"),
    ("bud_vl_gef2ux_opgroeien_2025_vek_bu", "opgroeien", 2025, 1369467000, "outturn", "GB0-1GEF2UX-IS Opgroeien KO+PGJO+adoptie VEK BU 1369.467m"),
    ("bud_opgroeien_ko_parent_fees_2025", "opgroeien", 2025, 233463000, "outturn", "Parent financial contributions kinderopvang 233.463m (raming 249.360m)"),
    ("bud_opgroeien_ko_other_receipts_2025", "opgroeien", 2025, 11820000, "outturn", "Other own receipts maribel/fed/cities KO 11.820m (raming 14.702m)"),
    ("bud_opgroeien_agef2ua_lo_2025", "opgroeien", 2025, 100986000, "outturn", "GDF-AGEF2UA-LO personnel/ops 100.986m (-0.926m vs raming)"),
    ("bud_vl_gezinsbeleid_vek_surplus_2025", "vl_gezinsbeleid", 2025, 79200000, "outturn", "AGEF2UA-WT VEK surplus 79.2m under-exec expansion places (not spent)"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, eid, yr, amt, basis, notes in budgets:
        f.write(
            f'{bid},{eid},{yr},{amt},,,,{basis},src_vl_bbt_wvg_bu2025_gp_ko,strong,"{notes}"\n'
        )
print("budgets +", len(budgets))

# --- commitments ---
cmt1 = (
    "cmt_vl_groeipakket_l5_2025,Flanders Groeipakket ISE L5 2025 dual AF,vl_groeipakket,"
    "Families children Flanders via Fons+4 private UAs,Decreet Groeipakket / BBT WVG BU2025,"
    "2025-01-01,2025,2025,4906672000,"
    '"{""ise_vek_ba_m"":4906.129,""ise_vek_bu_m"":4906.672,""ise_vak_bu_m"":4906.699,'
    '""gef2qx_m"":4797.102,""gef2qy_vek_bu_m"":109.57,""opgroeien_exp_m"":4859.865,'
    '""recoveries_m"":32.972,""vutg_private_ua_m"":67.082,""vutg_admin_lonen_m"":38.047,'
    '""vutg_invest_m"":4.342,""vutg_gp_benefits_m"":1147.696,""vutg_toelage_opgroeien_m"":1131.694,'
    '""private_ua_names"":[""Kidslife"",""Infino"",""MyFamily"",""Parentia""],""public_ua"":""Fons"",'
    '""dual_wal_af_2026_m"":3013.486,""dual_bru_iriscare_m"":1081.4,'
    '""note"":""Strong BU2025; per-UA admin+benefit split residual FOI; prior awards~4.7bn class refined""}",'
    "0,active,https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "Universal family benefits Growth Package Flanders,"
    "Publish per-UA EUR; dual unit-cost WAL/BRU; BO2026,"
    "src_vl_bbt_wvg_bu2025_gp_ko,strong,Vlaanderen>Opgroeien>Groeipakket>L5_2025,"
    "tick375: ISE 4.907bn VUTG private UA 67.1m\n"
)
cmt2 = (
    "cmt_vl_gezinsbeleid_l5_2025,Flanders Geintegreerd gezinsbeleid KO+PGJO 2025,vl_gezinsbeleid,"
    "Childcare operators parents adoptive families Flanders,"
    "Decreet kinderopvang / preventieve gezinsondersteuning,"
    "2025-01-01,2025,2025,1369467000,"
    '"{""ise_vek_ba_m"":1349.455,""ise_vek_bu_m"":1369.467,""ise_vak_bu_m"":1392.279,'
    '""gef2ux_vek_bu_m"":1369.467,""parent_fees_m"":233.463,""parent_fees_raming_m"":249.36,'
    '""other_receipts_m"":11.82,""agef2ua_lo_m"":100.986,""vek_surplus_m"":79.2,'
    '""dual_one_2026_m"":760.837,'
    '""note"":""Strong BU2025 ISE; KO sector split residual; dual ONE FWB; BO2026 KO 1557.7m prior""}",'
    "0,active,https://themis.vlaanderen.be/files/689c2360-49fe-11f1-909c-bd967777a5f1/download,"
    "Childcare preventive family support adoption Flanders,"
    "Open KO operator L5; dual unit-cost ONE; BO2026,"
    "src_vl_bbt_wvg_bu2025_gp_ko,strong,Vlaanderen>Opgroeien>Gezinsbeleid>L5_2025,"
    "tick375: ISE 1.369bn parent fees 233m\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt1)
    f.write(cmt2)
print("commitments +2")

# --- leaderboard ---
lbs = [
    (
        "lb_vl_groeipakket_ise_4_91bn",
        "Flanders Groeipakket ISE ~4.907bn 2025",
        "Flanders",
        "transfer",
        "Vlaanderen>Opgroeien>ISE_Groeipakket",
        4906672000,
        4906129000,
        "Strong BBT BU2025: VEK BU 4906.672m BA 4906.129m; GEF2QX 4797.1 + GEF2QY 109.57; dual WAL/BRU AF",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Families children Flanders",
        "Universal family benefits Growth Package",
        "Core social mega not pure waste; dual multi-caisse; per-UA L5 residual",
        3,
        9.5,
        4,
        6.68,
        "Publish per-UA admin+benefits; dual unit-cost; BO2026 codes",
        "seed",
        "",
        "tick375; supersedes awards~4.7bn class with exact ISE",
    ),
    (
        "lb_gef2qx_gp_4_80bn",
        "Flanders GEF2QX Opgroeien Groeipakket policy 4.797bn",
        "Flanders",
        "transfer",
        "Vlaanderen>Opgroeien>GEF2QX",
        4797102000,
        4797102000,
        "Strong: VAK=VEK BA=BU 4797.102m policy credits; agency exp 4859.865m with recoveries",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Families via payment actors",
        "Policy financing path for benefits",
        "Core open-end entitlement",
        2,
        9.5,
        3,
        6.53,
        "Reconcile overspend 32m; open AGEF2QB vs QY split",
        "seed",
        "",
        "tick375",
    ),
    (
        "lb_vutg_private_ua_67m",
        "Flanders private Groeipakket UAs admin subsidy 67.1m",
        "Flanders",
        "ops",
        "Vlaanderen>Opgroeien>VUTG>private_UA",
        67082000,
        67082000,
        "Strong: 4 private UAs Kidslife Infino MyFamily Parentia werkingssubsidie 67.082m; per-UA FOI",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Private payment organisms",
        "Admin financing dual public Fons",
        "Dual WAL private CAF admin; L5 per UA residual; not benefits cash",
        5,
        5.5,
        4,
        5.03,
        "Publish per-UA EUR; unit cost vs Fons; dual WAL",
        "seed",
        "",
        "tick375",
    ),
    (
        "lb_vutg_gp_channel_1_15bn",
        "Flanders VUTG/Fons Groeipakket benefits channel 1.148bn",
        "Flanders",
        "transfer",
        "Vlaanderen>Opgroeien>VUTG>Fons_benefits",
        1147696000,
        1147696000,
        "Strong: VUTG toelagen Gezinsbeleid VEK 1147.696m public channel; residual private benefit path FOI",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Public-channel families Fons",
        "Public payment of family benefits",
        "Core entitlement public channel share ~23pct of ISE class",
        3,
        8.5,
        4,
        6.18,
        "Open private-channel benefit EUR matrix AGEF2QB",
        "seed",
        "",
        "tick375",
    ),
    (
        "lb_vl_gezinsbeleid_ise_1_37bn",
        "Flanders Geintegreerd gezinsbeleid ISE ~1.35-1.37bn",
        "Flanders",
        "ops",
        "Vlaanderen>Opgroeien>ISE_Gezinsbeleid",
        1369467000,
        1349455000,
        "Strong: VEK BA 1349.455 BU 1369.467; GEF2UX; KO+PGJO+adoptie; dual ONE 761m",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Children families childcare Flanders",
        "Integrated family policy childcare prevention adoption",
        "Core social; KO operator L5 residual; surplus 79m expansion lag",
        3,
        8.5,
        4,
        6.18,
        "Open KO provider top; dual unit-cost ONE; BO2026",
        "seed",
        "",
        "tick375",
    ),
    (
        "lb_ko_parent_fees_233m",
        "Flanders kinderopvang parent fees 233.5m 2025",
        "Flanders",
        "receipt",
        "Vlaanderen>Opgroeien>KO>ouderbijdragen",
        233463000,
        249360000,
        "Strong: realized 233.463m vs raming 249.360m; under-exec with expansion lag",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Parents using subsidized childcare",
        "User co-payment financing path",
        "Receipt not spend; pairs with under-exec places",
        2,
        7.5,
        3,
        5.18,
        "Reconcile fees vs place utilization; BO2026 kindkorting reform",
        "seed",
        "",
        "tick375",
    ),
    (
        "lb_gezinsbeleid_surplus_79m",
        "Flanders GEF2UX/AGEF2UA-WT VEK surplus 79.2m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Opgroeien>Gezinsbeleid>under_exec",
        79200000,
        79200000,
        "Strong: 79.2m VEK surplus gradual start new places + returned places not redeployed",
        "strong",
        "src_vl_bbt_wvg_bu2025_gp_ko",
        "Planned childcare expansion places",
        "Expansion lag under-execution",
        "Opacity if expansion cash not spent vs waitlists; not pure waste claim",
        6,
        5.5,
        4,
        5.38,
        "Publish multi-year place delivery vs budget; redeploy unused places",
        "seed",
        "",
        "tick375",
    ),
]
with (DATA / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for row in lbs:
        parts = [
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            str(row[5]),
            str(row[6]),
            f'"{row[7]}"',
            row[8],
            row[9],
            row[10],
            row[11],
            f'"{row[12]}"',
            str(row[13]),
            str(row[14]),
            str(row[15]),
            str(row[16]),
            f'"{row[17]}"',
            row[18],
            row[19],
            f'"{row[20]}"',
        ]
        f.write(",".join(parts) + "\n")
print("leaderboard +", len(lbs))

# --- research queue ---
rq_path = DATA / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_366,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T01:45:00Z,,Spawned tick374 after VAPH L5; rq_116 SWA deferred"
)
new = (
    "rq_366,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_vl_gp_gezinsbeleid_l5,2026-08-01T01:45:00Z,2026-08-01T02:15:00Z,"
    "tick375: Groeipakket ISE 4.907bn + Gezinsbeleid 1.369bn BU2025 L5; FOI residual UA/KO; spawn rq_367"
)
if old not in text:
    raise SystemExit("rq_366 row not found for replace")
rq_path.write_text(text.replace(old, new), encoding="utf-8")
with rq_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_367,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T02:15:00Z,,Spawned tick375 after Groeipakket+KO L5; rq_116 SWA deferred\n"
    )
print("rq_366 done + rq_367 open")

# --- foi queue ---
foi_row = (
    "gap_vl_gp_gezinsbeleid_l5,Vlaanderen>Opgroeien>Groeipakket_Gezinsbeleid>L5,opgroeien,"
    "Per-private-UA admin EUR (Kidslife Infino MyFamily Parentia) under 67.082m + benefit channel "
    "AGEF2QB vs AGEF2QY cash-by-year 2023-2026; GDF-AGEF2UA-WT absolute total and KO sector/provider "
    "top20 under ISE 1.369bn; BO2026 GEF2QX/QY/UX lines; dual unit-cost WAL CAF/Iriscare,"
    "ISE totals+VUTG L5 public strong 2025; end-receiver and per-UA residual,6,"
    "Opgroeien / VUTG / Team Openbaarheid,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_gp_gezinsbeleid_l5.md,"
    "ready,2026-08-01,,,,,cmt_vl_groeipakket_l5_2025|cmt_vl_gezinsbeleid_l5_2025,"
    "lb_vl_groeipakket_ise_4_91bn|lb_vl_gezinsbeleid_ise_1_37bn,"
    "2026-08-01T02:15:00Z,2026-08-01T02:15:00Z,"
    "tick375 draft ready human send only; partial 2025 fill; updates gap_vl_groeipakket_bo2026_line residual"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_row + "\n")

foi_path = DATA / "foi_queue.csv"
ft = foi_path.read_text(encoding="utf-8")
old_foi = (
    "gap_vl_groeipakket_bo2026_line,Vlaanderen>Opgroeien>Groeipakket>BO2026_GEF2QY,opgroeien,"
    "Exact BO2026 VAK/VEK for GB0-1GEF2QX-IS and GB0-1GEF2QY-IS Groeipakket lines; private vs public "
    "payment actor admin cash-by-year 2023-2026; unit cost per dossier,"
    "2025 awards ~4.7bn strong; VUTG admin 42.6m strong; full BO line codes and dual unit costs thin,5,"
    "Opgroeien / VUTG / Team Openbaarheid,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_groeipakket_bo2026_line.md,"
    "ready,2026-07-29,,,,,cmt_groeipakket_2025_26,lb_groeipakket_4_7bn|lb_be_af_triple_map,"
    "2026-07-29T06:35:00Z,2026-07-29T06:35:00Z,tick239 draft ready human send"
)
new_foi = (
    "gap_vl_groeipakket_bo2026_line,Vlaanderen>Opgroeien>Groeipakket>BO2026_GEF2QY,opgroeien,"
    "Exact BO2026 VAK/VEK for GB0-1GEF2QX-IS and GB0-1GEF2QY-IS Groeipakket lines; residual multi-year "
    "after 2025 BU fill; unit cost per dossier dual private,"
    "2025 BU ISE 4.907bn GEF2QX 4.797 GEF2QY 109.57 private UA 67.1m filled tick375; BO2026+per-UA residual,5,"
    "Opgroeien / VUTG / Team Openbaarheid,openbaarheid@vlaanderen.be,"
    "Havenlaan 88 bus 20 1000 Brussel,docs/doge/foi/drafts/gap_vl_groeipakket_bo2026_line.md,"
    "ready,2026-07-29,,,,,cmt_vl_groeipakket_l5_2025,lb_vl_groeipakket_ise_4_91bn,"
    "2026-07-29T06:35:00Z,2026-08-01T02:15:00Z,tick239|tick375: 2025 strong fill; residual BO2026+per-UA human send"
)
if old_foi not in ft:
    print("WARN: old FOI row not exact match; skip update")
else:
    foi_path.write_text(ft.replace(old_foi, new_foi), encoding="utf-8")
    print("foi gap_vl_groeipakket_bo2026_line updated")

# --- loop_state ---
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T02:15:00Z,rq_366,375,no,"
    "Scheduler 60s. Next prio5 rq_367; rq_116 SWA deferred. FOI ready. tick375 Groeipakket 4.91bn + KO 1.37bn.\n",
    encoding="utf-8",
)
print("loop_state ticks=375")
print("OK", DATA)
