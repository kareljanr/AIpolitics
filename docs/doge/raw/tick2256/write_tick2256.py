# tick 2256 — Belair Marche-en-Famenne YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2256
UTC = "2026-08-27T06:10:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_belair_marche"
KBO = "0473.806.396"
KBO_BARE = "0473806396"
SRC_EN = "src_belair_jr2025_cw_en"
GAP = "gap_belair_nbb_pdf_assets_debt_empty_omzet_pnl_drop_73pct_eta_matrix_l5"
COMM = "comm_belair_jr2025_statutory_eta_empty_omzet_pnl_drop_73pct"
LB = "lb_belair_bruto_3_80m_empty_omzet_pnl_drop_73pct_jr2025"
RQ = "rq_2256"
RQ_NEXT = "rq_2257"

OMZET = None  # unpublished
BRUTO = 3799268
BRUTO24 = 3604864
PNL = 30342
PNL24 = 112047
EQUITY = 1997569
EQUITY24 = 1967226
FTE = 83.1
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
PNL_PCT = round((PNL - PNL24) / PNL24 * 100, 2)
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
                "leftover dual — Belair YE2025 Medium "
                f"(bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Belair ASBL Marche-en-Famenne {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet unpublished; bruto JUMP {BRUTO} (+{BRUTO_PCT}%); pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); "
                f"equity JUMP {EQUITY} (+{EQUITY_PCT}%); FTE {FTE}; 1 VE; NACE 88.993; neerlegging 06.07.2026; "
                f"assets/debt Unknown; FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre YE2024; after Corelap@2255; deferred FREE Nekto/Val du Geer/Erables; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Belair YE2025 FREE Walloon ETA after Corelap; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Belair — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Belair YE2025 Medium "
                    f"(bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Nekto / Val du Geer / Les Erables if YE2025 FREE; "
                    "skip Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/"
                    "Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/"
                    "L'Atelier/Axedis/ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/"
                    "Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/"
                    "ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; "
                    "Relais Haute Sambre/Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Belair; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre YE2024; deferred FREE Nekto/Val du Geer/Erables; "
                    "next every-10 2260"
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
                f"tick{TICK} leftover Belair {KBO} Medium (bruto JUMP {BRUTO}; empty omzet; "
                f"pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE {FTE}; 1 VE Marche ETA); "
                f"after Corelap@2255; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; "
                f"deferred FREE Nekto/Val du Geer/Erables; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Belair (NBB PDF / empty omzet / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Belair ASBL — KBO **{KBO}** (Actief; Aye, Rue André Feher 8, 6900 Marche-en-Famenne; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Marche)  
**recipient:** info@belair-eta144.be · Aye, Rue André Feher 8, 6900 Marche-en-Famenne  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [leseta](https://leseta.be/annuaire-eta/belair/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; omzet empty; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL BELAIR; **1 VE**; zetel Marche-en-Famenne/Aye; NACE **88.993** (+88.995 / green spaces).
- CW YE2025: omzet **unpublished**; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24:,}; pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; filed **06.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024. After Corelap@2255.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Belair ASBL
via info@belair-eta144.be
Aye, Rue André Feher 8, 6900 Marche-en-Famenne
Objet: Publicité des comptes annuels 2025 Belair (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BRUTO} et chiffre d'affaires (omzet non publié sur Companyweb).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts espaces verts / nettoyage / sylviculture / menuiserie.

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

## Tick {TICK} - {UTC} - rq_2256 Belair Marche-en-Famenne (bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2256** leftover dual after **rq_2255 Corelap**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre still **YE2024**. Took named FREE Walloon ETA **Belair ASBL** YE2025 (KBO **{KBO}**; Aye Rue André Feher 8 Marche-en-Famenne; **Actief** **1 VE**; NACE **88.993** AViQ). Deferred FREE Nekto/Val du Geer/Les Erables. Do not redo Corelap/Cambier/Gaillettes/Hunelle stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% vs YE2024 EUR{BRUTO24}; pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; neerlegging **06.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@belair-eta144.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.90); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2256=done + rq_2257 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2256/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2257 (AGB/FARO-if-YE2025 / AIESH-REW / unused Nekto).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_belair_jr2025_cw_nl",
                "title": "Companyweb NL Belair YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet empty bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"FTE {FTE}; neerlegging 06.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2256/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Belair YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 06-07-2026; Last balance sheet year 2025; "
                    f"Turnover unpublished Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_belair_jr2025_cw_fr",
                "title": "Companyweb FR Belair YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA non publié; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_belair_kbo_{TICK}",
                "title": f"KBO Belair {KBO} Actief Marche-en-Famenne 1 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL BELAIR; zetel Aye Rue André Feher 8 6900 Marche-en-Famenne "
                    f"(Zoning Industriel); 1 VE; NACE 88.993/88.995/81.210/81.300; begindatum 21.12.2000; KBO email empty"
                ),
            },
            {
                "source_id": f"src_belair_site_contact_{TICK}",
                "title": "Belair FOI channel info@belair-eta144.be",
                "url": "https://leseta.be/annuaire-eta/belair/",
                "publisher": "Les ETA / Eweta annuaire",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@belair-eta144.be / mc@belair-eta144.be; "
                    "Aye Rue André Feher 8 6900 Marche-en-Famenne; green spaces / cleaning ETA"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_belair_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; omzet empty (primary envelope)",
            },
            {
                "budget_id": "bud_belair_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW statutory winst/verlies YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL24}",
            },
            {
                "budget_id": "bud_belair_equity_jr2025_statutory",
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
                "budget_id": "bud_belair_fte_jr2025_statutory",
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
                "budget_id": "bud_belair_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP -73%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Belair YE2025 leftover dual "
                    f"(bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Marche-en-Famenne / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Belair (KBO {KBO}; Actief; 1 VE; NACE 88.993; Marche-en-Famenne)",
                "decision_date": "2026-07-06",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    f'{{"2025_bruto":{BRUTO},"2025_omzet":null,"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO24},'
                    f'"2024_pnl":{PNL24},"2024_equity":{EQUITY24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA green spaces / cleaning / forestry Marche",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; disclose empty-omzet vs bruto 3.80m AVIQ ETA matrix; "
                    "reconcile pnl DROP -73%"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Luxembourg>Marche>Belair>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} (omzet empty); pnl DROP {PNL}; "
                    f"FTE {FTE}; 1 VE; after Corelap@2255; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "not TE-additive of 348bn"
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
                    f"Belair bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Luxembourg>Marche>Belair>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} / omzet empty / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} / 1 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Marche-en-Famenne / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA green spaces / cleaning / forestry",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet unpublished; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 06.07.2026"
                ),
                "absurdity_score": "7.2",
                "cost_score": "4.5",
                "difficulty": "3.0",
                "priority_index": "5.90",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose empty-omzet vs bruto; "
                    "reconcile pnl DROP -73% + AVIQ ETA matrix"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Corelap@2255; deferred FREE Nekto"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Belair VZW (Marche-en-Famenne / ETA maatwerk Luxemburg BE)",
                "name_fr": "Belair ASBL (Marche-en-Famenne / entreprise de travail adapté Luxembourg BE)",
                "name_en": "Belair adapted-work ASBL (Marche Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://leseta.be/annuaire-eta/belair/",
                "foi_email": "info@belair-eta144.be",
                "foi_postal": "Aye, Rue André Feher 8, 6900 Marche-en-Famenne",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 1 VE NACE 88.993; "
                    f"omzet empty bruto JUMP {BRUTO} pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                    f"FTE {FTE}; neerlegging 06.07.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Corelap@2255; "
                    "not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Luxembourg>Marche>Belair>NBB_PDF_assets_debt_empty_omzet_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet unpublished on CW; "
                    f"bruto EUR{BRUTO}; pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 3.80m / empty omzet / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Belair ASBL",
                "recipient_email": "info@belair-eta144.be",
                "recipient_postal": "Aye, Rue André Feher 8, 6900 Marche-en-Famenne",
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
                    "AGB Bornem JR2024; after Corelap@2255; next EVERY-10 2260"
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
