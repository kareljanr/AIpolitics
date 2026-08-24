# tick2221 — Manus Antwerpen YE2025 Strong NBB leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_manus_antwerpen"
TICK = "2221"
UTC = "2026-08-26T19:15:00Z"
GAP = "gap_manus_antwerpen_subsidy_loonkost_gemeente_contract_matrix_l5"
COMM = "comm_manus_jr2025_nbb_maatwerk_omzet_jump_pnl_drop_subsidy_4_75m"
LB = "lb_manus_omzet_7_66m_pnl_drop_13pct_subsidy_4_75m_fte_jump_jr2025"

OM25, OM24 = 7656812, 7548524
BR25, BR24 = 9758854, 9353789
PN25, PN24 = 890156, 1024362
EQ25, EQ24 = 6558491, 5668335
AS25, AS24 = 8481817, 7639439
DE25, DE24 = 1871099, 1971104
SUB25, SUB24 = 4750724, 4639584
FTE25, FTE24 = 208.8, 202.0
OPBR25 = 12501108


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
        "src_manus_jr2025_nbb",
        "NBB/CBSO Manus Antwerpen YE2025 VOL-VZW 2026-00203915",
        "http://cdn.staatsbladmonitor.be/2026pdf/2026-00203915.pdf",
        "NBB CBSO via staatsbladmonitor CDN",
        "primary_official",
        f"tick{TICK}; Strong; omzet {OM25} bruto CW {BR25} pnl {PN25} equity {EQ25} assets {AS25} debt {DE25} code73 {SUB25} FTE {FTE25}; AV 23-06-2026; filed 26-06-2026",
    ),
    (
        "src_manus_jr2025_cw_nl",
        "Companyweb NL Manus Antwerpen YE2025 statutory",
        "https://www.companyweb.be/nl/0872564290/manus-antwerpen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet JUMP {OM25} bruto JUMP {BR25} pnl DROP {PN25} equity JUMP {EQ25} FTE {FTE25}; filed 26-06-2026",
    ),
    (
        "src_manus_jr2025_cw_en",
        "Companyweb EN Manus Antwerpen YE2025 statutory",
        "https://www.companyweb.be/en/0872564290/manus-antwerpen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_manus_jr2025_cw_fr",
        "Companyweb FR Manus Antwerpen YE2025 statutory",
        "https://www.companyweb.be/fr/0872564290/manus-antwerpen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}",
    ),
    (
        "src_manus_kbo_2221",
        "KBO Manus Antwerpen 0872.564.290 Actief VZW Deurne 7 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0872564290",
        "KBO FOD Economie",
        "official_register",
        "tick2221; Actief VZW; zetel Luchthavenlei 7A 2100 Deurne; 7 VE; RSZ/BTW NACE 88.999",
    ),
    (
        "src_manus_site_contact_2221",
        "Manus Antwerpen FOI channel info@manus.tv",
        "https://www.manus.tv/",
        "Manus Antwerpen VZW",
        "foi_contact",
        "tick2221; info@manus.tv; Luchthavenlei 7A 2100 Deurne; from NBB identification",
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
        "name_nl": "Manus Antwerpen VZW (Deurne / maatwerk-groen)",
        "name_fr": "Manus Anvers ASBL (Deurne / entreprise de travail adapté)",
        "name_en": "Manus Antwerp sheltered workshop (Deurne; maatwerk/green maintenance)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.manus.tv/",
        "foi_email": "info@manus.tv",
        "foi_postal": "Luchthavenlei 7A, 2100 Deurne (Antwerpen)",
        "notes": (
            f"tick{TICK} YE2025 Strong NBB PDF 2026-00203915 + CW NL+EN+FR + Strong KBO "
            f"0872.564.290 Actief 7 VE NACE 88.999; omzet JUMP {OM25} code73 subsidies {SUB25} "
            f"pnl DROP {PN25} equity JUMP {EQ25} FTE JUMP {FTE25}; Stad Antwerpen groen dual"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_manus_omzet_jr2025_nbb",
        "2025",
        OM25,
        "NBB code70 omzet YE2025",
        f"tick{TICK}; Strong NBB; omzet JUMP +1.43% vs YE2024 {OM24}",
    ),
    (
        "bud_manus_bruto_jr2025_cw",
        "2025",
        BR25,
        "CW bruto_marge YE2025 (NBB-derived)",
        f"tick{TICK}; Medium CW bruto; JUMP +4.33% vs YE2024 {BR24}; ~1.27x omzet",
    ),
    (
        "bud_manus_subsidies_jr2025_nbb",
        "2025",
        SUB25,
        "NBB code73 lidgeld/schenkingen/legaten/subsidies YE2025",
        f"tick{TICK}; Strong NBB; subsidies JUMP vs YE2024 {SUB24}; ~0.62x omzet",
    ),
    (
        "bud_manus_pnl_jr2025_nbb",
        "2025",
        PN25,
        "NBB code9904 winst YE2025",
        f"tick{TICK}; Strong NBB; pnl DROP -13.10% vs YE2024 {PN24}",
    ),
    (
        "bud_manus_equity_jr2025_nbb",
        "2025",
        EQ25,
        "NBB code10/15 eigen vermogen YE2025",
        f"tick{TICK}; Strong NBB; equity JUMP +15.70% vs YE2024 {EQ24}",
    ),
    (
        "bud_manus_assets_jr2025_nbb",
        "2025",
        AS25,
        "NBB code20/58 totaal activa YE2025",
        f"tick{TICK}; Strong NBB; assets JUMP +11.03% vs YE2024 {AS24}",
    ),
    (
        "bud_manus_debt_jr2025_nbb",
        "2025",
        DE25,
        "NBB code17/49 schulden YE2025",
        f"tick{TICK}; Strong NBB; debt DROP -5.07% vs YE2024 {DE24}",
    ),
    (
        "bud_manus_fte_jr2025_nbb",
        "2025",
        FTE25,
        "NBB social balance code9087 FTE YE2025",
        f"tick{TICK}; Strong NBB; FTE JUMP +3.37% vs YE2024 {FTE24}",
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
            "source_id": "src_manus_jr2025_nbb",
            "confidence": "strong",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_opbr":{OPBR25},"2025_code73":{SUB25},'
    f'"2025_pnl":{PN25},"2025_equity":{EQ25},"2025_assets":{AS25},"2025_debt":{DE25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_pnl":{PN24},"2024_equity":{EQ24},'
    f'"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Manus Antwerpen YE2025 leftover dual (omzet JUMP 7.66m / pnl DROP -13% / "
            "code73 subsidies 4.75m / FTE JUMP / Strong)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Antwerpen / Stad Antwerpen groen contracts / public subsidy path",
        "legal_basis": "VZW maatwerk (KBO 0872.564.290; Actief; 7 VE; NACE 88.999)",
        "decision_date": "2026-06-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00203915.pdf",
        "stated_goal": "Sheltered employment + municipal green maintenance Antwerpen",
        "cut_option": (
            "FOI code73 subsidy + Stad Antwerpen raamcontract euros split; scrutinise pnl DROP "
            "despite omzet/FTE/subsidy JUMP"
        ),
        "source_id": "src_manus_jr2025_nbb",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Antwerpen>Deurne>Manus>JR2025_NBB_L5",
        "notes": (
            f"tick{TICK}; Strong NBB; omzet primary {OM25}; code73 {SUB25}; pnl DROP -13.1%; "
            f"equity JUMP +15.7%; assets {AS25}; debt {DE25}; FTE {FTE25}; 7 VE; AGB Bornem JR2024; "
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
            "Manus Antwerpen omzet JUMP 7.66m / pnl DROP -13% / subsidies 4.75m / FTE JUMP (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Antwerpen>Deurne>Manus>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"NBB omzet {OM25} / code73 subsidies {SUB25} (~0.62x) / bruto CW {BR25} ~1.27x / "
            f"pnl DROP {PN25} -13% / equity JUMP {EQ25} / FTE JUMP {FTE25} / assets {AS25}"
        ),
        "confidence": "strong",
        "source_id": "src_manus_jr2025_nbb",
        "beneficiaries": "maatwerkers Antwerpen / Stad Antwerpen groen / public subsidy path",
        "stated_goal": "Sheltered employment + municipal green maintenance",
        "measured_outcome": (
            "omzet JUMP +1.43%; code73 subsidies 4.75m; pnl DROP -13.10%; equity JUMP +15.70%; "
            f"FTE JUMP +3.37%; 7 VE"
        ),
        "absurdity_score": "7.3",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "5.18",
        "cut_proposal": (
            "FOI code73 subsidy matrix + Stad Antwerpen raamcontract euros; explain pnl DROP "
            "despite omzet/FTE/subsidy JUMP; publish related-party Manus group transfers"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Strong NBB PDF; FOI {GAP}; stall FARO/REW YE2024; AGB Bornem JR2024; "
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
            "Vlaanderen>Antwerpen>Deurne>Manus>subsidy_loonkost_gemeente_contract_matrix"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"Code73 EUR{SUB25} subsidy/lidgeld/schenking split (GESCO/ESF/VDAB/Stad Antwerpen/"
            f"other); Stad Antwerpen groen raamcontract YE2025 euros vs omzet EUR{OM25}; pnl DROP "
            f"EUR{PN25} vs YE2024 EUR{PN24} recon despite FTE JUMP; Manus group related-party matrix"
        ),
        "why_it_matters": (
            "Strong NBB shows Deurne maatwerk VZW (omzet 7.66m / subsidies 4.75m / 208.8 FTE / "
            "7 VE) with pnl DROP -13% while omzet+FTE+subsidies JUMP under municipal green dual"
        ),
        "priority": "8",
        "recipient_body": "Manus Antwerpen VZW",
        "recipient_email": "info@manus.tv",
        "recipient_postal": "Luchthavenlei 7A, 2100 Deurne (Antwerpen)",
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
            f"tick{TICK}; ready NOT sent; Strong NBB PDF already public for balans; FOI targets "
            "subsidy/contract matrix opacity; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2221",
    {
        "task_id": "rq_2221",
        "title": (
            "leftover dual — Manus Antwerpen YE2025 Strong (omzet JUMP 7.66m / pnl DROP -13% / "
            "subsidies 4.75m / FTE JUMP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Manus Antwerpen after NBSW EVERY-10; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW still YE2024; Strong NBB YE2025 PDF + CW; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T18:55:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; omzet {OM25} code73 {SUB25} pnl {PN25} equity {EQ25} FTE {FTE25}; "
            "7 VE Deurne; NBB 2026-00203915"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2222",
    {
        "task_id": "rq_2222",
        "title": (
            "leftover dual hole-fill after Manus — prefer AGB/FARO-YE2025/AIESH-REW/"
            "unused maatwerk-WZC-IGS"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Manus Antwerpen YE2025 Strong (omzet JUMP 7.66m / pnl DROP -13% / "
            "subsidies 4.75m). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
            "YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO. Do NOT redo Manus "
            "Antwerpen, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel "
            "Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De "
            "Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
            "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, "
            "Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De "
            "Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, "
            "Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, "
            "Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK "
            "CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
            "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
            "Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2221 Manus; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; "
            "next every-10 2230"
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
    "last_unit_id": "rq_2221",
    "ticks_completed": "2221",
    "paused": "no",
    "notes": (
        f"tick2221 leftover Manus Antwerpen 0872.564.290 Strong NBB (omzet JUMP {OM25}; "
        f"code73 {SUB25}; pnl DROP {PN25} -13.1%; equity JUMP {EQ25}; FTE JUMP {FTE25}; 7 VE "
        "Deurne); after EVERY-10 NBSW@2220; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next "
        "rq_2222; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2221 Manus written")
