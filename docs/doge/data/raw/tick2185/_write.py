# tick2185 writer — Weerwerk YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T07:40:00Z"
TICK = "2185"
ENTITY = "vzw_weerwerk_gent"
SRC_EN = "src_weerwerk_jr2025_cw_en"
COMM = "comm_weerwerk_jr2025_statutory_maatwerk_pnl_jump_equity_jump"
LB = "lb_weerwerk_omzet_5_54m_pnl_jump_197k_bruto_gt_omzet_jr2025"
GAP = "gap_weerwerk_nbb_pdf_assets_debt_pnl_jump_bruto_gt_omzet_equity_jump_matrix_l5"

OMZET = 5535667
BRUTO = 9125341
PNL = 197410
EQUITY = 1841558
FTE = 205.3
OMZET24 = 5406622
BRUTO24 = 8708583
PNL24 = 73414
EQUITY24 = 1329384
FTE24 = 200.4


def append_csv(path, rows, fieldnames=None):
    path = ROOT / path
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = fieldnames or r.fieldnames
    # skip if id already present
    for row in rows:
        key = list(row.keys())[0]
        if any(e.get(key) == row.get(key) for e in existing):
            print("SKIP existing", row.get(key))
            return
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
        for row in rows:
            w.writerow({c: row.get(c, "") for c in cols})
    print("APPENDED", path.name, len(rows))


# sources
append_csv(
    "sources.csv",
    [
        {
            "source_id": "src_weerwerk_jr2025_cw_nl",
            "title": "Companyweb NL Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0465104904/weerwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 03.07.2026; raw docs/doge/data/raw/tick2185/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/en/0465104904/weerwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 03-07-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_weerwerk_jr2025_cw_fr",
            "title": "Companyweb FR Weerwerk YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0465104904/weerwerk",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; CA {OMZET}",
        },
        {
            "source_id": "src_weerwerk_kbo_2185",
            "title": "KBO Weerwerk 0465.104.904 Actief VZW Gent 3 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465104904",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2185; Actief VZW (Vereniging zonder winstoogmerk); Gaardeniersweg 80 9000 Gent; 3 VE; RSZ NACE 88.993; BTW 88.999/43.410; KBO email empty",
        },
        {
            "source_id": "src_weerwerk_foi_contact_2185",
            "title": "Weerwerk FOI channel info@weerwerk.be",
            "url": "https://weerwerk.be",
            "publisher": "Weerwerk VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2185; info@weerwerk.be; Gaardeniersweg 80 9000 Gent",
        },
    ],
)

# budgets
append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_weerwerk_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +2.39% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_weerwerk_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +4.79% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_weerwerk_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +168.9% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_weerwerk_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +38.53% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_weerwerk_fte_jr2025_statutory",
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
            "title": "Weerwerk Gent YE2025 leftover dual (omzet JUMP 5.54m / pnl JUMP +169% / equity JUMP +39%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Gent Oost-Vlaanderen",
            "legal_basis": "VZW maatwerk (KBO 0465.104.904; Actief; 3 VE; RSZ NACE 88.993)",
            "decision_date": "2026-07-03",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0465104904/weerwerk",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose equity JUMP path + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>JR2025_statutory_L5",
            "notes": "tick2185; Medium CW; omzet primary envelope; pnl JUMP + equity JUMP primary absurdity; bruto≫omzet; assets/debt Unknown; preferred AGB Bornem JR2024; FARO last balance 2024; AIESH/REW stall; deferred after Westlandia; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Weerwerk omzet JUMP 5.54m / pnl JUMP +169% / equity JUMP +39% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 5.54m / bruto 9.13m ≫ omzet / pnl JUMP 197k +168.9% / equity JUMP 1.84m +38.5% / FTE JUMP 205.3; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Gent / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +2.4%; bruto JUMP +4.8%; pnl JUMP +168.9%; equity JUMP +38.5%; FTE JUMP +2.4%",
            "absurdity_score": "6.6",
            "cost_score": "5.0",
            "difficulty": "3.0",
            "priority_index": "5.7",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose equity JUMP / retained earnings path; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Gent maatwerk dual after Westlandia/InterWest",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Weerwerk VZW (Gent)",
            "name_fr": "Weerwerk ASBL (Gand)",
            "name_en": "Weerwerk sheltered workshop non-profit (Ghent)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://weerwerk.be",
            "foi_email": "info@weerwerk.be",
            "foi_postal": "Gaardeniersweg 80, 9000 Gent",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0465.104.904 Actief VZW 3 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 03.07.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Gent>Weerwerk>NBB_PDF_assets_debt_pnl_equity_jump",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); equity JUMP EUR{EQUITY} vs YE2024 EUR{EQUITY24} (+38.53%) recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24}; FTE JUMP {FTE24}→{FTE} path",
            "why_it_matters": "Medium CW shows Gent maatwerk VZW with bruto≫omzet and equity JUMP +39% while assets/debt unpublished — subsidy opacity under public loonkost path",
            "priority": "8",
            "recipient_body": "WEERWERK VZW",
            "recipient_email": "info@weerwerk.be",
            "recipient_postal": "Gaardeniersweg 80, 9000 Gent",
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

# research_queue: mark rq_2185 done + spawn rq_2186
rq_path = ROOT / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)

updated = False
for row in rows:
    if row.get("task_id") == "rq_2185":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Weerwerk YE2025 Medium (omzet JUMP 5.54m / pnl JUMP +169% / equity JUMP +39%)"
        row["notes"] = (
            "tick2185; Weerwerk 0465.104.904 YE2025 Medium CW; AGB Bornem JR2024; FARO last balance 2024; "
            "AIESH/REW stall; deferred FREE after Westlandia; next rq_2186; every-10 next 2190"
        )
        updated = True
        break
if not updated:
    raise SystemExit("rq_2185 not found")

if not any(r.get("task_id") == "rq_2186" for r in rows):
    rows.append(
        {
            "task_id": "rq_2186",
            "title": "leftover dual hole-fill after Weerwerk — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2186 after Weerwerk Gent YE2025 Medium (omzet JUMP 5.54m / pnl JUMP +169% / equity JUMP +39% / bruto≫omzet / FTE 205). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS. "
                "Do NOT redo Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2185 Weerwerk; FARO/AIESH/REW still YE2024; next every-10 2190",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue updated rq_2185=done rq_2186=open")

# loop_state
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
    "last_unit_id": "rq_2185",
    "ticks_completed": "2185",
    "paused": "no",
    "notes": (
        "tick2185 leftover WEERWERK 0465.104.904 Medium (omzet JUMP 5.54m; bruto 9.13m ≫ omzet; pnl JUMP 197k +169%; "
        "equity JUMP 1.84m +39%; FTE JUMP 205.3; 3 VE Gent); AGB Bornem JR2024; FARO last balance 2024; AIESH/REW stall; "
        "next rq_2186; next every-10 2190; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> tick 2185")
print("DONE")
