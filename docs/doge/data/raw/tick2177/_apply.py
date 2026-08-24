# -*- coding: utf-8 -*-
"""tick2177 Stroom Maatwerk Antwerpen YE2025 Medium — omzet JUMP 9.20m / bruto 19.5m."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path("docs/doge/data")
TS = "2026-08-26T05:00:00Z"
ENTITY = "vzw_maatwerk_stroom"
GAP = "gap_stroom_maatwerk_nbb_pdf_assets_debt_bruto_gt_omzet_subsidy_matrix_l5"
COMM = "comm_stroom_maatwerk_jr2025_statutory_omzet_jump_bruto_19_5m"
LB = "lb_stroom_omzet_jump_9_20m_bruto_19_5m_fte495_jr2025"
SRC_EN = "src_stroom_maatwerk_jr2025_cw_en"
OMZET = 9196890
BRUTO = 19463745
PNL = 437325
EQUITY = 27798223
FTE = 494.9
OMZET_PY = 8717106
BRUTO_PY = 18625364
PNL_PY = 440032
EQUITY_PY = 27427204


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added)


def update_rq():
    path = ROOT / "research_queue.csv"
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        r = csv.DictReader(f)
        rows = list(r)
        cols = r.fieldnames
    for row in rows:
        if row.get("task_id") == "rq_2177":
            row["status"] = "done"
            row["updated_utc"] = TS
            row["title"] = (
                "leftover dual — Stroom Maatwerk Antwerpen YE2025 Medium "
                "(omzet JUMP 9.20m / bruto 19.5m / FTE 495)"
            )
            row["notes"] = (
                "tick2177 Stroom 0407.839.369 Medium; omzet JUMP 9196890 pnl 437325 "
                "equity JUMP 27798223 bruto JUMP 19463745 FTE 494.9; NACE 88.993/88.999; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Waak+Stijn FREE deferred; "
                "next rq_2178; next every-10 2180"
            )
            row["entity_id"] = ENTITY
            row["blocked_gap_id"] = GAP
            row["instructions"] = (
                "Completed leftover Stroom Maatwerk after Springplank/Farys Solar race; "
                "preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 "
                "+ Strong KBO; FOI ready not sent"
            )
    ids = {row.get("task_id") for row in rows}
    if "rq_2178" not in ids:
        rows.append(
            {
                "task_id": "rq_2178",
                "title": (
                    "leftover dual hole-fill after Stroom — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Waak-or-Stijn/unused IGS-DSO-WZC-MRS-HVZ"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2178 after Stroom Maatwerk YE2025 Medium (omzet JUMP 9.20m / bruto 19.5m / "
                    "FTE 495). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else FREE Waak Maatwerk 0439.993.582 or Stijn 0439.452.461 "
                    "if still unused, else unused IGS/DSO/WZC/MRS/HVZ live euros. Do NOT redo "
                    "Stroom/Springplank/Farys Solar/Senes/Orpimmo/Langerheide/Cur@-Z/Het Dorp/"
                    "De Vlietoever/Abdij/Aaigem/Anima*/Zorg-Saam/Ben/Sint Lodewijk/Lork Hoeselt/emeis."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": (
                    "spawned after tick2177 Stroom; FARO/AIESH/REW still YE2024; "
                    "Waak+Stijn YE2025 FREE; next every-10 2180"
                ),
            }
        )
        print("spawn rq_2178")
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("rq_2177=done")


def write_loop_state():
    path = ROOT / "loop_state.csv"
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)
        cols = r.fieldnames
    rows[0] = {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": TS,
        "last_unit_id": "rq_2177",
        "ticks_completed": "2177",
        "paused": "no",
        "notes": (
            "tick2177 leftover Stroom Maatwerk 0407.839.369 Medium (omzet JUMP 9.20m +5.5%; "
            "bruto JUMP 19.5m; pnl flat 437k; equity JUMP 27.8m; FTE 494.9; 2 VE NACE 88.993/"
            "88.999 maatwerk Merksem); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Waak+Stijn FREE; next rq_2178; next every-10 2180; continuous hole_fill"
        ),
    }
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("loop_state=2177")


append_csv(
    ROOT / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Stroom Maatwerk VZW (Antwerpen / Merksem)",
            "name_fr": "Stroom Maatwerk ASBL (Anvers / Merksem)",
            "name_en": "Stroom Maatwerk VZW (Antwerp / Merksem)",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.stroommaatwerk.be",
            "foi_email": "info@stroommaatwerk.be",
            "foi_postal": "Winterling 3-7, 2170 Antwerpen (Merksem); tel 03 646 94 64",
            "notes": (
                "tick2177 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.839.369 Actief VZW 2 VE "
                "RSZ NACE 88.993 / BTW 88.999 maatwerk; omzet JUMP 9196890 pnl 437325 equity JUMP "
                "27798223 bruto JUMP 19463745 FTE 494.9; neerlegging 08.07.2026; assets/debt Unknown; "
                f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn"
            ),
        }
    ],
)

append_csv(
    ROOT / "sources.csv",
    [
        {
            "source_id": "src_stroom_maatwerk_jr2025_cw_nl",
            "title": "Companyweb NL Stroom Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407839369/stroom-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2177; YE2025 omzet 9196890 pnl 437325 equity 27798223 bruto 19463745 "
                "FTE 494.9; neerlegging 08.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2177/"
            ),
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Stroom Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407839369",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": (
                "tick2177; EN mirror YE2025 Medium; filed 08-07-2026; Last balance sheet year 2025; "
                "Turnover 9196890 Profit/Loss 437325 Equity 27798223 Gross margin 19463745"
            ),
        },
        {
            "source_id": "src_stroom_maatwerk_jr2025_cw_fr",
            "title": "Companyweb FR Stroom Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407839369",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": "tick2177; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_stroom_maatwerk_kbo_2177",
            "title": "KBO Stroom Maatwerk 0407.839.369 Actief VZW Antwerpen 2 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407839369",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "primary_register",
            "notes": (
                "tick2177; Strong Actief VZW sinds 01.01.1960; Winterling 3-7 2170 Antwerpen; "
                "2 VE; RSZ NACE 88.993 / BTW 88.999; KBO email/web empty"
            ),
        },
        {
            "source_id": "src_stroom_maatwerk_site_contact_2177",
            "title": "Stroom Maatwerk official contact (info@ + tel 03 646 94 64)",
            "url": "https://www.stroommaatwerk.be/contact/",
            "publisher": "stroommaatwerk.be",
            "accessed_date": "2026-08-26",
            "source_class": "primary_org",
            "notes": (
                "tick2177; Winterling 3-7 2170 Merksem; BE 0407.839.369; tel 03 646 94 64; "
                "info@stroommaatwerk.be (doeners.be Medium mirror); FOI channel"
            ),
        },
    ],
)

append_csv(
    ROOT / "budgets.csv",
    [
        {
            "budget_id": "bud_stroom_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick2177; Medium CW; omzet JUMP +5.5% vs YE2024 {OMZET_PY}",
        },
        {
            "budget_id": "bud_stroom_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick2177; bruto>omzet; JUMP +4.5% vs YE2024 {BRUTO_PY}",
        },
        {
            "budget_id": "bud_stroom_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory pnl / Profit-Loss YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick2177; pnl flat -0.62% vs YE2024 {PNL_PY}",
        },
        {
            "budget_id": "bud_stroom_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick2177; equity JUMP +1.35% vs YE2024 {EQUITY_PY}",
        },
        {
            "budget_id": "bud_stroom_omzet_jr2024_compar",
            "entity_id": ENTITY,
            "year": "2024",
            "amount_eur": str(OMZET_PY),
            "amount_min_eur": str(OMZET_PY),
            "amount_max_eur": str(OMZET_PY),
            "basis": "CW comparative omzet YE2024",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": "tick2177; prior-year omzet comparator",
        },
    ],
)

append_csv(
    ROOT / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "Stroom Maatwerk Antwerpen YE2025 leftover dual "
                "(omzet JUMP 9.20m / bruto 19.5m / FTE 495)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Antwerpen-Merksem",
            "legal_basis": "VZW maatwerk (KBO 0407.839.369; Actief; 2 VE; NACE 88.993/88.999)",
            "decision_date": "2026-07-08",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                '{"2025_omzet":%d,"2025_bruto":%d,"2025_pnl":%d,'
                '"2025_equity":%d,"2025_fte":%s,"2024_omzet":%d,'
                '"2024_bruto":%d,"2024_pnl":%d,"2024_equity":%d}'
                % (OMZET, BRUTO, PNL, EQUITY, FTE, OMZET_PY, BRUTO_PY, PNL_PY, EQUITY_PY)
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407839369",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers since 1960",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; disclose loonkostsubsidie/GESCO/ESF/"
                "stad-provincie matrix; explain bruto 19.5m vs omzet 9.2m"
            ),
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Merksem>StroomMaatwerk>JR2025_statutory_L5",
            "notes": (
                "tick2177; Medium CW; omzet primary envelope; bruto>omzet (~2.1x); "
                "assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        }
    ],
)

append_csv(
    ROOT / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Stroom Maatwerk omzet JUMP 9.20m / bruto 19.5m / FTE 495 (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Merksem>StroomMaatwerk>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet envelope 9.20m / bruto 19.5m (~2.1x) / 494.9 FTE; pnl flat 437k; "
                "equity 27.8m; assets/debt Unknown pending NBB PDF; public maatwerk loonkost path"
            ),
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Antwerpen-Merksem / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk since 1960",
            "measured_outcome": (
                "omzet JUMP +5.5%; bruto JUMP +4.5%; pnl flat -0.62%; equity JUMP +1.35%; FTE 494.9"
            ),
            "absurdity_score": "5.0",
            "cost_score": "5.5",
            "difficulty": "3.5",
            "priority_index": "5.2",
            "cut_proposal": (
                "Publish NBB PDF assets/debt/cash FOI; disclose loonkostsubsidie/GESCO/ESF/"
                "stad-provincie split; explain bruto>>omzet"
            ),
            "status": "open",
            "notes": (
                f"tick2177; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "Waak+Stijn YE2025 FREE deferred"
            ),
        }
    ],
)

append_csv(
    ROOT / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Merksem>StroomMaatwerk>NBB_PDF_assets_debt_bruto_omzet",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); "
                "bruto EUR19.46m vs omzet EUR9.20m recon; loonkostsubsidie/GESCO/ESF/"
                "stad Antwerpen/provincie matrix YE2024-2025; FTE 494.9 vs ~540 staff claims"
            ),
            "why_it_matters": (
                "Medium CW shows large Antwerp maatwerk VZW with bruto ~2.1x omzet and 495 FTE — "
                "balanstotaal/assets/debt and public wage-cost subsidies unpublished"
            ),
            "priority": "8",
            "recipient_body": "Stroom Maatwerk VZW",
            "recipient_email": "info@stroommaatwerk.be",
            "recipient_postal": "Winterling 3-7, 2170 Antwerpen/Merksem (tel 03 646 94 64)",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": "2026-08-26",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": TS,
            "updated_utc": TS,
            "response_summary": "",
            "notes": (
                "tick2177; ready NOT sent; Medium CW + Strong KBO; FOI email Medium org/doeners; "
                "next every-10 2180"
            ),
        }
    ],
)

update_rq()
write_loop_state()
print("DONE tick2177 Stroom Maatwerk")
