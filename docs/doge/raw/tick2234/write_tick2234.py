# tick2234 — Ateliers de Tertre YE2025 Medium leftover dual (FREE unused ETA)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_ateliers_de_tertre"
TICK = "2234"
UTC = "2026-08-26T23:50:00Z"
GAP = "gap_ateliers_tertre_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_97pct_eta_matrix_l5"
COMM = "comm_ateliers_tertre_jr2025_statutory_eta_omzet_jump_pnl_drop_97pct"
LB = "lb_ateliers_tertre_omzet_10_00m_pnl_drop_97pct_bruto_gt_omzet_jr2025"

OM25, OM24 = 9998674, 8827596
BR25, BR24 = 13109077, 12268665
PN25, PN24 = 41123, 1486084
EQ25, EQ24 = 9639449, 9680279
FTE25, FTE24 = 335.9, 327.8
RATIO = round(BR25 / OM25, 2)  # ~1.31


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
        "src_ateliers_tertre_jr2025_cw_nl",
        "Companyweb NL Ateliers de Tertre YE2025 statutory",
        "https://www.companyweb.be/nl/0407799084/ateliers-de-tertre",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+13.27%) bruto JUMP {BR25} (+6.85% "
            f"bruto≫omzet ~{RATIO}x) pnl DROP {PN25} (-97.23%) equity DROP {EQ25} "
            f"FTE {FTE25}; filed 16-06-2026"
        ),
    ),
    (
        "src_ateliers_tertre_jr2025_cw_en",
        "Companyweb EN Ateliers de Tertre YE2025 statutory",
        "https://www.companyweb.be/en/0407799084/ateliers-de-tertre",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 16-06-2026"
        ),
    ),
    (
        "src_ateliers_tertre_jr2025_cw_fr",
        "Companyweb FR Ateliers de Tertre YE2025 statutory",
        "https://www.companyweb.be/fr/0407799084/ateliers-de-tertre",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_ateliers_tertre_kbo_2234",
        "KBO Ateliers de Tertre 0407.799.084 Actief Saint-Ghislain 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407799084",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2234; Actief ASBL; zetel Rue Olivier Lhoir(T) 97 7333 Saint-Ghislain; 1 VE; "
            "NACE RSZ/BTW 88.993; erkenning aannemer van werken"
        ),
    ),
    (
        "src_ateliers_tertre_site_contact_2234",
        "Ateliers de Tertre FOI channel info@etater.be",
        "https://etater.be/",
        "ASBL Ateliers de Tertre",
        "foi_contact",
        "tick2234; info@etater.be; 065 76 03 60; Rue Olivier Lhoir 97 7333 Tertre/Saint-Ghislain",
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
            "accessed_date": "2026-08-26",
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
        "name_nl": "Ateliers de Tertre ASBL (Saint-Ghislain / ETA maatwerk)",
        "name_fr": "ASBL Ateliers de Tertre (Saint-Ghislain / entreprise de travail adapte)",
        "name_en": "Ateliers de Tertre adapted-work ASBL (Saint-Ghislain ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://etater.be/",
        "foi_email": "info@etater.be",
        "foi_postal": "Rue Olivier Lhoir(T) 97, 7333 Saint-Ghislain",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.799.084 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl DROP {PN25} "
            f"(-97.23%) equity flat DROP {EQ25} FTE JUMP {FTE25}; neerlegging 16.06.2026; "
            f"assets/debt Unknown; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/"
            "AIESH/REW YE2024; Heropbeuring CW opaque; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_ateliers_tertre_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +13.27% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_ateliers_tertre_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +6.85% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_ateliers_tertre_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -97.23% vs YE2024 {PN24}",
    ),
    (
        "bud_ateliers_tertre_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -0.42% vs YE2024 {EQ24}",
    ),
    (
        "bud_ateliers_tertre_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 335.9",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_ateliers_tertre_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative",
        f"tick{TICK}; YE2024 pnl {PN24} comparative (pre DROP -97%)",
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
            "source_id": "src_ateliers_tertre_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Ateliers de Tertre YE2025 leftover dual (omzet JUMP 10.00m / bruto≫omzet "
            "~1.31x / pnl DROP -97% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Hainaut (Saint-Ghislain/Tertre) / Walloon adapted-work public path"
        ),
        "legal_basis": (
            "ASBL ETA (KBO 0407.799.084; Actief; 1 VE; NACE 88.993; erkenning aannemer)"
        ),
        "decision_date": "2026-06-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0407799084/ateliers-de-tertre",
        "stated_goal": "Adapted work / ETA multi-pole (palettes metal cleaning titres-services)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.31x; reconcile pnl "
            "DROP -97% (1.49m->41k) despite omzet JUMP +13% and FTE JUMP; AWIPH/AVIQ ETA "
            "subsidy matrix; pole cost allocation"
        ),
        "source_id": "src_ateliers_tertre_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>SaintGhislain>AteliersTertre>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope {OM25}; bruto≫omzet ~{RATIO}x; "
            f"pnl DROP -97.23%; FTE JUMP {FTE25}; 1 VE; after Le Rucher@2233; AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; not TE-additive"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Ateliers de Tertre omzet JUMP 10.00m / pnl DROP -97% / bruto≫omzet ~1.31x "
            "(YE2025 ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Hainaut>SaintGhislain>AteliersTertre>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} (~{RATIO}x) / pnl DROP {PN25} (-97.23% from "
            f"{PN24}) / equity {EQ25} / FTE JUMP {FTE25} / 1 VE Tertre ETA"
        ),
        "confidence": "medium",
        "source_id": "src_ateliers_tertre_jr2025_cw_en",
        "beneficiaries": "ETA workers Hainaut / Walloon adapted-work public path",
        "stated_goal": "Adapted work / ETA multi-pole",
        "measured_outcome": (
            f"omzet JUMP +13.27%; bruto≫omzet ~{RATIO}x; pnl crater -97.23% (1.49m->41k); "
            f"equity flat -0.42%; FTE JUMP {FTE25}; 1 VE; filed 16.06.2026"
        ),
        "absurdity_score": "7.5",
        "cost_score": "5.8",
        "difficulty": "3.0",
        "priority_index": "6.50",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.31x vs AWIPH/AVIQ "
            "ETA subsidy matrix; reconcile pnl DROP -97% despite omzet+FTE growth; pole cost "
            "allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Le Rucher@2233; next every-10 2240"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>SaintGhislain>AteliersTertre>NBB_PDF_assets_debt_pnl_drop_97pct_eta"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl DROP EUR{PN25} vs YE2024 EUR{PN24} (-97.23%) "
            f"despite omzet/FTE JUMP; AWIPH/AVIQ ETA subsidy matrix; multi-pole cost allocation"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL (omzet ~10.00m / bruto 13.11m / {FTE25} FTE) "
            "with pnl crater -97% under public adapted-work path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "ASBL Ateliers de Tertre",
        "recipient_email": "info@etater.be",
        "recipient_postal": "Rue Olivier Lhoir(T) 97, 7333 Saint-Ghislain",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/"
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Ateliers de Tertre (NBB PDF / pnl DROP −97% / bruto≫omzet ~{RATIO}x)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ASBL Ateliers de Tertre — KBO **0407.799.084** (Actief; Rue Olivier Lhoir(T) 97, 7333 Saint-Ghislain; **1 VE**; FTE {FTE25} CW; NACE **88.993** ETA)  
**recipient:** info@etater.be · Rue Olivier Lhoir 97, 7333 Tertre  
**sources:** [CW EN](https://www.companyweb.be/en/0407799084/ateliers-de-tertre) · [CW NL](https://www.companyweb.be/nl/0407799084/ateliers-de-tertre) · [CW FR](https://www.companyweb.be/fr/0407799084/ateliers-de-tertre) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407799084) · [site](https://etater.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Rue Olivier Lhoir Tertre/Saint-Ghislain; NACE **88.993**; erkenning aannemer van werken.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +13.27% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +6.85% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** DROP −97.23% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** DROP −0.42%; FTE **{FTE25}**; filed **16.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ASBL Ateliers de Tertre
via info@etater.be
Rue Olivier Lhoir 97, 7333 Tertre (Saint-Ghislain)
Objet: Publicité des comptes annuels 2025 Ateliers de Tertre (BCE 0407.799.084)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL DROP EUR{PN25} vs bénéfice YE2024 EUR{PN24} (−97,23%) — réconciliation avec CA JUMP +13% et FTE JUMP vers {FTE25}.
4. Matrice des subsides AWIPH/AVIQ / régionaux ETA derrière le CA EUR{OM25}.
5. Allocation des coûts par pôle d'activité (palettes, métal, nettoyage, titres-services, etc.).

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2234",
    {
        "task_id": "rq_2234",
        "title": (
            "leftover dual — Ateliers de Tertre YE2025 Medium (omzet JUMP 10.00m / "
            "pnl DROP -97% / bruto≫omzet ~1.31x)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Le Rucher; unused ETA YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T23:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Ateliers de Tertre 0407.799.084 YE2025 Medium CW; omzet JUMP "
            f"{OM25} bruto {BR25} (~{RATIO}x) pnl DROP {PN25} (-97%) equity {EQ25} FTE JUMP "
            f"{FTE25}; 1 VE Saint-Ghislain ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; next rq_2235; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2235",
    {
        "task_id": "rq_2235",
        "title": (
            "leftover dual hole-fill after Ateliers de Tertre — prefer AGB/FARO-YE2025/"
            "AIESH-REW/Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Ateliers de Tertre YE2025 Medium (omzet JUMP 10.00m / "
            "pnl DROP -97% / bruto≫omzet ~1.31x). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if "
            "NBB/CW euros live, else unused maatwerk/kringloop/WZC/IGS/HVZ/ETA. Do NOT redo "
            "Ateliers de Tertre, Le Rucher, Travie, SDB, De Vleugels, Kiemkracht, De Oever, "
            "ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel West, Manus "
            "BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, "
            "NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel "
            "Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, "
            "ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, "
            "Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier "
            "Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, "
            "A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, "
            "Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, "
            "Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, "
            "Mobiel, Vlotter (YE2024), Aralea (YE2024), Gandae (YE2024), IPFBW, Aquiris, SPGE, "
            "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
            "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, "
            "ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2234 Ateliers de Tertre; FARO/AIESH/REW YE2024; AGB Bornem "
            "JR2024; Heropbeuring CW opaque; Gandae still YE2024"
        ),
    },
)
write_csv("research_queue.csv", r_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
ls[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2234",
    "ticks_completed": "2234",
    "paused": "no",
    "notes": (
        f"tick2234 leftover Ateliers de Tertre 0407.799.084 Medium (omzet JUMP {OM25}; "
        f"bruto {BR25} ~{RATIO}x; pnl DROP {PN25} -97.23%; equity {EQ25}; FTE JUMP {FTE25}; "
        "1 VE Saint-Ghislain ETA); after Le Rucher@2233; AGB Bornem JR2024; FARO/AIESH/REW "
        "YE2024; Heropbeuring CW opaque; next rq_2235; next every-10 2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2234 - 2026-08-26T23:50:00Z - rq_2234 Ateliers de Tertre (omzet JUMP 10.00m / pnl DROP -97% / bruto≫omzet ~1.31x / Medium)

- Unit: **rq_2234** leftover dual after **rq_2233 Le Rucher**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Gandae still **YE2024**. Took FREE unused Walloon ETA **ASBL Ateliers de Tertre** YE2025 (KBO **0407.799.084**; Rue Olivier Lhoir 97 Saint-Ghislain/Tertre; **Actief** **1 VE**; NACE **88.993**). Do not redo Le Rucher/Travie/SDB/De Vleugels/Kiemkracht stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +13.27% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +6.85% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** DROP -97.23% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP -0.42%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **16.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@etater.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.50); entities (+1 vzw_ateliers_de_tertre); foi + draft {GAP}; rq_2234=done + rq_2235 open; loop_state ticks=2234; raw docs/doge/raw/tick2234/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2235 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2234 Ateliers Tertre omzet={OM25} bruto={BR25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
