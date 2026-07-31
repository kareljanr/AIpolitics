# tick383: INAMI/RIZIV budget sante 2025 full matrix + correction L5
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
    "src_inami_budget_sante_2025_matrix,"
    "INAMI Budget soins de sante 2025 Conseil des ministres recettes depenses corrections L5,"
    "docs/doge/data/raw/inami_budget_sante_2025.pdf,"
    "INAMI / Conseil des ministres,"
    "2026-08-01,primary_budget,"
    '"CM decision 2025: total 45221.741m; prestations 39812.150m; beheer 1188.516m; corrections 216.802m; dual mutual admin"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")
print("sources +1")

# amounts in document are thousands EUR
rows = [
    # totals
    ("bud_riziv_rec_total_2025", "riziv", 2025, 45221741, "budgeted", "Total recettes assurance soins sante 2025 45221.741m"),
    ("bud_riziv_exp_total_2025", "riziv", 2025, 45221741, "budgeted", "Total depenses 45221.741m; primary result 0"),
    ("bud_riziv_prestation_2025", "riziv_care", 2025, 39812150, "budgeted", "Prestations objectif 39812.150m (+1987.440m / +5.25pct)"),
    ("bud_riziv_prestation_authorized_2025", "riziv_care", 2025, 39692495, "budgeted", "Depenses autorisees 39692.495m after non-affectable 119.655m"),
    ("bud_riziv_beheer_2025", "riziv", 2025, 1188516, "budgeted", "Couts de gestion 1188.516m (+4.77pct; dual mutual OA admin path)"),
    ("bud_riziv_transferts_ext_2025", "riziv", 2025, 2727230, "budgeted", "Transferts externes depenses 2727.230m"),
    ("bud_riziv_diverse_exp_2025", "riziv", 2025, 1486595, "budgeted", "Depenses diverses 1486.595m (+25.06pct)"),
    ("bud_riziv_relance_2025", "riziv", 2025, 7250, "budgeted", "Relanceplan EU 7.250m"),
    # receipts
    ("bud_riziv_globaal_beheer_2025", "riziv", 2025, 38322478, "budgeted", "Transferts gestion globale 38322.478m (+5.85pct)"),
    ("bud_riziv_contrib_2025", "riziv", 2025, 1806220, "budgeted", "Contributions 1806.220m"),
    ("bud_riziv_state_alloc_2025", "riziv", 2025, 824733, "budgeted", "Allocations publiques 824.733m"),
    ("bud_riziv_recettes_allouees_2025", "riziv", 2025, 1733477, "budgeted", "Recettes allouees 1733.477m"),
    ("bud_riziv_diverse_rec_2025", "riziv", 2025, 2527073, "budgeted", "Recettes diverses 2527.073m"),
    # corrections package
    ("bud_riziv_corrections_2025", "riziv_care", 2025, 216802, "budgeted", "Mesures correction totales 216.802m annual yield"),
    ("bud_riziv_corr_medecins_2025", "riziv_care", 2025, 73381, "budgeted", "Correction medecins 73.381m (teleconsult 68.404 + specialist key 4.977)"),
    ("bud_riziv_corr_meds_2025", "riziv_care", 2025, 113432, "budgeted", "Correction medicaments 113.432m (claw forward 80.363 etc)"),
    ("bud_riziv_corr_dentistes_2025", "riziv_care", 2025, 19989, "budgeted", "Correction dentistes DPSI 19.989m"),
    ("bud_riziv_corr_implants_2025", "riziv_care", 2025, 10000, "budgeted", "Correction implants nouvelles initiatives -10m"),
    ("bud_riziv_corr_teleconsult_2025", "riziv_care", 2025, 68404, "budgeted", "Suppression teleconsultations letter-key 68.404m"),
    ("bud_riziv_corr_claw_forward_2025", "riziv_care", 2025, 80363, "budgeted", "Claw forward pharma industry 80.363m"),
    ("bud_riziv_corr_prescription_2025", "riziv_care", 2025, 16000, "budgeted", "Prescription rationnelle 16m"),
    ("bud_riziv_sous_util_2025", "riziv_care", 2025, 114401, "budgeted", "Sous-utilisation non-structurelle 114.401m (Blouses blanches 38.2 etc)"),
    ("bud_riziv_reserve_2025", "riziv_care", 2025, 30148, "budgeted", "Montants reserves measures delay 30.148m"),
    ("bud_riziv_nonaffectable_2025", "riziv_care", 2025, 119655, "budgeted", "Montants non affectables 119.655m (down from 352.5m path)"),
    ("bud_riziv_prestation_delta_2025", "riziv_care", 2025, 1987440, "budgeted", "Croissance prestations +1987.440m (index 3.34 + real 2.35 class)"),
]
with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, eid, yr, amt_k, basis, notes in rows:
        f.write(
            f'{bid},{eid},{yr},{k(amt_k)},,,,{basis},src_inami_budget_sante_2025_matrix,strong,"{notes}"\n'
        )
print("budgets +", len(rows))

# --- commitments ---
cmt = (
    "cmt_riziv_budget_2025_matrix,INAMI RIZIV health insurance full budget matrix 2025,riziv,"
    "Patients providers mutualities pharma hospitals,"
    "Loi SSI 14 juillet 1994 art.40 Conseil des ministres 28/02/2025,"
    "2025-01-01,2025,2025,45221741000,"
    '"{""total_m"":45221.741,""prestations_m"":39812.15,""authorized_m"":39692.495,'
    '""beheer_m"":1188.516,""transferts_ext_m"":2727.23,""diverse_exp_m"":1486.595,'
    '""globaal_beheer_m"":38322.478,""corrections_m"":216.802,'
    '""corr_medecins_m"":73.381,""corr_meds_m"":113.432,""corr_dent_m"":19.989,""corr_implants_m"":10,'
    '""sous_util_m"":114.401,""reserve_m"":30.148,""nonaffectable_m"":119.655,'
    '""growth_pct"":5.69,""index_pct"":3.34,""real_growth_pct"":2.35,'
    '""dual_2026_global_m"":46775,""note"":""Strong CM primary PDF; mutual admin L5 residual gap_mutual_admin; dual VSB/AViQ care""}",'
    "0,active,docs/doge/data/raw/inami_budget_sante_2025.pdf,"
    "Universal compulsory health insurance financing and benefits,"
    "Open partial objectifs L5; dual mutual admin landsbond; track correction delivery,"
    "src_inami_budget_sante_2025_matrix,strong,SS>RIZIV>budget_2025_matrix,"
    "tick383: 45.222bn beheer 1.189bn corrections 216.8m\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)
print("cmt +1")

# --- leaderboard ---
lbs = [
    (
        "lb_riziv_global_45_2bn_2025",
        "RIZIV global health insurance budget 45.22bn 2025",
        "federal",
        "transfer",
        "SS>RIZIV>global_2025",
        45221741000,
        45221741000,
        "Strong CM: rec=exp 45221.741m; +5.69pct; dual 2026 46.775bn path",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "All insured residents Belgium",
        "Compulsory health insurance envelope",
        "Core entitlement mega not pure waste",
        2,
        10.0,
        3,
        6.73,
        "Track correction delivery vs overrun; protect access",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_prestations_39_8bn_2025",
        "RIZIV medical prestations objectif 39.81bn 2025",
        "federal",
        "transfer",
        "SS>RIZIV>prestations_2025",
        39812150000,
        39812150000,
        "Strong: 39812.150m objectif (+1987m); authorized 39692.5m after non-affectable",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "Patients providers",
        "Reimburse health care benefits",
        "Core; correction package 216.8m",
        2,
        10.0,
        4,
        6.63,
        "Partial objectifs L5 FOI; audit volume growth",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_beheer_1_19bn_2025",
        "RIZIV management costs 1.189bn 2025",
        "federal",
        "ops",
        "SS>RIZIV>beheerskosten",
        1188516000,
        1188516000,
        "Strong: 1188.516m couts de gestion (+4.77pct); dual mutual OA admin ~1.3-1.4bn path",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "INAMI + mutualities admin path",
        "Administration of health insurance",
        "Core admin; L5 landsbond residual FOI",
        4,
        8.5,
        4,
        6.33,
        "Open landsbond split dual gap_mutual_admin",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_corrections_217m_2025",
        "RIZIV budget correction package 216.8m 2025",
        "federal",
        "ops",
        "SS>RIZIV>corrections_2025",
        216802000,
        216802000,
        "Strong: 216.802m annual yield; meds 113.4 doctors 73.4 dentists 20 implants 10",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "Providers pharma industry",
        "Correct structural overrun path",
        "Policy correction not pure waste; delivery risk",
        5,
        7.5,
        5,
        6.18,
        "Publish mid-year delivery table vs 216.8m",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_corr_meds_113m_2025",
        "RIZIV pharma correction 113.4m 2025",
        "federal",
        "ops",
        "SS>RIZIV>corrections>medicaments",
        113432000,
        113432000,
        "Strong: claw forward 80.363 + prescription 16 + chapter IV 10 + pharmacists 7.07 net path",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "Pharma industry pharmacists prescribers",
        "Drug spending control package",
        "Largest correction block; claw forward opacity",
        5,
        7.5,
        5,
        6.18,
        "Open claw forward legal mechanism cash path",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_corr_teleconsult_68m_2025",
        "RIZIV teleconsultation key zeroing 68.4m 2025",
        "federal",
        "ops",
        "SS>RIZIV>corrections>teleconsult",
        68404000,
        68404000,
        "Strong: zero letter-key teleconsultations 68.404m of doctors 73.381m package",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "GP specialist teleconsult practices",
        "End pandemic teleconsult tariff path",
        "High-visibility cut; access trade-off",
        6,
        5.5,
        4,
        5.53,
        "Track volume residual after zero key",
        "seed",
        "",
        "tick383",
    ),
    (
        "lb_riziv_globaal_beheer_38_3bn_2025",
        "RIZIV transfer from global SS management 38.32bn 2025",
        "federal",
        "transfer",
        "SS>RIZIV>gestion_globale",
        38322478000,
        38322478000,
        "Strong: 38322.478m from Globaal Beheer (+5.85pct); dual ONSS financing path",
        "strong",
        "src_inami_budget_sante_2025_matrix",
        "Health insurance via SS treasury",
        "Primary financing path from global management",
        "Core transfer not waste",
        2,
        10.0,
        3,
        6.73,
        "Reconcile ONSS GFB multi-year",
        "seed",
        "",
        "tick383",
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

# update entity notes lightly
ent = (DATA / "entities.csv").read_text(encoding="utf-8")
old = "riziv,RIZIV / INAMI (globaal),INAMI (global),NIHDI global health insurance,social_security,sec_ss,bi,https://www.riziv.fgov.be,,,Global VGV 46.775 bn 2026 (45.222 bn 2025)"
new = "riziv,RIZIV / INAMI (globaal),INAMI (global),NIHDI global health insurance,social_security,sec_ss,bi,https://www.riziv.fgov.be,,,Global 45.222bn 2025 (beheer 1.189bn corrections 217m); 46.775bn 2026; tick383"
if old in ent:
    (DATA / "entities.csv").write_text(ent.replace(old, new), encoding="utf-8")
    print("entity riziv updated")

# research queue
rq = DATA / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    "rq_374,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T05:45:00Z,,Spawned tick382 after FSO 2025; rq_116 SWA deferred"
)
new = (
    "rq_374,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_riziv_partial_objectifs_l5,2026-08-01T05:45:00Z,2026-08-01T06:15:00Z,"
    "tick383: RIZIV 45.222bn matrix + corrections 216.8m; FOI partial objectifs; spawn rq_375"
)
if old not in text:
    raise SystemExit("rq_374 not found")
rq.write_text(text.replace(old, new), encoding="utf-8")
with rq.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_375,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T06:15:00Z,,Spawned tick383 after RIZIV 45.2bn; rq_116 SWA deferred\n"
    )
print("rq done")

foi = (
    "gap_riziv_partial_objectifs_l5,SS>RIZIV>objectifs_partiels_L5,riziv,"
    "Full partial budget objectives table (annexe 2) with EUR by sector 2024-2026; mid-year "
    "delivery of 216.802m corrections; landsbond split inside beheer 1.189bn; claw-forward cash path,"
    "Global and correction aggregates strong CM 2025; sector L5 and mutual admin residual,6,"
    "RIZIV-INAMI / FOD SZ / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_riziv_partial_objectifs_l5.md,ready,2026-08-01,,,,,"
    "cmt_riziv_budget_2025_matrix,lb_riziv_global_45_2bn_2025|lb_riziv_corrections_217m_2025,"
    "2026-08-01T06:15:00Z,2026-08-01T06:15:00Z,"
    "tick383 draft ready; dual gap_mutual_admin residual"
)
with (DATA / "foi_queue.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(foi + "\n")
print("foi +1")

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T06:15:00Z,rq_374,383,no,"
    "Scheduler 60s. Next prio5 rq_375; rq_116 SWA deferred. FOI ready. tick383 RIZIV 45.2bn corrections 217m.\n",
    encoding="utf-8",
)
print("state 383 OK")
