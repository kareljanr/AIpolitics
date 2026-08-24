# tick2230 — EVERY-10 + Kiemkracht YE2025 Medium leftover dual (FREE after De Oever)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_kiemkracht_hamme"
TICK = "2230"
UTC = "2026-08-26T22:20:00Z"
GAP = "gap_kiemkracht_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_75pct_matrix_l5"
COMM = "comm_kiemkracht_jr2025_statutory_maatwerk_omzet_jump_pnl_drop_75pct"
LB = "lb_kiemkracht_omzet_13_26m_bruto_gt_omzet_pnl_drop_75pct_jr2025"

OM25, OM24 = 13257892, 12162919
BR25, BR24 = 18730949, 17254418
PN25, PN24 = 322935, 1296587
EQ25, EQ24 = 9211065, 8894630
FTE25, FTE24 = 404.4, 370.4
RATIO = round(BR25 / OM25, 2)  # ~1.41


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
        "src_kiemkracht_jr2025_cw_nl",
        "Companyweb NL Kiemkracht YE2025 statutory",
        "https://www.companyweb.be/nl/0454343743/kiemkracht",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+9.00%) bruto JUMP {BR25} (+8.56% "
            f"bruto≫omzet ~{RATIO}x) pnl DROP {PN25} (-75.09%) equity JUMP {EQ25} (+3.56%) "
            f"FTE {FTE25}; filed 16-06-2026"
        ),
    ),
    (
        "src_kiemkracht_jr2025_cw_en",
        "Companyweb EN Kiemkracht YE2025 statutory",
        "https://www.companyweb.be/en/0454343743/kiemkracht",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 16-06-2026"
        ),
    ),
    (
        "src_kiemkracht_jr2025_cw_fr",
        "Companyweb FR Kiemkracht YE2025 statutory",
        "https://www.companyweb.be/fr/0454343743/kiemkracht",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_kiemkracht_kbo_2230",
        "KBO Kiemkracht 0454.343.743 Actief Hamme 13 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0454343743",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2230; Actief VZW; zetel Zwaarveld 57 9220 Hamme; 13 VE Actief; "
            "NACE RSZ/BTW 88.993 Beschutte en sociale werkplaatsen; absorbed Pro Natura "
            "0463.036.032 + Pro Natura Sociale Werkplaats 0466.462.409 since 01.01.2023; "
            "DISTINCT De Kemphaan Hamme 0425.803.472"
        ),
    ),
    (
        "src_kiemkracht_site_contact_2230",
        "Kiemkracht FOI channel info@kiemkracht.org",
        "https://kiemkracht.org/",
        "Kiemkracht VZW",
        "foi_contact",
        "tick2230; info@kiemkracht.org; 052 48 00 60; Zwaarveld 57 9220 Hamme; maatwerk+kringwinkel",
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
        "name_nl": "Kiemkracht VZW (Hamme / maatwerk / Kringwinkel)",
        "name_fr": "Kiemkracht ASBL (Hamme / entreprise de travail adapte / ressourcerie)",
        "name_en": "Kiemkracht adapted-work VZW (Hamme; maatwerk + Kringwinkel)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://kiemkracht.org/",
        "foi_email": "info@kiemkracht.org",
        "foi_postal": "Zwaarveld 57, 9220 Hamme",
        "notes": (
            f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0454.343.743 Actief "
            f"13 VE NACE 88.993; omzet JUMP {OM25} bruto JUMP {BR25} (~{RATIO}x) pnl DROP "
            f"{PN25} (-75.09%) equity JUMP {EQ25} FTE JUMP {FTE25}; neerlegging 16.06.2026; "
            f"assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW "
            "YE2024; Heropbeuring CW opaque; NOT De Kemphaan Hamme; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_kiemkracht_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +9.00% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_kiemkracht_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +8.56% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_kiemkracht_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -75.09% vs YE2024 {PN24}",
    ),
    (
        "bud_kiemkracht_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +3.56% vs YE2024 {EQ24}",
    ),
    (
        "bud_kiemkracht_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 404.4",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_kiemkracht_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_kiemkracht_jr2025_cw_en",
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
            "Kiemkracht YE2025 leftover dual (omzet JUMP 13.26m / bruto≫omzet ~1.41x / "
            "pnl DROP -75% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "maatwerk workers East-Flanders (Hamme/Dendermonde/Zele/Puurs) + Kringwinkel "
            "clients / public ESF-VDAB path"
        ),
        "legal_basis": (
            "VZW maatwerk / beschutte werkplaats (KBO 0454.343.743; Actief; 13 VE; NACE 88.993)"
        ),
        "decision_date": "2026-06-16",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0454343743/kiemkracht",
        "stated_goal": "Adapted work + reuse/Kringwinkel (Mens Natuur Toekomst)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~1.41x; reconcile pnl DROP "
            "-75% (1.30m->0.32m) despite omzet/FTE JUMP with public maatwerk/ESF subsidy matrix; "
            "per-VE (13) cost allocation; Pro Natura absorb effects"
        ),
        "source_id": "src_kiemkracht_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Hamme>Kiemkracht>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK} EVERY-10; Medium CW; omzet primary envelope {OM25}; bruto≫omzet "
            f"~{RATIO}x; pnl DROP -75.09%; equity JUMP; FTE JUMP {FTE25}; 13 VE; FREE after "
            "De Oever stalls (AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque); "
            "NOT De Kemphaan; not TE-additive"
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
            "Kiemkracht omzet JUMP 13.26m / bruto≫omzet ~1.41x / pnl DROP -75% (YE2025 maatwerk)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Hamme>Kiemkracht>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} (~{RATIO}x) / pnl DROP {PN25} (-75.09% from "
            f"{PN24}) / equity {EQ25} / FTE JUMP {FTE25} / 13 VE Hamme maatwerk+kringwinkel"
        ),
        "confidence": "medium",
        "source_id": "src_kiemkracht_jr2025_cw_en",
        "beneficiaries": "maatwerk workers Oost-Vlaanderen / Kringwinkel clients / ESF-VDAB path",
        "stated_goal": "Adapted work + circular reuse (Mens Natuur Toekomst)",
        "measured_outcome": (
            f"omzet JUMP +9.00%; bruto≫omzet ~{RATIO}x; pnl crater -75.09% (1.30m->0.32m); "
            f"equity +3.56%; FTE JUMP {FTE25} vs {FTE24}; 13 VE; filed 16.06.2026"
        ),
        "absurdity_score": "7.3",
        "cost_score": "5.8",
        "difficulty": "3.0",
        "priority_index": "6.50",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.41x composition; "
            "reconcile pnl DROP -75% with public maatwerk/ESF/gemeente subsidy matrix despite "
            "omzet+FTE growth; 13-VE + Pro Natura absorb cost allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / "
            "FARO YE2024 / AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after De Oever@2229; "
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
            "Vlaanderen>OostVlaanderen>Hamme>Kiemkracht>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop_75pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x) composition; pnl DROP EUR{PN25} vs YE2024 EUR{PN24} "
            f"(-75.09%) recon despite omzet/FTE JUMP; ESF/VDAB/gemeente/maatwerk subsidy matrix; "
            f"13 VE + Pro Natura absorb (0463.036.032 / 0466.462.409) cost allocation"
        ),
        "why_it_matters": (
            f"Medium CW shows Oost-Vlaanderen maatwerk+Kringwinkel VZW (omzet 13.26m / "
            f"{FTE25} FTE / 13 VE) with bruto≫omzet ~{RATIO}x and pnl crater -75% under public "
            "maatwerk path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Kiemkracht VZW",
        "recipient_email": "info@kiemkracht.org",
        "recipient_postal": "Zwaarveld 57, 9220 Hamme",
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
    f"""# FOI draft — Kiemkracht (NBB PDF / bruto≫omzet / pnl DROP −75%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Kiemkracht VZW — KBO **0454.343.743** (Actief; Zwaarveld 57, 9220 Hamme; **13 VE**; FTE {FTE25} CW; NACE **88.993**)  
**recipient:** info@kiemkracht.org · Zwaarveld 57, 9220 Hamme  
**sources:** [CW EN](https://www.companyweb.be/en/0454343743/kiemkracht) · [CW NL](https://www.companyweb.be/nl/0454343743/kiemkracht) · [CW FR](https://www.companyweb.be/fr/0454343743/kiemkracht) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0454343743) · [site](https://kiemkracht.org/)  
**tick:** {TICK} EVERY-10  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW; **13 VE**; zetel Zwaarveld 57 Hamme; NACE **88.993** Beschutte en sociale werkplaatsen; absorbed Pro Natura 0463.036.032 + 0466.462.409 since 01.01.2023. DISTINCT from De Kemphaan Hamme 0425.803.472.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +9.00% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +8.56% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** DROP −75.09% vs YE2024 EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +3.56%; FTE **{FTE25}**; filed **16.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Kiemkracht VZW
via info@kiemkracht.org
Zwaarveld 57, 9220 Hamme
Betreft: Openbaarmaking jaarrekening 2025 Kiemkracht (KBO 0454.343.743)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Samenstelling brutomarge EUR{BR25} vs omzet EUR{OM25} (~{RATIO}x).
3. PnL DROP EUR{PN25} vs YE2024 winst EUR{PN24} (−75,09%) — reconciliatie met omzet JUMP +9% en FTE JUMP naar {FTE25}.
4. ESF / VDAB / gemeente / andere publieke subsidie-matrix achter omzet EUR{OM25}.
5. Per-VE cost allocation (13 VE) + effect Pro Natura-absorpties 0463.036.032 / 0466.462.409.

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

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
    "rq_2230",
    {
        "task_id": "rq_2230",
        "title": (
            "EVERY-10 + leftover dual — Kiemkracht YE2025 Medium (omzet JUMP 13.26m / "
            "bruto≫omzet ~1.41x / pnl DROP -75%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "EVERY-10 at 2230 + leftover dual after De Oever; prefer AGB/FARO/AIESH/REW else unused"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T21:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK} EVERY-10; Kiemkracht 0454.343.743 YE2025 Medium CW; omzet JUMP {OM25} "
            f"bruto {BR25} (~{RATIO}x) pnl DROP {PN25} (-75%) equity JUMP {EQ25} FTE JUMP "
            f"{FTE25}; 13 VE Hamme; progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW "
            "YE2024; Heropbeuring CW opaque; next rq_2231; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2231",
    {
        "task_id": "rq_2231",
        "title": (
            "leftover dual hole-fill after Kiemkracht — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Kiemkracht Hamme YE2025 Medium (omzet JUMP 13.26m / "
            "bruto≫omzet ~1.41x / pnl DROP -75%). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if "
            "NBB/CW euros live, else unused maatwerk/kringloop/WZC/IGS/HVZ. Do NOT redo "
            "Kiemkracht, De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, "
            "Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, "
            "Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, "
            "Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, "
            "Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, "
            "Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
            "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, "
            "A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, "
            "Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, "
            "MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, "
            "Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), "
            "Aralea (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
            "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, "
            "Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2230 EVERY-10 + Kiemkracht; FARO/AIESH/REW YE2024; AGB Bornem "
            "JR2024; Heropbeuring CW opaque"
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
    "last_unit_id": "rq_2230",
    "ticks_completed": "2230",
    "paused": "no",
    "notes": (
        f"tick2230 EVERY-10 + leftover Kiemkracht 0454.343.743 Medium (omzet JUMP {OM25}; "
        f"bruto JUMP {BR25} ~{RATIO}x; pnl DROP {PN25} -75.09%; equity JUMP {EQ25}; FTE JUMP "
        f"{FTE25}; 13 VE Hamme); progress+top10 refreshed; after De Oever@2229; AGB Bornem "
        "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; next rq_2231; next every-10 "
        "2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

# inventory for progress file
counts = {}
for name in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        counts[name] = sum(1 for _ in f) - 1

foi_status: dict[str, int] = {}
with (DATA / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        st = (row.get("status") or "").strip() or "?"
        foi_status[st] = foi_status.get(st, 0) + 1

(DATA / "progress_every_10_ticks.md").write_text(
    f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2230** (2026-08-26)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2221-2230 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2221-2230 is residual dual L5 (not near-complete of 348bn):** **Manus Antwerpen** · **Manus groep** · **Kringwinkel ZOV** · **Manus BXL** · **Kringwinkel Maasland** · **Kringwinkel West** · **Den Azalee** · **Reset** · **ViTeS** · **Midwest** · **ViTeS BE** · **De Oever** bruto **10.22m** / pnl DROP **-97%** · **Kiemkracht** omzet **13.26m** / bruto≫omzet **~1.41x** / pnl DROP **-75%** (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~{foi_status.get('ready', 0)}** drafts ready | Human send only; answered **~{foi_status.get('answered', 0)}**; partial **~{foi_status.get('partial', 0)}**; total FOI rows **~{counts['foi_queue.csv']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2221-2230** Manus stack · Kringwinkel ZOV/Maasland/West/Midwest · Den Azalee · Reset · ViTeS · ViTeS BE · De Oever · **Kiemkracht** · prior 2211-2220 stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2230)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets.csv']}+ |
| commitments.csv | {counts['commitments.csv']}+ |
| leaderboard.csv | {counts['leaderboard.csv']}+ |
| entities.csv | {counts['entities.csv']}+ |
| sources.csv | {counts['sources.csv']}+ |
| FOI ready | ~{foi_status.get('ready', 0)} |
| FOI answered | {foi_status.get('answered', 0)} |
| FOI partial | {foi_status.get('partial', 0)} |
| FOI total rows | ~{counts['foi_queue.csv']} |
| research_queue open | rq_2231 after progress |

### What improved since tick 2220

- **Residual dual (tick2221-2230):** **Manus Antwerpen** (Strong NBB) · **Manus groep** · **Kringwinkel ZOV** · **Manus BXL** (Strong NBB / pnl DROP **-94%**) · **Kringwinkel Maasland** · **Kringwinkel West** · **Den Azalee** omzet **4.66m** / pnl DROP **-52%** · **Reset** omzet **6.05m** / pnl DROP **-85%** · **ViTeS** omzet **14.04m** / FTE **529.8** · **Midwest** LOSS FLIP · **ViTeS BE** PROFIT FLIP · **De Oever** bruto **10.22m** / empty omzet / pnl DROP **-97%** · **Kiemkracht** (EVERY-10 primary — omzet JUMP **13.26m** **+9%**; bruto≫omzet **~1.41x**; pnl DROP **-75%**; equity JUMP; FTE JUMP **404.4**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024; narrative JV2025 only) · AIESH / REW YE2024-only · Heropbeuring CW kern opaque · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
""",
    encoding="utf-8",
)

(DATA / "doge_waste_top10_current.md").write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2230** (2026-08-26) · **{counts['leaderboard.csv']}+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2221-2230:** **ViTeS omzet 14.04m / FTE 529.8** · **Kiemkracht omzet 13.26m / pnl DROP -75%** (EVERY-10@2230 primary) · **De Oever bruto 10.22m / pnl DROP -97%** · **Reset pnl DROP -85%** · **Manus BXL pnl DROP -94%** · prior 2211-2220 OptimaT/Odas/Deltagroep/NBSW stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2220:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2221-2230 (off pure top10 / dual):** Manus Antwerpen · Manus groep · Kringwinkel ZOV · Manus BXL · Kringwinkel Maasland · Kringwinkel West · Den Azalee · Reset · ViTeS · Midwest · ViTeS BE · De Oever · **Kiemkracht omzet JUMP 13.26m / bruto≫omzet ~1.41x / pnl DROP -75% / FTE JUMP 404.4** (EVERY-10@2230 primary). Count NEW since 2220: ~13 residual dual fills. **Prior 2211-2220 + 2201-2210 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **Kiemkracht** EVERY-10 primary omzet JUMP **EUR13.26m (+9%)** / bruto≫omzet **~1.41x** / pnl DROP **-75%** / FTE JUMP **404.4** — Hamme maatwerk+Kringwinkel subsidy opacity.
- **De Oever** bruto **EUR10.22m** / empty omzet / pnl DROP **-97%** / FTE **126.9**.
- **ViTeS Leuven** omzet **EUR14.04m** / bruto **~1.71x** / pnl DROP **-30%** / FTE **529.8**.
- **Reset Genk** omzet **EUR6.05m** / bruto **~1.47x** / pnl DROP **-85%**.
- **Manus BXL** bruto **EUR2.37m** / empty omzet / pnl DROP **-94%**.
- **Kringwinkel Midwest** omzet **EUR3.26m** / pnl LOSS FLIP **-175k**.
- **OptimaT** bruto **~3.54×** omzet / equity JUMP **EUR39.4m** (prior retained).
- **Entiris** omzet **EUR18.93m** / equity JUMP **EUR92.3m** (prior retained).
- **ACG** omzet DROP **EUR7.49m** / bruto **~1.89×** / pnl JUMP **+69%** (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
""",
    encoding="utf-8",
)

log_block = f"""

## Tick 2230 - 2026-08-26T22:20:00Z - rq_2230 EVERY-10 + Kiemkracht Hamme (omzet JUMP 13.26m / bruto≫omzet ~1.41x / pnl DROP -75% / Medium)

- Unit: **rq_2230** EVERY-10 FIRST + leftover dual after **rq_2229 De Oever**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (narrative JV2025 only); AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE leftover **Kiemkracht VZW** YE2025 (KBO **0454.343.743**; Zwaarveld 57 Hamme; **Actief** **13 VE**; RSZ/BTW NACE **88.993**) — DISTINCT De Kemphaan Hamme. Do not redo De Oever/ViTeS BE/Midwest/ViTeS/Reset/Manus stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +9.00% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +8.56% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** DROP -75.09% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +3.56%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **16.06.2026**. Strong KBO Actief 13 VE; Pro Natura absorb 01.01.2023. Assets/debt Unknown. Medium. FOI via info@kiemkracht.org.
- EVERY-10: refreshed `progress_every_10_ticks.md` + `doge_waste_top10_current.md` (A–E; pure top10 stable; NEW residual 2221-2230 + Kiemkracht primary). Next every-10 **2240**.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.50); entities (+1 vzw_kiemkracht_hamme); foi + draft {GAP}; rq_2230=done + rq_2231 open; loop_state ticks=2230; raw docs/doge/raw/tick2230/.
- FOI: **ready not sent** (human-gated).
- Next: rq_2231 (AGB/FARO-if-YE2025 / AIESH-REW / Heropbeuring-or-unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2230 EVERY-10 + Kiemkracht omzet={OM25} bruto={BR25} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25} ratio={RATIO}"
)
