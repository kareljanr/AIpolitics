# tick 604 — AWaP dual OE heritage hole-fill deepen
from pathlib import Path
import json
import re

root = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
utc = "2026-07-31T16:45:00Z"


def esc_json(d):
    return json.dumps(d, separators=(",", ":")).replace('"', '""')


# update entity awap line
ent = (root / "entities.csv").read_text(encoding="utf-8")
old_ent = (
    "awap,Agence wallonne du Patrimoine AWaP,Agence wallonne du Patrimoine,"
    "Walloon Heritage Agency dual Flanders OE,agency,wallonie_gov,fr,"
    "https://agencewallonnedupatrimoine.be,,,Dual OE Flanders; budget total residual FOI; tick349"
)
new_ent = (
    "awap,Agence wallonne du Patrimoine AWaP,Agence wallonne du Patrimoine,"
    "Walloon Heritage Agency dual Flanders OE,agency,wallonie_gov,fr,"
    "https://agencewallonnedupatrimoine.be,,,SACA; staff 312; eng 46.076m liq 49.135m 2025; "
    "subs eng 31.314m 68pct; RW subvention 49.5m own ~0.7m; dual OE VL VEK 127.8m; tick604"
)
if old_ent not in ent:
    # try partial replace notes only
    if "awap,Agence wallonne" in ent and "tick349" in ent:
        ent = ent.replace(
            "Dual OE Flanders; budget total residual FOI; tick349",
            "SACA; staff 312; eng 46.076m liq 49.135m 2025; subs eng 31.314m; RW 49.5m; dual OE; tick604",
        )
    else:
        raise SystemExit("awap entity not found for update")
else:
    ent = ent.replace(old_ent, new_ent)
(root / "entities.csv").write_text(ent, encoding="utf-8")

with open(root / "sources.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "src_awap_ra_2025,AWaP Rapport d activites 2025 moyens humains financiers,"
        "https://agencewallonnedupatrimoine.be/wp-content/uploads/2026/05/B-DEF_RA2025_AWaP_vf.pdf,"
        "AWaP Wallonie,2026-07-31,official_annual_report,"
        "Strong tick604: staff 312; eng 46075932.64 liq 49134500.36; subs eng 31313974.38 68pct; "
        "RW subvention 49.5m own under 0.7m; missions 91pct admin 7pct PRW 2pct; "
        "public mon 14.1m cadres 5.9m private 4m regional props 3m; 176 dossiers; raw awap_ra_2025.pdf\n"
    )
    f.write(
        "src_awap_budget_ajust_2025,Decret RW ajust budget 2025 Art16 AWaP,"
        "https://wallex.wallonie.be/eli/loi-decret/2025/07/09/2025006092,"
        "Parlement wallon / Wallex,2026-07-31,official_budget,"
        "Strong tick604 Art16: budget ajuste AWaP 2025 recettes 51624000 depenses 52246000 EUR\n"
    )
    f.write(
        "src_dual_heritage_awap_oe_tick604,Dual heritage AWaP WAL + OE Flanders 2025-26,"
        "docs/doge/raw/awap_ra_2025.pdf,DOGE synthesis AWaP RA2025 + OE BO2026,"
        "2026-07-31,synthesis,"
        "Strong dual: AWaP liq 49.1m staff 312 vs OE VEK 127.8m VAK 121.8m; heritage dual scale; tick604\n"
    )

bud_rows = [
    ("bud_awap_eng_2025", 46075933, "AWaP total engagé 46.075933m 2025 RA; tick604"),
    ("bud_awap_liq_2025", 49134500, "AWaP total liquidé 49.134500m 2025 RA; tick604"),
    ("bud_awap_subs_eng_2025", 31313974, "AWaP subventions octroyées eng 31.313974m 68pct 2025; tick604"),
    ("bud_awap_rw_subvention_2025", 49500000, "AWaP RW annual subvention 49.5m 2025 RA text; tick604"),
    ("bud_awap_own_income_2025", 700000, "AWaP own activities under 0.7m 2025 RA approx; tick604"),
    ("bud_awap_subs_public_2025", 14100000, "AWaP subs public sector monuments 14.1m 2025; tick604"),
    ("bud_awap_subs_cadres_2025", 5900000, "AWaP accords-cadres pluriannuels 5.9m 2025; tick604"),
    ("bud_awap_subs_private_2025", 4000000, "AWaP subs private classified owners 4.0m 2025; tick604"),
    ("bud_awap_subs_regional_props_2025", 3000000, "AWaP regional properties direct works 3.0m 2025; tick604"),
    ("bud_awap_recettes_2025b", 51624000, "AWaP budget ajuste 2025 recettes 51.624m decret Art16; tick604"),
    ("bud_awap_depenses_2025b", 52246000, "AWaP budget ajuste 2025 depenses 52.246m decret Art16; tick604"),
    ("bud_awap_staff_2025", 0, "AWaP staff 312 agents 2025 (not EUR); tick604"),
    ("bud_awap_dossiers_2025", 0, "AWaP 176 dossiers travaux soutenus 2025 (not EUR); tick604"),
]
# conf for own income medium (approx under 700k)
with open(root / "budgets.csv", "a", encoding="utf-8", newline="") as f:
    for bid, amt, note in bud_rows:
        conf = "medium" if "own_income" in bid else "strong"
        src = "src_awap_budget_ajust_2025" if "2025b" in bid else "src_awap_ra_2025"
        f.write(f"{bid},awap,2025,{amt},,,outturn,{src},{conf},{note}\n")

cmt = {
    "2025_eng": 46075933,
    "2025_liq": 49134500,
    "2025_subs_eng": 31313974,
    "2025_rw_subvention": 49500000,
    "staff": 312,
    "dossiers": 176,
    "2025b_rec": 51624000,
    "2025b_dep": 52246000,
    "note": "SACA heritage dual OE Flanders; 68pct grants",
}
cmt_dual = {
    "awap_liq_m": 49.135,
    "awap_subs_m": 31.314,
    "awap_staff": 312,
    "oe_vek_2026_m": 127.789,
    "oe_vak_2026_m": 121.823,
    "note": "Dual heritage AWaP WAL ~49m vs OE Flanders VEK 128m",
}
with open(root / "commitments.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        f'cmt_awap_ra_2025,AWaP heritage dual OE 2025,awap,'
        f'Wallonie owners communes fabriques,RW subvention + own + grants out,'
        f'2025-01-01,2025,2030,49134500,"{esc_json(cmt)}",0,active,'
        f'https://agencewallonnedupatrimoine.be,Protect restore Walloon heritage,'
        f'Publish L5 top awards dual OE FOI residual,'
        f'src_awap_ra_2025,strong,Wallonie>Heritage>AWaP,tick604 RA2025 primary deepen\n'
    )
    f.write(
        f'cmt_dual_heritage_awap_oe_2025,Dual heritage AWaP WAL + OE Flanders 2025-26,gg_belgium,'
        f'Regional heritage dual,AWaP RA2025 + OE BO2026,'
        f'2025-01-01,2025,2026,0,"{esc_json(cmt_dual)}",0,active,,'
        f'Map dual regional heritage agencies,FOI dual L5 awards matrix,'
        f'src_dual_heritage_awap_oe_tick604,strong,BE>dual>heritage_AWaP_OE,tick604\n'
    )

lb = [
    (
        "lb_awap_liq_49m_2025",
        "AWaP liquidé 49.1m engagé 46.1m 2025 dual OE",
        "Wallonia",
        "ops",
        "Wallonie>Heritage>AWaP>liq_49m",
        49134500,
        49134500,
        "Strong RA2025: liq 49.135m eng 46.076m; RW sub 49.5m; staff 312 dual OE VL 128m",
        "src_awap_ra_2025",
        3,
        7.5,
        4,
        5.50,
        "L5 awards FOI residual",
    ),
    (
        "lb_awap_subs_31m_2025",
        "AWaP subventions 31.3m eng 68pct 2025",
        "Wallonia",
        "ops",
        "Wallonie>Heritage>AWaP>subs_31m",
        31313974,
        31313974,
        "Strong: grants eng 31.314m 68pct budget; public 14.1m cadres 5.9m private 4m regional 3m",
        "src_awap_ra_2025",
        4,
        7.5,
        4,
        5.60,
        "Named top awards FOI",
    ),
    (
        "lb_awap_rw_sub_49_5m_2025",
        "AWaP RW subvention 49.5m 2025",
        "Wallonia",
        "ops",
        "Wallonie>Heritage>AWaP>rw_sub_49_5m",
        49500000,
        49500000,
        "Strong RA: structural RW annual subvention 49.5m core; own under 0.7m",
        "src_awap_ra_2025",
        4,
        7.5,
        3,
        5.65,
        "Multi-year sub FOI",
    ),
    (
        "lb_awap_staff_312_2025",
        "AWaP staff 312 agents 2025 dual OE",
        "Wallonia",
        "ops",
        "Wallonie>Heritage>AWaP>staff_312",
        0,
        0,
        "Strong: 312 agents SACA dual Flanders OE larger package",
        "src_awap_ra_2025",
        3,
        6.5,
        3,
        4.75,
        "Benchmark dual heritage FTE",
    ),
    (
        "lb_awap_budget_52m_2025b",
        "AWaP budget ajuste dep 52.2m rec 51.6m 2025",
        "Wallonia",
        "ops",
        "Wallonie>Heritage>AWaP>budget_52m_2025b",
        52246000,
        52246000,
        "Strong decret Art16: 2025b dep 52.246m rec 51.624m vs RA liq 49.1m",
        "src_awap_budget_ajust_2025",
        3,
        7.5,
        4,
        5.50,
        "Budget vs outturn recon",
    ),
    (
        "lb_dual_heritage_awap_oe_2025",
        "Dual heritage AWaP 49m + OE VEK 128m 2025-26",
        "multi",
        "ops",
        "BE>dual>heritage_AWaP_OE_2025",
        49134500,
        127789000,
        "Strong dual: AWaP WAL liq 49.1m/312 staff vs OE Flanders VEK 127.8m VAK 121.8m",
        "src_dual_heritage_awap_oe_tick604",
        4,
        8.5,
        5,
        6.35,
        "FOI dual L5 awards matrix",
    ),
]
with open(root / "leaderboard.csv", "a", encoding="utf-8", newline="") as f:
    for r in lb:
        lid, title, jur, cat, hpath, annual, stock, note, src, prio, scale, opac, pidx, hook = r
        f.write(
            f"{lid},{title},{jur},{cat},{hpath},{annual},{stock},{note},strong,{src},"
            f"WAL heritage owners,Protect restore heritage,Core public heritage dual,"
            f"{prio},{scale},{opac},{pidx:.2f},{hook},seed,,tick604\n"
        )

# FOI - deepen named L5 residual (gap_oe_awap already exists ready - add execution gap)
with open(root / "foi_queue.csv", "a", encoding="utf-8", newline="") as f:
    f.write(
        "gap_awap_subs_l5_2025,Wallonie>AWaP>subventions_L5_2025,awap,"
        "Named top30 subventions 2025 recon to 31.314m eng; multi-year Thermes Spa 8.5m Arlon 7.9m; "
        "dual unit-cost vs OE premies; final comptes vs liq 49.1m,"
        "RA2025 eng/liq/subs strong tick604; named L5 residual,5,"
        "AWaP / SPW / openabilite wallonne,,https://agencewallonnedupatrimoine.be,"
        "docs/doge/foi/drafts/gap_awap_subs_l5_2025.md,ready,2026-07-31,,,,"
        "cmt_awap_ra_2025|cmt_dual_heritage_awap_oe_2025,"
        "lb_awap_subs_31m_2025|lb_dual_heritage_awap_oe_2025,"
        f"{utc},{utc},tick604 AWaP RA2025 primary; residual named awards human send\n"
    )

rq_path = root / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_595,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:30:00Z,,Spawned tick603 after IBSA dual IWEPS; rq_116 deferred; progress@610 in 7"
)
new = (
    "rq_595,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:30:00Z,2026-07-31T16:45:00Z,"
    "tick604: AWaP liq 49.1m subs 31.3m staff 312 dual OE; spawn rq_596; rq_116 deferred"
)
if old not in text:
    raise SystemExit("rq_595 not found")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += (
    "rq_596,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
    "2026-07-31T16:45:00Z,,Spawned tick604 after AWaP dual OE; rq_116 deferred; progress@610 in 6\n"
)
rq_path.write_text(text, encoding="utf-8")

(root / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{utc},rq_595,604,no,"
    "tick604 AWaP liq 49.1m subs 31.3m dual OE; next rq_596; progress@610 in 6; rq_116 deferred\n",
    encoding="utf-8",
)

print("tick604 CSV writes OK")
