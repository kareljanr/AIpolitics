# tick2203 writer — Ijsedal Maatwerkbedrijf YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T13:40:00Z"
TICK = "2203"
ENTITY = "vzw_ijsedal_maatwerk_overijse"
SRC_EN = "src_ijsedal_jr2025_cw_en"
COMM = "comm_ijsedal_jr2025_statutory_maatwerk_pnl_loss_flip_bruto_gt_omzet"
LB = "lb_ijsedal_omzet_3_20m_pnl_loss_flip_bruto_gt_omzet_jr2025"
GAP = "gap_ijsedal_nbb_pdf_assets_debt_omzet_pnl_loss_flip_bruto_gt_omzet_matrix_l5"

OMZET = 3201710
BRUTO = 5617556
PNL = -77982
EQUITY = 2829539
FTE = 150.3
OMZET24 = 3071579
BRUTO24 = 5380730
PNL24 = 92856
EQUITY24 = 2932146
FTE24 = 144.1
ENVELOPE = OMZET


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
            "source_id": "src_ijsedal_jr2025_cw_nl",
            "title": "Companyweb NL Ijsedal Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407602017/ijsedal-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE {FTE}; neerlegging 08.06.2026; raw docs/doge/data/raw/tick2203/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Ijsedal Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407602017/ijsedal-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 08-06-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Gross margin {BRUTO} Employees {FTE}",
        },
        {
            "source_id": "src_ijsedal_jr2025_cw_fr",
            "title": "Companyweb FR Ijsedal Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407602017/ijsedal-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; CA {OMZET}",
        },
        {
            "source_id": "src_ijsedal_kbo_2203",
            "title": "KBO Ijsedal 0407.602.017 Actief VZW 1 VE Overijse",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=407602017",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2203; Actief VZW sinds 29.12.1969; Schavei 75 3090 Overijse; 1 VE; RSZ NACE 88.993; BTW sinds 01.01.1971; 7 bestuurders",
        },
        {
            "source_id": "src_ijsedal_foi_contact_2203",
            "title": "Ijsedal FOI channel info@ijsedal.be",
            "url": "https://www.ijsedal.be/",
            "publisher": "IJSEDAL Maatwerkbedrijf VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2203; info@ijsedal.be / alissa.stouffs@ijsedal.be; Schavei 75 3090 Overijse; 02 686 09 20",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_ijsedal_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +4.24% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_ijsedal_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025 (bruto≫omzet ~1.75x)",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.4% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_ijsedal_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP -183.98% vs YE2024 profit {PNL24}",
        },
        {
            "budget_id": "bud_ijsedal_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -3.5% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_ijsedal_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24}; assets/debt Unknown",
        },
    ],
)

cash = {
    "2025_omzet": OMZET,
    "2025_bruto": BRUTO,
    "2025_pnl": PNL,
    "2025_equity": EQUITY,
    "2025_fte": FTE,
    "2024_omzet": OMZET24,
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
            "title": "Ijsedal YE2025 leftover dual (omzet JUMP 3.20m / bruto≫omzet ~1.75x / pnl LOSS FLIP -78k)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Overijse Vlaams-Brabant",
            "legal_basis": "VZW maatwerk (KBO 0407.602.017; Actief; 1 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-08",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(ENVELOPE),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407602017/ijsedal-maatwerkbedrijf",
            "stated_goal": "Sheltered employment / maatwerk Overijse",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~1.75x + LOSS FLIP subsidy matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Overijse>Ijsedal>JR2025_statutory_L5",
            "notes": "tick2203; Medium CW; omzet primary envelope; bruto≫omzet ~1.75x + pnl LOSS FLIP while FTE JUMP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW 404/YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Ijsedal omzet JUMP 3.20m / bruto≫omzet ~1.75x / pnl LOSS FLIP -78k (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Overijse>Ijsedal>JR2025",
            "annual_cost_eur": str(ENVELOPE),
            "total_cost_eur": str(ENVELOPE),
            "tco_notes": "CW omzet JUMP envelope 3.20m / bruto 5.62m ≫omzet ~1.75x / pnl LOSS FLIP -78k from YE2024 +93k / equity DROP 2.83m / FTE JUMP 150.3; VL maatwerk Overijse; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Overijse / VDAB-ESF path / commercial clients",
            "stated_goal": "Sheltered employment maatwerk Overijse",
            "measured_outcome": "omzet JUMP +4.2%; bruto≫omzet ~1.75x; pnl LOSS FLIP -184%; equity DROP -3.5%; FTE JUMP +4.3%",
            "absurdity_score": "7.9",
            "cost_score": "4.8",
            "difficulty": "3.0",
            "priority_index": "7.0",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet + LOSS FLIP path; VDAB/ESF/gemeente subsidy split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO YE2024 AIESH/REW; VL maatwerk dual after Aarova/Kaliber",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "IJSEDAL Maatwerkbedrijf VZW (Overijse)",
            "name_fr": "IJSEDAL entreprise de travail adapté ASBL (Overijse)",
            "name_en": "Ijsedal sheltered workshop (Overijse)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.ijsedal.be/",
            "foi_email": "info@ijsedal.be",
            "foi_postal": "Schavei 75, 3090 Overijse",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.602.017 Actief VZW 1 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO}≫omzet pnl LOSS FLIP {PNL} vs YE2024 profit {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 08.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW 404/YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Overijse>Ijsedal>NBB_PDF_assets_debt_pnl_loss_flip",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} vs omzet EUR{OMZET} (~1.75x); pnl LOSS FLIP EUR{PNL} vs YE2024 profit EUR{PNL24} (-183.98%); FTE JUMP {FTE24}->{FTE}; VDAB/ESF/gemeente/provincie subsidy matrix",
            "why_it_matters": "Medium CW shows VL maatwerk VZW with bruto≫omzet ~1.75x and pnl LOSS FLIP while FTE JUMP — public subsidy path opaque",
            "priority": "8",
            "recipient_body": "IJSEDAL Maatwerkbedrijf VZW",
            "recipient_email": "info@ijsedal.be",
            "recipient_postal": "Schavei 75, 3090 Overijse",
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
    if row.get("task_id") == "rq_2203":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["blocked_gap_id"] = GAP
        row["title"] = (
            "leftover dual — Ijsedal YE2025 Medium (omzet JUMP 3.20m / bruto≫omzet ~1.75x / pnl LOSS FLIP -78k)"
        )
        row["notes"] = (
            "tick2203; Ijsedal 0407.602.017 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW 404/YE2024; next rq_2204; every-10 next 2210"
        )
        row["instructions"] = (
            "Tick 2203 after Aarova (+race Kaliber). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS/maatwerk "
            "(Ijsedal 0407.602.017 YE2025 FREE taken). Do NOT redo Ijsedal, Aarova, Kaliber, MWP Pajottenland, De Winning, "
            "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, "
            "Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, "
            "InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank."
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2203 missing")

if not any(r.get("task_id") == "rq_2204" for r in rows):
    rows.append(
        {
            "task_id": "rq_2204",
            "title": "leftover dual hole-fill after Ijsedal — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2204 after Ijsedal YE2025 Medium (omzet JUMP 3.20m / bruto≫omzet ~1.75x / pnl LOSS FLIP -78k / FTE JUMP). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused "
                "maatwerk/WZC/IGS/DSO (FREE: Kromme Boom YE2025 / Werkplus YE2025 empty-omzet / Oesterbank/Werkhuizen MIN/…). "
                "Do NOT redo Ijsedal, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, "
                "De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, "
                "Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, "
                "Het Dorp, De Vlietoever. Vlotter/De Ploeg still YE2024 — skip unless YE2025 appears."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2203 Ijsedal; FARO still YE2024; AIESH/REW 404/YE2024; next every-10 2210",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2203=done rq_2204=open")

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
    "last_unit_id": "rq_2203",
    "ticks_completed": "2203",
    "paused": "no",
    "notes": (
        "tick2203 leftover Ijsedal 0407.602.017 Medium (omzet JUMP 3.20m; bruto≫omzet ~1.75x 5.62m; "
        "pnl LOSS FLIP -78k; equity DROP 2.83m; FTE JUMP 150.3; 1 VE Overijse); AGB Bornem JR2024; FARO YE2024; "
        "AIESH/REW 404/YE2024; next rq_2204; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2203 DONE")
