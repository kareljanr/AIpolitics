# tick384: RIZIV partial objectifs L5 matrix + admin OA split (closes FOI partial)
from pathlib import Path
import os

REPO = Path(os.getcwd())
if not (REPO / "docs/doge/data").exists():
    REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "docs/doge/data"

def k(n):
    return int(n * 1000)

src = (
    "src_inami_objectifs_partiels_2025,"
    "INAMI Budget 2025 annexe 2 objectifs partiels L5 + annexe1 admin OA split,"
    "docs/doge/data/raw/inami_budget_sante_2025.pdf,"
    "INAMI Conseil des ministres,"
    "2026-08-01,primary_budget,"
    '"Partial objectifs Budget 2025: doctors 11642.5m pharma 6979.2 hospitals day 8513.2 nurses 2319.8; OA admin 988.1m; dual tick383"'
)
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(src + "\n")

# partial objectifs (000 EUR final Budget 2025 column)
partial = [
    ("bud_riziv_obj0_transversal_2025", 74035, "Objectif 0 transversal health goals 74.035m"),
    ("bud_riziv_obj1_doctors_2025", 11642546, "Objectif 1 honoraires medecins 11642.546m (after -73.381 corrections)"),
    ("bud_riziv_obj1_clinbio_2025", 1556970, "1a clinical biology 1556.970m"),
    ("bud_riziv_obj1_imaging_2025", 1752703, "1b medical imaging 1752.703m"),
    ("bud_riziv_obj1_consult_2025", 3566427, "1c consultations visits 3566.427m (after -68.404 teleconsult)"),
    ("bud_riziv_obj1_special_2025", 1955396, "1d special prestations 1955.396m"),
    ("bud_riziv_obj1_surgery_2025", 1535595, "1e surgery 1535.595m"),
    ("bud_riziv_obj1_hors_nom_2025", 397581, "1h honoraires hors nomenclature 397.581m"),
    ("bud_riziv_obj2_dentists_2025", 1622006, "Objectif 2 dentists 1622.006m"),
    ("bud_riziv_obj3_pharma_2025", 6979202, "Objectif 3 pharmaceutical 6979.202m"),
    ("bud_riziv_obj3_specialites_2025", 6484040, "3a pharma specialites 6484.040m"),
    ("bud_riziv_obj3_marge_eco_2025", 150302, "3a.1 economic margin pharmacists 150.302m"),
    ("bud_riziv_obj3_basishon_2025", 605288, "3a.2 base honorarium pharmacists 605.288m"),
    ("bud_riziv_obj4_nurses_2025", 2319840, "Objectif 4 nursing home care 2319.840m"),
    ("bud_riziv_obj6_kines_2025", 1340350, "Objectif 6 physiotherapy 1340.350m"),
    ("bud_riziv_obj7_band_ortho_2025", 317194, "Objectif 7 bandagists orthopedists 317.194m"),
    ("bud_riziv_obj8_implants_2025", 1008228, "Objectif 8 implants devices 1008.228m"),
    ("bud_riziv_obj9_opticians_2025", 52264, "Objectif 9 opticians 52.264m"),
    ("bud_riziv_obj10_audiciens_2025", 127065, "Objectif 10 audiologists 127.065m"),
    ("bud_riziv_obj11_midwives_2025", 52299, "Objectif 11 midwives 52.299m"),
    ("bud_riziv_obj12_hospital_day_2025", 8513199, "Objectif 12 hospital day-rate package 8513.199m"),
    ("bud_riziv_obj12a_verpleegdag_2025", 8068468, "12a nursing day price 8068.468m"),
    ("bud_riziv_obj14_dialysis_2025", 581802, "Objectif 14 dialysis 581.802m"),
    ("bud_riziv_obj18_rehab_2025", 627091, "Objectif 18 rehab reeducation 627.091m"),
    ("bud_riziv_obj20_logopedie_2025", 218310, "Objectif 20 speech therapy 218.310m"),
    ("bud_riziv_obj23_maf_2025", 383521, "Objectif 23 maximum facture 383.521m"),
    ("bud_riziv_obj24_chronic_2025", 165047, "Objectif 24 chronic patients 165.047m"),
    ("bud_riziv_obj31_maisons_med_2025", 373212, "Objectif 31 medical houses 373.212m"),
    ("bud_riziv_obj33_soc_akkoord_2025", 295214, "Objectif 33 social accord 295.214m"),
    ("bud_riziv_obj40_psycho_2025", 250770, "Objectif 40 psychological care 250.770m"),
    ("bud_riziv_obj41_lvz_2025", 439863, "Objectif 41 LVZ forfait honoraria 439.863m"),
    # admin / external from annexe 1
    ("bud_riziv_admin_oa_2025", 988052, "Frais administration organismes assureurs 988.052m (mutualities)"),
    ("bud_riziv_admin_nmbs_2025", 24396, "Admin NMBS SNCB mutual path 24.396m"),
    ("bud_riziv_admin_hziv_2025", 28355, "Admin HZIV CAAMI 28.355m"),
    ("bud_riziv_admin_patient_orgs_2025", 2650, "Patient associations 2.650m"),
    ("bud_riziv_admin_inami_beheer_2025", 121731, "INAMI proper frais de gestion 121.731m"),
    ("bud_riziv_wet_ziekenhuizen_2025", 2696209, "External transfer wet ziekenhuizen 2696.209m"),
    ("bud_riziv_sociaal_statuut_2025", 332762, "Diverse sociaal statuut 332.762m"),
    ("bud_riziv_int_verdragen_exp_2025", 971057, "Internationale verdragen depenses 971.057m"),
    ("bud_riziv_art111_contracts_rec_2025", 2000515, "Recettes contrats art.111 medicaments 2000.515m"),
    ("bud_riziv_heffing_pharma_ca_2025", 347553, "Cotisation chiffre d affaires pharma 347.553m"),
    ("bud_riziv_private_insurers_2025", 228206, "Private insurance companies receipts 228.206m"),
    ("bud_riziv_blouses_blanches_fin_2025", 346431, "Financement fonds blouses blanches receipt 346.431m"),
    ("bud_riziv_taxe_effecten_2025", 478302, "Dotation tax securities accounts 478.302m"),
    ("bud_riziv_gfb_salaries_2025", 27275397, "Globaal beheer salaried 27275.397m"),
    ("bud_riziv_gfb_selfemp_2025", 2671742, "Globaal beheer self-employed 2671.742m"),
    ("bud_riziv_gfb_alt_salaries_2025", 7318632, "Globaal beheer alt finance salaries 7318.632m"),
    ("bud_riziv_gfb_alt_self_2025", 716891, "Globaal beheer alt finance self-employed 716.891m"),
]

with (DATA / "budgets.csv").open("a", encoding="utf-8", newline="") as f:
    for bid, amt_k, notes in partial:
        f.write(
            f'{bid},riziv_care,2025,{k(amt_k)},,,,budgeted,src_inami_objectifs_partiels_2025,strong,"{notes}"\n'
        )
print("budgets +", len(partial))

cmt = (
    "cmt_riziv_objectifs_partiels_2025,RIZIV partial budget objectives L5 matrix 2025,riziv_care,"
    "Doctors hospitals pharma nurses mutualities patients,"
    "Loi SSI art.40 annexe 2 Budget 2025 CM,"
    "2025-01-01,2025,2025,39812150000,"
    '"{""doctors_m"":11642.546,""pharma_m"":6979.202,""hospital_day_m"":8513.199,'
    '""nurses_m"":2319.84,""dentists_m"":1622.006,""kines_m"":1340.35,""implants_m"":1008.228,'
    '""dialysis_m"":581.802,""rehab_m"":627.091,""maisons_med_m"":373.212,""psycho_m"":250.77,'
    '""lvz_m"":439.863,""soc_akkoord_m"":295.214,""admin_oa_m"":988.052,""admin_inami_m"":121.731,'
    '""wet_ziekenhuizen_m"":2696.209,""esante_m"":113.436,""consult_m"":3566.427,'
    '""imaging_m"":1752.703,""note"":""Strong annexe2 Budget column; closes major FOI partial objectifs; residual mid-year delivery""}",'
    "0,active,docs/doge/data/raw/inami_budget_sante_2025.pdf,"
    "Allocate compulsory health insurance by care sector,"
    "Publish mid-year outturn vs objectifs; dual mutual landsbond,"
    "src_inami_objectifs_partiels_2025,strong,SS>RIZIV>objectifs_partiels_2025,"
    "tick384: doctors 11.64bn hospital day 8.51bn pharma 6.98bn OA admin 988m\n"
)
with (DATA / "commitments.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(cmt)

lbs = [
    ("lb_riziv_doctors_11_6bn_2025", "RIZIV doctors honoraria 11.64bn 2025", "federal", "transfer", "SS>RIZIV>obj1_medecins", 11642546000, 11642546000,
     "Strong annexe2: 11642.546m after 73.4m corrections; consults 3.57 imaging 1.75 surgery 1.54", "strong", "src_inami_objectifs_partiels_2025",
     "Physicians patients", "Medical fees reimbursement", "Core care; teleconsult cut 68.4m inside", 3, 9.5, 4, 6.68,
     "Track volume vs fee path", "seed", "", "tick384"),
    ("lb_riziv_hospital_day_8_51bn_2025", "RIZIV hospital day-rate package 8.51bn 2025", "federal", "transfer", "SS>RIZIV>obj12_hospital", 8513199000, 8513199000,
     "Strong: obj12 total 8513.199m; verpleegdagprijs 8068.468m", "strong", "src_inami_objectifs_partiels_2025",
     "Hospital patients", "Hospital nursing day financing", "Core hospital BMF dual", 2, 9.5, 4, 6.53,
     "Dual regional hospital investment VIPA", "seed", "", "tick384"),
    ("lb_riziv_pharma_6_98bn_2025", "RIZIV pharmaceutical package 6.98bn 2025", "federal", "transfer", "SS>RIZIV>obj3_pharma", 6979202000, 6979202000,
     "Strong: 6979.202m after 113.4m corrections; specialites 6484m", "strong", "src_inami_objectifs_partiels_2025",
     "Patients pharmacies industry", "Drug reimbursement", "Core; claw forward residual delivery", 3, 9.5, 4, 6.68,
     "Open claw-forward cash path", "seed", "", "tick384"),
    ("lb_riziv_nurses_2_32bn_2025", "RIZIV home nursing 2.32bn 2025", "federal", "transfer", "SS>RIZIV>obj4_nurses", 2319840000, 2319840000,
     "Strong: 2319.840m after Blouses blanches sous-util -38.2m path", "strong", "src_inami_objectifs_partiels_2025",
     "Home nursing patients", "Home care nursing fees", "Core long-term care dual regional", 2, 9.0, 3, 6.13,
     "Dual VSB/AViQ home care", "seed", "", "tick384"),
    ("lb_riziv_dentists_1_62bn_2025", "RIZIV dental fees 1.62bn 2025", "federal", "transfer", "SS>RIZIV>obj2_dentists", 1622006000, 1622006000,
     "Strong: 1622.006m after DPSI -20m and technical -11.2m", "strong", "src_inami_objectifs_partiels_2025",
     "Dental patients", "Dental care reimbursement", "Core", 2, 8.5, 3, 5.93,
     "Track DPSI delivery", "seed", "", "tick384"),
    ("lb_riziv_admin_oa_988m_2025", "RIZIV mutualities admin envelope 988m 2025", "federal", "ops", "SS>RIZIV>admin_OA", 988052000, 988052000,
     "Strong annexe1: frais administration O.A. 988.052m; dual gap_mutual_admin landsbond residual", "strong", "src_inami_objectifs_partiels_2025",
     "Mutualities landsbonden", "Admin financing of payment organisms", "Core dual CDZ 1.38bn path different year", 5, 8.5, 4, 6.48,
     "Open per-landsbond cash 2023-26", "seed", "", "tick384"),
    ("lb_riziv_wet_ziekenhuizen_2_70bn_2025", "RIZIV hospital law external transfer 2.70bn 2025", "federal", "transfer", "SS>RIZIV>wet_ziekenhuizen", 2696209000, 2696209000,
     "Strong: external transfer loi hopitaux 2696.209m", "strong", "src_inami_objectifs_partiels_2025",
     "Hospitals BMF path", "Hospital financing via hospital law", "Core dual day-rate obj12", 2, 9.0, 4, 6.03,
     "Reconcile with hospital BMF tables", "seed", "", "tick384"),
    ("lb_riziv_consult_3_57bn_2025", "RIZIV consultations and visits 3.57bn 2025", "federal", "transfer", "SS>RIZIV>obj1_consult", 3566427000, 3566427000,
     "Strong: 3566.427m after zeroing teleconsult key -68.404m", "strong", "src_inami_objectifs_partiels_2025",
     "GP specialist visit patients", "Consultation fee reimbursement", "Core ambulatory; teleconsult cut", 3, 9.0, 3, 6.28,
     "Track residual teleconsult volume", "seed", "", "tick384"),
    ("lb_riziv_kines_1_34bn_2025", "RIZIV physiotherapy 1.34bn 2025", "federal", "transfer", "SS>RIZIV>obj6_kines", 1340350000, 1340350000,
     "Strong: 1340.350m after -10.562 technical", "strong", "src_inami_objectifs_partiels_2025",
     "Physio patients", "Physiotherapy reimbursement", "Core", 2, 8.5, 3, 5.93,
     "Sector self-compensation note M24", "seed", "", "tick384"),
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

# update FOI gap_riziv to residual only
foi = (DATA / "foi_queue.csv").read_text(encoding="utf-8")
old = (
    "gap_riziv_partial_objectifs_l5,SS>RIZIV>objectifs_partiels_L5,riziv,"
    "Full partial budget objectives table (annexe 2) with EUR by sector 2024-2026; mid-year "
    "delivery of 216.802m corrections; landsbond split inside beheer 1.189bn; claw-forward cash path,"
    "Global and correction aggregates strong CM 2025; sector L5 and mutual admin residual,6,"
)
# if exact match hard, try simpler replace on notes
if "gap_riziv_partial_objectifs_l5" in foi:
    # append update via replace of ready note
    target = "tick383 draft ready; dual gap_mutual_admin residual"
    if target in foi:
        foi = foi.replace(
            target,
            "tick383|384: annexe2 L5 major sectors filled public; residual mid-year delivery + landsbond OA split + claw cash path human send",
        )
        (DATA / "foi_queue.csv").write_text(foi, encoding="utf-8")
        print("foi note updated")
    else:
        print("foi note target missing")

# also update gap_mutual_admin if present
foi2 = (DATA / "foi_queue.csv").read_text(encoding="utf-8")
if "gap_mutual_admin_l5" in foi2 and "988.052m" not in foi2:
    pass  # leave as is

# research queue
rq = DATA / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    "rq_375,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
    "2026-08-01T06:15:00Z,,Spawned tick383 after RIZIV 45.2bn; rq_116 SWA deferred"
)
new = (
    "rq_375,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,"
    "gap_riziv_partial_objectifs_l5,2026-08-01T06:15:00Z,2026-08-01T06:45:00Z,"
    "tick384: RIZIV partial objectifs L5 doctors 11.64bn hospital 8.51bn pharma 6.98bn OA 988m; spawn rq_376"
)
if old not in text:
    raise SystemExit("rq_375 not found")
rq.write_text(text.replace(old, new), encoding="utf-8")
with rq.open("a", encoding="utf-8", newline="") as f:
    f.write(
        "rq_376,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle.,,"
        "2026-08-01T06:45:00Z,,Spawned tick384 after RIZIV objectifs L5; rq_116 SWA deferred\n"
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-08-01T06:45:00Z,rq_375,384,no,"
    "Scheduler 60s. Next prio5 rq_376; rq_116 SWA deferred. FOI ready. tick384 RIZIV objectifs L5 doctors 11.6bn.\n",
    encoding="utf-8",
)
print("OK ticks=384")
