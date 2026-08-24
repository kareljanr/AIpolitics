# tick2235 — Entra Fleurus YE2025 Medium leftover dual (largest Walloon ETA FREE)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_entra_fleurus"
TICK = "2235"
UTC = "2026-08-27T00:15:00Z"
GAP = "gap_entra_nbb_pdf_assets_debt_bruto_gt_omzet_eta_aviq_matrix_l5"
COMM = "comm_entra_jr2025_statutory_eta_omzet_jump_bruto_gt_omzet"
LB = "lb_entra_omzet_28_61m_bruto_35_33m_fte_885_jr2025"

OM25, OM24 = 28614682, 27146011
BR25, BR24 = 35333600, 35227244
PN25, PN24 = 579837, 592708
EQ25, EQ24 = 12873938, 12380612
FTE25, FTE24 = 885.2, 878.1
RATIO = round(BR25 / OM25, 2)  # ~1.23


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
        "src_entra_jr2025_cw_nl",
        "Companyweb NL Entra YE2025 statutory",
        "https://www.companyweb.be/nl/0406645972/l-entraide-par-le-travail",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+5.41%) bruto JUMP {BR25} (+0.30% "
            f"bruto≫omzet ~{RATIO}x) pnl DROP {PN25} (-2.17%) equity JUMP {EQ25} (+3.98%) "
            f"FTE {FTE25}; filed 30-06-2026"
        ),
    ),
    (
        "src_entra_jr2025_cw_en",
        "Companyweb EN Entra YE2025 statutory",
        "https://www.companyweb.be/en/0406645972/entraide-par-le-travail",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 30-06-2026"
        ),
    ),
    (
        "src_entra_jr2025_cw_fr",
        "Companyweb FR Entra YE2025 statutory",
        "https://www.companyweb.be/fr/0406645972/entraide-par-le-travail",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_entra_kbo_2235",
        "KBO Entra 0406.645.972 Actief Fleurus/Heppignies 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0406645972",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2235; Actief ASBL Entraide par le Travail / Entra; zetel Rue du Tilloi(H) 11 "
            "6220 Fleurus; 1 VE; NACE RSZ 88.993 + BTW multi (callcenter/cleaning/electro/"
            "painting); erkenning aannemer van werken"
        ),
    ),
    (
        "src_entra_site_contact_2235",
        "Entra FOI channel scm@entra.be / accueil@entra.be",
        "https://www.entra.be/",
        "Entra ASBL",
        "foi_contact",
        "tick2235; scm@entra.be; accueil@entra.be; 071 25 39 00; Rue du Tilloi 11 Heppignies/Fleurus",
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
        "name_nl": "Entra / Entraide par le Travail ASBL (Fleurus-Heppignies / ETA)",
        "name_fr": "Entra ASBL / Entraide par le Travail (Fleurus-Heppignies / ETA)",
        "name_en": "Entra adapted-work ASBL (Fleurus-Heppignies; largest Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.entra.be/",
        "foi_email": "scm@entra.be",
        "foi_postal": "Rue du Tilloi(H) 11, 6220 Fleurus",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0406.645.972 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl {PN25} equity JUMP "
            f"{EQ25} FTE JUMP {FTE25}; neerlegging 30.06.2026; assets/debt Unknown; FOI {GAP}; "
            "preferred stalls AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE Enghien/EntrAnam YE2025; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_entra_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +0.30% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_entra_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +5.41% vs YE2024 {OM24}",
    ),
    (
        "bud_entra_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -2.17% vs YE2024 {PN24}",
    ),
    (
        "bud_entra_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +3.98% vs YE2024 {EQ24}",
    ),
    (
        "bud_entra_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 885.2",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_entra_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_entra_jr2025_cw_en",
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
            "Entra YE2025 leftover dual (omzet JUMP 28.61m / bruto 35.33m ~1.23x / "
            "FTE 885 / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Hainaut (Fleurus/Heppignies/Charleroi) / Walloon AVIQ adapted-work path"
        ),
        "legal_basis": (
            "ASBL ETA Entraide par le Travail (KBO 0406.645.972; Actief; 1 VE; NACE 88.993; "
            "erkenning aannemer)"
        ),
        "decision_date": "2026-06-30",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0406645972/entraide-par-le-travail",
        "stated_goal": "Largest Walloon ETA — adapted work multi-sector (callcenter/industry/laundry)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.23x (35.33m vs 28.61m); "
            "AVIQ/AWIPH ETA wage-intervention matrix; sector cost allocation (callcenter/"
            "assembly/laundry/building); reconcile FTE 885 with public subsidy path"
        ),
        "source_id": "src_entra_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Fleurus>Entra>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"omzet JUMP; FTE JUMP {FTE25}; 1 VE; after Ateliers Tertre@2234; AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; deferred FREE Enghien/"
            "EntrAnam; not TE-additive"
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
            "Entra omzet JUMP 28.61m / bruto 35.33m ~1.23x / FTE 885 (YE2025 largest Walloon ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Hainaut>Fleurus>Entra>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet JUMP {OM25} (~{RATIO}x) / pnl {PN25} / equity JUMP "
            f"{EQ25} / FTE JUMP {FTE25} / 1 VE Fleurus-Heppignies ETA"
        ),
        "confidence": "medium",
        "source_id": "src_entra_jr2025_cw_en",
        "beneficiaries": "ETA workers Hainaut / AVIQ Walloon adapted-work path",
        "stated_goal": "Largest Walloon ETA multi-sector adapted work",
        "measured_outcome": (
            f"omzet JUMP +5.41%; bruto≫omzet ~{RATIO}x; pnl flat DROP -2.17%; equity JUMP "
            f"+3.98%; FTE JUMP {FTE25}; 1 VE; filed 30.06.2026"
        ),
        "absurdity_score": "6.8",
        "cost_score": "6.2",
        "difficulty": "3.0",
        "priority_index": "6.50",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.23x vs AVIQ ETA "
            "wage-intervention matrix; sector cost allocation across callcenter/industry/"
            "laundry/building; FTE 885 public-path transparency"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Ateliers Tertre@2234; "
            "deferred FREE Enghien/EntrAnam; next every-10 2240"
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
            "Wallonie>Hainaut>Fleurus>Entra>NBB_PDF_assets_debt_bruto_gt_omzet_aviq_eta"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x) composition; AVIQ/AWIPH ETA wage-intervention / "
            f"subsidy matrix behind bruto 35.33m; sector cost allocation (callcenter/assembly/"
            f"laundry/building); FTE {FTE25} recon"
        ),
        "why_it_matters": (
            f"Medium CW shows largest Walloon ETA ASBL (bruto 35.33m / omzet 28.61m / "
            f"{FTE25} FTE) under public AVIQ adapted-work path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Entra ASBL / Entraide par le Travail",
        "recipient_email": "scm@entra.be",
        "recipient_postal": "Rue du Tilloi(H) 11, 6220 Fleurus",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; cc accueil@entra.be; "
            "preferred stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
            "deferred FREE Enghien/EntrAnam; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Entra (NBB PDF / bruto≫omzet ~{RATIO}x / AVIQ ETA matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Entra ASBL / Entraide par le Travail — KBO **0406.645.972** (Actief; Rue du Tilloi(H) 11, 6220 Fleurus; **1 VE**; FTE {FTE25} CW; NACE **88.993**; largest Walloon ETA)  
**recipient:** scm@entra.be · cc accueil@entra.be · Rue du Tilloi 11, 6220 Heppignies/Fleurus  
**sources:** [CW EN](https://www.companyweb.be/en/0406645972/entraide-par-le-travail) · [CW NL](https://www.companyweb.be/nl/0406645972/l-entraide-par-le-travail) · [CW FR](https://www.companyweb.be/fr/0406645972/entraide-par-le-travail) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406645972) · [site](https://www.entra.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Rue du Tilloi Fleurus/Heppignies; NACE **88.993** + multi BTW (callcenter/cleaning/electro/painting); erkenning aannemer.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +5.41% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +0.30% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** DROP −2.17%; equity **EUR{EQ25:,}** JUMP +3.98%; FTE **{FTE25}**; filed **30.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. Deferred FREE: Enghien ETA / EntrAnam YE2025.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: Entra ASBL / Entraide par le Travail
via scm@entra.be (cc: accueil@entra.be)
Rue du Tilloi 11, 6220 Fleurus (Heppignies)
Objet: Publicité des comptes annuels 2025 Entra (BCE 0406.645.972)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. Matrice des interventions AVIQ/AWIPH / subsides ETA derrière la marge brute EUR{BR25}.
4. Allocation des coûts par secteur (call center, assemblage, sous-traitance industrielle, blanchisserie, bâtiment).
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
    "rq_2235",
    {
        "task_id": "rq_2235",
        "title": (
            "leftover dual — Entra YE2025 Medium (omzet JUMP 28.61m / bruto 35.33m ~1.23x / "
            "FTE 885)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Ateliers Tertre; unused Walloon ETA YE2025",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T23:50:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Entra 0406.645.972 YE2025 Medium CW; omzet JUMP {OM25} bruto "
            f"{BR25} (~{RATIO}x) pnl {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; 1 VE "
            "Fleurus ETA; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "deferred FREE Enghien/EntrAnam; next rq_2236; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2236",
    {
        "task_id": "rq_2236",
        "title": (
            "leftover dual hole-fill after Entra — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-Enghien-EntrAnam-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Entra Fleurus YE2025 Medium (omzet JUMP 28.61m / bruto "
            "35.33m ~1.23x / FTE 885). Prefer leftover AGB/APB if JR2025 PDF live, else FARO "
            "if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros "
            "live, else named FREE L'Entraide Enghien (0407.598.255 YE2025 bruto≫omzet "
            "~1.96x / equity JUMP +77%) / EntrAnam (0407.273.801) / unused maatwerk/kringloop/"
            "WZC/IGS/HVZ/ETA. Do NOT redo Entra, Ateliers de Tertre, Le Rucher, Travie, SDB, "
            "De Vleugels, Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, "
            "Den Azalee, Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, "
            "Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, "
            "Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, "
            "Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, "
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
            "spawned after tick2235 Entra; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; named FREE Enghien/EntrAnam YE2025"
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
    "last_unit_id": "rq_2235",
    "ticks_completed": "2235",
    "paused": "no",
    "notes": (
        f"tick2235 leftover Entra 0406.645.972 Medium (omzet JUMP {OM25}; bruto {BR25} "
        f"~{RATIO}x; pnl {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 1 VE Fleurus ETA "
        "largest Walloon); after Ateliers Tertre@2234; AGB Bornem JR2024; FARO/AIESH/REW "
        "YE2024; Heropbeuring CW opaque; deferred Enghien/EntrAnam; next rq_2236; next "
        "every-10 2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2235 - 2026-08-27T00:15:00Z - rq_2235 Entra Fleurus (omzet JUMP 28.61m / bruto 35.33m ~1.23x / FTE 885 / Medium)

- Unit: **rq_2235** leftover dual after **rq_2234 Ateliers de Tertre**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Gandae/NLZ already mined. Took FREE unused Walloon ETA **Entra ASBL / Entraide par le Travail** YE2025 (KBO **0406.645.972**; Rue du Tilloi 11 Fleurus/Heppignies; **Actief** **1 VE**; NACE **88.993**; largest Walloon ETA). Deferred FREE **Enghien** / **EntrAnam**. Do not redo Ateliers Tertre/Le Rucher/Travie/SDB stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +5.41% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +0.30% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** DROP -2.17% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +3.98%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **30.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via scm@entra.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.50); entities (+1 vzw_entra_fleurus); foi + draft {GAP}; rq_2235=done + rq_2236 open; loop_state ticks=2235; raw docs/doge/raw/tick2235/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2236 (AGB/FARO-if-YE2025 / AIESH-REW / Enghien-EntrAnam-or-unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2235 Entra omzet={OM25} bruto={BR25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
