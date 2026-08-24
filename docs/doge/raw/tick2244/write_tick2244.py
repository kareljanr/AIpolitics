# tick2244 — leftover dual ETA La Lumière YE2025 Medium (bruto 7.25m / ~2.37x / pnl LOSS DEEPEN)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_eta_la_lumiere_liege"
TICK = "2244"
UTC = "2026-08-27T03:10:00Z"
GAP = "gap_la_lumiere_nbb_pdf_assets_debt_bruto_gt_omzet_2_37x_pnl_loss_deepen_eta_matrix_l5"
COMM = "comm_la_lumiere_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_deepen"
LB = "lb_la_lumiere_bruto_7_25m_gt_omzet_2_37x_pnl_loss_deepen_jr2025"

OM25, OM24 = 3056352, 2898178
BR25, BR24 = 7253203, 6127282
PN25, PN24 = -185782, -74020
EQ25, EQ24 = 7933506, 8121288
FTE25, FTE24 = 122.4, 118.5
RATIO = round(BR25 / OM25, 2)  # ~2.37


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
        "src_la_lumiere_jr2025_cw_nl",
        "Companyweb NL ETA La Lumière YE2025 statutory",
        "https://www.companyweb.be/nl/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+5.46%) bruto JUMP {BR25} (+18.38% "
            f"bruto≫omzet ~{RATIO}x) pnl LOSS DEEPEN {PN25} vs YE2024 {PN24} "
            f"equity DROP {EQ25} (-2.31%) FTE JUMP {FTE25}; filed 24-06-2026"
        ),
    ),
    (
        "src_la_lumiere_jr2025_cw_en",
        "Companyweb EN ETA La Lumière YE2025 statutory",
        "https://www.companyweb.be/en/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 24-06-2026"
        ),
    ),
    (
        "src_la_lumiere_jr2025_cw_fr",
        "Companyweb FR ETA La Lumière YE2025 statutory",
        "https://www.companyweb.be/fr/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_la_lumiere_kbo_2244",
        "KBO La Lumière 0402.345.211 Actief Liège 2 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=402345211",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2244; Actief VZW/ASBL LA LUMIERE Oeuvre Royale; zetel Rue Sainte-Véronique 17 "
            "4000 Liège; 2 VE; NACE RSZ 88.993; ETA site Boulevard Louis Hillier 1"
        ),
    ),
    (
        "src_la_lumiere_site_contact_2244",
        "ETA La Lumière FOI channel eta@lalumiere.be",
        "https://etalalumiere.be/contact/",
        "ETA La Lumière ASBL",
        "foi_contact",
        "tick2244; eta@lalumiere.be; +32 4 223 25 48; Boulevard Louis Hillier 1 4000 Liège",
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
        "name_nl": "ETA La Lumière VZW (Luik / maatwerk + Oeuvre Royale)",
        "name_fr": "ETA La Lumière ASBL (Liège / entreprise de travail adapté)",
        "name_en": "ETA La Lumière adapted-work ASBL (Liège Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://etalalumiere.be/",
        "foi_email": "eta@lalumiere.be",
        "foi_postal": "Boulevard Louis Hillier 1, 4000 Liège (siège Rue Sainte-Véronique 17)",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0402.345.211 Actief 2 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl LOSS DEEPEN {PN25} "
            f"equity DROP {EQ25} FTE JUMP {FTE25}; neerlegging 24.06.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; after APAM@2243; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_la_lumiere_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +18.38% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_la_lumiere_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +5.46% vs YE2024 {OM24}",
    ),
    (
        "bud_la_lumiere_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 LOSS DEEPEN",
        f"tick{TICK}; Medium CW; pnl LOSS DEEPEN {PN25} vs YE2024 {PN24} (-150.99%)",
    ),
    (
        "bud_la_lumiere_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -2.31% vs YE2024 {EQ24}",
    ),
    (
        "bud_la_lumiere_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 122.4",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_la_lumiere_fte_jr2024_statutory_cmp",
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
            "source_id": "src_la_lumiere_jr2025_cw_en",
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
            f"ETA La Lumière YE2025 leftover dual (bruto 7.25m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS DEEPEN / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Liège / AVIQ adapted-work + blind/low-vision services",
        "legal_basis": (
            "ASBL La Lumière / ETA (KBO 0402.345.211; Actief; 2 VE; NACE 88.993; Liège)"
        ),
        "decision_date": "2026-06-24",
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
            "https://www.companyweb.be/en/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes"
        ),
        "stated_goal": "Liège ETA mailing / packaging / printing / cannage",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl LOSS DEEPEN vs bruto JUMP +18%"
        ),
        "source_id": "src_la_lumiere_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>LaLumiere>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl LOSS DEEPEN {PN25}; FTE JUMP {FTE25}; 2 VE; after APAM@2243"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.2 (~7m), abs 7.7 (2.37x + LOSS DEEPEN), diff 3 → pi = 2.86+2.695+0.7 = 6.255 → 6.25
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"La Lumière bruto 7.25m / bruto≫omzet ~{RATIO}x / pnl LOSS DEEPEN "
            "(YE2025 Liège ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Liege>LaLumiere>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl LOSS DEEPEN {PN25} / "
            f"equity DROP {EQ25} / FTE JUMP {FTE25} / 2 VE Liège ETA"
        ),
        "confidence": "medium",
        "source_id": "src_la_lumiere_jr2025_cw_en",
        "beneficiaries": "ETA workers Liège / AVIQ adapted-work public path",
        "stated_goal": "Liège ETA mailing / packaging / printing",
        "measured_outcome": (
            f"omzet JUMP +5.46%; bruto≫omzet ~{RATIO}x; pnl LOSS DEEPEN {PN25}; "
            f"equity DROP -2.31%; FTE JUMP {FTE25}; filed 24.06.2026"
        ),
        "absurdity_score": "7.7",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.25",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "AVIQ ETA matrix; reconcile LOSS DEEPEN vs bruto JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after APAM@2243"
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
            "Wallonie>Liege>LaLumiere>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_deepen"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl LOSS DEEPEN EUR{PN25} vs YE2024 EUR{PN24}; "
            f"AVIQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Liège ETA ASBL (bruto 7.25m / omzet 3.06m / ~{RATIO}x / "
            "pnl LOSS DEEPEN) under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "ETA La Lumière ASBL",
        "recipient_email": "eta@lalumiere.be",
        "recipient_postal": "Boulevard Louis Hillier 1, 4000 Liège",
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
            "after APAM@2243"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2244",
    {
        "task_id": "rq_2244",
        "title": (
            f"leftover dual — ETA La Lumière YE2025 Medium (bruto 7.25m / bruto≫omzet "
            f"~{RATIO}x / pnl LOSS DEEPEN)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after APAM; named FREE La Lumière YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T02:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; La Lumière 0402.345.211 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl LOSS DEEPEN {PN25} equity DROP {EQ25} FTE JUMP {FTE25}; "
            "2 VE Liège ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after APAM@2243; do NOT redo APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123; "
            "next rq_2245; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2245",
    {
        "task_id": "rq_2245",
        "title": (
            "leftover dual after La Lumière — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after La Lumière YE2025 Medium (bruto 7.25m / bruto≫omzet ~{RATIO}x / "
            "pnl LOSS DEEPEN). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. Charles Lambert / APRE / Binche if YE2025 FREE; skip "
            "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). Do NOT redo La Lumière, "
            "APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, Metalgroup, "
            "EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, "
            "De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, "
            "Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} La Lumière; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
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
        "last_unit_id": "rq_2244",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover La Lumière 0402.345.211 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl LOSS DEEPEN {PN25}; equity DROP {EQ25}; FTE JUMP {FTE25}; 2 VE Liège ETA); "
            "after APAM@2243; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "next rq_2245; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — ETA La Lumière (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS DEEPEN)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** La Lumière / ETA ASBL — KBO **0402.345.211** (Actief; Rue Sainte-Véronique 17 / Boulevard Louis Hillier 1, 4000 Liège; **2 VE**; FTE {FTE25} CW; NACE **88.993**; Liège ETA)  
**recipient:** eta@lalumiere.be · Boulevard Louis Hillier 1, 4000 Liège  
**sources:** [CW EN](https://www.companyweb.be/en/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes) · [CW NL](https://www.companyweb.be/nl/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes) · [CW FR](https://www.companyweb.be/fr/0402345211/la-lumiere-oeuvre-royale-pour-personnes-aveugles-et-malvoyantes) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=402345211) · [site](https://etalalumiere.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **2 VE**; zetel Rue Sainte-Véronique Liège; NACE **88.993**; ETA site Hillier.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +5.46% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +18.38% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** LOSS DEEPEN vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -2.31%; FTE **{FTE25}** JUMP vs {FTE24}; filed **24.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After APAM@2243.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ETA La Lumière ASBL
via eta@lalumiere.be
Boulevard Louis Hillier 1, 4000 Liège
Objet: Publicité des comptes annuels 2025 La Lumière / ETA (BCE 0402.345.211)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL LOSS DEEPEN EUR{PN25} vs YE2024 EUR{PN24} — réconciliation avec bruto JUMP +18% et FTE JUMP {FTE25}.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts site Hillier / mailing / emballage / impression / cannage vs œuvre royale.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2244 ETA La Lumière Liège (bruto 7.25m / bruto≫omzet ~{RATIO}x / pnl LOSS DEEPEN / Medium)

- Unit: **rq_2244** leftover dual after **rq_2243 APAM**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE Liège ETA **La Lumière ASBL** YE2025 (KBO **0402.345.211**; Rue Sainte-Véronique 17 / Boulevard Louis Hillier 1 Liège; **Actief** **2 VE**; NACE **88.993** AViQ). Do not redo APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +5.46% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +18.38% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** LOSS DEEPEN vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP -2.31%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **24.06.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via eta@lalumiere.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.25); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2244=done + rq_2245 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2244/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2245 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} pnl={PN25} next=rq_2245")
