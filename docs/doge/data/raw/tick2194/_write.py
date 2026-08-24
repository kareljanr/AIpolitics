# tick2194 writer — Forena YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T10:40:00Z"
TICK = "2194"
ENTITY = "vzw_forena_menen"
SRC_EN = "src_forena_jr2025_cw_en"
COMM = "comm_forena_jr2025_statutory_maatwerk_fte_jump_pnl_drop"
LB = "lb_forena_omzet_jump_16_30m_fte_jump_pnl_drop_jr2025"
GAP = "gap_forena_nbb_pdf_assets_debt_fte_jump_pnl_drop_bruto_gt_omzet_matrix_l5"

OMZET = 16296866
BRUTO = 27867647
PNL = 649564
EQUITY = 20129222
FTE = 708.7
OMZET24 = 14125096
BRUTO24 = 21929051
PNL24 = 948653
EQUITY24 = 18586646
FTE24 = 564.6


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
            "source_id": "src_forena_jr2025_cw_nl",
            "title": "Companyweb NL Forena YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0425410920/forena",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 06.05.2026; raw docs/doge/data/raw/tick2194/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Forena YE2025 statutory",
            "url": "https://www.companyweb.be/en/0425410920/forena",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 06-05-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_forena_jr2025_cw_fr",
            "title": "Companyweb FR Forena YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0425410920/forena",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_forena_kbo_2194",
            "title": "KBO Forena 0425.410.920 Actief VZW Menen 2 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0425410920",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2194; Actief VZW; Industrielaan 32 8930 Menen; 2 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_forena_foi_contact_2194",
            "title": "Forena FOI channel info@forena.be",
            "url": "https://www.forena.be/contact",
            "publisher": "Forena VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2194; info@forena.be; Industrielaan 32 8930 Menen",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_forena_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +15.38% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_forena_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +27.08% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_forena_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -31.53% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_forena_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +8.3% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_forena_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE JUMP vs YE2024 {FTE24} (+25.5%); assets/debt Unknown",
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
            "title": "Forena Menen YE2025 leftover dual (omzet JUMP 16.30m / FTE JUMP +26% / pnl DROP -32%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients West-Vlaanderen Menen",
            "legal_basis": "VZW maatwerk (KBO 0425.410.920; Actief; 2 VE; RSZ NACE 88.993)",
            "decision_date": "2026-05-06",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0425410920/forena",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose FTE JUMP +144 vs pnl DROP + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>Forena>JR2025_statutory_L5",
            "notes": "tick2194; Medium CW; omzet primary envelope; FTE JUMP +25.5% with pnl DROP primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; Kunnig FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Forena omzet JUMP 16.30m / FTE JUMP +26% / pnl DROP -32% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>Forena>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 16.30m / bruto 27.87m ≫ omzet / pnl DROP 650k -32% from YE2024 949k / equity JUMP 20.1m / FTE JUMP 708.7 from 564.6 (+25.5%); wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Menen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +15.4%; bruto JUMP +27.1%; pnl DROP -31.5%; equity JUMP +8.3%; FTE JUMP +25.5%",
            "absurdity_score": "7.4",
            "cost_score": "6.0",
            "difficulty": "3.0",
            "priority_index": "6.5",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose FTE JUMP +144 vs pnl DROP; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; West-Vlaanderen maatwerk dual after A-kwadraat/Mivas",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Forena VZW (Menen)",
            "name_fr": "Forena ASBL (Menin)",
            "name_en": "Forena sheltered workshop non-profit (Menen)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.forena.be/",
            "foi_email": "info@forena.be",
            "foi_postal": "Industrielaan 32, 8930 Menen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0425.410.920 Actief VZW 2 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl DROP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE} from {FTE24}; neerlegging 06.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Menen>Forena>NBB_PDF_assets_debt_fte_jump",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); FTE JUMP {FTE24}→{FTE} (+25.5%) with pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} recon; bruto JUMP EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; equity JUMP EUR{EQUITY}; 2 VE cost allocation",
            "why_it_matters": "Medium CW shows West-Vlaanderen maatwerk VZW adding ~144 FTE (+26%) while pnl DROPS -32% and bruto JUMPS +27% — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "FORENA VZW",
            "recipient_email": "info@forena.be",
            "recipient_postal": "Industrielaan 32, 8930 Menen",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; next every-10 2200",
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
    if row.get("task_id") == "rq_2194":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Forena YE2025 Medium (omzet JUMP 16.30m / FTE JUMP +26% / pnl DROP -32%)"
        row["notes"] = (
            "tick2194; Forena 0425.410.920 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; Kunnig FREE deferred; next rq_2195; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2194 missing")

if not any(r.get("task_id") == "rq_2195" for r in rows):
    rows.append(
        {
            "task_id": "rq_2195",
            "title": "leftover dual hole-fill after Forena — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2195 after Forena Menen YE2025 Medium (omzet JUMP 16.30m / FTE JUMP +26% / pnl DROP -32% / bruto≫omzet). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Kunnig FREE). "
                "Do NOT redo Forena, A-kwadraat, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2194 Forena; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2194=done rq_2195=open")

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
    "last_unit_id": "rq_2194",
    "ticks_completed": "2194",
    "paused": "no",
    "notes": (
        "tick2194 leftover FORENA 0425.410.920 Medium (omzet JUMP 16.30m; bruto 27.87m ≫ omzet; pnl DROP 650k -32%; "
        "equity JUMP 20.1m; FTE JUMP 708.7 from 564.6 +25.5%; 2 VE Menen); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2195; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2194 DONE")
