# tick2204 writer — Trianval Wetteren YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T14:00:00Z"
TICK = "2204"
ENTITY = "vzw_trianval_wetteren"
SRC_EN = "src_trianval_jr2025_cw_en"
COMM = "comm_trianval_jr2025_statutory_maatwerk_bruto_gt_omzet_pnl_jump"
LB = "lb_trianval_omzet_jump_6_10m_bruto_gt_omzet_pnl_jump_92pct_jr2025"
GAP = "gap_trianval_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_jump_matrix_l5"

OMZET = 6103169
BRUTO = 10640408
PNL = 748211
EQUITY = 15150698
FTE = 255.3
OMZET24 = 5141842
BRUTO24 = 9312994
PNL24 = 390627
EQUITY24 = 14393864
FTE24 = 248.1
RATIO = round(BRUTO / OMZET, 2)


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
            "source_id": "src_trianval_jr2025_cw_nl",
            "title": "Companyweb NL Trianval YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0419052074/trianval",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 01.05.2026; raw docs/doge/data/raw/tick2204/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Trianval YE2025 statutory",
            "url": "https://www.companyweb.be/en/0419052074/trianval",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 01-05-2026; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_trianval_jr2025_cw_fr",
            "title": "Companyweb FR Trianval YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0419052074/trianval",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_trianval_kbo_2204",
            "title": "KBO Trianval 0419.052.074 Actief VZW 3 VE Wetteren",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419052074",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2204; Actief VZW; Biezeweg 8 9230 Wetteren; 3 VE; RSZ NACE 88.993",
        },
        {
            "source_id": "src_trianval_foi_contact_2204",
            "title": "Trianval FOI channel info@trianval.be",
            "url": "https://trianval.be/contact/",
            "publisher": "Trianval VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2204; info@trianval.be; 09 252 28 69; Biezeweg 8 9230 Wetteren",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_trianval_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +18.7% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_trianval_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +14.25% vs YE2024 {BRUTO24}; bruto≫omzet (~{RATIO}x)",
        },
        {
            "budget_id": "bud_trianval_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +91.54% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_trianval_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +5.26% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_trianval_fte_jr2025_statutory",
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
            "title": f"Trianval Wetteren YE2025 leftover dual (omzet JUMP 6.10m / bruto≫omzet ~{RATIO}x / pnl JUMP +92%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / packaging-assembly clients Oost-Vlaanderen Wetteren",
            "legal_basis": "VZW maatwerk (KBO 0419.052.074; Actief; 3 VE; RSZ NACE 88.993)",
            "decision_date": "2026-05-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0419052074/trianval",
            "stated_goal": "Sheltered employment / industrial packaging maatwerk",
            "cut_option": f"Publish NBB PDF assets/debt FOI; disclose bruto~{RATIO}x omzet loonkost matrix + pnl JUMP +92%",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Wetteren>Trianval>JR2025_statutory_L5",
            "notes": f"tick{TICK}; Medium CW; omzet primary envelope; bruto≫omzet (~{RATIO}x) + pnl JUMP +92% primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": f"Trianval omzet JUMP 6.10m / bruto≫omzet ~{RATIO}x / pnl JUMP +92% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Wetteren>Trianval>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": f"CW omzet JUMP envelope 6.10m / bruto 10.64m ≫ omzet (~{RATIO}x) / pnl JUMP 748k +92% from YE2024 391k / equity JUMP 15.15m / FTE JUMP 255.3; Wetteren maatwerk; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Wetteren / public loonkost path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +18.7%; bruto JUMP +14.3%; pnl JUMP +91.5%; equity JUMP +5.3%; FTE JUMP +2.9%",
            "absurdity_score": "7.2",
            "cost_score": "5.3",
            "difficulty": "3.0",
            "priority_index": "6.6",
            "cut_proposal": f"Publish NBB PDF assets/debt/cash FOI; disclose bruto~{RATIO}x omzet loonkost/GESCO/ESF split; pnl JUMP path",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/REW YE2024; Oost-Vlaanderen maatwerk dual after Ijsedal/Kromme Boom/Aarova",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Trianval VZW (Wetteren)",
            "name_fr": "Trianval ASBL (Wetteren)",
            "name_en": "Trianval sheltered workshop non-profit (Wetteren)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://trianval.be/",
            "foi_email": "info@trianval.be",
            "foi_postal": "Biezeweg 8, 9230 Wetteren",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0419.052.074 Actief VZW 3 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~{RATIO}x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE JUMP {FTE}; neerlegging 01.05.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>OostVlaanderen>Wetteren>Trianval>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto EUR{BRUTO} ≫ omzet EUR{OMZET} (~{RATIO}x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24} (+92%); equity JUMP EUR{EQUITY}; FTE JUMP {FTE24}->{FTE}; 3 VE cost allocation",
            "why_it_matters": f"Medium CW shows Wetteren maatwerk VZW with bruto ~{RATIO}x omzet and pnl JUMP +92% under public subsidy path while assets/debt unpublished",
            "priority": "8",
            "recipient_body": "Trianval VZW",
            "recipient_email": "info@trianval.be",
            "recipient_postal": "Biezeweg 8, 9230 Wetteren",
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
        row["title"] = f"leftover dual — Trianval YE2025 Medium (omzet JUMP 6.10m / bruto≫omzet ~{RATIO}x / pnl JUMP +92%)"
        row["notes"] = (
            "tick2204; Trianval 0419.052.074 YE2025 Medium CW; AGB Bornem JR2024; FARO/REW YE2024; "
            "next rq_2205; every-10 next 2210"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2204 missing")

if not any(r.get("task_id") == "rq_2205" for r in rows):
    rows.append(
        {
            "task_id": "rq_2205",
            "title": "leftover dual hole-fill after Trianval — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2205 after Trianval Wetteren YE2025 Medium (omzet JUMP 6.10m / bruto≫omzet ~1.74x / pnl JUMP +92% / FTE 255). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(FREE: Oesterbank/Noordheuvel/Arcor/ACG/Entiris/Odas/Kemphaan). "
                "Do NOT redo Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2204 Trianval; FARO/REW still YE2024; next every-10 2210",
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
        f"tick2204 leftover Trianval 0419.052.074 Medium (omzet JUMP 6.10m; bruto 10.64m ≫ omzet ~{RATIO}x; pnl JUMP 748k +92%; "
        "equity JUMP 15.15m; FTE JUMP 255.3; 3 VE Wetteren); AGB Bornem JR2024; FARO/REW YE2024; "
        "next rq_2205; next every-10 2210; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2204 DONE")
