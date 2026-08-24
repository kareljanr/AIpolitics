# tick 2186 — De Brug Mortsel YE2025 Medium CW after Weerwerk
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T08:00:00Z"
ENTITY = "vzw_de_brug_mortsel"
GAP = "gap_de_brug_nbb_pdf_assets_debt_pnl_loss_flip_bruto_gt_omzet_matrix_l5"
COMM = "comm_de_brug_jr2025_statutory_maatwerk_pnl_loss_flip"
LB = "lb_de_brug_omzet_12_64m_pnl_loss_flip_bruto_gt_omzet_jr2025"
SRC_EN = "src_de_brug_jr2025_cw_en"


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
        if row.get("task_id") == "rq_2186":
            row = dict(row)
            row["title"] = (
                "leftover dual — De Brug Mortsel YE2025 Medium "
                "(omzet JUMP 12.64m / pnl LOSS FLIP -254k / bruto>omzet)"
            )
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover De Brug after Weerwerk; preferred AGB Bornem JR2024 / "
                "FARO still YE2024 CW / AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
                "FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2186 De Brug 0408.347.828 Medium; omzet JUMP 12637954 bruto 13046815 "
                "pnl LOSS FLIP -253528 vs YE2024 +98717 equity DROP 24599275 FTE JUMP 341.3; "
                "1 VE Mortsel; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2187; next every-10 2190"
            )
        out.append(row)
    if not any(x.get("task_id") == "rq_2187" for x in out):
        out.append(
            {
                "task_id": "rq_2187",
                "title": (
                    "leftover dual hole-fill after De Brug — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2187 after De Brug Mortsel YE2025 Medium (omzet JUMP 12.64m / pnl LOSS FLIP "
                    "-254k from +99k / bruto>omzet). Prefer leftover AGB/APB if JR2025 PDF live, else "
                    "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/WZC/MRS/HVZ "
                    "(e.g. Mirto Gent YE2025 live unused). Do NOT redo De Brug/Weerwerk/Westlandia/"
                    "InterWest/Wase Werkplaats/BWB/Groep INTRO Maatwerk/MAAAT/WAAK SW/Waak/Stijn/"
                    "Stroom/Springplank/Creat CV/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/"
                    "Het Dorp/De Vlietoever/Anima*/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2186 De Brug; FARO/AIESH/REW still YE2024; next every-10 2190",
            }
        )
        print("SPAWN rq_2187")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2186=done")


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
        "last_unit_id": "rq_2186",
        "ticks_completed": "2186",
        "paused": "no",
        "notes": (
            "tick2186 leftover DE BRUG 0408.347.828 Medium (omzet JUMP 12.64m; bruto 13.05m > omzet; "
            "pnl LOSS FLIP -254k from +99k; equity DROP 24.60m; FTE JUMP 341.3; 1 VE Mortsel); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2187; next every-10 2190; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2186")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Brug VZW (Mortsel)",
            "name_fr": "De Brug ASBL (Mortsel)",
            "name_en": "De Brug sheltered workshop non-profit (Mortsel)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://debrug.be",
            "foi_email": "info@debrug.be",
            "foi_postal": "Waesdonckstraat 1, 2640 Mortsel",
            "notes": (
                "tick2186 YE2025 Medium CW NL+EN+FR + Strong KBO 0408.347.828 Actief VZW 1 VE "
                "RSZ NACE 88.993; omzet JUMP 12637954 bruto 13046815 (>omzet) pnl LOSS FLIP -253528 "
                "equity DROP 24599275 FTE JUMP 341.3; neerlegging 07.04.2026; "
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
            "source_id": "src_de_brug_jr2025_cw_nl",
            "title": "Companyweb NL De Brug YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0408347828/de-brug",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2186; YE2025 omzet JUMP 12637954 bruto 13046815 pnl LOSS FLIP -253528 "
                "equity DROP 24599275 FTE JUMP 341.3; neerlegging 07.04.2026; "
                "raw docs/doge/data/raw/tick2186/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Brug YE2025 statutory",
            "url": "https://www.companyweb.be/en/0408347828/de-brug",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2186; EN mirror YE2025 Medium; filed 07-04-2026; Last balance sheet year 2025; "
                "Turnover 12637954 Profit/Loss -253528 Equity 24599275 Employees 341.3"
            ),
        },
        {
            "source_id": "src_de_brug_jr2025_cw_fr",
            "title": "Companyweb FR De Brug YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0408347828/de-brug",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2186; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_de_brug_kbo_2186",
            "title": "KBO De Brug 0408.347.828 Actief VZW Mortsel 1 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=408347828",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2186; Actief VZW; Waesdonckstraat 1 2640 Mortsel; 1 VE; RSZ NACE 88.993 "
                "Beschutte en sociale werkplaatsen; KBO email empty; aannemer erkenning"
            ),
        },
        {
            "source_id": "src_de_brug_foi_contact_2186",
            "title": "De Brug FOI channel info@debrug.be",
            "url": "https://debrug.be/contact/",
            "publisher": "De Brug VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2186; info@debrug.be (+ sales@debrug.be); Waesdonckstraat 1 2640 Mortsel; BE 0408.347.828",
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_de_brug_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "12637954",
            "amount_min_eur": "12637954",
            "amount_max_eur": "12637954",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2186; Medium CW; omzet JUMP +0.73% vs YE2024 12546205",
        },
        {
            "budget_id": "bud_de_brug_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "13046815",
            "amount_min_eur": "13046815",
            "amount_max_eur": "13046815",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2186; Medium CW; bruto JUMP +2.15% vs YE2024 12771604; bruto>omzet",
        },
        {
            "budget_id": "bud_de_brug_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "-253528",
            "amount_min_eur": "-253528",
            "amount_max_eur": "-253528",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2186; Medium CW; pnl LOSS FLIP vs YE2024 +98717 (-356.82%)",
        },
        {
            "budget_id": "bud_de_brug_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "24599275",
            "amount_min_eur": "24599275",
            "amount_max_eur": "24599275",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2186; Medium CW; equity DROP -1.13% vs YE2024 24881273",
        },
        {
            "budget_id": "bud_de_brug_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "341.3",
            "amount_min_eur": "341.3",
            "amount_max_eur": "341.3",
            "basis": "CW social-balance FTE / Employees 341.3",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2186; Medium CW; FTE JUMP vs YE2024 333; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "De Brug Mortsel YE2025 leftover dual "
                "(omzet JUMP 12.64m / pnl LOSS FLIP -254k / bruto>omzet)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Mortsel-Antwerpen",
            "legal_basis": "VZW maatwerk (KBO 0408.347.828; Actief; 1 VE; RSZ NACE 88.993)",
            "decision_date": "2026-04-07",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "12637954",
            "cash_by_year": (
                '{"2025_omzet":12637954,"2025_bruto":13046815,"2025_pnl":-253528,"2025_equity":24599275,'
                '"2025_fte":341.3,"2024_omzet":12546205,"2024_bruto":12771604,"2024_pnl":98717,'
                '"2024_equity":24881273,"2024_fte":333}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0408347828/de-brug",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers (psychische beperking focus)",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loss-flip drivers + loonkostsubsidie matrix "
                "behind bruto>omzet"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Mortsel>DeBrug>JR2025_statutory_L5",
            "notes": (
                "tick2186; Medium CW; omzet primary envelope; pnl LOSS FLIP primary absurdity; "
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
            "name": "De Brug omzet JUMP 12.64m / pnl LOSS FLIP -254k / bruto>omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Mortsel>DeBrug>JR2025",
            "annual_cost_eur": "12637954",
            "total_cost_eur": "12637954",
            "tco_notes": (
                "CW omzet JUMP envelope 12.64m / bruto 13.05m > omzet / pnl LOSS FLIP -254k from +99k / "
                "equity DROP 24.60m / FTE JUMP 341.3; wage-cost subsidies opaque; "
                "assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Mortsel / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +0.73%; bruto JUMP +2.15%; pnl LOSS FLIP -357%; equity DROP -1.13%; FTE JUMP +2.5%",
            "absurdity_score": "7.0",
            "cost_score": "5.8",
            "difficulty": "3.0",
            "priority_index": "6.2",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loss-flip one-offs; "
                "loonkostsubsidie/GESCO/ESF split behind bruto>omzet"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2186; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Mortsel maatwerk dual after Weerwerk"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Mortsel>DeBrug>NBB_PDF_assets_debt_pnl_loss_flip",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl LOSS FLIP EUR-253528 vs YE2024 EUR+98717 (-356.82%) one-offs toelichting; "
                "bruto EUR13046815 > omzet EUR12637954 loonkostsubsidie/GESCO/ESF/VDAB matrix; "
                "FTE JUMP 333→341.3 with omzet flat / pnl flip path; equity DROP recon"
            ),
            "why_it_matters": (
                "Medium CW shows Mortsel maatwerk VZW flipping to EUR0.25m loss while omzet/bruto flat-up "
                "and assets/debt unpublished — subsidy / operating opacity under public loonkost path"
            ),
            "priority": "8",
            "recipient_body": "DE BRUG VZW",
            "recipient_email": "info@debrug.be",
            "recipient_postal": "Waesdonckstraat 1, 2640 Mortsel",
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
            "notes": "tick2186; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2186")
