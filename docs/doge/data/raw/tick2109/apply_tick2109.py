# -*- coding: utf-8 -*-
"""Apply tick 2109 — WZC Zilverlinde Olen YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T07:40:00Z"
TICK = 2109
RQ = "rq_2109"
NEXT_RQ = "rq_2110"
ENTITY = "vzw_wzc_zilverlinde_olen"
GAP = "gap_zilverlinde_olen_nbb_pdf_assets_debt_pnl_drop_omzet_jump_matrix_l5"
KBO = "0445.175.263"
KBO_DIGITS = "0445175263"
OMZET = 4928407
BRUTO = 4930500
PNL = 133746
EQUITY = 1314431
FTE = 54.5
OMZET_PRIOR = 4783776
PNL_PRIOR = 232907
BRUTO_PRIOR = 4934421
EQUITY_PRIOR = 1180685
EMAIL = "info@wzczilverlinde.be"
ADDR = "Berkenstraat 15, 2250 Olen"
WEBSITE = "https://www.wzczilverlinde.be"
LB = "lb_zilverlinde_olen_omzet_jump_4_93m_pnl_drop_jr2025"
COMM = "comm_zilverlinde_olen_jr2025_statutory_wzc"
SLUG = "wzc-zilverlinde"

DO_NOT_REDO = (
    "Do NOT redo WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, "
    "IDELUX Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, "
    "IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, "
    "SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, HYGEA, BEP Environnement, "
    "AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, "
    "IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, "
    "Colisée Belgium, Familiezorg Gent, emeis."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW 1 VE "
        f"NACE 87.101 RVT; omzet JUMP {OMZET/1e6:.2f}m (+3.02%) bruto FLAT/DROP "
        f"{BRUTO/1e6:.2f}m (−0.08%) pnl DROP {PNL/1e6:.2f}m (−42.58%) equity JUMP "
        f"{EQUITY/1e6:.2f}m (+11.33%) FTE {FTE} (YoY Unknown); assets/debt Unknown; "
        f"neerlegging 08.07.2026; FOI {GAP}; preferred AGB Bornem JR2024; "
        f"FARO/AIESH/REW YE2024; DISTINCT Sint-Camillus/Armonea/SLG/emeis/Korian"
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
                "name_nl": "WZC Zilverlinde (Olen)",
                "name_fr": "Maison de repos Zilverlinde (Olen)",
                "name_en": "Nursing home Zilverlinde Olen (VZW)",
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
            r["title"] = "leftover dual — WZC Zilverlinde Olen YE2025 Medium"
            r["instructions"] = (
                f"Completed leftover WZC Zilverlinde Olen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto FLAT {BRUTO} pnl DROP {PNL} "
                f"equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}; 1 VE; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Camillus taken"
            )
            r["notes"] = (
                f"tick{TICK} Zilverlinde Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto FLAT {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP "
                f"{EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; AGB Bornem JR2024; "
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
                    "EVERY-10 + leftover dual hole-fill after Zilverlinde — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC Sint-Jozef Ninove"
                ),
                "sprint": "hole_fill",
                "priority": "9",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} EVERY-10 after WZC Zilverlinde Olen YE2025 Medium. "
                    "MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md "
                    "then hole-fill one unit. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Rusthuis Sint Jozef "
                    "Ninove 0452.865.383 YE2025 BV optional if public-interest). "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Zilverlinde; EVERY-10 mandatory at 2110; "
                    "Sint-Jozef Ninove YE2025 deferred; FARO/AIESH/REW still YE2024"
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
                    f"tick{TICK} leftover WZC Zilverlinde Olen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto FLAT {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE {FTE}; assets/debt Unknown; 1 VE NACE 87.101); "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Camillus taken; "
                    f"next {NEXT_RQ} EVERY-10; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} WZC Zilverlinde Olen (omzet JUMP 4.93m / pnl DROP 0.13m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2108 WZC Sint-Camillus Wevelgem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred unused **WZC Zilverlinde Olen** YE2025 (KBO **{KBO}**; Berkenstraat 15 Olen; **VZW** NACE **87.101** / **1 VE**). Do not redo Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +3.02%; bruto **EUR{BRUTO}** DROP −0.08%; pnl **EUR{PNL}** DROP −42.58% vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP +11.33%; FTE **{FTE}** (YoY Unknown); neerlegging **08.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.9); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2109/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2100**; next **2110** MUST refresh progress + waste top10 then hole-fill). Next: {NEXT_RQ} (EVERY-10 + AGB/FARO-if-YE2025 / AIESH-REW / unused WZC Sint-Jozef Ninove deferred).
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
                "source_id": "src_zilverlinde_olen_jr2025_cw_nl",
                "title": "Companyweb NL — WZC Zilverlinde Olen YE2025",
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
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "title": "Companyweb EN — WZC Zilverlinde Olen YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 08.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_zilverlinde_olen_jr2025_cw_fr",
                "title": "Companyweb FR — WZC Zilverlinde Olen YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_zilverlinde_olen_kbo_{TICK}",
                "title": f"KBO — WZC Zilverlinde Olen {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 1 VE; NACE 87.101 RVT; zetel {ADDR}; "
                    f"email {EMAIL}; Strong identity"
                ),
            },
            {
                "source_id": f"src_zilverlinde_olen_contact_{TICK}",
                "title": "WZC Zilverlinde Olen FOI contact (gemeente + site)",
                "url": "https://www.olen.be/zilverlinde",
                "publisher": "Gemeente Olen / WZC Zilverlinde",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": f"tick{TICK}; {EMAIL}; tel 014/262620; {ADDR}; {WEBSITE}",
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_zilverlinde_olen_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope WZC VZW)",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +3.02% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_zilverlinde_olen_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −0.08% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_zilverlinde_olen_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −42.58% vs YE2024 {PNL_PRIOR}",
            },
            {
                "budget_id": "bud_zilverlinde_olen_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +11.33% vs YE2024 {EQUITY_PRIOR}",
            },
            {
                "budget_id": "bud_zilverlinde_olen_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE}; YoY Unknown (CW shows current only)",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "WZC Zilverlinde Olen YE2025 leftover dual "
                    "(omzet JUMP 4.93m / pnl DROP 0.13m)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "WZC residents / care users Olen",
                "legal_basis": (
                    f"VZW woonzorgcentrum RVT (KBO {KBO}; NACE 87.101; 1 VE)"
                ),
                "decision_date": "2026-07-08",
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
                "stated_goal": "Public-interest nursing-home care (WZC Zilverlinde)",
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl DROP −42.58% with "
                    "omzet JUMP +3.02%; map public care toelage vs private fee split"
                ),
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": "Vlaanderen>Antwerpen>Olen>WZC_Zilverlinde>JR2025_statutory_L5",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "DISTINCT Sint-Camillus/Armonea/SLG/emeis/Korian"
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
                    "WZC Zilverlinde Olen omzet JUMP 4.93m / pnl DROP −42.6% (YE2025)"
                ),
                "level": "L5",
                "type": "wzc_statutory_vzw",
                "hierarchy_path": "Vlaanderen>Antwerpen>Olen>WZC_Zilverlinde>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +3.02% (primary); bruto {BRUTO} DROP "
                    f"−0.08%; pnl {PNL} DROP −42.58%; equity {EQUITY} JUMP +11.33%; "
                    f"FTE {FTE} YoY Unknown; assets/debt Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_zilverlinde_olen_jr2025_cw_en",
                "beneficiaries": "WZC residents / care users Olen (1 VE)",
                "stated_goal": "Public-interest nursing-home care",
                "measured_outcome": (
                    "omzet JUMP +3.02%; bruto DROP −0.08%; pnl DROP −42.58%; "
                    f"equity JUMP +11.33%; FTE {FTE} YoY Unknown"
                ),
                "absurdity_score": "5.0",
                "cost_score": "4.0",
                "difficulty": "3.5",
                "priority_index": "4.9",
                "cut_proposal": (
                    "FOI NBB PDF + care/toelage split + explain pnl DROP with omzet JUMP; "
                    "map public subsidy exposure"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still "
                    "YE2024; DISTINCT Sint-Camillus/Armonea/SLG/emeis"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>Antwerpen>Olen>WZC_Zilverlinde>"
            "NBB_PDF_assets_debt_pnl_drop_omzet_jump"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP path; "
            "omzet care/toelage split; FTE YoY; public subsidy matrix"
        ),
        "why_it_matters": (
            "Medium CW shows 4.93m omzet Olen WZC VZW with pnl DROP −42.58% to "
            "0.13m while omzet JUMP +3.02% — care-margin transparency gap"
        ),
        "priority": "8",
        "recipient_body": "WZC Zilverlinde VZW",
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
