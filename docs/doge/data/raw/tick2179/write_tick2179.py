# tick 2179 — Stijn VZW YE2025 Medium CW after Waak
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T05:40:00Z"
ENTITY = "vzw_stijn_hasselt"
GAP = "gap_stijn_nbb_pdf_assets_debt_bruto_128m_vs_omzet_22m_vaph_matrix_l5"
COMM = "comm_stijn_jr2025_statutory_disability_bruto_jump_128m_omzet_22m"
LB = "lb_stijn_bruto_jump_128m_omzet_22m_pnl_drop_jr2025"
SRC_EN = "src_stijn_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2179":
            row = dict(row)
            row["title"] = (
                "leftover dual — Stijn VZW YE2025 Medium "
                "(bruto JUMP 128m / omzet 22.7m / pnl DROP 5.08m)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Stijn after Waak; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2179 Stijn 0439.452.461 Medium; bruto JUMP 128036084 omzet 22746378 "
                "pnl DROP 5079250 equity JUMP 59569328 FTE 1611.2; 36 VE; aanbestedende; "
                "NACE 88.104; same zetel Integro; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2180 EVERY-10; next every-10 2180"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2180" for x in out):
        out.append(
            {
                "task_id": "rq_2180",
                "title": (
                    "EVERY-10 + leftover dual hole-fill after Stijn — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2180 EVERY-10 progress+top10 THEN leftover after Stijn VZW YE2025 Medium "
                    "(bruto JUMP 128m / omzet 22.7m). Prefer leftover AGB/APB if JR2025 PDF live, else "
                    "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. "
                    "Do NOT redo Stijn/Waak/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/"
                    "Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis/Integro."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2179 Stijn; EVERY-10 due; FARO/AIESH/REW still YE2024",
            }
        )
        print("SPAWN rq_2180")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2179=done")


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
        "last_unit_id": "rq_2179",
        "ticks_completed": "2179",
        "paused": "no",
        "notes": (
            "tick2179 leftover STIJN 0439.452.461 Medium (bruto JUMP 128.0m ≫ omzet 22.7m; "
            "pnl DROP 5.08m; equity JUMP 59.6m; FTE 1611; 36 VE; aanbestedende; NACE 88.104; "
            "Hasselt same zetel Integro); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2180 EVERY-10; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2179")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Stijn VZW (Hasselt / handicapenzorg)",
            "name_fr": "Stijn ASBL (Hasselt / soins handicap)",
            "name_en": "Stijn non-profit (Hasselt / disability care)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.stijn.be",
            "foi_email": "info@stijn.be",
            "foi_postal": "Kempische steenweg 555, 3500 Hasselt",
            "notes": (
                "tick2179 YE2025 Medium CW NL+EN+FR + Strong KBO 0439.452.461 Actief VZW 36 VE "
                "aanbestedende; RSZ NACE 88.104; bruto JUMP 128036084 omzet JUMP 22746378 "
                "pnl DROP 5079250 equity JUMP 59569328 FTE 1611.2; neerlegging 19.06.2026; "
                "same zetel Integro; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_stijn_jr2025_cw_nl",
            "title": "Companyweb NL Stijn VZW YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0439452461",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2179; YE2025 bruto JUMP 128036084 omzet 22746378 pnl DROP 5079250 "
                "equity JUMP 59569328 FTE 1611.2; neerlegging 19.06.2026; "
                "raw docs/doge/data/raw/tick2179/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Stijn VZW YE2025 statutory",
            "url": "https://www.companyweb.be/en/0439452461",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2179; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; "
                "Turnover 22746378 Gross margin 128036084 Profit/Loss 5079250 Equity 59569328 Employees 1611.2"
            ),
        },
        {
            "source_id": "src_stijn_jr2025_cw_fr",
            "title": "Companyweb FR Stijn VZW YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0439452461",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2179; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_stijn_kbo_2179",
            "title": "KBO Stijn VZW 0439.452.461 Actief Hasselt aanbestedende 36 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0439452461",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2179; Actief VZW; Kempische steenweg 555 3500 Hasselt; 36 VE; "
                "aanbestedende overheid; RSZ NACE 88.104; KBO email empty"
            ),
        },
        {
            "source_id": "src_stijn_foi_contact_2179",
            "title": "Stijn VZW FOI channel info@stijn.be",
            "url": "https://www.stijn.be/nl_BE/contact",
            "publisher": "Stijn VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2179; info@stijn.be; T 011 198 900; Kempische steenweg 555 3500 Hasselt",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_stijn_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "128036084",
            "amount_min_eur": "128036084",
            "amount_max_eur": "128036084",
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (primary subsidy envelope)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2179; Medium CW; bruto JUMP +6.74% vs YE2024 119951369; bruto≫omzet",
        },
        {
            "budget_id": "bud_stijn_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "22746378",
            "amount_min_eur": "22746378",
            "amount_max_eur": "22746378",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2179; Medium CW; omzet JUMP +2.79% vs YE2024 22129604",
        },
        {
            "budget_id": "bud_stijn_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "5079250",
            "amount_min_eur": "5079250",
            "amount_max_eur": "5079250",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2179; Medium CW; pnl DROP -8.9% vs YE2024 5575225",
        },
        {
            "budget_id": "bud_stijn_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "59569328",
            "amount_min_eur": "59569328",
            "amount_max_eur": "59569328",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2179; Medium CW; equity JUMP +6.73% vs YE2024 55814912",
        },
        {
            "budget_id": "bud_stijn_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1611.2",
            "amount_min_eur": "1611.2",
            "amount_max_eur": "1611.2",
            "basis": "CW social-balance FTE / Employees 1611.2",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2179; Medium CW; FTE 1611.2 vs YE2024 1615; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Stijn VZW YE2025 leftover dual "
                "(bruto JUMP 128m / omzet 22.7m / pnl DROP 5.08m)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "adults with disabilities / VAPH clients Limburg+ multi-site",
            "legal_basis": (
                "VZW disability care (KBO 0439.452.461; Actief; 36 VE; NACE 88.104; "
                "aanbestedende overheid)"
            ),
            "decision_date": "2026-06-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "128036084",
            "cash_by_year": (
                '{"2025_bruto":128036084,"2025_omzet":22746378,"2025_pnl":5079250,"2025_equity":59569328,'
                '"2025_fte":1611.2,"2024_bruto":119951369,"2024_omzet":22129604,"2024_pnl":5575225,'
                '"2024_equity":55814912,"2024_fte":1615}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0439452461",
            "stated_goal": "Day centres / residential disability care (VAPH path)",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose VAPH/PVF/RIZIV matrix behind bruto≫omzet; "
                "map Integro same-zetel relation"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Stijn>JR2025_statutory_L5",
            "notes": (
                "tick2179; Medium CW; bruto primary envelope (VAPH-subsidy inflated); omzet 22.7m; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive; "
                "DISTINCT Integro same address; named FREE after Waak"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Stijn bruto JUMP 128m ≫ omzet 22.7m / pnl DROP 5.08m (YE2025)",
            "level": "L5",
            "type": "disability_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Stijn>JR2025",
            "annual_cost_eur": "128036084",
            "total_cost_eur": "128036084",
            "tco_notes": (
                "CW bruto JUMP envelope 128.0m ≫ omzet 22.7m (×5.6); pnl DROP 5.08m; equity 59.6m; "
                "FTE 1611; 36 VE; VAPH/PVF subsidy opacity; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "adults with disabilities / VAPH clients multi-site",
            "stated_goal": "Day centres / residential disability care",
            "measured_outcome": "bruto JUMP +6.7%; omzet JUMP +2.8%; pnl DROP -8.9%; FTE flat 1611",
            "absurdity_score": "7.8",
            "cost_score": "8.2",
            "difficulty": "3.5",
            "priority_index": "7.4",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose VAPH/PVF/RIZIV/gemeente split "
                "behind bruto≫omzet; map Integro same-zetel + 36 VE matrix"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2179; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "named FREE after Waak; EVERY-10 next 2180"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>Stijn>NBB_PDF_assets_debt_bruto_vaph",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR128.0m ≫ omzet EUR22.7m VAPH/PVF/RIZIV/gemeente/provincie matrix; "
                "pnl DROP EUR5.08m path; related-party vs Integro same zetel Kempische steenweg 555; "
                "per-VE bedden/dagcentra + FTE 1611 split across 36 VE"
            ),
            "why_it_matters": (
                "Medium CW shows major Hasselt disability-care VZW with EUR128m bruto vs only EUR22.7m omzet "
                "and EUR5.1m pnl — VAPH subsidy stack opacity; balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Stijn VZW",
            "recipient_email": "info@stijn.be",
            "recipient_postal": "Kempische steenweg 555, 3500 Hasselt",
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
            "notes": "tick2179; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2179")
