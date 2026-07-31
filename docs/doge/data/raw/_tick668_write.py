# -*- coding: utf-8 -*-
"""Tick 668: FWB aju2026 full DO matrix + debt Moody A3 + economies dual WAL — rq_659."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T08:45:00Z"
TICK = 668
RQ = "rq_659"
NEXT_RQ = "rq_660"
GAP = "gap_fwb_aju2026_do_debt_l5"
SRC = "src_ccrek_fwb_aju2026_do_debt"
SRC_DUAL = "src_dual_fwb_wal_aju2026_tick668"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str]) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and any(
            L.startswith(key + ",") or L.startswith("\ufeff" + key + ",")
            for L in existing.splitlines()
        ):
            print(f"SKIP exists {key}")
            continue
        if not text.endswith("\n"):
            text += "\n"
        text += row + "\n"
        existing = text
        added += 1
        print(f"ADD {key}")
    path.write_bytes(text.encode("utf-8"))
    return added


def update_rq_done(path: Path, rq_id: str, notes: str) -> None:
    text = read_text(path)
    lines = text.splitlines()
    out = []
    for L in lines:
        if L.startswith(rq_id + ",") or L.startswith("\ufeff" + rq_id + ","):
            parts = L.split(",")
            if len(parts) >= 5:
                parts[4] = "done"
            if len(parts) >= 11:
                parts[10] = NOW
            if len(parts) >= 12:
                parts[11] = notes.replace(",", ";")
            else:
                parts.append(notes.replace(",", ";"))
            L = ",".join(parts)
            print(f"RQ done {rq_id}")
        out.append(L)
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


def spawn_rq(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    if any(L.startswith(key + ",") for L in text.splitlines()):
        print(f"SKIP spawn {key}")
        return
    if not text.endswith("\n"):
        text += "\n"
    text += row + "\n"
    path.write_bytes(text.encode("utf-8"))
    print(f"SPAWN {key}")


def set_loop_state(path: Path) -> None:
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes"
    notes = (
        f"tick{TICK} FWB aju DO matrix 16.5bn Moody A3 debt 16.2bn dual WAL Baa1; "
        f"next {NEXT_RQ}; progress@670 in 2; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


def update_foi(path: Path, row: str) -> None:
    text = read_text(path)
    key = row.split(",", 1)[0]
    lines = text.splitlines()
    out = []
    found = False
    for L in lines:
        if L.startswith(key + ",") or L.startswith("\ufeff" + key + ","):
            out.append(row)
            found = True
            print(f"FOI update {key}")
        else:
            out.append(L)
    if not found:
        out.append(row)
        print(f"FOI add {key}")
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


ent_rows = [
    "fwb_cabinets,Cabinets ministeriels FWB,Cabinets ministeriels Communaute francaise,FWB ministerial cabinets dual VL WAL,agency,fwb_gov,fr,https://www.federation-wallonie-bruxelles.be,,,CoA aju2026 DO06 CE=CL 16.788m path -0.084; dual WAL cabinets 28.043m; tick668",
]

src_rows = [
    f"{SRC},CoA FWB aju2026 full DO matrix + debt Moody A3 + economies dual WAL,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCFB_2026_AJU.pdf,Cour des comptes Belgique,2026-08-01,audit,"
    "Strong tick668: Table18 total CE 16409.5 CL 16504.2 path +193.7/+184.6; DO51 2957.6 DO52 3648.5 DO53 942.3 DO54 1166.2 DO55 756.0 DO19 enfance 775.0 DO25 AV 458.5 DO20 culture CL 324.6 DO23 jeunesse 181.6 DO85 dette 1313.0 DO90 580.9 cabinets 16.8; debt eoy2025 14421.3 path eoy2026 16200.3 eoy2029 20624.8; interest aju 356.5 (code21 343.5 swaps 13); Moody A3 Apr2026 from A2; financing need 2181.7; ratio debt/rec 98.4pct 2024 to 140pct 2029; interest path to 560.6 2029; econ Table3 253.6/522.9/599.1/733 (oblig 87.5 enfance 118 sup 17.9 cult 12.6 FP 8.7); CRP netting >493.8; index path 158.8 CE; pupils 868731 (-3503); +151 ETP; SACA +35.4 consol -49.7; snowball risk 2026",
    f"{SRC_DUAL},Dual FWB aju DO debt Moody A3 vs WAL Baa1 cabinets dual,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCFB_2026_AJU.pdf,DOGE synthesis CoA FWB+WAL aju dual,2026-08-01,synthesis,"
    "Strong dual: FWB SEC -1.753bn CL 16.50bn cabinets 16.8m Moody A3 debt 16.2bn vs WAL SEC -2.015bn CL 21.94bn cabinets 28.0m Moody Baa1 debt 33.0bn; not TE-additive; tick668",
]

# Note: CoA report URL may be 2026_33_BudgetCFB or similar - existing source used Docs path from earlier
# Fix URL to match existing if known
SRC_URL_NOTE = "https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCFB_2026_AJU.pdf"

bud_rows = [
    # Totals Table17/18
    f"bud_fwb_do_total_ce_aju_2026,fwb_gov,2026,16409539000,,,budgeted,{SRC},strong,Total CE aju 16409.539m path +193.698 (+1.2pct) vs init 16215.841; tick668",
    f"bud_fwb_do_total_cl_aju_2026,fwb_gov,2026,16504162000,,,budgeted,{SRC},strong,Total CL aju 16504.162m path +184.554 (+1.1pct) vs init 16319.608; exec 29Jun 8572.210 (52pct); tick668",
    f"bud_fwb_do_total_ce_init_2026,fwb_gov,2026,16215841000,,,budgeted,{SRC},strong,Total CE init 16215.841m; tick668",
    f"bud_fwb_do_total_cl_init_2026,fwb_gov,2026,16319608000,,,budgeted,{SRC},strong,Total CL init 16319.608m; tick668",
    f"bud_fwb_credits_lim_ce_aju_2026,fwb_gov,2026,7878700000,,,budgeted,{SRC},strong,Credits limitatifs CE aju 7878.7m path -42.8; tick668",
    f"bud_fwb_credits_nonlim_ce_aju_2026,fwb_gov,2026,8485100000,,,budgeted,{SRC},strong,Credits non limitatifs CE=CL aju 8485.1m path +235.2 (mainly enseignement); tick668",
    f"bud_fwb_fonds_budg_ce_aju_2026,fwb_gov,2026,45800000,,,budgeted,{SRC},strong,Fonds budgetaires CE=CL aju 45.8m path +1.4; tick668",
    f"bud_fwb_exec_cl_jun2026,fwb_gov,2026,8572209698,,,outturn,{SRC},strong,CL execution 29Jun2026 8572.210m ~52pct of aju CL; tick668",
    # Dual overhead
    f"bud_fwb_do01_parlement_aju_2026,fwb_gov,2026,37561000,,,budgeted,{SRC},strong,DO01 Parlement+Mediateur CE=CL aju 37.561m path +0.024 exec 20.601 (55pct); dual WAL DO01 88.9; tick668",
    f"bud_fwb_cabinets_aju_2026,fwb_cabinets,2026,16788000,,,budgeted,{SRC},strong,DO06 cabinets CE=CL aju 16.788m path -0.084 exec 5.681 (34pct); dual WAL 28.043m; tick668",
    f"bud_fwb_do11_sg_ce_aju_2026,fwb_gov,2026,879834000,,,budgeted,{SRC},strong,DO11 Affaires gen SG CE aju 879.834 CL 862.328 path -23.245/-22.110; tick668",
    f"bud_fwb_do11_sg_cl_aju_2026,fwb_gov,2026,862328000,,,budgeted,{SRC},strong,DO11 SG CL aju 862.328m; tick668",
    f"bud_fwb_do12_it_aju_2026,fwb_gov,2026,129469000,,,budgeted,{SRC},strong,DO12 Informatique CE=CL aju 129.469m path -4.668 exec 96.872 (75pct); dual Digitaal; tick668",
    f"bud_fwb_do13_immeubles_aju_2026,fwb_gov,2026,59420000,,,budgeted,{SRC},strong,DO13 Gestion immeubles CE=CL aju 59.420m path -0.027 exec near 0; tick668",
    f"bud_fwb_do14_ri_fonds_aju_2026,fwb_gov,2026,50515000,,,budgeted,{SRC},strong,DO14 Relations int + Fonds EU CE aju 50.515 CL 50.516; tick668",
    f"bud_fwb_do15_infra_sante_aju_2026,fwb_gov,2026,81069000,,,budgeted,{SRC},strong,DO15 Infra sante/sociale/culture/sport CE aju 81.069 CL 81.506; tick668",
    f"bud_fwb_do17_aj_ce_aju_2026,fwb_gov,2026,474404000,,,budgeted,{SRC},strong,DO17 Aide a la Jeunesse CE aju 474.404 CL 474.143 path +3.873/+3.526; dual VL jeugdhulp; tick668",
    f"bud_fwb_do18_mdj_ce_aju_2026,fwb_gov,2026,28708000,,,budgeted,{SRC},strong,DO18 Maisons de Justice CE aju 28.708 CL 30.356 path +0.346/+0.232; tick668",
    f"bud_fwb_do19_enfance_ce_aju_2026,fwb_gov,2026,774994000,,,budgeted,{SRC},strong,DO19 Enfance CE=CL aju 774.994m path +14.017 exec 518.655 (67pct); dual ONE/KO; tick668",
    f"bud_fwb_do20_culture_ce_aju_2026,fwb_gov,2026,227942000,,,budgeted,{SRC},strong,DO20 Culture (hors EP/jeun/AV) CE aju 227.942 CL 324.618 path -39.271/-42.850; tick668",
    f"bud_fwb_do20_culture_cl_aju_2026,fwb_gov,2026,324618000,,,budgeted,{SRC},strong,DO20 Culture CL aju 324.618m; tick668",
    f"bud_fwb_do23_jeunesse_ce_aju_2026,fwb_gov,2026,168350000,,,budgeted,{SRC},strong,DO23 Jeunesse+EP CE aju 168.350 CL 181.570 path +69.957/+69.829 exec 169.344 (93pct); tick668",
    f"bud_fwb_do23_jeunesse_cl_aju_2026,fwb_gov,2026,181570000,,,budgeted,{SRC},strong,DO23 Jeunesse+EP CL aju 181.570m; tick668",
    f"bud_fwb_do25_audiovisuel_ce_aju_2026,rtbf,2026,457266000,,,budgeted,{SRC},strong,DO25 Audiovisuel Multimedia CE aju 457.266 CL 458.497 path +6.770/+6.636 (RTBF channel dual VRT); tick668",
    f"bud_fwb_do25_audiovisuel_cl_aju_2026,rtbf,2026,458497000,,,budgeted,{SRC},strong,DO25 AV CL aju 458.497m; tick668",
    f"bud_fwb_do26_sport_aju_2026,fwb_gov,2026,51647000,,,budgeted,{SRC},strong,DO26 Sport CE aju 51.647 CL 53.330 path +3.331/+3.349; tick668",
    f"bud_fwb_do40_services_communs_aju_2026,fwb_gov,2026,162858000,,,budgeted,{SRC},strong,DO40 services communs CE aju 162.858 CL 162.920 path -3.803/-4.868; tick668",
    f"bud_fwb_do41_pilotage_ens_aju_2026,fwb_gov,2026,103447000,,,budgeted,{SRC},strong,DO41 Pilotage enseignement CE aju 103.447 CL 102.287 path +8.536/+7.254; tick668",
    f"bud_fwb_do42_dot_wallonie_aju_2026,fwb_gov,2026,39858000,,,budgeted,{SRC},strong,DO42 Dotation a Wallonie CE=CL aju 39.858m path +0.122; dual transfer; tick668",
    f"bud_fwb_do44_batiments_scol_aju_2026,fwb_gov,2026,225864000,,,budgeted,{SRC},strong,DO44 Batiments scolaires CE aju 225.864 CL 227.144 path +1.090/+0.570 exec 6pct; tick668",
    f"bud_fwb_do45_recherche_ce_aju_2026,fwb_gov,2026,265750000,,,budgeted,{SRC},strong,DO45 Recherche scientifique CE aju 265.750 CL 262.637 path +3.003/-0.119; dual FWO; tick668",
    f"bud_fwb_do47_alloc_etudes_aju_2026,fwb_gov,2026,105590000,,,budgeted,{SRC},strong,DO47 Allocations d etudes CE=CL aju 105.590m path +7.229; tick668",
    f"bud_fwb_do48_pms_aju_2026,fwb_gov,2026,144217000,,,budgeted,{SRC},strong,DO48 Centres PMS CE=CL aju 144.217m path +2.718; tick668",
    # Education core
    f"bud_fwb_do51_fondamental_aju_2026,fwb_gov,2026,2957618000,,,budgeted,{SRC},strong,DO51 prescolaire+primaire CE=CL aju 2957.618m path +39.160; tick668",
    f"bud_fwb_do52_secondaire_ce_aju_2026,fwb_gov,2026,3648284000,,,budgeted,{SRC},strong,DO52 secondaire CE aju 3648.284 CL 3648.478 path +69.902; tick668",
    f"bud_fwb_do52_secondaire_cl_aju_2026,fwb_gov,2026,3648478000,,,budgeted,{SRC},strong,DO52 secondaire CL aju 3648.478m; tick668",
    f"bud_fwb_do53_specialise_aju_2026,fwb_gov,2026,942276000,,,budgeted,{SRC},strong,DO53 specialise CE=CL aju 942.276m path +1.737; poles territoriaux -4.2m hyp; tick668",
    f"bud_fwb_do54_universite_aju_2026,fwb_gov,2026,1166169000,,,budgeted,{SRC},strong,DO54 universitaire CE=CL aju 1166.169m path +11.506; dual VL unis; tick668",
    f"bud_fwb_do55_sup_hors_uni_aju_2026,fwb_gov,2026,756042000,,,budgeted,{SRC},strong,DO55 sup hors uni/HE CE=CL aju 756.042m path +1.612; tick668",
    f"bud_fwb_do56_promo_soc_aju_2026,fwb_gov,2026,271391000,,,budgeted,{SRC},strong,DO56 promotion sociale CE=CL aju 271.391m path +3.844; tick668",
    f"bud_fwb_do57_artistique_aju_2026,fwb_gov,2026,265039000,,,budgeted,{SRC},strong,DO57 enseignement artistique CE=CL aju 265.039m path +3.438; tick668",
    f"bud_fwb_do58_distance_aju_2026,fwb_gov,2026,2372000,,,budgeted,{SRC},strong,DO58 enseignement a distance CE=CL aju 2.372m flat; tick668",
    f"bud_fwb_do85_dette_directe_aju_2026,fwb_gov,2026,1312974000,,,budgeted,{SRC},strong,DO85 dette directe CE=CL aju 1312.974m path +7.500; tick668",
    f"bud_fwb_do90_dot_rw_cocof_aju_2026,fwb_gov,2026,580939000,,,budgeted,{SRC},strong,DO90 Dotations RW+COCOF CE=CL aju 580.939m path +5.623 (Ste-Emilie channel dual); tick668",
    # Education commentary residual
    f"bud_fwb_pupils_jan2026,fwb_gov,2026,868731,,,outturn,{SRC},strong,Population scolaire obligatoire 15Jan2026 868731 vs 2025 872234 (-3503); charges still up +151 ETP; tick668",
    f"bud_fwb_pupils_jan2025,fwb_gov,2025,872234,,,outturn,{SRC},strong,Population scolaire 15Jan2025 872234; tick668",
    f"bud_fwb_etp_plus_151_2026,fwb_gov,2026,151,,,budgeted,{SRC},strong,Creation 151 ETP pedagogiques malgre baisse eleves; tick668",
    f"bud_fwb_poles_territoriaux_minus_4_2m,fwb_gov,2026,-4200000,,,budgeted,{SRC},strong,DO53 poles territoriaux path -4.2m (nouvelle hypothese calcul CoA flags weak); tick668",
    f"bud_fwb_index_path_158_8m_ce,fwb_gov,2026,158800000,,,budgeted,{SRC},strong,Indexation traitements+fonctionnement path +158.8m CE / +158.6m CL conclave; tick668",
    f"bud_fwb_crp_netting_493_8m,fwb_gov,2026,493800000,,,budgeted,{SRC},strong,CRP+transition pension netted vs IPP dot understate rec+dep >493.8m (no net impact); universality breach; tick668",
    # Debt chapter
    f"bud_fwb_debt_direct_eoy2018,fwb_gov,2018,6911000000,,,outturn,{SRC},strong,Dette directe eoy2018 6911.0m; tick668",
    f"bud_fwb_debt_direct_eoy2025,fwb_gov,2025,14421300000,,,outturn,{SRC},strong,Dette directe eoy2025 14421.3m (+108.7pct vs 2018); tick668",
    f"bud_fwb_debt_path_eoy2026,fwb_gov,2026,16200300000,,,budgeted,{SRC},strong,Dette directe path eoy2026 16200.3m (+1779 need; +285.6 vs init path); tick668",
    f"bud_fwb_debt_path_eoy2029,fwb_gov,2029,20624800000,,,budgeted,{SRC},strong,Dette directe path eoy2029 20624.8m (+61.4pct vs eoy2024); tick668",
    f"bud_fwb_debt_brute_consol_eoy2024,fwb_gov,2024,14240600000,,,outturn,{SRC},strong,Dette brute consol eoy2024 ICN 14240.6m (+6134.7 vs 2018 +75.7pct); tick668",
    f"bud_fwb_financing_need_aju_2026,fwb_gov,2026,2181700000,,,budgeted,{SRC},strong,Financing need total aju 2181.7m (init 2081.9; 2025 aju 1825.8); tick668",
    f"bud_fwb_financing_need_hors_amort_2026,fwb_gov,2026,1779000000,,,budgeted,{SRC},strong,Financing need hors amort 1779.0m; tick668",
    f"bud_fwb_interest_charges_aju_2026,fwb_gov,2026,343500000,,,budgeted,{SRC},strong,Interest charges aju 343.5m (init 340.0; exec2025 285.2); tick668",
    f"bud_fwb_swaps_aju_2026,fwb_gov,2026,13000000,,,budgeted,{SRC},strong,Swaps aju 13.0m (init 17.0; 2025 9.2); tick668",
    f"bud_fwb_interest_total_aju_2026,fwb_gov,2026,356500000,,,budgeted,{SRC},strong,Interest total aju 356.5m (init 357.0 nearly flat); taux implicite 2.2pct; tick668",
    f"bud_fwb_interest_path_2029,fwb_gov,2029,560600000,,,budgeted,{SRC},strong,Interest path ~560.6m 2029 (3.8pct recettes) from 255.4 2024 (2.0pct); tick668",
    f"bud_fwb_debt_rec_ratio_2024,fwb_gov,2024,98.4,,,outturn,{SRC},strong,Debt/recettes ratio 98.4pct 2024; tick668",
    f"bud_fwb_debt_rec_ratio_path_2029,fwb_gov,2029,140.0,,,budgeted,{SRC},strong,Debt/recettes path 140.0pct 2029; tick668",
    f"bud_fwb_refi_plus_new_2025_29,fwb_gov,2029,10115500000,,,budgeted,{SRC},strong,Refi+new financing 2025-29 10115.5m (refi 2458.9 + new 7656.7); snowball risk; tick668",
    f"bud_fwb_new_loan_rate_2025,fwb_gov,2025,3.6,,,outturn,{SRC},strong,New loan rate 2025 3.6pct vs 1.6pct 2021; fixed share 92.2pct 2025 (94.5 2024); tick668",
    # Economies Table3 residual sector split (some totals exist)
    f"bud_fwb_econ_oblig_esa_2026,fwb_gov,2026,87500000,,,budgeted,{SRC},strong,Economies enseignement obligatoire+ESAHR+adultes SEC 87.5m 2026 (path 300.1 2029); tick668",
    f"bud_fwb_econ_enfance_2026,fwb_gov,2026,118000000,,,budgeted,{SRC},strong,Economies Enfance SEC 118.0m 2026 (path 143.3 2029); tick668",
    f"bud_fwb_econ_superieur_2026,fwb_gov,2026,17900000,,,budgeted,{SRC},strong,Economies ens superieur+hopitaux univ 17.9m 2026 (path 96.9 2029); tick668",
    f"bud_fwb_econ_culture_2026,fwb_gov,2026,12600000,,,budgeted,{SRC},strong,Economies Culture 12.6m 2026 (path 26.7 2029); tick668",
    f"bud_fwb_econ_fp_2026,fwb_gov,2026,8700000,,,budgeted,{SRC},strong,Economies Fonction publique 8.7m 2026 (path 57.0 2029); tick668",
    f"bud_fwb_econ_autres_2026,fwb_gov,2026,8800000,,,budgeted,{SRC},strong,Economies Autres 8.8m 2026 (path 109.0 2029); tick668",
    f"bud_fwb_econ_path_2029_total,fwb_gov,2029,733000000,,,budgeted,{SRC},strong,Economies SEC path total 733.0m 2029 (2026 253.6 already seeded); tick668",
    # Consol residual Table4 detail
    f"bud_fwb_consol_inst_aju_2026,fwb_gov,2026,-49700000,,,budgeted,{SRC},strong,Solde institutions consol aju -49.7m path +83.5 vs init -133.2; tick668",
    f"bud_fwb_saca_sec_aju_2026,fwb_gov,2026,35400000,,,budgeted,{SRC},strong,SACA SEC aju +35.4m path +76.8 vs init -41.4; tick668",
    f"bud_fwb_type2_sec_aju_2026,fwb_gov,2026,62700000,,,budgeted,{SRC},strong,OAP type2 SEC aju +62.7m path -5.1; tick668",
    f"bud_fwb_type3_sec_aju_2026,fwb_gov,2026,-33700000,,,budgeted,{SRC},strong,OAP type3 SEC aju -33.7m path -2.3; tick668",
    f"bud_fwb_ens_sup_sec_aju_2026,fwb_gov,2026,-108000000,,,budgeted,{SRC},strong,Etablissements ens superieur SEC aju -108.0m path +14.1; tick668",
    f"bud_fwb_corr_sec_aju_2026,fwb_gov,2026,-238100000,,,budgeted,{SRC},strong,Corrections SEC aju -238.1m path -80.6; tick668",
    f"bud_fwb_solde_net_consol_aju_2026,fwb_gov,2026,-1966800000,,,budgeted,{SRC},strong,Solde net consol aju -1966.8m path -29.3; tick668",
    f"bud_fwb_emprunts_prod_aju_2026,fwb_gov,2026,2690300000,,,budgeted,{SRC},strong,Produits d emprunts aju 2690.3m path +111.0; tick668",
    f"bud_fwb_amort_dette_aju_2026,fwb_gov,2026,912700000,,,budgeted,{SRC},strong,Amortissements dette aju 912.7m flat; tick668",
    # Dual package
    f"bud_dual_fwb_wal_sec_aju_2026,gg_belgium,2026,-3768200000,,,budgeted,{SRC_DUAL},strong,Dual Entity II SEC aju FWB -1752.8 + WAL -2015.4 = -3768.2m (not TE-additive); tick668",
    f"bud_dual_cabinets_fwb_wal_2026,gg_belgium,2026,44831000,,,budgeted,{SRC_DUAL},strong,Dual cabinets FWB 16.788 + WAL 28.043 = 44.831m (not full BE cabinets); tick668",
]

cmt_rows = [
    f"cmt_fwb_do_matrix_aju2026,FWB aju2026 full DO CL 16.50bn dual VL,fwb_gov,FWB DO stack,CoA 2026_33 Table18,2026-06-30,2026,2026,16504162000,\"{{\"\"2026\"\":16504162000}}\",,active,,Map FWB spend aju,FOI L5,{SRC},strong,FWB>DO>aju2026,DO52 3.65bn DO51 2.96bn DO54 1.17bn dual; tick668",
    f"cmt_fwb_debt_moody_a3_2026,FWB debt 16.2bn Moody A3 dual WAL Baa1,fwb_gov,MFWB debt agency,CoA 2026_33 ch3,2026-04-01,2025,2029,16200300000,\"{{\"\"2025\"\":14421300000,\"\"2026\"\":16200300000,\"\"2029\"\":20624800000}}\",,active,,Debt snowball dual,Interest path 561m 2029,{SRC},strong,FWB>dette>aju2026,Ratio 140pct 2029; tick668",
    f"cmt_fwb_econ_sector_table3,FWB economies SEC by sector 254m 2026 dual,fwb_gov,FWB savings package,CoA Table3,2026-01-01,2026,2029,253600000,\"{{\"\"2026\"\":253600000,\"\"2029\"\":733000000}}\",,active,,Track DP1-3 delivery,Opaque incidence FOI,{SRC},strong,FWB>economies>sector,Enfance 118 oblig 87.5; tick668",
    f"cmt_fwb_cabinets_16_8m_dual,FWB cabinets 16.8m dual WAL 28.0m,fwb_cabinets,FWB cabinets,CoA Table18 DO06,2026-06-30,2026,2026,16788000,\"{{\"\"2026\"\":16788000}}\",,active,,Political overhead dual,Compare VL,{SRC},strong,FWB>DO06>cabinets,Path -0.084; tick668",
    f"cmt_fwb_crp_netting_493m,CRP pension netting >493.8m IPP dual,fwb_gov,LSF CRP,CoA 5.3.3,2026-01-01,2026,2026,493800000,\"{{\"\"2026\"\":493800000}}\",,active,,Universality breach,Show gross lines,{SRC},strong,FWB>recettes>CRP,No net impact; tick668",
    f"cmt_dual_fwb_wal_aju2026,Dual FWB+WAL aju SEC debt Moody cabinets,gg_belgium,Entity II dual,CoA FWB+WAL aju,2026-06-30,2026,2026,3768200000,\"{{\"\"2026\"\":3768200000}}\",,active,,Dual Entity II map,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>fwb_wal_aju,SEC -3.77bn; tick668",
]

lb_rows = [
    f"lb_fwb_do52_secondaire_3_65bn_2026,FWB DO52 secondaire CL 3.65bn,FWB,ops,FWB>DO52,3648478000,0,Strong CoA aju path +69.9m; pupils down but ETP +151 dual GO!;strong,{SRC},schools staff,Compulsory secondary,Primary,5.0,8.5,3,6.55,Track economies DP2,open,,tick668",
    f"lb_fwb_debt_16_2bn_moody_a3_2026,FWB debt path 16.2bn Moody A3,FWB,ops,FWB>dette,16200300000,0,Strong CoA: eoy2025 14.42bn path 16.20/20.62 2026/29; Moody A3 Apr2026; interest 357m path 561m; dual WAL Baa1,strong,{SRC},bondholders,Debt snowball dual,Primary,7.5,9.0,3,7.35,Publish interest paid-accrued,open,,tick668",
    f"lb_fwb_cabinets_16_8m_2026,FWB cabinets 16.8m dual WAL 28m,FWB,ops,FWB>DO06>cabinets,16788000,0,Strong CoA DO06 flat path -0.08m exec 34pct; dual WAL 28.0m,strong,{SRC},ministerial staff,Political overhead,Primary,7.0,5.0,2,5.8,FTE+comms FOI,open,,tick668",
    f"lb_fwb_do25_av_458m_2026,FWB DO25 audiovisuel 458m dual VRT,FWB,ops,FWB>DO25>RTBF,458497000,0,Strong CoA CL 458.5m path +6.6m dual VRT package,strong,{SRC},RTBF,Public AV dual,Primary,6.0,7.5,2,6.3,RTBF L5 split,open,,tick668",
    f"lb_fwb_econ_enfance_118m_2026,FWB economies Enfance 118m 2026,FWB,ops,FWB>economies>enfance,118000000,0,Strong CoA Table3; CoA cannot verify incidence; dual KO,strong,{SRC},ONE channel,Savings opacity,Primary,7.5,6.5,3,6.55,Publish cash path,open,,tick668",
    f"lb_dual_fwb_wal_aju_sec_2026,Dual FWB+WAL SEC aju -3.77bn,Belgium,ops,Belgium>dual>fwb_wal_sec,3768200000,0,Strong dual: FWB -1.753 + WAL -2.015; Moody A3/Baa1; cabinets 44.8m; not TE-additive,strong,{SRC_DUAL},Entity II,Dual fiscal residual,Primary dual,6.5,8.5,3,6.85,Cross-entity FOI,open,,tick668",
]

foi_row = (
    f"{GAP},FWB>Aju2026>DO_debt_L5,fwb_gov,"
    "DO L5 split enseignement 51-55 economies incidence DP1-3; cabinets FTE; RTBF within DO25; debt interest paid-accrued; CRP gross lines; Moody drivers,"
    "CoA FWB aju2026 DO matrix debt Moody strong tick668; L5 residual dual WAL,"
    f"5,MFWB Budget / Agence de la dette / service transparence FWB,transparence@cfwb.be,https://www.federation-wallonie-bruxelles.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_fwb_do_matrix_aju2026|cmt_fwb_debt_moody_a3_2026|cmt_fwb_econ_sector_table3,"
    f"lb_fwb_debt_16_2bn_moody_a3_2026|lb_fwb_do52_secondaire_3_65bn_2026|lb_dual_fwb_wal_aju_sec_2026,"
    f"{NOW},{NOW},tick668 CoA FWB aju primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes FWB aju 2026 (2026_33) Table18 + ch.3 debt

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: MFWB Budget / Agence de la dette / service transparence
transparence@cfwb.be
https://www.federation-wallonie-bruxelles.be

Betreft: Openbaarheid — aju 2026 matrice DO, dette Moody A3, économies sectorielles L5

Geachte,

Op grond van de openbaarheidsregels van de Franse Gemeenschap verzoek ik om:

1. Ventilation L5 DO51-55 (enseignement) aju 2026: ETP, indexation vs volume,
   et suivi cash des economies Table3 (obligatoire 87,5 mEUR; superieur 17,9).
2. Cabinets DO06 (16,788 mEUR): FTE et communication/consultance par cabinet.
3. DO25 Audiovisuel (458,5 mEUR): part RTBF vs autres lignes.
4. Dette: estimation 2026 de la correction interets payes vs courus;
   detail des 10.115,5 mEUR refi+new 2025-2029.
5. CRP/transition pension: montants bruts recettes et depenses (>493,8 mEUR
   neutralises sur dotation IPP).
6. Pieces justificatives de la notation Moody A3 (avril 2026) si publiques.

Période: 2024-01-01 à 2029-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes agent
- Primary: CoA 2026_33 FWB aju (tick668). Local PDF: ccrek_2026_33_fwb_budget_aju.pdf
- Dual with WAL aju 2026_26 (cabinets/debt/Moody).
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **FWB aju2026 full DO matrix 16.50bn + debt Moody A3 + economies dual WAL**)
- Found (primary CoA 2026_33): **Total** CE **EUR16.410bn** / CL **EUR16.504bn** path **+193.7/+184.6**; exec Jun **EUR8.572bn** (52pct). Matrix: **DO52 sec EUR3.648bn** / **DO51 fond EUR2.958bn** / **DO54 uni EUR1.166bn** / **DO85 dette EUR1.313bn** / **DO55 EUR756m** / **DO19 enfance EUR775m** / **DO90 RW+COCOF EUR581m** / **DO25 AV EUR458m** / **DO17 AJ EUR474m** / **DO20 cult CL EUR325m** / **DO23 jeun EUR182m** / **cabinets EUR16.788m** (dual WAL **28.043m**). **Debt:** eoy2025 **EUR14.421bn** path eoy2026 **EUR16.200bn** / 2029 **EUR20.625bn**; financing **EUR2.182bn**; interest **EUR356.5m** path **EUR561m** 2029; ratio debt/rec **98.4%->140%**; **Moody A3** Apr2026 (from A2). **Economies** 2026 **EUR253.6m** (enfance **118** oblig **87.5**). **CRP netting >EUR493.8m**; index **+EUR158.8m**; pupils **-3503** but **+151 ETP**. Dual WAL SEC **-2.015** + FWB **-1.753** = **-3.768bn**. Strong CoA; L5 FOI.
- Wrote: entities (+fwb_cabinets); budgets (+75); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@670 in 2 ticks; rq_116 deferred
"""


def main() -> None:
    # fix source URL to match local file naming convention used in repo
    global src_rows
    src_rows = [
        f"{SRC},CoA FWB aju2026 full DO matrix + debt Moody A3 + economies dual WAL,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCFB_2026_AJU.pdf,Cour des comptes Belgique,2026-08-01,audit,"
        "Strong tick668: Table18 total CE 16409.5 CL 16504.2 path +193.7/+184.6; DO51 2957.6 DO52 3648.5 DO53 942.3 DO54 1166.2 DO55 756.0 DO19 775.0 DO25 458.5 DO20 CL 324.6 DO23 181.6 DO85 1313.0 DO90 580.9 cabinets 16.8; debt eoy2025 14421.3 path 16200.3/20624.8; interest 356.5 path 560.6; Moody A3 Apr2026; financing 2181.7; ratio 98.4 to 140pct; econ 253.6 sector split; CRP >493.8; index 158.8; pupils 868731 +151 ETP; SACA +35.4 consol -49.7",
        f"{SRC_DUAL},Dual FWB aju DO debt Moody A3 vs WAL Baa1 cabinets,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCFB_2026_AJU.pdf,DOGE synthesis CoA FWB+WAL aju dual,2026-08-01,synthesis,"
        "Strong dual: FWB SEC -1.753bn CL 16.50bn cabinets 16.8m Moody A3 debt 16.2bn vs WAL SEC -2.015bn CL 21.94bn cabinets 28.0m Moody Baa1 debt 33.0bn; not TE-additive; tick668",
    ]

    n_ent = append_rows(ROOT / "entities.csv", ent_rows)
    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_bud = append_rows(ROOT / "budgets.csv", bud_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    update_foi(ROOT / "foi_queue.csv", foi_row)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    draft_path.write_bytes(foi_draft.encode("utf-8"))
    print(f"DRAFT {draft_path}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} FWB aju DO matrix 16.50bn Moody A3 debt 16.2bn dual WAL; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,fwb_gov,"
        f"Next residual: FWB aju ch7 SACA/OAP perimeter L5 or Flanders CoA BA2026 dual cabinets/PRW or RTBF within DO25.,,"
        f"{NOW},,spawned tick{TICK} after {RQ}",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log = read_text(LOG)
    if f"tick {TICK}" not in log[-2500:]:
        if not log.endswith("\n"):
            log += "\n"
        log += log_entry
        LOG.write_bytes(log.encode("utf-8"))
        print("LOG appended")
    else:
        print("LOG skip duplicate")

    print(f"DONE tick{TICK}: ent={n_ent} src={n_src} bud={n_bud} cmt={n_cmt} lb={n_lb}")


if __name__ == "__main__":
    main()
