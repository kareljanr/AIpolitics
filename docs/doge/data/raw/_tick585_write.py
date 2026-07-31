# -*- coding: utf-8 -*-
"""Tick 585: Intradel Liege waste dual HYGEA / COPIDEC — rq_576."""
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data
DATA = ROOT
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-07-31T12:00:00Z"
TICK = 585
RQ = "rq_576"
NEXT_RQ = "rq_577"


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1", errors="replace")


def append_rows(path: Path, rows: list[str], id_col_prefix: str | None = None) -> int:
    text = read_text(path)
    existing = text
    added = 0
    for row in rows:
        key = row.split(",", 1)[0]
        if key and key in existing:
            # skip if id already present as start of a line
            if any(L.startswith(key + ",") or L.startswith("\ufeff" + key + ",") for L in existing.splitlines()):
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


# --- entities ---
ent_rows = [
    "intradel,INTRADEL,INTRADEL,Liege province household waste intercommunale SC,intercommunale,wallonie_gov,fr,https://www.intradel.be,,,Waste dual AIDE water; CA 125.1m ventes 155.8m loss 12.7m assets 187.4m equity 35.5m dettes 114.7m staff 314 ETP; 72 communes 1.05m hab; 49 recyparcs UVE Herstal CET Hallembaye; tick585",
    "uvelia,UVELIA SA,UVELIA,Intradel 70pct UVE operator Herstal,subsidiary,intradel,fr,,,Intradel participation 70pct 350k capital; LT claim 1.43m; tick585",
]

# --- sources ---
src_rows = [
    "src_intradel_rg_2025,INTRADEL Rapport activites declaration environnementale comptes 2025,https://www.intradel.be/files/library/AG-2026/2026.06.25-1.1-Rapport-de-gestion-Exercice-2025.pdf,INTRADEL AG 2026,2026-07-31,official_annual_report,Strong tick585: CA 125.062m ventes 155.829m op loss 10.589m net loss 12.682m; associates intervention BEP+Idelux 12.744m; assets 187.406m equity 35.538m dettes 114.687m LT 40.777m ST 55.705m provisions 37.182m personnel 23.123m staff 314.2 ETP; pop 1.049m 72 communes; cout verite 68.05 EUR/hab; UVE 348349 t elec 82.58 EUR/MWh; invest 7.926m; raw intradel_rapport_gestion_2025.pdf",
    "src_dual_waste_intradel_hygea_tick585,Dual WAL waste Intradel Liege vs HYGEA Hainaut 2025,docs/doge/data/raw/intradel_rapport_gestion_2025.pdf,DOGE synthesis Intradel RG2025 + HYGEA Mons,2026-07-31,synthesis,Strong dual: Intradel CA 125.1m assets 187.4m staff 314 / 1.05m hab vs HYGEA Mons package 7.76m; COPIDEC 7 public waste operators WAL; tick585",
]

# --- budgets ---
bud_rows = [
    "bud_intradel_ca_2025,intradel,2025,125062424,,,outturn,src_intradel_rg_2025,strong,INTRADEL chiffre d affaires 125.062m 2025 (vs 129.659m 2024); tick585",
    "bud_intradel_ventes_2025,intradel,2025,155829155,,,outturn,src_intradel_rg_2025,strong,INTRADEL ventes et prestations 155.829m 2025; tick585",
    "bud_intradel_other_op_prod_2025,intradel,2025,24902297,,,outturn,src_intradel_rg_2025,strong,INTRADEL autres produits exploitation 24.902m 2025; tick585",
    "bud_intradel_nonrec_prod_2025,intradel,2025,5864434,,,outturn,src_intradel_rg_2025,strong,INTRADEL produits non recurrents 5.864m (Inova litige 4.694m + UVELIA 0.925m); tick585",
    "bud_intradel_costs_2025,intradel,2025,166418071,,,outturn,src_intradel_rg_2025,strong,INTRADEL cout ventes prestations 166.418m 2025; tick585",
    "bud_intradel_services_2025,intradel,2025,111900596,,,outturn,src_intradel_rg_2025,strong,INTRADEL services biens divers 111.901m 2025; tick585",
    "bud_intradel_personnel_2025,intradel,2025,23123374,,,outturn,src_intradel_rg_2025,strong,INTRADEL remunerations charges pensions 23.123m 2025; tick585",
    "bud_intradel_amort_2025,intradel,2025,16044529,,,outturn,src_intradel_rg_2025,strong,INTRADEL amortissements 16.045m 2025; tick585",
    "bud_intradel_other_charges_2025,intradel,2025,10708925,,,outturn,src_intradel_rg_2025,strong,INTRADEL autres charges exploitation 10.709m 2025; tick585",
    "bud_intradel_op_result_2025,intradel,2025,-10588916,,,outturn,src_intradel_rg_2025,strong,INTRADEL benefice exploitation -10.589m 2025 (loss); tick585",
    "bud_intradel_fin_charges_2025,intradel,2025,1876640,,,outturn,src_intradel_rg_2025,strong,INTRADEL charges financieres 1.877m 2025; tick585",
    "bud_intradel_fin_prod_2025,intradel,2025,501533,,,outturn,src_intradel_rg_2025,strong,INTRADEL produits financiers 0.502m 2025; tick585",
    "bud_intradel_net_result_2025,intradel,2025,-12682319,,,outturn,src_intradel_rg_2025,strong,INTRADEL perte exercice -12.682m 2025 (vs -15.191m 2024); tick585",
    "bud_intradel_assoc_loss_cover_2025,intradel,2025,12743893,,,outturn,src_intradel_rg_2025,strong,INTRADEL intervention associes BEP+Idelux dans perte societe interne 12.744m 2025; tick585",
    "bud_intradel_assets_2025,intradel,2025,187406229,,,outturn,src_intradel_rg_2025,strong,INTRADEL total bilan 187.406m 2025 (vs 193.790m 2024); tick585",
    "bud_intradel_fixed_assets_2025,intradel,2025,108772353,,,outturn,src_intradel_rg_2025,strong,INTRADEL actifs immobilises 108.772m 2025; tick585",
    "bud_intradel_tangible_2025,intradel,2025,98800101,,,outturn,src_intradel_rg_2025,strong,INTRADEL immobilisations corporelles 98.800m 2025; tick585",
    "bud_intradel_fin_assets_2025,intradel,2025,7514891,,,outturn,src_intradel_rg_2025,strong,INTRADEL immobilisations financieres 7.515m (UVELIA SITEL etc); tick585",
    "bud_intradel_current_assets_2025,intradel,2025,78633876,,,outturn,src_intradel_rg_2025,strong,INTRADEL actifs circulants 78.634m 2025; tick585",
    "bud_intradel_cash_2025,intradel,2025,21133225,,,outturn,src_intradel_rg_2025,strong,INTRADEL valeurs disponibles 21.133m 2025; tick585",
    "bud_intradel_receivables_2025,intradel,2025,43893293,,,outturn,src_intradel_rg_2025,strong,INTRADEL creances a un an 43.893m 2025; tick585",
    "bud_intradel_equity_2025,intradel,2025,35537642,,,outturn,src_intradel_rg_2025,strong,INTRADEL capitaux propres 35.538m 2025; tick585",
    "bud_intradel_provisions_2025,intradel,2025,37181699,,,outturn,src_intradel_rg_2025,strong,INTRADEL provisions risques charges 37.182m 2025 (CET rehab UVE UBDO moratoire); tick585",
    "bud_intradel_debt_total_2025,intradel,2025,114686888,,,outturn,src_intradel_rg_2025,strong,INTRADEL dettes total 114.687m 2025; tick585",
    "bud_intradel_debt_lt_2025,intradel,2025,40777203,,,outturn,src_intradel_rg_2025,strong,INTRADEL dettes plus un an 40.777m 2025 (-21pct YoY); tick585",
    "bud_intradel_debt_st_2025,intradel,2025,55704780,,,outturn,src_intradel_rg_2025,strong,INTRADEL dettes un an au plus 55.705m 2025 (incl revamp credit 4.09m CBC); tick585",
    "bud_intradel_invest_2025,intradel,2025,7926315,,,outturn,src_intradel_rg_2025,strong,INTRADEL investissements hors fin 7.926m 2025 (UVE revamp 3.278m); tick585",
    "bud_intradel_uve_t_2025,intradel,2025,348349,,,outturn,src_intradel_rg_2025,strong,COUNT UVE Herstal tonnes traitees 348349 (vs 352624 2024); tick585",
    "bud_intradel_cet_t_2025,intradel,2025,130129,,,outturn,src_intradel_rg_2025,strong,COUNT CET Hallembaye tonnes enfouies 130129 (+4.9pct); tick585",
    "bud_intradel_green_t_2025,intradel,2025,94302,,,outturn,src_intradel_rg_2025,strong,COUNT dechets verts plateformes 94302 t 2025; tick585",
    "bud_intradel_elec_mwh_2025,intradel,2025,202300,,,outturn,src_intradel_rg_2025,strong,COUNT electricite mise reseau UVE+UBDO+CET 202300 MWh 2025; tick585",
    "bud_intradel_elec_price_eur_mwh_2025,intradel,2025,8258,,,outturn,src_intradel_rg_2025,strong,COUNT elec sale price 82.58 EUR/MWh x100 (vs 170.50 2024); tick585",
    "bud_intradel_cout_verite_eur_hab_2025,intradel,2025,6805,,,outturn,src_intradel_rg_2025,strong,COUNT cout verite hors options 68.05 EUR/hab.an x100 (vs 65.12 2024; 70.90 excl non-rec); tick585",
    "bud_intradel_staff_etp_2025,intradel,2025,3142,,,outturn,src_intradel_rg_2025,strong,COUNT collaborateurs ETP 314.2 x10; tick585",
    "bud_intradel_pop_2025,intradel,2025,1049217,,,outturn,src_intradel_rg_2025,strong,COUNT population desservie 72 communes 1049217 hab; tick585",
    "bud_intradel_waste_kg_hab_2025,intradel,2025,478,,,outturn,src_intradel_rg_2025,strong,COUNT dechets menagers 478 kg/hab 2025; residual 112 kg/hab; tick585",
    "bud_intradel_ubdo_subsidy_prov_2025,intradel,2025,1863845,,,outturn,src_intradel_rg_2025,strong,Provision moratoire subsides UBDO infrastructure 1.864m 2025; tick585",
    "bud_intradel_mtm_hedge_2025,intradel,2025,-450046,,,outturn,src_intradel_rg_2025,strong,MTM couverture taux COLLAR/IRS ING -0.450m 2025; tick585",
    "bud_intradel_gross_invest_cumul,intradel,2025,523739452,,,outturn,src_intradel_rg_2025,strong,Valeur brute investissements cumul depuis creation 523.739m; tick585",
]

# --- commitments ---
cmt_rows = [
    'cmt_intradel_rg_2025,INTRADEL Liege waste dual COPIDEC 2025,intradel,72 communes 1.05m inhabitants Liege province,Code democratie locale intercommunale SC dechets menagers,2025-01-01,2025,2031,125062424,"{""2025_ca"":125062424,""2025_ventes"":155829155,""2025_op"":-10588916,""2025_net"":-12682319,""2025_assoc_cover"":12743893,""2025_assets"":187406229,""2025_equity"":35537642,""2025_dettes"":114686888,""2025_lt"":40777203,""2025_provisions"":37181699,""personnel"":23123374,""staff_etp"":314.2,""pop"":1049217,""communes"":72,""cout_verite_eur_hab"":68.05,""uve_t"":348349,""note"":""Waste dual HYGEA; loss covered by BEP+Idelux associates; electricity price shock""}",0,active,https://www.intradel.be,Household waste collection treatment valorisation Liege province,Publish commune cotisation matrix dual unit-cost HYGEA IPALLE IDELUX FOI residual,src_intradel_rg_2025,strong,Wallonie>Dechets>INTRADEL,tick585 RG2025 primary new entity',
    'cmt_dual_waste_intradel_hygea_2025,Dual WAL waste Intradel Liege + HYGEA Hainaut 2025,gg_belgium,Walloon waste users two provinces,Intradel RG2025 + HYGEA Mons cout-verite,2025-01-01,2025,2025,0,"{""intradel_ca_m"":125.1,""intradel_assets_m"":187.4,""intradel_staff"":314,""intradel_pop_m"":1.05,""hygea_mons_package_m"":7.76,""copidec_operators"":7,""note"":""Dual public waste stack; full HYGEA group CA residual FOI""}",0,active,,Multi-entity WAL waste dual COPIDEC,Unit-cost waste matrix commune FOI residual,src_dual_waste_intradel_hygea_tick585,strong,BE>dual>waste_Intradel_HYGEA,tick585',
]

# --- leaderboard ---
lb_rows = [
    "lb_intradel_ca_125m_2025,INTRADEL Liege CA 125.1m loss 12.7m 2025,Wallonia,ops,Wallonie>Dechets>INTRADEL>ca_125m,125062424,187406229,Strong RG2025: ventes 155.8m op -10.6m net -12.7m assets 187.4m equity 35.5m dettes 114.7m; dual HYGEA,strong,src_intradel_rg_2025,1.05m hab 72 communes,Household waste full-cycle public utility,Structural loss; elec price shock -11.4m; associates cover 12.7m,4,8.0,5,6.05,Publish commune cotisations dual unit-cost FOI,seed,,tick585",
    "lb_intradel_debt_115m_2025,INTRADEL debt 114.7m provisions 37.2m 2025,Wallonia,ops,Wallonie>Dechets>INTRADEL>debt_115m,0,114686888,Strong: dettes 114.7m (LT 40.8 ST 55.7) + provisions 37.2m (CET rehab UVE); equity only 35.5m,strong,src_intradel_rg_2025,1.05m hab,Finance UVE CET long tools,High leverage vs equity; revamp UVE path,5,7.5,5,5.95,Debt amort schedule + CET rehab FOI,seed,,tick585",
    "lb_intradel_personnel_23m_2025,INTRADEL personnel 23.1m staff 314 ETP 2025,Wallonia,ops,Wallonie>Dechets>INTRADEL>personnel_23m,23123374,23123374,Strong: rem 23.1m of CA 125m; ETP 314.2; dual HYGEA staff residual,strong,src_intradel_rg_2025,INTRADEL staff,Operate 49 recyparcs UVE CET collectes,Core ops cost,3,6.5,4,4.85,Benchmark ETP/1000hab dual waste,seed,,tick585",
    "lb_intradel_cout_verite_68_2025,INTRADEL cout verite 68.05 EUR/hab 2025,Wallonia,ops,Wallonie>Dechets>INTRADEL>cout_verite,0,0,Strong: 68.05 EUR/hab.an (70.90 excl non-rec Inova); +2.93 YoY; dual Mons HYGEA package path,strong,src_intradel_rg_2025,1.05m hab,Truth-cost waste service per inhabitant,Citizen bill driver via commune cotisations,4,6.0,4,4.70,Publish commune-level cout verite matrix,seed,,tick585",
    "lb_intradel_uve_348kt_2025,INTRADEL UVE Herstal 348kt elec price crash 2025,Wallonia,ops,Wallonie>Dechets>INTRADEL>uve,0,0,Strong: 348349 t; elec 82.58 EUR/MWh vs 170.50 2024 (-11.4m CA); cost 91.33 EUR/t; ETS risk up to 12m/yr,strong,src_intradel_rg_2025,Liege waste residual stream,Energy recovery residual household waste,Price exposure dominates results; revamp decision Sep 2025,5,7.0,6,5.80,Hedge policy + ETS scenario FOI,seed,,tick585",
    "lb_dual_waste_intradel_hygea_2025,Dual WAL waste Intradel 125m + HYGEA Mons 7.8m,multi,ops,BE>dual>waste_Intradel_HYGEA_2025,125062424,7760388,Strong dual: Intradel province-scale 125m/187m/314 staff vs HYGEA Mons city package 7.76m; COPIDEC 7 ops,strong,src_dual_waste_intradel_hygea_tick585,Walloon waste users,Map public waste operator stack,HYGEA full group CA still FOI; dual unit-cost incomplete,4,7.5,5,5.70,FOI HYGEA group CA + Intradel commune matrix,seed,,tick585",
]

# --- foi_queue ---
foi_rows = [
    "gap_intradel_commune_l5_2025,Wallonie>INTRADEL>commune_cotisation_L5_2025,intradel,Commune-by-commune cotisation matrix 2024-26 recon to CA 125.1m; sector P&L tables (recyparc collectes UVE CET organiques); dual unit-cost vs HYGEA IPALLE IDELUX BEP; consolidated UVELIA SITEL BNB; top20 works invest; UVE revamp multi-year budget; associates loss-cover BEP+Idelux contract,RG2025 aggregates strong tick585; commune L5 and dual waste residual,5,INTRADEL / COPIDEC / Wallonie transparence,,https://www.intradel.be,docs/doge/foi/drafts/gap_intradel_commune_l5_2025.md,ready,2026-07-31,,,,cmt_intradel_rg_2025|cmt_dual_waste_intradel_hygea_2025,lb_intradel_ca_125m_2025|lb_dual_waste_intradel_hygea_2025|lb_intradel_cout_verite_68_2025,2026-07-31T12:00:00Z,2026-07-31T12:00:00Z,tick585 Intradel RG2025 primary; residual commune matrix human send",
]

# --- research_queue updates ---
def update_research_queue():
    path = DATA / "research_queue.csv"
    text = read_text(path)
    lines = text.splitlines()
    out = []
    found = False
    for L in lines:
        if L.startswith("rq_576,"):
            # mark done
            parts = L.split(",")
            # status is field index 4 (0-based): rq_id,title,sprint,prio,status,...
            # safer: replace ,open, with ,done, once in status position
            # original: rq_576,Continuous...,continuous,5,open,L5,...
            L2 = L.replace(",open,", ",done,", 1)
            # set completed_at and notes - append-ish
            # columns: task_id,title,sprint,priority,status,target_level,entity_id,notes,depends_on,created_at,completed_at,result_notes
            cols = L2.split(",")
            # This is fragile for CSV with commas in fields - rq_576 line has no quoted commas in critical spots
            # From read: rq_576,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,Prefer public...,,2026-07-31T11:45:00Z,,Spawned...
            # Actually the Prefer field has commas! Need careful parse.
            # Simpler: rebuild known line
            L = (
                f"rq_576,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
                f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
                f"2026-07-31T11:45:00Z,{NOW},"
                f"tick585: Intradel Liege CA 125m dual HYGEA waste + COPIDEC; spawn {NEXT_RQ}; rq_116 deferred"
            )
            found = True
        out.append(L)
    if not found:
        print("WARN rq_576 not found")
    # append next rq if missing
    next_line = (
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,"
        f"Spawned tick585 after Intradel dual waste; rq_116 deferred; progress@590 in 5 ticks"
    )
    if not any(L.startswith(f"{NEXT_RQ},") for L in out):
        out.append(next_line)
        print(f"ADD {NEXT_RQ}")
    else:
        print(f"SKIP exists {NEXT_RQ}")
    path.write_bytes(("\n".join(out) + "\n").encode("utf-8"))
    print("research_queue updated")


def update_loop_state():
    path = DATA / "loop_state.csv"
    header = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    row = (
        f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,"
        f"tick585 Intradel Liege CA 125m dual HYGEA waste COPIDEC; next {NEXT_RQ}; progress@590 in 5; rq_116 deferred\n"
    )
    path.write_bytes((header + row).encode("utf-8"))
    print("loop_state updated")


def write_foi_draft():
    FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
    path = FOI_DRAFTS / "gap_intradel_commune_l5_2025.md"
    path.write_text(
        """# FOI draft — gap_intradel_commune_l5_2025

**gap_id:** `gap_intradel_commune_l5_2025`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Source:** INTRADEL Rapport d'activités & comptes 2025

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: INTRADEL / COPIDEC / Wallonie transparence
https://www.intradel.be
Centre de documentation / Assemblées générales

Betreft: Demande de publicité — INTRADEL cotisations communales L5 2025 + dual déchets

Geachte,

Op grond van het Waalse openbaarheidsregime verzoek ik om:

1. Matrice des cotisations communales 2024–2026 (72 communes) reconduisant
   le chiffre d'affaires 125,1 m€ et le coût vérité 68,05 €/hab.an.
2. Tableaux de résultats sectoriels complets (recyparcs, collectes DMR/organiques,
   obligations de reprise, UVE, CET, déchets verts, biométhanisation, frais de structure)
   avec montants à financer par commune / obligataire.
3. Contrat d'intervention des associés (BEP + Idelux) dans la perte de la société
   interne (12,744 m€ en 2025) et multi-annualité.
4. Budget multi-annuel revamping UVE Herstal (décision CA 4/9/2025) + échéancier dette
   LT 40,8 m€ et couverture taux (MTM −0,45 m€).
5. Comptes consolidés UVELIA / SITEL / SIDECO 2025 (liens BNB) et part des communes.
6. Unit-costs 2024–2025 (EUR/t UVE, EUR/hab collectes, EUR/t enfouissement) dual vs
   HYGEA, IPALLE, IDELUX, BEP (COPIDEC).
7. Top-20 marchés 2025 (adjudicataire, montant, objet) et liste complète des
   adjudicataires annexée au rapport.

Public déjà connu (RG 2025) : CA 125,1 m€ ; perte 12,7 m€ ; bilan 187,4 m€ ;
CP 35,5 m€ ; 314 ETP ; 1,05 m hab ; 49 recyparcs ; UVE 348 kt ; coût vérité 68,05 €/hab.
Cette demande porte sur la matrice communale, le dual COPIDEC et le revamping UVE.

Période : 2023–2031.
Réf. interne : gap_intradel_commune_l5_2025

Met vriendelijke groet / Cordialement,
[Naam]
```

*(Concept — agent verzendt niet tenzij expliciet bevolen.)*
""",
        encoding="utf-8",
    )
    print(f"FOI draft {path}")


def append_log():
    entry = f"""
### {NOW} — tick {TICK}
- Unit: {RQ} (FOI-adjacent dual waste hole-fill — INTRADEL Liège)
- Found: **INTRADEL** RG/comptes 2025 (primary PDF AG 2026, 116 pp). **CA €125.062m** (ventes €155.829m); **op loss €10.589m**; **net loss €12.682m** covered by **BEP+Idelux associate intervention €12.744m** (post-cover +€0.062m). **Assets €187.406m**; **equity €35.538m**; **dettes €114.687m** (LT €40.777m ST €55.705m); **provisions €37.182m**; personnel **€23.123m** / **314.2 ETP**; **72 communes / 1.049m hab**; **coût vérité €68.05/hab** (70.90 excl non-rec); UVE **348 kt** elec **€82.58/MWh** (−11.4m CA YoY); invest **€7.926m**; dual waste vs **HYGEA Mons €7.76m**; COPIDEC 7 public ops. Strong confidence.
- Wrote: entities (+intradel +uvelia); budgets (+38); commitments (+2); leaderboard (+6); sources (+2); raw PDF; FOI draft gap_intradel_commune_l5_2025; rq_576=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: gap_intradel_commune_l5_2025 → ready (not sent)
- Next: {NEXT_RQ}; progress@590 in 5 ticks; rq_116 deferred
"""
    log = read_text(LOG)
    if f"tick {TICK}" in log and f"Unit: {RQ}" in log:
        print("LOG already has tick entry — skip append")
        return
    if not log.endswith("\n"):
        log += "\n"
    log += entry
    LOG.write_bytes(log.encode("utf-8"))
    print("loop_log appended")


def main():
    print("=== tick 585 write ===")
    append_rows(DATA / "entities.csv", ent_rows)
    append_rows(DATA / "sources.csv", src_rows)
    append_rows(DATA / "budgets.csv", bud_rows)
    append_rows(DATA / "commitments.csv", cmt_rows)
    append_rows(DATA / "leaderboard.csv", lb_rows)
    append_rows(DATA / "foi_queue.csv", foi_rows)
    write_foi_draft()
    update_research_queue()
    update_loop_state()
    append_log()
    print("=== done ===")


if __name__ == "__main__":
    main()
