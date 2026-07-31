# tick377: Iriscare RA2024 institutional outturn L5 dual BRU AF/care
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

# --- entities ---
ent_rows = [
    "famiris,Famiris caisse publique allocations familiales Bruxelles,Famiris caisse publique AF Bruxelles,Brussels public family benefits payment caisse under Iriscare,agency,iriscare,bi,https://www.famiris.brussels,,,Public AF channel 427m 2024; 122524 children; tick377",
    "vivalis,Vivalis administration COCOM Bruxelles,Vivalis administration COCOM,Brussels bicommunal administration funding Iriscare dots,agency,cocom,bi,https://www.vivalis.brussels,,,Dot Iriscare missions+fonct 1660.923m 2024; tick377",
]
with (DATA / "entities.csv").open("a", encoding="utf-8", newline="") as f:
    for r in ent_rows:
        f.write(r + "\n")
print("entities +", len(ent_rows))

# --- sources ---
src_row = (
    "src_iriscare_ra_2024,"
    "Iriscare Rapport annuel 2024 budget depenses recettes L5,"
    "https://rapport.iriscare.brussels/wp-content/uploads/2025/09/Rapport-annuel-2024.pdf,"
    "Iriscare OIP COCOM,"
    "2026-08-01,primary_annual_report,"
    '"RA2024 p5-6: dep 1732.255m rec 1727.883m AF 1055.302 MR forfait 345.969 APA 35.386 Vivalis dot 1660.923; Famiris 427m; dual VL/WAL AF"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src_row + "\n")
print("sources +1")

# --- budgets ---
budgets = [
    ("bud_iriscare_dep_2024", "iriscare", 2024, 1732255421, "outturn", "Iriscare total depenses 2024 1732.25542087m RA p5"),
    ("bud_iriscare_rec_2024", "iriscare", 2024, 1727882763, "outturn", "Iriscare total recettes 2024 1727.88276322m"),
    ("bud_iriscare_af_2024", "iriscare", 2024, 1055302130, "outturn", "Allocations familiales depenses 1055.30213047m largest line"),
    ("bud_iriscare_mr_forfait_2024", "iriscare", 2024, 345969453, "outturn", "Forfait maisons de repos 345.96945325m sante"),
    ("bud_iriscare_apa_2024", "iriscare", 2024, 35386308, "outturn", "APA aide personnes agees 35.38630838m"),
    ("bud_iriscare_vivalis_dot_2024", "iriscare", 2024, 1660923000, "outturn", "Dotation Vivalis missions+fonctionnement 1660.923m"),
    ("bud_iriscare_af_recoveries_2024", "iriscare", 2024, 51548817, "outturn", "Allocations familiales a recuperer 51.54881693m"),
    ("bud_iriscare_anm_recoveries_2024", "iriscare", 2024, 2972283, "outturn", "Recuperations Accords non marchand 2.97228250m"),
    ("bud_iriscare_placement_income_2024", "iriscare", 2024, 1043234, "outturn", "Revenus de placements 1.04323446m"),
    ("bud_iriscare_restaurant_2024", "iriscare", 2024, 23172, "outturn", "Restaurant d entreprise 23171.73 EUR"),
    ("bud_iriscare_location_2024", "iriscare", 2024, 120470, "outturn", "Locations locaux 120470.15 EUR"),
    ("bud_famiris_af_2024", "famiris", 2024, 427000000, "outturn", "Famiris public caisse AF paid 427m to 122524 children 65117 families"),
    ("bud_iriscare_af_private_channel_class_2024", "iriscare", 2024, 628302130, "outturn", "Implied residual AF outside Famiris 1055.302-427=628.302m private caisses class medium calc"),
    ("bud_be_af_triple_outturn_class", "gg_belgium", 2024, 0, "synthesis", "Dual AF class: VL GP awards~4.7bn 2025 + WAL 3.01bn 2026 + Iriscare AF 1.055bn 2024; years differ not TE-additive; Iriscare headcount 363"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, eid, yr, amt, basis, notes in budgets:
        conf = "medium" if ("class" in bid or "Implied" in notes or basis == "synthesis") else "strong"
        f.write(
            f'{bid},{eid},{yr},{amt},,,,{basis},src_iriscare_ra_2024,{conf},"{notes}"\n'
        )
print("budgets +", len(budgets))

# --- commitments ---
cmt = (
    "cmt_iriscare_outturn_2024,Iriscare institutional outturn 2024 dual VL/WAL AF care,iriscare,"
    "Brussels families elderly MR residents APA handicap via OAs,"
    "Ordonnance Iriscare / COCOM transferred competences,"
    "2024-01-01,2024,2024,1732255421,"
    '"{""dep_m"":1732.255,""rec_m"":1727.883,""vivalis_dot_m"":1660.923,'
    '""af_m"":1055.302,""mr_forfait_m"":345.969,""apa_m"":35.386,'
    '""af_recoveries_m"":51.549,""anm_recoveries_m"":2.972,""placement_m"":1.043,'
    '""famiris_af_m"":427,""famiris_children"":122524,""famiris_families"":65117,'
    '""headcount"":363,""dual_vl_gp_ise_2025_m"":4906.672,""dual_wal_af_2026_m"":3013.486,'
    '""budget_2026_m"":1826.39,""note"":""Strong RA2024; residual private AF caisse L5 + MR institution L5 FOI; '
    'stats site public partial""}",'
    "0,active,https://rapport.iriscare.brussels/wp-content/uploads/2025/09/Rapport-annuel-2024.pdf,"
    "Bicommunal family benefits elderly care APA disability aids Brussels,"
    "Publish private AF channel L5; MR top operators; payroll; dual unit-cost VL/WAL,"
    "src_iriscare_ra_2024,strong,Bruxelles>COCOM>Iriscare>outturn_2024,"
    "tick377: dep 1.732bn AF 1.055bn MR 346m Famiris 427m\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("commitments +1")

# --- leaderboard ---
lbs = [
    (
        "lb_iriscare_dep_1_73bn_2024",
        "Iriscare total expenditure 1.732bn 2024",
        "Brussels",
        "ops",
        "Bruxelles>COCOM>Iriscare>total",
        1732255421,
        1732255421,
        "Strong RA2024: dep 1732.255m rec 1727.883m; Vivalis dot 1660.923m; dual 2026 budget 1826m path",
        "strong",
        "src_iriscare_ra_2024",
        "Brussels families elderly disability residents",
        "Bicommunal health and family benefits delivery",
        "Core social mega dual VL/WAL; not pure waste; L5 residual institutions",
        2,
        9.0,
        4,
        6.28,
        "Publish full L5 matrix stats site export; dual unit-cost",
        "seed",
        "",
        "tick377",
    ),
    (
        "lb_iriscare_af_1_06bn_2024",
        "Iriscare allocations familiales 1.055bn 2024",
        "Brussels",
        "transfer",
        "Bruxelles>COCOM>Iriscare>AF",
        1055302130,
        1055302130,
        "Strong: AF 1055.302m; Famiris public 427m; residual private caisses ~628m class; dual VL GP 4.91bn WAL 3.01bn",
        "strong",
        "src_iriscare_ra_2024",
        "Brussels children families 300k+ class",
        "Universal family benefits Brussels",
        "Core entitlement dual multi-caisse; per-private L5 residual",
        3,
        8.5,
        4,
        6.18,
        "Open private caisse EUR matrix; dual unit-cost VL/WAL",
        "seed",
        "",
        "tick377",
    ),
    (
        "lb_famiris_af_427m_2024",
        "Famiris public AF channel 427m 2024",
        "Brussels",
        "transfer",
        "Bruxelles>Iriscare>Famiris",
        427000000,
        427000000,
        "Strong: 427m to 122524 children 65117 families 841265 payments; ~40pct of Iriscare AF",
        "strong",
        "src_iriscare_ra_2024",
        "Public-channel Brussels families",
        "Public family benefits payment organism",
        "Dual Fons/VUTG VL and Famiwal WAL public channels",
        3,
        7.5,
        3,
        5.68,
        "Publish unit cost vs private caisses; admin envelope",
        "seed",
        "",
        "tick377",
    ),
    (
        "lb_iriscare_mr_forfait_346m_2024",
        "Iriscare nursing home forfait 346.0m 2024",
        "Brussels",
        "ops",
        "Bruxelles>Iriscare>MR_forfait",
        345969453,
        345969453,
        "Strong: forfait maisons de repos 345.969m; dual 2026 budget 353.7m; dual VL VSB ROZ",
        "strong",
        "src_iriscare_ra_2024",
        "Brussels nursing home residents",
        "Institutional elderly care financing forfait",
        "Core care; per-MR L5 residual FOI; dual VSB WZC",
        3,
        7.5,
        4,
        5.78,
        "Open top MR operators EUR; dual unit-cost VSB",
        "seed",
        "",
        "tick377",
    ),
    (
        "lb_iriscare_apa_35m_2024",
        "Iriscare APA elderly aid 35.4m 2024",
        "Brussels",
        "transfer",
        "Bruxelles>Iriscare>APA",
        35386308,
        35386308,
        "Strong: APA 35.386m; 8596 active dossiers; 4498 demandes; dual VL zorgbudget path",
        "strong",
        "src_iriscare_ra_2024",
        "Brussels elderly 65+ low income autonomy loss",
        "Means-tested elderly care allowance",
        "Core social small vs AF/MR",
        2,
        5.5,
        3,
        4.18,
        "Publish multi-year path vs COCOM budget AAPA",
        "seed",
        "",
        "tick377",
    ),
    (
        "lb_iriscare_vivalis_dot_1_66bn_2024",
        "Vivalis dotation to Iriscare 1.661bn 2024",
        "Brussels",
        "transfer",
        "Bruxelles>COCOM>Vivalis>Iriscare_dot",
        1660923000,
        1660923000,
        "Strong: Vivalis missions+fonct dot 1660.923m of 1727.883m receipts (~96pct)",
        "strong",
        "src_iriscare_ra_2024",
        "Iriscare as delivery OIP",
        "Primary financing path bicommunal",
        "Core transfer; dual SCR 2026 M05 path",
        2,
        9.0,
        3,
        6.13,
        "Reconcile multi-year SCR M05 dots vs RA outturn",
        "seed",
        "",
        "tick377",
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
print("leaderboard +", len(lbs))

# --- research queue ---
rq_path = DATA / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    "rq_368,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T02:45:00Z,,Spawned tick376 after Beleid+Zorginfra; rq_116 SWA deferred"
)
new = (
    "rq_368,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_iriscare_l5_2024,2026-08-01T02:45:00Z,2026-08-01T03:15:00Z,"
    "tick377: Iriscare RA2024 dep 1.732bn AF 1.055 MR 346 Famiris 427; FOI residual; spawn rq_369"
)
if old not in text:
    raise SystemExit("rq_368 not found")
rq_path.write_text(text.replace(old, new), encoding="utf-8")
with rq_path.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_369,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T03:15:00Z,,Spawned tick377 after Iriscare RA2024; rq_116 SWA deferred\n"
    )
print("rq_368 done + rq_369")

# --- foi ---
foi_row = (
    "gap_iriscare_l5_2024,Bruxelles>COCOM>Iriscare>L5_2024,iriscare,"
    "Machine-readable full L5: private AF caisses EUR under residual ~628m of AF 1.055bn; top MR "
    "operators under forfait 346m; payroll/fonctionnement split of residual dep; APA multi-year; "
    "stats-site export 2023-2026; reconcile Vivalis/SCR M05 dots,"
    "RA2024 aggregates strong; end-receiver and private caisse L5 residual,6,"
    "Iriscare / Vivalis / COCOM transparence,transparence@sprb.brussels,,"
    "docs/doge/foi/drafts/gap_iriscare_l5_2024.md,ready,2026-08-01,,,,,"
    "cmt_iriscare_outturn_2024,lb_iriscare_dep_1_73bn_2024|lb_iriscare_af_1_06bn_2024,"
    "2026-08-01T03:15:00Z,2026-08-01T03:15:00Z,"
    "tick377 draft ready human send only; dual VL GP + WAL AF"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi_row + "\n")
print("foi +1")

# --- loop_state ---
(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T03:15:00Z,rq_368,377,no,"
    "Scheduler 60s. Next prio5 rq_369; rq_116 SWA deferred. FOI ready. tick377 Iriscare 1.73bn AF 1.06bn.\n",
    encoding="utf-8",
)
print("loop_state 377 OK")
