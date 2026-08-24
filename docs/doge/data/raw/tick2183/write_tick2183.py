# tick 2183 — Wase Werkplaats YE2025 Medium CW after Groep INTRO Maatwerk
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T07:00:00Z"
ENTITY = "vzw_wase_werkplaats"
GAP = "gap_wase_werkplaats_nbb_pdf_assets_debt_pnl_loss_bruto_gt_omzet_fte_jump_matrix_l5"
COMM = "comm_wase_werkplaats_jr2025_statutory_omzet_jump_bruto_gt_omzet_pnl_loss"
LB = "lb_wase_werkplaats_omzet_jump_13_06m_bruto_28m_pnl_loss_improving_jr2025"
SRC_EN = "src_wase_werkplaats_jr2025_cw_en"


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
                "leftover dual — Wase Werkplaats YE2025 Medium "
                "(omzet JUMP 13.06m / bruto 28.0m ≫ omzet / pnl LOSS improving / FTE JUMP)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Wase Werkplaats after Groep INTRO; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2183 Wase Werkplaats 0406.769.993 Medium; omzet JUMP 13059679 bruto 27984893 "
                "pnl LOSS improving -465728 equity DROP 10625410 FTE JUMP 761.6; 4 VE Temse; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2184; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2184" for x in out):
        out.append(
            {
                "task_id": "rq_2184",
                "title": (
                    "leftover dual hole-fill after Wase Werkplaats — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2184 after Wase Werkplaats YE2025 Medium (omzet JUMP 13.06m / bruto 28m ≫ "
                    "omzet / pnl LOSS improving). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if "
                    "TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo "
                    "Wase Werkplaats/Groep INTRO Maatwerk/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank/"
                    "Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2183 Wase Werkplaats; FARO/AIESH/REW still YE2024; next every-10 2190",
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
            "tick2183 leftover WASE WERKPLAATS 0406.769.993 Medium (omzet JUMP 13.06m; "
            "bruto 28.0m ≫ omzet; pnl LOSS improving -466k; equity DROP 10.63m; FTE JUMP 761.6; 4 VE Temse); "
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
            "name_nl": "Wase Werkplaats VZW (Temse / maatwerk)",
            "name_fr": "Wase Werkplaats ASBL (Temse / travail adapté)",
            "name_en": "Wase Werkplaats non-profit (Temse / sheltered workshop)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.wasewerkplaats.be",
            "foi_email": "boekhouding@wasewerkplaats.be",
            "foi_postal": "Kapelanielaan 20, 9140 Temse",
            "notes": (
                "tick2183 YE2025 Medium CW NL+EN+FR + Strong KBO 0406.769.993 Actief VZW 4 VE "
                "RSZ NACE 88.993; omzet JUMP 13059679 bruto JUMP 27984893 (≫omzet) pnl LOSS improving "
                "-465728 equity DROP 10625410 FTE JUMP 761.6; neerlegging 19.06.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_wase_werkplaats_jr2025_cw_nl",
            "title": "Companyweb NL Wase Werkplaats YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0406769993/wase-werkplaats",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2183; YE2025 omzet JUMP 13059679 bruto 27984893 pnl LOSS improving -465728 "
                "equity DROP 10625410 FTE JUMP 761.6; neerlegging 19.06.2026; "
                "raw docs/doge/data/raw/tick2183/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Wase Werkplaats YE2025 statutory",
            "url": "https://www.companyweb.be/en/0406769993/wase-werkplaats",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2183; EN mirror YE2025 Medium; filed 19-06-2026; Last balance sheet year 2025; "
                "Turnover 13059679 Profit/Loss -465728 Equity 10625410 Employees 761.6"
            ),
        },
        {
            "source_id": "src_wase_werkplaats_jr2025_cw_fr",
            "title": "Companyweb FR Wase Werkplaats YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0406769993/wase-werkplaats",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2183; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_wase_werkplaats_kbo_2183",
            "title": "KBO Wase Werkplaats 0406.769.993 Actief VZW Temse 4 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406769993",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2183; Actief VZW; Kapelanielaan 20 9140 Temse; 4 VE; RSZ NACE 88.993; "
                "aannemer erkenning; KBO email empty"
            ),
        },
        {
            "source_id": "src_wase_werkplaats_foi_contact_2183",
            "title": "Wase Werkplaats FOI channel boekhouding@wasewerkplaats.be",
            "url": "https://www.wasewerkplaats.be/nl/contact",
            "publisher": "Wase Werkplaats",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": (
                "tick2183; boekhouding@wasewerkplaats.be; also info@wasewerkplaats.be (Sociale Kaart); "
                "+32 3 710 95 12; Kapelanielaan 20 9140 Temse"
            ),
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_wase_werkplaats_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "13059679",
            "amount_min_eur": "13059679",
            "amount_max_eur": "13059679",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; omzet JUMP +7.58% vs YE2024 12139158",
        },
        {
            "budget_id": "bud_wase_werkplaats_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "27984893",
            "amount_min_eur": "27984893",
            "amount_max_eur": "27984893",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; bruto JUMP +7.68% vs YE2024 25989822; bruto≫omzet",
        },
        {
            "budget_id": "bud_wase_werkplaats_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "-465728",
            "amount_min_eur": "-465728",
            "amount_max_eur": "-465728",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; pnl LOSS improving 68.1% vs YE2024 -1459915",
        },
        {
            "budget_id": "bud_wase_werkplaats_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "10625410",
            "amount_min_eur": "10625410",
            "amount_max_eur": "10625410",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; equity DROP -3.93% vs YE2024 11059719",
        },
        {
            "budget_id": "bud_wase_werkplaats_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "761.6",
            "amount_min_eur": "761.6",
            "amount_max_eur": "761.6",
            "basis": "CW social-balance FTE / Employees 761.6",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2183; Medium CW; FTE JUMP vs YE2024 743.2; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Wase Werkplaats YE2025 leftover dual "
                "(omzet JUMP 13.06m / bruto 28m ≫ omzet / pnl LOSS improving)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Waasland multi-site",
            "legal_basis": "VZW maatwerk (KBO 0406.769.993; Actief; 4 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "13059679",
            "cash_by_year": (
                '{"2025_omzet":13059679,"2025_bruto":27984893,"2025_pnl":-465728,"2025_equity":10625410,'
                '"2025_fte":761.6,"2024_omzet":12139158,"2024_bruto":25989822,"2024_pnl":-1459915,'
                '"2024_equity":11059719,"2024_fte":743.2}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0406769993/wase-werkplaats",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "map multi-year loss path despite FTE JUMP"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Waasland>Temse>WaseWerkplaats>JR2025_statutory_L5",
            "notes": (
                "tick2183; Medium CW; omzet primary envelope; bruto≫omzet; pnl LOSS improving; "
                "FTE JUMP with equity DROP; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Wase Werkplaats omzet JUMP 13.06m / bruto 28m ≫ omzet / pnl LOSS improving (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Waasland>Temse>WaseWerkplaats>JR2025",
            "annual_cost_eur": "13059679",
            "total_cost_eur": "13059679",
            "tco_notes": (
                "CW omzet JUMP envelope 13.06m / bruto 28.0m ≫ omzet / pnl LOSS improving -466k / "
                "equity DROP 10.63m / FTE JUMP 761.6; 4 VE; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Waasland / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +7.6%; bruto JUMP +7.7%; pnl LOSS improving 68%; equity DROP; FTE JUMP",
            "absurdity_score": "6.4",
            "cost_score": "5.6",
            "difficulty": "3.0",
            "priority_index": "6.0",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/VDAB/ESF split; "
                "map multi-year loss + FTE JUMP path"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2183; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Waasland maatwerk dual after Groep INTRO"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Waasland>Temse>WaseWerkplaats>NBB_PDF_assets_debt_bruto",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR28.0m ≫ omzet EUR13.06m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "multi-year pnl LOSS path (-1.46m YE2024 → -0.47m YE2025) with FTE JUMP 743.2→761.6; "
                "equity DROP path; per-VE / top-10 opdrachtgevers + aannemer recognition residual"
            ),
            "why_it_matters": (
                "Medium CW shows large Waasland maatwerk VZW with EUR13.06m omzet, subsidy-inflated bruto "
                "EUR28.0m, persistent LOSS despite FTE JUMP — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Wase Werkplaats VZW",
            "recipient_email": "boekhouding@wasewerkplaats.be",
            "recipient_postal": "Kapelanielaan 20, 9140 Temse",
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
