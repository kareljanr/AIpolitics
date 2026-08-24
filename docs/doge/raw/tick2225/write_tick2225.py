# tick2225 — Reset Genk YE2025 Medium leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_reset_genk"
TICK = "2225"
UTC = "2026-08-26T20:35:00Z"
GAP = "gap_reset_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_85pct_matrix_l5"
COMM = "comm_reset_jr2025_statutory_maatwerk_omzet_jump_bruto_gt_omzet_pnl_drop"
LB = "lb_reset_omzet_6_05m_bruto_gt_omzet_1_47x_pnl_drop_85pct_jr2025"

OM25, OM24 = 6054875, 5450363
BR25, BR24 = 8910909, 8270329
PN25, PN24 = 19665, 134396
EQ25, EQ24 = 8275359, 8313051
FTE25 = 201.0


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
        "src_reset_jr2025_cw_nl",
        "Companyweb NL Reset YE2025 statutory",
        "https://www.companyweb.be/nl/0460015174/reset",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet JUMP {OM25} (+11.09%) bruto JUMP {BR25} (~1.47x) pnl DROP {PN25} (-85.37%) equity DROP {EQ25} FTE {FTE25}; filed 02-07-2026",
    ),
    (
        "src_reset_jr2025_cw_en",
        "Companyweb EN Reset YE2025 statutory",
        "https://www.companyweb.be/en/0460015174/reset",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_reset_jr2025_cw_fr",
        "Companyweb FR Reset YE2025 statutory",
        "https://www.companyweb.be/fr/0460015174/reset",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_reset_kbo_2225",
        "KBO Reset 0460.015.174 Actief Genk 12 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0460015174",
        "KBO FOD Economie",
        "official_register",
        "tick2225; Actief VZW sinds 21.12.1996; zetel Bosdel 36 3600 Genk; 12 VE; RSZ NACE 88.993",
    ),
    (
        "src_reset_site_contact_2225",
        "Reset FOI channel info@vzwreset.be",
        "https://www.vzwreset.be/",
        "Reset VZW",
        "foi_contact",
        "tick2225; info@vzwreset.be; Bosdel 36 3600 Genk; Limburg kringloop/maatwerk",
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
        "name_nl": "Reset VZW (Genk / maatwerk-kringloop Limburg)",
        "name_fr": "Reset ASBL (Genk / entreprise de travail adapté / réemploi Limbourg)",
        "name_en": "Reset sheltered reuse workshop (Genk; Limburg maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vzwreset.be/",
        "foi_email": "info@vzwreset.be",
        "foi_postal": "Bosdel 36, 3600 Genk",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0460.015.174 Actief 12 VE "
            f"RSZ 88.993; omzet JUMP {OM25} bruto JUMP {BR25} (~1.47x) pnl DROP {PN25} (-85%) "
            f"equity DROP {EQ25} FTE {FTE25}; assets/debt Unknown"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_reset_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +11.09% vs YE2024 {OM24}; primary published sales",
    ),
    (
        "bud_reset_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +7.75% vs YE2024 {BR24}; bruto≫omzet ~1.47x",
    ),
    (
        "bud_reset_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -85.37% vs YE2024 {PN24}",
    ),
    (
        "bud_reset_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -0.45% vs YE2024 {EQ24}",
    ),
    (
        "bud_reset_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 201",
        f"tick{TICK}; Medium CW; FTE {FTE25}; YE2024 FTE Unknown on free CW; assets/debt Unknown",
    ),
    (
        "bud_reset_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_reset_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":null}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Reset Genk YE2025 leftover dual (omzet JUMP 6.05m / bruto≫omzet ~1.47x / "
            "pnl DROP -85% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Limburg Genk / hergebruik clients / public loonkost path",
        "legal_basis": "VZW maatwerk (KBO 0460.015.174; Actief; 12 VE; RSZ NACE 88.993)",
        "decision_date": "2026-07-02",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0460015174/reset",
        "stated_goal": "Sheltered employment + reuse retail Limburg",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.47x loonkost/GESCO/ESF/"
            "VDAB/OVAM/gemeente split; pnl DROP -85% path"
        ),
        "source_id": "src_reset_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>Genk>Reset>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary {OM25}; bruto {BR25} ~1.47x; pnl DROP -85.37%; "
            f"equity DROP; FTE {FTE25}; 12 VE; named in rq_2225 ViTeS/Reset prefer; AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; not TE-additive of 348bn"
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
            "Reset Genk omzet JUMP 6.05m / bruto≫omzet ~1.47x / pnl DROP -85% (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Limburg>Genk>Reset>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} ~1.47x / pnl DROP {PN25} -85% from {PN24} / "
            f"equity DROP {EQ25} / FTE {FTE25} / 12 VE"
        ),
        "confidence": "medium",
        "source_id": "src_reset_jr2025_cw_en",
        "beneficiaries": "maatwerkers Genk / hergebruik Limburg / public loonkost path",
        "stated_goal": "Sheltered employment + reuse retail",
        "measured_outcome": (
            "omzet JUMP +11.09%; bruto≫omzet ~1.47x; pnl DROP -85.37%; equity DROP -0.45%; "
            f"FTE {FTE25}"
        ),
        "absurdity_score": "7.6",
        "cost_score": "5.0",
        "difficulty": "3.0",
        "priority_index": "6.90",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.47x "
            "loonkost/GESCO/ESF/VDAB/OVAM/gemeente split; pnl DROP -85% path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024; "
            "AGB Bornem JR2024; next every-10 2230"
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
            "Vlaanderen>Limburg>Genk>Reset>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop_85pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} ≫ "
            f"omzet EUR{OM25} (~1.47x) subsidy/loonkost matrix; pnl DROP EUR{PN25} vs YE2024 "
            f"EUR{PN24} (-85.37%); YE2024 FTE"
        ),
        "why_it_matters": (
            f"Medium CW shows Genk Limburg maatwerk/kringloop VZW (omzet 6.05m / bruto 8.91m / "
            f"{FTE25} FTE / 12 VE) with bruto≫omzet ~1.47x and pnl crater -85% under public "
            "loonkost + reuse path — assets/debt still Unknown"
        ),
        "priority": "8",
        "recipient_body": "Reset VZW",
        "recipient_email": "info@vzwreset.be",
        "recipient_postal": "Bosdel 36, 3600 Genk",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; named prefer in rq_2225; "
            "Heropbeuring CW opaque; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2225",
    {
        "task_id": "rq_2225",
        "title": (
            "leftover dual — Reset Genk YE2025 Medium (omzet JUMP 6.05m / bruto≫omzet ~1.47x / "
            "pnl DROP -85%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Reset after Den Azalee; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T20:10:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "12 VE Genk"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2226",
    {
        "task_id": "rq_2226",
        "title": (
            "leftover dual hole-fill after Reset — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Reset Genk YE2025 Medium (omzet JUMP 6.05m / bruto≫omzet ~1.47x / pnl "
            "DROP -85%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
            "else AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live (CW "
            "currently opaque), else unused maatwerk/kringloop/WZC/IGS (ViTeS / Aralea / other). "
            "Do NOT redo Reset, Den Azalee, Kringwinkel West, Manus BXL, Manus VZW groep, Manus "
            "Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, "
            "Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize "
            "Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, "
            "Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP "
            "Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, "
            "BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
            "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, "
            "Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, "
            "Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
            "NLZ, Mobiel, Vlotter (YE2024), ViTeS (if already filled), IPFBW, Aquiris, SPGE, IRE*, "
            "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
            "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, "
            "BRUGEL. Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2225 Reset; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2230"
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
    "last_unit_id": "rq_2225",
    "ticks_completed": "2225",
    "paused": "no",
    "notes": (
        f"tick2225 leftover Reset Genk 0460.015.174 Medium (omzet JUMP {OM25}; bruto JUMP "
        f"{BR25} ~1.47x; pnl DROP {PN25} -85.37%; equity DROP {EQ25}; FTE {FTE25}; 12 VE Genk); "
        "after Den Azalee@2224; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
        "next rq_2226; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2225 Reset written")
