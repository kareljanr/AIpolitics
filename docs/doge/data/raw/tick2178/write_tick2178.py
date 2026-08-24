# tick 2178 — Waak Maatwerk YE2025 Medium CW after Stroom/Creat
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T05:20:00Z"
ENTITY = "vzw_waak_maatwerk"
GAP = "gap_waak_nbb_pdf_assets_debt_pnl_loss_bruto_gt_omzet_fte_drop_matrix_l5"
COMM = "comm_waak_jr2025_statutory_maatwerk_omzet_jump_pnl_loss_bruto_gt_omzet"
LB = "lb_waak_omzet_jump_37_7m_pnl_loss_bruto_gt_omzet_fte_drop_jr2025"
SRC_EN = "src_waak_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2178":
            row = dict(row)
            row["title"] = (
                "leftover dual — Waak Maatwerk YE2025 Medium "
                "(omzet JUMP 37.7m / pnl LOSS -387k / bruto>omzet / FTE DROP)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Waak after Stroom/Creat; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2178 Waak 0439.993.582 Medium; omzet JUMP 37663381 bruto 55169684 "
                "pnl LOSS -386787 equity DROP 44039284 FTE DROP 1592.1; NACE 88.993; 3 VE; "
                "Stijn FREE deferred; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2179; next every-10 2180"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2179" for x in out):
        out.append(
            {
                "task_id": "rq_2179",
                "title": (
                    "leftover dual hole-fill after Waak — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Stijn-or-unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2179 after Waak Maatwerk YE2025 Medium (omzet JUMP 37.7m / pnl LOSS -387k / "
                    "bruto>omzet / FTE DROP). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
                    "NBB YE2025, else AIESH/REW if YE2025, else FREE Stijn 0439.452.461 if still unused, "
                    "else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo Waak/Stroom/Springplank/Creat CV/"
                    "Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2178 Waak; FARO/AIESH/REW still YE2024; Stijn FREE; next every-10 2180",
            }
        )
        print("SPAWN rq_2179")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2178=done")


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
        "last_unit_id": "rq_2178",
        "ticks_completed": "2178",
        "paused": "no",
        "notes": (
            "tick2178 leftover WAAK 0439.993.582 Medium (omzet JUMP 37.7m; bruto 55.2m ≫ omzet; "
            "pnl LOSS -387k DEEPER; equity DROP 44.0m; FTE DROP 1592; NACE 88.993; 3 VE Kuurne); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Stijn FREE deferred; "
            "next rq_2179; next every-10 2180; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2178")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Waak Maatwerkbedrijf VZW (Kuurne)",
            "name_fr": "Waak entreprise de travail adapté ASBL (Kuurne)",
            "name_en": "Waak sheltered workshop non-profit (Kuurne)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.waak.be",
            "foi_email": "info@waak.be",
            "foi_postal": "Heirweg 125, 8520 Kuurne",
            "notes": (
                "tick2178 YE2025 Medium CW NL+EN+FR + Strong KBO 0439.993.582 Actief VZW 3 VE "
                "NACE 88.993; omzet JUMP 37663381 bruto JUMP 55169684 (≫omzet) pnl LOSS -386787 "
                "equity DROP 44039284 FTE DROP 1592.1; neerlegging 15.05.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Stijn FREE deferred; "
                "not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_waak_jr2025_cw_nl",
            "title": "Companyweb NL Waak Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0439993582",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2178; YE2025 omzet JUMP 37663381 bruto 55169684 pnl LOSS -386787 "
                "equity DROP 44039284 FTE DROP 1592.1; neerlegging 15.05.2026; "
                "raw docs/doge/data/raw/tick2178/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Waak Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/en/0439993582",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2178; EN mirror YE2025 Medium; filed 15-05-2026; Last balance sheet year 2025; "
                "Turnover 37663381 Profit/Loss -386787 Equity 44039284 Employees 1592.1"
            ),
        },
        {
            "source_id": "src_waak_jr2025_cw_fr",
            "title": "Companyweb FR Waak Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0439993582",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2178; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_waak_kbo_2178",
            "title": "KBO Waak Maatwerkbedrijf 0439.993.582 Actief VZW Kuurne",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0439993582",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2178; Actief VZW; Heirweg 125 8520 Kuurne; 3 VE; NACE 88.993; "
                "gedelegeerd Tim Vannieuwenhuyse; KBO email empty"
            ),
        },
        {
            "source_id": "src_waak_foi_contact_2178",
            "title": "Waak Maatwerk FOI channel info@waak.be",
            "url": "https://www.waak.be/nl/contact",
            "publisher": "Waak Maatwerkbedrijf VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2178; info@waak.be; +32 56 36 34 34; Heirweg 125 8520 Kuurne",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_waak_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "37663381",
            "amount_min_eur": "37663381",
            "amount_max_eur": "37663381",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2178; Medium CW; omzet JUMP +3.04% vs YE2024 36553945",
        },
        {
            "budget_id": "bud_waak_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "55169684",
            "amount_min_eur": "55169684",
            "amount_max_eur": "55169684",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2178; Medium CW; bruto JUMP +9.97% vs YE2024 50166860; bruto≫omzet",
        },
        {
            "budget_id": "bud_waak_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "-386787",
            "amount_min_eur": "-386787",
            "amount_max_eur": "-386787",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2178; Medium CW; pnl DEEPER LOSS vs YE2024 -363789",
        },
        {
            "budget_id": "bud_waak_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "44039284",
            "amount_min_eur": "44039284",
            "amount_max_eur": "44039284",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2178; Medium CW; equity DROP -1.11% vs YE2024 44534261",
        },
        {
            "budget_id": "bud_waak_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1592.1",
            "amount_min_eur": "1592.1",
            "amount_max_eur": "1592.1",
            "basis": "CW social-balance FTE / Employees 1592.1",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2178; Medium CW; FTE DROP vs YE2024 1643.2; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Waak Maatwerk YE2025 leftover dual "
                "(omzet JUMP 37.7m / pnl LOSS -387k / bruto>omzet / FTE DROP)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients West-Vlaanderen Kuurne",
            "legal_basis": "VZW maatwerk (KBO 0439.993.582; Actief; 3 VE; NACE 88.993)",
            "decision_date": "2026-05-15",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "37663381",
            "cash_by_year": (
                '{"2025_omzet":37663381,"2025_bruto":55169684,"2025_pnl":-386787,"2025_equity":44039284,'
                '"2025_fte":1592.1,"2024_omzet":36553945,"2024_bruto":50166860,"2024_pnl":-363789,'
                '"2024_equity":44534261,"2024_fte":1643.2}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0439993582",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie/GESCO/ESF matrix behind "
                "bruto≫omzet; explain DEEPER LOSS + FTE DROP"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>JR2025_statutory_L5",
            "notes": (
                "tick2178; Medium CW; omzet primary envelope; bruto≫omzet wage-cost subsidies opaque; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive; "
                "Stijn 0439.452.461 FREE deferred"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Waak omzet JUMP 37.7m / pnl LOSS -387k / bruto>omzet / FTE DROP (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>JR2025",
            "annual_cost_eur": "37663381",
            "total_cost_eur": "37663381",
            "tco_notes": (
                "CW omzet JUMP envelope 37.7m / bruto 55.2m ≫ omzet / pnl LOSS -387k DEEPER / "
                "equity 44.0m / FTE DROP 1592; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers West-Vlaanderen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +3.0%; bruto JUMP +10.0%; pnl DEEPER LOSS; FTE DROP -3.1%",
            "absurdity_score": "6.5",
            "cost_score": "6.8",
            "difficulty": "3.5",
            "priority_index": "6.4",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF/"
                "gemeente/provincie split behind bruto≫omzet; explain LOSS + FTE DROP"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2178; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "named FREE after Stroom"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Kuurne>Waak>NBB_PDF_assets_debt_pnl_loss",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR55.17m ≫ omzet EUR37.66m loonkostsubsidie/GESCO/ESF/VDAB/gemeente/provincie matrix; "
                "pnl DEEPER LOSS EUR-386787 path; FTE DROP 1643→1592 recon; "
                "related-party vs Stroom/Springplank/Stijn maatwerk"
            ),
            "why_it_matters": (
                "Medium CW shows major Kuurne maatwerk VZW with EUR37.7m omzet, EUR55.2m bruto "
                "(subsidy-inflated) and deepening LOSS while shedding FTE — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Waak Maatwerkbedrijf VZW",
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
            "notes": "tick2178; ready NOT sent; Medium CW + Strong KBO; Stijn FREE deferred; next every-10 2180",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2178")
