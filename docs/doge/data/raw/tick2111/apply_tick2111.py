# -*- coding: utf-8 -*-
"""Apply tick 2111 — Maison de Repos du XXe Août YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T08:10:00Z"
TICK = 2111
RQ = "rq_2111"
NEXT_RQ = "rq_2112"
ENTITY = "nv_mrs_xxe_aout_herstal"
GAP = "gap_xxe_aout_nbb_pdf_assets_debt_pnl_flip_equity_flip_matrix_l5"
KBO = "0443.082.637"
KBO_DIGITS = "0443082637"
OMZET = 10949029
BRUTO = 8984821
PNL = 179756
EQUITY = 148177
FTE = 126.7
OMZET_PRIOR = 10741350
PNL_PRIOR = -54372
BRUTO_PRIOR = 8353352
EQUITY_PRIOR = -31579
EMAIL = "info@korian.be"
ADDR = "Chaussée Brunehault 404, 4041 Herstal"
WEBSITE = "https://www.korian.be/"
LB = "lb_xxe_aout_omzet_jump_10_95m_pnl_flip_equity_flip_jr2025"
COMM = "comm_xxe_aout_jr2025_statutory_mrs"
SLUG = "maison-de-repos-du-xxe-aout"

DO_NOT_REDO = (
    "Do NOT redo Maison de Repos du XXe Août / PLIMCO, Rusthuis Sint Jozef Ninove, "
    "WZC Zilverlinde Olen, Woonzorgcentrum Sint-Camillus Wevelgem, "
    "IDELUX Développement, IDELUX Projets Publics, IDELUX Eau, IDELUX Finances, "
    "IDELUX Environnement, INTRADEL, Korian Belgium, Comnexio, ORES SC, ORES Assets, "
    "SLG Vlaanderen, Always Home, SLG Operaties, AREWAL, HYGEA, BEP Environnement, "
    "AIEG, RESA, Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, "
    "IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, CILE, SWDE, Aquafin, AGB Bornem, "
    "Armonea, Colisée Belgium, Familiezorg Gent, emeis, IRE*, FANC, SCK CEN, "
    "EURIDICE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, WZC Sint-Jozef Rumst, "
    "Huize Sint-Jozef Ieper."
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
        f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO {KBO} Actief NV/SA "
        f"3 VE NACE 87.101 RVT + 87.301 ROB; omzet JUMP {OMZET/1e6:.2f}m (+1.93%) "
        f"bruto JUMP {BRUTO/1e6:.2f}m (+7.56%) pnl FLIP {PNL/1e6:.2f}m (+430.61% vs "
        f"YE2024 LOSS {PNL_PRIOR}) equity FLIP {EQUITY/1e6:.2f}m (+569.22% vs YE2024 "
        f"NEG {EQUITY_PRIOR}) FTE {FTE}; assets/debt Unknown; neerlegging 28.07.2026; "
        f"FOI {GAP}; bestuurder Korian Belgium 0869.769.702; preferred AGB Bornem "
        f"JR2024; FARO/AIESH/REW YE2024; DISTINCT Korian holding/SLG*/Always Home/"
        f"Ninove/Zilverlinde/Sint-Camillus"
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
                "name_nl": "Maison de Repos du XXe Août (Herstal)",
                "name_fr": "Maison de Repos du XXe Août (Herstal / PLIMCO)",
                "name_en": "Nursing home Maison de Repos du XXe Août Herstal (NV/SA)",
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
                "leftover dual — Maison de Repos du XXe Août Herstal YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover MRS XXe Août Herstal YE2025 Medium CW; KBO {KBO}; "
                f"omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl FLIP {PNL} equity FLIP "
                f"{EQUITY} FTE {FTE}; FOI {GAP}; 3 VE NACE 87.101/87.301; Korian-path; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} XXe Août Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP "
                f"{BRUTO/1e6:.2f}m pnl FLIP {PNL/1e6:.2f}m equity FLIP {EQUITY/1e6:.2f}m "
                f"FTE {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
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
                    "leftover dual hole-fill after XXe Août — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Maison de Repos du XXe Août YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB "
                    "YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/"
                    "energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} XXe Août; "
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
                    f"tick{TICK} leftover MRS XXe Août Herstal {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl "
                    f"FLIP {PNL/1e6:.2f}m equity FLIP {EQUITY/1e6:.2f}m FTE {FTE}; "
                    f"assets/debt Unknown; 3 VE NACE 87.101/87.301 Korian-path); "
                    f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ninove/"
                    f"Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian "
                    f"holding taken; next {NEXT_RQ}; next every-10 2120; "
                    f"continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Maison de Repos du XXe Août (omzet JUMP 10.95m / pnl FLIP 0.18m / equity FLIP / Medium)

- Unit: **{RQ}** leftover dual after **rq_2110 Rusthuis Sint Jozef Ninove**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Maison de Repos du XXe Août / PLIMCO** YE2025 (KBO **{KBO}**; Chaussée Brunehault 404 Herstal; **NV/SA** NACE **87.101/87.301** / **3 VE**; Korian Belgium bestuurder path). Do not redo Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +1.93%; bruto **EUR{BRUTO}** JUMP +7.56%; pnl **EUR{PNL}** FLIP +430.61% vs YE2024 LOSS EUR{PNL_PRIOR}; equity **EUR{EQUITY}** FLIP +569.22% vs YE2024 NEG EUR{EQUITY_PRIOR}; FTE **{FTE}** (YoY Unknown); neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL} (parent) + postal.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.9); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2111/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC).
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
                "source_id": "src_xxe_aout_jr2025_cw_nl",
                "title": "Companyweb NL — Maison de Repos du XXe Août YE2025",
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
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "title": "Companyweb EN — Maison de Repos du XXe Août YE2025",
                "url": f"https://www.companyweb.be/en/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": (
                    f"tick{TICK}; filed 28.07.2026; equity {EQUITY}; FTE {FTE}; "
                    "last BS year 2025"
                ),
            },
            {
                "source_id": "src_xxe_aout_jr2025_cw_fr",
                "title": "Companyweb FR — Maison de Repos du XXe Août YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_xxe_aout_kbo_{TICK}",
                "title": f"KBO — Maison de Repos du XXe Août {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV/SA 3 VE; NACE 87.101/87.301; zetel {ADDR}; "
                    f"bestuurder Korian Belgium 0869.769.702; FOI {EMAIL}; Strong identity"
                ),
            },
            {
                "source_id": f"src_xxe_aout_contact_{TICK}",
                "title": "Korian Belgium FOI contact for XXe Août MRS",
                "url": WEBSITE,
                "publisher": "Korian Belgium / Maison de Repos du XXe Août",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; KBO email empty; postal {ADDR}; "
                    f"parent site {WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_xxe_aout_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS NV)",
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +1.93% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_xxe_aout_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +7.56% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_xxe_aout_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; FLIP +430.61% vs YE2024 LOSS {PNL_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_xxe_aout_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; FLIP +569.22% vs YE2024 NEG {EQUITY_PRIOR}; thin vs omzet"
                ),
            },
            {
                "budget_id": "bud_xxe_aout_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_xxe_aout_jr2025_cw_en",
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
                    "Maison de Repos du XXe Août YE2025 leftover dual "
                    "(omzet JUMP 10.95m / pnl+equity FLIP)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "MRS residents / care users Herstal (3 VE)",
                "legal_basis": (
                    f"NV/SA maison de repos RVT/ROB (KBO {KBO}; NACE 87.101/87.301; 3 VE)"
                ),
                "decision_date": "2026-07-28",
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
                    "Public-interest nursing-home care (XXe Août / Korian-path MRS)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain pnl+equity FLIP from "
                    "prior-year loss/negative equity; map INAMI/AViQ vs private fee "
                    "split; 3 VE + Korian holding dual transparency"
                ),
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Wallonie>Liege>Herstal>MRS_XXe_Aout>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt Unknown; "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                    "DISTINCT Korian holding/SLG*/Ninove/Zilverlinde/Sint-Camillus"
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
                    "MRS XXe Août Herstal omzet JUMP 10.95m / pnl+equity FLIP "
                    "(YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_nv",
                "hierarchy_path": (
                    "Wallonie>Liege>Herstal>MRS_XXe_Aout>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +1.93% (primary); bruto {BRUTO} JUMP "
                    f"+7.56%; pnl {PNL} FLIP from LOSS {PNL_PRIOR}; equity {EQUITY} FLIP "
                    f"from NEG {EQUITY_PRIOR}; FTE {FTE}; assets/debt Unknown pending "
                    "NBB PDF; Korian Belgium bestuurder dual"
                ),
                "confidence": "medium",
                "source_id": "src_xxe_aout_jr2025_cw_en",
                "beneficiaries": "MRS residents / care users Herstal (3 VE)",
                "stated_goal": "Public-interest nursing-home care (Korian-path)",
                "measured_outcome": (
                    "omzet JUMP +1.93%; bruto JUMP +7.56%; pnl FLIP +430.61%; "
                    f"equity FLIP +569.22%; FTE {FTE}"
                ),
                "absurdity_score": "6.0",
                "cost_score": "5.5",
                "difficulty": "3.5",
                "priority_index": "5.9",
                "cut_proposal": (
                    "FOI NBB PDF + care/toelage split + explain pnl+equity FLIP from "
                    "prior loss/negative equity; map 3 VE + Korian holding dual"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still "
                    "YE2024; DISTINCT Korian holding/SLG*/Ninove/Zilverlinde/Sint-Camillus"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Liege>Herstal>MRS_XXe_Aout>"
            "NBB_PDF_assets_debt_pnl_flip_equity_flip"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl+equity FLIP "
            "path; omzet care/toelage split; 3 VE matrix; Korian holding dual matrix"
        ),
        "why_it_matters": (
            "Medium CW shows 10.95m omzet Herstal MRS NV with pnl FLIP to 0.18m "
            "(+430%) and equity FLIP to 0.15m (+569%) from prior-year loss/negative "
            "equity — care-margin + solvency transparency gap under Korian path"
        ),
        "priority": "8",
        "recipient_body": "Maison de Repos du XXe Août NV / Korian Belgium",
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
