# -*- coding: utf-8 -*-
"""Tick 649: Financement alternatif + OCPP dual (CoA Table10-11) — rq_640."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T04:00:00Z"
TICK = 649
RQ = "rq_640"
NEXT_RQ = "rq_641"
GAP = "gap_fa_ocpp_requalif_l5_2025"


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
        f"tick{TICK} FA+OCPP requalif 125m dual PMV; "
        f"next {NEXT_RQ}; progress@650 NEXT; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "financement_alternatif_wal,Financement alternatif Wallonie CRAC Sowafinal,Financement alternatif et missions deleguees RW,Walloon alternative financing CRAC Sowafinal dual VL local finance,agency,wallonie_gov,fr,https://www.crac.be,,,CoA Table10 BI2025 total FA+MD 74.767m path -19.544m; FA 66.973 CRAC 13.067 Sowafinal 53.906 missions 7.794; dual VL Gemeentefonds/PMV; tick649",
    "ocpp_wal,OCPP Wallonie code8,Octrois de credits et prises de participations RW,Walloon credit grants and equity participations (ESA code8) dual PMV,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA Table11 BI2025 OCPP budget 212.113m after GW corr 435.287m expose 309.917m requalif margin 125.370m; dual PMV equity; tick649",
]

src_rows = [
    "src_ccrek_fa_ocpp_bi2025,CoA Budget RW Table10 FA missions + Table11 OCPP dual PMV,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick649: Table10 FA+MD BI2025 74767k path -19544k (BA 94311); FA 66973 (CRAC 13067 CRAC-FA 21928 CRAC-PWI -12213 CRAC-LT 3352 Sowafinal 53906 SF-I 34081 SF-II 19825); missions 7794 (SOWAER 2822 WE 13297 FLW 0 SPAQuE -8325); Sowafinal dots 72.9 vs repay 19.0; Table11 OCPP (A) 212113 dep 881173 rec 669060 path -77837; GW corr (B) 223174 (Kyoto 133368 env 10500 PRW 8106 Renopack 71200); after corr (C) 435287; expose (D) 309917 path -102232; requalif margin C-D 125370 path +35861; fiscal companion circulation 778769 TC 610164 TMC 168605 encours taxes 256.2m douteux 53.1m",
    "src_dual_fa_ocpp_wal_vl_tick649,Dual WAL FA OCPP vs VL local finance PMV,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA Table10-11 + prior VL,2026-08-01,synthesis,Strong dual: WAL FA+MD 74.8m OCPP after-corr 435m requalif 125m vs VL Gemeentefonds/PMV equity class; not TE-additive; tick649",
]

bud_rows = [
    # Table 10 FA + missions
    "bud_fa_md_total_bi2025,financement_alternatif_wal,2025,74767000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,FA+missions deleguees SEC impact BI2025 +74.767m path -19.544m; tick649",
    "bud_fa_md_total_ba2024,financement_alternatif_wal,2024,94311000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,FA+MD SEC impact BA2024 +94.311m; tick649",
    "bud_fa_total_bi2025,financement_alternatif_wal,2025,66973000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Financement alternatif subtotal BI2025 +66.973m path -11.543m; tick649",
    "bud_fa_crac_total_bi2025,crac,2025,13067000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,CRAC total FA impact BI2025 +13.067m path -13.218m; tick649",
    "bud_fa_crac_fa_bi2025,crac,2025,21928000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,CRAC financement alternatif BI2025 +21.928m path +2.135m; tick649",
    "bud_fa_crac_pwi_bi2025,crac,2025,-12213000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,CRAC FA PWI BI2025 -12.213m path +4.920m; tick649",
    "bud_fa_crac_lt_bi2025,crac,2025,3352000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,CRAC long terme BI2025 +3.352m path -20.273m; tick649",
    "bud_fa_sowafinal_total_bi2025,sowafinal,2025,53906000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Sowafinal total SEC impact BI2025 +53.906m path +1.675m; tick649",
    "bud_fa_sowafinal_i_bi2025,sowafinal,2025,34081000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Sowafinal I BI2025 +34.081m; tick649",
    "bud_fa_sowafinal_ii_bi2025,sowafinal,2025,19825000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Sowafinal II BI2025 +19.825m; tick649",
    "bud_fa_sowafinal_dots_bi2025,sowafinal,2025,72900000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Sowafinal dots verses 72.9m vs repay charges 19.0m (positive SEC); tick649",
    "bud_fa_sowafinal_repay_bi2025,sowafinal,2025,19000000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Sowafinal charges remboursement emprunts 19.0m; tick649",
    "bud_md_total_bi2025,financement_alternatif_wal,2025,7794000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Missions deleguees total BI2025 +7.794m path -8.001m; tick649",
    "bud_md_sowaer_bi2025,sowaer,2025,2822000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Missions SOWAER BI2025 +2.822m; tick649",
    "bud_md_we_bi2025,wallonie_entreprendre,2025,13297000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Missions WE BI2025 +13.297m path -0.818m; tick649",
    "bud_md_spaque_bi2025,spaque,2025,-8325000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Missions SPAQuE BI2025 -8.325m path -10.774m (Sarec+Happe-Chapois); tick649",
    "bud_md_flw_bi2025,flw,2025,0,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Missions FLW BI2025 0 path +3.040m vs BA -3.040m; tick649",
    # Table 11 OCPP
    "bud_ocpp_budget_bi2025,ocpp_wal,2025,212113000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP budget net (A) BI2025 212.113m path -77.837m; tick649",
    "bud_ocpp_dep_bi2025,ocpp_wal,2025,881173000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP depenses CL BI2025 881.173m path -84.118m; tick649",
    "bud_ocpp_rec_bi2025,ocpp_wal,2025,669060000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP recettes BI2025 669.060m path -6.281m; tick649",
    "bud_ocpp_budget_ba2024,ocpp_wal,2024,289950000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP budget net BA2024 289.950m; tick649",
    "bud_ocpp_gw_corr_bi2025,ocpp_wal,2025,223174000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,GW corrections depenses non-code8 (B) BI2025 223.174m path +11.466m; tick649",
    "bud_ocpp_corr_kyoto_bi2025,ocpp_wal,2025,133368000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP corr Fonds Kyoto non-code8 133.368m BI2025; tick649",
    "bud_ocpp_corr_env_bi2025,ocpp_wal,2025,10500000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP corr Fonds protection env 10.5m; tick649",
    "bud_ocpp_corr_prw_bi2025,ocpp_wal,2025,8106000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP corr PRW invest 8.106m path -48.219m; tick649",
    "bud_ocpp_corr_renopack_bi2025,ocpp_wal,2025,71200000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP corr Ecopack/Renopack 71.2m path +43.502m; tick649",
    "bud_ocpp_after_corr_bi2025,ocpp_wal,2025,435287000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP after GW corrections (C) BI2025 435.287m path -66.371m; tick649",
    "bud_ocpp_expose_corr_bi2025,ocpp_wal,2025,309917000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,OCPP correction expose general (D) BI2025 309.917m path -102.232m; tick649",
    "bud_ocpp_requalif_margin_bi2025,ocpp_wal,2025,125370000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Marge de requalification OCPP (C-D) BI2025 125.370m path +35.861m; tick649",
    "bud_ocpp_requalif_margin_ba2024,ocpp_wal,2024,89509000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Marge requalification OCPP BA2024 89.509m; tick649",
    # Fiscal companion circulation dual VL
    "bud_fiscal_circulation_total_bi2025,wallonie_gov,2025,778769000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Impots circulation BI2025 778.769m path +39.79m vs BA 738.979; dual VL vehicle tax; tick649",
    "bud_fiscal_taxe_circulation_bi2025,wallonie_gov,2025,610164000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Taxe de circulation BI2025 610.164m path +27.055m; tick649",
    "bud_fiscal_tmc_ecomalus_bi2025,wallonie_gov,2025,168605000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,TMC+ecomalus BI2025 168.605m path +12.735m (reform 2025-07-01 +10m); tick649",
    "bud_fiscal_circulation_encours_sep2024,wallonie_gov,2024,256200000,,,outturn,src_ccrek_fa_ocpp_bi2025,strong,Encours taxes circulation 256.2m at 30Sep2024 of which douteux 53.1m; tick649",
    "bud_fiscal_circulation_douteux_sep2024,wallonie_gov,2024,53100000,,,outturn,src_ccrek_fa_ocpp_bi2025,strong,Creances douteuses circulation 53.1m of 256.2m encours; tick649",
    "bud_fiscal_jeux_paris_bi2025,wallonie_gov,2025,45000000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Jeux et paris BI2025 45.0m; tick649",
    "bud_fiscal_appareils_divert_bi2025,wallonie_gov,2025,20000000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Appareils automatiques divertissement BI2025 20.0m; tick649",
    "bud_fiscal_precompte_immo_bi2025,wallonie_gov,2025,49200000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Precompte immobilier regional share 1.25pct BI2025 49.2m; tick649",
    "bud_fiscal_taxes_automates_bi2025,wallonie_gov,2025,16800000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Taxes regionales automates BI2025 16.8m (mats pylones suppressed); tick649",
    "bud_nonfiscal_dividendes_bi2025,wallonie_gov,2025,55000000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Participation benefices entreprises 55.0m incl FN Herstal 15.0m; tick649",
    "bud_nonfiscal_fn_herstal_div_bi2025,wallonie_gov,2025,15000000,,,budgeted,src_ccrek_fa_ocpp_bi2025,strong,Dividendes FN Herstal class 15.0m within 55m; tick649",
]

cmt_rows = [
    'cmt_fa_md_coa_bi2025,Financement alternatif + missions CoA Table10 BI2025,financement_alternatif_wal,CRAC Sowafinal SOWAER WE SPAQuE FLW,Decret budget RW + CoA Table10,2024-11-15,2025,2025,74767000,"{""total_m"":74.767,""fa_m"":66.973,""crac_m"":13.067,""sowafinal_m"":53.906,""missions_m"":7.794,""path_m"":-19.544,""sowafinal_dots_m"":72.9,""sowafinal_repay_m"":19.0,""note"":""Strong CoA; positive FA impact offsets UAP deficits partially""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Alternative finance SEC impact,Publish CRAC loanbook L5 dual VL,src_ccrek_fa_ocpp_bi2025,strong,Wallonie>FA_missions,tick649',
    'cmt_ocpp_requalif_coa_bi2025,OCPP + marge requalification CoA Table11 BI2025,ocpp_wal,WE equity funds PRW Renopack Kyoto,CoA Table11 code8,2024-11-15,2025,2025,435287000,"{""budget_a_m"":212.113,""dep_m"":881.173,""rec_m"":669.060,""gw_corr_b_m"":223.174,""after_corr_c_m"":435.287,""expose_d_m"":309.917,""requalif_margin_m"":125.370,""path_margin_m"":35.861,""kyoto_corr_m"":133.368,""renopack_corr_m"":71.2,""note"":""Strong CoA; requalif margin opacity residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Financial ops code8 and reclassification,FOI line-level requalif map dual PMV,src_ccrek_fa_ocpp_bi2025,strong,Wallonie>OCPP,tick649',
    'cmt_fiscal_circulation_bi2025,Impots circulation dual VL vehicle tax BI2025,wallonie_gov,Vehicle owners,Code taxes assimilees + TMC reform 2025-07-01,2024-11-15,2025,2025,778769000,"{""total_m"":778.769,""tc_m"":610.164,""tmc_m"":168.605,""path_m"":39.79,""encours_sep2024_m"":256.2,""douteux_m"":53.1,""note"":""Strong CoA Table24; no irrecuperables provision 2025""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Regional vehicle taxation,Track TMC reform yield FOI dual VL,src_ccrek_fa_ocpp_bi2025,strong,Wallonie>Fiscal>Circulation,tick649',
    'cmt_dual_fa_ocpp_wal_vl_2025,Dual WAL FA OCPP vs VL PMV local finance,financement_alternatif_wal,Regional alternative finance dual,CoA WAL + prior VL PMV,2024-11-15,2025,2025,0,"{""wal_fa_md_m"":74.767,""wal_ocpp_after_corr_m"":435.287,""wal_requalif_m"":125.370,""wal_circulation_m"":778.769,""note"":""Not TE-additive dual finance stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional alternative finance dual,Cross-region OCPP transparency FOI,src_dual_fa_ocpp_wal_vl_tick649,strong,Belgium>FA_OCPP>dual,tick649',
    'cmt_sowafinal_dots_repay_bi2025,Sowafinal dots 72.9 vs repay 19.0 BI2025,sowafinal,Communal ZAE infra,Sowafinal programmes I-II,2024-11-15,2025,2029,72900000,"{""dots_m"":72.9,""repay_m"":19.0,""sec_impact_m"":53.906,""sf_i_m"":34.081,""sf_ii_m"":19.825,""note"":""Strong CoA; positive SEC from dots>repay""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Alternative ZAE finance residual,FOI project list dual specialty breach prior,src_ccrek_fa_ocpp_bi2025,strong,Wallonie>Sowafinal>dots_repay,tick649',
]

lb_rows = [
    "lb_ocpp_requalif_125m_2025,OCPP requalification margin 125.4m BI2025,Wallonia,ops,Wallonie>OCPP>requalif_125m,125370000,125370000,Strong CoA Table11: marge requalification C-D 125.370m path +35.9m; code8 opacity residual,strong,src_ccrek_fa_ocpp_bi2025,WAL taxpayers equity funds,Financial ops reclassification risk,High-abs accounting residual dual PMV,7.5,8.0,4,7.25,FOI line-level requalif map,seed,,tick649",
    "lb_ocpp_after_corr_435m_2025,OCPP after GW corrections 435.3m BI2025,Wallonia,ops,Wallonie>OCPP>after_corr_435m,435287000,435287000,Strong CoA: OCPP after corr 435.287m (budget 212 + GW 223 Kyoto/Renopack/PRW/env),strong,src_ccrek_fa_ocpp_bi2025,WE equity climate funds,Code8 financial operations stack,Not pure waste financial; opacity residual,6.0,8.0,4,6.50,Publish beneficiary L5 FOI,seed,,tick649",
    "lb_fa_md_75m_2025,FA+missions SEC impact +74.8m BI2025,Wallonia,ops,Wallonie>FA_missions>75m,74767000,74767000,Strong CoA Table10: FA+MD +74.767m path -19.5m; Sowafinal +53.9 CRAC +13.1,strong,src_ccrek_fa_ocpp_bi2025,Local infra communal,Alternative finance SEC buffer,Positive SEC offsets UAP deficits partially,5.0,7.0,4,5.60,FOI CRAC loanbook dual VL,seed,,tick649",
    "lb_sowafinal_dots_73m_2025,Sowafinal dots 72.9m vs repay 19m,Wallonia,ops,Wallonie>Sowafinal>dots_73m,72900000,72900000,Strong CoA: dots 72.9 vs repay 19.0 drives positive SEC +53.9m SF I+II,strong,src_ccrek_fa_ocpp_bi2025,Communal ZAE,Alternative ZAE finance residual,Dual specialty breach prior residual,5.5,7.0,4,5.85,FOI project recon cum eng,seed,,tick649",
    "lb_fiscal_circulation_779m_2025,Impots circulation 778.8m dual VL vehicle tax,Wallonia,ops,Wallonie>Fiscal>Circulation_779m,778769000,778769000,Strong CoA Table24: 778.769m TC 610 TMC 169; encours 256m douteux 53m; dual VL,strong,src_ccrek_fa_ocpp_bi2025,Vehicle owners WAL,Regional vehicle taxation,Core revenue not waste; collection residual,4.0,8.0,3,5.50,Track TMC reform + irrecuperables FOI,seed,,tick649",
    "lb_dual_fa_ocpp_wal_vl_2025,Dual WAL FA OCPP 435m vs VL PMV stack,Belgium,ops,Belgium>FA_OCPP>dual,435287000,0,Strong dual: WAL OCPP after-corr 435m requalif 125m FA+MD 75m vs VL PMV/local finance; not TE-additive,strong,src_dual_fa_ocpp_wal_vl_tick649,BE regional taxpayers,Parallel alternative finance stacks,Dual opacity residual,6.5,8.0,4,6.70,Cross-region OCPP FOI,seed,,tick649",
]

foi_row = (
    f"{GAP},Wallonie>FA_OCPP>L5_2025,ocpp_wal,"
    "OCPP line L5 code8 vs non-code8 requalif 125m map; Kyoto/Renopack/PRW/env correction "
    "beneficiary lists; CRAC FA/PWI/LT loanbook; Sowafinal dots vs repay project recon; "
    "circulation douteux 53m collection plan dual VL,"
    "CoA Table10-11 totals strong tick649; L5 residual dual,"
    "5,SPW Budget / WFE / CRAC / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_fa_md_coa_bi2025|cmt_ocpp_requalif_coa_bi2025|cmt_dual_fa_ocpp_wal_vl_2025,"
    "lb_ocpp_requalif_125m_2025|lb_ocpp_after_corr_435m_2025|lb_dual_fa_ocpp_wal_vl_2025,"
    f"{NOW},{NOW},tick649 CoA FA OCPP primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW Table 10 FA + Table 11 OCPP; dual VL PMV prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / Wallonie Finances Expertise / CRAC / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Financement alternatif + OCPP / marge requalification L5

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Ventilation L5 des OCPP code 8 BI2025 (dépenses 881,2 mEUR /
   recettes 669,1 mEUR) par bénéficiaire et nature (crédits /
   participations).
2. Cartographie de la marge de requalification 125,4 mEUR (C-D CoA
   Table 11): lignes exactes Kyoto 133,4 / Renopack 71,2 / PRW 8,1 /
   env 10,5 et justification non-code 8 vs expose général 309,9 mEUR.
3. CRAC: détail FA / FA-PWI / long terme (impacts SEC 21,9 / -12,2 /
   3,4 mEUR) — encours prêts et projets 2023-2025.
4. Sowafinal I+II: réconciliation dots 72,9 mEUR vs remboursements
   19,0 mEUR avec liste de projets (lien specialty breach DO16).
5. Missions déléguées SPAQuE (-8,3 mEUR): conventions Sarec et
   Happe-Chapois montants et calendrier.
6. Taxes circulation: plan de recouvrement de l'encours 256,2 mEUR
   dont créances douteuses 53,1 mEUR (30/09/2024).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Tables 10–11 + fiscal Tables 23–24.
- Dual VL: PMV equity / vehicle tax / local finance (prior).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual finance hole-fill -- **FA+missions Table10 + OCPP Table11** dual PMV + fiscal circulation)
- Found: **FA+MD** (primary CoA Table10): BI2025 **+EUR74.8m** (path **-EUR19.5m**). FA **EUR67.0m** (CRAC **EUR13.1m** / Sowafinal **EUR53.9m** SF-I **EUR34.1m** SF-II **EUR19.8m**; dots **EUR72.9m** vs repay **EUR19.0m**). Missions **EUR7.8m** (WE **EUR13.3m** / SPAQuE **-EUR8.3m**). **OCPP:** budget **EUR212.1m** / after GW corr **EUR435.3m** / expose **EUR309.9m** / **requalif margin EUR125.4m** (path **+EUR35.9m**; Kyoto **EUR133.4m** + Renopack **EUR71.2m**). Companion **circulation EUR778.8m** (TC **EUR610m** / TMC **EUR169m**; encours **EUR256m** douteux **EUR53m**). Dual **PMV/VL vehicle tax**. Strong confidence CoA; L5 residual FOI.
- Wrote: entities (+2); budgets (+40); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; **progress@650 NEXT tick**; rq_116 deferred
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
        f"tick{TICK} FA OCPP requalif 125m dual PMV; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch + progress@650,continuous,5,open,L5,gg_belgium,"
        f"PROGRESS MILESTONE tick650: refresh progress_every_10_ticks.md + doge_waste_top10_current.md; "
        f"then FOI-adjacent dual/L5 public fill.,,"
        f"{NOW},,Spawned tick{TICK} after FA OCPP dual; progress@650 NEXT; rq_116 deferred",
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
