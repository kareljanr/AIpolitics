# -*- coding: utf-8 -*-
"""Apply tick 2113 — Résidence 3 (Saphir/Korian) YE2025 Medium leftover dual."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T08:40:00Z"
TICK = 2113
RQ = "rq_2113"
NEXT_RQ = "rq_2114"
ENTITY = "nv_residence_3_bruxelles"
GAP = "gap_residence_3_nbb_pdf_assets_debt_pnl_loss_narrow_neg_equity_matrix_l5"
KBO = "0412.640.671"
KBO_DIGITS = "0412640671"
OMZET = 7437576
BRUTO = 4217863
PNL = -754218
EQUITY = -2506120
FTE = 90.4
OMZET_PRIOR = 5957434
PNL_PRIOR = -1208632
BRUTO_PRIOR = 4471125
EQUITY_PRIOR = -1751903
FTE_PRIOR = 78.7
EMAIL = "info@korian.be"
EMAIL_ALT = "info@saphir.be"
ADDR = "Eliane Vogel-Polskystraat 20, 1020 Brussel"
WEBSITE = "https://www.korian.be/fr/residences-services/saphir-assistentiewoning-fr/"
LB = "lb_residence_3_omzet_jump_7_44m_pnl_loss_narrow_neg_equity_jr2025"
COMM = "comm_residence_3_jr2025_statutory_mrs"
SLUG = "residence-3"

DO_NOT_REDO = (
    "Do NOT redo Résidence 3 / Saphir, Elisabeth Aan Zee Oostende, Maison de Repos "
    "du XXe Août / PLIMCO, Rusthuis Sint Jozef Ninove, WZC Zilverlinde Olen, "
    "Woonzorgcentrum Sint-Camillus Wevelgem, IDELUX Développement, IDELUX Projets "
    "Publics, IDELUX Eau, IDELUX Finances, IDELUX Environnement, INTRADEL, Korian "
    "Belgium, Comnexio, ORES SC, ORES Assets, SLG Vlaanderen, Always Home, SLG "
    "Operaties, AREWAL, HYGEA, BEP Environnement, AIEG, RESA, Enodia, Fluxys*, "
    "ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, "
    "Vivaqua, Hydria, CILE, SWDE, Aquafin, AGB Bornem, Armonea, Colisée Belgium, "
    "Familiezorg Gent, emeis, IRE*, FANC, SCK CEN, Veilige Have, Molenheide, "
    "WZC Sint-Jozef Rumst, Cassiers, OLV Roosdaal, De Verlosser Dilbeek."
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
        f"2 VE NACE 87.101/87.301 RVT+ROB; omzet JUMP {OMZET/1e6:.2f}m (+24.85%) "
        f"bruto DROP {BRUTO/1e6:.2f}m (−5.66%) pnl LOSS NARROW {PNL/1e6:.2f}m "
        f"(+37.6% vs YE2024 LOSS {PNL_PRIOR}) equity NEG DROP {EQUITY/1e6:.2f}m "
        f"(−43.05%) FTE JUMP {FTE} (was {FTE_PRIOR}); assets/debt Unknown; "
        f"neerlegging 28.07.2026; FOI {GAP}; Korian Belgium bestuurder "
        f"0869.769.702 path (Saphir Laeken + Palmboomstraat Woluwe); preferred "
        f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; DISTINCT Elisabeth Aan Zee/"
        f"XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL"
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
                "name_nl": "Résidence 3 (Brussel / Saphir Laeken)",
                "name_fr": "Résidence 3 SA (Bruxelles / Saphir Laeken)",
                "name_en": "Résidence 3 nursing home Brussels (NV/SA; Korian path)",
                "level": "other",
                "parent_id": "sec_brussels",
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
                "leftover dual — Résidence 3 Bruxelles YE2025 Medium"
            )
            r["instructions"] = (
                f"Completed leftover Résidence 3 Bruxelles YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto DROP {BRUTO} pnl LOSS NARROW "
                f"{PNL} equity NEG DROP {EQUITY} FTE JUMP {FTE}; FOI {GAP}; "
                f"2 VE NACE 87.101/87.301 Korian path; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Résidence 3 Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto DROP {BRUTO/1e6:.2f}m pnl LOSS NARROW {PNL/1e6:.2f}m "
                f"equity NEG DROP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
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
                    "leftover dual hole-fill after Résidence 3 — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Résidence 3 YE2025 Medium. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
                    "NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/"
                    "IGS/HVZ/energy/hospital/WZC/psych/MRS "
                    "(Les Buissons Spa deferred). " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Résidence 3; "
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
                    f"tick{TICK} leftover Résidence 3 Bruxelles {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m pnl "
                    f"LOSS NARROW {PNL/1e6:.2f}m equity NEG DROP {EQUITY/1e6:.2f}m "
                    f"FTE JUMP {FTE}; assets/debt Unknown; 2 VE NACE 87.101/87.301 "
                    f"Korian/Saphir path); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    f"Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/"
                    f"IDELUX*/INTRADEL/ORES SC taken; next {NEXT_RQ}; next every-10 "
                    f"2120; continuous hole_fill"
                ),
            }
        )
    print("loop_state ->", TICK)


def append_log():
    entry = f"""

## Tick {TICK} - {UTC} - {RQ} Résidence 3 Bruxelles (omzet JUMP 7.44m / pnl LOSS NARROW -0.75m / NEG equity / Medium)

- Unit: **{RQ}** leftover dual after **rq_2112 Elisabeth Aan Zee Oostende**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Résidence 3** YE2025 (KBO **{KBO}**; Eliane Vogel-Polskystraat 20 Brussel/Laken; **NV/SA** NACE **87.101/87.301** / **2 VE** Saphir+Palmboomstraat; **Korian Belgium** bestuurder **0869.769.702** path). Do not redo Elisabeth Aan Zee/XXe Août/Ninove/Zilverlinde/Sint-Camillus/IDELUX*/INTRADEL/ORES SC/Korian holding/Comnexio/SLG*/Always Home/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +24.85%; bruto **EUR{BRUTO}** DROP −5.66%; pnl **LOSS EUR{PNL}** LOSS NARROW +37.6% vs YE2024 LOSS EUR{PNL_PRIOR}; equity **NEG EUR{EQUITY}** DROP −43.05% vs YE2024 NEG EUR{EQUITY_PRIOR}; FTE **{FTE}** JUMP vs YE2024 {FTE_PRIOR}; neerlegging **28.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via {EMAIL} (alt {EMAIL_ALT}).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.6); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2113/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2110**; next **2120**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Les Buissons Spa deferred / unused IGS-DSO-WZC-MRS).
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
                "source_id": "src_residence_3_jr2025_cw_nl",
                "title": "Companyweb NL — Résidence 3 YE2025",
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
                "source_id": "src_residence_3_jr2025_cw_en",
                "title": "Companyweb EN — Résidence 3 YE2025",
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
                "source_id": "src_residence_3_jr2025_cw_fr",
                "title": "Companyweb FR — Résidence 3 YE2025",
                "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}/{SLUG}",
                "publisher": "Companyweb",
                "accessed_date": "2026-08-25",
                "source_class": "secondary_aggregator",
                "notes": f"tick{TICK}; FR cross-check same YE2025 euros; Medium",
            },
            {
                "source_id": f"src_residence_3_kbo_{TICK}",
                "title": f"KBO — Résidence 3 {KBO}",
                "url": (
                    "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
                    f"?ondernemingsnummer={KBO_DIGITS}"
                ),
                "publisher": "KBO/BCE",
                "accessed_date": "2026-08-25",
                "source_class": "primary_register",
                "notes": (
                    f"tick{TICK}; Actief NV 2 VE; NACE 87.101/87.301; zetel {ADDR}; "
                    f"bestuurder Korian Belgium 0869.769.702; FOI {EMAIL}; Strong"
                ),
            },
            {
                "source_id": f"src_residence_3_contact_{TICK}",
                "title": "Résidence 3 / Saphir / Korian FOI contact",
                "url": WEBSITE,
                "publisher": "Korian Belgium / Saphir",
                "accessed_date": "2026-08-25",
                "source_class": "entity_site",
                "notes": (
                    f"tick{TICK}; {EMAIL}; alt {EMAIL_ALT}; KBO email empty; "
                    f"postal {ADDR}; site {WEBSITE}"
                ),
            },
        ],
    )
    append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": "bud_residence_3_omzet_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(OMZET),
                "amount_min_eur": str(OMZET),
                "amount_max_eur": str(OMZET),
                "basis": "CW YE2025 omzet / Turnover (primary envelope MRS NV)",
                "source_id": "src_residence_3_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; JUMP +24.85% vs YE2024 {OMZET_PRIOR}",
            },
            {
                "budget_id": "bud_residence_3_bruto_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(BRUTO),
                "amount_min_eur": str(BRUTO),
                "amount_max_eur": str(BRUTO),
                "basis": "CW YE2025 Brutomarge / Gross margin",
                "source_id": "src_residence_3_jr2025_cw_en",
                "confidence": "medium",
                "notes": f"tick{TICK}; DROP −5.66% vs YE2024 {BRUTO_PRIOR}",
            },
            {
                "budget_id": "bud_residence_3_pnl_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(PNL),
                "amount_min_eur": str(PNL),
                "amount_max_eur": str(PNL),
                "basis": "CW YE2025 Profit/Loss",
                "source_id": "src_residence_3_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; LOSS NARROW +37.6% vs YE2024 LOSS {PNL_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_residence_3_equity_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(EQUITY),
                "amount_min_eur": str(EQUITY),
                "amount_max_eur": str(EQUITY),
                "basis": "CW YE2025 Eigen vermogen / Equity",
                "source_id": "src_residence_3_jr2025_cw_en",
                "confidence": "medium",
                "notes": (
                    f"tick{TICK}; NEG DROP −43.05% vs YE2024 NEG {EQUITY_PRIOR}"
                ),
            },
            {
                "budget_id": "bud_residence_3_fte_jr2025_statutory",
                "entity_id": ENTITY,
                "year": "2025",
                "amount_eur": str(FTE),
                "amount_min_eur": str(FTE),
                "amount_max_eur": str(FTE),
                "basis": "CW social-balance FTE / Employees",
                "source_id": "src_residence_3_jr2025_cw_en",
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
                    "Résidence 3 YE2025 leftover dual "
                    "(omzet JUMP 7.44m / pnl LOSS NARROW / NEG equity)"
                ),
                "entity_id": ENTITY,
                "beneficiary": "MRS residents / care users Bruxelles (2 VE)",
                "legal_basis": (
                    f"NV/SA maison de repos RVT+ROB (KBO {KBO}; NACE 87.101/87.301; "
                    "2 VE; Korian Belgium bestuurder)"
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
                    "Public-interest nursing-home care (Résidence 3 / Saphir / "
                    "Korian path; Iriscare-adjacent)"
                ),
                "cut_option": (
                    "Publish NBB PDF assets/debt FOI; explain LOSS NARROW vs NEG "
                    "equity DROP −43%; map Iriscare/INAMI vs omzet split; 2 VE "
                    "matrix (Saphir Laeken + Palmboomstraat); dual Korian holding"
                ),
                "source_id": "src_residence_3_jr2025_cw_en",
                "confidence": "medium",
                "hierarchy_path": (
                    "Bruxelles>Laeken>Residence_3_Saphir>JR2025_statutory_L5"
                ),
                "notes": (
                    f"tick{TICK}; Medium CW; omzet primary envelope; assets/debt "
                    "Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; not "
                    "TE-additive of 348bn; DISTINCT Elisabeth Aan Zee/XXe Août/"
                    "Ninove/Zilverlinde/Sint-Camillus; dual Korian Belgium"
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
                    "Résidence 3 omzet JUMP 7.44m / pnl LOSS NARROW −0.75m / "
                    "NEG equity −2.51m (YE2025)"
                ),
                "level": "L5",
                "type": "mrs_statutory_nv_korian_path",
                "hierarchy_path": (
                    "Bruxelles>Laeken>Residence_3_Saphir>JR2025"
                ),
                "annual_cost_eur": str(OMZET),
                "total_cost_eur": str(OMZET),
                "tco_notes": (
                    f"CW YE2025 omzet {OMZET} JUMP +24.85% (primary); bruto {BRUTO} "
                    f"DROP −5.66%; pnl LOSS {PNL} NARROW +37.6% vs LOSS {PNL_PRIOR}; "
                    f"equity NEG {EQUITY} DROP −43.05%; FTE JUMP {FTE}; assets/debt "
                    "Unknown pending NBB PDF; Korian/Saphir path"
                ),
                "confidence": "medium",
                "source_id": "src_residence_3_jr2025_cw_en",
                "beneficiaries": "MRS residents / care users Bruxelles (2 VE)",
                "stated_goal": (
                    "Public-interest nursing-home care (Korian/Saphir path)"
                ),
                "measured_outcome": (
                    "omzet JUMP +24.85%; bruto DROP −5.66%; pnl LOSS NARROW +37.6%; "
                    f"equity NEG DROP −43.05%; FTE JUMP {FTE}"
                ),
                "absurdity_score": "7.2",
                "cost_score": "5.5",
                "difficulty": "3.5",
                "priority_index": "6.6",
                "cut_proposal": (
                    "FOI NBB PDF + Iriscare/INAMI split + explain NEG equity DROP "
                    "despite LOSS NARROW and omzet JUMP; map 2 VE + Korian holding dual"
                ),
                "status": "open",
                "struck_reason": "",
                "notes": (
                    f"tick{TICK}; Medium CW; FOI {GAP}; preferred FARO/AIESH/REW still "
                    "YE2024; DISTINCT Elisabeth Aan Zee/XXe Août/Ninove; dual Korian"
                ),
            }
        ],
    )
    foi_row = {
        "gap_id": GAP,
        "hierarchy_path": (
            "Bruxelles>Laeken>Residence_3_Saphir>"
            "NBB_PDF_assets_debt_pnl_loss_narrow_neg_equity"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); LOSS NARROW "
            "vs NEG equity DROP path; Iriscare/INAMI vs omzet split; 2 VE matrix "
            "(Saphir Laeken + Palmboomstraat Woluwe); Korian holding dual"
        ),
        "why_it_matters": (
            "Medium CW shows 7.44m omzet Brussels MRS NV with LOSS NARROW to −0.75m "
            "but equity NEG DROP to −2.51m (−43%) despite omzet JUMP +25% — "
            "care-margin / solvency transparency gap on Iriscare-adjacent path"
        ),
        "priority": "8",
        "recipient_body": "Résidence 3 SA / Korian Belgium / Saphir",
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
