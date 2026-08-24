# tick2229 — De Oever Hasselt YE2025 Medium leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_de_oever_hasselt"
TICK = "2229"
UTC = "2026-08-26T21:55:00Z"
GAP = "gap_de_oever_nbb_pdf_assets_debt_empty_omzet_pnl_drop_97pct_matrix_l5"
COMM = "comm_de_oever_jr2025_statutory_jeugdhulp_empty_omzet_pnl_drop"
LB = "lb_de_oever_bruto_10_22m_empty_omzet_pnl_drop_97pct_jr2025"

BR25, BR24 = 10224653, 9935070
PN25, PN24 = 22395, 712453
EQ25, EQ24 = 7314516, 7295591
FTE25, FTE24 = 126.9, 124.3


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
        "src_de_oever_jr2025_cw_nl",
        "Companyweb NL De Oever YE2025 statutory",
        "https://www.companyweb.be/nl/0413895634/de-oever",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet empty; bruto JUMP {BR25} (+2.91%) pnl DROP {PN25} (-96.86%) equity JUMP {EQ25} FTE JUMP {FTE25}; filed 27-06-2026",
    ),
    (
        "src_de_oever_jr2025_cw_en",
        "Companyweb EN De Oever YE2025 statutory",
        "https://www.companyweb.be/en/0413895634/de-oever",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover unpublished; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_de_oever_jr2025_cw_fr",
        "Companyweb FR De Oever YE2025 statutory",
        "https://www.companyweb.be/fr/0413895634/de-oever",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA non publie; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_de_oever_kbo_2229",
        "KBO De Oever 0413.895.634 Actief Hasselt 9 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0413895634",
        "KBO FOD Economie",
        "official_register",
        "tick2229; Actief VZW sinds 28.12.1973; zetel Smetstraat 19 3501 Hasselt; 9 VE; NACE 87.991/87.901 integrale jeugdhulp met huisvesting",
    ),
    (
        "src_de_oever_site_contact_2229",
        "De Oever FOI channel directie@deoever.be / welkom@deoever.be",
        "https://www.deoever.be/",
        "De Oever VZW",
        "foi_contact",
        "tick2229; directie@deoever.be; welkom@deoever.be; Smetstraat 19 3501 Hasselt",
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
        "name_nl": "De Oever VZW (Hasselt / integrale jeugdhulp met huisvesting)",
        "name_fr": "De Oever ASBL (Hasselt / aide à la jeunesse avec hébergement)",
        "name_en": "De Oever youth care with housing (Hasselt; VL jeugdhulp dual)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.deoever.be/",
        "foi_email": "directie@deoever.be",
        "foi_postal": "Smetstraat 19, 3501 Hasselt",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0413.895.634 Actief 9 VE "
            f"NACE 87.991/87.901; bruto JUMP {BR25} empty omzet pnl DROP {PN25} (-96.86%) "
            f"FTE JUMP {FTE25}; VL jeugdhulp public euros"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_de_oever_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (omzet unpublished)",
        f"tick{TICK}; Medium CW; bruto JUMP +2.91% vs YE2024 {BR24}; primary envelope",
    ),
    (
        "bud_de_oever_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -96.86% vs YE2024 {PN24}",
    ),
    (
        "bud_de_oever_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +0.26% vs YE2024 {EQ24}",
    ),
    (
        "bud_de_oever_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 126.9",
        f"tick{TICK}; Medium CW; FTE JUMP +2.09% vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_de_oever_bruto_jr2024_statutory_cmp",
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
            "source_id": "src_de_oever_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":null,"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":null,"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "De Oever Hasselt YE2025 leftover dual (bruto JUMP 10.22m / empty omzet / "
            "pnl DROP -97% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "jeugdhulp clients Limburg / VL Agentschap Opgroeien path / public care euros",
        "legal_basis": "VZW jeugdhulp (KBO 0413.895.634; Actief; 9 VE; NACE 87.991/87.901)",
        "decision_date": "2026-06-27",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0413895634/de-oever",
        "stated_goal": "Integral youth care with housing Limburg",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 10.22m "
            "Opgroeien/VAPH/gemeente/federale matrix; pnl DROP -97% path"
        ),
        "source_id": "src_de_oever_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>Hasselt>DeOever>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary (omzet empty); pnl DROP -96.86%; FTE JUMP "
            f"{FTE25}; 9 VE; named prefer in rq_2229; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; next every-10 2230; not TE-additive of 348bn"
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
            "De Oever bruto JUMP 10.22m / empty omzet / pnl DROP -97% (YE2025)"
        ),
        "level": "L5",
        "type": "jeugdhulp_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Limburg>Hasselt>DeOever>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto JUMP envelope {BR25} (omzet unpublished) / pnl DROP {PN25} -97% from "
            f"{PN24} / equity {EQ25} / FTE JUMP {FTE25} / VL jeugdhuisvesting"
        ),
        "confidence": "medium",
        "source_id": "src_de_oever_jr2025_cw_en",
        "beneficiaries": "jeugdhulp clients / Opgroeien path / public care euros",
        "stated_goal": "Integral youth care with housing",
        "measured_outcome": (
            "bruto JUMP +2.91%; omzet unpublished; pnl DROP -96.86%; FTE JUMP +2.09%; 9 VE"
        ),
        "absurdity_score": "8.0",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "7.20",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 10.22m "
            "Opgroeien/VAPH/gemeente matrix; pnl DROP -97% despite FTE JUMP"
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
            "Vlaanderen>Limburg>Hasselt>DeOever>NBB_PDF_assets_debt_empty_omzet_pnl_drop_97pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished "
            f"while bruto EUR{BR25} published; pnl DROP EUR{PN25} vs YE2024 EUR{PN24} (-96.86%); "
            f"Opgroeien/VAPH/gemeente subsidy matrix"
        ),
        "why_it_matters": (
            f"Medium CW shows Hasselt jeugdhulp VZW (bruto 10.22m / {FTE25} FTE / 9 VE) with "
            "empty omzet and pnl crater -97% under VL Opgroeien public care path — assets/debt "
            "still Unknown"
        ),
        "priority": "8",
        "recipient_body": "De Oever VZW",
        "recipient_email": "directie@deoever.be",
        "recipient_postal": "Smetstraat 19, 3501 Hasselt",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; named prefer in rq_2229; "
            "next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2229",
    {
        "task_id": "rq_2229",
        "title": (
            "leftover dual — De Oever YE2025 Medium (bruto JUMP 10.22m / empty omzet / "
            "pnl DROP -97%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover De Oever after ViTeS BE; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T21:35:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; 9 VE Hasselt; "
            "next EVERY-10 at 2230"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2230",
    {
        "task_id": "rq_2230",
        "title": (
            "EVERY-10 + leftover dual hole-fill after De Oever — prefer AGB/FARO-YE2025/"
            "AIESH-REW/Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "EVERY-10 at 2230 FIRST: refresh progress_every_10_ticks.md + doge_waste_top10_current.md "
            "from on-disk CSVs; note A–E coverage brief in log. THEN leftover dual after De Oever "
            "Hasselt YE2025 Medium (bruto JUMP 10.22m / empty omzet / pnl DROP -97%). Prefer leftover "
            "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
            "Heropbeuring if NBB/CW euros live, else unused maatwerk/kringloop/WZC/IGS. Do NOT redo "
            "De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel West, "
            "Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, "
            "NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, "
            "Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, "
            "Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, "
            "Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, "
            "BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, "
            "De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
            "InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, "
            "Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, "
            "De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), IPFBW, Aquiris, SPGE, "
            "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, "
            "Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, "
            "BNO, SWDE, BRUGEL. Next EVERY-10 after this: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2229 De Oever; EVERY-10 mandatory at 2230; FARO/AIESH/REW YE2024; "
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
    "last_unit_id": "rq_2229",
    "ticks_completed": "2229",
    "paused": "no",
    "notes": (
        f"tick2229 leftover De Oever 0413.895.634 Medium (bruto JUMP {BR25}; omzet empty; "
        f"pnl DROP {PN25} -96.86%; equity JUMP {EQ25}; FTE JUMP {FTE25}; 9 VE Hasselt); after "
        "ViTeS BE@2228; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
        "next rq_2230 EVERY-10; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2229 De Oever written")
