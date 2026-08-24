# tick2228 — ViTeS BE YE2025 Medium leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_vites_be"
TICK = "2228"
UTC = "2026-08-26T21:35:00Z"
GAP = "gap_vites_be_nbb_pdf_assets_debt_dual_leuven_pnl_flip_matrix_l5"
COMM = "comm_vites_be_jr2025_statutory_maatwerk_omzet_jump_pnl_flip"
LB = "lb_vites_be_omzet_1_04m_pnl_flip_equity_jump_jr2025"

OM25, OM24 = 1042666, 802813
BR25, BR24 = 697994, 493248
PN25, PN24 = 109606, -92515
EQ25, EQ24 = 832052, 722446
FTE25, FTE24 = 11.8, 12.0


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
        "src_vites_be_jr2025_cw_nl",
        "Companyweb NL ViTeS BE YE2025 statutory",
        "https://www.companyweb.be/nl/0466637997/vites-be",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+29.88%) bruto JUMP {BR25} (+41.51%; "
            f"bruto/omzet ~0.67x) pnl PROFIT FLIP {PN25} vs LOSS {PN24} equity JUMP {EQ25} "
            f"(+15.17%) FTE {FTE25}; filed 03-07-2026"
        ),
    ),
    (
        "src_vites_be_jr2025_cw_en",
        "Companyweb EN ViTeS BE YE2025 statutory",
        "https://www.companyweb.be/en/0466637997/vites-be",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}"
        ),
    ),
    (
        "src_vites_be_jr2025_cw_fr",
        "Companyweb FR ViTeS BE YE2025 statutory",
        "https://www.companyweb.be/fr/0466637997/vites-be",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_vites_be_kbo_2228",
        "KBO ViTeS BE 0466.637.997 Actief Anderlecht 3 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0466637997",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2228; Actief VZW; zetel Bergense Steenweg 95 1070 Anderlecht (sinds 22.06.2026); "
            "3 VE; NACE 88.999 / 47.792 / 47.793; dual sister of VITeS Leuven 0431.067.802"
        ),
    ),
    (
        "src_vites_be_site_contact_2228",
        "ViTeS BE FOI channel info@vites.be (Kringwinkel Laken / KiloMet)",
        "https://www.vites.be/nl/wat-doen-we/vites-be",
        "ViTeS / ViTeS BE VZW",
        "foi_contact",
        (
            "tick2228; info@vites.be; Kringwinkel Laken De Wandstraat 122 + KiloMet Bergense "
            "Steenweg 95 Anderlecht; tel 016260921"
        ),
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
        "name_nl": "ViTeS BE VZW (Anderlecht / Kringwinkel Laken / KiloMet)",
        "name_fr": "ViTeS BE ASBL (Anderlecht / ressourcerie Laeken / KiloMet)",
        "name_en": "ViTeS BE sheltered reuse workshop (Anderlecht; sister of VITeS Leuven)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vites.be/nl/wat-doen-we/vites-be",
        "foi_email": "info@vites.be",
        "foi_postal": "Bergense Steenweg 95, 1070 Anderlecht",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0466.637.997 Actief 3 VE "
            f"NACE 88.999/47.792/47.793; omzet JUMP {OM25} bruto JUMP {BR25} (~0.67x omzet) "
            f"pnl PROFIT FLIP {PN25} equity JUMP {EQ25} FTE {FTE25}; DISTINCT from VITeS Leuven "
            "0431.067.802 (tick2226)"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_vites_be_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +29.88% vs YE2024 {OM24}",
    ),
    (
        "bud_vites_be_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +41.51% vs YE2024 {BR24}; bruto/omzet ~0.67x",
    ),
    (
        "bud_vites_be_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl PROFIT FLIP vs YE2024 LOSS {PN24}",
    ),
    (
        "bud_vites_be_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +15.17% vs YE2024 {EQ24}",
    ),
    (
        "bud_vites_be_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 11.8",
        f"tick{TICK}; Medium CW; FTE {FTE25} vs YE2024 ~{FTE24}; assets/debt Unknown",
    ),
    (
        "bud_vites_be_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_vites_be_jr2025_cw_en",
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
            "ViTeS BE YE2025 leftover dual (omzet JUMP 1.04m / pnl PROFIT FLIP +110k / "
            "equity JUMP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "maatwerkers Brussel/Vlaams-Brabant / Kringwinkel Laken / KiloMet clients / "
            "public loonkost"
        ),
        "legal_basis": (
            "VZW maatwerk (KBO 0466.637.997; Actief; 3 VE; NACE 88.999/47.792/47.793); "
            "sister of VITeS Leuven 0431.067.802"
        ),
        "decision_date": "2026-07-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0466637997/vites-be",
        "stated_goal": "Sheltered employment + reuse retail Brussels / Laken / Anderlecht",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose dual accounting vs VITeS Leuven "
            "0431.067.802; reconcile PROFIT FLIP + omzet JUMP +29.88% with public loonkost path"
        ),
        "source_id": "src_vites_be_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Brussel>Anderlecht>ViTeS_BE>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary {OM25}; bruto {BR25} ~0.67x; PROFIT FLIP; "
            f"equity JUMP; FTE {FTE25}; 3 VE; named prefer in rq_2228 after Midwest; "
            "DISTINCT from VITeS Leuven; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; De Oever deferred; not TE-additive"
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
            "ViTeS BE omzet JUMP 1.04m / pnl PROFIT FLIP +110k / equity JUMP (YE2025 dual Leuven)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Brussel>Anderlecht>ViTeS_BE>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} ~0.67x / PROFIT FLIP {PN25} from LOSS {PN24} / "
            f"equity JUMP {EQ25} / FTE {FTE25} / dual sister VITeS Leuven"
        ),
        "confidence": "medium",
        "source_id": "src_vites_be_jr2025_cw_en",
        "beneficiaries": "maatwerkers Brussel / Kringwinkel Laken / KiloMet / public loonkost",
        "stated_goal": "Sheltered employment + reuse retail Brussels",
        "measured_outcome": (
            "omzet JUMP +29.88%; bruto JUMP +41.51% (~0.67x omzet); pnl PROFIT FLIP +110k from "
            f"LOSS; equity JUMP +15.17%; FTE {FTE25}; 3 VE; dual vs Leuven 14.04m omzet"
        ),
        "absurdity_score": "6.4",
        "cost_score": "3.6",
        "difficulty": "3.0",
        "priority_index": "5.80",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose dual split vs VITeS Leuven "
            "0431.067.802; reconcile PROFIT FLIP with public loonkost / gemeente / Actiris path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; De Oever deferred; next every-10 2230"
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
            "Brussel>Anderlecht>ViTeS_BE>NBB_PDF_assets_debt_dual_leuven_pnl_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); dual accounting vs "
            f"VITeS Leuven 0431.067.802; pnl PROFIT FLIP EUR{PN25} vs YE2024 LOSS EUR{PN24}; "
            f"omzet JUMP EUR{OM25} (+29.88%) subsidy/loonkost/Actiris/gemeente matrix; "
            f"per-VE (3 VE Laken/Anderlecht/…) allocation"
        ),
        "why_it_matters": (
            f"Medium CW shows Brussels sister maatwerk/Kringwinkel VZW (omzet 1.04m / bruto "
            f"0.70m / {FTE25} FTE / 3 VE) with PROFIT FLIP after YE2024 LOSS, while sister "
            "VITeS Leuven (tick2226) is 14.04m omzet / 529.8 FTE — dual opacity under public "
            "loonkost path; assets/debt Unknown"
        ),
        "priority": "8",
        "recipient_body": "ViTeS BE VZW",
        "recipient_email": "info@vites.be",
        "recipient_postal": "Bergense Steenweg 95, 1070 Anderlecht",
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
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; named prefer in rq_2228; "
            "DISTINCT from VITeS Leuven; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2228",
    {
        "task_id": "rq_2228",
        "title": (
            "leftover dual — ViTeS BE YE2025 Medium (omzet JUMP 1.04m / pnl PROFIT FLIP / "
            "equity JUMP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover ViTeS BE after Midwest; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW YE2025 + Strong KBO; "
            "FOI ready not sent; De Oever deferred"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T21:15:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "3 VE Anderlecht; DISTINCT VITeS Leuven"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2229",
    {
        "task_id": "rq_2229",
        "title": (
            "leftover dual hole-fill after ViTeS BE — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-DeOever-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after ViTeS BE YE2025 Medium (omzet JUMP 1.04m / pnl PROFIT FLIP). Prefer "
            "leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW "
            "if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live, else De Oever "
            "0413.895.634 YE2025 (bruto JUMP 10.22m / empty omzet / pnl DROP) / other unused "
            "maatwerk-kringloop-WZC. Do NOT redo ViTeS BE, Kringwinkel Midwest, ViTeS Leuven, "
            "Reset, Den Azalee, Kringwinkel West, Manus BXL, Manus VZW groep, Manus Antwerpen, "
            "Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, "
            "Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, "
            "Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, "
            "Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De "
            "Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, "
            "Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, "
            "Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, "
            "Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter "
            "(YE2024), Aralea (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, "
            "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
            "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
            "Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2228 ViTeS BE; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; De Oever YE2025 FREE; next every-10 2230"
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
    "last_unit_id": "rq_2228",
    "ticks_completed": "2228",
    "paused": "no",
    "notes": (
        f"tick2228 leftover ViTeS BE 0466.637.997 Medium (omzet JUMP {OM25}; bruto JUMP "
        f"{BR25} ~0.67x; pnl PROFIT FLIP {PN25}; equity JUMP {EQ25}; FTE {FTE25}; 3 VE "
        "Anderlecht); after Midwest@2227; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; De Oever deferred; next rq_2229; next every-10 2230; "
        "continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2228 ViTeS BE written")
