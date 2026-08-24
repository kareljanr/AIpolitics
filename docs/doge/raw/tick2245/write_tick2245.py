# tick2245 — leftover dual Les Jeunes Jardiniers YE2025 Medium (bruto 4.78m / ~1.97x / pnl LOSS FLIP / equity DROP -52%)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_jeunes_jardiniers_uccle"
TICK = "2245"
UTC = "2026-08-27T03:25:00Z"
GAP = "gap_jeunes_jardiniers_nbb_pdf_assets_debt_bruto_gt_omzet_1_97x_pnl_loss_flip_equity_drop_eta_matrix_l5"
COMM = "comm_jeunes_jardiniers_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_flip_equity_drop"
LB = "lb_jeunes_jardiniers_bruto_4_78m_gt_omzet_1_97x_pnl_loss_flip_equity_drop_jr2025"

OM25, OM24 = 2426594, 2082684
BR25, BR24 = 4781722, 4720786
PN25, PN24 = -157194, 49819
EQ25, EQ24 = 136133, 285294
FTE25, FTE24 = 140.5, 139.7
RATIO = round(BR25 / OM25, 2)  # ~1.97


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
        "src_jeunes_jardiniers_jr2025_cw_nl",
        "Companyweb NL Les Jeunes Jardiniers YE2025 statutory",
        "https://www.companyweb.be/nl/0414842571/les-jeunes-jardiniers",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+16.51%) bruto JUMP {BR25} (+1.29% "
            f"bruto≫omzet ~{RATIO}x) pnl LOSS FLIP {PN25} vs YE2024 profit {PN24} "
            f"equity DROP {EQ25} (-52.28%) FTE JUMP {FTE25}; filed 27-07-2026"
        ),
    ),
    (
        "src_jeunes_jardiniers_jr2025_cw_en",
        "Companyweb EN Les Jeunes Jardiniers YE2025 statutory",
        "https://www.companyweb.be/en/0414842571/les-jeunes-jardiniers",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 27-07-2026"
        ),
    ),
    (
        "src_jeunes_jardiniers_jr2025_cw_fr",
        "Companyweb FR Les Jeunes Jardiniers YE2025 statutory",
        "https://www.companyweb.be/fr/0414842571/les-jeunes-jardiniers",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_jeunes_jardiniers_kbo_2245",
        "KBO Les Jeunes Jardiniers 0414.842.571 Actief Uccle 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=414842571",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2245; Actief VZW/ASBL Les Jeunes Jardiniers; zetel Chaussée d'Alsemberg 1393 "
            "1180 Uccle; 1 VE; NACE RSZ 88.993; Brussels ETA (COCOF/PHARE); info@lesjeunesjardiniers.be"
        ),
    ),
    (
        "src_jeunes_jardiniers_site_contact_2245",
        "Les Jeunes Jardiniers FOI channel info@lesjeunesjardiniers.be",
        "https://lesjeunesjardiniers.be/contact/",
        "Les Jeunes Jardiniers ASBL",
        "foi_contact",
        "tick2245; info@lesjeunesjardiniers.be; compta@lesjeunesjardiniers.be; +32 2 332 15 30; Chaussée d'Alsemberg 1393 1180 Uccle",
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
        "name_nl": "Les Jeunes Jardiniers VZW (Ukkel / Brussels ETA tuinaanleg)",
        "name_fr": "Les Jeunes Jardiniers ASBL (Uccle / entreprise de travail adapté jardins)",
        "name_en": "Les Jeunes Jardiniers adapted-work ASBL (Uccle Brussels ETA gardens)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "fr",
        "website": "https://lesjeunesjardiniers.be/",
        "foi_email": "info@lesjeunesjardiniers.be",
        "foi_postal": "Chaussée d'Alsemberg 1393, 1180 Uccle",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0414.842.571 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl LOSS FLIP {PN25} "
            f"equity DROP {EQ25} (-52%) FTE JUMP {FTE25}; neerlegging 27.07.2026; assets/debt "
            f"Unknown; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; after La Lumière@2244; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_jeunes_jardiniers_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +1.29% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_jeunes_jardiniers_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +16.51% vs YE2024 {OM24}",
    ),
    (
        "bud_jeunes_jardiniers_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 LOSS FLIP",
        f"tick{TICK}; Medium CW; pnl LOSS FLIP {PN25} vs YE2024 profit {PN24}",
    ),
    (
        "bud_jeunes_jardiniers_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -52.28% vs YE2024 {EQ24} (thin)",
    ),
    (
        "bud_jeunes_jardiniers_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 140.5",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_jeunes_jardiniers_fte_jr2024_statutory_cmp",
        "2024",
        FTE24,
        "CW social-balance FTE YE2024 comparative",
        f"tick{TICK}; YE2024 FTE {FTE24} comparative",
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
            "source_id": "src_jeunes_jardiniers_jr2025_cw_en",
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
            f"Les Jeunes Jardiniers YE2025 leftover dual (bruto 4.78m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS FLIP / equity DROP -52% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Brussels-Uccle / PHARE-COCOF adapted-work public path",
        "legal_basis": (
            "ASBL ETA Les Jeunes Jardiniers (KBO 0414.842.571; Actief; 1 VE; NACE 88.993; Brussels)"
        ),
        "decision_date": "2026-07-27",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": (
            f'{{"2025_bruto":{BR25},"2025_omzet":{OM25},"2025_pnl":{PN25},'
            f'"2025_equity":{EQ25},"2025_fte":{FTE25},"2024_bruto":{BR24},'
            f'"2024_omzet":{OM24},"2024_pnl":{PN24},"2024_fte":{FTE24}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0414842571/les-jeunes-jardiniers",
        "stated_goal": "Brussels ETA garden creation / maintenance",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl LOSS FLIP + equity DROP -52%"
        ),
        "source_id": "src_jeunes_jardiniers_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>Uccle>JeunesJardiniers>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl LOSS FLIP {PN25}; equity DROP {EQ25}; FTE JUMP {FTE25}; 1 VE; after La Lumière@2244"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.2, abs 7.9, diff 3 → pi = 2.86+2.765+0.7 = 6.325 → 6.30
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"Jeunes Jardiniers bruto 4.78m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / "
            "equity DROP -52% (YE2025 Brussels ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Bruxelles>Uccle>JeunesJardiniers>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl LOSS FLIP {PN25} / "
            f"equity DROP {EQ25} (-52%) / FTE JUMP {FTE25} / 1 VE Brussels ETA"
        ),
        "confidence": "medium",
        "source_id": "src_jeunes_jardiniers_jr2025_cw_en",
        "beneficiaries": "ETA workers Brussels-Uccle / PHARE-COCOF adapted-work public path",
        "stated_goal": "Brussels ETA garden creation / maintenance",
        "measured_outcome": (
            f"omzet JUMP +16.51%; bruto≫omzet ~{RATIO}x; pnl LOSS FLIP {PN25}; "
            f"equity DROP -52.28%; FTE JUMP {FTE25}; filed 27.07.2026"
        ),
        "absurdity_score": "7.9",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "PHARE ETA matrix; reconcile LOSS FLIP + equity DROP -52%"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after La Lumière@2244"
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
            "Bruxelles>Uccle>JeunesJardiniers>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip_equity_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl LOSS FLIP EUR{PN25} vs YE2024 profit EUR{PN24}; "
            f"equity DROP EUR{EQ25} (-52% vs {EQ24}); PHARE ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels ETA ASBL (bruto 4.78m / omzet 2.43m / ~{RATIO}x / "
            "pnl LOSS FLIP / equity DROP -52%) under PHARE path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Les Jeunes Jardiniers ASBL",
        "recipient_email": "info@lesjeunesjardiniers.be",
        "recipient_postal": "Chaussée d'Alsemberg 1393, 1180 Uccle",
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
            "after La Lumière@2244"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2245",
    {
        "task_id": "rq_2245",
        "title": (
            f"leftover dual — Les Jeunes Jardiniers YE2025 Medium (bruto 4.78m / bruto≫omzet "
            f"~{RATIO}x / pnl LOSS FLIP / equity DROP -52%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after La Lumière; unused FREE Brussels ETA Jeunes Jardiniers YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T03:10:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Jeunes Jardiniers 0414.842.571 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl LOSS FLIP {PN25} equity DROP {EQ25} (-52%) FTE JUMP {FTE25}; "
            "1 VE Brussels ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after La Lumière@2244; deferred FREE TRAVCO/Pilifs; do NOT redo La Lumière/APAM/"
            "Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123; next rq_2246; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2246",
    {
        "task_id": "rq_2246",
        "title": (
            "leftover dual after Jeunes Jardiniers — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after Jeunes Jardiniers YE2025 Medium (bruto 4.78m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS FLIP / equity DROP -52%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
            "TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. TRAVCO / La Ferme Nos Pilifs / Charles Lambert if YE2025 FREE; skip "
            "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). Do NOT redo "
            "Jeunes Jardiniers, La Lumière, APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, "
            "Manufast, Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, "
            "Travie, SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, "
            "Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Jeunes Jardiniers; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; deferred FREE TRAVCO/Pilifs; next every-10 2250"
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
        "last_unit_id": "rq_2245",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover Jeunes Jardiniers 0414.842.571 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl LOSS FLIP {PN25}; equity DROP {EQ25} -52%; FTE JUMP {FTE25}; 1 VE Brussels ETA); "
            "after La Lumière@2244; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE TRAVCO/Pilifs; next rq_2246; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — Les Jeunes Jardiniers (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / equity DROP -52%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Les Jeunes Jardiniers ASBL — KBO **0414.842.571** (Actief; Chaussée d'Alsemberg 1393, 1180 Uccle; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Brussels ETA COCOF/PHARE)  
**recipient:** info@lesjeunesjardiniers.be · Chaussée d'Alsemberg 1393, 1180 Uccle  
**sources:** [CW EN](https://www.companyweb.be/en/0414842571/les-jeunes-jardiniers) · [CW NL](https://www.companyweb.be/nl/0414842571/les-jeunes-jardiniers) · [CW FR](https://www.companyweb.be/fr/0414842571/les-jeunes-jardiniers) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=414842571) · [site](https://lesjeunesjardiniers.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **1 VE**; zetel Chaussée d'Alsemberg Uccle; NACE **88.993**; info@lesjeunesjardiniers.be.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +16.51% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +1.29% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** LOSS FLIP vs YE2024 profit EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -52.28% vs YE2024 EUR{EQ24:,}; FTE **{FTE25}** JUMP vs {FTE24}; filed **27.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After La Lumière@2244. Deferred FREE TRAVCO/Pilifs.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Les Jeunes Jardiniers ASBL
via info@lesjeunesjardiniers.be
Chaussée d'Alsemberg 1393, 1180 Uccle
Objet: Publicité des comptes annuels 2025 Les Jeunes Jardiniers (BCE 0414.842.571)

Madame, Monsieur,

Sur la base de l'ordonnance bruxelloise relative à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL LOSS FLIP EUR{PN25} vs YE2024 profit EUR{PN24} — réconciliation avec equity DROP -52% (EUR{EQ25}).
4. Matrice des subsides PHARE/COCOF / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts création/entretien jardins / livraison Drogenbos.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2245 Les Jeunes Jardiniers Uccle (bruto 4.78m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / equity DROP -52% / Medium)

- Unit: **rq_2245** leftover dual after **rq_2244 La Lumière**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE unused Brussels ETA **Les Jeunes Jardiniers ASBL** YE2025 (KBO **0414.842.571**; Chaussée d'Alsemberg 1393 Uccle; **Actief** **1 VE**; NACE **88.993** PHARE/COCOF). Deferred FREE TRAVCO/Pilifs. Do not redo La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +16.51% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +1.29% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** LOSS FLIP vs YE2024 profit EUR{PN24}; equity **EUR{EQ25}** DROP -52.28% vs YE2024 EUR{EQ24}; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **27.07.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@lesjeunesjardiniers.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2245=done + rq_2246 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2245/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2246 (AGB/FARO-if-YE2025 / AIESH-REW / unused TRAVCO-Pilifs).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} equity={EQ25} next=rq_2246")
