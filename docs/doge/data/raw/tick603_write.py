# tick 603 — IBSA dual IWEPS multi-layer stats hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T16:30:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "ibsa,IBSA Institut Bruxellois Statistique Analyse,"
        "IBSA Brussels Institute for Statistics and Analysis,"
        "Brussels stats authority dual IWEPS Statbel embedded Perspective,"
        "agency,brussels_gov,fr,https://ibsa.brussels,,,"
        "Dept of Perspective.brussels; staff 42 end2025 (41 end2024); "
        "ops credits eng 809k liq 680k 2025 (ex personnel/comms/IT in Perspective); "
        "2024 eng 1130k liq 516k; dual IWEPS full UAP; tick603\n"
    )
    f.write(
        "perspective_bru,perspective.brussels,perspective.brussels,"
        "Brussels planning agency parent of IBSA dual,"
        "agency,brussels_gov,fr,https://perspective.brussels,,,"
        "Parent UAP of IBSA dept; personnel/comms/IT of IBSA in Perspective AB; tick603\n"
    )

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_ibsa_ra_2025,IBSA Rapport annuel 2025 ressources budget,"
        "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-FR-2025.pdf,"
        "IBSA / Perspective Brussels,2026-07-31,official_annual_report,"
        "Strong tick603: staff 42 31Dec2025; budget ops only eng 809000 liq 680000 "
        "(private 350k/320k public admin 459k/360k); personnel NOT in IBSA lines "
        "in Perspective AB; dual IWEPS; raw ibsa_ra_2025.pdf\n"
    )
    f.write(
        "src_ibsa_ra_2024,IBSA Rapport annuel 2024 ressources budget,"
        "https://ibsa.brussels/sites/default/files/publication/documents/RapportAnnuel-FR-2024-WEB.pdf,"
        "IBSA / Perspective Brussels,2026-07-31,official_annual_report,"
        "Strong tick603: staff 41 31Dec2024; budget eng 1130000 liq 516000 "
        "(private 475k/219k public 655k/297k); personnel in Perspective AB; raw ibsa_ra_2024.pdf\n"
    )
    f.write(
        "src_dual_stats_ibsa_iweps_tick603,Dual multi-layer stats IBSA BCR + IWEPS WAL,"
        "docs/doge/raw/ibsa_ra_2025.pdf,DOGE synthesis IBSA+IWEPS dual,"
        "2026-07-31,synthesis,"
        "Strong dual: IBSA embedded Perspective ops-only 0.68-0.81m visible staff 42 "
        "vs IWEPS standalone UAP rec 9.1m dep 11.4m staff 60; full IBSA TCO FOI residual; tick603\n"
    )

bud_rows = [
    ("bud_ibsa_eng_2025", 2025, 809000, "IBSA engagement credits ops stats 0.809m 2025 excl personnel; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_liq_2025", 2025, 680000, "IBSA liquidation credits ops stats 0.680m 2025 excl personnel; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_eng_private_2025", 2025, 350000, "IBSA eng private sector fonct 0.350m 2025; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_liq_private_2025", 2025, 320000, "IBSA liq private sector fonct 0.320m 2025; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_eng_public_2025", 2025, 459000, "IBSA eng public admin fonct 0.459m 2025; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_liq_public_2025", 2025, 360000, "IBSA liq public admin fonct 0.360m 2025; tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_eng_2024", 2024, 1130000, "IBSA engagement credits ops 1.130m 2024 excl personnel; tick603", "src_ibsa_ra_2024"),
    ("bud_ibsa_liq_2024", 2024, 516000, "IBSA liquidation credits ops 0.516m 2024 excl personnel; tick603", "src_ibsa_ra_2024"),
    ("bud_ibsa_staff_2025", 2025, 0, "IBSA staff 42 persons 31Dec2025 (not EUR; pay in Perspective); tick603", "src_ibsa_ra_2025"),
    ("bud_ibsa_staff_2024", 2024, 0, "IBSA staff 41 persons 31Dec2024 (not EUR); tick603", "src_ibsa_ra_2024"),
    ("bud_ibsa_stats_diffused_2025", 2025, 0, "IBSA statistics diffused 887 of which 34 new 2025 (not EUR); tick603", "src_ibsa_ra_2025"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, year, amt, note, src in bud_rows:
        f.write(f"{bid},ibsa,{year},{amt},,,outturn,{src},strong,{note}\n")

cmt = {
    "2025_eng": 809000,
    "2025_liq": 680000,
    "2024_eng": 1130000,
    "2024_liq": 516000,
    "staff_2025": 42,
    "staff_2024": 41,
    "parent": "perspective.brussels",
    "note": "Ops credits only; personnel/comms/IT in Perspective AB; dual IWEPS full UAP",
}
cmt_dual = {
    "ibsa_liq_2025_m": 0.68,
    "ibsa_staff": 42,
    "iweps_rec_2024_m": 9.066,
    "iweps_staff": 60,
    "note": "Dual multi-layer stats: IBSA embedded vs IWEPS standalone UAP opacity asymmetry",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_ibsa_ra_2025,IBSA dual IWEPS embedded Perspective 2024-25,ibsa,'
        f'Brussels government policy Stats,Perspective budget AB ops + personnel residual,'
        f'2024-01-01,2024,2030,680000,"{esc_json(cmt)}",0,active,'
        f'https://ibsa.brussels,Brussels public statistics analysis evaluation,'
        f'Publish full TCO incl Perspective personnel FOI,'
        f'src_ibsa_ra_2025,strong,Brussels>Stats>IBSA,tick603 RA2025 primary new entity\n'
    )
    f.write(
        f'cmt_dual_stats_ibsa_iweps_2025,Dual multi-layer stats IBSA + IWEPS 2024-25,gg_belgium,'
        f'Belgian multi-layer statistical system,IBSA RA + IWEPS RA dual,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual multi-layer regional stats institutes,FOI dual full TCO IBSA personnel,'
        f'src_dual_stats_ibsa_iweps_tick603,strong,BE>dual>stats_IBSA_IWEPS,tick603\n'
    )

lb = [
    (
        "lb_ibsa_liq_0_68m_2025",
        "IBSA ops liquidation 0.68m eng 0.81m 2025 excl personnel dual IWEPS",
        "Brussels",
        "ops",
        "Brussels>Stats>IBSA>liq_0_68m",
        680000,
        809000,
        "Strong RA2025: ops only eng 809k liq 680k; personnel in Perspective parent AB dual opacity",
        "src_ibsa_ra_2025",
        4,
        5.5,
        6,
        5.15,
        "Full TCO FOI Perspective",
    ),
    (
        "lb_ibsa_eng_1_13m_2024",
        "IBSA ops engagement 1.13m liq 0.52m 2024",
        "Brussels",
        "ops",
        "Brussels>Stats>IBSA>eng_1_13m_2024",
        516000,
        1130000,
        "Strong RA2024: eng 1.13m liq 0.516m ops only; eng-liq gap large",
        "src_ibsa_ra_2024",
        3,
        5.5,
        5,
        4.55,
        "Eng vs liq FOI",
    ),
    (
        "lb_ibsa_staff_42_2025",
        "IBSA staff 42 embedded Perspective dual IWEPS 60",
        "Brussels",
        "ops",
        "Brussels>Stats>IBSA>staff_42",
        0,
        0,
        "Strong: 42 staff end2025 (41 end2024); pay cost not published dual IWEPS 60 with full P&L",
        "src_ibsa_ra_2025",
        4,
        6.0,
        6,
        5.25,
        "Personnel cost FOI",
    ),
    (
        "lb_ibsa_opacity_parent_2025",
        "IBSA full TCO opacity personnel in Perspective parent 2025",
        "Brussels",
        "ops",
        "Brussels>Stats>IBSA>tco_opacity",
        0,
        0,
        "Strong RA disclaimer: personnel comms equipment in other Perspective AB; incomplete public cost",
        "src_ibsa_ra_2025",
        5,
        5.5,
        7,
        5.55,
        "FOI Perspective AB matrix",
    ),
    (
        "lb_dual_stats_ibsa_iweps_2025",
        "Dual multi-layer stats IBSA 0.68m ops + IWEPS 9.1m full UAP",
        "multi",
        "ops",
        "BE>dual>stats_IBSA_IWEPS_2025",
        680000,
        9066161,
        "Strong dual: IBSA embedded 42 staff ops-only visible vs IWEPS UAP 9.1m/60 staff full accounts",
        "src_dual_stats_ibsa_iweps_tick603",
        4,
        8.0,
        6,
        6.20,
        "FOI dual full TCO matrix",
    ),
    (
        "lb_ibsa_stats_887_2025",
        "IBSA 887 statistics diffused 2025 dual public stats mission",
        "Brussels",
        "ops",
        "Brussels>Stats>IBSA>stats_887",
        0,
        0,
        "Strong: 887 stats of which 34 new; output volume dual IWEPS mission class",
        "src_ibsa_ra_2025",
        2,
        5.0,
        2,
        3.50,
        "Output benchmark dual",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        lid, title, jur, cat, hpath, annual, stock, note, src, prio, scale, opac, pidx, hook = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"BCR policy Stats,Brussels public statistics,Core public stats dual opacity,"
            f"{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick603\n"
        )

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_ibsa_full_tco_l5_2025,Brussels>IBSA>full_TCO_L5_2025,ibsa,"
        "Full TCO IBSA 2024-25 incl Perspective personnel/comms/IT AB recon; multi-year; "
        "dual unit-cost vs IWEPS EUR/ETP; eng vs liq gap 2024 1.13 vs 0.52m,"
        "RA ops credits strong tick603; personnel residual parent opacity,5,"
        "IBSA / perspective.brussels / openbaarheid BCR,,https://ibsa.brussels,"
        "docs/doge/foi/drafts/gap_ibsa_full_tco_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_ibsa_ra_2025|cmt_dual_stats_ibsa_iweps_2025,"
        "lb_ibsa_liq_0_68m_2025|lb_dual_stats_ibsa_iweps_2025,"
        f"{utc},{utc},tick603 IBSA RA primary; residual full TCO human send\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_594,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:15:00Z,,Spawned tick602 after IWEPS dual stats; rq_116 deferred; progress@610 in 8"
)
new = (
    "rq_594,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:15:00Z,2026-07-31T16:30:00Z,"
    "tick603: IBSA ops 0.68m staff 42 dual IWEPS full TCO FOI; spawn rq_595; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_594 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_595,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:30:00Z,,Spawned tick603 after IBSA dual IWEPS; rq_116 deferred; progress@610 in 7\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_594,603,no,"
    "tick603 IBSA ops 0.68m staff 42 dual IWEPS; next rq_595; progress@610 in 7; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick603 CSV writes OK")
