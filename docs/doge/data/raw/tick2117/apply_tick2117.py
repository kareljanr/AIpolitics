# -*- coding: utf-8 -*-
"""Apply tick 2117 — La Charmille Pont-à-Celles YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T09:40:00Z"
TICK = 2117
RQ = "rq_2117"
NEXT_RQ = "rq_2118"
ENTITY = "asbl_la_charmille_pont_a_celles"
GAP = "gap_la_charmille_pac_nbb_pdf_assets_debt_pnl_loss_equity_flip_matrix_l5"
KBO = "0416.116.637"
KBO_DIGITS = "0416116637"
OMZET = 4199544
BRUTO = 4627753
PNL = -185148
EQUITY = 66812
FTE = 67.2
OMZET_PRIOR = 4181158
PNL_PRIOR = -186552
BRUTO_PRIOR = 4640085
EQUITY_PRIOR = -186015
FTE_PRIOR = 69.7
EMAIL = "lacharmille@jolimont.be"
EMAIL_ALT = "secretariat.general@jolimont.be"
ADDR = "Rue des Vignobles 2, 6230 Pont-à-Celles"
WEBSITE = "https://jolimont.be/maisons-de-repos"
LB = "lb_la_charmille_pac_omzet_4_20m_pnl_loss_equity_flip_jr2025"
COMM = "comm_la_charmille_pac_jr2025_statutory_mrs"
SLUG = "la-charmille"

DO_NOT_REDO = (
    "Do NOT redo La Charmille Pont-à-Celles, Residence Les Charmilles Sambreville, "
    "Les Sittelles Chastre, Les Buissons / Château Sous Bois Spa, Résidence 3 / Saphir, "
    "Elisabeth Aan Zee Oostende, Maison de Repos du XXe Août / PLIMCO, Rusthuis Sint Jozef "
    "Ninove, WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX "
    "Développement, IDELUX Projets Publics, IDELUX Eau, INTRADEL, Korian Belgium, "
    "Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG Operaties, "
    "AREWAL, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, "
    "IPFBW, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, AGB Bornem, Armonea, emeis."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief ASBL 1 VE "
        f"NACE 87.301 ROB/MRPA Jolimont Pôle Senior AViQ-path; omzet FLAT "
        f"{OMZET/1e6:.2f}m (+0.44%) bruto FLAT {BRUTO/1e6:.2f}m (−0.27%) pnl LOSS "
        f"{PNL/1e6:.2f}m NARROW vs {PNL_PRIOR} equity FLIP {EQUITY/1e6:.3f}m from NEG "
        f"{EQUITY_PRIOR} FTE DROP {FTE} (vs {FTE_PRIOR}); assets/debt Unknown; "
        f"filed 10.07.2026; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW "
        f"YE2024; DISTINCT Les Charmilles Sambreville"
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
                "name_nl": "La Charmille (Pont-à-Celles)",
                "name_fr": "La Charmille ASBL (Pont-à-Celles / Thiméon)",
                "name_en": "Nursing home La Charmille Pont-à-Celles (ASBL)",
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
                "leftover dual — La Charmille Pont-à-Celles YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover La Charmille Pont-à-Celles YE2025 Medium CW; "
                f"KBO {KBO}; omzet FLAT {OMZET} bruto FLAT {BRUTO} pnl LOSS {PNL} "
                f"equity FLIP {EQUITY} FTE {FTE}; FOI {GAP}; 1 VE NACE 87.301 "
                f"Jolimont; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Charmilles "
                f"Sambreville taken"
            )
            r["notes"] = (
                f"tick{TICK} La Charmille Medium omzet FLAT {OMZET/1e6:.2f}m bruto "
                f"FLAT {BRUTO/1e6:.2f}m pnl LOSS {PNL/1e6:.2f}m equity FLIP "
                f"{EQUITY/1e6:.3f}m FTE {FTE}; FOI ready; next {NEXT_RQ}; "
                f"next every-10 2120"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after La Charmille — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after La Charmille Pont-à-Celles YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
                    "NBB YE2025, else AIESH/REW if YE2025, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} La Charmille; FARO/AIESH/REW still "
                    "YE2024; next every-10 2120"
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
                    f"tick{TICK} leftover La Charmille Pont-à-Celles {KBO} Medium CW "
                    f"(omzet FLAT {OMZET/1e6:.2f}m bruto FLAT {BRUTO/1e6:.2f}m "
                    f"pnl LOSS {PNL/1e6:.2f}m equity FLIP {EQUITY/1e6:.3f}m "
                    f"FTE {FTE}; assets/debt Unknown; 1 VE NACE 87.301 Jolimont); "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Charmilles Sambreville "
                    f"taken; next {NEXT_RQ}; next every-10 2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} La Charmille Pont-à-Celles (omzet FLAT 4.20m / pnl LOSS −0.19m / equity FLIP / Medium)

- Unit: **{RQ}** leftover dual after **rq_2116 Residence Les Charmilles Sambreville**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred unused **La Charmille Pont-à-Celles / Thiméon** YE2025 (KBO **{KBO}**; Rue des Vignobles 2; **ASBL** NACE **87.301** / **1 VE**; Jolimont Pôle Senior AViQ-path). Do not redo Charmilles Sambreville/Sittelles/Buissons/Résidence 3/Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** FLAT +0.44%; bruto **EUR{BRUTO}** FLAT −0.27%; pnl **EUR{PNL}** LOSS NARROW vs YE2024 EUR{PNL_PRIOR}; equity **EUR{EQUITY}** FLIP from NEG EUR{EQUITY_PRIOR}; FTE **{FTE}** DROP vs {FTE_PRIOR}; filed **10.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL} / {EMAIL_ALT}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 4.7); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2117/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (last **2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
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
                "source_id": "src_la_charmille_pac_jr2025_cw_nl",
                "title": "Companyweb NL — La Charmille Pont-à-Celles YE2025",
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
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "title": "Companyweb EN — La Charmille Pont-à-Celles YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 10.07.2026; equity {EQUITY} FLIP; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_la_charmille_pac_jr2025_cw_fr",
                "title": "Companyweb FR — La Charmille Pont-à-Celles YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_la_charmille_pac_kbo_{TICK}",
                "title": f"KBO — La Charmille Pont-à-Celles {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief ASBL 1 VE; NACE 87.301; zetel {ADDR}; "
                    f"email {EMAIL_ALT}; Strong identity"
                ),
            },
            {
                "source_id": f"src_la_charmille_pac_contact_{TICK}",
                "title": "Jolimont / La Charmille FOI contact",
                "url": WEBSITE,
                "publisher": "Groupe Jolimont Pôle Senior",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL} / {EMAIL_ALT}; tel 071 34 10 12; {ADDR}; "
                    "AViQ-subsidised MRS"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_la_charmille_pac_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS ASBL)",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLAT +0.44% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_la_charmille_pac_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FLAT −0.27% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_la_charmille_pac_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; LOSS NARROW vs YE2024 {PNL_PRIOR}",
            },
            {
                "budget_id": "bud_la_charmille_pac_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; FLIP from NEG {EQUITY_PRIOR} to {EQUITY} (+135.92%)"
                ),
            },
            {
                "budget_id": "bud_la_charmille_pac_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; FTE DROP {FTE} vs YE2024 {FTE_PRIOR}",
            },
        ],
    )
    append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": (
                    "La Charmille Pont-à-Celles YE2025 leftover dual "
                    "(omzet FLAT 4.20m / pnl LOSS / equity FLIP)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "MRS residents Pont-à-Celles / Thiméon (Jolimont)",
                "legal_basis": (
                    f"ASBL maison de repos ROB/MRPA (KBO {KBO}; NACE 87.301; 1 VE; "
                    "AViQ-agréée)"
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
                    "Public-interest nursing-home care (La Charmille / Jolimont)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain chronic LOSS + equity "
                    "FLIP; map AViQ/INAMI toelage vs private fee split; Jolimont "
                    "group matrix"
                ),
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>Hainaut>PontACelles>La_Charmille>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; DISTINCT Les Charmilles Sambreville"
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
                    "La Charmille Pont-à-Celles omzet 4.20m / pnl LOSS / equity FLIP "
                    "(YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_asbl",
                "hierarchy_path": (
                    "Wallonie>Hainaut>PontACelles>La_Charmille>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} FLAT +0.44% (primary); bruto {BRUTO} "
                    f"FLAT −0.27%; pnl {PNL} LOSS NARROW; equity {EQUITY} FLIP from "
                    f"NEG {EQUITY_PRIOR}; FTE {FTE} DROP vs {FTE_PRIOR}; assets/debt "
                    "Unknown pending NBB PDF"
                ),
                "confidence": "medium",
                "source_id": "src_la_charmille_pac_jr2025_cw_en",
                "beneficiaries": "MRS residents Pont-à-Celles (1 VE Jolimont)",
                "stated_goal": "Public-interest nursing-home care (AViQ-path)",
                "measured_outcome": (
                    "omzet FLAT +0.44%; bruto FLAT −0.27%; pnl LOSS NARROW; "
                    f"equity FLIP to {EQUITY}; FTE DROP {FTE}"
                ),
                "absurdity_score": "6.0",
                "cost_score": "3.5",
                "difficulty": "3.5",
                "priority_index": "4.7",
                "cut_proposal": (
                    "FOI NBB PDF + AViQ/INAMI split + explain chronic LOSS with "
                    "equity FLIP; Jolimont 8-MRS continuum transparency"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW "
                    "still YE2024; DISTINCT Les Charmilles Sambreville"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Hainaut>PontACelles>La_Charmille>"
            "NBB_PDF_assets_debt_pnl_loss_equity_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS path; "
            "equity FLIP path; AViQ/INAMI toelage split; Jolimont group matrix"
        ),
        "why_it_matters": (
            "Medium CW shows 4.20m omzet Pont-à-Celles MRS ASBL with chronic LOSS "
            "−0.19m and equity FLIP from NEG −0.19m to thin +0.07m — care-margin + "
            "continuity transparency gap on AViQ-path Jolimont shell"
        ),
        "priority": "8",
        "recipient_body": "ASBL La Charmille / Groupe Jolimont",
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
        "notes": (
            f"tick{TICK}; human-send only; Medium CW; alt {EMAIL_ALT}; "
            "next every-10 2120"
        ),
    }
    append_rows(DATA / "foi_queue.csv", [foi_row])
    close_queue()
    write_loop_state()
    append_log()
    print("DONE tick", TICK)


if __name__ == "__main__":
    main()
