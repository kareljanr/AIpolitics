# -*- coding: utf-8 -*-
"""Tick 653: CAF family benefits dual Groeipakket + Type3 annex gap — rq_644."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOI_DRAFTS = ROOT.parent / "foi" / "drafts"
LOG = ROOT.parent / "loop_log.md"
NOW = "2026-08-01T05:00:00Z"
TICK = 653
RQ = "rq_644"
NEXT_RQ = "rq_645"
GAP = "gap_caf_family_benefits_l5_2025"


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
        f"tick{TICK} CAF private 1.58bn Famiwal 1.11bn dual Groeipakket; "
        f"next {NEXT_RQ}; progress@660 in 7; rq_116 deferred"
    )
    row = f"main,continuous,hole_fill,{NOW},{RQ},{TICK},no,{notes}"
    path.write_bytes((header + "\n" + row + "\n").encode("utf-8"))
    print(f"loop_state ticks={TICK}")


ent_rows = [
    "caf_private_aggregate_wal,Caisses allocations familiales privees Wallonie,Caisses d allocations familiales Type3 Wallonie,Walloon private family benefits funds aggregate dual Groeipakket,agency,aviq,fr,,,CoA Annex3 BI2025 aggregate rec 1579.939m dep 1578.737m solde +1.202m; Camille+Parentia+Infino+KidsLife; dual VL Groeipakket; tick653",
    "infino_wal,Infino Wallonie CAF,Infino Wallonie caisse allocations familiales,Infino private family benefits fund Wallonia,parastatal,aviq,fr,https://www.infino.be,,,Type3 CoA Annex3 BI2025 rec 341.544m dep 341.234m solde +0.309m; dual Groeipakket; tick653",
]

src_rows = [
    "src_ccrek_caf_family_benefits_bi2025,CoA Budget RW CAF family benefits dual Groeipakket,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Cour des comptes Belgique,2026-08-01,audit,Strong tick653: Annex3 CAF aggregate Type3 BI2025 rec 1579938748 dep 1578736919 solde +1201829; Camille 578919361/578393147/+526214; Parentia 651742290/651361404/+380886; Infino 341543694/341234297/+309397; KidsLife 7733403/7748071/-14669 (CoA perimeter functioning-class residual vs EPCO prest 360m 2026); Famiwal Type2 Table33 BI2025 rec=dep 1109819565 solde 0 (BI2024 -996k); Type3 annex non-compliance 46 of 112 orgs + 2 incomplete; 7 fusion/liquidated still on UAP list; dual VL Groeipakket class",
    "src_dual_caf_groeipakket_tick653,Dual WAL CAF stack vs VL Groeipakket family benefits,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,DOGE synthesis CoA CAF + prior Groeipakket,2026-08-01,synthesis,Strong dual: WAL Famiwal 1.110bn + private CAF aggregate 1.580bn class vs VL Groeipakket/Opgroeien path; not TE-additive; tick653",
]

bud_rows = [
    # Aggregate private CAF
    "bud_caf_private_rec_bi2025,caf_private_aggregate_wal,2025,1579938748,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,CAF privees aggregate rec BI2025 1579.939m CoA Annex3; tick653",
    "bud_caf_private_dep_bi2025,caf_private_aggregate_wal,2025,1578736919,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,CAF privees aggregate dep BI2025 1578.737m solde +1.202m; tick653",
    "bud_caf_private_solde_bi2025,caf_private_aggregate_wal,2025,1201829,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,CAF privees aggregate solde SEC BI2025 +1.202m; tick653",
    # Camille BI2025 CoA (update from 2026 EPCO)
    "bud_camille_rec_bi2025,camille_wal,2025,578919361,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Camille rec BI2025 578.919m CoA Annex3; tick653",
    "bud_camille_dep_bi2025,camille_wal,2025,578393147,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Camille dep BI2025 578.393m solde +0.526m; tick653",
    "bud_camille_solde_bi2025,camille_wal,2025,526214,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Camille solde SEC BI2025 +0.526m; tick653",
    # Parentia
    "bud_parentia_rec_bi2025,parentia_wal,2025,651742290,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Parentia rec BI2025 651.742m largest private CAF CoA; tick653",
    "bud_parentia_dep_bi2025,parentia_wal,2025,651361404,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Parentia dep BI2025 651.361m solde +0.381m; tick653",
    "bud_parentia_solde_bi2025,parentia_wal,2025,380886,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Parentia solde SEC BI2025 +0.381m; tick653",
    # Infino
    "bud_infino_rec_bi2025,infino_wal,2025,341543694,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Infino rec BI2025 341.544m CoA Annex3; tick653",
    "bud_infino_dep_bi2025,infino_wal,2025,341234297,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Infino dep BI2025 341.234m solde +0.309m; tick653",
    "bud_infino_solde_bi2025,infino_wal,2025,309397,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Infino solde SEC BI2025 +0.309m; tick653",
    # KidsLife CoA perimeter (functioning-class small)
    "bud_kidslife_rec_bi2025_coa,kidslife_wal,2025,7733403,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,KidsLife CoA Annex3 rec BI2025 7.733m (functioning-class perimeter not full prest; dual EPCO 2026 prest 360m); tick653",
    "bud_kidslife_dep_bi2025_coa,kidslife_wal,2025,7748071,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,KidsLife CoA Annex3 dep BI2025 7.748m solde -0.015m; tick653",
    "bud_kidslife_solde_bi2025_coa,kidslife_wal,2025,-14669,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,KidsLife CoA solde BI2025 -0.015m; tick653",
    # Famiwal already has BI2025 - add dual stack total
    "bud_caf_stack_private_plus_famiwal_bi2025,aviq,2025,2689758313,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Famiwal 1109.820 + private CAF 1579.939 = 2689.758m class family benefits stack BI2025 (not TE-additive double-count risk if mixed with AViQ dots); tick653",
    "bud_caf_share_parentia_pct_bi2025,parentia_wal,2025,41,,,other,src_ccrek_caf_family_benefits_bi2025,strong,Parentia ~41pct of private CAF aggregate rec (651.7/1579.9); not EUR; tick653",
    "bud_caf_share_camille_pct_bi2025,camille_wal,2025,37,,,other,src_ccrek_caf_family_benefits_bi2025,strong,Camille ~37pct of private CAF aggregate rec; not EUR; tick653",
    "bud_caf_share_infino_pct_bi2025,infino_wal,2025,22,,,other,src_ccrek_caf_family_benefits_bi2025,strong,Infino ~22pct of private CAF aggregate rec; not EUR; tick653",
    # Type3 compliance
    "bud_type3_annex_noncompliance_count,uap_perimeter_wal,2025,46,,,other,src_ccrek_caf_family_benefits_bi2025,strong,CoA: 46 of 112 Type3 orgs did not annex budgets + 2 incomplete; not EUR; tick653",
    "bud_type3_uap_list_stale_count,uap_perimeter_wal,2025,7,,,other,src_ccrek_caf_family_benefits_bi2025,strong,CoA: 7 fusion/liquidated orgs still on UAP list; not EUR; tick653",
    # Regional invest residual companion (Hoccinvest/Socaris)
    "bud_hoccinvest_rec_bi2025,wallonie_entreprendre,2025,21408,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Hoccinvest spin-off rec BI2025 0.021m; tick653",
    "bud_hoccinvest_dep_bi2025,wallonie_entreprendre,2025,159170,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Hoccinvest dep BI2025 0.159m solde -0.138m; tick653",
    "bud_socaris_rec_bi2025,wallonie_entreprendre,2025,2082339,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Socaris Hainaut rec BI2025 2.082m; tick653",
    "bud_socaris_dep_bi2025,wallonie_entreprendre,2025,647035,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Socaris dep BI2025 0.647m solde +1.435m; tick653",
    "bud_namur_innovation_rec_bi2025,wallonie_entreprendre,2025,700716,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Namur Innovation Growth rec BI2025 0.701m; tick653",
    "bud_namur_innovation_dep_bi2025,wallonie_entreprendre,2025,365002,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,Namur Innovation dep BI2025 0.365m solde +0.336m; tick653",
    "bud_imbc2020_rec_bi2025,wallonie_entreprendre,2025,750000,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,IMBC 2020 rec BI2025 0.750m; tick653",
    "bud_imbc2020_dep_bi2025,wallonie_entreprendre,2025,838800,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,IMBC 2020 dep BI2025 0.839m solde -0.089m; tick653",
    "bud_eap_dep_bi2025,wallonie_gov,2025,6692000,,,budgeted,src_ccrek_caf_family_benefits_bi2025,strong,EAP Type2 dep BI2025 6.692m path -0.455m solde +0.454m; dual FWB; tick653",
]

cmt_rows = [
    'cmt_caf_private_aggregate_bi2025,CAF privees aggregate CoA Annex3 BI2025 dual Groeipakket,caf_private_aggregate_wal,Families Wallonia private funds,CoA Annex3 Type3 CAF,2024-11-15,2025,2025,1578736919,"{""rec_m"":1579.939,""dep_m"":1578.737,""solde_m"":1.202,""parentia_m"":651.742,""camille_m"":578.919,""infino_m"":341.544,""kidslife_coa_m"":7.733,""note"":""Strong CoA; KidsLife CoA perimeter small vs EPCO prest class""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Private family benefits funds stack,Reconcile KidsLife prest FOI dual Groeipakket,src_ccrek_caf_family_benefits_bi2025,strong,Wallonie>Famille>CAF_privees,tick653',
    'cmt_caf_stack_famiwal_private_bi2025,Family benefits stack Famiwal+private CAF BI2025,aviq,All WAL family benefit recipients,CoA Table33+Annex3,2024-11-15,2025,2025,2689758313,"{""famiwal_m"":1109.820,""private_m"":1579.939,""stack_m"":2689.758,""note"":""Strong CoA; dual VL Groeipakket; do not double-count AViQ dots""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Full WAL family benefits institutional stack,Unit-cost dual FOI,src_ccrek_caf_family_benefits_bi2025,strong,Wallonie>Famille>Stack,tick653',
    'cmt_type3_annex_compliance_gap_bi2025,Type3 annex non-compliance 46 of 112 BI2025,uap_perimeter_wal,Type3 UAP ministers,Decret 15 Dec 2011 art 87 para3,2024-11-15,2025,2025,0,"{""non_annexed"":46,""incomplete"":2,""total_type3"":112,""stale_list"":7,""note"":""Strong CoA s8.1.2; opacity residual FOI""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Type3 budget annex compliance gap,Force annex all Type3 FOI,src_ccrek_caf_family_benefits_bi2025,strong,Wallonie>UAP>Type3_compliance,tick653',
    'cmt_dual_caf_groeipakket_2025,Dual WAL CAF stack vs VL Groeipakket,caf_private_aggregate_wal,Families BE dual,CoA WAL + prior Groeipakket,2024-11-15,2025,2025,0,"{""wal_famiwal_m"":1109.820,""wal_private_m"":1579.939,""wal_stack_m"":2689.758,""note"":""Not TE-additive dual family benefit stacks""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Interregional family benefits dual,Unit-cost dual FOI,src_dual_caf_groeipakket_tick653,strong,Belgium>Famille>dual_CAF_Groeipakket,tick653',
    'cmt_parentia_largest_private_caf_bi2025,Parentia largest private CAF BI2025,parentia_wal,Parentia beneficiaries,CoA Annex3,2024-11-15,2025,2025,651361404,"{""rec_m"":651.742,""dep_m"":651.361,""solde_m"":0.381,""share_private_pct"":41,""note"":""Strong CoA; dual EPCO 2026 prest 992.8m different year""}",0,active,https://www.ccrek.be/sites/default/files/Docs/2024_63_BudgetRW_2024A2025I.pdf,Largest private family fund Wallonia,Publish unit-cost FOI,src_ccrek_caf_family_benefits_bi2025,strong,Wallonie>Famille>Parentia,tick653',
]

lb_rows = [
    "lb_caf_private_1_58bn_2025,CAF privees aggregate 1.58bn BI2025 dual Groeipakket,Wallonia,ops,Wallonie>Famille>CAF_privees_1_58bn,1578736919,1578736919,Strong CoA Annex3: private CAF dep 1578.737m rec 1579.939m; dual VL,strong,src_ccrek_caf_family_benefits_bi2025,WAL families private funds,Private family benefits stack,Core social transfer not pure waste; multi-fund dual residual,3.5,9.5,4,6.30,FOI unit-cost dual Groeipakket,seed,,tick653",
    "lb_caf_stack_2_69bn_2025,Family benefits stack Famiwal+private 2.69bn BI2025,Wallonia,ops,Wallonie>Famille>Stack_2_69bn,2689758313,2689758313,Strong CoA: Famiwal 1.110 + private 1.580 = 2.690bn class; dual Groeipakket,strong,src_ccrek_caf_family_benefits_bi2025,All WAL family recipients,Full institutional family benefits,Core social; dual community residual,3.5,9.5,4,6.30,Unit-cost dual FOI,seed,,tick653",
    "lb_parentia_652m_2025,Parentia CAF 651.7m BI2025 largest private,Wallonia,ops,Wallonie>Famille>Parentia_652m,651361404,651742290,Strong CoA: Parentia dep 651.361m ~41pct private CAF,strong,src_ccrek_caf_family_benefits_bi2025,Parentia beneficiaries,Largest private family fund,Core transfer multi-fund dual residual,3.0,8.0,4,5.45,FOI unit-cost,seed,,tick653",
    "lb_camille_578m_2025,Camille CAF 578.4m BI2025,Wallonia,ops,Wallonie>Famille>Camille_578m,578393147,578919361,Strong CoA: Camille dep 578.393m ~37pct private CAF,strong,src_ccrek_caf_family_benefits_bi2025,Camille beneficiaries,Private family fund,Core transfer dual residual,3.0,8.0,4,5.45,FOI unit-cost,seed,,tick653",
    "lb_type3_annex_gap_46_of_112,Type3 annex non-compliance 46 of 112 orgs,Wallonia,ops,Wallonie>UAP>Type3_annex_gap,0,0,Strong CoA s8.1.2: 46/112 Type3 no annex + 2 incomplete + 7 stale list; opacity residual,strong,src_ccrek_caf_family_benefits_bi2025,WAL transparency,Type3 budget annex compliance,High-abs governance residual,7.5,5.0,3,6.15,Force annex FOI,seed,,tick653",
    "lb_dual_caf_groeipakket_2025,Dual WAL CAF 2.69bn vs VL Groeipakket,Belgium,ops,Belgium>Famille>dual_CAF_Groeipakket,2689758313,0,Strong dual: WAL Famiwal+private 2.69bn vs VL Groeipakket/Opgroeien; not TE-additive,strong,src_dual_caf_groeipakket_tick653,BE families,Parallel family benefit stacks,Institutional dual residual,5.0,9.0,4,6.50,Unit-cost dual FOI,seed,,tick653",
]

foi_row = (
    f"{GAP},Wallonie>Famille>CAF>L5_2025,caf_private_aggregate_wal,"
    "CAF private prest vs fonct recon KidsLife 7.7m CoA vs 360m EPCO; unit-cost Parentia/Camille/Infino/Famiwal; "
    "Type3 46 non-annex list; dual Groeipakket unit-cost,"
    "CoA CAF totals strong tick653; L5 residual dual,"
    "5,AViQ / FAMIWAL / Wallonie transparence,transparence@spw.wallonie.be,https://www.wallonie.be,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-08-01,,,,,"
    "cmt_caf_private_aggregate_bi2025|cmt_caf_stack_famiwal_private_bi2025|cmt_dual_caf_groeipakket_2025,"
    "lb_caf_private_1_58bn_2025|lb_caf_stack_2_69bn_2025|lb_dual_caf_groeipakket_2025,"
    f"{NOW},{NOW},tick653 CoA CAF dual primary; residual L5 dual human send"
)

foi_draft = f"""# FOI draft — {GAP}

**gap_id:** `{GAP}`  
**Status:** ready (not sent — human send only)  
**Priority:** 5  
**Sources:** Cour des comptes Budget RW Annex 3 CAF + Table 33 Famiwal; dual Groeipakket prior

---

## Brief

```text
[Naam verzoeker]
[Adres / e-mail]
[Datum]

Aan: AViQ / FAMIWAL / service transparence
transparence@spw.wallonie.be
https://www.wallonie.be

Betreft: Openbaarheid — Caisses d'allocations familiales L5 2024-2026

Geachte,

Op grond van de Waalse openbaarheidsregels verzoek ik om:

1. Réconciliation KidsLife: CoA Annex3 BI2025 rec/dep ~7,7 mEUR vs
   prestations EPCO 2026 ~360 mEUR — périmètre exact.
2. Ventilation prestations vs fonctionnement 2024-2025 pour Parentia
   (651,7 mEUR), Camille (578,9 mEUR), Infino (341,5 mEUR) et
   Famiwal (1.109,8 mEUR).
3. Coût unitaire par enfant / dossier et effectifs FTE par caisse.
4. Liste des 46 organismes de type 3 dont le budget BI2025 n'a pas
   été annexé (CoA §8.1.2) et statut de mise à jour.
5. Comparaison méthodologique disponible avec Groeipakket / Opgroeien
   Flandre (si documents AViQ).

Période: 2023-01-01 à 2026-12-31.
Forme: tableaux machine-lisibles (CSV/XLSX) de préférence.

Cordialement,
[Naam]
```

## Notes (internal)

- Primary CoA Budget RW 2024_63 Annex 3 + Table 33.
- Dual VL: Groeipakket / Opgroeien (prior ticks).
- Do **not** send as agent; human identity + send only.
"""

log_entry = f"""
### {NOW} -- tick {TICK}
- Unit: {RQ} (FOI-adjacent dual family benefits hole-fill -- **CAF privees + Famiwal** dual Groeipakket + Type3 annex gap)
- Found: **CAF privees aggregate** (primary CoA Annex3): BI2025 rec **EUR1.580bn** / dep **EUR1.579bn** / solde **+EUR1.2m**. **Parentia EUR651.7m** (~41%); **Camille EUR578.9m** (~37%); **Infino EUR341.5m** (~22%); **KidsLife CoA EUR7.7m** (functioning-class perimeter vs EPCO prest class **EUR360m** 2026). **Famiwal Type2** BI2025 **EUR1.110bn** balanced. Stack class **EUR2.690bn**. **Type3 annex gap:** **46/112** non-annexed + 2 incomplete + 7 stale list. Dual **Groeipakket**. Strong confidence CoA; unit-cost residual FOI.
- Wrote: entities (+2); budgets (+29); commitments (+5); leaderboard (+6); sources (+2); FOI draft {GAP}; {RQ}=done; spawn {NEXT_RQ}; loop_state ticks={TICK}
- FOI opened: {GAP} -- ready (not sent)
- Next: {NEXT_RQ}; progress@660 in 7 ticks; rq_116 deferred
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
        f"tick{TICK} CAF private 1.58bn Famiwal 1.11bn dual Groeipakket; FOI {GAP} ready",
    )
    spawn_rq(
        ROOT / "research_queue.csv",
        f"{NEXT_RQ},Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        f"Prefer public primary fills (FOI-adjacent dual/L5). Prefer before idle. "
        f"Progress milestone if ticks_completed multiple of 10.,,"
        f"{NOW},,Spawned tick{TICK} after CAF dual; rq_116 deferred; progress@660 in 7",
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
