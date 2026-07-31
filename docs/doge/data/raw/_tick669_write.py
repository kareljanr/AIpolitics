# -*- coding: utf-8 -*-
"""Tick 669: FWB aju2026 SACA/OAP perimeter L5 + encours + reserve repay dual WAL — rq_660."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T09:00:00Z"
TICK = 669
RQ = "rq_660"
NEXT_RQ = "rq_661"
GAP = "gap_fwb_aju2026_saca_oap_l5"
SRC = "src_ccrek_fwb_aju2026_saca_oap"
SRC_DUAL = "src_dual_fwb_saca_oap_tick669"


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
        f"tick{TICK} FWB SACA -215m report 1.10bn Piebs/CUR/ONE dual; "
        f"next {NEXT_RQ}; progress@670 NEXT tick; rq_116 deferred"
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
    "etnic,Etnic IT FWB,Etnic,FWB digital services dual Digitaal VL,agency,fwb_gov,fr,https://www.etnic.be,,,CoA aju2026 rec 132.1m CE 198.7 CL 143.1 SEC -11.1 reserve repay 11.1; dual Digitaal; tick669",
    "one_fwb,ONE Office naissance enfance,Office de la Naissance et de l Enfance,FWB child agency dual Kind en Gezin,agency,fwb_gov,fr,https://www.one.be,,,CoA aju2026 rec 803.2 CL 821.6 SEC -18.5 reserve repay 29.5; dual KO/Opgroeien; tick669",
    "wbe,WBE Wallonie Bruxelles Enseignement,Wallonie-Bruxelles Enseignement,FWB official education network dual GO!,agency,fwb_gov,fr,https://www.wbe.be,,,CoA aju2026 rec 77.5 CL 78.0 SEC -0.5; Seca budgets not annexed; dual GO!; tick669",
    "saca_piebs,SACA Piebs batiments scolaires,Saca Plan investissement exceptionnel batiments scolaires,FWB school buildings exceptional plan,agency,fwb_gov,fr,https://www.federation-wallonie-bruxelles.be,,,CoA aju eng 400m CL 1.463 report use 400m stock 699.5->299.5; not on ICN list CoA flag; tick669",
    "saca_cur,SACA CUR Cellule urgence redeploiement,Saca Cellule urgence et redeploiement,FWB PRR emergency cell dual,agency,fwb_gov,fr,,,CoA aju rec 95.7 CL 267.0 solde -171.3 PRR path; report 29.8->56.0; tick669",
    "fonds_ecureuil,Fonds Ecureuil FWB,Fonds Ecureuil,FWB delegated advances fund dual,agency,fwb_gov,fr,,,CoA aju rec 135.2 CL 49.8 SEC +85.4; reserve use 83.6 misclassified as rec CoA; tick669",
]

src_rows = [
    f"{SRC},CoA FWB aju2026 SACA Table20-21 OAP Table23-24 encours dual WAL,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCF_2026_AJU.pdf,Cour des comptes Belgique,2026-08-01,audit,"
    "Strong tick669: SACA 17 units rec 498.8 CE 865.9 CL 714.1 solde -215.4; CUR 95.7/267.0 -171.3; Piebs eng 400 CL 1.5; PPT 0/48; FBSCF 96.5/124.2; FBSELS 57.3/17.8 +39.4; SGPGI 114.3; CCA 26.5; report 1103.1->734.6 (Piebs -400 PPT -28.3 FBSELS +36.3 CUR +26.2); OAP T1 Etnic 132.1/143.1 SEC -11.1; T2 total 1073.5/1010.8 SEC +62.6 ONE 803.2/821.6 -18.5 WBE 77.5/78 Ecureuil 135.2/49.8 +85.4; reserve repay 41.5 (ONE 29.5 Etnic 11.1); perimeter ICN 148 budgets 112/113 ImpacTheo missing; fonds budg rec 60.9 dep 45.8 solde 15.1; encours eoy2025 863.1 path eoy2026 768.5; dual WAL SACA/Type3",
    f"{SRC_DUAL},Dual FWB SACA/OAP perimeter vs WAL Type3 dual,https://www.ccrek.be/sites/default/files/Docs/2026_33_BudgetCF_2026_AJU.pdf,DOGE synthesis CoA FWB SACA dual WAL,2026-08-01,synthesis,"
    "Strong dual: FWB SACA solde -215m report 1.10bn ONE 822m Etnic 143m vs WAL Type3/SACA stacks; not TE-additive; tick669",
]

bud_rows = [
    # Fonds budg Table19
    f"bud_fwb_fonds_rec_aju_2026,fwb_gov,2026,60938000,,,budgeted,{SRC},strong,Fonds budg recettes affectees aju 60.938m path +3.970; tick669",
    f"bud_fwb_fonds_dep_aju_2026,fwb_gov,2026,45814000,,,budgeted,{SRC},strong,Fonds budg credits variables CE=CL aju 45.814m path +1.402; tick669",
    f"bud_fwb_fonds_solde_exante_aju_2026,fwb_gov,2026,15124000,,,budgeted,{SRC},strong,Fonds budg solde ex ante aju 15.124m path +2.568; tick669",
    # SACA totals Table20
    f"bud_fwb_saca_rec_aju_2026,fwb_gov,2026,498781000,,,budgeted,{SRC},strong,SACA total recettes aju 498.781m path +99.5 (+24.9pct) vs init 399.4; tick669",
    f"bud_fwb_saca_ce_aju_2026,fwb_gov,2026,865878000,,,budgeted,{SRC},strong,SACA total CE aju 865.878m; tick669",
    f"bud_fwb_saca_cl_aju_2026,fwb_gov,2026,714148000,,,budgeted,{SRC},strong,SACA total CL aju 714.148m path +103.9 vs init 610.3; tick669",
    f"bud_fwb_saca_solde_aju_2026,fwb_gov,2026,-215367000,,,budgeted,{SRC},strong,SACA solde aju -215.367m path -4.5 vs init -210.8; tick669",
    # Named SACA (kEUR -> EUR)
    f"bud_saca_aef_cl_aju_2026,fwb_gov,2026,3894000,,,budgeted,{SRC},strong,SACA AEF CL aju 3.894m solde +0.398; tick669",
    f"bud_saca_aeqes_cl_aju_2026,fwb_gov,2026,1722000,,,budgeted,{SRC},strong,SACA Aeqes CL aju 1.722m solde -0.470; tick669",
    f"bud_saca_cca_rec_aju_2026,fwb_gov,2026,26508000,,,budgeted,{SRC},strong,SACA CCA cinema/AV rec aju 26.508 CL 26.509; dual media; tick669",
    f"bud_saca_afse_cl_aju_2026,fwb_gov,2026,9728000,,,budgeted,{SRC},strong,SACA AFSE CL aju 9.728m solde +1.453; tick669",
    f"bud_saca_fbscf_rec_aju_2026,fwb_gov,2026,96473000,,,budgeted,{SRC},strong,SACA FBSCF rec aju 96.473 CE 93.198 CL 124.238 solde -27.765; tick669",
    f"bud_saca_fbscf_cl_aju_2026,fwb_gov,2026,124238000,,,budgeted,{SRC},strong,SACA FBSCF CL aju 124.238m; tick669",
    f"bud_saca_fgbs_cl_aju_2026,fwb_gov,2026,22864000,,,budgeted,{SRC},strong,SACA FGBS CL aju 22.864m; tick669",
    f"bud_saca_fbseos_cl_aju_2026,fwb_gov,2026,53365000,,,budgeted,{SRC},strong,SACA FBSEOS CL aju 53.365 path +14.7 PRR delays; tick669",
    f"bud_saca_fncp_cl_aju_2026,fwb_gov,2026,17300000,,,budgeted,{SRC},strong,SACA FCNP (places scolaires) CL aju 17.300 CE 1.393 solde -17.300; tick669",
    f"bud_saca_cur_rec_aju_2026,saca_cur,2026,95723000,,,budgeted,{SRC},strong,SACA CUR rec aju 95.723 path +86.5 to reach PRR total 401.0; tick669",
    f"bud_saca_cur_ce_aju_2026,saca_cur,2026,69541000,,,budgeted,{SRC},strong,SACA CUR CE aju 69.541; tick669",
    f"bud_saca_cur_cl_aju_2026,saca_cur,2026,266977000,,,budgeted,{SRC},strong,SACA CUR CL aju 266.977 path +77.7 PRR end; solde -171.254; tick669",
    f"bud_saca_ppt_ce_aju_2026,fwb_gov,2026,28342000,,,budgeted,{SRC},strong,SACA PPT CE aju 28.342 CL 48.000 solde -48.0 school buildings grants; tick669",
    f"bud_saca_ppt_cl_aju_2026,fwb_gov,2026,48000000,,,budgeted,{SRC},strong,SACA PPT CL aju 48.000m; tick669",
    f"bud_saca_sgpgi_rec_aju_2026,fwb_gov,2026,114312000,,,budgeted,{SRC},strong,SACA SGPGI rec aju 114.312 CL 101.482 solde +12.830; tick669",
    f"bud_saca_piebs_ce_aju_2026,saca_piebs,2026,400000000,,,budgeted,{SRC},strong,SACA Piebs CE aju 400.000 CL 1.463 solde -1.463; eng from report stock; tick669",
    f"bud_saca_piebs_cl_aju_2026,saca_piebs,2026,1463000,,,budgeted,{SRC},strong,SACA Piebs CL aju 1.463m; tick669",
    f"bud_saca_sport_cl_aju_2026,fwb_gov,2026,15893000,,,budgeted,{SRC},strong,SACA Sport CL aju 15.893m solde +0.054; not on ICN list CoA flag; tick669",
    f"bud_saca_fbsels_rec_aju_2026,fwb_gov,2026,57263000,,,budgeted,{SRC},strong,SACA FBSELS rec aju 57.263 CL 17.817 solde +39.446; tick669",
    f"bud_saca_fbsels_cl_aju_2026,fwb_gov,2026,17817000,,,budgeted,{SRC},strong,SACA FBSELS CL aju 17.817m; tick669",
    # Report Table21
    f"bud_saca_report_start_2026,fwb_gov,2026,1103099000,,,budgeted,{SRC},strong,SACA solde reporte 01/01/2026 1103.099m; tick669",
    f"bud_saca_report_end_2026,fwb_gov,2026,734621000,,,budgeted,{SRC},strong,SACA solde reporte path 31/12/2026 734.621m (-368.5); tick669",
    f"bud_saca_piebs_report_start_2026,saca_piebs,2026,699518000,,,budgeted,{SRC},strong,Piebs report 01/01 699.518 path end 299.518 (use -400.0); tick669",
    f"bud_saca_piebs_report_use_400m,saca_piebs,2026,-400000000,,,budgeted,{SRC},strong,Piebs report consumption -400.0m 2026; tick669",
    f"bud_saca_ppt_report_use_28_3m,fwb_gov,2026,-28342000,,,budgeted,{SRC},strong,PPT report use -28.342m (32.808->4.466); tick669",
    f"bud_saca_cur_report_end_2026,saca_cur,2026,55994000,,,budgeted,{SRC},strong,CUR report path 29.812->55.994 (+26.182 result); tick669",
    f"bud_saca_fbsels_report_end_2026,fwb_gov,2026,83504000,,,budgeted,{SRC},strong,FBSELS report 47.191->83.504 (+36.313); tick669",
    f"bud_saca_sgpgi_report_2026,fwb_gov,2026,157843000,,,budgeted,{SRC},strong,SGPGI report stock 157.843 path end 157.419; tick669",
    f"bud_saca_fbseos_report_end_2026,fwb_gov,2026,36435000,,,budgeted,{SRC},strong,FBSEOS report 46.947->36.435 (-10.512); tick669",
    # OAP Table23-24
    f"bud_oap_reserve_repay_total_2026,fwb_gov,2026,41500000,,,budgeted,{SRC},strong,OAP type1+2 reserve repay to FWB 41.5m (Etnic 11.1 ONE 29.5 Ares 0.2 IFPC 0.5 CSA 0.2); tick669",
    f"bud_etnic_rec_aju_2026,etnic,2026,132100000,,,budgeted,{SRC},strong,Etnic rec aju 132.1m path -3.2 (IT strategic dot -3.6); tick669",
    f"bud_etnic_ce_aju_2026,etnic,2026,198700000,,,budgeted,{SRC},strong,Etnic CE aju 198.7m path -2.2; tick669",
    f"bud_etnic_cl_aju_2026,etnic,2026,143100000,,,budgeted,{SRC},strong,Etnic CL aju 143.1m path -3.3 SEC -11.1; dual Digitaal; tick669",
    f"bud_etnic_reserve_repay_11_1m,etnic,2026,11100000,,,budgeted,{SRC},strong,Etnic reserve repay 11.1m = authorized SEC mali; tick669",
    f"bud_one_rec_aju_2026,one_fwb,2026,803200000,,,budgeted,{SRC},strong,ONE rec aju 803.2m path +15.7; dual KO; tick669",
    f"bud_one_ce_aju_2026,one_fwb,2026,826000000,,,budgeted,{SRC},strong,ONE CE aju 826.0m; tick669",
    f"bud_one_cl_aju_2026,one_fwb,2026,821600000,,,budgeted,{SRC},strong,ONE CL aju 821.6m path +4.6 SEC -18.5 (mali improved 11.1); tick669",
    f"bud_one_dot_mfwb_aju_2026,one_fwb,2026,774900000,,,budgeted,{SRC},strong,ONE dots MFWB aju 774.9m path +7.9 (index +10.9 economies -3.1); tick669",
    f"bud_one_cur_it_subs_aju_2026,one_fwb,2026,12700000,,,budgeted,{SRC},strong,ONE CUR IT subsidy aju 12.7m path +6.8; tick669",
    f"bud_one_reserve_repay_29_5m,one_fwb,2026,29500000,,,budgeted,{SRC},strong,ONE reserve repay 29.5m largest OAP repay; tick669",
    f"bud_wbe_rec_aju_2026,wbe,2026,77500000,,,budgeted,{SRC},strong,WBE rec aju 77.5m path +10.1; dual GO!; tick669",
    f"bud_wbe_cl_aju_2026,wbe,2026,78000000,,,budgeted,{SRC},strong,WBE CL aju 78.0m path +10.1 SEC -0.5 HQ fit-out; Seca budgets not annexed CoA flag; tick669",
    f"bud_ares_cd_rec_aju_2026,fwb_gov,2026,30700000,,,budgeted,{SRC},strong,Ares C&D federal rec aju 30.7m CL 32.5 SEC -1.8; tick669",
    f"bud_ares_fwb_rec_aju_2026,fwb_gov,2026,8100000,,,budgeted,{SRC},strong,Ares FWB rec aju 8.1m CL 9.8 SEC -1.7; reserve use 1.6 misclassified rec CoA; tick669",
    f"bud_ifpc_cl_aju_2026,fwb_gov,2026,15100000,,,budgeted,{SRC},strong,IFPC CL aju 15.1 CE 18.2 path +1.4 multi-year training; tick669",
    f"bud_csa_cl_aju_2026,fwb_gov,2026,4000000,,,budgeted,{SRC},strong,CSA CL aju 4.0m SEC -0.2; dual media regulator; tick669",
    f"bud_fonds_ecureuil_rec_aju_2026,fonds_ecureuil,2026,135200000,,,budgeted,{SRC},strong,Fonds Ecureuil rec aju 135.2m path -19.7; tick669",
    f"bud_fonds_ecureuil_cl_aju_2026,fonds_ecureuil,2026,49800000,,,budgeted,{SRC},strong,Fonds Ecureuil CL=CE aju 49.8m path -5.1 SEC +85.4; tick669",
    f"bud_fonds_ecureuil_reserve_use_83_6m,fonds_ecureuil,2026,83600000,,,budgeted,{SRC},strong,Ecureuil reserve use 83.6m booked as rec code 08.10 CoA rejects as budget rec; tick669",
    f"bud_oap_type1_cl_aju_2026,etnic,2026,143100000,,,budgeted,{SRC},strong,OAP type1 total CL aju 143.1m SEC -11.1 (Etnic only); tick669",
    f"bud_oap_type2_rec_aju_2026,fwb_gov,2026,1073500000,,,budgeted,{SRC},strong,OAP type2 total rec aju 1073.5m; tick669",
    f"bud_oap_type2_cl_aju_2026,fwb_gov,2026,1010800000,,,budgeted,{SRC},strong,OAP type2 total CL aju 1010.8 CE 1017.2 SEC +62.6; tick669",
    # Perimeter + encours
    f"bud_fwb_perimeter_icn_units_2026,fwb_gov,2026,148,,,outturn,{SRC},strong,ICN Apr2026 perimeter 148 units S.1312 FWB (+Sonuma -Orthopedagogie); tick669",
    f"bud_fwb_budgets_joined_aju_2026,fwb_gov,2026,112,,,outturn,{SRC},strong,112 of 113 expected budgets joined (ImpacTheo missing); 17 SACA +1 T1 +6 T2 +88 T3; tick669",
    f"bud_fwb_encours_eoy2025,fwb_gov,2025,863100000,,,outturn,{SRC},strong,Encours engagements eoy2025 863.1m; tick669",
    f"bud_fwb_encours_path_eoy2026,fwb_gov,2026,768500000,,,budgeted,{SRC},strong,Encours path eoy2026 768.5m (aju reduces 94.6 vs init reduce 13.1 less); tick669",
    f"bud_fwb_encours_aju_reduce_94_6m,fwb_gov,2026,-94600000,,,budgeted,{SRC},strong,Aju potential encours reduction -94.6m (CE-CL dynamics); WBFin encours rules suspended; tick669",
    f"bud_prr_cur_total_401m,saca_cur,2026,401000000,,,budgeted,{SRC},strong,CUR PRR total envelope target 401.0m (dot path +86.5 to complete); tick669",
    # Dual
    f"bud_dual_fwb_saca_solde_vs_wal_2026,gg_belgium,2026,-215367000,,,budgeted,{SRC_DUAL},strong,Dual FWB SACA solde -215.4m vs WAL SACA/Type stacks; not TE-additive; tick669",
    f"bud_dual_one_ko_channel_2026,gg_belgium,2026,821600000,,,budgeted,{SRC_DUAL},strong,Dual ONE CL 821.6m vs VL Kind en Gezin/Oproeien channel (compare not sum); tick669",
]

cmt_rows = [
    f"cmt_fwb_saca_perimeter_aju2026,FWB SACA 17 units solde -215m report 1.10bn dual,fwb_gov,17 SACA,CoA Table20-21,2026-06-30,2026,2026,714148000,\"{{\"\"2026\"\":714148000}}\",,active,,SACA perimeter map,FOI L5 Piebs CUR,{SRC},strong,FWB>SACA>aju2026,Piebs eng 400 CUR CL 267; tick669",
    f"cmt_fwb_oap_type12_aju2026,FWB OAP T1+T2 CL 1.15bn reserve repay 41.5m,fwb_gov,Etnic ONE WBE Ares IFPC CSA Ecureuil,CoA Table23-24,2026-06-30,2026,2026,1153900000,\"{{\"\"2026\"\":1153900000}}\",,active,,OAP dual GO/KO,Reserve repay opacity,{SRC},strong,FWB>OAP>aju2026,ONE 822 Etnic 143 Ecureuil +85.4 SEC; tick669",
    f"cmt_fwb_one_821m_aju2026,ONE CL 821.6m dual Kind en Gezin,one_fwb,ONE,CoA 7.3.4.2,2026-06-30,2026,2026,821600000,\"{{\"\"2026\"\":821600000}}\",,active,,Childcare dual,L5 FOI,{SRC},strong,FWB>ONE>aju2026,Reserve repay 29.5; tick669",
    f"cmt_fwb_piebs_report_400m,Piebs report use 400m school buildings dual,saca_piebs,Piebs,CoA Table21,2026-06-30,2026,2026,400000000,\"{{\"\"2026\"\":400000000}}\",,active,,School infra stock,ICN list gap,{SRC},strong,FWB>SACA>Piebs,Stock 700->300; tick669",
    f"cmt_fwb_encours_863m_2025,FWB encours 863m path 769m dual WAL,fwb_gov,MFWB,CoA 5.5,2025-12-31,2025,2026,863100000,\"{{\"\"2025\"\":863100000,\"\"2026\"\":768500000}}\",,active,,Commitment stock,WBFin rules suspended,{SRC},strong,FWB>encours,Dual WAL encours 5.94bn incomplete; tick669",
    f"cmt_dual_fwb_saca_oap_tick669,Dual FWB SACA/OAP vs WAL Type3,gg_belgium,Entity II dual perimeter,CoA FWB dual WAL,2026-06-30,2026,2026,714148000,\"{{\"\"2026\"\":714148000}}\",,active,,Dual perimeter,Not TE-additive,{SRC_DUAL},strong,Belgium>dual>fwb_saca_oap,tick669",
]

lb_rows = [
    f"lb_fwb_saca_solde_215m_2026,FWB SACA solde -215m report stock 1.10bn,FWB,ops,FWB>SACA,215367000,0,Strong CoA Table20-21: CL 714m CUR -171 Piebs eng 400 report use; dual WAL SACA,strong,{SRC},17 SACA,Perimeter opacity,Primary,7.0,7.5,3,6.85,Publish Piebs project list,open,,tick669",
    f"lb_fwb_one_822m_2026,ONE CL 821.6m dual Kind en Gezin,FWB,ops,FWB>ONE,821600000,0,Strong CoA: rec 803 CL 822 SEC -18.5 reserve repay 29.5; dual KO/Opgroeien,strong,{SRC},childcare operators,Child dual,Primary,5.5,8.0,3,6.55,L5 beneficiary FOI,open,,tick669",
    f"lb_fwb_etnic_143m_2026,Etnic CL 143.1m dual Digitaal VL,FWB,ops,FWB>Etnic,143100000,0,Strong CoA CE 198.7 reserve repay 11.1 SEC -11.1; dual Digitaal,strong,{SRC},FWB IT,Digital dual,Primary,6.5,6.5,2,6.1,Project list FOI,open,,tick669",
    f"lb_fwb_piebs_eng_400m_2026,Piebs eng 400m report drawdown,FWB,ops,FWB>SACA>Piebs,400000000,0,Strong CoA: eng 400 from report stock 700->300; not on ICN list CoA flag dual school infra,strong,{SRC},school buildings,Infra stock opacity,Primary,7.5,7.5,3,7.0,ICN perimeter + L5 projects,open,,tick669",
    f"lb_fwb_ecureuil_sec_85m_2026,Fonds Ecureuil SEC +85.4m reserve bookkeeping,FWB,ops,FWB>OAP>Ecureuil,85400000,0,Strong CoA: SEC +85.4 but 83.6m reserve misclassified as rec; dual finance ops,strong,{SRC},delegated advances,Accounting opacity,Primary,8.0,6.5,2,6.9,Correct rec classification,open,,tick669",
    f"lb_dual_fwb_saca_oap_2026,Dual FWB SACA/OAP perimeter residual,Belgium,ops,Belgium>dual>fwb_saca_oap,714148000,0,Strong dual: SACA -215m ONE 822 Etnic 143 vs WAL Type3; not TE-additive,strong,{SRC_DUAL},Entity II dual,Perimeter dual,Primary dual,6.5,7.5,3,6.65,Cross FOI,open,,tick669",
]

foi_row = (
    f"{GAP},FWB>Aju2026>SACA_OAP_L5,fwb_gov,"
    "Piebs project list eng 400m; CUR PRR 401m outturn; ONE L5 top beneficiaries; Etnic IT projects; Ecureuil 83.6m reserve booking; Seca WBE budgets; ImpacTheo missing budget; ICN list gaps Piebs/FBSELS/Sport,"
    "CoA FWB aju2026 SACA/OAP strong tick669; L5 residual dual WAL,"
    f"5,MFWB Budget / ONE / Etnic / service transparence FWB,transparence@cfwb.be,https://www.federation-wallonie-bruxelles.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    f"cmt_fwb_saca_perimeter_aju2026|cmt_fwb_one_821m_aju2026|cmt_fwb_piebs_report_400m,"
    f"lb_fwb_saca_solde_215m_2026|lb_fwb_one_822m_2026|lb_fwb_piebs_eng_400m_2026,"
    f"{NOW},{NOW},tick669 CoA FWB SACA/OAP primary; human send only"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes FWB aju 2026 (2026_33) ch.6-7 Tables 19-24

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: MFWB Budget / ONE / Etnic / service transparence
transparence@cfwb.be
https://www.federation-wallonie-bruxelles.be

Betreft: Openbaarheid — SACA/OAP aju 2026 (Piebs, CUR, ONE, Etnic, Ecureuil) L5

Geachte,

Op grond van de openbaarheidsregels van de Franse Gemeenschap verzoek ik om:

1. SACA Piebs: liste des projets couverts par les 400 mEUR d'engagements 2026
   et etat du solde reporte (699,5 -> 299,5 mEUR).
2. SACA CUR: avancement PRR vers l'enveloppe 401 mEUR (dotation path +86,5)
   et liquidations 267 mEUR par projet.
3. ONE: top 30 beneficiaires / programmes (CL 821,6 mEUR) et detail du
   remboursement de reserves 29,5 mEUR.
4. Etnic: liste des projets IT (CE 198,7 / CL 143,1) et reserve repay 11,1 mEUR.
5. Fonds Ecureuil: justification de l'imputation de 83,6 mEUR de reserves en
   recettes (code 08.10) critiquee par la Cour.
6. WBE: budgets des Seca non annexes; date de transmission.
7. Budget manquant ImpacTheo; statut ICN pour Piebs / FBSELS / Saca Sport.

Période: 2024-01-01 à 2027-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes agent
- Primary: CoA 2026_33 FWB aju ch.6-7 (tick669).
- Dual with WAL SACA/Type3 perimeter.
- Do **not** send unless human orders.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual residual -- **FWB aju2026 SACA/OAP perimeter L5 + encours + reserve repay dual WAL**)
- Found (primary CoA 2026_33): **SACA** 17 units rec **EUR498.8m** CE **865.9** CL **714.1** solde **-215.4**; **CUR** CL **267.0** solde **-171.3** (PRR path +86.5 to **401** total); **Piebs** eng **400** report stock **699.5->299.5**; **PPT** CL **48**; **FBSCF** CL **124.2**; **FBSELS** solde **+39.4**; report total **1103->735**. **OAP:** Etnic CL **143.1** SEC **-11.1** repay **11.1**; ONE CL **821.6** SEC **-18.5** repay **29.5**; WBE **78.0**; Ecureuil CL **49.8** SEC **+85.4** (reserve **83.6** misbooked); T2 total CL **1010.8** SEC **+62.6**; repay total **41.5**. Perimeter ICN **148** budgets **112/113**. Encours eoy2025 **863.1** path **768.5**. Fonds budg solde **15.1**. Dual WAL Type3/SACA. Strong CoA; L5 FOI.
- Wrote: entities (+6); budgets (+70); commitments (+6); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; **progress@670 NEXT tick**; rq_116 deferred
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
        f"tick{TICK} FWB SACA -215m report 1.10bn Piebs/CUR/ONE/Etnic dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Progress milestone tick670 + FOI-adjacent dual hole-fill residual,continuous,5,open,L5,gg_belgium,"
        f"PROGRESS@670: refresh progress_every_10_ticks.md + doge_waste_top10_current.md; then residual dual FWB/WAL or Flanders CoA.,,"
        f"{NOW},,spawned tick{TICK} after {RQ} progress next",
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
