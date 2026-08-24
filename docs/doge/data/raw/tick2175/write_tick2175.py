# tick 2175 — Senes WZC YE2025 Medium CW after Orpimmo
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DATA = ROOT / "docs" / "doge" / "data"
csv.field_size_limit(10_000_000)

UTC = "2026-08-26T04:20:00Z"
ENTITY = "bv_senes_wzc"
GAP = "gap_senes_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_orpimmo_matrix_l5"
COMM = "comm_senes_jr2025_statutory_wzc_re_omzet_jump_pnl_loss_flip"
LB = "lb_senes_omzet_jump_1_19m_pnl_loss_flip_equity_drop_jr2025"
SRC_EN = "src_senes_jr2025_cw_en"


def append_rows(path, rows):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    ids = set()
    key = fieldnames[0]
    for row in existing:
        ids.add(row.get(key))
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        for row in rows:
            if row.get(key) in ids:
                print("SKIP dup", path.name, row.get(key))
                continue
            out = {k: row.get(k, "") for k in fieldnames}
            w.writerow(out)
            print("ADD", path.name, row.get(key))


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        rows = list(r)
    out = []
    for row in rows:
        if row.get("task_id") == "rq_2175":
            row = dict(row)
            row["title"] = "leftover dual — Senes WZC YE2025 Medium (omzet JUMP 1.19m / pnl LOSS FLIP -34k / equity DROP)"
            row["status"] = "done"
            row["entity_id"] = ENTITY
            row["instructions"] = (
                "Completed leftover Senes WZC after Orpimmo; preferred AGB Bornem JR2024 / "
                "FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; FOI ready not sent"
            )
            row["blocked_gap_id"] = GAP
            row["updated_utc"] = UTC
            row["notes"] = (
                "tick2175 Senes 0666.821.451 Medium; omzet JUMP 1192600 pnl LOSS FLIP -33890 "
                "equity DROP 6467829 bruto 1188602 FTE 0; Orpimmo board; NACE 68.201; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2176; next every-10 2180"
            )
        out.append(row)
    # spawn rq_2176
    if not any(x.get("task_id") == "rq_2176" for x in out):
        out.append(
            {
                "task_id": "rq_2176",
                "title": "leftover dual hole-fill after Senes — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2176 after Senes WZC YE2025 Medium (omzet JUMP 1.19m / pnl LOSS FLIP -34k / equity DROP / Orpimmo board). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/"
                    "De Vlietoever/Abdij/Aaigem/Anima*/Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis Belgium."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2175 Senes; FARO/AIESH/REW still YE2024; next every-10 2180",
            }
        )
        print("SPAWN rq_2176")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    print("UPD research_queue rq_2175=done")


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
        "last_unit_id": "rq_2175",
        "ticks_completed": "2175",
        "paused": "no",
        "notes": (
            "tick2175 leftover SENES WZC 0666.821.451 Medium (omzet JUMP 1.19m; pnl LOSS FLIP -33.9k; "
            "equity DROP 6.47m; bruto 1.19m; FTE 0; Orpimmo board; 1 VE NACE 68.201); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2176; next every-10 2180; continuous hole_fill"
        ),
    }
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("UPD loop_state ticks=2175")


append_rows(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Senes WZC BV (Ukkel / Orpimmo RE)",
            "name_fr": "Senes WZC SRL (Uccle / Orpimmo immobilier)",
            "name_en": "Senes WZC BV (Ukkel / Orpimmo care RE)",
            "level": "parastatal",
            "parent_id": "nv_orpimmo",
            "community_language": "bi",
            "website": "https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
            "foi_email": "hetdorp@emeis.com",
            "foi_postal": "Alsembergsesteenweg 1037, 1180 Ukkel",
            "notes": (
                "tick2175 YE2025 Medium CW NL+EN+FR + Strong KBO 0666.821.451 Actief BV 1 VE NACE 68.201/68.203; "
                "bestuurder ORPIMMO 0870.166.709 + 1026.468.648; omzet JUMP 1192600 pnl LOSS FLIP -33890 "
                "equity DROP 6467829 bruto 1188602 FTE 0; same zetel Orpimmo + Het Dorp; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_rows(
    DATA / "sources.csv",
    [
        {
            "source_id": "src_senes_jr2025_cw_nl",
            "title": "Companyweb NL Senes WZC YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0666821451/senes",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2175; YE2025 omzet JUMP 1192600 pnl LOSS FLIP -33890 equity DROP 6467829 bruto 1188602 FTE 0; "
                "neerlegging 07.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2175/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Senes WZC YE2025 statutory",
            "url": "https://www.companyweb.be/en/0666821451/senes",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2175; EN mirror YE2025 Medium; filed 07-07-2026; Last balance sheet year 2025; "
                "Turnover 1192600 Profit/Loss -33890 Equity 6467829"
            ),
        },
        {
            "source_id": "src_senes_jr2025_cw_fr",
            "title": "Companyweb FR Senes WZC YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0666821451",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2175; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_senes_kbo_2175",
            "title": "KBO Senes WZC 0666.821.451 Actief BV Ukkel Orpimmo board",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0666821451",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": (
                "tick2175; Actief BV; Alsembergsesteenweg 1037 1180 Ukkel; 1 VE; NACE 68.201/68.203; "
                "bestuurder ORPIMMO 0870.166.709 + 1026.468.648; KBO email empty"
            ),
        },
        {
            "source_id": "src_senes_foi_contact_2175",
            "title": "Senes WZC / Orpimmo / emeis Het Dorp FOI channel hetdorp@emeis.com",
            "url": "https://emeis.be/nl/locaties/woonzorgcentrum/het-dorp",
            "publisher": "emeis / Het Dorp path",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": (
                "tick2175; hetdorp@emeis.com; same zetel Alsembergsesteenweg 1037 as Orpimmo + Het Dorp; "
                "KBO email empty"
            ),
        },
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        {
            "budget_id": "bud_senes_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1192600",
            "amount_min_eur": "1192600",
            "amount_max_eur": "1192600",
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2175; Medium CW; omzet JUMP +2.92% vs YE2024 1158729",
        },
        {
            "budget_id": "bud_senes_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "1188602",
            "amount_min_eur": "1188602",
            "amount_max_eur": "1188602",
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2175; Medium CW; bruto JUMP +2.56% vs YE2024 1158968",
        },
        {
            "budget_id": "bud_senes_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "-33890",
            "amount_min_eur": "-33890",
            "amount_max_eur": "-33890",
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2175; Medium CW; pnl LOSS FLIP vs YE2024 +15306",
        },
        {
            "budget_id": "bud_senes_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "6467829",
            "amount_min_eur": "6467829",
            "amount_max_eur": "6467829",
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2175; Medium CW; equity DROP -4.46% vs YE2024 6769776",
        },
        {
            "budget_id": "bud_senes_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "0",
            "amount_min_eur": "0",
            "amount_max_eur": "0",
            "basis": "CW social-balance FTE / Employees 0",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2175; Medium CW; FTE 0; assets/debt Unknown",
        },
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "Senes WZC YE2025 leftover dual (omzet JUMP 1.19m / pnl LOSS FLIP -34k / equity DROP / Orpimmo)",
            "entity_id": ENTITY,
            "beneficiary": "Orpimmo / emeis / Het Dorp Ukkel care-RE path",
            "legal_basis": "BV RE (KBO 0666.821.451; Actief; 1 VE; NACE 68.201/68.203; board ORPIMMO 0870.166.709)",
            "decision_date": "2026-07-07",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "1192600",
            "cash_by_year": (
                '{"2025_omzet":1192600,"2025_bruto":1188602,"2025_pnl":-33890,"2025_equity":6467829,'
                '"2025_fte":0,"2024_omzet":1158729,"2024_bruto":1158968,"2024_pnl":15306,"2024_equity":6769776}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0666821451/senes",
            "stated_goal": "WZC-named RE rental/ops vehicle (Senes / Orpimmo Ukkel)",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose LOSS FLIP + equity DROP + Orpimmo/emeis/Het Dorp matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Brussel>Ukkel>Orpimmo>SenesWZC>JR2025_statutory_L5",
            "notes": (
                "tick2175; Medium CW; omzet primary envelope; pnl LOSS FLIP -34k; equity DROP 6.47m; "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn; "
                "DISTINCT Orpimmo holding + Het Dorp VZW"
            ),
        }
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Senes WZC omzet JUMP 1.19m / pnl LOSS FLIP -34k / equity DROP (YE2025)",
            "level": "L5",
            "type": "care_re_bv_statutory",
            "hierarchy_path": "Brussel>Ukkel>Orpimmo>SenesWZC>JR2025",
            "annual_cost_eur": "1192600",
            "total_cost_eur": "1192600",
            "tco_notes": (
                "CW omzet JUMP envelope 1.19m / bruto 1.19m / pnl LOSS FLIP -34k / equity DROP 6.47m / FTE 0; "
                "Orpimmo board; NACE 68 RE shell; assets/debt Unknown pending NBB PDF"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "Orpimmo / emeis / Het Dorp Ukkel care-RE path",
            "stated_goal": "WZC-named RE rental/ops Ukkel",
            "measured_outcome": "omzet JUMP +2.9%; pnl LOSS FLIP -34k; equity DROP -4.5%; FTE 0",
            "absurdity_score": "5.8",
            "cost_score": "4.2",
            "difficulty": "3.5",
            "priority_index": "4.9",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose LOSS FLIP + equity DROP + related-party "
                "vs Orpimmo 0870.166.709 / emeis / Het Dorp"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2175; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Orpimmo board dual after tick2174"
            ),
        }
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Brussel>Ukkel>Orpimmo>SenesWZC>NBB_PDF_assets_debt_pnl_flip_orpimmo",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "pnl LOSS FLIP EUR-33890 vs YE2024 +15306 recon; equity DROP to EUR6.47m path; "
                "related-party vs ORPIMMO 0870.166.709 + emeis Belgium 0887.690.451 + Het Dorp 0835.884.236; "
                "NACE 68.201 RE lease/huur matrix vs WZC-naam"
            ),
            "why_it_matters": (
                "Medium CW shows Orpimmo-boarded WZC-named RE BV with EUR1.19m omzet, LOSS FLIP and equity DROP "
                "while parent Orpimmo just flipped EUR70m equity — balanstotaal/assets/debt unpublished"
            ),
            "priority": "8",
            "recipient_body": "Senes WZC BV / ORPIMMO NV / emeis Belgium",
            "recipient_email": "hetdorp@emeis.com",
            "recipient_postal": "Alsembergsesteenweg 1037, 1180 Ukkel",
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
            "notes": "tick2175; ready NOT sent; Medium CW + Strong KBO; next every-10 2180",
        }
    ],
)

update_rq()
update_loop_state()
print("DONE tick2175")
