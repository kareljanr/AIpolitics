# tick2188 writer — Blankedale YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T08:40:00Z"
TICK = "2188"
ENTITY = "vzw_blankedale_tienen"
SRC_EN = "src_blankedale_jr2025_cw_en"
COMM = "comm_blankedale_jr2025_statutory_maatwerk_pnl_drop_bruto_gt_omzet"
LB = "lb_blankedale_omzet_12_93m_pnl_drop_bruto_gt_omzet_jr2025"
GAP = "gap_blankedale_nbb_pdf_assets_debt_pnl_drop_bruto_gt_omzet_matrix_l5"

OMZET = 12934810
BRUTO = 26139293
PNL = 391309
EQUITY = 29439327
FTE = 775.6
OMZET24 = 12870608
BRUTO24 = 26073483
PNL24 = 1023960
EQUITY24 = 29089768
FTE24 = 778.9


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
            "source_id": "src_blankedale_jr2025_cw_nl",
            "title": "Companyweb NL Blankedale YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0400999978/blankedale",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 02.06.2026; raw docs/doge/data/raw/tick2188/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Blankedale YE2025 statutory",
            "url": "https://www.companyweb.be/en/0400999978/blankedale",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 02-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_blankedale_jr2025_cw_fr",
            "title": "Companyweb FR Blankedale YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0400999978/blankedale",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_blankedale_kbo_2188",
            "title": "KBO Blankedale 0400.999.978 Actief VZW Tienen 2 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0400999978",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2188; Actief VZW; Ambachtenlaan 70 3300 Tienen; 2 VE; RSZ NACE 88.993; replaces 0410.425.608; KBO email empty",
        },
        {
            "source_id": "src_blankedale_foi_contact_2188",
            "title": "Blankedale FOI channel info@blankedale.be",
            "url": "https://www.blankedale.com/",
            "publisher": "Blankedale VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2188; info@blankedale.be; Ambachtenlaan 70 3300 Tienen",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_blankedale_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +0.5% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_blankedale_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +0.25% vs YE2024 {BRUTO24}; bruto≫omzet (~2.0x)",
        },
        {
            "budget_id": "bud_blankedale_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -61.78% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_blankedale_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +1.2% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_blankedale_fte_jr2025_statutory",
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
            "title": "Blankedale Tienen YE2025 leftover dual (omzet JUMP 12.93m / pnl DROP -62% / bruto≫omzet ~2x)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Vlaams-Brabant Tienen",
            "legal_basis": "VZW maatwerk (KBO 0400.999.978; Actief; 2 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-02",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0400999978/blankedale",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose pnl DROP path + loonkostsubsidie matrix behind bruto~2x omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Tienen>Blankedale>JR2025_statutory_L5",
            "notes": "tick2188; Medium CW; omzet primary envelope; bruto≫omzet (~2x) + pnl DROP primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after Mirto; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Blankedale omzet JUMP 12.93m / pnl DROP -62% / bruto≫omzet ~2x (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Tienen>Blankedale>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 12.93m / bruto 26.14m ≫ omzet (~2.0x) / pnl DROP 391k -62% from YE2024 1.02m / equity JUMP 29.4m / FTE DROP 775.6; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Tienen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +0.5%; bruto JUMP +0.3%; pnl DROP -61.8%; equity JUMP +1.2%; FTE DROP -0.4%",
            "absurdity_score": "7.0",
            "cost_score": "5.8",
            "difficulty": "3.0",
            "priority_index": "6.2",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose pnl crater vs flat omzet; loonkostsubsidie/GESCO/ESF split behind bruto~2x",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Vlaams-Brabant maatwerk dual after Mirto/Mariasteen",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Blankedale VZW (Tienen)",
            "name_fr": "Blankedale ASBL (Tirlemont)",
            "name_en": "Blankedale sheltered workshop non-profit (Tienen)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.blankedale.com/",
            "foi_email": "info@blankedale.be",
            "foi_postal": "Ambachtenlaan 70, 3300 Tienen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0400.999.978 Actief VZW 2 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~2x) pnl DROP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 02.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>VlaamsBrabant>Tienen>Blankedale>NBB_PDF_assets_debt_pnl_drop_bruto",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-61.78%) recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~2.0x) loonkostsubsidie/GESCO/ESF/VDAB matrix; equity JUMP EUR{EQUITY}; FTE DROP {FTE24}→{FTE} path",
            "why_it_matters": "Medium CW shows Vlaams-Brabant maatwerk VZW with bruto nearly 2x omzet and pnl crater -62% while assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "BLANKEDALE VZW",
            "recipient_email": "info@blankedale.be",
            "recipient_postal": "Ambachtenlaan 70, 3300 Tienen",
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
    if row.get("task_id") == "rq_2188":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "leftover dual — Blankedale YE2025 Medium (omzet JUMP 12.93m / pnl DROP -62% / bruto≫omzet ~2x)"
        row["notes"] = (
            "tick2188; Blankedale 0400.999.978 YE2025 Medium CW; AGB Bornem JR2024; FARO YE2024; "
            "AIESH/REW stall; named FREE after Mirto; next rq_2189; every-10 next 2190"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2188 missing")

if not any(r.get("task_id") == "rq_2189" for r in rows):
    rows.append(
        {
            "task_id": "rq_2189",
            "title": "leftover dual hole-fill after Blankedale — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2189 after Blankedale Tienen YE2025 Medium (omzet JUMP 12.93m / pnl DROP -62% / bruto≫omzet ~2x / FTE 776). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Kringwinkel Antwerpen/De Wroeter/Demival/Mivas FREE). "
                "Do NOT redo Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2188 Blankedale; FARO/AIESH/REW still YE2024; next every-10 2190",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2188=done rq_2189=open")

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
    "last_unit_id": "rq_2188",
    "ticks_completed": "2188",
    "paused": "no",
    "notes": (
        "tick2188 leftover BLANKEDALE 0400.999.978 Medium (omzet JUMP 12.93m; bruto 26.14m ≫ omzet ~2x; pnl DROP 391k -62% from 1.02m; "
        "equity JUMP 29.4m; FTE DROP 775.6; 2 VE Tienen); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2189; next every-10 2190; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2188 DONE")
