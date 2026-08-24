# tick2243 — leftover dual APAM Uccle YE2025 Medium (bruto 6.13m / ~3.08x / pnl PROFIT FLIP)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_apam_uccle"
TICK = "2243"
UTC = "2026-08-27T02:55:00Z"
GAP = "gap_apam_nbb_pdf_assets_debt_bruto_gt_omzet_3_08x_pnl_profit_flip_eta_matrix_l5"
COMM = "comm_apam_jr2025_statutory_eta_bruto_gt_omzet_pnl_profit_flip"
LB = "lb_apam_bruto_6_13m_gt_omzet_3_08x_pnl_profit_flip_jr2025"

OM25, OM24 = 1989997, 2096740
BR25, BR24 = 6131223, 5867908
PN25, PN24 = 268707, -3049
EQ25, EQ24 = 3214666, 2973275
FTE25, FTE24 = 184.1, 172.8
RATIO = round(BR25 / OM25, 2)  # ~3.08


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
        "src_apam_jr2025_cw_nl",
        "Companyweb NL APAM YE2025 statutory",
        "https://www.companyweb.be/nl/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet DROP {OM25} (-5.09%) bruto JUMP {BR25} (+4.49% "
            f"bruto≫omzet ~{RATIO}x) pnl PROFIT FLIP {PN25} vs YE2024 loss {PN24} "
            f"equity JUMP {EQ25} (+8.12%) FTE JUMP {FTE25}; filed 03-07-2026"
        ),
    ),
    (
        "src_apam_jr2025_cw_en",
        "Companyweb EN APAM YE2025 statutory",
        "https://www.companyweb.be/en/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 03-07-2026"
        ),
    ),
    (
        "src_apam_jr2025_cw_fr",
        "Companyweb FR APAM YE2025 statutory",
        "https://www.companyweb.be/fr/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_apam_kbo_2243",
        "KBO APAM 0406.772.468 Actief Uccle 2 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=406772468",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2243; Actief VZW/ASBL APAM; zetel Drogenbossesteenweg 130 1180 Ukkel; "
            "2 VE; NACE RSZ 88.993; Brussels ETA (PHARE)"
        ),
    ),
    (
        "src_apam_site_contact_2243",
        "APAM FOI channel info@apam.be",
        "https://apam.be/contact/",
        "APAM ASBL",
        "foi_contact",
        "tick2243; info@apam.be (handicap.brussels/autisme.brussels); +32 2 333 83 11; Chaussée de Drogenbos 130 1180 Uccle",
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
        "name_nl": "APAM VZW (Ukkel / Brussels ETA maatwerk)",
        "name_fr": "APAM ASBL (Uccle / entreprise de travail adapté bruxelloise)",
        "name_en": "APAM adapted-work ASBL (Uccle Brussels ETA)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "fr",
        "website": "https://apam.be/",
        "foi_email": "info@apam.be",
        "foi_postal": "Chaussée de Drogenbos 130, 1180 Uccle",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0406.772.468 Actief 2 VE "
            f"NACE 88.993; omzet DROP {OM25} bruto {BR25} (~{RATIO}x) pnl PROFIT FLIP {PN25} "
            f"equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 03.07.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; Jean Gielen already mined; after Le Perron@2242; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_apam_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +4.49% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_apam_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet DROP -5.09% vs YE2024 {OM24}",
    ),
    (
        "bud_apam_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 PROFIT FLIP",
        f"tick{TICK}; Medium CW; pnl PROFIT FLIP {PN25} vs YE2024 loss {PN24}",
    ),
    (
        "bud_apam_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +8.12% vs YE2024 {EQ24}",
    ),
    (
        "bud_apam_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 184.1",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_apam_fte_jr2024_statutory_cmp",
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
            "source_id": "src_apam_jr2025_cw_en",
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
            f"APAM YE2025 leftover dual (bruto 6.13m / bruto≫omzet ~{RATIO}x / "
            "pnl PROFIT FLIP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Brussels-Uccle / PHARE adapted-work public path",
        "legal_basis": (
            "ASBL ETA APAM (KBO 0406.772.468; Actief; 2 VE; NACE 88.993; Brussels PHARE)"
        ),
        "decision_date": "2026-07-03",
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
            "https://www.companyweb.be/en/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides"
        ),
        "stated_goal": "Brussels ETA packaging / mailing / recycling / green spaces",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl PROFIT FLIP vs omzet DROP"
        ),
        "source_id": "src_apam_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>Uccle>APAM>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl PROFIT FLIP {PN25}; FTE JUMP {FTE25}; 2 VE; after Le Perron@2242"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.2 (~6m), abs 7.8 (~3.08x + PROFIT FLIP), diff 3 → pi = 2.86+2.73+0.7 = 6.29 → 6.30
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"APAM bruto 6.13m / bruto≫omzet ~{RATIO}x / pnl PROFIT FLIP "
            "(YE2025 Brussels ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Bruxelles>Uccle>APAM>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl PROFIT FLIP {PN25} / "
            f"equity JUMP {EQ25} / FTE JUMP {FTE25} / 2 VE Brussels ETA"
        ),
        "confidence": "medium",
        "source_id": "src_apam_jr2025_cw_en",
        "beneficiaries": "ETA workers Brussels-Uccle / PHARE adapted-work public path",
        "stated_goal": "Brussels ETA packaging / mailing / recycling",
        "measured_outcome": (
            f"omzet DROP -5.09%; bruto≫omzet ~{RATIO}x; pnl PROFIT FLIP {PN25}; "
            f"equity JUMP +8.12%; FTE JUMP {FTE25}; filed 03.07.2026"
        ),
        "absurdity_score": "7.8",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "PHARE ETA matrix; reconcile PROFIT FLIP vs omzet DROP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Jean Gielen already mined; after Le Perron@2242"
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
            "Bruxelles>Uccle>APAM>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_profit_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl PROFIT FLIP EUR{PN25} vs YE2024 loss EUR{PN24}; "
            f"PHARE ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels ETA ASBL (bruto 6.13m / omzet 1.99m / ~{RATIO}x / "
            "pnl PROFIT FLIP) under PHARE path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "APAM ASBL",
        "recipient_email": "info@apam.be",
        "recipient_postal": "Chaussée de Drogenbos 130, 1180 Uccle",
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
            "Jean Gielen already mined; after Le Perron@2242"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2243",
    {
        "task_id": "rq_2243",
        "title": (
            f"leftover dual — APAM YE2025 Medium (bruto 6.13m / bruto≫omzet "
            f"~{RATIO}x / pnl PROFIT FLIP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Le Perron; unused FREE Brussels ETA APAM YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T02:40:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; APAM 0406.772.468 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl PROFIT FLIP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; "
            "2 VE Brussels ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "Jean Gielen already mined; after Le Perron@2242; do NOT redo Le Perron/L'Atelier/"
            "Axedis/ETA123/Manufast/Jean Gielen; next rq_2244; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2244",
    {
        "task_id": "rq_2244",
        "title": (
            "leftover dual after APAM — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after APAM YE2025 Medium (bruto 6.13m / bruto≫omzet ~{RATIO}x / "
            "pnl PROFIT FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. La Lumière / Charles Lambert if YE2025 FREE; skip APAM/"
            "Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). Do NOT redo APAM, Jean Gielen, Le Perron, "
            "L'Atelier, Axedis, ETA 123 Beauraing, Manufast, Metalgroup, EntrAnam, Enghien, Entra, "
            "Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, "
            "De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, Kemphaan, Mirto, Blankedale, "
            "Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} APAM; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
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
        "last_unit_id": "rq_2243",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover APAM 0406.772.468 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl PROFIT FLIP {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 2 VE Brussels ETA); "
            "after Le Perron@2242; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "Jean Gielen already mined; next rq_2244; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — APAM Uccle (NBB PDF / bruto≫omzet ~{RATIO}x / pnl PROFIT FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** APAM ASBL — KBO **0406.772.468** (Actief; Chaussée de Drogenbos 130, 1180 Uccle; **2 VE**; FTE {FTE25} CW; NACE **88.993**; Brussels ETA PHARE)  
**recipient:** info@apam.be · Chaussée de Drogenbos 130, 1180 Uccle  
**sources:** [CW EN](https://www.companyweb.be/en/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides) · [CW NL](https://www.companyweb.be/nl/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides) · [CW FR](https://www.companyweb.be/fr/0406772468/atelier-pour-l-acces-des-moins-valides-au-monde-du-travail-e-t-a-pour-moins-valides) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=406772468) · [site](https://apam.be/contact/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL APAM; **2 VE**; zetel Drogenbossesteenweg/Chaussée de Drogenbos Ukkel; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** DROP -5.09% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +4.49% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** PROFIT FLIP vs YE2024 loss EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +8.12%; FTE **{FTE25}** JUMP vs {FTE24}; filed **03.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Jean Gielen already mined. After Le Perron@2242.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: APAM ASBL
via info@apam.be
Chaussée de Drogenbos 130, 1180 Uccle
Objet: Publicité des comptes annuels 2025 APAM (BCE 0406.772.468)

Madame, Monsieur,

Sur la base de l'ordonnance bruxelloise relative à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL PROFIT FLIP EUR{PN25} vs YE2024 perte EUR{PN24} — réconciliation avec omzet DROP et FTE JUMP {FTE25}.
4. Matrice des subsides PHARE / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts sites / conditionnement / mailing / recyclage / espaces verts.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2243 APAM Uccle (bruto 6.13m / bruto≫omzet ~{RATIO}x / pnl PROFIT FLIP / Medium)

- Unit: **rq_2243** leftover dual after **rq_2242 Le Perron**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Jean Gielen already mined@race. Took FREE unused Brussels ETA **APAM ASBL** YE2025 (KBO **0406.772.468**; Chaussée de Drogenbos 130 Uccle; **Actief** **2 VE**; NACE **88.993** PHARE). Do not redo Le Perron/L'Atelier/Axedis/ETA123/Jean Gielen/Manufast stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP -5.09% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +4.49% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** PROFIT FLIP vs YE2024 loss EUR{PN24}; equity **EUR{EQ25}** JUMP +8.12%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **03.07.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@apam.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2243=done + rq_2244 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2243/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2244 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} pnl={PN25} next=rq_2244")
