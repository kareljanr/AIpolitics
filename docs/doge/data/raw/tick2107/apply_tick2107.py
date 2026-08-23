# -*- coding: utf-8 -*-
"""Apply tick 2107 — IDELUX Développement YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T07:10:00Z"
TICK = 2107
RQ = "rq_2107"
NEXT_RQ = "rq_2108"
ENTITY = "igs_idelux_developpement"
GAP = "gap_idelux_dev_nbb_pdf_assets_debt_pnl_flip_loss_omzet_drop_matrix_l5"
KBO = "0205.797.475"
KBO_DIGITS = "0205797475"
OMZET = 19151123
BRUTO = 10797628
PNL = -898763
EQUITY = 102328170
FTE = 91.1
EMAIL = "officiel.ic-ideluxdeveloppement@idelux.be"
ADDR = "Schoppach, drève de l'Arc-en-Ciel 98, 6700 Arlon"
LB = "lb_idelux_dev_omzet_drop_19_15m_pnl_flip_loss_0_90m_jr2025"
COMM = "comm_idelux_dev_jr2025_statutory_econ_dev"
SLUG = "association-intercommunale-pour-le-developpement-economique-durable-de-la-province-de-luxembourg"

DO_NOT_REDO = (
    "Do NOT redo IDELUX Développement, IDELUX Projets Publics, IDELUX Eau, "
    "IDELUX Finances, IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, "
    "ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, "
    "HYGEA, BEP Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, "
    "Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
    "CILE, SWDE, AGB Bornem, Armonea, Colisée Belgium, Familiezorg Gent, emeis."
)


def append_rows(path: Path, new_rows: list[dict]):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    ids = {r.get(fieldnames[0]) for r in rows}
    added = 0
    for nr in new_rows:
        if nr.get(fieldnames[0]) in ids:
            print("SKIP exists", path.name, nr.get(fieldnames[0]))
            continue
        # only keep known fields
        clean = {k: nr.get(k, "") for k in fieldnames}
        rows.append(clean)
        added += 1
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(path.name, "appended", added)


def upsert_entity():
    path = DATA / "entities.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    note = (
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief SC 1 VE "
        f"aanbestedende overheid; NACE 71.121/84.130/68.*; omzet DROP {OMZET/1e6:.2f}m "
        f"bruto DROP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m equity JUMP "
        f"{EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; neerlegging 19.06.2026; "
        f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; dual IDELUX "
        f"Eau/Environnement/Finances/Projets Publics; DISTINCT HYGEA/INTRADEL"
    )
    found = False
    for r in rows:
        if r.get("entity_id") == ENTITY:
            r["foi_email"] = EMAIL
            r["foi_postal"] = ADDR
            r["website"] = "https://www.idelux.be"
            r["notes"] = note
            found = True
            break
    if not found:
        rows.append(
            {
                "entity_id": ENTITY,
                "name_nl": "IDELUX Développement",
                "name_fr": "IDELUX Développement",
                "name_en": "Luxembourg province economic-development intercommunale",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.idelux.be",
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": note,
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("entities", "updated" if found else "created", ENTITY)


def close_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: {RQ} status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — IDELUX Développement YE2025 Medium"
            r["instructions"] = (
                f"Completed leftover IDELUX Développement YE2025 Medium CW; KBO {KBO}; "
                f"omzet DROP {OMZET} bruto DROP {BRUTO} pnl FLIP LOSS {PNL} equity JUMP "
                f"{EQUITY} FTE DROP {FTE}; FOI {GAP}; 1 VE; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; dual IDELUX group; DISTINCT Eau/Projets Publics"
            )
            r["notes"] = (
                f"tick{TICK} IDELUX Développement Medium omzet DROP {OMZET/1e6:.2f}m "
                f"bruto DROP {BRUTO/1e6:.2f}m pnl FLIP LOSS {abs(PNL)/1e6:.2f}m equity JUMP "
                f"{EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after IDELUX Développement — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after IDELUX Développement YE2025 Medium. Prefer "
                    "leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych (Sint-Camillus Wevelgem 0417.958.152 / "
                    "Zilverlinde Olen 0445.175.263 deferred). " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} IDELUX Développement; next every-10 2110; "
                    "Camillus/Zilverlinde YE2025 deferred"
                ),
            }
        )
        print("spawned", NEXT_RQ)
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue closed", RQ)


def write_loop_state():
    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "state_id",
                "mode",
                "current_sprint",
                "last_tick_utc",
                "last_unit_id",
                "ticks_completed",
                "paused",
                "notes",
            ],
            lineterminator="\n",
        )
        w.writeheader()
        w.writerow(
            {
                "state_id": "main",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "last_tick_utc": UTC,
                "last_unit_id": RQ,
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover IDELUX Développement {KBO} Medium CW "
                    f"(omzet DROP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                    f"pnl FLIP LOSS {abs(PNL)/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE DROP {FTE}; assets/debt Unknown; 1 VE econ-dev dual IDELUX); "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                    f"next every-10 2110; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} IDELUX Développement (omzet DROP 19.15m / pnl FLIP LOSS 0.90m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2106 IDELUX Projets Publics**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred **IDELUX Développement** YE2025 (KBO **{KBO}**; Schoppach Arlon; **SC** econ-dev NACE **71.121/84.130** / **1 VE**; aanbestedende overheid). Do not redo Projets Publics/Eau/Finances/Environnement/INTRADEL/Korian/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** DROP −29.80%; bruto **EUR{BRUTO}** DROP −20.50%; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR3205547 (−128.04%); equity **EUR{EQUITY}** JUMP +1.15%; FTE **{FTE}** DROP vs YE2024 118.1; neerlegging **19.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.0); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2107/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2100**; next **2110**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused WZC Camillus/Zilverlinde deferred).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")


def main():
    # race check first
    with (DATA / "research_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["task_id"] == RQ and (r.get("status") or "").lower() not in (
                "open",
                "in_progress",
            ):
                raise SystemExit(f"RACE early: {RQ} status={r.get('status')}")

    upsert_entity()
    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_idelux_dev_jr2025_cw_nl",
                "title": "Companyweb NL — IDELUX Développement YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} FTE {FTE}",
            },
            {
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "title": "Companyweb EN — IDELUX Développement YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed 19.06.2026; equity {EQUITY}; FTE {FTE}; last BS year 2025",
            },
            {
                "source_id": "src_idelux_dev_jr2025_cw_fr",
                "title": "Companyweb FR — IDELUX Développement YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_idelux_dev_kbo_{TICK}",
                "title": f"KBO — IDELUX Développement {KBO}",
                "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief SC 1 VE; NACE 71.121/84.130/68.*; "
                    f"aanbestedende overheid; {EMAIL}; zetel {ADDR}; Strong identity"
                ),
            },
            {
                "source_id": f"src_idelux_dev_contact_{TICK}",
                "title": "IDELUX Développement FOI contact",
                "url": "https://www.idelux.be/",
                "publisher": "IDELUX",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; {EMAIL}; {ADDR}",
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_idelux_dev_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope econ-dev SC)",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP -29.80% vs YE2024 27281519",
            },
            {
                "budget_id": "bud_idelux_dev_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP -20.50% vs YE2024 13582098",
            },
            {
                "budget_id": "bud_idelux_dev_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLIP LOSS vs YE2024 PROFIT 3205547 (-128.04%)",
            },
            {
                "budget_id": "bud_idelux_dev_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.15% vs YE2024 101166215",
            },
            {
                "budget_id": "bud_idelux_dev_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} DROP vs YE2024 118.1",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "IDELUX Développement YE2025 leftover dual "
                    "(omzet DROP 19.15m / pnl FLIP LOSS 0.90m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "Luxembourg-province communes / economic-development users",
                "legal_basis": (
                    f"SC intercommunale econ-dev (KBO {KBO}; NACE 71.121/84.130; "
                    "1 VE; aanbestedende overheid)"
                ),
                "decision_date": "2026-06-19",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": str(OMZET),
                "cash_by_year": (
                    f'{{"2025_omzet":{OMZET},"2025_bruto":{BRUTO},"2025_pnl":{PNL},'
                    f'"2025_equity":{EQUITY},"2025_fte":{FTE}}}'
                ),
                "remaining_eur": "0",
                "status": "active",
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "stated_goal": "Public economic development intercommunale (IDELUX Développement)",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain omzet DROP and pnl FLIP LOSS; "
                    "map dual IDELUX group related-party flows"
                ),
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Luxembourg>IDELUX_Developpement>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "dual IDELUX Eau/Environnement/Finances/Projets Publics; DISTINCT HYGEA/INTRADEL"
                ),
            }
        ],
    )
    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": (
                    "IDELUX Développement omzet DROP 19.15m / pnl FLIP LOSS 0.90m (YE2025)"
                ),
                "level": "L5",
                "type": "econ_dev_statutory_intercommunale",
                "hierarchy_path": "Wallonie>Luxembourg>IDELUX_Developpement>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} DROP -29.80% (primary); bruto {BRUTO} DROP "
                    f"-20.50%; pnl LOSS {PNL} FLIP -128.04%; equity {EQUITY} JUMP +1.15%; "
                    f"FTE {FTE} DROP; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_idelux_dev_jr2025_cw_en",
                "beneficiaries": "Luxembourg-province communes / econ-dev users (1 VE)",
                "stated_goal": "Public economic development intercommunale",
                "measured_outcome": (
                    "omzet DROP -29.80%; bruto DROP -20.50%; pnl FLIP LOSS -128.04%; "
                    "equity JUMP +1.15%; FTE DROP 91.1 vs 118.1"
                ),
                "absurdity_score": "6.8",
                "cost_score": "5.0",
                "difficulty": "4.0",
                "priority_index": "6.0",
                "cut_proposal": (
                    "FOI NBB PDF + activity split + explain omzet DROP/pnl FLIP LOSS/"
                    "FTE DROP; map dual IDELUX group related-party flows"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
                    "dual IDELUX; DISTINCT Eau/Projets Publics/Finances/Environnement"
                ),
            }
        ],
    )
    with (DATA / "foi_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
        foi_fields = csv.DictReader(fh).fieldnames
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Luxembourg>IDELUX_Developpement>NBB_PDF_assets_debt_pnl_flip_omzet_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP LOSS path; "
            "omzet DROP activity split; FTE DROP path; dual IDELUX group related-party map"
        ),
        "why_it_matters": (
            "Medium CW shows 19.15m omzet Luxembourg econ-dev SC with pnl FLIP to LOSS "
            "-0.90m and omzet DROP -29.8% while equity stays >102m — public-development "
            "continuity risk without balance-sheet transparency"
        ),
        "priority": "8",
        "recipient_body": "IDELUX Développement SC",
        "recipient_email": EMAIL,
        "recipient_postal": ADDR,
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2110",
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
