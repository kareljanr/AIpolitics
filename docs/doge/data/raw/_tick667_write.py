# -*- coding: utf-8 -*-
"""Tick 667: aju2026 Annex programme L5 matrix + cabinets + DO17/18/14 residual + AViQ pivot — rq_658."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T08:30:00Z"
TICK = 667
RQ = "rq_658"
NEXT_RQ = "rq_659"
GAP = "gap_wal_aju2026_annex_prog_l5"
SRC = "src_ccrek_wal_aju2026_annex_prog"
SRC_DUAL = "src_dual_aju2026_annex_prog_tick667"


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
        f"tick{TICK} annex prog L5 cabinets PRW/FRR 1.73bn DO17 sante 7.05bn dual; "
        f"next {NEXT_RQ}; progress@670 in 3; rq_116 deferred"
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


# amounts in EUR; CoA annex in kEUR
ent_rows = [
    "cwape,Cwape regulateur energie Wallonie,Commission wallonne pour l Energie Cwape,Walloon energy regulator dual VREG,agency,wallonie_gov,fr,https://www.cwape.be,,,DO01.129 dotation aju 9.380m path +0.121; dual VREG; tick667",
    "ceseffb,CeSEFFB expertise fiscale,Centre strategique d expertise fiscale financiere et budgetaire,Walloon fiscal expertise cell dual VL,agency,wallonie_gov,fr,https://www.wallonie.be,,,DO09.126 CE aju 9.918 CL 8.918 path +1.029/+0.029; tick667",
    "iweps,IWEPS statistique Wallonie,Institut wallon evaluation prospective statistique,Walloon statistics institute dual Statistiek Vlaanderen,agency,wallonie_gov,fr,https://www.iweps.be,,,DO09.021 CE=CL aju 7.727m flat; dual; tick667",
]

src_rows = [
    f"{SRC},CoA Budget RW aju2026 Annex programme L5 matrix + cabinets + AViQ residual dual,https://www.ccrek.be/sites/default/files/Docs/2026_26_BudgetRW_2026_AJU.pdf,Cour des comptes Belgique,2026-08-01,audit,"
    "Strong tick667 Annex kEUR: DO01 parl 77582 mediateur 1924 cwape 9380; cabinets MP 5404 Terr 5068 Eco 5328 Sante 3180 FP 1556 Tour 1593 Energ 2957 Agri 2957 total 28043; DO09 CESE 7858 AWEX 76843 Tourisme 68669/67928 RelExt 30098 IWEPS 7727 CeSEFFB 9918/8918; DO10 PRW/FRR CE 430885 CL 1734091 path +18461/+342405 exec 77026; DO14 transport 919597/887703 airports 84483/84552 sports 53775/59622 reseau 664067/575955; DO16 log prive 337870/342006 public 116199/120365 alliance EE 124683/124512; DO17 aff int 2765489/2469873 dot sante 7033912/7049370 action soc 358139/348606 creches 30684/15761; DO18 aides inv 165710/105828 outils 139352/121421 ZAE 83204/74303 recherche 247509/202495 Forem 2876052; DO19 dettes garanties 1915356; AViQ pivot -13m non-marchand -5 foreign care -6.7 PNRR internal 20.8/13.6; Forem inst 3007.4 path +42.4",
    f"{SRC_DUAL},Dual aju2026 annex prog cabinets PRW DO17 sante vs VL dual,https://www.ccrek.be/sites/default/files/Docs/2026_26_BudgetRW_2026_AJU.pdf,DOGE synthesis CoA annex dual VL,2026-08-01,synthesis,"
    "Strong dual: cabinets 28m PRW/FRR 1.73bn sante dot 7.05bn AWEX 76.8 dual FIT VL; not TE-additive; tick667",
]

bud_rows = [
    # DO01 programmes
    f"bud_parlement_dot_aju_2026,parlement_wallonie,2026,77582000,,,budgeted,{SRC},strong,Prog 002 Parlement dot CE=CL aju 77.582m path +1.328 exec 50.836; tick667",
    f"bud_mediateur_aju_2026,mediateur_wallonie,2026,1924000,,,budgeted,{SRC},strong,Prog 003 Mediateur CE=CL aju 1.924m path +0.033; tick667",
    f"bud_cwape_dot_aju_2026,cwape,2026,9380000,,,budgeted,{SRC},strong,Prog 129 Cwape CE=CL aju 9.380m path +0.121 exec 3.704; dual VREG; tick667",
    # Cabinets full matrix DO02
    f"bud_cabinet_mp_aju_2026,wallonie_gov,2026,5404000,,,budgeted,{SRC},strong,Cab 004 MP Budget Finances Recherche Bien-etre animal CE=CL 5.404m exec 1.196; tick667",
    f"bud_cabinet_territoire_aju_2026,wallonie_gov,2026,5068000,,,budgeted,{SRC},strong,Cab 005 Territoire Infra Mobilite Pouvoirs locaux CE=CL 5.068m exec 1.258; tick667",
    f"bud_cabinet_eco_emploi_aju_2026,wallonie_gov,2026,5328000,,,budgeted,{SRC},strong,Cab 006 Eco Industrie Num Emploi Formation CE=CL 5.328m exec 1.348; tick667",
    f"bud_cabinet_sante_env_aju_2026,wallonie_gov,2026,3180000,,,budgeted,{SRC},strong,Cab 007 Sante Env Solidarites Eco sociale CE=CL 3.180m exec 0.733; tick667",
    f"bud_cabinet_fp_aju_2026,wallonie_gov,2026,1556000,,,budgeted,{SRC},strong,Cab 008 FP Simplification Infra sportives CE=CL 1.556m exec 0.310; tick667",
    f"bud_cabinet_tourisme_aju_2026,wallonie_gov,2026,1593000,,,budgeted,{SRC},strong,Cab 009 Tourisme Patrimoine Petite enfance CE=CL 1.593m exec 0.367; tick667",
    f"bud_cabinet_energie_aju_2026,wallonie_gov,2026,2957000,,,budgeted,{SRC},strong,Cab 010 Energie Air-Climat Logement Aeroports CE=CL 2.957m exec 0.845; tick667",
    f"bud_cabinet_agri_aju_2026,wallonie_gov,2026,2957000,,,budgeted,{SRC},strong,Cab 011 Agriculture Ruralite CE=CL 2.957m exec 0.886; tick667",
    f"bud_cabinets_total_aju_2026,wallonie_gov,2026,28043000,,,budgeted,{SRC},strong,DO02 cabinets total CE=CL aju 28.043m flat exec 6.942 (24.8pct); dual VL cabinets; tick667",
    # DO09 named
    f"bud_cese_dot_aju_2026,wallonie_gov,2026,7858000,,,budgeted,{SRC},strong,Prog 012 CESE Wallonie CE=CL aju 7.858m flat exec 6.441; tick667",
    f"bud_service_social_do09_aju_2026,wallonie_gov,2026,6067000,,,budgeted,{SRC},strong,Prog 013 service social CE=CL aju 6.067m flat exec 100pct; tick667",
    f"bud_tourisme_do09_aju_2026,wallonie_gov,2026,68669000,,,budgeted,{SRC},strong,Prog 018 Tourisme CE aju 68.669 CL 67.928 path +3.037/+2.296 exec 25.100; tick667",
    f"bud_relations_ext_aju_2026,wallonie_gov,2026,30098000,,,budgeted,{SRC},strong,Prog 019 Relations exterieures CE=CL aju 30.098m flat exec 20.065; tick667",
    f"bud_awex_dot_aju_2026,awex,2026,76843000,,,budgeted,{SRC},strong,Prog 020 commerce exterieur/investisseurs CE=CL aju 76.843m flat exec 76.621 (99.7pct); dual FIT; tick667",
    f"bud_iweps_dot_aju_2026,iweps,2026,7727000,,,budgeted,{SRC},strong,Prog 021 IWEPS CE=CL aju 7.727m flat exec 5.795; dual; tick667",
    f"bud_ceseffb_ce_aju_2026,ceseffb,2026,9918000,,,budgeted,{SRC},strong,Prog 126 CeSEFFB CE aju 9.918 CL 8.918 path +1.029/+0.029 exec 1.867; tick667",
    f"bud_ceseffb_cl_aju_2026,ceseffb,2026,8918000,,,budgeted,{SRC},strong,Prog 126 CeSEFFB CL aju 8.918m; tick667",
    # DO10 PRW/FRR
    f"bud_prw_frr_ce_aju_2026,wallonie_gov,2026,430885000,,,budgeted,{SRC},strong,Prog 122 PRW+FRR CE aju 430.885m path +18.461; tick667",
    f"bud_prw_frr_cl_aju_2026,wallonie_gov,2026,1734091000,,,budgeted,{SRC},strong,Prog 122 PRW+FRR CL aju 1734.091m path +342.405 vs init 1391.686; exec 77.026 (4.4pct); tick667",
    f"bud_do10_dev_durable_aju_2026,wallonie_gov,2026,13255000,,,budgeted,{SRC},strong,Prog 085 dev durable CE aju 13.255 CL 5.184 flat; tick667",
    f"bud_do10_presidence_aju_2026,wallonie_gov,2026,13089000,,,budgeted,{SRC},strong,Prog 023 Presidence/Chancellerie CE aju 13.089 CL 9.496 path +1.256; tick667",
    # DO14 residual programmes
    f"bud_do14_mobilite_secu_ce_aju_2026,wallonie_gov,2026,50666000,,,budgeted,{SRC},strong,Prog 044 mobilite/securite routiere CE aju 50.666 CL 18.427 path +3.727/+2.605; tick667",
    f"bud_do14_transport_ce_aju_2026,otw,2026,919597000,,,budgeted,{SRC},strong,Prog 045 transport urbain/interurbain/scolaire CE aju 919.597 CL 887.703 path -0.691/+0.990 exec 621.857; dual De Lijn; tick667",
    f"bud_do14_transport_cl_aju_2026,otw,2026,887703000,,,budgeted,{SRC},strong,Prog 045 transport CL aju 887.703m; tick667",
    f"bud_do14_aeroports_aju_2026,wallonie_gov,2026,84483000,,,budgeted,{SRC},strong,Prog 046 aeroports CE aju 84.483 CL 84.552 path +1.132/+1.201; dual SOWAER; tick667",
    f"bud_do14_sports_infra_cl_aju_2026,wallonie_gov,2026,59622000,,,budgeted,{SRC},strong,Prog 047 infra sportives CL aju 59.622 path +5.274 CE flat 53.775; tick667",
    f"bud_do14_reseau_ce_aju_2026,wallonie_gov,2026,664067000,,,budgeted,{SRC},strong,Prog 049 reseau routier/hydraulique CE aju 664.067 CL 575.955 path -9.440/+28.578; tick667",
    f"bud_do14_reseau_cl_aju_2026,wallonie_gov,2026,575955000,,,budgeted,{SRC},strong,Prog 049 reseau CL aju 575.955m; tick667",
    f"bud_do14_fonds_secu_routiere_aju_2026,wallonie_gov,2026,45028000,,,budgeted,{SRC},strong,Prog 050 fonds securite routiere CE=CL aju 45.028 path -5.292; tick667",
    # DO16
    f"bud_do16_logement_prive_ce_aju_2026,wallonie_gov,2026,337870000,,,budgeted,{SRC},strong,Prog 080 logement prive CE aju 337.870 CL 342.006 path +6.236/+11.687 exec 102.018; primes dual; tick667",
    f"bud_do16_logement_prive_cl_aju_2026,wallonie_gov,2026,342006000,,,budgeted,{SRC},strong,Prog 080 logement prive CL aju 342.006m; tick667",
    f"bud_do16_logement_public_cl_aju_2026,wallonie_gov,2026,120365000,,,budgeted,{SRC},strong,Prog 081 logement public CL aju 120.365 CE 116.199; tick667",
    f"bud_do16_energie_ce_aju_2026,wallonie_gov,2026,35432000,,,budgeted,{SRC},strong,Prog 083 energie CE aju 35.432 CL 29.195 path +1.037/+0.835; tick667",
    f"bud_alliance_emploi_env_aju_2026,wallonie_gov,2026,124683000,,,budgeted,{SRC},strong,Prog 084 Alliance Emploi-Environnement CE aju 124.683 CL 124.512 path +4.926; tick667",
    f"bud_do16_fonds_energie_ce_aju_2026,wallonie_gov,2026,15147000,,,budgeted,{SRC},strong,Prog 089 fonds Energie CE aju 15.147 CL 12.557 path +7.161/+4.571; tick667",
    f"bud_do16_renopack_fonds_aju_2026,wallonie_gov,2026,72400000,,,budgeted,{SRC},strong,Prog 090 Ecopack/Renopack CE=CL aju 72.400m flat; tick667",
    # DO17 L4
    f"bud_do17_affaires_int_ce_aju_2026,wallonie_gov,2026,2765489000,,,budgeted,{SRC},strong,Prog 091 affaires interieures CE aju 2765.489 CL 2469.873 path +83.130/+82.965 exec 1380.041; fonds communes+aides; tick667",
    f"bud_do17_affaires_int_cl_aju_2026,wallonie_gov,2026,2469873000,,,budgeted,{SRC},strong,Prog 091 affaires interieures CL aju 2469.873m; tick667",
    f"bud_do17_dot_sante_ce_aju_2026,aviq,2026,7033912000,,,budgeted,{SRC},strong,Prog 093 dotations sante/protection sociale/handicap/familles CE aju 7033.912 CL 7049.370 path +7.311/-13.106 exec 5736.582; dual VAPH; tick667",
    f"bud_do17_dot_sante_cl_aju_2026,aviq,2026,7049370000,,,budgeted,{SRC},strong,Prog 093 dot sante CL aju 7049.370m; tick667",
    f"bud_do17_action_sociale_ce_aju_2026,wallonie_gov,2026,358139000,,,budgeted,{SRC},strong,Prog 094 action sociale CE aju 358.139 CL 348.606 path +28.541/+29.587; tick667",
    f"bud_do17_action_sociale_cl_aju_2026,wallonie_gov,2026,348606000,,,budgeted,{SRC},strong,Prog 094 action sociale CL aju 348.606m; tick667",
    f"bud_do17_creches_ce_aju_2026,wallonie_gov,2026,30684000,,,budgeted,{SRC},strong,Prog 095 creches CE aju 30.684 path +14.434 CL 15.761 path +5.294; tick667",
    f"bud_do17_creches_cl_aju_2026,wallonie_gov,2026,15761000,,,budgeted,{SRC},strong,Prog 095 creches CL aju 15.761m; tick667",
    # DO18 residual
    f"bud_do18_aides_invest_ce_aju_2026,wallonie_gov,2026,165710000,,,budgeted,{SRC},strong,Prog 096 aides investissement CE aju 165.710 CL 105.828 path +4.105/+15.644; dual VLAIO; tick667",
    f"bud_do18_aides_invest_cl_aju_2026,wallonie_gov,2026,105828000,,,budgeted,{SRC},strong,Prog 096 aides invest CL aju 105.828m; tick667",
    f"bud_do18_outils_eco_ce_aju_2026,wallonie_gov,2026,139352000,,,budgeted,{SRC},strong,Prog 097 outils economiques/financiers CE aju 139.352 CL 121.421 path +6.900; tick667",
    f"bud_do18_outils_eco_cl_aju_2026,wallonie_gov,2026,121421000,,,budgeted,{SRC},strong,Prog 097 outils eco CL aju 121.421m; tick667",
    f"bud_zae_ce_aju_2026,wallonie_gov,2026,83204000,,,budgeted,{SRC},strong,Prog 098 ZAE CE aju 83.204 CL 74.303 path +18.000/+5.000; tick667",
    f"bud_do18_entreprises_comp_ce_aju_2026,wallonie_gov,2026,56712000,,,budgeted,{SRC},strong,Prog 099 entreprises competitivite CE aju 56.712 CL 35.395 path +1.273/+0.625; tick667",
    f"bud_do18_fonds_structurels_cl_aju_2026,wallonie_gov,2026,30203000,,,budgeted,{SRC},strong,Prog 100 fonds structurels CL aju 30.203 CE 4.151 (new vs init 0); tick667",
    f"bud_do18_eco_sociale_aju_2026,wallonie_gov,2026,30212000,,,budgeted,{SRC},strong,Prog 104 economie sociale CE aju 30.212 CL 30.912 path -0.296; tick667",
    f"bud_do18_recherche_ce_aju_2026,wallonie_gov,2026,247509000,,,budgeted,{SRC},strong,Prog 114 recherche CE aju 247.509 CL 202.495 path 0/+3.400 exec 62.407; dual FWO; tick667",
    f"bud_do18_recherche_cl_aju_2026,wallonie_gov,2026,202495000,,,budgeted,{SRC},strong,Prog 114 recherche CL aju 202.495m; tick667",
    f"bud_do18_numerique_aju_2026,wallonie_gov,2026,35391000,,,budgeted,{SRC},strong,Prog 115 numerique CE aju 35.391 CL 24.970 path 0/-0.608; tick667",
    f"bud_do18_formation_agricole_ce_aju_2026,wallonie_gov,2026,2663000,,,budgeted,{SRC},strong,Prog 111 formation agricole CE aju 2.663 CL 1.300 path +2.663/0; tick667",
    # DO19
    f"bud_do19_dettes_garanties_aju_2026,wallonie_gov,2026,1915356000,,,budgeted,{SRC},strong,Prog 036 dettes et garanties CE=CL aju 1915.356m path +33.639 exec 29.770 (1.6pct); interest core; tick667",
    f"bud_do19_fiscalite_aju_2026,wallonie_gov,2026,6598000,,,budgeted,{SRC},strong,Prog 119 fiscalite CE=CL aju 6.598m path +0.422; tick667",
    f"bud_do19_budget_compta_aju_2026,wallonie_gov,2026,49725000,,,budgeted,{SRC},strong,Prog 034 budget-compta-tresorerie CE=CL aju 49.725m path +2.268; tick667",
    # DO15 residual sample
    f"bud_do15_aides_agri_aju_2026,wallonie_gov,2026,97532000,,,budgeted,{SRC},strong,Prog 058 aides agriculture CE aju 97.532 CL 97.533 path +4.207; tick667",
    f"bud_do15_dechets_path_plus_19m,wallonie_gov,2026,32501000,,,budgeted,{SRC},strong,Prog 064 dechets-ressources CE aju 32.501 path +19.222 (large path); tick667",
    f"bud_do15_kyoto_fonds_aju_2026,wallonie_gov,2026,158000000,,,budgeted,{SRC},strong,Prog 074 fonds Kyoto CE=CL aju 158.000m flat; tick667",
    f"bud_do15_env_fonds_ce_aju_2026,wallonie_gov,2026,71249000,,,budgeted,{SRC},strong,Prog 075 fonds protection env CE aju 71.249 CL 61.289 path -7.026; tick667",
    # AViQ residual ch7
    f"bud_aviq_rec_aju_exact_2026,aviq,2026,7007848000,,,budgeted,{SRC},strong,AViQ rec aju exact 7007848000 path +35.508m (+0.5pct); tick667",
    f"bud_aviq_dep_aju_exact_2026,aviq,2026,7523550000,,,budgeted,{SRC},strong,AViQ dep aju exact 7523550000 path +232.082m (+3.2pct); tick667",
    f"bud_aviq_result_aju_exact_2026,aviq,2026,-515702000,,,budgeted,{SRC},strong,AViQ result aju -515702000 path -196.574 vs init -319.128; tick667",
    f"bud_aviq_pivot_impact_13m,aviq,2026,13000000,,,budgeted,{SRC},strong,AViQ BFP pivot revision adverse impact est 13.0m on 2026 result (not in aju base); tick667",
    f"bud_aviq_nonmarchand_path_minus_5m,aviq,2026,-5000000,,,budgeted,{SRC},strong,AViQ non-marchand harmonisation salarial MR path -5.0m (sous-util creation emploi); tick667",
    f"bud_aviq_protection_soc_plus_194_7m,aviq,2026,194700000,,,budgeted,{SRC},strong,AViQ protection sociale wallonne path +194.7m (billing 14-month +198.1 dominant); tick667",
    f"bud_aviq_soins_etranger_minus_6_7m,aviq,2026,-6700000,,,budgeted,{SRC},strong,AViQ soins Wallons a l etranger path -6.7m (50pct rec N-1 update); tick667",
    f"bud_aviq_pnrr_internal_liq_20_8m,aviq,2026,20800000,,,budgeted,{SRC},strong,AViQ internal aju 4Jun2026 PNRR/PRW liq 20.8 eng 0.4; rec dot 13.6; SEC degrade 7.2 offset inexec; tick667",
    f"bud_forem_inst_total_aju_2026,forem,2026,3007400000,,,budgeted,{SRC},strong,Forem institutional CE=CL aju 3007.4m path +42.4 (macro +22.2 Job+ +31.9 aides -12.4); dual VDAB; tick667",
    f"bud_forem_jobplus_net_path_aju_2026,forem,2026,31900000,,,budgeted,{SRC},strong,Forem Job Plus path +31.9m offset aides -12.4m; RW line 2876; tick667",
    # financing residual detail
    f"bud_financing_need_total_2026,wallonie_gov,2026,3919400000,,,budgeted,{SRC},strong,Financing need 2026 3919.4m (amort 1101.9 + lease 18.9 + deficit 2798.6); tick667",
    f"bud_financing_raised_may2026,wallonie_gov,2026,3415000000,,,outturn,{SRC},strong,Raised by 31May2026 3415.0m + BEI 200 residual need 304.4 covered by tres sous-util 350; tick667",
    f"bud_interest_re_code21_aju_2026,wallonie_gov,2026,729100000,,,budgeted,{SRC},strong,Interest code21 RE aju 729.1 path +44.8 vs init 684.3; total charge 753.7; tick667",
    f"bud_interest_swaps_aju_2026,wallonie_gov,2026,11900000,,,budgeted,{SRC},strong,Swaps aju 11.9m path -2.6; tick667",
    f"bud_dette_indirecte_eoy2025,wallonie_gov,2025,10859000000,,,outturn,{SRC},strong,Dette indirecte ICN Apr2026 eoy2025 10859.0m; brute path eoy2026 43833; tick667",
]

cmt_rows = [
    f"cmt_cabinets_wal_matrix_aju2026,WAL cabinets full matrix 28.0m dual VL,wallonie_gov,8 ministerial cabinets,CoA aju2026 Annex DO02,2026-06-11,2026,2026,28043000,\"{{\"\"2026\"\":28043000}}\",,active,,Political cabinets overhead,Compare VL cabinets,{SRC},strong,Wallonie>DO02>cabinets,MP 5.4 Eco 5.3 Terr 5.1 dual; tick667",
    f"cmt_prw_frr_cl_1_73bn_aju2026,PRW+FRR CL 1.734bn path +342m dual RRF,wallonie_gov,PRW FRR projects,CoA aju2026 Annex prog122,2026-06-11,2026,2026,1734091000,\"{{\"\"2026\"\":1734091000}}\",,active,,Relance liquidations,Exec only 4.4pct May,{SRC},strong,Wallonie>DO10>PRW_FRR,Specialty redistrib risk dual; tick667",
    f"cmt_do17_dot_sante_7_05bn_aju2026,DO17 dot sante 7.05bn dual VAPH,aviq,AViQ channel,CoA aju2026 Annex prog093,2026-06-11,2026,2026,7049370000,\"{{\"\"2026\"\":7049370000}}\",,active,,Health social dual,L5 FOI,{SRC},strong,Wallonie>DO17>sante,Exec 5.74bn May; dual; tick667",
    f"cmt_awex_76_8m_aju2026,AWEX commerce exterieur 76.8m dual FIT,awex,AWEX,CoA aju2026 Annex prog020,2026-06-11,2026,2026,76843000,\"{{\"\"2026\"\":76843000}}\",,active,,Export promo dual,Compare FIT VL,{SRC},strong,Wallonie>DO09>AWEX,Exec 99.7pct; tick667",
    f"cmt_do19_dettes_1_92bn_aju2026,DO19 dettes garanties 1.915bn dual,wallonie_gov,Debt service,CoA aju2026 Annex prog036,2026-06-11,2026,2026,1915356000,\"{{\"\"2026\"\":1915356000}}\",,active,,Debt charges,Moody Baa1 context,{SRC},strong,Wallonie>DO19>dettes,Path +33.6m; tick667",
    f"cmt_dual_aju2026_annex_prog,Dual aju2026 annex prog cabinets PRW sante vs VL,gg_belgium,BE dual L4,CoA aju2026 dual,2026-06-11,2026,2026,7049370000,\"{{\"\"2026\"\":7049370000}}\",,active,,Dual Entity II,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>aju2026_annex,tick667",
]

lb_rows = [
    f"lb_cabinets_wal_28m_2026,WAL cabinets DO02 28.0m dual VL,Wallonia,ops,Wallonie>DO02>cabinets,28043000,0,Strong CoA annex: 8 cabinets MP 5.4 Eco 5.3 Terr 5.1; exec 24.8pct May; dual VL,strong,{SRC},ministerial staff,Political overhead,Primary,7.0,5.5,2,5.95,Publish FTE+comms split,open,,tick667",
    f"lb_prw_frr_cl_1_73bn_2026,PRW+FRR CL 1.734bn path +342m,Wallonia,ops,Wallonie>DO10>PRW_FRR,1734091000,0,Strong CoA: CL path +342m exec only 77m May (4.4pct); specialty redistrib dual RRF VL,strong,{SRC},PRW projects,Relance opacity,Primary,7.5,8.5,3,7.15,List projects >5m,open,,tick667",
    f"lb_do17_dot_sante_7_05bn_2026,DO17 dot sante/social 7.05bn dual VAPH,Wallonia,ops,Wallonie>DO17>sante,7049370000,0,Strong CoA prog093 CL 7049m path -13m exec 5737m; dual VAPH WVG,strong,{SRC},AViQ beneficiaries,Health dual,Primary,5.0,9.0,3,6.7,L5 FOI,open,,tick667",
    f"lb_awex_76_8m_2026,AWEX export promo 76.8m dual FIT,Wallonia,ops,Wallonie>DO09>AWEX,76843000,0,Strong CoA prog020 flat exec 99.7pct; dual FIT Flanders,strong,{SRC},exporters,Trade dual,Primary,6.0,6.0,2,5.6,Outcome metrics,open,,tick667",
    f"lb_do19_dettes_1_92bn_2026,DO19 dettes garanties 1.915bn,Wallonia,ops,Wallonie>DO19>dettes,1915356000,0,Strong CoA path +33.6m; interest charge 753.7; Moody Baa1 dual,strong,{SRC},bondholders,Debt service,Primary,5.5,8.5,2,6.45,Interest paid-accrued FOI,open,,tick667",
    f"lb_dual_aju2026_annex_prog_2026,Dual aju2026 annex cabinets PRW sante,Belgium,ops,Belgium>dual>aju2026_annex,7049370000,0,Strong dual: cabinets 28m PRW 1.73bn sante 7.05bn AWEX 76.8 vs VL; not TE-additive,strong,{SRC_DUAL},BE dual,Entity II dual L4,Primary dual,6.0,8.5,3,6.65,Cross FOI,open,,tick667",
]

foi_row = (
    f"{GAP},Wallonie>Aju2026>Annex_prog_L5,wallonie_gov,"
    "L5 split cabinets FTE/comms; PRW/FRR top projects CL 1.73bn; DO17 prog093 AViQ L5; AWEX outcomes; DO18 aides invest beneficiaries; AViQ pivot 13m + PNRR internal 20.8,"
    "CoA aju2026 Annex programme matrix strong tick667; L5 residual dual,"
    f"5,SPW Budget / Cabinets / AWEX / AViQ / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_cabinets_wal_matrix_aju2026|cmt_prw_frr_cl_1_73bn_aju2026|cmt_do17_dot_sante_7_05bn_aju2026,"
    f"lb_cabinets_wal_28m_2026|lb_prw_frr_cl_1_73bn_2026|lb_do17_dot_sante_7_05bn_2026,"
    f"{NOW},{NOW},tick667 CoA annex primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW aju 2026 (2026_26) Annex + ch.7

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / Cabinets / AWEX / AViQ / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Annex programmes aju 2026 (cabinets, PRW/FRR, DO17 sante, AWEX) L5

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Cabinets DO02 (28,043 mEUR): FTE et ventilation communication/consultance
   par cabinet (prog 004-011).
2. Prog 122 PRW+FRR CL 1.734,1 mEUR: liste des projets >5 mEUR liquidés/engagés
   2025-2026 et taux d'exécution au 30/06/2026.
3. Prog 093 dotations sante 7.049,4 mEUR: top 20 bénéficiaires / branches AViQ.
4. AWEX prog 020 (76,843 mEUR): indicateurs d'impact export 2024-2026.
5. Prog 096 aides investissement (CL 105,8 mEUR): top 30 bénéficiaires.
6. AViQ: impact pivot 13 mEUR (estimation BFP) et ajustement interne 4/06/2026
   (liq 20,8 mEUR PNRR/PRW).

Période: 2025-01-01 à 2027-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes agent
- Primary: CoA 2026_26 Annex pp.49-55 + ch.7 (tick667).
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **aju2026 Annex programme L5 matrix + cabinets 28m + PRW/FRR 1.73bn + DO17 sante 7.05bn**)
- Found (primary CoA 2026_26 Annex kEUR): **Cabinets** total **EUR28.043m** (MP **5.404** Eco **5.328** Terr **5.068** Sante **3.180** Energ/Agri **2.957** each Tour **1.593** FP **1.556**). **DO01:** Parlement **77.582** Mediateur **1.924** Cwape **9.380**. **DO09:** AWEX **76.843** (exec 99.7pct) Tourisme **68.669** RelExt **30.098** CESE **7.858** IWEPS **7.727** CeSEFFB **9.918/8.918**. **DO10 PRW/FRR CL EUR1.734bn** path **+EUR342.4m** exec May only **EUR77.0m** (4.4pct). **DO14:** transport **919.6/887.7** reseau **664.1/576.0** airports **84.5** sports CL **59.6**. **DO16:** log prive **337.9/342.0** public **120.4** Alliance EE **124.7**. **DO17:** aff int **2765/2470** **dot sante 7034/7049** action soc **358/349** creches **30.7/15.8**. **DO18:** aides inv **165.7/105.8** outils **139.4/121.4** ZAE **83.2** recherche **247.5/202.5** Forem **2876**. **DO19 dettes EUR1.915bn**. **AViQ:** pivot **-13m** non-marchand **-5** foreign care **-6.7** PNRR internal liq **20.8**; Forem inst **3007.4**. Dual VL. Strong CoA; L5 FOI.
- Wrote: entities (+cwape ceseffb iweps); budgets (+75); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@670 in 3 ticks; rq_116 deferred
"""


def main() -> None:
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
        f"tick{TICK} Annex prog L5 cabinets PRW/FRR 1.73bn DO17 sante 7.05bn AWEX dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,wallonie_gov,"
        f"Next residual: dual VL BO compare on cabinets/PRW or new CoA PDF (FWB aju / Flanders) or DO15/16 full L5 FOI-adjacent.,,"
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
