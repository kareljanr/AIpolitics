# tick381: RVA/ONEM JV2025 budget L5 opdrachten+beheer
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

def k(n):
    return int(n * 1000)

# --- sources ---
src = (
    "src_rva_jv_2025_vol1,"
    "RVA Jaarverslag 2025 vol1 budget opdrachten beheer gewestelijk,"
    "https://www.rva.be/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/4c72432bbd4f872cdeb5b77cd1fc696928bca847/jv-2025-vol1-volledig-nl.pdf,"
    "RVA-ONEM,"
    "2026-08-01,primary_annual_report,"
    '"JV2025 tables 1.4.6 keuro: global exp 7371m beheer 306.6m pers 236.0 UI 233.6 sociale prestaties 6383m; dual ONSS; payment channel FOI residual"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

# --- budgets ---
rows = [
    # global
    ("bud_rva_global_rec_2025", 2025, 7343783, "outturn", "RVA global receipts 7343.783m keuro table1.4.6.I"),
    ("bud_rva_global_exp_2025", 2025, 7371035, "outturn", "RVA global exp 7371.035m; saldo -27.252m"),
    ("bud_rva_global_rec_2024", 2024, 6969374, "outturn", "RVA global receipts 6969.374m 2024 CoA-corrected"),
    ("bud_rva_global_exp_2024", 2024, 7011991, "outturn", "RVA global exp 7011.991m 2024"),
    # opdrachten
    ("bud_rva_opdr_rec_2025", 2025, 7219572, "outturn", "Opdrachten receipts 7219.572m (GFB 6658.819 + own 560.753)"),
    ("bud_rva_opdr_gfb_2025", 2025, 6658819, "outturn", "Ontvangsten globaal financieel beheer RSZ path 6658.819m"),
    ("bud_rva_opdr_eigen_2025", 2025, 560753, "outturn", "Eigen ontvangsten opdrachten 560.753m"),
    ("bud_rva_opdr_exp_2025", 2025, 6950791, "outturn", "Opdrachten exp total 6950.791m"),
    ("bud_rva_sociale_prestaties_2025", 2025, 6383351, "outturn", "Sociale prestaties 6383.351m (~92pct opdrachten)"),
    ("bud_rva_sociale_prestaties_2024", 2024, 6362845, "outturn", "Sociale prestaties 6362.845m 2024"),
    ("bud_rva_ui_vergoedingen_2025", 2025, 233604, "outturn", "Vergoedingen uitbetalingsinstellingen 233.604m (ACV ABVV ACLVB/SYNOVA HVW channels)"),
    ("bud_rva_ui_vergoedingen_2024", 2024, 234995, "outturn", "UI vergoedingen 234.995m 2024"),
    ("bud_rva_diverse_opdr_2025", 2025, 333837, "outturn", "Diverse uitgaven opdrachten 333.837m"),
    # beheer
    ("bud_rva_beheer_exp_2025", 2025, 306638, "outturn", "Beheersbegroting exp 306.638m (+11.39m vs 2024)"),
    ("bud_rva_beheer_exp_2024", 2024, 295248, "outturn", "Beheer exp 295.248m 2024"),
    ("bud_rva_beheer_exp_2023", 2023, 277909, "outturn", "Beheer exp 277.909m 2023 matches CoA prior"),
    ("bud_rva_beheer_pers_2025", 2025, 236021, "outturn", "Personeelsuitgaven beheer 236.021m (77pct)"),
    ("bud_rva_beheer_pers_2024", 2024, 220513, "outturn", "Personeel beheer 220.513m 2024"),
    ("bud_rva_beheer_werking_2025", 2025, 65826, "outturn", "Werkingsuitgaven 65.826m (incl IT)"),
    ("bud_rva_beheer_werking_2024", 2024, 66797, "outturn", "Werking 66.797m 2024"),
    ("bud_rva_beheer_invest_2025", 2025, 4352, "outturn", "Investeringen 4.352m"),
    ("bud_rva_beheer_invest_2024", 2024, 7371, "outturn", "Invest 7.371m 2024"),
    ("bud_rva_beheer_rec_2025", 2025, 10546, "outturn", "Beheer eigen ontvangsten 10.546m"),
    # gewestelijk
    ("bud_rva_gewest_rec_2025", 2025, 113665, "outturn", "Gewestelijke opdrachten rec 113.665m (activation via regions)"),
    ("bud_rva_gewest_exp_2025", 2025, 113594, "outturn", "Gewestelijke opdrachten exp 113.594m saldo +0.071m"),
    ("bud_rva_gewest_exp_2024", 2024, 116220, "outturn", "Gewestelijk exp 116.220m 2024"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, yr, amt_k, basis, notes in rows:
        f.write(
            f'{bid},rva,{yr},{k(amt_k)},,,,{basis},src_rva_jv_2025_vol1,strong,"{notes}"\n'
        )
print("budgets +", len(rows))

# entity - check if rva exists
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
if "rva," not in ent and "\nrva," not in ent:
    with (DATA / "entities.csv").open("a", encoding="utf-8", newline="") as f:
        f.write(
            "rva,Rijksdienst voor Arbeidsvoorziening RVA,Office national de l emploi ONEM,"
            "National Employment Office unemployment benefits,parastatal,sec_ss,bi,https://www.rva.be,,,"
            "Global exp 7.371bn 2025; beheer 306.6m; UI vergoedingen 233.6m; staff 2959 FE; tick381\n"
        )
    print("entity +1")
else:
    # try update note
    import re
    m = re.search(r"^rva,[^\n]+", ent, re.M)
    if m:
        print("entity rva exists:", m.group(0)[:120])
    else:
        print("entity pattern odd")

# --- commitments ---
cmt = (
    "cmt_rva_budget_2023_25,RVA ONEM global and beheer budget path 2023-2025,rva,"
    "Unemployed career-break workers via UI funds HVW unions,"
    "Werkloosheidsreglementering / bestuursovereenkomst,"
    "2023-01-01,2023,2025,7371035000,"
    '"{""global_exp_2025_m"":7371.035,""global_rec_2025_m"":7343.783,'
    '""opdr_exp_2025_m"":6950.791,""sociale_2025_m"":6383.351,""ui_comp_2025_m"":233.604,'
    '""diverse_opdr_2025_m"":333.837,""beheer_2025_m"":306.638,""beheer_pers_2025_m"":236.021,'
    '""beheer_werking_2025_m"":65.826,""beheer_invest_2025_m"":4.352,'
    '""beheer_2024_m"":295.248,""beheer_2023_m"":277.909,""gewest_exp_2025_m"":113.594,'
    '""staff_fe_2025"":2959,""staff_vte_2025"":2621.6,""external_staff"":336,'
    '""beneficiaries_avg_month_2025"":726387,""note"":""Strong JV2025 tables keuro; per-union UI L5 residual FOI gap_unemp_pay_unit_cost; dual ONSS GFB""}",'
    "0,active,https://jaarverslag.rva.be/,"
    "Pay unemployment and career-break benefits via payment organisms,"
    "Open per-union L5 compensations; dual ONSS; unit cost per dossier,"
    "src_rva_jv_2025_vol1,strong,SS>RVA>budget_2025,"
    "tick381: global 7.371bn beheer 306.6 UI 233.6\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt +1")

# --- leaderboard ---
lbs = [
    (
        "lb_rva_global_7_37bn_2025",
        "RVA global expenditure 7.371bn 2025",
        "federal",
        "transfer",
        "SS>RVA>global",
        7371035000,
        7371035000,
        "Strong JV2025: global exp 7371.035m rec 7343.783m; opdrachten 6950.8m dominate",
        "strong",
        "src_rva_jv_2025_vol1",
        "726k avg monthly benefit recipients 2025",
        "Unemployment career-break outplacement benefits",
        "Core SS entitlement mega; dual ONSS financing; not pure waste",
        2,
        9.5,
        3,
        6.53,
        "Publish multi-year reform savings path post-2026",
        "seed",
        "",
        "tick381",
    ),
    (
        "lb_rva_sociale_prestaties_6_38bn_2025",
        "RVA sociale prestaties 6.383bn 2025",
        "federal",
        "transfer",
        "SS>RVA>sociale_prestaties",
        6383351000,
        6383351000,
        "Strong: 6383.351m benefits (~92pct of opdrachten); +20.5m yoy",
        "strong",
        "src_rva_jv_2025_vol1",
        "Unemployed SWT career-break beneficiaries",
        "Core benefit payments",
        "Core social; reform time-limit 2026 path",
        2,
        9.5,
        3,
        6.53,
        "Track reform caseload vs spend",
        "seed",
        "",
        "tick381",
    ),
    (
        "lb_rva_beheer_307m_2025",
        "RVA beheersbegroting 306.6m 2025",
        "federal",
        "ops",
        "SS>RVA>beheer",
        306638000,
        306638000,
        "Strong: 306.638m (pers 236.0 werking 65.8 invest 4.4); dual ONSS gestion 301m class",
        "strong",
        "src_rva_jv_2025_vol1",
        "RVA administration staff 2959 FE",
        "Institutional operating budget",
        "Core admin; dual ONSS Smals stack",
        3,
        7.5,
        3,
        5.68,
        "Open IT/Smals split inside werking; dual ONSS",
        "seed",
        "",
        "tick381",
    ),
    (
        "lb_rva_personeel_236m_2025",
        "RVA personnel costs 236.0m 2025",
        "federal",
        "ops",
        "SS>RVA>personnel",
        236021000,
        236021000,
        "Strong: 236.021m = 77pct beheer; path 210.9/220.5/236.0 2023-25; VTE 2622",
        "strong",
        "src_rva_jv_2025_vol1",
        "Internal staff 2959 FE + 336 external",
        "Wage bill employment office",
        "Core labour; headcount down long-run post-regionalisation",
        2,
        7.5,
        3,
        5.43,
        "Publish FTE by process cost map",
        "seed",
        "",
        "tick381",
    ),
    (
        "lb_rva_ui_comp_234m_2025",
        "RVA payment-organism compensations 233.6m 2025",
        "federal",
        "ops",
        "SS>RVA>uitbetalingsinstellingen",
        233604000,
        233604000,
        "Strong: 233.604m admin compensations to 4 payment channels; dual gap_unemp_pay_unit_cost L5 residual",
        "strong",
        "src_rva_jv_2025_vol1",
        "Union funds + HVW payment organisms",
        "Admin financing of unemployment payment channels",
        "Dual multi-channel opacity; per-union still FOI",
        6,
        7.5,
        5,
        6.48,
        "Open ABVV ACV ACLVB HVW cash-by-year unit cost",
        "seed",
        "",
        "tick381",
    ),
    (
        "lb_rva_gewest_114m_2025",
        "RVA regionalised activation budget 113.6m 2025",
        "federal",
        "transfer",
        "SS>RVA>gewestelijke_opdrachten",
        113594000,
        113594000,
        "Strong: gewestelijk exp 113.594m rec 113.665m; activation premiums executed for regions",
        "strong",
        "src_rva_jv_2025_vol1",
        "Regional activation beneficiaries",
        "6th reform residual execution via RVA",
        "Dual regional PES; declining path from 183m 2021",
        3,
        7.5,
        4,
        5.78,
        "Publish per-region split VL/WAL/BRU",
        "seed",
        "",
        "tick381",
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

# update gap_unemp notes if possible
foi_path = DATA / "foi_queue.csv"
ft = foi_path.read_text(encoding="utf-8")
# append note lightly via replace on known substring
old_note = "tick138 partial fill 169+219m; residual L5 human send,, | tick277: HVW beheer 47.9m + RVA 277.9m CoA 2023; residual per-union L5 still ready"
if old_note in ft:
    ft = ft.replace(
        old_note,
        "tick138|277|381: RVA UI vergoedingen 233.6m 2025 strong aggregate; residual per-union L5 still ready",
    )
    foi_path.write_text(ft, encoding="utf-8")
    print("foi unemp note updated")
else:
    print("foi unemp note skip")

# research queue
rq = DATA / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    "rq_372,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T04:45:00Z,,Spawned tick380 after progress; rq_116 SWA deferred"
)
new = (
    "rq_372,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_unemp_pay_unit_cost,2026-08-01T04:45:00Z,2026-08-01T05:15:00Z,"
    "tick381: RVA JV2025 global 7.371bn beheer 306.6 UI 233.6; residual per-union FOI; spawn rq_373"
)
if old not in text:
    raise SystemExit("rq_372 not found")
rq.write_text(text.replace(old, new), encoding="utf-8")
with rq.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_373,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T05:15:00Z,,Spawned tick381 after RVA 7.37bn; rq_116 SWA deferred\n"
    )
print("rq done")

# optional new FOI for RVA mission residual / FSO - light: update existing unemp is enough
# create gap_rva_process_cost_l5 for process cost map?
foi_new = (
    "gap_rva_werking_smals_l5,SS>RVA>werking_IT_Smals_L5,rva,"
    "Split werkingsuitgaven 65.826m 2025: Smals vs other IT vs ordinary; process full-cost map EUR; "
    "FSO budget perimeter inside/outside; multi-year 2023-2026,"
    "Beheer totals strong; IT/Smals and process EUR residual dual ONSS,5,"
    "RVA-ONEM / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_rva_werking_smals_l5.md,ready,2026-08-01,,,,,"
    "cmt_rva_budget_2023_25,lb_rva_beheer_307m_2025,"
    "2026-08-01T05:15:00Z,2026-08-01T05:15:00Z,"
    "tick381 draft ready human send; UI per-union remains gap_unemp_pay_unit_cost"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_new + "\n")
print("foi +1")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T05:15:00Z,rq_372,381,no,"
    "Scheduler 60s. Next prio5 rq_373; rq_116 SWA deferred. FOI ready. tick381 RVA global 7.37bn beheer 307m.\n",
    encoding="utf-8",
)
print("state 381 OK")
