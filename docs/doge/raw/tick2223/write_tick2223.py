# tick2223 — Manus BXL YE2025 Strong NBB leftover dual
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_manus_bxl"
TICK = "2223"
UTC = "2026-08-26T19:55:00Z"
GAP = "gap_manus_bxl_nbb_subsidy_empty_omzet_pnl_drop_94pct_fte_jump_matrix_l5"
COMM = "comm_manus_bxl_jr2025_nbb_maatwerk_empty_omzet_pnl_drop_94pct_fte_jump"
LB = "lb_manus_bxl_bruto_2_37m_empty_omzet_pnl_drop_94pct_fte_jump_jr2025"

BR25, BR24 = 2366024, 2317563
PN25, PN24 = 10308, 168389
EQ25, EQ24 = 980133, 969825
AS25, AS24 = 2495982, 2546663
DE25, DE24 = 1515849, 1576838
FTE25, FTE24 = 59.8, 55.7
STAFF25 = 2303691


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
        "src_manus_bxl_jr2025_nbb",
        "NBB/CBSO Manus BXL YE2025 VKT-VZW 2026-00203914",
        "http://cdn.staatsbladmonitor.be/2026pdf/2026-00203914.pdf",
        "NBB CBSO via staatsbladmonitor CDN",
        "primary_official",
        f"tick{TICK}; Strong; bruto {BR25} omzet empty pnl DROP {PN25} equity {EQ25} assets {AS25} debt {DE25} FTE {FTE25}; AV 23-06-2026; filed 26-06-2026",
    ),
    (
        "src_manus_bxl_jr2025_cw_nl",
        "Companyweb NL Manus BXL YE2025 statutory",
        "https://www.companyweb.be/nl/0828752657/manus-bxl",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet empty; bruto JUMP {BR25} pnl DROP {PN25} (-93.88%) equity JUMP {EQ25} FTE JUMP {FTE25}",
    ),
    (
        "src_manus_bxl_jr2025_cw_en",
        "Companyweb EN Manus BXL YE2025 statutory",
        "https://www.companyweb.be/en/0828752657/manus-bxl",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror; Turnover unpublished; Gross margin {BR25}; Profit {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_manus_bxl_jr2025_cw_fr",
        "Companyweb FR Manus BXL YE2025 statutory",
        "https://www.companyweb.be/fr/0828752657/manus-bxl",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA non publie; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_manus_bxl_kbo_2223",
        "KBO Manus BXL 0828.752.657 Actief Sint-Agatha-Berchem 7 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0828752657",
        "KBO FOD Economie",
        "official_register",
        "tick2223; Actief VZW sinds 26.08.2010; zetel Nestor Martinstraat 313-315 1082; 7 VE; NACE 88.999; Manus dual",
    ),
    (
        "src_manus_bxl_site_contact_2223",
        "Manus BXL FOI channel info@manus.tv",
        "https://www.manus.tv/",
        "Manus BXL VZW",
        "foi_contact",
        "tick2223; info@manus.tv; Nestor Martinstraat 313-315 1082 Sint-Agatha-Berchem",
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
        "name_nl": "Manus BXL VZW (Sint-Agatha-Berchem / maatwerk)",
        "name_fr": "Manus BXL ASBL (Berchem-Sainte-Agathe / travail adapté)",
        "name_en": "Manus BXL sheltered workshop (Sint-Agatha-Berchem; Manus dual)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.manus.tv/",
        "foi_email": "info@manus.tv",
        "foi_postal": "Nestor Martinstraat 313-315, 1082 Sint-Agatha-Berchem",
        "notes": (
            f"tick{TICK} YE2025 Strong NBB 2026-00203914 + CW + Strong KBO 0828.752.657 Actief "
            f"7 VE NACE 88.999; bruto JUMP {BR25} empty omzet pnl DROP {PN25} (-93.88%) FTE JUMP "
            f"{FTE25}; sister Manus Antwerpen/groep"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_manus_bxl_bruto_jr2025_nbb",
        "2025",
        BR25,
        "NBB code9900 brutomarge YE2025 (omzet unpublished)",
        f"tick{TICK}; Strong NBB; bruto JUMP +2.09% vs YE2024 {BR24}; primary envelope",
    ),
    (
        "bud_manus_bxl_pnl_jr2025_nbb",
        "2025",
        PN25,
        "NBB code9904 winst YE2025",
        f"tick{TICK}; Strong NBB; pnl DROP -93.88% vs YE2024 {PN24}; op loss flip 9901 -6748",
    ),
    (
        "bud_manus_bxl_equity_jr2025_nbb",
        "2025",
        EQ25,
        "NBB code10/15 eigen vermogen YE2025",
        f"tick{TICK}; Strong NBB; equity JUMP +1.06% vs YE2024 {EQ24}",
    ),
    (
        "bud_manus_bxl_assets_jr2025_nbb",
        "2025",
        AS25,
        "NBB code20/58 activa YE2025",
        f"tick{TICK}; Strong NBB; assets DROP -1.99% vs YE2024 {AS24}",
    ),
    (
        "bud_manus_bxl_debt_jr2025_nbb",
        "2025",
        DE25,
        "NBB code17/49 schulden YE2025",
        f"tick{TICK}; Strong NBB; debt DROP -3.87% vs YE2024 {DE24}",
    ),
    (
        "bud_manus_bxl_staff_jr2025_nbb",
        "2025",
        STAFF25,
        "NBB code62 bezoldigingen YE2025",
        f"tick{TICK}; Strong NBB; staff costs JUMP vs YE2024 2154516",
    ),
    (
        "bud_manus_bxl_fte_jr2025_nbb",
        "2025",
        FTE25,
        "NBB code9087 FTE YE2025",
        f"tick{TICK}; Strong NBB; FTE JUMP +7.36% vs YE2024 {FTE24}",
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
            "source_id": "src_manus_bxl_jr2025_nbb",
            "confidence": "strong",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":null,"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_assets":{AS25},"2025_debt":{DE25},"2025_staff":{STAFF25},"2025_fte":{FTE25},'
    f'"2024_bruto":{BR24},"2024_pnl":{PN24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Manus BXL YE2025 leftover dual (bruto JUMP 2.37m / empty omzet / pnl DROP -94% / "
            "FTE JUMP / Strong)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers Brussels / Manus dual / public loonkost path",
        "legal_basis": "VZW maatwerk (KBO 0828.752.657; Actief; 7 VE; NACE 88.999)",
        "decision_date": "2026-06-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00203914.pdf",
        "stated_goal": "Sheltered employment Brussels Manus dual",
        "cut_option": (
            "FOI empty omzet vs bruto 2.37m subsidy/loonkost matrix; explain pnl DROP -94% despite "
            "FTE JUMP; related-party vs Manus Antwerpen/groep"
        ),
        "source_id": "src_manus_bxl_jr2025_nbb",
        "confidence": "strong",
        "hierarchy_path": "Brussel>SintAgathaBerchem>ManusBXL>JR2025_NBB_L5",
        "notes": (
            f"tick{TICK}; Strong NBB; bruto primary (omzet empty); pnl DROP -93.88%; FTE JUMP "
            f"{FTE25}; assets {AS25}; debt {DE25}; Heropbeuring CW opaque deferred; AGB Bornem "
            "JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
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
            "Manus BXL bruto JUMP 2.37m / empty omzet / pnl DROP -94% / FTE JUMP (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Brussel>SintAgathaBerchem>ManusBXL>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"NBB bruto JUMP {BR25} (omzet unpublished) / pnl DROP {PN25} -94% from {PN24} / "
            f"FTE JUMP {FTE25} / staff {STAFF25} / op-loss flip / Manus dual"
        ),
        "confidence": "strong",
        "source_id": "src_manus_bxl_jr2025_nbb",
        "beneficiaries": "maatwerkers Brussels / Manus dual / public loonkost path",
        "stated_goal": "Sheltered employment Brussels",
        "measured_outcome": (
            "bruto JUMP +2.09%; omzet unpublished; pnl DROP -93.88%; FTE JUMP +7.36%; "
            "op-loss flip; 7 VE"
        ),
        "absurdity_score": "8.0",
        "cost_score": "4.6",
        "difficulty": "3.0",
        "priority_index": "7.00",
        "cut_proposal": (
            "FOI empty omzet vs bruto 2.37m subsidy matrix; explain pnl DROP -94% despite FTE "
            "JUMP + staff JUMP; map related-party vs Manus Antwerpen/groep"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Strong NBB PDF; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024; "
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
            "Brussel>SintAgathaBerchem>ManusBXL>subsidy_empty_omzet_pnl_drop_94pct_fte_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"Why omzet unpublished while bruto EUR{BR25} published; subsidy/loonkost/"
            f"GESCO/ESF/VDAB/gemeente matrix; pnl DROP EUR{PN25} vs YE2024 EUR{PN24} (-93.88%) "
            f"recon despite FTE JUMP {FTE24}→{FTE25}; related-party vs Manus Antwerpen/groep"
        ),
        "why_it_matters": (
            "Strong NBB shows Brussels Manus dual (bruto 2.37m / 59.8 FTE / 7 VE) with empty "
            "omzet, pnl crater -94% and FTE JUMP under public loonkost path — contrasts sister "
            "Manus Antwerpen omzet 7.66m"
        ),
        "priority": "8",
        "recipient_body": "Manus BXL VZW",
        "recipient_email": "info@manus.tv",
        "recipient_postal": "Nestor Martinstraat 313-315, 1082 Sint-Agatha-Berchem",
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
            f"tick{TICK}; ready NOT sent; Strong NBB balans public; FOI targets subsidy/empty "
            "omzet/pnl crater matrix; next every-10 2230"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2223",
    {
        "task_id": "rq_2223",
        "title": (
            "leftover dual — Manus BXL YE2025 Strong (bruto JUMP 2.37m / empty omzet / "
            "pnl DROP -94% / FTE JUMP)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Completed leftover Manus BXL after Manus groep; preferred AGB Bornem JR2024 / "
            "FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Strong NBB YE2025; FOI ready not sent"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T19:35:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; bruto {BR25} pnl {PN25} equity {EQ25} FTE {FTE25}; 7 VE Berchem; "
            "NBB 2026-00203914"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2224",
    {
        "task_id": "rq_2224",
        "title": (
            "leftover dual hole-fill after Manus BXL — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick after Manus BXL YE2025 Strong (bruto JUMP 2.37m / empty omzet / pnl DROP -94%). "
            "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
            "AIESH/REW if YE2025, else Heropbeuring 0406.678.141 if NBB/CW euros live (CW currently "
            "opaque), else unused maatwerk/WZC/IGS/DSO. Do NOT redo Manus BXL, Manus VZW groep, "
            "Manus Antwerpen, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, "
            "Kringloopwinkel Deltagroep, Kringwinkel ZOV, Groep Maatwerk, OptimaT, Huize Tordale, "
            "Odas, Ecoso, Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, "
            "Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De "
            "Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, "
            "Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
            "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, "
            "Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, "
            "Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter "
            "(YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, "
            "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
            "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2230."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2223 Manus BXL; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
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
    "last_unit_id": "rq_2223",
    "ticks_completed": "2223",
    "paused": "no",
    "notes": (
        f"tick2223 leftover Manus BXL 0828.752.657 Strong NBB (bruto JUMP {BR25}; omzet empty; "
        f"pnl DROP {PN25} -93.88%; FTE JUMP {FTE25}; 7 VE Berchem); after Manus groep@2222; "
        "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; next rq_2224; "
        "next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)
print("OK tick2223 Manus BXL written")
