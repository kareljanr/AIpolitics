# tick 2185 — Weerwerk Gent YE2025 Medium CW after InterWest/Westlandia
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T07:40:00Z"
ENTITY = "vzw_weerwerk_gent"
GAP = "gap_weerwerk_nbb_pdf_assets_debt_bruto_gt_omzet_equity_jump_matrix_l5"
COMM = "comm_weerwerk_jr2025_statutory_maatwerk_omzet_jump_equity_jump"
LB = "lb_weerwerk_omzet_jump_5_54m_pnl_jump_197k_bruto_gt_omzet_jr2025"
SRC_EN = "src_weerwerk_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2185":
            row = dict(row)
            row["title"] = (
                "leftover dual — Weerwerk Gent YE2025 Medium "
                "(omzet JUMP 5.54m / pnl JUMP 197k / bruto>omzet / equity JUMP)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Weerwerk after InterWest/Westlandia; preferred AGB Bornem JR2024 / "
                "FARO still YE2024 CW / AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
                "FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2185 Weerwerk 0465.104.904 Medium; omzet JUMP 5535667 bruto 9125341 "
                "pnl JUMP 197410 equity JUMP 1841558 FTE JUMP 205.3; 3 VE Gent; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2186; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2186" for x in out):
        out.append(
            {
                "task_id": "rq_2186",
                "title": (
                    "leftover dual hole-fill after Weerwerk — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2186 after Weerwerk Gent YE2025 Medium (omzet JUMP 5.54m / pnl JUMP 197k / "
                    "bruto>omzet / equity JUMP +38.5%). Prefer leftover AGB/APB if JR2025 PDF live, else "
                    "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. "
                    "Do NOT redo Weerwerk/Westlandia/InterWest/Wase Werkplaats/BWB/Groep INTRO Maatwerk/"
                    "MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/"
                    "Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2185 Weerwerk; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2186")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2185=done")


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
        "last_unit_id": "rq_2185",
        "ticks_completed": "2185",
        "paused": "no",
        "notes": (
            "tick2185 leftover WEERWERK 0465.104.904 Medium (omzet JUMP 5.54m; bruto 9.13m ≫ omzet; "
            "pnl JUMP 197k +168.9%; equity JUMP 1.84m +38.5%; FTE JUMP 205.3; 3 VE Gent); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2186; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2185")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Weerwerk VZW (Gent)",
            "name_fr": "Weerwerk ASBL (Gand)",
            "name_en": "Weerwerk sheltered workshop non-profit (Ghent)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://weerwerk.be",
            "foi_email": "info@weerwerk.be",
            "foi_postal": "Gaardeniersweg 80, 9000 Gent",
            "notes": (
                "tick2185 YE2025 Medium CW NL+EN+FR + Strong KBO 0465.104.904 Actief VZW 3 VE "
                "RSZ NACE 88.993; omzet JUMP 5535667 bruto 9125341 (≫omzet) pnl JUMP 197410 "
                "equity JUMP 1841558 FTE JUMP 205.3; neerlegging 03.07.2026; "
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
            "source_id": "src_weerwerk_jr2025_cw_nl",
            "title": "Companyweb NL Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0465104904/weerwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2185; YE2025 omzet JUMP 5535667 bruto 9125341 pnl JUMP 197410 "
                "equity JUMP 1841558 FTE JUMP 205.3; neerlegging 03.07.2026; "
                "raw docs/doge/data/raw/tick2185/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0465104904/weerwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2185; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; "
                "Turnover 5535667 Profit/Loss 197410 Equity 1841558 Employees 205.3"
            ),
        },
        {
            "source_id": "src_weerwerk_jr2025_cw_fr",
            "title": "Companyweb FR Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0465104904",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2185; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_weerwerk_kbo_2185",
            "title": "KBO Weerwerk 0465.104.904 Actief VZW Gent 3 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465104904",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2185; Actief VZW; Gaardeniersweg 80 9000 Gent; 3 VE; RSZ NACE 88.993 "
                "Beschutte en sociale werkplaatsen; KBO email empty"
            ),
        },
        {
            "source_id": "src_weerwerk_foi_contact_2185",
            "title": "Weerwerk FOI channel info@weerwerk.be",
            "url": "https://weerwerk.be/contact/",
            "publisher": "Weerwerk VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2185; info@weerwerk.be; Gaardeniersweg 80 9000 Gent; BE 0465.104.904",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_weerwerk_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "5535667",
            "amount_min_eur": "5535667",
            "amount_max_eur": "5535667",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2185; Medium CW; omzet JUMP +2.39% vs YE2024 5406622",
        },
        {
            "budget_id": "bud_weerwerk_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "9125341",
            "amount_min_eur": "9125341",
            "amount_max_eur": "9125341",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2185; Medium CW; bruto JUMP +4.79% vs YE2024 8708583; bruto≫omzet",
        },
        {
            "budget_id": "bud_weerwerk_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "197410",
            "amount_min_eur": "197410",
            "amount_max_eur": "197410",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2185; Medium CW; pnl JUMP +168.9% vs YE2024 73414",
        },
        {
            "budget_id": "bud_weerwerk_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1841558",
            "amount_min_eur": "1841558",
            "amount_max_eur": "1841558",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2185; Medium CW; equity JUMP +38.53% vs YE2024 1329384",
        },
        {
            "budget_id": "bud_weerwerk_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "205.3",
            "amount_min_eur": "205.3",
            "amount_max_eur": "205.3",
            "basis": "CW social-balance FTE / Employees 205.3",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2185; Medium CW; FTE JUMP vs YE2024 200.4; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Weerwerk Gent YE2025 leftover dual "
                "(omzet JUMP 5.54m / pnl JUMP 197k / bruto>omzet)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Gent-Oost-Vlaanderen",
            "legal_basis": "VZW maatwerk (KBO 0465.104.904; Actief; 3 VE; RSZ NACE 88.993)",
            "decision_date": "2026-07-03",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "5535667",
            "cash_by_year": (
                '{"2025_omzet":5535667,"2025_bruto":9125341,"2025_pnl":197410,"2025_equity":1841558,'
                '"2025_fte":205.3,"2024_omzet":5406622,"2024_bruto":8708583,"2024_pnl":73414,'
                '"2024_equity":1329384,"2024_fte":200.4}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0465104904/weerwerk",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie matrix behind bruto≫omzet; "
                "explain equity JUMP +38.5% path"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>JR2025_statutory_L5",
            "notes": (
                "tick2185; Medium CW; omzet primary envelope; bruto≫omzet + equity JUMP primary absurdity; "
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
            "name": "Weerwerk omzet JUMP 5.54m / pnl JUMP 197k / bruto≫omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>JR2025",
            "annual_cost_eur": "5535667",
            "total_cost_eur": "5535667",
            "tco_notes": (
                "CW omzet JUMP envelope 5.54m / bruto 9.13m ≫ omzet / pnl JUMP 197k +168.9% / "
                "equity JUMP 1.84m +38.5% / FTE JUMP 205.3; wage-cost subsidies opaque; "
                "assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Gent / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +2.4%; bruto JUMP +4.8%; pnl JUMP +169%; equity JUMP +38.5%; FTE JUMP +2.4%",
            "absurdity_score": "6.2",
            "cost_score": "4.8",
            "difficulty": "3.0",
            "priority_index": "5.2",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF split "
                "behind bruto≫omzet; equity JUMP recon"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2185; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Gent maatwerk dual deferred from Westlandia tick"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR9.13m ≫ omzet EUR5.54m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "equity JUMP EUR1.33m→1.84m (+38.5%) recon; "
                "FTE JUMP 200.4→205.3 path; related-party vs other Gent maatwerk if any"
            ),
            "why_it_matters": (
                "Medium CW shows Gent maatwerk VZW with bruto nearly 1.65× omzet and equity JUMP +38.5% "
                "while assets/debt unpublished — classic subsidy-inflated envelope opacity"
            ),
            "priority": "8",
            "recipient_body": "WEERWERK VZW",
            "recipient_email": "info@weerwerk.be",
            "recipient_postal": "Gaardeniersweg 80, 9000 Gent",
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
            "notes": "tick2185; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2185")
