# tick 2183 — BWB Londerzeel YE2025 Medium CW after Groep INTRO
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T07:00:00Z"
ENTITY = "vzw_bwb_londerzeel"
GAP = "gap_bwb_nbb_pdf_assets_debt_pnl_drop_omzet_jump_bruto_gt_omzet_matrix_l5"
COMM = "comm_bwb_jr2025_statutory_maatwerk_omzet_jump_pnl_drop"
LB = "lb_bwb_omzet_jump_6_00m_pnl_drop_bruto_gt_omzet_jr2025"
SRC_EN = "src_bwb_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2183":
            row = dict(row)
            row["title"] = (
                "leftover dual — BWB Londerzeel YE2025 Medium "
                "(omzet JUMP 6.00m / pnl DROP -43% / bruto>omzet)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover BWB after Groep INTRO; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2183 BWB 0407.642.104 Medium; omzet JUMP 6000571 bruto 10555433 "
                "pnl DROP 110515 equity JUMP 7121604 FTE JUMP 295.7; NACE 88.993; 1 VE Londerzeel; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2184; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2184" for x in out):
        out.append(
            {
                "task_id": "rq_2184",
                "title": (
                    "leftover dual hole-fill after BWB — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2184 after BWB Londerzeel YE2025 Medium (omzet JUMP 6.00m / pnl DROP -43% / "
                    "bruto>omzet). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo BWB/"
                    "Groep INTRO Maatwerk/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank/Creat CV/"
                    "Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2183 BWB; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2184")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2183=done")


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
        "last_unit_id": "rq_2183",
        "ticks_completed": "2183",
        "paused": "no",
        "notes": (
            "tick2183 leftover BWB 0407.642.104 Medium (omzet JUMP 6.00m; bruto 10.56m ≫ omzet; "
            "pnl DROP 111k -43%; equity JUMP 7.12m; FTE JUMP 295.7; NACE 88.993; 1 VE Londerzeel); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2184; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2183")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "maatWERKbedrijf BWB VZW (Londerzeel / B.W. Bouchout)",
            "name_fr": "maatWERKbedrijf BWB ASBL (Londerzeel / B.W. Bouchout)",
            "name_en": "BWB sheltered workshop non-profit (Londerzeel)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://maatwerkbedrijfbwb.be",
            "foi_email": "info@maatwerkbedrijfbwb.be",
            "foi_postal": "Nijverheidsstraat 15/2, 1840 Londerzeel",
            "notes": (
                "tick2183 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.642.104 Actief VZW 1 VE "
                "NACE 88.993; omzet JUMP 6000571 bruto DROP 10555433 (≫omzet) pnl DROP 110515 "
                "equity JUMP 7121604 FTE JUMP 295.7; neerlegging 21.07.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_bwb_jr2025_cw_nl",
            "title": "Companyweb NL maatWERKbedrijf BWB YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407642104/maatwerkbedrijf-bwb",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2183; YE2025 omzet JUMP 6000571 bruto 10555433 pnl DROP 110515 "
                "equity JUMP 7121604 FTE JUMP 295.7; neerlegging 21.07.2026; "
                "raw docs/doge/data/raw/tick2183/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN maatWERKbedrijf BWB YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407642104/maatwerkbedrijf-bwb",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2183; EN mirror YE2025 Medium; filed 21-07-2026; Last balance sheet year 2025; "
                "Turnover 6000571 Profit/Loss 110515 Equity 7121604 Employees 295.7"
            ),
        },
        {
            "source_id": "src_bwb_jr2025_cw_fr",
            "title": "Companyweb FR maatWERKbedrijf BWB YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407642104",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2183; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_bwb_kbo_2183",
            "title": "KBO maatWERKbedrijf BWB 0407.642.104 Actief VZW Londerzeel",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407642104",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2183; Actief VZW; Nijverheidsstraat 15 bus 2 1840 Londerzeel; 1 VE; "
                "NACE 88.993; afkorting B.W. Bouchout; KBO email empty"
            ),
        },
        {
            "source_id": "src_bwb_foi_contact_2183",
            "title": "BWB FOI channel info@maatwerkbedrijfbwb.be",
            "url": "https://maatwerkbedrijfbwb.be/",
            "publisher": "maatWERKbedrijf BWB VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2183; info@maatwerkbedrijfbwb.be; 052 52 27 00; Nijverheidsstraat 15/2 1840 Londerzeel",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_bwb_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "6000571",
            "amount_min_eur": "6000571",
            "amount_max_eur": "6000571",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; omzet JUMP +6.84% vs YE2024 5616428",
        },
        {
            "budget_id": "bud_bwb_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "10555433",
            "amount_min_eur": "10555433",
            "amount_max_eur": "10555433",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; bruto DROP -2.64% vs YE2024 10841610; bruto≫omzet",
        },
        {
            "budget_id": "bud_bwb_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "110515",
            "amount_min_eur": "110515",
            "amount_max_eur": "110515",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; pnl DROP -43.18% vs YE2024 194484",
        },
        {
            "budget_id": "bud_bwb_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "7121604",
            "amount_min_eur": "7121604",
            "amount_max_eur": "7121604",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; equity JUMP +1.28% vs YE2024 7031483",
        },
        {
            "budget_id": "bud_bwb_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "295.7",
            "amount_min_eur": "295.7",
            "amount_max_eur": "295.7",
            "basis": "CW social-balance FTE / Employees 295.7",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; FTE JUMP vs YE2024 288.5; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "BWB Londerzeel YE2025 leftover dual "
                "(omzet JUMP 6.00m / pnl DROP -43% / bruto>omzet)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Vlaams-Brabant Londerzeel",
            "legal_basis": "VZW maatwerk (KBO 0407.642.104; Actief; 1 VE; NACE 88.993)",
            "decision_date": "2026-07-21",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "6000571",
            "cash_by_year": (
                '{"2025_omzet":6000571,"2025_bruto":10555433,"2025_pnl":110515,"2025_equity":7121604,'
                '"2025_fte":295.7,"2024_omzet":5616428,"2024_bruto":10841610,"2024_pnl":194484,'
                '"2024_equity":7031483,"2024_fte":288.5}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407642104/maatwerkbedrijf-bwb",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "explain pnl DROP with omzet+FTE JUMP"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Londerzeel>BWB>JR2025_statutory_L5",
            "notes": (
                "tick2183; Medium CW; omzet primary envelope; bruto≫omzet; pnl DROP primary absurdity; "
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
            "name": "BWB omzet JUMP 6.00m / pnl DROP -43% / bruto>omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Londerzeel>BWB>JR2025",
            "annual_cost_eur": "6000571",
            "total_cost_eur": "6000571",
            "tco_notes": (
                "CW omzet JUMP envelope 6.00m / bruto 10.56m ≫ omzet / pnl DROP 111k -43% / "
                "equity 7.12m / FTE JUMP 295.7; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Vlaams-Brabant / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +6.8%; bruto DROP -2.6%; pnl DROP -43%; FTE JUMP +2.5%",
            "absurdity_score": "6.0",
            "cost_score": "4.8",
            "difficulty": "3.0",
            "priority_index": "5.4",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF split; "
                "explain pnl DROP with omzet+FTE JUMP"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2183; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "maatwerk dual after Groep INTRO/MAAAT"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Londerzeel>BWB>NBB_PDF_assets_debt_pnl_drop",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl DROP EUR110515 (-43%) vs omzet JUMP +6.84% + FTE JUMP recon; "
                "bruto EUR10.56m ≫ omzet EUR6.00m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "top-10 opdrachtgevers public vs private offtake"
            ),
            "why_it_matters": (
                "Medium CW shows Londerzeel maatwerk VZW with omzet JUMP and FTE JUMP while pnl DROPs "
                "43% under subsidy-inflated bruto — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "maatWERKbedrijf BWB VZW",
            "recipient_email": "info@maatwerkbedrijfbwb.be",
            "recipient_postal": "Nijverheidsstraat 15/2, 1840 Londerzeel",
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
            "notes": "tick2183; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2183")
