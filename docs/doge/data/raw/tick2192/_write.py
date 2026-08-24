# tick2192 Mivas YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T10:00:00Z"
TICK = "2192"
ENTITY = "vzw_mivas_lier"
SRC_EN = "src_mivas_jr2025_cw_en"
COMM = "comm_mivas_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump"
LB = "lb_mivas_omzet_11_59m_bruto_gt_omzet_pnl_jump_jr2025"
GAP = "gap_mivas_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_omzet_drop_matrix_l5"

OMZET = 11593122
BRUTO = 24404242
PNL = 411958
EQUITY = 28104207
FTE = 634.6
OMZET24 = 12412386
BRUTO24 = 24891017
PNL24 = 189529
EQUITY24 = 27486555
FTE24 = 641.0


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
            "source_id": "src_mivas_jr2025_cw_nl",
            "title": "Companyweb NL Mivas YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407597958/mivas",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet DROP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 24.06.2026; raw docs/doge/data/raw/tick2192/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Mivas YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407597958/mivas",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 24-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_mivas_jr2025_cw_fr",
            "title": "Companyweb FR Mivas YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407597958/mivas",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_mivas_kbo_2192",
            "title": "KBO Mivas 0407.597.958 Actief VZW Lier 7 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407597958",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2192; Actief VZW; MIVAS; Plaslaar 41 2500 Lier; 7 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_mivas_foi_contact_2192",
            "title": "Mivas FOI channel mailbox@mivas.be",
            "url": "https://mivas.be/contact",
            "publisher": "Mivas VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2192; mailbox@mivas.be; Plaslaar 41 2500 Lier",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_mivas_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet DROP -6.6% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_mivas_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto DROP -1.96% vs YE2024 {BRUTO24}; bruto≫omzet ~2.1x",
        },
        {
            "budget_id": "bud_mivas_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +117.36% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_mivas_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +2.25% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_mivas_fte_jr2025_statutory",
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
            "title": "Mivas Lier YE2025 leftover dual (omzet DROP 11.59m / bruto≫omzet ~2.1x / pnl JUMP +117%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy + packaging clients Antwerpen Lier Mechelen Rumst",
            "legal_basis": "VZW maatwerk (KBO 0407.597.958; Actief; 7 VE; RSZ NACE 88.993; afkorting Mivas)",
            "decision_date": "2026-06-24",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407597958/mivas",
            "stated_goal": "Sheltered employment / maatwerk packaging + circular projects",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet ~2.1x loonkost matrix + pnl JUMP vs omzet DROP path",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Mivas>JR2025_statutory_L5",
            "notes": "tick2192 primary; Medium CW; omzet primary envelope; bruto≫omzet ~2.1x + pnl JUMP vs omzet DROP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after Demival; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Mivas omzet DROP 11.59m / bruto≫omzet ~2.1x / pnl JUMP +117% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Mivas>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet DROP envelope 11.59m / bruto 24.40m ≫ omzet ~2.1x / pnl JUMP 412k +117% from YE2024 190k / equity JUMP 28.10m / FTE DROP 634.6; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Lier / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet DROP -6.6%; bruto DROP -2.0%; pnl JUMP +117%; equity JUMP +2.3%; FTE DROP -1.0%",
            "absurdity_score": "6.9",
            "cost_score": "5.6",
            "difficulty": "3.0",
            "priority_index": "6.1",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~2.1x; pnl JUMP vs omzet DROP; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} primary; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Antwerpen maatwerk dual after Demival/De Wroeter",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Mivas VZW (Lier)",
            "name_fr": "Mivas entreprise de travail adapté ASBL (Lier)",
            "name_en": "Mivas sheltered workshop non-profit (Lier)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://mivas.be/",
            "foi_email": "mailbox@mivas.be",
            "foi_postal": "Plaslaar 41, 2500 Lier",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.597.958 Actief VZW 7 VE RSZ NACE 88.993; omzet DROP {OMZET} bruto {BRUTO} (≫omzet ~2.1x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 24.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Lier>Mivas>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~2.1x) loonkostsubsidie/GESCO/ESF/VDAB matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+117%) while omzet DROP -6.6%; FTE DROP {FTE24}→{FTE}; 7 VE cost allocation",
            "why_it_matters": "Medium CW shows Antwerpen maatwerk VZW with bruto ~2.1x omzet and pnl JUMP +117% while omzet DROPS — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "MIVAS VZW",
            "recipient_email": "mailbox@mivas.be",
            "recipient_postal": "Plaslaar 41, 2500 Lier",
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
    if row.get("task_id") == "rq_2192":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Mivas YE2025 Medium (omzet DROP 11.59m / bruto≫omzet ~2.1x / pnl JUMP +117%)"
        row["notes"] = (
            "tick2192; Mivas 0407.597.958 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; next rq_2193; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2192 missing")

if not any(r.get("task_id") == "rq_2193" for r in rows):
    rows.append(
        {
            "task_id": "rq_2193",
            "title": "leftover dual hole-fill after Mivas — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2193 after Mivas Lier YE2025 Medium (omzet DROP 11.59m / bruto≫omzet ~2.1x / pnl JUMP +117% / FTE DROP 635). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
                "Do NOT redo Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2192 Mivas; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2192=done rq_2193=open")

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
    "last_unit_id": "rq_2192",
    "ticks_completed": "2192",
    "paused": "no",
    "notes": (
        "tick2192 leftover MIVAS 0407.597.958 Medium (omzet DROP 11.59m; bruto 24.40m ≫ omzet ~2.1x; pnl JUMP 412k +117% from 190k; "
        "equity JUMP 28.10m; FTE DROP 634.6; 7 VE Lier); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2193; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2192 DONE")
