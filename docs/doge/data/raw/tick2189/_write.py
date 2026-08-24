# tick2189 writer — De Kringwinkel Antwerpen YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T09:00:00Z"
TICK = "2189"
ENTITY = "vzw_kringwinkel_antwerpen"
SRC_EN = "src_kringwinkel_antwerpen_jr2025_cw_en"
COMM = "comm_kringwinkel_antwerpen_jr2025_statutory_maatwerk_pnl_loss_flip"
LB = "lb_kringwinkel_antwerpen_omzet_jump_13_39m_pnl_loss_flip_jr2025"
GAP = "gap_kringwinkel_antwerpen_nbb_pdf_assets_debt_pnl_loss_flip_equity_drop_matrix_l5"

OMZET = 13392667
BRUTO = 17680883
PNL = -1051340
EQUITY = 3545202
FTE = 407.0
OMZET24 = 12135291
BRUTO24 = 16924613
PNL24 = 370212
EQUITY24 = 4621271
FTE24 = 365.5


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
            "source_id": "src_kringwinkel_antwerpen_jr2025_cw_nl",
            "title": "Companyweb NL De Kringwinkel Antwerpen YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0442423037/de-kringwinkel-antwerpen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl LOSS FLIP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 26.06.2026; raw docs/doge/data/raw/tick2189/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Kringwinkel Antwerpen YE2025 statutory",
            "url": "https://www.companyweb.be/en/0442423037/de-kringwinkel-antwerpen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 26-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_kringwinkel_antwerpen_jr2025_cw_fr",
            "title": "Companyweb FR De Kringwinkel Antwerpen YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0442423037/de-kringwinkel-antwerpen",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_kringwinkel_antwerpen_kbo_2189",
            "title": "KBO De Kringwinkel Antwerpen 0442.423.037 Actief VZW 16 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0442423037",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2189; Actief VZW; DE KRINGWINKEL ANTWERPEN / DKA; Deurnsebaan 52 2170 Antwerpen; 16 VE; RSZ NACE 88.993; BTW 47.793; KBO email empty",
        },
        {
            "source_id": "src_kringwinkel_antwerpen_foi_contact_2189",
            "title": "De Kringwinkel Antwerpen FOI channel info@dekringwinkelantwerpen.be",
            "url": "https://www.kringwinkel.be/centra/antwerpen",
            "publisher": "De Kringwinkel Antwerpen VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2189; info@dekringwinkelantwerpen.be (+ network info@kringwinkel.be); Deurnsebaan 52 2170 Antwerpen",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_kringwinkel_antwerpen_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +10.36% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_kringwinkel_antwerpen_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.47% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_kringwinkel_antwerpen_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 +{PNL24}",
        },
        {
            "budget_id": "bud_kringwinkel_antwerpen_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -23.29% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_kringwinkel_antwerpen_fte_jr2025_statutory",
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
            "title": "De Kringwinkel Antwerpen YE2025 leftover dual (omzet JUMP 13.39m / pnl LOSS FLIP -1.05m from +370k)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / reuse clients Antwerpen second-hand retail",
            "legal_basis": "VZW maatwerk (KBO 0442.423.037; Actief; 16 VE; RSZ NACE 88.993; DKA)",
            "decision_date": "2026-06-26",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0442423037/de-kringwinkel-antwerpen",
            "stated_goal": "Sheltered employment / reuse retail maatwerk",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose LOSS FLIP vs FTE JUMP + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>KringwinkelAntwerpen>JR2025_statutory_L5",
            "notes": "tick2189; Medium CW; omzet primary envelope; pnl LOSS FLIP + equity DROP primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after Blankedale; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Kringwinkel Antwerpen omzet JUMP 13.39m / pnl LOSS FLIP -1.05m from +370k (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>KringwinkelAntwerpen>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 13.39m / bruto 17.68m ≫ omzet / pnl LOSS FLIP -1.05m from YE2024 +370k / equity DROP 3.55m -23% / FTE JUMP 407; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Antwerpen / reuse shoppers / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment + second-hand retail",
            "measured_outcome": "omzet JUMP +10.4%; bruto JUMP +4.5%; pnl LOSS FLIP; equity DROP -23.3%; FTE JUMP +11.4%",
            "absurdity_score": "7.8",
            "cost_score": "5.9",
            "difficulty": "3.0",
            "priority_index": "6.8",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose LOSS FLIP vs FTE JUMP path; loonkostsubsidie/GESCO/ESF/OVAM reuse matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Antwerpen maatwerk/reuse dual after Blankedale/Mirto",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Kringwinkel Antwerpen VZW (DKA)",
            "name_fr": "De Kringwinkel Anvers ASBL (DKA)",
            "name_en": "De Kringwinkel Antwerp sheltered reuse non-profit (DKA)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.kringwinkel.be/centra/antwerpen",
            "foi_email": "info@dekringwinkelantwerpen.be",
            "foi_postal": "Deurnsebaan 52, 2170 Antwerpen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0442.423.037 Actief VZW 16 VE RSZ NACE 88.993 DKA; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl LOSS FLIP {PNL} vs YE2024 +{PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 26.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>KringwinkelAntwerpen>NBB_PDF_assets_debt_pnl_loss_flip",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl LOSS FLIP EUR{PNL} vs YE2024 winst EUR{PNL24} recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/OVAM matrix; equity DROP EUR{EQUITY} vs YE2024 EUR{EQUITY24} (-23.29%); FTE JUMP {FTE24}→{FTE} with LOSS path; 16 VE cost allocation",
            "why_it_matters": "Medium CW shows Antwerpen reuse/maatwerk VZW flipping from EUR370k profit to EUR1.05m LOSS while FTE JUMPS +11% and equity DROPS -23% — assets/debt unpublished",
            "priority": "8",
            "recipient_body": "DE KRINGWINKEL ANTWERPEN VZW",
            "recipient_email": "info@dekringwinkelantwerpen.be",
            "recipient_postal": "Deurnsebaan 52, 2170 Antwerpen",
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
            "notes": f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; also info@kringwinkel.be; next every-10 2190",
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
    if row.get("task_id") == "rq_2189":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Kringwinkel Antwerpen YE2025 Medium (omzet JUMP 13.39m / pnl LOSS FLIP -1.05m)"
        row["notes"] = (
            "tick2189; DKA 0442.423.037 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; named FREE after Blankedale; next rq_2190 EVERY-10; every-10 next 2190"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2189 missing")

if not any(r.get("task_id") == "rq_2190" for r in rows):
    rows.append(
        {
            "task_id": "rq_2190",
            "title": "EVERY-10 + leftover dual hole-fill after Kringwinkel Antwerpen — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2190 EVERY-10 after De Kringwinkel Antwerpen YE2025 Medium (omzet JUMP 13.39m / pnl LOSS FLIP -1.05m / equity DROP -23% / FTE JUMP 407). "
                "Refresh progress_every_10_ticks.md + doge_waste_top10_current.md. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(De Wroeter/Demival/Mivas FREE). "
                "Do NOT redo Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2189 Kringwinkel Antwerpen; EVERY-10 due at 2190; FARO/AIESH/REW still YE2024",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2189=done rq_2190=open")

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
    "last_unit_id": "rq_2189",
    "ticks_completed": "2189",
    "paused": "no",
    "notes": (
        "tick2189 leftover KRINGWINKEL ANTWERPEN/DKA 0442.423.037 Medium (omzet JUMP 13.39m; bruto 17.68m ≫ omzet; pnl LOSS FLIP -1.05m from +370k; "
        "equity DROP 3.55m -23%; FTE JUMP 407; 16 VE Antwerpen); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2190 EVERY-10; next every-10 2190; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2189 DONE")
