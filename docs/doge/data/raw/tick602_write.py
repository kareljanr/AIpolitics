# tick 602 — IWEPS dual stats/eval hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T16:15:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "iweps,IWEPS Institut wallon Evaluation Prospective Statistique,"
        "IWEPS Institut wallon de l evaluation de la prospective et de la statistique,"
        "Walloon statistics evaluation institute dual Statbel IBSA,agency,wallonie_gov,fr,"
        "https://www.iweps.be,,,Type1 UAP BCE 0866.518.618; RA2024 rec 9.066m dep 11.394m "
        "(hors transfert 8.394m) personnel 6.836m; staff 60 ETP 58.3; dual multi-layer stats; "
        "budget ajust 2025 rec 9.288m dep 17.213m; tick602\n"
    )

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_iweps_ra_2024,IWEPS Rapport d activite 2024 rapport financier,"
        "https://www.iweps.be/wp-content/uploads/2025/06/IWEPS-RA2024.pdf,"
        "IWEPS Wallonie,2026-07-31,official_annual_report,"
        "Strong tick602: rec total 9066161; dot fonctionnement 7742k ODT 103k FWB 194k "
        "federal precompte 602k other sub 413k; dep total 11393569 personnel 6835839 "
        "services 909721 transfert tresorerie 3000000 inventaire 104832 missions 543177; "
        "hors transfert 8394k +9.67pct YoY; staff 60 ETP 58.3 research 41; raw iweps_ra_2024.pdf\n"
    )
    f.write(
        "src_iweps_budget_ajust_2025,Decret RW ajust budget 2025 Art22 IWEPS,"
        "https://wallex.wallonie.be/eli/loi-decret/2025/07/09/2025006092,"
        "Parlement wallon / Wallex,2026-07-31,official_budget,"
        "Strong tick602 Art22: budget ajuste IWEPS 2025 recettes 9288000 depenses 17213000 EUR\n"
    )
    f.write(
        "src_dual_stats_iweps_tick602,Dual multi-layer stats IWEPS WAL vs Statbel IBSA,"
        "docs/doge/raw/iweps_ra_2024.pdf,DOGE synthesis IWEPS RA2024 dual stats,"
        "2026-07-31,synthesis,"
        "Strong dual: IWEPS WAL statistical authority rec 9.1m staff 60 dual federal Statbel "
        "+ IBSA Brussels + FWB synergy 194k; multi-layer stats overhead; tick602\n"
    )

bud_rows = [
    ("bud_iweps_recettes_2024", "iweps", 2024, 9066161, "IWEPS total recettes realisees 9.066m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_dot_fonct_2024", "iweps", 2024, 7742000, "IWEPS dotation fonctionnement 7.742m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_odt_2024", "iweps", 2024, 103000, "IWEPS Observatoire developpement territorial 0.103m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_fwb_2024", "iweps", 2024, 194000, "IWEPS FWB synergies statistiques 2 salaries 0.194m 2024 dual; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_precompte_fed_2024", "iweps", 2024, 602000, "IWEPS federal precompte exemption research 0.602m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_other_sub_2024", "iweps", 2024, 413000, "IWEPS other specific ministerial subsidies 0.413m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_depenses_2024", "iweps", 2024, 11393569, "IWEPS total depenses 11.394m 2024 incl tresorerie transfer; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_dep_hors_transfert_2024", "iweps", 2024, 8394000, "IWEPS depenses hors transfert tresorerie 8.394m 2024 (+9.67pct); tick602", "src_iweps_ra_2024"),
    ("bud_iweps_personnel_2024", "iweps", 2024, 6835839, "IWEPS personnel direct cost 6.836m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_services_2024", "iweps", 2024, 909721, "IWEPS services biens divers 0.910m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_transfert_tres_2024", "iweps", 2024, 3000000, "IWEPS transfert revenus pouvoir institutionnel tresorerie 3.0m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_inventaire_2024", "iweps", 2024, 104832, "IWEPS biens inventaire invest 0.105m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_missions_2024", "iweps", 2024, 543177, "IWEPS missions decretale 0.543m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_fonct_total_2024", "iweps", 2024, 10850392, "IWEPS depenses fonctionnement total 10.850m 2024; tick602", "src_iweps_ra_2024"),
    ("bud_iweps_staff_2024", "iweps", 2024, 0, "IWEPS staff 60 persons ETP 58.3 31Dec2024 (not EUR); tick602", "src_iweps_ra_2024"),
    ("bud_iweps_research_staff_2024", "iweps", 2024, 0, "IWEPS research staff 41 of 60 2024 (not EUR); tick602", "src_iweps_ra_2024"),
    ("bud_iweps_recettes_2025b", "iweps", 2025, 9288000, "IWEPS budget ajuste 2025 recettes 9.288m decret Art22; tick602", "src_iweps_budget_ajust_2025"),
    ("bud_iweps_depenses_2025b", "iweps", 2025, 17213000, "IWEPS budget ajuste 2025 depenses 17.213m decret Art22; tick602", "src_iweps_budget_ajust_2025"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, ent, year, amt, note, src in bud_rows:
        f.write(f"{bid},{ent},{year},{amt},,,outturn,{src},strong,{note}\n")

cmt = {
    "2024_recettes": 9066161,
    "2024_depenses": 11393569,
    "2024_hors_transfert": 8394000,
    "2024_dot_fonct": 7742000,
    "2024_personnel": 6835839,
    "2024_transfert_tresorerie": 3000000,
    "staff": 60,
    "etp": 58.3,
    "research_staff": 41,
    "2025b_rec": 9288000,
    "2025b_dep": 17213000,
    "note": "WAL stats authority dual multi-layer; tresorerie transfer inflates dep total",
}
cmt_dual = {
    "iweps_rec_m": 9.066,
    "iweps_dep_hors_m": 8.394,
    "iweps_staff": 60,
    "fwb_synergy_k": 194,
    "note": "Dual multi-layer stats IWEPS WAL vs Statbel federal / IBSA Brussels",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_iweps_ra_2024,IWEPS dual stats evaluation WAL 2024-25,iweps,'
        f'Wallonie government policy Stats,WAL dotation + FWB + federal precompte + missions,'
        f'2024-01-01,2024,2030,9066161,"{esc_json(cmt)}",0,active,'
        f'https://www.iweps.be,Regional statistics evaluation prospective,'
        f'Publish 2025 outturn recon + multi-year FOI,'
        f'src_iweps_ra_2024,strong,Wallonie>Stats_Eval>IWEPS,tick602 RA2024 primary new entity\n'
    )
    f.write(
        f'cmt_dual_stats_iweps_2024,Dual multi-layer stats IWEPS WAL 2024,gg_belgium,'
        f'Belgian multi-layer statistical system,IWEPS RA2024 dual Statbel IBSA class,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual multi-layer regional stats institutes,FOI dual unit-cost stats layer,'
        f'src_dual_stats_iweps_tick602,strong,BE>dual>stats_IWEPS,tick602\n'
    )

lb = [
    (
        "lb_iweps_rec_9m_2024",
        "IWEPS recettes 9.1m depenses 11.4m 2024 dual stats",
        "Wallonia",
        "ops",
        "Wallonie>Stats_Eval>IWEPS>rec_9m",
        9066161,
        11393569,
        "Strong RA2024: rec 9.066m dep 11.394m of which tresorerie transfer 3.0m; hors transfer 8.394m; dual multi-layer stats",
        "src_iweps_ra_2024",
        3,
        7.0,
        4,
        5.05,
        "2025 outturn FOI",
    ),
    (
        "lb_iweps_dot_7_7m_2024",
        "IWEPS dotation fonctionnement 7.7m 2024",
        "Wallonia",
        "ops",
        "Wallonie>Stats_Eval>IWEPS>dot_7_7m",
        7742000,
        7742000,
        "Strong: structural WAL dot 7.742m covers 98.62pct personnel on fonct budget",
        "src_iweps_ra_2024",
        4,
        6.5,
        3,
        5.05,
        "Multi-year dot FOI",
    ),
    (
        "lb_iweps_personnel_6_8m_2024",
        "IWEPS personnel 6.8m staff 60 ETP 58.3 2024",
        "Wallonia",
        "ops",
        "Wallonie>Stats_Eval>IWEPS>personnel_6_8m",
        6835839,
        6835839,
        "Strong: personnel 6.836m; 60 staff 58.3 ETP of which 41 research; cadre 69",
        "src_iweps_ra_2024",
        3,
        6.5,
        3,
        4.75,
        "Benchmark dual stats FTE",
    ),
    (
        "lb_iweps_transfert_3m_2024",
        "IWEPS tresorerie transfer 3.0m to WAL institutional 2024",
        "Wallonia",
        "ops",
        "Wallonie>Stats_Eval>IWEPS>transfert_3m",
        3000000,
        3000000,
        "Strong: rapatriement tresorerie 3.0m inflates dep total vs ops 8.4m; governance opacity",
        "src_iweps_ra_2024",
        4,
        6.0,
        5,
        5.05,
        "FOI transfer policy",
    ),
    (
        "lb_iweps_budget_17m_2025",
        "IWEPS budget ajuste dep 17.2m rec 9.3m 2025",
        "Wallonia",
        "ops",
        "Wallonie>Stats_Eval>IWEPS>budget_17m_2025",
        17213000,
        17213000,
        "Strong decret Art22: 2025b dep 17.213m rec 9.288m; large gap vs 2024 outturn FOI residual",
        "src_iweps_budget_ajust_2025",
        4,
        7.0,
        5,
        5.55,
        "Perimeter recon FOI",
    ),
    (
        "lb_dual_stats_iweps_2024",
        "Dual multi-layer stats IWEPS 9.1m + FWB synergy dual Statbel class",
        "multi",
        "ops",
        "BE>dual>stats_IWEPS_2024",
        9066161,
        9066161,
        "Strong dual: WAL IWEPS statistical authority dual federal Statbel + IBSA + FWB 194k",
        "src_dual_stats_iweps_tick602",
        4,
        7.5,
        5,
        5.85,
        "FOI dual stats matrix",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        lid, title, jur, cat, hpath, annual, stock, note, src, prio, scale, opac, pidx, hook = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"WAL policy Stats,Regional statistics evaluation,Core public stats dual layers,"
            f"{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick602\n"
        )

with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_iweps_2025_outturn_l5,Wallonie>IWEPS>outturn_L5_2025,iweps,"
        "2025 execution recon to budget 9.3/17.2m vs 2024 outturn 9.1/11.4m; multi-year dotation; "
        "tresorerie transfer policy; dual unit-cost vs IBSA Statbel; missions decretale L5,"
        "RA2024 + decret 2025b strong tick602; 2025 outturn residual,5,"
        "IWEPS / SPW / openabilite wallonne,,https://www.iweps.be,"
        "docs/doge/foi/drafts/gap_iweps_2025_outturn_l5.md,ready,2026-07-31,,,,"
        "cmt_iweps_ra_2024|cmt_dual_stats_iweps_2024,"
        "lb_iweps_rec_9m_2024|lb_dual_stats_iweps_2024,"
        f"{utc},{utc},tick602 IWEPS RA+decret primary; residual 2025 outturn human send\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_593,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:00:00Z,,Spawned tick601 after Meise dual VL/FWB; rq_116 deferred; progress@610 in 9"
)
new = (
    "rq_593,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:00:00Z,2026-07-31T16:15:00Z,"
    "tick602: IWEPS rec 9.1m dep 11.4m staff 60 dual stats; spawn rq_594; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_593 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_594,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:15:00Z,,Spawned tick602 after IWEPS dual stats; rq_116 deferred; progress@610 in 8\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_593,602,no,"
    "tick602 IWEPS rec 9.1m dep 11.4m dual stats; next rq_594; progress@610 in 8; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick602 CSV writes OK")
