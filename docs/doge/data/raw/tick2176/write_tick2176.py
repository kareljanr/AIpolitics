# tick 2176 — Farys Solar YE2025 Medium CW after Senes
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T04:40:00Z"
ENTITY = "bv_farys_solar"
GAP = "gap_farys_solar_nbb_pdf_assets_debt_nace_nonrenewable_solar_name_matrix_l5"
COMM = "comm_farys_solar_jr2025_statutory_water_dual_omzet_jump_pnl_jump"
LB = "lb_farys_solar_omzet_jump_1_12m_pnl_jump_nace_nonrenewable_jr2025"
SRC_EN = "src_farys_solar_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2176":
            row = dict(row)
            row["title"] = (
                "leftover dual — Farys Solar YE2025 Medium "
                "(omzet JUMP 1.12m / pnl JUMP +134% / NACE non-renewable)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Farys Solar after Senes; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2176 Farys Solar 0886.870.604 Medium; omzet JUMP 1117192 pnl JUMP 263038 "
                "equity JUMP 4828566 bruto 837933 FTE 1; NACE 35.110 non-renewable; aanbestedende; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2177; next every-10 2180"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2177" for x in out):
        out.append(
            {
                "task_id": "rq_2177",
                "title": (
                    "leftover dual hole-fill after Farys Solar — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2177 after Farys Solar YE2025 Medium (omzet JUMP 1.12m / pnl JUMP +134% / "
                    "NACE 35.110 non-renewable vs Solar name). Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. "
                    "Do NOT redo Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/"
                    "Abdij/Aaigem/Anima*/Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis Belgium/Farys OV."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2176 Farys Solar; FARO/AIESH/REW still YE2024; next every-10 2180",
            }
        )
        print("SPAWN rq_2177")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2176=done")


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
        "last_unit_id": "rq_2176",
        "ticks_completed": "2176",
        "paused": "no",
        "notes": (
            "tick2176 leftover FARYS SOLAR 0886.870.604 Medium (omzet JUMP 1.12m; pnl JUMP 263k +134%; "
            "equity JUMP 4.83m; bruto 838k; FTE 1; NACE 35.110 non-renewable vs Solar name; "
            "aanbestedende; Stropstraat 1 Gent); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2177; next every-10 2180; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2176")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Farys Solar BV (Gent / Vanbo Solar Invest)",
            "name_fr": "Farys Solar SRL (Gand / Vanbo Solar Invest)",
            "name_en": "Farys Solar BV (Ghent / Vanbo Solar Invest)",
            "level": "parastatal",
            "parent_id": "farys",
            "community_language": "nl",
            "website": "https://www.farys.be",
            "foi_email": "info@farys.be",
            "foi_postal": "Stropstraat 1, 9000 Gent",
            "notes": (
                "tick2176 YE2025 Medium CW NL+EN+FR + Strong KBO 0886.870.604 Actief BV 1 VE "
                "NACE 35.110 non-renewable; handelsnaam Vanbo Solar Invest; aanbestedende overheid; "
                "omzet JUMP 1117192 pnl JUMP 263038 equity JUMP 4828566 bruto JUMP 837933 FTE 1; "
                "same zetel Farys OV; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_farys_solar_jr2025_cw_nl",
            "title": "Companyweb NL Farys Solar YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0886870604/farys-solar",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2176; YE2025 omzet JUMP 1117192 pnl JUMP 263038 equity JUMP 4828566 bruto 837933 FTE 1; "
                "neerlegging 18.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2176/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Farys Solar YE2025 statutory",
            "url": "https://www.companyweb.be/en/0886870604/farys-solar",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2176; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; "
                "Turnover 1117192 Profit/Loss 263038 Equity 4828566"
            ),
        },
        {
            "source_id": "src_farys_solar_jr2025_cw_fr",
            "title": "Companyweb FR Farys Solar YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0886870604",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2176; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_farys_solar_kbo_2176",
            "title": "KBO Farys Solar 0886.870.604 Actief BV Gent aanbestedende",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0886870604",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2176; Actief BV; Stropstraat 1 9000 Gent; 1 VE; NACE 35.110; "
                "aanbestedende overheid; handelsnaam Vanbo Solar Invest; KBO email empty"
            ),
        },
        {
            "source_id": "src_farys_solar_foi_contact_2176",
            "title": "Farys Solar / Farys OV FOI channel info@farys.be",
            "url": "https://www.farys.be",
            "publisher": "Farys OV",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2176; info@farys.be; Stropstraat 1 9000 Gent; KBO email empty",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_farys_solar_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1117192",
            "amount_min_eur": "1117192",
            "amount_max_eur": "1117192",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2176; Medium CW; omzet JUMP +18.79% vs YE2024 940475",
        },
        {
            "budget_id": "bud_farys_solar_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "837933",
            "amount_min_eur": "837933",
            "amount_max_eur": "837933",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2176; Medium CW; bruto JUMP +28.47% vs YE2024 652250",
        },
        {
            "budget_id": "bud_farys_solar_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "263038",
            "amount_min_eur": "263038",
            "amount_max_eur": "263038",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2176; Medium CW; pnl JUMP +134.38% vs YE2024 112229",
        },
        {
            "budget_id": "bud_farys_solar_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "4828566",
            "amount_min_eur": "4828566",
            "amount_max_eur": "4828566",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2176; Medium CW; equity JUMP +5.76% vs YE2024 4565527",
        },
        {
            "budget_id": "bud_farys_solar_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1",
            "amount_min_eur": "1",
            "amount_max_eur": "1",
            "basis": "CW social-balance FTE / Employees 1",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2176; Medium CW; FTE 1; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Farys Solar YE2025 leftover dual "
                "(omzet JUMP 1.12m / pnl JUMP +134% / NACE non-renewable)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "Farys OV / municipal water dual renewable-power path",
            "legal_basis": (
                "BV power (KBO 0886.870.604; Actief; 1 VE; NACE 35.110; "
                "aanbestedende overheid; handelsnaam Vanbo Solar Invest)"
            ),
            "decision_date": "2026-06-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "1117192",
            "cash_by_year": (
                '{"2025_omzet":1117192,"2025_bruto":837933,"2025_pnl":263038,"2025_equity":4828566,'
                '"2025_fte":1,"2024_omzet":940475,"2024_bruto":652250,"2024_pnl":112229,"2024_equity":4565527}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0886870604/farys-solar",
            "stated_goal": "Electricity production vehicle (Farys Solar / Vanbo Solar Invest)",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose NACE 35.110 non-renewable vs Solar name; "
                "map Farys/Creat/Waterunie related-party"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>IGS>Farys>FarysSolar>JR2025_statutory_L5",
            "notes": (
                "tick2176; Medium CW; omzet primary envelope; pnl JUMP +134%; NACE non-renewable paradox; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "DISTINCT Farys OV parent + Creat"
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
                "Farys Solar omzet JUMP 1.12m / pnl JUMP +134% / NACE non-renewable (YE2025)"
            ),
            "level": "L5",
            "type": "water_dual_power_bv_statutory",
            "hierarchy_path": "Vlaanderen>IGS>Farys>FarysSolar>JR2025",
            "annual_cost_eur": "1117192",
            "total_cost_eur": "1117192",
            "tco_notes": (
                "CW omzet JUMP envelope 1.12m / bruto 0.84m / pnl JUMP 263k +134% / equity 4.83m / FTE 1; "
                "NACE 35.110 non-renewable vs Solar name; aanbestedende; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "Farys OV / municipal water dual renewable-power path",
            "stated_goal": "Electricity production (named Solar / coded non-renewable)",
            "measured_outcome": "omzet JUMP +18.8%; pnl JUMP +134%; equity JUMP +5.8%; FTE 1; NACE 35.110",
            "absurdity_score": "6.2",
            "cost_score": "4.0",
            "difficulty": "3.0",
            "priority_index": "5.1",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose generation mix vs Solar name; "
                "map related-party vs Farys OV / Creat / Waterunie"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2176; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "unused water dual after Senes"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>IGS>Farys>FarysSolar>NBB_PDF_assets_debt_nace_solar",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "NACE 35.110 non-renewable vs Solar/Vanbo name generation mix; "
                "related-party vs Farys OV + Creat + Waterunie Operator; "
                "omzet JUMP EUR1.12m PPA/offtake path; ownership % + dividend vs equity EUR4.83m"
            ),
            "why_it_matters": (
                "Medium CW shows Farys aanbestedende Solar-named BV with EUR1.12m omzet and pnl JUMP +134% "
                "while KBO codes non-renewable electricity — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Farys Solar BV / Farys OV",
            "recipient_email": "info@farys.be",
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
            "notes": "tick2176; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2176")
