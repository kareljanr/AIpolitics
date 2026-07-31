# -*- coding: utf-8 -*-
"""Tick 652: Recettes non fiscales diverses + WE Type3 residual dual PMV — rq_643."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T04:45:00Z"
TICK = 652
RQ = "rq_643"
NEXT_RQ = "rq_644"
GAP = "gap_nonfiscal_we_subs_l5_2025"


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
        f"tick{TICK} nonfiscal 871.5m WE subs dual PMV; "
        f"next {NEXT_RQ}; progress@660 in 8; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "nonfiscal_diverses_wal,Recettes non fiscales diverses Wallonie,Recettes diverses non fiscales RW,Walloon miscellaneous non-fiscal receipts dual VL,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA s4.5.1 BI2025 871.5m path -164.4m; tresorerie remonte 536.6m dividends 55m swaps 68.4m; dual VL nonfiscal; tick652",
    "we_international,WE International ex Sofinex,WE International anciennement Sofinex,Walloon export finance subsidiary dual FIT/PMV,subsidiary,wallonie_entreprendre,fr,https://www.wallonie-entreprendre.be,,,Type3 CoA Annex3 BI2025 rec 4.838m dep 2.627m solde +2.211m; BI2024 rec 2.126m dep 1.340m solde +0.786m; tick652",
    "socamut,Socamut cautions mutuelles Wallonie,Societe des cautions mutuelles de Wallonie,Walloon mutual guarantee company dual PMV guarantees,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 4.103m dep 2.432m solde +1.671m path solde +1.660m; tick652",
    "novallia,Novallia,Novallia,Walloon innovation finance vehicle dual VLAIO,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 4.494m dep 0.278m solde +4.216m; BI2024 solde +2.278m; tick652",
    "we_accompagnement,WE Accompagnement et strategie ex Sowaccess,WE Accompagnement et strategie anciennement Sowaccess,Walloon SME accompaniment dual VLAIO,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 19.724m dep 19.058m solde +0.666m; tick652",
    "wow_wallonie,Wallonia Offshore Wind WOW,Wallonia Offshore Wind WOW,Walloon offshore wind investment vehicle,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec=dep path flat 3.561/0.720 solde +2.841m; tick652",
    "arceo_wal,Arceo,Arceo,Walloon holding vehicle Type3,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 6.024m dep 7.251m solde -1.227m path -3.974m; tick652",
    "fpw_participation,Fonds de participation de Wallonie FPW,Fonds de participation de Wallonie,Walloon participation fund dual PMV,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 0.877m dep 0.187m solde +0.691m; tick652",
    "we_environnement,WE Environnement ex SRIW Environnement,WE Environnement anciennement SRIW Environnement,Walloon environment finance dual,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 10.131m dep 6.820m solde +3.310m (BA2024 non communique); tick652",
    "be_fin_wal,BE Fin,BE Fin,Walloon finance vehicle Type3,subsidiary,wallonie_entreprendre,fr,,,Type3 CoA Annex3 BI2025 rec 6.581m dep 6.022m solde +0.559m; tick652",
    "wallonie_sante_invest,Wallonie Sante investissement,Societe wallonne d investissement sante hopitaux ages handicap,Walloon health-sector investment company dual,agency,wallonie_gov,fr,,,Type3 CoA Annex3 BI2025 rec 4.017m dep 1.916m solde +2.101m; tick652",
]

src_rows = [
    "src_ccrek_nonfiscal_we_subs_bi2025,CoA Budget RW nonfiscal diverses s4.5.1 + Annex3 WE Type3 dual PMV,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick652: nonfiscal diverses BI2025 871.5m path -164.4m; tresorerie remonte 536.6m (AViQ 335.3 WE 110 SPAQuE 40.5 Sowaer 20 IWEPS 8 CRAC-LT 5 CGT 4.4 WBI 4 Service social+Awap 3 CRA-W 2 OPW 1 Apaq-W 0.5); dividends 55m (FN Herstal 15); Sofico expropri 15.8; immeubles 10; bois 14; placements 5; tresorerie int 70; swaps 68.4; SPF PP rembours 19.3 (scientific 16 night 3.3 CoA overstate actual 0.085m 2024); WE subs: WE Int 4.838/2.627/+2.211; Socamut 4.103/2.432/+1.671; Novallia 4.494/0.278/+4.216; WE Acc 19.724/19.058/+0.666; WOW 3.561/0.720/+2.841; Arceo 6.024/7.251/-1.227; FPW 0.877/0.187/+0.691; WE Env 10.131/6.820/+3.310; BE Fin 6.581/6.022/+0.559; Wallonie Sante 4.017/1.916/+2.101; Espace Fin 0.579/0.912/-0.332; Invests 4.166/2.571/+1.595; dual PMV",
    "src_dual_nonfiscal_we_pmv_tick652,Dual WAL nonfiscal + WE Type3 vs VL PMV,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA nonfiscal+Annex3 + prior PMV,2026-08-01,synthesis,Strong dual: WAL nonfiscal 871.5m + WE group residual Type3 vs VL PMV holdings/dividends; not TE-additive; tick652",
]

bud_rows = [
    # Non-fiscal
    "bud_nonfiscal_diverses_bi2025,nonfiscal_diverses_wal,2025,871500000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Recettes diverses non fiscales BI2025 871.5m path -164.4m; tick652",
    "bud_nonfiscal_tresorerie_remonte_uap_bi2025,nonfiscal_diverses_wal,2025,536600000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Rapatriement tresoreries UAP 536.6m (component of 575.6m total remonte); tick652",
    "bud_nonfiscal_remonte_aviq_bi2025,aviq,2025,335300000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte AViQ 335.3m of UAP treasury; tick652",
    "bud_nonfiscal_remonte_we_bi2025,wallonie_entreprendre,2025,110000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte WE 110.0m; tick652",
    "bud_nonfiscal_remonte_spaque_bi2025,spaque,2025,40500000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte SPAQuE 40.5m; tick652",
    "bud_nonfiscal_remonte_sowaer_bi2025,sowaer,2025,20000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte Sowaer 20.0m; tick652",
    "bud_nonfiscal_remonte_iweps_bi2025,wallonie_gov,2025,8000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte IWEPS 8.0m; tick652",
    "bud_nonfiscal_remonte_crac_lt_bi2025,crac,2025,5000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte CRAC long terme 5.0m; tick652",
    "bud_nonfiscal_remonte_cgt_bi2025,tourisme_wallonie,2025,4400000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte CGT 4.4m; tick652",
    "bud_nonfiscal_remonte_wbi_bi2025,wbi,2025,4000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte WBI 4.0m; tick652",
    "bud_nonfiscal_remonte_craw_bi2025,cra_w,2025,2000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Remonte CRA-W 2.0m; tick652",
    "bud_nonfiscal_dividendes_bi2025,nonfiscal_diverses_wal,2025,55000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Participation benefices entreprises 55.0m; tick652",
    "bud_nonfiscal_fn_herstal_bi2025,nonfiscal_diverses_wal,2025,15000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Dividendes FN Herstal 15.0m within 55m; tick652",
    "bud_nonfiscal_sofico_expropri_bi2025,sofico,2025,15800000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Sofico expropriation remboursements 15.8m (matched dep); tick652",
    "bud_nonfiscal_vente_immeubles_bi2025,nonfiscal_diverses_wal,2025,10000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Vente immeubles 10.0m (7 sites Liege Mons Malmedy); tick652",
    "bud_nonfiscal_coupe_bois_bi2025,nonfiscal_diverses_wal,2025,14000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Vente coupe de bois 14.0m; tick652",
    "bud_nonfiscal_interets_placements_bi2025,nonfiscal_diverses_wal,2025,5000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Interets crediteurs placements 5.0m; tick652",
    "bud_nonfiscal_interets_tresorerie_bi2025,nonfiscal_diverses_wal,2025,70000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Interets tresorerie 70.0m; tick652",
    "bud_nonfiscal_swaps_bi2025,nonfiscal_diverses_wal,2025,68400000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Revenus des swaps 68.4m; tick652",
    "bud_nonfiscal_spf_pp_rembours_bi2025,nonfiscal_diverses_wal,2025,19300000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,SPF Finances precompte rembours 19.3m (scientific 16 + night 3.3); tick652",
    "bud_nonfiscal_pp_scientific_bi2025,nonfiscal_diverses_wal,2025,16000000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Precompte professionnel fonctions scientifiques 16.0m; tick652",
    "bud_nonfiscal_pp_night_budget_bi2025,nonfiscal_diverses_wal,2025,3300000,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,medium,Precompte night/team budget 3.3m CoA overstate; tick652",
    "bud_nonfiscal_pp_night_actual_2024,nonfiscal_diverses_wal,2024,85000,,,outturn,src_ccrek_nonfiscal_we_subs_bi2025,strong,Actual night/team PP recovery 2024 (remun 2023) only 0.085m CoA; tick652",
    # WE Type3 residual
    "bud_we_int_rec_bi2025,we_international,2025,4838417,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE International rec BI2025 4.838m; tick652",
    "bud_we_int_dep_bi2025,we_international,2025,2626957,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE International dep BI2025 2.627m solde +2.211m; tick652",
    "bud_socamut_rec_bi2025,socamut,2025,4102523,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Socamut rec BI2025 4.103m; tick652",
    "bud_socamut_dep_bi2025,socamut,2025,2431688,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Socamut dep BI2025 2.432m solde +1.671m; tick652",
    "bud_novallia_rec_bi2025,novallia,2025,4493756,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Novallia rec BI2025 4.494m; tick652",
    "bud_novallia_dep_bi2025,novallia,2025,277773,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Novallia dep BI2025 0.278m solde +4.216m; tick652",
    "bud_we_acc_rec_bi2025,we_accompagnement,2025,19723899,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE Accompagnement rec BI2025 19.724m; tick652",
    "bud_we_acc_dep_bi2025,we_accompagnement,2025,19058112,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE Accompagnement dep BI2025 19.058m solde +0.666m; tick652",
    "bud_wow_rec_bi2025,wow_wallonie,2025,3560776,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WOW rec BI2025 3.561m; tick652",
    "bud_wow_dep_bi2025,wow_wallonie,2025,719862,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WOW dep BI2025 0.720m solde +2.841m; tick652",
    "bud_arceo_rec_bi2025,arceo_wal,2025,6024300,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Arceo rec BI2025 6.024m; tick652",
    "bud_arceo_dep_bi2025,arceo_wal,2025,7251319,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Arceo dep BI2025 7.251m solde -1.227m; tick652",
    "bud_fpw_rec_bi2025,fpw_participation,2025,877370,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,FPW rec BI2025 0.877m; tick652",
    "bud_fpw_dep_bi2025,fpw_participation,2025,186834,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,FPW dep BI2025 0.187m solde +0.691m; tick652",
    "bud_we_env_rec_bi2025,we_environnement,2025,10130781,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE Environnement rec BI2025 10.131m; tick652",
    "bud_we_env_dep_bi2025,we_environnement,2025,6820467,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,WE Environnement dep BI2025 6.820m solde +3.310m; tick652",
    "bud_be_fin_rec_bi2025,be_fin_wal,2025,6581495,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,BE Fin rec BI2025 6.581m; tick652",
    "bud_be_fin_dep_bi2025,be_fin_wal,2025,6022279,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,BE Fin dep BI2025 6.022m solde +0.559m; tick652",
    "bud_wallonie_sante_rec_bi2025,wallonie_sante_invest,2025,4016956,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie Sante rec BI2025 4.017m; tick652",
    "bud_wallonie_sante_dep_bi2025,wallonie_sante_invest,2025,1916319,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie Sante dep BI2025 1.916m solde +2.101m; tick652",
    "bud_espace_fin_dep_bi2025,wallonie_entreprendre,2025,911928,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Espace Financement dep BI2025 0.912m solde -0.332m (path +11.2m vs BI2024 -11.5m); tick652",
    "bud_invests_rec_bi2025,wallonie_entreprendre,2025,4166260,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Invests rec BI2025 4.166m path -1.011m; tick652",
    "bud_invests_dep_bi2025,wallonie_entreprendre,2025,2570968,,,budgeted,src_ccrek_nonfiscal_we_subs_bi2025,strong,Invests dep BI2025 2.571m solde +1.595m; tick652",
]

cmt_rows = [
    'cmt_nonfiscal_diverses_coa_bi2025,Recettes non fiscales diverses CoA s4.5.1 BI2025,nonfiscal_diverses_wal,UAP treasuries FN Herstal Sofico,Budget recettes RW + CoA,2024-11-15,2025,2025,871500000,"{""total_m"":871.5,""path_m"":-164.4,""remonte_m"":536.6,""dividends_m"":55,""fn_herstal_m"":15,""swaps_m"":68.4,""tresorerie_int_m"":70,""spf_pp_m"":19.3,""pp_night_actual_2024_m"":0.085,""note"":""Strong CoA; night PP overstated residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Miscellaneous non-fiscal receipts,Correct night PP forecast FOI dual VL,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie>Recettes>Nonfiscal,tick652',
    'cmt_we_type3_subs_coa_bi2025,WE Type3 subsidiaries residual CoA Annex3 BI2025,wallonie_entreprendre,WE group export guarantees innovation offshore,CoA Annex3 Type3,2024-11-15,2025,2025,0,"{""we_int_solde_m"":2.211,""socamut_m"":1.671,""novallia_m"":4.216,""we_acc_m"":0.666,""wow_m"":2.841,""arceo_m"":-1.227,""fpw_m"":0.691,""we_env_m"":3.310,""be_fin_m"":0.559,""sante_m"":2.101,""note"":""Strong CoA L5 residual; dual PMV; non-communique residual FOI""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,WE group subsidiary SEC map,Publish full non-communique FOI dual PMV,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie>WE>Type3_subs,tick652',
    'cmt_pp_night_overstate_coa_bi2025,Precompte night/team overstated CoA s4.5.1,nonfiscal_diverses_wal,SPW employers,EIWT night/team public employers,2024-11-15,2025,2025,3300000,"{""budget_m"":3.3,""actual_2024_m"":0.085,""scientific_m"":16.0,""note"":""Strong CoA: public employers night PP only real-estate works; overstate residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Overstated night precompte receipt,Correct budget FOI,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie>Recettes>PP_night,tick652',
    'cmt_dual_nonfiscal_we_pmv_2025,Dual WAL nonfiscal WE Type3 vs VL PMV,nonfiscal_diverses_wal,Regional holdings dual,CoA WAL + prior PMV,2024-11-15,2025,2025,0,"{""wal_nonfiscal_m"":871.5,""wal_remonte_m"":536.6,""wal_we_group_solde_m"":-38.619,""note"":""Not TE-additive dual holding stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional holding dual map,Cross-region transparency FOI,src_dual_nonfiscal_we_pmv_tick652,strong,Belgium>Holdings>dual_WE_PMV,tick652',
    'cmt_uap_remonte_breakdown_bi2025,UAP treasury remonte breakdown 536.6m BI2025,nonfiscal_diverses_wal,AViQ WE SPAQuE Sowaer IWEPS CRAC CGT WBI,Budget recettes remonte,2024-11-15,2025,2025,536600000,"{""aviq_m"":335.3,""we_m"":110,""spaque_m"":40.5,""sowaer_m"":20,""iweps_m"":8,""crac_lt_m"":5,""cgt_m"":4.4,""wbi_m"":4,""craw_m"":2,""note"":""Strong CoA footnote; no SEC net impact""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,UAP excess treasury sweep,Publish annual remonte series FOI,src_ccrek_nonfiscal_we_subs_bi2025,strong,Wallonie>UAP>Remonte,tick652',
]

lb_rows = [
    "lb_nonfiscal_diverses_872m_2025,Nonfiscal diverses 871.5m path -164m BI2025,Wallonia,ops,Wallonie>Recettes>Nonfiscal_872m,871500000,871500000,Strong CoA s4.5.1: 871.5m path -164.4m; remonte 536.6m dominates,strong,src_ccrek_nonfiscal_we_subs_bi2025,WAL taxpayers UAP,Miscellaneous non-fiscal receipts,Remonte non-structural residual,5.5,8.0,3,6.20,Publish remonte sustainability FOI,seed,,tick652",
    "lb_pp_night_overstate_3_3m_2025,Precompte night budget 3.3m vs actual 0.085m,Wallonia,ops,Wallonie>Recettes>PP_night_overstate,3300000,3300000,Strong CoA: budget 3.3m vs 2024 actual 0.085m; public night PP real-estate only,strong,src_ccrek_nonfiscal_we_subs_bi2025,SPW employers,Overstated night precompte receipt,High-abs forecast residual,7.5,3.5,2,5.85,Correct budget line FOI,seed,,tick652",
    "lb_nonfiscal_swaps_68m_2025,Swap revenues 68.4m BI2025,Wallonia,ops,Wallonie>Recettes>Swaps_68m,68400000,68400000,Strong CoA: revenus swaps 68.4m within nonfiscal; dual debt book,strong,src_ccrek_nonfiscal_we_subs_bi2025,WAL debt management,Interest-rate swap receipts,Finance residual dual debt,4.5,6.0,4,4.85,Publish swap book FOI,seed,,tick652",
    "lb_novallia_solde_4_2m_2025,Novallia SEC solde +4.2m BI2025 dual VLAIO,Wallonia,ops,Wallonie>WE>Novallia_4_2m,4215983,4493756,Strong CoA Annex3: Novallia solde +4.216m (rec 4.494 dep 0.278); dual VLAIO innovation,strong,src_ccrek_nonfiscal_we_subs_bi2025,Innovation promoters,WE innovation vehicle,Holding residual dual PMV,4.0,3.5,4,3.65,FOI portfolio L5 dual VLAIO,seed,,tick652",
    "lb_arceo_solde_minus_1_2m_2025,Arceo SEC solde -1.2m path -4.0m BI2025,Wallonia,ops,Wallonie>WE>Arceo_minus_1_2m,1227019,7251319,Strong CoA: Arceo solde -1.227m path -3.974m; Type3 residual,strong,src_ccrek_nonfiscal_we_subs_bi2025,Holding taxpayers,WE vehicle deficit path,Opacity residual FOI,5.5,4.0,4,4.55,FOI mission L5,seed,,tick652",
    "lb_dual_nonfiscal_we_pmv_2025,Dual WAL nonfiscal 872m WE Type3 vs VL PMV,Belgium,ops,Belgium>Holdings>dual_nonfiscal_WE_PMV,871500000,0,Strong dual: WAL nonfiscal 871.5m + WE Type3 residual vs VL PMV holdings; not TE-additive,strong,src_dual_nonfiscal_we_pmv_tick652,BE regional taxpayers,Parallel holding/nonfiscal stacks,Dual opacity residual,6.0,8.0,4,6.50,Cross-region FOI,seed,,tick652",
]

foi_row = (
    f"{GAP},Wallonie>Nonfiscal_WE>L5_2025,nonfiscal_diverses_wal,"
    "Nonfiscal L5: night PP correct forecast; remonte sustainability by UAP; dividends L5 beyond FN Herstal; "
    "WE Type3 non-communique list (123CDI Sofibail Gepart mutualites); dual PMV portfolio,"
    "CoA nonfiscal+Annex3 totals strong tick652; L5 residual dual,"
    "5,SPW Budget / WE / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_nonfiscal_diverses_coa_bi2025|cmt_we_type3_subs_coa_bi2025|cmt_dual_nonfiscal_we_pmv_2025,"
    "lb_nonfiscal_diverses_872m_2025|lb_pp_night_overstate_3_3m_2025|lb_dual_nonfiscal_we_pmv_2025,"
    f"{NOW},{NOW},tick652 CoA nonfiscal WE Type3 primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW §4.5.1 nonfiscal + Annex 3 WE Type3; dual PMV prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / Wallonie Entreprendre / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Recettes non fiscales + filiales WE Type3 L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Correction et base de calcul du précompte nuit/équipe budgété
   3,3 mEUR BI2025 (CoA: réalisation 2024 seulement 0,085 mEUR).
2. Série pluriannuelle du rapatriement de trésorerie UAP (536,6 mEUR
   2025) par organisme et impact sur leurs soldes SEC.
3. Ventilation L5 des dividendes 55 mEUR (hors FN Herstal 15 mEUR).
4. Budgets BI2025 des Type3 « non communiqué » (Sofibail, 123CDI,
   Gepart, mutualités régionales, etc.) s'ils existent.
5. Portefeuille L5 Novallia / Socamut / WE International / WOW /
   Arceo (investissements, garanties, bénéficiaires 2023-2025).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 §4.5.1 + Annex 3.
- Dual VL: PMV holdings / non-fiscal receipts (prior).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual nonfiscal/holding hole-fill -- **Recettes non fiscales diverses + WE Type3 residual** dual PMV)
- Found: **Nonfiscal diverses** (primary CoA s4.5.1): BI2025 **EUR871.5m** (path **-EUR164.4m**). Remonte UAP **EUR536.6m** (AViQ **EUR335.3m** / WE **EUR110m** / SPAQuE **EUR40.5m** / Sowaer **EUR20m**). Dividendes **EUR55m** (FN Herstal **EUR15m**). Swaps **EUR68.4m**; tresorerie int **EUR70m**; Sofico expropri **EUR15.8m**. **PP night budget EUR3.3m vs actual EUR0.085m** (CoA overstate). **WE Type3 residual:** Novallia solde **+EUR4.2m**; Socamut **+EUR1.7m**; WE Int **+EUR2.2m**; WOW **+EUR2.8m**; WE Acc **+EUR0.7m**; Arceo **-EUR1.2m**; WE Env **+EUR3.3m**; Wallonie Sante **+EUR2.1m**. Dual **PMV**. Strong confidence CoA; non-communique residual FOI.
- Wrote: entities (+11); budgets (+45); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@660 in 8 ticks; rq_116 deferred
"""


def main() -> None:
    n_ent = append_rows(ROOT / "entities.csv", ent_rows)
    n_src = append_rows(ROOT / "sources.csv", src_rows)
    n_bud = append_rows(ROOT / "budgets.csv", bud_rows)
    n_cmt = append_rows(ROOT / "commitments.csv", cmt_rows)
    n_lb = append_rows(ROOT / "leaderboard.csv", lb_rows)
    n_foi = append_rows(ROOT / "foi_queue.csv", [foi_row])

    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    draft_path = FOI_DRAFTS / f"{GAP}.md"
    if not draft_path.exists():
        draft_path.write_text(foi_draft, encoding="utf-8")
        print(f"WROTE draft {draft_path.name}")
    else:
        print(f"SKIP draft exists {draft_path.name}")

    update_rq_done(
        ROOT / "research_queue.csv",
        RQ,
        f"tick{TICK} nonfiscal 871.5m WE Type3 dual PMV; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after nonfiscal WE dual; rq_116 deferred; progress@660 in 8",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log_text = read_text(LOG)
    if f"-- tick {TICK}" not in log_text[-3000:]:
        if not log_text.endswith("\n"):
            log_text += "\n"
        log_text += log_entry
        LOG.write_bytes(log_text.encode("utf-8"))
        print("LOG appended")
    else:
        print("SKIP log already has tick")

    print(
        f"DONE tick{TICK}: ent+{n_ent} src+{n_src} bud+{n_bud} cmt+{n_cmt} lb+{n_lb} foi+{n_foi}"
    )


if __name__ == "__main__":
    main()
