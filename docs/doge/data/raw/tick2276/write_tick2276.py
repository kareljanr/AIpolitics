# tick 2276 — leftover dual Atelier Saint-Vincent YE2025 Medium (bruto JUMP 2.89m / empty omzet / pnl LOSS NARROW / FTE 75.2)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2276
UTC = "2026-08-27T11:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_atelier_saint_vincent_rochefort"
KBO = "0414.231.471"
KBO_BARE = "0414231471"
SRC_EN = "src_asv_jr2025_cw_en"
GAP = "gap_asv_nbb_pdf_assets_debt_empty_omzet_bruto_2_89m_pnl_loss_narrow_eta_matrix_l5"
COMM = "comm_asv_jr2025_statutory_eta_empty_omzet_bruto_2_89m_pnl_loss_narrow"
LB = "lb_asv_bruto_2_89m_empty_omzet_pnl_loss_narrow_jr2025"
RQ = "rq_2276"
RQ_NEXT = "rq_2277"

BRUTO = 2891462
BRUTO24 = 2635998
PNL = -30831
PNL24 = -114469
EQUITY = 2395817
EQUITY24 = 2436009
FTE = 75.2
FTE24 = 69.6
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / abs(PNL24) * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)
FTE_PCT = round((FTE - FTE24) / FTE24 * 100, 2)
PI = "5.90"


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
                "leftover dual — Atelier Saint-Vincent YE2025 Medium "
                f"(bruto JUMP 2.89m / empty omzet / pnl LOSS NARROW / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Atelier Saint-Vincent ASBL Rochefort {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto JUMP {BRUTO} (+{BRUTO_PCT}%); "
                f"pnl LOSS NARROW {PNL} (+{PNL_PCT}% vs {PNL24}); equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE} (+{FTE_PCT}% vs {FTE24}); 1 VE; NACE 88.993/96.101; neerlegging 11.05.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / "
                f"FARO/AIESH/Citeco/Groupe Foes YE2024; after APAC+Adapta@2275; next EVERY-10 2280"
            )
            r["instructions"] = (
                "leftover dual Atelier Saint-Vincent YE2025 FREE Walloon ETA Rochefort laundry after A.P.A.C./Adapta; "
                "preferred AGB/FARO/AIESH/Citeco/Groupe Foes still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Atelier Saint-Vincent — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Citeco-Groupe Foes-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Atelier Saint-Vincent YE2025 Medium "
                    f"(bruto JUMP 2.89m / empty omzet / pnl LOSS NARROW / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else named FREE Citeco if YE2025 / Groupe Foes if YE2025, "
                    "else unused ETA-VAPH-WZC-maatwerk with live sourced euros. "
                    "Skip Atelier Saint-Vincent/A.P.A.C./Adapta/Atelier 85/La Gaume/Fournipac/"
                    "De Enter/La Serre-Outil/Amis des Aveugles/Hautes Ardennes/Village n°1/"
                    "Le Trait d'Union/L'Ouvroir/APRE/Brochage Renaitre/Stallbois/Sipres/La Lorraine/"
                    "BW Eupen/AJR/Alteria; Relais Haute Sambre/APN YE2024; Citeco/Groupe Foes YE2024. "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. Next EVERY-10: 2280."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Atelier Saint-Vincent; FARO/AIESH/Citeco/Groupe Foes YE2024; "
                    "AGB Bornem JR2024; next every-10 2280"
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
                f"tick{TICK} leftover dual Atelier Saint-Vincent {KBO} Medium (bruto JUMP {BRUTO} +{BRUTO_PCT}%; "
                f"empty omzet; pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; "
                f"1 VE Rochefort Walloon ETA AViQ industrial laundry/workwear); after APAC+Adapta@2275; "
                f"AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; next {RQ_NEXT}; "
                f"next EVERY-10 2280; continuous hole_fill"
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
        f"""# FOI draft — Atelier Saint-Vincent (NBB PDF / empty omzet / bruto 2.89m / pnl LOSS NARROW / Walloon ETA)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Atelier Saint-Vincent ASBL — KBO **{KBO}** (Actief; Rue du Tige 44, 5580 Rochefort; **1 VE**; FTE {FTE} CW; NACE **88.993** / **96.101**; Walloon ETA AViQ laundry)  
**recipient:** postal Rue du Tige 44, 5580 Rochefort · +32 84 21 17 77 (no published email on KBO/site)  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/atelier-saint-vincent) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/atelier-saint-vincent) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/atelier-saint-vincent) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=fr&ondernemingsnummer={KBO_BARE}) · [site](https://www.atelierstvincent.be/) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/{KBO_BARE})  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown; omzet unpublished)

## Context
- KBO Strong: Actief ASBL Atelier Saint - Vincent; **1 VE**; zetel Rue du Tige 44, 5580 Rochefort; RSZ NACE **88.993**; TVA **96.101** industrial laundry; begindatum 29.03.1974.
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** LOSS NARROW +{PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}% vs YE2024 EUR{EQUITY24:,}; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); filed **11.05.2026**.
- Preferred stall check this tick: AGB Bornem JR2024; FARO YE2024; AIESH YE2024; Citeco YE2024; Groupe Foes YE2024; Relais Haute Sambre YE2024; APN YE2024; Heropbeuring CW opaque. After A.P.A.C./Adapta@2275.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Atelier Saint-Vincent ASBL
Rue du Tige 44
5580 Rochefort
(+32 84 21 17 77)
Objet: Publicité des comptes annuels 2025 Atelier Saint-Vincent (BCE {KBO})

Madame, Monsieur,

Sur la base des règles applicables en matière de publicité de l'administration
(Région wallonne / AViQ / Code de la démocratie locale), je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Chiffre d'affaires YE2025 (non publié sur Companyweb) et explication de la marge brute
   EUR{BRUTO} (+{BRUTO_PCT}%) malgré perte EUR{PNL} (amélioration vs EUR{PNL24}).
3. Matrice des subsides AViQ / ETA derrière les charges de personnel (FTE {FTE}).
4. Répartition CA/activités (blanchisserie industrielle / location vêtements de travail / Horeca).
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


### 2026-08-27T11:10:00Z - tick 2276 - rq_2276 Atelier Saint-Vincent Rochefort (bruto JUMP 2.89m / empty omzet / pnl LOSS NARROW / FTE {FTE} / Medium)

- Unit: **rq_2276** leftover dual after **rq_2275 A.P.A.C./Adapta**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; Citeco/Groupe Foes still **YE2024**; Relais Haute Sambre/APN still **YE2024**; Heropbeuring CW opaque. Took FREE Walloon ETA **Atelier Saint-Vincent ASBL** YE2025 (KBO **{KBO}**; Rue du Tige 44 Rochefort; **Actief** **1 VE**; NACE **88.993**/**96.101** AViQ industrial laundry/workwear). Do not redo APAC/Adapta/Atelier85/La Gaume/Fournipac/Amis/Hautes stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** LOSS NARROW +{PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}** (+{FTE_PCT}% vs {FTE24}); neerlegging **11.05.2026**. Strong KBO Actief 1 VE ASBL. Assets/debt Unknown. Medium. FOI postal +32 84 21 17 77 (no published email).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2276=done + rq_2277 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2276/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2270**; next **2280**). Next: rq_2277 (AGB/FARO-if-YE2025 / AIESH-REW / Citeco-Foes-if-YE2025 / unused ETA).
"""
        )
    print("loop_log appended")


def main():
    src_raw = ROOT / "docs" / "doge" / "raw" / "tick2276"
    dst_raw = DATA / "raw" / "tick2276"
    dst_raw.mkdir(parents=True, exist_ok=True)
    src_raw.mkdir(parents=True, exist_ok=True)
    for f in dst_raw.glob("*.html"):
        shutil.copy2(f, src_raw / f.name)
    shutil.copy2(Path(__file__), src_raw / Path(__file__).name)

    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_asv_jr2025_cw_nl",
                "title": "Companyweb NL Atelier Saint-Vincent YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/atelier-saint-vincent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet unpublished bruto JUMP {BRUTO} pnl LOSS NARROW {PNL} "
                    f"equity DROP {EQUITY} FTE {FTE}; neerlegging 11.05.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2276/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Atelier Saint-Vincent YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/atelier-saint-vincent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 11-05-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_asv_jr2025_cw_fr",
                "title": "Companyweb FR Atelier Saint-Vincent YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/atelier-saint-vincent",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BRUTO}; Benefice {PNL}",
            },
            {
                "source_id": f"src_asv_kbo_{TICK}",
                "title": f"KBO Atelier Saint-Vincent {KBO} Actief Rochefort 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=fr&ondernemingsnummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief ASBL Atelier Saint - Vincent; zetel Rue du Tige 44 5580 Rochefort; "
                    f"1 VE; RSZ NACE 88.993; TVA 96.101; begindatum 29.03.1974"
                ),
            },
            {
                "source_id": f"src_asv_site_contact_{TICK}",
                "title": "Atelier Saint-Vincent FOI channel postal +32 84 21 17 77",
                "url": "https://www.atelierstvincent.be/",
                "publisher": "Atelier Saint-Vincent ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; no published email on KBO/site; +32 84 21 17 77; "
                    "Rue du Tige 44 Rochefort; Walloon ETA AViQ industrial laundry/workwear"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_asv_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025 (primary; omzet unpublished)",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO24}; empty omzet",
            },
            {
                "budget_id": "bud_asv_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025 LOSS NARROW",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl LOSS NARROW +{PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_asv_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW statutory eigen_vermogen YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; equity DROP {EQUITY_PCT}% vs YE2024 {EQUITY24}",
            },
            {
                "budget_id": "bud_asv_fte_jr2025_statutory",
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
                "budget_id": "bud_asv_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory pnl YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre LOSS NARROW +{PNL_PCT}%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Atelier Saint-Vincent YE2025 leftover dual "
                    f"(bruto 2.89m / empty omzet / pnl LOSS NARROW / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Rochefort / Walloon adapted-work public path AViQ laundry",
                "legal_basis": f"ASBL ETA Atelier Saint-Vincent (KBO {KBO}; Actief; 1 VE; NACE 88.993/96.101; Rochefort)",
                "decision_date": "2026-05-11",
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
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/atelier-saint-vincent",
                "stated_goal": "Walloon ETA sheltered workshop Rochefort (industrial laundry / workwear rental)",
                "cut_option": (
                    "Publish NBB PDF assets/debt + omzet; reconcile bruto JUMP + LOSS NARROW vs AViQ ETA matrix"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Namur>Rochefort>Atelier_Saint_Vincent>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet unpublished); "
                    f"pnl LOSS NARROW {PNL}; equity DROP {EQUITY}; FTE {FTE}; 1 VE; after APAC+Adapta@2275; "
                    "AGB Bornem JR2024; FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
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
                    f"Atelier Saint-Vincent bruto 2.89m / empty omzet / pnl LOSS NARROW / FTE {FTE} "
                    "(YE2025 Walloon ETA Rochefort)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Namur>Rochefort>Atelier_Saint_Vincent>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (+{BRUTO_PCT}%) / omzet unpublished / pnl LOSS NARROW {PNL} (+{PNL_PCT}%) / "
                    f"equity DROP {EQUITY} ({EQUITY_PCT}%) / FTE {FTE} (vs {FTE24}) / 1 VE Walloon ETA laundry"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Rochefort / Walloon adapted-work public path AViQ",
                "stated_goal": "Walloon ETA sheltered workshop Rochefort (laundry/workwear)",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet unpublished; pnl LOSS NARROW +{PNL_PCT}%; "
                    f"equity DROP {EQUITY_PCT}%; FTE {FTE} (+{FTE_PCT}%); filed 11.05.2026"
                ),
                "absurdity_score": "6.9",
                "cost_score": "4.0",
                "difficulty": "3.0",
                "priority_index": PI,
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/omzet FOI; disclose AViQ ETA matrix behind empty omzet + LOSS despite bruto JUMP"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; after APAC+Adapta@2275"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Atelier Saint-Vincent VZW (Rochefort / Walloon ETA wasserij)",
                "name_fr": "Atelier Saint-Vincent ASBL (Rochefort / entreprise de travail adapté blanchisserie)",
                "name_en": "Atelier Saint-Vincent adapted-work ASBL (Rochefort Walloon ETA laundry)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.atelierstvincent.be/",
                "foi_email": "",
                "foi_postal": "Rue du Tige 44, 5580 Rochefort (+32 84 21 17 77)",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993/96.101; "
                    f"omzet unpublished bruto JUMP {BRUTO} (+{BRUTO_PCT}%) pnl LOSS NARROW {PNL} (+{PNL_PCT}%) "
                    f"equity DROP {EQUITY} ({EQUITY_PCT}%) FTE {FTE}; neerlegging 11.05.2026; "
                    f"assets/debt Unknown; FOI {GAP}; after APAC+Adapta@2275; AGB Bornem JR2024; "
                    "FARO/AIESH/Citeco/Groupe Foes YE2024; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Namur>Rochefort>Atelier_Saint_Vincent>NBB_PDF_assets_debt_empty_omzet_bruto_2_89m",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO}; pnl LOSS NARROW EUR{PNL} vs EUR{PNL24}; "
                    f"AViQ ETA subsidy matrix; FTE {FTE}; activity split laundry/workwear/Horeca"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 2.89m / empty omzet / pnl LOSS NARROW / "
                    f"FTE {FTE}) under AViQ path; assets/debt/omzet unpublished"
                ),
                "priority": "8",
                "recipient_body": "Atelier Saint-Vincent ASBL",
                "recipient_email": "",
                "recipient_postal": "Rue du Tige 44, 5580 Rochefort (+32 84 21 17 77)",
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
                    f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; no published email (postal+phone); "
                    "preferred stall FARO/AIESH/Citeco/Foes YE2024; AGB Bornem JR2024; after APAC@2275; next EVERY-10 2280"
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
