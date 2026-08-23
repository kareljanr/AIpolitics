# -*- coding: utf-8 -*-
"""Apply tick 2106 — IDELUX Eau YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)

UTC = "2026-08-25T07:00:00Z"
TICK = 2106
RQ = "rq_2106"
NEXT_RQ = "rq_2107"
ENTITY = "idelux_eau"
GAP = "gap_idelux_eau_nbb_pdf_assets_debt_pnl_jump_spge_oaa_matrix_l5"
KBO = "0204.359.994"
KBO_DIGITS = "0204359994"
OMZET = 26319619
BRUTO = 15966385
PNL = 1721496
EQUITY = 50559932
FTE = 101.2
EMAIL = "idelux@idelux.be"
ADDR = "Schoppach, drève de l'Arc-en-Ciel 98, 6700 Arlon"
LB = "lb_idelux_eau_omzet_jump_26_32m_pnl_jump_1_72m_spge_oaa_jr2025"
COMM = "comm_idelux_eau_jr2025_statutory_spge_oaa"

DO_NOT_REDO = (
    "Do NOT redo IDELUX Eau, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, "
    "SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, HYGEA, BEP Environnement, "
    "IDELUX Environnement, IDELUX Finances, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, "
    "BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
    "CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, "
    "EURIDICE, IRE*, BRUGEL, AGB Bornem, Armonea, Colisée Belgium, Familiezorg Gent, "
    "emeis Belgium."
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
        rows.append(nr)
        added += 1
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(path.name, "appended", added)


def update_entity():
    path = DATA / "entities.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("entity_id") == ENTITY:
            r["foi_email"] = EMAIL
            r["foi_postal"] = ADDR
            r["notes"] = (
                f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief SC "
                f"13 VE aanbestedende overheid; NACE 37.000 sewerage; omzet JUMP "
                f"{OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m "
                f"(+201.26%) equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt "
                f"Unknown; neerlegging 19.06.2026; FOI {GAP}; preferred AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; dual SPGE/AIDE/INASEP/inBW; DISTINCT "
                f"IDELUX Environnement/Finances/HYGEA/INTRADEL; prior tick588 RA narrative"
            )
            r["website"] = "https://www.idelux.be"
            found = True
            break
    if not found:
        rows.append(
            {
                "entity_id": ENTITY,
                "name_nl": "IDELUX Eau",
                "name_fr": "IDELUX Eau",
                "name_en": "Luxembourg province water sanitation OAA intercommunale",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.idelux.be",
                "foi_email": EMAIL,
                "foi_postal": ADDR,
                "notes": f"tick{TICK} YE2025 Medium CW; KBO {KBO}",
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("entities updated", ENTITY, "found" if found else "created")


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
            r["title"] = "leftover dual — IDELUX Eau YE2025 Medium"
            r["instructions"] = (
                f"Completed leftover IDELUX Eau YE2025 Medium CW; KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP "
                f"{EQUITY} FTE DROP {FTE}; FOI {GAP}; 13 VE NACE 37.000; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; dual SPGE OAA; "
                f"DISTINCT IDELUX Environnement/Finances/HYGEA/INTRADEL"
            )
            r["notes"] = (
                f"tick{TICK} IDELUX Eau Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP "
                f"{BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after IDELUX Eau — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after IDELUX Eau YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                    "AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/"
                    "WZC/psych (e.g. Sint-Camillus Wevelgem 0417.958.152 or Zilverlinde "
                    "Olen 0445.175.263 if still unused). " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} IDELUX Eau; next every-10 2110; "
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
    path = DATA / "loop_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
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
                    f"tick{TICK} leftover IDELUX Eau {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE DROP {FTE}; assets/debt Unknown; NACE 37.000 13 VE SPGE OAA dual); "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                    f"next every-10 2110; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} IDELUX Eau (omzet JUMP 26.32m / pnl JUMP 1.72m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2105 INTRADEL**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred **IDELUX Eau** YE2025 (KBO **{KBO}**; Schoppach Arlon; **SC** sewerage NACE **37.000** / **13 VE**; aanbestedende overheid; dual SPGE/AIDE/INASEP). Do not redo INTRADEL/Korian/Comnexio/ORES SC/HYGEA/IDELUX Environnement/Finances/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +4.73%; bruto **EUR{BRUTO}** JUMP +7.34%; pnl **PROFIT EUR{PNL}** JUMP +201.26% vs YE2024 PROFIT EUR571426; equity **EUR{EQUITY}** JUMP +8.43%; FTE **{FTE}** DROP vs YE2024 102.2; neerlegging **19.06.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.2); entities (update {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2106/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2100**; next **2110**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused WZC Camillus/Zilverlinde deferred).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")


def main():
    update_entity()
    append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": "src_idelux_eau_jr2025_cw_nl",
                "title": "Companyweb NL — IDELUX Eau YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/idelux-eau",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} FTE {FTE}",
            },
            {
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "title": "Companyweb EN — IDELUX Eau YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/idelux-eau",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; filed 19.06.2026; equity {EQUITY}; FTE {FTE}; last BS year 2025",
            },
            {
                "source_id": "src_idelux_eau_jr2025_cw_fr",
                "title": "Companyweb FR — IDELUX Eau YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/idelux-eau",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_idelux_eau_kbo_{TICK}",
                "title": f"KBO — IDELUX Eau {KBO}",
                "url": f"https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer={KBO_DIGITS}",
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief SC 13 VE; NACE 37.000 sewerage; "
                    f"aanbestedende overheid; zetel {ADDR}; Strong identity"
                ),
            },
            {
                "source_id": f"src_idelux_eau_contact_{TICK}",
                "title": "IDELUX contact (Eau dual)",
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
                "budget_id": "bud_idelux_eau_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope SPGE OAA SC)",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +4.73% vs YE2024 25131409; dual SPGE stack",
            },
            {
                "budget_id": "bud_idelux_eau_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +7.34% vs YE2024 14874373",
            },
            {
                "budget_id": "bud_idelux_eau_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +201.26% vs YE2024 PROFIT 571426",
            },
            {
                "budget_id": "bud_idelux_eau_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +8.43% vs YE2024 46628011",
            },
            {
                "budget_id": "bud_idelux_eau_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} DROP vs YE2024 102.2",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "IDELUX Eau YE2025 leftover dual (omzet JUMP 26.32m / "
                    "pnl JUMP 1.72m / SPGE OAA)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "Luxembourg-province communes / SPGE sanitation users",
                "legal_basis": (
                    f"SC intercommunale sewerage (KBO {KBO}; NACE 37.000; 13 VE; "
                    "aanbestedende overheid)"
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
                "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}/idelux-eau",
                "stated_goal": "Public wastewater sanitation OAA (IDELUX Eau / SPGE dual)",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl JUMP +201%; "
                    "map SPGE/AIDE/INASEP/inBW related-party flows"
                ),
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Wallonie>Luxembourg>IDELUX_Eau>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "dual SPGE/AIDE/INASEP; DISTINCT IDELUX Environnement/Finances/HYGEA/INTRADEL"
                ),
            }
        ],
    )
    append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "IDELUX Eau omzet JUMP 26.32m / pnl JUMP 1.72m / SPGE OAA (YE2025)",
                "level": "L5",
                "type": "water_oaa_statutory_intercommunale",
                "hierarchy_path": "Wallonie>Luxembourg>IDELUX_Eau>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +4.73% (primary); bruto {BRUTO} JUMP "
                    f"+7.34%; pnl PROFIT {PNL} JUMP +201.26%; equity {EQUITY} JUMP +8.43%; "
                    f"FTE {FTE} DROP; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_idelux_eau_jr2025_cw_en",
                "beneficiaries": "Luxembourg-province commune households / SPGE OAA users (13 VE)",
                "stated_goal": "Public wastewater sanitation intercommunale (SPGE dual)",
                "measured_outcome": (
                    "omzet JUMP +4.73%; bruto JUMP +7.34%; pnl JUMP +201.26%; "
                    "equity JUMP +8.43%; FTE DROP -1.0 vs 102.2"
                ),
                "absurdity_score": "5.0",
                "cost_score": "5.2",
                "difficulty": "4.0",
                "priority_index": "5.2",
                "cut_proposal": (
                    "FOI NBB PDF + SPGE/CSU OAA split + related-party map to "
                    "AIDE/INASEP/inBW; explain pnl JUMP path"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still YE2024; "
                    "dual SPGE; DISTINCT IDELUX Environnement/Finances/HYGEA/INTRADEL"
                ),
            }
        ],
    )
    # foi_queue may have extra notes col
    with (DATA / "foi_queue.csv").open(encoding="utf-8-sig", newline="") as fh:
        foi_fields = csv.DictReader(fh).fieldnames
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Luxembourg>IDELUX_Eau>NBB_PDF_assets_debt_pnl_jump_spge_oaa",
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl JUMP path; "
            "SPGE/CSU OAA vs commune cotisations split; FTE YoY; AIDE/INASEP/inBW related-party map"
        ),
        "why_it_matters": (
            "Medium CW shows 26.32m omzet Luxembourg water OAA SC with pnl JUMP +201% "
            "and Unknown balance sheet — public sanitation continuity risk without SPGE dual transparency"
        ),
        "priority": "8",
        "recipient_body": "IDELUX Eau SC",
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
    }
    if "notes" in (foi_fields or []):
        foi_row["notes"] = (
            f"tick{TICK}; human-send only; Medium CW; next every-10 2110"
        )
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
