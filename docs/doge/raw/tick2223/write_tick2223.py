# tick2223 — Kringwinkel Maasland YE2025 Medium leftover dual after Kringwinkel ZOV
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_kringwinkel_maasland"
TICK = "2223"
UTC = "2026-08-26T19:45:00Z"
GAP = "gap_kringwinkel_maasland_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_equity_jump_matrix_l5"
COMM = "comm_kringwinkel_maasland_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_drop_equity_jump"
LB = "lb_kringwinkel_maasland_omzet_3_18m_bruto_gt_omzet_1_81x_pnl_drop_jr2025"

OM25, OM24 = 3184457, 3018677
BR25, BR24 = 5753438, 5181229
PN25, PN24 = 227945, 302701
EQ25, EQ24 = 5956845, 5746500
FTE25 = 135.7


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
        "src_kringwinkel_maasland_jr2025_cw_nl",
        "Companyweb NL De Kringwinkel Maasland YE2025 statutory",
        "https://www.companyweb.be/nl/0417701992/de-kringwinkel-maasland",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+5.49%) bruto JUMP {BR25} (+11.04% ~1.81x) "
            f"pnl DROP {PN25} (-24.70%) equity JUMP {EQ25} (+3.66%) FTE {FTE25}; filed 31-07-2026"
        ),
    ),
    (
        "src_kringwinkel_maasland_jr2025_cw_en",
        "Companyweb EN De Kringwinkel Maasland YE2025 statutory",
        "https://www.companyweb.be/en/0417701992/de-kringwinkel-maasland",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 31-07-2026; Turnover {OM25}; "
            f"Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}"
        ),
    ),
    (
        "src_kringwinkel_maasland_jr2025_cw_fr",
        "Companyweb FR De Kringwinkel Maasland YE2025 statutory",
        "https://www.companyweb.be/fr/0417701992/de-kringwinkel-maasland",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OM25}; "
            f"Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}; Effectifs {FTE25}"
        ),
    ),
    (
        "src_kringwinkel_maasland_kbo_2223",
        "KBO De Kringwinkel Maasland 0417.701.992 Actief VZW 10 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417701992",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2223; Actief VZW sinds 06.10.1977; zetel Boorsemstraat(O) 2 3630 Maasmechelen "
            "sinds 13.02.2003; 10 VE; RSZ NACE 88.993; BTW NACE 47.792"
        ),
    ),
    (
        "src_kringwinkel_maasland_site_contact_2223",
        "Kringwinkel Maasland FOI channel info@kringwinkel.com",
        "https://www.kringwinkel.be/centra/maasland",
        "Kringwinkel Maasland",
        "foi_contact",
        "tick2223; info@kringwinkel.com / info@kringwinkel.be; Boorsemstraat 2 3630 Maasmechelen; tel 089 77 92 92",
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
        "name_nl": "De Kringwinkel Maasland VZW (Maasmechelen / maatwerk / hergebruik)",
        "name_fr": "Kringwinkel Maasland ASBL (entreprise de travail adapté / réemploi)",
        "name_en": "Kringwinkel Maasland sheltered reuse workshop (maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.kringwinkel.be/centra/maasland",
        "foi_email": "info@kringwinkel.com",
        "foi_postal": "Boorsemstraat 2, 3630 Maasmechelen",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0417.701.992 Actief VZW 10 VE "
            f"RSZ NACE 88.993 / BTW 47.792; omzet JUMP {OM25} bruto JUMP {BR25} (~1.81x) pnl DROP "
            f"{PN25} equity JUMP {EQ25} FTE {FTE25}; assets/debt Unknown"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_kringwinkel_maasland_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +5.49% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_kringwinkel_maasland_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +11.04% vs YE2024 {BR24}; bruto≫omzet ~1.81x",
    ),
    (
        "bud_kringwinkel_maasland_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -24.70% vs YE2024 {PN24}",
    ),
    (
        "bud_kringwinkel_maasland_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +3.66% vs YE2024 {EQ24}",
    ),
    (
        "bud_kringwinkel_maasland_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 135.7",
        f"tick{TICK}; Medium CW; FTE {FTE25}; YE2024 FTE Unknown on free CW; assets/debt Unknown",
    ),
    (
        "bud_kringwinkel_maasland_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_kringwinkel_maasland_jr2025_cw_en",
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
            "Kringwinkel Maasland YE2025 leftover dual (omzet JUMP 3.18m / bruto≫omzet ~1.81x / "
            "pnl DROP -24.7% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers / reuse shoppers Maasland Limburg",
        "legal_basis": "VZW maatwerk (KBO 0417.701.992; Actief; 10 VE; RSZ NACE 88.993; BTW 47.792)",
        "decision_date": "2026-07-31",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0417701992/de-kringwinkel-maasland",
        "stated_goal": "Sheltered employment + second-hand retail / circular reuse",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.81x "
            "loonkost/GESCO/ESF/VDAB/gemeente/OVAM split + pnl DROP vs equity JUMP"
        ),
        "source_id": "src_kringwinkel_maasland_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>Maasmechelen>KringwinkelMaasland>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet JUMP +5.49%; bruto JUMP +11.04% (~1.81x); "
            f"pnl DROP -24.70%; equity JUMP +3.66%; FTE {FTE25}; FOI {GAP}; "
            "stall FARO/AIESH/REW YE2024; AGB Bornem JR2024"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# absurdity 6.9 (bruto≫omzet ~1.81x + pnl DROP), cost 3.3, difficulty 3.0 → pi ~5.04
ABS, COST, DIFF, PI = "6.9", "3.3", "3.0", "5.04"
l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": "Kringwinkel Maasland omzet 3.18m / bruto≫omzet ~1.81x / pnl DROP -24.7% (YE2025)",
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Limburg>Maasmechelen>KringwinkelMaasland>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet envelope {OM25} / bruto {BR25} ≫omzet ~1.81x / pnl DROP {PN25} -24.7% / "
            f"equity JUMP {EQ25} +3.7% / FTE {FTE25}; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
        ),
        "confidence": "medium",
        "source_id": "src_kringwinkel_maasland_jr2025_cw_en",
        "beneficiaries": "maatwerkers Maasland / reuse shoppers / public loonkostsubsidie path",
        "stated_goal": "Sheltered employment + second-hand retail",
        "measured_outcome": (
            "omzet JUMP +5.49%; bruto JUMP +11.04%; pnl DROP -24.70%; equity JUMP +3.66%; FTE 135.7"
        ),
        "absurdity_score": ABS,
        "cost_score": COST,
        "difficulty": DIFF,
        "priority_index": PI,
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.81x "
            "loonkost/GESCO/ESF/OVAM matrix; pnl DROP vs equity JUMP path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "do not redo ZOV/NBSW/Opnieuw/Deltagroep/Manus/ACG"
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
            "Vlaanderen>Limburg>Maasmechelen>KringwinkelMaasland>"
            "NBB_PDF_assets_debt_bruto_gt_omzet_pnl_drop_equity_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} ≫ "
            f"omzet EUR{OM25} (~1.81x) loonkostsubsidie/GESCO/ESF/OVAM matrix; equity JUMP "
            f"EUR{EQ25} vs YE2024 EUR{EQ24} (+3.66%) with pnl DROP EUR{PN25} (-24.70%); "
            f"FTE {FTE25}; 10 VE cost allocation"
        ),
        "why_it_matters": (
            "Medium CW shows Maasland reuse/maatwerk VZW with bruto≫omzet ~1.81x while pnl "
            "DROPS −24.7% and equity JUMPS +3.7% — assets/debt unpublished; public loonkost path opaque"
        ),
        "priority": "8",
        "recipient_body": "De Kringwinkel Maasland VZW",
        "recipient_email": "info@kringwinkel.com",
        "recipient_postal": "Boorsemstraat 2, 3630 Maasmechelen",
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
        "notes": f"tick{TICK}; ready NOT sent; Medium CW; Strong KBO",
    },
)
write_csv("foi_queue.csv", f_fields, foi)

q_fields, queue = read_csv("research_queue.csv")
upsert(
    queue,
    "task_id",
    "rq_2223",
    {
        "task_id": "rq_2223",
        "title": (
            "leftover dual — Kringwinkel Maasland YE2025 Medium "
            "(omzet JUMP 3.18m / bruto≫omzet ~1.81x / pnl DROP -24.7%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "Vlaanderen>Limburg>Maasmechelen>KringwinkelMaasland>JR2025",
        "entity_id": ENTITY,
        "instructions": (
            "Fill YE2025 CW statutory euros; FOI NBB PDF assets/debt; do not redo ZOV/NBSW/Opnieuw"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T19:25:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Medium CW omzet {OM25} bruto {BR25} (~1.81x) pnl DROP {PN25} equity "
            f"JUMP {EQ25} FTE {FTE25}; FOI ready not sent; stall FARO/AIESH/REW YE2024"
        ),
    },
)
upsert(
    queue,
    "task_id",
    "rq_2224",
    {
        "task_id": "rq_2224",
        "title": (
            "leftover dual hole-fill after Kringwinkel Maasland — prefer "
            "AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "Vlaanderen>maatwerk_kringloop_WZC_residual",
        "entity_id": "",
        "instructions": (
            "Prefer FARO/AIESH/REW if YE2025 live; AGB Bornem if JR2025; else unused "
            "maatwerk/kringloop/WZC with live sourced euros (Midwest/Reset/Azalee/Vites/Stroom free). "
            "Do NOT redo Maasland/ZOV/NBSW/Opnieuw/Deltagroep/Manus/ACG."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned by tick2223; next every-10 2230",
    },
)
write_csv("research_queue.csv", q_fields, queue)

st_fields, state_rows = read_csv("loop_state.csv")
state_rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2223",
    "ticks_completed": "2223",
    "paused": "no",
    "notes": (
        f"tick2223 leftover Kringwinkel Maasland 0417.701.992 Medium (omzet JUMP {OM25}; "
        f"bruto JUMP {BR25} ~1.81x; pnl DROP {PN25} -24.70%; equity JUMP {EQ25} +3.66%; "
        f"FTE {FTE25}); FARO/AIESH/REW YE2024; AGB Bornem JR2024; after ZOV@2222; "
        "next rq_2224; next every-10 2230; continuous hole_fill"
    ),
}
write_csv("loop_state.csv", st_fields, state_rows)

entry = f"""
## Tick 2223 - {UTC} - rq_2223 Kringwinkel Maasland (omzet JUMP 3.18m / bruto≫omzet ~1.81x / pnl DROP -24.7% / Medium)

- Unit: **rq_2223** leftover dual after **rq_2222 Kringwinkel ZOV**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took named FREE leftover **De Kringwinkel Maasland VZW** YE2025 (KBO **0417.701.992**; Boorsemstraat 2 Maasmechelen; **Actief** **10 VE**; RSZ NACE **88.993** / BTW **47.792**). Deferred FREE Midwest/Reset/Azalee/Vites/Stroom. Do not redo ZOV/NBSW/Opnieuw&Co/Deltagroep/Manus/ACG/Groep Maatwerk stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +5.49% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +11.04% (bruto≫omzet ~1.81x); pnl **EUR{PN25}** DROP -24.70% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +3.66%; FTE **{FTE25}**; neerlegging **31.07.2026**. Strong KBO Actief 10 VE. Assets/debt Unknown. Medium. FOI via info@kringwinkel.com.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2223=done + rq_2224 open; loop_state ticks=2223; raw docs/doge/raw/tick2223/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2220**; next **2230**). Next: rq_2224 (AGB/FARO-if-YE2025 / AIESH-REW / unused maatwerk-WZC-IGS).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(entry)

print("OK tick2223", ENTITY, OM25, PI)
