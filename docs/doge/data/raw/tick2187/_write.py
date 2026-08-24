# tick2187 writer — Mirto YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T08:20:00Z"
TICK = "2187"
ENTITY = "vzw_mirto_gent"
SRC_EN = "src_mirto_jr2025_cw_en"
COMM = "comm_mirto_jr2025_statutory_maatwerk_pnl_loss_bruto_gt_omzet"
LB = "lb_mirto_omzet_6_59m_pnl_loss_bruto_gt_omzet_jr2025"
GAP = "gap_mirto_nbb_pdf_assets_debt_pnl_loss_bruto_gt_omzet_equity_drop_matrix_l5"

OMZET = 6585087
BRUTO = 10031081
PNL = -113147
EQUITY = 5055657
FTE = 317.2
OMZET24 = 6824280
BRUTO24 = 10440940
PNL24 = -116848
EQUITY24 = 5184345
FTE24 = 321.4


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
            "source_id": "src_mirto_jr2025_cw_nl",
            "title": "Companyweb NL Mirto YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407656257/mirto",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto {BRUTO} pnl LOSS {PNL} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 28.05.2026; raw docs/doge/data/raw/tick2187/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Mirto YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407656257/mirto",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 28-05-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_mirto_jr2025_cw_fr",
            "title": "Companyweb FR Mirto YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407656257/mirto",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_mirto_kbo_2187",
            "title": "KBO Mirto 0407.656.257 Actief VZW Gent 4 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407656257",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2187; Actief VZW; Industriepark-Drongen 21 9031 Gent; 4 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_mirto_foi_contact_2187",
            "title": "Mirto FOI channel info@mirto.be",
            "url": "https://mirto.be/",
            "publisher": "Mirto VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2187; info@mirto.be; Industriepark-Drongen 21 9031 Gent",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_mirto_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet DROP -3.51% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_mirto_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP -3.93% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_mirto_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS IMPROVED +3.17% vs YE2024 {PNL24}; 3rd consecutive LOSS year",
        },
        {
            "budget_id": "bud_mirto_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -2.48% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_mirto_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE DROP vs YE2024 {FTE24}; assets/debt Unknown",
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
            "title": "Mirto Gent YE2025 leftover dual (omzet DROP 6.59m / pnl LOSS -113k / bruto≫omzet)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Gent Oost-Vlaanderen",
            "legal_basis": "VZW maatwerk (KBO 0407.656.257; Actief; 4 VE; RSZ NACE 88.993)",
            "decision_date": "2026-05-28",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407656257/mirto",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose multi-year LOSS path + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Mirto>JR2025_statutory_L5",
            "notes": "tick2187; Medium CW; omzet primary envelope; pnl LOSS (3rd year) primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after De Brug; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Mirto omzet DROP 6.59m / pnl LOSS -113k / bruto≫omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Mirto>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet DROP envelope 6.59m / bruto 10.03m ≫ omzet / pnl LOSS -113k (3rd consecutive LOSS) / equity DROP 5.06m / FTE DROP 317.2; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Gent / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet DROP -3.5%; bruto DROP -3.9%; pnl LOSS IMPROVED +3.2%; equity DROP -2.5%; FTE DROP -1.3%",
            "absurdity_score": "6.7",
            "cost_score": "5.2",
            "difficulty": "3.0",
            "priority_index": "5.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose multi-year LOSS path; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Gent maatwerk dual after Mariasteen/Weerwerk/De Brug",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Mirto VZW (Gent)",
            "name_fr": "Mirto ASBL (Gand)",
            "name_en": "Mirto sheltered workshop non-profit (Ghent)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://mirto.be/",
            "foi_email": "info@mirto.be",
            "foi_postal": "Industriepark-Drongen 21, 9031 Gent",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.656.257 Actief VZW 4 VE RSZ NACE 88.993; omzet DROP {OMZET} bruto {BRUTO} (≫omzet) pnl LOSS {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE DROP {FTE}; neerlegging 28.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Mirto>NBB_PDF_assets_debt_pnl_loss",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl LOSS EUR{PNL} (3rd consecutive vs YE2024 EUR{PNL24} / YE2023 -182k) recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; equity DROP EUR{EQUITY} vs YE2024 EUR{EQUITY24}; FTE DROP {FTE24}→{FTE} path",
            "why_it_matters": "Medium CW shows Gent maatwerk VZW with 3 consecutive LOSS years and bruto≫omzet while assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "MIRTO VZW",
            "recipient_email": "info@mirto.be",
            "recipient_postal": "Industriepark-Drongen 21, 9031 Gent",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2190",
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
    if row.get("task_id") == "rq_2187":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Mirto YE2025 Medium (omzet DROP 6.59m / pnl LOSS -113k / bruto≫omzet)"
        row["notes"] = (
            "tick2187; Mirto 0407.656.257 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; named FREE after De Brug; next rq_2188; every-10 next 2190"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2187 missing")

if not any(r.get("task_id") == "rq_2188" for r in rows):
    rows.append(
        {
            "task_id": "rq_2188",
            "title": "leftover dual hole-fill after Mirto — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2188 after Mirto Gent YE2025 Medium (omzet DROP 6.59m / pnl LOSS -113k / bruto≫omzet / FTE 317). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Blankedale/Kringwinkel Antwerpen/De Wroeter/Demival/Mivas FREE). "
                "Do NOT redo Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2187 Mirto; FARO/AIESH/REW still YE2024; next every-10 2190",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2187=done rq_2188=open")

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
    "last_unit_id": "rq_2187",
    "ticks_completed": "2187",
    "paused": "no",
    "notes": (
        "tick2187 leftover MIRTO 0407.656.257 Medium (omzet DROP 6.59m; bruto 10.03m ≫ omzet; pnl LOSS -113k 3rd year; "
        "equity DROP 5.06m; FTE DROP 317.2; 4 VE Gent); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2188; next every-10 2190; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2187 DONE")
