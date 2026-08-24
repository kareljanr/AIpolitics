# tick2226 — VITeS Leuven YE2025 Medium CW leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_vites_leuven"
TICK = "2226"
UTC = "2026-08-26T20:50:00Z"
GAP = "gap_vites_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_30pct_fte_jump_matrix_l5"
COMM = "comm_vites_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop_30pct_fte_jump"
LB = "lb_vites_omzet_14_04m_bruto_gt_omzet_1_71x_pnl_drop_30pct_fte_jump_jr2025"

OM25, OM24 = 14044208, 12957216
BR25, BR24 = 24007757, 22516666
PN25, PN24 = 1067155, 1520209
EQ25, EQ24 = 31241325, 30206512
FTE25, FTE24 = 529.8, 507.4


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
        "src_vites_jr2025_cw_nl",
        "Companyweb NL VITeS YE2025 statutory",
        "https://www.companyweb.be/nl/0431067802/vites",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+8.39%) bruto {BR25} (+6.62% ~1.71x) "
            f"pnl DROP {PN25} (−29.80%) equity JUMP {EQ25} FTE {FTE25}; filed 03-07-2026"
        ),
    ),
    (
        "src_vites_jr2025_cw_en",
        "Companyweb EN VITeS YE2025 statutory",
        "https://www.companyweb.be/en/0431067802/vites",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 03-07-2026; Turnover {OM25}; "
            f"Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}"
        ),
    ),
    (
        "src_vites_jr2025_cw_fr",
        "Companyweb FR VITeS YE2025 statutory",
        "https://www.companyweb.be/fr/0431067802/vites",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OM25}; "
            f"Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}; Effectifs {FTE25}"
        ),
    ),
    (
        "src_vites_kbo_2226",
        "KBO VITeS 0431.067.802 Actief VZW Leuven 14 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0431067802",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2226; Actief VZW sinds 08.08.1985; naam VITeS sinds 20.06.2022; "
            "zetel Ijzerenmolenstraat 4 3001 Leuven sinds 18.09.2009; 14 VE; RSZ/BTW NACE 88.993"
        ),
    ),
    (
        "src_vites_site_contact_2226",
        "VITeS FOI channel info@vites.be",
        "https://www.vites.be/",
        "VITeS VZW",
        "foi_contact",
        "tick2226; info@vites.be; Ijzerenmolenstraat 4 3001 Leuven; maatwerk + Kringwinkel Leuven region",
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
        "name_nl": "VITeS VZW (Leuven / maatwerk / Kringwinkel)",
        "name_fr": "VITeS ASBL (Louvain / travail adapté / ressourcerie)",
        "name_en": "VITeS sheltered workshop (Leuven; Kringwinkel reuse)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vites.be/",
        "foi_email": "info@vites.be",
        "foi_postal": "Ijzerenmolenstraat 4, 3001 Leuven",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0431.067.802 Actief VZW "
            f"14 VE RSZ/BTW NACE 88.993; omzet JUMP {OM25} bruto≫omzet ~1.71x pnl DROP {PN25} "
            f"equity JUMP {EQ25} FTE JUMP {FTE25}"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes, conf in [
    (
        "bud_vites_omzet_jr2025_cw",
        "2025",
        OM25,
        "CW code70 omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +8.39% vs YE2024 {OM24}; primary envelope",
        "medium",
    ),
    (
        "bud_vites_bruto_jr2025_cw",
        "2025",
        BR25,
        "CW code9900 brutomarge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +6.62% vs YE2024 {BR24}; bruto≫omzet ~1.71x",
        "medium",
    ),
    (
        "bud_vites_pnl_jr2025_cw",
        "2025",
        PN25,
        "CW code9904 winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP −29.80% vs YE2024 {PN24}",
        "medium",
    ),
    (
        "bud_vites_equity_jr2025_cw",
        "2025",
        EQ25,
        "CW code10/15 eigen vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +3.43% vs YE2024 {EQ24}",
        "medium",
    ),
    (
        "bud_vites_fte_jr2025_cw",
        "2025",
        FTE25,
        "CW FTE YE2025",
        f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}",
        "medium",
    ),
    (
        "bud_vites_omzet_jr2024_cw",
        "2024",
        OM24,
        "CW code70 omzet YE2024 comparative",
        f"tick{TICK}; Medium CW YoY base",
        "medium",
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
            "source_id": "src_vites_jr2025_cw_nl",
            "confidence": conf,
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
            "VITeS YE2025 leftover dual (omzet JUMP 14.04m / bruto≫omzet ~1.71x / "
            "pnl DROP −30% / FTE JUMP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Leuven-regio / Kringwinkel / public loonkost path",
        "legal_basis": "VZW maatwerk (KBO 0431.067.802; Actief; 14 VE; NACE 88.993)",
        "decision_date": "2026-07-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/nl/0431067802/vites",
        "stated_goal": "Sheltered employment + reuse retail Leuven region",
        "cut_option": (
            "FOI NBB PDF assets/debt; explain bruto≫omzet ~1.71x subsidy matrix; pnl DROP −30% "
            "vs omzet JUMP +8%; per-VE allocation"
        ),
        "source_id": "src_vites_jr2025_cw_nl",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>VITeS>JR2025_CW_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary {OM25}; bruto {BR25} ~1.71x; pnl DROP −29.80%; "
            "assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH YE2024; Heropbeuring CW opaque; "
            "not TE-additive of 348bn"
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
            "VITeS omzet JUMP 14.04m / bruto≫omzet ~1.71x / pnl DROP −30% / FTE JUMP (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>VlaamsBrabant>Leuven>VITeS>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} (~1.71x) / pnl DROP {PN25} −30% from {PN24} / "
            f"equity JUMP {EQ25} / FTE JUMP {FTE25} / 14 VE"
        ),
        "confidence": "medium",
        "source_id": "src_vites_jr2025_cw_nl",
        "beneficiaries": "maatwerkers Leuven-regio / Kringwinkel / public loonkost path",
        "stated_goal": "Sheltered employment + reuse retail Leuven region",
        "measured_outcome": (
            "omzet JUMP +8.39%; bruto≫omzet ~1.71x; pnl DROP −29.80%; equity JUMP +3.43%; "
            "FTE 529.8 JUMP vs 507.4; 14 VE"
        ),
        "absurdity_score": "7.2",
        "cost_score": "6.5",
        "difficulty": "3.0",
        "priority_index": "6.50",
        "cut_proposal": (
            "FOI NBB PDF assets/debt; publish subsidy/loonkost matrix behind bruto≫omzet; "
            "explain pnl DROP −30% vs omzet JUMP +8%; per-VE FOI"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall AGB Bornem JR2024 / FARO YE2024 / "
            "AIESH YE2024 / Heropbeuring CW opaque; deferred Midwest YE2025 live; next every-10 2230"
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
            "Vlaanderen>VlaamsBrabant>Leuven>VITeS>nbb_pdf_bruto_gt_omzet_pnl_drop_30pct_fte_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB/CBSO YE2025 PDF assets/debt/cash; why bruto EUR{BR25} ≫ omzet EUR{OM25} "
            f"(~1.71x) — subsidy/loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix; pnl DROP "
            f"EUR{PN25} vs YE2024 EUR{PN24} (−29.80%) recon vs equity JUMP EUR{EQ25}; "
            f"FTE JUMP {FTE25} vs {FTE24}; per-VE allocation (14 VE)"
        ),
        "why_it_matters": (
            "Medium CW shows large Leuven-region maatwerk/Kringwinkel (omzet 14.04m / bruto 24.01m / "
            "529.8 FTE / 14 VE / equity 31.24m) with pnl DROP −30% under public loonkost path"
        ),
        "priority": "8",
        "recipient_body": "VITeS VZW",
        "recipient_email": "info@vites.be",
        "recipient_postal": "Ijzerenmolenstraat 4, 3001 Leuven",
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
            f"tick{TICK}; ready NOT sent; Medium CW; FOI targets NBB PDF + bruto≫omzet + "
            "pnl DROP −30% matrix; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2226",
    {
        "task_id": "rq_2226",
        "title": (
            "leftover dual — VITeS YE2025 Medium (omzet JUMP 14.04m / bruto≫omzet ~1.71x / "
            "pnl DROP −30% / FTE JUMP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover VITeS after Reset Genk; preferred AGB Bornem JR2024 / "
            "FARO/AIESH YE2024 / Heropbeuring CW opaque; took named FREE VITeS YE2025 live; "
            "deferred live Kringwinkel Midwest; Medium CW; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T20:35:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "14 VE Leuven; filed 03-07-2026"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2227",
    {
        "task_id": "rq_2227",
        "title": (
            "leftover dual hole-fill after VITeS — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after VITeS YE2025 Medium (omzet JUMP 14.04m / bruto≫omzet ~1.71x / "
            "pnl DROP −30%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live "
            "(CW currently opaque), else unused maatwerk/kringloop/WZC/IGS (Kringwinkel Midwest "
            "YE2025 live / other). Do NOT redo VITeS, Reset Genk, Den Azalee, Kringwinkel West, "
            "Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, "
            "NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, "
            "Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, "
            "Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, "
            "Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, "
            "BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, "
            "De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
            "InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, "
            "Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, "
            "De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, "
            "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
            "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, "
            "SWDE, BRUGEL. Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2226 VITeS; FARO/AIESH YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; Midwest YE2025 live deferred; next every-10 2230"
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
    "last_unit_id": "rq_2226",
    "ticks_completed": "2226",
    "paused": "no",
    "notes": (
        f"tick2226 leftover VITeS 0431.067.802 Medium CW (omzet JUMP {OM25}; bruto {BR25} "
        f"~1.71x; pnl DROP {PN25} −29.80%; equity JUMP {EQ25}; FTE JUMP {FTE25}; 14 VE Leuven); "
        "after Reset@2225; AGB Bornem JR2024; FARO/AIESH YE2024; Heropbeuring CW opaque; "
        "deferred Midwest YE2025 live; next rq_2227; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2226 VITeS written")
