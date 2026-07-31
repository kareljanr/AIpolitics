# tick 599 — VLIZ dual marine research hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T15:30:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "vliz,VLIZ Vlaams Instituut voor de Zee,VLIZ Institut flamand de la Mer,"
        "Flanders Marine Institute dual ILVO marine Belgica,parastatal,sec_flanders,nl,"
        "https://www.vliz.be,,,Ostend InnovOcean; turnover 19.61m 2025 (26.40m 2024); "
        "Flemish grants 11.879m external 10.078m; staff 178; dual ILVO marine + RV Belgica; tick599\n"
    )

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vliz_mgmt_indicators_2025,VLIZ Annual Report management indicators 2025,"
        "https://www.vliz.be/sites/vliz.be/files/vliz_annual_report_management_indicators_2025def.pdf,"
        "VLIZ Flanders Marine Institute,2026-07-31,official_annual_report,"
        "Strong tick599: turnover 19610837 2025 / 26402745 2024 / 19162933 2023; "
        "Flemish grants 11879000; external financing 10077970 (84.8pct of Flemish grants); "
        "social liability 1593513; staff 178 (fixed 66 contractual 109); 27 new projects; "
        "project revenue methodology change 2025; raw vliz_management_indicators_2025.pdf\n"
    )
    f.write(
        "src_dual_marine_vliz_ilvo_tick599,Dual marine research VLIZ + ILVO + Belgica,"
        "docs/doge/raw/vliz_management_indicators_2025.pdf,DOGE synthesis VLIZ indicators + ILVO,"
        "2026-07-31,synthesis,"
        "Strong dual: VLIZ turnover 19.6m staff 178 marine vs ILVO agri-marine stack 24.9+50.3m; "
        "InnovOcean campus shared; RV Belgica federal dual; tick599\n"
    )

# --- budgets ---
bud_rows = [
    ("bud_vliz_turnover_2025", 2025, 19610837, "VLIZ turnover 19.610837m 2025 management indicators; tick599"),
    ("bud_vliz_turnover_2024", 2024, 26402745, "VLIZ turnover 26.402745m 2024 (spike YoY); tick599"),
    ("bud_vliz_turnover_2023", 2023, 19162933, "VLIZ turnover 19.162933m 2023; tick599"),
    ("bud_vliz_flemish_grants_2025", 2025, 11879000, "VLIZ Flemish grants operations+investment 11.879m 2025; tick599"),
    ("bud_vliz_external_fin_2025", 2025, 10077970, "VLIZ external financing 10.07797m 2025 (84.8pct of Flemish grants); tick599"),
    ("bud_vliz_social_liab_2025", 2025, 1593513, "VLIZ social liability 1.593513m 2025; tick599"),
    ("bud_vliz_social_liab_2024", 2024, 1504130, "VLIZ social liability 1.50413m 2024; tick599"),
    ("bud_vliz_staff_2025", 2025, 0, "VLIZ total employees 178 2025 (not EUR); tick599"),
    ("bud_vliz_fixed_staff_2025", 2025, 0, "VLIZ fixed employees 66 2025 (not EUR); tick599"),
    ("bud_vliz_contract_staff_2025", 2025, 0, "VLIZ contractual employees 109 2025 (not EUR); tick599"),
    ("bud_vliz_projects_init_2025", 2025, 0, "VLIZ initiated research projects external budget 27 in 2025 (30 in 2024); tick599"),
    ("bud_vliz_members_2025", 2025, 0, "VLIZ members 1119 of which partner 338 institutional 34; tick599"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, year, amt, note in bud_rows:
        f.write(
            f"{bid},vliz,{year},{amt},,,outturn,src_vliz_mgmt_indicators_2025,strong,{note}\n"
        )

# --- commitments ---
cmt_vliz = {
    "2025_turnover": 19610837,
    "2024_turnover": 26402745,
    "2023_turnover": 19162933,
    "2025_flemish_grants": 11879000,
    "2025_external": 10077970,
    "2025_social_liability": 1593513,
    "staff": 178,
    "fixed_staff": 66,
    "contractual": 109,
    "projects_initiated_2025": 27,
    "note": "Marine research dual ILVO InnovOcean + Belgica; methodology change project revenue 2025",
}
cmt_dual = {
    "vliz_turnover_m": 19.61,
    "vliz_flemish_m": 11.879,
    "vliz_staff": 178,
    "ilvo_iva_exp_m": 24.9,
    "ilvo_ev_out_m": 50.3,
    "ilvo_staff": 756,
    "note": "Dual marine-agri Flanders research VLIZ vs ILVO; shared InnovOcean Ostend",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_vliz_mgmt_2025,VLIZ marine dual ILVO Belgica 2025,vliz,'
        f'Flanders marine science industry EU,VL grants + external projects,'
        f'2025-01-01,2023,2030,19610837,"{esc_json(cmt_vliz)}",0,active,'
        f'https://www.vliz.be,Flanders marine research data vessels,'
        f'Publish full jaarrekening recon + multi-year VL structural FOI,'
        f'src_vliz_mgmt_indicators_2025,strong,Vlaanderen>Marine>VLIZ,tick599 indicators primary new entity\n'
    )
    f.write(
        f'cmt_dual_marine_vliz_ilvo_2025,Dual marine VLIZ + ILVO Flanders 2025,gg_belgium,'
        f'Flanders marine and agri-marine research,VLIZ indicators + ILVO CoA,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual VLIZ ILVO marine agri,FOI dual unit-cost + Simon Stevin L5,'
        f'src_dual_marine_vliz_ilvo_tick599,strong,BE>dual>marine_VLIZ_ILVO,tick599\n'
    )

# --- leaderboard ---
lb = [
    (
        "lb_vliz_turnover_20m_2025",
        "VLIZ turnover 19.6m 2025 (26.4m 2024 spike) dual marine",
        "Flanders",
        "ops",
        "Vlaanderen>Marine>VLIZ>turnover_20m",
        19610837,
        19610837,
        "Strong indicators: 19.611m 2025 vs 26.403m 2024 vs 19.163m 2023; methodology note project revenue",
        "src_vliz_mgmt_indicators_2025",
        "VL marine science",
        "Flanders marine institute ops",
        "Core public science; 2024 spike opacity FOI",
        3,
        7.5,
        4,
        5.50,
        "Full jaarrekening FOI",
    ),
    (
        "lb_vliz_turnover_26m_2024",
        "VLIZ turnover 26.4m 2024 spike YoY",
        "Flanders",
        "ops",
        "Vlaanderen>Marine>VLIZ>turnover_26m_2024",
        26402745,
        26402745,
        "Strong: 2024 turnover 26.403m +37pct vs 2023; 2025 reverts 19.611m",
        "src_vliz_mgmt_indicators_2025",
        "VLIZ",
        "Marine research peak year",
        "Spike vs trend FOI residual",
        4,
        7.5,
        5,
        5.75,
        "Explain 2024 spike FOI",
    ),
    (
        "lb_vliz_flemish_grants_12m_2025",
        "VLIZ Flemish grants 11.9m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Marine>VLIZ>flemish_grants_12m",
        11879000,
        11879000,
        "Strong: Flemish grants ops+investment 11.879m 2025",
        "src_vliz_mgmt_indicators_2025",
        "VL taxpayers",
        "Structural and investment grants marine",
        "Grant L5 multi-year residual",
        4,
        7.0,
        4,
        5.25,
        "Multi-year VL grant FOI",
    ),
    (
        "lb_vliz_external_10m_2025",
        "VLIZ external financing 10.1m 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Marine>VLIZ>external_10m",
        10077970,
        10077970,
        "Strong: external 10.078m = 84.8pct of Flemish grants; projects province ESFRI EU",
        "src_vliz_mgmt_indicators_2025",
        "EU province projects",
        "Competitive external marine funding",
        "Project mix dual ILVO",
        3,
        7.0,
        4,
        5.05,
        "Project L5 FOI",
    ),
    (
        "lb_vliz_staff_178_2025",
        "VLIZ staff 178 fixed 66 contractual 109 2025",
        "Flanders",
        "ops",
        "Vlaanderen>Marine>VLIZ>staff_178",
        0,
        0,
        "Strong: 178 employees; contractual majority dual project path",
        "src_vliz_mgmt_indicators_2025",
        "VLIZ staff",
        "Operate marine institute vessels data",
        "Core ops dual marine FTE",
        3,
        6.5,
        3,
        4.75,
        "Benchmark dual marine FTE",
    ),
    (
        "lb_dual_marine_vliz_ilvo_2025",
        "Dual marine VLIZ 19.6m + ILVO agri-marine stack dual",
        "multi",
        "ops",
        "BE>dual>marine_VLIZ_ILVO_2025",
        19610837,
        75200000,
        "Strong dual: VLIZ 19.6m/178 staff marine vs ILVO IVA+EV ~75m/756; InnovOcean shared Ostend",
        "src_dual_marine_vliz_ilvo_tick599",
        "Flanders marine agri dual",
        "Map dual VLIZ ILVO research",
        "VL grant L5 both residual",
        4,
        8.0,
        5,
        6.15,
        "FOI dual grant matrix marine",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        (
            lid, title, jur, cat, hpath, annual, stock, note, src,
            spenders, purpose, mech, prio, scale, opac, pidx, hook,
        ) = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"{spenders},{purpose},{mech},{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick599\n"
        )

# --- foi ---
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_vliz_jaarrekening_l5_2025,Vlaanderen>VLIZ>jaarrekening_L5_2025,vliz,"
        "Full statutory jaarrekening 2024-25 recon to turnover 19.6m/26.4m; multi-year VL structural vs "
        "Flemish grants 11.879m; 2024 turnover spike explain; external project L5; Simon Stevin ops cost; "
        "dual unit-cost vs ILVO,"
        "Indicators turnover grants strong tick599; full accounts residual,5,"
        "VLIZ / Vlaanderen WEWIS / openbaarheid,,https://www.vliz.be,"
        "docs/doge/foi/drafts/gap_vliz_jaarrekening_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_vliz_mgmt_2025|cmt_dual_marine_vliz_ilvo_2025,"
        "lb_vliz_turnover_20m_2025|lb_dual_marine_vliz_ilvo_2025,"
        f"{utc},{utc},tick599 VLIZ indicators primary; residual jaarrekening human send\n"
    )

# --- research_queue ---
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_590,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:15:00Z,,Spawned tick598 after CRA-W dual ILVO; rq_116 deferred; progress@600 in 2"
)
new = (
    "rq_590,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:15:00Z,2026-07-31T15:30:00Z,"
    "tick599: VLIZ turnover 19.6m Flemish grants 11.9m dual ILVO marine; spawn rq_591; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_590 row not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_591,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:30:00Z,,Spawned tick599 after VLIZ dual marine; rq_116 deferred; progress@600 NEXT TICK\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_590,599,no,"
    "tick599 VLIZ turnover 19.6m Flemish grants 11.9m dual ILVO marine; next rq_591; progress@600 NEXT; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick599 CSV writes OK")
