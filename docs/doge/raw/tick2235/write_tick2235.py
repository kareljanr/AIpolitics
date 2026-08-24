# tick2235 — Het Rekreatief YE2025 Medium leftover dual (unused maatwerk; after Ateliers@2234 race)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_het_rekreatief_wilrijk"
TICK = "2235"
UTC = "2026-08-27T00:10:00Z"
GAP = "gap_het_rekreatief_nbb_pdf_assets_debt_empty_omzet_pnl_profit_flip_matrix_l5"
COMM = "comm_het_rekreatief_jr2025_statutory_bruto_jump_pnl_profit_flip"
LB = "lb_het_rekreatief_bruto_2_42m_pnl_profit_flip_jr2025"

BR25, BR24 = 2420426, 1890365
PN25, PN24 = 75336, -107458
EQ25, EQ24 = 545451, 472787
FTE25, FTE24 = 57.4, 54.9
BR_PCT = round((BR25 - BR24) / BR24 * 100, 2)
EQ_PCT = round((EQ25 - EQ24) / EQ24 * 100, 2)


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
        "src_het_rekreatief_jr2025_cw_nl",
        "Companyweb NL Het Rekreatief YE2025 statutory",
        "https://www.companyweb.be/nl/0445687284/het-rekreatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet empty/unpublished; bruto JUMP {BR25} (+{BR_PCT}%) "
            f"pnl PROFIT FLIP {PN25} vs YE2024 LOSS {PN24}; equity JUMP {EQ25} (+{EQ_PCT}%); "
            f"FTE JUMP {FTE25}; filed 23-07-2026"
        ),
    ),
    (
        "src_het_rekreatief_jr2025_cw_en",
        "Companyweb EN Het Rekreatief YE2025 statutory",
        "https://www.companyweb.be/en/0445687284/het-rekreatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover unpublished; Gross margin {BR25}; Profit/Loss "
            f"{PN25}; Equity {EQ25}; Employees {FTE25}; filed 23-07-2026"
        ),
    ),
    (
        "src_het_rekreatief_jr2025_cw_fr",
        "Companyweb FR Het Rekreatief YE2025 statutory",
        "https://www.companyweb.be/fr/0445687284/het-rekreatief",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA unpublished; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_het_rekreatief_kbo_2235",
        "KBO Het Rekreatief 0445.687.284 Actief Wilrijk 2 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0445687284",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2235; Actief VZW; zetel Doornstraat 600 2610 Antwerpen; 2 VE Actief; "
            "NACE RSZ 88.993 beschutte/sociale werkplaatsen; BTW 88.999/56.220"
        ),
    ),
    (
        "src_het_rekreatief_site_contact_2235",
        "Het Rekreatief FOI channel info@rekreatief.be",
        "https://www.rekreatief.be/",
        "Het Rekreatief VZW",
        "foi_contact",
        "tick2235; info@rekreatief.be; jobs@rekreatief.be; 03 830 42 95; Doornstraat 600 2610 Wilrijk",
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
        "name_nl": "Het Rekreatief VZW (Wilrijk / collectief maatwerk)",
        "name_fr": "Het Rekreatief ASBL (Wilrijk / entreprise de travail adapte)",
        "name_en": "Het Rekreatief adapted-work VZW (Wilrijk maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.rekreatief.be/",
        "foi_email": "info@rekreatief.be",
        "foi_postal": "Doornstraat 600, 2610 Antwerpen",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0445.687.284 Actief 2 VE "
            f"NACE 88.993; omzet empty; bruto JUMP {BR25} (+{BR_PCT}%) pnl PROFIT FLIP "
            f"{PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 23.07.2026; "
            f"assets/debt Unknown; FOI {GAP}; preferred stall AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Stroom already mined; "
            "after Ateliers de Tertre@2234 race; not TE-additive"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_het_rekreatief_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary; omzet empty)",
        f"tick{TICK}; Medium CW; bruto JUMP +{BR_PCT}% vs YE2024 {BR24}; omzet unpublished",
    ),
    (
        "bud_het_rekreatief_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl PROFIT FLIP vs YE2024 LOSS {PN24}",
    ),
    (
        "bud_het_rekreatief_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +{EQ_PCT}% vs YE2024 {EQ24}",
    ),
    (
        "bud_het_rekreatief_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 57.4",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_het_rekreatief_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative (LOSS)",
        f"tick{TICK}; YE2024 pnl LOSS {PN24} comparative (pre PROFIT FLIP)",
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
            "source_id": "src_het_rekreatief_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_bruto":{BR25},"2025_omzet":"Unknown","2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_bruto":{BR24},"2024_pnl":{PN24},"2024_equity":{EQ24},'
    f'"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Het Rekreatief YE2025 leftover dual (bruto JUMP 2.42m / empty omzet / "
            "pnl PROFIT FLIP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "Maatwerk workers Antwerpen-Wilrijk / Villa Marienborgh events + groendienst "
            "public path"
        ),
        "legal_basis": (
            "VZW collectief maatwerk (KBO 0445.687.284; Actief; 2 VE; NACE 88.993)"
        ),
        "decision_date": "2026-07-23",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0445687284/het-rekreatief",
        "stated_goal": "Collectief maatwerk / green services + event catering Villa Marienborgh",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose empty-omzet behind bruto JUMP "
            f"+{BR_PCT}%; reconcile pnl PROFIT FLIP ({PN24}->+{PN25}) with FTE JUMP; "
            "WEWIS/VDAB maatwerk subsidy matrix; Villa Marienborgh cost allocation"
        ),
        "source_id": "src_het_rekreatief_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Antwerpen>Wilrijk>HetRekreatief>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; omzet empty; pnl PROFIT "
            f"FLIP; equity JUMP; FTE JUMP {FTE25}; 2 VE; preferred stall AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Stroom already mined; after "
            "Ateliers de Tertre@2234; not TE-additive"
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
            "Het Rekreatief bruto JUMP 2.42m / empty omzet / pnl PROFIT FLIP +75k (YE2025 maatwerk)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Antwerpen>Wilrijk>HetRekreatief>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto JUMP {BR25} (+{BR_PCT}%) / omzet empty / pnl PROFIT FLIP {PN25} "
            f"(from LOSS {PN24}) / equity JUMP {EQ25} / FTE JUMP {FTE25} / 2 VE Wilrijk"
        ),
        "confidence": "medium",
        "source_id": "src_het_rekreatief_jr2025_cw_en",
        "beneficiaries": "Maatwerk workers Antwerpen-Wilrijk / public adapted-work path",
        "stated_goal": "Collectief maatwerk / green + events Villa Marienborgh",
        "measured_outcome": (
            f"omzet unpublished; bruto JUMP +{BR_PCT}%; pnl PROFIT FLIP ({PN24}->+{PN25}); "
            f"equity JUMP +{EQ_PCT}%; FTE JUMP {FTE25} vs {FTE24}; 2 VE; filed 23.07.2026"
        ),
        "absurdity_score": "6.8",
        "cost_score": "4.5",
        "difficulty": "3.0",
        "priority_index": "5.90",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose empty-omzet vs bruto JUMP "
            f"+{BR_PCT}%; reconcile PROFIT FLIP with WEWIS/VDAB maatwerk subsidy matrix; "
            "Villa Marienborgh site cost allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; preferred stall Heropbeuring CW opaque / "
            "FARO YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem JR2024; Stroom already "
            "mined; after Ateliers@2234; next every-10 2240"
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
            "Vlaanderen>Antwerpen>Wilrijk>HetRekreatief>NBB_PDF_assets_debt_empty_omzet_pnl_profit_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); empty omzet behind "
            f"bruto EUR{BR25} (+{BR_PCT}%); pnl PROFIT FLIP EUR{PN25} vs YE2024 LOSS "
            f"EUR{PN24}; WEWIS/VDAB collectief-maatwerk subsidy matrix; Villa Marienborgh "
            f"/ groendienst cost split; FTE JUMP {FTE25} vs {FTE24} recon"
        ),
        "why_it_matters": (
            f"Medium CW shows VL maatwerk VZW (bruto JUMP 2.42m / empty omzet / {FTE25} FTE) "
            "with pnl PROFIT FLIP under public adapted-work path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Het Rekreatief VZW",
        "recipient_email": "info@rekreatief.be",
        "recipient_postal": "Doornstraat 600, 2610 Antwerpen",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall "
            "FARO/AIESH/REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; Stroom "
            "already mined; after Ateliers@2234; next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Het Rekreatief (NBB PDF / empty omzet / pnl PROFIT FLIP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Het Rekreatief VZW — KBO **0445.687.284** (Actief; Doornstraat 600, 2610 Antwerpen; **2 VE**; FTE {FTE25} CW; NACE **88.993** maatwerk)  
**recipient:** info@rekreatief.be · Doornstraat 600, 2610 Antwerpen (Wilrijk)  
**sources:** [CW EN](https://www.companyweb.be/en/0445687284/het-rekreatief) · [CW NL](https://www.companyweb.be/nl/0445687284/het-rekreatief) · [CW FR](https://www.companyweb.be/fr/0445687284/het-rekreatief) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445687284) · [site](https://www.rekreatief.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW; **2 VE**; zetel Doornstraat 600 Wilrijk/Antwerpen; NACE **88.993** Beschutte/sociale werkplaatsen (collectief maatwerk); Villa Mariënborgh events + groendienst.
- CW YE2025: omzet **empty/unpublished**; bruto **EUR{BR25:,}** JUMP +{BR_PCT}% vs YE2024 EUR{BR24:,}; pnl **EUR{PN25:,}** PROFIT FLIP vs YE2024 LOSS EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +{EQ_PCT}%; FTE **{FTE25}**; filed **23.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. Stroom Maatwerk already mined. After Ateliers de Tertre@2234 race — took unused Het Rekreatief.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Het Rekreatief VZW
via info@rekreatief.be
Doornstraat 600, 2610 Antwerpen
Betreft: Openbaarheid jaarrekening 2025 Het Rekreatief (KBO 0445.687.284)

Geachte,

Op grond van het Bestuursdecreet verzoek ik openbaarmaking van:

1. NBB/CBSO PDF jaarrekening YE2025 (balans + resultaten + toelichting; activa/schulden/cash).
2. Samenstelling brutomarge EUR{BR25} bij niet-gepubliceerde omzet (JUMP +{BR_PCT}% vs YE2024).
3. PnL PROFIT FLIP EUR{PN25} vs YE2024 verlies EUR{PN24} — reconciliatie met FTE JUMP naar {FTE25}.
4. Matrix WEWIS/VDAB / collectief-maatwerk toelagen achter bruto EUR{BR25}.
5. Kostentoerekening Villa Mariënborgh vs groendienst (2 VE).

Periode YE2025 (+ vergelijking YE2024). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
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
            "leftover dual — Het Rekreatief YE2025 Medium (bruto JUMP 2.42m / empty omzet / "
            "pnl PROFIT FLIP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "leftover dual after Ateliers de Tertre@2234; FARO/AIESH/REW still YE2024; "
            "Stroom already mined — take unused Het Rekreatief YE2025"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T23:50:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Het Rekreatief 0445.687.284 YE2025 Medium CW; bruto JUMP {BR25} "
            f"(+{BR_PCT}%) omzet empty pnl PROFIT FLIP {PN25} equity JUMP {EQ25} FTE JUMP "
            f"{FTE25}; 2 VE Wilrijk; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring "
            "CW opaque; Stroom already mined; after Ateliers@2234; next rq_2236; every-10 next 2240"
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
            "leftover dual hole-fill after Het Rekreatief — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Het Rekreatief Wilrijk YE2025 Medium (bruto JUMP 2.42m / "
            "empty omzet / pnl PROFIT FLIP). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if "
            "NBB/CW euros live, else unused maatwerk/kringloop/WZC/IGS/HVZ/ETA/VAPH. Do NOT "
            "redo Het Rekreatief, Ateliers de Tertre, Le Rucher, Travie, SDB, De Vleugels, "
            "Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, "
            "Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel "
            "Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, "
            "Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize "
            "Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, "
            "Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, "
            "Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, "
            "BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, "
            "Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, "
            "De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
            "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, "
            "Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter "
            "(YE2024), Aralea (YE2024), Gandae (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, "
            "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, "
            "Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, "
            "Elia, BNO, SWDE, BRUGEL. Candidates if YE2025 live: De Enter Brecht / De Ploeg "
            "Sint-Truiden / De Dageraad Kontich / IN-Z Genk / BUSELOC / RODEA / Den Diepen "
            "Boomgaard / Vlaspit / Aurora / TWERK if YE2025. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2235 Het Rekreatief; FARO/AIESH/REW YE2024; AGB Bornem "
            "JR2024; Heropbeuring CW opaque; Stroom already mined; Ateliers@2234 done"
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
        f"tick2235 leftover Het Rekreatief 0445.687.284 Medium (bruto JUMP {BR25} "
        f"+{BR_PCT}%; empty omzet; pnl PROFIT FLIP {PN25}; equity JUMP {EQ25}; FTE JUMP "
        f"{FTE25}; 2 VE Wilrijk); preferred stall FARO/AIESH/REW YE2024; AGB Bornem "
        "JR2024; Heropbeuring CW opaque; Stroom already mined; after Ateliers@2234; "
        "next rq_2236; next every-10 2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2235 - 2026-08-27T00:10:00Z - rq_2235 Het Rekreatief Wilrijk (bruto JUMP 2.42m / empty omzet / pnl PROFIT FLIP / Medium)

- Unit: **rq_2235** leftover dual after **rq_2234 Ateliers de Tertre** (race took 2234). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (CW last balance 2024; NBB YE2025 unpublished); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Stroom Maatwerk already mined — skipped. Took FREE unused leftover **Het Rekreatief VZW** YE2025 (KBO **0445.687.284**; Doornstraat 600 Wilrijk; **Actief** **2 VE**; NACE **88.993** collectief maatwerk / Villa Mariënborgh + groendienst). Do not redo Ateliers/Le Rucher/Travie/SDB/De Vleugels/Kiemkracht/De Oever/Stroom stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **empty/unpublished**; bruto **EUR{BR25}** JUMP +{BR_PCT}% vs YE2024 EUR{BR24}; pnl **EUR{PN25}** PROFIT FLIP vs YE2024 LOSS EUR{PN24}; equity **EUR{EQ25}** JUMP +{EQ_PCT}%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **23.07.2026**. Strong KBO Actief 2 VE. Assets/debt Unknown. Medium. FOI via info@rekreatief.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.90); entities (+1 vzw_het_rekreatief_wilrijk); foi + draft {GAP}; rq_2235=done + rq_2236 open; loop_state ticks=2235; raw docs/doge/raw/tick2235/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2236 (AGB/FARO-if-YE2025 / AIESH-REW / unused-VAPH-WZC-maatwerk).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2235 Het Rekreatief bruto={BR25} pnl={PN25} equity={EQ25} FTE={FTE25} "
    f"bruto_pct=+{BR_PCT}"
)
