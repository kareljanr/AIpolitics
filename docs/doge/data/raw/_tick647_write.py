# -*- coding: utf-8 -*-
"""Tick 647: UAP consolidated SEC impact dual (CoA Table9) — rq_638."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T03:30:00Z"
TICK = 647
RQ = "rq_638"
NEXT_RQ = "rq_639"
GAP = "gap_uap_sec_consol_l5_2025"


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
        f"tick{TICK} UAP SEC consol -755m type3 -207m dual VL; "
        f"next {NEXT_RQ}; progress@650 in 3; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


# --- entities ---
ent_rows = [
    "uap_perimeter_wal,Perimetre consolidation UAP Wallonie,Perimetre de consolidation des UAP wallonnes,Walloon public administrative units consolidation perimeter (ICN 146),agency,wallonie_gov,fr,https://www.inr-icn.fgov.be,,,CoA Table9 BI2025 unites institutionnelles impact -755.157m; Saca -0.905 type1 -180.556 type2 -35.455 type3 -207.352 AViQ -330.562; institutions consolidees -469.9m; SEC -2286.5m; dual VL agencies; tick647",
]

# --- sources ---
src_rows = [
    "src_ccrek_uap_sec_consol_bi2025,CoA Budget RW Table9 UAP SEC consol dual VL,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick647: unites institutionnelles BI2025 impact -755157k path -197973k vs BA2024 -557184k; Saca -905 (AWAC +95 AWAP 0 OPW -1000); type1 -180556 (CGT -2000 FWCN -165039 IWEPS -7925 CRA-W -1460 ISSeP -1861 WBI -2271); type2 -35455 (Forem -30000 IFAPME +306 AWEX -6652); type3 -207352 (WE -40171 SPAQuE -51500 Sofico +35118 aero -28391 FLW+guichets +8172 SWCS -9378 SWL +17351 OTW -139364 autres +811); AViQ -330562; parlement/mediateur/Cwape -327; institutions consolidees solde -469.9m; SEC -2286.5m; tresorerie remonte 575.6m; perimeter 146 ICN Oct2024; FWCN obj -165m vs budget -63.3m gap",
    "src_dual_uap_sec_wal_vl_tick647,Dual WAL UAP SEC consol vs VL agencies,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA Table9 + prior VL UAP,2026-08-01,synthesis,Strong dual: WAL unites -755m type3 -207m OTW -139m AViQ -331m vs VL agency stack (VAPH VDAB De Lijn VMSW class); not TE-additive; tick647",
]

# --- budgets (kEUR*1000) ---
bud_rows = [
    "bud_uap_unites_impact_bi2025,uap_perimeter_wal,2025,-755157000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Unites institutionnelles SEC impact BI2025 -755.157m path -197.973m; tick647",
    "bud_uap_unites_impact_ba2024,uap_perimeter_wal,2024,-557184000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Unites institutionnelles SEC impact BA2024 -557.184m; tick647",
    "bud_uap_saca_impact_bi2025,uap_perimeter_wal,2025,-905000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Saca total impact BI2025 -0.905m (path +34.072m vs BA -34.977m); tick647",
    "bud_uap_type1_impact_bi2025,uap_perimeter_wal,2025,-180556000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Type1 UAP impact BI2025 -180.556m path -68.734m; tick647",
    "bud_uap_type2_impact_bi2025,uap_perimeter_wal,2025,-35455000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Type2 UAP impact BI2025 -35.455m path -31.647m; tick647",
    "bud_uap_type3_impact_bi2025,uap_perimeter_wal,2025,-207352000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Type3 UAP impact BI2025 -207.352m path -132.372m; tick647",
    "bud_uap_aviq_impact_bi2025,aviq,2025,-330562000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,AViQ SEC impact BI2025 -330.562m (treasury remonte -335.3m class); tick647",
    "bud_uap_fwcn_obj_bi2025,fwcn,2025,-165039000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,FWCN gov SEC objective BI2025 -165.039m vs budget solde -63.3m recon gap; tick647",
    "bud_uap_otw_impact_bi2025,tec,2025,-139364000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,OTW Type3 SEC impact BI2025 -139.364m (invest missions vs amort subs); tick647",
    "bud_uap_spaque_impact_bi2025,spaque,2025,-51500000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Groupe SPAQuE SEC impact BI2025 -51.5m path -27.3m; tick647",
    "bud_uap_we_impact_bi2025,wallonie_entreprendre,2025,-40171000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Groupe WE SEC impact BI2025 -40.171m path +87.080m vs BA -127.251m; tick647",
    "bud_uap_sofico_impact_bi2025,sofico,2025,35118000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Sofico SEC impact BI2025 +35.118m path -8.276m; tick647",
    "bud_uap_swl_impact_bi2025,swl,2025,17351000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,SWL SEC impact BI2025 +17.351m path -38.410m; tick647",
    "bud_uap_swcs_impact_bi2025,swcs,2025,-9378000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,SWCS SEC impact BI2025 -9.378m; tick647",
    "bud_uap_flw_guichets_impact_bi2025,flw,2025,8172000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,FLW+guichets SEC impact BI2025 +8.172m; tick647",
    "bud_uap_aero_impact_bi2025,sowaer,2025,-28391000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Secteur aeroportuaire SEC impact BI2025 -28.391m path -55.877m; tick647",
    "bud_uap_forem_impact_bi2025,forem,2025,-30000000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Forem Type2 SEC impact BI2025 -30.0m (dotation cut path); tick647",
    "bud_uap_awex_impact_bi2025,awex,2025,-6652000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,AWEX Type2 SEC impact BI2025 -6.652m; tick647",
    "bud_uap_ifapme_impact_bi2025,ifapme,2025,306000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,IFAPME Type2 SEC impact BI2025 +0.306m; tick647",
    "bud_uap_instit_consol_solde_bi2025,uap_perimeter_wal,2025,-469900000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Solde institutions consolidees (7) BI2025 -469.9m path -127.6m; tick647",
    "bud_uap_fin_alternatifs_bi2025,uap_perimeter_wal,2025,74200000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Financements alternatifs + missions deleguees BI2025 +74.2m (alt 67.0 missions 7.2); tick647",
    "bud_uap_sous_util_uap_bi2025,uap_perimeter_wal,2025,129000000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Sous-utilisation credits UAP BI2025 +129.0m flat; tick647",
    "bud_uap_sec_solde_bi2025,wallonie_gov,2025,-2286500000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Solde financement SEC BI2025 -2286.5m path -3.0m vs BA -2283.5m; tick647",
    "bud_uap_tresorerie_remonte_bi2025,wallonie_gov,2025,575600000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Tresorerie remonte operation 575.6m (excess UAP 536.6 + dots 39); no SEC net impact; tick647",
    "bud_uap_perimeter_count_2024,uap_perimeter_wal,2024,146,,,other,src_ccrek_uap_sec_consol_bi2025,strong,ICN perimeter 146 institutions Oct2024 (not EUR); tick647",
    # Research dual companion hole-fill (DO18 114/118)
    "bud_do18_114_recherche_ce_bi2025,wallonie_gov,2025,247484000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,DO18 prog114 Recherche CE BI2025 247.484m path eng -8.337m; tick647",
    "bud_do18_114_recherche_cl_bi2025,wallonie_gov,2025,199655000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,DO18 prog114 Recherche CL BI2025 199.655m path liq +10.387m; dual VLAIO FWO; tick647",
    "bud_do18_114_recherche_exec_class,wallonie_gov,2024,140650000,,,outturn,src_ccrek_uap_sec_consol_bi2025,strong,Prog114 CoA exec class 140.650m; tick647",
    "bud_fonds_rdi_rec_bi2025,wallonie_gov,2025,22700000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Fonds RDI recettes BI2025 22.700m; tick647",
    "bud_fonds_rdi_dep_bi2025,wallonie_gov,2025,13594000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Fonds RDI depenses BI2025 13.594m surplus 9.106m; tick647",
    "bud_fonds_rdi_stock_liq_eoy2025,wallonie_gov,2025,171200000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,Fonds RDI solde reporte liq class eoy2025 171.2m (top4 fonds); tick647",
    "bud_do18_total_cl_bi2025,wallonie_gov,2025,3786351000,,,budgeted,src_ccrek_uap_sec_consol_bi2025,strong,DO18 Entreprises emploi recherche CL BI2025 3786.351m path -164.409m; tick647",
]

# --- commitments ---
cmt_rows = [
    'cmt_uap_sec_consol_coa_bi2025,UAP SEC consolidation CoA Table9 BI2025,uap_perimeter_wal,146 UAP ICN perimeter,Decret budget RW + CoA Table9,2024-11-15,2025,2025,0,"{""unites_m"":-755.157,""saca_m"":-0.905,""type1_m"":-180.556,""type2_m"":-35.455,""type3_m"":-207.352,""aviq_m"":-330.562,""instit_consol_m"":-469.9,""sec_solde_m"":-2286.5,""tresorerie_remonte_m"":575.6,""perimeter"":146,""note"":""Strong CoA Table9; impacts not TE additive to GG""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Consolidated UAP SEC deficit drivers,Publish full entity SEC matrix annual; dual VL,src_ccrek_uap_sec_consol_bi2025,strong,Wallonie>UAP>SEC_consol,tick647',
    'cmt_uap_type3_drivers_bi2025,Type3 UAP SEC drivers OTW SPAQuE WE BI2025,uap_perimeter_wal,OTW SPAQuE WE Sofico SWL,CoA Table9 type3,2024-11-15,2025,2025,0,"{""type3_m"":-207.352,""otw_m"":-139.364,""spaque_m"":-51.5,""we_m"":-40.171,""sofico_m"":35.118,""swl_m"":17.351,""aero_m"":-28.391,""note"":""OTW invest SEC mismatch primary driver""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Type3 SEC deficit composition,FOI invest vs amort recon OTW,src_ccrek_uap_sec_consol_bi2025,strong,Wallonie>UAP>Type3_drivers,tick647',
    'cmt_fwcn_obj_vs_budget_bi2025,FWCN SEC objective vs budget gap BI2025,fwcn,Flood indemnity claimants 2021,Fonds calamites + CoA,2021-07-01,2025,2025,165039000,"{""obj_m"":-165.039,""budget_solde_m"":-63.3,""gap_m"":101.7,""note"":""Strong CoA; gov objective overstates vs dossiers""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Flood indemnity residual path,Align objective to dossier stock FOI,src_ccrek_uap_sec_consol_bi2025,strong,Wallonie>Type1>FWCN,tick647',
    'cmt_do18_114_recherche_bi2025,DO18 prog114 Recherche dual VLAIO FWO BI2025,wallonie_gov,Research promoters universities,Budget RW DO18.114,2024-11-15,2025,2025,199655000,"{""ce_m"":247.484,""cl_m"":199.655,""path_eng_m"":-8.337,""path_liq_m"":10.387,""exec_class_m"":140.65,""fonds_rdi_dep_m"":13.594,""fonds_rdi_stock_m"":171.2,""dual_fwo_m"":448,""dual_fnrs_m"":254,""note"":""Applied research dual not additive to FWO/FNRS fundamental""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Applied research promotion Wallonia,Open L5 awards; dual VLAIO,src_ccrek_uap_sec_consol_bi2025,strong,Wallonie>DO18>Recherche_114,tick647',
    'cmt_dual_uap_sec_wal_vl_2025,Dual WAL UAP SEC consol vs VL agency stack,uap_perimeter_wal,Regional parastatals dual,CoA WAL Table9 + prior VL,2024-11-15,2025,2025,0,"{""wal_unites_m"":-755.157,""wal_type3_m"":-207.352,""wal_aviq_m"":-330.562,""wal_sec_m"":-2286.5,""note"":""Not TE-additive dual institutional stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional UAP SEC dual map,Cross-region transparency FOI,src_dual_uap_sec_wal_vl_tick647,strong,Belgium>UAP>dual_SEC,tick647',
]

# --- leaderboard ---
lb_rows = [
    "lb_uap_unites_impact_755m_2025,UAP unites institutionnelles SEC -755m BI2025,Wallonia,ops,Wallonie>UAP>unites_impact_755m,755157000,755157000,Strong CoA Table9: unites -755.157m path -198m; AViQ -331 type1 -181 type3 -207,strong,src_ccrek_uap_sec_consol_bi2025,WAL taxpayers UAP users,Consolidated UAP SEC deficit,Mega dual opacity residual,7.0,8.5,4,7.15,Publish full entity SEC matrix FOI,seed,,tick647",
    "lb_uap_type3_207m_2025,Type3 UAP SEC impact -207m BI2025,Wallonia,ops,Wallonie>UAP>type3_207m,207352000,207352000,Strong CoA: type3 -207.352m OTW -139 SPAQuE -51.5 WE -40 Sofico +35,strong,src_ccrek_uap_sec_consol_bi2025,WAL mobility env enterprise,Type3 deficit drivers,OTW invest SEC mismatch primary,6.5,8.0,4,6.70,FOI OTW invest vs amort recon,seed,,tick647",
    "lb_otw_sec_impact_139m_2025,OTW SEC impact -139.4m BI2025,Wallonia,ops,Wallonie>Mobilite>OTW>sec_impact_139m,139364000,139364000,Strong CoA: OTW -139.364m invest missions full-year SEC vs amort-only subs,strong,src_ccrek_uap_sec_consol_bi2025,OTW passengers taxpayers,PSO invest SEC accounting,Not pure waste; accounting dual residual,5.5,7.5,4,6.10,Publish invest liquidations FOI,seed,,tick647",
    "lb_fwcn_obj_gap_165m_2025,FWCN SEC objective -165m vs budget -63m,Wallonia,ops,Wallonie>Type1>FWCN>obj_gap,165039000,165039000,Strong CoA: gov objective -165.039m vs budget solde -63.3m gap ~102m; flood residual,strong,src_ccrek_uap_sec_consol_bi2025,Flood victims 2021,Disaster indemnity path,Objective overstates dossiers CoA,6.5,7.5,3,6.50,Align objective to dossier stock FOI,seed,,tick647",
    "lb_do18_114_recherche_200m_2025,DO18 Recherche CL 199.7m dual VLAIO FWO,Wallonia,ops,Wallonie>DO18>Recherche_114_200m,199655000,199655000,Strong CoA: prog114 CL 199.655m CE 247.484m + fonds RDI stock 171.2m; dual FWO 448 FNRS 254,strong,src_ccrek_uap_sec_consol_bi2025,Researchers innovators,Applied research promotion,Core applied stack not pure waste; L5 residual,4.5,7.5,4,5.75,FOI L5 awards dual VLAIO,seed,,tick647",
    "lb_dual_uap_sec_wal_vl_2025,Dual WAL UAP -755m vs VL agency stack,Belgium,ops,Belgium>UAP>dual_SEC_consol,755157000,0,Strong dual: WAL unites -755m type3 -207 AViQ -331 vs VL VAPH VDAB De Lijn VMSW class; not TE-additive,strong,src_dual_uap_sec_wal_vl_tick647,BE regional taxpayers,Parallel UAP SEC stacks,Institutional dual opacity residual,6.5,8.0,4,6.70,Cross-region SEC matrix FOI,seed,,tick647",
]

# --- FOI ---
foi_row = (
    f"{GAP},Wallonie>UAP>SEC_consol>L5_2025,uap_perimeter_wal,"
    "Full entity SEC matrix 146 ICN for BI2025/exec2024; FWCN obj -165 vs budget -63 recon; "
    "OTW invest vs amort SEC; type3 annex non-communique list; treasury remonte 575.6 entity list; "
    "prog114 L5 awards dual VLAIO,"
    "CoA Table9 totals strong tick647; L5 residual dual UAP,"
    "5,SPW Budget / Wallonie transparence / ICN,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_uap_sec_consol_coa_bi2025|cmt_uap_type3_drivers_bi2025|cmt_dual_uap_sec_wal_vl_2025,"
    "lb_uap_unites_impact_755m_2025|lb_uap_type3_207m_2025|lb_dual_uap_sec_wal_vl_2025,"
    f"{NOW},{NOW},tick647 CoA UAP SEC consol primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW Table 9 UAP SEC; dual VL agency prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: SPW Budget / Wallonie Finances Expertise / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — UAP solde SEC consolidé L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Matrice complète des objectifs / soldes SEC pour les 146 institutions
   du périmètre ICN (liste octobre 2024) pour BA2024, BI2025 et
   exécution 2024 si disponible (CoA Table 9: impact unités
   -755,157 mEUR BI2025).
2. Réconciliation FWCN: objectif SEC gouvernement -165,039 mEUR vs
   solde du projet de budget -63,3 mEUR — stock de dossiers inondations
   juillet 2021 et calendrier de paiement 2025-2027.
3. OTW: ventilation L5 des investissements missions déléguées
   expliquant l'impact SEC -139,364 mEUR (subventions amortissement vs
   invest full-year SEC).
4. Liste des organismes de type 3 dont le budget BI2025 n'a pas été
   annexé / « non communiqué » (CoA Annex 3) avec montants si connus.
5. Détail de l'opération de trésorerie 575,6 mEUR (excédents 536,6 +
   dots 39): liste des UAP concernées et montants.
6. Programme 18.114 Recherche: top 50 bénéficiaires / projets
   2023-2025 (CE/CL) et lien avec le fonds RDI (stock liq class
   171,2 mEUR eoy2025).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Table 9 + Annex 3 + DO18.114.
- Dual VL: VAPH/VDAB/De Lijn/VMSW/FWO agency stack (prior ticks).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual UAP hole-fill -- **UAP SEC consol Table9** dual VL agencies + **DO18.114 Recherche**)
- Found: **Unites institutionnelles** (primary CoA Table9): BI2025 impact **-EUR755.2m** (path **-EUR198.0m** vs BA **-EUR557.2m**). **Saca -EUR0.9m**; **Type1 -EUR180.6m** (FWCN obj **-EUR165.0m** vs budget **-EUR63.3m**); **Type2 -EUR35.5m** (Forem **-EUR30m**); **Type3 -EUR207.4m** (OTW **-EUR139.4m** / SPAQuE **-EUR51.5m** / WE **-EUR40.2m** / Sofico **+EUR35.1m** / aero **-EUR28.4m**). **AViQ -EUR330.6m**. Institutions consolidees **-EUR469.9m**. SEC solde **-EUR2.287bn**. Tresorerie remonte **EUR575.6m**. Perimeter **146** ICN. Companion **prog114 Recherche** CL **EUR199.7m** + fonds RDI stock **EUR171.2m** dual FWO/FNRS. Strong confidence CoA; L5 residual FOI.
- Wrote: entities (+1); budgets (+32); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@650 in 3 ticks; rq_116 deferred
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
        f"tick{TICK} UAP SEC consol -755m type3 -207m dual; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after UAP SEC dual; rq_116 deferred; progress@650 in 3",
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
