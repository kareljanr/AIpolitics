# tick 2180 EVERY-10 + WAAK SW YE2025 Medium CW after Stijn/Waak
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T06:00:00Z"
ENTITY = "vzw_waak_sw"
GAP = "gap_waak_sw_nbb_pdf_assets_debt_omzet_related_waak_parent_matrix_l5"
COMM = "comm_waak_sw_jr2025_statutory_maatwerk_omzet_4_32m_pnl_jump"
LB = "lb_waak_sw_omzet_4_32m_pnl_jump_related_waak_jr2025"
SRC_EN = "src_waak_sw_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2180":
            row = dict(row)
            row["title"] = (
                "EVERY-10 + leftover dual — WAAK SW YE2025 Medium "
                "(omzet 4.32m / pnl JUMP 430k / Waak sister)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed EVERY-10 + leftover WAAK SW after Stijn; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2180 EVERY-10 + WAAK SW 0457.351.040 Medium; omzet 4320994 bruto JUMP 2842358 "
                "pnl JUMP 429634 equity JUMP 4927322 FTE 61.3; sister of Waak 0439.993.582; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2181; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2181" for x in out):
        out.append(
            {
                "task_id": "rq_2181",
                "title": (
                    "leftover dual hole-fill after WAAK SW — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2181 after EVERY-10 + WAAK SW YE2025 Medium (omzet 4.32m / pnl JUMP 430k / "
                    "Waak sister). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo WAAK SW/Waak/"
                    "Stijn/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Anima*/emeis/Integro."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2180 EVERY-10 WAAK SW; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2181")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2180=done")


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
        "last_unit_id": "rq_2180",
        "ticks_completed": "2180",
        "paused": "no",
        "notes": (
            "tick2180 EVERY-10 + leftover WAAK SW 0457.351.040 Medium (omzet 4.32m; bruto JUMP 2.84m; "
            "pnl JUMP 430k; equity JUMP 4.93m; FTE 61.3; NACE 88.993; sister Waak parent); "
            "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2181; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2180")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "WAAK SW / Waak Maatwerkbedrijf WSW VZW (Kuurne)",
            "name_fr": "WAAK SW / Waak entreprise de travail adapté WSW ASBL (Kuurne)",
            "name_en": "WAAK SW / Waak sheltered workshop WSW non-profit (Kuurne)",
            "level": "parastatal",
            "parent_id": "vzw_waak_maatwerk",
            "community_language": "nl",
            "website": "https://www.waak.be",
            "foi_email": "info@waak.be",
            "foi_postal": "Heirweg 125, 8520 Kuurne",
            "notes": (
                "tick2180 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0457.351.040 Actief VZW 1 VE "
                "NACE 88.993; omzet 4320994 bruto JUMP 2842358 pnl JUMP 429634 equity JUMP 4927322 FTE 61.3; "
                "sister of Waak parent 0439.993.582 same zetel+board; neerlegging 13.05.2026; "
                f"assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_waak_sw_jr2025_cw_nl",
            "title": "Companyweb NL WAAK SW YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0457351040",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2180; YE2025 omzet 4320994 bruto JUMP 2842358 pnl JUMP 429634 "
                "equity JUMP 4927322 FTE 61.3; neerlegging 13.05.2026; "
                "raw docs/doge/data/raw/tick2180/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN WAAK SW YE2025 statutory",
            "url": "https://www.companyweb.be/en/0457351040",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2180; EN mirror YE2025 Medium; filed 13-05-2026; Last balance sheet year 2025; "
                "Turnover 4320994 Profit/Loss 429634 Equity 4927322 Employees 61.3"
            ),
        },
        {
            "source_id": "src_waak_sw_jr2025_cw_fr",
            "title": "Companyweb FR WAAK SW YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0457351040",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2180; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_waak_sw_kbo_2180",
            "title": "KBO WAAK SW 0457.351.040 Actief VZW Kuurne",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0457351040",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2180; Actief VZW; Heirweg 125 8520 Kuurne; 1 VE; NACE 88.993; "
                "afkorting WAAK SW; gedelegeerd Tim Vannieuwenhuyse; aannemer erkenning"
            ),
        },
        {
            "source_id": "src_waak_sw_foi_contact_2180",
            "title": "WAAK SW / Waak FOI channel info@waak.be",
            "url": "https://www.waak.be/nl/contact",
            "publisher": "Waak / WAAK SW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2180; info@waak.be; +32 56 36 34 34; Heirweg 125 8520 Kuurne",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_waak_sw_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "4320994",
            "amount_min_eur": "4320994",
            "amount_max_eur": "4320994",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2180; Medium CW; YE2024 omzet unpublished on CW; YE2022 omzet 3557197",
        },
        {
            "budget_id": "bud_waak_sw_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "2842358",
            "amount_min_eur": "2842358",
            "amount_max_eur": "2842358",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2180; Medium CW; bruto JUMP +6.79% vs YE2024 2661567",
        },
        {
            "budget_id": "bud_waak_sw_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "429634",
            "amount_min_eur": "429634",
            "amount_max_eur": "429634",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2180; Medium CW; pnl JUMP +9.24% vs YE2024 393296",
        },
        {
            "budget_id": "bud_waak_sw_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "4927322",
            "amount_min_eur": "4927322",
            "amount_max_eur": "4927322",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2180; Medium CW; equity JUMP +9.37% vs YE2024 4505334",
        },
        {
            "budget_id": "bud_waak_sw_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "61.3",
            "amount_min_eur": "61.3",
            "amount_max_eur": "61.3",
            "basis": "CW social-balance FTE / Employees 61.3",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2180; Medium CW; FTE 61.3 vs YE2024 59.9; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "WAAK SW YE2025 leftover dual EVERY-10 "
                "(omzet 4.32m / pnl JUMP 430k / Waak sister)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients West-Vlaanderen via Waak WSW path",
            "legal_basis": "VZW maatwerk WSW (KBO 0457.351.040; Actief; 1 VE; NACE 88.993)",
            "decision_date": "2026-05-13",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "4320994",
            "cash_by_year": (
                '{"2025_omzet":4320994,"2025_bruto":2842358,"2025_pnl":429634,"2025_equity":4927322,'
                '"2025_fte":61.3,"2024_bruto":2661567,"2024_pnl":393296,"2024_equity":4505334,"2024_fte":59.9}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0457351040",
            "stated_goal": "Sheltered employment WSW / maatwerk sister of Waak parent",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose related-party vs Waak parent 0439.993.582; "
                "explain separate WSW VZW vs parent EUR37.7m path"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>WSW>JR2025_statutory_L5",
            "notes": (
                "tick2180 EVERY-10; Medium CW; omzet primary envelope; sister of Waak parent; "
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
            "name": "WAAK SW omzet 4.32m / pnl JUMP 430k / Waak sister (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>WSW>JR2025",
            "annual_cost_eur": "4320994",
            "total_cost_eur": "4320994",
            "tco_notes": (
                "CW omzet envelope 4.32m / bruto 2.84m / pnl JUMP 430k / equity 4.93m / FTE 61.3; "
                "sister of Waak parent EUR37.7m; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers West-Vlaanderen / Waak WSW path",
            "stated_goal": "Sheltered employment WSW sister dual",
            "measured_outcome": "omzet 4.32m; bruto JUMP +6.8%; pnl JUMP +9.2%; FTE 61.3",
            "absurdity_score": "5.0",
            "cost_score": "4.5",
            "difficulty": "3.0",
            "priority_index": "4.9",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose related-party vs Waak parent; "
                "explain WSW split rationale"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2180 EVERY-10; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Waak sister dual"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>WSW>NBB_PDF_assets_debt_related",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "related-party vs Waak Maatwerkbedrijf VZW 0439.993.582 shared board/flows/cost allocation; "
                "YE2024 omzet unpublished recon; loonkostsubsidie split; WSW vs parent activity split"
            ),
            "why_it_matters": (
                "Medium CW shows Waak sister WSW VZW with EUR4.32m omzet and pnl JUMP while parent "
                "Waak runs EUR37.7m omzet / DEEPER LOSS — dual opacity on shared Kuurne seat"
            ),
            "priority": "8",
            "recipient_body": "WAAK MAATWERKBEDRIJF WSW VZW / Waak Maatwerkbedrijf VZW",
            "recipient_email": "info@waak.be",
            "recipient_postal": "Heirweg 125, 8520 Kuurne",
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
            "notes": "tick2180 EVERY-10; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2180")
