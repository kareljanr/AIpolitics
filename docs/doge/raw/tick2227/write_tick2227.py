# tick2227 — Kringwinkel Midwest YE2025 Medium leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_kringwinkel_midwest"
TICK = "2227"
UTC = "2026-08-26T21:15:00Z"
GAP = "gap_kringwinkel_midwest_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_loss_flip_matrix_l5"
COMM = "comm_kringwinkel_midwest_jr2025_statutory_maatwerk_omzet_jump_pnl_loss_flip"
LB = "lb_kringwinkel_midwest_omzet_3_26m_bruto_gt_omzet_1_64x_pnl_loss_flip_jr2025"

OM25, OM24 = 3256446, 2894433
BR25, BR24 = 5340288, 4999384
PN25, PN24 = -174600, 126222
EQ25, EQ24 = 4249386, 4423985
FTE25, FTE24 = 133.2, 122.0


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
        "src_kw_midwest_jr2025_cw_nl",
        "Companyweb NL Kringwinkel Midwest YE2025 statutory",
        "https://www.companyweb.be/nl/0456349366/de-kringwinkel-midden-west-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet JUMP {OM25} (+12.51%) bruto JUMP {BR25} (~1.64x) pnl LOSS FLIP {PN25} equity DROP {EQ25} FTE JUMP {FTE25}; filed 15-06-2026",
    ),
    (
        "src_kw_midwest_jr2025_cw_en",
        "Companyweb EN Kringwinkel Midwest YE2025 statutory",
        "https://www.companyweb.be/en/0456349366/de-kringwinkel-midden-west-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_kw_midwest_jr2025_cw_fr",
        "Companyweb FR Kringwinkel Midwest YE2025 statutory",
        "https://www.companyweb.be/fr/0456349366/de-kringwinkel-midden-west-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_kw_midwest_kbo_2227",
        "KBO Kringwinkel Midwest 0456.349.366 Actief Roeselare 9 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0456349366",
        "KBO FOD Economie",
        "official_register",
        "tick2227; Actief VZW; zetel Noordlaan 77 8800 Roeselare (sinds 04.06.2026); 9 VE; RSZ NACE 88.993/88.999; tel 051244914",
    ),
    (
        "src_kw_midwest_site_contact_2227",
        "Kringwinkel Midwest FOI channel info@dekringwinkelmidwest.be",
        "https://www.kringwinkel.be/",
        "Kringwinkel Midwest VZW",
        "foi_contact",
        "tick2227; info@dekringwinkelmidwest.be; Noordlaan 77 8800 Roeselare",
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
        "name_nl": "Kringwinkel Midwest / Midden-West-Vlaanderen VZW (Roeselare)",
        "name_fr": "Kringwinkel Midwest ASBL (Roulers / entreprise de travail adapté)",
        "name_en": "Kringwinkel Midwest sheltered reuse workshop (Roeselare; maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.kringwinkel.be/",
        "foi_email": "info@dekringwinkelmidwest.be",
        "foi_postal": "Noordlaan 77, 8800 Roeselare",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0456.349.366 Actief 9 VE "
            f"RSZ 88.993; omzet JUMP {OM25} bruto JUMP {BR25} (~1.64x) pnl LOSS FLIP {PN25} "
            f"equity DROP {EQ25} FTE JUMP {FTE25}; NOT HVZ Midwest IGS"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_kw_midwest_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +12.51% vs YE2024 {OM24}",
    ),
    (
        "bud_kw_midwest_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +6.82% vs YE2024 {BR24}; bruto≫omzet ~1.64x",
    ),
    (
        "bud_kw_midwest_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 profit {PN24}",
    ),
    (
        "bud_kw_midwest_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -3.95% vs YE2024 {EQ24}",
    ),
    (
        "bud_kw_midwest_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 133.2",
        f"tick{TICK}; Medium CW; FTE JUMP +9.18% vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_kw_midwest_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_kw_midwest_jr2025_cw_en",
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
            "Kringwinkel Midwest YE2025 leftover dual (omzet JUMP 3.26m / bruto≫omzet ~1.64x / "
            "pnl LOSS FLIP -175k / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers West-Vlaanderen Roeselare / hergebruik clients / public loonkost",
        "legal_basis": "VZW maatwerk (KBO 0456.349.366; Actief; 9 VE; RSZ NACE 88.993/88.999)",
        "decision_date": "2026-06-15",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0456349366/de-kringwinkel-midden-west-vlaanderen",
        "stated_goal": "Sheltered employment + reuse retail Midden-West-Vlaanderen",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.64x loonkost/GESCO/ESF/"
            "VDAB/OVAM/gemeente split; LOSS FLIP path despite omzet/FTE JUMP"
        ),
        "source_id": "src_kw_midwest_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Roeselare>KringwinkelMidwest>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary {OM25}; bruto {BR25} ~1.64x; LOSS FLIP; "
            f"equity DROP; FTE JUMP {FTE25}; 9 VE; named prefer in rq_2227; NOT HVZ Midwest; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; not TE-additive"
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
            "Kringwinkel Midwest omzet JUMP 3.26m / bruto≫omzet ~1.64x / pnl LOSS FLIP (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>WestVlaanderen>Roeselare>KringwinkelMidwest>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} ~1.64x / LOSS FLIP {PN25} from profit {PN24} / "
            f"equity DROP {EQ25} / FTE JUMP {FTE25}"
        ),
        "confidence": "medium",
        "source_id": "src_kw_midwest_jr2025_cw_en",
        "beneficiaries": "maatwerkers Roeselare / hergebruik / public loonkost path",
        "stated_goal": "Sheltered employment + reuse retail",
        "measured_outcome": (
            "omzet JUMP +12.51%; bruto≫omzet ~1.64x; pnl LOSS FLIP -175k; equity DROP -3.95%; "
            f"FTE JUMP +9.18%"
        ),
        "absurdity_score": "7.8",
        "cost_score": "4.6",
        "difficulty": "3.0",
        "priority_index": "7.00",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.64x "
            "loonkost/GESCO/ESF/VDAB/OVAM/gemeente split; LOSS FLIP despite omzet/FTE JUMP"
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
            "Vlaanderen>WestVlaanderen>Roeselare>KringwinkelMidwest>NBB_PDF_assets_debt_bruto_gt_omzet_pnl_loss_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} ≫ "
            f"omzet EUR{OM25} (~1.64x) subsidy/loonkost matrix; pnl LOSS FLIP EUR{PN25} vs YE2024 "
            f"profit EUR{PN24}; equity DROP path"
        ),
        "why_it_matters": (
            f"Medium CW shows Roeselare kringwinkel/maatwerk VZW (omzet 3.26m / bruto 5.34m / "
            f"{FTE25} FTE / 9 VE) with bruto≫omzet ~1.64x and LOSS FLIP despite omzet/FTE JUMP "
            "under public loonkost + reuse path — assets/debt still Unknown"
        ),
        "priority": "8",
        "recipient_body": "Kringwinkel Midwest VZW",
        "recipient_email": "info@dekringwinkelmidwest.be",
        "recipient_postal": "Noordlaan 77, 8800 Roeselare",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; named prefer in rq_2227; "
            "NOT HVZ Midwest; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2227",
    {
        "task_id": "rq_2227",
        "title": (
            "leftover dual — Kringwinkel Midwest YE2025 Medium (omzet JUMP 3.26m / "
            "bruto≫omzet ~1.64x / pnl LOSS FLIP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Kringwinkel Midwest after ViTeS; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T20:50:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "9 VE Roeselare"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2228",
    {
        "task_id": "rq_2228",
        "title": (
            "leftover dual hole-fill after Kringwinkel Midwest — prefer AGB/FARO-YE2025/"
            "AIESH-REW/Heropbeuring-ViTeSBE-DeOever-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Kringwinkel Midwest YE2025 Medium (omzet JUMP 3.26m / bruto≫omzet ~1.64x / "
            "pnl LOSS FLIP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else "
            "ViTeS BE 0466.637.997 YE2025 / De Oever 0413.895.634 YE2025 / other unused. Do NOT "
            "redo Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel West, Manus BXL, "
            "Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, "
            "Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, "
            "Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De "
            "Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
            "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, "
            "Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De "
            "Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, "
            "Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, "
            "Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), "
            "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
            "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
            "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2227 Kringwinkel Midwest; FARO/AIESH/REW YE2024; AGB Bornem "
            "JR2024; Heropbeuring CW opaque; ViTeS BE + De Oever YE2025 FREE; next every-10 2230"
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
    "last_unit_id": "rq_2227",
    "ticks_completed": "2227",
    "paused": "no",
    "notes": (
        f"tick2227 leftover Kringwinkel Midwest 0456.349.366 Medium (omzet JUMP {OM25}; bruto "
        f"JUMP {BR25} ~1.64x; pnl LOSS FLIP {PN25}; equity DROP {EQ25}; FTE JUMP {FTE25}; 9 VE "
        "Roeselare); after ViTeS@2226; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
        "opaque; ViTeS BE/De Oever deferred; next rq_2228; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2227 Kringwinkel Midwest written")
