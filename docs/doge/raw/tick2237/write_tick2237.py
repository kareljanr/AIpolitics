# tick2237 — EntrAnam YE2025 Medium leftover dual (named FREE after Enghien)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_entranam_fernelmont"
TICK = "2237"
UTC = "2026-08-27T01:05:00Z"
GAP = "gap_entranam_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_deepen_eta_matrix_l5"
COMM = "comm_entranam_jr2025_statutory_eta_bruto_gt_omzet_pnl_loss_deepen"
LB = "lb_entranam_bruto_7_66m_gt_omzet_1_83x_pnl_loss_deepen_jr2025"

OM25, OM24 = 4197245, 4343098
BR25, BR24 = 7663710, 7814918
PN25, PN24 = -301095, -71506
EQ25, EQ24 = 7865533, 8204226
FTE25, FTE24 = 233.7, 233.6
RATIO = round(BR25 / OM25, 2)  # ~1.83


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
        "src_entranam_jr2025_cw_nl",
        "Companyweb NL EntrAnam YE2025 statutory",
        "https://www.companyweb.be/nl/0407273801/l-entraide-par-le-travail-de-namur",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet DROP {OM25} (-3.36%) bruto DROP {BR25} (-1.93% "
            f"bruto≫omzet ~{RATIO}x) pnl LOSS DEEPEN {PN25} vs YE2024 {PN24} equity DROP "
            f"{EQ25} (-4.13%) FTE {FTE25}; filed 21-05-2026"
        ),
    ),
    (
        "src_entranam_jr2025_cw_en",
        "Companyweb EN EntrAnam YE2025 statutory",
        "https://www.companyweb.be/en/0407273801/l-entraide-par-le-travail-de-namur",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 21-05-2026"
        ),
    ),
    (
        "src_entranam_jr2025_cw_fr",
        "Companyweb FR EntrAnam YE2025 statutory",
        "https://www.companyweb.be/fr/0407273801/l-entraide-par-le-travail-de-namur",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_entranam_kbo_2237",
        "KBO EntrAnam 0407.273.801 Actief Fernelmont 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407273801",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2237; Actief ASBL L'Entraide par le Travail de Namur / EntrAnam; zetel "
            "Rue du Tronquoy ZI Nov. 10 5380 Fernelmont; 1 VE; NACE RSZ 88.993; "
            "erkenning aannemer; DISTINCT Enghien/Entra Fleurus"
        ),
    ),
    (
        "src_entranam_site_contact_2237",
        "EntrAnam FOI channel info@entranam.be",
        "https://www.entranam.be/",
        "EntrAnam ASBL",
        "foi_contact",
        "tick2237; info@entranam.be; secretariat@entranam.be; 081 71 92 00; Rue du Tronquoy 10 Fernelmont",
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
        "name_nl": "EntrAnam ASBL (Fernelmont / ETA Namur maatwerk)",
        "name_fr": "EntrAnam ASBL / L'Entraide par le Travail de Namur (ETA Fernelmont)",
        "name_en": "EntrAnam adapted-work ASBL (Fernelmont Namur ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.entranam.be/",
        "foi_email": "info@entranam.be",
        "foi_postal": "Rue du Tronquoy ZI Nov. 10, 5380 Fernelmont",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.273.801 Actief 1 VE "
            f"NACE 88.993; omzet DROP {OM25} bruto {BR25} (~{RATIO}x) pnl LOSS DEEPEN "
            f"{PN25} equity DROP {EQ25} FTE {FTE25}; neerlegging 21.05.2026; assets/debt "
            f"Unknown; FOI {GAP}; DISTINCT Enghien/Entra Fleurus; preferred stalls AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_entranam_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto DROP -1.93% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_entranam_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet DROP -3.36% vs YE2024 {OM24}",
    ),
    (
        "bud_entranam_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl LOSS DEEPEN vs YE2024 LOSS {PN24}",
    ),
    (
        "bud_entranam_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -4.13% vs YE2024 {EQ24}",
    ),
    (
        "bud_entranam_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 233.7",
        f"tick{TICK}; Medium CW; FTE {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_entranam_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative (LOSS)",
        f"tick{TICK}; YE2024 pnl LOSS {PN24} comparative (pre DEEPEN)",
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
            "source_id": "src_entranam_jr2025_cw_en",
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
            "EntrAnam YE2025 leftover dual (bruto 7.66m / bruto≫omzet ~1.83x / "
            "pnl LOSS DEEPEN -301k / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "ETA workers Namur (Fernelmont/Noville-les-Bois) / Walloon AVIQ adapted-work path"
        ),
        "legal_basis": (
            "ASBL ETA EntrAnam (KBO 0407.273.801; Actief; 1 VE; NACE 88.993; "
            "DISTINCT Enghien/Entra Fleurus)"
        ),
        "decision_date": "2026-05-21",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            "https://www.companyweb.be/en/0407273801/l-entraide-par-le-travail-de-namur"
        ),
        "stated_goal": "Adapted work / ETA Namur (metal/electronics/building)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.83x; reconcile pnl "
            "LOSS DEEPEN (-72k->-301k) with AVIQ ETA wage-intervention matrix; equity DROP "
            "-4% vs ongoing losses"
        ),
        "source_id": "src_entranam_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Namur>Fernelmont>EntrAnam>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl LOSS DEEPEN; equity DROP; FTE {FTE25}; 1 VE; named prefer in rq_2237 after "
            "Enghien; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
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
            "EntrAnam bruto 7.66m / bruto≫omzet ~1.83x / pnl LOSS DEEPEN -301k (YE2025 ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Namur>Fernelmont>EntrAnam>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet DROP {OM25} (~{RATIO}x) / pnl LOSS DEEPEN {PN25} "
            f"(from {PN24}) / equity DROP {EQ25} / FTE {FTE25} / 1 VE Fernelmont ETA"
        ),
        "confidence": "medium",
        "source_id": "src_entranam_jr2025_cw_en",
        "beneficiaries": "ETA workers Namur / AVIQ Walloon adapted-work path",
        "stated_goal": "Adapted work / ETA Namur",
        "measured_outcome": (
            f"omzet DROP -3.36%; bruto≫omzet ~{RATIO}x; pnl LOSS DEEPEN (-72k->-301k); "
            f"equity DROP -4.13%; FTE flat {FTE25}; 1 VE; filed 21.05.2026"
        ),
        "absurdity_score": "7.3",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.83x vs AVIQ ETA "
            "matrix; reconcile LOSS DEEPEN second consecutive year; equity DROP vs ongoing "
            "losses; site cost allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; DISTINCT Enghien@2236 / Entra@2235; stall "
            "Heropbeuring CW opaque / FARO YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem "
            "JR2024; next every-10 2240"
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
            "Wallonie>Namur>Fernelmont>EntrAnam>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_deepen"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x); pnl LOSS DEEPEN EUR{PN25} vs YE2024 EUR{PN24}; "
            f"AVIQ/AWIPH ETA subsidy matrix; equity DROP EUR{EQ25} vs consecutive losses"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL Namur (bruto 7.66m / omzet 4.20m / ~{RATIO}x / "
            f"pnl LOSS DEEPEN -301k / {FTE25} FTE) under public AVIQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "EntrAnam ASBL / L'Entraide par le Travail de Namur",
        "recipient_email": "info@entranam.be",
        "recipient_postal": "Rue du Tronquoy ZI Nov. 10, 5380 Fernelmont",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; cc secretariat@entranam.be; "
            "preferred stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; "
            "next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — EntrAnam (NBB PDF / bruto≫omzet ~{RATIO}x / pnl LOSS DEEPEN)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** EntrAnam ASBL / L'Entraide par le Travail de Namur — KBO **0407.273.801** (Actief; Rue du Tronquoy 10, 5380 Fernelmont; **1 VE**; FTE {FTE25} CW; NACE **88.993**; DISTINCT Enghien/Entra Fleurus)  
**recipient:** info@entranam.be · cc secretariat@entranam.be · Rue du Tronquoy 10, 5380 Noville-les-Bois  
**sources:** [CW EN](https://www.companyweb.be/en/0407273801/l-entraide-par-le-travail-de-namur) · [CW NL](https://www.companyweb.be/nl/0407273801/l-entraide-par-le-travail-de-namur) · [CW FR](https://www.companyweb.be/fr/0407273801/l-entraide-par-le-travail-de-namur) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407273801) · [site](https://www.entranam.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Rue du Tronquoy Fernelmont; NACE **88.993**; erkenning aannemer.
- CW YE2025: omzet **EUR{OM25:,}** DROP −3.36% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP −1.93% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** LOSS DEEPEN vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** DROP −4.13%; FTE **{FTE25}**; filed **21.05.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: EntrAnam ASBL / L'Entraide par le Travail de Namur
via info@entranam.be (cc: secretariat@entranam.be)
Rue du Tronquoy 10, 5380 Fernelmont
Objet: Publicité des comptes annuels 2025 EntrAnam (BCE 0407.273.801)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. PnL LOSS DEEPEN EUR{PN25} vs perte YE2024 EUR{PN24} — réconciliation et plan de redressement.
4. Matrice des interventions AVIQ/AWIPH / subsides ETA derrière la marge brute EUR{BR25}.
5. Allocation des coûts du site (1 UE).

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
    "rq_2237",
    {
        "task_id": "rq_2237",
        "title": (
            "leftover dual — EntrAnam YE2025 Medium (bruto 7.66m / bruto≫omzet ~1.83x / "
            "pnl LOSS DEEPEN)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": "leftover dual after Enghien; named FREE EntrAnam",
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T00:40:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; EntrAnam 0407.273.801 YE2025 Medium CW; bruto {BR25} (~{RATIO}x "
            f"omzet {OM25}) pnl LOSS DEEPEN {PN25} equity DROP {EQ25} FTE {FTE25}; 1 VE "
            "Fernelmont; DISTINCT Enghien/Entra; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; next rq_2238; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2238",
    {
        "task_id": "rq_2238",
        "title": (
            "leftover dual hole-fill after EntrAnam — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after EntrAnam Fernelmont YE2025 Medium (bruto 7.66m / bruto≫omzet "
            "~1.83x / pnl LOSS DEEPEN). Prefer leftover AGB/APB if JR2025 PDF live, else FARO "
            "if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros "
            "live, else unused maatwerk/kringloop/WZC/IGS/HVZ/ETA. Do NOT redo EntrAnam, "
            "Enghien, Entra, Ateliers de Tertre, Le Rucher, Travie, SDB, De Vleugels, "
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
            "spawned after tick2237 EntrAnam; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque"
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
    "last_unit_id": "rq_2237",
    "ticks_completed": "2237",
    "paused": "no",
    "notes": (
        f"tick2237 leftover EntrAnam 0407.273.801 Medium (bruto {BR25} ~{RATIO}x omzet "
        f"{OM25}; pnl LOSS DEEPEN {PN25}; equity DROP {EQ25}; FTE {FTE25}; 1 VE Fernelmont); "
        "after Enghien@2236; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
        "opaque; next rq_2238; next every-10 2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2237 - 2026-08-27T01:05:00Z - rq_2237 EntrAnam Fernelmont (bruto 7.66m / bruto≫omzet ~1.83x / pnl LOSS DEEPEN / Medium)

- Unit: **rq_2237** leftover dual after **rq_2236 Enghien**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE **EntrAnam ASBL / L'Entraide par le Travail de Namur** YE2025 (KBO **0407.273.801**; Rue du Tronquoy 10 Fernelmont; **Actief** **1 VE**; NACE **88.993**) — named prefer in rq_2237. DISTINCT from Enghien/Entra Fleurus. Do not redo Enghien/Entra/Ateliers Tertre stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP -3.36% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -1.93% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** LOSS DEEPEN vs YE2024 EUR{PN24}; equity **EUR{EQ25}** DROP -4.13%; FTE **{FTE25}**; neerlegging **21.05.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@entranam.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 vzw_entranam_fernelmont); foi + draft {GAP}; rq_2237=done + rq_2238 open; loop_state ticks=2237; raw docs/doge/raw/tick2237/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2238 (AGB/FARO-if-YE2025 / AIESH-REW / unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2237 EntrAnam bruto={BR25} omzet={OM25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
