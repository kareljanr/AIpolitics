# -*- coding: utf-8 -*-
"""Tick 651: IPP regional + enregistrement/succession reform dual VL — rq_642."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T04:30:00Z"
TICK = 651
RQ = "rq_642"
NEXT_RQ = "rq_643"
GAP = "gap_fiscal_ipp_enregistrement_l5_2025"


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
        f"tick{TICK} IPP 3.74bn enregistrement reform path -253m dual VL; "
        f"next {NEXT_RQ}; progress@660 in 9; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "fiscal_ipp_wal,IPP centimes additionnels Wallonie,Part regionale IPP centimes additionnels RW,Walloon personal income tax regional surcharge dual VL,agency,wallonie_gov,fr,https://www.wallonie.be,,,CoA Table21 BI2025 total 3743.367m path +228.998m; brut 4523.079 dep fiscales 882.827 net 3640.252; dual VL IPP; tick651",
    "fiscal_enregistrement_wal,Droits enregistrement succession Wallonie,Droits d enregistrement et de succession RW via Etat,Walloon registration and inheritance taxes collected by federal dual VL,agency,wallonie_gov,fr,https://finances.belgium.be,,,CoA Table22 BI2025 total 2167.322m path -233.027m; enregistrement 1273.435 path -252.978 reform 3pct cost 245.4m; succession 874.163; dual VL registration reform; tick651",
]

src_rows = [
    "src_ccrek_fiscal_ipp_enregistrement_bi2025,CoA Budget RW Table21 IPP + Table22 enregistrement succession dual VL,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick651: Table21 IPP BI2025 total 3743367k path +228998k (+6.52pct) brut 4523079 dep fiscales 882827 net 3640252 coeff 99.78pct 3632244 decomptes 113324 nonres -2201; Table22 fed-collected regional taxes BI2025 2167322k path -233027k (-9.71pct); enregistrement total 1273435 path -252978 transmissions immeubles 1004847 path -263383 (-20.77pct) hypotheque 73708 partages 29100 donations 165780; succession 874163 path +19164; interets amendes 19724; reform 3pct cost 245.4m (impact -470.7 + abattement primo suppress 94 + modestes 131.3); SPF sep est 2405924 vs budget 2167322; CoA optimistic residual on non-transmissions; federal service dots 18.1m; dual VL registration reform",
    "src_dual_fiscal_wal_vl_tick651,Dual WAL IPP enregistrement vs VL fiscal reforms,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA Table21-22 + prior VL fiscal,2026-08-01,synthesis,Strong dual: WAL IPP 3.74bn + enregistrement path -253m reform 3pct vs VL registration/inheritance reform path; not TE-additive; tick651",
]

bud_rows = [
    # Table 21 IPP
    "bud_ipp_brut_bi2025,fiscal_ipp_wal,2025,4523079000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Centimes additionnels brut BI2025 4523.079m path +240.582m (+5.62pct); tick651",
    "bud_ipp_dep_fiscales_bi2025,fiscal_ipp_wal,2025,882827000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Depenses fiscales IPP BI2025 882.827m path +33.408m; tick651",
    "bud_ipp_net_bi2025,fiscal_ipp_wal,2025,3640252000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Centimes additionnels net BI2025 3640.252m path +207.174m; tick651",
    "bud_ipp_coeff_perception_bi2025,fiscal_ipp_wal,2025,3632244000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,IPP after coeff perception 99.78pct BI2025 3632.244m; tick651",
    "bud_ipp_decomptes_bi2025,fiscal_ipp_wal,2025,113324000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Decomptes annees anterieures BI2025 113.324m path +12.510m; tick651",
    "bud_ipp_nonresidents_bi2025,fiscal_ipp_wal,2025,-2201000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Impot non-residents BI2025 -2.201m; tick651",
    "bud_ipp_total_bi2025,fiscal_ipp_wal,2025,3743367000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,IPP regional total BI2025 3743.367m path +228.998m (+6.52pct); tick651",
    "bud_ipp_total_ba2024,fiscal_ipp_wal,2024,3514369000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,IPP regional total BA2024 3514.369m; tick651",
    "bud_ipp_brut_ba2024,fiscal_ipp_wal,2024,4282497000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Centimes brut BA2024 4282.497m; tick651",
    # Table 22 enregistrement/succession
    "bud_enreg_transmissions_bi2025,fiscal_enregistrement_wal,2025,1004847000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Droits enregistrement transmissions immeubles BI2025 1004.847m path -263.383m (-20.77pct); tick651",
    "bud_enreg_hypotheque_bi2025,fiscal_enregistrement_wal,2025,73708000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Droits enregistrement hypotheque BI2025 73.708m path +1.437m; tick651",
    "bud_enreg_partages_bi2025,fiscal_enregistrement_wal,2025,29100000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Droits enregistrement partages BI2025 29.100m path +1.159m; tick651",
    "bud_enreg_donations_bi2025,fiscal_enregistrement_wal,2025,165780000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Droits enregistrement donations BI2025 165.780m path +7.809m; tick651",
    "bud_enreg_total_bi2025,fiscal_enregistrement_wal,2025,1273435000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Total droits enregistrement BI2025 1273.435m path -252.978m (-16.57pct); tick651",
    "bud_succession_bi2025,fiscal_enregistrement_wal,2025,874163000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Droits succession mutation deces BI2025 874.163m path +19.164m; tick651",
    "bud_enreg_interets_amendes_bi2025,fiscal_enregistrement_wal,2025,19724000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Interets et amendes impots regionaux BI2025 19.724m path +0.787m; tick651",
    "bud_impots_regionaux_fed_total_bi2025,fiscal_enregistrement_wal,2025,2167322000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Total impots regionaux percus par Etat BI2025 2167.322m path -233.027m (-9.71pct); tick651",
    "bud_impots_regionaux_fed_total_ba2024,fiscal_enregistrement_wal,2024,2400349000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Total impots regionaux fed BA2024 2400.349m; tick651",
    "bud_impots_regionaux_spf_sep_est,fiscal_enregistrement_wal,2025,2405924000,,,estimate,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,SPF Finances sep2024 estimate 2405.924m before regional reform correction; tick651",
    # Reform path
    "bud_enreg_reform_cost_bi2025,fiscal_enregistrement_wal,2025,245400000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Reform enregistrement net cost BI2025 245.4m CoA; tick651",
    "bud_enreg_reform_3pct_impact_bi2025,fiscal_enregistrement_wal,2025,-470700000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Reform 3pct rate negative impact -470.7m BI2025; tick651",
    "bud_enreg_reform_primo_suppress_bi2025,fiscal_enregistrement_wal,2025,94000000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Suppress abattement primo acquerant +94.0m compensation BI2025; tick651",
    "bud_enreg_reform_modestes_suppress_bi2025,fiscal_enregistrement_wal,2025,131300000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Suppress taux reduit habitations modestes +131.3m compensation BI2025; tick651",
    "bud_enreg_cheque_habitat_from2026,fiscal_enregistrement_wal,2026,0,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,medium,Cheque habitat suppress effects from 2026 only (not 2025); amount Unknown CoA; tick651",
    "bud_fiscal_fed_service_dots_bi2025,wallonie_gov,2025,18100000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Federal service dots for transferred regional taxes BI2025 18.1m (0.2m below SPF est); tick651",
    "bud_enreg_non_transmissions_avg5y,fiscal_enregistrement_wal,2024,1030100000,,,outturn,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,5y avg non-transmission regional taxes fed 1030.1m vs BI2025 1162.5m CoA optimistic residual; tick651",
    "bud_enreg_non_transmissions_bi2025_class,fiscal_enregistrement_wal,2025,1162500000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Non-transmission regional taxes class BI2025 1162.5m (succession+other excl transmissions immeubles); tick651",
    # 119quater companion residual (from DO11 deepen)
    "bud_spw_119quater_economy_gross_bi2025,wallonie_gov,2025,26100000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,119quater already statutaires 2472 agents gross employer SSC economy 26.1m/yr; tick651",
    "bud_spw_119quater_potential_full_gross,wallonie_gov,2025,43300000,,,estimate,src_ccrek_fiscal_ipp_enregistrement_bi2025,medium,If all 1635 remaining statutarisables: gross economy 43.3m/yr CoA; tick651",
    "bud_spw_119quater_economy_net_bi2025,wallonie_gov,2025,15900000,,,budgeted,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,119quater net economy after CRP 15.9m/yr (6416 EUR/agent); tick651",
]

cmt_rows = [
    'cmt_ipp_regional_coa_bi2025,IPP centimes additionnels regional CoA Table21 BI2025,fiscal_ipp_wal,Walloon PIT surcharge taxpayers,LSF + code impots + CoA Table21,2024-11-15,2025,2025,3743367000,"{""total_m"":3743.367,""brut_m"":4523.079,""dep_fiscales_m"":882.827,""net_m"":3640.252,""coeff_pct"":99.78,""decomptes_m"":113.324,""path_m"":228.998,""path_pct"":6.52,""note"":""Strong CoA Table21; dual VL IPP surcharge""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Regional PIT surcharge revenue,Publish taxex L5 within 882.8m FOI dual VL,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Wallonie>Fiscal>IPP,tick651',
    'cmt_enreg_succession_coa_bi2025,Enregistrement succession via Etat CoA Table22 BI2025,fiscal_enregistrement_wal,Property buyers heirs donors,Code droits enregistrement + reform 3pct 2025,2024-11-15,2025,2026,2167322000,"{""total_m"":2167.322,""enreg_m"":1273.435,""transmissions_m"":1004.847,""succession_m"":874.163,""path_total_m"":-233.027,""reform_cost_m"":245.4,""reform_3pct_m"":-470.7,""primo_suppress_m"":94.0,""modestes_suppress_m"":131.3,""note"":""Strong CoA; reform path dual VL""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Registration and inheritance tax reform path,Track 2025-26 reform outturn FOI dual VL,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Wallonie>Fiscal>Enregistrement,tick651',
    'cmt_enreg_reform_3pct_bi2025,Reform droits enregistrement 3pct path BI2025,fiscal_enregistrement_wal,Property acquirers primo modest homes,Decret reforme fiscale enregistrement,2024-11-15,2025,2029,245400000,"{""net_cost_2025_m"":245.4,""rate_3pct_impact_m"":-470.7,""primo_m"":94.0,""modestes_m"":131.3,""cheque_habitat_from"":2026,""traj_2026_29_m_class"":525.2,""note"":""Strong CoA; multi-year registration reform impact class 525.2m 2026-29 prior debt ch""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,3pct registration rate reform,Publish ex-post yield FOI dual VL,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Wallonie>Fiscal>Reform_3pct,tick651',
    'cmt_dual_fiscal_wal_vl_2025,Dual WAL IPP enregistrement vs VL fiscal,fiscal_ipp_wal,Regional taxpayers dual,CoA WAL + prior VL fiscal reforms,2024-11-15,2025,2026,0,"{""wal_ipp_m"":3743.367,""wal_enreg_fed_m"":2167.322,""wal_enreg_path_m"":-252.978,""wal_reform_cost_m"":245.4,""note"":""Not TE-additive dual fiscal stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional fiscal dual map,Cross-region reform ROI FOI,src_dual_fiscal_wal_vl_tick651,strong,Belgium>Fiscal>dual_WAL_VL,tick651',
    'cmt_spw_119quater_statutarisation_bi2025,SPW 119quater statutarisation economy dual,wallonie_gov,SPW contractual agents,Code fonction publique art 119quater,2022-04-01,2025,2025,15900000,"{""statutaires_done"":2472,""gross_economy_m"":26.1,""remaining"":1635,""potential_gross_m"":43.3,""net_after_crp_m"":15.9,""net_per_agent_eur"":6416,""ssc_statutaire_pct"":11.2,""ssc_contractuel_pct"":30.7,""note"":""Strong CoA DO11 deepen; DPR end-statutory risk residual""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Statutory conversion employer SSC economy,Track CRP offset FOI,src_ccrek_fiscal_ipp_enregistrement_bi2025,strong,Wallonie>Personnel>119quater,tick651',
]

lb_rows = [
    "lb_ipp_total_3_74bn_2025,IPP regional centimes 3.74bn BI2025 dual VL,Wallonia,ops,Wallonie>Fiscal>IPP_3_74bn,3743367000,3743367000,Strong CoA Table21: IPP total 3743.367m path +229m; dep fiscales 882.8m nested,strong,src_ccrek_fiscal_ipp_enregistrement_bi2025,WAL PIT surcharge taxpayers,Regional income tax surcharge,Core revenue not waste; taxex L5 residual,3.5,9.5,3,6.20,FOI taxex L5 within 882.8m dual VL,seed,,tick651",
    "lb_ipp_dep_fiscales_883m_2025,IPP depenses fiscales 882.8m BI2025,Wallonia,ops,Wallonie>Fiscal>IPP_taxex_883m,882827000,882827000,Strong CoA: dep fiscales within IPP 882.827m path +33.4m; L5 residual FOI,strong,src_ccrek_fiscal_ipp_enregistrement_bi2025,Tax expenditure beneficiaries,Regional PIT tax expenditures,Core TE layer not pure waste,5.5,8.0,4,6.35,Open L5 measure list FOI,seed,,tick651",
    "lb_enreg_transmissions_path_263m_2025,Enregistrement transmissions path -263m reform,Wallonia,ops,Wallonie>Fiscal>Enreg_path_263m,263383000,1004847000,Strong CoA: transmissions 1004.847m path -263.383m (-20.8pct) reform 3pct driver,strong,src_ccrek_fiscal_ipp_enregistrement_bi2025,Property acquirers,Registration tax reform path,Policy reform not pure waste; dual VL,5.5,8.0,3,6.20,Track ex-post yield FOI,seed,,tick651",
    "lb_enreg_reform_cost_245m_2025,Reform enregistrement net cost 245.4m BI2025,Wallonia,ops,Wallonie>Fiscal>Reform_cost_245m,245400000,245400000,Strong CoA: net cost 245.4m (3pct -470.7 + primo 94 + modestes 131.3),strong,src_ccrek_fiscal_ipp_enregistrement_bi2025,Housing market taxpayers,3pct registration reform package,Policy choice dual VL residual,6.0,7.5,3,6.30,Publish multi-year outturn FOI,seed,,tick651",
    "lb_impots_regionaux_fed_2_17bn_2025,Impots regionaux via fed 2.17bn path -233m,Wallonia,ops,Wallonie>Fiscal>Fed_collected_2_17bn,2167322000,2167322000,Strong CoA Table22: total 2167.322m path -233m; succession 874m + enreg 1273m,strong,src_ccrek_fiscal_ipp_enregistrement_bi2025,Property heirs donors,Fed-collected regional taxes,Core revenue path reform residual,4.0,8.5,3,5.85,Dual VL registration/inheritance FOI,seed,,tick651",
    "lb_dual_fiscal_wal_vl_2025,Dual WAL IPP 3.74bn enreg reform vs VL fiscal,Belgium,ops,Belgium>Fiscal>dual_WAL_VL,3743367000,0,Strong dual: WAL IPP 3.74bn + enreg path -253m reform 245m vs VL fiscal reform stacks; not TE-additive,strong,src_dual_fiscal_wal_vl_tick651,BE regional taxpayers,Parallel regional fiscal reforms,Dual opacity residual,6.0,8.5,4,6.65,Cross-region reform ROI FOI,seed,,tick651",
]

foi_row = (
    f"{GAP},Wallonie>Fiscal>IPP_Enregistrement>L5_2025,fiscal_ipp_wal,"
    "IPP dep fiscales 882.8m L5 measure list; enregistrement reform 3pct ex-post vs 245.4m; "
    "succession series; SPF vs budget recon; cheque habitat 2026; dual VL registration reform,"
    "CoA Table21-22 totals strong tick651; L5 residual dual fiscal,"
    "5,SPW Fiscalite / SPF Finances / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_ipp_regional_coa_bi2025|cmt_enreg_succession_coa_bi2025|cmt_dual_fiscal_wal_vl_2025,"
    "lb_ipp_total_3_74bn_2025|lb_enreg_reform_cost_245m_2025|lb_dual_fiscal_wal_vl_2025,"
    f"{NOW},{NOW},tick651 CoA fiscal IPP enregistrement primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW Table 21 IPP + Table 22 enregistrement/succession; dual VL fiscal prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Fiscalité / SPF Finances (partage) / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — IPP centimes + droits d'enregistrement/succession L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Ventilation L5 des dépenses fiscales IPP 882,827 mEUR BI2025
   (mesures, montants, bénéficiaires agrégés) — CoA Table 21.
2. Suivi ex post de la réforme des droits d'enregistrement à 3 %:
   coût net 245,4 mEUR 2025 (impact −470,7 + primo +94 + modestes
   +131,3) vs réalisations mensuelles 2025-2026.
3. Série 2019-2025 des droits de succession (874,163 mEUR BI2025)
   et impact projeté de la réforme des successions 2028-2029.
4. Réconciliation SPF Finances septembre 2024 (2.405,9 mEUR) vs
   budget régional 2.167,3 mEUR pour impôts régionaux perçus par
   l'État.
5. Calendrier et estimation 2026+ de la suppression du chèque habitat.
6. Comparaison méthodologique disponible avec les réformes flamandes
   d'enregistrement / succession (si documents SPW).

Période: 2019-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Tables 21–22 + reform narrative.
- Dual VL: registration / inheritance reforms (prior ticks).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual fiscal hole-fill -- **IPP Table21 + enregistrement/succession Table22** dual VL)
- Found: **IPP regional** (primary CoA Table21): BI2025 **EUR3.743bn** (path **+EUR229m** / **+6.52%**); brut **EUR4.523bn**; dep fiscales **EUR882.8m**; net **EUR3.640bn**. **Impots regionaux via fed** (Table22): BI2025 **EUR2.167bn** (path **-EUR233m** / **-9.71%**). Enregistrement **EUR1.273bn** (transmissions **EUR1.005bn** path **-EUR263m** / **-20.8%**); succession **EUR874m**. **Reform 3pct:** net cost **EUR245.4m** (impact **-EUR470.7m** + primo **+EUR94m** + modestes **+EUR131.3m**); cheque habitat from **2026**. SPF sep est **EUR2.406bn** vs budget **EUR2.167bn**. Companion **119quater** net economy **EUR15.9m**. Dual **VL fiscal reforms**. Strong confidence CoA; taxex L5 residual FOI.
- Wrote: entities (+2); budgets (+30); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@660 in 9 ticks; rq_116 deferred
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
        f"tick{TICK} IPP 3.74bn enreg reform path -253m dual VL; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after fiscal IPP dual; rq_116 deferred; progress@660 in 9",
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
