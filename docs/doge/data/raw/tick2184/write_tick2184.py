# tick 2184 — Westlandia VZW YE2025 Medium CW after BWB/Wase race
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T07:20:00Z"
ENTITY = "vzw_westlandia_ieper"
GAP = "gap_westlandia_nbb_pdf_assets_debt_pnl_jump_bruto_gt_omzet_matrix_l5"
COMM = "comm_westlandia_jr2025_statutory_maatwerk_omzet_pnl_jump"
LB = "lb_westlandia_omzet_jump_20_18m_pnl_jump_bruto_gt_omzet_jr2025"
SRC_EN = "src_westlandia_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2184":
            row = dict(row)
            row["title"] = (
                "leftover dual — Westlandia Ieper YE2025 Medium "
                "(omzet JUMP 20.18m / pnl JUMP +102% / bruto>omzet / FTE 708)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Westlandia after BWB/Wase race; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2184 Westlandia 0407.768.895 Medium; omzet JUMP 20179678 bruto 28739117 "
                "pnl JUMP 1633039 equity JUMP 35038860 FTE JUMP 707.6; NACE 88.993; 4 VE Ieper; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2185; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2185" for x in out):
        out.append(
            {
                "task_id": "rq_2185",
                "title": (
                    "leftover dual hole-fill after Westlandia — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2185 after Westlandia Ieper YE2025 Medium (omzet JUMP 20.18m / pnl JUMP +102% / "
                    "bruto>omzet / FTE 708). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
                    "NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ/Weerwerk. "
                    "Do NOT redo Westlandia/BWB/Wase Werkplaats/Groep INTRO Maatwerk/MAAAT/WAAK SW/Waak/"
                    "Stijn/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2184 Westlandia; FARO/AIESH/REW still YE2024; "
                    "Weerwerk 0465.104.904 YE2025 FREE deferred; next every-10 2190"
                ),
            }
        )
        print("SPAWN rq_2185")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2184=done")


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
        "last_unit_id": "rq_2184",
        "ticks_completed": "2184",
        "paused": "no",
        "notes": (
            "tick2184 leftover Westlandia 0407.768.895 Medium (omzet JUMP 20.18m; bruto 28.74m ≫ omzet; "
            "pnl JUMP 1.63m +102%; equity JUMP 35.04m; FTE JUMP 707.6; NACE 88.993; 4 VE Ieper); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2185; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2184")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Westlandia VZW (Ieper maatwerk)",
            "name_fr": "Westlandia ASBL (entreprise de travail adapté Ieper)",
            "name_en": "Westlandia sheltered workshop non-profit (Ieper)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.westlandia.be",
            "foi_email": "info@westlandia.be",
            "foi_postal": "Dehemlaan 1, 8900 Ieper",
            "notes": (
                "tick2184 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.768.895 Actief VZW 4 VE "
                "NACE 88.993; omzet JUMP 20179678 bruto JUMP 28739117 (≫omzet) pnl JUMP 1633039 "
                "equity JUMP 35038860 FTE JUMP 707.6; neerlegging 05.06.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_westlandia_jr2025_cw_nl",
            "title": "Companyweb NL Westlandia VZW YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407768895/westlandia-vzw",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2184; YE2025 omzet JUMP 20179678 bruto 28739117 pnl JUMP 1633039 "
                "equity JUMP 35038860 FTE JUMP 707.6; neerlegging 05.06.2026; "
                "raw docs/doge/data/raw/tick2184/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Westlandia VZW YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407768895/westlandia-vzw",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2184; EN mirror YE2025 Medium; filed 05-06-2026; Last balance sheet year 2025; "
                "Turnover 20179678 Profit/Loss 1633039 Equity 35038860 Employees 707.6"
            ),
        },
        {
            "source_id": "src_westlandia_jr2025_cw_fr",
            "title": "Companyweb FR Westlandia VZW YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407768895",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2184; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_westlandia_kbo_2184",
            "title": "KBO Westlandia VZW 0407.768.895 Actief VZW Ieper",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407768895",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2184; Actief VZW; Dehemlaan 1 8900 Ieper; 4 VE; NACE 88.993; "
                "replaces 0411.020.375; KBO email/web empty; FOI via info@westlandia.be"
            ),
        },
        {
            "source_id": "src_westlandia_foi_contact_2184",
            "title": "Westlandia FOI channel info@westlandia.be",
            "url": "https://www.westlandia.be/nl/",
            "publisher": "Westlandia VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2184; info@westlandia.be; +32 57 220 440; Dehemlaan 1 8900 Ieper",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_westlandia_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "20179678",
            "amount_min_eur": "20179678",
            "amount_max_eur": "20179678",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; omzet JUMP +9.25% vs YE2024 18471578",
        },
        {
            "budget_id": "bud_westlandia_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "28739117",
            "amount_min_eur": "28739117",
            "amount_max_eur": "28739117",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; bruto JUMP +3.95% vs YE2024 27647942; bruto≫omzet",
        },
        {
            "budget_id": "bud_westlandia_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1633039",
            "amount_min_eur": "1633039",
            "amount_max_eur": "1633039",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; pnl JUMP +101.88% vs YE2024 808926",
        },
        {
            "budget_id": "bud_westlandia_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "35038860",
            "amount_min_eur": "35038860",
            "amount_max_eur": "35038860",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; equity JUMP +4.65% vs YE2024 33483521",
        },
        {
            "budget_id": "bud_westlandia_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "707.6",
            "amount_min_eur": "707.6",
            "amount_max_eur": "707.6",
            "basis": "CW social-balance FTE / Employees 707.6",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; FTE JUMP vs YE2024 697.9; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Westlandia Ieper YE2025 leftover dual "
                "(omzet JUMP 20.18m / pnl JUMP +102% / bruto>omzet)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients West-Vlaanderen Ieper",
            "legal_basis": "VZW maatwerk (KBO 0407.768.895; Actief; 4 VE; NACE 88.993)",
            "decision_date": "2026-06-05",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "20179678",
            "cash_by_year": (
                '{"2025_omzet":20179678,"2025_bruto":28739117,"2025_pnl":1633039,"2025_equity":35038860,'
                '"2025_fte":707.6,"2024_omzet":18471578,"2024_bruto":27647942,"2024_pnl":808926,'
                '"2024_equity":33483521,"2024_fte":697.9}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407768895/westlandia-vzw",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "explain pnl JUMP +102% vs omzet +9%"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>Westlandia>JR2025_statutory_L5",
            "notes": (
                "tick2184; Medium CW; omzet primary envelope; bruto≫omzet; pnl JUMP primary absurdity; "
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
            "name": "Westlandia omzet JUMP 20.18m / pnl JUMP +102% / bruto>omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>Westlandia>JR2025",
            "annual_cost_eur": "20179678",
            "total_cost_eur": "20179678",
            "tco_notes": (
                "CW omzet JUMP envelope 20.18m / bruto 28.74m ≫ omzet / pnl JUMP 1.63m +102% / "
                "equity 35.04m / FTE JUMP 707.6; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers West-Vlaanderen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +9.3%; bruto JUMP +4.0%; pnl JUMP +101.9%; FTE JUMP +1.4%",
            "absurdity_score": "6.8",
            "cost_score": "6.5",
            "difficulty": "3.0",
            "priority_index": "6.7",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF split; "
                "explain pnl JUMP +102% with only +9% omzet"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2184; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "maatwerk dual after BWB/Wase/Groep INTRO"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Ieper>Westlandia>NBB_PDF_assets_debt_pnl_jump",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl JUMP EUR1,633,039 (+101.88%) vs omzet JUMP +9.25% recon; "
                "bruto EUR28.74m ≫ omzet EUR20.18m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "top-10 opdrachtgevers public vs private offtake; per-VE split (4 VE)"
            ),
            "why_it_matters": (
                "Medium CW shows large Ieper maatwerk VZW (FTE 708) with pnl JUMP +102% while "
                "bruto≫omzet under subsidy inflation — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Westlandia VZW",
            "recipient_email": "info@westlandia.be",
            "recipient_postal": "Dehemlaan 1, 8900 Ieper",
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
            "notes": "tick2184; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2184")
