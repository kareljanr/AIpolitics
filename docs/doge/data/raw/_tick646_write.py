# -*- coding: utf-8 -*-
"""Tick 646: DO10 Secrétariat général + PRW/FRR dual VV — rq_637."""
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T03:15:00Z"
TICK = 646
RQ = "rq_637"
NEXT_RQ = "rq_638"
GAP = "gap_do10_prw_frr_l5_2025"


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
            # task_id,title,sprint,priority,status,... notes last
            if len(parts) >= 5:
                parts[4] = "done"
            # updated_utc is index 10 typically
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
        f"tick{TICK} DO10 PRW FRR 2.255bn CL dual VV; "
        f"next {NEXT_RQ}; progress@650 in 4; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


# --- entities ---
ent_rows = [
    "do10_secretariat_wal,DO10 Secretariat general Wallonie,Division organique 10 Secretariat general RW,Walloon DO10 general secretariat PRW FRR holder,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA BI2025 CE 732.811m CL 2274.208m path eng -1303.115m liq -117.339m; prog122 PRW+FRR CL 2254.954m; dual VL VV; tick646",
    "prw_frr_wallonie,PRW FRR Wallonie prog 10.122,Plan de relance de la Wallonie et FRR europeen,Walloon recovery plan + EU RRF provision dual Vlaamse Veerkracht,programme,do10_secretariat_wal,fr,https://www.wallonie.be,,,CoA BI2025 CE 713.5m CL 2254.954m path eng -1286.432m; FRR rec 920m RePower 109.6m; traj 2240m to 150m 2028; dual VV 4.2bn cum; tick646",
]

# --- sources ---
src_rows = [
    "src_ccrek_do10_prw_frr_bi2025,CoA Budget RW DO10 Secretariat PRW FRR dual VV,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick646: DO10 BI2025 CE 732811k CL 2274208k path eng -1303115k liq -117339k vs BA2024 2035926/2391547; exec class 638794k; prog122 PRW+FRR CE 713500k CL 2254954k path eng -1286432k liq +15950k vs BA 1999932/2239004; exec class 4586k; prog028 Plan relance zeroed path -6520/-119491; FRR rec BI2025 920m + RePower 109.6m; provision PRW eng 444.1m path -43.7pct vs BI2024 1016.6m; traj PRW 2240m BI2025 to 150m 2028-29 (2026 class 1180.6m); BA2024 adj FRR eng +447m liq +200m; dual VL VV",
    "src_dual_prw_vv_recovery_tick646,Dual WAL PRW FRR DO10 vs VL Vlaamse Veerkracht,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA DO10 + prior VV,2026-08-01,synthesis,Strong dual: WAL prog122 CL 2.255bn CE 713.5m + FRR 920m RePower 109.6m vs VL VV cum commit 4.2bn paid 3.5bn open 0.7bn spend2025 399.4m underuse 342m; not TE-additive; tick646",
]

# --- budgets (kEUR * 1000 = EUR) ---
bud_rows = [
    "bud_do10_ce_bi2025,do10_secretariat_wal,2025,732811000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 Secretariat BI2025 CE 732.811m path eng -1303.115m vs BA2024 2035.926m; tick646",
    "bud_do10_cl_bi2025,do10_secretariat_wal,2025,2274208000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 Secretariat BI2025 CL 2274.208m path liq -117.339m vs BA2024 2391.547m; tick646",
    "bud_do10_ce_ba2024,do10_secretariat_wal,2024,2035926000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 BA2024 CE 2035.926m (pre path to BI2025); tick646",
    "bud_do10_cl_ba2024,do10_secretariat_wal,2024,2391547000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 BA2024 CL 2391.547m; tick646",
    "bud_do10_exec_class_coa,do10_secretariat_wal,2024,638794000,,,outturn,src_ccrek_do10_prw_frr_bi2025,strong,DO10 CoA table execution class 638.794m (reference col); tick646",
    "bud_do10_path_eng_bi2025,do10_secretariat_wal,2025,-1303115000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 path eng -1303.115m BI2025 vs BA2024; tick646",
    "bud_do10_path_liq_bi2025,do10_secretariat_wal,2025,-117339000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 path liq -117.339m BI2025 vs BA2024; tick646",
    # prog 122 already has CE/CL from tick642 - add path/exec/BA/recettes
    "bud_prw_122_ce_ba2024,prw_frr_wallonie,2024,1999932000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog122 PRW+FRR BA2024 CE 1999.932m; tick646",
    "bud_prw_122_cl_ba2024,prw_frr_wallonie,2024,2239004000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog122 PRW+FRR BA2024 CL 2239.004m; tick646",
    "bud_prw_122_path_eng_bi2025,prw_frr_wallonie,2025,-1286432000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog122 path eng -1286.432m BI2025 (CE 713.5 from 2000); tick646",
    "bud_prw_122_path_liq_bi2025,prw_frr_wallonie,2025,15950000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog122 path liq +15.950m BI2025; tick646",
    "bud_prw_122_exec_class_coa,prw_frr_wallonie,2024,4586000,,,outturn,src_ccrek_do10_prw_frr_bi2025,medium,Prog122 CoA execution class only 4.586m vs CL 2.255bn opacity signal; tick646",
    "bud_prw_provision_eng_bi2025,prw_frr_wallonie,2025,444100000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Provision Plan de relance wallon eng 444.1m BI2025 path -43.7pct vs BI2024 1016.6m; tick646",
    "bud_prw_provision_eng_bi2024,prw_frr_wallonie,2024,1016600000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Provision PRW eng BI2024 1016.6m; tick646",
    "bud_frr_recettes_bi2025,prw_frr_wallonie,2025,920000000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,FRR/RRF recettes BI2025 920.0m (two AB half code8); tick646",
    "bud_repower_eu_recettes_bi2025,prw_frr_wallonie,2025,109600000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,RePower EU recettes BI2025 109.6m half code8; tick646",
    "bud_frr_rrf_repower_rec_sum_bi2025,prw_frr_wallonie,2025,1029600000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,FRR 920 + RePower 109.6 = 1029.6m class (matches recettes RRF line prior); tick646",
    "bud_frr_ba2024_adj_eng,prw_frr_wallonie,2024,447000000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,BA2024 adjustment FRR DF122.002/003 eng +447.0m; tick646",
    "bud_frr_ba2024_adj_liq,prw_frr_wallonie,2024,200000000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,BA2024 adjustment FRR liq +200.0m; tick646",
    "bud_prw_traj_bi2025_class,prw_frr_wallonie,2025,2240000000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Gouv trajectory: plan de relance spend class 2240m at BI2025 project; tick646",
    "bud_prw_traj_2026_class,prw_frr_wallonie,2026,1180600000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Trajectory PRW-linked spend class 1180.6m in 2026; tick646",
    "bud_prw_traj_2028_class,prw_frr_wallonie,2028,150000000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Trajectory PRW spend class 150m in 2028 and 2029; tick646",
    "bud_prw_prog028_cl_ba2024,prw_frr_wallonie,2024,119491000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog028 Plan de relance BA2024 CL 119.491m zeroed BI2025 (reclass to 122); tick646",
    "bud_prw_prog028_path_liq_bi2025,prw_frr_wallonie,2025,-119491000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,Prog028 path liq -119.491m BI2025 (zeroed); tick646",
    "bud_do10_018_tourisme_cl_bi2025,do10_secretariat_wal,2025,69868000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 prog018 Tourisme CL BI2025 69.868m path -4.904m; tick646",
    "bud_do10_019_rel_ext_cl_bi2025,do10_secretariat_wal,2025,30698000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 prog019 Relations exterieures CL 30.698m path -7.589m; tick646",
    "bud_do10_020_awex_cl_bi2025,do10_secretariat_wal,2025,67547000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO10 prog020 Commerce exterieur AWEX CL 67.547m path -9.428m; tick646",
    "bud_do12_digital_cl_bi2025,wallonie_gov,2025,55060000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO12 Digital CL BI2025 55.060m path -0.615m (companion to DO10); tick646",
    "bud_do12_gestion_digital_cl_bi2025,wallonie_gov,2025,54914000,,,budgeted,src_ccrek_do10_prw_frr_bi2025,strong,DO12 prog029 Gestion du digital CL 54.914m; tick646",
]

# --- commitments ---
cmt_rows = [
    'cmt_do10_secretariat_coa_bi2025,DO10 Secretariat general CoA BI2025,do10_secretariat_wal,SPW SG / PRW operators / AWEX / Tourisme / WBI channel,Decret budget RW + CoA 2024_63,2024-11-15,2025,2025,2274208000,"{""ce_m"":732.811,""cl_m"":2274.208,""path_eng_m"":-1303.115,""path_liq_m"":-117.339,""ba_ce_m"":2035.926,""ba_cl_m"":2391.547,""exec_class_m"":638.794,""prog122_cl_m"":2254.954,""note"":""Strong CoA annex DO table; PRW dominates CL""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,General secretariat + recovery provision holder,Publish L5 DF map for 122; dual VV ROI,src_ccrek_do10_prw_frr_bi2025,strong,Wallonie>DO10>Secretariat,tick646 primary CoA',
    'cmt_prw_frr_prog122_bi2025,PRW FRR programme 10.122 BI2025 dual VV,prw_frr_wallonie,PRW project promoters Sofico OTW AViQ Forem,Plan de relance Wallonie + NextGenEU RRF,2021-01-01,2025,2029,2254954000,"{""ce_m"":713.5,""cl_m"":2254.954,""path_eng_m"":-1286.432,""path_liq_m"":15.95,""ba_ce_m"":1999.932,""ba_cl_m"":2239.004,""provision_eng_m"":444.1,""provision_eng_bi2024_m"":1016.6,""frr_rec_m"":920,""repower_rec_m"":109.6,""traj_2025_m"":2240,""traj_2026_m"":1180.6,""traj_2028_m"":150,""exec_class_m"":4.586,""note"":""Strong CoA; eng collapse vs sticky CL; dual VV 4.2bn cum""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Recovery and resilience investment Wallonia,Sunset trajectory; FOI project L5; dual VV underuse,src_ccrek_do10_prw_frr_bi2025,strong,Wallonie>DO10>PRW_FRR,tick646',
    'cmt_frr_repower_recettes_bi2025,FRR RePower EU recettes Wallonie BI2025,prw_frr_wallonie,EU Commission RRF disbursements,Next Generation EU RRF + RePowerEU,2021-06-16,2025,2026,1029600000,"{""frr_m"":920,""repower_m"":109.6,""sum_m"":1029.6,""half_code8"":true,""ba2024_adj_eng_m"":447,""ba2024_adj_liq_m"":200,""note"":""Strong CoA 4.5.2; milestone-conditional""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,EU recovery receipts,Track milestones; dual BE RRF,src_ccrek_do10_prw_frr_bi2025,strong,Wallonie>Recettes>FRR_RePower,tick646',
    'cmt_dual_prw_vv_2025,Dual WAL PRW FRR vs VL Vlaamse Veerkracht,prw_frr_wallonie,Regional recovery operators dual,CoA WAL + CoA VL RR2025,2021-01-01,2025,2026,0,"{""wal_cl_m"":2254.954,""wal_ce_m"":713.5,""wal_frr_rec_m"":920,""wal_traj_2028_m"":150,""vl_cum_commit_bn"":4.2,""vl_paid_bn"":3.5,""vl_open_bn"":0.7,""vl_spend_2025_m"":399.4,""vl_underuse_2025_m"":342.1,""note"":""Not TE-additive dual recovery stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional recovery dual map,Publish cross-region L5 ROI,src_dual_prw_vv_recovery_tick646,strong,Belgium>Recovery>dual_WAL_VL,tick646',
    'cmt_do12_digital_companion_bi2025,DO12 Digital companion to DO10 BI2025,wallonie_gov,ADN / SPW digital,Budget RW DO12,2024-11-15,2025,2025,55060000,"{""ce_m"":53.854,""cl_m"":55.060,""prog029_cl_m"":54.914,""path_eng_k"":-420,""path_liq_k"":-615,""exec_class_m"":35.578,""note"":""Companion digital dual Smals ADN""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Regional digital ops,Dual Digitaal Vlaanderen residual,src_ccrek_do10_prw_frr_bi2025,strong,Wallonie>DO12>Digital,tick646',
]

# --- leaderboard ---
lb_rows = [
    "lb_do10_cl_2_27bn_2025,DO10 Secretariat CL 2.274bn BI2025,Wallonia,ops,Wallonie>DO10>Secretariat>cl_2_27bn,2274208000,2274208000,Strong CoA: DO10 CL 2274.208m CE 732.811m path eng -1303m; PRW-dominated,strong,src_ccrek_do10_prw_frr_bi2025,WAL taxpayers PRW operators,SG + recovery provision,Mega provision opacity residual,6.5,8.5,4,6.95,FOI DF L5 map dual VV,seed,,tick646",
    "lb_prw_122_cl_2_25bn_2025,PRW FRR prog122 CL 2.255bn BI2025,Wallonia,ops,Wallonie>DO10>PRW_FRR>cl_2_25bn,2254954000,2254954000,Strong CoA: prog122 CL 2254.954m CE only 713.5m path eng -1286m; sticky liq,strong,src_ccrek_do10_prw_frr_bi2025,Recovery project promoters,Plan de relance + RRF,Eng collapse vs CL stickiness dual VV,7.0,8.5,4,7.15,FOI project L5 + milestone map,seed,,tick646",
    "lb_prw_provision_444m_2025,PRW provision eng 444.1m path -43.7pct,Wallonia,ops,Wallonie>DO10>PRW>provision_444m,444100000,444100000,Strong CoA: provision eng 444.1m from 1016.6m (-43.7pct),strong,src_ccrek_do10_prw_frr_bi2025,PRW reallocation recipients,Recovery provision taper,Still large unallocated pool FOI,6.5,7.5,4,6.55,Publish allocation circular FOI,seed,,tick646",
    "lb_frr_recettes_920m_2025,FRR recettes 920m + RePower 109.6m BI2025,Wallonia,ops,Wallonie>Recettes>FRR_920m,920000000,1029600000,Strong CoA 4.5.2: FRR 920m RePower 109.6m half code8; milestone-conditional,strong,src_ccrek_do10_prw_frr_bi2025,EU + WAL taxpayers,RRF receipts,Conditional on reforms; dual BE RRF,5.5,8.0,4,6.35,Track Commission milestones,seed,,tick646",
    "lb_prw_traj_sunset_150m_2028,PRW trajectory sunset to 150m 2028-29,Wallonia,ops,Wallonie>DO10>PRW>traj_150m_2028,150000000,2240000000,Strong CoA: traj 2240m BI2025 to 1180.6m 2026 to 150m 2028-29; deficit path driver,strong,src_ccrek_do10_prw_frr_bi2025,Future WAL budgets,Recovery sunset,Honest taper if delivered; structuralise risk,6.0,7.5,3,6.30,Lock structural vs temporary FOI,seed,,tick646",
    "lb_dual_prw_vv_recovery_2025,Dual WAL PRW 2.25bn CL vs VL VV 4.2bn cum,Belgium,ops,Belgium>Recovery>dual_PRW_VV,2254954000,0,Strong dual synthesis: WAL CL 2.255bn CE 714m + FRR 920m vs VL cum 4.2/3.5/0.7bn spend399 underuse342; not TE-additive,strong,src_dual_prw_vv_recovery_tick646,BE recovery taxpayers,Parallel regional recovery stacks,Dual opacity underuse residual,6.5,8.0,4,6.70,Cross-region L5 ROI FOI,seed,,tick646",
]

# --- FOI queue ---
foi_row = (
    f"{GAP},Wallonie>DO10>PRW_FRR>L5_2025,prw_frr_wallonie,"
    "Prog122 DF L5 map (122.001/002/003/074/328); provision 444.1m allocation; "
    "FRR 920 + RePower 109.6 milestone status; project list dual Sofico OTW AViQ Forem; "
    "exec class 4.6m vs CL 2.255bn recon; dual VV underuse,"
    "CoA DO10 totals strong tick646; L5 residual dual recovery,"
    "5,SPW Budget / SPW SG / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_do10_secretariat_coa_bi2025|cmt_prw_frr_prog122_bi2025|cmt_dual_prw_vv_2025,"
    "lb_do10_cl_2_27bn_2025|lb_prw_122_cl_2_25bn_2025|lb_dual_prw_vv_recovery_2025,"
    f"{NOW},{NOW},tick646 CoA DO10 PRW FRR primary; residual L5 dual human send"
)

# --- FOI draft ---
foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW DO10 + PRW/FRR (2024_63); dual VL Vlaamse Veerkracht prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / SPW Secrétariat général / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — DO10 Secrétariat / PRW-FRR L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Ventilation L5 du programme 10.122 PRW+FRR BI2025
   (CoA: CE 713.500.000 EUR / CL 2.254.954.000 EUR):
   DF 122.001 Plan de relance, 122.002 provision FRR, 122.003
   préfinancement FRR, 122.074 Réserve Ukraine, 122.328 RePowerEU,
   et tout autre DF du programme 122.
2. Liste des projets PRW et RRF avec montants engagés/liquidés
   2023-2025 et bénéficiaires (y compris Sofico, OTW, AViQ, Forem,
   et autres UAP), réconciliation avec la provision engagée
   444,1 mEUR (path -43,7 % vs 1.016,6 mEUR BI2024).
3. Justification de la colonne d'exécution CoA ~4,586 mEUR pour
   le prog.122 face au CL 2.255 mEUR (réconciliation encours /
   codes 8 / provisions non liquidées).
4. État d'avancement des jalons Commission pour les recettes FRR
   920 mEUR et RePower EU 109,6 mEUR BI2025 (versements reçus vs
   prévus; risques de non-décaissement).
5. Trajectoire pluriannuelle PRW 2025-2029 (CoA: 2.240 m → 1.180,6 m
   en 2026 → 150 m en 2028-2029): part structurelle vs temporaire
   après extinction.
6. Cartographie des crédits de liquidation PRW non encore portés
   sur une adresse budgétaire spécifique (ex. OTW 78,4 mEUR rec.,
   Sofico 33,4 mEUR) au BGD 2025.

Période: 2023-01-01 à 2026-12-31 (et projections 2027-2029 si disponibles).
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Tables DO annex + §4.5.2 + §5 DO10.
- Dual VL: Vlaamse Veerkracht cum commit ~€4.2bn / paid ~€3.5bn / open ~€0.7bn;
  2025 spend €399.4m underuse €342m (prior ticks).
- Do **not** send as agent; human identity + send only.
"""

# --- log entry ---
log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual recovery hole-fill -- **DO10 Secretariat + PRW/FRR** dual VV)
- Found: **DO10** (primary CoA): BI2025 CE **EUR732.8m** / CL **EUR2.274bn** (path eng **-EUR1.303bn** / liq **-EUR117.3m**). **Prog 122 PRW+FRR:** CE **EUR713.5m** / CL **EUR2.255bn** (path eng **-EUR1.286bn** / liq **+EUR16.0m**); provision eng **EUR444.1m** (path **-43.7%** vs BI2024 **EUR1.017bn**); exec class only **EUR4.6m** vs CL 2.255bn. **FRR rec EUR920m** + **RePower EUR109.6m**. Trajectory **EUR2.240bn** BI2025 → **EUR1.181bn** 2026 → **EUR150m** 2028-29. Prog028 zeroed (**-EUR119.5m** CL reclass). Companion **DO12 Digital** CL **EUR55.1m**. Dual **Vlaamse Veerkracht** cum **EUR4.2bn** / paid **EUR3.5bn** / underuse 2025 **EUR342m**. Strong confidence CoA; project L5 residual FOI.
- Wrote: entities (+2); budgets (+28); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@650 in 4 ticks; rq_116 deferred
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
        f"tick{TICK} DO10 PRW FRR CL 2.255bn dual VV; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after DO10 PRW dual; rq_116 deferred; progress@650 in 4",
    )
    set_loop_state(ROOT / "loop_state.csv")

    log_text = read_text(LOG)
    if f"tick {TICK}" not in log_text and f"tick{TICK}" not in log_text[-2000:]:
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
