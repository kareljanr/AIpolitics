# -*- coding: utf-8 -*-
"""Tick 655: AViQ branch residual dual VAPH + Parlement/cabinets + SEC corr — rq_646."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T05:30:00Z"
TICK = 655
RQ = "rq_646"
NEXT_RQ = "rq_647"
GAP = "gap_aviq_branch_parlement_l5_2025"


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
        f"tick{TICK} AViQ branch non-marchand 276m Papy-boom dual VAPH; "
        f"next {NEXT_RQ}; progress@660 in 5; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "parlement_wallonie,Parlement de Wallonie,Parlement de Wallonie,Walloon Parliament dual VL Parliament,legislature,wallonie_gov,fr,https://www.parlement-wallonie.be,,,CoA DO01 BI2025 CE=CL 77.437m path +1.058m exec 100pct; dotation 75.572m mediateur 1.865m; dual VL Parlement; tick655",
    "mediateur_wallonie,Mediateur de la Region wallonne,Service du mediateur de la Region wallonne,Walloon Ombudsman dual VL Ombudsman,agency,parlement_wallonie,fr,https://www.mediateurwallonie.be,,,DO01.003 BI2025 CE=CL 1.865m path +0.034m; dual VL Ombudsman; tick655",
]

src_rows = [
    "src_ccrek_aviq_branch_parlement_bi2025,CoA Budget RW AViQ s8.2 Table34 + DO01 Parlement dual VAPH,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick655: AViQ Table34 rec 6876645k dep 7255891k result -379246k path rec +336304 (+5.1pct) dep +286620 (+4.1pct); treasury remonte 335.3m drives deficit; consol impact -330.6m after inexec 48.6m; PRW rec 2.4m but RW DF122.006 liq zero; facultatives -10m (subs -5 + inexec +5); non-marchand 276.2m path +151.1 vs BI2024 125.1; index pivot +128.4m; Papy-boom eng 23.7 liq 19.9 encours 34.0 mid-Nov eng 113.5 liq 80.2 beds residual 1886+442 done 331+173; priority handicap places 79.9m (+5 for 100 new); prevention +40m (promo 15 ETP-PSY 8.6 provision 16.4); Safa +4.4m; MR/MRS +6.8m programming 2019-24 +1413 MR +4690 MRS +160 CSJ; DO01 Parlement 77437 path +1058 (dot 75572 mediateur 1865); cabinets MP 5401 Territoire 5177 Eco 5325 Sante 3251 FP 1556 Tourisme 1408 Energie 2954 Agri 2954; SEC other corr 161.1m (hospital 103.3 green cert 33 succession lag 32 guarantees -5 fines -3.1); requalif effective margin 75.8 after ICN 49.6; dual VAPH",
    "src_dual_aviq_vaph_tick655,Dual WAL AViQ branch residual vs VL VAPH VSB,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA AViQ s8.2 + prior VAPH,2026-08-01,synthesis,Strong dual: AViQ dep 7.256bn non-marchand 276m Papy-boom residual dual VAPH/VSB/Opgroeien; not TE-additive; tick655",
]

bud_rows = [
    # AViQ Table34 (budgetary not just SEC)
    "bud_aviq_rec_table34_bi2025,aviq,2025,6876645000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ recettes totales Table34 BI2025 6876.645m path +336.304m (+5.1pct); tick655",
    "bud_aviq_dep_table34_bi2025,aviq,2025,7255891000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ depenses totales Table34 BI2025 7255.891m path +286.620m (+4.1pct); tick655",
    "bud_aviq_result_table34_bi2025,aviq,2025,-379246000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ resultat budgetaire Table34 BI2025 -379.246m path +49.684m; tick655",
    "bud_aviq_inexec_presume_bi2025,aviq,2025,48600000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ inexecution presumee 48.6m in consol impact calc; tick655",
    "bud_aviq_consol_impact_bi2025,aviq,2025,-330600000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ impact solde financement consol -330.6m after inexec; tick655",
    "bud_aviq_prw_rec_bi2025,aviq,2025,2400000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,AViQ PRW recettes 2.4m but RW DF122.006 liq zero reallocation residual; tick655",
    "bud_aviq_facultatives_cut_bi2025,aviq,2025,10000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Facultatives dotation cut 10.0m (subs -5m + inexec +5m); tick655",
    "bud_aviq_nonmarchand_bi2025,aviq,2025,276200000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Non-marchand accords 2021-24 credits 276.2m BI2025 path +151.1m vs BI2024 125.1m; tick655",
    "bud_aviq_nonmarchand_bi2024,aviq,2024,125100000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Non-marchand BI2024 125.1m; tick655",
    "bud_aviq_index_pivot_bi2025,aviq,2025,128400000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Index pivot depassements path +128.4m AViQ credits; tick655",
    "bud_aviq_papyboom_eng_bi2025,aviq,2025,23700000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Papy-boom elderly construction eng 23.7m BI2025; tick655",
    "bud_aviq_papyboom_liq_bi2025,aviq,2025,19900000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Papy-boom liq 19.9m BI2025; tick655",
    "bud_aviq_papyboom_encours_nov2024,aviq,2024,34000000,,,outturn,src_ccrek_aviq_branch_parlement_bi2025,strong,Papy-boom encours 34.0m at 7 Nov 2024; tick655",
    "bud_aviq_papyboom_cum_eng_nov2024,aviq,2024,113500000,,,outturn,src_ccrek_aviq_branch_parlement_bi2025,strong,Papy-boom cum eng mid-Nov 2024 113.5m; tick655",
    "bud_aviq_papyboom_cum_liq_nov2024,aviq,2024,80200000,,,outturn,src_ccrek_aviq_branch_parlement_bi2025,strong,Papy-boom cum liq mid-Nov 2024 80.2m; tick655",
    "bud_aviq_priority_places_bi2025,aviq,2025,79900000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Priority handicap places eng=liq 79.9m (+5m for 100 new places 2025); tick655",
    "bud_aviq_prevention_promo_bi2025,aviq,2025,40000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Prevention/promo sante +40m (promo 15 + ETP-PSY 8.6 + provision 16.4) structuralize from PRW; tick655",
    "bud_aviq_promo_sante_15m_bi2025,aviq,2025,15000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Agrement acteurs promotion sante 15.0m of prevention pack; tick655",
    "bud_aviq_etp_psy_bi2025,aviq,2025,8600000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,ETP PSY prolongation 1yr 8.6m; tick655",
    "bud_aviq_prevention_provision_bi2025,aviq,2025,16400000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Provision nouveaux projets prevention 16.4m; tick655",
    "bud_aviq_safa_bi2025,aviq,2025,4400000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Safa family aid +4.4m (contrib 0.4 to 1.9 EUR Jul2024); tick655",
    "bud_aviq_mr_mrs_extra_bi2025,aviq,2025,6800000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,MR/MRS sejour +6.8m (staff reinfort + programming); tick655",
    "bud_aviq_mr_staff_reinfort_est,aviq,2025,5400000,,,estimate,src_ccrek_aviq_branch_parlement_bi2025,medium,Staff reinfort MR estimate 5.4m within 6.8m CoA questions dual measure delivery; tick655",
    # Parlement
    "bud_parlement_wal_ce_bi2025,parlement_wallonie,2025,77437000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,DO01 Parlement CE=CL BI2025 77.437m path +1.058m; tick655",
    "bud_parlement_wal_dot_bi2025,parlement_wallonie,2025,75572000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Dotation Parlement Wallonie BI2025 75.572m path +1.024m; tick655",
    "bud_mediateur_wal_bi2025,mediateur_wallonie,2025,1865000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Mediateur RW BI2025 1.865m path +0.034m; tick655",
    "bud_parlement_wal_exec_12nov2024,parlement_wallonie,2024,76379000,,,outturn,src_ccrek_aviq_branch_parlement_bi2025,strong,Parlement exec CL 12Nov2024 76.379m (100pct BA); tick655",
    # Cabinets by minister
    "bud_cabinet_mp_budget_bi2025,do02_cabinets_wal,2025,5401000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet MP Budget/Finances/Recherche BI2025 5.401m path +0.350m; tick655",
    "bud_cabinet_territoire_bi2025,do02_cabinets_wal,2025,5177000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Territoire/Mobilite/PL BI2025 5.177m path +0.671m; tick655",
    "bud_cabinet_economie_bi2025,do02_cabinets_wal,2025,5325000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Economie/Emploi/Numerique BI2025 5.325m path +0.664m; tick655",
    "bud_cabinet_sante_bi2025,do02_cabinets_wal,2025,3251000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Sante/Env/Solidarites BI2025 3.251m path -0.788m; tick655",
    "bud_cabinet_fp_bi2025,do02_cabinets_wal,2025,1556000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Fonction publique/Sports BI2025 1.556m path -0.907m; tick655",
    "bud_cabinet_tourisme_bi2025,do02_cabinets_wal,2025,1408000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Tourisme/Patrimoine/PE BI2025 1.408m path -1.211m; tick655",
    "bud_cabinet_energie_bi2025,do02_cabinets_wal,2025,2954000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Energie/Climat/Logement/Aeroports BI2025 2.954m path -0.284m; tick655",
    "bud_cabinet_agriculture_bi2025,do02_cabinets_wal,2025,2954000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Cabinet Agriculture/Ruralite BI2025 2.954m path -0.146m; tick655",
    # SEC other corrections
    "bud_sec_other_corr_total_bi2025,wallonie_gov,2025,161100000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Autres corrections SEC BI2025 161.1m; tick655",
    "bud_sec_corr_hospital_capital_bi2025,wallonie_gov,2025,103300000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Hospital past+new invest capital fed refund corr 103.3m; tick655",
    "bud_sec_corr_green_certs_bi2025,wallonie_gov,2025,33000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Certificats verts SEC corr 33.0m WFE projections; tick655",
    "bud_sec_corr_succession_lag_bi2025,wallonie_gov,2025,32000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Succession cash lag 2-month corr 32.0m; tick655",
    "bud_sec_corr_garanties_std_bi2025,wallonie_gov,2025,-5000000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Garanties standardisees SEC corr -5.0m; tick655",
    "bud_sec_corr_amendes_routieres_bi2025,wallonie_gov,2025,-3100000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Decomptes amendes routieres -3.1m; tick655",
    "bud_sec_corr_leasing_cauchy_bi2025,wallonie_gov,2025,300000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Leasing financier Cauchy +0.3m; tick655",
    "bud_sec_corr_galileo_bi2025,wallonie_gov,2025,700000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Projet Galileo +0.7m; tick655",
    "bud_ocpp_requalif_effective_margin_bi2025,ocpp_wal,2025,75800000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,Effective requalif margin 75.8m after ICN 49.6m of 125.4m; tick655",
    "bud_icn_requalif_known_bi2025,ocpp_wal,2025,49600000,,,budgeted,src_ccrek_aviq_branch_parlement_bi2025,strong,ICN already requalified ops 49.6m in BI2025 projects (Sowaer 0.4 energy 0.4 avances 48.8); tick655",
]

cmt_rows = [
    'cmt_aviq_branch_coa_bi2025,AViQ branch residual CoA s8.2 Table34 dual VAPH,aviq,Elderly disability health family providers,CoA s8.2 + Table34,2024-11-15,2025,2025,7255891000,"{""rec_m"":6876.645,""dep_m"":7255.891,""result_m"":-379.246,""remonte_m"":335.3,""consol_impact_m"":-330.6,""inexec_m"":48.6,""nonmarchand_m"":276.2,""index_m"":128.4,""papyboom_eng_m"":23.7,""priority_places_m"":79.9,""prevention_m"":40,""note"":""Strong CoA; dual VAPH residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,AViQ multi-branch health social disability,FOI bed/places L5 dual VAPH,src_ccrek_aviq_branch_parlement_bi2025,strong,Wallonie>AViQ>Branch,tick655',
    'cmt_aviq_papyboom_coa_bi2025,AViQ Papy-boom elderly beds residual CoA,aviq,Rest homes MR MRS operators,Plan Papy-boom + CoA,2024-11-15,2025,2025,23700000,"{""eng_m"":23.7,""liq_m"":19.9,""encours_m"":34.0,""cum_eng_m"":113.5,""cum_liq_m"":80.2,""beds_residual_recond"":1886,""beds_principle"":442,""done_recond"":331,""done_principle"":173,""note"":""Strong CoA; delivery lag residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Elderly accommodation investment residual,Publish bed delivery FOI dual VSB,src_ccrek_aviq_branch_parlement_bi2025,strong,Wallonie>AViQ>Papyboom,tick655',
    'cmt_parlement_wal_coa_bi2025,Parlement Wallonie DO01 CoA dual VL,parlement_wallonie,Parliament + Mediateur,Budget DO01,2024-11-15,2025,2025,77437000,"{""total_m"":77.437,""dot_m"":75.572,""mediateur_m"":1.865,""path_m"":1.058,""exec_pct"":100,""note"":""Strong CoA; dual VL Parlement""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Walloon Parliament dotation,Benchmark dual VL FOI,src_ccrek_aviq_branch_parlement_bi2025,strong,Wallonie>Parlement,tick655',
    'cmt_cabinets_by_minister_bi2025,Cabinets by minister L5 CoA annex BI2025,do02_cabinets_wal,8 ministerial cabinets,Budget DO02 annex,2024-11-15,2025,2025,28026000,"{""mp_m"":5.401,""territoire_m"":5.177,""economie_m"":5.325,""sante_m"":3.251,""fp_m"":1.556,""tourisme_m"":1.408,""energie_m"":2.954,""agri_m"":2.954,""note"":""Strong CoA annex; sum class matches DO02 residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cabinet subsistence by minister,Publish FTE FOI dual VL,src_ccrek_aviq_branch_parlement_bi2025,strong,Wallonie>DO02>Cabinets_L5,tick655',
    'cmt_sec_other_corr_bi2025,SEC other corrections 161.1m CoA BI2025,wallonie_gov,Hospital green certs succession guarantees,CoA s2.2.3.3,2024-11-15,2025,2025,161100000,"{""total_m"":161.1,""hospital_m"":103.3,""green_certs_m"":33.0,""succession_lag_m"":32.0,""guarantees_m"":-5.0,""fines_m"":-3.1,""requalif_effective_m"":75.8,""icn_known_m"":49.6,""note"":""Strong CoA; effective margin residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,SEC financing corrections residual,FOI interest paid vs accrued missing,src_ccrek_aviq_branch_parlement_bi2025,strong,Wallonie>SEC>Other_corr,tick655',
]

lb_rows = [
    "lb_aviq_dep_7_26bn_table34_2025,AViQ dep Table34 7.256bn dual VAPH,Wallonia,ops,Wallonie>AViQ>Dep_7_26bn,7255891000,7255891000,Strong CoA Table34: dep 7255.891m path +287m; remonte drives result -379m,strong,src_ccrek_aviq_branch_parlement_bi2025,WAL health disability aging families,AViQ full budget residual,Core social dual VAPH; remonte residual,3.5,9.5,4,6.30,FOI branch L5 dual VAPH,seed,,tick655",
    "lb_aviq_nonmarchand_276m_2025,AViQ non-marchand 276.2m path +151m,Wallonia,ops,Wallonie>AViQ>Nonmarchand_276m,276200000,276200000,Strong CoA: non-marchand 276.2m path +151.1m vs BI2024 125.1m,strong,src_ccrek_aviq_branch_parlement_bi2025,Non-market social sector,Non-marchand wage accords,Core social path dual residual,4.0,7.5,3,5.55,FOI employer L5,seed,,tick655",
    "lb_aviq_papyboom_residual_2025,AViQ Papy-boom beds residual dual VSB,Wallonia,ops,Wallonie>AViQ>Papyboom,23700000,113500000,Strong CoA: eng 23.7m cum eng 113.5m; residual 1886 recond +442 principle beds,strong,src_ccrek_aviq_branch_parlement_bi2025,Elderly home operators,Elderly bed investment residual,Delivery lag residual dual,5.5,5.5,4,5.25,FOI bed delivery dual VSB,seed,,tick655",
    "lb_aviq_prevention_40m_prw_shift_2025,AViQ prevention 40m structuralize from PRW,Wallonia,ops,Wallonie>AViQ>Prevention_40m,40000000,40000000,Strong CoA: +40m (promo 15 + ETP-PSY 8.6 + provision 16.4) from PRW to structural,strong,src_ccrek_aviq_branch_parlement_bi2025,Health promo actors,Prevention structuralize residual,PRW to structural dual residual,5.0,5.5,3,5.05,FOI project L5 provision 16.4m,seed,,tick655",
    "lb_parlement_wal_77m_2025,Parlement Wallonie 77.4m dual VL,Wallonia,ops,Wallonie>Parlement>77m,77437000,77437000,Strong CoA DO01: 77.437m path +1.058m exec 100pct; dual VL,strong,src_ccrek_aviq_branch_parlement_bi2025,Democratic institutions,Parliament dotation,Core institution dual residual,3.0,6.0,2,4.50,Benchmark dual VL FOI,seed,,tick655",
    "lb_dual_aviq_vaph_branch_2025,Dual AViQ 7.26bn branch vs VL VAPH VSB,Belgium,ops,Belgium>Social>dual_AViQ_VAPH,7255891000,0,Strong dual: AViQ 7.256bn non-marchand 276m Papy-boom residual vs VAPH/VSB/Opgroeien; not TE-additive,strong,src_dual_aviq_vaph_tick655,BE social care recipients,Parallel regional care stacks,Institutional dual residual,5.5,9.0,4,6.70,Unit-cost dual FOI,seed,,tick655",
]

foi_row = (
    f"{GAP},Wallonie>AViQ_Parlement>L5_2025,aviq,"
    "AViQ branch L5: Papy-boom bed delivery; priority places list; prevention provision 16.4m projects; "
    "non-marchand employer matrix; MR/MRS programming 2024-25 assignment; cabinets FTE; dual VAPH,"
    "CoA AViQ s8.2 + DO01 totals strong tick655; L5 residual dual,"
    "5,AViQ / Parlement wallon / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_aviq_branch_coa_bi2025|cmt_aviq_papyboom_coa_bi2025|cmt_dual_aviq_vaph_branch_2025,"
    "lb_aviq_dep_7_26bn_table34_2025|lb_aviq_papyboom_residual_2025|lb_dual_aviq_vaph_branch_2025,"
    f"{NOW},{NOW},tick655 CoA AViQ branch Parlement primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW §8.2 AViQ Table 34 + DO01; dual VAPH prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: AViQ / Parlement wallon / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — AViQ branches L5 + Parlement/cabinets 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Plan Papy-boom: état des 1.886 lits à reconditionner et 442 en
   accord de principe; engagements/liquidations 2023-2025 (CoA:
   cum eng 113,5 mEUR / liq 80,2 mEUR mi-nov 2024).
2. Liste des 100 places prioritaires handicap 2025 et des 1.371 prises
   en charge nominatives (18/11/2024).
3. Ventilation de la provision prévention 16,4 mEUR et bénéficiaires
   promotion santé 15 mEUR + ETP PSY 8,6 mEUR.
4. Matrice employeurs non-marchand 276,2 mEUR BI2025.
5. Affectation des tranches MR/MRS/CSJ 2024-2025 (programmation
   +1.130 MR +48 CSJ/an sur 10 ans — CoA: partiellement atteinte).
6. Effectifs FTE par cabinet ministériel 2025 (subsistance DO02).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 §8.2 + Table 34 + DO annex.
- Dual VL: VAPH / VSB / Opgroeien / Parlement (prior).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual social/admin hole-fill -- **AViQ branch residual + Parlement/cabinets + SEC corr** dual VAPH)
- Found: **AViQ Table34** (primary CoA s8.2): rec **EUR6.877bn** / dep **EUR7.256bn** / result **-EUR379m** (remonte **EUR335m**); consol impact **-EUR330.6m** after inexec **EUR48.6m**. **Non-marchand EUR276.2m** (path **+EUR151m**). Index **+EUR128.4m**. **Papy-boom** eng **EUR23.7m** / cum eng **EUR113.5m** / residual beds **1886+442**. Priority places **EUR79.9m**. Prevention **EUR40m** (PRW structuralize). Safa **+EUR4.4m**; MR/MRS **+EUR6.8m**. **Parlement DO01 EUR77.4m** (mediateur **EUR1.9m**). Cabinets L5: MP **EUR5.4m** / Eco **EUR5.3m** / Territoire **EUR5.2m**. SEC other corr **EUR161m** (hospital **EUR103m**). Dual **VAPH**. Strong confidence CoA; bed/places L5 residual FOI.
- Wrote: entities (+2); budgets (+45); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@660 in 5 ticks; rq_116 deferred
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
        f"tick{TICK} AViQ branch non-marchand 276m Papy-boom dual VAPH; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after AViQ branch dual; rq_116 deferred; progress@660 in 5",
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
