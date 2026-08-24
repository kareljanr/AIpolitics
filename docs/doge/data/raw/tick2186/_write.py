# tick2186 writer — Mariasteen YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T08:00:00Z"
TICK = "2186"
ENTITY = "vzw_mariasteen_hooglede"
SRC_EN = "src_mariasteen_jr2025_cw_en"
COMM = "comm_mariasteen_jr2025_statutory_maatwerk_pnl_loss_improved_omzet_jump"
LB = "lb_mariasteen_omzet_jump_22_93m_pnl_loss_improved_bruto_gt_omzet_jr2025"
GAP = "gap_mariasteen_nbb_pdf_assets_debt_pnl_loss_bruto_gt_omzet_equity_drop_matrix_l5"

OMZET = 22932124
BRUTO = 29770020
PNL = -222391
EQUITY = 27992743
FTE = 877.7
OMZET24 = 21155147
BRUTO24 = 28285019
PNL24 = -366959
EQUITY24 = 28359207
FTE24 = 871.5


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
            return
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        for row in rows:
            w.writerow({c: row.get(c, "") for c in cols})
    print("APPENDED", path.name, len(rows))


append_csv(
    "sources.csv",
    [
        {
            "source_id": "src_mariasteen_jr2025_cw_nl",
            "title": "Companyweb NL Mariasteen YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0407079207/mariasteen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl LOSS IMPROVED {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 30.05.2026; raw docs/doge/data/raw/tick2186/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Mariasteen YE2025 statutory",
            "url": "https://www.companyweb.be/en/0407079207/mariasteen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 30-05-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_mariasteen_jr2025_cw_fr",
            "title": "Companyweb FR Mariasteen YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0407079207/mariasteen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_mariasteen_kbo_2186",
            "title": "KBO Mariasteen 0407.079.207 Actief VZW Hooglede 9 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407079207",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2186; Actief VZW; Koolskampstraat 24 8830 Hooglede; 9 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_mariasteen_foi_contact_2186",
            "title": "Mariasteen FOI channel info@mariasteen.be",
            "url": "https://mariasteen.be/",
            "publisher": "Mariasteen VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2186; info@mariasteen.be; Koolskampstraat 24 8830 Hooglede",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_mariasteen_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +8.4% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_mariasteen_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +5.25% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_mariasteen_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS IMPROVED +39.4% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_mariasteen_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -1.29% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_mariasteen_fte_jr2025_statutory",
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
            "title": "Mariasteen Hooglede YE2025 leftover dual (omzet JUMP 22.93m / pnl LOSS IMPROVED -222k / bruto≫omzet)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients West-Vlaanderen Hooglede",
            "legal_basis": "VZW maatwerk (KBO 0407.079.207; Actief; 9 VE; RSZ NACE 88.993)",
            "decision_date": "2026-05-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0407079207/mariasteen",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose persistent LOSS path + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Hooglede>Mariasteen>JR2025_statutory_L5",
            "notes": "tick2186; Medium CW; omzet primary envelope; pnl LOSS IMPROVED primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO last balance 2024; AIESH/REW stall; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Mariasteen omzet JUMP 22.93m / pnl LOSS IMPROVED -222k / bruto≫omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Hooglede>Mariasteen>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 22.93m / bruto 29.77m ≫ omzet / pnl LOSS IMPROVED -222k from YE2024 -367k / equity DROP 28.0m / FTE JUMP 877.7; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers West-Vlaanderen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +8.4%; bruto JUMP +5.3%; pnl LOSS IMPROVED +39.4%; equity DROP -1.3%; FTE JUMP +0.7%",
            "absurdity_score": "6.8",
            "cost_score": "6.5",
            "difficulty": "3.0",
            "priority_index": "6.5",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose multi-year LOSS path; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; West-Vlaanderen maatwerk dual after Weerwerk/InterWest/Westlandia",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Mariasteen VZW (Hooglede)",
            "name_fr": "Mariasteen ASBL (Hooglede)",
            "name_en": "Mariasteen sheltered workshop non-profit (Hooglede)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://mariasteen.be/",
            "foi_email": "info@mariasteen.be",
            "foi_postal": "Koolskampstraat 24, 8830 Hooglede",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.079.207 Actief VZW 9 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl LOSS IMPROVED {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 30.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>WestVlaanderen>Hooglede>Mariasteen>NBB_PDF_assets_debt_pnl_loss",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl LOSS EUR{PNL} IMPROVED vs YE2024 EUR{PNL24} recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; equity DROP EUR{EQUITY} vs YE2024 EUR{EQUITY24}; FTE JUMP {FTE24}→{FTE} path",
            "why_it_matters": "Medium CW shows large West-Vlaanderen maatwerk VZW (22.9m omzet / 878 FTE) with persistent LOSS and bruto≫omzet while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "MARIASTEEN VZW",
            "recipient_email": "info@mariasteen.be",
            "recipient_postal": "Koolskampstraat 24, 8830 Hooglede",
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

# research_queue
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row.get("task_id") == "rq_2186":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Mariasteen YE2025 Medium (omzet JUMP 22.93m / pnl LOSS IMPROVED -222k / bruto≫omzet)"
        row["notes"] = (
            "tick2186; Mariasteen 0407.079.207 YE2025 Medium CW; AGB Bornem JR2024; FARO last balance 2024; "
            "AIESH/REW stall; next rq_2187; every-10 next 2190"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2186 missing")

if not any(r.get("task_id") == "rq_2187" for r in rows):
    rows.append(
        {
            "task_id": "rq_2187",
            "title": "leftover dual hole-fill after Mariasteen — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2187 after Mariasteen Hooglede YE2025 Medium (omzet JUMP 22.93m / pnl LOSS IMPROVED -222k / bruto≫omzet / FTE 878). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Blankedale/Kringwinkel Antwerpen/De Wroeter/Demival/Mirto/Mivas FREE). "
                "Do NOT redo Mariasteen, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2186 Mariasteen; FARO/AIESH/REW still YE2024; next every-10 2190",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2186=done rq_2187=open")

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
    "last_unit_id": "rq_2186",
    "ticks_completed": "2186",
    "paused": "no",
    "notes": (
        "tick2186 leftover MARIASTEEN 0407.079.207 Medium (omzet JUMP 22.93m; bruto 29.77m ≫ omzet; pnl LOSS IMPROVED -222k from -367k; "
        "equity DROP 28.0m; FTE JUMP 877.7; 9 VE Hooglede); AGB Bornem JR2024; FARO last balance 2024; AIESH/REW stall; "
        "next rq_2187; next every-10 2190; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2186")
print("DONE")
