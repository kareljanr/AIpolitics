# tick2195 writer — Kunnig Operations YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T11:00:00Z"
TICK = "2195"
ENTITY = "vzw_kunnig_operations_antwerpen"
SRC_EN = "src_kunnig_ops_jr2025_cw_en"
COMM = "comm_kunnig_ops_jr2025_statutory_maatwerk_bruto_gt_omzet"
LB = "lb_kunnig_ops_omzet_jump_4_35m_bruto_gt_omzet_jr2025"
GAP = "gap_kunnig_ops_nbb_pdf_assets_debt_bruto_gt_omzet_holding_matrix_l5"

OMZET = 4345803
BRUTO = 8476863
PNL = 345461
EQUITY = 9921695
FTE = 241.1
OMZET24 = 4090159
BRUTO24 = 8186046
PNL24 = 232063
EQUITY24 = 9641832
FTE24 = 242.6


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
            "source_id": "src_kunnig_ops_jr2025_cw_nl",
            "title": "Companyweb NL Kunnig Operations YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0404745465/kunnig-operations",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} FTE DROP {FTE}; neerlegging 08.06.2026; raw docs/doge/data/raw/tick2195/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN Kunnig Operations YE2025 statutory",
            "url": "https://www.companyweb.be/en/0404745465/kunnig-operations",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 08-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_kunnig_ops_jr2025_cw_fr",
            "title": "Companyweb FR Kunnig Operations YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0404745465/kunnig-operations",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025; Chiffre d affaires {OMZET}",
        },
        {
            "source_id": "src_kunnig_ops_kbo_2195",
            "title": "KBO Kunnig Operations 0404.745.465 Actief VZW Antwerpen 2 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0404745465",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2195; Actief VZW; Kielsbroek 2 2020 Antwerpen; 2 VE; RSZ NACE 88.993; 11 functiehouders; absorbed BW-Arbeid-Vrede 0445.576.428 (2023); daily management via holding 0627.884.760",
        },
        {
            "source_id": "src_kunnig_ops_foi_contact_2195",
            "title": "Kunnig FOI channel info@kunnig.be",
            "url": "https://www.kunnig.be/contact",
            "publisher": "Kunnig VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2195; info@kunnig.be; +32 3 248 48 11; Kielsbroek 2 2020 Antwerpen",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_kunnig_ops_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +6.25% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_kunnig_ops_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +3.55% vs YE2024 {BRUTO24}; bruto≫omzet ~1.95x",
        },
        {
            "budget_id": "bud_kunnig_ops_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl JUMP +48.87% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_kunnig_ops_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity JUMP +2.9% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_kunnig_ops_fte_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(FTE),
            "amount_min_eur": str(FTE),
            "amount_max_eur": str(FTE),
            "basis": f"CW social-balance FTE / Employees {FTE}",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; FTE DROP vs YE2024 {FTE24}; assets/debt Unknown; holding 0627.884.760 separate",
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
            "title": "Kunnig Operations Antwerpen YE2025 leftover dual (omzet JUMP 4.35m / bruto≫omzet ~1.95x / pnl JUMP +49%)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy clients Antwerpen",
            "legal_basis": "VZW maatwerk (KBO 0404.745.465; Actief; 2 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-08",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0404745465/kunnig-operations",
            "stated_goal": "Sheltered employment / maatwerk for hard-to-place workers",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose bruto≫omzet loonkostsubsidie matrix + dual holding 0627.884.760 LOSS/equity collapse",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Antwerpen>KunnigOperations>JR2025_statutory_L5",
            "notes": "tick2195; Medium CW; omzet primary envelope; bruto≫omzet ~1.95x primary absurdity; pnl JUMP; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; deferred BWZ/De Schakel/BosKat/AGE; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "Kunnig Operations omzet JUMP 4.35m / bruto≫omzet ~1.95x / pnl JUMP +49% (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Antwerpen>KunnigOperations>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 4.35m / bruto 8.48m ≫ omzet ~1.95x / pnl JUMP 345k +49% from YE2024 232k / equity JUMP 9.92m / FTE DROP 241.1 from 242.6; wage-cost subsidies opaque; dual holding 0627.884.760; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Antwerpen / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +6.3%; bruto JUMP +3.6%; pnl JUMP +48.9%; equity JUMP +2.9%; FTE DROP -0.6%",
            "absurdity_score": "6.8",
            "cost_score": "5.0",
            "difficulty": "3.0",
            "priority_index": "5.7",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet loonkostsubsidie/GESCO/ESF split; holding LOSS matrix",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK}; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Antwerpen maatwerk dual after Forena/A-kwadraat",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "Kunnig Operations VZW (Antwerpen)",
            "name_fr": "Kunnig Operations ASBL (Anvers)",
            "name_en": "Kunnig Operations sheltered workshop non-profit (Antwerp)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.kunnig.be/",
            "foi_email": "info@kunnig.be",
            "foi_postal": "Kielsbroek 2, 2020 Antwerpen",
            "notes": f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0404.745.465 Actief VZW 2 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet ~1.95x) pnl JUMP {PNL} vs YE2024 {PNL24} equity JUMP {EQUITY} FTE DROP {FTE} from {FTE24}; neerlegging 08.06.2026; dual holding Kunnig 0627.884.760; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Antwerpen>KunnigOperations>NBB_PDF_assets_debt_bruto_gt_omzet",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); bruto JUMP EUR{BRUTO} ≫ omzet EUR{OMZET} (~1.95x) loonkostsubsidie/GESCO/ESF/VDAB/gemeente matrix; pnl JUMP EUR{PNL} vs YE2024 EUR{PNL24}; dual holding 0627.884.760 LOSS/equity collapse recon; 2 VE cost allocation",
            "why_it_matters": "Medium CW shows Antwerpen maatwerk VZW with bruto ~1.95x omzet under public loonkost path while assets/debt unpublished; dual holding structure opaque",
            "priority": "8",
            "recipient_body": "Kunnig Operations VZW",
            "recipient_email": "info@kunnig.be",
            "recipient_postal": "Kielsbroek 2, 2020 Antwerpen",
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
    if row.get("task_id") == "rq_2195":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = (
            "leftover dual — Kunnig Operations YE2025 Medium "
            "(omzet JUMP 4.35m / bruto≫omzet ~1.95x / pnl JUMP +49%)"
        )
        row["notes"] = (
            "tick2195; Kunnig Operations 0404.745.465 YE2025 Medium CW; AGB Bornem JR2024; "
            "FARO YE2024; AIESH/REW stall; deferred BWZ/De Schakel/BosKat/AGE; "
            "next rq_2196; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2195 missing")

if not any(r.get("task_id") == "rq_2196" for r in rows):
    rows.append(
        {
            "task_id": "rq_2196",
            "title": "leftover dual hole-fill after Kunnig Ops — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2196 after Kunnig Operations Antwerpen YE2025 Medium "
                "(omzet JUMP 4.35m / bruto≫omzet ~1.95x / pnl JUMP +49%). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(BWZ Zottegem / De Schakel Balen / BosKat / Atelier Groot Eiland FREE). "
                "Do NOT redo Kunnig Operations, Forena, A-kwadraat, SW-WEB, Mivas, Demival, "
                "De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, "
                "Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, "
                "Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, "
                "Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, "
                "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
                "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2195 Kunnig Ops; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2195=done rq_2196=open")

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
    "last_unit_id": "rq_2195",
    "ticks_completed": "2195",
    "paused": "no",
    "notes": (
        "tick2195 leftover Kunnig Operations 0404.745.465 Medium (omzet JUMP 4.35m; "
        "bruto 8.48m ≫ omzet ~1.95x; pnl JUMP 345k +49%; equity JUMP 9.92m; FTE DROP 241.1; "
        "2 VE Antwerpen); AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2196; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2195 DONE")
