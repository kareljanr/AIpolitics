# tick 2253 — Atelier Les Gaillettes Herve/Battice YE2025 Medium
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

TICK = 2253
UTC = "2026-08-27T05:25:00Z"
DATE = "2026-08-27"
ENTITY = "vzw_gaillettes_herve"
KBO = "0408.044.059"
KBO_BARE = "0408044059"
SRC_EN = "src_gaillettes_jr2025_cw_en"
GAP = "gap_gaillettes_nbb_pdf_assets_debt_bruto_gt_omzet_2_03x_pnl_drop_82pct_eta_matrix_l5"
COMM = "comm_gaillettes_jr2025_statutory_eta_bruto_gt_omzet_pnl_drop_82pct"
LB = "lb_gaillettes_bruto_8_02m_2_03x_pnl_drop_82pct_jr2025"
RQ = "rq_2253"
RQ_NEXT = "rq_2254"

OMZET = 3942482
OMZET24 = 3947106
BRUTO = 8020283
BRUTO24 = 7697385
PNL = 365574
PNL24 = 2033921
EQUITY = 5742782
EQUITY24 = 5389484
FTE = 222.9
RATIO = round(BRUTO / OMZET, 2)
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
                "leftover dual — Les Gaillettes YE2025 Medium "
                f"(bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE})"
            )
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK}; Gaillettes ASBL Herve/Battice {KBO} YE2025 Medium CW NL+EN+FR + Strong KBO; "
                f"omzet flat {OMZET} ({OMZET_PCT}%); bruto JUMP {BRUTO} (~{RATIO}x / +{BRUTO_PCT}%); "
                f"pnl DROP {PNL} ({PNL_PCT}% vs YE2024 {PNL24}); equity JUMP {EQUITY} (+{EQUITY_PCT}%); "
                f"FTE {FTE}; 2 VE; NACE 88.993; neerlegging 07.08.2026; assets/debt Unknown; "
                f"FOI {GAP} ready NOT sent; stalls AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                f"after Hunelle@2252; next EVERY-10 2260"
            )
            r["instructions"] = (
                "leftover dual Les Gaillettes YE2025 FREE Walloon ETA after Hunelle; "
                "preferred AGB/FARO/AIESH/REW still YE2024"
            )
    assert found
    if not any(r["task_id"] == RQ_NEXT for r in rows):
        rows.append(
            {
                "task_id": RQ_NEXT,
                "title": (
                    "leftover dual after Gaillettes — prefer AGB/FARO-YE2025/AIESH-REW/"
                    "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "leftover dual after Les Gaillettes YE2025 Medium "
                    f"(bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE}). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, "
                    "else unused ETA/VAPH/WZC/maatwerk (e.g. Relais Haute Sambre if YE2025 FREE; "
                    "skip Gaillettes/Hunelle/Dauphins Gembloux/Saupont/Serviplast/Jean Del'Cour/"
                    "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/"
                    "ETA 123 Beauraing/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers de Tertre/Le Rucher/"
                    "Het Rekreatief/Travie/SDB/De Vleugels/Kiemkracht/De Oever/ViTeS*/Kringwinkel*/Manus*/Reset/"
                    "Den Azalee/Kemphaan/Mirto/Blankedale/Werkmmaat; Dauphins Visé CW N/A; Sipres/APN still YE2024). "
                    "Do NOT redo IPFBW/Aquiris/SPGE/IRE*/FANC/SCK CEN/EURIDICE/Hydria/Vivaqua/Belgoprocess/"
                    "Laborelec/CILE/NIRAS/Bel V/Dijk92/Synergrid/AIEG/Synatom/Atrias/RESA/Enodia/Fluxys*/ETB/"
                    "Elia/BNO/SWDE/BRUGEL/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Senes. "
                    "Next EVERY-10: 2260."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Gaillettes; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
                    "Heropbeuring CW opaque; deferred FREE Relais Haute Sambre; next every-10 2260"
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
                f"tick{TICK} leftover Gaillettes {KBO} Medium (bruto JUMP {BRUTO} ~{RATIO}x; "
                f"omzet flat {OMZET}; pnl DROP {PNL} {PNL_PCT}%; equity JUMP {EQUITY}; FTE {FTE}; 2 VE ETA Herve); "
                f"after Hunelle@2252; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
                f"deferred FREE Relais Haute Sambre; next {RQ_NEXT}; next EVERY-10 2260; continuous hole_fill"
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
        f"""# FOI draft — Les Gaillettes (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP {PNL_PCT}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Atelier Les Gaillettes ASBL — KBO **{KBO}** (Actief; Rue de Maestricht 43, 4651 Herve; **2 VE**; FTE {FTE} CW; NACE **88.993**; Walloon ETA Battice/Barchon)  
**recipient:** secretariat@lesgaillettes.be · commercial@lesgaillettes.be · Rue de Maestricht 43, 4651 Herve  
**sources:** [CW EN](https://www.companyweb.be/en/{KBO_BARE}/atelier-les-gaillettes-asbl) · [CW NL](https://www.companyweb.be/nl/{KBO_BARE}/atelier-les-gaillettes-asbl) · [CW FR](https://www.companyweb.be/fr/{KBO_BARE}/atelier-les-gaillettes-asbl) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}) · [site](https://lesgaillettes.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL ATELIER LES GAILLETTES ASBL; **2 VE**; zetel Herve/Battice; NACE **88.993** (+88.995).
- CW YE2025: omzet **EUR{OMZET:,}** flat ({OMZET_PCT}% vs YE2024 EUR{OMZET24:,}); bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; filed **07.08.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Hunelle@2252.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Atelier Les Gaillettes ASBL
via secretariat@lesgaillettes.be
Rue de Maestricht 43, 4651 Herve
Objet: Publicité des comptes annuels 2025 Les Gaillettes (BCE {KBO})

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OMZET} / marge brute EUR{BRUTO} (~{RATIO}x).
3. PnL DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}) — réconciliation avec FTE {FTE}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts menuiserie / conditionnement / mise à disposition / sites Battice-Barchon-Retinne.

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

## Tick {TICK} - {UTC} - rq_2253 Les Gaillettes Herve (bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)

- Unit: **rq_2253** leftover dual after **rq_2252 Hunelle**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Sipres/APN still **YE2024**. Took named FREE Walloon ETA **Atelier Les Gaillettes ASBL** YE2025 (KBO **{KBO}**; Rue de Maestricht 43 Herve/Battice; **Actief** **2 VE**; NACE **88.993** AViQ). Deferred FREE Relais Haute Sambre. Do not redo Hunelle/Dauphins/Saupont/Serviplast stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** flat ({OMZET_PCT}% vs YE2024 EUR{OMZET24}); bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{RATIO}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL24}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}**; neerlegging **07.08.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via secretariat@lesgaillettes.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2253=done + rq_2254 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2253/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2250**; next **2260**). Next: rq_2254 (AGB/FARO-if-YE2025 / AIESH-REW / unused Relais Haute Sambre).
"""
        )
    print("loop_log appended")


def main():
    append_csv(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_gaillettes_jr2025_cw_nl",
                "title": "Companyweb NL Les Gaillettes YE2025 statutory",
                "url": f"https://www.companyweb.be/nl/{KBO_BARE}/atelier-les-gaillettes-asbl",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; YE2025 omzet flat {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                    f"bruto {BRUTO} FTE {FTE}; neerlegging 07.08.2026; assets/debt Unknown; "
                    f"raw docs/doge/data/raw/tick2253/"
                ),
            },
            {
                "source_id": SRC_EN,
                "title": "Companyweb EN Les Gaillettes YE2025 statutory",
                "url": f"https://www.companyweb.be/en/{KBO_BARE}/atelier-les-gaillettes-asbl",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; EN mirror YE2025 Medium; filed 07-08-2026; Last balance sheet year 2025; "
                    f"Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_gaillettes_jr2025_cw_fr",
                "title": "Companyweb FR Les Gaillettes YE2025 statutory",
                "url": f"https://www.companyweb.be/fr/{KBO_BARE}/atelier-les-gaillettes-asbl",
                "publisher": "Companyweb (NBB-derived)",
                "accessed_date": DATE,
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR mirror; CA {OMZET}; Marge brute {BRUTO}; Bénéfice {PNL}",
            },
            {
                "source_id": f"src_gaillettes_kbo_{TICK}",
                "title": f"KBO Les Gaillettes {KBO} Actief Herve 2 VE",
                "url": f"https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer={KBO_BARE}",
                "publisher": "KBO FOD Economie",
                "accessed_date": DATE,
                "source_class": "official_register",
                "notes": (
                    f"tick{TICK}; Actief VZW/ASBL ATELIER LES GAILLETTES ASBL; zetel Rue de Maestricht 43 4651 Herve; "
                    f"2 VE; NACE 88.993/88.995; begindatum 08.12.1970; DG Delbrassine since 30.06.2025; KBO email empty"
                ),
            },
            {
                "source_id": f"src_gaillettes_site_contact_{TICK}",
                "title": "Les Gaillettes FOI channel secretariat@lesgaillettes.be",
                "url": "https://lesgaillettes.be/",
                "publisher": "Atelier Les Gaillettes ASBL",
                "accessed_date": DATE,
                "source_class": "foi_contact",
                "notes": (
                    f"tick{TICK}; secretariat@lesgaillettes.be / commercial@lesgaillettes.be; "
                    "Rue de Maestricht 43 4651 Herve (Battice); also leseta.be annuaire"
                ),
            },
        ],
    )

    append_csv(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_gaillettes_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW statutory bruto_marge YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; bruto JUMP +{BRUTO_PCT}%; bruto≫omzet ~{RATIO}x (primary envelope)",
            },
            {
                "budget_id": "bud_gaillettes_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW statutory omzet YE2025",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; Medium CW; omzet flat {OMZET_PCT}% vs YE2024 {OMZET24}",
            },
            {
                "budget_id": "bud_gaillettes_pnl_jr2025_statutory",
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
                "budget_id": "bud_gaillettes_equity_jr2025_statutory",
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
                "budget_id": "bud_gaillettes_fte_jr2025_statutory",
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
                "budget_id": "bud_gaillettes_pnl_jr2024_statutory_cmp",
                "entity_id": ENTITY,
                "year": "2024",
                "amount_eur": str(PNL24),
                "amount_min_eur": str(PNL24),
                "amount_max_eur": str(PNL24),
                "basis": "CW statutory winst YE2024 comparative",
                "source_id": SRC_EN,
                "confidence": "medium",
                "notes": f"tick{TICK}; YE2024 pnl {PNL24} comparative (pre DROP -82%)",
            },
        ],
    )

    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Les Gaillettes YE2025 leftover dual "
                    f"(bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} / Medium)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "ETA workers Herve-Battice / AVIQ adapted-work public path",
                "legal_basis": f"ASBL ETA Atelier Les Gaillettes (KBO {KBO}; Actief; 2 VE; NACE 88.993; Herve)",
                "decision_date": "2026-08-07",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(BRUTO),
                "cash_by_year": (
                    f'{{"2025_bruto":{BRUTO},"2025_omzet":{OMZET},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE},"2024_bruto":{BRUTO24},'
                    f'"2024_omzet":{OMZET24},"2024_pnl":{PNL24},"2024_equity":{EQUITY24}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_BARE}/atelier-les-gaillettes-asbl",
                "stated_goal": "Walloon ETA joinery / packaging / personnel secondment",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; reconcile pnl DROP -82% vs AVIQ ETA subsidy matrix; "
                    f"explain bruto≫omzet ~{RATIO}x; Retinne consolidation path"
                ),
                "source_id": SRC_EN,
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Liege>Herve>Gaillettes>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; bruto primary envelope {BRUTO} ~{RATIO}x; pnl DROP {PNL}; "
                    f"FTE {FTE}; 2 VE; after Hunelle@2252; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    f"Les Gaillettes bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE} "
                    "(YE2025 Walloon ETA)"
                ),
                "level": "L5",
                "type": "eta_asbl_statutory",
                "hierarchy_path": "Wallonie>Liege>Herve>Gaillettes>JR2025",
                "annual_cost_eur": str(BRUTO),
                "total_cost_eur": str(BRUTO),
                "tco_notes": (
                    f"CW bruto {BRUTO} (~{RATIO}x omzet {OMZET}) / pnl DROP {PNL} ({PNL_PCT}%) / "
                    f"equity JUMP {EQUITY} / FTE {FTE} / 2 VE Walloon ETA"
                ),
                "confidence": "medium",
                "source_id": SRC_EN,
                "beneficiaries": "ETA workers Herve-Battice / AVIQ adapted-work public path",
                "stated_goal": "Walloon ETA joinery / packaging / personnel secondment",
                "measured_outcome": (
                    f"bruto JUMP +{BRUTO_PCT}%; omzet flat {OMZET_PCT}%; pnl DROP {PNL_PCT}%; "
                    f"equity JUMP +{EQUITY_PCT}%; FTE {FTE}; filed 07.08.2026"
                ),
                "absurdity_score": "7.4",
                "cost_score": "5.0",
                "difficulty": "3.0",
                "priority_index": "6.20",
                "cut_proposal": (
                    "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
                    "reconcile pnl DROP -82% + bruto≫omzet; Retinne site consolidation"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
                    "FARO/AIESH/REW YE2024; after Hunelle@2252"
                ),
            }
        ],
    )

    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": "Atelier Les Gaillettes VZW (Herve-Battice / ETA maatwerk Luik)",
                "name_fr": "Atelier Les Gaillettes ASBL (Herve-Battice / entreprise de travail adapté Liège)",
                "name_en": "Atelier Les Gaillettes adapted-work ASBL (Herve Walloon ETA)",
                "level": "parastatal",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
                "website": "https://lesgaillettes.be/",
                "foi_email": "secretariat@lesgaillettes.be",
                "foi_postal": "Rue de Maestricht 43, 4651 Herve",
                "notes": (
                    f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief 2 VE NACE 88.993; "
                    f"omzet flat {OMZET} bruto JUMP {BRUTO} (~{RATIO}x) pnl DROP {PNL} ({PNL_PCT}%) "
                    f"equity JUMP {EQUITY} FTE {FTE}; neerlegging 07.08.2026; assets/debt Unknown; FOI {GAP}; "
                    "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Hunelle@2252; "
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
                "hierarchy_path": "Wallonie>Liege>Herve>Gaillettes>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop",
                "entity_id": ENTITY,
                "what_is_missing": (
                    f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OMZET} / "
                    f"bruto EUR{BRUTO} (~{RATIO}x); pnl DROP EUR{PNL} ({PNL_PCT}% vs YE2024 EUR{PNL24}); "
                    f"FTE {FTE}; AVIQ ETA subsidy matrix; Retinne consolidation"
                ),
                "why_it_matters": (
                    f"Medium CW shows Walloon ETA ASBL (bruto 8.02m / ~{RATIO}x / pnl DROP {PNL_PCT}% / FTE {FTE}) "
                    "under AVIQ path; assets/debt unpublished"
                ),
                "priority": "8",
                "recipient_body": "Atelier Les Gaillettes ASBL",
                "recipient_email": "secretariat@lesgaillettes.be",
                "recipient_postal": "Rue de Maestricht 43, 4651 Herve",
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
                    "AGB Bornem JR2024; after Hunelle@2252; next EVERY-10 2260"
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
