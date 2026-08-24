# tick2204 writer — Werkplus Maatwerk YE2025 Medium CW (empty omzet / bruto 2.69m / pnl DROP -71%)
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T14:00:00Z"
TICK = "2204"
ENTITY = "vzw_werkplus_maatwerk_waregem"
SRC_EN = "src_werkplus_jr2025_cw_en"
COMM = "comm_werkplus_jr2025_statutory_maatwerk_empty_omzet_pnl_drop"
LB = "lb_werkplus_bruto_2_69m_empty_omzet_pnl_drop_jr2025"
GAP = "gap_werkplus_nbb_pdf_assets_debt_empty_omzet_pnl_drop_matrix_l5"

BRUTO = 2691553
PNL = 91880
EQUITY = 2457096
FTE = 62.8
BRUTO24 = 2663252
PNL24 = 315287
EQUITY24 = 2365216
FTE24 = 60.4
ENVELOPE = BRUTO  # omzet empty → bruto primary envelope


def append_csv(path, rows):
    path = ROOT / path
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    key = list(rows[0].keys())[0]
    for row in rows:
        if any(e.get(key) == row.get(key) for e in existing):
            print("SKIP", row.get(key))
            return False
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        for row in rows:
            w.writerow({c: row.get(c, "") for c in cols})
    print("APPENDED", path.name, len(rows))
    return True


append_csv(
    "sources.csv",
    [
        {
            "source_id": "src_werkplus_jr2025_cw_nl",
            "title": "Companyweb NL Werkplus Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0466950179/werkplus-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 empty omzet; bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE {FTE}; neerlegging 27.06.2026; raw docs/doge/data/raw/tick2204/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Werkplus Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0466950179/werkplus-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 27-06-2026; Turnover empty; Profit/Loss {PNL}; Equity {EQUITY}; Gross margin {BRUTO}; Employees {FTE}",
        },
        {
            "source_id": "src_werkplus_jr2025_cw_fr",
            "title": "Companyweb FR Werkplus Maatwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0466950179/werkplus-maatwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; CA unpublished; marge brute {BRUTO}",
        },
        {
            "source_id": "src_werkplus_kbo_2204",
            "title": "KBO Werkplus 0466.950.179 Actief VZW 1 VE Waregem",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466950179",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2204; Actief VZW sinds 27.09.1999; Windhoek 17 8790 Waregem; 1 VE; RSZ NACE 88.993; info@werkplus.be; tel 056613438",
        },
        {
            "source_id": "src_werkplus_foi_contact_2204",
            "title": "Werkplus FOI channel info@werkplus.be",
            "url": "https://www.werkplus.be/",
            "publisher": "Werkplus Maatwerk VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2204; info@werkplus.be; Windhoek 17 8790 Waregem; 056 61 34 38",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_werkplus_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (omzet empty → bruto envelope)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +1.06% vs YE2024 {BRUTO24}; omzet unpublished",
        },
        {
            "budget_id": "bud_werkplus_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -70.86% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_werkplus_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +3.88% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_werkplus_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown; omzet empty",
        },
        {
            "budget_id": "bud_werkplus_omzet_jr2025_empty",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": "Unknown",
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "CW FAQ: omzet / Turnover unpublished at latest deposit",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; empty omzet confirmed NL+EN+FR; bruto {BRUTO} used as envelope",
        },
    ],
)

cash = {
    "2025_omzet": "empty",
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
    "2024_bruto": BRUTO24,
    "2024_pnl": PNL24,
    "2024_equity": EQUITY24,
    "2024_fte": FTE24,
}

append_csv(
    "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": "Werkplus YE2025 leftover dual (bruto 2.69m empty-omzet / pnl DROP -71%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Waregem West-Vlaanderen",
            "legal_basis": "VZW maatwerk (KBO 0466.950.179; Actief; 1 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-27",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ENVELOPE),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0466950179/werkplus-maatwerk",
            "stated_goal": "Sheltered employment / maatwerk Waregem",
            "cut_option": "Publish NBB PDF assets/debt/omzet FOI; disclose empty-omzet + pnl DROP -71% subsidy matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Waregem>Werkplus>JR2025_statutory_L5",
            "notes": "tick2204; Medium CW; bruto primary envelope (omzet empty); pnl DROP -70.86% while FTE JUMP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Werkplus bruto 2.69m empty-omzet / pnl DROP -71% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Waregem>Werkplus>JR2025",
            "annual_cost_eur": str(ENVELOPE),
            "total_cost_eur": str(ENVELOPE),
            "tco_notes": "CW bruto envelope 2.69m / omzet empty / pnl DROP 91.9k from YE2024 315k (-71%) / equity JUMP 2.46m / FTE JUMP 62.8; VL maatwerk Waregem; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Waregem / VDAB-ESF path / commercial clients",
            "stated_goal": "Sheltered employment maatwerk Waregem",
            "measured_outcome": "omzet empty; bruto +1.1%; pnl DROP -70.9%; equity JUMP +3.9%; FTE JUMP +4.0%",
            "absurdity_score": "7.6",
            "cost_score": "4.5",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash/omzet FOI; disclose empty-omzet + pnl DROP path; VDAB/ESF/gemeente subsidy split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; VL maatwerk dual after Ijsedal/Kromme Boom",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Werkplus Maatwerk VZW (Waregem)",
            "name_fr": "Werkplus entreprise de travail adapté ASBL (Waregem)",
            "name_en": "Werkplus sheltered workshop (Waregem)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.werkplus.be/",
            "foi_email": "info@werkplus.be",
            "foi_postal": "Windhoek 17, 8790 Waregem",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0466.950.179 Actief VZW 1 VE RSZ NACE 88.993; omzet empty bruto JUMP {BRUTO} pnl DROP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 27.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Waregem>Werkplus>NBB_PDF_assets_debt_empty_omzet_pnl_drop",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal/omzet code70); empty/unpublished omzet vs bruto EUR{BRUTO}; pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-70.86%); FTE JUMP {FTE24}->{FTE}; VDAB/ESF/gemeente/provincie subsidy matrix",
            "why_it_matters": "Medium CW shows VL maatwerk VZW with empty omzet and pnl DROP -71% while FTE JUMP — public subsidy path opaque",
            "priority": "8",
            "recipient_body": "Werkplus Maatwerk VZW",
            "recipient_email": "info@werkplus.be",
            "recipient_postal": "Windhoek 17, 8790 Waregem",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2210",
        }
    ],
)

rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row.get("task_id") == "rq_2204":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = (
            "leftover dual — Werkplus YE2025 Medium (bruto 2.69m empty-omzet / pnl DROP -71%)"
        )
        row["notes"] = (
            "tick2204; Werkplus 0466.950.179 YE2025 Medium CW; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "next rq_2205; every-10 next 2210"
        )
        row["instructions"] = (
            "Tick 2204 after Ijsedal (+race De Kromme Boom). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS/maatwerk "
            "(Werkplus 0466.950.179 YE2025 FREE taken). Do NOT redo Werkplus, Ijsedal, De Kromme Boom, Aarova, Kaliber, "
            "MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, "
            "Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, "
            "De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank."
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2204 missing")

if not any(r.get("task_id") == "rq_2205" for r in rows):
    rows.append(
        {
            "task_id": "rq_2205",
            "title": "leftover dual hole-fill after Werkplus — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2205 after Werkplus YE2025 Medium (bruto 2.69m empty-omzet / pnl DROP -71% / FTE JUMP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                "maatwerk/WZC/IGS/DSO (FREE: Oesterbank if YE2025 / Werkhuizen MIN / other unused maatwerk-WZC-IGS). "
                "Do NOT redo Werkplus, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, "
                "Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, "
                "Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank. Vlotter/De Ploeg/Oesterbank still YE2024 — skip unless YE2025."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2204 Werkplus; FARO/AIESH/REW still YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2204=done rq_2205=open")

ls_path = ROOT / "loop_state.csv"
with ls_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
rows[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2204",
    "ticks_completed": "2204",
    "paused": "no",
    "notes": (
        "tick2204 leftover Werkplus 0466.950.179 Medium (omzet empty; bruto JUMP 2.69m; "
        "pnl DROP -71% 91.9k; equity JUMP 2.46m; FTE JUMP 62.8; 1 VE Waregem); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "next rq_2205; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2204 DONE")
