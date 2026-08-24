# tick 2267 — leftover dual APRE YE2025 Medium (bruto 2.02m / empty omzet / pnl PROFIT FLIP / FTE 95.7)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # .../data/raw/tick2267 -> repo root
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2267
UTC = "2026-08-27T08:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_apre_forest"
KBO = "0407.598.354"
KBO_BARE = "0407598354"
SRC_EN = "src_apre_jr2025_cw_en"
GAP = "gap_apre_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_eta_matrix_l5"
COMM = "comm_apre_jr2025_statutory_eta_empty_omzet_pnl_profit_flip"
LB = "lb_apre_bruto_2_02m_empty_omzet_pnl_profit_flip_jr2025"
RQ = "rq_2267"
RQ_NEXT = "rq_2268"

BRUTO = 2015380
BRUTO24 = 2094904
PNL = 112223
PNL24 = -32660
EQUITY = 716631
EQUITY24 = 679650
FTE = 95.7
FTE24 = 99.9
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_FLIP_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
PI = "5.60"


def append_csv(path: Path, rows: list[dict]):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    id_key = fieldnames[0]
    ids = {r[id_key] for r in existing}
    new = [r for r in rows if r[id_key] not in ids]
    if not new:
        print(f"skip {path.name}")
        return
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        for r in new:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(f"appended {len(new)} -> {path.name}")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            found = True
            r["status"] = "done"
            r["title"] = (
                "leftover dual — APRE YE2025 Medium "
                f"(bruto DROP 2.02m / empty omzet / pnl PROFIT FLIP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; APRE ASBL Forest/Vorst {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto DROP {BRUTO} ({BRUTO_PCT}%); "
                f"pnl PROFIT FLIP {PNL} (+{PNL_FLIP_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE} ({FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.999; neerlegging 29.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; after Renaitre@2266; "
                f"next EVERY-10 2270"
            )
            r["instructions"] = (
                "leftover dual APRE YE2025 FREE Brussels ETA epilepsy after Renaitre; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after APRE — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after APRE YE2025 Medium "
                    f"(bruto DROP 2.02m / empty omzet / pnl PROFIT FLIP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk. "
                    "Skip APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria/"
                    "Les Erables/Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/"
                    "Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
                    "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/"
                    "Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/"
                    "Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/"
                    "Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/APN YE2024; Citeco YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2270."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} APRE; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024; next every-10 2270"
                ),
            }
        )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue updated")


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    rows[0].update(
        {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover dual APRE {KBO} Medium (bruto DROP {BRUTO} {BRUTO_PCT}%; "
                f"empty omzet; pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; "
                f"1 VE Forest/Vorst Brussels ETA epilepsy/PHARE); after Renaitre@2266; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre/APN YE2024; "
                f"next {RQ_NEXT}; next EVERY-10 2270; continuous hole_fill"
            ),
        }
    )
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state updated")


def write_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — APRE (NBB PDF / empty omzet / pnl PROFIT FLIP / Brussels ETA epilepsy matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** A.P.R.E. ASBL — KBO **{KBO}** (Actief; Neerstalse Steenweg 178, 1190 Vorst; **1 VE**; FTE {FTE} CW; NACE **88.999**; Brussels ETA epilepsy / PHARE)  
**recipient:** contact@apreservices.be · Chaussée de Neerstalle 178, 1190 Forest (+32 2 333 00 90)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://apreservices.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief VZW A.P.R.E.; **1 VE**; zetel Neerstalse Steenweg 178, 1190 Vorst; BTW NACE **88.999**; begindatum 24.01.1967.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); filed **29.07.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024 (0201.712.587); REW YE2024; Heropbeuring CW opaque; Relais Haute Sambre/APN YE2024. After Renaitre@2266.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: A.P.R.E. ASBL
via contact@apreservices.be
Chaussée de Neerstalle 178, 1190 Forest
Objet: Publicité des comptes annuels 2025 APRE (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région de Bruxelles-Capitale / PHARE / COCOF), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Chiffre d'affaires YE2025 (non publié sur Companyweb) et explication du retour au bénéfice
   EUR{PNL} vs perte EUR{PNL24} (+{PNL_FLIP_PCT}%) ainsi que de la baisse de marge brute
   EUR{BRUTO} ({BRUTO_PCT}%).
3. Matrice des subsides PHARE / ETA / COCOF derrière les charges de personnel (FTE {FTE}).
4. Répartition activités (atelier protégé / réadaptation épilepsie / sous-traitance / packaging).
5. Dettes LT/CT et trésorerie YE2025 (non publiées sur Companyweb).

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )
    print("foi draft written")


def append_log():
    with LOG.open("a", encoding="utf-8") as f:
        f.write(
            f"""


### 2026-08-27T08:55:00Z - tick 2267 - rq_2267 APRE Forest/Vorst (bruto DROP 2.02m / empty omzet / pnl PROFIT FLIP / FTE {FTE} / Medium)

- Unit: **rq_2267** leftover dual after **rq_2266 Brochage Renaitre**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024** (0201.712.587); REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre/APN still **YE2024**. Took named FREE Brussels ETA **APRE ASBL** YE2025 (KBO **{KBO}**; Neerstalse Steenweg 178 Vorst; **Actief** **1 VE**; NACE **88.999** PHARE / epilepsy adapted work). Do not redo Renaitre/Stallbois/Sipres/La Lorraine/BW Eupen/AJR/Alteria stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** ({FTE_PCT}% vs {FTE24}); neerlegging **29.07.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI via contact@apreservices.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2267=done + rq_2268 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2267/ + data/raw/tick2267/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2260**; next **2270**). Next: rq_2268 (AGB/FARO-if-YE2025 / AIESH-REW / unused ETA-VAPH-WZC-maatwerk).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2267"
    dst_raw = DATA / "raw" / "tick2267"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_apre_jr2025_cw_nl",
                "title": "Companyweb NL APRE YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet unpublished bruto DROP {BRUTO} pnl PROFIT FLIP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 29.07.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2267/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN APRE YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 29-07-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_apre_jr2025_cw_fr",
                "title": "Companyweb FR APRE YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_apre_kbo_{TICK}",
                "title": f"KBO APRE {KBO} Actief Vorst 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW A.P.R.E.; zetel Neerstalse Steenweg 178 1190 Vorst; "
                    f"1 VE; BTW NACE 88.999; begindatum 24.01.1967; KBO email/web empty"
                ),
            },
            {
                "source_id": f"src_apre_site_contact_{TICK}",
                "title": "APRE FOI channel contact@apreservices.be",
                "url": "https://apreservices.be/",
                "publisher": "APRE ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; contact@apreservices.be; +32 2 333 00 90; "
                    "Chaussée de Neerstalle 178 Forest; Brussels ETA epilepsy/PHARE"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_apre_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025 (primary; omzet unpublished)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}% vs YE2024 {BRUTO24}; empty omzet",
            },
            {
                "budget_id": "bud_apre_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 PROFIT FLIP",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl PROFIT FLIP +{PNL_FLIP_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_apre_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW statutory eigen_vermogen YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_apre_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": f"CW social-balance FTE {FTE}",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; FTE {FTE} vs YE2024 {FTE24}; assets/debt Unknown",
            },
            {
                "budget_id": "bud_apre_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative (pre PROFIT FLIP)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl LOSS {PNL24} comparative (pre PROFIT FLIP +{PNL_FLIP_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "APRE YE2025 leftover dual "
                    f"(bruto 2.02m / empty omzet / pnl PROFIT FLIP / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Forest / Brussels adapted-work public path PHARE epilepsy",
                "legal_basis": f"ASBL ETA APRE (KBO {KBO}; Actief; 1 VE; NACE 88.999; Vorst)",
                "decision_date": "2026-07-29",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    "{"
                    f'"2025_omzet":null,"2025_bruto":{BRUTO},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_fte":{FTE},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},"2024_fte":{FTE24}'
                    "}"
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Brussels ETA sheltered workshop Forest (epilepsy adaptation / packaging)",
                "cut_option": (
                    "Publish NBB PDF assets/debt + omzet; reconcile PROFIT FLIP vs PHARE/COCOF ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Bruxelles>Forest>APRE>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); "
                    f"pnl PROFIT FLIP {PNL}; equity JUMP {EQUITY}; FTE {FTE}; 1 VE; after Renaitre@2266; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    f"APRE bruto 2.02m / empty omzet / pnl PROFIT FLIP / FTE {FTE} "
                    "(YE2025 Brussels ETA epilepsy)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Bruxelles>Forest>APRE>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} ({BRUTO_PCT}%) / omzet unpublished / pnl PROFIT FLIP {PNL} "
                    f"(+{PNL_FLIP_PCT}%) / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / "
                    "1 VE Brussels ETA epilepsy"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Forest / Brussels adapted-work public path PHARE epilepsy",
                "stated_goal": "Brussels ETA sheltered workshop Forest (epilepsy adaptation)",
                "measured_outcome": (
                    f"bruto DROP {BRUTO_PCT}%; omzet unpublished; pnl PROFIT FLIP +{PNL_FLIP_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE} ({FTE_PCT}%); filed 29.07.2026"
                ),
                "absurdity_score": "6.5",
                "cost_score": "4.0",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/omzet FOI; disclose PHARE/COCOF ETA matrix behind empty omzet + PROFIT FLIP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Renaitre@2266"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "APRE VZW (Vorst / Brussels ETA epilepsie maatwerk)",
                "name_fr": "APRE ASBL (Forest / entreprise de travail adapté bruxelloise épilepsie)",
                "name_en": "APRE adapted-work ASBL (Forest Brussels ETA epilepsy)",
                "level": "parastatal",
                "parent_id": "sec_brussels",
                "community_language": "fr",
                "website": "https://apreservices.be/",
                "foi_email": "contact@apreservices.be",
                "foi_postal": "Chaussée de Neerstalle 178, 1190 Forest",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.999; "
                    f"omzet unpublished bruto DROP {BRUTO} ({BRUTO_PCT}%) pnl PROFIT FLIP {PNL} "
                    f"equity JUMP {EQUITY} (+{EQUITY_PCT}%) FTE {FTE}; neerlegging 29.07.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after Renaitre@2266; AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Bruxelles>Forest>APRE>NBB_PDF_assets_debt_empty_omzet_pnl_profit_flip",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO}; pnl PROFIT FLIP EUR{PNL} vs EUR{PNL24}; "
                    f"PHARE/COCOF ETA subsidy matrix; FTE {FTE}; activity split epilepsy workshop"
                ),
                "why_it_matters": (
                    f"Medium CW shows Brussels ETA ASBL (bruto 2.02m / empty omzet / pnl PROFIT FLIP / "
                    f"FTE {FTE}) under PHARE epilepsy path; assets/debt/omzet unpublished"
                ),
                "priority": "8",
                "recipient_body": "APRE ASBL",
                "recipient_email": "contact@apreservices.be",
                "recipient_postal": "Chaussée de Neerstalle 178, 1190 Forest",
                "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
                "status": "ready",
                "date_ready": DATE,
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/REW YE2024; "
                    "AGB Bornem JR2024; after Renaitre@2266; next EVERY-10 2270"
                ),
            }
        ],
    )

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
