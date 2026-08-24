# tick 2181 — MAAAT Aalst YE2025 Medium CW after WAAK SW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T06:20:00Z"
ENTITY = "vzw_maaat_aalst"
GAP = "gap_maaat_nbb_pdf_assets_debt_pnl_jump_omzet_drop_bruto_gt_omzet_matrix_l5"
COMM = "comm_maaat_jr2025_statutory_maatwerk_pnl_jump_omzet_drop"
LB = "lb_maaat_pnl_jump_1_79m_omzet_drop_bruto_gt_omzet_jr2025"
SRC_EN = "src_maaat_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2181":
            row = dict(row)
            row["title"] = (
                "leftover dual — MAAAT Aalst YE2025 Medium "
                "(pnl JUMP 1.79m / omzet DROP 3.65m / bruto>omzet)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover MAAAT after WAAK SW; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2181 MAAAT 0407.766.422 Medium; omzet DROP 3645749 bruto 6595759 "
                "pnl JUMP 1785300 equity JUMP 11278293 FTE 186.8; NACE 88.993; 1 VE Aalst; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2182; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2182" for x in out):
        out.append(
            {
                "task_id": "rq_2182",
                "title": (
                    "leftover dual hole-fill after MAAAT — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2182 after MAAAT Aalst YE2025 Medium (pnl JUMP 1.79m / omzet DROP 3.65m / "
                    "bruto>omzet). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo MAAAT/WAAK SW/"
                    "Waak/Stijn/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2181 MAAAT; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2182")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2181=done")


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
        "last_unit_id": "rq_2181",
        "ticks_completed": "2181",
        "paused": "no",
        "notes": (
            "tick2181 leftover MAAAT 0407.766.422 Medium (omzet DROP 3.65m; bruto 6.60m ≫ omzet; "
            "pnl JUMP 1.79m >1000%; equity JUMP 11.28m; FTE 186.8; NACE 88.993; 1 VE Aalst); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2182; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2181")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "MAAAT VZW (Aalst / maatwerk)",
            "name_fr": "MAAAT ASBL (Alost / travail adapté)",
            "name_en": "MAAAT non-profit (Aalst / sheltered workshop)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.maaat.be",
            "foi_email": "info@maaat.be",
            "foi_postal": "Wijngaardveld 7, 9300 Aalst",
            "notes": (
                "tick2181 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.766.422 Actief VZW 1 VE "
                "NACE 88.993; omzet DROP 3645749 bruto 6595759 (≫omzet) pnl JUMP 1785300 (>1000%) "
                "equity JUMP 11278293 FTE 186.8; neerlegging 16.06.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_maaat_jr2025_cw_nl",
            "title": "Companyweb NL MAAAT YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407766422/maaat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2181; YE2025 omzet DROP 3645749 bruto 6595759 pnl JUMP 1785300 "
                "equity JUMP 11278293 FTE 186.8; neerlegging 16.06.2026; "
                "raw docs/doge/data/raw/tick2181/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN MAAAT YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407766422/maaat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2181; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; "
                "Turnover 3645749 Profit/Loss 1785300 Equity 11278293 Employees 186.8"
            ),
        },
        {
            "source_id": "src_maaat_jr2025_cw_fr",
            "title": "Companyweb FR MAAAT YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407766422",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2181; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_maaat_kbo_2181",
            "title": "KBO MAAAT 0407.766.422 Actief VZW Aalst",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407766422",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2181; Actief VZW; Wijngaardveld 7 9300 Aalst; 1 VE; NACE 88.993; "
                "dagelijks bestuur Johan Delauw sinds 06.05.2026; KBO email empty"
            ),
        },
        {
            "source_id": "src_maaat_foi_contact_2181",
            "title": "MAAAT FOI channel info@maaat.be",
            "url": "https://www.maaat.be/nl",
            "publisher": "MAAAT VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2181; info@maaat.be; +32 53 70 14 24; Wijngaardveld 7 9300 Aalst",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_maaat_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "3645749",
            "amount_min_eur": "3645749",
            "amount_max_eur": "3645749",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2181; Medium CW; omzet DROP -12.16% vs YE2024 4150649",
        },
        {
            "budget_id": "bud_maaat_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "6595759",
            "amount_min_eur": "6595759",
            "amount_max_eur": "6595759",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2181; Medium CW; bruto DROP -1.54% vs YE2024 6699158; bruto≫omzet",
        },
        {
            "budget_id": "bud_maaat_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1785300",
            "amount_min_eur": "1785300",
            "amount_max_eur": "1785300",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2181; Medium CW; pnl JUMP >1000% vs YE2024 83141",
        },
        {
            "budget_id": "bud_maaat_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "11278293",
            "amount_min_eur": "11278293",
            "amount_max_eur": "11278293",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2181; Medium CW; equity JUMP +18.7% vs YE2024 9501769",
        },
        {
            "budget_id": "bud_maaat_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "186.8",
            "amount_min_eur": "186.8",
            "amount_max_eur": "186.8",
            "basis": "CW social-balance FTE / Employees 186.8",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2181; Medium CW; FTE 186.8 vs YE2024 184.5; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "MAAAT Aalst YE2025 leftover dual "
                "(pnl JUMP 1.79m / omzet DROP 3.65m / bruto>omzet)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Oost-Vlaanderen Aalst",
            "legal_basis": "VZW maatwerk (KBO 0407.766.422; Actief; 1 VE; NACE 88.993)",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "3645749",
            "cash_by_year": (
                '{"2025_omzet":3645749,"2025_bruto":6595759,"2025_pnl":1785300,"2025_equity":11278293,'
                '"2025_fte":186.8,"2024_omzet":4150649,"2024_bruto":6699158,"2024_pnl":83141,'
                '"2024_equity":9501769,"2024_fte":184.5}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407766422/maaat",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "explain pnl JUMP >1000% with omzet DROP"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MAAAT>JR2025_statutory_L5",
            "notes": (
                "tick2181; Medium CW; omzet primary envelope; pnl JUMP primary absurdity; bruto≫omzet; "
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
            "name": "MAAAT pnl JUMP 1.79m / omzet DROP 3.65m / bruto>omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MAAAT>JR2025",
            "annual_cost_eur": "3645749",
            "total_cost_eur": "3645749",
            "tco_notes": (
                "CW omzet DROP envelope 3.65m / bruto 6.60m ≫ omzet / pnl JUMP 1.79m (>1000%) / "
                "equity JUMP 11.28m / FTE 186.8; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Oost-Vlaanderen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet DROP -12.2%; bruto DROP -1.5%; pnl JUMP >1000%; equity JUMP +18.7%",
            "absurdity_score": "7.0",
            "cost_score": "4.2",
            "difficulty": "3.0",
            "priority_index": "5.6",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF split; "
                "explain pnl JUMP vs omzet DROP"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2181; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "maatwerk dual after Waak stack"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Aalst>MAAAT>NBB_PDF_assets_debt_pnl_jump",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl JUMP EUR1.785m (>1000% vs YE2024 EUR83k) recon with omzet DROP -12%; "
                "bruto EUR6.60m ≫ omzet EUR3.65m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "non-recurring/herwaardering one-offs"
            ),
            "why_it_matters": (
                "Medium CW shows Aalst maatwerk VZW with pnl JUMP to EUR1.79m while omzet DROPs "
                "and bruto stays subsidy-inflated — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "MAAAT VZW",
            "recipient_email": "info@maaat.be",
            "recipient_postal": "Wijngaardveld 7, 9300 Aalst",
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
            "notes": "tick2181; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2181")
