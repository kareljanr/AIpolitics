# tick382: FSO Fonds Sluiting 2025 L5 from RVA JV chapter 5
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

# --- sources ---
src = (
    "src_fso_rva_jv_2025,"
    "FSO Fonds Sluiting Ondernemingen 2025 L5 via RVA Jaarverslag 2025 ch5,"
    "https://www.rva.be/file/cc73d96153bbd5448a56f19d925d05b1379c7f21/4c72432bbd4f872cdeb5b77cd1fc696928bca847/jv-2025-vol1-volledig-nl.pdf,"
    "Fonds voor Sluiting van Ondernemingen / RVA,"
    "2026-08-01,primary_annual_report,"
    '"FSO 2025: rec 516.68m exp compensations 371.94m TW 178.70m beheer 8.48m; Van Hool largest; dual RVA"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

# --- budgets ---
rows = [
    ("bud_fso_rec_total_2025", 2025, 516683434, "outturn", "FSO total receipts 516683433.79 EUR (+67pct)"),
    ("bud_fso_rec_industry_2025", 2025, 510568945, "outturn", "Industry/commerce receipts 510568945.34"),
    ("bud_fso_rec_socialprofit_2025", 2025, 6114488, "outturn", "Social profit + liberal professions receipts 6114488.45"),
    ("bud_fso_contrib_tw_2025", 2025, 237813500, "outturn", "Employer contributions temp unemployment financing 237813500 (+69pct; rate 0.16pct)"),
    ("bud_fso_contrib_classic_2025", 2025, 215046500, "outturn", "Employer contributions classic tasks 215046500 (+102pct; rate 0.22/0.17)"),
    ("bud_fso_bijzonder_comp_2025", 2025, 24831500, "outturn", "Bijzonder compenserende bijdrage verbrekingsvergoedingen 24831500"),
    ("bud_fso_terugvorderingen_2025", 2025, 32877348, "outturn", "Recoveries employers/employees industry 32877347.76"),
    ("bud_fso_comp_industry_2025", 2025, 366369009, "outturn", "Industry/commerce compensation total 366369008.53 (+55pct)"),
    ("bud_fso_contractueel_2025", 2025, 338689012, "outturn", "Contractuele vergoedingen industry 338689012.45 (92pct of industry; Van Hool effect)"),
    ("bud_fso_sluiting_vergoeding_2025", 2025, 23873552, "outturn", "Sluitingsvergoedingen industry 23873551.60"),
    ("bud_fso_overbrugging_2025", 2025, 3019419, "outturn", "Overbruggingsvergoedingen industry 3019418.76"),
    ("bud_fso_bedrijfstoeslag_2025", 2025, 787026, "outturn", "Bedrijfstoeslag industry 787025.72"),
    ("bud_fso_comp_socialprofit_2025", 2025, 5575161, "outturn", "Social profit compensations 5575161.40"),
    ("bud_fso_comp_total_2025", 2025, 371944170, "outturn", "Total compensation payouts 371944169.93 (industry+social profit)"),
    ("bud_fso_tw_share_2025", 2025, 178698864, "outturn", "FSO share temporary unemployment 178698863.66 (+35pct)"),
    ("bud_fso_tw_same_year_2025", 2025, 120032000, "outturn", "TW same-year advances 120032000 (+36.773m due 2026)"),
    ("bud_fso_beheer_2025", 2025, 8477683, "outturn", "Beheersuitgaven 8477682.82 (+8pct path from 7.8m 2023-24)"),
    ("bud_fso_beheer_2024", 2024, 7816485, "outturn", "Beheer 7816485.02 2024"),
    ("bud_fso_beheer_2023", 2023, 7808965, "outturn", "Beheer 7808965.08 2023 (prior CoA 7.7m class)"),
    ("bud_fso_comp_industry_2024", 2024, 236104245, "outturn", "Industry compensations 236104244.67 2024"),
    ("bud_fso_tw_share_2024", 2024, 132101507, "outturn", "TW share 132101507.10 2024"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, yr, amt, basis, notes in rows:
        f.write(
            f'{bid},fso,{yr},{amt},,,,{basis},src_fso_rva_jv_2025,strong,"{notes}"\n'
        )
print("budgets +", len(rows))

# update entity
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
old_e = "fso,Fonds Sluiting Ondernemingen FSO,Fonds de fermeture des entreprises,Company Closure Fund,parastatal,sec_ss,bi,https://www.fonds-sluiting.be,,,Closure compensations; exp 838.7m 2024; beheer 7.7m 2023; tick277"
new_e = "fso,Fonds Sluiting Ondernemingen FSO,Fonds de fermeture des entreprises,Company Closure Fund,parastatal,sec_ss,bi,https://www.fonds-sluiting.be,,,Compensations 371.9m + TW 178.7m + beheer 8.5m 2025; rec 516.7m; Van Hool peak; tick277+382"
if old_e in ent:
    (DATA / "entities.csv").write_text(ent.replace(old_e, new_e), encoding="utf-8")
    print("entity updated")
else:
    print("WARN entity")

# --- commitments ---
cmt = (
    "cmt_fso_budget_2025,FSO company closure fund 2025 multi-line L5,fso,"
    "Dismissed workers bankruptcy closures Van Hool etc,"
    "Wet 26 juni 2002 sluiting ondernemingen,"
    "2025-01-01,2025,2025,559121000,"
    '"{""rec_total"":516683434,""comp_total"":371944170,""comp_industry"":366369009,'
    '""contractueel"":338689012,""sluiting"":23873552,""overbrug"":3019419,""bedrijfstoeslag"":787026,'
    '""socialprofit"":5575161,""tw_share"":178698864,""beheer"":8477683,'
    '""contrib_tw"":237813500,""contrib_classic"":215046500,""bijzonder"":24831500,'
    '""beneficiaries_comp"":27626,""dossiers_opened"":5368,""applications"":18425,'
    '""van_hool_largest"":true,""note"":""Strong RVA JV2025 ch5; prior CoA 838.7m 2024 different perimeter class; dual RVA TW""}",'
    "0,active,https://jaarverslag.rva.be/,"
    "Compensate workers after company closures and finance TW share,"
    "Publish top-10 closure dossiers EUR; dual unit-cost; multi-year TW rate path,"
    "src_fso_rva_jv_2025,strong,SS>FSO>2025,"
    "tick382: rec 516.7m comp 371.9 TW 178.7 beheer 8.5\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt +1")

# --- leaderboard ---
lbs = [
    (
        "lb_fso_comp_372m_2025",
        "FSO closure compensations 371.9m 2025",
        "federal",
        "transfer",
        "SS>FSO>compensations",
        371944170,
        371944170,
        "Strong: 371.944m industry+socialprofit (+54pct); Van Hool largest dossier; 27626 beneficiaries",
        "strong",
        "src_fso_rva_jv_2025",
        "Workers after company closures",
        "Statutory closure compensation package",
        "Core social insurance not pure waste; peak cases drive volatility",
        3,
        7.5,
        4,
        5.78,
        "Publish top dossiers EUR; multi-year average cost",
        "seed",
        "",
        "tick382",
    ),
    (
        "lb_fso_contractueel_339m_2025",
        "FSO contractual wage compensations 338.7m 2025",
        "federal",
        "transfer",
        "SS>FSO>contractueel",
        338689012,
        338689012,
        "Strong: 338.689m = 92pct industry compensations; avg 19931 EUR/beneficiary; +57pct yoy",
        "strong",
        "src_fso_rva_jv_2025",
        "16993 beneficiaries contractual claims",
        "Unpaid wages/severance via closure fund",
        "Core; Van Hool cost spike",
        3,
        7.5,
        3,
        5.68,
        "Open largest employer dossiers",
        "seed",
        "",
        "tick382",
    ),
    (
        "lb_fso_tw_179m_2025",
        "FSO temporary unemployment share 178.7m 2025",
        "federal",
        "transfer",
        "SS>FSO>tijdelijke_werkloosheid",
        178698864,
        178698864,
        "Strong: 178.699m FSO share of RVA TW (33pct workers + 27pct white-collar suspension path); dual RVA",
        "strong",
        "src_fso_rva_jv_2025",
        "Employers using temporary unemployment",
        "Employer co-financing of TW via FSO",
        "Core labour-market stabiliser; rate path 0.16pct 2025",
        3,
        7.5,
        4,
        5.78,
        "Reconcile with RVA TW total; multi-year rate series",
        "seed",
        "",
        "tick382",
    ),
    (
        "lb_fso_rec_517m_2025",
        "FSO total receipts 516.7m 2025",
        "federal",
        "receipt",
        "SS>FSO>receipts",
        516683434,
        516683434,
        "Strong: 516.683m (+67pct); employer contrib TW 237.8 classic 215.0 bijzonder 24.8 recoveries 32.9",
        "strong",
        "src_fso_rva_jv_2025",
        "Employers financing closure fund",
        "Employer contributions and recoveries",
        "Financing side; rate doubling classic tasks 2025",
        2,
        8.5,
        3,
        5.93,
        "Publish contribution incidence by firm size",
        "seed",
        "",
        "tick382",
    ),
    (
        "lb_fso_beheer_8_5m_2025",
        "FSO management costs 8.48m 2025",
        "federal",
        "ops",
        "SS>FSO>beheer",
        8477683,
        8477683,
        "Strong: 8.478m beheer path 6.7-8.5m 2021-25; dual RVA staff hosting",
        "strong",
        "src_fso_rva_jv_2025",
        "FSO administration via RVA",
        "Fund operating costs",
        "Small admin vs 372m compensations",
        2,
        3.5,
        3,
        3.18,
        "Publish FTE hosted at RVA",
        "seed",
        "",
        "tick382",
    ),
    (
        "lb_fso_package_class_559m_2025",
        "FSO total package class ~559m 2025",
        "federal",
        "ops",
        "SS>FSO>package",
        559120717,
        559120717,
        "Strong sum: comp 371.944 + TW 178.699 + beheer 8.478 = 559.121m class institutional spend",
        "strong",
        "src_fso_rva_jv_2025",
        "Closure and TW co-finance system",
        "Full FSO institutional outlay class",
        "Not TE additive with RVA TW full; dual channels",
        3,
        8.5,
        4,
        6.18,
        "Publish single consol table annual",
        "seed",
        "",
        "tick382",
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

# research queue
rq = DATA / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    "rq_373,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T05:15:00Z,,Spawned tick381 after RVA 7.37bn; rq_116 SWA deferred"
)
new = (
    "rq_373,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_fso_top_dossiers_l5,2026-08-01T05:15:00Z,2026-08-01T05:45:00Z,"
    "tick382: FSO 2025 rec 516.7m comp 371.9 TW 178.7; FOI top dossiers; spawn rq_374"
)
if old not in text:
    raise SystemExit("rq_373 not found")
rq.write_text(text.replace(old, new), encoding="utf-8")
with rq.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_374,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T05:45:00Z,,Spawned tick382 after FSO 2025; rq_116 SWA deferred\n"
    )
print("rq done")

foi = (
    "gap_fso_top_dossiers_l5,SS>FSO>top_closure_dossiers_L5,fso,"
    "Top 20 closure dossiers by EUR 2023-2026 (incl Van Hool cash-by-year); per-type compensation "
    "matrix multi-year; FTE beheer hosted at RVA; reconcile any CoA 838.7m 2024 class vs JV path,"
    "Aggregates strong JV2025; end-receiver employer dossiers residual,6,"
    "Fonds voor Sluiting van Ondernemingen / RVA / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_fso_top_dossiers_l5.md,ready,2026-08-01,,,,,"
    "cmt_fso_budget_2025,lb_fso_comp_372m_2025|lb_fso_package_class_559m_2025,"
    "2026-08-01T05:45:00Z,2026-08-01T05:45:00Z,"
    "tick382 draft ready human send only"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")
print("foi +1")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T05:45:00Z,rq_373,382,no,"
    "Scheduler 60s. Next prio5 rq_374; rq_116 SWA deferred. FOI ready. tick382 FSO 517m rec 372m comp.\n",
    encoding="utf-8",
)
print("state 382 OK")
