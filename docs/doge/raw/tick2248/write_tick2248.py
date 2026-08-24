# tick2248 — leftover dual ATE Ensival YE2025 Medium (bruto 3.99m / bruto≫omzet ~2.47x / pnl JUMP +171% / FTE DROP)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_ate_ensival_verviers"
TICK = "2248"
UTC = "2026-08-27T04:10:00Z"
GAP = "gap_ate_ensival_nbb_pdf_assets_debt_bruto_gt_omzet_2_47x_pnl_jump_171pct_fte_drop_eta_matrix_l5"
COMM = "comm_ate_ensival_jr2025_statutory_eta_bruto_gt_omzet_pnl_jump_fte_drop"
LB = "lb_ate_ensival_bruto_3_99m_bruto_gt_omzet_2_47x_pnl_jump_171pct_fte_drop_jr2025"

OM25, OM24 = 1617935, 1581578
BR25, BR24 = 3989520, 4023245
PN25, PN24 = 351372, 129498
EQ25, EQ24 = 3905723, 3560301
FTE25, FTE24 = 83.0, 90.0
RATIO = round(BR25 / OM25, 2)  # ~2.47


def read_csv(name: str) -> tuple[list[str], list[dict]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def upsert(rows: list[dict], key: str, kid: str, new: dict) -> None:
    for i, r in enumerate(rows):
        if r.get(key) == kid:
            rows[i] = {**r, **new}
            return
    rows.append(new)


s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_ate_ensival_jr2025_cw_nl",
        "Companyweb NL ATE Ensival YE2025 statutory",
        "https://www.companyweb.be/nl/0407637451/ate-les-ateliers-d-ensival",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+2.3%); bruto {BR25} (~{RATIO}x) DROP -0.84%; "
            f"pnl JUMP {PN25} (+171.33%); equity JUMP {EQ25}; FTE DROP {FTE25}; filed 17-06-2026"
        ),
    ),
    (
        "src_ate_ensival_jr2025_cw_en",
        "Companyweb EN ATE Ensival YE2025 statutory",
        "https://www.companyweb.be/en/0407637451/ate-les-ateliers-d-ensival",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 17-06-2026"
        ),
    ),
    (
        "src_ate_ensival_jr2025_cw_fr",
        "Companyweb FR ATE Ensival YE2025 statutory",
        "https://www.companyweb.be/fr/0407637451/ate-les-ateliers-d-ensival",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}; Personnel {FTE25}",
    ),
    (
        "src_ate_ensival_kbo_2248",
        "KBO ATE Ensival 0407.637.451 Actief Verviers 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407637451&lang=nl",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2248; Actief VZW ATE-Les Ateliers d' Ensival; zetel Rue des Weines 65 4800 Verviers; "
            "1 VE; RSZ NACE 88.993; BTW metal/wood/packaging/furniture; Walloon ETA AViQ"
        ),
    ),
    (
        "src_ate_ensival_site_contact_2248",
        "ATE Ensival FOI channel info@ate-ensival.be",
        "https://www.ate-ensival.be/",
        "ATE Ensival ASBL",
        "foi_contact",
        "tick2248; info@ate-ensival.be; +32 87 30 72 90; Rue des Weines 65 4800 Verviers (Ensival)",
    ),
]:
    upsert(
        sources,
        "source_id",
        sid,
        {
            "source_id": sid,
            "title": title,
            "url": url,
            "publisher": publisher,
            "accessed_date": "2026-08-27",
            "source_class": sclass,
            "notes": notes,
        },
    )
write_csv("sources.csv", s_fields, sources)

e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "ATE Ensival VZW (Verviers / Walloon ETA onderaanneming)",
        "name_fr": "ATE-Les Ateliers d'Ensival ASBL (Verviers / entreprise de travail adapte)",
        "name_en": "ATE Ensival adapted-work ASBL (Verviers Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.ate-ensival.be/",
        "foi_email": "info@ate-ensival.be",
        "foi_postal": "Rue des Weines 65, 4800 Verviers",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.637.451 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25}; bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} "
            f"equity JUMP {EQ25} FTE DROP {FTE25}; neerlegging 17.06.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; Groupe FOES YE2024; after TRAVCO@2247; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_ate_ensival_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +2.3% vs YE2024 {OM24}",
    ),
    (
        "bud_ate_ensival_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto DROP -0.84% vs YE2024 {BR24}; ratio ~{RATIO}x omzet",
    ),
    (
        "bud_ate_ensival_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 JUMP +171%",
        f"tick{TICK}; Medium CW; pnl JUMP {PN25} vs YE2024 {PN24} (+171.33%)",
    ),
    (
        "bud_ate_ensival_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP {EQ25} vs YE2024 {EQ24} (+9.7%)",
    ),
    (
        "bud_ate_ensival_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 83.0",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_ate_ensival_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory pnl YE2024 comparative",
        f"tick{TICK}; YE2024 pnl {PN24} comparative (pre JUMP)",
    ),
]:
    upsert(
        budgets,
        "budget_id",
        bid,
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": year,
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_ate_ensival_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            f"ATE Ensival YE2025 leftover dual (bruto 3.99m / bruto≫omzet ~{RATIO}x / "
            "pnl JUMP +171% / FTE DROP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Verviers / Walloon AViQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA ATE-Les Ateliers d'Ensival (KBO 0407.637.451; Actief; 1 VE; NACE 88.993; AViQ)"
        ),
        "decision_date": "2026-06-17",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": (
            f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},'
            f'"2025_equity":{EQ25},"2025_fte":{FTE25},"2024_omzet":{OM24},'
            f'"2024_bruto":{BR24},"2024_pnl":{PN24},"2024_equity":{EQ24},'
            f'"2024_fte":{FTE24},"ratio_bruto_omzet":{RATIO}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0407637451/ate-les-ateliers-d-ensival",
        "stated_goal": "Walloon ETA industrial subcontracting / metal / wood / packaging / mattresses",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl JUMP +171% with FTE DROP"
        ),
        "source_id": "src_ate_ensival_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Verviers>ATE_Ensival>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl JUMP {PN25}; FTE DROP {FTE25}; 1 VE; after TRAVCO@2247"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.1, abs 7.6, diff 3 → pi ≈ 2.805+2.66+0.7 = 6.165 → 6.20
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"ATE Ensival bruto 3.99m / bruto≫omzet ~{RATIO}x / pnl JUMP +171% / FTE DROP "
            "(YE2025 Walloon ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Liege>Verviers>ATE_Ensival>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} (vs YE2024 {PN24}) / "
            f"equity JUMP {EQ25} / FTE DROP {FTE25} / 1 VE Walloon ETA"
        ),
        "confidence": "medium",
        "source_id": "src_ate_ensival_jr2025_cw_en",
        "beneficiaries": "ETA workers Verviers / Walloon AViQ adapted-work public path",
        "stated_goal": "Walloon ETA industrial subcontracting / metal / wood / packaging",
        "measured_outcome": (
            f"omzet JUMP +2.3%; bruto≫omzet ~{RATIO}x; pnl JUMP +171.33%; "
            f"equity JUMP +9.7%; FTE DROP {FTE24}->{FTE25}; filed 17.06.2026"
        ),
        "absurdity_score": "7.6",
        "cost_score": "5.1",
        "difficulty": "3.0",
        "priority_index": "6.20",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~{RATIO}x AViQ matrix; "
            "reconcile pnl JUMP +171% with FTE DROP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Groupe FOES YE2024; after TRAVCO@2247"
        ),
    },
)
write_csv("leaderboard.csv", lb_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Liege>Verviers>ATE_Ensival>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_jump_fte_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl JUMP EUR{PN25} vs YE2024 EUR{PN24} (+171.33%) "
            f"with FTE DROP {FTE24}->{FTE25}; AViQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL (bruto 3.99m / bruto≫omzet ~{RATIO}x / pnl JUMP "
            "+171% while FTE DROP) under AViQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "ATE-Les Ateliers d'Ensival ASBL",
        "recipient_email": "info@ate-ensival.be",
        "recipient_postal": "Rue des Weines 65, 4800 Verviers",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-27",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall "
            "FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
            "Groupe FOES YE2024; after TRAVCO@2247"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2248",
    {
        "task_id": "rq_2248",
        "title": (
            f"leftover dual — ATE Ensival YE2025 Medium (bruto 3.99m / bruto≫omzet ~{RATIO}x / "
            "pnl JUMP +171% / FTE DROP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after TRAVCO; named FREE ATE Ensival YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T03:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; ATE Ensival 0407.637.451 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl JUMP {PN25} equity JUMP {EQ25} FTE DROP {FTE25}; "
            "1 VE Walloon ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "Groupe FOES YE2024; after TRAVCO@2247; do NOT redo TRAVCO/Pilifs/Jeunes Jardiniers/"
            "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123; next rq_2249; "
            "next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2249",
    {
        "task_id": "rq_2249",
        "title": (
            "leftover dual after ATE Ensival — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after ATE Ensival YE2025 Medium (bruto 3.99m / bruto≫omzet ~{RATIO}x / "
            "pnl JUMP +171% / FTE DROP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
            "TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else "
            "unused ETA/VAPH/WZC/maatwerk (e.g. Etablissements Deneyer / other FREE YE2025 ETA; skip "
            "ATE Ensival/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/"
            "L'Atelier/Axedis/ETA123/Groupe FOES-if-YE2024). Do NOT redo ATE Ensival, TRAVCO, Pilifs, "
            "Jeunes Jardiniers, La Lumière, APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 "
            "Beauraing, Manufast, Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, "
            "Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, "
            "Reset, Den Azalee, Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} ATE Ensival; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; Groupe FOES YE2024; next every-10 2250"
        ),
    },
)
write_csv("research_queue.csv", rq_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
upsert(
    ls,
    "state_id",
    "main",
    {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2248",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover ATE Ensival 0407.637.451 Medium (bruto {BR25} ~{RATIO}x "
            f"omzet {OM25}; pnl JUMP {PN25}; equity JUMP {EQ25}; FTE DROP {FTE25}; "
            "1 VE Walloon ETA); after TRAVCO@2247; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; Groupe FOES YE2024; next rq_2249; next EVERY-10 2250; "
            "continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — ATE Ensival (NBB PDF / bruto≫omzet ~{RATIO}x / pnl JUMP +171% / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ATE-Les Ateliers d'Ensival ASBL — KBO **0407.637.451** (Actief; Rue des Weines 65, 4800 Verviers; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon ETA AViQ)  
**recipient:** info@ate-ensival.be · Rue des Weines 65, 4800 Verviers  
**sources:** [CW EN](https://www.companyweb.be/en/0407637451/ate-les-ateliers-d-ensival) · [CW NL](https://www.companyweb.be/nl/0407637451/ate-les-ateliers-d-ensival) · [CW FR](https://www.companyweb.be/fr/0407637451/ate-les-ateliers-d-ensival) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407637451&lang=nl) · [site](https://www.ate-ensival.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW ATE-Les Ateliers d' Ensival; **1 VE**; zetel Rue des Weines Verviers; RSZ NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +2.3% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP -0.84% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +171.33% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +9.7%; FTE **{FTE25}** DROP vs {FTE24}; filed **17.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Groupe FOES YE2024. After TRAVCO@2247.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ATE-Les Ateliers d'Ensival ASBL
via info@ate-ensival.be
Rue des Weines 65, 4800 Verviers
Objet: Publicité des comptes annuels 2025 ATE Ensival (BCE 0407.637.451)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (ratio ~{RATIO}x).
3. PnL JUMP EUR{PN25} (+171%) vs YE2024 EUR{PN24} avec FTE DROP {FTE24}->{FTE25} — réconciliation.
4. Matrice des subsides AViQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts ateliers (métal/bois/emballage/literie/espaces verts/mise à disposition).

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2248 ATE Ensival Verviers (bruto 3.99m / bruto≫omzet ~{RATIO}x / pnl JUMP +171% / FTE DROP / Medium)

- Unit: **rq_2248** leftover dual after **rq_2247 TRAVCO**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Groupe FOES still **YE2024**. Took named FREE Walloon ETA **ATE-Les Ateliers d'Ensival ASBL** YE2025 (KBO **0407.637.451**; Rue des Weines 65 Verviers; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +2.3% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -0.84% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +171.33% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +9.7%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **17.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@ate-ensival.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2248=done + rq_2249 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2248/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2249 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} pnl={PN25} ratio={RATIO} next=rq_2249")
