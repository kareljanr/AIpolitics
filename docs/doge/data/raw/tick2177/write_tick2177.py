# tick 2177 — Creat CV / Farys cvba YE2025 Medium CW after Farys Solar
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T05:00:00Z"
ENTITY = "cv_creat_farys"
GAP = "gap_creat_cv_nbb_pdf_assets_debt_omzet_50m_bruto_thin_fte0_matrix_l5"
COMM = "comm_creat_cv_jr2025_statutory_farys_dual_omzet_jump_50m_bruto_thin"
LB = "lb_creat_cv_omzet_jump_50_2m_bruto_thin_fte0_jr2025"
SRC_EN = "src_creat_cv_jr2025_cw_en"


def append_rows(path, rows):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    key = fieldnames[0]
    ids = {row.get(key) for row in existing}
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        for row in rows:
            if row.get(key) in ids:
                print("SKIP dup", path.name, row.get(key))
                continue
            w.writerow({k: row.get(k, "") for k in fieldnames})
            print("ADD", path.name, row.get(key))


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    out = []
    for row in rows:
        if row.get("task_id") == "rq_2177":
            row = dict(row)
            row["title"] = (
                "leftover dual — Creat CV / Farys cvba YE2025 Medium "
                "(omzet JUMP 50.2m / bruto thin 350k / FTE 0)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Creat CV after Farys Solar; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2177 Creat CV 0554.887.312 Medium; omzet JUMP 50163334 bruto thin 349506 "
                "pnl DROP 179023 equity JUMP 1994141 FTE 0; NACE 46.190; Farys cvba; aanbestedende; "
                "DISTINCT igs_creat 0692.624.441; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2178; next every-10 2180"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2178" for x in out):
        out.append(
            {
                "task_id": "rq_2178",
                "title": (
                    "leftover dual hole-fill after Creat CV — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2178 after Creat CV / Farys cvba YE2025 Medium (omzet JUMP 50.2m / bruto thin "
                    "350k / FTE 0). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo Creat CV/"
                    "Farys Solar/Springplank/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/"
                    "Anima*/emeis/Farys OV/Creat Services dv."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2177 Creat CV; FARO/AIESH/REW still YE2024; next every-10 2180",
            }
        )
        print("SPAWN rq_2178")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2177=done")


def update_loop_state():
    path = DATA / "loop_state.csv"
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    rows[0] = {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2177",
        "ticks_completed": "2177",
        "paused": "no",
        "notes": (
            "tick2177 leftover CREAT CV 0554.887.312 Medium (omzet JUMP 50.2m; bruto thin 350k; "
            "pnl DROP 179k; equity JUMP 1.99m; FTE 0; NACE 46.190; handelsnaam Farys cvba; "
            "aanbestedende; Stropstraat 1 Gent; DISTINCT igs_creat); AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2178; next every-10 2180; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2177")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Creat CV (Gent / handelsnaam Farys cvba)",
            "name_fr": "Creat SC (Gand / nom commercial Farys cvba)",
            "name_en": "Creat CV (Ghent / commercial name Farys cvba)",
            "level": "parastatal",
            "parent_id": "farys",
            "community_language": "nl",
            "website": "https://www.creat.be",
            "foi_email": "secretariaat@creat.be",
            "foi_postal": "Stropstraat 1, 9000 Gent",
            "notes": (
                "tick2177 YE2025 Medium CW NL+EN+FR + Strong KBO 0554.887.312 Actief CV 1 VE "
                "NACE 46.190; handelsnaam Farys cvba; aanbestedende overheid; "
                "omzet JUMP 50163334 bruto thin 349506 pnl DROP 179023 equity JUMP 1994141 FTE 0; "
                "same zetel Farys OV + Farys Solar; Porto-Carrero gedelegeerd; "
                "DISTINCT igs_creat Creat Services dv 0692.624.441; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_creat_cv_jr2025_cw_nl",
            "title": "Companyweb NL Creat CV / Farys cvba YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0554887312/creat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2177; YE2025 omzet JUMP 50163334 bruto thin 349506 pnl DROP 179023 "
                "equity JUMP 1994141 FTE 0; neerlegging 18.06.2026; assets/debt Unknown; "
                "raw docs/doge/data/raw/tick2177/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Creat CV / Farys cvba YE2025 statutory",
            "url": "https://www.companyweb.be/en/0554887312/creat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2177; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; "
                "Turnover 50163334 Profit/Loss 179023 Equity 1994141"
            ),
        },
        {
            "source_id": "src_creat_cv_jr2025_cw_fr",
            "title": "Companyweb FR Creat CV / Farys cvba YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0554887312",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2177; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_creat_cv_kbo_2177",
            "title": "KBO Creat CV 0554.887.312 Actief CV Gent Farys cvba aanbestedende",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0554887312",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2177; Actief CV; Stropstraat 1 9000 Gent; 1 VE; NACE 46.190; "
                "aanbestedende overheid; handelsnaam Farys cvba; email secretariaat@creat.be; "
                "gedelegeerd Porto-Carrero"
            ),
        },
        {
            "source_id": "src_creat_cv_foi_contact_2177",
            "title": "Creat CV / Farys FOI channel secretariaat@creat.be",
            "url": "https://www.creat.be",
            "publisher": "Creat CV / Farys",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2177; secretariaat@creat.be; also info@farys.be; Stropstraat 1 9000 Gent",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_creat_cv_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "50163334",
            "amount_min_eur": "50163334",
            "amount_max_eur": "50163334",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; Medium CW; omzet JUMP +20.89% vs YE2024 41495913",
        },
        {
            "budget_id": "bud_creat_cv_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "349506",
            "amount_min_eur": "349506",
            "amount_max_eur": "349506",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; Medium CW; bruto DROP -2.33% vs YE2024 357832; thin vs 50.2m omzet",
        },
        {
            "budget_id": "bud_creat_cv_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "179023",
            "amount_min_eur": "179023",
            "amount_max_eur": "179023",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; Medium CW; pnl DROP -11.11% vs YE2024 201403",
        },
        {
            "budget_id": "bud_creat_cv_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1994141",
            "amount_min_eur": "1994141",
            "amount_max_eur": "1994141",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; Medium CW; equity JUMP +10.37% vs YE2024 1806748",
        },
        {
            "budget_id": "bud_creat_cv_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "0",
            "amount_min_eur": "0",
            "amount_max_eur": "0",
            "basis": "CW social-balance FTE / Employees 0",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; Medium CW; FTE 0; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Creat CV / Farys cvba YE2025 leftover dual "
                "(omzet JUMP 50.2m / bruto thin 350k / FTE 0)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "Farys OV / municipal procurement / Creat aankoopcentrale path",
            "legal_basis": (
                "CV trading (KBO 0554.887.312; Actief; 1 VE; NACE 46.190; "
                "aanbestedende overheid; handelsnaam Farys cvba)"
            ),
            "decision_date": "2026-06-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "50163334",
            "cash_by_year": (
                '{"2025_omzet":50163334,"2025_bruto":349506,"2025_pnl":179023,"2025_equity":1994141,'
                '"2025_fte":0,"2024_omzet":41495913,"2024_bruto":357832,"2024_pnl":201403,"2024_equity":1806748}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0554887312/creat",
            "stated_goal": "Non-specialised wholesale agency / Farys municipal procurement dual",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose pass-through vs true margin; "
                "map Farys Solar / Creat Services / Waterunie related-party + per-deelnemer volume"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>IGS>Farys>CreatCV>JR2025_statutory_L5",
            "notes": (
                "tick2177; Medium CW; omzet primary envelope; bruto thin 0.7pct of omzet; FTE 0; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive; "
                "DISTINCT igs_creat 0692.624.441 + Farys Solar 0886.870.604"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Creat CV / Farys cvba omzet JUMP 50.2m / bruto thin 350k / FTE 0 (YE2025)",
            "level": "L5",
            "type": "water_dual_trading_cv_statutory",
            "hierarchy_path": "Vlaanderen>IGS>Farys>CreatCV>JR2025",
            "annual_cost_eur": "50163334",
            "total_cost_eur": "50163334",
            "tco_notes": (
                "CW omzet JUMP envelope 50.2m / bruto thin 0.35m (0.7pct) / pnl 179k / equity 1.99m / FTE 0; "
                "pass-through trading shell; aanbestedende; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "Farys OV / municipal procurement dual",
            "stated_goal": "Wholesale agency / Farys cvba procurement dual",
            "measured_outcome": "omzet JUMP +20.9%; bruto DROP -2.3%; pnl DROP -11.1%; FTE 0",
            "absurdity_score": "7.5",
            "cost_score": "6.5",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose pass-through matrix vs Farys Solar/"
                "Creat Services; per-deelnemer procurement volume behind EUR50m"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2177; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Farys stack dual after Farys Solar"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>IGS>Farys>CreatCV>NBB_PDF_assets_debt_omzet_50m_thin",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "omzet JUMP EUR50.16m vs bruto EUR0.35m / FTE 0 pass-through recon; "
                "related-party vs Farys OV + Farys Solar 0886.870.604 + Creat Services dv 0692.624.441; "
                "per-deelnemer / municipal procurement volume; ownership % + dividend vs equity EUR1.99m"
            ),
            "why_it_matters": (
                "Medium CW shows Farys-named aanbestedende CV with EUR50.2m omzet but only EUR350k bruto "
                "and 0 FTE — classic pass-through opacity; balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Creat CV (Farys cvba) / Farys OV",
            "recipient_email": "secretariaat@creat.be",
            "recipient_postal": "Stropstraat 1, 9000 Gent",
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
            "notes": "tick2177; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2177")
