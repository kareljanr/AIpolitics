# -*- coding: utf-8 -*-
"""Apply tick 2110 EVERY-10 — Rusthuis Sint Jozef Ninove YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T07:55:00Z"
TICK = 2110
RQ = "rq_2110"
NEXT_RQ = "rq_2111"
ENTITY = "bv_rusthuis_sint_jozef_ninove"
GAP = "gap_sint_jozef_ninove_nbb_pdf_assets_debt_pnl_drop_omzet_jump_matrix_l5"
KBO = "0452.865.383"
KBO_DIGITS = "0452865383"
OMZET = 11899054
BRUTO = 7819890
PNL = 209734
EQUITY = 857139
FTE = 128.8
OMZET_PRIOR = 11590573
PNL_PRIOR = 957563
BRUTO_PRIOR = 7688762
EQUITY_PRIOR = 847404
FTE_PRIOR = 124.4
EMAIL = "dir.wilgendries.voorde@mr-wzc.be"
ADDR = "Geraardsbergsesteenweg 303, 9400 Ninove"
WEBSITE = "https://www.wilgendries.be"
LB = "lb_sint_jozef_ninove_omzet_jump_11_90m_pnl_drop_jr2025"
COMM = "comm_sint_jozef_ninove_jr2025_statutory_wzc"
SLUG = "rusthuis-sint-jozef"

DO_NOT_REDO = (
    "Do NOT redo Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, "
    "Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX Développement, "
    "IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, IDELUX Environnement, "
    "INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, "
    "Always Home, SLG Operaties, AREWAL, HYGEA, BEP Environnement, AIEG, RESA, "
    "Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, "
    "IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, "
    "Colisée Belgium, Familiezorg Gent, emeis, IRE*, FANC, SCK CEN, EURIDICE, "
    "Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief BV/SRL "
        f"2 VE NACE 87.301 ROB; omzet JUMP {OMZET/1e6:.2f}m (+2.66%) bruto JUMP "
        f"{BRUTO/1e6:.2f}m (+1.71%) pnl DROP {PNL/1e6:.2f}m (−78.10%) equity JUMP "
        f"{EQUITY/1e6:.2f}m (+1.15%) FTE JUMP {FTE} (vs {FTE_PRIOR}); "
        f"assets/debt Unknown; neerlegging 30.07.2026; FOI {GAP}; Wilgendries path; "
        f"preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT "
        f"Zilverlinde/Sint-Camillus/Armonea/SLG/emeis/Korian"
    )
    found = False
    for r in rows:
        if r.get("entity_id") == ENTITY:
            r["foi_email"] = EMAIL
            r["foi_postal"] = ADDR
            r["website"] = WEBSITE
            r["notes"] = note
            found = True
            break
    if not found:
        rows.append(
            {
                "entity_id": ENTITY,
                "name_nl": "Rusthuis Sint Jozef (Ninove)",
                "name_fr": "Maison de repos Sint Jozef (Ninove)",
                "name_en": "Nursing home Rusthuis Sint Jozef Ninove (BV/SRL)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": WEBSITE,
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
            r["title"] = (
                "EVERY-10 + leftover dual — Rusthuis Sint Jozef Ninove YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed EVERY-10 + leftover Rusthuis Sint Jozef Ninove YE2025 "
                f"Medium CW; KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} "
                f"pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}; 2 VE "
                f"NACE 87.301; progress+waste refreshed; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} EVERY-10 Sint-Jozef Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP "
                f"{EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; progress+waste @2110; "
                f"next {NEXT_RQ}; next every-10 2120"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Sint-Jozef Ninove — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused DSO-water-IGS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after EVERY-10 Rusthuis Sint Jozef Ninove "
                    "YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else "
                    "unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Sint-Jozef EVERY-10; "
                    "FARO/AIESH/REW still YE2024; next every-10 2120"
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
                    f"tick{TICK} EVERY-10 leftover Rusthuis Sint Jozef Ninove {KBO} "
                    f"Medium CW (omzet JUMP {OMZET/1e6:.2f}m bruto JUMP "
                    f"{BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP "
                    f"{EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; 2 VE "
                    f"NACE 87.301); progress+waste refreshed; AGB Bornem JR2024; "
                    f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2120; "
                    f"continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} EVERY-10 + Rusthuis Sint Jozef Ninove (omzet JUMP 11.90m / pnl DROP 0.21m / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **rq_2109 WZC Zilverlinde Olen**. MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md (done). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred unused **Rusthuis Sint Jozef Ninove** YE2025 (KBO **{KBO}**; Geraardsbergsesteenweg 303 Ninove; **BV/SRL** NACE **87.301** ROB / **2 VE**; Wilgendries path). Do not redo Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +2.66%; bruto **EUR{BRUTO}** JUMP +1.71%; pnl **EUR{PNL}** DROP −78.10% vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP +1.15% (thin vs omzet); FTE **{FTE}** JUMP vs {FTE_PRIOR}; neerlegging **30.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.6); entities (+1 {ENTITY}); foi + draft {GAP}; progress+waste EVERY-10 @2110; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2110/.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done (last was 2100; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-water-IGS-HVZ).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")


def main():
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
                "source_id": "src_sint_jozef_ninove_jr2025_cw_nl",
                "title": "Companyweb NL — Rusthuis Sint Jozef Ninove YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl {PNL} "
                    f"FTE {FTE}"
                ),
            },
            {
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "title": "Companyweb EN — Rusthuis Sint Jozef Ninove YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 30.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_sint_jozef_ninove_jr2025_cw_fr",
                "title": "Companyweb FR — Rusthuis Sint Jozef Ninove YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_sint_jozef_ninove_kbo_{TICK}",
                "title": f"KBO — Rusthuis Sint Jozef Ninove {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief BV/SRL 2 VE; NACE 87.301 ROB; zetel {ADDR}; "
                    f"email {EMAIL}; Strong identity"
                ),
            },
            {
                "source_id": f"src_sint_jozef_ninove_contact_{TICK}",
                "title": "WZC Wilgendries / Rusthuis Sint Jozef FOI contact",
                "url": "https://www.wilgendries.be/voorde/contact",
                "publisher": "WZC Wilgendries / Rusthuis Sint Jozef",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; sociale dienst 0471 98 67 72; {ADDR}; "
                    f"{WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_sint_jozef_ninove_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope WZC BV)",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +2.66% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_sint_jozef_ninove_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.71% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_sint_jozef_ninove_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −78.10% vs YE2024 {PNL_PRIOR}",
            },
            {
                "budget_id": "bud_sint_jozef_ninove_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.15% vs YE2024 {EQUITY_PRIOR}; thin vs omzet",
            },
            {
                "budget_id": "bud_sint_jozef_ninove_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE JUMP {FTE} vs YE2024 {FTE_PRIOR}",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Rusthuis Sint Jozef Ninove YE2025 leftover dual "
                    "(omzet JUMP 11.90m / pnl DROP 0.21m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "WZC residents / care users Ninove (Wilgendries path)",
                "legal_basis": (
                    f"BV/SRL woonzorgcentrum ROB (KBO {KBO}; NACE 87.301; 2 VE)"
                ),
                "decision_date": "2026-07-30",
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
                "stated_goal": (
                    "Public-interest nursing-home care (Rusthuis Sint Jozef / Wilgendries)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl DROP −78.10% with "
                    "omzet JUMP +2.66%; map public care toelage vs private fee split; "
                    "2 VE transparency"
                ),
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>OostVlaanderen>Ninove>Rusthuis_Sint_Jozef>"
                    "JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "DISTINCT Zilverlinde/Sint-Camillus/Armonea/SLG/emeis/Korian"
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
                    "Rusthuis Sint Jozef Ninove omzet JUMP 11.90m / pnl DROP −78.1% "
                    "(YE2025)"
                ),
                "level": "L5",
                "type": "wzc_statutory_bv",
                "hierarchy_path": (
                    "Vlaanderen>OostVlaanderen>Ninove>Rusthuis_Sint_Jozef>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +2.66% (primary); bruto {BRUTO} JUMP "
                    f"+1.71%; pnl {PNL} DROP −78.10%; equity {EQUITY} JUMP +1.15% thin "
                    f"vs omzet; FTE {FTE} JUMP vs {FTE_PRIOR}; assets/debt Unknown "
                    "pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_sint_jozef_ninove_jr2025_cw_en",
                "beneficiaries": "WZC residents / care users Ninove (2 VE)",
                "stated_goal": "Public-interest nursing-home care (Wilgendries path)",
                "measured_outcome": (
                    "omzet JUMP +2.66%; bruto JUMP +1.71%; pnl DROP −78.10%; "
                    f"equity JUMP +1.15% thin; FTE JUMP {FTE}"
                ),
                "absurdity_score": "5.5",
                "cost_score": "5.5",
                "difficulty": "3.5",
                "priority_index": "5.6",
                "cut_proposal": (
                    "FOI NBB PDF + care/toelage split + explain pnl DROP −78.1% with "
                    "omzet JUMP; map 2 VE + public subsidy exposure"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; EVERY-10@2110; preferred "
                    "FARO/AIESH/REW still YE2024; DISTINCT Zilverlinde/Sint-Camillus/"
                    "Armonea/SLG/emeis"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>OostVlaanderen>Ninove>Rusthuis_Sint_Jozef>"
            "NBB_PDF_assets_debt_pnl_drop_omzet_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP path; "
            "omzet care/toelage split; 2 VE matrix; public subsidy matrix"
        ),
        "why_it_matters": (
            "Medium CW shows 11.90m omzet Ninove WZC BV with pnl DROP −78.10% to "
            "0.21m while omzet JUMP +2.66% and equity thin 0.86m — care-margin "
            "transparency gap"
        ),
        "priority": "8",
        "recipient_body": "Rusthuis Sint Jozef BV / WZC Wilgendries",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; EVERY-10; next every-10 2120",
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
