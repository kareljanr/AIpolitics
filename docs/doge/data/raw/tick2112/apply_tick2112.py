# -*- coding: utf-8 -*-
"""Apply tick 2112 — Elisabeth Aan Zee Oostende YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T08:25:00Z"
TICK = 2112
RQ = "rq_2112"
NEXT_RQ = "rq_2113"
ENTITY = "vzw_elisabeth_aan_zee_oostende"
GAP = "gap_elisabeth_aan_zee_nbb_pdf_assets_debt_pnl_flip_matrix_l5"
KBO = "0405.311.530"
KBO_DIGITS = "0405311530"
OMZET = 7721338
BRUTO = 7423006
PNL = 134982
EQUITY = 8790569
FTE = 96.0
OMZET_PRIOR = 7134669
PNL_PRIOR = -4249
BRUTO_PRIOR = 7068277
EQUITY_PRIOR = 8995611
EMAIL = "onthaalseo@gvo.be"
ADDR = "Zwaluwenstraat 2, 8400 Oostende"
WEBSITE = "https://www.elisabethaanzee.gvo.be/"
LB = "lb_elisabeth_aan_zee_omzet_jump_7_72m_pnl_flip_jr2025"
COMM = "comm_elisabeth_aan_zee_jr2025_statutory_wzc"
SLUG = "elisabeth-aan-zee"

DO_NOT_REDO = (
    "Do NOT redo Elisabeth Aan Zee Oostende, Maison de Repos du XXe Août / PLIMCO, "
    "Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus "
    "Wevelgem, IDELUX Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX "
    "Finances, IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, "
    "ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, HYGEA, BEP "
    "Environnement, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, "
    "Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Aquafin, "
    "AGB Bornem, Armonea, Colisée Belgium, Familiezorg Gent, emeis, IRE*, FANC, "
    "SCK CEN, Heilig Hart Grimbergen, Maria Moorslede, Ter Burg, Sint-Antonius, "
    "Huize Sint-Jozef Ieper, WZC Sint-Jozef Rumst."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief VZW "
        f"2 VE NACE 87.301 ROB; omzet JUMP {OMZET/1e6:.2f}m (+8.22%) bruto JUMP "
        f"{BRUTO/1e6:.2f}m (+5.02%) pnl FLIP {PNL/1e6:.2f}m vs YE2024 LOSS "
        f"{PNL_PRIOR} equity DROP {EQUITY/1e6:.2f}m (−2.28%) FTE {FTE}; "
        f"assets/debt Unknown; neerlegging 01.07.2026; FOI {GAP}; GVO path "
        f"onthaalseo@gvo.be; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        f"DISTINCT XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL"
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
                "name_nl": "Elisabeth Aan Zee (Oostende)",
                "name_fr": "Elisabeth Aan Zee (Ostende / ASBL MRS)",
                "name_en": "Elisabeth Aan Zee nursing home Oostende (VZW)",
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
                "leftover dual — Elisabeth Aan Zee Oostende YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover Elisabeth Aan Zee Oostende YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl FLIP {PNL} "
                f"equity DROP {EQUITY} FTE {FTE}; FOI {GAP}; 2 VE NACE 87.301; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Elisabeth Aan Zee Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl FLIP {PNL/1e6:.2f}m equity DROP "
                f"{EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2120"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Elisabeth Aan Zee — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Elisabeth Aan Zee YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
                    "NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/"
                    "IGS/HVZ/energy/hospital/WZC/psych/MRS. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Elisabeth Aan Zee; "
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
                    f"tick{TICK} leftover Elisabeth Aan Zee Oostende {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl "
                    f"FLIP {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; "
                    f"assets/debt Unknown; 2 VE NACE 87.301 GVO-path); AGB Bornem "
                    f"JR2024; FARO/AIESH/REW YE2024; XXe Août/Ninove/Zilverlinde/"
                    f"Sint-Camillus/IDELUX*/INTRADEL/ORES SC taken; next {NEXT_RQ}; "
                    f"next every-10 2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Elisabeth Aan Zee Oostende (omzet JUMP 7.72m / pnl FLIP 0.13m / Medium)

- Unit: **{RQ}** leftover dual after **rq_2111 Maison de Repos du XXe Août Herstal**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Elisabeth Aan Zee** YE2025 (KBO **{KBO}**; Zwaluwenstraat 2 Oostende; **VZW** NACE **87.301** / **2 VE**; GVO path). Do not redo XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +8.22%; bruto **EUR{BRUTO}** JUMP +5.02%; pnl **EUR{PNL}** FLIP vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** DROP −2.28% vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **01.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.4); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2112/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
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
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_nl",
                "title": "Companyweb NL — Elisabeth Aan Zee YE2025",
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
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "title": "Companyweb EN — Elisabeth Aan Zee YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 01.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_fr",
                "title": "Companyweb FR — Elisabeth Aan Zee YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_elisabeth_aan_zee_kbo_{TICK}",
                "title": f"KBO — Elisabeth Aan Zee {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 2 VE; NACE 87.301 ROB; zetel {ADDR}; "
                    f"FOI {EMAIL}; Strong identity"
                ),
            },
            {
                "source_id": f"src_elisabeth_aan_zee_contact_{TICK}",
                "title": "Elisabeth Aan Zee / GVO FOI contact",
                "url": WEBSITE,
                "publisher": "Elisabeth Aan Zee / GastVrij Omgeven",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; KBO email empty; postal {ADDR}; "
                    f"site {WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_elisabeth_aan_zee_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope WZC VZW)",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +8.22% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_elisabeth_aan_zee_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +5.02% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_elisabeth_aan_zee_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; FLIP vs YE2024 LOSS {PNL_PRIOR} (CW shows +1000% cap)"
                ),
            },
            {
                "budget_id": "bud_elisabeth_aan_zee_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −2.28% vs YE2024 {EQUITY_PRIOR}",
            },
            {
                "budget_id": "bud_elisabeth_aan_zee_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE}; YoY Unknown",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Elisabeth Aan Zee YE2025 leftover dual "
                    "(omzet JUMP 7.72m / pnl FLIP)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "WZC residents / care users Oostende (2 VE)",
                "legal_basis": (
                    f"VZW woonzorgcentrum ROB (KBO {KBO}; NACE 87.301; 2 VE)"
                ),
                "decision_date": "2026-07-01",
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
                    "Public-interest nursing-home care (Elisabeth Aan Zee / GVO path)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl FLIP from prior-year "
                    "loss; map IFIC/Alivia vs dagprijs split; 2 VE matrix"
                ),
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Vlaanderen>WestVlaanderen>Oostende>Elisabeth_Aan_Zee>"
                    "JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive "
                    "of 348bn; DISTINCT XXe Août/Ninove/Zilverlinde/Sint-Camillus"
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
                    "Elisabeth Aan Zee omzet JUMP 7.72m / pnl FLIP 0.13m (YE2025)"
                ),
                "level": "L5",
                "type": "wzc_statutory_vzw",
                "hierarchy_path": (
                    "Vlaanderen>WestVlaanderen>Oostende>Elisabeth_Aan_Zee>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +8.22% (primary); bruto {BRUTO} JUMP "
                    f"+5.02%; pnl {PNL} FLIP from LOSS {PNL_PRIOR}; equity {EQUITY} DROP "
                    f"−2.28%; FTE {FTE}; assets/debt Unknown pending NBB PDF; GVO path"
                ),
                "confidence": "medium",
                "source_id": "src_elisabeth_aan_zee_jr2025_cw_en",
                "beneficiaries": "WZC residents / care users Oostende (2 VE)",
                "stated_goal": "Public-interest nursing-home care (GVO path)",
                "measured_outcome": (
                    "omzet JUMP +8.22%; bruto JUMP +5.02%; pnl FLIP from LOSS; "
                    f"equity DROP −2.28%; FTE {FTE}"
                ),
                "absurdity_score": "5.5",
                "cost_score": "5.2",
                "difficulty": "3.5",
                "priority_index": "5.4",
                "cut_proposal": (
                    "FOI NBB PDF + care/toelage split + explain pnl FLIP from prior "
                    "loss; map 2 VE (Sint-Elisabeth + Residentie Coost)"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still "
                    "YE2024; DISTINCT XXe Août/Ninove/Zilverlinde/Sint-Camillus"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>WestVlaanderen>Oostende>Elisabeth_Aan_Zee>"
            "NBB_PDF_assets_debt_pnl_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl FLIP path; "
            "omzet care/toelage split; 2 VE matrix (Sint-Elisabeth + Residentie Coost)"
        ),
        "why_it_matters": (
            "Medium CW shows 7.72m omzet Oostende WZC VZW with pnl FLIP to 0.13m from "
            "prior-year loss and equity DROP −2.28% — care-margin transparency gap"
        ),
        "priority": "8",
        "recipient_body": "Elisabeth Aan Zee vzw / GastVrij Omgeven",
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
        "notes": f"tick{TICK}; human-send only; Medium CW; next every-10 2120",
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
