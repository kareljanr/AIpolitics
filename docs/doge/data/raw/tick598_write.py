# tick 598 — CRA-W dual ILVO agri research hole-fill
from pathlib import Path
import json

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T15:15:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


# --- entities ---
with open(root / "entities.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "cra_w,CRA-W Centre wallon de Recherches agronomiques,"
        "CRA-W Centre wallon de Recherches agronomiques,"
        "Walloon Agricultural Research Centre dual ILVO Flanders,agency,wallonie_gov,fr,"
        "https://www.cra.wallonie.be,,,Gembloux; BCE 0262.172.984 Type1 UAP; "
        "budget ajust 2025 rec 53.417m dep 54.839m decret 9Jul2025; staff 454 Dec2025 sci 141; "
        "dual ILVO VO/EV agri research; tick598\n"
    )

# --- sources ---
with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_craw_budget_ajust_2025,Decret RW premier ajustement budget 2025 Art21 CRA-W,"
        "https://wallex.wallonie.be/eli/loi-decret/2025/07/09/2025006092,"
        "Parlement wallon / Wallex,2026-07-31,official_budget,"
        "Strong tick598 Art21: budget ajuste CRA-W 2025 recettes 53417000 EUR depenses 54839000 EUR; "
        "Type1 UAP BCE 0262172984; MB 22Aug2025\n"
    )
    f.write(
        "src_craw_ra_2025,CRA-W Rapport d activite 2025 RH key figures,"
        "https://www.cra.wallonie.be/uploads/2026/06/ra-cra-w-2025.pdf,"
        "CRA-W Wallonie,2026-07-31,official_annual_report,"
        "Strong tick598: effectif 454 agents 31Dec2025; scientifiques 141; nouveaux 34; "
        "statut 31pct statutaire 34pct CDI 33pct CDD 2pct remplacement; dual ILVO; raw cra_w_ra_2025.pdf\n"
    )
    f.write(
        "src_dual_agri_craw_ilvo_tick598,Dual agri research CRA-W WAL vs ILVO VL 2025,"
        "docs/doge/raw/cra_w_ra_2025.pdf,DOGE synthesis CRA-W budget+RA + ILVO CoA,"
        "2026-07-31,synthesis,"
        "Strong dual: CRA-W dep 54.8m staff 454 vs ILVO IVA 24.9m+EV 50.3m staff 756; "
        "regional agri research dual; tick598\n"
    )

# --- budgets ---
bud_rows = [
    ("bud_craw_recettes_2025", 53417000, "CRA-W budget ajuste 2025 recettes 53.417m decret Art21; tick598"),
    ("bud_craw_depenses_2025", 54839000, "CRA-W budget ajuste 2025 depenses 54.839m decret Art21; tick598"),
    ("bud_craw_staff_2025", 0, "CRA-W effectif 454 agents 31Dec2025 (not EUR); tick598"),
    ("bud_craw_scientifiques_2025", 0, "CRA-W agents scientifiques 141 Dec2025 (not EUR); tick598"),
    ("bud_craw_hires_2025", 0, "CRA-W nouveaux engages 34 en 2025 (not EUR); tick598"),
]
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, amt, note in bud_rows:
        src = "src_craw_ra_2025" if "staff" in bid or "scien" in bid or "hires" in bid else "src_craw_budget_ajust_2025"
        conf = "strong"
        f.write(f"{bid},cra_w,2025,{amt},,,outturn,{src},{conf},{note}\n")

# --- commitments ---
cmt_craw = {
    "2025_recettes": 53417000,
    "2025_depenses": 54839000,
    "2025_staff": 454,
    "2025_scientifiques": 141,
    "2025_hires": 34,
    "bce": "0262.172.984",
    "note": "WAL agri research dual ILVO; budget decret primary",
}
cmt_dual = {
    "craw_dep_m": 54.839,
    "craw_rec_m": 53.417,
    "craw_staff": 454,
    "ilvo_iva_exp_m": 24.9,
    "ilvo_ev_out_m": 50.3,
    "ilvo_staff": 756,
    "note": "Dual regional agri research CRA-W vs ILVO VO/EV stack",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_craw_budget_ra_2025,CRA-W agri research dual ILVO 2025,cra_w,'
        f'Wallonie farmers food industry EU,WAL decret budget + project finance,'
        f'2025-01-01,2025,2030,54839000,"{esc_json(cmt_craw)}",0,active,'
        f'https://www.cra.wallonie.be,Walloon agronomic research public,'
        f'Publish multi-year dotation L5 + full comptes FOI residual,'
        f'src_craw_budget_ajust_2025,strong,Wallonie>Agri_Research>CRA_W,tick598 budget+RA primary new entity\n'
    )
    f.write(
        f'cmt_dual_agri_craw_ilvo_2025,Dual agri research CRA-W WAL + ILVO VL 2025,gg_belgium,'
        f'Regional agri research dual,CRA-W budget2025 + ILVO CoA BO2025,'
        f'2024-01-01,2024,2025,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual regional agri research centres,FOI dual unit-cost + dotation L5,'
        f'src_dual_agri_craw_ilvo_tick598,strong,BE>dual>agri_CRAW_ILVO,tick598\n'
    )

# --- leaderboard ---
lb = [
    (
        "lb_craw_dep_55m_2025",
        "CRA-W depenses 54.8m recettes 53.4m budget ajust 2025 dual ILVO",
        "Wallonia",
        "ops",
        "Wallonie>Agri_Research>CRA_W>dep_55m",
        54839000,
        54839000,
        "Strong decret Art21: dep 54.839m rec 53.417m; staff 454 dual ILVO VO/EV",
        "src_craw_budget_ajust_2025",
        "WAL taxpayers SPW agri",
        "Public agronomic research",
        "Core public science not pure waste; dual regional",
        3,
        7.5,
        4,
        5.50,
        "Multi-year dotation FOI",
    ),
    (
        "lb_craw_rec_53m_2025",
        "CRA-W recettes 53.4m budget ajust 2025",
        "Wallonia",
        "ops",
        "Wallonie>Agri_Research>CRA_W>rec_53m",
        53417000,
        53417000,
        "Strong decret: recettes 53.417m vs dep 54.839m deficit path 1.4m",
        "src_craw_budget_ajust_2025",
        "WAL + EU projects",
        "Fund agri research centre",
        "Income mix L5 residual",
        3,
        7.0,
        4,
        5.05,
        "L5 income mix FOI",
    ),
    (
        "lb_craw_staff_454_2025",
        "CRA-W staff 454 scientifiques 141 2025 dual ILVO",
        "Wallonia",
        "ops",
        "Wallonie>Agri_Research>CRA_W>staff_454",
        0,
        0,
        "Strong RA2025: 454 agents 141 sci; dual ILVO 756 staff larger Flanders",
        "src_craw_ra_2025",
        "CRA-W staff",
        "Operate research Gembloux labs",
        "Core ops dual agri FTE",
        3,
        6.5,
        3,
        4.75,
        "Benchmark dual agri FTE",
    ),
    (
        "lb_craw_deficit_1_4m_2025",
        "CRA-W budget gap dep-rec 1.42m 2025",
        "Wallonia",
        "ops",
        "Wallonie>Agri_Research>CRA_W>budget_gap_1_4m",
        1422000,
        1422000,
        "Strong: dep 54.839 - rec 53.417 = 1.422m budget gap path; reserves residual FOI",
        "src_craw_budget_ajust_2025",
        "CRA-W",
        "Balance budget gap",
        "Small gap vs scale; stock residual",
        3,
        5.5,
        5,
        4.55,
        "FOI reserve drawdown",
    ),
    (
        "lb_dual_agri_craw_ilvo_2025",
        "Dual agri CRA-W 54.8m + ILVO IVA24.9+EV50.3m 2025",
        "multi",
        "ops",
        "BE>dual>agri_CRAW_ILVO_2025",
        54839000,
        75200000,
        "Strong dual: CRA-W WAL 54.8m/454 staff vs ILVO VL stack ~75m CoA arms/756 staff",
        "src_dual_agri_craw_ilvo_tick598",
        "Regional agri research dual",
        "Map dual regional agri centres",
        "VL dual VO/EV more complex than WAL single UAP",
        4,
        8.5,
        5,
        6.35,
        "FOI dual unit-cost matrix",
    ),
    (
        "lb_craw_statut_mix_2025",
        "CRA-W staff mix 31pct statutaire 34pct CDI 33pct CDD 2025",
        "Wallonia",
        "ops",
        "Wallonie>Agri_Research>CRA_W>statut_mix",
        0,
        0,
        "Strong RA2025 RH: high CDD share 33pct dual project funding path",
        "src_craw_ra_2025",
        "CRA-W HR",
        "Employment structure research centre",
        "Contract intensity dual project finance",
        3,
        5.5,
        4,
        4.40,
        "HR L5 residual",
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
            f"{spenders},{purpose},{mech},{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick598\n"
        )

# --- foi ---
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_craw_comptes_l5_2025,Wallonie>CRA_W>comptes_L5_2025,cra_w,"
        "Full comptes execution 2024-25 recon to budget 53.4/54.8m; multi-year WAL dotation L5; "
        "income mix GW SPW PRW UE; dual unit-cost vs ILVO VO/EV; annex budget tables,"
        "Decret budget+RA staff strong tick598; comptes residual,5,"
        "CRA-W / SPW Agriculture / openabilite wallonne,,https://www.cra.wallonie.be,"
        "docs/doge/foi/drafts/gap_craw_comptes_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_craw_budget_ra_2025|cmt_dual_agri_craw_ilvo_2025,"
        "lb_craw_dep_55m_2025|lb_dual_agri_craw_ilvo_2025,"
        f"{utc},{utc},tick598 CRA-W budget+RA primary; residual comptes human send\n"
    )

# --- research_queue ---
rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_589,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:00:00Z,,Spawned tick597 after ILVO dual agri; rq_116 deferred; progress@600 in 3"
)
new = (
    "rq_589,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:00:00Z,2026-07-31T15:15:00Z,"
    "tick598: CRA-W budget 53.4/54.8m staff 454 dual ILVO; spawn rq_590; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_589 row not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_590,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T15:15:00Z,,Spawned tick598 after CRA-W dual ILVO; rq_116 deferred; progress@600 in 2\n"
)
rq_path.write_text(text, encoding="utf-8")

# --- loop_state ---
(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_589,598,no,"
    "tick598 CRA-W budget 53.4/54.8m staff 454 dual ILVO; next rq_590; progress@600 in 2; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick598 CSV writes OK")
