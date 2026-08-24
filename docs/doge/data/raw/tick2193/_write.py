# tick2193 writer — A-kwadraat YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T10:20:00Z"
TICK = "2193"
ENTITY = "vzw_a_kwadraat_turnhout"
SRC_EN = "src_a_kwadraat_jr2025_cw_en"
COMM = "comm_a_kwadraat_jr2025_statutory_maatwerk_bruto_gt_omzet"
LB = "lb_a_kwadraat_omzet_jump_13_43m_bruto_gt_omzet_jr2025"
GAP = "gap_a_kwadraat_nbb_pdf_assets_debt_bruto_gt_omzet_matrix_l5"

OMZET = 13433258
BRUTO = 25698142
PNL = 406438
EQUITY = 18020318
FTE = 614.7
OMZET24 = 12258783
BRUTO24 = 24504419
PNL24 = 370235
EQUITY24 = 17667822
FTE24 = 606.9


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
            "source_id": "src_a_kwadraat_jr2025_cw_nl",
            "title": "Companyweb NL A-kwadraat YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0406668540/a-kwadraat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 30.06.2026; raw docs/doge/data/raw/tick2193/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN A-kwadraat YE2025 statutory",
            "url": "https://www.companyweb.be/en/0406668540/a-kwadraat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 30-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_a_kwadraat_jr2025_cw_fr",
            "title": "Companyweb FR A-kwadraat YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0406668540/a-kwadraat",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_a_kwadraat_kbo_2193",
            "title": "KBO A-kwadraat 0406.668.540 Actief VZW Turnhout 5 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406668540",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2193; Actief VZW; Everdongenlaan 27 2300 Turnhout; 5 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_a_kwadraat_foi_contact_2193",
            "title": "A-kwadraat FOI channel info@a-kwadraat.be",
            "url": "https://www.a-kwadraat.be/contact",
            "publisher": "A-kwadraat VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2193; info@a-kwadraat.be; Everdongenlaan 27 2300 Turnhout",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_a_kwadraat_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +9.58% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_a_kwadraat_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.87% vs YE2024 {BRUTO24}; bruto≫omzet (~1.91x)",
        },
        {
            "budget_id": "bud_a_kwadraat_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +9.78% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_a_kwadraat_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +2% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_a_kwadraat_fte_jr2025_statutory",
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
            "title": "A-kwadraat Turnhout YE2025 leftover dual (omzet JUMP 13.43m / bruto≫omzet ~1.9x / pnl JUMP +10%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Antwerpen Turnhout Kempen",
            "legal_basis": "VZW maatwerk (KBO 0406.668.540; Actief; 5 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-30",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0406668540/a-kwadraat",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto~1.9x omzet loonkostsubsidie matrix",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>AKwadraat>JR2025_statutory_L5",
            "notes": "tick2193; Medium CW; omzet primary envelope; bruto≫omzet (~1.91x) primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; Forena/Kunnig FREE deferred; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "A-kwadraat omzet JUMP 13.43m / bruto≫omzet ~1.9x (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>AKwadraat>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 13.43m / bruto 25.70m ≫ omzet (~1.91x) / pnl JUMP 406k +10% / equity JUMP 18.0m / FTE JUMP 614.7; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Turnhout Kempen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +9.6%; bruto JUMP +4.9%; pnl JUMP +9.8%; equity JUMP +2.0%; FTE JUMP +1.3%",
            "absurdity_score": "6.8",
            "cost_score": "5.8",
            "difficulty": "3.0",
            "priority_index": "6.1",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto~1.9x omzet loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Kempen maatwerk dual after Mivas/Demival",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "A-kwadraat VZW (Turnhout)",
            "name_fr": "A-kwadraat ASBL (Turnhout)",
            "name_en": "A-kwadraat sheltered workshop non-profit (Turnhout)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.a-kwadraat.be/",
            "foi_email": "info@a-kwadraat.be",
            "foi_postal": "Everdongenlaan 27, 2300 Turnhout",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0406.668.540 Actief VZW 5 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~1.91x) pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 30.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>AKwadraat>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~1.91x) loonkostsubsidie/GESCO/ESF/VDAB matrix; pnl JUMP EUR{PNL}; equity JUMP EUR{EQUITY}; FTE JUMP {FTE24}→{FTE}; 5 VE cost allocation",
            "why_it_matters": "Medium CW shows Kempen maatwerk VZW with bruto ~1.9x omzet under public loonkost path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "A-KWADRAAT VZW",
            "recipient_email": "info@a-kwadraat.be",
            "recipient_postal": "Everdongenlaan 27, 2300 Turnhout",
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
    if row.get("task_id") == "rq_2193":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — A-kwadraat YE2025 Medium (omzet JUMP 13.43m / bruto≫omzet ~1.9x)"
        row["notes"] = (
            "tick2193; A-kwadraat 0406.668.540 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; Forena/Kunnig FREE deferred; next rq_2194; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2193 missing")

if not any(r.get("task_id") == "rq_2194" for r in rows):
    rows.append(
        {
            "task_id": "rq_2194",
            "title": "leftover dual hole-fill after A-kwadraat — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2194 after A-kwadraat Turnhout YE2025 Medium (omzet JUMP 13.43m / bruto≫omzet ~1.9x / FTE 615). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Forena/Kunnig FREE). "
                "Do NOT redo A-kwadraat, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2193 A-kwadraat; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2193=done rq_2194=open")

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
    "last_unit_id": "rq_2193",
    "ticks_completed": "2193",
    "paused": "no",
    "notes": (
        "tick2193 leftover A-KWADRAAT 0406.668.540 Medium (omzet JUMP 13.43m; bruto 25.70m ≫ omzet ~1.91x; pnl JUMP 406k +10%; "
        "equity JUMP 18.0m; FTE JUMP 614.7; 5 VE Turnhout); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2194; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2193 DONE")
