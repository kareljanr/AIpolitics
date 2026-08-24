# tick2224 — Den Azalee YE2025 Medium CW leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_den_azalee_sint_niklaas"
TICK = "2224"
UTC = "2026-08-26T20:10:00Z"
GAP = "gap_den_azalee_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_52pct_equity_jump_matrix_l5"
COMM = "comm_den_azalee_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop_52pct_equity_jump"
LB = "lb_den_azalee_omzet_4_66m_bruto_gt_omzet_1_85x_pnl_drop_52pct_equity_jump_jr2025"

OM25, OM24 = 4655785, 4525519
BR25, BR24 = 8596346, 8625512
PN25, PN24 = 340447, 711844
EQ25, EQ24 = 15538237, 15165370
FTE25, FTE24 = 188.2, 184.6


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
        "src_den_azalee_jr2025_cw_nl",
        "Companyweb NL Den Azalee YE2025 statutory",
        "https://www.companyweb.be/nl/0456719748/den-azalee",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+2.88%) bruto {BR25} (−0.34% ~1.85x) "
            f"pnl DROP {PN25} (−52.17%) equity JUMP {EQ25} (+2.46%) FTE {FTE25}; filed 04-07-2026"
        ),
    ),
    (
        "src_den_azalee_jr2025_cw_en",
        "Companyweb EN Den Azalee YE2025 statutory",
        "https://www.companyweb.be/en/0456719748/den-azalee",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 04-07-2026; Turnover {OM25}; "
            f"Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}"
        ),
    ),
    (
        "src_den_azalee_jr2025_cw_fr",
        "Companyweb FR Den Azalee YE2025 statutory",
        "https://www.companyweb.be/fr/0456719748/den-azalee",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OM25}; "
            f"Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}; Effectifs {FTE25}"
        ),
    ),
    (
        "src_den_azalee_kbo_2224",
        "KBO Den Azalee 0456.719.748 Actief VZW Sint-Niklaas 10 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0456719748",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2224; Actief VZW sinds 18.04.1995; zetel Nobels-Peelmanstraat 17 9100 "
            "Sint-Niklaas sinds 21.10.2025; 10 VE; RSZ/BTW NACE 88.993; Mo-Clean absorbed 01.01.2026"
        ),
    ),
    (
        "src_den_azalee_site_contact_2224",
        "Den Azalee FOI channel info@vzwdenazalee.be",
        "https://denazalee.be/",
        "Den Azalee VZW",
        "foi_contact",
        "tick2224; info@vzwdenazalee.be; Heistraat 115 / Nobels-Peelmanstraat 17 9100 Sint-Niklaas; 03 766 70 45",
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
        "name_nl": "Den Azalee VZW (Sint-Niklaas / maatwerk / Kringwinkel Waasland)",
        "name_fr": "Den Azalee ASBL (Saint-Nicolas / travail adapté / ressourcerie)",
        "name_en": "Den Azalee sheltered workshop (Sint-Niklaas; Kringwinkel Waasland)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://denazalee.be/",
        "foi_email": "info@vzwdenazalee.be",
        "foi_postal": "Nobels-Peelmanstraat 17, 9100 Sint-Niklaas",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0456.719.748 Actief VZW "
            f"10 VE RSZ/BTW NACE 88.993; omzet JUMP {OM25} bruto≫omzet ~1.85x pnl DROP {PN25} "
            f"equity JUMP {EQ25} FTE {FTE25}; Mo-Clean absorbed 2026"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes, conf in [
    (
        "bud_den_azalee_omzet_jr2025_cw",
        "2025",
        OM25,
        "CW code70 omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +2.88% vs YE2024 {OM24}; primary envelope",
        "medium",
    ),
    (
        "bud_den_azalee_bruto_jr2025_cw",
        "2025",
        BR25,
        "CW code9900 brutomarge YE2025",
        f"tick{TICK}; Medium CW; bruto flat −0.34% vs YE2024 {BR24}; bruto≫omzet ~1.85x",
        "medium",
    ),
    (
        "bud_den_azalee_pnl_jr2025_cw",
        "2025",
        PN25,
        "CW code9904 winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP −52.17% vs YE2024 {PN24}",
        "medium",
    ),
    (
        "bud_den_azalee_equity_jr2025_cw",
        "2025",
        EQ25,
        "CW code10/15 eigen vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +2.46% vs YE2024 {EQ24}",
        "medium",
    ),
    (
        "bud_den_azalee_fte_jr2025_cw",
        "2025",
        FTE25,
        "CW FTE YE2025",
        f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}",
        "medium",
    ),
    (
        "bud_den_azalee_omzet_jr2024_cw",
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
            "source_id": "src_den_azalee_jr2025_cw_nl",
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
            "Den Azalee YE2025 leftover dual (omzet JUMP 4.66m / bruto≫omzet ~1.85x / "
            "pnl DROP −52% / equity JUMP / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Waasland / Kringwinkel / public loonkost path",
        "legal_basis": "VZW maatwerk (KBO 0456.719.748; Actief; 10 VE; NACE 88.993)",
        "decision_date": "2026-07-04",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/nl/0456719748/den-azalee",
        "stated_goal": "Sheltered employment + reuse retail Waasland",
        "cut_option": (
            "FOI NBB PDF assets/debt; explain bruto≫omzet ~1.85x subsidy matrix; pnl DROP −52% "
            "vs equity JUMP; Mo-Clean 2026 fusion perimeter"
        ),
        "source_id": "src_den_azalee_jr2025_cw_nl",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>SintNiklaas>DenAzalee>JR2025_CW_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary {OM25}; bruto {BR25} ~1.85x; pnl DROP −52.17%; "
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
            "Den Azalee omzet JUMP 4.66m / bruto≫omzet ~1.85x / pnl DROP −52% / equity JUMP (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>SintNiklaas>DenAzalee>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} (~1.85x) / pnl DROP {PN25} −52% from {PN24} / "
            f"equity JUMP {EQ25} / FTE {FTE25} / 10 VE / Mo-Clean absorb 2026"
        ),
        "confidence": "medium",
        "source_id": "src_den_azalee_jr2025_cw_nl",
        "beneficiaries": "maatwerkers Waasland / Kringwinkel / public loonkost path",
        "stated_goal": "Sheltered employment + reuse retail Waasland",
        "measured_outcome": (
            "omzet JUMP +2.88%; bruto≫omzet ~1.85x; pnl DROP −52.17%; equity JUMP +2.46%; "
            "FTE 188.2; 10 VE"
        ),
        "absurdity_score": "7.0",
        "cost_score": "5.2",
        "difficulty": "3.0",
        "priority_index": "5.85",
        "cut_proposal": (
            "FOI NBB PDF assets/debt; publish subsidy/loonkost matrix behind bruto≫omzet; "
            "explain pnl DROP −52% vs equity JUMP; Mo-Clean fusion FOI"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall AGB Bornem JR2024 / FARO YE2024 / "
            "AIESH YE2024 / Heropbeuring CW opaque; next every-10 2230"
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
            "Vlaanderen>OostVlaanderen>SintNiklaas>DenAzalee>nbb_pdf_bruto_gt_omzet_pnl_drop_52pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB/CBSO YE2025 PDF assets/debt/cash; why bruto EUR{BR25} ≫ omzet EUR{OM25} "
            f"(~1.85x) — subsidy/loonkost/GESCO/ESF/VDAB/gemeente/OVAM matrix; pnl DROP "
            f"EUR{PN25} vs YE2024 EUR{PN24} (−52.17%) recon vs equity JUMP EUR{EQ25}; "
            f"Mo-Clean absorb 01.01.2026 perimeter; per-VE allocation (10 VE)"
        ),
        "why_it_matters": (
            "Medium CW shows large Waasland maatwerk/Kringwinkel (omzet 4.66m / bruto 8.60m / "
            "188.2 FTE / 10 VE / equity 15.5m) with pnl crater −52% under public loonkost path"
        ),
        "priority": "8",
        "recipient_body": "Den Azalee VZW",
        "recipient_email": "info@vzwdenazalee.be",
        "recipient_postal": "Nobels-Peelmanstraat 17, 9100 Sint-Niklaas",
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
            "pnl DROP −52% matrix; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2224",
    {
        "task_id": "rq_2224",
        "title": (
            "leftover dual — Den Azalee YE2025 Medium (omzet JUMP 4.66m / bruto≫omzet ~1.85x / "
            "pnl DROP −52% / equity JUMP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Den Azalee after Manus BXL; preferred AGB Bornem JR2024 / "
            "FARO/AIESH YE2024 / Heropbeuring CW opaque; Medium CW YE2025; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T19:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "10 VE Sint-Niklaas; filed 04-07-2026"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2225",
    {
        "task_id": "rq_2225",
        "title": (
            "leftover dual hole-fill after Den Azalee — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Den Azalee YE2025 Medium (omzet JUMP 4.66m / bruto≫omzet ~1.85x / "
            "pnl DROP −52%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live "
            "(CW currently opaque), else unused maatwerk/kringloop/WZC/IGS (ViTeS / Reset / "
            "Midwest if YE2025 / other). Do NOT redo Den Azalee, Manus BXL, Manus VZW groep, "
            "Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, Opnieuw & Co, "
            "Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, Groep Maatwerk, "
            "OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, "
            "Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, "
            "Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, "
            "De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De "
            "Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
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
            "spawned after tick2224 Den Azalee; FARO/AIESH YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; Midwest YE2024; next every-10 2230"
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
    "last_unit_id": "rq_2224",
    "ticks_completed": "2224",
    "paused": "no",
    "notes": (
        f"tick2224 leftover Den Azalee 0456.719.748 Medium CW (omzet JUMP {OM25}; bruto {BR25} "
        f"~1.85x; pnl DROP {PN25} −52.17%; equity JUMP {EQ25}; FTE {FTE25}; 10 VE Sint-Niklaas); "
        "after Manus BXL@2223; AGB Bornem JR2024; FARO/AIESH YE2024; Heropbeuring CW opaque; "
        "next rq_2225; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2224 Den Azalee written")
