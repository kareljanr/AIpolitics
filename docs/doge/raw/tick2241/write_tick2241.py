# tick2241 — leftover dual L'Atelier Namur YE2025 Medium (bruto 12.09m / ~2.07x / pnl LOSS FLIP)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_latelier_namur"
TICK = "2241"
UTC = "2026-08-27T02:25:00Z"
GAP = "gap_latelier_nbb_pdf_assets_debt_bruto_gt_omzet_2_07x_pnl_loss_flip_eta_matrix_l5"
COMM = "comm_latelier_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_flip"
LB = "lb_latelier_bruto_12_09m_gt_omzet_2_07x_pnl_loss_flip_jr2025"

OM25, OM24 = 5845927, 5802371
BR25, BR24 = 12091076, 11897830
PN25, PN24 = -64415, 50410
EQ25, EQ24 = 6288893, 6433470
FTE25, FTE24 = 324.7, 326.6
RATIO = round(BR25 / OM25, 2)  # ~2.07


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


# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_latelier_jr2025_cw_nl",
        "Companyweb NL L'Atelier Namur YE2025 statutory",
        "https://www.companyweb.be/nl/0407884307/l-atelier",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+0.75%) bruto JUMP {BR25} (+1.62% "
            f"bruto≫omzet ~{RATIO}x) pnl LOSS FLIP {PN25} vs YE2024 profit {PN24} "
            f"equity DROP {EQ25} (-2.25%) FTE DROP {FTE25}; filed 27-06-2026"
        ),
    ),
    (
        "src_latelier_jr2025_cw_en",
        "Companyweb EN L'Atelier Namur YE2025 statutory",
        "https://www.companyweb.be/en/0407884307/l-atelier",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 27-06-2026"
        ),
    ),
    (
        "src_latelier_jr2025_cw_fr",
        "Companyweb FR L'Atelier Namur YE2025 statutory",
        "https://www.companyweb.be/fr/0407884307/l-atelier",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice/perte {PN25}",
    ),
    (
        "src_latelier_kbo_2241",
        "KBO L'Atelier 0407.884.307 Actief Namur-Naninne 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407884307",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2241; Actief VZW/ASBL L'Atelier; zetel Rue des Pieds d'Alouette 51-53 5100 Namur; "
            "1 VE; NACE RSZ/BTW 88.993; Namur province ETA (Naninne)"
        ),
    ),
    (
        "src_latelier_site_contact_2241",
        "L'Atelier FOI channel info@atelier-namur.be",
        "https://www.atelier-namur.be/contact",
        "L'Atelier ASBL",
        "foi_contact",
        "tick2241; info@atelier-namur.be; +32 81 30 19 77; Rue Pieds d'Alouette 51-53 5100 Naninne",
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
        "name_nl": "L'Atelier VZW (Namur-Naninne / ETA maatwerk provincie Namen)",
        "name_fr": "L'Atelier ASBL (Namur-Naninne / entreprise de travail adapté)",
        "name_en": "L'Atelier adapted-work ASBL (Namur-Naninne Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.atelier-namur.be/",
        "foi_email": "info@atelier-namur.be",
        "foi_postal": "Rue des Pieds d'Alouette 51-53, 5100 Namur (Naninne)",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.884.307 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl LOSS FLIP {PN25} "
            f"equity DROP {EQ25} FTE DROP {FTE25}; neerlegging 27.06.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; after Axedis@2240; do NOT redo Axedis/ETA123/Manufast/Metalgroup; "
            "not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_latelier_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +1.62% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_latelier_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +0.75% vs YE2024 {OM24}",
    ),
    (
        "bud_latelier_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 LOSS FLIP",
        f"tick{TICK}; Medium CW; pnl LOSS FLIP {PN25} vs YE2024 profit {PN24} (-227.78%)",
    ),
    (
        "bud_latelier_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -2.25% vs YE2024 {EQ24}",
    ),
    (
        "bud_latelier_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 324.7",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_latelier_fte_jr2024_statutory_cmp",
        "2024",
        FTE24,
        "CW social-balance FTE YE2024 comparative",
        f"tick{TICK}; YE2024 FTE {FTE24} comparative (pre DROP)",
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
            "source_id": "src_latelier_jr2025_cw_en",
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
            f"L'Atelier Namur YE2025 leftover dual (bruto 12.09m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS FLIP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Namur-Naninne / AVIQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA L'Atelier (KBO 0407.884.307; Actief; 1 VE; NACE 88.993; Namur province)"
        ),
        "decision_date": "2026-06-27",
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
        "evaluation_url": "https://www.companyweb.be/en/0407884307/l-atelier",
        "stated_goal": "Namur ETA industrial subcontracting / packaging / green spaces",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl LOSS FLIP vs modest FTE DROP"
        ),
        "source_id": "src_latelier_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Namur>Naninne>LAtelier>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl LOSS FLIP {PN25}; FTE DROP {FTE25}; 1 VE; after Axedis@2240"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost_score ~5.5 (<100m), absurdity 7.6 (2.07x + LOSS FLIP), difficulty 3
# pi = 0.55*5.5 + 0.35*7.6 + 0.10*7 = 6.385 → 6.40
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"L'Atelier bruto 12.09m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP "
            "(YE2025 Namur ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Namur>Naninne>LAtelier>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl LOSS FLIP {PN25} / "
            f"equity DROP {EQ25} / FTE DROP {FTE25} / 1 VE Namur ETA"
        ),
        "confidence": "medium",
        "source_id": "src_latelier_jr2025_cw_en",
        "beneficiaries": "ETA workers Namur-Naninne / AVIQ adapted-work public path",
        "stated_goal": "Namur ETA industrial subcontracting / packaging",
        "measured_outcome": (
            f"omzet JUMP +0.75%; bruto≫omzet ~{RATIO}x; pnl LOSS FLIP {PN25}; "
            f"equity DROP -2.25%; FTE DROP {FTE25}; filed 27.06.2026"
        ),
        "absurdity_score": "7.6",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "6.40",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "AVIQ ETA matrix; reconcile pnl LOSS FLIP vs FTE DROP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Axedis@2240"
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
            "Wallonie>Namur>Naninne>LAtelier>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl LOSS FLIP EUR{PN25} vs YE2024 profit EUR{PN24}; "
            f"AVIQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Namur ETA ASBL (bruto 12.09m / omzet 5.85m / ~{RATIO}x / "
            "pnl LOSS FLIP) under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "L'Atelier ASBL",
        "recipient_email": "info@atelier-namur.be",
        "recipient_postal": "Rue des Pieds d'Alouette 51-53, 5100 Namur (Naninne)",
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
            "after Axedis@2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

# research queue: close rq_2241, spawn rq_2242
rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2241",
    {
        "task_id": "rq_2241",
        "title": (
            f"leftover dual — L'Atelier Namur YE2025 Medium (bruto 12.09m / bruto≫omzet "
            f"~{RATIO}x / pnl LOSS FLIP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Axedis; unused FREE Namur ETA L'Atelier YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T02:05:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; L'Atelier 0407.884.307 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl LOSS FLIP {PN25} equity DROP {EQ25} FTE DROP {FTE25}; "
            "1 VE Namur ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Axedis@2240; do NOT redo Axedis/ETA123/Manufast/Metalgroup/EntrAnam/Enghien/"
            "Entra/Ateliers/Rekreatief; next rq_2242; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2242",
    {
        "task_id": "rq_2242",
        "title": (
            "leftover dual after L'Atelier — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after L'Atelier YE2025 Medium (bruto 12.09m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. Jean Gielen / Le Perron if YE2025 FREE; skip L'Atelier/"
            "Axedis/ETA123). Do NOT redo L'Atelier, Axedis, ETA 123 Beauraing, Manufast, Metalgroup, "
            "EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, "
            "De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, "
            "Kemphaan. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} L'Atelier; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
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
        "last_unit_id": "rq_2241",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover L'Atelier 0407.884.307 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl LOSS FLIP {PN25}; equity DROP {EQ25}; FTE DROP {FTE25}; 1 VE Namur ETA); "
            "after Axedis@2240; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "next rq_2242; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — L'Atelier Namur (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** L'Atelier ASBL — KBO **0407.884.307** (Actief; Rue des Pieds d'Alouette 51-53, 5100 Namur/Naninne; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Namur province ETA)  
**recipient:** info@atelier-namur.be · Rue des Pieds d'Alouette 51-53, 5100 Namur (Naninne)  
**sources:** [CW EN](https://www.companyweb.be/en/0407884307/l-atelier) · [CW NL](https://www.companyweb.be/nl/0407884307/l-atelier) · [CW FR](https://www.companyweb.be/fr/0407884307/l-atelier) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407884307) · [site](https://www.atelier-namur.be/contact)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **1 VE**; zetel Rue des Pieds d'Alouette Namur; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +0.75% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +1.62% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** LOSS FLIP vs YE2024 profit EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -2.25%; FTE **{FTE25}** DROP vs {FTE24}; filed **27.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Axedis@2240.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: L'Atelier ASBL
via info@atelier-namur.be
Rue des Pieds d'Alouette 51-53, 5100 Namur (Naninne)
Objet: Publicité des comptes annuels 2025 L'Atelier (BCE 0407.884.307)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL LOSS FLIP EUR{PN25} vs YE2024 profit EUR{PN24} — réconciliation avec FTE DROP {FTE25}.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts site Naninne / sous-traitance industrielle / espaces verts.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2241 L'Atelier Namur (bruto 12.09m / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP / Medium)

- Unit: **rq_2241** leftover dual after **rq_2240 Axedis**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; ETA 123 Beauraing / Axedis / Senes already mined. Took FREE unused Namur ETA **L'Atelier ASBL** YE2025 (KBO **0407.884.307**; Rue des Pieds d'Alouette 51-53 Namur/Naninne; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Axedis/ETA123/Manufast/Metalgroup/EntrAnam stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +0.75% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +1.62% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** LOSS FLIP vs YE2024 profit EUR{PN24}; equity **EUR{EQ25}** DROP -2.25%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **27.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@atelier-namur.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.40); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2241=done + rq_2242 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2241/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2242 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} pnl={PN25} next=rq_2242")
