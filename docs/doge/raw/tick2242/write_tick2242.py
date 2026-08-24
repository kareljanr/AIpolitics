# tick2242 — leftover dual ETA Le Perron YE2025 Medium (bruto 4.00m / ~1.70x / FTE JUMP 90)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_eta_le_perron_liege"
TICK = "2242"
UTC = "2026-08-27T02:40:00Z"
GAP = "gap_le_perron_nbb_pdf_assets_debt_bruto_gt_omzet_1_70x_fte_jump_eta_matrix_l5"
COMM = "comm_le_perron_jr2025_statutory_eta_bruto_gt_omzet_fte_jump"
LB = "lb_le_perron_bruto_4_00m_gt_omzet_1_70x_fte_jump_jr2025"

OM25, OM24 = 2357524, 2195929
BR25, BR24 = 4004628, 3575530
PN25, PN24 = 330810, 310743
EQ25, EQ24 = 6018954, 5703795
FTE25, FTE24 = 90.0, 88.8
RATIO = round(BR25 / OM25, 2)  # ~1.70


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
        "src_le_perron_jr2025_cw_nl",
        "Companyweb NL ETA Le Perron YE2025 statutory",
        "https://www.companyweb.be/nl/0404225130/entreprise-de-travail-adapte-le-perron",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+7.36%) bruto JUMP {BR25} (+12% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+6.46%) equity JUMP {EQ25} (+5.53%) "
            f"FTE JUMP {FTE25}; filed 29-04-2026"
        ),
    ),
    (
        "src_le_perron_jr2025_cw_en",
        "Companyweb EN ETA Le Perron YE2025 statutory",
        "https://www.companyweb.be/en/0404225130/entreprise-de-travail-adapte-le-perron",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 29-04-2026"
        ),
    ),
    (
        "src_le_perron_jr2025_cw_fr",
        "Companyweb FR ETA Le Perron YE2025 statutory",
        "https://www.companyweb.be/fr/0404225130/entreprise-de-travail-adapte-le-perron",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_le_perron_kbo_2242",
        "KBO ETA Le Perron 0404.225.130 Actief Liège 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=404225130",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2242; Actief VZW/ASBL ETA LE PERRON; zetel Boulevard Sainte-Beuve 31A 4000 Liège; "
            "1 VE; NACE RSZ 88.993; Liège ETA"
        ),
    ),
    (
        "src_le_perron_site_contact_2242",
        "Le Perron FOI channel info@leperron.be",
        "https://www.leperron.be/contact/",
        "ETA Le Perron ASBL",
        "foi_contact",
        "tick2242; info@leperron.be; +32 4 252 69 06; Boulevard Sainte-Beuve 31A 4000 Liège",
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
        "name_nl": "ETA Le Perron VZW (Luik / maatwerk Wallonië)",
        "name_fr": "ETA Le Perron ASBL (Liège / entreprise de travail adapté)",
        "name_en": "ETA Le Perron adapted-work ASBL (Liège Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.leperron.be/",
        "foi_email": "info@leperron.be",
        "foi_postal": "Boulevard Sainte-Beuve 31A, 4000 Liège",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0404.225.130 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} "
            f"equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 29.04.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; after L'Atelier@2241; do NOT redo L'Atelier/Axedis/ETA123/Manufast; "
            "not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_le_perron_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +12% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_le_perron_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +7.36% vs YE2024 {OM24}",
    ),
    (
        "bud_le_perron_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +6.46% vs YE2024 {PN24}",
    ),
    (
        "bud_le_perron_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +5.53% vs YE2024 {EQ24}",
    ),
    (
        "bud_le_perron_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 90",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_le_perron_fte_jr2024_statutory_cmp",
        "2024",
        FTE24,
        "CW social-balance FTE YE2024 comparative",
        f"tick{TICK}; YE2024 FTE {FTE24} comparative (pre JUMP)",
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
            "source_id": "src_le_perron_jr2025_cw_en",
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
            f"ETA Le Perron YE2025 leftover dual (bruto 4.00m / bruto≫omzet ~{RATIO}x / "
            "FTE JUMP 90 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Liège / AVIQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA Le Perron (KBO 0404.225.130; Actief; 1 VE; NACE 88.993; Liège)"
        ),
        "decision_date": "2026-04-29",
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
        "evaluation_url": (
            "https://www.companyweb.be/en/0404225130/entreprise-de-travail-adapte-le-perron"
        ),
        "stated_goal": "Liège ETA industrial subcontracting / electrical / packaging",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile FTE JUMP 90 vs AVIQ ETA matrix"
        ),
        "source_id": "src_le_perron_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>LePerron>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"FTE JUMP {FTE25}; 1 VE; after L'Atelier@2241"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost ~5.2 (<10m), abs 7.0 (1.70x), diff 3 → pi = 0.55*5.2 + 0.35*7.0 + 0.7 = 6.01 → 6.00
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"Le Perron bruto 4.00m / bruto≫omzet ~{RATIO}x / FTE JUMP 90 "
            "(YE2025 Liège ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Liege>LePerron>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} / "
            f"equity JUMP {EQ25} / FTE JUMP {FTE25} / 1 VE Liège ETA"
        ),
        "confidence": "medium",
        "source_id": "src_le_perron_jr2025_cw_en",
        "beneficiaries": "ETA workers Liège / AVIQ adapted-work public path",
        "stated_goal": "Liège ETA industrial subcontracting",
        "measured_outcome": (
            f"omzet JUMP +7.36%; bruto≫omzet ~{RATIO}x; pnl JUMP +6.46%; "
            f"equity JUMP +5.53%; FTE JUMP {FTE25}; filed 29.04.2026"
        ),
        "absurdity_score": "7.0",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.00",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "AVIQ ETA matrix; reconcile FTE JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after L'Atelier@2241"
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
            "Wallonie>Liege>LePerron>NBB_PDF_assets_debt_bruto_gt_omzet_fte_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); FTE JUMP {FTE25} vs YE2024 {FTE24}; "
            f"AVIQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Liège ETA ASBL (bruto 4.00m / omzet 2.36m / ~{RATIO}x / "
            "FTE JUMP 90) under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "ETA Le Perron ASBL",
        "recipient_email": "info@leperron.be",
        "recipient_postal": "Boulevard Sainte-Beuve 31A, 4000 Liège",
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
            "after L'Atelier@2241"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2242",
    {
        "task_id": "rq_2242",
        "title": (
            f"leftover dual — ETA Le Perron YE2025 Medium (bruto 4.00m / bruto≫omzet "
            f"~{RATIO}x / FTE JUMP 90)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after L'Atelier; named FREE Le Perron YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T02:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Le Perron 0404.225.130 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl JUMP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; "
            "1 VE Liège ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after L'Atelier@2241; do NOT redo L'Atelier/Axedis/ETA123/Manufast/Metalgroup/"
            "EntrAnam/Enghien/Entra; next rq_2243; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2243",
    {
        "task_id": "rq_2243",
        "title": (
            "leftover dual after Le Perron — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after Le Perron YE2025 Medium (bruto 4.00m / bruto≫omzet ~{RATIO}x / "
            "FTE JUMP 90). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. Jean Gielen if YE2025 FREE; skip Le Perron/L'Atelier/"
            "Axedis/ETA123). Do NOT redo Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, "
            "Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, "
            "Travie, SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, "
            "Den Azalee, Kemphaan. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Le Perron; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
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
        "last_unit_id": "rq_2242",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover Le Perron 0404.225.130 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl JUMP {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 1 VE Liège ETA); "
            "after L'Atelier@2241; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "next rq_2243; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — ETA Le Perron (NBB PDF / bruto≫omzet ~{RATIO}x / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ETA Le Perron ASBL — KBO **0404.225.130** (Actief; Boulevard Sainte-Beuve 31A, 4000 Liège; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Liège ETA)  
**recipient:** info@leperron.be · Boulevard Sainte-Beuve 31A, 4000 Liège  
**sources:** [CW EN](https://www.companyweb.be/en/0404225130/entreprise-de-travail-adapte-le-perron) · [CW NL](https://www.companyweb.be/nl/0404225130/entreprise-de-travail-adapte-le-perron) · [CW FR](https://www.companyweb.be/fr/0404225130/entreprise-de-travail-adapte-le-perron) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=404225130) · [site](https://www.leperron.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **1 VE**; zetel Boulevard Sainte-Beuve Liège; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +7.36% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +12% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +6.46%; equity **EUR{EQ25:,}** JUMP +5.53%; FTE **{FTE25}** JUMP vs {FTE24}; filed **29.04.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After L'Atelier@2241.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ETA Le Perron ASBL
via info@leperron.be
Boulevard Sainte-Beuve 31A, 4000 Liège
Objet: Publicité des comptes annuels 2025 ETA Le Perron (BCE 0404.225.130)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. FTE JUMP {FTE25} vs YE2024 {FTE24} — réconciliation avec pnl/equity JUMP.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts site Liège / sous-traitance industrielle (électricité, mécanique, emballage).

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2242 ETA Le Perron Liège (bruto 4.00m / bruto≫omzet ~{RATIO}x / FTE JUMP 90 / Medium)

- Unit: **rq_2242** leftover dual after **rq_2241 L'Atelier**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Jean Gielen still YE2024. Took named FREE Liège ETA **Le Perron ASBL** YE2025 (KBO **0404.225.130**; Boulevard Sainte-Beuve 31A Liège; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo L'Atelier/Axedis/ETA123/Manufast stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +7.36% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +12% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +6.46%; equity **EUR{EQ25}** JUMP +5.53%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **29.04.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@leperron.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2242=done + rq_2243 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2242/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2243 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} fte={FTE25} next=rq_2243")
