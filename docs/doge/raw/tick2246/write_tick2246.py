# tick2246 — leftover dual La Ferme Nos Pilifs YE2025 Medium (bruto 7.68m / ~1.43x / pnl JUMP +401% / FTE JUMP 224)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_ferme_nos_pilifs_bruxelles"
TICK = "2246"
UTC = "2026-08-27T03:40:00Z"
GAP = "gap_pilifs_nbb_pdf_assets_debt_bruto_gt_omzet_1_43x_pnl_jump_401pct_fte_jump_eta_matrix_l5"
COMM = "comm_pilifs_jr2025_statutory_eta_bruto_gt_omzet_pnl_jump_fte_jump"
LB = "lb_pilifs_bruto_7_68m_gt_omzet_1_43x_pnl_jump_401pct_fte_jump_jr2025"

OM25, OM24 = 5371265, 5369502
BR25, BR24 = 7682582, 7656007
PN25, PN24 = 184476, 36797
EQ25, EQ24 = 2386868, 2276135
FTE25, FTE24 = 224.0, 216.1
RATIO = round(BR25 / OM25, 2)  # ~1.43


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
        "src_pilifs_jr2025_cw_nl",
        "Companyweb NL La Ferme Nos Pilifs YE2025 statutory",
        "https://www.companyweb.be/nl/0438065757/la-ferme-nos-pilifs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+0.03%) bruto JUMP {BR25} (+0.35% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+401.34%) equity JUMP {EQ25} (+4.86%) "
            f"FTE JUMP {FTE25}; filed 10-07-2026"
        ),
    ),
    (
        "src_pilifs_jr2025_cw_en",
        "Companyweb EN La Ferme Nos Pilifs YE2025 statutory",
        "https://www.companyweb.be/en/0438065757/la-ferme-nos-pilifs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 10-07-2026"
        ),
    ),
    (
        "src_pilifs_jr2025_cw_fr",
        "Companyweb FR La Ferme Nos Pilifs YE2025 statutory",
        "https://www.companyweb.be/fr/0438065757/la-ferme-nos-pilifs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Bénéfice {PN25}",
    ),
    (
        "src_pilifs_kbo_2246",
        "KBO La Ferme Nos Pilifs 0438.065.757 Actief Bruxelles 3 VE",
        "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=438065757",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2246; Actief VZW/ASBL LA FERME NOS PILIFS; zetel Trassersweg 347-349 1120 Brussel; "
            "3 VE; NACE RSZ 88.993; Brussels ETA PHARE/COCOF; info@pilifs.be"
        ),
    ),
    (
        "src_pilifs_site_contact_2246",
        "La Ferme Nos Pilifs FOI channel info@pilifs.be",
        "https://www.fermenospilifs.be/contact",
        "La Ferme Nos Pilifs ASBL",
        "foi_contact",
        "tick2246; info@pilifs.be; compta@pilifs.be; +32 2 262 11 06; Trassersweg 347 1120 Bruxelles",
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
        "name_nl": "La Ferme Nos Pilifs VZW (Brussel NOH / Brussels ETA boerderij)",
        "name_fr": "La Ferme Nos Pilifs ASBL (Bruxelles NOH / entreprise de travail adapté)",
        "name_en": "La Ferme Nos Pilifs adapted-work ASBL (Brussels NOH ETA farm)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "fr",
        "website": "https://www.fermenospilifs.be/",
        "foi_email": "info@pilifs.be",
        "foi_postal": "Trassersweg 347-349, 1120 Bruxelles",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0438.065.757 Actief 3 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} (+401%) "
            f"equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 10.07.2026; assets/debt Unknown; "
            f"FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; after Jeunes Jardiniers@2245; deferred FREE TRAVCO; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_pilifs_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +0.35% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_pilifs_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +0.03% vs YE2024 {OM24}",
    ),
    (
        "bud_pilifs_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory pnl YE2025 JUMP",
        f"tick{TICK}; Medium CW; pnl JUMP +401.34% vs YE2024 {PN24}",
    ),
    (
        "bud_pilifs_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +4.86% vs YE2024 {EQ24}",
    ),
    (
        "bud_pilifs_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 224",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_pilifs_fte_jr2024_statutory_cmp",
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
            "source_id": "src_pilifs_jr2025_cw_en",
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
            f"La Ferme Nos Pilifs YE2025 leftover dual (bruto 7.68m / bruto≫omzet ~{RATIO}x / "
            "pnl JUMP +401% / FTE JUMP 224 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Brussels-NOH / PHARE-COCOF adapted-work public path",
        "legal_basis": (
            "ASBL ETA La Ferme Nos Pilifs (KBO 0438.065.757; Actief; 3 VE; NACE 88.993; Brussels)"
        ),
        "decision_date": "2026-07-10",
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
        "evaluation_url": "https://www.companyweb.be/en/0438065757/la-ferme-nos-pilifs",
        "stated_goal": "Brussels ETA farm / gardens / bakery / grocery / green spaces",
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{RATIO}x; "
            "reconcile pnl JUMP +401% vs FTE JUMP 224"
        ),
        "source_id": "src_pilifs_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>NOH>Pilifs>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl JUMP {PN25}; FTE JUMP {FTE25}; 3 VE; after Jeunes Jardiniers@2245"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# cost 5.2, abs 7.2, diff 3 → pi = 2.86+2.52+0.7 = 6.08 → 6.10
lb_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"Pilifs bruto 7.68m / bruto≫omzet ~{RATIO}x / pnl JUMP +401% / FTE JUMP 224 "
            "(YE2025 Brussels ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Bruxelles>NOH>Pilifs>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} (+401%) / "
            f"equity JUMP {EQ25} / FTE JUMP {FTE25} / 3 VE Brussels ETA"
        ),
        "confidence": "medium",
        "source_id": "src_pilifs_jr2025_cw_en",
        "beneficiaries": "ETA workers Brussels-NOH / PHARE-COCOF adapted-work public path",
        "stated_goal": "Brussels ETA farm / gardens / bakery",
        "measured_outcome": (
            f"omzet JUMP +0.03%; bruto≫omzet ~{RATIO}x; pnl JUMP +401%; "
            f"equity JUMP +4.86%; FTE JUMP {FTE25}; filed 10.07.2026"
        ),
        "absurdity_score": "7.2",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "6.10",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{RATIO}x vs "
            "PHARE ETA matrix; reconcile pnl JUMP +401% vs FTE JUMP"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} primary; Medium CW; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Jeunes Jardiniers@2245; deferred FREE TRAVCO"
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
            "Bruxelles>NOH>Pilifs>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_jump_fte_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl JUMP EUR{PN25} (+401% vs YE2024 EUR{PN24}); "
            f"FTE JUMP {FTE25} vs {FTE24}; PHARE ETA subsidy matrix behind bruto {BR25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels ETA ASBL (bruto 7.68m / omzet 5.37m / ~{RATIO}x / "
            "pnl JUMP +401% / FTE JUMP 224) under PHARE path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "La Ferme Nos Pilifs ASBL",
        "recipient_email": "info@pilifs.be",
        "recipient_postal": "Trassersweg 347-349, 1120 Bruxelles",
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
            "after Jeunes Jardiniers@2245; deferred FREE TRAVCO"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2246",
    {
        "task_id": "rq_2246",
        "title": (
            f"leftover dual — La Ferme Nos Pilifs YE2025 Medium (bruto 7.68m / bruto≫omzet "
            f"~{RATIO}x / pnl JUMP +401% / FTE JUMP 224)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Jeunes Jardiniers; named FREE Pilifs YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T03:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Pilifs 0438.065.757 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl JUMP {PN25} (+401%) equity JUMP {EQ25} FTE JUMP {FTE25}; "
            "3 VE Brussels ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "after Jeunes Jardiniers@2245; deferred FREE TRAVCO; do NOT redo Jeunes Jardiniers/"
            "La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123; next rq_2247; next EVERY-10 2250"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2247",
    {
        "task_id": "rq_2247",
        "title": (
            "leftover dual after Pilifs — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            f"leftover dual after Pilifs YE2025 Medium (bruto 7.68m / bruto≫omzet ~{RATIO}x / "
            "pnl JUMP +401% / FTE JUMP 224). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
            "TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "ETA/VAPH/WZC/maatwerk (e.g. TRAVCO if YE2025 FREE; skip Pilifs/Jeunes Jardiniers/La Lumière/"
            "APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123). Do NOT redo Pilifs, Jeunes Jardiniers, "
            "La Lumière, APAM, Jean Gielen, Le Perron, L'Atelier, Axedis, ETA 123 Beauraing, Manufast, "
            "Metalgroup, EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, "
            "SDB, De Vleugels, Kiemkracht, De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, "
            "Kemphaan, Mirto, Blankedale, Werkmmaat. Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Pilifs; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; deferred FREE TRAVCO; next every-10 2250"
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
        "last_unit_id": "rq_2246",
        "ticks_completed": TICK,
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover Pilifs 0438.065.757 Medium (bruto {BR25} ~{RATIO}x omzet "
            f"{OM25}; pnl JUMP {PN25} +401%; equity JUMP {EQ25}; FTE JUMP {FTE25}; 3 VE Brussels ETA); "
            "after Jeunes Jardiniers@2245; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE TRAVCO; next rq_2247; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

draft = f"""# FOI draft — La Ferme Nos Pilifs (NBB PDF / bruto≫omzet ~{RATIO}x / pnl JUMP +401% / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** La Ferme Nos Pilifs ASBL — KBO **0438.065.757** (Actief; Trassersweg 347-349, 1120 Bruxelles; **3 VE**; FTE {FTE25} CW; NACE **88.993**; Brussels ETA PHARE/COCOF)  
**recipient:** info@pilifs.be · Trassersweg 347-349, 1120 Bruxelles  
**sources:** [CW EN](https://www.companyweb.be/en/0438065757/la-ferme-nos-pilifs) · [CW NL](https://www.companyweb.be/nl/0438065757/la-ferme-nos-pilifs) · [CW FR](https://www.companyweb.be/fr/0438065757/la-ferme-nos-pilifs) · [KBO](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?lang=nl&nummer=438065757) · [site](https://www.fermenospilifs.be/contact)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **3 VE**; zetel Trassersweg Bruxelles-NOH; NACE **88.993**; info@pilifs.be.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +0.03% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +0.35% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +401.34% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +4.86%; FTE **{FTE25}** JUMP vs {FTE24}; filed **10.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Jeunes Jardiniers@2245. Deferred FREE TRAVCO.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: La Ferme Nos Pilifs ASBL
via info@pilifs.be
Trassersweg 347-349, 1120 Bruxelles
Objet: Publicité des comptes annuels 2025 La Ferme Nos Pilifs (BCE 0438.065.757)

Madame, Monsieur,

Sur la base de l'ordonnance bruxelloise relative à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL JUMP EUR{PN25} (+401% vs YE2024 EUR{PN24}) — réconciliation avec FTE JUMP {FTE25}.
4. Matrice des subsides PHARE/COCOF / ETA derrière la marge brute EUR{BR25}.
5. Répartition coûts ferme / jardinerie / boulangerie / épicerie / équipes jardin.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
"""
(FOI_DRAFTS / f"{GAP}.md").write_text(draft, encoding="utf-8")

log_block = f"""

## Tick {TICK} - {UTC} - rq_2246 La Ferme Nos Pilifs Bruxelles (bruto 7.68m / bruto≫omzet ~{RATIO}x / pnl JUMP +401% / FTE JUMP 224 / Medium)

- Unit: **rq_2246** leftover dual after **rq_2245 Jeunes Jardiniers**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE Brussels ETA **La Ferme Nos Pilifs ASBL** YE2025 (KBO **0438.065.757**; Trassersweg 347-349 Bruxelles-NOH; **Actief** **3 VE**; NACE **88.993** PHARE/COCOF). Deferred FREE TRAVCO. Do not redo Jeunes Jardiniers/La Lumière/APAM/Jean Gielen/Le Perron/L'Atelier/Axedis/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +0.03% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +0.35% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +401.34% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +4.86%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **10.07.2026**. Strong KBO Actief 3 VE. Assets/debt Unknown. Medium. FOI via info@pilifs.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.10); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2246=done + rq_2247 open; loop_state ticks={TICK}; raw docs/doge/raw/tick2246/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2247 (AGB/FARO-if-YE2025 / AIESH-REW / unused TRAVCO).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(f"tick{TICK} done; bruto={BR25} ratio~{RATIO} pnl={PN25} next=rq_2247")
