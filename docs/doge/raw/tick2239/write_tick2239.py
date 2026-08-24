# tick2239 — Manufast-ABP YE2025 Medium leftover dual (FREE Brussels ETA)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_manufast_abp_brussel"
TICK = "2239"
UTC = "2026-08-27T01:45:00Z"
GAP = "gap_manufast_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_flip_eta_matrix_l5"
COMM = "comm_manufast_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_flip"
LB = "lb_manufast_bruto_6_25m_gt_omzet_1_87x_pnl_loss_flip_equity_drop_jr2025"

OM25, OM24 = 3337881, 3291617
BR25, BR24 = 6254925, 5997451
PN25, PN24 = -299652, 949872
EQ25, EQ24 = 1363356, 1881340
FTE25, FTE24 = 234.0, 248.0
RATIO = round(BR25 / OM25, 2)  # ~1.87


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
        "src_manufast_jr2025_cw_nl",
        "Companyweb NL Manufast-ABP YE2025 statutory",
        "https://www.companyweb.be/nl/0409118977/manufast-abp-entreprise-de-travail-adapte",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+1.41%) bruto JUMP {BR25} (+4.29% "
            f"bruto≫omzet ~{RATIO}x) pnl LOSS FLIP {PN25} vs YE2024 profit {PN24} equity "
            f"DROP {EQ25} (-27.53%) FTE DROP {FTE25}; filed 16-07-2026; note YE2023 omzet "
            "was ~7.94m / FTE 357.6 (structural shrink)"
        ),
    ),
    (
        "src_manufast_jr2025_cw_en",
        "Companyweb EN Manufast-ABP YE2025 statutory",
        "https://www.companyweb.be/en/0409118977/manufast-abp-entreprise-de-travail-adapte",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 16-07-2026"
        ),
    ),
    (
        "src_manufast_jr2025_cw_fr",
        "Companyweb FR Manufast-ABP YE2025 statutory",
        "https://www.companyweb.be/fr/0409118977/manufast-abp-entreprise-de-travail-adapte",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_manufast_kbo_2239",
        "KBO Manufast-ABP 0409.118.977 Actief Berchem-Sainte-Agathe 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0409118977",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2239; Actief ASBL MANUFAST-ABP; zetel Gentsesteenweg/Chaussée de Gand 1434 "
            "1082 Sint-Agatha-Berchem; 1 VE; NACE RSZ/BTW 88.993; Brussels CoCoF ETA"
        ),
    ),
    (
        "src_manufast_site_contact_2239",
        "Manufast FOI channel info@manufast.be",
        "https://www.manufast.be/en/contact/",
        "Manufast-ABP ASBL",
        "foi_contact",
        "tick2239; info@manufast.be; 02 464 26 11; Chaussée de Gand 1434 1082 Brussels",
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
        "name_nl": "Manufast-ABP ASBL (Sint-Agatha-Berchem / Brussels ETA)",
        "name_fr": "Manufast-ABP ASBL / Entreprise de Travail Adapté (Bruxelles)",
        "name_en": "Manufast-ABP adapted-work ASBL (Brussels ETA logistics)",
        "level": "parastatal",
        "parent_id": "sec_brussels",
        "community_language": "fr",
        "website": "https://www.manufast.be/",
        "foi_email": "info@manufast.be",
        "foi_postal": "Chaussée de Gand 1434, 1082 Berchem-Sainte-Agathe",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0409.118.977 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl LOSS FLIP {PN25} "
            f"equity DROP {EQ25} (-27.53%) FTE DROP {FTE25}; neerlegging 16.07.2026; "
            f"assets/debt Unknown; FOI {GAP}; structural shrink vs YE2023 omzet~7.94m/"
            "FTE357.6; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; after Metalgroup@2238; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_manufast_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +4.29% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_manufast_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +1.41% vs YE2024 {OM24}; note YE2023 was ~7.94m",
    ),
    (
        "bud_manufast_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 profit {PN24}",
    ),
    (
        "bud_manufast_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -27.53% vs YE2024 {EQ24}",
    ),
    (
        "bud_manufast_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 234",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_manufast_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative (profit)",
        f"tick{TICK}; YE2024 pnl profit {PN24} comparative (pre LOSS FLIP)",
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
            "source_id": "src_manufast_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_bruto":{BR25},"2025_omzet":{OM25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_bruto":{BR24},"2024_omzet":{OM24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Manufast-ABP YE2025 leftover dual (bruto 6.25m / bruto≫omzet ~1.87x / "
            "pnl LOSS FLIP -300k / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Brussels (Berchem-Sainte-Agathe) / CoCoF adapted-work public path"
        ),
        "legal_basis": (
            "ASBL ETA Manufast-ABP (KBO 0409.118.977; Actief; 1 VE; NACE 88.993; Brussels CoCoF)"
        ),
        "decision_date": "2026-07-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            "https://www.companyweb.be/en/0409118977/manufast-abp-entreprise-de-travail-adapte"
        ),
        "stated_goal": "Brussels ETA social logistics (e-picking/co-packing/digitization)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.87x; reconcile pnl "
            "LOSS FLIP (+950k->-300k) and equity DROP -27.5% with CoCoF ETA subsidy matrix; "
            "note structural shrink vs YE2023 omzet~7.94m/FTE357.6"
        ),
        "source_id": "src_manufast_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Bruxelles>BerchemSteAgathe>Manufast>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl LOSS FLIP; equity DROP -27.53%; FTE DROP {FTE25}; 1 VE; after Metalgroup@"
            "2238; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "not TE-additive"
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
            "Manufast bruto 6.25m / bruto≫omzet ~1.87x / pnl LOSS FLIP -300k / equity DROP "
            "-27% (YE2025 Brussels ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Bruxelles>BerchemSteAgathe>Manufast>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet {OM25} (~{RATIO}x) / pnl LOSS FLIP {PN25} (from profit "
            f"{PN24}) / equity DROP {EQ25} (-27.53%) / FTE DROP {FTE25} / 1 VE Brussels ETA"
        ),
        "confidence": "medium",
        "source_id": "src_manufast_jr2025_cw_en",
        "beneficiaries": "ETA workers Brussels / CoCoF adapted-work public path",
        "stated_goal": "Brussels ETA social logistics",
        "measured_outcome": (
            f"omzet JUMP +1.41%; bruto≫omzet ~{RATIO}x; pnl LOSS FLIP (+950k->-300k); "
            f"equity DROP -27.53%; FTE DROP {FTE25}; structural shrink vs YE2023; filed "
            "16.07.2026"
        ),
        "absurdity_score": "7.5",
        "cost_score": "5.4",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.87x vs CoCoF ETA "
            "matrix; reconcile LOSS FLIP + equity DROP -27.5% + FTE DROP; explain shrink vs "
            "YE2023 omzet~7.94m"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Metalgroup@2238; next every-10 2240"
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
            "Bruxelles>BerchemSteAgathe>Manufast>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl LOSS FLIP EUR{PN25} vs YE2024 profit "
            f"EUR{PN24}; equity DROP EUR{EQ25} (-27.53%); CoCoF ETA subsidy matrix; "
            f"reconciling structural shrink vs YE2023 omzet~7.94m / FTE357.6"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels ETA ASBL (bruto 6.25m / omzet 3.34m / ~{RATIO}x / "
            f"pnl LOSS FLIP / equity DROP -27.5% / FTE DROP {FTE25}) under CoCoF path; "
            "assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Manufast-ABP ASBL",
        "recipient_email": "info@manufast.be",
        "recipient_postal": "Chaussée de Gand 1434, 1082 Berchem-Sainte-Agathe",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/"
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Manufast-ABP (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Manufast-ABP ASBL — KBO **0409.118.977** (Actief; Chaussée de Gand 1434, 1082 Berchem-Sainte-Agathe; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Brussels CoCoF ETA)  
**recipient:** info@manufast.be · Chaussée de Gand 1434, 1082 Brussels  
**sources:** [CW EN](https://www.companyweb.be/en/0409118977/manufast-abp-entreprise-de-travail-adapte) · [CW NL](https://www.companyweb.be/nl/0409118977/manufast-abp-entreprise-de-travail-adapte) · [CW FR](https://www.companyweb.be/fr/0409118977/manufast-abp-entreprise-de-travail-adapte) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409118977) · [site](https://www.manufast.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Chaussée de Gand Berchem-Sainte-Agathe; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +1.41% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +4.29% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** LOSS FLIP vs YE2024 profit EUR{PN24:,}; equity **EUR{EQ25:,}** DROP −27.53%; FTE **{FTE25}** DROP vs {FTE24}; filed **16.07.2026**. Note YE2023 omzet ~EUR7.94m / FTE 357.6 (structural shrink).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Metalgroup@2238.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Manufast-ABP ASBL
via info@manufast.be
Chaussée de Gand 1434, 1082 Berchem-Sainte-Agathe
Objet: Publicité des comptes annuels 2025 Manufast-ABP (BCE 0409.118.977)

Madame, Monsieur,

Sur la base de l'ordonnance bruxelloise relative à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL LOSS FLIP EUR{PN25} vs bénéfice YE2024 EUR{PN24} — réconciliation avec equity DROP −27,53% et FTE DROP.
4. Matrice des subsides CoCoF / ETA derrière la marge brute EUR{BR25}.
5. Explication du rétrécissement structurel vs YE2023 (CA ~EUR7,94m / FTE 357,6).

Période YE2025 (+ comparative YE2024/YE2023). Réf: {GAP}

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
    "rq_2239",
    {
        "task_id": "rq_2239",
        "title": (
            "leftover dual — Manufast-ABP YE2025 Medium (bruto 6.25m / bruto≫omzet ~1.87x / "
            "pnl LOSS FLIP / equity DROP -27%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Metalgroup; unused FREE Brussels ETA Manufast-ABP YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T01:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Manufast 0409.118.977 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl LOSS FLIP {PN25} equity DROP {EQ25} (-27.53%) FTE DROP "
            f"{FTE25}; 1 VE Brussels ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; after Metalgroup@2238; next rq_2240 EVERY-10; "
            "do NOT redo Metalgroup/EntrAnam/Enghien/Entra/Ateliers/Rekreatief"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2240",
    {
        "task_id": "rq_2240",
        "title": (
            "EVERY-10 progress coverage % + waste top10 THEN leftover dual after Manufast — "
            "prefer AGB/FARO-YE2025/AIESH-REW/Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "10",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 MANDATORY first: refresh progress_every_10_ticks.md (layers A-E of "
            "EUR 347.956 bn TE) + doge_waste_top10_current.md (top 10 by priority_index). "
            "Then hole-fill ONE unit: leftover dual after Manufast-ABP YE2025 Medium "
            "(bruto 6.25m / bruto≫omzet ~1.87x / pnl LOSS FLIP / equity DROP -27%). Prefer "
            "leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
            "AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "maatwerk/kringloop/WZC/IGS/HVZ/ETA. Do NOT redo Manufast, Metalgroup, "
            "EntrAnam, Enghien, Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, "
            "Travie, SDB, De Vleugels, Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, "
            "ViTeS, Reset, Den Azalee, Kringwinkel West, Manus BXL, Manus VZW groep, Manus "
            "Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, "
            "Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep "
            "Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, "
            "Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
            "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, "
            "Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, "
            "Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, "
            "Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
            "NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), Gandae (YE2024), IPFBW, "
            "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
            "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
            "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 after this: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2239 Manufast; MUST every-10 progress + waste top10 then "
            "hole-fill one unit; FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque"
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
    "last_unit_id": "rq_2239",
    "ticks_completed": "2239",
    "paused": "no",
    "notes": (
        f"tick2239 leftover Manufast 0409.118.977 Medium (bruto {BR25} ~{RATIO}x omzet "
        f"{OM25}; pnl LOSS FLIP {PN25}; equity DROP {EQ25} -27.53%; FTE DROP {FTE25}; "
        "1 VE Brussels ETA); after Metalgroup@2238; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; next rq_2240 EVERY-10; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2239 - 2026-08-27T01:45:00Z - rq_2239 Manufast-ABP Brussels (bruto 6.25m / bruto≫omzet ~1.87x / pnl LOSS FLIP / equity DROP -27% / Medium)

- Unit: **rq_2239** leftover dual after **rq_2238 Metalgroup**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024; NBB YE2025 unpublished); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE unused Brussels ETA **Manufast-ABP ASBL** YE2025 (KBO **0409.118.977**; Chaussée de Gand 1434 Berchem-Sainte-Agathe; **Actief** **1 VE**; NACE **88.993** CoCoF ETA) — race leftover prepared@2238 but Metalgroup committed. Do not redo Metalgroup/EntrAnam/Enghien/Entra/Ateliers Tertre/Het Rekreatief/Le Rucher stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +1.41% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +4.29% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** LOSS FLIP vs YE2024 profit EUR{PN24}; equity **EUR{EQ25}** DROP -27.53%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **16.07.2026**. Note YE2023 omzet ~7.94m / FTE 357.6 (structural shrink). Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@manufast.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 vzw_manufast_abp_brussel); foi + draft {GAP}; rq_2239=done + rq_2240 open (EVERY-10); loop_state ticks=2239; raw docs/doge/raw/tick2239/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240** MUST refresh progress + waste top10 then hole-fill). Next: rq_2240.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2239 Manufast bruto={BR25} omzet={OM25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
