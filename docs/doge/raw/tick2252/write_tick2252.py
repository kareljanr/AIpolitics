# tick 2252 — Le Moulin de la Hunelle Chièvres YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

csv.field_size_limit(10_000_000)

TICK = 2252
UTC = "2026-08-27T05:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_moulin_hunelle_chievres"
KBO = "0411.558.033"
KBO_BARE = "0411558033"
SRC_EN = "src_hunelle_jr2025_cw_en"
GAP = "gap_hunelle_nbb_pdf_assets_debt_bruto_gt_omzet_1_70x_pnl_loss_flip_eta_matrix_l5"
COMM = "comm_hunelle_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_flip"
LB = "lb_hunelle_omzet_2_05m_bruto_1_70x_pnl_loss_flip_jr2025"
RQ = "rq_2252"
RQ_NEXT = "rq_2253"

OMZET = 2045841
OMZET24 = 2105324
BRUTO = 3467890
BRUTO24 = 3742263
PNL = -18963
PNL24 = 82461
EQUITY = 6458761
EQUITY24 = 6477724
FTE = 111.4
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)


def append_csv(path: Path, rows: list[dict]):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    id_key = fieldnames[0]
    ids = {r[id_key] for r in existing}
    new = [r for r in rows if r[id_key] not in ids]
    if not new:
        print(f"skip append {path.name}")
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
                "leftover dual — Le Moulin de la Hunelle YE2025 Medium "
                f"(omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Hunelle ASBL Chièvres {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}% vs {OMZET24}); bruto DROP {BRUTO} (~{RATIO}x); "
                f"pnl LOSS FLIP {PNL} vs YE2024 {PNL24}; equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE}; 2 VE; NACE 88.993; neerlegging 01.07.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024 / "
                f"Heropbeuring CW opaque; after Dauphins@2251; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Le Moulin de la Hunelle YE2025 FREE Walloon ETA after Dauphins; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found, "rq_2252 missing"

    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Hunelle — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Le Moulin de la Hunelle YE2025 Medium "
                    f"(omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Les Gaillettes / Sipres / Relais Haute Sambre / APN "
                    "if YE2025 FREE; skip Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/"
                    "Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Dauphins Visé still CW N/A; Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Hunelle; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; deferred FREE Gaillettes; next every-10 2260"
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
                f"tick{TICK} leftover Hunelle {KBO} Medium (omzet DROP {OMZET}; "
                f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; bruto {BRUTO} ~{RATIO}x; FTE {FTE}; 2 VE ETA Chièvres); "
                f"after Dauphins@2251; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
                f"deferred FREE Gaillettes; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
    path = FOI / f"{GAP}.md"
    path.write_text(
        f"""# FOI draft — Le Moulin de la Hunelle (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Le Moulin de la Hunelle ASBL — KBO **{KBO}** (Actief; Rue d'Ath 90, 7950 Chièvres; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Chièvres / Hainaut)  
**recipient:** info@hunelle.be · Rue d'Ath 90, 7950 Chièvres  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [leseta](https://leseta.be/annuaire-eta/le-moulin-de-la-hunelle/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL Le Moulin de la Hunelle; **2 VE**; zetel Chièvres; NACE **88.993** (+88.995).
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** DROP {BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP vs YE2024 profit EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}**; filed **01.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Dauphins@2251. Deferred FREE Les Gaillettes.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Le Moulin de la Hunelle ASBL
via info@hunelle.be
Rue d'Ath 90, 7950 Chièvres
Objet: Publicité des comptes annuels 2025 Le Moulin de la Hunelle (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24} — réconciliation avec FTE {FTE}.
4. Matrice des subsides AVIQ / ETA / Province de Hainaut derrière les charges de personnel.
5. Répartition coûts restaurant / ferme / espaces verts / abattoir / aménagement.

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
    entry = f"""

## Tick {TICK} - {UTC} - rq_2252 Le Moulin de la Hunelle Chièvres (omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} / Medium)

- Unit: **rq_2252** leftover dual after **rq_2251 Les Dauphins**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Sipres/APN still **YE2024**. Took named FREE Walloon ETA **Le Moulin de la Hunelle ASBL** YE2025 (KBO **{KBO}**; Rue d'Ath 90 Chièvres; **Actief** **2 VE**; NACE **88.993** AViQ / Hainaut). Deferred FREE Les Gaillettes. Do not redo Dauphins/Saupont/Serviplast/Jean Del'Cour stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** DROP {BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP vs YE2024 profit EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}**; neerlegging **01.07.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@hunelle.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 5.70); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2252=done + rq_2253 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2252/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2253 (AGB/FARO-if-YE2025 / AIESH-REW / unused Gaillettes).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log appended")


def main():
    sources = [
        {
            "source_id": "src_hunelle_jr2025_cw_nl",
            "title": "Companyweb NL Le Moulin de la Hunelle YE2025 statutory",
            "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; YE2025 omzet DROP {OMZET} pnl LOSS FLIP {PNL} equity DROP {EQUITY} "
                f"bruto {BRUTO} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; "
                f"raw docs/doge/data/raw/tick2252/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Le Moulin de la Hunelle YE2025 statutory",
            "url": f"https://www.companyweb.be/en/{KBO_BARE}",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; EN mirror YE2025 Medium; filed 01-07-2026; Last balance sheet year 2025; "
                f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
            ),
        },
        {
            "source_id": "src_hunelle_jr2025_cw_fr",
            "title": "Companyweb FR Le Moulin de la Hunelle YE2025 statutory",
            "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}",
        },
        {
            "source_id": f"src_hunelle_kbo_{TICK}",
            "title": f"KBO Le Moulin de la Hunelle {KBO} Actief Chièvres 2 VE",
            "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
            "publisher": "KBO FOD Economie",
            "accessed_date": DATE,
            "source_class": "official_register",
            "notes": (
                f"tick{TICK}; Actief VZW/ASBL Le Moulin de la Hunelle; zetel Rue d'Ath 90 7950 Chièvres; "
                f"2 VE; NACE 88.993/88.995; begindatum 07.10.1971; KBO email empty"
            ),
        },
        {
            "source_id": f"src_hunelle_site_contact_{TICK}",
            "title": "Le Moulin de la Hunelle FOI channel info@hunelle.be",
            "url": "https://leseta.be/annuaire-eta/le-moulin-de-la-hunelle/",
            "publisher": "Les ETA / Eweta annuaire",
            "accessed_date": DATE,
            "source_class": "foi_contact",
            "notes": (
                f"tick{TICK}; info@hunelle.be; Rue d'Ath 90 7950 Chièvres; "
                "Hainaut provincial ETA path (ferme/resto/espaces verts/abattoir)"
            ),
        },
    ]
    append_csv(DATA / "sources.csv", sources)

    budgets = [
        {
            "budget_id": "bud_hunelle_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet DROP {OMZET_PCT}% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_hunelle_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP {BRUTO_PCT}%; bruto≫omzet ~{RATIO}x",
        },
        {
            "budget_id": "bud_hunelle_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst/verlies YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 profit {PNL24}",
        },
        {
            "budget_id": "bud_hunelle_equity_jr2025_statutory",
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
            "budget_id": "bud_hunelle_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE {FTE}; YE2024 FTE Unknown on CW page; assets/debt Unknown",
        },
        {
            "budget_id": "bud_hunelle_omzet_jr2024_statutory_cmp",
            "entity_id": ENTITY,
            "year": "2024",
            "amount_eur": str(OMZET24),
            "amount_min_eur": str(OMZET24),
            "amount_max_eur": str(OMZET24),
            "basis": "CW statutory omzet YE2024 comparative",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; YE2024 omzet {OMZET24} comparative (pre DROP)",
        },
    ]
    append_csv(DATA / "budgets.csv", budgets)

    commitments = [
        {
            "commitment_id": COMM,
            "title": (
                "Le Moulin de la Hunelle YE2025 leftover dual "
                f"(omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE} / Medium)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "ETA workers Chièvres / AVIQ + Province Hainaut adapted-work path",
            "legal_basis": f"ASBL ETA Le Moulin de la Hunelle (KBO {KBO}; Actief; 2 VE; NACE 88.993; Chièvres)",
            "decision_date": "2026-07-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
            "stated_goal": "Walloon ETA farm / restaurant / green spaces / abattoir / fit-out",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; reconcile pnl LOSS FLIP vs AVIQ/Hainaut ETA subsidy matrix; "
                f"explain bruto≫omzet ~{RATIO}x"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Wallonie>Hainaut>Chievres>Hunelle>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl LOSS FLIP {PNL}; "
                f"FTE {FTE}; 2 VE; after Dauphins@2251; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        }
    ]
    append_csv(DATA / "commitments.csv", commitments)

    leaderboard = [
        {
            "item_id": LB,
            "name": (
                f"Le Moulin de la Hunelle omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP "
                f"/ FTE {FTE} (YE2025 Walloon ETA)"
            ),
            "level": "L5",
            "type": "eta_asbl_statutory",
            "hierarchy_path": "Wallonie>Hainaut>Chievres>Hunelle>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl LOSS FLIP {PNL} / "
                f"equity DROP {EQUITY} / FTE {FTE} / 2 VE Walloon ETA"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "ETA workers Chièvres / AVIQ + Province Hainaut adapted-work path",
            "stated_goal": "Walloon ETA farm / restaurant / green spaces / abattoir",
            "measured_outcome": (
                f"omzet DROP {OMZET_PCT}%; pnl LOSS FLIP {PNL}; equity DROP {EQUITY_PCT}%; "
                f"FTE {FTE}; filed 01.07.2026"
            ),
            "absurdity_score": "7.0",
            "cost_score": "4.2",
            "difficulty": "3.0",
            "priority_index": "5.70",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ/Hainaut ETA matrix; "
                "reconcile pnl LOSS FLIP + bruto≫omzet"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; after Dauphins@2251; deferred FREE Gaillettes"
            ),
        }
    ]
    append_csv(DATA / "leaderboard.csv", leaderboard)

    entities = [
        {
            "entity_id": ENTITY,
            "name_nl": "Le Moulin de la Hunelle VZW (Chièvres / ETA maatwerk Henegouwen)",
            "name_fr": "Le Moulin de la Hunelle ASBL (Chièvres / entreprise de travail adapté Hainaut)",
            "name_en": "Le Moulin de la Hunelle adapted-work ASBL (Chièvres Walloon ETA)",
            "level": "parastatal",
            "parent_id": "sec_wallonia",
            "community_language": "fr",
            "website": "https://leseta.be/annuaire-eta/le-moulin-de-la-hunelle/",
            "foi_email": "info@hunelle.be",
            "foi_postal": "Rue d'Ath 90, 7950 Chièvres",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                f"omzet DROP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl LOSS FLIP {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; FOI {GAP}; preferred stalls "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; after Dauphins@2251; "
                "Hainaut provincial ETA path; not TE-additive of 348bn"
            ),
        }
    ]
    append_csv(DATA / "entities.csv", entities)

    foi_rows = [
        {
            "gap_id": GAP,
            "hierarchy_path": "Wallonie>Hainaut>Chievres>Hunelle>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip",
            "entity_id": ENTITY,
            "what_is_missing": (
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                f"bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24}; "
                f"FTE {FTE}; AVIQ/Hainaut ETA subsidy matrix"
            ),
            "why_it_matters": (
                f"Medium CW shows Walloon ETA ASBL (omzet 2.05m / bruto~{RATIO}x / pnl LOSS FLIP / FTE {FTE}) "
                "under AVIQ/Hainaut path; assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Le Moulin de la Hunelle ASBL",
            "recipient_email": "info@hunelle.be",
            "recipient_postal": "Rue d'Ath 90, 7950 Chièvres",
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
                "AGB Bornem JR2024; Heropbeuring CW opaque; after Dauphins@2251; next EVERY-10 2260"
            ),
        }
    ]
    append_csv(DATA / "foi_queue.csv", foi_rows)

    write_foi_draft()
    update_research_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
