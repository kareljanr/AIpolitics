# -*- coding: utf-8 -*-
"""Tick 666: aju2026 full DO CE/CL matrix + SPW remun + Emploi Table13 + consol/OCPP residual — rq_657."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T08:15:00Z"
TICK = 666
RQ = "rq_657"
NEXT_RQ = "rq_658"
GAP = "gap_wal_aju2026_do_matrix_spw_emploi_l5"


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
        f"tick{TICK} DO matrix full CE/CL + SPW remun 740.8m + Emploi Table13 + OCPP/sous-util dual; "
        f"next {NEXT_RQ}; progress@670 in 4; rq_116 deferred"
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
        if out and not out[-1].endswith("\n") and text and not text.endswith("\n"):
            pass
        out.append(row)
        print(f"FOI add {key}")
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))


SRC = "src_ccrek_wal_aju2026_do_matrix"
SRC_DUAL = "src_dual_aju2026_do_matrix_tick666"

ent_rows = [
    "spw_support_do11,SPW Support DO11 personnel,SPW Support DO11 personnel immobilier,SPW DO11 support personnel dual VL,agency,wallonie_gov,fr,https://www.spw.wallonie.be,,,CoA aju2026 DO11 CE 926.2m CL 932.3m; prog031 personnel 816.4/816.1; DF031.005 remun 740.8m path +9.6; dual VL admin; tick666",
    "spw_digital_do12,SPW Digital DO12,SPW Digital DO12,SPW Digital DO12 dual Digitaal Vlaanderen,agency,wallonie_gov,fr,https://www.spw.wallonie.be,,,CoA aju2026 DO12 CE 79.0m CL 72.9m; prov digital +10/+3.5 no master plan dual Digitaal VL; tick666",
]

src_rows = [
    f"{SRC},CoA Budget RW aju2026 full DO CE/CL matrix + SPW remun + Emploi Table13 + OCPP/sous-util dual,https://www.ccrek.be/sites/default/files/Docs/2026_26_BudgetRW_2026_AJU.pdf,Cour des comptes Belgique,2026-08-01,audit,"
    "Strong tick666: Table DO aju CE 21452.9 CL 21937.9 path +276.5/+602.2; DO01 88.9 DO02 28.0 DO09 215.2/213.4 DO10 464.2/1755.6 DO11 926.2/932.3 DO12 79.0/72.9 DO14 1843.8/1696.1 DO15 634.6/598.6 DO16 861.0/845.5 DO17 10194.6/9890.9 DO18 3913.1/3760.3 DO19 2018.7/2025.2 DO36 185.6/30.2; encours May 8926.7 exec 51.9pct; prog031 remun DF031.005 740.8 (+9.6 from 731.2) postal +2.4 Cap Sud +5.0 prov interdep 0.8 (-7.4) pilier2 pension reaff; digital prov +10/+3.5 no plan; pivot impact 24.8 dep 2021-25 +13.1pct +2291.4 2026 +2.6 +518.1; Table13 emploi 101 72.8 108 27.1 109 31.3 112 88.3 113 30.7/18.9 130 2876 total 3126.2/3114.3 path +43.6; OCPP dep 859.6 rec 745.1 impact 273.2 margin 65.9 eff 49.5; sous-util 524 vs inexec2025 891.2; consol -180.1 units -486.5 FA 111.6; OPW -6.8 Tourisme -5.9 AWAP -4.7 Sp aque -5.4 OTW +97.1 Sowaer +24 SWL -23.8; type3 -18.5 path +91.9; solde net -2798.6; interest payes-courus missing 2025 -67.9; macro June SEC +98.7; wage mod gain 0.756; index residual 1.0",
    f"{SRC_DUAL},Dual aju2026 DO matrix SPW remun Emploi OCPP vs VL dual,https://www.ccrek.be/sites/default/files/Docs/2026_26_BudgetRW_2026_AJU.pdf,DOGE synthesis CoA aju2026 dual VL,2026-08-01,synthesis,"
    "Strong dual: DO17 9.89bn DO18 3.76bn SPW remun 740.8m digital opacity dual Digitaal VL Forem/VDAB; not TE-additive; tick666",
]

# amounts in EUR (tables in kEUR or mEUR as noted)
bud_rows = [
    # --- Full DO matrix aju CE/CL (from CoA p32 table) ---
    f"bud_do_total_ce_aju_2026,wallonie_gov,2026,21452905000,,,budgeted,{SRC},strong,Total CE aju 21452.905m path +276.505 (+1.3pct) vs init 21176.4; tick666",
    f"bud_do_total_cl_aju_2026,wallonie_gov,2026,21937935000,,,budgeted,{SRC},strong,Total CL aju 21937.935m path +602.187 (+2.8pct) vs init 21335.748; tick666",
    f"bud_do_total_ce_init_2026,wallonie_gov,2026,21176400000,,,budgeted,{SRC},strong,Total CE init 21176.4m; tick666",
    f"bud_do_total_cl_init_2026,wallonie_gov,2026,21335748000,,,budgeted,{SRC},strong,Total CL init 21335.748m; tick666",
    f"bud_do_total_exec_cl_may2026,wallonie_gov,2026,11066315000,,,outturn,{SRC},strong,CL exec 18May 11066.315m = 51.9pct of aju CL; tick666",
    f"bud_do01_ce_aju_2026,parlement_wallonie,2026,88886000,,,budgeted,{SRC},strong,DO01 Parlement CE=CL aju 88.886m path +1.482; exec 56.431 (64.6pct) encours 30.973; tick666",
    f"bud_do01_cl_aju_2026,parlement_wallonie,2026,88886000,,,budgeted,{SRC},strong,DO01 Parlement CL aju 88.886m; tick666",
    f"bud_do02_ce_aju_2026,wallonie_gov,2026,28043000,,,budgeted,{SRC},strong,DO02 cabinets CE=CL aju 28.043m flat; exec 6.942 (24.8pct) encours 3.451; tick666",
    f"bud_do02_cl_aju_2026,wallonie_gov,2026,28043000,,,budgeted,{SRC},strong,DO02 cabinets CL aju 28.043m; tick666",
    f"bud_do09_ce_aju_2026,wallonie_gov,2026,215151000,,,budgeted,{SRC},strong,DO09 services GW + organismes non rattaches CE aju 215.151m path +3.956; tick666",
    f"bud_do09_cl_aju_2026,wallonie_gov,2026,213392000,,,budgeted,{SRC},strong,DO09 CL aju 213.392m path +2.215 exec 143.773 (68.1pct) encours 75.997; tick666",
    f"bud_do10_ce_aju_2026,wallonie_gov,2026,464198000,,,budgeted,{SRC},strong,DO10 Secretariat general CE aju 464.198m path +20.229; CL heavy FRR/PRW; tick666",
    f"bud_do10_cl_path_aju_2026,wallonie_gov,2026,1755613000,,,budgeted,{SRC},strong,DO10 CL aju 1755.613m path +344.238 vs init 1411.375; exec only 5.7pct encours 1587.701; tick666",
    f"bud_do11_ce_aju_2026,spw_support_do11,2026,926202000,,,budgeted,{SRC},strong,DO11 Support CE aju 926.202m path +8.660; tick666",
    f"bud_do11_cl_aju_2026,spw_support_do11,2026,932264000,,,budgeted,{SRC},strong,DO11 Support CL aju 932.264m path +13.525 exec 279.736 (30.4pct) encours 131.990; tick666",
    f"bud_do12_ce_aju_2026,spw_digital_do12,2026,79026000,,,budgeted,{SRC},strong,DO12 Digital CE aju 79.026m path +9.977; tick666",
    f"bud_do12_cl_aju_2026,spw_digital_do12,2026,72917000,,,budgeted,{SRC},strong,DO12 Digital CL aju 72.917m path +3.477 exec 15.272 (22.0pct) encours 41.680; tick666",
    f"bud_do14_ce_aju_2026,wallonie_gov,2026,1843797000,,,budgeted,{SRC},strong,DO14 Mobilite CE aju 1843.797m path -7.743; tick666",
    f"bud_do14_cl_aju_2026,wallonie_gov,2026,1696070000,,,budgeted,{SRC},strong,DO14 CL aju 1696.070m path +34.239 exec 837.520 (50.4pct) encours 1326.853; tick666",
    f"bud_do15_ce_aju_2026,wallonie_gov,2026,634569000,,,budgeted,{SRC},strong,DO15 Agri RN env CE aju 634.569m path +14.980; tick666",
    f"bud_do15_cl_aju_2026,wallonie_gov,2026,598624000,,,budgeted,{SRC},strong,DO15 CL aju 598.624m path +28.440 exec 113.076 (19.8pct) encours 526.173; tick666",
    f"bud_do16_ce_aju_2026,wallonie_gov,2026,860989000,,,budgeted,{SRC},strong,DO16 ATelier logement energie CE aju 860.989m path +13.205; tick666",
    f"bud_do16_cl_aju_2026,wallonie_gov,2026,845541000,,,budgeted,{SRC},strong,DO16 CL aju 845.541m path +18.955 exec 154.520 (18.7pct) encours 693.570; tick666",
    f"bud_do17_ce_aju_2026,wallonie_gov,2026,10194648000,,,budgeted,{SRC},strong,DO17 Pouvoirs locaux action sociale sante CE aju 10194.648m path +131.649; tick666",
    f"bud_do17_cl_path_aju_2026,wallonie_gov,2026,9890876000,,,budgeted,{SRC},strong,DO17 CL aju 9890.876m path +103.115 exec 7221.867 (73.8pct) encours 2130.121; tick666",
    f"bud_do18_ce_aju_2026,wallonie_gov,2026,3913087000,,,budgeted,{SRC},strong,DO18 Entreprises emploi recherche CE aju 3913.087m path +80.694; tick666",
    f"bud_do18_cl_path_aju_2026,wallonie_gov,2026,3760283000,,,budgeted,{SRC},strong,DO18 CL aju 3760.283m path +104.766 exec 2115.556 (57.9pct) encours 2322.940; tick666",
    f"bud_do19_ce_aju_2026,wallonie_gov,2026,2018720000,,,budgeted,{SRC},strong,DO19 Finances CE aju 2018.720m path +37.461 (interest/debt service); tick666",
    f"bud_do19_cl_aju_2026,wallonie_gov,2026,2025213000,,,budgeted,{SRC},strong,DO19 CL aju 2025.213m path +37.462 exec 40.685 (2.0pct) encours 55.282; tick666",
    f"bud_do36_ce_aju_2026,wallonie_gov,2026,185589000,,,budgeted,{SRC},strong,DO36 EU cofin 2021-27 CE aju 185.589m path -38.045; tick666",
    f"bud_do36_cl_aju_2026,wallonie_gov,2026,30213000,,,budgeted,{SRC},strong,DO36 CL aju 30.213m path -89.727 exec 0; tick666",
    # --- DO11 personnel residual ---
    f"bud_do11_prog031_ce_aju_2026,spw_support_do11,2026,816400000,,,budgeted,{SRC},strong,Prog 11.031 personnel CE aju 816.4m path +5.1; tick666",
    f"bud_spw_remun_df031005_aju_2026,spw_support_do11,2026,740800000,,,budgeted,{SRC},strong,DF031.005 remun SPW aju 740.8m path +9.6 from init 731.2; indexation + transfers 4.8; tick666",
    f"bud_spw_remun_init_2026,spw_support_do11,2026,731200000,,,budgeted,{SRC},strong,DF031.005 remun SPW init 731.2m; tick666",
    f"bud_do11_prov_interdep_aju_2026,spw_support_do11,2026,800000,,,budgeted,{SRC},strong,DF031.001 prov interdep aju 0.8m path -7.4 (transfers 2.5 + aju -4.9); pilier2 pension reallocated to encours; tick666",
    f"bud_do11_postal_plus_2_4m,spw_support_do11,2026,2400000,,,budgeted,{SRC},strong,DF001.107 postal arrears 2025 covered from prov +2.4m + redistrib 0.9 total DF +3.3; tick666",
    f"bud_do11_capsud_liq_plus_5m,spw_support_do11,2026,5000000,,,budgeted,{SRC},strong,DF001.112 Cap Sud admin buildings final invoices liq +5.0m; tick666",
    f"bud_moderation_salariale_gain_0_756m,spw_support_do11,2026,756000,,,budgeted,{SRC},strong,Federal wage-moderation special SSC not applied to regional admins: gain 189k/mo x4 = 0.756m Sep-Dec 2026; tick666",
    f"bud_index_residual_1m_uncounted,spw_support_do11,2026,1000000,,,budgeted,{SRC},strong,Index advance Oct->Sep 2026 cost 1.0m not in aju (admin est); first index Mar +1.1 second Sep +3.4 integrated; tick666",
    f"bud_wal_index_pivot_impact_dep_24_8m,wallonie_gov,2026,24800000,,,budgeted,{SRC},strong,Cabinet Budget: pivot param revision adverse dep impact 24.8m (BFP May/Jun); tick666",
    f"bud_wal_dep_growth_2021_2025,wallonie_gov,2025,2291400000,,,outturn,{SRC},strong,Dep growth 2021-2025 +13.1pct = +2291.4m (ex amort SP sous-util); tick666",
    f"bud_wal_dep_path_2026_vs_2025,wallonie_gov,2026,518100000,,,budgeted,{SRC},strong,Aju2026 dep vs provisional 2025 exec +2.6pct = +518.1m; level 20293.1m graph; tick666",
    # --- Emploi Table13 programme split ---
    f"bud_emploi_101_ce_aju_2026,wallonie_gov,2026,72800000,,,budgeted,{SRC},strong,Prog 101 promotion emploi CE aju 72.8 CL 72.5 (init 72.0/71.7); tick666",
    f"bud_emploi_101_cl_aju_2026,wallonie_gov,2026,72500000,,,budgeted,{SRC},strong,Prog 101 CL aju 72.5m; tick666",
    f"bud_emploi_108_ce_aju_2026,wallonie_gov,2026,27100000,,,budgeted,{SRC},strong,Prog 108 emplois de proximite CE=CL aju 27.1 (init 26.7); tick666",
    f"bud_emploi_109_ce_aju_2026,wallonie_gov,2026,31300000,,,budgeted,{SRC},strong,Prog 109 formation pro CE aju 31.3 CL 31.5; tick666",
    f"bud_emploi_112_ifapme_ce_aju_2026,ifapme,2026,88300000,,,budgeted,{SRC},strong,Prog 112 IFAPME CE=CL aju 88.3m flat; dual Syntra VL; tick666",
    f"bud_emploi_113_ce_aju_2026,wallonie_gov,2026,30700000,,,budgeted,{SRC},strong,Prog 113 politiques croisees CE aju 30.7 CL 18.9; tick666",
    f"bud_emploi_113_cl_aju_2026,wallonie_gov,2026,18900000,,,budgeted,{SRC},strong,Prog 113 CL aju 18.9m; tick666",
    f"bud_emploi_macro_param_plus_22_1m,wallonie_gov,2026,22100000,,,budgeted,{SRC},strong,Emploi pack macro param adjust +22.1m (Forem 21.1 + 101 0.8 + 108 0.4 + 109 0.1); tick666",
    f"bud_ape_creches_plus_2_1m,wallonie_gov,2026,2100000,,,budgeted,{SRC},strong,APE DF130.006 +2.1m creche places Plan Cigogne; tick666",
    f"bud_cisp_plus_2_8m_aju_2026,wallonie_gov,2026,2800000,,,budgeted,{SRC},strong,CISP DF130.016 +2.8m reform failed to deliver expected savings; tick666",
    # --- OCPP / sous-util / consol residual ---
    f"bud_ocpp_dep_aju_2026,wallonie_gov,2026,859600000,,,budgeted,{SRC},strong,OCPP dep aju 859.6m path +148.1; tick666",
    f"bud_ocpp_rec_aju_2026,wallonie_gov,2026,745100000,,,budgeted,{SRC},strong,OCPP rec aju 745.1m path +175.5; tick666",
    f"bud_ocpp_budget_solde_aju_2026,wallonie_gov,2026,114500000,,,budgeted,{SRC},strong,OCPP budget solde aju 114.5m path -27.4; tick666",
    f"bud_ocpp_gw_corr_aju_2026,wallonie_gov,2026,224600000,,,budgeted,{SRC},strong,OCPP GW corrections aju 224.6m (Kyoto 133.4 env 5.0 EU 13.8 Renopack 72.4); tick666",
    f"bud_ocpp_after_corr_aju_2026,wallonie_gov,2026,339000000,,,budgeted,{SRC},strong,OCPP after GW corr aju 339.0m; tick666",
    f"bud_ocpp_impact_expose_aju_2026,wallonie_gov,2026,273200000,,,budgeted,{SRC},strong,OCPP impact expose general aju 273.2m path -9.8; tick666",
    f"bud_ocpp_margin_aju_2026,wallonie_gov,2026,65900000,,,budgeted,{SRC},strong,OCPP requalif margin aju 65.9m (ICN already 16.4 -> effective 49.5); tick666",
    f"bud_ocpp_margin_eff_aju_2026,wallonie_gov,2026,49500000,,,budgeted,{SRC},strong,OCPP effective safety margin aju 49.5m after ICN 16.4; tick666",
    f"bud_sous_util_sg_aju_2026,wallonie_gov,2026,524000000,,,budgeted,{SRC},strong,Sous-utilisation services gov aju 524.0m (2.4pct CL) path -85 vs init 609; tick666",
    f"bud_sous_util_uap_aju_2026,wallonie_gov,2026,187900000,,,budgeted,{SRC},strong,Sous-util UAP institutions aju 187.9m in SEC hyp; tick666",
    f"bud_inexec_2025_provisoire,wallonie_gov,2025,891200000,,,outturn,{SRC},strong,Inexecution credits 2025 provisional 891.2m (4.0pct CL; dissoc 826.9 var 64.3); tick666",
    f"bud_solde_net_financer_aju_2026,wallonie_gov,2026,-2798600000,,,budgeted,{SRC},strong,Solde net a financer aju -2798.6m path +12.5 vs init -2811.1; amort understate 10m; tick666",
    f"bud_solde_brut_aju_2026,wallonie_gov,2026,150000000,,,budgeted,{SRC},strong,Solde budg brut aju +150.0m flat (rec 22087.9 - dep 21937.9); tick666",
    f"bud_consol_inst_sec_aju_2026,wallonie_gov,2026,-180100000,,,budgeted,{SRC},strong,Solde institutions consol aju -180.1m path +74.0; tick666",
    f"bud_type_units_sec_aju_2026,wallonie_gov,2026,-486500000,,,budgeted,{SRC},strong,Unites institutionnelles SEC aju -486.5m path +75.8; tick666",
    f"bud_type1_sec_aju_2026,wallonie_gov,2026,-153200000,,,budgeted,{SRC},strong,Organismes type1 SEC aju -153.2m path -5.6; tick666",
    f"bud_type2_sec_aju_2026,wallonie_gov,2026,-27000000,,,budgeted,{SRC},strong,Organismes type2 SEC aju -27.0m path -0.5; tick666",
    f"bud_type3_sec_aju_2026,wallonie_gov,2026,-18500000,,,budgeted,{SRC},strong,Organismes type3 SEC aju -18.5m path +91.9 (largest consol improvement); tick666",
    f"bud_saca_sec_aju_2026,wallonie_gov,2026,-28400000,,,budgeted,{SRC},strong,SACA SEC aju -28.4m path -11.5; tick666",
    f"bud_fa_missions_sec_aju_2026,wallonie_gov,2026,111600000,,,budgeted,{SRC},strong,Financement alternatif + missions deleguees SEC +111.6m path -18.7 vs init 130.3; tick666",
    f"bud_otw_sec_path_plus_97_1m,otw,2026,97100000,,,budgeted,{SRC},strong,OTW SEC path +97.1m (capital spend cut); tick666",
    f"bud_opw_sec_path_minus_6_8m,opw,2026,-6800000,,,budgeted,{SRC},strong,OPW SEC path -6.8m (EU interest repay + Feader non-reimb); tick666",
    f"bud_awap_sec_path_minus_4_7m,wallonie_gov,2026,-4700000,,,budgeted,{SRC},strong,AWAP SEC path -4.7m objective corr to budget; tick666",
    f"bud_tourisme_sec_path_minus_5_9m,wallonie_gov,2026,-5900000,,,budgeted,{SRC},strong,Wallonie Tourisme SEC path -5.9m; tick666",
    f"bud_spaque_sec_path_minus_5_4m,wallonie_gov,2026,-5400000,,,budgeted,{SRC},strong,Groupe Spaque SEC path -5.4m (invest +3.5 dot -5.5 Erpion +2); tick666",
    f"bud_autres_corr_sec_aju_2026,wallonie_gov,2026,166200000,,,budgeted,{SRC},strong,Autres corrections SEC aju 166.2m path +8.8 (hospital past +10.2 green cert -1.9); tick666",
    f"bud_interets_payes_courus_2025,wallonie_gov,2025,-67900000,,,outturn,{SRC},strong,Interest paid vs accrued SEC corr 2025 -67.9m (prov ICN Apr2026); missing in 2026 aju; tick666",
    f"bud_macro_june_sec_impact_98_7m,wallonie_gov,2026,98700000,,,budgeted,{SRC},strong,If June 2026 macro params applied: rec +123.5 dep -24.8 SEC impact +98.7m; tick666",
    f"bud_dep_hors_sp_sousutil_aju_2026,wallonie_gov,2026,20303000000,,,budgeted,{SRC},strong,Dep hors SP emprunts after sous-util 524 = 20303.0m; rec after UAP tres 460.7 = 17567.7; gap 2735.3; tick666",
    f"bud_rec_hors_sp_tres_aju_2026,wallonie_gov,2026,17567700000,,,budgeted,{SRC},strong,Recettes hors SP emprunts after UAP tresor mobilisation 460.7 = 17567.7m; tick666",
    f"bud_uap_tresorerie_aju_2026,wallonie_gov,2026,460700000,,,budgeted,{SRC},strong,UAP tresorerie mobilisation aju 460.7m (init 440.7 path +20); dual prior years 69.5-707m; tick666",
    f"bud_credits_dissoc_ce_aju_2026,wallonie_gov,2026,21047084000,,,budgeted,{SRC},strong,Credits dissoc CE aju 21047.084m path +280.820; tick666",
    f"bud_credits_var_ce_aju_2026,wallonie_gov,2026,405821000,,,budgeted,{SRC},strong,Credits variables CE aju 405.821m path -4.315; tick666",
    f"bud_credits_dissoc_cl_aju_2026,wallonie_gov,2026,21547044000,,,budgeted,{SRC},strong,Credits dissoc CL aju 21547.044m path +609.092; tick666",
    f"bud_credits_var_cl_aju_2026,wallonie_gov,2026,390891000,,,budgeted,{SRC},strong,Credits variables CL aju 390.891m path -6.905; tick666",
    f"bud_encours_potential_reduce_2026,wallonie_gov,2026,485000000,,,budgeted,{SRC},strong,Potential encours reduce 2026: CE-CL gap -485.0m (CL>CE); eoy2025 encours 5937.1; tick666",
]

cmt_rows = [
    f"cmt_do_matrix_aju2026,WAL aju2026 full DO CE/CL matrix dual VL,wallonie_gov,WAL DO stack,CoA 2026_26 ch5.4,2026-06-11,2026,2026,21937935000,\"{{\"\"2026\"\":21937935000}}\",,active,,Map all DO spend aju,FOI L5 residual,{SRC},strong,Wallonie>DO>aju2026,Table DO: DO17 9.89bn DO18 3.76bn DO10 1.76bn DO14 1.70bn DO19 2.03bn DO11 0.93bn; dual VL; tick666",
    f"cmt_spw_remun_740m_aju2026,SPW remun DF031.005 740.8m dual VL admin,spw_support_do11,SPW staff,CoA aju2026 5.4.1,2026-06-11,2026,2026,740800000,\"{{\"\"2026\"\":740800000}}\",,active,,SPW wage bill,Audit index + pilier2 reaff,{SRC},strong,Wallonie>DO11>remun,Path +9.6m; pilier2 pension credits reallocated to postal/building encours; dual; tick666",
    f"cmt_digital_prov_no_plan_aju2026,DO12 digital provision no master plan dual Digitaal VL,spw_digital_do12,SPW Digital,CoA aju2026 5.4.2,2026-06-11,2026,2026,10000000,\"{{\"\"2026\"\":10000000}}\",,active,,Central IT provision,Require master plan before spend,{SRC},strong,Wallonie>DO12>digital_prov,IF + CoA: no plan directeur; only MI transfer confirmed; dual Digitaal VL; tick666",
    f"cmt_emploi_table13_aju2026,Emploi-formation Table13 pack 3.13bn dual VDAB,wallonie_gov,Forem IFAPME pack,CoA aju2026 Table13,2026-06-11,2026,2026,3126200000,\"{{\"\"2026\"\":3126200000}}\",,active,,Emploi pack L4,L5 split FOI,{SRC},strong,Wallonie>DO18>emploi,80pct DO18 / 15pct WAL dep; dual VDAB; tick666",
    f"cmt_ocpp_sousutil_aju2026,OCPP 273m + sous-util 524m dual SEC hygiene,wallonie_gov,WAL SEC corrections,CoA aju2026 2.2.3,2026-06-11,2026,2026,524000000,\"{{\"\"2026\"\":524000000}}\",,active,,SEC assumptions,Compare inexec 891m 2025,{SRC},strong,Wallonie>SEC>ocpp_sousutil,Margin eff 49.5m; interest payes-courus missing; tick666",
    f"cmt_dual_aju2026_do_matrix,Dual aju2026 DO matrix SPW Emploi OCPP vs VL,gg_belgium,BE dual DO stacks,CoA aju2026 dual,2026-06-11,2026,2026,21937935000,\"{{\"\"2026\"\":21937935000}}\",,active,,Dual Entity II map,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>aju2026_do,DO17/18 + remun + digital dual; tick666",
]

lb_rows = [
    f"lb_do17_social_sante_9_89bn_2026,DO17 pouvoirs locaux action sociale sante CL 9.89bn,Wallonia,ops,Wallonie>DO17,9890876000,0,Strong CoA aju CL 9890.876m path +103m exec 73.8pct encours 2.13bn; dual VL WVG,strong,{SRC},communes+AViQ channel,Local social health stack,Primary table only,5.5,9.0,3,6.85,FOI L5 split communes/AViQ/sante,open,,tick666 primary CoA DO matrix",
    f"lb_do18_emploi_3_76bn_2026,DO18 entreprises emploi recherche CL 3.76bn,Wallonia,ops,Wallonie>DO18,3760283000,0,Strong CoA aju CL 3760.283m path +105m; emploi pack 3.13bn ~80pct; dual VDAB,strong,{SRC},Forem IFAPME firms,Employment dual PES,Primary table,5.5,8.5,3,6.55,L5 Job+ APE CISP FOI,open,,tick666",
    f"lb_spw_remun_740m_2026,SPW remun DF031.005 740.8m,Wallonia,ops,Wallonie>DO11>remun,740800000,0,Strong CoA path +9.6m; pilier2 pension reallocated to postal/building arrears; dual VL,strong,{SRC},SPW staff,Admin wage bill,Primary,6.5,7.5,2,6.55,Publish pilier2 status + FTE,open,,tick666",
    f"lb_digital_prov_no_plan_10m_2026,DO12 digital provision 10m no master plan,Wallonia,ops,Wallonie>DO12>digital_prov,10000000,0,Strong CoA+IF: no plan directeur; specialty risk dual Digitaal VL,strong,{SRC},SPW Digital,IT provision opacity,Primary,8.0,5.0,2,6.4,Block until master plan,open,,tick666",
    f"lb_ocpp_sousutil_524m_2026,Sous-util 524m vs inexec 891m 2025 dual,Wallonia,ops,Wallonie>SEC>sousutil,524000000,0,Strong CoA: aju hyp 524 (2.4pct) vs 2025 inexec 891 (4.0pct); OCPP impact 273 margin eff 49.5; interest payes-courus missing,strong,{SRC},WAL SEC,SEC optimism risk,Primary,7.5,7.0,3,6.85,Disclose interest accrued corr,open,,tick666",
    f"lb_dual_aju2026_do_matrix_2026,Dual aju2026 DO matrix SPW Emploi OCPP,Belgium,ops,Belgium>dual>aju2026_do,21937935000,0,Strong dual: DO CL 21.94bn remun 741m digital opacity emploi 3.13bn vs VL; not TE-additive,strong,{SRC_DUAL},BE dual,Entity II dual map,Primary dual,6.0,8.5,3,6.65,Cross-entity L5 FOI,open,,tick666",
]

foi_row = (
    f"{GAP},Wallonie>Aju2026>DO_matrix_SPW_emploi_L5,wallonie_gov,"
    "Full DO L5 beneficiary split DO17/18/10/14; SPW remun FTE+pilier2 pension status; digital provision project list+plan directeur; OCPP ICN 16.4 list; interest payes-courus 2026 estimate; emploi L5 Job+/APE/CISP outturn,"
    "CoA aju2026 DO matrix SPW Emploi OCPP strong tick666; L5 residual dual VL,"
    f"5,SPW Budget / SPW Digital / SPW Personnel / Forem / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_do_matrix_aju2026|cmt_spw_remun_740m_aju2026|cmt_digital_prov_no_plan_aju2026,"
    f"lb_do17_social_sante_9_89bn_2026|lb_spw_remun_740m_2026|lb_digital_prov_no_plan_10m_2026,"
    f"{NOW},{NOW},tick666 CoA aju2026 DO matrix primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW aju 2026 (2026_26) ch.2 + ch.5.4 Table DO + Table13

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / SPW Digital / SPW Personnel / Forem / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — matrice DO aju 2026, rémunérations SPW, provision digital, OCPP/SEC L5

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Ventilation L5 des crédits DO17 (CL 9.890,9 mEUR) et DO18 (CL 3.760,3 mEUR)
   aju 2026: top 50 bénéficiaires / domaines fonctionnels > 5 mEUR.
2. DF 031.005 rémunérations SPW 740,8 mEUR: effectifs FTE, indexation détail,
   statut du 2e pilier de pension (crédits réaffectés vers encours postaux/immobilier).
3. Provision digitale DF 029.041 (+10 mEUR eng / +3,5 mEUR liq): liste des projets
   et plan directeur informatique SPW Digital validé par le GW (ou confirmation d'absence).
4. OCPP: détail des 16,4 mEUR déjà requalifiés ICN et composition marge 49,5 mEUR.
5. Estimation 2026 de la correction intérêts payés vs courus (2025: −67,9 mEUR).
6. Emploi Table13: outturn Job+ 32 mEUR, APE +2,1 mEUR, CISP +2,8 mEUR
   (bénéficiaires / heures) au 30/06/2026.

Période: 2025-01-01 à 2027-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes agent
- Primary: CoA 2026_26 pages 9-15 + 29-41 (tick666).
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual fiscal residual -- **aju2026 full DO CE/CL matrix + SPW remun 740.8m + Emploi Table13 + OCPP/sous-util**)
- Found (primary CoA 2026_26): **DO total** CE **EUR21.453bn** / CL **EUR21.938bn** path **+276.5 / +602.2**; exec May **51.9%** encours **EUR8.927bn**. Matrix: **DO17 CL EUR9.891bn** / **DO18 EUR3.760bn** / **DO19 EUR2.025bn** / **DO10 EUR1.756bn** / **DO14 EUR1.696bn** / **DO11 EUR0.932bn** / DO16 0.846 / DO15 0.599 / DO09 0.213 / DO12 0.073 / DO01 0.089 / DO02 0.028 / DO36 0.030. **SPW remun** DF031.005 **EUR740.8m** (+9.6 from 731.2); postal **+2.4**; Cap Sud **+5.0**; prov interdep **0.8** (−7.4; **pilier2 pension reaff**); wage-mod gain **EUR0.756m**; index residual **EUR1.0m** uncounted; pivot dep **EUR24.8m**. **Digital** prov **+10/+3.5** no master plan (IF+CoA). **Emploi Table13:** 101 **72.8** / 108 **27.1** / 109 **31.3** / IFAPME **88.3** / 113 **30.7/18.9** / Forem **2876** total **3126.2/3114.3** path **+43.6**; APE **+2.1** CISP **+2.8**. **OCPP** impact **273.2** margin eff **49.5**; sous-util **524** vs inexec2025 **891.2**; consol **−180.1** (OTW **+97.1** Sowaer **+24** SWL **−23.8** type3 **−18.5** path **+91.9**); interest payes-courus missing (2025 **−67.9**); macro June SEC **+98.7**. Dual VL Digitaal/VDAB/WVG. Strong confidence CoA; L5 residual FOI.
- Wrote: entities (+spw_support_do11 spw_digital_do12); budgets (+70); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@670 in 4 ticks; rq_116 deferred
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
        f"tick{TICK} DO matrix full CE/CL SPW remun 740.8m Emploi Table13 OCPP/sous-util dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,wallonie_gov,"
        f"Next residual after aju2026 DO matrix: ch7 perimeter UAP detail beyond AViQ/Forem/OTW or dual VL compare or new CoA PDF.,,"
        f"{NOW},,spawned tick{TICK} after {RQ}",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log = read_text(LOG)
    if f"tick {TICK}" not in log[-2000:]:
        if not log.endswith("\n"):
            log += "\n"
        log += log_entry
        LOG.write_bytes(log.encode("utf-8"))
        print("LOG appended")
    else:
        print("LOG skip duplicate")

    print(
        f"DONE tick{TICK}: ent={n_ent} src={n_src} bud={n_bud} cmt={n_cmt} lb={n_lb}"
    )


if __name__ == "__main__":
    main()
