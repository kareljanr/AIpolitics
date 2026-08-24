# -*- coding: utf-8 -*-
"""Apply tick 2118 — Entraide Fraternelle Jolimont YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFT = ROOT / "foi" / "drafts"
csv.field_size_limit(10**7)

UTC = "2026-08-25T09:55:00Z"
TICK = 2118
RQ = "rq_2118"
NEXT_RQ = "rq_2119"
ENTITY = "asbl_entraide_fraternelle_jolimont"
GAP = "gap_entraide_jolimont_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
KBO = "0407.699.017"
KBO_DIGITS = "0407699017"
OMZET = 28734828
BRUTO = 31503767
PNL = 1703142
EQUITY = 32305838
FTE = 372.8
OMZET_PRIOR = 27780747
PNL_PRIOR = 2251893
BRUTO_PRIOR = 30821763
EQUITY_PRIOR = 29212613
EMAIL = "secretariat.general@jolimont.be"
ADDR = "Rue Ferrer(PAU) 159, 7100 La Louvière"
WEBSITE = "https://jolimont.be/maisons-de-repos"
LB = "lb_entraide_jolimont_omzet_28_73m_pnl_drop_jr2025"
COMM = "comm_entraide_jolimont_jr2025_statutory_mrs"
SLUG = "asbl-entraide-fraternelle-jolimont"

DO_NOT_REDO = (
    "Do NOT redo Entraide Fraternelle Jolimont, La Charmille Pont-à-Celles, "
    "Residence Les Charmilles Sambreville, Les Sittelles Chastre, Les Buissons "
    "/ Château Sous Bois Spa, Résidence 3 / Saphir, Elisabeth Aan Zee Oostende, "
    "Maison de Repos du XXe Août / PLIMCO, Rusthuis Sint Jozef Ninove, WZC "
    "Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX "
    "Développement, IDELUX Projets Publics, IDELUX Eau, INTRADEL, Korian "
    "Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, "
    "SLG Operaties, AREWAL, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, "
    "Synergrid, Atrias, Synatom, IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, "
    "SWDE, AGB Bornem, Armonea, emeis."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief "
        f"VZW/ASBL 6 VE NACE 87.101/87.301 RVT+ROB (La Louvière Pôle Senior); "
        f"omzet JUMP {OMZET/1e6:.2f}m (+3.43%) bruto JUMP {BRUTO/1e6:.2f}m "
        f"(+2.21%) pnl DROP {PNL} (−24.37% vs YE2024 {PNL_PRIOR}) equity JUMP "
        f"{EQUITY/1e6:.2f}m (+10.59%) FTE {FTE} (YoY Unknown); assets/debt "
        f"Unknown; neerlegging 10.07.2026; FOI {GAP}; Aanbestedende overheid; "
        f"dual La Charmille ASBL; preferred AGB Bornem JR2024; "
        f"FARO/AIESH/REW YE2024"
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
                "name_nl": "Entraide Fraternelle Jolimont (La Louvière)",
                "name_fr": "ASBL Entraide Fraternelle Jolimont (La Louvière)",
                "name_en": (
                    "Entraide Fraternelle Jolimont nursing-home ASBL "
                    "(La Louvière; Jolimont Pôle Senior)"
                ),
                "level": "other",
                "parent_id": "sec_wallonia",
                "community_language": "fr",
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
                "leftover dual — Entraide Fraternelle Jolimont YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover Entraide Fraternelle Jolimont YE2025 "
                f"Medium CW; KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} "
                f"pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}; "
                f"6 VE NACE 87.101/87.301 Jolimont; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Entraide Jolimont Medium omzet JUMP "
                f"{OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl DROP "
                f"{PNL/1e6:.2f}m (−24%) equity JUMP {EQUITY/1e6:.2f}m FTE "
                f"{FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    "leftover dual hole-fill after Entraide Jolimont — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Entraide Fraternelle Jolimont "
                    "YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF "
                    "live, else FARO if TRUE NBB YE2025, else AIESH/REW if "
                    "YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/"
                    "WZC/psych/MRS. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Entraide Jolimont; "
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
                    f"tick{TICK} leftover Entraide Fraternelle Jolimont {KBO} "
                    f"Medium CW (omzet JUMP {OMZET/1e6:.2f}m bruto JUMP "
                    f"{BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP "
                    f"{EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; 6 VE "
                    f"NACE 87.101/87.301 Jolimont); AGB Bornem JR2024; "
                    f"FARO/AIESH/REW YE2024; La Charmille/Les Charmilles/"
                    f"Sittelles/Buissons/Résidence 3 taken; next {NEXT_RQ}; "
                    f"next every-10 2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Entraide Fraternelle Jolimont (omzet JUMP 28.73m / pnl DROP 1.70m −24% / Medium)

- Unit: **{RQ}** leftover dual after **rq_2117 La Charmille Pont-à-Celles**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Entraide Fraternelle Jolimont** YE2025 (KBO **{KBO}**; Rue Ferrer(PAU) 159 La Louvière; **VZW/ASBL** NACE **87.101/87.301** / **6 VE**; **Groupe Jolimont** Pôle Senior multi-site; Aanbestedende overheid). Do not redo La Charmille/Les Charmilles Sambreville/Les Sittelles/Les Buissons/Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +3.43%; bruto **EUR{BRUTO}** JUMP +2.21%; pnl **EUR{PNL}** DROP −24.37% vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** JUMP +10.59% vs YE2024 EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **10.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.2); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2118/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")


def main():
    draft = FOI_DRAFT / f"{GAP}.md"
    if not draft.exists():
        raise SystemExit(f"missing FOI draft {draft}")

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
                "source_id": "src_entraide_jolimont_jr2025_cw_nl",
                "title": "Companyweb NL — Entraide Fraternelle Jolimont YE2025",
                "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; Medium CW; omzet {OMZET} bruto {BRUTO} pnl "
                    f"{PNL} FTE {FTE}"
                ),
            },
            {
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "title": "Companyweb EN — Entraide Fraternelle Jolimont YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 10.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_entraide_jolimont_jr2025_cw_fr",
                "title": "Companyweb FR — Entraide Fraternelle Jolimont YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_entraide_jolimont_kbo_{TICK}",
                "title": f"KBO — Entraide Fraternelle Jolimont {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief VZW 6 VE; NACE 87.101/87.301; zetel "
                    f"{ADDR}; Aanbestedende overheid; FOI {EMAIL}; Strong"
                ),
            },
            {
                "source_id": f"src_entraide_jolimont_contact_{TICK}",
                "title": "Entraide Fraternelle Jolimont / Jolimont FOI contact",
                "url": WEBSITE,
                "publisher": "Groupe Jolimont",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; postal {ADDR}; site {WEBSITE}; "
                    "AVIQ multi-site Pôle Senior"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_entraide_jolimont_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS ASBL)",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +3.43% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_entraide_jolimont_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +2.21% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_entraide_jolimont_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −24.37% vs YE2024 {PNL_PRIOR}",
            },
            {
                "budget_id": "bud_entraide_jolimont_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +10.59% vs YE2024 {EQUITY_PRIOR}",
            },
            {
                "budget_id": "bud_entraide_jolimont_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE {FTE} (YoY Unknown)",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "Entraide Fraternelle Jolimont YE2025 leftover dual "
                    "(omzet 28.73m / pnl DROP −24%)"
                ),
                "entity_id": ENTITY,
                "beneficiary": (
                    "MRS residents / care users Jolimont Pôle Senior multi-site "
                    "(6 VE)"
                ),
                "legal_basis": (
                    f"VZW/ASBL maisons de repos RVT/ROB (KBO {KBO}; NACE "
                    "87.101/87.301; 6 VE; Aanbestedende overheid; Jolimont)"
                ),
                "decision_date": "2026-07-10",
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
                    "Public-interest multi-site nursing-home care (Jolimont "
                    "Pôle Senior; AVIQ-subsidised)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl DROP −24% "
                    "at rising omzet; per-site AVIQ/INAMI vs omzet matrix; "
                    "dual La Charmille ASBL"
                ),
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>La_Louviere>Entraide_Jolimont>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; dual La Charmille ASBL"
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
                    "Entraide Jolimont omzet 28.73m / pnl DROP 1.70m −24% "
                    "(YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_asbl_jolimont_path",
                "hierarchy_path": "Wallonie>La_Louviere>Entraide_Jolimont>JR2025",
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +3.43% (primary); bruto "
                    f"{BRUTO} JUMP +2.21%; pnl {PNL} DROP −24.37% vs "
                    f"{PNL_PRIOR}; equity {EQUITY} JUMP +10.59%; FTE {FTE}; "
                    "assets/debt Unknown pending NBB PDF; 6 VE Jolimont"
                ),
                "confidence": "medium",
                "source_id": "src_entraide_jolimont_jr2025_cw_en",
                "beneficiaries": (
                    "MRS residents / care users Jolimont Pôle Senior (6 VE)"
                ),
                "stated_goal": (
                    "Public-interest multi-site nursing-home care (Jolimont "
                    "Pôle Senior)"
                ),
                "measured_outcome": (
                    "omzet JUMP +3.43%; bruto JUMP +2.21%; pnl DROP −24.37%; "
                    f"equity JUMP +10.59%; FTE {FTE}"
                ),
                "absurdity_score": "7.1",
                "cost_score": "7.0",
                "difficulty": "3.5",
                "priority_index": "6.2",
                "cut_proposal": (
                    "FOI NBB PDF + per-site AVIQ/INAMI split + explain pnl DROP "
                    "−24% at rising omzet; dual La Charmille"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; dual La Charmille ASBL"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>La_Louviere>Entraide_Jolimont>"
            "NBB_PDF_assets_debt_pnl_drop"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl DROP "
            "−24% path; per-site AVIQ/INAMI vs omzet matrix across 6 VE; dual "
            "La Charmille ASBL"
        ),
        "why_it_matters": (
            "Medium CW shows 28.73m omzet Jolimont multi-site MRS ASBL with pnl "
            "DROP −24% at rising omzet/equity — care-margin transparency gap "
            "on AVIQ-adjacent Aanbestedende overheid path"
        ),
        "priority": "8",
        "recipient_body": "ASBL Entraide Fraternelle Jolimont / Groupe Jolimont",
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
