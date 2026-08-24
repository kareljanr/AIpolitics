# tick 2258 — Val du Geer Bassenge YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2258
UTC = "2026-08-27T06:40:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_val_du_geer_bassenge"
KBO = "0407.841.646"
KBO_BARE = "0407841646"
SRC_EN = "src_val_du_geer_jr2025_cw_en"
GAP = "gap_val_du_geer_nbb_pdf_assets_debt_pnl_drop_22pct_eta_matrix_l5"
COMM = "comm_val_du_geer_jr2025_statutory_eta_omzet_pnl_drop_22pct"
LB = "lb_val_du_geer_omzet_10_75m_pnl_drop_22pct_jr2025"
RQ = "rq_2258"
RQ_NEXT = "rq_2259"

OMZET = 10750401
OMZET24 = 10822629
BRUTO = 10374789
BRUTO24 = 9941227
PNL = 66091
PNL24 = 84628
EQUITY = 9460222
EQUITY24 = 9437263
FTE = 241.4
FTE24 = 240.7
RATIO = round(BRUTO / OMZET, 3)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
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
                "leftover dual — Val du Geer YE2025 Medium "
                f"(omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Val du Geer ASBL Bassenge {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet DROP {OMZET} ({OMZET_PCT}%); bruto JUMP {BRUTO} (+{BRUTO_PCT}%; ~{RATIO}x); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE}; 4 VE; NACE 88.993; neerlegging 09.06.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"Relais Haute Sambre YE2024; after Nekto@2257; deferred FREE Les Erables; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Val du Geer YE2025 FREE Walloon ETA after Nekto; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Val du Geer — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Val du Geer YE2025 Medium "
                    f"(omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Les Erables if YE2025 FREE; "
                    "skip Val du Geer/Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle/Dauphins Gembloux/"
                    "Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/"
                    "Jean Gielen/Le Perron/L'Atelier/Axedis/ETA 123 Beauraing/Manufast/Metalgroup/"
                    "EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/Het Rekreatief/Travie/SDB/"
                    "De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/Den Azalee/"
                    "Kemphaan/Mirto/Blankedale/Werkmmaat; Relais Haute Sambre/Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/"
                    "Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/"
                    "RESA/Enodia/Fluxys*/ETB/Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260 — MUST refresh progress_every_10_ticks.md + "
                    "doge_waste_top10_current.md then hole-fill one unit."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Val du Geer; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Relais Haute Sambre YE2024; deferred FREE Les Erables; "
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
                f"tick{TICK} leftover Val du Geer {KBO} Medium (omzet DROP {OMZET}; "
                f"bruto JUMP {BRUTO} ~{RATIO}x; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; "
                f"FTE {FTE}; 4 VE Bassenge ETA); after Nekto@2257; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024; deferred FREE Les Erables; "
                f"next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Val du Geer (NBB PDF / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Val du Geer ASBL — KBO **{KBO}** (Actief; Rue de la Cerisaie 8, 4690 Bassenge; **4 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Bassenge)  
**recipient:** info@valdugeer.be · Rue de la Cerisaie 8, 4690 Bassenge  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.valdugeer.be/013/fr/Contact) · [leseta](https://leseta.be/annuaire-eta/le-val-du-geer/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL VAL DU GEER; **4 VE**; zetel Bassenge Rue de la Cerisaie 8 (sinds 18.12.2025); NACE **88.993** (+88.995).
- CW YE2025: omzet **EUR{OMZET:,}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (~{RATIO}x omzet); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** (YE2024 {FTE24}); filed **09.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Relais Haute Sambre YE2024. After Nekto@2257.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Val du Geer ASBL
via info@valdugeer.be
Rue de la Cerisaie 8, 4690 Bassenge
Objet: Publicité des comptes annuels 2025 Val du Geer (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Réconciliation omzet EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x) et PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — lien FTE {FTE}.
3. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
4. Répartition coûts par atelier / site (4 VE) et type d'activité.

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

## Tick {TICK} - {UTC} - rq_2258 Val du Geer Bassenge (omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2258** leftover dual after **rq_2257 Nekto**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Relais Haute Sambre still **YE2024**. Took named FREE Walloon ETA **Val du Geer ASBL** YE2025 (KBO **{KBO}**; Rue de la Cerisaie 8 Bassenge; **Actief** **4 VE**; NACE **88.993** AViQ). Deferred FREE Les Erables. Do not redo Nekto/Belair/Corelap/Cambier/Gaillettes/Hunelle stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; neerlegging **09.06.2026**. Strong KBO Actief 4 VE. Assets/debt Unknown. Medium. FOI via info@valdugeer.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2258=done + rq_2259 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2258/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2259 (AGB/FARO-if-YE2025 / AIESH-REW / unused Les Erables); at **2260** MUST refresh progress + waste top10 then hole-fill.
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_val_du_geer_jr2025_cw_nl",
                "title": "Companyweb NL Val du Geer YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 09.06.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2258/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Val du Geer YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 09-06-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Gross margin {BRUTO} Profit/Loss {PNL} Equity {EQUITY} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_val_du_geer_jr2025_cw_fr",
                "title": "Companyweb FR Val du Geer YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_val_du_geer_kbo_{TICK}",
                "title": f"KBO Val du Geer {KBO} Actief Bassenge 4 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL VAL DU GEER; zetel Rue de la Cerisaie 8 4690 Bassenge "
                    f"(sinds 18.12.2025); 4 VE; NACE 88.993/88.995; begindatum 18.10.1964; KBO email empty"
                ),
            },
            {
                "source_id": f"src_val_du_geer_site_contact_{TICK}",
                "title": "Val du Geer FOI channel info@valdugeer.be",
                "url": "https://www.valdugeer.be/013/fr/Contact",
                "publisher": "Val du Geer ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; info@valdugeer.be / cv@valdugeer.be; TVA BE{KBO}; "
                    "ETA Bassenge packaging/textile/wood adapted work"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_val_du_geer_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet/turnover YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet DROP {OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_val_du_geer_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; ~{RATIO}x omzet",
            },
            {
                "budget_id": "bud_val_du_geer_pnl_jr2025_statutory",
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
                "budget_id": "bud_val_du_geer_equity_jr2025_statutory",
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
                "budget_id": "bud_val_du_geer_fte_jr2025_statutory",
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
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Val du Geer YE2025 leftover dual "
                    f"(omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Bassenge / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Val du Geer (KBO {KBO}; Actief; 4 VE; NACE 88.993; Bassenge)",
                "decision_date": "2026-06-09",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_omzet":{OMZET24},'
                    f'"2024_bruto":{BRUTO24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24},'
                    f'"2024_fte":{FTE24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}",
                "stated_goal": "Walloon ETA packaging / textile / wood Bassenge",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; disclose AVIQ ETA matrix; "
                    f"reconcile pnl DROP {PNL_PCT}%"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Liege>Bassenge>ValDuGeer>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; bruto {BRUTO} ~{RATIO}x; "
                    f"pnl DROP {PNL}; FTE {FTE}; 4 VE; after Nekto@2257; AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
                    f"Val du Geer omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Liege>Bassenge>ValDuGeer>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} / 4 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Bassenge / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA packaging / textile / wood",
                "measured_outcome": (
                    f"omzet DROP {OMZET_PCT}%; bruto JUMP +{BRUTO_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 09.06.2026"
                ),
                "absurdity_score": "6.8",
                "cost_score": "5.2",
                "difficulty": "3.0",
                "priority_index": "6.00",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    f"reconcile pnl DROP {PNL_PCT}%"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Nekto@2257; deferred FREE Les Erables"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Val du Geer VZW (Bassenge / ETA maatwerk Luik BE)",
                "name_fr": "Val du Geer ASBL (Bassenge / entreprise de travail adapté Liège BE)",
                "name_en": "Val du Geer adapted-work ASBL (Bassenge Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://www.valdugeer.be/",
                "foi_email": "info@valdugeer.be",
                "foi_postal": "Rue de la Cerisaie 8, 4690 Bassenge",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 4 VE NACE 88.993; "
                    f"omzet DROP {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 09.06.2026; assets/debt Unknown; "
                    f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "after Nekto@2257; not TE-additive of 348bn"
                ),
            }
        ],
    )

    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": "Wallonie>Liege>Bassenge>ValDuGeer>NBB_PDF_assets_debt_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); "
                    f"omzet EUR{OMZET}; bruto EUR{BRUTO} (~{RATIO}x); "
                    f"pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix / 4 VE split"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (omzet 10.75m / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Val du Geer ASBL",
                "recipient_email": "info@valdugeer.be",
                "recipient_postal": "Rue de la Cerisaie 8, 4690 Bassenge",
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
                    "AGB Bornem JR2024; after Nekto@2257; next EVERY-10 2260"
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
