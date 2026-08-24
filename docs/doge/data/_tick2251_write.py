# tick 2251 — Les Dauphins Gembloux YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"

csv.field_size_limit(10_000_000)

TICK = 2251
UTC = "2026-08-27T04:55:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_les_dauphins_gembloux"
KBO = "0429.051.883"
KBO_BARE = "0429051883"
SRC_EN = "src_dauphins_gembloux_jr2025_cw_en"
GAP = "gap_dauphins_gembloux_nbb_pdf_assets_debt_pnl_loss_flip_eta_matrix_l5"
COMM = "comm_dauphins_gembloux_jr2025_statutory_eta_omzet_pnl_loss_flip"
LB = "lb_dauphins_gembloux_omzet_3_37m_pnl_loss_flip_jr2025"
RQ = "rq_2251"
RQ_NEXT = "rq_2252"

OMZET = 3370669
OMZET24 = 3329859
BRUTO = 4274364
BRUTO24 = 4103618
PNL = -44270
PNL24 = 25835
EQUITY = 3401876
EQUITY24 = 3458442
FTE = 110.1
RATIO = round(BRUTO / OMZET, 2)
OMZET_PCT = round((OMZET - OMZET24) / OMZET24 * 100, 2)
BRUTO_PCT = round((BRUTO - BRUTO24) / BRUTO24 * 100, 2)
EQUITY_PCT = round((EQUITY - EQUITY24) / EQUITY24 * 100, 2)


def append_csv(path: Path, rows: list[dict]):
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        existing = list(reader)
    ids = set()
    id_key = fieldnames[0]
    for r in existing:
        ids.add(r[id_key])
    new = [r for r in rows if r[id_key] not in ids]
    if not new:
        print(f"skip append {path.name} (already present)")
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
                "leftover dual — Les Dauphins Gembloux YE2025 Medium "
                "(omzet 3.37m / pnl LOSS FLIP / bruto~1.27x / FTE 110.1)"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Les Dauphins ASBL Gembloux {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet JUMP {OMZET} (+{OMZET_PCT}% vs {OMZET24}); bruto JUMP {BRUTO} (~{RATIO}x); "
                f"pnl LOSS FLIP {PNL} vs YE2024 {PNL24}; equity DROP {EQUITY} ({EQUITY_PCT}%); "
                f"FTE {FTE}; 2 VE; NACE 88.993; neerlegging 02.07.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024 / "
                f"Heropbeuring CW opaque / Dauphins Visé N/A; after Saupont@2250; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Les Dauphins Gembloux YE2025 FREE Walloon ETA after Saupont; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found, "rq_2251 missing"

    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Les Dauphins — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Les Dauphins Gembloux YE2025 Medium "
                    f"(omzet 3.37m / pnl LOSS FLIP / FTE 110.1). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (skip Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/"
                    "Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Dauphins Visé still CW N/A). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Dauphins Gembloux; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; Dauphins Visé N/A; next every-10 2260"
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
                f"tick{TICK} leftover Dauphins Gembloux {KBO} Medium (omzet JUMP {OMZET}; "
                f"pnl LOSS FLIP {PNL}; equity DROP {EQUITY}; bruto {BRUTO} ~{RATIO}x; FTE {FTE}; 2 VE ETA); "
                f"after Saupont@2250; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
                f"Dauphins Visé N/A; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Les Dauphins Gembloux (NBB PDF / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Dauphins ASBL — KBO **{KBO}** (Actief; Rue des Praules 13, 5030 Gembloux; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Gembloux)  
**recipient:** secretariat@lesdauphins.be · Rue des Praules 13, 5030 Gembloux  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/les-dauphins) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/les-dauphins) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/les-dauphins) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://www.lesdauphins.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL Les Dauphins; **2 VE**; zetel Gembloux; NACE **88.993**.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** LOSS FLIP vs YE2024 profit EUR{PNL24:,}; equity **EUR{EQUITY:,}** DROP {EQUITY_PCT}%; FTE **{FTE}**; filed **02.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Dauphins Visé CW N/A. After Saupont@2250.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Les Dauphins ASBL
via secretariat@lesdauphins.be
Rue des Praules 13, 5030 Gembloux
Objet: Publicité des comptes annuels 2025 Les Dauphins (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24} — réconciliation avec FTE {FTE}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts bois / palettes / conditionnement / espaces verts.

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

## Tick {TICK} - {UTC} - rq_2251 Les Dauphins Gembloux (omzet 3.37m / pnl LOSS FLIP / bruto~{RATIO}x / FTE {FTE} / Medium)

- Unit: **rq_2251** leftover dual after **rq_2250 Le Saupont**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Dauphins Visé still **CW N/A**. Took named FREE Walloon ETA **Les Dauphins ASBL** YE2025 (KBO **{KBO}**; Rue des Praules 13 Gembloux; **Actief** **2 VE**; NACE **88.993** AViQ). Do not redo Saupont/Serviplast/Jean Del'Cour/TRAVCO/Pilifs stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET24}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** LOSS FLIP vs YE2024 profit EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_PCT}%; FTE **{FTE}**; neerlegging **02.07.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via secretariat@lesdauphins.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 5.90); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2251=done + rq_2252 open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2251/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2252 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log appended")


def main():
    sources = [
        {
            "source_id": "src_dauphins_gembloux_jr2025_cw_nl",
            "title": "Companyweb NL Les Dauphins Gembloux YE2025 statutory",
            "url": f"https://www.companyweb.be/nl/{KBO_BARE}/les-dauphins",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; YE2025 omzet JUMP {OMZET} pnl LOSS FLIP {PNL} equity DROP {EQUITY} "
                f"bruto {BRUTO} FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; "
                f"raw docs/doge/data/raw/tick2251/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Les Dauphins Gembloux YE2025 statutory",
            "url": f"https://www.companyweb.be/en/{KBO_BARE}/les-dauphins",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; "
                f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
            ),
        },
        {
            "source_id": "src_dauphins_gembloux_jr2025_cw_fr",
            "title": "Companyweb FR Les Dauphins Gembloux YE2025 statutory",
            "url": f"https://www.companyweb.be/fr/{KBO_BARE}/les-dauphins",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": DATE,
            "source_class": "secondary_aggregator",
            "notes": (
                f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Perte {PNL}"
            ),
        },
        {
            "source_id": f"src_dauphins_gembloux_kbo_{TICK}",
            "title": f"KBO Les Dauphins {KBO} Actief Gembloux 2 VE",
            "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
            "publisher": "KBO FOD Economie",
            "accessed_date": DATE,
            "source_class": "official_register",
            "notes": (
                f"tick{TICK}; Actief VZW/ASBL LES DAUPHINS; zetel Rue des Praules 13 5030 Gembloux; "
                f"2 VE; NACE 88.993; begindatum 01.07.1986; KBO email empty"
            ),
        },
        {
            "source_id": f"src_dauphins_gembloux_site_contact_{TICK}",
            "title": "Les Dauphins FOI channel secretariat@lesdauphins.be",
            "url": "https://www.lesdauphins.be/",
            "publisher": "Les Dauphins ASBL",
            "accessed_date": DATE,
            "source_class": "foi_contact",
            "notes": (
                f"tick{TICK}; secretariat@lesdauphins.be / jdessy@lesdauphins.be; "
                "Rue des Praules 13 5030 Gembloux; also leseta.be annuaire"
            ),
        },
    ]
    append_csv(DATA / "sources.csv", sources)

    budgets = [
        {
            "budget_id": "bud_dauphins_gembloux_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_dauphins_gembloux_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; bruto≫omzet ~{RATIO}x",
        },
        {
            "budget_id": "bud_dauphins_gembloux_pnl_jr2025_statutory",
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
            "budget_id": "bud_dauphins_gembloux_equity_jr2025_statutory",
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
            "budget_id": "bud_dauphins_gembloux_fte_jr2025_statutory",
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
            "budget_id": "bud_dauphins_gembloux_omzet_jr2024_statutory_cmp",
            "entity_id": ENTITY,
            "year": "2024",
            "amount_eur": str(OMZET24),
            "amount_min_eur": str(OMZET24),
            "amount_max_eur": str(OMZET24),
            "basis": "CW statutory omzet YE2024 comparative",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; YE2024 omzet {OMZET24} comparative (pre JUMP)",
        },
    ]
    append_csv(DATA / "budgets.csv", budgets)

    commitments = [
        {
            "commitment_id": COMM,
            "title": (
                "Les Dauphins Gembloux YE2025 leftover dual "
                "(omzet 3.37m / pnl LOSS FLIP / bruto~1.27x / FTE 110.1 / Medium)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "ETA workers Gembloux / AVIQ adapted-work public path",
            "legal_basis": f"ASBL ETA Les Dauphins (KBO {KBO}; Actief; 2 VE; NACE 88.993; Gembloux)",
            "decision_date": "2026-07-02",
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
            "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/les-dauphins",
            "stated_goal": "Walloon ETA wood / pallets / packaging / green spaces",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; reconcile pnl LOSS FLIP vs AVIQ ETA subsidy matrix; "
                f"explain bruto≫omzet ~{RATIO}x"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Wallonie>Namur>Gembloux>LesDauphins>JR2025_statutory_L5",
            "notes": (
                f"tick{TICK}; Medium CW; omzet primary envelope {OMZET}; pnl LOSS FLIP {PNL}; "
                f"FTE {FTE}; 2 VE; after Saupont@2250; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        }
    ]
    append_csv(DATA / "commitments.csv", commitments)

    leaderboard = [
        {
            "item_id": LB,
            "name": "Les Dauphins Gembloux omzet 3.37m / pnl LOSS FLIP / FTE 110.1 (YE2025 Walloon ETA)",
            "level": "L5",
            "type": "eta_asbl_statutory",
            "hierarchy_path": "Wallonie>Namur>Gembloux>LesDauphins>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                f"CW omzet {OMZET} / bruto {BRUTO} (~{RATIO}x) / pnl LOSS FLIP {PNL} / "
                f"equity DROP {EQUITY} / FTE {FTE} / 2 VE Walloon ETA"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "ETA workers Gembloux / AVIQ adapted-work public path",
            "stated_goal": "Walloon ETA wood / pallets / packaging / green spaces",
            "measured_outcome": (
                f"omzet JUMP +{OMZET_PCT}%; pnl LOSS FLIP {PNL}; equity DROP {EQUITY_PCT}%; "
                f"FTE {FTE}; filed 02.07.2026"
            ),
            "absurdity_score": "7.0",
            "cost_score": "4.6",
            "difficulty": "3.0",
            "priority_index": "5.90",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                "reconcile pnl LOSS FLIP + bruto≫omzet"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; after Saupont@2250"
            ),
        }
    ]
    append_csv(DATA / "leaderboard.csv", leaderboard)

    entities = [
        {
            "entity_id": ENTITY,
            "name_nl": "Les Dauphins VZW (Gembloux / ETA maatwerk Namen)",
            "name_fr": "Les Dauphins ASBL (Gembloux / entreprise de travail adapté Namur)",
            "name_en": "Les Dauphins adapted-work ASBL (Gembloux Walloon ETA)",
            "level": "parastatal",
            "parent_id": "sec_wallonia",
            "community_language": "fr",
            "website": "https://www.lesdauphins.be/",
            "foi_email": "secretariat@lesdauphins.be",
            "foi_postal": "Rue des Praules 13, 5030 Gembloux",
            "notes": (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                f"omzet JUMP {OMZET} bruto {BRUTO} (~{RATIO}x) pnl LOSS FLIP {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; FOI {GAP}; preferred stalls "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Dauphins Visé N/A; "
                "after Saupont@2250; not TE-additive of 348bn"
            ),
        }
    ]
    append_csv(DATA / "entities.csv", entities)

    foi_rows = [
        {
            "gap_id": GAP,
            "hierarchy_path": "Wallonie>Namur>Gembloux>LesDauphins>NBB_PDF_assets_debt_pnl_loss_flip",
            "entity_id": ENTITY,
            "what_is_missing": (
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                f"bruto EUR{BRUTO} (~{RATIO}x); pnl LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24}; "
                f"FTE {FTE}; AVIQ ETA subsidy matrix"
            ),
            "why_it_matters": (
                f"Medium CW shows Walloon ETA ASBL (omzet 3.37m / pnl LOSS FLIP / FTE {FTE}) under AVIQ path; "
                "assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Les Dauphins ASBL",
            "recipient_email": "secretariat@lesdauphins.be",
            "recipient_postal": "Rue des Praules 13, 5030 Gembloux",
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
                "AGB Bornem JR2024; Heropbeuring CW opaque; after Saupont@2250; next EVERY-10 2260"
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
