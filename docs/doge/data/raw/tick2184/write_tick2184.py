# tick 2184 — InterWest Veurne YE2025 Medium CW after Wase/BWB
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T07:20:00Z"
ENTITY = "vzw_interwest_veurne"
GAP = "gap_interwest_nbb_pdf_assets_debt_pnl_loss_flip_bruto_gt_omzet_fte_drop_matrix_l5"
COMM = "comm_interwest_jr2025_statutory_maatwerk_pnl_loss_flip_omzet_jump"
LB = "lb_interwest_omzet_jump_10_78m_pnl_loss_flip_bruto_gt_omzet_jr2025"
SRC_EN = "src_interwest_jr2025_cw_en"


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
                "leftover dual — InterWest Veurne YE2025 Medium "
                "(omzet JUMP 10.78m / pnl LOSS FLIP -25k from +3.32m)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover InterWest after Wase/BWB; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2184 InterWest 0407.963.885 Medium; omzet JUMP 10780920 bruto 15403841 "
                "pnl LOSS FLIP -25093 vs YE2024 +3319507 equity JUMP 14224725 FTE DROP 425.8; "
                "4 VE Veurne; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2185; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2185" for x in out):
        out.append(
            {
                "task_id": "rq_2185",
                "title": (
                    "leftover dual hole-fill after InterWest — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2185 after InterWest Veurne YE2025 Medium (omzet JUMP 10.78m / pnl LOSS FLIP "
                    "from +3.32m). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ. Do NOT redo InterWest/"
                    "Wase Werkplaats/BWB/Groep INTRO Maatwerk/MAAAT/WAAK SW/Waak/Stijn/Stroom/Springplank/"
                    "Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2184 InterWest; FARO/AIESH/REW still YE2024; next every-10 2190",
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
            "tick2184 leftover INTERWEST 0407.963.885 Medium (omzet JUMP 10.78m; bruto 15.40m ≫ omzet; "
            "pnl LOSS FLIP -25k from YE2024 +3.32m; equity JUMP 14.22m; FTE DROP 425.8; 4 VE Veurne); "
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
            "name_nl": "InterWest / Maatwerkbedrijf Interwest VZW (Veurne)",
            "name_fr": "InterWest / Maatwerkbedrijf Interwest ASBL (Furnes)",
            "name_en": "InterWest sheltered workshop non-profit (Veurne)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://interwest.be",
            "foi_email": "info@interwest.be",
            "foi_postal": "Albert I laan 29, 8630 Veurne",
            "notes": (
                "tick2184 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.963.885 Actief VZW 4 VE "
                "RSZ NACE 88.993; omzet JUMP 10780920 bruto 15403841 (≫omzet) pnl LOSS FLIP -25093 "
                "vs YE2024 +3319507 equity JUMP 14224725 FTE DROP 425.8; neerlegging 16.06.2026; "
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
            "source_id": "src_interwest_jr2025_cw_nl",
            "title": "Companyweb NL InterWest YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407963885/maatwerkbedrijf-interwest",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2184; YE2025 omzet JUMP 10780920 bruto 15403841 pnl LOSS FLIP -25093 "
                "equity JUMP 14224725 FTE DROP 425.8; neerlegging 16.06.2026; "
                "raw docs/doge/data/raw/tick2184/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN InterWest YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407963885/maatwerkbedrijf-interwest",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2184; EN mirror YE2025 Medium; filed 16-06-2026; Last balance sheet year 2025; "
                "Turnover 10780920 Profit/Loss -25093 Equity 14224725 Employees 425.8"
            ),
        },
        {
            "source_id": "src_interwest_jr2025_cw_fr",
            "title": "Companyweb FR InterWest YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407963885",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2184; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_interwest_kbo_2184",
            "title": "KBO InterWest 0407.963.885 Actief VZW Veurne 4 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407963885",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2184; Actief VZW; Albert I laan 29 8630 Veurne; 4 VE; RSZ NACE 88.993; "
                "afkorting InterWest; aannemer; absorbed De IJzer; KBO email empty"
            ),
        },
        {
            "source_id": "src_interwest_foi_contact_2184",
            "title": "InterWest FOI channel info@interwest.be",
            "url": "https://interwest.be",
            "publisher": "Maatwerkbedrijf Interwest VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2184; info@interwest.be; Albert I laan 29 8630 Veurne",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_interwest_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "10780920",
            "amount_min_eur": "10780920",
            "amount_max_eur": "10780920",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; omzet JUMP +3.38% vs YE2024 10428743",
        },
        {
            "budget_id": "bud_interwest_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "15403841",
            "amount_min_eur": "15403841",
            "amount_max_eur": "15403841",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; bruto DROP -1.46% vs YE2024 15632631; bruto≫omzet",
        },
        {
            "budget_id": "bud_interwest_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "-25093",
            "amount_min_eur": "-25093",
            "amount_max_eur": "-25093",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; pnl LOSS FLIP vs YE2024 +3319507",
        },
        {
            "budget_id": "bud_interwest_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "14224725",
            "amount_min_eur": "14224725",
            "amount_max_eur": "14224725",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; equity JUMP +0.67% vs YE2024 14130356",
        },
        {
            "budget_id": "bud_interwest_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "425.8",
            "amount_min_eur": "425.8",
            "amount_max_eur": "425.8",
            "basis": "CW social-balance FTE / Employees 425.8",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2184; Medium CW; FTE DROP vs YE2024 438.9; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "InterWest Veurne YE2025 leftover dual "
                "(omzet JUMP 10.78m / pnl LOSS FLIP -25k from +3.32m)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Westhoek Veurne",
            "legal_basis": "VZW maatwerk (KBO 0407.963.885; Actief; 4 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "10780920",
            "cash_by_year": (
                '{"2025_omzet":10780920,"2025_bruto":15403841,"2025_pnl":-25093,"2025_equity":14224725,'
                '"2025_fte":425.8,"2024_omzet":10428743,"2024_bruto":15632631,"2024_pnl":3319507,'
                '"2024_equity":14130356,"2024_fte":438.9}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407963885/maatwerkbedrijf-interwest",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose why YE2024 EUR3.32m profit FLIPs to LOSS; "
                "loonkostsubsidie matrix behind bruto≫omzet"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Veurne>InterWest>JR2025_statutory_L5",
            "notes": (
                "tick2184; Medium CW; omzet primary envelope; pnl LOSS FLIP primary absurdity; bruto≫omzet; "
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
            "name": "InterWest omzet JUMP 10.78m / pnl LOSS FLIP from +3.32m (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Veurne>InterWest>JR2025",
            "annual_cost_eur": "10780920",
            "total_cost_eur": "10780920",
            "tco_notes": (
                "CW omzet JUMP envelope 10.78m / bruto 15.40m ≫ omzet / pnl LOSS FLIP -25k from YE2024 "
                "+3.32m / equity 14.22m / FTE DROP 425.8; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Westhoek / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +3.4%; bruto DROP -1.5%; pnl LOSS FLIP; FTE DROP -3.0%",
            "absurdity_score": "7.2",
            "cost_score": "5.5",
            "difficulty": "3.0",
            "priority_index": "6.1",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose YE2024 profit→LOSS flip one-offs; "
                "loonkostsubsidie/GESCO/ESF split"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2184; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Westhoek maatwerk dual after Wase/BWB"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Veurne>InterWest>NBB_PDF_assets_debt_pnl_flip",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl LOSS FLIP EUR-25093 vs YE2024 winst EUR3319507 recon (one-offs/herwaardering); "
                "bruto EUR15.40m ≫ omzet EUR10.78m loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "FTE DROP 438.9→425.8 path; related-party vs Kringwinkel West/Westlandia if any"
            ),
            "why_it_matters": (
                "Medium CW shows Westhoek maatwerk VZW flipping from EUR3.32m profit to LOSS while "
                "omzet JUMPS under subsidy-inflated bruto — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "MAATWERKBEDRIJF INTERWEST VZW",
            "recipient_email": "info@interwest.be",
            "recipient_postal": "Albert I laan 29, 8630 Veurne",
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
