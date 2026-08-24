# tick2222 — Kringwinkel Zuid-Oost-Vlaanderen YE2025 Medium leftover dual
# (race: tick2221 Manus took rq_2221; this unit closes rq_2222)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_kringwinkel_zov"
TICK = "2222"
UTC = "2026-08-26T19:25:00Z"
GAP = "gap_kringwinkel_zov_nbb_pdf_assets_debt_bruto_gt_omzet_equity_jump_pnl_drop_matrix_l5"
COMM = "comm_kringwinkel_zov_jr2025_statutory_maatwerk_bruto_gt_omzet_equity_jump"
LB = "lb_kringwinkel_zov_omzet_3_86m_bruto_gt_omzet_1_60x_equity_jump_jr2025"

OM25, OM24 = 3857860, 3851895
BR25, BR24 = 6163360, 5907046
PN25, PN24 = 506445, 546170
EQ25, EQ24 = 5180878, 4674433
FTE25, FTE24 = 136.6, 131.5


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


# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_kringwinkel_zov_jr2025_cw_nl",
        "Companyweb NL Kringwinkel Zuid-Oost-Vlaanderen YE2025 statutory",
        "https://www.companyweb.be/nl/0466159432/kringwinkel-zuid-oost-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; YE2025 omzet {OM25} (+0.15%) bruto JUMP {BR25} (+4.34% ~1.60x) pnl DROP {PN25} (-7.27%) equity JUMP {EQ25} (+10.83%) FTE {FTE25}; filed 28-05-2026",
    ),
    (
        "src_kringwinkel_zov_jr2025_cw_en",
        "Companyweb EN Kringwinkel Zuid-Oost-Vlaanderen YE2025 statutory",
        "https://www.companyweb.be/en/0466159432/kringwinkel-zuid-oost-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; EN mirror YE2025 Medium; filed 28-05-2026; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; Employees {FTE25}",
    ),
    (
        "src_kringwinkel_zov_jr2025_cw_fr",
        "Companyweb FR Kringwinkel Zuid-Oost-Vlaanderen YE2025 statutory",
        "https://www.companyweb.be/fr/0466159432/kringwinkel-zuid-oost-vlaanderen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OM25}; Marge brute {BR25}; Benefice {PN25}; Capitaux propres {EQ25}; Effectifs {FTE25}",
    ),
    (
        "src_kringwinkel_zov_kbo_2222",
        "KBO Kringwinkel Zuid-Oost-Vlaanderen 0466.159.432 Actief VZW 10 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466159432",
        "KBO FOD Economie",
        "official_register",
        "tick2222; Actief VZW sinds 27.01.1999; zetel Gaverstraat(Ove) 35 9500 Geraardsbergen sinds 16.03.2026; 10 VE; RSZ NACE 88.993; BTW NACE 47.793",
    ),
    (
        "src_kringwinkel_zov_site_contact_2222",
        "Kringwinkel ZOV FOI channel info@kwzov.be",
        "https://www.kringwinkel.be/regio/kwzov/contact",
        "Kringwinkel Zuid-Oost-Vlaanderen",
        "foi_contact",
        "tick2222; info@kwzov.be; hoofdzetel Alexandre Louis Vanhovestraat 14 9600 Ronse; tel 054 32 05 00; KBO zetel Gaverstraat 35 Geraardsbergen",
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

# --- entities ---
e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "Kringwinkel Zuid-Oost-Vlaanderen VZW (Geraardsbergen/Ronse / maatwerk / hergebruik)",
        "name_fr": "Kringwinkel Flandre orientale-Sud ASBL (entreprise de travail adapté / réemploi)",
        "name_en": "Kringwinkel South-East Flanders sheltered reuse workshop (maatwerk)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.kringwinkel.be/centra/zuid-oost-vlaanderen",
        "foi_email": "info@kwzov.be",
        "foi_postal": "Alexandre Louis Vanhovestraat 14, 9600 Ronse",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0466.159.432 Actief VZW 10 VE "
            f"RSZ NACE 88.993 / BTW 47.793; omzet {OM25} bruto JUMP {BR25} (~1.60x) pnl DROP {PN25} "
            f"equity JUMP {EQ25} FTE {FTE25}; KBO zetel Gaverstraat 35 Geraardsbergen; assets/debt Unknown"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

# --- budgets ---
b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_kringwinkel_zov_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet / Turnover YE2025",
        f"tick{TICK}; Medium CW; omzet flat +0.15% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_kringwinkel_zov_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +4.34% vs YE2024 {BR24}; bruto≫omzet ~1.60x",
    ),
    (
        "bud_kringwinkel_zov_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick{TICK}; Medium CW; pnl DROP -7.27% vs YE2024 {PN24}",
    ),
    (
        "bud_kringwinkel_zov_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +10.83% vs YE2024 {EQ24}",
    ),
    (
        "bud_kringwinkel_zov_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE / Employees 136.6",
        f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_kringwinkel_zov_omzet_jr2024_statutory_cmp",
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
            "source_id": "src_kringwinkel_zov_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

# --- commitments ---
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
            "Kringwinkel Zuid-Oost-Vlaanderen YE2025 leftover dual "
            "(omzet 3.86m / bruto≫omzet ~1.60x / equity JUMP +10.8% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "maatwerkers / reuse shoppers Zuid-Oost-Vlaanderen",
        "legal_basis": "VZW maatwerk (KBO 0466.159.432; Actief; 10 VE; RSZ NACE 88.993; BTW 47.793)",
        "decision_date": "2026-05-28",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0466159432/kringwinkel-zuid-oost-vlaanderen",
        "stated_goal": "Sheltered employment + second-hand retail / circular reuse",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.60x "
            "loonkost/GESCO/ESF/VDAB/gemeente/OVAM split + equity JUMP vs pnl DROP"
        ),
        "source_id": "src_kringwinkel_zov_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Geraardsbergen>KringwinkelZOV>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary; bruto≫omzet ~1.60x; equity JUMP +10.83%; "
            f"pnl DROP -7.27%; FTE {FTE25}; 10 VE; assets/debt Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; after Manus@2221; not TE-additive of 348bn"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# --- leaderboard ---
# pi = 0.55*3.5 + 0.35*6.6 + 0.10*7 = 4.93
l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Kringwinkel ZOV omzet 3.86m / bruto≫omzet ~1.60x / equity JUMP +10.8% (YE2025)"
        ),
        "level": "L5",
        "type": "maatwerk_vzw_statutory",
        "hierarchy_path": "Vlaanderen>OostVlaanderen>Geraardsbergen>KringwinkelZOV>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet envelope {OM25} / bruto {BR25} ≫omzet ~1.60x / pnl DROP {PN25} -7.3% / "
            f"equity JUMP {EQ25} +10.8% / FTE JUMP {FTE25}; wage-cost subsidies opaque; "
            "assets/debt Unknown pending NBB PDF"
        ),
        "confidence": "medium",
        "source_id": "src_kringwinkel_zov_jr2025_cw_en",
        "beneficiaries": "maatwerkers ZOV / reuse shoppers / public loonkostsubsidie path",
        "stated_goal": "Sheltered employment + second-hand retail",
        "measured_outcome": (
            "omzet flat +0.15%; bruto JUMP +4.34%; pnl DROP -7.27%; equity JUMP +10.83%; "
            f"FTE JUMP +3.9% to {FTE25}"
        ),
        "absurdity_score": "6.6",
        "cost_score": "3.5",
        "difficulty": "3.0",
        "priority_index": "4.93",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~1.60x "
            "loonkost/GESCO/ESF/OVAM matrix; equity JUMP vs pnl DROP path"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
            "AGB Bornem JR2024; after Manus@2221; next every-10 2230"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

# --- foi ---
f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Geraardsbergen>KringwinkelZOV>"
            "NBB_PDF_assets_debt_bruto_gt_omzet_equity_jump_pnl_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BR25} ≫ "
            f"omzet EUR{OM25} (~1.60x) loonkostsubsidie/GESCO/ESF/OVAM matrix; equity JUMP "
            f"EUR{EQ25} vs YE2024 EUR{EQ24} (+10.83%) with pnl DROP EUR{PN25} (-7.27%); "
            f"FTE JUMP {FTE24}→{FTE25}; 10 VE cost allocation"
        ),
        "why_it_matters": (
            "Medium CW shows ZOV reuse/maatwerk VZW with bruto≫omzet ~1.60x while equity JUMPS "
            "+10.8% and pnl DROPS −7.3% — assets/debt unpublished; public loonkost path opaque"
        ),
        "priority": "8",
        "recipient_body": "Kringwinkel Zuid-Oost-Vlaanderen VZW",
        "recipient_email": "info@kwzov.be",
        "recipient_postal": "Alexandre Louis Vanhovestraat 14, 9600 Ronse",
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
            f"tick{TICK}; Medium CW YE2025; ready NOT sent; stall FARO/AIESH/REW YE2024; "
            "AGB Bornem JR2024; after Manus@2221"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

# --- research_queue ---
rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2222",
    {
        "task_id": "rq_2222",
        "title": (
            "leftover dual — Kringwinkel Zuid-Oost-Vlaanderen YE2025 Medium "
            "(omzet 3.86m / bruto≫omzet ~1.60x / equity JUMP +10.8%)"
        ),
        "sprint": "continuous",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "Leftover dual hole-fill after rq_2221 Manus. Prefer NON-stall live: AGB Bornem JR2025 / "
            "FARO YE2025 / AIESH-REW YE2025 else unused maatwerk-kringloop. Took Kringwinkel ZOV."
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T19:15:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Medium CW; omzet {OM25} bruto {BR25} pnl DROP {PN25} equity JUMP {EQ25} "
            f"FTE {FTE25}; FOI ready; next every-10 2230"
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
            "leftover dual hole-fill after Kringwinkel ZOV — prefer "
            "AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS"
        ),
        "sprint": "continuous",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Leftover dual hole-fill after rq_2222 Kringwinkel Zuid-Oost-Vlaanderen YE2025 Medium "
            "(omzet 3.86m / bruto≫omzet ~1.60x / equity JUMP +10.8%). Prefer NON-stall live: "
            "AGB Bornem if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
            "else unused maatwerk/kringloop/WZC/IGS/DSO with live sourced €. Do NOT redo "
            "Kringwinkel ZOV/Manus/NBSW/Opnieuw&Co/Deltagroep/Groep Maatwerk/Odas/OptimaT/"
            "Constructief/Werkmmaat/Veerkracht4/ACG/Entiris/Oesterbank stack."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2222 Kringwinkel ZOV; FARO/AIESH/REW still YE2024; "
            "AGB Bornem JR2024; next EVERY-10 at 2230"
        ),
    },
)
write_csv("research_queue.csv", rq_fields, rq)

# --- loop_state ---
ls_fields, ls = read_csv("loop_state.csv")
upsert(
    ls,
    "state_id",
    "main",
    {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2222",
        "ticks_completed": "2222",
        "paused": "no",
        "notes": (
            "tick2222 leftover Kringwinkel ZOV 0466.159.432 Medium (omzet 3857860; bruto JUMP "
            "6163360 ~1.60x; pnl DROP 506445 -7.27%; equity JUMP 5180878 +10.83%; FTE JUMP 136.6); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Manus@2221; next rq_2223; "
            "next every-10 2230; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

# --- update FOI draft tick ref ---
draft = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{GAP}.md"
if draft.exists():
    txt = draft.read_text(encoding="utf-8")
    txt = txt.replace("**tick:** 2221", "**tick:** 2222")
    draft.write_text(txt, encoding="utf-8")

# --- log ---
log_block = f"""

## Tick 2222 - {UTC} - rq_2222 Kringwinkel Zuid-Oost-Vlaanderen (omzet 3.86m / bruto≫omzet ~1.60x / equity JUMP +10.8% / Medium)

- Unit: **rq_2222** leftover dual after **rq_2221 Manus** (race: this agent first probed KZOV as rq_2221 but Manus committed first — rebased to rq_2222). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024-class**. Took named FREE leftover **Kringwinkel Zuid-Oost-Vlaanderen VZW** YE2025 (KBO **0466.159.432**; Gaverstraat 35 Geraardsbergen KBO zetel; hoofdzetel Ronse; **Actief** **10 VE**; RSZ NACE **88.993** / BTW **47.793**). Do not redo Manus/NBSW/Opnieuw&Co/Deltagroep/Groep Maatwerk/Odas/OptimaT/Constructief/Werkmmaat/Veerkracht4/ACG stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** flat +0.15% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +4.34% (bruto≫omzet ~1.60x); pnl **EUR{PN25}** DROP -7.27% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +10.83%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **28.05.2026**. Strong KBO Actief 10 VE. Assets/debt Unknown. Medium. FOI via info@kwzov.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 4.93); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2222=done + rq_2223 open; loop_state ticks=2222; raw docs/doge/raw/tick2222/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2220**; next **2230**). Next: rq_2223 (AGB/FARO-if-YE2025 / AIESH-REW / unused maatwerk-WZC-IGS).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick2222 OK", ENTITY, OM25, BR25, PN25, EQ25, FTE25)
