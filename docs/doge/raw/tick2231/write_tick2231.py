# tick2231 — De Vleugels YE2025 Medium leftover dual (FREE after Kiemkracht stalls)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_de_vleugels_houthulst"
TICK = "2231"
UTC = "2026-08-26T22:45:00Z"
GAP = "gap_de_vleugels_nbb_pdf_assets_debt_bruto_gt_omzet_7_37x_vaph_matrix_l5"
COMM = "comm_de_vleugels_jr2025_statutory_disability_bruto_gt_omzet_7_37x"
LB = "lb_de_vleugels_bruto_35_11m_gt_omzet_7_37x_equity_35_35m_jr2025"

OM25, OM24 = 4766566, 4604287
BR25, BR24 = 35113710, 33883606
PN25, PN24 = 2297992, 1868258
EQ25, EQ24 = 35353015, 33083496
FTE25, FTE24 = 442.8, 434.8
RATIO = round(BR25 / OM25, 2)  # ~7.37


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
        "src_de_vleugels_jr2025_cw_nl",
        "Companyweb NL De Vleugels YE2025 statutory",
        "https://www.companyweb.be/nl/0431408290/de-vleugels",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+3.52%) bruto JUMP {BR25} (+3.63% "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+23%) equity JUMP {EQ25} (+6.86%) "
            f"FTE {FTE25}; filed 01-07-2026"
        ),
    ),
    (
        "src_de_vleugels_jr2025_cw_en",
        "Companyweb EN De Vleugels YE2025 statutory",
        "https://www.companyweb.be/en/0431408290/de-vleugels",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 01-07-2026"
        ),
    ),
    (
        "src_de_vleugels_jr2025_cw_fr",
        "Companyweb FR De Vleugels YE2025 statutory",
        "https://www.companyweb.be/fr/0431408290/de-vleugels",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_de_vleugels_kbo_2231",
        "KBO De Vleugels 0431.408.290 Actief Houthulst 7 VE aanbestedende overheid",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0431408290",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2231; Actief VZW; zetel Stokstraat 1 8650 Houthulst; 7 VE Actief; "
            "NACE RSZ/BTW 87.202 Instellingen met huisvesting voor volwassenen met een "
            "mentale handicap; Aanbestedende overheid; VAPH vergunde zorgaanbieder"
        ),
    ),
    (
        "src_de_vleugels_site_contact_2231",
        "De Vleugels FOI channel info@devleugels.be",
        "https://devleugels.be/",
        "De Vleugels VZW",
        "foi_contact",
        "tick2231; info@devleugels.be; 051 50 12 12; Stokstraat 1 8650 Houthulst/Klerken",
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
        "name_nl": "De Vleugels VZW (Houthulst / VAPH disability care)",
        "name_fr": "De Vleugels ASBL (Houthulst / soins residentiels handicap mental)",
        "name_en": "De Vleugels VZW (Houthulst; residential care mental disability / VAPH)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://devleugels.be/",
        "foi_email": "info@devleugels.be",
        "foi_postal": "Stokstraat 1, 8650 Houthulst",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0431.408.290 Actief 7 VE "
            f"NACE 87.202 aanbestedende overheid; omzet JUMP {OM25} bruto JUMP {BR25} "
            f"(~{RATIO}x) pnl JUMP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; "
            f"neerlegging 01.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; deferred FREE SDB/Travie/"
            "Rucher YE2025; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_de_vleugels_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary envelope; bruto≫omzet)",
        f"tick{TICK}; Medium CW; bruto JUMP +3.63% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_de_vleugels_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +3.52% vs YE2024 {OM24}",
    ),
    (
        "bud_de_vleugels_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +23% vs YE2024 {PN24}",
    ),
    (
        "bud_de_vleugels_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +6.86% vs YE2024 {EQ24}",
    ),
    (
        "bud_de_vleugels_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 442.8",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_de_vleugels_bruto_jr2024_statutory_cmp",
        "2024",
        BR24,
        "CW statutory bruto_marge YE2024 comparative",
        f"tick{TICK}; YE2024 bruto {BR24} comparative",
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
            "source_id": "src_de_vleugels_jr2025_cw_en",
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
            "De Vleugels YE2025 leftover dual (bruto JUMP 35.11m / bruto≫omzet ~7.37x / "
            "equity JUMP 35.35m / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "adults with mental disability West-Flanders (Houthulst/Klerken) / VAPH public path"
        ),
        "legal_basis": (
            "VZW VAPH disability care (KBO 0431.408.290; Actief; 7 VE; NACE 87.202; "
            "aanbestedende overheid)"
        ),
        "decision_date": "2026-07-01",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0431408290/de-vleugels",
        "stated_goal": "Residential care adults with mental disability (Thuis in warme zorg)",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~7.37x (35.11m vs 4.77m); "
            "reconcile VAPH PVB/RTH/MFC subsidy matrix behind bruto; equity stock 35.35m vs "
            "flow transparency; 7-VE cost allocation"
        ),
        "source_id": "src_de_vleugels_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Houthulst>DeVleugels>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"pnl JUMP; equity JUMP {EQ25}; FTE {FTE25}; 7 VE; FREE after Kiemkracht stalls "
            "(AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque); deferred "
            "SDB/Travie/Rucher YE2025; not TE-additive"
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
            "De Vleugels bruto JUMP 35.11m / bruto≫omzet ~7.37x / equity JUMP 35.35m "
            "(YE2025 VAPH)"
        ),
        "level": "L5",
        "type": "disability_vzw_statutory",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Houthulst>DeVleugels>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto JUMP {BR25} / omzet {OM25} (~{RATIO}x) / pnl JUMP {PN25} / equity "
            f"JUMP {EQ25} / FTE JUMP {FTE25} / 7 VE VAPH disability care Houthulst"
        ),
        "confidence": "medium",
        "source_id": "src_de_vleugels_jr2025_cw_en",
        "beneficiaries": "adults with mental disability / VAPH public path West-Flanders",
        "stated_goal": "Residential care adults with mental disability",
        "measured_outcome": (
            f"bruto JUMP +3.63%; bruto≫omzet ~{RATIO}x (35.11m vs 4.77m); pnl JUMP +23%; "
            f"equity JUMP +6.86% to 35.35m; FTE JUMP {FTE25}; 7 VE; filed 01.07.2026"
        ),
        "absurdity_score": "8.2",
        "cost_score": "6.0",
        "difficulty": "3.0",
        "priority_index": "6.90",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~7.37x composition "
            "(VAPH PVB/RTH/MFC vs commercial omzet); reconcile equity stock 35.35m; 7-VE cost "
            "allocation as aanbestedende overheid"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Kiemkracht@2230; deferred "
            "FREE SDB/Travie/Rucher; next every-10 2240"
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
            "Vlaanderen>WestVlaanderen>Houthulst>DeVleugels>NBB_PDF_assets_debt_bruto_gt_omzet_7_37x_vaph"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} vs "
            f"omzet EUR{OM25} (~{RATIO}x) composition; VAPH PVB/RTH/MFC / gemeente subsidy "
            f"matrix; equity stock EUR{EQ25} vs flow; 7 VE cost allocation (aanbestedende overheid)"
        ),
        "why_it_matters": (
            f"Medium CW shows West-Flanders VAPH disability VZW (bruto 35.11m / omzet only "
            f"4.77m / ~{RATIO}x / equity 35.35m / {FTE25} FTE / 7 VE) under public VAPH path; "
            "assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "De Vleugels VZW",
        "recipient_email": "info@devleugels.be",
        "recipient_postal": "Stokstraat 1, 8650 Houthulst",
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
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; deferred SDB/Travie/Rucher; "
            "next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — De Vleugels (NBB PDF / bruto≫omzet ~{RATIO}x / VAPH matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** De Vleugels VZW — KBO **0431.408.290** (Actief; Stokstraat 1, 8650 Houthulst; **7 VE**; FTE {FTE25} CW; NACE **87.202**; aanbestedende overheid)  
**recipient:** info@devleugels.be · Stokstraat 1, 8650 Houthulst  
**sources:** [CW EN](https://www.companyweb.be/en/0431408290/de-vleugels) · [CW NL](https://www.companyweb.be/nl/0431408290/de-vleugels) · [CW FR](https://www.companyweb.be/fr/0431408290/de-vleugels) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431408290) · [site](https://devleugels.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW; **7 VE**; zetel Stokstraat 1 Houthulst; NACE **87.202**; **aanbestedende overheid**; VAPH vergunde zorgaanbieder.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +3.52% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +3.63% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +23%; equity **EUR{EQ25:,}** JUMP +6.86%; FTE **{FTE25}**; filed **01.07.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. Deferred FREE: SDB / Travie / Rucher YE2025.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: De Vleugels VZW
via info@devleugels.be
Stokstraat 1, 8650 Houthulst
Betreft: Openbaarmaking jaarrekening 2025 De Vleugels (KBO 0431.408.290)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. Samenstelling brutomarge EUR{BR25} vs omzet EUR{OM25} (~{RATIO}x).
3. VAPH PVB / RTH / MFC / gemeente / andere publieke subsidie-matrix achter bruto EUR{BR25}.
4. Toelichting eigen vermogen EUR{EQ25} vs operationele flow.
5. Per-VE cost allocation (7 VE; aanbestedende overheid).

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
    "rq_2231",
    {
        "task_id": "rq_2231",
        "title": (
            "leftover dual — De Vleugels YE2025 Medium (bruto JUMP 35.11m / bruto≫omzet "
            "~7.37x / equity JUMP 35.35m)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "leftover dual after Kiemkracht; prefer AGB/FARO/AIESH/REW else unused"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T22:20:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; De Vleugels 0431.408.290 YE2025 Medium CW; bruto JUMP {BR25} "
            f"(~{RATIO}x omzet {OM25}) pnl JUMP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; "
            "7 VE Houthulst VAPH; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
            "opaque; deferred FREE SDB/Travie/Rucher; next rq_2232; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2232",
    {
        "task_id": "rq_2232",
        "title": (
            "leftover dual hole-fill after De Vleugels — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-SDB-Travie-Rucher-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after De Vleugels Houthulst YE2025 Medium (bruto JUMP 35.11m / "
            "bruto≫omzet ~7.37x / equity JUMP 35.35m). Prefer leftover AGB/APB if JR2025 PDF "
            "live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring "
            "if NBB/CW euros live, else named FREE SDB (0665.861.844 YE2025 PROFIT FLIP) / "
            "Travie (0420.015.938 YE2025 pnl DROP -89%) / Le Rucher (0860.345.458 YE2025 LOSS "
            "FLIP) / unused maatwerk/kringloop/WZC/IGS/HVZ. Do NOT redo De Vleugels, "
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
            "Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), IPFBW, "
            "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
            "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
            "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2231 De Vleugels; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; named FREE SDB/Travie/Rucher YE2025"
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
    "last_unit_id": "rq_2231",
    "ticks_completed": "2231",
    "paused": "no",
    "notes": (
        f"tick2231 leftover De Vleugels 0431.408.290 Medium (bruto JUMP {BR25} ~{RATIO}x "
        f"omzet {OM25}; pnl JUMP {PN25}; equity JUMP {EQ25}; FTE JUMP {FTE25}; 7 VE "
        "Houthulst VAPH); after Kiemkracht@2230; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; deferred SDB/Travie/Rucher; next rq_2232; next every-10 "
        "2240; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2231 - 2026-08-26T22:45:00Z - rq_2231 De Vleugels Houthulst (bruto JUMP 35.11m / bruto≫omzet ~7.37x / equity JUMP 35.35m / Medium)

- Unit: **rq_2231** leftover dual after **rq_2230 Kiemkracht**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took FREE leftover **De Vleugels VZW** YE2025 (KBO **0431.408.290**; Stokstraat 1 Houthulst; **Actief** **7 VE**; NACE **87.202**; aanbestedende overheid / VAPH). Deferred FREE **SDB** / **Travie** / **Le Rucher** YE2025. Do not redo Kiemkracht/De Oever/ViTeS stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +3.52% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +3.63% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +23% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +6.86%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **01.07.2026**. Strong KBO Actief 7 VE aanbestedende overheid. Assets/debt Unknown. Medium. FOI via info@devleugels.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.90); entities (+1 vzw_de_vleugels_houthulst); foi + draft {GAP}; rq_2231=done + rq_2232 open; loop_state ticks=2231; raw docs/doge/raw/tick2231/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2232 (AGB/FARO-if-YE2025 / AIESH-REW / SDB-Travie-Rucher-or-unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2231 De Vleugels bruto={BR25} omzet={OM25} ratio={RATIO} pnl={PN25} "
    f"equity={EQ25} FTE={FTE25}"
)
