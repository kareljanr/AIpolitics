# tick379: ONSS/RSZ RA2025 budget de gestion L5 + collection financing
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

# amounts in table are x1000 EUR
def k(n):
    return n * 1000

# --- sources ---
src = (
    "src_onss_ra_2025_budget,"
    "ONSS Rapport annuel 2025 budget de gestion + chiffres clefs financement,"
    "https://www.onssrapportannuel.be/2025/fr/chiffres-clefs-de-l-onss/budget/index.html,"
    "ONSS-RSZ,"
    "2026-08-01,primary_annual_report,"
    '"Gestion 2025 x1000: pers 172571 fonct 123651 invest 4989 total 301211; Smals fonct 108957 invest 1949; cotis 83.4bn alt 22.7bn state 11.8bn; dual Smals"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

# --- budgets ---
# 2023-2025 series gestion
series = [
    # personnel
    ("bud_onss_pers_2023", 2023, 158104, "outturn", "ONSS depenses personnel gestion 2023 158.104m"),
    ("bud_onss_pers_2024", 2024, 167438, "outturn", "ONSS depenses personnel gestion 2024 167.438m"),
    ("bud_onss_pers_2025", 2025, 172571, "outturn", "ONSS depenses personnel gestion 2025 172.571m (57pct of gestion)"),
    # fonct total
    ("bud_onss_fonct_2023", 2023, 123328, "outturn", "ONSS fonctionnement total 2023 123.328m"),
    ("bud_onss_fonct_2024", 2024, 123717, "outturn", "ONSS fonctionnement total 2024 123.717m"),
    ("bud_onss_fonct_2025", 2025, 123651, "outturn", "ONSS fonctionnement total 2025 123.651m"),
    # fonct ordinary
    ("bud_onss_fonct_ord_2025", 2025, 13228, "outturn", "Fonctionnement ordinaire 2025 13.228m (~5pct locaux Mess)"),
    # IT fonct
    ("bud_onss_it_fonct_2025", 2025, 110423, "outturn", "Fonctionnement informatique 2025 110.423m"),
    ("bud_onss_smals_fonct_2023", 2023, 107002, "outturn", "Smals IT fonctionnement 2023 107.002m"),
    ("bud_onss_smals_fonct_2024", 2024, 107353, "outturn", "Smals IT fonctionnement 2024 107.353m"),
    ("bud_onss_smals_fonct_2025", 2025, 108957, "outturn", "Smals IT fonctionnement 2025 108.957m (+2.35pct; ~37pct gestion)"),
    ("bud_onss_it_autres_2025", 2025, 1466, "outturn", "IT fonctionnement autres tiers 2025 1.466m"),
    # invest
    ("bud_onss_invest_2023", 2023, 1330, "outturn", "Investissement total 2023 1.330m"),
    ("bud_onss_invest_2024", 2024, 1495, "outturn", "Investissement total 2024 1.495m"),
    ("bud_onss_invest_2025", 2025, 4989, "outturn", "Investissement total 2025 4.989m (1.1pct gestion)"),
    ("bud_onss_smals_invest_2025", 2025, 1949, "outturn", "Smals IT investissement 2025 1.949m"),
    ("bud_onss_it_invest_autres_2025", 2025, 275, "outturn", "IT invest autres tiers 2025 0.275m"),
    ("bud_onss_invest_mobilier_2025", 2025, 99, "outturn", "Invest mobilier 2025 0.099m"),
    ("bud_onss_invest_immo_2025", 2025, 2666, "outturn", "Invest immobilier 2025 2.666m"),
    # totals
    ("bud_onss_gestion_total_2025", 2025, 301211, "outturn", "Gestion total 2025 172.571+123.651+4.989=301.211m; pers+Smals>93pct"),
    ("bud_onss_smals_total_2025", 2025, 110906, "outturn", "Smals ONSS path fonct+invest 108.957+1.949=110.906m dual Smals omzet"),
    # financing headlines (missions - bn scale)
    ("bud_onss_cotisations_2025", 2025, 83400000000, "outturn", "Cotisations percues 83.4bn 2025; payment on time 95.89pct"),
    ("bud_onss_financement_alternatif_2025", 2025, 22700000000, "outturn", "Financement alternatif 22.7bn 2025"),
    ("bud_onss_subventions_etat_2025", 2025, 11800000000, "outturn", "Subventions de l etat 11.8bn 2025"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, yr, amt_k, basis, notes in series:
        if "cotisations" in bid or "financement" in bid or "subventions" in bid:
            amt = amt_k  # already full euros
        else:
            amt = k(amt_k)
        f.write(
            f'{bid},rsz,{yr},{amt},,,,{basis},src_onss_ra_2025_budget,strong,"{notes}"\n'
        )
print("budgets +", len(series))

# --- commitments ---
cmt = (
    "cmt_onss_gestion_2023_25,ONSS budget de gestion 2023-2025 dual Smals,rsz,"
    "Employers workers SS administration via ONSS Smals,"
    "Loi ONSS / contrat administration IPSS,"
    "2023-01-01,2023,2025,301211000,"
    '"{""gestion_2023_m"":282.762,""gestion_2024_m"":292.65,""gestion_2025_m"":301.211,'
    '""pers_2025_m"":172.571,""fonct_2025_m"":123.651,""invest_2025_m"":4.989,'
    '""smals_fonct_2025_m"":108.957,""smals_invest_2025_m"":1.949,""smals_total_2025_m"":110.906,'
    '""pers_pct"":57,""smals_pct_class"":37,""pers_smals_gt93pct"":true,'
    '""cotisations_2025_bn"":83.4,""alt_finance_2025_bn"":22.7,""state_subs_2025_bn"":11.8,'
    '""employers"":251734,""workers_m"":4.0,""staff_headcount"":1668,""staff_statutaire"":1578,'
    '""payment_on_time_pct"":95.89,""coa_beheer_2023_m"":282.8,'
    '""note"":""Strong RA2025 table x1000; mission budget non-limitative residual detail FOI; dual Smals omzet 579m""}",'
    "0,active,https://www.onssrapportannuel.be/2025/fr/chiffres-clefs-de-l-onss/budget/index.html,"
    "Collect and administer employee SS contributions and finance branches,"
    "Publish mission budget full L5; dual Smals member matrix; unit cost per employer,"
    "src_onss_ra_2025_budget,strong,SS>ONSS>gestion_2025,"
    "tick379: gestion 301.2m Smals 110.9m cotis 83.4bn\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt +1")

# --- leaderboard ---
lbs = [
    (
        "lb_onss_gestion_301m_2025",
        "ONSS budget de gestion 301.2m 2025",
        "federal",
        "ops",
        "SS>ONSS>gestion",
        301211000,
        301211000,
        "Strong RA2025: pers 172.6 + fonct 123.7 + invest 5.0 = 301.2m; limited credits; dual CoA 2023 282.8m path",
        "strong",
        "src_onss_ra_2025_budget",
        "Employers workers SS system",
        "ONSS institutional operating budget",
        "Core admin not pure waste; >93pct personnel+Smals",
        3,
        7.5,
        4,
        5.78,
        "Open mission budget detail; dual Smals L5",
        "seed",
        "",
        "tick379",
    ),
    (
        "lb_onss_personnel_173m_2025",
        "ONSS personnel costs 172.6m 2025",
        "federal",
        "ops",
        "SS>ONSS>personnel",
        172571000,
        172571000,
        "Strong: 172.571m = 57pct gestion; +3pct yoy index/seniority; ETP paid down; headcount 1668 class",
        "strong",
        "src_onss_ra_2025_budget",
        "ONSS staff 1578 statutory + 90 contract",
        "Wage bill social security office",
        "Core labour; dual other IPSS admin",
        2,
        7.5,
        3,
        5.43,
        "Publish FTE by directorate multi-year",
        "seed",
        "",
        "tick379",
    ),
    (
        "lb_onss_smals_111m_2025",
        "ONSS Smals IT path 110.9m 2025",
        "federal",
        "ops",
        "SS>ONSS>Smals",
        110906000,
        110906000,
        "Strong: Smals fonct 108.957 + invest 1.949 = 110.906m; ~37pct gestion; dual Smals omzet 578.9m",
        "strong",
        "src_onss_ra_2025_budget",
        "ONSS via Smals shared ICT",
        "Shared SS ICT services recharges",
        "Largest non-wage gestion line; dual gap_smals_l5_members",
        4,
        7.5,
        4,
        5.93,
        "Open ONSS share of Smals member matrix; NRRR EU share",
        "seed",
        "",
        "tick379",
    ),
    (
        "lb_onss_cotisations_83_4bn_2025",
        "ONSS cotisations percues 83.4bn 2025",
        "federal",
        "transfer",
        "SS>ONSS>cotisations",
        83400000000,
        83400000000,
        "Strong homepage RA2025: 83.4bn cotisations; 95.89pct paid on time; dual Globaal Beheer path",
        "strong",
        "src_onss_ra_2025_budget",
        "4m workers 251734 employers",
        "Collect employee social security contributions",
        "Core SS financing mega; not waste; mission L5 residual",
        2,
        10.0,
        3,
        6.73,
        "Publish mission budget full branch split cash",
        "seed",
        "",
        "tick379",
    ),
    (
        "lb_onss_alt_finance_22_7bn_2025",
        "ONSS alternative financing 22.7bn 2025",
        "federal",
        "transfer",
        "SS>ONSS>financement_alternatif",
        22700000000,
        22700000000,
        "Strong RA2025: 22.7bn alternative financing + 11.8bn state subsidies class",
        "strong",
        "src_onss_ra_2025_budget",
        "SS branches financed via alt + state",
        "Alternative financing of social security",
        "Core fiscal-SS interface; method dual FPS residual",
        3,
        9.5,
        4,
        6.68,
        "Publish alt-finance instrument L5 multi-year",
        "seed",
        "",
        "tick379",
    ),
    (
        "lb_onss_state_subs_11_8bn_2025",
        "ONSS state subsidies 11.8bn 2025",
        "federal",
        "transfer",
        "SS>ONSS>subventions_etat",
        11800000000,
        11800000000,
        "Strong RA2025: subventions de l etat 11.8bn",
        "strong",
        "src_onss_ra_2025_budget",
        "SS system via state budget transfers",
        "Federal subsidies to SS financing",
        "Core transfer; dual FPS budget codes residual FOI",
        3,
        9.0,
        4,
        6.28,
        "Map FPS article codes cash-by-year",
        "seed",
        "",
        "tick379",
    ),
]
with (DATA / "leaderboard.csv").open("a", encoding="utf-8", newline="") as f:
    for row in lbs:
        parts = [
            row[0], row[1], row[2], row[3], row[4],
            str(row[5]), str(row[6]), f'"{row[7]}"', row[8], row[9],
            row[10], row[11], f'"{row[12]}"',
            str(row[13]), str(row[14]), str(row[15]), str(row[16]),
            f'"{row[17]}"', row[18], row[19], f'"{row[20]}"',
        ]
        f.write(",".join(parts) + "\n")
print("lb +", len(lbs))

# update rsz entity notes (first matching line with tick278)
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
old1 = "rsz,Rijksdienst voor Sociale Zekerheid RSZ,Office national de securite sociale ONSS,National Social Security Office,parastatal,sec_ss,bi,https://www.rsz.be,,,Centralises employee SS funds Globaal Beheer; beheer 282.8m 2023; opdrachten 106.9bn; tick278"
new1 = "rsz,Rijksdienst voor Sociale Zekerheid RSZ,Office national de securite sociale ONSS,National Social Security Office,parastatal,sec_ss,bi,https://www.rsz.be,,,Centralises employee SS; gestion 301.2m 2025 Smals 110.9m; cotis 83.4bn; tick278+379"
if old1 in ent:
    ent = ent.replace(old1, new1)
    print("entity rsz updated")
else:
    print("WARN rsz entity not exact")
(DATA / "entities.csv").write_text(ent, encoding="utf-8")

# research queue
rq_path = DATA / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_370,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T03:45:00Z,,Spawned tick378 after Samusocial 72.4m; rq_116 SWA deferred"
)
new = (
    "rq_370,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_onss_mission_l5,2026-08-01T03:45:00Z,2026-08-01T04:15:00Z,"
    "tick379: ONSS gestion 301.2m Smals 110.9m cotis 83.4bn; FOI mission L5; spawn rq_371"
)
if old not in text:
    raise SystemExit("rq_370 not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")
with rq_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_371,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Note: tick 380 = mandatory progress coverage % + waste top10.,,"
        "2026-08-01T04:15:00Z,,Spawned tick379 after ONSS gestion; next may be progress@380; rq_116 SWA deferred\n"
    )
print("rq done")

# foi
foi = (
    "gap_onss_mission_l5,SS>ONSS>mission_budget_L5,rsz,"
    "Full mission budget recettes/depenses branch split cash-by-year 2023-2026 (travailleurs locaux Maribel SSOM marins); "
    "FPS article codes for 11.8bn state subsidies and 22.7bn alt finance components; reconcile CoA opdrachten path; "
    "ETP by directorate multi-year,"
    "Gestion L5 strong RA2025; mission non-limitative aggregates thin; dual Smals FOI already open,6,"
    "ONSS-RSZ / FOD SZ / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_onss_mission_l5.md,ready,2026-08-01,,,,,"
    "cmt_onss_gestion_2023_25,lb_onss_gestion_301m_2025|lb_onss_cotisations_83_4bn_2025,"
    "2026-08-01T04:15:00Z,2026-08-01T04:15:00Z,"
    "tick379 draft ready human send; gestion filled; mission residual"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")
print("foi +1")

# loop state - note next progress at 380
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T04:15:00Z,rq_370,379,no,"
    "Scheduler 60s. Next: progress@380 then rq_371; rq_116 SWA deferred. FOI ready. tick379 ONSS gestion 301m.\n",
    encoding="utf-8",
)
print("state 379 OK")
