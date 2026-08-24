# tick2236 — L'Entraide Enghien YE2025 Medium leftover dual (named FREE after Entra)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_entraide_enghien"
TICK = "2236"
UTC = "2026-08-27T00:40:00Z"
GAP = "gap_enghien_nbb_pdf_assets_debt_bruto_gt_omzet_equity_jump_77pct_eta_matrix_l5"
COMM = "comm_enghien_jr2025_statutory_eta_bruto_gt_omzet_equity_jump_77pct"
LB = "lb_enghien_bruto_4_63m_omzet_2_36m_equity_jump_77pct_jr2025"

OM25, OM24 = 2363211, 2092441
BR25, BR24 = 4625722, 4355191
PN25, PN24 = 153168, 68165
EQ25, EQ24 = 323288, 182264
FTE25, FTE24 = 123.5, 116.5
RATIO = round(BR25 / OM25, 2)  # ~1.96


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
        "src_enghien_jr2025_cw_nl",
        "Companyweb NL L'Entraide Enghien YE2025 statutory",
        "https://www.companyweb.be/nl/0407598255/l-entraide-par-le-travail-d-enghien-et-environs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+12.94%) bruto JUMP {BR25} (+6.21% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+124.7%) equity JUMP {EQ25} (+77.37%) "
            f"FTE {FTE25}; filed 23-06-2026"
        ),
    ),
    (
        "src_enghien_jr2025_cw_en",
        "Companyweb EN L'Entraide Enghien YE2025 statutory",
        "https://www.companyweb.be/en/0407598255/l-entraide-par-le-travail-d-enghien-et-environs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 23-06-2026"
        ),
    ),
    (
        "src_enghien_jr2025_cw_fr",
        "Companyweb FR L'Entraide Enghien YE2025 statutory",
        "https://www.companyweb.be/fr/0407598255/l-entraide-par-le-travail-d-enghien-et-environs",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_enghien_kbo_2236",
        "KBO L'Entraide Enghien 0407.598.255 Actief 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407598255",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2236; Actief ASBL L'Entraide par le Travail d'Enghien et Environs; zetel "
            "Handelslaan/Avenue du Commerce(P.E) 19 7850 Enghien; 1 VE; RSZ NACE 88.993; "
            "BTW 32.400 toys; dagelijks bestuur Patrick Godart"
        ),
    ),
    (
        "src_enghien_site_contact_2236",
        "ETA Enghien FOI channel contact@etaenghien.com",
        "https://www.etaenghien.com/",
        "ETA Enghien ASBL",
        "foi_contact",
        "tick2236; contact@etaenghien.com; +32 2 395 30 64; Avenue du Commerce 19 Enghien; leseta.be annuaire",
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
        "name_nl": "L'Entraide Enghien / ETA Enghien ASBL (Enghien / ETA maatwerk)",
        "name_fr": "L'Entraide par le Travail d'Enghien et Environs ASBL (ETA)",
        "name_en": "L'Entraide Enghien adapted-work ASBL (ETA Enghien)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.etaenghien.com/",
        "foi_email": "contact@etaenghien.com",
        "foi_postal": "Avenue du Commerce(P.E) 19, 7850 Enghien",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.598.255 Actief 1 VE "
            f"RSZ NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl JUMP {PN25} "
            f"equity JUMP {EQ25} (+77%) FTE JUMP {FTE25}; neerlegging 23.06.2026; assets/debt "
            f"Unknown; FOI {GAP}; preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; after Entra@2235; deferred FREE EntrAnam/IN-Z; not "
            "TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_enghien_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +6.21% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_enghien_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +12.94% vs YE2024 {OM24}",
    ),
    (
        "bud_enghien_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +124.7% vs YE2024 {PN24}",
    ),
    (
        "bud_enghien_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +77.37% vs YE2024 {EQ24}",
    ),
    (
        "bud_enghien_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 123.5",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_enghien_omzet_jr2024_statutory_cmp",
        "2024",
        OM24,
        "CW statutory omzet YE2024 comparative",
        f"tick{TICK}; YE2024 omzet {OM24} comparative",
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
            "source_id": "src_enghien_jr2025_cw_en",
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
            "L'Entraide Enghien YE2025 leftover dual (bruto≫omzet ~1.96x / equity JUMP +77% / "
            "Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Hainaut (Enghien) / Walloon AVIQ adapted-work path / packaging/"
            "green spaces"
        ),
        "legal_basis": (
            "ASBL ETA L'Entraide par le Travail d'Enghien et Environs (KBO 0407.598.255; "
            "Actief; 1 VE; RSZ NACE 88.993)"
        ),
        "decision_date": "2026-06-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            "https://www.companyweb.be/en/0407598255/l-entraide-par-le-travail-d-enghien-et-environs"
        ),
        "stated_goal": (
            "Walloon ETA Enghien — adapted work (packaging/industrial subcontracting/green spaces)"
        ),
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.96x (4.63m vs 2.36m); "
            "AVIQ ETA wage-intervention matrix; equity JUMP +77% drivers; FTE 123.5 public path"
        ),
        "source_id": "src_enghien_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Enghien>EntraideEnghien>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"omzet JUMP; equity JUMP +77%; FTE JUMP {FTE25}; 1 VE; after Entra@2235; AGB "
            "Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; deferred FREE "
            "EntrAnam/IN-Z; not TE-additive"
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
            "L'Entraide Enghien bruto 4.63m ≫ omzet 2.36m ~1.96x / equity JUMP +77% (YE2025 ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Hainaut>Enghien>EntraideEnghien>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet JUMP {OM25} (~{RATIO}x) / pnl JUMP {PN25} / equity JUMP "
            f"{EQ25} (+77%) / FTE JUMP {FTE25} / 1 VE Enghien ETA"
        ),
        "confidence": "medium",
        "source_id": "src_enghien_jr2025_cw_en",
        "beneficiaries": "ETA workers Enghien / AVIQ Walloon adapted-work path",
        "stated_goal": "Walloon ETA packaging/industrial subcontracting/green spaces",
        "measured_outcome": (
            f"omzet JUMP +12.94%; bruto≫omzet ~{RATIO}x; pnl JUMP +124.7%; equity JUMP "
            f"+77.37%; FTE JUMP {FTE25}; 1 VE; filed 23.06.2026"
        ),
        "absurdity_score": "6.5",
        "cost_score": "5.4",
        "difficulty": "3.0",
        "priority_index": "6.20",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.96x vs AVIQ ETA "
            "wage-intervention matrix; explain equity JUMP +77%; FTE 123.5 public-path "
            "transparency"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Entra@2235; deferred FREE "
            "EntrAnam/IN-Z; next every-10 2240"
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
            "Wallonie>Hainaut>Enghien>EntraideEnghien>NBB_PDF_assets_debt_bruto_gt_omzet_"
            "equity_jump_aviq_eta"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x) composition; AVIQ ETA wage-intervention / subsidy "
            f"matrix behind bruto 4.63m; equity JUMP +77% drivers (EUR{EQ25} vs YE2024 "
            f"EUR{EQ24}); FTE {FTE25} recon"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL (bruto 4.63m / omzet 2.36m / equity JUMP +77% "
            f"/ {FTE25} FTE) under public AVIQ adapted-work path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "L'Entraide par le Travail d'Enghien et Environs ASBL / ETA Enghien",
        "recipient_email": "contact@etaenghien.com",
        "recipient_postal": "Avenue du Commerce(P.E) 19, 7850 Enghien",
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
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; deferred FREE EntrAnam/"
            "IN-Z; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — L'Entraide Enghien (NBB PDF / bruto≫omzet ~{RATIO}x / equity JUMP +77%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** L'Entraide par le Travail d'Enghien et Environs ASBL / ETA Enghien — KBO **0407.598.255** (Actief; Avenue du Commerce(P.E) 19, 7850 Enghien; **1 VE**; FTE {FTE25} CW; RSZ NACE **88.993**)  
**recipient:** contact@etaenghien.com · Avenue du Commerce 19, 7850 Enghien  
**sources:** [CW EN](https://www.companyweb.be/en/0407598255/l-entraide-par-le-travail-d-enghien-et-environs) · [CW NL](https://www.companyweb.be/nl/0407598255/l-entraide-par-le-travail-d-enghien-et-environs) · [CW FR](https://www.companyweb.be/fr/0407598255/l-entraide-par-le-travail-d-enghien-et-environs) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407598255) · [site](https://www.etaenghien.com/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Handelslaan/Avenue du Commerce Enghien; RSZ NACE **88.993**; BTW 32.400; dagelijks bestuur Patrick Godart.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +12.94% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +6.21% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +124.7%; equity **EUR{EQ25:,}** JUMP +77.37%; FTE **{FTE25}**; filed **23.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Entra@2235. Deferred FREE: EntrAnam / IN-Z Genk YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: L'Entraide par le Travail d'Enghien et Environs ASBL / ETA Enghien
via contact@etaenghien.com
Avenue du Commerce 19, 7850 Enghien
Objet: Publicité des comptes annuels 2025 ETA Enghien (BCE 0407.598.255)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. Matrice des interventions AVIQ / subsides ETA derrière la marge brute EUR{BR25}.
4. Drivers de la hausse des capitaux propres +77% (EUR{EQ25} vs YE2024 EUR{EQ24}).
5. Réconciliation FTE {FTE25} avec le financement public.

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
    "rq_2236",
    {
        "task_id": "rq_2236",
        "title": (
            "leftover dual — L'Entraide Enghien YE2025 Medium (bruto≫omzet ~1.96x / equity "
            "JUMP +77%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Entra; named FREE Enghien ETA YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T00:15:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Enghien 0407.598.255 YE2025 Medium CW; omzet JUMP {OM25} bruto "
            f"{BR25} (~{RATIO}x) pnl JUMP {PN25} equity JUMP {EQ25} (+77%) FTE JUMP "
            f"{FTE25}; 1 VE Enghien ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; deferred FREE EntrAnam/IN-Z; next rq_2237; every-10 "
            "next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2237",
    {
        "task_id": "rq_2237",
        "title": (
            "leftover dual hole-fill after Enghien — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-EntrAnam-IN-Z-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after L'Entraide Enghien YE2025 Medium (bruto≫omzet ~1.96x / "
            "equity JUMP +77%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
            "TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros "
            "live, else named FREE EntrAnam (0407.273.801) / IN-Z Genk (0457.521.086 YE2025 "
            "omzet 14.36m / bruto≫omzet ~1.67x / pnl LOSS DEEP -356k) / De Enter Brecht / "
            "De Ploeg / De Dageraad / BUSELOC / RODEA / Den Diepen Boomgaard / Vlaspit / "
            "Aurora / unused maatwerk/kringloop/WZC/IGS/HVZ/ETA/VAPH. Do NOT redo Enghien, "
            "Entra, Het Rekreatief, Ateliers de Tertre, Le Rucher, Travie, SDB, De Vleugels, "
            "Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, "
            "Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel "
            "Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, "
            "Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize "
            "Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, "
            "Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, "
            "Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, "
            "BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, "
            "Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, "
            "De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK "
            "SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, "
            "Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), "
            "Aralea (YE2024), Gandae (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
            "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
            "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, "
            "BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2236 Enghien; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; named FREE EntrAnam/IN-Z YE2025"
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
    "last_unit_id": "rq_2236",
    "ticks_completed": "2236",
    "paused": "no",
    "notes": (
        f"tick2236 leftover Enghien 0407.598.255 Medium (omzet JUMP {OM25}; bruto {BR25} "
        f"~{RATIO}x; pnl JUMP {PN25}; equity JUMP {EQ25} +77%; FTE JUMP {FTE25}; 1 VE "
        "Enghien ETA); after Entra@2235; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; deferred EntrAnam/IN-Z; next rq_2237; next every-10 2240; "
        "continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2236 - 2026-08-27T00:40:00Z - rq_2236 L'Entraide Enghien (bruto≫omzet ~1.96x / equity JUMP +77% / Medium)

- Unit: **rq_2236** leftover dual after **rq_2235 Entra**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE leftover **L'Entraide Enghien / ETA Enghien ASBL** YE2025 (KBO **0407.598.255**; Avenue du Commerce 19 Enghien; **Actief** **1 VE**; RSZ NACE **88.993**). Deferred FREE **EntrAnam** / **IN-Z Genk**. Do not redo Entra/Het Rekreatief/Ateliers Tertre/Le Rucher/Travie/SDB stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +12.94% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +6.21% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +124.7% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +77.37%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **23.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via contact@etaenghien.com.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 vzw_entraide_enghien); foi + draft {GAP}; rq_2236=done + rq_2237 open; loop_state ticks=2236; raw docs/doge/raw/tick2236/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2237 (AGB/FARO-if-YE2025 / AIESH-REW / EntrAnam-IN-Z-or-unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2236 Enghien omzet={OM25} bruto={BR25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
