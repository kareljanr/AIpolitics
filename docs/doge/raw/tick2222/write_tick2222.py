# tick2222 — Manus VZW (group) YE2025 Medium leftover dual after Manus Antwerpen
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_manus_groep"
TICK = "2222"
UTC = "2026-08-26T19:35:00Z"
GAP = "gap_manus_groep_nbb_pdf_assets_debt_empty_omzet_pnl_jump_equity_jump_matrix_l5"
COMM = "comm_manus_groep_jr2025_statutory_maatwerk_empty_omzet_pnl_jump_equity_jump"
LB = "lb_manus_groep_bruto_3_04m_empty_omzet_pnl_jump_21pct_equity_jump_42pct_jr2025"

BR25, BR24 = 3044848, 2800796
PN25, PN24 = 600300, 495811
EQ25, EQ24 = 2039760, 1439460
FTE25 = 60.8


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
        "src_manus_groep_jr2025_cw_nl",
        "Companyweb NL Manus VZW (groep) YE2025 statutory",
        "https://www.companyweb.be/nl/0808114522/manus",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet empty; bruto JUMP {BR25} (+8.71%) pnl JUMP {PN25} (+21.07%) equity JUMP {EQ25} (+41.70%) FTE {FTE25}; filed 26-06-2026",
    ),
    (
        "src_manus_groep_jr2025_cw_en",
        "Companyweb EN Manus VZW (groep) YE2025 statutory",
        "https://www.companyweb.be/en/0808114522/manus",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror YE2025 Medium; filed 26-06-2026; Turnover unpublished; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_manus_groep_jr2025_cw_fr",
        "Companyweb FR Manus VZW (groep) YE2025 statutory",
        "https://www.companyweb.be/fr/0808114522/manus",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror YE2025 Medium; CA non publie; Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}",
    ),
    (
        "src_manus_groep_kbo_2222",
        "KBO Manus VZW 0808.114.522 Actief Antwerpen 7 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0808114522",
        "KBO FOD Economie",
        "official_register",
        "tick2222; Actief VZW sinds 02.12.2008; zetel Luchthavenlei 7A 2100 Antwerpen; 7 VE; NACE 88.999; sister dual Manus Antwerpen 0872.564.290",
    ),
    (
        "src_manus_groep_site_contact_2222",
        "Manus groep FOI channel info@manus.tv",
        "https://www.manus.tv/",
        "Manus VZW / Manus Antwerpen dual",
        "foi_contact",
        "tick2222; info@manus.tv; Luchthavenlei 7A 2100 Antwerpen; shared with Manus Antwerpen",
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
        "name_nl": "Manus VZW (groep / Antwerpen maatwerk holding-shell)",
        "name_fr": "Manus ASBL (groupe / coquille travail adapté Anvers)",
        "name_en": "Manus VZW group shell (Antwerp maatwerk; sister of Manus Antwerpen)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.manus.tv/",
        "foi_email": "info@manus.tv",
        "foi_postal": "Luchthavenlei 7A, 2100 Antwerpen",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0808.114.522 Actief 7 VE NACE "
            f"88.999 same address as Manus Antwerpen; bruto JUMP {BR25} empty omzet pnl JUMP "
            f"{PN25} equity JUMP {EQ25} FTE {FTE25}; assets/debt Unknown"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_manus_groep_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (omzet unpublished)",
        f"tick{TICK}; Medium CW; bruto JUMP +8.71% vs YE2024 {BR24}; primary envelope",
    ),
    (
        "bud_manus_groep_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +21.07% vs YE2024 {PN24}",
    ),
    (
        "bud_manus_groep_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +41.70% vs YE2024 {EQ24}",
    ),
    (
        "bud_manus_groep_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 60.8",
        f"tick{TICK}; Medium CW; FTE {FTE25}; YE2024 FTE Unknown on free CW; assets/debt Unknown",
    ),
    (
        "bud_manus_groep_bruto_jr2024_statutory_cmp",
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
            "source_id": "src_manus_groep_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":null,"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":null,"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":null}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Manus VZW groep YE2025 leftover dual (bruto JUMP 3.04m / empty omzet / "
            "pnl JUMP +21% / equity JUMP +42% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Antwerpen / Manus Antwerpen sister dual / public loonkost path",
        "legal_basis": "VZW maatwerk (KBO 0808.114.522; Actief; 7 VE; NACE 88.999)",
        "decision_date": "2026-06-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0808114522/manus",
        "stated_goal": "Sheltered employment group shell Antwerpen",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose empty omzet vs bruto 3.04m + related-party "
            "vs Manus Antwerpen 0872.564.290; reconcile equity JUMP +42% vs sister pnl DROP"
        ),
        "source_id": "src_manus_groep_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Antwerpen>Deurne>ManusGroep>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary (omzet empty); pnl JUMP +21.07%; equity JUMP "
            f"+41.70%; FTE {FTE25}; same address as Manus Antwerpen Strong@2221; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
            "Manus groep bruto JUMP 3.04m / empty omzet / pnl JUMP +21% / equity JUMP +42% (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Antwerpen>Deurne>ManusGroep>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto JUMP envelope {BR25} (omzet unpublished) / pnl JUMP {PN25} +21% / equity "
            f"JUMP {EQ25} +42% / FTE {FTE25} / sister Manus Antwerpen omzet 7.66m Strong"
        ),
        "confidence": "medium",
        "source_id": "src_manus_groep_jr2025_cw_en",
        "beneficiaries": "maatwerkers Antwerpen / Manus Antwerpen dual / public loonkost path",
        "stated_goal": "Sheltered employment group shell",
        "measured_outcome": (
            "bruto JUMP +8.71%; omzet unpublished; pnl JUMP +21.07%; equity JUMP +41.70%; "
            f"FTE {FTE25}; 7 VE"
        ),
        "absurdity_score": "7.6",
        "cost_score": "4.6",
        "difficulty": "3.0",
        "priority_index": "6.90",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose empty omzet vs bruto 3.04m; map "
            "related-party vs Manus Antwerpen; reconcile equity JUMP +42% vs sister pnl DROP -13%"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; "
            "next every-10 2230"
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
            "Vlaanderen>Antwerpen>Deurne>ManusGroep>NBB_PDF_assets_debt_empty_omzet_pnl_jump_equity_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); why omzet unpublished "
            f"while bruto EUR{BR25} published; pnl JUMP EUR{PN25} (+21.07%); equity JUMP "
            f"EUR{EQ25} (+41.70%); related-party matrix vs Manus Antwerpen 0872.564.290"
        ),
        "why_it_matters": (
            f"Medium CW shows Manus group shell (bruto 3.04m / {FTE25} FTE / 7 VE) same address as "
            "Manus Antwerpen Strong (omzet 7.66m / pnl DROP -13%) — empty omzet + equity JUMP +42% "
            "dual opacity under public loonkost path"
        ),
        "priority": "8",
        "recipient_body": "Manus VZW",
        "recipient_email": "info@manus.tv",
        "recipient_postal": "Luchthavenlei 7A, 2100 Antwerpen",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; sister Manus Antwerpen Strong "
            "NBB already filled tick2221; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2222",
    {
        "task_id": "rq_2222",
        "title": (
            "leftover dual — Manus VZW groep YE2025 Medium (bruto JUMP 3.04m / empty omzet / "
            "pnl JUMP +21% / equity JUMP +42%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Manus VZW groep after Manus Antwerpen; preferred AGB Bornem JR2024 "
            "/ FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T19:15:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; 7 VE same address "
            "Manus Antwerpen; Heropbeuring CW thin deferred"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2223",
    {
        "task_id": "rq_2223",
        "title": (
            "leftover dual hole-fill after Manus groep — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Manus VZW groep YE2025 Medium (bruto JUMP 3.04m / empty omzet / pnl JUMP "
            "+21% / equity JUMP +42%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
            "TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if YE2025 "
            "CW/NBB live, else unused maatwerk/WZC/IGS/DSO. Do NOT redo Manus VZW groep, Manus "
            "Antwerpen, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel "
            "Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De "
            "Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
            "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, "
            "Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De "
            "Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, "
            "Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, "
            "Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), IPFBW, Aquiris, SPGE, "
            "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, "
            "Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, "
            "BNO, SWDE, BRUGEL. Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2222 Manus groep; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; "
            "Heropbeuring filed 25-06-2026 but CW kern thin; next every-10 2230"
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
    "last_unit_id": "rq_2222",
    "ticks_completed": "2222",
    "paused": "no",
    "notes": (
        f"tick2222 leftover Manus VZW groep 0808.114.522 Medium (bruto JUMP {BR25}; omzet empty; "
        f"pnl JUMP {PN25} +21.07%; equity JUMP {EQ25} +41.70%; FTE {FTE25}; 7 VE same address "
        "Manus Antwerpen); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring deferred; next "
        "rq_2223; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2222 Manus groep written")
