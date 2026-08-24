# tick2247 — leftover dual TRAVCO YE2025 Medium (bruto 3.57m / empty omzet / pnl PROFIT FLIP)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_travco_anderlecht"
TICK = "2247"
UTC = "2026-08-27T03:55:00Z"
GAP = "gap_travco_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_eta_matrix_l5"
COMM = "comm_travco_jr2025_statutory_eta_bruto_empty_omzet_pnl_profit_flip"
LB = "lb_travco_bruto_3_57m_empty_omzet_pnl_profit_flip_jr2025"

BR25, BR24 = 3570097, 3400776
PN25, PN24 = 22942, -314919
EQ25, EQ24 = 670527, 670230
FTE25, FTE24 = 125.1, 124.8


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
        "src_travco_jr2025_cw_nl",
        "Companyweb NL TRAVCO YE2025 statutory",
        "https://www.companyweb.be/nl/0428335073/travail-et-cooperation",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 empty omzet; bruto JUMP {BR25} (+4.98%) pnl PROFIT FLIP "
            f"{PN25} vs YE2024 loss {PN24} equity {EQ25} FTE JUMP {FTE25}; filed 15-07-2026"
        ),
    ),
    (
        "src_travco_jr2025_cw_en",
        "Companyweb EN TRAVCO YE2025 statutory",
        "https://www.companyweb.be/en/0428335073/travail-et-cooperation",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; empty Turnover; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 15-07-2026"
        ),
    ),
    (
        "src_travco_jr2025_cw_fr",
        "Companyweb FR TRAVCO YE2025 statutory",
        "https://www.companyweb.be/fr/0428335073/travail-et-cooperation",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA empty; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_travco_kbo_2247",
        "KBO TRAVCO 0428.335.073 Actief Anderlecht 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=428335073",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2247; Actief VZW/ASBL TRAVAIL ET COOPERATION / TRAVCO; zetel Fernand Demetskaai 28 "
            "1070 Anderlecht; 1 VE; NACE RSZ 88.993; Brussels ETA; ops Rue de la Technologie 109 Ganshoren"
        ),
    ),
    (
        "src_travco_site_contact_2247",
        "TRAVCO FOI channel info@travco.be",
        "https://www.travco.be/fr/contact",
        "TRAVCO ASBL",
        "foi_contact",
        "tick2247; info@travco.be; +32 2 522 57 99; Rue de la Technologie 109 1083 Ganshoren (siège Quai Fernand Demets 28 Anderlecht)",
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
        "name_nl": "TRAVCO VZW (Anderlecht-Ganshoren / Brussels ETA onderaanneming)",
        "name_fr": "TRAVCO ASBL (Anderlecht-Ganshoren / entreprise de travail adapté)",
        "name_en": "TRAVCO adapted-work ASBL (Anderlecht-Ganshoren Brussels ETA)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "fr",
        "website": "https://www.travco.be/",
        "foi_email": "info@travco.be",
        "foi_postal": "Quai Fernand Demets 28, 1070 Anderlecht (ops Rue de la Technologie 109, 1083 Ganshoren)",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0428.335.073 Actief 1 VE "
            f"NACE 88.993; empty omzet; bruto JUMP {BR25} pnl PROFIT FLIP {PN25} equity {EQ25} "
            f"FTE JUMP {FTE25}; neerlegging 15.07.2026; assets/debt Unknown; FOI {GAP}; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Pilifs@2246; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_travco_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; empty omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +4.98% vs YE2024 {BR24}; omzet unpublished",
    ),
    (
        "bud_travco_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 PROFIT FLIP",
        f"tick{TICK}; Medium CW; pnl PROFIT FLIP {PN25} vs YE2024 loss {PN24}",
    ),
    (
        "bud_travco_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity flat {EQ25} vs YE2024 {EQ24} (after prior DROP)",
    ),
    (
        "bud_travco_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 125.1",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_travco_fte_jr2024_statutory_cmp",
        "2024",
        FTE24,
        "CW social-balance FTE YE2024 comparative",
        f"tick{TICK}; YE2024 FTE {FTE24} comparative",
    ),
    (
        "bud_travco_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory pnl YE2024 comparative LOSS",
        f"tick{TICK}; YE2024 pnl LOSS {PN24} comparative (pre PROFIT FLIP)",
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
            "source_id": "src_travco_jr2025_cw_en",
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
            "TRAVCO YE2025 leftover dual (bruto 3.57m / empty omzet / pnl PROFIT FLIP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Brussels-Anderlecht/Ganshoren / PHARE-COCOF adapted-work public path",
        "legal_basis": (
            "ASBL ETA TRAVCO / Travail et Coopération (KBO 0428.335.073; Actief; 1 VE; NACE 88.993; Brussels)"
        ),
        "decision_date": "2026-07-15",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": (
            f'{{"2025_bruto":{BR25},"2025_omzet":null,"2025_pnl":{PN25},'
            f'"2025_equity":{EQ25},"2025_fte":{FTE25},"2024_bruto":{BR24},'
            f'"2024_pnl":{PN24},"2024_fte":{FTE24}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0428335073/travail-et-cooperation",
        "stated_goal": "Brussels ETA packaging / carton / pharma handling / mailing",
        "cut_option": (
            "Publish NBB PDF assets/debt/omzet FOI; explain empty omzet vs bruto 3.57m; "
            "reconcile pnl PROFIT FLIP from deep YE2024 loss"
        ),
        "source_id": "src_travco_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>Anderlecht>TRAVCO>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; empty omzet; "
            f"pnl PROFIT FLIP {PN25}; FTE JUMP {FTE25}; 1 VE; after Pilifs@2246"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.0, abs 7.5, diff 3 → pi = 2.75+2.625+0.7 = 6.075 → 6.10
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "TRAVCO bruto 3.57m / empty omzet / pnl PROFIT FLIP (YE2025 Brussels ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Bruxelles>Anderlecht>TRAVCO>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / empty omzet / pnl PROFIT FLIP {PN25} (vs YE2024 loss {PN24}) / "
            f"equity {EQ25} / FTE JUMP {FTE25} / 1 VE Brussels ETA"
        ),
        "confidence": "medium",
        "source_id": "src_travco_jr2025_cw_en",
        "beneficiaries": "ETA workers Brussels-Anderlecht/Ganshoren / PHARE-COCOF adapted-work public path",
        "stated_goal": "Brussels ETA packaging / carton / pharma handling",
        "measured_outcome": (
            f"empty omzet; bruto JUMP +4.98%; pnl PROFIT FLIP {PN25}; "
            f"equity flat {EQ25}; FTE JUMP {FTE25}; filed 15.07.2026"
        ),
        "absurdity_score": "7.5",
        "cost_score": "5.0",
        "difficulty": "3.0",
        "priority_index": "6.10",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/omzet FOI; disclose empty omzet vs bruto 3.57m; "
            "reconcile PROFIT FLIP from YE2024 deep loss"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Pilifs@2246"
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
            "Bruxelles>Anderlecht>TRAVCO>NBB_PDF_assets_debt_empty_omzet_pnl_profit_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/omzet); bruto EUR{BR25} "
            f"with empty published omzet; pnl PROFIT FLIP EUR{PN25} vs YE2024 loss EUR{PN24}; "
            f"PHARE ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            "Medium CW shows Brussels ETA ASBL (bruto 3.57m / empty omzet / pnl PROFIT FLIP "
            "from -315k) under PHARE path; assets/debt/omzet unpublished"
        ),
        "priority": "8",
        "recipient_body": "TRAVCO ASBL",
        "recipient_email": "info@travco.be",
        "recipient_postal": "Rue de la Technologie 109, 1083 Ganshoren (siège Quai Fernand Demets 28, 1070 Anderlecht)",
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
            "after Pilifs@2246"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2247",
    {
        "task_id": "rq_2247",
        "title": (
            "leftover dual — TRAVCO YE2025 Medium (bruto 3.57m / empty omzet / pnl PROFIT FLIP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Pilifs; named FREE TRAVCO YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T03:40:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; TRAVCO 0428.335.073 YE2025 Medium CW; bruto {BR25} empty omzet "
            f"pnl PROFIT FLIP {PN25} equity {EQ25} FTE JUMP {FTE25}; "
            "1 VE Brussels ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Pilifs@2246; do NOT redo Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/"
            "Le Perron/L'Atelier/Axedis/ETA123; next rq_2248; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2248",
    {
        "task_id": "rq_2248",
        "title": (
            "leftover dual after TRAVCO — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after TRAVCO YE2025 Medium (bruto 3.57m / empty omzet / pnl PROFIT FLIP). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
            "if YE2025, else Heropbeuring if NBB/CW euros live, else unused ETA/VAPH/WZC/maatwerk "
            "(e.g. Groupe FOES / Charles Lambert if YE2025 FREE; skip TRAVCO/Pilifs/Jeunes Jardiniers/"
            "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). Do NOT redo TRAVCO, Pilifs, "
            "Jeunes Jardiniers, La Lumière, APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 "
            "Beauraing, Manufast, Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, "
            "Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, "
            "Reset, Den Azalee, Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} TRAVCO; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2250"
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
        "last_unit_id": "rq_2247",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover TRAVCO 0428.335.073 Medium (bruto {BR25} empty omzet; "
            f"pnl PROFIT FLIP {PN25}; equity {EQ25}; FTE JUMP {FTE25}; 1 VE Brussels ETA); "
            "after Pilifs@2246; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "next rq_2248; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — TRAVCO (NBB PDF / empty omzet / pnl PROFIT FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** TRAVCO ASBL — KBO **0428.335.073** (Actief; Quai Fernand Demets 28, 1070 Anderlecht / ops Rue de la Technologie 109, 1083 Ganshoren; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Brussels ETA PHARE/COCOF)  
**recipient:** info@travco.be · Rue de la Technologie 109, 1083 Ganshoren  
**sources:** [CW EN](https://www.companyweb.be/en/0428335073/travail-et-cooperation) · [CW NL](https://www.companyweb.be/nl/0428335073/travail-et-cooperation) · [CW FR](https://www.companyweb.be/fr/0428335073/travail-et-cooperation) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=428335073) · [site](https://www.travco.be/fr/contact)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt/omzet Unknown)

## Context
- KBO Strong: Actief VZW/ASBL TRAVAIL ET COOPERATION; **1 VE**; zetel Fernand Demetskaai Anderlecht; NACE **88.993**.
- CW YE2025: omzet **unpublished**; bruto **EUR{BR25:,}** JUMP +4.98% vs YE2024 EUR{BR24:,}; pnl **EUR{PN25:,}** PROFIT FLIP vs YE2024 loss EUR{PN24:,}; equity **EUR{EQ25:,}** flat; FTE **{FTE25}** JUMP vs {FTE24}; filed **15.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Pilifs@2246.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: TRAVCO ASBL
via info@travco.be
Rue de la Technologie 109, 1083 Ganshoren
Objet: Publicité des comptes annuels 2025 TRAVCO (BCE 0428.335.073)

Madame, Monsieur,

Sur la base de l'ordonnance bruxelloise relative à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash/omzet).
2. Composition marge brute EUR{BR25} et chiffre d'affaires (non publié sur Companyweb).
3. PnL PROFIT FLIP EUR{PN25} vs YE2024 perte EUR{PN24} — réconciliation.
4. Matrice des subsides PHARE/COCOF / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts Anderlecht / Ganshoren / pharma / carton / mailing.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2247 TRAVCO Anderlecht (bruto 3.57m / empty omzet / pnl PROFIT FLIP / Medium)

- Unit: **rq_2247** leftover dual after **rq_2246 Pilifs**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE Brussels ETA **TRAVCO ASBL** YE2025 (KBO **0428.335.073**; Quai Fernand Demets 28 Anderlecht / Rue de la Technologie 109 Ganshoren; **Actief** **1 VE**; NACE **88.993** PHARE/COCOF). Do not redo Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **unpublished**; bruto **EUR{BR25}** JUMP +4.98% vs YE2024 EUR{BR24}; pnl **EUR{PN25}** PROFIT FLIP vs YE2024 loss EUR{PN24}; equity **EUR{EQ25}** flat; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **15.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@travco.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.10); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2247=done + rq_2248 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2247/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2248 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} pnl={PN25} next=rq_2248")
