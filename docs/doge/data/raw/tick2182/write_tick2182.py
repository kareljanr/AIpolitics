# tick 2182 — Groep INTRO Maatwerk YE2025 Medium CW after MAAAT
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T06:40:00Z"
ENTITY = "vzw_groep_intro_maatwerk"
GAP = "gap_groep_intro_maatwerk_nbb_pdf_assets_debt_bruto_gt_omzet_fte_drop_equity_jump_matrix_l5"
COMM = "comm_groep_intro_maatwerk_jr2025_statutory_omzet_jump_bruto_gt_omzet"
LB = "lb_groep_intro_maatwerk_omzet_jump_8_13m_bruto_gt_omzet_fte_drop_jr2025"
SRC_EN = "src_groep_intro_maatwerk_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2182":
            row = dict(row)
            row["title"] = (
                "leftover dual — Groep INTRO Maatwerk YE2025 Medium "
                "(omzet JUMP 8.13m / bruto>omzet / FTE DROP / equity JUMP)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Groep INTRO Maatwerk after MAAAT; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2182 Groep INTRO Maatwerk 0472.098.703 Medium; omzet JUMP 8125120 bruto 12149754 "
                "pnl JUMP 971754 equity JUMP 4209703 FTE DROP 274.5; 24 VE Anderlecht; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2183; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2183" for x in out):
        out.append(
            {
                "task_id": "rq_2183",
                "title": (
                    "leftover dual hole-fill after Groep INTRO Maatwerk — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2183 after Groep INTRO Maatwerk YE2025 Medium (omzet JUMP 8.13m / bruto>omzet / "
                    "FTE DROP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo Groep INTRO Maatwerk/"
                    "MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/"
                    "Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2182 Groep INTRO Maatwerk; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2183")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2182=done")


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
        "last_unit_id": "rq_2182",
        "ticks_completed": "2182",
        "paused": "no",
        "notes": (
            "tick2182 leftover GROEP INTRO MAATWERK 0472.098.703 Medium (omzet JUMP 8.13m; "
            "bruto 12.15m ≫ omzet; pnl JUMP 972k; equity JUMP 4.21m; FTE DROP 274.5; 24 VE Anderlecht); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2183; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2182")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Groep INTRO Maatwerk VZW (Anderlecht)",
            "name_fr": "Groep INTRO Maatwerk ASBL (Anderlecht)",
            "name_en": "Groep INTRO Maatwerk non-profit (Anderlecht / sheltered workshop)",
            "level": "parastatal",
            "parent_id": "brussels_gov",
            "community_language": "bi",
            "website": "https://www.groepintro.be",
            "foi_email": "info@groepintro.be",
            "foi_postal": "Charles Parentéstraat 6, 1070 Anderlecht",
            "notes": (
                "tick2182 YE2025 Medium CW NL+EN+FR + Strong KBO 0472.098.703 Actief VZW 24 VE "
                "RSZ NACE 88.993; omzet JUMP 8125120 bruto JUMP 12149754 (≫omzet) pnl JUMP 971754 "
                "equity JUMP 4209703 FTE DROP 274.5; absorbed Levanto-Fixit; same zetel Groep INTRO VZW "
                "0461.936.071; neerlegging 22.04.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_groep_intro_maatwerk_jr2025_cw_nl",
            "title": "Companyweb NL Groep INTRO Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0472098703/groep-intro-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2182; YE2025 omzet JUMP 8125120 bruto 12149754 pnl JUMP 971754 "
                "equity JUMP 4209703 FTE DROP 274.5; neerlegging 22.04.2026; "
                "raw docs/doge/data/raw/tick2182/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Groep INTRO Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0472098703/groep-intro-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2182; EN mirror YE2025 Medium; filed 22-04-2026; Last balance sheet year 2025; "
                "Turnover 8125120 Profit/Loss 971754 Equity 4209703 Employees 274.5"
            ),
        },
        {
            "source_id": "src_groep_intro_maatwerk_jr2025_cw_fr",
            "title": "Companyweb FR Groep INTRO Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0472098703",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2182; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_groep_intro_maatwerk_kbo_2182",
            "title": "KBO Groep INTRO Maatwerk 0472.098.703 Actief VZW Anderlecht 24 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472098703",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2182; Actief VZW; Charles Parentéstraat 6 1070 Anderlecht; 24 VE; "
                "RSZ NACE 88.993; absorbed Levanto-Fixit 0476.914.158; aannemer; KBO email empty"
            ),
        },
        {
            "source_id": "src_groep_intro_maatwerk_foi_contact_2182",
            "title": "Groep INTRO Maatwerk FOI channel info@groepintro.be",
            "url": "https://www.groepintro.be/nl/contact/",
            "publisher": "Groep INTRO",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2182; info@groepintro.be; +32 2 242 85 43; Charles Parentéstraat 6 1070 Anderlecht",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_groep_intro_maatwerk_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "8125120",
            "amount_min_eur": "8125120",
            "amount_max_eur": "8125120",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2182; Medium CW; omzet JUMP +5.12% vs YE2024 7729276",
        },
        {
            "budget_id": "bud_groep_intro_maatwerk_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "12149754",
            "amount_min_eur": "12149754",
            "amount_max_eur": "12149754",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2182; Medium CW; bruto JUMP +2.81% vs YE2024 11818211; bruto≫omzet",
        },
        {
            "budget_id": "bud_groep_intro_maatwerk_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "971754",
            "amount_min_eur": "971754",
            "amount_max_eur": "971754",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2182; Medium CW; pnl JUMP +26.32% vs YE2024 769294",
        },
        {
            "budget_id": "bud_groep_intro_maatwerk_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "4209703",
            "amount_min_eur": "4209703",
            "amount_max_eur": "4209703",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2182; Medium CW; equity JUMP +29.32% vs YE2024 3255253",
        },
        {
            "budget_id": "bud_groep_intro_maatwerk_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "274.5",
            "amount_min_eur": "274.5",
            "amount_max_eur": "274.5",
            "basis": "CW social-balance FTE / Employees 274.5",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2182; Medium CW; FTE DROP vs YE2024 283.5; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Groep INTRO Maatwerk YE2025 leftover dual "
                "(omzet JUMP 8.13m / bruto>omzet / FTE DROP / equity JUMP)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Brussels-Anderlecht multi-site",
            "legal_basis": "VZW maatwerk (KBO 0472.098.703; Actief; 24 VE; RSZ NACE 88.993)",
            "decision_date": "2026-04-22",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "8125120",
            "cash_by_year": (
                '{"2025_omzet":8125120,"2025_bruto":12149754,"2025_pnl":971754,"2025_equity":4209703,'
                '"2025_fte":274.5,"2024_omzet":7729276,"2024_bruto":11818211,"2024_pnl":769294,'
                '"2024_equity":3255253,"2024_fte":283.5}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0472098703/groep-intro-maatwerk",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "map Groep INTRO VZW parent + Levanto-Fixit absorption"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Brussel>Anderlecht>GroepINTRO>Maatwerk>JR2025_statutory_L5",
            "notes": (
                "tick2182; Medium CW; omzet primary envelope; bruto≫omzet; FTE DROP with equity JUMP; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Groep INTRO Maatwerk omzet JUMP 8.13m / bruto>omzet / FTE DROP (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Brussel>Anderlecht>GroepINTRO>Maatwerk>JR2025",
            "annual_cost_eur": "8125120",
            "total_cost_eur": "8125120",
            "tco_notes": (
                "CW omzet JUMP envelope 8.13m / bruto 12.15m ≫ omzet / pnl JUMP 972k / equity JUMP 4.21m / "
                "FTE DROP 274.5; 24 VE; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Brussels / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +5.1%; bruto JUMP +2.8%; pnl JUMP +26%; equity JUMP +29%; FTE DROP",
            "absurdity_score": "5.8",
            "cost_score": "5.0",
            "difficulty": "3.0",
            "priority_index": "5.4",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/Actiris/ESF split; "
                "map Groep INTRO VZW + 24 VE matrix"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2182; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Brussels maatwerk dual after MAAAT"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Brussel>Anderlecht>GroepINTRO>Maatwerk>NBB_PDF_assets_debt_bruto",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR12.15m ≫ omzet EUR8.13m loonkostsubsidie/GESCO/ESF/Actiris matrix; "
                "equity JUMP +29% vs FTE DROP path; related-party vs Groep INTRO VZW 0461.936.071 + "
                "Levanto-Fixit absorption residual; per-VE / top-10 opdrachtgevers"
            ),
            "why_it_matters": (
                "Medium CW shows Brussels maatwerk VZW with EUR8.13m omzet, subsidy-inflated bruto "
                "EUR12.15m, equity JUMP while shedding FTE — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Groep INTRO Maatwerk VZW",
            "recipient_email": "info@groepintro.be",
            "recipient_postal": "Charles Parentéstraat 6, 1070 Anderlecht",
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
            "notes": "tick2182; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2182")
