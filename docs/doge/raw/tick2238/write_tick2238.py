# tick2238 — Metalgroup ETA Charleroi YE2025 Medium leftover dual (unused after EntrAnam)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_metalgroup_eta_charleroi"
TICK = "2238"
UTC = "2026-08-27T01:25:00Z"
GAP = "gap_metalgroup_nbb_pdf_assets_debt_bruto_gt_omzet_2_21x_pnl_drop_69pct_eta_matrix_l5"
COMM = "comm_metalgroup_jr2025_statutory_eta_bruto_gt_omzet_pnl_drop"
LB = "lb_metalgroup_bruto_6_62m_gt_omzet_2_21x_pnl_drop_69pct_jr2025"

OM25, OM24 = 2987007, 2644698
BR25, BR24 = 6616725, 6123186
PN25, PN24 = 62047, 202314
EQ25, EQ24 = 5412773, 5359893
FTE25, FTE24 = 172.4, 163.7
RATIO = round(BR25 / OM25, 2)  # ~2.21


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
        "src_metalgroup_jr2025_cw_nl",
        "Companyweb NL Metalgroup ETA YE2025 statutory",
        "https://www.companyweb.be/nl/0407623001/asbl-metalgroup-eta",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+12.94%) bruto JUMP {BR25} (+8.06% "
            f"bruto≫omzet ~{RATIO}x) pnl DROP {PN25} (-69.33%) vs YE2024 {PN24} equity JUMP "
            f"{EQ25} (+0.99%) FTE JUMP {FTE25}; filed 22-06-2026"
        ),
    ),
    (
        "src_metalgroup_jr2025_cw_en",
        "Companyweb EN Metalgroup ETA YE2025 statutory",
        "https://www.companyweb.be/en/0407623001/asbl-metalgroup-eta",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 22-06-2026"
        ),
    ),
    (
        "src_metalgroup_jr2025_cw_fr",
        "Companyweb FR Metalgroup ETA YE2025 statutory",
        "https://www.companyweb.be/fr/0407623001/asbl-metalgroup-eta",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_metalgroup_kbo_2238",
        "KBO Metalgroup ETA 0407.623.001 Actief Charleroi 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407623001",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2238; Actief ASBL Metalgroup ETA; zetel Rue du Debarcadere 61 6001 Charleroi; "
            "1 VE; RSZ NACE 88.993; BTW 25.401; aanbestedende overheid; erkenning aannemer"
        ),
    ),
    (
        "src_metalgroup_site_contact_2238",
        "Metalgroup FOI channel info@metalgroup.be",
        "https://www.metalgroup.be/",
        "Metalgroup ETA ASBL",
        "foi_contact",
        "tick2238; info@metalgroup.be; +32 71 36 00 15; Rue du Debarcadere 61 6001 Marcinelle",
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
        "name_nl": "Metalgroup ETA ASBL (Charleroi / Marcinelle maatwerk)",
        "name_fr": "ASBL Metalgroup ETA (entreprise de travail adapte Charleroi)",
        "name_en": "Metalgroup ETA adapted-work ASBL (Charleroi / Marcinelle)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.metalgroup.be/",
        "foi_email": "info@metalgroup.be",
        "foi_postal": "Rue du Debarcadere 61, 6001 Charleroi",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.623.001 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} bruto {BR25} (~{RATIO}x) pnl DROP {PN25} "
            f"(-69%) equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 22.06.2026; "
            f"assets/debt Unknown; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO NBB YE2024 (JV2025 already mapped); AIESH/REW YE2024; Heropbeuring CW "
            "opaque; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_metalgroup_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +8.06% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_metalgroup_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +12.94% vs YE2024 {OM24}",
    ),
    (
        "bud_metalgroup_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -69.33% vs YE2024 {PN24}",
    ),
    (
        "bud_metalgroup_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +0.99% vs YE2024 {EQ24}",
    ),
    (
        "bud_metalgroup_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 172.4",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_metalgroup_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative",
        f"tick{TICK}; YE2024 pnl {PN24} comparative (pre DROP)",
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
            "source_id": "src_metalgroup_jr2025_cw_en",
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
            "Metalgroup ETA YE2025 leftover dual (bruto 6.62m / bruto≫omzet ~2.21x / "
            "pnl DROP -69% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Charleroi-Marcinelle / Walloon AVIQ adapted-work path"
        ),
        "legal_basis": (
            "ASBL ETA Metalgroup (KBO 0407.623.001; Actief; 1 VE; NACE 88.993; "
            "aanbestedende overheid)"
        ),
        "decision_date": "2026-06-22",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0407623001/asbl-metalgroup-eta",
        "stated_goal": "Adapted work / ETA Charleroi (metal/tole/usinage/ferronnerie)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~2.21x; reconcile pnl "
            "DROP -69% (202k->62k) with AVIQ ETA wage-intervention matrix; FTE JUMP vs "
            "profit squeeze"
        ),
        "source_id": "src_metalgroup_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Charleroi>Metalgroup_ETA>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl DROP -69%; equity JUMP; FTE JUMP {FTE25}; 1 VE; unused after EntrAnam; "
            "AGB Bornem JR2024; FARO NBB YE2024; AIESH/REW YE2024; Heropbeuring CW opaque; "
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
            "Metalgroup ETA bruto 6.62m / bruto≫omzet ~2.21x / pnl DROP -69% (YE2025 ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Hainaut>Charleroi>Metalgroup_ETA>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet JUMP {OM25} (~{RATIO}x) / pnl DROP {PN25} "
            f"(from {PN24}) / equity JUMP {EQ25} / FTE JUMP {FTE25} / 1 VE Charleroi ETA"
        ),
        "confidence": "medium",
        "source_id": "src_metalgroup_jr2025_cw_en",
        "beneficiaries": "ETA workers Charleroi / AVIQ Walloon adapted-work path",
        "stated_goal": "Adapted work / ETA Charleroi metal",
        "measured_outcome": (
            f"omzet JUMP +12.94%; bruto≫omzet ~{RATIO}x; pnl DROP -69.33% (202k->62k); "
            f"equity JUMP +0.99%; FTE JUMP {FTE25}; 1 VE; filed 22.06.2026"
        ),
        "absurdity_score": "7.1",
        "cost_score": "5.3",
        "difficulty": "3.0",
        "priority_index": "6.20",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~2.21x vs AVIQ ETA "
            "matrix; reconcile pnl DROP -69% despite omzet/bruto JUMP and FTE JUMP; site "
            "cost allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; after EntrAnam@2237; stall Heropbeuring CW "
            "opaque / FARO NBB YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem JR2024; "
            "next every-10 2240"
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
            "Wallonie>Hainaut>Charleroi>Metalgroup_ETA>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl DROP EUR{PN25} vs YE2024 EUR{PN24} (-69%); "
            f"AVIQ/AWIPH ETA subsidy matrix; FTE JUMP {FTE25} vs profit squeeze"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL Charleroi (bruto 6.62m / omzet 2.99m / "
            f"~{RATIO}x / pnl DROP -69% / {FTE25} FTE) under public AVIQ path; assets/debt "
            "unpublished"
        ),
        "priority": "8",
        "recipient_body": "ASBL Metalgroup ETA",
        "recipient_email": "info@metalgroup.be",
        "recipient_postal": "Rue du Debarcadere 61, 6001 Charleroi",
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
            "FARO NBB YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Metalgroup ETA (NBB PDF / bruto≫omzet ~{RATIO}x / pnl DROP -69%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ASBL Metalgroup ETA — KBO **0407.623.001** (Actief; Rue du Débarcadère 61, 6001 Charleroi; **1 VE**; FTE {FTE25} CW; NACE **88.993**; aanbestedende overheid)  
**recipient:** info@metalgroup.be · Rue du Débarcadère 61, 6001 Marcinelle  
**sources:** [CW EN](https://www.companyweb.be/en/0407623001/asbl-metalgroup-eta) · [CW NL](https://www.companyweb.be/nl/0407623001/asbl-metalgroup-eta) · [CW FR](https://www.companyweb.be/fr/0407623001/asbl-metalgroup-eta) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407623001) · [site](https://www.metalgroup.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Rue du Débarcadère Charleroi/Marcinelle; RSZ NACE **88.993**; BTW 25.401; aanbestedende overheid; erkenning aannemer.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +12.94% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +8.06% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** DROP −69.33% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +0.99%; FTE **{FTE25}** JUMP vs {FTE24}; filed **22.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO NBB YE2024 (JV2025 already mapped); AIESH/REW YE2024; Heropbeuring CW opaque.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ASBL Metalgroup ETA
via info@metalgroup.be
Rue du Debarcadere 61, 6001 Charleroi
Objet: Publicite des comptes annuels 2025 Metalgroup ETA (BCE 0407.623.001)

Madame, Monsieur,

Sur la base du decret wallon relatif a la publicite de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + resultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL DROP EUR{PN25} (-69,33%) vs benefice YE2024 EUR{PN24} — drivers malgre CA/bruto en hausse.
4. Matrice des interventions AVIQ/AWIPH / subsides ETA derriere la marge brute EUR{BR25}.
5. Effectifs FTE JUMP {FTE25} vs {FTE24} — allocation des couts du site (1 UE).

Periode YE2025 (+ comparative YE2024). Ref: {GAP}

Veuillez agreer, Madame, Monsieur, l'expression de mes salutations distinguees,
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
    "rq_2238",
    {
        "task_id": "rq_2238",
        "title": (
            "leftover dual — Metalgroup ETA YE2025 Medium (bruto 6.62m / bruto≫omzet "
            "~2.21x / pnl DROP -69%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after EntrAnam; unused FREE Metalgroup ETA Charleroi",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T01:05:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Metalgroup 0407.623.001 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl DROP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; 1 VE "
            "Charleroi; AGB Bornem JR2024; FARO NBB YE2024; AIESH/REW YE2024; Heropbeuring "
            "CW opaque; next rq_2239; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2239",
    {
        "task_id": "rq_2239",
        "title": (
            "leftover dual hole-fill after Metalgroup — prefer AGB/FARO-NBB-YE2025/"
            "AIESH-REW/Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Metalgroup ETA Charleroi YE2025 Medium (bruto 6.62m / "
            "bruto≫omzet ~2.21x / pnl DROP -69%). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025 (JV2025 already mapped — skip redo), else "
            "AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else unused "
            "maatwerk/kringloop/WZC/IGS/HVZ/ETA. Do NOT redo Metalgroup, EntrAnam, Enghien, "
            "Entra, Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, "
            "Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, "
            "Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel "
            "Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, "
            "Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, "
            "Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, "
            "Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP "
            "Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, "
            "BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
            "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
            "InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, "
            "Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, "
            "Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), Gandae "
            "(YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, "
            "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
            "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2238 Metalgroup; FARO NBB YE2024; AIESH/REW YE2024; "
            "AGB Bornem JR2024; Heropbeuring CW opaque"
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
    "last_unit_id": "rq_2238",
    "ticks_completed": "2238",
    "paused": "no",
    "notes": (
        f"tick2238 leftover Metalgroup ETA 0407.623.001 Medium (bruto {BR25} ~{RATIO}x "
        f"omzet {OM25}; pnl DROP {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 1 VE "
        "Charleroi); after EntrAnam@2237; AGB Bornem JR2024; FARO NBB YE2024; "
        "AIESH/REW YE2024; Heropbeuring CW opaque; next rq_2239; next every-10 2240; "
        "continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2238 - 2026-08-27T01:25:00Z - rq_2238 Metalgroup ETA Charleroi (bruto 6.62m / bruto≫omzet ~2.21x / pnl DROP -69% / Medium)

- Unit: **rq_2238** leftover dual after **rq_2237 EntrAnam**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **NBB YE2024** (JV2025 already mapped — skip redo); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE unused Walloon ETA **ASBL Metalgroup ETA** YE2025 (KBO **0407.623.001**; Rue du Débarcadère 61 Charleroi/Marcinelle; **Actief** **1 VE**; NACE **88.993**). Do not redo EntrAnam/Enghien/Entra/Ateliers Tertre/Le Rucher/Het Rekreatief stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +12.94% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +8.06% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** DROP -69.33% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +0.99%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **22.06.2026**. Strong KBO Actief 1 VE aanbestedende overheid. Assets/debt Unknown. Medium. FOI via info@metalgroup.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 vzw_metalgroup_eta_charleroi); foi + draft {GAP}; rq_2238=done + rq_2239 open; loop_state ticks=2238; raw docs/doge/raw/tick2238/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2239 (AGB/FARO-if-NBB-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2238 Metalgroup bruto={BR25} omzet={OM25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
