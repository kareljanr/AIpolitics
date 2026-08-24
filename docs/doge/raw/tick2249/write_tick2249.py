# tick2249 — leftover dual Serviplast YE2025 Medium (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "sc_serviplast_bastogne"
TICK = "2249"
UTC = "2026-08-27T04:25:00Z"
GAP = "gap_serviplast_nbb_pdf_assets_debt_pnl_loss_deepen_fte_drop_eta_matrix_l5"
COMM = "comm_serviplast_jr2025_statutory_eta_omzet_pnl_loss_deepen_fte_drop"
LB = "lb_serviplast_omzet_5_85m_pnl_loss_deepen_fte_drop_jr2025"

OM25, OM24 = 5851312, 6171128
BR25, BR24 = 3087393, 3152125
PN25, PN24 = -353097, -322911
EQ25, EQ24 = 4562608, 4955499
FTE25, FTE24 = 144.1, 157.5


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
        "src_serviplast_jr2025_cw_nl",
        "Companyweb NL Serviplast YE2025 statutory",
        "https://www.companyweb.be/nl/0416287970/serviplast",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet DROP {OM25} (-5.18%) bruto DROP {BR25} (-2.05%) "
            f"pnl LOSS DEEPEN {PN25} equity DROP {EQ25} (-7.93%) FTE DROP {FTE25}; filed 18-05-2026"
        ),
    ),
    (
        "src_serviplast_jr2025_cw_en",
        "Companyweb EN Serviplast YE2025 statutory",
        "https://www.companyweb.be/en/0416287970/serviplast",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 18-05-2026"
        ),
    ),
    (
        "src_serviplast_jr2025_cw_fr",
        "Companyweb FR Serviplast YE2025 statutory",
        "https://www.companyweb.be/fr/0416287970/serviplast",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_serviplast_kbo_2249",
        "KBO Serviplast 0416.287.970 Actief Bastogne 2 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=416287970",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2249; Actief SC SERVIPLAST; zetel Rue du Marché Couvert 42 6600 Bastogne; "
            "2 VE; NACE RSZ 88.993; Walloon ETA Luxembourg province"
        ),
    ),
    (
        "src_serviplast_site_contact_2249",
        "Serviplast FOI channel info@serviplast.be",
        "https://www.serviplast.be/",
        "Serviplast SC",
        "foi_contact",
        "tick2249; info@serviplast.be; +32 61 24 06 70; Rue du Marché Couvert 42 6600 Bastogne",
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
        "name_nl": "Serviplast SC (Bastenaken / ETA kunststofinjectie)",
        "name_fr": "Serviplast SC (Bastogne / entreprise de travail adapté injection plastique)",
        "name_en": "Serviplast adapted-work SC (Bastogne Walloon ETA plastics)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.serviplast.be/",
        "foi_email": "info@serviplast.be",
        "foi_postal": "Rue du Marché Couvert 42, 6600 Bastogne",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0416.287.970 Actief 2 VE "
            f"NACE 88.993; omzet DROP {OM25} bruto {BR25} pnl LOSS DEEPEN {PN25} equity DROP "
            f"{EQ25} FTE DROP {FTE25}; neerlegging 18.05.2026; assets/debt Unknown; FOI {GAP}; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Jean Del'Cour@2248; deferred FREE Saupont/Dauphins; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_serviplast_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025 (primary commercial)",
        f"tick{TICK}; Medium CW; omzet DROP -5.18% vs YE2024 {OM24}",
    ),
    (
        "bud_serviplast_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto DROP -2.05% vs YE2024 {BR24}",
    ),
    (
        "bud_serviplast_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 LOSS DEEPEN",
        f"tick{TICK}; Medium CW; pnl LOSS DEEPEN {PN25} vs YE2024 {PN24}",
    ),
    (
        "bud_serviplast_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -7.93% vs YE2024 {EQ24}",
    ),
    (
        "bud_serviplast_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 144.1",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_serviplast_fte_jr2024_statutory_cmp",
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
            "source_id": "src_serviplast_jr2025_cw_en",
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
            "Serviplast YE2025 leftover dual (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Bastogne / AVIQ adapted-work public path",
        "legal_basis": (
            "SC ETA Serviplast (KBO 0416.287.970; Actief; 2 VE; NACE 88.993; Bastogne)"
        ),
        "decision_date": "2026-05-18",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": (
            f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},'
            f'"2025_equity":{EQ25},"2025_fte":{FTE25},"2024_omzet":{OM24},'
            f'"2024_bruto":{BR24},"2024_pnl":{PN24},"2024_fte":{FTE24}}}'
        ),
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0416287970/serviplast",
        "stated_goal": "Walloon ETA plastic injection / packaging / green spaces",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; reconcile pnl LOSS DEEPEN + FTE DROP "
            "vs AVIQ ETA subsidy matrix"
        ),
        "source_id": "src_serviplast_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Luxembourg>Bastogne>Serviplast>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope {OM25}; pnl LOSS DEEPEN {PN25}; "
            f"FTE DROP {FTE25}; 2 VE; after Jean Del'Cour@2248"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.2 (omzet ~5.85m), abs 7.6, diff 3 → pi = 2.86+2.66+0.7 = 6.22 → 6.20
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Serviplast omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1 (YE2025 Walloon ETA)"
        ),
        "level": "L5",
        "type": "eta_sc_statutory",
        "hierarchy_path": "Wallonie>Luxembourg>Bastogne>Serviplast>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet {OM25} / bruto {BR25} / pnl LOSS DEEPEN {PN25} / "
            f"equity DROP {EQ25} / FTE DROP {FTE25} / 2 VE Walloon ETA"
        ),
        "confidence": "medium",
        "source_id": "src_serviplast_jr2025_cw_en",
        "beneficiaries": "ETA workers Bastogne / AVIQ adapted-work public path",
        "stated_goal": "Walloon ETA plastic injection",
        "measured_outcome": (
            f"omzet DROP -5.18%; pnl LOSS DEEPEN {PN25}; equity DROP -7.93%; "
            f"FTE DROP {FTE25}; filed 18.05.2026"
        ),
        "absurdity_score": "7.6",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.20",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose AVIQ ETA matrix; "
            "reconcile LOSS DEEPEN + FTE DROP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Jean Del'Cour@2248; deferred FREE Saupont/Dauphins"
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
            "Wallonie>Luxembourg>Bastogne>Serviplast>NBB_PDF_assets_debt_pnl_loss_deepen_fte_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); omzet EUR{OM25} / "
            f"bruto EUR{BR25}; pnl LOSS DEEPEN EUR{PN25} vs YE2024 EUR{PN24}; "
            f"FTE DROP {FTE25} vs {FTE24}; AVIQ ETA subsidy matrix"
        ),
        "why_it_matters": (
            "Medium CW shows Walloon ETA SC (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1) "
            "under AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Serviplast SC",
        "recipient_email": "info@serviplast.be",
        "recipient_postal": "Rue du Marché Couvert 42, 6600 Bastogne",
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
            "after Jean Del'Cour@2248; deferred FREE Saupont/Dauphins"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2249",
    {
        "task_id": "rq_2249",
        "title": (
            "leftover dual — Serviplast YE2025 Medium (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Jean Del'Cour; named FREE Serviplast YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T04:10:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Serviplast 0416.287.970 YE2025 Medium CW; omzet DROP {OM25} bruto {BR25} "
            f"pnl LOSS DEEPEN {PN25} equity DROP {EQ25} FTE DROP {FTE25}; "
            "2 VE Bastogne ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Jean Del'Cour@2248; deferred FREE Saupont/Dauphins; do NOT redo Jean Del'Cour/"
            "TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM; next rq_2250 EVERY-10; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2250",
    {
        "task_id": "rq_2250",
        "title": (
            "EVERY-10 + leftover dual after Serviplast — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 mandatory: refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
            "Then leftover dual after Serviplast YE2025 Medium (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
            "if YE2025, else Heropbeuring if NBB/CW euros live, else unused ETA/VAPH/WZC/maatwerk "
            "(e.g. Le Saupont / Les Dauphins if YE2025 FREE; skip Serviplast/Jean Del'Cour/TRAVCO/Pilifs/"
            "Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). "
            "Do NOT redo Serviplast, Jean Del'Cour, TRAVCO, Pilifs, Jeunes Jardiniers, La Lumière, APAM, "
            "Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, Metalgroup, EntrAnam, "
            "Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, "
            "Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, Kemphaan, Mirto, "
            "Blankedale, Werkmmaat. Next EVERY-10 after this: 2260."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Serviplast; EVERY-10@2250 MANDATORY; FARO/AIESH/REW YE2024; "
            "AGB Bornem JR2024; Heropbeuring CW opaque; deferred FREE Saupont/Dauphins"
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
        "last_unit_id": "rq_2249",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover Serviplast 0416.287.970 Medium (omzet DROP {OM25}; "
            f"pnl LOSS DEEPEN {PN25}; equity DROP {EQ25}; FTE DROP {FTE25}; 2 VE Bastogne ETA); "
            "after Jean Del'Cour@2248; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE Saupont/Dauphins; next rq_2250 EVERY-10; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — Serviplast (NBB PDF / pnl LOSS DEEPEN / FTE DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Serviplast SC — KBO **0416.287.970** (Actief; Rue du Marché Couvert 42, 6600 Bastogne; **2 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon ETA Bastogne)  
**recipient:** info@serviplast.be · Rue du Marché Couvert 42, 6600 Bastogne  
**sources:** [CW EN](https://www.companyweb.be/en/0416287970/serviplast) · [CW NL](https://www.companyweb.be/nl/0416287970/serviplast) · [CW FR](https://www.companyweb.be/fr/0416287970/serviplast) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=416287970) · [site](https://www.serviplast.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief SC SERVIPLAST; **2 VE**; zetel Bastogne; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** DROP -5.18% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP -2.05%; pnl **EUR{PN25:,}** LOSS DEEPEN vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -7.93%; FTE **{FTE25}** DROP vs {FTE24}; filed **18.05.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Jean Del'Cour@2248. Deferred FREE Saupont/Dauphins.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Serviplast SC
via info@serviplast.be
Rue du Marché Couvert 42, 6600 Bastogne
Objet: Publicité des comptes annuels 2025 Serviplast (BCE 0416.287.970)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition chiffre d'affaires EUR{OM25} / marge brute EUR{BR25}.
3. PnL LOSS DEEPEN EUR{PN25} vs YE2024 EUR{PN24} — réconciliation avec FTE DROP {FTE25}.
4. Matrice des subsides AVIQ / ETA derrière les charges de personnel.
5. Répartition coûts injection plastique / conditionnement / espaces verts.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2249 Serviplast Bastogne (omzet 5.85m / pnl LOSS DEEPEN / FTE DROP 144.1 / Medium)

- Unit: **rq_2249** leftover dual after **rq_2248 Jean Del'Cour**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE Walloon ETA **Serviplast SC** YE2025 (KBO **0416.287.970**; Rue du Marché Couvert 42 Bastogne; **Actief** **2 VE**; NACE **88.993** AViQ). Deferred FREE Le Saupont/Les Dauphins. Do not redo Jean Del'Cour/TRAVCO/Pilifs/Jeunes Jardiniers/La Lumière/APAM stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP -5.18% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -2.05%; pnl **EUR{PN25}** LOSS DEEPEN vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP -7.93%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **18.05.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@serviplast.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2249=done + rq_2250 open (EVERY-10); loop_state ticks={TICK}; raw docs/doge/raw/tick2249/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250** MUST refresh progress + waste top10). Next: rq_2250.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; omzet={OM25} pnl={PN25} next=rq_2250 EVERY-10")
