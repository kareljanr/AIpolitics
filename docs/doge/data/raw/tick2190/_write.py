# tick2190 EVERY-10 + De Wroeter YE2025 Medium CW
import csv
import json
from pathlib import Path

ROOT = Path("docs/doge/data")
csv.field_size_limit(10**7)

UTC = "2026-08-26T09:20:00Z"
TICK = "2190"
ENTITY = "vzw_de_wroeter_hasselt"
SRC_EN = "src_de_wroeter_jr2025_cw_en"
COMM = "comm_de_wroeter_jr2025_statutory_maatwerk_pnl_drop_bruto_gt_omzet"
LB = "lb_de_wroeter_omzet_jump_5_06m_pnl_drop_bruto_gt_omzet_jr2025"
GAP = "gap_de_wroeter_nbb_pdf_assets_debt_pnl_drop_bruto_gt_omzet_fte_jump_matrix_l5"

OMZET = 5057412
BRUTO = 7067728
PNL = 99403
EQUITY = 3886825
FTE = 175.2
OMZET24 = 4694503
BRUTO24 = 6628572
PNL24 = 273357
EQUITY24 = 3897087
FTE24 = 161.5


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
            "source_id": "src_de_wroeter_jr2025_cw_nl",
            "title": "Companyweb NL De Wroeter Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/nl/0433138454/de-wroeter-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; YE2025 omzet JUMP {OMZET} bruto {BRUTO} pnl DROP {PNL} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 18.06.2026; raw docs/doge/data/raw/tick2190/",
        },
        {
            "source_id": SRC_EN,
            "title": "Companyweb EN De Wroeter Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/en/0433138454/de-wroeter-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; Turnover {OMZET} Profit/Loss {PNL} Equity {EQUITY} Employees {FTE}",
        },
        {
            "source_id": "src_de_wroeter_jr2025_cw_fr",
            "title": "Companyweb FR De Wroeter Maatwerkbedrijf YE2025 statutory",
            "url": "https://www.companyweb.be/fr/0433138454/de-wroeter-maatwerkbedrijf",
            "publisher": "Companyweb (NBB-derived)",
            "accessed_date": "2026-08-26",
            "source_class": "secondary_aggregator",
            "notes": f"tick{TICK}; FR mirror YE2025 Medium; Dernier bilan 2025",
        },
        {
            "source_id": "src_de_wroeter_kbo_2190",
            "title": "KBO De Wroeter Maatwerkbedrijf 0433.138.454 Actief VZW Hasselt 5 VE",
            "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0433138454",
            "publisher": "KBO FOD Economie",
            "accessed_date": "2026-08-26",
            "source_class": "official_register",
            "notes": "tick2190; Actief VZW; St.-Rochusstraat 8 3720 Hasselt; 5 VE; RSZ NACE 88.993; KBO email empty",
        },
        {
            "source_id": "src_de_wroeter_foi_contact_2190",
            "title": "De Wroeter FOI channel info@dewroeter.be",
            "url": "https://www.dewroeter.be/contact",
            "publisher": "De Wroeter Maatwerkbedrijf VZW",
            "accessed_date": "2026-08-26",
            "source_class": "foi_contact",
            "notes": "tick2190; info@dewroeter.be; St.-Rochusstraat 8 3720 Hasselt",
        },
    ],
)

append_csv(
    "budgets.csv",
    [
        {
            "budget_id": "bud_de_wroeter_omzet_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(OMZET),
            "amount_min_eur": str(OMZET),
            "amount_max_eur": str(OMZET),
            "basis": "CW statutory omzet / Turnover YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; omzet JUMP +7.73% vs YE2024 {OMZET24}",
        },
        {
            "budget_id": "bud_de_wroeter_bruto_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(BRUTO),
            "amount_min_eur": str(BRUTO),
            "amount_max_eur": str(BRUTO),
            "basis": "CW statutory bruto_marge / Gross margin YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; bruto JUMP +6.63% vs YE2024 {BRUTO24}; bruto≫omzet",
        },
        {
            "budget_id": "bud_de_wroeter_pnl_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(PNL),
            "amount_min_eur": str(PNL),
            "amount_max_eur": str(PNL),
            "basis": "CW statutory winst / Profit-Loss after tax YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; pnl DROP -63.64% vs YE2024 {PNL24}",
        },
        {
            "budget_id": "bud_de_wroeter_equity_jr2025_statutory",
            "entity_id": ENTITY,
            "year": "2025",
            "amount_eur": str(EQUITY),
            "amount_min_eur": str(EQUITY),
            "amount_max_eur": str(EQUITY),
            "basis": "CW statutory eigen_vermogen / Equity YE2025",
            "source_id": SRC_EN,
            "confidence": "medium",
            "notes": f"tick{TICK}; Medium CW; equity DROP -0.26% vs YE2024 {EQUITY24}",
        },
        {
            "budget_id": "bud_de_wroeter_fte_jr2025_statutory",
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
            "title": "De Wroeter Hasselt YE2025 leftover dual (omzet JUMP 5.06m / pnl DROP -64% / bruto≫omzet)",
            "entity_id": ENTITY,
            "beneficiary": "maatwerkers / social-economy + edible landscape clients Limburg Hasselt",
            "legal_basis": "VZW maatwerk (KBO 0433.138.454; Actief; 5 VE; RSZ NACE 88.993)",
            "decision_date": "2026-06-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": json.dumps(cash, separators=(",", ":")),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0433138454/de-wroeter-maatwerkbedrijf",
            "stated_goal": "Sheltered employment / maatwerk + edible landscape social enterprise",
            "cut_option": "Publish NBB PDF assets/debt FOI; disclose pnl DROP vs FTE JUMP + loonkostsubsidie matrix behind bruto≫omzet",
            "source_id": SRC_EN,
            "confidence": "medium",
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>DeWroeter>JR2025_statutory_L5",
            "notes": "tick2190 EVERY-10 primary; Medium CW; omzet primary envelope; pnl DROP + bruto≫omzet primary absurdity; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; named FREE after Kringwinkel Antwerpen; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "De Wroeter omzet JUMP 5.06m / pnl DROP -64% / bruto≫omzet (YE2025)",
            "level": "L5",
            "type": "maatwerk_vzw_statutory",
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>DeWroeter>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": "CW omzet JUMP envelope 5.06m / bruto 7.07m ≫ omzet / pnl DROP 99k -64% from YE2024 273k / equity flat 3.89m / FTE JUMP 175.2; wage-cost subsidies opaque; assets/debt Unknown pending NBB PDF",
            "confidence": "medium",
            "source_id": SRC_EN,
            "beneficiaries": "maatwerkers Limburg / public loonkostsubsidie path",
            "stated_goal": "Sheltered employment maatwerk",
            "measured_outcome": "omzet JUMP +7.7%; bruto JUMP +6.6%; pnl DROP -63.6%; equity DROP -0.3%; FTE JUMP +8.5%",
            "absurdity_score": "6.6",
            "cost_score": "5.0",
            "difficulty": "3.0",
            "priority_index": "5.7",
            "cut_proposal": "Publish NBB PDF assets/debt/cash FOI; disclose pnl crater vs FTE JUMP; loonkostsubsidie/GESCO/ESF split",
            "status": "open",
            "struck_reason": "",
            "notes": f"tick{TICK} EVERY-10 primary; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; Limburg maatwerk dual after Kringwinkel Antwerpen/Blankedale",
        }
    ],
)

append_csv(
    "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "De Wroeter Maatwerkbedrijf VZW (Hasselt)",
            "name_fr": "De Wroeter entreprise de travail adapté ASBL (Hasselt)",
            "name_en": "De Wroeter sheltered workshop non-profit (Hasselt)",
            "level": "parastatal",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.dewroeter.be/",
            "foi_email": "info@dewroeter.be",
            "foi_postal": "St.-Rochusstraat 8, 3720 Hasselt",
            "notes": f"tick{TICK} EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0433.138.454 Actief VZW 5 VE RSZ NACE 88.993; omzet JUMP {OMZET} bruto {BRUTO} (≫omzet) pnl DROP {PNL} vs YE2024 {PNL24} equity DROP {EQUITY} FTE JUMP {FTE}; neerlegging 18.06.2026; assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
        }
    ],
)

append_csv(
    "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Vlaanderen>Limburg>Hasselt>DeWroeter>NBB_PDF_assets_debt_pnl_drop",
            "entity_id": ENTITY,
            "what_is_missing": f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash/balanstotaal); pnl DROP EUR{PNL} vs YE2024 EUR{PNL24} (-63.64%) recon; bruto EUR{BRUTO} ≫ omzet EUR{OMZET} loonkostsubsidie/GESCO/ESF/VDAB matrix; FTE JUMP {FTE24}→{FTE} with pnl DROP path; 5 VE cost allocation",
            "why_it_matters": "Medium CW shows Limburg maatwerk VZW with pnl crater -64% while FTE JUMPS +8.5% and bruto≫omzet — assets/debt unpublished under public loonkost path",
            "priority": "8",
            "recipient_body": "DE WROETER MAATWERKBEDRIJF VZW",
            "recipient_email": "info@dewroeter.be",
            "recipient_postal": "St.-Rochusstraat 8, 3720 Hasselt",
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
            "notes": f"tick{TICK} EVERY-10; ready NOT sent; Medium CW + Strong KBO; next every-10 2200",
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
    if row.get("task_id") == "rq_2190":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["title"] = "EVERY-10 + leftover dual — De Wroeter YE2025 Medium (omzet JUMP 5.06m / pnl DROP -64%)"
        row["notes"] = (
            "tick2190 EVERY-10; De Wroeter 0433.138.454 YE2025 Medium CW; progress+top10 refreshed; "
            "AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; next rq_2191; every-10 next 2200"
        )
        found = True
        break
if not found:
    raise SystemExit("rq_2190 missing")

if not any(r.get("task_id") == "rq_2191" for r in rows):
    rows.append(
        {
            "task_id": "rq_2191",
            "title": "leftover dual hole-fill after De Wroeter — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS-HVZ",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2191 after De Wroeter Hasselt YE2025 Medium (omzet JUMP 5.06m / pnl DROP -64% / bruto≫omzet / FTE JUMP 175). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused IGS/DSO/water/nuclear/HVZ/WZC/MRS "
                "(Demival/Mivas FREE). "
                "Do NOT redo De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2190 EVERY-10 De Wroeter; FARO/AIESH/REW still YE2024; next every-10 2200",
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("research_queue rq_2190=done rq_2191=open")

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
    "last_unit_id": "rq_2190",
    "ticks_completed": "2190",
    "paused": "no",
    "notes": (
        "tick2190 EVERY-10 leftover DE WROETER 0433.138.454 Medium (omzet JUMP 5.06m; bruto 7.07m ≫ omzet; pnl DROP 99k -64% from 273k; "
        "equity flat 3.89m; FTE JUMP 175.2; 5 VE Hasselt); progress+top10 refreshed; AGB Bornem JR2024; FARO YE2024; AIESH/REW stall; "
        "next rq_2191; next every-10 2200; continuous hole_fill"
    ),
}
with ls_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2190 DONE")
