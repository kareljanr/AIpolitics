# tick2248 — leftover dual Jean Del'Cour YE2025 Medium (bruto 21.81m / ~1.57x / FTE JUMP 548)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_jean_delcour_grace_hollogne"
TICK = "2248"
UTC = "2026-08-27T04:10:00Z"
GAP = "gap_jean_delcour_nbb_pdf_assets_debt_bruto_gt_omzet_1_57x_fte_jump_548_eta_matrix_l5"
COMM = "comm_jean_delcour_jr2025_statutory_eta_bruto_gt_omzet_fte_jump"
LB = "lb_jean_delcour_bruto_21_81m_gt_omzet_1_57x_fte_jump_548_jr2025"

OM25, OM24 = 13917312, 13670459
BR25, BR24 = 21813084, 21086822
PN25, PN24 = 189058, 154190
EQ25, EQ24 = 3135044, 3077926
FTE25, FTE24 = 548.0, 535.6
RATIO = round(BR25 / OM25, 2)  # ~1.57


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
        "src_jean_delcour_jr2025_cw_nl",
        "Companyweb NL Jean Del'Cour YE2025 statutory",
        "https://www.companyweb.be/nl/0407410490/jean-del-cour",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+2%) bruto JUMP {BR25} (+3% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+23%) equity JUMP {EQ25} (+2%) "
            f"FTE JUMP {FTE25}; filed 05-05-2026"
        ),
    ),
    (
        "src_jean_delcour_jr2025_cw_en",
        "Companyweb EN Jean Del'Cour YE2025 statutory",
        "https://www.companyweb.be/en/0407410490/jean-del-cour",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 05-05-2026"
        ),
    ),
    (
        "src_jean_delcour_jr2025_cw_fr",
        "Companyweb FR Jean Del'Cour YE2025 statutory",
        "https://www.companyweb.be/fr/0407410490/jean-del-cour",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_jean_delcour_kbo_2248",
        "KBO Jean Del'Cour 0407.410.490 Actief Grâce-Hollogne 4 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407410490",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2248; Actief VZW/ASBL Jean Del'cour; zetel Rue de l'Expansion 29 4460 Grâce-Hollogne; "
            "4 VE; NACE RSZ 88.993; Walloon ETA Liège province; administration@jean-delcour.be"
        ),
    ),
    (
        "src_jean_delcour_site_contact_2248",
        "Jean Del'Cour FOI channel info@jean-delcour.be",
        "https://jean-delcour.be/",
        "Jean Del'Cour ASBL",
        "foi_contact",
        "tick2248; info@jean-delcour.be / administration@jean-delcour.be; +32 4 239 80 80; Rue de l'Expansion 29 4460 Grâce-Hollogne",
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
        "name_nl": "Jean Del'Cour VZW (Grâce-Hollogne / ETA maatwerk Luik)",
        "name_fr": "Jean Del'Cour ASBL (Grâce-Hollogne / entreprise de travail adapté Liège)",
        "name_en": "Jean Del'Cour adapted-work ASBL (Grâce-Hollogne Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://jean-delcour.be/",
        "foi_email": "info@jean-delcour.be",
        "foi_postal": "Rue de l'Expansion 29, 4460 Grâce-Hollogne",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.410.490 Actief 4 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} "
            f"equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 05.05.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; FOES YE2024-only; after TRAVCO@2247; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_jean_delcour_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +3% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_jean_delcour_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +2% vs YE2024 {OM24}",
    ),
    (
        "bud_jean_delcour_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +23% vs YE2024 {PN24}",
    ),
    (
        "bud_jean_delcour_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +2% vs YE2024 {EQ24}",
    ),
    (
        "bud_jean_delcour_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 548",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_jean_delcour_fte_jr2024_statutory_cmp",
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
            "source_id": "src_jean_delcour_jr2025_cw_en",
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
            f"Jean Del'Cour YE2025 leftover dual (bruto 21.81m / bruto≫omzet ~{RATIO}x / "
            "FTE JUMP 548 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Liège province / AVIQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA Jean Del'Cour (KBO 0407.410.490; Actief; 4 VE; NACE 88.993; Grâce-Hollogne)"
        ),
        "decision_date": "2026-05-05",
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
        "evaluation_url": "https://www.companyweb.be/en/0407410490/jean-del-cour",
        "stated_goal": "Walloon ETA logistics / technical / green spaces / aerospace subcontracting",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile FTE JUMP 548 vs AVIQ ETA matrix"
        ),
        "source_id": "src_jean_delcour_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>JeanDelCour>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"FTE JUMP {FTE25}; 4 VE; after TRAVCO@2247"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.5 (21.8m), abs 7.4, diff 3 → pi = 3.025+2.59+0.7 = 6.315 → 6.30
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"Jean Del'Cour bruto 21.81m / bruto≫omzet ~{RATIO}x / FTE JUMP 548 "
            "(YE2025 Walloon ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Liege>JeanDelCour>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} / "
            f"equity JUMP {EQ25} / FTE JUMP {FTE25} / 4 VE Walloon ETA"
        ),
        "confidence": "medium",
        "source_id": "src_jean_delcour_jr2025_cw_en",
        "beneficiaries": "ETA workers Liège province / AVIQ adapted-work public path",
        "stated_goal": "Walloon ETA logistics / technical / green spaces",
        "measured_outcome": (
            f"omzet JUMP +2%; bruto≫omzet ~{RATIO}x; pnl JUMP +23%; "
            f"equity JUMP +2%; FTE JUMP {FTE25}; filed 05.05.2026"
        ),
        "absurdity_score": "7.4",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "AVIQ ETA matrix; reconcile FTE JUMP 548"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; FOES YE2024-only; after TRAVCO@2247"
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
            "Wallonie>Liege>JeanDelCour>NBB_PDF_assets_debt_bruto_gt_omzet_fte_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); FTE JUMP {FTE25} vs YE2024 {FTE24}; "
            f"AVIQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows large Walloon ETA ASBL (bruto 21.81m / omzet 13.92m / ~{RATIO}x / "
            "FTE JUMP 548) under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Jean Del'Cour ASBL",
        "recipient_email": "info@jean-delcour.be",
        "recipient_postal": "Rue de l'Expansion 29, 4460 Grâce-Hollogne",
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
            "FOES YE2024-only; after TRAVCO@2247"
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
            f"leftover dual — Jean Del'Cour YE2025 Medium (bruto 21.81m / bruto≫omzet "
            f"~{RATIO}x / FTE JUMP 548)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after TRAVCO; unused FREE large Walloon ETA Jean Del'Cour YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T03:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Jean Del'Cour 0407.410.490 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl JUMP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; "
            "4 VE Walloon ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "FOES YE2024-only; after TRAVCO@2247; do NOT redo TRAVCO/Pilifs/Jeunes Jardiniers/"
            "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123; next rq_2249; next EVERY-10 2250"
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
            "leftover dual after Jean Del'Cour — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after Jean Del'Cour YE2025 Medium (bruto 21.81m / bruto≫omzet ~{RATIO}x / "
            "FTE JUMP 548). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused ETA/VAPH/"
            "WZC/maatwerk (e.g. Serviplast / Les Dauphins / Le Saupont if YE2025 FREE; skip Jean Del'Cour/"
            "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). "
            "Do NOT redo Jean Del'Cour, TRAVCO, Pilifs, Jeunes Jardiniers, La Lumière, APAM, Jean Gielen, "
            "Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, Metalgroup, EntrAnam, Enghien, Entra, "
            "Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, De Oever, "
            "ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, Kemphaan, Mirto, Blankedale, Werkmmaat. "
            "Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Jean Del'Cour; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; FOES YE2024-only; next every-10 2250"
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
            f"tick{TICK} leftover Jean Del'Cour 0407.410.490 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl JUMP {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 4 VE Walloon ETA); "
            "after TRAVCO@2247; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "FOES YE2024-only; next rq_2249; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — Jean Del'Cour (NBB PDF / bruto≫omzet ~{RATIO}x / FTE JUMP 548)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Jean Del'Cour ASBL — KBO **0407.410.490** (Actief; Rue de l'Expansion 29, 4460 Grâce-Hollogne; **4 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon ETA Liège)  
**recipient:** info@jean-delcour.be · Rue de l'Expansion 29, 4460 Grâce-Hollogne  
**sources:** [CW EN](https://www.companyweb.be/en/0407410490/jean-del-cour) · [CW NL](https://www.companyweb.be/nl/0407410490/jean-del-cour) · [CW FR](https://www.companyweb.be/fr/0407410490/jean-del-cour) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=407410490) · [site](https://jean-delcour.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **4 VE**; zetel Rue de l'Expansion Grâce-Hollogne; NACE **88.993**; administration@jean-delcour.be.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +2% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +3% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +23%; equity **EUR{EQ25:,}** JUMP +2%; FTE **{FTE25}** JUMP vs {FTE24}; filed **05.05.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; FOES YE2024-only. After TRAVCO@2247.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Jean Del'Cour ASBL
via info@jean-delcour.be
Rue de l'Expansion 29, 4460 Grâce-Hollogne
Objet: Publicité des comptes annuels 2025 Jean Del'Cour (BCE 0407.410.490)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. FTE JUMP {FTE25} vs YE2024 {FTE24} — réconciliation avec pnl/equity JUMP.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts sites Grâce-Hollogne / Herstal / Hauts-Sarts / Trilogiport / Plénesses.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2248 Jean Del'Cour Grâce-Hollogne (bruto 21.81m / bruto≫omzet ~{RATIO}x / FTE JUMP 548 / Medium)

- Unit: **rq_2248** leftover dual after **rq_2247 TRAVCO**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Groupe FOES still **YE2024**. Took FREE unused large Walloon ETA **Jean Del'Cour ASBL** YE2025 (KBO **0407.410.490**; Rue de l'Expansion 29 Grâce-Hollogne; **Actief** **4 VE**; NACE **88.993** AViQ). Do not redo TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +2% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +3% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +23%; equity **EUR{EQ25}** JUMP +2%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **05.05.2026**. Strong KBO Actief 4 VE. Assets/debt Unknown. Medium. FOI via info@jean-delcour.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2248=done + rq_2249 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2248/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2249 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} fte={FTE25} next=rq_2249")
